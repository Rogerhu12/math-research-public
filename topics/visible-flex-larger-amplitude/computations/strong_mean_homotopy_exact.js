#!/usr/bin/env node
"use strict";
/*
Exact rational interval implication for the height-mean difference of two
finite prefix fields in one fixed physical metric and one common angle chart.

This consumes supplied continuous field boxes. It does NOT generate or verify
those boxes from a checkpoint and therefore NEVER certifies an actual prefix.
All arithmetic, including square-root enclosures, is rational BigInt.
No RHS, BVP, Node tail worker, external package, or MJS module is imported.
*/
const SCHEMA="strong-mean-homotopy-interval-input-v1";
const PINNED={
 adaptive_frame_sha256:"958a9e2e428f8d64dfc786bed515bad77a208433fa16af7cbbe6f03b1bcc7ebe",
 cylindrical_mean_sha256:"e621ee2e9e8a706332b3839122a8ec57e1c5c2cfe82a48a759dcdad0548c54b2",
 source_commit:"869436630c99aa5a68afb55bd8877c826034d117"
};
function assert(ok,message){if(!ok)throw Error(message);}
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){const t=a%b;a=b;b=t;}return a;}
class Rat{
 constructor(n,d=1n){n=BigInt(n);d=BigInt(d);assert(d!==0n,"zero rational denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);this.n=n/g;this.d=d/g;}
 add(q){q=Q(q);return new Rat(this.n*q.d+q.n*this.d,this.d*q.d);}
 sub(q){return this.add(Q(q).neg());}
 mul(q){q=Q(q);return new Rat(this.n*q.n,this.d*q.d);}
 div(q){q=Q(q);return new Rat(this.n*q.d,this.d*q.n);}
 neg(){return new Rat(-this.n,this.d);}
 abs(){return this.n<0n?this.neg():this;}
 cmp(q){q=Q(q);const x=this.n*q.d-q.n*this.d;return x<0n?-1:x>0n?1:0;}
 eq(q){return this.cmp(q)===0;}
 toString(){return this.n.toString()+"/"+this.d.toString();}
 toJSON(){return this.toString();}
}
function Q(x){
 if(x instanceof Rat)return x;
 if(typeof x==="bigint")return new Rat(x);
 if(typeof x==="number"){assert(Number.isSafeInteger(x),"internal noninteger Number");return new Rat(BigInt(x));}
 assert(typeof x==="string","exact input must be a rational or decimal string");
 if(/^[+-]?\d+\/[+-]?\d+$/.test(x)){const p=x.split("/");return new Rat(BigInt(p[0]),BigInt(p[1]));}
 const m=/^([+-]?)(\d+)(?:\.(\d*))?(?:[eE]([+-]?\d+))?$/.exec(x);
 assert(m,"invalid exact decimal: "+String(x));const e=Number(m[4]||"0")-(m[3]||"").length;
 assert(Number.isSafeInteger(e)&&Math.abs(e)<=10000,"decimal exponent out of range");
 let n=BigInt(m[2]+(m[3]||""));if(m[1]==="-")n=-n;
 return e>=0?new Rat(n*10n**BigInt(e)):new Rat(n,10n**BigInt(-e));
}
const Z=Q(0),O=Q(1),TWO=Q(2),FOUR=Q(4);
function minQ(xs){return xs.reduce((a,b)=>a.cmp(b)<=0?a:b);}
function maxQ(xs){return xs.reduce((a,b)=>a.cmp(b)>=0?a:b);}
function I(a,b=a){a=Q(a);b=Q(b);assert(a.cmp(b)<=0,"reversed interval");return [a,b];}
const IZ=I(Z),IO=I(O);
function readI(x){
 if(typeof x==="string")return I(Q(x));
 assert(Array.isArray(x)&&x.length===2&&x.every(v=>typeof v==="string"),"interval requires two exact strings");
 return I(Q(x[0]),Q(x[1]));
}
function iadd(a,b){return I(a[0].add(b[0]),a[1].add(b[1]));}
function ineg(a){return I(a[1].neg(),a[0].neg());}
function isub(a,b){return iadd(a,ineg(b));}
function imul(a,b){const p=[a[0].mul(b[0]),a[0].mul(b[1]),a[1].mul(b[0]),a[1].mul(b[1])];return I(minQ(p),maxQ(p));}
function iinv(a){assert(a[0].cmp(Z)>0||a[1].cmp(Z)<0,"interval reciprocal crosses zero");return I(O.div(a[1]),O.div(a[0]));}
function idiv(a,b){return imul(a,iinv(b));}
function isquare(a){const p=[a[0].mul(a[0]),a[1].mul(a[1])];return I(a[0].cmp(Z)<=0&&a[1].cmp(Z)>=0?Z:minQ(p),maxQ(p));}
function absmax(a){return maxQ(a.map(x=>x.abs()));}
function contains(a,b){return a[0].cmp(b[0])<=0&&a[1].cmp(b[1])>=0;}
function integerSqrt(n){assert(n>=0n,"negative integer square root");if(n<2n)return n;let x=1n<<BigInt(Math.ceil(n.toString(2).length/2));for(;;){const y=(x+n/x)>>1n;if(y>=x)return x;x=y;}}
function sqrtPoint(q,bits){
 assert(q.cmp(Z)>=0,"negative square root");
 const nr=integerSqrt(q.n),dr=integerSqrt(q.d);
 if(nr*nr===q.n&&dr*dr===q.d){const exact=new Rat(nr,dr);return [exact,exact];}
 const scale=1n<<BigInt(bits);
 const k=integerSqrt((q.n*scale*scale)/q.d);const lo=new Rat(k,scale);
 return [lo,lo.mul(lo).eq(q)?lo:new Rat(k+1n,scale)];
}
function isqrt(a,bits){return I(sqrtPoint(a[0],bits)[0],sqrtPoint(a[1],bits)[1]);}
function upperDecimal(q,digits=18){
 assert(q.cmp(Z)>=0,"upper decimal expects nonnegative");
 const scale=10n**BigInt(digits);const n=(q.n*scale+q.d-1n)/q.d;
 const s=n.toString().padStart(digits+1,"0");return s.slice(0,-digits)+"."+s.slice(-digits);
}
function boundRecord(q){return {exact:q.toString(),outward_decimal:upperDecimal(q)};}
function jconstant(a){return [a,IZ,IZ,IZ];}
function jadd(a,b){return a.map((v,k)=>iadd(v,b[k]));}
function jneg(a){return a.map(ineg);}
function jsub(a,b){return jadd(a,jneg(b));}
function jmul(a,b){return [
 imul(a[0],b[0]),
 iadd(imul(a[1],b[0]),imul(a[0],b[1])),
 iadd(imul(a[2],b[0]),imul(a[0],b[2])),
 iadd(iadd(imul(a[3],b[0]),imul(a[1],b[2])),iadd(imul(a[2],b[1]),imul(a[0],b[3])))
];}
function junary(a,value,first,second){return [
 value,imul(first,a[1]),imul(first,a[2]),
 iadd(imul(first,a[3]),imul(second,imul(a[1],a[2])))
];}
function jsquare(a){return junary(a,isquare(a[0]),imul(I(TWO),a[0]),I(TWO));}
function jinv(a){const inv=iinv(a[0]),sq=isquare(inv),cube=imul(sq,inv);return junary(a,inv,ineg(sq),imul(I(TWO),cube));}
function jsqrt(a,bits){const root=isqrt(a[0],bits),inv=iinv(root);return junary(a,root,imul(I("1/2"),inv),ineg(imul(I("1/4"),imul(isquare(inv),inv))));}
function jdiv(a,b){return jmul(a,jinv(b));}
function jdot(a,b){return a.reduce((v,x,k)=>jadd(v,jmul(x,b[k])),jconstant(IZ));}
function jnorm2(a){return a.reduce((v,x)=>jadd(v,jsquare(x)),jconstant(IZ));}
function jcross(a,b){return [
 jsub(jmul(a[1],b[2]),jmul(a[2],b[1])),
 jsub(jmul(a[2],b[0]),jmul(a[0],b[2])),
 jsub(jmul(a[0],b[1]),jmul(a[1],b[0]))
];}
function velocityJets(d,e,c,v,bits=96){
 const P=jnorm2(d);assert(P[0][0].cmp(Z)>0,"P=|d|^2 not proved positive");
 const R=jdot(d,e),w=jcross(d,e),W=jnorm2(w);assert(W[0][0].cmp(Z)>0,"W=|d cross e|^2 not proved positive");
 const P3=jmul(jsquare(P),P),D=jsub(W,jmul(jsquare(c),P3));
 assert(D[0][0].cmp(Z)>0,"D=W-c^2 P^3 not proved positive on the full homotopy box");
 const root=jsqrt(D,bits),Winv=jinv(W);
 const velocity=d.map((dj,k)=>{
  const A=jsub(jmul(P,e[k]),jmul(R,dj));
  return jadd(jmul(jadd(jneg(jmul(jmul(c,P),A)),jmul(root,w[k])),Winv),jmul(v,dj));
 });
 return {P,W,D,velocity,alphaSquared:idiv(imul(isquare(c[0]),P3[0]),W[0])};
}
function vec(x,name){assert(Array.isArray(x)&&x.length===3,name+" needs three components");return x.map(readI);}
function fieldJets(box,valueName,sName,deltaName,deltaSName,U){
 const a=vec(box[valueName],valueName),as=vec(box[sName],sName);
 const du=vec(box[deltaName],deltaName),dus=vec(box[deltaSName],deltaSName);
 return a.map((x,k)=>[iadd(x,imul(U,du[k])),du[k],iadd(as[k],imul(U,dus[k])),dus[k]]);
}
function grid(x,name,finish){
 assert(Array.isArray(x)&&x.length>=2&&x.every(y=>typeof y==="string"),name+" requires exact string endpoints");
 const q=x.map(Q);assert(q[0].eq(Z),name+" must start at 0");
 if(finish!==null)assert(q.at(-1).eq(finish),name+" must end at "+finish);
 for(let k=1;k<q.length;k++)assert(q[k-1].cmp(q[k])<0,name+" must strictly increase");
 return q;
}
function evaluateInput(input,bits=96){
 assert(input&&input.schema===SCHEMA,"input schema differs");
 assert(Number.isSafeInteger(bits)&&bits>=32&&bits<=256,"square-root bits outside 32..256");
 const ids=input.identity;assert(ids&&typeof ids==="object","missing input identity");
 for(const k of ["coarse_sha256","fine_sha256","common_metric_sha256","common_chart_sha256"])
  assert(typeof ids[k]==="string"&&/^[0-9a-f]{64}$/.test(ids[k]),"missing exact identity "+k);
 assert(typeof input.enclosure_provenance==="string"&&input.enclosure_provenance.length>0,"missing enclosure provenance");
 const S=grid(input.physical_s_breaks,"physical_s_breaks",null);
 const A=grid(input.angular_turn_breaks,"angular_turn_breaks",O),U=grid(input.homotopy_breaks,"homotopy_breaks",O);
 const sizes=[S.length-1,A.length-1,U.length-1],count=sizes.reduce((x,y)=>x*y,1);
 assert(Number.isSafeInteger(count)&&Array.isArray(input.boxes)&&input.boxes.length===count,"incomplete rectangular box count");
 const seen=new Set(),weighted=Array.from({length:sizes[0]},()=>[IZ,IZ]);
 let minRadius=null,minP=null,minW=null,minD=null,maxAlpha=Z;
 const witnesses={};
 for(const box of input.boxes){
  const ix=box.index;assert(Array.isArray(ix)&&ix.length===3&&ix.every((x,k)=>Number.isInteger(x)&&x>=0&&x<sizes[k]),"invalid box index");
  const key=ix.join(":");assert(!seen.has(key),"duplicate box");seen.add(key);
  const ui=I(U[ix[2]],U[ix[2]+1]);
  const d=fieldJets(box,"d0","f0","delta_d","delta_f",ui);
  const e=fieldJets(box,"e0","g0","delta_e","delta_g",ui);
  const radius=readI(box.a),radiusS=readI(box.a_s),radiusSS=readI(box.a_ss);
  assert(radius[0].cmp(Z)>0,"box "+key+": physical radius a not proved positive");
  if(minRadius===null||radius[0].cmp(minRadius)<0)minRadius=radius[0];
  const c=jdiv([radiusS,IZ,radiusSS,IZ],[radius,IZ,radiusS,IZ]);
  const v=[readI(box.v),IZ,readI(box.v_s),IZ];
  let out;try{out=velocityJets(d,e,c,v,bits);}catch(error){throw Error("box "+key+": "+String(error.message));}
  for(const [name,value] of [["P",out.P[0][0]],["W",out.W[0][0]],["D",out.D[0][0]]]){
   const old=name==="P"?minP:name==="W"?minW:minD;
   if(old===null||value.cmp(old)<0){if(name==="P")minP=value;else if(name==="W")minW=value;else minD=value;witnesses[name]=ix.slice();}
  }
  maxAlpha=maxQ([maxAlpha,out.alphaSquared[1]]);
  const weight=A[ix[1]+1].sub(A[ix[1]]).mul(U[ix[2]+1].sub(U[ix[2]]));
  weighted[ix[0]][0]=iadd(weighted[ix[0]][0],imul(I(weight),out.velocity[2][1]));
  weighted[ix[0]][1]=iadd(weighted[ix[0]][1],imul(I(weight),out.velocity[2][3]));
 }
 assert(seen.size===count,"incomplete box cover");
 const anchor=readI(input.height_anchor_difference);
 let prefix=anchor,A0=absmax(anchor),A1=Z,A2=Z;
 const slabs=[];
 for(let i=0;i<sizes[0];i++){
  const h=S[i+1].sub(S[i]),m1=weighted[i][0],m2=weighted[i][1];
  const within=iadd(prefix,imul(I(Z,h),m1));
  A0=maxQ([A0,absmax(within)]);A1=maxQ([A1,absmax(m1)]);A2=maxQ([A2,absmax(m2)]);
  const next=iadd(prefix,imul(I(h),m1));
  slabs.push({index:i,s:[S[i],S[i+1]],delta_mean_prime:m1,delta_mean_second:m2,
   delta_mean_height_at_left:prefix,delta_mean_height_anywhere:within,delta_mean_height_at_right:next});
  prefix=next;
 }
 return {
  schema:"strong-mean-homotopy-interval-implication-v1",status:"conditional-interval-implication-passed",
  scope:"Exact rational implication from supplied full physical-s/angle/homotopy field enclosures; not an executed actual-prefix certificate.",
  pinned_sources:PINNED,identity:ids,enclosure_provenance:input.enclosure_provenance,
  all_rectangular_boxes_consumed:true,box_count:count,grid_shape:sizes,square_root_bits:bits,
  full_homotopy_domain:{physical_radius_lower:minRadius,P_lower:minP,W_lower:minW,D_lower:minD,alpha_squared_upper:maxAlpha,witnesses},
  mean_definition:"H'(s)=(1/2pi) integral_0^2pi V_z(s,psi) dpsi, H fixed by the supplied anchor; exact integrals, not finite quadrature samples.",
  mean_derivative_enclosures:slabs,height_anchor_difference:anchor,
  A0:boundRecord(A0),A1:boundRecord(A1),A2:boundRecord(A2),
  source_field_enclosures_verified_by_this_tool:false,actual_prefix_C2_certificate:false,
  exact_knot_continuity_inferred:false,convergence_to_exact_solution_claim:false,
  numerical_quadrature_or_alias_error_paid:false,physical_RHS_calls:0,tail_workers:0,newton_solves:0,
  limitations:[
   "The producer must prove every supplied vector/scalar box and its identity. Coverage and interval implication do not prove those input bounds.",
   "All-s second derivative bounds hold on the supplied smooth panels and one-sided limits; global C2 requires a separate exact knot-join or declared repair.",
   "A1/A2 bound the exact mean defined above. Numeric angular/Gauss approximations require separate error bounds.",
   "This compares two finite reconstructed fields and does not establish either field's distance to the exact PDE solution."
  ]
 };
}
function pointJet(a,u=0,s=0,us=0){return [I(a),I(u),I(s),I(us)];}
function equalJ(a,b){return a.every((v,k)=>v[0].eq(b[k][0])&&v[1].eq(b[k][1]));}
function throws(fn){try{fn();return false;}catch(error){return true;}}
function fixtureInput(){
 const z=["0","0","0"],zero="0";
 return {schema:SCHEMA,identity:{coarse_sha256:"0".repeat(64),fine_sha256:"1".repeat(64),common_metric_sha256:"2".repeat(64),common_chart_sha256:"3".repeat(64)},
  enclosure_provenance:"Pure algebra/storage fixture. These are NOT boxes generated from an actual surface.",
  physical_s_breaks:["0","1/2","1"],angular_turn_breaks:["0","1/3","1"],homotopy_breaks:["0","1/2","1"],
  height_anchor_difference:"0",boxes:[]
 };
}
function selfCheck(){
 const checks={},j0=pointJet(0),c=pointJet("2/15"),v=pointJet("1/7");
 const d=[j0,pointJet(3),j0],e=[pointJet(-2),j0,j0],base=velocityJets(d,e,c,v);
 checks.axis_value_exact=equalJ(base.velocity[0],pointJet("3/5"))&&equalJ(base.velocity[1],pointJet("3/7"))&&equalJ(base.velocity[2],pointJet("4/5"));
 checks.axis_domain_exact=base.P[0][0].eq(9)&&base.W[0][0].eq(36)&&base.D[0][0].eq("576/25");
 const r=pointJet(3,"1/10","1/7","1/20"),cc=pointJet("1/5",0,"1/50");
 const circle=velocityJets([j0,r,j0],[jneg(r),j0,j0],cc,pointJet(0));
 const k=jmul(cc,r),knownZ=jsqrt(jsub(pointJet(1),jsquare(k)),96);
 checks.mixed_derivative_circle_exact=circle.velocity.every((a,i)=>equalJ(a,i===0?k:i===2?knownZ:j0));
 const rot=[["1","0","0"],["0","3/5","-4/5"],["0","4/5","3/5"]].map(row=>row.map(Q));
 const rotate=vec=>rot.map(row=>row.reduce((sum,x,k)=>jadd(sum,jmul(pointJet(x),vec[k])),j0));
 const rd=rotate([j0,r,j0]),re=rotate([jneg(r),j0,j0]),rv=velocityJets(rd,re,cc,pointJet(0));
 checks.rational_rotation_all_four_jets=rv.velocity.every((a,k)=>equalJ(a,rotate(circle.velocity)[k]));
 const sq=isqrt(I(2,3),96);
 checks.sqrt_outward_exact=sq[0].mul(sq[0]).cmp(2)<=0&&sq[1].mul(sq[1]).cmp(3)>=0;
 checks.parallel_domain_rejected=throws(()=>velocityJets(d,d,c,v));
 checks.zero_tangent_rejected=throws(()=>velocityJets([j0,j0,j0],e,c,v));
 checks.bad_discriminant_rejected=throws(()=>velocityJets(d,e,pointJet(1),v));
 const f=fixtureInput(),zero=["0","0","0"];
 for(let i=0;i<2;i++)for(let j=0;j<2;j++)for(let k0=0;k0<2;k0++)f.boxes.push({
  index:[i,j,k0],d0:["0",["1","11/10"],"0"],e0:[["-11/10","-1"],"0","0"],
  f0:["0","1/10","0"],g0:["-1/10","0","0"],delta_d:zero,delta_e:zero,delta_f:zero,delta_g:zero,
  a:"1",a_s:"1/10",a_ss:"1/100",v:"1/7",v_s:"1/9"
 });
 const result=evaluateInput(f);
 checks.full_grid_consumed=result.box_count===8&&result.all_rectangular_boxes_consumed;
 checks.identical_field_means_exact_zero=[result.A0,result.A1,result.A2].every(x=>Q(x.exact).eq(Z));
 const missing=JSON.parse(JSON.stringify(f));missing.boxes.pop();
 checks.missing_box_rejected=throws(()=>evaluateInput(missing));
 const badRadius=JSON.parse(JSON.stringify(f));badRadius.boxes[0].a=["-1","1"];
 checks.nonpositive_radius_rejected=throws(()=>evaluateInput(badRadius));
 const duplicate=JSON.parse(JSON.stringify(f));duplicate.boxes[7]=duplicate.boxes[0];
 checks.duplicate_box_rejected=throws(()=>evaluateInput(duplicate));
 const changed=JSON.parse(JSON.stringify(f));
 for(const b of changed.boxes){b.delta_d=["0","1/20","0"];b.delta_e=["-1/20","0","0"];}
 const varied=evaluateInput(changed);
 checks.nonzero_difference_finite=Q(varied.A1.exact).cmp(Z)>0&&Q(varied.A2.exact).cmp(Z)>0;
 checks.actual_certificate_remains_false=!varied.actual_prefix_C2_certificate&&!varied.source_field_enclosures_verified_by_this_tool;
 assert(Object.values(checks).every(Boolean),"self-check failed: "+JSON.stringify(checks));
 return {schema:"strong-mean-homotopy-self-check-v1",checks,all_checks_passed:true,
  execution:"Pure BigInt rational interval algebra; no actual field boxes, RHS, tail or BVP.",
  fixture_result:result,nonzero_fixture_result:varied,physical_RHS_calls:0,tail_workers:0,newton_solves:0};
}
const api={SCHEMA,Q,I,readI,velocityJets,evaluateInput,selfCheck};
if(typeof module!=="undefined")module.exports=api;
if(typeof require!=="undefined"&&typeof module!=="undefined"&&require.main===module){
 const fs=require("node:fs"),crypto=require("node:crypto"),args=process.argv.slice(2);
 const take=flag=>{const i=args.indexOf(flag);return i<0?null:args[i+1];};
 const out=take("--out");assert(out,"--out is required");assert(!fs.existsSync(out),"fresh output required");
 let result,inputBytes=null;
 if(args.includes("--self-check"))result=selfCheck();
 else{const input=take("--input");assert(input,"--input or --self-check required");inputBytes=fs.readFileSync(input);result=evaluateInput(JSON.parse(inputBytes.toString("utf8")),Number(take("--sqrt-bits")||96));}
 result.source_sha256=crypto.createHash("sha256").update(fs.readFileSync(__filename)).digest("hex");
 if(inputBytes)result.input_sha256=crypto.createHash("sha256").update(inputBytes).digest("hex");
 const data=JSON.stringify(result,null,2)+"\n";assert(Buffer.byteLength(data)<5000000,"result exceeds repository size limit");
 fs.writeFileSync(out,data,{flag:"wx"});
 process.stdout.write(JSON.stringify({event:"mean_homotopy_complete",out,actual_prefix_C2_certificate:false,checks:result.checks||null})+"\n");
}
