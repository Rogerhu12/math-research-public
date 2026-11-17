"""Exact half-step knot insertion, leaving the represented geometry unchanged."""
import argparse,json,numpy as np
from scipy.interpolate import BSpline
from negative_entry_cap_base import Model
ap=argparse.ArgumentParser();ap.add_argument('--source',required=True);ap.add_argument('--out',required=True);a=ap.parse_args();d=json.load(open(a.source));p=d['parameters'];old=Model(**{k:p[k]for k in ['B','height','speed','rc','nc','m','bend']});q=np.array(d['q']).reshape(old.shape);full=np.zeros((old.nc,q.shape[1]));full[3:-3]=q;spline=BSpline(old.spline.t,full,5)
for left,right in zip(old.intervals[:-1],old.intervals[1:]):spline=spline.insert_knot((left+right)/2)
newnc=len(spline.c);newp=p.copy();newp['nc']=newnc;qnew=spline.c[3:-3]
out={'q':qnew.ravel().tolist(),'parameters':newp,'source':a.source,'exact_knot_insertion':True,'new_nc':newnc};json.dump(out,open(a.out,'w'))
print('refined nc',old.nc,'->',newnc)
