"""WSM: complete per-index strict mixed jets and full-output profiles.

No entry point, I/O, FLINT import, old-producer import or old target invocation.
A single future owner admits complete immutable JSON inputs. Mixed coefficient
tables are private finite working data of one scientific child, not published
certificates or independently declared targets. Only the complete profile,
ordered strict residual and same whole receiver are public natural conclusions.
Every public record is captured before a later operation and every public node
is read back canonically before a downstream public node consumes it. A failed
public target is locked; this library never starts a recovery or an old target.

All mixed coefficients use t0**p/(p! q!), with the actual t0=-T(r0,phi0)
FROZEN during differentiation. A fixed bound t_hi or inverse t_lo is used
only after the complete displayed identity is assembled. The tables never
replace all equal-total-degree coefficients by their maximum.
Background A0 and geometric/amplitude sup bounds are explicitly distinct.
"""
from __future__ import annotations
import copy
import json
from fractions import Fraction
from math import factorial, comb

N0 = 388
STRICT_CUT = Fraction(76285779072683, 320000000000000)
ROOT_HI = Fraction(2383968743003, 10000000000000)
FOLD_STRIP = Fraction(3, 128)
FREE_STRIP = Fraction(1, 512)
BANDWIDTH = 384
NODE_KIND = "complete_strict_per_index_scaled_mixed_profile_node_v1"
BASIS = "t0^p times ordinary derivative divided by p! q!; frozen actual t0"
INTERNAL_STAGE_ORDER = (
    "strict_per_index_background",
    "strict_per_index_drift",
    "strict_relative_phase_and_gap",
    "strict_absolute_fold_edges",
    "strict_fold_factors_and_inverses",
    "strict_leading_amplitudes",
    "strict_lower_order_coefficients",
    "strict_complete_first_forcing",
    "strict_complete_cut_and_transport_kernel",
    "strict_complete_free_transport",
    "strict_complete_potential_compositions",
    "strict_complete_genuine_amplitudes",
)
PUBLIC_NODE_ORDER = (
    "strict_complete_angular_profile",
    "strict_complete_ordered_N6",
    "strict_complete_whole_receiver",
)
REQUIRED_OLD_ROLES = (
    "wgs_main", "wgs_copies", "wdg",
    "extension_scalars", "Jost_scalars", "profile_geometry_strict",
    "profile_block_strict", "same_angular_J_strict", "extended_amplitude_strict", "prior_WRT",
)

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

class OrdinaryAlgebra:
    """Neutral finite algebra for the new ordered residual, no old producer."""
    def __init__(self,scalar_api):
        self.scalar=scalar_api
    def __getattr__(self,name):
        require(name in ("ex","up","lower","read_up","read_lower","record"),
                "only admitted directed scalar operations are delegated")
        return getattr(self.scalar,name)
    def _mark(self,jet):
        jet.ordinary_basis=True
        return jet
    def factory(self,m,p,values,label,omitted_value=False):
        zero=[ab for ab,v in values.items() if v==self.scalar.ex(0)]
        return self._mark(Jet(self.scalar,m,p,values,label,zero,omitted_value))
    def constant(self,value,m,p,label="constant"):
        return self._mark(constant(self.scalar,value,m,p,label))
    def zero(self,m,p,label="zero"):
        return self.constant(self.scalar.ex(0),m,p,label)
    def add(self,*jets,m,p,label="complete_sum"):
        require(all(getattr(j,"ordinary_basis",False) for j in jets),
                "ordinary input tables")
        return self._mark(add(self.scalar,*jets,m=m,p=p,label=label))
    def mul(self,*jets,m,p,label="complete_product"):
        require(all(getattr(j,"ordinary_basis",False) for j in jets),
                "ordinary input tables")
        return self._mark(mul(self.scalar,*jets,m=m,p=p,label=label))
    def scale(self,jet,value,m=None,p=None,label="complete_scale"):
        require(getattr(jet,"ordinary_basis",False),"ordinary input table")
        return self._mark(scale(self.scalar,jet,value,m=m,p=p,label=label))

class NodeSink:
    def __init__(self, api, name, progress_state, publish_graph):
        require(name in PUBLIC_NODE_ORDER, "declared public natural conclusion")
        self.api,self.name,self.progress,self.publish_graph=(
            api,name,progress_state,publish_graph)
        self.doc={"kind":NODE_KIND,"node_name":name,"complete":False,
                  "basis":BASIS,"new_records":{},
                  "copied_original_records":{},
                  "retained_scope":complete_scope()}
        progress_state.clear()
        progress_state.update({"node_name":name,"complete":False,
            "complete_scientific_document_prefix":self.doc,
            "printed_record_paths":[],
            "each_printed_record_reconstructible_at_its_complete_prefix_path":True})

    def emit(self,path,value):
        require(isinstance(path,list) and bool(path),"exact target path")
        record=self.api.record(self.api.up(value))
        require(isinstance(record,dict) and set(record)=={"ball"}
                and isinstance(record["ball"],str),"one complete ball record")
        def put(root):
            dst=root
            for key in path[:-1]:
                dst=dst.setdefault(key,{})
            require(path[-1] not in dst,"same declared target evaluated twice")
            dst[path[-1]]=copy.deepcopy(record)
        put(self.doc["new_records"])
        self.progress["printed_record_paths"].append(list(path))
        saved=self.api.checkpoint_current_node(self.name,self.doc,self.progress)
        require(canonical(saved)==canonical(self.doc),"record prefix canonical read-back")
        return self.api.read_up(at(saved["new_records"],path))

    def copy(self,name,record):
        require(isinstance(record,dict) and set(record)=={"ball"}
                and isinstance(record["ball"],str),"whole original record copy")
        require(name not in self.doc["copied_original_records"],"old copy alias")
        self.doc["copied_original_records"][name]=copy.deepcopy(record)
        saved=self.api.checkpoint_current_node(self.name,self.doc,self.progress)
        require(canonical(saved)==canonical(self.doc),"copy prefix canonical read-back")
        return self.api.read_up(saved["copied_original_records"][name])

    def jet(self,name,jet):
        table={"shape":[jet.m,jet.p],"indices":[],"bounds":[],
               "exact_zero_indices":[],"value_omitted_for_lift":jet.omitted_value,
               "relative_unit":jet.relative_unit,"basis":BASIS}
        for a,b in indices(jet.m,jet.p):
            if (a,b)==(0,0) and jet.omitted_value:
                table["indices"].append([a,b]);table["bounds"].append(None)
            elif (a,b) in jet.zero:
                table["indices"].append([a,b]);table["bounds"].append({"exact":"0"})
                table["exact_zero_indices"].append([a,b])
            elif (a,b)==(0,0) and jet.relative_unit:
                table["indices"].append([a,b]);table["bounds"].append({"exact":"1"})
            elif (a,b) in jet.source_records:
                alias=name+"_p"+str(a)+"_q"+str(b)
                jet.c[a,b]=self.copy(alias,jet.source_records[a,b])
                table["indices"].append([a,b])
                table["bounds"].append({"copied_record_name":alias})
            else:
                alias="p"+str(a)+"_q"+str(b)
                jet.c[a,b]=self.emit(["jets",name,alias],jet.c[a,b])
                table["indices"].append([a,b])
                table["bounds"].append({"record_path":["jets",name,alias]})
        self.doc.setdefault("complete_jet_tables",{})[name]=table

    def finish(self,qualifications=None):
        if qualifications:
            self.doc["qualifications"]=copy.deepcopy(qualifications)
        self.doc["complete"]=True
        saved=self.publish_graph(self.name,copy.deepcopy(self.doc))
        require(canonical(saved)==canonical(self.doc),"publisher exact canonical read-back")
        self.progress["complete"]=True
        return saved

def complete_scope():
    return {
      "selected_original_real_member_only":True,
      "strict_interval":["0",str(STRICT_CUT)],
      "fixed_intrinsic_parameter":"eta_0",
      "ordinary_physical_angle_period":"pi/2",
      "physical_frequency":"4j",
      "original_interfaces":3070,
      "full_one_sided_radial_coefficients_retained":True,
      "same_actual_lifts_and_nonzero_cut_trace":True,
      "actual_relative_omega_only_orders_1_through_14":True,
      "absolute_flow_and_phase_WBF_relative_phase_and_omega_WJR":True,
      "relative_phase_divides_same_actual_positive_base_before_norms":True,
      "no_root_T_inverse_or_individual_root_Phi_radial_extension":True,
      "physical_background_A0_geometry_amplitude_sup_are_distinct":True,
      "same_angular_J_is_read_only":True,
      "full_primitive_means_two_physical_means_and_independent_ports_retained":True,
      "all_old_successful_targets_immutable":True,
      "mixed_tables_are_private_working_coefficients_not_published_certificates":True,
      "old_producer_imports_or_calls":0,
      "new_ray_or_ODE_integrations":0,
      "old_flow_phase_and_extension_scalar_targets_recomputed":0,
      "does_not_prove_smallness_or_finite_signed_inverse":True,
    }

class _PrivateStage:
    """Finite working coefficients; never serialized or published as a result."""
    def __init__(self,name,jets,qualifications):
        self.name=name
        self.jets=dict(jets)
        self.qualifications=dict(qualifications or {})

