#!/usr/bin/env python3
"""Recover the documented pulse->Hold->mode-damped warm from a fresh prefix.

The historical sources remain unmodified. Their output-byte identity constants
are explicitly rebound to this run's NEW artifacts; original and new values are
recorded. This preserves the mathematical generator while not claiming byte
identity with lost scratch outputs. No continuous certificate is inherited.
Only nodal integration, the existing C2 bridge and assembly are run; old large
readout grids and certificates are deliberately not reproduced.
"""
import argparse
import contextlib
import copy
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time
from types import SimpleNamespace as NS

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(name,p):
    sp=importlib.util.spec_from_file_location(name,p)
    m=importlib.util.module_from_spec(sp);sys.modules[name]=m;sp.loader.exec_module(m);return m
def readgz(p):return json.loads(gzip.decompress(Path(p).read_bytes()))
def writegz(p,obj):Path(p).write_bytes(gzip.compress((json.dumps(obj)+'\n').encode(),mtime=0))

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo',type=Path,required=True)
    p.add_argument('--work',type=Path,required=True)
    p.add_argument('--prefix',type=Path)
    a=p.parse_args();a.repo=a.repo.resolve();a.work=a.work.resolve()
    t=a.repo/'topics/visible-flex-larger-amplitude';notes=t/'notes';scripts=t/'scripts'
    sys.path.insert(0,str(scripts));data=a.work/'data';logs=a.work/'logs'
    data.mkdir(exist_ok=True,parents=True);logs.mkdir(exist_ok=True)
    prefix=(a.prefix or data/'continue0995m112.json.gz').resolve()
    d=readgz(prefix)
    if not d.get('success') or d['M']!=112 or d['N']!=2048 or d['mesh'][-1]!=.995:
        raise ValueError('Need the actual accepted reconstructed .995 M112/N2048 prefix')
    manifest=a.work/'rebuild-closed-warm-manifest.json'
    if manifest.exists():
        report=json.loads(manifest.read_text())
        if report['prefix_sha256']!=sha(prefix):raise ValueError('Recovery prefix changed')
    else:
        report=dict(schema='fullclosed-warm-recovery-20261120-v1',driver_sha256=sha(__file__),
            prefix=str(prefix),prefix_sha256=sha(prefix),outputs_are_new_reproductions=True,
            historical_certificates_inherited=False,stages=[])
    def save():manifest.write_text(json.dumps(report,indent=2)+'\n')
    def done(name):
        x=next((x for x in report['stages']if x['name']==name),None)
        if x and x.get('complete'):
            for f,h in x['outputs'].items():
                if not Path(f).exists() or sha(f)!=h:raise ValueError('A completed recovery output changed: '+f)
            return True
        return False
    def record(name,start,outputs,**kw):
        r=dict(name=name,complete=True,seconds=time.monotonic()-start,
            outputs={str(f):sha(f)for f in outputs},**kw)
        report['stages'].append(r);save()
        print(json.dumps(dict(event='completed_warm_recovery_stage',name=name,seconds=r['seconds'],**kw)),flush=True)

    metric=data/'inward-scalar-parameter-carrier.json.gz'
    if not metric.exists():
        from parallel_20261117_inward_profile import InwardProfile
        import parallel_20261117_inward_profile as inward
        g=InwardProfile(d['fixed_scalar_profile']['geometry'],d['analytic_extension_origin'],.995,1.5,.02,.02,32)
        carrier=dict(schema='scalar-parameter-carrier-only-20261120',
            scope='Parameters only, not an accepted inward BVP or any surface field.',
            source_sha256=sha(__file__),inward_profile_sha256=sha(inward.__file__),
            fixed_scalar_profile=d['fixed_scalar_profile'],analytic_extension_origin=d['analytic_extension_origin'],
            inward_scalar_profile=g.spec(),success=False)
        writegz(metric,carrier)
    local=data/'pulse-a5-fullfield-n4096-c2.json.gz'
    pulse_path=notes/'2026-11-17-parallel-inward-curvature-pulse.py'
    wrapper_path=notes/'2026-11-17-parallel-pulse-common-jet-field.py'
    if not done('pulse_shared_jets'):
        start=time.monotonic();wrapper=load('recovery_pulse_shared_jets',wrapper_path)
        metricdata=readgz(metric);z=metricdata['inward_scalar_profile']
        profile=wrapper.pulse.PulseProfile(d['fixed_scalar_profile']['geometry'],d['analytic_extension_origin'],
            z['cut'],z['curvature'],z['ramp_in'],z['ramp_out'],z['quadrature'],-5.,.005)
        wrapper.field.h.profile_from=lambda unused:profile
        cfg=NS(reference=prefix,metric=metric,modes=320,end=1.,rtol=1e-13,atol=1e-16,
            max_step=.000015625,keep_terminal_microcells=False,output_stem=data/'pulse-a5-fullfield')
        with (logs/'pulse-shared-jets.log').open('w') as f,contextlib.redirect_stdout(f):
            raw_record,raw=wrapper.field.nodal_field(cfg,d,metricdata,4096)
        if raw is None or not raw_record['ivp_reached_end']:raise RuntimeError('Actual pulse IVP did not reach the original endpoint: '+str(raw_record))
        raw.update(scope=wrapper.__doc__,inward_scalar_profile=profile.spec(),source_sha256=sha(wrapper_path),
            common_jet_source_sha256=sha(wrapper.FIELD),pulse_source_sha256=sha(pulse_path),
            unmodified_inward_profile_sha256=raw['inward_profile_sha256'],recovery_driver_sha256=sha(__file__))
        rawpath=Path(raw_record['field_path']);writegz(rawpath,raw)
        raw['frozen_local_field_sha256']=sha(rawpath)
        joined=wrapper.bridge(raw,d,32);writegz(local,joined)
        record('pulse_shared_jets',start,[rawpath,local,metric],
            source_sha256=sha(wrapper_path),pulse_source_sha256=sha(pulse_path),
            nodes=len(joined['mesh']),M=joined['M'],N=joined['N'],nfev=joined['nfev'],
            exact_shared_initial_jets=True,new_geometry_readouts=0)
    assembled=data/'pulse-a5-complete-base.json.gz'
    if not done('assemble_common_prefix'):
        start=time.monotonic();asm_path=scripts/'parallel_20261117_pulse_arclength_readout.py'
        asm=load('recovery_assembly_only',asm_path)
        assembled_data,_=asm.assemble(NS(parent=prefix,local=local,pulse_source=pulse_path,assembled=assembled))
        record('assemble_common_prefix',start,[assembled],source_sha256=sha(asm_path),
            nodes=len(assembled_data['mesh']),M=assembled_data['M'],
            cut_jet_differences=assembled_data['cut_jet_differences'],new_geometry_readouts=0)
    scalar=notes/'2026-11-17-parallel-model-full-hold-oracle.py'
    integer=notes/'2026-11-17-parallel-inward-integral-enclosure.py'
    hold=scripts/'parallel_20261117_negative_hold_profile_ivp.py'
    parent_report=data/'fullclosed-hold-warm.json';parent_bundle=parent_report.with_suffix('.npz')
    if not done('fullclosed_hold_warm'):
        start=time.monotonic();src=notes/'2026-11-17-parallel-model-fullclosed-hold-warm.py'
        gen=load('recovery_hold_warm',src);old=gen.INPUT_SHA;gen.INPUT_SHA=sha(assembled)
        with (logs/'fullclosed-hold-warm.log').open('w') as f,contextlib.redirect_stdout(f):
            gen.main(NS(input=assembled,scalar_source=scalar,integer_source=integer,hold_source=hold,out=parent_report))
        r=json.loads(parent_report.read_text())
        record('fullclosed_hold_warm',start,[parent_report,parent_bundle],source_sha256=sha(src),
            explicit_identity_rebinding=dict(INPUT_SHA=dict(historical=old,reproduced=gen.INPUT_SHA)),
            J=r['J'],M=r['M'],Hcap=r['Hcap'],S_carrier=r['S_carrier'],radius_carrier=r['radius_carrier'])
    final_report=data/'fullclosed-mode-damped-warm.json';final_bundle=final_report.with_suffix('.npz')
    if not done('fullclosed_mode_damped_warm'):
        start=time.monotonic();src=notes/'2026-11-17-parallel-model-fullclosed-mode-damped-warm.py'
        gen=load('recovery_mode_damped_warm',src)
        changes={}
        for key,path in [('PARENT_BUNDLE_SHA',parent_bundle),('PARENT_REPORT_SHA',parent_report),('INPUT_SHA',assembled)]:
            changes[key]=dict(historical=getattr(gen,key),reproduced=sha(path));setattr(gen,key,sha(path))
        with (logs/'fullclosed-mode-damped-warm.log').open('w') as f,contextlib.redirect_stdout(f):
            gen.main(NS(parent_bundle=parent_bundle,parent_report=parent_report,input=assembled,
                scalar_source=scalar,integer_source=integer,hold_source=hold,out=final_report))
        r=json.loads(final_report.read_text())
        record('fullclosed_mode_damped_warm',start,[final_report,final_bundle],source_sha256=sha(src),
            explicit_identity_rebindings=changes,J=r['J'],M=r['M'],Hcap=r['Hcap'],
            prefix_819_triples_bitwise_identical=r['prefix_819_triples_bitwise_identical'])
    report['complete']=True;report['final_bundle']=str(final_bundle);save()
    print(json.dumps(dict(event='fullclosed_warm_recovery_complete',manifest=str(manifest),bundle=str(final_bundle),sha256=sha(final_bundle))),flush=True)

if __name__=='__main__':main()
