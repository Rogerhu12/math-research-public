#!/usr/bin/env python3
"""Actual CM height-difference calibration, without absolute section constants.

First53 rows use j=54000 minus j=0.  The last uses j=-3375 minus j=0
in F=27*T2+4.  It computes no local-height right hand side.
"""
import argparse,gzip,hashlib,json
from pathlib import Path
from p41_cm_height_calibration47 import invert,matmul

Q=47**4

def build(full,jacobi,absolute,bad):
    V=[[] for _ in range(54)];r12s=[]
    for field,jf in zip(full['fields'],jacobi['fields']):
        assert field['factor_descending']==jf['factor_descending']
        f=[a%Q for a in field['factor_descending'][::-1]];n=len(f)-1
        def val(pair):return [a*pow(pair[0],-1,Q)%Q for a in pair[1][::-1]]
        def add(a,b):return [((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0))%Q for i in range(max(len(a),len(b)))]
        def scale(a,s):return [x*s%Q for x in a]
        def mul(a,b):
            out=[0]*(len(a)+len(b)-1)
            for i,x in enumerate(a):
                for j,y in enumerate(b):out[i+j]=(out[i+j]+x*y)%Q
            while len(out)>n:
                c=out.pop();k=len(out)-n
                for j in range(n):out[k+j]=(out[k+j]-c*f[j])%Q
            return out+[0]*(n-len(out))
        r3=val([jf['r3_denominator'],jf['r3_numerator_descending']])
        r7=val([jf['r7_denominator'],jf['r7_numerator_descending']])
        t2=val(field['directions'][0][0]);r12=scale(mul(t2,r3),pow(3,-1,Q));r12s.append(r12)
        for k,(dd,meta) in enumerate(zip(field['directions'],full['row_metadata'])):
            T=val(dd[0]);xi=val(dd[2]);F=add(scale(T,meta['F_Tn_coefficient']),[meta['F_identity_coefficient']])
            assert meta['G_multiplier']==2
            def v(r):return add(scale(mul(F,mul(r,r)),2),scale(mul(r,xi),-1))
            V[k]+=add(v(r12),scale(v(r3),-1))
            if k==0:
                assert meta['n']==2;V[53]+=add(v(r7),scale(v(r3),-1))
    assert len(V)==54 and all(len(row)==54 for row in V)
    G=absolute['trace_gram'];M=matmul(V,G,Q)
    _,dv=invert(V,Q);MI,dm=invert(M,Q)
    assert (dv%47,dm%47)==(4,43)
    assert [x['n'] for x in full['row_metadata']]==[x['n'] for x in bad['directions']]
    assert bad['component_labels']==[0,3,28,32]
    bad_rows=[x['bad_values'][1] for x in bad['directions']]+[bad['directions'][0]['bad_values'][2]]
    assert bad_rows[-1]==0
    return V,G,M,MI,r12s,bad_rows,{'class_difference_matrix':dv%47,'trace_gram':46,'height_coefficient_matrix':dm%47}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--script-dir',type=Path,default=Path(__file__).resolve().parent);p.add_argument('--output',type=Path);args=p.parse_args();root=args.script_dir/'data'
    names=['p41_full_chow_heegner_certificate.json.gz','p41_jacobi_cm_certificate.json','p41_cm_height_calibration47_certificate.json.gz','p41_all_bad_heights_certificate.json']
    raw=[(root/n).read_bytes() for n in names];objs=[json.loads(gzip.decompress(b) if n.endswith('.gz') else b) for n,b in zip(names,raw)]
    V,G,M,MI,r12s,bad,dets=build(*objs)
    out={'level':41,'auxiliary_prime':47,'precision':4,'modulus':Q,
         'source_sha256':{n:hashlib.sha256(b).hexdigest() for n,b in zip(names,raw)},
         'coordinate_basis':'ascending powers of H in the eight R89 fields, in published order',
         'actual_CM_relation':'T2(P_minus3)=3*P_minus12, j(P_minus12)=54000; r_minus12=T2*r_minus3/3',
         'r_minus12_field_coefficients_ascending':r12s,
         'rows':[{'CM_discriminant':-12,'anchor_discriminant':-3,'n':n,'bad_component':3} for n in objs[0]['indices'][1:]]+[{'CM_discriminant':-7,'anchor_discriminant':-3,'n':2,'bad_component':28}],
         'vector_formula':'2*F_n*(r_delta^2-r_minus3^2)-(r_delta-r_minus3)*xi_(2F_n)',
         'CM_class_difference_matrix':V,'trace_gram':G,'height_coefficient_matrix':M,'inverse_height_coefficient_matrix':MI,
         'bad_height_differences':bad,'determinants_mod47':dets,
         'right_hand_side':'lambda47(t_n(P_delta))-lambda47(t_n(P_minus3))-log47(41)*bad_height_differences[row]',
         'section_requirement':'t_n is an actual algebraic nowhere-vanishing section of the full pullback line bundle on the entire X over Q47, or the corresponding fixed rational-power construction; an arbitrary analytic disk frame is insufficient',
         'status':'Exact invertible relative CM calibration. Actual algebraic section ratios and local-height values remain to be computed.'}
    packed=gzip.compress((json.dumps(out,sort_keys=True,separators=(',',':'))+'\n').encode(),mtime=0)
    target=args.output or root/'p41_cm_relative_calibration47_certificate.json.gz';target.write_bytes(packed)
    print('All54 actual CM height-difference rows and two-sided inverse PASS.',flush=True)
    print('Determinants mod47',dets,flush=True)
    print(target,len(packed),'SHA256',hashlib.sha256(packed).hexdigest(),flush=True)
if __name__=='__main__':main()
