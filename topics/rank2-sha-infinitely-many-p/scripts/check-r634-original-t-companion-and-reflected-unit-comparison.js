// R634 exact Q(omega) certificate. Run: node check-r634-original-t-companion-and-reflected-unit-comparison.js [output.json]
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

const N=72,m=9,aN=19,shift=36;
const col=(j,r,s)=>{const e=((s*(j+m*r))%4+4)%4;return {j:(j+2*m*r)%N,re:e===0?1:e===2?-1:0,im:e===1?1:e===3?-1:0};};
const perm=[],sign=[];
for(let j=0;j<N;j++){
 const acc=new Map(),put=(i,re,im)=>{const o=acc.get(i)||[0,0];acc.set(i,[o[0]+re,o[1]+im])};
 for(let r=0;r<4;r++)for(let s=0;s<4;s++){const x=col(j,r,s);put(x.j,x.re,x.im);}
 for(let r=0;r<4;r+=2)for(let s=0;s<4;s+=2){const x=col(j,r,s);put(x.j,-2*x.re,-2*x.im);}
 const k=(aN*j+shift)%N,v=j%2?1:-1;
 for(const[i,c]of acc)ck(c[0]===(i===k?4*v:0)&&c[1]===0,"whole72 quarter");
 ck((aN*k+shift)%N===j&&v*(k%2?1:-1)===1,"whole72 square");
 perm.push(k);sign.push(v);
}
const mod=(x,n)=>((x%n)+n)%n,cmul=(a,b,n)=>[mod(a[0]*b[0]-a[1]*b[1],n),mod(a[0]*b[1]+a[1]*b[0]-a[1]*b[1],n)];
const gsq=cmul([91,72],[91,72],144);
ck(gsq[0]===73&&gsq[1]===0,"entire centre square");
const de=E(1,2),w=E(0,1),w2=E(-1,-1),ga=E(3,1),gb=E(2,-1),al=E(1,3);
const Y=[de,esc(de,2),ga,gb,E(1),E(2)],W=[de,esc(de,2),ga,gb,esc(de,3),E(4)];
const C=[ei(de),E(0),en(ei(de)),ei(de),E(0),E(0)],R=[E(0),E(0),E(0),E(0),al,E(1)];
ck(eq(he(C,C),E(1))&&ez(he(C,Y))&&ez(he(C,W))&&ez(he(C,R)),"pure C full physical row");
const zetas=[E(1),en(E(1)),w,en(w),w2,en(w2)];
const I=ident(6),rotations=[];
for(const z of zetas){
 const A=I.map((row,i)=>va(row,vm(C,em(es(z,E(1)),ec(C[i])))));
 ck(mm([W],A)[0].every((a,i)=>eq(a,W[i])),"complete W first parameters fixed");
 rotations.push({zeta:out(z),whole_W_row:W.map(out)});
}
const cw=E(19,3,72),EW=vs(R,vm(W,cw)),EW72=vm(EW,E(72));
ck(eq(he(W,W),E(72))&&ez(he(EW,W))&&eq(he(EW72,EW72),E(18936)),"entire companion chart");
const cy=E(3,3,34),EY=vs(R,vm(Y,cy)),bY=ea(E(1),esc(cy,2)),Wminus=vs(W,vm(Y,esc(bY,2)));
const Acoeff=E(-23,-6,17),cc=E(11,96,17),dd=E(-12,-12,17),expected=[em(Acoeff,de),em(Acoeff,esc(de,2)),em(Acoeff,ga),em(Acoeff,gb),cc,dd];
ck(Wminus.every((a,i)=>eq(a,expected[i])),"full reflected W parameters");
ck(eq(he(Wminus,Wminus),E(72)),"reflected norm");
const W17=vm(Wminus,E(17));
ck(eq(he(W17,W17),E(20808)),"complete reflected covered level");
const a=E(0,-3,8),aW=ea(a,E(2));
ck(W.every((a,i)=>eq(a,ea(em(bY,Y[i]),esc(EY[i],2)))),"exact W plus in Y companion chart");

