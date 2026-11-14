#!/usr/bin/env python3
"""Exact nonplanarity of a shared-node C2 tail Hermite normal form.

The input retains only original four-angle node bytes. This consumer performs
the geometric arithmetic in public Actions. It constructs exact rational jets
at each shared radial node, then exact quintics, outer correction and collar.
It does not identify this exact normal form with literal rounded FFT/Hermite
coefficients of a previous renderer, nor with an exact nonlinear tail limit.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
from functools import lru_cache
import gzip
import hashlib
import json
from pathlib import Path
import struct
import time

HERE=Path(__file__).resolve().parent
ZERO=F(0)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def load_verified(root,record):
    encoded=(root/record['file']).read_bytes()
    if sha(encoded)!=record['sha256']:
        raise ValueError('Compressed packet hash differs: '+record['file'])
    raw=gzip.decompress(encoded)
    if sha(raw)!=record['raw_sha256']:
        raise ValueError('Raw packet hash differs: '+record['file'])
    return raw


def zeros():
    return [[ZERO for _ in range(3)] for _ in range(3)]


def matrix_add(a,b):
    return [[a[j][k]+b[j][k] for k in range(3)] for j in range(3)]


def matrix_sub(a,b):
    return [[a[j][k]-b[j][k] for k in range(3)] for j in range(3)]


def hermite(y0,y1,v0,v1,w0,w1,width):
    out=[zeros() for _ in range(6)]
    for j in range(3):
        for k in range(3):
            c0=y0[j][k]
            c1=width*v0[j][k]
            c2=width*width*w0[j][k]/2
            a=y1[j][k]-c0-c1-c2
            b=width*v1[j][k]-c1-2*c2
            c=width*width*w1[j][k]-2*c2
            for coefficient,value in zip(out,(c0,c1,c2,10*a-4*b+c/2,-15*a+7*b-c,6*a-3*b+c/2)):
                coefficient[j][k]=value
    return out


def evaluate(coefficients,t):
    out=zeros()
    for c in reversed(coefficients):
        out=[[out[j][k]*t+c[j][k] for k in range(3)] for j in range(3)]
    return out


def det(v):
    a,b,c=v
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
            -a[1]*(b[0]*c[2]-b[2]*c[0])
            +a[2]*(b[0]*c[1]-b[1]*c[0]))


def determinant_record(value):
    numerator,denominator=str(value.numerator),str(value.denominator)
    return dict(sign=1 if value>0 else -1 if value<0 else 0,
        numerator_bits=abs(value.numerator).bit_length(),denominator_bits=value.denominator.bit_length(),
        numerator_sha256=sha(numerator.encode()),denominator_sha256=sha(denominator.encode()))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--packet',type=Path,required=True,help='manifest.json from the lossless extractor')
    parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--target-json',type=Path,help='Optional external exact radial_difference_jets, shape 3x3x3, rational strings')
    for name in ('checkpoint','source-topic','port'):
        parser.add_argument('--'+name,type=Path)
    args=parser.parse_args()
    start=time.monotonic()
    if args.out.exists():
        raise FileExistsError('Refusing to overwrite exact-check evidence')
    manifest_bytes=args.packet.read_bytes()
    manifest=json.loads(manifest_bytes)
    if manifest.get('schema')!='original-tail-four-cardinal-byte-packet-v1' or not manifest.get('finished'):
        raise ValueError('Finished original-node cardinal byte packet required')
    root=args.packet.parent
    packed=load_verified(root,manifest['data'])
    index=json.loads(load_verified(root,manifest['source_node_index']))
    definition=manifest['definition']
    count=definition['shape'][0]
    if definition['shape']!=[count,4,12] or len(index)!=count or len(packed)!=count*384:
        raise ValueError('Cardinal packet shape or byte count differs')
    if definition['source_orientation']!='outer-to-inner':
        raise ValueError('Unexpected original node orientation')
    for i,row in enumerate(index):
        if sha(packed[i*384:(i+1)*384])!=row['four_cardinal_rows_sha256']:
            raise ValueError('Retained per-node bytes differ at '+str(i))
    radii=[F(row['radius']) for row in reversed(index)]
    if any(a>=b for a,b in zip(radii,radii[1:])):
        raise ValueError('Exact binary node radii must increase strictly')
    cuff,inner,cut,width=[F(definition[key]) for key in ('cuff','inner','cut','patch_width')]
    sigma=int(definition['sigma'])
    if sigma not in (-1,1) or radii[0]!=inner or radii[-1]!=cut or not 0<width<cut-inner or not 0<cuff<inner:
        raise ValueError('Endpoint geometry and packet radii differ')
    patch_start=cut-width  # exact endpoint identity, not a rounded subtraction
    background=[[F(-1),F(1),ZERO],[F(-2),ZERO,ZERO],[F(-1),F(-1),ZERO]]

    @lru_cache(maxsize=12)
    def raw_node(i):
        return struct.unpack_from('<48d',packed,(count-1-i)*384)

    @lru_cache(maxsize=12)
    def difference(i,start_column,components=3):
        row=raw_node(i)
        return [[F.from_float(row[(j+1)*12+start_column+k])-F.from_float(row[start_column+k])
                 for k in range(components)] for j in range(3)]

    @lru_cache(maxsize=8)
    def node_jets(i):
        position=difference(i,0)
        first=difference(i,3)
        second=zeros()
        for j in range(3):
            second[j][2]=sigma*difference(i,9,1)[j][0]
            for k in range(2):
                if i==0:
                    value=(difference(1,3)[j][k]-first[j][k])/(radii[1]-radii[0])
                elif i==count-1:
                    value=(first[j][k]-difference(i-1,3)[j][k])/(radii[i]-radii[i-1])
                else:
                    hm,hp=radii[i]-radii[i-1],radii[i+1]-radii[i]
                    value=(hp*(first[j][k]-difference(i-1,3)[j][k])/hm+
                           hm*(difference(i+1,3)[j][k]-first[j][k])/hp)/(hm+hp)
                second[j][k]=value
        position=[[position[j][k]*(sigma if k==2 else 1)+radii[i]*background[j][k]
                   for k in range(3)] for j in range(3)]
        first=[[first[j][k]*(sigma if k==2 else 1)+background[j][k]
                for k in range(3)] for j in range(3)]
        return position,first,second

    if args.target_json:
        raw=args.target_json.read_bytes();target_data=json.loads(raw)
        target=[[[F(value) for value in row] for row in order]
                for order in target_data['radial_difference_jets']]
        if len(target)!=3 or any(len(order)!=3 or any(len(row)!=3 for row in order) for order in target):
            raise ValueError('External target jets must have shape 3x3x3')
        target_info=dict(kind='external exact difference jets',sha256=sha(raw),source=target_data.get('source'))
    else:
        if any(getattr(args,key) is None for key in ('checkpoint','source_topic','port')):
            parser.error('Supply --target-json or all of --checkpoint --source-topic --port')
        from exact_20261114_refined_tail_adapter import module,prefix_cut_coefficients
        from geometry_20261114_tail_planar_germ import cardinal
        checkpoint_raw=args.checkpoint.read_bytes()
        port_raw=args.port.read_bytes()
        for key,raw in (('checkpoint',checkpoint_raw),('port',port_raw)):
            if sha(raw)!=manifest['plan_inputs'][key]['sha256']:
                raise ValueError('Prefix cut input binding differs: '+key)
        meta=json.loads(gzip.decompress(checkpoint_raw) if checkpoint_raw[:2]==b'\x1f\x8b' else checkpoint_raw)
        pb=module('exact_cardinal_prefix_loader',HERE/'geometric-checkpoint-core-pullback.py')
        saved,_=pb.load_saved(args.checkpoint,args.source_topic,args.port,angular=int(meta['config']['angular']))
        if float(saved.flow.bridge.sigma)!=sigma:
            raise ValueError('Upper reflection sign differs')
        coefficient_jets,cut_geometry=prefix_cut_coefficients(saved,0.,0.,definition['source_angles']//2)
        target=[]
        for c in coefficient_jets:
            values=cardinal(c)
            target.append([[values[j+1][k]-values[0][k] for k in range(3)] for j in range(3)])
        target_info=dict(kind='binary direct prefix Fourier radial jets, evaluated exactly at four cardinal angles',
            checkpoint_sha256=sha(checkpoint_raw),port_sha256=sha(port_raw),
            conversion_geometry=cut_geometry,common_height_means_cancel_exactly=True,
            exact_prefix_to_target_conversion_rounding_paid=False)

    outer=node_jets(count-1)
    delta=[matrix_sub(t,o) for t,o in zip(target,outer)]
    patch=hermite(zeros(),delta[0],zeros(),delta[1],zeros(),delta[2],width)
    inner_jets=node_jets(0)
    cap_position=[[cuff*v for v in row] for row in background]
    collar=hermite(cap_position,inner_jets[0],background,inner_jets[1],zeros(),inner_jets[2],inner-cuff)
    witness,failed=[],[]
    fractions=[F(0),F(1),F(1,2)]
    fractions.extend(F(j,15) for j in range(1,15) if F(j,15) not in fractions)

    def check_piece(label,lo,hi,origin,span_width,coefficients):
        for fraction in fractions:
            radius=lo+(hi-lo)*fraction
            value=evaluate(coefficients,(radius-origin)/span_width)
            if radius>=patch_start:
                value=matrix_add(value,evaluate(patch,(radius-patch_start)/width))
            determinant=det(value)
            if determinant:
                witness.append(dict(piece=label,lo=str(lo),hi=str(hi),witness_radius=str(radius),
                    witness_relative_position=str(fraction),determinant=determinant_record(determinant)))
                return
        failed.append(dict(piece=label,lo=str(lo),hi=str(hi),reason='The four-cardinal determinant polynomial is identically zero; a planar surface is not inferred.'))

    check_piece('inner-collar',cuff,inner,cuff,inner-cuff,collar)
    for i in range(count-1):
        lo,hi=radii[i],radii[i+1]
        left,right=node_jets(i),node_jets(i+1)
        coefficients=hermite(left[0],right[0],left[1],right[1],left[2],right[2],hi-lo)
        bounds=[lo]+([patch_start] if lo<patch_start<hi else [])+[hi]
        for part,(a,b) in enumerate(zip(bounds,bounds[1:])):
            check_piece(f'tail-{i}-part-{part}',a,b,lo,hi-lo,coefficients)
        if (i+1)%512==0:
            print(json.dumps(dict(event='exact_cardinal_normal_form',completed_spans=i+1,uncovered=len(failed),seconds=time.monotonic()-start)),flush=True)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    witness_path=args.out.with_name(args.out.stem+'-witnesses.json.gz')
    if witness_path.exists():
        raise FileExistsError('Refusing to overwrite exact determinant witnesses')
    witness_raw=(json.dumps(witness,separators=(',',':'))+'\n').encode()
    witness_encoded=gzip.compress(witness_raw,compresslevel=9,mtime=0)
    if len(witness_encoded)>=5_000_000:
        raise ValueError('Witness archive exceeds the per-file bound')
    witness_path.write_bytes(witness_encoded)
    result=dict(schema='exact-C2-cardinal-tail-normal-form-nonplanarity-v1',finished=True,
        source_sha256=sha(Path(__file__).read_bytes()),packet_manifest_sha256=sha(manifest_bytes),
        original_complete_sha256=manifest['original_complete']['sha256'],
        original_plan_sha256=manifest['original_plan']['sha256'],
        original_nodes_verified=count,tail_spans=count-1,
        polynomial_subpieces_checked=len(witness)+len(failed),
        all_cardinal_normal_form_tail_and_collar_pieces_nonplanar=not failed,
        uncovered=failed,cut_target=target_info,
        exact_patch_interval=[str(patch_start),str(cut)],
        shared_node_jets_exactly_reused=True,
        C2_radial_cardinal_traces_from_exact_Hermite=True,
        outer_cardinal_jets_equal_supplied_target=True,
        cuff_cardinal_difference_jet_matches_flat_circle_through_order_two=True,
        witness_file=witness_path.name,witness_sha256=sha(witness_encoded),witness_raw_sha256=sha(witness_raw),
        mathematical_scope='Any finite field analytic in the periodic angle and having these exact shared-node Hermite cardinal traces, including the natural exact trigonometric interpolant of the original full angular node arrays, has no planar open subset on these radial pieces.',
        literal_previous_renderer_binary_field_identity=False,
        exact_prefix_seam_and_common_mean_C2_paid=False,
        exact_nonlinear_limit_nonplanarity_certified=False,
        actual_delta_E_certified=False,task_completed=False,
        limitations=['Exact fractions reconstruct a C2 radial normal form from original nodal bytes, not the literal rounded FFT/Hermite coefficient implementation.',
            'No bound for the normal-form-versus-renderer representation discrepancy is asserted here.',
            'Only angular differences enter the determinant; the source height mean is canceled exactly, not reset in a physical surface.',
            'A nonzero determinant may be arbitrarily small and is not a refinement-stable certificate for an exact nonlinear limit.',
            'Full angular field identity, exact prefix seam conversion, common mean C2 gluing, embedding and image variation remain separate inputs to R238.'],
        seconds=time.monotonic()-start)
    args.out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(output=str(args.out),uncovered=len(failed),normal_form_nonplanar=not failed,seconds=result['seconds'])),flush=True)
    if failed:
        raise SystemExit(1)


if __name__=='__main__':
    main()
