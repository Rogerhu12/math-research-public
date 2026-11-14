#!/usr/bin/env python3
"""Run the existing neck BVP with retained warm mesh and bounded radial batches.

Use --workflow amplitude, design, or triple, then the original arguments.
With --nodes 0 the successful previous physical mesh is carried through the
explicit radial-coordinate map. A fresh nonlinear solve remains mandatory.
The original files and frozen source remain unchanged. This adapter changes
neither the physical flow nor boundary conditions or requested mesh tolerance.
Optional --newton-residual-factor tightens only the inner Newton stopping
threshold; its exact text replacement is recorded in the output.
Optional --linear-solver block-qr factors the same adjacent-node/parameter
Jacobian by balanced orthogonal elimination, avoiding global sparse-LU fill.
The direct-block-qr option also avoids the global sparse Jacobian and its
indices, using the validated root_block_collocation formulas. It collects
discarded Flow cycles after each independent Jacobian batch.
After geometric finite differences, the two-control Jacobian restores its
already selected baseline Flow and exact key. This retains the identical
Fourier tables across radial batches without changing derivative arithmetic.
Optional --geometric-flow-cache-size (default 0) also retains a bounded number
of identical geometric finite-difference Flow constructions. Its complete
constructor/reference/chart keys and independent three-point checks are in
strong_flow_lru.py and strong_flow_lru_check.py.
The two-control amplitude warm deformation also uses 24-point radial batches
and skips its exact identity at ratio=1, avoiding a full-grid geometry array.
"""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[name]='1'
import gzip,hashlib,json,sys,types,time,resource,gc
from pathlib import Path
P=Path(__file__).resolve().parent
TRANSFORMS={}
NEWTON_FACTOR=1.
LINEAR_SOLVER='sparse-lu'
TRACE_NEWTON=False
COLLECT_FLOW_GARBAGE=False
ENTRY_HASHES={}
GEOMETRIC_FLOW_CACHE_SIZE=0
FLOW_CACHE_RECORDS=[]

def memory_record():
    record={'peak_rss_kib':int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)}
    try:
        for line in Path('/proc/self/status').read_text().splitlines():
            if line.startswith('VmRSS:'):record['rss_kib']=int(line.split()[1])
    except OSError:pass
    return record

def trace(event,**fields):
    if COLLECT_FLOW_GARBAGE and event in ('newton_iteration','newton_trial','newton_factor_begin','block_qr_factor'):
        fields['before_gc_memory']=memory_record()
        fields['collected_unreachable_objects']=gc.collect()
    print(json.dumps(dict(event=event,**fields,**memory_record())),flush=True)

