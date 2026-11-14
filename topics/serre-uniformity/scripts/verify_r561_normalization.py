#!/usr/bin/env python3
"""Independent small R561 marking/normalization check.

The large Robert product is not recomputed here.  The independent field gate
is a direct Rabin irreducibility check of the recovered degree-43 polynomial.
The remaining checks use the original input and finite coefficient algebra.
"""
import argparse
import hashlib
import json
from pathlib import Path
from flint import fmpz_mod_poly_ctx, fq_default_ctx


def mul(z,w,m):
    return ((z[0]*w[0]-z[1]*w[1])%m,(z[0]*w[1]+z[1]*w[0])%m)


def add(z,w,m):
    return ((z[0]+w[0])%m,(z[1]+w[1])%m)


def sm(z,n,m):
    return (z[0]*n%m,z[1]*n%m)


def power(z,n,m):
    r=(1,0)
    while n:
        if n&1:r=mul(r,z,m)
        z=mul(z,z,m); n>>=1
    return r


def inverse(z,m):
    norm=(z[0]*z[0]+z[1]*z[1])%m
    return sm((z[0],-z[1]),pow(norm,-1,m),m)


def main():
    p=argparse.ArgumentParser()
    p.add_argument('scalar_certificate',type=Path)
    p.add_argument('r198_input',type=Path)
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args()
    sc=json.loads(a.scalar_certificate.read_text())
    old=json.loads(a.r198_input.read_text())
    q=int(sc['q']); assert q==int(old['q']) and sc['status']=='PASS'
    assert hashlib.sha256(a.r198_input.read_bytes()).hexdigest()==sc['input_sha256']
    assert len(sc['rows'])==44 and [x['index'] for x in sc['rows']]==list(range(44))
    assert all(x['base_u0']==x['norm_S'] and x['norm_ratio']=='1' for x in sc['rows'])
    pc=fmpz_mod_poly_ctx(q)
    f=pc([int(c) for c in sc['f43']])
    assert f.degree()==43 and f.is_monic() and f.is_irreducible()
    print('Independent degree-43 Rabin irreducibility: PASS',flush=True)
    # Embed the original Weil root through the recorded algebraic i.
    f86=pc([int(c) for c in sc['f86']])
    F=fq_default_ctx(modulus=f86,check_prime=False,check_modulus=False)
    ii=F([int(c) for c in sc['i_in_f86']]); assert ii*ii==-1
    za,zb=map(int,old['zeta_Weil']); zeta=za+zb*ii
    assert zeta**43==1 and zeta!=1
    for n,v in zip(sc['high_projection_logs'],sc['high_projection_powers']):
        assert zeta**n==F([int(c) for c in v])
    assert sc['high_projection_logs']==[9,0]
    assert ((q*q-1)//43)%43==21
    assert ((q**86-1)//1849)%43==21
    assert ((-q-1)//43)%43==32 and 32*39%43==1
    assert pow(5,43,1849)==sc['closure_Q_multiplier']==1639
    assert sc['s_on_mu_p2']==87
    omega=(8,25); omegahat=(352,197)
    assert power(omegahat,44,1849)==(1,0)
    assert power(omegahat,11,1849)==(0,1)
    coeff=[]; w=(1,0)
    for j in range(44):
        v=15*w[0]%43
        coeff.append(v if v<=21 else v-43)
        w=mul(w,omega,43)
    wi=inverse(omega,43); w=(1,0); kval=(0,0)
    for n in coeff:
        kval=add(kval,sm(w,n,43),43);w=mul(w,wi,43)
    assert kval==(29,0)
    aval=(0,15*pow(7,-1,43)%43)
    y_scale=mul(aval,inverse(kval,43),43)
    assert y_scale==(0,31)
    # The direct mu_p exponent of scalar u_s is -2 times its high log.
    r_us=-2*9%43; assert r_us==25
    rows=[]
    for L in range(43):
        sumY=(L+3)*pow(19,-1,43)%43
        ell_y=mul(y_scale,(0,2*sumY%43),43)
        assert ell_y==((40-L)%43,0)
        r_y=-2*ell_y[0]%43
        assert r_y==(2*L+6)%43
        r_h=(r_us-r_y)*pow(2,-1,43)%43
        ell_h=21*r_h%43
        assert ell_h==(r_y-25)*pow(4,-1,43)%43
        C=(0,-ell_h*pow(32,-1,43)%43)
        assert C==(0,(r_y-25)%43)
        translated=add((31,0),mul((0,-22),C,43),43)
        assert translated==(L,0)
        assert (L==10)==(C==(0,1))
        assert (L==40)==(C==(0,18))
        rows.append({'L':L,'r_y':r_y,'ell_y':ell_y[0],'r_h':r_h,'ell_h':ell_h,'C':list(C)})
    result={'status':'PASS','independent_degree_43_irreducibility':True,
      'original_input_sha256':sc['input_sha256'],'scalar_certificate_sha256':hashlib.sha256(a.scalar_certificate.read_bytes()).hexdigest(),
      'original_Weil_root_and_stored_high_outputs_checked':True,
      'large_Robert_products_recomputed':False,'high_power_exponent_recomputed':False,
      'Pi_coefficients':coeff,'k_mod_p':list(kval),'a_over_k_mod_p':list(y_scale),
      'mu_p_index_to_power_log':21,'power_log_to_mu_p_index':41,
      'scalar_unit_high_log':9,'scalar_unit_direct_mu_p_index':25,
      'all_43_normalization_rows':rows,'actual_C_computed':False,'actual_L_computed':False,
      'old_b_lambda_34_bridge_recovered':False}
    a.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','independent_degree_43_irreducibility','scalar_unit_high_log','scalar_unit_direct_mu_p_index','actual_C_computed','actual_L_computed']}),flush=True)


if __name__=='__main__':
    main()
