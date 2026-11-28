#!/usr/bin/env node
/** Exhaustive material BVT for both closed flat disks, both transitions and the entire center. */
import {readFileSync} from 'node:fs';
import {pathToFileURL} from 'node:url';
import {compactCurvatureCover} from './2ecf-compact-p32-full-curvature.mjs';
function compactPairCover(z,depth=11,quarter=6,gramOrder=7,limit=12000000){
 return compactCurvatureCover(z,8,8,10.305,1,0,0,({angularPanel,radialNode,vector,real,lambda,plus,prod,norm,dot,times})=>{
 const V=real(lambda), fac=V[1],L=.1015625,r0=.35,h0=.54,piHi=3.141592653589795,sq=x=>x*x,hi=x=>x+1e-13*(1+Math.abs(x)),lo=x=>x-1e-13*(1+Math.abs(x)),mirror=(a,sign)=>sign===1?a:[-a[1],-a[0]],unch=[0,0];
 const n=2**gramOrder, ng=2**quarter, slab=Array.from({length:n},()=>[0,0,0]);
 for(let i=0;i<n;i++)for(let j=0;j<ng;j++){
  const [v,u]=vector(radialNode(i,gramOrder).b,angularPanel(j,quarter),[[1,0],[0,1]]);
  const e=norm(v),f=dot(v,u),g=norm(u),x=slab[i];x[0]=Math.max(x[0],hi(fac*fac*e[1]));x[1]=Math.max(x[1],hi(fac*fac*Math.max(-f[0],f[1])));x[2]=Math.max(x[2],hi(fac*fac*g[1]));
 }
 const range=[slab];while(range.at(-1).length>1){let a=range.at(-1);range.push(Array.from({length:a.length/2},(_,i)=>a[2*i].map((x,k)=>Math.max(x,a[2*i+1][k]))));}
 function gram(a,b){const x=[0,0,0],f2=hi(fac*fac);if(a>b)[a,b]=[b,a];
  if(a<=L&&b>=-L){x[0]=f2;x[2]=f2;}
  for(let sign of [-1,1]){let l=sign===1?a:-b,h=sign===1?b:-a;
   if(h>=1+L){const r=hi(Math.max(0,Math.min(r0,1+L+r0-l)));x[0]=Math.max(x[0],f2);x[2]=Math.max(x[2],hi(f2*r*r));}
   if(l<=1+L&&h>=L){let i=Math.max(0,Math.min(n-1,Math.floor(lo((l-L)*n)))),j=Math.max(0,Math.min(n-1,Math.floor(hi((h-L)*n))));
    while(i<=j){let p=0;while((i%(2**(p+1)))===0&&i+2**(p+1)-1<=j)p++;
     const s=range[p][i/2**p];for(let k=0;k<3;k++)x[k]=Math.max(x[k],s[k]);i+=2**p;}}
  }return x;
 }
 let next=0;const posCache=new Map(),root=[];
 function local(domain,i,d,j,l,needV){
  const key=domain+','+i+','+d+','+j+','+l+(needV?',v':'');if(posCache.has(key))return posCache.get(key);
  const T=angularPanel(j,l),a=i/2**d,b=(i+1)/2**d;let vals;
  if(domain===1)vals=vector(radialNode(i,d).b,T,needV?[[1,0],[0,1]]:[[0,0]]);
  else if(domain===0){const depth=[lo((2*a-1)*L),hi((2*b-1)*L)];
   vals=needV?[[unch,unch,[1,1]],[...T.gamma[1],unch]]:[[...T.gamma[0],depth]];}
  else{const rad=[lo(r0*(1-b)),hi(r0*(1-a))];
   vals=needV?[[...T.e[0],unch],[prod(rad,T.e[1][0]),prod(rad,T.e[1][1]),unch]]:[[prod(rad,T.e[0][0]),prod(rad,T.e[0][1]),[lo(h0),hi(h0)]]];}
  vals=vals.map(a=>a.map(x=>prod(x,V)));posCache.set(key,vals);return vals;
 }
 function make(dom,sgn,q,i,d,j,l){
  const scale=2**d,a=i/scale,b=(i+1)/scale,ui=j/2**l,uj=(j+1)/2**l;
  let m=dom===0?[(2*a-1)*L,(2*b-1)*L]:dom===1?[L+a,L+b]:[1+L+r0*a,1+L+r0*b];
  if(sgn<0)m=[-m[1],-m[0]];
  const s0=lo(m[0]),s1=hi(m[1]),uc=q%2===0?q+(ui+uj)/2:q+1-(ui+uj)/2,uh=(uj-ui)/2;
  const sign=[q===1||q===2?-1:1,q>=2?-1:1,sgn],p=local(dom,i,d,j,l,false)[0].map((v,k)=>mirror(v,sign[k]));
  const wd=Math.max(...p.map(v=>v[1]-v[0])),sizeR=dom===0?2*L/scale:dom===1?1.6/scale:r0/scale,
      sizeU=(dom===2?Math.max(.045,r0*(1-a)):1)*piHi*uh;
  return {id:next++,dom,sgn,q,i,d,j,l,s0,s1,uc,uh,p,sign,wd,sizeR,sizeU};
 }
 for(let q=0;q<4;q++){root.push(make(0,1,q,0,0,0,0));for(let s of [1,-1])for(let k of [1,2])root.push(make(k,s,q,0,0,0,0));}
 function kids(a){if(a.children)return a.children;const {dom,sgn,q,i,d,j,l}=a,rr=(a.sizeR>=a.sizeU||l===depth)&&d<depth;
  return a.children=rr?[make(dom,sgn,q,2*i,d+1,j,l),make(dom,sgn,q,2*i+1,d+1,j,l)]:[make(dom,sgn,q,i,d,2*j,l+1),make(dom,sgn,q,i,d,2*j+1,l+1)];}
 function tangent(a){return a.V||(a.V=local(a.dom,a.i,a.d,a.j,a.l,true).map(v=>v.map((x,k)=>mirror(x,a.sign[k]))));}
 const counts={sameFlat:0,far:0,shortPath:0,tangent:0},rho2=.194*.194,short2=sq(3.14159265/10.306);let tried=0,miss=0,example=[];
 function visit(a,b){if(++tried>limit)throw Error('Pair visit limit '+JSON.stringify([tried,miss,example.slice(0,2)]));
  if(a.dom===2&&b.dom===2&&a.sgn===b.sgn){counts.sameFlat++;return;}
  let dist=0;for(let k=0;k<3;k++)dist+=sq(Math.max(0,a.p[k][0]-b.p[k][1],b.p[k][0]-a.p[k][1]));if(lo(dist)>hi(rho2)){counts.far++;return;}
  let du0=Math.abs(a.uc-b.uc),du=hi(Math.min(2,Math.min(du0,4-du0)+a.uh+b.uh)*piHi/2),ds=hi(Math.max(a.s1-b.s0,b.s1-a.s0));
  if(ds<.6&&du<2.4){const G=gram(Math.min(a.s0,b.s0),Math.max(a.s1,b.s1)),e=G[0]*ds*ds+2*G[1]*ds*du+G[2]*du*du;if(hi(e)<lo(short2)){counts.shortPath++;return;}}
  if(a!==b&&Math.max(a.wd,b.wd)<.14){const dx=b.p.map((x,k)=>[lo(x[0]-a.p[k][1]),hi(x[1]-a.p[k][0])]);for(let q of [a,b])for(let v of tangent(q)){let w=dot(v,dx);if(w[0]>0||w[1]<0){counts.tangent++;return;}}}
  const canA=a.d<depth||a.l<depth,canB=b.d<depth||b.l<depth;if(!canA&&!canB){miss++;if(example.length<6)example.push([a,b].map(x=>[x.dom,x.sgn,x.q,x.i,x.d,x.j,x.l]));return;}
  if(a===b){let [l,r]=kids(a);visit(l,l);visit(l,r);visit(r,r);}
  else if(canA&&(!canB||a.wd>=b.wd)){for(let c of kids(a))visit(c,b);}
  else for(let c of kids(b))visit(a,c);
 }
 for(let i=0;i<root.length;i++)for(let j=i;j<root.length;j++)visit(root[i],root[j]);
 return {depth,quarter,gramOrder,visited:tried,distinctNodes:next,accepted:counts,unresolved:miss,example,globalGram:range.at(-1)[0],range:root.length,complete:miss===0};
 });
}
export {compactPairCover};
if(process.argv[1] && import.meta.url===pathToFileURL(process.argv[1]).href){
 const [state,d='9',a='5',r='6']=process.argv.slice(2);
 if(!state)throw Error('Expected regenerated p32-192.json');
 const result=compactPairCover(JSON.parse(readFileSync(state)),Number(d),Number(a),Number(r),7500000);
 console.log(JSON.stringify(result,null,2));if(!result.complete)process.exitCode=1;
}
