#!/usr/bin/env python3
"""Append only the six missing true-root finite columns and intrinsic10..15.

All old successful arrays and scalar records remain unchanged. Supporting
arrays are saved as natural stages. New mathematics runs only in public Actions.
"""
from __future__ import annotations
import argparse,copy,gzip,hashlib,json,math,os,shutil,sys,time
from fractions import Fraction as Q
from pathlib import Path
import flint,numpy as np
from flint import acb,arb,ctx
from fourfold_codazzi_cubic_target_jets import CubicCodazziTarget
from fourfold_codazzi_high_target_jets import trig_derivatives,derivative_product
from fourfold_phase_beta_bulk_box import CBox,Box,zeros,cstack,cdot,reduce_box,DirectedFFT
import fourfold_codazzi_true_root_high_intrinsic_jets_v2 as old

PUBLIC="Rogerhu12/math-research-public"
COUNT=18
ORDERS=16
OLD_COUNT=12
OLD_ORDERS=10
HIGH="38a8ba8d2998a75ddb863fe9b486defd756a22488e1c3a96ed8bf54581877e8f"
HPROC="3b06c881b8b00f8bb830653b3eb290b09687b0a2576320b605ba758e2e706abe"
HSOURCE="c3bb77f96f05ceedd05a0fc4cda39d591065d4ee2203fd7b05be79169d04709d"
HMANIFEST="36ed4257fae6afb0170fa937c044bece1a55db0e5a0e4c1036035b9135e68ac5"
CONTRACT="ae0e26fd6a18b2d11e0429a0ad516f160618c41267047ab88f231a33dbb2d6e4"
sha,read,ex,interval,up,rec,box=old.sha,old.read,old.ex,old.interval,old.up,old.rec,old.box
pack,unpack,payload_sha=old.pack_cbox,old.unpack_cbox,old.payload_sha
mul,inv,diff,sqrt_series=old.mul,old.inv,old.diff,old.sqrt_series

def save(path,value):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(value,separators=(",",":"),allow_nan=False)+"\n").encode()
    if path.suffix==".gz":raw=gzip.compress(raw,compresslevel=6,mtime=0)
    temporary=path.with_name(path.name+".partial")
    temporary.write_bytes(raw);temporary.replace(path)

def czeros(v):
    return bool(np.all(v.real.lo<=0) and np.all(v.real.hi>=0)
        and np.all(v.imag.lo<=0) and np.all(v.imag.hi>=0))

def exact_finite_view(value):
    if not czeros(value[256,:]):
        raise ValueError("an exact finite Nyquist zero is absent from its raw enclosure")
    value[256,:]=0
    return value

def structural_unit(value):
    if not (czeros(value[256,:]) and czeros(value[0,1]) and czeros(value[0,2])):
        raise ValueError("an original unit-primitive zero identity lost its enclosure")
    value[256,:]=0;value[0,1]=0;value[0,2]=0
    pos=np.arange(1,256)
    for component,parity in enumerate((1,-1,1)):
        combined=(value[pos,component]+parity*value[-pos,component])/2
        value[pos,component],value[-pos,component]=combined,parity*combined
    return value

def coef(a,b,n):
    if len(a)<=n or len(b)<=n:
        raise ValueError("an unpaid series coefficient would be padded with zero")
    return sum((a[j]*b[n-j] for j in range(n+1)),arb(0))

def derivative_coefficient(a,b,n):
    if len(a.real.lo)<=n or len(b.real.lo)<=n:
        raise ValueError("an ordinary product lost a required derivative")
    return sum((math.comb(n,j)*a[j]*b[n-j] for j in range(n+1)),CBox(0.))

def scalar_real(value):
    z=value.to_acb()
    if not z.imag.contains(0):
        raise ValueError("an original real scalar derivative lost reality")
    return z.real

