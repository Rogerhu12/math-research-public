"""WSMF: complete per-index strict physical-mean candidate, fifty-two new records.

No entry point, filesystem/network I/O, FLINT import, old producer call or old
scientific target execution. Only neutral finite jet algebra is copied. The
owner admits complete immutable inputs and makes every emitted scalar durable
before readback. Private intermediates are not separate public targets.
"""
from __future__ import annotations
import copy
import json
from fractions import Fraction
from math import factorial, comb

N0 = 388
STRICT_CUT = Fraction(76285779072683,320000000000000)
PW_CUT = Fraction(2333968743003,10000000000000)
FOLD_STRIP = Fraction(3,128)
BANDWIDTH = 384
BASIS = "ordinary derivative divided by p! q! after frozen-t0 per-index construction"
PUBLIC_NODE_ORDER = ("strict_per_index_flux_mean", "complete_physical_mean_and_four_waist_endpoints", "complete_current_negative_and_whole_receiver")
NEW_COUNTS = (32,7,13)

def require(condition, message):
    if not condition:
        raise ValueError(message)

def indices(m, p):
    require(type(m) is int and type(p) is int and 0 <= p <= m,
            "finite nonnegative triangular shape")
    return [(a, b) for a in range(p + 1) for b in range(m - a + 1)]

def at(value, path):
    for key in path:
        value = value[key]
    return value

def canonical(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False,
                      separators=(",", ":"), allow_nan=False) + "\n"

def rational(api, n, d=1):
    return api.ex(Fraction(n, d))

def finite_power(api, x, alpha, label):
    alpha = Fraction(alpha)
    if alpha < 0:
        base = api.lower(x, label)
    else:
        base = api.up(x)
        require(base >= 0, label + " nonnegative base")
        if base == 0:
            require(alpha > 0, label + " zero/nonpositive exponent")
            return api.ex(0)
    return api.up(base ** rational(api, alpha.numerator, alpha.denominator))

def upper_sum(api, values):
    return api.up(sum(values, api.ex(0)))

def whole_max(api, values):
    vv = [api.up(v) for v in values]
    require(bool(vv), "complete maximum has at least one candidate")
    return max(vv)

