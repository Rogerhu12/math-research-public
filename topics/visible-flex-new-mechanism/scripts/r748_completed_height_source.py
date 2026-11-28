"""Restore immutable R738 material data once and retain all new reconstruction receipts."""
from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import numpy as np
import scipy
from r728_closed_spinor_continuation_20261128 import PaidBook
from r738_macro_spline_space import Layout,PhysicalFields,OLD,distinct,radial_breaks
from r738_negative_tail_and_macro_source import SIGNS,propagated_curve,THETA,stepp
from r738_real_macro_reference import Base
from r745_completed_source_and_paid_units import Donor
from r748_paid_material_height_projection import projected,QuinticHeight
from r748_nested_true_material_height import base_height


class Book(PaidBook):
    def __init__(self,req,opt,limit,elapsed,counts):
        self.hashlib,self.os,self.elapsed,self.counts=hashlib,os,elapsed,counts
        self.limit,self.reserve=limit,opt['reserve_seconds']
        self.root=Path(os.environ['RUNNER_TEMP'])/'r748-paid';self.root.mkdir(exist_ok=True)
        self.ledger_file=self.root/'ledger.json'
        semantic=dict(schema='r748-common-E-height-v1',sources={k:v for k,v in req['source_sha256'].items() if k.endswith('.py')},
                     geometry=opt,completed=req['completed_sources'],runtime=[np.__version__,scipy.__version__])
        fid=hashlib.sha256(json.dumps(semantic,sort_keys=True,separators=(',',':')).encode()).hexdigest()
        if self.ledger_file.exists():
            self.ledger=json.loads(self.ledger_file.read_bytes())
            if self.ledger['fingerprint']!=fid:raise ValueError('Paid whole-material height identity changed.')
            counts.update(self.ledger['counts'])
        else:self.ledger=dict(schema=semantic['schema'],fingerprint=fid,semantic=semantic,kept={},retired={},counts={},
                unit_max_seconds={},runs=[],cumulative_seconds=0.,latest_state=None,pending=None,context={})
        self.prior_seconds=self.ledger['cumulative_seconds']
        self.ledger['runs'].append(dict(id=os.environ['GITHUB_RUN_ID'],source=os.environ['GITHUB_SHA'],
                                   attempt=os.environ.get('GITHUB_RUN_ATTEMPT')))
        self.flush()


class BaseBook:
    def __init__(self,book,donor):self.b,self.d=book,donor
    def once(self,key,fn):
        if self.d.has(key):
            # A prior scientific row is only reused by its exact ledger binding; never re-evaluate it.
            return self.d.load(key)
        return self.b.once(key,'base_new_radii',fn)


def prepare(req,opt,book,counts):
    root=Path(os.environ['RUNNER_TEMP'])/'r745-sources';spec=req['completed_sources']['files']
    mandatory=('r738/ledger.json','r738/r734-original-final.json','r735-final.json','r738-final.json')
    for name in mandatory:
        f=root/name;bind=spec[name]
        if f.stat().st_size!=bind['bytes'] or book.digest(f)!=bind['sha256']:raise ValueError('Incorrect genuine completed member '+name)
    ledger,orig,thin,wide=[json.loads((root/k).read_bytes()) for k in mandatory]
    if book.digest(root/mandatory[-1])!='4a271c0f8df58456a66a71a59e003c5d887c07d54b8bb53290e7269625f3ff7e':
        raise ValueError('A different R738 natural terminal was supplied.')
    q=np.ascontiguousarray(wide['all_parameters'],dtype='<f8')
    if (wide['kind']!='terminal' or wide['accepted']!=14 or wide['actual_space']!=[32,6,2]
        or wide['fingerprint']!=ledger['fingerprint'] or len(q)!=1882 or
        hashlib.sha256(q.tobytes()).hexdigest()!='951ee71b25d7c710ece1d60b4a3e4881fd4203e5a41486212700edc70d862594'):
        raise ValueError('Wrong paid parameter, space, or source run.')
    donor=Donor(root/'r738',ledger)
    nb=BaseBook(book,donor);base=Base(64,nb,counts)
    center=np.array(wide['full_independent_cross']['both']['actual_center_for_all_sectors'])[[0,2]]
    ref_z=base.paid(np.array([.075]))['center'][0,0,2]
    def project_raw():
        costs=donor.load('complete_tail_source')
        native={(s,j):propagated_curve(orig,j,s,-1,2e-12,counts,donor) for s in SIGNS for j in (2,3)}
        old=Layout(32,6,2,PhysicalFields(Base(48,nb,counts),native,counts,1),costs['true_amplitude_scale'])
        r=distinct(np.r_[radial_breaks(32,2,True),.083,.085,.09,.105,.145,.15,.175,.205,.21,.212])
        r=r[(r>=OLD[-1])&(r<=OLD[1])];r=distinct(np.r_[OLD[-1],r,OLD[1]])
        def take(rr):
            fixed=base.paid(rr)['reference_E']
            counts['projected_genuine_R738_radii']+=len(rr)
            return projected(old,q,rr,129,opt['seed_K'],fixed)
        z=book.once('source_129_native_and_projection_at_knots','source',lambda:take(r))
        def lift(rr):
            v,d,dd=stepp((rr-.105)/.07)
            return np.stack((1-v,-d/.07,-dd/.07**2))
        z['cos']-=base_height(base,r,opt['seed_K'])
        z['cos'][:,:,0]-=lift(r)*(center[1]-ref_z)
        init=QuinticHeight(r,z['cos'],z['sin'],True)
        mid=(r[:-1]+r[1:])/2
        fresh=book.once('source_129_native_and_projection_at_held_out_midpoints','source',lambda:take(mid))
        interp=init.coefficient_jets(mid)[0]+base_height(base,mid,opt['seed_K'])
        interp[:,:,0]+=lift(mid)*(center[1]-ref_z)
        diagnostics=dict(original_final_sha256=spec[mandatory[-1]]['sha256'],original_q_sha256=hashlib.sha256(q.tobytes()).hexdigest(),
           original_DOP_midpoint_tolerance=2e-12,original_angular_samples=129,original_base_order=48,
           native_material_twojet_max_projection_errors=z['material_three_projection_error'],
           original_native_integrator_disagreements=z['material_three_native_source_error'],
           original_reflection_sine_coefficients=z['reflection_sin_absolute_by_order'],
           midpoint_held_out_Hermite_coefficient_errors=np.max(abs(fresh['cos']-interp),axis=(1,2)),
           midpoint_projection_max_errors=fresh['material_three_projection_error'],
           all_old_deep_guards=wide['full_independent_cross']['both']['omitted_native_entire_old_caps'],
           old_nonnegative_cell_DOP_recomputed=False,new_deep_ansatz=True,
           old_cumulative_scientific_seconds=wide['cumulative_seconds'],old_counts=wide['counts'],
           old_status=wide['kind'],old_all_stages=wide['stages'],old_parameter_count=len(q),
           old_R734_units=orig['paid_units'],old_R734_scientific_seconds=orig['current_elapsed_seconds'],
           old_R735_units=thin['total_new_units'],old_R735_seconds=thin['current_elapsed_seconds'],initial_pose_xz=center)
        return dict(r=r,cos=z['cos'],sin=z['sin'],diagnostics=diagnostics)
    pack=book.once('original_1882q_transfer_129_actual_phi','source',project_raw)
    return QuinticHeight(pack['r'],pack['cos'],pack['sin'],True),base,center,ref_z,pack['diagnostics']

