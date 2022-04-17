from decouple import config
from google.oauth2 import service_account
import googleapiclient.discovery
import datetime

CAL_ID = 'garvitkhurana-gcapi@regal-stage-347417.iam.gserviceaccount.com'
SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = './service_accounts.json'


def test_calendar():
    print("RUNNING TEST_CALENDAR()")
    
    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = googleapiclient.discovery.build('calendar', 'v3', credentials=credentials)

    # CREATE A NEW EVENT
    new_event = {
    'summary': "Adding Garvit Khurana's Event",
    'location': 'Dehradun, India',
    'description': 'Intern Task',
    'start': {
        'date': f"{datetime.date.today()}",
        'timeZone': 'Asia/Kolkata',
    },
    'end': {
        'date': f"{datetime.date.today() + datetime.timedelta(days=3)}",
        'timeZone': 'Asia/Kolkata',
    },
    }
    service.events().insert(calendarId=CAL_ID, body=new_event).execute()
    print('Event created')

    # GET ALL EXISTING EVENTS
    events_result = service.events().list(calendarId=CAL_ID, maxResults=2500).execute()
    events = events_result.get('items', [])
    
    # LOG THEM ALL OUT IN DEV TOOLS CONSOLE
    for e in events:
        print(e)
        # event_id = e['id']
        # service.events().delete(calendarId=CAL_ID, eventId=event_id).execute()
    
    return events


    
