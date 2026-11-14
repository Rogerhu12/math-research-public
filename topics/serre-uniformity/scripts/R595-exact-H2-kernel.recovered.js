"use strict";
// Exact core reconstructed from the surviving original tool-call text.
// The old long R595 orchestration wrapper is not this file.
// No mathematics was rerun during environment recovery.

function exactH2KernelRationals(){
 const SCALE=4n*5184n*5184n;
 const mulc=(a,b)=>{const v=a*b;if(v%SCALE)throw Error("insufficient fixed denominator");return v/SCALE;};
 const rat=(n,d=1)=>{const a=BigInt(n)*SCALE,b=BigInt(d);if(a%b)throw Error("denominator");return a/b;};
 const trim=a=>{while(a.length>1&&a.at(-1)===0n)a.pop();return a;};
 const pa=(a,b)=>trim(Array.from({length:Math.max(a.length,b.length)},(_,i)=>(a[i]||0n)+(b[i]||0n)));
 const ps=(c,a)=>trim(a.map(v=>mulc(c,v)));
 const pm=(a,b)=>{const c=Array(a.length+b.length-1).fill(0n);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)c[i+j]+=mulc(a[i],b[j]);return trim(c);};
 const pd=a=>a.slice(1).map((v,i)=>v*BigInt(i+1));
 const DD=[-64,0,0,48,0,0,-228,0,0,1].map(x=>rat(x));
 const rem=a=>{a=a.slice();for(let k=a.length-1;k>=9;k--)if(a[k]){const c=a[k];for(let j=0;j<=9;j++)a[k-9+j]-=mulc(c,DD[j]);}return trim(a.slice(0,9));};
 const qp={},dp=[[SCALE]];
 function qpow(n){if(!qp[n]){const a=Array(n+1).fill(0n);a[n]=SCALE;qp[n]=rem(a);}return qp[n];}
 function dpow(n){while(dp.length<=n)dp.push(pm(dp.at(-1),DD));return dp[n];}
 const clean=a=>new Map([...a].filter(([k,v])=>v!==0n));
 const add=(a,b)=>{const c=new Map(a);for(const[k,v]of b)c.set(k,(c.get(k)||0n)+v);return clean(c);};
 const sc=(c,a)=>clean(new Map([...a].map(([k,v])=>[k,mulc(c,v)])));
 const ONE=new Map([["0,0,0,0,0",SCALE]]),ZERO=new Map();
 const choose=(n,k)=>{let c=1;for(let i=1;i<=k;i++)c=c*(n-i+1)/i;return c;};
 function mul(a,b){
  const out=new Map();for(const[ka,va]of a)for(const[kb,vb]of b){
   const aa=ka.split(",").map(Number),bb=kb.split(",").map(Number),[ee,yy,qq,dd,xx]=aa.map((v,i)=>v+bb[i]),yr=Math.floor(yy/2),qr=qpow(qq),v=mulc(va,vb);
   for(let t=0;t<=yr;t++){const yc=BigInt(choose(yr,t)*((-1)**(yr-t)));for(let r=0;r<qr.length;r++)if(qr[r]){const k=[ee,yy%2,r,dd,xx+3*t].join(",");out.set(k,(out.get(k)||0n)+mulc(v,qr[r])*yc);}}
  }return clean(out);
 }
 function power(a,n){let b=ONE;while(n){if(n%2)b=mul(b,a);n=Math.floor(n/2);if(n)a=mul(a,a);}return b;}
 const variable=i=>new Map([[Array.from({length:5},(_,j)=>+(i===j)).join(","),SCALE]]);
 const[E,Y,Q,dd,X]=Array.from({length:5},(_,i)=>variable(i));
 const q31=add(power(Q,3),sc(rat(-1),ONE));
 const plus=(a,b)=>[add(a[0],b[0]),add(a[1],b[1])];
 const scale=(c,a)=>[sc(c,a[0]),sc(c,a[1])];
 const times=(a,b)=>[add(mul(a[0],b[0]),mul(q31,mul(a[1],b[1]))),add(mul(a[0],b[1]),mul(a[1],b[0]))];
 function pp(a,n){let b=[ONE,ZERO];while(n){if(n%2)b=times(b,a);n=Math.floor(n/2);if(n)a=times(a,a);}return b;}
 const eh=mul(power(Q,2),add(add(sc(rat(-19,5184),power(Q,6)),sc(rat(541,648),power(Q,3))),sc(rat(-1,324),ONE)));
 const slope=[mul(Y,dd),sc(rat(-1),dd)];
 const xp=plus(pp(slope,2),[sc(rat(-1),add(X,Q)),ZERO]);
 const yp=plus([sc(rat(-1),Y),ZERO],times(slope,plus([X,ZERO],scale(rat(-1),xp))));
 const ep=[add(E,mul(Y,dd)),add(eh,sc(rat(-1),dd))];
 const T2=scale(rat(-1,2),plus(plus(times(pp(ep,2),yp),scale(rat(2),times(ep,pp(xp,2)))),times(xp,yp)));
 const odd=T2[1],maxd=Math.max(...[...odd.keys()].map(k=>+k.split(",")[3])),tr={};
 const Num=[-8,0,0,34,0,0,1].map(x=>rat(x));
 for(let k=0;k<9;k++){const xx=Array(k+3).fill(0n);xx[k+2]=rat(3);const v=rem(pm(xx,Num));tr[k+",0"]=[v[8]||0n];tr[k+",1"]=v;for(let n=1;n<maxd;n++)tr[k+","+(n+1)]=pa(pm(pd(DD),tr[k+","+n]),ps(rat(-1,n),pm(DD,pd(tr[k+","+n]))));}
 const out={};
 for(const[key,c]of odd){const[a,y,q,n,x]=key.split(",").map(Number),v=n===0?pm(tr[q+",0"],dpow(maxd)):pm(tr[q+","+n],dpow(maxd-n)),poly=Array(x).fill(0n).concat(ps(c,v)),k=a+","+y;out[k]=pa(out[k]||[0n],poly);}
 const gcd=(a,b)=>{a=a<0n?-a:a;while(b)[a,b]=[b,a%b];return a;};
 const rows={};for(const[k,poly]of Object.entries(out)){rows[k]=poly.map(v=>{let g=gcd(v,SCALE);return[(v/g).toString(),(SCALE/g).toString()];});}
 return{common_factor:"H2/C0=-1/3 times sum E^a y^b N_ab(x)/D(x)^3",denominator_power:maxd,terms:rows,source:"Exact Q arithmetic with common denominator4*5184^2, all intermediate divisions asserted integral"};
}

if (typeof module !== "undefined") {
  module.exports = { exactH2KernelRationals };
  if (require.main === module) process.stdout.write(JSON.stringify(exactH2KernelRationals(), null, 2) + "\n");
}
