class Point:
    def __init__(self,x,y): # is used a constructor
        self.x=x
        self.y=y
    def move(self):
        print("move")

#self is used to point to the object
#self is always first parameter in evry function in class

point =Point(10,20)




#inheritance

class mam:
    def walk(self):
        print("yolo")


class cat(mam):
    # python doesn't allow empty classes
    pass # so we use pass



# each file is called a module
#each directory is a oackage