class _WorkingSink:
    def __init__(self,name,progress_state):
        require(name in INTERNAL_STAGE_ORDER,"declared finite internal stage")
        self.name,self.progress,self.jets=name,progress_state,{}
        self.progress["current_internal_stage"]=name
        self.progress["internal_work_is_not_a_published_certificate"]=True
    def jet(self,name,jet):
        require(name not in self.jets and isinstance(jet,Jet),"complete private Jet")
        self.jets[name]=jet
    def finish(self,qualifications=None):
        self.progress.setdefault("completed_internal_stages",[]).append(self.name)
        return _PrivateStage(self.name,self.jets,qualifications)

def decode_jet(api,doc,name):
    if isinstance(doc,_PrivateStage):
        require(name in doc.jets,"complete private coefficient demand")
        return doc.jets[name]
    require(doc["complete"] is True and doc["kind"]==NODE_KIND,"complete new node")
    table=doc["complete_jet_tables"][name]
    m,p=table["shape"]
    require(table["basis"]==BASIS and table["indices"]==[list(x) for x in indices(m,p)],
            "complete ordered individual coefficient table")
    vals={};zz=set()
    for ab,entry in zip(table["indices"],table["bounds"]):
        key=tuple(ab)
        if entry is None:
            require(key==(0,0) and table["value_omitted_for_lift"],"only true lift omission")
        elif entry=={"exact":"0"}:
            vals[key]=api.ex(0);zz.add(key)
        elif entry=={"exact":"1"}:
            require(key==(0,0) and table["relative_unit"],"only exact relative unit")
            vals[key]=api.ex(1)
        elif set(entry)=={"copied_record_name"}:
            vals[key]=api.read_up(doc["copied_original_records"][entry["copied_record_name"]])
        else:
            require(set(entry)=={"record_path"},"complete record reference")
            vals[key]=api.read_up(at(doc["new_records"],entry["record_path"]))
    require([list(x) for x in indices(m,p) if x in zz]==table["exact_zero_indices"],
            "all declared exact zeros preserved")
    return Jet(api,m,p,vals,name,zz,table["value_omitted_for_lift"],table["relative_unit"])

def decode_scalar(api,doc,name):
    require(doc["complete"] is True,"complete new scalar node")
    return api.read_up(doc["new_records"]["scalars"][name])

class Inputs:
    """Only reads whole admitted documents and saved directed endpoints."""
    def __init__(self,api,documents,admission,angular_packet=None):
        require(admission.get("complete") is True
                and admission.get("all_complete_original_bytes_and_scopes_verified") is True,
                "owner must finish full immutable admission before any new arithmetic")
        require(set(documents)==set(REQUIRED_OLD_ROLES),"exact complete predecessor role set")
        self.a,self.docs=api,documents
        self.main,self.copies=documents["wgs_main"],documents["wgs_copies"]
        require(self.main["complete"] is True and self.main["proved"] is True
                and self.main["actual_returncode"]==0,"complete WGS mathematics")
        require(self.main["run_id"]=="43820816332" and self.main["run_attempt"]=="1",
                "original WGS identity")
        self.old=self.copies["copied_original_scalar_records"]
        self.stage=self.copies["copied_original_stage_records"]
        self.high=self.main["complete_higher_flow_and_cut_conclusion"]
        self.extension=documents["extension_scalars"]["conclusion"]
        self.jost=documents["Jost_scalars"]["conclusion"]
        self.profile=documents["profile_block_strict"]["conclusion"]
        self.pgeometry=documents["profile_geometry_strict"]["conclusion"]
        self.wrt=documents["prior_WRT"]
        wdg=documents["wdg"]
        require(wdg["complete"] is True and wdg["proved"] is True
                and wdg["actual_returncode"]==0,"complete new WDG predecessor")
        self.wdg=wdg["complete_new_graphs"]
        self.romega=self.wdg["complete_new_relative_omega_angular_conclusion"]["new_records"][
            "complete_strict_relative_omega_angular_orders_1_through_14"]
        self.cut_t_high=self.wdg["complete_new_cut_T_high_angular_conclusion"]["new_records"][
            "ordinary_cut_T_orders_5_through_14"]
        require(len(self.romega)==14 and len(self.cut_t_high)==10,
                "complete new ordinary WDG lists")
        require(self.high["all_shorter_intervals_both_branches_both_orientations"] is True,
                "all original directed shorter characteristic maps")
        require(self.copies["copied_complete_original_scopes"]["fa_parameters"][
                    "exact_fold_strip"]=="3/128","original full cut strip")
        require(self.profile["complete_block_includes_all_signed_Fourier_inputs"] is True
                and self.profile["two_Jost_phases_already_included"] is True
                and self.profile["full_output_zero_and_low_modes_retained"] is True,
                "complete original full-output profile scope")
        self.tlo=api.read_lower(self.old["t_cut_lower"],"strict minus T lower")
        self.thi=api.read_up(self.main["complete_strict_geometry_conclusion"][
            "complete_jets"]["t"]["group_upper"][0])
        self.eta_lo=api.read_lower(self.old["eta_lower"],"same real eta positive lower")
        self.qlo=api.read_lower(self.old["q_lower"],"same whole strict q positive lower")
        self.philo=api.read_lower(self.high["strict_phase_lower"],"same true phases")
        self.phase={j:api.read_up(self.high[
            "complete_strict_phase_angular_orders_1_through_15"][j-1])
            for j in range(1,16)}
        self.flow={j:api.read_up(self.old["flow_"+str(j)] if j<=4 else
                   self.high["flow_orders_5_through_15"][j-5]) for j in range(1,15)}
        self.positive_phase_relative=None
        self.relative_angular_source_identity=None
        self.angular_source_identity={"kind":"original_WGS_plus_complete_WDG",
            "wgs_run_id":self.main["run_id"],"wdg_run_id":wdg["run_id"]}
        if angular_packet is not None:
            require(admission.get("complete_angular_packet_verified") is True,
                    "owner must admit the complete new angular predecessor")
            require(angular_packet["kind"]=="complete_same_strict_angular_packet_v1"
                    and angular_packet["complete"] is True
                    and angular_packet["strict_interval"]==["0",str(STRICT_CUT)]
                    and angular_packet["ordinary_physical_angle_period"]=="pi/2"
                    and angular_packet["all_shorter_intervals_both_branches_both_orientations"] is True
                    and angular_packet["relative_omega_derivatives_are_ordinary"] is True,
                    "same complete strict angular predecessor type")
            require(canonical(angular_packet["strict_phase_lower"])==
                    canonical(self.high["strict_phase_lower"]),
                    "the same already established positive phase lower")
            ff=angular_packet["flow_orders_1_through_14"]
            pp=angular_packet["phase_orders_1_through_15"]
            rr=angular_packet["relative_omega_orders_1_through_14"]
            require(len(ff)==14 and len(pp)==15 and len(rr)==14,
                    "complete angular predecessor lists")
            for record in ff+pp+rr:
                require(isinstance(record,dict) and set(record)=={"ball"}
                        and isinstance(record["ball"],str),"complete saved angular record")
            require(canonical(ff[0])==canonical(self.old["flow_1"])
                    and canonical(pp[0])==canonical(self.high[
                        "complete_strict_phase_angular_orders_1_through_15"][0]),
                    "original flow1 and phase1 are immutable read-only records")
            identity=angular_packet["complete_source_identity"]
            require(isinstance(identity,dict) and set(identity)==
                        {"role","path","bytes","sha256","git_blob_sha"}
                    and type(identity["bytes"]) is int and 0<identity["bytes"]<100000
                    and isinstance(identity["role"],str) and len(identity["role"])<=64
                    and isinstance(identity["path"],str) and len(identity["path"])<=256
                    and isinstance(identity["sha256"],str) and len(identity["sha256"])==64
                    and isinstance(identity["git_blob_sha"],str) and len(identity["git_blob_sha"])==40
                    and all(c in "0123456789abcdef" for c in
                            identity["sha256"]+identity["git_blob_sha"]),
                    "complete bounded five-field admitted angular source identity")
            self.flow={j:api.read_up(ff[j-1]) for j in range(1,15)}
            self.phase={j:api.read_up(pp[j-1]) for j in range(1,16)}
            self.romega=rr
            self.angular_source_identity=copy.deepcopy(identity)
            require(admission.get("complete_relative_angular_packet_verified") is True
                    and angular_packet["relative_positive_phase_derivatives_are_ordinary"] is True
                    and angular_packet["relative_bounds_divide_same_actual_positive_base"] is True
                    and angular_packet["absolute_WBF_flow_and_phase_arrays_unchanged"] is True,
                    "same actual positive phase and omega relative predecessor")
            pr=angular_packet["positive_phase_relative_orders_1_through_14"]
            require(len(pr)==14 and all(isinstance(record,dict)
                    and set(record)=={"ball"} and isinstance(record["ball"],str)
                    for record in pr),"complete ordinary positive phase ratios")
            relative_identity=angular_packet["complete_relative_source_identity"]
            require(isinstance(relative_identity,dict) and set(relative_identity)==
                        {"role","path","bytes","sha256","git_blob_sha"}
                    and type(relative_identity["bytes"]) is int
                    and 0<relative_identity["bytes"]<100000
                    and isinstance(relative_identity["role"],str)
                    and len(relative_identity["role"])<=64
                    and isinstance(relative_identity["path"],str)
                    and len(relative_identity["path"])<=256
                    and isinstance(relative_identity["sha256"],str)
                    and len(relative_identity["sha256"])==64
                    and isinstance(relative_identity["git_blob_sha"],str)
                    and len(relative_identity["git_blob_sha"])==40
                    and all(c in "0123456789abcdef" for c in
                            relative_identity["sha256"]+relative_identity["git_blob_sha"]),
                    "complete bounded separate relative source identity")
            self.positive_phase_relative=copy.deepcopy(pr)
            self.relative_angular_source_identity=copy.deepcopy(relative_identity)
        self.Q0=api.read_up(self.main["complete_strict_geometry_conclusion"][
            "complete_jets"]["Q"]["group_upper"][0])
        self.mu0=api.read_up(self.main["complete_strict_geometry_conclusion"][
            "complete_jets"]["mu_inverse"]["group_upper"][0])
        self.G0=api.read_up(self.main["complete_strict_leading_conclusion"]["complete_G_upper"])
        self.Glo=api.read_lower(self.main["complete_strict_leading_conclusion"][
            "complete_G_lower"],"same complete G lower")
        self.sqrt_two=api.read_up(self.wrt["copied_original_scalar_records"]["sqrt_two_upper"])

    def r(self,name):
        return self.a.read_up(self.old[name])

    def radial(self,prefix,m,p):
        return radial_from_coefficients(self.a,[
            self.a.up(self.r(prefix+"_"+str(k))*self.thi**k/self.a.ex(factorial(k)))
            for k in range(p+1)],m,p,prefix)

    def old_group0(self,conclusion,name):
        return self.main[conclusion]["complete_jets"][name]["group_upper"][0]


