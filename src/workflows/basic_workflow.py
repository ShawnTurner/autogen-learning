import asyncio
from typing import Optional, Any, Union
from ..agents.custom_assistant import CustomAssistant

async def run_basic_workflow(
    task: str,
    system_message: Optional[str] = None,
    model: str = "gpt-3.5-turbo"
) -> Union[str, dict, None]:
    """
    Run a basic workflow with a custom assistant.
    
    Args:
        task: The task to be performed
        system_message: Optional custom system message for the assistant
        model: The model to use (default: gpt-3.5-turbo)
        
    Returns:
        The assistant's response
    """
    assistant = CustomAssistant(
        name="workflow_assistant",
        system_message=system_message,
        llm_config={"model": model}
    )
    
    response = await assistant.run(task=task)
    return response

async def main():
    """Example usage of the basic workflow."""
    response = await run_basic_workflow(
        task="Explain what is AutoGen in one sentence.",
        system_message="You are an expert in AutoGen framework."
    )
    print(f"Response: {response}")

if __name__ == "__main__":
    asyncio.run(main())
