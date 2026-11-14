#!/usr/bin/env python3
"""Persist the complete boundary QR and both exact substitution passes.

All factor seeds, state rows, parameter entries and affine right-hand sides
are retained.  Disk state is an implementation checkpoint only: the caller
still checks every answer against the independent complete collocation
operator with the original 5e-8 backward gate.
"""
from __future__ import annotations
import hashlib
import json
import os
import resource
import time
from pathlib import Path
from types import SimpleNamespace
import numpy as np
from scipy.linalg import lu_solve, solve_triangular
from numpy.lib.format import open_memmap
from fourfold_codazzi_block_qr_checkpointed import CheckpointBoundaryQR
from fourfold_codazzi_block_qr_collocation import apply_qt


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def array_digest(*arrays, label=''):
    result=hashlib.sha256(label.encode())
    for value in arrays:
        a=np.ascontiguousarray(value)
        result.update(str((a.shape,a.dtype.str)).encode());result.update(a.tobytes())
    return result.hexdigest()


def atomic_npz(path,**values):
    path=Path(path);temporary=path.with_name(path.name+'.partial')
    with temporary.open('wb') as stream:np.savez(stream,**values)
    os.replace(temporary,path)


def atomic_json(path,value):
    path=Path(path);temporary=path.with_name(path.name+'.partial')
    temporary.write_text(json.dumps(value,indent=2,allow_nan=False)+'\n')
    os.replace(temporary,path)


class DiskSeeds:
    """The seed-store protocol used by CheckpointBoundaryQR; no resident seeds."""
    def __init__(self,directory,records=None):
        self.directory=Path(directory);self.directory.mkdir(parents=True,exist_ok=True)
        self.records={} if records is None else {int(k):v for k,v in records.items()}

    def path(self,index):return self.directory/f'seed-{index:06d}.npy'

    def __setitem__(self,index,value):
        path=self.path(index);temporary=path.with_name(path.name+'.partial')
        with temporary.open('wb') as stream:np.save(stream,value,allow_pickle=False)
        os.replace(temporary,path)
        self.records[int(index)]=dict(sha256=sha(path),nbytes=int(value.nbytes))

    def __getitem__(self,index):
        path=self.path(index)
        if sha(path)!=self.records[int(index)]['sha256']:
            raise RuntimeError('the complete saved boundary seed failed its hash')
        return np.load(path,mmap_mode='r',allow_pickle=False)

    def values(self):
        # The parent's only iteration is its exact retained-size accounting.
        return (SimpleNamespace(nbytes=x['nbytes']) for x in self.records.values())


