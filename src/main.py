import logging
import os
from dotenv import load_dotenv
import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main() -> None:
    load_dotenv()
    api_key = os.getenv('OPENAI_API_KEY')
    organization = os.getenv('OPENAI_ORGANIZATION')
    
    logger.debug(f"OPENAI_API_KEY: {api_key}")
    logger.debug(f"OPENAI_ORGANIZATION: {organization}")
    
    if not api_key:
        logger.error("OPENAI_API_KEY is not set")
        return
    
    if not organization:
        logger.error("OPENAI_ORGANIZATION is not set")
        return
    
    try:
        agent = AssistantAgent("assistant", OpenAIChatCompletionClient(model="gpt-3.5-turbo"))
        response = await agent.run(task="Say 'Hello World!'")
        logger.info(f"Response: {response}")
    except Exception as e:
        logger.error(f"Failed to complete the task: {e}")

if __name__ == "__main__":
    asyncio.run(main())