# Complete finite internal stages. All source formulas are WSJ/WUA.
def complete_background(inp,sink):
    a=inp.a
    m,p=15,2
    pair={}
    for r,j in indices(m,p):
        saved=inp.old["Q_"+str(r)+"_"+str(min(j,3))]
        ordinary=a.read_up(saved)
        if j>3:
            ordinary=a.up(a.ex(BANDWIDTH)**(j-3)*ordinary)
        pair[r,j]=a.up(inp.thi**r*ordinary/a.ex(factorial(r)*factorial(j)))
    U=Jet(a,m,p,pair,"both_original_background_components_A0")
    U.source_records={(0,0):inp.old["Q_0_0"],(0,1):inp.old["Q_0_1"]}
    sink.jet("background_pair_A0",U)
    for name,order in (("beta",2),("K",2),("gamma",2),("q",3)):
        jet=inp.radial(name,15,order)
        jet.source_records={(0,0):inp.old[name+"_0"]}
        sink.jet(name,jet)
    er=inp.main["complete_strict_coefficient_conclusion"]["new_jets"]["eta"]["group_upper"]
    eta=radial_from_coefficients(a,[a.up(a.read_up(er[r])*inp.thi**r)
                                   for r in range(3)],15,2,"pure_radial_eta")
    eta.source_records={(0,0):er[0]}
    sink.jet("eta",eta)
    return sink.finish({
      "background_joint_A0_bounds_cover_each_component":True,
      "physical_bandwidth_384_used_only_on_original_A0_background":True,
      "eta_has_no_angular_dependence":True,
      "radial_normalization_factorial_in_original_eta_groups_already_paid":True,
      "old_Qmixed_and_radial_targets_are_read_only":True})

def complete_drift(inp,sink,background):
    a=inp.a
    U=decode_jet(a,background,"background_pair_A0")
    beta=decode_jet(a,background,"beta")
    K=decode_jet(a,background,"K")
    eta=decode_jet(a,background,"eta")
    q=decode_jet(a,background,"q")
    S=add(a,mul(a,U,U,m=14,p=2),mul(a,K,U,U,m=14,p=2),m=14,p=2,
          label="complete_u_squared_plus_K_v_squared_A0")
    BS=mul(a,beta,S,m=14,p=2)
    dc={}
    for r,j in indices(15,2):
        dc[r,j]=a.up(BS.c[r,0]/4 if j==0 else BS.c[r,j-1]/a.ex(j))
    d=Jet(a,15,2,dc,"complete_drift_A0")
    d0=inp.main["complete_strict_coefficient_conclusion"]["new_jets"]["d"]["group_upper"][0]
    d.c[0,0]=a.read_up(d0);d.source_records={(0,0):d0}
    ell0=radial_from_coefficients(a,[a.up(2*BS.c[r,0]) for r in range(3)],
                                 14,2,"complete_physical_mean_ell0")
    oldell=inp.main["complete_strict_coefficient_conclusion"]["new_jets"]["ell0"]["group_upper"][0]
    ell0.c[0,0]=a.read_up(oldell);ell0.source_records={(0,0):oldell}
    ap=mul(a,eta,q,m=15,p=2,label="radial_eta_q")
    for name,j in (("S_A0",S),("d_A0",d),("ell0",ell0),("radial_eta_q",ap)):
        sink.jet(name,j)
    return sink.finish({
      "d_equals_minus_beta_I_P_of_full_S":True,
      "I_A0_norm_one_fourth_used_only_on_true_background":True,
      "positive_angular_drift_derivatives_use_one_fewer_S_derivative":True,
      "full_physical_mean_not_deleted":True})

def complete_relative_phase_and_gap(inp,sink,background,drift):
    a=inp.a
    d=decode_jet(a,drift,"d_A0")
    ap=decode_jet(a,drift,"radial_eta_q")
    velocity=add(a,d,ap,m=15,p=2)
    pr={(0,0):a.ex(1)}
    for j in range(1,15):
        if inp.positive_phase_relative is None:
            pr[0,j]=a.up(inp.phase[j+1]/(inp.philo*a.ex(factorial(j))))
        else:
            # WJR.21: divide the SAME actual positive base before norms.
            # Its denominator is frozen at this Taylor base, never differentiated.
            pr[0,j]=a.up(a.read_up(inp.positive_phase_relative[j-1])/a.ex(factorial(j)))
    for r in range(3):
        for j in range(14-r):
            terms=[]
            for u in range(r+1):
                for v in range(j+2):
                    terms.append(velocity.c[u,v]*pr[r-u,j+1-v])
            pr[r+1,j]=a.up(inp.thi*a.ex(j+1)*upper_sum(a,terms)/a.ex(r+1))
    P=Jet(a,14,3,pr,"both_true_phase_relative_derivative_bounds",relative_unit=True)
    eta=decode_jet(a,background,"eta")
    q=decode_jet(a,background,"q")
    erel=unit_relative(a,eta,inp.eta_lo,14,2,"relative_eta")
    qrel=unit_relative(a,q,inp.qlo,14,2,"relative_q")
    A=mul(a,erel,qrel,m=14,p=2)
    x=scale(a,P,inp.phase[1],14,3,"complete_x")
    wg={(0,0):a.ex(1)}
    for j in range(1,15):
        wg[0,j]=a.up(a.read_up(inp.romega[j-1])/a.ex(factorial(j)))
    for r in range(3):
        for j in range(14-r):
            drift_terms=[]
            source_terms=[]
            for u in range(r+1):
                for v in range(j+1):
                    drift_terms.append(d.c[u,v]*a.ex(j-v+1)*wg[r-u,j-v+1])
                    source_terms.append(A.c[u,v]*x.c[r-u,j-v])
            wg[r+1,j]=a.up((inp.thi*upper_sum(a,drift_terms)
                    +rational(a,3,2)*inp.Q0*upper_sum(a,source_terms))/a.ex(r+1))
    W=Jet(a,14,3,wg,"relative_actual_omega",relative_unit=True)
    tau=relative_power(a,W,Fraction(2,3),14,3,"relative_minus_T")
    for name,j in (("phase_relative_both",P),("omega_relative",W),("t_relative",tau),
                   ("common_x_u_bound",x)):
        sink.jet(name,j)
    return sink.finish({
      "same_actual_base_value_divided_out_before_positive_triangle":True,
      "saved_complete_ordinary_phase_1_15_read_without_recomputation":True,
      "admitted_ordinary_relative_omega_1_14_divided_by_factorial_once":True,
      "ordinary_positive_phase_ratio_1_14_divided_by_factorial_once":True,
      "phase_radial_recurrence_uses_eta_q_and_complete_d":True,
      "gap_radial_recurrence_uses_complete_eta_q_relative_product":True,
      "t0_is_frozen_not_differentiated":True,
      "relative_omega_15_not_claimed":True})

