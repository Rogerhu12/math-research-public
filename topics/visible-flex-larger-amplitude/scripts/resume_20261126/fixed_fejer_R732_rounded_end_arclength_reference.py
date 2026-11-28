#!/usr/bin/env python3
"""Bound R732 central/rounded full-domain physical seed.

The existing outer solver consumes the four unit-tangent derivative roles.
evaluate_six_jets also supplies the six working primitive jets. A complete
root packet binds the physical end recipe, working integrals, frozen chart
and all original input files to the selected model on the public runner.
"""
from __future__ import annotations

from fractions import Fraction as F
import hashlib
import inspect
import json
import math
import os
from pathlib import Path

import numpy as np

SCHEMA = "complete-fixed-fejer-R732-rounded-end-arclength-reference-v1"
ORIGINAL_REFERENCE_SCHEMA = "R690-fixed-fejer-axisymmetric-SO3-reference-input-v1"
ORIGINAL_REFERENCE_SHA = "e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb"
FULL_HOLD_SHA = "a1ed8fa5d2186f400ea50a1d609574ec6996e59317a57638a6820a59cf0e7670"
LENGTH_KERNEL_SCHEMA = "complete-R732-rounded-end-length-and-inverse-arclength-working-kernel-v1"
LENGTH_KERNEL_SHA = "032b6c68570c75a849daa2a5a335a9546cf31e1c3c0ad8a7ee4eb0dee3cb0420"


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS")!="true"
            or os.environ.get("GITHUB_REPOSITORY")!="Rogerhu12/math-research-public"):
        raise RuntimeError("R732 scientific reference evaluation requires public repository Actions")


def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda:stream.read(1<<20),b""):h.update(block)
    return h.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":"),
        allow_nan=False).encode()).hexdigest()


def array_sha(value):
    a=np.ascontiguousarray(value);h=hashlib.sha256(str(a.dtype).encode())
    h.update(json.dumps(list(a.shape)).encode());h.update(a.tobytes())
    return h.hexdigest()


def array_record(value):
    a=np.ascontiguousarray(value)
    return dict(shape=list(a.shape),dtype=str(a.dtype),sha256=array_sha(a))


def file_record(path):
    p=Path(path).resolve()
    return dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p))


def write_json(path,value):
    path=Path(path);temporary=path.with_name(path.name+".partial")
    temporary.write_text(json.dumps(value,indent=2,allow_nan=False)+"\n",encoding="utf-8")
    temporary.replace(path)


class SeedReferenceFailure(RuntimeError):
    def __init__(self,message,record):
        super().__init__(message);self.record=record


