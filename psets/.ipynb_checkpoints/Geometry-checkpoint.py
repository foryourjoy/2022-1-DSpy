class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def __str__(self):
        return 'A point at ({},{})'.format(self.x,self.y)
    
    def __repr__(self):
        return 'Point({},{})'.format(self.x,self.y)
        
    def halfway(self,q):
        h=(self.x+q.x)/2
        a=(self.y+q.y)/2
        return Point(h,a)
    
    def midpoint(p,q):
        h=(p.x+q.x)/2
        a=(p.y+q.y)/2
        return Point(h,a)
    
    def reflect_x(self):
        i=-self.y
        return Point(self.x,i)
    
    def slope_to_origin(self):
        s=(self.y/self.x)
        return s
    
class Square:
    def __init__(self,side):
        self.s=side
        
    def __str__(self):
        return '{} X {} Square'.format(self.s,self.s)
    
    def __repr__(self):
        return 'Square({})'.format(self.s)
        
    def perimeter(self):
        k=self.s*4
        return k
    
    def area(self):
        j=self.s*self.s
        return j
    
class Circle:
    def __init__(self,r=0):
        self.__r=r
        
    def __str__(self):
        return 'A circle with a radius of {}cm'.format(self.__r)
    
    def __repr__(self):
        return 'Circle({})'.format(self.__r)
    
    def radius(self):
        return self.__r
    
    def diameter(self):
        return self.__r*2
