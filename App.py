import streamlit as st
from streamlit_oauth import OAuth2Component
from dotenv import load_dotenv
import ResumeHandler as ResumeAnalasis
from HTMLTemplate import css, CV_template, ANA_template
import requests
from requests.auth import HTTPBasicAuth

#def HandleUserQuestion(userQuestion):
#     questionResponse = st.session_state.conversation({'question':userQuestion})
#     st.write(questionResponse)

load_dotenv()
st.set_page_config(page_title="CV Screening", page_icon=":document:")
st.write(css, unsafe_allow_html=True)

if "userQuestion" not in st.session_state:
     st.session_state['userQuestion'] = ''

with st.sidebar:
     st.subheader("Job Profile")
     jobTitle = st.text_input("KeyWord:")
     #st.text_input("Experience level:")
     #st.text_input("Communication level:")
     #st.text_input("Company culture:")
     #st.subheader("Candidate Profile")
     #pdf_doc = st.file_uploader("Upload your candidate resume here and click 'Forecast'",accept_multiple_files=False)
     
st.header("Analysis of candidate resume")

# create an OAuth2Component instance
CLIENT_ID = '8e597d3d-4f9a-4a64-bf76-3d82e3625019'
CLIENT_SECRET = 'dPW8Q~P4C3ZhLnTBcaHk6Necnc9O.e3RpOxcFb87'
AUTHORIZE_ENDPOINT = "https://login.microsoftonline.com/organizations/oauth2/v2.0/authorize"
TOKEN_ENDPOINT = "https://login.microsoftonline.com/organizations/oauth2/v2.0/token"
REVOKE_ENDPOINT = "https://login.microsoftonline.com/organizations/oauth2/v2.0/revoke"


if st.sidebar.button("Search"):
     if jobTitle:
          #st.session_state['userQuestion'] = "Please analyze this resume for  "+jobTitle+" post"
          #st.text_input("Forecast this candidate based on:",st.session_state['userQuestion'])

        oauth2 = OAuth2Component(CLIENT_ID, CLIENT_SECRET, AUTHORIZE_ENDPOINT, TOKEN_ENDPOINT, TOKEN_ENDPOINT, REVOKE_ENDPOINT)
        result = oauth2.authorize_button(
                        name="Genrate Access Token",       
                        redirect_uri="http://localhost:8501",
                        scope="Sites.Search.All User.Read",
                        key="Token",     
                        extras_params={"grant_type": "client_credentials"},
                        use_container_width=True,
            )

        #st.write("token A ",result)
        #token = result["token"]["access_token"]
    #st.write("token A ",token)
        api_url =  "https://bistecglobal.sharepoint.com/_api/search/query?querytext='buddhika'"
        api_url_New =  "https://bistecglobal.sharepoint.com/sites/Interview-Tracker/_api/Web/Lists(guid'08f9ea3d-65ba-41c0-9fd8-03230d829062')/items(22)/AttachmentFiles"
        #api_call_headers = {'Accept': 'application/json; odata=verbose','Authorization': 'Bearer ' + token}
    #api_call_response = requests.get(api_url, headers=api_call_headers, verify=False)
    
    #api_call_headers = {'Authorization': 'Bearer ' + token}
    
        #api_call_response = requests.get(api_url,auth = ('buddhika@bistecglobal.com', 'Budjan@bistec&8790'), headers=api_call_headers)
        #st.write("E1",api_call_response.text)
        #st.write("E2",api_call_response.status_code)






          #with st.spinner("Analyzing"):
               #resumeAnalysisData = ResumeAnalasis.GetSingleResumeResult(pdf_doc,st.session_state['userQuestion'],jobTitle)
               #for x,y in resumeAnalysisData.items():
                    #jobDescription = st.text_area("Job description:",(y[0]["jobDescription"]).strip(),height=100)                    
                    #st.write(CV_template.replace("{{MSG}}", "Resume forecast:"),unsafe_allow_html=True)
                    #st.write(ANA_template.replace("{{MSG}}", (y[0]["analysis"]).strip()),unsafe_allow_html=True)
                    #st.sidebar.text_input("LinkedIn profile:",(y[0]["linkedinURL"]).strip())
                    #st.sidebar.text_input("FaceBook profile:",(y[0]["facebookURL"]).strip())
                    #st.sidebar.text_input("Github account:",(y[0]["githubURL"]).strip())
                    #st.sidebar.text_input("Hackerank:")
                    #st.sidebar.text_input("SO:")
#else:
#st.error('Please check whether "job title" inserted and "Resume" uploaded', icon="⚠️")                    
              
 

#st.title("Google OIDC Example")
#st.write("This example shows how to use the raw OAuth2 component to authenticate with a Google OAuth2 and get email from id_token.")




if "auth" not in st.session_state:
    # create a button to start the OAuth2 flow
    oauth2 = OAuth2Component(CLIENT_ID, CLIENT_SECRET, AUTHORIZE_ENDPOINT, TOKEN_ENDPOINT, TOKEN_ENDPOINT, REVOKE_ENDPOINT)
    result = oauth2.authorize_button(
        name="Genrate Access Token",       
        redirect_uri="http://localhost:8501",
        scope="Sites.Search.All User.Read",
        key="Token",     
        extras_params={"grant_type": "client_credentials"},
        use_container_width=True,
    )

    st.write("token A1 ",result)
    token = result["token"]["access_token"]
    #st.write("token A ",token)
    api_url =  "https://bistecglobal.sharepoint.com/_api/search/query?querytext='buddhika'"
    api_url_New =  "https://bistecglobal.sharepoint.com/sites/Interview-Tracker/_api/Web/Lists(guid'08f9ea3d-65ba-41c0-9fd8-03230d829062')/items"
    api_call_headers = {'Accept': 'application/json; odata=verbose','Authorization': 'Bearer ' + token}
    #api_call_response = requests.get(api_url, headers=api_call_headers, verify=False)
    
    #api_call_headers = {'Authorization': 'Bearer ' + token}
    headers = {
    'Authorization': "Bearer " + token,
    'Accept':'application/json;odata=verbose',
    'Content-Type': 'application/json;odata=verbose'
}
    basic = HTTPBasicAuth('buddhika@bistecglobal.com', 'Pass')
    api_call_response = requests.get(api_url, headers=headers)
    st.write("E1",api_call_response.text)
    st.write("E2",api_call_response.status_code)

