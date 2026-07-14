import os
import pandas as pd
import plotly.express as px
import streamlit as st


# ---------------------------------------------------
# Load History (Cached)
# ---------------------------------------------------
@st.cache_data
def load_history():

    file = "history/history.csv"

    if not os.path.exists(file):
        return None

    df = pd.read_csv(file)

    if df.empty:
        return None

    df["timestamp"] = pd.to_datetime(df["timestamp"])

    return df


# ---------------------------------------------------
# Emotion Distribution Bar Chart
# ---------------------------------------------------
@st.cache_data
def emotion_chart():

    df = load_history()

    if df is None:
        return None

    counts = (
        df["emotion"]
        .value_counts()
        .reset_index()
    )

    counts.columns = [
        "Emotion",
        "Count"
    ]

    fig = px.bar(
        counts,
        x="Emotion",
        y="Count",
        color="Emotion",
        title="Emotion Distribution"
    )

    fig.update_layout(
        template="plotly_dark",
        xaxis_title="Emotion",
        yaxis_title="Count"
    )

    return fig


# ---------------------------------------------------
# Emotion Distribution Pie Chart
# ---------------------------------------------------
@st.cache_data
def emotion_pie_chart():

    df = load_history()

    if df is None:
        return None

    fig = px.pie(
        df,
        names="emotion",
        title="Emotion Distribution",
        hole=0.4
    )

    fig.update_traces(
        textposition="inside",
        textinfo="percent+label"
    )

    return fig


# ---------------------------------------------------
# Confidence Timeline
# ---------------------------------------------------
@st.cache_data
def confidence_timeline():

    df = load_history()

    if df is None:
        return None

    if "confidence" not in df.columns:
        return None

    fig = px.line(
        df,
        x="timestamp",
        y="confidence",
        color="emotion",
        markers=True,
        title="Emotional Journey"
    )

    fig.update_layout(
        template="plotly_dark"
    )

    return fig


# ---------------------------------------------------
# Field-wise Emotion Chart
# ---------------------------------------------------
@st.cache_data
def field_chart():

    df = load_history()

    if df is None:
        return None

    if "field" not in df.columns:
        return None

    field_counts = (
        df.groupby(
            ["field", "emotion"]
        )
        .size()
        .reset_index(name="Count")
    )

    fig = px.bar(
        field_counts,
        x="field",
        y="Count",
        color="emotion",
        barmode="group",
        title="Emotion Distribution by Study Field"
    )

    fig.update_layout(
        template="plotly_dark"
    )

    return fig


# ---------------------------------------------------
# Summary Statistics
# ---------------------------------------------------
@st.cache_data
def summary_stats():

    df = load_history()

    if df is None:
        return None

    stats = {}

    stats["Total Sessions"] = len(df)

    stats["Most Common Emotion"] = (
        df["emotion"]
        .mode()[0]
    )

    if "field" in df.columns:

        stats["Most Studied Field"] = (
            df["field"]
            .mode()[0]
        )

    if "confidence" in df.columns:

        stats["Average Confidence"] = (
            round(
                df["confidence"].mean() * 100,
                2
            )
        )

    return stats