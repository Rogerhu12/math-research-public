#!/usr/bin/env python3
"""Compare every regenerated scientific array using the original shard format.

Only if all original gzip bytes, all initial-state bits and the exact metric
metadata match may the historical index be restored.  A mismatch is a new
centre and does not authorize any historical candidate-dependent certificate.
"""
from __future__ import annotations
import argparse,gzip,hashlib,io,json,sys
from pathlib import Path
import numpy as np

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--topic',type=Path,required=True)
    ap.add_argument('--candidate',type=Path,required=True)
    ap.add_argument('--manifest',type=Path,required=True)
    ap.add_argument('--out-dir',type=Path,required=True)
    a=ap.parse_args();sys.path.insert(0,str(a.topic/'scripts'))
    from fourfold_codazzi_candidate_shards import load_candidate
    sha=lambda b:hashlib.sha256(b).hexdigest()
    a.out_dir.mkdir(parents=True,exist_ok=False)
    manifest=json.loads(a.manifest.read_text());old=manifest['complete_candidate_index']
    current=load_candidate(a.candidate);meta=json.loads(str(current['metadata']))
    r=current['radial_nodes'];c=current['piece_coefficients'];initial=current['initial_state']
    scientific_fields=['coordinates','modes','physical_frequency_factor','amplitude','exact_float_amplitude',
        'nu','exact_float_nu','object_sha256','new_metric_family','exact_bump','mean_boundary',
        'finite_state_angle','boundary_angle','exact_cap_cut','exact_float_q_values','q_vector_sha256']
    matches={k:meta.get(k)==old['metadata'].get(k) for k in scientific_fields}
    initial_equal=np.array_equal(initial.view(np.uint64),np.asarray(old['initial_state'],dtype=np.float64).view(np.uint64))
    shapes_equal=list(c.shape)==old['coefficient_shape'] and len(r)==old['radial_nodes_count']
    rows=[]
    if shapes_equal:
        for part in old['parts']:
            left=part['first_interval'];right=part['last_interval_exclusive']
            nodes=r[left:right+1];coefficients=c[:,left:right,:]
            buffer=io.BytesIO();np.savez(buffer,radial_nodes=nodes,piece_coefficients=coefficients)
            raw=buffer.getvalue();compressed=io.BytesIO()
            with gzip.GzipFile(filename=part['file'],mode='wb',fileobj=compressed,mtime=0) as f:f.write(raw)
            encoded=compressed.getvalue();same=sha(encoded)==part['sha256'] and len(encoded)==part['bytes']
            rows.append(dict(file=part['file'],matches_historical_bytes=same,sha256=sha(encoded),
                expected_sha256=part['sha256'],uncompressed_payload_sha256=sha(raw),
                bytes=len(encoded),first_interval=left,last_interval_exclusive=right))
            # These bytes are computed from the complete new arrays, never from
            # an old checksum. The directory is explicitly an identity attempt.
            (a.out_dir/part['file']).write_bytes(encoded)
    all_equal=shapes_equal and initial_equal and all(matches.values()) and all(p['matches_historical_bytes'] for p in rows)
    restored=None
    if all_equal:
        old_index=(json.dumps(old,indent=2,allow_nan=False)+'\n').encode()
        if sha(old_index)!=manifest['candidate_sha256']:
            raise ValueError('manifest serialization does not reconstruct the original index')
        restored=a.out_dir/Path(manifest['candidate_path']).name
        restored.write_bytes(old_index)
        load_candidate(restored)
    result=dict(kind='complete_original_scientific_array_identity_comparison',complete=True,
        candidate_sha256=sha(a.candidate.read_bytes()),manifest_sha256=sha(a.manifest.read_bytes()),
        producer_sha256=sha(Path(__file__).read_bytes()),all_scientific_fields=matches,
        initial_state_uint64_equal=initial_equal,complete_shape_equal=shapes_equal,parts=rows,
        original_scientific_arrays_and_container_recovered=all_equal,
        historical_certificate_reuse_authorized_by_identity_only=all_equal,
        new_centre_if_any_mismatch=not all_equal,restored_candidate=str(restored) if restored else None)
    (a.out_dir/'identity-report.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps(result,indent=2),flush=True)

if __name__=='__main__':main()
