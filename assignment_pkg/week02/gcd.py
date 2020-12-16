class GCD:
    def gcd_naive(self,a,b):
        """
        docstring
        """
        d=1
        for i in range(1,a+b):
            if a % i == 0 and b % i==0:
                d=i
        return d
    
    def gcd(self,a,b):
        """
        a^ = when a is divded by b
        """
        assert a > 0 and b > 0
        r=a%b
        if r == 0:
            return b
        else:
            return self.gcd(b,r)                                                                   
