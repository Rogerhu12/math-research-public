#!/usr/bin/env python3
"""Read the completed original weight-eleven log; never rebuild a matrix.

Author: Astra-ISP-347c-20261126 / root; AI-assisted GPT-6 Astra Pro.
The output contains execution identities, scalar ranks and hashes only.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

def need(value, message):
    if not value:
        raise ValueError(message)

def identity(path):
    raw=Path(path).read_bytes()
    return {'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--job-log',type=Path,required=True)
    ap.add_argument('--repo',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    a=ap.parse_args()
    records=[]
    for line in a.job_log.read_text().splitlines():
        m=re.fullmatch(r'\d{4}-\d{2}-\d{2}T[^ ]+Z (\{.*\})',line)
        if m:
            try:
                records.append(json.loads(m.group(1)))
            except json.JSONDecodeError:
                pass
    def one(key,value):
        matches=[x for x in records if x.get(key)==value]
        need(len(matches)==1,'one complete '+value)
        return matches[0]
    frozen=one('event','frozen-input-sources')
    inp=one('event','complete-original-weight11-input')
    final=one('kind','weight11_projected_augmented_result')
    done=one('event','complete-weight11-execution')
    need(frozen['sourceCommit']=='52d167bb4346eaa4232ad567a1d0f5f9f6eaea99','original source commit')
    need(frozen['count']==13,'all immutable source files')
    need(inp['sourceTerms']==8037189 and inp['targetTerms']==[1008,952,1008,1008],'complete original coefficient stream')
    need(inp['canonicalNormalizationDet127']==74,'unchanged canonical four-dimensional target space')
    need(final['complete_original_sources'] is True,'complete original sources')
    need(final['original_source_columns']==37568 and final['projection_rows']==40000 and final['hashes_per_original_row']==5,'original complete dimensions')
    need(final['source_rank_lower_bound']==36782 and final['augmented_rank_lower_bounds']==[36783,36784,36785,36786],'actual exact rank lower bounds')
    need(final['selected_projected_minor_det127']==45 and final['four_class_threshold_reached'] is True,'nonzero full selected minor')
    need(done['sourceRankLowerBound']==final['source_rank_lower_bound'] and done['augmentedRankLowerBounds']==final['augmented_rank_lower_bounds'],'native and whole runner agree')
    native_return=[x for x in records if x.get('event')=='child-return' and x.get('name')=='new-weight11-full-augmented-rank']
    need(len(native_return)==1,'one actual native return')
    native_return=native_return[0]
    need(native_return['exitCode']==0 and native_return['outerBudget'] is False,'completed rather than timed-out native computation')
    need(done['nativeLog']==native_return['log'],'same complete native log')
    notes=a.repo/'topics/invariant-subspace-problem/notes'
    request_path=notes/'2026-11-20-r150-weight11-projected-rank-request-b2a9.json'
    request=json.loads(request_path.read_text())
    need(request['sequence']==3,'request three')
    need(request['originalInput']=={'rows':150646,'sourceColumns':37568,'generators':200,'generatorTerms':8037189,'targets':'the four fixed original canonical q_j(y)*b^3*e0','weight':11,'prime':127,'coefficientRoot':100},'same original input')
    sources={
        'runner':('2026-11-20-r150-weight11-projected-rank-runner-b2a9.py',request['runnerSHA256']),
        'native':('2026-11-20-r150-weight11-projected-rank-b2a9.cpp',request['nativeSHA256']),
        'arithmetic':('2026-11-15-r150-original-f127-bitplane-789f.hpp',request['bitplaneHeaderSHA256']),
    }
    verified={}
    for label,(name,sha) in sources.items():
        item=identity(notes/name)
        need(item['sha256']==sha,'unchanged '+label+' source')
        verified[label]={'path':name,**item}
    result={
        'format':'isp-completed-weight11-log-audit-20261126-v1',
        'author':'Astra-ISP-347c-20261126 / root; AI-assisted GPT-6 Astra Pro',
        'runId':44732018666,'jobId':136273939599,
        'runUrl':'https://github.com/Rogerhu12/math-research-public/actions/runs/44732018666/job/136273939599',
        'completedAtUtc':'2026-11-20T16:03:56Z',
        'sourceCommit':frozen['sourceCommit'],
        'request':{'path':request_path.name,**identity(request_path)},
        'sources':verified,'retrievedDecodedJobLog':identity(a.job_log),
        'originalInput':inp,'nativeResult':final,'wholeExecution':done,
        'nativeExitCode':native_return['exitCode'],
        'nativeExactElapsedSeconds':native_return['elapsedSeconds'],
        'auditSource':{'path':Path(__file__).name,**identity(Path(__file__))},
        'onlyReadExistingLog':True,'matricesRecomputed':False,'arraysStored':False,
        'scope':'The mathematical characteristic-zero conclusions also use the independently proved source-rank ceiling; the row projection alone supplies only rank lower bounds.'
    }
    a.output.write_text(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)+'\n')
    print(json.dumps({'status':'completed-original-log-recovered','sourceRank':36782,'augmentedRanks':[36783,36784,36785,36786],'det127':45,'output':str(a.output)},sort_keys=True))

if __name__=='__main__':
    main()
