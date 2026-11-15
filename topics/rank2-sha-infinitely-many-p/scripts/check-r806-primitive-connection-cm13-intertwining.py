#!/usr/bin/env python3
"""Exact R806/R807 connection between the actual type-five primitive and type-four blocks.

Public execution only. Rebuilds the two CM13 operators from the original full
division/trace algorithm and the canonical halfperiod from all E[2] terms.
No saved output tables, auxiliary finite-field samples, or negative-moment
nonvanishing assertions are used.
Usage: python3 scripts/check-r806-primitive-connection-cm13-intertwining.py --workers=4
Dependencies: python-flint==0.9.0. Writes no output files.
"""
from __future__ import annotations
import concurrent.futures, hashlib, importlib.util, json, pathlib, sys
HERE=pathlib.Path(__file__).resolve().parent
HP=HERE/"check-r798-type-four-halfperiod-and-cm13.py"
spec=importlib.util.spec_from_file_location("r806_hp",HP)
hp=importlib.util.module_from_spec(spec);sys.modules[spec.name]=hp
spec.loader.exec_module(hp)
for name in ("Q","Z","O","W","K","add","sub","mul","neg","div","inv","power",
             "scale","sumk","rref","mm","ma","ms","eye","mpow","enc"):
    globals()[name]=getattr(hp,name)

def rank(A):return len(rref(A)[1])
def encode(A):return [[enc(x) for x in row] for row in A]
def coord(B,A):
    columns=[]
    for col in zip(*A):
        _,piv,v=rref(B,list(col))
        assert len(piv)==len(B[0])
        columns.append(v)
    X=[list(r) for r in zip(*columns)]
    assert mm(B,X)==A
    return X
def det3(A):
    return sumk([
      mul(A[0][0],sub(mul(A[1][1],A[2][2]),mul(A[1][2],A[2][1]))),
      neg(mul(A[0][1],sub(mul(A[1][0],A[2][2]),mul(A[1][2],A[2][0])))),
      mul(A[0][2],sub(mul(A[1][0],A[2][1]),mul(A[1][1],A[2][0])))
    ])
def main():
    with concurrent.futures.ProcessPoolExecutor(max_workers=hp.core.ARGS.workers) as ex:
        rows=dict(ex.map(hp.fiber,range(2,10)))
    A4=hp.operator(rows,"type4",[3*j for j in range(6)],range(2,8),(8,9))
    A5=hp.operator(rows,"type5",[1+3*j for j in range(5)],range(2,7),(7,8,9))
    I3=eye(3)
    PP=ma(eye(5),ms(hp.PB5,neg(O)))
    B4,R4,piv4=hp.restriction(A4,hp.PB4)
    B5,R5,piv5=hp.restriction(A5,PP)
    assert len(piv4)==len(piv5)==3
    assert mpow(R4,3)==ms(I3,neg(W))
    assert mpow(R5,3)==ms(I3,neg(W))
    C=[[Z]*5 for _ in range(6)]
    for j in range(5):
        C[j][j]=K(-6*j-2);C[j+1][j]=K(-6*j-5)
    J=coord(B4,mm(mm(hp.PB4,C),B5))
    assert rank(J)==3
    comm=ma(mm(R4,J),ms(mm(J,R5),neg(O)))
    R5inv=ms(mpow(R5,2),inv(neg(W)))
    assert mm(R5,R5inv)==I3
    components=[]
    total=ms(I3,Z)
    for r in range(3):
        Jr=ms(I3,Z)
        for k in range(3):
            term=mm(mm(mpow(R4,k),J),mpow(R5inv,k))
            Jr=ma(Jr,ms(term,div(power(W,(-r*k)%3),K(3))))
        assert mm(R4,Jr)==ms(mm(Jr,R5),power(W,r))
        total=ma(total,Jr)
        components.append({
          "ratio_power":r,"matrix":encode(Jr),"rank":rank(Jr),
          "determinant":enc(det3(Jr)),
          "old_to_new_labels":[[j,(j+3+12*r)%18] for j in (1,7,13)]})
    assert total==J
    result={
      "format":"R806 exact primitive-to-type-four projected connection",
      "status":"PASS","field":"Q(omega), omega^2+omega+1=0",
      "type4_basis":"b^(5-j)*sigma_b^34*x_b^(3j), j=0..5",
      "type5_basis":"-b^(4-j)*sigma_b^34*x_b^(1+3j)*y_b, j=0..4",
      "B4_columns":piv4,"primitive5_columns":piv5,
      "B4_basis":encode(B4),"primitive5_basis":encode(B5),
      "B4_CM13":encode(R4),"primitive5_CM13":encode(R5),
      "projected_connection":encode(J),
      "projected_connection_determinant":enc(det3(J)),
      "CM13_commutator":encode(comm),"CM13_commutator_rank":rank(comm),
      "is_exact_CM13_intertwiner":comm==ms(I3,Z),
      "three_character_ratio_components":components,
      "all_components_sum_to_actual_connection":True,
      "full_fibers":list(range(2,10)),
      "input_sha256":{x.name:hashlib.sha256(x.read_bytes()).hexdigest()
        for x in (HP,hp.path)},
      "scope":"Full characteristic-zero source and operator identities only. The old primitive characters have order 9, the new type-four characters have order 18. Keep every canonical halfperiod connection term and the original negative-two/unit/cut observations; no elliptic-logarithm or central nonvanishing is inferred.",
      "outputs_persisted":False
    }
    text=json.dumps(result,separators=(",",":"))
    if len(text.encode())>59000:raise RuntimeError("Report budget exceeded")
    print(text)
if __name__=="__main__":main()
