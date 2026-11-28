#!/usr/bin/env node
/** True normal length correction and a clamped material clock for the resulting meridians. */
import {readFileSync,writeFileSync} from 'node:fs';
import {pathToFileURL} from 'node:url';
import {compactClock} from './2ecf-compact-p32-two-material-clocks.mjs';
import {compactNormalModel,gauss01,observeNormal} from './2ecf-compact-p32-normal-meridian-design.mjs';
function meridianCorrection(model,z,p,N=48,degree=8){
 const pi=Math.PI,clock=compactClock(10,5,z),[xx,ww]=gauss01(degree),ends=Array.from(new Set([...Array.from({length:14},(_,i)=>i/13),...Array.from({length:16},(_,i)=>i/15)])).sort((a,b)=>a-b),grid=[];
 for(let i=0;i<ends.length-1;i++)for(let j=0;j<degree;j++){let w=ends[i+1]-ends[i];grid.push([ends[i]+w*xx[j],w*ww[j]]);}
 const g=grid.map(([t,w])=>w*Math.sqrt(clock.goal(t)[0])).reduce((a,b)=>a+b,0),dot=(v,w)=>v[0]*w[0]+v[1]*w[1]+v[2]*w[2];
 function profile(t){const x=t*(1-t),q=1-2*t;return [64*x**3,192*x*x*q,384*x*q*q-384*x*x];}
 function ray(u){let a=grid.map(([t,w])=>{const Y=model.jet(p,t,u),[P,n]=model.base(t,u),[h,d]=profile(t),v=n[0].map((z,j)=>d*z+h*n[1][j]),V=Y[1];return [w,dot(V,V),dot(V,v),dot(v,v)];});
  return x=>{let v=0,d=0;for(let [w,E,F,G] of a){let q=Math.sqrt(E+2*x*F+x*x*G);v+=w*q;d+=w*(F+x*G)/q;}return [v/g-1,d/g];};
 }
 const vals=[],before=[],after=[],slopes=[];
 for(let i=0;i<=N;i++){const length=ray(pi*i/(2*N));let a=0,[v,d]=length(a);before.push(v);for(let s=0;s<10;s++){if(Math.abs(d)<.02)throw Error('Ray correction is singular');a-=v/d;[v,d]=length(a);if(Math.abs(v)<5e-15)break;}vals.push(a);after.push(v);slopes.push(d);}
 const coeff=Array.from({length:N+1},(_,k)=>{let r=0;for(let j=0;j<=N;j++)r+=vals[j]*Math.cos(pi*j*k/N)*(j===0||j===N?.5:1);return r*(k===0||k===N?1:2)/N;});
 return {coef:coeff,range:[Math.min(...vals),Math.max(...vals)],before:[Math.min(...before),Math.max(...before)],maxRootResidual:Math.max(...after.map(Math.abs)),derivative:[Math.min(...slopes),Math.max(...slopes)],lengthTarget:g,pointsPerRay:grid.length};
}
function correctedModel(model,coeff){
 const pi=Math.PI,alpha=u=>{let d=[0,0,0];for(let k=0;k<coeff.length;k++){let m=2*k,x=coeff[k],c=Math.cos(m*u),s=Math.sin(m*u);d[0]+=x*c;d[1]-=m*x*s;d[2]-=m*m*x*c;}return d;};
 return {jet(p,t,u){const Y=model.jet(p,t,u),[base,n]=model.base(t,u),[a,ap,app]=alpha(u),x=t*(1-t),q=1-2*t,w=64*x**3,wp=192*x*x*q,wpp=384*x*q*q-384*x*x,der=[w*a,wp*a,w*ap,wpp*a,wp*ap,w*app];
 const Z=[n[0].map(v=>der[0]*v),n[0].map((v,k)=>der[1]*v+der[0]*n[1][k]),n[0].map((v,k)=>der[2]*v+der[0]*n[2][k]),n[0].map((v,k)=>der[3]*v+2*der[1]*n[1][k]+der[0]*n[3][k]),n[0].map((v,k)=>der[4]*v+der[1]*n[2][k]+der[2]*n[1][k]+der[0]*n[4][k]),n[0].map((v,k)=>der[5]*v+2*der[2]*n[2][k]+der[0]*n[5][k])];return Y.map((v,i)=>v.map((x,k)=>x+Z[i][k]));},alpha};
}
function equalizeMeridians(model,z,p,nr=44,M=24,K=64,H=480){
 const pi=Math.PI,cl=compactClock(10,5,z),h=1/(nr+3),norm=x=>Math.hypot(...x),dot=(x,y)=>x[0]*y[0]+x[1]*y[1]+x[2]*y[2],nk=M+1;
 function b3(x){const a=Math.abs(x),s=Math.sign(x);if(a>=2)return [0,0,0];return a>1?[(2-a)**3/6,-s*(2-a)**2/2,2-a]:[2/3-a*a+.5*a**3,s*(-2*a+1.5*a*a),-2+3*a];}
 const radial=t=>{let arr=[];for(let j=Math.max(0,Math.floor(t/h)-3);j<Math.min(nr,Math.floor(t/h)+1);j++){let [v,d,dd]=b3(t/h-j-2);arr.push([j,h*v,d,dd/h]);}return arr;};
 const v0=Array.from({length:H+1},(_,j)=>Math.sqrt(cl.goal(j/H)[0])),d0=v0.map((v,i)=>i===0?(v0[1]-v)*H:i===H?(v-v0[H-1])*H:(v0[i+1]-v0[i-1])*H/2);
 function cumulative(v,d){let y=[0];for(let j=0;j<H;j++)y.push(y.at(-1)+(v[j]+v[j+1])/(2*H)+(d[j]-d[j+1])/(12*H*H));return y;}
 const A0=cumulative(v0,d0),L=A0[H],rows=Array.from({length:H+1},(_,i)=>radial(i/H)),a0=Array.from({length:H+1},()=>new Float64Array(nk)),a1=Array.from({length:H+1},()=>new Float64Array(nk));let worstDelta=0;
 for(let k=0;k<=K;k++){const u=pi*k/(2*K),vals=Array.from({length:H+1},(_,j)=>{let x=model.jet(p,j/H,u),a=norm(x[1]);return [a,dot(x[1],x[3])/a];}),v=vals.map(x=>x[0]),d=vals.map(x=>x[1]),A=cumulative(v,d),delta=A[H]-L;worstDelta=Math.max(worstDelta,Math.abs(delta/L));
  function val(j,y){let w=v[j],x=v[j+1],f=d[j]/H,g=d[j+1]/H,a=-3*w+3*x-2*f-g,b=2*w-2*x+f+g;return [A[j]+(w*y+f*y*y/2+a*y**3/3+b*y**4/4)/H,w+f*y+a*y*y+b*y**3];}
  const trig=Array.from({length:nk},(_,m)=>Math.cos(pi*k*m/K)*(k===0||k===K?.5:1)*(m===0||m===K?1:2)/K);
  let bin=0;for(let j=0;j<=H;j++){let t=j/H,b=t**3*(10+t*(-15+6*t)),bp=30*(t*(1-t))**2,goal=A0[j]+delta*b;
   while(bin<H-1&&A[bin+1]<goal)bin++;let y=Math.max(0,Math.min(1,(goal-A[bin])/(A[bin+1]-A[bin])));for(let i=0;i<4;i++){let [l,a]=val(bin,y);y=Math.max(0,Math.min(1,y-(l-goal)*H/a));}
   let x=(bin+y)/H,first=(v0[j]+delta*bp)/val(bin,y)[1]-1;for(let m=0;m<nk;m++){a0[j][m]+=(x-t)*trig[m];a1[j][m]+=first*trig[m];}
  }
 }
 const G=Array.from({length:nr},()=>new Float64Array(nr)),rhs=Array.from({length:nr},()=>new Float64Array(nk));
 for(let i=0;i<=H;i++){let wt=i===0||i===H?.5:1,row=rows[i],v0=a0[i],v1=a1[i];
  for(let [j,b,d] of row){for(let [k,c,e] of row)G[j][k]+=wt*(b*c+.008*d*e);for(let m=0;m<nk;m++)rhs[j][m]+=wt*(b*v0[m]+.008*d*v1[m]);}}
 for(let j=0;j<nr;j++){if(!(G[j][j]>1e-12))throw Error('Positive normal diagonal required');let val=G[j][j];for(let k=j;k<nr;k++)G[j][k]/=val;for(let m=0;m<nk;m++)rhs[j][m]/=val;
  for(let i=0;i<nr;i++)if(i!==j&&G[i][j]!==0){let f=G[i][j];for(let k=j;k<nr;k++)G[i][k]-=f*G[j][k];for(let m=0;m<nk;m++)rhs[i][m]-=f*rhs[j][m];}}
 const out=rhs.flatMap(x=>Array.from(x));return {coeff:out,nr,M,K,H,inputMeridianMeanTarget:L,maxDiscreteMeridianLengthMismatch:worstDelta};
}
function materialRadialModel(model,coef,nr,M){
 const h=1/(nr+3),modes=M+1;return {jet(p,t,u){
  let T=[t,1,0,0,0,0];const cos=Array.from({length:modes},(_,i)=>Math.cos(2*i*u)),sin=Array.from({length:modes},(_,i)=>Math.sin(2*i*u));
  for(let j=Math.max(0,Math.floor(t/h)-3);j<Math.min(nr,Math.floor(t/h)+1);j++){let x=t/h-j-2,a=Math.abs(x),s=Math.sign(x),b,d,dd;if(a>=2)continue;
   if(a>1){b=(2-a)**3/6;d=-s*(2-a)**2/2;dd=2-a;}else{b=2/3-a*a+.5*a**3;d=s*(-2*a+1.5*a*a);dd=-2+3*a;}
   let f=0,g=0,v=0;for(let k=0;k<modes;k++){let c=coef[j*modes+k],m=2*k;f+=c*cos[k];g-=c*m*sin[k];v-=c*m*m*cos[k];}T[0]+=h*b*f;T[1]+=d*f;T[2]+=h*b*g;T[3]+=dd*f/h;T[4]+=d*g;T[5]+=h*b*v;
  }
  const [P,V,U,A,B,C]=model.jet(p,T[0],u),[q,a,b,c,d,e]=T;return [P,V.map(x=>x*a),U.map((x,k)=>x+b*V[k]),A.map((x,k)=>a*a*x+c*V[k]),A.map((x,k)=>a*b*x+a*B[k]+d*V[k]),A.map((x,k)=>b*b*x+2*b*B[k]+C[k]+e*V[k])];
 },derivativeLower(){let peak=0;for(let j=0;j<=nr;j++){let v=0;for(let k=0;k<modes;k++)v+=Math.abs((j<nr?coef[j*modes+k]:0)-(j>0?coef[(j-1)*modes+k]:0));peak=Math.max(peak,v);}return 1-peak-1e-12;}};
}
export {meridianCorrection,correctedModel,equalizeMeridians,materialRadialModel};
if(process.argv[1]&&import.meta.url===pathToFileURL(process.argv[1]).href){
 const [op,state,clock,shape,extra,rad]=process.argv.slice(2),read=x=>JSON.parse(readFileSync(x)),z=read(state),w=read(clock),p=read(shape),m=compactNormalModel(z,w,12,7);
 if(op==='correct'){const a=meridianCorrection(m,z,p,48,8);writeFileSync(extra,JSON.stringify(a.coef)+'\n');const {coef,...stats}=a;console.log(JSON.stringify(stats));}
 else if(op==='observeCorrection')console.log(JSON.stringify(['G10a','G10b','G11'].map(g=>observeNormal(correctedModel(m,read(extra)),p,z,g)),null,2));
 else if(op==='fitRadial'){const a=equalizeMeridians(correctedModel(m,read(extra)),z,p,44,24,64,480);writeFileSync(rad,JSON.stringify(a.coeff)+'\n');const {coeff,...stats}=a;console.log(JSON.stringify(stats));}
 else if(op==='observeRadial'){const a=materialRadialModel(correctedModel(m,read(extra)),read(rad),44,24);console.log(JSON.stringify({derivativeLower:a.derivativeLower(),full:['G10a','G10b','G11'].map(g=>observeNormal(a,p,z,g))},null,2));}
 else throw Error('correct | observeCorrection | fitRadial | observeRadial; STATE192 CLOCK100 SHAPE84 EXTRA49 [RAD1100]');
}
