/* R196: simple nonuniform cubic B-splines and exact Boehm refinement.
 * Normalized knots are exact rationals 0=t0<...<tm=1. Finite bases have
 * compact support [ti,ti+4] and their zero extensions are C2.
 * Stored binary64 coefficient rounding and numerical evaluation are distinct.
 */
"use strict";
function createR196CubicSplines(){
  const abs=x=>x<0n?-x:x;
  function gcd(a,b){a=abs(a);b=abs(b);while(b){const r=a%b;a=b;b=r;}return a;}
  function F(n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return[n/g,d/g];}
  const Z=F(0),O=F(1);
  const add=(a,b)=>F(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
  const neg=a=>[-a[0],a[1]],sub=(a,b)=>add(a,neg(b));
  const mul=(a,b)=>F(a[0]*b[0],a[1]*b[1]),div=(a,b)=>F(a[0]*b[1],a[1]*b[0]);
  const cmp=(a,b)=>{const x=a[0]*b[1]-b[0]*a[1];return x<0n?-1:x>0n?1:0;};
  const max=(a,b)=>cmp(a,b)>0?a:b,ar=a=>F(abs(a[0]),a[1]);
  const show=a=>a.map(String);
  function binary64(x){
    if(!Number.isFinite(x))throw Error("nonfinite coefficient/knot");if(x===0)return Z;
    const d=new DataView(new ArrayBuffer(8));d.setFloat64(0,x,false);
    const h=d.getUint32(0,false),l=d.getUint32(4,false),e=(h>>>20)&2047;
    let m=(BigInt(h&1048575)<<32n)+BigInt(l);if(e)m+=1n<<52n;if(h>>>31)m=-m;
    const p=e?e-1075:-1074;return p>=0?F(m<<BigInt(p)):F(m,1n<<BigInt(-p));
  }
  function R(v){
    if(typeof v==="number")return binary64(v);
    if(typeof v==="bigint")return F(v);
    if(typeof v==="string"){const a=v.split("/");if(a.length>2)throw Error("invalid rational");return F(a[0],a.length===2?a[1]:1);}
    if(Array.isArray(v)&&v.length===2)return F(v[0],v[1]);
    throw Error("rational string, pair or binary64 required");
  }
  function nearest(a){
    if(a[0]===0n)return 0;const sign=a[0]<0n?-1:1,n=abs(a[0]),d=a[1];
    let e=n.toString(2).length-d.toString(2).length;
    if(e>=0?n<(d<<BigInt(e)):(n<<BigInt(-e))<d)e--;
    const scale=e>=-1022?52-e:1074;
    const nn=scale>=0?n<<BigInt(scale):n,dd=scale>=0?d:d<<BigInt(-scale);
    let q=nn/dd;const r=nn%dd,twice=2n*r;
    if(twice>dd||(twice===dd&&(q&1n)))q++;
    const v=Number(q)*2**(e>=-1022?e-52:-1074);
    if(!Number.isFinite(v))throw Error("rounded rational outside binary64");return sign*v;
  }
  function knots(input){
    if(!Array.isArray(input)||input.length<5)throw Error("at least five simple knots required");
    const t=input.map(R);if(cmp(t[0],Z)!==0||cmp(t[t.length-1],O)!==0)throw Error("end knots must be exactly 0 and 1");
    for(let i=1;i<t.length;i++)if(cmp(t[i-1],t[i])>=0)throw Error("knots must be strictly ordered; repeated knots change C2");
    return t;
  }
  function uniformKnots(J){
    if(!Number.isInteger(J)||J<1)throw Error("positive integer basis count required");
    return Array.from({length:J+4},(_,i)=>show(F(i,J+3)));
  }
  function createBasis(input){
    const t=knots(input),J=t.length-4,m=t.length-1,tf=t.map(nearest);
    const floatingKnotsDistinct=tf.every((x,i)=>i===0||x>tf[i-1]);
    function exactJets(value){
      const q=R(value);
      if(cmp(q,Z)<0||cmp(q,O)>=0)return{indices:[],value:[],first:[],second:[],q:show(q)};
      let lo=0,hi=m;
      while(lo+1<hi){const mid=(lo+hi)>>1;if(cmp(t[mid],q)<=0)lo=mid;else hi=mid;}
      const k=lo;let old=new Map([[k,[O,Z,Z]]]);
      for(let p=1;p<=3;p++){
        const next=new Map();
        for(let i=Math.max(0,k-p);i<=Math.min(k,m-p-1);i++){
          const a=old.get(i)||[Z,Z,Z],b=old.get(i+1)||[Z,Z,Z];
          const denA=sub(t[i+p],t[i]),denB=sub(t[i+p+1],t[i+1]),pr=F(p);
          const n=add(mul(div(sub(q,t[i]),denA),a[0]),mul(div(sub(t[i+p+1],q),denB),b[0]));
          const d=sub(mul(div(pr,denA),a[0]),mul(div(pr,denB),b[0]));
          const dd=sub(mul(div(pr,denA),a[1]),mul(div(pr,denB),b[1]));
          if(n[0]||d[0]||dd[0])next.set(i,[n,d,dd]);
        }
        old=next;
      }
      const indices=[...old.keys()];
      return {indices,value:indices.map(i=>show(old.get(i)[0])),first:indices.map(i=>show(old.get(i)[1])),
        second:indices.map(i=>show(old.get(i)[2])),q:show(q)};
    }
    function jets(q){
      if(!Number.isFinite(q))throw Error("nonfinite evaluation coordinate");
      if(!floatingKnotsDistinct)throw Error("exact knots collide after binary64 conversion; use exactJets or more precision");
      if(q<0||q>=1)return{indices:[],value:[],first:[],second:[],q};
      let lo=0,hi=m;while(lo+1<hi){const mid=(lo+hi)>>1;if(tf[mid]<=q)lo=mid;else hi=mid;}
      const k=lo;let old=new Map([[k,[1,0,0]]]);
      for(let p=1;p<=3;p++){
        const next=new Map();
        for(let i=Math.max(0,k-p);i<=Math.min(k,m-p-1);i++){
          const a=old.get(i)||[0,0,0],b=old.get(i+1)||[0,0,0];
          const da=tf[i+p]-tf[i],db=tf[i+p+1]-tf[i+1];
          const n=(q-tf[i])/da*a[0]+(tf[i+p+1]-q)/db*b[0];
          const d=p/da*a[0]-p/db*b[0],dd=p/da*a[1]-p/db*b[1];
          if(n!==0||d!==0||dd!==0)next.set(i,[n,d,dd]);
        }
        old=next;
      }
      const indices=[...old.keys()];
      return{indices,value:indices.map(i=>old.get(i)[0]),first:indices.map(i=>old.get(i)[1]),second:indices.map(i=>old.get(i)[2]),q};
    }
    function physicalJets(s,c,S){
      if(!Number.isFinite(s)||!Number.isFinite(c)||!Number.isFinite(S)||!(S>c))throw Error("finite positive physical span required");
      if(s<=c||s>=S)return{indices:[],value:[],first:[],second:[],q:s<=c?0:1};
      const L=S-c,r=jets((s-c)/L);return{...r,first:r.first.map(x=>x/L),second:r.second.map(x=>x/(L*L))};
    }
    function exactPhysicalJets(s,c,S){
      const sr=R(s),cr=R(c),Sr=R(S),L=sub(Sr,cr);if(cmp(L,Z)<=0)throw Error("positive exact physical span required");
      const q=div(sub(sr,cr),L),r=exactJets(show(q));
      return{...r,first:r.first.map(x=>show(div(R(x),L))),second:r.second.map(x=>show(div(R(x),mul(L,L))))};
    }
    return{schema:"fd2d-R196-simple-cubic-basis-v1",degree:3,count:J,knots:t.map(show),knotNumbers:tf,
      floatingKnotsDistinct,maxActive:4,jets,exactJets,physicalJets,exactPhysicalJets,
      definition:{coordinate:"q=(s-c)/(S-c)",support:"basis i on [t_i,t_(i+4)]",endpoint_extension:"zero C2",knots_exact:true}};
  }
  function insertionMatrix(input,value){
    const t=knots(input),q=R(value),J=t.length-4;
    if(cmp(q,Z)<=0||cmp(q,O)>=0)throw Error("inserted knot must be strictly inside (0,1)");
    let k=0;while(k+1<t.length&&cmp(t[k+1],q)<0)k++;
    if(cmp(t[k],q)===0||cmp(t[k+1],q)===0)throw Error("knot already present; no multiplicity increase");
    const rows=[];
    for(let i=0;i<=J;i++){
      let entries=[];
      if(i<=k-3)entries=[[i,O]];
      else if(i>=k+1)entries=[[i-1,O]];
      else{
        const alpha=div(sub(q,t[i]),sub(t[i+3],t[i]));
        if(i<J&&alpha[0])entries.push([i,alpha]);
        const beta=sub(O,alpha);if(i>0&&beta[0])entries.push([i-1,beta]);
      }
      entries.sort((a,b)=>a[0]-b[0]);
      const mass=entries.reduce((a,e)=>add(a,e[1]),Z);
      if(cmp(mass,Z)<0||cmp(mass,O)>0||entries.some(e=>cmp(e[1],Z)<0))throw Error("internal Boehm coefficient error");
      rows.push({old_indices:entries.map(e=>e[0]),weights:entries.map(e=>show(e[1])),row_mass:show(mass)});
    }
    const nt=[...t.slice(0,k+1),q,...t.slice(k+1)];
    return{schema:"fd2d-R196-exact-cubic-Boehm-insertion-v1",degree:3,old_count:J,new_count:J+1,
      old_knots:t.map(show),new_knots:nt.map(show),inserted_knot:show(q),old_span:k,rows,
      missing_outside_coefficients_are_zero:true};
  }
  function coefficientRows(rows,J){
    if(!Array.isArray(rows)||rows.length!==J||!rows.length||!Array.isArray(rows[0])||!rows[0].length)
      throw Error("coefficient rows [basis][channel] required");
    const K=rows[0].length;
    if(rows.some(r=>!Array.isArray(r)||r.length!==K))throw Error("inconsistent channel count");
    return rows.map(r=>r.map(R));
  }
  function applyExact(matrix,c){
    const channels=c[0].length;
    return matrix.rows.map(row=>Array.from({length:channels},(_,h)=>row.old_indices.reduce((sum,j,k)=>add(sum,mul(R(row.weights[k]),c[j][h])),Z)));
  }
  function derivativeCoefficients(c,t,degree){
    const K=c[0].length,zero=Array.from({length:K},()=>Z),out=[];
    for(let i=0;i<=c.length;i++){
      const right=i<c.length?c[i]:zero,left=i>0?c[i-1]:zero,scale=div(F(degree),sub(t[i+degree],t[i]));
      out.push(right.map((v,k)=>mul(scale,sub(v,left[k]))));
    }
    return out;
  }
  function prolongCoefficients(input,rows,inserted){
    let t=knots(input),c=coefficientRows(rows,t.length-4);
    const inputCoefficientsExact=c.map(row=>row.map(show)),steps=[];
    if(!Array.isArray(inserted))throw Error("explicit ordered inserted-knot array required");
    for(const q of inserted){
      const M=insertionMatrix(t.map(show),q);c=applyExact(M,c);t=M.new_knots.map(R);steps.push(M);
    }
    const rounded=c.map(row=>row.map(nearest)),err=c.map((row,i)=>row.map((v,k)=>sub(binary64(rounded[i][k]),v)));
    const d1=derivativeCoefficients(err,t,3),d2=derivativeCoefficients(d1,t,2);
    const bound=table=>table[0].map((_,h)=>show(table.reduce((v,row)=>max(v,ar(row[h])),Z)));
    return{schema:"fd2d-R196-simple-cubic-prolongation-v1",old_count:rows.length,new_count:c.length,channels:c[0].length,
      old_knots:knots(input).map(show),new_knots:t.map(show),insertions:steps,input_coefficients_exact:inputCoefficientsExact,
      coefficients_exact:c.map(row=>row.map(show)),coefficients_binary64:rounded,
      coefficient_roundoff_exact:err.map(row=>row.map(show)),
      stored_spline_roundoff_bounds:{coordinate:"normalized q; numerical basis evaluation excluded",
        value_per_channel:bound(err),first_per_channel:bound(d1),second_per_channel:bound(d2),
        reason:"each finite lower-degree nonnegative B-spline family has total mass <=1"},
      exact_real_field_preserved:true,binary64_field_claimed_bitwise_equal:false,
      intermediate_rounding:false,rounding_mode:"nearest binary64, ties to even"};
  }
  function evaluateExact(knotsInput,rows,q){
    const b=createBasis(knotsInput),c=coefficientRows(rows,b.count),j=b.exactJets(q),K=c[0].length;
    const sum=key=>Array.from({length:K},(_,h)=>show(j.indices.reduce((v,i,k)=>add(v,mul(c[i][h],R(j[key][k]))),Z)));
    return{value:sum("value"),first:sum("first"),second:sum("second"),active:j.indices};
  }
  return{uniformKnots,createBasis,insertionMatrix,prolongCoefficients,evaluateExact};
}
if(typeof module!=="undefined"&&module.exports)module.exports={createR196CubicSplines};
