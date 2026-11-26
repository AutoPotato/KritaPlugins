from krita import *

dockersList = Krita.instance().dockers()
#Krita.instance().dockers().children()
#for docker in dockersList:
#for i, d in enumerate(dockersList):
#    print(i, d.objectName(), d.windowTitle())

#IT'S NOT ALWAYS THE 30TH ITEM
toolbox = dockersList[30]
#toolchild = toolbox.children()
#print(dir(toolbox))
#print(dir(toolbox.windowIcon()))
#print(toolbox.windowIcon().name())
#print(type(toolbox.windowIcon()))

#toolchild = toolchild[1].icon()
#print(toolchild)

#for i in toolchild:
#    print(i)
#    print(type(i))
#    print(dir(i)
#    print(type(i.children()))
#
count = 0

def pleaseFindtheThing(item, indent=0):
    global count 
    count = count + 1
    print(count,"    " * indent + str(item.objectName()))
    if item.objectName() == "SvgTextTool":
        item.setIcon(QIcon('Text.png'));
    
    for k in item.children():
        pleaseFindtheThing(k, indent + 1)

pleaseFindtheThing(toolbox)

#print(toolbox.children()[4])
#print(toolbox.children()[4].children()[1].children()[1].children())
#print(Krita.instance().dockers()[30].children(1))

print("\r--------------------------------------------------->end\r")