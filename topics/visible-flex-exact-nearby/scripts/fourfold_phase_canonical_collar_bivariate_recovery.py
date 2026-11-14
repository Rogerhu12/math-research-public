#!/usr/bin/env python3
"""Reconstruct the actual R87 mixed Taylor cover after executor loss.

This is a new, explicitly identified source. It reruns actual cells; it does
not reconstruct any lost interval output from a prose summary. The immutable
finite geometry, true infinite primitive and Cauchy shift-tail formulas are
used with 40 primitive terms and 39 E terms, m=10, n=18, Q=512.
"""
from __future__ import annotations
import argparse,ctypes,gc,gzip,json,math,time
from fractions import Fraction as F
from pathlib import Path
from flint import arb,acb_series,ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_canonical_collar_centered import CenteredPhysicalRootGeometry
from fourfold_phase_canonical_collar_centered_cover import ROOT_ORDERS
from fourfold_phase_canonical_collar_finite import (
    FiniteRootCoordinates,finite_canonical_operator,physical_polynomial_trial,
    root_potential_coefficients,trial_residual_coefficients,sha,
    canonical_derivative,jet_function,mul,add,real_jet,
    ParameterGermBallTarget,root_family)


def read(path):
    with gzip.open(path,"rt") as f:return json.load(f)


def string(value):
    return arb(value).str(50)


class FortyTermGeometry(CenteredPhysicalRootGeometry):
    def __init__(self,object_path,half_width,root_certificate,*,nodes=512,
                 radial_precision=10,angle_precision=18,scale=F(1,1024)):
        self.m,self.n=radial_precision,angle_precision
        self.scale=exact_arb(scale)
        self.target=ParameterGermBallTarget(object_path,half_width,nodes,nodes)
        self.root,self.spans=root_family(self.target,root_certificate)
        self.polynomial_order=40
        if self.polynomial_order<=max(self.m+3,self.n+3):
            raise ValueError("the true retained polynomial is too short")
        self.offset=None;self._states={}
        self.prepare_offset(arb(0))
        # E contains one true radial derivative. The inherited shift-tail
        # formula reads this actual precision, not the nominal cap.
        if self.root_E.prec!=39 or self.root_coefficient[0,0].prec!=40:
            raise ValueError("unexpected actual native polynomial precision")
        old=ctx.cap;ctx.cap=max(self.m+3,self.n+3)
        try:
            self.root_kappa=acb_series(
                [-self.K[j+1]/self.scale for j in range(self.m-1)],prec=self.m-1)
        finally:ctx.cap=old
        if not self.root_kappa[0].real>0:
            raise ValueError("actual root deflation lost positivity")


def angular_bound(whole,centre,i,j,scale,radius,limit):
    """sup |d_s^i d_theta^j f|/i!, with a true whole-angle remainder."""
    if i>=min(whole.m,centre.m) or j>=min(whole.n,centre.n):
        raise ValueError("missing actual mixed coefficient")
    best=(abs(whole.coefficient(i,j).real)*math.factorial(j)/scale**i).upper()
    nmax=min(limit,whole.n-j-1,centre.n-j-1)
    total=arb(0)
    for p in range(1,nmax+1):
        r=p-1
        total+=(abs(centre.coefficient(i,j+r).real)
            *math.factorial(j+r)/math.factorial(r)*radius**r/scale**i).upper()
        remainder=(abs(whole.coefficient(i,j+p).real)
            *math.factorial(j+p)/math.factorial(p)*radius**p/scale**i).upper()
        best=min(best,(total+remainder).upper())
    return best


def coefficient_set(model,angle,offset,coordinates,root_values):
    principal=model.principal(angle,at_root=offset.is_zero())
    chart=coordinates.positive(offset,model.m-1,model.n)
    op=finite_canonical_operator(principal,chart,model.scale)
    invpt=jet_function(op["pt"],"inverse")
    invheight=jet_function(op["height"],"inverse")
    op["slice_density_multiplier"]=real_jet(mul(op["physical_source_factor"],invpt))
    op["slice_radial_jacobian"]=real_jet(mul(op["J"],invpt))
    hy=canonical_derivative(op["height"],op,model.scale,"normal")
    hp=canonical_derivative(op["height"],op,model.scale,"angle")
    op["height_normal_log"]=real_jet(mul(
        add(hy,mul(op["cross_error"],hp)),invheight))
    trial=physical_polynomial_trial(root_values,chart,offset,model.scale)
    return op,{**op,**trial_residual_coefficients(op,trial,model.scale)}


