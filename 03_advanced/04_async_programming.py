import asyncio

async def say_hello():
    # Defines an asynchronous function.
    await asyncio.sleep(10)
    # Simulates a 10-second delay.
    print("Hello, Async World!")
    # Prints a message after the delay.

asyncio.run(say_hello())
# Runs the asynchronous function.
