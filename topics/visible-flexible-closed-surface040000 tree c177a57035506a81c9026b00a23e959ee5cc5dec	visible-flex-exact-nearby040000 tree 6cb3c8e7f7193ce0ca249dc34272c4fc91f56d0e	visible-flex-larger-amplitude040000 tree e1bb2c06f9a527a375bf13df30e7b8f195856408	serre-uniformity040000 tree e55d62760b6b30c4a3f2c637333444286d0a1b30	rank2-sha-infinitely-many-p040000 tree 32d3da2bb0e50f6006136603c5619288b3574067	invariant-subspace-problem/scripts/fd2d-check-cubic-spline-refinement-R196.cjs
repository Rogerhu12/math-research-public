/* R196: one immutable J27/433 state, exact refinement and floating jet overlap.
 * This is not a solver state for an old uniform-grid factory.
 */
"use strict";
function checkR196Refinement(createSplines,actualState,physical,bindings){
  const api=createSplines(),J=actualState.options.radialBasisCount,K=actualState.options.modes,z=actualState.z;
  if(J!==27||K!==7||z.length!==J*(2*K+2)+1)throw Error("fixture expects the explicitly bound actual 433 state");
  const cut=2*J*K+J,rows=Array.from({length:J},(_,j)=>[
    ...z.slice(j*K,(j+1)*K),...z.slice(J*K+j*K,J*K+(j+1)*K),z[2*J*K+j],z[cut+1+j]]);
  const oldKnots=api.uniformKnots(J),inserted=["3/20","23/60"],p=api.prolongCoefficients(oldKnots,rows,inserted);
  const points=["0","1/120","1/30","1/10","3/20","1/6","1/5","37/100","23/60","2/3","29/30","119/120","1"];
  let comparisons=0;
  for(const q of points){
    const a=api.evaluateExact(oldKnots,rows,q),b=api.evaluateExact(p.new_knots,p.coefficients_exact,q);
    for(const name of["value","first","second"]){
      if(JSON.stringify(a[name])!==JSON.stringify(b[name]))throw Error("exact field identity failed at "+q+" "+name);
      comparisons+=a[name].length;
    }
  }
  const old=api.createBasis(oldKnots),fresh=api.createBasis(p.new_knots);
  function sum(jets,coef){
    const result={value:Array(coef[0].length).fill(0),first:Array(coef[0].length).fill(0),second:Array(coef[0].length).fill(0)};
    for(const name of Object.keys(result))for(let k=0;k<jets.indices.length;k++){
      const row=coef[jets.indices[k]];for(let h=0;h<row.length;h++)result[name][h]+=jets[name][k]*row[h];
    }return result;
  }
  function legacy(s){
    const L=physical.S-physical.c,h=L/(J+3),v={value:Array(2*K+2).fill(0),first:Array(2*K+2).fill(0),second:Array(2*K+2).fill(0)};
    for(let j=0;j<J;j++){
      const t=(s-(physical.c+(j+2)*h))/h,a=Math.abs(t),sg=t<0?-1:1;
      const b=a>=2?[0,0,0]:a<1?[(4-6*a*a+3*a*a*a)/6,sg*(-12*a+9*a*a)/6,(-12+18*a)/6]:[(2-a)**3/6,-sg*(2-a)**2/2,2-a];
      for(let k=0;k<rows[j].length;k++){v.value[k]+=b[0]*rows[j][k];v.first[k]+=b[1]/h*rows[j][k];v.second[k]+=b[2]/(h*h)*rows[j][k];}
    }return v;
  }
  const number=x=>{if(typeof x==="number")return x;const q=Array.isArray(x)?x:x.split("/");return Number(q[0])/(q.length>1?Number(q[1]):1);};
  const physicalPoints=points.map(q=>physical.c+(physical.S-physical.c)*number(q));
  physicalPoints.push(.20913328,.3935625);
  const max={old_normalized_vs_refined:{value:0,first:0,second:0},legacy_uniform_vs_refined:{value:0,first:0,second:0}};
  const at=[];
  for(const s of physicalPoints){
    const oj=old.physicalJets(s,physical.c,physical.S),nj=fresh.physicalJets(s,physical.c,physical.S);
    if(oj.indices.length>4||nj.indices.length>4)throw Error("lost cubic locality");
    const a=sum(oj,rows),b=sum(nj,p.coefficients_binary64),l=legacy(s),r={s,q:nj.q,active:nj.indices};
    for(const name of["value","first","second"]){
      const d=Math.max(...a[name].map((x,i)=>Math.abs(x-b[name][i]))),
      e=Math.max(...l[name].map((x,i)=>Math.abs(x-b[name][i])));
      max.old_normalized_vs_refined[name]=Math.max(max.old_normalized_vs_refined[name],d);
      max.legacy_uniform_vs_refined[name]=Math.max(max.legacy_uniform_vs_refined[name],e);
      r[name]={normalized_difference:d,legacy_difference:e};
    }at.push(r);
  }
  for(const q of["0","1"]){
    const j=fresh.exactJets(q);if(j.indices.length)throw Error("nonzero boundary two-jet");
  }
  // First and last spans use the same Boehm identity with implicit zero outside coefficients.
  const boundaryRows=[[1,-2],[3,4],[-5,6],[7,-8]],boundaryKnots=api.uniformKnots(4);
  const bp=api.prolongCoefficients(boundaryKnots,boundaryRows,["1/56","55/56"]);
  for(const q of["0","1/112","1/56","1/7","1/2","6/7","55/56","111/112","1"]){
    const a=api.evaluateExact(boundaryKnots,boundaryRows,q),b=api.evaluateExact(bp.new_knots,bp.coefficients_exact,q);
    for(const name of["value","first","second"])if(JSON.stringify(a[name])!==JSON.stringify(b[name]))throw Error("boundary-span identity failed");
  }
  const newJ=p.new_count,newVector=[];
  for(let j=0;j<newJ;j++)newVector.push(...p.coefficients_binary64[j].slice(0,K));
  for(let j=0;j<newJ;j++)newVector.push(...p.coefficients_binary64[j].slice(K,2*K));
  for(let j=0;j<newJ;j++)newVector.push(p.coefficients_binary64[j][2*K]);
  newVector.push(z[cut]);
  for(let j=0;j<newJ;j++)newVector.push(p.coefficients_binary64[j][2*K+1]);
  return{schema:"fd2d-R196-actual-J27-cubic-refinement-check-v1",passed:true,bindings,physical_interval:physical,
    old_layout:{J,K,dimension:z.length,cut_height_index:cut},new_layout:{J:newJ,K,dimension:newVector.length,cut_height_index:2*newJ*K+newJ},
    channel_order:"theta modes, phi modes, axial height, radius; cut-height scalar copied unchanged",
    inserted_knots:inserted,inserted_physical_points:inserted.map(q=>physical.c+(physical.S-physical.c)*number(q)),
    exact_common_point_component_comparisons:comparisons,exact_arithmetic_identity:true,
    normalized_test_points:points,floating_differences:max,floating_common_points:at,
    endpoint_zero_two_jets_exact:true,first_and_last_span_insertion_exact:true,max_active_radial_blocks:4,
    prolongation:p,refined_vector:newVector,cut_height_copied_identically:newVector[2*newJ*K+newJ]===z[cut],
    old_candidate_profile_atlas_central_gap_or_angular_modes_changed:false,
    new_solver_or_native_state_claimed:false,requires_new_factory_to_consume_explicit_knots:true,
    full_position_floating_two_jets_recomputed:false,
    scope:"exact complete scalar radial channel two-jets; full nonlinear position is identical in real arithmetic by composition/primitive linearity; actual floating overlap only for the reported scalar channels"};
}
if(typeof module!=="undefined"&&module.exports)module.exports={checkR196Refinement};
