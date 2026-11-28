"""Initial Cauchy balls and literal realization for the existing R643 source. No ODE or root."""
import ast
from decimal import Decimal
from fractions import Fraction
from pathlib import Path
import json

import r663_actual_dense_denominator_20261128 as proof

iv=proof.coef
I, rat, mag=iv.I,iv.rat,iv.mag


def weight(a,s,mu):
    u=a+s
    ar,r=iv.RC+iv.ELL/a,iv.RC+iv.ELL/u
    return (a/u)**2*iv.exp((2*mu-2)*iv.log(r/ar)+a*(2-iv.sin(a))-u*(2-iv.sin(u)))


def moments(a,mu,left,right):
    s=I(left,right)
    u=a+s
    v=iv.RC/(iv.RC*u+iv.ELL)
    w=weight(a,s,mu)
    d1=-2*mu/u+(2*mu-2)*v-2+iv.sin(u)+u*iv.cos(u)
    d2=2*mu/u**2-(2*mu-2)*v**2+2*iv.cos(u)-u*iv.sin(u)
    d3=-4*mu/u**3+2*(2*mu-2)*v**3-3*iv.sin(u)-u*iv.cos(u)
    d4=12*mu/u**4-6*(2*mu-2)*v**4-4*iv.cos(u)+u*iv.sin(u)
    f2=w*(d1**2+d2)
    f3=w*(d1**3+3*d1*d2+d3)
    f4=w*(d1**4+6*d1**2*d2+3*d2**2+4*d1*d3+d4)
    m=(left+right)/2
    weights=[weight(a,I(x),mu) for x in (left,m,right)]
    h=I(right)-left
    result=[]
    for order,derivative in [(0,f4),(2,s**2*f4+8*s*f3+12*f2)]:
        x,y,z=[v*I(q)**order for v,q in zip(weights,(left,m,right))]
        estimate=h*(x+4*y+z)/6
        error=(h**5*mag(derivative)/2880).hi
        result.append(estimate+I(-error,error))
    return result


def initial_ball(flat,j,cursor):
    """Yield between panel evaluations; return one real ball after the entire first window."""
    alpha=float(flat.alpha)
    zhat=float(flat.finite_inner_data['z_alpha_first'])
    a,delta=iv.seed_alpha(alpha,j*j)
    mu=j*j
    if cursor:
        if (cursor['mode'],cursor['alpha'],cursor['paid_z'])!=(j,alpha.hex(),zhat.hex()):
            raise ValueError('different real paid peak while restoring the initial window')
        acc=[I(*v) for v in cursor['sum']]
        pending=list(cursor['pending'])
        tried,accepted=cursor['examined'],cursor['accepted']
    else:
        acc=[I(0),I(0)]
        pending=[(0.,1.,0)]
        tried=accepted=0
    while pending:
        left,right,depth=pending.pop()
        pair=moments(a,mu,left,right)
        tried+=1
        if max((I(v.hi)-v.lo).hi for v in pair)>2e-7*(right-left) and depth<13:
            mid=(left+right)/2
            pending.extend([(mid,right,depth+1),(left,mid,depth+1)])
        else:
            acc=[v+w for v,w in zip(acc,pair)]
            accepted+=1
        cursor.update(mode=j,alpha=alpha.hex(),paid_z=zhat.hex(),pending=list(pending),
                      sum=[[v.lo,v.hi] for v in acc],examined=tried,accepted=accepted)
        yield
    eps=iv.flat_parts(a,mu)[1]
    z=I((acc[0]-rat('1e-14')).lo,(acc[0]+rat('25/24')*eps*acc[1]+rat('1e-14')).hi)
    return {'mode':j,'paid_alpha_hex':alpha.hex(),'paid_z_hex':zhat.hex(),'alpha_radius':delta,
            'finite_z_at_exact_alpha':[z.lo,z.hi],'paid_z_absolute_error_upper':mag(z-zhat),
            'J':[acc[0].lo,acc[0].hi],'J_second_moment':[acc[1].lo,acc[1].hi],
            'examined_Simpson_panels':tried,'accepted_Simpson_panels':accepted}


def qtext(q):
    return str(q.numerator)+'/'+str(q.denominator)


def literal_vector(raw,observed):
    values=json.loads(raw,parse_float=Decimal)
    if [float(x) for x in values]!=list(map(float,observed)):
        raise ValueError('live vector and its bound source literal differ')
    ds=[abs(Fraction(x)-Fraction.from_float(float(y))) for x,y in zip(values,observed)]
    largest=max(range(len(ds)),key=ds.__getitem__)
    return {'count':len(ds),'literal_sha256':proof.old.germ.sha(raw.encode()),'largest_index':largest,
            'absolute_error_linf_exact':qtext(ds[largest]),'absolute_error_l1_exact':qtext(sum(ds)),
            'nonzero_literal_to_binary64_differences':sum(x!=0 for x in ds)}


