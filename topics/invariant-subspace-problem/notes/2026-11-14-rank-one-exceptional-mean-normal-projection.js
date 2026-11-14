"use strict";
function rankOneNormalLinearProjection(system,tangent){
 const normals=Array.from({length:11},(_,i)=>i).filter(i=>!tangent.includes(i)),cols=[];
 for(let d=0;d<=4;d++)for(let a=0;a<=d;a++)for(const j of normals)cols.push([a,d-a,j]);
 const index=new Map(cols.map((m,i)=>[m.join(","),i])),rows=[];
 for(const e of system.equations)for(let d=0;d<=3;d++)for(let a=0;a<=d;a++){
  const row=Array(cols.length).fill(0n),add=(aa,bb,j,v)=>{row[index.get([aa,bb,j].join(","))]+=BigInt(v);};
  for(const j of normals)if(BigInt(e.linear[j]))add(a,d-a,j,e.linear[j]);
  system.quadraticMonomials.forEach(([i,j],k)=>{const ti=tangent.indexOf(i),tj=tangent.indexOf(j);if((ti>=0)===(tj>=0))return;const t=ti>=0?ti:tj,n=ti>=0?j:i;add(a+(t===0?1:0),d-a+(t===1?1:0),n,e.quadratic[k]);});
  rows.push(row.map(String));
 }
 return {cols,rows,tangent,normals};
}
function checkRankOneProjectionKernel(projection,certificate){
 const {rows,cols}=projection,{free,kernels}=certificate,count=kernels.length;
 if(rows.length!==170||cols.length!==135||!count||free.length!==count)throw new Error("Wrong dimensions");
 for(let k=0;k<count;k++){
  const v=kernels[k].map(BigInt);if(v.length!==135)throw new Error("Wrong kernel length");
  for(let j=0;j<count;j++)if((j===k&&!v[free[j]])||(j!==k&&v[free[j]]))throw new Error("Non-independent kernel certificate");
  for(const row of rows){let s=0n;for(let j=0;j<135;j++)s+=BigInt(row[j])*v[j];if(s)throw new Error("Kernel identity failed");}
 }
 return {independentRationalKernelVectors:count,projectionRankUpperBound:135-count};
}
if(typeof module!=="undefined")module.exports={rankOneNormalLinearProjection,checkRankOneProjectionKernel};
