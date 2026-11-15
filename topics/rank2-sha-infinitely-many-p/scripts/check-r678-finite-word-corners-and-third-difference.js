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




function compute(){
 const vars=["x","z","y","eps","eps_n"];
 const zero=()=>new Map(),key=e=>e.join(","),unkey=k=>k.split(",").map(Number);
 const mon=(e,c=E(1))=>{const p=zero();e=e.slice();e[3]=((e[3]%2)+2)%2;e[4]=((e[4]%2)+2)%2;if(!ez(c))p.set(key(e),c);return p;};
 const con=c=>mon([0,0,0,0,0],c);
 const add=(p,q)=>{const r=new Map(p);for(const[k,c]of q){const s=ea(r.get(k)||E(0),c);if(ez(s))r.delete(k);else r.set(k,s);}return r;};
 const neg=p=>new Map([...p].map(([k,c])=>[k,en(c)]));
 const sub=(p,q)=>add(p,neg(q));
 const mul=(p,q)=>{let r=zero();for(const[k,a]of p)for(const[l,b]of q){let e=unkey(k).map((v,i)=>v+unkey(l)[i]);r=add(r,mon(e,em(a,b)));}return r;};
 const sc=(p,c)=>mul(p,con(c));
 const same=(p,q)=>sub(p,q).size===0;
 const vec=(...v)=>v;
 const rowadd=(p,q)=>p.map((t,i)=>add(t,q[i]));
 const rowsc=(p,q)=>p.map(t=>mul(t,q));
 const rowsub=(p,q)=>rowadd(p,rowsc(q,con(E(-1))));
 let checks=0;const check=(x,m)=>{ck(x,m);checks++;};
 const basis=Array.from({length:6},(_,j)=>Array.from({length:6},(_,i)=>con(E(i===j?1:0))));
 const [A,Qr,L,C,Ds,H1]=basis;
 const x=mon([1,0,0,0,0]),z=mon([0,1,0,0,0]),y=mon([0,0,1,0,0]);
 const x2=mul(x,x),xz=mul(x,z),xzInv=mon([1,-1,0,0,0]),x2yInv=mon([2,0,-1,0,0]);
 const eps=mon([0,0,0,1,0]),epsn=mon([0,0,0,0,1]);
 const a=E(-5,-6,29),bf=E(5,6,5),ell=E(0,-3,5),g=E(3,-2);
 const bq=E(11,6,5),bl=E(2,12,5),by=E(20,3,17),one=E(1);
 check(eq(ea(esc(a,29),esc(bf,5)),E(0)),"F0 perpendicular Y0");
 check(eq(esc(ea(E(29),esc(bq,5)),1,34),by),"actual W/Y coefficient");
 const B=[rowsc(A,x2),rowsc(Qr,xz),rowsc(L,y),C,Ds,H1];
 const actual=row=>row.reduce((r,p,i)=>rowadd(r,rowsc(B[i],p)),Array.from({length:6},()=>zero()));
 const Y0=rowadd(A,Qr),Y1=rowadd(A,L);
 const W0=rowadd(rowadd(A,rowsc(Qr,con(bq))),rowsc(L,con(bl)));
 const W1=rowadd(rowadd(A,rowsc(Qr,con(en(bl)))),rowsc(L,con(bq)));
 const s0Inv=mon([-1,-1,0,1,0]),s1Inv=mon([0,0,-1,0,1]);
 const obs0=actual(rowadd(W0,rowsc(Y0,sc(sub(s0Inv,con(one)),by))));
 const obs1=actual(rowadd(W1,rowsc(Y1,sc(sub(s1Inv,con(one)),by))));
 const normY0=rowsc(actual(Y0),s0Inv),normY1=rowsc(actual(Y1),s1Inv);
 const expY0=rowsc(rowadd(Qr,rowsc(A,xzInv)),eps);
 const expY1=rowsc(rowadd(L,rowsc(A,x2yInv)),epsn);
 const expW0=rowadd(rowsc(expY0,con(by)),rowadd(rowsc(Qr,sc(xz,es(bq,by))),rowadd(rowsc(A,sc(x2,es(one,by))),rowsc(L,sc(y,bl)))));
 const expW1=rowadd(rowsc(expY1,con(by)),rowadd(rowsc(Qr,sc(xz,en(bl))),rowadd(rowsc(A,sc(x2,es(one,by))),rowsc(L,sc(y,es(bq,by))))));
 for(let i=0;i<6;i++){check(same(normY0[i],expY0[i]),"Y0 full pullback "+i);check(same(normY1[i],expY1[i]),"Y1 full pullback "+i);check(same(obs0[i],expW0[i]),"W0 full pullback "+i);check(same(obs1[i],expW1[i]),"W1 full pullback "+i);}
 const F0=rowadd(rowadd(C,Ds),rowadd(rowsc(A,con(a)),rowadd(rowsc(Qr,con(bf)),rowsc(L,con(ell)))));
 const F1=rowadd(rowadd(C,Ds),rowadd(rowsc(A,con(a)),rowadd(rowsc(Qr,con(en(ell))),rowsc(L,con(bf)))));
 const sh0=rowadd(rowsc(A,sc(x2,a)),rowadd(rowsc(Qr,sc(xz,bf)),rowsc(L,sc(y,ell))));
 const sh1=rowadd(rowsc(A,sc(x2,a)),rowadd(rowsc(Qr,sc(xz,en(ell))),rowsc(L,sc(y,bf))));
 for(let i=0;i<6;i++){
 check(same(actual(F0)[i],rowadd(rowadd(C,Ds),sh0)[i]),"q0 first gate "+i);
 check(same(actual(F1)[i],rowadd(rowadd(C,Ds),sh1)[i]),"q1 first gate "+i);
 }
 const G0=rowadd(rowsc(H1,con(E(13))),rowsc(F0,con(g)));
 const G1=rowadd(rowsc(H1,con(E(13))),rowsc(F1,con(g)));
 for(let i=0;i<6;i++){
 check(same(actual(G0)[i],rowadd(rowadd(rowsc(H1,con(E(13))),rowsc(rowadd(C,Ds),con(g))),rowsc(sh0,con(g)))[i]),"q0 G gate "+i);
 check(same(actual(G1)[i],rowadd(rowadd(rowsc(H1,con(E(13))),rowsc(rowadd(C,Ds),con(g))),rowsc(sh1,con(g)))[i]),"q1 G gate "+i);
 }
 // Integer-polynomial identities for the four integral interpolation weights.
 const trim=p=>{p=p.slice();while(p.length&&p.at(-1)===0n)p.pop();return p;};
 const pa=(p,q)=>trim(Array.from({length:Math.max(p.length,q.length)},(_,i)=>(p[i]||0n)+(q[i]||0n)));
 const pn=p=>p.map(t=>-t);
 const pm=(p,q)=>{let r=Array(p.length+q.length-1).fill(0n);for(let i=0;i<p.length;i++)for(let j=0;j<q.length;j++)r[i+j]+=p[i]*q[j];return trim(r);};
 const ps=(p,n)=>Array(n).fill(0n).concat(p), peq=(p,q)=>{p=trim(p);q=trim(q);return p.length===q.length&&p.every((x,i)=>x===q[i]);};
 const den=pm(pm([1n,-1n],[1n,0n,-1n]),[1n,0n,0n,-1n]);
 const nums=[[0n,0n,0n,1n],[0n,-1n,-1n,-1n],[1n,1n,1n],[-1n]];
 for(let k=0;k<=3;k++){
 const sum=nums.reduce((r,p,j)=>pa(r,ps(p,j*k)),[]);
 check(peq(sum,k===3?ps(den,3):[]),"interpolation moment "+k);
 }
 // Verify A(z) numerator = -(z-1)(z-kappa)(z-kappa^2), coefficient by z.
 let polyZ=[[1n]];
 for(const c of[[1n],[0n,1n],[0n,0n,1n]]){
 let nxt=Array.from({length:polyZ.length+1},()=>[]);
 for(let i=0;i<polyZ.length;i++){nxt[i]=pa(nxt[i],pn(pm(polyZ[i],c)));nxt[i+1]=pa(nxt[i+1],polyZ[i]);}
 polyZ=nxt;
 }
 for(let j=0;j<4;j++)check(peq(pn(polyZ[j]),nums[j]),"full arithmetic coefficient "+j);
 // Pair angle two and original total carry degree six: y degree at most two in the mass.
 const allowed=[];
 for(let q=0;q<=6;q++)for(let l=0;l<=6-q;l++)if((q+l)%6===2){allowed.push([q,l]);check(l<=2,"whole mass third difference");}
 const serialize=p=>[...p].sort(([a],[b])=>a.localeCompare(b)).map(([k,c])=>({exponents:unkey(k),coefficient:out(c)}));
 return{
 format:"R678 exact original word and interpolation certificate",field:"Q(omega), omega^2+omega+1=0",
 coordinate_order:["A","Q","L","C","D_star","H1"],formal_variables:vars,
 constants:{a:out(a),b_F:out(bf),ell_0:out(ell),g:out(g),b_Q:out(bq),b_L:out(bl),b_Y:out(by),h:out(em(bl,ei(by)))},
 word_image:B.map(row=>row.map(serialize)),
 first_Y:expY0.map(serialize),first_W:expW0.map(serialize),
 opposite_Y:expY1.map(serialize),opposite_W:expW1.map(serialize),
 first_gate_shift:sh0.map(serialize),opposite_gate_shift:sh1.map(serialize),
 interpolation:{denominator:den.map(String),numerators:nums.map(p=>p.map(String)),valuation:[3,1,0,0],moments_k_0_1_2_3:["0","0","0","kappa^3"],whole_A:"-(z-1)(z-kappa)(z-kappa^2)/((1-kappa)(1-kappa^2)(1-kappa^3))"},
 allowed_pair_mass_powers:allowed,
 depth_conditions:["N is positive and divisible by 4","r is even","m=0 or 1","M>=2","j=0,1,2,3","n=r+M+j","r>max(N,M+3)"],
 actual_cell:"A in p^(2r), Q in p^(r+m) units, L in p^n units",
 equivalent_observations:"Y0,Y2,c,d,E_all have valuation r+m; Y1,Y3 have valuation n",
 common_gate:"C unit and D_star in p^N",
 source_scalar:"lambda^(2r)*beta^(r+m+n)",
 normalized_error:"p^(r-4N) O after the third divided difference",
 original_I:"I_(Sigma_5,-1), R655; not a positive moment",
 main_coefficient:"72*b*Omega^3*(b_L/b_Y)*J_N^dagger*(1-beta*kappa^3)*I_(Sigma_5,-1)",
 finite_nonzero_condition:"r>2N+v_p(I_(Sigma_5,-1))",
 bounded_corner_valuation:"3(r+M)+3-2N+v_p(I_(Sigma_5,-1))",
 remaining:"The complementary S and T cuts and the opposite-Y q1/observation remain distinct; no external integral is assigned zero.",
 exact_checks:checks};
}


if(typeof module!=="undefined")module.exports={compute};
if(typeof require!=="undefined"&&require.main===module){
 const fs=require("fs");const data=JSON.stringify(compute(),null,2)+"\n";
 if(process.argv[2])fs.writeFileSync(process.argv[2],data);else process.stdout.write(data);
}
