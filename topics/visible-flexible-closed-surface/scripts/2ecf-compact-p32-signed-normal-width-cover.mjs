#!/usr/bin/env node
import {readFileSync} from 'node:fs';
import {pathToFileURL} from 'node:url';
import {compactCurvatureCover} from './2ecf-compact-p32-full-curvature.mjs';
function signedNormalWidth(z,clock,height,extra=null,upper=.89765,budget=1500000){
 return compactCurvatureCover(z,8,8,10.305,1,0,0,({radialNode,angularPanel,vector,real,lambda,plus,prod,times,norm})=>{
 const low=x=>x-1e-13*(1+Math.abs(x)),hi=x=>x+1e-13*(1+Math.abs(x)),minus=(a,b)=>[low(a[0]-b[1]),hi(a[1]-b[0])],one=[1,1],zero=[0,0],pi=3.141592653589793;
 const reciprocal=a=>a[0]>0?[low(1/a[1]),hi(1/a[0])]:null,ext=a=>Math.max(-a[0],a[1]),fac=real(lambda),pival=[low(pi),hi(pi)],uScale=reciprocal(times(pival,.5));
 function valueB(x){let a=Math.abs(x);return a>=2?0:a>1?(2-a)**3/6:2/3-a*a+.5*a**3;}
 function binterval(t,nr){let h=1/(nr+3),out=[];for(let k=Math.max(0,Math.floor((nr+3)*t[0])-4);k<Math.min(nr,Math.floor((nr+3)*t[1])+2);k++){let l=low((nr+3)*t[0]-k-2),r=hi((nr+3)*t[1]-k-2),a=l<=0&&r>=0?0:Math.min(Math.abs(l),Math.abs(r)),b=Math.max(Math.abs(l),Math.abs(r));if(a>=2)continue;out.push([k,[Math.max(0,low(valueB(b))),hi(valueB(a))]]);}return out;}
 function restrict(a,b){let l=Math.max(0,a),r=Math.min(1,b);if(r<l)throw Error('Clock outside closed quadrant');let d=Math.max(0,Math.min(14,Math.floor(-Math.log2(Math.max(1e-13,r-l))))),n=2**d,i=Math.max(0,Math.min(n-1,Math.floor(n*l))),j=Math.max(0,Math.min(n-1,Math.floor(n*r)));return Array.from({length:j-i+1},(_,k)=>[i+k,d]);}
 const bool=(a,cut)=>a[0]>-cut&&a[1]<cut,pCache=new Map();
 function original(rr,tt){const key=rr.join('/')+','+tt.join('/');if(pCache.has(key))return pCache.get(key);
  const T=angularPanel(...tt),R=radialNode(...rr),[P,V,U]=vector(R.b,T,[[0,0],[1,0],[0,1]]),n=[0,1,2].map(k=>minus(prod(V[(k+1)%3],U[(k+2)%3]),prod(V[(k+2)%3],U[(k+1)%3]))),ss=norm(n),den=[low(Math.sqrt(Math.max(.13347,ss[0]))),hi(Math.sqrt(ss[1]))],ny=prod(n[1],reciprocal(den));const result=[P[1],[Math.max(-1,ny[0]),Math.min(1,ny[1])]];pCache.set(key,result);return result;}
 let visits=0,closed=0,failed=0,witness=[],maxAccepted=0,deep=0;const absExtra=extra?hi(extra.reduce((s,v)=>s+Math.abs(v),0)):0;
 function visit(i,d,j,a){if(++visits>budget)throw Error('visit budget; unresolved');const t=[i/2**d,(i+1)/2**d],v=[j/2**a,(j+1)/2**a],ang=angularPanel(j,a),c=Array.from({length:8},(_,k)=>ang.f[16+k][0]),sin=k=>times(ang.f[16+k][1],-1/(2*k)),T0=binterval(t,10),H0=binterval(t,12);let T=t,U=v,H=[low(-absExtra),hi(absExtra)];
  for(let [k,p] of T0){let tval=zero,uval=zero;for(let m=0;m<5;m++){tval=plus(tval,times(c[m],clock[(k*2)*5+m]));uval=plus(uval,times(sin(m+1),clock[(k*2+1)*5+m]/(2*(m+1))));}T=plus(T,times(prod(p,tval),1/13));U=plus(U,prod(prod(p,uval),uScale));}
  for(let [k,p] of H0){let hh=zero;for(let m=0;m<7;m++)hh=plus(hh,times(c[m],height[k*7+m]));H=plus(H,prod(p,hh));}
  let max=0;for(let rr of restrict(...T))for(let tt of restrict(...U)){const [pos,ny]=original(rr,tt),y=prod(fac,plus(pos,prod(H,ny)));max=Math.max(max,ext(y));}
  if(max<upper){closed++;maxAccepted=Math.max(maxAccepted,max);deep=Math.max(deep,d+a);return;}if(d+a>=27){failed++;if(witness.length<6)witness.push([i,d,j,a,max]);return;}
  if(d<=a+1){visit(2*i,d+1,j,a);visit(2*i+1,d+1,j,a);}else{visit(i,d,2*j,a+1);visit(i,d,2*j+1,a+1);}
 }
 for(let i=0;i<16;i++)for(let j=0;j<16;j++)visit(i,4,j,4);
 return {upper,visited:visits,closed,unresolved:failed,maximumAccepted:maxAccepted,deepestSum:deep,witness,extraCoefficientBound:absExtra};
 });
}
export {signedNormalWidth};
if(process.argv[1]&&import.meta.url===pathToFileURL(process.argv[1]).href){
 const [state,clock,normal,extra]=process.argv.slice(2),read=x=>JSON.parse(readFileSync(x)),r=signedNormalWidth(read(state),read(clock),read(normal),read(extra),.8955,380000);
 console.log(JSON.stringify(r,null,2));if(r.unresolved)process.exitCode=1;
}
