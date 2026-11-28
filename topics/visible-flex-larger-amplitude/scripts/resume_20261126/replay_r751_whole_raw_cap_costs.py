#!/usr/bin/env python3
"""Whole original R751 command replay; read its exact raw from disk in original order."""
import argparse
from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import sys
import numpy as np
import measure_r751_closed_mixed_atlas as original
import forensic_r751_original_caps as audit
import r751_curvature_mixed_closed_two_jets as m


def words(a):
    return sha256(np.asarray(a,dtype="<f8").tobytes()).hexdigest()


def replay(raw,record):
    rows=[];offset=0;nchecked=0
    data=np.memmap(raw,dtype="<f8",mode="r")
    for count,trans,order in ((48,12,16),(96,24,24),(192,48,32)):
        period,knots,m0,m1,top=m.offsets(order)
        ss=np.unique(np.r_[np.arange(count)*period/count,knots[:-1],
                    top+np.array([-m.BOOST_WIDTH,-m.PLATEAU,-m.PLATEAU/2,0.,m.PLATEAU,m.BOOST_WIDTH])])
        capv=np.unique(np.r_[np.linspace(1/trans,1,trans),1-np.array([0.,m.CAP_STRAIGHT,m.CAP_TURN,m.CAP_TURN+m.FLATTEN])])
        base={}
        for phase in (0.,.4,.8,.9,1.,1.2,np.pi/2):
            row=next(x for x in record["rows"] if x["grid"]==[count,trans] and x["phase"]==phase)
            for name,n1,n2 in (("cylinder",len(ss),trans+1),("end+",len(ss),trans+1),
                    ("end-",len(ss),trans+1),("cap+",len(ss),len(capv)),("cap-",len(ss),len(capv)),
                    ("cap-normal+",len(ss),trans+1),("cap-normal-",len(ss),trans+1),
                    ("cap-cartesian+",1,1),("cap-cartesian-",1,1),
                    ("exact/end+",17,trans+1),("exact/cap-normal+",17,trans+1),
                    ("exact/end-",17,trans+1),("exact/cap-normal-",17,trans+1)):
                first=offset
                offset+=n1*n2*18
                j=np.asarray(data[first:offset]).reshape(n1,n2,6,3)
                if phase==0.:
                    base[name]=j
                if name not in ("cap+","cap-"):
                    continue
                measured=original.measure(j,base[name])
                nchecked+=1
                su,ve=np.meshgrid(ss,capv,indexing="ij")
                independent=audit.working(j)
                k=np.unravel_index(np.argmax(independent),independent.shape)
                # Literally form the original Boolean-indexed expression and keep its argmax.
                g,b=original.forms(j);g0,_=original.forms(base[name])
                det=lambda a:a[...,0]*a[...,2]-a[...,1]**2
                d0,d=det(g0),det(g)
                valid=(d0>0)&(d>0)&np.isfinite(d)&np.isfinite(d0)
                gf,bf,df=g[valid],b[valid],d[valid]
                tr=(gf[...,2]*bf[...,0]-2*gf[...,1]*bf[...,1]+gf[...,0]*bf[...,2])/df
                old_values=(np.abs(tr)+np.sqrt(np.maximum(0.,tr*tr-4*det(bf)/df)))/2
                oldflat=np.flatnonzero(valid.ravel())[np.argmax(old_values)]
                ko=np.unravel_index(oldflat,valid.shape)
                # Pull the pre-rotation coordinates directly from the original raw.
                pre=j.copy()
                ox,oz=m.axial.axis(order)
                dx=j[...,0].copy();dz=j[...,2].copy()
                dx[...,0]-=ox;dz[...,0]-=oz
                co,si=np.cos(phase),np.sin(phase)
                pre[...,0]=co*dx+si*dz;pre[...,2]=-si*dx+co*dz
                pre[...,0,0]+=ox;pre[...,0,2]+=oz
                cc,f,se=audit.cartesian(pre,ve,phase,1 if name=="cap+" else -1)
                whole=m.chart_jet(name,su,ve,phase,order)
                rowdata={"level":[count,trans,order],"phase":float(phase),"chart":name,
                    "raw_offset_bytes":first*8,"raw_absolute_bytes":(offset-first)*8,
                    "raw_cap_sha":words(j),"fresh_independent_source_cap_sha":words(whole),
                    "raw_vs_fresh_max":float(np.max(np.abs(j-whole))),
                    "original_replay_report":row["charts"][name],"original_measure_on_disk":measured,
                    "unflattened_peak":float(independent[k]),"literal_flattened_peak":float(np.max(old_values)),
                    "same_peak_index":bool(k==ko),"original_raw_peak":[float(su[ko]),float(ve[ko])],
                    "unflattened_index":[int(a) for a in k],"literal_flattened_index":[int(a) for a in ko],
                    "cartesian_at_literal_peak":float(cc[ko]) if 1-ve[ko]>=m.CAP_TURN-5e-16 else None}
                if count==192 and phase==np.pi/2:
                    tang=j[ko][1:3].T;normal=np.cross(tang[:,0],tang[:,1]);normal/=np.linalg.norm(normal)
                    _,sig,vt=np.linalg.svd(tang,full_matrices=False)
                    ii=np.array([[normal@j[ko][3],normal@j[ko][4]],[normal@j[ko][4],normal@j[ko][5]]])
                    rowdata.update({"world_six_jet_at_original_raw_peak":j[ko].tolist(),
                         "normal":normal.tolist(),"tangent_sigmas":sig.tolist(),
                         "svd_k":np.linalg.eigvalsh(vt@ii@vt.T/(sig[:,None]*sig[None,:])).tolist(),
                         "first_graph_chain":f[ko].tolist(),"second_graph_chain":se[ko].tolist()})
                rows.append(rowdata)
    if offset!=data.size:
        raise ValueError("raw byte walk did not cover whole unmodified output")
    return rows,nchecked


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--report",type=Path,required=True)
    a=p.parse_args()
    m.old.disk._public()
    temp=Path(os.environ["RUNNER_TEMP"])
    report=temp/"unchanged-r751-replay-report.json";raw=temp/"unchanged-r751-replay.raw"
    subprocess.run([sys.executable,"-u",str(Path(original.__file__).resolve()),"--report",str(report),
                    "--raw",str(raw)],check=True)
    rec=json.loads(report.read_bytes())
    rows,n=replay(raw,rec)
    old_sha="69bca3cab9ff1cc12c47c20aca55d7526aeeb3979e3016554244c3565c80cefc"
    result={"schema":"R751-original-unaltered-entry-whole-byte-replay-v1","run":os.environ["GITHUB_RUN_ID"],
        "attempt":os.environ["GITHUB_RUN_ATTEMPT"],"rules_read_commit":os.environ["R751_RULES_COMMIT"],
        "source_commit":rec["source_commit"],"trigger_commit":os.environ["GITHUB_SHA"],
        "original_recorded_whole":old_sha,"original_run":"46150384106","independent_audit":"46151602924",
        "new_whole_raw":rec["whole_raw"],"same_whole_raw":rec["whole_raw"]["sha256"]==old_sha,
        "unchanged_replay_report_sha256":sha256(report.read_bytes()).hexdigest(),"full_original_cap_blocks":n,
        "all_original_cap_blocks":rows,"numpy":np.__version__}
    words_out=(json.dumps(result,sort_keys=True,separators=(",",":"))+"\n").encode()
    a.report.parent.mkdir(parents=True,exist_ok=True);a.report.write_bytes(words_out)
    print("R751 original byte replay",len(words_out),flush=True)


if __name__=="__main__":
    main()
