#!/usr/bin/env python3
"""Refine geometry sampling without changing the actual height space.

The three previously published definition files remain untouched. Extra
physical background nodes near an independently observed curvature peak are
added to the integration and objective grid. B-spline coefficient functions,
cut jets and reference-metric basis are unchanged. Further optimization may
change their coefficients, and is explicitly a new candidate.
"""
from pathlib import Path
import argparse,hashlib,importlib.util,json
import numpy as np
from scipy.optimize import linprog

HERE=Path(__file__).parent
spec=importlib.util.spec_from_file_location('refined_height_definition',HERE/'2026-11-17-parallel-model-direct-height-accepted-base.py')
model=importlib.util.module_from_spec(spec);spec.loader.exec_module(model)

class RefinedGrid(model.AcceptedBase):
    def __init__(self,args):
        super().__init__(args)
        self.definition_sha=self.source_sha;old_panels=self.nc
        base_end=float(self.h0mean[0]+np.sum(self.width[:,None]*self.gw*self.w.reshape(self.r.shape))+self.base_increment_offset)
        points=json.loads(args.critical_radii);extra=[]
        for point in points:
            index=int(np.searchsorted(self.bg.r,point))
            extra.extend(self.bg.r[max(0,index-args.critical_neighbors):min(len(self.bg.r),index+args.critical_neighbors+1)])
            extra.append(point)
        self.edges=model.direct.base.distinct_knots(np.r_[self.edges,extra])
        self.width=np.diff(self.edges);self.nc=len(self.width)
        self.r=self.edges[:-1,None]+self.width[:,None]*self.gx;self.flat_r=self.r.ravel();self.x=self.flat_r-self.r0
        self.w,self.wr=self.reference_metric(self.flat_r);self.E=1+self.w*self.w
        self.oldlogw=np.log(self.w);self.oldlogwr=self.wr/self.w
        self.base=model.direct.base.boundary_fundamentals(self.x,self.L,args.decay_length)
        self.B=[self.spline(self.x,j)[:,self.free] for j in range(3)]
        self.Bend=[self.spline(self.x,j)[:,-3:].sum(axis=1) for j in range(3)]
        self.MB=[self.metric_spline(self.x,j)[:,self.metric_free] for j in range(3)]
        self.base_H,self.base_hr,self.base_hrr,self.base_hp,self.base_hrp,self.base_hpp=self._base_height_at(self.flat_r)
        self.base_increment_offset=base_end-self.h0mean[0]-float(np.sum(self.width[:,None]*self.gw*self.w.reshape(self.r.shape)))
        correction=self.cartesian_join_correction(self.flat_r)
        self.correct_xy=correction['value'];self.correct_Fr=correction['first'];self.correct_Frr=correction['second']
        self.wquad=np.sqrt((self.width[:,None]*self.gw/self.L).ravel())[:,None]/np.sqrt(self.N)
        self.refined_grid=dict(original_panels=old_panels,refined_panels=self.nc,
            requested_radii=points,background_neighbors=args.critical_neighbors,
            same_height_basis=True,same_reference_metric_basis=True)
        self.source_sha=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
        print(json.dumps(dict(event='refined-grid',**self.refined_grid)),flush=True)

    def save_design(self,x,cost,finished,optimizer=None):
        super().save_design(x,cost,finished,optimizer)
        report=json.loads(self.args.out.read_text());report['refined_grid']=self.refined_grid
        report['accepted_base']['definition_sha256']=self.definition_sha
        report['mean_curvature_initializer']=getattr(self,'mean_initialization',None)
        self.args.out.write_text(json.dumps(report,indent=2)+'\n')

    def prepare_initial(self,coefficients):
        x=super().prepare_initial(coefficients)
        if not getattr(self.args,'mean_curvature_initialization',False):return x
        lower=self.args.mean_curvature_radius
        free=self.free[self.spline.t[self.free]+self.r0>=lower]
        local=np.searchsorted(self.free,free)
        if not len(local):raise ValueError('No mean-height basis is supported in the selected radial region')
        edges=self.atomic_radii();edges=edges[edges>=lower]
        nodes=np.array([(1-1/np.sqrt(3))/2,(1+1/np.sqrt(3))/2])
        r=model.direct.base.distinct_knots(np.r_[edges,(edges[:-1,None]+np.diff(edges)[:,None]*nodes).ravel()])
        amin=np.empty(len(r));amax=np.empty(len(r))
        for start in range(0,len(r),64):
            sl=slice(start,start+64);v=self.evaluate_height(r[sl],x)
            amin[sl]=v['hrr'].min(axis=1);amax[sl]=v['hrr'].max(axis=1)
        A=self.height_scale*self.spline(r-self.r0,2)[:,free]
        speed=self.height_scale*self.spline(r-self.r0,1)[:,free]
        strength=np.maximum(np.max(abs(A),axis=0),1e-12);A=A/strength;speed=speed/strength
        n=len(local);zero=np.zeros_like(A);zs=np.zeros_like(speed)
        matrix=np.vstack((np.c_[A,zero],np.c_[-A,zero],np.c_[speed,zs],np.c_[-speed,zs],
                          np.c_[np.eye(n),-np.eye(n)],np.c_[-np.eye(n),-np.eye(n)]))
        target=self.args.actual_curvature_limit
        rhs=np.r_[target-amax,target+amin,np.full(2*len(r),self.args.mean_speed_change),np.zeros(2*n)]
        result=linprog(np.r_[np.zeros(n),np.ones(n)],A_ub=matrix,b_ub=rhs,
            bounds=[(None,None)]*n+[(0,None)]*n,method='highs')
        info=dict(scope='Sampled hrr feasibility only; actual curvature is checked separately',
            radii=len(r),variables=n,success=bool(result.success),message=result.message,
            initial_hrr_min=float(amin.min()),initial_hrr_max=float(amax.max()),target=target)
        if result.success:
            delta=result.x[:n]/strength;x[local]+=delta
            final_min=amin+A@result.x[:n];final_max=amax+A@result.x[:n]
            geometry=self.reconstruct(x)
            info.update(final_hrr_min=float(final_min.min()),final_hrr_max=float(final_max.max()),
                max_coefficient_change=float(abs(delta).max()),minimum_D=float(geometry['D'].min()),
                sampled_actual_curvature=float(geometry['actual_curvature'].max()),
                sampled_gram=self.diagnostics(geometry)['sampled_gram'])
        self.mean_initialization=info;print(json.dumps(dict(event='mean-curvature-feasibility',**info)),flush=True)
        return x

