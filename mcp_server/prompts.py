def get_prompt_template(task_type):
    templates = {
        "summarization": """
            You are a helpful assistant.
            
            Task: Summarize the following text.
            Constraints:
            - Keep it under 100 words
            - Use bullet points
            
            Input:
            {text}
        """,
        "qa": """
        You are an expert assistant.
        
        Answer the question concisely.
        
        Question: {question}
        """
    }

    return templates.get(task_type)