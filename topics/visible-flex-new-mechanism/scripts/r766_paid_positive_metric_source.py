"""Actual new R766 exact-source and curvature-field initialization."""
from pathlib import Path
import base64
import hashlib
import io
import json
import os
import numpy as np
import scipy
from r728_closed_spinor_continuation_20261128 import PaidBook
from r738_real_macro_reference import Base
from r761_unrestricted_frame_and_solid import dot
from r766_codazzi_physical_rows import Field
from r764_positive_slope_material import geometry

class Book(PaidBook):
    def __init__(self,req,opt,limit,elapsed,counts):
        self.hashlib,self.os,self.elapsed,self.counts=hashlib,os,elapsed,counts
        self.limit,self.reserve=limit,opt['reserve_seconds']
        self.root=Path(os.environ['RUNNER_TEMP'])/'r766-paid';self.root.mkdir(exist_ok=True)
        self.ledger_file=self.root/'ledger.json'
        semantic=dict(schema='r766-Gauss-Codazzi-positive-material-v1',sources={k:v for k,v in req['source_sha256'].items() if k.endswith('.py')},
                     geometry=opt,calibration='bf12e73ac01668167581f3a4037d115a226984555ca1c80dc146ee7239f14b73',runtime=[np.__version__,scipy.__version__])
        fid=hashlib.sha256(json.dumps(semantic,sort_keys=True,separators=(',',':')).encode()).hexdigest()
        if self.ledger_file.exists():
            self.ledger=json.loads(self.ledger_file.read_bytes())
            if self.ledger['fingerprint']!=fid:raise ValueError('Paid whole-material height identity changed.')
            counts.update(self.ledger['counts'])
        else:self.ledger=dict(schema=semantic['schema'],fingerprint=fid,semantic=semantic,kept={},retired={},counts={},
                unit_max_seconds={},runs=[],cumulative_seconds=0.,latest_state=None,pending=None,context={})
        self.prior_seconds=self.ledger['cumulative_seconds']
        self.ledger['runs'].append(dict(id=os.environ['GITHUB_RUN_ID'],source=os.environ['GITHUB_SHA'],
                                   attempt=os.environ.get('GITHUB_RUN_ATTEMPT')))
        self.flush()


class OriginalCalibration:
    def __init__(self,record):self.record=record
    def once(self,key,fn):
        if key!='r738_angular_calibration_64':raise ValueError('Only the completed 64-point R738 calibration is shared.')
        return self.record


def actual_source(opt,book,count,sp):
    name=Path(__file__).resolve().parent.parent/'computations'/'r764-r738-source-angular64.json'
    meta=json.loads(name.read_bytes());raw=base64.b64decode(meta['base64'],validate=True)
    if (meta['name']!='r738_angular_calibration_64.npz' or len(raw)!=610 or
        hashlib.sha256(raw).hexdigest()!='bf12e73ac01668167581f3a4037d115a226984555ca1c80dc146ee7239f14b73'):
        raise ValueError('Invalid original angular R738 calibration.')
    with np.load(io.BytesIO(raw),allow_pickle=False) as data:
        old=json.loads(data['meta'].tobytes());k=old['right']['@array'];right=np.asarray(data[k]).copy()
    base=Base(64,OriginalCalibration(dict(M=old['M'],right=right)),count)
    g=Field(book,base,opt,opt['stages'][0],opt['initial_projection_detail'],sp)
    def project():
        rr=g.r[:,None,None];m=g.frame.original.mat['m'][:,None];kap=g.frame.original.mat['kap'][:,None]
        reports={};target=None
        for phase in (0,1):
            geo=geometry(base,g.r,g.phi,phase);F,D,H,DD,DH,HH=geo['six'];nr=D.shape[0]
            T=H/rr;N=np.cross(D,T);N/=np.linalg.norm(N,axis=-1)[...,None];P=D/np.linalg.norm(D,axis=-1)[...,None]
            # Genuine shape pair of the geometric seed (its own positive definite first form).
            k=dot(HH/rr,N);ell=dot(DH,N)/np.linalg.norm(D,axis=-1)
            defect=[dot(D,D)/m**2-1,dot(D,T)/m,dot(T,T)-1]
            reports[str(phase)]=dict(center=geo['actual_relative_center'],max_three_Gram=[float(abs(t).max()) for t in defect],
                minmax_k=[float(k.min()),float(k.max())],minmax_ell=[float(ell.min()),float(ell.max())],radii=len(g.r),angles=len(g.phi),
                unresolved_deep_primitive_abs=geo['unresolved_deep_primitive_absolute_bound'])
            if phase:
                from r764_positive_slope_material import material
                z=material(base,g.r);W=z['W'][:,None];weight=g.width*g.r*m[:,0];weight/=weight.sum()
                high=np.zeros_like(g.r)
                for center in (.085,.21):high+=.013*np.maximum(0.,1-((g.r-center)/.0045)**2)**6
                match=k+high[:,None]
                # The genuine positive regularization at the internally flat reference circles changes k.
                # In the constant-angle tail the real k equals W/m exactly, even where evaluation loses digits.
                outside=((g.r<=.085)|(g.r>=.21))[:,None]
                match=np.where(outside,kap,match)
                if np.any(match[1:-1]<=0):raise FloatingPointError('Tilted reference lost its genuine positive k chart.')
                u=np.zeros_like(k);v=np.zeros_like(k);u[1:-1]=np.log(match[1:-1]/kap[1:-1]);v[1:-1]=np.where(outside[1:-1],0.,ell[1:-1]/match[1:-1]);target=(u,v)
            count['new_R764_true_geometric_six_fields']+=1
        # Kronecker factorization is exactly the full physical least squares for both scalar fields.
        # Radial and angular factors are unpivoted SVDs. All their product singular directions are retained.
        b=g.frame.original.b;angular=g.frame.original.angular[0];w=np.sqrt(weight);n=np.sqrt(len(g.phi))
        ur,sr,vr=np.linalg.svd(b*w[:,None],full_matrices=False);ua,sa,va=np.linalg.svd(angular/n,full_matrices=False)
        if min(sr.min(),sa.min())<=0:raise FloatingPointError('Initial physical chart factors are singular on this grid.')
        co=[];costs=[]
        for y in target:
            coef=vr.T@((ur.T@(y*w[:,None])@ua/n)/(sr[:,None]*sa[None,:]))@va
            co.append(coef);costs.append(float(np.linalg.norm((b@coef@angular.T-y)*w[:,None]/n)))
        x=np.r_[reports['1']['center'],np.array(co).ravel()]
        count['new_full_rank_curvature_projections']+=1
        return dict(x=x,source_reference_and_actual_six=reports,radial_singular=sr,angular_singular=sa,
                    all_product_singular_values=sr[:,None]*sa[None,:],all_projected_curvature_columns=2*len(sr)*len(sa),
                    centers=3,weighted_target_fit_errors=costs,reference_and_new_material='R764-positive-cutoff',
                    R748_or_R762_operators_replayed=0,continuous_root_established=False)
    return base,book.once('R766_genuine_R764_reference_and_all_field_projection','source',project)