def complete_absolute_fold_edges(inp,sink,drift,relative):
    a=inp.a
    P=decode_jet(a,relative,"phase_relative_both")
    tau=decode_jet(a,relative,"t_relative")
    x=scale(a,P,inp.phase[1],14,3,"X_phi")
    # The common half-sum/half-difference majorant includes both true phases.
    u=scale(a,P,inp.phase[1],14,3,"omega_phi")
    invs=scale(a,relative_power(a,tau,Fraction(-1,2),14,3,"relative_inverse_s"),
               finite_power(a,inp.tlo,Fraction(-1,2),"actual t lower"),label="inverse_s")
    tphi=mul(a,u,invs,m=14,p=3)
    tt={ab:a.up(inp.thi*tau.c[ab]) for ab in indices(14,3)}
    for r,j in indices(15,3):
        if (r,j) not in tt:
            require(j>=1,"all radial-only T derivatives were already retained")
            tt[r,j]=a.up(tphi.c[r,j-1]/a.ex(j))
    T=Jet(a,15,3,tt,"absolute_minus_T")
    y=T.shift(0,1,14,3,"absolute_T_phi")
    d=decode_jet(a,drift,"d_A0")
    ap=decode_jet(a,drift,"radial_eta_q")
    dx=add(a,mul(a,d,x,m=14,p=2),mul(a,ap,u,m=14,p=2),m=14,p=2)
    phir=mul(a,add(a,d,ap,m=14,p=2),x,m=14,p=2)
    X,Phi={},{}
    for r,j in indices(15,3):
        if r==0 and j==0:
            continue
        if j>=1:
            X[r,j]=a.up(x.c[r,j-1]/a.ex(j))
            Phi[r,j]=a.up(x.c[r,j-1]/a.ex(j))
        else:
            X[r,0]=a.up(inp.thi*dx.c[r-1,0]/a.ex(r))
            Phi[r,0]=a.up(inp.thi*phir.c[r-1,0]/a.ex(r))
    XX=Jet(a,15,3,X,"true_X_derivatives",omitted_value=True)
    PP=Jet(a,15,3,Phi,"both_true_lift_derivatives",omitted_value=True)
    for name,j in (("T_absolute",T),("X_derivatives",XX),("Phi_derivatives",PP)):
        sink.jet(name,j)
    return sink.finish({
      "absolute_edge_15_uses_t_phi_equals_u_over_s":True,
      "relative_omega_order_15_not_requested":True,
      "true_lift_value_is_omitted_not_zero":True,
      "all_radial_only_lift_derivatives_come_from_actual_PDE":True,
      "u_fold_is_distinct_from_physical_u":True})

def complete_fold_factors_and_inverses(inp,sink,background,relative):
    a=inp.a
    P=decode_jet(a,relative,"phase_relative_both")
    tau=decode_jet(a,relative,"t_relative")
    eta=decode_jet(a,background,"eta")
    q=decode_jet(a,background,"q")
    erel=unit_relative(a,eta,inp.eta_lo,13,2,"relative_eta")
    qrel=unit_relative(a,q,inp.qlo,13,2,"relative_q")
    srel=relative_power(a,tau,Fraction(1,2),13,2,"relative_s")
    sirel=relative_power(a,tau,Fraction(-1,2),13,2,"relative_inverse_s")
    s=scale(a,srel,finite_power(a,inp.thi,Fraction(1,2),"t upper"))
    si=scale(a,sirel,finite_power(a,inp.tlo,Fraction(-1,2),"t lower"))
    pinv=scale(a,relative_power(a,P,-1,13,2,"relative_phase_inverse"),1/inp.philo)
    H=add(a,scale(a,pinv,2),mul(a,s,pinv,m=13,p=2),
          mul(a,si,pinv,m=13,p=2),m=13,p=2,label="complete_physical_H_inverse_entry_sum")
    Q=scale(a,mul(a,erel,qrel,sirel,m=13,p=2),inp.Q0,label="complete_Q")
    q0rec=inp.main["complete_strict_geometry_conclusion"]["complete_jets"]["Q"]["group_upper"][0]
    Q.c[0,0]=a.read_up(q0rec);Q.source_records={(0,0):q0rec}
    epinv=relative_power(a,erel,-2,13,2,"relative_eta_inverse_squared")
    qpinv=relative_power(a,qrel,-2,13,2,"relative_q_inverse_squared")
    pp=relative_power(a,P,-1,13,2,"relative_phase_inverse")
    mu=scale(a,mul(a,tau,epinv,qpinv,pp,pp,m=13,p=2),
             inp.mu0,label="complete_mu_inverse")
    murec=inp.main["complete_strict_geometry_conclusion"]["complete_jets"]["mu_inverse"]["group_upper"][0]
    mu.c[0,0]=a.read_up(murec);mu.source_records={(0,0):murec}
    for name,j in (("H_inverse_entry_sum",H),("Q",Q),("mu_inverse",mu)):
        sink.jet(name,j)
    return sink.finish({
      "H_inverse_has_both_diagonals_and_both_offdiagonals":True,
      "ha_and_hb_bounded_by_complete_two_phase_reciprocals":True,
      "variable_nonunitary_s_similarity_not_used_as_physical_isometry":True,
      "mu_inverse_uses_eta_q_and_both_phase_reciprocals":True,
      "all_denominators_are_actual_positive_original_lowers":True})

def complete_leading_amplitudes(inp,sink,background,drift,relative):
    a=inp.a
    tau=decode_jet(a,relative,"t_relative")
    P=decode_jet(a,relative,"phase_relative_both")
    q=decode_jet(a,background,"q")
    ell0=decode_jet(a,drift,"ell0")
    qrel=unit_relative(a,q,inp.qlo,14,3,"relative_radial_q")
    E=[a.ex(1),a.up(inp.thi*ell0.c[0,0]),
       a.up((inp.thi**2*ell0.c[0,0]**2+inp.thi*ell0.c[1,0])/2),
       a.up((inp.thi**3*ell0.c[0,0]**3
             +3*inp.thi**2*ell0.c[0,0]*ell0.c[1,0]
             +2*inp.thi*ell0.c[2,0])/6)]
    EG=radial_from_coefficients(a,E,14,3,"relative_complete_EG")
    RG=mul(a,relative_power(a,tau,Fraction(1,4),14,3,"relative_t_quarter"),
           relative_power(a,qrel,Fraction(-1,2),14,3,"relative_q_minus_half"),
           EG,m=14,p=3,label="relative_complete_G")
    RG.relative_unit=True;RG.c[0,0]=a.ex(1)
    G=scale(a,RG,inp.G0)
    pp=mul(a,P,P,m=14,p=3)
    a0=scale(a,mul(a,G,pp,m=14,p=3),inp.phase[1]**2,
             label="complete_a0_from_half_sum_of_G_p_sigma_squared")
    # This full upper covers both p_sigma. No signed upper is subtracted.
    b0=scale(a,mul(a,G,pp,
             relative_power(a,tau,Fraction(-1,2),14,3,"relative_inverse_s"),
             m=14,p=3),inp.phase[1]**2*
             finite_power(a,inp.tlo,Fraction(-1,2),"t lower"),
             label="complete_b0_from_true_half_difference")
    v0=scale(a,mul(a,G,pp,m=12,p=2),inp.phase[1]**2,
             label="both_complete_v0")
    for name,j in (("G_relative",RG),("a0",a0),("b0",b0),("v0_both",v0)):
        sink.jet(name,j)
    return sink.finish({
      "G0_upper_and_lower_are_original_complete_records":True,
      "EG_r_equals_minus_ell0_EG_full_mean_retained":True,
      "q_radial_three_and_ell0_radial_two_retained":True,
      "a0_equals_G_times_phase_square_halfsum":True,
      "b0_true_phase_square_halfdifference_bounded_after_identity":True,
      "v0_sigma_equals_G_p_sigma_squared_positive":True})

def complete_lower_order_coefficients(inp,sink,background):
    a=inp.a
    U=decode_jet(a,background,"background_pair_A0")
    beta=decode_jet(a,background,"beta")
    K=decode_jet(a,background,"K")
    mm,pp=14,2
    UU=mul(a,U,U,m=mm,p=pp)
    KVV=mul(a,K,U,U,m=mm,p=pp)
    one=constant(a,a.ex(1),mm,pp)
    e=mul(a,beta,add(a,one,scale(a,UU,3),KVV,m=mm,p=pp),m=mm,p=pp)
    b=mul(a,beta,add(a,one,UU,scale(a,KVV,3),m=mm,p=pp),m=mm,p=pp)
    ell=scale(a,mul(a,beta,U,U,m=mm,p=pp),2)
    for name,j in (("e",e),("b_local",b),("ell",ell)):
        old=inp.main["complete_strict_forcing_conclusion"]["complete_coefficient_jets"][name]["group_upper"][0]
        j.c[0,0]=a.read_up(old);j.source_records={(0,0):old}
        sink.jet(name,j)
    return sink.finish({
      "same_full_background_A0_bound_applied_to_both_components":True,
      "L11_bound_is_e_and_L22_bound_is_b_local":True,
      "coefficient_signs_remain_in_exact_operator_not_in_norm_table":True,
      "all_intermediate_mean_projection_words_retained":True})

