import asyncio


# asyncio.Future オブジェクトを返す関数
async def function_that_returns_a_future_object():
    future = asyncio.Future()

    # 別のタスクで Future の結果を設定
    task = asyncio.create_task(set_future_result(future))

    await future

    return future


# Future の結果を設定する関数
async def set_future_result(future):
    await asyncio.sleep(2)
    future.set_result("Result from Future")


# 別の非同期コルーチン
async def some_python_coroutine():
    await asyncio.sleep(1)
    return "Result from coroutine"


# メインの実行部分
async def main():
    # Future オブジェクトを待機し、その結果を出力
    future1 = await function_that_returns_a_future_object()
    print(f"Future1 result: {future1}")

    # asyncio.gatherで複数の非同期タスクを並行実行し、その結果を出力
    future2 = await asyncio.gather(
        function_that_returns_a_future_object(), some_python_coroutine()
    )
    print(f"Future2 results: {future2}")


asyncio.run(main())
