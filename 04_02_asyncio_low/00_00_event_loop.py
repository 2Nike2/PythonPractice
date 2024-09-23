import asyncio

def hello_world(loop):
    print("Hello World!")
    loop.stop()

loop = asyncio.new_event_loop()

loop.call_soon(hello_world, loop)

try:
    loop.run_forever()
finally:
    loop.close()
