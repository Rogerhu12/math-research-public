#!/usr/bin/env python3
"""Prescribe actual q1/c6, free actual q4, and solve delta/boost_length.

The previous two-mode reference angle chart is retained exactly. The actual
inlet support coefficients are separate: q1 and c6 are prescribed, q4 and
modes 8+ are unknown. No third physical metric control is introduced. Every
accepted output still needs a genuine nonlinear solve and remains a finite
linear-DN prefix, not a closed surface or fixed-g refinement.

Use --third-support VALUE and otherwise strong_neck_bvp.py arguments with
--workflow amplitude. The successful --restart is mandatory. A changed q1
deforms the warm image explicitly; it does not certify a new isometry.
"""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[name]='1'
import argparse,gzip,hashlib,importlib.util,json,math,sys
from pathlib import Path
import numpy as np
P=Path(__file__).resolve().parent

def main():
    parser=argparse.ArgumentParser(add_help=False)
    parser.add_argument('--third-support',type=float,required=True)
    options,remaining=parser.parse_known_args()
    if '--restart' not in remaining:raise ValueError('A successful checkpoint is required')
    restart=Path(remaining[remaining.index('--restart')+1]);raw=restart.read_bytes()
    previous=json.loads(gzip.decompress(raw) if restart.suffix=='.gz' else raw)
    if not previous.get('solver_success'):raise ValueError('A successful checkpoint is required')
    frequencies=previous.get('chart_reference_frequencies',[2,4])
    if frequencies!=[2,4]:raise ValueError('This adapter retains a previous two-mode reference chart')
    reference=np.asarray(previous['chart_reference_coefficients'],float)
    if reference.shape!=(2,):raise ValueError('A two-mode reference is required')
    source_hash=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    restart_hash=hashlib.sha256(raw).hexdigest()
    if '--workflow' in remaining and remaining[remaining.index('--workflow')+1]!='amplitude':
        raise ValueError('Use the amplitude runner; this adapter defines its own boundary design')
    sys.argv=[sys.argv[0]]+remaining
    spec=importlib.util.spec_from_file_location('strong_free_q4_runner',P/'strong_neck_bvp.py')
    runner=importlib.util.module_from_spec(spec);spec.loader.exec_module(runner)
    original_module=runner.module

    def module(name,path):
        loaded=original_module(name,path)
        if Path(path).name!='root_dual_core_bvp.py':return loaded
        original_make=loaded.make_dual
        def make_free(adaptive,charts,chart,secondary_law='linear',secondary_scale=.2,
                      meridian_chart='all-knots',second_control='boost_length'):
            if second_control!='boost_length':raise ValueError('Use the physical delta/LB controls')
            Base=original_make(adaptive,charts,chart,secondary_law,secondary_scale,meridian_chart,second_control)
            from fixed_metric_mode3_core import PlanarSupportCore
            from fixed_metric_mode3_bvp import merge_profile_mesh
            class FreeQ4(Base):
                def __init__(self,cfg,port,q,M,angular):
                    if M<3:raise ValueError('At least three core modes are required')
                    self.prescribed_c6=options.third_support
                    super().__init__(cfg,port,q,M,angular)
                    self.ref_coeff=reference.copy();self.ref_frequencies=[2,4]
                    self._flow_key=self._core_key=None;self._initial=None
                    self.pscale[1]=q*q
                    self._special_layout='p0=delta offset; p1=boost_length offset; p2=actual q4 / q1^2; p3..=support modes 8,10,...'
                    self.design_provenance=dict(scope=__doc__,prescribed_support=dict(q1=q,c6=self.prescribed_c6),
                        free_core_frequencies=[4]+list(range(8,2*M+1,2)),
                        unchanged_reference_coefficients=reference.tolist(),unchanged_reference_frequencies=[2,4],
                        adapter_sha256=source_hash,starting_checkpoint_sha256=restart_hash,
                        physical_controls=['delta','boost_length'],third_physical_control=False)
                    self.raw_recovery_context=dict(kind='actual-q1-c6-with-free-q4-v1',
                        prescribed_actual_support=dict(q1=q,c6=self.prescribed_c6),
                        reference_coefficients=reference.tolist(),reference_frequencies=[2,4])

                def initial(self,p):
                    self.select(p);key=tuple(np.asarray(p[2:],float))
                    if key!=self._core_key:
                        corrections=np.zeros(self.M-1)
                        corrections[0]=p[2]*self.pscale[1];corrections[1]=self.prescribed_c6
                        if self.M>3:corrections[2:]=np.asarray(p[3:])*self.pscale[2:]
                        core=PlanarSupportCore(self.q,corrections,2);f=self.flow(p[0]);N=max(2048,128*self.M)
                        gi=f.general_core_chart.inlet_geometry(N);exact=core.evaluate(gi['theta']);B,B1,B2=f.basis(N)
                        self._initial=f.project((exact['F']-gi['pos'])[None,:,:],B)[:,0]/self.q
                        J=f.project(core.parameter_derivatives(gi['theta']),B)
                        self._initial_jac=np.zeros((self.n,self.M));self._initial_jac[:,2]=J[:,1]*self.pscale[1]/self.q
                        if self.M>3:self._initial_jac[:,3:]=J[:,3:]*self.pscale[None,2:]/self.q
                        first=gi['p1']+self.q*f.values(self._initial[:,None],B1)[0]
                        second=gi['p2']+self.q*f.values(self._initial[:,None],B2)[0]
                        mapped=gi['pos']+self.q*f.values(self._initial[:,None],B)[0]
                        true1=exact['Ft']*gi['rho'][:,None]
                        true2=exact['Ftt']*gi['rho'][:,None]**2+exact['Ft']*gi['rhop'][:,None]
                        error=np.sum(first*first,axis=1)/gi['rho']**2-1
                        self._inlet_metrics=dict(position=float(np.linalg.norm(mapped-exact['F'],axis=1).max()),
                            first=float(np.linalg.norm(first-true1,axis=1).max()),second=float(np.linalg.norm(second-true2,axis=1).max()),
                            metric_l1=float(np.sum(abs(np.fft.fft(error)/N))))
                        self._core=core;self._core_key=key;self.support_amplitude=self.q
                    return self._initial

                def restart_from(self,saved,pullback,nodes,scale='linear'):
                    old=saved.rec;oldcfg=old['frozen_profile']
                    if not old.get('solver_success'):raise ValueError('Warm checkpoint is not a successful solve')
                    for key in sorted((set(oldcfg)|set(self.cfg))-{'delta','boost_length'}):
                        if oldcfg.get(key)!=self.cfg.get(key):raise ValueError('Uncontrolled physical profile changed: '+key)
                    if old['physical_tail_parameters']!=self.port['parameters'] or old['physical_tail_cut']!=self.port['cut']:
                        raise ValueError('Physical tail port changed')
                    p=np.zeros(self.M);p[0]=oldcfg['delta']-self.cfg['delta'];p[1]=oldcfg['boost_length']-self.cfg['boost_length']
                    ratio=self.q/saved.q;coeff=np.asarray(old['core']['coefficients'])
                    p[2]=coeff[1]*(ratio**2 if scale=='linear' else 1.)/self.pscale[1]
                    for j in range(3,min(self.M,len(coeff))):
                        exponent=j+1 if secondary_law=='quadratic' else math.ceil((j+1)/2)
                        p[j]=coeff[j]*(ratio**exponent if scale=='linear' else 1.)/self.pscale[j-1]
                    self.select(p);f=self.flow(p[0])
                    if abs(f.end-saved.flow.end)>2e-12*max(1.,f.end):raise ValueError('Warm physical meridian changed')
                    grid=self.inverse_chart(np.asarray(saved.sol.x),p[0]) if nodes<=0 else np.linspace(0,1,nodes)
                    t=merge_profile_mesh(grid,self.chart_breaks);s,_=self.chart(t,p[0])
                    N=max(512,32*(2*self.M+1))
                    arrays,record=pullback.convert(saved,f.general_core_chart,self.M,self.q,s,angular=N,height_angular=128)
                    y=arrays['y']
                    if scale=='linear' and ratio!=1.:
                        B,_,_=f.basis(N)
                        for start in range(0,len(s),24):
                            sl=slice(start,start+24);g=f.geo(s[sl],N);theta=g['theta']
                            radial=np.stack((np.cos(theta),np.sin(theta),np.zeros_like(theta)),axis=-1)
                            background=f.profile(s[sl])[0][:,None,None]*radial
                            y[:,sl]=ratio*y[:,sl]+(ratio-1)*f.project(g['pos']-background,B)/self.q
                    correction=self.initial(p)-y[:,0]
                    y+=correction[:,None]*np.maximum(0,1-s/(f.Tu/2))[None,:]**3
                    record.update(scope=__doc__,amplitude_ratio=ratio,amplitude_scaling=scale,
                        actual_q4_warm_guess=float(p[2]*self.pscale[1]),prescribed_actual_c6=self.prescribed_c6,
                        unchanged_reference_coefficients=reference.tolist(),q4_warm_scaling='q1 ratio squared, only as an initial guess',
                        inlet_guess_correction_max=float(np.max(abs(correction))),radial_warm_batch_size=24,
                        final_scope='Explicitly deformed initial guess. The following nonlinear solve determines a new physical metric; no coordinate change is counted as a metric design change.')
                    return t,y,p,record

                def prepare_recovery_output(self,out):
                    out['secondary_law']='free actual support q4'
                    out['secondary_scale']=None
                    out['prescribed_actual_core']=dict(q1=self.q,c6=self.prescribed_c6)

                def finalize_output(self,out,physical):
                    self.prepare_recovery_output(out)
            return FreeQ4
        loaded.make_dual=make_free
        return loaded
    runner.module=module;runner.main()

if __name__=='__main__':main()
