#!/usr/bin/env python3
"""Independent FLINT/Python verification of actual formal discs from selected global quadrics."""
import argparse,gzip,hashlib,json,sys
from pathlib import Path

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--script-dir',type=Path,required=True)
    p.add_argument('--input',type=Path,default=Path('/tmp/p41_cm_quadratic_jets47_raw.json.gz'))
    p.add_argument('--output',type=Path,default=Path('/tmp/p41_cm_quadratic_jets47_independent.json'))
    args=p.parse_args();sys.path.insert(0,str(args.script_dir.resolve()))
    import p41_r2_matrix as r
    from p41_group_operations47 import load_sources,make_model
    from p41_cm4_divisor47 import kernel
    from flint import nmod_mat
    raw=args.input.read_bytes();data=json.loads(gzip.decompress(raw));sources,hashes=load_sources(args.script_dir/'data')
    assert data['source_sha256']==hashes;M=make_model(sources);q=47**4;order=data['order'];d=sources[1]
    K=r.from_json(kernel(73,d['cusp_rank_columns_1based'],d['cusp_free_columns_1based'],d['canonical_kernel_block']))
    fc=r.to_json(r.mm(K,r.column(d['canonical_coefficients'])));fc=[x[0] for x in fc]
    sq=[(a-1,b-1) for a,b in d['square_basis_monomials_1based']]
    fm=lambda A:(nmod_mat(A[0].tolist(),q),nmod_mat(A[1].tolist(),q))
    S=fm(r.from_json(d['square_basis_inverse']));VM=fm(M['V2'])
    def add(x,y):return [(x[0]+y[0])%q,(x[1]+y[1])%q]
    def sub(x,y):return [(x[0]-y[0])%q,(x[1]-y[1])%q]
    def mul(x,y):return [(x[0]*y[0]-x[1]*y[1])%q,(x[0]*y[1]+x[1]*y[0])%q]
    def dot(a,b):
        x=[0,0]
        for v,w in zip(a,b):x=add(x,mul(v,w))
        return x
    def fmm(A,B):return A[0]*B[0]-A[1]*B[1],A[0]*B[1]+A[1]*B[0]
    cert=[]
    for rec in data['records']:
        x=rec['normalized_weight2_coefficients'];uc=[v[0] for v in rec['parameter_coefficients']]
        assert len(x)==order+1
        assert hashlib.sha256(json.dumps(x,separators=(',',':')).encode()).hexdigest()==rec['jets_sha256']
        pairs=[(a-1,b-1) for a,b in rec['selected_quadric_pairs_1based']];assert len(pairs)==71
        C0=[];C1=[]
        for row in M['P2']:
            pairs_at_row=[mul([int(M['W'][0][row,a]),int(M['W'][1][row,a])],
                              [int(M['W'][0][row,b]),int(M['W'][1][row,b])]) for a,b in pairs]
            C0.append([v[0] for v in pairs_at_row]);C1.append([v[1] for v in pairs_at_row])
        C=(nmod_mat(C0,q),nmod_mat(C1,q));globalvalues=fmm(VM,C)
        for row in range(820):
            for j,(a,b) in enumerate(pairs):
                actual=mul([int(M['W'][0][row,a]),int(M['W'][1][row,a])],
                           [int(M['W'][0][row,b]),int(M['W'][1][row,b])])
                assert actual==[int(globalvalues[0][row,j]),int(globalvalues[1][row,j])]
        HH=fmm(S,C);H=[[[int(HH[0][k,j]),int(HH[1][k,j])] for k in range(199)] for j in range(71)]
        selected_monomial_jets=[]
        for k in range(order+1):
            row=[]
            for a,b in sq:
                total=[0,0]
                for i in range(k+1):total=add(total,mul(x[i][a],x[k-i][b]))
                row.append(total)
            selected_monomial_jets.append(row)
        for k in range(order+1):
            assert dot(fc,x[k])==([1,0] if k==0 else [0,0])
            if k:assert dot(uc,x[k])==([1,0] if k==1 else [0,0])
            for j,(a,b) in enumerate(pairs):
                actual=[0,0]
                for i in range(k+1):actual=add(actual,mul(x[i][a],x[k-i][b]))
                assert actual==dot(H[j],selected_monomial_jets[k])
        J=[]
        for j,(a,b) in enumerate(pairs):
            row=[[0,0] for _ in range(73)];row[a]=add(row[a],x[0][b]);row[b]=add(row[b],x[0][a])
            for h,(c,e) in zip(H[j],sq):
                row[c]=sub(row[c],mul(h,x[0][e]));row[e]=sub(row[e],mul(h,x[0][c]))
            J.append(row)
        J += [fc,uc]
        block=[]
        for row in J:block.append([a%47 for a,b in row]+[(-b)%47 for a,b in row])
        for row in J:block.append([b%47 for a,b in row]+[a%47 for a,b in row])
        det=int(nmod_mat(block,47).det());a,b=rec['unit_jacobian_determinant']
        assert det!=0 and det==(a*a+b*b)%47
        cert.append({'label':rec['label'],'norm_of_unit_jacobian_mod47':det,'order':order,
                     'global_quadrics_checked_on_all820_points':71,'all_selected_quadric_jets':True})
        print('INDEPENDENT ACTUAL DISC PASS',rec['label'],flush=True)
    result={'status':'PASS','source_sha256':hashes,'input_sha256':hashlib.sha256(raw).hexdigest(),
            'verifier_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'arithmetic':'FLINT exact modular matrices plus Python integer formal-polynomial products; no NumPy jet solver used',
            'records':cert}
    args.output.write_text(json.dumps(result,sort_keys=True,separators=(',',':'))+'\n')
    print('ALL INDEPENDENT ACTUAL DISCS PASS',len(cert),'sha',hashlib.sha256(args.output.read_bytes()).hexdigest(),flush=True)

if __name__=='__main__':main()
