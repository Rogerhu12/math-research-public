#!/usr/bin/env python3
"""Explicit resource budget for the original true M14/Node computation.

This is a distinct true-coupled wrapper, not the affine-only 1.5 GiB wrapper.
RLIMIT_DATA is inherited separately by each child; it is not an aggregate RSS
or cgroup limit. The original Node heap option and every mathematical argument
remain unchanged. Resource failure never implies mathematical nonexistence.
"""
import hashlib, importlib.util, json, resource
from pathlib import Path

CAP=4*1024*1024*1024
GUARD_SHA='cf1e2364300015c841b2070be51e948dc7ba37ef5b98eef0441819bca1e6aabd'

def main():
    path=Path(__file__).with_name('db6f-root-run-space-guarded.py')
    assert hashlib.sha256(path.read_bytes()).hexdigest()==GUARD_SHA
    prior=resource.getrlimit(resource.RLIMIT_DATA)
    effective=min([CAP]+[v for v in prior if v!=resource.RLIM_INFINITY])
    assert effective>0
    resource.setrlimit(resource.RLIMIT_DATA,(effective,effective))
    actual=resource.getrlimit(resource.RLIMIT_DATA)
    assert actual==(effective,effective)
    print(json.dumps({'event':'true_M14_per_process_data_resource_budget','requested_bytes':CAP,'effective_limits':actual,'prior_limits':prior,'original_Node_heap_MiB':1536,'numerical_inputs_unchanged':True,'scope':'Per process only, including inherited Node limit; not aggregate memory or a proof that 6500 nodes fit.'}),flush=True)
    spec=importlib.util.spec_from_file_location('original_true_M14_space_guard',path)
    guard=importlib.util.module_from_spec(spec);spec.loader.exec_module(guard);guard.main()

if __name__=='__main__':main()
