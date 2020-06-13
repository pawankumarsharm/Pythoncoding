class D:pass
class E:pass
class F:pass
class B(D,E):pass
class C(D,F):pass
class A(B,C):pass
a=A()
a.m1()#A+B+C+D+E+F+O

''' File "C:\Users\bikram chandra\AppData\Local\Programs\Python\Python38-32\C3ALGORITHAM.PY", line 8, in <module>
    a.m1()#A+B+C+D+E+F+O
AttributeError: 'A' object has no attribute 'm1''''