"use strict";
/* R199 orientation consumer reconstructed after the fifth environment loss.
   This source has its own identity. It is not the unavailable 4991-byte source.
   It transports complete position two-jets of one fixed actual core map.
   It does not construct caps, certify reach, or turn finite residual into zero. */
const KEYS=["X","Xs","Xu","Xss","Xsu","Xuu"];
function check3(a,name){if(!a||a.length!==3||Array.from(a).some(x=>!Number.isFinite(x)))throw Error("Expected finite3-vector "+name);return Array.from(a);}
function rot(a,angle){const c=Math.cos(angle),s=Math.sin(angle);return[c*a[0]-s*a[1],s*a[0]+c*a[1],a[2]];}
function omega(a){return[-a[1],a[0],0];}
function add(a,b){return a.map((x,i)=>x+b[i]);}
function sub(a,b){return a.map((x,i)=>x-b[i]);}
function scale(a,c){return a.map(x=>x*c);}
function dot(a,b){return a.reduce((x,v,i)=>x+v*b[i],0);}
function cross(a,b){return[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]];}
function transportTwoJet(base,angle,{angularVelocity=2*Math.PI/3,angularAcceleration=0}={}){
 if(![angle,angularVelocity,angularAcceleration].every(Number.isFinite))throw Error("Nonfinite orientation law");
 const f=Object.fromEntries(KEYS.map(k=>[k,rot(check3(base[k],k),angle)]));
 const gen=sub(omega(f.X),f.Xu);
 f.Xt=scale(gen,angularVelocity);
 f.Xst=scale(sub(omega(f.Xs),f.Xsu),angularVelocity);
 f.Xut=scale(sub(omega(f.Xu),f.Xuu),angularVelocity);
 f.Xtt=add(scale(add(sub(omega(omega(f.X)),scale(omega(f.Xu),2)),f.Xuu),angularVelocity*angularVelocity),scale(gen,angularAcceleration));
 return f;
}
function createOrientationOrbit(baseEvaluate,{fixedParameters,angularVelocity=2*Math.PI/3,angleOrigin=0}={}){
 if(typeof baseEvaluate!=="function")throw Error("baseEvaluate must supply full canonical spatial twojet");
 // No parameter is chosen as a function of t by this factory.
 const p=Array.isArray(fixedParameters)||ArrayBuffer.isView(fixedParameters)?Array.from(fixedParameters):fixedParameters;
 return{
  definition:{schema:"fd2d-R199-fixed-map-orientation-orbit-recovery-v1",formula:"R_alpha Y(s,u-alpha); alpha=angleOrigin+angularVelocity*t",angularVelocity,angleOrigin,time_is_orientation_not_gap:true,metric_fixed_if_the_input_radial_metric_and_all_map_parameters_are_fixed:true,caps_are_separate_fixed_surfaces:true,new_metric_or_global_reach_certificate:false},
  evaluate(s,u,t){const alpha=angleOrigin+angularVelocity*t;return transportTwoJet(baseEvaluate(s,u-alpha,p),alpha,{angularVelocity});}
 };
}
function localGeometry(j){
 const E=dot(j.Xs,j.Xs),F=dot(j.Xs,j.Xu),G=dot(j.Xu,j.Xu),D=E*G-F*F;
 if(!(D>0))throw Error("Input is not a sampled immersion");
 const normal=scale(cross(j.Xs,j.Xu),1/Math.sqrt(D));
 const e=dot(normal,j.Xss),f=dot(normal,j.Xsu),g=dot(normal,j.Xuu);
 const trace=(G*e-2*F*f+E*g)/D,det=(e*g-f*f)/D,disc=Math.max(0,trace*trace-4*det);
 return{firstForm:[E,F,G],secondForm:[e,f,g],normal,principalCurvatures:[(trace-Math.sqrt(disc))/2,(trace+Math.sqrt(disc))/2]};
}
module.exports={transportTwoJet,createOrientationOrbit,localGeometry};
