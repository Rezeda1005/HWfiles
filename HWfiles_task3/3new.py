import pathlib
def file_lenghs(file):
    len = 0
    f = open(file, 'r', encoding = 'utf-8')
    for line in f:
        len += 1
    f.close()
    return len
dict_files_len = {}
for filename in pathlib.Path('txt').iterdir():
    dict_files_len.update({filename.name: file_lenghs(filename)})
sorted_list_of_files_by_len = sorted(dict_files_len, key=dict_files_len.get)
with open('result.txt', 'w', encoding = 'utf-8') as f:
    for file in sorted_list_of_files_by_len:
        f.write(file + '\n')
        f.write(str(dict_files_len[file]) + '\n')
        with open(pathlib.Path('txt', file), 'r', encoding = 'utf-8') as f1:
            for line in f1.readlines():
                f.write(line)
with open('result.txt', 'r', encoding = 'utf-8') as f:
    print(f"\n{f.read()}")
