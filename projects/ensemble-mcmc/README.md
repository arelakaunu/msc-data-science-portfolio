# Ensemble MCMC and parallel Bayesian inference

**Bayesian computation · Numerical methods · Parallel experiments · May 2025**

An educational exploration of ensemble sampling: a manual stretch move, an `emcee` implementation, and independent Ray tasks for Bayesian logistic regression on synthetic classification data.

[Open the notebook](ensemble-mcmc.ipynb).

## What the experiment demonstrates

- Ensemble proposals on a strongly correlated two-dimensional Gaussian.
- Library-based sampling and posterior summaries.
- Parallel independent ensemble runs with different random seeds.
- Trace/acceptance/autocorrelation diagnostics and a corner plot.
- An optional toy model/likelihood abstraction inspired by CosmoHammer.

The mock is not a cosmology implementation. Local Ray tasks are not evidence of a cloud deployment or a speedup benchmark.

## Run

```sh
python -m venv .venv
# Activate the environment using the command for your shell.
python -m pip install -r requirements.txt
python -m jupyterlab
```

Open the notebook from this directory and execute in order. No external dataset or cloud account is needed. Ray starts local workers. Resource needs depend on the number of chains and walkers; defaults launch four ensemble runs. Stop the kernel or run `ray.shutdown()` after use.

## Corrections and boundaries

The submission sampled the manual stretch factor uniformly, which did not match the stretch acceptance formula. The portfolio uses the transformed uniform draw for a density proportional to `z**(-1/2)`, consistent with the [emcee reference implementation](https://github.com/dfm/emcee/blob/main/src/emcee/moves/stretch.py). Class definitions broken across notebook cells have been reunited. The logistic log-likelihood uses `logaddexp` for numerical stability. Historical outputs were cleared because the code changed.

The final predictive example remains exploratory: it generates a separate classification problem for testing and computes scaling from already-standardised training data. Its accuracy should not be treated as a valid held-out generalisation estimate. A proper follow-up would split a single generated dataset, retain training scaling parameters, and assess predictive uncertainty on that held-out split. Short-chain autocorrelation estimates do not establish convergence, especially when `tol=0` suppresses the length check.

The from-scratch sampler was checked against the known covariance of its Gaussian target during preparation. Full `emcee`, Ray, and plotting execution was not performed. See [VALIDATION.md](../../VALIDATION.md).

## References in the coursework

Goodman & Weare (2010), *Ensemble Samplers with Affine Invariance*; Foreman-Mackey et al. (2013), *emcee: The MCMC Hammer*; Akeret et al. (2013), *CosmoHammer*. The source notebook explicitly credits these methods.
