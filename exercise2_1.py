from thinkbayes import Suite

class Bowl(dict):
    def __init__(self, *args, **kwargs):
        dict.__init__(self,*args,**kwargs)
        for flavor, num_cookies in self.iteritems():
            assert num_cookies >= 0, "no negative cookies!"

    def eat(self,flavor):
        likelihood = self[flavor]
        self[flavor] -= 1
        if self[flavor] < 0:
            self[flavor] = 0
        return likelihood

class Cookie(Suite):
    '''hypos should be a dict like:
        {
            'Bowl 1' : Bowl(vanilla=12, chocolate=10),
            'Bowl 2' : Bowl(vanilla=3, chocolate=8)
        }'''

    def __init__(self,bowls):
        Suite.__init__(self,bowls.keys())
        self.bowls = bowls

    def Likelihood(self, flavor, hypo):
        bowl = self.bowls[hypo]
        likelihood = bowl.eat(flavor)
        return likelihood