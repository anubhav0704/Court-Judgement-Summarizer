import streamlit as st
import summarizer
import preprocessing
import time

st.set_page_config(page_title="Legal Judgement Summarizer", layout="wide")

st.title("🇮🇳 Indian Court Judgement Summarizer")
st.markdown("""
This tool uses a Transformer-based model (LED) to generate abstractive summaries of long Indian court judgements.
It handles long documents (up to 16k tokens) and aims to extract:
- **Facts**
- **Legal Issues**
- **Reasoning**
- **Decision**
""")

@st.cache_resource
def load_summarizer():
    return summarizer.LegalSummarizer()

try:
    with st.spinner("Loading Model (this may take a minute)..."):
        model = load_summarizer()
    st.success("Model Loaded Successfully!")
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

uploaded_file = st.file_uploader("Upload a Judgement (.txt file)", type=["txt"])

if uploaded_file is not None:
    text = uploaded_file.read().decode("utf-8")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Original Text")
        st.text_area("Full Content", text, height=600)
        
        # Display stats
        words = len(text.split())
        st.info(f"Word Count: {words}")
        
    with col2:
        st.subheader("Abstractive Summary")
        if st.button("Generate Summary"):
            with st.spinner("Summarizing..."):
                start_time = time.time()
                try:
                    summary = model.summarize(text)
                    end_time = time.time()
                    
                    st.text_area("Summary", summary, height=400)
                    st.success(f"Summarization complete in {end_time - start_time:.2f} seconds.")
                    
                    st.subheader("Summary Analysis")
                    st.write(f"Summary Length: {len(summary.split())} words")
                    
                except Exception as e:
                    st.error(f"Error during summarization: {e}")

st.markdown("---")
st.markdown("Developed with HuggingFace Transformers & Streamlit.")
