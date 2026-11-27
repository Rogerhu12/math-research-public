#!/usr/bin/env python3
"""Bounded original level-47 finite-field Miller logarithmic derivatives.

Only the pinned public Actions job may execute this module.  The field worker
is a fresh Python process: Sage and the pip python-flint wheel are NEVER
imported in the same process.  All divisor arithmetic uses the certified
original L^1,...,L^5 and its 836 actual cusp coefficients.
"""
import argparse
import hashlib
import importlib.util
import json
import multiprocessing
import os
from pathlib import Path
import random
import signal
import subprocess
import sys
import time
import traceback

ROOT=Path(__file__).resolve().parents[3]
PRE="topics/serre-uniformity/"
REPO="Rogerhu12/math-research-public"
REQUEST=ROOT/(PRE+"notes/full-p47-finite-third-kind-request.json")
WORKER=PRE+"scripts/full_p47_Miller_support.py"
GRADED=PRE+"scripts/full_p47_graded_RR_source.py"
RR_REQUEST=PRE+"notes/full-p47-graded-RR-source-request.json"
HODGE_REQUEST=PRE+"notes/full-p47-CM-height-move-request.json"
P,Q,D,G,PREC=47,4513,167,73,836
N_DECIMAL="742266853925625458713243508737444915533428277366669119033521300217492895040102736787342457363136225645180735565013054428967661465865407320382176274743268354544602364030107341159933929139057712438508843574566526942566329769865133045386011286572648321672762475375516291"
N_JSON_SHA256="cd5db67aa8fa60ef764bb773a9a694878698cba5663f6bfe2cfd2f2b3d863e41"
IDS=[0,76,77,100,108,141,196,220]
START=time.monotonic()
DEADLINE=None
STAGE="preflight"
SOURCE=None
REQUEST_HASH=None
COMPLETED=[]
CTX=None

def canonical(value):
    return json.dumps(value,sort_keys=True,separators=(",",":")).encode()

def digest(value):
    return hashlib.sha256(canonical(value)).hexdigest()

def emit(kind,**data):
    print(json.dumps(dict(kind=kind,miller_seconds=time.monotonic()-START,**data),
                     sort_keys=True),flush=True)

def ci_only():
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get(
            "GITHUB_REPOSITORY")!=REPO:
        raise RuntimeError("Mathematics is restricted to this public repository's Actions.")

def check_budget():
    if DEADLINE is not None and time.monotonic()>=DEADLINE:
        raise TimeoutError("Declared original Miller reserve reached.")

def stop(signum,frame):
    raise TimeoutError("Declared original Miller reserve reached.")

def load_module(name,path):
    spec=importlib.util.spec_from_file_location(name,ROOT/path)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def rows_as_ints(M):
    return [[int(c) for c in row] for row in M.rows()]

def row_hash(M):
    return digest(rows_as_ints(M))

class Point:
    """E of degree167, W=H0(L^2(-E)), div(F)=formal_divisor-(E-D0)."""
    __slots__=("W","gamma","label","stamp")
    def __init__(self,W,gamma,label,stamp):
        self.W=W
        self.gamma=gamma
        self.label=tuple(int(x) for x in label)
        self.stamp=stamp

