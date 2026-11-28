"""Complete true phase validation, original physical root through the waist.

All newly computed arrays remain private. The exact GCS carrier is reused or
necessarily rematerialized with the published original whole SHA. Scientific
progress is emitted per natural block without publishing coefficient arrays.
"""
from fractions import Fraction as Q
from pathlib import Path
from math import isfinite,nextafter,inf
import argparse,gzip,hashlib,json,os,struct,subprocess,time,sys
from fourfold_codazzi_true_phase_original_inputs import check,admit,MANIFEST,CUT

PAIR=struct.Struct("<dd")
BOX=struct.Struct("<dddd")
FLOAT=struct.Struct("<d")
LENGTH=struct.Struct("<I")


def canonical(v):
    return (json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False)+"\n").encode()


def file_sha(p):
    with p.open("rb") as f:
        return hashlib.file_digest(f,"sha256").hexdigest()


def load_seed(p,whole_sha,whole_bytes):
    from flint import arb,acb
    from fourfold_codazzi_true_phase_circle_validation import GRID,JET_ORDER
    check(p.stat().st_size==whole_bytes and file_sha(p)==whole_sha,"first successful GCS whole identity")
    fields=("phase_displacement_plus","phase_displacement_minus","omega")
    samples={name:[[],[]] for name in fields}
    with gzip.open(p,"rb") as f:
        size,=LENGTH.unpack(f.read(4));check(0<size<20000,"whole GCS header size")
        head=json.loads(f.read(size));shape=head["schema"]
        check(head["cut"]==str(CUT) and head["cells"]==GRID and head["period"]=="pi/2"
              and head["bits"]==320 and len(dict(shape))==len(shape)
              and all(dict(shape)[k]==JET_ORDER+1 for k in fields),"same original normalized cut jets")
        for kind in range(2):
            for name in fields:
                samples[name][kind]=[[] for _ in range(JET_ORDER+1)]
            for j in range(GRID):
                for name,n in shape:
                    raw=f.read(BOX.size*n)
                    check(len(raw)==BOX.size*n,"all original private seed bytes")
                    if name not in samples:continue
                    for m,(a,b,c,d) in enumerate(BOX.iter_unpack(raw)):
                        check(all(map(isfinite,(a,b,c,d))) and a<=b and c<=0<=d,
                              "true real phase or common gap in the original GCS box")
                        samples[name][kind][m].append(acb(arb(a).union(arb(b))))
        check(not f.read(1),"GCS private EOF")
    return [samples[k] for k in fields]


def upper64(v):
    check(v.is_finite() and v.upper()>=0,"finite nonnegative true error")
    x=nextafter(float(v.upper()),inf)
    check(isfinite(x),"a saved directed upper fits binary64")
    return x


def polys_row(q,ends,errors):
    from fourfold_codazzi_true_phase_circle_validation import NMODES,TIME_DEGREE
    raw=bytearray()
    for branch,endpoint in zip(q,ends):
        check(len(branch)==TIME_DEGREE+1,"complete trial in dimensionless time")
        for p in [*branch,endpoint]:
            for j in range(NMODES+1):
                z=p.coeff(j)
                re,im=float(z.real),float(z.imag)
                check(isfinite(re) and isfinite(im) and z.real==re and z.imag==im
                      and p.coeff(-j)==z.conjugate(),"exact stored Hermitian binary64 proposal")
                raw.extend(PAIR.pack(re,im))
    for branch in errors:
        for y in branch:
            raw.extend(FLOAT.pack(upper64(y)))
    return bytes(raw)


def verify(path,expected_head,rowbytes,expected_digest):
    """Read back all dyadics and error upper endpoints in every private row."""
    head=canonical(expected_head);rawhash=hashlib.sha256()
    ncomplex=2*(expected_head["time_degree"]+2)*(expected_head["positive_modes"]+1)
    with gzip.open(path,"rb") as f:
        length=f.read(4);n,=LENGTH.unpack(length);actual=f.read(n)
        check(actual==head,"whole true phase carrier metadata")
        rawhash.update(length+actual)
        for _ in expected_head["inward_plan"]:
            b=f.read(rowbytes);check(len(b)==rowbytes,"complete true phase private row")
            rawhash.update(b)
            for k,(x,y) in enumerate(PAIR.iter_unpack(b[:PAIR.size*ncomplex])):
                check(isfinite(x) and isfinite(y) and (k%(expected_head["positive_modes"]+1)!=0 or y==0),
                      "complete real-valued dyadic comparison readback")
            for y, in FLOAT.iter_unpack(b[PAIR.size*ncomplex:]):
                check(isfinite(y) and y>=0,"whole positive error readback")
        check(not f.read(1) and rawhash.hexdigest()==expected_digest,"whole validated coefficient readback")
    return {"bytes":path.stat().st_size,"sha256":file_sha(path),"uncompressed_sha256":rawhash.hexdigest(),
            "uncompressed_bytes":4+len(head)+rowbytes*len(expected_head["inward_plan"])}


