num = int(input())
a1 = num // 100
a2 = (num // 10) % 10
a3 = num % 10
summ = a1 + a2 +a3
reverd_num =  a3*100 + a2*10 + a1
print(summ, reverd_num)
#через строки
s_num = str(num) summ_str = sum(int(c) for c in s_num) print(summ_str, {s_num[::-1]})
