#!/usr/bin/env python3
"""Follow completed g0 leaves with same-reference actual parameter densities.

Expanded-domain proof children finish before each density child is started.
The existing v5 proof cache and every actual analytic/DFT gate are unchanged.
Each child process is isolated to release its native interval/FFT arrays.
The index contains full source identities, signed first integrals and retained
local J2 via the immutable leaf reports. Final chronological accumulation and
the endpoint/KAM processor are separate; no missing prefix is called complete.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import hashlib
import json
import gzip
import os
from pathlib import Path
import subprocess
import sys
import time
from flint import arb,ctx

from fourfold_saved_circle_field_multidomain_budget import read
from fourfold_phase_beta_affine import sha
from fourfold_phase_beta_interval import ball_record
from fourfold_forward_density_pipeline_Q1024_v3 import save,upper
from fourfold_phase_domain_cover_verify import Time


def key_from_identity(identity):
    ref=identity["reference"]
    return (int(ref["segment"]),*map(Fraction,ref["normalized_subspan"]))


def source_for(report,g0_index):
    sources={digest:Path(path) for path,digest in g0_index["pipeline_sources"].items()}
    wanted=report["source_sha256"]
    if wanted not in sources or sha(sources[wanted])!=wanted:
        raise ValueError("the actual g0 source bytes are absent or changed")
    return sources[wanted]


def validate_parameter_report(path,g0_path,args,expected_key):
    report,g0=read(path),read(g0_path)
    if not(report.get("complete") and report.get("complete_continuous_parameter_densities_proved")):
        raise ValueError("only complete actual parameter densities may enter the cover")
    source=args.source_versions.get(report["source_sha256"])
    if source is None or sha(source)!=report["source_sha256"]:
        raise ValueError("the completed parameter source version is absent or changed")
    if report["reference_certificate_sha256"]!=sha(g0_path):
        raise ValueError("parameter input uses another completed g0 leaf")
    if (key_from_identity(report["identity"])!=expected_key
        or report["identity"]["reference"]!=g0["identity"]["reference"]
        or report["identity"]["reference"]["retarget_descriptor_sha256"]!=sha(args.descriptor)):
        raise ValueError("actual parameter/finite-reference identity mismatch")
    uniform=bool(args.uniform_half_width)
    if report["identity"]["whole_real_parameter_tube"]!=uniform:
        raise ValueError("central and uniform parameter scopes cannot be mixed")
    if uniform and Fraction(report["identity"]["actual_parameter_source"]["exact_parameter_half_width"])!=args.uniform_half_width:
        raise ValueError("the saved real parameter half-width differs")
    if (Fraction(report["label_strip"])!=Fraction(args.label_strip)
        or Fraction(report["inner_strip"])!=Fraction(args.inner_strip)
        or Fraction(report["spatial_derivative_strip"])!=args.spatial_strip):
        raise ValueError("saved parameter strip scopes differ")
    available={item["parameter_order"]:item for item in report["density"]}
    required=[2] if uniform else [1,2]
    if any(j not in available for j in required):
        raise ValueError("a required actual parameter source is absent")
    for j in required:
        if not available[j].get("complete_spatial_jet_inputs",{}).get("proved"):
            raise ValueError("actual spatial jet fees are missing")
    local=report["R82_local_inputs"]
    if uniform:
        if local["first_coefficients"][2] is None or local["remaining_local_J0_J1_J2_fees"][2] is None:
            raise ValueError("uniform g2 first or full g0/g2 local fee is absent")
    elif not local.get("retained_local_second_coefficients"):
        raise ValueError("the full center local 2J11 is absent")
    return report,g0


def main():
    p=argparse.ArgumentParser(description=__doc__);base=Path("data/phase_ring_continuation")
    p.add_argument("--descriptor",type=Path,default=base/"step5_retargeted_reference/descriptor.json")
    p.add_argument("--g0-index",type=Path,default=base/"step5_forward_density_complete/index.json")
    p.add_argument("--pipeline",type=Path,default=Path(__file__).with_name("fourfold_parameter_density_pipeline_efficient_v5.py"))
    p.add_argument("--out-directory",type=Path,default=base/"step5_parameter_density_forward")
    p.add_argument("--expanded-domain-directory",type=Path,default=base/"step5_expanded_time_domain_full")
    p.add_argument("--parameter-proof-directory",type=Path,default=base/"step5_expanded_parameter_time_domain_full")
    p.add_argument("--parameter-proof-lock-directory",type=Path,default=Path("/tmp/visible-flex-parameter-domain-locks"))
    p.add_argument("--precomputation-directory",type=Path,default=base/"step5_parameter_precomputations")
    p.add_argument("--expanded-proof-nodes",type=int,default=512)
    p.add_argument("--expanded-proof-bits",type=int,default=320)
    p.add_argument("--expanded-proof-half-width",type=Fraction,default=Fraction(1,10**9))
    p.add_argument("--log-directory",type=Path,default=Path("/workspace/scratch/f6a2c7886477/parameter-density-logs"))
    p.add_argument("--seed",type=Path,action="append",default=[])
    p.add_argument("--uniform-half-width",type=Fraction,default=Fraction(0))
    p.add_argument("--target",default="1e-9")
    p.add_argument("--label-strip",default="1/256");p.add_argument("--inner-strip",default="3/1024")
    p.add_argument("--spatial-strip",type=Fraction,default=Fraction(7,2048))
    p.add_argument("--primitive-nodes",type=int,default=512);p.add_argument("--root-nodes",type=int,default=1024)
    p.add_argument("--bits",type=int,default=256);p.add_argument("--coefficient-bits",type=int,default=160)
    p.add_argument("--outer",type=Fraction,default=Fraction(3))
    p.add_argument("--follow",action="store_true");p.add_argument("--wait-seconds",type=float,default=15)
    p.add_argument("--stop-segment",type=int,default=550);p.add_argument("--stop-file",type=Path)
    args=p.parse_args()
    if not 0<args.stop_segment<=550 or not 0<args.wait_seconds<=60:
        raise ValueError("invalid cover endpoint or wait interval")
    if args.uniform_half_width<0:
        raise ValueError("parameter half-width must be nonnegative")
    ctx.prec=args.bits
    descriptor=read(args.descriptor);meta=descriptor["old_forward_reference"]
    if sha(meta["path"])!=meta["sha256"]:
        raise ValueError("the complete forward time grid changed")
    grid=read(meta["path"])
    if grid["segment_count"]!=550:
        raise ValueError("this cover expects the complete 550-segment reference")
    args.out_directory.mkdir(parents=True,exist_ok=True)
    args.log_directory.mkdir(parents=True,exist_ok=True)
    args.precomputation_directory.mkdir(parents=True,exist_ok=True)
    precompute_source=Path(__file__).with_name("fourfold_parameter_precompute_expanded_domain.py")
    suffix="uniform" if args.uniform_half_width else "center"
    index_path=args.out_directory/("index_"+suffix+".json")
    previous=read(index_path) if index_path.exists() else None
    if previous and (previous["descriptor_sha256"]!=sha(args.descriptor)
                     or Fraction(previous["uniform_parameter_half_width"])!=args.uniform_half_width):
        raise ValueError("refuse to replace a different parameter cover")
    versions=dict(previous.get("pipeline_sources",{})) if previous else {}
    if previous:
        versions[previous["pipeline_path"]]=previous["pipeline_sha256"]
    versions[str(args.pipeline)]=sha(args.pipeline)
    for name in ("fourfold_parameter_density_pipeline_l2_v2.py",
                 "fourfold_parameter_density_pipeline_l2_v3.py"):
        path=Path(__file__).with_name(name)
        versions[str(path)]=sha(path)
    args.source_versions={}
    for name,digest in versions.items():
        if sha(name)!=digest:raise ValueError("a retained pipeline version changed")
        args.source_versions[digest]=Path(name)
    old={(row["segment"],*map(Fraction,row["normalized_subspan"])):row for row in previous["leaves"]} if previous else {}
    seeds={}
    for path in args.seed:
        doc=read(path)
        if not doc.get("complete"):
            raise ValueError("a seed parameter leaf is still running")
        seeds[key_from_identity(doc["identity"])]=path
    index=dict(kind="actual_complete_forward_parameter_density_inputs",complete=False,
        source_sha256=sha(__file__),pipeline_path=str(args.pipeline),pipeline_sha256=sha(args.pipeline),
        descriptor_sha256=sha(args.descriptor),g0_index_path=str(args.g0_index),
        pipeline_sources=versions,required_parameter_orders=[2] if args.uniform_half_width else [1,2],
        exact_target_delta_fraction=descriptor["target_exact_delta_fraction"]
            if "target_exact_delta_fraction" in descriptor else None,
        uniform_parameter_half_width=str(args.uniform_half_width),
        whole_real_parameter_tube=bool(args.uniform_half_width),
        label_strip=args.label_strip,inner_strip=args.inner_strip,spatial_strip=str(args.spatial_strip),
        completed_segments=0,leaves=[],input_g0_snapshots=[],whole_forward_leg=False,
        independent_precompute_source_sha256=sha(precompute_source),precomputation_runs=[])
    keys=("B2","E2","localJ2_g0_g2") if args.uniform_half_width else ("A","E0","B1","B2","E1","E2","localJ0","localJ1","localJ2")
    totals={key:arb(0)for key in keys}
    required=[2] if args.uniform_half_width else [1,2]
    spatial={j:[arb(0)for _ in range(3)]for j in required}
    start=time.monotonic();last=Time(Fraction(0),Fraction(-1,2))
    env=dict(os.environ,PYTHONDONTWRITEBYTECODE="1",OPENBLAS_NUM_THREADS="1",OMP_NUM_THREADS="1")
    for segment in range(args.stop_segment):
        while True:
            g0_raw=args.g0_index.read_bytes()
            g0_index=json.loads(gzip.decompress(g0_raw) if args.g0_index.suffix=='.gz' else g0_raw)
            if g0_index["descriptor_sha256"]!=sha(args.descriptor):
                raise ValueError("g0 index changed to a different reference")
            entries=[row for row in g0_index["leaves"]if row["segment"]==segment]
            if g0_index["completed_segments"]>segment:
                break
            index["waiting_for_g0_segment"]=segment;save(index_path,index)
            if not args.follow:
                return
            if args.stop_file and args.stop_file.exists():
                return
            time.sleep(args.wait_seconds)
        index.pop("waiting_for_g0_segment",None)
        snapshot=dict(path=str(args.g0_index),sha256=hashlib.sha256(g0_raw).hexdigest(),
                      completed_segments=g0_index["completed_segments"])
        if not index["input_g0_snapshots"] or index["input_g0_snapshots"][-1]!=snapshot:
            index["input_g0_snapshots"].append(snapshot)
        entries.sort(key=lambda row:Fraction(row["normalized_subspan"][0]))
        spans=[tuple(map(Fraction,row["normalized_subspan"]))for row in entries]
        if not spans or spans[0][0]!=0 or spans[-1][1]!=1 or any(a[1]!=b[0]for a,b in zip(spans,spans[1:])):
            raise ValueError("the completed zero-order segment has a time gap")
        for entry,(left,right) in zip(entries,spans):
            key=(segment,left,right);g0_path=Path(entry["path"])
            if sha(g0_path)!=entry["sha256"]:
                raise ValueError("completed g0 report bytes changed")
            g0=read(g0_path);source=source_for(g0,g0_index)
            label=hashlib.sha256((str(left)+":"+str(right)).encode()).hexdigest()[:10]
            stem="forward_%04d_%s_%s"%(segment,label,suffix)
            path=args.out_directory/(stem+".json.gz")
            if key in old:
                path=Path(old[key]["path"])
                if sha(path)!=old[key]["sha256"]:
                    raise ValueError("saved parameter leaf bytes changed")
            elif key in seeds:
                path=seeds[key]
            elif not(path.exists()and read(path).get("complete")):
                if args.stop_file and args.stop_file.exists():
                    index["paused_between_leaves"]=True;save(index_path,index);return
                domain=entry.get("current_field_cover_domain",g0["domain_path"])
                proof_arguments=["--descriptor",str(args.descriptor),"--domain",str(domain),
                    "--uniform-half-width",str(args.uniform_half_width),"--root-nodes",str(args.root_nodes),
                    "--expanded-domain-directory",str(args.expanded_domain_directory),
                    "--parameter-proof-directory",str(args.parameter_proof_directory),
                    "--parameter-proof-lock-directory",str(args.parameter_proof_lock_directory),
                    "--expanded-proof-nodes",str(args.expanded_proof_nodes),
                    "--expanded-proof-bits",str(args.expanded_proof_bits),
                    "--expanded-proof-half-width",str(args.expanded_proof_half_width)]
                prep_path=args.precomputation_directory/(stem+".json.gz")
                prep_log=args.log_directory/(stem+"_precompute.log")
                prep_command=[sys.executable,"-u",str(precompute_source),*proof_arguments,
                              "--log-directory",str(args.log_directory),"--out",str(prep_path)]
                print(dict(stage="parameter_proof_separate_process_start",segment=segment,scope=suffix),flush=True)
                with prep_log.open("w") as output:
                    prepared=subprocess.run(prep_command,stdout=output,stderr=subprocess.STDOUT,env=env)
                if prepared.returncode:
                    index["failed_precomputation"]=dict(segment=segment,normalized_subspan=list(map(str,(left,right))),
                        report_path=str(prep_path),log_path=str(prep_log),returncode=prepared.returncode,command=prep_command)
                    save(index_path,index)
                    raise RuntimeError("separate parameter proof process failed; saved report/log: "+str(prep_path))
                prep=read(prep_path)
                if not prep.get("complete") or not prep.get("all_requested_child_processes_finished"):
                    raise ValueError("parameter proof precomputation did not finish")
                index["precomputation_runs"].append(dict(path=str(prep_path),sha256=sha(prep_path),
                    segment=segment,normalized_subspan=list(map(str,(left,right)))))
                command=[sys.executable,"-u",str(args.pipeline),"--descriptor",str(args.descriptor),
                    "--domain",domain,"--reference-certificate",str(g0_path),
                    "--reference-source",str(source),"--uniform-half-width",str(args.uniform_half_width),
                    "--target",args.target,"--label-strip",args.label_strip,
                    "--inner-strip",args.inner_strip,"--spatial-strip",str(args.spatial_strip),
                    "--primitive-nodes",str(args.primitive_nodes),"--root-nodes",str(args.root_nodes),
                    "--bits",str(args.bits),"--coefficient-bits",str(args.coefficient_bits),
                    "--outer",str(args.outer),"--directory",str(args.out_directory/stem),"--out",str(path)]
                command.extend(["--expanded-domain-directory",str(args.expanded_domain_directory),
                    "--parameter-proof-directory",str(args.parameter_proof_directory),
                    "--parameter-proof-lock-directory",str(args.parameter_proof_lock_directory),
                    "--expanded-proof-nodes",str(args.expanded_proof_nodes),
                    "--expanded-proof-bits",str(args.expanded_proof_bits),
                    "--expanded-proof-half-width",str(args.expanded_proof_half_width)])
                if args.uniform_half_width:command.append("--second-only")
                log=args.log_directory/(stem+".log")
                print(dict(stage="actual_parameter_leaf_start",segment=segment,scope=suffix,log=str(log)),flush=True)
                with log.open("w") as output:
                    result=subprocess.run(command,stdout=output,stderr=subprocess.STDOUT,env=env)
                if result.returncode:
                    index["failed_leaf"]=dict(segment=segment,normalized_subspan=list(map(str,(left,right))),
                        report_path=str(path),log_path=str(log),returncode=result.returncode,command=command)
                    save(index_path,index)
                    raise RuntimeError("actual parameter leaf failed; saved report/log: "+str(path))
            report,g0=validate_parameter_report(path,g0_path,args,key)
            a,b=map(Time.parse,grid["exact_time_endpoints"][segment:segment+2])
            ta,tb=a+(b-a).scale(left),a+(b-a).scale(right)
            if ta!=last:
                raise ValueError("actual parameter source chronology has a gap")
            last=tb
            data=report["R82_local_inputs"]
            available={item["parameter_order"]:item for item in report["density"]}
            if not args.uniform_half_width:
                totals["A"]+=upper(g0["R72_inputs"]["common_integrated_majorant_A"])
                totals["E0"]+=upper(g0["R72_inputs"]["integrated_approximation_error_E"])
            for j in required:
                item=available[j]
                totals["B"+str(j)]+=upper(item["true_integrated_modulus"])
                totals["E"+str(j)]+=upper(item["true_integrated_error"])
                for d,v in enumerate(item["complete_spatial_jet_inputs"]["true_integrated_spatial_derivative_SUP_moduli"]):
                    spatial[j][d]+=upper(v)
            if args.uniform_half_width:
                totals["localJ2_g0_g2"]+=upper(data["remaining_local_J0_J1_J2_fees"][2])
            else:
                for j,v in enumerate(data["remaining_local_J0_J1_J2_fees"]):
                    totals["localJ"+str(j)]+=upper(v)
            index["leaves"].append(dict(path=str(path),sha256=sha(path),bytes=path.stat().st_size,
                segment=segment,normalized_subspan=list(map(str,(left,right))),
                g0_report_path=str(g0_path),g0_report_sha256=sha(g0_path)))
            index["integrated_scalar_summary"]={key:ball_record(v.upper())for key,v in totals.items()}
            index["integrated_spatial_SUP_moduli_by_parameter_order"]={str(j):list(map(ball_record,spatial[j]))for j in required}
            if args.uniform_half_width:
                index["g0_g1_uniform_control_requires_hybrid_center_mean_value_transfer"]=True
            else:
                index["integrated_parameter_spatial_SUP_moduli"]=[list(map(ball_record,spatial[j]))for j in required]
            index["exact_final_time"]=dict(rational=str(last.q),pi_coefficient=str(last.p))
            index["completed_segments"]=segment+int(right==1)
            index["wall_seconds_this_process"]=time.monotonic()-start
            save(index_path,index)
            print(dict(stage="actual_parameter_leaf_complete",segment=segment,scope=suffix,
                sha256=sha(path),B1=str(totals["B1"]) if "B1" in totals else None,B2=str(totals["B2"])),flush=True)
    index["whole_forward_leg"]=args.stop_segment==550 and last==Time(Fraction(0),Fraction(1,2))
    index["complete"]=index["whole_forward_leg"]
    index["requested_prefix_finished"]=True;save(index_path,index)
    print(dict(complete=index["complete"],completed_segments=index["completed_segments"],
               index_path=str(index_path),sha256=sha(index_path)),flush=True)


if __name__=="__main__":
    main()


