#streamlit frontend of web-scraper

import streamlit as st
from scrape import (
    web_scrape,
    extract_body_content,
    clean_body_content,
    split_dom_content
)
from parse import parse_with_ollama

st.title('AI Web Scraper')
url = st.text_input('Enter your URL for scraping')

if st.button('Scrape site'):
    st.write('scraping....')

    result = web_scrape(url)
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)

    st.session_state.dom_content = cleaned_content

    with st.expander('VIEW DOM CONTENT'):
        st.text_area('DOM CONTENT', cleaned_content, height=300)

if 'dom_content' in st.session_state:
    parse_description = st.text_area('Describe what your looking for?')

    if st.button('Parsed data'):
        if parse_description:
            st.write('Parsing data...')

            dom_chunks = split_dom_content(st.session_state.dom_content)
            result = parse_with_ollama(dom_chunks, parse_description)
            st.write(result)
   

