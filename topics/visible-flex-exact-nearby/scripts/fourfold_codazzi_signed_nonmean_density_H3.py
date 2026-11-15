#!/usr/bin/env python3
"""New complete first-symbol nonmean transport, with signed H3 validation.

Only frozen original scalar identities, finite polynomials, completed mean
integrals and the selected true-angle certificate are restored. The only new
target is SN's forced density and its complete H3 enclosure. No accepted scalar,
ray, response, Green, root Newton or circle iteration is called.
"""
from __future__ import annotations
import argparse,bisect,gzip,hashlib,io,json,math,os,time,traceback
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import arb,acb,ctx
import fourfold_codazzi_signed_density_transport_arithmetic as sn
from fourfold_codazzi_signed_density_transport_arithmetic import (
    LP,Jet,Dual,exact,ball,up,hull,rat,real,positive,rec,restrict_scalar,
    inward_scalar,source_algebra,gram_error_step,h3_columns,reference_step,
    complete_reference_residual,finite_angle_derivative,inverse_density_constant)

REL="topics/visible-flex-exact-nearby/"
PRODUCER=REL+"scripts/fourfold_codazzi_signed_nonmean_density_H3.py"
HELPER=REL+"scripts/fourfold_codazzi_signed_density_transport_arithmetic.py"
CONTRACT=REL+"results/R133-supplement-signed-nonmean-density-transport-and-H3-validation.md"
PUBLIC="Rogerhu12/math-research-public"
KIND="actual_complete_signed_nonmean_density_H3_validation_v1"
CANDIDATE="ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413"
CENTRE="440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
DIRECTION="6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04"
ROOT_CONTRACT="1910bdc2ee84cd23a7a92d94689d8cd90a3a5c25cf56caa3cc585159a9c5af43"
DELTA=Fraction(1,10**10)
CUT=Fraction(76285779072683,320000000000000)
PARAMETERS=dict(arithmetic_bits=320,reference_modes=128,reference_radial_degree=6,
    complete_radial_remainder_order=6,angle_exp_degree=24,angle_tail_width="1/128",
    exact_real_parameter_half_width=str(DELTA),root_piece=2549,candidate_prefix_parts=2,
    original_strict_intervals=3146,original_scalar_germs=169,original_scalar_cells=626,
    original_compact_T_cells=220,physical_frequency_factor=4,
    output_Sobolev_exponent=3,all_output_means_retained=True,
    source_reference_is_not_a_Fourier_projection_proof=True,
    maximum_new_subcells=120000,maximum_optical_step="1/4",
    original_scalar_integrals_rays_KAM_and_response_recomputed=0)

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def canonical(v):return (json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False)+"\n").encode()
def read(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith(".gz") else raw)
def encode(v):
    if isinstance(v,arb):return rec(v)
    if isinstance(v,Fraction):return str(v)
    if isinstance(v,dict):return {k:encode(x) for k,x in v.items()}
    if isinstance(v,(list,tuple)):return [encode(x) for x in v]
    return v
def gate(doc,name,value):
    doc["gates"].append(dict(name=name,passed=bool(value)))
    if not value:raise ValueError("new complete SN gate: "+name)
def save(path,value):
    raw=canonical(encode(value))
    p=Path(path);p.parent.mkdir(parents=True,exist_ok=True)
    tmp=p.with_suffix(p.suffix+".partial");tmp.write_bytes(raw);tmp.replace(p)
    # Rendering limits never erase or relabel an already completed new target.
    return {"bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest(),
            "within_preferred_small_limit":len(raw)<=58000}
def symmetric(z):return arb(0,up(z))
def const(v,n=1):return Dual(Jet.const(v,n))
def coef(root,name,k):return ball(root["actual_finite_Taylor_terms"][name][k]["normalized_derivative"])
def nth_tail(root,name):return up(ball(root["complete_next_normalized_derivatives"][name]))
def derivative_parameter(root,key):
    return up(ball(root["complete_parameter_derivative_envelopes"][key]))
def finite_norm_jet(values,order=4):
    return [sum((up(v)*(4*abs(j))**q for j,v in values),arb(0)).upper()
            for q in range(order+1)]
def product_norm(a,b,q):
    return sum((math.comb(q,j)*a[j]*b[q-j] for j in range(q+1)),arb(0)).upper()

