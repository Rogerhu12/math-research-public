#!/usr/bin/env python3
"""Complete true-core prefix/cut C2 bounds at identical physical (s,theta).

Read a genuine QR anchor/fixed or fixed/fixed pair, together with each field's
own full angular tables and complete-cut coefficient report. Compare the
literal shared Hermite fields on the exact union of their physical radial
knots. The different finite e(s) charts are explicitly transported through
their inverse two-jets. No BVP, native tail, Jacobian, mean construction or
old low-lambda field is executed or regenerated.

This bounds one pair of the declared true-integral Cartesian maps. The
finite Gauss core.evaluate query is not redefined as an exact integral, nor
are its independently computed tangent values declared to be derivatives
of its rounded finite position. It is not a Cauchy proof or whole-surface
certificate. All interval data and per-span records remain outside Git.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_name] = '1'

import argparse
import bisect
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import sys
import time
import traceback

import numpy as np

HERE = Path(__file__).resolve().parent
SCRIPTS = HERE.parents[1]
REPO = SCRIPTS.parents[2]
sys.path.insert(0,str(HERE))
import prefix_physical_theta_c2_bounds as bounds

PAIR_GATE = SCRIPTS/'resume_20261128/tail/qr_fixed_complete_tail_c2.py'
PAIR_SHA = '1808a976bf4082fbe9b339fb24fdd7b87f3d29d36be05d15bcfdb7c7f24cc00e'
SCHEMA = 'genuine-QR-fixed-problem-complete-prefix-cut-same-material-theta-C2-v1'


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda:stream.read(1024*1024),b''):
            digest.update(block)
    return digest.hexdigest()


def ref(path):
    path = Path(path).resolve()
    return dict(path=str(path),sha256=sha(path))


def check(reference):
    path = Path(reference['path']).resolve()
    if ref(path) != reference:
        raise ValueError('A bound input changed: '+str(path))
    return path


def read(path):
    return json.loads(Path(path).read_text())


def read_bound(path):
    path = Path(path).resolve()
    content = path.read_bytes()
    return json.loads(content),dict(path=str(path),sha256=hashlib.sha256(content).hexdigest())


def write(path,value):
    path = Path(path)
    temporary = path.with_name(path.name+'.tmp')
    with temporary.open('w') as stream:
        json.dump(value,stream,indent=2,allow_nan=False)
        stream.write('\n');stream.flush();os.fsync(stream.fileno())
    temporary.replace(path)


def fq(value):
    if not np.isfinite(value):
        raise ValueError('A finite literal binary64 value is required')
    return Q.from_float(float(value))


def exact(value):
    if isinstance(value,Q):
        return str(value)
    if isinstance(value,bounds.Pair):
        return dict(size_exact=str(value.size),difference_exact=str(value.delta))
    if isinstance(value,dict):
        return {str(key):exact(item) for key,item in value.items()}
    if isinstance(value,(list,tuple)):
        return [exact(item) for item in value]
    return value


def scalar_summary(values):
    return {str(key):dict(upper_exact=str(value),display_only=float(value))
            for key,value in values.items()}


def checked_float64(value,shape=None):
    value = np.asarray(value)
    if (value.dtype != np.dtype('float64') or not np.all(np.isfinite(value))
            or (shape is not None and value.shape != shape)):
        raise ValueError('Require every finite literal binary64 defining coefficient')
    return value


def keys(pm,hm):
    pm,hm = np.asarray(pm),np.asarray(hm)
    if (pm.ndim != 1 or hm.ndim != 1
            or not np.issubdtype(pm.dtype,np.integer) or not np.issubdtype(hm.dtype,np.integer)
            or len(set(pm.tolist())) != len(pm) or len(set(hm.tolist())) != len(hm)
            or np.any(pm%3 != 1) or np.any(hm%3 != 0)
            or 1 not in pm or 0 not in hm):
        raise ValueError('Require the complete unique threefold planar and height spectra')
    return [('planar',int(m)) for m in pm]+[('height',int(m)) for m in hm]


def weight(key,order):
    return Q(abs(key[1])**order)


def vector_box_bound(array,shape):
    """Rational l1 upper bound of each vector norm, all closed sector boxes."""
    array = checked_float64(array,shape)
    if np.any(array[0] > array[1]):
        raise ValueError('An angular interval is reversed')
    maximum = np.maximum(np.abs(array[0]),np.abs(array[1]))
    # Max/abs only select or exactly negate binary inputs. Sum in Q, not float.
    return sum((fq(np.max(maximum[...,axis])) for axis in range(3)),Q(0))


def load_field(source,table_path,cut_path,problem):
    table_path,cut_path = Path(table_path).resolve(),Path(cut_path).resolve()
    report,table_reference = read_bound(table_path)
    cut,cut_reference = read_bound(cut_path)
    source['context'].require_report(report)
    source['context'].require_report(cut)
    if (report.get('status') != 'complete_angular_three_jet_interval_tables'
            or report.get('right_sector_endpoint_gram_equals_left_exactly') is not True
            or Path(report['source_run']).resolve() != Path(source['source_run']['path'])
            or report['source_run_sha256'] != source['source_run']['sha256']
            or report['physical_sha256'] != source['physical']['sha256']
            or report['modes'] != source['record']['modes']
            or report['homotopy'] != 1 or report['mean_nodes'] != source['mean_nodes']
            or report['source_mean_gauss_order'] != 6):
        raise ValueError('Require this actual field\'s complete original angular construction')
    for record in (report,cut):
        for path,digest in record['source_hashes'].items():
            check(dict(path=path,sha256=digest))
    if (Path(cut['table_report']).resolve() != table_path
            or cut['table_report_sha256'] != table_reference['sha256']
            or cut['defining_jets'] != report['defining_jets']):
        raise ValueError('The complete cut coefficients belong to another finite prefix')
    # A completed metric proof is not imposed as an extra pair-comparison
    # condition: complete cut data can already exist after an unresolved
    # metric attempt. Its actual constructor/source/field contract is required.
    if cut.get('status') not in {
        'continuous_full_cut_prefix_running', 'continuous_cut_prefix_unresolved',
        'continuous_full_cut_prefix_metric_geometry_certified',
        'continuous_cut_prefix_execution_failed'}:
        raise ValueError('No complete constructed cut is recorded for this field')
    cd = cut['cut_definition']
    for name in ('all_original_tail_modes_retained','full_height_identity_checked',
                 'tail_mean_value_cancelled_exactly','tail_mean_derivatives_retained'):
        if cd.get(name) is not True:
            raise ValueError('The complete literal cut contract is missing: '+name)
    if (cd.get('source_kind') != source['source_kind']
            or cd.get('full_height_binding') != source['final_height_binding']
            or cd.get('full_height_packet') != source['final_packet']
            or cd.get('raw_candidate_used_as_final_height') is not False):
        raise ValueError('Cut data must bind this final physical-H field without substitution')
    bundle = check(dict(path=cut['geometry_bundle'],sha256=cut['geometry_bundle_sha256']))
    defining = check(report['defining_jets'])
    with np.load(defining,allow_pickle=False) as archive:
        data = {name:archive[name].copy() for name in (
            'knots','jets','lift_jets','chart_jets','planar_modes','height_modes',
            'source_initial','E0','Epp','q','center_width')}
    x = checked_float64(data['knots'])
    if x.ndim != 1 or len(x) < 2 or x[0] != 0 or not np.all(np.diff(x)>0):
        raise ValueError('The entire physical-s knot sequence must be strictly increasing from zero')
    modes = keys(data['planar_modes'],data['height_modes'])
    checked_float64(data['jets'],(3,len(modes),len(x)))
    for name in ('lift_jets','chart_jets'):
        checked_float64(data[name],(3,1,len(x)))
        if np.any(data[name][:,:,-1] != 0):
            raise ValueError('Complete lift/chart two-jets at the actual cut must vanish')
    M = source['record']['modes']
    checked_float64(data['source_initial'],(3*M+1,))
    for name in ('E0','Epp','q','center_width'):
        checked_float64(data[name],())
    if (not abs(fq(data['E0'])) < 1 or not fq(data['center_width']) > 0
            or fq(data['q']) != fq(problem['gauge_q'])
            or report['radial_spans'] != len(x)-1
            or not np.array_equal(data['chart_jets'][:,0,0],
                                  np.array([data['E0'],0.,data['Epp']]))):
        raise ValueError('The complete finite center chart/gauge/radial representation changed')
    with np.load(check(source['physical']),allow_pickle=False) as physical:
        if x[-1] != physical['x'][-1]:
            raise ValueError('The finite prefix does not end at the genuine physical endpoint')
    endpoint,center = fq(x[-1]),fq(data['center_width'])
    width,start = Q(cd['cut_width_exact']),Q(cd['cut_start_exact'])
    if (Q(cd['prefix_end_exact']) != endpoint or start != endpoint-width
            or not 0 < center < start < endpoint
            or Q(cd['R_exact']) != fq(problem['physical_tail_parameters']['rCut'])
            or Q(cd['w_exact']) != fq(problem['physical_tail_parameters']['wCut'])):
        raise ValueError('The actual cut metric/domain or disjoint repair widths changed')
    oracle = report['oracle']
    expected = {name:fq(problem['core_settings'][key]) for name,key in (
        ('homotopy_exact','homotopy'),('S_exact','halfwidth'),
        ('b_exact','transition'),('k_exact','target_curvature'))}
    if (oracle.get('queried_core_kind') != 'true-R53-material-support'
            or oracle.get('zero_phase_specialization') is not True
            or oracle.get('source_field_relabelled') is not False
            or any(Q(v) != 0 for v in oracle['phase_controls_exact'])
            or oracle.get('true_period') != '2*pi/3'
            or any(Q(oracle[key]) != value for key,value in expected.items())):
        raise ValueError('Use the same true-integral core, window and fixed material origin')
    coefficients = list(map(Q,oracle['anchor_support_exact']))
    literal = (source['record']['returned_support_coefficients']
               if source['role'] == 'own_accepted_QR_fixed_metric_return'
               else source['record']['raw_return']['core_summary']['physical_parameters'])
    if len(coefficients) != M or coefficients != list(map(fq,literal)):
        raise ValueError('The entire oracle support list differs from the actual returned core')
    A = sum((abs((1-9*(j+1)**2)*v) for j,v in enumerate(coefficients)),Q(0))
    if A >= 1 or Q(oracle['rho_lower_exact']) != 1-A:
        raise ValueError('The current complete true inverse certificate is not this literal support')
    N = report['angular_boxes_per_sector']
    if type(N) is not int or N < 32:
        raise ValueError('Missing the complete true angular sector cover')
    angular = check(report['angular_tables'])
    lift_abs,center_abs = [],[]
    with np.load(angular,allow_pickle=False) as archive:
        for order in range(4):
            lift_abs.append(vector_box_bound(archive[f'box_lift_{order}'],(2,N,3)))
            array = checked_float64(archive[f'box_center_{order}'],(2,3,N,3))
            center_abs.append([vector_box_bound(array[:,j],(2,N,3)) for j in range(3)])
    cut_data = check(cut['cut_data'])
    with np.load(cut_data,allow_pickle=False) as archive:
        cut_modes = keys(archive['planar_modes'],archive['height_modes'])
        enclosures = checked_float64(archive['cut_coefficient_enclosures'],(2,3,len(cut_modes))).copy()
    if np.any(enclosures[0]>enclosures[1]):
        raise ValueError('A complete cut coefficient interval is reversed')
    cz = cut_modes.index(('height',0))
    if np.any(enclosures[:,0,cz] != 0):
        raise ValueError('The actual zeroth cut-height correction must cancel identically')
    cut_intervals = [{mode:(fq(enclosures[0,j,c]),fq(enclosures[1,j,c]))
                      for c,mode in enumerate(cut_modes)} for j in range(3)]
    return dict(source=source,report=report,cut_report=cut,data=data,keys=modes,
        x=list(map(fq,x)),end=endpoint,center_width=center,cut_width=width,
        core_coefficients=coefficients,lift_absolute=lift_abs,center_absolute=center_abs,
        cut_intervals=cut_intervals,
        identity=dict(table_report=table_reference,cut_report=cut_reference,
            defining_jets=report['defining_jets'],angular_tables=report['angular_tables'],
            cut_data=cut['cut_data'],geometry_bundle=ref(bundle),cut_definition=cd,
            table_status=report['status'],cut_status=cut['status'],
            core_oracle=oracle,source_initial_is_literal_saved_projection=True,
            numerical_core_position_is_not_the_defining_true_integral=True))


def projection(field):
    c = list(map(fq,field['data']['source_initial']))
    M,q = field['source']['record']['modes'],fq(field['data']['q'])
    result = {('planar',1):q*c[0]}
    for j in range(M):
        R,T,Z = c[1+j],c[1+M+j],c[1+2*M+j]
        m = 3*(j+1)
        result['planar',1+m] = q*(R+T)/2
        result['planar',1-m] = q*(R-T)/2
        result['height',m] = q*Z
    return result


def scalar_fourier_difference(left,right,order):
    return sum((abs(right.get(key,Q(0))-left.get(key,Q(0)))*weight(key,order)
                for key in set(left)|set(right)),Q(0))


def angular_differences(left,right,core):
    if any(fq(left['data'][name]) != fq(right['data'][name]) for name in ('E0','Epp','q')):
        raise ValueError('The same frozen inlet angular chart and gauge must be explicit')
    e0,epp = abs(fq(left['data']['E0'])),abs(fq(left['data']['Epp']))
    rho,rhop = 1+e0,3*e0
    G = core['core_derivative_differences']
    composed = [G[0],rho*G[1],rho*rho*G[2]+rhop*G[1]]
    tangent = [G[1],rho*G[2],rho*rho*G[3]+rhop*G[2]]
    pleft,pright = projection(left),projection(right)
    lift = [composed[j]+scalar_fourier_difference(pleft,pright,j) for j in range(3)]
    b = [epp/3,epp,3*epp]
    second = [b[0]*tangent[0],b[1]*tangent[0]+b[0]*tangent[1],
              b[2]*tangent[0]+2*b[1]*tangent[1]+b[0]*tangent[2]]
    target = [[composed[order],Q(0),second[order]] for order in range(3)]
    center = [[Q(0)]*3 for _ in range(3)]
    for radial in range(3):
        li = {key:fq(left['data']['jets'][radial,j,0]) for j,key in enumerate(left['keys'])}
        ri = {key:fq(right['data']['jets'][radial,j,0]) for j,key in enumerate(right['keys'])}
        hl,hr = (fq(field['data']['lift_jets'][radial,0,0]) for field in (left,right))
        for angular in range(3):
            absolute = max(field['lift_absolute'][angular] for field in (left,right))
            center[angular][radial] = (target[angular][radial]
                +scalar_fourier_difference(li,ri,angular)
                +max(abs(hl),abs(hr))*lift[angular]+abs(hr-hl)*absolute)
    cut = [[Q(0)]*3 for _ in range(3)]
    cut_absolute = [[[Q(0)]*3 for _ in range(4)] for _ in range(2)]
    for radial in range(3):
        ld,rd = left['cut_intervals'][radial],right['cut_intervals'][radial]
        for key in set(ld)|set(rd):
            lo,hi = ld.get(key,(Q(0),Q(0))),rd.get(key,(Q(0),Q(0)))
            d = max(abs(hi[0]-lo[1]),abs(hi[1]-lo[0]))
            for angular in range(3):
                cut[angular][radial] += d*weight(key,angular)
            for side,interval in enumerate((lo,hi)):
                for angular in range(4):
                    cut_absolute[side][angular][radial] += max(map(abs,interval))*weight(key,angular)
    return dict(lift=lift,center=center,cut=cut,cut_absolute=cut_absolute,
        common_inlet_rho_absolute=rho,common_inlet_rho_psi_absolute=rhop)


class RadialPolynomials:
    """Only the active source span is held as exact rational quintics."""
    def __init__(self,field,algebra):
        self.field,self.algebra = field,algebra
        self.index,self.polynomials = None,None

    def span(self,left,right):
        x = self.field['x']
        index = bisect.bisect_right(x,left)-1
        if not 0 <= index < len(x)-1 or not x[index] <= left < right <= x[index+1]:
            raise ValueError('A common span leaves a source shared-Hermite interval')
        if index != self.index:
            width = x[index+1]-x[index]
            values = {}
            for name in ('jets','lift_jets','chart_jets'):
                data = self.field['data'][name]
                values[name] = [self.algebra.hermite(
                    [fq(data[a,j,index]) for a in range(3)],
                    [fq(data[a,j,index+1]) for a in range(3)],width)
                    for j in range(data.shape[1])]
            self.index,self.polynomials = index,values
        start = (left-x[index])/(x[index+1]-x[index])
        length = (right-left)/(x[index+1]-x[index])
        result = {}
        for name,polys in self.polynomials.items():
            base = [self.algebra.restrict(poly,start,length) for poly in polys]
            orders = [base]
            for _ in range(2):
                orders.append([self.algebra.derivative(poly,right-left) for poly in orders[-1]])
            result[name] = orders
        return result


def compare_span(left,right,polys,angular,lo,hi,algebra):
    L,R = polys
    rows = []
    for field,values in zip((left,right),polys):
        rows.append([{key:values['jets'][a][j] for j,key in enumerate(field['keys'])}
                     for a in range(3)])
    W,CW = bounds.radial_weights(lo,hi,center_width=left['center_width'],
        end=left['end'],cut_width=left['cut_width'],algebra=algebra)
    h_abs = [[algebra.bernstein_abs(values['lift_jets'][a][0]) for a in range(3)] for values in polys]
    dh = [algebra.bernstein_abs(bounds.difference(L['lift_jets'][a][0],R['lift_jets'][a][0]))
          for a in range(3)]
    e_abs = [[algebra.bernstein_abs(values['chart_jets'][a][0]) for a in range(3)] for values in polys]
    E = [max(values[a] for values in e_abs) for a in range(3)]
    de = [algebra.bernstein_abs(bounds.difference(L['chart_jets'][a][0],R['chart_jets'][a][0]))
          for a in range(3)]
    absolute,same = {},{}
    for a,b in bounds.NEEDED:
        totals = []
        for side,(field,row) in enumerate(zip((left,right),rows)):
            value = sum((algebra.bernstein_abs(poly)*weight(key,b)
                         for key,poly in row[a].items()),Q(0))
            value += h_abs[side][a]*field['lift_absolute'][b]
            value += sum((W[a][j]*field['center_absolute'][b][j]
                          +CW[a][j]*angular['cut_absolute'][side][b][j] for j in range(3)),Q(0))
            totals.append(value)
        absolute[a,b] = max(totals)
        if (a,b) in bounds.SIX:
            value = sum((algebra.bernstein_abs(bounds.difference(
                rows[0][a].get(key,[Q(0)]),rows[1][a].get(key,[Q(0)])))*weight(key,b)
                for key in set(rows[0][a])|set(rows[1][a])),Q(0))
            value += max(h_abs[0][a],h_abs[1][a])*angular['lift'][b]
            value += dh[a]*max(left['lift_absolute'][b],right['lift_absolute'][b])
            value += sum((W[a][j]*angular['center'][b][j]+CW[a][j]*angular['cut'][b][j]
                          for j in range(3)),Q(0))
            same[a,b] = value
    physical,chart = bounds.physical_theta_pair(same,absolute,E,de)
    return dict(physical=physical,same_psi=same,absolute_cartesian=absolute,
                chart=chart,chart_absolute=E,chart_difference=de,radial_lift_difference=dh)


def compare(args):
    out = args.outdir.resolve()
    if out == REPO or REPO in out.parents:
        raise ValueError('All actual pair data and journals stay outside the repository')
    output_created = False
    started = time.monotonic()
    report = dict(schema=SCHEMA,status='checking_genuine_complete_fixed_pair',
        finite_pair_C2_certified=False,C2_limit_proved=False,whole_surface=False,
        same_physical_material_theta=True,same_computational_psi_substituted=False,
        numerical_core_query_error_certified=False,new_solver_or_native_calls=0,
        source_hashes={str(Path(__file__).resolve()):sha(__file__),
                       str(Path(bounds.__file__).resolve()):sha(bounds.__file__)})
    try:
        if sha(PAIR_GATE) != PAIR_SHA:
            raise ValueError('The genuine pair gate needs an explicit new source version')
        spec = importlib.util.spec_from_file_location('_fixed_actual_prefix_pair_gate',PAIR_GATE)
        gate = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = gate;spec.loader.exec_module(gate)
        # The old anonymous-QR anchor continuous provider is not an alias for
        # a new mapped-QR anchor. Own fixed1/fixed2 remains fully supported.
        preliminary_left,preliminary_right = read(args.left_source_run),read(args.right_source_run)
        if (preliminary_right.get('model_kind') == gate.FIXED_KIND
                and preliminary_left.get('model_kind') != gate.FIXED_KIND
                and preliminary_right['fixed_problem']['anchor_source_kind'] != gate.ANCHOR_SOURCE_KIND):
            raise ValueError('This anchor-left needs its own explicit continuous provider; compare two genuine own fixed returns meanwhile')
        ls,rs,agreement,algebra,roots = gate.accepted_pair(args)
        if any(out == root or root in out.parents for root in roots):
            raise ValueError('The pair output may not be inside any preserved source tree')
        out.mkdir(parents=True,exist_ok=False)
        output_created = True
        problem = agreement['fixed_problem']
        fields = [load_field(source,tables,cut,problem) for source,tables,cut in (
            (ls,args.left_tables,args.left_cut),(rs,args.right_tables,args.right_cut))]
        left,right = fields
        if any(left[key] != right[key] for key in ('end','center_width','cut_width')):
            raise ValueError('Compare the same exact physical domain and declared repair widths')
        settings = problem['core_settings']
        core = bounds.true_core_pair(left['core_coefficients'],right['core_coefficients'],
            homotopy=fq(settings['homotopy']),halfwidth=fq(settings['halfwidth']),
            transition=fq(settings['transition']),curvature=fq(settings['target_curvature']))
        angular = angular_differences(left,right,core)
        grid = sorted(set(left['x']+right['x']+[left['center_width'],left['end']-left['cut_width']]))
        if grid[0] != 0 or grid[-1] != left['end']:
            raise ValueError('The common exact partition does not cover the complete prefix')
        report.update(status='complete_same_theta_pair_running',pair=agreement,
            left_source=gate.source_metadata(ls),right_source=gate.source_metadata(rs),
            left_definition=left['identity'],right_definition=right['identity'],
            true_core_pair=exact(core),angular_difference_inputs=exact(angular),
            total_common_spans=len(grid)-1,completed_spans=0,
            exact_common_grid_sha256=hashlib.sha256(('\n'.join(map(str,grid))+'\n').encode()).hexdigest(),
            physical_s_range=['0',str(left['end'])],angular_range='all real theta modulo 2*pi',
            center_width_exact=str(left['center_width']),cut_width_exact=str(left['cut_width']),
            no_rigid_phase_height_or_core_center_alignment=True,
            source_Gauss_projection_and_mean_are_literal_coefficients=True,
            mathematical_core_definition='True R53 phase and position integrals, fixed threefold center.',
            numerical_query_responsibility=('The source core.evaluate finite-Gauss point function is an '
                'approximation to this definition. Its query error is not inferred from BVP residuals '
                'or from separately supplied tangent values. See the exact query-error propagation formula.'),
            all_complete_planar_height_and_zero_modes_retained=True,
            old_field_numerical_certificates_reused=False)
        report['source_hashes'].update({str(PAIR_GATE):PAIR_SHA,str(Path(algebra.__file__).resolve()):sha(algebra.__file__)})
        for field in fields:
            report['source_hashes'].update(field['report']['source_hashes'])
            report['source_hashes'].update(field['cut_report']['source_hashes'])
        report['source_hashes'].update({str(gate.ANALYTIC/'qr_fixed_actual_prefix_continuous.py'):
                                       sha(gate.ANALYTIC/'qr_fixed_actual_prefix_continuous.py')})
        extractors = [RadialPolynomials(field,algebra) for field in fields]
        maxima = {key:Q(0) for key in bounds.SIX}
        same_max = dict(maxima)
        witnesses = {}
        chart_max = Q(0)
        write(out/'summary.json',report)
        journal = out/'complete-common-spans.jsonl'
        with journal.open('x') as stream:
            cursor = Q(0)
            for ordinal,(lo,hi) in enumerate(zip(grid[:-1],grid[1:])):
                if lo != cursor or not lo < hi:
                    raise ValueError('The exact common partition has a gap or repeated span')
                polynomials = [extractor.span(lo,hi) for extractor in extractors]
                value = compare_span(left,right,polynomials,angular,lo,hi,algebra)
                row = dict(ordinal=ordinal,left_exact=str(lo),right_exact=str(hi),**exact(value))
                stream.write(json.dumps(row,allow_nan=False)+'\n');stream.flush();os.fsync(stream.fileno())
                for key,bound in value['physical'].items():
                    if bound > maxima[key]:
                        maxima[key] = bound
                        witnesses[str(key)] = dict(ordinal=ordinal,left_exact=str(lo),right_exact=str(hi))
                    same_max[key] = max(same_max[key],value['same_psi'][key])
                chart_max = max(chart_max,value['chart']['phase'])
                cursor = hi
                report.update(completed_spans=ordinal+1,last_right_exact=str(cursor),
                    physical_C2_component_bounds=scalar_summary(maxima),
                    same_psi_component_bounds=scalar_summary(same_max),
                    inverse_angle_difference_upper_exact=str(chart_max),worst_spans=witnesses,
                    seconds=time.monotonic()-started)
                write(out/'summary.json',report)
                if (ordinal+1)%32 == 0 or ordinal+1 == len(grid)-1:
                    print(json.dumps(dict(stage='same_physical_theta_C2_pair',
                        completed=ordinal+1,total=len(grid)-1,seconds=report['seconds'])),flush=True)
        if cursor != left['end'] or report['completed_spans'] != len(grid)-1:
            raise ValueError('Not every original common radial span has a complete durable result')
        # These are squared Frobenius bounds for derivative orders 1 and 2;
        # no rounded square root is promoted to an upper bound.
        grouped = dict(position=maxima[0,0],
            gradient_frobenius_squared=maxima[1,0]**2+maxima[0,1]**2,
            hessian_frobenius_squared=maxima[2,0]**2+2*maxima[1,1]**2+maxima[0,2]**2)
        report.update(status='complete_true_integral_prefix_cut_same_theta_finite_pair_certified',
            finite_pair_C2_certified=True,complete_common_spans=ref(journal),
            grouped_derivative_bounds=scalar_summary(grouped),
            reflected_prefix_has_identical_component_bounds=True,
            cylinder_tail_marker_and_phase_frame_not_in_this_report=True,
            maximum_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            seconds=time.monotonic()-started)
        for field in fields:
            for name in ('table_report','cut_report','defining_jets','angular_tables','cut_data','geometry_bundle'):
                check(field['identity'][name])
            for name in ('source_run','raw','physical','final_height_binding','final_packet',
                         'runtime','baseline','port','native_manifest'):
                check(field['source'][name])
        for path,digest in report['source_hashes'].items():
            check(dict(path=path,sha256=digest))
        write(out/'summary.json',report)
        print(json.dumps(dict(status=report['status'],spans=report['completed_spans'],
            bounds=report['physical_C2_component_bounds'],seconds=report['seconds'])),flush=True)
        return 0
    except Exception as error:
        report.update(status='complete_same_theta_pair_not_certified',error=repr(error),
            finite_pair_C2_certified=False,seconds=time.monotonic()-started)
        if output_created:
            (out/'exception.txt').write_text(traceback.format_exc())
            write(out/'summary.json',report)
        raise


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--left-source-run',type=Path,required=True)
    parser.add_argument('--left-coupling-summary',type=Path,
        help='Required only for the genuine QR anchor; never for an own fixed return.')
    parser.add_argument('--right-source-run',type=Path,required=True)
    parser.add_argument('--left-tables',type=Path,required=True)
    parser.add_argument('--right-tables',type=Path,required=True)
    parser.add_argument('--left-cut',type=Path,required=True)
    parser.add_argument('--right-cut',type=Path,required=True)
    parser.add_argument('--outdir',type=Path,required=True)
    return compare(parser.parse_args())


if __name__ == '__main__':
    raise SystemExit(main())
