class fraction(object):
    def __init__(self,n=None,d=None):
        self.numerator = n
        self.denominator = d

    def __str__(self):
        return "%s / %s" % (self.numerator , self.denominator)

    def numerator(self,n):
        self.numerator = n 

    def denominator(self,d):
        self.denominator = d

    def __mul__(self,rhs):
        x = self.numerator * rhs.numerator
        y = self.denominator * rhs.denominator
        return fraction(x,y)

    def mixed(self):
        whole,n2 = divmod(self.numerator,self.denominator)
        if self.denominator == 1:
            return str(self.numerator)
        elif whole == 0:
            return "%s%s" % (n2,self.denominator)
        else:
            return "%s and %s/%s" % (whole,n2,self,d) 

    def __add__(self,otherfraction):
        newnum = self.numerator*otherfraction.denominator +self.denominator*otherfraction.numerator
        newden = self.denominator*otherfraction.denominator
        print ('%d/%d + %d/%d = %d %d/%d'% (self.numerator,self.denominator,
                                            otherfraction.numerator
                                            ,otherfraction.denominator
                                            ,newnum//newden, newnum %
                                            newden,newden))
        return fraction(newnum,newden)

if __name__ == '__main__':
    a = fraction(1,2)
    b = fraction(4,5)
    c = a * b
    d = a + b
