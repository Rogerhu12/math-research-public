"""Explicit recovery of the R182 continuous K domain and subset installer.

This is a NEW canonical schema and source, not a claim to recover the
unavailable original domain-02 bytes. It rebuilds the same proved finite
Bernstein sufficient inequalities from the already published exact R182
continuous rows. The first saved version has not been executed in Python;
generation and integration must report their actual later outcomes.

The installer selects certified windows by all FOUR exact dyadic breaks.
Names and trace signs do not choose K constraints. The actual names/signs
remain in the saved subset definition. No field, F/J, or BVP is evaluated.

CLI, from the topic cwd:
  python scripts/fd2d_gc_signed_search_domain_recovery.py --out-prefix \
    notes/2026-11-12-fd2d-signed-domain-recovery-01

Outputs: -domain.json.gz, -qp.npz, -report.json.
"""
from __future__ import annotations

import argparse
import copy
from fractions import Fraction as F
import gzip
import hashlib
import json
import math
from pathlib import Path
import time

import numpy as np

SCHEMA="fd2d-R182-Bernstein-positive-K-domain-recovery-v1"
SUBSET_SCHEMA="fd2d-R182-active-window-subset-domain-recovery-v1"
ROWS_SHA256="d7f990bcef75ec30311e23d3cf92dadf5736f871f141dd3f7fa62071f7793095"
CERTIFICATE_SHA256="44d3d9318ffa7b70f7bcc59cebf81df09e72b9c37562c05e1410cdb65b627a68"
CANDIDATE_SHA256="7c3f31de4b230e8d98b99c3e3914d65ae69daa3cb5c54ae22f585a36a888bfd1"
DEGREE=8


def identity(path):
    path=Path(path);data=path.read_bytes()
    return dict(path=str(path),bytes=len(data),sha256=hashlib.sha256(data).hexdigest())


def same_identity(a,b):
    return a["bytes"]==b["bytes"] and a["sha256"]==b["sha256"]


def pair(value):
    value=F(value)
    return [str(value.numerator),str(value.denominator)]


def fraction(value):
    if isinstance(value,F):
        return value
    if isinstance(value,(list,tuple)) and len(value)==2:
        return F(int(value[0]),int(value[1]))
    if isinstance(value,(int,np.integer)):
        return F(int(value))
    if isinstance(value,str):
        return F(value)
    value=float(value)
    if not math.isfinite(value):
        raise ValueError("Nonfinite coefficient")
    return F.from_float(value)


def bound(record,side):
    m,e=record[side+"_binary"];m=int(m);e=int(e)
    return F(m*(1<<e),1) if e>=0 else F(m,1<<(-e))


def portable(value):
    if isinstance(value,dict):
        return {k:portable(v) for k,v in value.items()
                if not (k=="path" and "bytes" in value and "sha256" in value)}
    if isinstance(value,(tuple,list)):
        return [portable(v) for v in value]
    return value


def digest(value):
    return hashlib.sha256(json.dumps(portable(value),sort_keys=True,
        separators=(",",":"),allow_nan=False).encode()).hexdigest()


def read_json(path):
    path=Path(path);data=path.read_bytes()
    if path.suffix==".gz":
        data=gzip.decompress(data)
    return json.loads(data)


def write_gzip_json(path,value):
    data=(json.dumps(value,sort_keys=True,separators=(",",":"),allow_nan=False)+"\n").encode()
    with Path(path).open("wb") as stream:
        with gzip.GzipFile(filename="",fileobj=stream,mode="wb",mtime=0) as output:
            output.write(data)
    return dict(uncompressed_bytes=len(data),
        uncompressed_sha256=hashlib.sha256(data).hexdigest())


def canonical_breaks(window):
    """No float tolerance, sign test or window-name lookup selects a domain."""
    if "exact_dyadic_breaks" not in window:
        raise ValueError("The active window must declare all four exact dyadic breaks")
    values=tuple(fraction(v) for v in window["exact_dyadic_breaks"])
    if len(values)!=4 or not all(values[j]<values[j+1] for j in range(3)):
        raise ValueError("Four strictly ordered exact window breaks are required")
    if "breaks" in window:
        displayed=tuple(F.from_float(float(v)) for v in window["breaks"])
        if displayed!=values:
            raise ValueError("The actual binary64 breaks disagree with their exact declaration")
    return values


