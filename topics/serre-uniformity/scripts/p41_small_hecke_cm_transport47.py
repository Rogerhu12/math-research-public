#!/usr/bin/env python3
"""Exact small-Hecke coordinates and a torsion annihilator for the actual CM classes.

This produces actual endomorphism relations after multiplication by 16 and a
47-unit denominator. It does not construct their principal rational functions.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
import math
from pathlib import Path
import sys


def bareiss(a):
    a=[row[:] for row in a];n=len(a);previous=1;sign=1
    if n==1:return a[0][0]
    for k in range(n-1):
        pivot=next((i for i in range(k,n) if a[i][k]),None)
        if pivot is None:return 0
        if pivot!=k:a[k],a[pivot]=a[pivot],a[k];sign=-sign
        v=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                value=a[i][j]*v-a[i][k]*a[k][j]
                assert value%previous==0
                a[i][j]=value//previous
            a[i][k]=0
        previous=v
    return sign*a[-1][-1]


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--script-dir',type=Path,default=Path(__file__).resolve().parent)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args();folder=args.script_dir.resolve();sys.path.insert(0,str(folder))
    from p41_cm_height_calibration47 import invert
    from sympy import Matrix,Rational,Poly,resultant,symbols,ilcm
    names=['p41_full_chow_heegner_certificate.json.gz','p41_jacobi_cm_certificate.json']
    raw=[(folder/'data'/name).read_bytes() for name in names]
    full,jacobi=[json.loads(gzip.decompress(b) if name.endswith('.gz') else b) for name,b in zip(names,raw)]
    assert full['jacobi_reference_sha256']==hashlib.sha256(raw[1]).hexdigest()
    indices=full['indices'];size=54;rows=[[] for _ in range(size)]
    targets={'x12':[],'x7':[]}
    for n in indices[1:]:targets['kappa_'+str(n)]=[]
    for n in indices[1:]:targets['D12_'+str(n)]=[]
    targets['D7_2']=[]
    field_norms={3:[],5:[]};X=symbols('X');dimensions=[]
    for field,jf in zip(full['fields'],jacobi['fields']):
        factor=field['factor_descending'];assert factor==jf['factor_descending']
        f=factor[::-1];degree=len(f)-1;dimensions.append(degree)
        def val(pair):
            a=[F(x,pair[0]) for x in pair[1][::-1]]
            return a+[F(0)]*(degree-len(a))
        def mul(a,b):
            c=[F(0)]*(2*degree-1)
            for i,x in enumerate(a):
                for j,y in enumerate(b):c[i+j]+=x*y
            while len(c)>degree:
                lead=c[-1];offset=len(c)-degree-1
                for i,x in enumerate(f):c[offset+i]-=lead*x
                c.pop()
            return c
        r3=val([jf['r3_denominator'],jf['r3_numerator_descending']])
        r7=val([jf['r7_denominator'],jf['r7_numerator_descending']])
        t2=val(field['directions'][0][0]);r12=[x/3 for x in mul(t2,r3)]
        x12=[(x-y)/20 for x,y in zip(r12,r3)]
        x7=[(x-y)/20 for x,y in zip(r7,r3)]
        rows[0]+=[F(1)]+[F(0)]*(degree-1)
        targets['x12']+=x12;targets['x7']+=x7
        for k,(direction,meta) in enumerate(zip(field['directions'],full['row_metadata']),1):
            n=indices[k];assert n==meta['n']
            T=val(direction[0]);rows[k]+=T
            Fn=[meta['F_Tn_coefficient']*v for v in T];Fn[0]+=meta['F_identity_coefficient']
            xi=val(direction[2]);Fr3=mul(Fn,r3)
            kappa=[(v/2-2*w)/20 for v,w in zip(xi,Fr3)]
            targets['kappa_'+str(n)]+=kappa
            targets['D12_'+str(n)]+=[v-w for v,w in zip(mul(Fn,x12),kappa)]
            if n==2:targets['D7_2']+=[v-w for v,w in zip(mul(Fn,x7),kappa)]
        for q in field_norms:
            aq=val(field['directions'][indices.index(q)-1][0])
            columns=[]
            for j in range(degree):
                basis=[F(int(i==j)) for i in range(degree)]
                product=mul(aq,basis)
                columns.append([(q+1)*basis[i]-product[i] for i in range(degree)])
            denominator=math.lcm(*[v.denominator for col in columns for v in col])
            integral=[[int(columns[j][i]*denominator) for j in range(degree)] for i in range(degree)]
            determinant=bareiss(integral);scale=denominator**degree
            assert determinant%scale==0
            norm=determinant//scale
            ff=Poly.from_list(factor,gens=X)
            aa=sum(Rational(v.numerator,v.denominator)*X**i for i,v in enumerate(aq))
            assert norm==resultant(ff.as_expr(),q+1-aa,X)
            field_norms[q].append(norm)
    assert sum(dimensions)==size and all(len(v)==size for v in rows+list(targets.values()))
    Q=47**4
    basis_mod=[[v.numerator*pow(v.denominator,-1,Q)%Q for v in row] for row in rows]
    inverse,det=invert(basis_mod,Q);assert det%47==1
    basis=Matrix([[Rational(v.numerator,v.denominator) for v in row] for row in rows])
    target_names=list(targets)
    target_matrix=Matrix.hstack(*[Matrix([Rational(v.numerator,v.denominator) for v in targets[name]]) for name in target_names])
    coefficients=basis.T.inv()*target_matrix
    assert basis.T*coefficients==target_matrix
    expressions={};common=1
    for j,name in enumerate(target_names):
        col=list(coefficients[:,j]);den=int(ilcm(*[v.q for v in col]));nums=[int(v*den) for v in col]
        assert den%47
        expressions[name]={'denominator':den,'numerators':nums}
        common=math.lcm(common,den)
    orders={q:math.prod(norms) for q,norms in field_norms.items()}
    torsion_bound=math.gcd(*orders.values());assert torsion_bound==16
    result={'level':41,'dimension':size,'auxiliary_prime':47,'precision':4,
      'source_sha256':{name:hashlib.sha256(b).hexdigest() for name,b in zip(names,raw)},
      'field_degrees':dimensions,'indices':indices,
      'basis_convention':'rows T_n; columns ascending powers of H=T2+2T3 in the eight R89 fields',
      'basis_matrix_mod47_4':basis_mod,'inverse_basis_matrix_mod47_4':inverse,
      'basis_determinant_mod47_4':det,'basis_determinant_mod47':det%47,
      'coordinates':expressions,'common_denominator':common,
      'actual_point_multiplier':16*common,'torsion_annihilator':16,
      'finite_field_orders':orders,'finite_field_orders_by_factor':field_norms,
      'independent_order_check':'integer Bareiss multiplication determinants and rational polynomial resultants agree',
      'point_conventions':{'x12':'(T2*r3/3-r3)/20','x7':'(r7-r3)/20',
        'kappa_n':'(xi_(2F_n)/2-2*F_n*r3)/20',
        'D12_n':'F_n*x12-kappa_n','D7_2':'F2*x7-kappa2'},
      'equality':'e*C = sum_n (e*coordinate_n) T_n(B_minus4) in J(Q), e=16*common_denominator',
      'status':'exact all109 CM/translation coordinates and torsion removal PASS; principal functions not yet constructed',
      'generating_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    encoded=(json.dumps(result,sort_keys=True,separators=(',',':'))+'\n').encode()
    packed=gzip.compress(encoded,mtime=0)
    output=args.output or folder/'data'/'p41_small_hecke_cm_transport47_certificate.json.gz'
    output.write_bytes(packed)
    print('EXACT SMALL HECKE TRANSPORT PASS',len(expressions),'vectors',flush=True)
    print('basis det mod47',det%47,'torsion annihilator',torsion_bound,'common denominator',common,flush=True)
    print('saved',output,len(packed),'SHA256',hashlib.sha256(packed).hexdigest(),flush=True)


if __name__=='__main__':main()
