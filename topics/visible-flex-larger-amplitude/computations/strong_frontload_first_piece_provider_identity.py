#!/usr/bin/env python3
"""Bind a completed first-piece certificate to the actual frozen provider table.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
Only source identity, exact stored coefficient equality and 64 binary Gauss
triples are checked. No profile geometry, ODE, Node or Newton is evaluated.
"""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[name]='1'
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import struct
import time

PINS={
    'alternative-neck-provider.py':'84ed048425c8b0f4deeec8af37828e318150cde5d59995da77f64d923591b9c2',
    'alternative-neck-flatturn.py':'c0578ed401a2433c72ec99702c9c32a8412c66264a7fb81a8b8c74ba054fbbdd',
    'alternative-neck-excursion.py':'f70571b8356e33cb89eabae2dba4e173e6612dac4d65d5df74f5ec14c34ad53c',
    'strong_monotone_initial_speed.py':'12d6340d4e9dce27ee93d390971d0258cc1e2299dedf99fe21365a70494549e7',
    'strong_monotone_initial_speed_anchor.py':'583af82cdd6bb672325844587d8aac67e47365ccb5152ac2eae543837adc0ffc',
}
HERE=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):return json.loads(Path(p).read_text())
def q(z):return F(z['numerator'])/F(z['denominator'])

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ('certificate','resource','table','out'):
        ap.add_argument('--'+name,type=Path,required=True)
    a=ap.parse_args();start=time.monotonic()
    if a.out.exists():raise FileExistsError(a.out)
    gates={}
    def check(name,yes):
        if not yes:raise ArithmeticError(name)
        gates[name]=True
    cert,owned,table=map(read,(a.certificate,a.resource,a.table))
    check('formal_first_piece_result',cert['all_gates'] and cert['gate_count']==1041
        and cert['all_ellipse_domain_boxes_passed'] and cert['input_kind']=='completed-unsolved-warm'
        and owned['wait4_observed'] and owned['exitcode']==0 and owned['termination_signal'] is None)
    source=HERE/'strong_frontload_stored_first_piece_ellipse_gauss64.py'
    check('same_producer_source',sha(source)==cert['source_sha256'])
    check('owned_same_certificate',owned['command'][owned['command'].index('--out')+1]==str(a.certificate))
    check('same_proved_table',sha(a.table)==cert['input_sha256'][str(a.table)])
    for name,wanted in PINS.items():check('frozen_'+name,sha(HERE/name)==wanted)
    spec=importlib.util.spec_from_file_location('frontload_frozen_table_identity',HERE/'alternative-neck-provider.py')
    provider=importlib.util.module_from_spec(spec);spec.loader.exec_module(provider)
    check('actual_transitive_flat_source',sha(provider.fl.__file__)==PINS['alternative-neck-flatturn.py'])
    check('actual_transitive_excursion_source',sha(provider.base.__file__)==PINS['alternative-neck-excursion.py'])
    check('actual_table_shape',len(provider.base.gx)==len(provider.base.gw)==len(provider.base.gu)==64)
    data=b''
    for i,(x,w,u,row) in enumerate(zip(provider.base.gx,provider.base.gw,provider.base.gu,table['root_weight_rows'])):
        check('actual_gx_'+str(i),F.from_float(float(x))==q(row['actual_binary_gx']))
        check('actual_normalized_gw_'+str(i),F.from_float(float(w))/2==q(row['actual_normalized_binary_weight']))
        check('actual_gu_'+str(i),F.from_float(float(u))==q(row['actual_binary_gu']))
        check('actual_positive_table_'+str(i),w>0 and 0<u<1)
        data+=struct.pack('<ddd',float(x),float(w),float(u))
    table_sha=hashlib.sha256(data).hexdigest()
    check('all_table_bits_identical',table_sha==table['binary_table_float64le_sha256'])
    from strong_monotone_initial_speed_anchor import physical_piece,source_identity
    profile=cert['actual_profile']
    actual=physical_piece(1.,profile['delta'],profile['vu'],profile['start_acceleration'],
                          profile['initial_speed_frontload'],cert['degree'])
    check('actual_stored_first_piece_coefficients_identical',actual==cert['exact_provider_first_piece_data'])
    check('same_initial_anchor',cert['coherent_radius_control_exact'][0]=={'numerator':'1','denominator':'1'})
    output=dict(schema='frontload-first-piece-provider-and-Gauss-table-identity-v1',
        author='geometry_audit (GPT-6 Astra Pro; AI-assisted)',source_sha256=sha(__file__),
        inputs={str(p):sha(p) for p in (a.certificate,a.resource,a.table)},
        frozen_source_sha256=PINS,anchor_identity=source_identity(),
        actual_binary_Gauss64_table_sha256=table_sha,gate_count=len(gates),gates=gates,all_gates=True,
        input_kind=cert['input_kind'],new_ODE_Node_Newton_or_geometry_samples=0,
        floating_function_evaluation_or_coordinate_alignment_certified=False,
        elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    a.out.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(dict(out=str(a.out),sha256=sha(a.out),gates=len(gates),all_gates=True)),flush=True)

if __name__=='__main__':main()
