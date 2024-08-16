import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# Apply dark theme settings
st.set_page_config(page_title="Enhanced Q&A Chatbot", layout="wide", initial_sidebar_state="expanded")

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries."),
        ("user", "Question: {question}")
    ]
)

def generate_response(question, api_key, engine, temperature, max_tokens):
    llm = ChatOpenAI(model=engine, temperature=temperature, max_tokens=max_tokens, openai_api_key=api_key)
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer = chain.invoke({'question': question})
    return answer

# Enhanced App Title
st.markdown("<h1 style='text-align: center; color: white;'>💬 Enhanced Q&A Chatbot With OpenAI</h1>", unsafe_allow_html=True)

# Custom sidebar styling with mature, matching theme
st.sidebar.markdown(
    """
    <style>
    .sidebar-content {
        background-color: #2e2e2e;
        color: #dcdcdc;
        padding: 10px;
        border-radius: 10px;
    }
    .sidebar-content input {
        background-color: #444;
        color: #dcdcdc;
        border-radius: 5px;
    }
    .sidebar-content .stButton button {
        background-color: #444;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 8px 16px;
    }
    .sidebar-content .stSlider > div {
        color: #dcdcdc;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
st.sidebar.title("⚙️ Settings")
st.sidebar.markdown("<p style='color: #dcdcdc;'>Customize your experience below:</p>", unsafe_allow_html=True)

api_key = st.sidebar.text_input("🔑 Enter your OpenAI API Key:", type="password", placeholder="Your API Key")

# Select the OpenAI model with hover info
engine = st.sidebar.selectbox("🧠 Select OpenAI model", ["gpt-3.5-turbo"], help="Choose the model for generating responses")

# Adjust response parameters with added tooltips
temperature = st.sidebar.slider("🎛️ Temperature", min_value=0.0, max_value=1.0, value=0.7, help="Controls the creativity of the response. Lower is more focused, higher is more random.")
max_tokens = st.sidebar.slider("📝 Max Tokens", min_value=50, max_value=300, value=150, help="The maximum number of tokens in the generated response.")

st.sidebar.markdown('</div>', unsafe_allow_html=True)

# Main interface for user input
st.write("### 🗨️ Ask Me Anything!")
st.markdown("<p style='color: #dcdcdc;'>Type your question below and press Enter:</p>", unsafe_allow_html=True)

user_input = st.text_input("You:", key="input", placeholder="Type your question here...")

# Display response with a card
if user_input and api_key:
    with st.spinner("🤖 Thinking..."):
        response = generate_response(user_input, api_key, engine, temperature, max_tokens)
        st.markdown(f"<div style='background-color: #333; padding: 10px; border-radius: 10px; color: white;'>**Assistant:** {response}</div>", unsafe_allow_html=True)
elif user_input:
    st.warning("⚠️ Please enter your OpenAI API Key in the sidebar.")
else:
    st.info("ℹ️ Please provide your input above to get started.")

# Footer with gradient effect, positioned from the right corner to the sidebar
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        right: 0;
        width: calc(100% - 250px); /* Adjust based on the width of your sidebar */
        text-align: center;
        padding: 10px 0;
        background: linear-gradient(90deg, #111, #333);
        font-size: 14px;
        color: white;
        z-index: 9999;
    }

    /* Full black background and white text theme */
    .stApp {
        background-color: #000000;
        color: white;
    }
    .css-18e3th9 {
        background-color: #000000; /* Background of the top part */
        color: white;
    }
    .stTextInput input {
        background-color: #333;
        color: white;
    }
    .stButton button {
        background-color: #444;
        color: white;
    }
    .stSidebar .stText {
        color: #dcdcdc;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="footer">Developed with ❤️ by Mihir Joshi</div>', unsafe_allow_html=True)
