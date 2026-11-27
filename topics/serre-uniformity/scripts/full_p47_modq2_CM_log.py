#!/usr/bin/env python3
"""First original CM Abel logarithms over Z/4513^2 by R1108.

Actual lifted Reynolds sections, bounded degree167 KM divisors and a fixed
finite etale residue algebra. No local execution, stored raw matrices or
substitute abstract Jacobian model. All arithmetic runs in public Actions.
"""
import hashlib
import importlib.util
import json
import multiprocessing
import os
from pathlib import Path
import random
import signal
import sys
import time
import traceback

ROOT = Path(__file__).resolve().parents[3]
PRE = "topics/serre-uniformity/"
REQUEST = ROOT/(PRE+"notes/full-p47-modq2-CM-log-request.json")
Q = 4513
MOD = Q*Q
PREC = 836
IDS = (0,141,76,108)
START = time.monotonic()
DEADLINE = None
STAGE = "preflight"
SOURCE = None
REQUEST_HASH = None
COMPLETED = {}
ACTIVE = None


def canonical(value):
    return json.dumps(value,sort_keys=True,separators=(",",":")).encode()


def digest(value):
    return hashlib.sha256(canonical(value)).hexdigest()


def rows(M):
    return [[int(x) for x in row] for row in M.rows()]


def row_hash(M):
    return digest(rows(M))


def emit(kind,**data):
    print(json.dumps(dict(kind=kind,elapsed_seconds=time.monotonic()-START,**data),
                     sort_keys=True),flush=True)


def check_budget():
    if DEADLINE is not None and time.monotonic()>=DEADLINE:
        raise TimeoutError("The declared mathematical reserve was reached.")


def stop(signum,frame):
    raise TimeoutError("The declared mathematical reserve was reached.")


def ci_only():
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get(
            "GITHUB_REPOSITORY")!="Rogerhu12/math-research-public":
        raise RuntimeError("Mathematics is restricted to this public repository's Actions.")


def module(path,name):
    spec=importlib.util.spec_from_file_location(name,ROOT/path)
    obj=importlib.util.module_from_spec(spec)
    sys.modules[name]=obj
    spec.loader.exec_module(obj)
    return obj


def source_head():
    gd=ROOT/".git"
    value=(gd/"HEAD").read_text().strip()
    if value.startswith("ref: "):
        ref=value[5:]
        if not ref.startswith("refs/") or ".." in ref.split("/"):
            raise RuntimeError("Unexpected checkout ref.")
        if (gd/ref).exists():
            value=(gd/ref).read_text().strip()
        else:
            matches=[line.split(" ",1)[0] for line in (gd/"packed-refs").read_text().splitlines()
                     if line.endswith(" "+ref)]
            if len(matches)!=1:
                raise RuntimeError("Ambiguous actual checkout.")
            value=matches[0]
    if len(value)!=40 or value!=os.environ.get("GITHUB_SHA"):
        raise RuntimeError("The actual checkout differs from GITHUB_SHA.")
    return value


