#!/usr/bin/env python3
"""Original full-p47 mod4513^2 source and four actual CM projective evaluations.

Arithmetic is restricted to the pinned public repository's Actions.  The
Sage process never imports python-flint.  A fresh wheel-only child exports
ONLY the old finite-field modulus and the already specified marked basis.
All q^2 arithmetic, Hensel lifts, Frobenius, Weil and source checks occur
in the Sage parent.  No new prime/model/necklace scan is performed.
"""
import hashlib
import importlib.util
from importlib.metadata import version
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time
import traceback

ROOT=Path(__file__).resolve().parents[3]
PRE="topics/serre-uniformity/"
REPO="Rogerhu12/math-research-public"
P,Q,PREC=47,4513,836
IDS=[0,141,76,108]
ALL_IDS=[0,76,77,100,108,141,196,220]
THIS=PRE+"scripts/full_p47_modq2_CM_source.py"
METHOD=PRE+"notes/2026-11-27-full-p47-modq2-CM-source-method.md"
HODGE=PRE+"scripts/full_p47_weight_one_Hodge_certificate.py"
TANGENTS=PRE+"scripts/full_p47_eight_CM_tangents.py"
TRANSFER=PRE+"scripts/original_p47_ell4513_cuspidal_transfer.py"
OLD_INPUT=PRE+"scripts/original_p47_cuspidal_disks.py"
CM_REQUEST=PRE+"notes/full-p47-CM-height-move-request.json"
TRANSFER_REQUEST=PRE+"notes/original-p47-ell4513-cuspidal-transfer-request.json"
GRADED=PRE+"scripts/full_p47_graded_RR_source.py"
REQUEST=ROOT/(PRE+"notes/full-p47-modq2-CM-source-request.json")
START=time.monotonic()
DEADLINE=None
STAGE="preflight"
COMPLETED=[]

def canonical(value):
    return json.dumps(value,sort_keys=True,separators=(",",":")).encode()

def digest(value):
    return hashlib.sha256(canonical(value)).hexdigest()

def emit(kind,**data):
    print(json.dumps(dict(kind=kind,modq2_source_seconds=time.monotonic()-START,
                         **data),sort_keys=True),flush=True)

def ci_only():
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get(
            "GITHUB_REPOSITORY")!=REPO:
        raise RuntimeError("Mathematics is restricted to this repository's public Actions.")

def check_budget():
    if DEADLINE is None or time.monotonic()>=DEADLINE:
        raise TimeoutError("No remaining time in the parent's declared arithmetic budget.")

def stop(signum,frame):
    raise TimeoutError("The shared mod-q2 source budget expired.")

def load_module(name,path):
    spec=importlib.util.spec_from_file_location(name,ROOT/path)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def rows_as_ints(M):
    return [[int(x) for x in row] for row in M.rows()]

def source_head():
    text=(ROOT/".git"/"HEAD").read_text().strip()
    if text.startswith("ref: "):
        ref=text[5:]
        if not ref.startswith("refs/") or ".." in ref.split("/"):
            raise RuntimeError("Unexpected checkout ref.")
        path=ROOT/".git"/ref
        if path.is_file():
            text=path.read_text().strip()
        else:
            matches=[line.split(" ",1)[0] for line in
                (ROOT/".git"/"packed-refs").read_text().splitlines()
                if line.endswith(" "+ref)]
            if len(matches)!=1:
                raise RuntimeError("Ambiguous checkout.")
            text=matches[0]
    if len(text)!=40 or text!=os.environ.get("GITHUB_SHA"):
        raise RuntimeError("The actual checkout and GITHUB_SHA differ.")
    return text

def check_pins(req):
    needed=(THIS,METHOD,HODGE,TANGENTS,TRANSFER,OLD_INPUT,CM_REQUEST,TRANSFER_REQUEST)
    pins=req.get("source_sha256",{})
    if any(path not in pins for path in needed):
        raise RuntimeError("The original mod-q2 source dependencies are not all pinned.")
    for path,wanted in pins.items():
        pp=Path(path)
        if pp.is_absolute() or ".." in pp.parts:
            raise RuntimeError("Invalid repository pin path.")
        if hashlib.sha256((ROOT/path).read_bytes()).hexdigest()!=wanted:
            raise RuntimeError("Source/request file pin changed: "+path)

def runtime_libraries():
    maps=Path("/proc/self/maps")
    if not maps.is_file():
        raise RuntimeError("The pinned Linux loader metadata is unavailable.")
    return sorted({line.split()[-1] for line in maps.read_text().splitlines()
        if "libflint" in line and line.split()[-1].startswith("/")})

def mm(a,b):
    return ((a[0]*b[0]+a[1]*b[2])%P,(a[0]*b[1]+a[1]*b[3])%P,
            (a[2]*b[0]+a[3]*b[2])%P,(a[2]*b[1]+a[3]*b[3])%P)

def inverse_matrix(a):
    di=pow((a[0]*a[3]-a[1]*a[2])%P,-1,P)
    return (a[3]*di%P,-a[1]*di%P,-a[2]*di%P,a[0]*di%P)

