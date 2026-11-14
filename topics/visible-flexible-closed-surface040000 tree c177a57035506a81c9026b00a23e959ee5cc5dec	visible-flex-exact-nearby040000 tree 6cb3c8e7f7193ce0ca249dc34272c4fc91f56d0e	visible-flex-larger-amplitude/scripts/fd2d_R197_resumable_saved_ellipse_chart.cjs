/* New independent execution adapter for frozen R197.
 * Every arithmetic expression of the original local/whole Taylor recurrence
 * and the material/geometric jet consumers is retained. No perimeter solve.
 * Resumption trusts the declared actual completed packets after exact source,
 * mathematical-binding, ordered-row and SHA checks; a checksum is transport,
 * not a replacement for the R197 analytic proof or an authentication claim.
 */
function utf8(s){const a=[];for(const c of s){let n=c.codePointAt(0);if(n<128)a.push(n);else if(n<2048)a.push(192|(n>>6),128|(n&63));else if(n<65536)a.push(224|(n>>12),128|((n>>6)&63),128|(n&63));else a.push(240|(n>>18),128|((n>>12)&63),128|((n>>6)&63),128|(n&63));}return a;}
function sha256(s){const b=utf8(s),bitlen=b.length*8;b.push(128);while(b.length%64!==56)b.push(0);const hi=Math.floor(bitlen/4294967296),lo=bitlen>>>0;for(let k=3;k>=0;k--)b.push((hi>>>(k*8))&255);for(let k=3;k>=0;k--)b.push((lo>>>(k*8))&255);
const K=[1116352408,1899447441,3049323471,3921009573,961987163,1508970993,2453635748,2870763221,3624381080,310598401,607225278,1426881987,1925078388,2162078206,2614888103,3248222580,3835390401,4022224774,264347078,604807628,770255983,1249150122,1555081692,1996064986,2554220882,2821834349,2952996808,3210313671,3336571891,3584528711,113926993,338241895,666307205,773529912,1294757372,1396182291,1695183700,1986661051,2177026350,2456956037,2730485921,2820302411,3259730800,3345764771,3516065817,3600352804,4094571909,275423344,430227734,506948616,659060556,883997877,958139571,1322822218,1537002063,1747873779,1955562222,2024104815,2227730452,2361852424,2428436474,2756734187,3204031479,3329325298],H=[1779033703,3144134277,1013904242,2773480762,1359893119,2600822924,528734635,1541459225];const r=(x,n)=>(x>>>n)|(x<<(32-n));for(let off=0;off<b.length;off+=64){let w=Array(64);for(let i=0;i<16;i++)w[i]=((b[off+4*i]<<24)|(b[off+4*i+1]<<16)|(b[off+4*i+2]<<8)|b[off+4*i+3])>>>0;for(let i=16;i<64;i++){const x=w[i-15],y=w[i-2];w[i]=(w[i-16]+(r(x,7)^r(x,18)^(x>>>3))+w[i-7]+(r(y,17)^r(y,19)^(y>>>10)))>>>0;}let[a,c,d,e,f,g,h,j]=H;for(let i=0;i<64;i++){let t1=(j+(r(f,6)^r(f,11)^r(f,25))+((f&g)^(~f&h))+K[i]+w[i])>>>0,t2=((r(a,2)^r(a,13)^r(a,22))+((a&c)^(a&d)^(c&d)))>>>0;j=h;h=g;g=f;f=(e+t1)>>>0;e=d;d=c;c=a;a=(t1+t2)>>>0;}const v=[a,c,d,e,f,g,h,j];for(let i=0;i<8;i++)H[i]=(H[i]+v[i])>>>0;}return H.map(x=>x.toString(16).padStart(8,'0')).join('');}
function stableJSON(v){if(v===null||typeof v!=="object")return JSON.stringify(v);if(Array.isArray(v))return"["+v.map(stableJSON).join(",")+"]";return"{"+Object.keys(v).sort().map(k=>JSON.stringify(k)+":"+stableJSON(v[k])).join(",")+"}";}
/* R197: rigorous saved-axis ellipse material-angle chart.
 * Same exact ellipse and perimeter identity as the R187 normalization
 * certificate. A validated Taylor integration of its scalar inverse chart,
 * not a new surface equation. Uses the frozen R188 interval arithmetic.
 */
