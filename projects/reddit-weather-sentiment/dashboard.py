from pathlib import Path

import streamlit as st
import pandas as pd
import plotly.express as px

# File paths for batch data
clean_cyber_path = Path(__file__).parent / 'clean_eco.csv'
sentiment_and_text_path = Path(__file__).parent / 'sentiment_and_text_eco.csv'

# Load datasets
if not clean_cyber_path.exists() or not sentiment_and_text_path.exists():
    st.info("Run 01-batch-collection.ipynb from this directory to create the two input CSVs. See README.md.")
    st.stop()

clean_cyber_df = pd.read_csv(clean_cyber_path)
sentiment_and_text_df = pd.read_csv(sentiment_and_text_path)

# Set page title
st.title("Extreme Weather Event Sentiment Analysis - Batch Data Insights")
st.markdown("This dashboard analyses sentiment from extreme weather event-related social media posts.")

# Define keywords and groupings
keywords_eco = [
    "extreme weather", "severe weather", "weather emergency", 
    "natural disaster", "hurricane", "cyclone", 
    "typhoon", "flood", "wildfire", "disaster relief"
]
general_keywords = {"extreme weather", "severe weather", "weather emergency", "natural disaster", "disaster relief"}
specific_keywords = {"hurricane", "cyclone", "typhoon", "flood", "wildfire"}

# Map keywords into general and specific groups
def map_keyword_group(keyword):
    if keyword in general_keywords:
        return "General"
    elif keyword in specific_keywords:
        return "Specific"
    return None

clean_cyber_df["keyword_group"] = clean_cyber_df["keywords"].apply(map_keyword_group)

# Merge with sentiment data
merged_df = pd.merge(clean_cyber_df, sentiment_and_text_df[["content", "polarity"]], on="content", how="left")

# Add a sentiment label column
def assign_sentiment_label(polarity):
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

merged_df["sentiment"] = merged_df["polarity"].apply(assign_sentiment_label)

# Group by keyword group and sentiment
grouped_sentiment = merged_df.groupby(["keyword_group", "sentiment"]).size().reset_index(name="count")

# Section 1: Sentiment by Keyword Group
st.subheader("1. Sentiment Analysis by Keyword Group")
fig = px.bar(
    grouped_sentiment, 
    x="keyword_group", 
    y="count", 
    color="sentiment", 
    barmode="group",
    title="Sentiment Distribution by Keyword Group",
    labels={"keyword_group": "Keyword Group", "count": "Count"},
    template="plotly_white"
)
st.plotly_chart(fig)

# Section 2: Sentiment Polarity Distribution
st.subheader("2. Sentiment Polarity Distribution")
fig1 = px.histogram(sentiment_and_text_df, x="polarity", nbins=20, color="sentiment",
                    title="Sentiment Polarity Analysis",
                    labels={"polarity": "Polarity", "count": "Frequency"},
                    template="plotly_dark")
st.plotly_chart(fig1)

# Section 3: Top Keywords
st.subheader("3. Filter by Keyword in Extreme Weather Event Discussions")
unique_keywords = clean_cyber_df["keywords"].dropna().unique()
selected_keyword = st.selectbox("Choose a keyword to filter data:", options=unique_keywords)
filtered_data = clean_cyber_df[clean_cyber_df["keywords"] == selected_keyword]

if not filtered_data.empty:
    keyword_counts = filtered_data["keywords"].value_counts()
    fig2 = px.bar(x=keyword_counts.index, y=keyword_counts.values, title=f"Posts Related to '{selected_keyword}'",
                  labels={"x": "Keyword", "y": "Frequency"}, template="plotly_white")
    st.plotly_chart(fig2)
else:
    st.write(f"No data available for keyword: {selected_keyword}")

# Section 4: Sentiment by Post Type
st.subheader("4. Sentiment Polarity by Post Type")
fig3 = px.box(sentiment_and_text_df, x="type", y="polarity", color="type",
              title="Sentiment Polarity by Post Type",
              labels={"type": "Post Type", "polarity": "Sentiment Polarity"},
              template="plotly_white")
st.plotly_chart(fig3)
