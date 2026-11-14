#!/usr/bin/env python3
"""Full sampled cap traces and actual principal-form change for Codazzi states.

All outputs are floating diagnostics.  The old-reference finite difference
U=Fold dot (Fnew-Fold)/Fold_z is explicitly NOT asserted to be a Jacobi
field.  Its conormal is computed with the old fixed-type grounded matrix,
and cannot be compared to a homogeneous cap DN without its forcing and the
regular trace.  New actual and target-modified matrices are kept separate.
"""
from __future__ import annotations
import argparse,gzip,io,json
from pathlib import Path
import numpy as np
from fourfold_phase_symmetric_geometry import load_exact_object
from fourfold_phase_core_low_block import uniform_fields
from fourfold_phase_codazzi_evolution_probe import Evolution,resample
from fourfold_phase_local_correction_probe import (
    sha,dot,angular_derivative,scalar_target,source_and_geometry,correction_norms,
)


def principal(fields,K):
    F,P,T,PP,PT,TT=fields
    cross=np.cross(T,P);G=dot(cross,cross);S=dot(F,cross)
    L,M,N=[dot(cross,z) for z in (PP,PT,TT)]
    factor=F[:,2]**2/S**2
    result=np.empty((len(F),2,2));result[:,0,0]=-factor*N
    result[:,0,1]=result[:,1,0]=factor*M
    result[:,1,1]=-factor*(M*M+K*G*G)/N
    actual=result.copy();actual[:,1,1]=-factor*L
    return result,actual,dict(minus_nraw_min=float(np.min(-N)),
        height_min=float(np.min(F[:,2])),support_min=float(np.min(S/np.sqrt(G))),
        actual_K_min=float(np.min((L*N-M*M)/G**2)),
        actual_K_max=float(np.max((L*N-M*M)/G**2)))


def relative_form(reference,other):
    # L^{-1} other L^{-T} is congruent to the reference-normalized form.
    L=np.linalg.cholesky(reference);T=np.linalg.inv(L)
    relative=T@other@np.swapaxes(T,1,2)
    eig=np.linalg.eigvalsh(relative)
    return dict(sampled_generalized_eigenvalue_range=[float(np.min(eig)),float(np.max(eig))],
        sampled_relative_form_difference=float(np.max(abs(eig-1))))


