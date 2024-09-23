import asyncio
import random


async def some_coro(param):
    await asyncio.sleep(5)
    await asyncio.sleep(random.random() * 0.01)
    print(param)


async def main():

    background_tasks = set()

    for i in range(10):

        task = asyncio.create_task(some_coro(param=i))

        background_tasks.add(task)

        task.add_done_callback(background_tasks.discard)

    await asyncio.gather(*background_tasks)


asyncio.run(main())
