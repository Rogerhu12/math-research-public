/* Small actual 0--2-jet overlap check for the R187 geometry consumer.
 * Uses complete functions, no DFT. Finite differences are local diagnostics.
 */
"use strict";
function checkR187Geometry(engine,provider,createGeometry){
  const started=Date.now(),geometry=createGeometry(engine,provider),base=provider.base,def=provider.definition;
  if(def.radialBasisCount!==12||def.angularModes!==7||def.fullEquivalentAngles!==64)
    throw Error("This closed small fixture binds J12/K7/N64");
  const zero=provider.initialVector(),z=Float64Array.from(zero),step=(base.end-base.centralLength)/15;
  const nonzero=[[15,.018],[37,-.011],[105,.014],[136,-.009],[172,.006],[180,.02]];
  for(const [i,v] of nonzero)z[i]=v;
  const max=v=>Math.max(...v.map(Math.abs));
  const error=(a,b)=>max(a.map((x,j)=>x-b[j]));
  const initialAngular=engine.angular(provider.curve,64),zeroRows=[];
  const initialPoints=[[0,0],[base.centralLength,5],[.31,7],[.55,19],[.83,43],[base.end,16]];
  for(const [s,j] of initialPoints){
    const g=initialAngular.rows[j],actual=geometry.point(s,g.u,zero);
    const previous=engine.point(base.at(s),engine.profileWeights(s,base.centralLength,base.end),g);
    zeroRows.push({s,u:g.u,positionMaximumDifference:error(actual.X,previous.X),
      metricMaximumDifference:Math.max(Math.abs(actual.geometry.E-previous.E),Math.abs(actual.geometry.F-previous.F),Math.abs(actual.geometry.G-previous.G)),
      curvatureDifference:Math.abs(actual.geometry.curvature-previous.curvature)});
  }
  const locations=[
    [base.centralLength+4.2*step,.37],
    [base.centralLength+8.4*step,2.31],
    [base.centralLength+10.3*step,5.12]
  ],fd=[];
  const vectorKeys=["Xs","Xu","Xss","Xsu","Xuu"];
  for(const [s,u] of locations){
    const at=geometry.point(s,u,z),rows=[];
    for(const h of [2e-6,1e-6]){
      const sp=geometry.point(s+h,u,z),sm=geometry.point(s-h,u,z),up=geometry.point(s,u+h,z),um=geometry.point(s,u-h,z);
      const d=(a,b)=>a.map((x,j)=>(x-b[j])/(2*h));
      const raw={
        Xs:error(d(sp.X,sm.X),at.Xs),Xu:error(d(up.X,um.X),at.Xu),
        Xss:error(d(sp.Xs,sm.Xs),at.Xss),Xuu:error(d(up.Xu,um.Xu),at.Xuu),
        Xsu_from_Xs:error(d(up.Xs,um.Xs),at.Xsu),Xsu_from_Xu:error(d(sp.Xu,sm.Xu),at.Xsu),
        Tss:error(d(sp.Ts,sm.Ts),at.Tss)
      };
      const scaled={};
      for(const [key,v]of Object.entries(raw)){
        const target=key.startsWith("Xsu")?at.Xsu:at[key];
        scaled[key]=v/Math.max(1,...target.map(Math.abs));
      }
      rows.push({h,maximum_absolute:raw,maximum_scaled:scaled});
    }
    fd.push({s,u,tangent_identities:at.tangentIdentities,geometry:at.geometry,finite_differences:rows});
  }
  const boundary=[];
  for(const s of [0,base.centralLength,base.end]){
    const before=geometry.point(s,.63,zero),after=geometry.point(s,.63,z);
    const positionExpected=before.X.map((x,j)=>x+(s===base.end&&j===2?.02:0));
    boundary.push({s,positionDifferenceFromDeclaredBoundary:error(after.X,positionExpected),
      maximumJetDifference:Math.max(...vectorKeys.map(key=>error(after[key],before[key])))});
  }
  const sample=geometry.samples(z,{s_values:locations.map(x=>x[0]),u_values:[0,.37,Math.PI/2,2.31,Math.PI,5.12]});
  return {schema:"fd2d-R187-actual-position-two-jet-local-check-v1",
    runtime:{engine:"pure JavaScript/V8",completed:true,milliseconds:Date.now()-started,OS_child_created:false,OS_exit_code:null},
    provider_definition:def,geometry_definition:geometry.definition(),
    nonzero_parameter_entries:nonzero,zero_parameter_overlap:zeroRows,local_differential_checks:fd,
    exact_boundary_fixture:boundary,nonzero_finite_sample:sample.summary,
    assertion_scope:"Finite local overlap and differential consistency; not a continuous certificate or a nonlinear solve",
    no_whole_BVP_or_body:true};
}
if(typeof module!=="undefined"&&module.exports)module.exports={checkR187Geometry};
