import asyncio
import sys

async def get_date():
    code = "import datetime; print(datetime.datetime.now())"

    proc = await asyncio.create_subprocess_exec(
        sys.executable, '-c', code, stdout=asyncio.subprocess.PIPE
    )

    data = await proc.stdout.readline()
    line = data.decode("ascii").rstrip()

    await proc.wait()
    return line

data = asyncio.run(get_date())
print(f"Current date: {data}")
