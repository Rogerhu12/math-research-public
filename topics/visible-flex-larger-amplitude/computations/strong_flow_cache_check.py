#!/usr/bin/env python3
"""Inspect baseline-Flow retention on three actual radial BVP states.

Pass --check-output PATH and an ordinary strong_neck_bvp command. No nonlinear
solve or global Jacobian is performed. The candidate only restores the already
selected baseline Flow and its exact key after geometric finite differences;
all derivative arithmetic is obtained from the same loaded root source.
"""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[name]='1'
import gc,hashlib,importlib.util,json,sys,textwrap,time,types
from pathlib import Path
import numpy as np
P=Path(__file__).resolve().parent

OLD='self.select(p);self.flow(p[0])\n            return ds[None,None,:]*J,PJ'
NEW='self.select(p);self._flow=f;self._flow_key=(float(p[0]),float(p[1]))\n            return ds[None,None,:]*J,PJ'

def main():
    i=sys.argv.index('--check-output');output=Path(sys.argv[i+1]);del sys.argv[i:i+2]
    entry={name:hashlib.sha256((P/name).read_bytes()).hexdigest() for name in
           ('strong_flow_cache_check.py','strong_neck_bvp.py','root_dual_core_bvp.py','root_radial_batching.py')}
    root_source=(P/'root_dual_core_bvp.py').read_text()
    spec=importlib.util.spec_from_file_location('strong_flow_cache_runner',P/'strong_neck_bvp.py')
    runner=importlib.util.module_from_spec(spec);spec.loader.exec_module(runner)
    loader=runner.module

    def inspect_solver(fun,bc,x,y,p,**kw):
        obj=fun.__self__;loaded_method=kw['fun_jac']
        indices=np.unique(np.round(np.linspace(0,len(x)-1,5)[1:-1]).astype(int))
        t=np.asarray(x)[indices];states=np.asarray(y)[:,indices]
        source=root_source
        for transform in runner.TRANSFORMS['root_dual_core_bvp.py']['replacements']:
            source=source.replace(transform['old'],transform['new'])
        method=source[source.index('        def fun_jac(self,t,y,p):'):source.index('        def terminal(self,y,p):')]
        if method.count(NEW)==1:method=method.replace(NEW,OLD)
        if method.count(OLD)!=1:raise ValueError('Baseline restoration pattern changed')
        namespace=dict(loaded_method.__func__.__globals__,second_control=obj.second_control)
        exec(compile(textwrap.dedent(method),str(P/'strong_flow_cache_check.py')+':original','exec'),namespace)
        original=types.MethodType(namespace['fun_jac'],obj)
        exec(compile(textwrap.dedent(method.replace(OLD,NEW)),str(P/'strong_flow_cache_check.py')+':candidate','exec'),namespace)
        candidate=types.MethodType(namespace['fun_jac'],obj)
        obj.select(p);obj._flow_key=None;baseline=obj.flow(p[0])
        table_globals=baseline.adapt_fun_jac.__func__.__globals__
        table_builder=table_globals['build_tables'];counts={'calls':0,'wall':0.,'cpu':0.}
        table_file=Path(table_builder.__code__.co_filename)
        entry[str(table_file)]=hashlib.sha256(table_file.read_bytes()).hexdigest()
        def counted(flow):
            wall=time.perf_counter();cpu=time.process_time()
            value=table_builder(flow)
            counts['calls']+=1;counts['wall']+=time.perf_counter()-wall;counts['cpu']+=time.process_time()-cpu
            return value
        table_globals['build_tables']=counted
        records=[];outputs=[]
        def evaluate(label,method,reset):
            if reset:
                obj.select(p);obj._flow_key=None;obj.flow(p[0]);gc.collect()
            before=counts.copy();start=time.perf_counter();cpu=time.process_time()
            J,PJ=method(t,states,p)
            table=getattr(obj._flow,'_fourier_jacobian_tables',None)
            item=dict(label=label,seconds=time.perf_counter()-start,cpu_seconds=time.process_time()-cpu,
                      table_builds=counts['calls']-before['calls'],table_build_seconds=counts['wall']-before['wall'],
                      table_build_cpu_seconds=counts['cpu']-before['cpu'],baseline_flow_id=id(obj._flow),
                      table_id=id(table) if table is not None else None,
                      selected_key=list(obj._flow_key),table_retained=table is not None)
            records.append(item);outputs.append((J,PJ));gc.collect()
            print(json.dumps(dict(event='three_point_flow_cache',**item,**runner.memory_record())),flush=True)
        try:
            evaluate('original_first',original,True)
            evaluate('original_repeat',original,False)
            evaluate('retained_first',candidate,True)
            evaluate('retained_repeat',candidate,False)
            equality=[dict(label=records[j]['label'],state_array_equal=bool(np.array_equal(outputs[0][0],a)),
                           parameter_array_equal=bool(np.array_equal(outputs[0][1],b)),
                           state_max_abs=float(np.max(abs(outputs[0][0]-a))),
                           parameter_max_abs=float(np.max(abs(outputs[0][1]-b)))) for j,(a,b) in enumerate(outputs)]
            result=dict(scope=__doc__,inspection_only=True,nonlinear_solution=False,n=obj.n,modes=obj.M,
                        radial_points=t.tolist(),selected_mesh_indices=indices.tolist(),full_warm_nodes=len(x),
                        exact_return_comparison=equality,measurements=records,source_sha256=entry,
                        transform=dict(old=OLD,new=NEW),memory=runner.memory_record(),
                        explanation='Only three radial points are inspected. Timing is diagnostic, not a full-Jacobian speed claim.')
            output.write_text(json.dumps(result,indent=2)+'\n')
            if not all(v['state_array_equal'] and v['parameter_array_equal'] for v in equality):
                raise RuntimeError('Baseline retention changed the evaluated Jacobian')
            if records[3]['table_builds']!=0 or records[2]['table_id']!=records[3]['table_id']:
                raise RuntimeError('Baseline table was not reused')
        finally:table_globals['build_tables']=table_builder
        raise RuntimeError('Inspection complete; no nonlinear solve requested')

    def module(name,path):
        result=loader(name,path)
        if Path(path).name=='root_dual_core_bvp.py':result.solve_bvp=inspect_solver
        return result
    runner.module=module;runner.main()

if __name__=='__main__':main()
