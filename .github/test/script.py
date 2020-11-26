import os

# 読み込むファイルのパスを変数に追加
path = os.path.abspath('test.txt')

# 一つ目の要素を追加する配列
brand_list = []


class Error(Exception):
    pass


# ブランド名の重複を確認する関数
def has_duplicates(seq):
    return len(seq) != len(set(seq))


# ファイルを一行ずつ読み込み
f = open(path)
lines = f.readlines()
for line in lines:
    # 改行を削除
    line = line.replace("\n", "")

    # 要素数を取得し、要素数が４つあるのかを確認：チェックポイント①
    elements = line.split(',')
    if len(elements) != 4:
        raise Error('要素数が違います')
        # print('要素数が違います')
        # break
    
    # ４つ目以外の各要素内のダブルクォートの数を確認：チェックポイント①

    elements_one = elements[0]
    elements_two = elements[1]
    elements_three = elements[2]
    if elements_one.count('"') != 2 or elements_two.count('"') != 2 or elements_three.count('"') != 2:
        print('ダブルクォートの数が不適切です')
        break

    # elements.remove('カスタム名詞-brand')
    # for element in elements:
    #   if element.count('"') != 2:
    #     print('ダブルクォートの数が不適切です')
    #     break

    # 空白数が一致しているかの確認：チェックポイント②
    if elements[1].count(' ') != elements[2].count(' '):
        print('空白数が違います')
        break

    # １つ目の要素を配列に追加
    brand_list.append(elements[0])

    # 開発用
    print(elements)

# 一つ目の要素(ブランド名)に重複がないかの確認：チェックポイント③
print(has_duplicates(brand_list))