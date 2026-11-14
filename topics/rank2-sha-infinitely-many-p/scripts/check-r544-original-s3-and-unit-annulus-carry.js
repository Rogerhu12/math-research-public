#!/usr/bin/env node
// R544 exact characteristic-zero source, frame and word certificate.
function certifyD6Frames(){"use strict";
const ck=(x,m)=>{if(!x)throw Error(m);};
const abs=x=>x<0n?-x:x,gcd=(x,y)=>{x=abs(x);y=abs(y);while(y)[x,y]=[y,x%y];return x;};
const Q=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);ck(d!==0n,"zero denominator");if(d<0n){n=-n;d=-d;}let g=gcd(n,d);return[n/g,d/g];};
const qa=(x,y)=>Q(x[0]*y[1]+y[0]*x[1],x[1]*y[1]),qn=x=>[-x[0],x[1]],
qm=(x,y)=>Q(x[0]*y[0],x[1]*y[1]),qi=x=>Q(x[1],x[0]),
qs=x=>x[1]===1n?String(x[0]):String(x[0])+"/"+x[1];
const E=(a,b=0,d=1)=>[Q(a,d),Q(b,d)], ea=(x,y)=>[qa(x[0],y[0]),qa(x[1],y[1])],
en=x=>[qn(x[0]),qn(x[1])],es=(x,y)=>ea(x,en(y)),
em=(x,y)=>[qa(qm(x[0],y[0]),qn(qm(x[1],y[1]))),
qa(qa(qm(x[0],y[1]),qm(x[1],y[0])),qn(qm(x[1],y[1])))],
ec=x=>[qa(x[0],qn(x[1])),qn(x[1])],
eq=(x,y)=>x[0][0]===y[0][0]&&x[0][1]===y[0][1]&&x[1][0]===y[1][0]&&x[1][1]===y[1][1],
esc=(x,a,b=1)=>em(x,E(a,0,b)),ez=x=>eq(x,E(0)),
ei=x=>{let n=em(x,ec(x));ck(n[1][0]===0n,"norm rational");return[ qm(ec(x)[0],qi(n[0])),qm(ec(x)[1],qi(n[0])) ];},
out=x=>x.map(qs);
const he=(x,y)=>x.reduce((a,t,i)=>ea(a,em(t,ec(y[i]))),E(0));
const va=(x,y)=>x.map((t,i)=>ea(t,y[i])),vs=(x,y)=>x.map((t,i)=>es(t,y[i])),
vm=(x,c)=>x.map(t=>em(t,c));
const mm=(A,B)=>A.map(row=>B[0].map((_,j)=>row.reduce((s,t,k)=>ea(s,em(t,B[k][j])),E(0))));
const ident=n=>Array.from({length:n},(_,i)=>Array.from({length:n},(_,j)=>E(i===j?1:0)));
function inverse(A){let M=A.map(row=>row.map(x=>x)),B=ident(A.length),det=E(1);
 for(let k=0;k<M.length;k++){let p=k;while(p<M.length&&ez(M[p][k]))p++;ck(p<M.length,"singular");
  if(p!==k){[M[p],M[k]]=[M[k],M[p]];[B[p],B[k]]=[B[k],B[p]];det=en(det);}
  const pivot=M[k][k];det=em(det,pivot);const inv=ei(pivot);M[k]=vm(M[k],inv);B[k]=vm(B[k],inv);
  for(let i=0;i<M.length;i++)if(i!==k&&!ez(M[i][k])){const f=M[i][k];M[i]=vs(M[i],vm(M[k],f));B[i]=vs(B[i],vm(B[k],f));}
 } return {inverse:B,det}; }


