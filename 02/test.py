def test(a,b,func):
    result = func(a,b)
    print(result)
func = eval(input("输入函数："))
test(11,22,func)    