class Arithmetic:
    def __init__(self,graded,data,req):
        from sage.all import matrix,vector,PolynomialRing,GF
        self.matrix,self.vector,self.GF=matrix,vector,GF
        self.K=graded["source"]["K"]
        self.ring=graded["ring"]
        self.M=graded["matrices"]
        self.polys=graded["polynomials"]
        self.pairs=graded["product_pairs"]
        self.cusp=graded["cusp_values"]
        cusp0=vector(self.K,list(self.cusp[1].row(0)))
        standard_cusp0=vector(self.K,list(self.M[1].column(0)))
        if cusp0!=standard_cusp0:
            raise ArithmeticError("The declared base cusp is not the standard 836-jet cusp.")
        self.fields={}
        self.point_rows=[]
        self.point_ids=[]
        self.point_degrees=[]
        self.point_index={}
        self.initial={}
        self.negative={}
        self.serial=0
        self.counters={"products":0,"colon_calls":0,"add_flips":0,
                       "negations":0,"initial_closed_points":0}
        self.chain=hashlib.sha256()
        self.seed=int(req["deterministic_seed"])
        self.attempts=int(req.get("section_attempts",32))
        if not 1<=self.attempts<=128:
            raise RuntimeError("The finite section prefix must be explicit and bounded.")
        self.center_ids=[int(row["candidate_id"]) for row in data["centers"]]
        if self.center_ids!=IDS:
            raise ArithmeticError("Eight target centers are not in the original fixed order.")
        if data["protocol"]!="full-p47-Miller-support-v1" or data["prime"]!=P or (
                data["coefficient_prime"]!=Q):
            raise ArithmeticError("Wrong finite support protocol.")
        if data["descriptor_sha256"]!=digest(graded["source"]["descriptors"]):
            raise ArithmeticError("Point values belong to a different original Hodge source.")
        expected=req["certified_CM_tangent95_sha256"]
        vals=[]
        ders=[]
        for row in data["centers"]:
            if row["coarse_parameter"]!="j-j_CM":
                raise ArithmeticError("A CM target has a different derivative parameter.")
            v=[int(a)%Q for a in row["ratio_values"]]
            dv=[int(a)%Q for a in row["ratio_dz"]]
            pivot=int(row["denominator_index"])
            if len(v)!=95 or len(dv)!=95:
                raise ArithmeticError("Incomplete original CM section jet.")
            if (row["coarse_tangent95_sha256"]!=expected[str(row["candidate_id"])] or
                not 0<=pivot<95 or v[pivot]!=1 or dv[pivot]!=0):
                raise ArithmeticError("New target ratios disagree with the consumed tangent input.")
            vals.append(v)
            ders.append(dv)
        self.raw_target_values=matrix(self.K,vals).transpose()
        self.raw_target_derivatives=matrix(self.K,ders).transpose()
        for entry in data["fields"]:
            fid=str(entry["id"])
            degree=int(entry["degree"])
            coeff=[int(a)%Q for a in entry["modulus"]]
            if degree==1:
                field=self.K
            else:
                pr=PolynomialRing(self.K,"z")
                modulus=pr(coeff)
                if modulus.degree()!=degree or not modulus.is_monic() or not modulus.is_irreducible():
                    raise ArithmeticError("The actual field-worker modulus is invalid.")
                field=GF(Q**degree,name="z_"+fid,modulus=modulus)
            self.fields[fid]=(field,degree)
        for entry in data["points"]:
            fid=str(entry["field_id"])
            field,ambient_degree=self.fields[fid]
            f=int(entry["degree"])
            if not 1<=f<=159 or ambient_degree%f:
                raise ArithmeticError("Unsupported actual closed support degree.")
            if len(entry["values95"])!=95:
                raise ArithmeticError("Incomplete original projective support values.")
            def decode(coeff):
                if ambient_degree==1:
                    if any(int(a)%Q for a in coeff[1:]):
                        raise ArithmeticError("Nonconstant coordinate in the prime field.")
                    return field(int(coeff[0])%Q if coeff else 0)
                return field(coeff)
            v=[decode(c) for c in entry["values95"]]
            if not any(v) or any(a**(Q**f)!=a for a in v):
                raise ArithmeticError("Projective support values failed finite-field descent.")
            for h in range(1,f):
                if f%h==0 and all(a**(Q**h)==a for a in v):
                    raise ArithmeticError("A claimed closed point has a smaller actual degree.")
            self.add_support(str(entry["id"]),field,ambient_degree,f,v)
        # The cusps remain the original all23 rows; only c_infty_0 is the base.
        for b in range(23):
            v=list(self.cusp[1].row(b))
            self.add_support("cusp_%d"%b,self.K,1,1,v)
        self.base_id="cusp_0"
        self.base_index=self.point_index[self.base_id]
        self.cases=self.build_cases(data,req)
        self.f0=self.choose_base_section()
        # Every target derivative is normalized by the SAME nonzero f0.
        f0_values=self.f0*self.raw_target_values
        f0_derivatives=self.f0*self.raw_target_derivatives
        self.TV={1:matrix(self.K,95,8,lambda i,y:
                         self.raw_target_values[i,y]/f0_values[y])}
        self.TD={1:matrix(self.K,95,8,lambda i,y:
            (self.raw_target_derivatives[i,y]*f0_values[y]
             -self.raw_target_values[i,y]*f0_derivatives[y])/f0_values[y]**2)}
        for n in range(2,6):
            pairs=self.pairs[n]
            self.TV[n]=matrix(self.K,len(pairs),8,lambda i,y:
                self.TV[n-1][pairs[i][0],y]*self.TV[1][pairs[i][1],y])
            self.TD[n]=matrix(self.K,len(pairs),8,lambda i,y:
                self.TD[n-1][pairs[i][0],y]*self.TV[1][pairs[i][1],y]+
                self.TV[n-1][pairs[i][0],y]*self.TD[1][pairs[i][1],y])
        f0t=self.f0*self.TV[1]
        f0d=self.f0*self.TD[1]
        if list(f0t)!=[self.K.one()]*8 or not f0d.is_zero():
            raise ArithmeticError("The original line-frame cancellation failed.")
        self.fixed_pencil=[self.polys[1][0],self.polys[1][1]]
        self.FP={}
        for n in (1,3):
            self.FP[n]=[self.multiply_jets(self.M[n],f) for f in self.fixed_pencil]
        self.support_eval2={}
        for i,(field,ambient_degree,v) in enumerate(self.point_rows):
            values=[v[a]*v[b] for a,b in self.pairs[2]]
            self.support_eval2[i]=values
        self.record("input",{"support_count":len(self.point_ids),
            "support_total_degree":sum(self.point_degrees),
            "f0":list(map(int,self.f0)),"cases":self.cases,
            "target_normalized_values_sha256":row_hash(self.TV[1]),
            "target_normalized_derivatives_sha256":row_hash(self.TD[1])})
        self.input_chain=self.chain.copy()
        self.base_seed=self.seed
        self.input_counters=dict(self.counters)

    def add_support(self,pid,field,ambient_degree,f,values):
        if pid in self.point_index:
            raise ArithmeticError("A support identifier was repeated.")
        index=len(self.point_ids)
        self.point_index[pid]=index
        self.point_ids.append(pid)
        self.point_degrees.append(f)
        self.point_rows.append((field,ambient_degree,values))

    def build_cases(self,data,req):
        # Each image is an actual effective degree24/48 coarse Hecke fiber.
        images=data["angle_images"]
        def image(cm,c):
            key="%d:%d"%(cm,c)
            result={str(pid):int(mult) for pid,mult in images[key]}
            if len(result)!=len(images[key]) or any(m<=0 for m in result.values()):
                raise ArithmeticError("A raw angle fiber has invalid coarse multiplicity.")
            degree=sum(self.point_degrees[self.point_index[pid]]*m
                       for pid,m in result.items())
            if degree!=(24 if c==0 else 48):
                raise ArithmeticError("The complete original angle degree changed.")
            return result
        def linear(terms):
            out={}
            for coefficient,im in terms:
                for pid,m in im.items():
                    out[pid]=out.get(pid,0)+coefficient*m
            return {pid:m for pid,m in out.items() if m}
        cusp={("cusp_%d"%b):1 for b in range(23)}
        allcases={}
        for cm in IDS:
            za=linear([(39,image(141,20)),(12,image(141,5)),
                       (52,image(0,4)),(48,cusp),
                       (-156,image(cm,0)),(-48,image(cm,2))])
            zb=linear([(-21,image(141,20)),(8,image(0,12)),
                       (-28,image(0,4)),(48,cusp),
                       (-24,image(cm,4)),(84,image(cm,0))])
            for name,weights in (("ZA",za),("ZB",zb)):
                if sum(m*self.point_degrees[self.point_index[pid]]
                       for pid,m in weights.items()):
                    raise ArithmeticError("An actual cleared Chow-Heegner divisor has nonzero degree.")
                case_id="%d-%s"%(cm,name)
                allcases[case_id]={"id":case_id,"candidate_id":cm,"angle":name,
                                 "clearing_denominator":6,"weights":weights}
        wanted=req["cases"]
        if len(set(wanted))!=len(wanted) or any(k not in allcases for k in wanted):
            raise RuntimeError("Unexpected finite Miller case list.")
        return [allcases[k] for k in wanted]

    def record(self,kind,obj):
        self.chain.update(canonical([kind,obj])+b"\n")

    def choose_base_section(self):
        # R1104 certifies the actual first two sections form a basepoint-free pencil.
        # Every closed point excludes at most its degree many constants.  Verify
        # every accepted value rather than infer one from a probabilistic choice.
        total=sum(self.point_degrees)+8
        limit=min(Q,total+2)
        for c in range(limit):
            row=self.vector(self.K,[1,c]+[0]*93)
            if any(not (row*self.raw_target_values)[y] for y in range(8)):
                continue
            good=True
            for field,ambient_degree,v in self.point_rows:
                if not (v[0]+field(c)*v[1]):
                    good=False
                    break
            if good:
                return row
        raise ArithmeticError("The declared base-section prefix did not avoid all actual support.")

    def poly(self,row):
        return self.ring(list(row))

    def multiply_jets(self,M,f):
        check_budget()
        self.counters["products"]+=M.nrows()
        rows=[]
        for row in M.rows():
            product=self.poly(row)._mul_trunc_(f,PREC)
            rows.append([product[k] for k in range(PREC)])
        return self.matrix(self.K,rows)

    def colon_coefficients(self,A,B):
        """All rows x with x*A in row(B); B is an injective multiplication image."""
        check_budget()
        self.counters["colon_calls"]+=1
        if B.rank()!=B.nrows():
            raise ArithmeticError("A multiplication denominator lost rank.")
        relations=A.stack(-B).left_kernel().basis_matrix()
        answer=relations.matrix_from_columns(range(A.nrows()))
        if answer.rank()!=relations.nrows():
            raise ArithmeticError("A colon projection has a spurious kernel.")
        return answer.row_space().basis_matrix()

    def candidate(self,basis,degree,tag,avoid_base=False):
        """Finite reproducible section prefix; every chosen section is checked."""
        rng=random.Random(digest([self.seed,self.serial,tag]))
        self.serial+=1
        for k in range(self.attempts):
            if k<min(4,basis.nrows()):
                row=basis.row(k)
            else:
                coeff=self.vector(self.K,[rng.randrange(Q) for _ in range(basis.nrows())])
                row=coeff*basis
            values=row*self.TV[degree]
            if any(not a for a in values):
                continue
            if avoid_base and not (row*self.cusp[degree].row(0)):
                continue
            yield row
        # Caller reports failure if no certified choice in this exact finite prefix.

    def raw_candidate(self,basis,tag):
        rng=random.Random(digest([self.seed,self.serial,tag]))
        self.serial+=1
        for k in range(self.attempts):
            if k<min(4,basis.nrows()):
                yield basis.row(k)
            else:
                yield self.vector(self.K,[rng.randrange(Q)
                    for _ in range(basis.nrows())])*basis

    def dlog(self,coeff,degree):
        value=coeff*self.TV[degree]
        deriv=coeff*self.TD[degree]
        if any(not a for a in value):
            raise ArithmeticError("A Miller factor is not a unit at an actual target.")
        return self.vector(self.K,[deriv[i]/value[i] for i in range(8)])

    def flipped_space(self,U,s,degree,tag):
        """div(s)=fixed+E, U=H0(L^degree(-fixed)), degE=167."""
        sjets=s*self.M[degree]
        spoly=self.poly(sjets)
        denominator=self.multiply_jets(self.M[2],spoly)
        for u in self.raw_candidate(U,tag):
            numerator=self.multiply_jets(self.M[2],self.poly(u*self.M[degree]))
            W=self.colon_coefficients(numerator,denominator)
            if W.nrows()<95:
                raise ArithmeticError("A residual-gcd colon fell below its RR dimension.")
            if W.nrows()==95:
                return W
        raise ArithmeticError("No residual-gcd-free section in the declared finite prefix.")

    def make_point(self,W,gamma,label,kind,extra):
        if W.nrows()!=95 or W.ncols()!=262 or W.rank()!=95:
            raise ArithmeticError("An actual degree167 divisor has the wrong ideal dimension.")
        stamp=digest([kind,row_hash(W),list(map(int,gamma)),list(label),extra])
        self.record(kind,{"stamp":stamp,"extra":extra})
        return Point(W,gamma,label,stamp)

    def product_space(self,first,second):
        left=first.W*self.M[2]
        right=second.W*self.M[2]
        lp=[self.poly(row) for row in left.rows()]
        rp=[self.poly(row) for row in right.rows()]
        selected=[]
        batch=[]
        considered=0
        for j,g in enumerate(rp):
            for i,f in enumerate(lp):
                if first.stamp==second.stamp and i<j:
                    continue
                product=f._mul_trunc_(g,PREC)
                batch.append([product[k] for k in range(PREC)])
                considered+=1
                if len(batch)==95:
                    M=self.matrix(self.K,selected+batch)
                    pivot=list(M.transpose().pivots())
                    selected=[list(M.row(k)) for k in pivot]
                    batch=[]
                    if len(selected)>262:
                        raise ArithmeticError("A true product space exceeded its RR bound.")
                    if len(selected)==262:
                        break
            if len(selected)==262:
                break
            if batch:
                M=self.matrix(self.K,selected+batch)
                selected=[list(M.row(k)) for k in M.transpose().pivots()]
                batch=[]
                if len(selected)>262:
                    raise ArithmeticError("A true product space exceeded its RR bound.")
                if len(selected)==262:
                    break
            check_budget()
        self.counters["products"]+=considered
        if len(selected)!=262:
            raise ArithmeticError("The complete bounded product prefix did not fill the required space.")
        return self.matrix(self.K,selected),considered

    def addflip(self,first,second):
        check_budget()
        Z,considered=self.product_space(first,second)
        U0=self.colon_coefficients(self.FP[3][0],Z)
        U1=self.colon_coefficients(U0*self.FP[3][1],Z)
        U=(U1*U0).row_space().basis_matrix()
        if U.nrows()!=95:
            raise ArithmeticError("The actual degree167 AddFlip pencil has the wrong RR dimension.")
        for s in self.candidate(U,3,"addflip-section"):
            W=self.flipped_space(U,s,3,"addflip-residual")
            gamma=-first.gamma-second.gamma-self.dlog(s,3)
            label=tuple(-a-b for a,b in zip(first.label,second.label))
            self.counters["add_flips"]+=1
            return self.make_point(W,gamma,label,"addflip",
                                  [first.stamp,second.stamp,considered])
        raise ArithmeticError("No AddFlip section avoided all eight targets.")

    def negate(self,point):
        if point.stamp in self.negative:
            return self.negative[point.stamp]
        for s in self.candidate(point.W,2,"negative-section"):
            W=self.flipped_space(point.W,s,2,"negative-residual")
            out=self.make_point(W,-point.gamma-self.dlog(s,2),
                tuple(-a for a in point.label),"negate",[point.stamp])
            self.counters["negations"]+=1
            self.negative[point.stamp]=out
            self.negative[out.stamp]=point
            return out
        raise ArithmeticError("No negative section avoided all eight targets.")

    def initial_closed_point(self,index):
        if index in self.initial:
            return self.initial[index]
        if index==self.base_index:
            raise ArithmeticError("The reference cusp does not need an initial Miller point.")
        field,ambient_degree,values=self.point_rows[index]
        f=self.point_degrees[index]
        evaluations=self.support_eval2[index]
        if ambient_degree==1:
            constraints=self.matrix(self.K,1,262,
                                   lambda i,j:self.K(evaluations[j]))
        else:
            constraints=self.matrix(self.K,ambient_degree,262,
                lambda i,j:self.K(evaluations[j].polynomial()[i]))
        if constraints.rank()!=f:
            raise ArithmeticError("The complete closed-point evaluation lost its actual degree.")
        WP=constraints.right_kernel().basis_matrix()
        if WP.nrows()!=262-f:
            raise ArithmeticError("The initial closed-point vanishing space is incomplete.")
        for h in self.candidate(WP,2,"initial-h-%d"%index,avoid_base=True):
            hpoly=self.poly(h*self.M[2])
            denominator=self.multiply_jets(self.M[3],hpoly)
            U0=None
            for g in self.raw_candidate(WP,"initial-g-%d"%index):
                numerator=self.multiply_jets(self.M[3],self.poly(g*self.M[2]))
                trial=self.colon_coefficients(numerator,denominator)
                if trial.nrows()<95+f:
                    raise ArithmeticError("The initial gcd colon fell below its RR dimension.")
                if trial.nrows()==95+f:
                    U0=trial
                    break
            if U0 is None:
                continue
            at_base=(U0*self.M[3]).matrix_from_columns(range(f))
            vanishing=at_base.left_kernel().basis_matrix()
            U=(vanishing*U0).row_space().basis_matrix()
            if U.nrows()!=95:
                raise ArithmeticError("The exact f-fold base-cusp correction has wrong dimension.")
            for s in self.candidate(U,3,"initial-s-%d"%index):
                W=self.flipped_space(U,s,3,"initial-residual-%d"%index)
                gamma=self.dlog(h,2)-self.dlog(s,3)
                label=[0]*len(self.point_ids)
                label[index]=1
                out=self.make_point(W,gamma,label,"initial",
                    {"point_id":self.point_ids[index],"degree":f,
                     "function":"h*f0/s","base_cusp":self.base_id})
                self.initial[index]=out
                self.counters["initial_closed_points"]+=1
                emit("initial_closed_point",point_id=self.point_ids[index],degree=f,
                     point_sha256=out.stamp)
                return out
        raise ArithmeticError("The declared initial-section prefixes did not complete this closed point.")

    def positive_sum(self,points):
        if not points:
            raise ArithmeticError("The zero sum needs no effective representative.")
        current=points[0]
        sign=1
        for point in points[1:]:
            aligned=point if sign==1 else self.negate(point)
            current=self.addflip(current,aligned)
            sign=-sign
        return current if sign==1 else self.negate(current)

    def scalar_signed(self,point,n,progress=False):
        n=int(n)
        if n<=0:
            raise ValueError("The signed binary core accepts a positive scalar.")
        current=point
        negative=self.negate(point)
        sign=1
        bits=bin(n)[3:]
        for position,bit in enumerate(bits,1):
            current=self.addflip(current,current)
            sign=-sign
            if bit=="1":
                current=self.addflip(current,point if sign==1 else negative)
                sign=-sign
            if progress and (position%16==0 or position==len(bits)):
                emit("Miller_bit_progress",bit=position,total_bits=len(bits),
                     prefix_sign=sign,point_sha256=current.stamp,
                     counters=self.counters)
        expected=tuple(sign*n*a for a in point.label)
        if current.label!=expected:
            raise ArithmeticError("The signed addition chain lost its exact divisor multiplier.")
        return current,sign

    def case_initial(self,case):
        weights=case["weights"]
        expected=[0]*len(self.point_ids)
        for pid,m in weights.items():
            if pid!=self.base_id:
                expected[self.point_index[pid]]=m
        if weights.get(self.base_id,0)!=-sum(
                expected[i]*self.point_degrees[i] for i in range(len(expected))
                if i!=self.base_index):
            raise ArithmeticError("The reference-cusp subtraction changed the actual divisor.")
        groups={}
        for i,m in enumerate(expected):
            if m:
                groups.setdefault(m,[]).append(self.initial_closed_point(i))
        terms=[]
        for m,points in sorted(groups.items()):
            group=self.positive_sum(points)
            multiple,sign=self.scalar_signed(group,abs(m))
            if sign*(1 if m>0 else -1)==-1:
                multiple=self.negate(multiple)
            terms.append(multiple)
        result=self.positive_sum(terms)
        if result.label!=tuple(expected):
            raise ArithmeticError("Initial class combination changed the original cleared divisor.")
        return result

    def terminal_function(self,point):
        W=point.W*self.M[2]
        U0=self.colon_coefficients(self.FP[1][0],W)
        U1=self.colon_coefficients(U0*self.FP[1][1],W)
        U=(U1*U0).row_space().basis_matrix()
        if U.nrows()!=1:
            raise ArithmeticError("The N-torsion endpoint is not the exact trivial class.")
        h=U.row(0)
        # div(h/f0)=E-D0, with PLUS sign in the terminal product.
        return self.dlog(h,1),row_hash(U)

    def run_case(self,case,N):
        self.initial={}
        self.negative={}
        self.serial=0
        self.seed=int(digest([self.base_seed,case["id"]]),16)
        self.chain=self.input_chain.copy()
        self.record("case",case)
        self.counters=dict(self.input_counters)
        initial=self.case_initial(case)
        current,sign=self.scalar_signed(initial,N,progress=True)
        correction,terminal_hash=self.terminal_function(current)
        actual=current.gamma+correction
        alpha=actual/(self.K(sign)*self.K(N%Q)*self.K(6))
        target=self.center_ids.index(case["candidate_id"])
        result={"id":case["id"],"candidate_id":case["candidate_id"],
            "angle":case["angle"],"coarse_parameter":"j-j_CM",
            "alpha":int(alpha[target]),
            "all_eight_log_derivatives":[int(a) for a in alpha],
            "clearing_denominator":6,"order_mod_q":int(N%Q),
            "terminal_sign":sign,"initial_point_sha256":initial.stamp,
            "terminal_point_sha256":current.stamp,
            "terminal_function_space_sha256":terminal_hash,
            "exact_initial_divisor_sha256":digest(case["weights"]),
            "operation_chain_sha256":self.chain.hexdigest(),
            "counters":dict(self.counters)}
        emit("actual_third_kind_value",**result)
        return result

