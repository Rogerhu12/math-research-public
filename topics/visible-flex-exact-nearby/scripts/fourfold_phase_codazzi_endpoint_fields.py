#!/usr/bin/env python3
"""Export finite B,C and Riemann-variable endpoint fields for validation work.

This postprocesses a frozen FLOATING Codazzi endpoint. B,C are upsampled as
the retained finite trigonometric polynomial. Derivatives of p=(B+k)/C and
q=(B-k)/C use the rational chain rule; they are not obtained by silently
discarding the high modes of p,q. The exported full doubled-grid spectrum
still has an uncertified infinite tail and roundoff, explicitly labelled.
"""
from __future__ import annotations

import argparse,json
from pathlib import Path
import numpy as np
from fourfold_phase_symmetric_geometry import load_exact_object
from fourfold_phase_local_correction_probe import sha,scalar_target
from fourfold_phase_codazzi_evolution_probe import Evolution,resample,scalar_derivative


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    p.add_argument('--state',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--fields',type=Path,required=True);p.add_argument('--oversample',type=int,default=2)
    args=p.parse_args();saved=np.load(args.state,allow_pickle=False)
    meta=json.loads(str(saved['metadata']))
    if meta['object_sha256']!=sha(args.object):raise ValueError('state belongs to another initial object')
    r=float(saved['r']);state=saved['state'];N=len(state);M=N*args.oversample
    geometry,definition=load_exact_object(args.object,512);target=scalar_target(geometry,r)
    if not target['K']<0:raise ValueError('real Riemann variables require strictly negative target curvature')
    evolution=Evolution(geometry,N,args.oversample)
    yd=evolution.evaluate(r,state.ravel()).reshape(N,14)
    bc=resample(state[:,:2],M);bct=scalar_derivative(bc);bctt=scalar_derivative(bct)
    bcr=resample(yd[:,:2],M);bcrt=scalar_derivative(bcr)
    B,C=bc.T;Bt,Ct=bct.T;Btt,Ctt=bctt.T;Br,Cr=bcr.T;Brt,Crt=bcrt.T
    k=np.sqrt(-target['K']);kr=target['minus_K_x']/(2*k);eta=kr/(2*k)
    c=np.sqrt(target['E'])/target['a'];h=target['a_x']/target['a']
    def riemann(sign):
        num=B+sign*k;u=num/C
        ut=Bt/C-num*Ct/C**2
        utt=Btt/C-2*Bt*Ct/C**2-num*Ctt/C**2+2*num*Ct**2/C**3
        ur=(Br+sign*kr)/C-num*Cr/C**2
        urt=Brt/C-(Br+sign*kr)*Ct/C**2-Bt*Cr/C**2-num*Crt/C**2+2*num*Cr*Ct/C**3
        return u,ut,utt,ur,urt
    P,Pt,Ptt,Pr,Prt=riemann(1);Q,Qt,Qtt,Qr,Qrt=riemann(-1)
    RP=Pr-c*Q*Pt+h*Q*(1+P**2)-eta*(P-Q)
    RQ=Qr-c*P*Qt+h*P*(1+Q**2)+eta*(P-Q)
    RPt=Prt-c*(Qt*Pt+Q*Ptt)+h*(Qt*(1+P**2)+2*Q*P*Pt)-eta*(Pt-Qt)
    RQt=Qrt-c*(Pt*Qt+P*Qtt)+h*(Pt*(1+Q**2)+2*P*Q*Qt)+eta*(Pt-Qt)
    names=['B','C','B_theta','C_theta','B_thetatheta','C_thetatheta','p','q','p_theta','q_theta','p_thetatheta','q_thetatheta','R_p','R_q','R_p_theta','R_q_theta']
    values=np.stack([B,C,Bt,Ct,Btt,Ctt,P,Q,Pt,Qt,Ptt,Qtt,RP,RQ,RPt,RQt],axis=1)
    coeff=np.fft.fft(values,axis=0)/M
    frequency=4*np.fft.fftfreq(M,1/M).astype(int)
    base_coeff=np.fft.fft(state[:,:2],axis=0)/N
    # Choose and save an exactly Hermitian dyadic reference for B,C. The
    # discrepancy from the floating state is reported, not discarded.
    chosen=base_coeff.copy();chosen[0]=chosen[0].real;chosen[N//2]=0
    for j in range(1,N//2):
        value=(base_coeff[j]+np.conj(base_coeff[-j]))/2
        chosen[j]=value;chosen[-j]=np.conj(value)
    choice_fee=float(np.sum(abs(chosen-base_coeff)))
    metadata=dict(kind='floating_Codazzi_Riemann_endpoint_fields',certified=False,r=r,
        base_angular_grid=N,spectral_grid=M,source_sha256=sha(__file__),input_state_sha256=sha(args.state),
        object_sha256=sha(args.object),base_columns=['B','C'],
        coefficient_contract='base_BC_coefficients are an exactly Hermitian dyadic chosen finite reference; full_spectrum contains sampled floating spectra of the listed rational fields, not certified tail bounds')
    np.savez_compressed(args.fields,physical_frequency=frequency,columns=np.array(names),
        full_spectrum=coeff,base_BC_coefficients=chosen,metadata=np.array(json.dumps(metadata)))
    ranges={name:dict(minimum=float(np.min(values[:,i])),maximum=float(np.max(values[:,i])),
        sampled_C0=float(np.max(abs(values[:,i]))),finite_coefficient_l1=float(np.sum(abs(coeff[:,i])))) for i,name in enumerate(names)}
    doc=dict(**metadata,initial_definition=definition['delta_fraction'],
        origin_sha256=definition['origin_inputs']['sha256'],direction_sha256=definition['direction']['sha256'],
        target={key:target[key] for key in ('E','E_x','a','a_x','K','minus_K_x')},
        k=k,k_r=kr,k_r_over_2k=eta,transport_factor=c,radial_log_radius=h,
        minimum_abs_C=float(np.min(abs(C))),Hermitian_reference_finite_l1_difference=choice_fee,
        fields=ranges,spectrum_path=str(args.fields),spectrum_sha256=sha(args.fields),
        dependency_sha256={s:sha(Path(__file__).with_name(s)) for s in ('fourfold_phase_codazzi_evolution_probe.py','fourfold_phase_local_correction_probe.py','fourfold_phase_symmetric_geometry.py','fourfold_phase_geometry.py')},
        limitations=['Only one radial endpoint and the center affine parameter are processed.',
            'B,C references are finite; p,q are rational functions with unbounded Fourier support. The exported doubled-grid spectra do not certify their infinite tails.',
            'Residuals use the semidiscrete RHS, not a validated radial interpolant; temporal integration error is not bounded.',
            'All norms/ranges are sampled floating diagnostics, not directed enclosures.'])
    args.out.write_text(json.dumps(doc,indent=2)+'\n')
    print({'r':r,'grid':N,'minC':doc['minimum_abs_C'],'k':k,'kr_over_2k':eta,
           'norms':{key:ranges[key]['sampled_C0'] for key in ('p','q','p_theta','q_theta','p_thetatheta','q_thetatheta','R_p','R_q','R_p_theta','R_q_theta')},
           'fields_bytes':args.fields.stat().st_size},flush=True)


if __name__=='__main__':main()