class Inputs:
    def __init__(self,a,doc):
        self.a=a;self.doc=doc;root=a.root.resolve()
        gate(doc,"mathematics runs only in the declared public Actions child",
             os.environ.get("GITHUB_ACTIONS")=="true" and os.environ.get("GITHUB_REPOSITORY")==PUBLIC)
        gate(doc,"the new science helper manifest and exact parameters are frozen",
             sha(a.manifest)==a.manifest_sha and a.bits==PARAMETERS["arithmetic_bits"])
        m=read(a.manifest);self.manifest=m
        gate(doc,"both new source identities and the published SN contract are pinned",
             m["parameters"]==PARAMETERS and m["files"][PRODUCER]==sha(__file__)
             and m["files"][HELPER]==sha(sn.__file__) and CONTRACT in m["files"])
        seen=set();total=0
        for row in m["file_receipts"]:
            name=row["path"];p=(root/name).resolve()
            if name in seen or not name.startswith(REL) or not p.is_relative_to(root):
                raise ValueError("a complete original pin is duplicated or outside the topic")
            if not p.is_file() or p.stat().st_size!=row["bytes"] or sha(p)!=row["sha256"]:
                raise ValueError("an immutable new or original input changed: "+name)
            if m["files"][name]!=row["sha256"]:raise ValueError("two input manifests disagree")
            seen.add(name);total+=row["bytes"]
        gate(doc,"every original byte is checked before a mathematical field is evaluated",
             seen==set(m["files"]))
        self.paths={k:root/v for k,v in m["input_paths"].items()}
        self.records={k:read(p) for k,p in self.paths.items() if k not in ("candidate_part0","candidate_part1")}
        self.fp=self.records["finite_part"];self.transfer=self.records["parameter_transfer"]
        self.cover=self.records["scalar_cover"];self.tc=self.records["t_cache"]
        self.direction=self.records["direction"];self.rb=self.records["root_budget"]
        self.germ=self.records["root_germ"];self.repair=self.records["repair"]
        self.strip=self.records["strip_proof"];self.angle_root=self.records["angle_root"]
        self.post=self.records["angle_post"];self.index=self.records["candidate"]
        gate(doc,"all restored completed scientific originals are complete without relabelling an old attempt",
             all(v.get("complete") is True for k,v in self.records.items() if k not in ("candidate","angle_root"))
             and self.fp["candidate_sha256"]==CANDIDATE
             and self.fp["continuous_centre_definition_sha256"]==CENTRE
             and self.direction["derived_direction_definition_sha256"]==DIRECTION
             and self.repair["derived_definition_sha256"]==CENTRE)
        gate(doc,"the old mean and selected parameter retain all3146 rows and both root steps",
             len(self.fp["rows"])==PARAMETERS["original_strict_intervals"]
             and len(self.transfer["rows"])==PARAMETERS["original_strict_intervals"]
             and self.fp["explicit_family_parameter_delta"]=="0"
             and self.transfer["transfer_enclosure_complete"] is True
             and self.transfer["explicit_direction_definition_sha256"]==DIRECTION
             and self.fp["original_root_newton_steps_reused"]==2)
        self.rlo,self.rhi=map(Fraction,self.transfer["exact_root_enclosure"])
        self.rs=hull(self.rlo,self.rhi)
        gate(doc,"the same fixed root and strict interface are used without a new Newton step",
             list(map(str,(self.rlo,self.rhi)))==self.fp["actual_eta0_root_enclosure"]
             and self.fp["exact_strict_cut"]==str(CUT) and 0<CUT<self.rlo
             and self.germ["compact_bump_identically_zero_on_entire_actual_germ"])
        self.oldroot=self.fp["root_finite_part"]
        self.rootpar=self.transfer["root_Cauchy_candidates"][self.transfer["selected_root_Cauchy_index"]]
        self.Rpar=Fraction(self.rootpar["exact_radial_radius"])
        self.Router=Fraction(self.germ["complex_radial_radius"])
        gate(doc,"the original root analytic family and all angular means remain fixed",
             self.Router==Fraction(1,100000)
             and Fraction(self.rb["exact_outer_radial_radius"])==self.Router
             and Fraction(self.rb["exact_complex_parameter_radius"])>=DELTA
             and self.rb["explicit_direction_definition_sha256"]==DIRECTION
             and len(self.direction["complete_negative_interval_direction_coefficient_suprema"])==193
             and len(self.rb["response_repaired_complete_coefficient_upper"])==193
             and self.rb["exact_radial_rectangle"]==self.germ["complex_radial_rectangle"]
             and self.rb["exact_moving_Wiener_strip"]=="1/1024"
             and self.germ["domain_contains_disks_about_every_true_parameter_root"])
        self.load_candidate_prefix()
        self.scalar=[]
        for g in self.cover["germs"]:
            name=g["path"] if g["path"].startswith(REL) else REL+g["path"]
            if m["files"].get(name)!=g["sha256"]:
                raise ValueError("an original scalar-cover relative path lost its exact manifest identity")
            p=root/name;v=read(p)
            if sha(p)!=g["sha256"] or not v["complete"] or v["configuration"]!=self.cover["configuration"]:
                raise ValueError("an original complete scalar germ changed")
            self.scalar.extend((Fraction(r["interval"][0]),Fraction(r["interval"][1]),g["sha256"],r)
                               for r in v["rows"])
        self.scalar.sort(key=lambda x:x[0])
        gate(doc,"all169 original scalar germs and626 complete cells are read without their producer",
             len(self.cover["germs"])==169 and len(self.scalar)==626
             and all(self.scalar[i-1][1]==self.scalar[i][0] for i in range(1,len(self.scalar)))
             and self.scalar[0][0]==0 and self.scalar[-1][1]>CUT)
        self.Trows={tuple(map(Fraction,r["interval"])):r for r in self.tc["compact_T_models"]}
        gate(doc,"all220 compact T polynomials are original complete read-only identities",
             self.tc["compact_T_complete"] is True and len(self.Trows)==220)
        self.zvals=[up(ball(v)) for v in self.direction["complete_negative_interval_direction_coefficient_suprema"]]
        self.rzvals=[up(ball(v)) for v in self.rb["response_repaired_complete_coefficient_upper"]]
        self.er=[exact(Fraction(v)) for v in self.repair["exact_cumulative_coefficient_suprema"]]
        self.root_offsets=list(map(Fraction,self.rb["exact_background_root_offsets"]))
        gate(doc,"base repair and physical193 direction have distinct full units and exact root offset",
             len(self.er)==65 and len(self.root_offsets)==65
             and self.root_offsets==list(map(Fraction,self.repair["special_piece_offsets"]["2549"]["physical_offset"]))
             and self.direction["background_definition_sha256"]==CENTRE)
        self.root_u=self.candidate_fields(2549,self.rlo,self.rhi,None,1,exact_root=True)[0]
        self.root_U=(self.root_u*self.root_u).ne()
        self.beta_complex=self.germ["complex_intrinsic_coefficients"]["beta"]
        self.bstar=ball(self.beta_complex["real"])
        self.g00=coef(self.oldroot,"A",0);self.g10=coef(self.oldroot,"A",1)
        self.B00=coef(self.oldroot,"B",0);self.chibar=self.g10+self.B00
        self.old_suffix=[arb(0)]*(len(self.fp["rows"])+1)
        self.par_suffix=[arb(0)]*(len(self.fp["rows"])+1)
        for i in range(len(self.fp["rows"])-1,-1,-1):
            self.old_suffix[i]=self.old_suffix[i+1]+ball(self.fp["rows"][i]["complete_signed_integral"])
            self.par_suffix[i]=self.par_suffix[i+1]+up(ball(self.transfer["rows"][i]["integrated_complete_parameter_derivative"]))
        rootI=ball(self.oldroot["complete_signed_root_finite_part"])
        self.old_suffix=[v+rootI for v in self.old_suffix]
        gate(doc,"the complete original scalar finite part is recovered only by summing its saved rows",
             self.old_suffix[0].overlaps(ball(self.fp["complete_signed_first_symbol_finite_part"]))
             and up(ball(self.transfer["complete_total_parameter_derivative"]))<exact("186751.988620238"))
        self.selected=self.strip["selected"]
        gate(doc,"the finite lifts and the physical1over128 errors belong to one selected true angle",
             self.strip["physical_true_conjugacy_strip_proved"]
             and self.selected["physical_conjugacy_A1over128_proved"]
             and self.strip["physical_requested_strip"]=="1/128"
             and self.strip["root_contract_sha256"]==ROOT_CONTRACT
             and self.strip["postcomposition_native_sha256"]==sha(self.paths["angle_post"])
             and sha(self.paths["angle_root"])==ROOT_CONTRACT)
        gate(doc,"the actual selected parameter lies in the declared real disk",
             up(ball(self.transfer["actual_selected_R31_parameter_abs_upper"]))<exact(DELTA)
             and self.transfer["inputs"]["strip_proof"]["sha256"]==sha(self.paths["strip_proof"])
             )
        self.mu=ball(self.transfer["complete_selected_parameter_finite_part"])
        self.Hs,self.Hc=[list(map(Fraction,self.angle_root[k])) for k in
            ("exact_H_sine_coefficients","exact_H_cosine_coefficients")]
        self.Ks,self.Kc=[list(map(Fraction,self.post[k])) for k in
            ("exact_postcomposition_sine_coefficients","exact_postcomposition_cosine_coefficients")]
        self.KH,self.Ej,self.angledata=inverse_density_constant(
            self.Hs,self.Hc,self.Ks,self.Kc,self.selected)
        gate(doc,"the same selected true j verifies both literal AC endpoints before its matrix is used",
             self.angledata["literal_31over32_33over32_gates_verified"]
             and self.angledata["proved_j_lower"]>=exact(Fraction(31,32))
             and self.angledata["proved_j_upper"]<=exact(Fraction(33,32)))
        doc["original_input_sha256"]={k:sha(v) for k,v in self.paths.items()}
        doc["complete_original_inventory"]={"count":len(seen),"bytes":total,
            "canonical_sha256":hashlib.sha256(canonical(m["file_receipts"])).hexdigest()}
        doc["exact_original_root"]=[str(self.rlo),str(self.rhi)]
        doc["complete_original_mean_finite_part"]=self.transfer["complete_selected_parameter_finite_part"]
        self.root_diagnostics={}

    def load_candidate_prefix(self):
        if sha(self.paths["candidate"])!=CANDIDATE:raise ValueError("the original candidate index changed")
        doc=self.index;parts=doc["parts"][:2];nodes=[];cc=[];end=None;cursor=0
        for i,pin in enumerate(parts):
            path=self.paths["candidate_part"+str(i)]
            if sha(path)!=pin["sha256"] or path.stat().st_size!=pin["bytes"]:
                raise ValueError("a complete original prefix shard changed")
            z=np.load(io.BytesIO(gzip.decompress(path.read_bytes())),allow_pickle=False)
            r=z["radial_nodes"];c=z["piece_coefficients"]
            if (pin["first_interval"]!=cursor or c.dtype!=np.float64 or r.dtype!=np.float64
                or c.shape!=(4,pin["last_interval_exclusive"]-cursor,65)
                or len(r)!=c.shape[1]+1 or not np.isfinite(c).all() or not np.isfinite(r).all()
                or not (np.diff(r)>0).all()
                or (end is not None and r[0].view(np.uint64)!=end.view(np.uint64))):
                raise ValueError("the complete prefix dtype finite shape or exact-node gate failed")
            nodes.extend(r if end is None else r[1:]);cc.append(c);end=r[-1]
            cursor=pin["last_interval_exclusive"]
        self.nodes=[Fraction(float(x)) for x in nodes];self.cc=np.concatenate(cc,axis=1)
        self.alpha=Fraction(doc["metadata"]["exact_float_amplitude"])
        if (self.cc.shape!=(4,2692,65) or doc["coefficient_shape"]!=[4,6144,65]
            or not self.nodes[2549]<CUT<self.rlo<self.rhi<self.nodes[2550]):
            raise ValueError("the exact two-shard prefix does not contain the entire root domain")
        gate(self.doc,"the two complete original shards cover every waist-to-root candidate cell",
             self.nodes[0]==0 and self.nodes[-1]>self.rhi
             and doc["metadata"]["physical_frequency_factor"]==4
             and doc["metadata"]["finite_state_angle"]=="moving phi")

    def candidate_fields(self,piece,left,right,sseries,n,exact_root=False):
        """Normalized inward-r jets; physical alpha occurs exactly once."""
        middle=hull(left,right)-exact(self.nodes[piece])
        rr=Jet([middle,-1]+[0]*(max(0,n-2))).pad(n)
        vals=[]
        for k in range(65):
            val=Jet.const(0,n)
            for degree in range(4):val=val*rr+exact(self.alpha*Fraction(float(self.cc[degree,piece,k])))
            offset=(exact(self.root_offsets[k]) if exact_root else symmetric(self.er[k]))
            val=val+offset;vals.append(val)
        U=[];V=[]
        for t in range(n):
            uu=[acb(0)]*65;vv=[acb(0)]*65
            vv[32]=vals[32].c[t].coeff(0)
            for j in range(1,33):
                a=vals[j-1].c[t].coeff(0);b=vals[32+j].c[t].coeff(0)
                uu[32+j]=a/acb(0,2);uu[32-j]=-a/acb(0,2)
                vv[32+j]=vv[32-j]=b/2
            U.append(LP(uu,-32));V.append(LP(vv,-32))
        if sseries is not None:
            V=[x+sseries.c[k] for k,x in enumerate(V)]
        return Jet(U),Jet(V)

    def direction_field(self,root=False):
        vals=self.rzvals if root else self.zvals;U=[acb(0)]*193;V=[acb(0)]*193
        V[96]=acb(symmetric(vals[96]))
        for j in range(1,97):
            a=symmetric(vals[j-1])/2;b=symmetric(vals[96+j])/2
            U[96+j]=acb(0,-a);U[96-j]=acb(0,a);V[96+j]=V[96-j]=acb(b)
        return Jet([LP(U,-96)]),Jet([LP(V,-96)])

    def root_data(self,n,parameter=False):
        ma=derivative_parameter(self.rootpar,"A")
        mb=derivative_parameter(self.rootpar,"B")
        if parameter:
            de=exact(DELTA);zU=self.direction_field(True)[0]
            u0=self.root_u.pad(1)
            ur=Dual(u0+Jet.const(1,1)*zU*arb(0,de),zU)
            g0=Dual(Jet.const(self.g00+arb(0,de*ma),1),Jet.const(symmetric(ma),1))
            a1=Dual(Jet.const(self.g10+arb(0,de*ma/exact(self.Rpar)),1),
                    Jet.const(symmetric(ma/exact(self.Rpar)),1))
            B0=Dual(Jet.const(self.B00+arb(0,de*mb),1),Jet.const(symmetric(mb),1))
        else:
            ur=Dual(self.root_u.pad(n));g0=const(self.g00,n)
            a1=const(self.g10,n);B0=const(self.B00,n)
        b=const(self.bstar,n);chi=a1+B0-exact(Fraction(26,3))*b*g0*(ur*ur).ne()
        return dict(g0=g0,A1=a1,B0=B0,b=b,chi=chi,U=(ur*ur).ne())

    def scalar_membership(self,left,right,old):
        i=bisect.bisect_right([r[0] for r in self.scalar],left)-1
        a,b,h,row=self.scalar[i]
        if not a<=left<=right<=b or h!=old["scalar_native_sha256"]:
            raise ValueError("a new interval leaves its old complete scalar cell")
        return row

    def fields(self,row,piece,left,right,n,parameter=False):
        if parameter and n!=1:raise ValueError("no unrecorded radial Z derivatives may be invented")
        # For q_r retain one extra original derivative; all other fields need n.
        b=inward_scalar(row,"beta",left,right,n)
        gamma=inward_scalar(row,"gamma",left,right,n)
        q0=inward_scalar(row,"q",left,right,n+1)
        qr=-q0.derivative();q0=q0.pad(n)
        ss=inward_scalar(row,"s",left,right,n)
        u,v=self.candidate_fields(piece,left,right,ss,n)
        rho=Jet([self.rs-hull(left,right),1]+[0]*max(0,n-2)).pad(n)
        root=self.root_data(n,parameter)
        if not parameter:return [Dual(x) for x in (u,v,b,gamma,q0,qr,rho)],root
        zu,zv=self.direction_field()
        de=Dual(Jet.const(arb(0,exact(DELTA)),1),Jet.const(1,1))
        uu=Dual(u+zu*arb(0,exact(DELTA)),zu);vv=Dual(v+zv*arb(0,exact(DELTA)),zv)
        ga=Dual(gamma);qq=Dual(q0);qr0=Dual(qr)
        if right<=Fraction(1,20) or left>=Fraction(9,50):
            return [uu,vv,Dual(b),ga,qq,qr0,Dual(rho)],root
        if not Fraction(1,20)<=left<=right<=Fraction(9,50):
            raise ValueError("a new parameter interval crosses an actual compact endpoint")
        a0,b0=Fraction(1,20),Fraction(9,50)
        t=Jet.const(hull((left-a0)/(b0-a0),(right-a0)/(b0-a0)),1)
        w=4096*t**6*(1-t)**6
        wp=exact(Fraction(24576,b0-a0))*t**5*(1-t)**5*(1-2*t)
        wpp=exact(Fraction(24576,(b0-a0)**2))*t**4*(1-t)**4*(5*(1-2*t)**2-2*t*(1-t))
        tr=self.Trows[tuple(map(Fraction,row["interval"]))]
        T=Dual(inward_scalar(tr,"T",left,right,1))
        Tr=const(restrict_scalar(tr,"T",left,right,1),1)
        W=qq*qq-de*T*Dual(wp)
        expfactor=(-de*Dual(w)/2).exp()
        qd=expfactor*W.sqrt()
        qrd=qd*(-de*Dual(wp)/2+(2*qq*qr0-de*(Tr*Dual(wp)+T*Dual(wpp)))/(2*W))
        gd=ga*(de*Dual(w)/2).exp()
        return [uu,vv,Dual(b),gd,qd,qrd,Dual(rho)],root

    def endpoint_mean(self,index,side):
        old=self.fp["rows"][index]
        r=Fraction(old["interval"][0 if side=="left" else 1])
        I=self.old_suffix[index if side=="left" else index+1]
        rho=self.rs-exact(r);s=rho.sqrt()
        return -I/2-self.g00/(3*rho*s)-self.chibar/s

    def mean_parameter_fee(self,rho,left_index):
        ma=derivative_parameter(self.rootpar,"A");mb=derivative_parameter(self.rootpar,"B")
        mc=derivative_parameter(self.rootpar,"C");md=derivative_parameter(self.rootpar,"D")
        lo=rho.lower();hi=rho.upper();R=exact(self.Rpar)
        general=(exact(DELTA)*((
            up(ball(self.transfer["complete_root_parameter_derivative"]))+self.par_suffix[left_index])/2
            +ma/(3*lo*lo.sqrt())+(ma/R+mb)/lo.sqrt())).upper()
        if hi<R:
            local=(exact(DELTA)*(ma*hi.sqrt()/(R*R*(1-hi/R))
                +mb*hi.sqrt()/(R*(1-hi/R))+mc*hi.sqrt()+md*hi*hi.sqrt()/3)).upper()
            return min(local,general).upper()
        return general

    def mean_reference(self,index,row,piece):
        old=self.fp["rows"][index];left,right=map(Fraction,old["interval"]);length=exact(right-left)
        # The reference is linear in inward coordinate t=right-r.
        ml=self.endpoint_mean(index,"right");mr=self.endpoint_mean(index,"left")
        ref=[exact(rat(ml)),exact(rat((mr-ml)/length))]
        whole,roots=self.fields(row,piece,left,right,2)
        mhat=const(0,2)
        _,_,mp,_=source_algebra(*whole,roots,mhat,1)
        curvature=up(mp.v.c[1].scalar())
        endpoints=max(up(ml-ref[0]),up(mr-(ref[0]+length*ref[1]))).upper()
        fee=(endpoints+length**2*curvature/8).upper()
        return ref,fee,{"new_partial_mean_curvature":curvature,
            "old_endpoint_interval_fee":endpoints,"linear_reference_uniform_error":fee}

    def nominal_source(self,index,row,piece,left,right,n,mref,mright,sigma):
        vals,roots=self.fields(row,piece,left,right,n)
        # The same original linear m0 reference is evaluated on all subcells.
        c=hull(mright-right,mright-left)
        mh=Jet([mref[0]+mref[1]*c,mref[1]]+[0]*max(0,n-2)).pad(n)
        F,a,_,extra=source_algebra(*vals,roots,Dual(mh),sigma)
        return F.v,a.v,extra

    def parameter_error(self,index,row,piece,left,right,reference,mref,mright,meanfee,sigma):
        vals,roots=self.fields(row,piece,left,right,1,True)
        c=hull(mright-right,mright-left);mh=const(mref[0]+mref[1]*c,1)
        F,a,_,extra=source_algebra(*vals,roots,mh,sigma)
        # A single dual differential pays both forcing and transport coefficient.
        ref=Jet([reference])
        derivative=F.t-(a.t*ref).dphi()
        rho=vals[-1].v.value().scalar()
        dm=(meanfee+self.mean_parameter_fee(rho,index)).upper()
        s=rho.sqrt()
        # In ordinary dr the 2s from SN.16 cancels exactly.
        d=extra["d"].v.value()
        fees=[(exact(DELTA)*derivative.value().l2(q)+dm*d.l2(q+1)).upper() for q in range(4)]
        drift=[d.a(q) for q in range(5)]
        return fees,drift,dm

