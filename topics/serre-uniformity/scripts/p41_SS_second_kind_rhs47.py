#!/usr/bin/env python3
"""Actual regularized second-kind SS Hecke right sides and Frobenius shifts."""
import argparse,gzip,hashlib,json,random,sys,time
from pathlib import Path

def read(p):
    b=Path(p).read_bytes();return json.loads(gzip.decompress(b) if str(p).endswith('.gz') else b)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--script-dir',type=Path,required=True)
    ap.add_argument('--moved',type=Path,required=True)
    ap.add_argument('--work-dir',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args();sys.path.insert(0,str(args.script_dir.resolve()))
    args.work_dir.mkdir(parents=True,exist_ok=True)
    import numpy as np
    import p41_r2_matrix as r
    from p41_projective_jet_frames47 import install_exact_float_mm,ProjectiveJetFrames,ordinary_physical_jets,matrix_digest
    install_exact_float_mm(r)
    from p41_native_r2_linear47 import install
    install(r,args.work_dir/'native')
    from p41_elliptic_coarse_atlas47 import setup,Series,ClassicalInvariants
    from p41_actual_differentials47 import save
    from p41_scalar_primitive_atlas47 import scalar_gm
    from p41_coprime_kernel_dag47 import Jets,R,division_polynomial,Dual
    at=setup(args.script_dir.resolve());a=at.a;M=a.M;scale=a.scale;Q=r.Q;Q3=47**3
    inv=ClassicalInvariants(at);frames=ProjectiveJetFrames(a);start=time.monotonic()
    graph=a.read('p41_SS_Hecke_graph47.json.gz')
    coarse=a.read('p41_elliptic_coarse_atlas47_verified.json.gz')
    atlas=a.read('p41_rational_SS_residue_atlas47_complete.json.gz')
    moved=read(args.moved);assert moved['all54_second_kind_poles_moved_away_from_all_SS_disks']
    w=r.from_json(moved['new_pole_denominator_w']);v=r.from_json(moved['old_pole_denominator_v'])
    Fn=r.from_json(moved['moving_function_quadratic_numerators_rational_basis'])
    Nn=r.from_json(moved['moved_form_cubic_numerators_rational_basis'])
    fn=r.from_json(moved['T3_original_function_reframed_numerators_rational_basis'])
    b=r.from_json(moved['T3_original_function_reframed_denominator'])
    H=(np.asarray(moved['T3_rational_matrix'],dtype=np.int64),np.zeros((54,54),dtype=np.int64))
    Z=set(moved['old_pole_SS_vertices_0based']);S=set(moved['T3_pole_SS_vertices_0based'])
    n=3154;tau=np.asarray(graph['frobenius_permutation_0based'],dtype=np.int64)
    source={str(j):{'W':x['W'],'labels':list(range(1,821))} for j,x in at.refs.items()}
    for rec in coarse['elliptic_charts']:
        source[rec['kind']]={'W':r.from_json(rec['coarse_values'][0]),'labels':rec['indices_1based']}
    position={key:{label:i for i,label in enumerate(x['labels'])} for key,x in source.items()}
    WG=r.zeros(n,73);chosen={};members={}
    for vertex in graph['vertices']:
        i=vertex['vertex_0based'];s=vertex['chosen_reference'];key=s['reference_key'];row=s['input_row_0based']
        chosen.setdefault(key,{})[row]=i
        for part in range(2):WG[part][i]=source[key]['W'][part][row]
        for s in vertex['members']:members[(s['reference_key'],s['necklace_label_1based'])]=i
    W2,W3=a.evaluate(WG);wv=r.mm(WG,w);assert np.all(r.units(wv))
    # One frame w works throughout all 3154 disks; choose unit coordinates.
    HW=frames.frame_derivation(w)['H'];Wnorm=r.mul(WG,r.inverse_values(wv))
    Vnorm=a.evaluate(Wnorm)[1];tangent=r.mm(Vnorm,HW)
    possibilities=r.units(r.mm(tangent,frames.candidates));left=set(range(n));groups=[];first=True
    while left:
        rows=sorted(left)
        col=0 if first else int(np.argmax(np.sum(possibilities[rows],axis=0)));first=False
        hit=[i for i in rows if possibilities[i,col]]
        if not hit:continue
        groups.append((hit,r.cols(frames.candidates,[col])));left.difference_update(hit)
    Wcoef=[r.zeros(n,73) for _ in range(4)]
    tinycoef=[r.zeros(n,54) for _ in range(3)]
    coords=r.zeros(n,73);coord0=r.zeros(n,1);charts=[]
    for rows,c in groups:
        for first in range(0,len(rows),64):
            I=rows[first:first+64];chart=frames.local_jets(r.rows(WG,I),w,c,HW,order=3)
            omega=Series(a,3).mul([r.mm(x,Nn) for x in chart['V3'][:3]],chart['inverse_Hc'][:3])
            primitive=[scale(omega[k],pow(k+1,-1,Q)) for k in range(3)]
            for part in range(2):
                for k in range(4):Wcoef[k][part][I]=chart['W'][k][part]
                for k in range(3):tinycoef[k][part][I]=primitive[k][part]
                coords[part][I]=c[part][:,0][None,:]
                coord0[part][I]=chart['coordinate_base_value'][part]
            name='moved-chart-'+str(len(charts)).zfill(3)+'.json.gz'
            content={'vertices_0based':I,'coordinate':r.to_json(c),'frame':r.to_json(w),
                     'coordinate_base_value':r.to_json(chart['coordinate_base_value']),
                     'W_coefficients_0to3':[r.to_json(x) for x in chart['W']],
                     'mu_coefficients_0to2':[r.to_json(x) for x in omega],
                     'primitive_coefficients_1to3':[r.to_json(x) for x in primitive]}
            digest=save(args.work_dir/name,content)
            charts.append({'file':name,'sha256':digest,'vertices_0based':I})
    print('All3154 regular second-kind charts and actual primitives',len(charts),flush=True)
    def rowdot(X,Y):
        return ((X[0]*Y[0]-X[1]*Y[1]).sum(axis=1)[:,None]%Q,
                (X[0]*Y[1]+X[1]*Y[0]).sum(axis=1)[:,None]%Q)
    def tiny_to(W,I):
        f=r.mm(W,w);assert np.all(r.units(f))
        z=r.sub(r.mul(rowdot(W,r.rows(coords,I)),r.inverse_values(f)),r.rows(coord0,I))
        assert not np.any(z[0]%47) and not np.any(z[1]%47)
        recovered=r.zeros(len(I),73)
        for c in reversed(Wcoef):recovered=r.add(r.mul(recovered,z),r.rows(c,I))
        assert r.equal(recovered,r.mul(W,r.inverse_values(f))),'all73 actual target chart mismatch'
        delta=r.zeros(len(I),54)
        for c in reversed(tinycoef):delta=r.mul(r.add(delta,r.rows(c,I)),z)
        return delta,z
    def Fvalues(W):
        vv,ww=r.mm(W,v),r.mm(W,w);D=r.mul(vv,ww);ok=np.flatnonzero(r.units(D)[:,0]).tolist()
        out=r.zeros(W[0].shape[0],54)
        if ok:
            num=r.mm(a.evaluate(r.rows(W,ok))[0],Fn)
            val=r.mul(num,r.inverse_values(r.rows(D,ok)))
            for part in range(2):out[part][ok]=val[part]
        return out,ok
    fsD=r.mm(W3,b);good=sorted(set(range(n))-S)
    assert set(np.flatnonzero(r.units(fsD)[:,0]).tolist())==set(good)
    Fsource,Fsource_good=Fvalues(WG);assert set(Fsource_good)==set(range(n))-Z
    folded=r.zeros(n,54)
    val=r.mul(r.mm(r.rows(W3,good),fn),r.inverse_values(r.rows(fsD,good)))
    for part in range(2):folded[part][good]=val[part]
    expression=r.sub(folded,r.mm(Fsource,H));tiny_sum=r.zeros(n,54)
    physical={str(j):ordinary_physical_jets(at,j,order=3)['W'] for j in at.refs}
    for rec in coarse['elliptic_charts']:physical[rec['kind']]=[r.from_json(x) for x in rec['coarse_values']]
    def physical_values(key,labels,t):
        I=[position[key][x] for x in labels];X=r.zeros(len(I),73);tt=r.column([list(t)]*len(I))
        for c in reversed(physical[key]):X=r.add(r.mul(X,tt),r.rows(c,I))
        return X
    bad_targets={};branch_audit=[];source_counts=np.zeros(n,dtype=np.int64)
    for name,branch in graph['constant_branches'].items():
        if branch['ell']!=3:continue
        key=branch['source_reference_key'];selected=[];src=[]
        for row,label in enumerate(graph['source_input_labels_0based'][key]):
            k=position[key][label+1]
            if k in chosen[key]:selected.append(row);src.append(chosen[key][k])
        target=[branch['target_vertices_0based'][row] for row in selected]
        WT=r.zeros(len(src),73);regular=[];special=[]
        for k,row in enumerate(selected):
            label=branch['image_indices_1based'][row]
            (regular if (branch['reference_key'],label) in members else special).append((k,row,label))
        for items,is_special in [(regular,False),(special,True)]:
            if not items:continue
            rec=branch['coarse'] if is_special else branch;tkey=rec['reference_key']
            labels=[rec['image_indices_1based'][row] for k,row,label in items]
            t=rec['invariant_parameter'] if is_special else rec['reference_parameter']
            val=physical_values(tkey,labels,t)
            # Nonelliptic rows use the actual Velu differential frame.
            if not is_special:
                val=at.matrix_scale(val,R.power(tuple(rec['homothety']),2))
            for part in range(2):WT[part][[k for k,row,label in items]]=val[part]
        delta,z=tiny_to(WT,target);Ft,ok=Fvalues(WT)
        for part in range(2):
            tiny_sum[part][src]=(tiny_sum[part][src]+delta[part])%Q
            expression[part][src]=(expression[part][src]+Ft[part])%Q
        source_counts[src]+=1
        bad=[k for k,t in enumerate(target) if t in Z]
        assert set(bad)==set(range(len(src)))-set(ok)
        for k in bad:
            assert src[k] in S-Z and src[k] not in bad_targets
            assert k in [x[0] for x in regular]
            bad_targets[src[k]]={'branch':name,'W0':r.to_json(r.rows(WT,[k]))}
        branch_audit.append({'branch':name,'source_points':len(src),'all73_target_coordinates':True,
                             'target_parameter_sha256':matrix_digest(z),'pole_target_count':len(bad)})
        print('Actual regular mu Hecke targets',name,len(src),'pole targets',len(bad),flush=True)
    assert np.all(source_counts==4) and set(bad_targets)==S-Z
    # Generate physical Serre jets only where two apparent simple poles cancel.
    def raw_jets(W0,aa,bb,order,seed):
        assert len(aa)>=order and len(bb)>=order
        total=W0[0].shape[0];output=[W0]+[r.zeros(total,73) for _ in range(order)]
        remaining=set(range(total));rng=random.Random(seed)
        for attempt in range(30):
            if attempt==0:cv,CG=at.v,at.G
            else:
                c=r.column([[rng.randrange(47),rng.randrange(47)] for _ in range(52)])
                cv=r.mm(at.K,c);cv=r.add(cv,r.mm(M['A1'],r.conjugate(cv)))
                vals=r.mul(r.mm(M['W'],cv),at.delta);CG=r.rows(vals,M['P3'])
                assert r.equal(r.mm(M['V3'],CG),vals)
            unit=r.units(r.mm(W0,cv))[:,0];I=[i for i in sorted(remaining) if unit[i]]
            if not I:continue
            W=[r.rows(W0,I)]
            for n0 in range(order):
                V3=inv.section_series(W)[1];vs=[r.mm(x,cv) for x in W]
                iv=Series(a,n0+1).inverse(vs);Gs=[r.mm(x,CG) for x in V3];rhs=r.zeros(len(I),73)
                for k in range(n0+1):
                    for j in range(n0-k+1):rhs=r.add(rhs,at.matrix_scale(r.mul(Gs[k],iv[j]),bb[n0-k-j]))
                    rhs=r.sub(rhs,at.matrix_scale(W[n0-k],R.scale(aa[k],2)))
                W.append(scale(rhs,pow(n0+1,-1,Q)))
                for part in range(2):output[n0+1][part][I]=W[-1][part]
            remaining.difference_update(I)
            if not remaining:break
        assert not remaining
        return output
    ORDER=8;source_jets={};gm={}
    for key in sorted({graph['vertices'][i]['chosen_reference']['reference_key'] for i in S}):
        j=int(key);ref=at.refs[j];I=sorted(i for i in S if graph['vertices'][i]['chosen_reference']['reference_key']==key)
        aa,bb=scalar_gm(ref['A'],ref['B'],j==0,ORDER);gm[key]=(aa,bb)
        W=raw_jets(r.rows(WG,I),aa,bb,ORDER,24700000+j)
        for k,i in enumerate(I):source_jets[i]=[r.rows(x,[k]) for x in W]
        print('Actual source pole jets',key,len(I),'order',ORDER,flush=True)
    target_jets={}
    for name in sorted({d['branch'] for d in bad_targets.values()}):
        branch=graph['constant_branches'][name];key=branch['source_reference_key'];j=int(key)
        I=sorted(i for i,d in bad_targets.items() if d['branch']==name)
        W0=r.from_json([bad_targets[i]['W0'][0] for i in I]);aa,bb=gm[key]
        # The actual degree3 kernel is linear: u=2*x in the R218 de Rham relation.
        J=Jets(R,ORDER+1);A=J.constant(tuple(branch['source_A']));B=J.constant(tuple(branch['source_B']))
        A=list(A);B=list(B);(A if j==0 else B)[1]=R.one;A=tuple(A);B=tuple(B)
        x=J.constant(R.neg(tuple(branch['kernel'][0])));DJ=Dual(J)
        for _ in range(4):
            err,der=division_polynomial(3,(x,J.one),(A,J.zero),(B,J.zero),DJ)
            x=J.sub(x,J.mul(err,J.inverse(der)))
        assert division_polynomial(3,x,A,B,J)==J.zero
        inv3=pow(3,-1,Q);atarget=[];btarget=[R.scale(x,inv3) for x in bb]
        for k in range(ORDER):
            u=R.zero
            for h in range(k+1):u=R.add(u,R.mul(R.scale(x[h],2),bb[k-h]))
            atarget.append(R.add(aa[k],R.scale(u,inv3)))
        W=raw_jets(W0,atarget,btarget,ORDER,24710000+len(target_jets))
        for k,i in enumerate(I):target_jets[i]=[r.rows(x,[k]) for x in W]
        print('Actual target pole jets',name,len(I),flush=True)
    finite_parts=[]
    for count,i in enumerate(sorted(S)):
        W=source_jets[i];V2,V3=inv.section_series(W);ss=Series(a,ORDER+1)
        nb=[r.mm(x,fn) for x in V3];db=[r.mm(x,b) for x in V3]
        if i in Z:
            nf=[r.mm(r.mm(x,Fn),H) for x in V2]
            df=ss.mul([r.mm(x,v) for x in W],[r.mm(x,w) for x in W])
            num=ss.sub(ss.mul(nb,df),ss.mul(nf,db));kind='source'
        else:
            TW=target_jets[i];TV2=inv.section_series(TW)[0]
            nf=[r.mm(x,Fn) for x in TV2]
            df=ss.mul([r.mm(x,v) for x in TW],[r.mm(x,w) for x in TW])
            num=ss.add(ss.mul(nb,df),ss.mul(nf,db));kind='target'
        den=ss.mul(db,df)
        assert not np.any(den[0][0]%47) and not np.any(den[0][1]%47)
        assert not np.any(den[1][0]%47) and not np.any(den[1][1]%47)
        assert np.all(r.units(den[2]))
        size=6;mat=r.zeros(size,size)
        for j in range(size):
            for k in range(size):
                d=2+j-k
                if 0<=d<len(den):
                    for part in range(2):mat[part][j,k]=den[d][part][0,0]
        rhs=tuple(np.concatenate([num[k][part] for k in range(2,2+size)],axis=0)%Q3 for part in range(2))
        mm=a.reduce(mat,Q3);quot=r.mm(r.inverse_matrix(mm,Q3),rhs,Q3)
        assert r.equal(r.mm(mm,quot,Q3),rhs)
        for k in range(2):
            val=r.zeros(1,54)
            for j in range(k+1):val=r.add(val,r.mul(a.reduce(den[j],Q3),r.rows(quot,[k-j]),Q3),Q3)
            assert r.equal(val,a.reduce(num[k],Q3)),('finite part low equation',i,k)
        for part in range(2):expression[part][i]=(expression[part][i]+quot[part][0])%Q3
        finite_parts.append({'vertex_0based':i,'pole_kind':kind,'division_order':2,'matrix_size':size,
                             'denominator_coefficients':[r.to_json(x) for x in den],
                             'numerator_coefficients_0to7':[r.to_json(x) for x in num[:8]],
                             'quotient_coefficients':r.to_json(quot),'low_equations_mod47cubed':True})
        if (count+1)%54==0:print('Actual finite parts',count+1,'/270',flush=True)
    expression=a.reduce(expression,Q3)
    # Exact full-field traces at the two length10 Frobenius^2 cusp orbits.
    a.field_setup();poly=a.field_polynomial;tr=[80]
    for k in range(1,80):
        tr.append((-sum(int(poly[80-j])*tr[k-j] for j in range(1,k))-k*int(poly[80-k]))%Q)
    tr=np.asarray(tr,dtype=np.int64)
    def finverse(x):
        eye=np.eye(80,dtype=np.int64);B=np.stack([a.field_mul(x,y) for y in eye],axis=1)
        iv=r.inverse_matrix((B,np.zeros_like(B)));z=iv[0][:,0]
        assert not np.any(iv[1]) and np.array_equal(a.field_mul(x,z),eye[0])
        return z
    def cusp_raw(index):
        cw=np.asarray(a.cusp['cusp_values'][index],dtype=np.int64)
        vv2=a.field_rows([a.field_mul(cw[x],cw[y]) for x,y in zip(a.a2,a.b2)],a.C2)
        ex=a.field_rows([a.field_mul(cw[x],vv2[y]) for x,y in zip(a.a3,a.b3)],a.E3)
        vv3=[(-x)%Q for x in a.field_rows(ex,a.C)]+ex
        return cw,vv2,vv3
    def trace_cusp_values(values):
        re=np.asarray([int(tr@x)%Q for x in values],dtype=np.int64)*pow(8,-1,Q)%Q
        im=np.asarray([-int(tr@a.field_mul(a.ii,x))%Q for x in values],dtype=np.int64)*pow(8,-1,Q)%Q
        return re[None,:],im[None,:]
    FD=r.zeros(1,54);fD=r.zeros(1,54);cusp_audit=[]
    for idx in [0,11]:
        cw,cv2,cv3=cusp_raw(idx)
        dv=a.field_mul(a.field_rows(cw,v)[0],a.field_rows(cw,w)[0])
        db=a.field_rows(cv3,b)[0];iv,idb=finverse(dv),finverse(db)
        fvals=[a.field_mul(x,iv) for x in a.field_rows(cv2,Fn)]
        bvals=[a.field_mul(x,idb) for x in a.field_rows(cv3,fn)]
        FD=r.add(FD,trace_cusp_values(fvals));fD=r.add(fD,trace_cusp_values(bvals))
        cusp_audit.append({'cusp_index_0based':idx,'all_full_field_denominators_units':True})
    assert not np.any(FD[1]) and not np.any(fD[1])
    totalfD=r.sub(r.add(fD,scale(FD,4)),r.mm(FD,H))
    rhs=r.sub(r.sub(scale(expression,20,Q3),a.reduce(totalfD,Q3),Q3),scale(a.reduce(tiny_sum,Q3),20,Q3),Q3)
    frobW=r.mm(r.conjugate(WG),r.conjugate(M['A1']))
    delta_frob,zf=tiny_to(frobW,tau.tolist())
    anti=10*delta_frob[0]%Q3
    assert not np.any((anti+anti[tau])%Q3)
    adj=np.asarray(graph['adjacency']['3'],dtype=np.int64)
    antiT=sum((anti[adj[:,k]] for k in range(4)),np.zeros_like(anti))%Q3
    defect=(antiT-r.mm((anti,np.zeros_like(anti)),a.reduce(H,Q3),Q3)[0])%Q3
    evenrhs=(rhs[0]-defect)%Q3
    assert np.array_equal(evenrhs,evenrhs[tau]),'true Frobenius tiny correction does not make RHS even'
    # The already-computed actual Poincare gradient of B fixes the even kernel.
    cm4=[i for i,x in enumerate(graph['vertices']) if x['chosen_reference']['reference_key']=='CM4']
    assert len(cm4)==20
    nu=a.read('p41_second_kind_connection47.json.gz')
    Omega=r.neg(r.from_json(nu['second_kind_holomorphic_residue_pairing']))
    completion=a.read('p41_miller_completion47_compact.json.gz')
    gLie=r.from_json(completion['actual_initial_fibre_Lie_gradient_mod47_cubed'],Q3)
    gnu=tuple(x.T for x in r.mm(a.reduce(Omega,Q3),gLie,Q3))
    C=r.from_json(moved['original_to_rational_change'],Q3)
    gnew=r.mm(gnu,C,Q3)
    sumF=tuple(np.sum(x[cm4],axis=0)[None,:]%Q3 for x in Fsource)
    gnew=r.add(gnew,r.sub(sumF,a.reduce(FD,Q3),Q3),Q3)
    assert not np.any(gnew[1])
    Banchor=(20*gnew[0]-np.sum(anti[cm4],axis=0)[None,:])%Q3
    geometric={tuple(x['projective_146_mod47_real']):x['vertex_0based'] for x in graph['vertices'] if x['F47_rational']}
    rational=[]
    for disk in atlas['SS_disk_records']:
        i=geometric[tuple(disk['rational_projective_146_mod47'])]
        ch=atlas['charts'][disk['chart_0based']]
        WP=r.rows(r.from_json(ch['W_coefficients_0to3'][0]),[disk['chart_row_0based']])
        delta,z=tiny_to(WP,[i]);FP,ok=Fvalues(WP);assert ok==[0]
        rational.append({'disk_id':disk['disk_id'],'vertex_0based':i,
                         'tiny_mu_from_graph_center_mod47four':r.to_json(delta)[0],
                         'moving_F_rational_center_mod47four':r.to_json(FP)[0],
                         'all73_actual_rational_center_coordinates':True})
    assert len(rational)==110
    out={'result':'R247-RHS','level':41,'auxiliary_prime':47,'precision':3,'modulus':Q3,
         'complete_actual_second_kind_Hecke_rhs':True,'complete_second_kind_large_integrals':False,
         'complete_local_QC_heights':False,'equation':'A3*Re(N)-Re(N)*H3=Re(rhs); X=Re(N)-anti is Frobenius even',
         'T3_rational_matrix':moved['T3_rational_matrix'],'rhs_real_mod47cubed':rhs[0].astype(int).tolist(),
         'Frobenius_antisymmetric_part_mod47cubed':anti.astype(int).tolist(),
         'Frobenius_even_rhs_mod47cubed':evenrhs.astype(int).tolist(),
         'B_anchor_vertices_0based':cm4,'B_anchor_sum_even_N_mod47cubed':Banchor[0].astype(int).tolist(),
         'actual_B_second_kind_rational_gradient_mod47cubed':gnew[0][0].astype(int).tolist(),
         'rational_SS_center_maps':rational,'rational_to_original_change':moved['rational_to_original_change'],
         'charts':charts,'actual_branch_checks':branch_audit,'actual_target_count':int(source_counts.sum()),
         'finite_part_vertices':len(finite_parts),'cusp_checks':cusp_audit,
         'cusp_F_sum_mod47four':r.to_json(FD),'cusp_f_tilde_sum_mod47four':r.to_json(totalfD),
         'all54_Frobenius_even_equations_verified':True,
         'input_sha256':dict(a.inputs,**{args.moved.name:sha(args.moved)}),
         'source_sha256':sha(__file__),'runtime_seconds':round(time.monotonic()-start,3)}
    finitefile=args.work_dir/'all270_actual_second_kind_finite_parts47.json.gz'
    out['finite_part_certificate']={'file':finitefile.name,'sha256':save(finitefile,{'records':finite_parts,'precision':3})}
    digest=save(args.output,out)
    print('PASS all3154 genuine second-kind RHS,270 finite parts,12616 targets,Frobenius and B anchor',digest,flush=True)

if __name__=='__main__':main()