def second_bernstein_on_child(left,right,support):
    """Exact degree-eight coefficients of the compact bump second derivative."""
    a,b=map(fraction,(left,right));L,R=map(fraction,support)
    if not a<b or not L<R:
        raise ValueError("Positive child and support widths required")
    if b<=L or a>=R:
        return [F(0)]*(DEGREE+1)
    if not L<=a<b<=R:
        raise ValueError("Split at every compact-support boundary before evaluating a polynomial")
    width=R-L
    power=[F(0)]*(DEGREE+1)
    for j in range(6):
        power[3+j]=F(1024*((-1)**j)*math.comb(5,j)*(5+j)*(4+j),1)/(width*width)
    start=(a-L)/width;extent=(b-a)/width
    local=[]
    for i in range(DEGREE+1):
        local.append((extent**i)*sum(
            (power[k]*math.comb(k,i)*(start**(k-i))
             for k in range(i,DEGREE+1)),F(0)))
    return [sum((local[i]*F(math.comb(k,i),math.comb(DEGREE,i))
                 for i in range(k+1)),F(0)) for k in range(DEGREE+1)]


def floor_binary64(value):
    value=F(value);out=float(value)
    if not math.isfinite(out):
        raise ValueError("Finite binary64 QP coefficients are required")
    while F.from_float(out)>value:
        out=math.nextafter(out,-math.inf)
    return out


def exact_row(child,k):
    return [fraction(v) for v in child["bernstein_rows"][int(k)]],fraction(child["rhs_upper"])


def rounded_row(coefficients,rhs,bounds):
    """M delta >= lower implies exact A delta <= rhs inside the saved box."""
    ahat=[float(v) for v in coefficients]
    if not all(math.isfinite(v) for v in ahat):
        raise ValueError("Nonfinite rounded Bernstein coefficient")
    error=sum((abs(F.from_float(v)-a)*M
               for v,a,M in zip(ahat,coefficients,bounds)),F(0))
    safe_upper=floor_binary64(rhs-error)
    return [-v for v in ahat],-safe_upper,-float(rhs),error


def verify_exact_delta(packet,selected_children,delta):
    """Exact selected continuous-domain check, independent of QP tolerance."""
    dimension=int(packet["dimension"])
    try:
        values=[fraction(v) for v in delta]
    except (ValueError,TypeError,OverflowError) as exc:
        return dict(passed=False,reason="invalid coefficient: "+str(exc))
    if len(values)!=dimension:
        return dict(passed=False,reason="wrong explicit profile dimension")
    limits=[fraction(v) for v in packet["delta_absolute_bounds_exact"]]
    inside=all(abs(v)<=M for v,M in zip(values,limits))
    minimum=None;worst=None;rows=0
    for child_id in selected_children:
        child=packet["children"][int(child_id)]
        for k in range(DEGREE+1):
            coefficients,rhs=exact_row(child,k)
            slack=rhs-sum((a*v for a,v in zip(coefficients,values)),F(0))
            if minimum is None or slack<minimum:
                minimum=slack;worst=[int(child_id),k]
            rows+=1
    radius=fraction(packet["base_radius_lower"])-sum((abs(v) for v in values),F(0))
    positive=radius>0
    rows_passed=minimum is None or minimum>=0
    return dict(passed=inside and positive and rows_passed,
        exact_coefficient_box_passed=inside,exact_selected_rows_passed=rows_passed,
        exact_global_radius_lower=pair(radius),global_radius_positive=positive,
        selected_children=len(selected_children),selected_exact_rows=rows,
        minimum_exact_slack=None if minimum is None else pair(minimum),
        minimum_slack_display=None if minimum is None else float(minimum),
        worst_global_child_and_degree=worst,
        delta_exact=[pair(v) for v in values],
        scope="Only the selected complete positive-K supports; not an unknown-field or geometry certificate")


