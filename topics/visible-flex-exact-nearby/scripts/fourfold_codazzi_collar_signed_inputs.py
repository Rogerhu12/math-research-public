"""Whole original natural signed background, fold and numerator admission."""
from fractions import Fraction as Q
from hashlib import sha256
import gzip,json
from flint import arb
import fourfold_codazzi_root_Laurent_Taylor_algebra as L
import fourfold_codazzi_true_characteristic_seed_admission as S
import fourfold_codazzi_collar_signed_helper_admission as H
from fourfold_codazzi_true_phase_original_inputs import check

BASE=S.TOPIC+'/notes/correlated_first_Airy_local_numerator_ci/run-43666374252-1/'
FILES={'native':('consumers/correlated-first-Airy-local-numerator.json.gz',60456,'fbe1bce690f33335d2b024fe38a751743e0017e7d275b4d1fb0712be155f177e'),
       'process':('consumers/process.json',34986,'6396a554ab8401d709744b47315ab73830dfe2051937a980ecaab0efa8fc82db'),
       'pub':('publication.json',13844,'41e83e4a927f2bd7c71ff4ec365727cf568c5b54b378dc3a9e4802b1ce1a6b02')}

def receive(read):
    receipts=[]
    def get(fn,n,s):
        b=read(S.HISTORY,BASE+fn)
        check((len(b),sha256(b).hexdigest())==(n,s),'whole original numerator '+fn)
        receipts.append(dict(path=BASE+fn,bytes=n,sha256=s))
        return json.loads(gzip.decompress(b) if fn.endswith('.gz') else b)
    doc,proc,pub=[get(*FILES[k]) for k in ('native','process','pub')]
    check(doc['complete'] and doc['proved'] and not doc['failure'] and doc['run_id']==proc['run_id']
          and str(doc['run_id'])=='43666374252' and str(doc['run_attempt'])=='1'
          and proc['actual_returncode']==0 and proc['mathematical_proved'] and proc['mathematical_complete']
          and proc['native_sha256']==FILES['native'][2] and doc['original_extension_native_sha256']==S.FIXED['native'][2]
          and pub['complete'] and pub['actual_returncode']==0 and all(v['passed'] for v in doc['gates'])
          and doc['exact_root_interval']==list(S.ROOT) and doc['algebra_sha256']==S.ALGEBRA
          and doc['complete_branch_identity']['Nraw_a_minus']=='-Nraw_a_plus'
          and doc['complete_branch_identity']['Nraw_b_minus']=='Nraw_b_plus','original entire true local numerator family')
    table={r['file']:r for r in pub['files']}
    def stage(n):
        e=doc['stages'][n];k='consumers/stages/'+n+'.json.gz';r=table[k]
        check(e['file']=='stages/'+n+'.json.gz' and r['bytes']==e['bytes'] and r['sha256']==e['sha256'],
              'unchanged complete original numerator publication')
        d=get(k,e['bytes'],e['sha256'])
        check(d['stage']==n and d['complete'] and d['stage_kind']==e['stage_kind'] and
              all(d[k]==doc[k] for k in ('source_sha256','input_manifest_sha256','algebra_sha256','runtime',
                                        'original_extension_native_sha256','original_larger_fold_native_sha256')),
              'original local numerator natural header')
        return d['payload']
    raw={k:[] for k in ('Nraw_a','Nraw_b')}
    for n in range(11):
        r=stage('correlated-local-numerator-degree-%03d'%n)
        check(r['degree']==n and r['complete_signed_operator_sum_before_norm'],'true stored signed Nraw')
        for k in raw:raw[k].append(L.LP.restore(r[k]))
    mult=stage('complete-local-numerator-whole-product-multipliers')
    mr=Q(mult['exact_common_product_rho_radius']);ms=Q(mult['exact_common_product_phi_width'])
    coef={k:arb(v['ball']).upper() for k,v in mult['complete_multiplier_bounds'].items()}
    z=proc['new_complete_correlated_Nraw_budgets'][0];outer=Q(z['exact_physical_rho_cover_radius'])
    check(Q(z['exact_output_phi_width'])==0 and z['residual_Taylor_order']==10 and mr==Q(1,6000) and ms==Q(1,128),
          'full old signed inner radius and strip')
    ntail={}
    for budget in proc['new_complete_correlated_Nraw_budgets']:
        w=Q(budget['exact_output_phi_width'])
        check(Q(budget['exact_physical_rho_cover_radius'])==outer and budget['residual_Taylor_order']==10,
              'complete naturally split numerator tails on the same root radius')
        ntail[w]={'Nraw_'+k:arb(budget['complete_finite_and_infinite_parts']['strip_sup'][k]['0']['complete_infinite_radial_and_angular_tail']).upper() for k in ('a','b')}
    names=['complete-background-root-series','complete-local-operator-series','helper-complete-vartheta-Q-through-twelve']
    leading=('T','Q','Xp','a0','b0')
    names+=['fold-degree-%03d'%i for i in range(15)]+['leading-complete-'+k for k in leading]
    names+=['leading-%s-degree-%03d'%(k,i) for k in leading for i in range(9,15)]
    for i in range(13):names+=['normalized-forcing-degree-%03d'%i,'first-correction-degree-%03d'%i]
    for i in range(9,15):names+=['background-inputs-degree-%03d'%i,'background-main-degree-%03d'%i]
    sel,ma,ids=H.admit(read,names);receipts+=ids
    check(len({r['path'] for r in receipts})==len(receipts),'distinct original whole records')
    bg=sel['complete-background-root-series']
    check(all(bg[k] for k in ('complete_mean_at_all_orders_retained','positive_order_value_repair_derivatives_exactly_zero',
                             'original_65_and_193_rows_retained','zero_bump_germ_and_fixed_eta0')),'original full repair and direction')
    c={k:L.unpack_series(v) for k,v in bg['series'].items()}
    for n in range(9,15):
        ri=sel['background-inputs-degree-%03d'%n];rm=sel['background-main-degree-%03d'%n]
        check(ri['degree']==rm['degree']==n,'same one-sided physical degree')
        for k in ('K','beta','gamma','s','u','v','k'):c[k].append(L.LP.restore(ri['coefficients'][k]))
        for k in ('eta','a','S'):c[k].append(L.LP.restore(rm[k]))
    arr={'chi':[L.LP.restore(sel['fold-degree-%03d'%i]['chi']) for i in range(15)]}
    for k in leading:
        h=sel['leading-complete-'+k];check(h['name']==k,'correct whole leading field')
        arr[k]=L.unpack_series(h['coefficients'])
        for i in range(9,15):
            r=sel['leading-%s-degree-%03d'%(k,i)];check(r['degree']==i and r['name']=='leading-'+k,'correct signed leading coefficient')
            arr[k].append(L.LP.restore(r['coefficient']))
    for k,key,stem in [('fa','fa','normalized-forcing'),('fb','fb','normalized-forcing'),('w1a','a1','first-correction'),('w1b','b1','first-correction')]:
        arr[k]=[L.LP.restore(sel[stem+'-degree-%03d'%i][key]) for i in range(13)]
    arr['d']=c['d'];arr['T0']=L.unpack_series(sel['complete-local-operator-series']['T0'])
    # This helper belongs to the Taylor extension (stored there, not recomputed).
    arr['vq']=L.unpack_series(sel['helper-complete-vartheta-Q-through-twelve']['coefficients'])
    oldmaj={}
    for k,m in dict(chi='chi',T='T',Q='Q',Xp='Xp',a0='a0',b0='b0',w1a='w1a',w1b='w1b',fa='f0',fb='f1').items():
        oldmaj[k]=(arb(ma[m][0]['ball']).upper(),Q(ma[m][1]),Q(ma[m][2]))
    for k,M in [('d',coef['C11']/2),('T0',coef['C10']),('vq',coef['Cba'])]:oldmaj[k]=(M,mr,ms)
    return c,arr,oldmaj,raw,ntail,outer,receipts
