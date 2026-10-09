# SMS Spam Detection

An educational machine-learning project for binary classification of SMS messages as `spam` or `ham`.

I built the first version while learning ML, over roughly two weeks of evening work. The project explores a classic text-classification workflow rather than claiming to be a production service.

## What the project explores

- Text preprocessing with regular expressions
- TF-IDF features, including unigrams and bigrams
- Logistic Regression for binary classification
- Class imbalance and a simple keyword-based baseline
- Precision, recall, F1, Average Precision, and threshold selection
- Probability calibration with scikit-learn

## Dataset

The notebooks use the UCI SMS Spam Collection dataset (5,572 messages before duplicate handling). The dataset is not committed to this repository. Obtain it from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/228/sms+spam+collection) and place the extracted `SMSSpamCollection` file in the project root, unless you update the notebook's data path.

Please check the dataset's terms and attribution requirements before redistributing it.

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

- The original notebook's threshold-selection workflow used test predictions to choose a threshold. That means the reported test metrics are not an unbiased final evaluation. A proper revision should split data into train, validation, and test sets, select the threshold on validation data, and evaluate once on the untouched test set.
- Calibration should be assessed with appropriate metrics/plots rather than assumed from using a calibration class.
- The original notebook contains exploratory experiments and should not be described as production-ready.
- No deployment, API service, monitoring, or automated retraining pipeline is included.

## Learning notes

See [the Russian project walkthrough](docs/PROJECT_WALKTHROUGH_RU.md) for explanations of preprocessing, TF-IDF, Logistic Regression, class imbalance, evaluation metrics, thresholds, and calibration.

## Possible next improvements

1. Separate training, evaluation, and prediction into small Python modules.
2. Add train/validation/test evaluation and threshold selection without test leakage.
3. Compare the keyword baseline with a simple TF-IDF + Logistic Regression baseline.
4. Add calibration evaluation and a small set of tests.
5. Document reproducible dataset setup and tested dependency versions.

## License and attribution

Check the dataset's own terms and add an explicit project license before reusing or redistributing the code.
