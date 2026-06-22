import os
from fastapi import FastAPI
from api_server.validator import validate_input, validate_output
from api_server.scoring import score_output
from mcp_server.context_builder import build_prompt
from openai import OpenAI

app = FastAPI()
API_KEY = os.environ.get("AZURE_OPENAI_KEY")
AI_MODEL = os.environ.get("AZURE_OPENAI_DEPLOYMENT")
client = OpenAI(api_key=API_KEY)


@app.post("/generate")
def generate(task_type: str, input_text: str):
    # 1. Validate input
    validate_input(input_text)

    # 2. Build prompt using MCP
    final_prompt = build_prompt(task_type, input_text)

    # 3. Call OpenAI
    response = client.responses.create(
        model=AI_MODEL,
        input=final_prompt
    )

    output = response.output[0].content[0].text

    # 4. Validate output
    is_valid = validate_output(output)

    # 5. Score output
    score = score_output(output)

    return {
        "prompt": final_prompt,
        "output": output,
        "valid": is_valid,
        "score": score
    }