def complete_first_forcing(inp,sink,background,drift,relative,geometry,leading,lower):
    a=inp.a
    m,p=12,1
    U=decode_jet(a,background,"background_pair_A0")
    beta=decode_jet(a,background,"beta")
    eta=decode_jet(a,background,"eta")
    K=decode_jet(a,background,"K")
    d=decode_jet(a,drift,"d_A0")
    S=decode_jet(a,drift,"S_A0")
    e=decode_jet(a,lower,"e")
    b=decode_jet(a,lower,"b_local")
    ell=decode_jet(a,lower,"ell")
    def product(*jj):
        return mul(a,*jj,m=m,p=p)
    def summ(*jj):
        return add(a,*jj,m=m,p=p)
    def dr(j):
        return scale(a,j.shift(1,0,m,p),1/inp.tlo)
    def da(j):
        return j.shift(0,1,m,p)
    def D(j):
        return summ(dr(j),product(d,da(j)))
    erel=unit_relative(a,eta,inp.eta_lo,m,p,"relative_eta")
    einv=scale(a,relative_power(a,erel,-1,m,p,"relative_eta_inverse"),1/inp.eta_lo)
    eratio=product(dr(eta),einv)
    dp=da(d)
    meanS=radial_from_coefficients(a,[S.c[r,0] for r in range(3)],
                                   14,2,"complete_mean_S")
    tQ=summ(eratio,dp,e)
    T0=summ(eratio,scale(a,product(beta,meanS),4),scale(a,dp,5))
    rQ=summ(D(ell),product(eta,da(e)),scale(a,product(beta,eta,da(U),U),2),
             product(ell,summ(eratio,dp)))
    theta=summ(product(rQ,einv),scale(a,product(beta,K,U,da(U)),2))
    V0=summ(product(tQ,b),D(b),product(K,summ(product(ell,ell),
                          scale(a,product(beta,eta,U,da(U)),4))))
    second=summ(product(d,d),product(eta,eta,K))
    drift_first=summ(product(d,dp),dr(d))
    aa=decode_jet(a,leading,"a0")
    bb=decode_jet(a,leading,"b0")
    Q=decode_jet(a,geometry,"Q")
    mu=decode_jet(a,geometry,"mu_inverse")
    tau=decode_jet(a,relative,"t_relative")
    T=scale(a,tau,inp.thi,m,p,"complete_T_for_first_forcing")
    def diagonal(j):
        return summ(scale(a,j.shift(2,0,m,p),1/(inp.tlo**2)),
                    scale(a,product(d,j.shift(1,1,m,p)),2/inp.tlo),
                    product(second,j.shift(0,2,m,p)),
                    product(drift_first,da(j)),product(T0,D(j)),product(V0,j))
    Fb=product(mu,summ(diagonal(aa),product(theta,Q,T,bb)))
    Fa=product(mu,summ(diagonal(bb),product(theta,Q,aa)))
    for name,j in (("tQ",tQ),("T0",T0),("rQ",rQ),("theta",theta),("V0",V0),
                   ("Fb",Fb),("Fa",Fa)):
        sink.jet(name,j)
    return sink.finish({
      "complete_WUA_first_forcing_with_theta_Hinverse_HD_retained":True,
      "H_D_is_phase_matrix_not_radial_derivative_of_H":True,
      "both_Airy_components_and_all_drift_product_derivatives_retained":True,
      "second_order_requires_leading_radial_three":True,
      "eta_radial_two_and_q_radial_three_not_suppressed":True,
      "all_frozen_t0_shifts_paid_before_positive_bound":True})

def complete_cut_and_transport_kernel(inp,sink,relative,geometry,leading,forcing):
    a=inp.a
    m,p=12,1
    P=decode_jet(a,relative,"phase_relative_both")
    tau=decode_jet(a,relative,"t_relative")
    Q=decode_jet(a,geometry,"Q")
    RG=decode_jet(a,leading,"G_relative")
    Fa=decode_jet(a,forcing,"Fa")
    Fb=decode_jet(a,forcing,"Fb")
    invG=scale(a,relative_power(a,RG,-1,m,p,"relative_G_inverse"),1/inp.Glo)
    invp=scale(a,relative_power(a,P,-1,m,p,"relative_phase_inverse"),1/inp.philo)
    invs=scale(a,relative_power(a,tau,Fraction(-1,2),m,p,"relative_inverse_s"),
               finite_power(a,inp.tlo,Fraction(-1,2),"strict t lower"))
    absphase=scale(a,P,inp.phase[1],m,p)
    pair=add(a,Fa,mul(a,invs,Fb,m=m,p=p),m=m,p=p)
    kernel=scale(a,mul(a,Q,absphase,invG,invp,invp,pair,m=m,p=p),rational(a,1,2),
                 label="both_complete_K_sigma")
    # At rc use the actual same analytic germ and true phase lower, never
    # the global mixed v0-inverse derivative group.
    cutlo=a.read_lower(inp.old["t_cut_lower"],"original cut t")
    cuthi=a.read_up(inp.old["t_cut_upper"])
    cut={ (0,0):a.ex(1) }
    for j in range(1,13):
        rr=inp.old["cut_t_"+str(j)] if j<=4 else inp.cut_t_high[j-5]
        cut[0,j]=a.up(a.read_up(rr)/(cutlo*a.ex(factorial(j))))
    ct=Jet(a,12,0,cut,"relative_true_cut_t",relative_unit=True)
    cs=scale(a,relative_power(a,ct,Fraction(1,2),12,0,"relative_cut_s"),
             finite_power(a,cuthi,Fraction(1,2),"complete cut t upper"))
    free={}
    for name in ("a1","b1"):
        values={}
        for j in range(13):
            if j<=3:
                raw=inp.stage["free_components"][name]["0"][j]
                val=a.read_up(raw)
            elif j<=6:
                # These are p=0 TWO-COMPONENT SUMS, not a1/b1 separate rows.
                val=inp.r("free_old_0_"+str(j))
            else:
                base=a.read_up(inp.stage["free_components"][name]["0"][3])
                val=a.up(a.ex(factorial(j-3))*base/
                         (a.ex(FREE_STRIP)**(j-3)))
            values[0,j]=a.up(val/a.ex(factorial(j)))
        free[name]=Jet(a,12,0,values,"true_cut_free_"+name)
    Gi=a.read_up(inp.stage["fold"]["Gi"])
    ginv=Jet(a,12,0,{(0,j):a.up(Gi/(a.ex(FOLD_STRIP)**j)) for j in range(13)},
             "same_cut_holomorphic_G_inverse")
    plow=a.read_lower(inp.high["cut_phase_lower"],"original real cut phase lower")
    pp={(0,0):a.ex(1)}
    for j in range(1,13):
        order=j+1
        raw=(inp.old["cut_phase_"+str(order)] if order<=4 else
             inp.high["cut_phase_orders_5_through_15"][order-5])
        pp[0,j]=a.up(a.read_up(raw)/(plow*a.ex(factorial(j))))
    cp=Jet(a,12,0,pp,"both_true_cut_phase_relative",relative_unit=True)
    cpinv=scale(a,relative_power(a,cp,-1,12,0,"cut_phase_inverse"),1/plow)
    cutpair=add(a,free["a1"],mul(a,cs,free["b1"],m=12,p=0),m=12,p=0)
    cutR=mul(a,cutpair,ginv,cpinv,cpinv,m=12,p=0,label="both_true_nonzero_cut_R")
    sink.jet("complete_transport_kernel_both",kernel)
    sink.jet("complete_nonzero_cut_ratio_both",cutR)
    return sink.finish({
      "cut_G_and_inverse_G_on_original_full_3_over_128_strip":True,
      "real_phase_lower_used_only_in_finite_real_reciprocal_chain":True,
      "no_complex_phase_nonzero_claim_from_a_real_lower":True,
      "free_old_first_index_is_radial_order_not_component":True,
      "component_p0_q0_3_and_old_p0_two_component_q4_6_are_read_only":True,
      "only_missing_cut_free_q7_12_use_full_saved_strip_Cauchy":True,
      "both_characteristic_branch_kernels_are_complete":True,
      "cut_trace_not_restarted_at_zero":True})

def complete_free_transport(inp,sink,drift,relative,leading,cutkernel):
    a=inp.a
    cutR=decode_jet(a,cutkernel,"complete_nonzero_cut_ratio_both")
    kernel=decode_jet(a,cutkernel,"complete_transport_kernel_both")
    d=decode_jet(a,drift,"d_A0")
    aq=decode_jet(a,drift,"radial_eta_q")
    velocity=add(a,d,aq,m=12,p=2)
    cutord={j:ordinary_angle(a,cutR,j) for j in range(13)}
    kord={j:ordinary_angle(a,kernel,j) for j in range(13)}
    cr=angular_composition(a,cutord,inp.flow,12)
    kr=angular_composition(a,kord,inp.flow,12)
    vals={(0,j):a.up(cr.c[0,j]+a.ex(STRICT_CUT)*kr.c[0,j]) for j in range(13)}
    for j in range(12):
        term=upper_sum(a,(velocity.c[0,k]*a.ex(j-k+1)*vals[0,j-k+1]
                           for k in range(j+1)))
        vals[1,j]=a.up(inp.thi*(term+kernel.c[0,j]))
    for j in range(11):
        terms=upper_sum(a,(
          velocity.c[1,k]*a.ex(j-k+1)*vals[0,j-k+1]
          +velocity.c[0,k]*a.ex(j-k+1)*vals[1,j-k+1]
          for k in range(j+1)))
        vals[2,j]=a.up(inp.thi*(terms+kernel.c[1,j])/2)
    R=Jet(a,12,2,vals,"both_complete_R_sigma")
    v0=decode_jet(a,leading,"v0_both")
    v1=mul(a,v0,R,m=12,p=2)
    tau=decode_jet(a,relative,"t_relative")
    si=scale(a,relative_power(a,tau,Fraction(-1,2),12,2,"relative_inverse_s"),
             finite_power(a,inp.tlo,Fraction(-1,2),"strict t lower"))
    a1=v1
    b1=mul(a,v1,si,m=12,p=2)
    for name,j in (("R_both",R),("a1_free",a1),("b1_free",b1)):
        sink.jet(name,j)
    return sink.finish({
      "ordinary_dr_integral_bound_uses_true_original_strict_length_once":True,
      "all_shorter_directed_characteristic_derivatives_read_only":True,
      "R_r_velocity_R_phi_plus_K_and_complete_R_rr_retained":True,
      "kernel_radial_derivative_kept":True,
      "both_branch_average_and_difference_retained":True,
      "new_ray_integrations":0})

