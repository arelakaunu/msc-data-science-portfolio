# Exploring multivariate datasets

**Exploratory analysis · Statistical modelling · Visual communication · January 2025**

[Read the original report](report.pdf).

This report explores four datasets with different variable types and analytical questions:

| Dataset | Analysis in the report |
|---|---|
| Glass identification | Pairwise oxide comparisons, regression/ANOVA and multinomial modelling |
| El Niño | Air/sea temperature relationships and geographic variation |
| Adult census income | Categorical and continuous relationships with income class; sparse categories and separation |
| Dow Jones index | Exploratory comparisons of weekly price and volume changes |

The report demonstrates R-based visualisation, model comparison, and written interpretation. For example, it reports an air/sea temperature correlation of approximately 0.94 in the analysed records.

## Scope and limitations

The archive contained the report with selected R listings, but no standalone analysis scripts or source datasets. It is included as a communication case study rather than a runnable application. Dataset references appear in the original bibliography.

The report is preserved as submitted. Some interpretations need qualification: a small AIC difference does not establish a uniquely best model, removing sparse categories changes the population represented, and temperature observations can have spatial and temporal dependence. The Dow Jones section is exploratory and does not demonstrate an out-of-sample forecasting strategy. The original analysis has not been rerun.