def seed_worker():
    """Export the old, marked finite-field basis; no Sage import is permitted."""
    global DEADLINE,STAGE
    ci_only()
    packet=json.loads(sys.stdin.read())
    if (packet.get("protocol")!="full-p47-modq2-seeds-v1" or
            packet.get("parent_pid")!=os.getppid() or packet.get("ids")!=IDS or
            packet.get("source")!=source_head()):
        raise RuntimeError("The seed packet is not the actual parent source.")
    if os.environ.get("SERRE_MODQ2_SEED_WORKER")!="fresh-exec-v1":
        raise RuntimeError("The seed worker requires the isolated parent entry.")
    if digest(packet["request"])!=packet["request_sha256"]:
        raise RuntimeError("The seed request packet was altered.")
    req=packet["request"]
    check_pins(req)
    DEADLINE=float(packet["deadline"])
    if not time.monotonic()<DEADLINE:
        raise TimeoutError("The seed child has no remaining parent time.")
    signal.signal(signal.SIGALRM,stop)
    signal.setitimer(signal.ITIMER_REAL,DEADLINE-time.monotonic())
    if any(name=="sage" or name.startswith("sage.") for name in sys.modules):
        raise RuntimeError("Sage was imported in the pure seed child.")
    if runtime_libraries():
        raise RuntimeError("A native FLINT library preceded the isolated wheel import.")
    from flint import fq_default_ctx,nmod_poly
    libraries=runtime_libraries()
    if version("python-flint")!="0.9.0" or len(libraries)!=1 or (
            "python_flint.libs" not in Path(libraries[0]).parts):
        raise RuntimeError("The seed child did not load exactly the wheel's bundled FLINT.")
    tangent=load_module("q2_old_tangents",TANGENTS)
    transfer=load_module("q2_old_transfer",TRANSFER)
    tangent.DEADLINE=transfer.DEADLINE=DEADLINE
    tangent.START=transfer.STARTED=float(packet["parent_started"])
    cmreq=json.loads((ROOT/CM_REQUEST).read_text())
    trreq=json.loads((ROOT/TRANSFER_REQUEST).read_text())
    if packet["descriptors"]!=cmreq["Hodge_descriptors"]:
        raise ArithmeticError("The seed request changed the original95 descriptors.")
    STAGE="consume_original_235_input"
    old,roles,character_rows,models,candidates=transfer.candidate_input(
        ROOT,trreq,nmod_poly)
    cmrows=transfer.consume_known_cm(candidates,trreq["certified_cm_rows"])
    by_id={int(row["candidate_id"]):row for row in cmrows}
    zeta0=next(z for z in range(2,Q) if pow(z,P,Q)==1)
    log0={pow(zeta0,i,Q):i for i in range(P)}
    beta=transfer.circle_values(zeta0,list(range(2,P-2,2)),log0)
    result=[]
    all_old_rows={}
    for identifier in ALL_IDS:
        check_budget()
        STAGE="old_marked_seed_%d"%identifier
        cm=by_id[identifier]
        target=[c*beta[r]%P for c,r in zip(candidates[identifier]["vector"],roles)]
        curve,pp,qq,marking=tangent.select_actual_model(
            transfer,fq_default_ctx,cm,target,roles,zeta0,beta)
        if identifier==141:
            fm=(1,0,0,1)
        else:
            a,b,c,d=map(int,marking["matching_necklace"])
            rr,ss=map(int,marking["Hodge_basis_marking"]["norm_scaling"])
            change=((rr+13*a*ss)%P,(-ss+13*a*rr)%P,
                    13*c*ss%P,13*c*rr%P)
            native=(0,P-1,1,int(marking["model"]["trace"])%P)
            fm=mm(mm(inverse_matrix(change),native),change)
        for col,point in enumerate((pp,qq)):
            expected=curve.add(curve.mul(fm[col],pp),curve.mul(fm[2+col],qq))
            if curve.frobenius(point)!=expected:
                raise ArithmeticError("The marked finite-field Frobenius matrix changed.")
        model=marking["model"]
        old_order=1 if model["j"]==1728%Q else (2 if model["j"]==0 else 0)
        old_grid,old_grid_receipt=tangent.torsion_grid(
            curve,pp,qq,old_order,model["j"])
        old_jets=tangent.original_reynolds_jets(
            curve,old_grid,packet["descriptors"],old_order)
        old_coarse,old_formula=tangent.coarse_tangent_vector(
            old_jets,model["A"],model["B"],model["j"])
        old_hashes={"G1_grid_sha256":old_grid_receipt["grid_sha256"],
            "heat_jets95_sha256":digest(old_jets),
            "coarse_tangent95_sha256":digest(old_coarse)}
        if old_hashes!=CERTIFIED_LOW_JETS[str(identifier)]:
            raise ArithmeticError("An old eight-CM input failed its original three hashes.")
        all_old_rows[str(identifier)]=old_coarse
        field=curve.field
        row={"candidate_id":identifier,"j_rational":int(cm["j_rational"]),
             "marking":marking,"P":tangent.point_key(pp),"Q":tangent.point_key(qq),
             "normalized_frobenius":list(fm),
             "coefficient_encoding":{"zero":[int(x) for x in field.zero().to_list()],
                                     "one":[int(x) for x in field.one().to_list()]}}
        if identifier in IDS:
            result.append(row)
        emit("old_modq_marked_seed",candidate_id=identifier,
             old_low_jet_hashes=old_hashes,new_modq2_basis_requested=identifier in IDS,
             field_degree=marking["field_degree"],
             tested_necklaces=marking["tested_necklaces"],
             marked_basis_sha256=digest([row["P"],row["Q"]]))
    result=sorted(result,key=lambda row:IDS.index(row["candidate_id"]))
    if sorted(map(int,all_old_rows))!=ALL_IDS:
        raise ArithmeticError("The eight original CM input rows are incomplete.")
    signal.setitimer(signal.ITIMER_REAL,0)
    answer={"protocol":"full-p47-modq2-seeds-v1","source":packet["source"],
            "request_sha256":packet["request_sha256"],"ids":IDS,"seeds":result,
            "seeds_sha256":digest(result),"flint_libraries":libraries,
            "all_CM_rows_modq":all_old_rows,
            "all_CM_rows_modq_sha256":digest(all_old_rows),
            "imports_sage":False,"full4513_scan_repeated":False}
    print(json.dumps(dict(kind="seed_packet",packet=answer),sort_keys=True),flush=True)

