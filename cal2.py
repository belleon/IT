from math import *
def calc(string):
    digit= {'ноль':0,'один': 1, 'два': 2, 'три': 3, 'четыре': 4, 'пять': 5, 'шесть': 6, 'семь': 7, 'восемь': 8, 'девять': 9,'десять': 10, 'одиннадцать': 11, 'двенадцать': 12, 'тринадцать': 13, 'четырнадцать': 14, 'пятнадцать': 15,'шестнадцать': 16, 'семнадцать': 17, 'восемнадцать': 18, 'девятнадцать': 19,'двадцать': 20, 'тридцать': 30, 'сорок': 40, 'пятьдесят': 50, 'шестьдесят': 60, 'семьдесят': 70,'восемьдесят': 80, 'девяносто': 90,'сто': 100, 'двести': 200, 'триста': 300, 'четыреста': 400, 'пятьсот': 500, 'шестьсот': 600, 'семьсот': 700,'восемьсот': 800, 'девятьсот': 900, 'тысяча':1000,"две тысячи":2000,"три тысячи":3000,"четыре тысячи":4000,"пять тысяч":5000,"шесть тысяч":6000,"семь тысяч":7000,"восемь тысяч":8000,"девять тысяч":9000}
    operations={"плюс":lambda x,y:x+y,"минус":lambda x,y:x-y,'умножить на':lambda x,y:x*y,'размещений из':lambda x,y:factorial(x)/factorial(x-y)}

    def numberToName(number):
        digit1={y:x for x,y in digit.items()}
        negative='' if number>0 else 'минус '
        ans = []
        number=abs(number)
        while number != 0:
            curnumber=number
            while curnumber not in digit1 :
                curnumber = int(str(curnumber)[1:])
            ans.append(digit1.get(curnumber))
            number-=curnumber
        return negative+' '.join(ans[::-1])
    def tran(sr):
        return sum((digit.get(n) for n in sr.split()))
    for operation in operations:
        if operation in string:
            str1 = string.split(operation)
            str1 = [i.strip() for i in str1]
            ans=operations.get(operation)(tran(str1[0]),tran(str1[1]))
    return numberToName(ans)
print(calc(input()))