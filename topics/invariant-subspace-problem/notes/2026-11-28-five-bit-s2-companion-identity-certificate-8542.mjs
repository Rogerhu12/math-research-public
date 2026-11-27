// Exact new companion/source identities over five independent variables.
// No original S2 inverse/cost recomputation and no floating arithmetic.
"use strict";
function zero(){return new Map();}
const one=new Map([[0,1n]]),bases=[1,16,256,4096,65536];
const z=bases.map(b=>new Map([[b,1n]]));
function add(a,b,c=1n){const o=new Map(a);for(const[k,v]of b){const w=(o.get(k)||0n)+c*v;if(w)o.set(k,w);else o.delete(k);}return o;}
function scale(a,c){c=BigInt(c);return new Map([...a].map(([k,v])=>[k,v*c]).filter(([k,v])=>v));}
function mul(a,b){const o=new Map;for(const[k,v]of a)for(const[j,w]of b){const v0=(o.get(k+j)||0n)+v*w;if(v0)o.set(k+j,v0);else o.delete(k+j);}return o;}
function pow(a,n){let p=one;for(let i=0;i<n;i++)p=mul(p,a);return p;}
function prod(a){return a.reduce(mul,one);}
function combos(n,k,s=0){if(!k)return[[]];let o=[];for(let i=s;i<=n-k;i++)for(const a of combos(n,k-1,i+1))o.push([i,...a]);return o;}
function sum(a){return a.reduce((s,x)=>add(s,x),zero());}
function elem(k,indices=[0,1,2,3,4]){return sum(combos(indices.length,k).map(c=>prod(c.map(i=>z[indices[i]]))));}
function mat(n,m,f){return Array.from({length:n},(_,i)=>Array.from({length:m},(_,j)=>f(i,j)));}
function eye(n){return mat(n,n,(i,j)=>i===j?one:zero());}
function mm(A,B){return mat(A.length,B[0].length,(i,j)=>sum(B.map((_,k)=>mul(A[i][k],B[k][j]))));}
function ma(A,B,c=1n){return mat(A.length,A[0].length,(i,j)=>add(A[i][j],B[i][j],c));}
function ms(A,p){return A.map(r=>r.map(x=>mul(x,p)));}
function mi(p){return mat(5,5,(i,j)=>i===j?p:zero());}
function isEqual(A,B){return A.every((r,i)=>r.every((x,j)=>!add(x,B[i][j],-1n).size));}
function divInteger(A,n){return A.map(r=>r.map(p=>new Map([...p].map(([k,v])=>{if(v%n)throw Error("nonintegral coefficient");return[k,v/n];}))));}
function verifyCompanionSourceIdentities(){
 const checks=[];function ck(name,A,B){if(!isEqual(A,B))throw Error("FAILED "+name);checks.push(name);}
 const S=elem(1),Z=elem(2),W=elem(3),U=elem(4),V=elem(5);
 const moments=Array.from({length:5},(_,j)=>sum(z.map(t=>pow(t,j+1))));
 const [m1,m2,m3,m4,m5]=moments;
 const T=mat(5,5,(i,j)=>i===j?z[i]:zero()),Q=mat(5,5,(i,j)=>z[j]);
 const T2=mm(T,T),T3=mm(T2,T),T4=mm(T3,T),I=eye(5);
 const R2ind=combos(5,3),Rind=combos(5,2),R3ind=combos(5,4);
 const R=mat(5,10,(i,j)=>Rind[j].includes(i)?prod(Rind[j].filter(k=>k!==i).map(k=>z[k])):zero());
 const Rs=mat(10,5,(i,j)=>Rind[i].includes(j)?one:zero());
 const C=mat(5,10,(i,j)=>Rind[j].includes(i)?prod(Rind[j].filter(k=>k!==i).map(k=>pow(z[k],2))):zero());
 const Cs=mat(10,5,(i,j)=>Rind[i].includes(j)?sum(Rind[i].filter(k=>k!==j).map(k=>z[k])):zero());
 const d3=mat(10,10,(i,j)=>Rind[i].every(k=>R2ind[j].includes(k))?prod(R2ind[j].filter(k=>!Rind[i].includes(k)).map(k=>z[k])):zero());
 const d3s=mat(10,10,(i,j)=>Rind[j].every(k=>R2ind[i].includes(k))?one:zero());
 const R2=mat(5,10,(i,j)=>R2ind[j].includes(i)?prod(R2ind[j].filter(k=>k!==i).map(k=>z[k])):zero());
 const R2s=mat(10,5,(i,j)=>R2ind[i].includes(j)?one:zero());
 const R3=mat(5,5,(i,j)=>R3ind[j].includes(i)?prod(R3ind[j].filter(k=>k!==i).map(k=>z[k])):zero());
 const R3s=mat(5,5,(i,j)=>R3ind[i].includes(j)?one:zero());
 const F1=mm(R,Rs),F2=mm(R2,R2s),Fmid=mm(d3,d3s),CD=mm(C,d3),CDs=mm(d3s,Cs);
 const SminusT=ma(mi(S),T,-1n);
 const DX=ma(ma(ma(mi(add(mul(S,m2),m3,-1n)),ms(T,scale(m2,2)),-1n),ms(T2,scale(S,2)),-1n),ms(T3,new Map([[0,6n]])));
 const X=ma(ma(ma(ma(ma(DX,ms(Q,m2)),ms(mm(Q,T),S)),mm(mm(T,Q),T),-1n),mm(T2,Q),-1n),ms(mm(Q,T2),new Map([[0,2n]])),-1n);
 const Xs=ma(ma(ma(ma(ma(DX,ms(Q,m2)),ms(mm(T,Q),S)),mm(mm(T,Q),T),-1n),mm(Q,T2),-1n),ms(mm(T2,Q),new Map([[0,2n]])),-1n);
 ck("full_X_Cd_R2star",X,mm(CD,R2s));
 ck("physical_Xstar_R2_Cdstar",Xs,mm(R2,CDs));
 let DC=mi(add(add(mul(S,m3),mul(m2,m2)),scale(m4,2),-1n));
 DC=ma(ma(ma(ma(DC,ms(T,scale(m3,2)),-1n),ms(T2,scale(m2,4)),-1n),ms(T3,scale(S,2)),-1n),ms(T4,new Map([[0,12n]])));
 const mixed=ma(ma(mm(T3,Q),mm(Q,T3)),ma(mm(mm(T2,Q),T),mm(mm(T,Q),T2)));
 const FC=ma(ma(ma(ma(DC,ms(Q,m3)),ms(ma(mm(T,Q),mm(Q,T)),m2)),ms(mm(mm(T,Q),T),S)),ms(mixed,new Map([[0,2n]])),-1n);
 ck("full_FCd_Cd_Cdstar",FC,mm(CD,CDs));
 const J=mat(5,5,(i,j)=>pow(z[i],j));
 const companion=mat(5,5,(i,j)=>j<4&&i===j+1?one:zero());
 [V,scale(U,-1),W,scale(Z,-1),S].forEach((p,i)=>{companion[i][4]=p;});
 const Qc=mat(5,5,(i,j)=>i===0?moments[j]:zero());
 ck("exact_companion_evaluation_intertwining",mm(T,J),mm(J,companion));
 ck("exact_rank_one_moment_intertwining",mm(Q,J),mm(J,Qc));
 const tn=mat(5,5,(i,j)=>i===j?prod(z.filter((_,k)=>k!==i)):zero());
 const en=mat(10,5,(i,j)=>Rind[i].includes(j)?prod(z.filter((_,k)=>k!==Rind[i].find(k=>k!==j))):zero());
 const ed=mat(5,10,(i,j)=>Rind[j].includes(i)?one:zero());
 const H=ma(ma(mi(m2),ms(T2,new Map([[0,2n]])),-1n),mm(Q,T));
 ck("full_C_Rstar",H,mm(C,Rs));
 const Cen=ma(ms(ma(mi(S),ms(T,new Map([[0,2n]])),-1n),V),mm(mm(tn,Q),T));
 ck("complete_inverse_creation_Ce",Cen,mm(C,en));
 const Yn=ma(ms(F1,scale(V,4)),ms(mm(mm(tn,Q),SminusT),new Map([[0,2n]])));
 ck("two_times_pi_Y_R_Fmid_e",Yn,mm(mm(R,Fmid),en));
 ck("C_Fmid_e_numerator",mm(mm(C,Fmid),en),ma(mm(Cen,F1),ms(H,V)));
 const Ein=ma(ma(mi(U),ms(tn,new Map([[0,2n]])),-1n),mat(5,5,(i,j)=>prod(z.filter((_,k)=>k!==i))));
 ck("full_e_star_e_numerator",Ein,mm(ed,en));
 ck("e_star_Fmid_e_numerator",mm(mm(ed,Fmid),en),ma(ma(mm(Ein,F1),mi(scale(V,3))),mm(Q,tn)));
 const F3direct=mm(R3,R3s);
 let F3=ma(ma(ma(ma(mi(W),ms(T,scale(Z,2)),-1n),ms(T2,scale(S,3))),ms(T3,new Map([[0,4n]])),-1n),ms(Q,Z));
 F3=ma(F3,ms(ma(mm(T,Q),mm(Q,T)),S),-1n);
 F3=ma(F3,ma(ma(mm(T2,Q),mm(mm(T,Q),T)),mm(Q,T2)));
 ck("full_third_gram_polynomial",F3,F3direct);
 const En=ma(ms(F3,U),divInteger(mm(mm(F3,Q),F3),16n),-1n);
 const explicit=mat(5,5,(i,j)=>{
  if(i===j)return mul(prod(z.filter((_,k)=>k!==i)),elem(3,[0,1,2,3,4].filter(k=>k!==i)));
  let p=one;for(let k=0;k<5;k++)p=mul(p,pow(z[k],2-(k===i?2:0)-(k===j?1:0)));return scale(p,-1);
 });
 ck("actual_top_precision_short_equals_R298",En,explicit);
 const expectedMoments=[
 S,add(pow(S,2),scale(Z,2),-1n),
 add(add(pow(S,3),scale(mul(S,Z),3),-1n),scale(W,3)),
 add(add(add(add(pow(S,4),scale(mul(pow(S,2),Z),4),-1n),scale(pow(Z,2),2)),scale(mul(S,W),4)),scale(U,4),-1n),
 add(add(add(add(add(add(pow(S,5),scale(mul(pow(S,3),Z),5),-1n),scale(mul(S,pow(Z,2)),5)),scale(mul(pow(S,2),W),5)),scale(mul(Z,W),5),-1n),scale(mul(S,U),5),-1n),scale(V,5))
 ];
 if(expectedMoments.some((p,i)=>add(p,moments[i],-1n).size))throw Error("Newton moments");
 checks.push("first_five_Newton_moments");
 return {all_pass:true,arithmetic:"BigInt over five independent polynomial variables",checks,
          actual_cost_recomputed:false,no_positive_S2_inference:true,monomialBase:16,maximumTotalDegreeBound:10};
}
if(typeof process!=="undefined"&&process.argv.includes("--run")){
 const t=Date.now();const r=verifyCompanionSourceIdentities();r.runtimeMilliseconds=Date.now()-t;
 process.stdout.write(JSON.stringify(r,null,2)+"\n");
}
