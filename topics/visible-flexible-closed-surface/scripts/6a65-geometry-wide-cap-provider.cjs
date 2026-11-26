"use strict";
/* R215 changes the actual complete cap geometry. The finite guide consumes
 * its conservative interior thresholds; zero sampled penalty is not a
 * continuous certificate. All position columns are inherited from R210. */
function createR215WideCapGeometryProvider(positionProvider,options={}) {
  const geometryOptions={radius:1.59,width:.885,held:.65,
    weight:options.weight===undefined?10:options.weight,
    nodeShare:options.nodeShare===undefined?.5:options.nodeShare,
    cutWindow:[.51,.60],heightAllowance:{maximum:.0195,radialStart:.52,radialEnd:.54}};
  if(!(positionProvider.definition.parentMetric.centralA>=1.4))
    throw Error("R215 requires actual central support at least 1.4; exact seed proof remains separate");
  const p=require("./fd2d-R210-amplitude-height-allowance-geometric-guide.cjs")
    .createR210AmplitudeGeometryProvider(positionProvider,geometryOptions);
  const completeCap={schema:"6a65-R215-wider-core-complete-fixed-caps-v1",
    exactParameters:{B:"1.6",R:".097",a:".30",cuffRadius:".32",lambda:".01",
      epsilon:".0001",smoothingRadius:".000001",throatExtension:".02",
      cornerX:".694",cornerY:"1.056",cornerHeight:".925",topHeight:"1.55"},
    exactRequiredCore:{centralSupportAtLeast:"1.4",actualCuffHeightWindow:[".50",".61"],
      ballRadius:"1.6",phaseZeroHalfWidth:".895",heldExclusionRadius:".64",
      reachAtLeast:".097",heightAllowance:".02",overheightCylindricalRadiusAtLeast:".514"},
    guaranteedBoundsConditionalOnCompleteCore:{diameterAtMost:"3.2",heldAtLeast:".64",
      allE3HausdorffAtLeast:".1609",reachAtLeast:".097"},
    allCompleteCoreMetricAndNonlocalReachRemainInputs:true,
    finiteGuideZeroNotContinuousCertificate:true};
  return {...p,r215GeometryOptions:geometryOptions,
    definition:{...p.definition,geometryFamilySchema:"6a65-R215-wider-core-height-allowance-guide-v1",
      geometry:{...p.definition.geometry,completeCap,
        objectiveTransition:"New actual R215 caps; original R204 width target is not reused",
        allParameterDerivatives:"Unchanged complete R210 position/cut/amplitude/radius chain"}}};
}
module.exports={createR215WideCapGeometryProvider};
