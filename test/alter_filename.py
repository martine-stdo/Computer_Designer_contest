import os
import re
import shutil
dirs = '/Users/xkool/Desktop/test/rename_dirs/'
new_underground_path = '/Users/xkool/Desktop/test/new_underground'
new_overground_path = '/Users/xkool/Desktop/test/new_overground'

# 数据分组
dirs_list = os.listdir(dirs)
print(dirs_list)

under_end_num = 0
over_end_num = 0
for file_list in dirs_list:
    if os.path.isdir(dirs+file_list):
        print(file_list)
        num_num_list = []
        files = os.listdir(dirs+file_list)
        under_str = ['ug', 'underground']
        underfile_list = [file for file in files if any(str in file for str in under_str)]
        overfile_list = [file for file in files if not any(str in file for str in under_str)]
        for under_file in sorted(underfile_list):
            # print("under:" + under_file)
            num = re.findall('\d{2}', under_file)
            if len(num) == 1:
                under_end_num += 1
                new_name = new_underground_path + '/underground_' + str(under_end_num) + '.dwg'
            elif len(num) == 2 and int(num[0]) not in num_num_list:
                num_num_list.append(int(num[0]))
                under_end_num += 1
                new_name = new_underground_path + '/underground_' + str(under_end_num) + '_' + str(num[1]) + '.dwg'
            elif len(num) == 2 and int(num[0]) in num_num_list:
                new_name = new_underground_path + '/underground_' + str(under_end_num) + '_' + str(num[1]) + '.dwg'
            else:
                under_end_num += 1
                new_name = new_underground_path + '/underground_' + str(under_end_num) + '.dwg'
            # print(new_name)
            old_name = dirs + '/' + file_list + '/' + under_file
            os.rename(old_name, new_name)

        ground_str, roof_str, std_str = ['ground', 'gf'], ['roof', 'rf'], ['std', 'standard', "图"]
        ground_list, roof_list, std_list = [], [], []
        for over_file in sorted(overfile_list):
            print('over:'+ over_file)
            num = re.findall('\d{2}', over_file)
            if any(file_str in over_file for file_str in ground_str):
                print('ground:'+ over_file)
                if len(num) == 1:
                    over_end_num += 1
                    new_name = new_overground_path + '/overground_' + 'ground_' + str(over_end_num) + '.dwg'
                elif len(num) == 2 and num[0] not in ground_list:
                    ground_list.append(num[0])
                    over_end_num += 1
                    new_name = new_overground_path + '/overground_' + 'ground_' + str(over_end_num) + '_' + str(num[1]) + '.dwg'
                elif len(num) == 2 and num[0] in ground_list:
                    new_name = new_overground_path + '/overground_' + 'ground_' + str(over_end_num) + '_' + str(num[1]) + '.dwg'
                else:
                    over_end_num += 1
                    new_name = new_overground_path + '/overground_' + 'ground_' + str(over_end_num) + '.dwg'
                print(new_name)
                old_name = dirs + '/' + file_list + '/' + over_file
                os.rename(old_name, new_name)
            elif any(str in over_file for str in roof_str):
                print('roof:'+ over_file)
                if len(num) == 1:
                    over_end_num += 1
                    new_name = new_overground_path + '/overground_' + 'roof_' + str(over_end_num) + '.dwg'
                elif len(num) == 2 and num[0] not in roof_list:
                    roof_list.append(num[0])
                    over_end_num += 1
                    new_name = new_overground_path + '/overground_' + 'roof_' + str(over_end_num) + '_' + str(num[1]) + '.dwg'
                elif len(num) == 2 and num[0] in roof_list:
                    new_name = new_overground_path + '/overground_' + 'roof_' + str(over_end_num) + '_' + str(num[1]) + '.dwg'
                else:
                    over_end_num += 1
                    new_name = new_overground_path + '/overground_' + 'roof_' + str(over_end_num) + '.dwg'
                print(new_name)
                old_name = dirs + '/' + file_list + '/' + over_file
                os.rename(old_name, new_name)
            elif any(str in over_file for str in std_str):
                print('standard:'+over_file)
                if len(num) == 1 and "图" not in over_file:
                    over_end_num += 1
                    new_name = new_overground_path + '/overground_' + 'standard_' + str(over_end_num) + '.dwg'
                elif len(num) == 2 and num[0] not in std_list and "图" not in over_file:
                    std_list.append(num[0])
                    over_end_num += 1
                    new_name = new_overground_path + '/overground_' + 'standard_' + str(over_end_num) + '_' + str(num[1]) + '.dwg'
                elif len(num) == 2 and num[0] in std_list and "图" not in over_file:
                    new_name = new_overground_path + '/overground_' + 'standard_' + str(over_end_num) + '_' + str(num[1]) + '.dwg'
                else:
                    over_end_num += 1
                    new_name = new_overground_path + '/overground_' + 'standard_' + str(over_end_num) + '.dwg'
                print(new_name)
                old_name = dirs + '/' + file_list + '/' + over_file
                os.rename(old_name, new_name)
            else:
                new_name = None
