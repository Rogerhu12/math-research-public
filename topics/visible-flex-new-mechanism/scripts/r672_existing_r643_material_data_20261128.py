"""Lift the actual R643 accepted body's existing radial quantities without constructing a field or root."""
from fractions import Fraction
from decimal import Decimal
from pathlib import Path
import json

import r668_r643_natural_source_progress_20261128 as funding
import r672_material_angular_ring_20261128 as alg

I,rat=alg.I,alg.rat
germ=funding.germ


for module,expected in ((funding,'ca423eec84490d0da2dd21ddcd1cdc02ca245f6f32a230d44873d2dd024fe8ff'),
                        (alg,'b9ecd35a2ea11fca1a9c2b670f95bafb7b7749750ec06757bad2211bd03bec82')):
    if germ.sha(Path(module.__file__).read_bytes())!=expected:
        raise ValueError('different same-field source or continuous angular calculus')


def val(x):
    return I(float(x))


def hull(a,b):
    return alg.iv.hull(a,b)


def identity(run):
    q=run.response
    if run.tail is None or run.current is None or run.tail.joint is not run.model:
        raise ValueError('the existing accepted R643 field is required')
    data,state=run.current
    run.model._require(q,data,state)
    c=funding.proof.old.germ.actual_tail_component(run.tail,q,run.accepted_tail)
    if c['actual_response_sha256']!=state['response_sha256'] or run.model.nq!=1566:
        raise ValueError('different accepted current q or model')
    return {'target':c['same_target_sha256'],'model':c['joint_model_sha256'],
            'q':c['actual_response_sha256'],'paid_tail':c['consumed_R643_tail_receipt_sha256'],
            'contract':c['source_contract_sha256'],'radial_grid':state['radial_grid_sha256'],
            'angular_grid':state['theta_grid_sha256']}


def paid_grid(run):
    origin=identity(run)
    data,state=run.current
    eta=float(state['conditional_eta_identity_observation'])
    gaps=[(Fraction.from_float(float(b))-Fraction.from_float(float(a)),i)
          for i,(a,b) in enumerate(zip(data['r'][:-1],data['r'][1:]))]
    gap,i=max(gaps)
    return {'origin':origin,'radial_nodes':len(data['r']),'angles':len(data['theta']),
            'canonical_mean_angles':len(data['fixed_mean_data']['theta']),'all_columns':run.model.nq,
            'sample_eta':eta,'remaining_endpoint_plus_material_radius':rat('1e-6')-val(eta),
            'domain':[float(data['r'][0]),float(data['r'][-1])],
            'largest_paid_material_r_gap_exact':str(gap),'largest_gap_edge_index':i,
            'largest_gap_endpoints_hex':[float(v).hex() for v in data['r'][i:i+2]],
            'all_original_source_rows':run.tail.contract['source_error_accounting'],
            'point_observation_only':True}


def paid_corner(run,i,j):
    data,state=run.current
    pos=state['positions'][i]
    row=state['output_states'][i]
    t=[val(x) for x in pos['T'][j]]
    S=[val(x) for x in pos['S'][j]]
    E=val(row['E'])
    ref=[val(x)/alg.iv.iv.sqrt_i(E) for x in pos['pred'][j]]
    d=sum((2*x*y+y**2 for x,y in zip(ref,S)),I(0))
    f=val(row['b'][j])/val(data['r'][i])*sum((x*y for x,y in zip(t,S)),I(0))
    return {'d':d,'f':f,'legacy_eta':float(pos['eta'][j]),
            'r_hex':float(data['r'][i]).hex(),'theta_hex':float(data['theta'][j]).hex()}


