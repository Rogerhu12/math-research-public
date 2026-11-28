"""Receive the original two successful, whole, nonpersistent input carriers.

Original physical GPR rows need the signed speed, two proposals and three
error jets that were encoded in each row. Root/spacetime H1 totals and
original acceptance gates are read from the original Actions receipt.
"""
from pathlib import Path
from hashlib import sha256
from importlib.metadata import version
from zipfile import ZipFile
import argparse,gzip,json,os,subprocess,sys


GCS=("46132087372","a3c58553c4591e6ddc97a493fcc12af2085a12a6",19866,
     "201c8215275b04dfa69c6a9b03248dea6bde01bd782969d006c823088c0637b7",
     "complete-physical-cut/6_Compute true root labels and all four signed ratio jets at c.txt",
     "GCS_WHOLE_SMALL_RECEIPT")
GPR=("46135620219","12cd72d84df91a464d4d01faed764b1661af228f",2950,
     "586c1a68fd29bcb622fc2a932f0f82b6fa52468215491bec41490d9265c327c9",
     "full-domain-validation/6_Validate both true phase rays and common gap from root to waist.txt",
     "GPR_WHOLE_SMALL_RECEIPT")
SEED=(11131542,"9af56c23e91a021f0463aa01b68ea93916ba11d374ecd7323ce4c4b51b3da9ba")
PHASE={"bytes":53688308,"sha256":"048aaf65e96b3b7edbd5c26f078994874bb894398c390d4de2b1d9176a5c2450",
       "uncompressed_bytes":100890185,"uncompressed_sha256":"1e7c3a5c6abd07ce04f12bc3abbf16079ae94db229f1d042b86b6c55300fef42"}


def require(condition,message):
    if not condition:raise ValueError(message)


def original_log(path,spec):
    run,_,length,digest,step_log,marker=spec
    # GitHub can return aggregate job logs, separate numbered step logs,
    # or both. File names are presentation metadata. Consume every archive
    # member to EOF and require all copies of the actual receipt to agree.
    prefix=(marker+" ").encode();rows=set();members=[]
    with ZipFile(path) as archive:
        for entry in archive.infolist():
            if entry.is_dir():continue
            hits=0
            with archive.open(entry) as f:
                for line in f:
                    before,sep,body=line.rstrip(b"\r\n").partition(prefix)
                    front=before.removeprefix(b"\xef\xbb\xbf").strip()
                    if not sep or not body.startswith(b"{"):continue
                    if front and not (front[:4].isdigit() and front.endswith(b"Z")):continue
                    rows.add(body+b"\n");hits+=1
            if hits:members.append([entry.filename,hits])
        if not rows:print("GRQ_ORIGINAL_LOG_MEMBER_NAMES",run,archive.namelist(),flush=True)
    require(len(rows)==1,"one distinct complete original scientific receipt across the whole job archive")
    raw=rows.pop()
    require(len(raw)==length and sha256(raw).hexdigest()==digest,"the exact original complete small receipt bytes")
    print("GRQ_ORIGINAL_PUBLIC_RECEIPT",run,length,digest,"matched_members",members,
          "documented_step",step_log,flush=True)
    return raw


def original(directory,spec):
    run,event,_,_,_,_=spec
    observation=json.loads((directory/(run+".json")).read_bytes())
    require(str(observation["id"])==run and observation["run_attempt"]==1
            and observation["head_sha"]==event and observation["event"]=="push"
            and observation["status"]=="completed" and observation["conclusion"]=="success",
            "the original successful first attempt and event")
    raw=original_log(directory/(run+".zip"),spec)
    value=json.loads(raw)
    require(value["complete"] is value["proved"] is True and str(value["run"])==run
            and str(value["attempt"])=="1" and value["event_commit"]==event,
            "whole historical receipt bound to its own successful workflow")
    return raw,value


