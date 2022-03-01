class Parent(object):

    def __init__(self):
        #does something
        pass

    def method_parent(self):
        print ("Parent")

class Child(Parent):

    def __init__(self):
        Parent.__init__(self)

    def method_parent_masood(self):
        super().method_parent()
        print ("Child")


new = Child()
new.method_parent_masood()
