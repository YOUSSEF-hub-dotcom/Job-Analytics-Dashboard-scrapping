import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(page_title="Advanced Job Analytics", layout="wide")

# Custom CSS to make the links look better
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    stDataFrame { border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Data Scientist Job Analytics Dashboard")

# Load and Clean Data
@st.cache_data
def load_data():
    df = pd.read_csv("detailed_jobs.csv")
    # Clean nulls if any
    df = df.dropna(subset=['Description'])
    return df

try:
    df = load_data()

    # --- Sidebar: Search & Filters ---
    st.sidebar.header("🔍 Search & Filter")
    
    # 1. Search Functionality
    search_query = st.sidebar.text_input("Search in Description:", placeholder="e.g. Python, SQL, Remote")
    
    # 2. Company Filter
    all_companies = df["Company"].unique()
    selected_companies = st.sidebar.multiselect("Filter by Company:", options=all_companies, default=all_companies[:3])

    # Apply Filtering Logic
    filtered_df = df[df["Company"].isin(selected_companies)]
    if search_query:
        filtered_df = filtered_df[filtered_df['Description'].str.contains(search_query, case=False)]

    # --- Top Metrics ---
    m1, m2, m3 = st.columns(3)
    m1.metric("Jobs Found", len(filtered_df))
    m2.metric("Total Companies", filtered_df["Company"].nunique())
    m3.metric("Avg Description Length", int(filtered_df['Description'].str.len().mean()))

    st.divider()

    # --- Advanced Text Analysis (WordCloud) ---
    st.subheader("💡 Key Skills & Keywords Cloud")
    
    if not filtered_df.empty:
        # Combine all descriptions into one big text
        text = " ".join(desc for desc in filtered_df.Description)
        
        # Generate WordCloud
        wordcloud = WordCloud(width=800, height=400, 
                              background_color='white', 
                              colormap='viridis',
                              max_words=100).generate(text)
        
        # Display using Matplotlib
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis("off")
        st.pyplot(fig)
    else:
        st.warning("No data found for the current filters.")

    # --- Visualizations ---
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.subheader("📍 Location Distribution")
        fig_loc = px.bar(filtered_df['Location'].value_counts().head(10), orientation='h', color_discrete_sequence=['#636EFA'])
        st.plotly_chart(fig_loc, use_container_width=True)

    with col_right:
        st.subheader("🏢 Jobs per Company")
        fig_comp = px.treemap(filtered_df, path=['Company'], title="Company Market Share")
        st.plotly_chart(fig_comp, use_container_width=True)

    # --- Interactive Data Table ---
    st.subheader("📋 Detailed Job Postings")
    
    # Format the URL to be clickable
    display_df = filtered_df.copy()
    
    # Displaying dataframe with link column configuration
    st.dataframe(
        display_df,
        column_config={
            "URL": st.column_config.LinkColumn("Application Link"),
            "Description": st.column_config.TextColumn("Job Summary", width="large")
        },
        use_container_width=True,
        hide_index=True
    )

except FileNotFoundError:
    st.error("Missing 'detailed_jobs.csv'. Please run your scraper first!")