# from langchain.tools import tool
from langchain_community.tools.gmail import GmailCreateDraft
from crewai.tools import BaseTool
from pydantic import Field
from langchain_community.tools.tavily_search.tool import TavilySearchResults
from langchain_community.agent_toolkits import GmailToolkit
import os
from dotenv import load_dotenv
load_dotenv()
from langchain_community.tools import GmailSearch

os.environ['TAVILY_API_KEY']=os.getenv("TAVILY_API_KEY")

class GetGmailThreadTool(BaseTool):
    name:str='thread'
    description:str="Tool for getting gmail threads"
    gmail:GmailToolkit=GmailToolkit()
    search:GmailSearch=Field(default_factory=GmailSearch)

    def _run(self):
        return self.search.invoke("after:newer_than:5d")


class CreateDraftTool(BaseTool):
    name:str = "draft"
    description:str="Tool to create email drafts.The input should be pipe(|) separated of length three representing reciever email, subject of the email, and actual message. For example: lorem@ipsum.com | subject | message"
    gmail:GmailToolkit=Field(default_factory=GmailToolkit)
    
    def _run(self,data:str):
        """Tool to create email drafts"""
        email,sub,msg=data.split("|")
        draft=GmailCreateDraft(api_resource=self.gmail.api_resource)

        res=draft({                
            'to':[email],
            'subject':sub,
            'message':msg
        })
        return res
    
class TavilyTool(BaseTool):
    name: str = "Search"
    description: str = "Useful for search-based queries. Use this to perform your search, If NECESSARY."
    search:TavilySearchResults = Field(default_factory=TavilySearchResults)

    def _run(self, query: str):
        """Execute the search query and return results"""
        try:
            return self.search.run(query)
        except Exception as e:
            return f"Error performing search: {str(e)}"