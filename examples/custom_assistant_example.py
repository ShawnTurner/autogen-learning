import asyncio
import json
import os
from pathlib import Path
from src.agents.custom_assistant import CustomAssistant

async def load_config():
    """Load the agent configuration."""
    config_path = Path(__file__).parent.parent / "src" / "config" / "agent_config.json"
    with open(config_path) as f:
        return json.load(f)

async def main():
    """Demonstrate usage of the custom assistant with configuration."""
    config = await load_config()
    
    # Create an assistant with code expert configuration
    code_assistant = CustomAssistant(
        name="code_expert",
        system_message=config["system_messages"]["code_expert"],
        llm_config={
            "model": config["default_model"],
            **config["models"][config["default_model"]]
        }
    )
    
    # Example tasks
    tasks = [
        "Write a Python function to calculate the Fibonacci sequence.",
        "Explain the concept of async/await in Python."
    ]
    
    for task in tasks:
        print(f"\nTask: {task}")
        try:
            response = await code_assistant.run(task=task)
            print(f"Response: {response}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
