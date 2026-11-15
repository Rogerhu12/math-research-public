#!/usr/bin/env python3
"""New complete97 physical adjoint trial from already certified scalar jets.

Only the selected finite proposal is computed here. No old target, quarter
residual, forward cap state, or mathematical high-to-low bound is rerun or
claimed. Exact nodal binary64 arrays define a fresh Hermite trial whose full
continuous adjoint residual and true boundaries are separate obligations.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,math,os,shutil,time
from bisect import bisect_right
from fractions import Fraction
from pathlib import Path
from types import SimpleNamespace
for _adjoint_thread_variable in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[_adjoint_thread_variable]='1'
import numpy as np
from numpy.lib.format import open_memmap
from scipy.linalg import lu_solve,solve_triangular
from flint import ctx
from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_codazzi_final_continuous_value_repair import iter_repair
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_codazzi_final_regular_head_trial import Budget,Pause,ResumableHeadQR,atomic_npy
from fourfold_codazzi_block_qr_collocation import apply_qt
from fourfold_codazzi_block_qr_persistent import array_digest,atomic_json,atomic_npz
from fourfold_codazzi_cap128_CI_worker import read,digest

PUBLIC='Rogerhu12/math-research-public'
KIND='actual_cached_scalar_complete97_physical_adjoint_Hermite_proposal_v2'
CURRENT='ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
REPAIR='440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47'
REPAIR_NATIVE='6ee8b07fe94a8d9f87865a9ebb6650266b7eca792d435136ba533be92b1959fc'
PLAN='406e3e5331720a3f87f2b5f53c2e7d2988bea25b7537d650157ed97278e3073a'
QUARTER='770106a925812df4fc380785ca3e715b2a30a649a355fb888e0dcbe0e6a65298'
QUARTER_SOURCE='222b9a3dbfe842fbf8823d79584174cab5a350652db8a35cded0a610c45f6793'
QUARTER_WORKER='cdaebcd03696c86249dc2cb0798a39fb4e4fabef92259af7ec3fcbe63c12a9e2'
QUARTER_MANIFEST='b141f6d9be92cb86fc06b49933bfb005eb0de383eef5dd8bd91a6c347d8b1263'
POINT='41156aa8ac5b124b2ccca96e2f52b210edf1a3f5c170fdf839e66bf0602725b8'
POINT_SOURCE='5845549dd474d744be2dae5ef3f0c608ea61eb7a2c97c6cedebd3b73d0b159e5'
POINT_WORKER='a934d2ad4afa6fae2d56f6a4202662792771618fc564699ff1fb67d601503398'
POINT_MANIFEST='a4ca896cc3eb2b0b3f02a7249aec49deabe3920ee9e50f0b59f984c4661f60f0'
QVECTOR='8f2471f709d5350212c3bb12a2e180fef37cbd8ced72e7ed858d6687b5fa36d9'
LEFT,RIGHT=Fraction(9,10),Fraction(25,8)
NAMES=('gamma','beta','K','s')
M,N,COLS,ANGLES=128,257,97,1024
RANGES=((0,256),(256,512),(512,768),(768,1024),(1024,1280),(1280,1536),(1536,1792),(1792,1977))


def canonical(d):
    return hashlib.sha256((json.dumps(d,sort_keys=True,separators=(',',':'))+'\n').encode()).hexdigest()


def save(path,d):
    raw=(json.dumps(d,ensure_ascii=False,indent=2)+'\n').encode()
    if Path(path).suffix=='.gz':raw=gzip.compress(raw,mtime=0)
    Path(path).parent.mkdir(parents=True,exist_ok=True)
    tmp=Path(str(path)+'.partial');tmp.write_bytes(raw);os.replace(tmp,path)


def gate(d,name,ok):
    d['gates'].append(dict(name=name,passed=bool(ok)))
    if not ok:raise ValueError(name)


def success(d):
    return bool(d.get('complete') and not d.get('failure') and d.get('gates')
        and all(g.get('passed') for g in d['gates']))


def actual(p,run,worker,manifest,native,label=None):
    children=[c for c in p.get('children',[]) if c.get('actual_returncode')==0
        and (label is None or c.get('label')==label)]
    return bool(p.get('repository')==PUBLIC and str(p.get('run_id'))==str(run)
        and p.get('worker_source_sha256')==worker and p.get('input_manifest_sha256')==manifest
        and children and any(x.get('sha256')==native for x in p.get('native_files',[])))


def load_inputs(a,doc):
    bundle=read(a.input_index)
    if bundle.get('repository')!=PUBLIC or bundle.get('kind')!='cached_adjoint_trial_original_inputs_v1':
        raise ValueError('the exact public original-input index is required')
    paths={key:Path(value['path']) for key,value in bundle['files'].items()}
    identities={key:digest(path) for key,path in paths.items()}
    if any(identities[key]!=bundle['files'][key]['sha256'] for key in paths):
        raise ValueError('an original input changed after it was indexed')
    doc['input_sha256']=identities;doc['actual_input_index_sha256']=digest(a.input_index)
    if (identities['candidate']!=CURRENT or identities['repair']!=REPAIR_NATIVE
        or identities['q-vector']!=QVECTOR or identities['quarter-plan']!=PLAN
        or identities['quarter']!=QUARTER or identities['native-points']!=POINT):
        raise ValueError('an exact original scientific input identity changed')
    plan,quarter,point=[read(paths[k]) for k in ('quarter-plan','quarter','native-points')]
    pp,qp,mp=[read(paths[k]) for k in ('quarter-plan-process','quarter-process','native-points-process')]
    gate(doc,'actual_complete7908_quarters_and64_original_native_points_are_successful',
        success(plan) and success(quarter) and success(point)
        and quarter.get('source_sha256')==QUARTER_SOURCE
        and point.get('source_sha256')==POINT_SOURCE
        and actual(qp,43626024582,QUARTER_WORKER,QUARTER_MANIFEST,QUARTER,'actual_complete_quarter_cap_finish')
        and actual(mp,43635264409,POINT_WORKER,POINT_MANIFEST,POINT)
        and quarter.get('complete_quarter_domains')==7908
        and point.get('complete_new_native_point_domains')==64
        and point.get('original7908_whole_target_domains_recomputed')==0)
    if (str(pp.get('run_id'))!='43623547711'
        or pp.get('worker_source_sha256')!='04d4380d840504f3aedf2da2d95f2112677819885f4a1e367480f97298b332db'
        or pp.get('input_manifest_sha256')!='6dc5bf2d8030d506c74dc29ef2cb3c1991cd5f7fb8c2a051b03b0ad89cb2fb69'
        or not any(x.get('sha256')==PLAN for x in pp.get('native_files',[]))):
        raise ValueError('the exact original successful quarter plan process is required')
    table={tuple(r['request']):r for r in plan['reused_quarter_rows']}
    if len(table)!=64:raise ValueError('the original64 complete quarter cells are required')
    receipts={tuple(r['range']):r for r in quarter['range_receipts']}
    if set(receipts)!=set(RANGES):raise ValueError('all eight original completed ranges are required')
    for first,end in RANGES:
        key=f'range-{first}-{end}';path=paths[key];process=read(paths[key+'-process'])
        d=read(path);receipt=receipts[first,end]
        if (digest(path)!=receipt['native_sha256'] or digest(paths[key+'-process'])!=receipt['actual_original_process_sha256']
            or d.get('range')!=[first,end] or not success(d)
            or d.get('source_sha256')!=receipt['source_sha256']
            or str(process.get('run_id'))!=str(receipt['actual_workflow_run'])
            or process.get('worker_source_sha256')!=receipt['actual_worker_sha256']
            or process.get('input_manifest_sha256')!=receipt['actual_manifest_sha256']
            or not any(c.get('label')=='actual_complete_quarter_cap_range'
                and c.get('actual_returncode')==0 for c in process.get('children',[]))
            or not any(e.get('sha256')==digest(path) for e in process.get('native_files',[]))):
            raise ValueError('one original complete range lost its actual source/process receipt')
        for row in d['rows']:
            request=tuple(row['request'])
            if request in table:raise ValueError('an original quarter was included twice')
            table[request]=row
    expected=[(i,4,j) for i in range(1977) for j in range(4)]
    if sorted(table)!=expected:raise ValueError('the complete original quarter partition has a gap')
    decisions=quarter['complete_parent_representation_decisions']
    if len(decisions)!=1977:raise ValueError('the complete original parent identity table is required')
    for i,decision in enumerate(decisions):
        if [canonical(table[i,4,j]) for j in range(4)]!=decision['complete_quarter_row_sha256']:
            raise ValueError('one original certified quarter byte identity changed')
    native_points={tuple(row['request']):row for row in point['new_native_point_cells']}
    missing={key for key,row in table.items() if not row.get('intrinsic_midpoint_jets')}
    if len(native_points)!=64 or set(native_points)!=missing:
        raise ValueError('only the exact64 missing native midpoint enclosures may be supplied')
    rows=[]
    for key in expected:
        original=table[key];row=native_points.get(key,original)
        if key in native_points:
            receipt=row['native_point_receipt']
            if (receipt['original_quarter_row_sha256']!=canonical(original)
                or canonical(row['all_original_target_coefficients'])!=canonical(original['all_original_target_coefficients'])
                or not receipt.get('native_parameter_enclosure_contains_same_fixed_eta0')):
                raise ValueError('one native point changed its original whole scalar germ')
        left,right=map(Fraction,row['interval']);germ=tuple(map(Fraction,row['actual_scalar_germ']))
        if (row['request']!=list(key) or not germ[0]<=left<right<=germ[1]
            or not row.get('intrinsic_midpoint_jets')
            or any(name+suffix not in row['all_original_target_coefficients']
                or name+suffix not in row['intrinsic_midpoint_jets']
                for name in NAMES for suffix in ('','1','2','3'))):
            raise ValueError('one complete fixed-eta original scalar jet row is missing')
        if rows and rows[-1]['interval'][1]!=row['interval'][0]:
            raise ValueError('the full certified scalar cover has a gap')
        rows.append(row)
    gate(doc,'all7908_original_whole_jets_and_all7908_native_midpoints_reused_without_target_calls',
        Fraction(rows[0]['interval'][0])==LEFT and Fraction(rows[-1]['interval'][1])==RIGHT)
    doc.update(original_quarter_native_sha256=QUARTER,original_native_point_native_sha256=POINT,
        original_scalar_domain_count=7908,original_native_midpoints_count=7908,
        old_target_calls=0,old_forward_cap_state_or_residual_cells_recomputed=0,
        original_continuous_centre_definition_sha256=REPAIR,
        physical_parameter='fixed physical eta0, original nu, repaired M32 delta0')
    return paths,rows,plan


class CachedScalars:
    """A fresh floating proposal, selected only from original certified jets."""
    def __init__(self,rows,directory):
        self.rows=rows;self.left=[Fraction(r['interval'][0]) for r in rows]
        self.right=[Fraction(r['interval'][1]) for r in rows]
        path=directory/'selected-intrinsic-proposal.npz'
        identity=canonical([dict(request=r['request'],interval=r['interval'],
            germ=r['actual_scalar_germ'],whole_sha256=canonical(r['all_original_target_coefficients']),
            midpoint_sha256=canonical(r['intrinsic_midpoint_jets'])) for r in rows])
        report=directory/'selected-intrinsic-proposal.json'
        if path.exists() or report.exists():
            if not path.exists() or not report.exists():raise ValueError('a cached scalar selection is incomplete')
            receipt=read(report)
            if receipt.get('original7908_jet_identity')!=identity or receipt.get('sha256')!=digest(path):
                raise ValueError('one selected original scalar proposal changed')
            with np.load(path,allow_pickle=False) as z:
                self.coefficients=z['coefficients'].copy();self.centres=z['centres'].copy()
        else:
            self.coefficients=np.empty((7908,4,3))
            self.centres=np.asarray([float((l+r)/2) for l,r in zip(self.left,self.right)])
            for i,row in enumerate(rows):
                for j,name in enumerate(NAMES):
                    for k in range(3):
                        value=box_from_record(row['intrinsic_midpoint_jets'][name+('' if k==0 else str(k))])
                        self.coefficients[i,j,k]=float(value.mid())/math.factorial(k)
            atomic_npz(path,coefficients=self.coefficients,centres=self.centres)
            atomic_json(report,dict(original7908_jet_identity=identity,sha256=digest(path),
                exact_binary64_selection_only=True,no_new_target_evaluation=True,
                not_claimed_as_a_rigorous_value_or_derivative_enclosure=True))
        if self.coefficients.shape!=(7908,4,3) or self.centres.shape!=(7908,):
            raise ValueError('the original selected scalar proposal has the wrong complete shape')
        self.identity=identity;self.file=path;self.calls=0

    def at(self,radius):
        rr=Fraction.from_float(float(radius))
        # Only the first floating knot lies above exact9/10. No arbitrary
        # extrapolation or a different scalar germ is authorized.
        if rr<LEFT or rr>RIGHT:raise ValueError('outside the fixed physical cap')
        i=min(7907,max(0,bisect_right(self.left,rr)-1))
        if not self.left[i]<=rr<=self.right[i]:raise ValueError('one cached scalar evaluation escaped its complete cell')
        d=float(radius)-self.centres[i];c=self.coefficients[i]
        self.calls+=1
        return (c[:,2]*d+c[:,1])*d+c[:,0]


class CachedAdjointHead:
    def __init__(self,paths,rows,directory):
        self.m=M;self.n=N;self.columns=COLS;self.angles=ANGLES;self.mc=32
        self.saved=load_candidate(paths['candidate'])
        meta=json.loads(str(self.saved['metadata']))
        self.alpha=Fraction(meta['exact_float_amplitude']);self.nu=Fraction(meta['exact_float_nu'])
        self.coefficients=np.asarray(self.saved['piece_coefficients'])
        self.nodes=np.asarray(self.saved['radial_nodes'],dtype=float)
        if self.coefficients.shape!=(4,6144,65) or int(meta['modes'])!=32:
            raise ValueError('all exact original moving centre coefficients are required')
        repair=read(paths['repair'])
        if (not repair.get('complete') or repair.get('derived_definition_sha256')!=REPAIR
            or canonical(repair['definition'])!=REPAIR):
            raise ValueError('the exact original continuous centre repair definition is required')
        offsets=[];h=hashlib.sha256()
        for piece,offset,_ in iter_repair(self.saved,self.alpha):
            h.update((json.dumps(dict(piece=piece,physical_offset=list(map(str,offset))),
                sort_keys=True,separators=(',',':'))+'\n').encode())
            offsets.append(list(map(float,offset)))
        if h.hexdigest()!=repair['definition']['offset_sequence_sha256']:
            raise ValueError('the original full exact repair offsets changed')
        self.offsets=np.asarray(offsets);self.scalars=CachedScalars(rows,directory)
        self.theta=np.arange(ANGLES)*np.pi/(2*ANGLES);self.freq=4*np.arange(1,M+1)
        self.sines=np.sin(self.theta[:,None]*self.freq)
        self.cosines=np.column_stack((np.ones(ANGLES),np.cos(self.theta[:,None]*self.freq)))
        self.basis_b=np.column_stack((self.sines,np.zeros((ANGLES,M+1))))
        self.basis_c=np.column_stack((np.zeros((ANGLES,M)),self.cosines))
        self.basis_bp=np.column_stack((self.cosines[:,1:]*self.freq,np.zeros((ANGLES,M+1))))
        self.basis_cp=np.column_stack((np.zeros((ANGLES,M+1)),-self.sines*self.freq))
        self.q=np.asarray(read(paths['q-vector'])['q_values'][:M],dtype=float)
        if self.q.shape!=(M,) or not np.isfinite(self.q).all():raise ValueError('all128 original outer proposal rows required')
        self.max_angle_residual=0.;self.min_angle_jacobian=float('inf')
        self.identity=dict(candidate_sha256=CURRENT,repair_definition_sha256=REPAIR,
            original_scalar_selection_identity=self.scalars.identity,
            selected_intrinsic_array_sha256=digest(self.scalars.file),
            fixed_exact_alpha=str(self.alpha),fixed_exact_nu=str(self.nu),
            actual_scalar_targets_recomputed=0,physical_modes=M,physical_state_dimension=N,
            independent_adjoint_input_columns=COLS,physical_input_basis='sqrt2 sine j1..96 plus independent even mean',
            exact_reflection='odd physical B, even physical C including mean',
            selected_scalar_polynomial_degree=2,
            proposal_generator='minus formal physical adjoint; full residual Hessian is a separate exact defect',
            formal_coefficient_derivatives_not_numerically_differentiated=True,
            original_q_vector_sha256=QVECTOR,exact_true_left=str(LEFT),exact_true_right=str(RIGHT))

    def piece(self,r):return min(6143,max(0,int(np.searchsorted(self.nodes,float(r),side='right'))-1))

    def fields(self,radius,piece=None):
        r=float(radius);piece=self.piece(r) if piece is None else int(piece)
        t=r-self.nodes[piece];cube=self.coefficients[:,piece]
        value=((cube[0]*t+cube[1])*t+cube[2])*t+cube[3]
        odd=float(self.alpha)*value[:32]+self.offsets[piece,:32]
        even=float(self.alpha)*value[32:]+self.offsets[piece,32:]
        gamma,beta,K,s=map(float,self.scalars.at(r));mean=s+even[0];ell=K*s*s
        if not mean<0:raise ValueError('the original centre mean sign was lost')
        modes=4*np.arange(1,33);phi=self.theta.copy()
        for _ in range(24):
            phase=phi[:,None]*modes;sine,cosine=np.sin(phase),np.cos(phase)
            psi=sine@(even[1:]/modes)/mean;jacobian=1+cosine@even[1:]/mean
            if not np.all(jacobian>0):raise ValueError('a floating inverse angle is not monotone')
            difference=phi+psi-self.theta;phi-=difference/jacobian
            if np.max(abs(difference))<2e-15:break
        phase=phi[:,None]*modes;sine,cosine=np.sin(phase),np.cos(phase)
        psi=sine@(even[1:]/modes)/mean;jacobian=1+cosine@even[1:]/mean
        error=float(np.max(abs(phi+psi-self.theta)))
        if error>2e-13 or not np.isfinite(phi).all():raise ValueError('the new proposal inverse-angle solve failed')
        self.max_angle_residual=max(self.max_angle_residual,error)
        self.min_angle_jacobian=min(self.min_angle_jacobian,float(jacobian.min()))
        u=sine@odd;dv=even[0]+cosine@even[1:]
        return gamma,beta,ell,2*u,-u*u-K*(2*s*dv+dv*dv),mean,phi

    def project(self,b,c):
        if b.ndim==1:b=b[:,None];c=c[:,None]
        odd=(2/ANGLES)*self.sines.T@b
        even=(2/ANGLES)*self.cosines.T@c;even[0]*=.5
        return np.vstack((odd,even))

    def matrix(self,r,pieces=None):
        radii=np.atleast_1d(r);out=np.empty((N,N,len(radii)))
        for j,radius in enumerate(radii):
            piece=None if pieces is None else pieces[j]
            gamma,beta,ell,qb,qc,_,_=self.fields(radius,piece)
            B=2*beta*self.basis_b+gamma*qb[:,None]*self.basis_bp+gamma*self.basis_cp-beta*qb[:,None]*self.basis_c
            C=gamma*(qc-ell)[:,None]*self.basis_bp-beta*(qc-ell-1)[:,None]*self.basis_c
            out[:,:,j]=self.project(B,C)
        return out

    def action_at(self,r,values,piece):
        # Independently synthesize supplied columns before complete pointwise
        # products. This is a floating proposal check, not its full residual.
        z=np.asarray(values)
        if z.ndim==1:z=z[:,None]
        b=self.sines@z[:M];c=self.cosines@z[M:]
        bp=(self.cosines[:,1:]*self.freq)@z[:M]
        cp=(-self.sines*self.freq)@z[M+1:]
        gamma,beta,ell,qb,qc,_,_=self.fields(r,piece)
        return self.project(2*beta*b+gamma*qb[:,None]*bp+gamma*cp-beta*qb[:,None]*c,
            gamma*(qc-ell)[:,None]*bp-beta*(qc-ell-1)[:,None]*c)

    def boundary(self):
        left=np.zeros((N+1,N));right=np.zeros_like(left);parameter=np.zeros((N+1,1))
        left[:M,:M]=np.eye(M);left[M,M]=1
        right[M+1:N,:M]=-np.diag(self.q);right[M+1:N,M+1:]=np.eye(M)
        parameter[-1,0]=1
        _,_,_,_,_,mean,phi=self.fields(float(LEFT))
        targets=mean*np.sqrt(2)*np.sin(phi[:,None]*(4*np.arange(1,97)))
        d=(2/ANGLES)*self.sines.T@targets
        rhs=np.zeros((N+1,COLS));rhs[:M,:96]=d;rhs[M,96]=1
        return left,right,parameter,rhs

class AdjointCollocation:
    def __init__(self,model,rows,directory):
        self.model=model;self.n=N
        exact={LEFT,RIGHT}
        exact.update(Fraction(row['interval'][0]) for row in rows[::4])
        exact.update(Fraction(row['interval'][1]) for row in rows[3::4])
        original=[float(r) for r in model.nodes if LEFT<=Fraction.from_float(float(r))<=RIGHT]
        self.x=np.asarray(sorted(set(float(r) for r in exact)|set(original)),dtype=float)
        if (self.x[0]!=float(LEFT) or self.x[-1]!=float(RIGHT)
            or np.any(np.diff(self.x)<=0) or not set(original).issubset(set(self.x))):
            raise ValueError('the complete exact original joins must be retained in the new proposal grid')
        self.h=np.diff(self.x);self.nodes=len(self.x)
        # All original knots are exact members of this binary64 node set.
        # The left endpoint therefore determines the unique one-sided
        # candidate cubic. A rounded midpoint can equal the next knot.
        self.pieces=np.asarray([model.piece(a) for a in self.x[:-1]],dtype=int)
        bad=np.flatnonzero((self.x[:-1]<model.nodes[self.pieces])
            |(self.x[1:]>model.nodes[self.pieces+1]))
        if len(bad):
            i=int(bad[0]);piece=int(self.pieces[i])
            raise ValueError('an exact left-selected candidate interval failed original containment: '+str(dict(
                index=i,piece=piece,left=float(self.x[i]).hex(),right=float(self.x[i+1]).hex(),
                original_left=float(model.nodes[piece]).hex(),original_right=float(model.nodes[piece+1]).hex())))
        # A resumed public runner reuses the exact already selected boundary
        # arrays. It does not silently assume BLAS angle projection is
        # bit-identical on another runner.
        selected=directory/'selected-boundary-proposal.npz'
        receipt_path=directory/'selected-boundary-proposal.json'
        selection_identity=canonical(dict(model=model.identity,nodes=list(map(float,self.x))))
        if selected.exists() or receipt_path.exists():
            if not selected.exists() or not receipt_path.exists():
                raise ValueError('an original selected boundary proposal is incomplete')
            receipt=read(receipt_path)
            if receipt.get('selection_identity')!=selection_identity or receipt.get('sha256')!=digest(selected):
                raise ValueError('one exact selected boundary proposal changed')
            with np.load(selected,allow_pickle=False) as z:
                self.left=z['left'].copy();self.right=z['right'].copy()
                self.parameter=z['parameter'].copy();self.boundary_rhs=z['rhs'].copy()
        else:
            self.left,self.right,self.parameter,self.boundary_rhs=model.boundary()
            atomic_npz(selected,left=self.left,right=self.right,parameter=self.parameter,rhs=self.boundary_rhs)
            atomic_json(receipt_path,dict(selection_identity=selection_identity,sha256=digest(selected),
                selected_finite_boundary_only=True,all_continuous_boundary_defects_still_required=True))
        if (self.left.shape!=(258,257) or self.right.shape!=(258,257)
            or self.parameter.shape!=(258,1) or self.boundary_rhs.shape!=(258,97)):
            raise ValueError('the complete selected97 boundary arrays have wrong dimensions')
        self.grid_definition=dict(original_whole_quarter_partition_sha256=QUARTER,
            original_parent_endpoints_included=True,all_original_candidate_joins_included=True,
            binary64_duplicate_endpoints_merged=True,true_left=str(LEFT),true_right=str(RIGHT),
            first_Hermite_polynomial_extended_only_to_exact_true_left=True,
            one_sided_candidate_piece_selected_from_exact_left_node=True,
            original_complete_two_endpoint_containment_gate_unchanged=True,
            actual_native_points_or_whole_target_domains_recomputed=0)

    def blocks(self,begin,end):
        eye=np.eye(N)
        for i in range(begin,end):
            a,b=self.x[i:i+2];h=b-a
            values=self.model.matrix([a,a+h/2,b],[self.pieces[i]]*3)
            A0,Am,A1=[values[:,:,j] for j in range(3)]
            yield (-eye-h*(A0+2*Am)/6-h*h*(Am@A0)/12,
                   eye-h*(A1+2*Am)/6+h*h*(Am@A1)/12,np.zeros(N))


def matrix_solve(factor,problem,directory,budget):
    """Reuse one complete257-state QR for all97 independent adjoint loads."""
    n,p,nodes,columns=factor.n,factor.p,factor.nodes,problem.boundary_rhs.shape[1]
    if columns!=COLS:raise ValueError('all96 odd and the independent mean input are required')
    directory.mkdir(parents=True,exist_ok=True)
    checkpoint=directory/'progress.json';top_path=directory/'top.npy'
    state_path=directory/'state.npy';current_path=directory/'current.npy'
    rhs=problem.boundary_rhs;signature=array_digest(rhs,label=factor.fingerprint)
    if checkpoint.exists():
        doc=read(checkpoint)
        if doc['rhs_identity']!=signature:raise ValueError('the complete97 adjoint RHS changed')
        top=np.load(top_path,mmap_mode='r+',allow_pickle=False)
        current=np.load(current_path,allow_pickle=False) if doc['stage']=='forward' else None
    else:
        top=open_memmap(top_path,mode='w+',dtype=np.float64,shape=(nodes-1,n,columns))
        current=solve_triangular(factor.initial_r.T,rhs[factor.left_rows],lower=True,check_finite=False)
        doc=dict(rhs_identity=signature,stage='forward',next_index=0,complete_columns=columns,
            complete_independent_mean_input=True)
        atomic_npy(current_path,current);atomic_json(checkpoint,doc)
    if top.shape!=(nodes-1,n,columns):raise ValueError('a complete forward matrix array is missing')
    if doc['stage']=='forward':
        for i in range(int(doc['next_index']),nodes-1):
            packed,tau,_,_,norm_r,_=factor.read(i)
            result=apply_qt(packed,tau,np.vstack((current,np.zeros((n,columns)))))
            top[i]=result[:n]
            current=solve_triangular(norm_r.T,result[n:],lower=True,check_finite=False)
            budget.add(1)
            if (i+1)%factor.span==0 or i==nodes-2:
                top.flush();atomic_npy(current_path,current)
                doc.update(next_index=i+1);atomic_json(checkpoint,doc)
                if i!=nodes-2:budget.checkpoint()
        endpoint=lu_solve(factor.end_lu,np.vstack((current,
            factor.right_scale[:,None]*rhs[factor.right_rows])),check_finite=False)
        state=open_memmap(state_path,mode='w+',dtype=np.float64,shape=(nodes,n,columns))
        state[-1]=endpoint[:n];state.flush();atomic_npy(directory/'dummy.npy',endpoint[-1])
        doc.update(stage='backward',next_index=nodes-2);atomic_json(checkpoint,doc)
    else:state=np.load(state_path,mmap_mode='r+',allow_pickle=False)
    if state.shape!=(nodes,n,columns):raise ValueError('a complete backward matrix array is missing')
    dummy=np.load(directory/'dummy.npy',allow_pickle=False)
    if doc['stage']=='backward':
        for i in range(int(doc['next_index']),-1,-1):
            packed,_,right,param,_,_=factor.read(i)
            state[i]=solve_triangular(packed[:n],top[i]-right@state[i+1]
                -param[:,None]*dummy[None,:],lower=False,check_finite=False)
            budget.add(1)
            if i%factor.span==0:
                state.flush();doc.update(next_index=i-1);atomic_json(checkpoint,doc)
                if i:budget.checkpoint()
        state.flush();doc.update(stage='complete',next_index=-1);atomic_json(checkpoint,doc)
    if doc['stage']!='complete' or not np.isfinite(state).all():
        raise ValueError('the complete97 adjoint substitution is not complete and finite')
    return state,dummy


def check_and_hermite(problem,state,dummy,directory,budget):
    """Independent complete finite action; no continuous proof is claimed."""
    progress=directory/'independent-check.json';nodes=problem.nodes
    identity=array_digest(problem.x,problem.boundary_rhs,label='complete97 new physical adjoint')
    if progress.exists():
        report=read(progress)
        if report.get('identity')!=identity:raise ValueError('the independent complete check changed')
        left=np.load(directory/'derivative-left.npy',mmap_mode='r+',allow_pickle=False)
        right=np.load(directory/'derivative-right.npy',mmap_mode='r+',allow_pickle=False)
        if report.get('complete'):
            if not report.get('passed'):raise ValueError('the original finite diagnostic gate failed')
            return report
    else:
        left=open_memmap(directory/'derivative-left.npy',mode='w+',dtype=np.float64,shape=(nodes-1,N,COLS))
        right=open_memmap(directory/'derivative-right.npy',mode='w+',dtype=np.float64,shape=(nodes-1,N,COLS))
        report=dict(identity=identity,complete=False,next_index=0,squared_error=0.,maximum_error=0.,
            finite_backward_gate=5e-8,complete_state_dimension=N,complete_input_columns=COLS,
            source_is_physical_adjoint=True,complete_even_mean_retained=True,
            complete_continuous_residual_certified=False)
    for i in range(int(report['next_index']),nodes-1):
        a,b=problem.x[i:i+2];h=b-a;piece=problem.pieces[i]
        f0=problem.model.action_at(a,state[i],piece);f1=problem.model.action_at(b,state[i+1],piece)
        middle=(state[i]+state[i+1])/2-h*(f1-f0)/8
        fm=problem.model.action_at(a+h/2,middle,piece)
        residual=state[i+1]-state[i]-h*(f0+f1+4*fm)/6
        left[i]=f0;right[i]=f1
        report['squared_error']+=float(np.sum(residual*residual))
        report['maximum_error']=max(report['maximum_error'],float(np.max(abs(residual))))
        report['next_index']=i+1;budget.add(1)
        if (i+1)%16==0 or i==nodes-2:
            left.flush();right.flush();atomic_json(progress,report)
            if i!=nodes-2:budget.checkpoint()
    boundary=problem.left@state[0]+problem.right@state[-1]+problem.parameter*dummy[None,:]-problem.boundary_rhs
    total=report['squared_error']+float(np.sum(boundary*boundary))
    relative=float(np.sqrt(total/max(float(np.sum(problem.boundary_rhs**2)),1e-300)))
    report.update(complete=True,full_relative_residual=relative,
        maximum_boundary_error=float(np.max(abs(boundary))),
        passed=bool(np.isfinite(relative) and relative<report['finite_backward_gate']),
        shared_exact_dyadic_endpoint_Hermite_definition=True,
        original_forward_cap_columns_transposed_as_certificate=False)
    atomic_json(progress,report)
    if not report['passed']:raise ValueError('the complete finite97 adjoint backward gate failed')
    return report


def progress(directory):
    result={}
    for name in ('factor-prefix.json','factor.json','matrix-RHS/progress.json','matrix-RHS/independent-check.json'):
        path=directory/name
        if not path.exists():continue
        d=read(path)
        result[name]={k:d.get(k) for k in ('complete','stage','next_index','nodes','complete_columns',
            'full_relative_residual','passed','array_file','array_sha256') if k in d}
        if 'factor-prefix' in name:
            result[name]['complete_checkpoint_seed_count']=len(d.get('seeds',{}))
    return result


def dependency_sha256():
    names=('fourfold_codazzi_candidate_shards.py','fourfold_codazzi_final_continuous_value_repair.py',
        'fourfold_codazzi_rotational_cap_jacobi.py','fourfold_codazzi_final_regular_head_trial.py',
        'fourfold_codazzi_block_qr_collocation.py','fourfold_codazzi_block_qr_persistent.py')
    return {name:digest(Path(__file__).with_name(name)) for name in names}


def array_receipt(path,root):
    return dict(file=str(path.relative_to(root)),bytes=path.stat().st_size,sha256=digest(path),
        exact_binary64_data=True,storage='original public Actions artifact only')


def run(a,doc):
    paths,rows,plan=load_inputs(a,doc)
    a.state_dir.mkdir(parents=True,exist_ok=True)
    model=CachedAdjointHead(paths,rows,a.state_dir)
    problem=AdjointCollocation(model,rows,a.state_dir)
    gate(doc,'all257_states_and97_independent_boundary_inputs_retained_on_the_complete_cap',
        model.n==257 and problem.boundary_rhs.shape==(258,97)
        and np.count_nonzero(problem.left[:,M])==1
        and problem.right.shape==(258,257))
    identity=dict(model=model.identity,grid=problem.grid_definition,span=a.span,
        source_sha256=digest(__file__),dependency_sha256=dependency_sha256(),
        exact_input_sha256=doc['input_sha256'],
        complete_continuous_residual_and_outer_graph_Hessian_fees_still_required=True)
    case=array_digest(problem.x,problem.left,problem.right,problem.parameter,problem.boundary_rhs,
        label=json.dumps(identity,sort_keys=True,separators=(',',':')))
    directory=a.state_dir/case;directory.mkdir(parents=True,exist_ok=True)
    ip=directory/'identity.json'
    if ip.exists():
        if read(ip)!=identity:raise ValueError('the new complete adjoint proposal identity changed')
    else:atomic_json(ip,identity)
    if a.resume:
        previous=read(a.resume)
        if (previous.get('kind')!=KIND or previous.get('source_sha256')!=digest(__file__)
            or previous.get('input_sha256')!=doc['input_sha256'] or previous.get('case')!=case
            or previous.get('identity')!=identity):
            raise ValueError('only an exact original adjoint proposal prefix may resume')
        doc['original_resume_native_sha256']=digest(a.resume)
        doc['original_resume_failure_preserved']=previous.get('failure')
        doc['original_complete_prefix_status']=previous.get('actual_checkpoint_progress')
    doc.update(case=case,identity=identity,radial_nodes=problem.nodes,collocation_intervals=problem.nodes-1,
        selected_scalar_proposal_sha256=digest(model.scalars.file),new_target_evaluations=0,
        complete_continuous_adjoint_bound_proved=False,complete_full_cap_high_to_low_bound_proved=False,
        actual_checkpoint_progress=progress(directory),stage='new_complete_adjoint_QR')
    if not (directory/'nodes.npy').exists():atomic_npy(directory/'nodes.npy',problem.x)
    if not (directory/'boundary-data.npz').exists():
        atomic_npz(directory/'boundary-data.npz',left=problem.left,right=problem.right,
            parameter=problem.parameter,rhs=problem.boundary_rhs)
    # A bounded inner batch only yields at an exact atomic QR/substitution/check
    # checkpoint. The public worker keeps its separate10-minute real pull clock.
    while True:
        budget=Budget(a.batch_blocks)
        try:
            doc['stage']='new_complete_adjoint_QR';save(a.out,doc)
            factor=ResumableHeadQR(N,problem.nodes,problem.left,problem.right,problem.parameter,
                problem.blocks,[],directory=a.state_dir,fingerprint=case,span=a.span,budget=budget)
            doc['end_model_condition_2']=factor.end_condition
            doc['stage']='complete97_adjoint_matrix_substitutions';save(a.out,doc)
            state,dummy=matrix_solve(factor,problem,directory/'matrix-RHS',budget)
            doc['stage']='complete97_independent_action_and_Hermite';save(a.out,doc)
            check=check_and_hermite(problem,state,dummy,directory/'matrix-RHS',budget)
            doc['actual_finite_backward_check']=check
            doc['counted_new_blocks_in_this_child']+=budget.used
            break
        except Pause:
            doc['counted_new_blocks_in_this_child']+=budget.used
            doc['actual_checkpoint_progress']=progress(directory)
            doc['atomic_batches_completed']+=1
            doc['selected_scalar_evaluation_calls_in_this_child']=model.scalars.calls
            save(a.out,doc)
            print(json.dumps(dict(kind=KIND,stage=doc['stage'],batch=doc['atomic_batches_completed'],
                progress=doc['actual_checkpoint_progress'],old_target_evaluations=0)),flush=True)
    endpoint=directory/'physical-adjoint-endpoints.npz'
    if not endpoint.exists():
        atomic_npz(endpoint,left_state=np.asarray(state[0]),right_state=np.asarray(state[-1]),
            selected_inner_nonmean_C=np.asarray(state[0,M+1:]),nodes=problem.x,
            left_derivative=np.load(directory/'matrix-RHS/derivative-left.npy',mmap_mode='r',allow_pickle=False)[0],
            right_derivative=np.load(directory/'matrix-RHS/derivative-right.npy',mmap_mode='r',allow_pickle=False)[-1])
    gate(doc,'all97_complete_finite_actions_and_both_boundaries_pass_the_original5e8_gate',
        check['passed'] and check['complete_input_columns']==97 and check['complete_state_dimension']==257)
    files=[model.scalars.file,directory/'nodes.npy',directory/'boundary-data.npz',endpoint,
        directory/'matrix-RHS/state.npy',directory/'matrix-RHS/derivative-left.npy',
        directory/'matrix-RHS/derivative-right.npy']
    receipts=[array_receipt(path,a.state_dir) for path in files]
    gate(doc,'exact_shared_dyadic_Hermite_arrays_and_all_input_columns_are_saved',
        all(x['bytes']>0 for x in receipts) and state.shape==(problem.nodes,257,97))
    doc.update(complete=True,stage='complete_selected_adjoint_Hermite_proposal',
        actual_checkpoint_progress=progress(directory),proposal_array_receipts=receipts,
        all_original7908_scalar_domains_recomputed=0,all_original64_native_points_recomputed=0,
        original_forward_cap_columns_recomputed_or_transposed_as_certificate=False,
        selected_scalar_evaluation_calls_in_this_child=model.scalars.calls,
        maximum_floating_inverse_angle_residual=model.max_angle_residual,
        minimum_floating_inverse_angle_jacobian=(model.min_angle_jacobian
            if math.isfinite(model.min_angle_jacobian) else None),
        exact_input_Gram='97 Euclidean coordinates: normalized moving odd modes1..96 and independent mean',
        exact_physical_output_Gram='odd128 and nonmean even128 each1/2; independent even mean1',
        mathematical_certificate=False,complete_continuous_adjoint_bound_proved=False,
        complete_full_cap_high_to_low_bound_proved=False,complete_infinite_BVP_inverse_proved=False)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('input-index','state-dir','out'):p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--resume',type=Path);p.add_argument('--span',type=int,default=8)
    p.add_argument('--batch-blocks',type=int,default=256)
    a=p.parse_args();ctx.prec=256;ctx.cap=6;started=time.monotonic()
    if a.out.exists():raise FileExistsError('preserve every original adjoint outcome before a new child')
    if a.span!=8 or a.batch_blocks<8 or a.batch_blocks%8:
        raise ValueError('the frozen complete QR checkpoint span is8')
    doc=dict(kind=KIND,source_sha256=digest(__file__),repository=PUBLIC,
        complete=False,failure=None,gates=[],mathematical_certificate=False,
        atomic_batches_completed=0,counted_new_blocks_in_this_child=0,
        old_target_evaluations=0,complete_full_cap_high_to_low_bound_proved=False)
    try:run(a,doc)
    except Exception as error:
        doc['failure']=dict(type=type(error).__name__,message=str(error))
    finally:
        doc['seconds']=time.monotonic()-started;save(a.out,doc)
    print(json.dumps({k:doc.get(k) for k in ('kind','complete','stage','failure','gates','seconds')}),flush=True)
    if doc['failure']:raise RuntimeError(str(doc['failure']))


if __name__=='__main__':main()
