"""Complete signed cut seed for the genuine incoming rays, in public Actions."""
from __future__ import annotations
from fractions import Fraction as Q
from pathlib import Path
from math import factorial, isfinite, nextafter, inf
import argparse, gzip, hashlib, json, os, struct, subprocess, sys

CUT=Q(76285779072683,320000000000000)
ANGULAR_CELLS=2048
ORDERS={"chi":9,"T":9,"Xp":8,"Q":6,"G":6,"a0":6,"b0":6,"w1a":6,"w1b":6}
BINARY=struct.Struct("<dddd")


def canonical(value):
    return (json.dumps(value,sort_keys=True,separators=(",",":"),allow_nan=False)+"\n").encode()


def check(ok,message):
    if not ok:
        raise ValueError(message)


def product(a,b,count):
    return [sum((a[j]*b[k-j] for j in range(k+1)),a[0]*0) for k in range(count)]


def frac_power(a,power,ex):
    """Solution to f y' = power f' y for a positive real true f."""
    check(a[0].lower()>0,"uniform real seed gap for rational power")
    out=[(ex(power)*a[0].log()).exp()]
    for n in range(1,len(a)):
        value=sum((ex((power+1)*k/n-1)*a[k]*out[n-k] for k in range(1,n+1)),a[0]*0)
        out.append(value/a[0])
    return out


def signed_fields(f,acb,ex):
    # f holds normalized true angular jets on this node or entire angular bin.
    for name in ("chi","T","Xp","Q","G","a0"):
        check(all(z.imag.contains(0) for z in f[name]),"real signed geometric field "+name)
        f[name]=[z.real for z in f[name]]
    s=frac_power([-z for z in f["T"]],Q(1,2),ex)
    omega=[ex(Q(2,3))*z for z in product(s,[-z for z in f["T"]],10)]
    c_rad=product(f["G"],frac_power([-z for z in f["T"][:7]],Q(-1,4),ex),7)
    check(all(z.contains(0) for z in c_rad[1:]),"exactly radial G / (-T)^(1/4)")
    out={**f,"sqrt_minus_T":s,"omega":omega,"radial_prefactor":c_rad[:1]}
    ii=acb(0,1)
    for sign,key in ((1,"plus"),(-1,"minus")):
        displacement=[x-sign*w for x,w in zip(f["chi"],omega)]
        p=[x-sign*(j+1)*omega[j+1] for j,x in enumerate(f["Xp"])]
        check(p[0].lower()>0,"strict root-label derivative on the entire bin")
        weight=product(f["G"],product(p,p,7),7)
        check(weight[0].lower()>0,"strict positive leading ray weight")
        free_b0=product(s,f["b0"],7)
        check(all(acb(weight[k]).real.overlaps((f["a0"][k]+ii*sign*free_b0[k]).real)
                  and (f["a0"][k]+ii*sign*free_b0[k]).imag.contains(0) for k in range(7)),
              "signed matching with the saved true leading root amplitude")
        out["phase_displacement_"+key]=displacement
        out["p_"+key]=p
        out["v0_"+key]=weight
        inverse=frac_power(weight,Q(-1),ex)
        sb=product(s,f["w1b"],7)
        for eps,frequency in ((1,"positive"),(-1,"negative")):
            # Native exact branch: a1_minus=-a1_plus, b1_minus=b1_plus.
            v1=[eps*f["w1a"][k]+ii*(eps*sign)*sb[k] for k in range(7)]
            out["R_"+key+"_"+frequency]=product(v1,inverse,7)
    return out


def pack_value(z,acb):
    z=acb(z)
    vals=(nextafter(float(z.real.lower()),-inf),nextafter(float(z.real.upper()),inf),
          nextafter(float(z.imag.lower()),-inf),nextafter(float(z.imag.upper()),inf))
    check(all(isfinite(v) for v in vals),"finite whole directed binary64 output")
    return BINARY.pack(*vals)