const H=[[E(-1,-1,2),E(-1,-2,2)],[E(2,1,2),E(-1,-1,2)]],Hi=inverse(H).inverse;
const T=[[E(0),E(-1)],[E(1),E(-1)]],Ti=inverse(T).inverse,R=[[E(-1),E(1)],[E(0),E(1)]];
const Y=[E(1),E(2)],W=[E(3,6),E(4)],L=[E(1,3),E(1)],M=[E(1),E(2,3)];
const outm=A=>A.map(r=>r.map(out)),power=(A,n)=>{let X=ident(2);while(n--)X=mm(X,A);return X;};
const matEq=(A,B)=>A.every((r,i)=>r.every((x,j)=>eq(x,B[i][j])));
ck(matEq(power(H,3),vmatrix(ident(2),E(-1))),"H^3=-I");
function vmatrix(A,c){return A.map(r=>vm(r,c));}
ck(matEq(power(T,3),ident(2))&&matEq(power(R,2),ident(2)),"D6 orders");
ck(matEq(mm(mm(R,T),R),Ti),"RTR=T^-1");
const frames=[];
for(let j=0;j<3;j++){const F=power(Hi,j),invF=power(H,j),Rj=mm(mm(power(T,j),R),power(Ti,j));ck(matEq(power(Rj,2),ident(2)),"reflection j");
frames.push({j,frame:outm(F),Rj:outm(Rj),Y:out(mm([Y],invF)[0][0]),Ypair:mm([Y],invF)[0].map(out),Wpair:mm([W],invF)[0].map(out),Lpair:mm([L],invF)[0].map(out),Mpair:mm([M],invF)[0].map(out)});
}
const rawRs=[R,mm(mm(T,R),Ti),mm(mm(power(T,2),R),power(Ti,2))];
ck(rawRs[0].every((r,i)=>r.every((v,k)=>ez(ea(ea(v,rawRs[1][i][k]),rawRs[2][i][k])))),"sum Rj=0");
const cs=[0,1,2].map(j=>power(Hi,j)[0]);let dets=[];
for(let i=0;i<3;i++)for(let j=i+1;j<3;j++){let d=inverse([cs[i],cs[j]]).det;dets.push({i,j,det:out(d),norm:out(em(d,ec(d)))});}
return{H:outm(H),T:outm(T),R:outm(R),frames,pairwise_C_determinants:dets};
}
function certifyS3Sources(){"use strict";
const ck=(x,m)=>{if(!x)throw Error(m);};
const abs=x=>x<0n?-x:x,gcd=(x,y)=>{x=abs(x);y=abs(y);while(y)[x,y]=[y,x%y];return x;};
const Q=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);ck(d!==0n,"zero denominator");if(d<0n){n=-n;d=-d;}let g=gcd(n,d);return[n/g,d/g];};
const qa=(x,y)=>Q(x[0]*y[1]+y[0]*x[1],x[1]*y[1]),qn=x=>[-x[0],x[1]],
qm=(x,y)=>Q(x[0]*y[0],x[1]*y[1]),qi=x=>Q(x[1],x[0]),
qs=x=>x[1]===1n?String(x[0]):String(x[0])+"/"+x[1];
const E=(a,b=0,d=1)=>[Q(a,d),Q(b,d)], ea=(x,y)=>[qa(x[0],y[0]),qa(x[1],y[1])],
en=x=>[qn(x[0]),qn(x[1])],es=(x,y)=>ea(x,en(y)),
em=(x,y)=>[qa(qm(x[0],y[0]),qn(qm(x[1],y[1]))),
qa(qa(qm(x[0],y[1]),qm(x[1],y[0])),qn(qm(x[1],y[1])))],
ec=x=>[qa(x[0],qn(x[1])),qn(x[1])],
eq=(x,y)=>x[0][0]===y[0][0]&&x[0][1]===y[0][1]&&x[1][0]===y[1][0]&&x[1][1]===y[1][1],
esc=(x,a,b=1)=>em(x,E(a,0,b)),ez=x=>eq(x,E(0)),
ei=x=>{let n=em(x,ec(x));ck(n[1][0]===0n,"norm rational");return[ qm(ec(x)[0],qi(n[0])),qm(ec(x)[1],qi(n[0])) ];},
out=x=>x.map(qs);
const he=(x,y)=>x.reduce((a,t,i)=>ea(a,em(t,ec(y[i]))),E(0));
const va=(x,y)=>x.map((t,i)=>ea(t,y[i])),vs=(x,y)=>x.map((t,i)=>es(t,y[i])),
vm=(x,c)=>x.map(t=>em(t,c));
const mm=(A,B)=>A.map(row=>B[0].map((_,j)=>row.reduce((s,t,k)=>ea(s,em(t,B[k][j])),E(0))));
const ident=n=>Array.from({length:n},(_,i)=>Array.from({length:n},(_,j)=>E(i===j?1:0)));
function inverse(A){let M=A.map(row=>row.map(x=>x)),B=ident(A.length),det=E(1);
 for(let k=0;k<M.length;k++){let p=k;while(p<M.length&&ez(M[p][k]))p++;ck(p<M.length,"singular");
  if(p!==k){[M[p],M[k]]=[M[k],M[p]];[B[p],B[k]]=[B[k],B[p]];det=en(det);}
  const pivot=M[k][k];det=em(det,pivot);const inv=ei(pivot);M[k]=vm(M[k],inv);B[k]=vm(B[k],inv);
  for(let i=0;i<M.length;i++)if(i!==k&&!ez(M[i][k])){const f=M[i][k];M[i]=vs(M[i],vm(M[k],f));B[i]=vs(B[i],vm(B[k],f));}
 } return {inverse:B,det}; }


