"""Deterministic moment/norm comparison, plus one matched-moment old direction.

All supremum diagnostics are sampled, not interval estimates. The replacement
basis separately supplies rational conservative derivative bounds. No BVP is
solved, and matching higher moments need not preserve the primary moment.
"""
import argparse
import gzip
import importlib.util
import json
import time
from pathlib import Path
import numpy as np
from audit_uniform_core import sha
from complementary_moment_basis import ComplementaryMomentBasis
from uniform_complement_core import make_core_class


def finite_norms(basis,sample_count):
    phi=basis.T*np.arange(sample_count)/sample_count
    jets=basis.support_jets(phi,3)
    rho=np.max(abs(jets[0]+jets[2]),axis=1)
    prime=np.max(abs(jets[1]+jets[3]),axis=1)
    bound,prime_bound,_=basis.homotopy_rho_bounds(1.)
    return dict(sample_count=sample_count,
        support_condition=basis.constants['support_condition'],
        rho_condition=basis.constants['rho_condition'],
        canonical_rho_sup_max=float(rho.max()),
        canonical_rho_prime_sup_max=float(prime.max()),
        canonical_rho_sup_per_unit_high_rho_max=float(np.max(rho/(basis.target_freq**2-1))),
        canonical_rho_prime_sup_per_unit_high_rho_max=float(np.max(prime/(basis.target_freq**2-1))),
        conservative_rho_bound_max=float(bound.max()),
        conservative_rho_prime_bound_max=float(prime_bound.max()),
        fundamental_leakage_max=float(abs(basis.fundamental_leakage).max()),
        rational_neumann_residual_upper=float(basis.certificate['neumann_residual']))


