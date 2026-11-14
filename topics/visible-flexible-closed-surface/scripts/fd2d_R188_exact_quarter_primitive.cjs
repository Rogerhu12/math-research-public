/* R188 strict quarter-primitive cell consumer.
 * Exact reduced rational + outward dyadic interval arithmetic, no crypto,
 * filesystem, DFT, implicit numerical derivative or OS process required.
 * Taylor packets are bounds on the COMPLETE T channels, not Fourier tails.
 * The included nonlinear analytic fixture is not a repository BVP solution.
 */
"use strict";
function createR188ExactPrimitive(precision=160) {
  const Q=1n<<BigInt(precision);
  const abs=n=>n<0n?-n:n;
  function gcd(a,b){a=abs(a);b=abs(b);while(b){const r=a%b;a=b;b=r;}return a;}
  function F(n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return[n/g,d/g];}
  const add=(a,b)=>F(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
  const neg=a=>[-a[0],a[1]],sub=(a,b)=>add(a,neg(b));
  const mul=(a,b)=>F(a[0]*b[0],a[1]*b[1]),div=(a,b)=>F(a[0]*b[1],a[1]*b[0]);
  const cmp=(a,b)=>{const t=a[0]*b[1]-b[0]*a[1];return t<0n?-1:t>0n?1:0;};
  const zero=F(0),one=F(1),two=F(2);
  function pow(a,n){let out=one;for(let j=0;j<n;j++)out=mul(out,a);return out;}
  function floor(a){return a[0]>=0n?a[0]/a[1]:-((-a[0]+a[1]-1n)/a[1]);}
  const ceil=a=>-floor(neg(a));
  function I(lo,hi=lo){if(cmp(lo,hi)>0)throw Error("reversed interval");return[F(floor(mul(lo,F(Q))),Q),F(ceil(mul(hi,F(Q))),Q)];}
  const ip=a=>I(a),iz=ip(zero),io=ip(one);
  const ia=(a,b)=>I(add(a[0],b[0]),add(a[1],b[1]));
  const ine=a=>I(neg(a[1]),neg(a[0])),is=(a,b)=>ia(a,ine(b));
  function im(a,b){const v=[mul(a[0],b[0]),mul(a[0],b[1]),mul(a[1],b[0]),mul(a[1],b[1])];v.sort(cmp);return I(v[0],v[3]);}
  function id(a,b){if(cmp(b[0],zero)<=0&&cmp(b[1],zero)>=0)throw Error("division by interval containing zero");return im(a,I(div(one,b[1]),div(one,b[0])));}
  const scale=(a,b)=>im(a,ip(b));
  function ipow(a,n){let v=io;for(let j=0;j<n;j++)v=im(v,a);return v;}
  const abmax=a=>cmp(absF(a[0]),absF(a[1]))>=0?absF(a[0]):absF(a[1]);
  function absF(a){return F(abs(a[0]),a[1]);}
  function expand(a,e){if(cmp(e,zero)<0)throw Error("negative error radius");return I(sub(a[0],e),add(a[1],e));}
  function record(a){return{lower:a[0].map(String),upper:a[1].map(String),
    lower_display:Number(a[0][0])/Number(a[0][1]),upper_display:Number(a[1][0])/Number(a[1][1]),
    width:sub(a[1],a[0]).map(String)};}
  function fact(n){let v=1n;for(let j=2;j<=n;j++)v*=BigInt(j);return v;}
  function atanRational(x,n){
    let sum=zero;
    for(let k=0;k<n;k++)sum=add(sum,mul(F(k%2?-1:1,2*k+1),pow(x,2*k+1)));
    const next=div(pow(x,2*n+1),F(2*n+1));
    return n%2?I(sub(sum,next),sum):I(sum,add(sum,next));
  }
  // Machin: pi/4=4 atan(1/5)-atan(1/239), with signed geometric remainders.
  const quarterAngle=scale(is(scale(atanRational(F(1,5),40),F(4)),atanRational(F(1,239),12)),F(2));
  function sincos(x){
    const xx=im(x,x);let ts=x,tc=io,s=iz,c=iz;
    const count=36;
    for(let k=0;k<count;k++){
      s=ia(s,ts);c=ia(c,tc);
      ts=scale(im(ts,xx),F(-1,(2*k+2)*(2*k+3)));
      tc=scale(im(tc,xx),F(-1,(2*k+1)*(2*k+2)));
    }
    const a=abmax(x);
    s=expand(s,div(pow(a,2*count+1),F(fact(2*count+1))));
    c=expand(c,div(pow(a,2*count),F(fact(2*count))));
    return[s,c];
  }
  function ja(a,b){return a.map((x,k)=>ia(x,b[k]));}
  function jn(a){return a.map(ine);}
  function js(a,c){return a.map(x=>scale(x,c));}
  function jm(a,b){return a.map((_,k)=>{let v=iz;for(let j=0;j<=k;j++)v=ia(v,im(a[j],b[k-j]));return v;});}
  function jconst(x,n){return Array.from({length:n},(_,k)=>k?iz:x);}
  function jSinCos(z){
    const n=z.length,[s0,c0]=sincos(z[0]),s=jconst(s0,n),c=jconst(c0,n);
    for(let k=0;k<n-1;k++){
      let sv=iz,cv=iz;
      for(let j=0;j<=k;j++){const dz=scale(z[j+1],F(j+1));sv=ia(sv,im(dz,c[k-j]));cv=ia(cv,im(dz,s[k-j]));}
      s[k+1]=scale(sv,F(1,k+1));c[k+1]=scale(ine(cv),F(1,k+1));
    }
    return[s,c];
  }
  function validatePacket(packet) {
    if(packet.schema!=="fd2d-R188-complete-channel-Taylor-packets-v1")throw Error("wrong Taylor-packet schema");
    if(!packet.definition_binding||packet.derivatives!=="fixed physical s,u")throw Error("explicit complete-function binding and physical derivatives required");
    if(!packet.symmetry_proof||!packet.channels.length)throw Error("explicit R187/R188 symmetry proof required");
    let prev=zero;
    for(const cell of packet.cells){
      if(cmp(cell.left,prev)!==0||cmp(cell.left,cell.right)>=0)throw Error("gap/overlap in quarter partition");
      if(!Number.isInteger(cell.order)||cell.order<1)throw Error("positive Taylor order required");
      for(const name of packet.channels){
        const d=cell.channels[name];
        if(!d||d.coefficients.length!==cell.order||d.remainder.length!==3)throw Error("missing complete channel packet");
        for(const row of d.coefficients)if(row.length!==3)throw Error("need three Cartesian components");
        for(const e of d.remainder)if(cmp(e,zero)<0)throw Error("negative remainder bound");
      }
      prev=cell.right;
    }
    if(cmp(prev,one)!==0)throw Error("quarter coverage incomplete");
  }
  function consume(packet,query){
    validatePacket(packet);
    if(cmp(query,zero)<0||cmp(query,one)>0)throw Error("query outside quarter");
    if(!packet.cells.some(c=>cmp(query,c.left)===0)||cmp(query,one)===0){
      if(cmp(query,one)!==0)throw Error("split the actual Taylor partition at the query first");
    }
    const sums=Object.fromEntries(packet.channels.map(n=>[n,[iz,iz,iz]]));
    let terms=0;
    for(const cell of packet.cells){
      if(cmp(cell.left,query)<0&&cmp(cell.right,query)>0)throw Error("query lies inside an unsplit cell");
      const left=cmp(cell.right,query)<=0,mid=div(add(cell.left,cell.right),two),h=div(sub(cell.right,cell.left),two),n=cell.order;
      for(const name of packet.channels){
        const d=cell.channels[name];
        for(let component=0;component<3;component++){
          let alpha,beta;
          if(component===0){alpha=left?zero:F(-1);beta=zero;}
          else if(component===1){alpha=left?one:zero;beta=zero;}
          else{alpha=left?mid:sub(mid,one);beta=one;}
          if(cmp(alpha,zero)===0&&cmp(beta,zero)===0)continue;
          let poly=iz;
          for(let k=0;k<n;k++){
            const factor=k%2?mul(beta,div(mul(two,pow(h,k+2)),F(k+2))):mul(alpha,div(mul(two,pow(h,k+1)),F(k+1)));
            poly=ia(poly,scale(d.coefficients[k][component],factor));
          }
          // These weights have constant sign on their entire cell.
          const error=mul(mul(absF(alpha),d.remainder[component]),div(mul(two,pow(h,n+1)),F(n+1)));
          sums[name][component]=ia(sums[name][component],expand(poly,error));terms++;
        }
      }
    }
    const answer={};for(const name of packet.channels)answer[name]=sums[name].map(x=>im(quarterAngle,x));
    return {intervals:answer,definition_binding:packet.definition_binding,
      normalized_query:query.map(String),query_angle:"(pi/2)*normalized_query",
      cells:packet.cells.length,channel_count:packet.channels.length,nonzero_weighted_terms:terms,
      exact_zero_mean_identity:"R188 symmetry and Fubini; not a numerical sample mean",
      Taylor_remainders_included:true,complete_T_provider_required:true};
  }
  function analyticFixturePacket(p=F(1,10),q=F(1,20),s=F(1,2),count=16,order=12) {
    // Complete analytic candidate: Theta=u+p*s*sin(2u), Phi=q*s*sin(2u).
    // This fixture binds p,q,s exactly; no numerical isometry is claimed.
    if(cmp(p,F(1,10))!==0||cmp(q,F(1,20))!==0||cmp(s,F(1,2))!==0)
      throw Error("the saved Cauchy bounds are for the explicit fixture only");
    const channels=["T","Ts","Tss","Tp","Tq","Tsp","Tsq"];
    const bounds={T:4,Ts:8,Tss:8,Tp:16,Tq:16,Tsp:64,Tsq:64};
    const A=quarterAngle,cells=[];
    const vz=()=>Array.from({length:order},()=>iz);
    const va=(a,b)=>a.map((x,j)=>ja(x,b[j]));
    const vn=a=>a.map(jn);
    const vm=(a,b)=>a.map(x=>jm(x,b));
    const vs=(a,c)=>a.map(x=>js(x,c));
    for(let cell=0;cell<count;cell++){
      const l=F(cell,count),r=F(cell+1,count),mid=div(add(l,r),two),u0=scale(A,mid);
      const [sn,cs]=sincos(scale(u0,F(2)));
      const sin2=Array.from({length:order},(_,k)=>{
        const cycle=k%4,base=cycle===0?sn:cycle===1?cs:cycle===2?ine(sn):ine(cs);
        return scale(base,F(2n**BigInt(k),fact(k)));
      });
      const theta=js(sin2,mul(p,s));theta[0]=ia(theta[0],u0);theta[1]=ia(theta[1],io);
      const phi=js(sin2,mul(q,s)),[st,ct]=jSinCos(theta),[sp,cp]=jSinCos(phi);
      const T=[jn(jm(st,cp)),jm(ct,cp),sp];
      const Tt=[jn(jm(ct,cp)),jn(jm(st,cp)),vz()];
      const Tf=[jm(st,sp),jn(jm(ct,sp)),cp];
      const Ttt=[jm(st,cp),jn(jm(ct,cp)),vz()];
      const Ttf=[jm(ct,sp),jm(st,sp),vz()];
      const Tff=vn(T),thS=js(sin2,p),phS=js(sin2,q),par=js(sin2,s);
      const Ts=va(vm(Tt,thS),vm(Tf,phS));
      const Tss=va(va(vm(Ttt,jm(thS,thS)),vs(vm(Ttf,jm(thS,phS)),F(2))),vm(Tff,jm(phS,phS)));
      const Tp=vm(Tt,par),Tq=vm(Tf,par);
      const Tsp=va(vm(Tt,sin2),va(vm(Ttt,jm(thS,par)),vm(Ttf,jm(phS,par))));
      const Tsq=va(vm(Tf,sin2),va(vm(Ttf,jm(thS,par)),vm(Tff,jm(phS,par))));
      const fields={T,Ts,Tss,Tp,Tq,Tsp,Tsq},data={};
      for(const name of channels){
        const v=fields[name],coefficients=[];
        for(let k=0;k<order;k++)coefficients.push(v.map(row=>im(row[k],ipow(A,k))));
        const rem=mul(F(bounds[name]),pow(A[1],order));
        data[name]={coefficients,remainder:[rem,rem,rem]};
      }
      cells.push({left:l,right:r,order,channels:data});
    }
    return {
      schema:"fd2d-R188-complete-channel-Taylor-packets-v1",
      definition_binding:{kind:"explicit nonlinear analytic fixture",theta:"u+p*s*sin(2u)",phi:"q*s*sin(2u)",
        p:p.map(String),q:q.map(String),s:s.map(String),complete_trigonometric_composition:true,
        source_problem_is_repository_BVP:false,Cauchy_strip_radius:"1",
        Cauchy_component_bounds:bounds},
      derivatives:"fixed physical s,u",symmetry_proof:"R187 and R188; all raw angle corrections odd and pi-periodic",
      channels,cells
    };
  }
  return {F,add,sub,mul,div,cmp,pow,I,ip,ia,is,im,id,ine,scale,ipow,expand,record,
    sincos,quarterAngle,consume,analyticFixturePacket,precision};
}
function runR188Fixture(){
  const C=createR188ExactPrimitive(),packet=C.analyticFixturePacket(),result=C.consume(packet,C.F(1,4));
  const values={};let width=0;
  for(const [name,v] of Object.entries(result.intervals)){
    values[name]=v.map(C.record);
    for(const x of v){const w=C.sub(x[1],x[0]);width=Math.max(width,Number(w[0])/Number(w[1]));}
  }
  return {schema:"fd2d-R188-actual-strict-nonlinear-quarter-primitive-fixture-v1",
    arithmetic:"outward dyadic interval endpoints computed by exact BigInt operations",
    precision_bits:C.precision,quarter_angle:C.record(C.quarterAngle),
    definition:result.definition_binding,query:result.normalized_query,cells:result.cells,
    Taylor_order:packet.cells[0].order,channels:packet.channels,primitive_intervals:values,
    maximum_interval_width_display:width,all_full_T_and_parameter_channels_integrated:true,
    DFT_used:false,OS_subprocess_started:false,new_BVP_or_actual_main_candidate_claimed:false,
    status:"strict complete-function integrals for this explicit fixture only"};
}
if(typeof module!=="undefined"&&module.exports){
  module.exports={createR188ExactPrimitive,runR188Fixture};
  if(require.main===module)console.log(JSON.stringify(runR188Fixture(),null,2));
}
if(typeof emit==="function")emit(runR188Fixture());