def band_sums(c):
    mode=abs(np.fft.fftfreq(len(c),1/len(c)))
    cuts=[0,1,4,8,16,32,64,128,256,512,1024,len(c)//2+1]
    cuts=sorted(set(x for x in cuts if x<=len(c)//2+1))
    return {f'{a}:{b}':float(np.sum(abs(c[(mode>=a)&(mode<b)])))
        for a,b in zip(cuts,cuts[1:])}


def snapshot(path,geometry,object_sha):
    saved=np.load(path,allow_pickle=False);meta=json.loads(str(saved['metadata']))
    if meta['object_sha256']!=object_sha:raise ValueError('different actual object')
    r=float(saved['r']);coarse=saved['state'];ngrid=len(coarse);fine=resample(coarse,2*ngrid)
    t=scalar_target(geometry,r);sqrtE=np.sqrt(t['E'])
    evolution=Evolution(geometry,ngrid,2)
    radial=resample(evolution.evaluate(r,coarse.ravel()).reshape(ngrid,14),2*ngrid)
    B,C=fine[:,0],fine[:,1];F,X=fine[:,2:5],fine[:,5:8]
    P=sqrtE*X;T=angular_derivative(F)
    PP=t['E_x']/(2*sqrtE)*X+sqrtE*radial[:,5:8]
    PT=angular_derivative(P);TT=angular_derivative(T)
    new=(F,P,T,PP,PT,TT);old=uniform_fields(geometry,r,2*ngrid)
    old_form,old_actual,old_info=principal(old,t['K'])
    new_form,new_actual,new_info=principal(new,t['K'])
    V=tuple(v-o for v,o in zip(new,old));F0,Pr0,Pt0=old[:3]
    h=F0[:,2];U=dot(F0,V[0])/h
    Ur=(dot(Pr0,V[0])+dot(F0,V[1])-U*Pr0[:,2])/h
    Ut=(dot(Pt0,V[0])+dot(F0,V[2])-U*Pt0[:,2])/h
    outward=-(old_form[:,0,0]*Ur+old_form[:,0,1]*Ut)
    old_geom=source_and_geometry(old,t);new_geom=source_and_geometry(new,t)
    A=(t['K']+B*B)/C
    values=np.column_stack([B,C,A,U,Ur,Ut,outward])
    names=['B','C','A','old_reference_grounded_difference','old_reference_grounded_difference_r',
        'old_reference_grounded_difference_theta','old_reference_outward_conormal']
    spectrum=np.fft.fft(values,axis=0)/len(values)
    row=dict(state_path=str(path),state_sha256=sha(path),r=r,angular_grid=ngrid,
        diagnostic_grid=len(values),K0=t['K'],minimum_abs_C=float(np.min(abs(C))),
        B_C_supnorm=np.max(abs(values[:,:2]),axis=0).tolist(),
        old_geometry=old_info,new_geometry=new_info,
        old_modified_to_new_modified=relative_form(old_form,new_form),
        old_modified_to_new_actual=relative_form(old_form,new_actual),
        old_modified_to_old_actual=relative_form(old_form,old_actual),
        updated_metric_defect_C0=float(np.max(new_geom['metric_norm'])),
        updated_source_C0=float(np.max(abs(new_geom['q']))),
        actual_curvature_defect_C0=float(np.max(abs(new_geom['actual_K']-t['K']))),
        correction=correction_norms(V,old_geom),
        old_reference_grounded_difference=dict(
            U_supnorm=float(np.max(abs(U))),Ur_supnorm=float(np.max(abs(Ur))),
            Utheta_supnorm=float(np.max(abs(Ut))),outward_flux_supnorm=float(np.max(abs(outward))),
            U_mean=float(np.mean(U)),outward_flux_mean=float(np.mean(outward)),
            regular_trace=None,regular_conjugate_flux=None,
            boundary_source_particular_not_computed=True),
        spectrum_bands={name:band_sums(spectrum[:,j]) for j,name in enumerate(names)},
        spectrum_fields=names)
    if t['K']>0:
        row['sampled_maximum_elliptic_growth_coefficient_per_physical_frequency']=float(
            np.max(sqrtE/t['a']*np.sqrt(t['K'])/abs(C)))
    return row,spectrum


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    p.add_argument('--state-in',type=Path,action='append',required=True)
    p.add_argument('--out',type=Path,required=True);p.add_argument('--spectra',type=Path,required=True)
    args=p.parse_args();geometry,definition=load_exact_object(args.object,512)
    rows=[];spectra={};states=[]
    for j,path in enumerate(args.state_in):
        row,spectrum=snapshot(path,geometry,sha(args.object));rows.append(row)
        spectra[f'row_{j}_sampled_spectrum']=spectrum
        spectra[f'row_{j}_physical_frequencies']=4*np.fft.fftfreq(len(spectrum),1/len(spectrum))
        raw=np.load(path,allow_pickle=False)['state']
        states.append(np.fft.fft(raw,axis=0)/len(raw))
    comparisons=[]
    for i in range(len(rows)):
        for j in range(i+1,len(rows)):
            if rows[i]['r']!=rows[j]['r']:continue
            ni,nj=len(states[i]),len(states[j]);limit=min(ni,nj)//2
            indices=np.arange(-limit+1,limit)
            difference=states[i][indices%ni]-states[j][indices%nj]
            bands={}
            for left,right in zip([0,1,4,8,16,32,64,128],[1,4,8,16,32,64,128,256]):
                right=min(right,limit)
                if left>=right:continue
                mask=(abs(indices)>=left)&(abs(indices)<right)
                bands[f'{left}:{right}']=np.sum(abs(difference[mask]),axis=0).tolist()
            comparisons.append(dict(rows=[i,j],r=rows[i]['r'],
                description='Floating coefficient differences on common physical modes; different input truncations and unvalidated histories remain.',
                common_positive_mode_max=limit-1,
                column_order=['B','C','F0','F1','F2','X0','X1','X2','Y0','Y1','Y2','nu0','nu1','nu2'],
                common_mode_difference_l1_by_column=np.sum(abs(difference),axis=0).tolist(),
                common_mode_difference_band_l1_by_column=bands))
    doc=dict(kind='floating_actual_Codazzi_cap_boundary_and_principal_form_diagnostic',certified=False,
        source_sha256=sha(__file__),object_sha256=sha(args.object),
        origin_sha256=definition['origin_inputs']['sha256'],direction_sha256=definition['direction']['sha256'],
        exact_center_parameter=definition['delta_fraction'],mean_retained=True,original_target_fixed=True,
        whole_real_angular_circle=False,whole_parameter_interval=False,whole_radial_domain=False,
        rows=rows,same_endpoint_comparisons=comparisons,dependency_sha256={s:sha(Path(__file__).with_name(s)) for s in
            ('fourfold_phase_codazzi_evolution_probe.py','fourfold_phase_local_correction_probe.py',
             'fourfold_phase_symmetric_geometry.py','fourfold_phase_geometry.py','fourfold_phase_core_low_block.py')},
        limitations=['Endpoint floating samples of finite candidates only; no exact PDE or angular/radial enclosure.',
            'Sampled rational-field DFTs are not their infinite Fourier expansions; no unobserved tail is paid.',
            'The finite-difference grounded trace is referenced to the OLD fixed-type operator, not a new Jacobi solution.',
            'Its true forcing, nonlinear terms, regular trace and regular flux remain uncomputed. No homogeneous cap DN test is claimed.',
            'Pointwise sampled form differences do not compare the complete cap or transfer any prior inverse certificate.'])
    spectra['metadata']=np.array(json.dumps(dict(kind=doc['kind'],source_sha256=doc['source_sha256'],
        fields=[r['spectrum_fields'] for r in rows],input_states=[r['state_sha256'] for r in rows])))
    memory=io.BytesIO();np.savez(memory,**spectra)
    with gzip.GzipFile(filename=str(args.spectra),mode='wb',mtime=0) as stream:stream.write(memory.getvalue())
    doc['spectrum_path']=str(args.spectra);doc['spectrum_sha256']=sha(args.spectra)
    args.out.write_text(json.dumps(doc,indent=2)+'\n')
    print([dict(r=x['r'],grid=x['angular_grid'],q=x['updated_source_C0'],
        relative_form=x['old_modified_to_new_modified']['sampled_relative_form_difference'],
        C_min=x['minimum_abs_C']) for x in rows])


if __name__=='__main__':main()
