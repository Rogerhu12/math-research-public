#!/usr/bin/env python3
"""Actual cyclic/Lie change of basis and all110 SS tiny Abel integrals.

The 54 cyclic coordinates are normalized by B_minus4.  The input logB is
known mod47^4, so logB/47 and the inverse change of basis are mod47^3.
All global height coefficients are divisible by47, making this precision
sufficient for their mod47^4 evaluation.  Three actual CM disks receive
their true constants; no constant on another disk is silently set to zero.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import sys

P=47
Q=P**4
Q3=P**3


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith('.gz') else raw)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--script-dir',type=Path,required=True)
    ap.add_argument('--atlas',type=Path,required=True)
    ap.add_argument('--polynomials',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args();sys.path.insert(0,str(args.script_dir.resolve()))
    import numpy as np
    from p41_actual_differentials47 import ActualModel
    from p41_projective_jet_frames47 import ProjectiveJetFrames
    from p41_elliptic_coarse_atlas47 import Series
    from p41_global_qc_polynomials47 import Field,eval_blocks
    a=ActualModel(args.script_dir.resolve());r=a.r;h=ProjectiveJetFrames(a)
    inputs={args.atlas.name:sha(args.atlas),args.polynomials.name:sha(args.polynomials)}
    atlas=read(args.atlas);globalpoly=read(args.polynomials)
    assert atlas['complete_SS_rational_disk_inventory'] and globalpoly['complete_global_polynomials']
    def get(name):
        path=a.folder/'data'/name;inputs[name]=sha(path);return read(path)
    hecke=get('p41_hecke47_compact.json.gz');log=get('p41_formal47_log_compact.json.gz')
    cmjets=get('p41_cm3_logjets47_checkpoint.json.gz');coarse=get('p41_elliptic_coarse_atlas47_verified.json.gz')
    c3=get('p41_cm3_makdisi47_certificate.json');c12=get('p41_cm12_hecke47_verified.json.gz')
    c7=get('p41_cm7_q2_support47_verified.json.gz')
    assert cmjets['hecke_sha256']==inputs['p41_hecke47_compact.json.gz']
    assert cmjets['log_sha256']==inputs['p41_formal47_log_compact.json.gz']
    T2,T3=[r.from_json(hecke['operators'][str(ell)]['canonical_operator']) for ell in (2,3)]
    H=r.add(T2,a.scale(T3,2));H3=a.reduce(H,Q3)
    logB=r.from_json(log['log_of_B_minus4']);assert all(not np.any(v%P) for v in logB)
    dividedB=tuple(v//P for v in logB)
    orbit=r.zeros(54,54);value=dividedB
    for k in range(54):
        for z in range(2):orbit[z][k]=value[z][0]
        value=r.mm(value,H3,Q3)
    assert r.equal(a.reduce(orbit,P),r.from_json(cmjets['orbit_of_logB_divided47_mod47'],P))
    fields=[Field(ff['factor_descending']) for ff in globalpoly['fields']]
    values=[[1]+[0]*(ff.d-1) for ff in fields];C=[]
    for k in range(54):
        C.append([x%Q3 for val in values for x in val])
        values=[ff.mul(val,[0,1]) for ff,val in zip(fields,values)]
    C=(np.asarray(C,dtype=np.int64),np.zeros((54,54),dtype=np.int64))
    Ci=r.inverse_matrix(C,Q3)
    basis=r.mm(Ci,orbit,Q3);inverse=r.inverse_matrix(basis,Q3)
    assert r.equal(r.mm(basis,inverse,Q3),r.eye(54))
    assert r.equal(r.mm(inverse,basis,Q3),r.eye(54))
    AK=a.reduce(r.from_json(a.cusp['canonical_frobenius_matrix']),Q3)
    assert r.equal(r.mm(basis,AK,Q3),r.conjugate(basis,Q3))
    r3=[x for f in globalpoly['fields'] for x in f['r_minus3']]
    r7=[x for f in globalpoly['fields'] for x in f['r_minus7']]
    r12=[x for f in globalpoly['fields'] for x in f['r_minus12']]
    for key,vec in [('r3',r3),('r7',r7)]:
        cc=(np.asarray([vec],dtype=np.int64)%Q3,np.zeros((1,54),dtype=np.int64))
        got=a.scale(r.mm(cc,basis,Q3),P)
        assert r.equal(got,r.from_json(cmjets['class_logarithms'][key]))
    one=np.asarray([[int(k==0) for ff in fields for k in range(ff.d)]],dtype=np.int64)
    assert r.equal(r.mm((one,np.zeros_like(one)),basis,Q3),dividedB)
    # Weighted global coefficients have valuation at least one.
    for row in globalpoly['directions']:
        for convention in ['absolute_U','based_C']:
            assert all(x%P==0 for block in row[convention]['quadratic_blocks_mod47four'] for rr in block for x in rr)
            assert all(x%P==0 for x in row[convention]['linear_vector_mod47four'])
    omega_by_chart={};tiny_by_chart={};chart_records=[]
    for ch in atlas['charts']:
        W=[r.from_json(v) for v in ch['W_coefficients_0to3']]
        V3=[r.from_json(v) for v in ch['V3_coefficients_0to3']]
        v=r.from_json(ch['frame']);c=r.from_json(ch['coordinate'])
        Hv=h.frame_derivation(v)['H']
        hc=[r.mm(r.mm(v3,Hv),c) for v3 in V3[:3]]
        ih=Series(a,3).inverse(hc)
        wk=[r.mm(w,a.K1) for w in W[:3]]
        omega=Series(a,3).mul(wk,ih)
        assert all(r.equal(r.mm(om,r.from_json(a.cusp['canonical_frobenius_matrix'])),r.conjugate(om)) for om in omega)
        tiny=[]
        for k in range(1,4):
            coeff=a.scale(a.reduce(omega[k-1],Q3),P**(k-1)*pow(k,-1,Q3),Q3)
            cc=r.mm(coeff,inverse,Q3)
            assert not np.any(cc[1]),('nonrational cyclic tiny integral',ch['chart_0based'],k)
            tiny.append(cc[0])
        number=ch['chart_0based'];omega_by_chart[number]=omega;tiny_by_chart[number]=tiny
        chart_records.append({'chart_0based':number,'disk_ids':ch['disk_ids'],
            'canonical_differential_coefficients_0to2_mod47four':[r.to_json(om) for om in omega],
            'cyclic_coordinate_tiny_coefficients_1to3_in_y_mod47cubed':[t.astype(int).tolist() for t in tiny],
            'all54_cyclic_coefficients_rational':True,
            'parameter':'y=z/47 in Z47; cyclic tiny equals a(P)-a(center)'})
    diskmap={tuple(rec['rational_projective_146_mod47']):rec for rec in atlas['SS_disk_records']}
    assert len(diskmap)==110
    def find_disk(W):
        values=r.mm(W,h.candidates);re,im=[v[0]%P for v in values]
        k=next(k for k in range(146) if (int(re[k])**2+int(im[k])**2)%P)
        inv=pow((int(re[k])**2+int(im[k])**2)%P,-1,P)
        normal=(re*int(re[k])+im*int(im[k]))*inv%P
        imaginary=(im*int(re[k])-re*int(im[k]))*inv%P
        assert not np.any(imaginary)
        return diskmap[tuple(int(x) for x in normal)]
    actualpoints=[(-3,r.from_json([c3['coarse_evaluation_coefficients'][0]]),r3,0),
                  (-12,r.from_json([c12['weight2_evaluation_coefficients'][0]]),r12,3),
                  (-7,r.from_json(c7['weight2_evaluation_coefficients'][0]),r7,28)]
    anchors=[]
    for discriminant,raw,classr,component in actualpoints:
        disk=find_disk(raw);ci=disk['chart_0based'];ri=disk['chart_row_0based'];ch=atlas['charts'][ci]
        v=r.from_json(ch['frame']);c=r.from_json(ch['coordinate'])
        W=r.mul(raw,r.inverse_values(r.mm(raw,v)))
        w=r.mm(W,c);center=ch['rational_coordinate_at_center_mod47four'][ri]
        assert not w[1][0,0] and (int(w[0][0,0])-center)%P==0
        z=(int(w[0][0,0])-center)%Q;y=z//P
        tiny=tiny_by_chart[ci]
        delta=[sum(int(tiny[k-1][ri,j])*pow(y,k,Q3) for k in range(1,4))%Q3 for j in range(54)]
        pointa=[(x-b)*pow(20,-1,Q3)%Q3 for x,b in zip(classr,r3)]
        a0=[(x-d)%Q3 for x,d in zip(pointa,delta)]
        # Reproduce every coordinate of the actual CM embedding from the chart.
        ws=[r.from_json(z) for z in ch['W_coefficients_0to3']]
        recovered=r.zeros(1,73)
        for k in range(4):recovered=r.add(recovered,a.scale(r.rows(ws[k],[ri]),pow(z,k,Q)))
        assert r.equal(recovered,W)
        polynomials=[];local_values=[]
        aa=[a0]+[tiny[k][ri].astype(int).tolist() for k in range(3)]
        for row in globalpoly['directions']:
            based=row['based_C'];L=based['linear_vector_mod47four'];result=[0]*7
            for k in range(4):result[k]=sum(x*y for x,y in zip(L,aa[k]))%Q
            offset=0
            for block in based['quadratic_blocks_mod47four']:
                d=len(block)
                for k in range(4):
                    for ell in range(4):
                        result[k+ell]+=sum(aa[k][offset+i]*block[i][j]*aa[ell][offset+j] for i in range(d) for j in range(d))
                offset+=d
            result=[x%Q for x in result];assert result[5:]==[0,0]
            observed=sum(result[k]*pow(y,k,Q) for k in range(5))%Q
            assert observed==eval_blocks(row,pointa,'based_C')
            target=row['QC_defect_targets_by_component_order'][globalpoly['component_order'].index(component)]
            local=(observed-target)%Q
            polynomials.append({'n':row['n'],'coefficients_0to4_in_y_mod47four':result[:5]})
            local_values.append(local)
        anchors.append({'discriminant':discriminant,'disk_id':disk['disk_id'],
            'chart_0based':ci,'chart_row_0based':ri,'bad_component_at41':component,
            'physical_chart_parameter_z_of_CM_point_mod47four':z,'rescaled_parameter_y_of_CM_point_mod47cubed':y,
            'actual_CM_cyclic_coordinates_mod47cubed':pointa,
            'actual_center_cyclic_coordinates_mod47cubed':a0,
            'global_polynomials_at_rational_center':polynomials,
            'local_global_section_heights_at_CM_point_by_global_reciprocity':local_values,
            'local_values_method':'Global R222 heights and the known rational CM point with its R134/R135 bad component, not a new local Miller computation'})
    # Independent CM3 KS/physical-coordinate comparison through u^2.
    c3rec=next(rec for rec in coarse['elliptic_charts'] if rec['kind']=='CM3')
    physical=[r.from_json(v) for v in c3rec['coarse_values']]
    anch=next(x for x in anchors if x['discriminant']==-3);ci=anch['chart_0based'];ri=anch['chart_row_0based']
    ch=atlas['charts'][ci];v=r.from_json(ch['frame']);c=r.from_json(ch['coordinate'])
    fv=[r.mm(w,v) for w in physical]
    normalized=Series(a,4).mul(physical,Series(a,4).inverse(fv))
    zseries=[r.mm(w,c) for w in normalized]
    zseries[0]=r.sub(zseries[0],r.column([[ch['rational_coordinate_at_center_mod47four'][ri],0]]))
    assert r.iszero(zseries[0])
    composed=Series(a,3).compose([r.rows(om,[ri]) for om in omega_by_chart[ci]],zseries[:3],3)
    derivative=[a.scale(zseries[k],k) for k in range(1,4)]
    physical_omega=Series(a,3).mul(composed,derivative)
    expected=[r.from_json(v) for v in cmjets['canonical_differential_coefficients']]
    assert all(r.equal(x,y) for x,y in zip(physical_omega,expected))
    anchored={x['disk_id'] for x in anchors};missing=[rec['disk_id'] for rec in atlas['SS_disk_records'] if rec['disk_id'] not in anchored]
    assert len(missing)==107
    output={'level':41,'auxiliary_prime':47,'precision':4,'modulus':Q,
        'complete_cyclic_Lie_change_of_basis':True,'complete_110_SS_tiny_Abel_integrals':True,
        'complete_all_SS_Abel_constants':False,'complete_local_QC_functions':False,'complete_common_roots':False,
        'coordinate_basis':globalpoly['coordinate_basis'],
        'Lie_basis':log['differential_basis'],
        'cyclic_to_divided_Lie_mod47cubed':r.to_json(basis),
        'divided_Lie_to_cyclic_mod47cubed':r.to_json(inverse),
        'matrix_convention':'row log(aB)/47 = row a * cyclic_to_divided_Lie; inverse multiplication recovers row a',
        'unit_orbit_matches_R121':True,'both_matrix_inverse_products_identity':True,
        'true_CM3_physical_KS_jets_all54_through_degree2_match':True,
        'differential_formula':'omega=(W*K1)/(V3*H_v*c) dz in normalized W*v=1 and z=W*c-center',
        'tiny_formula':'a(P)-a(center)=[sum_{k=1}^3 47^(k-1)*omega_(k-1)*y^k/k]*inverse_basis mod47^3, y=z/47',
        'global_precision_reason':'All global quadratic and linear coefficients are in47; cyclic coordinates modulo47^3 suffice modulo47^4',
        'tail_bound':'Integral differential coefficients imply valuation n-v47(n) for integrated z^n at z in47Z47; after division by47 every n>=4 term vanishes mod47^3',
        'charts':chart_records,'known_CM_anchored_disks':anchors,
        'missing107_SS_center_constant_disk_ids':missing,
        'additional19_ordinary_disks_require_centers_and_constants':True,
        'input_sha256':dict(a.inputs,**inputs),'source_sha256':sha(__file__),
        'module_sha256':{n:sha(sys.modules[n].__file__) for n in ['p41_global_qc_polynomials47','p41_projective_jet_frames47']}}
    args.output.write_bytes(gzip.compress((json.dumps(output,sort_keys=True,separators=(',',':'))+'\n').encode(),mtime=0))
    print('PASS cyclic/Lie unit basis, all110 tiny Abel integrals, independent54 CM3 KS jets and 3 true CM constants',flush=True)
    print('CM anchor disks',[(x['discriminant'],x['disk_id']) for x in anchors],'; remaining SS constants',len(missing),flush=True)
    print('SHA',sha(args.output),flush=True)


if __name__=='__main__':main()
