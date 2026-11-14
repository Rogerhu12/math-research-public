/* Explicit fixed-state R190 geometry adapter, using the closed R187 jets.
 * Only a/as/ass change; original Z, angular lifting, physical s and all
 * spline supports stay unchanged. No old fixed-metric identity is claimed.
 */
"use strict";
function createR190GeometryView(engine,oldProvider,designedProvider,fullParameters,createR187Geometry){
  const od=oldProvider.definition,dd=designedProvider.definition;
  if(od.schema!=="fd2d-R187-C2-direct-position-two-angle-finite-provider-v1"||
     dd.schema!=="fd2d-R190-C2-direct-position-designed-radius-finite-provider-v1")
    throw Error("Explicit original and designed-radius providers required");
  const J=dd.radialBasisCount,K=dd.angularModes,oldDimension=dd.oldDimension,z=Float64Array.from(fullParameters);
  if(oldDimension!==oldProvider.dimension||dd.dimension!==oldDimension+J||z.length!==dd.dimension||Array.from(z).some(x=>!Number.isFinite(x)))
    throw Error("Wrong complete R190 parameter layout");
  if(J!==od.radialBasisCount||K!==od.angularModes||dd.fullEquivalentAngles!==od.fullEquivalentAngles||
     oldProvider.base.end!==designedProvider.base.end||oldProvider.curve.A!==designedProvider.curve.A||
     oldProvider.curve.B!==designedProvider.curve.B)
    throw Error("The declared shared original metric/angle reference differs");
  const rho=Array.from(z.slice(oldDimension)),maxRadiusCoefficient=Math.max(...rho.map(Math.abs));
  if(maxRadiusCoefficient>dd.radiusCoefficientBound)throw Error("Outside actual R190 radius coefficient box");
  const parent=oldProvider.base,c=parent.centralLength,S=parent.end,step=(S-c)/(J+3);
  function cubic(t){
    const a=Math.abs(t),sg=t<0?-1:1;
    if(a>=2)return [0,0,0];
    if(a<1)return [(4-6*a*a+3*a*a*a)/6,sg*(-12*a+9*a*a)/6,(-12+18*a)/6];
    return [(2-a)**3/6,-sg*(2-a)**2/2,2-a];
  }
  const modifiedBase={...parent,at(s){
    const p=parent.at(s);let a=p.a,as=p.as,ass=p.ass;
    for(let j=0;j<J;j++){
      const [b,bt,btt]=cubic((s-(c+(j+2)*step))/step);
      a+=rho[j]*b;as+=rho[j]*bt/step;ass+=rho[j]*btt/(step*step);
    }
    return {...p,a,as,ass};
  }};
  const providerView={...oldProvider,base:modifiedBase};
  const geometry=createR187Geometry(engine,providerView);
  return {providerView,geometry,oldParameters:z.slice(0,oldDimension),fullParameters:z,
    definition:{schema:"fd2d-R190-explicit-designed-radius-geometry-view-v1",
      designed_provider:dd,inner_geometry:geometry.definition(),state_layout:dd.stateLayout,
      original_dimension:oldDimension,complete_dimension:dd.dimension,radius_coefficients:rho,
      maxRadiusCoefficient,conservativeRadiusLowerBound:.8-maxRadiusCoefficient,
      actual_formula:"a=a_base+sum rho_j B_j; as/ass differentiated analytically, original Zbg unchanged",
      old_provider_evaluate_or_normal_used:false,
      old_schema_is_only_the_inner_two_jet_formula_interface:true,
      physical_metric_changes_with_rho:true,continuous_certificate:false}};
}
if(typeof module!=="undefined"&&module.exports)module.exports={createR190GeometryView};
