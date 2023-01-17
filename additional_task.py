#  Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный. 
    
#     *Пример:* 
    
#     2+2 => 4; 
    
#     1+2*3 => 7; 
    
#     1-2*3 => -5;

def preparation(equation_list: list, operator: str):
    res = None
    for i in range(len(equation_list)-1,0,-1):
        if str(equation_list[i]) in operator:
            left = equation_list[i-1]
            right = equation_list[i+1]
            res = operation[equation_list[i]](left, right)
            equation_list[i] = res
            equation_list.pop(i+1)
            equation_list.pop(i-1)
    print(f'{equation_list} после операции "{operator}"')
    return equation_list

operation = {
    "+" : lambda x, y: x+y,
    "*" : lambda x, y: x*y,
    "-" : lambda x,y : x-y,
    "/" : lambda x,y: x/y if y != 0 else None   
}


user_string = input("Введите выражение в формате a*b-c/d+e: ")
user_string= (user_string.strip() 
                        .replace('+',' + ')
                        .replace('*'," * ")
                        .replace('-', ' + -')
                        .replace('/',' / ')
                        .split())
user_string = [int(x) if x not in '*/+' else x for x in user_string]
user_string = user_string[1:] if user_string[0] == '+' else user_string
print(f'{user_string} <= после парсинга')

for item in '*/+':
    preparation(user_string, item)


