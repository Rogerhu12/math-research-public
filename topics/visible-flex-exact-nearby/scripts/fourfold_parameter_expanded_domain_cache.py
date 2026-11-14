#!/usr/bin/env python3
"""Identity-checked shared parameter bounds on an independently proved disk.

The point sampler is never changed.  Its primitive grid can differ from the
proof grid, because both enclose the same infinite affine target.  A cached
larger-disk proof is used only after exact object, root, germ, time, source,
parameter interval and dependency checks.  Ordinary crossing-cap fees are
still those of the original R3 models.
"""
from __future__ import annotations
from fractions import Fraction
from pathlib import Path
import fcntl
import hashlib
import json
from flint import arb,ctx

import fourfold_parameter_expanded_time_domain as proof_source
from fourfold_forward_density_pipeline_spatial_v7 import checked_extended_domain
from fourfold_forward_density_pipeline_Q1024_v3 import upper
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_beta_affine import sha
from fourfold_saved_circle_field_multidomain_budget import read
from fourfold_phase_unified_scalar_time_circle import exact_time


def _same_base(left,right):
    for key in ('domain_sha256','descriptor_sha256','target_object_sha256',
                'target_root_sha256','exact_delta_fraction','mode','branch_sign'):
        if left[key]!=right[key]:
            raise ValueError('expanded parameter proof has another base identity: '+key)
    if (tuple(map(Fraction,left['common_span']))!=tuple(map(Fraction,right['common_span']))
        or tuple(map(exact_time,left['exact_time_endpoints']))!=
           tuple(map(exact_time,right['exact_time_endpoints']))):
        raise ValueError('expanded parameter proof changes the actual germ or time coordinates')


def checked_parameter_proof(path,source,domain_path,germ_index,args):
    doc=read(path)
    if (doc.get('kind')!='actual_expanded_time_parameter_source_bounds'
        or not doc.get('complete') or not doc.get('complete_center_source_proved')
        or doc['source_sha256']!=sha(proof_source.__file__)
        or doc['domain_sha256']!=sha(domain_path)
        or sha(doc['domain_path'])!=sha(domain_path)
        or doc['selected_germ_index']!=germ_index):
        raise ValueError('incomplete or mismatched expanded parameter proof')
    for name,digest in doc['dependency_sha256'].items():
        if sha(Path(__file__).with_name(name))!=digest:
            raise ValueError('expanded parameter dependency changed: '+name)
    expanded_path=Path(doc['expanded_true_domain_path'])
    if sha(expanded_path)!=doc['expanded_true_domain_sha256']:
        raise ValueError('expanded true domain changed')
    expanded,row=checked_extended_domain(expanded_path,domain_path,germ_index)
    point=source.identity();center=doc['center_parameter_identity']
    _same_base(center['base_identity'],point['base_identity'])
    _same_base(doc['original_central_identity']['base_identity'],point['base_identity'])
    if (center['source_sha256']!=sha(Path(__file__).with_name('fourfold_phase_parameter_time_circle.py'))
        or center['local_root_jets_sha256']!=sha(args.local_root_jets)
        or not center.get('actual_center_parameter_only')
        or not center.get('fixed_physical_tau_parameter_derivatives')):
        raise ValueError('expanded center source or root derivatives changed')
    R=exact_arb(Fraction(doc['time_radius']))
    strip=exact_arb(Fraction(doc['physical_theta_strip']))
    if (not R>source.outer or strip!=source.strip
        or Fraction(doc['time_radius'])!=Fraction(expanded['time_radius'])
        or Fraction(doc['physical_theta_strip'])!=Fraction(expanded['physical_theta_strip'])):
        raise ValueError('expanded parameter bound has incompatible disks')
    uniform=bool(args.uniform_half_width)
    if uniform:
        if not doc.get('complete_uniform_real_parameter_source_proved'):
            raise ValueError('the uniform source has no larger-disk proof')
        tube=doc['uniform_parameter_identity'];_same_base(tube['base_identity'],point['base_identity'])
        if (tube['source_sha256']!=sha(Path(__file__).with_name('fourfold_phase_uniform_parameter_time_circle.py'))
            or tube['local_root_jets_sha256']!=sha(args.local_root_jets)
            or tube['wide_root_jets_sha256']!=sha(args.wide_root_jets)
            or not tube.get('whole_real_parameter_tube')
            or not tube.get('fixed_physical_tau_parameter_derivatives')):
            raise ValueError('expanded uniform source or true root tube changed')
        lo,hi=map(Fraction,tube['exact_parameter_interval'])
        point_lo,point_hi=map(Fraction,point['exact_parameter_interval'])
        if not lo<=point_lo<=point_hi<=hi:
            raise ValueError('larger-disk proof does not contain the sampled parameter interval')
        moduli=doc['uniform_source_moduli']
    else:
        moduli=doc['center_source_moduli']
    values=[upper(moduli[key]) for key in ('fp','fpp')]
    if any(not v.is_finite() or not v>0 for v in values):
        raise ValueError('nonpositive expanded source modulus')
    return R,values,doc


