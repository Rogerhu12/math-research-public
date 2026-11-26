#!/usr/bin/env python3
"""R943: new E89 fifth original low jet, exact angular membership, and norm.
Public Actions only; standard-library reader and the original python-flint 0.9.0 producer.
No generated output files.
The original full CM reader is run in the same job and its unique mass line
is passed in memory. No generated source coefficient table is stored.
"""
from fractions import Fraction as Q
import hashlib,json,pathlib,subprocess,sys
_producer=pathlib.Path(__file__).resolve().parent/"check-r943-degree178-full-cm-source.py"
_proc=subprocess.run([sys.executable,str(_producer),"--workers=4"],
                     stdout=subprocess.PIPE,stderr=None,text=True,check=True)
_report=json.loads(_proc.stdout)
assert _report["status"]=="PASS"
assert _report["canonical_matrix_sha256"]=="6ee0222d90db6add172d6d6e650a2f8186b1776072661594a242b4e65c78d665"
assert _report["joint_mass_kernel_dimension"]==1
_line=_report["joint_mass_kernel"][0]
assert _line["origin_order"]==6
_cs=_line["polynomial_X_ascending"]
assert len(_cs)==30 and _cs[29]==["0","0"] and _cs[28]==["1","0"]
assert all(x[1]=="0" for x in _cs)
SOURCE_ASC=[Q(x[0]) for x in _cs[:29]]
del _proc,_report,_line,_cs

N=5
def pm(a,b):
    out=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out
def product(factors,den=1):
    p=[Q(1)]
    for a in factors:p=pm(p,[Q(x) for x in a])
    return [x/den for x in p]
def trim(p):
    p=list(p)
    while p and not p[-1]:p.pop()
    return p
def pdiv(a,b):
    a=trim(a);b=trim(b);q=[Q(0)]*max(0,len(a)-len(b)+1)
    while len(a)>=len(b):
        j=len(a)-len(b);c=a[-1]/b[-1];q[j]=c
        for k,x in enumerate(b):a[j+k]-=c*x
        a=trim(a)
    return trim(q),a
def trunc(a):return list(a[:N])+[Q(0)]*max(0,N-len(a))
def smul(a,b):return trunc(pm(trunc(a),trunc(b)))
def sinv(a):
    a=trunc(a);assert a[0]
    out=[1/a[0]]+[Q(0)]*(N-1)
    for n in range(1,N):out[n]=-sum(a[i]*out[n-i] for i in range(1,n+1))/a[0]
    return out
def spow(a,n):
    if n<0:a,n=sinv(a),-n
    out=trunc([Q(1)])
    while n:
        if n&1:out=smul(out,a)
        a=smul(a,a);n//=2
    return out
def sexp(a):
    a=trunc(a);assert not a[0]
    out=[Q(1)]+[Q(0)]*(N-1)
    for n in range(1,N):out[n]=sum(i*a[i]*out[n-i] for i in range(1,n+1))/n
    return out
def compose(p,a):
    out=[Q(0)]*N
    for c in reversed(p):
        out=smul(out,a);out[0]+=c
    return out
def determinant(a):
    a=[list(row) for row in a];n=len(a);out=Q(1)
    for j in range(n):
        k=next((i for i in range(j,n) if a[i][j]),None)
        if k is None:return Q(0)
        if k!=j:a[j],a[k]=a[k],a[j];out=-out
        v=a[j][j];out*=v
        for i in range(j+1,n):
            t=a[i][j]/v
            for k in range(j+1,n):a[i][k]-=t*a[j][k]
            a[i][j]=Q(0)
    return out
def source_jets():
    W=[Q(1),Q(-1,7)]+[Q(0)]*(N-2)
    for n in range(2,N):
        W[n]=sum(W[i]*W[n-i] for i in range(1,n))/((6*n+1)*(n-1))
    log_sigma=[Q(0)]+[-W[i]/(6*i*(6*i-1)) for i in range(1,N)]
    a=smul(trunc([Q(0),Q(1)]),spow(W,-3))
    PS=product([[1,1],[1,-8],[7,-4,16]],7)
    PT=pm(PS,product([[1,4],[1,-96,48,64],[1,20,-8]]))
    PU=product([[1,1],[1,20,-8],[7,-4,16],
       [1,40,2112,3136,1792],[13,52,1536,1024,256],
       [1,1232,-58688,-49408,-439040,-2111488,-1949696,-851968,-32768]],91)
    PV=product([[1,1],[1,-8],[1,-8],[1,4],[7,-4,16],[1,228,48,64]],7)
    result=[]
    for name,n,p in (("S34",17,PS),("T72",36,PT),("U136",68,PU),
                     ("V66",33,PV),("W178",89,list(reversed(SOURCE_ASC)))):
        jet=smul(sexp([2*n*x for x in log_sigma]),
                 smul(spow(W,n-3),compose(p,a)))
        assert jet[0]==1
        result.append((name,jet))
    expected=[
      ["1","-988/105","16594771/1576575","-12606807124/725830875"],
      ["1","-2938/35","-230804229/175175","2448768505164/152334875"],
      ["1","135218/105","21083507491/1576575","1377083080404572/9435801375"],
      ["1","7436/35","-53394351/15925","115502678148/13848625"]]
    for (_,jet),old in zip(result,expected):assert jet[:4]==[Q(x) for x in old]
    b4=determinant([list(reversed(jet[:4])) for _,jet in result[:4]])
    assert b4==Q(-33226598045199130624,173559375)
    b5=determinant([list(reversed(jet)) for _,jet in result])
    return result,b4,b5
