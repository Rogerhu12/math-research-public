/* R194 small exact-arithmetic consumers. No B32 state, solver, or whole body. */
"use strict";
function runR194Fixtures(createCertificate,r193ArithmeticFixture) {
  const c=createCertificate();
  const I=(lo,hi=lo)=>({lower:lo,upper:hi});
  const common={scope:"certified common continuous physical box",derivatives:"fixed physical s,u",
    bindings:{geometry_definition:"X(s,u)=(s,u,s^2+s*u/2-u^2/2)",
      domain:{s:["-1/100","1/100"],u:["-1/100","1/100"]},
      enclosure_evidence:"exact polynomial derivatives and rational box arithmetic; analytic fixture, not repository candidate"}};
  const graph={...common,jets:{
    Xs:["1","0",I("-1/40","1/40")],Xu:["0","1",I("-3/200","3/200")],
    Xss:["0","0","2"],Xsu:["0","0","1/2"],Xuu:["0","0","-1"]
  }};
  const graphCertificate=c.certifyCartesianJetBox(graph,"21/10");
  if(!graphCertificate.passed||!graphCertificate.strict_cap_proved)throw Error("continuous quadratic graph cap did not close");
  const origin={...graph,scope:"certified single physical point",
    bindings:{...graph.bindings,domain:{s:"0",u:"0"}},jets:{...graph.jets,Xs:["1","0","0"],Xu:["0","1","0"]}};
  const tooSmall=c.certifyCartesianJetBox(origin,"2");
  if(tooSmall.passed)throw Error("false curvature cap was accepted");
  const formMeta={scope:"certified single physical point",bindings:origin.bindings};
  const form=c.certifyFormBox({...formMeta,H:["1","0","1"],Q:["2","1/2","-1"]},"21/10");
  const rotated=c.certifyFormBox({...formMeta,H:["1","0","1"],Q:["14/25","-79/50","11/25"]},"21/10");
  const rescaled=c.certifyFormBox({...formMeta,H:["9","0","4"],Q:["18","3","-4"]},"21/10");
  if(!form.passed||!rotated.passed||!rescaled.passed)throw Error("exact 2x2 coordinate checks failed");
  const cylinder={scope:"certified common continuous physical box",derivatives:"fixed physical s,u",
    bindings:{geometry_definition:"X(s,u)=(s,sin(u),-cos(u)); a=1",
      domain:{s:["-1","1"],u:["-1/100","1/100"]},
      enclosure_evidence:"|sin u|<=1/100 and 1-u^2/2<=cos u<=1, with exact unit tangent"},
    exact_unit_tangent:true,exact_position_identity:"X_u=a T; X_s=V",
    jets:{a:"1",V:["1","0","0"],T:["0",I("19999/20000","1"),I("-1/100","1/100")],
      Ts:["0","0","0"],Tu:["0",I("-1/100","1/100"),I("19999/20000","1")],Xss:["0","0","0"]}
  };
  const cylinderCertificate=c.certifyUnitTangentJetBox(cylinder,"1001/1000");
  const cylinderSharpUnresolved=c.certifyUnitTangentJetBox(cylinder,"1");
  if(!cylinderCertificate.passed||cylinderSharpUnresolved.passed)throw Error("unit tangent/interval unresolved distinction failed");
  let adapter=null;
  if(r193ArithmeticFixture){
    const f=r193ArithmeticFixture();
    const b=f.nonzero_result;
    adapter=c.fromR193Budget(b,{
      scope:b.scope,expected_budget_bindings:b.bindings,
      Q0_definition:"N0 dot [Xss0,Ts0,Tu0/a0]",Q0:["6","0","-5"],
      domain:{kind:"same conditional arithmetic fixture box as R193; not an actual B32 enclosure"},
      Q0_evidence:{kind:"additional exact conditional component bounds [6,0,-5]; not sampled principal curvatures"},
      budget_evidence:{source:"fd2d_R193_direct_position_error_budget.cjs",fixture:"runR193BudgetFixture nonzero_result"}
    },"15/2");
    if(!adapter.passed)throw Error("R193 component-error adapter did not close its conditional fixture");
  }
  return {schema:"fd2d-R194-actual-exact-arithmetic-fixture-v1",passed:true,
    continuous_quadratic_graph:{input:graph,result:graphCertificate},
    false_cap_at_origin:{result:tooSmall,exact_Rayleigh_witness:{vector:["10","1"],Q_energy:"209",H_energy:"101",cap_energy:"202"}},
    exact_coordinate_changes:{original:form,rotation_3_4_5:rotated,coordinate_scales_3_2:rescaled},
    continuous_unit_cylinder:{input:cylinder,result:cylinderCertificate,sharp_cap_interval_unresolved:cylinderSharpUnresolved},
    R193_conditional_adapter:adapter,
    OS_subprocess_started:false,repository_B32_or_complete_surface_certified:false,
    scope_note:"The graph and cylinder are analytic verification fixtures. The R193 data are conditional arithmetic hypotheses. No repository candidate box was certified."
  };
}
if(typeof module!=="undefined"&&module.exports){
  module.exports={runR194Fixtures};
  if(require.main===module){
    const f=require("./fd2d-position-curvature-certificate-R194.cjs").createR194CurvatureCertificate;
    let r=null;try{r=require("./fd2d_R193_direct_position_error_budget.cjs").runR193BudgetFixture;}catch(e){if(e.code!=="MODULE_NOT_FOUND")throw e;}
    console.log(JSON.stringify(runR194Fixtures(f,r),null,2));
  }
}
