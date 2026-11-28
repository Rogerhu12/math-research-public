"""R750 native all-column annulus solve, both fixed open boundaries and all relative positions."""
import builtins
from collections import OrderedDict
import hashlib
import importlib.util
import os
from pathlib import Path
import sys
from types import ModuleType,SimpleNamespace

HERE=Path(__file__).resolve().parent
PINS={'r743_early_material_disk.py':'9513d8fb67459f4338bf494be0d88a07b848ed6da98cd9975fbac523b5d9ca0c',
      'r743_native_disk_solver.py':'a83c42cdbeded98836e539fdb98664475b2798e4919511a39f9d78328e766f18',
      'r742_native_tsqr.py':'d9565b37ad9e3b8d70df7adf0aa1b82015fd66edadcd6386923c1a1197f2b729'}
FILES=('r750_rigid_annulus.py','r750_relative_boundary.py','r750_annulus_solver.py')


def main():
    if (os.environ.get('GITHUB_ACTIONS')!='true' or not os.environ.get('GITHUB_RUN_ID','').isdigit()
            or os.environ.get('GITHUB_REPOSITORY','').lower()!='rogerhu12/math-research-public'):
        raise SystemExit('R750 requires the public research Actions runner')
    import numpy as np
    from scipy.sparse import csr_matrix,vstack
    import r743_early_material_disk as early
    import r750_rigid_annulus as model
    import r750_relative_boundary as rays
    from r742_native_tsqr import tsqr_factor
    for name,sha in PINS.items():
        if hashlib.sha256((HERE/name).read_bytes()).hexdigest()!=sha:
            raise ValueError('changed R750 pinned source '+name)
    facade=ModuleType('_r750_material')
    vars(facade).update({k:v for k,v in vars(early).items() if not k.startswith('__')})
    facade.R743Frame,facade.R743Build=model.R750Frame,model.R750Build
    facade.weak=SimpleNamespace(**vars(early.weak));facade.space=SimpleNamespace(**vars(early.space))
    facade.space.tagged_terms,facade.space.padded=model.tags,model.padded
    physical=None

    def bound(label,name):
        nonlocal physical
        module=early.weak.bound_module(label,name)
        if name=='r732_disk_qualification.py':
            physical=module
            original_center=module.center_jets
            module.center_jets=lambda *args:model.center_from_source(original_center,*args)
            integrate=module.reconstructed
            def prescribed_center(build,phase,q,degree,radii,s,order,mean=None,need_all=True):
                true=model.core_shift(build,phase)
                if mean is not None and not np.array_equal(mean,true):
                    raise ValueError('foreign centre translation in R750 physical reconstruction')
                return integrate(build,phase,q,degree,radii,s,order,true,need_all)
            module.reconstructed=prescribed_center
        if name!='r732_disk_solver.py':
            return module
        module.FILES=(*module.FILES,*FILES)
        original_main=module.main
        old_metrics=module.metrics
        def metrics(joint,frame):
            n=len(frame.r)
            a=np.asarray(joint)
            ns=frame.shape[-1]
            if a.shape!=(n+ns,3) or not np.isfinite(a).all():
                raise ValueError('incomplete native curl/relative-boundary residual')
            curl=a[:n].reshape(frame.shape+(3,))
            c=old_metrics(curl,frame)
            scale=np.sqrt(n/ns)
            moment=a[n:]/scale
            norm=np.linalg.norm(moment,axis=1);j=int(np.argmax(norm))
            rel=max(c['relative_peak'],float(norm[j]))
            return dict(max=rel,relative_peak=rel,rms=float(np.sqrt(np.mean(np.sum(a*a,axis=1)))),
                      curl=c,position=dict(absolute_peak=float(norm[j]),rms=float(np.sqrt(np.mean(norm**2))),
                      angles=ns,angle=float(frame.s.reshape(frame.shape)[0,j]),vector=moment[j].tolist(),
                      by_axis=np.abs(moment).max(axis=0).tolist(),array=module.array_id(moment)),
                      combined=module.array_id(a),position_row_weight=float(scale),
                      metric_scope='max(curl/source_min,unweighted original relative-position norm)')
        module.metrics=metrics

        def start():
            base=module.Continuation
            class Relative(base):
                def __init__(self,paid,level,iterations):
                    super().__init__(paid,level,iterations)
                    self.kernels=OrderedDict()
                    self.live_bytes=0

                def setup(self,phase,degree):
                    frames=super().setup(phase,degree)
                    key=[phase]
                    if not self.p.filename('r750_actual_release_probe',key).exists():
                        val=self.p.get('r750_actual_release_probe',key,lambda:model.release_probe(self.build,phase))
                        builtins.print('R750_RELEASE_CHECK',module.plain(module.summarize(val)),flush=True)
                    return frames

                def pieces(self,phase,degree,purpose,frame):
                    level=self.level+(purpose=='validation')
                    order=8+2*level+(4 if purpose=='validation' else 0)
                    grid=self.p.get('r750_ray_rule',[purpose,level,order],lambda:rays.ray_grid(self.build,physical,order))
                    ss=frame.s.reshape(frame.shape)[0]
                    prefix=[phase,degree,purpose,level,order,module.array_id(ss)]
                    for lo in range(0,len(ss),8):
                        hi=min(lo+8,len(ss));key=prefix+[lo,hi]
                        def load(key=key,lo=lo,hi=hi):
                            pid=module.plain(key)
                            part=self.kernels.pop(pid,None)
                            if part is None:
                                kernel=self.p.get('r750_true_ray_kernel',key,
                                    lambda:rays.kernel(self.build,phase,degree,ss[lo:hi],grid))
                                size=sum(a.nbytes for a in kernel.values() if isinstance(a,np.ndarray))
                                part=(kernel,size)
                                while self.kernels and self.live_bytes+size>96*1024**2:
                                    _,(_,old)=self.kernels.popitem(last=False)
                                    self.live_bytes-=old
                                self.live_bytes+=size
                            self.kernels[pid]=part
                            return part[0]
                        yield key,load

                def field(self,phase,degree,purpose,q,frame):
                    orig=super().field(phase,degree,purpose,q,frame).reshape(-1,3)
                    qid=module.array_id(q)
                    data_key=[phase,degree,purpose,self.level,qid]
                    if self.p.filename('r750_all_relative_positions',data_key).is_file():
                        moment=self.p.get('r750_all_relative_positions',data_key,None)
                    else:
                        blocks=[]
                        for key,load in self.pieces(phase,degree,purpose,frame):
                            bk=key+[qid]
                            if self.p.filename('r750_relative_position',bk).is_file():
                                block=self.p.get('r750_relative_position',bk,None)
                            else:
                                part=load()
                                block=self.p.get('r750_relative_position',bk,lambda:rays.evaluate(part,q))
                            blocks.append(block)
                        moment=self.p.get('r750_all_relative_positions',data_key,lambda:np.concatenate(blocks))
                    return np.concatenate((orig,np.sqrt(len(orig)/len(moment))*moment))

                def operator(self,phase,degree,q,frame,residual):
                    key=[phase,degree,self.level,module.array_id(q)]
                    if self.p.filename('tsqr_svd',key+['complete']).is_file():
                        return self.p.get('tsqr_svd',key+['complete'],None)
                    def stage(kind,subkey,compute):
                        return self.p.get(kind,key+subkey,compute)
                    if self.p.filename('full_sparse_jacobian',key).is_file():
                        combined=self.p.get('full_sparse_jacobian',key,None)
                        return tsqr_factor(combined,residual,module.array_id,stage)
                    if self.p.filename('r750_complete_curl_csr',key).is_file():
                        raw=self.p.get('r750_complete_curl_csr',key,None)
                    else:
                        ch=self.p.get('nine_angular_derivatives',key,lambda:early.space.channels(frame,q))
                        raw=self.p.get('r750_complete_curl_csr',key,lambda:early.space.sparse_jac(frame,q,ch))
                    ids=raw['sampled_columns']
                    blocks=[]
                    for pkey,load in self.pieces(phase,degree,'train',frame):
                        pk=pkey+[key[-1]]
                        if self.p.filename('r750_relative_jacobian',pk).is_file():
                            z=self.p.get('r750_relative_jacobian',pk,None)
                        else:
                            part=load()
                            z=self.p.get('r750_relative_jacobian',pk,lambda:rays.derivative(part,q,ids))
                        blocks.append(z)
                    def combine():
                        j=csr_matrix((raw['data'],raw['indices'],raw['indptr']),shape=raw['shape'])
                        nm=sum(z['block'].shape[0]//3 for z in blocks)
                        scale=np.sqrt((j.shape[0]//3)/nm)
                        full=vstack([j]+[csr_matrix(scale*z['block']) for z in blocks],format='csr')
                        defects=np.maximum.reduce([np.asarray(raw['scaled_check_defects'])]+
                                                   [np.asarray(z['scaled_check_defects']) for z in blocks])
                        return dict(data=full.data,indices=full.indices,indptr=full.indptr,shape=full.shape,
                                    sampled_columns=ids,scaled_check_defects=defects,curl_rows=j.shape[0],
                                    actual_relative_position_rows=3*nm,position_scale=float(scale))
                    combined=self.p.get('full_sparse_jacobian',key,combine)
                    return tsqr_factor(combined,residual,module.array_id,stage)

                def qualify(self,phase,degree,q):
                    report=super().qualify(phase,degree,q)
                    key=[phase,degree,module.array_id(q)]
                    file=self.p.root/'physical'/Path(report['physical_archive']).name
                    def check():
                        with np.load(file,allow_pickle=False) as data:
                            r=data['r'];ell=self.build.profile.read(r)[-1]
                            sel=(r<=early.weak.physical.R0)|(ell>=model.FLAT_START-1.e-15)
                            g=data['source_jets'][:,sel];p=data['physical_jets'][:,sel]
                            b=data['centre_drift'];bs=data['boundary_derivative_drift']
                            centre=data['physical_center_jets'];ss=data['s']
                        if not np.any(r[sel]>early.weak.physical.R0) or not np.any(r[sel]<=early.weak.physical.R0):
                            raise ValueError('R750 physical grid missed the core or the terminal true plane band')
                        want=np.empty_like(g);want[0]=model.prescribed(self.build,phase,g[0]);want[1:]=g[1:]@model.turn(phase).T
                        err=np.linalg.norm(p-want,axis=-1)
                        local=np.linalg.norm(b,axis=-1);j=int(np.argmax(local))
                        if not np.isfinite([*err.max(axis=(1,2)),local.max(),np.abs(bs).max()]).all():
                            raise ValueError('nonfinite closed boundary physical archive')
                        return dict(physical_six_jet_maxima=err.max(axis=(1,2)).tolist(),true_flat_rows=int(sum(sel)),
                                    exact_center_position=centre[0].tolist(),all_original_angles=len(ss),
                                    relative_period_max=float(local.max()),relative_period_peak_s=float(ss[j]),
                                    relative_period_max_vector=b[j].tolist(),
                                    relative_period_angular_derivative_max=float(np.linalg.norm(bs,axis=-1).max()),
                                    reference_diameter_bound=3.162,remaining_continuous_qualification='open')
                    report['source']='R750 R743 metric with the physical rigid terminal plane (d=.42 sqrt(lambda))'
                    report['actual_rigid_core_and_two_edge_positions']=self.p.get('r750_physical_two_edge_check',key,check)
                    return report
            module.Continuation=Relative
            original_main()
        module.main=start
        return module
    facade.weak.bound_module=bound
    def emit(marker,*args,**kwargs):
        marker={'R743_PHASE':'R750_PHASE','R743_DISK_FINAL':'R750_ANNULUS_FINAL'}.get(marker,marker)
        builtins.print(marker,*args,**kwargs)
    spec=importlib.util.spec_from_file_location('_r750_paid_driver',HERE/'r743_native_disk_solver.py')
    run=importlib.util.module_from_spec(spec);spec.loader.exec_module(run)
    run.builtins=SimpleNamespace(print=emit)
    if not any(x=='--state' or x.startswith('--state=') for x in sys.argv[1:]):
        sys.argv.extend(('--state','r750-paid-state'))
    sys.modules['r743_early_material_disk']=facade
    try:
        run.main()
    finally:
        sys.modules['r743_early_material_disk']=early


if __name__=='__main__':
    main()
