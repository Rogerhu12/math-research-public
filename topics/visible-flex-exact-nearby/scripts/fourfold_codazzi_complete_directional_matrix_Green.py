#!/usr/bin/env python3
"""Complete directional finite193 Green bounds from immutable same-F matrix data.

Both128-column channels retain full signed193 covariance and even mean.
Only new coordinate maps, two matrix sweeps and posterior contractions are
computed. Old targets, F polynomials, source/output Grams and scalar
positive Green ports are immutable inputs. No infinite inverse is claimed.
"""
from __future__ import annotations
import argparse,fcntl,hashlib,json,os,shutil,time
from collections import OrderedDict
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import arb,arb_mat,ctx
import fourfold_codazzi_same_F_triangular_source_Gram_pilot as base
import fourfold_codazzi_complete_same_F_directional_matrices_v2 as local
import fourfold_codazzi_finite193_L2_Green_kernel as old
import fourfold_codazzi_finite193_cached_interface_impulse_gains as impulse_source

KIND='actual_complete_direction_preserving_finite193_matrix_Green_v1'
LOCAL_SOURCE='e2cedf8860bbf807a3db66718fd9d195b5c312776f1902d492aa8180e1525d59'
LOCAL_WORKER='71b203d54afc982de4ac762a7486cd99bde7acbd9ca50d7ca9c486a283c1326b'
LOCAL_MANIFEST='8d334ee75c0cf78a13b31483ceb495194c73e7cbcf57c1eeec3f447da17cab19'
BASE_SOURCE='2173281e0558cbbabf3a21d506ae3cf9b0253a9406aa2d9d15b8681e8faeaf44'
PROFILE=local.PROFILE
PROFILE_PROCESS=local.PROFILE_PROCESS
PLAN=local.ORIGINAL_PLAN_NATIVE
PILOT=local.PILOT_NATIVE
KERNEL='ac4441cb98afabbbc646697434caebf464a22f702e2d0fa7d8e5910efd7ef448'
KERNEL_SOURCE='5b8f83906d36363266977441427add053a6ed05625525cfd000e05e03360b3db'
KERNEL_PROCESS='641c0ca655a9f0ac7c49a30c4b5fd44a4b79552d7c8f8f4533f086d6d2f88800'
IMPULSE='fbba350708fb89366272641433e9c2899c4ec04027616650b4317969105bcd37'
IMPULSE_SOURCE='12e40b3849f4c1f29b1c0da0a52825afd710ab4cb70e09b539760d6672295439'
IMPULSE_REVIEWED_PROCESS='b55c2df02439b910c1e6e46fb78c2391ca135138421e2f05ee05a14dcb5de468'
IMPULSE_WORKER='f7def106a57225f5a456f37da90df73947b3eb57c89dafa280592f170c983a69'
IMPULSE_MANIFEST='75b9039039a663a5fb8aad5a7f719e5fcea9edf648096441bc0777e25240a44c'
BOUNDARY='56db8a3498494bf48de14b50418010053bb6058c722c41993c894c463786dc25'
CUT='528e2f47d4572d7b90878abc542c3389d76d5fb326d7ef7c3390ef086d6266ba'
CHANNELS=('cross_reference','complete_cross_source_error')
WINDOWS=('whole_inner_body','fixed_complete_negative_phase_window')
N,P,Q=193,96,97
PHASE_RIGHT=base.PHASE_RIGHT
RIGHT=Fraction(9,10)
sha,read,save,canonical=base.sha,base.read,base.save,base.canonical
q,record,norm,exact,eye,zero=base.q,base.record,base.norm,base.exact,base.eye,base.zero
ball,up,block,transpose,trace=base.ball,base.up,base.block,base.transpose,base.trace
CHUNK=32


def nonnegative(value):
    v=arb(value).upper()
    if not v.is_finite():raise ArithmeticError('a complete directional bound is nonfinite')
    if v<0:raise ArithmeticError('a mathematically nonnegative directional bound has negative upper endpoint')
    return max(arb(0),v).upper()


def sqrt_upper(value):return nonnegative(value).sqrt().upper()


def dot_trace(A,B):
    if A.nrows()!=A.ncols() or A.nrows()!=B.nrows() or A.ncols()!=B.ncols():
        raise ValueError('the complete signed covariance trace dimensions differ')
    n=A.nrows()
    # These matrices are exactly symmetric. Signed off-diagonal products
    # remain intact until the entire quadratic trace has been evaluated.
    value=sum((A[i,i]*B[i,i] for i in range(n)),arb(0))
    value+=2*sum((A[i,j]*B[i,j] for i in range(n) for j in range(i+1,n)),arb(0))
    return nonnegative(value)


def sym(A):return (A+transpose(A))/2


def checked_inverse(A,name):
    if A.nrows()!=A.ncols():raise ValueError(name+' is not square')
    inverse=A.inv();n=A.nrows()
    fee=max(norm(inverse*A-eye(n)),norm(A*inverse-eye(n))).upper()
    if not fee<q(Fraction(1,10**30)):
        raise ValueError(name+' true inverse identity is not enclosed at the declared threshold')
    return inverse,record(fee)


def selected_twice(A):
    hi,H,_=base.choose(A)
    lo,L,_=base.choose(A-H)
    chosen=H+L
    if not np.isfinite(hi).all() or not np.isfinite(lo).all():
        raise ArithmeticError('a two-dyadic selected matrix is nonfinite')
    return hi,lo,chosen,norm(A-chosen).upper()


def pack_symmetric(A):
    if A.ndim!=2 or A.shape[0]!=A.shape[1] or not np.array_equal(A,A.T):
        raise ValueError('a saved covariance midpoint is not exactly symmetric')
    return np.asarray(A[np.triu_indices(A.shape[0])],dtype='<f8')


