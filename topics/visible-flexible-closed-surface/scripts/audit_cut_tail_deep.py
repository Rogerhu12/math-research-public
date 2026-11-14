#!/usr/bin/env python3
"""Independent witness on a raw-source first transition.
The raw formula is retained by the candidate only at n>=protectCell.
No cell calibration alpha enters this segment. The optional crude all-segment
bound assumes every deep calibrated alpha is in [1/2,2] and R dominates
all plateau levels; these hypotheses are not certified by this script.
"""
import argparse,gzip,json,math
from pathlib import Path
from scipy.optimize import minimize_scalar

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('input',type=Path);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args()
    with gzip.open(a.input,'rt') as f:d=json.load(f)
    p=d['parameters']
    if p['rejoinR20At'] is not None:raise ValueError('script expects unrejoined fixed source')
    rows=[]
    for n in [79,80,96,112,120,128]:
        delta=p['delta0']*2.**(-n);eta=p['etaRatioAtN0']*p['delta0']*2.**(-p['etaPower']*n)
        mu=p['epsilonScale']*delta**p['a'];after=3*delta+6*p['etaRatioAtN0']*p['delta0']*2.**(-p['etaPower']*(n+1))/(1-2.**(-p['etaPower']))
        def point(x):
            S=x*x*x*(10+x*(-15+6*x));Sp=30*x*x*(1-x)*(1-x)
            lr=math.log(p['rCuff'])+p['orientation']*(after+eta*(1+x))/math.sqrt(12)
            r=math.exp(lr);w=math.exp(math.log(mu)+(math.log(p['R'])-math.log(delta))*S-7*lr)
            wr=w*((math.log(p['R'])-math.log(delta))*Sp-7*p['orientation']*eta/math.sqrt(12))/(p['orientation']*eta*r/math.sqrt(12))
            return {'n':n,'segment':1,'x':x,'r':r,'w':w,'w_r':wr,'curvature':abs(wr)/(1+w*w)**1.5}
        opt=minimize_scalar(lambda x:-point(x)['curvature'],bounds=(.5,1),method='bounded',options={'xatol':1e-14})
        W=p['epsilonScale']*p['R']*delta**(p['a']-1)*p['rCuff']**(-7)
        bound=W*(math.sqrt(12)*(15/8)*(2*abs(math.log(delta))+math.log(128))/(eta*p['rCuff'])+7/p['rCuff'])
        rows.append({'retained_unmodified':n>=p['protectCell'],'optimized_first_transition':point(opt.x),'fixed_x_0p9':point(.9),'conditional_coarse_bound_all_raw_segments':bound})
    out={'scope':__doc__,'source_parameters':{k:p[k] for k in ['delta0','R','a','etaPower','etaRatioAtN0','epsilonScale','rCuff','orientation','protectCell']},'rows':rows}
    a.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'rows':[{'n':r['fixed_x_0p9']['n'],'fixed_x_curvature':r['fixed_x_0p9']['curvature'],'optimized_curvature':r['optimized_first_transition']['curvature'],'conditional_coarse_bound':r['conditional_coarse_bound_all_raw_segments']} for r in rows]},indent=2))
if __name__=='__main__':main()