def evaluate(model,row,height,radial_cells=2,angular_order=6,angular_centres=4):
    left,right=map(F,row["exact_quarter_interval"])
    centre=exact_arb((left+right)/4)*arb.pi()
    radius=exact_arb((right-left)/4)*arb.pi()
    angle=centre+arb(0,radius)
    model.prepare_offset(arb(0))
    root=model.principal(angle,at_root=True)
    centres=[centre+exact_arb(F(2*i+1,angular_centres)-1)*radius
             for i in range(angular_centres)]
    subradius=radius/angular_centres
    roots_c=[model.principal(c,at_root=True) for c in centres]
    coords=FiniteRootCoordinates(root,model.scale)
    coords_c=[FiniteRootCoordinates(rc,model.scale) for rc in roots_c]
    rv=root_potential_coefficients(root,model.scale)
    rv_c=[root_potential_coefficients(rc,model.scale) for rc in roots_c]
    _,root_all=coefficient_set(model,angle,arb(0),coords,rv)
    roots_all_c=[coefficient_set(model,c,arb(0),cc,v)[1]
                 for c,cc,v in zip(centres,coords_c,rv_c)]
    for name,k in ROOT_ORDERS.items():
        for i in range(k):
            for j in range(3):
                if not root_all[name].coefficient(i,j).real.contains(0):
                    raise ValueError(f"true root identity not enclosed: {name}[{i},{j}]")
    uniform={name:[[arb(0) for _ in range(3)] for _ in range(root_all[name].m)]
             for name in ROOT_ORDERS}
    nvalid={name:min(root_all[name].m,*(rc[name].m for rc in roots_all_c))
            for name in ROOT_ORDERS}
    def across_centres(whole,points,i,j):
        return max(angular_bound(whole,point,i,j,model.scale,subradius,angular_order)
                   for point in points)
    ordinary_names=("defining_ratio","height","physical_source_factor","ys","yt","ps","pt","J","A11",
      "slice_density_multiplier","slice_radial_jacobian","height_normal_log")
    ordinary={name:[arb(0) for _ in range(3)] for name in ordinary_names}
    actual_radial=[]
    for cell in range(radial_cells):
        a,b=height*cell/radial_cells,height*(cell+1)/radial_cells
        offset=exact_arb((a+b)/2)+arb(0,exact_arb((b-a)/2))
        model.prepare_offset(offset)
        op,full=coefficient_set(model,angle,offset,coords,rv)
        pairs_c=[coefficient_set(model,c,offset,cc,v)
                 for c,cc,v in zip(centres,coords_c,rv_c)]
        ops_c=[v[0] for v in pairs_c];points=[v[1] for v in pairs_c]
        for name,k in ROOT_ORDERS.items():
            nvalid[name]=min(nvalid[name],full[name].m,*(p[name].m for p in points))
            for i in range(k,nvalid[name]):
                for j in range(3):
                    value=across_centres(full[name],[p[name] for p in points],i,j)
                    if not value.is_finite():raise ValueError("nonfinite actual mixed remainder")
                    uniform[name][i][j]=max(uniform[name][i][j],value)
        for name in ordinary_names:
            for j in range(3):
                ordinary[name][j]=max(ordinary[name][j],
                    across_centres(op[name],[p[name] for p in ops_c],0,j))
        actual_radial.append([str(a),str(b)])
    H=exact_arb(height);bounds={};methods={};root_data={};rem_data={}
    for name,k in ROOT_ORDERS.items():
        nmax=nvalid[name]-1
        root_coeff=[[across_centres(root_all[name],[rc[name] for rc in roots_all_c],i,j)
                     for j in range(3)] for i in range(k,nmax+1)]
        cols=[];chosen=[]
        for j in range(3):
            best=min(arb(row["derivative_sup_for_root_division"][name][j]).upper(),
                     uniform[name][k][j]).upper()
            method={"type":"whole_radial_derivative_integral","remainder_order":k}
            for n in range(k+1,nmax+1):
                value=sum((root_coeff[i-k][j]*H**(i-k) for i in range(k,n)),arb(0))
                value+=uniform[name][n][j]*H**(n-k)
                if value.upper()<best:
                    best=value.upper()
                    method={"type":"root_Taylor_true_continuous_remainder","remainder_order":n}
            cols.append(string(best));chosen.append(method)
        bounds[name]=cols;methods[name]=chosen
        root_data[name]=dict(first_order=k,coefficients=[[string(z) for z in v] for v in root_coeff])
        rem_data[name]=dict(first_order=k,coefficients=[
            [string(z) for z in uniform[name][i]] for i in range(k,nmax+1)])
    return dict(exact_quarter_interval=row["exact_quarter_interval"],
      exact_positive_radial_interval=["0",str(height)],actual_radial_subslabs=actual_radial,
      exact_quarter_subintervals=[[str(left+(right-left)*i/angular_centres),
        str(left+(right-left)*(i+1)/angular_centres)] for i in range(angular_centres)],
      derivative_sup_for_root_division=bounds,selected_radial_taylor_bounds=methods,
      root_after_actual_angular_Taylor=root_data,whole_slab_after_actual_angular_Taylor=rem_data,
      ordinary_physical_theta_derivatives={k:list(map(string,v)) for k,v in ordinary.items()})


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--base-cover",type=Path,default=Path(
      "notes/2026-11-12-actual-finite-canonical-collar-centered-cover.json.gz"))
    ap.add_argument("--first-index",type=int,default=0)
    ap.add_argument("--last-index",type=int)
    ap.add_argument("--batch-cells",type=int,default=4)
    ap.add_argument("--resume",action="store_true")
    ap.add_argument("--out",type=Path,required=True)
    args=ap.parse_args()
    base=read(args.base_cover);config=base["configuration"];rows=base["cells"]
    last=len(rows) if args.last_index is None else args.last_index
    if not base.get("proved") or base["failed_cells"] or base["pending"]:
        raise ValueError("complete actual R87 cover required")
    if not 0<=args.first_index<last<=len(rows) or args.batch_cells<1:
        raise ValueError("invalid actual range or process batch")
    ctx.prec,ctx.cap=256,40;obj=config["object"]
    root_path=Path("data/phase_ring_continuation/type_fixed_step02_d5_step5_local_parameter_root_jets_h5e7.json")
    if sha(root_path)!=config["root_certificate_sha256"]:raise ValueError("actual root changed")
    for name,value in config["dependencies"].items():
        if sha(Path(__file__).with_name(name))!=value:
            raise ValueError("actual native dependency changed: "+name)
    if sha(obj["center_object_path"])!=obj["center_object_sha256"]:
        raise ValueError("actual object changed")
    model=FortyTermGeometry(Path(obj["center_object_path"]),F(obj["exact_parameter_half_width"]),
                           root_path,nodes=config["nodes"])
    height=F(config["exact_collar_height"]);start=time.monotonic();previous_seconds=0.0
    report=dict(kind="actual_R87_bivariate_recovery_with_full_40_term_Cauchy_tail",proved=False,
      source_sha256=sha(__file__),base_cover_sha256=sha(args.base_cover),actual_object=obj,
      root_certificate_sha256=sha(root_path),exact_collar_height=str(height),
      first_index=args.first_index,last_index=last,base_cell_count=len(rows),
      radial_cells=2,radial_precision=10,angle_precision=18,
      angular_Taylor_maximum_order=6,bits=256,angular_centres_per_old_interval=4,
      retained_native_root_order=40,retained_E_order=39,
      dependencies={name:sha(Path(__file__).with_name(name)) for name in (
        "fourfold_phase_canonical_collar_centered.py","fourfold_phase_canonical_collar_finite.py",
        "fourfold_phase_canonical_collar_centered_cover.py","fourfold_phase_root_potential_complex_strip.py")},
      cells=[],failed_cells=[],next_index=args.first_index,
      scope=["Every reported interval row is actually recomputed from the true native object.",
             "The retained 40 primitive and 39 E terms carry the unchanged actual Cauchy shift-tail formulas.",
             "No lost 80-term or mixed-order result is reconstructed from prose.",
             "Full source/contact or reflection constants require a separate completed-cover aggregation."])
    if args.resume:
        old=read(args.out)
        for key in report:
            if key in ("proved","cells","failed_cells","next_index"):continue
            if old.get(key)!=report[key]:raise ValueError("exact source/configuration changed: "+key)
        if old["failed_cells"] or old["next_index"]!=args.first_index+len(old["cells"]):
            raise ValueError("invalid or failed actual prefix")
        for i,row in enumerate(old["cells"],args.first_index):
            if row["base_index"]!=i or row["exact_quarter_interval"]!=rows[i]["exact_quarter_interval"]:
                raise ValueError("saved actual rows are not contiguous")
        previous_seconds=float(old.get("seconds",0));report=old
    elif args.out.exists():
        raise ValueError("explicit --resume required for an existing output")
    def save():
        report["seconds"]=previous_seconds+time.monotonic()-start
        args.out.parent.mkdir(parents=True,exist_ok=True)
        temporary=args.out.with_suffix(args.out.suffix+".tmp")
        with gzip.open(temporary,"wt") as f:json.dump(report,f,indent=2);f.write("\n")
        temporary.replace(args.out)
    count=0;save();libc=ctypes.CDLL(None)
    for i in range(report["next_index"],last):
        if count>=args.batch_cells:
            print(json.dumps(dict(saved_actual_checkpoint=True,next_index=i)),flush=True)
            raise SystemExit(75)
        try:row=evaluate(model,rows[i],height)
        except (ValueError,ZeroDivisionError) as exc:
            report["failed_cells"].append(dict(base_index=i,reason=str(exc)))
            save();raise
        row["base_index"]=i;report["cells"].append(row);report["next_index"]=i+1
        count+=1;save();gc.collect()
        if hasattr(libc,"malloc_trim"):libc.malloc_trim(0)
        print(json.dumps(dict(accepted=len(report["cells"]),next_index=i+1,
                             seconds=report["seconds"])),flush=True)
    report["covered_specified_cells"]=True
    report["proved"]=args.first_index==0 and last==len(rows)
    save()
    print(json.dumps(dict(covered_specified_cells=True,proved=report["proved"],
                         cells=len(report["cells"]),report_sha256=sha(args.out))),flush=True)


if __name__=="__main__":main()