def literals(tail,response):
    model=tail.model
    paid=model.old.old
    weak=model.driver.weak
    definition=json.loads(proof.old.germ.DEFINITION.read_bytes())
    path=Path(weak.__file__)
    source=path.read_bytes()
    frozen=[v for k,v in definition['all_source_sha256'].items() if k.endswith('/'+path.name)]
    if (frozen!=[proof.old.germ.sha(source)] or proof.old.germ.sha(weak.RAW_Q_JSON.encode())!=weak.SOURCE_Q_SHA
            or proof.old.germ.sha(weak.RAW_KNOT_JSON.encode())!=weak.SOURCE_KNOT_SHA):
        raise ValueError('force scale, paid q or knots changed source')
    text=source.decode()
    assignments=[n for n in ast.parse(text).body if isinstance(n,ast.Assign)
                 and any(isinstance(k,ast.Name) and k.id=='PAID_FORCE_NORMALIZATION' for k in n.targets)]
    if len(assignments)!=1:
        raise ValueError('expected one literal forced scale')
    literal=ast.get_source_segment(text,assignments[0].value)
    exact=Fraction(literal)
    scale=float(paid.forced.scale)
    if exact!=Fraction('16533.1541790287') or scale!=float(exact):
        raise ValueError('different fixed force scale')
    force={'exact_decimal':literal,'paid_binary64_hex':scale.hex(),
           'absolute_rounding_error_exact':qtext(abs(exact-Fraction.from_float(scale))),
           'exact_inverse':qtext(1/exact)}
    ref=literal_vector(model.original_q_json,model.q_reference)
    if ref['literal_sha256']!=definition['actual_accepted_q_sha256']:
        raise ValueError('different actual reference vector literal')
    def canonical_array(x):
        return json.dumps(x.tolist(),separators=(',',':'),allow_nan=False)
    return {'original_265q':literal_vector(weak.RAW_Q_JSON,model.old.paidq),
            'all_67_knots':literal_vector(weak.RAW_KNOT_JSON,paid.bs.t),'actual_reference_1130q':ref,
            'actual_fixed_seed':literal_vector(canonical_array(tail.joint.seed_response),tail.joint.seed_response),
            'current_1566q_canonical_display':literal_vector(canonical_array(response),response),
            'original_frozen_force_scale':force}


def envelope_geometry(tail):
    p=tail.model.old.old
    if len(p.mode_height_scales)!=4 or tuple(int(m.mode) for m in p.modes[:4])!=(2,4,6,8):
        raise ValueError('four original envelope columns required')
    # R576 uses the first point of R - geomspace(1e-7,.03,33).
    # The interval below covers decimal and binary representations and the rim subtraction.
    at=I(rat('.9e-7').lo,rat('1.1e-7').hi)
    x=iv.power(at/iv.D,9,20)
    if x.lo<=rat('1/2000').hi or x.hi>=rat('1/1000').lo:
        raise ArithmeticError('outer normalization node leaves the proved core window')
    # 1/2000 is not exactly representable; use its true outward lower endpoint.
    lower=(rat('3/4')*3*rat('11/9')**2*rat('9/31')*iv.power(rat('1/2000'),31,9)).lo
    upper=(4+iv.power(iv.R-iv.RC,31,10)).hi
    return {'first_four_mode_height_scale_strict_lower':lower,
            'raw_envelope_scale_strict_lower':1,'raw_envelope_scale_upper':upper,
            'actual_observed_mode_scales_hex':[float(v).hex() for v in p.mode_height_scales],
            'actual_observed_envelope_scale_hex':float(p.envelope_scale).hex(),
            'envelope_scale_absolute_error_upper':max(mag(I(1)-float(p.envelope_scale)),
                                                       mag(I(upper)-float(p.envelope_scale))),
            'maximum_operator':'same finite source-defined normal_nodes; all four true field maxima',
            'original_mode_upper_and_tight_normalization_errors_still_open':True}


def root_observations(tail):
    def group(records):
        largest=None
        count=0
        missing=0
        for r,item in records.items():
            root=item.get('root_receipt',{})
            if 'residual_decimal' not in root:
                missing+=1
                continue
            value=abs(Decimal(root['residual_decimal']))
            count+=1
            if largest is None or value>largest[0]:
                largest=(value,{'r_hex':float(r).hex(),'root_coordinate_decimal':root.get('returned_coordinate_decimal'),
                                'observed_residual_decimal':str(value),
                                'observed_derivative_decimal':root.get('derivative_decimal'),
                                'chart':item.get('chart')})
        return {'recorded_points':count,'other_paid_root_receipt_forms':missing,
                'largest_observed_absolute_residual':None if largest is None else largest[1]}
    return {'same_accepted_reference':group(tail.joint.owned.target_cache),
            'same_fixed_seed':group(tail.joint.seed_mean_cache),
            'interval_angular_residual_and_uniform_derivative_lower_still_required':True}