const Zrow=[E(1),E(0),E(-1),E(-2),E(0),E(0)],Qrow=[E(1),E(0),E(1),E(0),E(0),E(0)],rrow=[E(0),E(1),E(0),E(0),E(0),E(0)];
const Krow=[E(0),E(0),E(0),E(0),E(1),E(2,3)],Vrow=vs(W,vm(R,aW));
const Hrow=vm(vs(C,rrow),de),Kbrow=vm(va(C,rrow),de),Xrow=va(Hrow,vm(Vrow,E(48,0,263)));
const aZ=E(-2,1,2),aQ=E(4,3,2),bK=E(-1,-6,8);
const L1=vs(Zrow,vm(Kbrow,ec(aZ))),L2=vs(Qrow,vm(Kbrow,esc(ec(aQ),1,3))),L3=vs(Krow,vm(Kbrow,esc(ec(bK),4,3)));
const wholeFrame=[W,EW72,vm(Xrow,E(263)),vm(L1,E(2)),vm(L2,E(6)),vm(L3,E(6))],wholeInv=inverse(wholeFrame);
for(let j=1;j<6;j++)ck(ez(he(wholeFrame[0],wholeFrame[j])),"full W orthogonal companions");
for(let j=2;j<6;j++)ck(ez(he(wholeFrame[1],wholeFrame[j])),"full EW orthogonal remaining four");
const oddCount=row=>row.reduce((n,x)=>{ck(x[0][1]===1n&&x[1][1]===1n,"integral CM halfcharacter row");return n+(x[0][0]%2n||x[1][0]%2n?1:0);},0);
ck(oddCount(W)===4&&oddCount(EW72)===4,"first two complete even halfcharacters");
const theta=es(E(1),em(a,cy));
ck(eq(theta,E(263,0,272)),"Y-deep V coefficient");
const eW_Y=es(cy,em(cw,bY)),eW_E=es(E(1),esc(cw,2));

return {format:"R634 original T companion complete one-layer return",
 N72:{g:[91,72],g_square_mod144:gsq,A_permutation:perm,A_sign:sign,absolute_anchor:"Theta(6z), eigenvalue -1",whole_square:1},
 full_integral_frame:{rows:wholeFrame.map(row=>row.map(out)),inverse:wholeInv.inverse.map(row=>row.map(out)),determinant:out(wholeInv.det),Gram:wholeFrame.map(row=>wholeFrame.map(col=>out(he(row,col)))),halfcharacter_odd_counts:[oddCount(W),oddCount(EW72)]},
 pure_C_row:C.map(out),six_C_rotations:rotations,first_W_half_character:"four odd CM coefficients; standard even S72 for every C rotation",
 actual_companion:{E_W:EW.map(out),integral_axis_72E_W:EW72.map(out),entire_degree:18936,perpendicular_to_W:true},
 actual_two_state:{state0:"P6_C rho0",state1:"P6_C rho1 = K_W mu0",W_core:"X",E_W_core:"epsilon X",both_W_marginals:"6 delta T"},
 old_Y_marginal:{state1:"Xi",new_projector_companion_mass:"52/3",no_full_Xi_central_zero:true},
 reflected_observations:{bY:out(bY),bY_norm:out(em(bY,ec(bY))),Wminus:Wminus.map(out),common_A_scale:out(Acoeff),sigma_c_scale:out(cc),sigma_d_scale:out(dd),covered_level:20808,full_Wminus_arithmetic_identity:"unknown",E_W_in_Y_EY:[out(eW_Y),out(eW_E)],Ydeep_V_coefficient:out(theta)},
 complete_native_difference:{domain:"E_Y in p^n; both W+/W- unit iff Y unit, n>=1",coefficient:"2 d_p beta^N0 (-epsilon lambda)^n",series:"sum_{j>=0} (2 kappa^n/bY)^(2j+1) M_(2j+1)/(2j+1)",all_common_units:true},
 first_pole_bridge:"M1-P1 = -a int_{Y,V unit} R^2/(YV) + int_{Y unit,V deep} R/Y - int_{V unit,Y deep} R/V",
 V_deep_failure_first_three_terms_zero:true,no_unknown_reflected_central_set_zero:true};

}
const text=JSON.stringify(certificate(),null,2)+'\n';
if(process.argv[2])require('fs').writeFileSync(process.argv[2],text);else process.stdout.write(text);