class PersistentCheckpointBoundaryQR(CheckpointBoundaryQR):
    @property
    def seeds(self):return self._seed_store

    @seeds.setter
    def seeds(self,initial):
        self._seed_store=DiskSeeds(self.directory/'seeds')
        for index,value in initial.items():self._seed_store[index]=value

    def __init__(self,n,nodes,left,right,parameter,block_factory,history,*,
                 directory,fingerprint,span=8):
        self.directory=Path(directory)/fingerprint
        self.directory.mkdir(parents=True,exist_ok=True)
        self.fingerprint=fingerprint
        manifest=self.directory/'factor.json';arrays=self.directory/'factor.npz'
        if manifest.exists():
            saved=json.loads(manifest.read_text())
            if (not saved['complete'] or saved['fingerprint']!=fingerprint
                or saved['n']!=n or saved['nodes']!=nodes or saved['span']!=span
                or saved['factor_sha256']!=sha(arrays)):
                raise RuntimeError('the complete factor checkpoint identity differs')
            self.n,self.nodes,self.span,self.history=n,nodes,span,history
            self.block_factory=block_factory;self.file=None
            self.cache_start=-1;self.cache=[];self.p=int(saved['p'])
            self.minimum_local_diagonal=saved['minimum_local_diagonal']
            self.end_condition=saved['end_condition'];self.record_bytes=saved['record_bytes']
            with np.load(arrays,allow_pickle=False) as data:
                for name in ('left_rows','right_rows','c0','initial_r','right_boundary','right_scale','end'):
                    setattr(self,name,data[name].copy())
                self.end_lu=(data['lu'].copy(),data['pivots'].copy())
            self._seed_store=DiskSeeds(self.directory/'seeds',saved['seeds'])
            if set(self._seed_store.records)!=set(range(0,nodes,span)):
                raise RuntimeError('incomplete disk boundary seed index')
            item=dict(kind='restored_complete_boundary_QR_factor',fingerprint=fingerprint,
                radial_nodes=nodes,state_dimension=n,parameter_dimension=1,
                all_Fourier_couplings_retained=True,all_saved_seed_hashes_checked_when_used=True,
                original_factorization=saved['original_factorization'])
            history.append(item);print(item,flush=True)
        else:
            super().__init__(n,nodes,left,right,parameter,block_factory,history,span=span)
            atomic_npz(arrays,left_rows=self.left_rows,right_rows=self.right_rows,c0=self.c0,
                initial_r=self.initial_r,right_boundary=self.right_boundary,right_scale=self.right_scale,
                end=self.end,lu=self.end_lu[0],pivots=self.end_lu[1])
            saved=dict(complete=True,fingerprint=fingerprint,n=n,nodes=nodes,p=self.p,span=span,
                minimum_local_diagonal=self.minimum_local_diagonal,end_condition=self.end_condition,
                record_bytes=self.record_bytes,seeds=self._seed_store.records,
                factor_sha256=sha(arrays),original_factorization=history[-1])
            atomic_json(manifest,saved)
            print(dict(persisted_complete_QR_factor=str(manifest),
                seed_bytes=sum(x['nbytes'] for x in self._seed_store.records.values()),
                maximum_resident_recomputed_factor_bytes=span*self.record_bytes),flush=True)

    def solve(self,residual):
        tick=time.monotonic();n,p,nodes=self.n,self.p,self.nodes
        if residual.shape!=(n*nodes+1,):raise RuntimeError('wrong complete RHS dimension')
        identity=array_digest(residual,label=self.fingerprint)
        directory=self.directory/('rhs-'+identity);directory.mkdir(exist_ok=True)
        progress=directory/'progress.npz';top_path=directory/'top.npy';state_path=directory/'state.npy'
        body=residual[:n*(nodes-1)].reshape((n,nodes-1),order='F')
        boundary=residual[n*(nodes-1):]
        def persist(stage,index,current=None,parameter=0.):
            values=dict(stage=np.array(stage),next_index=np.array(index),parameter=np.array(parameter),
                factor=np.array(self.fingerprint),rhs=np.array(identity))
            if current is not None:values['current']=current
            atomic_npz(progress,**values)
            hook=getattr(self,'checkpoint_hook',None)
            if hook is not None:hook(stage,index)
        if progress.exists():
            with np.load(progress,allow_pickle=False) as saved:
                if str(saved['factor'])!=self.fingerprint or str(saved['rhs'])!=identity:
                    raise RuntimeError('the complete substitution checkpoint identity differs')
                stage=str(saved['stage']);index=int(saved['next_index']);parameter=float(saved['parameter'])
                current=saved['current'].copy() if 'current' in saved else None
            top=np.load(top_path,mmap_mode='r+',allow_pickle=False)
            print(dict(resumed_complete_QR_substitution=stage,next_index=index,rhs=identity),flush=True)
        else:
            top=open_memmap(top_path,mode='w+',dtype=np.float64,shape=(nodes-1,n))
            current=solve_triangular(self.initial_r.T,boundary[self.left_rows],lower=True,check_finite=False)
            stage,index,parameter='forward',0,0.;top.flush();persist(stage,index,current)
        if top.shape!=(nodes-1,n):raise RuntimeError('incomplete saved forward row array')
        if stage=='forward':
            if not 0<=index<=nodes-1 or current.shape!=(p,):
                raise RuntimeError('invalid complete forward resume point')
            for i in range(index,nodes-1):
                packed,tau,_,_,norm_r,scale=self.read(i)
                result=apply_qt(packed,tau,np.r_[current,scale*body[:,i]])[:,0]
                top[i]=result[:n]
                current=solve_triangular(norm_r.T,result[n:],lower=True,check_finite=False)
                if (i+1)%self.span==0 or i==nodes-2:
                    top.flush();persist('forward',i+1,current)
                if (i+1)%64==0 or i==nodes-2:
                    print(dict(full_QR_substitution='forward',completed_blocks=i+1,expected_blocks=nodes-1,
                        seconds=time.monotonic()-tick,
                        peak_resident_KiB=int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
            end=lu_solve(self.end_lu,np.r_[current,self.right_scale*boundary[self.right_rows]],check_finite=False)
            parameter=float(end[-1]);state=open_memmap(state_path,mode='w+',dtype=np.float64,shape=(n,nodes))
            state[:,-1]=end[:n];state.flush();stage,index='backward',nodes-2
            persist(stage,index,parameter=parameter)
        else:
            if stage not in ('backward','complete'):raise RuntimeError('unknown complete substitution phase')
            state=np.load(state_path,mmap_mode='r+',allow_pickle=False)
        if state.shape!=(n,nodes):raise RuntimeError('incomplete saved backward state array')
        if stage=='backward':
            if not -1<=index<=nodes-2:raise RuntimeError('invalid complete backward resume point')
            for i in range(index,-1,-1):
                packed,_,next_block,param,_,_=self.read(i)
                state[:,i]=solve_triangular(packed[:n],top[i]-next_block@state[:,i+1]-param*parameter,
                    lower=False,check_finite=False)
                if i%self.span==0:
                    state.flush();persist('backward',i-1,parameter=parameter)
                if i%64==0:
                    print(dict(full_QR_substitution='backward',remaining_blocks=i,expected_blocks=nodes-1,
                        seconds=time.monotonic()-tick,
                        peak_resident_KiB=int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
            state.flush();persist('complete',-1,parameter=parameter)
        answer=np.r_[state.ravel(order='F'),parameter]
        if not np.all(np.isfinite(answer)):raise RuntimeError('nonfinite complete resumed QR answer')
        return answer