def make_recovery_domain(rows_path,certificate_path,out_prefix):
    """Rebuild NEW transport bytes from the original exact proved input rows."""
    started=time.monotonic()
    rows_path,certificate_path,out_prefix=map(Path,(rows_path,certificate_path,out_prefix))
    row_id,cert_id=identity(rows_path),identity(certificate_path)
    if row_id["sha256"]!=ROWS_SHA256 or cert_id["sha256"]!=CERTIFICATE_SHA256:
        raise ValueError("The published original R182 certificate inputs changed")
    rows_packet=read_json(rows_path);certificate=read_json(certificate_path)
    if not certificate["passed"] or not same_identity(rows_packet["actual_field"],certificate["actual_field"]):
        raise ValueError("The continuous source rows and certificate disagree")
    supports=[tuple(fraction(v) for v in row) for row in certificate["bump_supports_exact"]]
    dimension=len(supports)
    if dimension!=7:
        raise ValueError("This published R182 packet proves the original explicit seven-parameter family")
    limits=[F.from_float(.08)]*dimension
    base_lower=F(4,5)
    radius_box_lower=base_lower-sum(limits,F(0))
    if radius_box_lower<=0:
        raise ValueError("The declared coefficient box does not preserve the proved positive radius")
    windows=[];children=[];owners=[];matrix=[];lower=[];ordinary=[];maximum_error=F(0)
    for widx,window in enumerate(certificate["windows"]):
        ends=tuple(fraction(v["exact"]) for v in window["endpoints"])
        if not len(ends)==4 or not all(ends[i]<ends[i+1] for i in range(3)):
            raise ValueError("Malformed certified window")
        records=rows_packet["rows"][window["name"]]
        if len(records)!=int(window["exact_cover_rows"]):
            raise ValueError("The full certified window cover is required")
        previous=ends[0];first_child=len(children)
        for parent_ordinal,row in enumerate(records):
            left,right=map(fraction,row["interval"])
            if left!=previous or not left<right:
                raise ValueError("Source cover has a gap, overlap, or unordered row")
            previous=right
            margin=-bound(row["a_ss"],"upper")
            if margin<=0:
                raise ValueError("The source continuous row does not have a positive margin")
            if "current_a_ss_negative_margin" in row and fraction(row["current_a_ss_negative_margin"])!=margin:
                raise ValueError("The stored source margin differs from its exact interval bound")
            eta=margin/2;base_upper=bound(row["base_a_ss"],"upper")
            rhs=-eta-base_upper
            cuts=sorted({left,right}|{p for support in supports for p in support if left<p<right})
            for a,b in zip(cuts[:-1],cuts[1:]):
                basis=[second_bernstein_on_child(a,b,support) for support in supports]
                coefficients=[[basis[j][k] for j in range(dimension)] for k in range(DEGREE+1)]
                child_id=len(children)
                child=dict(child_id=child_id,window_index=widx,
                    source_row_ordinal=parent_ordinal,source_row_index=int(row["index"]),
                    interval_exact=[pair(a),pair(b)],base_a_ss_upper=pair(base_upper),
                    strict_a_ss_margin=pair(eta),rhs_upper=pair(rhs),
                    bernstein_rows=[[pair(v) for v in row_values] for row_values in coefficients])
                children.append(child)
                for k,row_values in enumerate(coefficients):
                    M,bound_value,raw_bound,error=rounded_row(row_values,rhs,limits)
                    owners.append([child_id,k]);matrix.append(M);lower.append(bound_value);ordinary.append(raw_bound)
                    maximum_error=max(maximum_error,error)
        if previous!=ends[-1]:
            raise ValueError("A certified closed support has an uncovered endpoint")
        windows.append(dict(window_index=widx,certificate_name=window["name"],
            certificate_trace_sign=int(window["sign"]),
            exact_dyadic_breaks=[pair(v) for v in ends],
            child_ids=list(range(first_child,len(children))),
            trace_sign_is_not_a_K_domain_constraint=True))
    output={key:out_prefix.with_name(out_prefix.name+suffix) for key,suffix in
        [("domain","-domain.json.gz"),("qp","-qp.npz"),("report","-report.json")]}
    if any(path.exists() for path in output.values()):
        raise FileExistsError("Choose a new recovery output stem; do not overwrite originals")
    out_prefix.parent.mkdir(parents=True,exist_ok=True)
    M=np.asarray(matrix,dtype=np.float64).reshape(-1,dimension)
    b=np.asarray(lower,dtype=np.float64)
    owner=np.asarray(owners,dtype=np.int64).reshape(-1,2)
    packet=dict(schema=SCHEMA,source=identity(__file__),dimension=dimension,bernstein_degree=DEGREE,
        original_input_rows=row_id,original_certificate=cert_id,
        original_actual_field=certificate["actual_field"],
        profile_input_binding_sha256=certificate["profile_input_binding_sha256"],
        base_candidate_sha256=CANDIDATE_SHA256,base_radius_lower=pair(base_lower),
        profile_supports_exact=[[pair(v) for v in support] for support in supports],
        delta_absolute_bounds_exact=[pair(v) for v in limits],
        original_center_delta_exact=certificate["center_delta_exact"],
        global_radius_lower_on_entire_parameter_box=pair(radius_box_lower),
        windows=windows,children=children,
        row_semantics="For each child and k: A_k*delta <= -eta-base_a_ss_upper; exact degree-eight Bernstein rows give a_ss <= -eta throughout that child",
        qp_semantics="matrix@delta >= lower with safe coefficient-rounding budget on the exact saved absolute coefficient box",
        rounding="Ahat=float(A); error=sum(abs(Ahat-A)*M); bhat=floor_binary64(rhs-error); matrix=-Ahat,lower=-bhat",
        maximum_coefficient_rounding_budget=pair(maximum_error),
        original_domain02_bytes_or_sha_recovered=False,new_canonical_transport_schema=True)
    center_check=verify_exact_delta(packet,range(len(children)),
        [fraction(v) for v in certificate["center_delta_exact"]])
    if not center_check["passed"]:
        raise ValueError("The exact original center failed the recovered sufficient domain")
    np.savez_compressed(output["qp"],matrix=M,lower=b,
        ordinary_lower=np.asarray(ordinary,dtype=np.float64),
        delta_absolute_bounds=np.asarray([float(v) for v in limits],dtype=np.float64),
        row_owner=owner)
    packet["qp_identity"]=identity(output["qp"])
    packet["binding_sha256"]=digest(packet)
    raw=write_gzip_json(output["domain"],packet)
    report=dict(schema="fd2d-R182-Bernstein-domain-recovery-generation-v1",
        passed=True,source=identity(__file__),original_rows=row_id,original_certificate=cert_id,
        domain=identity(output["domain"]),qp=identity(output["qp"]),uncompressed_domain=raw,
        domain_binding_sha256=packet["binding_sha256"],dimension=dimension,
        children=len(children),rows=len(owners),windows=windows,
        exact_original_center_check=center_check,
        safe_QP_original_center_minimum=float(np.min(M@np.array([float(fraction(v)) for v in certificate["center_delta_exact"]])-b)),
        maximum_exact_rounding_budget=pair(maximum_error),
        source_family_sha256=CANDIDATE_SHA256,
        new_profile_Arb_F_J_BVP_body_evaluated=False,
        original_domain02_bytes_or_sha_claimed=False,
        seconds=time.monotonic()-started)
    output["report"].write_text(json.dumps(report,indent=2,allow_nan=False)+"\n")
    return report