def module(name,path):
    path=Path(path);source=path.read_text();original=source;replacements=[]
    if path.name=='root_dual_core_bvp.py':
        replacements=[
            ('import numpy as np','import numpy as np\nimport root_radial_batching as radial'),
            ('t=merge_profile_mesh(np.linspace(0,1,nodes),self.chart_breaks)\n            s,_=self.chart(t,p[0])\n            arrays,record=pullback.convert',
             'grid=self.inverse_chart(np.asarray(saved.sol.x),p[0]) if nodes<=0 else np.linspace(0,1,nodes)\n            t=merge_profile_mesh(grid,self.chart_breaks)\n            s,_=self.chart(t,p[0])\n            arrays,record=pullback.convert'),
            ('return ds[None,:]*f.fun(s,y,p)','return ds[None,:]*radial.value(f,s,y,p)'),
            ('J,_=f.fun_jac(s,y,p)','J=radial.state_jacobian(f,s,y,p)'),
            ('self.select(p);self.flow(p[0])\n            return ds[None,None,:]*J,PJ',
             'self.select(p);self._flow=f;self._flow_key=(float(p[0]),float(p[1]))\n            return ds[None,None,:]*J,PJ'),
            ("            if scale=='linear':\n                N=max(512,32*(2*self.M+1));g=f.geo(s,N);theta=g['theta']\n                radial=np.stack((np.cos(theta),np.sin(theta),np.zeros_like(theta)),axis=-1)\n                background=f.profile(s)[0][:,None,None]*radial\n                B,_,_=f.basis(N)\n                y=ratio*y+(ratio-1)*f.project(g['pos']-background,B)/self.q",
             "            if scale=='linear' and ratio!=1.:\n                N=max(512,32*(2*self.M+1));B,_,_=f.basis(N)\n                for first in range(0,len(s),24):\n                    sl=slice(first,first+24);g=f.geo(s[sl],N);theta=g['theta']\n                    radial=np.stack((np.cos(theta),np.sin(theta),np.zeros_like(theta)),axis=-1)\n                    background=f.profile(s[sl])[0][:,None,None]*radial\n                    y[:,sl]=ratio*y[:,sl]+(ratio-1)*f.project(g['pos']-background,B)/self.q")]
    elif path.name=='root_domain_newton.py':
        if NEWTON_FACTOR!=1.:
            replacements.append(('threshold = h*(bvp_tol/30.)','threshold = h*(bvp_tol/30.)*'+repr(NEWTON_FACTOR)))
        if LINEAR_SOLVER!='sparse-lu':
            replacements.append(('factor = splu(jac(y, p, ym, ff, fm, br))','factor = _strong_block_factor(jac(y, p, ym, ff, fm, br),n,m,len(p))'))
            replacements.append(('try:\n                factor =','factor = None\n            try:\n                factor ='))
        if TRACE_NEWTON:
            replacements.extend([
                ('residual, cr, ym, ff, fm, br = data',
                 'residual, cr, ym, ff, fm, br = data\n        _strong_trace("newton_iteration", call=STATS["calls"], iteration=iteration, nodes=m, factors=factors, updates=updates, collocation_scaled_max=float(np.max(abs(cr)/(h[None,:]*(1+abs(fm))))), boundary_max=float(np.max(abs(br))))'),
                ('try:\n                factor =',
                 'try:\n                _strong_trace("newton_factor_begin", iteration=iteration, nodes=m)\n                factor ='),
                ('cost = float(step@step)',
                 'cost = float(step@step)\n            _strong_trace("newton_merit", iteration=iteration, merit=cost, step_max=float(np.max(abs(step))))'),
                ("STATS['rejected_domain_trials'] += 1",
                 "STATS['rejected_domain_trials'] += 1\n                _strong_trace(\"newton_trial\", iteration=iteration, alpha=alpha, status=\"outside-domain\")"),
                ('if np.isfinite(newcost) and newcost < (1-.4*alpha)*cost:',
                 '_strong_trace("newton_trial", iteration=iteration, alpha=alpha, status="evaluated", merit=newcost, old_merit=cost, armijo=bool(np.isfinite(newcost) and newcost < (1-.4*alpha)*cost))\n            if np.isfinite(newcost) and newcost < (1-.4*alpha)*cost:'),
                ('y, p, data, step, cost, alpha = accepted',
                 'y, p, data, step, cost, alpha = accepted\n        _strong_trace("newton_accepted", iteration=iteration, alpha=alpha, merit=cost)')])
    elif path.name=='alternative-neck-design-warm.py':
        replacements=[
            ('t=merge_profile_mesh(np.linspace(0,1,nodes),self.chart_breaks)',
             'old_grid=neck_chart.NeckChart(self._neck_knots,saved.flow.breaks).inverse(np.asarray(saved.sol.x))\n                grid=old_grid if nodes<=0 else np.linspace(0,1,nodes)\n                t=merge_profile_mesh(grid,self.chart_breaks)')]
    applied=[]
    for old,new in replacements:
        count=source.count(old)
        if count!=1:raise ValueError('Expected exactly one transform in '+path.name+': '+repr(old))
        source=source.replace(old,new);applied.append(dict(old=old,new=new,count=count))
    m=types.ModuleType(name);m.__file__=str(path);sys.modules[name]=m
    exec(compile(source,str(path),'exec'),m.__dict__)
    if path.name=='root_dual_core_bvp.py' and GEOMETRIC_FLOW_CACHE_SIZE:
        from strong_flow_lru import install_class
        original_make=m.make_dual
        def cached_make(*args,**kwargs):
            cls=original_make(*args,**kwargs)
            chart=args[2] if len(args)>2 else kwargs['chart']
            context=dict(class_chart=chart)
            def record(cache):FLOW_CACHE_RECORDS.append(dict(size=cache.size,stats=cache.stats))
            return install_class(cls,GEOMETRIC_FLOW_CACHE_SIZE,context,on_install=record)
        m.make_dual=cached_make
    if path.name=='root_domain_newton.py':m._strong_trace=trace
    if path.name=='root_domain_newton.py' and LINEAR_SOLVER!='sparse-lu':
        if LINEAR_SOLVER=='direct-block-qr':
            from root_block_collocation import DirectBlockQRFactor as BlockQRFactor
        else:
            from strong_block_qr import BlockQRFactor
        def block_factor(matrix,n,node_count,k):
            start=time.time();factor=BlockQRFactor(matrix,n,node_count,k);elapsed=time.time()-start
            m.STATS['block_qr_factorizations']=m.STATS.get('block_qr_factorizations',0)+1
            m.STATS['block_qr_factor_seconds']=m.STATS.get('block_qr_factor_seconds',0.)+elapsed
            trace('direct_block_qr_factor' if LINEAR_SOLVER=='direct-block-qr' else 'block_qr_factor',n=n,nodes=node_count,parameters=k,seconds=elapsed)
            return factor
        m._strong_block_factor=block_factor
        m.STATS['linear_factor_kind']='direct-block-balanced-QR' if LINEAR_SOLVER=='direct-block-qr' else 'balanced-block-QR'
    if path.name in ('alternative-neck-design-warm.py','alternative-neck-bvp.py','root_dual_core_bvp.py','root_triple_core_bvp.py'):m.module=module
    TRANSFORMS[path.name]=dict(original_sha256=hashlib.sha256(original.encode()).hexdigest(),replacements=applied)
    return m

