from django.shortcuts import render
import datetime

def fliter(req):
    lst = ["苹果","橘子","香蕉","西瓜"]
    default = None  # 该变量是一个空值
    value1= "Django"
    nowtime = datetime.datetime.now()
    return render(req,"fliter.html",{
                                        "list":lst,
                                        "Empty":default,
                                        "value1":value1,
                                        "nowtime":nowtime
    })
