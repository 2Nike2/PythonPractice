import asyncio


async def nested():
    return 42


async def main():

    # not executed
    print(nested())

    print(await nested())


asyncio.run(main())