def old_lookup(paths):
    out={}
    for path in paths:
        data=json.loads(path.read_text())
        for row in data['rows']:
            for lock,key in ((False,'unlocked'),(True,'locked')):
                item=row[key]
                out[(row['halfwidth'],row['M'],lock)]=dict(source=str(path),source_sha256=sha(path),
                    support_condition=item['support_moment_condition'],rho_condition=item['rho_moment_condition'],
                    canonical_rho_sup_max=max(item['canonical_rho_sup_per_unit_high_support']),
                    canonical_rho_prime_sup_max=max(item['canonical_rho_prime_sup_per_unit_high_support']),
                    sample_count=item['sample_count'])
    return out


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--reference-core',type=Path,required=True)
    p.add_argument('--old-diagnostics',type=Path,nargs='+',required=True)
    direction=p.add_mutually_exclusive_group(required=True)
    direction.add_argument('--checkpoint',type=Path)
    direction.add_argument('--direction-input',type=Path,help='Compact literal parameter input; contains no BVP arrays.')
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();start=time.monotonic();old=old_lookup(a.old_diagnostics)
    spec=importlib.util.spec_from_file_location('basis_comparison_reference',a.reference_core)
    ref=importlib.util.module_from_spec(spec);spec.loader.exec_module(ref)
    Core=make_core_class(ref.PlateauSupportCore)
    rows=[]
    for halfwidth,eps in ((.28,.08),(.28,.12),(.16,.08),(.145,.08)):
        for M in (4,6,8):
            for lock in (False,True):
                b=ComplementaryMomentBasis(base_mode=4,modes=M,halfwidth=halfwidth,transition=eps,lock_fundamental=lock)
                rows.append(dict(halfwidth=halfwidth,control_transition=eps,modes=M,lock_fundamental=lock,
                                 new=finite_norms(b,16384),old=old.get((halfwidth,M,lock))))
    if a.checkpoint is not None:
        cp=json.loads(gzip.decompress(a.checkpoint.read_bytes()));cs=cp['core_summary']
        provenance=dict(checkpoint=str(a.checkpoint),checkpoint_sha256=sha(a.checkpoint))
    else:
        compact=json.loads(a.direction_input.read_text());cs=compact['core_summary']
        provenance=dict(**compact['provenance'],direction_input_sha256=sha(a.direction_input))
    n=cs['base_mode'];M=len(cs['corrections'])+1;T=2*np.pi/n
    corrections=np.array(cs['corrections']);q=cs['q_parameter'];lam=cs['homotopy']
    plain=ref.PlateauSupportCore(q=q,corrections=np.zeros(M-1),base_mode=n,
        halfwidth=cs['halfwidth'],transition=cs['transition'],homotopy=1.,arc_nodes=512)
    freq=n*np.arange(1,M+1)
    def old_moments(order):
        x,w=np.polynomial.legendre.leggauss(order)
        ph=plain.a+plain.L*(x+1)/2
        b=plain._basis(ph)[1]
        return plain.L/T*(b*w)@np.cos(freq[:,None]*ph).T
    low=corrections@old_moments(200)
    low_check=corrections@old_moments(240)
    x,w=np.polynomial.legendre.leggauss(200);primary=np.zeros(M)
    for lo,hi in ((0.,plain.a),(plain.a,plain.a+plain.transition),(plain.a+plain.transition,T/2)):
        ph=(lo+hi)/2+(hi-lo)*x/2
        primary+=(2*(hi-lo)/T)*((w*q*plain.unit_rho(ph))@np.cos(freq[:,None]*ph).T)
    ph=T*np.arange(32768)/32768;C=np.cos(freq[:,None]*ph)
    old_jets=plain._basis(ph);old_rho=corrections@(old_jets[1]+old_jets[3])
    old_low_rho=(low*(1-freq**2))@C
    primary_hidden=q*plain.unit_rho(ph)-primary@C
    old_hidden=old_rho-old_low_rho
    direction=dict(**provenance,
        old_corrections=corrections.tolist(),q=q,homotopy=lam,base_mode=n,modes=M,
        higher_support_moments=low[1:].tolist(),old_primary_support_moment=float(low[0]),
        old_moment_200_to_240_difference=float(abs(low-low_check).max()),
        old_compact_control_rho_sup=float(abs(old_rho).max()),old_compact_control_hidden_rho_sup=float(abs(old_hidden).max()),
        old_combined_actual_hidden_rho_sup=float(lam*abs(primary_hidden+old_hidden).max()),
        primary_plateau_hidden_rho_sup=float(abs(primary_hidden).max()),
        caveat='New controls match only support modes 8,...,24. Primary leakage changes; none of these replacements is claimed to solve the old BVP.',
        replacements=[])
    for eps in (.08,.12,.16):
        b=ComplementaryMomentBasis(base_mode=n,modes=M,halfwidth=cs['halfwidth'],transition=eps)
        jets=b.support_jets(ph,3);high=low[1:]
        rho=high@(jets[0]+jets[2]);prime=high@(jets[1]+jets[3])
        new_low=np.r_[b.fundamental_leakage@high,high]
        hidden=rho-(new_low*(1-freq**2))@C
        item=dict(control_transition=eps,new_primary_support_moment=float(new_low[0]),
            primary_support_moment_change=float(new_low[0]-low[0]),
            compact_control_rho_sup=float(abs(rho).max()),compact_control_rho_prime_sup=float(abs(prime).max()),
            compact_control_hidden_rho_sup=float(abs(hidden).max()),
            combined_actual_hidden_rho_sup=float(lam*abs(primary_hidden+hidden).max()),
            **finite_norms(b,16384))
        try:
            core=Core(q=q,corrections=high,base_mode=n,halfwidth=cs['halfwidth'],transition=cs['transition'],
                      control_transition=eps,homotopy=lam,arc_nodes=4096)
            item['rho_guard']=dict(accepted=True,lower=core.rho_lower,sampled_min=core.rho_min_sample,
                                   sampled_max=core.rho_max_sample,grid_count=core.positivity_grid_per_sector)
        except FloatingPointError as e:item['rho_guard']=dict(accepted=False,message=str(e))
        direction['replacements'].append(item)
    report=dict(scope=__doc__,reference_core_sha256=sha(a.reference_core),
        source_sha256={n:sha(Path(__file__).with_name(n)) for n in ('compare_complement_controls.py','uniform_complement_core.py','complementary_moment_basis.py','moment_interval_bounds.py')},
        rows=rows,actual_direction=direction,elapsed_seconds=time.monotonic()-start)
    a.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(rows=len(rows),actual_direction=direction,elapsed_seconds=report['elapsed_seconds'])))


if __name__=='__main__':main()
