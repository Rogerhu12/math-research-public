#!/usr/bin/env python3
"""Zero-embed one ACTUAL M12 correction in a higher angular space.

No radial knot, quadrature rule, original g, physical domain, or source is
changed. Copying all old binary64 coefficients into their matching Fourier
channels introduces exactly zero position or derivative error. This is a
warm initial field, not a solved refinement or an exact isometry.
"""
from __future__ import annotations
import argparse,hashlib,json,time
from pathlib import Path
import numpy as np

DEFINITION_KEYS=('data_sha256','common_meta_sha256','bridge_sha256','joint_source_sha256',
 'background_source_sha256','background_tolerance','physical_prefix_length_numerical',
 'material_chart_length_numerical','true_cuff_exact','query_file_sha256','gauss')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def transfer(coeff,old_pm,old_zm,new_pm,new_zm):
    old_modes=[('planar',int(m)) for m in old_pm]+[('height',int(m)) for m in old_zm]
    new_modes=[('planar',int(m)) for m in new_pm]+[('height',int(m)) for m in new_zm]
    lookup={mode:i for i,mode in enumerate(new_modes)}
    if len(lookup)!=len(new_modes) or any(mode not in lookup for mode in old_modes):
        raise ValueError('Complete old angular space is not contained in the new one')
    out=np.zeros((coeff.shape[0],len(new_modes)),dtype=np.float64)
    indices=np.array([lookup[mode] for mode in old_modes],int)
    out[:,indices]=coeff
    if out[:,indices].tobytes()!=coeff.tobytes():
        raise ArithmeticError('Old binary coefficients did not survive unchanged')
    extra=np.setdiff1d(np.arange(len(new_modes)),indices)
    if np.count_nonzero(out[:,extra]):
        raise ArithmeticError('High angular channels are not exactly zero')
    return out,indices,extra

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for key in ('old-field','old-grid','old-result','new-grid','out'):
        ap.add_argument('--'+key,type=Path,required=True)
    args=ap.parse_args();started=time.monotonic()
    field=Path(str(args.out)+'.field.npz')
    if args.out.exists() or field.exists():raise FileExistsError('Fresh exact warm-transfer output required')
    old=json.loads(args.old_grid.read_text());new=json.loads(args.new_grid.read_text())
    result=json.loads(args.old_result.read_text())
    for key in DEFINITION_KEYS:
        if old[key]!=new[key]:raise ValueError('The fixed original problem changed: '+key)
    if old['unit_mesh']!=new['unit_mesh'] or 'unit_knots' in old or 'unit_knots' in new:
        raise ValueError('This frequency-only consumer requires exactly the same simple radial knot mesh')
    if new['order']<=old['order'] or new['angular']<=old['angular'] or new['angular']%old['angular']:
        raise ValueError('A strictly larger nested angular layer is required')
    if new['angular']<=2*(3*new['order']+1):raise ValueError('Aliased new correction space')
    for key,path in [('field_sha256',args.old_field),('grid_sha256',args.old_grid)]:
        if result[key]!=sha(path):raise ValueError('Old actual field identity mismatch: '+key)
    for key in ('original_exact_metric_unchanged','all_internal_interfaces_free','true_flat_cuff_included',
                'full_half_including_finite_tail_and_deep_collar'):
        if result.get(key) is not True:raise ValueError('Incomplete old actual half: '+key)
    expected_knots=np.asarray([0.]*6+old['unit_mesh'][1:-1]+[1.]*6,dtype=np.float64)
    with np.load(args.old_field,allow_pickle=False) as data:
        coeff=data['coefficients'].copy();knots=data['unit_knots'].copy()
        pm=data['planar_modes'].copy();zm=data['vertical_modes'].copy()
    if coeff.dtype!=np.float64 or not np.all(np.isfinite(coeff)):
        raise ValueError('Complete finite actual binary64 field required')
    if not np.array_equal(knots,expected_knots):
        raise ValueError('Actual saved radial basis disagrees with the unchanged physical grid')
    if not np.array_equal(pm,3*np.arange(-old['order'],old['order']+1)+1):
        raise ValueError('Complete original D3 planar angular modes required')
    if not np.array_equal(zm,3*np.arange(old['order']+1)):
        raise ValueError('Complete original reflected height angular modes required')
    if coeff.shape!=(len(expected_knots)-12,len(pm)+len(zm)):
        raise ValueError('Actual field is missing radial or angular coefficients')
    npm=3*np.arange(-new['order'],new['order']+1)+1;nzm=3*np.arange(new['order']+1)
    lifted,indices,extra=transfer(coeff,pm,zm,npm,nzm)
    np.savez_compressed(field,coefficients=lifted,unit_knots=knots,planar_modes=npm,vertical_modes=nzm)
    report={'schema':'6a65-M12-exact-frequency-only-warm-transfer-v1',
        'script_sha256':sha(__file__),'old_field_sha256':sha(args.old_field),
        'old_grid_sha256':sha(args.old_grid),'old_result_sha256':sha(args.old_result),
        'new_grid_sha256':sha(args.new_grid),'transferred_field_sha256':sha(field),
        'unchanged_definition_keys':list(DEFINITION_KEYS),'same_original_g':True,
        'same_physical_mesh_and_radial_knots':True,'same_training_and_observation_Gauss_rules':True,
        'old_angular_order':old['order'],'new_angular_order':new['order'],
        'old_shape':list(coeff.shape),'new_shape':list(lifted.shape),
        'old_channels_copied':len(indices),'new_zero_channels':len(extra),
        'old_coefficient_bytes_unchanged':True,'exact_position_and_all_derivatives_unchanged':True,
        'exact_native_six_jet_transfer_errors':['0']*6,
        'exact_physical_material_six_jet_transfer_errors':['0']*6,
        'D3_and_ambient_reflection_retained':True,
        'complete_central_and_true_cuff_zero_two_jets_retained':True,
        'new_nonlinear_solve_executed':False,'exact_isometry_proved':False,
        'raw_retention':'Temporary only; no raw Git/artifact/release.',
        'seconds':time.monotonic()-started}
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(report,indent=2,allow_nan=False))
if __name__=='__main__':main()