def main(a):
    old=json.loads(a.input.read_text());params=old['parameters']
    for key in ('trace','background','out','input','accepted_state'):
        if params.get(key):params[key]=Path(params[key])
    params.update(input=a.input,out=a.out,max_nfev=a.iterations,method='armijo',
        critical_radii=a.critical_radii,critical_neighbors=a.neighbors,
        actual_curvature_limit=a.curvature_limit,actual_curvature_weight=a.curvature_weight,
        end_weight=a.end_weight,log_every=20,function_tolerance=1e-20,
        metric_height_coupling=a.coupled_metric_height,cap_length_weight=10.,
        mean_curvature_initialization=a.mean_curvature_initialization,
        mean_curvature_radius=a.mean_curvature_radius,mean_speed_change=a.mean_speed_change)
    if a.cap_lift is not None:params['cap_lift']=a.cap_lift
    if a.gauss is not None:params['gauss']=a.gauss
    if a.cut_fraction is not None:params['cut_fraction']=a.cut_fraction
    if a.angles is not None:params['angles']=a.angles
    model.direct.Design=RefinedGrid;model.direct.main(argparse.Namespace(**params))

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--input',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--iterations',type=int,default=400);p.add_argument('--critical-radii',default='[1.6883406815921667]')
    p.add_argument('--neighbors',type=int,default=8);p.add_argument('--gauss',type=int);p.add_argument('--angles',type=int)
    p.add_argument('--cut-fraction',type=float);p.add_argument('--cap-lift',type=float)
    p.add_argument('--curvature-limit',type=float,default=6.6);p.add_argument('--curvature-weight',type=float,default=.1)
    p.add_argument('--end-weight',type=float,default=3.);p.add_argument('--coupled-metric-height',action='store_true')
    p.add_argument('--mean-curvature-initialization',action='store_true')
    p.add_argument('--mean-curvature-radius',type=float,default=1.60);p.add_argument('--mean-speed-change',type=float,default=.005)
    main(p.parse_args())
