import asyncio
from rasa.core.agent import Agent

async def predict():
    # Load the Rasa agent
    agent = Agent.load('D:/Documents/Master/Thesis/Reference-code/rasa-diet/model/restage.tar.gz')

    # Predict intent and entities for a sentence
    result = await agent.parse_message('Hello, how are you?')

    # Display the result
    print(result)

# Run the asynchronous function inside an event loop
loop = asyncio.get_event_loop()
loop.run_until_complete(predict())