def complete_potential_compositions(inp,sink,edges):
    a=inp.a
    T=decode_jet(a,edges,"T_absolute")
    original_V=inp.extension["Vext_derivatives"]
    original_B=inp.extension["complete_B_derivatives"]
    require(len(original_V)==17 and len(original_B)==17
            and inp.extension["Bext_negative_tail_retained"] is True,
            "complete existing C64 extension and nonzero B tail")
    V=[a.read_up(r) for r in original_V]
    B=[a.read_up(r) for r in original_B]
    jj={
      "V_of_T":finite_composition(a,V,T,12,2,"complete_Vext_of_T"),
      "B_of_T":finite_composition(a,B,T,12,2,"complete_Bext_of_T"),
      "Bprime_of_T":finite_composition(a,B[1:],T,12,2,"complete_Bext_prime_of_T")}
    for name,j in jj.items():
        base=(original_V[0] if name=="V_of_T" else
              original_B[1] if name=="Bprime_of_T" else original_B[0])
        j.c[0,0]=a.read_up(base);j.source_records={(0,0):base}
        sink.jet(name,j)
    return sink.finish({
      "old_full_C64_and_B_tail_derivatives_not_recomputed":True,
      "complete_B_nonzero_negative_tail_in_every_composition":True,
      "all_finite_mixed_chain_terms_through_total12_radial2":True})

def complete_genuine_amplitudes(inp,sink,edges,leading,free,potential):
    a=inp.a
    aa=decode_jet(a,leading,"a0")
    bb=decode_jet(a,leading,"b0")
    a1=decode_jet(a,free,"a1_free")
    b1=decode_jet(a,free,"b1_free")
    T=decode_jet(a,edges,"T_absolute")
    B=decode_jet(a,potential,"B_of_T")
    Bp=decode_jet(a,potential,"Bprime_of_T")
    ae=add(a,a1,mul(a,B,T,bb,m=12,p=2),m=12,p=2)
    be=add(a,b1,mul(a,B,aa,m=12,p=2),m=12,p=2)
    in2a=mul(a,B,T,be,m=12,p=2)
    in2b=add(a,mul(a,B,ae,m=12,p=2),mul(a,Bp,bb,m=12,p=2),m=12,p=2)
    in3b=mul(a,Bp,be,m=12,p=2)
    for name,j in (("a1_ext",ae),("b1_ext",be),("IN2_a",in2a),
                   ("IN2_b",in2b),("IN3_b",in3b)):
        sink.jet(name,j)
    return sink.finish({
      "w1_ext_equals_free_w1_plus_complete_B_KT_w0":True,
      "all_cB_squared_and_first_Airy_cross_terms_retained":True,
      "IN3_a_identically_zero_by_exact_two_by_two_product":True,
      "second_reference_port_not_removed":True})

def log_relative_coefficients(api, unit, m, p, label):
    require(unit.relative_unit,"actual relative unit for finite logarithmic derivatives")
    delta=Jet(api,m,p,{ab:(api.ex(0) if ab==(0,0) else unit.c[ab])
                       for ab in indices(m,p)},label+"_increment",
              unit.zero | {(0,0)})
    total=constant(api,api.ex(0),m,p,label)
    total.zero.add((0,0))
    term=constant(api,api.ex(1),m,p)
    for k in range(1,m+1):
        term=mul(api,term,delta,m=m,p=p)
        total=add(api,total,scale(api,term,rational(api,1,k)),m=m,p=p,label=label)
    total.c[0,0]=api.ex(0);total.zero.add((0,0))
    return total

def normalized_budget_jet(api, jet, positive_budget, label):
    """Relative to a positive saved MAJORANT, never a nonzero-function claim."""
    den=api.lower(positive_budget,label+" positive saved budget constant")
    vals={ab:api.up(jet.c[ab]/den) for ab in indices(jet.m,jet.p)}
    vals[0,0]=api.ex(1)
    return Jet(api,jet.m,jet.p,vals,label,jet.zero,relative_unit=True)

def coefficientwise_complete_max(api,jets,m,p,label):
    require(bool(jets),"full finite candidate collection")
    for jet in jets:
        jet.need(m,p)
    vals={ab:whole_max(api,[j.c[ab] for j in jets]) for ab in indices(m,p)}
    result=Jet(api,m,p,vals,label,
               [ab for ab in indices(m,p) if all(ab in j.zero for j in jets)])
    if all(j.relative_unit for j in jets):
        result.relative_unit=True;result.c[0,0]=api.ex(1)
    return result

def complete_angular_profile(inp,sink,relative):
    a=inp.a
    tau=decode_jet(a,relative,"t_relative").part(4,0,"pure_angular_relative_q")
    old=inp.profile
    rows=old["new_complete_records"]
    near_records=old["complete_near_scaled_ODE_derivatives_0_5"]
    require(len(near_records)==6,"complete original near-ODE derivatives")
    near=[a.read_up(r) for r in near_records]
    xmax=a.read_up(rows["complete_scaled_near_T_upper"])
    xi=scale(a,tau,xmax,4,0,"new_complete_scaled_T_angular_increment")
    ny=finite_composition(a,near,xi,4,0,"new_near_Y_envelope")
    nyp=finite_composition(a,near[1:],xi,4,0,"new_near_Yprime_envelope")
    nyrel=normalized_budget_jet(a,ny,near[0],"near_Y_budget")
    nyprel=normalized_budget_jet(a,nyp,near[1],"near_Yprime_budget")
    nr=coefficientwise_complete_max(a,[nyrel,nyprel],4,0,
                                   "complete_two_near_summand_relative_majorant")
    near0=old["complete_profile_jets"]["near_profile"]["group_upper"][0]
    nearnew=scale(a,nr,a.read_up(near0),label="new_complete_near_profile")
    nearnew.c[0,0]=a.read_up(near0);nearnew.source_records={(0,0):near0}
    # Old near0 >= nb*(A0+N0^-1/3*A1), for its complete same positive
    # algorithm. The max bounds EACH entire summand relative to that same
    # saved positive budget. No lower bound on Y or Y' is asserted.
    logt=scale(a,log_relative_coefficients(a,tau,4,0,"log_actual_q"),rational(a,3,2))
    E=[a.read_up(r) for r in inp.jost["complete_Euler_a_0_4"]]
    Ep=[a.read_up(r) for r in inp.jost["complete_Euler_aprime_0_4"]]
    require(len(E)==5 and len(Ep)==5,"complete old five Euler derivatives")
    aa=finite_composition(a,E,logt,4,0,"new_complete_far_a")
    ap=finite_composition(a,Ep,logt,4,0,"new_complete_far_aprime")
    ar=normalized_budget_jet(a,aa,E[0],"saved_Euler_a_budget")
    apr=normalized_budget_jet(a,ap,Ep[0],"saved_Euler_aprime_budget")
    qm=relative_power(a,tau,Fraction(-1,4),4,0,"actual_q_minus_quarter_relative")
    qp=relative_power(a,tau,Fraction(1,4),4,0,"actual_q_plus_quarter_relative")
    invt=relative_power(a,tau,Fraction(-3,2),4,0,"actual_far_phase_reciprocal_relative")
    four=[
      mul(a,qm,ar,m=4,p=0),
      mul(a,qp,ar,m=4,p=0),
      mul(a,qp,invt,ar,m=4,p=0),
      mul(a,qp,apr,m=4,p=0)]
    fr=coefficientwise_complete_max(a,four,4,0,"complete_four_far_summand_relative_majorant")
    far0=old["complete_profile_jets"]["one_far_phase"]["group_upper"][0]
    farnew=scale(a,fr,a.read_up(far0),label="new_complete_one_far_phase")
    farnew.c[0,0]=a.read_up(far0);farnew.source_records={(0,0):far0}
    # Save/read every new near and far derivative before the whole packet uses it.
    sink.jet("near_profile",nearnew)
    sink.jet("one_far_phase",farnew)
    whole=add(a,nearnew,scale(a,farnew,2),m=4,p=0,label="new_complete_near_plus_two_far")
    whole0=old["complete_profile_jets"]["complete_profile"]["group_upper"][0]
    whole.c[0,0]=a.read_up(whole0);whole.source_records={(0,0):whole0}
    sink.jet("complete_profile",whole)
    # These original zero-order envelopes are copied. Their printed uppers
    # need not satisfy oldwhole0 >= reread(oldnear0)+2*reread(oldfar0).
    # The q=0 full function bound and the q>=1 new derivative bounds are
    # separately complete inequalities for the SAME function.
    ml=inp.philo
    f1,f2,f3,f4=[inp.phase[j] for j in range(1,5)]
    inv1=sink.copy("original_inverse_phase_derivative_1",
                   rows["inverse_phase_derivative_1_upper"])
    inv2=sink.emit(["scalars","inverse_phase_derivative_2_upper"],f2/ml**3)
    inv3=sink.emit(["scalars","inverse_phase_derivative_3_upper"],
                    f3/ml**4+3*f2*f2/ml**5)
    inv4=sink.emit(["scalars","inverse_phase_derivative_4_upper"],
                    f4/ml**5+10*f2*f3/ml**6+15*f2*f2*f2/ml**7)
    K0=sink.copy("original_phase_pullback_L2",rows["complete_phase_pullback_L2_upper"])
    K2=sink.emit(["scalars","complete_phase_pullback_Hminus2_upper"],
        finite_power(a,f1,Fraction(1,2),"complete individual phase derivative")*
        (inv1+inp.sqrt_two*(inv2+inv1*inv1)+inv3+3*inv1*inv2+inv1**3))
    K53=sink.emit(["scalars","complete_phase_pullback_Hminus5_3_upper"],
        finite_power(a,K0,Fraction(1,6),"positive old K0")*
        finite_power(a,K2,Fraction(5,6),"positive complete new K2"))
    two16=a.read_up(inp.wrt["complete_new_graphs"]["complete_terminal_summation_constants"][
        "new_records"]["two_one_sixth_upper"])
    inverse={1:inv1,2:inv2,3:inv3,4:inv4}
    for window,Kd,pref in (("zero",K0,a.ex(1)),("five_thirds",K53,a.up(two16**5)),
                           ("two",K2,a.ex(2))):
        for q in range(5):
            zeroth=whole.c[0,0] if q==0 else a.ex(0)
            full=upper_sum(a,(
              ordinary_bell(a,4,j,inverse)*a.ex(comb(j,q))*
              ordinary_angle(a,whole,j-q)
              for j in range(1,5) if q<=j))
            sink.emit(["full_output_block_weights",window,"angle_"+str(q)],
                      pref*Kd*(zeroth+rational(a,17,64)*full))
    sink.copy("single_signed_point_profile_upper",rows["single_signed_point_profile_upper"])
    return sink.finish({
      "new_profile_uses_only_true_pure_angular_relative_T":True,
      "old_near_ODE_Jost_and_all_zero_order_positive_algorithm_bounds_read_only":True,
      "budget_denominators_do_not_assert_nonzero_Airy_or_Jost_functions":True,
      "every_near_and_far_positive_algorithm_summand_retained":True,
      "oldwhole0_not_compared_to_reread_near0_plus_two_far0":True,
      "two_true_far_phases_and_near_partition_retained":True,
      "near_partition_angular_derivatives_are_zero":True,
      "all_signed_input_modes_and_all_zero_low_high_outputs":True,
      "no_output_block_orthogonality":True,
      "only_original_normalized_reflection_restriction_is_isometric":True,
      "independent_second_reference_port_not_eliminated":True,
      "ordinary_amplitude_angles_0_through_4_required":True,
      "profile_weights_include_no_extra_terminal_or_mean_factor_two":True})

