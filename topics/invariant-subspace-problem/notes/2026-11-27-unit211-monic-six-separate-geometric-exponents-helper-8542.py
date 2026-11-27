#!/usr/bin/env python3
"""Exact geometric localization with separate named-factor exponents.
Companion to the monic-six helper. There is no norm or pivot inverse.
A fraction is n / product(atom[i]**pole[i]); equality uses a complete
cross multiplication in the original monic quotient. Failure to certify
equality is never advertised as proof of inequality in a localization.
"""
def make_atom_localization(A,named_factors):
    K=A.K6
    names=[];atoms=[];provenance={}
    for name,atom,origin in named_factors:
        assert isinstance(name,str) and name and name not in names
        assert isinstance(origin,str) and origin
        names.append(name);atoms.append(K(atom));provenance[name]=origin
    assert names
    count=len(names);zero_poles=(0,)*count
    powers=[[K(1),atom] for atom in atoms]
    counters=dict(cross_product_checks=0,named_geometric_inverse_checks=0,
                  checked_rebases=0)
    def power(i,n):
        assert isinstance(n,int) and n>=0
        while len(powers[i])<=n:
            powers[i].append(powers[i][-1]*atoms[i])
        return powers[i][n]
    def transport(numerator,old,new):
        assert len(old)==len(new)==count
        answer=numerator
        for i in range(count):
            assert new[i]>=old[i]
            if new[i]>old[i]:answer=answer*power(i,new[i]-old[i])
        return answer
    class Fraction:
        _isp_quotient_level=2
        __slots__=("numerator","pole_orders")
        def __init__(self,numerator=0,pole_orders=None):
            if isinstance(numerator,Fraction):
                assert pole_orders is None
                self.numerator=numerator.numerator
                self.pole_orders=numerator.pole_orders
                return
            if pole_orders is None:pole_orders=zero_poles
            assert isinstance(pole_orders,(tuple,list)) and len(pole_orders)==count
            assert all(isinstance(n,int) and n>=0 for n in pole_orders)
            self.numerator=K(numerator)
            self.pole_orders=zero_poles if self.numerator==0 else tuple(pole_orders)
        def has_zero_numerator(self):return self.numerator==0
        def __bool__(self):
            raise TypeError("No unit test: use exact cross multiplication or has_zero_numerator")
        def __add__(self,other):
            if getattr(other,"_isp_quotient_level",0)>2:return NotImplemented
            other=Fraction(other)
            if self.has_zero_numerator():return other
            if other.has_zero_numerator():return self
            pole=tuple(max(a,b) for a,b in zip(self.pole_orders,other.pole_orders))
            return Fraction(transport(self.numerator,self.pole_orders,pole)
                            +transport(other.numerator,other.pole_orders,pole),pole)
        __radd__=__add__
        def __neg__(self):return Fraction(-self.numerator,self.pole_orders)
        def __sub__(self,other):
            if getattr(other,"_isp_quotient_level",0)>2:return NotImplemented
            return self+(-Fraction(other))
        def __rsub__(self,other):return Fraction(other)+(-self)
        def __mul__(self,other):
            if getattr(other,"_isp_quotient_level",0)>2:return NotImplemented
            other=Fraction(other)
            return Fraction(self.numerator*other.numerator,
                            tuple(a+b for a,b in zip(self.pole_orders,other.pole_orders)))
        __rmul__=__mul__
        def __truediv__(self,other):
            if isinstance(other,int) and other!=0:
                return Fraction(self.numerator/other,self.pole_orders)
            raise TypeError("Use named original parameter or geometric inverses")
        def __pow__(self,n):
            if not isinstance(n,int) or n<0:raise TypeError("Only nonnegative integer powers")
            return Fraction(self.numerator**n,tuple(n*p for p in self.pole_orders))
        def equal_by_cross_product(self,other):
            other=Fraction(other)
            pole=tuple(max(a,b) for a,b in zip(self.pole_orders,other.pole_orders))
            counters["cross_product_checks"]+=1
            return (transport(self.numerator,self.pole_orders,pole)
                    ==transport(other.numerator,other.pole_orders,pole))
        def __eq__(self,other):
            if getattr(other,"_isp_quotient_level",0)>2:return NotImplemented
            return self.equal_by_cross_product(other)
    class Localization:
        pass
    out=Localization()
    out.Fraction=Fraction;out.names=tuple(names)
    out.factors=dict(zip(names,atoms));out.provenance=provenance
    out.statistics=counters;out.power=power
    inverse_cache={}
    def inverse_atom(name):
        assert name in out.factors,"unregistered geometric inverse"
        if name not in inverse_cache:
            pole=[0]*count;pole[names.index(name)]=1
            answer=Fraction(1,pole)
            assert Fraction(out.factors[name])*answer==Fraction(1)
            counters["named_geometric_inverse_checks"]+=1
            inverse_cache[name]=answer
        return inverse_cache[name]
    def inverse_parameter(name,value):
        return Fraction(A.inverse_parameter(name,value))
    def rebase_checked(value,numerator,pole_orders=None):
        value=Fraction(value);candidate=Fraction(numerator,pole_orders)
        assert value.equal_by_cross_product(candidate),"unproved denominator cancellation"
        counters["checked_rebases"]+=1
        return candidate
    out.inverse_atom=inverse_atom
    out.inverse_parameter=inverse_parameter
    out.rebase_checked=rebase_checked
    return out
