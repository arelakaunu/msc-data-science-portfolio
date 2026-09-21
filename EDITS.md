# Portfolio preparation record

The original ZIP was retained unchanged. Only selected copies were prepared for publication. Source filenames and SHA-256 hashes are recorded in provenance.json.

## Presentation and privacy

- Added portfolio navigation, individual project READMEs, setup notes, requirements files, and limitations.
- Renamed notebooks into readable filenames and an execution order.
- Removed notebook machine metadata, raw text/HTML logs, installation logs, and error outputs. HAR chart images remain and are explicitly labelled as historical outputs.
- Removed all embedded Reddit credentials and replaced them with environment-variable lookups. No secret is included in the publication history.
- Normalised PDF metadata while retaining original report pages, citations, and disclosures.
- Omitted course-provided teaching materials, raw data, and redundant submissions.

## Small code changes

| Project | Change | Why |
|---|---|---|
| HAR | Added GBM plotting imports and derived labels from fitted model classes | Avoid undefined names in a fresh kernel |
| HAR | Corrected RF identifier CSV path | Match feature engineering output |
| HAR | Removed automatic Kaggle submission | Keep running a portfolio notebook from submitting externally |
| Reddit | Read credentials from environment | Avoid publishing or embedding secrets |
| Reddit | Use the batch function's `limit` argument | Original parameter was ignored |
| Reddit | Align CSV filenames and make dashboard paths relative; show missing-data message | Allow notebook/dashboard handoff on another computer |
| Reddit | Align Spark schema with CSV field order, read headers, separate input/output directories | Prevent schema mismatch and ingesting its own output |
| MCMC | Reunite methods split from their classes | Fix cell-level indentation and missing methods |
| MCMC | Correct manual stretch-factor sampling | Match proposal distribution to acceptance formula |
| MCMC | Use `logaddexp(0, logits)` | Avoid overflow in logistic likelihood |
| MCMC | Replace notebook pip commands with setup notes and qualify production/cloud language | Keep installation explicit and claims evidence-based |
| R simulation | Set seed, use HTML output, replace copied questions with section headings | Improve repeatability and standalone presentation |
| R simulation | Remove the contradicted “below 0.01” conclusion | Avoid repeating a claim unsupported by the submitted tables |

Reddit and MCMC outputs were cleared because the code changed. The statistical methods, modelling experiments, feature extraction approach, and original report prose were not broadly rewritten. Known remaining limitations are explained in each README. No model retraining, new performance claims, cloud deployment, or missing dissertation code has been added.