def consume_seeds(req,descriptors,deadline):
    check_budget()
    child_seconds=int(req.get("field_worker_seconds",1800))
    if not 1<=child_seconds<=1800:
        raise RuntimeError("The old seed input budget must lie in1..1800 seconds.")
    child_deadline=min(deadline,time.monotonic()+child_seconds)
    packet={"protocol":"full-p47-modq2-seeds-v1","source":source_head(),
            "request":req,"request_sha256":digest(req),"parent_pid":os.getpid(),
            "ids":IDS,"descriptors":descriptors,"parent_started":START,
            "deadline":child_deadline}
    env=dict(os.environ)
    env["SERRE_MODQ2_SEED_WORKER"]="fresh-exec-v1"
    proc=subprocess.Popen([sys.executable,"-u",str(ROOT/THIS),"--seed-worker"],
        stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,
        text=True,env=env)
    try:
        stdout,stderr=proc.communicate(canonical(packet).decode(),
                                     timeout=max(0.1,child_deadline-time.monotonic()))
    except BaseException:
        proc.kill()
        proc.communicate()
        raise
    finally:
        if proc.poll() is None:
            proc.kill()
            proc.communicate()
    answer=None
    for line in stdout.splitlines():
        item=json.loads(line)
        if item.get("kind")=="seed_packet":
            if answer is not None:
                raise ArithmeticError("The old seed worker emitted multiple packets.")
            answer=item["packet"]
        else:
            emit("seed_worker_progress",record=item)
    if proc.returncode!=0 or answer is None:
        if stderr:
            print(stderr[-12000:],file=sys.stderr,flush=True)
        raise RuntimeError("The isolated old-seed child failed; no q2 conclusion.")
    if (answer["source"]!=packet["source"] or answer["request_sha256"]!=digest(req)
            or answer["ids"]!=IDS or digest(answer["seeds"])!=answer["seeds_sha256"]
            or digest(answer["all_CM_rows_modq"])!=answer["all_CM_rows_modq_sha256"]):
        raise ArithmeticError("The marked seed protocol/hash did not round-trip.")
    if sorted(map(int,answer["all_CM_rows_modq"]))!=ALL_IDS:
        raise ArithmeticError("The eight consumed old CM row identifiers changed.")
    for identifier in ALL_IDS:
        row=answer["all_CM_rows_modq"][str(identifier)]
        if len(row)!=95 or digest(row)!=CERTIFIED_LOW_JETS[str(identifier)][
                "coarse_tangent95_sha256"]:
            raise ArithmeticError("An old CM input value row failed its actual original hash.")
    return answer

class UnramifiedModSquare:
    """R[theta]/F with explicit unit Newton inverses and true Frobenius lift."""
    def __init__(self,R,seed):
        from sage.all import GF,PolynomialRing,matrix,vector
        self.R=R
        self.degree=int(seed["marking"]["field_degree"])
        self.modulus=[int(a)%Q for a in seed["marking"]["field_modulus"]]
        self.encoding=seed["coefficient_encoding"]
        if (self.degree<1 or self.degree>48 or len(self.modulus)!=self.degree+1
                or self.modulus[-1]!=1):
            raise ArithmeticError("The old extension modulus is not the declared monic input.")
        self.P=PolynomialRing(R,"theta0")
        K0=GF(Q)
        KP=PolynomialRing(K0,"theta0")
        fp=KP(self.modulus)
        if not fp.is_irreducible():
            raise ArithmeticError("The actual old extension modulus is not irreducible.")
        if self.degree==1:
            self.S=R
            self.K=K0
            self.theta=R(-self.modulus[0])
        else:
            self.S=self.P.quotient(self.P(self.modulus),names=("theta",))
            self.K=GF(Q**self.degree,name="theta_bar",modulus=fp,proof=True)
            self.theta=self.S.gen()
        self.zero,self.one=self.S(0),self.S(1)
        self.F=self.P(self.modulus)
        self.Fprime=self.F.derivative()
        if self.degree==1:
            self.frob_matrix=matrix(R,[[1]])
        else:
            old_root=self.reduce(self.theta)**Q
            trial=self.lift_residue(old_root)
            root=trial-self.evaluate(self.F,trial)*self.inv(self.evaluate(self.Fprime,trial))
            if self.evaluate(self.F,root)!=self.zero or self.reduce(root)!=old_root:
                raise ArithmeticError("The unramified Frobenius root did not Hensel lift.")
            powers=[self.one]
            for _ in range(1,self.degree):
                powers.append(powers[-1]*root)
            self.frob_matrix=matrix(R,[self.coefficients(x,pad=True) for x in powers]).transpose()
            current=self.theta
            for _ in range(self.degree):
                current=self.sigma(current)
            if current!=self.theta:
                raise ArithmeticError("The genuine lifted Frobenius has the wrong period.")
        if self.sigma(self.one)!=self.one:
            raise ArithmeticError("The genuine Frobenius did not fix the base identity.")

    def coefficients(self,value,pad=False):
        value=self.S(value)
        out=[int(value)] if self.degree==1 else [int(a) for a in value.lift().list()]
        while out and out[-1]==0:
            out.pop()
        if pad:
            out=out+[0]*(self.degree-len(out))
        return out

    def from_coefficients(self,coeff):
        coeff=[self.R(int(a)) for a in coeff]
        if len(coeff)>self.degree and any(coeff[self.degree:]):
            raise ArithmeticError("An extension coefficient packet exceeds its old basis.")
        return self.R(coeff[0]) if self.degree==1 and coeff else (
            self.R(0) if self.degree==1 else self.S(self.P(coeff)))

    def reduce(self,value):
        c=[a%Q for a in self.coefficients(value)]
        return self.K(c[0] if c else 0) if self.degree==1 else self.K(c)

    def lift_residue(self,value):
        coeff=[int(value)] if self.degree==1 else [int(a) for a in value.polynomial().list()]
        return self.from_coefficients(coeff)

    def inv(self,value):
        value=self.S(value)
        reduced=self.reduce(value)
        if not reduced:
            raise ArithmeticError("A q-divisible denominator was encountered.")
        guess=self.lift_residue(reduced**(-1))
        answer=guess*(2-value*guess)
        if value*answer!=self.one:
            raise ArithmeticError("The unit Newton inverse failed in the original ring.")
        return answer

    def evaluate(self,poly,x):
        out=self.zero
        for c in reversed(poly.list()):
            out=out*x+self.S(c)
        return out

    def sigma(self,value):
        from sage.all import vector
        coeff=self.frob_matrix*vector(self.R,self.coefficients(value,pad=True))
        return self.from_coefficients(list(coeff))

    def base_integer(self,value):
        coeff=self.coefficients(value,pad=True)
        if any(coeff[1:]) or self.sigma(value)!=self.S(value):
            raise ArithmeticError("A complete original Reynolds value did not descend to R.")
        return int(coeff[0])

    def old_coefficients(self,value):
        coeff=[a%Q for a in self.coefficients(value,pad=True)]
        if self.degree>1 and len(self.encoding["one"])==self.degree:
            return coeff
        while coeff and coeff[-1]==0:
            coeff.pop()
        if not coeff:
            return list(self.encoding["zero"])
        return coeff

    def old_point_key(self,point):
        return tuple(tuple(self.old_coefficients(x)) for x in point)

    def point_key(self,point):
        return tuple(tuple(self.coefficients(x,pad=True)) for x in point)