def source_node(run,i):
    origin=identity(run)
    data,state=run.current
    model=run.tail.model
    old=model.old
    paid=old.old
    j4=(2,4,6,8)
    modes=tuple(range(2,97,2))
    if (len(model.core_modes)!=48 or tuple(map(int,model.core_modes))!=modes
            or old.nq!=1130 or len(old.column_modes)!=1129 or model.J!=48 or run.model.mean_count!=94):
        raise ValueError('all original, independent and dependent modes must match the actual layout')
    amp=val(model.amplitude)
    pre={j:[I(0) for _ in range(3)] for j in j4}
    post={j:[I(0) for _ in range(3)] for j in modes}
    def add(dst,j,col,c):
        if len(col)!=3:
            raise ValueError('paid value and two radial derivatives required')
        dst[j]=[v+val(x)*c for v,x in zip(dst[j],col)]
    for h,j in enumerate(j4):
        add(pre,j,data['fields'][i,h],amp*(I(1) if h==0 else val(old.paidq[h])))
        for k in range(paid.nb):
            add(pre,j,data['bulk'][i,k],amp*val(old.paidq[4+h*paid.nb+k]))
    add(post,4,data['forced_j4'][i],amp**2*val(old.paidq[paid.original_nq]))
    z=state['angular_response']
    for k,j in enumerate(old.column_modes):
        add(post,int(j),data['new_columns'][i,k],amp*(val(model.q_reference[k+1])+val(z[k])))
    for k,j in enumerate(model.core_modes):
        add(post,int(j),data['core_radial'][i],
            val(model.original_core_correction[k])+val(state['core']['correction_delta'][k]))
    for start,js,key in ((model.compact_start,model.extra_compact_modes,'compact_radial_dictionary'),
                         (model.tail_start,model.modes,'analytic_tail_columns')):
        cols=data[key][i]
        for a,j in enumerate(js):
            for b,v in enumerate(cols):
                add(post,int(j),v,amp*val(z[start+a*len(cols)+b]))
    for k,j in enumerate(model.core_free_modes):
        add(post,int(j),data['new_core_lift'][i],amp*val(z[model.core_start+k]))
    mean_key=(data['r'].tobytes(),float(model.amplitude))
    if mean_key not in old.canonical_mean_cache:
        raise LookupError('paid fixed512 radial canonical mean table absent; no old evaluation restarted')
    canonical=old.canonical_mean_cache[mean_key][i]
    seed=state['mean_seed_states'][i]
    target=seed['target']
    if target['target_sha256']!=origin['target']:
        raise ValueError('paid fixed-seed target differs')
    W,Wr=val(target['W']),val(target['W_r'])
    x=rat(Decimal(seed['x_decimal']))
    if seed['chart']=='lambda':
        slope=W*x
    elif seed['chart']=='zeta':
        slope=x/W
    else:
        raise ValueError('wrong fixed seed chart')
    split=target['split_reference']
    sc=W**2 if split['normalization']=='W_squared' else I(1)
    E=1+W**2+sc*(rat(Decimal(split['centre_decimal']))+rat(Decimal(split['offset_decimal'])))
    Er=2*W*Wr+rat(Decimal(split['e_r_decimal']))
    m=state['mean_change'][i]
    return {'origin':origin,'node_index':i,'r':val(data['r'][i]),'E':E,'Er':Er,
            'pre':pre,'post':post,'base':[-W+slope+val(m[1])-val(canonical[1]),
                -Wr+rat(Decimal(seed['s_r_decimal']))+val(m[2])-val(canonical[2])],
            'canonical_fixed_512_paid_radial_means':[val(x) for x in canonical],
            'all_94_mean_coordinates_used_in_paid_mean_change':True}


def flat_fields(radial):
    fields={k:radial[k] for k in ('E','Er','Err') if k in radial}
    for k,v in enumerate(radial['base'],1):
        fields['base/'+str(k)]=v
    for key in ('pre','post'):
        for j,vector in radial[key].items():
            for k,v in enumerate(vector):
                fields[f'{key}/{j}/{k}']=v
    return fields


def assemble(fields,r,third):
    n=4 if third else 3
    d={k:fields[k] for k in (('E','Er','Err') if third else ('E','Er'))}
    d['r']=r
    d['base']=[fields['base/'+str(k)] for k in range(1,n)]
    for key,modes in [('pre',(2,4,6,8)),('post',range(2,97,2))]:
        d[key]={j:[fields[f'{key}/{j}/{k}'] for k in range(n)] for j in modes}
    return d