class RoundedEndUnitMeridianJet:
    """Complete original input; own immutable scalar-length state at every angle."""

    def __init__(self,problem,prepared,*,expected_bundle_sha256,
                 length_parameters,length_kernel_module,cache_directory=None):
        require_actions()
        c=problem.axisymmetric_reference_context
        if (c.model.get("schema")!=ORIGINAL_REFERENCE_SCHEMA
                or c.model.get("source_sha256")!=ORIGINAL_REFERENCE_SHA
                or canonical(c.model)!=c.identity
                or expected_bundle_sha256!=c.input_records["reference_bundle"]["sha256"]
                or sha(inspect.getfile(type(c)))!=ORIGINAL_REFERENCE_SHA
                or sha(inspect.getfile(type(c.law)))!=ORIGINAL_REFERENCE_SHA
                or sha(c.reference_at.__func__.__code__.co_filename)!=ORIGINAL_REFERENCE_SHA
                or not np.array_equal(prepared.core,c.core)
                or float(prepared.height).hex()!=float(c.height).hex()
                or c.scalar_identity!=c.model["fixed_scalar_metric_identity_sha256"]
                or canonical(c.scalar_definition)!=c.scalar_identity
                or sha(inspect.getfile(type(c.full)))!=FULL_HOLD_SHA):
            raise ValueError("Bind the whole original reference, scalar, chart, core and H")
        kernel=length_kernel_module
        if (kernel is None or sha(kernel.__file__)!=LENGTH_KERNEL_SHA
                or kernel.SCHEMA!=LENGTH_KERNEL_SCHEMA
                or sha(inspect.getfile(kernel.CompleteLengthRule))!=LENGTH_KERNEL_SHA
                or sha(kernel.geometry_jets.__code__.co_filename)!=LENGTH_KERNEL_SHA
                or sha(kernel.length_samples.__code__.co_filename)!=LENGTH_KERNEL_SHA
                or sha(kernel.physical_definition.__code__.co_filename)!=LENGTH_KERNEL_SHA
                or sha(inspect.getfile(kernel.RoundedTerminal))!=LENGTH_KERNEL_SHA
                or sha(kernel._deep_angle.__code__.co_filename)!=LENGTH_KERNEL_SHA
                or sha(c.law.d.__file__)!="e091f67566ef6a380758a3aac5d79d9b41e4bffcc9a9860e66eaaa9b314257c2"
                or type(length_parameters) is not kernel.LengthParameters):
            raise ValueError("Bind the complete new length/inverse-arclength source")
        eta,maximum,ints,tolerance,armijo=length_parameters.definitions()
        scalar_record=c.input_records["scalar_input"]
        raw=Path(scalar_record["path"]).read_bytes()
        if len(raw)!=scalar_record["bytes"] or hashlib.sha256(raw).hexdigest()!=scalar_record["sha256"]:
            raise ValueError("The entire original scalar-input bytes changed")
        scalar=json.loads(raw)
        projection=dict(analytic_extension_origin=scalar["analytic_extension_origin"],
                        geometry=scalar["fixed_scalar_profile"]["geometry"])
        if canonical(projection)!=c.model["original_scalar_parameters_identity_sha256"]:
            raise ValueError("Keep the complete original defining scalar projection")
        law=projection["geometry"]["initial_law"];word=law["k0"]
        if type(word) not in (int,float) or not math.isfinite(float(word)):
            raise ValueError("Retain the finite original core-curvature word")
        kappa=F(float(word))
        if (c.full.x[0]!=0 or c.full.coefficients[0][0]!=1
                or c.full.coefficients[0][1]!=0
                or 2*c.full.coefficients[0][2]/(c.full.x[1]-c.full.x[0])**2!=kappa):
            raise ValueError("The complete core jet must be a=1, a_s=0, a_ss=kappa0")
        self.context,self.kernel,self.parameters=c,kernel,length_parameters
        self.eta_exact,self.maximum_exact=eta,maximum
        self.eta,self.height,self.radius=float(eta),float(c.height),float(c.radius)
        self.kappa0_exact,self.kappa0=kappa,float(kappa)
        self.core=np.array(c.core,dtype=float,copy=True);self.core.setflags(write=False)
        self.freq=2*np.arange(1,c.M+1,dtype=float);self.qfreq=1-self.freq*self.freq
        self.freq.setflags(write=False);self.qfreq.setflags(write=False)
        if (not math.isfinite(self.eta) or self.eta<=0. or not 2*self.eta<self.height
                or not math.isfinite(self.kappa0) or c.M!=160 or c.J!=923):
            raise ValueError("Retain all original modes/cells and a positive-height R732 baseline")
        nodes=np.asarray(c.mesh,dtype=float)/float(c.mesh[-1])
        nodes[0]=0.;nodes[-1]=1.
        self.terminal=kernel.RoundedTerminal(c,length_parameters)
        self.rule=kernel.CompleteLengthRule(nodes,self.terminal.Sc,length_parameters)
        self.cache_directory=None if cache_directory is None else Path(cache_directory)
        self._plan=None;self._angle_cache={};self._batches=[];self._radial_cache={}
        self.last_failure=None
        self.counts=dict(reference_evaluations=0,requested_points=0,
            requested_literal_angles=0,new_literal_angles=0,angle_cache_hits=0,
            completed_root_batches=0,radial_query_batches=0)
        self.working_definition=dict(
            schema="complete-R732-rounded-end-reference-working-definition-v1",
            length_kernel_source_sha256=LENGTH_KERNEL_SHA,
            complete_length_definition=kernel.physical_definition(length_parameters),
            exact_S_definition=c.full.metadata()["S"],
            physical_S_carrier_hex=float(c.mesh[-1]).hex(),
            rounded_end=self.terminal.definition(),
            original_material_affine_nodes=[[str(a),str(b)] for a,b in c.nodes],
            full_original_material_cells=len(c.nodes)-1,
            working_quadrature_partition=(
                "every original increasing material mesh carrier divided by the same S "
                "carrier; this complete partition is a working rule, not a new target"),
            root_identity_includes_literal_angle_and_full_frozen_model=True,
            inverse_queries_use_original_affine_material_addresses=True,
            original_bubbles_raw_defect_lift_outer_full_cell_Gauss_and_normal32_are_separate=True,
            working_inverse_normalizes_actual_total_length_to_central_S_minus_L=True,
            working_primitive_equals_integral_of_returned_unit_T0_claimed=False,
            working_errors_enclosed=False)
        self.model=dict(schema=SCHEMA,source_sha256=sha(__file__),
            original_reference_source_sha256=ORIGINAL_REFERENCE_SHA,
            length_kernel_source_sha256=LENGTH_KERNEL_SHA,
            complete_axisymmetric_reference_model=c.model,
            initial_reference_model_identity_sha256=c.identity,
            initial_reference_bundle_sha256=c.input_records["reference_bundle"]["sha256"],
            fixed_scalar_metric_identity_sha256=c.scalar_identity,
            fixed_scalar_profile_definition=c.scalar_definition,
            fixed_chart_core_sha256=array_sha(self.core),
            initial_height_hex=self.height.hex(),radius_carrier_hex=self.radius.hex(),
            exact_core_radial_curvature=str(kappa),exact_physical_handle_length=str(eta),
            exact_maximum_contraction=str(maximum),
            complete_safe_cone_definition=kernel.physical_definition(length_parameters),
            core_cap_control_jets="R732 controls (8), actual kappa0*rho*n, Q vertical, exact R690 cap tail",
            reference_height_is_declared_working_word_not_exact_scalar_integral=True,
            accurate_S_R_chart_from_complete_original_definition=True,
            scalar_and_S_carriers_not_promoted_to_exact_values=True,
            seed_is_frozen_from_original_initial_point=True,
            current_outer_core_H_and_all_rotation_variables_are_not_seed_inputs=True,
            original_scalar_reference_outside_old_supports_retained=False,
            old_mean_v_d_w_lambda_arrays_or_roots_inherited=False,
            accurate_reference="central G(xi(phi),t(s,phi),phi) with length S-L; terminal P(S-s,phi) by R732 (3)-(6)",
            accurate_T0="central arclength unit tangent; terminal (-cos(alpha)*e,sin(alpha))",
            working_definition=self.working_definition)
        self.model_identity=canonical(self.model)
        self.binding=dict(schema=SCHEMA,source_sha256=sha(__file__),
            reference_bundle=c.input_records["reference_bundle"],
            reference_model_identity_sha256=c.identity,
            safe_cone_seed_model_identity_sha256=self.model_identity,
            fixed_scalar_metric_identity_sha256=c.scalar_identity,
            complete_original_reference_input_records=json.loads(json.dumps(c.input_records)),
            original_reference_source_sha256=ORIGINAL_REFERENCE_SHA,
            full_hold_source_sha256=FULL_HOLD_SHA,length_kernel_source_sha256=LENGTH_KERNEL_SHA,
            original_optimized_q_field_used=False,
            seed_core_and_H_frozen_but_all_outer_free_variables_unchanged=True)
        self.bound_files={role:dict(value) for role,value in c.input_records.items()}
        self.bound_sources=dict(seed=file_record(__file__),length_kernel=file_record(kernel.__file__),
            reference=file_record(inspect.getfile(type(c))),full_hold=file_record(inspect.getfile(type(c.full))),
            deep_scalar=file_record(c.law.d.__file__))

    def _cache_path(self):
        if self.cache_directory is None:return None
        if not self.cache_directory.is_dir():
            raise ValueError("The caller must first create its complete original cache directory")
        path=self.cache_directory/"R732-rounded-end-reference";path.mkdir(exist_ok=True)
        return path

    def _fail(self,phase,reason,**details):
        record=dict(schema=SCHEMA,complete=False,failure_phase=phase,reason=str(reason),
            source_sha256=sha(__file__),seed_model_identity_sha256=getattr(self,"model_identity",None),
            reference_model_identity_sha256=self.context.identity,
            fixed_scalar_metric_identity_sha256=self.context.scalar_identity,
            counts=dict(self.counts),continuous_certificate=False,**details)
        self.last_failure=record;directory=self._cache_path()
        if directory is not None:
            path=directory/"last-complete-reference-failure.json";write_json(path,record)
            self.last_failure=dict(record,runner_raw_failure_file=file_record(path))
        raise SeedReferenceFailure(str(reason),self.last_failure)

    def _recheck_inputs(self):
        for role,record in self.bound_files.items():
            actual=file_record(record["path"])
            if actual!=record:
                self._fail("whole_input_recheck","Changed complete actual reference input",
                    role=role,original_record=record,current_record=actual)
        for role,record in self.bound_sources.items():
            actual=file_record(record["path"])
            if actual!=record:
                self._fail("whole_source_recheck","Changed complete actual source",
                    role=role,original_record=record,current_record=actual)

    def _prepare_plan(self):
        if self._plan is not None:return self._plan
        record=dict(schema=SCHEMA+"-complete-length-plan",source_sha256=sha(__file__),
            length_kernel_source_sha256=LENGTH_KERNEL_SHA,
            seed_model_identity_sha256=self.model_identity,
            full_original_material_nodes=[[str(a),str(b)] for a,b in self.context.nodes],
            full_original_material_cell_count=self.context.J-1,
            complete_normalized_rule=self.rule.metadata(),baseline_degree=5,pulse_degree=84,
            complete_physical_domain=True,rounded_end=self.terminal.definition(),
            internal_formula_cuts=self.model["complete_safe_cone_definition"]["internal_formula_cuts"],
            inverse_arclength_is_not_polynomial_in_material_s=True,
            root_or_integral_error_enclosed=False)
        directory=self._cache_path()
        if directory is not None:
            path=directory/"complete-length-rule.npz";temporary=path.with_name(path.name+".partial")
            with temporary.open("wb") as stream:
                np.savez_compressed(stream,normalized_nodes=self.rule.nodes,
                    gauss_u=self.rule.u,gauss_w=self.rule.w,full_points=self.rule.points,
                    full_weights=self.rule.weights,physical_S=np.array(self.terminal.S),
                    central_length=np.array(self.rule.S),terminal_partition=self.terminal.nodes,
                    terminal_primitive_prefix=self.terminal.prefix,blend_partition=self.terminal.blend_nodes,
                    blend_beta_prefix=self.terminal.blend_prefix,
                    model_identity=np.array(self.model_identity))
            temporary.replace(path);record["runner_raw_rule"]=file_record(path)
            description=directory/"complete-length-plan.json";write_json(description,record)
            record["runner_raw_description"]=file_record(description)
        self._plan=record
        return record

    def _controls(self,chart,index):
        out=np.zeros((3,6,3),dtype=float)
        for q in range(3):
            Gamma=chart[("Gamma","Gamma1","Gamma2")[q]][index]
            e=chart[("e0","e1","e2")[q]][index]
            out[q,0]=Gamma;out[q,1]=Gamma
            core=chart[("rho_n","rho_n1","rho_n2")[q]][index]
            out[q,2]=Gamma+(5./4.)*self.kappa0*self.eta*self.eta*core
            out[q,3:]=self.terminal.Rv*e
        z=self.terminal.Z
        heights=np.array((0.,self.eta,2*self.eta,z-2*self.eta,z-self.eta,z))
        out[0,:,2]=heights
        if (not np.isfinite(out).all() or np.any(out[1:,:,2]!=0.)
                or not np.array_equal(out[0,:,2],heights)):
            self._fail("complete_control_jets","The complete R732 baseline or common heights changed")
        return out

    def _chart(self, phi):
        phase = phi[:, None]*self.freq[None]
        cp, sp = np.cos(phase), np.sin(phase)
        theta = phi+sp@((self.qfreq/self.freq)*self.core)
        rho = 1.+cp@(self.qfreq*self.core)
        rhop = -sp@(self.freq*self.qfreq*self.core)
        if (not np.isfinite(theta).all() or not np.isfinite(rho).all()
                or not np.isfinite(rhop).all() or np.any(rho <= 0)):
            self._fail("fixed_chart", "The bound original chart is not positive at every requested angle",
                angle_hex=[float(v).hex() for v in phi])
        zeros = np.zeros_like(phi)
        er = np.column_stack((np.cos(theta), np.sin(theta), zeros))
        et = np.column_stack((-np.sin(theta), np.cos(theta), zeros))
        e1 = rho[:, None]*et
        e2 = rhop[:, None]*et-rho[:, None]**2*er
        normal = np.column_stack((np.cos(phi), np.sin(phi), zeros))
        tangent = np.column_stack((-np.sin(phi), np.cos(phi), zeros))
        support = 1.+cp@self.core
        support_phi = -sp@(self.freq*self.core)
        Gamma = support[:, None]*normal+support_phi[:, None]*tangent
        Gamma1 = rho[:, None]*tangent
        Gamma2 = rhop[:, None]*tangent-rho[:, None]*normal
        rhopp=-cp@(self.freq*self.freq*self.qfreq*self.core)
        rho_n=rho[:,None]*normal
        rho_n1=rhop[:,None]*normal+rho[:,None]*tangent
        rho_n2=(rhopp-rho)[:,None]*normal+2*rhop[:,None]*tangent
        return dict(theta=theta, rho=rho, rhop=rhop, e0=er, e1=e1, e2=e2,
                    rho_n=rho_n,rho_n1=rho_n1,rho_n2=rho_n2,
                    Gamma=Gamma, Gamma1=Gamma1, Gamma2=Gamma2)


    def _roots(self,phi,chart):
        self._prepare_plan();self.counts["requested_literal_angles"]+=len(phi)
        states=[];created=[]
        for j,value in enumerate(phi):
            key=float(value).hex()
            if key in self._angle_cache:
                self.counts["angle_cache_hits"]+=1;states.append(self._angle_cache[key]);continue
            self.counts["new_literal_angles"]+=1;controls=self._controls(chart,j)
            try:state=self.rule.solve(controls,angle_hex=key)
            except self.kernel.LengthReferenceFailure as error:
                self._fail("complete_length_root",str(error),literal_angle_hex=key,
                    full_working_failure=error.record)
            packet=dict(schema=SCHEMA+"-literal-length-root",literal_angle_hex=key,
                source_sha256=sha(__file__),length_kernel_source_sha256=LENGTH_KERNEL_SHA,
                seed_model_identity_sha256=self.model_identity,
                reference_model_identity_sha256=self.context.identity,
                rounded_end=self.terminal.definition(),
                complete_control_jet_record=array_record(controls),
                complete_working_root=state["root"],
                continuous_root_and_angle_jets_certified=False)
            packet["identity_sha256"]=canonical(packet);state["packet"]=packet
            self._angle_cache[key]=state;created.append(key);states.append(state)
        if created:
            batch=dict(schema=SCHEMA+"-complete-root-batch",source_sha256=sha(__file__),
                seed_model_identity_sha256=self.model_identity,complete=True,
                created_literal_angle_hex=created,
                requested_literal_angle_hex=[float(v).hex() for v in phi],
                roots=[self._angle_cache[key]["packet"] for key in created],
                continuous_root_or_global_branch_certified=False,full_rule=self.rule.metadata())
            directory=self._cache_path()
            if directory is not None:
                serial=self.counts["completed_root_batches"]
                path=directory/("root-batch-%06d.npz"%serial)
                temporary=path.with_name(path.name+".partial")
                with temporary.open("wb") as stream:
                    np.savez_compressed(stream,
                        angles=np.array([float.fromhex(key) for key in created]),
                        scalar_root_and_jets=np.array([[self._angle_cache[key]["root"][n]
                            for n in ("xi","xi_phi","xi_phiphi")] for key in created]),
                        complete_prefixes=np.stack([self._angle_cache[key]["prefix"] for key in created]),
                        complete_control_jets=np.stack([self._angle_cache[key]["controls"] for key in created]),
                        model_identity=np.array(self.model_identity))
                temporary.replace(path);batch["runner_raw_arrays"]=file_record(path)
                description=directory/("root-batch-%06d.json"%serial);write_json(description,batch)
                batch["runner_raw_description"]=file_record(description)
            self.counts["completed_root_batches"]+=1;self._batches.append(batch)
        return states

    def _physical_rows(self,cells,local):
        key=(array_sha(cells),array_sha(local),self.model_identity)
        if key in self._radial_cache:return self._radial_cache[key]
        self.counts["radial_query_batches"]+=1
        values=[];backward=[];terminal_rows=[];definitions=[];S=self.terminal.S
        for cell,u in zip(cells,local):
            left,right=self.context.nodes[int(cell)],self.context.nodes[int(cell)+1]
            fraction=F(float(u))
            point=tuple((1-fraction)*a+fraction*b for a,b in zip(left,right))
            box=self.context.full.affine_time(point[0],point[1])
            s_exact=point[0]*self.terminal.S_exact_mid+point[1]
            u_exact=(1-point[0])*self.terminal.S_exact_mid-point[1]
            value=float(s_exact)
            backward.append(float(u_exact))
            terminal_rows.append(u_exact<=F(self.terminal.L))
            if not F(box[0],self.context.full.h.S)<=s_exact<=F(box[1],self.context.full.h.S):
                self._fail("physical_material_rows","The material carrier left the original affine box",
                    cell=int(cell),local_hex=float(u).hex())
            if not math.isfinite(value) or not 0.<=value<=S:
                self._fail("physical_material_rows","A full affine query left the original domain",
                    cell=int(cell),local_hex=float(u).hex(),exact_affine_point=[str(v) for v in point],
                    original_physical_S_hex=S.hex())
            definitions.append([str(v) for v in point]);values.append(value)
        result=np.array(values,dtype=float);result.setflags(write=False)
        u=np.asarray(backward,dtype=float);u.setflags(write=False)
        mask=np.asarray(terminal_rows,dtype=bool);mask.setflags(write=False)
        out=dict(values=result,backward=u,terminal_mask=mask,exact_affine_points=definitions,
            source_record=array_record(result),physical_S_carrier_hex=S.hex())
        self._radial_cache[key]=out
        return out

    def evaluate(self,cells,local,phi):
        return self._evaluate(cells,local,phi,False)

    def evaluate_six_jets(self,cells,local,phi):
        return self._evaluate(cells,local,phi,True)

    def _evaluate(self,cells,local,phi,positions):
        require_actions()
        raw_cells,local,phi=np.asarray(cells),np.asarray(local),np.asarray(phi)
        if (raw_cells.ndim!=1 or local.shape!=raw_cells.shape or phi.ndim!=1
                or not len(local) or not len(phi) or np.iscomplexobj(local) or np.iscomplexobj(phi)
                or not np.isfinite(raw_cells).all() or not np.isfinite(local).all()
                or not np.isfinite(phi).all()):
            raise ValueError("Keep all complete finite original rows and fixed-chart angles")
        cells=raw_cells.astype(np.int64)
        if (not np.array_equal(cells,raw_cells) or np.any(cells<0)
                or np.any(cells>=self.context.J-1) or np.any(local<0) or np.any(local>1)):
            raise ValueError("Use exact integer original cells and literal local coordinates in [0,1]")
        local,phi=np.asarray(local,dtype=float),np.asarray(phi,dtype=float)
        self.counts["reference_evaluations"]+=1
        self.counts["requested_points"]+=len(cells)*len(phi)
        chart=self._chart(phi)
        radial=self._physical_rows(cells,local)
        end=radial["terminal_mask"]
        central=~end
        states=self._roots(phi,chart) if np.any(central) else [None]*len(phi)
        tangent_names=("T0","T0_s","T0_phi","T0_phiphi")
        names=tangent_names+(("F","F_s","F_phi","F_ss","F_sphi","F_phiphi") if positions else ())
        complete={name:[] for name in names}
        roll=self.terminal.rows(radial["backward"][end],positions)
        for j,(angle,state) in enumerate(zip(phi,states)):
            values={name:np.empty((len(cells),3)) for name in names}
            try:
                if np.any(central):
                    middle=self.rule.evaluate_tangents(state,radial["values"][central],positions)
                    for name in names:values[name][central]=middle[name]
                if len(roll):
                    terminal=self.terminal.jet(roll,chart,j,positions)
                    for name in names:values[name][end]=terminal[name]
            except self.kernel.LengthReferenceFailure as error:
                self._fail("complete_inverse_arclength",str(error),
                    literal_angle_hex=float(angle).hex(),
                    whole_radial_query=dict(cells=array_record(cells),local=array_record(local),
                        exact_affine_points=radial["exact_affine_points"]),
                    full_working_failure=error.record)
            for name in complete:complete[name].append(values[name])
        result={name:np.stack(rows,axis=1) for name,rows in complete.items()}
        result.update(norm=np.linalg.norm(result["T0"],axis=-1),
            theta_parent=chart["theta"],rho_parent=chart["rho"],rho_phi_parent=chart["rhop"],
            metadata=dict(schema=SCHEMA,source_sha256=sha(__file__),
                length_kernel_source_sha256=LENGTH_KERNEL_SHA,
                seed_model_identity_sha256=self.model_identity,
                reference_model_identity_sha256=self.context.identity,
                complete_fixed_safe_cone_reference=True,all_original_outer_free_variables_preserved=True,
                accurate_unit_speed_uses_the_full_new_length_and_inverse_equations=True,
                accurate_length_root_inverse_angular_jets_and_continuous_geometry_certified=False,
                old_mean_arrays_normal_branches_raw_lift_calibration_inherited=False,
                scalar_trigonometric_quadrature_root_inverse_and_rounding_errors_enclosed=False))
        for value in result.values():
            if isinstance(value,np.ndarray):
                if not np.isfinite(value).all():
                    self._fail("complete_reference_jets","A required full tangent jet is nonfinite")
                value.setflags(write=False)
        return result

    def metadata(self):
        self._recheck_inputs()
        return dict(schema=SCHEMA,source_sha256=sha(__file__),model=self.model,
            model_identity_sha256=self.model_identity,binding=self.binding,
            counts=dict(self.counts),working_definition=self.working_definition,
            full_bound_source_records=dict(self.bound_sources),
            complete_bound_reference_input_records=dict(self.bound_files),
            length_plan=self._plan,completed_literal_angle_count=len(self._angle_cache),
            length_root_batch_records=self._batches,full_rule=self.rule.metadata(),
            rounded_end=self.terminal.metadata(),
            last_failure=self.last_failure,all_bound_input_and_source_bytes_rechecked=True,
            accurate_length_root_error_or_global_branch_certified=False,
            complete_reference_safe_cone_and_diameter_certified=False,
            seed_physical_field_or_normal_control_rank_inherited=False,
            continuous_metric_geometry_or_full_phase_certificate=False)
