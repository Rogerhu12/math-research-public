#!/usr/bin/env python3
"""Exact CM calibration matrix for all layer41 global height coefficients.

Uses actual R89 point classes and R94 translations.  It does not compute the
54 local-height right hand sides and makes no quadratic-Chabauty root claim.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path

P=47
Q=P**4


def matmul(A,B,q):
    return [[sum(a*b for a,b in zip(row,col))%q for col in zip(*B)] for row in A]


def identity(n):return [[int(i==j) for j in range(n)] for i in range(n)]


def invert(A,q):
    n=len(A);a=[list(row)+eye for row,eye in zip(A,identity(n))];det=1
    for c in range(n):
        pivot=next((i for i in range(c,n) if a[i][c]%P),None)
        assert pivot is not None,('nonunit matrix',c)
        if pivot!=c:a[c],a[pivot]=a[pivot],a[c];det=-det
        v=a[c][c];det=det*v%q;iv=pow(v,-1,q);a[c]=[x*iv%q for x in a[c]]
        for i in range(n):
            if i!=c:
                v=a[i][c];a[i]=[(x-v*y)%q for x,y in zip(a[i],a[c])]
    assert [row[:n] for row in a]==identity(n)
    inv=[row[n:] for row in a]
    assert matmul(A,inv,q)==identity(n) and matmul(inv,A,q)==identity(n)
    return inv,det%q


def power_traces(f):
    n=len(f)-1;out=[n]
    for k in range(1,2*n-1):
        v=sum(f[j]*out[k-j] for j in range(1,min(k-1,n)+1))
        if k<=n:v+=k*f[k]
        out.append(-v)
    return out


def build(full,jacobi):
    rows=[[] for _ in range(54)];gram=[[0]*54 for _ in range(54)];offset=0;field_dets=[]
    assert full['indices'][1:]==[m['n'] for m in full['row_metadata']]
    for field,jf in zip(full['fields'],jacobi['fields']):
        assert field['factor_descending']==jf['factor_descending']
        f=[x%Q for x in field['factor_descending'][::-1]];n=len(f)-1
        def val(pair):return [a*pow(pair[0],-1,Q)%Q for a in pair[1][::-1]]
        def add(a,b):return [((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0))%Q for i in range(max(len(a),len(b)))]
        def scale(a,v):return [x*v%Q for x in a]
        def mul(a,b):
            out=[0]*(len(a)+len(b)-1)
            for i,x in enumerate(a):
                for j,y in enumerate(b):out[i+j]=(out[i+j]+x*y)%Q
            while len(out)>n:
                v=out[-1];k=len(out)-len(f)
                for i,x in enumerate(f):out[k+i]=(out[k+i]-v*x)%Q
                out.pop()
            return out+[0]*(n-len(out))
        r3=val([jf['r3_denominator'],jf['r3_numerator_descending']])
        r7=val([jf['r7_denominator'],jf['r7_numerator_descending']])
        for k,(direction,meta) in enumerate(zip(field['directions'],full['row_metadata'])):
            T=val(direction[0]);xi=val(direction[2])
            F=add(scale(T,meta['F_Tn_coefficient']),[meta['F_identity_coefficient']])
            assert meta['G_multiplier']==2
            def v(r):return add(scale(mul(F,mul(r,r)),2),scale(mul(r,xi),-1))
            rows[k].extend(v(r3))
            if k==0:rows[53].extend(v(r7));assert meta['n']==2
        traces=power_traces(field['factor_descending'])
        block=[[traces[i+j]%Q for j in range(n)] for i in range(n)]
        _,det=invert(block,Q);field_dets.append(det%P)
        for i in range(n):gram[offset+i][offset:offset+n]=block[i]
        offset+=n
    assert offset==54 and all(len(row)==54 for row in rows)
    _,dv=invert(rows,Q);_,dg=invert(gram,Q)
    matrix=matmul(rows,gram,Q);inverse,dm=invert(matrix,Q)
    assert dm==dv*dg%Q
    return rows,gram,matrix,inverse,{'class_vector_matrix':dv%P,'trace_gram':dg%P,'height_coefficient_matrix':dm%P,'field_trace_grams':field_dets}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--script-dir',type=Path,default=Path(__file__).resolve().parent)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args();folder=args.script_dir.resolve();names=['p41_full_chow_heegner_certificate.json.gz','p41_jacobi_cm_certificate.json']
    raw=[(folder/'data'/n).read_bytes() for n in names]
    full,jacobi=[json.loads(gzip.decompress(b) if n.endswith('.gz') else b) for n,b in zip(names,raw)]
    assert full['jacobi_reference_sha256']==hashlib.sha256(raw[1]).hexdigest()
    V,G,M,I,dets=build(full,jacobi)
    result={'level':41,'auxiliary_prime':P,'precision':4,'modulus':Q,
        'source_sha256':{n:hashlib.sha256(b).hexdigest() for n,b in zip(names,raw)},
        'rows':[{'CM_discriminant':-3,'n':n} for n in full['indices'][1:]]+[{'CM_discriminant':-7,'n':2}],
        'coordinate_basis':'eight R89 fields in order, ascending powers of H=T2+2T3',
        'vector_formula':'2*F_n*r_delta^2-r_delta*xi_(2F_n)',
        'CM_class_vector_matrix':V,'trace_gram':G,'height_coefficient_matrix':M,'inverse_height_coefficient_matrix':I,
        'determinants_mod47':dets,
        'right_hand_side':'the same actual auxiliary local height plus all nonauxiliary local contributions at the specified CM point; identical component labels across directions',
        'unknowns':'s in E tensor Q47, defined by h(a*B_minus4,b*B_minus4)=Tr(s*a*b)',
        'status':'exact invertible CM calibration; actual local-height right hand sides have not been computed'}
    encoded=(json.dumps(result,sort_keys=True,separators=(',',':'))+'\n').encode();packed=gzip.compress(encoded,mtime=0)
    out=args.output or folder/'data'/'p41_cm_height_calibration47_certificate.json.gz';out.write_bytes(packed)
    print('All54 exact CM calibration equations,trace pairing and two-sided inverse PASS.',flush=True)
    print('Determinants mod47:',dets,flush=True)
    print('Saved',out,len(packed),'bytes; SHA256',hashlib.sha256(packed).hexdigest(),flush=True)


if __name__=='__main__':main()
