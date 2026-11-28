#!/usr/bin/env python3
"""Run the true full-half field on the improved frozen W040 profile design, or on its original physical-profile parent."""
import argparse,hashlib,json,os,subprocess,sys
from pathlib import Path
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
    p=argparse.ArgumentParser()
    for k in ('whole-source','design-report','fallback-parent','out'):p.add_argument('--'+k,type=Path,required=True)
    a,rest=p.parse_known_args()
    if '--parent' in rest:raise ValueError('Choose the actual parent from the design report')
    fallback=sha(a.fallback_parent);chosen=a.fallback_parent;reason='original W040 three-profile parent, new design did not complete'
    metric=None
    if a.design_report.is_file():
        d=json.loads(a.design_report.read_text())
        if d['parentSHA256']!=fallback:raise ValueError('New design has a different physical parent')
        if d['accepted'] and d['finalFrozenCandidate']['peak']<d['initialIndependent']['peak']:
            candidate=a.design_report.with_suffix('.npz')
            if not candidate.is_file() or sha(candidate)!=d['stateSHA256']:raise ValueError('Completed design state differs')
            chosen=candidate;metric=d['chosenMetricSHA256'];reason='successful fine positive design reduced the independent metric peak'
        else:reason='original W040 three-profile parent, new design did not improve its independent peak'
    subprocess.run([sys.executable,str(a.whole_source),*rest,'--parent',str(chosen),'--out',str(a.out)],check=True)
    data=json.loads(a.out.read_text())
    if data['parentSHA']!=sha(chosen):raise ValueError('Whole field was not built on the selected state')
    data['parentSelection']=dict(reason=reason,fallbackSHA=fallback,chosenSHA=sha(chosen),newFrozenMetricSHA=metric,
        designReportSHA=(sha(a.design_report) if a.design_report.is_file() else None))
    temp=a.out.with_suffix('.annotated.tmp');temp.write_text(json.dumps(data,indent=2)+'\n');os.replace(temp,a.out)
if __name__=='__main__':main()
