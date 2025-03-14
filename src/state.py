from typing import TypedDict

class EmailState(TypedDict):
    checked_emails_id:list[str]
    emails:list[dict]
    action_required_emails:dict