# # 数据分类
# files_path = os.walk(dirs)
# for root, dir, files in files_path:
#     print("root:" + str(root))
#     print("dir:" + str(dir))
#     under_str = ['ug', 'underground']
#     underfile_list = [file for file in files if any(str in file for str in under_str)]
#     overfile_list = [file for file in files if not any(str in file for str in under_str)]
#     for index, value in enumerate(underfile_list):
#         print("underground:" + value)
#         old_name = root + '/' + value
#         new_name = new_underground_path + '/' + value
#         # print(new_name)
#         # os.rename(old_name, new_name)
#     for index, value in enumerate(overfile_list):
#         print('overground:' + value)
#         old_name = root + '/' + value
#         new_name = new_overground_path + '/' + value
        # os.rename(old_name, new_name)
        # print(new_name)

# 重命名
# under_file = os.listdir(new_underground_path)
# under_file_num = 0
# num_num_list = []
# for index, file in enumerate(sorted(under_file)):
    # print(index, file)
    # num = re.findall('\d{2}', file)
    # if len(num) == 1:
    #     under_file_num += 1
    #     new_name = new_underground_path + '/underground_' + str(under_file_num) + '.dwg'
    # elif len(num) == 2 and num[0] not in num_num_list:
    #     num_num_list.append(num[0])
    #     under_file_num += 1
    #     new_name = new_underground_path + '/underground_' + str(under_file_num) + '_' + str(num[1]) + '.dwg'
    # elif len(num) == 2 and num[0] in num_num_list:
    #     new_name = new_underground_path + '/underground_' + str(under_file_num) + '_' + str(num[1]) + '.dwg'
    # else:
    #     under_file.remove(file)
    #     new_name = None
    # print(new_name)
    # old_name = new_underground_path + '/' + file
    # if new_name != None:
    #     os.rename(old_name, new_name)

# over_file = os.listdir(new_overground_path)
# over_file_num = 0
# ground_str, roof_str, std_str = ['ground', 'gf'], ['roof', 'rf'], ['std', 'standard']
# ground_list, roof_list, std_list = [], [], []
# for index, file in enumerate(sorted(over_file)):
    # print(index, file)
    # num = re.findall('\d+', file)
    # if any(str in file for str in ground_str):
    #     print('ground')
    #     if len(num) == 1:
    #         over_file_num += 1
    #         new_name = new_overground_path + '/overground_' + 'ground_' + str(over_file_num) + '.dwg'
    #     elif len(num) == 2 and num[0] not in ground_list:
    #         ground_list.append(num[0])
    #         over_file_num += 1
    #         new_name = new_overground_path + '/overground_' + 'ground_' + str(over_file_num) + '_' + str(num[1]) + '.dwg'
    #     elif len(num) == 2 and num[0] in ground_list:
    #         new_name = new_overground_path + '/overground_' + 'ground_' + str(over_file_num) + '_' + str(num[1]) + '.dwg'
    #     else:
    #         new_name = None
    #     print(new_name)
    # elif any(str in file for str in roof_str):
    #     print('roof')
    #     if len(num) == 1:
    #         over_file_num += 1
    #         new_name = new_overground_path + '/overground_' + 'roof_' + str(over_file_num) + '.dwg'
    #     elif len(num) == 2 and num[0] not in roof_list:
    #         roof_list.append(num[0])
    #         over_file_num += 1
    #         new_name = new_overground_path + '/overground_' + 'roof_' + str(over_file_num) + '_' + str(num[1]) + '.dwg'
    #     elif len(num) == 2 and num[0] in roof_list:
    #         new_name = new_overground_path + '/overground_' + 'roof_' + str(over_file_num) + '_' + str(num[1]) + '.dwg'
    #     else:
    #         new_name = None
    #     print(new_name)
    # elif any(str in file for str in std_str):
    #     print('standard')
    #     if len(num) == 1:
    #         over_file_num += 1
    #         new_name = new_overground_path + '/overground_' + 'standard_' + str(over_file_num) + '.dwg'
    #     elif len(num) == 2 and num[0] not in std_list:
    #         std_list.append(num[0])
    #         over_file_num += 1
    #         new_name = new_overground_path + '/overground_' + 'standard_' + str(over_file_num) + '_' + str(num[1]) + '.dwg'
    #     elif len(num) == 2 and num[0] in std_list:
    #         new_name = new_overground_path + '/overground_' + 'standard_' + str(over_file_num) + '_' + str(num[1]) + '.dwg'
    #     else:
    #         new_name = None
    #     print(new_name)
    # else:
    #     new_name = None
    # new_name = new_overground_path + '/overground_' + str(index) + '.dwg'
    # print(new_name)
    # old_name = new_overground_path + '/' + file
#     if new_name != None:
#         os.rename(old_name, new_name)

