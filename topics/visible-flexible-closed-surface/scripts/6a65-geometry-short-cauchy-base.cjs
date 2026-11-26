"use strict";
/* Explicit scalar metric/reference for the NEW short Cauchy transplant.
 * It is independent of the long-prefix warm02 factory. Exact defining
 * integrals are retained as rational strings; binary64 Gauss evaluation
 * does not claim an interval remainder bound.
 */
function createShortCauchyWarmBase(engine,a0,options={}) {
  const c=options.centralLength??13/128,ramp=options.rampLength??.06,
    coast=options.coastLength??.02,L=options.rightLength??.75,v=options.v??.05;
  const rampEnd=c+ramp,coastEnd=rampEnd+coast,end=coastEnd+L,a1=a0+v*ramp/2,f0=a1+v*coast;
  const rational=[null,["1","2"],["38251","92378"],["17141","46189"],
    ["376009639","1094020070"],["11451340856","35336848261"],
    ["3307149308705467","10702515099241394"],
    ["46079328383180761","155186468939000213"],
    ["3008062272705324698929883","10483830270076968893338822"]];
  const I=rational.map(x=>x?Number(x[0])/Number(x[1]):null),target=(v-(.8-f0)/L)/(1+v);
  let power=0,beta;
  for(let p=1;p<8;p++)if(I[p+1]<=target&&target<=I[p]){power=p;beta=(target-I[p])/(I[p+1]-I[p]);break;}
  if(!(a0>0&&ramp>0&&coast>=0&&L>0&&v>0&&v<1&&power>0&&beta>=0&&beta<=1))throw Error("Declared adjacent S9 powers cannot pay this scalar metric");
  const g40=engine.gauss(40),g32=engine.gauss(32);
  function S9(t) {
    if(t<=0)return 0;if(t>=1)return 1;
    const x=Math.min(t,1-t),q=x**5*(126+x*(-420+x*(540+x*(-315+70*x))));return t<=.5?q:1-q;
  }
  function complement(x) {
    const y=1-x,small=y**5*(126+y*(-420+y*(540+y*(-315+70*y)))),z=1-small;
    let low=0,high=0,zp=1;
    for(let j=0;j<=power;j++){if(j<power)low+=zp;high+=zp;zp*=z;}
    return small*((1-beta)*low+beta*high);
  }
  function scalar(s) {
    if(!(s>=0&&s<=end&&Number.isFinite(s)))throw Error("s outside the explicit new short half-core");
    if(s<=c)return {a:a0,as:0,ass:0};
    if(s<=rampEnd) {
      const t=(s-c)/ramp,J=t**6*(21+t*(-60+t*(67.5+t*(-35+7*t))));
      return {a:a0+v*ramp*J,as:v*S9(t),ass:v/ramp*630*t**4*(1-t)**4};
    }
    if(s<=coastEnd)return {a:a1+v*(s-rampEnd),as:v,ass:0};
    const t=(s-coastEnd)/L,S=S9(t),qp=((1-beta)*power*S**(power-1)+beta*(power+1)*S**power)*630*t**4*(1-t)**4;
    let a,as;
    if(t<=.5) {
      const integral=engine.quad(x=>{const q=S9(x);return (1-beta)*q**power+beta*q**(power+1);},0,t,g40);
      a=f0+L*(v*t-(1+v)*integral);as=v-(1+v)*((1-beta)*S**power+beta*S**(power+1));
    } else {
      a=.8+L*(1-t)-L*(1+v)*engine.quad(complement,t,1,g40);as=-1+(1+v)*complement(t);
    }
    return {a,as,ass:-(1+v)*qp/L};
  }
  const cuts=[0,c];
  for(let j=1;j<=32;j++)cuts.push(c+ramp*j/32);
  for(let j=1;j<=4;j++)cuts.push(rampEnd+coast*j/4);
  for(let j=1;j<=64;j++)cuts.push(coastEnd+L*j/64);
  const heights=[0];
  const zs=s=>{const q=scalar(s);return Math.sqrt(Math.max(0,(1-q.as)*(1+q.as)));};
  for(let j=1;j<cuts.length;j++)heights.push(heights.at(-1)+engine.quad(zs,cuts[j-1],cuts[j],g32));
  function at(s) {
    const q=scalar(s);let lo=0,hi=cuts.length-1;
    while(hi-lo>1){const mid=(lo+hi)>>1;if(cuts[mid]<=s)lo=mid;else hi=mid;}
    const z=s===end?heights.at(-1):heights[lo]+engine.quad(zs,cuts[lo],s,g32),z_s=zs(s);
    return {...q,s,z,zs:z_s,zss:s===end||z_s===0?0:-q.as*q.ass/z_s};
  }
  return {a0,centralLength:c,end,height:heights.at(-1),deepCoast:coast,at,scalar,
    segments:cuts.slice(1).map((s1,j)=>({kind:"short_cauchy_metric_cell",s0:cuts[j],s1,L:s1-cuts[j]})),
    cauchyWarmDesign:{schema:"6a65-short-Cauchy-R137-strong-transplant-new-metric-v1",centralLength:c,rampLength:ramp,
      coastLength:coast,rightLength:L,v,a0,rampEnd,coastEnd,end,power,beta,targetIntegral:target,
      Ip:rational[power],Ip1:rational[power+1],fRampEnd:a1,fCoastEnd:f0,fCut:.8,
      trueTailIsSeparateR205:true,roundReferenceHasC2FlatCut:true,physicalMetricChanged:true,
      scalarTurn:"a'=v-(1+v)*((1-beta)*S9(t)^power+beta*S9(t)^(power+1))",
      primitiveQuadrature:{scalarOrder:40,heightOrder:32,continuousRemainderCertified:false}}};
}
module.exports={createShortCauchyWarmBase};
