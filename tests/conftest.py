import os
import pytest
from dotenv import load_dotenv

@pytest.fixture(autouse=True)
def load_env():
    """Load environment variables before each test."""
    load_dotenv()
    # Ensure required env vars are set
    assert os.getenv('OPENAI_API_KEY'), "OPENAI_API_KEY must be set"
    assert os.getenv('OPENAI_ORGANIZATION'), "OPENAI_ORGANIZATION must be set"

@pytest.fixture
def mock_response():
    """Fixture for mocking API responses in tests."""
    return {
        "content": "This is a test response",
        "role": "assistant"
    }
