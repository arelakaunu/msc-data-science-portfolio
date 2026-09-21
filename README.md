# Arel Akaunu | Data Science Portfolio

Selected work from my MSc Data Science at Liverpool John Moores University. These projects cover statistical inference, machine learning, signal processing, data collection, and communicating results.

## Start here

| Project | What I investigated or built | Evidence and tools |
|---|---|---|
| **[Squash ratings and behavioural effects](projects/squash-ratings/)** | Whether fatigue and mismatched opponents change performance relative to rating expectations | Dissertation; 237,114 paired player-days and 3.83 million matches in the reported analyses |
| **[Human activity recognition](projects/human-activity-recognition/)** | Classifying six activities from accelerometer signals using engineered features | Five Python notebooks, original report; pandas, SciPy, scikit-learn |
| **[Extreme weather sentiment on Reddit](projects/reddit-weather-sentiment/)** | Collecting discussions, scoring sentiment, and displaying batch insights | PRAW, TextBlob, Spark Structured Streaming, Streamlit, Plotly |
| **[Ensemble MCMC](projects/ensemble-mcmc/)** | Exploring stretch moves, Bayesian logistic regression, and parallel chains | Python notebook; NumPy, emcee, Ray |
| **[Statistical test power](projects/statistical-test-power/)** | Comparing false positives and detection power across distributions and sample sizes | R Markdown simulations; Shapiro-Wilk, KS, Anderson-Darling |
| **[Multivariate data analysis](projects/multivariate-analysis/)** | Exploring glass composition, ocean temperatures, census income, and stock data | Original analytical report with R code listings and visualisations |

## What this portfolio represents

The analyses and experiments originate in my coursework. Preparation for GitHub added navigation, project descriptions, setup guidance, privacy cleanup, and a small number of documented fixes. Original report pages are retained, including their original AI-use disclosures. No new model scores or historical results have been invented.

Each project explains its question, approach, evidence, and limitations. Some are code projects; the dissertation and multivariate analysis are explicitly presented as report-based case studies because standalone analysis code was absent from the submission archive.

## Reproduction

Open a project README before running anything. Python projects have separate `requirements.txt` files, inferred from their imports rather than recovered lockfiles. Use a separate virtual environment for each project. Dependencies are not pinned to an unverified historical environment.

The activity-recognition datasets and Reddit collection outputs were not included in the archive. The R simulation generates its own data. MCMC uses synthetic data. Live Reddit collection requires your own API access and can run continuously.

See [VALIDATION.md](VALIDATION.md) for checks actually performed, [EDITS.md](EDITS.md) for changes, and [DATA_AND_ATTRIBUTION.md](DATA_AND_ATTRIBUTION.md) for data and authorship boundaries.
