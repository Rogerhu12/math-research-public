"use strict";
function checkR195(band,dense,normal,definition,lambda){
  const began=Date.now(),n=normal.g.length;
  const inputs={H:Array.from(normal.H),g:Array.from(normal.g),diagonal:Array.from(normal.diagonal)};
  const preparedStart=Date.now(),prepared=band.prepareBandBorderNormal(normal,definition),prepareMs=Date.now()-preparedStart;
  const bandStart=Date.now(),a=band.solvePreparedBandBorder(prepared,lambda),bandMs=Date.now()-bandStart;
  const denseStart=Date.now(),b=dense.solveDampedNormal(normal,{lambda}),denseMs=Date.now()-denseStart;
  if(!a.ok||!b.ok)throw Error("Actual same-lambda solve did not succeed");
  const norm=x=>Math.hypot(...x),diff=Array.from(a.direction,(v,i)=>v-b.direction[i]);
  const sd=Array.from(a.scaledDirection,(v,i)=>v-b.scaledDirection[i]);
  let eqMax=0,eqNorm=0,equationDenominator=0;
  for(let i=0;i<n;i++){
    let s=0,c=0;
    for(let j=0;j<n;j++){
      const t=((normal.H[i*n+j]*a.scale[i])*a.scale[j])*a.scaledDirection[j],v=s+t;
      c+=Math.abs(s)>=Math.abs(t)?(s-v)+t:(t-v)+s;s=v;
    }
    const lhs=s+c+lambda*a.scaledDirection[i],rhs=normal.g[i]*a.scale[i],r=lhs+rhs;
    eqMax=Math.max(eqMax,Math.abs(r));eqNorm=Math.hypot(eqNorm,r);equationDenominator=Math.hypot(equationDenominator,lhs,rhs);
  }
  const unchanged=["H","g","diagonal"].every(key=>inputs[key].every((v,i)=>Object.is(v,normal[key][i])));
  const def={schema:"fd2d-R190-C2-direct-position-designed-radius-finite-provider-v1",
    radialBasisCount:1,angularModes:1,dimension:5,stateLayout:{theta:[0,1],phi:[1,2],height:[2,3],cutHeight:3,radius:[4,5]}};
  const toy=(kind)=>{
    const H=new Float64Array(25),g=new Float64Array(5);
    if(kind!=="zero")for(let i=0;i<5;i++)H[i*5+i]=1;
    if(kind==="field"){H[1]=2;H[5]=2;}
    if(kind==="border"){H[3]=2;H[15]=2;}
    return band.solveDampedNormal({H,g,squaredNorm:1},{definition:def,lambda:.01});
  };
  const zero=toy("zero"),badField=toy("field"),badBorder=toy("border");
  const corrupt={...normal,H:Float64Array.from(normal.H)};
  const plan=prepared.layout,oi=plan.permutation[0],oj=plan.permutation[4*plan.blockSize];
  corrupt.H[oi*n+oj]=1e-300;let rejected=false,offBandDetails=null;
  try{band.prepareBandBorderNormal(corrupt,definition);}catch(e){rejected=e.code==="NONZERO_OUTSIDE_RADIAL_BAND";offBandDetails=e.details;}
  const relative=norm(diff)/Math.max(Number.MIN_VALUE,norm(b.direction)),scaledRelative=norm(sd)/Math.max(Number.MIN_VALUE,norm(b.scaledDirection));
  const report={schema:"R195-actual-normal-and-policy-check-v1",runtime:"functions.exec V8",OSProcessCreated:false,OSExitCode:null,
    dimension:n,lambda,squaredNorm:normal.squaredNorm,actualNormalAssembliesInThisCheck:0,
    elapsedMilliseconds:Date.now()-began,prepareMilliseconds:prepareMs,bandSolveMilliseconds:bandMs,densePrepareAndSolveMilliseconds:denseMs,
    directionRelativeL2:relative,directionMaximumAbsolute:Math.max(...diff.map(Math.abs)),
    scaledDirectionRelativeL2:scaledRelative,predictedSquaredNormBand:a.predictedSquaredNorm,predictedSquaredNormDense:b.predictedSquaredNorm,
    predictedSquaredNormDifference:Math.abs(a.predictedSquaredNorm-b.predictedSquaredNorm),slopeDifference:Math.abs(a.slope-b.slope),
    independentOriginalScaledEquationResidualMaximum:eqMax,independentOriginalScaledEquationRelative:eqNorm/Math.max(Number.MIN_VALUE,equationDenominator),
    bandInfo:a.info,denseInfo:b.info,inputArraysBitwiseUnchanged:unchanged,
    zeroColumnCase:{ok:zero.ok,zeroColumnCount:zero.info?.zeroDiagonalColumns.length,directionExactlyZero:zero.ok&&Array.from(zero.direction).every(v=>v===0),scaleExactlyOne:zero.ok&&Array.from(zero.scale).every(v=>v===1)},
    nonSPDField:{ok:badField.ok,phase:badField.phase,pivot:badField.pivot,lambda:badField.lambda,hiddenDiagonalShift:badField.hiddenDiagonalShift},
    nonSPDBorder:{ok:badBorder.ok,phase:badBorder.phase,pivot:badBorder.pivot,lambda:badBorder.lambda,hiddenDiagonalShift:badBorder.hiddenDiagonalShift},
    smallestInjectedOffBand:1e-300,offBandRejected:rejected,offBandDetails,
    wholeJvpCalled:false,actualTrialOrValueCalled:false,providerModified:false,continuousCertificate:false};
  report.passed=relative<1e-10&&scaledRelative<1e-10&&eqMax<1e-12&&unchanged&&rejected&&zero.ok&&report.zeroColumnCase.directionExactlyZero&&report.zeroColumnCase.scaleExactlyOne&&!badField.ok&&!badBorder.ok;
  if(!report.passed)throw Object.assign(Error("R195 check failed"),{report});
  return report;
}
if(typeof module!=="undefined")module.exports={checkR195};