def restore(args):
    from flint import ctx
    from fourfold_codazzi_true_ratio_live_rules import gate
    from fourfold_codazzi_true_phase_original_inputs import admit,MANIFEST,CUT
    from fourfold_codazzi_true_characteristic_seed_owner import produce
    from fourfold_codazzi_true_phase_signed_speed import Inputs
    from fourfold_codazzi_true_phase_circle_validation import (
        NMODES,JET_ORDER,TIME_DEGREE,fit,initial,advance)
    from fourfold_codazzi_true_phase_global_validation import canonical,load_seed,polys_row,verify,LENGTH
    root=args.private;root.mkdir(parents=True,exist_ok=True)
    cs,seed_receipt=original(args.logs,GCS);pr,phase_receipt=original(args.logs,GPR)
    require((seed_receipt["private_bytes"],seed_receipt["private_whole_sha256"])==SEED and
            phase_receipt["private_carrier"]==PHASE and phase_receipt["completed_cells"]==3026
            and phase_receipt["original_successful_GCS_run"]==GCS[0]+"/1"
            and (phase_receipt["seed_bytes"],phase_receipt["seed_sha256"])==SEED
            and all(phase_receipt["quantitative_gates"].values()),"both original whole input identities")
    (root/"gcs-receipt.json").write_bytes(cs);(root/"gpr-receipt.json").write_bytes(pr)
    def read(commit,path):
        return subprocess.check_output(["git","show",commit+":"+path],cwd=args.repo)
    ctx.prec=320
    old=admit((args.repo/MANIFEST).read_bytes(),read);inp=Inputs(*old[:-1])
    gate()
    actual=produce(root,read)
    gate()
    actual.update(run=GCS[0],attempt="1",event_commit=GCS[1])
    require(canonical(actual)==cs,"one necessary original seed and its complete original receipt")
    path=root/"true-signed-cut-seed.bin.gz"
    seed=load_seed(path,SEED[1],SEED[0])
    starts=[fit(v[0]) for v in seed[:2]]
    errors=[initial(v,p,JET_ORDER) for v,p in zip(seed[:2],starts)]
    errors.append(initial(seed[2],(starts[1]-starts[0])/2,JET_ORDER-1))
    plan=[[str(l),str(r),k,i] for l,r,k,i in inp.plan]
    require(len(plan)==3026 and sha256(canonical(plan)).hexdigest()==phase_receipt["inward_plan_sha256"]
            and sha256(canonical(old[-1])).hexdigest()==phase_receipt["original_receipts_sha256"],
            "the original full ordered natural domain")
    head={"schema":"GPR-1","physical_period":"pi/2","cut":str(CUT),"inward_plan":plan,
          "positive_modes":NMODES,"time_degree":TIME_DEGREE,"jet_order":JET_ORDER,
          "labels":["plus","minus"],"extra_error":"(Pminus-Pplus)/2 minus signed trial difference",
          "coefficients":"two branches, powers 0..6 plus binary64 outgoing target, then nonnegative Fourier j, real imag f64",
          "continuous_comparison":"q(tau)+tau*(outgoing_target-q(1)); root uses rho/rho_c times entry at c",
          "error_bounds":"plus C0..9, minus C0..9, common gap C0..8 normalized by factorial; full cell",
          "seed_bytes":SEED[0],"seed_sha256":SEED[1]}
    phase=root/"true-phase-inward-complete.bin.gz";row_size=None;hh=sha256()
    with phase.open("xb") as raw:
        with gzip.GzipFile(fileobj=raw,filename="",mode="wb",mtime=0,compresslevel=1) as out:
            h=canonical(head);b=LENGTH.pack(len(h))+h;out.write(b);hh.update(b)
            for k,cell in enumerate(inp.plan,1):
                gate()
                trial,errors,starts,_=advance(starts,errors,inp.speeds(cell))
                b=polys_row(trial,starts,errors)
                if row_size is None:row_size=len(b)
                require(len(b)==row_size,"complete original natural row size")
                out.write(b);hh.update(b)
                if k%512==0:print("GRQ_ORIGINAL_CARRIER_ROWS",k,len(plan),flush=True)
    require(verify(phase,head,row_size,hh.hexdigest())==PHASE,"entire private original phase and all endpoints")
    print("GRQ_TWO_EXACT_ORIGINAL_INPUTS",GCS[0],GPR[0],SEED,PHASE,"old_targets_reawarded",0,flush=True)


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    for k in ("repo","logs","private"):p.add_argument("--"+k,required=True,type=Path)
    a=p.parse_args()
    require(os.environ.get("GITHUB_ACTIONS")=="true" and os.environ.get("GITHUB_RUN_ATTEMPT")=="1"
            and os.environ.get("GITHUB_REPOSITORY")=="Rogerhu12/math-research-public" and
            sys.version_info[:3]==(3,12,14) and version("python-flint")=="0.9.0" and version("numpy")=="2.3.5",
            "original single-thread public container runtime")
    restore(a)
