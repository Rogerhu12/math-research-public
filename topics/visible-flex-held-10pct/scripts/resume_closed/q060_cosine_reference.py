#!/usr/bin/env python3
"""Bind the genuine q=.06 cosine reference for a later R44 design initializer.

The command-line entry performs metadata/source binding only. It does not
construct a new core, project an initial guess, change q, embed into M16 or
call a BVP/tail solver. The separate native_reference method is an explicit
future evaluation entry, using the original cosine constructor and original
material chart. No raw/circle homotopy metadata is attached to this input.
"""
from dataclasses import dataclass
import argparse
import copy
import gzip
import hashlib
import importlib.util
import inspect
import json
from pathlib import Path
import sys
from types import SimpleNamespace

import numpy as np


CHECKPOINT_SHA256='4755143bb3c02c28669eebaa2db53ad97142acec799afd4136125db4277350d9'
SUPPORTED_REFERENCE_SOURCES={
    'scripts/950f-prefix-adaptive-chart-bvp-v2.py':'958a9e2e428f8d64dfc786bed515bad77a208433fa16af7cbbe6f03b1bcc7ebe',
    'scripts/950f-prefix-warped-bvp.py':'eb70e36397ea47638e042e7f2ef465ccef30cd853342adf049c2e3718261ac70',
    'scripts/db6f-prefix-flat-profile.py':'5066cd6d8f94d3b22c0450cc2016df6f90d04efb85d7a13bc833c11868eaaa4b',
    'scripts/950f-prefix-flat-accel-screen.py':'dca3d7fdd5495f4eeeea923522b3001499f48f4b770d262b43e6f88a80b8f6ef',
    'notes/fixed_metric_mode3_core.py':'a529904e265ddc95635c6c6601ea173eb0e1383a75e458d3eaee024fe7078ead',
    'notes/fixed_metric_mode3_flow.py':'0e5555fa23609e2e7154f0e952c6b7ddc402a4cf54be148842f36db886103dc5',
    'notes/fixed_metric_mode3_bvp.py':'e2e5cf08339c82fac24ef296dc721cec4e43852d2a6d963721ce69a1d8d7a11c',
    'repro/source-root/topics/large-amplitude-twist-flex/scripts/curve_stable_prefix_bvp.py':'e621ee2e9e8a706332b3839122a8ec57e1c5c2cfe82a48a759dcdad0548c54b2',
}
SHORT_BRIDGE_SHA256='7e00a3336a302ba94c751c09e6f75749d6973c86605269538c8f0b44c60779b4'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ref(path):
    return dict(path=str(Path(path).resolve()),sha256=sha(path))


