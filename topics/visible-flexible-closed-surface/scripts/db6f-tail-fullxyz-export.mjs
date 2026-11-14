// Explicit C2 finite-tail maps: exact rotational background + Hermite V.
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
if(!(D>0&&D<=(p.physicalDepth??p.depth)&&S>0&&N>=2*degree+4))throw Error('bad depth/steps/angular degree');
const {createRecalibrationFactory}=await import(pathToFileURL(path.join(here,'closing_weighted_tail.mjs')));
const {subdividePhysical}=await import(pathToFileURL(path.join(here,'950f-tail-subdivision.mjs')));
const {createFastSplitFluxMomentumTailEngine}=await import(source('f6tail_fast_split_flux_engine.mjs'));
const {withCuspAwareRK}=await import(source('f6tail_cusp_grid.mjs'));
const {createRelativeSpatialJetEvaluator}=await import(source('f6tail_relative_spatial_jets.mjs'));
const {relativeSurfaceGeometry}=await import(source('f6tail_relative_development.mjs'));
const physical=createRecalibrationFactory(rec.config??p).assemble(),stages=subdividePhysical(physical,D,p.shootingParts??1);
const keys=['rCut','wCut','width','curvatureBound','delta0','R','a','etaPower','etaRatioAtN0','orientation','prefixR','prefixEnd','prefixReturnStart','protectCell','calibrationSteps','warpSteps','quadratureTolerance','slopeCap','capTransition','capMode','cuspAwareQuadrature','valleyControls','pulseCaps','valleyCaps','warpWeightLevels','rCuff','epsilonScale'];
for(const k of keys)if(JSON.stringify(p[k]??null)!==JSON.stringify(physical.parameters[k]??null))throw Error('physical mismatch '+k);
if(!cp.rawNode||cp.rawNode[D]!==stages.cells.length)throw Error('requires matching staged checkpoint');
const planar=[];for(let m=-degree;m<=degree;m++)if((m-1)%3===0)planar.push(m);
const height=Array.from({length:M+1},(_,j)=>3*j),C=planar.length+height.length,stride=2+3*C;
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
function combine(a,b,L,x){
 const out=new Float64Array(3*C);
 for(let k=0;k<C;k++){
  const z0=a[k],z1=L*a[C+k],z2=.5*L*L*a[2*C+k],d=b[k]-z0;
  const z3=10*d-6*z1-4*L*b[C+k]-3*z2+.5*L*L*b[2*C+k];
  const z4=-15*d+8*z1+7*L*b[C+k]+3*z2-L*L*b[2*C+k];
  const z5=6*d-3*z1-3*L*b[C+k]-z2+.5*L*L*b[2*C+k];
  out[k]=z0+x*(z1+x*(z2+x*(z3+x*(z4+x*z5))));
  out[C+k]=(z1+x*(2*z2+x*(3*z3+x*(4*z4+5*x*z5))))/L;
  out[2*C+k]=(2*z2+x*(6*z3+x*(12*z4+20*x*z5)))/(L*L);
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
const report={status:'finite-C2-explicit-tail-with-sampled-audit',scope:'Exact C2 Hermite perturbation plus one fixed analytic rotational background; shared binary nodes and C3 coefficients. Sampling is not a continuous metric/curvature certificate. Planar rr source uses finite differences; ODE and far nonlinear graph errors remain unpaid.',input:path.resolve(input),inputSHA256:sha(input),sourceSHA256:Object.fromEntries(sourceFiles.map(f=>[f,sha(f)])),parameters:p,physicalStats:physical.stats,settings:{depth:D,steps:S,angularNodes:N,degree,radialDifferenceStep:dh,grid:values.grid,auditAngularNodes:An,auditFractions:fractions},format:{dtype:'little-endian float64',stride,columns:['r','rotational-height-above-cuff-approx',...['value','r-derivative','rr-derivative'].flatMap(j=>[...planar.map(m=>j+':planar-exp-i'+m+'theta'),...height.map(m=>j+':height-cos-'+m+'theta')])],planarModes:planar,heightModes:height,coefficientCount:C,interpretation:'Gamma-r exp(i theta)=sum real a_m exp(i m theta); z-h=sum c_m cos(m theta). Each block is interpolated by quintic Hermite in physical r using the shared first/second radial jets. Duplicate raw-cell interface rows are byte-identical.'},gauge:'At deepest represented port the nonlinear mean-height perturbation is zero; mean is accumulated outward without resets. Exact fixed h_rot has cuff value zero; stored h_rot values are numerical primitive evaluations, used only for positions, not metric derivatives.',files:[],totals:{metric:0,fullTensor:0,curvature:0,minArea:Infinity,sourceMetric:0,sourceFullD:0,maxSeamValue:0,maxSeamFirst:0,maxSeamSecond:0,minRadialGap:Infinity,maximumWholeCellV2Norm:0},rawCells:[]};
let mean=0,bg=physical.cells.slice(D).reduce((v,c)=>v+c.heightSpan,0),last=null,deepest=null,rawBuffer=[],currentRaw=D-1,currentSummary=null,totalNodes=0;
function flushRaw(){
 if(!rawBuffer.length)return;
 const data=new Float64Array(rawBuffer.length*stride);for(let j=0;j<rawBuffer.length;j++)data.set(rawBuffer[j],j*stride);
 const bytes=gzipSync(Buffer.from(data.buffer),{level:9}),name=outPrefix+'-raw'+String(currentRaw).padStart(3,'0')+'.f64.gz';
 if(bytes.length>=5000000)throw Error('packet exceeds 5 MB');if(fs.existsSync(name))throw Error('refusing overwrite '+name);
 fs.writeFileSync(name,bytes);report.files.push({rawCell:currentRaw,path:path.resolve(name),rows:rawBuffer.length,columns:stride,bytes:bytes.length,sha256:sha(name),minR:rawBuffer[0][0],maxR:rawBuffer.at(-1)[0]});
 report.rawCells.push(currentSummary);fs.writeFileSync(outPrefix+'-manifest.json',JSON.stringify(report,null,2)+'\n');
 console.log(JSON.stringify({rawCell:currentRaw,rows:rawBuffer.length,metric:currentSummary.metric,fullTensor:currentSummary.fullTensor,curvature:currentSummary.curvature,wholeCellV2Norm:currentSummary.wholeCellV2Norm,bytes:bytes.length}));rawBuffer=[];
}
for(let n=stages.cells.length-1;n>=0;n--){
 const cell=stages.cells[n],profile=cell.profiles[0];
 if(cell.rawCell!==currentRaw){flushRaw();currentRaw=cell.rawCell;rawBuffer.push(last);currentSummary=null;}
 if(!currentSummary)currentSummary={n:currentRaw,metric:0,fullTensor:0,curvature:0,wholeCellV2Norm:0};
 let engine=createFastSplitFluxMomentumTailEngine({modes:M,spacing:p.spacing,quadrature:N,mu:cell.mu,orientation:p.orientation,projectionFloor:p.projectionFloor});engine=withCuspAwareRK(engine);
 const evaluator=createRelativeSpatialJetEvaluator(engine,{spacing:p.spacing,radialDifferenceStep:dh});
 let state=new Float64Array(K+2);state.set(cp.states[n+1]);state[K]=mean;state[K+1]=bg;
 let xs;
 if(values.grid==='uniform')xs=[...new Set([0,1,...Array.from({length:S-1},(_,k)=>(k+1)/S),...(profile.integrationBreakpoints??[])])].sort((a,b)=>a-b);
 else if(values.grid==='chebyshev'){const breaks=[0,...(profile.integrationBreakpoints??[]),1].sort((a,b)=>a-b);xs=[0];for(let k=0;k<breaks.length-1;k++){const l=breaks[k],r=breaks[k+1],ns=Math.max(4,Math.ceil(S*(r-l)));for(let j=1;j<=ns;j++)xs.push(l+(r-l)*(1-Math.cos(Math.PI*j/ns))/2);}}
 else throw Error('unknown grid '+values.grid);
 let priorX=null;
 for(let k=0;k<xs.length;k++){
  const x=xs[k];
  if(k)state=engine.rk4(state,profile,xs[k-1],x-xs[k-1]);
  if(k===xs.length-1){const target=cp.states[n];for(let j=0;j<K;j++)state[j]=target[j]*(j<M?1:cell.portRatio);}
  const a=evaluator.evaluate(state,profile,x),coef=packed(a,state),row=new Float64Array(stride);row[0]=a.g.r;row[1]=state[K+1];row.set(coef,2);
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
   const L=row[0]-last[0];if(!(L>0))throw Error('non-positive representable radial interval');report.totals.minRadialGap=Math.min(report.totals.minRadialGap,L);
   for(const f of fractions){
    const xx=priorX+f*(x-priorX),g=engine.geometry(profile,xx),s=(g.r-last[0])/L,c=combine(last.subarray(2),coef,L,s);
    for(let q=0;q<An;q++){
     const v=vectors(c,q),z=relativeSurfaceGeometry(g,2*Math.PI*q/An,v[1],v[2],v[3],v[4],v[5]);
     currentSummary.metric=Math.max(currentSummary.metric,z.metric);currentSummary.fullTensor=Math.max(currentSummary.fullTensor,z.fullTensorFrobeniusBound);currentSummary.curvature=Math.max(currentSummary.curvature,z.actualCurvature);
     report.totals.metric=Math.max(report.totals.metric,z.metric);report.totals.fullTensor=Math.max(report.totals.fullTensor,z.fullTensorFrobeniusBound);report.totals.curvature=Math.max(report.totals.curvature,z.actualCurvature);report.totals.minArea=Math.min(report.totals.minArea,z.areaNormalized);
    }
   }
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