def root_entry(inp):
    """New nonmean collar only; all old radial Taylor numbers are read."""
    rr=inp.oldroot;h=inp.rs-exact(CUT);H=h.upper();s=H.sqrt()
    R=exact(inp.Router);gap=positive(R-H,"root quotient radius")
    rp=inp.rootpar;Rp=exact(inp.Rpar)
    positive(Rp-H,"root parameter quotient radius")
    de=exact(DELTA);ma=derivative_parameter(rp,"A");mb=derivative_parameter(rp,"B")
    mc=derivative_parameter(rp,"C");md=derivative_parameter(rp,"D")
    def scalar_poly(name,last):
        return sum((abs(coef(rr,name,k))*H**k for k in range(last+1)),arb(0))+nth_tail(rr,name)*H**(last+1)
    A=(scalar_poly("A",5)+de*ma).upper()
    Bbar=(scalar_poly("B",4)+de*mb).upper()
    g0=(abs(inp.g00)+de*ma).upper()
    chibar=(abs(inp.chibar)+de*(ma/Rp+mb)).upper()
    bcomplex=acb(ball(inp.beta_complex["real"]),ball(inp.beta_complex["imag"]))
    bm=exact(rat(bcomplex.real))
    bdiff=(abs(bcomplex-acb(bm))/gap).upper()
    b=up(bcomplex)
    intrinsic=inp.germ["complex_intrinsic_coefficients"]
    kgap=positive(ball(intrinsic["K1"]["real"]).lower(),"old complete k real part")
    k=up(ball(intrinsic["K1"]["modulus_upper"]))
    gamma=up(ball(intrinsic["gamma"]["modulus_upper"]))
    root_fields=inp.candidate_fields(2549,CUT,inp.rhi,None,2,exact_root=True)
    ur=root_fields[0]
    vv=root_fields[1].value()+ball(intrinsic["s"]["real"])
    Zu=list(map(lambda x:up(ball(x)),inp.rb["direction_angular_norms_u"]))
    Zv=list(map(lambda x:up(ball(x)),inp.rb["direction_angular_norms_v"]))
    U=[(ur.value().a(q)+de*Zu[q]).upper() for q in range(5)]
    V=[(vv.a(q)+de*Zv[q]).upper() for q in range(5)]
    Ud=[(ur.c[1].a(q)+de*Zu[q]/gap).upper() for q in range(4)]
    Ustar=[(inp.root_u.value().a(q)+de*Zu[q]).upper() for q in range(5)]
    Um=[product_norm(U,U,q) for q in range(5)]
    Us=[product_norm(Ustar,Ustar,q) for q in range(5)]
    Vn=[arb(0)]*5
    Vne0=(vv.ne().a()+de*Zv[1]/4).upper()
    Vmean=(abs(vv.mean())+de*up(ball(inp.rb["response_repaired_complete_coefficient_upper"][96]))).upper()
    Vn[0]=(2*Vmean*Vne0+Vne0*Vne0).upper()
    for q in range(1,5):Vn[q]=product_norm(V,V,q)
    E=[(Um[q]+H*k*Vn[q]).upper() for q in range(5)]
    D=[(b*E[0]/4).upper()]+[(b*E[q-1]).upper() for q in range(1,6)]
    chik=[(exact(Fraction(26,3))*up(inp.bstar)*g0*Us[q]).upper() for q in range(5)]
    chik[0]=(chik[0]+chibar).upper()
    Aq=(sum((abs(coef(rr,"A",j))*H**(j-1) for j in range(1,6)),arb(0))
        +nth_tail(rr,"A")*H**5+de*ma/(Rp-H)).upper()
    J=(b*(8*A+2*g0/3)).upper()
    Jq=(8*b*Aq+exact(Fraction(26,3))*g0*bdiff).upper()
    Uquot=[(2*sum((math.comb(q,j)*Ud[j]*U[q-j] for j in range(q+1)),arb(0))).upper()
           for q in range(4)]
    quotient=[(J*Uquot[q]+Jq*Us[q]).upper() for q in range(4)]
    Cne=[(4*b*Bbar*E[q]+16*A*b*b*product_norm(E,E,q)).upper() for q in range(4)]
    UV=[product_norm(U,V,q) for q in range(5)]
    Dne=[]
    for q in range(4):
        cross=sum((math.comb(q,j)*(U[j]*V[q-j+1]+V[j]*U[q-j+1]) for j in range(q+1)),arb(0))
        Dne.append((64*A*b*b*k*product_norm(UV,UV,q)+2*b*k.sqrt()*cross).upper())
    m0=arb(0)
    for name,start,last,shift,sgn in (("A",2,5,Fraction(-3,2),-1),
        ("B",1,4,Fraction(-1,2),-1),("C",0,3,Fraction(1,2),-1),
        ("D",0,2,Fraction(3,2),1)):
        for j in range(start,last+1):
            power=Fraction(j)+shift
            m0+=abs(coef(rr,name,j))*H**exact(power)/(2*exact(power))
    m0+=H**exact(Fraction(9,2))*sum((nth_tail(rr,z) for z in "ABCD"),arb(0))/9
    dm=de*(ma*s/(Rp*Rp*(1-H/Rp))+mb*s/(Rp*(1-H/Rp))+mc*s+md*H*s/3)
    mm=(m0+dm).upper();eta=(gamma*(Vmean+de*up(ball(inp.rb["response_repaired_complete_coefficient_upper"][96])))).upper()
    F=[]
    for q in range(4):
        # One derivative acts on the whole d(chi+s*m) product.
        prod=sum((math.comb(q+1,j)*D[j]*(chik[q+1-j]+(s*mm if q+1-j==0 else 0))
                  for j in range(q+2)),arb(0))
        F.append((quotient[q]+b*k*(8*A+2*g0/3)*Vn[q]+Cne[q]+H*Dne[q]
                  +2*prod+s*D[q+2]+2*s*eta*k.sqrt()*chik[q+1]).upper())
    # This first interval uses s, so its drift derivatives are exactly2s*d^q.
    drift=[(2*s*x).upper() for x in D[:5]]
    z,ener=gram_error_step([arb(0)]*4,s,F,drift)
    data=dict(ordinary_s_interval=["0",rec(s)],root_rho_upper=rec(H),
        complete_new_root_nonmean_source=[rec(x) for x in F],
        complete_new_root_H3_error_columns=[rec(x) for x in z],
        complete_root_mean_value_bound=rec(mm),
        original_mean_tail_reused=True,new_scalar_finite_part_integral=False,
        root_u_quotient_is_exact_cubic_plus_complete_direction_Cauchy=True,
        original_radial_quotient_radius=rec(gap),complete_energy=encode(ener))
    return z,data