def extended_parameter_domains(source,domain_path,germ_index,args,report,orders):
    domains=[[(source.outer,upper(source.moduli[('fp','fpp')[j-1]]))] for j in orders]
    record=dict(point_sampler_domain_unchanged=True,point_primitive_nodes=source.nodes,
                crossing_caps_still_from_original_models=True,attempts=[])
    report['expanded_parameter_domains']=record
    explicit=getattr(args,'expanded_parameter_proof',None)
    if explicit is not None:
        R,values,proof=checked_parameter_proof(explicit,source,domain_path,germ_index,args)
        record.update(path=str(explicit),sha256=sha(explicit),proved=True,
                      proof_primitive_nodes=proof['nodes'],reused=True)
    else:
        explicit_domain=getattr(args,'expanded_domain',None)
        directory=getattr(args,'expanded_domain_directory',None)
        candidates=([Path(explicit_domain)] if explicit_domain is not None else
                    sorted(Path(directory).glob('forward_%04d_*.json.gz'%source.base.domain['segment']))
                    if directory is not None else [])
        selected=None
        for path in candidates:
            try:
                candidate=read(path)
                if (candidate.get('original_domain_sha256')!=sha(domain_path)
                    or not candidate.get('proved_selected_actual_germs')):
                    continue
                checked_extended_domain(path,domain_path,germ_index)
                selected=path;break
            except (KeyError,ValueError,FileNotFoundError) as exc:
                record['attempts'].append(dict(path=str(path),rejected=str(exc)))
                if explicit_domain is not None:
                    raise
        if selected is None:
            record.update(proved=False,reason='no complete matching larger true domain')
            return domains
        half=max(Fraction(args.uniform_half_width),Fraction(args.expanded_proof_half_width))
        key=dict(domain=sha(domain_path),expanded=sha(selected),germ=germ_index,
                 descriptor=sha(args.descriptor),local_root=sha(args.local_root_jets),
                 wide_root=sha(args.wide_root_jets),half_width=str(half),
                 nodes=args.expanded_proof_nodes,root_nodes=args.root_nodes,
                 bits=args.expanded_proof_bits,radial_degree=args.radial_degree,
                 proof_source=sha(proof_source.__file__))
        digest=hashlib.sha256(json.dumps(key,sort_keys=True).encode()).hexdigest()
        cache=Path(args.parameter_proof_directory);cache.mkdir(parents=True,exist_ok=True)
        path=cache/('forward_%04d_%s.json.gz'%(source.base.domain['segment'],digest[:20]))
        lockdir=Path(args.parameter_proof_lock_directory);lockdir.mkdir(parents=True,exist_ok=True)
        with (lockdir/(digest+'.lock')).open('a') as lock:
            fcntl.flock(lock,fcntl.LOCK_EX)
            reused=path.exists()
            if not reused:
                precision,cap=ctx.prec,ctx.cap
                try:
                    proof_source.prove(args.descriptor,domain_path,selected,path,
                        local_root_jets=args.local_root_jets,wide_root_jets=args.wide_root_jets,
                        half_width=half,nodes=args.expanded_proof_nodes,root_nodes=args.root_nodes,
                        germ_index=germ_index,radial_degree=args.radial_degree,
                        bits=args.expanded_proof_bits)
                finally:
                    ctx.prec,ctx.cap=precision,cap
            proof=read(path)
            record.update(path=str(path),sha256=sha(path),proof_key=key,reused=reused)
            if not proof.get('complete'):
                record.update(proved=False,failure=proof.get('failure','unproved larger parameter disk'))
                return domains
            R,values,proof=checked_parameter_proof(path,source,domain_path,germ_index,args)
        record.update(proved=True,proof_primitive_nodes=proof['nodes'])
    for index,order in enumerate(orders):
        domains[index].append((R,values[order-1]))
    record['actual_source_domains']=[
        [dict(radius=ball_record(radius),modulus=ball_record(modulus)) for radius,modulus in group]
        for group in domains]
    return domains
