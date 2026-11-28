"""Exact Bernstein ranges for actual compact responses and their decimal-to-binary realization."""
import ast
from decimal import Decimal
from fractions import Fraction as Q
from functools import lru_cache
from math import comb
from pathlib import Path
import json

import r672_existing_r643_material_data_20261128 as original


if original.germ.sha(Path(original.__file__).read_bytes())!='8ed67dd778712d0d62fd568a3500ac8405fb2b2532e2c3ccaabf925cbb051a35':
    raise ValueError('different actual source-material layout')


def binary(v):
    return Q.from_float(float(v))


def plus(a,b):
    return [x+y for x,y in zip(a,b)]


def linear_times(p,a,b):
    return [a*x+y*b for x,y in zip(list(p)+[0],[0]+list(p))]


def basis_polynomial(nodes,left,right):
    """Exact restricted polynomial of one degree-five basis with its seven local knots."""
    m=(left+right)/2
    @lru_cache(None)
    def build(i,k):
        if not k:
            return (Q(int(nodes[i]<=m<nodes[i+1])),)
        p=[Q(0)]*(k+1)
        if nodes[i+k]!=nodes[i]:
            d=nodes[i+k]-nodes[i]
            p=plus(p,linear_times(build(i,k-1),(left-nodes[i])/d,(right-left)/d))
        if nodes[i+k+1]!=nodes[i+1]:
            d=nodes[i+k+1]-nodes[i+1]
            p=plus(p,linear_times(build(i+1,k-1),(nodes[i+k+1]-left)/d,(left-right)/d))
        return tuple(p)
    return build(0,5)


def bernstein_jet(p,width,order):
    p=list(p)
    out=[]
    for _ in range(order+1):
        d=len(p)-1
        b=[sum((p[k]*Q(comb(i,k),comb(d,k)) for k in range(i+1)),Q(0)) for i in range(d+1)]
        out.append([min(b),max(b)])
        p=[k*p[k]/width for k in range(1,len(p))]
    return out


def literal_patches(module,definition):
    source=Path(module.__file__).read_bytes()
    sha=original.germ.sha(source)
    if [v for k,v in definition['all_source_sha256'].items() if k.endswith('/'+Path(module.__file__).name)]!=[sha]:
        raise ValueError('different original compact quintic source')
    tree=ast.parse(source)
    node=next(x.value for x in tree.body if isinstance(x,ast.Assign)
              and any(isinstance(n,ast.Name) and n.id=='PATCH_KNOTS' for n in x.targets))
    text=source.decode()
    exact=[[Q(ast.get_source_segment(text,atom)) for atom in call.args[0].elts] for call in node.elts]
    if [list(map(float,x)) for x in exact]!=[list(map(float,x)) for x in module.PATCH_KNOTS]:
        raise ValueError('paid patch knots differ from their original literal source')
    return [tuple(p[i:i+7]) for p in exact for i in range(len(p)-6)]


