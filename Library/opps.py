


class Father:
    def __init__(self,pr):
        self.property = pr
        

    def Show_property(self):
        print(self.property)


class Son(Father):
    def __init__(self, pr1,pr):
        self.property1= pr1
        super().__init__(pr)

    def Show_property(self):
        # print(self.property+self.property1)
        print(self.property1)
        # Father.Show_property(self)              # class se father ki property acess ki
        super().Show_property()          # this is ne method t acess fathers proprty             


# res = Son(1500,2500)
# print(res.__dict__)
# (res.Show_property())


# Example of Muliple

# class Father:
#     def Father (self):
#         print("father Height :-5.7")


# class Mother:
#     def Mother (self):
#         print("Mother height:- 5.2")

# class Son(Father,Mother):
#     def son (self):
#         print("sons Height:- 5.8")


# obj = Son()
# obj.Father()
# obj.Mother()
# obj.son()


# Example of multilevel

class A:
    def m1(self):
        print("In class m1")
class B(A):
    def m2(self):
        print("In class m2")

class C(B):
    def m3(self):
        print("In class m3")

class D(C):
    def m4(self):
        print("In class m4")


# obj = D()
# obj.m1()
# obj.m2()
# obj.m3()
# obj.m4()

# print(D.__mro__)  # Method resolutins order #(<class '__main__.D'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
# dimond problem
# c3 algoritm   --> is me left most method k pass jayga    D    means A k pass ayga ye problema multiple inheretance me ata hai
                                                        # A   B
                                                           # c


# class GrandMother:
#     def __init__(self, GN):
#         self.Gname = GN

# class Mother(GrandMother):
#     def __init__(self, Mn,GN):
#         self.Mname =Mn
#         GrandMother.__init__(self,GN)



# class Daughter(Mother):
#     def __init__(self,Dn, Mn, GN):
#         self.Dname = Dn

#         Mother.__init__(self,Mn,GN)

# res = Daughter("Pret","Madhavi","Parvati")
# print(res.__dict__)



# hierarchy

# class Parent:
#     def func1(self):
#         print("In Function 1")


# class Child1(Parent):
#     def func2(self):
#         print("In function 2")

# class Child2(Parent):
#     def func3(self):
#         print("In function 3")

# res = Child1()
# res1= Child2()
# res.func1()
# res.func2()

# res1.func1()
# res1.func3()





