class FabNum:
    def fab_recursive(self, n):
        if(n <= 1):
            return 1
        return self.fab_recursive(n-1) + self.fab_recursive(n-2)
    def fab_table(self,n):
        """
        docstring
        """
        if n <=1:
            return 1
        n0=0
        n1=1
        r=0
        for _ in range(2,n+2):
            r=n0+n1
            n0=n1
            n1=r
        return n1