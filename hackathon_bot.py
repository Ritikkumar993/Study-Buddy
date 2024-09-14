import requests
import streamlit as st

# Custom CSS for enhanced aesthetics
st.markdown(
    """
    <style>
    /* Background gradient */
    .reportview-container {
        background: linear-gradient(to bottom right, #f8fafc, #e0eafc);
        padding: 20px;
    }
    /* Central container */
    .stApp {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }
    /* Title Styling */
    .title {
        text-align: center;
        font-size: 3em;
        font-weight: bold;
        color: #2c3e50;
        margin-bottom: 0.5em;
        font-family: 'Arial', sans-serif;
    }
    /* Subtitle Styling */
    .subtitle {
        text-align: center;
        font-size: 1.2em;
        color: #7f8c8d;
        margin-bottom: 2em;
        font-family: 'Arial', sans-serif;
    }
    /* Input box styling */
    .stTextInput {
        border: 2px solid #bdc3c7;
        border-radius: 10px;
        padding: 10px;
        font-size: 1.1em;
        width: 100%;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    /* Submit button */
    .submit-button {
        background-color: #3498db;
        color: white;
        font-size: 1.2em;
        padding: 12px 30px;
        border: none;
        border-radius: 10px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .submit-button:hover {
        background-color: #2980b9;
    }
    /* Response box */
    .response-box {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        margin-top: 20px;
        font-size: 1.2em;
        line-height: 1.5em;
        font-family: 'Arial', sans-serif;
        color: #2c3e50;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# # Header Image (Optional)
# st.image("https://example.com/hackathon_icon.png", use_column_width=True)  # Replace with an actual image

# Streamlit UI for user input
st.markdown('<h1 class="title">Smart_Bot</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Your personal guide for hackathons, coding tips, and queries!</p>', unsafe_allow_html=True)

# API and user information
api_key = "OCxIwjhQg0XLtO6IuEiTj22h8iajR3hd"
external_user_id = "Abhishek"
query = st.text_input("Ask me anything about hackathons, coding, or tech:", "")

if st.button("Submit Query", key="submit-button"):
    # Create Chat Session
    create_session_url = "https://api.on-demand.io/chat/v1/sessions"
    headers = {"apikey": api_key}
    body = {"pluginIds": ["plugin-1726255273"], "externalUserId": external_user_id}
    
    response = requests.post(create_session_url, headers=headers, json=body)
    session_data = response.json()
    session_id = session_data['data']['id']
    
    # Submit Query
    submit_query_url = f"https://api.on-demand.io/chat/v1/sessions/{session_id}/query"
    query_body = {
        "endpointId": "predefined-openai-gpt4o",
        "query": query,
        "pluginIds": ["plugin-1712327325", "plugin-1713962163", "plugin-1726249854"],
        "responseMode": "sync"
    }
    
    query_response = requests.post(submit_query_url, headers=headers, json=query_body)
    query_result = query_response.json()
    
    # Display the result in a stylized response box
    st.markdown(
        f'<div class="response-box"><strong>Response:</strong> {query_result["data"]["answer"]}</div>',
        unsafe_allow_html=True
    )