class LiftedCurve:
    def __init__(self,ur,a,b):
        self.ur=ur
        self.a=ur.S(a)
        self.b=ur.S(b)
    def check(self,point):
        if point is not None:
            x,y=point
            if y*y!=x*x*x+self.a*x+self.b:
                raise ArithmeticError("A lifted point failed the actual short equation.")
        return point
    def neg(self,point):
        return None if point is None else (point[0],-point[1])
    def add_with_slope(self,left,right):
        if left is None or right is None:
            raise ArithmeticError("An original slope step unexpectedly used O.")
        x,y=left
        xx,yy=right
        if x==xx:
            if y!=yy or not self.ur.reduce(y):
                raise ArithmeticError("An original slope step met a vertical line.")
            slope=(3*x*x+self.a)*self.ur.inv(2*y)
        else:
            slope=(yy-y)*self.ur.inv(xx-x)
        nx=slope*slope-x-xx
        out=self.check((nx,slope*(x-nx)-y))
        return out,slope
    def add(self,left,right):
        if left is None:
            return right
        if right is None:
            return left
        if left[0]==right[0] and left[1]==-right[1]:
            return None
        return self.add_with_slope(left,right)[0]
    def mul(self,n,point):
        if n<0:
            return self.mul(-n,self.neg(point))
        answer=None
        while n:
            if n&1:
                answer=self.add(answer,point)
            n>>=1
            if n:
                point=self.add(point,point)
        return answer
    def chain46(self,point,with_e=False):
        current,total,n=point,self.ur.zero,1
        for next_n in (2,4,5,10,11,22,23,46):
            if next_n==2*n:
                current,slope=self.add_with_slope(current,current)
                total=2*total+slope
            elif next_n==n+1:
                current,slope=self.add_with_slope(current,point)
                total=total+slope
            else:
                raise ArithmeticError("The original47 slope chain changed.")
            n=next_n
        if with_e:
            if current!=self.neg(point):
                raise ArithmeticError("The original G1 seed is not47-torsion.")
            return -total*self.ur.inv(self.ur.S(P))
        return current
    def lift_torsion(self,old):
        ur=self.ur
        x=ur.from_coefficients(old[0])
        y=ur.from_coefficients(old[1])
        y=y-(y*y-x*x*x-self.a*x-self.b)*ur.inv(2*y)
        trial=self.check((x,y))
        x46,y46=self.chain46(trial)
        s=(x46-x)*ur.inv(y46-y)
        if ur.reduce(s):
            raise ArithmeticError("The last inverse slope is not q-divisible.")
        tau=-s*ur.inv(ur.S(P))
        answer=self.check((x+2*y*tau,y+(3*x*x+self.a)*tau))
        if ur.old_point_key(answer)!=tuple(tuple(row) for row in old):
            raise ArithmeticError("The exact torsion lift changed the old marked point.")
        if self.chain46(answer)!=self.neg(answer):
            raise ArithmeticError("The unit correction did not produce actual47-torsion.")
        return answer
    def line_step(self,left,right,evaluation):
        x,y=left
        xx,yy=right
        xt,yt=evaluation
        if x==xx and y==-yy:
            value=xt-x
            self.ur.inv(value)
            return value,None
        out,slope=self.add_with_slope(left,right)
        numerator=-yt+y+slope*(xt-x)
        denominator=xt-out[0]
        self.ur.inv(numerator)
        return numerator*self.ur.inv(denominator),out
    def miller(self,point,evaluation):
        value,current=self.ur.one,point
        for bit in bin(P)[3:]:
            line,current=self.line_step(current,current,evaluation)
            value=value*value*line
            if bit=="1":
                line,current=self.line_step(current,point,evaluation)
                value=value*line
        if current is not None:
            raise ArithmeticError("The exact lifted Miller chain did not end at O.")
        return value
    def weil(self,left,right):
        return -self.miller(left,right)*self.ur.inv(self.miller(right,left))

def primitive_root_lift(R,residue,order):
    r=R(residue)
    derivative=R(order)*r**(order-1)
    if int(derivative)%Q==0:
        raise ArithmeticError("A tame root derivative is not a unit.")
    root=r-(r**order-1)*derivative**(-1)
    if root**order!=1 or int(root)%Q!=residue%Q:
        raise ArithmeticError("The original primitive root did not Hensel lift.")
    return root

