#!/usr/bin/env python3
"""Actual projected high physical-angle lift and compressed cap contact costs.

The lift is the true shear extension followed by the fixed physical Fourier
projection.  Its full transport commutator is included explicitly.
"""
from __future__ import annotations
import argparse,hashlib,json
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx
from fourfold_phase_beta_interval import ball_record


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def lo(r):return arb(r['lower']).lower()
def hi(r):return arb(r['upper']).upper()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--volume',type=Path,default=Path('notes/2026-11-12-actual-physical-high-energy-budget.json'))
    ap.add_argument('--collar',type=Path,default=Path('notes/2026-11-12-positive-family-root-collar.json'))
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();ctx.prec=256
    volume,collar=[json.loads(p.read_text()) for p in (args.volume,args.collar)]
    if not volume.get('proved') or not collar.get('complete'):
        raise ValueError('actual body and collar proofs must be complete')
    if volume['source_sha256']!=sha(Path(__file__).with_name('fourfold_phase_physical_high_energy_budget.py')):
        raise ValueError('actual compressed body source changed')
    if volume['exact_source_cell_hashes'][str(args.collar)]!=sha(args.collar):
        raise ValueError('projected lift is not in the same actual body')
    a,b=map(Fraction,collar['exact_parameter_interval']);c,d=map(Fraction,volume['exact_parameter_interval'])
    if not a<=c<=d<=b:raise ValueError('parameter family mismatch')
    Q0=max(max(abs(arb(float(x))).upper() for x in r['real_geometry']['drift'])
           for r in collar['cells']).upper()
    Q1=max(max(abs(arb(float(x))).upper() for x in r['real_geometry']['drift_theta'])
           for r in collar['cells']).upper()
    const=collar['operator_constants'];ell=lo(const['length_lower']);M=hi(const['M_upper'])
    table=[]
    for row in volume['cutoff_table']:
        if not row['proved_positive']:continue
        N=row['N'];lam=arb(row['first_retained_physical_frequency'])
        lam23=(lam.log()*arb(2)/3).exp()
        dn=max(arb(1),1/(ell*lam23)).upper()
        comm=(8*N*Q0+Q1).upper();un=(comm/(arb(3).sqrt()*lam23)).upper()
        energy=(M*((dn.sqrt()+un)**2+arb(1)/12)).upper()
        kappa=lo(row['compressed_L2_coercivity'])
        contact=(energy/kappa).sqrt().upper()
        table.append(dict(N=N,first_retained_physical_frequency=row["first_retained_physical_frequency"],
          physical_projection_transport_commutator=ball_record(comm),
          radial_lift_factor=ball_record(dn),normalized_commutator_factor=ball_record(un),
          true_projected_boundary_lift_energy=ball_record(energy),
          compressed_L2_Poisson_and_source_contact=ball_record(contact),
          compressed_regular_Robin_load_to_energy=ball_record(arb(7).sqrt().upper()),
          compressed_regular_Robin_load_to_L2=ball_record((arb(7)/kappa).sqrt().upper()),
          compressed_regular_Robin_load_to_root_contact=ball_record((7*energy).sqrt().upper())))
    report=dict(kind='actual_physical_high_projected_lift_and_compressed_full_cap_contact',proved=True,
      source_sha256=sha(__file__),input_sha256={str(p):sha(p) for p in (args.volume,args.collar)},
      exact_parameter_interval=volume['exact_parameter_interval'],
      origin_inputs_sha256=volume['origin_inputs_sha256'],direction_sha256=volume['direction_sha256'],
      physical_drift_modulus=ball_record(Q0),physical_drift_theta_modulus=ball_record(Q1),
      local_length_lower=ball_record(ell),local_sheared_matrix_upper=ball_record(M),
      actual_collar_cells=len(collar['cells']),cutoff_table=table,
      norm_conventions=dict(root_input='physical high Fourier homogeneous H^(1/3)',
                            volume_source='L2(dx dtheta), projected against the genuine high form domain',
                            root_contact='physical high homogeneous H^(-1/3)',
                            regular_Robin_load='physical high homogeneous H^(-1/2)'),
      scope=['Poisson and contact are for the actual restricted high form on the entire true cap.',
             'The low root modes and both regular mean slots remain in the complete Schur system.',
             'No commutator is omitted; E is projected after the genuine physical shear lift.',
             'The bound does not replace the full uncompressed cap contact by the compressed contact.'])
    args.out.parent.mkdir(parents=True,exist_ok=True);args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'Q0':str(Q0),'Q1':str(Q1),'table':[{'N':r['N'],
       'energy':r['true_projected_boundary_lift_energy']['ball'],
       'contact':r['compressed_L2_Poisson_and_source_contact']['ball']} for r in table]},indent=2))


if __name__=='__main__':main()