def main():
    global NEWTON_FACTOR,LINEAR_SOLVER,ENTRY_HASHES,TRACE_NEWTON,COLLECT_FLOW_GARBAGE,GEOMETRIC_FLOW_CACHE_SIZE
    ENTRY_HASHES={name:hashlib.sha256((P/name).read_bytes()).hexdigest() for name in ('strong_neck_bvp.py','strong_angle_boost.py','strong_block_qr.py','root_radial_batching.py')}
    if '--trace-newton' in sys.argv:
        TRACE_NEWTON=True;sys.argv.remove('--trace-newton')
    if '--collect-flow-garbage' in sys.argv:
        COLLECT_FLOW_GARBAGE=True;sys.argv.remove('--collect-flow-garbage')
    if '--geometric-flow-cache-size' in sys.argv:
        i=sys.argv.index('--geometric-flow-cache-size');GEOMETRIC_FLOW_CACHE_SIZE=int(sys.argv[i+1]);del sys.argv[i:i+2]
    if not 0<=GEOMETRIC_FLOW_CACHE_SIZE<=32:raise ValueError('Flow cache size must be between 0 and 32')
    if GEOMETRIC_FLOW_CACHE_SIZE:
        ENTRY_HASHES['strong_flow_lru.py']=hashlib.sha256((P/'strong_flow_lru.py').read_bytes()).hexdigest()
    if '--linear-solver' in sys.argv:
        i=sys.argv.index('--linear-solver');LINEAR_SOLVER=sys.argv[i+1];del sys.argv[i:i+2]
    if LINEAR_SOLVER not in ('sparse-lu','block-qr','direct-block-qr'):raise ValueError('Unknown exact Jacobian factor')
    if LINEAR_SOLVER=='direct-block-qr':
        ENTRY_HASHES['root_block_collocation.py']=hashlib.sha256((P/'root_block_collocation.py').read_bytes()).hexdigest()
        import root_block_collocation as blocks
        blocks.install();original_prepare=blocks.prepare_sys
        def prepare(n,m,k,fun,bc,fun_jac,bc_jac,x,h):
            if fun_jac is None:raise ValueError('The strong prefix requires its analytic state Jacobian')
            def bounded_jacobian(*args):
                try:return fun_jac(*args)
                finally:gc.collect()
            return original_prepare(n,m,k,fun,bc,bounded_jacobian,bc_jac,x,h)
        blocks._bvp.prepare_sys=prepare
    if '--newton-residual-factor' in sys.argv:
        i=sys.argv.index('--newton-residual-factor');NEWTON_FACTOR=float(sys.argv[i+1]);del sys.argv[i:i+2]
        if not 0<NEWTON_FACTOR<=1:raise ValueError('Newton factor must tighten stopping')
    workflow='amplitude'
    if '--workflow' in sys.argv:
        i=sys.argv.index('--workflow');workflow=sys.argv[i+1];del sys.argv[i:i+2]
    scripts=dict(amplitude='alternative-neck-bvp.py',design='alternative-neck-design-warm.py',triple='root_triple_core_bvp.py')
    if workflow not in scripts:raise ValueError('Unknown workflow')
    script=scripts[workflow]
    runner=module('strong_neck_runner',P/script)
    try:runner.main()
    finally:
        if '--out-prefix' in sys.argv:
            out=Path(sys.argv[sys.argv.index('--out-prefix')+1])
            record=dict(scope=__doc__,workflow=workflow,newton_residual_factor=NEWTON_FACTOR,linear_solver=LINEAR_SOLVER,trace_newton=TRACE_NEWTON,collect_flow_garbage=COLLECT_FLOW_GARBAGE,jacobian_batch_gc=LINEAR_SOLVER=='direct-block-qr',memory=memory_record(),angle_boost_helper_sha256=ENTRY_HASHES['strong_angle_boost.py'],wrapper_sha256=ENTRY_HASHES['strong_neck_bvp.py'],transforms=TRANSFORMS,radial_batching_sha256=ENTRY_HASHES['root_radial_batching.py'],block_qr_sha256=ENTRY_HASHES['strong_block_qr.py'],direct_block_sha256=ENTRY_HASHES['root_block_collocation.py'] if LINEAR_SOLVER=='direct-block-qr' else None)
            record['geometric_flow_cache']=dict(size=GEOMETRIC_FLOW_CACHE_SIZE,instances=FLOW_CACHE_RECORDS,
                source_sha256=ENTRY_HASHES.get('strong_flow_lru.py'),scope='Identical actual Flow objects reused with bounded storage; no derivative or trial-state approximation.')
            record['dual_amplitude_warm_radial_batch_size']=24
            for f in (out.with_suffix('.json.gz'),out.with_name(out.name+'-summary.json')):
                if not f.exists():continue
                raw=gzip.decompress(f.read_bytes()) if f.suffix=='.gz' else f.read_bytes()
                d=json.loads(raw);d['strong_mesh_adapter']=record
                raw=(json.dumps(d,indent=2)+'\n').encode()
                if f.suffix=='.gz':raw=gzip.compress(raw,mtime=0)
                if len(raw)>=5000000:raise ValueError('Metadata exceeds file limit')
                f.write_bytes(raw)
if __name__=='__main__':main()
