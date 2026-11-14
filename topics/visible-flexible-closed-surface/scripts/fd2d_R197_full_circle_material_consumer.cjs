/* Full-circle physical-material consumer for an actually complete R197 quarter.
 * This is exact reflection of certified intervals, not a trigonometric
 * interpolation and not a claim that the finite seed is unchanged.
 * All rational inputs are string pairs. No OS or numerical finite difference.
 */
"use strict";
function createR197FullCircleMaterialConsumer(chart,target) {
  if(!chart||typeof chart.progress!=="function"||!chart.progress().complete)
    throw Error("An actual complete strict quarter is required");
  if(!target||!target.exact_interval||!target.identity)
    throw Error("Explicit accurate target-a0 interval and source identity required");
  const C=chart.arithmetic;
  const {F,add,sub,mul,cmp,I,ip,ia,ine,im,scale,record}=C;
  const z=F(0),one=F(1),four=F(4),Q=C.quarterAngle;
  function rat(v){if(Array.isArray(v)&&v.length===2)return F(v[0],v[1]);if(typeof v==="string"){const a=v.split("/");return F(a[0],a[1]||"1");}throw Error("Exact rational pair/string required");}
  function decode(v){if(!v||!v.lower||!v.upper)throw Error("Exact interval record required");return I(rat(v.lower),rat(v.upper));}
  const a0=decode(target.exact_interval);
  if(cmp(a0[0],z)<=0)throw Error("Strictly positive accurate a0 required");
  function signed(x,s){return s===1?x:ine(x);}
  function shift(x,n){return ia(scale(Q,F(n)),x);}
  function intervalHull(a,b){return I(cmp(a[0],b[0])<0?a[0]:b[0],cmp(a[1],b[1])>0?a[1]:b[1]);}
  const diagonals=[[1,1],[-1,1],[-1,-1],[1,-1]];
  function quadrantPacket(q,left,right) {
    const odd=q%2===1,sgn=odd?-1:1;
    const localLeft=odd?sub(F(q+1),right):sub(left,F(q));
    const localRight=odd?sub(F(q+1),left):sub(right,F(q));
    const L=localLeft.map(String),R=localRight.map(String);
    const p=chart.geometricSeedBox(L,R),m=chart.materialJetBox(L,R,2);
    const diag=diagonals[q];
    const curve=p.normalized_curve.map((v,j)=>signed(decode(v),diag[j]));
    const tangent=p.unit_tangent.map((v,j)=>signed(decode(v),sgn*diag[j]));
    const tangentU=p.unit_tangent_u.map((v,j)=>signed(decode(v),diag[j]));
    const tangentUU=p.unit_tangent_uu.map((v,j)=>signed(decode(v),sgn*diag[j]));
    const theta=shift(signed(decode(p.theta),sgn),odd?q+1:q);
    const thetaU=decode(m.jets.theta[1]);
    const thetaUU=signed(scale(decode(m.jets.theta[2]),F(2)),sgn);
    const beta=decode(p.tangent_turn_rate),betaU=signed(decode(p.tangent_turn_rate_u),sgn);
    const h=signed(decode(p.h),sgn),hU=decode(p.h_u),hUU=signed(decode(p.h_uu),sgn);
    return {
      quadrant:q,normalized_left:left.map(String),normalized_right:right.map(String),
      reflected_quarter_left:L,reflected_quarter_right:R,
      coordinate:"u=(pi/2)*normalized angle; all displayed derivatives below are actual physical-u derivatives",
      enclosures:{
        u:record(im(Q,I(left,right))),
        theta:record(theta),theta_u:record(thetaU),theta_uu:record(thetaUU),
        normalized_curve:curve.map(record),
        normalized_curve_u:tangent.map(record),
        normalized_curve_uu:tangentU.map(record),
        normalized_curve_uuu:tangentUU.map(record),
        physical_curve:curve.map(v=>record(im(a0,v))),
        physical_curve_u:tangent.map(v=>record(im(a0,v))),
        physical_curve_uu:tangentU.map(v=>record(im(a0,v))),
        physical_curve_uuu:tangentUU.map(v=>record(im(a0,v))),
        unit_tangent:tangent.map(record),unit_tangent_u:tangentU.map(record),unit_tangent_uu:tangentUU.map(record),
        tangent_turn_rate:record(beta),tangent_turn_rate_u:record(betaU),
        physical_curvature:record(C.id(beta,a0)),
        h:record(h),h_u:record(hU),h_uu:record(hUU),
        cosine_delta:p.cosine_delta,sine_delta:record(signed(decode(p.sine_delta),sgn))
      },
      safe_seed_horizontal_norm_squared_lower:["1","2"]
    };
  }
  function combine(a,b){
    if(Array.isArray(a))return a.map((x,i)=>combine(x,b[i]));
    return record(intervalHull(decode(a),decode(b)));
  }
  function box(left,right=left){
    left=rat(left);right=rat(right);
    if(cmp(left,z)<0||cmp(right,four)>0||cmp(left,right)>0)throw Error("Full-circle normalized query must lie in [0,4]");
    const parts=[];
    if(cmp(left,right)===0){
      let q=Number(left[0]/left[1]);if(q===4)q=3;
      parts.push(quadrantPacket(q,left,right));
    }else for(let q=0;q<4;q++){
      const l=cmp(left,F(q))>0?left:F(q),r=cmp(right,F(q+1))<0?right:F(q+1);
      if(cmp(l,r)<0)parts.push(quadrantPacket(q,l,r));
    }
    if(!parts.length)throw Error("No quadrant covers the query");
    const e={};
    for(const key of Object.keys(parts[0].enclosures)){
      let v=parts[0].enclosures[key];
      for(let j=1;j<parts.length;j++)v=combine(v,parts[j].enclosures[key]);
      e[key]=v;
    }
    return {schema:"fd2d-R197-accurate-full-circle-material-twojet-box-v1",
      normalized_query:{left:left.map(String),right:right.map(String)},
      pieces:parts,enclosures:e,definition:definition()};
  }
  function definition(){
    return {schema:"fd2d-R197-accurate-full-circle-material-consumer-definition-v1",
      quarter:chart.definition(),quarter_binding_sha256:chart.progress().binding_sha256,
      target_mean_radius:target,
      full_chart:[
        {interval:["0","1"],local:"t",theta:"theta_q(t)",position_diagonal:[1,1],local_derivative_sign:1},
        {interval:["1","2"],local:"2-t",theta:"pi-theta_q(2-t)",position_diagonal:[-1,1],local_derivative_sign:-1},
        {interval:["2","3"],local:"t-2",theta:"pi+theta_q(t-2)",position_diagonal:[-1,-1],local_derivative_sign:1},
        {interval:["3","4"],local:"4-t",theta:"2*pi-theta_q(4-t)",position_diagonal:[1,-1],local_derivative_sign:-1}],
      physical_curve:"(a0/a_E)*(A*cos(theta(u)), B*sin(theta(u)))",
      actual_derivatives_not_factorial_coefficients:true,
      safe_seed_chart:"h=2*sin(delta/2), h_u=cos(delta/2)*(beta-1), h_uu=-h*(beta-1)^2/4+cos(delta/2)*beta_u; cos(delta/2)>0",
      whole_surface_metric_reach_or_motion_certified:false,
      finite_provider_bitwise_equality_claimed:false};
  }
  return {box,point:t=>box(t,t),definition,arithmetic:C};
}
if(typeof module!=="undefined"&&module.exports)module.exports={createR197FullCircleMaterialConsumer};
