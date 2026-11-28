"""Consume an actual R688 parameter vector and paid whole-cell bounds for R696."""
from fractions import Fraction as F
import hashlib
import json
import os
from math import isfinite, isqrt
import struct


ACTUAL_REQUEST_SHA = '0218265a5a3cd1fb41d1544308679580c7618bfe07f0fbc043d8f43d8951ea63'
ACTUAL_SOURCE_COMMIT = '5374a6817d9761fbea489d44803e4728ddc22d0b'
ACTUAL_RUN = 46148075849
ACTUAL_JOB = 140988404437
GEOMETRY_SHA = '774e67247d6aa0b96afb882f4080659fdfcdb991ca66ca18750c7b1be5982408'
SOURCE_ERRORS = ('centerline', 'negative_collar', 'caps_and_shoulders', 'material_coordinates',
                 'phase_and_cell_remainder', 'physical_reconstruction', 'rounding')


def digest(value):
    return isinstance(value,str) and len(value)==64 and all(c in '0123456789abcdef' for c in value)


def rational(x):
    if isinstance(x,float):
        raise ValueError('Use enclosing rational strings for cell and error bounds')
    return F(x)


def upper(x):
    x=rational(x)
    if x<0:
        raise ValueError('Upper bound must be nonnegative')
    return x