class Jet:
    """One fixed, complete mixed coefficient table; no numerical producer."""
    def __init__(self, api, m, p, values, label="", exact_zero=(),
                 omitted_value=False, relative_unit=False):
        self.api, self.m, self.p, self.label = api, m, p, label
        self.zero = set(exact_zero)
        self.omitted_value = bool(omitted_value)
        self.relative_unit = bool(relative_unit)
        self.c = {}
        self.source_records = {}
        for ab in indices(m, p):
            if ab == (0, 0) and self.omitted_value:
                require(ab not in values, "an omitted lift value is never filled")
                continue
            if ab in self.zero:
                self.c[ab] = api.ex(0)
            else:
                require(ab in values, label + " missing coefficient " + str(ab))
                self.c[ab] = api.up(values[ab])
        if self.relative_unit:
            require(not self.omitted_value, "relative unit needs its value")
            self.c[0, 0] = api.ex(1)

    def need(self, m, p):
        require(m <= self.m and p <= self.p,
                self.label + " insufficient mixed derivative demand")
        for ab in indices(m, p):
            require(ab in self.c, self.label + " missing actual value " + str(ab))

    def part(self, m, p, label=""):
        require(m <= self.m and p <= self.p, "complete restriction")
        ii = set(indices(m, p))
        result=Jet(self.api, m, p, {k:v for k,v in self.c.items() if k in ii},
                   label or self.label, self.zero & ii, self.omitted_value,
                   self.relative_unit)
        result.source_records={k:copy.deepcopy(v) for k,v in self.source_records.items() if k in ii}
        if getattr(self,"ordinary_basis",False):
            result.ordinary_basis=True
        return result

    def shift(self, dr, da, m, p, label=""):
        require(type(dr) is int and type(da) is int and dr >= 0 and da >= 0,
                "nonnegative mixed shift")
        require(m + dr + da <= self.m and p + dr <= self.p,
                self.label + " mixed derivative missing")
        out, zz = {}, set()
        for a,b in indices(m,p):
            src=(a+dr,b+da)
            require(src in self.c, "derivative must not read an omitted lift value")
            out[a,b] = self.api.up(
                self.api.ex(factorial(a+dr)//factorial(a)) *
                self.api.ex(factorial(b+da)//factorial(b)) * self.c[src])
            if src in self.zero:
                zz.add((a,b))
        return Jet(self.api,m,p,out,label or self.label+"_shift",zz)

    def derivative(self, dr=0, da=0, m=None, p=None, label=""):
        """Derivative of an ORDINARY normalized table supplied to the new N6 core.

        Scaled tables use shift explicitly and pay the frozen t0 conversion.
        The caller may only invoke this on a table made by ordinary_adapter.
        """
        require(getattr(self,"ordinary_basis",False),
                "ordinary derivative must not silently differentiate a scaled table")
        mm=self.m-dr-da if m is None else m
        pp=min(self.p-dr,mm) if p is None else p
        require(mm>=0 and pp>=0,"complete ordinary derivative demand")
        result=self.shift(dr,da,mm,pp,label)
        result.ordinary_basis=True
        return result

def constant(api, value, m, p, label="constant"):
    zz=set(indices(m,p)); zz.remove((0,0))
    return Jet(api,m,p,{(0,0):value},label,zz)

def radial_from_coefficients(api, coefficients, m, p, label):
    require(len(coefficients) > p, label + " radial demand")
    return Jet(api,m,p,{(a,0):coefficients[a] for a in range(p+1)},label,
               [(a,b) for a,b in indices(m,p) if b > 0])

def add(api, *jets, m, p, label="complete_sum"):
    require(bool(jets), "nonempty complete sum")
    for j in jets:
        j.need(m,p)
    vv={ab:upper_sum(api,(j.c[ab] for j in jets)) for ab in indices(m,p)}
    zz={ab for ab in indices(m,p) if all(ab in j.zero for j in jets)}
    return Jet(api,m,p,vv,label,zz)

def scale(api, jet, scalar, m=None, p=None, label="complete_scalar_product"):
    m=jet.m if m is None else m
    p=jet.p if p is None else p
    jet.need(m,p)
    return Jet(api,m,p,{ab:api.up(scalar*jet.c[ab]) for ab in indices(m,p)},
               label,jet.zero & set(indices(m,p)))

def mul(api, *jets, m, p, label="complete_ordered_product_majorant"):
    require(bool(jets), "nonempty complete product")
    result=constant(api,api.ex(1),m,p)
    for jet in jets:
        jet.need(m,p)
        values,zz={},set()
        for a,b in indices(m,p):
            terms=[]
            structural_zero=True
            for i in range(a+1):
                for j in range(b+1):
                    left,right=(i,j),(a-i,b-j)
                    terms.append(result.c[left]*jet.c[right])
                    if left not in result.zero and right not in jet.zero:
                        structural_zero=False
            values[a,b]=upper_sum(api,terms)
            if structural_zero:
                zz.add((a,b))
        result=Jet(api,m,p,values,label,zz)
    return result

def unit_relative(api, jet, lower_value, m, p, label):
    jet.need(m,p)
    denominator=api.lower(lower_value,label+" actual base lower")
    vals={ab:api.up(jet.c[ab]/denominator) for ab in indices(m,p)}
    vals[0,0]=api.ex(1)
    return Jet(api,m,p,vals,label,jet.zero,relative_unit=True)

def relative_power(api, unit, alpha, m, p, label):
    require(unit.relative_unit, label+" exact relative constant one")
    unit.need(m,p)
    alpha=Fraction(alpha)
    delta=Jet(api,m,p,{ab:(api.ex(0) if ab==(0,0) else unit.c[ab])
                       for ab in indices(m,p)},label+"_nonconstant",
              unit.zero | {(0,0)})
    result=constant(api,api.ex(1),m,p,label)
    term=constant(api,api.ex(1),m,p)
    coefficient=Fraction(1)
    for k in range(1,m+1):
        coefficient *= (alpha-(k-1))/k
        term=mul(api,term,delta,m=m,p=p)
        if coefficient:
            result=add(api,result,scale(api,term,api.ex(abs(coefficient))),
                       m=m,p=p,label=label)
    result.relative_unit=True
    result.c[0,0]=api.ex(1)
    return result

def finite_composition(api, ordinary_derivatives, argument, m, p, label):
    argument.need(m,p)
    require(len(ordinary_derivatives) > m, label+" complete outer derivative list")
    delta=Jet(api,m,p,{ab:(api.ex(0) if ab==(0,0) else argument.c[ab])
                       for ab in indices(m,p)},label+"_increment",
              argument.zero | {(0,0)})
    result=constant(api,ordinary_derivatives[0],m,p,label)
    term=constant(api,api.ex(1),m,p)
    for k in range(1,m+1):
        term=mul(api,term,delta,m=m,p=p)
        result=add(api,result,scale(api,term,
                   ordinary_derivatives[k]/api.ex(factorial(k))),
                   m=m,p=p,label=label)
    return result

def ordinary_bell(api, order, terms, values):
    cache={}
    def b(n,k):
        if n==0:
            return api.ex(1 if k==0 else 0)
        if k==0 or k>n:
            return api.ex(0)
        if (n,k) not in cache:
            cache[n,k]=upper_sum(api,(
                api.ex(comb(n-1,j-1))*values[j]*b(n-j,k-1)
                for j in range(1,n-k+2)))
        return cache[n,k]
    return b(order,terms)

def angular_composition(api, outer_ordinary, flow_ordinary, degree):
    out={}
    for b in range(degree+1):
        out[0,b]=(outer_ordinary[0] if b==0 else
          upper_sum(api,(outer_ordinary[k]*ordinary_bell(api,b,k,flow_ordinary)
                         for k in range(1,b+1)))/api.ex(factorial(b)))
    return Jet(api,degree,0,out,"complete_angular_composition")

def ordinary_angle(api, jet, q):
    require((0,q) in jet.c, "actual angle coefficient required")
    return api.up(api.ex(factorial(q))*jet.c[0,q])

def ordinary_adapter(api, jet, t_lower):
    """Working representation for a NEW residual target, never a new old graph."""
    lo=api.lower(t_lower,"strict t lower for same ordinary derivative")
    vals={ab:api.up(v/(lo**ab[0])) for ab,v in jet.c.items()}
    result=Jet(api,jet.m,jet.p,vals,jet.label+"_ordinary",jet.zero,
               jet.omitted_value,jet.relative_unit and jet.p==0)
    result.ordinary_basis=True
    return result

CURRENT_PROVIDER_RECORDS = (
    "sqrt_two_upper","ell_plus_one_fourth_upper","complete_collar_B_union_upper",
    "sqrt_ell_plus_upper","N_minus5_3_upper","ell_minus_negative_fourth_upper",
    "strict_B_t_upper","N_minus4_3_upper","C_O","C_R","jump_collar","C_1",
    "jump_strict","dyadic_one_third","dyadic_two_thirds","Bessel_prefactor",
    "complete_terminal_dyadic_contribution_upper","Rplus","RF","Lrec","Calg",
    "D_infinity","prior_whole","prior_reduced")


def copy_complete_current_WRP_provider(actual,source_identity,admission):
    """Data-only adapter for the once-successful complete WRP receiver.

    It copies the entire already-selected whole record for each operator. It
    neither evaluates a scalar nor promotes a component estimate to a whole one.
    """
    require(admission.get("complete") is True
            and admission.get("all_complete_original_bytes_and_scopes_verified") is True,
            "complete immutable WRP admission before provider decoding")
    require(set(source_identity)=={"role","path","git_blob_sha","bytes","sha256"},
            "complete immutable provider identity")
    require(actual["complete"] is True and actual["proved"] is True
            and actual["actual_returncode"]==0 and actual["stage"]=="complete"
            and actual["failure"] is None,"successful complete WRP source")
    scope=actual["retained_scope"]
    require(scope["physical_mean_coordinates"]==2
            and scope["original_true_interfaces"]==3070
            and scope["original_PW_cut"]==str(PW_CUT)
            and scope["strict_interval"]==["0",str(STRICT_CUT)]
            and scope["same_ordered_IJ_and_original_negative_windows"] is True
            and scope["entire_E3_terminal_dyadic_contribution_copied_without_subtotal_subtraction"] is True
            and scope["all_positive_root_four_waist_ends_and_ordered_readout_retained"] is True,
            "same full-mean operator, true sources, terminals, and endpoints")
    graph=actual["complete_new_graphs"]["complete_new_same_whole_receiver_conclusion"]
    require(graph["complete"] is True,"complete current ordinary and received graph")
    saved=actual["copied_original_scalar_records"]
    new=graph["new_records"]
    records={}
    for key in CURRENT_PROVIDER_RECORDS:
        if key in ("complete_collar_B_union_upper","strict_B_t_upper"):
            record=new[key]
        elif key in ("prior_whole","prior_reduced"):
            which=key.removeprefix("prior_")
            choice=actual["whole_candidate_choices"][which]
            require(choice["both_complete_candidates_retained"] is True
                    and choice["prior_wins_equal_saved_upper"] is True,
                    "two complete same-operator candidates remain available")
            record=at(actual,choice["selected_record_path"])
            require(canonical(record)==canonical(choice["complete_selected_upper"]),
                    "actual selected whole record, without new comparison arithmetic")
        else:
            record=saved[key]
        require(isinstance(record,dict) and set(record)=={"ball"}
                and isinstance(record["ball"],str),"entire original provider record")
        records[key]=copy.deepcopy(record)
    return {
        "complete":True,"same_operator_and_trial":True,"physical_mean_coordinates":2,
        "original_true_interfaces":3070,"input_order":[-4,3],
        "old_complete_terminal_copied_not_recomputed":True,
        "source_identity":copy.deepcopy(source_identity),
        "complete_runtime_binding":{key:copy.deepcopy(actual[key]) for key in
            ("run_id","run_attempt","workflow_event_commit","actual_checkout_commit",
             "manifest_sha256","scientific_modules","input_sha256","retained_scope",
             "whole_candidate_choices")},
        "records":records,
        "record_source_kind":"complete_successful_WRP_actual_only",
        "old_targets_recomputed":0}

class MeanInputs:
    """Complete admitted JSON only; this class performs no old producer call."""
    def __init__(self,api,documents,admission,provider):
        require(admission.get("complete") is True
                and admission.get("all_complete_original_bytes_and_scopes_verified") is True
                and admission.get("all_same_mean_and_current_provider_types_verified") is True,
                "full immutable typed admission precedes new arithmetic")
        roles={"wgs_main","wgs_copies","wbf","wjr","wdg","extension","wmt"}
        require(set(documents)==roles,"seven fixed mathematical predecessor roles")
        self.a,self.docs,self.provider=api,documents,provider
        self.main=documents["wgs_main"]
        self.copies=documents["wgs_copies"]
        self.old=self.copies["copied_original_scalar_records"]
        self.stage=self.copies["copied_original_stage_records"]
        self.high=self.main["complete_higher_flow_and_cut_conclusion"]
        self.wmt=documents["wmt"]
        self.mold=self.wmt["copied_original_scalar_records"]
        self.kernels=self.wmt["complete_new_graphs"][
            "complete_normalized_weight_L1_kernels"]["new_records"]
        self.extension=documents["extension"]["conclusion"]
        require(self.extension["Bext_negative_tail_retained"] is True
                and len(self.extension["Vext_derivatives"])==17
                and len(self.extension["complete_B_derivatives"])==17,
                "complete old potential and nonzero B tail")
        self.tlo=api.read_lower(self.old["t_cut_lower"],"same strict positive t lower")
        self.thi=api.read_up(self.main["complete_strict_geometry_conclusion"][
            "complete_jets"]["t"]["group_upper"][0])
        self.qlo=api.read_lower(self.old["q_lower"],"same strict positive q lower")
        self.eta_lo=api.read_lower(self.old["eta_lower"],"same strict eta lower")
        self.philo=api.read_lower(self.high["strict_phase_lower"],"same positive phases")
        self.Glo=api.read_lower(self.main["complete_strict_leading_conclusion"][
            "complete_G_lower"],"same complete G lower")
        self.G0=api.read_up(self.main["complete_strict_leading_conclusion"]["complete_G_upper"])
        geo=self.main["complete_strict_geometry_conclusion"]["complete_jets"]
        self.Q0=api.read_up(geo["Q"]["group_upper"][0])
        self.mu0=api.read_up(geo["mu_inverse"]["group_upper"][0])
        wbf,wjr=documents["wbf"],documents["wjr"]
        self.phase1=api.read_up(wbf["copied_original_scalar_records"]["phase_1"])
        ff=wbf["complete_new_graphs"]["complete_new_sharp_flow_conclusion"][
            "new_records"]["ordinary_flow_orders_2_through_15"]
        self.flow={1:api.read_up(wbf["copied_original_scalar_records"]["flow_1"])}
        self.flow.update({j:api.read_up(ff[j-2]) for j in range(2,6)})
        jg=wjr["complete_new_graphs"]
        self.pr=jg["complete_new_positive_phase_average_ratio_conclusion"][
            "new_records"]["ordinary_common_positive_phase_and_average_ratios_1_through_14"]
        self.wr=jg["complete_new_relative_omega_conclusion"]["new_records"][
            "complete_strict_relative_omega_angular_orders_1_through_14"]
        require(len(self.pr)==len(self.wr)==14 and len(ff)==14,
                "complete saved ordinary relative and absolute arrays")
        require(canonical(self.mold["wgs_d_g0"])==canonical(
                    self.main["complete_strict_coefficient_conclusion"]["new_jets"][
                        "d"]["group_upper"][0]),"same old d0 for copied kappa0")
        cert=self.main["complete_derivative_request_certificate"]
        require(cert["fixed_degree_groups"]==[
            [0,0],[1,1],[2,2],[3,3],[4,4],[5,6],[7,9],[10,12],[13,15]]
            and cert["normalized_coefficients"]=="ordinary derivative norm divided by a! b!",
            "exact ordinary old group convention")
        self.groups=cert["fixed_degree_groups"]
        require(provider["complete"] is True and provider["same_operator_and_trial"] is True
                and provider["physical_mean_coordinates"]==2
                and provider["original_true_interfaces"]==3070
                and provider["input_order"]==[-4,3]
                and provider["old_complete_terminal_copied_not_recomputed"] is True,
                "one complete current same-operator nonmean provider")
        require(set(provider["records"])==set(CURRENT_PROVIDER_RECORDS),
                "complete fixed provider record map without extra or missing fields")
        self.receiver=provider["records"]

    def r(self,name):
        return self.a.read_up(self.old[name])

    def mr(self,name):
        return self.a.read_up(self.mold[name])

    def fallback(self,jet,old):
        """Only ORDINARY same-function, same-domain normalized coefficient bounds."""
        require(old["value_omitted_for_lift"] is False,"no invented lift value")
        shape=old["shape"]
        vals=dict(jet.c)
        for i,q in indices(jet.m,jet.p):
            if i<=shape[1] and i+q<=shape[0]:
                g=next(k for k,(l,r) in enumerate(self.groups) if l<=i+q<=r)
                vals[i,q]=min(self.a.up(vals[i,q]),self.a.read_up(old["group_upper"][g]))
        return Jet(self.a,jet.m,jet.p,vals,jet.label+"_same_function_fallback",jet.zero)


def scale_radial(api,jet,tupper):
    return Jet(api,jet.m,jet.p,{(i,q):api.up(tupper**i*v)
        for (i,q),v in jet.c.items()},jet.label+"_frozen_radial",jet.zero)


def private_background(inp):
    a=inp.a
    old_pure=inp.kernels["pure_angular_background_pair_upper"]
    require(len(old_pure)==6,"all six already-computed pure background targets")
    uv={}
    for i,q in indices(6,1):
        if i==0 and q<=5:
            uv[i,q]=a.read_up(old_pure[q])
        else:
            uv[i,q]=a.up(inp.r("Q_"+str(i)+"_"+str(min(q,3)))*
                a.ex(BANDWIDTH)**max(0,q-3)/a.ex(factorial(i)*factorial(q)))
    U=Jet(a,6,1,uv,"true_physical_pair_A0")
    def radial(name,m,p):
        return radial_from_coefficients(a,[
            a.up(inp.r(name+"_"+str(i))/a.ex(factorial(i)))
            for i in range(p+1)],m,p,name+"_ordinary")
    beta,K=radial("beta",7,1),radial("K",7,1)
    q=radial("q",7,2)
    oldeta=inp.main["complete_strict_coefficient_conclusion"]["new_jets"][
        "eta"]["group_upper"]
    eta=radial_from_coefficients(a,[a.read_up(oldeta[i]) for i in range(2)],
                                7,1,"same_pure_radial_eta_ordinary")
    S=add(a,mul(a,U,U,m=6,p=1),mul(a,K,U,U,m=6,p=1),m=6,p=1)
    BS=mul(a,beta,S,m=6,p=1)
    d=Jet(a,7,1,{(i,j):a.up(BS.c[i,0]/4 if j==0 else BS.c[i,j-1]/a.ex(j))
                  for i,j in indices(7,1)},"complete_drift_A0_ordinary")
    d.c[0,0]=a.read_up(inp.mold["wgs_d_g0"])
    ell0=radial_from_coefficients(a,[a.up(2*BS.c[i,0]) for i in range(2)],
                                 7,1,"complete_radial_ell0")
    oldell=inp.main["complete_strict_coefficient_conclusion"]["new_jets"][
        "ell0"]["group_upper"][0]
    ell0.c[0,0]=a.read_up(oldell)
    one=constant(a,a.ex(1),6,1)
    UU=mul(a,U,U,m=6,p=1)
    KVV=mul(a,K,U,U,m=6,p=1)
    e=mul(a,beta,add(a,one,scale(a,UU,3),KVV,m=6,p=1),m=6,p=1)
    b=mul(a,beta,add(a,one,UU,scale(a,KVV,3),m=6,p=1),m=6,p=1)
    ell=scale(a,mul(a,beta,U,U,m=6,p=1),2)
    for name,j in (("e",e),("b_local",b),("ell",ell)):
        j.c[0,0]=a.read_up(inp.main["complete_strict_forcing_conclusion"][
            "complete_coefficient_jets"][name]["group_upper"][0])
    return {"U":U,"beta":beta,"K":K,"q":q,"eta":eta,"S":S,"d":d,
            "ell0":ell0,"e":e,"b":b,"ell":ell}


def private_geometry_and_leading(inp,bg):
    a=inp.a
    ds=scale_radial(a,bg["d"],inp.thi)
    aqs=scale_radial(a,mul(a,bg["eta"],bg["q"],m=7,p=1),inp.thi)
    vel=add(a,ds,aqs,m=7,p=1)
    pp={(0,0):a.ex(1)}
    for j in range(1,8):
        pp[0,j]=a.up(a.read_up(inp.pr[j-1])/a.ex(factorial(j)))
    for i in range(2):
        for j in range(7-i):
            vv=upper_sum(a,(vel.c[u,v]*pp[i-u,j+1-v]
                for u in range(i+1) for v in range(j+2)))
            pp[i+1,j]=a.up(inp.thi*a.ex(j+1)*vv/a.ex(i+1))
    P=Jet(a,7,2,pp,"both_positive_phase_relative",relative_unit=True)
    etas=scale_radial(a,bg["eta"],inp.thi)
    qs=scale_radial(a,bg["q"],inp.thi)
    er=unit_relative(a,etas,inp.eta_lo,7,1,"relative_eta")
    qr=unit_relative(a,qs,inp.qlo,7,2,"relative_q")
    A=mul(a,er,qr,m=7,p=1)
    x=scale(a,P,inp.phase1)
    ww={(0,0):a.ex(1)}
    for j in range(1,8):
        ww[0,j]=a.up(a.read_up(inp.wr[j-1])/a.ex(factorial(j)))
    for i in range(2):
        for j in range(7-i):
            drift=upper_sum(a,(ds.c[u,v]*a.ex(j-v+1)*ww[i-u,j-v+1]
                for u in range(i+1) for v in range(j+1)))
            source=upper_sum(a,(A.c[u,v]*x.c[i-u,j-v]
                for u in range(i+1) for v in range(j+1)))
            ww[i+1,j]=a.up((inp.thi*drift+rational(a,3,2)*inp.Q0*source)/a.ex(i+1))
    W=Jet(a,7,2,ww,"relative_actual_omega",relative_unit=True)
    tau=relative_power(a,W,Fraction(2,3),7,2,"relative_t")
    ell0=bg["ell0"]
    E=[a.ex(1),a.up(inp.thi*ell0.c[0,0]),
       a.up(inp.thi**2*(ell0.c[0,0]**2+ell0.c[1,0])/2)]
    EG=radial_from_coefficients(a,E,7,2,"relative_complete_EG")
    RG=mul(a,relative_power(a,tau,Fraction(1,4),7,2,"t_quarter"),
           relative_power(a,qr,Fraction(-1,2),7,2,"q_minus_half"),
           EG,m=7,p=2)
    RG.relative_unit=True;RG.c[0,0]=a.ex(1)
    G=scale(a,RG,inp.G0)
    pinvrel=relative_power(a,P,-1,6,0,"both_phase_reciprocals")
    pinv=scale(a,pinvrel,1/inp.philo)
    si=scale(a,relative_power(a,tau,Fraction(-1,2),6,0,"inverse_s_relative"),
             finite_power(a,inp.tlo,Fraction(-1,2),"strict t lower"))
    s=scale(a,relative_power(a,tau,Fraction(1,2),5,0,"s_relative"),
            finite_power(a,inp.thi,Fraction(1,2),"strict t upper"))
    H=add(a,scale(a,pinv,2,m=5,p=0),mul(a,s,pinv,m=5,p=0),
          mul(a,si,pinv,m=5,p=0),m=5,p=0,label="whole_H_inverse_entry_sum")
    Q=scale(a,relative_power(a,tau,Fraction(-1,2),6,0,"Q_relative"),inp.Q0)
    mu=scale(a,mul(a,tau,pinvrel,pinvrel,m=5,p=0),inp.mu0)
    t=scale(a,tau,inp.thi,m=6,p=0)
    y=mul(a,x,si,m=5,p=0)
    pp2=mul(a,P,P,m=7,p=2)
    a0s=scale(a,mul(a,G,pp2,m=7,p=2),inp.phase1**2)
    b0s=scale(a,mul(a,G,pp2,
              relative_power(a,tau,Fraction(-1,2),7,2,"b0_inverse_s"),
              m=7,p=2),inp.phase1**2*
              finite_power(a,inp.tlo,Fraction(-1,2),"strict t lower"))
    oldlead=inp.main["complete_strict_leading_conclusion"]["complete_jets"]
    a0=inp.fallback(ordinary_adapter(a,a0s,inp.tlo),oldlead["a0"])
    b0=inp.fallback(ordinary_adapter(a,b0s,inp.tlo),oldlead["b0"])
    oldgeo=inp.main["complete_strict_geometry_conclusion"]["complete_jets"]
    H=inp.fallback(H,oldgeo["H_inverse_entry_sum"])
    Q=inp.fallback(Q,oldgeo["Q"])
    mu=inp.fallback(mu,oldgeo["mu_inverse"])
    t=inp.fallback(t,oldgeo["t"])
    y=inp.fallback(y,oldgeo["y"])
    xx=inp.fallback(x.part(6,0),oldgeo["x"])
    v0=scale(a,mul(a,G,P,P,m=5,p=0),inp.phase1**2)
    v0=inp.fallback(v0,oldlead["v0"])
    return {"P":P,"tau":tau,"G_relative":RG,"x":xx,"y":y,"t":t,
            "Q":Q,"mu":mu,"H":H,"a0":a0,"b0":b0,"v0":v0,"si":si}


def private_complete_forcing(inp,bg,g):
    a=inp.a
    U,beta,K,eta,d=(bg[k] for k in ("U","beta","K","eta","d"))
    e,b,ell=bg["e"],bg["b"],bg["ell"]
    def prod(*jj):
        return mul(a,*jj,m=5,p=0)
    def addj(*jj):
        return add(a,*jj,m=5,p=0)
    def dr(j):
        return j.shift(1,0,5,0)
    def da(j):
        return j.shift(0,1,5,0)
    def D(j):
        return addj(dr(j),prod(d,da(j)))
    eratio=scale(a,dr(eta),1/inp.eta_lo)
    dp=da(d)
    meanS=constant(a,bg["S"].c[0,0],5,0)
    tQ=addj(eratio,dp,e)
    T0=addj(eratio,scale(a,prod(beta,meanS),4),scale(a,dp,5))
    rQ=addj(D(ell),prod(eta,da(e)),scale(a,prod(beta,eta,da(U),U),2),
              prod(ell,addj(eratio,dp)))
    theta=addj(scale(a,rQ,1/inp.eta_lo),scale(a,prod(beta,K,U,da(U)),2))
    V0=addj(prod(tQ,b),D(b),prod(K,addj(prod(ell,ell),
              scale(a,prod(beta,eta,U,da(U)),4))))
    second=addj(prod(d,d),prod(eta,eta,K))
    first=addj(prod(d,dp),dr(d))
    def diagonal(j):
        return addj(j.shift(2,0,5,0),scale(a,prod(d,j.shift(1,1,5,0)),2),
                    prod(second,j.shift(0,2,5,0)),prod(first,da(j)),
                    prod(T0,D(j)),prod(V0,j))
    Fb=prod(g["mu"],addj(diagonal(g["a0"]),prod(theta,g["Q"],g["t"],g["b0"])))
    Fa=prod(g["mu"],addj(diagonal(g["b0"]),prod(theta,g["Q"],g["a0"])))
    old=inp.main["complete_strict_forcing_conclusion"]["complete_forcing_jets"]
    return {"Fa":inp.fallback(Fa,old["Fa"]),"Fb":inp.fallback(Fb,old["Fb"])}

def private_free_and_genuine_transport(inp,g,forcing):
    a=inp.a
    ct={(0,0):a.ex(1)}
    cutlo=a.read_lower(inp.old["t_cut_lower"],"same true cut t lower")
    cuthi=a.read_up(inp.old["t_cut_upper"])
    t5=inp.docs["wdg"]["complete_new_graphs"]["complete_new_cut_T_high_angular_conclusion"][
        "new_records"]["ordinary_cut_T_orders_5_through_14"][0]
    for j in range(1,6):
        rec=inp.old["cut_t_"+str(j)] if j<=4 else t5
        ct[0,j]=a.up(a.read_up(rec)/(cutlo*a.ex(factorial(j))))
    CT=Jet(a,5,0,ct,"relative_true_cut_t",relative_unit=True)
    CS=scale(a,relative_power(a,CT,Fraction(1,2),5,0,"cut_s_relative"),
             finite_power(a,cuthi,Fraction(1,2),"cut t upper"))
    free={}
    for name in ("a1","b1"):
        vv={}
        for j in range(6):
            rec=(inp.stage["free_components"][name]["0"][j] if j<=3
                 else inp.old["free_old_0_"+str(j)])
            vv[0,j]=a.up(a.read_up(rec)/a.ex(factorial(j)))
        free[name]=Jet(a,5,0,vv,"true_cut_free_"+name)
    Gi=a.read_up(inp.stage["fold"]["Gi"])
    IG=Jet(a,5,0,{(0,j):a.up(Gi/a.ex(FOLD_STRIP)**j) for j in range(6)},
           "true_full_strip_cut_inverse_G")
    cp={(0,0):a.ex(1)}
    cutplow=a.read_lower(inp.high["cut_phase_lower"],"true cut phase lower")
    for j in range(1,6):
        order=j+1
        rec=(inp.old["cut_phase_"+str(order)] if order<=4 else
             inp.high["cut_phase_orders_5_through_15"][order-5])
        cp[0,j]=a.up(a.read_up(rec)/(cutplow*a.ex(factorial(j))))
    CP=Jet(a,5,0,cp,"true_cut_relative_phase",relative_unit=True)
    CPI=scale(a,relative_power(a,CP,-1,5,0,"cut_phase_inverse"),1/cutplow)
    cutR=mul(a,add(a,free["a1"],mul(a,CS,free["b1"],m=5,p=0),m=5,p=0),
             IG,CPI,CPI,m=5,p=0)
    Ginv=scale(a,relative_power(a,g["G_relative"],-1,5,0,"G_inverse"),1/inp.Glo)
    Pinv=scale(a,relative_power(a,g["P"],-1,5,0,"phase_inverse"),1/inp.philo)
    opposite=scale(a,g["P"],inp.phase1,m=5,p=0)
    kernel=scale(a,mul(a,g["Q"],opposite,Ginv,Pinv,Pinv,
                 add(a,forcing["Fa"],mul(a,g["si"],forcing["Fb"],m=5,p=0),
                     m=5,p=0),m=5,p=0),rational(a,1,2))
    cr=angular_composition(a,{j:ordinary_angle(a,cutR,j) for j in range(6)},inp.flow,5)
    kr=angular_composition(a,{j:ordinary_angle(a,kernel,j) for j in range(6)},inp.flow,5)
    R=add(a,cr,scale(a,kr,a.ex(STRICT_CUT)),m=5,p=0)
    v1=mul(a,g["v0"],R,m=5,p=0)
    af=v1
    bf=mul(a,v1,g["si"],m=5,p=0)
    oldfree=inp.main["complete_free_first_transport_conclusion"]["complete_jets"]
    af=inp.fallback(af,oldfree["a1"])
    bf=inp.fallback(bf,oldfree["b1"])
    V=finite_composition(a,[a.read_up(v) for v in inp.extension["Vext_derivatives"][:6]],
                         g["t"],5,0,"complete_Vext_of_T")
    B=finite_composition(a,[a.read_up(v) for v in inp.extension["complete_B_derivatives"][:6]],
                         g["t"],5,0,"complete_Bext_of_T_with_tail")
    V.c[0,0]=a.read_up(inp.extension["Vext_derivatives"][0])
    B.c[0,0]=a.read_up(inp.extension["complete_B_derivatives"][0])
    ae=add(a,af,mul(a,B,g["t"],g["b0"],m=5,p=0),m=5,p=0)
    be=add(a,bf,mul(a,B,g["a0"],m=5,p=0),m=5,p=0)
    def old_pure_fallback(jet,prefix):
        vals={}
        for j in range(6):
            idx=next(k for k,(l,r) in enumerate(inp.groups) if l<=j<=r)
            vals[0,j]=min(a.up(jet.c[0,j]),a.read_up(inp.mold[prefix+str(idx)]))
        return Jet(a,5,0,vals,jet.label+"_same_function_old_fallback")
    V=old_pure_fallback(V,"ext_Vext_g")
    ae=old_pure_fallback(ae,"ext_a1_g")
    be=old_pure_fallback(be,"ext_b1_g")
    W0=add(a,g["a0"],g["b0"],m=5,p=0)
    W1=add(a,ae,be,m=5,p=0)
    Fae=add(a,forcing["Fa"],mul(a,V,g["b0"],m=5,p=0),m=5,p=0)
    Fbe=add(a,forcing["Fb"],mul(a,V,g["a0"],m=5,p=0),m=5,p=0)
    return {"V":V,"B":B,"W0":W0,"W1":W1,"Fa_ext":Fae,"Fb_ext":Fbe}


def array_convolution(api,left,right,degree):
    return [upper_sum(api,(left[i]*right[j-i] for i in range(j+1)))
            for j in range(degree+1)]


def array_product(api,*arrays,degree):
    out=[api.ex(1)]+[api.ex(0)]*degree
    for values in arrays:
        require(len(values)>degree,"complete normalized angular array")
        out=array_convolution(api,out,values,degree)
    return out


def pure_array(jet,degree):
    jet.need(degree,0)
    return [jet.c[0,j] for j in range(degree+1)]


def complete_scope():
    return {
        "selected_original_real_member_only":True,
        "same_intrinsic_eta0":True,
        "strict_interval":["0",str(STRICT_CUT)],
        "original_PW_cut":str(PW_CUT),
        "physical_period":"pi/2",
        "complete_genuine_root_matrix_beta_n_and_two_reference_roles_retained":True,
        "full_genuine_Vext_Bext_tail_and_extended_forcing_retained":True,
        "complete_theta_forcing_and_second_order_drift_retained":True,
        "mean_source_unit":"n^(-23/6)",
        "new_leading_total_order":7,
        "new_leading_radial_order":2,
        "new_first_forcing_radial_order":0,
        "new_first_forcing_angular_order":5,
        "full_C_angular_order":6,
        "no_first_amplitude_radial_derivative_needed_in_exact_flux":True,
        "same_positive_actual_phase_base_frozen_before_norm":True,
        "ordinary_WJR_ratios_divided_by_factorial_once":True,
        "same_function_old_fallback_only_after_ordinary_conversion":True,
        "full_physical_Jr_and_Tk_fees_retained_readonly":True,
        "physical_mean_coordinates":2,
        "physical_mean_initial_condition":"z_ph(r_star)=0",
        "original_true_interfaces":3070,
        "no_radial_integration_by_parts":True,
        "old_local_mean_and_all_old_exponentials_readonly":True,
        "all_five_mean_steps_and_terminal_degrees_0_through_7_retained":True,
        "all_four_waist_endpoints_retained":True,
        "same_whole_and_reduced_compared_separately_old_wins_ties":True,
        "no_saved_upper_subtraction":True,
        "no_new_signed_finite_inverse_or_smallness_claim":True,
        "old_scientific_targets_recomputed":0,
    }


class NodeSink:
    def __init__(self,api,name,progress,publish_graph):
        require(name in PUBLIC_NODE_ORDER,"one declared complete natural conclusion")
        self.a,self.name,self.progress,self.publish=api,name,progress,publish_graph
        self.doc={"kind":"WSMF_complete_natural_conclusion_v1","node_name":name,
                  "complete":False,"new_records":{},"copied_original_records":{},
                  "retained_scope":complete_scope()}
        progress.clear()
        progress.update({"node_name":name,"complete":False,
             "complete_scientific_document_prefix":self.doc,"printed_record_paths":[],
             "each_printed_record_in_complete_prefix":True})
        saved=api.checkpoint_current_node(name,self.doc,progress)
        require(canonical(saved)==canonical(self.doc),"empty durable node prefix")

    def emit(self,path,value):
        require(isinstance(path,list) and bool(path),"complete unique record path")
        record=self.a.record(self.a.up(value))
        require(isinstance(record,dict) and set(record)=={"ball"}
                and isinstance(record["ball"],str),"whole printed scalar record")
        dst=self.doc["new_records"]
        for key in path[:-1]:
            dst=dst.setdefault(key,{})
        require(path[-1] not in dst,"no completed public target is evaluated twice")
        dst[path[-1]]=copy.deepcopy(record)
        self.progress["printed_record_paths"].append(list(path))
        saved=self.a.checkpoint_current_node(self.name,self.doc,self.progress)
        require(canonical(saved)==canonical(self.doc),"complete scalar prefix readback")
        return self.a.read_up(at(saved["new_records"],path))

    def copy(self,name,record,endpoint="upper"):
        require(isinstance(record,dict) and set(record)=={"ball"}
                and isinstance(record["ball"],str),"complete old scalar object")
        require(name not in self.doc["copied_original_records"],"unique old copy alias")
        self.doc["copied_original_records"][name]=copy.deepcopy(record)
        saved=self.a.checkpoint_current_node(self.name,self.doc,self.progress)
        require(canonical(saved)==canonical(self.doc),"old copy prefix readback")
        require(endpoint in ("upper","lower"),"declared original endpoint")
        if endpoint=="lower":
            return self.a.read_lower(saved["copied_original_records"][name],name)
        return self.a.read_up(saved["copied_original_records"][name])

    def finish(self,extra=None):
        expected=NEW_COUNTS[PUBLIC_NODE_ORDER.index(self.name)]
        require(len(self.progress["printed_record_paths"])==expected,"exact whole new count")
        if extra:
            self.doc.update(copy.deepcopy(extra))
        self.doc["complete"]=True
        saved=self.publish(self.name,copy.deepcopy(self.doc))
        require(canonical(saved)==canonical(self.doc),"complete natural conclusion readback")
        self.progress["complete"]=True
        return saved

def complete_strict_flux_mean(inp,sink):
    a=inp.a
    p=[sink.copy("old_p_L1_q"+str(j),r)
       for j,r in enumerate(inp.kernels["p_L1_upper"])]
    e=[sink.copy("old_e_L1_q"+str(j),r)
       for j,r in enumerate(inp.kernels["e_L1_upper"])]
    U=[sink.copy("old_background_q"+str(j),r)
       for j,r in enumerate(inp.kernels["pure_angular_background_pair_upper"])]
    require(len(p)==6 and len(e)==7 and len(U)==6,"complete unchanged WMT arrays")
    kappa=[sink.copy("old_kappa_L1_q0",inp.kernels["e_kappa_L1_upper"][0])]
    beta=sink.copy("old_strict_beta",inp.mold["strict_beta"])
    mean=sink.copy("old_strict_mean_abs",inp.mold["strict_V"])
    K=sink.copy("old_strict_K_abs",inp.mold["strict_Kabs"])
    base=sink.copy("old_strict_base",inp.mold["strict_base"])
    eta=sink.copy("old_strict_eta_lower",inp.mold["strict_eta_lower"],endpoint="lower")
    bg=private_background(inp)
    d=pure_array(bg["d"],5)
    du=array_convolution(a,d,U,5)
    zeta=[a.up(K*U[j]+du[j]/eta) for j in range(6)]
    rho=array_convolution(a,p,zeta,5)
    for j in range(1,6):
        kappa.append(sink.emit(["complete_e_kappa_L1_upper","q"+str(j)],
                               base*e[j]+2*beta*mean*rho[j]))
    g=private_geometry_and_leading(inp,bg)
    forcing=private_complete_forcing(inp,bg,g)
    ext=private_free_and_genuine_transport(inp,g,forcing)
    def prod(*jj,m=5):
        return mul(a,*jj,m=m,p=0)
    def aj(*jj,m=5):
        return add(a,*jj,m=m,p=0)
    C=aj(scale(a,bg["d"],2,m=6,p=0),
         prod(g["Q"],aj(g["t"],constant(a,a.ex(1),6,0),m=6),m=6),m=6)
    R=scale(a,relative_power(a,g["tau"],-1,5,0,"complete_T_inverse"),1/inp.tlo)
    hh={(0,0):a.up(inp.r("q_1")/inp.qlo+4*beta+4*base+4*bg["d"].c[0,1])}
    for j in range(1,6):
        hh[0,j]=a.up(4*a.ex(j+1)*bg["d"].c[0,j+1])
    h=Jet(a,5,0,hh,"complete_transport_h")
    L=aj(h,scale(a,prod(g["Q"],aj(scale(a,prod(g["x"],R),2),
                         g["y"],prod(g["y"],R))),rational(a,1,4)))
    M=aj(g["x"],g["y"])
    qe=scale(a,prod(g["Q"],aj(
        prod(aj(g["x"],g["y"]),ext["Fa_ext"]),
        prod(aj(g["y"],prod(g["x"],R)),ext["Fb_ext"]))),rational(a,1,2))
    Ca=pure_array(C,6)
    La=pure_array(L,5)
    Ma=pure_array(M,5)
    Qa=pure_array(g["Q"],5)
    Va=pure_array(ext["V"],5)
    W0=pure_array(ext["W0"],5)
    W1=pure_array(ext["W1"],5)
    eC=array_convolution(a,e,Ca,6)
    eL=array_convolution(a,e,La,5)
    BA=[a.up(2*kappa[j]+a.ex(j+1)*eC[j+1]+eL[j]) for j in range(6)]
    DA=array_product(a,e,Va,Qa,Ma,degree=5)
    EA=array_convolution(a,e,pure_array(qe,5),5)
    aw0=array_convolution(a,BA,W0,5)
    aw1=array_convolution(a,BA,W1,5)
    dw0=array_convolution(a,DA,W0,5)
    dw1=array_convolution(a,DA,W1,5)
    amplitudes={}
    for j in range(6):
        vals=(aw0[j],a.up(aw1[j]+dw0[j]+EA[j]),dw1[j])
        for k,value in enumerate(vals):
            amplitudes[j,k]=sink.emit(
                ["complete_flux_amplitude_L1_upper","k"+str(k),"q"+str(j)],value)
    H=pure_array(g["H"],5)
    c=pure_array(prod(ext["V"],g["y"]),5)
    inverse={(j,k):upper_sum(a,(H[i]*amplitudes[j-i,k] for i in range(j+1)))
             for j in range(6) for k in range(3)}
    for level in range(4):
        degree=3+level
        maxangle=4-level
        D={}
        for j in range(maxangle+1):
            for k in range(degree+1):
                direct=a.ex(j+1)*inverse.get((j+1,k),a.ex(0))
                pot=upper_sum(a,(c[i]*inverse.get((j-i,k-1),a.ex(0))
                                  for i in range(j+1)))
                D[j,k]=a.up(direct+pot)
        inverse={(j,k):upper_sum(a,(H[i]*D[j-i,k] for i in range(j+1)))
                 for j in range(maxangle+1) for k in range(degree+1)}
    terminal=[]
    for k in range(8):
        value=inverse.get((1,k),a.ex(0))+c[0]*inverse.get((0,k-1),a.ex(0))
        terminal.append(sink.emit(["complete_five_step_terminal_upper","k"+str(k)],value))
    point=sink.copy("old_single_reference_point_profile",inp.mold["point_profile"])
    cf=sink.emit(["complete_reflected_strict_mean_source_upper"],
                 2*point*upper_sum(a,(terminal[k]/a.ex(N0)**k for k in range(8))))
    return sink.finish({
        "complete_private_demand":{"leading_total":7,"leading_radial":2,
             "first_forcing_angular":5,"first_forcing_radial":0,
             "free_transport_angular":5,"C_angular":6},
        "complete_flux_degrees":[0,1,2],
        "complete_inverse_step_count":5,
        "complete_terminal_degrees":list(range(8)),
        "same_old_kappa0_copied_without_arithmetic":True,
        "full_theta_and_extended_forcing_retained":True,
        "physical_mean_source_unit":"n^(-23/6)",
        "fixed_new_per_index_branch_not_a_subtraction":True,
        "private_jet_arrays_not_public_certificates":True})


def complete_physical_mean_and_endpoints(inp,sink,mean_doc):
    a=inp.a
    require(mean_doc["complete"] is True
            and mean_doc["node_name"]==PUBLIC_NODE_ORDER[0]
            and mean_doc["physical_mean_source_unit"]=="n^(-23/6)",
            "complete saved same-unit mean source")
    cf=sink.copy("new_complete_strict_CF_read_back",
        mean_doc["new_records"]["complete_reflected_strict_mean_source_upper"])
    names=("local_mean","local_raw_mean_source","strict_backward_factor",
           "strict_absolute_coefficient","strict_k0","strict_Ik","strict_Tk",
           "endpoint_Vz","Xi23_6","endpoint_scattering","endpoint_second_order","endpoint_WT")
    old={key:sink.copy("old_"+key,inp.mold[key]) for key in names}
    Z=sink.emit(["complete_strict_mean_upper"],
                old["strict_backward_factor"]*(a.ex(STRICT_CUT)*cf+old["local_mean"]))
    Zr=sink.emit(["complete_strict_mean_derivative_upper"],
                 old["strict_absolute_coefficient"]*Z+cf)
    Ms=sink.emit(["complete_strict_raw_mean_source_upper"],
                 old["strict_k0"]*Zr+old["strict_Tk"]*Z)
    Mt=sink.emit(["complete_strict_primitive_mean_source_upper"],
                 old["strict_Ik"]*Zr+old["strict_Tk"]*Z/4)
    sink.emit(["complete_collar_raw_mean_union_upper"],
              max(a.up(Ms),a.up(old["local_raw_mean_source"])))
    Emean=sink.emit(["complete_physical_mean_endpoint_upper"],
                    old["endpoint_Vz"]*old["Xi23_6"]*Z)
    sink.emit(["complete_same_waist_endpoint_upper"],
               old["endpoint_scattering"]+old["endpoint_second_order"]+old["endpoint_WT"]+Emean)
    return sink.finish({
        "same_true_root_initial_condition":"z_ph(r_star)=0",
        "complete_old_local_mean_and_source_copied":True,
        "complete_old_signed_backward_propagator_copied":True,
        "complete_absolute_coefficient_used_for_mean_derivative":True,
        "full_k_Jr_Tk_and_feedback_paid":True,
        "both_physical_density_mean_entries_retained":True,
        "same_original_four_endpoints":True,
        "physical_mean_source_unit":"n^(-23/6)",
        "same_unit_as_original_complete_terminal_and_jumps":True})


def complete_current_negative_and_whole(inp,sink,mean_end_doc):
    a=inp.a
    require(mean_end_doc["complete"] is True
            and mean_end_doc["node_name"]==PUBLIC_NODE_ORDER[1]
            and mean_end_doc["physical_mean_source_unit"]=="n^(-23/6)",
            "complete saved physical mean and all endpoints")
    rr=inp.receiver
    old={key:sink.copy("provider_"+key,record) for key,record in rr.items()}
    new=mean_end_doc["new_records"]
    Mc=sink.copy("new_collar_raw_mean_read_back",new["complete_collar_raw_mean_union_upper"])
    Mt=sink.copy("new_strict_primitive_mean_read_back",new["complete_strict_primitive_mean_source_upper"])
    E=sink.copy("new_four_waist_endpoints_read_back",new["complete_same_waist_endpoint_upper"])
    collar=sink.emit(["complete_collar_retained_and_mean_ordinary_upper"],
         old["sqrt_two_upper"]*old["ell_plus_one_fourth_upper"]*old["complete_collar_B_union_upper"]
         +old["sqrt_ell_plus_upper"]*Mc*old["N_minus5_3_upper"])
    strict=sink.emit(["complete_strict_retained_and_mean_ordinary_upper"],
         a.ex(PW_CUT)*(old["ell_minus_negative_fourth_upper"]*old["strict_B_t_upper"]
                       +Mt*old["N_minus4_3_upper"]))
    Rc=sink.emit(["complete_collar_retained_mean_and_jumps_received_upper"],
                  old["C_O"]*collar+old["C_R"]*old["jump_collar"])
    Rs=sink.emit(["complete_strict_retained_mean_and_jumps_received_upper"],
                  old["C_1"]*(strict+old["jump_strict"]))
    Nc=sink.emit(["complete_collar_dyadic_contribution_upper"],Rc*old["dyadic_one_third"])
    Ns=sink.emit(["complete_strict_dyadic_contribution_upper"],Rs*old["dyadic_two_thirds"])
    neg=sink.emit(["complete_same_negative_error_upper"],
          old["Bessel_prefactor"]*(Nc+Ns+old["complete_terminal_dyadic_contribution_upper"]))
    nonroot=sink.emit(["complete_nonroot_source_sum_upper"],old["Rplus"]+neg+E)
    allsource=sink.emit(["complete_all_source_sum_upper"],nonroot+old["RF"])
    wholereceived=sink.emit(["complete_whole_received_source_upper"],old["Lrec"]*allsource)
    sink.emit(["complete_same_whole_error_upper"],old["Calg"]+wholereceived)
    redreceived=sink.emit(["complete_reduced_received_source_upper"],old["Lrec"]*nonroot)
    sink.emit(["complete_same_reduced_error_upper"],old["D_infinity"]+redreceived)
    return sink.finish({
        "complete_current_provider_identity":copy.deepcopy(inp.provider["source_identity"]),
        "complete_nonmean_and_terminal_bounds_readonly":True,
        "all_original_jumps_unchanged_and_no_jump_length_factor":True,
        "ordinary_dr_lengths_only_on_ordinary_sources":True,
        "original_PW_source_and_jump_windows_retained":True,
        "Calg_only_in_whole_Dinfinity_only_in_reduced":True,
        "full_finite_factors_Theta_nu_radial_head_and_physical_means_retained":True,
        "same_whole_and_reduced_operators_as_provider":True,
        "owner_selects_only_after_complete_whole_graph_is_saved":True,
        "old_candidate_wins_equal_upper":True})


def complete_new_candidates(saved_whole,provider,api):
    """Pure saved-record comparison; never forms a norm or a new scalar target."""
    require(saved_whole["complete"] is True
            and saved_whole["node_name"]==PUBLIC_NODE_ORDER[2],
            "whole new candidate must be complete before selection")
    choices={}
    for which in ("whole","reduced"):
        path=["new_records","complete_same_"+which+"_error_upper"]
        new=at(saved_whole,path)
        old=provider["records"]["prior_"+which]
        prefer_old=api.read_up(old)<=api.read_up(new)
        choices[which]={
            "selected":"old_current_complete_candidate" if prefer_old else "new_complete_strict_flux_mean",
            "selected_record":copy.deepcopy(old if prefer_old else new),
            "old_complete_record":copy.deepcopy(old),
            "new_complete_record_path":path,
            "both_complete_candidates_retained":True,
            "old_wins_equal_upper":True,
            "same_operator_only":True}
    return choices
