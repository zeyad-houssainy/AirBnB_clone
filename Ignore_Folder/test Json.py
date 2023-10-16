import json
import os
print("Working file location is...............", os.getcwd())

json_text = """{
    "Name": "Zeyad",
    "Age": 28,
    "Gender": "Male",
    "Height": 172,
    "None": null
    }"""
data1 = json.loads(json_text)
print(data1)

json_file = open("json_file.txt", "r", encoding="utf-8")
data2 = json.load(json_file)
json_file.close()
print(data2)

# json.dump(data1)
# print(data1)
json_text_2 = {}
json_text_2["test1"] = 1
json_text_2["test2"] = 2
json_text_2["test3"] = 3
json_text_2["test4"] = 4
data3 = open("json_file2.txt", "w", encoding="utf-8")
json.dump(json_text_2, data3, ensure_ascii=False)

