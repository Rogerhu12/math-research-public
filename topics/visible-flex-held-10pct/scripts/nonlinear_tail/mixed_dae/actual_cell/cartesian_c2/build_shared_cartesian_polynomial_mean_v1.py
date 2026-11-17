"""Explicit C2 full-Cartesian Fourier/quintic map on one fixed physical cell.

The round planar term r(cos u,sin u) is retained algebraically, so its exact
linear dependence is not destroyed by subtracting nearly equal float values.
All three Cartesian perturbation components use shared position/two-jet data.
Their angular coefficients are finite real trigonometric polynomials. Global
height mean uses one compatible quartic primitive of the shared cubic slope.
Audits are finite samples, not continuous metric or curvature certificates.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse, gzip, hashlib, json, math, sys
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parent.parent))
from cartesian_interpolant import relative_geometry


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def polynomial(jets, x):
    """Normalized quintic coefficients, using the exact R11 Hermite formula."""
    a=np.asarray(jets,dtype=np.clongdouble if np.iscomplexobj(jets) else np.longdouble)
    h=np.diff(x).astype(np.longdouble)
    h=h.reshape((-1,)+(1,)*(a.ndim-2))
    y,d,q=a
    e0=y[1:]-y[:-1]-h*d[:-1]-h*h*q[:-1]/2
    e1=d[1:]-d[:-1]-h*q[:-1]
    e2=q[1:]-q[:-1]
    return np.stack((y[:-1],h*d[:-1],h*h*q[:-1]/2,
                     10*e0-4*h*e1+h*h*e2/2,
                     -15*e0+7*h*e1-h*h*e2,
                     6*e0-3*h*e1+h*h*e2/2))


def evaluate_poly(c,t,h,order):
    value=np.zeros_like(c[0])
    for k in range(5,order-1,-1):
        value=value*np.longdouble(t)+(math.factorial(k)//math.factorial(k-order))*c[k]
    return value/np.longdouble(h)**order


def angular_values(c,n,derivative=0):
    count=len(c);k=np.fft.fftfreq(count)*count
    value=np.asarray(c,dtype=np.complex128)*(1j*k[:,None])**derivative
    out=np.zeros((n,3),dtype=np.complex128)
    for j,f in enumerate(k.astype(int)):
        out[f%n]+=value[j]
    return (np.fft.ifft(out,axis=0)*n).real


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--angular',type=int,default=256)
    a=p.parse_args();doc=json.loads(gzip.decompress(a.input.read_bytes()))
    nodes=doc['nodes'];x=np.array([n['x'] for n in nodes]);N=doc['parameters']['N']
    if a.angular<N:raise ValueError('Audit angular grid must contain the input frequencies')
    relative=np.array([n['relative_jets'] for n in nodes]) # node, angle, rjet, xyz
    full=np.array([n['jets'] for n in nodes])
    data=np.transpose(relative,(2,0,1,3));data[1]*=-1 # x derivatives
    co=np.fft.fft(data,axis=2)/N
    discarded_nyquist=np.max(abs(co[:,:,N//2,:]),axis=(0,1)).tolist()
    co[:,:,N//2,:]=0
    # Centered planar primitive and non-mean height are the exact common gauge.
    discarded_means=np.max(abs(co[:,:,0,:]),axis=1).tolist()
    co[:,:,0,:]=0
    d=-np.mean(full[:,:,1,2],axis=1);q=np.mean(full[:,:,2,2],axis=1)
    mean=np.zeros(len(x),dtype=np.longdouble);hl=np.diff(x).astype(np.longdouble)
    for j,h in enumerate(hl):
        mean[j+1]=mean[j]+h*(np.longdouble(d[j])+np.longdouble(d[j+1]))/2+h*h*(np.longdouble(q[j])-np.longdouble(q[j+1]))/12
    # Literal mean positions are rounded once; same shared datum for both sides.
    mean=np.asarray(mean,float)
    mean_jets=np.stack((mean,d,q))
    c=polynomial(co,x);mc=polynomial(mean_jets,x)
    angular_changes=np.zeros(3);node_geometry={};identity_error=np.zeros(3)
    for i,n in enumerate(nodes):
        r=n['r'];u=2*np.pi*np.arange(N)/N
        represented=[angular_values(co[0,i],N,1)+np.c_[-r*np.sin(u),r*np.cos(u),np.zeros(N)],
                     -angular_values(co[1,i],N,1)+np.c_[-np.sin(u),np.cos(u),np.zeros(N)],
                     angular_values(co[0,i],N,2)+np.c_[-r*np.cos(u),-r*np.sin(u),np.zeros(N)]]
        for j in range(3):
            angular_changes[j]=max(angular_changes[j],float(np.linalg.norm(represented[j]-full[i,:,3+j],axis=1).max()))
    for i,h in enumerate(np.diff(x)):
        for k in range(3):
            for t,node in ((0,i),(1,i+1)):
                err=np.max(abs(evaluate_poly(c[:,i],t,h,k)-co[k,node]))
                err=max(err,abs(evaluate_poly(mc[:,i],t,h,k)-mean_jets[k,node]))
                identity_error[k]=max(identity_error[k],float(err))
    per_interval={};worst={};maxima={};minimum_area=float('inf');radial_second_change=0.
    for sample in doc['samples']:
        i=sample['interval'];t=sample['fraction'];h=x[i+1]-x[i]
        C=[evaluate_poly(c[:,i],t,h,k) for k in range(3)]
        Z=[float(evaluate_poly(mc[:,i],t,h,k)) for k in range(3)]
        # Enforce exact common-data endpoint identity in floating evaluation.
        if t in (0,1):
            node=i+int(t);C=[co[k,node] for k in range(3)];Z=[mean_jets[k,node] for k in range(3)]
        vals=[angular_values(C[0],a.angular),-angular_values(C[1],a.angular),
              angular_values(C[0],a.angular,1),angular_values(C[2],a.angular),
              -angular_values(C[1],a.angular,1),angular_values(C[0],a.angular,2)]
        vals[0][:,2]+=Z[0]
        vals[1][:,2]+=-Z[1]-sample['w']
        vals[3][:,2]+=Z[2]-sample['wr']
        result=relative_geometry(np.stack(vals,axis=1),sample['r'],sample['w'],sample['wr'])
        minimum_area=min(minimum_area,result.pop('minimum_normalized_area'))
        rec=per_interval.setdefault(i,dict(interval=i,stage=sample['stage'],raw_segment=nodes[i+1]['raw_segment'],x_left=x[i],x_right=x[i+1]))
        for k,v in result.items():
            rec[k]=max(rec.get(k,0.),v)
            if v>maxima.get(k,-1.):
                maxima[k]=v;worst[k]={**sample,'value':v}
        if t in (0,1):
            for k,v in result.items():node_geometry[k]=max(node_geometry.get(k,0.),v)
    segment=[]
    for raw in sorted(set(n['raw_segment'] for n in nodes)):
        rows=[v for v in per_interval.values() if v['raw_segment']==raw]
        segment.append(dict(raw_segment=raw,**{k:max(v[k] for v in rows) for k in maxima}))
    a.out.parent.mkdir(parents=True,exist_ok=True)
    array=a.out.with_suffix('.npz')
    np.savez_compressed(array,x=x,perturbation_node_jets=co,mean_node_jets=mean_jets)
    report=dict(scope='One explicit finite Fourier/shared Cartesian two-jet quintic C2 map on the original physical cell. Metrics and curvature below are finite samples, not interval bounds; no exact isometry, closed tail, reach, or 10-percent result.',
      representation=dict(radial='piecewise quintic shared Cartesian two-jets in x=rOuter-r',
       angular='full Cartesian finite Fourier frequencies -63 through 63 from the source 128-point centered development, with Nyquist zero',
       background='the planar r(cos u,sin u) term is retained algebraically',
       mean='global shared height positions integrate the unique endpoint-slope/derivative cubic on each interval; no independently reset shooting-stage mean',
       c2='Exact algebraic Hermite endpoint identities use the same literal node two-jet on both sides. No derivative fitting or independent left/right polynomial is used.',
       no_local_inverse_in_solve='The earlier mixed BVP did not invert Gram. This independent node-jet postprocessor uses the original positive-Gram chart only at the stable nodes.'),
      input=dict(path=str(a.input),sha256=sha(a.input)),source_sha256={str(p):sha(p) for p in (Path(__file__),Path(__file__).resolve().parent.parent/'cartesian_interpolant.py')},
      array=dict(path=str(array),sha256=sha(array)),parameters=doc['parameters'],
      nodes=len(x),intervals=len(x)-1,radial_samples=len(doc['samples']),angular_samples=a.angular,
      min_step=float(np.diff(x).min()),max_step=float(np.diff(x).max()),
      node_engine_root_relative=max(n['audit']['root_relative'] for n in nodes),node_engine_minA=min(n['audit']['minA'] for n in nodes),
      node_engine_L_change=max(n['audit']['L_change_from_mixed'] for n in nodes),
      discarded_nyquist_by_component=discarded_nyquist,discarded_means_by_jet=discarded_means,
      angular_node_jet_changes_Xu_Xru_Xuu=angular_changes.tolist(),
      numerical_polynomial_endpoint_identity_error=identity_error.tolist(),
      common_node_choice_maximum_jet_change=np.max([n['cartesian_jet_difference'] for n in doc['joins']],axis=0).tolist(),
      mean_height_change=float(mean[-1]),node_maxima=node_geometry,maxima=maxima,minimum_normalized_area=minimum_area,worst_samples=worst,segments=segment)
    a.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ('nodes','intervals','node_maxima','maxima','minimum_normalized_area','common_node_choice_maximum_jet_change','angular_node_jet_changes_Xu_Xru_Xuu','numerical_polynomial_endpoint_identity_error')}))


if __name__=='__main__':
    main()