INTERNAL_DEPENDENCIES = {
 "strict_per_index_background":(),
 "strict_per_index_drift":("strict_per_index_background",),
 "strict_relative_phase_and_gap":("strict_per_index_background","strict_per_index_drift"),
 "strict_absolute_fold_edges":("strict_per_index_drift","strict_relative_phase_and_gap"),
 "strict_fold_factors_and_inverses":("strict_per_index_background","strict_relative_phase_and_gap"),
 "strict_leading_amplitudes":("strict_per_index_background","strict_per_index_drift",
                             "strict_relative_phase_and_gap"),
 "strict_lower_order_coefficients":("strict_per_index_background",),
 "strict_complete_first_forcing":(
    "strict_per_index_background","strict_per_index_drift","strict_relative_phase_and_gap",
    "strict_fold_factors_and_inverses","strict_leading_amplitudes",
    "strict_lower_order_coefficients"),
 "strict_complete_cut_and_transport_kernel":(
    "strict_relative_phase_and_gap","strict_fold_factors_and_inverses",
    "strict_leading_amplitudes","strict_complete_first_forcing"),
 "strict_complete_free_transport":(
    "strict_per_index_drift","strict_relative_phase_and_gap","strict_leading_amplitudes",
    "strict_complete_cut_and_transport_kernel"),
 "strict_complete_potential_compositions":("strict_absolute_fold_edges",),
 "strict_complete_genuine_amplitudes":(
    "strict_absolute_fold_edges","strict_leading_amplitudes",
    "strict_complete_free_transport","strict_complete_potential_compositions"),
}
INTERNAL_PRODUCERS = {
 "strict_per_index_background":complete_background,
 "strict_per_index_drift":complete_drift,
 "strict_relative_phase_and_gap":complete_relative_phase_and_gap,
 "strict_absolute_fold_edges":complete_absolute_fold_edges,
 "strict_fold_factors_and_inverses":complete_fold_factors_and_inverses,
 "strict_leading_amplitudes":complete_leading_amplitudes,
 "strict_lower_order_coefficients":complete_lower_order_coefficients,
 "strict_complete_first_forcing":complete_first_forcing,
 "strict_complete_cut_and_transport_kernel":complete_cut_and_transport_kernel,
 "strict_complete_free_transport":complete_free_transport,
 "strict_complete_potential_compositions":complete_potential_compositions,
 "strict_complete_genuine_amplitudes":complete_genuine_amplitudes,
}

FALLBACK_GROUPS=((0,0),(1,1),(2,2),(3,3),(4,4),(5,6),(7,9),(10,12),(13,15))

def ordinary_same_function_fallback(api,new_ordinary,old_table,label):
    """Min of two complete bounds for each SAME derivative of the SAME function.

    Old groups are already normalized ordinary derivatives. No t_hi/t_lo
    scaling is applied to them. This is not an entrywise choice between
    different operators, different trials, or different coordinate maps.
    """
    require(getattr(new_ordinary,"ordinary_basis",False),"ordinary exit only")
    m,p=old_table["shape"]
    groups=[g for g in FALLBACK_GROUPS if g[0]<=m]
    require(len(old_table["group_upper"])==len(groups),"entire original group list")
    require(bool(old_table["value_omitted_for_lift"])==new_ordinary.omitted_value,
            label+" actual lift value convention")
    vals=dict(new_ordinary.c)
    for (r,q),value in vals.items():
        if r+q>m or r>p or (r,q) in new_ordinary.zero:
            continue
        gi=next(i for i,(left,right) in enumerate(groups) if left<=r+q<=right)
        record=old_table["group_upper"][gi]
        require(record is not None,"no original omitted lift value is read")
        vals[r,q]=min(api.up(value),api.read_up(record))
    result=Jet(api,new_ordinary.m,new_ordinary.p,vals,label,new_ordinary.zero,
               new_ordinary.omitted_value)
    result.ordinary_basis=True
    return result

class _WorkingSession:
    """One-child finite work. It is never serialized as a certificate."""
    def __init__(self,api,documents,admission,angular_packet,progress_state):
        self.api=api
        self.documents=documents
        self.inputs=Inputs(api,documents,admission,angular_packet)
        self.stages={}
        self.public_completed=set()
        self.progress=progress_state

    def ensure_stage(self,name):
        require(name in INTERNAL_STAGE_ORDER,"finite internal stage name")
        if name in self.stages:
            return self.stages[name]
        dependencies=[self.ensure_stage(n) for n in INTERNAL_DEPENDENCIES[name]]
        result=INTERNAL_PRODUCERS[name](
            self.inputs,_WorkingSink(name,self.progress),*dependencies)
        require(isinstance(result,_PrivateStage) and result.name==name,
                "complete finite private stage")
        self.stages[name]=result
        return result

def prepare_strict_profile_work(original_documents,admission,api,progress_state,
                                angular_packet=None):
    """Finite prework for the new complete profile; no public target is replayed.

    This constructor has no retry or resume policy. An owner encountering any
    failed/partial target must preserve its complete printed prefix and stop.
    """
    progress_state.clear()
    progress_state.update({
      "node_name":"strict_complete_angular_profile","complete":False,
      "current_stage":"finite_private_profile_prework",
      "printed_record_paths":[],
      "complete_scientific_document_prefix":{
        "kind":NODE_KIND,"node_name":"strict_complete_angular_profile","complete":False,
        "basis":BASIS,"new_records":{},"copied_original_records":{},
        "retained_scope":complete_scope()}})
    session=_WorkingSession(api,original_documents,admission,angular_packet,progress_state)
    session.ensure_stage("strict_relative_phase_and_gap")
    return session

def publish_complete_strict_profile(session,publish_graph,progress_state):
    require(isinstance(session,_WorkingSession),"same one-child finite session")
    name="strict_complete_angular_profile"
    require(name not in session.public_completed,"no complete target replay")
    sink=NodeSink(session.api,name,progress_state,publish_graph)
    sink.doc["angular_predecessor_identity"]=copy.deepcopy(
        session.inputs.angular_source_identity)
    sink.doc["relative_angular_predecessor_identity"]=copy.deepcopy(
        session.inputs.relative_angular_source_identity)
    saved=complete_angular_profile(session.inputs,sink,
                                  session.stages["strict_relative_phase_and_gap"])
    session.public_completed.add(name)
    return saved

