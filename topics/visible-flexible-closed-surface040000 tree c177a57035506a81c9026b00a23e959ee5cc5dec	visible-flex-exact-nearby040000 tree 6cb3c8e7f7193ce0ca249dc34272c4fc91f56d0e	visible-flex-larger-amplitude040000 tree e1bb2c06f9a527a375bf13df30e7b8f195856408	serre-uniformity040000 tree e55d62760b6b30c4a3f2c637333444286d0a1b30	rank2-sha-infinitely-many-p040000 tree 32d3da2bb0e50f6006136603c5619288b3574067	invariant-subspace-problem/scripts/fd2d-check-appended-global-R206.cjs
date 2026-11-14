function runR206ActualCheck(req,raw,source){
 const m={exports:{}};new Function("module","exports",source)(m,m.exports);
 const spl=req("fd2d-cubic-spline-refinement-R196.cjs").createR196CubicSplines();
 const input={options:{radialBasisCount:3,radialKnots:spl.uniformKnots(3),modes:2,angles:32,gap:.05,radiusCoefficientBound:.4},guide:{guide:9.5,weight:.01,nodeShare:.5},geometryGuide:{radius:1.59,width:.84,held:.65,weight:10,nodeShare:.5,cutWindow:[.4,.8]}};
 const p=req("fd2d-run-geometry-guided-position-R203.cjs").createR203RunProvider(raw,input);
 const z=Array.from({length:p.provider.dimension},(_,i)=>.00005*Math.sin((i+1)*.73));
 const start=Date.now(),normal=p.provider.normal(z),n=normal.g.length,N=n+1;
 function append(v){
  const H=new Float64Array(N*N),g=new Float64Array(N);
  for(let i=0;i<n;i++){g[i]=normal.g[i];for(let j=0;j<n;j++)H[i*N+j]=normal.H[i*n+j];}
  for(let i=0;i<n;i++){let h=0;for(let j=0;j<n;j++)h+=normal.H[i*n+j]*v[j];H[i*N+n]=H[n*N+i]=h;}
  let d=0,ga=0;for(let i=0;i<n;i++){d+=v[i]*H[i*N+n];ga+=v[i]*normal.g[i];}
  H[n*N+n]=d;g[n]=ga;
  return {H,g,diagonal:Float64Array.from({length:N},(_,i)=>H[i*N+i]),squaredNorm:normal.squaredNorm};
 }
 function denseSolve(nn,lambda){
  const scale=Float64Array.from({length:N},(_,i)=>nn.H[i*N+i]>0?1/Math.sqrt(nn.H[i*N+i]):1);
  const L=new Float64Array(N*N),b=Float64Array.from(nn.g,(x,i)=>-x*scale[i]);
  for(let i=0;i<N;i++)for(let j=0;j<=i;j++){
   let h=(nn.H[i*N+j]*scale[i])*scale[j]+(i===j?lambda:0);
   for(let k=0;k<j;k++)h-=L[i*N+k]*L[j*N+k];
   if(i===j){if(!(h>0))throw Error("Independent dense SPD");L[i*N+j]=Math.sqrt(h);}else L[i*N+j]=h/L[j*N+j];
  }
  const y=new Float64Array(N),x=new Float64Array(N);
  for(let i=0;i<N;i++){let v=b[i];for(let j=0;j<i;j++)v-=L[i*N+j]*y[j];y[i]=v/L[i*N+i];}
  for(let i=N-1;i>=0;i--){let v=y[i];for(let j=i+1;j<N;j++)v-=L[j*N+i]*x[j];x[i]=v/L[i*N+i];}
  return Array.from(x,(v,i)=>v*scale[i]);
 }
 const kernel=m.exports.createR206AppendedGlobalKernel(req("fd2d_scaled_band_border_lm_R203.cjs"));
 const definition={schema:"fd2d-R206-appended-global-parameter-provider-v1",baseProvider:p.provider.definition,dimension:N,globalIndex:n,globalName:"actual test column Jv (not yet tail-amplitude column)"};
 const cases=[];
 for(const name of ["duplicate_cut","all_original_columns"]){
  const v=Array.from({length:n},(_,i)=>name==="duplicate_cut"?(i===p.core.definition.stateLayout.cutHeight?1:0):.1*Math.sin((i+1)*.31));
  const nn=append(v),pp=kernel.prepareBandBorderNormal(nn,definition,{halfBandwidthBlocks:4});
  for(const lambda of [1e-2,1e-3,1e-5]){
   const s=kernel.solvePreparedBandBorder(pp,lambda);if(!s.ok)throw Error(JSON.stringify(s));
   const dense=denseSolve(nn,lambda);let e=0,d=0;for(let i=0;i<N;i++){e+=(s.direction[i]-dense[i])**2;d+=dense[i]**2;}
   const item={name,lambda,relativeDirection:Math.sqrt(e/d),relativeOriginalScaledResidual:s.info.originalScaledEquationRelativeResidual,schur:s.info.globalSchur,auxRHSRounding:s.info.auxiliaryScaledRHSRoundingMaximum};cases.push(item);
   if(item.relativeDirection>1e-7||item.relativeOriginalScaledResidual>1e-10)throw Error("R206 actual normal check failed "+JSON.stringify(item));
  }
 }
 return {schema:"R206-actual-complete-position-normal-linear-algebra-check-v1",runtime:"actual pure V8; no OS process or exit",baseDimension:n,fullDimension:N,baseSquaredNorm:normal.squaredNorm,actualBaseDefinition:p.provider.definition,actualState:z,appendedColumn:"Jv from complete actual finite metric/curvature/R203 geometry normal; not a tail-amplitude derivative",cases,elapsedSeconds:(Date.now()-start)/1000,sourceChars:source.length,actualTailAmplitudeNormalCompleted:false,actualNonlinearStepCompleted:false};
}
if(typeof module!=="undefined"&&module.exports)module.exports={runR206ActualCheck};

if(typeof require!=="undefined"&&typeof module!=="undefined"&&require.main===module){
 const fs=require("node:fs"),path=require("node:path"),[candidatePath,outputPath]=process.argv.slice(2);
 if(!candidatePath||!outputPath||fs.existsSync(outputPath))throw Error("candidate.json and fresh report.json required");
 const report=runR206ActualCheck(name=>require("./"+name),JSON.parse(fs.readFileSync(candidatePath)),
  fs.readFileSync(path.join(__dirname,"fd2d_appended_global_schur_R206.cjs"),"utf8"));
 report.runtime="Node actual process; actual exit belongs to external process receipt";
 fs.mkdirSync(path.dirname(outputPath),{recursive:true});fs.writeFileSync(outputPath,JSON.stringify(report,null,2)+"\n");
 console.log(JSON.stringify({output:outputPath,cases:report.cases,elapsedSeconds:report.elapsedSeconds}));
}
