# ローマ数字を表すクラスRomanNumeralsを定義しなさい。

# ただし，オブジェクト変数として整数の値を持ち，

# 以下の３つのオブジェクトメソッドを定義すること

# ・__init__：文字列または整数を引数としてとる

# ・__str__：ローマ数字の文字列を返す

# ・__add__：引数のオブジェクト変数を足し合わせた値を変数に持つ新たな RomanNumerals オブジェクトを生成する

# 実装例（部分）

# class RomanNumerals :
#   def  __init__ #以下省略
# #以下省略
# テスト例

# r_num1 = RomanNumerals(8)
# r_num2 = RomanNumerals('IX')
# r_num3 = r_num1+r_num2
# print(r_num1, '+', r_num2, '=', r_num3)
# 実行例

# VIII + IX = XVII


class RomanNumerals():
    def __init__(self, num):
        self.num = num
        if isinstance(num, str):
            self.num = romanToDecimal(num)  

    def __str__(self):
        return f"{int_to_Roman(self.num)}"

    def __add__(self, other):
        return RomanNumerals(self.num + other.num)


def int_to_Roman(num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num

def value(r):
    if (r == 'I'):
        return 1
    if (r == 'V'):
        return 5
    if (r == 'X'):
        return 10
    if (r == 'L'):
        return 50
    if (r == 'C'):
        return 100
    if (r == 'D'):
        return 500
    if (r == 'M'):
        return 1000
    return -1
 
def romanToDecimal(str):
    res = 0
    i = 0
 
    while (i < len(str)):
 
        # Getting value of symbol s[i]
        s1 = value(str[i])
 
        if (i + 1 < len(str)):
 
            # Getting value of symbol s[i + 1]
            s2 = value(str[i + 1])
 
            # Comparing both values
            if (s1 >= s2):
 
                # Value of current symbol is greater
                # or equal to the next symbol
                res = res + s1
                i = i + 1
            else:
 
                # Value of current symbol is greater
                # or equal to the next symbol
                res = res + s2 - s1
                i = i + 2
        else:
            res = res + s1
            i = i + 1
 
    return res


r_num1 = RomanNumerals(8)
r_num2 = RomanNumerals('IX')
r_num3 = r_num1+r_num2
print(r_num1, '+', r_num2, '=', r_num3)