/* R201 continuous phase-domain certificate from a completed R197 strong chart.
 * Independent exact rational consumer; no F/J or mean-phase quadrature.
 */
function utf8(s){const a=[];for(const c of s){let n=c.codePointAt(0);if(n<128)a.push(n);else if(n<2048)a.push(192|(n>>6),128|(n&63));else if(n<65536)a.push(224|(n>>12),128|((n>>6)&63),128|(n&63));else a.push(240|(n>>18),128|((n>>12)&63),128|((n>>6)&63),128|(n&63));}return a;}
function sha256(s){const b=utf8(s),bitlen=b.length*8;b.push(128);while(b.length%64!==56)b.push(0);const hi=Math.floor(bitlen/4294967296),lo=bitlen>>>0;for(let k=3;k>=0;k--)b.push((hi>>>(k*8))&255);for(let k=3;k>=0;k--)b.push((lo>>>(k*8))&255);
const K=[1116352408,1899447441,3049323471,3921009573,961987163,1508970993,2453635748,2870763221,3624381080,310598401,607225278,1426881987,1925078388,2162078206,2614888103,3248222580,3835390401,4022224774,264347078,604807628,770255983,1249150122,1555081692,1996064986,2554220882,2821834349,2952996808,3210313671,3336571891,3584528711,113926993,338241895,666307205,773529912,1294757372,1396182291,1695183700,1986661051,2177026350,2456956037,2730485921,2820302411,3259730800,3345764771,3516065817,3600352804,4094571909,275423344,430227734,506948616,659060556,883997877,958139571,1322822218,1537002063,1747873779,1955562222,2024104815,2227730452,2361852424,2428436474,2756734187,3204031479,3329325298],H=[1779033703,3144134277,1013904242,2773480762,1359893119,2600822924,528734635,1541459225];const r=(x,n)=>(x>>>n)|(x<<(32-n));for(let off=0;off<b.length;off+=64){let w=Array(64);for(let i=0;i<16;i++)w[i]=((b[off+4*i]<<24)|(b[off+4*i+1]<<16)|(b[off+4*i+2]<<8)|b[off+4*i+3])>>>0;for(let i=16;i<64;i++){const x=w[i-15],y=w[i-2];w[i]=(w[i-16]+(r(x,7)^r(x,18)^(x>>>3))+w[i-7]+(r(y,17)^r(y,19)^(y>>>10)))>>>0;}let[a,c,d,e,f,g,h,j]=H;for(let i=0;i<64;i++){let t1=(j+(r(f,6)^r(f,11)^r(f,25))+((f&g)^(~f&h))+K[i]+w[i])>>>0,t2=((r(a,2)^r(a,13)^r(a,22))+((a&c)^(a&d)^(c&d)))>>>0;j=h;h=g;g=f;f=(e+t1)>>>0;e=d;d=c;c=a;a=(t1+t2)>>>0;}const v=[a,c,d,e,f,g,h,j];for(let i=0;i<8;i++)H[i]=(H[i]+v[i])>>>0;}return H.map(x=>x.toString(16).padStart(8,'0')).join('');}