class SignedSearchDomainHandle:
    def __init__(self,problem,windows,domain_path,qp_path):
        self.domain_path,self.qp_path=Path(domain_path),Path(qp_path)
        self.packet=read_json(self.domain_path)
        packet=self.packet
        if packet.get("schema")!=SCHEMA:
            raise ValueError("Require the explicitly NEW recovery domain schema, not guessed original-02 keys")
        saved_binding=packet.get("binding_sha256")
        without_binding={k:v for k,v in packet.items() if k!="binding_sha256"}
        if saved_binding!=digest(without_binding):
            raise ValueError("The recovered exact domain binding changed")
        if packet["source"]["sha256"]!=identity(__file__)["sha256"]:
            raise ValueError("The recovery-domain source differs from the actual generating source")
        if (packet["original_input_rows"]["sha256"]!=ROWS_SHA256 or
                packet["original_certificate"]["sha256"]!=CERTIFICATE_SHA256 or
                packet["base_candidate_sha256"]!=CANDIDATE_SHA256):
            raise ValueError("The published exact proof inputs changed")
        if not same_identity(packet["qp_identity"],identity(self.qp_path)):
            raise ValueError("The QP packet differs from the bound new exact domain")
        dimension=int(packet["dimension"])
        if dimension!=len(packet["profile_supports_exact"]) or int(packet["bernstein_degree"])!=DEGREE:
            raise ValueError("Wrong explicit domain dimension or degree")
        if problem.profile.source_identity["sha256"]!=packet["base_candidate_sha256"]:
            raise ValueError("The actual problem belongs to another accurate base candidate")
        supports=[[pair(F.from_float(float(v))) for v in row] for row in problem.profile.supports]
        if supports!=packet["profile_supports_exact"]:
            raise ValueError("The current actual bump supports are not the certified exact supports")
        profile_slice=problem.profile_parameter_slice
        if profile_slice.step not in (None,1) or profile_slice.stop-profile_slice.start!=dimension:
            raise ValueError("The explicit global parameter slice disagrees with the domain")
        if int(problem.profile.parameter_count)!=dimension:
            raise ValueError("New physical design columns need their own complete domain certificate")
        self.profile_parameter_slice=profile_slice
        limits=[fraction(v) for v in packet["delta_absolute_bounds_exact"]]
        self.delta_absolute_bounds=np.array([float(v) for v in limits],dtype=np.float64)
        if any(F.from_float(float(v))!=M for v,M in zip(self.delta_absolute_bounds,limits)):
            raise ValueError("The saved original box must be exactly representable in binary64")
        self.delta_absolute_bounds.flags.writeable=False
        if windows is None:
            if not hasattr(problem,"signed_windows"):
                raise ValueError("Supply the actual signed field windows explicitly")
            windows=problem.signed_windows
        active=list(windows)
        if hasattr(problem,"signed_windows"):
            actual=list(problem.signed_windows)
            selected_identity=[(canonical_breaks(w),int(w["sign"])) for w in active]
            actual_identity=[(canonical_breaks(w),int(w["sign"])) for w in actual]
            if selected_identity!=actual_identity:
                raise ValueError("Install the actual field's declared windows, not a hidden different subset")
        by_breaks={}
        for window in packet["windows"]:
            key=canonical_breaks(window)
            if key in by_breaks:
                raise ValueError("Ambiguous duplicate certified windows")
            by_breaks[key]=window
        selected_windows=[];selected_children=[];seen=set()
        for window in active:
            key=canonical_breaks(window)
            if key in seen or key not in by_breaks:
                raise ValueError("Each active window must match one distinct certified four-break window")
            sign=int(window["sign"])
            if sign not in (-1,1):
                raise ValueError("An explicit trace sign +/-1 is required")
            proved=by_breaks[key];seen.add(key)
            selected_children.extend(map(int,proved["child_ids"]))
            selected_windows.append(dict(actual_name=str(window.get("name","")),
                actual_trace_sign=sign,exact_dyadic_breaks=[pair(v) for v in key],
                certified_window_index=int(proved["window_index"]),
                certificate_name=proved["certificate_name"],
                trace_sign_used_to_select_constraints=False))
        self.selected_children=tuple(sorted(selected_children))
        if len(set(self.selected_children))!=len(self.selected_children):
            raise ValueError("A child would be included more than once")
        children=packet["children"]
        expected_owners=[]
        for child_id,child in enumerate(children):
            if int(child["child_id"])!=child_id or len(child["bernstein_rows"])!=DEGREE+1:
                raise ValueError("The complete child ledger changed")
            if any(len(row)!=dimension for row in child["bernstein_rows"]):
                raise ValueError("Wrong exact row dimension")
            if fraction(child["strict_a_ss_margin"])<=0:
                raise ValueError("A strict continuous child margin is required")
            if fraction(child["rhs_upper"])!=-fraction(child["strict_a_ss_margin"])-fraction(child["base_a_ss_upper"]):
                raise ValueError("The exact child inequality changed")
            expected_owners.extend((child_id,k) for k in range(DEGREE+1))
        with np.load(self.qp_path,allow_pickle=False) as qp:
            matrix=np.array(qp["matrix"],dtype=np.float64,copy=True)
            lower=np.array(qp["lower"],dtype=np.float64,copy=True)
            owners=np.array(qp["row_owner"],copy=True)
            actual_limits=np.array(qp["delta_absolute_bounds"],dtype=np.float64,copy=True)
        if (matrix.shape!=(len(expected_owners),dimension) or lower.shape!=(len(expected_owners),)
                or owners.dtype.kind not in "iu" or
                not np.array_equal(owners,np.asarray(expected_owners,dtype=np.int64))
                or not np.array_equal(actual_limits,self.delta_absolute_bounds)
                or not np.all(np.isfinite(matrix)) or not np.all(np.isfinite(lower))):
            raise ValueError("The complete QP row ledger, shape or coefficient box is inconsistent")
        selected=np.isin(owners[:,0],np.asarray(self.selected_children,dtype=np.int64))
        # Check the sufficient rounding inequality for every row actually
        # appended; ordinary_lower is deliberately not a proof input.
        for row_index in np.flatnonzero(selected):
            child_id,k=map(int,owners[row_index])
            coefficients,rhs=exact_row(children[child_id],k)
            ahat=[-F.from_float(float(v)) for v in matrix[row_index]]
            error=sum((abs(v-a)*M for v,a,M in zip(ahat,coefficients,limits)),F(0))
            if F.from_float(float(lower[row_index])) < -rhs+error:
                raise ValueError("A selected rounded QP row is not a sufficient exact inequality")
        self.selected_row_indices=np.flatnonzero(selected)
        self.matrix=matrix[selected].copy();self.lower=lower[selected].copy()
        self.row_owner=owners[selected].copy()
        self.matrix.flags.writeable=False;self.lower.flags.writeable=False;self.row_owner.flags.writeable=False
        self._definition=dict(schema=SUBSET_SCHEMA,source=identity(__file__),
            exact_domain_identity=identity(self.domain_path),qp_identity=identity(self.qp_path),
            complete_domain_binding_sha256=saved_binding,base_candidate_sha256=CANDIDATE_SHA256,
            profile_supports_exact=packet["profile_supports_exact"],
            profile_parameter_slice=[profile_slice.start,profile_slice.stop],
            delta_absolute_bounds_exact=packet["delta_absolute_bounds_exact"],
            actual_active_windows=selected_windows,selected_global_children=list(self.selected_children),
            selected_original_row_indices=self.selected_row_indices.tolist(),
            selected_row_owner=self.row_owner.tolist(),selected_row_count=len(self.lower),
            active_profile_columns=np.flatnonzero(np.any(self.matrix!=0.,axis=0)).tolist(),
            every_selected_child_has_nine_rows=True,
            nonselected_window_rows_excluded=True,
            window_name_or_sign_used_as_K_constraint=False,
            required_context_box="The QP context must keep each |delta_j| within delta_absolute_bounds; verify_delta checks that exact box again",
            complete_field_or_continuous_geometry_certified=False)
        self._definition["binding_sha256"]=digest(self._definition)

    def verify_delta(self,delta7):
        result=verify_exact_delta(self.packet,self.selected_children,delta7)
        result["subset_binding_sha256"]=self._definition["binding_sha256"]
        return result

    def definition(self):
        return copy.deepcopy(self._definition)


