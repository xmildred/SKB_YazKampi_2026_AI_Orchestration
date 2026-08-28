# Agentic Sequential Orchestration Starter

A minimal educational project that demonstrates sequential orchestration with AI agents.

The project passes one shared state object through a fixed list of agents:

```text
User Request
  -> Requirements Agent
  -> Design Agent
  -> Implementation Agent
  -> Review Agent
  -> Final Output
```

Each agent reads the current state, adds its own contribution, and passes the updated state to the next agent.

## Why this project exists

This repository is designed for students who are learning the basics of agentic software development. It intentionally starts with the simplest useful orchestration pattern: a sequential pipeline.

Students can later evolve it into more advanced patterns such as conditional routing, evaluator loops, human approval, parallel review agents, memory, RAG, or a web dashboard.

## Project Structure

```text
agentic_sdlc/
|-- agents/                 # Agent classes
|-- prompts/                # Prompt templates for each agent
|-- core/                   # LLM, state, and orchestration logic
|-- outputs/                # Generated step outputs, ignored by git
|-- archive/legacy_version/ # Older version kept locally, ignored by git
|-- input.txt               # User request
|-- main.py                 # Entry point
|-- config.py               # Environment-based config
|-- requirements.txt
`-- .env.example
```

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file from `.env.example`:

```env
GEMINI_API_KEY=your_api_key_here
MODEL_NAME=gemini-2.5-flash-lite
OUTPUT_DIR=outputs
```

## Usage

Edit `input.txt`, then run:

```bash
python main.py
```

Each step writes the current state to `outputs/<agent_name>.json`.

## Learning Path

Suggested student exercises:

1. Add a new agent to the sequence.
2. Change a prompt and observe how the state changes.
3. Save the final implementation into real source files.
4. Add a retry when the Review Agent returns `NEEDS_WORK`.
5. Add a human approval step before implementation.
6. Replace the fixed sequence with conditional routing.
7. Add a small web dashboard.

## Notes

Do not commit your real `.env` file. Use `.env.example` to show which variables are required.
