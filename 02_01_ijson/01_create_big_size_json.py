"""Create a big size json."""

import json
import random

user_list = []
for i in range(100000000):
    user = f"user_{i}"
    # 16文字のランダムなパスワードを生成
    password = "".join(random.choices("abcdefghijklmnopqrstuvwxyz1234567890", k=24))
    data = {"user": user, "password": password}
    user_list.append(data)

    if i % 1000000 == 0:
        print(i)

with open("big_size_json.json", "w") as f:
    json.dump(user_list, f, indent=4)
