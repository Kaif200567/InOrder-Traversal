class Node:
    def __init__ (self, val):
        self.childleft = None
        self.childright = None
        self.nodedata = val

root = Node("Kaif")
root.childleft = Node("name")
root.childright = Node("!")
root.childleft.childleft = Node("My")
root.childleft.childright = Node("is")



message = input("Solve In order traversal, Type root: ")
print()
def trying():
    if message == "root":
        def InOrd(root):
            if root:
                InOrd(root.childleft)
                print(root.nodedata)
                InOrd(root.childright)
    InOrd(root)
trying()