def run(args):
    from importlib.metadata import version
    from flint import arb,ctx
    from fourfold_codazzi_true_phase_circle_validation import (
        fit,initial,advance,norms,NMODES,JET_ORDER,TIME_DEGREE)
    from fourfold_codazzi_true_phase_signed_speed import Inputs
    from fourfold_codazzi_signed_density_transport_arithmetic import exact
    from fourfold_codazzi_true_characteristic_seed_admission import ROOT
    check(os.environ["GITHUB_REPOSITORY"]=="Rogerhu12/math-research-public" and
          os.environ["GITHUB_ACTIONS"]=="true" and os.environ["GITHUB_RUN_ATTEMPT"]=="1",
          "one public scientific owner")
    check(sys.version_info[:3]==(3,12,14) and version("python-flint")=="0.9.0" and version("numpy")=="2.3.5",
          "fixed complete ball runtime")
    ctx.prec=320
    def read(c,p):
        return subprocess.check_output(["git","show",c+":"+p],cwd=args.repo)
    private=args.private;private.mkdir(parents=True,exist_ok=True)
    old=admit((args.repo/MANIFEST).read_bytes(),read)
    inputs=Inputs(*old[:-1]);receipts=old[-1]
    # The seed alone is nonpersistent. Recreate only when its exact first
    # successful private identity has independently been supplied.
    seed_path=args.seed
    restored=False
    if seed_path is None:
        from fourfold_codazzi_true_characteristic_seed_owner import produce
        prior=produce(private/"original-cut-seed",read)
        check(prior["complete"] and prior["private_bytes"]==args.seed_bytes and
              prior["private_whole_sha256"]==args.seed_sha,"same complete original GCS carrier")
        seed_path=private/"original-cut-seed"/"true-signed-cut-seed.bin.gz"
        restored=True
    seed=load_seed(seed_path,args.seed_sha,args.seed_bytes)
    starts=[fit(s[0]) for s in seed[:2]]
    qw=(starts[1]-starts[0])/2
    errors=[initial(s,p,JET_ORDER) for s,p in zip(seed[:2],starts)]
    errors.append(initial(seed[2],qw,JET_ORDER-1))
    maxima=[list(v) for v in errors]
    # At the root the comparison is (rho/rho_c)*q_entry, matching the strict
    # candidate continuously at c. Its derivatives are explicitly qualified.
    rhol,rhou=(exact(Q(x)-CUT) for x in ROOT)
    entry=[norms(p,1) for p in starts]
    root_h1=[];energy=[]
    for u0,u1 in entry:
        a=(exact(Q(1,4000000))+u0).upper()
        b=(exact(Q(1,93750))+u1).upper()
        c=(exact(Q(1,16))+u0/rhol).upper()
        root_h1.append((a*a+b*b).sqrt().upper())
        energy.append((rhou*(a*a+b*b+c*c)).upper())
    plan=[[str(l),str(r),k,i] for l,r,k,i in inputs.plan]
    head={"schema":"GPR-1","physical_period":"pi/2","cut":str(CUT),"inward_plan":plan,
          "positive_modes":NMODES,"time_degree":TIME_DEGREE,"jet_order":JET_ORDER,
          "labels":["plus","minus"],"extra_error":"(Pminus-Pplus)/2 minus signed trial difference",
          "coefficients":"two branches, powers 0..6 plus binary64 outgoing target, then nonnegative Fourier j, real imag f64",
          "continuous_comparison":"q(tau)+tau*(outgoing_target-q(1)); root uses rho/rho_c times entry at c",
          "error_bounds":"plus C0..9, minus C0..9, common gap C0..8 normalized by factorial; full cell",
          "seed_bytes":args.seed_bytes,"seed_sha256":args.seed_sha}
    path=private/"true-phase-inward-complete.bin.gz"
    rawhash=hashlib.sha256();rowbytes=None;beg=time.monotonic()
    science={"kind":"true_global_phase_and_common_gap_v1","run":os.environ["GITHUB_RUN_ID"],
             "attempt":1,"event_commit":os.environ["GITHUB_SHA"],"seed_bytes":args.seed_bytes,
             "seed_sha256":args.seed_sha,"original_successful_GCS_run":args.seed_run+"/1",
             "necessary_whole_GCS_rematerialization":restored,
             "old_scientific_targets_recomputed":0,"physical_angle":"phi","root_label_minus_identity_H1_upper":"1/90000",
             "original_count":len(receipts),"original_bytes":sum(e["bytes"] for e in receipts),
             "original_receipts_sha256":hashlib.sha256(canonical(receipts)).hexdigest(),
             "inward_plan_sha256":hashlib.sha256(canonical(plan)).hexdigest(),"radial_cells":len(plan),
             "complete":False,"proved":False,"uniform_high_response_proved":False}
    def store(sc):
        raw=canonical(sc);check(len(raw)<100000,"whole small scientific receipt")
        tmp=args.receipt.with_suffix(".tmp");tmp.write_bytes(raw);tmp.replace(args.receipt)
    with path.open("xb") as raw:
        with gzip.GzipFile(fileobj=raw,filename="",mode="wb",mtime=0,compresslevel=1) as f:
            h=canonical(head);first=LENGTH.pack(len(h))+h
            rawhash.update(first);f.write(first)
            for j,cell in enumerate(inputs.plan):
                try:
                    stage="true signed speed on the closed physical cell"
                    speeds=inputs.speeds(cell)
                    stage="two signed phase residuals and common gap"
                    q,errors,starts,radial=advance(starts,errors,speeds)
                    stage="physical H1 and dyadic row encoding"
                    h=exact(cell[1]-cell[0])
                    for s,e in enumerate(errors[:2]):
                        energy[s]=(energy[s]+h*(e[0]**2+e[1]**2)+(radial[s]**2)/h).upper()
                    b=polys_row(q,starts,errors)
                    if rowbytes is None:rowbytes=len(b)
                    check(len(b)==rowbytes,"uniform finite representation")
                except Exception as exc:
                    science.update(completed_cells=j,failed_cell=plan[j],failed_stage=stage,
                                   error=str(exc),whole_prefix_uncompressed_sha256=rawhash.hexdigest(),
                                   wall_seconds=time.monotonic()-beg)
                    store(science)
                    print("GPR_FAILED_CELL",canonical(science).decode().strip(),flush=True)
                    raise
                rawhash.update(b);f.write(b)
                for s,errs in enumerate(errors):
                    maxima[s]=[max(x,y).upper() for x,y in zip(maxima[s],errs)]
                if (j+1)%64==0:
                    elapsed=time.monotonic()-beg
                    science.update(completed_cells=j+1,wall_seconds=elapsed,
                                   whole_prefix_uncompressed_sha256=rawhash.hexdigest(),
                                   prefix_errors=[[upper64(v) for v in branch] for branch in maxima])
                    store(science)
                    print("GPR_PROGRESS",j+1,len(plan),round(elapsed,2),flush=True)
    identity=verify(path,head,rowbytes,rawhash.hexdigest())
    check(identity["uncompressed_bytes"]<=140_000_000 and identity["bytes"]<=140_000_000,
          "complete private phase carrier within fixed 140 MB budget")
    h1=[(v[0]**2+v[1]**2).sqrt().upper() for v in maxima]
    check(all(x.is_finite() for x in h1),"full strict H1 bounds")
    domain=[e.sqrt().upper() for e in energy]
    full=[max(v.upper(),q.upper()) for v,q in zip(h1,root_h1)]
    gates={"both_full_spacetime_H1_below_one_over_64":all(64*x<1 for x in domain),
           "both_full_angle_H1_below_one_over_64":all(64*x<1 for x in full),
           "both_strict_label_H1_below_one_over_64":all(64*x<1 for x in h1[:2]),
           "strict_gap_H1_below_one_over_64":64*h1[2]<1}
    science.update(complete=True,proved=True,completed_cells=len(plan),
                   complete_strict_error_upper=[[upper64(v) for v in branch] for branch in maxima],
                   strict_normalized_H1_upper=[upper64(v) for v in h1],
                   complete_root_to_waist_H1_upper=[upper64(v) for v in full],
                   complete_spacetime_H1_upper=[upper64(v) for v in domain],
                   quantitative_gates=gates,private_carrier=identity,wall_seconds=time.monotonic()-beg)
    store(science)
    print("GPR_WHOLE_SMALL_RECEIPT",canonical(science).decode().strip(),flush=True)
    check(all(gates.values()),"complete genuine H1 threshold failed; full measured bounds were preserved")


if __name__=="__main__":
    a=argparse.ArgumentParser(description=__doc__)
    a.add_argument("--repo",type=Path,required=True);a.add_argument("--private",type=Path,required=True)
    a.add_argument("--receipt",type=Path,required=True);a.add_argument("--seed",type=Path)
    a.add_argument("--seed-sha",required=True);a.add_argument("--seed-bytes",type=int,required=True)
    a.add_argument("--seed-run",required=True)
    args=a.parse_args()
    check(len(args.seed_sha)==64 and all(c in "0123456789abcdef" for c in args.seed_sha)
          and args.seed_bytes>0 and args.seed_run.isdigit(),"original successful seed identity")
    run(args)