"use strict";
function createR197ResumableSavedEllipseChart(spec,arithmetic){
  const C=arithmetic||(require("./fd2d_R188_exact_quarter_primitive.cjs").createR188ExactPrimitive(160));
  const {F,add,sub,mul,div,cmp,pow,I,ip,ia,is,im,id,ine,scale,record}=C;
  const zero=F(0),one=F(1),two=F(2),iz=ip(zero),io=ip(one),Aq=C.quarterAngle;
  function R(x){if(Array.isArray(x)&&x.length===2)return F(x[0],x[1]);if(typeof x==="string"){const p=x.split("/");return F(p[0],p.length===2?p[1]:1);}throw Error("exact rational pair/string expected");}
  function decode(b){if(!b||!b.lower||!b.upper)throw Error("explicit exact interval required");return I(R(b.lower),R(b.upper));}
  const absF=a=>F(a[0]<0n?-a[0]:a[0],a[1]);
  const max=(a,b)=>cmp(a,b)>0?a:b,min=(a,b)=>cmp(a,b)<0?a:b;
  function square(x){if(cmp(x[0],zero)<=0&&cmp(x[1],zero)>=0)return I(zero,max(mul(x[0],x[0]),mul(x[1],x[1])));return im(x,x);}
  function integerSqrt(n){if(n<2n)return n;let x=1n<<BigInt(Math.ceil(n.toString(2).length/2));while(true){const y=(x+n/x)>>1n;if(y>=x)return x;x=y;}}
  function sqrt(x){
    if(cmp(x[0],zero)<0)throw Error("negative square-root interval");
    const q=1n<<BigInt(C.precision),q2=q*q;
    const lo=integerSqrt(x[0][0]*q2/x[0][1]);
    const nn=(x[1][0]*q2+x[1][1]-1n)/x[1][1];let hi=integerSqrt(nn);if(hi*hi<nn)hi++;
    return I(F(lo,q),F(hi,q));
  }
  function intersection(a,b){const l=max(a[0],b[0]),r=min(a[1],b[1]);if(cmp(l,r)>0)throw Error("certified bounds have empty intersection");return I(l,r);}
  function hull(a,b){return I(min(a[0],b[0]),max(a[1],b[1]));}
  const cert=spec.perimeter_certificate;
  if(spec.schema!=="fd2d-R197-saved-ellipse-material-chart-input-v1"||!spec.perimeter_certificate_identity||!cert||cert.schema!=="fd2d-R187-saved-binary-ellipse-normalization-certificate-v1"||cert.definition_kind!=="saved exact dyadic axes, followed by accurate target-a0/perimeter normalization")throw Error("explicit matching saved-axis perimeter certificate required");
  const ax=R(cert.axes.A),bx=R(cert.axes.B);
  if(cmp(ax,zero)<=0||cmp(bx,zero)<=0)throw Error("positive exact axes required");
  const mean=decode(cert.perimeter_mean_radius),nu=im(Aq,mean),D=sub(mul(ax,ax),mul(bx,bx)),bmin=min(ax,bx),bmax=max(ax,bx);
  const order=spec.taylor_order===undefined?16:spec.taylor_order,cells=spec.cells===undefined?32:spec.cells;
  if(!Number.isInteger(order)||order<2||order>48||!Number.isInteger(cells)||cells<1||cells>2048)throw Error("declare a finite Taylor order and partition");
  const derivativeUpper=div(nu[1],bmin),domainTheta=I(zero,Aq[1]);
  const actual=[ax,bx,mean[0],mean[1],Aq[0],Aq[1]].map(x=>x.map(String));
  function convolve(a,b,n){let v=iz;for(let j=0;j<=n;j++)v=ia(v,im(a[j],b[n-j]));return v;}
  function systemJet(thetaBox,n){
    const [ss,cc]=C.sincos(thetaBox);
    let ell2=ia(ip(mul(bx,bx)),scale(square(ss),D));
    ell2=intersection(ell2,I(mul(bmin,bmin),mul(bmax,bmax)));
    const vv=id(io,sqrt(ell2)),theta=[thetaBox],sine=[ss],cosine=[cc],inverseSpeed=[vv],v2=[],v4=[],sc=[];
    for(let k=0;k<n;k++){
      v2[k]=convolve(inverseSpeed,inverseSpeed,k);
      v4[k]=convolve(v2,v2,k);sc[k]=convolve(sine,cosine,k);
      theta[k+1]=scale(im(nu,inverseSpeed[k]),F(1,k+1));
      sine[k+1]=scale(im(nu,convolve(cosine,inverseSpeed,k)),F(1,k+1));
      cosine[k+1]=scale(im(nu,convolve(sine,inverseSpeed,k)),F(-1,k+1));
      inverseSpeed[k+1]=scale(im(nu,convolve(sc,v4,k)),div(F(-1),F(k+1)));
      inverseSpeed[k+1]=scale(inverseSpeed[k+1],D);
    }
    return {theta,sine,cosine,inverseSpeed};
  }
  function evaluateTaylor(coeff,rem,x){
    let value=iz;
    for(let k=coeff.length-1;k>=0;k--)value=ia(im(value,ip(x)),coeff[k]);
    return ia(value,scale(rem,pow(x,coeff.length)));
  }
  const rows=[];let leftTheta=iz,maximumNodeWidth=zero;
  const construction={schema:"fd2d-R197-resumable-construction-v1",
    source_math_sha256:"3ccca82923ac0ed4cebcd66cc912944e41565d8e27567e0bd08f684a029ff79f",
    arithmetic_sha256:"5c04a135eed859a6d6d583877e53681cdc1dddc6102c913152adfc1913a9f97e",
    source_path:"scripts/fd2d_R197_resumable_saved_ellipse_chart.cjs",
    method:"Unchanged R197 whole-cell Taylor recurrence; only explicit incremental execution and hashed checkpoints are added"};
  const mathBinding={construction,axes:cert.axes,perimeter_certificate_identity:spec.perimeter_certificate_identity,
    mean_radius_enclosure:record(mean),quarter_angle:record(Aq),order,cells,precision_bits:C.precision,
    target_mean_radius_identity:spec.target_mean_radius_identity||null};
  const bindingHash=sha256(stableJSON(mathBinding)),rowHashes=[];
  function encodeRow(r,before=false){
    const out={left:r.left.map(String),right:r.right.map(String),
      theta_left:record(r.theta_left),theta_right:record(r.theta_right),apriori_theta:record(r.apriori_theta),
      coefficients:Object.fromEntries(Object.entries(r.coefficients).map(([k,v])=>[k,v.map(record)])),
      remainder:Object.fromEntries(Object.entries(r.remainder).map(([k,v])=>[k,record(v)]))};
    if(before)out.theta_right_before_endpoint_identity=record(r.theta_right_before_endpoint_identity);
    return out;
  }
  function restoreCheckpoint(checkpoint){
    if(checkpoint.schema!=="fd2d-R197-incremental-checkpoint-v1"||
       checkpoint.binding_sha256!==bindingHash||stableJSON(checkpoint.binding)!==stableJSON(mathBinding))throw Error("Checkpoint mathematical binding differs");
    if(!Array.isArray(checkpoint.rows)||checkpoint.rows.length>cells||
       checkpoint.rows.length!==checkpoint.completed_cells||checkpoint.row_hashes?.length!==checkpoint.rows.length)throw Error("Invalid complete-row count");
    let previous=bindingHash;
    for(let j=0;j<checkpoint.rows.length;j++){
      const raw=checkpoint.rows[j],h=sha256(previous+"\n"+stableJSON(raw));
      if(checkpoint.row_hashes[j]!==h)throw Error("Complete row checksum differs at "+j);
      const row={left:R(raw.left),right:R(raw.right),theta_left:decode(raw.theta_left),
        theta_right:decode(raw.theta_right),apriori_theta:decode(raw.apriori_theta),
        theta_right_before_endpoint_identity:decode(raw.theta_right_before_endpoint_identity),
        coefficients:{},remainder:{}};
      if(cmp(row.left,F(j,cells))!==0||cmp(row.right,F(j+1,cells))!==0||
         cmp(row.theta_left[0],leftTheta[0])!==0||cmp(row.theta_left[1],leftTheta[1])!==0)throw Error("Checkpoint partition or theta trace differs at "+j);
      for(const key of ["theta","sine","cosine","inverseSpeed"]){
        if(!Array.isArray(raw.coefficients[key])||raw.coefficients[key].length!==order||!raw.remainder[key])throw Error("Missing complete Taylor channel at "+j);
        row.coefficients[key]=raw.coefficients[key].map(decode);row.remainder[key]=decode(raw.remainder[key]);
      }
      if(cmp(row.theta_right[0],leftTheta[0])<0||cmp(row.theta_right[1],Aq[1])>0)throw Error("Checkpoint node escaped exact monotone quarter domain");
      rows.push(row);rowHashes.push(h);previous=h;leftTheta=row.theta_right;
      maximumNodeWidth=max(maximumNodeWidth,sub(leftTheta[1],leftTheta[0]));
    }
    if(checkpoint.last_row_sha256!==(rowHashes.length?rowHashes.at(-1):bindingHash))throw Error("Checkpoint final row hash differs");
    if(cmp(R(checkpoint.maximum_node_width),maximumNodeWidth)!==0)throw Error("Checkpoint maximum width differs");
  }
  if(spec.checkpoint)restoreCheckpoint(spec.checkpoint);
  function advance(count=1){
    if(!Number.isInteger(count)||count<0)throw Error("Finite nonnegative step count required");
    const stop=Math.min(cells,rows.length+count);
    for(let j=rows.length;j<stop;j++){
    const left=F(j,cells),right=F(j+1,cells),dt=sub(right,left);
    const apriori=intersection(I(leftTheta[0],add(leftTheta[1],mul(derivativeUpper,dt))),domainTheta);
    const local=systemJet(leftTheta,order-1),whole=systemJet(apriori,order);
    const row={left,right,theta_left:leftTheta,apriori_theta:apriori,coefficients:local,remainder:{}};
    for(const key of Object.keys(local))row.remainder[key]=whole[key][order];
    let next=evaluateTaylor(local.theta,row.remainder.theta,dt);
    next=intersection(next,I(leftTheta[0],Aq[1]));
    row.theta_right_before_endpoint_identity=next;
    if(j===cells-1)next=intersection(next,Aq);
    row.theta_right=next;
    maximumNodeWidth=max(maximumNodeWidth,sub(next[1],next[0]));
    rows.push(row);leftTheta=next;
    const encoded=encodeRow(row,true),previous=rowHashes.length?rowHashes.at(-1):bindingHash;
    const hash=sha256(previous+"\n"+stableJSON(encoded));rowHashes.push(hash);
    if(typeof spec.progress==="function")spec.progress({completed_cells:j+1,total_cells:cells,row_sha256:hash,maximum_node_width:maximumNodeWidth.map(String)});
    }
    return progress();
  }
  function progress(){return{completed_cells:rows.length,total_cells:cells,complete:rows.length===cells,
    binding_sha256:bindingHash,last_row_sha256:rowHashes.length?rowHashes.at(-1):bindingHash,
    maximum_node_width:maximumNodeWidth.map(String)};}
  function checkpointState(){return{schema:"fd2d-R197-incremental-checkpoint-v1",binding:mathBinding,
    binding_sha256:bindingHash,completed_cells:rows.length,rows:rows.map(r=>encodeRow(r,true)),row_hashes:rowHashes.slice(),
    last_row_sha256:rowHashes.length?rowHashes.at(-1):bindingHash,maximum_node_width:maximumNodeWidth.map(String),
    complete:rows.length===cells,OS_process_created:false};}

  function thetaPoint(t){
    t=R(t);if(cmp(t,zero)<0||cmp(t,one)>0)throw Error("quarter normalized angle outside [0,1]");
    if(cmp(t,zero)===0)return iz;
    if(!rows.length||cmp(t,rows.at(-1).right)>0)throw Error("Query exceeds completed strict chart cells");
    if(cmp(t,one)===0)return Aq;
    if(cmp(t,rows.at(-1).right)===0)return rows.at(-1).theta_right;
    let j=Number((t[0]*BigInt(cells))/t[1]);if(j>=cells)j=cells-1;
    const row=rows[j],x=sub(t,row.left);
    return intersection(evaluateTaylor(row.coefficients.theta,row.remainder.theta,x),row.apriori_theta);
  }
  function thetaBox(left,right=left){
    left=R(left);right=R(right);if(cmp(left,right)>0)throw Error("reversed angle box");
    const l=thetaPoint(left),r=thetaPoint(right);
    return I(l[0],r[1]); // Exact monotonicity, not an interpolation assumption.
  }
  function materialJetBox(left,right=left,n=2){
    if(!Number.isInteger(n)||n<0||n>order)throw Error("requested jet order exceeds the complete available order");
    const t=thetaBox(left,right),j=systemJet(t,n),invA=id(io,Aq);
    let factor=io;const out={};
    for(const key of Object.keys(j))out[key]=[];
    for(let k=0;k<=n;k++){for(const key of Object.keys(j))out[key].push(record(im(j[key][k],factor)));factor=im(factor,invA);}
    return {schema:"fd2d-R197-material-ellipse-Taylor-jet-box-v1",query:{normalized_left:R(left).map(String),normalized_right:R(right).map(String)},coefficient_convention:"actual physical u derivatives divided by k factorial",jets:out,definition:definition()};
  }
  function geometricSeedBox(left,right=left){
    const tl=R(left),tr=R(right),theta=thetaBox(tl,tr),u=scale(Aq,one),ubox=im(Aq,I(tl,tr));
    let [st,ct]=C.sincos(theta);
    if(cmp(tl,tr)===0&&cmp(tl,zero)===0){st=iz;ct=io;}
    if(cmp(tl,tr)===0&&cmp(tl,one)===0){st=io;ct=iz;}
    let ell2=ia(ip(mul(bx,bx)),scale(square(st),D));ell2=intersection(ell2,I(mul(bmin,bmin),mul(bmax,bmax)));
    const inv=id(io,sqrt(ell2)),inv2=im(inv,inv),inv3=im(inv2,inv),inv6=im(inv3,inv3);
    const v=[scale(im(st,inv),neg(ax)),scale(im(ct,inv),bx)],jv=[ine(v[1]),v[0]];
    const beta=scale(im(mean,inv3),mul(ax,bx));
    const beta_u=scale(im(im(im(mean,mean),im(st,ct)),inv6),mul(F(-3),mul(mul(ax,bx),D)));
    const vu=jv.map(x=>im(beta,x)),vuu=jv.map((x,k)=>is(im(beta_u,x),im(square(beta),v[k])));
    let [su,cu]=C.sincos(ubox);
    if(cmp(tl,tr)===0&&cmp(tl,zero)===0){su=iz;cu=io;}
    if(cmp(tl,tr)===0&&cmp(tl,one)===0){su=io;cu=iz;}
    const eu=[ine(su),cu],cosDelta=intersection(ia(im(eu[0],v[0]),im(eu[1],v[1])),I(zero,one));
    const sinDelta=is(im(eu[0],v[1]),im(eu[1],v[0]));
    const halfCos=sqrt(scale(ia(io,cosDelta),F(1,2)));
    const h=id(sinDelta,halfCos),deltaU=is(beta,io);
    const hu=im(halfCos,deltaU),huu=ia(scale(im(h,square(deltaU)),F(-1,4)),im(halfCos,beta_u));
    return {schema:"fd2d-R197-complete-geometric-ellipse-seed-jet-box-v1",
      query:{normalized_left:tl.map(String),normalized_right:tr.map(String)},
      coordinates:"fixed physical material u = (pi/2)*normalized angle",
      theta:record(theta),u:record(ubox),
      normalized_curve:[record(id(scale(ct,ax),mean)),record(id(scale(st,bx),mean))],
      unit_tangent:v.map(record),unit_tangent_u:vu.map(record),unit_tangent_uu:vuu.map(record),
      tangent_turn_rate:record(beta),tangent_turn_rate_u:record(beta_u),
      cosine_delta:record(cosDelta),sine_delta:record(sinDelta),
      h:record(h),h_u:record(hu),h_uu:record(huu),
      branch_free_seed_horizontal_norm_squared_lower:["1","2"],
      definition:definition()};
  }
  function neg(a){return F(-a[0],a[1]);}
  function definition(){
    return {schema:"fd2d-R197-saved-ellipse-material-chart-definition-v1",
      axes:cert.axes,perimeter_certificate_identity:spec.perimeter_certificate_identity,
      perimeter_definition:cert.definition_kind,mean_radius_enclosure:record(mean),
      normalized_angle:"t=u/(pi/2), from 0 to 1 on the complete quarter",
      exact_chart:"dtheta/dt=(pi/2)*a_E/sqrt(A^2 sin(theta)^2+B^2 cos(theta)^2), theta(0)=0; theta(1)=pi/2",
      exact_problem_is_original_arclength_inverse:true,terms:order,cells,precision_bits:C.precision,
      frozen_arithmetic_source:{path:"scripts/fd2d_R188_exact_quarter_primitive.cjs",sha256:"5c04a135eed859a6d6d583877e53681cdc1dddc6102c913152adfc1913a9f97e"},
      a_priori_method:"ell>=min(A,B) and exact monotonic quarter domain",
      derivative_remainder:"complete polynomial ODE jet evaluated on the certified whole-cell theta enclosure",
      maximum_node_theta_enclosure_width:maximumNodeWidth.map(String),
      construction,completed_cells:rows.length,whole_quarter_complete:rows.length===cells,
      full_surface_or_B32_profile_certified:false};
  }
  function portablePackets(){
    if(rows.length!==cells)throw Error("A complete quarter portable packet requires every actual cell");
    return {definition:definition(),rows:rows.map(r=>encodeRow(r,false))};
  }
  return {definition,thetaPoint,thetaBox,materialJetBox,geometricSeedBox,portablePackets,advance,progress,checkpointState,arithmetic:C};
}
if(typeof module!=="undefined"&&module.exports)module.exports={createR197ResumableSavedEllipseChart};
