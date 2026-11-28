"""Same R746 disk boundary data; add physical columns and import its naturally finished paid artifact."""
import argparse
import builtins
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import time
from types import ModuleType,SimpleNamespace

HERE=Path(__file__).resolve().parent


def main():
    if (os.environ.get('GITHUB_ACTIONS')!='true' or not os.environ.get('GITHUB_RUN_ID','').isdigit()
            or os.environ.get('GITHUB_REPOSITORY','').lower()!='rogerhu12/math-research-public'):
        raise SystemExit('R754 requires the public research Actions runner')
    ap=argparse.ArgumentParser(add_help=False)
    which=ap.add_mutually_exclusive_group(required=True)
    which.add_argument('--parent-zip');which.add_argument('--parent-remote',action='store_true')
    ap.add_argument('--parent-receipt',required=True)
    inputs,rest=ap.parse_known_args();sys.argv=[sys.argv[0],*rest]
    import numpy as np
    from scipy.sparse import vstack
    import r743_early_material_disk as early
    import r746_physical_core_seed as old
    import r754_nested_rotation as model
    import r754_augmented_operator as ops
    from r754_parent_archive import Parent
    from r754_tsqr_reuse import tsqr_factor
    facade=ModuleType('_r754_solver_material')
    vars(facade).update({k:v for k,v in vars(early).items() if not k.startswith('__')})
    facade.R743Build,facade.R743Frame=model.R754Build,model.R754Frame
    facade.weak=SimpleNamespace(**vars(early.weak));facade.space=SimpleNamespace(**vars(early.space))
    facade.space.tagged_terms,facade.space.padded=model.tags,model.padded

    physical_code=None;source_center=None
    def bound(label,name):
        nonlocal physical_code,source_center
        m=early.weak.bound_module(label,name)
        if name=='r732_disk_qualification.py':
            physical_code=m;source_center=m.center_jets
        if name!='r732_disk_solver.py':return m
        m.FILES=(*m.FILES,'r746_physical_core_seed.py','r746_native_disk_solver.py',*model.NEW_FILES)
        m.TYPES.update(R746Build=old.R746Build,R746Frame=old.R746Frame)
        original_main=m.main;old_metrics=m.metrics
        def metrics(field,frame):
            values=np.asarray(field);n=len(frame.r)
            if values.ndim!=2 or values.shape[1]!=3 or len(values)<=n or not np.isfinite(values).all():
                raise ValueError('incomplete original and newly released three-curl rows')
            first=old_metrics(values[:n].reshape(frame.shape+(3,)),frame)
            probe=frame.new_probe
            added=old_metrics(values[n:].reshape(probe.shape+(3,)),probe)
            return dict(max=max(first['max'],added['max']),relative_peak=max(first['relative_peak'],added['relative_peak']),
                        rms=float(np.sqrt(np.mean(np.sum(values*values,axis=1)))),original=first,
                        new_independent_material_rows=added,array=m.array_id(values))
        m.metrics=metrics

        def start():
            base=m.Continuation;paid_base=m.Paid
            def center(build,phase,q,degree,mean):
                first,source=old.centre_jets(source_center,build,phase,q,degree,mean)
                return model.broad.center(first,phase,q[-3],q[-1]),source
            physical_code.center_jets=center
            class Paid(paid_base):
                def __init__(self,directory,seconds,settings):
                    origin=time.monotonic()
                    self.parent=Parent(inputs.parent_zip,inputs.parent_receipt,m)
                    info=self.parent.spec
                    super().__init__(directory,seconds,{**settings,'immutable_parent':info})
                    elapsed=self.start-origin
                    self.start=origin;self.end-=elapsed;self.deadline-=elapsed;self.io+=elapsed
                    if (self.parent.meta['phases']!=list(m.PHASES) or self.parent.meta['degrees']!=list(m.DEGREES)
                            or self.parent.meta['build']!=m.OPTIONS or self.parent.level!=settings['level']):
                        raise ValueError('native phase, degree, grid or source choices differ from the R746 parent')
                    self.imported=set();self.physical_key=None;self.active_import_io=0.
                    m.write_json(self.root/'r746-parent.json',dict(parent=info,reason=self.parent.terminal['reason'],
                                    old_accepted=self.parent.state.get('accepted'),old_state_records=len(self.parent.records),
                                    terminal_sha256=info['terminal_sha256']))

                def append(self,filename,value):
                    # In the frozen engine a cache adoption may be nested inside
                    # a genuinely new stage. Split its original I/O out of the
                    # measured stage elapsed time exactly once.
                    if filename=='cost.jsonl':
                        value=dict(value)
                        if value['event']=='start':self.active_import_io=0.
                        elif value['event'] in ('saved','failed'):
                            spent=min(value['scientific_seconds'],self.active_import_io)
                            value['scientific_seconds']-=spent
                            value['original_archive_seconds']=spent
                            value['archive_seconds']=value.get('archive_seconds',0.)+spent
                            self.active_import_io=0.
                    return super().append(filename,value)

                def adoption_time(self,seconds):
                    self.io+=seconds
                    if self.current is not None:self.active_import_io+=seconds

                def acquire(self,kind,key):
                    path,_=self.parent.key(kind,key)
                    begin=time.monotonic()
                    value=self.parent.receipt(kind,key)
                    if path not in self.imported:
                        info=self.parent.zip.getinfo(path)
                        self.append('r746-imports.jsonl',dict(run=self.run,kind=kind,key=key,parent=self.parent.ident,
                                     original_path=path,original_bytes=info.file_size,crc32=info.CRC,
                                     member_sha256=self.parent.bytes_sha[path],range_bytes_total=
                                     self.parent.remote.bytes_received if self.parent.remote is not None else None))
                        self.imported.add(path)
                    self.adoption_time(time.monotonic()-begin)
                    self.now['reused_R746_'+kind]+=1
                    return value

                def get(self,kind,key,compute):
                    if kind=='source_build':
                        build=self.acquire(kind,key)
                        if build.seed_identity!=self.parent.source_id:raise ValueError('R746 donor source identity mismatch')
                        self.build=model.R754Build.extend(build)
                        return self.build
                    if kind in ('phase_ring','phase_pulses','native_nodes') and self.parent.has(kind,key):
                        return self.acquire(kind,key)
                    if kind=='native_frame' and self.parent.has(kind,key):
                        oldf=self.acquire(kind,key);phase=key[0]
                        def additional():
                            extended=model.R754Frame.extend(oldf,self.build,phase)
                            return {k:v for k,v in vars(extended).items() if k not in vars(oldf) or k in ('ncols','q0')}
                        ext=super().get('r754_parent_frame_extension',key,additional)
                        frame=model.R754Frame.__new__(model.R754Frame)
                        vars(frame).update(vars(oldf));vars(frame).update(ext)
                        return frame
                    if self.physical_key is not None and kind in ('qualification','forced_sleeve','sampled_shell_hull'):
                        new,prior,oldq=self.physical_key
                        if key==new and self.parent.has(kind,prior):
                            def fetch():
                                val=self.acquire(kind,prior)
                                if kind=='qualification':
                                    if val['q_sha256']!=m.digest(oldq.astype('<f8').tobytes()):
                                        raise ValueError('foreign donor physical qualification control vector')
                                    file=self.root/'physical'/Path(val['physical_archive']).name
                                    start_io=time.monotonic()
                                    self.parent.transfer_archive(val['physical_archive'],file,val['archive_sha256'])
                                    self.adoption_time(time.monotonic()-start_io)
                                    val={**val,'physical_archive':str(file),'unchanged_R746_physical_qualification':
                                        dict(parent=self.parent.ident,old_q=prior[-1],nested_q=new[-1],
                                             rule='original archive and six jets; added controls exactly zero')}
                                return val
                            return super().get(kind,key,fetch)
                    return super().get(kind,key,compute)
            m.Paid=Paid

            class Relative(base):
                def __init__(self,paid,level,iterations):
                    fresh=not (paid.root/'continuation.json').exists()
                    self.warm_index=None
                    super().__init__(paid,level,iterations)
                    self.warm_index=self.s['phase_index']
                    if fresh:
                        self.adopt_warm(self.warm_index);super().put()

                def adopt_warm(self,i):
                    if i>=len(m.PHASES):return
                    phase=m.PHASES[i];p=self.p.parent.warm(phase)
                    incoming=np.asarray(self.s['q'],dtype=float)
                    degree=self.s['degree']
                    if p is not None and p[0]>degree:
                        if len(incoming)!=3*len(model.tags(degree)):
                            raise ValueError('incoming native vector has the wrong degree')
                        incoming=model.padded(incoming,degree,p[0]);degree=p[0]
                    self.s['q']=incoming.tolist();self.s['degree']=degree
                    if p is not None:
                        self.p.append('r746-warm-starts.jsonl',dict(phase=phase,degree=p[0],
                                      parent_q=m.array_id(p[1]),incoming_q=m.array_id(incoming),
                                      parent=self.p.parent.ident,selection='both grids before first GN'))

                def put(self):
                    i=self.s['phase_index']
                    if self.warm_index is not None and i!=self.warm_index:
                        self.adopt_warm(i);self.warm_index=i
                    super().put()

                def setup(self,phase,degree):
                    fs=super().setup(phase,degree)
                    for purpose,level in (('train',self.level),('validation',self.level+1)):
                        frame=fs[purpose]
                        if hasattr(frame,'new_probe'):continue
                        fid=[phase,purpose,level]
                        def core_check():
                            if self.p.parent.has('r746_zero_core_seed',fid):
                                return self.p.acquire('r746_zero_core_seed',fid)
                            return old.check_zero_seed(frame,self.build,phase)
                        self.p.get('r754_same_true_core_seed',fid,core_check)
                        def make():
                            probe=model.probes(self.build,phase,degree,purpose)
                            # A pair already present in the old tensor must not count as a new source row.
                            taken=np.isin(probe.r,np.unique(frame.r))&np.isin(probe.s,np.unique(frame.s))
                            return probe.subset(~taken) if np.any(taken) else probe
                        frame.new_probe=self.p.get('r754_additional_native_frame',[phase,degree,purpose,level],make)
                    key=[phase]
                    if not self.p.filename('r754_exact_witness',key).is_file():
                        item=self.p.get('r754_exact_witness',key,lambda:model.exact_local_check(self.build,phase))
                        builtins.print('R754_ACTUAL_RELEASE',m.plain(m.summarize(item)),flush=True)
                    return fs

                def select_start(self,phase,degree,q):
                    # This runs only before the first fit at a new pose/degree.
                    # The continuation's live ndarray and checkpoint receive
                    # the same winning controls before its first residual key.
                    key=[phase,degree]
                    if self.s.get('r754_selected_at')==key:return
                    if self.s['iteration'] or self.s['line']:
                        raise ValueError('new-pose comparison cannot replace a live paid line search')
                    candidates={}
                    def add(label,vector):
                        qid=m.array_id(vector)['sha256']
                        if qid in candidates:candidates[qid][0].append(label)
                        else:candidates[qid]=([label],vector.copy())
                    add('continued',q)
                    p=self.p.parent.warm(phase)
                    if p is not None and p[0]<=degree:
                        old_degree,oldq=p
                        bare=np.zeros(3*len(model.tags(old_degree)));bare[:len(oldq)]=oldq
                        if old_degree!=degree:bare=model.padded(bare,old_degree,degree)
                        add('paid_parent',bare)
                    else:bare=None
                    zero=np.zeros_like(q);add('old_zero',zero)
                    if phase:
                        for label,coeff in (('compact_R752',(0.,-1.,0.)),('wide_meridian',(1.,0.,0.)),
                                            ('bounded_axial',(0.,0.,1.)),('interior_axial',(0.,0.,.5))):
                            test=zero.copy();test[-3:]=coeff;add(label,test)
                        if bare is not None and np.any(bare):
                            test=bare.copy();test[-2]=-1.;add('paid_parent_compact',test)
                    results=[];best=None
                    for labels,vector in candidates.values():
                        score=[]
                        for purpose in ('train','validation'):
                            fr=self.frames[purpose]
                            val=self.measured_field(phase,degree,purpose,vector,fr)
                            checked=metrics(val,fr)
                            if 'bounded_axial' in labels:
                                rr=np.r_[fr.r,fr.new_probe.r];ss=np.r_[fr.s,fr.new_probe.s]
                                ell=model.space.ell_data(rr)[0];size=np.linalg.norm(val,axis=1)
                                norm={}
                                for label,mask in (('outer_cauchy',ell<2*model.weak.physical.H),
                                                   ('axial_bulk',ell>=2*model.weak.physical.H),
                                                   ('rigid_fillet_core',ell>=model.weak.FILLET_START)):
                                    ids=np.flatnonzero(mask)
                                    if not len(ids):raise ValueError('missing true radial candidate sector')
                                    i=ids[np.argmax(size[ids])]
                                    norm[label]=dict(rows=len(ids),max=float(size[i]),r=float(rr[i]),s=float(ss[i]))
                                if (norm['axial_bulk']['max']>880*phase+2.e-8 or
                                        norm['rigid_fillet_core']['max']>2.e-8):
                                    raise ArithmeticError('actual all-row axial candidate exceeds its material bound')
                                checked['actual_axial_sectors']=norm
                            score.append(checked)
                        # Give both complete RMS and the worst held-out peak a vote.
                        # All raw fields, individual metrics and actual controls remain available.
                        rank=(max(s['rms'] for s in score),max(s['relative_peak'] for s in score),
                              max(s['max'] for s in score))
                        results.append(dict(labels=labels,q=m.array_id(vector),controls=vector.tolist(),
                                     train=score[0],validation=score[1],rank=rank))
                        if best is None or rank<best[0]:best=(rank,vector)
                    winner=best[1];q[:]=winner
                    self.s['q']=winner.tolist();self.s['r754_selected_at']=key
                    self.p.append('r754-global-candidates.jsonl',dict(phase=phase,degree=degree,
                                  parent=self.p.parent.ident,candidates=results,chosen=m.array_id(winner)))
                    super().put()

                def field(self,phase,degree,purpose,q,frame):
                    if purpose=='train':self.select_start(phase,degree,q)
                    return self.measured_field(phase,degree,purpose,q,frame)

                def measured_field(self,phase,degree,purpose,q,frame):
                    part,_,_=model.split(q,degree);key=[phase,degree,purpose,self.level,m.array_id(q)]
                    pk=[phase,degree,purpose,self.level,m.array_id(part)]
                    def original():
                        if self.p.parent.has('curl',pk):
                            return ops.restrict_field(frame,q,self.p.acquire('curl',pk))
                        return frame.curl(q)
                    primary=self.p.get('r754_original_node_field',key,original).reshape(-1,3)
                    fresh=self.p.get('r754_witness_field',key,lambda:frame.new_probe.curl(q)).reshape(-1,3)
                    return np.concatenate((primary,fresh))

                def operator(self,phase,degree,q,frame,residual):
                    part,_,carrier=model.split(q,degree);pk=[phase,degree,self.level,m.array_id(part)]
                    k=[phase,degree,self.level,m.array_id(q)]
                    def ts(kind,sub,fn):return self.p.get(kind,k+sub,fn)
                    if self.p.filename('tsqr_svd',k+['complete']).is_file():return ts('tsqr_svd',['complete'],None)
                    donor=None
                    if (self.p.parent.has('full_sparse_jacobian',pk) and self.p.parent.has('tsqr_scale',pk+['columns'])
                            and self.p.parent.has('curl',[phase,degree,'train',self.level,pk[-1]])):
                        donor=dict(columns=len(part),support=frame.support(carrier),
                            has=lambda kind,sub:self.p.parent.has(kind,pk+sub),
                            load=lambda kind,sub:self.p.acquire(kind,pk+sub))
                    if self.p.filename('full_sparse_jacobian',k).is_file():
                        return tsqr_factor(self.p.get('full_sparse_jacobian',k,None),residual,m.array_id,ts,donor)
                    blocks=[]
                    for name,fr in (('original',frame),('supplement',frame.new_probe)):
                        key=k+[name]
                        if self.p.filename('r754_augmented_row_group',key).is_file():
                            blocks.append(self.p.get('r754_augmented_row_group',key,None));continue
                        prior=None;channels=None
                        if name=='original':
                            if self.p.parent.has('full_sparse_jacobian',pk):prior=self.p.acquire('full_sparse_jacobian',pk)
                            if self.p.parent.has('nine_angular_derivatives',pk):channels=self.p.acquire('nine_angular_derivatives',pk)
                        def stage(kind,fn):return self.p.get('r754_'+kind,key,fn)
                        block=ops.add_operator(fr,q,prior,channels,None,stage)
                        blocks.append(self.p.get('r754_augmented_row_group',key,lambda:block))
                    def combine():
                        a,b=blocks
                        if not np.array_equal(a['sampled_columns'],b['sampled_columns']):
                            raise ValueError('different augmented column order between the two row groups')
                        return {**ops.raw(vstack([ops.matrix(a),ops.matrix(b)],format='csr')),
                          'sampled_columns':a['sampled_columns'],'scaled_check_defects':np.maximum(
                            a['scaled_check_defects'],b['scaled_check_defects']),
                          'original_parent_q':m.array_id(part),'inherited_parent_rows':a['unchanged_parent_rows'],
                          'old_prefix_columns':a['old_prefix_columns'],'new_columns':a['new_columns'],
                          'new_witness_rows':b['shape'][0]}
                    full=self.p.get('full_sparse_jacobian',k,combine)
                    return tsqr_factor(full,residual,m.array_id,ts,donor)

                def qualify(self,phase,degree,q):
                    part,extra,carrier=model.split(q,degree);new=[phase,degree,m.array_id(q)]
                    oldkey=[phase,degree,m.array_id(part)]
                    unchanged=not np.any(extra) and not np.any(carrier)
                    parent=self.p.parent
                    old_available=unchanged and parent.has('qualification',oldkey)
                    now=self.s.get('current',{})
                    if now.get('phase')!=phase or now.get('degree')!=degree or now.get('q')!=m.array_id(q):
                        raise ValueError('missing the actual two-grid field of the requested physical state')
                    fit=bool(now['finite_fit'])
                    if not fit and not old_available:
                        # The measured full two-grid curls already reject this
                        # new field. Reserve all-pair geometry for an actual fit.
                        def pending():
                            warm=parent.warm(phase)
                            prior=None if warm is None else [phase,warm[0],m.array_id(warm[1])]
                            return dict(status='full geometry deferred after a two-grid curl rejection',
                                    phase=phase,degree=degree,q_sha256=m.digest(q.astype('<f8').tobytes()),
                                    paired_field=now,continuous_material_and_time='open',physical_qualified=False,
                                    original_paid_qualification_key=prior if prior and parent.has('qualification',prior) else None,
                                    original_parent_input=parent.ident)
                        return self.p.get('r754_deferred_physical',new,pending)
                    self.p.physical_key=(new,oldkey,part) if old_available else None
                    all_records=self.s['records']
                    def has_hull(record):
                        k=[record['phase'],record['degree'],record['q']]
                        return self.p.filename('sampled_shell_hull',k).is_file()
                    available=[r for r in all_records if has_hull(r)]
                    self.s['records']=available
                    try:
                        result=super().qualify(phase,degree,q)
                    finally:
                        self.s['records']=all_records;self.p.physical_key=None
                    result['deferred_cross_pose_hulls']=[dict(phase=r['phase'],degree=r['degree'],q=r['q'])
                        for r in all_records if not has_hull(r)]
                    result['R754_same_boundary']=dict(total_native_columns=len(q),old_prefix=m.array_id(part),added=m.array_id(extra),
                        carrier=carrier.tolist(),physically_unchanged_by_new_controls=unchanged,
                        parent=self.p.parent.ident,full_continuous_qualification='open')
                    return result
            m.Continuation=Relative
            original_main()
        m.main=start
        return m
    facade.weak.bound_module=bound
    def emit(marker,*args,**kwargs):
        marker={'R743_PHASE':'R754_PHASE','R743_DISK_FINAL':'R754_DISK_FINAL'}.get(marker,marker)
        builtins.print(marker,*args,**kwargs)
    spec=importlib.util.spec_from_file_location('_r754_driver',HERE/'r743_native_disk_solver.py')
    run=importlib.util.module_from_spec(spec);spec.loader.exec_module(run);run.builtins=SimpleNamespace(print=emit)
    if not any(x=='--state' or x.startswith('--state=') for x in sys.argv[1:]):sys.argv.extend(('--state','r754-paid-state'))
    sys.modules['r743_early_material_disk']=facade
    try:run.main()
    finally:sys.modules['r743_early_material_disk']=early


if __name__=='__main__':main()
