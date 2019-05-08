# %%
import json

with open("erika/charTranslation.json", encoding="UTF-8") as f:
    test = json.load(f)
    ddr_2_ascii = {value: key for key, value in test.items()}
    for index in range(1, 128):
        tmp = ddr_2_ascii.get(hex(index).upper()[2:], " ")
        print(f"\"{tmp}\",")
