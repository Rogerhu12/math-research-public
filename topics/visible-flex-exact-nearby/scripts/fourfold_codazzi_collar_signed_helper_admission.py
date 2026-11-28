"""Read the uniquely identified signed vartheta-Q helper at its actual Taylor lineage."""
from hashlib import sha256
import gzip,json
import fourfold_codazzi_true_characteristic_seed_admission as S

HELPER='helper-complete-vartheta-Q-through-twelve'
BYTES=241693
SHA='ede1bbd9a53babc6ba7a413cf0ced5348aecadb99ede50a17234584195da203f'


def admit(read,names):
    S.check(list(names).count(HELPER)==1,'one exact signed vQ natural helper')
    ordinary=[k for k in names if k!=HELPER]
    sel,major,ids=S.admit(read,ordinary)
    def get(path,size,digest):
        raw=read(S.HISTORY,path)
        S.check(len(raw)==size and sha256(raw).hexdigest()==digest,'complete checked helper provenance '+path)
        return json.loads(gzip.decompress(raw) if path.endswith('.gz') else raw)
    n=get(*S.FIXED['native']);pub=get(*S.FIXED['publication'])
    e=n['stages'][HELPER];rel='consumers/stages/'+HELPER+'.json.gz';path=S.TAYLOR+rel
    rows=[r for r in pub['files'] if r['file']==rel]
    S.check(len(rows)==1 and e['file']=='stages/'+HELPER+'.json.gz' and
            rows[0]['bytes']==e['bytes']==BYTES and rows[0]['sha256']==e['sha256']==SHA and
            e['stage_kind']=='new_unsaved_helper' and HELPER not in n['original_stages'],
            'original complete helper publication and original Taylor-extension class')
    h=get(path,BYTES,SHA)
    S.check(h['complete'] and h['stage']==HELPER and h['stage_kind']==e['stage_kind'] and
            all(h[k]==n[k] for k in ('algebra_sha256','runtime','source_sha256','input_manifest_sha256',
                                      'original_Taylor_native_sha256','higher_intrinsic_native_sha256')) and
            h['algebra_sha256']==S.ALGEBRA and len(h['payload']['coefficients'])==13,
            'signed helper source, manifest, two prior native edges and full degree twelve')
    sel[HELPER]=h['payload'];ids.append(dict(path=path,bytes=BYTES,sha256=SHA))
    S.check(len(sel)==len(names) and len(set(k['path'] for k in ids))==len(ids),'whole selected natural inventory')
    return sel,major,ids
