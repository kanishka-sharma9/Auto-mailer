from crewai import Crew
from .agents import EmailFilterAgents
from .tasks import EmailFilterTasks
from src.state import EmailState

class EmailFilterCrew:
    def __init__(self):
        agents=EmailFilterAgents()
        self.filter_agent=agents.email_filter_agent()
        self.action_agent=agents.email_action_agent()
        self.writer_agent=agents.email_writer_agent()

    def kickoff(self,state:EmailState):
        print("Filtering emails")
        tasks=EmailFilterTasks()
        crew=Crew(
            agents=[self.filter_agent,self.action_agent,self.writer_agent],
            tasks=[tasks.email_action_task(self.action_agent),
                   tasks.filter_emails_task(agents=self.filter_agent,emails=self.format_emails(state.get('emails',[]))),
                   tasks.draft_task(agents=self.writer_agent)],
            verbose=True,
        )
        res=crew.kickoff()
        print("crew execution completed successfully")
        print(res)
        return {
            **state,
            'action_reuired_emails':res
        }
    
    def format_emails(self,emails):
        emails_string=[]
        for email in emails:
            print(email)
            arr=[
                f'ID: {email['id']}',
                f'Thread id: {email['threadId']}',
                f'Snippet: {email['snippet']}',
                f'sender:{email['sender']}'
            ]
            emails_string.append(arr)
        return emails_string