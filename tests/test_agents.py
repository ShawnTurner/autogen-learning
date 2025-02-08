import pytest
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient

@pytest.mark.asyncio
async def test_assistant_agent():
    """Test basic assistant agent functionality."""
    agent = AssistantAgent("test_assistant", OpenAIChatCompletionClient(model="gpt-3.5-turbo"))
    response = await agent.run(task="Say 'Test'")
    assert response is not None
    assert isinstance(response, str)