def read_complete_strict_bundle(session,saved_profile,api,jet_factory):
    """Finish private coefficients for a NEW exact-Q residual, then expose work.

    No private mixed coefficient table is published or claimed as a standalone
    bound/certificate. The downstream public residual must keep all ten ordered
    words, all retained powers, all terminal terms and every printed prefix.
    The complete public profile is read back before its weights are consumed.
    """
    require(isinstance(session,_WorkingSession) and session.api is api,
            "same one-child finite working session")
    require(callable(jet_factory),"neutral ordinary coefficient constructor")
    inp=session.inputs
    original_documents=session.documents
    require(saved_profile["kind"]==NODE_KIND and saved_profile["complete"] is True
            and saved_profile["node_name"]=="strict_complete_angular_profile"
            and saved_profile["retained_scope"]==complete_scope(),
            "one complete canonical-read-back public profile")
    for name in INTERNAL_STAGE_ORDER:
        session.ensure_stage(name)
    def raw(node,key):
        return decode_jet(api,session.stages[node],key)
    certificate=inp.main["complete_derivative_request_certificate"]
    require(certificate["fixed_degree_groups"]==[list(g) for g in FALLBACK_GROUPS]
            and certificate["normalized_coefficients"]==
                "ordinary derivative norm divided by a! b!",
            "the original ordinary normalized group decoder")
    extended=original_documents["extended_amplitude_strict"]
    require(extended["complete"] is True and extended["node_name"]=="extended_amplitude_strict"
            and extended["conclusion"]["root_and_positive_reference_unchanged"] is True
            and extended["conclusion"]["original_free_amplitudes_recomputed"]==0
            and extended["conclusion"]["cB_squared_first_Airy_cross_retained"] is True,
            "complete same genuine amplitude predecessor")
    ext_old=extended["conclusion"]["complete_jets"]
    geo_old=inp.main["complete_strict_geometry_conclusion"]["complete_jets"]
    lead_old=inp.main["complete_strict_leading_conclusion"]["complete_jets"]
    coef_old=inp.main["complete_strict_coefficient_conclusion"]["new_jets"]
    lower_old=inp.main["complete_strict_forcing_conclusion"]["complete_coefficient_jets"]
    fallback_routes=[]
    def convert(j,old_table=None,route=None,norm=None):
        o=ordinary_adapter(api,j,inp.tlo)
        if old_table is not None:
            require(route is not None and norm is not None,"complete typed same-function map")
            o=ordinary_same_function_fallback(api,o,old_table,j.label+"_safe_ordinary")
            fallback_routes.append({"actual_function":route[-1],"original_path":route,
              "norm":norm,"basis":"ordinary derivative divided by r! q!",
              "old_shape":list(old_table["shape"]),"new_shape":[j.m,j.p],
              "fallback_only_on_original_shape_intersection":True,
              "old_group_never_rescaled_by_t_bounds":True})
        return jet_factory(o.m,o.p,dict(o.c),o.label,o.omitted_value)
    def background_direct(j,kind):
        o=ordinary_adapter(api,j,inp.tlo)
        if kind=="Q":
            for r,q in indices(o.m,o.p):
                if r<=2 and q<=3:
                    direct=api.read_up(inp.old["Q_"+str(r)+"_"+str(q)])/api.ex(factorial(r)*factorial(q))
                    o.c[r,q]=min(api.up(o.c[r,q]),api.up(direct))
        else:
            for r,q in indices(o.m,o.p):
                if q==0 and r<=3:
                    direct=api.read_up(inp.old[kind+"_"+str(r)])/api.ex(factorial(r))
                    o.c[r,0]=min(api.up(o.c[r,0]),api.up(direct))
        return jet_factory(o.m,o.p,dict(o.c),o.label,o.omitted_value)
    background=session.stages["strict_per_index_background"]
    drift=session.stages["strict_per_index_drift"]
    lower=session.stages["strict_lower_order_coefficients"]
    geo=session.stages["strict_fold_factors_and_inverses"]
    edge=session.stages["strict_absolute_fold_edges"]
    leading=session.stages["strict_leading_amplitudes"]
    ext=session.stages["strict_complete_genuine_amplitudes"]
    pot=session.stages["strict_complete_potential_compositions"]
    physical={
      "U":background_direct(decode_jet(api,background,"background_pair_A0"),"Q"),
      "V":background_direct(decode_jet(api,background,"background_pair_A0"),"Q"),
      "beta":background_direct(decode_jet(api,background,"beta"),"beta"),
      "K":background_direct(decode_jet(api,background,"K"),"K"),
      "eta":convert(decode_jet(api,background,"eta"),coef_old["eta"],["wgs_main","complete_strict_coefficient_conclusion","new_jets","eta"],"pure radial scalar"),
      "d":convert(decode_jet(api,drift,"d_A0"),coef_old["d"],["wgs_main","complete_strict_coefficient_conclusion","new_jets","d"],"independently proved full Fourier A0 coefficient"),
      "ell":convert(decode_jet(api,lower,"ell"),lower_old["ell"],["wgs_main","complete_strict_forcing_conclusion","complete_coefficient_jets","ell"],"full background A0 Banach product"),
      "L11":convert(decode_jet(api,lower,"e"),lower_old["e"],["wgs_main","complete_strict_forcing_conclusion","complete_coefficient_jets","e"],"full background A0 Banach product"),
      "L22":convert(decode_jet(api,lower,"b_local"),lower_old["b_local"],["wgs_main","complete_strict_forcing_conclusion","complete_coefficient_jets","b_local"],"full background A0 Banach product"),
    }
    T=decode_jet(api,edge,"T_absolute")
    common=raw("strict_relative_phase_and_gap","common_x_u_bound")
    geometry={
      "H_inverse_entry_sum":convert(decode_jet(api,geo,"H_inverse_entry_sum"),geo_old["H_inverse_entry_sum"],["wgs_main","complete_strict_geometry_conclusion","complete_jets","H_inverse_entry_sum"],"complete matrix-entry sup sum"),
      "T_absolute_jet":convert(T,geo_old["t"],["wgs_main","complete_strict_geometry_conclusion","complete_jets","t"],"scalar sup"),
      "X_phi_jet":convert(common,geo_old["x"],["wgs_main","complete_strict_geometry_conclusion","complete_jets","x"],"scalar sup for X_phi only"),
      "T_phi_absolute_jet":convert(T.shift(0,1,14,3,"same_T_phi"),geo_old["y"],["wgs_main","complete_strict_geometry_conclusion","complete_jets","y"],"scalar sup for T_phi"),
      "X_derivative_jet":convert(decode_jet(api,edge,"X_derivatives"),geo_old["X_derivatives"],["wgs_main","complete_strict_geometry_conclusion","complete_jets","X_derivatives"],"scalar sup of nonconstant actual lift derivatives"),
      "T_derivative_absolute_jet":convert(T,geo_old["t"],["wgs_main","complete_strict_geometry_conclusion","complete_jets","t"],"scalar sup"),
    }
    old_J=original_documents["same_angular_J_strict"]["conclusion"]
    require(old_J["space"]=="the original angular even-mean-zero to odd realization"
            and old_J["stable_trace_inverse_used"] is False
            and old_J["physical_means_discarded"] is False,
            "same original angular inverse realization")
    jr=old_J["new_complete_records"]
    patch={
      "physical_coefficients":physical,"geometry":geometry,
      "potential":{"V_of_T_jet":convert(decode_jet(api,pot,"V_of_T"),ext_old["Vext"],["extended_amplitude_strict","conclusion","complete_jets","Vext"],"scalar sup")},
      "amplitudes":{
        "w0_pair":[convert(decode_jet(api,leading,"a0"),lead_old["a0"],["wgs_main","complete_strict_leading_conclusion","complete_jets","a0"],"scalar component sup"),
                   convert(decode_jet(api,leading,"b0"),lead_old["b0"],["wgs_main","complete_strict_leading_conclusion","complete_jets","b0"],"scalar component sup")],
        "w1ext_pair":[convert(decode_jet(api,ext,"a1_ext"),ext_old["a1_ext"],["extended_amplitude_strict","conclusion","complete_jets","a1_ext"],"scalar component sup"),
                      convert(decode_jet(api,ext,"b1_ext"),ext_old["b1_ext"],["extended_amplitude_strict","conclusion","complete_jets","b1_ext"],"scalar component sup")]},
      "same_J":{
        "J0_upper":copy.deepcopy(jr["same_J_L2_upper"]),
        "L0_upper":copy.deepcopy(jr["same_L_L2_upper"]),
        "eta_lower":copy.deepcopy(jr["same_eta_positive_lower"])},
      "qualifications":{
        "complete_WUA_transport_cancellation":True,
        "same_original_reflected_column":True,
        "positive_Jet_subtraction_used_to_prove_cancellation":False,
        "complete_internal_individual_coefficient_and_full_forcing_tables_retained":True,
        "ordinary_normalization_recovered_with_actual_strict_lower_once":True,
      },
      "positive_Jet_subtraction_used_to_prove_cancellation":False,
    }
    pdoc=saved_profile
    weights={}
    for original,name in (("0","zero"),("-5/3","five_thirds"),("-2","two")):
        weights[original]=[copy.deepcopy(pdoc["new_records"]["full_output_block_weights"][
                          name]["angle_"+str(k)]) for k in range(5)]
    point=copy.deepcopy(original_documents["profile_block_strict"]["conclusion"][
            "new_complete_records"]["single_signed_point_profile_upper"])
    reflected=copy.deepcopy(original_documents["prior_WRT"][
            "copied_original_scalar_records"]["strict_reflected_point_profile"])
    return {
      "complete_patches":{"strict":patch},
      "ordinary_same_function_fallback_routes":fallback_routes,
      "complete_block_receiver_weights":{"strict":weights},
      "single_signed_pointwise_upper":{"strict":point},
      "complete_reflected_point_upper":{"strict":reflected},
      "whole_t_over_rho_lower":copy.deepcopy(inp.main["complete_strict_geometry_conclusion"][
            "complete_positive_lowers"]["whole_t_over_rho"]),
      "block_rows_include_complete_reflected_assembly":True,
      "complete_whole_error_claimed":False,
      "new_strict_coefficient_recipe":"WSJ individual frozen mixed tables and full cut/profile WSM",
      "local_mean_jump_four_endpoints_and_all_remaining_fees_read_from_prior_WRT":True,
    }
