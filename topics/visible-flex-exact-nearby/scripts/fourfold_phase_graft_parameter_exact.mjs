#!/usr/bin/env node
// R111: complete natural-graft comparison from the actual small R66 input.
// Run from the topic directory:
// node scripts/fourfold_phase_graft_parameter_exact.mjs . /tmp/R111-graft.json
// Optional fourth argument writes the complete diagnostic report locally.
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { fileURLToPath, pathToFileURL } from "node:url";

function certifyGraft(entry, options={}) {
  const digits=60n, S=10n**digits, ZERO={lo:0n,hi:0n}, ONE={lo:S,hi:S};
  const floor=(a,b)=>{if(b<0n){a=-a;b=-b;}let q=a/b,r=a%b;return r<0n?q-1n:q;};
  const ceil=(a,b)=>-floor(-a,b);
  const I=(lo,hi=lo)=>{if(lo>hi)throw Error("reversed interval");return {lo,hi};};
  function rational(s){
    s=String(s).trim();
    if(s.includes("/")){let[a,b]=s.split("/").map(rational);return [a[0]*b[1],a[1]*b[0]];}
    const m=s.match(/^([+-]?)(\d*)(?:\.(\d*))?(?:[eE]([+-]?\d+))?$/);
    if(!m||!(m[2]||m[3]))throw Error("bad rational "+s);
    let n=BigInt((m[2]||"0")+(m[3]||""));if(m[1]==="-")n=-n;
    let k=Number(m[4]||0)-(m[3]||"").length;
    return k>=0?[n*10n**BigInt(k),1n]:[n,10n**BigInt(-k)];
  }
  function q(s){const[n,d]=rational(s);return I(floor(n*S,d),ceil(n*S,d));}
  const add=(a,b)=>I(a.lo+b.lo,a.hi+b.hi);
  const neg=a=>I(-a.hi,-a.lo),sub=(a,b)=>add(a,neg(b));
  function mul(a,b){const z=[a.lo*b.lo,a.lo*b.hi,a.hi*b.lo,a.hi*b.hi];return I(floor(z.reduce((x,y)=>x<y?x:y),S),ceil(z.reduce((x,y)=>x>y?x:y),S));}
  function inv(a){if(a.lo<=0n&&a.hi>=0n)throw Error("zero divisor");return I(floor(S*S,a.hi),ceil(S*S,a.lo));}
  const div=(a,b)=>mul(a,inv(b));
  const scale=(a,n)=>mul(a,q(n));
  const absmax=a=>{const x=a.lo<0n?-a.lo:a.lo,y=a.hi<0n?-a.hi:a.hi;return x>y?x:y;};
  const upperabs=a=>I(absmax(a));
  const sym=a=>I(-absmax(a),absmax(a));
  const upper=a=>I(a.hi);
  function pow(a,n){let z=ONE;for(let j=0;j<n;j++)z=mul(z,a);return z;}
  function isqrt(n){if(n<0n)throw Error("negative sqrt");if(n<2n)return n;let x=1n<<BigInt((n.toString(2).length+1)>>1);for(;;){let y=(x+n/x)>>1n;if(y>=x)return x;x=y;}}
  function sqrt(a){if(a.lo<0n)throw Error("sqrt interval negative");const l=isqrt(a.lo*S),u=isqrt(a.hi*S);return I(l,u*u===a.hi*S?u:u+1n);}
  function exp(a){
    if(a.lo===0n&&a.hi===0n)return ONE;
    const y=div(a,q(128)),r=upperabs(y);
    if(r.hi>S)throw Error("exponential reduction outside unit disk");
    let term=ONE,sum=ONE,absolute=ONE;
    for(let k=1;k<=48;k++){term=div(mul(term,y),q(k));sum=add(sum,term);absolute=div(mul(absolute,r),q(k));}
    const tail=scale(div(mul(absolute,r),q(49)),3);
    sum=add(sum,sym(tail));
    if(sum.lo<=0n)throw Error("exponential failed positive gate");
    for(let k=0;k<7;k++)sum=mul(sum,sum);
    return sum;
  }
  function ball(v){
    let s=(typeof v==="object"?v.ball:String(v)).trim();
    if(s[0]!=="[")return q(s);
    let m=s.match(/^\[\s*([+\-0-9.eE]+)\s*\+\/-\s*([+\-0-9.eE]+)\s*\]$/);
    if(!m)throw Error("bad displayed ball "+s);
    const c=q(m[1]),r=upperabs(q(m[2]));return I(c.lo-r.hi,c.hi+r.hi);
  }
  const fmt=a=>({lower:a.lo.toString()+"/10^60",upper:a.hi.toString()+"/10^60",
                lower_approx:Number(a.lo)/1e60,upper_approx:Number(a.hi)/1e60});
  function constS(a,n){return Array.from({length:n},(_,j)=>j?ZERO:a);}
  const sadd=(a,b)=>a.map((x,i)=>add(x,b[i]));
  const sscale=(a,b)=>a.map(x=>mul(x,b));
  function smul(a,b){const n=a.length,z=constS(ZERO,n);for(let i=0;i<n;i++)for(let j=0;j<=i;j++)z[i]=add(z[i],mul(a[j],b[i-j]));return z;}
  function spow(a,k){let z=constS(ONE,a.length);for(let j=0;j<k;j++)z=smul(z,a);return z;}
  function sexp(a){let z=constS(ZERO,a.length);z[0]=exp(a[0]);for(let n=1;n<a.length;n++){let v=ZERO;for(let k=1;k<=n;k++)v=add(v,scale(mul(a[k],z[n-k]),k));z[n]=div(v,q(n));}return z;}
  function spol(c,s){let z=constS(c[c.length-1],s.length);for(let i=c.length-2;i>=0;i--)z=sadd(smul(z,s),constS(c[i],s.length));return z;}
  const sum=a=>a.reduce(add,ZERO),maximum=a=>a.reduce((x,y)=>x.hi>y.hi?x:y,ZERO);
  const checks=[];
  function check(name,v){checks.push({name,passed:!!v});if(!v)throw Error(name);}
  check("completed actual entry",entry.kind==="actual_affine_C4_exterior_entry_scalar_jets"&&entry.complete===true);
  check("actual original input",entry.origin_inputs_sha256==="0d17500ac49c845b402145c4d0a48170b7163ec0d7e6ed6f0eedcc1c649ca59b");
  check("actual direction",entry.direction_sha256==="8db5d57d65ea49cfe3a0df250714392300c98feeb2e0de2774aacbb4764d89ab");
  check("actual entrance",entry.entry.cut==="3"&&entry.entry.beta.length===24&&entry.entry.gamma.length===24);
  const delta=q("-7789843107295549/4611686018427387904"),eta=q("1/1000000000");
  const interval=[q(entry.exact_parameter_interval[0]),q(entry.exact_parameter_interval[1])];
  check("current entire eta contained in original family",sub(delta,eta).lo>interval[0].hi&&add(delta,eta).hi<interval[1].lo);
  const e=entry.entry,l=e.log_radius.map(ball),c=e.slope_ratio.map(ball),height=e.height.map(ball),ell=q("1/8");
  check("decreasing log radius",l[1].hi<0n);
  const normalized=(name,n)=>e[name].map(row=>smul(row.map(ball),sexp(sscale(l,q(-n)))));
  const bn=normalized("beta",3),gn=normalized("gamma",2);
  const lc=sum(l.slice(2).map((v,j)=>mul(upperabs(v),pow(ell,j+2))));
  const cc=sum(c.slice(1).map((v,j)=>mul(upperabs(v),pow(ell,j+1))));
  const Cglobal=add(c[0],sym(cc)),aglobal=exp(add(add(l[0],mul(l[1],I(0n,ell.hi))),sym(lc)));
  check("complete graft slope positive",Cglobal.lo>0n);
  const Zinc=mul(mul(ell,pow(aglobal,2)),upper(Cglobal));
  const Z=add(height[0],sym(Zinc));
  check("complete mean height positive",Z.lo>0n);
  function jets(a,b,d){
    const s=[I(floor(a*S,d),ceil(b*S,d)),ONE,ZERO],u=sscale(s,q(8));
    const one=constS(ONE,3),oneMinus=sadd(one,sscale(u,q(-1)));
    const chi=smul(spow(oneMinus,5),spol([q(1),q(5),q(15),q(35),q(70)],u));
    const correction=sadd(sadd(sscale(spow(s,2),l[2]),sscale(spow(s,3),l[3])),sscale(spow(s,4),l[4]));
    const loga=sadd(sadd(constS(l[0],3),sscale(s,l[1])),smul(chi,correction));
    const radius=sexp(loga);
    const C=sadd(constS(c[0],3),smul(chi,spol([ZERO,c[1],c[2],c[3]],s)));
    const physical=(rows,power)=>rows.map(row=>smul(smul(spow(radius,power),chi),spol(row,s)));
    return {a:radius[0],L:loga[1],Lp:scale(loga[2],2),C:C[0],Cp:C[1],
            beta:physical(bn,3),gamma:physical(gn,2)};
  }
  function form(j){
    const {a,L,Lp,C,Cp,beta,gamma}=j;
    const norms=rows=>[0,1,2].map(k=>upper(sum(rows.map(v=>upperabs(scale(v[k],k===2?2:1))))));
    const b=norms(beta),g=norms(gamma),la=upperabs(L),lpa=upperabs(Lp);
    // Entire real Wiener majorants. The jets are actual radial derivatives.
    const eb=exp(b[0]),emg=exp(neg(g[0])),epg=exp(g[0]),
          emb=exp(neg(b[0]));
    const cg=div(add(epg,emg),q(2)),sg=div(sub(epg,emg),q(2)),
          cb=div(add(eb,emb),q(2)),sb=div(sub(eb,emb),q(2));
    const ph=[
      sub(mul(cg,eb),ONE),
      mul(eb,add(mul(cg,b[1]),mul(sg,g[1]))),
      mul(eb,add(mul(cg,add(add(b[2],pow(b[1],2)),pow(g[1],2))),
                    mul(sg,add(g[2],scale(mul(b[1],g[1]),2)))))].map(upperabs);
    const pz=[sg,mul(cg,g[1]),add(mul(cg,g[2]),mul(sg,pow(g[1],2)))].map(x=>upperabs(div(x,q(4))));
    const p0=[
      sub(mul(cg,cb),ONE),
      add(mul(mul(sg,g[1]),cb),mul(mul(cg,sb),b[1])),
      add(add(mul(cb,add(mul(cg,pow(g[1],2)),mul(sg,g[2]))),
              scale(mul(mul(sg,sb),mul(g[1],b[1])),2)),
          mul(cg,add(mul(cb,pow(b[1],2)),mul(sb,b[2]))))].map(upperabs);
    const uh=add(mul(la,ph[0]),ph[1]),uz=add(mul(la,pz[0]),pz[1]);
    const urh=add(add(mul(lpa,ph[0]),mul(la,ph[1])),ph[2]);
    const urz=add(add(mul(lpa,pz[0]),mul(la,pz[1])),pz[2]);
    const u0=add(mul(la,p0[0]),p0[1]),ur0=add(add(mul(lpa,p0[0]),mul(la,p0[1])),p0[2]);
    const e0=add(add(scale(mul(la,u0),2),scale(pow(uh,2),2)),pow(uz,2));
    const e1=add(add(scale(mul(lpa,u0),2),scale(mul(la,ur0),2)),
                 scale(add(scale(mul(uh,urh),2),mul(uz,urz)),2));
    const E=add(add(pow(L,2),mul(pow(a,2),pow(C,2))),sym(e0));
    const correction=div(add(mul(la,e1),scale(mul(lpa,e0),2)),scale(pow(a,2),2));
    const numerator=add(add(mul(pow(C,2),sub(pow(L,2),Lp)),mul(mul(L,C),Cp)),sym(correction));
    if(E.lo<=0n||numerator.lo<=0n)throw Error("Wiener target K positivity unresolved");
    const curvature=div(numerator,pow(E,2));
    const bt=upper(sum(beta.map((v,i)=>scale(upperabs(v[0]),4*(i+1)))));
    const gt=upper(sum(gamma.map((v,i)=>scale(upperabs(v[0]),4*(i+1)))));
    const sinb=sym(b[0]),sing=sym(g[0]);
    const cosb=I(sub(ONE,div(pow(b[0],2),q(2))).lo,S);
    const cosg=I(sub(ONE,div(pow(g[0],2),q(2))).lo,S);
    const X0=add(L,sym(uh)),X1=sym(uh),Xz=add(C,sym(div(uz,a)));
    const h1=add(neg(mul(sinb,X0)),mul(cosb,X1));
    const v1=sub(neg(mul(cosb,X0)),mul(sinb,X1));
    const Q2=sub(mul(cosg,Xz),div(mul(sing,h1),a));
    const D=sub(mul(mul(add(ONE,sym(bt)),cosg),Q2),div(mul(sym(gt),v1),a));
    const M=sub(mul(mul(sym(b[1]),cosg),Q2),div(mul(sym(g[1]),v1),a));
    const W=add(pow(v1,2),mul(pow(a,2),pow(Q2,2)));
    const Fh=add(neg(mul(sinb,add(ONE,sym(ph[0])))),mul(cosb,sym(ph[0])));
    const Fv=sub(neg(mul(cosb,add(ONE,sym(ph[0])))),mul(sinb,sym(ph[0])));
    const Fz=add(Z,mul(a,sym(pz[0])));
    const Fq=sub(mul(cosg,Fz),mul(mul(a,sing),Fh));
    const H=sub(mul(Fq,v1),mul(mul(pow(a,2),Fv),Q2));
    if([a,D,W,H,Fz].some(x=>x.lo<=0n))throw Error("real complete grounded form denominator unresolved");
    const alpha=div(mul(pow(Fz,2),D),pow(H,2));
    const drift=neg(div(M,D));
    const kappa=div(mul(mul(pow(Fz,2),pow(W,2)),curvature),mul(D,pow(H,2)));
    if(alpha.lo<=0n||kappa.lo<=0n)throw Error("grounded form not positive");
    return [alpha,mul(alpha,drift),add(mul(alpha,pow(drift,2)),kappa)];
  }
  function compare(values){
    const [u,v,w]=values,mid=x=>I((x.lo+x.hi)/2n);
    const A=mid(u),b=mid(div(v,A)),K=mid(sub(w,mul(A,pow(b,2))));
    if(A.lo<=0n||K.lo<=0n)throw Error("constant reference not positive");
    const e11=sub(div(u,A),ONE);
    const e12=div(sub(v,mul(b,u)),sqrt(mul(A,K)));
    const e22=sub(div(add(sub(w,scale(mul(b,v),2)),mul(pow(b,2),u)),K),ONE);
    const t=maximum([add(upperabs(e11),upperabs(e12)),add(upperabs(e12),upperabs(e22))]);
    if(t.hi>=S)throw Error("reference radius >=1");
    const epsilon=div(scale(t,2),sub(ONE,t));
    return {epsilon,t,A,b,K};
  }
  const target=q(options.relative_target||"1/500"),maxDepth=options.max_depth??14;
  const pending=[{a:0n,b:1n,d:8n,depth:0}],rows=[],rejected=[],failed=[];
  let maximumE=ZERO,evaluations=0;
  const rf=(a,d)=>{let x=a<0n?-a:a,y=d;while(y){let t=x%y;x=y;y=t;}return String(a/x)+"/"+String(d/x);};
  while(pending.length){
    const box=pending.pop();let result,error;
    evaluations++;
    try{result=compare(form(jets(box.a,box.b,box.d)));if(result.epsilon.hi>target.lo)throw Error("relative fee exceeds target");}
    catch(e){error=String(e.message||e);}
    const range=[rf(3n*box.d+box.a,box.d),rf(3n*box.d+box.b,box.d)];
    if(error){
      const rec={radial_interval:range,depth:box.depth,reason:error};
      if(box.depth>=maxDepth)failed.push(rec);
      else{rejected.push(rec);pending.push({a:box.a+box.b,b:2n*box.b,d:2n*box.d,depth:box.depth+1},{a:2n*box.a,b:box.a+box.b,d:2n*box.d,depth:box.depth+1});}
    }else{
      if(result.epsilon.hi>maximumE.hi)maximumE=upper(result.epsilon);
      rows.push({radial_interval:range,depth:box.depth,relative_form_error:fmt(result.epsilon),
                 reference_relative_radius:fmt(result.t),A:fmt(result.A),b:fmt(result.b),K:fmt(result.K)});
    }
  }
  rows.sort((x,y)=>{const[a,b]=rational(x.radial_interval[0]),[c,d]=rational(y.radial_interval[0]);return a*d<c*b?-1:a*d>c*b?1:0;});
  let cursor=[3n,1n],continuous=true;
  for(const row of rows){const[a,b]=rational(row.radial_interval[0]),[c,d]=rational(row.radial_interval[1]);if(a*cursor[1]!==cursor[0]*b||a*d>=c*b)continuous=false;cursor=[c,d];}
  const complete=failed.length===0&&continuous&&cursor[0]*8n===cursor[1]*25n;
  check("complete exact [3,25/8] cover",complete);
  check("maximum strict relative form budget",maximumE.hi<=target.lo);
  return {kind:"actual_R66_whole_family_natural_graft_parameter_form_comparison",
          complete,body_complete:false,full_cap_complete:false,whole_eta_graft_complete:true,
          arithmetic:"directed BigInt fixed-point intervals, scale 10^60; exponential Taylor48 with entire tail and 7 squarings",
          original_parameter_interval:entry.exact_parameter_interval,
          current_center:"-7789843107295549/4611686018427387904",current_half_width:"1/1000000000",
          input_sha256:"6748eb485a77031a3f50caccea5111d913e58aa32ac428e30a7689354cfd8f26",
          input_git_blob:"e59e11744782ecd8d2b65939f8c40391bde1225d",
          radial_interval:["3","25/8"],relative_target:options.relative_target||"1/500",
          maximum_relative_form_error:fmt(maximumE),evaluations,accepted_intervals:rows.length,
          checks,complete_mean_height_enclosure:fmt(Z),intervals:rows,rejected_parent_boxes:rejected,
          unresolved_intervals:failed,
          scope:"Complete infinite-angle actual natural graft over original R66 real family, which contains delta5 +/-1e-9. This pays only the graft part of R111; no body, DN inverse, high Schur or nonlinear solution is asserted."};
}

