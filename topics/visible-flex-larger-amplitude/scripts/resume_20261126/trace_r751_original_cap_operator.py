#!/usr/bin/env python3
"""Capture the original R751 op arguments and actual return vectors on every full cap."""
import argparse
import dis
from hashlib import sha256
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
import numpy as np
import forensic_r751_original_caps as audit
import measure_r751_closed_mixed_atlas as original
import r751_curvature_mixed_closed_two_jets as m


PREVIOUS="r751-actual-curvature-mixed-atlas-46153716771-1.json"
EXPECTED="4cb33726d3462f9ad1144827bcbd22ba983284f2b7562c72bd4769daa61f8d12"
OP=next(c for c in original.measure.__code__.co_consts if getattr(c,"co_name",None)=="op")


def word(a):
    return sha256(np.ascontiguousarray(a).tobytes()).hexdigest()


def capture(j,j0):
    caught=[]
    def local(frame,event,result):
        if event=="return":
            f=frame.f_locals
            caught.append((f["z"],f["mat"],f["den"],f["tr"],f["disc"],result))
        return local
    def entry(frame,event,arg):
        if event=="call" and frame.f_code is OP:
            frame.f_trace_lines=False
            return local
        return None
    sys.settrace(entry)
    try:
        ret=original.measure(j,j0)
    finally:
        sys.settrace(None)
    if len(caught)!=2:
        raise ValueError("expected metric and curvature op returns")
    return ret,caught


def explicit(b,g,d):
    det=b[...,0]*b[...,2]-b[...,1]**2
    tr=(g[...,2]*b[...,0]-2*g[...,1]*b[...,1]+g[...,0]*b[...,2])/d
    disc=np.maximum(0.,tr*tr-4*det/d)
    return tr,disc,(np.abs(tr)+np.sqrt(disc))/2


def note(file):
    return [len(file.read_bytes()),sha256(file.read_bytes()).hexdigest()]


