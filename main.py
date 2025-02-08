import asyncio
from src.workflows.basic_workflow import run_basic_workflow
from examples.custom_assistant_example import main as run_custom_example

async def main():
    """
    Main entry point demonstrating different AutoGen examples.
    Run with: python main.py
    """
    print("=== Running Basic Workflow ===")
    response = await run_basic_workflow(
        task="What is AutoGen and why is it useful?",
        system_message="You are an expert in AutoGen framework."
    )
    print(f"Basic Workflow Response: {response}\n")
    
    print("=== Running Custom Assistant Example ===")
    await run_custom_example()

if __name__ == "__main__":
    asyncio.run(main())
