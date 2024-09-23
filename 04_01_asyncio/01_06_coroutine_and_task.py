import asyncio


async def nested():
    return 42


async def main():

    task = asyncio.create_task(nested())

    result = await task
    print(result)


asyncio.run(main())