def build_grid(curve,pp,qq,fm,order,j,root2):
    ur=curve.ur
    ep,eq=curve.chain46(pp,True),curve.chain46(qq,True)
    points={(1,0):pp,(0,1):qq}
    values={(1,0):ep,(0,1):eq}
    for n in range(2,P):
        for axis,initial,ei in ((0,pp,ep),(1,qq,eq)):
            previous=(n-1,0) if axis==0 else (0,n-1)
            key=(n,0) if axis==0 else (0,n)
            point,slope=curve.add_with_slope(points[previous],initial)
            points[key]=point
            values[key]=values[previous]+ei+slope
    for b in range(1,P):
        check_budget()
        for a in range(1,P):
            point,slope=curve.add_with_slope(points[a-1,b],pp)
            points[a,b]=point
            values[a,b]=values[a-1,b]+ep+slope
    if len(points)!=P*P-1:
        raise ArithmeticError("The original complete torsion grid changed size.")
    inverse={ur.point_key(point):label for label,point in points.items()}
    if len(inverse)!=P*P-1:
        raise ArithmeticError("Two lifted marked torsion labels collided.")
    oldhash=hashlib.sha256()
    newhash=hashlib.sha256()
    jets={}
    for label in sorted(points):
        a,b=label
        point=curve.check(points[label])
        x,y=point
        e=values[label]
        neg=(-a%P,-b%P)
        frob=((fm[0]*a+fm[1]*b)%P,(fm[2]*a+fm[3]*b)%P)
        if points[neg]!=curve.neg(point) or values[neg]!=-e:
            raise ArithmeticError("The full lifted odd G1 identity failed.")
        if points[frob]!=(ur.sigma(x),ur.sigma(y)) or values[frob]!=ur.sigma(e):
            raise ArithmeticError("The complete lifted grid lost actual Frobenius.")
        row=[e]
        if order>=1:
            row.append(-x*e-y)
        if order>=2:
            # DERIVATIVES, not Taylor coefficients; A2'=4A is included.
            row.append(-2*e*e*y-4*x*x*e-2*curve.a*e-2*x*y)
        jets[label]=row
        oldhash.update(canonical([list(label),ur.old_point_key(point),
                                  [ur.old_coefficients(v) for v in row]])+b"\n")
        newhash.update(canonical([list(label),ur.point_key(point),
                    [ur.coefficients(v,pad=True) for v in row]])+b"\n")
    auto=None
    if j%Q==1728:
        ii=ur.S(primitive_root_lift(ur.R,95,4))
        if ii*ii!=-ur.one:
            raise ArithmeticError("The exact Gaussian square root changed.")
        columns=[]
        for point in (pp,qq):
            image=(-point[0],ii*point[1])
            columns.append(inverse[ur.point_key(image)])
        auto=[columns[0][0],columns[1][0],columns[0][1],columns[1][1]]
        if auto!=[0,P-1,1,0]:
            raise ArithmeticError("The full Gaussian automorphism marking changed.")
    elif j%Q==0:
        rho0=next(r for r in range(2,Q) if pow(r,3,Q)==1)
        rho=ur.S(primitive_root_lift(ur.R,rho0,3))
        columns=[]
        for point in (pp,qq):
            columns.append(inverse[ur.point_key((rho*point[0],point[1]))])
        auto=[columns[0][0],columns[1][0],columns[0][1],columns[1][1]]
        a,b,c,d=auto
        if ((a-d)%P or (b+c)%P or (a+d)%P!=P-1 or
                (a*d-b*c)%P!=1 or mm(auto,auto)==(1,0,0,1)):
            raise ArithmeticError("The full cubic automorphism marking changed.")
    return jets,{"point_count":P*P-1,"heat_order":order,
        "old_G1_grid_sha256":oldhash.hexdigest(),"q2_G1_grid_sha256":newhash.hexdigest(),
        "stabilizer_matrix":auto,"frobenius_matrix":list(fm),
        "curve_46_negative_Frobenius_odd_checks":True}

def product_jet(left,right):
    out=[left[0]*right[0]]
    if len(left)>1:
        out.append(left[1]*right[0]+left[0]*right[1])
    if len(left)>2:
        out.append(left[2]*right[0]+2*left[1]*right[1]+left[0]*right[2])
    return out

def reynolds_jets(curve,jets,descriptors,order,zeta):
    ur=curve.ur
    groups={n:[] for n in range(1,P)}
    for a in range(P):
        for b in range(P):
            if (a or b) and (a,b)<(-a%P,-b%P):
                norm=(a*a+b*b)%P
                if not norm:
                    raise ArithmeticError("A nonzero nonsplit vector had zero norm.")
                groups[norm].append((a,b))
    if any(len(labels)!=24 for labels in groups.values()):
        raise ArithmeticError("The original full46 norm fibers changed.")
    requested={}
    for i,(a,c,d) in enumerate(descriptors):
        requested.setdefault((int(c),int(d)),[]).append((i,int(a)))
    zetas=[ur.S(zeta**n) for n in range(P)]
    result={}
    for (c,d),rows in requested.items():
        check_budget()
        first,second={},{}
        for norm,labels in groups.items():
            f=[ur.zero for _ in range(order+1)]
            g=[ur.zero for _ in range(order+1)]
            for a,b in labels:
                left=jets[a,b]
                right=jets[(d*a-c*b)%P,(c*a+d*b)%P]
                conjugate=jets[(d*a+c*b)%P,(-c*a+d*b)%P]
                fprod,gprod=product_jet(left,right),product_jet(left,conjugate)
                for n in range(order+1):
                    f[n]+=2*fprod[n]
                    g[n]+=2*gprod[n]
            first[norm],second[norm]=f,g
        for index,a in rows:
            total=[ur.zero for _ in range(order+1)]
            for norm in range(1,P):
                for n in range(order+1):
                    total[n]+=zetas[a*norm%P]*first[norm][n]
                    total[n]+=zetas[-a*norm%P]*second[norm][n]
            result[index]=[ur.base_integer(v) for v in total]
    if len(result)!=95:
        raise ArithmeticError("The lifted original95 descriptor set is incomplete.")
    return [result[i] for i in range(95)]

