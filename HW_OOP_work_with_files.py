from pprint import pprint

with open('1.txt') as file_1:
    count_line_1 = 0
    dict_1 = {}
    text_1 = []
    for line in file_1:
        count_line_1 += 1
        text_1.append(line)
    dict_1 [count_line_1] = ['1.txt', count_line_1, text_1]
# print(dict_1)

with open('2.txt') as file_2:
    count_line_2 = 0
    dict_2 = {}
    text_2 = []
    for line in file_2:
        count_line_2 += 1
        text_2.append(line)
    dict_2[count_line_2] = ['2.txt', count_line_2, text_2]
# print(dict_2)

with open('3.txt') as file_3:
    count_line_3 = 0
    dict_3 = {}
    text_3 = []
    for line in file_3:
        count_line_3 += 1
        text_3.append(line)
    dict_3[count_line_3] = ['3.txt', count_line_3, text_3]
# print(dict_3)

files_dict = {**dict_1, **dict_2, **dict_3}
sorted_files = dict(sorted(files_dict.items()))
# pprint(sorted_files)

with open('result_file.txt', 'w') as result_file:
    for key in sorted_files:
        file_name = sorted_files[key][0]
        result_file.write((''.join(file_name)))
        result_file.write('\n')
        result_file.flush()

        count_lines = sorted_files[key][1]
        result_file.write(str(count_lines))
        result_file.write('\n')
        result_file.flush()

        text = sorted_files[key][2]
        result_file.write((''.join(text)))
        result_file.write('\n')
        result_file.flush()
print(result_file)
# t = dict_1[count_line_1][2]
# with open('result_file', 'w') as res_file:
#     res_file.write(('').join(t))
# print(t)
# print(res_file)