def payload_sha(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()


def load(path):
    path=Path(path)
    return json.loads(gzip.decompress(path.read_bytes()) if path.suffix=='.gz' else path.read_text())


def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    value=importlib.util.module_from_spec(spec)
    sys.modules[name]=value;spec.loader.exec_module(value)
    return value


@dataclass(frozen=True)
class CosineReferenceBinding:
    checkpoint: Path
    terminal_record: Path
    source_topic: Path
    short_bridge: Path
    record: dict
    terminal: dict
    input_files: dict
    all_source_sha256: dict
    current_reference_source_sha256: dict

    def check_sources(self):
        for path,digest in self.all_source_sha256.items():
            if sha(path)!=digest:raise ValueError('A bound reference source changed: '+path)
        if sha(self.checkpoint)!=CHECKPOINT_SHA256:
            raise ValueError('The pinned genuine reference checkpoint changed')

    @property
    def actual_controls(self):
        return np.asarray(self.record['parameters'][1:],float)*np.asarray(self.record['central_correction_scales'],float)

    def native_reference(self):
        """Future source evaluation only; not called by this file's CLI.

        Return the original Core, Flow and all-25-state exported polynomial.
        No BVP object, initial-guess projection, lift or end repair is made.
        The complete mean height is available through the returned original
        flow.height_integral method, never silently replaced by zero.
        """
        self.check_sources()
        fresh_names=('fixed_metric_mode3_core','fixed_metric_mode3_flow',
                     'fixed_metric_mode3_bvp','curve_stable_prefix_bvp')
        if any(name in sys.modules for name in fresh_names):
            raise RuntimeError('Construct this original cosine reference in a fresh process')
        scripts=self.source_topic/'scripts'
        ad=module('q060_original_cosine_adaptive',scripts/'950f-prefix-adaptive-chart-bvp-v2.py')
        module('q060_original_cosine_flat',scripts/'db6f-prefix-flat-profile.py').install(ad)
        ad.old.install_source(self.source_topic/'repro/source-root')
        module('q060_original_cosine_short',self.short_bridge).install()
        Flow,_=ad.build_classes(copy.deepcopy(self.record['chart']))
        import fixed_metric_mode3_core as original_core
        expected=(self.source_topic/'notes/fixed_metric_mode3_core.py').resolve()
        if Path(inspect.getsourcefile(original_core.PlanarSupportCore)).resolve()!=expected:
            raise ValueError('The original cosine constructor was replaced')
        record=self.record
        core=original_core.PlanarSupportCore(record['actual_primary_amplitude'],
                                             self.actual_controls,base_mode=3)
        if (not np.array_equal(core.coefficients,np.r_[record['actual_primary_amplitude'],self.actual_controls])
                or not np.array_equal(core.frequencies,3*np.arange(1,9))):
            raise AssertionError('The full original cosine core was not retained')
        port=load(self.input_files['linear_port']['path'])
        port['cut']['_prefix_bridge']=copy.deepcopy(record['frozen_profile']['prefix_bridge'])
        if (port['parameters']!=record['physical_tail_parameters'] or
                port['cut']!=record['physical_tail_cut']):
            raise ValueError('The supplied port changes the recorded physical reference')
        flow=Flow(copy.deepcopy(record['frozen_profile']),port,8,record['gauge_amplitude'],
                  record['config']['angular'],3,warp_q=record['warp_reference_q'])
        if flow.n!=25 or flow.M!=8 or float(flow.end).hex()!=float(record['meridian_length']).hex():
            raise ValueError('The original physical profile/domain was not retained')
        if hasattr(flow,'exact_lift_core'):
            raise ValueError('A raw/integral core lift was wrongly added to the cosine reference')
        from curve_stable_prefix_bvp import load_checkpoint
        from scipy.interpolate import PPoly
        decoded=load_checkpoint(self.checkpoint)
        values=np.asarray(decoded['pp_coefficients'],float)
        mesh=np.asarray(decoded['mesh'],float)
        if values.shape!=(6,len(mesh)-1,25) or len(mesh)!=1934:
            raise ValueError('The complete original M8/25-state quintic is required')
        pp=PPoly.construct_fast(values,mesh,extrapolate=False,axis=1)
        if mesh[0]!=0. or mesh[-1]!=flow.end:
            raise ValueError('The saved physical polynomial and original flow domain differ')
        sol=SimpleNamespace(x=mesh,sol=pp)
        self.check_sources()
        return SimpleNamespace(core=core,flow=flow,polynomial=pp,solution=sol,
            original_parameters=np.asarray(record['parameters'],float).copy(),
            original_scales=np.asarray(record['central_correction_scales'],float).copy(),
            physical_profile=copy.deepcopy(record['frozen_profile']),
            provenance=self.descriptor())

    def descriptor(self):
        r=self.record
        return dict(scope=__doc__,checkpoint=ref(self.checkpoint),terminal_record=ref(self.terminal_record),
            source_topic=str(self.source_topic),short_bridge=ref(self.short_bridge),
            original_execution_source_sha256=self.terminal['source_sha256'],
            current_reference_source_sha256=self.current_reference_source_sha256,
            additional_source_scope='These explicit current reference imports are bound for this new interface; they do not retroactively add source hashes to the earlier numerical execution.',
            original_inputs=self.input_files,
            core_kind=r['config']['core_kind'],base_mode=3,modes=8,state_components=25,
            actual_q=r['actual_primary_amplitude'],gauge_q=r['gauge_amplitude'],
            full_parameters=r['parameters'],full_correction_scales=r['central_correction_scales'],
            full_actual_controls=self.actual_controls.tolist(),
            original_support_frequencies=(3*np.arange(1,9)).tolist(),
            original_support_coefficients=[r['actual_primary_amplitude'],*self.actual_controls.tolist()],
            exact_old_primary_factor=1,old_primary_scope='Literal h=1+q*cos(3phi)+sum(c_j*cos(3j phi)), j=2..8; the signed support cosine-3 coefficient is q by Fourier orthogonality.',
            physical_profile=r['frozen_profile'],meridian_length_binary64=r['meridian_length'],
            warp_reference_q=r['warp_reference_q'],chart_kind=r['angular_chart'],
            chart_payload_sha256=payload_sha(r['chart']),physical_port_sha256=r['physical_port_sha256'],
            physical_tail_parameters=r['physical_tail_parameters'],physical_tail_cut=r['physical_tail_cut'],
            coefficient_chunks=self.terminal['coefficient_chunks'],
            source_reference_evaluation='Original PlanarSupportCore.evaluate / normal_geometry; original adaptive Flow.geo and all 25-state physical quintic; original height_integral for the omitted mean height.',
            artificial_raw_or_lambda_metadata_added=False,new_core_target_selected=False,
            new_primary_matching_q_selected=False,initializer_projected=False,
            native_reference_constructed_in_this_run=False,
            higher_modes='Not enabled. A later M16 initializer must separately document exact zero embedding and its new coordinate/space choices.',
            BVP_solver_invoked=False,actual_tail_solver_invoked=False,
            continuous_error_certificate=False)


def bind_reference(checkpoint,terminal_record,source_topic,short_bridge):
    checkpoint,terminal_record,source_topic,short_bridge=map(lambda p:Path(p).resolve(),
        (checkpoint,terminal_record,source_topic,short_bridge))
    if sha(checkpoint)!=CHECKPOINT_SHA256:
        raise ValueError('Use the completed genuine q060 saved-inner anchor')
    record,terminal=load(checkpoint),load(terminal_record)
    if terminal['checkpoint']!=ref(checkpoint) or terminal['solver_success'] is not True:
        raise ValueError('The terminal source record belongs to another candidate')
    cfg=record['config']
    if (record['solver_success'] is not True or cfg['core_kind']!='adaptive_warped_support' or
            cfg['base_mode']!=3 or cfg['modes']!=8 or cfg['fixed_metric'] is not False or
            cfg['actual_nonlinear_tail'] is not True or cfg.get('exact_core_lift') or
            'core_round_settings' in record):
        raise ValueError('This interface is solely the actual M8 cosine reference')
    if (record['actual_primary_amplitude']!=.06 or record['gauge_amplitude']!=.06 or
            record['warp_reference_q']!=.06 or len(record['parameters'])!=8 or
            len(record['central_correction_scales'])!=7 or record['nodes']!=1934):
        raise ValueError('Original q060 dimensions/gauges are required')
    actual=np.asarray(record['parameters'][1:])*np.asarray(record['central_correction_scales'])
    if not np.array_equal(np.r_[.06,actual],np.asarray(terminal['full_support_coefficients'])):
        raise ValueError('The full seven physical controls differ')
    raw_ref=terminal['saved_outer1']['raw_inner']
    if sha(raw_ref['path'])!=raw_ref['sha256']:raise ValueError('The original raw saved point changed')
    raw=load(raw_ref['path']);inputs=copy.deepcopy(raw['inputs'])
    for value in inputs.values():
        if sha(value['path'])!=value['sha256']:raise ValueError('An original input changed')
    if (raw['candidate_frozen_profile']!=record['frozen_profile'] or
            load(inputs['chart']['path'])!=record['chart'] or
            inputs['linear_port']['sha256']!=record['physical_port_sha256']):
        raise ValueError('Original profile/chart/port identity differs')
    for chunk in record['pp_coefficient_chunks']:
        if sha(checkpoint.parent/chunk['file'])!=chunk['sha256']:
            raise ValueError('The complete original polynomial chunk changed')
    sources=dict(terminal['source_sha256']);current={}
    for relative,digest in SUPPORTED_REFERENCE_SOURCES.items():
        path=source_topic/relative
        if sha(path)!=digest:raise ValueError('Unsupported original reference source: '+relative)
        current[str(path)]=digest
    if sha(short_bridge)!=SHORT_BRIDGE_SHA256:raise ValueError('Original short bridge changed')
    current[str(short_bridge)]=SHORT_BRIDGE_SHA256;sources.update(current)
    bound=CosineReferenceBinding(checkpoint,terminal_record,source_topic,short_bridge,
                                 record,terminal,inputs,sources,current)
    bound.check_sources()
    return bound


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for key in ('checkpoint','terminal-record','source-topic','short-bridge','output'):
        parser.add_argument('--'+key,type=Path,required=True)
    args=parser.parse_args()
    if args.output.exists():raise FileExistsError('Use a fresh binding file')
    bound=bind_reference(args.checkpoint,args.terminal_record,args.source_topic,args.short_bridge)
    result=bound.descriptor();result['reader']=ref(__file__)
    result['command']=[sys.executable,*sys.argv]
    with args.output.open('x') as stream:
        json.dump(result,stream,indent=2,allow_nan=False);stream.write('\n')
    print(json.dumps(dict(output=str(args.output),sha256=sha(args.output),
                         metadata_binding_only=True,modes=8,state_components=25)))


if __name__=='__main__':main()
