#!/usr/bin/env python3
"""Portably define the actual repaired M12 family and evaluate material Phi.

The JSON manifest gives the exact mathematical definition. The phi and
demo commands evaluate floating representatives for display and point
queries; they do not replace the continuous metric or geometry proofs.
The tail inverse uses a numerical representative of the SAME certified w
packet. Its exact definition is the monotone original-arclength inverse.
"""
from __future__ import annotations
import os
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_name]='1'
import argparse
import bisect
from fractions import Fraction as Q
import gzip
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import sys
import numpy as np

HERE=Path(__file__).resolve().parent;TOPIC=HERE.parent;NOTES=TOPIC/'notes';LD=np.longdouble


def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path);obj=importlib.util.module_from_spec(spec)
    sys.modules[name]=obj;spec.loader.exec_module(obj);return obj


def identity(path):
    path=Path(path).resolve();record=dict(file=str(path),bytes=path.stat().st_size,
        sha256=hashlib.sha256(path.read_bytes()).hexdigest())
    if path.is_relative_to(TOPIC):record['topic_relative_file']=str(path.relative_to(TOPIC))
    return record


def resolve(name,parent=NOTES):
    p=Path(name)
    if not p.exists():
        marker='/topics/visible-flexible-closed-surface/'
        suffix=str(name).split(marker,1)
        candidate=TOPIC/suffix[1] if len(suffix)==2 else TOPIC/p
        p=candidate if candidate.exists() else Path(parent)/p.name
    if not p.exists():raise FileNotFoundError(name)
    return p


INPUTS=dict(
    geometry='2026-11-09-db6f-root-flat17-common-cut-m12-critical-r01.json',
    tail='2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json',
    target='2026-11-09-db6f-root-flat17-m12-target.json',
    bridge='2026-11-09-db6f-root-exact-bridge-m12.json',
    tail_background_packet='2026-11-09-db6f-audit-transfer-lowmetric-final-m12-critical-r01.json',
    old_whole_certificate='2026-11-09-db6f-root-whole-metric-reach-m12-critical-r01-lowmetric.json',
    old_sharper_diameter='2026-11-09-db6f-prefix-m12-segment-ball-budget.json',
    prefix_field='2026-11-12-fd2d-metric-m12-gauge-c2-01/prefix-field.json',
    tail_field='2026-11-12-fd2d-metric-m12-gauge-tail-c2-streamfit-01/tail-field.json',
    global_field_bounds='2026-11-12-fd2d-metric-m12-global-field-bounds-01.json',
    image_meshes='2026-11-12-fd2d-visible-m12-manifest.json')


