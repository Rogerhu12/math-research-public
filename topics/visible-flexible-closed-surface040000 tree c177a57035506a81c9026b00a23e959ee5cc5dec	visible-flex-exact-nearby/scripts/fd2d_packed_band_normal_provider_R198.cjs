"use strict";
/* Independent R198 engineering source. Complete frozen position/J formulas
 * below are retained; only symmetric H storage, add and merge are replaced.
 * The caller explicitly declares a radial half-bandwidth. No tiny entry
 * outside it is silently omitted. Core fields and finite objective stay fixed.
 */
function requireTrue(c,m){if(!c)throw Error(m);}
function finiteNumber(x,m){requireTrue(typeof x==="number"&&Number.isFinite(x),m+" must be finite");return x;}
function positionBandLayout(definition,width){
  const d=definition.metricProvider||definition,J=d.radialBasisCount,K=d.angularModes,a=d.stateLayout;
  requireTrue(Number.isInteger(width)&&width>=0,"Explicit integer halfBandwidthBlocks required");
  requireTrue(Number.isInteger(J)&&J>0&&Number.isInteger(K)&&K>0&&a,"Explicit positive J,K and actual stateLayout required");
  const designed=Array.isArray(a.radius),cut=2*J*K+J,b=2*K+1+(designed?1:0),m=J*b,n=m+1;
  const eq=(v,l,r)=>Array.isArray(v)&&v.length===2&&v[0]===l&&v[1]===r;
  requireTrue(d.dimension===n&&definition.dimension===n&&eq(a.theta,0,J*K)&&eq(a.phi,J*K,2*J*K)&&eq(a.height,2*J*K,cut)&&a.cutHeight===cut,"Incompatible complete state layout");
  if(designed)requireTrue(eq(a.radius,cut+1,n),"Incorrect actual radius layout");
  const permutation=new Int32Array(n),inverse=new Int32Array(n);let i=0;
  for(let j=0;j<J;j++){for(let k=0;k<K;k++)permutation[i++]=j*K+k;for(let k=0;k<K;k++)permutation[i++]=J*K+j*K+k;permutation[i++]=2*J*K+j;if(designed)permutation[i++]=cut+1+j;}
  permutation[i]=cut;for(let p=0;p<n;p++)inverse[permutation[p]]=p;
  const binding=JSON.stringify({J,K,n,m,b,width,stateLayout:a});
  return {schema:"R198-explicit-position-band-layout-v1",n,fieldCount:m,J,K,blockSize:b,halfBandwidthBlocks:width,stride:(width+1)*b,
    cutHeightOriginalIndex:cut,permutation,inverse,designed,providerSchema:definition.schema,binding};
}
function uniformPositionLayout(J,K,width){
  const cut=2*J*K+J,n=cut+1+J;
  return positionBandLayout({dimension:n,radialBasisCount:J,angularModes:K,stateLayout:{theta:[0,J*K],phi:[J*K,2*J*K],height:[2*J*K,cut],cutHeight:cut,radius:[cut+1,n]}},width);
}
function createSymmetricBandAccumulator(layout){
  const {n,fieldCount:m,blockSize:b,stride,halfBandwidthBlocks:w,inverse}=layout;
  const packet={schema:"R198-symmetric-unscaled-band-border-v1",dimension:n,layoutBinding:layout.binding,
    radialBasisCount:layout.J,angularModes:layout.K,designed:layout.designed,halfBandwidthBlocks:w,
    lower:new Float64Array(m*stride),border:new Float64Array(m),borderDiagonal:0,
    diagnostics:{pairContributions:0,zeroOutsideBandContributions:0,maximumNonzeroRadialBlockDistance:0,denseMatrixAllocated:false}};
  function add(originalI,originalJ,value){
    requireTrue(Number.isInteger(originalI)&&originalI>=0&&originalI<n&&Number.isInteger(originalJ)&&originalJ>=0&&originalJ<n,"Actual H pair indices invalid");
    finiteNumber(value,"Actual H pair contribution");
    let i=inverse[originalI],j=inverse[originalJ];if(j>i){const t=i;i=j;j=t;}
    packet.diagnostics.pairContributions++;
    if(i===m){if(j===m)packet.borderDiagonal+=value;else packet.border[j]+=value;return;}
    const distance=Math.floor(i/b)-Math.floor(j/b);
    if(distance>w){
      if(value!==0){const e=Error("Nonzero actual row contribution outside declared packed radial band");e.code="NONZERO_OUTSIDE_RADIAL_BAND";e.details={originalI,originalJ,radialDistance:distance,halfBandwidthBlocks:w,value};throw e;}
      packet.diagnostics.zeroOutsideBandContributions++;return;
    }
    if(value!==0)packet.diagnostics.maximumNonzeroRadialBlockDistance=Math.max(packet.diagnostics.maximumNonzeroRadialBlockDistance,distance);
    packet.lower[i*stride+i-j]+=value;
  }
  return {add,packet:()=>packet,diagonal:()=>bandDiagonal(packet,layout)};
}
function assertPacket(packet,layout){
  requireTrue(packet&&packet.schema==="R198-symmetric-unscaled-band-border-v1"&&packet.dimension===layout.n&&packet.layoutBinding===layout.binding,"Packed normal layout binding mismatch");
  requireTrue(packet.lower.length===layout.fieldCount*layout.stride&&packet.border.length===layout.fieldCount,"Packed normal storage length mismatch");
}
function bandDiagonal(packet,layout){
  assertPacket(packet,layout);const d=new Float64Array(layout.n);
  for(let i=0;i<layout.fieldCount;i++)d[layout.permutation[i]]=packet.lower[i*layout.stride];
  d[layout.cutHeightOriginalIndex]=packet.borderDiagonal;return d;
}
function mergeBandPacketsInPlace(a,b){
  requireTrue(a.schema==="R198-symmetric-unscaled-band-border-v1"&&b.schema===a.schema&&a.layoutBinding===b.layoutBinding&&a.lower.length===b.lower.length&&a.border.length===b.border.length,"Cannot merge unlike actual normal layouts");
  for(let i=0;i<a.lower.length;i++)a.lower[i]+=b.lower[i];
  for(let i=0;i<a.border.length;i++)a.border[i]+=b.border[i];
  a.borderDiagonal+=b.borderDiagonal;
  a.diagnostics={pairContributions:a.diagnostics.pairContributions+b.diagnostics.pairContributions,
    zeroOutsideBandContributions:a.diagnostics.zeroOutsideBandContributions+b.diagnostics.zeroOutsideBandContributions,
    maximumNonzeroRadialBlockDistance:Math.max(a.diagnostics.maximumNonzeroRadialBlockDistance,b.diagnostics.maximumNonzeroRadialBlockDistance),
    denseMatrixAllocated:false};
  return a;
}
function packetForNormal(normal,definition,options={}){
  requireTrue(normal&&normal.bandNormal&&!normal.H,"Explicit packed normal required; ambiguous dense+packed inputs rejected");
  const packet=normal.bandNormal,w=options.halfBandwidthBlocks===undefined?packet.halfBandwidthBlocks:Number(options.halfBandwidthBlocks);
  const layout=positionBandLayout(definition,w);assertPacket(packet,layout);
  return {packet,layout};
}
function preparePackedBandBorderNormal(normal,definition,options={}){
  const {packet,layout}=packetForNormal(normal,definition,options),{n,fieldCount:m,blockSize:b,stride,halfBandwidthBlocks:w,permutation}=layout;
  const squaredNorm=finiteNumber(Number(normal.squaredNorm),"squaredNorm");requireTrue(squaredNorm>=0,"Negative squaredNorm");
  requireTrue(normal.g&&normal.g.length===n,"Gradient dimension mismatch");
  const gradient=Float64Array.from(normal.g,v=>finiteNumber(Number(v),"g"));
  const diagonal=bandDiagonal(packet,layout),scale=new Float64Array(n),zeros=[];
  const given=normal.diagonal;requireTrue(given==null||given.length===n,"Given diagonal dimension");
  let suppliedDiagonalDifference=0,suppliedDiagonalRelativeDifference=0;
  for(let i=0;i<n;i++){
    finiteNumber(diagonal[i],"H diagonal");requireTrue(diagonal[i]>=0,"Negative J^T J diagonal");
    scale[i]=diagonal[i]>0?1/Math.sqrt(diagonal[i]):1;finiteNumber(scale[i],"Exact scale");
    if(diagonal[i]===0)zeros.push(i);
    if(given){finiteNumber(Number(given[i]),"Given diagonal");const e=Math.abs(given[i]-diagonal[i]);suppliedDiagonalDifference=Math.max(suppliedDiagonalDifference,e);suppliedDiagonalRelativeDifference=Math.max(suppliedDiagonalRelativeDifference,e/Math.max(Number.MIN_VALUE,Math.abs(given[i]),diagonal[i]));}
  }
  const band=new Float64Array(m*stride),originalLower=new Float64Array(m*stride),originalUpper=new Float64Array(m*stride);
  const border=new Float64Array(m),originalFieldToBorder=new Float64Array(m),originalBorderToField=new Float64Array(m);
  let scalingOrderSymmetryAdjustment=0,storedLowerNonzeros=0;
  for(let i=0;i<m;i++){
    const si=scale[permutation[i]];
    for(let off=0;off<stride;off++){
      const at=i*stride+off,h=finiteNumber(Number(packet.lower[at]),"Packed H entry"),j=i-off;
      if(j<0||Math.floor(i/b)-Math.floor(j/b)>w){requireTrue(h===0,"Nonzero packed padding/out-of-band slot");continue;}
      const sj=scale[permutation[j]],low=(h*si)*sj,up=(h*sj)*si;
      finiteNumber(low,"Scaled H");finiteNumber(up,"Scaled H transpose");
      originalLower[at]=low;originalUpper[at]=up;band[at]=i===j?low:.5*low+.5*up;
      scalingOrderSymmetryAdjustment=Math.max(scalingOrderSymmetryAdjustment,Math.abs(low-up));
      if(h!==0)storedLowerNonzeros++;
    }
    const h=finiteNumber(Number(packet.border[i]),"Packed border"),sc=scale[layout.cutHeightOriginalIndex];
    const low=(h*sc)*si,up=(h*si)*sc;finiteNumber(low,"Scaled border");finiteNumber(up,"Scaled border transpose");
    originalBorderToField[i]=low;originalFieldToBorder[i]=up;border[i]=.5*low+.5*up;
    scalingOrderSymmetryAdjustment=Math.max(scalingOrderSymmetryAdjustment,Math.abs(low-up));if(h!==0)storedLowerNonzeros++;
  }
  const cb=finiteNumber(Number(packet.borderDiagonal),"Packed border diagonal"),sc=scale[layout.cutHeightOriginalIndex];
  const borderDiagonal=(cb*sc)*sc;finiteNumber(borderDiagonal,"Scaled border diagonal");if(cb!==0)storedLowerNonzeros++;
  const scaledGradient=new Float64Array(n);let scaledGradientInfinity=0;
  for(let i=0;i<n;i++){scaledGradient[i]=gradient[permutation[i]]*scale[permutation[i]];finiteNumber(scaledGradient[i],"Scaled g");scaledGradientInfinity=Math.max(scaledGradientInfinity,Math.abs(scaledGradient[i]));}
  return {schema:"R195-prepared-scaled-band-border-v1",layout,gradient,squaredNorm,diagonal,scale,scaledGradient,
    band,originalLower,originalUpper,border,originalFieldToBorder,originalBorderToField,borderDiagonal,originalBorderDiagonal:borderDiagonal,
    info:{dimension:n,radialBlocks:layout.J,blockSize:b,halfBandwidthBlocks:w,scalarStorageStride:stride,oneGlobalBorderOriginalIndex:layout.cutHeightOriginalIndex,
      offBandNonzeroCount:0,offBandMaximum:0,offBandTolerance:0,storedLowerNonzeros,
      zeroDiagonalColumns:zeros,zeroDiagonalScale:1,exactPositiveDiagonalScale:"1/sqrt(Hjj)",suppliedDiagonalDifference,suppliedDiagonalRelativeDifference,
      suppliedDiagonalUsedInsteadOfHjj:false,symmetryAdjustment:0,scaledSymmetryAdjustment:0,scalingOrderSymmetryAdjustment,scaledGradientInfinity,
      preparedNumericStorageBytes:band.byteLength+originalLower.byteLength+originalUpper.byteLength+border.byteLength+originalFieldToBorder.byteLength+originalBorderToField.byteLength+
        gradient.byteLength+diagonal.byteLength+scale.byteLength+scaledGradient.byteLength+permutation.byteLength+layout.inverse.byteLength,
      rawPackedNumericStorageBytes:packet.lower.byteLength+packet.border.byteLength+8,rawDenseMatrixAllocated:false,fullScaledMatrixAllocated:false,
      originalPairAdditionOrderPreserved:true,rawBandDiagnostics:{...packet.diagnostics},inputArraysModified:false,continuousCertificate:false}};
}
function createPackedBandNormalBackend(kernel,options={}){
  requireTrue(kernel&&typeof kernel.solvePreparedBandBorder==="function","Frozen variable-width R195 solver required");
  const configured=options.halfBandwidthBlocks;
  return {prepareBandBorderNormal:(normal,definition,more={})=>normal.bandNormal?
      preparePackedBandBorderNormal(normal,definition,{...options,...more}):
      kernel.prepareBandBorderNormal(normal,definition,{...options,...more}),
    solvePreparedBandBorder:kernel.solvePreparedBandBorder,
    implementationDefinition:{schema:"R198-packed-normal-preparation-backend-v1",explicitHalfBandwidthBlocks:configured??null,
      directionKernelParentSHA256:"3484c99bfe0a5602c16eb5ccd70288326be04eeadc2804df4c7fd16639ece02c",
      finiteObjectiveOrDomainChanged:false,rawDenseMatrixAllocated:false}};
}
function expandBandNormalForCheck(normal,definition){
  const {packet,layout}=packetForNormal(normal,definition),{n,fieldCount:m,blockSize:b,stride,halfBandwidthBlocks:w,permutation}=layout;
  const H=new Float64Array(n*n),cut=layout.cutHeightOriginalIndex;
  for(let i=0;i<m;i++){
    const ii=permutation[i],lo=Math.max(0,(Math.floor(i/b)-w)*b);
    for(let j=lo;j<=i;j++){const jj=permutation[j],h=packet.lower[i*stride+i-j];H[ii*n+jj]=h;H[jj*n+ii]=h;}
    H[ii*n+cut]=packet.border[i];H[cut*n+ii]=packet.border[i];
  }
  H[cut*n+cut]=packet.borderDiagonal;
  return {...normal,bandNormal:undefined,H,diagonal:bandDiagonal(packet,layout)};
}

