"""Reproduce the radial projection used before the ninth-degree design test."""
import argparse,json,numpy as np
from gauged_cap_homotopy_base import Model as Old
from ninth_cap_base import Model as New
p=argparse.ArgumentParser();p.add_argument('--source',required=True);p.add_argument('--out',required=True);p.add_argument('--nc',type=int,default=22);a=p.parse_args()
d=json.load(open(a.source));args={k:d['parameters'][k]for k in ['B','height','speed','rc','nc','m']};old=Old(**args);args['nc']=a.nc;new=New(**args);s=np.linspace(0,1,501)
co=np.array(d['q']).reshape(old.shape);q=np.linalg.lstsq(new.radial(s)[0],old.radial(s)[0]@co,rcond=None)[0]
json.dump({'q':q.ravel().tolist(),'projection_source':a.source,'parameters':args},open(a.out,'w'))