class UnitLinear:
    """Free images and kernels over R, with complete q^2 relation checks."""

    def __init__(self,R,K):
        from sage.all import identity_matrix,matrix,vector
        self.R,self.K=R,K
        self.matrix,self.vector,self.identity=matrix,vector,identity_matrix
        self.inverse_calls=0
        self.kernel_calls=0

    def reduction(self,M):
        return M.change_ring(self.K)

    def inverse(self,A):
        check_budget()
        if A.nrows()!=A.ncols():
            raise ValueError("A unit inverse requires a square matrix.")
        self.inverse_calls+=1
        B0=self.reduction(A).inverse().change_ring(self.R)
        I=self.identity(self.R,A.nrows())
        B=B0*(2*I-A*B0)
        if A*B!=I or B*A!=I:
            raise ArithmeticError("The q^2 Newton matrix inverse failed.")
        return B

    def independent_rows(self,M):
        return list(self.reduction(M).transpose().pivots())

    def image(self,M,expected=None):
        """Return actual row basis; detect every extra q-torsion relation."""
        check_budget()
        inds=self.independent_rows(M)
        if expected is not None and len(inds)!=int(expected):
            raise ArithmeticError("A free image has an unexpected special-fiber rank.")
        if not inds:
            if not M.is_zero():
                raise ArithmeticError("A putative zero image has nonzero q-torsion.")
            return self.matrix(self.R,0,M.ncols())
        B=M.matrix_from_rows(inds)
        piv=list(self.reduction(B).pivots())
        E=self.inverse(B.matrix_from_columns(piv))*B
        if M!=M.matrix_from_columns(piv)*E:
            raise ArithmeticError("The full q^2 row image is not free at its chosen unit minor.")
        return E

    def kernel(self,M,expected=None,allow_larger=False):
        """Left kernel of a true constant-rank map, verified over all columns.

        When a candidate residual divisor has extra gcd on the special fiber,
        return None BEFORE asserting flatness or lifting that false dimension.
        """
        check_budget()
        self.kernel_calls+=1
        inds=self.independent_rows(M)
        rank=len(inds)
        dim=M.nrows()-rank
        if expected is not None and dim!=int(expected):
            if allow_larger and dim>int(expected):
                return None
            raise ArithmeticError("A relative RR kernel has the wrong special-fiber dimension.")
        if rank==0:
            if not M.is_zero():
                raise ArithmeticError("A zero special-fiber map has nonzero q-torsion.")
            return self.identity(self.R,M.nrows())
        B=M.matrix_from_rows(inds)
        piv=list(self.reduction(B).pivots())
        free=[j for j in range(M.nrows()) if j not in set(inds)]
        C=M.matrix_from_rows_and_columns(free,piv)*self.inverse(
            B.matrix_from_columns(piv))
        if M.matrix_from_rows(free)!=C*B:
            raise ArithmeticError("The complete q^2 kernel relation failed; the map is not flat.")
        out=self.matrix(self.R,len(free),M.nrows())
        for a,j in enumerate(free):
            out[a,j]=1
            for b,i in enumerate(inds):
                out[a,i]=-C[a,b]
        if not (out*M).is_zero():
            raise ArithmeticError("The lifted RR kernel did not annihilate its complete map.")
        return out

    def projector(self,B):
        """Quotient by a free injective row image, using unit pivot columns."""
        check_budget()
        B0=self.reduction(B)
        piv=list(B0.pivots())
        if len(piv)!=B.nrows():
            raise ArithmeticError("A multiplication denominator lost injectivity.")
        inv=self.inverse(B.matrix_from_columns(piv))
        free=[j for j in range(B.ncols()) if j not in set(piv)]
        tail=inv*B.matrix_from_columns(free)
        return piv,free,tail

    def residual(self,A,projector):
        piv,free,tail=projector
        return A.matrix_from_columns(free)-A.matrix_from_columns(piv)*tail

    def colon(self,A,B,expected=None,allow_larger=False):
        return self.kernel(self.residual(A,self.projector(B)),expected,allow_larger)

    def simultaneous_colon(self,AA,B,expected):
        projection=self.projector(B)
        parts=[self.residual(A,projection) for A in AA]
        F=parts[0]
        for part in parts[1:]:
            F=F.augment(part)
        return self.kernel(F,expected)

    def prescribed_lift(self,B,bar_target):
        """An element of free row(B) with one exactly prescribed reduction."""
        B0=self.reduction(B)
        target=self.vector(self.K,list(bar_target))
        piv=list(B0.pivots())
        if len(piv)!=B.nrows():
            raise ArithmeticError("The prescribed-lift space is not free.")
        coeff=self.vector(self.K,[target[j] for j in piv])*B0.matrix_from_columns(piv).inverse()
        if coeff*B0!=target:
            raise ArithmeticError("The prescribed special-fiber section is outside the true RR space.")
        value=self.vector(self.R,[int(a) for a in coeff])*B
        if self.vector(self.K,list(value))!=target:
            raise ArithmeticError("The prescribed q^2 section changed its specified reduction.")
        return value


class Point:
    def __init__(self,W,label,stamp):
        self.W,self.label,self.stamp=W,tuple(label),stamp