def complete_taylor(inp,index,row,piece,left,right,n,mref,mright,sigma):
    """Point orders0..n-2, full whole-cell last derivative."""
    Fp,ap,_=inp.nominal_source(index,row,piece,right,right,n,mref,mright,sigma)
    Fw,aw,_=inp.nominal_source(index,row,piece,left,right,n,mref,mright,sigma)
    return Jet(Fp.c[:-1]+[Fw.c[-1]]),Jet(ap.c[:-1]+[aw.c[-1]])

def transport(inp,doc,temp):
    initial,rootdiag=root_entry(inp)
    gate(doc,"new root source has all four angular error columns and a regular zero entry",
         len(initial)==4 and all(v.is_finite() for v in initial)
         and inp.rs-exact(CUT)<exact(inp.Router)/2)
    N=PARAMETERS["reference_modes"];order=PARAMETERS["reference_radial_degree"]
    refs={s:LP([acb(0)]*(2*N+1),-N) for s in (-1,1)}
    errors={s:list(initial) for s in (-1,1)}
    hash_source=hashlib.sha256();hash_reference=hashlib.sha256()
    newrows=0;piececount=set();source_max={s:[arb(0)]*4 for s in (-1,1)}
    param_max=[arb(0)]*4;meanmax=arb(0);curvaturemax=arb(0)
    cursor=CUT;last_piece=None
    temp.mkdir(parents=True,exist_ok=True)
    source_path=temp/"complete-new-signed-source-and-reference.jsonl.gz"
    if source_path.exists():raise FileExistsError("preserve an already started new signed reference")
    with gzip.GzipFile(filename=str(source_path),mode="wb",mtime=0) as stream:
        for index in range(len(inp.fp["rows"])-1,-1,-1):
            old=inp.fp["rows"][index];left,right=map(Fraction,old["interval"])
            if right!=cursor:raise ValueError("new inward transport misses an original closed interval")
            piece=int(old["actual_candidate_piece"]);piececount.add(piece)
            row=inp.scalar_membership(left,right,old)
            if not inp.nodes[piece]<=left<right<=inp.nodes[piece+1]:
                raise ValueError("an original accepted row crosses a candidate piece")
            mref,mfee,mdata=inp.mean_reference(index,row,piece)
            curvaturemax=max(curvaturemax,mdata["new_partial_mean_curvature"]).upper()
            meanmax=max(meanmax,mfee).upper()
            # One common subdivision for both signs. This is new ordinary-r
            # forced transport, not a repetition of the old ray integration.
            whole,_=inp.fields(row,piece,left,right,1,True)
            uu,vv,bb,ga,qq,qr,rho=whole
            eta=-ga*vv.mean()
            speed_bound=(up(eta.v.value().scalar())*up(qq.v.value().scalar())
                +(bb*(uu*uu-qq*qq*vv*vv).ne().primitive()).v.value().a()).upper()
            work=exact(right-left)*(4*N)*speed_bound
            parts=max(1,int(work.upper().ceil()))
            # The step condition is Nphysical*speed*h <=1/4.
            parts*=4
            if newrows+parts>PARAMETERS["maximum_new_subcells"]:
                raise ArithmeticError("the declared new transport subdivision budget is exhausted")
            boundaries=[right-(right-left)*Fraction(j,parts) for j in range(parts+1)]
            for j in range(parts):
                hi,lo=boundaries[j],boundaries[j+1];h=exact(hi-lo)
                audit={"old_interval":index,"piece":piece,"new_interval":[str(lo),str(hi)],"branches":{}}
                for sigma in (-1,1):
                    F,a=complete_taylor(inp,index,row,piece,lo,hi,order+1,mref,right,sigma)
                    proposal,end=reference_step(refs[sigma],F,a,h,N,order)
                    residual,respoly=complete_reference_residual(proposal,F,a,h)
                    whole_ref=proposal.evaluate(arb(0,h))
                    pfee,drift,dm=inp.parameter_error(index,row,piece,lo,hi,whole_ref,
                                                     mref,right,mfee,sigma)
                    source=[(residual[q]+pfee[q]).upper() for q in range(4)]
                    # The exact dyadic re-centring is a genuine reference jump.
                    jump=end-proposal.evaluate(h)
                    e,energy=gram_error_step(errors[sigma],h,source,drift)
                    errors[sigma]=[(e[q]+jump.l2(q)).upper() for q in range(4)]
                    refs[sigma]=end
                    for q in range(4):
                        source_max[sigma][q]=max(source_max[sigma][q],source[q]).upper()
                        param_max[q]=max(param_max[q],pfee[q]).upper()
                    # Complete temporary coefficients support a later signed
                    # reference consumer within this same job only.
                    detail={"force":[{"lo":p.lo,"coefficients":[z.str(80) for z in p.p]} for p in F.c],
                        "speed":[{"lo":p.lo,"coefficients":[z.str(80) for z in p.p]} for p in a.c],
                        "reference":[{"lo":p.lo,"coefficients":[z.str(80) for z in p.p]} for p in proposal.c],
                        "complete_residual":{"lo":respoly.lo,"coefficients":[z.str(80) for z in respoly.p]},
                        "error_columns":[rec(x) for x in errors[sigma]],
                        "source_error_columns":[rec(x) for x in source],
                        "mean_reference_error":rec(dm),"energy":encode(energy)}
                    b=canonical(detail);hash_source.update(b)
                    hash_reference.update(canonical(detail["reference"]))
                    audit["branches"][str(sigma)]=detail
                stream.write(canonical(audit))
                newrows+=1
            cursor=left;last_piece=piece
            if index%64==0:
                print(json.dumps(dict(stage="new-complete-nonmean-transport",
                    original_interval=index,new_subcells=newrows,exact_radial_cursor=str(cursor),
                    complete_error_H3={str(s):h3_columns(errors[s]).str(16) for s in (-1,1)})),flush=True)
    gate(doc,"the new signed reference reaches the waist through every original closed cell",
         cursor==0 and newrows>0 and len(piececount)==2550)
    gate(doc,"both branches retain all reference-error and mean columns",
         all(len(errors[s])==4 and refs[s].mean().is_zero() and refs[s].finite()
             and all(x.is_finite() for x in errors[s]) for s in (-1,1)))
    doc["complete_new_transport_conclusion"]=dict(
        root_entry=rootdiag,new_subcells=newrows,original_intervals_read=3146,
        original_candidate_pieces_read=len(piececount),
        complete_error_columns={str(s):[rec(x) for x in errors[s]] for s in (-1,1)},
        complete_error_H3={str(s):rec(h3_columns(errors[s])) for s in (-1,1)},
        maximum_complete_source_columns={str(s):[rec(x) for x in source_max[s]] for s in (-1,1)},
        maximum_complete_parameter_and_mean_columns=[rec(x) for x in param_max],
        maximum_new_partial_mean_curvature=rec(curvaturemax),
        maximum_original_mean_interpolation_error=rec(meanmax),
        full_temporary_source_sha256=sha(source_path),
        full_temporary_canonical_source_sha256=hash_source.hexdigest(),
        full_temporary_reference_sha256=hash_reference.hexdigest(),
        temporary_reference_modes=N,complete_residual_modes_not_truncated=True,
        original_scalar_integrals_not_repeated=True,ordinary_inward_radial_measure="dr")
    return refs,errors