def coarse_vector(R,jets,a,b,j):
    if j%Q==1728:
        if any(row[0] for row in jets):
            raise ArithmeticError("The actual lifted Gaussian character did not vanish.")
        scale=-R(41472*a)**(-1)
        return [int(scale*R(row[1])) for row in jets]
    if j%Q==0:
        if any(row[0] or row[1] for row in jets):
            raise ArithmeticError("The actual lifted cubic character did not vanish.")
        scale=R(331776*b)**(-1)
        return [int(scale*R(row[2])) for row in jets]
    disc=R(4)*a**3+R(27)*b**2
    scale=disc*R(124416*a*a*b)**(-1)
    return [int(scale*R(row[0])) for row in jets]

def model_coefficients(R,identifier,j):
    if identifier==141:
        a,b=R(343),R(0)
    elif identifier==0:
        a,b=R(0),R(1)
    else:
        scale=R(j)*R(1728-j)**(-1)
        a,b=3*scale,2*scale
    disc=4*a**3+27*b**2
    if not int(disc)%Q or R(6912)*a**3*disc**(-1)!=R(j):
        raise ArithmeticError("The actual rational CM j was not lifted.")
    return a,b

# Literal prior public run45968484065/job140402824955 pins; no new evaluation.
CERTIFIED_LOW_JETS={
    "0": {
        "coarse_tangent95_sha256": "a8bb8a93e48b8508002ef8db853733a0785d41ff103c8c0bbb72e98ccb29354c",
        "heat_jets95_sha256": "b0a394cb0db9ae2804920ab9c2d767619d905c55cd9613ec29ca09f45d19cc1e",
        "G1_grid_sha256": "6d65eb6cfa14b23f7568d6de553b252b50a474a74e668f84d6e537a129921329"
    },
    "76": {
        "coarse_tangent95_sha256": "25f16f989716b2d7b3d80bd217bda8de3c0738dbfea0a65fb9eee2608c21233e",
        "heat_jets95_sha256": "1948b2c153fc0b244d097de49f611653ab8d91ca30ee84b87f5e51ec588cf0e0",
        "G1_grid_sha256": "979d166e9ee0fafd4de96796a7ce15d4af2ade0a32bfce526e576d6a23650acf"
    },
    "77": {
        "coarse_tangent95_sha256": "0e2265efba451a84394a870e3c8321d90d7541900a964bd4c0d04b09b52a6c91",
        "heat_jets95_sha256": "b1b76bee51bdade3f3dee904c631139f0bb26652fa6c124dccc8c7ad59dc8250",
        "G1_grid_sha256": "dde8dabb768917ab7d8e2362c06d7b44bce7c8f487d0196a25a7505863e12326"
    },
    "100": {
        "coarse_tangent95_sha256": "7aa3de36e17d42d4a5e32b24e5d3b610082390725efa77806f89e8ad5300463f",
        "heat_jets95_sha256": "40aff556f26e6771cc0e8807c38e8aaab9a6920f2b4ec5d0778875030eb5c2d8",
        "G1_grid_sha256": "7e2677dbfc610a7e306bc1a5fe9f0a19f54a1ef1f692293987243f28aba180aa"
    },
    "108": {
        "coarse_tangent95_sha256": "db3808c45948dbcea8fc08b95c48eb3a54101e733331f513f27f39f1cac550cb",
        "heat_jets95_sha256": "358c4687bd56812ebc09c9232919681b4eb2e5db4a75c28e21496e7a67ee4c02",
        "G1_grid_sha256": "4548dc9089588e4f0830e30e4c13249e14e133dd297a4e136bb9eb44295d7966"
    },
    "141": {
        "coarse_tangent95_sha256": "3cb7cc4c045604b4de037ea31348d13af728bbff8c2776916b427649544062c0",
        "heat_jets95_sha256": "924a12b24cd6b6280b2e4dfb38d2a09e001a914ad773ba7ef6edf2e1b15e5e7c",
        "G1_grid_sha256": "c11f5a157c6bb4f9e4438f0d392ee24823d7973080270544cfc6acabc74ac0fd"
    },
    "196": {
        "coarse_tangent95_sha256": "0cdb616c7ba3dc81e3bc2fd6e56381bfb44dfdf2552af53b9cf5b586303fdd58",
        "heat_jets95_sha256": "28860af123882cf3f67c4bfb785212e39f150ba76f5bd721a66c090a33a1f338",
        "G1_grid_sha256": "5016bb66bd604b3fac6ba69f80dc02abb09e2216d84f0a24692f132655530689"
    },
    "220": {
        "coarse_tangent95_sha256": "c319cf9e27820e348e091b337b57f1beba9edb9b5c313d7feee4b22c0c14f62d",
        "heat_jets95_sha256": "329978f5b83da6eb84cc23eff2d9b9069ebb737d3d4a7e27e71bad8bdea9695e",
        "G1_grid_sha256": "3540a9a4a714c9264685dc71e7759532d3dae02c279efd66cfe4e92d8bf079b6"
    }
}

