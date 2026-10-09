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