def sqrt_bounds(value):
    if value<0:
        raise ValueError('Negative squared norm')
    den=1<<160
    k=isqrt(value.numerator*den*den//value.denominator)
    return F(k,den),F(k+1,den)


def vnorm(v):
    return sqrt_bounds(sum(x*x for x in v))[1] if any(v) else F(0)


def control_norm(phase):
    return max(sum(vnorm(v) for v in phase[j:j+5]) for j in range(0,25,5))


def source_directional(phase):
    up=F(3,1000)
    zlo,zhi=sqrt_bounds(1-2*up**2)
    best=F(0)
    for xsign in (-1,1):
        proj=[]
        for x,y,z in phase:
            az=sorted((z*zlo,z*zhi))
            d=up*(xsign*x+y)
            proj.append((d+az[0],d+az[1]))
        for j in range(0,25,5):
            val=proj[j][1]
            for k in (1,3):
                a,b=(max(map(abs,proj[j+k+i])) for i in (0,1))
                val+=vnorm([a,b])
            best=max(best,val)
    return best


def unpack(actual):
    if actual['parameter_shape']!=[4,25,3] or actual['phases']!=[0.,.3,.65,1.]:
        raise ValueError('Different R688 material/phase or coefficient layout')
    params=actual['parameters']
    if len(params)!=4 or any(len(p)!=25 or any(len(v)!=3 for v in p) for p in params):
        raise ValueError('Truncated phase or Cartesian coefficients')
    data=[float(x) for p in params for v in p for x in v]
    if not all(map(isfinite,data)):
        raise ValueError('Nonfinite actual coefficient')
    sha=hashlib.sha256(struct.pack('<'+'d'*len(data),*data)).hexdigest()
    if sha!=actual['packed_le_float64_sha256']:
        raise ValueError('The actual source parameter identity differs')
    return sha,[[[F.from_float(float(x)) for x in v] for v in p] for p in params]


def partition(seq):
    out=list(map(rational,seq))
    if len(out)<2 or out[0]!=0 or out[-1]!=1 or any(b<=a for a,b in zip(out,out[1:])):
        raise ValueError('Material and phase cells must cover the full normalized interval')
    return out


def consume(literal_final,origin,receipt):
    """All scientific bounds are conditional on the corresponding proof receipts."""
    if (os.environ.get('GITHUB_ACTIONS')!='true'
            or os.environ.get('GITHUB_REPOSITORY','').lower()!='rogerhu12/math-research-public'
            or not os.environ.get('GITHUB_RUN_ID','').isdigit()):
        raise RuntimeError('Public Actions only')
    if type(literal_final) is not bytes:
        raise TypeError('The literal R688_FINAL JSON payload must be supplied as bytes')
    exact=hashlib.sha256(literal_final).hexdigest()
    if (str(origin.get('repository','')).lower()!='rogerhu12/math-research-public'
            or origin.get('natural_success') is not True or origin.get('terminal_tag')!='R688_FINAL'
            or origin.get('source_commit')!=ACTUAL_SOURCE_COMMIT or origin.get('run_id')!=ACTUAL_RUN
            or origin.get('job_id')!=ACTUAL_JOB or origin.get('request_sha256')!=ACTUAL_REQUEST_SHA
            or origin.get('literal_final_sha256')!=exact):
        raise ValueError('Actual public R688 terminal origin differs')
    actual=json.loads(literal_final)
    qsha,q=unpack(actual)
    if (receipt['q_sha256']!=qsha or receipt['geometry_sha256']!=GEOMETRY_SHA
            or receipt['original_public_request_sha256']!=ACTUAL_REQUEST_SHA
            or receipt['original_public_final_payload_sha256']!=exact
            or receipt['public_actions_run_id']!=ACTUAL_RUN or receipt['public_actions_job_id']!=ACTUAL_JOB):
        raise ValueError('Different actual public R688 field or run/job binding')
    src=control_norm(q[0]); rho=source_directional(q[0])
    deriv=F(0)
    for j,mult in enumerate((6,3,3,6)):
        change=[[mult*(b-a) for a,b in zip(v,w)] for v,w in zip(q[0][5*j:5*j+5],q[0][5*j+5:5*j+10])]
        deriv=max(deriv,sum(vnorm(v) for v in change))
    amp=[F(0)]+[control_norm(p) for p in q[1:]]
    phases=[F(0),F(3,10),F(13,20),F(1)]
    binary_phases=[F.from_float(float(v)) for v in actual['phases']]
    t=partition(receipt['normalized_radial_cuts'])
    theta=partition(receipt['angular_turn_cuts'])
    phase=partition(receipt['phase_cuts'])
    cells=receipt['phase_angle_radial_cells']
    if len(cells)!=len(phase)-1:
        raise ValueError('Missing phase slab')
    delta=src
    for lo,hi,slab in zip(phase,phase[1:],cells):
        if len(slab)!=len(theta)-1:
            raise ValueError('Missing periodic angular arc')
        rotation=max(max(amp[j],amp[j+1]) for knots in (phases,binary_phases) for j in range(3)
                     if knots[j]<hi and knots[j+1]>lo)
        for ray in slab:
            if len(ray)!=len(t)-1:
                raise ValueError('Missing radial segment on a real material ray')
            pieces=[]; weights=[]
            for u,v,cell in zip(t,t[1:],ray):
                if not digest(cell['outward_bound_proof_sha256']):
                    raise ValueError('Unbound material cell')
                if cell['method']=='direct_integrand':
                    bound=upper(cell['integrand_upper'])
                elif cell['method']=='actual_source_and_frame':
                    bound=(upper(cell['uncorrected_anchor_integrand_upper'])
                           +upper(cell['free_envelope_u_derivative_upper'])*src
                           +upper(cell['spline_parameter_u_derivative_upper'])*deriv
                           +min(2,rotation)*upper(cell['physical_seed_u_derivative_upper']))
                else:
                    raise ValueError('Unknown cell enclosure')
                wl,wr=map(rational,cell['two_port_weight_interval'])
                if not 0<=wl<=wr<=1:
                    raise ValueError('Invalid reconstruction weight')
                pieces.append((v-u)*bound); weights.append((wl,wr))
            prefix=F(0); remaining=sum(pieces)
            for piece,ws in zip(pieces,weights):
                prefix+=piece
                delta=max(delta,*[(1-w)*prefix+w*remaining for w in ws])
                remaining-=piece
    error=receipt['uniform_position_errors']
    if set(error)!=set(SOURCE_ERRORS):
        raise ValueError('All original, phase and reconstruction contributions are required')
    e=F(0)
    for key in SOURCE_ERRORS:
        rec=error[key]
        if not digest(rec['proof_sha256']) or rec['status'] not in ('outward_enclosure','exact_identity'):
            raise ValueError('Unqualified source error: '+key)
        e+=upper(rec['upper'])
    D=F(3012,1000)+2*(delta+e)
    motion=F(14299,10000)-F(374,1000)-rho-2*e
    grip=F(80,100)-2*e
    sufficient=rho+F(3,5)*delta+F(13,5)*e<=F(1522,10000)
    return dict(actual_q_sha256=qsha,public_actions_run_id=ACTUAL_RUN,public_actions_job_id=ACTUAL_JOB,
                actual_source_commit=ACTUAL_SOURCE_COMMIT,original_request_sha256=ACTUAL_REQUEST_SHA,
                original_literal_final_sha256=exact,
                source_upward_change_upper=str(rho),all_phase_design_position_change_upper=str(delta),
                supplied_continuous_source_error_upper=str(e),all_phase_diameter_upper=str(D),
                held_endpoint_separation_lower=str(motion),fixed_grip_diameter_lower=str(grip),
                displayed_sufficient_condition_met=sufficient,
                macro_ratios_follow_if_all_supplied_enclosures_hold=(motion>=F(3,10)*D and grip>=F(1,5)*D),
                independently_validated_input_proofs=False,metric_and_reach_qualification=False)
