// Probe only: same finite momentum equations on an independently known cone.
import fs from 'node:fs';import {pathToFileURL} from 'node:url';import {createHash} from 'node:crypto';
const [moduleFile,inputFile,outFile,stepsArg="64",modesArg="8,16,32"]=process.argv.slice(2);
const {createMomentumTailEngine}=await import(pathToFileURL(moduleFile));
const input=JSON.parse(fs.readFileSync(inputFile)),rows=[];
const norm=x=>Math.max(...Array.from(x,Math.abs)),hash=f=>createHash('sha256').update(fs.readFileSync(f)).digest('hex');
for(const row of input.rows)for(const M of modesArg.split(",").map(Number)){
 const {w,radius:r,H,meanSlope}=row,freq=Array.from({length:M},(_,j)=>2*(j+1));
 const engine=createMomentumTailEngine({modes:M,quadrature:512,spacing:2,projectionFloor:.01,mu:1,orientation:1});
 const profile=x=>({r:r+x,drdx:1,logw:Math.log(w),dlogwdx:0});
 const raw=new Float64Array(2*M);for(let j=0;j<M;j++){raw[j]=H[j]/r**4;raw[M+j]=(1-freq[j]**2)*raw[j]/Math.sqrt(12);}
 let result={amplitude:row.amplitude,M};
 try{
  const init=engine.initializeFromRaw(raw,profile),state=init.state,root=engine.root(state,profile,0,init.L);
  const expectedL=new Float64Array(M+1);expectedL[0]=meanSlope/w-1;
  for(let j=0;j<M;j++)expectedL[j+1]=(1-freq[j]**2)*H[j]/(Math.SQRT2*r*w);
  const f=engine.rhs(state,profile,0,false,root),expected=new Float64Array(f.length);
  for(let j=0;j<M;j++){expected[j]=-3*state[j]/r;expected[M+j]=4*state[M+j]/r;}
  expected[2*M]=w*init.L[0];expected[2*M+1]=w;
  engine.seedRootGuess(init.L);const jac=engine.rhsWithJacobian(state,profile,0).jacobian;
  const direction=Float64Array.from(state.slice(0,2*M),(v,j)=>Math.sin(j+1)*Math.max(Math.abs(v),1e-12));
  const Jv=Float64Array.from(f,(_,i)=>direction.reduce((v,x,j)=>v+jac[i*2*M+j]*x,0));
  const fd=[];
  for(const step of [1e-4,1e-5,1e-6]){
   const plus=Float64Array.from(state,(v,j)=>v+(direction[j]??0)*step),minus=Float64Array.from(state,(v,j)=>v-(direction[j]??0)*step);
   engine.seedRootGuess(init.L);const fp=engine.rhs(plus,profile,0);engine.seedRootGuess(init.L);const fm=engine.rhs(minus,profile,0);
   const error=norm(Float64Array.from(Jv,(v,j)=>v-(fp[j]-fm[j])/(2*step)))/Math.max(1e-20,norm(Jv));fd.push({step,relativeError:error});
  }
  // A fixed radial flow on the same exact cone; no amplitude continuation claim.
  let flowing=Float64Array.from(state);engine.seedRootGuess(init.L);const steps=Number(stepsArg),span=.02;
  for(let j=0;j<steps;j++)flowing=engine.rk4(flowing,profile,j*span/steps,span/steps);
  let qerr=0,pierr=0;const r1=r+span;
  for(let j=0;j<M;j++){qerr=Math.max(qerr,Math.abs(flowing[j]-state[j]*(r/r1)**3));pierr=Math.max(pierr,Math.abs(flowing[M+j]-state[M+j]*(r1/r)**4));}
  result={...result,success:true,minA:root.e.minA,minD:root.e.minD,minS:root.e.minS,rootRelativeResidual:root.err/root.scale,meanRootResidual:init.normalizedMeanResidual,LReferenceError:norm(Float64Array.from(init.L,(v,j)=>v-expectedL[j])),rhsReferenceError:norm(Float64Array.from(f,(v,j)=>v-expected[j])),finiteDifference:fd,flowSteps:steps,flowSpan:span,flowQError:qerr,flowMomentumError:pierr,flowMeanError:Math.abs(flowing[2*M]+flowing[2*M+1]-span*meanSlope),Gram:Array.from(root.e.B),solveDiagnostics:engine.solveDiagnostics};
 }catch(error){result={...result,success:false,error:String(error),solveDiagnostics:engine.solveDiagnostics};}
 rows.push(result);fs.writeFileSync(outFile,JSON.stringify({scope:'Experimental finite full-Gram chart, exact cone reference only. D/S and original residual thresholds retained; no closing tail or infinite-M existence.',module_sha256:hash(moduleFile),input_sha256:hash(inputFile),source_sha256:hash(process.argv[1]),rows},null,2)+'\n');
 console.log(JSON.stringify(Object.fromEntries(Object.entries(result).filter(([k])=>k!=='Gram'))));
}
