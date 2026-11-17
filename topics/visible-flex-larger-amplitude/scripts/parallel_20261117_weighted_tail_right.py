#!/usr/bin/env python3
"""Right-shallow weighted tail through an explicit affine coordinate reversal.

The physical scalar metric, complete equations, and declared deep boundary
are unchanged.  The solver uses x_comp=1-x_source so its shallow rows remain
on the computational left.  Output is converted back to ascending physical-r
source order, including the sign of the actual interpolation derivative.
No height reflection is silently applied: the supplied trace must already
use the desired height orientation and its positive background w.
"""
import argparse,gzip,hashlib,json
from pathlib import Path
import numpy as np
import parallel_20261117_weighted_tail_qr as solver
from parallel_20261117_dynamic_tail import Background


def sha(raw):return hashlib.sha256(raw).hexdigest()


class RightShallowBackground(Background):
    def __init__(self,path,coordinate):
        if coordinate!='reflected-source-index':raise ValueError('Require the declared reflected source coordinate')
        super().__init__(path,'source-index')
        if self.data.get('shallow_at')=='left':raise ValueError('Physical source declares its shallow cut on the left')
        if 'inner' in self.data and abs(self.data['inner']['r']-self.r[0])>1e-10:
            raise ValueError('Declared deep port is not the physical left endpoint')
        self.r=self.r[::-1].copy();self.rows=self.rows[::-1]
        self.logw=self.logw[::-1].copy();self.derivative=self.derivative[::-1].copy()
        self.data=dict(self.data,physical_shallow_at='right',shallow_at='left')
        self.coordinate=coordinate

    def radial(self,x):
        u=1-np.asarray(x)
        return self.radius(u),-self.radius(u,1)


def reverse_field(data,coordinate):
    result=dict(data)
    result['mesh']=(1-np.array(data['mesh'])[::-1]).tolist()
    result['states']=data['states'][::-1]
    if 'rhs' in data:result['rhs']=(-np.array(data['rhs'])[::-1]).tolist()
    if 'radial_mesh' in data:result['radial_mesh']=data['radial_mesh'][::-1]
    result['coordinate']=coordinate
    return result


def main(a):
    source=Path(__file__).read_bytes();requested=a.out
    trace=json.loads(a.trace.read_bytes());bg=Background(a.background,'source-index')
    if max(abs(trace['r']-bg.r[-1]),abs(trace['w']-np.exp(bg.logw[-1])))>1e-9:
        raise ValueError('Trace is not the physical right scalar cut')
    if 'w_r' in trace and abs(trace['w_r']-np.exp(bg.logw[-1])*bg.derivative[-1])>1e-8*max(1,abs(trace['w_r'])):
        raise ValueError('Physical right-cut slope derivative differs')
    inputs={}
    for name in ['input','material_input']:
        path=getattr(a,name)
        if path is None:continue
        raw=path.read_bytes();old=json.loads(gzip.decompress(raw))
        if not old.get('success') or old.get('coordinate')!='source-index' or old['background_sha256']!=bg.sha256:
            raise ValueError('Warm fields must be accepted on this scalar source in canonical source-index order')
        reflected=reverse_field(old,'reflected-source-index')
        reflected['coordinate_transformation_only']='Exact affine reversal of the supplied accepted interpolant; no new solve.'
        temporary=requested.with_name(requested.name+'.reflected-'+name+'.gz')
        payload=gzip.compress((json.dumps(reflected)+'\n').encode(),mtime=0);temporary.write_bytes(payload)
        inputs[name]=dict(canonical_sha256=sha(raw),reflected_sha256=sha(payload));setattr(a,name,temporary)
    solver.Background=RightShallowBackground
    if a.deep_dirichlet:
        if a.deep_columns:raise ValueError('A finite Dirichlet end does not use far columns')
        solver.weak_deep_boundary=lambda q,bg,columns:(np.eye(q.M),np.zeros((q.M,q.M)),
            dict(boundary_kind='finite zero nonmean height Dirichlet',scope='No infinite-tail equivalence is asserted.'))
    a.coordinate='reflected-source-index'
    a.out=requested.with_name(requested.name+'.computational.gz')
    print(json.dumps(dict(event='right_shallow_coordinate_reversal',source_sha256=sha(source),input_identities=inputs)),flush=True)
    solver.main(a)
    raw=a.out.read_bytes();computed=json.loads(gzip.decompress(raw));canonical=reverse_field(computed,'source-index')
    canonical.update(scope=__doc__,source_sha256=sha(source),reused_solver_source_sha256=computed['source_sha256'],
        computational_output_sha256=sha(raw),input_identities=inputs,shallow_at='right',
        computational_coordinate='x_comp=1-x_source',solver_left_boundary_rows=computed['left_boundary_rows'],
        canonical_left_boundary_rows=a.modes)
    # Preserve the solver's row-count metadata separately from canonical order.
    canonical['left_boundary_rows']=a.modes
    output=gzip.compress((json.dumps(canonical)+'\n').encode(),mtime=0);requested.write_bytes(output)
    print(json.dumps(dict(event='canonical_right_shallow_output',success=canonical['success'],
        output_sha256=sha(output),nodes=canonical['nodes'],collocation_rms_max=canonical['collocation_rms_max'])),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    for k in ['background','trace','out']:p.add_argument('--'+k,type=Path,required=True)
    for k in ['input','material-input','deep-columns']:p.add_argument('--'+k,type=Path)
    p.add_argument('--modes',type=int,default=8);p.add_argument('--angles',type=int,default=512)
    p.add_argument('--scale',type=float,default=1e-5);p.add_argument('--tol',type=float,default=1e-6)
    p.add_argument('--max-nodes',type=int,default=12000);p.add_argument('--mesh-stride',type=int,default=1);p.add_argument('--batch',type=int,default=32)
    p.add_argument('--allow-height-turn',action='store_true');p.add_argument('--fast-jacobian',action='store_true');p.add_argument('--deep-dirichlet',action='store_true')
    main(p.parse_args())
