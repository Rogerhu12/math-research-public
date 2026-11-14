/* R196 nonuniform factories: one immutable actual state, common physical
 * metric/JVP and complete position-two-jet/curvature/JVP overlap.
 * No whole normal, LM step or new accepted state.
 */
"use strict";
function checkR196Factories(engine,bundle,state,factories,bindings){
  const sp=factories.splines,algebra=factories.algebra,J=state.options.radialBasisCount,K=state.options.modes;
  const knots=sp.uniformKnots(J),inserted=["3/20","23/60"];
  function prolongVector(v){
    const cut=2*J*K+J,rows=Array.from({length:J},(_,j)=>[
      ...Array.from(v).slice(j*K,(j+1)*K),...Array.from(v).slice(J*K+j*K,J*K+(j+1)*K),v[2*J*K+j],v[cut+1+j]]);
    const p=sp.prolongCoefficients(knots,rows,inserted),nj=p.new_count,r=p.coefficients_binary64,z=[];
    for(let j=0;j<nj;j++)z.push(...r[j].slice(0,K));
    for(let j=0;j<nj;j++)z.push(...r[j].slice(K,2*K));
    for(let j=0;j<nj;j++)z.push(r[j][2*K]);
    z.push(v[cut]);
    for(let j=0;j<nj;j++)z.push(r[j][2*K+1]);
    return{z,knots:p.new_knots,J:nj};
  }
  const iz=prolongVector(state.z),direction=state.z.map((_,i)=>.001*Math.sin(i+1)),iv=prolongVector(direction);
  const oldMetric=factories.oldMetric(engine,bundle,state.options);
  const oldCurv=factories.oldCurvature(engine,oldMetric,state.curvatureOptions,algebra);
  const uniform=factories.newMetric(engine,bundle,{...state.options,radialKnots:knots},sp);
  const refined=factories.newMetric(engine,bundle,{...state.options,radialBasisCount:iz.J,radialKnots:iz.knots},sp);
  const uc=factories.newCurvature(engine,uniform,state.curvatureOptions,algebra);
  const rc=factories.newCurvature(engine,refined,state.curvatureOptions,algebra);
  if(rc.radialBasis!==refined.radialBasis||rc.radialCuts!==refined.radialCuts)throw Error("metric/curvature basis or cuts are not shared objects");
  const c=refined.base.centralLength,S=refined.base.end,points=[
    {s:c/2,u:.37},{s:.20913328,u:1.07992247},
    {s:c+(S-c)*.15,u:Math.PI/2},{s:.3935625,u:.88357293},{s:S,u:.42}];
  const jetNames=["X","Xs","Xu","Xss","Xsu","Xuu"];
  const scaled=(a,b)=>Math.abs(a-b)/(1+Math.max(Math.abs(a),Math.abs(b)));
  const metricStats={valueAbsolute:0,jvpAbsolute:0,jvpScaled:0};
  const jetStats={valueAbsolute:0,valueScaled:0,jvpAbsolute:0,jvpScaled:0};
  const curvatureStats={valueAbsolute:0,residualAbsolute:0,jvpAbsolute:0,jvpScaled:0};
  const rows=[];
  function metricJvp(row,v){
    const d=[0,0];for(let k=0;k<row.indices.length;k++){d[0]+=row.e[k]*v[row.indices[k]];d[1]+=row.f[k]*v[row.indices[k]];}return d;
  }
  function curvatureJvp(p,v){
    return p.jacobian.map(row=>row.reduce((s,a,k)=>s+a*v[p.indices[k]],0));
  }
  function jetJvp(p,v){
    const out=Object.fromEntries(jetNames.map(k=>[k,[0,0,0]]));
    for(let j=0;j<p.indices.length;j++)for(const k of jetNames)for(let a=0;a<3;a++)out[k][a]+=p.parameterJets[j][k][a]*v[p.indices[j]];
    return out;
  }
  let active=0;
  for(const pt of points){
    const om=oldMetric.metricRows(pt.s,state.z,{jacobian:true});
    const nm=refined.metricRows(pt.s,iz.z,{jacobian:true});
    if(om.length!==nm.length)throw Error("common angular row grid changed");
    for(let j=0;j<om.length;j++){
      metricStats.valueAbsolute=Math.max(metricStats.valueAbsolute,Math.abs(om[j].rE-nm[j].rE),Math.abs(om[j].rF-nm[j].rF));
      const a=metricJvp(om[j],direction),b=metricJvp(nm[j],iv.z);
      for(let k=0;k<2;k++){metricStats.jvpAbsolute=Math.max(metricStats.jvpAbsolute,Math.abs(a[k]-b[k]));metricStats.jvpScaled=Math.max(metricStats.jvpScaled,scaled(a[k],b[k]));}
    }
    const o=oldCurv.point(pt.s,pt.u,state.z,{jacobian:true}),r=rc.point(pt.s,pt.u,iz.z,{jacobian:true}),u=uc.point(pt.s,pt.u,state.z,{jacobian:true});
    const jo=jetJvp(o,direction),jr=jetJvp(r,iv.z);
    const oj=curvatureJvp(o,direction),rj=curvatureJvp(r,iv.z);
    let uniformDifference=0;
    for(const k of jetNames)for(let a=0;a<3;a++){
      jetStats.valueAbsolute=Math.max(jetStats.valueAbsolute,Math.abs(o.jets[k][a]-r.jets[k][a]));
      jetStats.valueScaled=Math.max(jetStats.valueScaled,scaled(o.jets[k][a],r.jets[k][a]));
      jetStats.jvpAbsolute=Math.max(jetStats.jvpAbsolute,Math.abs(jo[k][a]-jr[k][a]));
      jetStats.jvpScaled=Math.max(jetStats.jvpScaled,scaled(jo[k][a],jr[k][a]));
      uniformDifference=Math.max(uniformDifference,Math.abs(o.jets[k][a]-u.jets[k][a]));
    }
    curvatureStats.valueAbsolute=Math.max(curvatureStats.valueAbsolute,Math.abs(o.curvature-r.curvature));
    for(let k=0;k<3;k++){
      curvatureStats.residualAbsolute=Math.max(curvatureStats.residualAbsolute,Math.abs(o.residual[k]-r.residual[k]));
      curvatureStats.jvpAbsolute=Math.max(curvatureStats.jvpAbsolute,Math.abs(oj[k]-rj[k]));
      curvatureStats.jvpScaled=Math.max(curvatureStats.jvpScaled,scaled(oj[k],rj[k]));
    }
    if(o.penaltySquared>0&&r.penaltySquared>0)active++;
    rows.push({...pt,oldCurvature:o.curvature,newCurvature:r.curvature,oldPenalty:o.penaltySquared,newPenalty:r.penaltySquared,
      uniform_vs_old_complete_twojet_max:uniformDifference,oldIndices:o.indices.length,newIndices:r.indices.length,
      newActiveBlocks:refined.radialBasis.physicalJets(pt.s,c,S).indices});
  }
  if(active===0)throw Error("fixture has no genuinely active curvature penalty");
  if(metricStats.jvpScaled>1e-8||jetStats.valueScaled>1e-8||jetStats.jvpScaled>1e-8||curvatureStats.jvpScaled>1e-8)throw Error("actual identity/JVP discrepancy exceeds fixture diagnostic scale");
  return{schema:"fd2d-R196-actual-nonuniform-factory-overlap-v1",passed:true,bindings,
    oldDimension:state.z.length,newDimension:iz.z.length,inserted_knots:inserted,
    actual_active_curvature_points:active,commonPhysicalPoints:rows,
    metric:metricStats,completePositionTwoJets:jetStats,curvaturePenalty:curvatureStats,
    metricDefinition:refined.definition,curvatureDefinition:rc.definition,
    actual_basis_object_shared:true,actual_cut_array_shared:true,
    commonPointRowsOnly:true,wholeNormalOrBVPStarted:false,newAcceptedState:false,
    fieldIdentity:"exact real Boehm composition; separately measured binary64 overlap",
    quadrature_note:"New knots define a new finite radial sampling. This check compares the same physical points, not two different complete quadrature vectors."};
}
if(typeof module!=="undefined"&&module.exports)module.exports={checkR196Factories};
