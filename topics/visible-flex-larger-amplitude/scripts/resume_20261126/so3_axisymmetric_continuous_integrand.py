#!/usr/bin/env python3
"""Continuous whole-cell B/L inputs for the actual direct-R690 SO3 integrand.

This binds the genuine full checkpoint and independent reference. It
encloses T=Exp(omega cross)T0 and two angular derivatives on every exact
affine radial cell and all angles. It is a component, not a quadrature,
rounding, inverse-chart, Gram, reach or closed-isometry certificate.
Scientific execution belongs only in the public repository Actions.
"""
import argparse
import ast
from fractions import Fraction as F
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import subprocess
import sys
import time
from types import SimpleNamespace
import numpy as np

SCHEMA = 'continuous-direct-R690-SO3-integrand-input-bounds-v1'
TOPIC = 'topics/visible-flex-larger-amplitude'
PINS = {
    'reference': ('scripts/resume_20261126/so3_axisymmetric_reference.py','4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3'),
    'operator': ('scripts/resume_20261126/so3_axisymmetric_meridian_operator.py','7f26ff35d115d6bfd748a7382e7b3eb159221cd0b12823bee8fa867dee123aaf'),
    'driver': ('scripts/resume_20261126/fullclosed_axisymmetric_so3_qp.py','606e00485be3625378916cfa66f6da1803b82005ba14959610bb1a4be7cfb1f9'),
    'low_order': ('scripts/resume_20261126/so3_meridian_low_order_error_bounds.py','30ae7dc70ea836ab6f30e34b9b886f968c6e61c6646c807cd96a8611029c2636'),
}
REPORT_SCHEMA = 'complete-independent-axisymmetric-fixed-deep-so3-meridian-QP-v1'
OPERATOR_SCHEMA = 'complete-independent-axisymmetric-so3-meridian-with-core-lift-v1'

def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Scientific continuous input bounds require this public repository Actions')

def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda:stream.read(1<<20),b''):
            h.update(block)
    return h.hexdigest()

def canonical(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),
        allow_nan=False).encode()).hexdigest()

def array_sha(value):
    value = np.ascontiguousarray(value)
    h = hashlib.sha256(str(value.dtype).encode())
    h.update(json.dumps(list(value.shape)).encode()); h.update(value.tobytes())
    return h.hexdigest()

