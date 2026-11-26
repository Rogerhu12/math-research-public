"use strict";

/* Scalar metric/reference supplier for the complete Cauchy/R137 warm field.
 * Exact definitions use the stated polynomial integrals. Numeric primitives
 * use explicit Gauss quadrature and are not interval certificates. This is a
 * NEW g, not an inherited R208 metric or its fixed-g refinement.
 */
function createCauchyWarmBase(engine,a0,options={}) {
  const c=options.centralLength??13/128,ramp=options.rampLength??.18,
    coast=options.coastLength??.05,L=options.rightLength??.75,v=options.v??.15;
  const rampEnd=c+ramp,coastEnd=rampEnd+coast,end=coastEnd+L;
  const a1=a0+v*ramp/2,f0=a1+v*coast;
  const I2=38251/92378,I3=17141/46189,target=(v-(.8-f0)/L)/(1+v),beta=(target-I2)/(I3-I2);
  if(!(a0>0&&ramp>0&&L>0&&coast>=0&&v>0&&v<1&&beta>=0&&beta<=1))throw Error("Invalid Cauchy warm scalar input");
  const g16=engine.gauss(16),g32=engine.gauss(32);
  function S9(t) {
    if(t<=0)return 0;if(t>=1)return 1;
    const x=Math.min(t,1-t),r=x**5*(126+x*(-420+x*(540+x*(-315+70*x))));
    return t<=.5?r:1-r;
  }
  function scalar(s) {
    if(!(s>=0&&s<=end&&Number.isFinite(s)))throw Error("s outside the new whole half-core interval");
    if(s<=c)return {a:a0,as:0,ass:0};
    if(s<=rampEnd) {
      const t=(s-c)/ramp,J=t**6*(21+t*(-60+t*(67.5+t*(-35+7*t))));
      return {a:a0+v*ramp*J,as:v*S9(t),ass:v/ramp*630*t**4*(1-t)**4};
    }
    if(s<=coastEnd)return {a:a1+v*(s-rampEnd),as:v,ass:0};
    const t=(s-coastEnd)/L,S=S9(t),dq=(2*(1-beta)*S+3*beta*S*S)*630*t**4*(1-t)**4;
    let a,as;
    if(t<=.5) {
      const integ=engine.quad(x=>{const q=S9(x);return (1-beta)*q*q+beta*q**3;},0,t,g16);
      a=f0+L*(v*t-(1+v)*integ);as=v-(1+v)*((1-beta)*S*S+beta*S**3);
    } else {
      function complement(x) {
        const y=1-x,small=y**5*(126+y*(-420+y*(540+y*(-315+70*y)))),q=1-small;
        return small*((1-beta)*(1+q)+beta*(1+q+q*q));
      }
      a=.8+L*(1-t)-L*(1+v)*engine.quad(complement,t,1,g16);
      as=-1+(1+v)*complement(t);
    }
    return {a,as,ass:-(1+v)/L*dq};
  }
  const cuts=[0,c];
  for(let j=1;j<=32;j++)cuts.push(c+ramp*j/32);
  for(let j=1;j<=4;j++)cuts.push(rampEnd+coast*j/4);
  for(let j=1;j<=32;j++)cuts.push(coastEnd+L*j/32);
  const heights=[0];
  function zs(s) {const q=scalar(s);return Math.sqrt(Math.max(0,(1-q.as)*(1+q.as)));}
  for(let j=1;j<cuts.length;j++)heights.push(heights.at(-1)+engine.quad(zs,cuts[j-1],cuts[j],g32));
  function at(s) {
    const q=scalar(s);let lo=0,hi=cuts.length-1;
    while(hi-lo>1){const m=(lo+hi)>>1;if(cuts[m]<=s)lo=m;else hi=m;}
    const z=s===end?heights.at(-1):heights[lo]+engine.quad(zs,cuts[lo],s,g32),z_s=zs(s);
    const z_ss=z_s>0?-q.as*q.ass/z_s:0;
    return {...q,s,z,zs:z_s,zss:s===end?0:z_ss};
  }
  return {a0,centralLength:c,end,height:heights.at(-1),deepCoast:coast,at,scalar,
    segments:cuts.slice(1).map((s1,j)=>({kind:"cauchy_warm_metric_cell",s0:cuts[j],s1,L:s1-cuts[j]})),
    cauchyWarmDesign:{schema:"6a65-complete-Cauchy-R137-warm-new-metric-v1",centralLength:c,rampLength:ramp,
      coastLength:coast,rightLength:L,v,a0,rampEnd,coastEnd,end,beta,fRampEnd:a1,fCoastEnd:f0,fCut:.8,
      trueTailIsSeparateR205:true,roundReferenceHasC2FlatCut:true,physicalMetricChanged:true,
      scalarTurn:"a'=v-(1+v)*((1-beta)*S9(t)^2+beta*S9(t)^3)",
      primitiveQuadrature:{scalarOrder:16,heightOrder:32,continuousRemainderCertified:false}}};
}
module.exports={createCauchyWarmBase};
