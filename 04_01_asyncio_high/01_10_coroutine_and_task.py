import asyncio


async def factprial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})... current i={i}...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f


async def main():
    L = await asyncio.gather(
        factprial("A", 4),
        factprial("B", 5),
        factprial("C", 6),
    )
    print(L)


asyncio.run(main())
