#!/usr/bin/env python3
"""Actual piecewise real root folds, complete old-angle norms and true seams.

Reuse the entire 169-germ scalar cover, the original 4650 positive rows,
and exact original candidate/response shards. No target, transport or
response solve is rerun. All numerical work requires this public Actions.
"""
from __future__ import annotations
import argparse
from bisect import bisect_right
from fractions import Fraction as Q
from functools import lru_cache
import gzip, hashlib, io, json, math, os
from pathlib import Path
import sys, time
import flint
from flint import arb, ctx
import numpy as np

PUBLIC="Rogerhu12/math-research-public"
TOPIC="topics/visible-flex-exact-nearby"
CANDIDATE="ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413"
OBJECT="91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848"
BASE="440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
ZDEF="6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04"
PINS={
 "candidate":CANDIDATE,
 "response":"ed42a71ddeb0420428f0313df321dc1f9b10525521d399cb1d666ae98fe410f6",
 "repair":"6ee8b07fe94a8d9f87865a9ebb6650266b7eca792d435136ba533be92b1959fc",
 "direction":"87ed2f618bcaf77b0649abf561daea7225c9b7d667edc22afb91d86255da8f88",
 "root_germ":"397f9b428c787823994f8c849ad7d1f9209220c3c6e8907b38be562b3cbc9864",
 "scalar_cover":"94492bbafda1e5efb30b129e534171c9fc305524a2d972064e34e8894948bad3",
 "positive_parts":"32b430a27a20726f095098902afdb93e656ea746eb81bce09a559e6f65787fd3",
}
POSITIVE="ea17451120f8c368ea3e5d4ee511a9d1d03d8a97705e7bd36cf9d015a8d9d93d"
DELTA=Q(1,100000000)
WIDTHS=(Q(1,16),Q(1,32),Q(1,64))
RADII=(Q(1,1000),Q(1,500),Q(1,200),Q(1,100),Q(3,200),Q(1,50))
RIGHT_POS=Q("0.2384058742994")

def digest(data): return hashlib.sha256(data).hexdigest()
def sha(path): return digest(Path(path).read_bytes())
def read(path):
    data=Path(path).read_bytes()
    return json.loads(gzip.decompress(data) if str(path).endswith(".gz") else data)
def save(path,data):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(data,indent=2,allow_nan=False)+"\n").encode()
    if str(path).endswith(".gz"): raw=gzip.compress(raw,mtime=0)
    tmp=path.with_name(path.name+".partial");tmp.write_bytes(raw);tmp.replace(path)
def ex(x):
    x=Q(x);return arb(x.numerator)/x.denominator
def interval(a,b): return ex(a).union(ex(b))
def dyadic(x): return Q.from_float(float(x))
def up(x): return abs(x).upper()
def box(x): return arb(x["ball"])
def rec(x):
    x=arb(x)
    return {"ball":x.str(60),"lower":x.lower().str(60),"upper":x.upper().str(60)}
