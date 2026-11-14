#!/usr/bin/env python3
"""Same complete saved P at the true finite reference Y: local Taylor cost.

Every option still evaluates all finite modes and pays the full finite
Taylor tail.  No true field samples or new true-field domain are used.
"""
from __future__ import annotations
from fractions import Fraction
import json
from pathlib import Path
import time
import numpy as np
from flint import arb,acb,ctx
from fourfold_phase_beta_affine import sha
from fourfold_saved_circle_field_multidomain_budget import read,upper
from fourfold_phase_actual_field_fourier_package import decode_complex
from fourfold_packaged_reference_bidisk import PackageReference
from fourfold_exact_fourier_multipoint import time_coefficients
from fourfold_fourier_local_taylor import finite_taylor_evaluate


def main():
    ctx.prec=320
    base=Path('data/phase_ring_continuation')
    certificate=base/'step5_forward_density_pipeline_pilot419_Q1024/forward_0419_ef134f2a18.json.gz'
    document=read(certificate);link=document['field_exact_rectangle'];path=Path(link['path'])
    if sha(path)!=link['sha256']:raise ValueError('finite P manifest changed')
    manifest=read(path)
    if (not manifest['complete'] or not manifest['exactly_reloaded'] or manifest['frequency_scale']!=4
        or manifest['identity']['identity']!=document['identity']):
        raise ValueError('finite field normalization/identity differs')
    positive=[]
    for item in manifest['shards']:
        shard=path.parent/item['path']
        if sha(shard)!=item['sha256'] or len(positive)!=item['time_start']:
            raise ValueError('finite P exact shard identity/cover changed')
        payload=read(shard)
        positive.extend([list(map(decode_complex,row)) for row in payload['coefficients']])
    if len(positive)!=manifest['time_terms']:raise ValueError('incomplete finite time rectangle')
    full=np.array([[z.conjugate() for z in row[:0:-1]]+row for row in positive],dtype=object)
    package=base/'step5_forward419_exact_reference_package.npz.gz'
    reference=PackageReference(package)
    if reference.identity['target_object_sha256']!=document['identity']['reference']['target_object_sha256']:
        raise ValueError('finite P and reference objects differ')
    u=acb(0,arb(5)/4)
    tic,cpu=time.monotonic(),time.process_time()
    theta,_,_=reference.grid(u,4096,Fraction(0))
    row=time_coefficients(full,u)
    report=dict(kind='same_full_finite_P_at_actual_complex_time_reference_cost',complete=False,
        source_sha256=sha(__file__),field_certificate_sha256=sha(certificate),
        field_manifest_sha256=sha(path),reference_package_sha256=sha(package),
        normalized_time='5i/4',initial_label_strip='0',nodes=4096,bits=320,
        field_degree=(len(row)-1)//2,finite_time_terms=len(full),
        input_preparation_CPU=time.process_time()-cpu,input_preparation_wall=time.monotonic()-tic,
        cases=[],limitation='Finite-node evaluation cost only; the true f-P error and complete-label reconstruction remain separate.')
    output=Path('notes/2026-11-12-actual419-finite-composition-cost.json')
    baseline=None;best=None
    for anchors,radius in [(512,Fraction(1,64)),(512,Fraction(1,32)),(512,Fraction(1,16)),
                           (256,Fraction(1,32)),(1024,Fraction(1,32)),(512,Fraction(3,64))]:
        try:
            values,info=finite_taylor_evaluate(row,theta,anchors=anchors,radius=radius,tail_target='1e-42')
            if baseline is None:baseline=values
            if not all(v.real.overlaps(w.real) and v.imag.overlaps(w.imag) for v,w in zip(values,baseline)):
                raise ValueError('two complete finite evaluations do not overlap')
            data=dict(passed=True,all_4096_nodes_overlap_baseline=True,**info)
            if best is None or info['total_cpu_seconds']<best[0]:best=info['total_cpu_seconds'],values,len(report['cases'])
        except ValueError as exc:
            data=dict(passed=False,anchors=anchors,radius=str(radius),failure=str(exc))
        report['cases'].append(data);output.write_text(json.dumps(report,indent=2)+'\n')
        print(json.dumps({k:data[k] for k in ('passed','anchors','terms','Taylor_radius','total_cpu_seconds') if k in data}),flush=True)
    if best is None:raise ValueError('no finite Taylor option passed')
    K=(len(row)-1)//2;checks=[]
    for index in (0,4096//7,4096//3,4095):
        direct=sum((a*(acb(0,4*(k-K))*theta[index]).exp() for k,a in enumerate(row)),acb(0))
        got=best[1][index]
        if not got.real.overlaps(direct.real) or not got.imag.overlaps(direct.imag):
            raise ValueError('best finite evaluation misses an independent full Laurent sum')
        checks.append(dict(node=index,independent_full_Laurent_overlap=True))
    report.update(complete=True,fastest_case_index=best[2],independent_checks=checks)
    output.write_text(json.dumps(report,indent=2)+'\n')


if __name__=='__main__':main()
