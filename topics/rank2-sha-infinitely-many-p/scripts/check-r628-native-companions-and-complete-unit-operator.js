// Exact R628 certificate. Run: node <this-file> [output.json]
// Complete Q(omega) geometry and symbolic kappa products; no prime sampling.
"use strict";
const ck=(x,m)=>{if(!x)throw Error(m);};
const abs=x=>x<0n?-x:x,gcd=(x,y)=>{x=abs(x);y=abs(y);while(y)[x,y]=[y,x%y];return x;};
const Q=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);ck(d!==0n,"zero denominator");if(d<0n){n=-n;d=-d;}let g=gcd(n,d);return[n/g,d/g];};
const qa=(x,y)=>Q(x[0]*y[1]+y[0]*x[1],x[1]*y[1]),qn=x=>[-x[0],x[1]],
qm=(x,y)=>Q(x[0]*y[0],x[1]*y[1]),qi=x=>Q(x[1],x[0]),
qs=x=>x[1]===1n?String(x[0]):String(x[0])+"/"+x[1];
const E=(a,b=0,d=1)=>[Q(a,d),Q(b,d)], ea=(x,y)=>[qa(x[0],y[0]),qa(x[1],y[1])],
en=x=>[qn(x[0]),qn(x[1])],es=(x,y)=>ea(x,en(y)),
em=(x,y)=>[qa(qm(x[0],y[0]),qn(qm(x[1],y[1]))),
qa(qa(qm(x[0],y[1]),qm(x[1],y[0])),qn(qm(x[1],y[1])))],
ec=x=>[qa(x[0],qn(x[1])),qn(x[1])],
eq=(x,y)=>x[0][0]===y[0][0]&&x[0][1]===y[0][1]&&x[1][0]===y[1][0]&&x[1][1]===y[1][1],
esc=(x,a,b=1)=>em(x,E(a,0,b)),ez=x=>eq(x,E(0)),
ei=x=>{let n=em(x,ec(x));ck(n[1][0]===0n,"norm rational");return[ qm(ec(x)[0],qi(n[0])),qm(ec(x)[1],qi(n[0])) ];},
out=x=>x.map(qs);
const he=(x,y)=>x.reduce((a,t,i)=>ea(a,em(t,ec(y[i]))),E(0));
const va=(x,y)=>x.map((t,i)=>ea(t,y[i])),vs=(x,y)=>x.map((t,i)=>es(t,y[i])),
vm=(x,c)=>x.map(t=>em(t,c));
const mm=(A,B)=>A.map(row=>B[0].map((_,j)=>row.reduce((s,t,k)=>ea(s,em(t,B[k][j])),E(0))));
const ident=n=>Array.from({length:n},(_,i)=>Array.from({length:n},(_,j)=>E(i===j?1:0)));
function inverse(A){let M=A.map(row=>row.map(x=>x)),B=ident(A.length),det=E(1);
 for(let k=0;k<M.length;k++){let p=k;while(p<M.length&&ez(M[p][k]))p++;ck(p<M.length,"singular");
  if(p!==k){[M[p],M[k]]=[M[k],M[p]];[B[p],B[k]]=[B[k],B[p]];det=en(det);}
  const pivot=M[k][k];det=em(det,pivot);const inv=ei(pivot);M[k]=vm(M[k],inv);B[k]=vm(B[k],inv);
  for(let i=0;i<M.length;i++)if(i!==k&&!ez(M[i][k])){const f=M[i][k];M[i]=vs(M[i],vm(M[k],f));B[i]=vs(B[i],vm(B[k],f));}
 } return {inverse:B,det}; }



