# class FirstClass:
#     pass


# a = FirstClass()
# b = FirstClass()

# print(a)
# print(b)
# print(a is b)

# --------------------------------------------------
# class Point:
#     pass


# p1 = Point()
# p2 = Point()

# # you can assign value to coordinates
# # even though there is no arrtibute in the class
# p1.x = 5
# p1.y = 10

# p2.x = 44
# p2.y = 55

# print(p1.x, p1.y)
# print(p2.x, p2.y)


# ----------------Making it do something ---------------------------------------
# class Point:
#     def reset(self):
#         self.x = 0
#         self.y = 0


# p = Point()
# p.x = 25
# p.y = 38
# # you can also explicitly pass the object
# # this is not good practice
# # Point.reset(p)
# p.reset()
# print(p.x, p.y)


# ----------------- class method without passing the self------------
class Point:
    def reset():
        pass


p = Point
