#!/usr/bin/env python3
"""Fit a complete new R201 field to the actual normalized warm position.
All arrays remain outside Git. The fit itself is neither an LM acceptance nor
a metric certificate. It fits both values and physical first radial jets.
"""
import argparse, hashlib, json
from pathlib import Path
import numpy as np

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def main():
    p=argparse.ArgumentParser();p.add_argument('warm');p.add_argument('reference');p.add_argument('out')
    p.add_argument('--derivative-weight',type=float,default=.03)
    p.add_argument('--fit-radius',action='store_true',help='Explicit new design: fit complete rho values and physical first jets')
    a=p.parse_args();out=Path(a.out)
    if out.exists(): raise FileExistsError(out)
    raw=np.load(a.warm);ref=json.loads(Path(a.reference).read_text());u=np.asarray(ref['u'])
    s=np.asarray([r['s'] for r in ref['rows']]);idx=np.asarray([int(np.argmin(abs(raw['s']-v))) for v in s])
    if np.max(abs(raw['s'][idx]-s))>1e-13 or np.max(abs(raw['u']-u))>1e-14:raise ValueError('Same actual sample grid required')
    f=raw['f'][idx];fs=raw['fs'][idx];T=raw['Xu'][idx]/f[:,None,None]
    Ts=(raw['Xsu'][idx]-fs[:,None,None]*T)/f[:,None,None]
    cp2=T[:,:,0]**2+T[:,:,1]**2
    if np.min(cp2)<.1:raise ValueError('Angle chart too close to pole')
    th=np.arctan2(-T[:,:,0],T[:,:,1]);ph=np.arcsin(np.clip(T[:,:,2],-1,1))
    ths=(T[:,:,0]*Ts[:,:,1]-T[:,:,1]*Ts[:,:,0])/cp2;phs=Ts[:,:,2]/np.sqrt(cp2)
    old=np.asarray([r['angles'] for r in ref['rows']]);dth=np.angle(np.exp(1j*(th-old[:,:,0])))
    dph=ph-old[:,:,1];dths=ths-old[:,:,2];dphs=phs-old[:,:,3]
    B=np.asarray([r['B'] for r in ref['rows']]);Bs=np.asarray([r['Bs'] for r in ref['rows']])
    J=B.shape[1];K=ref['input']['options']['modes'];N=len(u);w=a.derivative_weight
    if not(w>0 and np.isfinite(w)):raise ValueError('Positive physical derivative fit weight required')
    # Trapezoidal radial weights retain every real warm row; endpoints have
    # zero basis jets and therefore cannot silently change the actual ports.
    ds=np.empty(len(s));ds[0]=(s[1]-s[0])/2;ds[-1]=(s[-1]-s[-2])/2;ds[1:-1]=(s[2:]-s[:-2])/2
    W=np.sqrt(ds/(s[-1]-s[0]));M=np.vstack([B*W[:,None],w*Bs*W[:,None]])
    def fit(v,d):return np.linalg.lstsq(M,np.concatenate([v*W,w*d*W]),rcond=1e-13)[0]
    z=np.asarray(ref['zero']);legacy=ref['legacyDimension'];width=2*K+1
    for k in range(K):
        sn=np.sin(2*(k+1)*u);cs=np.cos(2*(k+1)*u)
        z[np.arange(J)*K+k]=fit(2*dth@sn/N,2*dths@sn/N)
        z[J*K+np.arange(J)*K+k]=fit(2*dph@sn/N,2*dphs@sn/N)
        z[legacy+np.arange(J)*width+1+k]=fit(2*dth@cs/N,2*dths@cs/N)
        z[legacy+np.arange(J)*width+1+K+k]=fit(2*dph@cs/N,2*dphs@cs/N)
    z[legacy+np.arange(J)*width]=fit(dth.mean(axis=1),dths.mean(axis=1))
    # Constant phi is a phase gauge removed by the exact mean-phase rotation.
    hz=raw['X'][idx,:,2].mean(axis=1)-np.asarray([r['meanZ'] for r in ref['rows']])
    hzs=raw['Xs'][idx,:,2].mean(axis=1)-np.asarray([r['meanZs'] for r in ref['rows']])
    z[2*J*K:2*J*K+J]=fit(hz,hzs)
    if a.fit_radius:
        rho=f-np.asarray([r['f'] for r in ref['rows']])
        rhos=fs-np.asarray([r['fs'] for r in ref['rows']])
        z[legacy-J:legacy]=fit(rho,rhos)
        if np.max(abs(z[legacy-J:legacy]))>ref['input']['options'].get('radiusCoefficientBound',.4):
            raise ValueError('Complete fitted rho coefficients exceed the explicitly declared domain')
    state=ref['input'];state.update(schema='6a65-Cauchy-global-position-initial-v1',z=z.tolist(),cauchyAcceptedSteps=0,accepted=False,
        warmFit={'schema':'6a65-full-theta-phi-height-first-jet-LS-fit-v1','warmSHA256':sha(a.warm),'referenceSHA256':sha(a.reference),
        'entrySHA256':sha(__file__),'samples':len(s),'angles':N,'dimension':len(z),'modes':K,'radialBasisCount':J,
        'physicalDerivativeWeight':w,'linearFitRank':int(np.linalg.matrix_rank(M)),'zeroRadiusInitial':not a.fit_radius,
        'completeRadiusFirstJetFit':a.fit_radius,'maxAbsoluteRadiusCoefficient':float(abs(z[legacy-J:legacy]).max()),
        'resultingMetric':'finite base plus fitted rho; fitting the target perimeter is an explicit new physical metric design' if a.fit_radius else 'original new base with zero rho',
        'cutAndAmplitudeUnchanged':bool(z[ref['cutHeightIndex']]==ref['zero'][ref['cutHeightIndex']] and z[ref['amplitudeIndex']]==ref['zero'][ref['amplitudeIndex']]),
        'maxAbsoluteCoefficient':float(abs(z).max()),'fitNotMetricCertificate':True},
        physicalMetricStillADesignVariable=True,continuousCertificate=False,strongTargetComplete=False)
    out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(state,separators=(',',':'))+'\n')
    print(json.dumps({'outputSHA256':sha(out),**state['warmFit']}))

if __name__=='__main__':main()
