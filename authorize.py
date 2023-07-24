import os

import openai
import streamlit as st
from google.cloud import secretmanager

def get_api_key():
    openai.api_key = st.secrets["OPENAI_API_KEY"]
    return openai.api_key

def access_secret_version():
    project_id = st.secrets['PROJECT_ID']
    secret_id  = st.secrets['SECRET_ID']
    version_id = st.secrets['VERSION_ID']
    client    = secretmanager.SecretManagerServiceClient()
    name      = client.secret_version_path(project_id, secret_id, version_id)
    response  = client.access_secret_version(request={"name":name})
    payload   = response.payload.data.decode('UTF-8')
    return payload

def get_google_credentials():
    json_key_path = access_secret_version()
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = json_key_path
    return os.environ['GOOGLE_APPLICATION_CREDENTIALS']