def compact_piece(run,left,right):
    """All 24 post angular rows and the independent mean row on one *real* paid radial gap.

    Each output is the actual function restricted to that gap. Its difference entry compares
    exact source literals and exact binary64 inputs before any arithmetic at evaluation.
    """
    origin=original.identity(run)
    data,_=run.current
    a,b=binary(data['r'][left]),binary(data['r'][right])
    if right!=left+1 or not a<b:
        raise ValueError('a complete neighboring material gap is required')
    mod=run.tail.model
    definition=json.loads(original.germ.DEFINITION.read_bytes())
    knots=literal_patches(mod.compact,definition)
    if len(knots)!=28 or mod.compact.OLD_NQ!=682 or tuple(map(int,mod.extra_compact_modes))!=tuple(range(34,49,2)):
        raise ValueError('unexpected actual finite compact dictionary')
    stored=[(binary(l),binary(r)) for l,r,_ in mod.old.compact_splines]
    knums=[tuple(binary(v) for v in z) for z in knots]
    if stored!=[(z[0],z[-1]) for z in knums]:
        raise ValueError('different live compact support endpoints')
    ref=[Q(x) for x in json.loads(mod.original_q_json,parse_float=Decimal)]
    q=[Q(str(float(x))) for x in run.response]
    def coefficients(j):
        if j==0:
            first=run.model.mean_start+61
            return [(q[first+k],binary(run.response[first+k])) for k in range(28)]
        if j<=32:
            off=mod.compact.OLD_NQ+(j//2-1)*28
            return [(ref[off+k]+q[off-1+k],binary(mod.q_reference[off+k])+binary(run.response[off-1+k])) for k in range(28)]
        off=mod.compact_start+(j//2-17)*28
        return [(q[off+k],binary(run.response[off+k])) for k in range(28)]
    coeff={j:coefficients(j) for j in range(0,49,2)}
    cuts=sorted({a,b}|{v for z in knots+knums for v in z if a<v<b})
    results={}
    for l,r in zip(cuts,cuts[1:]):
        P=[basis_polynomial(t,l,r) for t in knots]
        Ph=[basis_polynomial(t,l,r) for t in knums]
        for j,col in coeff.items():
            exact=[sum((x*p[k] for (x,_),p in zip(col,P)),Q(0))/100000 for k in range(6)]
            actual=[sum((y*p[k] for (_,y),p in zip(col,Ph)),Q(0))*binary(mod.amplitude) for k in range(6)]
            # Also allow the actual full response coordinates to have their precise binary64
            # interpretation while the frozen reference and patch locations are exact decimals.
            if j<=32 and j!=0:
                off=mod.compact.OLD_NQ+(j//2-1)*28
                mixed=[ref[off+k]+binary(run.response[off-1+k]) for k in range(28)]
            else:
                mixed=[y for _,y in col]
            mixed=[sum((x*p[k] for x,p in zip(mixed,P)),Q(0))/100000 for k in range(6)]
            for label,polys in [('exact_field',[exact,mixed]),('literal_minus_binary',[plus(u,[-x for x in actual]) for u in (exact,mixed)])]:
                for p in polys:
                    jets=bernstein_jet(p,r-l,3)
                    key=(j,label)
                    if key in results:
                        jets=[[min(x[0],y[0]),max(x[1],y[1])] for x,y in zip(jets,results[key])]
                    results[key]=jets
    return {'origin':origin,'r_hex':[float(a).hex(),float(b).hex()],'knot_union_spans':len(cuts)-1,
            'actual_28_quintic_columns_per_mode':28,'all_post_modes_and_independent_mean':list(coeff),
            'exact_material_derivatives_0to3':{str(j):{k:[[str(a),str(b)] for a,b in results[j,k]]
                for k in ('exact_field','literal_minus_binary')} for j in coeff},
            'paid_mode_height_forced_noncompact_bulk_core_and_angular_evaluation_errors_still_separate':True}


def bare_bulk_basis(run,left,right):
    """Original 61 exact quintics, before their actual cutoff, rim power, and mean trace subtraction."""
    origin=original.identity(run)
    model=run.tail.model
    data,_=run.current
    a,b=binary(data['r'][left]),binary(data['r'][right])
    weak=model.driver.weak
    if right!=left+1 or not a<b or original.germ.sha(weak.RAW_KNOT_JSON.encode())!=weak.SOURCE_KNOT_SHA:
        raise ValueError('different material gap or source knots')
    knots=[Q(v) for v in json.loads(weak.RAW_KNOT_JSON,parse_float=Decimal)]
    actual=list(map(binary,model.old.bs.t))
    if list(map(float,knots))!=list(map(float,actual)) or len(knots)-6!=61:
        raise ValueError('different live 61-column quintic basis')
    cuts=sorted({a,b}|{x for x in knots+actual if a<x<b})
    out={}
    for i in range(61):
        bounds=None
        for l,r in zip(cuts,cuts[1:]):
            p=basis_polynomial(tuple(knots[i:i+7]),l,r)
            ph=basis_polynomial(tuple(actual[i:i+7]),l,r)
            jets=bernstein_jet(p,r-l,3)+bernstein_jet(plus(p,[-v for v in ph]),r-l,3)
            bounds=jets if bounds is None else [[min(x[0],y[0]),max(x[1],y[1])] for x,y in zip(bounds,jets)]
        out[str(i)]={'exact_0to3':[[str(a),str(b)] for a,b in bounds[:4]],
                     'knot_realization_difference_0to3':[[str(a),str(b)] for a,b in bounds[4:]]}
    return {'origin':origin,'r_hex':[float(a).hex(),float(b).hex()],'actual_original_61_quintics':out,
            'source_knot_sha256':weak.SOURCE_KNOT_SHA,
            'bulk_weight_envelope_and_trace_realization_still_required':True}
