#!/usr/bin/env python3
"""Append missing original background profiles without recomputing old ones.

The original hash-bound primitive contains the exact frozen parameter recipe.
All integral/alpha/calibration/source identities are rechecked against its
published provenance. No synthetic checkpoint or changed metric is created.
"""
import argparse,copy,gzip,hashlib,importlib.util,json,sys,time
from pathlib import Path

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
    b=Path(p).read_bytes();return json.loads(gzip.decompress(b) if b[:2]==b'\x1f\x8b' else b)
def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ('scripts','parent','out'):ap.add_argument('--'+name,type=Path,required=True)
    ap.add_argument('--depth',type=int,default=8);a=ap.parse_args();start=time.monotonic()
    if a.out.exists():raise FileExistsError('Fresh original-source primitive output required')
    if sha(a.parent)!='28577da04035f91bcd5dc310094d5844347cbeb78d6213dcba0232b62acf56e9':raise ValueError('Original complete depth4 primitive required')
    old=read(a.parent);notes=a.scripts.parent/'notes'
    if not old['finished'] or old['settings']['depth']!=4 or not 4<a.depth<=16:raise ValueError('Only an explicit complete deeper extension is supported')
    for name,digest in old['sources'].items():
        if sha(a.scripts/name)!=digest:raise ValueError('Frozen original implementation changed '+name)
    inputs={}
    for name in ('calibrations','alpha','cell_zero_A','inner_A','outer_B'):
        path=notes/Path(old['inputs'][name]['file']).name
        if sha(path)!=old['inputs'][name]['sha256']:raise ValueError('Frozen proof input changed '+name)
        inputs[name]=read(path)
    checkpoint=old['inputs']['checkpoint']['sha256'];calsha=old['inputs']['calibrations']['sha256']
    for name in ('cell_zero_A','inner_A','outer_B'):
        d=inputs[name]
        if d['checkpointSHA256']!=checkpoint or d.get('calibrationsSHA256',d.get('calibrationTableSHA256'))!=calsha:raise ValueError('Exact original integral source binding differs')
    al=inputs['alpha']
    if al['inputs']['checkpoint']['sha256']!=checkpoint or al['inputs']['calibrations']['sha256']!=calsha or al['exactRadialAlpha']!=old['alpha']:
        raise ValueError('Original calibrated alpha binding differs')
    sys.path.insert(0,str(a.scripts))
    from db6f_tail_interval_elementary import I
    from db6f_tail_interval_source_stable import FrozenSource
    from db6f_tail_background_primitive import build_profile,strong_profile_anchors
    p=old['parameters'];alpha=I(*old['alpha']);model=FrozenSource(p,inputs['calibrations'])
    anchors=strong_profile_anchors(p,old['alpha'],inputs['cell_zero_A'],inputs['inner_A'],inputs['outer_B'],a.depth)
    for profile in old['profiles']:
        if profile['anchor']!=anchors[(profile['n'],profile['segment'])]:raise ValueError('Recomputed exact anchor differs from original completed profile')
    out=copy.deepcopy(old);out['settings']['depth']=a.depth;out['finished']=False
    out['extension']={'script_sha256':sha(__file__),'parent_sha256':sha(a.parent),'parent_complete_profiles':len(old['profiles']),
      'original_parameter_recipe_copied_exactly':True,'actual_checkpoint_not_reconstructed_or_changed':True,
      'all_original_integral_and_source_identities_rechecked':True,'new_profiles':[]}
    def write():
        out['extension']['seconds']=time.monotonic()-start
        payload=json.dumps(out,separators=(',',':'),allow_nan=False).encode();a.out.write_bytes(gzip.compress(payload,mtime=0))
    write()
    for n in range(4,a.depth):
        for j in range(9):
            profile=build_profile(model,alpha,n,j,anchors[(n,j)],order=old['settings']['order'],density=old['settings']['density'])
            out['profiles'].append(profile);out['extension']['new_profiles'].append([n,j]);write()
            print(json.dumps({'n':n,'segment':j,'analytic_leaves':profile['analyticLeaves'],'range_leaves':profile['rangeLeaves'],'seconds':time.monotonic()-start}),flush=True)
    if out['profiles'][:len(old['profiles'])]!=old['profiles']:raise ArithmeticError('An already registered original profile changed')
    if {(x['n'],x['segment']) for x in out['profiles']}!={(n,j) for n in range(a.depth) for j in range(9)}:raise ArithmeticError('Incomplete original background extension')
    out['finished']=True;write();print(json.dumps({'complete':True,'profiles':len(out['profiles']),'sha256':sha(a.out),'bytes':a.out.stat().st_size,'seconds':out['extension']['seconds']}),flush=True)
if __name__=='__main__':main()
