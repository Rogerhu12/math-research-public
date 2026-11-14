#!/usr/bin/env python3
"""Floating stable evaluation of the fixed target's rotational reference.

This finite primitive evaluator is restricted to the actual frozen body
0<=r<=3. It never extrapolates the splines into the graft. Radius powers
are cancelled before E-a_r^2, K and the rotational curvatures are formed.
No interval/full-tail certification is asserted by this diagnostic producer.
"""
from __future__ import annotations
import argparse,gzip,json,time
from pathlib import Path
import numpy as np
from fourfold_phase_symmetric_geometry import load_exact_object
from fourfold_phase_geometry import tangent_radial_jets
from fourfold_phase_local_correction_probe import sha,scalar_target


def primitive_difference(geometry,phase):
    tangent,aux=tangent_radial_jets(phase,geometry.sine)
    b,g=aux['fields'][0,...,0],aux['fields'][0,...,1]
    bm=-2*np.sin(b/2)**2;gm=-2*np.sin(g/2)**2
    tangent[0,...,1]=bm+gm+bm*gm
    n=geometry.nodes;f=geometry.frequency
    c=np.fft.fft(tangent,axis=2)/n;p=np.zeros_like(c)
    d=(1-f*f)[None,None,:];ii=(1j*f)[None,None,:]
    p[...,0]=(ii*c[...,0]+c[...,1])/d
    p[...,1]=(-c[...,0]+ii*c[...,1])/d
    nz=np.flatnonzero(f);p[:,:,nz,2]=c[:,:,nz,2]/(1j*f[nz])[None,None,:]
    p[:,:,n//2,:]=0;p[:,:,0,1:]=0
    pos=np.arange(1,n//2)
    for j,parity in enumerate((1,-1,1)):
        z=(p[:,:,pos,j]+parity*p[:,:,-pos,j])/2
        p[:,:,pos,j]=z;p[:,:,-pos,j]=parity*z
    return p


class RotationalBodyTarget:
    def __init__(self,geometry):self.geometry=geometry

    def values(self,r):
        r=np.atleast_1d(np.asarray(r,dtype=float))
        if np.any(r<0) or np.any(r>3):raise ValueError('body target extrapolation is forbidden')
        q=self.geometry.profile_jets(r,2);p=primitive_difference(self.geometry,q['phase'])
        mean=q['mean'];a,ar,arr=mean[:3,:,0];zr,zrr=mean[1:3,:,2]
        L=ar/a;Lp=(a*arr-ar*ar)/(a*a)
        H=zr/(a*a);Hp=(a*zrr-2*ar*zr)/(a*a*a)
        u=L[:,None,None]*p[0]+p[1]
        ur=Lp[:,None,None]*p[0]+L[:,None,None]*p[1]+p[2]
        rev=(-np.arange(self.geometry.nodes))%self.geometry.nodes
        ebar=(2*L*u[:,0,0]+np.sum(u*u[:,rev,:],axis=(1,2))).real
        ebar_r=(2*Lp*u[:,0,0]+2*L*ur[:,0,0]
            +2*np.sum(u*ur[:,rev,:],axis=(1,2))).real
        Ebar=L*L+a*a*H*H+ebar
        R=H*H+ebar/(a*a)
        K=(H*H*(L*L-Lp)+L*H*Hp+(L*ebar_r-2*Lp*ebar)/(2*a*a))/(Ebar*Ebar)
        if not np.all(np.isfinite(Ebar)) or np.any(Ebar<=0) or np.any(R<=0):
            raise ValueError('floating rotational target chart failed')
        gamma=np.sqrt(Ebar);C=-np.sqrt(R)/gamma;A=K/C
        return dict(r=r,a=a,a_r=ar,a_rr=arr,E=a*a*Ebar,Ebar=Ebar,E_minus_a_r_squared=a**4*R,
            normalized_E_minus_a_r_squared=R,K=K,gamma=gamma,beta=L,
            Cref=C,Aref=A,lambda_ref=K/(C*C),a_s=L/gamma,
            primitive_mean_correction=ebar,primitive_mean_correction_r=ebar_r,
            height_slope_ratio=H,height_slope_ratio_r=Hp)

    def point(self,r):return {k:float(v[0]) for k,v in self.values([r]).items()}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--primitive-nodes',type=int,default=512)
    ap.add_argument('--endpoint',type=Path,nargs='+',default=[
        Path('notes/2026-11-13-codazzi-evolution-r0235-n1024-endpoint-floating.npz'),
        Path('notes/2026-11-13-codazzi-to-r0239-n1024-endpoint-floating.npz')])
    ap.add_argument('--out',type=Path,required=True);ap.add_argument('--spectrum',type=Path,required=True)
    a=ap.parse_args();started=time.monotonic()
    if a.out.exists() or a.spectrum.exists():raise FileExistsError('refusing to overwrite a diagnostic')
    geometry,definition=load_exact_object(a.object,a.primitive_nodes);target=RotationalBodyTarget(geometry)
    sample=[0.,.235,.239,.25,.5,.75,1.,1.5,2.,2.5,3.]
    body=[]
    for x in sample:
        t=target.point(x);old=scalar_target(geometry,x)
        body.append(dict(**t,direct_float_K=old['K'],direct_minus_stable_K=old['K']-t['K'],
            direct_float_E=old['E'],direct_minus_stable_E=old['E']-t['E']))
    endpoints=[];spectra={}
    for i,path in enumerate(a.endpoint):
        saved=np.load(path,allow_pickle=False);meta=json.loads(str(saved['metadata']))
        if meta['object_sha256']!=sha(a.object):raise ValueError('endpoint uses another fixed target')
        r=float(saved['r']);state=saved['state'];t=target.point(r)
        B,C=state[:,0],state[:,1];A=(t['K']+B*B)/C
        delta=np.column_stack([B,C-t['Cref'],A-t['Aref']])
        coeff=np.fft.fft(delta,axis=0)/len(delta);freq=4*np.fft.fftfreq(len(delta),1/len(delta))
        nonlinear=A-t['Aref']+t['lambda_ref']*(C-t['Cref'])
        algebra=B*B/C+t['K']*(C-t['Cref'])**2/(C*t['Cref']**2)
        row=dict(input_path=str(path),input_sha256=sha(path),input_metadata=meta,target=t,angular_nodes=len(B),
            B_range=[float(B.min()),float(B.max())],C_range=[float(C.min()),float(C.max())],A_range=[float(A.min()),float(A.max())],
            sampled_sup_B=float(np.max(abs(B))),sampled_sup_C_minus_Cref=float(np.max(abs(delta[:,1]))),
            sampled_sup_A_minus_Aref=float(np.max(abs(delta[:,2]))),
            sampled_relative_C_difference=float(np.max(abs(delta[:,1]))/abs(t['Cref'])),
            B_mean=float(np.mean(B)),C_mean=float(np.mean(C)),C_mean_minus_Cref=float(np.mean(C)-t['Cref']),
            finite_DFT_l1_B_C_A=np.sum(abs(coeff),axis=0).tolist(),
            nonlinear_A_remainder_sampled=float(np.max(abs(nonlinear))),
            exact_quadratic_identity_roundoff=float(np.max(abs(nonlinear-algebra))),
            low_four_B_sine=(-2*coeff[1:5,0].imag).tolist(),
            low_four_C_difference_cosine=(2*coeff[1:5,1].real).tolist(),
            scope='Floating finite endpoint only; no exact branch trace or whole-circle certificate is inferred.')
        endpoints.append(row);spectra['physical_frequency_'+str(i)]=freq;spectra['delta_B_C_A_coefficients_'+str(i)]=coeff
    spectra['metadata']=np.array(json.dumps(dict(kind='floating_Codazzi_vs_true_target_rotational_reference_spectra',
        source_sha256=sha(__file__),object_sha256=sha(a.object),endpoints=[x['input_sha256'] for x in endpoints])))
    import io
    b=io.BytesIO();np.savez_compressed(b,**spectra);a.spectrum.write_bytes(gzip.compress(b.getvalue(),mtime=0))
    report=dict(kind='floating_stable_fixed_target_rotational_Codazzi_reference',certified=False,
        source_sha256=sha(__file__),object_sha256=sha(a.object),primitive_nodes=a.primitive_nodes,
        exact_center_parameter=definition['delta_fraction'],origin_sha256=definition['origin_inputs']['sha256'],
        direction_sha256=definition['direction']['sha256'],body_samples=body,endpoints=endpoints,
        spectrum_path=str(a.spectrum),spectrum_sha256=sha(a.spectrum),
        body_domain=['0','3'],graft_extrapolation_forbidden=True,
        rotational_identities=dict(Cref='-sqrt(E-a_r^2)/(a sqrt(E))',B_ref='0',Aref='K/Cref',
            exact_height_derivative='sqrt(E-a_r^2)',
            Jacobi_matrix='[[-2 beta, gamma m lambda],[gamma m,-beta(lambda+1)]], lambda=K/Cref^2'),
        whole_parameter_interval=False,whole_radial_interval=False,whole_real_angular_circle=False,
        limitations=['Finite primitive and floating arithmetic; every displayed bound is diagnostic.',
            'The rotational formula is exact when E-a_r^2>0, but the point list does not certify that inequality on the full body.',
            'No Robin condition, full cap, mean/regular matching or nonlinear closure is solved here.'],
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in
            ('fourfold_phase_symmetric_geometry.py','fourfold_phase_geometry.py','fourfold_phase_local_correction_probe.py')},
        wall_seconds=time.monotonic()-started)
    a.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(dict(endpoints=[{k:q[k] for k in ('sampled_sup_B','sampled_sup_C_minus_Cref','sampled_relative_C_difference','nonlinear_A_remainder_sampled')} for q in endpoints],out=str(a.out)),flush=True)


if __name__=='__main__':main()