def install_signed_search_domain(problem,*,windows=None,domain_path,qp_path):
    """Append selected rows to the existing radius domain, preserving its keys.

    No +/- box rows are silently duplicated. The context has the declared
    original coefficient bounds and must compare them with the exposed
    delta_absolute_bounds. Exact acceptance uses handle.verify_delta().
    """
    if hasattr(problem,"_signed_search_domain_recovery_handle"):
        raise ValueError("This problem already has the recovered domain; do not append duplicate rows")
    handle=SignedSearchDomainHandle(problem,windows,domain_path,qp_path)
    old=problem.profile_domain
    if not isinstance(old,dict) or "matrix" not in old or "lower" not in old:
        raise ValueError("An explicit original radius profile_domain dictionary is required")
    dimension=int(handle.packet["dimension"])
    old_matrix=np.asarray(old["matrix"],dtype=np.float64)
    old_lower=np.asarray(old["lower"],dtype=np.float64)
    if old_matrix.ndim!=2 or old_matrix.shape[1]!=dimension or old_lower.shape!=(len(old_matrix),):
        raise ValueError("The original radius constraints have the wrong parameter dimension")
    updated=dict(old)
    updated["matrix"]=np.vstack((old_matrix,handle.matrix))
    updated["lower"]=np.r_[old_lower,handle.lower]
    updated["signed_search_domain_recovery"]=handle.definition()
    updated["original_profile_domain_row_count"]=len(old_lower)
    problem.profile_domain=updated
    problem._signed_search_domain_recovery_handle=handle
    return handle


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rows",type=Path,default=Path(
        "notes/2026-11-12-fd2d-metric-dyadic34-signed-trace-windows-R182-01-rows.json.gz"))
    parser.add_argument("--certificate",type=Path,default=Path(
        "notes/2026-11-12-fd2d-metric-dyadic34-signed-trace-windows-R182-01-report.json"))
    parser.add_argument("--out-prefix",type=Path,required=True)
    args=parser.parse_args()
    summary=make_recovery_domain(args.rows,args.certificate,args.out_prefix)
    print(json.dumps({k:summary[k] for k in ("passed","children","rows","domain","qp","seconds")},
                     allow_nan=False))
