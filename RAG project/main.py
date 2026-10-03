# RAG based Website assistant

import streamlit as st           #to build the frontend
#here process_urls function is downloading the data from Urls and storing it inthe vector Database 
#generate_answer function :llm processing the query and generating the answers
from rag import process_urls, generate_answer

st.title("RAG based Website assistant")

url1 = st.sidebar.text_input("URL-1")
url2 = st.sidebar.text_input("URL-2")
url3 = st.sidebar.text_input("URL-3")
#placeholder is used to show the status of the 
placeholder = st.empty()

process_url_button = st.sidebar.button("Process URL's")

if process_url_button:
    urls = [url for url in (url1, url2, url3) if url!=""]

    if len(urls) == 0:
        placeholder.text("Please mention atleast one URL")
    else:
        for status in process_urls(urls):
            placeholder.text(status)

query = placeholder.text_input("question")

if query:
    try:
        answer, sources  = generate_answer(query)

        st.header("Answer")
        st.write(answer)
        if sources:
            st.header("Sources")
            for s in sources.split("\n"):
                st.write(s)
    except Exception as e:
        placeholder.text("Please first click on process URL")