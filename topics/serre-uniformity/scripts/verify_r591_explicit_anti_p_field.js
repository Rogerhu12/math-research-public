#!/usr/bin/env node
'use strict';
// Recovery implementation, 2026-11-14. The original 13204-byte source was lost.
// Every mathematical output is recomputed exactly; old hashes are comparisons,
// not claims of byte recovery. This file writes only to the selected out-dir.
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const assert = (v,m='assertion failed') => { if (!v) throw Error(m); };
const hash = s => crypto.createHash('sha256').update(s).digest('hex');
const serial = x => JSON.stringify(x)+'\n';
const mod = (a,m) => ((a%m)+m)%m;
function pow(a,n,m) { let r=1n; a=mod(a,m); for(;n;n>>=1n,a=a*a%m) if(n&1n) r=r*a%m; return r; }
function inv(a,m) { let b=m,x=1n,y=0n; a=mod(a,m); while(b){const q=a/b; [a,b]=[b,a-q*b];[x,y]=[y,x-q*y];} assert(a===1n,'nonunit inverse');return mod(x,m); }
function vp(a,p=43n){if(a===0n)return null;a=a<0n?-a:a;let n=0;while(a%p===0n){a/=p;n++;}return n;}
const bitlen = n => (n<0n?-n:n).toString(2).length;
function parseLossless(s){return JSON.parse(s.replace(/"(?:\\.|[^"\\])*"|-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?/g,t=>t[0]==='"'||/[.eE]/.test(t)||t.replace('-','').length<16?t:'"'+t+'"'));}
const g0=()=>[0n,0n], g1=()=>[1n,0n];
const ga=(a,b)=>[a[0]+b[0],a[1]+b[1]];
const gs=(a,b)=>[a[0]-b[0],a[1]-b[1]];
const gm=(a,b)=>[a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]];
const gz=a=>a[0]===0n&&a[1]===0n;
const eqg=(a,b)=>a[0]===b[0]&&a[1]===b[1];
const gstr=a=>a.map(String);
function ringZero(){return Array.from({length:42},g0);}
function ringOne(){const r=ringZero();r[0]=g1();return r;}
function normalize43(a){const z=a[42];return a.slice(0,42).map(x=>gs(x,z));}
function ringMul(a,b){const c=Array.from({length:43},g0);for(let j=0;j<42;j++)if(!gz(a[j]))for(let k=0;k<42;k++)if(!gz(b[k]))c[(j+k)%43]=ga(c[(j+k)%43],gm(a[j],b[k]));return normalize43(c);}
function ringShift(a,d){const c=Array.from({length:43},g0);for(let j=0;j<42;j++)c[(j+d)%43]=ga(c[(j+d)%43],a[j]);return normalize43(c);}
function ringAdd(a,b){return a.map((x,j)=>ga(x,b[j]));}
function uPoly(d){const c=Array.from({length:43},g0);c[0]=[0n,1n];const ip=[[1n,0n],[0n,-1n],[-1n,0n],[0n,1n]];for(let v=0;v<43;v++){const j=d*v%43;c[j]=ga(c[j],gm([1n,-1n],ip[v%4]));}return normalize43(c);}
function inv43(a){let x=1;while(a*x%43!==1)x++;return x;}
const centered=d=>{let x=inv43(d);return x>21?x-43:x;};
function matZero(){return Array.from({length:43},()=>Array.from({length:43},g0));}
function matIdentity(){const a=matZero();for(let j=0;j<43;j++)a[j][j]=g1();return a;}
function matMul(a,b){const c=matZero();for(let i=0;i<43;i++)for(let k=0;k<43;k++)if(!gz(a[i][k]))for(let j=0;j<43;j++)if(!gz(b[k][j]))c[i][j]=ga(c[i][j],gm(a[i][k],b[k][j]));return c;}
function exactField(){
  const e=Array.from({length:42},(_,j)=>centered(j+1));
  const us=Array.from({length:43},(_,j)=>j?uPoly(j):null);
  const one=ringOne();
  for(let d=1;d<=21;d++)assert(us[d]&&ringMul(us[d],us[43-d]).every((x,j)=>eqg(x,one[j])),'u inverse');
  const squares=us.map(x=>x?ringMul(x,x):null), hs=[];
  for(let a=2;a<43;a++){
    const b=mod(BigInt(1-a),43n), ai=inv43(a),bi=inv43(Number(b));let h=ringOne();
    for(let d=1;d<=21;d++){
      const z=centered(ai*d%43)+centered(bi*d%43)-centered(d);
      assert(z%43===0,'nonintegral exponent');const m=z/43;assert(m>=-1&&m<=1,'exponent range');
      if(m)h=ringMul(h,squares[m>0?d:43-d]);
    }
    hs.push({a,b:Number(b),h});
  }
  const H=[];
  for(let k=0;k<43;k++){let h=ringZero();for(const z of hs)h=ringAdd(h,ringShift(z.h,z.b*k%43));H.push(h);}
  const M=matZero();for(let j=1;j<43;j++)M[j][0]=[-1n,0n];
  for(let k=1;k<43;k++){M[0][k]=[-1n,0n];for(let j=1;j<42;j++)M[j][k]=gs(H[k][j],H[k][0]);M[42][k]=[-H[k][0][0],-H[k][0][1]];}
  let B=matIdentity();const desc=[1n];
  for(let k=1;k<=43;k++){
    B=matMul(M,B);let tr=g0();for(let j=0;j<43;j++)tr=ga(tr,B[j][j]);
    assert(tr[0]%BigInt(k)===0n&&tr[1]%BigInt(k)===0n,'FL integrality');
    const c=[-tr[0]/BigInt(k),-tr[1]/BigInt(k)];assert(c[1]===0n,'nonreal charpoly');desc.push(c[0]);
    for(let j=0;j<43;j++)B[j][j]=ga(B[j][j],c);
  }
  assert(B.every(r=>r.every(gz)),'Cayley Hamilton');
  const asc=desc.slice().reverse();
  return {M,asc,e};
}
function fTrim(a){while(a.length>1&&a[a.length-1]===0)a.pop();return a;}
function fMod(a,b){a=a.slice();const deg=b.length-1,iv=Number(inv(BigInt(b[deg]),5n));while(a.length>=b.length&&!(a.length===1&&a[0]===0)){let c=a[a.length-1]*iv%5,d=a.length-b.length;for(let j=0;j<b.length;j++)a[d+j]=(a[d+j]-c*b[j]%5+5)%5;fTrim(a);}return a.length?a:[0];}
function fMul(a,b,P){const c=Array(a.length+b.length-1).fill(0);for(let j=0;j<a.length;j++)for(let k=0;k<b.length;k++)c[j+k]=(c[j+k]+a[j]*b[k])%5;return fMod(c,P);}
function fPow(a,n,P){let r=[1];for(;n;n>>=1n,a=fMul(a,a,P))if(n&1n)r=fMul(r,a,P);return r;}
function fGcd(a,b){while(!(b.length===1&&b[0]===0)){[a,b]=[b,fMod(a,b)];}return a;}
function checkRabin(asc){const P=asc.map(x=>Number(mod(x,5n)));let a=[0,1];const x5=fPow(a,5n,P);x5[1]=(x5[1]+4)%5;assert(fGcd(P,fTrim(x5)).length===1,'Rabin gcd');for(let j=0;j<43;j++)a=fPow(a,5n,P);assert(a.length===2&&a[0]===0&&a[1]===1,'Rabin Frobenius');return P;}
function finiteBeta(){
  const phi=Array(43).fill(1),one=[1];let eps=one;
  for(let d=1;d<=21;d++){
    const ee=2*centered(d);const u=uPoly(ee<0?43-d:d).map(x=>Number(mod(x[0]+3n*x[1],5n)));
    eps=fMul(eps,fPow(u,BigInt(Math.abs(ee)),phi),phi);
  }
  const symbol=fPow(eps,(5n**42n-1n)/43n,phi);let k=-1,z=one;
  for(let j=0;j<43;j++){if(JSON.stringify(fTrim(z.slice()))===JSON.stringify(fTrim(symbol.slice())))k=j;z=fMul(z,[0,1],phi);}
  assert(k===22,'finite beta symbol');
  let b=[-1n,2n],r=g1(),n=1848n;while(n){if(n&1n)r=gm(r,b).map(x=>mod(x,1849n));b=gm(b,b).map(x=>mod(x,1849n));n>>=1n;}
  assert(eqg(r,[904n,1376n]),'beta p2');const ray=Number(mod(-((r[1])/43n)*inv(21n,43n),43n));
  assert(ray===21&&Number(mod(BigInt(k)*inv(42n,43n),43n))===ray,'Artin normalization');
  return {symbol_exponent:k,residue_degree:42,positive_artin_exponent:ray,beta_power_1848_mod_1849:r.map(Number),original_t_coordinate:ray};
}
function qMarking(input,F){
  const q=BigInt(input.q),zeta=input.expected.zeta_Weil.map(BigInt);assert(q%172n===171n,'q congruence');
  const qa=(a,b)=>ga(a,b).map(x=>mod(x,q)),qm=(a,b)=>gm(a,b).map(x=>mod(x,q));
  const qi=a=>{const d=inv(mod(a[0]*a[0]+a[1]*a[1],q),q);return [a[0]*d%q,mod(-a[1]*d,q)];};
  function qp(a,n){let r=g1();while(n){if(n&1n)r=qm(r,a);a=qm(a,a);n>>=1n;}return r;}
  const zp=[g1()];for(let j=1;j<43;j++)zp.push(qm(zp[j-1],zeta));assert(eqg(qm(zp[42],zeta),g1())&&!eqg(zeta,g1()),'Weil order');
  const u=Array(43).fill(null);for(let a=1;a<43;a++){
    const iz=qm([0n,1n],zp[a]);const val=qm([0n,q-1n],qm(qa(g1(),iz.map(x=>mod(-x,q))),qi(qa(g1(),iz))));
    assert(val[1]===0n&&val[0]!==0n,'u lies Fq');u[a]=val[0];
  }
  const rho=Array(43).fill(null),rootexp=inv(43n,q-1n);
  for(let a=1;a<43;a++){
    let e=1n;for(let d=1;d<=21;d++){const k=2*centered(d),v=u[a*d%43];e=e*pow(k<0?inv(v,q):v,BigInt(Math.abs(k)),q)%q;}
    rho[a]=pow(e,rootexp,q);assert(pow(rho[a],43n,q)===e,'rho root');
  }
  const th=[];for(let j=0;j<43;j++){let s=g0();for(let a=1;a<43;a++)s=qa(s,zp[a*j%43].map(x=>x*rho[a]%q));th.push(s);}
  assert(th[0][1]===0n,'theta0 real branch');assert(new Set(th.map(x=>x.join(','))).size===43,'distinct q roots');
  const expected='148744992525694032252153033135038096685773870238183621798369636318237346986286226806884168316917318315826907918769500752959749152696299669679028280219160288356458960197068546157018804422255134115675506563630593485021850459734196136450';
  assert(th[0][0].toString()===expected,'original marked theta0 root');
  const M=F.M.map(r=>r.map(a=>a.map(x=>mod(x,q))));let checks=0;
  for(let k=0;k<43;k++){
    assert(eqg([th[k][0],mod(-th[k][1],q)],th[(43-k)%43]),'q Frobenius');
    let pv=g0();for(let j=43;j>=0;j--)pv=qa(qm(pv,th[k]),[mod(F.asc[j],q),0n]);assert(gz(pv),'q polynomial');
    const ev=[g1()];for(let j=1;j<43;j++)ev.push(th[(k+j)%43]);
    for(let col=0;col<43;col++){
      let v=g0();for(let row=0;row<43;row++)v=qa(v,qm(ev[row],M[row][col]));assert(eqg(v,qm(th[k],ev[col])),'marked multiplication evaluation');checks++;
    }
  }
  assert(checks===1849,'q count');
  return {q:q.toString(),zeta_Weil:gstr(zeta),rho_roots:rho.slice(1).map(String),theta_roots:th.map(gstr),matrix_evaluation_checks:checks,theta0_is_unique_Fq_root:true,original_t_marked:true};
}
function polyMul(a,b){const c=Array(a.length+b.length-1).fill(0n);for(let j=0;j<a.length;j++)for(let k=0;k<b.length;k++)c[j+k]+=a[j]*b[k];return c;}
function polyRem(a,P){a=a.slice();while(a.length>=P.length){const d=a.length-P.length,c=a[a.length-1];for(let j=0;j<P.length;j++)a[d+j]-=c*P[j];a.pop();}return a;}
function shifted(asc){const a=Array(44).fill(0n);for(let i=0;i<44;i++){let bin=1n;for(let j=0;j<=i;j++){a[j]+=asc[i]*bin*((i-j)%2?-1n:1n);bin=bin*BigInt(i-j)/BigInt(j+1);}}return a;}
function integralModels(input,F){
  const Pf=input.P.map(BigInt).reverse();assert(Pf.length===45&&Pf[44]===1n,'F polynomial');
  const r=Pf.slice(0,44).map(x=>{assert(x%43n===0n,'F Eisenstein');return x/43n;});assert(vp(Pf[0])===1&&mod(r[0],43n)===5n,'F constant');
  const c=BigInt(input.b);let norm=0n;for(let j=0;j<=44;j++)norm+=Pf[j]*c**BigInt(44-j);assert(norm===-BigInt(input.q),'original alpha norm');
  const g=shifted(F.asc),vals=g.map(x=>vp(x));assert(vals[0]===1&&g[42]===-43n&&g[43]===1n&&g[41]===0n,'g special coefficients');
  for(let j=1;j<=40;j++)assert(vals[j]===(j===17?3:2),'g valuation list');
  const hvals=g.map((x,j)=>x===0n?null:44*vals[j]+j-43);assert(hvals[0]===1&&hvals[42]===43&&hvals[43]===0,'relative Eisenstein');
  const derivative=hvals.map((v,j)=>j===0||v===null?null:43*(v+44*vp(BigInt(j)))+j-1);
  assert(Math.min(...derivative.filter(x=>x!==null))===1890&&derivative[42]===1890&&derivative.filter(x=>x===1890).length===1,'relative different');
  assert(derivative[43]===1934,'leading derivative');
  const gd=g.map((x,j)=>j===0||!x?null:43*vp(BigInt(j)*x)+j-1);assert(Math.min(...gd.filter(x=>x!==null))===84,'Kt different');
  const A=Array(44).fill(0n);A[0]=inv(mod(r[0],43n),43n);for(let n=1;n<44;n++){let s=0n;for(let j=1;j<=n;j++)s+=r[j]*A[n-j];A[n]=mod(-A[0]*s,43n);}
  const expected=[26,0,39,0,12,0,30,0,20,0,26,0,4,0,25,0,24,0,0,0,26,0,20,0,13,0,15,0,38,0,26,0,7,0,38,0,36,0,12,0,16,0,26,0];
  assert(A.every((x,j)=>Number(x)===expected[j]),'global inverse');
  const RA=polyRem(polyMul(r,A),Pf);while(RA.length<44)RA.push(0n);const BB=RA.map((x,j)=>{const z=x-(j===0?1n:0n);assert(z%43n===0n,'exact RA congruence');return z/43n;});
  const local={g_coefficients_ascending:g.map(String),g_43_valuations:vals,h_relative_valuations:hvals,derivative_valuations:derivative,Kt_different_exponent:84,relative_different_exponent:1890,relative_lower_break:44,relative_conductor_exponent:45,tensor_order_index_vF:903,local_basis:'1,z,...,z^42; z=(theta_0+1)/y_F'};
  const global={A_coefficients_ascending:A.map(Number),RA_minus_one_over_43_reduced_coefficients:BB.map(String),generator_count:85,base_ring:'actual maximal O_F',generators:'O_F O_Kt plus w_j, 1<=j<=42',w_j:'-(theta_0+1)^j*y_F^(44-j)*A(y_F)/43 = z^j*R(y_F)*A(y_F)',free_basis_claimed:false,ordinary_b_computed:false,actual_norm_preimage_computed:false};
  return {local,global};
}
function run(){
  const argv=process.argv.slice(2),at=k=>{const j=argv.indexOf(k);return j<0?null:argv[j+1];};
  const source=at('--r171');assert(source,'supply --r171 exact source JSON');const out=at('--out-dir')||__dirname,check=argv.includes('--check');
  const raw=fs.readFileSync(source),inputsha=hash(raw);assert(inputsha==='a3197f9b17672017a2e49072cfcdab7b1a07813c15eb3a73de2aa0093ef86aa6','R171 input SHA');const input=parseLossless(raw.toString('utf8'));
  const F=exactField(),rabin=checkRabin(F.asc),beta=finiteBeta();
  const mm=F.M.map(row=>row.map(gstr)),ss=F.asc.map(String);
  const oldPoly='601aeade1625cb2b533d10a9a45e00407ffe40a6b730eeb004acbf5c4a819b14',oldMat='8a663ac35d6a7066ed57f2aaf9a98eb9eb3cd25f1775fc7a9c865ee69ed3e547';
  const hashes={polynomial_ascending:hash(serial(ss)),polynomial_descending:hash(serial(ss.slice().reverse())),matrix_row_gaussian_strings:hash(serial(mm)),matrix_row_gaussian_numbers:hash(serial(F.M.map(r=>r.map(a=>a.map(Number)))))};
  const polynomialMatch=Object.values(hashes).includes(oldPoly),matrixMatch=Object.values(hashes).includes(oldMat);
  assert(Math.max(...F.asc.map(bitlen))===408,'408-bit polynomial');assert(Math.max(...F.M.flat().flat().map(bitlen))===26,'26-bit multiplication');
  const qdata=qMarking(input,F),models=integralModels(input,F);
  const algebra={p:43,basis:['1',...Array.from({length:42},(_,j)=>'theta_'+(j+1))],centered_inverse_exponents:F.e,multiplication_matrix_theta0:mm,polynomial_coefficients_ascending:ss,polynomial_mod_5_ascending:rabin,cayley_hamilton:true,rabin_mod_5:true,max_matrix_coefficient_bits:26,max_polynomial_coefficient_bits:408,t_action:'(c0,c1,...,c42) -> (c0,-c42,c1-c42,...,c41-c42)',relative_discriminant:'43^84',real_subfield_discriminant:'-2^42*43^84'};
  const entries=[['r591_exact_cyclotomic_algebra.json',algebra],['r591_exact_beta_marking.json',beta],['r591_exact_cyclotomic_q_marking.json',qdata],['r591_relative_local_norm_model.json',models.local],['r591_global_maximal_order_generators.json',models.global]];
  const files=[];for(const [name,obj] of entries){const text=serial(obj),dest=path.join(out,name);if(check)assert(fs.readFileSync(dest,'utf8')===text,'certificate mismatch '+name);else fs.writeFileSync(dest,text);files.push({name,bytes:Buffer.byteLength(text),sha256:hash(text)});}
  const report={status:'PASS',mode:check?'independent_check':'reconstruction_with_all_mathematical_checks',recovery:true,old_source_bytes_recovered:false,source_sha256:hash(fs.readFileSync(__filename)),r171_input_sha256:inputsha,comparison_hashes:hashes,old_polynomial_hash_matched:polynomialMatch,old_matrix_hash_matched:matrixMatch,files,actual_norm_preimage_computed:false,ordinary_b_computed:false,original_R201_R561_interface_closed:false};
  if(!check)fs.writeFileSync(path.join(out,'r591_recovery_validation.json'),serial(report));process.stdout.write(serial(report));
}
if(require.main===module)run();
module.exports={exactField,finiteBeta,qMarking,integralModels,parseLossless};
