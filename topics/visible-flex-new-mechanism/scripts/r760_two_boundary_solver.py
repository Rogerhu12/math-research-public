"""Public R760 full three-curl/two-edge GN with the complete original R750 archive as donor."""
import argparse
import builtins
from collections import OrderedDict
import importlib.util
import json
import os
from pathlib import Path
import sys
import time
from types import ModuleType,SimpleNamespace

HERE=Path(__file__).resolve().parent
NEW=('r754_ranged_zip.py','r754_tsqr_reuse.py','r760_meridian_moments.py','r760_angular_shoulders.py',
     'r760_triple_period.py','r760_full_annulus_frame.py','r760_original_annulus.py',
     'r760_relative_material_rows.py','r760_conserved_quadratures.py','r760_nested_operator.py',
     'r760_two_boundary_solver.py')


def facade(module,name):
    result=ModuleType(name)
    vars(result).update({k:v for k,v in vars(module).items() if not k.startswith('__')})
    return result


def main():
    if (os.environ.get('GITHUB_ACTIONS')!='true' or not os.environ.get('GITHUB_RUN_ID','').isdigit()
            or os.environ.get('GITHUB_REPOSITORY','').lower()!='rogerhu12/math-research-public'):
        raise SystemExit('R760 requires the public research Actions runner')
    p=argparse.ArgumentParser(add_help=False);p.add_argument('--parent-receipt',required=True)
    what=p.add_mutually_exclusive_group(required=True)
    what.add_argument('--parent-remote',action='store_true');what.add_argument('--parent-zip')
    conf,rest=p.parse_known_args();sys.argv=[sys.argv[0],*rest]
    import numpy as np
    import r743_early_material_disk as original_material
    import r742_native_tsqr as qr0
    import r750_rigid_annulus as previous
    import r750_relative_boundary as previous_ray
    import r760_full_annulus_frame as mod
    import r760_original_annulus as original
    import r760_relative_material_rows as kernels
    import r760_conserved_quadratures as conserved
    import r760_nested_operator as operator

    physical=facade(previous,'_r760_physical');physical.R750Build=mod.R760Build;physical.R750Frame=mod.R760Frame
    physical.tags,physical.padded=mod.shoulders.tags,mod.shoulders.padded
    physical.release_probe=mod.release_probe
    geometry=facade(original_material,'_r760_old_material')
    geometry.weak=SimpleNamespace(**vars(original_material.weak))
    rays=facade(previous_ray,'_r760_ray');rays.kernel=kernels.kernel
    qr=facade(qr0,'_r760_qr');state={}

    # Frames of the actual GN may read only committed per-label roots. The
    # standalone physical module also has a convenience evaluator for other uses.
    original_lookup=mod.triple.lookup
    def committed_lookup(build,phase,angles):
        if phase:
            known=build.r760_label_states.get(phase,{})
            if any(float(v) not in known for v in np.unique(angles)):
                raise ValueError('three-moment root was not charged before constructing the material frame')
        return original_lookup(build,phase,angles)
    def committed_phase(build,phase):
        if phase not in build.r760_states:
            raise ValueError('the two-order material phase parameter was not charged before frame construction')
    mod.triple.lookup=committed_lookup
    mod.R760Build.set_phase=committed_phase

    def tsqr(raw,residual,identity,stage):
        ctx=state['operator']
        return operator.original_first(raw,residual,identity,stage,ctx['frame'],ctx['link'],state['paid'])
    qr.tsqr_factor=tsqr

    def bound(label,name):
        engine=original_material.weak.bound_module(label,name)
        if name!='r732_disk_solver.py':return engine
        engine.FILES=(*engine.FILES,*NEW)
        engine.TYPES.update(R750Frame=previous.R750Frame,R750Build=previous.R750Build,
                            R760Frame=mod.R760Frame,R760Build=mod.R760Build)
        original_main=engine.main
        def start():
            relative=engine.Continuation;parent_paid=engine.Paid
            class Paid(parent_paid):
                def __init__(self,directory,seconds,settings):
                    t=time.monotonic();self.parent=original.Parent(conf.parent_receipt,engine,NEW,conf.parent_zip)
                    info=self.parent.spec
                    super().__init__(directory,seconds,{**settings,'R750_parent':info})
                    elapsed=self.start-t;self.start=t;self.end-=elapsed;self.deadline-=elapsed;self.io+=elapsed
                    if (self.parent.meta['phases']!=list(engine.PHASES) or self.parent.meta['degrees']!=list(engine.DEGREES)
                            or self.parent.meta['build']!=engine.OPTIONS or self.parent.level!=settings['level']):
                        raise ValueError('R760 requires the original R750 physical phases and numerical instruments')
                    self.level=settings['level'];self.node={};self.oldnode={}
                    self.grid={};self.oldgrid={};self.paid_angles={};self.loading={}
                    self.incoming=OrderedDict();self.incoming_bytes=0;self.import_time=0.
                    costs=self.root/'cost.jsonl'
                    if costs.exists():
                        with costs.open() as f:
                            for line in f:
                                rec=json.loads(line)
                                if rec['kind']=='r760_three_period_label_batch' and rec['event']=='saved':
                                    for angle in rec['key'][1]:self.paid_angles[(rec['key'][0],angle)]=rec['key']
                    state['paid']=self
                    engine.write_json(self.root/'r750-parent.json',dict(parent=info,original_finished=self.parent.records and
                        len(self.parent.records),old_integral_kernels=536,old_relative_values=27470,old_relative_J=459,
                        note='Only actual matched source rows are inherited; each use is recorded.'))

                def append(self,filename,value):
                    if filename=='cost.jsonl':
                        value=dict(value)
                        if value['event']=='start':self.import_time=0.
                        elif value['event'] in ('saved','failed'):
                            used=min(value['scientific_seconds'],self.import_time)
                            value['scientific_seconds']-=used;value['original_import_seconds']=used
                            value['archive_seconds']=value.get('archive_seconds',0.)+used;self.import_time=0.
                    return super().append(filename,value)

                def acquire(self,kind,key,keep=False):
                    path=self.parent.key(kind,key)[0]
                    if path in self.incoming:
                        val,size=self.incoming.pop(path);self.incoming[path]=(val,size);return val
                    begin=time.monotonic();val=self.parent.receipt(kind,key)
                    elapsed=time.monotonic()-begin;self.io+=elapsed
                    if self.current is not None:self.import_time+=elapsed
                    self.now['imported_R750_'+kind]+=1
                    z=self.parent.zip.getinfo(path)
                    self.append('r750-imports.jsonl',dict(kind=kind,key=key,member=path,parent=self.parent.ident,
                        bytes=z.file_size,crc32=z.CRC,sha256=self.parent.bytes_sha[path],archive_seconds=elapsed))
                    if keep:
                        size=sum(a.nbytes for a in val.values() if isinstance(a,np.ndarray))
                        if size<=120*2**20:
                            while self.incoming and self.incoming_bytes+size>120*2**20:
                                _,(_,old)=self.incoming.popitem(last=False);self.incoming_bytes-=old
                            self.incoming[path]=(val,size);self.incoming_bytes+=size
                    return val

                def phase(self,phase):
                    build=self.build
                    if phase not in build.r760_states:
                        flags=(False,True) if phase<=.08 else (False,)
                        record={}
                        for small in flags:
                            key=[phase,small,32,48,engine.array_id(build.r760_profile['ell_breaks'])]
                            record[small]=super().get('r760_meridian_phase_parameter',key,
                                lambda small=small:mod.moments.phase_parameters(build,phase,build.r760_profile,small))
                        build.r760_states[phase]=record

                def ensure(self,phase,angles):
                    if phase not in self.build.rings:
                        self.build.rings[phase]=self.get('phase_ring',[phase],lambda:self.build.target(phase))
                    if phase not in self.build.pulse_cache:
                        self.build.pulse_cache[phase]=self.get('phase_pulses',[phase],lambda:self.build.pulses(phase))
                    self.phase(phase)
                    if not (0.<phase<=.08):return
                    b=self.build;known=b.r760_label_states.setdefault(phase,{})
                    needed=[float(s) for s in np.unique(angles) if float(s) not in known]
                    cached={engine.plain(self.paid_angles[(phase,s)]):self.paid_angles[(phase,s)]
                            for s in needed if (phase,s) in self.paid_angles}
                    for key in cached.values():self.load_batch(phase,key,None)
                    new=[s for s in needed if s not in known]
                    for lo in range(0,len(new),24):
                        labels=new[lo:lo+24];key=[phase,labels,32,48]
                        def solve(labels=labels):
                            ss=np.array(labels)
                            broad=mod.triple.solve_labels(b,phase,ss,48);check=mod.triple.solve_labels(b,phase,ss,32)
                            e=np.max(abs(broad['parameters']-check['parameters']),axis=1)
                            de=np.max(abs(broad['parameter_sigma']-check['parameter_sigma']),axis=1)
                            if max(e)>2.e-8 or max(de)>2.e-6:raise ArithmeticError('independent true R760 inverses disagree')
                            return dict(fine=broad,independent=check,error=e,sigma_error=de)
                        self.load_batch(phase,key,solve)

                def load_batch(self,phase,key,fn):
                    record=super().get('r760_three_period_label_batch',key,fn)
                    fine=record['fine'];known=self.build.r760_label_states.setdefault(phase,{})
                    if list(fine['labels'])!=key[1]:raise ValueError('different true material angle batch')
                    for j,s in enumerate(key[1]):
                        known[s]={k:v[j] for k,v in fine.items() if isinstance(v,np.ndarray)}
                        known[s].update(independent_parameter_error=record['error'][j],
                                        independent_sigma_error=record['sigma_error'][j])
                        self.paid_angles[(phase,s)]=key

                def get(self,kind,key,compute):
                    if kind=='source_build':
                        source=self.acquire(kind,key)
                        if source.seed_identity!=self.parent.source_id:raise ValueError('different paid R750 physical source')
                        profile=super().get('r760_actual_full_terminal_moments',[32,48,64],
                                            lambda:mod.moments.solve_profile(source))
                        self.build=mod.R760Build.from_paid(source,profile)
                        return self.build
                    if kind in ('phase_ring','phase_pulses') and self.parent.has(kind,key):return self.acquire(kind,key)
                    if kind=='native_nodes':
                        pp,lev=key;k=(pp,lev)
                        if k not in self.oldnode:self.oldnode[k]=self.acquire(kind,key)
                        def extended():
                            r,s=self.oldnode[k];cuts=self.build.r760_profile['ell_breaks']
                            shift={'train':.5,'validation':.319,'qualification':.173}[pp]
                            return (np.unique(np.r_[r,self.build.radius_at(np.r_[cuts,cuts[:-1]+shift*np.diff(cuts)])]),
                                    np.unique(np.r_[s,mod.shoulders.true_angles(self.build,pp)]))
                        val=super().get(kind,key,extended);self.node[k]=val;return val
                    if kind=='native_frame':
                        phase,degree,pp,lev=key[:4];r,s=self.node[pp,lev]
                        self.ensure(phase,s);ro,so=self.oldnode[pp,lev]
                        pk=[phase,degree,pp,lev,engine.array_id(ro),engine.array_id(so)]
                        def make():
                            if self.parent.has('native_frame',pk):
                                return mod.merge_original_tensor(self.acquire('native_frame',pk),self.build,phase,r,s)
                            return mod.R760Frame(self.build,phase,r[:,None],s[None,:],degree)
                        return super().get(kind,key,make)
                    if kind=='r750_actual_release_probe':
                        v=np.array([.2061,.84625,.9474,.9474]);ring=self.build.ring
                        ss=(3+ring.LU-v)/ring.length;ss[-1]=(1+v[-1])/ring.length
                        self.ensure(key[0],ss)
                    if kind=='r750_ray_rule':
                        kk=tuple(key)
                        if kk not in self.oldgrid:self.oldgrid[kk]=self.acquire(kind,key)
                        val=super().get(kind,key,compute);self.grid[kk]=val;return val
                    if kind=='r750_true_ray_kernel':
                        return super().get(kind,key,lambda:self.kernel(key))
                    if kind=='nine_angular_derivatives':
                        c=state['operator'];return super().get(kind,key,
                            lambda:operator.channels(c['frame'],c['q'],c['link'],self))
                    if kind=='r750_complete_curl_csr':
                        c=state['operator']
                        if not self.filename(kind,key).is_file() and c.get('channels') is None:
                            c['channels']=super().get('nine_angular_derivatives',key,None)
                        return super().get(kind,key,lambda:operator.physical_csr(
                            c['frame'],c['q'],c['channels'],c['link'],self))
                    return super().get(kind,key,compute)

                def parent_parts(self,key):
                    phase,degree,pp,lev,order,ident,lo,hi=key
                    ss=self.node[pp,lev][1][lo:hi];so=self.oldnode[pp,lev][1]
                    prior=[phase,degree,pp,lev,order,engine.array_id(so)]
                    at=np.searchsorted(so,ss);hit=at<len(so);hit[hit]=so[at[hit]]==ss[hit]
                    found=[]
                    for start in np.unique(8*(at[hit]//8)):
                        ids=np.flatnonzero(hit&(at>=start)&(at<start+8))
                        pk=prior+[int(start),min(int(start)+8,len(so))]
                        if self.parent.has('r750_true_ray_kernel',pk):
                            found.append((ids,pk,at[ids]-start))
                    return ss,found

                def kernel(self,key):
                    phase,degree,pp,lev,order,_,_,_=key
                    ss,found=self.parent_parts(key);gr=self.grid[pp,lev,order];pg=self.oldgrid[pp,lev,order]
                    batches=[];used=np.zeros(len(ss),dtype=bool)
                    for ids,pk,columns in found:
                        prev=original.part_angles(self.acquire('r750_true_ray_kernel',pk,True),columns)
                        batches.append(kernels.kernel(self.build,phase,degree,ss[ids],gr,(pg,prev)))
                        used[ids]=True
                    if not np.all(used):batches.append(kernels.kernel(self.build,phase,degree,ss[~used],gr))
                    return original.join_angles(batches,ss)

                def position(self,key,q,load,derivative,ids=None):
                    phase,degree,pp,lev,order=key[:5];ng=3*len(previous.tags(degree));oldq=q[:ng]
                    pk=key+[engine.array_id(q)];kind='r760_relative_J' if derivative else 'r760_relative_value'
                    if self.filename(kind,pk).is_file():return super().get(kind,pk,None)
                    part=load();ss,found=self.parent_parts(key)
                    prevkind='r750_relative_jacobian' if derivative else 'r750_relative_position'
                    gr=self.grid[pp,lev,order];pg=self.oldgrid[pp,lev,order]
                    def calculate():
                        shape=(len(ss),3,len(q)) if derivative else (len(ss),3)
                        answer=np.empty(shape);done=np.zeros(len(ss),dtype=bool);work=[]
                        for take,orig,cols in found:
                            rk=orig+[engine.array_id(oldq)]
                            if not self.parent.has(prevkind,rk):continue
                            oldpart=self.acquire('r750_true_ray_kernel',orig,True)
                            stored=self.acquire(prevkind,rk)
                            vals=stored['block'].reshape(-1,3,len(oldq)) if derivative else stored
                            for j,k in zip(take,cols,strict=True):
                                a=original.part_angles(oldpart,[k]);b=original.part_angles(part,[j])
                                answer[j],usage=conserved.adopt(a,b,pg,gr,oldq,q,vals[k],derivative)
                                work.append(dict(angle=float(ss[j]),**usage));done[j]=True
                        if not np.all(done):
                            fresh=original.part_angles(part,np.flatnonzero(~done))
                            val=previous_ray.evaluate(fresh,q,derivative)
                            answer[~done]=val.reshape(answer[~done].shape)
                        if not np.isfinite(answer).all():raise ArithmeticError('incomplete R760 integral rows')
                        if not derivative:return dict(value=answer,original_integrals=work)
                        block=answer.reshape(3*len(ss),len(q));errors=[]
                        for j in ids:
                            z=q.astype(complex);z[j]+=1.e-24j
                            truth=previous_ray.evaluate(part,z).imag.ravel()/1.e-24
                            errors.append(float(np.max(abs(truth-block[:,j]))/max(1.,np.max(abs(truth)))))
                        if max(errors)>2.e-10:raise ArithmeticError('transported true R760 position columns failed complex-step')
                        return dict(block=block,independent_columns=ids,scaled_check_defects=np.array(errors),original_integrals=work)
                    return super().get(kind,pk,calculate)

            engine.Paid=Paid
            class Relative(relative):
                def __init__(self,paid,level,iterations):
                    super().__init__(paid,level,iterations)
                    self.audited=set()

                def setup(self,phase,degree):
                    fr=super().setup(phase,degree)
                    if (phase,degree) in self.audited:return fr
                    for pp in ('train','validation'):
                        f=fr[pp];key=[phase,degree,pp,self.level]
                        if not self.p.filename('r760_full_native_seed_jets',key).is_file():
                            self.p.get('r760_full_native_seed_jets',key,lambda f=f:mod.six_jet_and_curl(f,self.build,phase))
                    self.audited.add((phase,degree))
                    return fr

                def select_start(self,phase,degree,q):
                    key=[phase,degree]
                    if self.s.get('r760_selected_at')==key:return
                    if self.s['iteration'] or self.s['line']:
                        raise ValueError('initial R760 comparison cannot replace a live line search')
                    candidates={}
                    def register(name,vec):
                        token=engine.array_id(vec)['sha256']
                        if token in candidates:candidates[token][0].append(name)
                        else:candidates[token]=([name],vec.copy())
                    register('continued',q);register('actual_zero_three_period_or_full_meridian',np.zeros_like(q))
                    retained=self.p.parent.warm(phase)
                    if retained is not None and retained[0]<=degree:
                        d,oldq=retained
                        prev=previous.padded(oldq,d,degree) if d!=degree else oldq
                        vec=np.zeros_like(q);vec[:len(prev)]=prev
                        register('original_R750_at_this_phase',vec)
                    scores=[];best=None
                    for names,vector in candidates.values():
                        results=[]
                        for purpose in ('train','validation'):
                            f=self.frames[purpose]
                            ck=[phase,degree,purpose,self.level,engine.array_id(vector)]
                            kind='r760_initial_candidate_score'
                            if self.p.filename(kind,ck).is_file():report=self.p.get(kind,ck,None)
                            else:
                                value=self.measured_field(phase,degree,purpose,vector,f)
                                report=self.p.get(kind,ck,lambda:engine.metrics(value,f))
                            results.append(report)
                        rank=(max(z['rms'] for z in results),max(z['relative_peak'] for z in results))
                        scores.append(dict(labels=names,q=engine.array_id(vector),controls=vector.tolist(),
                              train=results[0],validation=results[1],rank=rank))
                        if best is None or rank<best[0]:best=(rank,vector)
                    q[:]=best[1];self.s['q']=q.tolist();self.s['r760_selected_at']=key
                    self.p.append('r760-candidates.jsonl',dict(phase=phase,degree=degree,parent=self.p.parent.ident,
                                  candidates=scores,selected=engine.array_id(q)))
                    self.put()

                def field(self,phase,degree,pp,q,frame):
                    if pp=='train':self.select_start(phase,degree,q)
                    return self.measured_field(phase,degree,pp,q,frame)

                def measured_field(self,phase,degree,pp,q,frame):
                    oldn=3*len(previous.tags(degree));prior=[phase,degree,pp,self.level,engine.array_id(q[:oldn])]
                    key=[phase,degree,pp,self.level,engine.array_id(q)]
                    def native():
                        if not self.p.parent.has('curl',prior):return frame.curl(q).reshape(-1,3)
                        link=operator.native_parent(frame,q,phase,prior,self.p.oldnode[pp,self.level+(pp=='validation')])
                        mask=link['safe'];rows=link['rows'][mask]
                        if not len(rows):return frame.curl(q).reshape(-1,3)
                        result=np.empty((len(frame.r),3))
                        result[rows]=self.p.acquire('curl',prior).reshape(-1,3)[mask]
                        ix=np.setdiff1d(np.arange(len(frame.r)),rows,assume_unique=True)
                        for lo in range(0,len(ix),256):
                            ii=ix[lo:lo+256];part=operator.thin(frame,ii);part.shape=(len(ii),)
                            result[ii]=mod.R760Frame.read(part,q)
                        return result
                    work=self.p.get('r760_curl_rows',key,native)
                    if self.p.filename('r760_all_periods',key).is_file():moment=self.p.get('r760_all_periods',key,None)
                    else:
                        blocks=[self.p.position(k,q,load,False)['value'] for k,load in self.pieces(phase,degree,pp,frame)]
                        moment=self.p.get('r760_all_periods',key,lambda:np.concatenate(blocks))
                    if not np.any(q) and not self.p.filename('r760_signed_seed_period_check',key).is_file():
                        ss=frame.s.reshape(frame.shape)[0];terms=[]
                        for lo in range(0,len(ss),24):
                            seg=ss[lo:lo+24];order=40 if pp=='train' else 52
                            sk=[phase,pp,self.level,order,engine.array_id(seg)]
                            rec=self.p.get('r760_independent_true_seed_period',sk,
                                     lambda:kernels.relative_seed(self.build,phase,seg,order))
                            terms.append(rec['outward_to_inward_residual'])
                        def crosscheck():
                            outward=np.concatenate(terms);err=np.max(abs(outward+moment),axis=0)
                            if not np.isfinite(err).all() or max(err)>4.e-8:
                                raise ArithmeticError('the genuine radial integrals disagree in opposite orientations')
                            return dict(physical_relative_periods=moment,outer_to_inner_formula=outward,
                                        signed_discrepancy_by_axis=err,expected_opposite_orientation=True)
                        self.p.get('r760_signed_seed_period_check',key,crosscheck)
                    return np.concatenate((work,np.sqrt(len(work)/len(moment))*moment))

                def operator(self,phase,degree,q,frame,residual):
                    from scipy.sparse import csr_matrix,vstack
                    key=[phase,degree,self.level,engine.array_id(q)];ng=3*len(previous.tags(degree))
                    prior=[phase,degree,self.level,engine.array_id(q[:ng])]
                    link=operator.native_parent(frame,q,phase,prior,self.p.oldnode['train',self.level])
                    state['operator']=dict(frame=frame,q=q,link=link)
                    stage=lambda kind,part,fn:self.p.get(kind,key+part,fn)
                    if self.p.filename('tsqr_svd',key+['complete']).is_file():return stage('tsqr_svd',['complete'],None)
                    if self.p.filename('full_sparse_jacobian',key).is_file():
                        return tsqr(self.p.get('full_sparse_jacobian',key,None),residual,engine.array_id,stage)
                    if not self.p.filename('r750_complete_curl_csr',key).is_file():
                        state['operator']['channels']=self.p.get('nine_angular_derivatives',key,None)
                    raw=self.p.get('r750_complete_curl_csr',key,None)
                    state['operator'].pop('channels',None);ids=raw['sampled_columns']
                    blocks=[self.p.position(k,q,load,True,ids) for k,load in self.pieces(phase,degree,'train',frame)]
                    def combine():
                        scale=np.sqrt(len(frame.r)/frame.shape[-1])
                        full=vstack([operator.csr(raw)]+[csr_matrix(scale*b['block']) for b in blocks],format='csr')
                        return {**operator.raw(full),'sampled_columns':ids,'scaled_check_defects':np.maximum.reduce(
                              [raw['scaled_check_defects']]+[b['scaled_check_defects'] for b in blocks]),
                              'true_native_curl_rows':raw['shape'][0],'true_position_rows':3*frame.shape[-1]}
                    return tsqr(self.p.get('full_sparse_jacobian',key,combine),residual,engine.array_id,stage)

                def qualify(self,phase,degree,q):
                    record=self.s['current'];key=[phase,degree,engine.array_id(q)]
                    if record['phase']!=phase or record['q']!=key[-1]:raise ValueError('unpaired candidate qualification')
                    if phase==0 and not np.any(q):
                        oldq=np.zeros(3*len(previous.tags(degree)));pk=[phase,degree,engine.array_id(oldq)]
                        if self.p.parent.has('qualification',pk):
                            def adopt():
                                original_check=self.p.acquire('qualification',pk)
                                return {**original_check,'original_R750_q':pk[-1],
                                    'actual_R760_q':key[-1],'exact_source_adopted':True,
                                    'archive_is_in_original_artifact':self.p.parent.ident,
                                    'new_material_grids_checked_separately':True}
                            ans=self.p.get('r760_identical_source_qualification',key,adopt)
                            self.p.get('sampled_shell_hull',key,lambda:self.p.acquire('sampled_shell_hull',pk))
                            return ans
                    if not record['finite_fit']:
                        return self.p.get('r760_deferred_geometry',key,lambda:dict(status='deferred after actual two-grid rejection',
                              phase=phase,q=key[-1],train=record['train'],validation=record['validation'],
                              continuous_material_and_reach='open',parent=self.p.parent.ident))
                    _,s=self.build.nodes(self.level,'qualification');fd=2.4e-7/(self.build.ring.length*self.level)
                    self.p.ensure(phase,np.unique(np.r_[s,s-fd,s+fd,s[::4]-fd/2,s[::4]+fd/2]))
                    allrec=self.s['records']
                    existing=[x for x in allrec if self.p.filename('sampled_shell_hull',[x['phase'],x['degree'],x['q']]).is_file()]
                    self.s['records']=existing
                    try:result=super().qualify(phase,degree,q)
                    finally:self.s['records']=allrec
                    result['unpaid_cross_phase_hulls']=[x['phase'] for x in allrec if x not in existing]
                    return result
            engine.Continuation=Relative
            original_main()
        engine.main=start;return engine
    geometry.weak.bound_module=bound
    def emit(tag,*args,**kw):
        tag={'R750_ANNULUS_FINAL':'R760_ANNULUS_FINAL','R750_PHASE':'R760_PHASE','R750_RELEASE_CHECK':'R760_RELEASE_CHECK'}.get(tag,tag)
        builtins.print(tag,*args,**kw)
    spec=importlib.util.spec_from_file_location('_r760_pipeline',HERE/'r750_annulus_solver.py')
    driver=importlib.util.module_from_spec(spec);spec.loader.exec_module(driver);driver.builtins=SimpleNamespace(print=emit)
    replacement={'r743_early_material_disk':geometry,'r750_rigid_annulus':physical,
                 'r750_relative_boundary':rays,'r742_native_tsqr':qr}
    previous_modules={k:sys.modules[k] for k in replacement};sys.modules.update(replacement)
    if not any(x=='--state' or x.startswith('--state=') for x in sys.argv[1:]):sys.argv.extend(('--state','r760-paid-state'))
    try:driver.main()
    finally:sys.modules.update(previous_modules)


if __name__=='__main__':main()
