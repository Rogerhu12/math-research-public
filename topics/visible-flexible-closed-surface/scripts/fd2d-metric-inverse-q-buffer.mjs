/**
 * A finite inverse-Q buffer, defined by positive Bernstein coefficients.
 *
 * Mathematical definition: r=a+(b-a)t, Q_t=t(1-t)k(t),
 * Q(0)=-a^2/(12(b-a)^2), (log w_raw)_t=-P/(r^2 k), where
 * r^2 Q_tt+8(b-a)r Q_t+12(b-a)^2 Q=t(1-t)P.
 * The optional exact endpoint calibration is w=w_raw exp(c S5(t)).
 *
 * This module is a floating evaluator of that integral definition.  Its
 * Gauss quadrature and displayed maxima are NOT interval certificates.
 * Recompute the actual new linear/nonlinear tail after any calibration.
 * Original source files and profiles are not modified.
 */

function choose(n,k) {
  if (k<0 || k>n) return 0;
  k=Math.min(k,n-k); let v=1;
  for(let j=1;j<=k;j++)v*= (n-k+j)/j;
  return v;
}
function multiply(a,b) {
  const n=a.length-1,m=b.length-1,c=new Float64Array(n+m+1);
  for(let i=0;i<=n;i++)for(let j=0;j<=m;j++)
    c[i+j]+=a[i]*b[j]*choose(n,i)*choose(m,j)/choose(n+m,i+j);
  return c;
}
function derivative(a) {
  const n=a.length-1,b=new Float64Array(n);
  for(let j=0;j<n;j++)b[j]=n*(a[j+1]-a[j]);
  return b;
}
function value(a,t) {
  const b=Float64Array.from(a);
  for(let n=b.length-1;n>0;n--)for(let j=0;j<n;j++)b[j]=(1-t)*b[j]+t*b[j+1];
  return b[0];
}

// Positive half of 16-point Gauss--Legendre; the other half is reflected.
const GX=[.095012509837637440185,.28160355077925891323,.45801677765722738634,
  .61787624440264374845,.75540440835500303390,.86563120238783174388,
  .94457502307323257608,.98940093499164993260];
const GW=[.18945061045506849629,.18260341504492358887,.16915651939500253819,
  .14959598881657673208,.12462897125553387205,.095158511682492784810,
  .062253523938647892863,.027152459411754094852];
function integrate16(f,a,b) {
  if(a===b)return 0;
  const c=(a+b)/2,h=(b-a)/2;let v=0;
  for(let j=0;j<8;j++)v+=GW[j]*(f(c-h*GX[j])+f(c+h*GX[j]));
  return h*v;
}
const S5=t=>t*t*t*(10+t*(-15+6*t));
const S5p=t=>30*t*t*(1-t)*(1-t);
const S5pp=t=>60*t*(1-t)*(1-2*t);

/**
 * definition may be the complete candidate JSON or the plain object:
 * {left,right,w0,wr0,outer_w,outer_logarithmic_radial_derivative,
 *  degree,kap,positive_interior_weights}.
 *
 * Pass an actual source-port override in options.port if the calling
 * physical factory evaluates the same exact source port more accurately.
 * Such overrides must be recorded by the caller's new-profile manifest.
 */