def run():
    cp=argparse.ArgumentParser(description=__doc__)
    cp.add_argument("--report",type=Path,required=True)
    out=cp.parse_args().report
    m.old.disk._public()
    prior=Path(os.environ["GITHUB_WORKSPACE"])/"topics/visible-flex-larger-amplitude/notes"/PREVIOUS
    if note(prior)[1]!=EXPECTED:
        raise ValueError("different prior complete report")
    ledger=json.loads(prior.read_bytes())["all_original_cap_blocks"]
    temp=Path(os.environ["RUNNER_TEMP"])
    full=temp/"trace-original-R751.raw";summary=temp/"trace-original-R751.json"
    subprocess.run([sys.executable,"-u",original.__file__,"--raw",str(full),"--report",str(summary)],check=True)
    orig=json.loads(summary.read_bytes())
    buf=np.memmap(full,mode="r",dtype="<f8");base={};rows=[]
    for rec in ledger:
        count,trans,order=rec["level"];sides=rec["chart"];ph=rec["phase"]
        period,knots,m0,m1,top=m.offsets(order)
        su=np.unique(np.r_[np.arange(count)*period/count,knots[:-1],
                    top+np.array([-m.BOOST_WIDTH,-m.PLATEAU,-m.PLATEAU/2,0.,m.PLATEAU,m.BOOST_WIDTH])])
        ve=np.unique(np.r_[np.linspace(1/trans,1,trans),1-np.array([0.,m.CAP_STRAIGHT,m.CAP_TURN,m.CAP_TURN+m.FLATTEN])])
        i=rec["raw_offset_bytes"]//8;n=rec["raw_absolute_bytes"]//8
        j=np.asarray(buf[i:i+n]).reshape(len(su),len(ve),6,3)
        if ph==0.:
            base[(count,sides)]=j
        j0=base[count,sides]
        plain=original.measure(j,j0)
        ret,caught=capture(j,j0)
        b,g,d,tr,disc,returned=caught[1]
        gb,bb=original.forms(j);g0,_=original.forms(j0)
        det=lambda a:a[...,0]*a[...,2]-a[...,1]**2
        db=det(gb);d0=det(g0)
        mask=(db>0)&(d0>0)&np.isfinite(db)&np.isfinite(d0)
        separate=(bb[mask],gb[mask],db[mask])
        trc,dc,vc=explicit(b,g,d)
        trs,ds,vs=explicit(*separate)
        maxidx=int(np.argmax(returned));ii=np.unravel_index(np.flatnonzero(mask.ravel())[maxidx],mask.shape)
        row={"level":rec["level"],"chart":sides,"phase":ph,"raw_same_as_replay":word(j)==rec["raw_cap_sha"],
             "plain":plain,"traced":ret,"actual_op_max":[float(np.max(caught[0][-1])),float(np.max(returned))],
             "recompute_captured_vs_separate_max":[float(np.max(vc)),float(np.max(vs))],
             "peak_coordinates":[float(su[ii[0]]),float(ve[ii[1]])],"peak_integer_index":[int(x) for x in ii],
             "op_hash_order_b_g_d_tr_disc_vector":[word(x) for x in caught[1]],
             "captured_equal_separate_b_g_d":[np.array_equal(x,y) for x,y in zip(caught[1][:3],separate)],
             "op_equal_captured_tr_disc_vec":[np.array_equal(x,y) for x,y in zip(caught[1][3:],(trc,dc,vc))],
             "captured_equal_separate_tr_disc_vec":[np.array_equal(x,y) for x,y in zip((trc,dc,vc),(trs,ds,vs))]}
        if count==192 and ph>0.:
            jj=j[ii];tan=jj[1:3].T
            cross=np.cross(tan[:,0],tan[:,1]);normal=cross/np.linalg.norm(cross)
            _,sv,vt=np.linalg.svd(tan,full_matrices=False)
            ii2=np.array([[normal@jj[3],normal@jj[4]],[normal@jj[4],normal@jj[5]]])
            pre=jj.copy();ox,oz=m.axial.axis(order)
            xx=pre[:,0].copy();zz=pre[:,2].copy();xx[0]-=ox;zz[0]-=oz
            co,si=np.cos(ph),np.sin(ph)
            pre[:,0]=co*xx+si*zz;pre[:,2]=-si*xx+co*zz;pre[0,0]+=ox;pre[0,2]+=oz
            cc,f,se=audit.cartesian(pre,np.asarray(ve[ii[1]]),ph,1 if sides=="cap+" else -1)
            row["peak_inputs"]={"original":[b[maxidx].tolist(),g[maxidx].tolist(),float(d[maxidx])],
                  "separate":[separate[0][maxidx].tolist(),separate[1][maxidx].tolist(),float(separate[2][maxidx])],
                  "tr_disc_value":[float(z[maxidx]) for z in (tr,disc,returned,trc,dc,vc,trs,ds,vs)],
                  "svd_principals":np.linalg.eigvalsh(vt@ii2@vt.T/(sv[:,None]*sv[None,:])).tolist(),
                  "cartesian_abs_principal":float(cc) if 1-ve[ii[1]]>=m.CAP_TURN-5e-16 else None,
                  "cartesian_first_chain":f.tolist(),"cartesian_second_chain":se.tolist(),
                  "world_six_jet":jj.tolist(),"tangent_singular_values":sv.tolist(),
                  "cross_product":cross.tolist(),"cross_area_squared":float(cross@cross),
                  "singular_gram_determinant":float((sv[0]*sv[1])**2),
                  "tangent_dot_gram":(tan.T@tan).tolist(),"tangent_condition":float(sv[0]/sv[1]),
                  "peak_sixjet_word_offset_mod64":int(jj.ctypes.data%64),
                  "arrays_b_g_d_mod64":[int(x.ctypes.data%64) for x in (b,g,d,*separate)]}
        rows.append(row)
    rep={"schema":"R751-actual-original-inner-op-capture-v1","run":os.environ["GITHUB_RUN_ID"],
         "attempt":os.environ["GITHUB_RUN_ATTEMPT"],"rules_read_commit":os.environ["R751_RULES_COMMIT"],
         "source_commit":orig["source_commit"],"trigger_commit":os.environ["GITHUB_SHA"],
         "sources":{Path(p).name:note(Path(p)) for p in (__file__,original.__file__,audit.__file__,m.__file__)},
         "previous":note(prior),"original_whole_raw":orig["whole_raw"],"python":platform.python_version(),
         "numpy":np.__version__,"bytecode_original_measure_and_op":[dis.Bytecode(original.measure).dis(),dis.Bytecode(OP).dis()],
         "rows":rows}
    out.write_text(json.dumps(rep,sort_keys=True,separators=(",",":"),allow_nan=False)+"\n")
    print("R751 original op capture complete",out.stat().st_size,flush=True)


if __name__=="__main__":
    run()