def make(path):
    if path.exists():raise FileExistsError('Use a new manifest')
    paths={k:NOTES/v for k,v in INPUTS.items()};bindings={k:identity(p) for k,p in paths.items()}
    meta={k:json.loads(p.read_text()) for k,p in paths.items()}
    g,t,bounds=meta['geometry'],meta['tail'],meta['global_field_bounds']
    if g['tail_manifest_sha256']!=bindings['tail']['sha256']:raise ValueError('Wrong own tail')
    if meta['tail_background_packet']['finite_tail_manifest_sha256']!=bindings['tail']['sha256']:
        raise ValueError('Wrong own background packet')
    if not (bounds['global_field_components_present'] and bounds['all_finite_angular_modes_covered'] and
            bounds['all_native_radial_intervals_covered'] and bounds['Dv_operator_upper']<1):
        raise ValueError('Actual global C2 field bounds are incomplete')
    fields={r['region']:r for r in bounds['regions']}
    for region in ('prefix','tail'):
        key=region+'_field'
        if fields[region]['field']['sha256']!=bindings[key]['sha256']:raise ValueError('Bounds belong to another field')
        if not fields[region]['exact_zero_endpoint_jets_verified']:raise ValueError('Missing exact interface identity')
        expected={x['sha256'] for x in fields[region]['bindings']}
        actual=set()
        for part in meta[key]['shards']:
            p=resolve(part['file'],paths[key].parent);record=identity(p)
            if record['sha256']!=part['sha256']:raise ValueError('Changed actual field shard')
            actual.add(record['sha256'])
        if expected!=actual:raise ValueError('Field shard bounds mismatch')
    proofs={name:identity(TOPIC/'results'/name) for name in (
        'R16-fixed-cap-volume-moment-noncongruence.md','R17-exact-finite-visible-closed-geometry.md',
        'R21-m12-whole-map-and-actual-metric-decrease.md','R25-m12-sharper-enclosing-ball.md',
        'R112-noncircular-metric-repair-and-stable-pullback.md')}
    out=dict(schema='fd2d-actual-repaired-m12-closed-family-v1',
        status='ACTUAL_C2_SAME_IMAGE_FAMILY_DEFINED__NEW_METRIC_POSTERIOR_SEPARATE',
        scope=__doc__,script=identity(__file__),inputs=bindings,proofs=proofs,
        domain='S^2: the original two mirrored active annuli joined to the original two fixed caps',
        time=dict(interval_exact=['0','1'],phase='alpha(t)=2*pi*t/3'),
        original_fixed_metric='Exactly the R21 original fixed g; no physical parameter, target profile, cap or time range is changed',
        original_background_definition_hashes=meta['tail_background_packet']['background_definition_hashes'],
        prefix=dict(native_coordinates='s, psi',material_angle='u=psi-e(s)*sin(3*psi)/3',
            field_definition='Saved binary two-jets, exact quintic Hermite, all saved cos(3n psi) and sin(3n psi) modes',
            native_transform='Phi_n(s,u)=(s+p_n(s,u),u+q_n(s,u))',
            physical_coordinate='sigma=s/lambda, lambda=S/L_exact from the unique original exact bridge',
            physical_radial_component='p_phys(sigma,u)=p_n(lambda*sigma,u)/lambda',
            physical_angular_component='q_phys(sigma,u)=q_n(lambda*sigma,u)',
            own_frozen_target='g0=ds^2+a0(s)^2 du^2; its fixed comparison with original g is paid separately',
            exact_bridge_scale_interval=meta['bridge']['arclength_rescale']),
        tail=dict(stored_coordinates='physical radius r and material angle u',
            field_components='p_T is physical meridian-arclength displacement; q_T is angular displacement',
            physical_coordinate='sigma(r)=L_exact+integral_r^c sqrt(1+w(z)^2) dz for the original exact w',
            radial_transform='r_prime is the unique root integral_(r_prime)^r sqrt(1+w(z)^2) dz=p_T(r,u)',
            angular_transform='u_prime=u+q_T(r,u)',
            inner_zero_extension='p_T=q_T=0 below the actual stored lower field endpoint, with its saved zero two-jet',
            support_native_enclosure=fields['tail']['field_support_native_enclosure']),
        mirror=dict(rule='p(-sigma,u)=-p(sigma,u); q(-sigma,u)=q(sigma,u)',
            exact_central_identities='p(0,psi)=p_ss(0,psi)=q_s(0,psi)=0; original exact clamped chart has e_s(0)=0',
            physical_C2_mirror='The chart identities imply the same material-coordinate mirror two-jets'),
        fixed_caps=dict(material_transform='identity',disk_radius_exact=str(Q(t['parameters']['rCuff'])),
            upper_height='Original common-cut Hc + integral_(r_cuff)^c w(r) dr + sum of the three R16 bumps',
            lower_height='Negative of the original unmarked cap height; no lower bump',
            centers_radius_exact='2/25',centers_angles='0,2*pi/3,4*pi/3',
            bump_radius_exact='3/100',bump_height_exact='1/2000',
            bump='(1/2000)*max(1-distance_to_center^2/(3/100)^2,0)^3'),
        family=dict(active='Y_alpha=R_alpha o (X_0 o Phi) o tau_(-alpha)',caps='Y_alpha=X_0 pointwise on each cap',
            warning='Phi need not commute with tau; X_alpha o Phi is not the defining formula',
            image_identity='At every t, the complete image equals that of the original R21 family at the same t'),
        global_C2_diffeomorphism_proved=True,actual_Dv_upper=bounds['Dv_operator_upper'],
        all_time_same_image_geometry='R21/R25 embedding, reach, D, held and noncongruence statements transfer exactly by the image identity',
        mesh_scope='The three existing M12 PLYs display the same images; their vertex material labels remain the old labels, not Phi-transported labels',
        evaluator_scope='Floating Phi and material-to-old-map coordinates only; no new vertex, metric or inverse error certificate is claimed',
        continuous_linear_residual_certified_here=False,nonlinear_metric_certified_here=False,
        README_gate_5_certified_here=False)
    path.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(out=str(path),sha256=identity(path)['sha256'],status=out['status'])))