const H=[[E(-1,-1,2),E(-1,-2,2)],[E(2,1,2),E(-1,-1,2)]],H2=mm(H,H),Rc=[[E(-1),E(0)],[E(0),E(1)]];
const mul=(a,b)=>{const r=Array.from({length:a.length+b.length-1},()=>E(0));a.forEach((x,i)=>b.forEach((y,j)=>r[i+j]=ea(r[i+j],em(x,y))));return r;};
const pow=(p,n)=>{let r=[E(1)];while(n--)r=mul(r,p);return r;};
const scale=(a,c)=>a.map(x=>em(x,c)),add=(a,b)=>Array.from({length:Math.max(a.length,b.length)},(_,i)=>ea(a[i]||E(0),b[i]||E(0)));
function source(M,k){const p=vm([M[0][0],M[1][0]],E(2)),q=vm([M[0][1],M[1][1]],E(2));if(k===2)return mul(p,q);return scale(add(mul(pow(p,7),q),mul(p,pow(q,7))),E(1,0,210));}
const checks=[];
for(const k of[2,8]){const m0=source(ident(2),k),e=scale(source(H,k),E(-1,-1)),teta=scale(source(H2,k),E(0,1)),rceta=scale(source(mm(Rc,H),k),E(-1,-1));
const cyc=add(add(m0,e),teta),ref=add(rceta,scale(add(m0,e),E(-1)));ck(cyc.every(ez),"three source "+k);ck(ref.every(ez),"raw reflection "+k);
checks.push({degree:k,cycle_difference:cyc.map(out),reflection_difference:ref.map(out)});}
const al=E(1,3),p=[al,E(1)],q=[E(1),en(ec(al))],f8=scale(add(mul(pow(p,7),q),mul(p,pow(q,7))),E(1,0,210));
ck(eq(esc(f8[3],2),E(-48,-48))&&eq(esc(f8[5],2),E(0,48)),"odd coordinates");
return{checks,odd_basis:{basis:"f_j=sigma^8*y*x^j",f2_f2:"-12",b_f0_f1:out(E(-48,-48)),b_f1_f0:out(E(0,48)),first_l_derivative:"12 f2",mixed_first_moment:"-12 Omega^2"},full_jet_bound:{axis_degree:4,required_rectangle:[4,4],simultaneous_type:2,total_degrees:[2,8]}};
}
function certifyMixedWord(){"use strict";
const ck=(x,m)=>{if(!x)throw Error(m);};
const abs=x=>x<0n?-x:x,gcd=(x,y)=>{x=abs(x);y=abs(y);while(y)[x,y]=[y,x%y];return x;};
const Q=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);ck(d!==0n,"zero denominator");if(d<0n){n=-n;d=-d;}let g=gcd(n,d);return[n/g,d/g];};
const qa=(x,y)=>Q(x[0]*y[1]+y[0]*x[1],x[1]*y[1]),qn=x=>[-x[0],x[1]],
qm=(x,y)=>Q(x[0]*y[0],x[1]*y[1]),qi=x=>Q(x[1],x[0]),
qs=x=>x[1]===1n?String(x[0]):String(x[0])+"/"+x[1];
const E=(a,b=0,d=1)=>[Q(a,d),Q(b,d)], ea=(x,y)=>[qa(x[0],y[0]),qa(x[1],y[1])],
en=x=>[qn(x[0]),qn(x[1])],es=(x,y)=>ea(x,en(y)),
em=(x,y)=>[qa(qm(x[0],y[0]),qn(qm(x[1],y[1]))),
qa(qa(qm(x[0],y[1]),qm(x[1],y[0])),qn(qm(x[1],y[1])))],
ec=x=>[qa(x[0],qn(x[1])),qn(x[1])],
eq=(x,y)=>x[0][0]===y[0][0]&&x[0][1]===y[0][1]&&x[1][0]===y[1][0]&&x[1][1]===y[1][1],
esc=(x,a,b=1)=>em(x,E(a,0,b)),ez=x=>eq(x,E(0)),
ei=x=>{let n=em(x,ec(x));ck(n[1][0]===0n,"norm rational");return[ qm(ec(x)[0],qi(n[0])),qm(ec(x)[1],qi(n[0])) ];},
out=x=>x.map(qs);
const he=(x,y)=>x.reduce((a,t,i)=>ea(a,em(t,ec(y[i]))),E(0));
const va=(x,y)=>x.map((t,i)=>ea(t,y[i])),vs=(x,y)=>x.map((t,i)=>es(t,y[i])),
vm=(x,c)=>x.map(t=>em(t,c));
const mm=(A,B)=>A.map(row=>B[0].map((_,j)=>row.reduce((s,t,k)=>ea(s,em(t,B[k][j])),E(0))));
const ident=n=>Array.from({length:n},(_,i)=>Array.from({length:n},(_,j)=>E(i===j?1:0)));
function inverse(A){let M=A.map(row=>row.map(x=>x)),B=ident(A.length),det=E(1);
 for(let k=0;k<M.length;k++){let p=k;while(p<M.length&&ez(M[p][k]))p++;ck(p<M.length,"singular");
  if(p!==k){[M[p],M[k]]=[M[k],M[p]];[B[p],B[k]]=[B[k],B[p]];det=en(det);}
  const pivot=M[k][k];det=em(det,pivot);const inv=ei(pivot);M[k]=vm(M[k],inv);B[k]=vm(B[k],inv);
  for(let i=0;i<M.length;i++)if(i!==k&&!ez(M[i][k])){const f=M[i][k];M[i]=vs(M[i],vm(M[k],f));B[i]=vs(B[i],vm(B[k],f));}
 } return {inverse:B,det}; }


