🏗️ High-Level Architecture
```
[Frontend UI]
     │
     ▼
[API Server]  ← validation, logging, scoring
     │
     ▼
[MCP Server]  ← prompt templates, context injection
     │
     ▼
[OpenAI API]
     │
     ▼
[Response → Validation → Score → Return]
```

✅ Components Overview
1. MCP Server (Prompt Layer)
Responsible for:

- Prompt templates
- Context injection
- Prompt versioning

👉 Think of this as a "prompt brain"

2. API Server
Responsible for:

- Input validation
- Calling MCP server
- Calling OpenAI API
- Output validation/scoring
- Logging results


3. Frontend (Optional but helpful)

Input prompt
View generated output
View validation score


📦 Project Structure
```
llm-model-fine-tuning/
│
├── api-server/
│   ├── app.py
│   ├── validator.py
│   ├── scoring.py
│
├── mcp-server/
│   ├── prompts.py
│   ├── context_builder.py
│
├── frontend/
│   ├── app.html
│   ├── app.js
│
└── config/
    ├── settings.py
```

RUN THE FRONTEND
```bash
cd frontend
python -m http.server 3000
```

RUN THE API SERVER
```bash
python -m uvicorn_runner
```