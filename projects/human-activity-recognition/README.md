# Human activity recognition from accelerometer signals

**Machine learning · Signal processing · Feature engineering · April 2025**

Classify walking, jogging, sitting, standing, upstairs, and downstairs from tri-axial accelerometer data. The main challenge was distinguishing similar movement patterns while handling imbalanced activity classes.

[Read the original report](report.pdf) or start with [feature engineering](02-feature-engineering.ipynb).

## Approach

1. Inspect class frequencies and supplied summary features.
2. Apply a high-pass filter to reduce the low-frequency gravity contribution.
3. Engineer statistical, spectral, wavelet, and exploratory nonlinear features for each signal snippet.
4. Inspect feature structure using t-SNE.
5. Compare gradient boosting with a random forest using SMOTE and a parameter search.

## Historical results

| Model | Accuracy recorded in submitted notebook | Context |
|---|---|---|
| Gradient boosting | 91.00% | 1,934 test examples; macro F1 approximately 0.83 |
| Tuned random forest | 88.99% | 1,934 test examples; weighted F1 0.8831 |

The written report rounds the GBM result to 90% and RF to 89%; the table above uses notebook outputs. The report also discusses a CNN at approximately 81%, but no CNN implementation was present in the supplied files, so it is not represented as included code. These are historical measurements, not independently reproduced scores.

## Files and execution order

Run Jupyter from this directory so the relative paths resolve:

```sh
python -m venv .venv
# Activate the environment using the command for your shell.
python -m pip install -r requirements.txt
python -m jupyterlab
```

1. [01-preprocessing.ipynb](01-preprocessing.ipynb): create baseline feature/label files in `data-prep/`.
2. [02-feature-engineering.ipynb](02-feature-engineering.ipynb): extract new signal features into `data-preprocess/new/`.
3. [03-eda.ipynb](03-eda.ipynb): explore baseline and engineered features.
4. [04-gradient-boosting.ipynb](04-gradient-boosting.ipynb): train and evaluate GBM.
5. [05-random-forest.ipynb](05-random-forest.ipynb): train, tune, and evaluate RF.

Required inputs in `data/` are `metadata.csv`, `metadata_test.csv`, `metadata_kaggle.csv`, `signals.csv`, `signals_test.csv`, and `signals_kaggle.csv`. Metadata needs `user_snippet` and supplied features; training/test metadata also need `activity`. Signals need `user_snippet`, `x-axis`, `y-axis`, and `z-axis`. Use the original authorised coursework data and splits. None of these inputs was in the archive; the prediction-only CSV is insufficient to reconstruct them.

## Limitations and next steps

The original experiments are preserved rather than redesigned. Test and competition missing values are imputed using their own column means. RF scaling and SMOTE happen before cross-validation, which can make the cross-validation score optimistic. A follow-up should put learned preprocessing and oversampling inside each training fold, and use only training-fitted transforms on held-out data ([scikit-learn guidance](https://scikit-learn.org/dev/common_pitfalls.html)).

Subject-level separation cannot be confirmed from the archived files. The nonlinear feature implementations are exploratory and need separate validation, and feature expansion assumes consistent vector lengths across snippets. High AUROC alone does not prove overfitting, despite that interpretation in the original report. The retained plots document the submission; they do not establish deployment readiness.

Portfolio fixes are limited to missing plotting imports, an undefined label variable, a prediction identifier path, notebook navigation, and removal of automatic competition submission. See [EDITS.md](../../EDITS.md).