"use strict";
function createR201PhaseSectorCertificate(){
  const abs=n=>n<0n?-n:n;
  function gcd(a,b){a=abs(a);b=abs(b);while(b){const r=a%b;a=b;b=r;}return a;}
  function F(n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error("Zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return[n/g,d/g];}
  const add=(a,b)=>F(a[0]*b[1]+b[0]*a[1],a[1]*b[1]),neg=a=>[-a[0],a[1]];
  const sub=(a,b)=>add(a,neg(b)),mul=(a,b)=>F(a[0]*b[0],a[1]*b[1]),div=(a,b)=>F(a[0]*b[1],a[1]*b[0]);
  const cmp=(a,b)=>{const x=a[0]*b[1]-b[0]*a[1];return x<0n?-1:x>0n?1:0;};
  const zero=F(0),one=F(1),sq=a=>mul(a,a),min=(a,b)=>cmp(a,b)<0?a:b,max=(a,b)=>cmp(a,b)>0?a:b;
  function rat(x){if(Array.isArray(x)&&x.length===2)return F(x[0],x[1]);if(typeof x==="string"){const a=x.split("/");return F(a[0],a[1]||"1");}throw Error("Exact rational strings required");}
  function binary64(x){
    if(!Number.isFinite(x))throw Error("Nonfinite coefficient");
    const buf=new ArrayBuffer(8),dv=new DataView(buf);dv.setFloat64(0,x,false);
    const b=(BigInt(dv.getUint32(0,false))<<32n)+BigInt(dv.getUint32(4,false));
    const sign=(b>>63n)?-1n:1n,e=Number((b>>52n)&2047n),m=b&((1n<<52n)-1n);
    if(e===0&&m===0n)return zero;
    const mant=e===0?m:m+(1n<<52n),shift=e===0?-1074:e-1023-52;
    return shift>=0?F(sign*(mant<<BigInt(shift))):F(sign*mant,1n<<BigInt(-shift));
  }
  function out(x){return{exact:x.map(String),display:Number(x[0])/Number(x[1])};}
  function floor(a){return a[0]>=0n?a[0]/a[1]:-((-a[0]+a[1]-1n)/a[1]);}
  function roundGrid(a,bits,up){const Q=1n<<BigInt(bits),v=mul(a,F(Q));return F(up?-floor(neg(v)):floor(v),Q);}
  function sincosPoint(x){
    if(cmp(x,zero)<0||cmp(x,F(8,5))>0)throw Error("Quarter Taylor argument outside certified [0,8/5]");
    const xx=sq(x);let ts=x,tc=one,s=x,c=one,sl,cl;
    for(let k=1;k<=8;k++){
      ts=neg(div(mul(ts,xx),F((2*k)*(2*k+1))));
      tc=neg(div(mul(tc,xx),F((2*k-1)*(2*k))));
      s=add(s,ts);c=add(c,tc);if(k===7){sl=s;cl=c;}
    }
    return {sin:[sl,s],cos:[cl,c]};
  }
  function quarterTrig(lo,hi){
    if(cmp(lo,hi)>0)throw Error("Reversed quarter argument");
    const l=sincosPoint(lo),r=sincosPoint(hi);
    return {sin:[max(zero,l.sin[0]),min(one,r.sin[1])],cos:[max(zero,r.cos[0]),min(one,l.cos[1])]};
  }
  function certifySeed(checkpoint,{expectedCheckpointSHA256,thresholdCos=["23","32"],gridBits=40}={}){
    if(!expectedCheckpointSHA256||sha256(JSON.stringify(checkpoint))!==expectedCheckpointSHA256)throw Error("Actual complete chart SHA mismatch");
    if(checkpoint.schema!=="fd2d-R197-incremental-checkpoint-v1"||!checkpoint.complete||checkpoint.completed_cells!==checkpoint.binding.cells||checkpoint.rows.length!==checkpoint.binding.cells)throw Error("Complete R197 chart required");
    if(checkpoint.binding.construction.source_math_sha256!=="3ccca82923ac0ed4cebcd66cc912944e41565d8e27567e0bd08f684a029ff79f"||
      checkpoint.binding.construction.arithmetic_sha256!=="5c04a135eed859a6d6d583877e53681cdc1dddc6102c913152adfc1913a9f97e")throw Error("Unexpected chart mathematical source");
    const A=rat(checkpoint.binding.axes.A),B=rat(checkpoint.binding.axes.B),D=sub(sq(A),sq(B));
    if(cmp(B,zero)<=0||cmp(D,zero)<0)throw Error("This consumer requires A>=B>0");
    const Qlo=rat(checkpoint.binding.quarter_angle.lower),Qhi=rat(checkpoint.binding.quarter_angle.upper),threshold=rat(thresholdCos);
    if(cmp(threshold,zero)<=0||cmp(threshold,one)>=0)throw Error("Positive cosine threshold below 1 required");
    let minimum=null,witness=null,passed=true;
    const rows=[];
    for(let j=0;j<checkpoint.rows.length;j++){
      const r=checkpoint.rows[j],tl=rat(r.left),tr=rat(r.right);
      if(cmp(tl,F(j,checkpoint.rows.length))!==0||cmp(tr,F(j+1,checkpoint.rows.length))!==0)throw Error("Exact chart partition differs");
      const thl=roundGrid(rat(r.theta_left.lower),gridBits,false),thr=roundGrid(rat(r.theta_right.upper),gridBits,true);
      const ul=roundGrid(mul(Qlo,tl),gridBits,false),ur=roundGrid(mul(Qhi,tr),gridBits,true);
      const th=quarterTrig(thl,thr),u=quarterTrig(ul,ur);
      const numeratorLower=add(mul(A,mul(th.sin[0],u.sin[0])),mul(B,mul(th.cos[0],u.cos[0])));
      const ellSquaredUpper=add(sq(B),mul(D,sq(th.sin[1])));
      const margin=sub(sq(numeratorLower),mul(sq(threshold),ellSquaredUpper));
      const ok=cmp(numeratorLower,zero)>=0&&cmp(margin,zero)>=0;passed=passed&&ok;
      if(minimum===null||cmp(margin,minimum)<0){minimum=margin;witness={cell:j,normalized_interval:[r.left,r.right],
        theta_grid:[thl.map(String),thr.map(String)],material_angle_grid:[ul.map(String),ur.map(String)],
        numerator_lower:out(numeratorLower),ell_squared_upper:out(ellSquaredUpper),squared_margin:out(margin)};}
      rows.push({cell:j,passed:ok,squared_margin:margin.map(String)});
    }
    const Hsquare=sub(F(2),mul(F(2),threshold));
    return {schema:"fd2d-R201-strong-seed-sector-certificate-v1",passed,
      input_checkpoint_sha256:expectedCheckpointSHA256,axes:checkpoint.binding.axes,chart_binding_sha256:checkpoint.binding_sha256,
      method:"Complete saved theta endpoint intervals; outward rational grid; alternating sin/cos polynomials through degrees17/16; squared positive-dot inequality on each whole cell.",
      no_inverse_cell_recomputed:true,grid_bits:gridBits,cells:rows.length,cosine_delta_lower:out(threshold),
      seed_H_squared_upper:out(Hsquare),minimum_squared_margin:out(minimum),minimum_witness:witness,
      row_checks_sha256:sha256(JSON.stringify(rows)),all_row_checks_count:rows.length,
      full_circle_extension:"R197 exact quadrant symmetries preserve cosine_delta and abs(H).",
      scope:"This consumes a proven complete material chart. The row hash is a transport identity, not a replacement for its proof."};
  }
  function certifyState(parameters,layout,seed,{stateIdentity,basisDefinition}={}){
    if(!seed?.passed||cmp(rat(seed.seed_H_squared_upper.exact),F(9,16))>0)throw Error("A paid seed bound |H|<=3/4 is required");
    const {radialBlocks:J,modes:K,phiSinStart,appendedStart,appendedWidth,amplitudeIndex}=layout;
    if(![J,K,phiSinStart,appendedStart,appendedWidth,amplitudeIndex].every(Number.isInteger)||J<1||K<1||appendedWidth!==2*K+1)throw Error("Explicit matching R201 phase layout required");
    if(!basisDefinition||basisDefinition.schema!=="fd2d-R196-shared-simple-cubic-radial-basis-v1"||basisDefinition.degree!==3||basisDefinition.count!==J||basisDefinition.knots.length!==J+4)throw Error("Exact simple cubic basis definition required");
    const knots=basisDefinition.knots.map(rat);for(let j=1;j<knots.length;j++)if(cmp(knots[j-1],knots[j])>=0)throw Error("Strictly increasing exact knots required");
    if(cmp(knots[0],zero)!==0||cmp(knots.at(-1),one)!==0)throw Error("Basis normalized interval must be [0,1]");
    if(phiSinStart<0||phiSinStart+J*K>parameters.length||appendedStart<0||appendedStart+J*appendedWidth>parameters.length||amplitudeIndex<0||amplitudeIndex>=parameters.length)throw Error("Phase indices exceed actual state");
    const amplitude=binary64(parameters[amplitudeIndex]);if(cmp(amplitude,zero)<0||cmp(amplitude,F(6,5))>0)throw Error("Outside actual R205 amplitude definition");
    let M=zero,jmax=0;const rowBounds=[];
    for(let j=0;j<J;j++){
      let sum=zero;
      for(let k=0;k<K;k++){
        const x=binary64(parameters[phiSinStart+j*K+k]),y=binary64(parameters[appendedStart+j*appendedWidth+1+K+k]);
        sum=add(sum,add(F(abs(x[0]),x[1]),F(abs(y[0]),y[1])));
      }
      rowBounds.push({radial_block:j,L1:out(sum)});if(cmp(sum,M)>0){M=sum;jmax=j;}
    }
    const budget=add(amplitude,M),slack=sub(one,budget),sector=add(F(2,5),budget);
    const x=F(7,5),x2=sq(x),cosLower=sub(add(sub(one,div(x2,F(2))),div(sq(x2),F(24))),div(mul(sq(x2),x2),F(720)));
    const sinTwoFifthsLower=sub(F(2,5),div(mul(sq(F(2,5)),F(2,5)),F(6)));
    const passed=cmp(slack,zero)>=0&&cmp(cosLower,F(1,6))>0&&cmp(sinTwoFifthsLower,F(3,8))>0;
    return {schema:"fd2d-R201-complete-radial-phase-sector-state-certificate-v1",passed,state_identity:stateIdentity,
      layout,basis_definition:basisDefinition,seed_certificate_input:seed.input_checkpoint_sha256,seed_row_checks_sha256:seed.row_checks_sha256,
      amplitude:out(amplitude),maximum_phase_control_L1:out(M),maximizing_radial_block:jmax,
      amplitude_plus_maximum_control_L1:out(budget),remaining_budget:out(slack),complete_phase_absolute_upper:out(sector),
      sufficient_condition:"0<=A<=6/5 and A+max_j sum_k(abs(psi_sin[j,k])+abs(psi_cos[j,k]))<=1, with the paid |H_seed|<=3/4 and this actual nonnegative cubic basis.",
      exact_polynomial_checks:{sin_two_fifths_lower:out(sinTwoFifthsLower),cos_seven_fifths_lower:out(cosLower),cos_lower_exceeds_one_sixth:cmp(cosLower,F(1,6))>0},
      continuous_conclusions:passed?{whole_radial_interval:true,whole_material_circle:true,Re_integral_zero_to_pi_exp_i_psi_strict_lower:["1","2"],
        modulus_integral_strict_lower:["1","2"],mean_phase_beta_global_single_branch:"Re Z>0; atan2 has no cut crossing; algebraic normalized phase and its two radial derivatives are C2."}:null,
      row_bounds:rowBounds,
      no_normal_or_BVP_or_new_phase_quadrature:true,
      no_whole_metric_reach_or_strong_motion_claim:true};
  }
  return{certifySeed,certifyState,binary64};
}
if(typeof module!=="undefined"&&module.exports)module.exports={createR201PhaseSectorCertificate};
