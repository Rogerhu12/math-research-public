"use strict";
/* Exact R128/R130/R204/R205 scalar-amplitude consumer. New independent source.
   No existing provider, metric, unknown, objective, or domain is modified. */

function binary64Q(x){
 if(!Number.isFinite(x))throw new RangeError("Finite binary64 input required");
 if(x===0)return Q(0n);
 const v=new DataView(new ArrayBuffer(8));v.setFloat64(0,x,false);
 const hi=v.getUint32(0,false),lo=v.getUint32(4,false),exp=(hi>>>20)&2047;
 let mant=(BigInt(hi&1048575)<<32n)|BigInt(lo);
 if(exp)mant|=1n<<52n;
 if(hi>>>31)mant=-mant;
 const e=exp?exp-1023-52:-1074;
 return e>=0?Q(mant<<BigInt(e)):Q(mant,1n<<BigInt(-e));
}
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){let t=a%b;a=b;b=t;}return a;}
function Q(a,b=1n){a=BigInt(a);b=BigInt(b);if(b===0n)throw Error("zero denominator");if(b<0n){a=-a;b=-b;}const d=gcd(a,b);return {n:a/d,d:b/d};}
function q(s){if(typeof s==="object"&&s.n!==undefined)return s;if(typeof s==="bigint")return Q(s);if(typeof s==="number")return binary64Q(s);s=String(s);if(s.includes("/")){const[a,b]=s.split("/");return Q(a,b);}if(s.includes(".")){const sign=s.startsWith("-")?-1n:1n;s=s.replace(/^-/,"");const[a,b]=s.split(".");return Q(sign*BigInt(a+b),10n**BigInt(b.length));}return Q(s);}
const add=(a,b)=>Q(a.n*b.d+b.n*a.d,a.d*b.d),neg=a=>Q(-a.n,a.d),sub=(a,b)=>add(a,neg(b)),mul=(a,b)=>Q(a.n*b.n,a.d*b.d),div=(a,b)=>Q(a.n*b.d,a.d*b.n),sq=a=>mul(a,a),cmp=(a,b)=>a.n*b.d<b.n*a.d?-1:a.n*b.d>b.n*a.d?1:0;
const zero=q(0),one=q(1),two=q(2);
function out(a){return {numerator:String(a.n),denominator:String(a.d),fraction:a.d===1n?String(a.n):String(a.n)+"/"+String(a.d),decimal:Number(a.n)/Number(a.d)};}
function sum(a){return a.reduce(add,zero);}
function dot(a,b){return sum(a.map((x,i)=>mul(x,b[i])));}

