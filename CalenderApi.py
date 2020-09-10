import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
service = None

def login():
    global service;
    creds = None
    if os.path.exists("token.pickle"):
        with open("token.pickle","rb") as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)
    service = build("calendar", "v3", credentials=creds)


def getAppointments(timeFrom, timeTo):
    global service
    timeFrom = timeFrom.isoformat() + 'Z'
    timeTo = timeTo.isoformat() + 'Z'
    calendarResults = service.events().list(calendarId='primary', timeMin=timeFrom, timeMax = timeTo, singleEvents=True, orderBy='startTime').execute()
    calendarData = calendarResults.get('items', [])
    if not calendarData:
        return None
    else:
        return calendarData #Array