def radial_cell(left,right,*,radial_remainders,source_certificates,third_endpoint_columns=None,fractions=(0,1)):
    """Enclose every actual radial coefficient on a whole cell; omitted evidence stays explicit.

    radial_remainders enclose interpolation departure of the nominal radial source from its two
    endpoint values. Each seven-source map encloses its own telescoping difference; a bound
    may be positive at both exact and floating endpoints. All supplied radii use exact fractions.
    """
    if (left['origin']!=right['origin'] or right['node_index']-left['node_index'] not in (0,1)
            or left['r'].lo>right['r'].lo):
        raise ValueError('same accepted adjacent material endpoints required')
    label={'origin':left['origin'],'r_hex':[left['r'].lo.hex(),right['r'].lo.hex()]}
    parent_label=dict(label)
    lo,hi=map(Fraction,fractions)
    if not 0<=lo<hi<=1 or (left['node_index']==right['node_index'] and (lo,hi)!=(0,1)):
        raise ValueError('invalid fractional subdivision of the authentic material edge')
    if (lo,hi)!=(0,1):
        label['cell_fraction']=[str(lo),str(hi)]
    a,b=flat_fields(left),flat_fields(right)
    if a.keys()!=b.keys():
        raise ValueError('source endpoint columns differ')
    if third_endpoint_columns is not None:
        if third_endpoint_columns.get('material')!=parent_label or not third_endpoint_columns.get('evidence_sha256'):
            raise ValueError('true third coefficients must identify this actual material cell')
        third=third_endpoint_columns['values']
        expected={'Err','base/3'}|{f'{key}/{j}/3' for key,js in [('pre',(2,4,6,8)),('post',range(2,97,2))] for j in js}
        if set(third)!=expected:
            raise ValueError('all original third derivatives, correct forced j4 and mean required')
        text=third_endpoint_columns.get('literal_evidence')
        if not isinstance(text,str) or germ.sha(text.encode())!=third_endpoint_columns['evidence_sha256']:
            raise ValueError('actual third endpoint proof literal is missing')
        ev=json.loads(text)
        encoded={k:[[i.lo.hex(),i.hi.hex()] for i in pair] for k,pair in third.items()}
        if ev.get('material')!=parent_label or ev.get('third_endpoint_intervals_hex')!=encoded:
            raise ValueError('different third endpoint columns in the bound evidence')
        for k,(v,w) in third.items():
            a[k],b[k]=v,w
    def segment(x,y):
        if (lo,hi)==(0,1):
            return hull(x,y)
        return hull(x*rat(1-lo)+y*rat(lo),x*rat(1-hi)+y*rat(hi))
    values={k:segment(a[k],b[k]) for k in a}
    summaries={}
    missing=[]
    def include(name,row):
        if row is None:
            missing.append(name)
            return
        if row.get('material')!=label or not row.get('evidence_sha256') or row.get('kind')!=name:
            raise ValueError('source interval provenance or named source differs')
        if row.get('proved_scope')!='all_listed_coefficients_on_entire_closed_material_cell':
            missing.append(name)
            return
        # A checksum of the actual reviewable witness is required. This is still an
        # implication conditional on the truth of the mathematical witness supplied.
        witness=row.get('literal_evidence')
        if not isinstance(witness,str) or germ.sha(witness.encode())!=row['evidence_sha256']:
            raise ValueError('missing or inconsistent literal source certificate')
        if row.get('relative_to')!='preceding_telescoping_realization' and name!='nominal_radial_interpolation':
            raise ValueError('source rows must bound successive same-field realizations')
        radii=row['absolute_radii']
        ev=json.loads(witness)
        if any(ev.get(k)!=row.get(k) for k in ('material','kind','proved_scope','absolute_radii','relative_to')):
            raise ValueError('numeric coefficient bounds differ from their literal evidence')
        summary={}
        if set(radii)!=set(values):
            raise ValueError('a missing coefficient cannot be silently assigned zero')
        for key,radius in radii.items():
            if type(radius) not in (str,int) or Fraction(radius)<0:
                raise ValueError('proved rational nonnegative coefficient radius required')
            bnd=rat(radius).hi
            values[key]=values[key]+I(-bnd,bnd)
            pieces=key.split('/')
            group='/'.join([pieces[0],pieces[-1]]) if len(pieces)==3 else key
            summary[group]=max(summary.get(group,Fraction(0)),Fraction(radius))
        summaries[name]={k:str(v) for k,v in summary.items()}
    if left['node_index']!=right['node_index']:
        include('nominal_radial_interpolation',radial_remainders)
    if set(source_certificates)-set(funding.ROWS):
        raise ValueError('unrecognized source row')
    for name in funding.ROWS:
        include(name,source_certificates.get(name))
    return {'material':label,'radial':assemble(values,segment(left['r'],right['r']),third_endpoint_columns is not None),
            'unresolved_errors':missing,'maximum_paid_input_radii_by_source_family_and_radial_order':summaries,'source_evidence_sha256':{k:v.get('evidence_sha256') for k,v in source_certificates.items() if v is not None},
            'radial_evidence_sha256':None if radial_remainders is None else radial_remainders.get('evidence_sha256'),
            'third_endpoint_evidence_sha256':None if third_endpoint_columns is None else third_endpoint_columns['evidence_sha256']}
