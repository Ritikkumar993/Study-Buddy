import requests
import streamlit as st

# Streamlit UI for user input
st.title("Chat API Integration")
api_key = "f5FliSQyeuFlQsPcUjFu5SwO7aSI0go1"
external_user_id = "Ritik"
query = st.text_input("Query")

if st.button("Submit Query"):
    # Create Chat Session
    create_session_url = "https://api.on-demand.io/chat/v1/sessions"
    create_session_headers = {
        "apikey": api_key
    }
    create_session_body = {
        "pluginIds": [],
        "externalUserId": external_user_id
    }

    create_session_response = requests.post(create_session_url, headers=create_session_headers, json=create_session_body)
    create_session_data = create_session_response.json()
    session_id = create_session_data['data']['id']

    # Submit Query
    submit_query_url = f"https://api.on-demand.io/chat/v1/sessions/{session_id}/query"
    submit_query_headers = {
        "apikey": api_key
    }
    submit_query_body = {
        "endpointId": "predefined-openai-gpt4o",
        "query": query,
        "pluginIds": ["plugin-1712327325", "plugin-1713962163", "plugin-1726263667"],
        "responseMode": "sync"
    }

    submit_query_response = requests.post(submit_query_url, headers=submit_query_headers, json=submit_query_body)
    submit_query_data = submit_query_response.json()

    # Display the response
    st.write(submit_query_data["data"]["answer"])