/* Actual C2 two-angle direct-position metric-design objective after R190.
 * Variable B32 radius and exact symmetric boundary lift. Complete angular
 * trigonometric functions are integrated by explicitly stated quadrature.
 */
"use strict";
function createR190BandProvider(engine,bundle,options={}){
  const J=options.radialBasisCount||12,K=options.modes||7;
  const N=options.angles||64;
  if(N%4||N<16)throw Error("Angular count must be a multiple of four");
  const nq=N/4,A=Math.PI/2,du=A/nq;
  const base=engine.candidate(bundle),c=base.centralLength,S=base.end;
  const step=(S-c)/(J+3),oldDimension=2*J*K+J+1,cutIndex=oldDimension-1,n=oldDimension+J;
  const bandWidth=options.halfBandwidthBlocks;
  const bandLayout=uniformPositionLayout(J,K,bandWidth);
  const radiusCoefficientBound=options.radiusCoefficientBound===undefined?.4:options.radiusCoefficientBound;
  if(!(radiusCoefficientBound>0&&radiusCoefficientBound<.8))throw Error("Require 0<radiusCoefficientBound<.8");
  let lo=.05,hi=2,curve;
  const gap=options.gap===undefined?.05:options.gap;
  if(gap===0)curve=engine.ellipse(1,1);
  else{
    for(let k=0;k<55;k++){
      const B=(lo+hi)/2,q=engine.ellipse(B+gap,B);
      if(q.a0>base.a0)hi=B;else lo=B;
    }
    const B=(lo+hi)/2;curve=engine.ellipse(B+gap,B);
  }
  const G8=engine.gauss(8),G2=engine.gauss(2);
  function cubic(t){
    const a=Math.abs(t),sg=t<0?-1:1;
    if(a>=2)return [0,0,0];
    if(a<1)return [(4-6*a*a+3*a*a*a)/6,sg*(-12*a+9*a*a)/6,(-12+18*a)/6];
    return [(2-a)**3/6,-sg*(2-a)**2/2,2-a];
  }
  function shape(s){
    if(s<=c)return {value:0,first:0,second:0};
    if(s>=S)return {value:1,first:0,second:0};
    const t=(s-c)/(S-c),L=S-c;
    return {value:t*t*t*(10+t*(-15+6*t)),
      first:30*t*t*(1-t)*(1-t)/L,second:60*t*(1-t)*(1-2*t)/(L*L)};
  }
  function angularRecord(u){
    const g=curve.at(u),modes=[];
    for(let k=1;k<=K;k++)modes.push(Math.sin(2*k*u));
    return {u,g,modes,ex:-Math.sin(u),ey:Math.cos(u)};
  }
  const nodes=[],quads=[];
  for(let j=0;j<=nq;j++)nodes.push(angularRecord(j*du));
  for(let j=0;j<nq;j++){
    const row=[];
    for(let k=0;k<8;k++)row.push({...angularRecord((j+G8.x[k])*du),weight:du*G8.w[k]});
    quads.push(row);
  }
  function seed(w,q){
    const dx=q.g.v[0]-q.ex,dy=q.g.v[1]-q.ey;
    const tx=q.ex+w.q*dx,ty=q.ey+w.q*dy,tz=w.r*q.g.h;
    const tsx=w.qs*dx,tsy=w.qs*dy,tsz=w.rs*q.g.h;
    const cp2=tx*tx+ty*ty;
    if(!(cp2>1e-15))throw Error("The explicit reference has a singular angle chart");
    return [q.u+Math.atan2(q.ex*ty-q.ey*tx,q.ex*tx+q.ey*ty),
      Math.asin(Math.max(-1,Math.min(1,tz))),
      (tx*tsy-ty*tsx)/cp2,tsz/Math.sqrt(cp2)];
  }
  function makeSlice(s,weight){
    const p=base.at(s),w=engine.profileWeights(s,c,S),angles=[],centers=[],radii=[];
    for(let j=0;j<J;j++){
      const [b,bt,btt]=cubic((s-(c+(j+2)*step))/step),bp=bt/step,bpp=btt/(step*step);
      if(b!==0||bp!==0){
        for(let k=0;k<K;k++){
          angles.push({index:j*K+k,kind:0,k,b,bp,bpp});
          angles.push({index:J*K+j*K+k,kind:1,k,b,bp,bpp});
        }
      }
      if(bp!==0)centers.push({index:2*J*K+j,b,bp,bpp});
      if(b!==0||bp!==0)radii.push({index:oldDimension+j,b,bp,bpp});
    }
    const sh=shape(s);if(sh.first!==0)centers.push({index:cutIndex,b:sh.value,bp:sh.first,bpp:sh.second});
    return {s,weight,p,w,angles,centers,radii,
      nodeSeed:nodes.map(q=>seed(w,q)),quadSeed:quads.map(row=>row.map(q=>seed(w,q)))};
  }
  let cuts=[0,S,...base.segments.map(p=>p.s0),...base.segments.map(p=>p.s1)];
  for(let j=0;j<=J+3;j++)cuts.push(c+j*step);
  cuts.sort((a,b)=>a-b);
  cuts=cuts.filter((x,i)=>i===0||x-cuts[i-1]>2e-14);
  cuts[0]=0;cuts[cuts.length-1]=S;
  const slices=[];
  for(let j=1;j<cuts.length;j++){
    const left=cuts[j-1],width=cuts[j]-left;
    for(let k=0;k<2;k++)slices.push(makeSlice(left+width*G2.x[k],width*G2.w[k]/S));
  }
  function fill(slc,q,sd,z,withJac,out){
    let th=sd[0],ph=sd[1],ths=sd[2],phs=sd[3];
    for(const col of slc.angles){
      const v=z[col.index]*q.modes[col.k];
      if(col.kind===0){th+=col.b*v;ths+=col.bp*v;}
      else{ph+=col.b*v;phs+=col.bp*v;}
    }
    const st=Math.sin(th),ct=Math.cos(th),sp=Math.sin(ph),cp=Math.cos(ph);
    const T=[-st*cp,ct*cp,sp],Dt=[-ct*cp,-st*cp,0],Dp=[st*sp,-ct*sp,cp];
    const Dtt=[st*cp,-ct*cp,0],Dtp=[ct*sp,st*sp,0];
    for(let k=0;k<3;k++){out[k]=T[k];out[3+k]=Dt[k]*ths+Dp[k]*phs;}
    if(!withJac)return;
    for(let j=0;j<slc.angles.length;j++){
      const col=slc.angles[j],v=col.b*q.modes[col.k],vs=col.bp*q.modes[col.k],off=6+6*j;
      for(let k=0;k<3;k++){
        const D=col.kind===0?Dt[k]:Dp[k];
        const Ds=col.kind===0?Dtt[k]*ths+Dtp[k]*phs:Dtp[k]*ths-T[k]*phs;
        out[off+k]=D*v;out[off+3+k]=Ds*v+D*vs;
      }
    }
  }
  function sliceValues(slc,z,withJac){
    const m=slc.angles.length,channels=6*(withJac?m+1:1);
    const total=new Float64Array(channels),moment=new Float64Array(channels);
    const prefix=new Float64Array((nq+1)*channels),out=new Float64Array(channels);
    for(let j=0;j<nq;j++){
      prefix.set(total,j*channels);
      for(let k=0;k<8;k++){
        const q=quads[j][k];fill(slc,q,slc.quadSeed[j][k],z,withJac,out);
        for(let d=0;d<channels;d++){
          const inc=q.weight*out[d];total[d]+=inc;moment[d]+=(A-q.u)*inc;
        }
      }
    }
    prefix.set(total,nq*channels);
    function primitive(node,off,k){
      const value=prefix[node*channels+off+k];
      return k===0?value-total[off+k]:k===1?value:value-moment[off+k]/A;
    }
    let zs=slc.p.zs;
    for(const col of slc.centers)zs+=z[col.index]*col.bp;
    let actualA=slc.p.a,actualAs=slc.p.as;
    for(const col of slc.radii){actualA+=z[col.index]*col.b;actualAs+=z[col.index]*col.bp;}
    const rows=[];
    for(let j=0;j<=nq;j++){
      fill(slc,nodes[j],slc.nodeSeed[j],z,withJac,out);
      const V=[],T=[out[0],out[1],out[2]];
      for(let k=0;k<3;k++)V.push(actualAs*primitive(j,0,k)+actualA*primitive(j,3,k)+(k===2?zs:0));
      const rE=V[0]*V[0]+V[1]*V[1]+V[2]*V[2]-1;
      const rF=V[0]*T[0]+V[1]*T[1]+V[2]*T[2];
      const angularWeight=(j===0||j===nq?.5:1)/nq;
      const row={s:slc.s,u:nodes[j].u,rE,rF,weight:slc.weight*angularWeight,
        relativeMetric:Math.abs(rE)/2+Math.hypot(rE/2,rF),
        immersion:1+rE-rF*rF};
      if(withJac){
        const indices=[],e=[],f=[];
        for(let a=0;a<m;a++){
          const off=6+6*a,dV=[];
          for(let k=0;k<3;k++)dV.push(actualAs*primitive(j,off,k)+actualA*primitive(j,off+3,k));
          indices.push(slc.angles[a].index);
          e.push(2*(V[0]*dV[0]+V[1]*dV[1]+V[2]*dV[2]));
          f.push(dV[0]*T[0]+dV[1]*T[1]+dV[2]*T[2]+V[0]*out[off]+V[1]*out[off+1]+V[2]*out[off+2]);
        }
        for(const col of slc.centers){indices.push(col.index);e.push(2*V[2]*col.bp);f.push(T[2]*col.bp);}
        for(const col of slc.radii){
          const dV=[];for(let k=0;k<3;k++)dV.push(col.bp*primitive(j,0,k)+col.b*primitive(j,3,k));
          indices.push(col.index);e.push(2*(V[0]*dV[0]+V[1]*dV[1]+V[2]*dV[2]));
          f.push(dV[0]*T[0]+dV[1]*T[1]+dV[2]*T[2]);
        }
        row.indices=indices;row.e=e;row.f=f;
      }
      rows.push(row);
    }
    return rows;
  }

  function evaluate(z,config={}){
    if(z.length!==n||Array.from(z).some(x=>!Number.isFinite(x)))throw Error("Wrong/nonfinite complete parameter vector");
    const maxRadiusCoefficient=Math.max(0,...Array.from(z).slice(oldDimension).map(Math.abs));
    if(maxRadiusCoefficient>radiusCoefficientBound)throw Error("Outside the declared sufficient positive-radius coefficient box");
    const jac=!!config.jacobian,need=jac||!!config.direction;
    const H=jac?createSymmetricBandAccumulator(bandLayout):null,g=jac?new Float64Array(n):null;
    const residual=[],jvp=[];
    let squaredNorm=0,maxRelativeMetric=0,minImmersion=Infinity,worst=null,rowCount=0;
    for(const slc of slices){
      for(const row of sliceValues(slc,z,need)){
        const {rE,rF,weight:w}=row;
        squaredNorm+=w*(rE*rE+2*rF*rF);rowCount+=2;
        if(row.relativeMetric>maxRelativeMetric){maxRelativeMetric=row.relativeMetric;worst={s:row.s,u:row.u,rE,rF};}
        minImmersion=Math.min(minImmersion,row.immersion);
        if(config.residuals){residual.push(Math.sqrt(w)*rE,Math.sqrt(2*w)*rF);}
        if(config.direction){
          let de=0,df=0;
          for(let j=0;j<row.indices.length;j++){const v=config.direction[row.indices[j]];de+=row.e[j]*v;df+=row.f[j]*v;}
          jvp.push(Math.sqrt(w)*de,Math.sqrt(2*w)*df);
        }
        if(jac){
          for(let i=0;i<row.indices.length;i++){
            const ii=row.indices[i],ei=row.e[i],fi=row.f[i];
            g[ii]+=w*(ei*rE+2*fi*rF);
            for(let j=0;j<=i;j++){
              const jj=row.indices[j],value=w*(ei*row.e[j]+2*fi*row.f[j]);
              H.add(ii,jj,value);
            }
          }
        }
      }
    }
    const out={squaredNorm,norm:Math.sqrt(squaredNorm),maxRelativeMetric,minImmersion,
      worst,rowCount,radialPoints:slices.length,quarterNodes:nq+1,fullEquivalentAngles:N,
      fixedPhysicalMetric:false,physicalMetricIsDesignVariable:true,maxRadiusCoefficient,conservativeRadiusLowerBound:.8-maxRadiusCoefficient,newNonlinearAcceptedState:false};
    if(jac){out.bandNormal=H.packet();out.g=g;out.diagonal=H.diagonal();}
    if(config.residuals)out.residuals=Float64Array.from(residual);
    if(config.direction)out.jvp=Float64Array.from(jvp);
    return out;
  }
  return {dimension:n,normalStorageDefinition:{schema:"R198-actual-band-normal-provider-v1",halfBandwidthBlocks:bandWidth,rawDenseMatrixAllocated:false,originalFormulaSourceSHA256:"cc45895fcf75972ee4339e5b86da70aaa589cb6491b2dbb29da26f1409771abb"},initialVector:()=>new Float64Array(n),
    normal:z=>evaluate(z,{jacobian:true}),value:z=>evaluate(z),
    evaluate,base,curve,
    definition:{
      schema:"fd2d-R190-C2-direct-position-designed-radius-finite-provider-v1",
      radialBasisCount:J,angularModes:K,fullEquivalentAngles:N,dimension:n,
      angularPrimitive:"complete quarter-cell Gauss8 with actual first moment; no Fourier projection",
      angularMetric:"exactly a^2 in mathematical complete definition",
      radialMetric:"R181 B32 plus complete C2 radius B-spline design; changing rho changes g",radiusCoefficientBound,oldDimension,
      boundary:"complete central ellipse cylinder and zero-tail round flat cut two jets",
      stateLayout:{theta:[0,J*K],phi:[J*K,2*J*K],height:[2*J*K,2*J*K+J],cutHeight:cutIndex,radius:[oldDimension,n]},
      centralGap:base.a0*(curve.A-curve.B)/curve.a0,
      centralA:base.a0*curve.A/curve.a0,centralB:base.a0*curve.B/curve.a0,
      radiusGrid:"C2 centered cardinal cubic B-splines with supports inside [c,S]",
      residual:"rE=|Xs|^2-1 and rF=Xs dot T, weighted squared rE^2+2*rF^2",
      radialQuadrature:"Gauss2 on union of original phase/Hermite breaks and spline knots",
      derivative:"complete state and primitive first-moment derivatives, fixed physical s and u",
      continuousMetricOrGeometryCertified:false,strongTargetComplete:false}
  };
}

