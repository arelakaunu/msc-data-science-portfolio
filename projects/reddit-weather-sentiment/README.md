# Extreme weather discussions on Reddit

**Data collection · Sentiment analysis · Streaming prototype · December 2024**

A coursework pipeline for collecting weather-related Reddit posts and comments, analysing polarity with TextBlob, and presenting batch insights through Streamlit.

## What is included

- [Batch notebook](01-batch-collection.ipynb): keyword-based collection, keyword columns, sentiment labels, and CSV exports.
- [Streaming notebook](02-streaming.ipynb): periodic Reddit polling into CSV files, then Spark Structured Streaming ingestion and output.
- [Dashboard](dashboard.py): sentiment by keyword group, polarity distribution, keyword filtering, and post/comment comparisons.

The live notebook demonstrates polling plus file streaming. The dashboard reads batch CSVs; it is not a live connection to Spark. No throughput or production-scale claims are made.

## Setup

```sh
python -m venv .venv
# Activate the environment using the command for your shell.
python -m pip install -r requirements.txt
python -m jupyterlab
```

Run notebooks from this directory. Set `REDDIT_CLIENT_ID`, `REDDIT_CLIENT_SECRET`, and `REDDIT_USER_AGENT` in your process environment before starting Jupyter. [.env.example](.env.example) lists the variable names; it is a template and is not automatically loaded. Never commit real credentials.

The batch notebook writes `clean_eco.csv` and `sentiment_and_text_eco.csv` here. After collection, run:

```sh
python -m streamlit run dashboard.py
```

No original Reddit data was supplied. The dashboard explains which files are missing until you generate them. API access is a prerequisite; the portfolio does not include credentials or guarantee access to Reddit.

For streaming, a Java runtime compatible with your installed PySpark version is also required. The notebook polls every 120 seconds and waits indefinitely for the stream; interrupt the kernel when finished. Raw files go to `reddit_stream_output/`; processed files go to `reddit_stream_processed/`, with checkpoints in `checkpoint_dir/`.

## Interpretation and limitations

Keyword sampling is not representative of public opinion. TextBlob polarity can misread sarcasm and context. The original dashboard maps exact keyword strings to groups, so rows with several comma-separated keywords may be omitted from that comparison. Joining by content can duplicate records with repeated text; missing polarity currently falls into the neutral branch. These limitations are retained and documented rather than silently redesigning the analysis.

The streaming prototype writes CSV directly, polls a bounded recent-post window, and does not maintain durable comment-level deduplication. It can miss events or ingest partial/duplicate records and is not production-ready. Live access, Spark execution, and sentiment quality were not validated during portfolio preparation.

The embedded credentials were removed, absolute dashboard paths were replaced, the batch limit now takes effect, output names were aligned with the dashboard, and the Spark schema/header and output directory were corrected. Original report screenshots of social posts are not redistributed.