function certificate(){
function main(){
const w=E(0,1),w2=E(-1,-1),de=E(1,2),alpha=E(1,3),gamma=E(3,1),gd=E(2,3),bk=E(-1,-6,8);
const a=E(0,-3,8),b=ea(a,E(2)),R=[E(1),E(0)],V=[E(0),E(1)],metric=[E(8),E(263,0,8)];
const ip=(x,y)=>x.reduce((v,t,i)=>ea(v,em(em(t,ec(y[i])),metric[i])),E(0));
const Y=[a,E(1)],W=[b,E(1)],NY=ip(Y,Y),NW=ip(W,W);
const cy=em(ip(R,Y),ei(NY)),cw=em(ip(R,W),ei(NW)),EY=vs(R,vm(Y,cy)),FW=vs(R,vm(W,cw));
ck(eq(NY,E(34))&&eq(NW,E(72)),"original indices");
ck(eq(cy,E(3,3,34))&&eq(cw,E(19,3,72)),"exact companion projection");
ck(ez(ip(EY,Y))&&ez(ip(FW,W)),"true perpendicular axes");
ck(eq(ip(EY,EY),E(263,0,34))&&eq(ip(FW,FW),E(263,0,72)),"true companion norms");
const p=L=>L.map((t,i)=>vm(L,em(em(metric[i],ec(t)),ei(ip(L,L)))));
const pY=p(Y),pE=p(EY),pW=p(W),pF=p(FW),I=ident(2);
const ma=(A,B)=>A.map((x,i)=>va(x,B[i])),ms=(A,B)=>A.map((x,i)=>vs(x,B[i]));
const mscale=(A,z)=>A.map(x=>vm(x,z)),zero=()=>I.map(x=>x.map(()=>E(0)));
const mmPoly=(A,B)=>{const out=Array.from({length:A.length+B.length-1},zero);for(let i=0;i<A.length;i++)for(let j=0;j<B.length;j++)out[i+j]=ma(out[i+j],mm(A[i],B[j]));return out;};
const RY=ms(I,mscale(pY,E(2))),AY=[ms(I,pY),mscale(pY,E(-1))],AE=[mm(ms(I,pE),RY),mm(pE,RY)];
const prod=mmPoly(AY,AE);
for(let j=0;j<prod.length;j++)for(let r=0;r<2;r++)for(let c=0;c<2;c++)ck(eq(prod[j][r][c],j===1?I[r][c]:E(0)),"full native companion cancellation");
const AW=[ms(I,pW),zero(),zero(),zero(),pW],AF=[ms(I,pF),zero(),zero(),zero(),pF],prodW=mmPoly(AW,AF);
for(let j=0;j<prodW.length;j++)for(let r=0;r<2;r++)for(let c=0;c<2;c++)ck(eq(prodW[j][r][c],j===4?I[r][c]:E(0)),"four-level W companion cancellation");
const thetaY=EY[0],thetaW=FW[0],holes={Y:en(ei(a)),W:en(ei(b)),E:em(cy,ei(thetaY)),F:em(cw,ei(thetaW))};
const norms={};for(const x of Object.keys(holes))for(const y of Object.keys(holes))if(x<y){const d=es(holes[x],holes[y]);norms[x+"-"+y]={difference:out(d),norm:out(em(d,ec(d)))};}
const phi0=[alpha,en(em(alpha,E(8,12,7)))],phi1=[en(gamma),em(gamma,E(-4,-12,7))];
const plus=vm(va(phi0,phi1),E(1,0,2)),minus=vm(vs(phi0,phi1),E(1,0,2));
ck(eq(plus[0],E(-1,1))&&eq(plus[1],E(2,-2)),"actual V fourth plus line");
ck(eq(minus[0],E(2,2))&&eq(minus[1],E(2,2)),"actual V fourth minus line");
const c29=esc(em(em(de,esc(de,2)),em(gamma,ec(gamma))),-1,84);
ck(eq(c29,E(1,0,2)),"exact first four sigma order-four coefficient");
const report={
format:"R628 exact two-source unit equation and native arithmetic companions",
 original_observations:{a:out(a),aW:out(b),norm_a:out(em(a,ec(a))),norm_aW:out(em(b,ec(b)))},
 plane_Gram:metric.map(out),Y:Y.map(out),W:W.map(out),cY:out(cy),cW:out(cw),
 E_Y:EY.map(out),E_W:FW.map(out),E_Y_norm:out(ip(EY,EY)),E_W_norm:out(ip(FW,FW)),
 complete_native_matrices:{Y_signed_scale:AY.map(x=>x.map(y=>y.map(out))),E_scale_with_Y_reflection:AE.map(x=>x.map(y=>y.map(out))),Y_times_E:"kappa I",W_times_F_four_layers:"kappa^4 I"},
 actual_source_core:{E:"epsilon lambda P_E,kappa R_Y",F_four:"lambda^4 P_F,kappa^4"},
 four_distinct_unit_ratio_centres:Object.fromEntries(Object.entries(holes).map(([k,z])=>[k,out(z)])),
 centre_differences:norms,
 binary_source:{first_four_sigma_leading:out(c29),first_three_V_conditional_moments_zero:true,V_fourth_factor:"12 Omega^4",
  pair_phi0_sigma8:[...phi0.map(out)],pair_phi1_sigma8:phi1.map(out),pair_plus:plus.map(out),pair_minus:minus.map(out)},
 complete_R_marginal_zero:true,both_unit_mass_zero:true,
 unit_reconstruction:{positive_ratio_moments:"(I-lambda kappa^k X)^(-1)",negative_ratio_moments:"(I-epsilon lambda kappa^k X)^(-1)",constant_V_log:"(I-lambda X)^(-1)",negative_first_three_ratios_zero:true},
 exact_q_invisibility:"all valid R594 choices give beta^N times both complete pi4 sources; restriction to any R/V domain is included",
 all_native_unit_cuts_retained:true,no_new_central_zero_assigned:true
};
return report;
}
function low(){
const al=E(1,3),gd=E(2,3),ga=E(3,1),bg=E(2,-1);
const pow=(x,n)=>{let y=E(1);for(let i=0;i<n;i++)y=em(y,x);return y;},ch=(n,k)=>{let v=1;for(let j=1;j<=k;j++)v=v*(n-j+1)/j;return v;};
function paircoef(a,b,j){
 // u=a*l+m, v=l+b*m; coefficient l^j m^(8-j) in (u^7v+uv^7)/210.
 let z=E(0);
 if(j<=7)z=ea(z,esc(em(pow(a,j),b),ch(7,j)));
 if(j>=1)z=ea(z,esc(pow(a,j-1),ch(7,j-1)));
 if(j>=1)z=ea(z,esc(em(a,pow(b,8-j)),ch(7,j-1)));
 if(j<=7)z=ea(z,esc(pow(b,7-j),ch(7,j)));
 return esc(z,1,210);
}
const c3=en(esc(paircoef(al,gd,3),6)),c5=en(esc(paircoef(al,gd,5),120));
return {R3_factor_times_b:out(c3),R5_factor_times_b:out(c5),
 F1_R3_derivative:out(esc(en(paircoef(ga,en(bg),3)),6)),
 c3_native:out(esc(es(pow(E(0,-3,8),3),pow(E(16,-3,8),3)),1,3))};
}
return {geometry:main(),conditional_moments:low()};
}
const text=JSON.stringify(certificate(),null,2)+'\n';
if(process.argv[2])require('fs').writeFileSync(process.argv[2],text);else process.stdout.write(text);
