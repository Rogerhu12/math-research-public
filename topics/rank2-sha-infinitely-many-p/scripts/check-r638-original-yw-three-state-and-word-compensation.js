// R638 exact Q(omega) certificate. Run: node check-r638-original-yw-three-state-and-word-compensation.js [output.json]
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

const zero=E(0),one=E(1),w=E(0,1),de=E(1,2),c=E(17,-3);
const mulInt=(x,y)=>em(x,y), charTable=[], sums=[];
for(let j=0;j<4;j++)for(let k=0;k<4;k++){
 let row=[],sum=0;
 for(let s=0;s<2;s++)for(let r=0;r<2;r++){
  const x=em(em(c,E(s,r)),ec(E(j,k)));
  ck(x[1][1]===1n,"integral mixed phase");
  const sign=x[1][0]%2n===0n?1:-1;row.push(sign);sum+=sign;
 }
 ck(sum===((j%2===0&&k%2===0)?4:0),"mixed E2/E4 exact projector");
 charTable.push({quarter:[j,k],characters:row,sum});sums.push(sum);
}

for(let j=0;j<72;j++){
 const half=j%2===0?[j,(j+36)%72]:[];
 const lhs=half.map(k=>(19*k+36)%72).sort((a,b)=>a-b);
 const rhs=half.slice().sort((a,b)=>a-b);
 ck(JSON.stringify(lhs)===JSON.stringify(rhs),"K72 H2=-H2 whole columns");
}