def evaluate_cm(R,seed,descriptors,zeta):
    check_budget()
    identifier=int(seed["candidate_id"])
    j=int(seed["j_rational"])
    if digest([seed["P"],seed["Q"]])!=seed["marking"]["Hodge_basis_marking"]["basis_sha256"]:
        raise ArithmeticError("The old marked basis receipt did not match its coefficients.")
    ur=UnramifiedModSquare(R,seed)
    a,b=model_coefficients(R,identifier,j)
    oldmodel=seed["marking"]["model"]
    if int(a)%Q!=oldmodel["A"] or int(b)%Q!=oldmodel["B"]:
        raise ArithmeticError("The lifted rational model changed the old actual model.")
    curve=LiftedCurve(ur,a,b)
    pp=curve.lift_torsion(seed["P"])
    qq=curve.lift_torsion(seed["Q"])
    fm=tuple(map(int,seed["normalized_frobenius"]))
    for col,point in enumerate((pp,qq)):
        expected=curve.add(curve.mul(fm[col],pp),curve.mul(fm[2+col],qq))
        if (ur.sigma(point[0]),ur.sigma(point[1]))!=expected:
            raise ArithmeticError("The true unramified Frobenius changed the actual marking.")
    weil=curve.weil(pp,qq)
    if weil!=ur.S(zeta) or weil**P!=ur.one or ur.reduce(weil)!=ur.K(2):
        raise ArithmeticError("The unique lifted Weil root is not the original zeta.")
    order=1 if identifier==141 else (2 if identifier==0 else 0)
    grid,gridcert=build_grid(curve,pp,qq,fm,order,j,zeta)
    rows=reynolds_jets(curve,grid,descriptors,order,zeta)
    coarse=coarse_vector(R,rows,a,b,j)
    oldrows=[[int(x)%Q for x in row] for row in rows]
    oldcoarse=[x%Q for x in coarse]
    expected=CERTIFIED_LOW_JETS[str(identifier)]
    actual={"G1_grid_sha256":gridcert["old_G1_grid_sha256"],
            "heat_jets95_sha256":digest(oldrows),
            "coarse_tangent95_sha256":digest(oldcoarse)}
    if actual!=expected:
        raise ArithmeticError("A q2 source failed an original modq grid/heat/coarse hash: %d"%identifier)
    pivot=next((i for i,x in enumerate(coarse) if x%Q),None)
    if pivot is None:
        raise ArithmeticError("The original CM source has no unit projective denominator.")
    inverse=R(coarse[pivot])**(-1)
    values=[int(R(x)*inverse) for x in coarse]
    if values[pivot]!=1:
        raise ArithmeticError("The projective CM row was not normalized.")
    old_inverse=pow(oldcoarse[pivot],-1,Q)
    if [x%Q for x in values]!=[x*old_inverse%Q for x in oldcoarse]:
        raise ArithmeticError("The lifted projective row changed its original reduction.")
    return {"candidate_id":identifier,"j_rational":j,"coarse_parameter":"j-j_CM",
        "denominator_index":pivot,"projective_values95":values,
        "coarse_values95":coarse,"coarse_tangent95_sha256":actual["coarse_tangent95_sha256"],
        "old_low_jet_hashes":actual,"q2_heat_jets95_sha256":digest(rows),
        "q2_projective95_sha256":digest(values),"q2_coarse95_sha256":digest(coarse),
        "field_modulus":ur.modulus,"field_degree":ur.degree,
        "q2_model":[int(a),int(b)],"q2_zeta":int(zeta),
        "marked_seed_sha256":digest(seed),"grid_certificate":gridcert,
        "torsion_lift_unique_and_checked":True,"actual_Frobenius_checked":True,
        "actual_Weil_root_checked":True}

