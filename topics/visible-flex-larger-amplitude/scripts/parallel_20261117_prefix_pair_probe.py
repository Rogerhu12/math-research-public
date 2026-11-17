#!/usr/bin/env python3
"""Literal normal-chord point-cloud diagnostic of one reflected C2 prefix.

The unique quintics match the actual common nodal 0/1/2 jets. Both reflected
halves are sampled; coincident copies of the central circle are omitted.
All point-cloud pairs within the specified distance are inspected in bounded
memory. More distant pairs have Q >= distance/2. This is NOT a continuous
reach certificate and does not close the two boundary circles.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import time
import numpy as np
from scipy.spatial import cKDTree
from parallel_20261117_frenet_symbol import Frenet
from parallel_20261117_profile import Profile


def main(args):
    started=time.perf_counter();raw=args.input.read_bytes()
    data=json.loads(gzip.decompress(raw))
    if not data.get('success'):raise ValueError('Actual accepted input required')
    if data.get('radial_growth_scale',1.)!=1.:raise ValueError('Use a matching growth-profile reader')
    q=Frenet(data['M'],args.angles);old=Frenet(data['M'],data['N'])
    profile=Profile(data['fixed_scalar_profile']['geometry'],data['analytic_extension_origin'])
    nodes=np.asarray(data['mesh']);states=np.asarray(data['states']);velocities=np.asarray(data['rhs'])
    accelerations=[]
    for s,y,v in zip(nodes,states,velocities):
        a,ap,app=profile(s);k=ap/a
        accelerations.append(old.jvp(y,k,v,dk=app/a-k*k))
    accelerations=np.asarray(accelerations)
    h=np.diff(nodes)[:,None];c0=states[:-1];c1=h*velocities[:-1];c2=h*h*accelerations[:-1]/2
    A=states[1:]-c0-c1-c2;B=h*velocities[1:]-c1-2*c2;C=h*h*accelerations[1:]-2*c2
    coefficients=np.stack((c0,c1,c2,10*A-4*B+C/2,-15*A+7*B-C,6*A-3*B+C/2),axis=1)
    u=np.linspace(0.,1.,args.meridian_points);s_values=nodes[-1]*(1-(1-u)**2)
    points=[];normals=[];parameters=[];maximum_curvature=0.
    selected=np.arange(0,q.N,args.angular_stride)
    cp,sp=np.cos(q.angle),np.sin(q.angle)
    def cart(v):return np.column_stack((cp*v[:,0]-sp*v[:,1],sp*v[:,0]+cp*v[:,1],v[:,2]))
    for s in s_values:
        cell=min(np.searchsorted(nodes,s,side='right')-1,len(nodes)-2)
        step=nodes[cell+1]-nodes[cell];t=(s-nodes[cell])/step;c=coefficients[cell]
        y=np.polynomial.polynomial.polyval(t,c)
        v=np.polynomial.polynomial.polyval(t,np.arange(1,6)[:,None]*c[1:])/step
        acc=np.polynomial.polynomial.polyval(t,(np.arange(2,6)*np.arange(1,5))[:,None]*c[2:])/(step*step)
        F,d,e=q.jet(y);V,dV,_=q.jet(v);Acc,_,_=q.jet(acc)
        n=np.cross(V,d);n/=np.linalg.norm(n,axis=1)[:,None]
        E=np.sum(V*V,axis=1);G=np.sum(d*d,axis=1);mixed=np.sum(V*d,axis=1)
        ee=np.sum(Acc*n,axis=1);ff=np.sum(dV*n,axis=1);gg=np.sum(e*n,axis=1)
        det=E*G-mixed*mixed;tr=(ee*G+gg*E-2*ff*mixed)/det;kd=(ee*gg-ff*ff)/det
        maximum_curvature=max(maximum_curvature,float(np.max((abs(tr)+np.sqrt(np.maximum(0,tr*tr-4*kd)))/2)))
        P=cart(F)[selected];N=cart(n)[selected];angles=q.angle[selected]
        points.append(P);normals.append(N);parameters.append(np.column_stack((np.full(len(selected),s),angles)))
        if s>0:
            points.append(P*np.array([1,1,-1]));normals.append(N*np.array([1,1,-1]))
            parameters.append(np.column_stack((np.full(len(selected),-s),angles)))
    points=np.concatenate(points);normals=np.concatenate(normals);parameters=np.concatenate(parameters)
    tree=cKDTree(points);best=float('inf');worst=None;pair_count=0;min_distance=float('inf')
    for first in range(0,len(points),args.chunk):
        stop=min(first+args.chunk,len(points));neighbors=tree.query_ball_point(points[first:stop],args.radius,workers=1)
        ii=np.repeat(np.arange(first,stop),[len(x) for x in neighbors]);jj=np.concatenate(neighbors).astype(int)
        chosen=jj>ii;ii=ii[chosen];jj=jj[chosen]
        if not len(ii):continue
        delta=points[jj]-points[ii];d2=np.sum(delta*delta,axis=1)
        if np.any(d2==0):raise ValueError('Distinct sample indices coincide geometrically')
        denominator=2*np.maximum(abs(np.sum(delta*normals[ii],axis=1)),abs(np.sum(delta*normals[jj],axis=1)))
        Q=np.divide(d2,denominator,out=np.full_like(d2,np.inf),where=denominator>0)
        index=int(np.argmin(Q));pair_count+=len(ii);min_distance=min(min_distance,float(np.sqrt(d2.min())))
        if Q[index]<best:
            best=float(Q[index]);i=int(ii[index]);j=int(jj[index])
            worst=dict(indices=[i,j],parameters=[parameters[i].tolist(),parameters[j].tolist()],
                       points=[points[i].tolist(),points[j].tolist()],normals=[normals[i].tolist(),normals[j].tolist()],
                       distance=float(np.sqrt(d2[index])),Q=best)
    report=dict(scope=__doc__,input_sha256=hashlib.sha256(raw).hexdigest(),
                source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                parameters={k:str(v) if isinstance(v,Path) else v for k,v in vars(args).items()},
                M=q.M,evaluation_angles=q.N,sampled_angles=len(selected),sample_points=len(points),
                inspected_distinct_pairs=pair_count,minimum_sample_pair_distance=min_distance,
                minimum_inspected_Q=best,all_point_cloud_pairs_Q_lower_bound=min(best,args.radius/2),
                far_pair_Q_lower_bound=args.radius/2,maximum_sample_principal_curvature=maximum_curvature,
                worst=worst,seconds=time.perf_counter()-started,continuous_certificate=False,closed_surface=False)
    args.out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--angles',type=int,default=512);p.add_argument('--angular-stride',type=int,default=2)
    p.add_argument('--meridian-points',type=int,default=81);p.add_argument('--radius',type=float,default=.34)
    p.add_argument('--chunk',type=int,default=128);main(p.parse_args())
