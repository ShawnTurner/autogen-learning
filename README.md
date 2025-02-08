# AutoGen 0.4 Example Project

This project demonstrates the usage of AutoGen 0.4 with custom agents and workflows.

## Project Structure

```
├── src/
│   ├── agents/         # Custom agent implementations
│   ├── prompts/        # Prompt templates
│   ├── workflows/      # Multi-agent workflow definitions
│   └── config/         # Configuration files
├── tests/              # Test files
├── docs/               # Documentation
└── examples/           # Example usage
```

## Setup

1. Create a virtual environment and install dependencies using UV:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -e ".[dev]"
```

2. Create a `.env` file with your OpenAI credentials:

```env
OPENAI_API_KEY=your_api_key_here
OPENAI_ORGANIZATION=your_org_id_here
```

## Usage

### Basic Example

```python
from src.workflows.basic_workflow import run_basic_workflow
import asyncio

async def main():
    response = await run_basic_workflow(
        task="Explain what is AutoGen in one sentence.",
        system_message="You are an expert in AutoGen framework."
    )
    print(f"Response: {response}")

asyncio.run(main())
```

### Running Tests

```bash
pytest
```

## Development

- Use `uv pip install -e ".[dev]"` to install in development mode
- Run `pytest` to execute tests
- Use `pyright` for type checking

## License

MIT