function compactCertificate(full, sourceSha) {
 return {
  kind:full.kind,complete:full.complete,whole_eta_graft_complete:true,body_complete:false,
  full_cap_complete:false,source_sha256:sourceSha,
  input_path:"notes/2026-11-12-positive-family-exterior-entry-jets.json",
  input_sha256:full.input_sha256,input_git_blob:full.input_git_blob,
  arithmetic:full.arithmetic,current_center:full.current_center,
  current_half_width:full.current_half_width,
  original_parameter_interval:full.original_parameter_interval,
  radial_interval:full.radial_interval,relative_target:full.relative_target,
  maximum_relative_form_error:full.maximum_relative_form_error,
  exact_interval_endpoint_denominator:"1000000000000000000000000000000000000000000000000000000000000",
  accepted_intervals:full.accepted_intervals,evaluations:full.evaluations,
  rejected_parent_count:full.rejected_parent_boxes.length,
  complete_mean_height_enclosure:full.complete_mean_height_enclosure,
  checks:full.checks,
  interval_columns:["physical_r_left","physical_r_right","relative_error_upper_numerator_over_10^60"],
  intervals:full.intervals.map(r=>[...r.radial_interval,r.relative_form_error.upper.split("/")[0]]),
  unresolved_intervals:full.unresolved_intervals,
  scope:full.scope,
  reproduction:"The compact certificate retains every accepted exact interval and directed upper endpoint. All normalization boxes and rejected parent details are deterministically regenerated by the same source; they are not split or encoded into connector transfers."
 };
}

