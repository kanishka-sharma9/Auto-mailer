from crewai import Task

class EmailFilterTasks:
    def filter_emails_task(self,agents,emails):
        return Task(
            description=f"""
            Analyse a batch of emails and filter out non-essential ones such as newsletter, promotions nd notifications.
            use your expertise in email analysis to distinguish importnat emails from the rest, pay attention to the sender and avoid invalid emails,
            Make sure to filter for the messages actually directed at the user and avoid notifications.
            <emails>{emails}</emails>.
            Your final answer must include relevant thread_ids and the sender, use bullets points wherever necessary.
            """,
            agent=agents,
            max_retries=2,
            expected_output="only real, non-spam email containing collection of emails."
        )
    
    def email_action_task(self,agents):
        return Task(
            description="""
            For each email thread, pull nd analyse the complete threads using only the actual Thread ID.
            unserstand the context, key points, and the overall sentiment of the conversation.
            
            Identify the main query or concern that needs to be addressed in the response for each
            Your final answer must be a list for all emails with:
            -- thread id
            -- summary of the email thread
            -- highlight of the main points of the email
            -- sender's email
            -- reciever's email
            -- communication style of the thread""",
            agent=agents,
            expected_output="return a list containing the specified information for each email thread."
        )
    
    def draft_task(self,agents):
        return Task(
            description="""
            Based on the action-required emails identified, draft responses for each.
            Ensure that each response is tailored to address the specific needs and context outlines in the email.
            
            -- assume the persona of the user and mimic the communication style in thread.
            -- feel free to do research on the topic to provide more detailed response, if NECESSARY.
            -- if you need to pull the thread again do it using only the actual thread id.

            Use the tool provided to draft each of the responses.
            when using the tool pass the following input:
                - to
                - subject
                - message
            You Must create all drafts before sending your final answer.
            Your final answer MUST be a confirmation that all responses have been drafted.
            """,
            agent=agents,
            expected_output="A well formatted and meaning ful email draft."
        )