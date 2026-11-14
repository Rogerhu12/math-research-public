#!/usr/bin/env python3
"""Retain the already computed Cartesian points of a complete fine warm run.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
Only derived array storage is added to the original mean1552 geometry loop.
The accepted fine baseline, verified coarse increment, original full means,
curvature, domains and all coordinates remain unchanged. Saved point chunks
are scratch-only and are not a closed-surface or Hausdorff certificate.
"""
import argparse
import ast
import hashlib
import inspect
import json
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
GEOMETRY_SHA='614a671b86dc1bacccf52d62311c51a7473c83072f9ce39e81ae3e421541dd86'
FINE_SHA='c986073622d4ebabb2be7d1eea46fe8ac4966a404b56bbc6a6af3b48371092bc'


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    p=argparse.ArgumentParser(add_help=False,description=__doc__)
    p.add_argument('--point-cloud-array',type=Path,required=True)
    own,remaining=p.parse_known_args()
    if own.point_cloud_array.exists():raise FileExistsError('Use a fresh complete actual point array')
    import root_actual_geometry_field_complete_mean as geometry
    import root_actual_coarse_increment_geometry_complete_mean as fine
    if sha(geometry.__file__)!=GEOMETRY_SHA or sha(fine.__file__)!=FINE_SHA:
        raise ValueError('Original complete fine geometry adapter changed')
    original=inspect.getsource(geometry.main)
    edits=[
        ("        values = np.memmap(resident_backing, mode='w+', shape=(len(t), angular, 3), dtype=np.float64)\n",
         "        values = np.memmap(resident_backing, mode='w+', shape=(len(t), angular, 3), dtype=np.float64)\n"
         "        point_backing = tempfile.TemporaryFile(prefix='fine_actual_points_')\n"
         "        point_values = np.memmap(point_backing, mode='w+', shape=(len(t),angular,3), dtype=np.float64)\n"),
        ("            points[:, :, 2] += height[sl, None]\n",
         "            points[:, :, 2] += height[sl, None]\n"
         "            point_values[sl] = points\n"),
        ("                release_values(values)\n                observed_rss_guard()\n",
         "                release_values(values)\n                release_values(point_values)\n                observed_rss_guard()\n"),
        ("        storage = write_chunks(output, values, release=release_values, observe=observed_rss_guard)\n",
         "        storage = write_chunks(output, values, release=release_values, observe=observed_rss_guard)\n"
         "        point_storage = write_chunks(POINT_ARRAY_OUTPUT, point_values, release=release_values, observe=observed_rss_guard)\n"),
        ("            geometry_fields=dict(file=str(output), sha256=sha(output), bytes=sum(item['bytes'] for item in storage['chunks']),\n",
         "            geometry_fields=dict(file=str(output), sha256=sha(output), bytes=sum(item['bytes'] for item in storage['chunks']),\n"
         "                actual_point_cloud=dict(file=str(POINT_ARRAY_OUTPUT),sha256=sha(POINT_ARRAY_OUTPUT),\n"
         "                    storage=point_storage,shape=list(point_values.shape),components=['x','y','z'],\n"
         "                    capture_source_sha256=POINT_CAPTURE_SHA,complete_original_mean=mean_angular,\n"
         "                    coordinates='The same already computed physical Cartesian points, same height anchor and complete mean as this geometry loop.',\n"
         "                    actual_prefix_only=True,full_closed_surface_claim=False),\n")]
    transformed=original
    for old,new in edits:
        if transformed.count(old)!=1:raise ValueError('Original pure point capture site differs')
        transformed=transformed.replace(old,new,1)
    reverse=transformed
    for old,new in reversed(edits):reverse=reverse.replace(new,old,1)
    if reverse!=original:raise ValueError('A non-storage original field formula changed')
    ast.parse(transformed)
    namespace=dict(geometry.main.__globals__,POINT_ARRAY_OUTPUT=own.point_cloud_array,
                   POINT_CAPTURE_SHA=sha(__file__))
    exec(compile(transformed,'<original-complete-geometry-plus-Cartesian-array-storage>','exec'),namespace)
    oldmain,oldargv=geometry.main,sys.argv
    geometry.main=namespace['main'];sys.argv=[oldargv[0],*remaining]
    try:fine.main()
    finally:geometry.main,sys.argv=oldmain,oldargv
    report=Path(remaining[remaining.index('--inspect-warm-output')+1]);value=json.loads(report.read_text())
    points=value['geometry_fields']['actual_point_cloud']
    if points['sha256']!=sha(own.point_cloud_array) or points['complete_original_mean']!=1552:
        raise ValueError('Complete actual Cartesian array identity differs')
    value['pure_point_capture_adapter']=dict(source_sha256=sha(__file__),original_geometry_sha256=GEOMETRY_SHA,
        original_fine_warm_sha256=FINE_SHA,exact_reverse_recovers_original_main=True,
        original_geometry_main_sha256=hashlib.sha256(original.encode()).hexdigest(),
        transformed_storage_main_sha256=hashlib.sha256(transformed.encode()).hexdigest(),
        mathematical_mean_curvature_and_domain_formulas_unchanged=True,
        scratch_only_reproducible_point_chunks=True)
    temporary=report.with_name(report.name+'.points-provenance.tmp')
    temporary.write_text(json.dumps(value,indent=2)+'\n');temporary.replace(report)
    print(json.dumps(dict(event='actual_fine_point_cloud_capture_finished',report=str(report),sha256=sha(report),
                         point_array=str(own.point_cloud_array),point_sha256=sha(own.point_cloud_array))),flush=True)


if __name__=='__main__':main()
