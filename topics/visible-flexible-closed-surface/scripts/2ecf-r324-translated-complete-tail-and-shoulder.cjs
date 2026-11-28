'use strict';
// Interval operations cover binary64 nearest rounding with a redundant relative/absolute margin.
const guard=2**-47;
function out(l,h){return [l-guard*(1+Math.abs(l)),h+guard*(1+Math.abs(h))]}
const point=x=>[x,x], plus=(a,b)=>out(a[0]+b[0],a[1]+b[1]), neg=a=>[-a[1],-a[0]], sub=(a,b)=>plus(a,neg(b));
function mul(a,b){const t=a[0]*b[0],v=a[1]*b[1],w=a[0]*b[1],z=a[1]*b[0];return out(Math.min(t,v,w,z),Math.max(t,v,w,z))}
function sq(a){const x=a[0]**2,y=a[1]**2;return out(a[0]<=0&&a[1]>=0?0:Math.min(x,y),Math.max(x,y))}
function div(a,b){if(b[0]<=0)throw Error('positive denominator required');return mul(a,out(1/b[1],1/b[0]))}
const one=point(1), zero=point(0);
function rootmin(x){if(x<0)throw Error('negative square sum');let y=Math.max(0,Math.sqrt(x)-1e-11);if(sq(point(y))[1]>x)throw Error('unverified lower sqrt');return y}

function q(x){return out(x,x)}
function val(x){return Math.max(-x[0],x[1])}
function absI(x){return x[0]>=0?x:x[1]<=0?neg(x):[0,val(x)]}
function sqrt(a){const lo=Math.max(0,Math.sqrt(Math.max(0,a[0]))-1e-12),hi=Math.sqrt(a[1])+1e-12;if(lo>0&&sq(point(lo))[1]>a[0]||sq(point(hi))[0]<a[1])throw Error('sqrt enclosure');return [lo,hi]}
function expI(x){
 let t=mul(x,point(1/64));if(val(t)>.125)throw Error('exp reduction');let a=point(1),z=point(1);
 for(let j=1;j<=15;j++){z=div(mul(z,t),point(j));a=plus(a,z)}
 a=plus(a,[-1e-25,1e-25]); // (8/7)*(1/8)^16/16! < 1e-25.
 for(let j=0;j<6;j++)a=sq(a);return a;
}
function logChecked(x,rough){const lo=rough-1e-9,hi=rough+1e-9;if(expI(point(lo))[1]>=x||expI(point(hi))[0]<=x)throw Error('log check');return [lo,hi]}
function gate(x){const fn=t=>mul(mul(sq(t),t),plus(point(10),mul(t,plus(point(-15),mul(point(6),t)))));return [Math.max(0,fn(point(x[0]))[0]),Math.min(1,fn(point(x[1]))[1])]}
function prepare(){
 const d=point(.006),eta=mul(d,point(.05)),q0=div(one,mul(point(2),sqrt(point(2)))),
 T=plus(mul(point(6),d),div(mul(point(6),eta),sub(one,q0))),root12=sqrt(point(12)),
 alpha=[97.64534740775790,97.64534740780158],
 k=div(mul(point(7),eta),root12),la=logChecked(.006,-5.115995809754082),l2=logChecked(2,.6931471805599453),lc=logChecked(.02,-3.912023005428146),
 lw=logChecked(.5,-.6931471805599453),lwt=logChecked(.05,-2.995732273553991),g=sub(neg(la),mul(point(2.75),l2));
 if(sub(lw,lc)[0]<=2||g[0]<=0)throw Error('old cap outside saturated branch');return {eta,T,root12,alpha,k,lc,lw,lwt,g};}
function density(x,c){
 const {eta,T,root12,alpha,k,lc,lw,lwt,g}=c,S=gate(x),S1=sub(one,S),Sd=mul(point(30),mul(sq(x),sq(sub(one,x)))),remaining=sub(point(2),x);
 const raw=plus(lw,plus(mul(k,remaining),mul(g,S1))),rawD=sub(neg(k),mul(g,Sd));
 const logw=plus(lc,mul(S,sub(raw,lc))),logwd=plus(mul(Sd,sub(raw,lc)),mul(S,rawD));
 const w=expI(logw),E=plus(one,sq(w)),dist=sub(T,mul(eta,remaining)),rho=mul(point(.14999999999999997),expI(div(dist,root12)));
 const A=div(absI(mul(w,logwd)),mul(point(6),mul(E,sqrt(E)))),B=div(mul(mul(div(eta,root12),rho),expI(mul(lwt,S1))),E),rad=plus(A,mul(alpha,B));
 return [rad,mul(w,rad)];
}

