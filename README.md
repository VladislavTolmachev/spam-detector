# SMS Spam Detection

An educational machine-learning project for binary classification of SMS messages as `spam` or `ham`.

I built the first version while learning ML, over roughly two weeks of evening work. The project explores a classic text-classification workflow rather than claiming to be a production service.

## What the project explores

- Text preprocessing with regular expressions
- TF-IDF features, including unigrams, bigrams, and trigrams
- Logistic Regression for binary classification
- Class imbalance and a simple keyword-based baseline
- Precision, recall, F1, Average Precision, and threshold selection
- Probability calibration with scikit-learn

## Dataset

The notebooks use the UCI SMS Spam Collection dataset (5,572 messages before duplicate handling). If `SMSSpamCollection` is present in the repository root, the training notebook reads it from there. Otherwise, obtain it from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/228/sms+spam+collection) and place the extracted file in the project root. Check the dataset's terms and attribution requirements before redistributing it.


## Getting started

Use a virtual environment, then install the listed dependencies:

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

python -m pip install --upgrade pip
pip install -r requirements.txt
```

Open `model_trainer.ipynb` in Jupyter and run its cells in order. The notebook contains the training and evaluation workflow. `spam_detector.ipynb` is an early prototype of a command-line inference wrapper and may refer to artifacts/modules that are not part of the current repository; it is retained as a record of the first implementation, not as a supported CLI.

## Important limitations

- The training notebook now uses a stratified 60/20/20 train/validation/test split. The decision threshold is selected on validation data, and the test split is used for final evaluation after that threshold is fixed.
- Calibration uses sigmoid calibration around the full text Pipeline. Its quality has not yet been independently verified with Brier score, log loss, or a reliability diagram.
- The notebook is an educational experiment and has not been validated for production use. The revised workflow has not yet been executed end-to-end in a clean environment.
- No deployment, API service, monitoring, or automated retraining pipeline is included.

## Learning notes

See [the Russian project walkthrough](docs/PROJECT_WALKTHROUGH_RU.md) for explanations of preprocessing, TF-IDF, Logistic Regression, class imbalance, evaluation metrics, thresholds, and calibration.

## Possible next improvements

1. Separate training, evaluation, and prediction into small Python modules.
2. Run the updated training workflow end-to-end in a clean environment and fix any runtime issues.
3. Add calibration evaluation (Brier score, log loss, reliability diagram) and a small set of tests.
4. Compare alternative models and calibration methods using validation data only.
5. Document reproducible dataset setup and tested dependency versions.

## License and attribution

Check the dataset's own terms and add an explicit project license before reusing or redistributing the code.
