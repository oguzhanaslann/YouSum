import streamlit as st
from youtube_util import is_youtube_url
import streamlit as st
from video_sum import get_qa_chain

@st.cache_resource
# dict of messages role : message
def getPastMessages(): 
    return {}

@st.cache_resource
def get_summarizer(url):
    return get_qa_chain(url)

st.header("YouTube Summarizer")
title = st.text_input(
    label = 'Youtube link',
    placeholder="Youtube link",
    help = 'Enter a valid youtube link'
)

if st.button("Summarize"):
    if not is_youtube_url(title):
        st.toast("Not a valid youtube url")
    else: 
        st.toast('Valid youtube url', icon="✅")
        get_summarizer(title)

def user_message(msg) : 
    with st.chat_message("user"):
        st.write(msg)

def bot_message(msg) :
    with st.chat_message("ai"):
        st.write(msg)

with st.container(): 
    print(getPastMessages())
    for msg in getPastMessages():
        if getPastMessages()[msg] == "user":
            user_message(msg)
        else:
            bot_message(msg)
   
    prompt = st.chat_input("Say something")
    if prompt:
        user_message(prompt)
        getPastMessages()[prompt] = "user"
        bot_message(get_summarizer(title).run(prompt))
        getPastMessages()[get_summarizer(title).run(prompt)] = "ai"
        
        
        
        
