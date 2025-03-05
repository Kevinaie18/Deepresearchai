import streamlit as st
from sentence_transformers import SentenceTransformer
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Load the sentence transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")

st.title("Deep Research AI")

# User input
query = st.text_input("Enter your research query:")

if st.button("Search"):
    if query:
        # Simple web scraping example
        url = f"https://www.google.com/search?q={query}"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            results = [link.get_text() for link in soup.find_all("h3")]

            # Generate embeddings for extracted results
            embeddings = model.encode(results)

            # Display results
            st.write("### Search Results")
            df = pd.DataFrame({"Title": results})
            st.dataframe(df)
            
            st.write("### Text Embeddings")
            st.write(embeddings)
        else:
            st.error("Failed to retrieve search results.")
    else:
        st.warning("Please enter a query.")

