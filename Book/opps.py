# class Book:
#     def __init__(self,nm , price, Qunty):
#         self.Name = nm
#         self.Price = int(price)
#         self.Qunty =int(Qunty) 
        



# class Novel(Book):
#     pass


# res = Novel("Ek Kahani", 450,25)
# print(res.__dict__)


class Father:
    def __init__(self,pr):
        self.property = pr



class Daughter(Father):
    def __init__(self, pr1,pr):
        self.property= pr1
        super().__init__(pr)

    # def show_property(self):
    #    print(self.property) 

res = Daughter(500,800)
print(res.__dict__)
    