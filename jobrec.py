import requests
import streamlit as st

# Streamlit UI for user input
st.title("Chat API Integration")
api_key = "TsvriMQAo7akwKs9tEqTfZapurzzuudp"
external_user_id = "ritik"
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

    response = requests.post(create_session_url, headers=create_session_headers, json=create_session_body)
    if response.status_code == 200:
        session_id = response.json()['data']['id']
        
        # Submit Query
        submit_query_url = f"https://api.on-demand.io/chat/v1/sessions/{session_id}/query"
        submit_query_headers = {
            "apikey": api_key
        }
        submit_query_body = {
            "endpointId": "predefined-openai-gpt4o",
            "query": query,
            "pluginIds": ["plugin-1712327325", "plugin-1713962163", "plugin-1726267491"],
            "responseMode": "sync"
        }

        query_response = requests.post(submit_query_url, headers=submit_query_headers, json=submit_query_body)
        if query_response.status_code == 200:
            st.write("Response:", query_response.json())
        else:
            st.write("Error in submitting query:", query_response.text)
    else:
        st.write("Error in creating session:", response.text)
