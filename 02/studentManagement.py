infors = []

def system_title():
    print("="*50)
    print("               学生管理系统v1.0               ")
    print("="*50)

def system_menu():
    print("1.新增学生信息")
    print("2.删除学生信息")
    print("3.修改学生信息")
    print("4.查询一名学生信息")
    print("5.查询所有学生信息")
    print("6.退出系统")

def add_student():
    infor = {}
    infor["name"]=input("请输入学生姓名:")
    infor["age"]=int(input("请输入学生年龄:"))
    infor["sex"]=input("请输入学生性别:")
    infor["addr"]=input("请输入学生家庭住址:")
    infors.append(infor)
    
def del_student():
    name = input("请输入要删除的学生姓名:")
    for infor in infors:
        if infor.get("name") == name:
            infors.remove(infor)
            print("该学生信息已删除")
            break
    else:
        print("未查询到要删除的学生信息")
        
def update_student():
    name = input("请输入要修改的学生姓名:")
    for infor in infors:
        if infor.get("name") == name:
            infor["name"]=input("请输入学生姓名:")
            infor["age"]=int(input("请输入学生年龄:"))
            infor["sex"]=input("请输入学生性别:")
            infor["addr"]=input("请输入学生家庭住址:")
            print("该学生信息已修改")
            break
    else:
        print("未查询到要修改的学生信息")
        
def find_one_student():
    name = input("请输入要查询的学生姓名:")
    for infor in infors:
        if infor.get("name") == name:
            print("姓名\t年龄\t性别\t住址\t")
            print("%s\t%d\t%s\t%s"%(infor["name"],infor["age"],infor["sex"],infor["addr"]))
            break
    else:
        print("未查询到该学生信息")
       
def find_all_student():
    print("姓名\t年龄\t性别\t住址\t")
    for infor in infors:
        print("%s\t%d\t%s\t%s"%(infor["name"],infor["age"],infor["sex"],infor["addr"]))


def main():
    while True:
        num = int(input("请选择操作编号:"))
        if num == 1:
            add_student()
            pass
        elif num == 2:
            del_student()
            pass
        elif num == 3:
            update_student()
            pass
        elif num == 4:
            find_one_student()
            pass
        elif num == 5:
            find_all_student()
            pass
        elif num == 6:
            print("谢谢使用...")
            break
        else:
            print("输入有误,重新输入")

system_title()
system_menu()
main()