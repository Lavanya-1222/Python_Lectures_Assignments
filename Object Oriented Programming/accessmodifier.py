"""
Access Modifier / Access Specifier
    Controls the accessibility of the class members(attributes,methods)

Types:
1-public: Everyonecan access
2-protected: access by the same class and child classes
3-private: access by the same class only 

"""


class A:
    def __init__(self):
        self.a=4    #public
        self._b=5   #protected
        self.__c=10 #private