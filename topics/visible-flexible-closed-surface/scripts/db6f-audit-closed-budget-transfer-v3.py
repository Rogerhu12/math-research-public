#!/usr/bin/env python3
"""Exact scalar closed-map budget with the explicit paired transfer interface, v3.

V3 pins the separately frozen transfer-v3 producer and its four bookkeeping
keys. Its parameter-only mode does not construct or certify a finite map.
The geometric inequalities and exact scalar arithmetic are unchanged.

This joins previously certified finite-map bounds and analytic background
lemmas. It is not a full tail metric/curvature certificate. All numerical
comparisons below are Fraction comparisons of saved outward bounds.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def q(x):return Q.from_float(float(x))
def low(x):
    f=float(x);return math.nextafter(f,-math.inf) if Q.from_float(f)>x else f
def high(x):
    f=float(x);return math.nextafter(f,math.inf) if Q.from_float(f)<x else f
def record(x):return {'exact':str(x),'lower_display':low(x),'upper_display':high(x)}

# V3 changes only the explicit transfer interface and its identity guards.
# Scalar geometry/moment arithmetic below is copied verbatim from the v2 file.
BASE_BUDGET_SHA256='0d68b718a43a69b24a865b1932e2700a47190724a3be4ea3f1202b56d1a59641'
BASE_TRANSFER_SHA256='35aa82514ec2be4b78cf3670e97343d0ba50085a7a6a687273108fbb6eb09705'
TRANSFER_FILE=HERE/'db6f-tail-transfer-background-v3.py'
TRANSFER_SHA256='bdf6307fd93328b1ae70923caac2687fa19b0187ca9c723fe5d7072d7799a47b'
ADDITIONAL_NUMERICAL_KEYS={'iterationCheckpointFile','sharedEngines',
                           'trialDiagnosticFile','trialStatePrefix'}
BASE_NUMERICAL_KEYS=set('''modes spacing depth physicalDepth steps quadrature linearFar
linearSteps linearMethod fastJacobian cuspAwareFlow actualCuspGrid
solveTolerance auditSteps maxIterations traceFile initialCheckpoint
harmonicAmplitudePredictor shootingParts warpSteps quadratureTolerance
cuspAwareQuadrature maxCachedBetas nodeIndex rhsEvaluation projectionFloor
farPadding'''.split())
PARAMETER_POLICY={
    'id':'visible-flat17-bookkeeping-keys-v2',
    'additional_numerical_keys':sorted(ADDITIONAL_NUMERICAL_KEYS),
    'base_file':'db6f-root-transfer-background.py',
    'base_sha256':BASE_TRANSFER_SHA256,
    'difference_semantics':'Key presence and canonical JSON value including JSON types; an unknown added null key rejects.'}
PARAMETER_POLICY_SHA256='2b4fd1d141d9116157037d05748ab2a019c9033441453ee8e6ab917eb355eae3'
BACKGROUND_SHA256={
    'checkpoint':'d23b03e4ce5cd7aaf4ac9d1134f8a23ee274be3a1d0a0192a7b294f1195e43f0',
    'calibrations':'bcfaba00aec62290b5b29432836c9e76ef6cf0d582b06c046677b0f8688ca9f4',
    'alpha':'04aae85c19f78fd82808ac32b104537dbb584c39cac8a648107722c855685c62',
    'cell_zero_A':'2f41f4a2a5879e9363f4e12aa52576aaa758a860c338f19e959e6f387c1b33de',
    'inner_A':'23f67ca7d0bfb981b29f9bddd5bbdd3f8fbb55720c0866c67db3194c858f7bba',
    'outer_B':'53676270742794da8af79d539aece0b7f88dc98d1c73ab1668157ebe700ba185'}


def check(ok,message):
    if not ok:raise ValueError(message)


def resolve(parent,value):
    check(isinstance(value,str) and bool(value),'Missing file reference')
    p=Path(value)
    for candidate in (p,Path(parent)/p,Path(parent)/p.name,HERE.parent/p):
        if candidate.is_file():return candidate
    raise ValueError('Referenced file is unavailable: '+value)


def read_json(path):
    import gzip
    raw=Path(path).read_bytes()
    if raw[:2]==b'\x1f\x8b':raw=gzip.decompress(raw)
    return json.loads(raw)


def checkpoint_parameters(path):
    record=read_json(path)
    check(type(record) is dict,'Checkpoint must be a JSON object')
    response=record.get('response',record)
    check(type(response) is dict,'Checkpoint response must be a JSON object')
    cp=response.get('checkpoint',response.get('tail_checkpoint',response))
    check(type(cp) is dict and type(cp.get('parameters')) is dict,
          'Checkpoint has no readable parameter dictionary')
    return cp['parameters']


def canonical(value):
    return json.dumps(value,sort_keys=True,separators=(',',':'),ensure_ascii=True,allow_nan=False)


def load_transfer_implementation(report):
    check(sha(HERE/'db6f-root-closed-budget-v2.py')==BASE_BUDGET_SHA256,
          'Frozen base closed-budget implementation changed')
    check(sha(HERE/'db6f-root-transfer-background.py')==BASE_TRANSFER_SHA256,
          'Frozen base transfer implementation changed')
    check(isinstance(TRANSFER_SHA256,str) and sha(TRANSFER_FILE)==TRANSFER_SHA256,
          'Paired transfer implementation is not the frozen reviewed source')
    check(report.get('script_sha256')==TRANSFER_SHA256 and
          report.get('base_transfer_script_sha256')==BASE_TRANSFER_SHA256,
          'Wrong transfer or base source identity')
    check(report.get('parameter_policy')==PARAMETER_POLICY and
          report.get('parameter_policy_sha256')==PARAMETER_POLICY_SHA256 and
          hashlib.sha256(canonical(report['parameter_policy']).encode()).hexdigest()==PARAMETER_POLICY_SHA256,
          'Wrong explicit parameter policy')
    check(report.get('all_other_parameters_identical') is True,
          'Transfer parameter comparison was not completed')
    spec=importlib.util.spec_from_file_location('closed_budget_explicit_transfer_v3',TRANSFER_FILE)
    same=importlib.util.module_from_spec(spec);sys.modules[spec.name]=same;spec.loader.exec_module(same)
    check(same.NUMERICAL_KEYS==BASE_NUMERICAL_KEYS|ADDITIONAL_NUMERICAL_KEYS,
          'Transfer numerical-key set is broader or narrower than the reviewed policy')
    return same


def parameter_differences(old,new,allowed):
    """Presence is significant, including an unknown added or removed null."""
    check(type(old) is dict and type(new) is dict,'Parameter inputs must be objects')
    for parameters in (old,new):
        for key in ADDITIONAL_NUMERICAL_KEYS:
            if key not in parameters or parameters[key] is None:continue
            if key=='sharedEngines':
                check(type(parameters[key]) is bool,'sharedEngines must be boolean or null')
            else:
                check(type(parameters[key]) is str,key+' must be a string or null')
    different=[key for key in sorted(set(old)|set(new))
               if key not in old or key not in new or canonical(old[key])!=canonical(new[key])]
    forbidden=[key for key in different if key not in allowed]
    check(not forbidden,'Unapproved changed physical or unknown parameter: '+', '.join(forbidden))
    return different


def verify_definitions(definitions,parent,height_path,positive_path):
    check(type(definitions) is dict and set(definitions)==set(BACKGROUND_SHA256),
          'The six frozen background definitions are not exactly present')
    paths={}
    for key,expected in BACKGROUND_SHA256.items():
        item=definitions[key]
        check(type(item) is dict and set(item)=={'file','sha256'} and item['sha256']==expected,
              'Changed frozen background definition: '+key)
        path=resolve(parent,item['file'])
        check(sha(path)==expected,'Changed background definition file: '+key)
        paths[key]=path
    height,positive=read_json(height_path),read_json(positive_path)
    check(height['checkpointSHA256']==positive['checkpointSHA256']==BACKGROUND_SHA256['checkpoint'],
          'Height/positive-alpha input does not have the frozen background checkpoint')
    check(positive['calibrationTableSHA256']==BACKGROUND_SHA256['calibrations'] and
          positive['cellZeroCertificateSHA256']==sha(height_path),
          'Height/calibration/positive-alpha proof connection changed')
    check(positive.get('positiveExactGlobalRadialAlphaProved') is True,
          'Exact positive radial normalization is not certified')
    tight=read_json(paths['alpha'])
    for key in ('checkpoint','calibrations','cell_zero_A','inner_A','outer_B'):
        item=tight['inputs'][key]
        check(item['sha256']==BACKGROUND_SHA256[key] and
              sha(resolve(paths['alpha'].parent,item['file']))==BACKGROUND_SHA256[key],
              'Tight-alpha input connection changed: '+key)
    book=tight['inputs']['numerical_bookkeeping']
    check(height['bookkeepingSHA256']==read_json(paths['calibrations'])['bookkeepingSHA256']==book['sha256'] and
          sha(resolve(paths['alpha'].parent,book['file']))==book['sha256'],
          'Frozen calibration/height bookkeeping connection changed')
    return paths


def verify_source_context(path,height_path,positive_path):
    """Metadata and file hashes only; no radial grid or geometry is evaluated."""
    report=read_json(path)
    same=load_transfer_implementation(report)
    check(report.get('background_definition_hashes_verified') is True,
          'Producer did not complete its background source identity checks')
    definitions=report['background_definition_hashes']
    paths=verify_definitions(definitions,path.parent,height_path,positive_path)
    old_manifest=resolve(path.parent,report['old_manifest'])
    check(sha(old_manifest)==report['old_manifest_sha256'],'Old background manifest changed')
    old_meta=read_json(old_manifest)
    check(old_meta.get('finished') is True and old_meta['inputSHA256']==BACKGROUND_SHA256['checkpoint'],
          'Old manifest is incomplete or has another physical source checkpoint')
    old_checkpoint=resolve(old_manifest.parent,old_meta['input'])
    check(sha(old_checkpoint)==BACKGROUND_SHA256['checkpoint'],'Old manifest source checkpoint changed')
    parameter_differences(checkpoint_parameters(paths['checkpoint']),old_meta['parameters'],same.NUMERICAL_KEYS)
    packet_path=resolve(path.parent,report['input_packet'])
    check(sha(packet_path)==report['input_packet_sha256'],'Original background packet changed')
    packet=read_json(packet_path)
    check(packet.get('finished') is True and packet['finite_tail_manifest_sha256']==sha(old_manifest),
          'Original packet is incomplete or belongs to a different old manifest')
    check(packet['background_definition_hashes']==definitions,'Transfer changed the source definition mapping')
    data=resolve(packet_path.parent,packet['data_file'])
    check(sha(data)==packet['data_sha256']==report['input_data_sha256'],'Original packet data changed')
    if 'input_data_file' in report:
        check(sha(resolve(path.parent,report['input_data_file']))==sha(data),'Input-data path/hash mismatch')
    return report,same,old_manifest,old_meta,packet_path,data


def verify_completed_transfer(path,new_manifest,height_path,positive_path):
    report,same,old_manifest,old_meta,packet,data=verify_source_context(path,height_path,positive_path)
    check(report.get('finished') is True and report.get('mode')=='finite-background-grid-transfer',
          'A parameter preflight is not a completed transfer')
    check(report['new_manifest_sha256']==report['finite_tail_manifest_sha256']==sha(new_manifest),
          'Transfer targets a different actual finite-tail manifest')
    check(sha(resolve(path.parent,report['new_manifest']))==sha(new_manifest),'New-manifest path/hash mismatch')
    new_meta=read_json(new_manifest)
    check(new_meta.get('finished') is True,'New finite-tail export is incomplete')
    checkpoint=resolve(new_manifest.parent,new_meta['input'])
    check(sha(checkpoint)==new_meta['inputSHA256'],'New manifest source checkpoint changed')
    parameter_differences(checkpoint_parameters(checkpoint),new_meta['parameters'],same.NUMERICAL_KEYS)
    different=parameter_differences(old_meta['parameters'],new_meta['parameters'],same.NUMERICAL_KEYS)
    check(different==report['different_numerical_parameter_keys'],'Transfer parameter ledger mismatch')
    _,old_grid=same.grid(old_manifest);_,new_grid=same.grid(new_manifest)
    check(old_grid[0]==new_grid[0] and old_grid[-1]==new_grid[-1],
          'Transferred physical background domains differ')
    check(report['old_finite_spans']==len(old_grid)-2 and report['new_finite_spans']==len(new_grid)-2,
          'Transfer grid counts do not match the actual manifests')
    from types import SimpleNamespace
    _,_,new_data=same.consumer.load_packet(path,SimpleNamespace(path=new_manifest,N=len(new_grid)-2))
    return {'file':str(path),'sha256':sha(path),'old_manifest_sha256':sha(old_manifest),
            'new_manifest_sha256':sha(new_manifest),'input_packet_sha256':sha(packet),
            'input_data_sha256':sha(data),'transferred_data_sha256':sha(new_data),
            'producer_script_sha256':TRANSFER_SHA256,'base_transfer_script_sha256':BASE_TRANSFER_SHA256,
            'parameter_policy_sha256':PARAMETER_POLICY_SHA256,
            'background_definition_hashes':report['background_definition_hashes'],
            'six_background_definition_files_rehashed':True}


def verify_parameter_preflight(path,height_path,positive_path):
    report,same,old_manifest,old_meta,packet,data=verify_source_context(path,height_path,positive_path)
    check(report.get('status')=='read-only-parameter-and-background-source-preflight' and
          report.get('mode')=='parameter-only-preflight','Not the explicit parameter-preflight schema')
    check('finished' not in report and 'finite_tail_manifest_sha256' not in report and
          'new_manifest_sha256' not in report and 'data_file' not in report,
          'Parameter preflight contains geometric-transfer completion fields')
    check(report.get('geometric_transfer_performed') is False and
          report.get('finite_map_was_created') is False and
          type(report.get('actual_new_root_flow_solver_calls')) is int and
          report['actual_new_root_flow_solver_calls']==0,'Preflight scope flags disagree')
    checkpoint=resolve(path.parent,report['new_parameter_checkpoint'])
    check(sha(checkpoint)==report['new_parameter_checkpoint_sha256'],'Preflight checkpoint changed')
    new_parameters=checkpoint_parameters(checkpoint)
    different=parameter_differences(old_meta['parameters'],new_parameters,same.NUMERICAL_KEYS)
    check(different==report['different_numerical_parameter_keys'],'Preflight parameter ledger mismatch')
    return {'status':'independent-consumer-parameter-preflight-only',
            'mode':'parameter-only-preflight','script_sha256':sha(__file__),
            'base_closed_budget_script_sha256':BASE_BUDGET_SHA256,
            'producer_preflight':str(path),'producer_preflight_sha256':sha(path),
            'producer_script_sha256':TRANSFER_SHA256,'base_transfer_script_sha256':BASE_TRANSFER_SHA256,
            'parameter_policy':PARAMETER_POLICY,'parameter_policy_sha256':PARAMETER_POLICY_SHA256,
            'old_manifest':str(old_manifest),'old_manifest_sha256':sha(old_manifest),
            'input_packet':str(packet),'input_packet_sha256':sha(packet),'input_data_sha256':sha(data),
            'new_parameter_checkpoint':str(checkpoint),'new_parameter_checkpoint_sha256':sha(checkpoint),
            'different_numerical_parameter_keys':different,'all_other_parameters_identical':True,
            'background_definition_hashes':report['background_definition_hashes'],
            'six_background_definition_files_rehashed':True,
            'proof_inputs':{key:{'file':str(p),'sha256':sha(p)} for key,p in
                           (('height',height_path),('positive_alpha',positive_path))},
            'geometric_transfer_performed':False,'finite_map_was_created':False,
            'radial_grid_was_evaluated':False,'geometry_metric_curvature_were_evaluated':False,
            'actual_new_root_flow_solver_calls':0,'README_complete':False,
            'scope':'Only frozen source identity and parameter-policy compatibility; no future finite map or new certificate is asserted.'}



def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('geometry','geometry-certificate','metric-certificate','moment-certificate',
                'tail-first','height','positive-alpha','out'):
        p.add_argument('--'+key,type=Path,required=(key=='out'))
    p.add_argument('--background-transfer',type=Path)
    p.add_argument('--check-transfer-policy-only',type=Path,
                   help='Recheck a producer parameter preflight, without geometry or grid evaluation')
    a=p.parse_args()
    if a.out.exists():p.error('Refusing to overwrite a previous output')
    if a.check_transfer_policy_only is not None:
        if a.height is None or a.positive_alpha is None:
            p.error('Parameter preflight requires --height and --positive-alpha')
        if any(getattr(a,key) is not None for key in
               ('geometry','geometry_certificate','metric_certificate','moment_certificate',
                'tail_first','background_transfer')):
            p.error('Parameter-only preflight cannot receive geometric certificate inputs')
        report=verify_parameter_preflight(a.check_transfer_policy_only,a.height,a.positive_alpha)
        a.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
        print(json.dumps({'status':report['status'],'different_numerical_parameter_keys':report['different_numerical_parameter_keys'],
                          'geometric_transfer_performed':False,'finite_map_was_created':False}))
        return
    missing=[key for key in ('geometry','geometry_certificate','metric_certificate','moment_certificate',
                            'tail_first','height','positive_alpha') if getattr(a,key) is None]
    if missing:p.error('Closed-map mode requires '+', '.join('--'+key.replace('_','-') for key in missing))
    meta=json.loads(a.geometry.read_text())
    geo=json.loads(a.geometry_certificate.read_text());metric=json.loads(a.metric_certificate.read_text())
    moment=json.loads(a.moment_certificate.read_text());tail=json.loads(a.tail_first.read_text())
    height=json.loads(a.height.read_text());alpha=json.loads(a.positive_alpha.read_text())
    for d in (geo,metric,moment):
        if d['geometry_sha256']!=sha(a.geometry):raise ValueError('Prefix certificate bound to another graph')
    if tail['manifestSHA256']!=meta['tail_manifest_sha256']:raise ValueError('Tail first-jet certificate mismatch')
    tail_manifest=Path(meta['tail_manifest']);tmeta=json.loads(tail_manifest.read_text())
    if height['checkpointSHA256']!=alpha['checkpointSHA256']:
        raise ValueError('Background height and alpha do not share the physical input')
    transfer_binding=None
    if a.background_transfer is not None or tmeta['inputSHA256']!=height['checkpointSHA256']:
        if a.background_transfer is None:
            raise ValueError('A reviewed same-background transfer is required for different numerical checkpoints')
        if sha(tail_manifest)!=meta['tail_manifest_sha256']:
            raise ValueError('Actual tail manifest differs from the closed-map definition')
        transfer_binding=verify_completed_transfer(a.background_transfer,tail_manifest,a.height,a.positive_alpha)
    if not alpha['positiveExactGlobalRadialAlphaProved']:raise ValueError('Positive exact background alpha not paid')
    implementations=[HERE/'db6f-root-common-cut.py',HERE/'db6f-root-common-cut-v2.py']
    matches=[p for p in implementations if sha(p)==meta['common_cut_implementation_sha256']]
    if len(matches)!=1:raise ValueError('No unique frozen common-cut implementation')
    s=importlib.util.spec_from_file_location('common_cut_budget',matches[0])
    common=importlib.util.module_from_spec(s);sys.modules[s.name]=common;s.loader.exec_module(common)
    base=common.module('common_cut_budget_intervals','db6f-audit-continuous-hermite.py');common.install(base)
    shape=base.ExactHermite(a.geometry)
    Hlo,Hhi=q(shape.background_cut_height.lo),q(shape.background_cut_height.hi)
    c=q(tmeta['parameters']['rCut']);cuff=q(tmeta['parameters']['rCuff'])
    if not Q(7,50)<cuff<Q(3,20) or c>Q(3,5):raise ValueError('Frozen radius box failed')
    f,cl=tail['finite'],tail['collar']
    maximum=lambda key:max(q(f[key]),q(cl[key]))
    vh=maximum('r0theta0Planar');vz=maximum('r0theta0Height')
    vrh=maximum('r1theta0Planar');vrz=maximum('r1theta0Height')
    vth=maximum('relativePlanarAngularDerivativeUpper')
    vtz=maximum('r0theta1Height')/cuff
    jmin=min(q(f['planarRadialJacobianOverRLower']),q(cl['planarRadialJacobianOverRLower']))
    if not (tail['entireTail']['planarJacobianPositive'] and tail['entireTail']['allCrossSectionsSimple']):
        raise ValueError('First-jet hypotheses fail')
    wmax=Q(16,15)  # separately reviewed whole-background slope lemma
    jmax=1+vrh+vth+vrh*vth
    nh=(wmax+vrz)*(1+vth)+vtz*(1+vrh)
    zmin=Hlo-vz;zmax=Hhi+q(height['wholeHeightUpper'])+vz
    rmax=c+vh
    normN=Q(3,2)
    if not jmax*jmax+nh*nh<normN*normN:raise ValueError('Normal-length budget fails')
    numerator=zmin*jmin-rmax*nh
    if numerator<=0:raise ValueError('Tail support positivity not proved')
    tail_support=numerator/normN
    cap_min_height=Hlo
    cap_gradient_factor=Q(101,100)  # > sqrt(1.01)
    cap_support=(cap_min_height-Q(3,200))/cap_gradient_factor
    support=min(q(geo['support_lower']),tail_support,cap_support)
    R=Q(49,25);D=2*R
    if not (q(geo['norm_upper'])<R and rmax*rmax+zmax*zmax<R*R):raise ValueError('Band ball budget fails')
    cap_zmax=Hhi+q(height['wholeHeightUpper'])+Q(1,2000)
    if not cuff*cuff+cap_zmax*cap_zmax<R*R:raise ValueError('Cap ball budget fails')
    witness=q(geo['witness_distance_lower'])
    if not min(zmin,cap_min_height)>witness:raise ValueError('Tail/caps may approach the core witness')
    holdratio=witness/D;held=2*cap_min_height
    if not (holdratio>Q(1,20) and held>D/5):raise ValueError('Geometric visible/hold budgets fail')
    # The proved annular flux bound, using pi<22/7.
    piup=Q(22,7);bh=q(height['wholeHeightUpper'])
    T=(max(abs(Hlo),abs(Hhi))+bh)*4*piup*c*vh*rmax**3+piup*vz*rmax**5
    Alo=q(moment['mirrored_prefix_real_moment_interval'][0])-2*T
    Ahi=q(moment['mirrored_prefix_real_moment_interval'][1])+2*T
    if Alo<=0:raise ValueError('Nonzero complete volume moment not proved')
    # B3=3*pi*a^3*b^2*h/4, pi>3 is enough for a strict lower bound.
    B3lo=Q(9,4)*Q(2,25)**3*Q(3,100)**2*Q(1,2000)
    tensor_gap=Alo*B3lo
    bridge=json.loads(Path(meta['bridge_parameter_certificate']).read_text())
    eta=q(bridge['relative_target_metric_difference_upper']);eps=q(metric['metric_operator_upper'])
    report={'status':'exact-scalar-budget-for-defined-finite-closed-map-pending-independent-assembly-review',
      'script_sha256':sha(__file__),
      'base_closed_budget_script_sha256':BASE_BUDGET_SHA256,
      'inputs':{key:{'file':str(getattr(a,key)),'sha256':sha(getattr(a,key))}for key in
                ('geometry','geometry_certificate','metric_certificate','moment_certificate','tail_first','height','positive_alpha')},
      'same_background_transfer':transfer_binding,
      'tail_support_lower':record(tail_support),'whole_surface_support_lower':record(support),
      'tail_height_lower':record(zmin),'tail_height_upper':record(zmax),
      'ball_radius_upper':record(R),'diameter_upper':record(D),
      'hausdorff_hold_lower':record(witness),'hold_over_diameter_lower':record(holdratio),
      'held_region_diameter_lower':record(held),'two_tail_moment_absolute_upper':record(2*T),
      'unmarked_volume_moment_real_lower':record(Alo),'unmarked_volume_moment_real_upper':record(Ahi),
      'centered_third_tensor_norm_squared_change_lower':record(tensor_gap),
      'corrected_prefix_exact_target_metric_upper':record(eps*(1+eta)+eta),
      'embedding_all_phases_follows_from_support_given_reviewed_assembly':True,
      'rigid_noncongruence_follows_from_moment_given_reviewed_assembly':True,
      'whole_tail_metric_certified':False,'whole_tail_curvature_certified':False,
      'quantitative_reach_certified':False,'README_complete':False,
      'remaining':['independent common-cut/closed-map implementation review',
                   'tight exact background parameter enclosure and whole-tail metric',
                   'actual whole-tail curvature and reach >= .03D',
                   'fixed-g high-frequency/full-XYZ convergence and final independent replay']}
    a.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({key:[report[key]['lower_display'],report[key]['upper_display']]for key in
          ('whole_surface_support_lower','diameter_upper','hold_over_diameter_lower',
           'unmarked_volume_moment_real_lower','corrected_prefix_exact_target_metric_upper')},indent=2))


if __name__=='__main__':main()
