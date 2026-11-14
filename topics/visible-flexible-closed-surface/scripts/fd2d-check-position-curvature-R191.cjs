/* R191 one local nonzero-state analytic-parameter-jet check.
 * The fixture is the immutable actual R187 step16 state; R190 appends
 * exactly zero radius controls and tests real nonzero radius directions.
 */
"use strict";
function checkR191Local(engine,bundle,state,factories){
  const start=Date.now(),alg=factories.algebra(),fixed=factories.fixed(engine,bundle,state.options);
  const p=factories.curvature(engine,fixed,{guide:9.5,weight:1e-4},alg);
  const opts={...state.options,radiusCoefficientBound:.4},designed=factories.designed(engine,bundle,opts);
  const q=factories.curvature(engine,designed,{guide:9.5,weight:1e-4},factories.algebra());
  const z0=Float64Array.from(state.z),z1=new Float64Array(q.dimension);z1.set(z0);
  const points=[[.36293298329056384,Math.PI/2],[.36293298329056384,1.55],[.36293298329056384,1.47]];
  const rows=[];
  function jvp(r,d,key){
    if(key==="residual")return [0,1,2].map(k=>r.indices.reduce((sum,index,j)=>sum+r.jacobian[k][j]*d[index],0));
    return [0,1,2].map(k=>r.indices.reduce((sum,index,j)=>sum+r.parameterJets[j][key][k]*d[index],0));
  }
  const max=v=>Math.max(...v.map(Math.abs)),keys=["X","Xs","Xu","Xss","Xsu","Xuu"];
  for(const [s,u]of points){
    const a=p.point(s,u,z0,{jacobian:true}),b=q.point(s,u,z1,{jacobian:true});
    const direction=Float64Array.from({length:q.dimension},(_,i)=>.02*Math.sin((i+1)*.37)+.01*Math.cos((i+1)*.19));
    const radiusOnly=new Float64Array(q.dimension);for(let j=181;j<q.dimension;j++)radiusOnly[j]=direction[j];
    const overlap=Math.max(...keys.map(key=>max(a.jets[key].map((x,k)=>x-b.jets[key][k]))));
    const groups={theta:[0,84],phi:[84,168],height:[168,180],cutHeight:[180,181],radius:[181,193]};
    const columnNorms={};
    for(const [name,[lo,hi]]of Object.entries(groups)){
      let v=0;for(let j=0;j<b.indices.length;j++)if(b.indices[j]>=lo&&b.indices[j]<hi)for(let k=0;k<3;k++)v=Math.max(v,Math.abs(b.jacobian[k][j]));
      columnNorms[name]=v;
    }
    const trials=[];
    for(const [name,d]of [["all_parameters",direction],["radius_only",radiusOnly]]){
      const pred=jvp(b,d,"residual");
      for(const h of [2e-6,1e-6,5e-7]){
        const plus=Float64Array.from(z1,(v,i)=>v+h*d[i]),minus=Float64Array.from(z1,(v,i)=>v-h*d[i]);
        const pp=q.point(s,u,plus),pm=q.point(s,u,minus),fd=pp.residual.map((v,k)=>(v-pm.residual[k])/(2*h));
        const abs=max(fd.map((v,k)=>v-pred[k])),scaled=abs/Math.max(1,max(pred));
        const jetErrors={};
        for(const key of keys){const pr=jvp(b,d,key),df=pp.jets[key].map((v,k)=>(v-pm.jets[key][k])/(2*h));
          jetErrors[key]={absolute:max(df.map((v,k)=>v-pr[k])),scaled:max(df.map((v,k)=>v-pr[k]))/Math.max(1,max(pr))};}
        trials.push({direction:name,h,analytic:pred,finite_difference:fd,maximum_absolute:abs,maximum_scaled:scaled,position_parameter_jet_errors:jetErrors});
      }
    }
    rows.push({s,u,fixed_radius_zero_injection_position_jet_difference:overlap,curvature:b.curvature,eigenvalues:b.principalCurvatures,
      residual:b.residual,active_parameter_columns:b.indices.length,group_column_maximum:columnNorms,trials});
  }
  return {schema:"fd2d-R191-actual-step16-local-complete-curvature-JVP-v1",runtime:{engine:"pure JavaScript/V8",completed:true,milliseconds:Date.now()-start,OS_child_created:false,OS_exit_code:null},
    input:{kind:state.kind,iteration:state.iteration,original_dimension:181,original_options:state.options,source_identity:state.identity,
      appended_radius:[181,193],appended_radius_values:Array(12).fill(0),designed_state_is_explicit_zero_embedding_not_a_new_accepted_state:true},
    definition:q.definition,points:rows,
    finite_difference_diagnostic_not_a_continuous_bound:true,no_whole_normal_or_BVP_run:true};
}
if(typeof module!=="undefined"&&module.exports)module.exports={checkR191Local};
