#!/usr/bin/env python3
"""Generate complete three-phase meshes of one continuously certified field.

The original complete material-angle STL generator is used unchanged.
Only actual repeated knots and exact-value source caching are adapted.
Full metric and all-phase geometry receipts must identify the same field.
The triangle meshes remain finite numerical representatives, not a new
proof of continuous isometry or of discretization convergence.
"""
from __future__ import annotations
import argparse,hashlib,importlib.util,json,sys
from fractions import Fraction as Q
from pathlib import Path

STL_SHA='0dacc33668048a650e0d7aec63ba57f3906c70e0a247852bf2df0e64f9d6fbfa'
CACHE_SHA='b69d67754d935a4e4342c934f80e5272d520f86164804c710350cf412a805745'
C2_SHA='34fb3936a57bef17ceb3c326bdfad885fe7372366e373030ec7a83a4202f8814'
METRIC_SHA='197a6696eae4f14723ef92a09c9543f102c789fef95d02fe1a751075e9d8e28d'
REGIONAL_SHA='0b62fcd84c7e19155197d6a2719ecd7484ecf515ca5f469fe4d56e52ea921296'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):return json.loads(Path(p).read_text())
def load(name,p):
    spec=importlib.util.spec_from_file_location(name,p)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

def main():
    ap=argparse.ArgumentParser(description=__doc__,add_help=False)
    ap.add_argument('--continuous-metric',type=Path,required=True)
    ap.add_argument('--continuous-geometry',type=Path,required=True)
    a,rest=ap.parse_known_args()
    parser=argparse.ArgumentParser(add_help=False)
    for key in ('scripts','grid','field','result','out'):parser.add_argument('--'+key,type=Path,required=True)
    b,_=parser.parse_known_args(rest)
    if '--geometry-report' in rest or '--reference-only' in rest:raise ValueError('Use actual full continuous receipts only')
    if b.out.exists() or any(b.out.parent.glob('entire-half-t*.stl')):raise FileExistsError('Fresh complete-mesh directory required')
    metric=read(a.continuous_metric);geometry=read(a.continuous_geometry);grid=read(b.grid)
    if metric['script_sha256']!=METRIC_SHA or geometry['script_sha256']!=REGIONAL_SHA:
        raise ValueError('Proved actual continuous producers required')
    for report in (metric,geometry):
        for key,path in [('field_sha256',b.field),('grid_sha256',b.grid),('solver_result_sha256',b.result)]:
            if report[key]!=sha(path):raise ValueError('Different actual certified field: '+key)
    if not metric['full_surface_certificate'] or not metric['covers_complete_moving_half_and_fixed_cuffs_caps_by_original_identity']:
        raise ValueError('Complete original-domain metric coverage required')
    if Q(metric['relative_metric_upper']['upper_exact'])>Q(1,10**6):raise ValueError('Continuous metric gate not established')
    if not geometry['whole_geometry_conditions'] or not geometry['same_actual_saved_field_no_refit']:
        raise ValueError('Whole continuous geometry is not established')
    quant=geometry['rational_quantities']
    if Q(quant['reach_over_D']['lower_exact'])<Q(3,100) or Q(quant['held_over_D']['lower_exact'])<Q(5,100):
        raise ValueError('Actual geometry thresholds not established')
    paths={'generator':b.scripts/'6a65-m12-entire-half-closed-stl.py',
           'cache':b.scripts/'2ecf-m12-h2-cached-direct-lm-v2.py',
           'basis':b.scripts/'2ecf-m12-h2-c2-direct-lm.py'}
    for name,expected in [('generator',STL_SHA),('cache',CACHE_SHA),('basis',C2_SHA)]:
        if sha(paths[name])!=expected:raise ValueError('Frozen mesh input helper changed: '+name)
    entry=load('complete_actual_closed_mesh',paths['generator'])
    cache=load('complete_mesh_exact_source_cache',paths['cache'])
    basis=load('complete_mesh_declared_C2_basis',paths['basis'])
    original_load=entry.load;receipts=[]
    def actual_load(name,path):
        m=original_load(name,path)
        if name=='closed_stl_whole':
            cache.cache_tail_apply(m.TailQueries,receipts)
            if 'unit_knots' in grid:
                factory=m.basis_for
                m.basis_for=lambda joint,mesh,order,chart:basis.checked_basis(factory,joint,mesh,order,chart,grid['unit_knots'])
        return m
    entry.load=actual_load;sys.argv=[str(paths['generator']),*rest];entry.main()
    original_report_sha=sha(b.out);report=read(b.out)
    report['originalMeshSchema']=report['schema'];report['originalMeshGeneratorSHA256']=report['scriptSHA256']
    report['schema']='2ecf-actual-certified-M12-complete-declared-basis-three-phase-mesh-v1'
    report['scriptSHA256']=sha(__file__);report['originalMeshReceiptBeforeBindingSHA256']=original_report_sha
    report['fullDeclaredKnotMultisetConsumed']=True
    report['continuousMetricReportSHA256']=sha(a.continuous_metric)
    report['continuousRegionalGeometryReportSHA256']=sha(a.continuous_geometry)
    report['continuousGeometryTransferChecksPassed']=True
    report['continuousRelativeMetricUpperExact']=metric['relative_metric_upper']['upper_exact']
    report['continuousReachOverDLowerExact']=quant['reach_over_D']['lower_exact']
    report['continuousHeldOverDLowerExact']=quant['held_over_D']['lower_exact']
    report['actualExactValueSourceCache']=receipts
    report['completeFixedMetricRefinementClaim']=False
    b.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'report':str(b.out),'sha256':sha(b.out),'meshes':report['meshFiles'],
        'sameActualContinuouslyCertifiedField':True,'fixedMetricConvergenceClaim':False}),flush=True)

if __name__=='__main__':main()
