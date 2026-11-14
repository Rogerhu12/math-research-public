#!/usr/bin/env node
// Exact rational independent checks for R117 (117.23).
// Direct side: differentiate Gauss curvature of s + epsilon*rho^2*f,
// using spatial Taylor jets and a separate first-order epsilon variable.
// Two-jet side: use only F0,F1,F2 and g0, dg0, K0 in the correlated formula.
// These are finite algebra checks, not a numerical candidate/source certificate.
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){const r=a%b;a=b;b=r;}return a;}
function R(n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return[n/g,d/g];}
const A=(a,b)=>R(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
const S=(a,b)=>R(a[0]*b[1]-b[0]*a[1],a[1]*b[1]);
const M=(a,b)=>R(a[0]*b[0],a[1]*b[1]);
const D=(a,b)=>R(a[0]*b[1],a[1]*b[0]);
const neg=a=>[-a[0],a[1]], eq=(a,b)=>a[0]*b[1]===b[0]*a[1];
const str=a=>a[1]===1n?String(a[0]):a[0]+"/"+a[1];
const sum=a=>a.reduce(A,R(0)), dot=(a,b)=>sum(a.map((x,i)=>M(x,b[i])));
const cross=(a,b)=>[S(M(a[1],b[2]),M(a[2],b[1])),S(M(a[2],b[0]),M(a[0],b[2])),S(M(a[0],b[1]),M(a[1],b[0]))];
const two=f=>[0,1].map(f), mat=f=>two(i=>two(j=>f(i,j)));
const det=a=>S(M(a[0][0],a[1][1]),M(a[0][1],a[1][0]));
function inverse(a){const z=det(a);return[[D(a[1][1],z),D(neg(a[0][1]),z)],[D(neg(a[1][0]),z),D(a[0][0],z)]];}
const trace=(a,b)=>sum(two(i=>sum(two(j=>M(a[i][j],b[i][j])))));
const bil=(a,x,y)=>sum(two(i=>sum(two(j=>M(M(a[i][j],x[i]),y[j])))));
const inner=(a,b,iv)=>sum(two(i=>sum(two(j=>sum(two(k=>sum(two(l=>M(M(iv[i][k],iv[j][l]),M(a[i][j],b[k][l]))))))))));
const N=4, indices=[];
for(let e=0;e<=1;e++)for(let i=0;i<=N;i++)for(let j=0;j<=N-i;j++)indices.push([i,j,e]);
const index=new Map(indices.map((v,k)=>[v.join(","),k]));
function J(c=R(0)){const a=indices.map(()=>R(0));a[0]=c;return a;}
const ja=(a,b)=>a.map((v,k)=>A(v,b[k]));
const js=(a,b)=>a.map((v,k)=>S(v,b[k]));
const jscale=(a,c)=>a.map(v=>M(v,c));
function jm(a,b){const c=J();for(let x=0;x<a.length;x++){if(a[x][0]===0n)continue;for(let y=0;y<b.length;y++){if(b[y][0]===0n)continue;const p=indices[x],q=indices[y];if(p[0]+q[0]+p[1]+q[1]>N||p[2]+q[2]>1)continue;const k=index.get([p[0]+q[0],p[1]+q[1],p[2]+q[2]].join(","));c[k]=A(c[k],M(a[x],b[y]));}}return c;}
function ji(a){const c=a[0];if(c[0]===0n)throw Error("singular jet");const r=js(J(R(1)),jscale(a,D(R(1),c)));let p=J(R(1)),s=p;for(let k=1;k<=N+1;k++){p=jm(p,r);s=ja(s,p);}return jscale(s,D(R(1),c));}
const jd=(a,b)=>jm(a,ji(b));
function partial(a,axis){const b=J();for(let k=0;k<a.length;k++){const p=indices[k].slice();if(!p[axis])continue;const factor=p[axis];p[axis]--;b[index.get(p.join(","))]=M(a[k],R(factor));}return b;}
function poly(terms){const a=J();for(const[i,j,n,d=1]of terms)a[index.get([i,j,0].join(","))]=R(n,d);return a;}
const eps=J();eps[index.get("0,0,1")]=R(1);
const val=a=>a[0];
const jdot=(a,b)=>a.reduce((s,v,k)=>ja(s,jm(v,b[k])),J());
const jdet=a=>js(jm(a[0][0],a[1][1]),jm(a[0][1],a[1][0]));
function jinv2(a){const z=ji(jdet(a));return[[jm(a[1][1],z),jscale(jm(a[0][1],z),R(-1))],[jscale(jm(a[1][0],z),R(-1)),jm(a[0][0],z)]];}
function firstChristoffel(g){return two(l=>mat((i,j)=>jscale(js(ja(partial(g[j][l],i),partial(g[i][l],j)),partial(g[i][j],l)),R(1,2))));}
function christoffelValue(g){const iv=inverse(g.map(row=>row.map(val))),c=firstChristoffel(g);return two(k=>mat((i,j)=>sum(two(l=>M(iv[k][l],val(c[l][i][j]))))));}
function curvature(g){
 const c=firstChristoffel(g),iv=jinv2(g);
 let q=jscale(js(js(jscale(partial(partial(g[0][1],0),1),R(2)),partial(partial(g[0][0],1),1)),partial(partial(g[1][1],0),0)),R(1,2));
 for(let k=0;k<2;k++)for(let l=0;l<2;l++)q=ja(q,jm(iv[k][l],js(jm(c[k][0][1],c[l][0][1]),jm(c[k][0][0],c[l][1][1]))));
 return jd(q,jdet(g));
}
function geometry(F){
 const d=two(i=>F.map(v=>partial(v,i))),d2=mat((i,j)=>F.map(v=>partial(partial(v,i),j)));
 const gamma=mat((i,j)=>jdot(d[i],d[j])),T=jdot(F,F),t=two(i=>jdot(F,d[i]));
 const s=mat((i,j)=>js(jd(gamma[i][j],T),jd(jm(t[i],t[j]),jm(T,T))));
 return{F,d,d2,gamma,T,t,s};
}
function correlated(z,g0){
 const F=z.F.map(val),F1=z.d.map(row=>row.map(val)),F2=z.d2.map(row=>row.map(v=>v.map(val)));
 const g=z.gamma.map(row=>row.map(val)),gg=g0.map(row=>row.map(val)),f=mat((i,j)=>S(gg[i][j],g[i][j]));
 const sv=z.s.map(row=>row.map(val)),iv=inverse(sv),giv=inverse(g),g0iv=inverse(gg);
 const cg=christoffelValue(z.gamma),cs=christoffelValue(z.s);
 const df=two(k=>mat((i,j)=>val(partial(js(g0[i][j],z.gamma[i][j]),k))));
 const cov=two(k=>mat((i,j)=>S(df[k][i][j],sum(two(l=>A(M(cg[l][k][i],f[l][j]),M(cg[l][k][j],f[i][l])))))));
 const dc=two(k=>mat((i,j)=>M(R(1,2),sum(two(l=>M(g0iv[k][l],S(A(cov[i][j][l],cov[j][i][l]),cov[l][i][j])))))));
 const bf=two(k=>mat((i,j)=>S(cg[k][i][j],cs[k][i][j])));
 const tau=two(k=>trace(bf[k],iv)),dt=two(k=>trace(dc[k],iv));
 let Q=A(A(bil(f,tau,tau),M(R(2),bil(gg,tau,dt))),bil(gg,dt,dt));
 for(let i=0;i<2;i++)for(let j=0;j<2;j++)for(let u=0;u<2;u++)for(let v=0;v<2;v++){
  const bi=two(k=>bf[k][i][j]),bu=two(k=>bf[k][u][v]),di=two(k=>dc[k][i][j]),du=two(k=>dc[k][u][v]);
  Q=S(Q,M(M(iv[i][u],iv[j][v]),A(A(bil(f,bi,bu),M(R(2),bil(gg,bi,du))),bil(gg,di,du))));
 }
 const Z=two(i=>S(sum(two(k=>A(M(f[i][k],tau[k]),M(gg[i][k],dt[k])))),
  sum(two(j=>sum(two(l=>sum(two(k=>M(iv[j][l],A(M(f[k][l],bf[k][i][j]),M(gg[k][l],dc[k][i][j])))))))))));
 const T=val(z.T),t=z.t.map(val),T2=M(T,T),T3=M(T2,T);
 const t2=mat((i,j)=>A(g[i][j],dot(F,F2[i][j])));
 const H=mat((i,j)=>A(S(D(M(R(8),M(t[i],t[j])),T3),D(M(R(2),t2[i][j]),T2)),
  D(M(R(2),sum(two(k=>M(cs[k][i][j],t[k])))),T2)));
 const C=cross(F1[1],F1[0]),G=dot(C,C),L=dot(C,F2[0][0]),B=dot(C,F2[0][1]),NN=dot(C,F2[1][1]);
 const Kgamma=D(S(M(L,NN),M(B,B)),M(G,G)),K0=val(curvature(g0));
 const Delta=M(S(Kgamma,K0),M(G,G));
 const dG=A(S(A(M(g[0][0],f[1][1]),M(g[1][1],f[0][0])),M(R(2),M(g[0][1],f[0][1]))),det(f));
 const curv=D(M(R(2),S(M(K0,dG),D(Delta,G))),det(sv));
 const main=D(A(S(Q,M(R(2),trace(f,iv))),curv),T);
 const result=S(A(S(main,D(M(R(4),bil(iv,t,Z)),T2)),inner(H,f,iv)),M(trace(H,iv),trace(f,iv)));
 const sLower=two(l=>mat((i,j)=>A(S(D(dot(F1[l],F2[i][j]),T),
  D(A(A(M(g[l][i],t[j]),M(g[l][j],t[i])),M(t[l],dot(F,F2[i][j]))),T2)),
  D(M(R(2),M(t[l],M(t[i],t[j]))),T3))));
 const alternateCs=two(k=>mat((i,j)=>sum(two(l=>M(iv[k][l],sLower[l][i][j])))));
 return{value:result,Kgamma,Delta,dG,cs,alternateCs,metricdet:G,metricdet2:det(g)};
}
function model(n,high){
 const u=n+1,h=high?u+3:0;
 const F=[
 poly([[1,0,1],[2,0,u,40],[1,1,-u,70],[0,2,1,30],[3,0,h,17],[1,2,-h,23]]),
 poly([[0,1,-1],[2,0,1,50],[1,1,u,60],[0,2,-u,80],[0,3,h,19],[2,1,h,29]]),
 poly([[0,0,1],[1,0,u,13],[0,1,-u,17],[2,0,u+1,11],[1,1,-u,31],[0,2,u+2,19],[3,0,-h,7],[1,2,h,37],[0,3,-h,41]])];
 const g0=[
 [poly([[0,0,u+4,2],[1,0,u,7],[0,1,-1,11],[2,0,1,5],[1,1,u,13],[0,2,1,17]]),
  poly([[0,0,u,31],[1,0,1,19],[0,1,u,23],[2,0,-1,29],[1,1,u,37],[0,2,1,41]])],
 [null,poly([[0,0,u+5,3],[1,0,-1,7],[0,1,u,11],[2,0,u,17],[1,1,-1,19],[0,2,u,23]])]];
 g0[1][0]=g0[0][1];return{F,g0};
}
export function certifyTwoJetSourceIdentity(){
 const gates=[],cases=[];let prior=null;
 function check(name,a,b){const ok=eq(a,b);gates.push({name,left:str(a),right:str(b),passed:ok});if(!ok)throw Error("failed exact identity: "+name+" "+str(a)+" != "+str(b));}
 for(let n=0;n<4;n++)for(const high of[false,true]){
  const {F,g0}=model(n,high),z=geometry(F),c=correlated(z,g0);
  const v=mat((i,j)=>ja(z.s[i][j],jm(eps,jd(js(g0[i][j],z.gamma[i][j]),z.T))));
  const direct=M(R(2),curvature(v)[index.get("0,0,1")]),name="model"+n+(high?"_third_jets_changed":"_quadratic");
  check(name+": spherical chart has K=1",val(curvature(z.s)),R(1));
  check(name+": direct Gauss first variation = correlated two-jet source",direct,c.value);
  check(name+": Gauss numerator orientation",val(curvature(z.gamma)),c.Kgamma);
  check(name+": cross determinant",c.metricdet,c.metricdet2);
  check(name+": correlated determinant defect",c.dG,S(val(jdet(g0)),val(jdet(z.gamma))));
  for(let k=0;k<2;k++)for(let i=0;i<2;i++)for(let j=0;j<2;j++)
   check(name+": cancelled radial-projection Christoffel "+k+i+j,c.cs[k][i][j],c.alternateCs[k][i][j]);
  const exact=correlated(z,z.gamma);
  check(name+": full exact metric source zero",exact.value,R(0));
  if(high)check("model"+n+": all changed third jets cancel in actual source",direct,prior);else prior=direct;
  cases.push({name,source_C_rho2_f:str(direct),Newton_source:str(M(R(-1,2),direct))});
 }
 return{kind:"R117_independent_exact_two_jet_identity",execution:"actual V8 BigInt rational algebra",
  spatial_Taylor_order:N,epsilon_order:1,cases,gates,gate_count:gates.length,passed:gates.every(x=>x.passed),
  scope:"Finite independent exact checks of (117.23), Gauss signs, spherical chart, mean-preserving determinant identity, and cancellation of changed third jets. These do not evaluate the repository candidate or execute the Python interval producer."};
}
if(typeof process!=="undefined"&&process.argv?.[1]&&import.meta.url===new URL("file://"+process.argv[1]).href){
 const {writeFileSync}=await import("node:fs");const report=certifyTwoJetSourceIdentity();
 const output=JSON.stringify(report,null,2)+"\n";
 if(process.argv[2])writeFileSync(process.argv[2],output);else process.stdout.write(output);
}
