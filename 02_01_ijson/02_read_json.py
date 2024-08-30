"""Test for json reading."""

import datetime as dt

# import json
import ijson

target_id = 6813506
print("start", dt.datetime.now())

# # jsonモジュールを使った場合
# with open("big_size_json.json", "r") as f:
#     data = json.load(f)
#     for data in data:
#         if data["user"] == f"user_{target_id}":
#             print(data)
#             break

# ijsonモジュールを使った場合
with open("big_size_json.json", "r") as f:
    for data in ijson.items(f, "item"):
        if data["user"] == f"user_{target_id}":
            print(data)
            break

print("end", dt.datetime.now())
