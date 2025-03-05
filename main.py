import streamlit as st
from agents.web_scraper import WebScraperAgent
from agents.data_processor import DataProcessorAgent
from agents.analysis_agent import AnalysisAgent
from agents.strategy_agent import StrategyAgent

# Title
st.title("Deep Research AI")

# User input
query = st.text_input("Enter your research topic:")

if st.button("Run Research"):
    if query:
        st.write("### Web Scraping Results:")
        scraper = WebScraperAgent()
        raw_data = scraper.scrape(query)
        st.write(raw_data)

        st.write("### Processed Data:")
        processor = DataProcessorAgent()
        structured_data = processor.process(raw_data)
        st.write(structured_data)

        st.write("### AI Analysis:")
        analysis = AnalysisAgent()
        insights = analysis.analyze(structured_data)
        st.write(insights)

        st.write("### Strategy Suggestions:")
        strategy = StrategyAgent()
        recommendations = strategy.plan(insights)
        st.write(recommendations)
    else:
        st.warning("Please enter a topic to research.")