def build_lifted_source(req,old_source,old_rr,*,deadline=None,callback=None):
    """Return actual R-source in the original95 order, never a lifted old kernel.

    Caller supplies the previously certified build_graded_source result.
    n=2,...,5 product pairs and unit-pivot RR are left to the caller.
    The deadline is shared with its entire request; no second budget is opened.
    """
    global DEADLINE,STAGE
    ci_only()
    check_pins(req)
    if deadline is None:
        deadline=req.get("absolute_deadline")
    if deadline is None:
        remaining,_interval=signal.getitimer(signal.ITIMER_REAL)
        if remaining<=0:
            raise RuntimeError("The parent must supply a deadline or an active total-budget alarm.")
        deadline=time.monotonic()+remaining
    DEADLINE=float(deadline)
    check_budget()
    if (int(req.get("prime",P))!=P or int(req.get("coefficient_prime",Q))!=Q or
            int(req.get("modulus",Q*Q))!=Q*Q or int(req.get("jet_length",PREC))!=PREC or
            list(req.get("basic_CM_candidate_ids",IDS))!=IDS):
        raise RuntimeError("The declared original modq2 inputs changed.")
    if ("certified_CM_low_jet_hashes" in req and
            req["certified_CM_low_jet_hashes"]!=CERTIFIED_LOW_JETS):
        raise ArithmeticError("The request changed a literal original eight-CM low-jet pin.")
    if any(name=="flint" or name.startswith("flint.") for name in sys.modules):
        raise RuntimeError("The Sage parent must not import the python-flint wheel.")
    from sage.all import Zmod,PolynomialRing,matrix
    from sage.env import SAGE_VERSION
    if SAGE_VERSION!="10.6":
        raise RuntimeError("The modq2 source is pinned to Sage10.6.")
    if old_rr["source"]["certificate"]!=old_source["certificate"]:
        raise ArithmeticError("The old graded and Hodge sources are inconsistent.")
    cmreq=json.loads((ROOT/CM_REQUEST).read_text())
    if old_source["descriptors"]!=cmreq["Hodge_descriptors"] or (
            old_source["certificate"]!=cmreq["Hodge_certificate"]):
        raise ArithmeticError("The supplied old source is not the certified original95 source.")
    if old_rr["matrices"][1].nrows()!=95 or old_rr["matrices"][1].ncols()!=PREC:
        raise ArithmeticError("The parent did not provide the original836-jet source.")
    def note(kind,**data):
        emit(kind,**data)
        if callback is not None:
            callback(kind,**data)
    STAGE="old_marked_seed_export"
    seed_packet=consume_seeds(req,old_source["descriptors"],DEADLINE)
    R=Zmod(Q*Q)
    zeta=primitive_root_lift(R,2,P)
    hodge=load_module("modq2_original_Hodge",HODGE)
    class LiftedSource(hodge.Original47Source):
        def __init__(self):
            ci_only()
            self.p,self.q,self.root=P,Q*Q,int(zeta)
            self.K=R
            self.PR=PolynomialRing(R,"t")
            self.inv2=pow(2,-1,Q*Q)
            self.inv47=pow(P,-1,Q*Q)
            self.callback=None
            self.labels=[(c,d) for c in range(P) for d in range(P) if c or d]
            self.half=[x for x in self.labels if x<self.neg(x)]
            counts={n:0 for n in range(1,P)}
            for x in self.half:
                counts[self.norm(x)]+=1
            if len(self.half)!=1104 or any(n!=24 for n in counts.values()):
                raise ArithmeticError("The original lifted half-vector fibers changed.")
            self._series_key=None
            self._series_value=None
            self.half_series_sha256=None
    STAGE="actual_modq2_Tate_and_cusps"
    engine=LiftedSource()
    descriptors=old_source["descriptors"]
    M=engine.jets(descriptors,length=PREC)
    residues=engine.residues(descriptors)
    cusp=residues*R(P)**(-1)
    reduced_M=matrix(old_source["K"],[[int(x)%Q for x in row] for row in M.rows()])
    reduced_cusp=matrix(old_source["K"],[[int(x)%Q for x in row] for row in cusp.rows()])
    if reduced_M!=old_rr["matrices"][1] or reduced_cusp!=old_rr["cusp_values"][1]:
        raise ArithmeticError("Actual modq2 global sections do not reduce to the original RR source.")
    if any(sum(residues.row(b)[j] for b in range(23))!=0 for j in range(95)):
        raise ArithmeticError("The full23 lifted residues do not sum to zero.")
    if list(cusp.row(0))!=list(M.column(0)):
        raise ArithmeticError("The standard cusp value and original Tate constant differ.")
    polys=[engine.PR(list(row)) for row in M.rows()]
    cert={"prime":P,"coefficient_prime":Q,"precision":2,"modulus":Q*Q,
        "primitive_root_modq":2,"primitive_root_modq2":int(zeta),
        "descriptors_sha256":digest(descriptors),"jet_length":PREC,
        "L1_modq2_jets_sha256":digest(rows_as_ints(M)),
        "all23_modq2_cusp_values_sha256":digest(rows_as_ints(cusp)),
        "all23_modq2_residues_sha256":digest(rows_as_ints(residues)),
        "consumed_modq_graded_certificate_sha256":digest(old_rr["certificate"]),
        "consumed_modq_Hodge_certificate_sha256":digest(old_source["certificate"]),
        "old_seeds_sha256":seed_packet["seeds_sha256"],
        "all_CM_rows_modq_sha256":seed_packet["all_CM_rows_modq_sha256"],
        "modq_long_jet_and_all23_values_exact":True,
        "holomorphic_kernel_lifted_here":False,
        "no_Hecke_log_or_Miller_chain_computed":True}
    note("actual_modq2_global_source",certificate=cert)
    rows={}
    for seed in seed_packet["seeds"]:
        identifier=int(seed["candidate_id"])
        STAGE="actual_modq2_CM_%d"%identifier
        row=evaluate_cm(R,seed,descriptors,zeta)
        rows[identifier]=row
        COMPLETED.append(identifier)
        note("actual_modq2_CM_source",record=row)
    if list(rows)!=IDS:
        raise ArithmeticError("The four prescribed basic CM sources are incomplete.")
    cert["CM_rows_sha256"]=digest([rows[i] for i in IDS])
    cert["CM_candidate_ids"]=IDS
    note("modq2_source_certificate",certificate=cert,certificate_sha256=digest(cert))
    return {"ring":R,"polynomial_ring":engine.PR,"engine":engine,
        "descriptors":descriptors,"polynomials":{1:polys},"matrices":{1:M},
        "cusp_values":{1:cusp},"residues":residues,
        "CM_rows":{i:rows[i]["projective_values95"] for i in IDS},
        "CM_records":rows,
        "all_CM_rows_modq":{int(i):row for i,row in seed_packet["all_CM_rows_modq"].items()},
        "CM_projective_values":matrix(R,[rows[i]["projective_values95"] for i in IDS]),
        "CM_candidate_ids":IDS,"certificate":cert,
        "old_source":old_source,"old_rr":old_rr}

def main():
    global DEADLINE,STAGE
    ci_only()
    raw=REQUEST.read_bytes()
    req=json.loads(raw)
    if hashlib.sha256(raw).hexdigest()!=os.environ.get("SERRE_EXPECTED_REQUEST_SHA256"):
        raise RuntimeError("The public modq2 request pin changed.")
    check_pins(req)
    if req.get("sage_version")!="10.6":
        raise RuntimeError("The request must explicitly pin Sage10.6.")
    total,reserve=int(req["total_seconds"]),int(req["reserve_seconds"])
    if not 0<reserve<total<=18000:
        raise RuntimeError("The total public arithmetic budget is not bounded.")
    DEADLINE=START+total-reserve
    signal.signal(signal.SIGALRM,stop)
    signal.setitimer(signal.ITIMER_REAL,max(0.1,DEADLINE-time.monotonic()))
    if GRADED not in req["source_sha256"]:
        raise RuntimeError("The standalone entry must pin its original graded-source module.")
    graded_module=load_module("modq2_original_RR",GRADED)
    graded_module.DEADLINE=DEADLINE
    STAGE="consume_original_graded_input"
    graded=graded_module.build_graded_source(req["old_graded_request"],
                                           expected_certificate=req["old_graded_certificate"])
    lifted=build_lifted_source(req,graded["source"],graded,deadline=DEADLINE)
    signal.setitimer(signal.ITIMER_REAL,0)
    STAGE="complete"
    emit("receipt",status="complete",source=source_head(),
        request_sha256=hashlib.sha256(raw).hexdigest(),
        certificate=lifted["certificate"],certificate_sha256=digest(lifted["certificate"]),
        scope="Actual mod4513^2 original95/836/all23 and four marked CM projective rows only; no new Abel log, height or rational-point exclusion.")

if __name__=="__main__":
    try:
        if sys.argv[1:]==["--seed-worker"]:
            seed_worker()
        elif not sys.argv[1:]:
            main()
        else:
            raise RuntimeError("Unexpected command-line arguments.")
    except BaseException as exc:
        signal.setitimer(signal.ITIMER_REAL,0)
        emit("receipt",status="incomplete",stage=STAGE,
             completed_basic_CM_ids=COMPLETED,exception_type=type(exc).__name__,
             message=str(exc),scope="Only individual completed exact source checks survive.")
        traceback.print_exc()
        sys.exit(1)