class StoredField:
    def __init__(self,path):
        source=module('fd2d_phi_field_reader',HERE/'fd2d-metric-material-field-bounds.py')
        self.meta,self.x,self.jets,self.bindings=source.read_field(path)
        self.frequencies=3*np.arange(self.meta['modes']+1,dtype=LD)

    def value(self,x,angle,zero_outside=False):
        x=LD(x)
        if x<LD(self.x[0]) or x>LD(self.x[-1]):
            if zero_outside:return np.zeros(2,dtype=LD)
            raise ValueError('Prefix material coordinate is outside its exact defining interval')
        i=min(max(int(np.searchsorted(self.x,x,side='right'))-1,0),len(self.x)-2)
        h=LD(self.x[i+1])-LD(self.x[i]);t=(x-LD(self.x[i]))/h
        basis=np.array([1-10*t**3+15*t**4-6*t**5,
            h*(t-6*t**3+8*t**4-3*t**5),h*h*(t*t/2-3*t**3/2+3*t**4/2-t**5/2),
            10*t**3-15*t**4+6*t**5,h*(-4*t**3+7*t**4-3*t**5),h*h*(t**3/2-t**4+t**5/2)],dtype=LD)
        jets=np.concatenate((self.jets[i],self.jets[i+1]),axis=1).astype(LD)
        c=np.einsum('j,fjnk->fnk',basis,jets)
        phase=self.frequencies*LD(angle)
        return np.sum(c[:,:,0]*np.cos(phase)+c[:,:,1]*np.sin(phase),axis=1,dtype=LD)


class Background:
    def __init__(self,manifest,packet):
        meta=json.loads(manifest.read_text());self.packet=json.loads(packet.read_text())
        if self.packet['finite_tail_manifest_sha256']!=identity(manifest)['sha256']:raise ValueError('Wrong background')
        increments=[];previous=None
        for part in meta['files']:
            path=resolve(part['path'],manifest.parent);raw=path.read_bytes()
            if hashlib.sha256(raw).hexdigest()!=part['sha256']:raise ValueError('Changed actual radial source')
            a=np.frombuffer(gzip.decompress(raw),dtype='<f8').reshape(part['rows'],part['columns'])
            if not np.isfinite(a).all():raise ValueError('Nonfinite actual radial source')
            if previous is not None and not np.array_equal(a[0],previous):raise ValueError('Different actual raw interface')
            increments.extend(Q(float(x)) for x in a[1:,-1]);previous=a[-1].copy()
        radial=meta['radialGeometry'];scale=Q(int(radial['normalization']['numerator']),int(radial['normalization']['denominator']))
        rq=[Q(radial['innerAnchor'])]
        for h in increments:rq.append(rq[-1]+scale*h)
        if rq[-1]!=Q(radial['outerAnchor']):raise ValueError('Exact radial endpoint mismatch')
        self.r=np.array([LD(q.numerator)/LD(q.denominator) for q in rq],dtype=LD)
        self.cuff=LD(meta['parameters']['rCuff']);self.cut=LD(meta['parameters']['rCut'])
        data=resolve(self.packet['data_file'],packet.parent);raw=data.read_bytes()
        if hashlib.sha256(raw).hexdigest()!=self.packet['data_sha256']:raise ValueError('Changed exact-background packet')
        with np.load(io.BytesIO(gzip.decompress(raw)),allow_pickle=False) as archive:
            self.data={k:archive[k].copy() for k in ('span_index','u_left','u_right','w_lo','w_hi','w_remainder')}
        self.first={};self.last={}
        for row,span in enumerate(self.data['span_index']):
            self.first.setdefault(int(span),row);self.last[int(span)]=row+1
        self.maximum_sampled_w_radius=LD(0)

    def w(self,r):
        r=LD(r)
        if not self.cuff<=r<=self.cut:raise ValueError('Numerical inverse left the actual tail')
        if r<self.r[0]:span=-1;local=(r-self.cuff)/(self.r[0]-self.cuff)
        else:
            span=min(int(np.searchsorted(self.r,r,side='right'))-1,len(self.r)-2)
            local=(r-self.r[span])/(self.r[span+1]-self.r[span])
        first,last=self.first[span],self.last[span]
        row=first+min(max(int(np.searchsorted(self.data['u_left'][first:last],local,side='right'))-1,0),last-first-1)
        z=(local-LD(self.data['u_left'][row]))/(LD(self.data['u_right'][row])-LD(self.data['u_left'][row]))
        lo,hi=self.data['w_lo'][row].astype(LD),self.data['w_hi'][row].astype(LD)
        center=(lo+hi)/2;radius=(hi-lo)/2
        value=np.polynomial.polynomial.polyval(z,center)
        rad=np.polynomial.polynomial.polyval(abs(z),radius)+LD(self.data['w_remainder'][row])
        self.maximum_sampled_w_radius=max(self.maximum_sampled_w_radius,rad)
        return value

    def shift(self,r,p):
        r,p=LD(r),LD(p)
        if p==0:return r,LD(0),LD(0),0
        nodes,weights=np.polynomial.legendre.leggauss(4);nodes=nodes.astype(LD);weights=weights.astype(LD)
        def change(delta):
            values=np.array([np.sqrt(1+self.w(r+delta*(x+1)/2)**2) for x in nodes],dtype=LD)
            return -delta*np.sum(weights*values,dtype=LD)/2
        lo,hi=-abs(p),abs(p)
        for iteration in range(80):
            middle=(lo+hi)/2
            if middle==lo or middle==hi:break
            if change(middle)>p:lo=middle
            else:hi=middle
        delta=(lo+hi)/2
        return r+delta,delta,change(delta)-p,iteration+1


