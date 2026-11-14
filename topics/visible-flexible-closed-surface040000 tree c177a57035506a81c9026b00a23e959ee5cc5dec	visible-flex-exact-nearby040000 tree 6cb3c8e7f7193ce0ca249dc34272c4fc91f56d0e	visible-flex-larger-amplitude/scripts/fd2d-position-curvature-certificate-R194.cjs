/* R194: exact rational interval consumers for true principal-curvature caps.
 * All input jet/form enclosures are caller premises on one common physical
 * box. This module neither constructs those enclosures nor proves coverage.
 * No eigengap, floating square root, finite-difference derivative or solver.
 */
"use strict";
function createR194CurvatureCertificate() {
  const abs=x=>x<0n?-x:x;
  function gcd(a,b){a=abs(a);b=abs(b);while(b){const r=a%b;a=b;b=r;}return a;}
  function rat(n,d=1n){
    n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero rational denominator");
    if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return [n/g,d/g];
  }
  const ZERO=rat(0),ONE=rat(1),TWO=rat(2);
  function binary64(x){
    if(!Number.isFinite(x))throw Error("nonfinite rational input");
    if(x===0)return ZERO;
    const v=new DataView(new ArrayBuffer(8));v.setFloat64(0,x,false);
    const hi=v.getUint32(0,false),lo=v.getUint32(4,false),e=(hi>>>20)&2047;
    let m=(BigInt(hi&1048575)<<32n)+BigInt(lo);
    if(e)m+=1n<<52n;if(hi>>>31)m=-m;
    const p=e?e-1075:-1074;
    return p>=0?rat(m<<BigInt(p)):rat(m,1n<<BigInt(-p));
  }
  function R(v){
    if(typeof v==="bigint")return rat(v);
    if(typeof v==="number")return binary64(v);
    if(typeof v==="string"){
      const z=v.split("/");if(z.length>2)throw Error("bad rational string");
      return rat(z[0],z.length===2?z[1]:1);
    }
    if(Array.isArray(v)&&v.length===2)return rat(v[0],v[1]);
    throw Error("a rational must be a string, [numerator,denominator], or actual binary64");
  }
  const cmp=(a,b)=>{const z=a[0]*b[1]-b[0]*a[1];return z<0n?-1:z>0n?1:0;};
  const add=(a,b)=>rat(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
  const neg=a=>[-a[0],a[1]],sub=(a,b)=>add(a,neg(b));
  const mul=(a,b)=>rat(a[0]*b[0],a[1]*b[1]);
  const div=(a,b)=>rat(a[0]*b[1],a[1]*b[0]);
  const min=(a,b)=>cmp(a,b)<0?a:b,max=(a,b)=>cmp(a,b)>0?a:b;
  const rp=a=>a.map(String),sq=a=>mul(a,a);
  function I(v){
    if(v&&typeof v==="object"&&!Array.isArray(v)&&
      (Object.prototype.hasOwnProperty.call(v,"lower")||Object.prototype.hasOwnProperty.call(v,"lo"))){
      const a=R(v.lower===undefined?v.lo:v.lower),b=R(v.upper===undefined?v.hi:v.upper);
      if(cmp(a,b)>0)throw Error("reversed interval");return [a,b];
    }
    const a=R(v);return[a,a];
  }
  const ip=a=>({lower:rp(a[0]),upper:rp(a[1])});
  const ia=(a,b)=>[add(a[0],b[0]),add(a[1],b[1])];
  const ineg=a=>[neg(a[1]),neg(a[0])],isub=(a,b)=>ia(a,ineg(b));
  function imul(a,b){
    const z=[mul(a[0],b[0]),mul(a[0],b[1]),mul(a[1],b[0]),mul(a[1],b[1])];
    return[z.reduce(min),z.reduce(max)];
  }
  function isq(a){
    const u=sq(a[0]),v=sq(a[1]);
    return[cmp(a[0],ZERO)<=0&&cmp(a[1],ZERO)>=0?ZERO:min(u,v),max(u,v)];
  }
  function idiv(a,b){
    if(cmp(b[0],ZERO)<=0&&cmp(b[1],ZERO)>=0)throw Error("division interval contains zero");
    return imul(a,[div(ONE,b[1]),div(ONE,b[0])]);
  }
  function intersect(a,b){
    const c=[max(a[0],b[0]),min(a[1],b[1])];
    if(cmp(c[0],c[1])>0)throw Error("inconsistent certified interval intersection");return c;
  }
  const iz=I("0"),io=I("1"),it=I("2");
  const isum=v=>v.reduce(ia,iz);
  function vec(v,name){
    if(!Array.isArray(v)||v.length!==3)throw Error("three components required for "+name);
    return v.map(I);
  }
  const dot=(a,b)=>isum(a.map((x,i)=>imul(x,b[i])));
  const norm2=a=>isum(a.map(isq));
  const cross=(a,b)=>[
    isub(imul(a[1],b[2]),imul(a[2],b[1])),
    isub(imul(a[2],b[0]),imul(a[0],b[2])),
    isub(imul(a[0],b[1]),imul(a[1],b[0]))
  ];
  function canonical(x){
    if(x===null||typeof x!=="object")return JSON.stringify(x);
    if(Array.isArray(x))return"["+x.map(canonical).join(",")+"]";
    return"{"+Object.keys(x).sort().map(k=>JSON.stringify(k)+":"+canonical(x[k])).join(",")+"}";
  }
  function meta(packet,kind,cap){
    const allowed=["certified common continuous physical box","certified single physical point","conditional interval fixture"];
    if(!packet||!allowed.includes(packet.scope))throw Error("explicit certified-box, certified-point, or conditional-fixture scope required");
    if(!packet.bindings||!packet.bindings.geometry_definition||!packet.bindings.domain||!packet.bindings.enclosure_evidence)
      throw Error("geometry, common domain and enclosure-evidence bindings required");
    const c=R(cap);if(cmp(c,ZERO)<0)throw Error("negative curvature cap");
    return {c,out:{schema:"fd2d-R194-exact-interval-curvature-certificate-v1",kind,scope:packet.scope,
      bindings:packet.bindings,curvature_cap:rp(c),arithmetic:"exact BigInt rational interval arithmetic",
      passed:false,strict_cap_proved:false,immersion_proved:false,
      pointwise_algebra_is_equivalent:true,interval_pass_is_sufficient_only:true,
      supplied_enclosures_are_premises:true,coverage_proved_here:false,
      repository_main_candidate_certified:false}};
  }
  function finish(out,immersion,margins,extras){
    const failed=Object.keys(margins).filter(k=>cmp(margins[k][0],ZERO)<0);
    out.immersion_proved=immersion;
    out.margins=Object.fromEntries(Object.entries(margins).map(([k,v])=>[k,ip(v)]));
    Object.assign(out,extras);
    out.passed=immersion&&failed.length===0;
    out.strict_cap_proved=out.passed&&Object.values(margins).every(v=>cmp(v[0],ZERO)>0);
    out.status=out.passed?"proved under the stated enclosure premises":"unresolved by these intervals";
    out.unresolved_quantities=immersion?failed:["immersion",...failed];
    out.continuous_box_conclusion=out.passed&&out.scope==="certified common continuous physical box";
    out.failure_is_not_geometric_nonexistence=true;return out;
  }
  function polynomial(out,c,E,F,G,D,B){
    const [b11,b12,b22]=B,ci=[c,c],c2=[sq(c),sq(c)];
    const detB=isub(imul(b11,b22),isq(b12));
    const mixed=isub(ia(imul(E,b22),imul(G,b11)),imul(it,imul(F,b12)));
    // det( C sqrt(D) I +/- B ) = L +/- C sqrt(D) mixed.
    // det(I)=D is an exact geometric identity, applied before interval arithmetic.
    const L=ia(imul(c2,isq(D)),detB);
    const margins={
      diagonal_11:isub(imul(c2,imul(D,isq(E))),isq(b11)),
      diagonal_22:isub(imul(c2,imul(D,isq(G))),isq(b22)),
      determinant_center:L,
      determinant_squared:isub(isq(L),imul(c2,imul(D,isq(mixed))))
    };
    return finish(out,cmp(D[0],ZERO)>0,margins,{
      Gram:{E:ip(E),F:ip(F),G:ip(G)},squared_cross_norm:ip(D),
      unnormalized_second_form:{B11:ip(b11),B12:ip(b12),B22:ip(b22)},
      determinant_B:ip(detB),determinant_mixed:ip(mixed),
      square_root_evaluation_used:false});
  }
  function certifyCartesianJetBox(packet,cap){
    const {c,out}=meta(packet,"Cartesian physical two-jet box",cap);
    if(packet.derivatives!=="fixed physical s,u")throw Error("physical s,u derivative declaration required");
    const j=packet.jets,U=vec(j.Xs,"Xs"),V=vec(j.Xu,"Xu");
    const A=vec(j.Xss,"Xss"),B=vec(j.Xsu,"Xsu"),C=vec(j.Xuu,"Xuu");
    const W=cross(U,V),D=norm2(W);
    out.derivatives=packet.derivatives;
    return polynomial(out,c,norm2(U),dot(U,V),norm2(V),D,[dot(W,A),dot(W,B),dot(W,C)]);
  }
  function certifyUnitTangentJetBox(packet,cap){
    const {c,out}=meta(packet,"unit-tangent normalized physical two-jet box",cap);
    if(packet.derivatives!=="fixed physical s,u"||packet.exact_unit_tangent!==true||
      packet.exact_position_identity!=="X_u=a T; X_s=V")
      throw Error("exact unit-tangent/position identities and physical derivatives required");
    const j=packet.jets,a=I(j.a);
    if(cmp(a[0],ZERO)<=0)throw Error("strictly positive radius enclosure required");
    const V=vec(j.V,"V"),T=vec(j.T,"T"),Ts=vec(j.Ts,"Ts"),Tu=vec(j.Tu,"Tu"),A=vec(j.Xss,"Xss");
    const W=cross(V,T),E=norm2(V),F=dot(V,T);
    // Both enclose the same D, because the complete T has norm exactly one.
    const D=intersect(norm2(W),isub(E,isq(F)));
    out.derivatives=packet.derivatives;
    out.exact_cancellations=["|T|^2=1","N dot (a_s T/a+T_s)=N dot T_s","det H=|V cross T|^2"];
    return polynomial(out,c,E,F,io,D,[dot(W,A),dot(W,Ts),idiv(dot(W,Tu),a)]);
  }
  function certifyFormBox(packet,cap){
    const {c,out}=meta(packet,"normalized Gram and second-form box",cap);
    if(!Array.isArray(packet.H)||packet.H.length!==3||!Array.isArray(packet.Q)||packet.Q.length!==3)
      throw Error("symmetric H and Q triples [11,12,22] required");
    const [E,F,G]=packet.H.map(I),[L,M,N]=packet.Q.map(I),ci=[c,c],c2=[sq(c),sq(c)];
    let detH=isub(imul(E,G),isq(F));
    if(packet.detH!==undefined)detH=intersect(detH,I(packet.detH));
    const detQ=isub(imul(L,N),isq(M));
    const center=ia(imul(c2,detH),detQ);
    const mixed=isub(ia(imul(E,N),imul(G,L)),imul(it,imul(F,M)));
    const margins={
      plus_11:ia(imul(ci,E),L),minus_11:isub(imul(ci,E),L),
      plus_22:ia(imul(ci,G),N),minus_22:isub(imul(ci,G),N),
      plus_determinant:ia(center,imul(ci,mixed)),
      minus_determinant:isub(center,imul(ci,mixed))
    };
    return finish(out,cmp(E[0],ZERO)>0&&cmp(detH[0],ZERO)>0,margins,{
      H:[E,F,G].map(ip),Q:[L,M,N].map(ip),determinant_H:ip(detH),determinant_Q:ip(detQ),
      determinant_center:ip(center),determinant_mixed:ip(mixed),square_root_evaluation_used:false});
  }
  function fromR193Budget(budget,reference,cap){
    if(!budget||budget.schema!=="fd2d-R193-direct-position-box-budget-output-v1"||
      budget.all_bounds_exact_rational_or_outward_dyadic!==true||!budget.second_form_error)
      throw Error("a complete R193 exact budget with second-form errors is required");
    if(!reference||reference.scope!==budget.scope||
      canonical(reference.expected_budget_bindings)!==canonical(budget.bindings))
      throw Error("reference Q0 must explicitly bind the same R193 identities and scope");
    if(reference.Q0_definition!=="N0 dot [Xss0,Ts0,Tu0/a0]"||!reference.Q0_evidence||!reference.domain)
      throw Error("certified same-box reference Q0, definition and evidence required");
    if(!Array.isArray(reference.Q0)||reference.Q0.length!==3)throw Error("three reference Q0 intervals required");
    const errs=["L","M","N"].map(k=>{
      const e=R(budget.second_form_error[k].exact);if(cmp(e,ZERO)<0)throw Error("negative R193 error");return e;
    });
    const q=reference.Q0.map((x,i)=>ia(I(x),[neg(errs[i]),errs[i]]));
    const e=ia(io,I(budget.accurate_residuals.rE)),f=I(budget.accurate_residuals.rF);
    let dh=isub(e,isq(f));
    if(budget.Gram_determinant_lower){
      const lower=R(budget.Gram_determinant_lower.exact);dh=intersect(dh,[lower,dh[1]]);
    }
    const packet={scope:budget.scope,bindings:{
      geometry_definition:{R193_bindings:budget.bindings,Q0_definition:reference.Q0_definition},
      domain:reference.domain,enclosure_evidence:{R193_budget:reference.budget_evidence||{schema:budget.schema},
        reference_Q0:reference.Q0_evidence,expected_budget_bindings:reference.expected_budget_bindings}
    },H:[ip(e),ip(f),ip(io)],Q:q.map(ip),detH:ip(dh)};
    const out=certifyFormBox(packet,cap);
    out.adapter="R193 exact metric intervals and componentwise second-form errors";
    out.reference_Q0=reference.Q0;out.added_Q_errors=errs.map(rp);
    out.sampled_or_formal_curvature_used_as_Q0_bound=false;return out;
  }
  return {certifyCartesianJetBox,certifyUnitTangentJetBox,certifyFormBox,fromR193Budget};
}
if(typeof module!=="undefined"&&module.exports)module.exports={createR194CurvatureCertificate};
