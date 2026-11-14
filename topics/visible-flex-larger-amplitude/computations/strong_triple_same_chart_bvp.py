#!/usr/bin/env python3
"""Three physical controls and three actual core harmonics in the old chart.

Use --third-support VALUE and the ordinary strong_neck_bvp arguments. This
loads root_triple_core_bvp with its original delta/LB/boost_speed unknowns,
actual q/q4/c6 inlet, physical flow, boundary equations and acceptance rules.
Only the numerical reference chart is kept at the previous [2,4] coefficients.
The warm image is explicitly pulled back; changing the prescribed inlet is
still a new design problem requiring a genuine nonlinear solve.
"""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[name]='1'
import gzip,hashlib,importlib.util,json,sys,types
from pathlib import Path
import numpy as np
P=Path(__file__).resolve().parent

def main():
    if '--restart' not in sys.argv:raise ValueError('A successful restart is required')
    restart=Path(sys.argv[sys.argv.index('--restart')+1]);raw=restart.read_bytes()
    saved=json.loads(gzip.decompress(raw) if restart.suffix=='.gz' else raw)
    if not saved.get('solver_success'):raise ValueError('A successful restart is required')
    reference=np.asarray(saved['chart_reference_coefficients'],float)
    if reference.shape!=(2,) or saved.get('chart_reference_frequencies',[2,4])!=[2,4]:
        raise ValueError('This adapter preserves a previous [2,4] reference')
    if '--workflow' in sys.argv:
        if sys.argv[sys.argv.index('--workflow')+1]!='triple':raise ValueError('Use the triple workflow')
    else:sys.argv+=['--workflow','triple']
    adapter_hash=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    restart_hash=hashlib.sha256(raw).hexdigest()
    triple_path=P/'root_triple_core_bvp.py';original_source=triple_path.read_text()
    source_hash=hashlib.sha256(original_source.encode()).hexdigest()
    spec=importlib.util.spec_from_file_location('strong_same_chart_triple_runner',P/'strong_neck_bvp.py')
    runner=importlib.util.module_from_spec(spec);spec.loader.exec_module(runner);load=runner.module
    changes=[
        ('self.ref_frequencies=[2,4,6]','self.ref_frequencies=[2,4]'),
        ('self.ref_coeff=self.prescribed.copy()','self.ref_coeff=_strong_reference.copy()'),
        ('charts.attach_to_adaptive_flow(flow,self.prescribed,self.ref_frequencies,reference=\'core-blend\')',
         'charts.attach_to_adaptive_flow(flow,_strong_reference,self.ref_frequencies,reference=\'core-blend\')'),
        ('prescribed_frequencies=self.ref_frequencies,','prescribed_frequencies=[2,4,6],'),
        ('self.select(p);self.flow(p[0])\n                return ds[None,None,:]*J,PJ',
         'self.select(p);self._flow=f;self._flow_key=tuple(float(v) for v in p[:3])\n                return ds[None,None,:]*J,PJ'),
        ('                    scope=__doc__)\n\n            def make_flow',
         '                    scope=__doc__)\n'
         '                self.design_provenance.update(same_chart_adapter_sha256=_strong_adapter_hash,starting_checkpoint_sha256=_strong_restart_hash,reference_coefficients=_strong_reference.tolist(),reference_frequencies=[2,4],reference_is_prescribed_core=False)\n'
         '                self.raw_recovery_context=dict(kind="three-physical-controls-old-two-mode-chart-v1",prescribed_actual_support=self.prescribed.tolist(),reference_coefficients=_strong_reference.tolist(),reference_frequencies=[2,4],control_names=list(self.control_names))\n\n'
         '            def prepare_recovery_output(self,out):\n'
         '                out["prescribed_actual_core"]=dict(q1=float(self.prescribed[0]),q4=float(self.prescribed[1]),c6=float(self.prescribed[2]))\n'
         '                out["three_control_reference_policy"]="unchanged previous [2,4] chart"\n\n'
         '            def make_flow'),
        ('                p=np.zeros(self.M)\n                for j,name in enumerate(self.control_names):p[j]=oldcfg[name]-self.cfg[name]',
         '                if old["physical_tail_parameters"]!=self.port["parameters"] or old["physical_tail_cut"]!=self.port["cut"]:\n'
         '                    raise ValueError("The physical tail port changed during same-chart triple continuation")\n'
         '                p=np.zeros(self.M)\n                for j,name in enumerate(self.control_names):p[j]=oldcfg[name]-self.cfg[name]'),
        ("                if scale=='linear':\n                    N=max(512,32*(2*self.M+1));g=f.geo(s,N);theta=g['theta']\n                    radial=np.stack((np.cos(theta),np.sin(theta),np.zeros_like(theta)),axis=-1)\n                    background=f.profile(s)[0][:,None,None]*radial;B,_,_=f.basis(N)\n                    y=ratio*y+(ratio-1)*f.project(g['pos']-background,B)/self.q",
         "                if scale=='linear' and ratio!=1.:\n                    N=max(512,32*(2*self.M+1));B,_,_=f.basis(N)\n                    for first in range(0,len(s),24):\n                        sl=slice(first,first+24);g=f.geo(s[sl],N);theta=g['theta']\n                        radial=np.stack((np.cos(theta),np.sin(theta),np.zeros_like(theta)),axis=-1)\n                        background=f.profile(s[sl])[0][:,None,None]*radial\n                        y[:,sl]=ratio*y[:,sl]+(ratio-1)*f.project(g['pos']-background,B)/self.q")]
    source=original_source
    for old,new in changes:
        if source.count(old)!=1:raise ValueError('Triple source transform no longer matches: '+repr(old))
        source=source.replace(old,new)
    def module(name,path):
        if Path(path).name!='root_triple_core_bvp.py':return load(name,path)
        loaded=types.ModuleType(name);loaded.__file__=str(path);sys.modules[name]=loaded
        loaded.__dict__.update(_strong_reference=reference,_strong_adapter_hash=adapter_hash,_strong_restart_hash=restart_hash)
        exec(compile(source,str(path),'exec'),loaded.__dict__);loaded.module=runner.module
        runner.TRANSFORMS[Path(path).name]=dict(original_sha256=source_hash,
            replacements=[dict(old=old,new=new,count=1) for old,new in changes],
            same_chart_adapter_sha256=adapter_hash,starting_checkpoint_sha256=restart_hash)
        return loaded
    runner.module=module;runner.main()

if __name__=='__main__':main()