class Evaluator:
    def __init__(self,manifest):
        self.manifest=Path(manifest);self.meta=json.loads(self.manifest.read_text())
        if self.meta['schema']!='fd2d-actual-repaired-m12-closed-family-v1':raise ValueError('Unknown repaired family')
        self.paths={}
        for key,record in self.meta['inputs'].items():
            relative=record.get('topic_relative_file')
            path=TOPIC/relative if relative is not None else resolve(record['file'],self.manifest.parent)
            if not path.exists():path=resolve(record['file'],self.manifest.parent)
            if identity(path)['sha256']!=record['sha256']:raise ValueError('Changed repaired-family input '+key)
            self.paths[key]=path
        self.prefix=StoredField(self.paths['prefix_field']);self.tail=StoredField(self.paths['tail_field'])
        geometry=json.loads(self.paths['geometry'].read_text());target=json.loads(self.paths['target'].read_text())
        self.supplier=module('fd2d_phi_exact_chart',HERE/'78718-prefix-metric-supplier-storage-v1.py')
        self.knots,self.coeff=self.supplier.exact_clamped_spline(geometry['chart'])
        self.end=Q(target['frozen_total_end']);self.warp=8*Q(geometry['warp_reference_q'])
        br=json.loads(self.paths['bridge'].read_text())['arclength_rescale']
        q=(Q(br['lo'])+Q(br['hi']))/2;self.lam=LD(q.numerator)/LD(q.denominator)
        self.bg=None;self.cuff=LD(Q(self.meta['fixed_caps']['disk_radius_exact']).numerator)/LD(Q(self.meta['fixed_caps']['disk_radius_exact']).denominator)

    def e(self,s):
        # Numerical query s is rounded to a binary64 material point, then
        # the original rational chart is evaluated exactly at that point.
        x=Q(float(s))/self.end;j=min(max(bisect.bisect_right(self.knots,x)-1,0),len(self.coeff)-1)
        y=Q(0)
        for c in self.coeff[j][::-1]:y=y*(x-self.knots[j])+c
        if x>Q(3,4):
            t=4*x-3;y*=1-10*t**3+15*t**4-6*t**5
        y*=self.warp;return LD(y.numerator)/LD(y.denominator)

    def inverse_angle(self,s,u):
        e=self.e(s);u=LD(u);lo,hi=u-abs(e)/3,u+abs(e)/3;psi=u
        if e==0:return psi,LD(0)
        for _ in range(100):
            residual=psi-e*np.sin(3*psi)/3-u
            if abs(residual)<=8*np.finfo(LD).eps*(1+abs(u)):break
            if residual<0:lo=psi
            else:hi=psi
            trial=psi-residual/(1-e*np.cos(3*psi))
            psi=trial if lo<trial<hi else (lo+hi)/2
        return psi,psi-e*np.sin(3*psi)/3-u

    def phi(self,region,coordinate,u,t='0',side='upper',prefix_units='native'):
        tq=Q(t)
        if not 0<=tq<=1:raise ValueError('Phase time must lie in [0,1]')
        sign=1 if side=='upper' else -1;coordinate=LD(coordinate);u=LD(u)
        alpha=2*np.arccos(LD(-1))*(LD(tq.numerator)/LD(tq.denominator))/3
        common=dict(region=region,side=side,t_exact=str(tq),input_coordinate=float(coordinate),input_material_u=float(u),
            numerical_representative_only=True,metric_or_vertex_error_certified=False)
        if region=='cap':
            if not 0<=coordinate<=self.cuff:raise ValueError('Cap point is outside its actual disk')
            return {**common,'mapped_coordinate':float(coordinate),'mapped_material_u':float(u),
                'p_physical_signed':0.,'q':0.,'ambient_rotation_alpha':0.,'fixed_cap_identity':True}
        material=u-alpha
        if region=='prefix':
            s=coordinate if prefix_units=='native' else coordinate*self.lam
            psi,error0=self.inverse_angle(s,material);p,q=self.prefix.value(s,psi)
            new_s=s+p;new_u=material+q;new_psi,error1=self.inverse_angle(new_s,new_u)
            return {**common,'prefix_input_units':prefix_units,'input_native_s':float(s),
                'input_prephase_u':float(material),'field_native_psi':float(psi),
                'mapped_native_s':float(new_s),'mapped_material_u':float(new_u),'mapped_native_psi':float(new_psi),
                'p_native':float(p),'p_physical_signed':float(sign*p/self.lam),'q':float(q),
                'native_radial_shift_longdouble':str(p),'physical_bridge_scale_representative':float(self.lam),
                'ambient_rotation_alpha':float(alpha),'lower_map_is_z_mirror':side=='lower',
                'maximum_numeric_angle_inverse_residual':float(max(abs(error0),abs(error1)))}
        if region!='tail':raise ValueError('Unknown material region')
        cut=LD(json.loads(self.paths['tail'].read_text())['parameters']['rCut'])
        if not self.cuff<=coordinate<=cut:raise ValueError('Tail point outside actual tail/collar')
        p,q=self.tail.value(coordinate,material,zero_outside=True)
        if p==0:new_r,delta,residual,iterations=coordinate,LD(0),LD(0),0
        else:
            if self.bg is None:self.bg=Background(self.paths['tail'],self.paths['tail_background_packet'])
            new_r,delta,residual,iterations=self.bg.shift(coordinate,p)
        return {**common,'input_prephase_u':float(material),'mapped_radius':float(new_r),
            'mapped_material_u':float(material+q),'p_physical_signed':float(sign*p),'q':float(q),
            'radial_shift_longdouble':str(delta),'ambient_rotation_alpha':float(alpha),
            'lower_map_is_z_mirror':side=='lower','numeric_relative_arclength_inverse_residual':float(abs(residual)),
            'inverse_iterations':iterations,'sampled_w_packet_radius_diagnostic':None if self.bg is None else float(self.bg.maximum_sampled_w_radius)}


