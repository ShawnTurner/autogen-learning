from typing import Any, Optional
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient

class CustomAssistant(AssistantAgent):
    """A custom assistant agent with enhanced capabilities."""
    
    def __init__(
        self,
        name: str,
        system_message: Optional[str] = None,
        llm_config: Optional[dict[str, Any]] = None
    ):
        if system_message is None:
            system_message = "You are a helpful assistant with expertise in Python programming."
        
        if llm_config is None:
            llm_config = {"model": "gpt-3.5-turbo"}
            
        super().__init__(
            name=name,
            model_client=OpenAIChatCompletionClient(**llm_config),
            system_message=system_message
        )
