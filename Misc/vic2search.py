import os

# searching_var = 'c'
#
# folder_se = r'H:\JS sub-mode\Фулл игра чистая 2.60.1 для 1.29.6\common\scripted_effects'
# files = os.listdir(folder_se)
# # print(f"{files=}")
# for file in files:
#     fpath = os.path.join(folder_se, file)
#     # print(f'{fpath=}')
#     with open(fpath, 'r') as f:
#         text = f.read()
#         c = text.count(searching_var)
#         if c > 0:
#             print(f"Переменная {searching_var} найдена в файле {fpath}")
#
# folder_st = r'H:\JS sub-mode\Фулл игра чистая 2.60.1 для 1.29.6\common\scripted_triggers'
# files = os.listdir(folder_st)
# # print(f"{files=}")
# for file in files:
#     fpath = os.path.join(folder_st, file)
#     # print(f'{fpath=}')
#     with open(fpath, 'r') as f:
#         text = f.read()
#         c = text.count(searching_var)
#         if c > 0:
#             print(f"Переменная {searching_var} найдена в файле {fpath}")
#
# folder_em = r'H:\JS sub-mode\Фулл игра чистая 2.60.1 для 1.29.6\common\event_modifiers'
# files = os.listdir(folder_em)
# # print(f"{files=}")
# for file in files:
#     fpath = os.path.join(folder_em, file)
#     # print(f'{fpath=}')
#     with open(fpath, 'r') as f:
#         text = f.read()
#         c = text.count(searching_var)
#         if c > 0:
#             print(f"Переменная {searching_var} найдена в файле {fpath}")

#### events
searching_evt = 'has_country_flag = FCA_independence_refused'

folder_evts = r'C:\Users\Иван\Greater-Flavor-Mod\GFM\events'
files = os.listdir(folder_evts)
# print(f"{files=}")
for file in files:
    fpath = os.path.join(folder_evts, file)
    # print(f'{fpath=}')
    with open(fpath, 'r') as f:
        text = f.read()
        c = text.count(searching_evt)
        if c > 0:
            print(f"Ивент {searching_evt} найден в файле {fpath}")

#### decisions
searching_dec = 'canadian_lands = {'

folder_dec = r'C:\Users\Иван\Greater-Flavor-Mod\GFM\decisions'
files = os.listdir(folder_dec)
# print(f"{files=}")
for file in files:
    fpath = os.path.join(folder_dec, file)
    # print(f'{fpath=}')
    with open(fpath, 'r') as f:
        text = f.read()
        c = text.count(searching_dec)
        if c > 0:
            print(f"Решение {searching_dec} найдено в файле {fpath}")
