#!/usr/bin/env python3
"""Trace change/g identity on the real R751 fine cap and its contiguous original rows."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import sys
import numpy as np
import measure_r751_closed_mixed_atlas as original
import r751_curvature_mixed_closed_two_jets as m


OP=next(q for q in original.measure.__code__.co_consts if getattr(q,"co_name",None)=="op")
word=lambda a:hashlib.sha256(np.ascontiguousarray(a).tobytes()).hexdigest()


def record(sample,base):
    g,b=original.forms(sample);g0,_=original.forms(base)
    diff=np.empty_like(g);np.subtract(g,g0,out=diff)
    plain=original.measure(sample,base)
    observed=[]
    def enter(frame,event,arg):
        if event=="call" and frame.f_code is OP:
            inner=frame.f_locals;outer=frame.f_back.f_locals
            x=outer["g"];change=outer["change"]
            observed.append({"outer_g_is_change":x is change,
                "shares_memory":bool(np.shares_memory(x,change)),
                "g_equals_explicit_difference":bool(np.array_equal(x,diff)),
                "g_equals_unchanged_gram":bool(np.array_equal(x,g)),
                "change_equals_explicit_difference":bool(np.array_equal(change,diff)),
                "outer_g0_equals_unchanged":bool(np.array_equal(outer["g0"],g0)),
                "inner_mat_is_outer_g":inner["mat"] is x,
                "outer_hashes_g_change_inner_mat":[word(q) for q in (x,change,inner["mat"])]})
        return None
    sys.settrace(enter)
    try:
        traced=original.measure(sample,base)
    finally:
        sys.settrace(None)
    return {"original_rows":len(sample),"masked_gram_bytes":int(g.nbytes),
            "plain":plain,"traced":traced,"first_relative_and_second_curvature_op":observed,
            "actual_sixjets_sha256":word(sample),"reference_sixjets_sha256":word(base),
            "independent_gram_reference_difference_sha256":[word(q) for q in (g,g0,diff)]}


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument("--report",required=True,type=Path)
    out=ap.parse_args().report;m.old.disk._public()
    count,trans,order=192,48,32
    period,knots,m0,m1,top=m.offsets(order)
    s=np.unique(np.r_[np.arange(count)*period/count,knots[:-1],
        top+np.array([-m.BOOST_WIDTH,-m.PLATEAU,-m.PLATEAU/2,0.,m.PLATEAU,m.BOOST_WIDTH])])
    v=np.unique(np.r_[np.linspace(1/trans,1,trans),1-np.array([0.,m.CAP_STRAIGHT,m.CAP_TURN,m.CAP_TURN+m.FLATTEN])])
    su,vv=np.meshgrid(s,v,indexing="ij");j=m.chart_jet("cap+",su,vv,np.pi/2,order)
    j0=m.chart_jet("cap+",su,vv,0.,order)
    j,j0=j.reshape(-1,6,3),j0.reshape(-1,6,3)
    rows=[record(j[:n],j0[:n]) for n in (10922,10923,len(j))]
    report={"schema":"R751-real-fine-upper-cap-gram-change-identity-v1",
        "run":os.environ["GITHUB_RUN_ID"],"attempt":os.environ["GITHUB_RUN_ATTEMPT"],
        "rules_read_commit":os.environ["R751_RULES_COMMIT"],"trigger_commit":os.environ["GITHUB_SHA"],
        "python":platform.python_version(),"numpy":np.__version__,
        "whole_source_sha256":{Path(f).name:hashlib.sha256(Path(f).read_bytes()).hexdigest()
                               for f in (__file__,m.__file__,original.__file__)},
        "rows":rows,"unmodified_original_complete_trace":"46154833248",
        "upstream_sources":{"numpy_v2.2.6_temp_elide.c_gitblob":"662a2fa52b06d32e7160f69d0eb7a674a4183351",
                            "numpy_v2.2.6_number.c_gitblob":"e6c04c1c9a9c158237888569d0411d8695d87900",
                            "cpython_temporary_reference_change":"https://github.com/python/cpython/issues/133164"}}
    out.write_text(json.dumps(report,separators=(",",":"),sort_keys=True)+"\n")


if __name__=="__main__":
    main()
