
#api_key = "OCxIwjhQg0XLtO6IuEiTj22h8iajR3hd"
  #      "pluginIds": ["plugin-1726242471"],
# import requests
# import streamlit as st

# # Streamlit UI for input
# st.title("Chat API Integration")
# api_key = "OCxIwjhQg0XLtO6IuEiTj22h8iajR3hd"
# external_user_id = st.text_input("External User ID")
# query = st.text_input("Query")

# if st.button("Submit Query"):
#     # Create Chat Session
#     create_session_url = "https://api.on-demand.io/chat/v1/sessions"
#     create_session_headers = {
#         "apikey": api_key
#     }
#     create_session_body = {
#         "pluginIds": ["plugin-1726242471"],
#         "externalUserId": external_user_id
#     }

#     response = requests.post(create_session_url, headers=create_session_headers, json=create_session_body)
#     if response.status_code == 200:
#         session_id = response.json()['data']['id']
        
#         # Submit Query
#         submit_query_url = f"https://api.on-demand.io/chat/v1/sessions/{session_id}/query"
#         submit_query_headers = {
#             "apikey": api_key
#         }
#         submit_query_body = {
#             "endpointId": "predefined-openai-gpt4o",
#             "query": query,
#             "pluginIds": ["plugin-1712327325", "plugin-1713962163", "plugin-1726242471"],
#             "responseMode": "sync"
#         }

#         query_response = requests.post(submit_query_url, headers=submit_query_headers, json=submit_query_body)
#         if query_response.status_code == 200:
#             st.write("Response:", query_response.json())
#         else:
#             st.write("Error in submitting query:", query_response.text)
#     else:
#         st.write("Error in creating session:", response.text)



import requests
import streamlit as st

# Streamlit UI for user input
st.title("dsabot")
api_key = "OCxIwjhQg0XLtO6IuEiTj22h8iajR3hd"
external_user_id = "rehan"
query = st.text_input("Query")

if st.button("Submit Query"):
    # Create Chat Session
    create_session_url = "https://api.on-demand.io/chat/v1/sessions"
    headers = {"apikey": api_key}
    body = {"pluginIds": ["plugin-1726249854"], "externalUserId": external_user_id}
    
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