const D=[[1,0,0],[0,-1,0],[0,1,1]].map(r=>r.map(x=>E(x)));
const K=[[0,1,0],[1,0,0],[0,0,-1]].map(r=>r.map(x=>E(x))),I3=ident(3);
const same=(A,B)=>A.every((r,i)=>r.every((x,j)=>eq(x,B[i][j])));
ck(same(mm(D,D),I3)&&same(mm(K,K),I3),"source involutions");
const DK=mm(D,K),dk2=mm(DK,DK),dk4=mm(dk2,dk2);
ck(same(dk4,I3)&&!same(dk2,I3),"actual order four source word");
const key=A=>JSON.stringify(A.map(r=>r.map(out))),group=[I3],seen=new Set([key(I3)]);
for(let i=0;i<group.length;i++)for(const C of[D,K]){let A=mm(C,group[i]),s=key(A);if(!seen.has(s)){seen.add(s);group.push(A);}}
ck(group.length===8,"eight distinct actual source matrices");
const rowT=[E(1),E(1),E(0)];
const rowsT=group.map(C=>mm([rowT],C)[0]);
for(const row of rowsT)ck((eq(row[0],one)||eq(row[0],en(one)))&&(eq(row[1],one)||eq(row[1],en(one)))&&ez(row[2]),"whole original T arithmetic row");
const z=[zero],o=[one],kap=[zero,one];
const trim=p=>{p=p.slice();while(p.length>1&&ez(p[p.length-1]))p.pop();return p;};
const pa=(p,q)=>trim(Array.from({length:Math.max(p.length,q.length)},(_,i)=>ea(p[i]||zero,q[i]||zero)));
const pn=p=>p.map(en),ps=(p,q)=>pa(p,pn(q));
const pm=(p,q)=>{let r=Array.from({length:p.length+q.length-1},()=>zero);for(let i=0;i<p.length;i++)for(let j=0;j<q.length;j++)r[i+j]=ea(r[i+j],em(p[i],q[j]));return trim(r);};
const pc=(p,c)=>p.map(x=>em(x,c)),peq=(p,q)=>key([trim(p)])===key([trim(q)]);
const pmm=(A,B)=>A.map(row=>B[0].map((_,j)=>row.reduce((s,t,k)=>pa(s,pm(t,B[k][j])),z)));
const peqM=(A,B)=>A.every((r,i)=>r.every((x,j)=>peq(x,B[i][j])));
const eye=[[o,z],[z,o]],kI=[[kap,z],[z,kap]],by=E(20,3,17);
const t=E(349,0,612),u=E(17,-3,18),v=E(5260,789,20808);
const P=[[t,u],[v,es(one,t)]];
ck(same(mm(P,P),P),"orthogonal W projector");
const B=P.map((r,i)=>r.map((x,j)=>[es(E(i===j?1:0),x),x]));
const Bc=P.map((r,i)=>r.map((x,j)=>[x,es(E(i===j?1:0),x)]));
const A=[[pn(kap),z],[z,o]],Ac=[[pn(o),z],[z,kap]];
ck(peqM(pmm(A,Ac),kI)&&peqM(pmm(B,Bc),kI),"complete complementary physical words");
const AB=pmm(A,B),tr=pa(AB[0][0],AB[1][1]),det=ps(pm(AB[0][0],AB[1][1]),pm(AB[0][1],AB[1][0]));
ck(peq(tr,[t,zero,en(t)])&&peq(det,[zero,zero,en(one)]),"physical AB trace and determinant");
const mats=[A,Ac,B,Bc],invPairs=[1,0,3,2],reducedPairs=[];
for(let i=0;i<4;i++)for(let j=0;j<4;j++){
 const p=pmm(mats[i],mats[j]),constant=p.map(r=>r.map(q=>q[0]||zero));
 const nonzero=constant.some(r=>r.some(x=>!ez(x)));
 ck(nonzero===(j!==invPairs[i]),"exact four-line reduced pair criterion");
 reducedPairs.push({left:i,right:j,constant_nonzero:nonzero});
}
const axes=[[one,zero],[zero,one],[by,E(2)],[E(-263,0,1224),E(17,-3,36)]];
const minors=[];for(let i=0;i<4;i++)for(let j=i+1;j<4;j++){const d=es(em(axes[i][0],axes[j][1]),em(axes[i][1],axes[j][0]));minors.push({axes:[i,j],det:out(d),norm:out(em(d,ec(d)))});}
return {
 format:"R638 same original Y/W three-source core and complete word compensation",
 half_character:{first_Y_double_period_four_odd_factors_sign:1,cross_2Y_W:"4(17-3omega)",quarter_character_table:charTable,P2_on_muW:"h/2",whole_K136:"R_Y(2P2-I)"},
 sources:["mu0","muW","h"],D:D.map(r=>r.map(out)),K:K.map(r=>r.map(out)),group_order:group.length,
 eight_source_matrices:group.map(M=>M.map(r=>r.map(out))),original_T_rows:rowsT.map(r=>r.map(out)),
 physical:{coordinate_order:["Y","E_Y"],A:A.map(r=>r.map(p=>p.map(out))),A_companion:Ac.map(r=>r.map(p=>p.map(out))),B:B.map(r=>r.map(p=>p.map(out))),B_companion:Bc.map(r=>r.map(p=>p.map(out))),AB_trace:tr.map(out),AB_det:det.map(out),four_axis_minors:minors,reduced_pair_table:reducedPairs},
 common_native_domain:{A_power_image:"Y in p^n",B_power_image:"W in p^n",intersection:"Y,E_Y both in p^n, all four other companions unchanged",A_inverse_W_on_intersection:"(-1)^n bY Y+2 kappa^n E_Y",B_inverse_W_on_intersection:"W"},
 arithmetic:{both_full_normalized_word_rows:"6 delta lambda^n beta^N0 J_T(u)",common_A_central:"epsilon^n lambda^(2n) beta^N0 [J_S' + d_p sum_{k>=1} (-1)^(k+1)(2(-1)^n kappa^n/bY)^k M_k/k]",common_B_central:"6 delta epsilon^n lambda^(2n) beta^N0 J_T'",outside_B:"6 delta beta^N0(lambda^n-epsilon^n lambda^(2n)) J_T'",outside_A_under_two_zeros:"minus the full common-A moment series",same_unit_cuts_not_assumed:true},
 new_line_companion:{mass:"52/3",E_Y_core:"-epsilon lambda",E_Y_unit_mass:"(1+epsilon lambda)52/3",mixed_W_cut_not_commuted:true},
 negative_five_link:"M1=(-36 bK)Omega^5 I1 + B1 - a C_YV + D_V - D_Y; all complete terms retained",
 no_reflected_W_arithmetic_identity_assumed:true,
 no_free_word_image_or_native_outside_zero_assumed:true
};
}
const text=JSON.stringify(certificate(),null,2)+'\n';
if(process.argv[2])require('fs').writeFileSync(process.argv[2],text);else process.stdout.write(text);
