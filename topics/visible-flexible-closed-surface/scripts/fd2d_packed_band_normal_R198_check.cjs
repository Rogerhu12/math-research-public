"use strict";
/* Reproducer for the recorded inline check. Caller supplies one already
 * evaluated packed normal and the saved dense normal. No normal/F/J call
 * is made here; optional point packets must be actual complete packets. */
function checkPackedNormal(pack,kernel,packedNormal,denseNormal,definition,lambda,points={}){
  const vec=x=>{
    if(x&&typeof x.length==="number")return Float64Array.from(x);
    const keys=Object.keys(x||{});if(!keys.every((k,i)=>k===String(i)))throw Error("Noncontiguous numeric-key vector");
    return Float64Array.from(keys,k=>x[k]);
  };
  const normal={...packedNormal,g:vec(packedNormal.g),diagonal:vec(packedNormal.diagonal),
    bandNormal:{...packedNormal.bandNormal,lower:vec(packedNormal.bandNormal.lower),border:vec(packedNormal.bandNormal.border)}};
  const expanded=pack.expandBandNormalForCheck(normal,definition),maxDiff=(a,b)=>{
    a=vec(a);b=vec(b);if(a.length!==b.length)throw Error("Dimension mismatch");
    let d=0;for(let i=0;i<a.length;i++)d=Math.max(d,Math.abs(a[i]-b[i]));return d;
  };
  const prepared=pack.preparePackedBandBorderNormal(normal,definition,{halfBandwidthBlocks:normal.bandNormal.halfBandwidthBlocks});
  const solved=kernel.solvePreparedBandBorder(prepared,lambda);
  if(!solved.ok)throw Error("Packed actual solve failed");
  const original=kernel.solveDampedNormal(denseNormal,{definition,lambda,halfBandwidthBlocks:normal.bandNormal.halfBandwidthBlocks});
  if(!original.ok)throw Error("Original actual solve failed");
  let pointMaximum=0,pointLeaves=0;
  function compare(a,b){
    if(typeof a==="number"){if(!Number.isFinite(a)||!Number.isFinite(b))throw Error("Nonfinite actual point");pointMaximum=Math.max(pointMaximum,Math.abs(a-b));pointLeaves++;return;}
    if(a==null||typeof a!=="object"){if(a!==b)throw Error("Unequal actual point");return;}
    const ka=Object.keys(a),kb=Object.keys(b);if(JSON.stringify(ka)!==JSON.stringify(kb))throw Error("Unequal point schema");
    for(const k of ka)compare(a[k],b[k]);
  }
  if(points.old||points.packed){if(!points.old||!points.packed)throw Error("Both actual point packets required");compare(points.old,points.packed);}
  const out={squaredNormDifference:normal.squaredNorm-denseNormal.squaredNorm,
    HMaximumDifference:maxDiff(expanded.H,denseNormal.H),gradientMaximumDifference:maxDiff(normal.g,denseNormal.g),
    diagonalMaximumDifference:maxDiff(normal.diagonal,denseNormal.diagonal),directionMaximumDifference:maxDiff(solved.direction,original.direction),
    pointMaximumDifference:pointLeaves?pointMaximum:null,pointNumericLeaves:pointLeaves,
    solverInfo:solved.info,normalOrValueCalled:false,newNonlinearAcceptedState:false};
  out.passed=out.squaredNormDifference===0&&out.HMaximumDifference===0&&out.gradientMaximumDifference===0&&out.diagonalMaximumDifference===0&&
    out.directionMaximumDifference<1e-12&&pointMaximum===0;
  if(!out.passed)throw Object.assign(Error("Packed normal comparison failed"),{report:out});
  return out;
}
module.exports={checkPackedNormal};
