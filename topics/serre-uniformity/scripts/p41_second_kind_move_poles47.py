#!/usr/bin/env python3
"""Move the complete second-kind basis away from every supersingular residue disk."""
import argparse,gzip,hashlib,json,random,sys,time
from pathlib import Path

def read(p):
    b=Path(p).read_bytes();return json.loads(gzip.decompress(b) if str(p).endswith('.gz') else b)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--script-dir',type=Path,required=True)
    ap.add_argument('--work-dir',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args();sys.path.insert(0,str(args.script_dir.resolve()))
    args.work_dir.mkdir(parents=True,exist_ok=True)
    import numpy as np
    import p41_r2_matrix as r
    from p41_projective_jet_frames47 import install_exact_float_mm,ProjectiveJetFrames
    install_exact_float_mm(r)
    from p41_native_r2_linear47 import install
    native=install(r,args.work_dir/'native')
    from p41_elliptic_coarse_atlas47 import setup
    from p41_actual_differentials47 import save
    from p41_hecke3_hessian47 import section_jets
    from p41_cm4_divisor47 import kernel as old_kernel
    at=setup(args.script_dir.resolve());a=at.a;M=a.M;scale=a.scale;start=time.monotonic()
    graph=a.read('p41_SS_Hecke_graph47.json.gz')
    coarse=a.read('p41_elliptic_coarse_atlas47_verified.json.gz')
    nu=a.read('p41_second_kind_connection47.json.gz')
    transport=a.read('p41_second_kind_hecke3_transport47.json.gz')
    source=a.read('p41_source_cubic47_full_saved.json.gz')
    bases=a.read('p41_hecke3_abel_bases_checkpoint.json.gz')
    W=[r.from_json(x) for x in source['evaluation_coefficients'][:2]]
    V2,V3=section_jets(W,at.source,M,r)
    I=[i-1 for i in nu['pole_indices_1based']];other=[i for i in range(820) if i not in set(I)]
    raw={str(j):x['W'] for j,x in at.refs.items()}
    for rec in coarse['elliptic_charts']:raw[rec['kind']]=r.from_json(rec['coarse_values'][0])
    WG=r.zeros(3154,73)
    for v in graph['vertices']:
        g=v['vertex_0based'];s=v['chosen_reference'];j=s['input_row_0based']
        for part in range(2):WG[part][g]=raw[s['reference_key']][part][j]
    assert np.all(np.any(r.units(WG),axis=1))
    vertex_of={(m['reference_key'],m['necklace_label_1based']):v['vertex_0based'] for v in graph['vertices'] for m in v['members']}
    Z=[vertex_of[('9',i+1)] for i in I];Zset=set(Z);outsideZ=[i for i in range(3154) if i not in Zset]
    assert len(Zset)==54 and all(graph['frobenius_permutation_0based'][j]!=j for j in Z)
    rng=random.Random(246004147)
    def cusps_unit(c):
        return all(np.any(a.field_rows(np.asarray(a.cusp['cusp_values'][i],dtype=np.int64),c)[0]%47) for i in [0,11])
    for attempt_w in range(1000):
        seed,w=r.rational_trace(M['A1'],rng)
        if np.all(r.units(r.mm(WG,w))) and cusps_unit(w):break
    else:raise AssertionError('No all-SS-unit auxiliary section')
    print('Actual section w avoids all3154 SS points and both cusp fields; attempt',attempt_w+1,flush=True)
    A=r.rows(M['W'],I);rr,cc=r.rank_pivots(A);assert len(rr)==54
    KL,free,block=r.kernel_from_rows(r.rows(A,rr),rr,cc);assert KL[0].shape==(73,19)
    AKL=r.rows(r.mm(M['A1'],r.conjugate(KL)),free)
    assert r.equal(r.mm(KL,AKL),r.mm(M['A1'],r.conjugate(KL)))
    for attempt_v in range(2000):
        seed,co=r.rational_trace(AKL,rng);v=r.mm(KL,co)
        vg=r.mm(WG,v)
        if not np.all(r.units(r.rows(vg,outsideZ))):continue
        if not np.all(r.units(r.mm(r.rows(W[1],I),v))):continue
        if not cusps_unit(v):continue
        break
    else:raise AssertionError('No auxiliary v with only the prescribed SS zeroes')
    assert r.iszero(r.mm(r.rows(W[0],I),v))
    print('Actual v has precisely54 simple SS zeroes; attempt',attempt_v+1,flush=True)
    vv=[r.mm(x,v) for x in W];ww=[r.mm(x,w) for x in W]
    den=[r.mul(vv[0],ww[0]),r.add(r.mul(vv[1],ww[0]),r.mul(vv[0],ww[1]))]
    # H0(2L-R_v), where div(v)=Z+R_v and deg(R_v)=72.
    E=r.rows(M['V2'],other);er,ec=r.rank_pivots(E);assert len(er)==199
    Einv=r.inverse_matrix(r.rows(E,er));constraint=r.zeros(0,199);colon=[]
    for trial in range(6):
        ss,hc=r.rational_trace(AKL,rng);h=r.mm(KL,hc)
        ratio=r.mul(r.mm(r.rows(W[0],other),h),r.inverse_values(r.rows(vv[0],other)))
        scaled=r.mul(ratio,E);res=r.sub(scaled,r.mm(E,r.mm(Einv,r.rows(scaled,er))))
        combined=tuple(np.concatenate([constraint[k],res[k]]) for k in range(2))
        cr,cc=r.rank_pivots(combined);constraint=r.rows(combined,cr);colon.append(r.to_json(h))
        if len(cr)==72:break
        assert len(cr)<72
    else:raise AssertionError('Colon did not saturate')
    KS,ff,bb=r.kernel_from_rows(constraint,cr,cc)
    assert KS[0].shape==(199,127) and r.iszero(r.mm(constraint,KS))
    restriction=r.mm(r.rows(V2[0],I),KS);pr,pc=r.rank_pivots(restriction);assert len(pr)==54
    rhs=r.mul(r.mm(r.rows(W[1],I),v),r.mm(r.rows(W[0],I),w))
    rhs=r.mul(rhs,r.eye(54));co=r.zeros(127,54)
    sol=r.mm(r.inverse_matrix(r.cols(restriction,pc)),rhs)
    for part in range(2):co[part][pc]=sol[part]
    fn=r.mm(KS,co);perm=nu['pole_Frobenius_permutation_0based']
    fn=scale(r.add(fn,r.cols(r.mm(M['A2'],r.conjugate(fn)),perm)),pow(2,-1,r.Q))
    normal=next(j for j in other if M['tau'][j]==j)
    c=r.mul(r.mm(r.rows(V2[0],[normal]),fn),r.inverse_values(r.rows(den[0],[normal])))
    dco=r.rows(den[0],M['P2']);assert r.equal(r.mm(M['V2'],dco),den[0])
    fn=r.sub(fn,r.mul(dco,c))
    assert r.equal(r.mm(r.rows(V2[0],I),fn),rhs)
    assert r.equal(r.mm(M['A2'],r.conjugate(fn)),r.cols(fn,perm))
    av,ad=[r.mm(r.rows(x,other),fn) for x in V2]
    d0,d1=[r.rows(x,other) for x in den]
    df=r.mul(r.sub(r.mul(ad,d0),r.mul(av,d1)),r.inverse_values(r.mul(d0,d0)))
    oldv=r.from_json(nu['denominator_linear_section']);oldn=r.from_json(nu['numerator_cubic_sections'])
    beta=-3*pow(27652,-1,r.Q)%r.Q
    ov=r.mm(r.rows(W[0],other),oldv)
    oldval=r.mul(r.mm(r.rows(V3[0],other),oldn),r.inverse_values(r.mul(ov,ov)))
    values=r.mul(r.add(oldval,scale(df,pow(beta,-1,r.Q))),r.mul(r.rows(ww[0],other),r.rows(ww[0],other)))
    EV=r.rows(M['V3'],other);vr,vc=r.rank_pivots(EV);assert len(vr)==325
    nnew=r.mm(r.inverse_matrix(r.rows(EV,vr)),r.rows(values,vr))
    assert r.equal(r.mm(EV,nnew),values)
    assert r.equal(r.mm(M['A3'],r.conjugate(nnew)),r.cols(nnew,perm))
    for j in [0,11]:
        _,cusp=a.cusp_evaluations(j);assert r.iszero(r.mm(cusp,nnew))
    # An explicit integral rational basis, preserving the actual Frob descent.
    C=r.zeros(54,54);column=0
    for j,k in enumerate(perm):
        if j>k:continue
        assert j!=k
        C[0][j,column]=C[0][k,column]=1
        C[1][j,column+1]=1;C[1][k,column+1]=r.Q-1;column+=2
    assert column==54;Ci=r.inverse_matrix(C)
    realn,realf=r.mm(nnew,C),r.mm(fn,C)
    assert r.equal(r.mm(M['A3'],r.conjugate(realn)),realn)
    assert r.equal(r.mm(M['A2'],r.conjugate(realf)),realf)
    rec=transport['families'][1];TP=r.from_json(rec['T3_parameter_matrix'])
    H=r.mm(r.mm(Ci,tuple(x.T for x in TP)),C);assert not np.any(H[1])
    print('All54 exact pole removals; complete moved cubic numerators and rational basis',flush=True)
    # Reframe the old T3 functions to avoid residual-denominator zeroes on SS disks.
    piv=rec['pole_evaluation_rank_columns_1based'];free=[j for j in range(1,326) if j not in set(piv)]
    KB=r.from_json(old_kernel(325,piv,free,rec['pole_evaluation_kernel_block']))
    assert KB[0].shape==(325,55)
    AB=r.rows(r.mm(M['A3'],r.conjugate(KB)),[i-1 for i in free])
    assert r.equal(r.mm(KB,AB),r.mm(M['A3'],r.conjugate(KB)))
    S=set(Z)
    labelpos={label:i for i,label in enumerate(graph['source_input_labels_0based']['9'])}
    for k in range(4):
        targets=graph['constant_branches']['9/3/'+str(k)]['target_vertices_0based']
        S.update(targets[labelpos[j]] for j in I)
    assert len(S)==270 and all(graph['frobenius_permutation_0based'][j]!=j for j in S)
    outsideS=[j for j in range(3154) if j not in S]
    GV3=a.evaluate(WG)[1];frames=ProjectiveJetFrames(a)
    hw=frames.frame_derivation(w)['H'];wn=r.mul(WG,r.inverse_values(r.mm(WG,w)))
    vv3=a.evaluate(wn)[1];tangent=r.mm(vv3,hw)
    derivative=section_jets([wn,tangent],at.source,M,r)[1][1]
    for attempt_b in range(2000):
        ss,co=r.rational_trace(AB,rng);b=r.mm(KB,co)
        if not np.all(r.units(r.mm(r.rows(GV3,outsideS),b))):continue
        if not np.all(r.units(r.mm(r.rows(derivative,sorted(S)),b))):continue
        break
    else:raise AssertionError('No all-SS-regular T3 denominator frame')
    assert not np.any(r.mm(r.rows(GV3,sorted(S)),b)[0]%47) and not np.any(r.mm(r.rows(GV3,sorted(S)),b)[1]%47)
    bn=r.mm(r.rows(V3[0],other),b);bo=r.mm(r.rows(V3[0],other),r.from_json(rec['denominator_coefficients']))
    fvalues=r.mul(r.mm(r.rows(V3[0],other),r.from_json(rec['numerator_coefficients'])),r.mul(bn,r.inverse_values(bo)))
    fnew=r.mm(r.inverse_matrix(r.rows(EV,vr)),r.rows(fvalues,vr))
    assert r.equal(r.mm(EV,fnew),fvalues)
    fnew=r.mm(fnew,C);assert r.equal(r.mm(M['A3'],r.conjugate(fnew)),fnew)
    print('Actual reframed T3 denominator; simple zeroes precisely270 nonrational SS vertices; attempt',attempt_b+1,flush=True)
    out={'result':'R246','level':41,'auxiliary_prime':47,'precision':4,'modulus':r.Q,
         'all54_second_kind_poles_moved_away_from_all_SS_disks':True,
         'complete_second_kind_large_integrals':False,'complete_local_QC_heights':False,
         'formula':'mu=(nu+dF)*C; F=quadratic_numerator/(v*w); mu=cubic_numerator/w^2*omega_L',
         'new_pole_denominator_w':r.to_json(w),'old_pole_denominator_v':r.to_json(v),
         'moving_function_quadratic_numerators_rational_basis':r.to_json(realf),
         'moved_form_cubic_numerators_rational_basis':r.to_json(realn),
         'original_to_rational_change':r.to_json(C),'rational_to_original_change':r.to_json(Ci),
         'T3_rational_matrix':H[0].astype(int).tolist(),
         'T3_original_function_reframed_numerators_rational_basis':r.to_json(fnew),
         'T3_original_function_reframed_denominator':r.to_json(b),
         'old_pole_SS_vertices_0based':Z,'T3_pole_SS_vertices_0based':sorted(S),
         'all3154_w_values_units':True,'both_cusp_fields_w_and_v_units':True,
         'v_only54_simple_SS_zeroes':True,'b_only270_simple_SS_zeroes':True,
         'colon_dimension':127,'colon_rank':72,'colon_test_sections':colon,
         'moving_principal_rank':54,'full_cubic_reconstruction_equations':766*54,
         'both_complete_cusp_fields_vanish':True,'rational_basis_Frobenius':True,
         'attempts_w_v_b':[attempt_w+1,attempt_v+1,attempt_b+1],
         'normalization_point_1based':normal+1,'input_sha256':a.inputs,
         'source_sha256':sha(__file__),'native':native,'runtime_seconds':round(time.monotonic()-start,3)}
    outsha=save(args.output,out);print('PASS complete pole-moving certificate',outsha,flush=True)

if __name__=='__main__':main()
