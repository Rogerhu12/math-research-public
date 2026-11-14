// Source-critical refinement of db6f-tail-increment-export.mjs.
// Explicit C2 finite-tail maps: exact background + integrated quartic Fr.
// Values after the first node are defined by exact integrals of the derivative interpolant.
// Packed finite Fourier coefficients are binary-real definitions, not an ODE certificate.
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {gunzipSync,gzipSync} from 'node:zlib';
import {createHash} from 'node:crypto';
import {parseArgs} from 'node:util';
const {values,positionals}=parseArgs({allowPositionals:true,options:{
 'source-root':{type:'string'},'depth':{type:'string',default:'8'},
 'steps':{type:'string',default:'16'},'angular-nodes':{type:'string',default:'256'},
 'grid':{type:'string',default:'uniform'},'degree':{type:'string',default:'96'},'difference-step':{type:'string',default:'0.00005'},
 'flow-steps':{type:'string'},
 'critical-ratio':{type:'string',default:'0.1'},'critical-cells':{type:'string',default:'0'},'critical-base-steps':{type:'string'},
 'plan-only':{type:'boolean',default:false},
 'audit-angular-nodes':{type:'string',default:'128'},'audit-fractions':{type:'string',default:'0.25,0.5,0.75'}
}});
if(positionals.length!==2||!values['source-root'])throw Error('checkpoint output-prefix --source-root ROOT required');
const [input,outPrefix]=positionals;
if(fs.existsSync(outPrefix+'-manifest.json'))throw Error('Refusing to overwrite an earlier manifest');
const sourceRoot=path.resolve(values['source-root']),here=path.dirname(fileURLToPath(import.meta.url)),srcDir=path.join(sourceRoot,'topics/large-amplitude-twist-flex/scripts');
process.env.VISIBLE_FLEX_SOURCE_ROOT=sourceRoot;process.env.CLOSING_TAIL_CACHE=srcDir;
const source=name=>pathToFileURL(path.join(srcDir,name));
const sha=f=>createHash('sha256').update(fs.readFileSync(f)).digest('hex');
const read=f=>JSON.parse((f.endsWith('.gz')?gunzipSync(fs.readFileSync(f)):fs.readFileSync(f)).toString());
const rec=read(input),response=rec.response??rec,cp=response.checkpoint??response.tail_checkpoint??response.seam?.tail_checkpoint??response;
if(!cp.parameters||!cp.states)throw Error('missing checkpoint');
const p=cp.parameters,M=p.modes,K=2*M,D=+values.depth,S=+values.steps,N=+values['angular-nodes'],degree=+values.degree,An=+values['audit-angular-nodes'],dh=+values['difference-step'],fractions=values['audit-fractions'].split(',').map(Number);
const flowSteps=+(values['flow-steps']??p.steps),criticalRatio=+values['critical-ratio'];
const criticalBaseSteps=+(values['critical-base-steps']??S);
const criticalCells=new Set(values['critical-cells'].split(',').filter(Boolean).map(Number));
if(![D,S,N,degree,An,flowSteps,criticalBaseSteps].every(v=>Number.isInteger(v)&&v>0))throw Error('integer positive discretizations required');
if(!(criticalRatio>0&&criticalRatio<=1)||![...criticalCells].every(n=>Number.isInteger(n)&&n>=0))throw Error('bad critical-grid parameters');
if(!(D>0&&D<=(p.physicalDepth??p.depth)&&S>0&&N>=2*degree+4))throw Error('bad depth/steps/angular degree');
const {createRecalibrationFactory}=await import(pathToFileURL(path.join(here,'closing_weighted_tail.mjs')));
const {subdividePhysical}=await import(pathToFileURL(path.join(here,'950f-tail-subdivision.mjs')));
const {createFastSplitFluxMomentumTailEngine}=await import(source('f6tail_fast_split_flux_engine.mjs'));
const {withCuspAwareRK}=await import(source('f6tail_cusp_grid.mjs'));
const {createRelativeSpatialJetEvaluator}=await import(source('f6tail_relative_spatial_jets.mjs'));
const {relativeSurfaceGeometry}=await import(source('f6tail_relative_development.mjs'));
const factory=createRecalibrationFactory(rec.config??p),physical=factory.assemble(),stages=subdividePhysical(physical,D,p.shootingParts??1);
const keys=['rCut','wCut','width','curvatureBound','delta0','R','a','etaPower','etaRatioAtN0','orientation','prefixR','prefixEnd','prefixReturnStart','protectCell','calibrationSteps','warpSteps','quadratureTolerance','slopeCap','capTransition','capMode','cuspAwareQuadrature','valleyControls','pulseCaps','valleyCaps','warpWeightLevels','rCuff','epsilonScale'];
for(const k of keys)if(JSON.stringify(p[k]??null)!==JSON.stringify(physical.parameters[k]??null))throw Error('physical mismatch '+k);
if(!cp.rawNode||cp.rawNode[D]!==stages.cells.length)throw Error('requires matching staged checkpoint');
const planar=[];for(let m=-degree;m<=degree;m++)if((m-1)%3===0)planar.push(m);
const height=Array.from({length:M+1},(_,j)=>3*j),C=planar.length+height.length,stride=3+4*C;
function criticalLayers(profile){
 const breaks=(profile.integrationBreakpoints??[]).filter(x=>x>0&&x<1).sort((a,b)=>a-b);
 const wx=x=>{const g=profile(x);return Math.exp(g.logw)*g.dlogwdx;};
 return breaks.map((x,k)=>{
  const h=Math.min(1e-5,(x-(breaks[k-1]??0))/8,((breaks[k+1]??1)-x)/8);
  if(!(h>1e-12))return null;
  const g=profile(x),w=Math.exp(g.logw),d2=(wx(x+h)-wx(x-h))/(2*h);
  if(!(Math.abs(d2)>1e-12))return null;
  const scale=physical.parameters.curvatureBound*(1+w*w)**1.5*Math.abs(g.drdx)/Math.abs(d2);
  if(!(scale>1e-12&&scale<1))return null;
  return {x,r:g.r,widthScale:scale,radialSpeed:g.drdx,sourceWxDerivative:d2,differenceStep:h};
 }).filter(Boolean);
}
function makeGrid(profile,rawCell){
 const localSteps=values.grid==='critical'&&criticalCells.has(rawCell)?criticalBaseSteps:S;
 const uniform=[0,1,...Array.from({length:localSteps-1},(_,k)=>(k+1)/localSteps),...(profile.integrationBreakpoints??[])];
 const layers=values.grid==='critical'&&criticalCells.has(rawCell)?criticalLayers(profile):[];
 if(values.grid==='critical'){
  for(const layer of layers)for(const direction of [-1,1])for(let k=1;k<10000;k++){
   const x=layer.x+direction*layer.widthScale*Math.expm1(k*criticalRatio);
   if(!(x>0&&x<1))break;
   uniform.push(x);
   if(k===9999)throw Error('critical grid did not reach the stage boundary');
  }
 }
 if(values.grid==='uniform'||values.grid==='critical')return {xs:[...new Set(uniform)].sort((a,b)=>a-b),layers};
 if(values.grid==='chebyshev'){const breaks=[0,...(profile.integrationBreakpoints??[]),1].sort((a,b)=>a-b),xs=[0];for(let k=0;k<breaks.length-1;k++){const l=breaks[k],r=breaks[k+1],ns=Math.max(4,Math.ceil(S*(r-l)));for(let j=1;j<=ns;j++)xs.push(l+(r-l)*(1-Math.cos(Math.PI*j/ns))/2);}return {xs,layers};}
 throw Error('unknown grid '+values.grid);
}
const plans=stages.cells.map(cell=>{
 const {xs,layers}=makeGrid(cell.profiles[0],cell.rawCell),entry=factory.getEntries(cell.rawCell,physical.parameters.valleyControls[cell.rawCell]??0).entries[cell.rawSegment];
 const integral=(a,b)=>{if(a===b)return 0;const v=entry.integrate(cell.rawLeft+(cell.rawRight-cell.rawLeft)*a,cell.rawLeft+(cell.rawRight-cell.rawLeft)*b);return v[0]+physical.stats.alpha*v[1];};
 const lengths=xs.slice(1).map((x,k)=>integral(xs[k],x));if(lengths.some(x=>!(x>0)))throw Error('non-positive independent radial increment');return {xs,integral,lengths,layers};
});
const gridPlan=plans.map((v,n)=>({stage:n,rawCell:stages.cells[n].rawCell,rawSegment:stages.cells[n].rawSegment,nodes:v.xs.length,layers:v.layers}));
console.log(JSON.stringify({grid:values.grid,criticalRatio,criticalBaseSteps,criticalCells:[...criticalCells],stages:gridPlan.length,nodes:plans.reduce((a,v)=>a+v.xs.length-1,1),criticalStages:gridPlan.filter(v=>v.layers.length)}));
if(values['plan-only']){
 fs.writeFileSync(outPrefix+'-grid-plan.json',JSON.stringify({status:'numerical-grid-proposal-only',input:path.resolve(input),inputSHA256:sha(input),scriptSHA256:sha(fileURLToPath(import.meta.url)),physicalStats:physical.stats,settings:{depth:D,steps:S,grid:values.grid,criticalRatio,criticalBaseSteps,criticalCells:[...criticalCells]},gridPlan},null,2)+'\n');
 process.exit(0);
}
const view=new DataView(new ArrayBuffer(8));
function dyadic(x){view.setFloat64(0,x);const bits=view.getBigUint64(0),sgn=bits>>63n?-1n:1n,eb=Number((bits>>52n)&2047n),mant=bits&((1n<<52n)-1n);return {n:sgn*(eb?mant+(1n<<52n):mant),e:eb?eb-1023-52:-1074};}
const innerR=stages.cells.at(-1).profiles[0](0).r,outerR=stages.cells[0].profiles[0](1).r,innerQ=dyadic(innerR),outerQ=dyadic(outerR),allDyadic=plans.flatMap(v=>v.lengths.map(dyadic));
const emin=Math.min(innerQ.e,outerQ.e,...allDyadic.map(v=>v.e)),num=q=>q.n<<BigInt(q.e-emin);
let sumNum=0n;for(const q of allDyadic)sumNum+=num(q);
const innerNum=num(innerQ),deltaNum=num(outerQ)-innerNum,scale=Number(deltaNum)/Number(sumNum);
let accumulated=0n;
for(let n=plans.length-1;n>=0;n--){const v=plans[n];v.r=[Number(innerNum*sumNum+deltaNum*accumulated)/Number(sumNum)*2**emin];for(const L of v.lengths){accumulated+=num(dyadic(L));v.r.push(Number(innerNum*sumNum+deltaNum*accumulated)/Number(sumNum)*2**emin);}}
if(accumulated!==sumNum)throw Error('exact radial sum mismatch');
const trig=(count,modes)=>modes.map(m=>({c:Float64Array.from({length:count},(_,j)=>Math.cos(2*Math.PI*j*m/count)),s:Float64Array.from({length:count},(_,j)=>Math.sin(2*Math.PI*j*m/count))}));
const basis=trig(N,planar),auditBasisP=trig(An,planar),auditBasisH=trig(An,height),baseC=Float64Array.from({length:An},(_,j)=>Math.cos(2*Math.PI*j/An)),baseS=Float64Array.from({length:An},(_,j)=>Math.sin(2*Math.PI*j/An));
function packed(a,state){
 const out=new Float64Array(3*C),{g,root,field,heightJets:j}=a,sigma=g.drdx/g.r;
 for(let derivative=0;derivative<3;derivative++){
  const name=['V','Vr','Vrr'][derivative];
  for(let k=0;k<planar.length;k++){
   let sum=0;for(let q=0;q<N;q++)sum+=a.perAngle[q][name][0]*basis[k].c[q]+a.perAngle[q][name][1]*basis[k].s[q];
   out[derivative*C+k]=sum/N;
  }
 }
 out[planar.length]=state[K];
 out[C+planar.length]=g.w*root.L[0];
 out[2*C+planar.length]=g.w*(j.Ldot[0]+g.dlogwdx*root.L[0])/g.drdx;
 for(let k=0;k<M;k++){
  const m=height[k+1],idx=planar.length+k+1;
  out[idx]=g.r**4*state[k];
  out[C+idx]=m*m*g.r**3*state[k]+Math.sqrt(2)*g.w*root.L[k+1];
  out[2*C+idx]=(m*m*g.r**3*(field[k]+3*sigma*state[k])+Math.sqrt(2)*g.w*(j.Ldot[k+1]+g.dlogwdx*root.L[k+1]))/g.drdx;
 }
 return out;
}
function firstPacked(q,state){
 const out=new Float64Array(C),{g,rt,development:d}=q;
 for(let k=0;k<planar.length;k++){let sum=0;for(let j=0;j<N;j++)sum+=d.dxR[j]*basis[k].c[j]+d.dyR[j]*basis[k].s[j];out[k]=sum/N;}
 out[planar.length]=g.w*rt.L[0];
 for(let k=0;k<M;k++){const m=height[k+1];out[planar.length+k+1]=m*m*g.r**3*state[k]+Math.sqrt(2)*g.w*rt.L[k+1];}
 return out;
}
function combine(a,b,mid,L,x){
 const out=new Float64Array(3*C);
 for(let k=0;k<C;k++){
  const u0=a[C+k],u1=b[C+k],v0=L*a[2*C+k],v1=L*b[2*C+k];
  const bubble=16*mid[k]-8*(u0+u1)-2*(v0-v1);
  const z0=u0,z1=v0,z2=-3*u0+3*u1-2*v0-v1+bubble,z3=2*u0-2*u1+v0+v1-2*bubble,z4=bubble;
  out[k]=a[k]+L*x*(z0+x*(z1/2+x*(z2/3+x*(z3/4+x*z4/5))));
  out[C+k]=z0+x*(z1+x*(z2+x*(z3+x*z4)));
  out[2*C+k]=(z1+x*(2*z2+x*(3*z3+4*x*z4)))/L;
 }
 return out;
}
function vectors(c,q){
 const ans=Array.from({length:6},()=>[0,0,0]);
 for(let k=0;k<planar.length;k++){
  const m=planar[k],co=auditBasisP[k].c[q],si=auditBasisP[k].s[q],v=c[k],r=c[C+k],rr=c[2*C+k];
  ans[0][0]+=v*co;ans[0][1]+=v*si;ans[1][0]+=r*co;ans[1][1]+=r*si;ans[2][0]-=m*v*si;ans[2][1]+=m*v*co;
  ans[3][0]+=rr*co;ans[3][1]+=rr*si;ans[4][0]-=m*r*si;ans[4][1]+=m*r*co;ans[5][0]-=m*m*v*co;ans[5][1]-=m*m*v*si;
 }
 for(let k=0;k<height.length;k++){
  const m=height[k],co=auditBasisH[k].c[q],si=auditBasisH[k].s[q],idx=planar.length+k,v=c[idx],r=c[C+idx],rr=c[2*C+idx];
  ans[0][2]+=v*co;ans[1][2]+=r*co;ans[2][2]-=m*v*si;ans[3][2]+=rr*co;ans[4][2]-=m*r*si;ans[5][2]-=m*m*v*co;
 }
 return ans;
}
function endpointPacket(row){
 const coeff=[];
 for(let j=0;j<3;j++){
  const a=Array.from({length:degree+1},(_,m)=>({frequency:m,cos:[0,0,0],sin:[0,0,0]}));
  for(let k=0;k<planar.length;k++){const m=planar[k],v=row[2+j*C+k];a[Math.abs(m)].cos[0]+=v;a[Math.abs(m)].sin[1]+=Math.sign(m)*v;}
  for(let k=0;k<height.length;k++)a[height[k]].cos[2]=row[2+j*C+planar.length+k];
  coeff.push(a);
 }
 return {rawNode:D,r:row[0],cuff:physical.parameters.rCuff,coefficients:coeff};
}
const sourceFiles=[fileURLToPath(import.meta.url),...['closing_weighted_tail.mjs','closing_recalibrated_tail.mjs','950f-tail-subdivision.mjs'].map(f=>path.join(here,f)),...['f6tail_relative_spatial_jets.mjs','f6tail_relative_development.mjs','f6tail_fast_split_flux_engine.mjs','f6tail_momentum_physical_jets.mjs'].map(f=>path.join(srcDir,f))];
const report={status:'finite-C2-integrated-explicit-tail-with-sampled-audit',scope:'Exact C2 integrated-quartic derivative perturbation plus one fixed analytic rotational background; shared binary nodes, endpoint derivative jets, physical-midpoint first derivatives and C3 coefficients. Sampling is not a continuous metric/curvature certificate. Planar rr source uses finite differences; ODE and far nonlinear graph errors remain unpaid.',input:path.resolve(input),inputSHA256:sha(input),sourceSHA256:Object.fromEntries(sourceFiles.map(f=>[f,sha(f)])),parameters:p,physicalStats:physical.stats,settings:{depth:D,steps:S,angularNodes:N,degree,radialDifferenceStep:dh,grid:values.grid,auditAngularNodes:An,auditFractions:fractions},format:{dtype:'little-endian float64',stride,columns:['r','rotational-height-above-cuff-approx',...['derived-value-approx','r-derivative','rr-derivative','previous-span-mid-r-derivative'].flatMap(j=>[...planar.map(m=>j+':planar-exp-i'+m+'theta'),...height.map(m=>j+':height-cos-'+m+'theta')])],planarModes:planar,heightModes:height,coefficientCount:C,interpretation:'Gamma-r exp(i theta)=sum real a_m exp(i m theta); z-h=sum c_m cos(m theta). Fr is the cubic Hermite interpolant of endpoint Fr,Frr plus the quartic bubble t^2(1-t)^2 matching its physical-midpoint value. F is the exact integral from the first endpoint; stored node positions are numerical evaluations only. Thus the model is piecewise quintic and exactly C2, without differentiating quantized point values. Duplicate raw-cell interface rows are byte-identical.'},gauge:'At deepest represented port the nonlinear mean-height perturbation is zero; mean is accumulated outward without resets. Exact fixed h_rot has cuff value zero; stored h_rot values are numerical primitive evaluations, used only for positions, not metric derivatives.',files:[],totals:{metric:0,fullTensor:0,curvature:0,minArea:Infinity,sourceMetric:0,sourceFullD:0,maxSeamValue:0,maxSeamFirst:0,maxSeamSecond:0,minRadialGap:Infinity,maximumWholeCellV2Norm:0,maxIntegratedPositionDeviation:0},rawCells:[]};
report.settings.stageHermiteCorrection=true;
report.settings.criticalRatio=criticalRatio;report.settings.criticalBaseSteps=criticalBaseSteps;report.settings.criticalCells=[...criticalCells];report.gridPlan=gridPlan;report.worstSamples={};
report.scope+=' Source-critical grid layers use finite-difference width proposals only to choose interpolation nodes. They do not certify the source ODE, and source CP/native flow steps remain separately recorded.';
report.settings.maximumFlowStep=1/flowSteps;
report.status='finite-C2-increment-integrated-explicit-tail-with-sampled-audit';
report.radialGeometry={innerAnchor:innerR,outerAnchor:outerR,unscaledSum:{numerator:sumNum.toString(),binaryExponent:emin},normalization:{numerator:deltaNum.toString(),denominator:sumNum.toString()},scaleApprox:scale,spanCount:allDyadic.length,definition:'Each saved final column is an exact binary positive increment ell_i, evaluated by a local radial integral without subtracting absolute radii. beta=(outerAnchor-innerAnchor)/sum_i ell_i is an exact rational. Actual node r_i=innerAnchor+beta*sum_{j<i}ell_j, and each Hermite span has exact length beta*ell_i. Displayed r columns are approximate only. Both radial end anchors are therefore exact. The target rotational metric is unchanged.'};
report.format.columns.push('previous-span-radial-integral-unscaled');
report.format.interpretation+=' Radii and span lengths use radialGeometry, not differences of the displayed cumulative r columns.';
report.scope+=' Sampled target jets are evaluated at the source profile radius; maxSourceRadiusDisplayDifference records the numerical shift to the exact-sum representation. No continuous certification is inferred from these samples.';
report.scope+=' Each stage endpoint shooting defect is distributed through one physical-r cubic Hermite correction to Fr; its exact derivative corrects Frr. This is part of the finite map definition, not an exact ODE correction.';
Object.assign(report.totals,{stageFirstEndpointDefect:0,stageSecondEndpointDefect:0,stageMaxFirstCorrection:0,stageMaxSecondCorrection:0});
report.totals.maxSourceRadiusDisplayDifference=0;
report.stageDefects=[];
let mean=0,bg=physical.cells.slice(D).reduce((v,c)=>v+c.heightSpan,0),last=null,deepest=null,rawBuffer=[],currentRaw=D-1,currentSummary=null,totalNodes=0;
function flushRaw(){
 if(!rawBuffer.length)return;
 let totalBytes=0,part=0;
 for(let start=0;start<rawBuffer.length-1;start+=999){
  const rows=rawBuffer.slice(start,Math.min(rawBuffer.length,start+1000)),data=new Float64Array(rows.length*stride);for(let j=0;j<rows.length;j++)data.set(rows[j],j*stride);
  const bytes=gzipSync(Buffer.from(data.buffer),{level:9}),name=outPrefix+'-raw'+String(currentRaw).padStart(3,'0')+'-part'+String(part).padStart(2,'0')+'.f64.gz';
  if(bytes.length>=5000000)throw Error('packet exceeds 5 MB');if(fs.existsSync(name))throw Error('refusing overwrite '+name);
  fs.writeFileSync(name,bytes);report.files.push({rawCell:currentRaw,part,path:path.resolve(name),rows:rows.length,columns:stride,bytes:bytes.length,sha256:sha(name),minR:rows[0][0],maxR:rows.at(-1)[0]});totalBytes+=bytes.length;part++;
 }
 report.rawCells.push(currentSummary);fs.writeFileSync(outPrefix+'-manifest.json',JSON.stringify(report,null,2)+'\n');
 console.log(JSON.stringify({rawCell:currentRaw,rows:rawBuffer.length,metric:currentSummary.metric,fullTensor:currentSummary.fullTensor,curvature:currentSummary.curvature,wholeCellV2Norm:currentSummary.wholeCellV2Norm,parts:part,totalBytes}));rawBuffer=[];
}
for(let n=stages.cells.length-1;n>=0;n--){
 const cell=stages.cells[n],profile=cell.profiles[0];
 if(cell.rawCell!==currentRaw){flushRaw();currentRaw=cell.rawCell;rawBuffer.push(last);currentSummary=null;}
 if(!currentSummary)currentSummary={n:currentRaw,metric:0,fullTensor:0,curvature:0,wholeCellV2Norm:0};
 let engine=createFastSplitFluxMomentumTailEngine({modes:M,spacing:p.spacing,quadrature:N,mu:cell.mu,orientation:p.orientation,projectionFloor:p.projectionFloor});engine=withCuspAwareRK(engine);
 const evaluator=createRelativeSpatialJetEvaluator(engine,{spacing:p.spacing,radialDifferenceStep:dh});
 function flow(state,xa,xb){const count=Math.max(1,Math.ceil((xb-xa)*flowSteps));let ans=Float64Array.from(state);for(let l=0;l<count;l++)ans=engine.rk4(ans,profile,xa+(xb-xa)*l/count,(xb-xa)/count);return ans;}
 let state=new Float64Array(K+2);state.set(cp.states[n+1]);state[K]=mean;state[K+1]=bg;
 const plan=plans[n],xs=plan.xs;
 const states=[Float64Array.from(state)];for(let k=1;k<xs.length;k++)states.push(flow(states.at(-1),xs[k-1],xs[k]));
 const sourceStart=packed(evaluator.evaluate(states[0],profile,0),states[0]),sourceEnd=packed(evaluator.evaluate(states.at(-1),profile,1),states.at(-1));
 const canonicalEnd=Float64Array.from(states.at(-1)),target=cp.states[n];for(let j=0;j<K;j++)canonicalEnd[j]=target[j]*(j<M?1:cell.portRatio);
 const canonicalEndCo=packed(evaluator.evaluate(canonicalEnd,profile,1),canonicalEnd),r0=plan.r[0],r1=plan.r.at(-1),stageL=scale*plan.lengths.reduce((a,b)=>a+b,0);
 const du0=new Float64Array(C),dv0=new Float64Array(C),du1=new Float64Array(C),dv1=new Float64Array(C);
 let dFirst=0,dSecond=0;
 for(let j=0;j<C;j++){
  du0[j]=last?last[2+C+j]-sourceStart[C+j]:0;dv0[j]=last?last[2+2*C+j]-sourceStart[2*C+j]:0;
  du1[j]=canonicalEndCo[C+j]-sourceEnd[C+j];dv1[j]=canonicalEndCo[2*C+j]-sourceEnd[2*C+j];
  dFirst=Math.max(dFirst,Math.abs(du0[j]),Math.abs(du1[j]));dSecond=Math.max(dSecond,Math.abs(dv0[j]),Math.abs(dv1[j]));
 }
 report.totals.stageFirstEndpointDefect=Math.max(report.totals.stageFirstEndpointDefect,dFirst);report.totals.stageSecondEndpointDefect=Math.max(report.totals.stageSecondEndpointDefect,dSecond);
 report.stageDefects.push({stage:n,rawCell:cell.rawCell,width:stageL,firstDefect:dFirst,secondDefect:dSecond});
 function correction(r){
  const t=(r-r0)/stageL,t2=t*t,t3=t2*t,c1=new Float64Array(C),c2=new Float64Array(C);
  for(let j=0;j<C;j++){
   c1[j]=(2*t3-3*t2+1)*du0[j]+stageL*(t3-2*t2+t)*dv0[j]+(-2*t3+3*t2)*du1[j]+stageL*(t3-t2)*dv1[j];
   c2[j]=(6*t2-6*t)*(du0[j]-du1[j])/stageL+(3*t2-4*t+1)*dv0[j]+(3*t2-2*t)*dv1[j];
   report.totals.stageMaxFirstCorrection=Math.max(report.totals.stageMaxFirstCorrection,Math.abs(c1[j]));report.totals.stageMaxSecondCorrection=Math.max(report.totals.stageMaxSecondCorrection,Math.abs(c2[j]));
  }
  return [c1,c2];
 }
 let priorX=null;
 for(let k=0;k<xs.length;k++){
  const x=xs[k];
  const leftState=k?states[k-1]:null;state=states[k];
  const a=evaluator.evaluate(state,profile,x),coef=packed(a,state),row=new Float64Array(stride);row[0]=plan.r[k];row[1]=state[K+1];row[stride-1]=k?plan.lengths[k-1]:0;row.set(coef,2);
  report.totals.maxSourceRadiusDisplayDifference=Math.max(report.totals.maxSourceRadiusDisplayDifference,Math.abs(row[0]-a.g.r));
  const [c1,c2]=correction(row[0]);for(let j=0;j<C;j++){coef[C+j]+=c1[j];coef[2*C+j]+=c2[j];}row.set(coef,2);
  if(k===xs.length-1)for(let j=0;j<C;j++){coef[C+j]=canonicalEndCo[C+j];coef[2*C+j]=canonicalEndCo[2*C+j];row[2+C+j]=coef[C+j];row[2+2*C+j]=coef[2*C+j];}
  report.totals.sourceMetric=Math.max(report.totals.sourceMetric,a.development.actualMetricRelativeOperatorError);report.totals.sourceFullD=Math.max(report.totals.sourceFullD,a.heightJets.maxDarboux);
  let v2=0;for(let j=0;j<3;j++){
   let z=0;for(let l=0;l<planar.length;l++)z+=2*(1+Math.abs(planar[l]))**2*Math.abs(coef[j*C+l]);for(let l=0;l<height.length;l++)z+=(1+height[l])**2*Math.abs(coef[j*C+planar.length+l]);v2=Math.max(v2,z);
  }
  currentSummary.wholeCellV2Norm=Math.max(currentSummary.wholeCellV2Norm,v2);report.totals.maximumWholeCellV2Norm=Math.max(report.totals.maximumWholeCellV2Norm,v2);
  if(k===0&&last){
   if(Math.abs(row[0]-last[0])>8*Number.EPSILON*Math.max(1,Math.abs(row[0])))throw Error('physical seam radius mismatch');
   for(let j=0;j<3;j++)for(let l=0;l<C;l++)report.totals[['maxSeamValue','maxSeamFirst','maxSeamSecond'][j]]=Math.max(report.totals[['maxSeamValue','maxSeamFirst','maxSeamSecond'][j]],Math.abs(row[2+j*C+l]-last[2+j*C+l]));
   priorX=x;continue;
  }
  if(last){
   const localLength=plan.lengths[k-1],L=scale*localLength;if(!(L>0))throw Error('non-positive representable radial interval');report.totals.minRadialGap=Math.min(report.totals.minRadialGap,L);
   const targetR=last[0]+L/2;let xlo=priorX,xhi=x;for(let j=0;j<44;j++){const xm=(xlo+xhi)/2;if(plan.integral(priorX,xm)<localLength/2)xlo=xm;else xhi=xm;}const xm=(xlo+xhi)/2;
   const midState=flow(leftState,priorX,xm),mid=firstPacked(evaluator.point(midState,profile,xm),midState),cmid=correction(targetR)[0];for(let j=0;j<C;j++)mid[j]+=cmid[j];row.set(mid,2+3*C);
   for(const f of fractions){
    const xx=priorX+f*(x-priorX),g=engine.geometry(profile,xx),s=plan.integral(priorX,xx)/localLength,c=combine(last.subarray(2),coef,mid,L,s);
    report.totals.maxSourceRadiusDisplayDifference=Math.max(report.totals.maxSourceRadiusDisplayDifference,Math.abs(last[0]+s*L-g.r));
    for(let q=0;q<An;q++){
     const v=vectors(c,q),z=relativeSurfaceGeometry(g,2*Math.PI*q/An,v[1],v[2],v[3],v[4],v[5]);
     for(const [key,value] of [['metric',z.metric],['fullTensor',z.fullTensorFrobeniusBound],['curvature',z.actualCurvature]])if(value>report.totals[key])report.worstSamples[key]={value,stage:n,rawCell:cell.rawCell,rawSegment:cell.rawSegment,x:xx,sourceR:g.r,displayR:last[0]+s*L,theta:2*Math.PI*q/An,span:[priorX,x]};
     currentSummary.metric=Math.max(currentSummary.metric,z.metric);currentSummary.fullTensor=Math.max(currentSummary.fullTensor,z.fullTensorFrobeniusBound);currentSummary.curvature=Math.max(currentSummary.curvature,z.actualCurvature);
     report.totals.metric=Math.max(report.totals.metric,z.metric);report.totals.fullTensor=Math.max(report.totals.fullTensor,z.fullTensorFrobeniusBound);report.totals.curvature=Math.max(report.totals.curvature,z.actualCurvature);report.totals.minArea=Math.min(report.totals.minArea,z.areaNormalized);
    }
   }
   const integrated=combine(last.subarray(2),coef,mid,L,1);let discrepancy=0;for(let j=0;j<C;j++){discrepancy=Math.max(discrepancy,Math.abs(integrated[j]-coef[j]));row[2+j]=integrated[j];}report.totals.maxIntegratedPositionDeviation=Math.max(report.totals.maxIntegratedPositionDeviation,discrepancy);
  }
  if(!deepest)deepest=row;last=row;rawBuffer.push(row);totalNodes++;priorX=x;
 }
 mean=state[K];bg=state[K+1];
}
flushRaw();report.totalUniqueNodes=totalNodes;report.cutMeanHeightCorrection=mean;report.cutBackgroundHeightApprox=bg;report.deepBackgroundHeightApprox=deepest[1];report.finished=true;
fs.writeFileSync(outPrefix+'-manifest.json',JSON.stringify(report,null,2)+'\n');
const packet={status:'explicit-Hermite-endpoint-source-packet',scope:report.scope,input:report.input,inputSHA256:report.inputSHA256,sourceSHA256:report.sourceSHA256,parameters:p,settings:{angularNodes:N,radialDifferenceStep:dh,assumedBackgroundCurvature:6.001,symmetry:'c3'},gauge:report.gauge,rows:[endpointPacket(deepest)]};
fs.writeFileSync(outPrefix+'-collar.json',JSON.stringify(packet)+'\n');
console.log(JSON.stringify({finished:true,nodes:totalNodes,...report.totals}));
