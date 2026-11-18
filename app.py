
import streamlit as st
from google import genai

st.title("jolitixai")
client = genai.Client(api_key="AQ.Ab8RN6JfTlAqc9qb9n7wqn0SLV1K6drBZs59AFXmXuwgLBULSQ")

if "m" not in st.session_state:
    st.session_state.m = []

for x in st.session_state.m:
    st.chat_message(x["r"]).write(x["c"])

if p := st.chat_input("Sawal poochein..."):
    st.session_state.m.append({"r": "user", "c": p})
    st.chat_message("user").write(p)
    res = client.models.generate_content(model="gemini-3.5-flash", contents=p)
    st.session_state.m.append({"r": "assistant", "c": res.text})
    st.chat_message("assistant").write(res.text)
    