function binom(n,k){if(k<0||k>n)return 0n;let v=1n;for(let j=1;j<=k;j++)v=v*BigInt(n-j+1)/BigInt(j);return v;}
function powq(x,n){let r=one;for(let j=0;j<n;j++)r=mul(r,x);return r;}
function polyMul(a,b){const c=Array(a.length+b.length-1).fill(null).map(()=>zero);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)c[i+j]=add(c[i+j],mul(a[i],b[j]));return c;}
function integrate01(a){return sum(a.map((v,i)=>div(v,q(i+1))));}
function bernsteinOn(a,left,right){
 const n=a.length-1,h=sub(right,left),p=Array(n+1).fill(null).map(()=>zero);
 for(let j=0;j<=n;j++)for(let k=j;k<=n;k++)p[j]=add(p[j],mul(a[k],mul(Q(binom(k,j)),mul(powq(left,k-j),powq(h,j)))));
 return p.map((_,j)=>sum(p.slice(0,j+1).map((v,i)=>mul(v,Q(binom(j,i),binom(n,i))))));
}
const S=[0,0,0,0,0,126,-420,540,-315,70].map(q),S2=polyMul(S,S),S4=polyMul(S2,S2);
const moments={S1:integrate01(S),S2:integrate01(S2),S4:integrate01(S4)};
const a=q(".8"),flat=q(".34"),cuff=q(".32"),L=q(".46"),h1=div(L,two);
const c2=div(mul(L,moments.S2),two),c4=div(mul(L,moments.S4),q(24));
const held=q(".64"),reachTarget=q(".097"),amplitudeMax=q("6/5"),ballRadius=q("1.6"),slab=q(".85");
function xUpper(A){return add(sub(a,mul(c2,sq(A))),mul(c4,powq(A,4)));}
function heldPolynomial(Aq,Z){
 Aq=q(Aq);Z=q(Z);
 const dx=[sub(Aq,a),zero,c2,zero,neg(c4)],zz=[Z,neg(h1)];
 const p=polyMul(dx,dx),v=polyMul(zz,zz);
 for(let i=0;i<v.length;i++)p[i]=add(p[i],v[i]);
 p[0]=sub(p[0],sq(held));return p;
}
function checkDomain(A,Aq,Z){
 if(cmp(A,zero)<0||cmp(A,amplitudeMax)>0)throw new RangeError("This consumer proves only 0<=amplitude<=6/5");
 if(cmp(Aq,a)<0)throw new RangeError("Require the true central support lower bound >=4/5");
 if(cmp(Z,mul(h1,A))<0)throw new RangeError("Require true cuff height >=23*amplitude/100 before squaring vertical lower bounds");
}
function tailBounds({amplitude,centralLower,cuffHeight}){
 const A=q(amplitude),Aq=q(centralLower),Z=q(cuffHeight);checkDomain(A,Aq,Z);
 const xu=xUpper(A),hu=mul(h1,A),zlo=sub(Z,hu),dx=sub(Aq,xu);
 const k=mul(q("7875/1472"),A),support=mul(Z,sub(one,div(sq(A),two)));
 const squared=add(sq(dx),sq(zlo)),margin=sub(squared,sq(held));
 return {schema:"fd2d-R205-rational-amplitude-tail-bounds-v1",
 inputs:{amplitude:out(A),central_support_lower:out(Aq),true_inner_cuff_height:out(Z)},
 input_number_interpretation:"JS numbers are their exact IEEE binary64 rational values; decimal strings are exact decimals",
 cut_horizontal_upper:out(xu),descent_upper:out(hu),minimum_height_lower:out(zlo),
 held_squared_lower:out(squared),held_squared_margin:out(margin),held_passed:margin.n>=0n,
 kappa_maximum:out(k),whole_cylinder_reach_lower:k.n===0n?null:out(div(one,k)),
 amplitude_zero_reach_is_infinite:k.n===0n,
 support_lower:out(support),support_margin:out(sub(support,reachTarget)),
 sphere_squared_upper:out(add(sq(a),sq(Z))),sphere_margin:out(sub(sq(ballRadius),add(sq(a),sq(Z)))),
 phase_zero_slab_upper:out(xu),slab_margin:out(sub(slab,xu)),
 opposite_tail_half_separation_margin:out(sub(zlo,reachTarget)),
 same_side_tail_and_filling_disk_normal_ball_source:"R130 complete no-boundary cylinder; subset surface-normal point-pair inequality only",
 still_required:["accurate complete prefix and full twojet match","whole prefix-core and prefix-tail/disk normal-ball comparisons","whole prefix sphere/slab/height/held conditions","fixed-g exact-solution approximation and full-surface certification"],
 qualification:"This computes sufficient tail bounds, not an evaluated finite LM state or a completed core."};
}
function uniformHeldCertificate({centralLower,cuffHeightLower,amplitudeCuts=["0","6/5"]}){
 const Aqs=q(centralLower),Z=q(cuffHeightLower),cuts=amplitudeCuts.map(q);
 if(cuts.length<2||cmp(cuts[0],zero)!==0||cuts.some((x,i)=>i&&cmp(x,cuts[i-1])<=0)||cmp(cuts.at(-1),amplitudeMax)>0)throw new RangeError("Increasing exact amplitude partition must cover [0,Amax], Amax<=6/5");
 checkDomain(cuts.at(-1),Aqs,Z);
 const p=heldPolynomial(Aqs,Z),boxes=[];
 for(let j=0;j+1<cuts.length;j++){
  const b=bernsteinOn(p,cuts[j],cuts[j+1]),minimum=b.reduce((v,w)=>cmp(v,w)<0?v:w);
  boxes.push({interval:[out(cuts[j]),out(cuts[j+1])],bernstein_coefficients:b.map(out),minimum:out(minimum),passed:b.every(v=>v.n>=0n)});
 }
 const minimum=boxes.map(b=>q(b.minimum.fraction)).reduce((v,w)=>cmp(v,w)<0?v:w);
 return {schema:"fd2d-R205-continuous-amplitude-held-certificate-v1",
 central_lower:out(Aqs),cuff_height_lower:out(Z),amplitude_upper:out(cuts.at(-1)),
 held_radius:out(held),power_coefficients:p.map(out),boxes,
 uniform_squared_margin:out(minimum),passed:boxes.every(b=>b.passed),
 source_of_continuity:"Exact Bernstein convex-combination identity on every complete amplitude interval; no amplitude sampling"};
}
function constants(){return{flat_radius:out(flat),cuff_radius:out(cuff),outer_cut_radius:out(a),L:out(L),amplitude_max:out(amplitudeMax),c2:out(c2),c4:out(c4),h1:out(h1),moments:Object.fromEntries(Object.entries(moments).map(([k,v])=>[k,out(v)]))};}
function commonBudget(){
 const Zmin=q(".40"),Zmax=q(".63"),Rmin=div(q("1472/7875"),amplitudeMax);
 const margins={
  whole_cylinder_reach:sub(Rmin,reachTarget),
  minimum_positive_height:sub(Zmin,mul(h1,amplitudeMax)),
  opposite_tail_half_separation:sub(sub(Zmin,mul(h1,amplitudeMax)),reachTarget),
  support:sub(mul(Zmin,sub(one,div(sq(amplitudeMax),two))),reachTarget),
  ball:sub(sq(ballRadius),add(sq(a),sq(Zmax))),
  slab:sub(slab,a),flat_collar:sub(flat,cuff)
 };
 return {schema:"fd2d-R205-common-cap-tail-budget-v1",amplitude_interval:["0","6/5"],true_height_interval:[".40",".63"],minimum_cylinder_reach:out(Rmin),margins:Object.fromEntries(Object.entries(margins).map(([k,v])=>[k,{...out(v),passed:v.n>0n}])),passed:Object.values(margins).every(v=>v.n>0n),held_not_included_in_this_common_geometric_packet:true};
}
module.exports={tailBounds,uniformHeldCertificate,commonBudget,constants,binary64Rational:x=>out(binary64Q(x))};
