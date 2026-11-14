#!/usr/bin/env python3
"""Consume the complete old R48 radial-to-centred drift on all eight parts.

Uses the original64 positive w dr bins and all1740 complete J leaves. A finite
positive-mass linear budget retains the common bin mass. No original integral,
candidate, root, ODE, physical worker or mathematical source is recomputed.
The output concerns a reference centre; it is not a true-surface error proof.

Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-13.
"""
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import resource
import sys
import time

EXPECTED = {
    "original_candidate": "7da554bdb467fe2b997a01971dd4917003fd5deeb36978e200e1457ea3c8fddf",
    "original_summary": "806fdb96b9aa6eafd921c07518a5b52218180d2182f7b8d18abb8e3d695638e4",
    "original_resource": "912ad6200027fdb445cd3e8636c1f6cd404a3480d2c013b6c4722e6888016820",
}
IO_SHA = "71b8e666c07e5e2a203dbde028ff8e0bb64a883551b0cd47d609773e88c848fe"
PROOF_SHA = "08f40aa33fe37055cf2f4870f9f4b7c05566f53e9e15e0de18171fe9880fa95f"
MODES = list(range(2,41,2))


def digest(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda:stream.read(1<<20),b""):
            h.update(block)
    return h.hexdigest()


def read(path):
    with (gzip.open(path,"rt",encoding="utf-8") if Path(path).suffix==".gz"
          else Path(path).open(encoding="utf-8")) as stream:
        return json.load(stream)