class SupportingGermOnly(CubicCodazziTarget):
    def forbidden(self,*args,**kwargs):
        raise RuntimeError("a completed target finite FFT or infinite-tail evaluator must not run")
    unit_finite_data=forbidden
    finite_data=forbidden
    finite_root_data=forbidden
    scalar_jets_and_fourier=forbidden
    coefficients=forbidden
    complete_data=forbidden
    complete_fast_data=forbidden
    tail_errors=forbidden
    unit_tail_errors=forbidden
    fast_fields=forbidden
    fast_density=forbidden
    exact_initial_C_polynomials=forbidden

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ("repo-root","manifest","out"):
        parser.add_argument("--"+name,type=Path,required=True)
    parser.add_argument("--resume",type=Path)
    args=parser.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("new mathematics runs only in this public repository Actions")
    import scipy
    runtime=dict(python=".".join(map(str,sys.version_info[:3])),python_flint=flint.__version__,
        numpy=np.__version__,scipy=scipy.__version__)
    if runtime!=dict(python="3.12.14",python_flint="0.9.0",numpy="2.3.5",scipy="1.17.0"):
        raise RuntimeError("the exact original numerical runtime changed")
    if args.out.exists():
        raise FileExistsError("preserve every accepted or failed original native")
    ctx.prec=320;ctx.cap=4;started=time.monotonic()
    doc=dict(kind="append_only_complete_true_root_intrinsic_orders_through_fifteen",
        public_repository=PUBLIC,source_sha256=sha(__file__),
        input_manifest_sha256=sha(args.manifest),runtime=runtime,
        run_id=os.environ.get("GITHUB_RUN_ID"),run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        original_high_native_sha256=HIGH,original_high_process_sha256=HPROC,
        original_high_source_sha256=HSOURCE,original_high_manifest_sha256=HMANIFEST,
        object_sha256=old.OBJECT,root_germ_sha256=old.ROOT,
        auxiliary_native_sha256=old.AUX,auxiliary_process_sha256=old.AUX_PROCESS,
        contract_sha256=CONTRACT,actual_intrinsic_parameter="eta_0",
        finite_primitive_derivative_count=COUNT,energy_derivative_count=COUNT-1,
        ordinary_intrinsic_derivative_count=ORDERS,
        complete=False,proved=False,failure=None,gates=[],stages={},
        new_scalar_rows=[],new_finite_columns=[],new_intrinsic_orders=[],
        new_supporting_stages=0,reused_supporting_stages=0,
        new_scalar_derivative_rows=0,new_finite_Fourier_columns=0,
        new_finite_primitive_columns=0,new_complete_error_orders=0,
        new_finite_component_norms=0,new_mean_products=0,new_energy_orders=0,
        new_intrinsic_derivative_values=0,
        original_successful_finite_columns_recomputed=0,
        original_successful_scalar_derivatives_recomputed=0,
        original_successful_error_or_mean_or_energy_or_intrinsic_rows_recomputed=0,
        original_successful_auxiliary_domains_recomputed=0,
        original_infinite_tail_evaluator_calls=0,
        exact_original_finite_point_and_low_order_records_preserved=False,
        higher_Airy_Taylor_coefficients_computed=False,
        smaller_Taylor_remainder_strong_return_or_full_inverse_claimed=False,
        all_original_physical_seams_and_independent_means_retained=True)
    def checkpoint():
        doc["seconds"]=time.monotonic()-started;save(args.out,doc)
    def gate(name,test):
        passed=bool(test);doc["gates"].append(dict(name=name,passed=passed))
        if not passed:raise ValueError("append-only high-root gate failed: "+name)
    def stage(name,builder):
        if name in doc["stages"]:
            entry=doc["stages"][name];path=args.out.parent/entry["file"]
            if not path.is_file() or path.stat().st_size!=entry["bytes"] or sha(path)!=entry["sha256"]:
                raise ValueError("an accepted natural supporting stage changed bytes")
            value=read(path)
            if not (value["complete"] and value["name"]==name
                and value["source_sha256"]==doc["source_sha256"]
                and value["input_manifest_sha256"]==doc["input_manifest_sha256"]
                and value["original_high_native_sha256"]==HIGH
                and value["payload_sha256"]==payload_sha(value["payload"])):
                raise ValueError("an accepted supporting stage changed identity")
            doc["reused_supporting_stages"]+=1
            return value["payload"]
        doc["last_attempted_stage"]=name;checkpoint()
        payload=builder()
        value=dict(name=name,complete=True,source_sha256=doc["source_sha256"],
            input_manifest_sha256=doc["input_manifest_sha256"],original_high_native_sha256=HIGH,
            payload=payload,payload_sha256=payload_sha(payload))
        path=args.out.parent/"stages"/(name+".json.gz");save(path,value)
        doc["stages"][name]=dict(file=str(path.relative_to(args.out.parent)),
            bytes=path.stat().st_size,sha256=sha(path),payload_sha256=value["payload_sha256"])
        doc["new_supporting_stages"]+=1;doc.pop("last_attempted_stage",None);checkpoint()
        return payload
    try:
        manifest=read(args.manifest)
        gate("the exact manifest describes only the six missing finite columns and intrinsic10..15",
            manifest["public_repository"]==PUBLIC
            and manifest["mathematical_parameters"]["finite_primitive_derivative_count"]==COUNT
            and manifest["mathematical_parameters"]["ordinary_intrinsic_derivative_count"]==ORDERS
            and manifest["mathematical_parameters"]["new_finite_orders"]==list(range(12,18)))
        for item in manifest["files"]:
            path=args.repo_root/item["path"]
            if not path.is_file() or sha(path)!=item["sha256"] or path.stat().st_size!=item["bytes"]:
                raise ValueError("an immutable complete mathematical input changed: "+item["path"])
        paths={k:args.repo_root/v for k,v in manifest["input_paths"].items()}
        original,process=[read(paths[k]) for k in ("complete_high_native","complete_high_process")]
        germ,aux,aproc=[read(paths[k]) for k in ("root_germ","auxiliary_native","auxiliary_process")]
        gate("the original complete high native retains its actual zero return and all15 gates",
            sha(paths["complete_high_native"])==HIGH and sha(paths["complete_high_process"])==HPROC
            and sha(paths["complete_high_source"])==HSOURCE and sha(paths["complete_high_manifest"])==HMANIFEST
            and original["complete"] and original["proved"] and original["failure"] is None
            and original["source_sha256"]==process["mathematical_source_sha256"]==HSOURCE
            and original["input_manifest_sha256"]==process["manifest_sha256"]==HMANIFEST
            and process["actual_returncode"]==0 and process["native_sha256"]==HIGH
            and process["native_bytes"]==paths["complete_high_native"].stat().st_size
            and len(original["gates"])==15 and all(g["passed"] for g in original["gates"])
            and process["mathematical_gates"]==original["gates"])
        roots=list(map(Q,germ["root_interval"]))
        scalarcell=list(map(Q,germ["original_scalar_germ"]))
        gate("the same fixed true-root germ object parameter and two complete auxiliary errors are retained",
            sha(paths["object"])==old.OBJECT and sha(paths["root_germ"])==old.ROOT
            and sha(paths["auxiliary_native"])==old.AUX and sha(paths["auxiliary_process"])==old.AUX_PROCESS
            and sha(paths["append_contract"])==CONTRACT
            and original["exact_root_interval"]==germ["root_interval"]==aux["exact_root_interval"]
            and original["original_scalar_germ"]==germ["original_scalar_germ"]
            and original["exact_fixed_intrinsic_parameter"]==germ["exact_center_parameter"]
            and original["original_parameter_half_width_used_for_outward_enclosure"]
                ==germ["exact_parameter_half_width"]
            and germ["complete"] and germ["proved"] and germ["failure"] is None
            and germ["compact_bump_identically_zero_on_entire_actual_germ"]
            and aux["successful_auxiliary_domains"]==["1/10000","1/2000"]
            and aproc["actual_returncode"]==1 and aproc["native_sha256"]==old.AUX)
        point=original["finite_root_stage"]
        gate("all old successful finite scalar and intrinsic records have the required complete dimensions",
            point["complete"] and point["nodes"]==512
            and point["exact_evaluation_interval"]==list(map(str,roots))
            and point["ordinary_radial_derivatives_not_factorial_normalized"]
            and point["original_scalar_germ"]==list(map(str,scalarcell))
            and len(original["complete_errors"])==12 and len(original["finite_component_norms"])==12
            and len(original["mean_products"])==36 and len(original["energy_jets"])==11
            and original["intrinsic_stage"]["complete"]
            and all(len(v)==10 for v in original["intrinsic_stage"]["ordinary_old_radial_jets"].values())
            and len(original["original_low_order_identity_checks"])==54
            and all(v["overlap"] for v in original["original_low_order_identity_checks"]))
        inherited=("finite_root_stage","complete_errors","finite_component_norms","mean_products",
            "energy_jets","physical_radius_ordinary_jets","denominator_gaps",
            "original_low_order_identity_checks","at_the_certified_true_root")
        for key in inherited:doc[key]=copy.deepcopy(original[key])
        doc["original_intrinsic_stage"]=copy.deepcopy(original["intrinsic_stage"])
        doc["intrinsic_stage"]=copy.deepcopy(original["intrinsic_stage"])
        doc["intrinsic_stage"]["complete"]=False
        doc["original_reference_payload_hashes"]={k:payload_sha(original[k]) for k in inherited}
        doc["original_reference_payload_hashes"]["intrinsic_stage"]=payload_sha(original["intrinsic_stage"])
        doc.update(exact_root_interval=original["exact_root_interval"],
            original_scalar_germ=original["original_scalar_germ"],
            exact_original_physical_piece_interval=original["exact_original_physical_piece_interval"],
            exact_fixed_intrinsic_parameter=original["exact_fixed_intrinsic_parameter"],
            original_parameter_half_width_used_for_outward_enclosure=original["original_parameter_half_width_used_for_outward_enclosure"],
            original_finite_point_payload_sha256=payload_sha(point),
            original_comparison_record_payload_sha256=payload_sha(original["original_low_order_identity_checks"]),
            original_failed_auxiliary_cases_preserved=copy.deepcopy(aux["failed_auxiliary_domains"]),
            original_high_gates=copy.deepcopy(original["gates"]))
        if args.resume:
            previous=read(args.resume)
            keys=("kind","public_repository","source_sha256","input_manifest_sha256","runtime",
                "original_high_native_sha256","original_high_process_sha256",
                "object_sha256","root_germ_sha256","auxiliary_native_sha256",
                "auxiliary_process_sha256","contract_sha256","exact_root_interval",
                "original_scalar_germ","exact_fixed_intrinsic_parameter",
                "original_parameter_half_width_used_for_outward_enclosure",
                "original_reference_payload_hashes","finite_primitive_derivative_count",
                "ordinary_intrinsic_derivative_count")
            gate("every accepted new prefix has the exact same source runtime manifest and original successful records",
                all(previous.get(k)==doc.get(k) for k in keys))
            for name,entry in previous["stages"].items():
                relative=Path(entry["file"])
                if relative.is_absolute() or ".." in relative.parts or relative.parts[0]!="stages":
                    raise ValueError("an accepted stage leaves its natural directory")
                source=args.resume.parent/relative;destination=args.out.parent/relative
                if not source.is_file() or sha(source)!=entry["sha256"] or source.stat().st_size!=entry["bytes"]:
                    raise ValueError("a resumed natural stage differs from its complete original")
                destination.parent.mkdir(parents=True,exist_ok=True)
                if destination.exists():raise FileExistsError("do not overwrite a previous mathematical stage")
                shutil.copyfile(source,destination)
            for key in ("stages","new_scalar_rows","new_finite_columns","new_intrinsic_orders",
                "complete_errors","finite_component_norms","mean_products","energy_jets",
                "physical_radius_ordinary_jets","intrinsic_stage","at_the_certified_true_root"):
                doc[key]=copy.deepcopy(previous[key])
            doc["preserved_actual_prefix"]=dict(native_sha256=sha(args.resume),
                native_bytes=args.resume.stat().st_size,run_id=previous.get("run_id"),
                complete=previous["complete"],proved=previous["proved"],
                failure=previous["failure"],gates=previous["gates"])
        checkpoint()
        N=512;modes=point["modes"]
        F0=unpack(point["complete_finite_field_array"],(12,N,3))
        oldphase=unpack(point["original_scalar_phase_ordinary_jets"],(12,modes))
        oldvertical=unpack(point["original_scalar_vertical_ordinary_jets"],(12,modes))
        olda=unpack(point["physical_radius_ordinary_jets"],(12,))
        oldz=unpack(point["physical_height_ordinary_jets"],(12,))
        finite=[exact_finite_view(F0[j]) for j in range(12)]
        def germ_support():
            target=SupportingGermOnly(paths["object"],Q(germ["exact_parameter_half_width"]),512,4096)
            target.set_cell(*scalarcell)
            if not (tuple(target.cell)==tuple(scalarcell) and target.nodes==512
                and target.modes==modes and list(map(int,target.frequency))==point["original_frequency"]
                and target.metric_half_width==Q(germ["exact_parameter_half_width"])):
                raise ValueError("the unsaved scalar germ support changed the original finite object")
            if target.fast_fourier.cache or target.fourier.cache or target.polynomial_fft.cache:
                raise ValueError("a supporting constructor unexpectedly performed an old Fourier evaluation")
            return dict(scalar_polynomial=pack(target.scalar_poly),fast_sines=pack(target.fast_sines),
                scalar_anchor_real=rec(target.anchor),original_frequency=point["original_frequency"],
                nodes=512,modes=modes,scalar_polynomial_degree_at_most=20,
                old_target_or_primitive_or_infinite_tail_called=False)
        support=stage("same-scalar-germ-and-angle-grid",germ_support)
        poly=unpack(support["scalar_polynomial"],(21,2*modes+2))
        sines=unpack(support["fast_sines"],(modes,512))
        delta=CBox.from_acb(acb(interval(*roots))-acb(box(support["scalar_anchor_real"])))
        if len(doc["new_scalar_rows"])>6:
            raise ValueError("a scalar extension prefix exceeds its six new orders")
        for j in range(12+len(doc["new_scalar_rows"]),18):
            value=zeros((2*modes+2,))
            for k in range(20,j-1,-1):
                factor=math.factorial(k)//math.factorial(k-j)
                exact_multiplier=CBox.from_acb(acb(ex(Q(factor))))
                value=value*delta+exact_multiplier*poly[k]
            doc["new_scalar_rows"].append(dict(order=j,values=pack(value)))
            doc["new_scalar_derivative_rows"]+=1;checkpoint()
        if any(row["order"]!=12+i for i,row in enumerate(doc["new_scalar_rows"])):
            raise ValueError("an accepted new scalar row changed derivative order")
        added=[unpack(row["values"],(2*modes+2,)) for row in doc["new_scalar_rows"]]
        phase=cstack([oldphase[j] for j in range(12)]+[v[:modes] for v in added])
        vertical=cstack([oldvertical[j] for j in range(12)]+[v[modes:2*modes] for v in added])
        a=cstack([olda[j] for j in range(12)]+[v[-2] for v in added])
        z=cstack([oldz[j] for j in range(12)]+[v[-1] for v in added])
        if len(doc["physical_radius_ordinary_jets"])>18:
            raise ValueError("an inherited radius prefix exceeds the requested order")
        for j in range(len(doc["physical_radius_ordinary_jets"]),18):
            doc["physical_radius_ordinary_jets"].append(rec(scalar_real(a[j])));checkpoint()
        aa=[box(v) for v in doc["physical_radius_ordinary_jets"]]
        gate("the original positive radius permits exact triangular unit-primitive recovery",aa[0]>0)
        primitive=[]
        for j in range(12):
            def recover(j=j):
                value=finite[j]
                correction=zeros((N,3));correction[0,0]=a[j];correction[0,2]=z[j]
                for h in range(j):
                    correction=correction+math.comb(j,h)*a[j-h]*primitive[h]
                value=structural_unit((value-correction)/a[0])
                return dict(order=j,unit_primitive=pack(value),no_old_Fourier_transform=True,
                    exact_identity="F_j=sum binomial a_(j-h) P_h+a_j e_x+z_j e_z")
            value=stage("recovered-unit-primitive-order-"+str(j).zfill(3),recover)
            if value["order"]!=j:raise ValueError("a recovered unit row changed order")
            primitive.append(unpack(value["unit_primitive"],(N,3)))
        def angular_support():
            b=(phase.reshape(COUNT,modes,1)*sines.reshape(1,modes,N)).sum(1)
            g=(vertical.reshape(COUNT,modes,1)*sines.reshape(1,modes,N)).sum(1)
            return dict(phase=pack(b),vertical=pack(g),new_unsaved_support_only=True)
        angles=stage("angular-scalar-derivative-support",angular_support)
        b=unpack(angles["phase"],(COUNT,N));g=unpack(angles["vertical"],(COUNT,N))
        trigs={}
        for name,values in (("phase",b),("vertical",g),("half-phase",b/2),("half-vertical",g/2)):
            def trig(values=values):
                sine,cosine=trig_derivatives(values)
                return dict(sine=pack(sine),cosine=pack(cosine),ordinary_derivatives=True)
            result=stage("trigonometric-"+name+"-support",trig)
            trigs[name]=(unpack(result["sine"],(COUNT,N)),unpack(result["cosine"],(COUNT,N)))
        def half_support():
            return dict(phase_cos_minus_one=pack(-2*derivative_product(trigs["half-phase"][0],trigs["half-phase"][0])),
                vertical_cos_minus_one=pack(-2*derivative_product(trigs["half-vertical"][0],trigs["half-vertical"][0])))
        halves=stage("half-angle-cos-minus-one-support",half_support)
        cmb=unpack(halves["phase_cos_minus_one"],(COUNT,N))
        cmg=unpack(halves["vertical_cos_minus_one"],(COUNT,N))
        sb,sg=trigs["phase"][0],trigs["vertical"][0]
        fft=DirectedFFT();frequency=np.asarray(point["original_frequency"])
        for j in range(12,18):
            def tangent_column(j=j):
                value=cstack([-(sb[j]+derivative_coefficient(cmg,sb,j)),
                    cmg[j]+cmb[j]+derivative_coefficient(cmg,cmb,j),sg[j]],-1)
                return dict(order=j,tangent=pack(value),old_derivative_columns_evaluated=0)
            tangent_record=stage("new-tangent-order-"+str(j).zfill(3),tangent_column)
            tangent=unpack(tangent_record["tangent"],(N,3))
            def Fourier_column(j=j,tangent=tangent):
                coefficient=fft.fft(tangent,0)/N
                doc["new_finite_Fourier_columns"]+=1
                return dict(order=j,complete_Fourier_coefficients=pack(coefficient),
                    nodes=N,ordinary_order=j,old_successful_Fourier_columns_recomputed=0)
            Fourier_record=stage("new-Fourier-order-"+str(j).zfill(3),Fourier_column)
            coefficient=unpack(Fourier_record["complete_Fourier_coefficients"],(N,3))
            def primitive_column(j=j,coefficient=coefficient):
                value=zeros((N,3));ii=CBox(0.,Box(frequency));denominator=Box(1-frequency*frequency)
                value[:,0]=(ii*coefficient[:,0]+coefficient[:,1])/denominator
                value[:,1]=(-coefficient[:,0]+ii*coefficient[:,1])/denominator
                nz=np.flatnonzero(frequency)
                value[nz,2]=coefficient[nz,2]/CBox(0.,Box(frequency[nz]))
                # These are the defining projections of the original finite primitive.
                value[256,:]=0;value[0,1]=0;value[0,2]=0
                value=structural_unit(value)
                return dict(order=j,unit_primitive=pack(value),original_finite_projection_kept=True)
            pr=stage("new-unit-primitive-order-"+str(j).zfill(3),primitive_column)
            primitive.append(unpack(pr["unit_primitive"],(N,3)))
            def finite_column(j=j):
                value=sum((math.comb(j,h)*a[j-h]*primitive[h] for h in range(j+1)),zeros((N,3)))
                value[0,0],value[0,2]=value[0,0]+a[j],value[0,2]+z[j]
                if not czeros(value[256,:]):
                    raise ValueError("a new complete finite column lost its structural Nyquist zero")
                doc["new_finite_primitive_columns"]+=1
                return dict(order=j,complete_finite_field=pack(value),
                    raw_Nyquist_intervals_preserved=True,finite_Nyquist_exact_zero=True)
            fr=stage("new-complete-finite-order-"+str(j).zfill(3),finite_column)
            finite.append(exact_finite_view(unpack(fr["complete_finite_field"],(N,3))))
            if j-12==len(doc["new_finite_columns"]):
                doc["new_finite_columns"].append(dict(order=j,
                    stage="new-complete-finite-order-"+str(j).zfill(3),
                    payload_sha256=payload_sha(fr)));checkpoint()
            elif j-12<len(doc["new_finite_columns"]):
                if doc["new_finite_columns"][j-12]!=dict(order=j,
                    stage="new-complete-finite-order-"+str(j).zfill(3),payload_sha256=payload_sha(fr)):
                    raise ValueError("a completed new finite column changed identity")
            else:raise ValueError("a new finite column prefix has a gap")
        gate("only six new scalar and Fourier derivative orders extend the unchanged twelve-column point",
            len(finite)==18 and len(doc["new_scalar_rows"])==len(doc["new_finite_columns"])==6
            and payload_sha(doc["finite_root_stage"])==payload_sha(point)
            and doc["original_successful_finite_columns_recomputed"]==0
            and doc["original_successful_scalar_derivatives_recomputed"]==0)
        cases=[]
        for R in old.RADII:
            item=next(v for v in aux["cases"] if Q(v["exact_auxiliary_radius"])==R)
            evidence=item["complete_complex_intrinsic_evidence"]
            gate("the existing auxiliary domain "+str(R)+" retains the complete six error jets",
                item["complete"] and item["proved"] and item["failure"] is None
                and item["exact_complex_rectangle"]==dict(
                    real_interval=[str(roots[0]-R),str(roots[1]+R)],imaginary_half_width=str(R))
                and len(evidence["complete_primitive_radial_errors"])==6
                and evidence["original_complete_primitive_nodes"]==512
                and evidence["original_scalar_polynomial_degree_at_most"]==20)
            cases.append((R,evidence))
        if not 12<=len(doc["complete_errors"])<=18 or not 12<=len(doc["finite_component_norms"])<=18:
            raise ValueError("an accepted error or finite-norm prefix changed length")
        for j in range(len(doc["complete_errors"]),18):
            candidates=[]
            for R,evidence in cases:
                for k in range(6):
                    epsilon=up(box(evidence["complete_primitive_radial_errors"][k]))
                    value=(math.factorial(j-k)*epsilon/ex(R)**(j-k)).upper()
                    candidates.append(dict(auxiliary_radius=str(R),saved_radial_order=k,
                        new_radial_order=j,bound=rec(value)))
            selected=min(range(len(candidates)),key=lambda q:box(candidates[q]["bound"]).upper())
            doc["complete_errors"].append(dict(order=j,complete_candidates=candidates,
                selected_candidate_index=selected,complete_error_upper=rec(box(candidates[selected]["bound"]).upper())))
            doc["new_complete_error_orders"]+=1;checkpoint()
        for j in range(len(doc["finite_component_norms"]),18):
            value=arb(float(np.max(reduce_box(Box(finite[j].magnitude_upper())).hi))).upper()
            doc["finite_component_norms"].append(dict(order=j,value=rec(value)))
            doc["new_finite_component_norms"]+=1;checkpoint()
        errors=[box(v["complete_error_upper"]).upper() for v in doc["complete_errors"]]
        norms=[box(v["value"]).upper() for v in doc["finite_component_norms"]]
        reverse=(-np.arange(N))%N
        pairs={str(i)+","+str(j) for i in range(1,18) for j in range(i,18) if i+j<=18}
        if not set(doc["mean_products"]).issubset(pairs):
            raise ValueError("an accepted complete mean has an unrelated derivative pair")
        def mean(i,j):
            i,j=min(i,j),max(i,j);key=str(i)+","+str(j)
            if key not in doc["mean_products"]:
                value=cdot(finite[i],finite[j][reverse]).sum().to_acb()
                if not value.imag.contains(0):
                    raise ValueError("a complete finite bilinear zero convolution lost reality")
                fee=(3*(norms[i]*errors[j]+norms[j]*errors[i]+errors[i]*errors[j])).upper()
                doc["mean_products"][key]=dict(radial_orders=[i,j],finite_real=rec(value.real),
                    finite_imaginary_zero_enclosed=True,complete_error_fee=rec(fee),
                    value=rec(value.real+arb(0,fee)))
                doc["new_mean_products"]+=1;checkpoint()
            row=doc["mean_products"][key]
            if row["radial_orders"]!=[i,j] or row["finite_imaginary_zero_enclosed"] is not True:
                raise ValueError("an accepted true bilinear mean changed its identity")
            return box(row["value"])
        if not 11<=len(doc["energy_jets"])<=17:
            raise ValueError("an accepted energy prefix changed its derivative range")
        for k in range(len(doc["energy_jets"]),17):
            value=sum((math.comb(k,j)*mean(j+1,k-j+1) for j in range(k+1)),arb(0))
            doc["energy_jets"].append(dict(order=k,value=rec(value)))
            doc["new_energy_orders"]+=1;checkpoint()
        E=[box(v["value"]) for v in doc["energy_jets"]]
        gate("all81 complete bilinear means and E0..16 retain the original three branch gaps",
            set(doc["mean_products"])==pairs and len(pairs)==81 and len(E)==17
            and aa[0]>0 and E[0]>0 and E[0]-aa[1]*aa[1]>0)
        def intrinsic_helpers():
            ar=[v/math.factorial(j) for j,v in enumerate(aa)]
            er=[v/math.factorial(j) for j,v in enumerate(E)]
            ia,ie=inv(ar),inv(er);ap,app,ep=diff(ar),diff(diff(ar)),diff(er)
            gap=[er[j]-coef(ap,ap,j) for j in range(16)]
            inverse_AE=mul(ia,ie,16)
            ep_AE2=mul(ep,mul(ia,mul(ie,ie,16),16),16)
            rotation_sqrt=sqrt_series(mul(er,inv(gap),16))
            values=dict(ar=ar,ap=ap,app=app,inverse_A=ia,inverse_AE=inverse_AE,
                Eprime_over_AE2=ep_AE2,sqrt_E=sqrt_series(er),rotation_sqrt=rotation_sqrt)
            return {k:[rec(v) for v in rows] for k,rows in values.items()}
        support=stage("complete-unsaved-intrinsic-series-helpers",intrinsic_helpers)
        q={k:[box(v) for v in rows] for k,rows in support.items()}
        output=doc["intrinsic_stage"]["ordinary_old_radial_jets"]
        lengths={len(v) for v in output.values()}
        if set(output)!={"K","beta","gamma","s"} or len(lengths)!=1 or not 10<=next(iter(lengths))<=16:
            raise ValueError("an appended intrinsic row lost its exact common derivative prefix")
        for j in range(next(iter(lengths)),16):
            values=dict(K=-coef(q["app"],q["inverse_AE"],j)+coef(q["ap"],q["Eprime_over_AE2"],j)/2,
                beta=coef(q["ap"],q["inverse_A"],j),gamma=coef(q["sqrt_E"],q["inverse_A"],j),
                s=-coef(q["ar"],q["rotation_sqrt"],j))
            for name,value in values.items():output[name].append(rec(math.factorial(j)*value))
            doc["new_intrinsic_orders"].append(j)
            doc["new_intrinsic_derivative_values"]+=4;checkpoint()
        doc["intrinsic_stage"].update(complete=True,
            complete_primitive_and_product_errors_included=True,
            missing_series_coefficients_padded_with_zero=False,
            original_orders_zero_through_nine_preserved=True,new_orders=list(range(10,16)))
        checkpoint()
        divided=doc["at_the_certified_true_root"]["divided_curvature_normalized_rho_coefficients"]
        if not 9<=len(divided)<=15:
            raise ValueError("the original divided-curvature coefficient prefix changed")
        for j in range(len(divided),15):
            divided.append(rec(((-1)**j)*box(output["K"][j+1])/math.factorial(j+1)));checkpoint()
        gate("four complete intrinsic rows reach order15 with unchanged certified root branch",
            all(len(v)==16 for v in output.values())
            and box(output["K"][0]).contains(0) and box(output["K"][1])>0
            and box(output["gamma"][0])>0 and box(output["s"][0])<0
            and len(divided)==15 and doc["at_the_certified_true_root"]["exact_K0"]=="0")
        unchanged=(doc["finite_root_stage"]==original["finite_root_stage"]
            and doc["complete_errors"][:12]==original["complete_errors"]
            and doc["finite_component_norms"][:12]==original["finite_component_norms"]
            and all(doc["mean_products"].get(k)==v for k,v in original["mean_products"].items())
            and doc["energy_jets"][:11]==original["energy_jets"]
            and doc["physical_radius_ordinary_jets"][:12]==original["physical_radius_ordinary_jets"]
            and all(output[k][:10]==v for k,v in original["intrinsic_stage"]["ordinary_old_radial_jets"].items())
            and doc["denominator_gaps"]==original["denominator_gaps"]
            and doc["original_low_order_identity_checks"]==original["original_low_order_identity_checks"]
            and divided[:9]==original["at_the_certified_true_root"]["divided_curvature_normalized_rho_coefficients"])
        gate("every original successful point error mean energy intrinsic and comparison record is unchanged",unchanged)
        doc["exact_original_finite_point_and_low_order_records_preserved"]=True
        doc["accepted_total_new_scalar_rows"]=len(doc["new_scalar_rows"])
        doc["accepted_total_new_finite_columns"]=len(doc["new_finite_columns"])
        doc["accepted_total_new_error_orders"]=len(doc["complete_errors"])-12
        doc["accepted_total_new_mean_products"]=len(doc["mean_products"])-36
        doc["accepted_total_new_energy_orders"]=len(doc["energy_jets"])-11
        doc["accepted_total_new_intrinsic_values"]=sum(len(v)-10 for v in output.values())
        gate("all new natural files fit unchanged publication and no original mathematical stage was recomputed",
            all(v["bytes"]<=5000000 for v in doc["stages"].values())
            and doc["original_successful_finite_columns_recomputed"]==0
            and doc["original_successful_scalar_derivatives_recomputed"]==0
            and doc["original_successful_error_or_mean_or_energy_or_intrinsic_rows_recomputed"]==0
            and doc["original_successful_auxiliary_domains_recomputed"]==0
            and doc["original_infinite_tail_evaluator_calls"]==0
            and not doc["smaller_Taylor_remainder_strong_return_or_full_inverse_claimed"])
        doc["complete"]=True;doc["proved"]=True
    except BaseException as error:
        doc["failure"]=dict(type=type(error).__name__,message=str(error));raise
    finally:
        checkpoint()
        print(json.dumps(dict(complete=doc["complete"],proved=doc["proved"],failure=doc["failure"],
            new_Fourier_columns=doc["new_finite_Fourier_columns"],
            new_mean_products=doc["new_mean_products"],new_energy_orders=doc["new_energy_orders"],
            new_intrinsic_values=doc["new_intrinsic_derivative_values"],
            natural_stages=len(doc["stages"]),native_sha256=sha(args.out),seconds=doc["seconds"]),
            allow_nan=False),flush=True)
if __name__=="__main__":main()