def main():
    p=argparse.ArgumentParser(description=__doc__);sub=p.add_subparsers(dest='command',required=True)
    m=sub.add_parser('make');m.add_argument('--out',type=Path,required=True)
    for name in ('phi','demo'):
        q=sub.add_parser(name);q.add_argument('--manifest',type=Path,required=True);q.add_argument('--out',type=Path)
        if name=='phi':
            q.add_argument('--region',choices=['prefix','tail','cap'],required=True)
            q.add_argument('--coordinate',required=True);q.add_argument('--u',required=True)
            q.add_argument('--t',default='0');q.add_argument('--side',choices=['upper','lower'],default='upper')
            q.add_argument('--prefix-units',choices=['native','physical'],default='native')
    args=p.parse_args()
    if args.command=='make':return make(args.out)
    if args.out is not None and args.out.exists():raise FileExistsError('Use a new query report')
    evaluator=Evaluator(args.manifest)
    if args.command=='phi':result=evaluator.phi(args.region,args.coordinate,args.u,args.t,args.side,args.prefix_units)
    else:
        end=float(evaluator.prefix.x[-1]);queries=[]
        for t in ('0','1/4','1/2'):
            for region,c,u in [('prefix',0.,.17),('prefix',.8,.4),('prefix',end,.3),
                               ('tail',.4,.2),('tail',.49866589752085294,.5),('tail',.6,.3),('cap',.08,0.)]:
                for side in ('upper','lower'):queries.append(evaluator.phi(region,c,u,t,side))
        result=dict(schema='fd2d-material-phi-floating-demo-v1',script=identity(__file__),manifest=identity(args.manifest),
            queries=queries,query_count=len(queries),scope=__doc__,continuous_certificate=False)
    text=json.dumps(result,indent=2,allow_nan=False)+'\n'
    if args.out is not None:
        args.out.write_text(text);print(json.dumps(dict(out=str(args.out),sha256=identity(args.out)['sha256'],
            query_count=result.get('query_count',1),continuous_certificate=False)))
    else:print(text)


if __name__=='__main__':main()
