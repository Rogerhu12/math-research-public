#!/usr/bin/env python3
"""R230: exact local-degree <=1 map with coupled original right-tail values.

The frozen raw primitive I is int_r^x, so I(E)(X)=I(E)(a)+int_a^X E.
Only coefficient functions of total profile degree three are normalized.
No full quartic normal form, profile evaluation or research entry point.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction as F
import hashlib
import json

import literature_colored_profile_algebra as colored
import literature_color_priority_words as priority

exact=colored.exact
SCHEMA="visible-flex-exact-first-endpoint-layer-v1"


def canonical(value):
    return json.dumps(value,sort_keys=True,separators=(",",":"),
                      ensure_ascii=False,allow_nan=False).encode()


def digest(value):
    return hashlib.sha256(canonical(value)).hexdigest()


def sparse_add(row,key,value):
    if not value:
        return
    row[key]=row.get(key,F(0))+value
    if not row[key]:
        del row[key]


def vector_rows(vector):
    return [[key,c.numerator,c.denominator] for key,c in sorted(vector.items())]


def expression_rows(mapping,ring):
    return [[key,ring.digest(value),len(value.terms)]
            for key,value in sorted(mapping.items())]


class FirstLayer:
    """Polynomial in query X; coefficients are actual raw functions at anchor a.

    zero[n] means X^n times an original expression evaluated at a.
    linear[(kind,n,j)] means X^n D^j f (kind='d') or
    X^n int_a^X s^j f(s)ds (kind='i'), with a coupled raw tail coefficient.
    The original ring's x variable denotes a only in these coefficients.
    """
    def __init__(self,ring,budget,max_terms=100000,max_cache_entries=200000):
        self.ring,self.budget=ring,budget
        self.max_terms,self.max_cache_entries=max_terms,max_cache_entries
        self.atoms,self.monomials={},{}
        self.stats={"raw_atoms":0,"raw_monomials":0,"max_zero_terms":0,
                    "max_linear_terms":0,"raw_primitive_direction":"int_r_to_x",
                    "independent_tail_symbols_created":0}

    def guard(self,zero=None,linear=None):
        self.budget.check()
        if len(self.atoms)+len(self.monomials)>self.max_cache_entries:
            raise exact.formal.CompilationBudgetExceeded("first-layer raw-cache ceiling")
        for data,label in ((zero,"zero"),(linear,"linear")):
            if data is not None:
                self.stats["max_"+label+"_terms"]=max(self.stats["max_"+label+"_terms"],len(data))
                if len(data)>self.max_terms:
                    raise exact.formal.CompilationBudgetExceeded("first-layer "+label+" term ceiling")

    def add(self,target,key,value):
        if not value.terms:
            return
        target[key]=target.get(key,self.ring.number(0))+value
        if not target[key].terms:
            del target[key]

    def add_pair(self,target,source,scale=F(1)):
        for part in (0,1):
            for key,value in source[part].items():
                self.add(target[part],key,scale*value)
        self.guard(*target)
        return target

    def multiply(self,left,right):
        zero,linear={},{}
        for n,a in left[0].items():
            for m,b in right[0].items():
                self.add(zero,n+m,a*b)
            for (kind,m,j),b in right[1].items():
                self.add(linear,(kind,n+m,j),a*b)
        for n,a in right[0].items():
            for (kind,m,j),b in left[1].items():
                self.add(linear,(kind,n+m,j),a*b)
        self.guard(zero,linear)
        return zero,linear

    def left_integrate(self,pair):
        zero,linear={},{}
        anchor=self.ring.x()
        for n,c in pair[0].items():
            self.add(zero,n+1,c/F(n+1))
            self.add(zero,0,-c*anchor**(n+1)/F(n+1))
        for (kind,n,j),c in pair[1].items():
            if kind=="i":
                self.add(linear,("i",n+1,j),c/F(n+1))
                self.add(linear,("i",0,n+j+1),-c/F(n+1))
            elif kind=="d" and j==0:
                self.add(linear,("i",0,n),c)
            elif kind=="d" and j>0:
                falling=1
                for i in range(min(n,j-1)+1):
                    if i:
                        falling*=n-i+1
                    self.add(linear,("d",n-i,j-1-i),c*((-1)**i)*falling)
                if j<=n:
                    falling=1
                    for i in range(j):
                        falling*=n-i
                    self.add(linear,("i",0,n-j),c*((-1)**j)*falling)
            else:
                raise ValueError("undeclared linear local operator")
        self.guard(zero,linear)
        return zero,linear

    def atom(self,index):
        if index in self.atoms:
            return self.atoms[index]
        node=self.ring.p.atoms[index]
        if node[0]=="jet":
            if node[1] not in ("q","qbar"):
                raise ValueError("first f-up local substitution requires only q/qbar")
            answer=({}, {("d",0,node[2]):self.ring.number(1)})
        elif node[0]=="int_right":
            # Preserve the actual raw primitive, including every nested child.
            answer=self.left_integrate(self.monomial(node[1]))
            self.add(answer[0],0,self.ring.monomial((0,(index,))))
        else:
            raise ValueError("unsupported original atom in first layer")
        self.guard(*answer)
        if len(self.atoms)+len(self.monomials)>=self.max_cache_entries:
            raise exact.formal.CompilationBudgetExceeded("first-layer raw-cache ceiling")
        self.atoms[index]=answer
        self.stats["raw_atoms"]+=1
        return answer

    def monomial(self,key):
        if key in self.monomials:
            return self.monomials[key]
        power,factors=key
        if type(power) is not int or power<0:
            raise ValueError("declared original profile powers must be nonnegative")
        answer=({power:self.ring.number(1)}, {})
        for index in factors:
            answer=self.multiply(answer,self.atom(index))
        self.guard(*answer)
        if len(self.atoms)+len(self.monomials)>=self.max_cache_entries:
            raise exact.formal.CompilationBudgetExceeded("first-layer raw-cache ceiling")
        self.monomials[key]=answer
        self.stats["raw_monomials"]+=1
        return answer

    def expression(self,expression):
        answer=({}, {})
        for key,c in expression.terms.items():
            self.add_pair(answer,self.monomial(key),c)
        return answer


class CubicTailMap:
    """Normalize only degree-three coefficients, then set EXTERIOR jets at a to zero.

    Word letters remain full q/qbar functions on the complete right interval.
    The output rows retain the negative right-primitive word convention.
    """
    def __init__(self,ring,budget,max_calls=300000,max_terms=100000,max_cache_entries=200000):
        self.ring,self.budget=ring,budget
        self.max_terms,self.max_cache_entries=max_terms,max_cache_entries
        self.words=priority.PriorityWords(ring,max_calls=max_calls,max_terms=max_terms,
            max_weight=3,max_shuffle_entries=max_cache_entries,
            max_cache_entries=max_cache_entries)
        self.coefficients={}
        self.records=[]
        self.stats={"new_cubic_coefficients":0,"exterior_jet_terms_removed":0,
                    "quartic_roots_normalized":0,"tail_values_independently_assigned":False}

    def coefficient(self,value):
        key=value.key()
        if key in self.coefficients:
            return self.coefficients[key]
        for monomial in value.terms:
            degree=Counter()
            for atom in monomial[1]:
                degree.update(self.ring.atom_color_degree(atom))
            if set(degree)-{"q","qbar"} or sum(degree.values())!=3:
                raise ValueError("the first quartic layer must have cubic true tail coefficients")
        word=self.words.expression(value)
        out={}
        for (local,letters),c in word.terms.items():
            if not all(priority.is_remainder_letter(letter) for letter in letters):
                raise AssertionError("new cubic coefficient left the proved R179 grammar")
            if local[1]:
                self.stats["exterior_jet_terms_removed"]+=1
                continue
            if sum(len(letter[1]) for letter in letters)!=3:
                raise ValueError("boundary cubic word has wrong actual degree")
            sparse_add(out,(local[0],letters),c)
        if len(out)>self.max_terms or len(self.coefficients)>=self.max_cache_entries:
            raise exact.formal.CompilationBudgetExceeded("new cubic boundary-map ceiling")
        self.records.append({"original_coefficient_sha256":self.ring.digest(value),
            "original_terms":len(value.terms),"full_cubic_word_sha256":priority.digest(priority.rows(word)),
            "boundary_word_sha256":digest(vector_rows(out)),
            "boundary_word_terms":len(out),"right_primitive_direction":"int_r_to_x",
            "all_letters_in_R179_grammar":True,"exterior_jets_only_set_to_zero":True})
        self.coefficients[key]=out
        self.stats["new_cubic_coefficients"]+=1
        self.budget.check()
        return out

    def layer(self,pair):
        out={}
        for (kind,n,j),value in sorted(pair[1].items()):
            for (anchor_power,letters),c in self.coefficient(value).items():
                sparse_add(out,("linear",kind,n,j,anchor_power,letters),c)
        if len(out)>self.max_terms:
            raise exact.formal.CompilationBudgetExceeded("new first-layer row ceiling")
        self.budget.check(out.values())
        return out


def original_first_layer(ring,expression,args,budget,calls=None):
    """A fresh first-layer conversion, not a full quartic normal form."""
    first=FirstLayer(ring,budget,args.max_terms,args.max_cache_entries)
    tail=CubicTailMap(ring,budget,args.max_IBP_calls if calls is None else calls,
                      args.max_terms,args.max_cache_entries)
    pair=first.expression(expression)
    vector=tail.layer(pair)
    return vector,first,tail,pair


def artificial_checks(ring,budget,args):
    """Only invented tiny expressions; never load real inputs."""
    q,qb,x=ring.color("q"),ring.color("qbar"),ring.x()
    checks={}
    first=FirstLayer(ring,budget,2000,5000)
    cubic=(qb**3).I()
    pair=first.expression(q*cubic)
    checks["raw_cubic_tail_retained_not_assigned"]=(
        len(pair[1])==1 and not (pair[1][("d",0,0)]-cubic).terms)
    nested=first.expression((q*cubic).I())
    checks["raw_int_r_to_x_uses_positive_left_increment"]=(
        len(nested[1])==1 and not (nested[1][("i",0,0)]-cubic).terms)
    high=first.expression((x*x*q.D().D()).I())[1]
    checks["left_IBP_keeps_all_derivative_boundary_terms"]=(
        set(high)=={("d",2,1),("d",1,0),("i",0,0)}
        and not (high[("d",2,1)]-1).terms
        and not (high[("d",1,0)]+2).terms
        and not (high[("i",0,0)]-2).terms)
    twice=first.expression((x*x*(x**3*q).I()).I())[1]
    checks["nested_left_moment_reduction"]=(
        set(twice)=={("i",3,3),("i",0,6)}
        and not (twice[("i",3,3)]-F(1,3)).terms
        and not (twice[("i",0,6)]+F(1,3)).terms)
    tail=CubicTailMap(ring,budget,5000,5000,10000)
    boundary_zero=tail.layer(first.expression(q*(qb**3).D().I()))
    checks["cubic_exact_derivative_has_zero_true_boundary_value"]=not boundary_zero
    shuffle=(q*q).I()*qb.I()-((q*q)*qb.I()+qb*(q*q).I()).I()
    checks["real_cubic_shuffle_relations_not_free_tail_symbols"]=not tail.layer(first.expression(q*shuffle))
    left=tail.layer(first.expression(q*cubic.I()))
    right=tail.layer(first.expression(q*(x*cubic-(x*qb**3).I())))
    checks["nested_true_anchor_polynomial_relation"]=left==right
    checks["purely_local_quartic_has_no_first_layer"]=not tail.layer(first.expression(q**4))
    return checks
