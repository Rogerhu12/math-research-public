#!/usr/bin/env node
// R509: complete original five-sigma joint, two pure-Y frames, and exact six-input T/U couplings.
// BigInt arithmetic verifies both the genuine descended axes and the nonzero hidden couplings.
const certificate = (() => {

const abs=x=>x<0n?-x:x;
function gcd(a,b){a=abs(a);b=abs(b);while(b){[a,b]=[b,a%b]}return a}
function q(a,b=1n){a=BigInt(a);b=BigInt(b);if(!b)throw Error("zero denominator");if(b<0n){a=-a;b=-b}const g=gcd(a,b);return[a/g,b/g]}
const add=(a,b)=>q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
const neg=a=>[-a[0],a[1]], sub=(a,b)=>add(a,neg(b));
const mul=(a,b)=>q(a[0]*b[0],a[1]*b[1]), div=(a,b)=>q(a[0]*b[1],a[1]*b[0]);
function pow(a,n){let r=q(1);for(;n;n>>=1,a=mul(a,a))if(n&1)r=mul(r,a);return r}
const eq=(a,b)=>a[0]===b[0]&&a[1]===b[1], qs=a=>a[1]===1n?String(a[0]):a[0]+"/"+a[1];
const c=(a=0,b=0)=>[Array.isArray(a)?a:q(a),Array.isArray(b)?b:q(b)];
const ca=(a,b)=>[add(a[0],b[0]),add(a[1],b[1])], cn=a=>[neg(a[0]),neg(a[1])], cs=(a,b)=>ca(a,cn(b));
const cm=(a,b)=>[sub(mul(a[0],b[0]),mul(q(3),mul(a[1],b[1]))),add(mul(a[0],b[1]),mul(a[1],b[0]))];
const cc=a=>[a[0],neg(a[1])], norm=a=>add(mul(a[0],a[0]),mul(q(3),mul(a[1],a[1])));
const ci=a=>[div(a[0],norm(a)),neg(div(a[1],norm(a)))], cd=(a,b)=>cm(a,ci(b));
const ce=(a,b)=>eq(a[0],b[0])&&eq(a[1],b[1]), cj=a=>({real:qs(a[0]),delta:qs(a[1])});
function cp(a,n){let r=c(1);for(;n;n>>=1,a=cm(a,a))if(n&1)r=cm(r,a);return r}
function dot(a,b){return a.map((x,i)=>cm(x,cc(b[i]))).reduce(ca,c())}
function mm(A,B){return A.map(row=>B[0].map((_,j)=>row.map((x,k)=>cm(x,B[k][j])).reduce(ca,c())))}

function cinv(A){
 const n=A.length,B=A.map((r,i)=>[...r,...r.map((_,j)=>c(i===j?1:0))]);
 for(let j=0;j<n;j++){
  let r=j;while(r<n&&ce(B[r][j],c()))r++;if(r===n)throw Error("singular");
  [B[j],B[r]]=[B[r],B[j]];const sc=ci(B[j][j]);B[j]=B[j].map(x=>cm(x,sc));
  for(let i=0;i<n;i++)if(i!==j){const t=B[i][j];B[i]=B[i].map((x,k)=>cs(x,cm(t,B[j][k])))}
 }
 return B.map(r=>r.slice(n));
}
function cdet(A){
 const B=A.map(r=>r.slice());let ans=c(1);
 for(let j=0;j<B.length;j++){
  let r=j;while(r<B.length&&ce(B[r][j],c()))r++;if(r===B.length)return c();
  if(r!==j){[B[j],B[r]]=[B[r],B[j]];ans=cn(ans)}
  const diag=B[j][j];ans=cm(ans,diag);
  for(let i=j+1;i<B.length;i++){const t=cd(B[i][j],diag);for(let k=j;k<B.length;k++)B[i][k]=cs(B[i][k],cm(t,B[j][k]))}
 }
 return ans;
}
const z=[c(0,1),c(0,2),c(q(5,2),q(1,2)),c(1),c(2)];
const v=[c(q(63,2),q(17,2)),c(9,-10),c(-17,14),c(22,12),c(17,-3)];
const r=[c(q(5,2),q(1,2)),c(0,2),c(q(9,2),q(3,2)),c(q(-3,2),q(1,2)),c(4)];
const az=dot(r,z),theta=c(q(71,2),q(-35,2));
const j=r.map((x,i)=>cd(cs(cm(c(27),x),cm(az,z[i])),c(2)));
const h=j.map((x,i)=>cd(cs(cm(c(137),x),cm(theta,v[i])),c(27)));
const k=v.map((x,i)=>cd(cs(cm(c(721),x),cm(cc(theta),h[i])),c(137)));
const first=[z,v,h],piv=[0,3,4],nonpiv=[1,2],D=first.map(row=>piv.map(a=>cc(row[a]))),Di=cinv(D);
const qrows=[];
for(const a of nonpiv){
 const rhs=first.map(row=>[cn(cc(row[a]))]),co=mm(Di,rhs).map(row=>row[0]);
 const row=Array.from({length:5},()=>c());piv.forEach((col,i)=>{row[col]=co[i]});row[a]=c(1);qrows.push(row);
}
const M=[...first,...qrows],Mi=cinv(M),gram=M.map(row=>M.map(other=>dot(row,other)));
for(let i=0;i<5;i++)for(let j0=0;j0<5;j0++)if(i!==j0&&(i<3||j0<3)&&!ce(gram[i][j0],c()))throw Error("cross term");
if(!ce(dot(j,j),c(4266))||!ce(dot(k,k),c(113918))||!ce(dot(j,k),c()))throw Error("even frame");
const C=[[cd(theta,c(137)),c(q(27,137))],[c(q(721,137)),cd(cn(cc(theta)),c(137))]];
const gram2=mm(mm(C,[[c(3699),c()],[c(),c(98777)]]),C[0].map((_,i)=>C.map(row=>cc(row[i]))));
if(!ce(gram2[0][0],c(4266))||!ce(gram2[1][1],c(113918))||!ce(gram2[0][1],c()))throw Error("two frame Gram");
const ds=cdet(M);
function primeDivisors(n){let x=abs(BigInt(n)),out=[];for(let a=2n;a*a<=x;a++)if(x%a===0n){out.push(String(a));while(x%a===0n)x/=a}if(x>1n)out.push(String(x));return out}
const bad=new Set();for(const A of [M,Mi])for(const row of A)for(const x of row)for(const y of x)for(const p of primeDivisors(y[1]))bad.add(p);
const cmInts={};for(const [name,row] of Object.entries({z,v,r,j,h,k})){
 cmInts[name]=row.map(x=>{const om=mul(q(2),x[1]),re=add(x[0],x[1]);if(om[1]!==1n||re[1]!==1n)throw Error("non CM integer "+name);return{a:String(re[0]),omega:String(om[0])}});
}
const geom={
 status:"exact original five-input joint geometry verified",
 alpha65:cj(az),theta:cj(theta),
 coefficients:Object.fromEntries(Object.entries({z,v,r,j,h,k}).map(([name,row])=>[name,row.map(cj)])),
 CM_integer_coefficients:cmInts,
 norms:{Z:27,V:3699,R:65,J:4266,H:98777,K:113918},
 full_frame:M.map(row=>row.map(cj)),full_frame_inverse:Mi.map(row=>row.map(cj)),
 full_gram:gram.map(row=>row.map(cj)),full_determinant:cj(ds),full_determinant_norm:qs(norm(ds)),
 pivot_columns:piv.map(i=>i+1),pivot_determinant:cj(cdet(first.map(row=>piv.map(i=>row[i])))),
 frame_denominator_bad_primes:[...bad].sort((a,b)=>Number(a)-Number(b)),
 even_companion_frame:C.map(row=>row.map(cj)),even_companion_determinant:cj(cdet(C)),
 common_odd_degree:2666979,
 common_odd_identity:"3699*Norm(gamma7 gamma103)=98777*Norm(3delta)=2666979",
 anchor_J:"Theta(3delta gamma79 z), Norm(3delta gamma79)=2133",
 anchor_K:"Theta(gamma7 gamma79 gamma103 z), Norm=56959",
 source_axes:"The complete source retains Z,V,H,Q1,Q2 and independent x; no two separate marginal lifts are identified."
};

const om=c(q(-1,2),q(1,2)),om2=cp(om,2),delta=c(0,1),gamma=c(q(5,2),q(1,2)),gb=cc(gamma);
const Hhad=[[1,1,1,1],[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]].map(row=>row.map(x=>c(q(x,2))));
const Ed=Array.from({length:4},(_,i)=>Array.from({length:4},(_,j)=>i===j?[c(1),om,om2,c(1)][i]:c()));
const Om=[[cn(om),c(),c(),c()],[c(),c(),om2,c()],[c(),c(),c(),om],[c(),c(1),c(),c()]];
const T4=mm(mm(Ed,Hhad),Om),T6=Array.from({length:6},(_,i)=>Array.from({length:6},(_,j)=>c(i===j?1:0)));
const selected=[0,2,3,4];for(let i=0;i<4;i++)for(let j0=0;j0<4;j0++)T6[selected[i]][selected[j0]]=T4[i][j0];
const Tcube=mm(mm(T6,T6),T6);for(let i=0;i<6;i++)for(let j0=0;j0<6;j0++)if(!ce(Tcube[i][j0],c(i===j0?1:0)))throw Error("T order");
const Wrow=[[delta,c(0,2),gamma,gb,c(0,3),c(4)]],W2=mm(Wrow,mm(T6,T6))[0];
for(let i=0;i<5;i++)if(!ce(W2[[0,1,2,4,5][i]],r[i]))throw Error("W2 actual five coefficients");
if(!ce(W2[3],c(2,1)))throw Error("W2 free coefficient");
const Crow=[[c(q(1,2)),c(),cd(om2,c(2)),cd(cn(om),c(2)),c(q(-1,2)),c()]],Ct=mm(Crow,T6)[0];
for(let i=0;i<6;i++)if(!ce(Ct[i],i===3?om2:c()))throw Error("C T");
const ga79=c(q(17,2),q(3,2)),ga103=c(10,1);
if(!eq(norm(ga79),q(79))||!eq(norm(ga103),q(103)))throw Error("CM norm");
const anchorJ=cm(c(0,3),ga79),anchorK=cm(cm(gamma,ga79),ga103);
if(!eq(norm(anchorJ),q(2133))||!eq(norm(anchorK),q(56959)))throw Error("anchor degrees");
const oddM=27n*7n*79n*103n*137n,ratio=1n+2n*oddM;
for(const N of [3699n,98777n,2666979n])if((ratio-1n)%(2n*N))throw Error("odd center");
for(const N of [4266n,113918n])if((ratio-(1n+N))%(2n*N))throw Error("even center");
const geom2={...geom,
 cyclic_three_T:T6.map(row=>row.map(cj)),W_T2:W2.map(cj),C_T:Ct.map(cj),
 gamma79:cj(ga79),gamma103:cj(ga103),theta_anchor_J:cj(anchorJ),theta_anchor_K:cj(anchorK),
 ratio_representative:String(ratio),ratio_modulus:String(4n*oddM),
 whole_odd_scalar_relation:"K98777 and K3699 have the same actual chi_V by their two nonzero pullbacks to odd level2666979",
 whole_even_scalar_relation:"K4266=K113918=-I by the displayed Theta anchors",
 remaining_two_companion_common_core:"lambda^2",
 complete_W2_margin:"-6 delta omega^2 T72"
};

const origCols=[0,1,2,4,5];
function embed(row){const a=Array.from({length:6},()=>c());for(let i=0;i<5;i++)a[origCols[i]]=row[i];return a}
const Frame6=[...M.slice(0,3).map(embed),Array.from({length:6},(_,i)=>c(i===3?1:0)),...M.slice(3).map(embed)];
const Frame6i=cinv(Frame6),Tnew=mm(mm(Frame6,T6),Frame6i);
const PCold=Array.from({length:6},(_,i)=>Array.from({length:6},(_,j0)=>cm(cc(Crow[0][i]),Crow[0][j0])));
const Uold=Array.from({length:6},(_,i)=>Array.from({length:6},(_,j0)=>cs(c(i===j0?1:0),cm(c(2),PCold[i][j0]))));
const Unew=mm(mm(Frame6,Uold),Frame6i),PCnew=mm(mm(Frame6,PCold),Frame6i);
const Wnew=mm(Wrow,Frame6i)[0],Cnew=mm(Crow,Frame6i)[0],Wp=mm(Wrow,T6)[0];
const Yold=[delta,c(0,2),gamma,gb,c(1),c(2)];
const axisRows={Y:Yold,W:Wrow[0],Wprime:Wp,W2,R:embed(r)};
const axisData={};
for(const [name,row] of Object.entries(axisRows)){
 const dest=mm([row],Frame6i)[0];
 if(!ce(dest[4],c())||!ce(dest[5],c()))throw Error("axis retains Q: "+name);
 axisData[name]=dest.map(cj);
 const nn=dot(row,row);
 const P=Array.from({length:6},(_,i)=>Array.from({length:6},(_,j0)=>cd(cm(cc(row[i]),row[j0]),nn)));
 const PN=mm(mm(Frame6,P),Frame6i);
 for(let i=0;i<6;i++)for(let j0=0;j0<6;j0++)if((i>=4||j0>=4)&&!ce(PN[i][j0],c()))throw Error("axis projector crosses Q: "+name);
}
if(ce(Cnew[4],c())||ce(Cnew[5],c()))throw Error("lost genuine C-Q cross");
if(Tnew.slice(0,4).every(row=>row.slice(4).every(x=>ce(x,c()))))throw Error("unexpected T descent");
for(let i=0;i<6;i++)if(!ce(ca(ca(Wrow[0][i],cm(om2,Wp[i])),cm(om,W2[i])),c()))throw Error("cyclic W linear relation");
return{...geom2,
 full_six_frame:Frame6.map(row=>row.map(cj)),
 full_six_frame_inverse:Frame6i.map(row=>row.map(cj)),
 actual_full_T_in_new_frame:Tnew.map(row=>row.map(cj)),
 actual_full_U_in_new_frame:Unew.map(row=>row.map(cj)),
 actual_full_C_projector_in_new_frame:PCnew.map(row=>row.map(cj)),
 four_input_axis_rows:axisData,C_in_full_new_frame:Cnew.map(cj),
 hidden_Q_fixed_by_T:false,hidden_Q_fixed_by_U:false,
 old_W_Y_Wprime_W2_R_have_no_Q_component:true,
 exact_cyclic_linear_relation:"W + omega^2 Wprime + omega W2 = 0",
 descent_statement:"Only the displayed Y/W/Wprime/W2/R axis operators descend directly. The four actual states descend via W and Wprime operators and inherit the same Q common core. T and U must retain their displayed nonzero hidden Q couplings."
};

})();
process.stdout.write(JSON.stringify(certificate, null, 2) + "\n");