def unpack_symmetric(values,n):
    if values.shape!=(n*(n+1)//2,):
        raise ValueError('one packed signed covariance has the wrong complete dimension')
    A=np.empty((n,n),dtype='<f8');ii,jj=np.triu_indices(n)
    A[ii,jj]=values;A[jj,ii]=values
    return A


def covariance_bound(A,key,arrays):
    A=sym(A);n=A.nrows()
    hi,lo,chosen,rounding=selected_twice(A)
    # Select symmetric dyadics directly, since opposite entries enclose
    # the same exact value but must not be chosen independently.
    for i in range(n):
        for j in range(i):
            hi[i,j]=hi[j,i];lo[i,j]=lo[j,i]
    chosen=exact(hi)+exact(lo)
    rounding=norm(A-chosen).upper()
    lam,slack=base.exact_upper_float(rounding)
    upper=sym(chosen+eye(n)*slack)
    arrays[key+'_hi_triangle']=pack_symmetric(hi)
    arrays[key+'_lo_triangle']=pack_symmetric(lo)
    receipt=dict(dimension=n,hi_array_key=key+'_hi_triangle',lo_array_key=key+'_lo_triangle',
        exact_diagonal_slack_binary64_hex=lam.hex(),
        full_signed_matrix_rounding_upper=record(rounding),
        complete_trace_upper=record(nonnegative(trace(upper))),
        exact_bound='exact(hi)+exact(lo)+exact(slack)*I; no binary64 addition of hi and lo',
        complete_signed_covariance_and_mean_kept=True)
    return upper,receipt


def read_covariance(arrays,receipt):
    n=receipt['dimension']
    hi=unpack_symmetric(arrays[receipt['hi_array_key']],n)
    lo=unpack_symmetric(arrays[receipt['lo_array_key']],n)
    slack=q(Fraction(float.fromhex(receipt['exact_diagonal_slack_binary64_hex'])))
    if slack<0:raise ValueError('a covariance Loewner slack is negative')
    return exact(hi)+exact(lo)+eye(n)*slack


def array_file(root,receipt):
    origin=receipt['original_public_array_origin']
    if origin.get('repository')!='Rogerhu12/math-research-public':
        raise ValueError('one scientific array is not from the authorized public repository')
    artifact=origin['artifact'];file=receipt['file'];folder=origin.get('folder','matrices')
    if Path(artifact).name!=artifact or Path(file).name!=file or folder!='matrices':
        raise ValueError('one scientific array origin path is not a safe original basename')
    return root/artifact/folder/file


class MatrixFiles:
    def __init__(self,root,profile,rows):
        self.root=root;self.profile=profile;self.rows=rows;self.cache=OrderedDict()
        self.verified=set()

    def load_receipt(self,receipt):
        key=receipt['sha256']
        if key in self.cache:
            self.cache.move_to_end(key);return self.cache[key]
        path=array_file(self.root,receipt)
        if not path.exists() or path.stat().st_size!=receipt['bytes'] or sha(path)!=key:
            raise ValueError('one original completed matrix or covariance array is absent or changed')
        with np.load(path,allow_pickle=False) as z:arrays={k:z[k].copy() for k in z.files}
        if set(arrays)!=set(receipt['arrays']):
            raise ValueError('one original scientific array key was added or lost')
        for name,A in arrays.items():
            r=receipt['arrays'][name]
            if (A.dtype!=np.dtype('float64') or str(A.dtype)!=r['dtype']
                or list(A.shape)!=r['shape'] or not np.isfinite(A).all()
                or base.raw_sha(A)!=r['raw_little_endian_array_sha256']):
                raise ValueError('one original raw scientific array identity changed')
        self.cache[key]=arrays;self.verified.add(key)
        if len(self.cache)>5:self.cache.popitem(last=False)
        return arrays

    def frame_values(self,index,side):
        row=self.rows[index];profile=self.profile['rows'][index]
        if index in base.INDICES:
            values=self.load_receipt(row['array_receipt'])['frame_'+side]
        else:
            values=self.load_receipt(row[side+'_frame_array_receipt'])['complete_frame']
        expected=profile['exact_'+side+'_anchor_array_sha256']
        if values.shape!=(N,N) or base.raw_sha(values[:,:P])!=expected:
            raise ValueError('the full frame changed one original Q column or its endpoint')
        return values

    def gram(self,index,kind,channel=None):
        row=self.rows[index];arrays=self.load_receipt(row['array_receipt'])
        if kind=='source':
            name='cross_reference' if channel=='cross_reference' else 'edge_y_unit'
            rec=row['source_Grams'][name];default='H_'+name+'_midpoint'
        else:
            name=kind;rec=row['output_Grams'][name]
            default={'full_weighted':'J_weighted_midpoint','full_physical':'J_physical_midpoint',
                     'negative_physical':'J_negative_physical_midpoint'}[name]
            if rec.get('exact_zero_matrix'):return zero()
        key=rec.get('saved_array_key',default);values=arrays[key]
        if values.ndim==1:values=unpack_symmetric(values,N)
        if values.shape!=(N,N) or not np.array_equal(values,values.T):
            raise ValueError('one original complete signed Gram is not symmetric193')
        slack=q(Fraction(float.fromhex(rec['exact_diagonal_slack_binary64_hex'])))
        if slack<0:raise ValueError('an original complete Gram slack is negative')
        G=exact(values)+eye()*slack
        if kind=='source' and channel=='complete_cross_source_error':
            E=up(row['source_definition']['full_true_weighted_cross_source_uniform_error'])
            G*=E*E
        return sym(G)

    def effective_port(self,index):
        row=self.rows[index];ar=self.load_receipt(row['array_receipt'])
        A,B,D=map(exact,(ar['T_A'],ar['T_B'],ar['T_D']))
        if (A.nrows(),A.ncols(),B.nrows(),B.ncols(),D.nrows(),D.ncols())!=(P,P,P,Q,Q,Q):
            raise ValueError('the complete triangular matrix dimensions changed')
        right=self.frame_values(index,'right');SR=exact(right)
        if index==0:
            next_values=right;Bc=zero(P,Q);Dc=eye(Q)
            coordinate=dict(exact_identity_at_true_cut=True,shared_Q_R_bytes_verified=True)
        else:
            next_values=self.frame_values(index-1,'left')
            w=self.profile['rows'][index]['exact_weight']
            nw=self.profile['rows'][index-1]['exact_weight']
            if (not np.array_equal(next_values[:,:P],right[:,:P])
                or w['exact_rho_right']!=nw['exact_rho_left']):
                raise ValueError('a free coordinate event changed the same physical Q or R')
            SN=exact(next_values);SNi,identity_fee=checked_inverse(SN,'the next exact full frame')
            C=SNi*SR
            fee=max(norm(block(C,0,P,0,P)-eye(P)),norm(block(C,P,N,0,P))).upper()
            if not fee<q(Fraction(1,10**30)):
                raise ValueError('the shared-Q coordinate map does not enclose its exact triangular identity')
            Bc=block(C,0,P,P,N);Dc=block(C,P,N,P,N)
            coordinate=dict(exact_identity_at_true_cut=False,shared_Q_R_bytes_verified=True,
                original_right_full_frame_array_sha256=base.raw_sha(right),
                next_left_full_frame_array_sha256=base.raw_sha(next_values),
                exact_first96_columns_canonical='[I96;0] because the original Q bytes are equal',
                numerical_identity_enclosure=record(fee),next_frame_inverse_identity=identity_fee)
        Beff=B+Bc*D;Deff=Dc*D
        Di,di_fee=checked_inverse(Deff,'the complete effective future block')
        coordinate['effective_future_inverse_identity']=di_fee
        return A,Beff,Di,exact(next_values),coordinate


def old_process_append_only(actual,reviewed):
    a,b=read(actual),read(reviewed)
    ca,cb=a.get('published_checkpoints',[]),b.get('published_checkpoints',[])
    if ({k:v for k,v in a.items() if k!='published_checkpoints'}
        !={k:v for k,v in b.items() if k!='published_checkpoints'}
        or ca[:min(len(ca),len(cb))]!=cb[:min(len(ca),len(cb))]):
        raise ValueError('an original artifact/repository process differs beyond appended publication receipts')
    return a


def gate(doc,name,condition):
    doc.setdefault('gates',[]).append(dict(name=name,passed=bool(condition)))
    if not condition:raise ValueError('complete matrix Green gate failed: '+name)


def input_identity(a):
    names=('matrix-data','matrix-process','profile','profile-process','green','green-process',
        'kernel','kernel-process','impulse','impulse-process','reviewed-impulse-process','boundary','nominal-cut')
    return {name:sha(getattr(a,name.replace('-','_'))) for name in names}


def inputs(a,doc):
    if sha(base.__file__)!=BASE_SOURCE or sha(local.__file__)!=LOCAL_SOURCE or sha(old.__file__)!=KERNEL_SOURCE:
        raise ValueError('one frozen matrix/Green mathematical source changed')
    if sha(impulse_source.__file__)!=IMPULSE_SOURCE:
        raise ValueError('the original complete impulse source changed')
    profile=local.profile_input(a.profile,a.profile_process)
    data,p=read(a.matrix_data),read(a.matrix_process)
    gate(doc,'actual_complete5970_same_F_matrix_cover_and_original_four_rows',
        data.get('kind')==local.KIND and data.get('phase')=='finish'
        and data.get('complete') and not data.get('failure')
        and data.get('source_sha256')==LOCAL_SOURCE and data.get('original_profile_sha256')==PROFILE
        and data.get('exact_plan_native_sha256')==PLAN and data.get('original_pilot_native_sha256')==PILOT
        and data.get('actual_complete_local_matrix_cells')==5970
        and data.get('complete_new_canonical_matrix_cells')==5966
        and data.get('reused_successful_pilot_cells')==4
        and data.get('original_successful_matrix_cells_recomputed')==0
        and data.get('old_target_or_validator_calls')==0
        and len(data.get('rows',[]))==5970
        and data.get('gates') and all(g['passed'] for g in data['gates'])
        and p.get('repository')=='Rogerhu12/math-research-public'
        and p.get('phase')=='finish' and str(p.get('run_id'))==str(a.matrix_run)
        and p.get('worker_source_sha256')==LOCAL_WORKER
        and p.get('input_manifest_sha256')==LOCAL_MANIFEST
        and (p.get('complete_native_sha256') is None or p.get('complete_native_sha256')==sha(a.matrix_data))
        and len([x for x in p.get('native_files',[]) if
            x.get('logical_file')=='native/complete5970-same-F-directional-matrix-data.json.gz'
            and x.get('sha256')==sha(a.matrix_data)])==1
        and (any(c.get('label')=='exact_all5970_same_F_matrix_cover_without_original_cell_recomputation'
            and c.get('actual_returncode')==0 for c in p.get('children',[]))
            or (p.get('original_complete_success_reused_without_child')
                and p.get('original_success_process_sha256'))))
    rows=data['rows']
    for i,row in enumerate(rows):
        r=profile['rows'][i]
        if (row.get('index')!=i or row.get('interval')!=r['interval'] or not row.get('complete')
            or row.get('original_complete_row_sha256')!=r['complete_original_row_canonical_json_sha256']
            or not row.get('same_patched_F_for_endpoints_inverse_and_all_Grams')):
            raise ValueError('one complete matrix row is not the same original exact reference')
        if i not in base.INDICES:local.validate_new_row(row,r)
        if row['source_definition'].get('cross_input_physical_high_modes')!=[97,160]:
            raise ValueError('one directional source lost its complete128 high input columns')
    green,events,weights=old.validate(a,doc)
    kernel=read(a.kernel);kp=read(a.kernel_process)
    gate(doc,'original_complete_true_ordinary_L2_Green_kernel_and_process',
        sha(a.kernel)==KERNEL and sha(a.kernel_process)==KERNEL_PROCESS
        and kernel.get('kind')==old.KIND and kernel.get('complete') and not kernel.get('failure')
        and kernel.get('source_sha256')==KERNEL_SOURCE
        and kernel.get('complete_finite193_ordinary_L2_source_inverse_bound_proved')
        and kernel.get('gates') and all(g['passed'] for g in kernel['gates'])
        and kp.get('complete_native_sha256')==KERNEL
        and any(c.get('label')=='actual_complete6391_ordinary_L2_Green_kernel_integrals'
            and c.get('actual_returncode')==0 for c in kp.get('children',[])))
    imp=read(a.impulse)
    if sha(a.reviewed_impulse_process)!=IMPULSE_REVIEWED_PROCESS:
        raise ValueError('the separately reviewed original impulse process changed')
    ip=old_process_append_only(a.impulse_process,a.reviewed_impulse_process)
    gate(doc,'all5970_true_individual_weighted_jump_gains_and_actual_public_process',
        sha(a.impulse)==IMPULSE and imp.get('kind')==impulse_source.KIND
        and imp.get('complete') and not imp.get('failure')
        and imp.get('source_sha256')==IMPULSE_SOURCE
        and imp.get('all_actual_interface_impulse_gains_proved')
        and len(imp.get('interface_impulse_rows',[]))==5970
        and imp.get('gates') and all(g['passed'] for g in imp['gates'])
        and ip.get('repository')=='Rogerhu12/math-research-public'
        and str(ip.get('run_id'))=='43649423561'
        and ip.get('worker_source_sha256')==IMPULSE_WORKER
        and ip.get('input_manifest_sha256')==IMPULSE_MANIFEST
        and ip.get('complete_native_sha256')==IMPULSE
        and any(c.get('actual_returncode')==0 for c in ip.get('children',[])))
    boundary,cut=read(a.boundary),read(a.nominal_cut)
    gate(doc,'complete_true97_boundary_including_mean_and_exact_nominal_matrix',
        sha(a.boundary)==BOUNDARY and sha(a.nominal_cut)==CUT
        and boundary.get('complete') and not boundary.get('failure')
        and len(boundary.get('gates',[]))==10 and all(g['passed'] for g in boundary['gates'])
        and boundary.get('exact_cut_anchor_array_sha256')==profile['rows'][0]['exact_right_anchor_array_sha256']
        and boundary.get('exact_waist_anchor_array_sha256')==profile['rows'][-1]['exact_left_anchor_array_sha256']
        and boundary.get('exact_cut_rho')==profile['rows'][0]['exact_weight']['exact_rho_right']
        and boundary.get('exact_waist_rho')==profile['rows'][-1]['exact_weight']['exact_rho_left']
        and cut.get('complete') and not cut.get('failure') and cut.get('exact_odd_block')=='I_96'
        and len(cut.get('rows',[]))==96
        and len(cut.get('independent_mean_row',{}).get('binary64_proposal_hex',[]))==97)
    return profile,rows,green,events,kernel,imp,boundary,cut


def source_blocks(H,V):
    Hpp=block(H,0,P,0,P);Hpq=block(H,0,P,P,N);Hqq=block(H,P,N,P,N)
    R=sym(Hpp-V*transpose(Hpq)-Hpq*transpose(V)+V*Hqq*transpose(V))
    return Hpp,Hpq,Hqq,R


def output_contraction(J,V,past_plus_current,Qleft):
    Jpp=block(J,0,P,0,P);Jpq=block(J,0,P,P,N);Jqq=block(J,P,N,P,N)
    Jeff=sym(transpose(V)*Jpp*V+transpose(V)*Jpq+transpose(Jpq)*V+Jqq)
    return nonnegative(dot_trace(Jpp,past_plus_current)+dot_trace(Jeff,Qleft))


class ChunkRows:
    """Each completed row is committed to a bounded chunk before the header.

    Scientific matrix arrays keep their original public artifact origin.
    Updating a partial copied chunk preserves every earlier row exactly.
    """
    def __init__(self,document,path,phase,previous=None,previous_root=None):
        self.document=document;self.path=path;self.phase=phase;self.root=path.parent
        self.entries=[];self.rows=[];self.pending=[]
        if previous:
            count=0
            for receipt in previous.get('row_chunks',[]):
                name=receipt['file'];p=previous_root/name
                if Path(name).name!=name or sha(p)!=receipt['sha256']:
                    raise ValueError('one exact successful sweep chunk changed')
                d=read(p)
                if (d.get('phase')!=phase or d.get('first_row')!=count
                    or d.get('source_sha256')!=sha(__file__)
                    or len(d.get('rows',[]))!=receipt['rows']
                    or not 0<len(d['rows'])<=CHUNK
                    or any(not r.get('complete') for r in d['rows'])):
                    raise ValueError('a successful matrix sweep chunk has another phase or incomplete row')
                expected=[i if phase=='backward' else 5969-i for i in range(count,count+len(d['rows']))]
                if [r.get('index') for r in d['rows']]!=expected:
                    raise ValueError('a matrix sweep prefix has a gap or reorder')
                self.rows.extend(d['rows']);count+=len(d['rows'])
                target=self.root/name;target.parent.mkdir(parents=True,exist_ok=True)
                if p.resolve()!=target.resolve():shutil.copyfile(p,target)
                self.entries.append(dict(receipt))
            if count!=previous.get('completed_rows') or count>5970:
                raise ValueError('the original complete row count disagrees with its chunks')
            if self.rows and len(self.rows)%CHUNK:
                self.pending=self.rows[-(len(self.rows)%CHUNK):]
        self.document['row_chunks']=self.entries
        self.document['completed_rows']=len(self.rows)

    def append(self,row):
        with (self.root/'checkpoint.lock').open('a') as checkpoint:
            fcntl.flock(checkpoint.fileno(),fcntl.LOCK_EX)
            expected=len(self.rows) if self.phase=='backward' else 5969-len(self.rows)
            if not row.get('complete') or row['index']!=expected:
                raise ValueError('the next mathematically complete matrix row is out of order')
            first=(len(self.rows)//CHUNK)*CHUNK
            if len(self.rows)%CHUNK==0:self.pending=[]
            self.pending.append(row);self.rows.append(row)
            # An unfinished chunk gets a new name at each committed row. The
            # previous header therefore never points at overwritten chunk bytes.
            previous_name=(self.entries[first//CHUNK]['file'] if len(self.entries)>first//CHUNK else None)
            name=f'{self.phase}-complete-rows-{first:05d}-{len(self.pending):02d}.json.gz'
            d=dict(kind=KIND,phase=self.phase,source_sha256=sha(__file__),first_row=first,rows=self.pending)
            path=self.root/name;save(path,d)
            receipt=dict(file=name,sha256=sha(path),bytes=path.stat().st_size,
                first_row=first,rows=len(self.pending),last_index=row['index'])
            if len(self.entries)>first//CHUNK:self.entries[first//CHUNK]=receipt
            else:self.entries.append(receipt)
            self.document.update(row_chunks=self.entries,completed_rows=len(self.rows),
                actual_progress=dict(phase=self.phase,complete_rows=len(self.rows),total=5970,
                    last_complete_index=row['index']))
            save(self.path,self.document)
            if previous_name and previous_name!=name:
                old=self.root/previous_name
                if old.exists():old.unlink()  # only this job's copied temporary partial chunk

    @staticmethod
    def complete(path,phase):
        header=read(path)
        if (header.get('kind')!=KIND or header.get('phase')!=phase or not header.get('complete')
            or header.get('failure') or header.get('source_sha256')!=sha(__file__)
            or header.get('completed_rows')!=5970
            or not header.get('gates') or not all(g['passed'] for g in header['gates'])):
            raise ValueError('one exact complete directional sweep is required')
        dummy={}
        loaded=ChunkRows(dummy,path.parent/'unused-reader-header.json.gz',phase,header,path.parent)
        return header,loaded.rows


def own_origin(phase):
    return dict(repository='Rogerhu12/math-research-public',
        run_id=os.environ.get('GITHUB_RUN_ID','unknown'),run_attempt=os.environ.get('GITHUB_RUN_ATTEMPT','unknown'),
        artifact='visible-exact-directional-matrix-Green-'+phase+'-'
            +os.environ.get('GITHUB_RUN_ID','unknown')+'-'+os.environ.get('GITHUB_RUN_ATTEMPT','unknown'),
        folder='matrices')


def previous_prefix(a,doc):
    if not a.resume:return None
    d=read(a.resume)
    if (d.get('kind')!=KIND or d.get('source_sha256')!=sha(__file__) or d.get('phase')!=a.phase
        or d.get('input_sha256')!=doc['input_sha256']
        or d.get('backward_native_sha256')!=doc.get('backward_native_sha256')):
        raise ValueError('a directional sweep prefix has a different exact mathematical identity')
    doc['original_prefix_native_sha256']=sha(a.resume)
    doc['original_prefix_failure_preserved']=d.get('failure')
    return d


def posterior_constants(green,events,kernel,impulse,boundary,doc):
    # These are the actual original L2 source norm and full boundary
    # columns, not the norm of a unit pointwise forcing.
    gains={w:dict(body=up(kernel['complete_ordinary_L2_source_to_L2_bounds'][w]),
        left=up(green['complete_source_component_L2_bounds'][w]['left_boundary_unit_norm']),
        right=up(green['complete_source_component_L2_bounds'][w]['right_boundary_unit_norm'])) for w in WINDOWS}
    rho=Fraction(boundary['exact_cut_rho'])
    physical=q(max(Fraction(1),1/rho))
    DL=up(boundary['right']['weighted_true_right_feedback_DL'])
    LR=up(boundary['right']['weighted_true_right_source_lifting_LR'])
    last=kernel['forward_kernel_event_rows'][-1]
    if last.get('kind')!='continuous' or Fraction(last['interval'][1])!=RIGHT:
        raise ValueError('the original L2 kernel has no true final cut node')
    kg=last['right_node_two_row_Gram']
    body_cut=(physical*sqrt_upper(up(kg['pp'])+up(kg['qq']))).upper()
    lastp=green['complete_forward_source_component_profiles'][-1]
    if Fraction(lastp['interval'][1])!=RIGHT:
        raise ValueError('the actual original boundary profiles do not reach the cut')
    bp={}
    for name,short in (('left_boundary_unit_norm','left'),('right_boundary_unit_norm','right')):
        p=up(lastp['channels'][name]['right_weighted_p'])
        qcut=DL*p+(LR if short=='right' else arb(0))
        bp[short]=(physical*sqrt_upper(p*p+qcut*qcut)).upper()
    gains['true_cut_trace']=dict(body=body_cut,**bp)
    allimp={Fraction(x['radius']):x for x in impulse['interface_impulse_rows']}
    if len(allimp)!=5970:raise ValueError('the complete impulse map has a repeated radius')
    # Events are stored from the true cut backwards. At each interface
    # product contains ALL events strictly outside that interface.
    # unit_weighted_jump_p_after already includes the interface's own b.
    multiplier=arb(1);jumps={};cutfactor=(physical*sqrt_upper(1+DL*DL)).upper()
    for event in events:
        if event['kind']=='interface':
            radius=Fraction(event['radius'])
            if radius not in allimp:raise ValueError('one real interface has no original gain')
            original=allimp[radius]
            if original['original_event_sha256']!=canonical(event):
                raise ValueError('one true interface impulse belongs to a different event')
            jumps[radius]={w:up(original['ordinary_L2_output_bound'][w]) for w in WINDOWS}
            jumps[radius]['true_cut_trace']=(cutfactor*multiplier
                *up(original['unit_weighted_jump_p_after'])).upper()
        multiplier=(multiplier*old.port(event)['p_from_p']).upper()
    if len(jumps)!=5970 or RIGHT in jumps:
        raise ValueError('the true cut is not an extra projector interface')
    doc['posterior_complete_true_Green_constants']={
        w:{k:record(v) for k,v in row.items()} for w,row in gains.items()}
    doc['new_cut_jump_trace_proof']=dict(
        exact_formula='metric_cut*sqrt(1+DL^2)*product(b strictly outside interface)*original_unit_p_after',
        interface_own_b_included_exactly_once_in_original_unit_p_after=True,
        true_zero_right_source_for_each_individual_jump=True,
        original_L2_kernel_final_node_used_for_ordinary_source_trace=True,
        body_L2_norm_not_substituted_for_a_trace=True,new_exponentials_or_old_port_calls=0)
    return gains,jumps


def exact_nominal_boundary(cut,rho):
    def hx(x):return q(Fraction(float.fromhex(x)))
    J=arb_mat([[hx(x) for x in row['complete_even_binary64_proposal_hex']] for row in cut['rows']])
    M=[hx(x) for x in cut['independent_mean_row']['binary64_proposal_hex']]
    if (J.nrows(),J.ncols(),len(M))!=(P,Q,Q):
        raise ValueError('all96 odd rows and the independent mean row are required')
    return arb_mat([[arb(int(i==j)) for j in range(P)]+[J[i,j]/q(rho) for j in range(Q)] for i in range(P)]
        +[[arb(0) for _ in range(P)]+[x/q(rho) for x in M]])


def right_defect(W,cut_frame,B,even_fee,rho):
    Qcut=block(cut_frame,0,N,0,P);BQ=B*Qcut;Qeven=block(Qcut,P,N,0,P)
    nominal=sqrt_upper(dot_trace(sym(transpose(BQ)*BQ),W))
    even=sqrt_upper(dot_trace(sym(transpose(Qeven)*Qeven),W))
    fee=(even_fee*even).upper()
    physical=block(Qcut,0,P,0,P)
    fullmetric=sym(transpose(physical)*physical+transpose(Qeven)*Qeven*q(1/rho**2))
    exact_cut=sqrt_upper(dot_trace(fullmetric,W))
    return (nominal+fee).upper(),exact_cut,dict(
        nominal_complete97_boundary_HS=record(nominal),
        true_error_on_complete_even97_input_HS=record(fee),
        true_boundary_error_only_even_columns=True,
        complete_even_input_kernel_HS=record(even),
        independent_mean_row_present=True)


def backward(a,doc,profile,rows,files):
    previous=previous_prefix(a,doc)
    chunks=ChunkRows(doc,a.out,'backward',previous,a.resume.parent if a.resume else None)
    qnext={ch:zero(Q,Q) for ch in CHANNELS}
    if chunks.rows:
        last=chunks.rows[-1]
        if last['original_matrix_row_sha256']!=canonical(rows[last['index']]):
            raise ValueError('the resumed backward row has a different original matrix')
        ar=files.load_receipt(last['array_receipt'])
        qnext={ch:read_covariance(ar,last['future_covariances'][ch]) for ch in CHANNELS}
    old_count=len(chunks.rows);began=time.monotonic();origin=own_origin('backward')
    for i in range(old_count,5970):
        start=time.monotonic();A,B,Di,Snext,coordinate=files.effective_port(i)
        arrays={};certs={};result={}
        for ch in CHANNELS:
            H=files.gram(i,'source',ch);Hqq=block(H,P,N,P,N)
            candidate=sym(Di*qnext[ch]*transpose(Di)+Hqq)
            result[ch],certs[ch]=covariance_bound(candidate,'Q_'+ch,arrays)
        ar=base.prior.array_receipt(a.arrays/f'future-covariance-{i:05d}.npz',arrays,origin)
        r=dict(complete=True,index=i,interval=rows[i]['interval'],
            original_matrix_row_sha256=canonical(rows[i]),effective_coordinate_event=coordinate,
            future_covariances=certs,array_receipt=ar,
            next_trace_coordinates='next original left full frame; true cut frame for cell0',
            all97_future_coordinates_and_even_mean_preserved=True,
            local_and_strict_future_input_supports_disjoint=True,seconds=time.monotonic()-start)
        qnext=result;chunks.append(r)
        if (i+1)%16==0:print(json.dumps(dict(phase='backward',complete_rows=i+1,
            seconds=time.monotonic()-began,last=i)),flush=True)
    gate(doc,'all5970_backward_covariances_keep_complete_future_mean_and128_input_directions',len(chunks.rows)==5970)
    gate(doc,'all_shared_Q_and_R_coordinate_events_bound_to_true_inverse_and_saved_arrays',True)
    gate(doc,'reference_and_complete_error_channels_kept_separate_until_operator_triangle',True)
    doc.update(complete=True,reused_complete_rows=old_count,new_covariance_rows=5970-old_count,
        no_original_F_C_Gram_target_validator_or_positive_port_recomputation=True,
        complete_directional_two_boundary_bound_proved=False,
        complete_infinite_BVP_inverse_proved=False,true_parameter_Schur_proved=False)
    save(a.out,doc)


def initial_forward_state(a,doc,previous,files,profile,rows,backrows):
    if previous and previous.get('initial_waist_state'):
        saved=previous['initial_waist_state'];arrays=files.load_receipt(saved['array_receipt'])
        hi,lo=arrays['V_initial_hi'],arrays['V_initial_lo']
        if hi.shape!=(P,Q) or lo.shape!=(P,Q):
            raise ValueError('the original chosen waist graph has wrong dimensions')
        V=exact(hi)+exact(lo)
        doc['initial_waist_state']=saved
        return V,{ch:up(saved['true_left_boundary_defect_HS'][ch]) for ch in CHANNELS}
    values=files.frame_values(5969,'left');S=exact(values)
    UQ=block(S,0,P,0,P);UN=block(S,0,P,P,N)
    inverse,inverse_fee=checked_inverse(UQ,'all96 true waist odd restrictions')
    target=-inverse*UN
    hi,lo,V,rounding=selected_twice(target)
    arrays={'V_initial_hi':hi,'V_initial_lo':lo}
    receipt=base.prior.array_receipt(a.arrays/'initial-exact-dyadic-waist-graph.npz',arrays,own_origin('forward'))
    residual=UQ*V+UN;normal=sym(transpose(residual)*residual)
    back=backrows[-1];qarrays=files.load_receipt(back['array_receipt'])
    defects={}
    for ch in CHANNELS:
        Qleft=read_covariance(qarrays,back['future_covariances'][ch])
        defects[ch]=sqrt_upper(dot_trace(normal,Qleft))
    doc['initial_waist_state']=dict(array_receipt=receipt,
        exact_original_waist_full_frame_array_sha256=base.raw_sha(values),
        true_waist_inverse_identity=inverse_fee,
        chosen_two_dyadic_graph_difference_upper=record(rounding),
        true_left_boundary_defect_HS={ch:record(v) for ch,v in defects.items()},
        independent_mean_remains_in_all97_future_coordinates=True,
        exact_definition='V0=exact(Vhi)+exact(Vlo); true defect UQ*V0+UN retained',
        chosen_midpoint_is_not_an_exact_waist_kernel_claim=True)
    save(a.out,doc)
    return V,defects


def forward(a,doc,profile,rows,files,green,events,kernel,impulse,boundary,cut):
    backdoc,backrows=ChunkRows.complete(a.backward,'backward')
    if backdoc.get('input_sha256')!=doc['input_sha256']:
        raise ValueError('the complete backward covariance has another exact matrix or Green input')
    for i,r in enumerate(backrows):
        if r['index']!=i or r['original_matrix_row_sha256']!=canonical(rows[i]):
            raise ValueError('the complete backward covariance row lost its exact original matrix identity')
    doc['backward_native_sha256']=sha(a.backward)
    previous=previous_prefix(a,doc)
    chunks=ChunkRows(doc,a.out,'forward',previous,a.resume.parent if a.resume else None)
    V,leftdef=initial_forward_state(a,doc,previous,files,profile,rows,backrows)
    W={ch:zero(P,P) for ch in CHANNELS}
    squared={ch:{w:arb(0) for w in WINDOWS} for ch in CHANNELS}
    body_squared={ch:arb(0) for ch in CHANNELS}
    jump_sums={ch:{w:arb(0) for w in (*WINDOWS,'true_cut_trace')} for ch in CHANNELS}
    gains,jumpgains=posterior_constants(green,events,kernel,impulse,boundary,doc)
    if chunks.rows:
        last=chunks.rows[-1];ar=files.load_receipt(last['array_receipt'])
        V=exact(ar['V_next_hi'])+exact(ar['V_next_lo'])
        W={ch:read_covariance(ar,last['past_covariances_after'][ch]) for ch in CHANNELS}
        squared={ch:{w:up(last['cumulative_proposal_L2_squares'][ch][w]) for w in WINDOWS} for ch in CHANNELS}
        body_squared={ch:up(last['cumulative_ordinary_body_defect_HS_squares'][ch]) for ch in CHANNELS}
        jump_sums={ch:{w:up(last['cumulative_true_jump_response_HS'][ch][w])
            for w in (*WINDOWS,'true_cut_trace')} for ch in CHANNELS}
    old_count=len(chunks.rows);began=time.monotonic();origin=own_origin('forward')
    for order in range(old_count,5970):
        i=5969-order;started=time.monotonic();row=rows[i]
        A,B,Di,Snext,coordinate=files.effective_port(i)
        candidate_next=(A*V+B)*Di
        hi,lo,Vnext,Verror=selected_twice(candidate_next)
        delta=Vnext-candidate_next
        qanchor=block(Snext,0,N,0,P)
        jump_factor=sym(transpose(delta)*transpose(qanchor)*qanchor*delta)
        saved={'V_next_hi':hi,'V_next_lo':lo};certs={};newW={};localstats={}
        current=backrows[i];current_arrays=files.load_receipt(current['array_receipt'])
        Qleft={ch:read_covariance(current_arrays,current['future_covariances'][ch]) for ch in CHANNELS}
        if i:
            nextrow=backrows[i-1];nextarrays=files.load_receipt(nextrow['array_receipt'])
            Qnext={ch:read_covariance(nextarrays,nextrow['future_covariances'][ch]) for ch in CHANNELS}
        else:Qnext={ch:zero(Q,Q) for ch in CHANNELS}
        left,right=map(Fraction,row['interval'])
        w=profile['rows'][i]['exact_weight']
        rhomin=min(Fraction(w['exact_rho_left']),Fraction(w['exact_rho_right']))
        metric=q(max(Fraction(1),1/rhomin))
        deltaA=up(row['patch']['true_complete_generator_difference_upper'])
        # The J matrices already contain true dr exactly once.
        # The two source channels have the same V, frames and output J.
        factors={}
        for name in ('full_weighted','full_physical','negative_physical'):
            if name=='negative_physical' and left>=PHASE_RIGHT:
                factors[name]=None;continue
            J=files.gram(i,name);Jpp=block(J,0,P,0,P);Jpq=block(J,0,P,P,N);Jqq=block(J,P,N,P,N)
            Jeff=sym(transpose(V)*Jpp*V+transpose(V)*Jpq+transpose(Jpq)*V+Jqq)
            factors[name]=(Jpp,Jeff)
        for ch in CHANNELS:
            H=files.gram(i,'source',ch)
            _,_,_,Hw=source_blocks(H,V)
            past_plus=sym(W[ch]+Hw)
            values={}
            for name,factor in factors.items():
                values[name]=(nonnegative(dot_trace(factor[0],past_plus)+dot_trace(factor[1],Qleft[ch]))
                    if factor is not None else arb(0))
            squared[ch]['whole_inner_body']=(squared[ch]['whole_inner_body']+values['full_physical']).upper()
            squared[ch]['fixed_complete_negative_phase_window']=(
                squared[ch]['fixed_complete_negative_phase_window']+values['negative_physical']).upper()
            defect=(deltaA*deltaA*metric*metric*values['full_weighted']).upper()
            body_squared[ch]=(body_squared[ch]+defect).upper()
            if i:
                jump=sqrt_upper(dot_trace(jump_factor,Qnext[ch]))
                if right not in jumpgains:raise ValueError('one true V-rounding jump has no original interface impulse')
                for window in (*WINDOWS,'true_cut_trace'):
                    jump_sums[ch][window]=(jump_sums[ch][window]+jumpgains[right][window]*jump).upper()
            else:
                # q at the true cut is exactly zero in this proposal,
                # hence changing V there creates no physical jump.
                jump=arb(0)
            newW[ch],certs[ch]=covariance_bound(A*past_plus*transpose(A),'W_'+ch,saved)
            localstats[ch]=dict(whole_physical_output_HS_square=record(values['full_physical']),
                negative_physical_output_HS_square=record(values['negative_physical']),
                complete_weighted_output_HS_square=record(values['full_weighted']),
                complete_ordinary_body_defect_HS_square=record(defect),
                actual_weighted_state_rounding_jump_HS=record(jump),
                complete_same_cell_signed_pq_source_covariance_retained=True)
        ar=base.prior.array_receipt(a.arrays/f'past-covariance-and-chosen-graph-{i:05d}.npz',saved,origin)
        result=dict(complete=True,index=i,interval=row['interval'],
            original_matrix_row_sha256=canonical(row),
            original_backward_row_sha256=canonical(current),
            effective_coordinate_event=coordinate,
            actual_exact_two_dyadic_V_difference_upper=record(Verror),
            exact_V_definition='exact(V_next_hi)+exact(V_next_lo); never binary64 hi+lo',
            actual_jump_definition='Qnext*(Vnext-(A*V+B_effective)*D_effective_inverse)*qnext',
            no_new_true_cut_jump_due_to_exact_zero_qcut=(i==0),
            past_covariances_after=certs,array_receipt=ar,
            local_complete_source_and_defect_bounds=localstats,
            cumulative_proposal_L2_squares={ch:{w:record(v) for w,v in x.items()} for ch,x in squared.items()},
            cumulative_ordinary_body_defect_HS_squares={ch:record(v) for ch,v in body_squared.items()},
            cumulative_true_jump_response_HS={ch:{w:record(v) for w,v in x.items()} for ch,x in jump_sums.items()},
            full_partial_H_dominating_bounds_not_declared_independent_same_source=True,
            independent_even_mean_and_all193_output_rows_retained=True,
            seconds=time.monotonic()-started)
        V,W=Vnext,newW
        chunks.append(result)
        if (order+1)%16==0:print(json.dumps(dict(phase='forward',complete_rows=order+1,
            last=i,seconds=time.monotonic()-began)),flush=True)
    gate(doc,'all5970_forward_signed_covariance_rows_and_all128_source_directions',len(chunks.rows)==5970)
    cut_values=files.frame_values(0,'right');S=exact(cut_values)
    rho=Fraction(boundary['exact_cut_rho'])
    B=exact_nominal_boundary(cut,rho)
    E=up(boundary['right']['weighted_true_low_97_row_matrix_error'])
    components={};totals={w:arb(0) for w in (*WINDOWS,'true_cut_trace')}
    final_arrays={}
    for ch in CHANNELS:
        # W here is the complete true cut p-coordinate covariance bound.
        # Save it so later consumers can keep all96 directions.
        _,wreceipt=covariance_bound(W[ch],'cut_W_'+ch,final_arrays)
        rdef,proposal_cut,rproof=right_defect(W[ch],S,B,E,rho)
        body=sqrt_upper(body_squared[ch])
        proposal={w:sqrt_upper(squared[ch][w]) for w in WINDOWS};proposal['true_cut_trace']=proposal_cut
        out={}
        for window in (*WINDOWS,'true_cut_trace'):
            terms=dict(proposal=proposal[window],body=(gains[window]['body']*body).upper(),
                left=(gains[window]['left']*leftdef[ch]).upper(),
                right=(gains[window]['right']*rdef).upper(),
                all_actual_rounding_jumps=jump_sums[ch][window])
            value=sum(terms.values(),arb(0)).upper()
            out[window]=dict(complete_HS_upper=record(value),
                individually_paid_components={k:record(v) for k,v in terms.items()})
            totals[window]=(totals[window]+value).upper()
        components[ch]=dict(ordinary_body_defect_HS=record(body),
            true_left96_boundary_defect_HS=record(leftdef[ch]),
            true_right97_boundary_defect_HS=record(rdef),
            true_right_boundary_details=rproof,
            complete_proposal_cut_covariance=wreceipt,
            complete_posterior_bounds=out)
    final_receipt=base.prior.array_receipt(a.arrays/'complete-cut-two-channel-covariances.npz',final_arrays,origin)
    gate(doc,'true96_waist_and_true97_regular_boundary_defects_paid_including_independent_mean',True)
    gate(doc,'all_piecewise_operator_defects_paid_in_ordinary_L2_on_the_entire_inner_body',True)
    gate(doc,'all_independent_V_rounding_jumps_paid_with_individual_actual_Green_gains',True)
    gate(doc,'complete_source_error_and_reference_responses_combined_only_by_operator_triangle',True)
    gate(doc,'true_cut_trace_uses_actual_point_kernel_boundary_columns_and_jump_ports',True)
    gate(doc,'complete_directional_bounds_are_finite_and_keep_high_cap_inputs_separate',
        all(x.is_finite() and x>=0 for x in totals.values()))
    doc.update(complete=True,reused_complete_rows=old_count,new_forward_covariance_rows=5970-old_count,
        complete_directional_posterior_components=components,
        complete_true_finite193_body_high_to_low_bounds={w:record(v) for w,v in totals.items()},
        complete_proposal_cut_covariance_array_receipt=final_receipt,
        exact_inner_interval=['0','9/10'],fixed_negative_norm_interval=['0',str(PHASE_RIGHT)],
        input='ordinary L2_r of complete high h; only modes97..160 enter the fixed M32 body cross block',
        all_full193_output_and_independent_even_mean_retained=True,
        exact_source_coefficient_basis='normalized angular circle and orthonormal reflected odd/even amplitudes',
        original_Q_R_frames_F_C_Grams_targets_validators_and_scalar_ports_recomputed=0,
        new_same_Q_R_coordinate_inverse_arithmetic_and_two_matrix_sweeps=True,
        complete_finite193_directional_two_boundary_bound_proved=True,
        full_cap_infinite_high_trace_input_still_independent=True,
        negative_high_BVP_inverse_and_full_low_high_Schur_still_required=True,
        nonzero_delta_and_changed_nonlinear_background_transfer_still_required=True,
        true_infinite_parameter_response_error_proved=False,
        complete_infinite_BVP_inverse_proved=False,true_parameter_Schur_proved=False)
    save(a.out,doc)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--phase',choices=('backward','forward'),required=True)
    for name in ('matrix-data','matrix-process','profile','profile-process','green','green-process','kernel',
        'kernel-process','impulse','impulse-process','reviewed-impulse-process','boundary','nominal-cut',
        'array-root','arrays','out'):
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--matrix-run',required=True)
    p.add_argument('--backward',type=Path)
    p.add_argument('--resume',type=Path)
    a=p.parse_args()
    if a.phase=='forward' and a.backward is None:raise ValueError('the completed true backward covariance sweep is required')
    if a.out.exists():raise FileExistsError('preserve every actual complete or partial matrix Green header')
    ctx.prec=320;ctx.cap=6;started=time.monotonic()
    doc=dict(kind=KIND,phase=a.phase,source_sha256=sha(__file__),complete=False,failure=None,gates=[],
        input_sha256=input_identity(a),arithmetic_bits=320,completed_rows=0,row_chunks=[],
        complete_infinite_BVP_inverse_proved=False,true_parameter_Schur_proved=False)
    if a.phase=='forward':doc['backward_native_sha256']=sha(a.backward)
    try:
        profile,rows,green,events,kernel,impulse,boundary,cut=inputs(a,doc)
        files=MatrixFiles(a.array_root,profile,rows)
        if a.phase=='backward':backward(a,doc,profile,rows,files)
        else:forward(a,doc,profile,rows,files,green,events,kernel,impulse,boundary,cut)
    except BaseException as error:
        doc['failure']=dict(type=type(error).__name__,message=str(error));raise
    finally:
        doc['seconds']=time.monotonic()-started;save(a.out,doc)
    print(json.dumps(dict(phase=a.phase,complete=doc['complete'],completed_rows=doc['completed_rows'],
        seconds=doc['seconds'],bounds=doc.get('complete_true_finite193_body_high_to_low_bounds'),
        infinite_inverse=False)),flush=True)


if __name__=='__main__':main()
