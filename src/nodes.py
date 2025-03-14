import os
import time
# from langchain_community.tools import GmailSearch
from langchain_google_community.gmail.search import GmailSearch
from langchain_google_community import GmailToolkit
from .state import EmailState

class Nodes():
    def __init__(self):
        self.gmail=GmailToolkit()

    def check_email(self,state:EmailState):
        print("checking new emails")
        search=GmailSearch(api_resource=self.gmail.api_resource)
        emails=search('after:newer_than:1d')
        checked_emails=state['checked_emails_id'] if state['checked_emails_id'] else []
        thread=[]
        new_emails=[]
        print("HERE ARE THE EMAILS: ",emails)
        for email in emails:
            if email['id'] not in checked_emails and email['threadId'] not in thread and os.environ['MY_EMAIL'] not in email['sender']:
                thread.append(email['threadId'])
                new_emails.append(
                    {
                        'id':email['id'],
                        'threadId':email['threadId'],
                        'snippet':email['snippet'],
                        'sender':email['sender']
                    }
                )
        checked_emails.extend([email['id'] for email in emails])
        return {
            **state,
            'emails':new_emails,
            'checked_emails_ids':checked_emails
        }

    def wait_next_run(self,state:EmailState):
        print("waiting 30 secs")
        time.sleep(30)
        return state

    def new_emails(self,state:EmailState):
        if len(state['emails']) ==0:
            print('no new emails')
            return "END"
        else:
            print('New emails')
            return 'CONTINUE'