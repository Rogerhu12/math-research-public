"""Restore only the original necessary five-field signed GRQ scientific input."""
from pathlib import Path
from fractions import Fraction as Q
from hashlib import sha256
from importlib.metadata import version
from math import isfinite
from argparse import ArgumentParser
import os,gzip,sys,json
from flint import arb,ctx
from fourfold_codazzi_true_phase_original_inputs import check
from fourfold_codazzi_true_characteristic_seed_admission import ROOT
from fourfold_codazzi_true_ratio_live_rules import gate,canonical
from fourfold_codazzi_true_ratio_restore_inputs import original,GCS,GPR,PHASE
from fourfold_codazzi_true_ratio_cut_and_reference import Phase,cut_ratio,subcells,file_sha,GCS_RUN
from fourfold_codazzi_true_ratio_label_quadrature import KEYS,L,BOX,boxes,selected_model_inputs,physical_output
from fourfold_codazzi_true_ratio_physical_packets import prepare
from fourfold_codazzi_true_ratio_label_mesh import M,CELLS,label_jet,project_to_labels
from fourfold_codazzi_signed_density_transport_arithmetic import exact,hull

GRQ=('46139062783','aaeae03b0671370319293acf7161cf65c8993f18',2537,
     'ea20996adecf10de592c38781ce8ed1c216a676cfc3833c9f58ea06de5ab6a2c',
     'full-signed-first-ratio/8_Integrate all four genuine first-ratio branches and their real physical reconstructions.txt',
     'GRQ_WHOLE_SMALL_RECEIPT')
CARRIER='true-complete-first-ratio.bin.gz'
WHOLE=(176771817,'53ae13a142f80d2bedd98beb7d9c4bc09a385dc464fdeb47dcc0ec11601275fd',219304395,
       '8f751b31e40a3c79a1996f05deb3d9f4124cf42856e802cc58ac8e080c81f003')
PLAN_SHA='320a3a58945287a56b25a5d69315a63679621228e382721a91ac28b7d9f6cdfa'


def plan_header(inp):
    rl,rh=map(Q,ROOT)
    plan=[(i,l,r) for i,(lo,hi,_,_) in enumerate(inp.plan) for l,r in subcells(lo,hi,rl)]
    ps=[[i,str(l),str(r)] for i,l,r in plan]
    check(len(plan)==3056 and sha256(canonical(ps)).hexdigest()==PLAN_SHA,'same entire original physical plan')
    identity=dict(schema='GRQ-1',run=GRQ[0],attempt=1,cut=str(inp.plan[0][1]),physical_cells=CELLS,
        fixed_label_cells=CELLS,angular_order=M,fields=list(KEYS),root=list(ROOT),source_phase_run=GPR[0],
        source_phase_receipt=GPR[3],source_cut_run=GCS_RUN,
        signed_continuation='at epsilon=+, R_sigma=i*sigma*rplus(sigma*phi); a1 is i times the stored real jet',
        storage='per inward piece then named field then centered bin then normalized jet: little-endian real f64 lo,hi',subpieces=ps)
    return plan,canonical(identity)


