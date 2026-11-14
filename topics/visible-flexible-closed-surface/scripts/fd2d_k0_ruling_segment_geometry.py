#!/usr/bin/env python3
"""R137 line-segment geometry on the whole radial coast, at supplied angles.

Sphere/slab/held and own-normal support extrema are algebraic in the ruling
coordinate.  No radial grid is used.  Angular sampling is explicitly kept
separate from continuous angular certification.
"""
from __future__ import annotations
import argparse,hashlib,json,time
from pathlib import Path
import numpy as np
from fd2d_k0_ruling_coast import ruling_coordinates
from fd2d_peak_spacer_ruling_consumer import SpectralInlet
from fd2d_balanced_curvature_core import FixedBalancedGeometry


def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def col(v):return np.asarray(v)[...,None]


def segment_geometry(a,v,L,inlet,held_point):
    n,m=inlet['n'],inlet['m'];nu,mu=inlet['n_u'],inlet['m_u']
    k=m/n;ku=mu/n-m*nu/(n*n)
    kuu=inlet['m_uu']/n-m*inlet['n_uu']/(n*n)-2*mu*nu/(n*n)+2*m*nu*nu/(n*n*n)
    coordinates=ruling_coordinates(a,v,L,k,ku,kuu);W=coordinates['w']
    X=inlet['X'];G=inlet['e1']-col(k)*inlet['e2']
    Gt=inlet['e1_u']-col(ku)*inlet['e2']-col(k)*inlet['e2_u']
    endpoint=X+col(W)*G;delta=X-np.asarray(held_point)
    ww=np.clip(-np.sum(delta*G,axis=-1)/np.sum(G*G,axis=-1),0,W)
    held_position=X+col(ww)*G
    C0=np.cross(G,inlet['X_u']);C1=np.cross(G,Gt)
    AA=-np.sum(X*C0,axis=-1);BB=-np.sum(X*C1,axis=-1)
    CC=np.sum(C0*C0,axis=-1);DD=np.sum(C0*C1,axis=-1);EE=np.sum(C1*C1,axis=-1)
    critical=np.divide(AA*DD-BB*CC,BB*DD-AA*EE,out=np.zeros_like(W),where=(BB*DD-AA*EE)!=0)
    has_critical=(critical>0)&(critical<W)
    critical=np.where(has_critical,critical,0)
    def support(w):
        normal=C0+col(w)*C1
        return -np.sum(X*normal,axis=-1)/np.linalg.norm(normal,axis=-1)
    s0,s1,sc=support(np.zeros_like(W)),support(W),support(critical)
    support_values=np.stack((s0,s1,np.where(has_critical,sc,np.inf)),axis=-1)
    chosen=np.argmin(support_values,axis=-1)
    support_w=np.where(chosen==0,0,np.where(chosen==1,W,critical))
    area_w=np.clip(np.divide(-DD,EE,out=np.zeros_like(W),where=EE!=0),0,W)
    area_min=np.linalg.norm(C0+col(area_w)*C1,axis=-1)
    return dict(W=W,D_end=coordinates['D'],material_end=inlet['u']+coordinates['material_shift'],
        sphere_radius_upper=np.maximum(np.linalg.norm(X,axis=-1),np.linalg.norm(endpoint,axis=-1)),
        abs_y_upper=np.maximum(abs(X[...,1]),abs(endpoint[...,1])),
        z_lower=np.minimum(X[...,2],endpoint[...,2]),z_upper=np.maximum(X[...,2],endpoint[...,2]),
        held_distance_lower=np.linalg.norm(held_position-np.asarray(held_point),axis=-1),
        held_minimizer_w=ww,held_minimizer_X=held_position,
        own_support_lower=np.min(support_values,axis=-1),own_support_minimizer_w=support_w,
        own_ruling_area_lower=area_min,own_ruling_area_minimizer_w=area_w,
        X_start=X,X_end=endpoint,ruling_direction=G)


def main():
    ap=argparse.ArgumentParser(description=__doc__);root=Path(__file__).resolve().parent.parent
    ap.add_argument('--inlet',type=Path,default=root/'notes/2026-11-12-fd2d-peak-spacer-ruling-consumer-01-inlet.npz')
    ap.add_argument('--angles',type=int,default=3072);ap.add_argument('--stem',type=Path,required=True)
    args=ap.parse_args()
    if list(args.stem.parent.glob(args.stem.name+'*')):raise FileExistsError('Use a new output stem')
    started=time.monotonic();p=np.load(args.inlet,allow_pickle=False);geometry=FixedBalancedGeometry()
    inlet=SpectralInlet(p['frame_fourier'],p['n_phi_cos'],p['m_phi_sin'],p['frequencies'],geometry)
    phi=np.arange(args.angles,dtype=np.longdouble)*(2*np.arccos(np.longdouble(-1))/args.angles)
    data=inlet.at_phi(phi);a,v,L=(float(p[k]) for k in ('a','v','coast_length'))
    held=np.array([0,float(geometry.A),0]);out=segment_geometry(a,v,L,data,held)
    summary={key:float(np.max(out[key])) for key in ('sphere_radius_upper','abs_y_upper','z_upper')}
    summary.update({key:float(np.min(out[key])) for key in ('D_end','z_lower','held_distance_lower','own_support_lower','own_ruling_area_lower')})
    locations={}
    for key,maximize in (('held_distance_lower',False),('own_support_lower',False),('sphere_radius_upper',True),('abs_y_upper',True)):
        j=int(np.argmax(out[key]) if maximize else np.argmin(out[key]))
        locations[key]=dict(index=j,phi=float(phi[j]),material_inlet=float(data['u'][j]),value=float(out[key][j]),
            W=float(out['W'][j]),held_minimizer_w=float(out['held_minimizer_w'][j]),
            own_support_minimizer_w=float(out['own_support_minimizer_w'][j]),
            X_start=np.asarray(out['X_start'][j],float).tolist(),X_end=np.asarray(out['X_end'][j],float).tolist())
    arrays=args.stem.with_name(args.stem.name+'-angles.npz')
    np.savez_compressed(arrays,phi=np.asarray(phi,float),material_u=np.asarray(data['u'],float),
        **{key:np.asarray(val,float) for key,val in out.items()},inlet_sha256=digest(args.inlet))
    report=dict(schema='fd2d-r137-complete-radial-segment-geometry-v1',actual_execution=True,
        source_sha256=digest(__file__),inlet_sha256=digest(args.inlet),
        dependencies={name:digest(root/'scripts'/name) for name in ('fd2d_k0_ruling_coast.py',
            'fd2d_peak_spacer_ruling_consumer.py','fd2d_balanced_curvature_core.py')},
        a=a,v=v,coast_length=L,held_point=held.tolist(),angles=args.angles,
        radial_grid_used=False,radial_extrema_method='Endpoints for convex norm/slab, clipped quadratic vertex for held and area, endpoints plus the unique possible critical point for own-normal support',
        summary=summary,locations=locations,arrays_file=arrays.name,arrays_sha256=digest(arrays),
        continuous_angular_bounds=False,rounding_enclosures=False,reach_certificate=False,
        seconds=time.monotonic()-started)
    path=args.stem.with_name(args.stem.name+'-report.json');path.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(report=str(path),sha256=digest(path),summary=summary,seconds=report['seconds']),allow_nan=False))


if __name__=='__main__':main()
