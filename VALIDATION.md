# Validation during portfolio preparation

Checks performed on 21 September 2026:

- Parsed all 75 Python code cells in eight published notebooks and the dashboard with Python AST parsing.
- Parsed all extracted R code chunks with R 4.4.1.
- Executed reduced Shapiro-Wilk and Kolmogorov-Smirnov simulations (100 trials per condition); both completed. The full original workload was not rerun, and Anderson-Darling was not executed because kSamples was unavailable.
- Executed the corrected manual MCMC sampler on its known correlated Gaussian target with 24 walkers and 8,000 steps, discarding 1,000 steps. The sample mean was approximately (−0.0052, −0.0083); covariance approximately [[0.2487, 0.2436], [0.2436, 0.2486]], close to the analytic [[0.2525, 0.2475], [0.2475, 0.2525]]. Also checked the narrow-axis variance and reunited mock likelihood methods. This is a targeted regression check, not proof of general convergence.
- Scanned every publication file for the exact credential values discovered in the source notebooks: no matches.
- Checked selected report text for credential and student-ID markers; none were found. PDF metadata was normalised.
- Checked local Markdown links and publication file inventory.

Not executed: HAR preprocessing/training (data absent), live Reddit requests, Spark streaming, Streamlit rendering, full emcee/Ray/plotting workflows, or dissertation replication. Notebook syntax checks do not establish end-to-end runtime correctness. Requirements lists are inferred and are not installed or version-locked environments. Retained HAR figures and report results are historical.