export { certifyGraft, compactCertificate };

if (process.argv[1] && import.meta.url === pathToFileURL(path.resolve(process.argv[1])).href) {
 const root=path.resolve(process.argv[2]||".");
 const inputPath=path.join(root,"notes/2026-11-12-positive-family-exterior-entry-jets.json");
 const text=fs.readFileSync(inputPath,"utf8");
 const digest=crypto.createHash("sha256").update(text,"utf8").digest("hex");
 if(digest!=="6748eb485a77031a3f50caccea5111d913e58aa32ac428e30a7689354cfd8f26")
   throw Error("the actual certified R66 input bytes changed");
 const full=certifyGraft(JSON.parse(text),{relative_target:"1/500",max_depth:12});
 const sourceSha=crypto.createHash("sha256").update(fs.readFileSync(fileURLToPath(import.meta.url))).digest("hex");
 const certificate=compactCertificate(full,sourceSha);
 const out=path.resolve(process.argv[3]||path.join(root,"notes/2026-11-12-R111-actual-whole-family-graft.json"));
 fs.mkdirSync(path.dirname(out),{recursive:true});
 fs.writeFileSync(out,JSON.stringify(certificate,null,2)+"\n");
 if(process.argv[4])fs.writeFileSync(path.resolve(process.argv[4]),JSON.stringify(full,null,2)+"\n");
 console.log(JSON.stringify({complete:certificate.complete,accepted_intervals:certificate.accepted_intervals,
   maximum_relative_form_error:certificate.maximum_relative_form_error,source_sha256:sourceSha}));
}