/* R191: complete true-curvature penalty on the R187/R190 position family.
 * All angular functions remain complete. All parameter columns are analytic:
 * theta, phi, height, cut height and (for R190) the actual radius coefficients.
 */
"use strict";
function createR191BandCurvatureProvider(engine,metricProvider,options={},algebra){
  if(!algebra){
    if(typeof require==="undefined")throw Error("Supply createR191Algebra() in a pure V8 call");
    algebra=require("./fd2d-position-curvature-chain-R191.cjs").createR191Algebra();
  }
  const md=metricProvider.definition,designed=md.schema==="fd2d-R190-C2-direct-position-designed-radius-finite-provider-v1";
  if(!designed&&md.schema!=="fd2d-R187-C2-direct-position-two-angle-finite-provider-v1")throw Error("Explicit complete position provider required");
  const J=md.radialBasisCount,K=md.angularModes,N=md.fullEquivalentAngles,nq=N/4,A=Math.PI/2,du=A/nq;
  const base=metricProvider.base,curve=metricProvider.curve,c=base.centralLength,S=base.end,step=(S-c)/(J+3);
  const oldDimension=2*J*K+J+1,n=metricProvider.dimension,cutIndex=oldDimension-1;
  requireTrue(metricProvider.normalStorageDefinition&&metricProvider.normalStorageDefinition.schema==="R198-actual-band-normal-provider-v1","Use the explicit packed metric provider");
  const bandWidth=metricProvider.normalStorageDefinition.halfBandwidthBlocks,bandLayout=positionBandLayout(md,bandWidth);
  if(n!==oldDimension+(designed?J:0))throw Error("Wrong original/designed parameter layout");
  const guide=options.guide===undefined?9.5:options.guide,weight=options.weight===undefined?1e-4:options.weight;
  const nodeShare=options.nodeShare===undefined?.5:options.nodeShare;
  if(![guide,weight,nodeShare].every(Number.isFinite)||!(guide>0&&weight>0&&nodeShare>=0&&nodeShare<=1))throw Error("Explicit positive guide/weight and nodeShare in [0,1] required");
  const G8=engine.gauss(8),G2=engine.gauss(2);
  const dot=(a,b)=>a[0]*b[0]+a[1]*b[1]+a[2]*b[2];
  function cubic(t){
    const a=Math.abs(t),sg=t<0?-1:1;
    if(a>=2)return [0,0,0];
    if(a<1)return [(4-6*a*a+3*a*a*a)/6,sg*(-12*a+9*a*a)/6,(-12+18*a)/6];
    return [(2-a)**3/6,-sg*(2-a)**2/2,2-a];
  }
  function shape(s){
    if(s<=c)return [0,0,0];
    if(s>=S)return [1,0,0];
    const t=(s-c)/(S-c),L=S-c;
    return [t*t*t*(10+t*(-15+6*t)),30*t*t*(1-t)*(1-t)/L,60*t*(1-t)*(1-2*t)/(L*L)];
  }
  function record(u){
    const f=[],fu=[];
    for(let k=1;k<=K;k++){f.push(Math.sin(2*k*u));fu.push(2*k*Math.cos(2*k*u));}
    return {u,g:curve.at(u),f,fu,sn:Math.sin(u),cs:Math.cos(u)};
  }
  const angleNodes=Array.from({length:nq+1},(_,j)=>record(j*du));
  const angleQuads=Array.from({length:nq},(_,j)=>G8.x.map((x,k)=>({...record((j+x)*du),weight:du*G8.w[k]})));
  function radial(s,z){
    if(!Number.isFinite(s)||s<0||s>S||z.length!==n||Array.from(z).some(x=>!Number.isFinite(x)))throw Error("Invalid complete state or physical point");
    if(designed&&Math.max(...Array.from(z).slice(oldDimension).map(Math.abs))>md.radiusCoefficientBound)throw Error("Outside original R190 radius domain");
    const p=base.at(s),w=engine.profileWeights(s,c,S),angles=[],heights=[],radii=[];
    let a=p.a,as=p.as,ass=p.ass,Z=p.z,Zs=p.zs,Zss=p.zss;
    for(let j=0;j<J;j++){
      const q=cubic((s-(c+(j+2)*step))/step),b=q[0],bp=q[1]/step,bpp=q[2]/(step*step);
      const hz=z[2*J*K+j];Z+=hz*b;Zs+=hz*bp;Zss+=hz*bpp;
      if(designed){const rr=z[oldDimension+j];a+=rr*b;as+=rr*bp;ass+=rr*bpp;}
      if(b===0&&bp===0&&bpp===0)continue;
      for(let k=0;k<K;k++){
        angles.push({index:j*K+k,kind:0,k,b,bp,bpp});
        angles.push({index:J*K+j*K+k,kind:1,k,b,bp,bpp});
      }
      heights.push({index:2*J*K+j,b,bp,bpp});
      if(designed)radii.push({index:oldDimension+j,b,bp,bpp});
    }
    const sh=shape(s);Z+=z[cutIndex]*sh[0];Zs+=z[cutIndex]*sh[1];Zss+=z[cutIndex]*sh[2];
    if(sh.some(x=>x!==0))heights.push({index:cutIndex,b:sh[0],bp:sh[1],bpp:sh[2]});
    if(!(a>0))throw Error("Actual designed radius is not positive");
    return {s,p,w,a,as,ass,Z,Zs,Zss,angles,heights,radii};
  }
  function fill(rad,q,z,derivatives){
    const {g,sn,cs}=q,w=rad.w,ex=-sn,ey=cs,dx=g.v[0]-ex,dy=g.v[1]-ey;
    const tx=ex+w.q*dx,ty=ey+w.q*dy,tz=w.r*g.h;
    const txs=w.qs*dx,tys=w.qs*dy,tzs=w.rs*g.h,txss=w.qss*dx,tyss=w.qss*dy,tzss=w.rss*g.h;
    const txu=-cs+w.q*(g.vu[0]+cs),tyu=-sn+w.q*(g.vu[1]+sn),tzu=w.r*g.hu;
    const cp2=tx*tx+ty*ty,cp=Math.sqrt(cp2);
    if(!(cp2>1e-15))throw Error("Original reference angle chart is singular");
    const cr=tx*tys-ty*txs,hd=tx*txs+ty*tys;
    let th=q.u+Math.atan2(ex*ty-ey*tx,ex*tx+ey*ty),ph=Math.asin(Math.max(-1,Math.min(1,tz)));
    let ths=cr/cp2,phs=tzs/cp,thss=(tx*tyss-ty*txss)/cp2-2*hd*cr/(cp2*cp2),phss=tzss/cp-tzs*hd/(cp2*cp);
    let thu=(tx*tyu-ty*txu)/cp2,phu=tzu/cp;
    for(const col of rad.angles){
      const v=z[col.index]*q.f[col.k],vu=z[col.index]*q.fu[col.k];
      if(col.kind===0){th+=col.b*v;ths+=col.bp*v;thss+=col.bpp*v;thu+=col.b*vu;}
      else{ph+=col.b*v;phs+=col.bp*v;phss+=col.bpp*v;phu+=col.b*vu;}
    }
    const st=Math.sin(th),ct=Math.cos(th),sp=Math.sin(ph),co=Math.cos(ph);
    const T=[-st*co,ct*co,sp],Dt=[-ct*co,-st*co,0],Dp=[st*sp,-ct*sp,co];
    const Dtt=[st*co,-ct*co,0],Dtp=[ct*sp,st*sp,0],Dttp=[-st*sp,ct*sp,0];
    const m=derivatives?rad.angles.length:0,out=new Float64Array(12*(m+1));
    for(let k=0;k<3;k++){
      out[k]=T[k];out[3+k]=Dt[k]*ths+Dp[k]*phs;
      out[6+k]=Dt[k]*thss+Dp[k]*phss+Dtt[k]*ths*ths+2*Dtp[k]*ths*phs-T[k]*phs*phs;
      out[9+k]=Dt[k]*thu+Dp[k]*phu;
    }
    if(!derivatives)return out;
    for(let j=0;j<m;j++){
      const col=rad.angles[j],v=col.b*q.f[col.k],vs=col.bp*q.f[col.k],vss=col.bpp*q.f[col.k],vu=col.b*q.fu[col.k],off=12*(j+1);
      for(let k=0;k<3;k++){
        let D,Ds,Dss,Du;
        if(col.kind===0){
          D=Dt[k];Ds=Dtt[k]*ths+Dtp[k]*phs;Du=Dtt[k]*thu+Dtp[k]*phu;
          Dss=Dtt[k]*thss+Dtp[k]*phss-Dt[k]*(ths*ths+phs*phs)+2*Dttp[k]*ths*phs;
        }else{
          D=Dp[k];Ds=Dtp[k]*ths-T[k]*phs;Du=Dtp[k]*thu-T[k]*phu;
          Dss=Dtp[k]*thss-T[k]*phss+Dttp[k]*ths*ths-2*Dt[k]*ths*phs-Dp[k]*phs*phs;
        }
        out[off+k]=D*v;out[off+3+k]=Ds*v+D*vs;
        out[off+6+k]=Dss*v+2*Ds*vs+D*vss;out[off+9+k]=Du*v+D*vu;
      }
    }
    return out;
  }
  function slice(s,parameters,derivatives=false){
    const z=Float64Array.from(parameters),rad=radial(s,z),m=derivatives?rad.angles.length:0,blocks=m+1,channels=9*blocks;
    const total=new Float64Array(channels),moment=new Float64Array(channels),prefix=Array.from({length:nq+1},()=>new Float64Array(channels));
    function addRecord(q,out,mo){
      const v=fill(rad,q,z,derivatives);
      for(let b=0;b<blocks;b++)for(let k=0;k<9;k++){
        const at=9*b+k,inc=q.weight*v[12*b+k];out[at]+=inc;if(mo)mo[at]+=(A-q.u)*inc;
      }
    }
    for(let j=0;j<nq;j++){prefix[j].set(total);for(const q of angleQuads[j])addRecord(q,total,moment);}
    prefix[nq].set(total);
    function atQuarter(u,nodeIndex){
      let sums,q;
      if(nodeIndex!==undefined){sums=prefix[nodeIndex];q=angleNodes[nodeIndex];}
      else{
        const i=Math.min(nq,Math.floor(u/du));sums=Float64Array.from(prefix[i]);q=record(u);
        if(i<nq){const lo=i*du,w=u-lo;for(let k=0;k<8;k++)addRecord({...record(lo+w*G8.x[k]),weight:w*G8.w[k]},sums,null);}
      }
      const values=fill(rad,q,z,derivatives);
      const prim=(b,order)=>[0,1,2].map(k=>{
        const off=9*b+3*order+k;return sums[off]-(k===0?total[off]:k===2?moment[off]/A:0);
      });
      const p0={Y:prim(0,0),Ys:prim(0,1),Yss:prim(0,2),T:Array.from(values.slice(0,3)),Ts:Array.from(values.slice(3,6)),Tu:Array.from(values.slice(9,12))};
      function jets(a,as,ass,Y,Ys,Yss,T,Ts,Tu,Z,Zs,Zss){
        return {X:Y.map((v,k)=>a*v+(k===2?Z:0)),Xs:Y.map((v,k)=>as*v+a*Ys[k]+(k===2?Zs:0)),Xu:T.map(v=>a*v),
          Xss:Y.map((v,k)=>ass*v+2*as*Ys[k]+a*Yss[k]+(k===2?Zss:0)),Xsu:T.map((v,k)=>as*v+a*Ts[k]),Xuu:Tu.map(v=>a*v)};
      }
      const j=jets(rad.a,rad.as,rad.ass,p0.Y,p0.Ys,p0.Yss,p0.T,p0.Ts,p0.Tu,rad.Z,rad.Zs,rad.Zss);
      const variations=[],indices=[];
      if(derivatives){
        for(let b=1;b<blocks;b++){
          const off=12*b;
          variations.push(jets(rad.a,rad.as,rad.ass,prim(b,0),prim(b,1),prim(b,2),Array.from(values.slice(off,off+3)),Array.from(values.slice(off+3,off+6)),Array.from(values.slice(off+9,off+12)),0,0,0));
          indices.push(rad.angles[b-1].index);
        }
        for(const col of rad.heights){
          variations.push({X:[0,0,col.b],Xs:[0,0,col.bp],Xu:[0,0,0],Xss:[0,0,col.bpp],Xsu:[0,0,0],Xuu:[0,0,0]});indices.push(col.index);
        }
        for(const col of rad.radii){
          variations.push(jets(col.b,col.bp,col.bpp,p0.Y,p0.Ys,p0.Yss,p0.T,p0.Ts,p0.Tu,0,0,0));indices.push(col.index);
        }
      }
      return {jets:j,variations,indices,radial:rad};
    }
    function finish(packet,u,quadrant=0){
      if(quadrant){
        const R=[[1,1,1],[-1,1,1],[-1,-1,1],[1,-1,1]][quadrant],sign=quadrant%2?-1:1;
        const reflect=j=>Object.fromEntries(Object.entries(j).map(([key,v])=>[key,v.map((x,k)=>R[k]*x*((key==="Xu"||key==="Xsu")?sign:1))]));
        packet.jets=reflect(packet.jets);packet.variations=packet.variations.map(reflect);
      }
      const curv=algebra.curvature(packet.jets),hinge=algebra.hinge(curv.S,guide);
      const jacobian=derivatives?[new Float64Array(packet.indices.length),new Float64Array(packet.indices.length),new Float64Array(packet.indices.length)]:null;
      if(derivatives)for(let j=0;j<packet.indices.length;j++){
        const d=hinge.apply(algebra.variation(packet.jets,curv,packet.variations[j]));
        for(let k=0;k<3;k++)jacobian[k][j]=d[k];
      }
      const rE=curv.E-1,rF=curv.F/rad.a,rG=curv.G/(rad.a*rad.a)-1,h=(rE+rG)/2,rr=Math.hypot((rE-rG)/2,rF);
      return {s,u,jets:packet.jets,indices:packet.indices,jacobian,residual:hinge.residual,penaltySquared:hinge.squared,
        curvature:curv.kappa,principalCurvatures:curv.eigenvalues,orthonormalII:curv.S,
        relativeMetric:Math.max(Math.abs(h+rr),Math.abs(h-rr)),immersion:curv.w2/(rad.a*rad.a),
        threshold:hinge.threshold,parameterJets:derivatives?packet.variations:undefined};
    }
    return {node:j=>finish(atQuarter(j*du,j),j*du),point:u=>{
      const v=((u%(2*Math.PI))+2*Math.PI)%(2*Math.PI),quadrant=Math.min(3,Math.floor(v/A)),q=quadrant%2?(quadrant+1)*A-v:v-quadrant*A;
      return finish(atQuarter(Math.max(0,Math.min(A,q))),u,quadrant);
    }};
  }
  let cuts=[0,S,...base.segments.map(p=>p.s0),...base.segments.map(p=>p.s1)];
  for(let j=0;j<=J+3;j++)cuts.push(c+j*step);
  cuts.sort((a,b)=>a-b);cuts=cuts.filter((x,i)=>i===0||x-cuts[i-1]>2e-14);cuts[0]=0;cuts[cuts.length-1]=S;
  const radialPoints=[];
  if(nodeShare>0)for(let i=0;i<cuts.length;i++){
    const h=(i?cuts[i]-cuts[i-1]:0)+(i+1<cuts.length?cuts[i+1]-cuts[i]:0);
    radialPoints.push({s:cuts[i],weight:nodeShare*h/(2*S),kind:"physical_knot"});
  }
  if(nodeShare<1)for(let i=1;i<cuts.length;i++){
    const lo=cuts[i-1],h=cuts[i]-lo;
    for(let j=0;j<2;j++)radialPoints.push({s:lo+h*G2.x[j],weight:(1-nodeShare)*h*G2.w[j]/S,kind:"cell_Gauss2"});
  }
  radialPoints.sort((a,b)=>a.s-b.s);
  function penalty(z,config={}){
    const need=!!config.jacobian||!!config.direction,rows=radialPoints.length*(nq+1)*3;
    const H=config.jacobian?createSymmetricBandAccumulator(bandLayout):null,g=config.jacobian?new Float64Array(n):null;
    const residuals=config.residuals?new Float64Array(rows):null,jvp=config.direction?new Float64Array(rows):null;
    let squared=0,maxCurvature=0,minImmersion=Infinity,maxRelativeMetric=0,active=0,thresholds=0,worst=null;
    for(let ri=0;ri<radialPoints.length;ri++){
      const rp=radialPoints[ri],sl=slice(rp.s,z,false),activeNodes=[];
      for(let j=0;j<=nq;j++){
        const p=sl.node(j),aw=(j===0||j===nq?.5:1)/nq,w=weight*rp.weight*aw,off=(ri*(nq+1)+j)*3;
        squared+=w*p.penaltySquared;
        if(p.curvature>maxCurvature){maxCurvature=p.curvature;worst={s:rp.s,u:j*du,kind:rp.kind,principalCurvatures:p.principalCurvatures,relativeMetric:p.relativeMetric};}
        minImmersion=Math.min(minImmersion,p.immersion);maxRelativeMetric=Math.max(maxRelativeMetric,p.relativeMetric);
        if(p.threshold)thresholds++;
        if(residuals)for(let k=0;k<3;k++)residuals[off+k]=Math.sqrt(w)*p.residual[k];
        if(p.penaltySquared>0){active++;if(need)activeNodes.push({j,w,off});}
      }
      if(!activeNodes.length)continue;
      const sj=slice(rp.s,z,true);
      for(const {j,w,off}of activeNodes){
        const p=sj.node(j),m=p.indices.length;
        for(let a=0;a<m;a++){
          const ia=p.indices[a];let grad=0;
          for(let k=0;k<3;k++)grad+=p.jacobian[k][a]*p.residual[k];
          if(g)g[ia]+=w*grad;
          if(H)for(let b=0;b<=a;b++){
            const ib=p.indices[b];let value=0;
            for(let k=0;k<3;k++)value+=p.jacobian[k][a]*p.jacobian[k][b];
            H.add(ia,ib,w*value);
          }
        }
        if(jvp)for(let k=0;k<3;k++){
          let v=0;for(let a=0;a<m;a++)v+=p.jacobian[k][a]*config.direction[p.indices[a]];
          jvp[off+k]=Math.sqrt(w)*v;
        }
      }
    }
    const out={squaredNorm:squared,norm:Math.sqrt(squared),maxCurvature,minImmersion,maxRelativeMetric,worst,
      activePoints:active,thresholdPoints:thresholds,rowCount:rows,radialPoints:radialPoints.length,quarterNodes:nq+1,guide,weight,nodeShare};
    if(H){out.bandNormal=H.packet();out.g=g;}
    if(residuals)out.residuals=residuals;if(jvp)out.jvp=jvp;
    return out;
  }
  function evaluate(z,config={}){
    const old=metricProvider.evaluate(z,config),curv=penalty(z,config),out={...old};
    out.metricSquaredNorm=old.squaredNorm;out.curvaturePenaltySquaredNorm=curv.squaredNorm;
    out.squaredNorm=old.squaredNorm+curv.squaredNorm;out.norm=Math.sqrt(out.squaredNorm);
    out.rowCount=old.rowCount+curv.rowCount;out.curvature={...curv};delete out.curvature.H;delete out.curvature.bandNormal;delete out.curvature.g;delete out.curvature.residuals;delete out.curvature.jvp;
    if(config.jacobian){mergeBandPacketsInPlace(out.bandNormal,curv.bandNormal);for(let i=0;i<n;i++)out.g[i]+=curv.g[i];out.diagonal=bandDiagonal(out.bandNormal,bandLayout);}
    for(const key of ["residuals","jvp"])if(old[key]&&curv[key]){
      const v=new Float64Array(old[key].length+curv[key].length);v.set(old[key]);v.set(curv[key],old[key].length);out[key]=v;
    }
    out.curvatureIsNumericalGuide=true;out.continuousCertificate=false;out.strongTargetComplete=false;
    return out;
  }
  return {dimension:n,normalStorageDefinition:{schema:"R198-actual-band-normal-provider-v1",halfBandwidthBlocks:bandWidth,rawDenseMatrixAllocated:false,originalFormulaSourceSHA256:"8122d9c03850563c49594c66fd3d7b21dd7e2364063b0f90247ec0700c24759f"},initialVector:()=>metricProvider.initialVector(),base,curve,
    point:(s,u,z,config={})=>slice(s,z,!!config.jacobian).point(u),
    slice,penalty,evaluate,value:z=>evaluate(z),normal:z=>evaluate(z,{jacobian:true}),
    definition:{schema:"fd2d-R191-complete-true-curvature-hinge-finite-provider-v1",metricProvider:md,
      dimension:n,guide,weight,nodeShare,stateLayout:md.stateLayout,physicalMetricChangesWithRadius:designed,
      residual:"sqrt(weight*radialWeight*angularWeight)*(Q11,sqrt(2)Q12,Q22), Q=S-clip(S,[-guide,guide]); S is actual orthonormal II",
      radialSampling:"physical profile and B3 knots plus actual cell G2; shares declared and fixed",
      curvatureRadialPoints:radialPoints.length,quarterNodes:nq+1,
      derivatives:"All actual theta/phi/height/cut-height/radius columns via complete T/Ts/Tss/Tu and quarter primitives, actual Gram and normal; no DFT",
      angularThirdTensorsAreParameterDerivativesNotRadialC3Requirement:true,
      thresholdConvention:"inactive slope zero at exact guide; generalized derivative, not claimed smooth there",
      completeSquaredPenaltyEqualsSumPrincipalCurvatureHingesSquared:true,
      continuousMetricOrReachCertificate:false,strongTargetComplete:false}
  };
}

module.exports={positionBandLayout,createSymmetricBandAccumulator,bandDiagonal,mergeBandPacketsInPlace,preparePackedBandBorderNormal,createPackedBandNormalBackend,expandBandNormalForCheck,createR190BandProvider,createR191BandCurvatureProvider};
