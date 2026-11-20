// Exact characteristic interval sums for the flattening design route after R55.
function certifyCharacteristicRoute() {
  const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){[a,b]=[b,a%b];}return a;};
  const Q=(a,b=1n)=>{a=BigInt(a);b=BigInt(b);if(b<0n){a=-a;b=-b;}const g=gcd(a,b);return[a/g,b/g];};
  const add=(a,b)=>Q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]),neg=a=>[-a[0],a[1]];
  const sub=(a,b)=>add(a,neg(b)),mul=(a,b)=>Q(a[0]*b[0],a[1]*b[1]),div=(a,b)=>Q(a[0]*b[1],a[1]*b[0]);
  const pow=(a,n)=>{let v=Q(1);for(let j=0;j<n;j++)v=mul(v,a);return v;};
  const cmp=(a,b)=>{const c=a[0]*b[1]-b[0]*a[1];return c<0n?-1:c>0n?1:0;};
  const min=(a,b)=>cmp(a,b)<=0?a:b,max=(a,b)=>cmp(a,b)>=0?a:b;
  const repr=a=>a.map(String).join("/");
  const one=Q(1),eta=Q(1,20),S=10n**30n,N=2000;
  function ramp(t){
    const left=cmp(t,Q(1,2))<=0,z=left?t:sub(one,t);
    let f,p,d;
    if(cmp(z,eta)<=0){
      const x=div(z,eta);
      f=mul(div(eta,sub(one,eta)),sub(pow(x,3),div(pow(x,4),Q(2))));
      p=mul(div(pow(eta,2),sub(one,eta)),sub(div(pow(x,4),Q(4)),div(pow(x,5),Q(10))));
      d=div(sub(mul(Q(3),pow(x,2)),mul(Q(2),pow(x,3))),sub(one,eta));
    }else{
      f=div(sub(z,div(eta,Q(2))),sub(one,eta));
      p=div(add(sub(div(pow(z,2),Q(2)),div(mul(eta,z),Q(2))),mul(Q(3,20),pow(eta,2))),sub(one,eta));
      d=div(one,sub(one,eta));
    }
    return left?[f,p,d]:[sub(one,f),add(sub(Q(1,2),z),p),d];
  }
  function isqrt(n){if(n<0n)throw Error("negative sqrt");if(n<2n)return n;let x=1n<<BigInt((n.toString(2).length+1)>>1);while(true){const y=(x+n/x)>>1n;if(y>=x)return x;x=y;}}
  function sqrtFloor(a){if(a[0]<0n)throw Error("negative integrand");return isqrt(a[0]*S*S/a[1]);}
  const stages=[
    {v0:Q(0),dv:Q(13,100),L:Q(104,1425),A:Q(0)},
    {v0:Q(13,100),dv:Q(8,25),L:Q(128,2025),A:Q(169,35625)}
  ];
  function integralBox(klo,khi,rlo,rhi,count,stops=null){
    let lowerTotal=Q(0),upperTotal=Q(0),index=0;
    for(const st of stages.slice(0,count)){
      const stop=stops?stops[index]:Q(1);index++;
      let lower=0n,upper=0n;
      for(let j=0;j<N;j++){
        const t0=mul(stop,Q(j,N)),t1=mul(stop,Q(j+1,N));
        const [f0,p0,d0]=ramp(t0),[f1,p1,d1]=ramp(t1);
        const dmin=min(d0,d1);
        let dmax=max(d0,d1);
        if(cmp(t1,eta)>=0&&cmp(t0,sub(one,eta))<=0)dmax=div(one,sub(one,eta));
        const v0=add(st.v0,mul(st.dv,f0)),v1=add(st.v0,mul(st.dv,f1));
        const A0=add(st.A,mul(st.L,add(mul(st.v0,t0),mul(st.dv,p0))));
        const A1=add(st.A,mul(st.L,add(mul(st.v0,t1),mul(st.dv,p1))));
        const alo=add(one,mul(rhi,A0)),ahi=add(one,mul(rlo,A1));
        const denlo=mul(ahi,sub(pow(khi,2),pow(v0,2)));
        const denhi=mul(alo,sub(pow(klo,2),pow(v1,2)));
        if(denlo[0]<=0n||denhi[0]<=0n)throw Error("root domain not uniform");
        const low=div(mul(mul(mul(rlo,st.L),st.dv),dmin),denlo);
        const high=div(mul(mul(mul(rhi,st.L),st.dv),dmax),denhi);
        lower+=sqrtFloor(low);upper+=sqrtFloor(high)+1n;
      }
      lowerTotal=add(lowerTotal,mul(stop,Q(lower,BigInt(N)*S)));
      upperTotal=add(upperTotal,mul(stop,Q(upper,BigInt(N)*S)));
    }
    return [lowerTotal,upperTotal];
  }
  const rlo=Q(21,20),rhi=Q(11,10);
  const center=integralBox(Q(13,20),Q(7,10),rlo,rhi,2);
  const representative=integralBox(Q(2,3),Q(2,3),Q(1069,1000),Q(107,100),2);
  const final=integralBox(Q(1,5),Q(41,200),rlo,rhi,1);
  if(cmp(center[0],Q(37,100))<=0||cmp(center[1],Q(83,200))>=0)throw Error("center summary bounds not paid");
  if(cmp(final[0],Q(13,25))<=0)throw Error("final first-stage loss not above .52");
  const intermediate=integralBox(Q(9,20),Q(9,20),rlo,rhi,2,[Q(1),Q(533,800)]);
  if(cmp(intermediate[1],Q(1,2))>=0)throw Error("intermediate arc not proved protected");
  const actualV=add(Q(13,100),mul(Q(8,25),ramp(Q(533,800))[0]));
  if(cmp(actualV,Q(173,500))!==0)throw Error("intermediate speed mismatch");
  const intermediateK2=div(pow(div(Q(405,76),rhi),2),sub(pow(Q(9,20),2),pow(actualV,2)));
  if(cmp(intermediateK2,pow(Q(50,3),2))<=0)throw Error("intermediate curvature not above necessary reach bound");
  if(cmp(center[0],Q(37049,100000))<=0||cmp(center[1],Q(82943,200000))>=0)throw Error("tau0 displayed interval not paid");
  if(cmp(representative[0],Q(9902,25000))<=0||cmp(representative[1],Q(396727,1000000))>=0)throw Error("representative displayed interval not paid");
  if(cmp(intermediate[0],Q(9651,20000))<=0||cmp(intermediate[1],Q(49427,100000))>=0)throw Error("intermediate displayed interval not paid");
  const firstUpper2=div(mul(mul(rhi,stages[0].L),stages[0].dv),sub(pow(Q(13,20),2),pow(Q(13,100),2)));
  const secondUpper2=div(mul(mul(rhi,stages[1].L),stages[1].dv),sub(pow(Q(13,20),2),pow(Q(9,20),2)));
  const c=Q(479,1000),gap=sub(sub(pow(c,2),firstUpper2),secondUpper2);
  if(gap[0]<=0n||cmp(pow(gap,2),mul(Q(4),mul(firstUpper2,secondUpper2)))<=0)throw Error("Cauchy upper not below .479");
  return {
    scope:"exact characteristic integrals of the new reference profile; no BVP or K=0-to-positive-K extension theorem",
    status:"all_exact_rational_bounds_passed",panels_per_stage:N,sqrt_scale:S.toString(),
    r_interval:[repr(rlo),repr(rhi)],
    tau0_conditional_k_interval:["13/20","7/10"],
    tau0_loss_interval:center.map(repr),tau0_summary:["37/100","83/200"],
    k_2over3_r_1069_to_1070:representative.map(repr),
    final_first_stage_k_interval:["1/5","41/200"],final_first_stage_loss_interval:final.map(repr),
    final_first_stage_strict_lower:"13/25",
    cauchy_upper_strict:"479/1000",
    intermediate_exact_k:"9/20",intermediate_second_stage_stop:"533/800",
    intermediate_speed:"173/500",intermediate_loss_interval:intermediate.map(repr),
    intermediate_curvature_square_lower:repr(intermediateK2),
    intermediate_reach_obstruction_under_R5:true,
    final_required_target_for_inherited_R54_constants:"k=1/5",
    safe_parameter_order:"finish curvature_blend=1 while homotopy<1; then homotopy to1",
    positive_K_degenerate_continuation_gap_preserved:true
  };
}
console.log(JSON.stringify(certifyCharacteristicRoute(),null,2));