def process_case(case):
    check_budget()
    N=int(N_DECIMAL)
    return CTX.run_case(case,N)

def main():
    global SOURCE,REQUEST_HASH,DEADLINE,STAGE,CTX
    ci_only()
    raw=REQUEST.read_bytes()
    REQUEST_HASH=hashlib.sha256(raw).hexdigest()
    if REQUEST_HASH!=os.environ.get("SERRE_EXPECTED_REQUEST_SHA256"):
        raise RuntimeError("Request pin mismatch.")
    req=json.loads(raw)
    if req["execution_id"]!="full-p47-finite-third-kind-v1" or (
            req["prime"]!=P or req["coefficient_prime"]!=Q or
            req["sage_version"]!="10.6" or req["jet_length"]!=PREC or
            req["maximum_workers"] not in (1,2,3,4)):
        raise RuntimeError("Unexpected bounded original Miller request.")
    if digest(N_DECIMAL)!=N_JSON_SHA256 or req["J_Fq_order_decimal"]!=N_DECIMAL or (
            req["J_Fq_order_json_sha256"]!=N_JSON_SHA256):
        raise RuntimeError("The consumed original group order changed.")
    for path,wanted in req["source_sha256"].items():
        if hashlib.sha256((ROOT/path).read_bytes()).hexdigest()!=wanted:
            raise RuntimeError("Pinned source changed: "+path)
    required={GRADED,RR_REQUEST,HODGE_REQUEST,WORKER,
              PRE+"scripts/full_p47_finite_third_kind.py",
              PRE+"notes/2026-11-27-full-p47-finite-third-kind-method.md",
              PRE+"scripts/full_p47_eight_CM_tangents.py",
              PRE+"scripts/original_p47_ell4513_cuspidal_transfer.py",
              PRE+"scripts/original_p47_cuspidal_disks.py",
              PRE+"scripts/full_p47_weight_one_Hodge_certificate.py",
              PRE+"notes/original-p47-ell4513-cuspidal-transfer-request.json",
              "README.md",PRE+"README.md"}
    if not required.issubset(req["source_sha256"]):
        raise RuntimeError("A required original input lacks a source pin.")
    total=int(req["total_seconds"])
    reserve=int(req["reserve_seconds"])
    if not 120<=total<=18000 or not 30<=reserve<total:
        raise RuntimeError("Unrecognized finite arithmetic budget.")
    DEADLINE=START+total-reserve
    signal.signal(signal.SIGALRM,stop)
    signal.setitimer(signal.ITIMER_REAL,max(0.1,DEADLINE-time.monotonic()))
    hodge=load_module("miller_source_head",PRE+"scripts/full_p47_weight_one_Hodge_certificate.py")
    SOURCE=hodge.source_head()
    scratch=Path(os.environ.get("RUNNER_TEMP","/tmp"))/(
        "original-p47-Miller-"+os.environ.get("GITHUB_RUN_ID","unknown"))
    scratch.mkdir(parents=True,exist_ok=True)
    field_path=scratch/"actual-support.json"
    STAGE="actual_support_fresh_process"
    # No Sage import has occurred in this process yet; the worker likewise
    # imports no Sage, and only its pinned integer JSON crosses this boundary.
    command=[sys.executable,str(ROOT/WORKER),"--request",str(REQUEST),
             "--output",str(field_path),"--seconds",
             str(min(int(req["field_worker_seconds"]),
                     max(1,int(DEADLINE-time.monotonic()))))]
    completed=subprocess.run(command,check=False,timeout=max(1,DEADLINE-time.monotonic()))
    if completed.returncode:
        raise RuntimeError("The isolated actual support worker did not complete.")
    data=json.loads(field_path.read_text())
    emit("actual_support_input",input_sha256=digest(data),
         source=SOURCE,request_sha256=REQUEST_HASH,
         raw_point_count=len(data["points"]),fields=len(data["fields"]),
         field_receipts=data["family_receipts"],target_jet_receipt=data["target_jet_receipt"])
    STAGE="consume_certified_original_graded_ring"
    from sage.all import proof
    from sage.env import SAGE_VERSION
    if SAGE_VERSION!="10.6":
        raise RuntimeError("Wrong pinned Sage release.")
    proof.all(True)
    rr=load_module("miller_graded_source",GRADED)
    rr.DEADLINE=DEADLINE
    graded=rr.build_graded_source(json.loads((ROOT/RR_REQUEST).read_text()),
                                 expected_certificate=req["graded_certificate"])
    CTX=Arithmetic(graded,data,req)
    if int(N_DECIMAL)%Q!=551:
        raise ArithmeticError("The consumed order is not the certified q-unit.")
    emit("bounded_Miller_inputs_ready",support_points=len(CTX.point_ids),
         cases=[c["id"] for c in CTX.cases],workers=req["maximum_workers"],
         graded_certificate_sha256=digest(graded["certificate"]),
         exact_N_json_sha256=N_JSON_SHA256)
    STAGE="new_original_finite_Miller"
    # Fork only the Sage parent, after the flint child has exited.  The graded
    # matrices are shared read-only by copy-on-write; each case owns its chain.
    if req["maximum_workers"]==1:
        for case in CTX.cases:
            COMPLETED.append(process_case(case))
    else:
        context=multiprocessing.get_context("fork")
        with context.Pool(processes=int(req["maximum_workers"])) as pool:
            for result in pool.imap_unordered(process_case,CTX.cases,chunksize=1):
                COMPLETED.append(result)
                emit("completed_case",id=result["id"],alpha=result["alpha"],
                     completed=len(COMPLETED),total=len(CTX.cases))
    if {r["id"] for r in COMPLETED}!={c["id"] for c in CTX.cases}:
        raise ArithmeticError("The declared finite case set is incomplete.")
    signal.setitimer(signal.ITIMER_REAL,0)
    STAGE="completed"
    ordered=sorted(COMPLETED,key=lambda r:r["id"])
    emit("receipt",status="complete",source=SOURCE,run=os.environ.get("GITHUB_RUN_ID"),
         request_sha256=REQUEST_HASH,completed=ordered,result_sha256=digest(ordered),
         scope="Actual finite-field normalized third-kind values only; no uncomputed QC rank or rational-point exclusion.")
    # Large matrices, functions and temporary field data are runner-only.
    field_path.unlink(missing_ok=True)

if __name__=="__main__":
    try:
        main()
    except BaseException as exc:
        signal.setitimer(signal.ITIMER_REAL,0)
        emit("receipt",status="incomplete",source=SOURCE,
             run=os.environ.get("GITHUB_RUN_ID"),request_sha256=REQUEST_HASH,
             stage=STAGE,exception_type=type(exc).__name__,message=str(exc),
             completed=COMPLETED,
             scope="Only individually completed original Miller values are retained.")
        traceback.print_exc()
        sys.exit(1)