def restore(a):
    check(os.environ['GITHUB_ACTIONS']=='true' and os.environ['GITHUB_REPOSITORY']=='Rogerhu12/math-research-public'
          and os.environ['GITHUB_RUN_ATTEMPT']=='1' and sys.version_info[:3]==(3,12,14)
          and version('python-flint')=='0.9.0' and version('numpy')=='2.3.5','original public directed runtime')
    ctx.prec=320;ctx.cap=16
    small,d=original(a.logs,GRQ);(a.parents/'grq-receipt.json').write_bytes(small)
    check(d['all_four_real_branches'] and d['physical_subpieces']==d['completed_subpieces']==3056
        and d['native_original_cells']==3026 and d['old_scientific_targets_recomputed']==0
        and d['input_phase_receipt']==GPR[3] and d['phase_run']==GPR[0] and d['original_cut_run']==GCS_RUN
        and d['plan_sha256']==PLAN_SHA and tuple(d[k] for k in ('private_bytes','private_sha256',
            'private_uncompressed_bytes','private_uncompressed_sha256'))==WHOLE,'actual successful original GRQ result')
    tmp=a.parents/(CARRIER+'.partial');out=a.parents/CARRIER
    if out.exists():
        check(out.stat().st_size==WHOLE[0] and file_sha(out)==WHOLE[1],'existing whole private original')
        return
    ps=(a.parents/'gpr-receipt.json').read_bytes()
    check(sha256(ps).hexdigest()==GPR[3] and json.loads(ps)['private_carrier']==PHASE,'whole actual GPR receipt')
    inp,z,km,ids=selected_model_inputs(a.repo);plan,header=plan_header(inp)
    check(sha256(canonical(ids)).hexdigest()==json.loads(ps)['original_receipts_sha256'],'same 176 original whole inputs')
    phase=Phase(a.parents/'true-phase-inward-complete.bin.gz',PHASE,inp.plan)
    rcut,pref=cut_ratio(a.parents/'true-signed-cut-seed.bin.gz');rl,rh=map(Q,ROOT)
    state=U=E=None;idx=-1;hh=sha256();size=0
    with tmp.open('xb') as g:
        def write(raw):
            nonlocal size
            hh.update(raw);size+=len(raw);g.write(gzip.compress(raw,compresslevel=1,mtime=0))
        write(L.pack(len(header))+header)
        for count,(i,l,r) in enumerate(plan,1):
            gate()
            cell=inp.plan[i];lo,hi=cell[:2]
            if i!=idx:q,errors=phase.row();idx=i
            rho0=hull(rl-r,rh-r);rr=hull(rl-r,rh-l)
            if state is None:
                im,ps,co,_,_,state,m=prepare(inp,z,km,cell,r,r,(rho0,rho0),q,errors,arb(0),None)
                U=project_to_labels(im,[label_jet([v-u for v,u in zip(x,y)],p)
                                   for x,y,p in zip(rcut,co,ps)])
                E=pref*(-m["K"]).sqrt().sqrt()
                check(E.lower()>0,"actual positive E scalar at cut")
            tau=hull((hi-r)/(hi-lo),(hi-l)/(hi-lo))
            images,p,corr,src,fields,state,m=prepare(inp,z,km,cell,l,r,(rho0,rr),q,errors,tau,state)
            src=project_to_labels(images,src)
            h=exact(r-l)
            right=[[v+h*w for v,w in zip(x,y)] for x,y in zip(U,src)]
            whole=[[v.union(w) for v,w in zip(x,y)] for x,y in zip(U,right)]
            Enext=E*(2*h*m["beta_mean_S"]).exp()
            Ew=E.union(Enext)
            rplus,wa,wb=physical_output(whole,images,p,corr,fields,m,Ew)
            write(b''.join(boxes(row) for field in (whole,src,rplus,wa,wb) for row in field))
            U,E=right,Enext
            if count%512==0:print('GFW_NECESSARY_GRQ_RAW_ROWS',count,flush=True)
    phase.close()
    check((tmp.stat().st_size,file_sha(tmp),size,hh.hexdigest())==WHOLE,'both complete original byte identities before new mathematics')
    tmp.replace(out);print('GFW_RESTORED_ORIGINAL_GRQ',GRQ[0],WHOLE,'old_science_reawarded',0,flush=True)


class Ratio:
    def __init__(self,path,inp):
        check(path.stat().st_size==WHOLE[0] and file_sha(path)==WHOLE[1],'whole original compressed first-ratio input')
        plan,header=plan_header(inp);self.plan=plan
        self.f=gzip.open(path,'rb');n=self.f.read(4);size,=L.unpack(n);raw=self.f.read(size)
        check(raw==header,'same complete actual root, all four signs and original physical lift')
        self.h=sha256(n+raw);self.size=4+size;self.count=0

    def row(self,decode=True):
        stride=CELLS*(M+1)*BOX.size
        whole=self.f.read(len(KEYS)*stride);check(len(whole)==len(KEYS)*stride,'all five complete original scientific fields')
        self.h.update(whole);self.size+=len(whole);self.count+=1
        if not decode:return None
        offset=KEYS.index('R_plus_physical')*stride
        result=[]
        for i in range(CELLS):
            vals=[]
            for j in range(M+1):
                lo,hi=BOX.unpack_from(whole,offset);offset+=BOX.size
                check(isfinite(lo) and isfinite(hi) and lo<=hi,'complete original signed physical-angle ratio interval')
                vals.append(arb(lo).union(arb(hi)))
            result.append(vals)
        return result

    def close(self):
        check(not self.f.read(1) and self.count==len(self.plan) and (self.size,self.h.hexdigest())==WHOLE[2:],
              'entire original ratio byte stream and physical EOF')
        self.f.close()


if __name__=='__main__':
    p=ArgumentParser()
    for x in ('repo','logs','parents'):p.add_argument('--'+x,required=True,type=Path)
    restore(p.parse_args())
