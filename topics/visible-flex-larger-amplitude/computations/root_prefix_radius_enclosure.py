#!/usr/bin/env python3
"""All-angle horizontal-radius enclosure of a saved finite neck representation.

The recorded binary polynomial coefficients and a frozen binary segment and
quadrature program define the finite horizontal map. Arb encloses that real
formula continuously in s and angle. This does not certify exact isometry,
C2 seam consistency of rounded segment data, a true integral profile, height,
embedding, reach, or closure. No nonlinear solve or Jacobian is constructed.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
from fractions import Fraction
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import sys
import time
import numpy as np
import flint
from flint import arb,ctx

HERE=Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load_json(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith('.gz') else raw)


def interval(lo,hi):
    return arb(lo).union(arb(hi))


def clipped(x,lo=0,hi=1):
    lo,hi=arb(lo),arb(hi)
    a,b=x.lower(),x.upper()
    a=lo if a<lo else hi if a>hi else a
    b=lo if b<lo else hi if b>hi else b
    return a.union(b)


def phase_point(seg,u):
    p0,p1=arb(seg['p0']),arb(seg['p1'])
    if 'turn_ramp' in seg:
        eps=arb(seg['turn_ramp'])
        # u is an exact endpoint. At a ramp join either formula agrees.
        if u<=eps:
            v=u/eps;primitive=eps*(v**3-v**4/2)
        elif u>=1-eps:
            v=(1-u)/eps;primitive=1-eps-eps*(v**3-v**4/2)
        else:
            primitive=u-eps/2
        return p0+(p1-p0)*primitive/(1-eps)
    if seg['kind']=='turn':return p0+(p1-p0)*(3*u*u-2*u**3)
    if seg['kind']=='brake':return p0+(p1-p0)*u*u
    return p0


def phase_interval(seg,u):
    # Every supported phase is monotone on [0,1].
    return phase_point(seg,u.lower()).union(phase_point(seg,u.upper()))


def radius_program(seg,s,gu,gw):
    length=arb(seg['length'])
    u=clipped((s-arb(seg['offset'])-arb(seg['s0']))/length)
    a0=arb(seg['a0'])
    if seg['kind']=='hermite':
        b=arb(seg['k0'])*length;v=arb(seg['v1']);c=3*v-2*b;d=b-2*v
        return a0+length*(b*u*u/2+c*u**3/3+d*u**4/4)
    if seg['kind']=='boost' and not seg.get('strong_angle_boost'):
        v=arb(seg['v0']);dv=arb(seg['v1'])-v
        return a0+length*(v*u+dv*(u**3-u**4/2))
    cuts=[arb(0),arb(1)]
    if 'turn_ramp' in seg:
        eps=arb(seg['turn_ramp']);cuts=[arb(0),eps,1-eps,arb(1)]
    total=arb(0)
    for left,right in zip(cuts[:-1],cuts[1:]):
        width=clipped(u-left,0,right-left)
        summed=arb(0)
        for point,weight in zip(gu,gw):
            angle=phase_interval(seg,clipped(left+width*point))
            summed+=weight*angle.sin()
        total+=width*summed/2
    return a0+length*total


def binary_bound(value,lower=True):
    value=value.lower() if lower else value.upper()
    mantissa,exponent=value.man_exp()
    return dict(mantissa=str(mantissa),exponent=int(exponent),
                decimal=float(value),direction='lower' if lower else 'upper')


def snapshot_program(record,port_file,input_file):
    name='root_radius_frozen_provider'
    source=HERE/'alternative-neck-provider.py'
    spec=importlib.util.spec_from_file_location(name,source)
    provider=importlib.util.module_from_spec(spec);sys.modules[name]=provider;spec.loader.exec_module(provider)
    cfg=record['frozen_profile'];prefix=provider.NeckPrefix(cfg)
    port=provider.tagged_port(load_json(port_file),cfg)
    if port['parameters']!=record['physical_tail_parameters'] or port['cut']!=record['physical_tail_cut']:
        raise ValueError('The frozen physical port changed')
    bridge=provider.NeckTerminalBridge(port['cut'])
    if prefix.end+bridge.end!=record['meridian_length']:
        raise ValueError('The rebuilt binary meridian length differs')
    segments=[]
    for region,offset,pieces in [('prefix',0.,prefix),('terminal_bridge',prefix.end,bridge)]:
        for seg in pieces.segments:
            segments.append(dict(seg,region=region,offset=offset))
    dependencies=['alternative-neck-provider.py','alternative-neck-flatturn.py',
                  'alternative-neck-excursion.py','alternative-angle-plateau-connector.py',
                  'alternative-direct-tail-connector.py','strong_angle_boost.py']
    return dict(scope='Frozen binary program for the finite horizontal representation; not an exact-integral or C2-seam certificate.',
        input_sha256=sha(input_file),port_sha256=sha(port_file),profile=cfg,
        meridian_length=record['meridian_length'],segments=segments,
        quadrature=dict(nodes=provider.base.gu.tolist(),weights=provider.base.gw.tolist()),
        dependency_sha256={name:sha(HERE/name) for name in dependencies})


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,required=True)
    p.add_argument('--port',type=Path,required=True)
    p.add_argument('--snapshot',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--bits',type=int,default=96)
    args=p.parse_args();started=time.monotonic();ctx.prec=args.bits
    if args.bits<80:raise ValueError('Use at least 80-bit midpoint precision')
    rec=load_json(args.input)
    if not rec.get('solver_success') or rec['angular_chart']!='general-support-core-blend-v1':
        raise ValueError('Require a complete successful general-core finite prefix')
    if rec['frozen_profile']['ramp_law']!='hermite_boost_neck':
        raise ValueError('The frozen program only supports the actual neck provider')
    if int(rec['config'].get('base_mode',2))!=2 or rec.get('chart_transition_start',0.)!=0. or rec.get('chart_transition_end',1.)!=1.:
        raise ValueError('Require the recorded mode-2 full-length core blend')
    if args.snapshot.exists():program=load_json(args.snapshot)
    else:
        program=snapshot_program(rec,args.port,args.input)
        args.snapshot.write_text(json.dumps(program,indent=2)+'\n')
    if program['input_sha256']!=sha(args.input) or program['port_sha256']!=sha(args.port):
        raise ValueError('Frozen program belongs to another saved prefix or port')
    chunks=[];next_state=0
    for item in rec['pp_coefficient_chunks']:
        path=args.input.parent/item['file']
        if Path(item['file']).name!=item['file'] or sha(path)!=item['sha256']:
            raise ValueError('Coefficient chunk identity changed')
        if item['state_first']!=next_state:raise ValueError('Noncontiguous state chunks')
        with gzip.open(path,'rb') as stream:chunk=np.load(stream,allow_pickle=False)
        if chunk.shape[2]!=item['state_last_exclusive']-next_state:
            raise ValueError('Wrong coefficient chunk state dimension')
        chunks.append(chunk);next_state=item['state_last_exclusive']
    coefficients=np.concatenate(chunks,axis=2)
    mesh=rec['mesh'];M=int(rec['config']['modes']);q=arb(rec['gauge_amplitude'])
    if not q>0 or coefficients.shape!=(6,len(mesh)-1,3*M+1):
        raise ValueError('Unexpected saved quintic layout or gauge')
    ref=rec['chart_reference_coefficients'];frequencies=rec['chart_reference_frequencies']
    A=sum((abs(arb(c))*abs(1-n*n)/n for n,c in zip(frequencies,ref)),arb(0)).upper()
    hmin=(1-sum((abs(arb(c)) for c in ref),arb(0))).lower()
    if not (hmin>0 and A<arb.pi()/2):raise ValueError('The simple reference radial bound is unavailable')
    gu=list(map(arb,program['quadrature']['nodes']));gw=list(map(arb,program['quadrature']['weights']))
    if any(not 0<g<1 for g in gu) or any(not w>0 for w in gw):
        raise ValueError('Quadrature must have positive interior nodes and weights')
    length=arb(rec['meridian_length']);segments=program['segments'];rows=[]
    worst=None;by_segment={};coverage=[]
    # Use exact binary rational split points, then enclose every interval.
    for i,(left,right) in enumerate(zip(mesh[:-1],mesh[1:])):
        left,right=Fraction.from_float(left),Fraction.from_float(right)
        covered=[]
        for j,seg in enumerate(segments):
            a=Fraction.from_float(seg['offset'])+Fraction.from_float(seg['s0'])
            b=Fraction.from_float(seg['offset'])+Fraction.from_float(seg['s1'])
            # Rounded global endpoint conventions can differ from a sum by one
            # ulp. Include either adjacent segment in that tiny fringe rather
            # than silently dropping any s from the recorded whole interval.
            edge_pad=Fraction(1,10**12)
            lo,hi=max(left,a-edge_pad),min(right,b+edge_pad)
            if lo>hi:continue
            S=interval(arb(str(lo)),arb(str(hi)));t=S-arb(mesh[i])
            amin=radius_program(seg,S,gu,gw).lower()
            if not amin>0:
                raise ValueError('Positive background radius was not enclosed on a piece')
            x=clipped(arb(str(lo))/length)
            bmax=(1-x**3*(10-15*x+6*x*x)).upper()
            bmax=arb(1) if bmax>1 else arb(0) if bmax<0 else bmax
            cmin=(bmax*A).cos().lower()
            lower_reference=min(cmin,((1-bmax)*cmin+bmax*hmin).lower())
            if not lower_reference>0:
                raise ValueError('Positive reference radial component was not enclosed')
            radial=[]
            for state in range(M+1):
                v=arb(float(coefficients[0,i,state]))
                for k in range(1,6):v=v*t+arb(float(coefficients[k,i,state]))
                radial.append(v)
            radial_lower=radial[0].lower()-sum((v.abs_upper() for v in radial[1:]),arb(0))
            lower=(amin*lower_reference+q*radial_lower).lower()
            row=dict(interval=i,segment=j,region=seg['region'],kind=seg['kind'],
                s_lower=float(lo),s_upper=float(hi),background_radius_lower=binary_bound(amin),
                reference_radial_lower=binary_bound(lower_reference),
                perturbation_radial_lower=binary_bound(q*radial_lower),
                horizontal_radius_lower=binary_bound(lower),positive=bool(lower>0))
            rows.append(row);covered.append((lo,hi))
            if worst is None or lower<worst[0]:worst=(lower,row)
            if j not in by_segment or lower<by_segment[j][0]:by_segment[j]=(lower,row)
        cursor=left
        for lo,hi in sorted(covered):
            if lo>cursor:raise ValueError('A recorded physical interval was left uncovered')
            cursor=max(cursor,hi)
        if cursor<right:raise ValueError('Uncovered terminal interval')
        coverage.append(True)
    out=dict(scope=__doc__,status='Certified radius of the stated finite binary-formula representation only',
        input=str(args.input),input_sha256=sha(args.input),snapshot=str(args.snapshot),snapshot_sha256=sha(args.snapshot),
        source_sha256=sha(Path(__file__)),python_flint_version=flint.__version__,arb_precision_bits=args.bits,
        arithmetic_reference='https://python-flint.readthedocs.io/en/stable/arb.html',
        core_reference_arc_offset_abs_upper=binary_bound(A,False),core_reference_support_lower=binary_bound(hmin),
        covered_quintic_intervals=len(coverage),piece_intersections=len(rows),
        all_horizontal_radius_lower_bounds_positive=all(row['positive'] for row in rows),
        worst=worst[1],segment_minima=[x[1] for _,x in sorted(by_segment.items())],
        intervals=rows,seconds=time.monotonic()-started,
        peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        limits=['No mean height or vertical separation is used or certified.',
                'The fixed quadrature program is enclosed as a real finite formula, not replaced by an exact profile integral.',
                'Rounded segment seams and the common exact metric still need separate control.',
                'Positive horizontal radius alone is not the projection-Jacobian, embedding or reach criterion.'])
    raw=(json.dumps(out,indent=2)+'\n').encode()
    if len(raw)>1_000_000 and args.out.suffix!='.gz':
        raise ValueError('Use a .json.gz output for a report over 1 MB')
    if args.out.suffix=='.gz':raw=gzip.compress(raw,mtime=0)
    if len(raw)>=5_000_000:raise ValueError('Output exceeds the repository file cap')
    args.out.write_bytes(raw)
    print(json.dumps(dict(output=str(args.out),seconds=out['seconds'],peak_RSS_KiB=out['peak_RSS_KiB'],
        intervals=len(coverage),pieces=len(rows),all_positive=out['all_horizontal_radius_lower_bounds_positive'],
        radius_lower=out['worst']['horizontal_radius_lower'],worst_segment=out['worst']['segment'])))


if __name__=='__main__':main()
