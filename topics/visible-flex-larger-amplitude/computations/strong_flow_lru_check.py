#!/usr/bin/env python3
"""Check optional bounded Flow reuse on three actual radial states.

This runs no BVP or full Jacobian. It compares exact J/PJ values with the
uncached constructor, including changed cfg, q, reference angle coefficients,
and numerical meridian chart knots. The cache is never used as a mathematical
approximation or a replacement for nonlinear continuation.
"""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[name]='1'
import gc,hashlib,importlib.util,json,sys,time
from pathlib import Path
import numpy as np
from strong_flow_lru import install_instance
P=Path(__file__).resolve().parent

def main():
    i=sys.argv.index('--check-output');out=Path(sys.argv[i+1]);del sys.argv[i:i+2]
    hashes={name:hashlib.sha256((P/name).read_bytes()).hexdigest() for name in
            ('strong_flow_lru.py','strong_flow_lru_check.py','strong_neck_bvp.py','root_dual_core_bvp.py')}
    spec=importlib.util.spec_from_file_location('strong_lru_check_runner',P/'strong_neck_bvp.py')
    runner=importlib.util.module_from_spec(spec);spec.loader.exec_module(runner);load=runner.module
    def inspect(fun,bc,x,y,p,**kw):
        obj=fun.__self__;jac=kw['fun_jac'];ids=np.unique(np.round(np.linspace(0,len(x)-1,5)[1:-1]).astype(int))
        t=x[ids];states=y[:,ids];rows=[];comparisons=[]
        def evaluate(label,reset=True):
            if reset:obj.select(p);obj._flow_key=None
            gc.collect();before=runner.memory_record();wall=time.perf_counter();cpu=time.process_time()
            value=jac(t,states,p)
            row=dict(label=label,seconds=time.perf_counter()-wall,cpu_seconds=time.process_time()-cpu,
                     before=before,after=runner.memory_record())
            cache=getattr(obj,'_strong_geometric_flow_cache',None)
            if cache is not None:row['cache_stats']=dict(cache.stats);row['retained_flows']=len(cache.entries)
            rows.append(row);print(json.dumps(dict(event='three_point_flow_lru',**row)),flush=True)
            return value
        cache=getattr(obj,'_strong_geometric_flow_cache',None)
        production_option_enabled=cache is not None
        if cache is not None:obj.Flow=cache.constructor
        baseline=evaluate('uncached_baseline');evaluate('uncached_repeat',False)
        if cache is None:cache=install_instance(obj,8,dict(scope='unchanged original class chart'))
        else:cache.entries.clear();obj.Flow=cache
        first=evaluate('cached_first');second=evaluate('cached_repeat',False)
        def compare(label,a,b,misses=None):
            record=dict(label=label,state_array_equal=bool(np.array_equal(a[0],b[0])),
                parameter_array_equal=bool(np.array_equal(a[1],b[1])),
                state_max_abs=float(np.max(abs(a[0]-b[0]))),parameter_max_abs=float(np.max(abs(a[1]-b[1]))))
            if misses is not None:record['new_constructor_misses']=misses
            comparisons.append(record)
        compare('baseline_first',baseline,first);compare('baseline_repeat',baseline,second)
        changes=[('physical_cfg',lambda:obj.cfg['start_acceleration'],lambda v:obj.cfg.__setitem__('start_acceleration',v),lambda v:v+1e-4),
                 ('gauge_q',lambda:obj.q,lambda v:setattr(obj,'q',v),lambda v:v+1e-4),
                 ('reference_angle_chart',lambda:obj.ref_coeff.copy(),lambda v:setattr(obj,'ref_coeff',v),lambda v:v+np.array([1e-4,0.])),
                 ('numerical_meridian_chart',lambda:obj._neck_knots.copy(),lambda v:setattr(obj,'_neck_knots',v),
                  lambda v:np.r_[v[0],v[1:-1]+1e-6*np.sin(np.pi*v[1:-1]),v[-1]])]
        for name,getter,setter,changed in changes:
            old=getter();setter(changed(old))
            try:
                obj.Flow=cache.constructor;reference=evaluate(name+'_uncached')
                obj.Flow=cache;misses=cache.stats['misses'];candidate=evaluate(name+'_cached')
                compare(name,reference,candidate,cache.stats['misses']-misses)
            finally:setter(old);obj.Flow=cache;obj._flow_key=None
        restored=evaluate('restored_baseline');compare('restored',baseline,restored)
        result=dict(scope=__doc__,inspection_only=True,nonlinear_solution=False,modes=obj.M,angular=obj.nt,
                    radial_points=t.tolist(),full_warm_nodes=len(x),cache_size=cache.size,production_option_enabled=production_option_enabled,measurements=rows,
                    comparisons=comparisons,source_sha256=hashes,cache_stats=dict(cache.stats),
                    interpretation='CPU and RSS are small-state diagnostics. No full-Jacobian speed or memory guarantee is inferred.')
        out.write_text(json.dumps(result,indent=2)+'\n')
        if not all(row['state_array_equal'] and row['parameter_array_equal'] for row in comparisons):
            raise RuntimeError('Bounded Flow cache changed actual Jacobian values')
        if not all(row.get('new_constructor_misses',1)>0 for row in comparisons):
            raise RuntimeError('Changed physical or chart dependency failed to miss the cache')
        if cache.stats['maximum_entries']>cache.size:raise RuntimeError('Flow cache exceeded its capacity')
        raise RuntimeError('Flow cache inspection complete; no nonlinear solve requested')
    def module(name,path):
        loaded=load(name,path)
        if Path(path).name=='root_dual_core_bvp.py':loaded.solve_bvp=inspect
        return loaded
    runner.module=module;runner.main()

if __name__=='__main__':main()
