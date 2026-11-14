// Nonlinear finite-M finite-depth tail DN wrapper. Not an infinite-tail certificate.
// Author: Astra / nonlinear_tail, 2026-11-08. Original engines are unchanged.
import {createPhysicalTailShooting} from '../notes/general-exact-tail-physical-shooting-v1.mjs';
import {createRawTailEngine} from './general_exact_tail_cauchy_raw.mjs';
import fs from 'node:fs/promises';
function solve(A,b,n){A=Float64Array.from(A);b=Float64Array.from(b);for(let k=0;k<n;k++){let p=k;for(let i=k+1;i<n;i++)if(Math.abs(A[i*n+k])>Math.abs(A[p*n+k]))p=i;if(Math.abs(A[p*n+k])<1e-280)throw Error('singular graph');for(let j=k;j<n;j++)[A[k*n+j],A[p*n+j]]=[A[p*n+j],A[k*n+j]];[b[k],b[p]]=[b[p],b[k]];for(let i=k+1;i<n;i++){const q=A[i*n+k]/A[k*n+k];for(let j=k;j<n;j++)A[i*n+j]-=q*A[k*n+j];b[i]-=q*b[k];}}const x=new Float64Array(n);for(let i=n-1;i>=0;i--){let v=b[i];for(let j=i+1;j<n;j++)v-=A[i*n+j]*x[j];x[i]=v/A[i*n+i];}return x;}
function mul(A,B,n){const C=new Float64Array(n*n);for(let i=0;i<n;i++)for(let j=0;j<n;j++)for(let k=0;k<n;k++)C[i*n+j]+=A[i*n+k]*B[k*n+j];return C;}
function inv(A,n){const B=new Float64Array(n*n);for(let k=0;k<n;k++){const e=new Float64Array(n);e[k]=1;const v=solve(A,e,n);for(let i=0;i<n;i++)B[i*n+k]=v[i];}return B;}
function graphJacobian(tail,z,target){
 const M=target.length,K=2*M,states=z.states.map(s=>Float64Array.from(s));
 const scales=new Float64Array(states.length);scales[0]=Math.max(1e-250,...target.map(Math.abs));for(let n=0;n<scales.length-1;n++)scales[n+1]=scales[n]/Math.abs(tail.gains[n][0]);
 const ev=tail.evaluate(states,target,true,scales);let G=new Float64Array(M*M);for(let j=0;j<M;j++)G[j*M+j]=tail.graphs[states.length-1][j];
 for(let n=states.length-2;n>=0;n--){const J=ev.flows[n].J,A=new Float64Array(M*M),B=new Float64Array(M*M),C=new Float64Array(M*M),D=new Float64Array(M*M);for(let i=0;i<M;i++)for(let j=0;j<M;j++){A[i*M+j]=J[i*K+j];B[i*M+j]=J[i*K+M+j];C[i*M+j]=J[(M+i)*K+j];D[i*M+j]=J[(M+i)*K+M+j];}const BG=mul(B,G,M),DG=mul(D,G,M);for(let k=0;k<M*M;k++){A[k]+=BG[k];C[k]+=DG[k];}G=mul(C,inv(A,M),M);}
 return G;
}
export function makeDN(parameters={}){
 const tail=createPhysicalTailShooting(parameters),M=tail.parameters.modes,K=2*M,ratio=2**tail.parameters.a;
 const rawEngine=createRawTailEngine({modes:M,quadrature:tail.parameters.quadrature});
 const engine=tail.cells[0].engine,profile=tail.cells[0].profiles.at(-1),g=engine.geometry(profile,1);
 function cutJets(node){const state=new Float64Array(K+2);state.set(node);for(let j=0;j<M;j++)state[M+j]*=ratio;const raw=engine.toRaw(state,profile,1);const old=new Float64Array(K+2);old.set(raw.raw);old[K]=raw.meanPhysical;const f=rawEngine.rhs(old,profile,1,true),dr=g.drdx;
  const height=new Float64Array(M),slope=new Float64Array(M),second=new Float64Array(M);
  for(let j=0;j<M;j++){const m2=4*(j+1)**2; height[j]=g.r**4*node[j];slope[j]=g.r**3*(m2*raw.raw[j]+Math.sqrt(12)*raw.raw[M+j]);second[j]=3*slope[j]/g.r+g.r**3*(m2*f.derivative[j]+Math.sqrt(12)*f.derivative[M+j])/dr;}
  return {radius:g.r,backgroundSlope:g.w,backgroundSecond:g.w*g.dlogwdx/dr,E:g.E,Ep:2*g.w2*g.dlogwdx/dr,height:Array.from(height),slope:Array.from(slope),second:Array.from(second),meanSlope:g.w+raw.meanPhysical,meanSecond:(g.w*g.dlogwdx+f.derivative[K])/dr,meanSlopeCorrection:raw.meanPhysical,meanSecondCorrection:f.derivative[K]/dr,minLeading:f.minA,minD:f.minD,endpointFullD:f.maxDarboux,endpointPhi:f.physicalHolonomyResidual,formalCurvature:f.formalHeightCurvature};
 }
 function audit(z,steps=tail.parameters.steps){let maxD=0,minA=Infinity,minD=Infinity,maxK=0,maxPV=0,maxPhi=0,maxNormalized=0;
  for(let n=0;n<tail.cells.length;n++){const c=tail.cells[n],s=new Float64Array(K+2);s.set(z.states[n+1]);let state=s;for(const p of c.profiles){for(let k=0;k<=steps;k++){const x=k/steps,e=c.engine.rhs(state,p,x,true),geom=c.engine.geometry(p,x);maxD=Math.max(maxD,e.legacy.maxDarboux);maxPhi=Math.max(maxPhi,Math.abs(e.legacy.physicalHolonomyResidual));minA=Math.min(minA,e.minA);minD=Math.min(minD,e.minD);maxK=Math.max(maxK,e.legacy.formalHeightCurvature);maxPV=Math.max(maxPV,e.legacy.peakValley);for(const a of e.legacy.perAngle)maxNormalized=Math.max(maxNormalized,Math.abs(a.darboux*geom.E**2*geom.r*geom.drdx/geom.w2));if(k<steps)state=c.engine.rk4(state,p,x,1/steps);}}}
  return {fullD:maxD,normalizedFullDefect:maxNormalized,minLeading:minA,minD,formalCurvature:maxK,maxPhysicalPV:maxPV,fullMeanPhiResidual:maxPhi};
 }
 return {tail,cutJets,solve(target,options={}){const z=tail.solve(Float64Array.from(target),options),jets=cutJets(z.states[0]);const out={...z,jets};if(options.jacobian){const G=graphJacobian(tail,z,Float64Array.from(target)),J=new Float64Array((3*M+2)*M),base=Float64Array.from(z.states[0]),scale=Math.max(...target.map(Math.abs),1e-250);for(let k=0;k<M;k++){const h=1e-5*Math.max(Math.abs(target[k]),scale*.01),plus=Float64Array.from(base),minus=Float64Array.from(base);plus[k]+=h;minus[k]-=h;for(let i=0;i<M;i++){plus[M+i]+=h*G[i*M+k];minus[M+i]-=h*G[i*M+k];}const p=cutJets(plus),q=cutJets(minus),pv=[...p.slope,...p.second,p.meanSlopeCorrection,p.meanSecondCorrection,...p.height],qv=[...q.slope,...q.second,q.meanSlopeCorrection,q.meanSecondCorrection,...q.height];for(let i=0;i<pv.length;i++)J[i*M+k]=(pv[i]-qv[i])/(2*h*g.r**4);}out.graphJacobian=Array.from(G);out.heightJetJacobian=Array.from(J);out.heightJetJacobianRows=['slope[m]','second[m]','meanSlope','meanSecond','height[m]'];}if(options.audit)out.audit=audit(z);return out;}};
}
if(process.argv[1]?.endsWith('tailnext_dn_response.mjs')){
 const args=process.argv.slice(2),i=args.indexOf('--input'),o=args.indexOf('--out');if(i<0||o<0)throw Error('--input CONFIG.json --out REPORT.json required');const config=JSON.parse(await fs.readFile(args[i+1],'utf8'));
 const rows=[];for(const entry of config.runs){const t=Date.now();try{const dn=makeDN(entry.parameters),r=dn.solve(entry.target,entry.options??{maxIterations:14,tolerance:1e-10,audit:true});rows.push({label:entry.label,...r,seconds:(Date.now()-t)/1000});console.log(JSON.stringify({label:entry.label,converged:r.converged,residual:r.normalizedResidual,jet:r.jets,audit:r.audit,seconds:(Date.now()-t)/1000}));}catch(e){const row={label:entry.label,parameters:entry.parameters,target:entry.target,failed:String(e),seconds:(Date.now()-t)/1000};rows.push(row);console.log(JSON.stringify(row));}await fs.writeFile(args[o+1],JSON.stringify({scope:'Finite-M and finite-depth physical nonlinear DN; no true infinite tail or positive completed example.',runs:rows},null,2)+'\n');}
}
