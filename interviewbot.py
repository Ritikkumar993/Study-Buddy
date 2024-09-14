import requests
import streamlit as st

# Streamlit UI for input
st.title("INTERVIEW CHATBOT")
api_key = "ZaIl7Ba3E1BzvgA6Xh7RtD0AWMSafZYN"
external_user_id = "abhishek"
query = st.text_input("Query")

if st.button("Submit Query"):
    # Create Chat Session
    create_session_url = "https://api.on-demand.io/chat/v1/sessions"
    headers = {"apikey": api_key}
    body = {"pluginIds": ["plugin-1726251563"], "externalUserId": external_user_id}
    
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
    
    # Display the result
    st.write("Response:", query_result["data"]["answer"])