def record(q, upward=True, bits=128):
    q=Q(q)
    if q<0:
        raise ValueError("Only positive budget quantities are serialized here")
    if not q:
        return ["0",0]
    n,d=q.numerator,q.denominator
    e=n.bit_length()-d.bit_length()
    if (n<d*(1<<e) if e>=0 else n*(1<<-e)<d):
        e-=1
    unit=Q(2)**(e-bits+1)
    v=q/unit
    k=((v.numerator+v.denominator-1)//v.denominator if upward
       else v.numerator//v.denominator)
    out=k*unit
    if not (q<=out<=(1+Q(2)**(1-bits))*q if upward else 0<=out<=q):
        raise ArithmeticError("Directed output arithmetic failed")
    n,d=out.numerator,out.denominator
    if not n:
        return ["0",0]
    if d & (d-1):
        raise ArithmeticError("The output is not dyadic")
    e=-(d.bit_length()-1)
    while not n & 1:
        n//=2
        e+=1
    return [str(n),e]


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in EXPECTED:
        p.add_argument("--"+name.replace("_","-"),type=Path,required=True)
    p.add_argument("--original-primary-dir",type=Path,required=True)
    p.add_argument("--out-prefix",type=Path,required=True)
    p.add_argument("--io-helper",type=Path,
                   default=Path(__file__).with_name("tail_r103_local_carrier_centre_drift.py"))
    p.add_argument("--proof",type=Path,default=Path(__file__).resolve().parent.parent/
                   "notes/2026-11-13-tail-r103-all-original-bins-centre-drift.md")
    p.add_argument("--rss-limit-mib",type=int,default=40)
    a=p.parse_args()
    if hasattr(sys,"set_int_max_str_digits"):
        sys.set_int_max_str_digits(0)
    began=time.monotonic()
    summary_path=Path(str(a.out_prefix)+"-summary.json")
    primary_path=Path(str(a.out_prefix)+"-bins.jsonl.gz")
    if summary_path.exists() or primary_path.exists():
        raise FileExistsError("Use a fresh complete original-drift prefix")
    summary_path.parent.mkdir(parents=True,exist_ok=True)
    if digest(a.io_helper)!=IO_SHA or digest(a.proof)!=PROOF_SHA:
        raise ValueError("A complete mathematical helper or application proof changed")
    spec=importlib.util.spec_from_file_location("r103_original_drift_io",a.io_helper)
    io=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(io)

    def memory():
        rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        if rss>a.rss_limit_mib*1024:
            raise MemoryError("Owned all-original-bin consumer exceeded observed RSS")
        return rss

    def positive_sum(values):
        result=Q(0)
        for v in values:
            if v<0:
                raise ValueError("A positive budget term is negative")
            result=io.positive_upper(result+v)
        return result

    inputs={}
    for name,h in EXPECTED.items():
        path=getattr(a,name)
        if digest(path)!=h:
            raise ValueError("The frozen original input changed: "+name)
        inputs[name]=dict(path=str(path),sha256=h,bytes=path.stat().st_size)
    candidate,summary,usage=map(read,(a.original_candidate,a.original_summary,a.original_resource))
    io.assert_gates(candidate)
    io.assert_gates(summary)
    if (usage["exitcode"]!=0 or usage["termination_signal"] is not None
            or Path(usage["command"][usage["command"].index("--out")+1]).name!=a.original_summary.name):
        raise ValueError("The original complete audit has no matching formal exit0")
    if (candidate["cell"]!=0 or candidate["segment"]!=7
            or candidate["modes"]!=MODES or candidate["shooting_parts"]!=8
            or len(candidate["nodes"])!=9
            or summary["cell"]!=0 or summary["segment"]!=7
            or summary["modes"]!=MODES
            or [v["part"] for v in summary["parts"]]!=list(range(8))
            or sum(v["panels"] for v in summary["parts"])!=1740
            or EXPECTED["original_candidate"] not in summary["input_hashes"].values()):
        raise ValueError("This is not the complete frozen eight-part candidate")
    bins=sorted(candidate["bins"],key=lambda b:(b["part"],b["bin"]))
    if len(bins)!=64:
        raise ValueError("All64 original positive bins are required")
    groups={}
    at=Q(0)
    for part in range(8):
        rows=[b for b in bins if b["part"]==part]
        if [b["bin"] for b in rows]!=list(range(8)):
            raise ValueError("A part lacks the original8 bins")
        for b in rows:
            left,right=Q(b["left"]),Q(b["right"])
            if left!=at or not left<right<=1:
                raise ValueError("The original positive bins do not cover the segment")
            q00,q01=io.interval(b["values"]["00"]),io.interval(b["values"]["01"])
            # Both integrands are mathematically nonnegative. Their sum is the
            # same true full positive mass, not a new coordinate substitution.
            lo=max(Q(0),q00[0])+max(Q(0),q01[0])
            hi=q00[1]+q01[1]
            if hi<=0 or lo>hi:
                raise ValueError("A proved positive true mass has an empty enclosure")
            groups[(part,b["bin"])]=dict(part=part,bin=b["bin"],
                left=left,right=right,mass_lower=lo,mass_upper=hi,leaves=[])
            at=right
        if at!=Q(part+1,8):
            raise ValueError("A complete original part endpoint differs")
    if at!=1:
        raise ValueError("The complete source interval stopped early")

    sources=[]
    for part in summary["parts"]:
        path=a.original_primary_dir/Path(part["output"]).name
        if digest(path)!=part["output_sha256"]:
            raise ValueError("An original complete primary changed: "+str(path))
        sources.append(dict(part=part["part"],path=path,metadata=part,
                            sha256=part["output_sha256"],bytes=path.stat().st_size))
    # All eight complete hashes are checked before writing any new primary.
    total_count=0
    for source in sources:
        part,k=source["metadata"],source["part"]
        at,count,header,trailer=Q(part["left"]),0,False,False
        if at!=Q(k,8) or Q(part["right"])!=Q(k+1,8):
            raise ValueError("The full audit and positive bins disagree on part cover")
        with gzip.open(source["path"],"rt",encoding="utf-8") as stream:
            for line in stream:
                row=json.loads(line)
                if row["kind"]=="header":
                    if (header or trailer or count or row["part"]!=k
                            or row["input_hashes"]!=summary["input_hashes"]
                            or row["source_hashes"]!=summary["source_hashes"]
                            or row["complete_J_cosine_modes"]!=list(range(0,81,2))):
                        raise ValueError("A complete primary header changed")
                    header=True
                    continue
                if row["kind"]=="complete_substage_trailer":
                    if (not header or trailer or row["part"]!=k
                            or not row["complete_source_cover"] or row["accepted_panels"]!=count):
                        raise ValueError("A complete original trailer changed")
                    trailer=True
                    continue
                left,right=Q(row["source_left"]),Q(row["source_right"])
                if (not header or trailer or row["kind"]!="accepted_complete_R64_and_J_panel"
                        or not row["same_candidate_complete_mean"]
                        or not row["outside_saved_J_has_no_c_or_cx"]
                        or left!=at or not left<right<=Q(k+1,8)
                        or any(io.dyadic(v)<=0 for v in row["gates_lower"].values())):
                    raise ValueError("The full real-root/J continuous cover changed")
                group=groups[(k,row["bin"])]
                if not group["left"]<=left<right<=group["right"]:
                    raise ValueError("An original audit leaf escaped its producing positive bin")
                rlo,rhi=io.interval(row["source"]["radius"])
                wlo,whi=io.interval(row["source"]["w"])
                rxlo,rxhi=io.interval(row["source"]["radius_x"])
                if min(rlo,wlo,rxlo)<=0:
                    raise ValueError("The true positive source geometry is missing")
                bounds={key:io.dyadic(v) for key,v in row["bounds_upper"].items()}
                coeff=[io.abs_interval(v) for v in row["full_J_cosine_intervals"]]
                if len(coeff)!=41 or min(bounds.values())<0:
                    raise ValueError("All scalar and retained/outside J frequencies are required")
                d=min(Q(1),io.dyadic(row["gates_lower"]["real_D_lower"]))
                if d<=0:
                    raise ValueError("The complete actual real D margin is nonpositive")
                perp=sum(coeff[1:],Q(0))
                zero=min(coeff[0],Q(3,2)*(1+whi*whi)**2
                         *bounds["full_D_nonconstant_W1"]*perp/d**3)
                j=min(sum(coeff,Q(0)),bounds["complete_J_l1"],zero+perp)
                density=Q(22,7)**2*rhi*whi*j/(16*rxlo*d*d)
                dx=right-left
                ml,mu=dx*wlo*rxlo,dx*whi*rxhi
                if not 0<ml<=mu or density<0:
                    raise ValueError("A positive mass or complete drift density is invalid")
                group["leaves"].append(dict(part=k,panel=count,left=left,right=right,
                    mass_lower=ml,mass_upper=mu,density=density,J=j,
                    actual_source_rx_lower=rxlo,real_D_lower=d))
                at,count,total_count=right,count+1,total_count+1
                if count%64==0:
                    memory()
        if not (header and trailer and count==part["panels"] and at==Q(k+1,8)):
            raise ValueError("A complete original part is absent")
        print(json.dumps(dict(event="original_part_read",part=k,panels=count,
                              total_panels=total_count,peak_RSS_KiB=memory())),flush=True)
    if total_count!=1740:
        raise ValueError("Not all1740 original complete leaves were consumed")

    for key,group in groups.items():
        leaves=group["leaves"]
        if not leaves:
            raise ValueError("A real positive bin has no continuous leaves")
        at=group["left"]
        for leaf in leaves:
            if leaf["left"]!=at:
                raise ValueError("The original leaves do not completely cover their bin")
            at=leaf["right"]
        if at!=group["right"]:
            raise ValueError("A positive bin ends before its complete cover")
        slo=sum((v["mass_lower"] for v in leaves),Q(0))
        shi=sum((v["mass_upper"] for v in leaves),Q(0))
        lo=max(slo,group["mass_lower"])
        hi=min(shi,group["mass_upper"])
        if not 0<lo<=hi:
            raise ArithmeticError("The true original mass and leaf enclosures are inconsistent")
        # Finite positive-mass LP. This is a comparison optimizer, not the
        # actual distribution of the true positive measure.
        allocated=[v["mass_lower"] for v in leaves]
        remaining=hi-slo
        order=sorted(range(len(leaves)),key=lambda j:(-leaves[j]["density"],j))
        for j in order:
            extra=min(remaining,leaves[j]["mass_upper"]-allocated[j])
            if extra<0:
                raise ArithmeticError("Negative exact mass capacity")
            allocated[j]+=extra
            remaining-=extra
        if remaining!=0 or sum(allocated,Q(0))!=hi:
            raise ArithmeticError("The finite positive budget was not completely filled")
        if any(not v["mass_lower"]<=x<=v["mass_upper"] for v,x in zip(leaves,allocated)):
            raise ArithmeticError("A comparison mass left its exact bounds")
        greedy=positive_sum(v["density"]*x for v,x in zip(leaves,allocated))
        maxmass=io.positive_upper(max(v["density"] for v in leaves)*hi)
        independent=positive_sum(v["density"]*v["mass_upper"] for v in leaves)
        bound=min(greedy,maxmass,independent)
        if bound<0:
            raise ArithmeticError("A complete drift bound is negative")
        group.update(feasible_mass_lower=lo,feasible_mass_upper=hi,
            greedy_upper=greedy,max_times_true_mass_upper=maxmass,
            independent_leaf_mass_upper=independent,chosen_upper=bound,
            comparison_allocation=allocated)
        memory()

    ordered=[groups[(k,j)] for k in range(8) for j in range(8)]
    part_bounds=[positive_sum(groups[(k,j)]["chosen_upper"] for j in range(8))
                 for k in range(8)]
    prefix=[Q(0)]
    for value in part_bounds:
        prefix.append(io.positive_upper(prefix[-1]+value))
    suffix=[Q(0)]*9
    for k in range(7,-1,-1):
        suffix[k]=io.positive_upper(suffix[k+1]+part_bounds[k])
    # Either whole-segment positive summation is valid. The maximum retains
    # monotonic display across both separately reported global conventions.
    whole=max(prefix[-1],suffix[0])
    part_records=[dict(part=k,panels=summary["parts"][k]["panels"],
        drift_increment_upper=record(part_bounds[k]),
        left_uniform_for_entire_part_upper=record(prefix[k+1]),
        right_uniform_for_entire_part_upper=record(suffix[k]))
        for k in range(8)]
    tmp=primary_path.with_name(primary_path.name+".tmp-"+str(os.getpid()))
    with gzip.open(tmp,"xt",encoding="utf-8",compresslevel=6) as stream:
        stream.write(json.dumps(dict(kind="header",schema="original64-positive-mass-drift-v1",
            source_sha256=digest(__file__),input_hashes={k:v["sha256"] for k,v in inputs.items()},
            all_original_primary_SHA={str(v["part"]):v["sha256"] for v in sources}),
            separators=(",",":"))+"\n")
        for group in ordered:
            row=dict(kind="complete_original_positive_bin_drift",
                part=group["part"],bin=group["bin"],
                source_left=str(group["left"]),source_right=str(group["right"]),
                true_mass_interval=[record(group["mass_lower"],False),record(group["mass_upper"])],
                feasible_total_mass_interval=[record(group["feasible_mass_lower"],False),
                                              record(group["feasible_mass_upper"])],
                positive_budget_upper={name:record(group[name]) for name in (
                    "greedy_upper","max_times_true_mass_upper","independent_leaf_mass_upper","chosen_upper")},
                comparison_allocation_is_not_actual_measure=True,
                leaves=[dict(panel=v["panel"],source_left=str(v["left"]),source_right=str(v["right"]),
                    mass_interval=[record(v["mass_lower"],False),record(v["mass_upper"])],
                    full_J_upper=record(v["J"]),complete_drift_density_upper=record(v["density"]),
                    source_rx_lower=record(v["actual_source_rx_lower"],False),
                    full_real_D_lower=record(v["real_D_lower"],False),
                    comparison_mass_interval=[record(x,False),record(x)])
                    for v,x in zip(group["leaves"],group["comparison_allocation"])])
            stream.write(json.dumps(row,separators=(",",":"),allow_nan=False)+"\n")
        stream.write(json.dumps(dict(kind="trailer",complete=True,bins=64,original_leaves=1740))+"\n")
    if tmp.stat().st_size>=5_000_000:
        raise ValueError("Complete derived primary exceeded the original file limit")
    if primary_path.exists():
        raise FileExistsError("An output appeared while writing")
    os.replace(tmp,primary_path)
    result=dict(
        schema="original-R48-all-eight-parts-positive-mass-centre-drift-v1",
        author="tail_refinement (GPT-6 Astra Pro, AI-assisted)",date_utc="2026-11-13",
        status="Actual positive-measure budget for an original compatible candidate reference; no exact outer solution asserted",
        source_sha256=digest(__file__),proof=dict(path=str(a.proof),sha256=PROOF_SHA),
        io_helper=dict(path=str(a.io_helper),sha256=IO_SHA),inputs=inputs,
        original_primaries=[{k:(str(v) if isinstance(v,Path) else v) for k,v in source.items()
                            if k!="metadata"} for source in sources],
        cell=0,segment=7,parts=part_records,original_leaves=1740,positive_bins=64,
        all_segment_radial_to_centred_position_upper=record(whole),
        centre_endpoint_change_upper=record(min(prefix[-1],suffix[0])),
        unit_reference_vector_change_from_recentering="0 exactly",
        global_gauges="One left or one right constant translation for the whole reference, never pointwise switching",
        pure_phase_scope="Uniform for the explicitly defined angular translates h_alpha(r,theta)=h_0(r,theta-alpha); complete mean and complex Fourier l1 are invariant",
        actual_candidate_reference_vector_not_claimed_as_its_geometric_normal=True,
        no_other_parameter_family_or_prefix_gluing_claimed=True,
        primary=dict(path=str(primary_path),sha256=digest(primary_path),bytes=primary_path.stat().st_size),
        gates=dict(
            frozen_candidate_full_summary_and_formal_exit0=True,
            all_eight_primary_SHA_and_continuous_covers=True,
            all1740_full_mean_and_real_domain_leaves=True,
            all64_original_positive_measure_bins=True,
            positive_mass_interval_feasibility_every_bin=True,
            every_complete_scalar_and_all40_nonzero_J_modes=True,
            R77_only_tightens_the_same_scalar_mode=True,
            physical_r_derivative_and_source_rx_units_preserved=True,
            positive_budget_exact_capacities_and_allocation=True,
            upward128_significant_bits_without_exponent_cutoff=True,
            both_fixed_global_centre_conventions_retained=True),
        true_outer_error_reach_and_Cartesian_bridge_still_unpaid=True,
        new_Arb_Node_ODE_source_integrals=0,
        elapsed_seconds=time.monotonic()-began,peak_RSS_KiB=memory())
    io.atomic_json(summary_path,result)
    print(json.dumps(dict(event="all_original_eight_part_centre_drift",
        summary=str(summary_path),gates=result["gates"],
        all_segment_upper=result["all_segment_radial_to_centred_position_upper"],
        peak_RSS_KiB=result["peak_RSS_KiB"])),flush=True)


if __name__=="__main__":
    main()
