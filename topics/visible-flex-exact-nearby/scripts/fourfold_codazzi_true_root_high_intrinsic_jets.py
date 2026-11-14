#!/usr/bin/env python3
"""New true-root intrinsic jets; reuse every completed auxiliary error domain.

One new finite root evaluation returns F0..11, E0..10 and K/beta/gamma/s0..9.
The infinite errors use only complete original auxiliary errors and Cauchy.
Every accepted finite array, error, mean product and scalar jet is checkpointed.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,math,os,sys,time
from fractions import Fraction as Q
from pathlib import Path
import numpy as np
import flint
from flint import acb,arb,ctx
from fourfold_codazzi_cubic_target_jets import CubicCodazziTarget
from fourfold_codazzi_high_target_jets import trig_derivatives,derivative_product
from fourfold_phase_beta_bulk_box import CBox,Box,zeros,cstack,cdot,reduce_box

PUBLIC="Rogerhu12/math-research-public"
COUNT=12
ORDERS=10
OBJECT="91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848"
ROOT="397f9b428c787823994f8c849ad7d1f9209220c3c6e8907b38be562b3cbc9864"
AUX="6276b4b8bd117b3092ce633b7164ff99968100f10b09cbaef8850d4c03f6b24f"
AUX_SOURCE="70f848effb2e57c64b2c9e8100d6ac0af01968c13c939a4874c6f44b0a759d21"
AUX_PROCESS="a6783642ae2c49f66c3a7b54f1506389f24771790f3bd5a324646df8229f9728"
RADII=(Q(1,10000),Q(1,2000))

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
    p=Path(p);raw=p.read_bytes()
    return json.loads(gzip.decompress(raw) if p.suffix==".gz" else raw)
def save(p,d):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(d,separators=(",",":"),allow_nan=False)+"\n").encode()
    if p.suffix==".gz":raw=gzip.compress(raw,compresslevel=9,mtime=0)
    tmp=p.with_name(p.name+".partial");tmp.write_bytes(raw);tmp.replace(p)
def ex(x):
    x=Q(x);return arb(x.numerator)/x.denominator
def interval(a,b):return ex(a).union(ex(b))
def up(x):return abs(x).upper()
def rec(x):
    x=arb(x)
    if not x.is_finite():raise ValueError("nonfinite new true-root scalar")
    return dict(ball=x.str(48),lower=x.lower().str(48),upper=x.upper().str(48))
def box(v):
    if "lower" in v and "upper" in v:
        return arb(v["lower"]).lower().union(arb(v["upper"]).upper())
    return arb(v["ball"])
def cb(v):return acb(box(v["real"]),box(v["imag"]))
def pack_cbox(v):
    parts={}
    shape=list(v.real.lo.shape)
    for name,p in (("real",v.real),("imag",v.imag)):
        if p.lo.shape!=tuple(shape) or p.hi.shape!=tuple(shape):
            raise ValueError("an original finite array changed shape")
        if not np.isfinite(p.lo).all() or not np.isfinite(p.hi).all() or not np.all(p.lo<=p.hi):
            raise ValueError("nonfinite or reversed original finite endpoints")
        parts[name]=dict(lower=p.lo.tolist(),upper=p.hi.tolist())
    return dict(shape=shape,exact_binary64_endpoints=True,**parts)
def unpack_cbox(v,shape):
    if v.get("exact_binary64_endpoints") is not True or v.get("shape")!=list(shape):
        raise ValueError("an accepted finite point array changed shape or endpoint convention")
    pairs=[]
    for name in ("real","imag"):
        lo=np.asarray(v[name]["lower"],dtype=np.float64)
        hi=np.asarray(v[name]["upper"],dtype=np.float64)
        if lo.shape!=tuple(shape) or hi.shape!=tuple(shape) or not np.isfinite(lo).all() or not np.isfinite(hi).all() or not np.all(lo<=hi):
            raise ValueError("an accepted finite point array lost its exact endpoints")
        pairs.append(Box(lo,hi))
    return CBox(*pairs)
def mul(a,b,n):
    if len(a)<n or len(b)<n:raise ValueError("a required true series coefficient is missing")
    return [sum((a[j]*b[k-j] for j in range(k+1)),arb(0)) for k in range(n)]
def inv(a):
    if a[0].contains(0):raise ValueError("a true-root series denominator meets zero")
    out=[1/a[0]]
    for n in range(1,len(a)):
        out.append(-out[0]*sum((a[j]*out[n-j] for j in range(1,n+1)),arb(0)))
    return out
def diff(a):return [(j+1)*a[j+1] for j in range(len(a)-1)]
def sqrt_series(a):
    if not a[0]>0:raise ValueError("the original positive series branch is unresolved")
    out=[a[0].sqrt()]
    for n in range(1,len(a)):
        out.append((a[n]-sum((out[j]*out[n-j] for j in range(1,n)),arb(0)))/(2*out[0]))
    return out

class RootTwelveJetTarget(CubicCodazziTarget):
    def unit_finite_data(self, radial):
        delta=CBox.from_acb(radial-acb(self.anchor));count=COUNT
        jet=zeros((count,2*self.modes+2))
        for n in range(20,-1,-1):
            jet=jet*delta+cstack([self.scalar_poly[n]]+
                                [j*jet[j-1] for j in range(1,count)])
        beta,vertical=jet[:,:self.modes],jet[:,self.modes:2*self.modes]
        radius,height=jet[:,-2],jet[:,-1]
        self.last_scalar=beta,vertical,radius,height
        sines=self.fast_sines.reshape(1,self.modes,self.nodes)
        b=(beta.reshape(count,self.modes,1)*sines).sum(1)
        g=(vertical.reshape(count,self.modes,1)*sines).sum(1)
        sb,_=trig_derivatives(b);sg,_=trig_derivatives(g)
        shb,_=trig_derivatives(b/2);shg,_=trig_derivatives(g/2)
        cmb=-2*derivative_product(shb,shb);cmg=-2*derivative_product(shg,shg)
        one=zeros((count,self.nodes));one[0]=1
        tangent=cstack([-derivative_product(one+cmg,sb),
                         cmg+cmb+derivative_product(cmg,cmb),sg],-1)
        coefficient=self.fast_fourier.fft(tangent,1)/self.nodes
        primitive=zeros((count,self.nodes,3));n=np.asarray(self.frequency)
        ii=CBox(0.,Box(n.reshape(1,-1)));denominator=Box((1-n*n).reshape(1,-1))
        primitive[:,:,0]=(ii*coefficient[:,:,0]+coefficient[:,:,1])/denominator
        primitive[:,:,1]=(-coefficient[:,:,0]+ii*coefficient[:,:,1])/denominator
        nz=np.flatnonzero(n)
        primitive[:,nz,2]=coefficient[:,nz,2]/CBox(0.,Box(n[nz].reshape(1,-1)))
        primitive[:,self.nodes//2,:]=0
        primitive[:,0,1],primitive[:,0,2]=0,0
        pos=np.arange(1,self.nodes//2)
        for component,parity in enumerate((1,-1,1)):
            v=(primitive[:,pos,component]+parity*primitive[:,-pos,component])/2
            primitive[:,pos,component],primitive[:,-pos,component]=v,parity*v
        self.unit_primitive=primitive
        return primitive,radius


    def finite_root_data(self,radial):
        P,_=self.unit_finite_data(radial)
        beta,vertical,a,z=self.last_scalar
        F=[]
        for j in range(COUNT):
            v=sum((math.comb(j,h)*a[j-h]*P[h] for h in range(j+1)),zeros((self.nodes,3)))
            v[0,0],v[0,2]=v[0,0]+a[j],v[0,2]+z[j]
            F.append(v)
        return cstack(F),beta,vertical,a,z

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ("repo-root","manifest","out"):p.add_argument("--"+name,type=Path,required=True)
    p.add_argument("--resume",type=Path)
    a=p.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("new high-root mathematics runs only in public repository Actions")
    import scipy
    runtime=dict(python=".".join(map(str,sys.version_info[:3])),python_flint=flint.__version__,
                 numpy=np.__version__,scipy=scipy.__version__)
    if runtime!=dict(python="3.12.14",python_flint="0.9.0",numpy="2.3.5",scipy="1.17.0"):
        raise RuntimeError("the exact new true-root numerical environment changed")
    if a.out.exists():raise FileExistsError("preserve each real outcome and accepted point prefix")
    ctx.prec=320;ctx.cap=4;start=time.monotonic()
    doc=dict(kind="actual_true_root_complete_intrinsic_jets_through_nine_v1",
        complete=False,proved=False,failure=None,gates=[],
        public_repository=PUBLIC,source_sha256=sha(__file__),
        input_manifest_sha256=sha(a.manifest),runtime=runtime,
        run_id=os.environ.get("GITHUB_RUN_ID"),run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        object_sha256=OBJECT,root_germ_sha256=ROOT,auxiliary_native_sha256=AUX,
        auxiliary_process_sha256=AUX_PROCESS,
        actual_intrinsic_parameter="eta_0",
        other_intrinsic_parameters_given_the_same_true_root=False,
        complete_intrinsic_delta_independence_only_on_original_bump_zero_germ=True,
        original_completed_auxiliary_domains_recomputed=0,original_infinite_tail_evaluations_recomputed=0,
        original_65_or_193_cubic_domains_recomputed=0,
        new_true_root_finite_evaluations=0,reused_true_root_finite_evaluations=0,
        new_complete_error_orders=0,reused_complete_error_orders=0,
        new_mean_products=0,reused_mean_products=0,new_energy_orders=0,reused_energy_orders=0,
        new_intrinsic_series_stages=0,reused_intrinsic_series_stages=0,
        finite_primitive_derivative_count=COUNT,energy_derivative_count=COUNT-1,
        ordinary_intrinsic_derivative_count=ORDERS,
        complete_errors=[],finite_component_norms=[],mean_products={},energy_jets=[],
        all_original_physical_seams_and_independent_means_retained=True,
        first_correction_root_Taylor_coefficients_paid=False,
        old_circle_I_J_or_independent_even_mean_on_first_correction_paid=False,
        full_strong_return_or_cutoff97_inverse_claimed=False)
    def checkpoint():
        doc["seconds"]=time.monotonic()-start;save(a.out,doc)
    def gate(name,test):
        okay=bool(test);doc["gates"].append(dict(name=name,passed=okay))
        if not okay:raise ValueError("new true-root gate failed: "+name)
    try:
        manifest=read(a.manifest)
        gate("the manifest belongs to the one public topic",manifest["public_repository"]==PUBLIC
            and manifest["mathematical_parameters"]["finite_primitive_derivative_count"]==COUNT
            and manifest["mathematical_parameters"]["ordinary_intrinsic_derivative_count"]==ORDERS)
        for f in manifest["files"]:
            path=a.repo_root/f["path"]
            if not path.is_file() or sha(path)!=f["sha256"] or path.stat().st_size!=f["bytes"]:
                raise ValueError("an exact original mathematical input changed: "+f["path"])
        paths={k:a.repo_root/v for k,v in manifest["input_paths"].items()}
        germ,aux,process=[read(paths[k]) for k in ("root_germ","auxiliary_native","auxiliary_process")]
        gate("the genuine fixed-root and original auxiliary bytes and process are identical",
            sha(paths["object"])==OBJECT and sha(paths["root_germ"])==ROOT
            and sha(paths["auxiliary_native"])==AUX and sha(paths["auxiliary_process"])==AUX_PROCESS
            and germ["complete"] and germ["proved"] and germ["failure"] is None
            and germ["object_sha256"]==OBJECT
            and aux["source_sha256"]==AUX_SOURCE and aux["object_sha256"]==OBJECT
            and aux["root_germ_sha256"]==ROOT and aux["actual_intrinsic_parameter"]=="eta_0"
            and process["native_sha256"]==AUX and process["actual_returncode"]==1
            and process["mathematical_source_sha256"]==AUX_SOURCE
            and aux["complete"] is True and aux["proved"] is False
            and aux["successful_auxiliary_domains"]==["1/10000","1/2000"]
            and len(aux["failed_auxiliary_domains"])==2)
        roots=list(map(Q,germ["root_interval"]))
        scalarcell=list(map(Q,germ["original_scalar_germ"]))
        physicalcell=list(map(Q,germ["exact_candidate_piece_interval"]))
        gate("the original root and fixed parameter have the same scalar germ and zero bump",
            len(roots)==2 and roots[0]<=roots[1]
            and list(map(Q,aux["exact_root_interval"]))==roots
            and list(map(Q,aux["original_scalar_germ"]))==scalarcell
            and aux["exact_intrinsic_affine_center"]==germ["exact_center_parameter"]
            and aux["exact_intrinsic_affine_half_width"]==germ["exact_parameter_half_width"]
            and scalarcell[0]<roots[0]<=roots[1]<scalarcell[1]
            and physicalcell[0]<roots[0]<=roots[1]<physicalcell[1]
            and germ["compact_bump_identically_zero_on_entire_actual_germ"])
        cases=[]
        for radius in RADII:
            c=next(x for x in aux["cases"] if Q(x["exact_auxiliary_radius"])==radius)
            expected=dict(real_interval=[str(roots[0]-radius),str(roots[1]+radius)],
                          imaginary_half_width=str(radius))
            ev=c["complete_complex_intrinsic_evidence"]
            gate("the completed auxiliary error domain "+str(radius)+" retains its complete six jets",
                c["complete"] is True and c["proved"] is True and c["failure"] is None
                and c["intrinsic_evaluation_complete"] is True and c["intrinsic_domain_failure"] is None
                and c["exact_complex_rectangle"]==expected
                and ev["original_complete_primitive_nodes"]==512
                and ev["original_scalar_polynomial_degree_at_most"]==20
                and ev["exact_bilinear_zero_convolution_without_conjugation"] is True
                and len(ev["complete_primitive_radial_errors"])==6
                and len(ev["physical_radius_ordinary_jets"])==6
                and len(ev["radial_metric_ordinary_jets"])==5)
            cases.append((radius,ev))
        doc.update(exact_root_interval=list(map(str,roots)),original_scalar_germ=list(map(str,scalarcell)),
            exact_original_physical_piece_interval=list(map(str,physicalcell)),
            exact_fixed_intrinsic_parameter=germ["exact_center_parameter"],
            original_parameter_half_width_used_for_outward_enclosure=germ["exact_parameter_half_width"],
            consumed_complete_auxiliary_radii=list(map(str,RADII)),
            original_auxiliary_failed_cases_preserved=aux["failed_auxiliary_domains"],
            original_auxiliary_process_returncode=process["actual_returncode"])
        if a.resume:
            prev=read(a.resume)
            keys=("kind","public_repository","source_sha256","input_manifest_sha256","runtime",
                  "object_sha256","root_germ_sha256","auxiliary_native_sha256","auxiliary_process_sha256",
                  "exact_root_interval","original_scalar_germ","exact_fixed_intrinsic_parameter",
                  "original_parameter_half_width_used_for_outward_enclosure",
                  "finite_primitive_derivative_count","energy_derivative_count","ordinary_intrinsic_derivative_count")
            gate("every accepted high-root prefix has the identical source runtime and all immutable inputs",
                 all(prev.get(k)==doc.get(k) for k in keys))
            for key in ("finite_root_stage","complete_errors","finite_component_norms","mean_products",
                        "energy_jets","intrinsic_stage"):
                if key in prev:doc[key]=prev[key]
            doc["original_prefix_audit"]=dict(native_sha256=sha(a.resume),
                native_bytes=a.resume.stat().st_size,run_id=prev.get("run_id"),
                complete=prev.get("complete"),proved=prev.get("proved"),
                failure=prev.get("failure"),all_original_gates=prev.get("gates"))
            checkpoint()
        if doc.get("finite_root_stage",{}).get("complete") is True:
            point=doc["finite_root_stage"];doc["reused_true_root_finite_evaluations"]+=1
        else:
            target=RootTwelveJetTarget(paths["object"],Q(germ["exact_parameter_half_width"]),512,4096)
            target.set_cell(*scalarcell)
            gate("the new finite point keeps the exact original primitive polynomial and parameter box",
                tuple(target.cell)==tuple(scalarcell) and target.nodes==512
                and target.metric_half_width==Q(germ["exact_parameter_half_width"]))
            F,phase,vertical,radius,height=target.finite_root_data(acb(interval(*roots)))
            point=dict(complete=True,exact_evaluation_interval=list(map(str,roots)),
                original_scalar_germ=list(map(str,scalarcell)),nodes=target.nodes,modes=target.modes,
                original_frequency=list(map(int,target.frequency)),
                ordinary_radial_derivatives_not_factorial_normalized=True,
                complete_finite_field_array=pack_cbox(F),
                physical_radius_ordinary_jets=pack_cbox(radius),
                physical_height_ordinary_jets=pack_cbox(height),
                original_scalar_phase_ordinary_jets=pack_cbox(phase),
                original_scalar_vertical_ordinary_jets=pack_cbox(vertical),
                original_infinite_tail_evaluator_called=False,
                original_auxiliary_domain_evaluator_called=False)
            doc["finite_root_stage"]=point;doc["new_true_root_finite_evaluations"]+=1;checkpoint()
        gate("the accepted point is the exact new true-root interval with all twelve finite columns",
            point["complete"] is True and point["exact_evaluation_interval"]==list(map(str,roots))
            and point["original_scalar_germ"]==list(map(str,scalarcell))
            and point["nodes"]==512 and point["ordinary_radial_derivatives_not_factorial_normalized"] is True
            and point["original_infinite_tail_evaluator_called"] is False
            and point["original_auxiliary_domain_evaluator_called"] is False)
        F=unpack_cbox(point["complete_finite_field_array"],(COUNT,512,3))
        radius=unpack_cbox(point["physical_radius_ordinary_jets"],(COUNT,))
        gate("the complete finite Nyquist column is exactly zero",
            all(np.all(part[:,256,:]==0) for part in (F.real.lo,F.real.hi,F.imag.lo,F.imag.hi)))
        aa=[]
        for j in range(COUNT):
            value=radius[j].to_acb()
            if not value.imag.contains(0):raise ValueError("the true real radius derivative lost reality")
            aa.append(value.real)
        doc["physical_radius_ordinary_jets"]=[rec(x) for x in aa]
        if len(doc["complete_errors"])>COUNT or len(doc["finite_component_norms"])>COUNT:
            raise ValueError("an accepted derivative prefix exceeded the exact requested order")
        doc["reused_complete_error_orders"]+=len(doc["complete_errors"])
        for j in range(len(doc["complete_errors"]),COUNT):
            candidates=[]
            for R,ev in cases:
                for k in range(min(j,5)+1):
                    eps=up(box(ev["complete_primitive_radial_errors"][k]))
                    # Each full quotient is evaluated before its upper endpoint is selected.
                    value=(math.factorial(j-k)*eps/ex(R)**(j-k)).upper()
                    candidates.append(dict(auxiliary_radius=str(R),saved_radial_order=k,
                                           new_radial_order=j,bound=rec(value)))
            selected=min(range(len(candidates)),key=lambda k:box(candidates[k]["bound"]).upper())
            value=box(candidates[selected]["bound"]).upper()
            doc["complete_errors"].append(dict(order=j,complete_candidates=candidates,
                selected_candidate_index=selected,complete_error_upper=rec(value)))
            doc["new_complete_error_orders"]+=1;checkpoint()
        for j in range(len(doc["finite_component_norms"]),COUNT):
            value=arb(float(np.max(reduce_box(Box(F[j].magnitude_upper())).hi))).upper()
            doc["finite_component_norms"].append(dict(order=j,value=rec(value)));checkpoint()
        for j,v in enumerate(doc["complete_errors"]):
            if v["order"]!=j or v["selected_candidate_index"]>=len(v["complete_candidates"]):
                raise ValueError("an accepted complete error order changed")
        for j,v in enumerate(doc["finite_component_norms"]):
            if v["order"]!=j:raise ValueError("an accepted finite norm order changed")
        errors=[box(x["complete_error_upper"]).upper() for x in doc["complete_errors"]]
        norms=[box(x["value"]).upper() for x in doc["finite_component_norms"]]
        reverse=(-np.arange(512))%512
        expected_pairs={str(i)+","+str(j) for i in range(1,COUNT) for j in range(i,COUNT)
                        if i+j<=COUNT}
        if not set(doc["mean_products"]).issubset(expected_pairs):
            raise ValueError("an accepted mean prefix has an unrelated pair")
        doc["reused_mean_products"]+=len(doc["mean_products"])
        def mean(i,j):
            i,j=min(i,j),max(i,j);key=str(i)+","+str(j)
            if key not in doc["mean_products"]:
                finite=cdot(F[i],F[j][reverse]).sum().to_acb()
                if not finite.imag.contains(0):raise ValueError("a true-root finite bilinear mean lost reality")
                fee=(3*(norms[i]*errors[j]+norms[j]*errors[i]+errors[i]*errors[j])).upper()
                value=finite.real+arb(0,fee)
                doc["mean_products"][key]=dict(radial_orders=[i,j],finite_real=rec(finite.real),
                    finite_imaginary_zero_enclosed=True,complete_error_fee=rec(fee),value=rec(value))
                doc["new_mean_products"]+=1;checkpoint()
            row=doc["mean_products"][key]
            if row["radial_orders"]!=[i,j] or row["finite_imaginary_zero_enclosed"] is not True:
                raise ValueError("an accepted exact bilinear pair changed its identity")
            return box(row["value"])
        if len(doc["energy_jets"])>COUNT-1:raise ValueError("an accepted energy prefix gained an order")
        doc["reused_energy_orders"]+=len(doc["energy_jets"])
        for k in range(len(doc["energy_jets"]),COUNT-1):
            value=sum((math.comb(k,j)*mean(j+1,k-j+1) for j in range(k+1)),arb(0))
            doc["energy_jets"].append(dict(order=k,value=rec(value)));doc["new_energy_orders"]+=1;checkpoint()
        for k,row in enumerate(doc["energy_jets"]):
            if row["order"]!=k:raise ValueError("an accepted true energy derivative changed order")
        Ej=[box(v["value"]) for v in doc["energy_jets"]]
        gate("the complete true-root energy has all eleven orders and three positive denominator gaps",
            len(Ej)==11 and set(doc["mean_products"])==expected_pairs
            and aa[0]>0 and Ej[0]>0 and Ej[0]-aa[1]*aa[1]>0)
        doc["denominator_gaps"]={k:rec(v.lower()) for k,v in (
            ("radius",aa[0]),("E",Ej[0]),("rotation",Ej[0]-aa[1]*aa[1]))}
        if doc.get("intrinsic_stage",{}).get("complete") is True:
            doc["reused_intrinsic_series_stages"]+=1
        else:
            ar=[v/math.factorial(j) for j,v in enumerate(aa)]
            er=[v/math.factorial(j) for j,v in enumerate(Ej)]
            ia,ie=inv(ar),inv(er)
            first=mul(mul(diff(diff(ar)),ia,ORDERS),ie,ORDERS)
            second=mul(mul(mul(mul(diff(ar),diff(er),ORDERS),ia,ORDERS),ie,ORDERS),ie,ORDERS)
            curvature=[-first[j]+second[j]/2 for j in range(ORDERS)]
            beta=mul(diff(ar),ia,ORDERS)
            gamma=mul(sqrt_series(er),ia,ORDERS)
            slope=diff(ar);square_slope=mul(slope,slope,ORDERS)
            gap=[er[j]-square_slope[j] for j in range(ORDERS)]
            rotation=[-v for v in mul(ar,sqrt_series(mul(er,inv(gap),ORDERS)),ORDERS)]
            jets={name:[math.factorial(j)*jet[j] for j in range(ORDERS)]
                for name,jet in (("K",curvature),("beta",beta),("gamma",gamma),("s",rotation))}
            doc["intrinsic_stage"]=dict(complete=True,
                ordinary_old_radial_jets={k:[rec(v) for v in values] for k,values in jets.items()},
                complete_primitive_and_product_errors_included=True,
                missing_series_coefficients_padded_with_zero=False)
            doc["new_intrinsic_series_stages"]+=1;checkpoint()
        stage=doc["intrinsic_stage"]
        gate("all four intrinsic rows have ten complete ordinary derivative columns",
            stage["complete"] is True and stage["complete_primitive_and_product_errors_included"] is True
            and stage["missing_series_coefficients_padded_with_zero"] is False
            and set(stage["ordinary_old_radial_jets"])=={"K","beta","gamma","s"}
            and all(len(v)==ORDERS for v in stage["ordinary_old_radial_jets"].values()))
        jets={k:[box(v) for v in values] for k,values in stage["ordinary_old_radial_jets"].items()}
        gate("the new true-root balls retain zero curvature and the original simple-root branches",
            jets["K"][0].contains(0) and jets["K"][1]>0 and jets["gamma"][0]>0 and jets["s"][0]<0)
        comparisons=[]
        for R,ev in cases:
            for name,values in jets.items():
                for j in range(4):
                    old=cb(ev["ordinary_intrinsic_jets"][name][j])
                    okay=old.imag.contains(0) and old.real.overlaps(values[j])
                    comparisons.append(dict(radius=str(R),name=name,ordinary_order=j,overlap=bool(okay)))
            for j in range(5):
                old=cb(ev["radial_metric_ordinary_jets"][j])
                comparisons.append(dict(radius=str(R),name="E",ordinary_order=j,
                    overlap=bool(old.imag.contains(0) and old.real.overlaps(Ej[j]))))
            for j in range(6):
                old=cb(ev["physical_radius_ordinary_jets"][j])
                comparisons.append(dict(radius=str(R),name="physical_radius",ordinary_order=j,
                    overlap=bool(old.imag.contains(0) and old.real.overlaps(aa[j]))))
        doc["original_low_order_identity_checks"]=comparisons
        gate("new point low orders agree with both original complete auxiliary domains",
             len(comparisons)==54 and all(v["overlap"] for v in comparisons))
        doc["at_the_certified_true_root"]=dict(fixed_intrinsic_parameter="eta_0",
            certified_root_germ_sha256=ROOT,exact_K0="0",raw_new_K0_ball_retained=True,
            other_intrinsic_parameter_roots_claimed=False,
            rho_definition="rho=r_star-r",
            divided_curvature_normalized_rho_coefficients=[
                rec(((-1)**q)*jets["K"][q+1]/math.factorial(q+1)) for q in range(ORDERS-1)])
        gate("all accepted new stages and original nonclaims are retained",
             len(doc["complete_errors"])==COUNT and len(doc["finite_component_norms"])==COUNT
             and doc["original_completed_auxiliary_domains_recomputed"]==0
             and doc["original_infinite_tail_evaluations_recomputed"]==0
             and doc["original_65_or_193_cubic_domains_recomputed"]==0
             and not doc["full_strong_return_or_cutoff97_inverse_claimed"])
        doc["complete"]=True;doc["proved"]=True
    except BaseException as error:
        doc["failure"]=dict(type=type(error).__name__,message=str(error));raise
    finally:
        checkpoint()
        print(json.dumps(dict(complete=doc["complete"],proved=doc["proved"],failure=doc["failure"],
            new_finite_root_evaluations=doc["new_true_root_finite_evaluations"],
            reused_finite_root_evaluations=doc["reused_true_root_finite_evaluations"],
            accepted_energy_orders=len(doc["energy_jets"]),native_sha256=sha(a.out),
            seconds=doc["seconds"]),allow_nan=False),flush=True)
if __name__=="__main__":main()
