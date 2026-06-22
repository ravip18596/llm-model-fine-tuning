from .prompts import get_prompt_template

def build_prompt(task_type, input_data):
    template = get_prompt_template(task_type)

    if task_type == "summarization":
        return template.format(text=input_data)

    if task_type == "qa":
        return template.format(question=input_data)

    return input_data