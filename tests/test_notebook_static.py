import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def notebook_source(filename):
    notebook = json.loads((ROOT / filename).read_text(encoding="utf-8"))
    return "\n".join(
        "".join(cell.get("source", [])) if isinstance(cell.get("source", []), list)
        else cell.get("source", "")
        for cell in notebook.get("cells", [])
        if cell.get("cell_type") == "code"
    )


def test_training_notebook_code_compiles():
    source = notebook_source("model_trainer.ipynb")
    compile(source, "model_trainer.ipynb", "exec")


def test_threshold_is_selected_on_validation_not_test():
    source = notebook_source("model_trainer.ipynb")
    assert "find_optimal_threshold_for_recall(\n        y_val, y_val_scores" in source
    assert "find_optimal_threshold_for_recall(\n        y_test" not in source
    assert "test_size=0.20" in source
    assert "test_size=0.25" in source


def test_inference_selects_spam_probability_by_label():
    source = notebook_source("spam_detector.ipynb")
    assert "self.spam_probability_index = classes.index('spam')" in source
    assert "[:, self.spam_probability_index]" in source
    assert "[:, 1]" not in source


def test_notebooks_have_no_saved_code_outputs():
    for filename in ("model_trainer.ipynb", "spam_detector.ipynb"):
        notebook = json.loads((ROOT / filename).read_text(encoding="utf-8"))
        for cell in notebook.get("cells", []):
            if cell.get("cell_type") == "code":
                assert cell.get("execution_count") is None
                assert cell.get("outputs", []) == []



def test_threshold_helper_enforces_recall_constraint_and_validates_inputs():
    source = notebook_source("model_trainer.ipynb")
    helper_start = source.index("def find_optimal_threshold_for_recall")
    helper_end = source.index("\ndef plot_precision_recall_tradeoff", helper_start)
    helper = source[helper_start:helper_end]
    assert "if not 0.0 <= target_recall <= 1.0" in helper
    assert "len(y_true) != len(y_proba)" in helper
    assert "recalls[:-1] >= target_recall" in helper
    assert "best_indices[-1]" in helper
    assert "np.argmin(np.abs(recalls - target_recall))" not in helper


def test_training_notebook_does_not_claim_production_readiness_or_store_secrets():
    source = notebook_source("model_trainer.ipynb")
    assert "Production ready" not in source
    assert "ADMIN_SPAM_2024" not in source
    notebook = json.loads((ROOT / "model_trainer.ipynb").read_text(encoding="utf-8"))
    serialized = json.dumps(notebook, ensure_ascii=False)
    assert "ADMIN_SPAM_2024" not in serialized
