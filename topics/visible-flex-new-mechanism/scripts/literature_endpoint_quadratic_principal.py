#!/usr/bin/env python3
"""R236: degree-two flat-end principal part from one original quartic DAG.

The original primitive is I=int_r^x.  At x=a+t its increment is PLUS int_0^t.
Its initial value remains the actual original raw expression at a.  Local
q=qbar=f, f'=p=sign*exp(-c/t)*a(t); only b=(log a)' Taylor coefficients are
formal independent germ parameters.  True quadratic tails are normalized
together and only exterior anchor jets are set to zero.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction as F
from math import comb
import hashlib
import json

import literature_colored_profile_algebra as colored
import literature_color_priority_words as priority

exact=colored.exact
SCHEMA="visible-flex-exact-quadratic-endpoint-principal-part-v1"


def canonical(value):
    return json.dumps(value,sort_keys=True,separators=(",",":"),
        ensure_ascii=False,allow_nan=False).encode()


def digest(value):
    return hashlib.sha256(canonical(value)).hexdigest()


def add_number(out,key,value):
    if value:
        out[key]=out.get(key,F(0))+value
        if not out[key]:
            del out[key]


def vector_rows(vector):
    return [[key,c.numerator,c.denominator] for key,c in sorted(vector.items())]


def scan_original_dag(ring,expression,budget):
    """Read only nodes reachable from this one target, including nested tails."""
    seen_atoms,seen_monomials=set(),set()
    maximum_jet=0
    maximum_power=0
    maximum_depth=0
    def monomial(key,depth=0):
        nonlocal maximum_power,maximum_depth
        power,atoms=key
        if type(power) is not int or power<0:
            raise ValueError("the frozen profile algebra must have nonnegative x powers")
        maximum_power=max(maximum_power,power)
        maximum_depth=max(maximum_depth,depth)
        if key in seen_monomials:
            return
        seen_monomials.add(key)
        for index in atoms:
            atom(index,depth)
        budget.check()
    def atom(index,depth):
        nonlocal maximum_jet,maximum_depth
        maximum_depth=max(maximum_depth,depth)
        if index in seen_atoms:
            return
        seen_atoms.add(index)
        node=ring.p.atoms[index]
        if node[0]=="jet":
            if node[1] not in ("q","qbar") or type(node[2]) is not int or node[2]<0:
                raise ValueError("only actual nonnegative q/qbar jets are allowed")
            maximum_jet=max(maximum_jet,node[2])
        elif node[0]=="int_right":
            monomial(node[1],depth+1)
        else:
            raise ValueError("unsupported actual original atom")
    for key in expression.terms:
        degree=Counter()
        for index in key[1]:
            degree.update(ring.atom_color_degree(index))
        if set(degree)-{"q","qbar"} or sum(degree.values())!=4:
            raise ValueError("one complete degree-four mixed root is required")
        monomial(key)
    return {"maximum_reachable_profile_jet":maximum_jet,
        "reachable_original_atoms":len(seen_atoms),
        "reachable_original_monomials":len(seen_monomials),
        "maximum_original_x_power":maximum_power,
        "maximum_observed_primitive_depth":maximum_depth,
        "all_original_monomials_have_actual_profile_degree_four":True,
        "scan_scope":"this one original H_E, including all nested primitive children"}


def precision_plan(maximum_jet):
    J=int(maximum_jet)
    if J<0:
        raise ValueError("nonnegative actual profile jet required")
    D=2*max(J-1,0)
    U={d:-5+(2-d)*D for d in range(3)}
    # For J>=3 this is 4J-11.  J<=2 is already zero by the pole bound.
    K=max(0,U[1]+2*max(J-2,0),2*D-9)
    return {"maximum_profile_jet":J,"single_factor_pole_bound_D":D,
        "coefficient_lower_exponents":{str(d):-d*D for d in range(3)},
        "retained_upper_exponents":{str(d):U[d] for d in range(3)},
        "maximum_log_amplitude_Taylor_index":K,
        "number_of_formal_log_amplitude_coefficients":K+1 if J>=3 else 0,
        "principal_part_exponent_min":4-2*D,
        "principal_part_exponent_max":-1,
        "principal_part_identically_zero_from_jet_bound":J<=2,
        "proof":"U_d=-5+(2-d)D; omitted errors times degree e begin above U_(d+e); positive-degree integration raises valuation by two",
        "germ_parameters":"c>0 and b_j=[t^j](a'/a); no a(0) value or tail number is assigned"}


class FlatSecondLayer:
    """Finite graded Laurent jets with coefficients in the ORIGINAL anchor ring.

    Key (d,n,k,bword) means p(t)^d*t^n*c^k*prod(b_j), coefficient a genuine
    original profile function evaluated at the fixed anchor a.  The ring x
    denotes a only in these coefficients.  Its query occurrence becomes a+t.
    Each local degree d uses its own proved upper exponent U_d.
    """
    def __init__(self,ring,budget,maximum_jet,max_terms=100000,
                 max_cache_entries=250000):
        self.ring,self.budget=ring,budget
        self.J=int(maximum_jet)
        self.plan=precision_plan(self.J)
        self.D=self.plan["single_factor_pole_bound_D"]
        self.U={int(d):v for d,v in self.plan["retained_upper_exponents"].items()}
        self.K=self.plan["maximum_log_amplitude_Taylor_index"]
        self.max_terms,self.max_cache_entries=max_terms,max_cache_entries
        self.atoms,self.monomials={},{}
        self.profile_jets={}
        self.stats={"mapped_original_atoms":0,"mapped_original_monomials":0,
            "maximum_series_keys":0,"formal_integer_rational_steps":0,
            "positive_degree_left_integrals":0,"zero_degree_left_integrals":0,
            "original_primitive_direction":"int_r_to_x",
            "left_increment_sign":"+",
            "independent_tail_symbols_created":0,
            "old_first_layer_normalizations":0,"old_quartic_normalizations":0}
        if self.J>=3:
            self._prepare_profile_jets()

    def guard(self,*series):
        self.budget.check()
        for value in series:
            self.stats["maximum_series_keys"]=max(self.stats["maximum_series_keys"],len(value))
            if len(value)>self.max_terms:
                raise exact.formal.CompilationBudgetExceeded("quadratic Laurent-series term ceiling")
        if len(self.atoms)+len(self.monomials)>self.max_cache_entries:
            raise exact.formal.CompilationBudgetExceeded("quadratic raw-DAG cache ceiling")

    def add(self,out,key,value,scale=F(1)):
        if not scale or not value.terms:
            return
        d,n,k,bword=key
        if d not in (0,1,2):
            raise ValueError("undeclared local degree")
        if n>self.U[d]:
            return
        if n < -d*self.D:
            raise AssertionError("actual series violates the proved structural pole bound")
        if any(type(j) is not int or j<0 or j>self.K for j in bword):
            raise ValueError("a log-amplitude coefficient outside the proved finite range was used")
        key=(d,n,k,tuple(sorted(bword)))
        out[key]=out.get(key,self.ring.number(0))+scale*value
        if not out[key].terms:
            del out[key]
        self.stats["formal_integer_rational_steps"]+=1
        if self.stats["formal_integer_rational_steps"]%128==0:
            self.guard(out)

    def plus(self,out,value,scale=F(1)):
        for key,c in value.items():
            self.add(out,key,c,scale)
        self.guard(out)
        return out

    def multiply(self,left,right):
        out={}
        for (d,n,k,bs),a in left.items():
            for (e,m,h,bt),b in right.items():
                degree=d+e
                if degree>2 or n+m>self.U[degree]:
                    continue
                self.add(out,(degree,n+m,k+h,tuple(sorted(bs+bt))),a*b)
        self.guard(out)
        return out

    def _scalar_add(self,out,key,value,upper):
        n,k,bword=key
        if n<=upper and value:
            add_number(out,(n,k,tuple(sorted(bword))),value)
            self.budget.check((value,))
        if len(out)>self.max_terms:
            raise exact.formal.CompilationBudgetExceeded("formal profile-jet term ceiling")

    def _prepare_profile_jets(self):
        # F_j=f^(j)/p, j>=1.  F_(j+1)=(D_t+lambda)F_j.
        # Two spare powers per remaining step cover multiplication by c*t^-2;
        # differentiation loses only one.  b_j is the Taylor coefficient, not
        # the unscaled derivative of b.
        current={(0,0,()):F(1)}
        self.profile_jets[1]={key:c for key,c in current.items() if key[0]<=self.U[1]}
        for j in range(2,self.J+1):
            upper=self.U[1]+2*(self.J-j)
            new={}
            for (n,k,bs),c in current.items():
                if n:
                    self._scalar_add(new,(n-1,k,bs),n*c,upper)
                self._scalar_add(new,(n-2,k+1,bs),c,upper)
                for r in range(self.K+1):
                    if n+r<=upper:
                        self._scalar_add(new,(n+r,k,tuple(sorted(bs+(r,)))),c,upper)
            current=new
            self.profile_jets[j]={key:c for key,c in current.items() if key[0]<=self.U[1]}
            self.guard(current)
        # f/p is the zero-left-integral solution of (D+lambda)F_0=1.
        seed={(1,0,0,()):self.ring.number(1)} if self.U[1]>=0 else {}
        fseries=self.left_integrate(seed)
        self.profile_jets[0]={
            (n,k,bs):value.terms.get((0,()),F(0))
            for (d,n,k,bs),value in fseries.items() if d==1}
        for value in fseries.values():
            if set(value.terms)-{(0,())}:
                raise AssertionError("profile f/p series acquired a false tail")

    def polynomial(self,power):
        out={}
        if self.U[0]<0:
            return out
        anchor=self.ring.x()
        for n in range(min(power,self.U[0])+1):
            self.add(out,(0,n,0,()),anchor**(power-n),F(comb(power,n)))
        return out

    def left_integrate(self,source):
        out={}
        for (d,n,k,bs),value in source.items():
            if d==0:
                if n<0:
                    raise AssertionError("zero-local-degree increments are genuine polynomials")
                if n+1<=self.U[0]:
                    self.add(out,(0,n+1,k,bs),value,F(1,n+1))
        if any(key[0]==0 for key in source):
            self.stats["zero_degree_left_integrals"]+=1
        for d in (1,2):
            rhs={key:value for key,value in source.items() if key[0]==d}
            if not rhs:
                continue
            self.stats["positive_degree_left_integrals"]+=1
            lower=-d*self.D+2
            # In (D+d lambda)S=R, coefficient t^(n-2) gives
            # d*c*S_n=R_(n-2)-(n-1)S_(n-1)-d*sum b_j*S_(n-2-j).
            solved={}
            for n in range(lower,self.U[d]+1):
                current={}
                for (dd,m,k,bs),value in rhs.items():
                    if m==n-2:
                        self.add(current,(d,n,k-1,bs),value,F(1,d))
                for (dd,m,k,bs),value in solved.items():
                    if m==n-1 and n!=1:
                        self.add(current,(d,n,k-1,bs),value,-F(n-1,d))
                    j=n-2-m
                    if 0<=j<=self.K:
                        self.add(current,(d,n,k-1,tuple(sorted(bs+(j,)))),value,F(-1))
                self.plus(solved,current)
            self.plus(out,solved)
        self.guard(out)
        return out

    def atom(self,index):
        if index in self.atoms:
            return self.atoms[index]
        node=self.ring.p.atoms[index]
        if node[0]=="jet":
            if node[1] not in ("q","qbar") or node[2]>self.J:
                raise ValueError("unscanned original local jet")
            out={}
            for (n,k,bs),c in self.profile_jets[node[2]].items():
                self.add(out,(1,n,k,bs),self.ring.number(c))
        elif node[0]=="int_right":
            out=self.left_integrate(self.monomial(node[1]))
            # This is the ACTUAL initial raw primitive at the anchor.
            self.add(out,(0,0,0,()),self.ring.monomial((0,(index,))))
        else:
            raise ValueError("unsupported original raw node")
        self.guard(out)
        if len(self.atoms)+len(self.monomials)>=self.max_cache_entries:
            raise exact.formal.CompilationBudgetExceeded("quadratic raw-DAG cache ceiling")
        self.atoms[index]=out
        self.stats["mapped_original_atoms"]+=1
        return out

    def monomial(self,key):
        if key in self.monomials:
            return self.monomials[key]
        power,atoms=key
        if type(power) is not int or power<0:
            raise ValueError("nonnegative actual polynomial query power required")
        out=self.polynomial(power)
        for index in atoms:
            out=self.multiply(out,self.atom(index))
        self.guard(out)
        if len(self.atoms)+len(self.monomials)>=self.max_cache_entries:
            raise exact.formal.CompilationBudgetExceeded("quadratic raw-DAG cache ceiling")
        self.monomials[key]=out
        self.stats["mapped_original_monomials"]+=1
        return out

    def expression(self,expression):
        if self.J<=2:
            # Proof: B has pole order <=2D<=4, hence pp(t^4 B)=0.
            # No unknown original term is discarded by an assumed jet cap.
            return {}
        out={}
        for key,c in expression.terms.items():
            self.plus(out,self.monomial(key),c)
        return {key:value for key,value in out.items() if key[0]==2}

    def original_rows(self,series):
        return [[key,self.ring.digest(value),len(value.terms)]
            for key,value in sorted(series.items())]


class QuadraticTailMap:
    """Coupled true degree-two tails; no free assignment of primitive values."""
    def __init__(self,ring,budget,max_calls=300000,max_terms=100000,
                 max_cache_entries=250000):
        self.ring,self.budget=ring,budget
        self.max_terms,self.max_cache_entries=max_terms,max_cache_entries
        self.words=priority.PriorityWords(ring,max_calls=max_calls,max_terms=max_terms,
            max_weight=2,max_shuffle_entries=max_cache_entries,
            max_cache_entries=max_cache_entries)
        self.cache={}
        self.records=[]
        self.stats={"new_quadratic_coefficients":0,"exterior_jet_terms_removed":0,
            "old_cubic_first_layer_normalizations":0,"old_quartic_normalizations":0,
            "tail_values_independently_assigned":False}

    def coefficient(self,value):
        key=value.key()
        if key in self.cache:
            return self.cache[key]
        for monomial in value.terms:
            degrees=Counter()
            for atom in monomial[1]:
                degrees.update(self.ring.atom_color_degree(atom))
            if set(degrees)-{"q","qbar"} or sum(degrees.values())!=2:
                raise ValueError("a quartic degree-two layer must have true quadratic tails")
        converted=self.words.expression(value)
        out={}
        for (local,letters),c in converted.terms.items():
            if not all(priority.is_remainder_letter(letter) for letter in letters):
                raise AssertionError("quadratic tail left the proved fixed-color remainder grammar")
            if local[1]:
                self.stats["exterior_jet_terms_removed"]+=1
                continue
            if sum(len(letter[1]) for letter in letters)!=2:
                raise ValueError("actual quadratic boundary word degree changed")
            add_number(out,(local[0],letters),c)
        if len(out)>self.max_terms or len(self.cache)>=self.max_cache_entries:
            raise exact.formal.CompilationBudgetExceeded("quadratic true-tail normalization ceiling")
        self.records.append({"original_coefficient_sha256":self.ring.digest(value),
            "original_terms":len(value.terms),
            "complete_quadratic_word_sha256":priority.digest(priority.rows(converted)),
            "boundary_word_sha256":digest(vector_rows(out)),
            "boundary_word_terms":len(out),"all_letters_in_proved_remainder_grammar":True,
            "only_exterior_anchor_jets_set_to_zero":True,
            "original_right_primitive_direction":"int_r_to_x"})
        self.cache[key]=out
        self.stats["new_quadratic_coefficients"]+=1
        self.budget.check()
        return out

    def principal_part(self,series):
        out={}
        for (d,n,k,bs),value in sorted(series.items()):
            if d!=2 or n+4>=0:
                raise ValueError("only the proved negative powers of t^4 B may be consumed")
            for (anchor,letters),c in self.coefficient(value).items():
                add_number(out,(n+4,k,bs,anchor,letters),c)
        if len(out)>self.max_terms:
            raise exact.formal.CompilationBudgetExceeded("quadratic principal-part row ceiling")
        self.budget.check(out.values())
        return out


def compute_one(ring,expression,args,budget):
    scan=scan_original_dag(ring,expression,budget)
    J=scan["maximum_reachable_profile_jet"]
    if J>args.max_profile_jet:
        raise exact.formal.CompilationBudgetExceeded(
            "the actual reachable jet exceeds the declared new-series budget")
    mapper=FlatSecondLayer(ring,budget,J,args.max_terms,args.max_cache_entries)
    series=mapper.expression(expression)
    tails=QuadraticTailMap(ring,budget,args.max_IBP_calls,args.max_terms,args.max_cache_entries)
    result=tails.principal_part(series)
    return result,mapper,tails,series,scan


def artificial_checks(ring,budget,args):
    """Only invented quartic expressions; never read any actual repository input."""
    q,qb,x=ring.color("q"),ring.color("qbar"),ring.x()
    q2=q.D().D()
    q3=q2.D()
    tau=(qb*qb).I()
    checks={}
    direct=q3*q3*tau
    pp,mapper,tails,series,scan=compute_one(ring,direct,args,budget)
    expected={
        (2,-8,4,()):tau,
        (2,-7,3,()):-4*tau,
        (2,-6,2,()):4*tau,
        (2,-6,3,(0,)):4*tau,
        (2,-5,2,(0,)):-8*tau,
        (2,-5,3,(1,)):4*tau}
    def equal_original(actual,wanted):
        return (set(actual)==set(wanted)
            and all(not (actual[k]-wanted[k]).terms for k in wanted))
    checks["universal_c_and_b0_b1_direct_quadratic_layer"]=equal_original(series,expected)
    checks["actual_reachable_J3_has_proved_degree_dependent_precision"]=(
        scan["maximum_reachable_profile_jet"]==3
        and mapper.U=={0:3,1:-1,2:-5} and mapper.K==1 and bool(pp))
    one,imapper,itail,iseries,_=compute_one(ring,direct.I(),args,budget)
    wanted={(2,-6,3,()):tau/2,(2,-5,2,()):-tau/2}
    checks["original_int_r_to_x_has_positive_zero_left_increment"]=equal_original(iseries,wanted) and bool(one)
    twice,tmapper,ttail,tseries,tscan=compute_one(ring,direct.I().I(),args,budget)
    checks["two_nested_left_integrals_cross_the_principal_threshold"]=(
        not twice and not tseries and tscan["maximum_reachable_profile_jet"]==3)
    outer,omapper,otail,oseries,_=compute_one(ring,x*direct,args,budget)
    owanted={}
    for (d,n,k,bs),v in expected.items():
        owanted[(d,n,k,bs)]=owanted.get((d,n,k,bs),ring.number(0))+x*v
        if n+1<=-5:
            key=(d,n+1,k,bs)
            owanted[key]=owanted.get(key,ring.number(0))+v
    owanted={k:v for k,v in owanted.items() if v.terms}
    checks["query_polynomial_is_anchor_plus_t_not_anchor_alone"]=equal_original(oseries,owanted)
    boundary=(qb*qb).D().I()
    bpp,_,_,_,_=compute_one(ring,q3*q3*boundary,args,budget)
    checks["true_quadratic_derivative_boundary_has_zero_exterior_value"]=not bpp
    shuffle=q.I()*qb.I()-(q*qb.I()+qb*q.I()).I()
    spp,_,_,_,_=compute_one(ring,q3*q3*shuffle,args,budget)
    checks["true_quadratic_shuffle_is_not_independent_tail_data"]=not spp
    low,lmapper,ltail,lseries,lscan=compute_one(ring,q2*q2*tau,args,budget)
    checks["jet_two_boundary_case_has_no_negative_part_without_NF"]=(
        not low and not lseries and lscan["maximum_reachable_profile_jet"]==2
        and lmapper.plan["principal_part_identically_zero_from_jet_bound"]
        and not ltail.records)
    local,_,_,_,_=compute_one(ring,q3*q3*q2*q2,args,budget)
    checks["local_degree_four_cannot_leak_into_degree_two"]=not local
    # One higher artificial jet proves that the largest required log-amplitude
    # coefficient is retained; q''''/p begins with c^3 t^-6.
    q4=q3.D()
    hpp,hmapper,htail,hseries,hscan=compute_one(ring,q4*q4*tau,args,budget)
    k=(2,-5,5,(5,))
    checks["J4_keeps_the_required_b5_boundary_coefficient"]=(
        hscan["maximum_reachable_profile_jet"]==4
        and hmapper.U=={0:7,1:1,2:-5} and hmapper.K==5
        and k in hseries and not (hseries[k]-6*tau).terms and bool(hpp))
    interior=(qb.D()*qb.D()).I()
    ipp,_,it,_,_=compute_one(ring,q3*q3*interior,args,budget)
    checks["anchor_zeroing_keeps_derivatives_inside_tail_letters"]=(
        bool(ipp) and all(r["only_exterior_anchor_jets_set_to_zero"] for r in it.records))
    checks["no_old_first_layer_or_independent_tail_assignment"]=(
        mapper.stats["independent_tail_symbols_created"]==0
        and mapper.stats["old_first_layer_normalizations"]==0
        and tails.stats["old_cubic_first_layer_normalizations"]==0
        and tails.stats["tail_values_independently_assigned"] is False)
    return checks
