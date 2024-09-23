import asyncio
import threading


# コルーチンの定義
async def example_coroutine():
    print("Coroutine started")
    await asyncio.sleep(1)
    print("Coroutine finished")
    return 42


# 別スレッドからコルーチンをスケジュールする関数
def thread_function(loop):
    # asyncio.run_coroutine_threadsafe でコルーチンをスケジュール
    future = asyncio.run_coroutine_threadsafe(example_coroutine(), loop)

    try:
        # 結果を取得（タイムアウトを指定可能）
        result = future.result(timeout=2)
        print(f"Result from coroutine: {result}")
    except Exception as e:
        print(f"Coroutine raised an exception: {e}")


# メイン関数
async def main():
    loop = asyncio.get_running_loop()

    # 別スレッドでコルーチンをスケジュール
    thread = threading.Thread(target=thread_function, args=(loop,))
    thread.start()
    thread.join()


# イベントループを実行
asyncio.run(main())