def local_norm():
    q=89
    def mul(a,b):return ((a[0]*b[0]-3*a[1]*b[1])%q,(a[0]*b[1]+a[1]*b[0])%q)
    def power(a,n):
        b=(1,0)
        while n:
            if n&1:b=mul(b,a)
            a=mul(a,a);n//=2
        return b
    omega=(44,45)
    lift={(1,0):(1,0),omega:(0,1),mul(omega,omega):(-1,-1)}
    sa=sb=count=0
    for x in range(q):
        for y in range(1,q):
            if (x*x+3*y*y-1)%q:continue
            count+=1
            g=(x,y);assert power(g,90)==(1,0)
            a,b=lift[power(g,30)] # tau(g)^(-1), tau(g)=g^60
            sign=pow(y,44,q);assert sign in (1,q-1)
            sign=1 if sign==1 else -1
            sa+=sign*a;sb+=sign*b
    assert count==88 and sb==0 and sa%2==0
    c=sa//2
    return {"q":q,"tau_exponent":60,"C":c,
            "f0":"sqrt(89)-C","norm_squared":"45*(89-C*sqrt(89))"}
def main():
    assert len(SOURCE_ASC)==29 and SOURCE_ASC[-1]==1
    common=pm([Q(1),Q(1)],[Q(16),Q(-4),Q(7)])
    quotient,remainder=pdiv(SOURCE_ASC,common)
    assert not remainder and len(quotient)==26
    # R473(12): native W fails both the a-valuation and infinity caps.
    assert (89+67)//68==2 and (11*89)//34==28
    assert SOURCE_ASC[0] and len(SOURCE_ASC)==29
    # S has a once and angular degree5.  Multiplying the same W by S
    # yields a twice, degree34, hence B106. This is not a new central zero.
    assert (106+67)//68==2 and (11*106)//34==34
    s34=[Q(-128,7),Q(-80,7),Q(-12,7),Q(-53,7),Q(1)]
    quotient_s,remainder_s=pdiv(SOURCE_ASC,s34)
    jets,b4,b5=source_jets()
    assert b5
    out={"status":"PASS",
      "source_certificate":{"run":45764784007,"job":139722963336,
         "commit":"ab5d8cefd5ccfc294ebf85408e539a4565b3362f",
         "matrix_sha256":"6ee0222d90db6add172d6d6e650a2f8186b1776072661594a242b4e65c78d665"},
      "source_origin_order":6,"source_charge":89,
      "source_fixed_denominator":91,
      "common_angular_factor":"t*(t-1)*(7+4*t+16*t*t)",
      "angular_quotient_degree":25,
      "member_of_original_normalization_B89":False,
      "B89_obstruction":{"required_a_multiplicity":2,"actual_t0_multiplicity":1,
                          "maximum_angular_degree":28,"actual_angular_degree":29},
      "S34_times_W178_member_of_B106":True,
      "S34_times_W178_angular_degree":34,
      "old_conductor_return_weight":11086,
      "divisible_by_original_S34":not remainder_s,
      "S34_quotient_degree_X":None if remainder_s else len(quotient_s)-1,
      "low_five_w_coefficients":{name:[str(x) for x in jet] for name,jet in jets},
      "B4_determinant":str(b4),"B5_determinant":str(b5),
      "finite_89_norm":local_norm(),
      "polynomial_X_ascending_sha256":hashlib.sha256(json.dumps([str(x) for x in SOURCE_ASC],separators=(",",":")).encode()).hexdigest(),
      "producer_sha256":hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
      "full_cm_dependency_sha256":hashlib.sha256(_producer.read_bytes()).hexdigest(),
      "output_files":False,
      "scope":"Exact actual fifth low-jet independence, native B89 failure and paid S*W return to B106, not a global deep kernel or an infinite-prime nonvanishing proof."}
    print(json.dumps(out,separators=(",",":")))
if __name__=="__main__":main()