def compact(x): return {"ball":arb(x).str(48)}
def power(x,p): return (x.log()*ex(p)).exp()
def maximum(values): return max((up(x) for x in values),default=arb(0)).upper()
def convolution(a,b):
    out=[arb(0) for _ in range(len(a)+len(b)-1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return out
@lru_cache(maxsize=None)
def angular_weight(k,width,order):
    return (ex(width)*k).exp().upper()*ex(k)**order
def weighted(values,frequencies,width,order=0):
    return sum((up(v)*angular_weight(k,width,order)
                for v,k in zip(values,frequencies)),arb(0)).upper()
def angular(values,start,width,order=0,nonmean=False,primitive=False):
    return sum((up(v)*angular_weight(abs(4*k),width,order)
                 *(1 if not primitive else 1/ex(abs(4*k)))
                 for k,v in zip(range(start,start+len(values)),values)
                 if not (nonmean and k==0)),arb(0)).upper()

def restrict_model(row,name,left,right,derivative=0):
    """Same complete high-seven identity as the published restriction proof."""
    left,right=Q(left),Q(right);j=int(derivative)
    a,b=map(Q,row["interval"]);center=Q(row["center"])
    if not a<=left<=right<=b or not 0<=j<=7:
        raise ValueError("restriction leaves a true original scalar cell")
    model=row["models"][name];c=list(map(Q,model["exact_centered_polynomial"]))
    point=[box(z) for z in model["point_jets"]]
    whole7=box(model["whole_final_derivative"])
    if len(c)!=8 or len(point)!=7: raise ValueError("a full degree-seven identity is required")
    h=ex(max(abs(left-center),abs(right-center)))
    fee=sum((math.factorial(k)//math.factorial(k-j)*abs(point[k]-ex(c[k]))*h**(k-j)
             for k in range(j,7)),arb(0))
    fee+=abs(whole7-math.factorial(7)*ex(c[7]))*h**(7-j)/math.factorial(7-j)
    coeff=[Q(math.factorial(k),math.factorial(k-j))*c[k] for k in range(j,8)]
    x=interval(left-center,right-center);value=arb(0)
    for z in reversed(coeff): value=value*x+ex(z)
    return value+arb(0,fee.upper())

class Shards:
    """Only complete original shards meeting the declared real window."""
    def __init__(self,path,parts,components):
        self.index=read(path);self.parts={};self.nodes={}
        if self.index["kind"]!="complete_lossless_radial_cubic_shards_v1":
            raise ValueError("unknown original polynomial container")
        if self.index["coefficient_shape"]!=[4,6144,components]:
            raise ValueError("an original polynomial component was dropped")
        for number in parts:
            spec=self.index["parts"][number];part=path.parent/spec["file"]
            if sha(part)!=spec["sha256"] or part.stat().st_size!=spec["bytes"]:
                raise ValueError("an original complete polynomial shard changed")
            with np.load(io.BytesIO(gzip.decompress(part.read_bytes())),allow_pickle=False) as data:
                r=data["radial_nodes"].copy();c=data["piece_coefficients"].copy()
            first,last=spec["first_interval"],spec["last_interval_exclusive"]
            if (r.shape!=(last-first+1,) or c.shape!=(4,last-first,components)
                or not np.isfinite(r).all() or not np.isfinite(c).all()
                or not (np.diff(r)>0).all()):
                raise ValueError("invalid original full polynomial array")
            for i,x in enumerate(r):
                idx=first+i;v=dyadic(x)
                if idx in self.nodes and self.nodes[idx]!=v:
                    raise ValueError("original shard endpoint bytes disagree")
                self.nodes[idx]=v
            self.parts[number]=(first,last,c)
        self.component_count=components
        self.indices=sorted(self.nodes)
        if any(b!=a+1 for a,b in zip(self.indices,self.indices[1:])):
            raise ValueError("selected original shards have an interval gap")
        self.first=self.indices[0];self.last=self.indices[-1]
        self.radial=[self.nodes[i] for i in self.indices]
    def piece(self,left,right):
        local=bisect_right(self.radial,left)-1;index=self.first+local
        if not self.first<=index<self.last or not self.nodes[index]<=left<right<=self.nodes[index+1]:
            raise ValueError("a closed interval crosses an original polynomial seam")
        return index
    @lru_cache(maxsize=4)
    def coefficients(self,piece):
        for first,last,c in self.parts.values():
            if first<=piece<last:
                return tuple(tuple(dyadic(c[d,piece-first,k]) for d in range(4))
                             for k in range(self.component_count))
        raise ValueError("required original polynomial piece is missing")
    def values(self,piece,left,right,derivative=0):
        x=interval(left-self.nodes[piece],right-self.nodes[piece]);out=[]
        for desc in self.coefficients(piece):
            v=arb(0)
            for k in range(3,derivative-1,-1):
                v=v*x+math.factorial(k)//math.factorial(k-derivative)*ex(desc[3-k])
            out.append(v)
        return out
    def endpoint(self,piece,r,derivative):
        x=r-self.nodes[piece];out=[]
        for desc in self.coefficients(piece):
            v=Q(0)
            for k in range(3,derivative-1,-1):
                v=v*x+Q(math.factorial(k),math.factorial(k-derivative))*desc[3-k]
            out.append(v)
        return out

def restore_positive(index_path):
    spec=read(index_path)
    if (spec["kind"]!="complete_native_lossless_container_binary_parts_v2"
        or spec["original_sha256"]!=POSITIVE or spec["complete_native_rows"]!=4650
        or not spec["native_complete"] or spec["native_failure"] is not None):
        raise ValueError("the complete original positive native identity changed")
    blocks=[];cursor=0
    for part in spec["parts"]:
        path=index_path.parent/part["file"];raw=path.read_bytes()
        if len(raw)!=part["compressed_bytes"] or digest(raw)!=part["compressed_sha256"]:
            raise ValueError("an original positive container part changed")
        block=gzip.decompress(raw)
        if (part["offset"]!=cursor or len(block)!=part["bytes"] or digest(block)!=part["sha256"]):
            raise ValueError("the original positive byte reconstruction has a gap")
        blocks.append(block);cursor+=len(block)
    raw=b"".join(blocks)
    if len(raw)!=spec["original_bytes"] or digest(raw)!=POSITIVE:
        raise ValueError("the original positive native was not restored exactly")
    doc=json.loads(gzip.decompress(raw))
    if (not doc["complete"] or doc.get("failure") is not None or len(doc["rows"])!=4650
        or doc["identity"]["candidate_sha256"]!=CANDIDATE
        or doc["identity"]["object_sha256"]!=OBJECT
        or doc["identity"]["source_sha256"]!="1292a1c06695d49a6f5e6bca27ad375b2fd82b44ebe1e6066327b7b7a79d882c"):
        raise ValueError("the original complete positive mathematical object differs")
    cursor=RIGHT_POS
    for row in doc["rows"]:
        a,b=map(Q,row["interval"])
        if a!=cursor or not a<b: raise ValueError("original 4650 closed rows have a gap")
        cursor=b
    if cursor!=Q(25,8): raise ValueError("original positive rows lost the regular endpoint")
    return doc

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo-root",type=Path,required=True)
    ap.add_argument("--manifest",type=Path,required=True)
    ap.add_argument("--out",type=Path,required=True)
    args=ap.parse_args()
    if args.out.exists(): raise FileExistsError("preserve every actual larger-window prefix")
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("all numerical work belongs to the actual public Actions job")
    runtime={"python":".".join(map(str,sys.version_info[:3])),
             "numpy":np.__version__,"python_flint":flint.__version__}
    if runtime!={"python":"3.12.14","numpy":"2.3.5","python_flint":"0.9.0"}:
        raise RuntimeError("the exact public arithmetic runtime changed")
    ctx.prec=256;started=time.monotonic()
    report=dict(kind="actual_piecewise_real_root_fold_and_complete_old_angle_envelopes",
        complete=False,proved=False,failure=None,runtime=runtime,source_sha256=sha(__file__),
        public_repository=PUBLIC,public_run_id=os.environ.get("GITHUB_RUN_ID"),
        public_run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        candidate_sha256=CANDIDATE,background_definition_sha256=BASE,
        explicit_direction_definition_sha256=ZDEF,inputs={},gates=[],rows=[],seams=[],cases=[],
        actual_intrinsic_parameter="eta_0",exact_complex_parameter_radius=str(DELTA),
        full193_direction_and_independent_even_mean=True,
        all_original_169_germs_and_4650_positive_rows_reused_not_recomputed=True,
        radial_domain_is_real_and_original_piecewise_smooth=True,
        radial_holomorphic_continuation_across_original_seams_claimed=False,
        new_Airy_forcing_amplitudes_or_strong_remainder_norm_evaluated=False,
        numerical_cutoff97_return_inverse_claimed=False,actual_PDE_branch_claimed=False)
    def check(name,okay):
        okay=bool(okay);report["gates"].append({"name":name,"passed":okay})
        if not okay: raise ValueError("failed actual larger-root gate: "+name)
    try:
        manifest=read(args.manifest)
        if manifest["public_repository"]!=PUBLIC: raise ValueError("wrong public input closure")
        files={v["path"]:v for v in manifest["files"]}
        bysha={v["sha256"]:v["path"] for v in manifest["files"]}
        for name,pin in PINS.items():
            rel=manifest["input_paths"][name];path=args.repo_root/rel
            if sha(path)!=pin: raise ValueError("a completed original input changed: "+name)
            report["inputs"][name]={"path":rel,"sha256":pin,"bytes":path.stat().st_size}
        paths={name:args.repo_root/rel for name,rel in manifest["input_paths"].items()}
        repair,direction,germ,cover=[read(paths[n]) for n in ("repair","direction","root_germ","scalar_cover")]
        check("the original exact continuous repair and all193 direction identities match",
            repair["complete"] and repair["derived_definition_sha256"]==BASE
            and repair["candidate_sha256"]==CANDIDATE
            and direction["complete"] and direction["derived_direction_definition_sha256"]==ZDEF
            and direction["background_definition_sha256"]==BASE
            and direction["candidate_sha256"]==CANDIDATE
            and direction["original_trial_sha256"]==PINS["response"]
            and direction["exact_affine_offset"]=="0" and direction["actual_affine_parameter"]=="eta_0")
        check("the complete original complex intrinsic root germ and zero compact support are retained",
            germ["complete"] and germ["proved"] and germ["candidate_sha256"]==CANDIDATE
            and germ["object_sha256"]==OBJECT and germ["source_sha256"]==
                "a3ad50b828c69d3e6f1e9254c1f266535171741ee2cd675d1569ef8f0fac0491"
            and germ["compact_bump_identically_zero_on_entire_actual_germ"])
        roots=list(map(Q,germ["root_interval"]));rlo,rhi=roots
        left,right=rlo-max(RADII),rhi+max(RADII)
        zone_left=rlo-Q(9,1000000);zone_right=RIGHT_POS
        check("the entire larger real window is outside the exact compact metric support",
            Q(9,50)<left<zone_left<rlo<rhi<zone_right<right
            and zone_left>rlo-Q(germ["complex_radial_radius"])
            and zone_right<rhi+Q(germ["complex_radial_radius"]))
        base=Shards(paths["candidate"],(1,2),65)
        response=Shards(paths["response"],(4,5,6),193)
        alpha=Q(base.index["metadata"]["exact_float_amplitude"])
        meta=response.index["metadata"]
        check("the exact original candidate and full193 physical response coordinates remain",
            base.index["metadata"]["object_sha256"]==OBJECT
            and base.index["metadata"]["modes"]==32
            and base.index["metadata"]["physical_frequency_factor"]==4
            and alpha==Q(6890507429876859,9007199254740992)
            and meta["background_candidate_sha256"]==CANDIDATE and meta["role"]=="response_full"
            and meta["modes"]==96 and meta["physical_frequency_factor"]==4
            and meta["finite_head_mean_was_not_removed_from_the_solve"]
            and meta["original_fourth_Robin_row_retained"]
            and meta["coordinates"]=="physical unnormalized moving variation; h1 sine(4j phi), h2 cosine(4j phi) including its true mean")
        check("both original polynomial families cover the whole larger window with identical nodes",
            base.radial[0]<left<right<base.radial[-1]
            and response.radial[0]<left<right<response.radial[-1]
            and all(base.nodes[i]==r for i,r in response.nodes.items() if i in base.nodes))
        ebase=list(map(Q,repair["exact_cumulative_coefficient_suprema"]))
        ez=list(map(Q,direction["exact_complete_repair_coefficient_suprema"]))
        check("all complete physical repair offsets are reused as exact value fees only",
            len(ebase)==65 and len(ez)==193 and all(x>=0 for x in ebase+ez)
            and repair["corrected_value_and_all_angular_derivatives_continuous"]
            and repair["piecewise_radial_derivative_correction"]=="exactly zero on every open original cubic piece")
        check("the whole original scalar cover is actual eta0 with every accepted cell",
            cover["complete"] and cover["accepted_cell_count"]==626
            and len(cover["germs"])==169 and cover["exact_affine_offset"]=="0")
        negative=[];scalar_count=0
        for item in cover["germs"]:
            pin=item["sha256"]
            if pin not in bysha: raise ValueError("one original scalar germ is absent from the exact closure")
            path=args.repo_root/bysha[pin]
            if sha(path)!=pin: raise ValueError("an original completed scalar germ changed")
            doc=read(path)
            if not doc["complete"]: raise ValueError("an incomplete scalar germ cannot supply a true cell")
            for original in doc["rows"]:
                scalar_count+=1
                a,b=map(Q,original["interval"])
                if a<zone_left and b>left:
                    negative.append((a,b,original,pin))
        negative.sort(key=lambda x:x[0])
        cursor=left
        for a,b,_,_ in negative:
            aa,bb=max(a,left),min(b,zone_left)
            if aa!=cursor or not aa<bb: raise ValueError("the selected actual negative scalar cells have a gap")
            cursor=bb
        check("all626 original scalar identities were retained and their selected restriction is gap free",
              scalar_count==626 and cursor==zone_left)
        positive=restore_positive(paths["positive_parts"])
        prows=[(Q(r["interval"][0]),Q(r["interval"][1]),r,i)
               for i,r in enumerate(positive["rows"]) if Q(r["interval"][0])<right]
        cursor=zone_right
        for a,b,_,_ in prows:
            if a!=cursor: raise ValueError("the selected positive intrinsic rows have a gap")
            cursor=min(b,right)
        check("the full original positive cache and exact root overlap cover the selected positive part",
              cursor==right)
        cintr=germ["complex_intrinsic_coefficients"]
        kroot=box(cintr["K1"]["real"])
        check("the original root derivative supplies the complete real divided-curvature gap",kroot>0)
        root_values={n:box(cintr[n]["real"]) for n in ("beta","gamma","s")}
        cuts={left,right,zone_left,zone_right,rlo,rhi}
        cuts.update(r for r in base.radial if left<r<right)
        for a,b,_,_ in negative:
            cuts.update((max(a,left),min(b,zone_left)))
        for a,b,_,_ in prows:
            cuts.update((max(a,zone_right),min(b,right)))
        for radius in RADII: cuts.update((rlo-radius,rhi+radius))
        cuts=sorted(x for x in cuts if left<=x<=right)
        negstarts=[x[0] for x in negative];posstarts=[x[0] for x in prows]
        bounds_rows=[]
        frequencies={32:[4*j for j in range(1,33)]+[0]+[4*j for j in range(1,33)],
                     96:[4*j for j in range(1,97)]+[0]+[4*j for j in range(1,97)]}
        for count,(a,b) in enumerate(zip(cuts[:-1],cuts[1:])):
            if not a<b: raise ValueError("a requested real row is empty")
            piece=base.piece(a,b)
            if response.piece(a,b)!=piece: raise ValueError("response and candidate radial pieces differ")
            if b<=zone_left:
                aa,bb,row,pin=negative[bisect_right(negstarts,a)-1]
                vals={n:restrict_model(row,n,a,b) for n in ("beta","gamma","s","K")}
                rho=interval(rlo-b,rhi-a)
                if not rho>0 or not vals["K"]<0: raise ValueError("negative divided curvature loses its true sign")
                kval=-vals["K"]/rho
                provenance={"kind":"original_high7_true_restriction","sha256":pin,"interval":row["interval"]}
            elif a>=zone_right:
                aa,bb,row,index=prows[bisect_right(posstarts,a)-1]
                if not aa<=a<b<=bb: raise ValueError("a positive row crossed its original true intrinsic box")
                vals={n:box(row["intrinsic"][n]) for n in ("beta","gamma","K")}
                vals["s"]=1/box(row["intrinsic"]["Cref"])
                distance=interval(a-rhi,b-rlo)
                if not distance>0 or not vals["K"]>0: raise ValueError("positive divided curvature loses its true sign")
                kval=vals["K"]/distance
                provenance={"kind":"original_complete_positive_intrinsic","row":index,"interval":row["interval"]}
            else:
                if not zone_left<=a<b<=zone_right: raise ValueError("a true row crosses the root envelope")
                vals=dict(root_values);kval=kroot
                vals["K"]=kroot*interval(a-rhi,b-rlo)
                provenance={"kind":"original_complete_complex_root_germ_real_restriction"}
            if not kval>0 or not vals["gamma"]>0: raise ValueError("the true scalar root coefficient is unresolved")
            raw=base.values(piece,a,b);zraw=response.values(piece,a,b)
            physical=[ex(alpha)*v+arb(0,ex(e)) for v,e in zip(raw,ebase)]
            physical[32]+=vals["s"]
            z=[(up(v)+ex(e)).upper() for v,e in zip(zraw,ez)]
            mbase=physical[32];mfee=ex(DELTA)*z[96]
            mgap=(-mbase.upper()-mfee).lower();mmax=(up(mbase)+mfee).upper()
            if not mgap>0: raise ValueError("the exact repaired full-family mean loses its sign")
            eta_min=(vals["gamma"].lower()*mgap).lower()
            eta_max=(vals["gamma"].upper()*mmax).upper()
            amin=(eta_min*kval.sqrt().lower()).lower()
            amax=(eta_max*up(kval.sqrt())).upper()
            ui=[arb(0) for _ in range(65)];vr=[arb(0) for _ in range(65)]
            vr[32]=physical[32]
            for j in range(1,33):
                ui[32+j]=-physical[j-1]/2;ui[32-j]=physical[j-1]/2
                vr[32+j]=vr[32-j]=physical[32+j]/2
            u2=[-x for x in convolution(ui,ui)];v2=convolution(vr,vr)
            S=[x+vals["K"]*y for x,y in zip(u2,v2)]
            bs=up(vals["beta"]);ks=up(vals["K"])
            row_bounds={"a_lower":amin,"a_upper":amax,"k_lower":kval.lower(),
                "k_upper":kval.upper(),"eta_lower":eta_min,"eta_upper":eta_max,
                "eta_inverse":(1/eta_min).upper(),"beta":bs,
                "optical_speed":(eta_max*ks.sqrt()).upper()}
            strips={}
            for width in WIDTHS:
                U=[weighted(physical[:32],frequencies[32][:32],width,j) for j in range(5)]
                V=[weighted(physical[32:],frequencies[32][32:],width,j) for j in range(5)]
                ZU=[weighted(z[:96],frequencies[96][:96],width,j) for j in range(5)]
                ZV=[weighted(z[96:],frequencies[96][96:],width,j) for j in range(5)]
                fullU=[(x+ex(DELTA)*y).upper() for x,y in zip(U,ZU)]
                fullV=[(x+ex(DELTA)*y).upper() for x,y in zip(V,ZV)]
                fee=[]
                for order in range(2):
                    cross=sum((math.comb(order,l)*(U[l]*ZU[order-l]+ks*V[l]*ZV[order-l])
                               for l in range(order+1)),arb(0))
                    square=sum((math.comb(order,l)*(ZU[l]*ZU[order-l]+ks*ZV[l]*ZV[order-l])
                               for l in range(order+1)),arb(0))
                    fee.append((2*ex(DELTA)*cross+ex(DELTA)**2*square).upper())
                D0=(bs*(angular(S,-64,width,nonmean=True,primitive=True)+fee[0]/4)).upper()
                D1=(bs*(angular(S,-64,width,nonmean=True)+fee[0])).upper()
                D2=(bs*(angular(S,-64,width,order=1,nonmean=True)+fee[1])).upper()
                L=[(2*bs*sum((math.comb(j,l)*fullU[l]*fullV[j-l] for l in range(j+1)),arb(0))
                    +bs/2*sum((math.comb(j,l)*fullV[l+1]*fullU[j-l] for l in range(j+1)),arb(0))).upper()
                   for j in range(4)]
                c=(L[0]/(4*eta_min)).upper()
                info=dict(U=fullU,V=fullV,ZU=ZU,ZV=ZV,D0=D0,D1=D1,D2=D2,L=L,c=c,
                    Smean=(up(S[64])+fee[0]).upper())
                if c<1:
                    J0=(1/(4*eta_min*(1-c))).upper()
                    J1=(1/(eta_min*(1-c))).upper()
                    h=[J0]
                    for order in range(4):
                        h.append(((1+sum((math.comb(order,l)*L[order-l]*h[l]
                                           for l in range(order+1)),arb(0)))/eta_min).upper())
                    H=[sum((math.comb(k+1,l)*h[l]**2 for l in range(k+2)),arb(0)).sqrt().upper()
                       for k in range(4)]
                    info.update(J0=J0,J1=J1,one_gain=H,
                        J_Hminus2over3_to_Hplus1over3=H[0],
                        J_Hminus5over3_to_Hminus2over3=power(H[0]*H[1]**2,Q(1,3)).upper())
                strips[str(width)]=info
            item={"interval":[str(a),str(b)],"candidate_and_response_piece":piece,
                "intrinsic_provenance":provenance,"bounds":{k:compact(v) for k,v in row_bounds.items()},
                "strips":{w:{k:([compact(x) for x in v] if isinstance(v,list) else compact(v))
                             for k,v in info.items()} for w,info in strips.items()}}
            report["rows"].append(item);bounds_rows.append((a,b,row_bounds,strips))
            if count%64==0:
                report["accepted_closed_rows"]=len(report["rows"]);report["seconds"]=time.monotonic()-started
                save(args.out,report)
                print(json.dumps({"accepted_closed_rows":len(report["rows"]),"right":str(b),
                                  "seconds":report["seconds"]}),flush=True)
        check("the complete original closed real cover has no missing or reversed row",
            report["rows"][0]["interval"][0]==str(left)
            and report["rows"][-1]["interval"][1]==str(right)
            and all(Q(a["interval"][1])==Q(b["interval"][0])
                    for a,b in zip(report["rows"],report["rows"][1:])))
        for piece in range(base.first+1,base.last):
            r=base.nodes[piece]
            if not left<r<right: continue
            entry={"radial":str(r),"left_piece":piece-1,"right_piece":piece,
                   "convention":"right minus left in the same physical moving coordinate",
                   "corrected_value_jump":"exactly zero by the complete original repair identities",
                   "base_and_direction_repairs_have_zero_open_piece_radial_derivatives":True,
                   "radial_derivatives":{}}
            for derivative in (1,2,3):
                bl=base.endpoint(piece-1,r,derivative);br=base.endpoint(piece,r,derivative)
                zl=response.endpoint(piece-1,r,derivative);zr=response.endpoint(piece,r,derivative)
                bj=[alpha*(y-x) for x,y in zip(bl,br)];zj=[y-x for x,y in zip(zl,zr)]
                raw=json.dumps({"base":list(map(str,bj)),"direction":list(map(str,zj))},
                               sort_keys=True,separators=(",",":")).encode()
                norms={}
                for width in WIDTHS:
                    norms[str(width)]={}
                    for order in range(3):
                        value=weighted(list(map(ex,bj)),frequencies[32],width,order)
                        value+=ex(DELTA)*weighted(list(map(ex,zj)),frequencies[96],width,order)
                        norms[str(width)][str(order)]=compact(value.upper())
                entry["radial_derivatives"][str(derivative)]={
                    "complete_exact_component_jump_sha256":digest(raw),
                    "base_components":65,"direction_components":193,
                    "base_even_mean_jump_exact":str(bj[32]),
                    "direction_even_mean_jump_exact":str(zj[96]),
                    "full_complex_family_pair_angular_norms":norms}
            report["seams"].append(entry)
        check("every original interior seam and all nonzero radial derivative sources are retained",
            len(report["seams"])==sum(left<r<right for r in base.radial)
            and all(entry["radial"] not in list(map(str,roots)) for entry in report["seams"]))
        for radius in RADII:
            cl,cr=rlo-radius,rhi+radius
            selected=[z for z in bounds_rows if z[0]>=cl and z[1]<=cr]
            if not selected or selected[0][0]!=cl or selected[-1][1]!=cr:
                raise ValueError("a proposed radius lacks its complete original row cover")
            length=ex(radius+rhi-rlo)
            amin=min(z[2]["a_lower"] for z in selected).lower()
            amax=maximum(z[2]["a_upper"] for z in selected)
            kmin=min(z[2]["k_lower"] for z in selected).lower()
            kmax=maximum(z[2]["k_upper"] for z in selected)
            etamin=min(z[2]["eta_lower"] for z in selected).lower()
            etamax=maximum(z[2]["eta_upper"] for z in selected)
            D=[maximum(z[3]["1/16"]["D"+str(j)] for z in selected) for j in range(3)]
            omin=sum((ex(min(b,rhi)-a)*bounds["optical_speed"]
                      for a,b,bounds,_ in selected if a<rhi),arb(0)).upper()
            oplus=sum((ex(b-max(a,rlo))*bounds["optical_speed"]
                       for a,b,bounds,_ in selected if b>rlo),arb(0)).upper()
            ray=(D[0]*length+max(omin,oplus)).upper()
            E1=(D[1]*length).exp().upper();j=(E1-1).upper()
            Am=(amin-amax*j).lower();Ap=(amax*E1).upper()
            values={"a_lower":amin,"a_upper":amax,"k_lower":kmin,"k_upper":kmax,
                "eta_lower":etamin,"eta_upper":etamax,"D0":D[0],"D1":D[1],"D2":D[2],
                "negative_optical_integral":omin,"positive_optical_integral":oplus,
                "whole_ray_displacement":ray,"angular_Jacobian_fee":j,
                "A_lower":Am,"A_upper":Ap}
            checks={"complete_complex_characteristics_fit_old_angle_loss":bool(ray<ex(Q(1,32))),
                    "both_ray_Jacobians_remain_close":bool(j<ex(Q(1,8))),
                    "divided_phase_positive_real_part":bool(Am>0)}
            if Am>0:
                BA=(ex(Q(3,5))*amax*D[2]*length*(4*D[1]*length).exp()).upper()
                BT=(ex(Q(2,5))*amax*D[2]*power(Am,Q(-1,3))*length**2*(4*D[1]*length).exp()).upper()
                Tmax=(length*power(Ap,Q(2,3))).upper()
                gap=(1-2*j-j*j-Tmax*BT*BT).lower()
                jac=(amin*power(Ap,Q(-1,3))*gap).lower()
                mu=(amin**2*power(Ap,Q(-2,3))*gap).lower()
                Xdisp=(D[0]*length+amax**2*D[2]*length**4*(4*D[1]*length).exp()/10).upper()
                image=(ex(radius)*power(Am,Q(2,3))).lower()
                sexp=maximum(2*z[2]["beta"]*z[3]["1/16"]["Smean"]*length for z in selected)
                E=sexp.exp().upper()
                G=(power(kmax/etamin,Q(1,6))*power(Ap,Q(1,6))*power(kmin,Q(-1,4))*E).upper()
                Gi=(power(etamax/kmin,Q(1,6))*power(Am,Q(-1,6))*power(kmax,Q(1,4))*E).upper()
                branch=(G*(1+j)**2).upper()
                branchi=(Gi/(1-j)**2).upper() if j<1 else arb("+inf")
                b_over_T2=(ex(Q(4,5))*G*(1+j)*amax*D[2]*power(Am,Q(-5,3))
                           *(4*D[1]*length).exp()).upper()
                C=(amax*power(Am,Q(-1,3))*(1+j+Tmax.sqrt()*BT)).upper()
                values.update(A_phi=BA,T_phi=BT,T_upper=Tmax,fold_noncharacteristic_gap=gap,
                    Jacobian_abs_lower=jac,principal_mu_abs_lower=mu,average_X_displacement=Xdisp,
                    guaranteed_real_canonical_half_width=image,leading_E_and_inverse=E,
                    leading_G=G,leading_G_inverse=Gi,leading_branch=branch,leading_branch_inverse=branchi,
                    leading_b0_divided_by_T_squared=b_over_T2,
                    forced_transport_C=C,forced_Fa_root_to_point_factor=(C*branchi*length/2).upper(),
                    forced_Fb_root_to_point_factor=(C*branchi*length.sqrt()*power(Am,Q(-1,3))).upper())
                checks.update(fold_gap_exceeds_three_quarters=bool(gap>ex(Q(3,4))),
                    true_fold_Jacobian_and_principal_scalar_separated=bool(jac>0 and mu>0))
            for width in ("1/32","1/64"):
                c=maximum(z[3][width]["c"] for z in selected)
                values["J_c_"+width]=c
                checks["complete_old_circle_inverse_"+width]=bool(c<ex(Q(3,4)))
                if c<1:
                    for key in ("J0","J1","J_Hminus2over3_to_Hplus1over3","J_Hminus5over3_to_Hminus2over3"):
                        values[key+"_"+width]=maximum(z[3][width][key] for z in selected)
            seamselected=[s for s in report["seams"] if cl<Q(s["radial"])<cr]
            seam_totals={}
            for d in ("1","2","3"):
                seam_totals[d]={}
                for width in ("1/32","1/64"):
                    seam_totals[d][width]={str(order):rec(sum(
                        (box(s["radial_derivatives"][d]["full_complex_family_pair_angular_norms"][width][str(order)])
                         for s in seamselected),arb(0)).upper()) for order in range(3)}
            passed=all(checks.values())
            report["cases"].append({"exact_radius":str(radius),"exact_radial_cover":[str(cl),str(cr)],
                "complete_original_rows":len(selected),"true_original_seams":len(seamselected),
                "passed":passed,"gates":[{"name":k,"passed":v} for k,v in checks.items()],
                "bounds":{k:rec(v) for k,v in values.items()},
                "complete_coefficient_derivative_seam_sums":seam_totals,
                "next_amplitude_and_reconstructed_state_seam_norms_claimed":False})
        successful=[c for c in report["cases"] if c["passed"]]
        check("at least one genuinely larger radius of at least1over200 passes every stated complete gate",
              any(Q(c["exact_radius"])>=Q(1,200) for c in successful))
        chosen=max(successful,key=lambda c:Q(c["exact_radius"]))
        report.update(selected=chosen,all_proposed_radii_passed=all(c["passed"] for c in report["cases"]),
            exact_root_interval=list(map(str,roots)),exact_cover=[str(left),str(right)],
            original_negative_scalar_cells=scalar_count,original_positive_rows=4650,
            accepted_closed_rows=len(report["rows"]),complete_original_seams=len(report["seams"]),
            old_coefficient_width="1/16",old_characteristic_output_width="1/32",
            certified_original_circle_inverse_widths=["1/32","1/64"],
            complete=True,proved=True)
    except Exception as exc:
        report["failure"]={"type":type(exc).__name__,"message":str(exc)}
        report["seconds"]=time.monotonic()-started;save(args.out,report);raise
    report["seconds"]=time.monotonic()-started;save(args.out,report)
    print(json.dumps({"complete":True,"gates":len(report["gates"]),
        "selected_radius":report["selected"]["exact_radius"],
        "closed_rows":report["accepted_closed_rows"],"true_seams":report["complete_original_seams"],
        "seconds":report["seconds"]}),flush=True)

if __name__=="__main__": main()
