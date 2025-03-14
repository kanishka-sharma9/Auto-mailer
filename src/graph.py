from .crew.crew import EmailFilterCrew
from .nodes import Nodes
from .state import EmailState
from langgraph.graph import StateGraph
from dotenv import load_dotenv
load_dotenv()

class Workflow():
    def __init__(self):
        nodes=Nodes()
        graph=StateGraph(EmailState)

        graph.add_node('check_new_emails',nodes.check_email)
        graph.add_node('wait_next_run',nodes.wait_next_run)
        graph.add_node('draft_responses',EmailFilterCrew().kickoff({}))

        graph.set_entry_point('check_new_emails')
        graph.add_conditional_edges(
            'check_new_emails',
            nodes.new_emails,
            {
                'CONTINUE':'draft_responses',
                "END":'wait_next_run'
            }
        )
        graph.add_edge('draft_responses','wait_next_run')
        graph.add_edge('wait_next_run','check_new_emails')
        self.app=graph.compile()

    