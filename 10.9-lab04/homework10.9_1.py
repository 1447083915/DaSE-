def Ten_to_Two (num):  #十进制转换成int型二进制
    result = 0
    time = 1
    while(num/2 > 0):
        i = (num % 2)*time
        result = result + i
        time = time*10
        num =  int(num/2)
    return result

x = input()      #输入IP地址并转换为数字数组
x2 = x.split('.')
num_list = []
for i in range(4):
    num_list.append(str(Ten_to_Two(int(x2[i]))))
print(num_list[0].rjust(8,'0')+(num_list[1].rjust(8,'0'))+(num_list[2].rjust(8,'0'))+(num_list[3].rjust(8,'0')))