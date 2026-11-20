import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'): os.environ[key]='1'
import argparse,importlib.util,sys,json,numpy as np
from pathlib import Path
p=argparse.ArgumentParser(description='Inspect the saved q=.01 material-core M8 failure; finite diagnostics only.')
for key in ('source-topic','short-bridge','input-dir','core-config','raw'):
 p.add_argument('--'+key,type=Path,required=True)
a=p.parse_args()
here=Path(__file__).resolve().parent
def mod(name,path):
 s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);sys.modules[name]=m;s.loader.exec_module(m);return m
scripts=a.source_topic/'scripts'
c=mod('inspect_coupler',scripts/'db6f-prefix-coupled.py')
mod('inspect_flat',scripts/'db6f-prefix-flat-profile.py').install(c.adaptive)
c.adaptive.old.install_source(scripts.parent/'repro/source-root')
mod('inspect_short',a.short_bridge).install()
mod('inspect_fourier',scripts/'78718-prefix-fourier-jacobian.py').install(c.adaptive)
settings=json.loads(a.core_config.read_text())
factory=mod('inspect_core',here/'material_core_factory.py').make_factory(settings)
__import__('fixed_metric_mode3_core').PlanarSupportCore=factory
__import__('fixed_metric_mode3_bvp').PlanarSupportCore=factory
chart=json.loads((a.input_dir/'reference/chart.json').read_text());cfg=json.loads((a.input_dir/'q060-profile.json').read_text());port=json.loads((a.input_dir/'q060-port.json').read_text());port['cut']['_prefix_bridge']=cfg['prefix_bridge']
Flow,Base=c.adaptive.build_classes(chart)
sys.path.insert(0,str(here/'round_raw_lib'))
from exact_core_lift import install_core_lift
Base=install_core_lift(Flow,Base)
import analytic_adaptive_core_jac as analytic
analytic.parameter_jets=lambda core,theta:core.jet_parameter_derivatives(theta)
analytic.install(Base)
o=Base(cfg,port,.01,8,256,False,.01);o.bcweights[:]=.02
raw=np.load(a.raw);x,y,p=raw['x'],raw['y'],raw['p'];o.initial(p);f=o.flow(p[0]);s,_=o.chart(x,p[0]);best=(np.inf,None,None)
for start in range(0,len(s),32):
 fr=f.frame(s[start:start+32],o.q*y[:,start:start+32]);i,j=np.unravel_index(np.argmin(fr['margin']),fr['margin'].shape)
 if fr['margin'][i,j]<best[0]:best=(float(fr['margin'][i,j]),float(s[start+i]),float(2*np.pi*j/fr['margin'].shape[1]))
print(json.dumps({'raw_core':o._core.summary(),'root_min_node':best,'legacy_input_controls':(p[1:]*o.pscale).tolist(),'actual_controls':list(o._core.corrections),'bc_max':float(abs(o.bc(y[:,0],y[:,-1],p)).max())}),flush=True)
# Check the exact control-chain Jacobian at representative valid nodes.
idx=np.linspace(0,len(x)-1,9,dtype=int);t=x[idx];Y=y[:,idx];J,PJ=o.fun_jac(t,Y,p);errs=[]
for j in range(8):
 h=2e-6*max(1,abs(p[j])) if j else 2e-7
 pp=p.copy();pm=p.copy();pp[j]+=h;pm[j]-=h
 fd=(o.fun(t,Y,pp)-o.fun(t,Y,pm))/(2*h)
 errs.append({'j':j,'relative':float(abs(fd-PJ[:,j,:]).max()/max(1,abs(fd).max())),'absolute':float(abs(fd-PJ[:,j,:]).max())})
print(json.dumps({'jacobian_checks':errs}),flush=True)