export function createInverseQBuffer(definition,options={}) {
  const record=definition.exact_definition;
  const p={...(definition.numerical_port??definition),...(options.port??{})};
  const degree=record?.degree??definition.degree;
  const kap=record?.kap_binary??definition.kap;
  const weights=record?.positive_interior_weights_binary??definition.positive_interior_weights;
  const a=p.left,b=p.right,L=b-a,w0=p.w0,w1=p.outer_w;
  const s0=p.wr0/w0,s1=p.outer_logarithmic_radial_derivative;
  if(!(a>0&&L>0&&w0>0&&w1>0&&kap>0&&degree>=4&&weights.length===degree-3))
    throw new Error('Invalid positive inverse-Q definition');
  if(!weights.every(v=>Number.isFinite(v)&&v>0))throw new Error('Interior weights must be positive');
  const k=new Float64Array(degree+1),moment=new Float64Array(degree+1);
  const d0=1-L*(10/a+s0)/2,d1=-kap*(1+L*(10/b+s1)/2);
  k[0]=1;k[1]=1+d0/degree;k[degree]=kap;k[degree-1]=kap-d1/degree;
  for(let j=0;j<=degree;j++)moment[j]=(j+1)*(degree-j+1)/((degree+1)*(degree+2)*(degree+3));
  const target=(a*a+b*b*kap)/(12*L*L);
  let fixed=0,den=0;
  for(const j of [0,1,degree-1,degree])fixed+=moment[j]*k[j];
  for(let j=2;j<degree-1;j++)den+=moment[j]*weights[j-2];
  const remaining=target-fixed;
  if(!(remaining>0&&den>0&&k[1]>0&&k[degree-1]>0))throw new Error('Positive moment normalization is unavailable');
  for(let j=2;j<degree-1;j++)k[j]=remaining*weights[j-2]/den;
  const qt=new Float64Array(degree+3);
  for(let j=0;j<=degree;j++)qt[j+1]=k[j]*(j+1)*(degree-j+1)/((degree+1)*(degree+2));
  const Q=new Float64Array(degree+4);Q[0]=-a*a/(12*L*L);
  for(let j=1;j<Q.length;j++)Q[j]=Q[j-1]+qt[j-1]/(degree+3);
  const qtt=derivative(qt),term1=multiply([a*a,a*b,b*b],qtt),term2=multiply([a,b],qt);
  const F=Float64Array.from(term1,(v,j)=>v+8*L*term2[j]+12*L*L*Q[j]);
  const D=degree+3,P=new Float64Array(degree+2);
  for(let j=1;j<D;j++)P[j-1]=F[j]*D*(D-1)/(j*(D-j));
  const kp=derivative(k),Pp=derivative(P);
  function rawLogJet(t) {
    const r=a+L*t,kv=value(k,t),pv=value(P,t),kvp=value(kp,t),pvp=value(Pp,t);
    const den=r*r*kv,denp=2*L*r*kv+r*r*kvp;
    return [-pv/den,-pvp/den+pv*denp/(den*den)];
  }
  const grid=options.grid??1024;
  if(!(Number.isInteger(grid)&&grid>0))throw new Error('Quadrature grid must be a positive integer');
  const primitive=new Float64Array(grid+1);
  for(let j=0;j<grid;j++)primitive[j+1]=primitive[j]+integrate16(t=>rawLogJet(t)[0],j/grid,(j+1)/grid);
  const rawLogRatio=primitive[grid],c=options.calibrate===false?0:Math.log(w1/w0)-rawLogRatio;
  const scale=12*L*L/(Math.pow(b,6)*kap);
  function logPrimitive(t) {
    if(t===1)return rawLogRatio;
    if(t===0)return 0;
    const j=Math.min(grid-1,Math.floor(t*grid));
    return primitive[j]+integrate16(v=>rawLogJet(v)[0],j/grid,t);
  }
  function evaluate(t) {
    if(!(t>=0&&t<=1&&Number.isFinite(t)))throw new RangeError('Inverse-Q coordinate must lie in [0,1]');
    const r=a+L*t,[raw1,raw2]=rawLogJet(t);
    const logw=Math.log(w0)+logPrimitive(t)+c*S5(t);
    const logwx=raw1+c*S5p(t),logwxx=raw2+c*S5pp(t),w=Math.exp(logw);
    const wx=w*logwx,wxx=w*(logwx*logwx+logwxx);
    const q=value(Q,t),q1=value(qt,t),pp=value(P,t);
    const H=scale*Math.pow(r,4)*q,J=scale*Math.pow(r,4)*q1/L;
    const Hr=4*H/r+J,Hrr=scale*r*r*t*(1-t)*pp/(L*L);
    const E=1+w*w,rootE=Math.sqrt(E),dl=-Hrr/rootE,dn=-rootE*J/r,dm=2*H/(r*r)-2*Hr/r;
    return {r,drdx:L,d2rdx2:0,w,wx,wxx,wr:wx/L,wrr:wxx/(L*L),E,
      logw,logwx,logwxx,logwr:logwx/L,
      referenceH:H,referenceHr:Hr,referenceHrr:Hrr,referenceJ:J,
      referenceLinearEquationDefect:c*S5p(t)*J/L,
      referenceGamma:J/w-4*H*w/r,
      referenceIIRow:Math.max(Math.abs(dl)+Math.abs(dm),Math.abs(dn)+Math.abs(dm)),
      backgroundMeridionalCurvature:wx/(L*Math.pow(E,1.5)),
      backgroundCircularCurvature:w/(r*rootE)};
  }
  return {evaluate,rawLogJet,logPrimitive,coefficients:{k:Array.from(k),Q:Array.from(Q),P:Array.from(P)},
    metadata:{kind:'finite_inverse_q_buffer',degree,left:a,right:b,innerW:w0,outerWTarget:w1,
      innerLogarithmicDerivative:s0,outerLogarithmicDerivative:s1,
      gamma:Math.pow(a/b,6)/kap,rawLogRatio,endpointCalibration:c,quadratureGrid:grid,
      exactDefinition:'positive-k weighted moment; rational log derivative primitive; S5 endpoint calibration',
      numericalOnly:true,originalPolynomialSolvesCalibratedEquation:c===0}};
}