def terminal(inp,refs,errors,doc):
    Gp,Gfee,Gaudit=finite_angle_derivative(inp.Hs,inp.Hc,inp.Ks,inp.Kc,
        Fraction(PARAMETERS["angle_tail_width"]),PARAMETERS["angle_exp_degree"])
    KH,Ej,Hdata=inp.KH,inp.Ej,inp.angledata
    chi=inp.root_data(1,True)["chi"].v.value().ne()
    rs=inp.rs.sqrt();qs={};qnorms={}
    for sigma in (-1,1):
        qpoly=refs[sigma]+sigma*chi/rs-sigma*inp.mu*(1-Gp)/2
        if not qpoly.mean().contains(0):raise ArithmeticError("the complete terminal nonmean target lost its mean")
        qpoly=qpoly.ne()
        tail=up(inp.mu)*Gfee/2
        bound=(qpoly.h3()+h3_columns(errors[sigma])+tail).upper()
        qnorms[sigma]=bound
        qs[str(sigma)]=dict(complete_signed_reference_H3=rec(qpoly.h3()),
            complete_transport_H3_error=rec(h3_columns(errors[sigma])),
            complete_finite_angle_tail_H3=rec(tail),
            complete_qG_H3=rec(bound),complete_reference_mode_extent=max(abs(qpoly.lo),abs(qpoly.hi)),
            complete_mean_is_exactly_zero=True)
    C=(KH*(qnorms[-1]+qnorms[1]+up(inp.mu)*Ej)).upper()
    gate(doc,"the true-angle output pays all finite and infinite signed Fourier terms and the actual measure",
         Gfee.is_finite() and KH.is_finite() and Ej.is_finite() and C.is_finite()
         and all(qnorms[s].is_finite() for s in (-1,1)))
    doc["complete_first_nonmean_coefficient_H3_conclusion"]=dict(
        full_real_family_transport_half_width=str(DELTA),
        true_angle_only_at_original_selected_parameter=True,
        complete_scalar_mu_copied=inp.transfer["complete_selected_parameter_finite_part"],
        branches=qs,finite_angle_new_target=encode(Gaudit),true_angle_derivatives=encode(Hdata),
        complete_nonmean_first_symbol_H3_upper=rec(C),
        norm_definition="sum_j (1+16j^2)^3 |c_j-mu*1_(j=0)|^2 under its square root",
        same_selected_parameter_and_true_mean=True,
        original_two_rays_and_KAM_not_recomputed=True,
        original_scalar_beta_not_substituted_for_this_target=True,
        linear_or_exponential_strong_return_remainder_proved=False,
        incoming_high_inverse_or_true_PDE_background_transfer_proved=False)
    # These are output bounds, not extra conditions asserting a small C.
    doc["complete"]=True
    doc["new_target_complete"]=True
    doc["new_recomputable_arrays_persisted"]=False
    doc["old_successful_mathematical_computations_repeated"]=0

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root",type=Path,required=True);ap.add_argument("--manifest",type=Path,required=True)
    ap.add_argument("--manifest-sha",required=True);ap.add_argument("--out",type=Path,required=True)
    ap.add_argument("--temporary",type=Path,required=True);ap.add_argument("--bits",type=int,default=320)
    args=ap.parse_args()
    if args.out.exists():raise FileExistsError("preserve every original successful or failed new target")
    ctx.prec=args.bits;ctx.cap=9;start=time.monotonic()
    doc=dict(kind=KIND,source_sha256=sha(__file__),helper_sha256=sha(sn.__file__),
        input_manifest_sha256=args.manifest_sha,parameters=PARAMETERS,
        complete=False,new_target_complete=False,gates=[],failure=None,
        run_id=os.environ.get("GITHUB_RUN_ID"),run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        complete_infinite_inverse_or_PDE_solution_proved=False)
    code=0
    try:
        inp=Inputs(args,doc)
        refs,errors=transport(inp,doc,args.temporary)
        terminal(inp,refs,errors,doc)
        gate(doc,"the new target makes no unverified strong-remainder incoming or PDE assertion",
            doc["old_successful_mathematical_computations_repeated"]==0
            and not doc["complete_infinite_inverse_or_PDE_solution_proved"]
            and not doc["new_recomputable_arrays_persisted"])
    except Exception as error:
        code=1;doc["complete"]=False;doc["failure"]=dict(type=type(error).__name__,message=str(error),
            traceback_frames=[dict(file=Path(f.filename).name,line=f.lineno,function=f.name)
                for f in traceback.extract_tb(error.__traceback__)[-12:]])
    doc["actual_returncode"]=code;doc["seconds"]=time.monotonic()-start
    doc["actual_gate_count"]=len(doc["gates"])
    saved=save(args.out,doc)
    print(json.dumps(dict(kind=KIND,complete=doc["complete"],actual_returncode=code,
        gates_passed=sum(v["passed"] for v in doc["gates"]),gates_total=len(doc["gates"]),
        output_bytes=saved["bytes"],output_sha256=saved["sha256"],
        within_preferred_small_limit=saved["within_preferred_small_limit"],
        complete_infinite_inverse_or_PDE_solution_proved=False)),flush=True)
    if code:raise SystemExit(code)

if __name__=="__main__":main()