function compute(b,h,man,N=4096){
 const p=man.parameters;if(p.rCut!==.6||p.rCuff!==.14999999999999997||p.delta0!==.006||p.etaRatioAtN0!==.05||p.a!==2.75||p.curvatureBound!==6||p.slopeCap!==.02||p.pulseCaps[0][1]!==.02||p.warpWeightLevels[0][3]!==.05||p.warpWeightLevels[0][4]!==1||p.capTransition!==2||p.wCut!==.5)throw Error('changed analytic background');
 const c=prepare(),W=q(.00001),U=plus(point(b.planar_perturbation_upper.upper_display),W),V=plus(point(b.height_perturbation_upper.upper_display),W);
 const hCut=[b.cut_height_lower.lower_display,b.cut_height_upper.upper_display],rCut=point(p.rCut);
 const tube=q(.11546),diam=q(3.830),half=q(1.915),rReach=div(tube,q(.06));
 function ceil(x){return x[1]}function floor(x){return x[0]}
 function norm(r,z){return sqrt(plus(sq(r),sq(z)))}
 function allowed(target,r,z){return sub(sqrt(sub(sq(target),sq(r))),z)}
 function witness(r,z,target){return ceil(allowed(target,sub(r,U),sub(z,V)))}
 const d=.04,cutR=sub(rCut,U),cutZ=sub(hCut,V),badD=mul(point(2),norm(cutR,plus(cutZ,q(.08)))),
 cutLimits={deltaForDiameterBudgetUpper:witness(rCut,hCut,half),deltaForReachRatioUpper:witness(rCut,hCut,rReach),diameterAt008Lower:floor(badD),reachRatioAt008Upper:ceil(div(tube,badD))};
 const seg=h.segments.find(row=>row.segment===8),len8=plus(seg.A,mul(c.alpha,seg.B)),rise8=plus(seg.AH,mul(c.alpha,seg.BH));
 let rr=sub(rCut,len8),zz=plus(hCut,rise8),maxNorm=0,maxJ7=0,maxMixed=0,guaranteed=1,rBound=1,zBound=1,criticalCell=0,k=0;
 function charge(r,z){
  maxNorm=Math.max(maxNorm,ceil(norm(r,plus(z,q(d)))));
  maxMixed=Math.max(maxMixed,ceil(norm(plus(q(2.194),r),plus(q(.233+d),z))));
  guaranteed=Math.min(guaranteed,floor(allowed(half,r,z)));
 }
 for(let i=N-1;i>=0;i--){
   const x=[i/N,(i+1)/N],[dr,dz]=density(x,c),rn=sub(rr,mul(dr,point(1/N))),zn=plus(zz,mul(dz,point(1/N)));
   const rup=point(ceil(plus(rr,U))),zup=point(ceil(plus(zn,V)));charge(rup,zup);maxJ7=maxNorm;
   const rc=witness(rn,zn,rReach),zc=witness(rn,zn,half);
   if(rc<rBound){rBound=rc;criticalCell=i}
   zBound=Math.min(zBound,zc);
   rr=rn;zz=zn;
 }
 for(const row of b.cell_zero_segment_boxes){if(row.raw_segment!==7)charge(plus(point(row.planar_radius_upper.upper_display),W),plus(point(row.absolute_height_upper.upper_display),W))}
 const zmax=plus(plus(point(b.cut_height_upper.upper_display),point(b.complete_background_height_upper.upper_display)),V);
 const rin=plus(point(b.cell_zero_segment_boxes.find(row=>row.raw_segment===0).planar_radius_upper.upper_display),W);
 charge(rin,zmax);charge(q(.15),sub(zmax,V));
 const rho=plus(plus(rCut,U),zero),globalMixed=ceil(norm(plus(q(2.194),rho),plus(q(.233+d),zmax)));
 const result={scope:'original complete tail, actual flat disks, unchanged compact arms',cellsJ7:N,fieldComponentEnvelope:1e-5,
  shift:d,maxNorm004:maxNorm,maxNormJ7_004:maxJ7,maxMixedArmTail004:maxMixed,globalSimpleMixed004:globalMixed,
  fullTailShiftSufficient:guaranteed,cutLimits,
  segment7ShapeShiftNecessaryUpper:zBound,segment7ReachShiftNecessaryUpper:rBound,reachWitnessNode:criticalCell};
 if(!(maxNorm<1.912&&globalMixed<3.495&&guaranteed>.0439&&cutLimits.reachRatioAt008Upper<.03))throw Error(JSON.stringify(result));
 return result;
}
if(typeof require==='function'&&require.main===module){
 const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto'),args=process.argv.slice(2);
 function arg(k){const i=args.indexOf(k);if(i<0||!args[i+1])throw Error(k);return args[i+1]}
 function sha(x){return crypto.createHash('sha256').update(x).digest('hex')}
 function read(file,h){const bytes=fs.readFileSync(path.join(arg('--notes'),file));if(sha(bytes)!==h)throw Error(file);return JSON.parse(bytes)}
 const budget=read('2026-11-09-db6f-prefix-m12-segment-ball-budget.json','f08875b25cc46328e0c04171fdbf7f50b802dac6951381e4fb2c64d5839c483c'),
 height=read('2026-11-09-db6f-tail-background-height-rigorous.json','dd64e00bf25124b03e725792e321e961106c6ee643f5526e0b5b95383161ff01'),
 manifest=read('2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json','cc23977e25a09c34db91723dd784cab4b18b89e325fc2ca2fb8dd7ee6866a104');
 const result=compute(budget,height,manifest);
 fs.writeFileSync(arg('--out'),JSON.stringify({sourceSHA256:sha(fs.readFileSync(__filename)),result},null,2)+'\n',{flag:'wx'});
}
