from langgraph_sdk import get_client
import asyncio
from dotenv import load_dotenv
import os
import traceback

load_dotenv()

endpoint = os.getenv("LANGGRAPH_API_URL")
api_key = os.getenv("LANGGRAPH_API_KEY")

agent_client = get_client(url=endpoint, api_key=api_key)

async def create_thread():
    thread = await agent_client.threads.create()
    return thread

async def main():
    thread = await create_thread()

    input = {
        'agent_input_a': 'foo',
        'agent_input_b': 'bar'
    }

    try:
        result = await asyncio.wait_for(
            agent_client.runs.wait(
                thread['thread_id'],
                'agent',
                input = input,
            ),
            timeout=300  # 5 minutes timeout
        )
    except TimeoutError:
        print(f"Timeout occurred")
    except Exception as e:
        print(f"An error occurred")
        print(f"Full traceback:\n{traceback.format_exc(e)}")
    else:
        print('Result: ' + result.get('result_value', ''))

asyncio.run(main())