def produce(private,read_historical):
    from flint import arb,acb,ctx
    import flint
    import fourfold_codazzi_true_characteristic_root_input as root
    import fourfold_codazzi_true_characteristic_seed_admission as A
    import fourfold_codazzi_root_Laurent_Taylor_algebra as L
    check(sys.version_info[:3]==(3,12,14) and flint.__version__=="0.9.0",
          "admitted signed root seed runtime")
    check(hashlib.sha256(Path(L.__file__).read_bytes()).hexdigest()==A.ALGEBRA,
          "original whole Laurent algebra")
    ctx.prec=320
    stage,m,receipts=A.admit(read_historical,root.required_stages())
    series=root.signed_series(stage)
    major={k:(arb(m[k][0]["ball"]).upper(),Q(m[k][1]),Q(m[k][2])) for k in ORDERS}
    anchor=tuple(map(Q,A.ROOT));piece=tuple(map(Q,A.PIECE))
    check(piece[0]<CUT<anchor[0]<=anchor[1]<piece[1],"cut and true root on the same physical piece")
    rho=L.ex(anchor[0]-CUT).union(L.ex(anchor[1]-CUT))
    knots=ANGULAR_CELLS
    samples={}
    for field,order in ORDERS.items():
        samples[field]=root.root_mesh(series[field],major[field],rho,knots,order)
    destination=Path(private)/"true-signed-cut-seed.bin.gz"
    destination.parent.mkdir(parents=True,exist_ok=True)
    total_boxes=0
    schema=None
    with destination.open("xb") as raw:
        with gzip.GzipFile(fileobj=raw,filename="",mode="wb",mtime=0) as out:
            for kind in range(2):
                for j in range(knots):
                    values={k:[v[j]/factorial(p) for p,v in enumerate(samples[k][kind])]
                            for k in ORDERS}
                    row=signed_fields(values,acb,L.ex)
                    shape=[(k,len(v)) for k,v in sorted(row.items())]
                    if schema is None:
                        schema=shape
                        head=canonical({"schema":schema,"cells":knots,"period":"pi/2",
                            "bin_halfwidth":"pi/(4*cells)","order":"nodes then centered whole bins",
                            "coefficients":"ordinary physical angle derivatives divided by factorial",
                            "format":"each complex rectangle little-endian float64 re lo,hi,im lo,hi",
                            "cut":str(CUT),"root":list(A.ROOT),"bits":ctx.prec})
                        out.write(struct.pack("<I",len(head)));out.write(head)
                    check(shape==schema,"one complete seed row shape")
                    for key,_ in shape:
                        for value in row[key]:
                            out.write(pack_value(value,acb));total_boxes+=1
    extrema={k:[inf,-inf] for k in ("T","omega","p_plus","p_minus","v0_plus","v0_minus")}
    with gzip.open(destination,"rb") as inp:
        length=struct.unpack("<I",inp.read(4))[0]
        check(inp.read(length)==head,"complete private seed header readback")
        for kind in range(2):
            for j in range(knots):
                for key,n in schema:
                    for q in range(n):
                        rl,rh,il,ih=BINARY.unpack(inp.read(BINARY.size))
                        check(all(isfinite(v) for v in (rl,rh,il,ih)) and rl<=rh and il<=ih,
                              "complete finite complex box readback")
                        if kind==1 and q==0 and key in extrema:
                            check(il<=0<=ih,"real projected geometry in full whole-bin readback")
                            e=extrema[key];e[0]=min(e[0],rl);e[1]=max(e[1],rh)
        check(not inp.read(1),"whole seed EOF")
    check(extrema["T"][1]<0 and all(extrema[k][0]>0 for k in extrema if k!="T"),
          "whole signed start chart positive gaps")
    with destination.open("rb") as source:
        whole_sha=hashlib.file_digest(source,"sha256").hexdigest()
    return {"kind":"R149_true_signed_root_cut_seed_v1","complete":True,"proved":True,
        "cut":str(CUT),"root_interval":list(A.ROOT),"physical_angle_cells":knots,
        "native_stage_count":len(stage),"all_whole_inputs":receipts,"orders":ORDERS,
        "private_field_shape":schema,"private_whole_box_count":total_boxes,
        "private_bytes":destination.stat().st_size,
        "private_whole_sha256":whole_sha,
        "whole_bin_binary64_extrema":extrema,"old_scientific_targets_recomputed":0,
        "all_global_negative_cells_complete":False,"uniform_high_response_proved":False}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo",type=Path,required=True)
    parser.add_argument("--private",type=Path,required=True)
    parser.add_argument("--receipt",type=Path,required=True)
    args=parser.parse_args()
    check(os.environ.get("GITHUB_ACTIONS")=="true" and
          os.environ.get("GITHUB_REPOSITORY")=="Rogerhu12/math-research-public",
          "public repository scientific owner")
    def read(commit,path):
        return subprocess.check_output(["git","show",commit+":"+path],cwd=args.repo)
    receipt=produce(args.private,read)
    receipt.update(run=os.environ["GITHUB_RUN_ID"],attempt=os.environ["GITHUB_RUN_ATTEMPT"],
                   event_commit=os.environ["GITHUB_SHA"])
    args.receipt.write_bytes(canonical(receipt))


if __name__=="__main__":
    main()
