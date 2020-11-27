import os
import re

# 読み込むファイルのパスを変数に追加
path = os.path.abspath('common.txt')

# 行数を入れる変数
number_of_lines = 0

# 一つ目の要素を追加する配列
brand_list = []


# ブランド名の重複を確認する関数
def has_duplicates(seq):
    return len(seq) != len(set(seq))


# ユーザー定義例外
class Error(Exception):
    pass

# ファイルを一行ずつ読み込み
f = open(path)
lines = f.readlines()
for line in lines:
    # 行数を更新
    number_of_lines += 1

    # 改行を削除
    line = line.replace("\n", "")

    # 要素数が４つあるのかを確認：チェックポイント①-1
    # ※ブランド名にカンマが入る場合があるため、「",」で区切る
    elements = line.split('",')
    # ※要素の先頭だけにダブルクォートが付いているため、それを削除
    elements[0] = elements[0].lstrip('"')
    elements[1] = elements[1].lstrip('"')
    elements[2] = elements[2].lstrip('"')

    if len(elements) != 4:
        raise Error('要素数が不適切です：　line ' + str(number_of_lines) + ' in common.txt')

    # ４つ目以外の各要素内のダブルクォートの数を確認（ブランド名にダブルクォートが含まれていないか）：チェックポイント①-2
    if elements[0].count('"') != 0 or elements[1].count('"') != 0 or elements[2].count('"') != 0:
        raise Error('ダブルクォートの数が不適切です：　line ' + str(number_of_lines) + ' in common.txt')

    # 空白数が一致しているかの確認：チェックポイント②
    # ※末尾の空白はカウントしないため削除
    elements[1] = elements[1].rstrip(' ')
    elements[2] = elements[2].rstrip(' ')
    # ※連続する空白は１つにカウントする
    elements[1] = re.sub(" +", " ", elements[1])
    elements[2] = re.sub(" +", " ", elements[2])

    if elements[1].count(' ') != elements[2].count(' '):
        raise Error('空白数が不適切です：　line ' + str(number_of_lines) + ' in common.txt')

    # １つ目の要素を配列に追加
    brand_list.append(elements[0])

    # 開発用
    # print(elements)

# 一つ目の要素(ブランド名)に重複がないかの確認：チェックポイント③
if has_duplicates(brand_list):
    raise Error('ブランド名が重複しています')
else:
    print('テストをpassしました')