class LiftedKM:
    """All representations are actual H0(L^2(-E)), deg(E)=167."""

    def __init__(self,old_rr,lifted,req):
        from sage.all import GF,PolynomialRing,Zmod,identity_matrix,matrix,vector
        self.R,self.K=Zmod(MOD),GF(Q)
        self.matrix,self.vector,self.identity=matrix,vector,identity_matrix
        self.lin=UnitLinear(self.R,self.K)
        self.ring=PolynomialRing(self.R,"t")
        self.old=old_rr
        self.req=req
        self.attempts=int(req["section_attempts"])
        self.seed=int(req["seed"])
        self.serial=0
        self.chain=hashlib.sha256()
        self.counters={"products":0,"add_flips":0,"negations":0,"initial_divisors":0}
        self.negative={}
        self.M={1:matrix(self.R,lifted["matrices"][1])}
        self.polys={1:[self.poly(row) for row in self.M[1].rows()]}
        self.cusp={1:matrix(self.R,lifted["cusp_values"][1])}
        self.cm={int(k):vector(self.R,v) for k,v in lifted["CM_rows"].items()}
        if self.M[1].dimensions()!=(95,PREC) or self.cusp[1].dimensions()!=(23,95):
            raise ArithmeticError("The original lifted source has wrong dimensions.")
        if any(int(x)%Q for x in (self.cusp[1].row(0)-self.M[1].column(0))):
            raise ArithmeticError("The standard actual cusp differs from the fixed jet constant.")
        if self.cusp[1].row(0)!=self.M[1].column(0):
            raise ArithmeticError("The standard cusp equality failed over q^2.")
        if set(self.cm)!=set(IDS):
            raise ArithmeticError("Exactly the four original basic CM points are required.")
        self.pairs=old_rr["product_pairs"]
        for n in range(2,6):
            check_budget()
            pairs=self.pairs[n]
            polys=[self.polys[n-1][a]._mul_trunc_(self.polys[1][b],PREC) for a,b in pairs]
            self.polys[n]=polys
            self.M[n]=matrix(self.R,[[f[j] for j in range(PREC)] for f in polys])
            self.cusp[n]=matrix(self.R,23,len(pairs),lambda c,j:
                self.cusp[n-1][c,pairs[j][0]]*self.cusp[1][c,pairs[j][1]])
            if self.M[n].change_ring(self.K)!=old_rr["matrices"][n]:
                raise ArithmeticError("A lifted product basis changed the original mod-q source.")
            if self.cusp[n].change_ring(self.K)!=old_rr["cusp_values"][n]:
                raise ArithmeticError("The lifted all23 cusps changed their original mod-q values.")
        self.cm2={cm:vector(self.R,[self.cm[cm][a]*self.cm[cm][b]
                                  for a,b in self.pairs[2]]) for cm in IDS}
        # Coordinate projections have full q^2 relation checks when consumed.
        self.coordinate={}
        for n in range(1,6):
            piv=list(self.M[n].change_ring(self.K).pivots())
            if len(piv)!=self.M[n].nrows():
                raise ArithmeticError("A lifted original graded basis is not free.")
            self.coordinate[n]=(piv,self.lin.inverse(self.M[n].matrix_from_columns(piv)))
        self.fixed_pencil=[self.polys[1][0],self.polys[1][1]]
        self.FP={n:[self.multiply_jets(self.M[n],f) for f in self.fixed_pencil]
                 for n in (1,3)}
        self.f1=vector(self.R,[0,1]+[0]*93)
        self.f1poly=self.polys[1][1]
        self.f0=None
        self.residue=None
        self.choose_etale_base(lifted)
        self.zero=self.make_point(self.coordinates(
            self.multiply_jets(self.M[1],self.poly(self.f0*self.M[1])),2),
            [0]*5,"actual-zero",{"f0":list(map(int,self.f0))})
        self.record("lifted_input",{"source_certificate":lifted["certificate"],
                    "graded_sha256":{str(n):row_hash(self.M[n]) for n in range(1,6)},
                    "all23_lifted_cusps_sha256":row_hash(self.cusp[1]),
                    "f0":list(map(int,self.f0)),
                    "residue_algebra":self.residue.certificate})
        self.input_chain=self.chain.copy()
        self.input_counters=dict(self.counters)

    def record(self,kind,value):
        self.chain.update(canonical([kind,value])+b"\n")

    def poly(self,row):
        return self.ring(list(row))

    def multiply_jets(self,M,f):
        check_budget()
        self.counters["products"]+=M.nrows()
        answer=[]
        for row in M.rows():
            prod=self.poly(row)._mul_trunc_(f,PREC)
            answer.append([prod[k] for k in range(PREC)])
        return self.matrix(self.R,answer)

    def coordinates(self,jets,n):
        piv,inv=self.coordinate[n]
        answer=jets.matrix_from_columns(piv)*inv
        if answer*self.M[n]!=jets:
            raise ArithmeticError("A complete q^2 product escaped the actual graded source.")
        return answer

    def vector_coordinates(self,jet,n):
        return self.coordinates(self.matrix(self.R,[list(jet)]),n).row(0)

    def choose_etale_base(self,lifted):
        old_points=lifted.get("all_CM_rows_modq")
        if old_points is None or set(map(int,old_points))!={0,76,77,100,108,141,196,220}:
            raise ArithmeticError("Keep all eight certified CM reductions when choosing D0.")
        for c in range(int(self.req["base_pencil_limit"])):
            row=self.vector(self.R,[1,c]+[0]*93)
            if any(not int(row*self.cusp[1].row(b))%Q for b in range(23)):
                continue
            if any(not (int(v[0])+c*int(v[1]))%Q for v in old_points.values()):
                continue
            candidate=ResidueAlgebra(self,row)
            if not candidate.etale:
                emit("base_pencil_rejected",pencil_c=c,reason="Wronskian is not a unit.")
                continue
            self.f0=row
            self.residue=candidate
            emit("actual_etale_base_algebra",**candidate.certificate)
            return
        raise ArithmeticError("No reduced avoiding fiber in the declared pencil prefix.")

    def raw_candidate(self,basis,tag):
        rng=random.Random(digest([self.seed,self.serial,tag]))
        self.serial+=1
        for k in range(self.attempts):
            if k<min(4,basis.nrows()):
                yield basis.row(k)
            else:
                yield self.vector(self.R,[rng.randrange(Q) for _ in range(basis.nrows())])*basis

    def candidate(self,basis,degree,tag,avoid_base=False):
        for row in self.raw_candidate(basis,tag):
            if not any(int(a)%Q for a in row):
                continue
            if avoid_base and not int(row*self.cusp[degree].row(0))%Q:
                continue
            yield row

    def flipped_space(self,U,s,degree,tag,forced_u=None):
        spoly=self.poly(s*self.M[degree])
        denominator=self.multiply_jets(self.M[2],spoly)
        projection=self.lin.projector(denominator)
        choices=[forced_u] if forced_u is not None else self.raw_candidate(U,tag)
        for u in choices:
            numerator=self.multiply_jets(self.M[2],self.poly(u*self.M[degree]))
            W=self.lin.kernel(self.lin.residual(numerator,projection),
                              expected=95,allow_larger=forced_u is None)
            if W is not None:
                return W
        raise ArithmeticError("The declared residual-gcd prefix did not produce an exact degree167 divisor.")

    def make_point(self,W,label,kind,extra):
        if W.dimensions()!=(95,262) or len(self.lin.independent_rows(W))!=95:
            raise ArithmeticError("A lifted actual divisor has the wrong free ideal dimension.")
        stamp=digest([kind,row_hash(W),list(label),extra])
        self.record(kind,{"stamp":stamp,"extra":extra})
        return Point(W,label,stamp)

    def product_space(self,first,second):
        lp=[self.poly(row) for row in (first.W*self.M[2]).rows()]
        rp=[self.poly(row) for row in (second.W*self.M[2]).rows()]
        selected=[]
        batch=[]
        considered=0
        for j,g in enumerate(rp):
            for i,f in enumerate(lp):
                if first.stamp==second.stamp and i<j:
                    continue
                prod=f._mul_trunc_(g,PREC)
                batch.append([prod[k] for k in range(PREC)])
                considered+=1
                if len(batch)==95:
                    M=self.matrix(self.R,selected+batch)
                    inds=self.lin.independent_rows(M)
                    selected=[list(M.row(k)) for k in inds]
                    batch=[]
                    if len(selected)>262:
                        raise ArithmeticError("The actual product exceeded its relative RR dimension.")
                    if len(selected)==262:
                        break
            if len(selected)==262:
                break
            if batch:
                M=self.matrix(self.R,selected+batch)
                selected=[list(M.row(k)) for k in self.lin.independent_rows(M)]
                batch=[]
                if len(selected)>262:
                    raise ArithmeticError("The actual product exceeded its relative RR dimension.")
                if len(selected)==262:
                    break
            check_budget()
        self.counters["products"]+=considered
        if len(selected)!=262:
            raise ArithmeticError("The bounded product prefix did not fill its actual RR space.")
        return self.matrix(self.R,selected),considered

    def addflip_space(self,first,second):
        Z,considered=self.product_space(first,second)
        # One simultaneous kernel is essential: a one-pencil intermediate
        # can jump in dimension even though the final relative RR space is free.
        U=self.lin.simultaneous_colon(self.FP[3],Z,95)
        return U,considered

    def addflip(self,first,second):
        check_budget()
        U,considered=self.addflip_space(first,second)
        for s in self.candidate(U,3,"addflip-s"):
            W=self.flipped_space(U,s,3,"addflip-u")
            label=tuple(-a-b for a,b in zip(first.label,second.label))
            self.counters["add_flips"]+=1
            return self.make_point(W,label,"addflip",
                                  [first.stamp,second.stamp,considered])
        raise ArithmeticError("No nonzero AddFlip section in the declared prefix.")

    def negate(self,point):
        if point.stamp in self.negative:
            return self.negative[point.stamp]
        for s in self.candidate(point.W,2,"negative-s"):
            W=self.flipped_space(point.W,s,2,"negative-u")
            out=self.make_point(W,[-a for a in point.label],"negate",[point.stamp])
            self.negative[point.stamp]=out
            self.negative[out.stamp]=point
            self.counters["negations"]+=1
            return out
        raise ArithmeticError("No nonzero negative section in the declared prefix.")

    def initial_effective_divisor(self,constraints,degree,label,name):
        """P disjoint from base cusp b; represent P-degree*b exactly."""
        f=int(degree)
        WP=self.lin.kernel(constraints.transpose(),262-f)
        for h in self.candidate(WP,2,"initial-h-"+name,avoid_base=True):
            denominator=self.multiply_jets(self.M[3],self.poly(h*self.M[2]))
            projection=self.lin.projector(denominator)
            U0=None
            for g in self.raw_candidate(WP,"initial-g-"+name):
                numerator=self.multiply_jets(self.M[3],self.poly(g*self.M[2]))
                U0=self.lin.kernel(self.lin.residual(numerator,projection),
                                   95+f,allow_larger=True)
                if U0 is not None:
                    break
            if U0 is None:
                continue
            at_base=(U0*self.M[3]).matrix_from_columns(range(f))
            U=self.lin.kernel(at_base,95)*U0
            for s in self.candidate(U,3,"initial-s-"+name):
                W=self.flipped_space(U,s,3,"initial-u-"+name)
                out=self.make_point(W,label,"initial",
                    {"name":name,"degree":f,"base_cusp":0,"function":"h*f0/s"})
                self.counters["initial_divisors"]+=1
                emit("initial_actual_divisor",name=name,degree=f,point_sha256=out.stamp)
                return out
        raise ArithmeticError("Initial divisor prefixes were exhausted: "+name)

    def scalar_signed(self,point,n,progress=False):
        n=int(n)
        if n<1:
            raise ValueError("The signed chain needs a positive integer.")
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
                emit("CM_log_bit_progress",candidate_id=self.current_cm,bit=position,
                     total_bits=len(bits),prefix_sign=sign,point_sha256=current.stamp,
                     counters=self.counters)
        if current.label!=tuple(sign*n*a for a in point.label):
            raise ArithmeticError("The signed chain changed its actual divisor multiplier.")
        return current,sign

    def prepare_initials(self):
        # P=C_infty-b has degree22 and is disjoint from b. Its one initial
        # class is exactly C_infty-23b, preserving every original cusp.
        cpoint=self.initial_effective_divisor(
            self.cusp[2].matrix_from_rows(range(1,23)),22,[0,0,0,0,1],"all22-nonbase-cusps")
        result={}
        for index,cm in enumerate(IDS):
            label=[0]*5
            label[index]=1
            ypoint=self.initial_effective_divisor(
                self.matrix(self.R,[list(self.cm2[cm])]),1,label,"CM-%d"%cm)
            multi,sign=self.scalar_signed(ypoint,23)
            if sign==-1:
                multi=self.negate(multi)
            result[cm]=self.negate(self.addflip(multi,self.negate(cpoint)))
            expected=[0]*5
            expected[index]=23
            expected[4]=-1
            if result[cm].label!=tuple(expected):
                raise ArithmeticError("The actual u_y=23y-C_infty initialization lost its scale.")
            emit("actual_CM_class_initialized",candidate_id=cm,
                 exact_divisor="23*y-C_infty",point_sha256=result[cm].stamp)
        return result

    def endpoint_h_modq(self,point):
        """Only reduce here: E_N is linearly equivalent to D0, not equal."""
        K=self.K
        L=UnitLinear(K,K)
        W=(point.W*self.M[2]).change_ring(K)
        AA=[A.change_ring(K) for A in self.FP[1]]
        U=L.simultaneous_colon(AA,W,1)
        return U.row(0)

    def normalized_endpoint(self,point,N,epsilon):
        hbar=self.endpoint_h_modq(point)
        U,considered=self.addflip_space(point,self.zero)
        barM={n:self.M[n].change_ring(self.K) for n in (1,2,3)}
        from sage.all import PolynomialRing
        pr=PolynomialRing(self.K,"t")
        h=pr(list(hbar*barM[1]))
        f0=pr(list(self.vector(self.K,list(self.f0))*barM[1]))
        f1=pr(list(self.vector(self.K,list(self.f1))*barM[1]))
        sj=h._mul_trunc_(f0,PREC)._mul_trunc_(f0,PREC)
        uj=h._mul_trunc_(f0,PREC)._mul_trunc_(f1,PREC)
        piv,_=self.coordinate[3]
        inverse=barM[3].matrix_from_columns(piv).inverse()
        sb=self.vector(self.K,[sj[j] for j in piv])*inverse
        ub=self.vector(self.K,[uj[j] for j in piv])*inverse
        if sb*barM[3]!=self.vector(self.K,[sj[j] for j in range(PREC)]) or (
                ub*barM[3]!=self.vector(self.K,[uj[j] for j in range(PREC)])):
            raise ArithmeticError("The prescribed terminal h*f0^2/h*f0*f1 is not in actual V3.")
        s=self.lin.prescribed_lift(U,sb)
        u=self.lin.prescribed_lift(U,ub)
        W=self.flipped_space(U,s,3,"forced-terminal",forced_u=u)
        endpoint=self.make_point(W,[-a for a in point.label],"forced-terminal",
                                 {"old":point.stamp,"product_count":considered})
        zero0=self.zero.W.change_ring(self.K).row_space()
        if W.change_ring(self.K).row_space()!=zero0:
            raise ArithmeticError("The normalized terminal divisor does not reduce to the actual D0.")
        f0f1=self.poly(self.f0*self.M[1])._mul_trunc_(self.f1poly,PREC)
        ref=self.vector_coordinates([f0f1[j] for j in range(PREC)],2)
        hnew=self.lin.prescribed_lift(W,self.vector(self.K,list(ref)))
        difference=hnew-ref
        if any(int(x)%Q for x in difference):
            raise ArithmeticError("The terminal section differs before the first infinitesimal layer.")
        dh=self.vector(self.K,[int(x)//Q for x in difference])
        value=self.residue.read_log(dh,epsilon,N)
        terminal={"hbar_sha256":digest(list(map(int,hbar))),
                  "forced_s_sha256":digest(list(map(int,s))),
                  "forced_u_sha256":digest(list(map(int,u))),
                  "normalized_endpoint_sha256":endpoint.stamp,
                  "delta_section_sha256":digest(list(map(int,dh))),
                  "terminal_reduction_is_actual_D0":True,
                  "formula":"lambda_D=Tr_A(delta*r)/(epsilon*N)",
                  "signed_multiplier":epsilon}
        return value,terminal

    def run_case(self,cm,point,N):
        self.current_cm=cm
        self.seed=int(digest([int(self.req["seed"]),cm]),16)
        self.serial=0
        self.negative={}
        self.chain=self.input_chain.copy()
        self.counters=dict(self.input_counters)
        self.record("case",{"cm":cm,"initial":point.stamp,"N_sha256":digest(str(N))})
        final,epsilon=self.scalar_signed(point,N,progress=True)
        value,terminal=self.normalized_endpoint(final,N,epsilon)
        output={"candidate_id":cm,"exact_divisor":"23*y-C_infty",
                "coefficient_prime":Q,"modulus":MOD,"lambda73":list(map(int,value)),
                "lambda73_sha256":digest(list(map(int,value))),
                "N_sha256":digest(str(N)),"N_mod_q":int(N%Q),
                "terminal":terminal,"residue_algebra":self.residue.certificate,
                "chain_sha256":self.chain.hexdigest(),"counters":self.counters,
                "unit_inverse_calls":self.lin.inverse_calls,
                "lifted_kernel_calls":self.lin.kernel_calls}
        emit("actual_CM_first_log",**output)
        return output


class ResidueAlgebra:
    """The complete A=H0(O_D0), using the original graded source over F_q."""

    def __init__(self,km,f0):
        from sage.all import PolynomialRing,identity_matrix,matrix,vector
        self.km,self.K=km,km.K
        K=self.K
        self.lin=UnitLinear(K,K)
        self.matrix,self.vector=matrix,vector
        self.ring=PolynomialRing(K,"t")
        self.M={n:km.old["matrices"][n] for n in (1,2,3,4)}
        self.coordinate={}
        for n in self.M:
            piv=list(self.M[n].pivots())
            self.coordinate[n]=(piv,self.M[n].matrix_from_columns(piv).inverse())
        f0v=vector(K,list(f0))
        f1v=vector(K,list(km.f1))
        p0=self.ring(list(f0v*self.M[1]))
        p1=self.ring(list(f1v*self.M[1]))
        self.p0,self.p1=p0,p1
        B2=self.coordinates(self.mul(self.M[1],p0),2)
        B3=self.coordinates(self.mul(self.M[2],p0),3)
        B4=self.coordinates(self.mul(self.M[3],p0),4)
        self.Q2,self.Q3,self.Q4=[self.lin.projector(B) for B in (B2,B3,B4)]
        self.free2=self.Q2[1]
        if len(self.free2)!=167 or len(self.Q3[1])!=167 or len(self.Q4[1])!=167:
            raise ArithmeticError("The complete degree167 residue algebra has the wrong dimension.")
        self.reps=identity_matrix(K,262).matrix_from_rows(self.free2)
        self.rep_jets=self.reps*self.M[2]
        f1square=p1._mul_trunc_(p1,PREC)
        one2=self.coordinates(matrix(K,[[f1square[j] for j in range(PREC)]]),2)
        self.one=self.lin.residual(one2,self.Q2).row(0)
        bridge3=self.lin.residual(self.coordinates(self.mul(self.rep_jets,p1),3),self.Q3)
        bridge4=self.lin.residual(self.coordinates(self.mul(self.rep_jets,f1square),4),self.Q4)
        if bridge3.rank()!=167 or bridge4.rank()!=167:
            raise ArithmeticError("Multiplication by the disjoint pencil section failed in the residue algebra.")
        self.bridge4_inverse=bridge4.inverse()
        self.bridge3_inverse=bridge3.inverse()
        W=(self.ring.gen()*(p0.derivative()._mul_trunc_(p1,PREC)-
                          p0._mul_trunc_(p1.derivative(),PREC))/K(47)).truncate(PREC)
        Wc=self.coordinates(matrix(K,[[W[j] for j in range(PREC)]]),3)
        w=(self.lin.residual(Wc,self.Q3)*self.bridge3_inverse).row(0)
        Mw=self.multiplication(w)
        normw=Mw.det()
        self.etale=bool(normw)
        self.certificate={"pencil_c":int(f0[1])%Q,"residue_dimension":167,
                          "Wronskian_norm":int(normw),
                          "Wronskian_coordinates_sha256":digest(list(map(int,w))),
                          "Wronskian_formula":"t*(F0_prime*F1-F0*F1_prime)/47",
                          "all_23_cusps_and_eight_CM_avoided":True}
        if not self.etale:
            return
        PR=PolynomialRing(K,"X")
        rng=random.Random(digest([int(km.req["seed"]),"residue-primitive",int(f0[1])]))
        primitive=None
        for attempt in range(int(km.req["primitive_attempts"])):
            if attempt==0:
                a,Ma=w,Mw
            elif attempt<=min(4,167):
                a=vector(K,[1 if j==attempt-1 else 0 for j in range(167)])
                Ma=self.multiplication(a)
            else:
                a=vector(K,[rng.randrange(Q) for _ in range(167)])
                Ma=self.multiplication(a)
            F=PR(Ma.charpoly())
            if F.degree()!=167 or not F.is_monic() or F.gcd(F.derivative()).degree()!=0:
                continue
            powers=[]
            current=self.one
            for i in range(167):
                powers.append(list(current))
                current=current*Ma
            cyclic=matrix(K,powers)
            if not cyclic.det():
                continue
            if current+vector(K,[F[i] for i in range(167)])*cyclic!=vector(K,167):
                raise ArithmeticError("The actual primitive algebra relation failed.")
            primitive=(a,Ma,F,cyclic,attempt)
            break
        if primitive is None:
            raise ArithmeticError("No actual primitive residue element in the declared finite prefix.")
        a,Ma,F,cyclic,attempt=primitive
        self.PR,self.F,self.cyclic_inverse=PR,F,cyclic.inverse()
        wp=PR(list(w*self.cyclic_inverse))
        winv=wp.inverse_mod(F)
        if (wp*winv)%F!=1:
            raise ArithmeticError("The complete etale Wronskian did not have its actual inverse.")
        traces=[K(167)]
        for k in range(1,167):
            traces.append(-K(k)*F[167-k]-sum(
                (F[167-j]*traces[k-j] for j in range(1,k)),K.zero()))
        self.traces=vector(K,traces)
        # Gi/f1 is represented by Gi*f1 in V2. Only the original
        # holomorphic mod-q basis is needed for this first infinitesimal layer.
        G=km.old["source"]["kernel"]*self.M[1]
        Gf1=self.coordinates(self.mul(G,p1),2)
        ratios=self.lin.residual(Gf1,self.Q2)*self.cyclic_inverse
        trace_rows=[]
        rpolys=[]
        for row in ratios.rows():
            r=(PR(list(row))*winv)%F
            rpolys.append([int(r[j]) for j in range(167)])
            tr=[]
            power=r
            for k in range(167):
                tr.append(sum((power[j]*traces[j] for j in range(167)),K.zero()))
                power=(PR.gen()*power)%F
            trace_rows.append(tr)
        self.trace_matrix=matrix(K,trace_rows)
        if self.trace_matrix.dimensions()!=(73,167):
            raise ArithmeticError("The whole original Hodge trace pairing was not retained.")
        self.certificate.update({
            "finite_etale":True,"primitive_attempt":attempt,
            "primitive_coordinates_sha256":digest(list(map(int,a))),
            "primitive_polynomial_sha256":digest([int(F[j]) for j in range(168)]),
            "primitive_cyclic_matrix_sha256":row_hash(cyclic),
            "Newton_traces_sha256":digest(list(map(int,self.traces))),
            "original_73_differentials_over_dz_sha256":digest(rpolys),
            "trace_reading_matrix_sha256":row_hash(self.trace_matrix),
            "Hodge_kernel_sha256":row_hash(km.old["source"]["kernel"]),
            "all_geometric_conjugates_included":True})

    def mul(self,M,poly):
        answer=[]
        for row in M.rows():
            product=self.ring(list(row))._mul_trunc_(poly,PREC)
            answer.append([product[k] for k in range(PREC)])
        return self.matrix(self.K,answer)

    def coordinates(self,jets,n):
        piv,inverse=self.coordinate[n]
        answer=jets.matrix_from_columns(piv)*inverse
        if answer*self.M[n]!=jets:
            raise ArithmeticError("A residue-algebra product escaped the actual graded source.")
        return answer

    def multiplication(self,a):
        actual=self.vector(self.K,list(a))*self.reps
        polynomial=self.ring(list(actual*self.M[2]))
        images=self.coordinates(self.mul(self.rep_jets,polynomial),4)
        answer=self.lin.residual(images,self.Q4)*self.bridge4_inverse
        if self.one*answer!=a:
            raise ArithmeticError("The original residue algebra failed its unit identity.")
        return answer

    def read_log(self,delta_section,epsilon,N):
        delta=self.lin.residual(self.matrix(self.K,[list(delta_section)]),self.Q2).row(0)
        coeff=delta*self.cyclic_inverse
        return (self.trace_matrix*coeff)/(self.K(epsilon)*self.K(N))


def worker(cm):
    km,initials,N=ACTIVE
    remaining=DEADLINE-time.monotonic()
    signal.signal(signal.SIGALRM,stop)
    signal.setitimer(signal.ITIMER_REAL,max(0.1,remaining))
    try:
        value=km.run_case(int(cm),initials[int(cm)],N)
        signal.setitimer(signal.ITIMER_REAL,0)
        return {"status":"complete","candidate_id":int(cm),"certificate":value}
    except BaseException as exc:
        signal.setitimer(signal.ITIMER_REAL,0)
        emit("CM_log_case_incomplete",candidate_id=int(cm),
             exception_type=type(exc).__name__,message=str(exc),
             counters=km.counters)
        traceback.print_exc()
        return {"status":"incomplete","candidate_id":int(cm),
                "exception_type":type(exc).__name__,"message":str(exc),
                "counters":km.counters}


def main():
    global SOURCE,REQUEST_HASH,DEADLINE,STAGE,ACTIVE
    ci_only()
    raw=REQUEST.read_bytes()
    REQUEST_HASH=hashlib.sha256(raw).hexdigest()
    if REQUEST_HASH!=os.environ.get("SERRE_EXPECTED_REQUEST_SHA256"):
        raise RuntimeError("The exact request hash differs from the workflow.")
    req=json.loads(raw)
    if (req["execution_id"]!="full-p47-modq2-CM-log-v1" or req["prime"]!=47 or
            req["coefficient_prime"]!=Q or req["modulus"]!=MOD or
            req["jet_length"]!=PREC or req["sage_version"]!="10.6" or
            req["total_seconds"]!=18000 or req["reserve_seconds"]!=120 or
            req["maximum_workers"]!=4 or req["section_attempts"]!=32 or
            req["base_pencil_limit"]!=512 or req["primitive_attempts"]!=32):
        raise RuntimeError("Unexpected original mod-q^2 CM request.")
    if not req["cases"] or len(set(req["cases"]))!=len(req["cases"]) or any(
            int(cm) not in IDS for cm in req["cases"]):
        raise RuntimeError("Unexpected actual CM case list.")
    for path,wanted in req["source_sha256"].items():
        if hashlib.sha256((ROOT/path).read_bytes()).hexdigest()!=wanted:
            raise RuntimeError("Source pin mismatch: "+path)
    SOURCE=source_head()
    N=int(req["J_Fq_order_decimal"])
    if digest(str(N))!=req["J_Fq_order_json_sha256"] or N%Q!=551:
        raise ArithmeticError("The already certified complete Jacobian order changed.")
    DEADLINE=START+int(req["total_seconds"])-int(req["reserve_seconds"])
    signal.signal(signal.SIGALRM,stop)
    signal.setitimer(signal.ITIMER_REAL,max(0.1,DEADLINE-time.monotonic()))
    from sage.env import SAGE_VERSION
    from sage.all import proof
    if SAGE_VERSION!="10.6":
        raise RuntimeError("The original mod-q^2 calculation requires pinned Sage10.6.")
    proof.all(True)
    emit("preflight",source=SOURCE,run=os.environ.get("GITHUB_RUN_ID"),
         request_sha256=REQUEST_HASH,cases=req["cases"],scope=req["scope"])
    STAGE="consuming_original_graded_source"
    graded_module=module(PRE+"scripts/full_p47_graded_RR_source.py","old_graded_modq2")
    oldreq=json.loads((ROOT/req["consumed_graded_source"]["input_request"]).read_text())
    old_rr=graded_module.build_graded_source(oldreq,req["graded_certificate"])
    COMPLETED["consumed_graded_source_sha256"]=digest(old_rr["certificate"])
    STAGE="actual_lifted_CM_source"
    lifting=module(PRE+"scripts/full_p47_modq2_CM_source.py","actual_CM_modq2_source")
    lifted=lifting.build_lifted_source(req,old_rr["source"],old_rr)
    COMPLETED["lifted_source"]=lifted["certificate"]
    emit("actual_lifted_source",**lifted["certificate"])
    STAGE="actual_fixed_etale_residue_algebra"
    km=LiftedKM(old_rr,lifted,req)
    COMPLETED["residue_algebra"]=km.residue.certificate
    COMPLETED["lifted_graded_source_sha256"]={str(n):row_hash(km.M[n]) for n in range(1,6)}
    STAGE="actual_CM_divisor_initialization"
    initials=km.prepare_initials()
    COMPLETED["initial_CM_classes"]={str(k):v.stamp for k,v in initials.items()}
    km.input_chain=km.chain.copy()
    km.input_counters=dict(km.counters)
    ACTIVE=(km,initials,N)
    STAGE="actual_CM_signed_N_chains"
    COMPLETED["CM_logs"]=[]
    failures=[]
    context=multiprocessing.get_context("fork")
    with context.Pool(processes=min(int(req["maximum_workers"]),len(req["cases"]))) as pool:
        iterator=pool.imap_unordered(worker,list(map(int,req["cases"])))
        for i in range(len(req["cases"])):
            answer=iterator.next(timeout=max(0.1,DEADLINE-time.monotonic()))
            if answer["status"]=="complete":
                COMPLETED["CM_logs"].append(answer["certificate"])
            else:
                failures.append(answer)
    COMPLETED["CM_logs"].sort(key=lambda x:x["candidate_id"])
    if failures:
        COMPLETED["incomplete_cases"]=failures
        raise ArithmeticError("At least one requested CM log is incomplete; complete case records survive.")
    if [r["candidate_id"] for r in COMPLETED["CM_logs"]]!=sorted(map(int,req["cases"])):
        raise ArithmeticError("The successful log receipt omitted a requested original CM case.")
    signal.setitimer(signal.ITIMER_REAL,0)
    STAGE="complete"
    emit("receipt",status="complete",source=SOURCE,run=os.environ.get("GITHUB_RUN_ID"),
         request_sha256=REQUEST_HASH,completed=COMPLETED,result_sha256=digest(COMPLETED),
         scope="Only the listed original CM first logarithms; no QC rank or rational-point exclusion is claimed.")


if __name__=="__main__":
    try:
        main()
    except BaseException as exc:
        signal.setitimer(signal.ITIMER_REAL,0)
        emit("receipt",status="incomplete",source=SOURCE,run=os.environ.get("GITHUB_RUN_ID"),
             request_sha256=REQUEST_HASH,stage=STAGE,completed=COMPLETED,
             exception_type=type(exc).__name__,message=str(exc),
             scope="Only explicitly complete stages and per-case records survive.")
        traceback.print_exc()
        sys.exit(1)