def load(name,path,expected):
    if sha(path)!=expected:
        raise ValueError('Changed complete source '+str(path))
    spec = importlib.util.spec_from_file_location(name,path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module

def file_record(path):
    path = Path(path).resolve()
    return dict(path=str(path),sha256=sha(path),bytes=path.stat().st_size)

def write_json(path,value):
    path = Path(path)
    temporary = path.with_name(path.name+'.partial')
    temporary.write_text(json.dumps(value,indent=2,allow_nan=False)+'\n')
    temporary.replace(path)

def event(**values):
    print(json.dumps(values,separators=(',',':'),allow_nan=False),flush=True)

def literal_registry(path,name):
    nodes = [node.value for node in ast.parse(Path(path).read_text()).body
        if isinstance(node,ast.Assign) and any(isinstance(target,ast.Name)
            and target.id==name for target in node.targets)]
    if len(nodes)!=1:
        raise ValueError('One complete literal source registry is required: '+name)
    return ast.literal_eval(nodes[0])

def affine(nodes,cell,u):
    u = F(u)
    if not 0<=u<=1:
        raise ValueError('Exact local coordinate outside the full cell')
    return tuple((1-u)*a+u*b for a,b in zip(nodes[cell],nodes[cell+1]))

def affine_difference(left,right):
    return tuple(b-a for a,b in zip(left,right))

class ActualInput:
    """Actual bound state, never an invented warm or a renamed zero-Delta field."""
    def __init__(self,args):
        require_actions()
        self.repo = args.repo.resolve()
        topic = self.repo/TOPIC
        self.paths = {role:topic/relative for role,(relative,digest) in PINS.items()}
        for role,path in self.paths.items():
            if sha(path)!=PINS[role][1]:
                raise ValueError('Changed continuous component dependency: '+role)
        self.reference = load('_continuous_axis_reference',self.paths['reference'],PINS['reference'][1])
        self.kernel = load('_continuous_axis_low_order',self.paths['low_order'],PINS['low_order'][1])
        self.report = report = json.loads(args.report.read_text())
        if report.get('schema')!=REPORT_SCHEMA or report.get('source_sha256')!=PINS['driver'][1]:
            raise ValueError('Use the actual complete independent hDelta driver report, not another field schema')
        for role,(relative,expected) in literal_registry(self.paths['driver'],'SOURCE_PINS').items():
            if (report['source_sha256_by_role'].get(role)!=expected or sha(topic/relative)!=expected):
                raise ValueError('Actual complete driver source differs: '+role)
        if args.state=='final':
            if report.get('complete') is not True:
                raise ValueError('A final-state input requires its actual completed full report')
            expected = report.get('final_bundle_sha256')
        else:
            expected = report.get('initial_new_bundle',{}).get('sha256')
            if report.get('initial') is None:
                raise ValueError('An initial-state input requires the actual initial full field record')
        if expected!=sha(args.checkpoint):
            raise ValueError('The selected actual state does not bind this checkpoint')
        for key,path in (
                ('bundle_sha256',args.reference_bundle),
                ('observation_carrier_sha256',args.carrier),
                ('exact_tail_node_report_sha256',args.node_report),
                ('exact_tail_scalar_input_sha256',args.scalar_input)):
            if report.get(key)!=sha(path):
                raise ValueError('Changed genuine same-field input: '+key)
        if report['independent_preparation_report']['sha256']!=sha(args.preparation_report):
            raise ValueError('The actual preparation report differs')
        self.context = context = self.reference.AxisymmetricReferenceContext.from_files(
            repo=self.repo,reference_bundle=args.reference_bundle,carrier=args.carrier,
            node_report=args.node_report,scalar_input=args.scalar_input,
            preparation_report=args.preparation_report,panels=args.panels)
        with np.load(args.checkpoint,allow_pickle=False) as saved:
            self.data = data = {key:np.array(saved[key],copy=True) for key in saved.files}
        model = json.loads(str(data['so3_model_json'].item()))
        if (str(data['schema'].item())!=OPERATOR_SCHEMA or model.get('schema')!=OPERATOR_SCHEMA
                or model.get('source_sha256')!=PINS['operator'][1]
                or canonical(model)!=str(data['so3_model_identity_sha256'].item())
                or model!=report['representation'] or canonical(model)!=report['model_identity_sha256']
                or model.get('reference_meridian_kernel_sha256')!=PINS['reference'][1]
                or model.get('complete_axisymmetric_reference_model')!=context.model
                or model.get('initial_reference_model_identity_sha256')!=context.identity
                or model.get('initial_reference_bundle_sha256')!=sha(args.reference_bundle)
                or model.get('fixed_scalar_metric_identity_sha256')!=context.scalar_identity
                or model.get('fixed_scalar_profile_definition')!=context.scalar_definition
                or report['fixed_scalar_metric']['identity_sha256']!=context.scalar_identity
                or report['fixed_scalar_metric']['exact_profile_definition']!=context.scalar_definition):
            raise ValueError('The complete actual field/target/reference identity is inconsistent')
        self.J,self.M,self.n = context.J,context.M,3*context.M+2
        self.omega = np.array(data['omega_jets'],copy=True)
        if (self.omega.shape!=(self.J,3,self.n) or not np.isfinite(self.omega).all()
                or data['core'].shape!=(self.M,) or not np.isfinite(data['core']).all()
                or not math.isfinite(float(data['Hcap']))
                or not np.array_equal(data['mesh'],context.mesh)
                or not np.array_equal(data['fixed_chart_core'],context.core)
                or not np.array_equal(data['core'][:3],context.core[:3])):
            raise ValueError('Use all literal current omega/core/H on the actual fixed chart and mesh')
        if np.any(self.omega.reshape(3*self.J,self.n)[[0,3*(self.J-1),3*(self.J-1)+1]]!=0):
            raise ValueError('The actual structural core/cap zero jets changed')
        self.model,self.identity = model,canonical(model)
        self.profile = context.scalar_identity
        self.inputs = {role:file_record(getattr(args,role)) for role in
            ('checkpoint','report','reference_bundle','carrier','node_report','scalar_input','preparation_report')}
        self.binding = dict(schema=SCHEMA,selected_actual_state=args.state,
            actual_driver_source_sha256=PINS['driver'][1],operator_source_sha256=PINS['operator'][1],
            actual_driver_source_commit=report['source_commit'],field_model_identity_sha256=self.identity,
            complete_field_model=model,fixed_scalar_metric_identity_sha256=self.profile,
            fixed_scalar_profile_definition=context.scalar_definition,
            reference_model_identity_sha256=context.identity,input_files=self.inputs,
            complete_omega_jets_sha256=array_sha(self.omega),
            complete_current_core_sha256=array_sha(data['core']),current_H_hex=float(data['Hcap']).hex(),
            fixed_chart_core_sha256=array_sha(context.core),
            exact_symbolic_nodes=[[str(a),str(b)]for a,b in context.nodes],
            numerical_mesh_is_exact_domain=False,
            scope='T=Exp(omega cross)T0 in this same hDelta field; not the entire F and not a zero-Delta corrected integrand')

class ScalarWholeInterval:
    """b,c,b_s,c_s on an entire exact affine subcell, with all scalar pieces."""
    def __init__(self,actual):
        self.a,self.c = actual,actual.context
        self.p,self.d,self.law = self.c.full,self.c.modules['deep_scalar'],self.c.law
        self.S = self.p.S
        self.scale = self.p.h.S
        self.calls = 0

    def old_to_deep(self,value):
        return self.d.box(F(value[0],self.scale),F(value[1],self.scale))

    def exact_affine_box(self,definition):
        return self.old_to_deep(self.p.affine_time(*definition))

    def width_box(self,left,right):
        result = self.exact_affine_box(affine_difference(left,right))
        if result[0]<=0:
            raise ValueError('The same exact physical affine cell needs a positive width enclosure')
        return result

    def endpoint_ranges(self,left,right):
        d = self.d
        sb0,sb1 = self.exact_affine_box(left),self.exact_affine_box(right)
        tb0 = self.exact_affine_box((1-left[0],-left[1]))
        tb1 = self.exact_affine_box((1-right[0],-right[1]))
        return (F(sb0[0],d.SCALE),F(sb1[1],d.SCALE)),(
            max(F(0),F(tb1[0],d.SCALE)),max(F(0),F(tb0[1],d.SCALE)))

    def enclose(self,left,right):
        require_actions()
        self.calls += 1
        p,d,h = self.p,self.d,self.p.h
        (slo,shi),(tlo,thi) = self.endpoint_ranges(left,right)
        if slo<0:
            if left!=(F(0),F(0)):
                raise ValueError('The exact input domain begins at the original zero core')
            slo=F(0)
        anchor=F(p.out)/4
        pieces=[]
        def add_old(values,kind,lo,hi):
            pieces.append(dict(kind=kind,s_range=[str(lo),str(hi)],
                boxes=tuple(self.old_to_deep(value) for value in values)))
        if thi>=anchor:
            anchor_box=self.exact_affine_box((F(1),-anchor))
            old_high=min(shi,F(anchor_box[1],d.SCALE))
            if slo<=old_high:
                if slo<=p.origin:
                    lo,hi=slo,min(old_high,p.origin)
                    add_old(self.law._prefix_boxes(lo,hi),'complete_original_quintic_prefix',lo,hi)
                if old_high>=p.origin and slo<=p.cut:
                    lo,hi=max(slo,p.origin),min(old_high,p.cut)
                    add_old(self.law._analytic_boxes(lo,hi),'original_exact_analytic_extension',lo,hi)
                if old_high>=p.cut:
                    # Each segment's endpoint boxes only enlarge the actual
                    # intersection. The original helper uses the proved
                    # global |K| and |K_s| when a queried interval touches
                    # a segment boundary; it is valid for a whole interval.
                    for j in range(5):
                        lo=max(slo,p.cut,F(p.time[j][0],h.S))
                        hi=min(old_high,F(p.time[j+1][1],h.S))
                        if lo>hi:
                            continue
                        angle,curvature=d.DeepValleyTail._old_angle_curvature(
                            SimpleNamespace(old=p),p.o.box(lo,hi))
                        proved=h.interval(F(5,2))
                        curvature=max(curvature[0],-proved[1]),min(curvature[1],proved[1])
                        if curvature[0]>curvature[1]:
                            raise ArithmeticError('The complete old Hold curvature missed its proved bound')
                        b,c=h.sine_cosine(angle)
                        add_old((b,c,h.neg(h.multiply(curvature,c)),h.multiply(curvature,b)),
                            'complete_original_Hold_segment_'+str(j),lo,hi)
        if tlo<=anchor:
            lo,hi=max(F(0),tlo),min(thi,anchor)
            if lo<=hi:
                beta,K=self.law.tail.beta_and_curvature(lo/F(p.out),hi/F(p.out))
                sine,cosine=d.sine_cosine(beta)
                pieces.append(dict(kind='entire_R690_deep_tail',
                    t_range=[str(lo),str(hi)],boxes=(d.neg(cosine),sine,
                        d.neg(d.mul(K,sine)),d.neg(d.mul(K,cosine))),
                    complete_infinite_tail=True))
        if not pieces:
            raise ValueError('The entire exact subcell must belong to the complete declared scalar')
        boxes=tuple(d.hull([piece['boxes'][k]for piece in pieces])for k in range(4))
        return boxes,[{key:value for key,value in piece.items() if key!='boxes'}for piece in pieces]

class ExactOmegaBounds:
    """Literal node jets on the exact affine mesh, restricted Bernstein bounds."""
    def __init__(self,actual,scalar):
        self.a,self.scalar,self.d = actual,scalar,scalar.d
        self.omega = actual.omega
        self.M,self.n = actual.M,actual.n
        self.frequencies = [*range(1,2*self.M+2,2),*range(1,2*self.M+2,2),*range(2,2*self.M+1,2)]
        self.channels = [0]*(self.M+1)+[1]*(self.M+1)+[2]*self.M
        self.prepared_cells = {}
        self.actual_nonzero_radial_polynomials=0

    def sum_boxes(self,terms):
        result=self.d.ZERO
        for value in terms:
            result=self.d.add(result,value)
        return result

    def polynomial(self,values,width):
        d=self.d
        y0,u0,a0,y1,u1,a1=[d.box(F(float(v)))for v in values]
        w2=d.mul(width,width)
        c0,c1,c2=y0,d.mul(width,u0),d.scale(d.mul(w2,a0),F(1,2))
        e0=d.sub(d.sub(y1,c0),d.add(c1,c2))
        e1=d.sub(d.mul(width,u1),d.add(c1,d.scale(c2,2)))
        e2=d.sub(d.mul(w2,a1),d.scale(c2,2))
        c3=d.add(d.sub(d.scale(e0,10),d.scale(e1,4)),d.scale(e2,F(1,2)))
        c4=d.sub(d.add(d.scale(e0,-15),d.scale(e1,7)),e2)
        c5=d.add(d.sub(d.scale(e0,6),d.scale(e1,3)),d.scale(e2,F(1,2)))
        return [c0,c1,c2,c3,c4,c5]

    def prepare_cell(self,cell):
        if cell in self.prepared_cells:
            return self.prepared_cells[cell]
        width=self.scalar.width_box(self.a.context.nodes[cell],self.a.context.nodes[cell+1])
        inverse=self.d.inverse(width)
        rows=self.omega[cell:cell+2].reshape(6,self.n)
        polynomials=[]
        for mode in range(self.n):
            literal=rows[:,mode]
            if np.all(literal==0):
                polynomials.append(None)
                continue
            coefficients=self.polynomial(literal,width)
            derivative=[self.d.mul(self.d.scale(coefficients[k+1],k+1),inverse)for k in range(5)]
            polynomials.append((coefficients,derivative))
            self.actual_nonzero_radial_polynomials+=1
        self.prepared_cells[cell]=(width,polynomials)
        return width,polynomials

    def restricted_range(self,coefficients,low,high):
        d=self.d
        degree=len(coefficients)-1
        width=high-low
        power=[]
        for k in range(degree+1):
            power.append(self.sum_boxes(d.scale(coefficients[j],
                F(math.comb(j,k))*low**(j-k)*width**k)for j in range(k,degree+1)))
        bernstein=[]
        for k in range(degree+1):
            bernstein.append(self.sum_boxes(d.scale(power[j],
                F(math.comb(k,j),math.comb(degree,j)))for j in range(k+1)))
        return min(v[0]for v in bernstein),max(v[1]for v in bernstein)

    def enclose(self,cell,low,high):
        _,polynomials=self.prepare_cell(cell)
        channel_l1={(r,k):[F(0),F(0),F(0)]for r in (0,1)for k in (0,1,2)}
        for mode,polynomial in enumerate(polynomials):
            if polynomial is None:
                continue
            channel,frequency=self.channels[mode],self.frequencies[mode]
            for radial in (0,1):
                magnitude=self.d.magnitude(self.restricted_range(polynomial[radial],low,high))
                for angular in (0,1,2):
                    channel_l1[(radial,angular)][channel]+=magnitude*frequency**angular
        norms={key:self.a.kernel.sqrt_upper(sum(v*v for v in values))for key,values in channel_l1.items()}
        return dict(value=norms[(0,0)],s=norms[(1,0)],phi=norms[(0,1)],
            phiphi=norms[(0,2)],sphi=norms[(1,1)],sphiphi=norms[(1,2)],
            channel_l1={str(r)+','+str(k):values for (r,k),values in channel_l1.items()},
            all_original_rotation_channels_used=True,all_angles=True,
            exact_omega_node_jets_on_exact_physical_mesh=True,
            numerical_Hermite_evaluation_error_paid=False)

class ContinuousIntegrand:
    """Whole-cell B_j,L_j for j=0,1,2 on the same actual mathematical field."""
    def __init__(self,actual,*,subdivisions=1):
        require_actions()
        if subdivisions!=int(subdivisions)or subdivisions<1:
            raise ValueError('Use a positive exact number of equal local subintervals')
        self.a,self.subdivisions=actual,int(subdivisions)
        self.scalar=ScalarWholeInterval(actual)
        self.rotation=ExactOmegaBounds(actual,self.scalar)
        self.d,self.k=actual.context.modules['deep_scalar'],actual.kernel
        core=[F(float(value))for value in actual.context.core]
        frequencies=[2*(j+1)for j in range(actual.M)]
        self.rho_abs=1+sum(abs((1-frequency*frequency)*value)for frequency,value in zip(frequencies,core))
        self.rhop_abs=sum(abs(frequency*(1-frequency*frequency)*value)for frequency,value in zip(frequencies,core))
        self.rho_triangle_lower=1-sum(abs((1-frequency*frequency)*value)for frequency,value in zip(frequencies,core))
        self.angular_second=self.k.sqrt_upper(self.rhop_abs*self.rhop_abs+self.rho_abs**4)

    def cell(self,cell):
        require_actions()
        cell=int(cell)
        if not 0<=cell<self.a.J-1:
            raise ValueError('Use an actual complete affine original cell')
        records=[]
        for index in range(self.subdivisions):
            lo,hi=F(index,self.subdivisions),F(index+1,self.subdivisions)
            left,right=affine(self.a.context.nodes,cell,lo),affine(self.a.context.nodes,cell,hi)
            boxes,pieces=self.scalar.enclose(left,right)
            b,c,bs,cs=[self.d.magnitude(value)for value in boxes]
            b,c=min(F(1),b),min(F(1),c)
            U=dict(value=F(1),s=self.k.sqrt_upper(bs*bs+cs*cs),
                phi=b*self.rho_abs,phiphi=b*self.angular_second,
                sphi=bs*self.rho_abs,sphiphi=bs*self.angular_second)
            omega=self.rotation.enclose(cell,lo,hi)
            R=self.k.rotation_jet_bounds(omega_s=omega['s'],omega_phi=omega['phi'],
                omega_phiphi=omega['phiphi'],omega_sphi=omega['sphi'],omega_sphiphi=omega['sphiphi'])
            T=self.k.meridian_jet_bounds(U,R)
            records.append(dict(local_exact=[str(lo),str(hi)],
                exact_affine_endpoints=[[str(a),str(b)]for a,b in (left,right)],
                scalar_pieces=pieces,complete_scalar_jet_boxes={
                    name:self.d.enclosure(box)for name,box in zip(('b','c','bs','cs'),boxes)},
                exact_unit_reference=U,full_rotation=omega,rotation_matrix=R,meridian=T))
        names=('T_norm','Tphi_norm','Tphiphi_norm','T_radial_Lipschitz','Tphi_radial_Lipschitz','Tphiphi_radial_Lipschitz')
        whole={name:max(row['meridian'][name]for row in records)for name in names}
        width=self.scalar.width_box(self.a.context.nodes[cell],self.a.context.nodes[cell+1])
        return dict(cell=cell,whole_exact_cell=True,all_angles=True,subintervals=records,
            complete_physical_width=self.d.enclosure(width),
            numerical_width_carrier_hex=float(self.a.context.mesh[cell+1]-self.a.context.mesh[cell]).hex(),
            B=[whole['T_norm'],whole['Tphi_norm'],whole['Tphiphi_norm']],
            L=[whole['T_radial_Lipschitz'],whole['Tphi_radial_Lipschitz'],whole['Tphiphi_radial_Lipschitz']],
            meridian=whole,normalization_lower_nu_needed=False,
            angular_sample_grid_used=False,scalar_whole_interval_not_point_query=True,
            whole_field_F_or_Gram_certified=False)

    def metadata(self):
        return dict(subdivisions=self.subdivisions,
            rho_absolute_upper_exact=str(self.rho_abs),rhop_absolute_upper_exact=str(self.rhop_abs),
            rho_triangle_lower_exact=str(self.rho_triangle_lower),
            fixed_chart_rho_positive_by_triangle_bound=self.rho_triangle_lower>0,
            fixed_chart_used=True,current_core_never_substituted_for_fixed_chart=True,
            actual_whole_scalar_interval_calls=self.scalar.calls,
            actual_nonzero_radial_polynomials=self.rotation.actual_nonzero_radial_polynomials,
            complete_actual_omega_modes=self.a.n,
            exact_unit_reference_formula=True,numerical_normalization_fees_included=False,
            scope='Continuous integrand norms/Lipschitz only. No quadrature, root or floating evaluation fee is paid here.')

def main(args):
    require_actions()
    start=time.monotonic()
    args.repo=args.repo.resolve();args.outdir=args.outdir.resolve()
    if args.outdir==args.repo or args.repo in args.outdir.parents:
        raise ValueError('Raw continuous enclosures must stay outside the repository')
    actual=ActualInput(args)
    evaluator=ContinuousIntegrand(actual,subdivisions=args.subdivisions)
    identity=dict(schema=SCHEMA,source_sha256=sha(__file__),
        bound_input_identity_sha256=canonical(actual.binding),subdivisions=args.subdivisions,
        integer_scale=str(evaluator.d.SCALE),sqrt_dyadic_bits=96)
    identity_sha=canonical(identity)
    journal=args.outdir/'cells.jsonl'
    record_path=args.outdir/'report.json'
    completed=0
    maxima={key:F(0)for key in ('T_norm','Tphi_norm','Tphiphi_norm','T_radial_Lipschitz','Tphi_radial_Lipschitz','Tphiphi_radial_Lipschitz')}
    chain=identity_sha
    if args.outdir.exists():
        if not args.resume or not record_path.is_file() or not journal.is_file():
            raise ValueError('Existing output requires an explicitly bound journal resume')
        prior=json.loads(record_path.read_text())
        if prior.get('identity')!=identity:
            raise ValueError('Do not resume another source, field, target or interval subdivision')
        for line in journal.read_text().splitlines():
            row=json.loads(line)
            content=row['record']
            if content['cell']!=completed or row['previous_record_identity_sha256']!=chain:
                raise ValueError('The complete ordered natural journal is discontinuous')
            if canonical(dict(previous=chain,record=content))!=row['record_identity_sha256']:
                raise ValueError('A persisted cell bound changed')
            chain=row['record_identity_sha256']
            for key in maxima:
                maxima[key]=max(maxima[key],F(content['meridian'][key]))
            completed+=1
    else:
        if args.resume:
            raise ValueError('An explicit resume requires the existing actual journal')
        args.outdir.mkdir(parents=True)
        journal.write_text('')
    source_commit=subprocess.check_output(['git','-C',str(args.repo),'rev-parse','HEAD'],text=True).strip()
    initial_completed=completed
    def save_report():
        whole=completed==actual.J-1
        report=dict(schema=SCHEMA,source_sha256=sha(__file__),source_commit=source_commit,
            identity=identity,identity_sha256=identity_sha,binding=actual.binding,
            source_records={role:file_record(path)for role,path in actual.paths.items()},
            complete=whole,all_original_cells_completed=whole,completed_cells=completed,total_cells=actual.J-1,
            partial_bounds_not_promoted_to_full_domain=not whole,all_angles_enclosed=True,
            processed_cells_maxima=evaluator.k.serialize(maxima),
            whole_domain_maxima=evaluator.k.serialize(maxima)if whole else None,
            journal=file_record(journal),final_journal_chain_sha256=chain,
            evaluator=evaluator.metadata(),newly_completed_cells=completed-initial_completed,
            actual_seconds=time.monotonic()-start,admission_seconds=args.admission_seconds,
            each_returned_cell_is_full_angle_and_full_radial=True,unprocessed_cells_reported_explicitly=True,
            numerical_F_or_J_recomputed=False,continuous_integrand_enclosures_computed=True,
            exact_unit_meridian_definition_not_numerical_unit_claim=True,
            numerical_omega_Hermite_and_T0_carrier_errors_certified=False,
            quadrature_inverse_chart_Gram_and_geometry_certified=False,
            zero_closure_corrected_meridian_certified=False,closed_isometry_accepted=False,
            execution=dict(repository=os.environ['GITHUB_REPOSITORY'],
                run_id=os.environ.get('GITHUB_RUN_ID'),attempt=os.environ.get('GITHUB_RUN_ATTEMPT')))
        write_json(record_path,report)
        return report
    save_report()
    while completed<actual.J-1:
        if time.monotonic()-start>=args.admission_seconds and completed>initial_completed:
            break
        cell_started=time.monotonic()
        value=evaluator.cell(completed)
        content=evaluator.k.serialize(value)
        next_chain=canonical(dict(previous=chain,record=content))
        with journal.open('a')as stream:
            stream.write(json.dumps(dict(previous_record_identity_sha256=chain,
                record_identity_sha256=next_chain,record=content),separators=(',',':'),allow_nan=False)+'\n')
            stream.flush();os.fsync(stream.fileno())
        chain=next_chain
        for key in maxima:
            maxima[key]=max(maxima[key],value['meridian'][key])
        completed+=1
        report=save_report()
        event(event='continuous_axis_integrand_whole_cell',cell=completed-1,
            whole_cell=True,all_angles=True,cell_seconds=time.monotonic()-cell_started,
            completed_cells=completed,total_cells=actual.J-1,record_identity_sha256=chain)
        # Replaceable algebra cache, not any permanent scientific location.
        evaluator.rotation.prepared_cells.clear()
    report=save_report()
    event(event='continuous_axis_integrand_admission_returned',complete=report['complete'],
        completed_cells=completed,total_cells=actual.J-1,report_sha256=sha(record_path),
        actual_seconds=report['actual_seconds'],no_full_certificate_claimed=True)

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('repo','report','checkpoint','reference-bundle','carrier','node-report',
                 'scalar-input','preparation-report','outdir'):
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--state',choices=('initial','final'),default='final')
    p.add_argument('--panels',type=int,default=128)
    p.add_argument('--subdivisions',type=int,default=1)
    p.add_argument('--admission-seconds',type=float,default=600.)
    p.add_argument('--resume',action='store_true')
    args=p.parse_args()
    if args.panels<1 or args.subdivisions<1 or not math.isfinite(args.admission_seconds)or args.admission_seconds<=0:
        raise ValueError('Use declared positive complete-bound numerical budgets')
    main(args)
