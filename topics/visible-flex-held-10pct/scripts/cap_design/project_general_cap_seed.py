"""Reproduce the full-angle m6 seed from the symmetric m6 negative-entry run."""
import argparse,json
import numpy as np
ap=argparse.ArgumentParser();ap.add_argument('--source',default='design_B065_h080_negative_entry.json');ap.add_argument('--out',required=True);ap.add_argument('--seed',type=int,default=917);ap.add_argument('--amplitude',type=float,default=5e-5);a=ap.parse_args()
d=json.load(open(a.source));p=d['parameters'];assert p['m']==6
old=np.array(d['q']).reshape(p['nc']-6,18);new=np.random.default_rng(a.seed).normal(size=(p['nc']-6,39))*a.amplitude
for f in [1,3,5]:new[:,2*f-1]=old[:,(f-1)//2];new[:,13+2*f]=old[:,6+(f-1)//2]
for f in [0,2,4,6]:new[:,26+(2*f-1 if f else 0)]=old[:,12+f//2]
out=dict(q=new.ravel().tolist(),source=a.source,seed=a.seed,extra_amplitude=a.amplitude)
json.dump(out,open(a.out,'w'))
