#!/usr/bin/env python3
"""R807: exact original covariant connection, complete halfperiod image and native obstruction.

Public execution only. Rebuilds the R798 canonical halfperiod matrices from their
actual E[2] formula and its S anchor; no saved output matrix is an input.
The native G2 row is reconstructed by the complete R801/R719 producer.
No negative-moment or original central nonvanishing is inferred.
"""
from __future__ import annotations
import hashlib, importlib.util, json, pathlib, subprocess, sys
HERE=pathlib.Path(__file__).resolve().parent
HP=HERE/"check-r798-type-four-halfperiod-and-cm13.py"
spec=importlib.util.spec_from_file_location("r807_hp",HP)
hp=importlib.util.module_from_spec(spec);sys.modules[spec.name]=hp
spec.loader.exec_module(hp)
for name in ("Q","Z","O","W","K","add","sub","mul","neg","div","scale","sumk",
             "rref","mm","ma","ms","eye","null","enc"):
    globals()[name]=getattr(hp,name)

def tr(A): return [list(r) for r in zip(*A)]
def basis(A):
    _,piv,_=rref(A)
    return [[r[j] for j in piv] for r in A],piv
def rank(A):return len(rref(A)[1])
def coords(B,A):
    cols=[]
    for col in zip(*A):
        _,piv,v=rref(B,list(col));assert len(piv)==len(B[0])
        cols.append(v)
    ans=tr(cols)
    assert mm(B,ans)==A
    return ans
def encode(A):return [[enc(x) for x in r] for r in A]
def frac_mod(x,p):
    return int(x.numerator)%p*pow(int(x.denominator)%p,-1,p)%p
def kmod(x,p,w):return (frac_mod(x[0],p)+w*frac_mod(x[1],p))%p
def matrix_mod(A,p,w):return [[kmod(x,p,w) for x in r] for r in A]
def dotmod(a,b,p):return sum(x*y for x,y in zip(a,b))%p

# The bases are b^(5-j)*sigma^34*x^(3j) and
# -b^(4-j)*sigma^34*x^(1+3j)*y; C therefore works for every b != 0.
C=[[Z]*5 for _ in range(6)]
for j in range(5):
    C[j][j]=K(-6*j-2);C[j+1][j]=K(-6*j-5)
ell=[O]
for j in range(5):ell.append(scale(ell[-1],Q(-6*j-2,6*j+5)))
assert rank(C)==5 and mm([ell],C)==[[Z]*5]
augment=[r+[O if i==0 else Z] for i,r in enumerate(C)]
assert rank(augment)==6
B4,p4=basis(hp.PB4)
B5a,p5a=basis(hp.PB5)
P5p=ma(eye(5),ms(hp.PB5,neg(O)))
B5p,p5p=basis(P5p)
PC=mm(hp.PB4,C)
Ca=mm(PC,B5a);Cp=mm(PC,B5p)
Da=coords(B4,Ca);Dp=coords(B4,Cp)
comm=ma(mm(hp.H4,C),ms(mm(C,hp.H5),neg(O)))
left_a=null(tr(Da))
left_p=null(tr(Dp))
left_phys=[]
for v in left_a:
    _,_,row=rref(tr(B4),v)
    assert mm([row],B4)==[v]
    left_phys.append(row)
lifts={}
for label,B5,im in (("all",eye(5),PC),("arith",B5a,Ca),("primitive",B5p,Cp)):
    if rank(im)==3:
        # rref chooses zero free coordinates: an explicit fixed right inverse.
        cols=[]
        for col in zip(*B4):
            _,_,v=rref(im,list(col));cols.append(v)
        lift=mm(B5,tr(cols))
        assert mm(PC,lift)==B4
        lifts[label]=encode(lift)
# Also resolve the exact unprojected image on the actual B4 carrier.
zero_C_on_B4=null(mm([ell],B4))
exact_in_C=mm(B4,tr(zero_C_on_B4)) if zero_C_on_B4 else [[] for _ in range(6)]
if zero_C_on_B4:
    coords(C,exact_in_C)

READER=HERE/"check-r798-native-second-z-source.js"
args=["--max-block=4","--taus=2","--with-b","--b-g-blocks=3","--neutral-degree=12"]
out=subprocess.run(["node",str(READER),*args],check=True,stdout=subprocess.PIPE)
native=json.loads(out.stdout)
native_rows=[]
for block in native["entries"]:
    for item in block["entries"]:
        aux=item["auxiliary"];p=aux["p"];w=aux["omega"]
        g=list(reversed(item["B0_second_theta"]))
        # Keep the original full source condition, not an arbitrary six-vector.
        PB=matrix_mod(hp.PB4,p,w)
        assert [dotmod(r,g,p) for r in PB]==g
        native_rows.append({
            "auxiliary":aux,"all_original_rows_verified":item["same_qstar"]["all_original_rows_verified"],
            "lambda_de_rham":dotmod([kmod(x,p,w) for x in ell],g,p),
            "arith_image_left_obstructions":[dotmod([kmod(x,p,w) for x in row],g,p) for row in left_phys],
            "same_qstar_actual_J2":item["same_qstar"]["actual_J2"]})
ans={
    "format":"R807 original covariant connection and actual second-source obstruction",
    "status":"PASS","field":"Q(omega), omega^2+omega+1=0",
    "basis4":"b^(5-j)*sigma^34*x^(3j), j=0..5",
    "basis5":"-b^(4-j)*sigma^34*x^(1+3j)*y, j=0..4",
    "canonical_halfperiod_sign":hp.EPS,
    "connection":encode(C),"de_rham_row":[enc(x) for x in ell],
    "de_rham_on_B4":encode(mm([ell],B4)),
    "unprojected_connection_rank":rank(C),
    "B4_rank":len(p4),"B4_pivot_columns":p4,
    "B5_arith_rank":len(p5a),"B5_primitive_rank":len(p5p),
    "projected_connection_rank":rank(PC),
    "projected_arith_rank":rank(Ca),"projected_primitive_rank":rank(Cp),
    "arith_connection_B4_coordinates":encode(Da),
    "primitive_connection_B4_coordinates":encode(Dp),
    "halfperiod_connection_commutator":encode(comm),
    "halfperiod_connection_commutator_rank":rank(comm),
    "arith_image_left_rows_B4":encode(left_a),
    "arith_image_left_rows_physical":encode(left_phys),
    "exact_unprojected_B4_subspace_dimension":len(zero_C_on_B4),
    "exact_unprojected_B4_subspace_basis":encode(exact_in_C),
    "projected_right_inverses_to_B4":lifts,
    "native_rows":native_rows,
    "native_reader_args":args,
    "native_reader_stdout_bytes":len(out.stdout),
    "native_reader_stdout_sha256":hashlib.sha256(out.stdout).hexdigest(),
    "input_sha256":{x.name:hashlib.sha256(x.read_bytes()).hexdigest()
                    for x in (HP,hp.path,READER)},
    "scope":"Exact finite original source identities and actual same-qstar obstruction only. Retain zeta companion and complete halfperiod commutator; no negative-two or central nonvanishing.",
    "outputs_persisted":False}
report=json.dumps(ans,separators=(",",":"))
if len(report.encode())>59000:raise RuntimeError("Report budget exceeded")
print(report)