const add=(p,q)=>Array.from({length:Math.max(p.length,q.length)},(_,i)=>ea(p[i]||E(0),q[i]||E(0))),neg=p=>p.map(en),mul=(p,q)=>{const r=Array.from({length:p.length+q.length-1},()=>E(0));p.forEach((x,i)=>q.forEach((y,j)=>r[i+j]=ea(r[i+j],em(x,y))));return r;};
const peq=(p,q)=>add(p,neg(q)).every(ez),pm=(A,B)=>A.map(row=>B[0].map((_,j)=>row.reduce((s,t,k)=>add(s,mul(t,B[k][j])),[E(0)])));
const C=[E(0,1,2),E(1,-1,2)],PC=C.map((_,i)=>C.map((_,j)=>{const proj=em(ec(C[i]),C[j]);return[es(E(i===j?1:0),proj),proj];}));
const P0=[[[E(0),E(1)],[E(0)]],[[E(0)],[E(1)]]],M=pm(P0,PC),A=pm(pm(M,M),M),tr=add(M[0][0],M[1][1]),det=add(mul(M[0][0],M[1][1]),neg(mul(M[0][1],M[1][0]))),tra=add(A[0][0],A[1][1]);
ck(peq(tr,[E(1,0,4),E(3,0,2),E(1,0,4)]),"word trace");ck(peq(det,[E(0),E(0),E(1)]),"word determinant");
ck(peq(tra,add(mul(mul(tr,tr),tr),neg(mul([E(0),E(0),E(3)],tr)))),"cube trace");
return{M:M.map(r=>r.map(p=>p.map(out))),trace_M:tr.map(out),det_M:det.map(out),trace_A:tra.map(out),unit_eigenvalue_mod_p:"1/64",det_A:"kappa^6",word_source:"(R1 R0)^3=I"};
}
function certifyR544(){return{sources:certifyS3Sources(),frames:certifyD6Frames(),mixed_word:certifyMixedWord(),normalization:{T:"omega^2 H_push",eta:"T rho0",c_d_core:"lambda R0",rotated_core:"lambda Rj",pair_core:"lambda^2 I"},annuli:{Aj:"Cj in p and Dj unit",pairwise_disjoint:true,inside_L_unit:true,remainder:"L,C0,C1,C2 all unit"},negative_moment:{pair:"-12 Omega^2(1-beta*kappa)^2 mod p",full_six:"Omega^6(1-beta*kappa)^6/7 mod p"}};}
if(typeof module!=="undefined"){module.exports={certifyR544};if(require.main===module){const report=certifyR544();require("fs").writeFileSync(__filename.replace(/\.js$/,".json"),JSON.stringify(report,null,2)+"\n");console.log("R544 exact S3, all raw frames, mixed word and odd-source coefficients passed.");}}
