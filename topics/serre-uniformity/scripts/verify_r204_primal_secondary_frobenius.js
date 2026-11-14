"use strict";
const fs=require("node:fs");
const C={"p":43,"q":"225196170077769188459647075003723446506290334538374935594311805764766375462943717166814768844511612408106442292450018627544384538312646994045716899229168141998348680872046002490066651342968053955905931120521143569132718008762168959999","P":[["33394750146194790765649469472547837490514177130010076735425672980662522876805868899390592419053375548932128552789686243150087769116503251190650595159188257014108013083444404325005912475712135747189340120575975548627405291819588145651","0"],["105971524503702502636043672316158349322260423550444493541426170484048156845678348646136672377218582504925670036420293139811724274157084436675916559592132515967995427027925989770126145341144538088870896345775311962514323576412778247819","0"]],"Q_real":[["79205847885131901513927649515699326043169439192146842054221770827666436216660091377902580457166044914272205154348100397256084302060789604626474192144810847536341358351879117203603264962865326827434480635945229364530987197686053501532","0"],["61318745458070519072635717613411420877718465121461892695206675978895304802838378783881634472011826164232402351061935782819398951677510892353973281488988706954961447586471804024639511036346659165302809020074133290831420889668950134248","0"]],"T5_beta":[["86291403028910370254696240820419847173480035482419545965936738077897347913499799040490439864223551022413921838431937199548181365124151796656651129490019461915862691550402143452853690489954847576071760692411189691063906119246183055588","96547855693631285808122101394007678495621085040783164733672907087768220204304348461086474674237052661666625807929066368182182238922314747555310676043015736351125742974045967614319564392364113397509729594639968649346199697151023697024"],["181863554244364268189922975972964448629523451556198003499219493461048940530988161741456066738163549680733380970824528509785412282990606321614464384125248443628546060007132395338341584963718380473046946373002822001917758243518469142919","92333544427987456623551408137472343880890767252597272267119193859114689485910800267886206081788681699940578569751735873047433961247878085927379196816535453316756790822821460844075169347144665285175223183203385001105269613859723381822"]],"zeta_Weil":["33192256431478777534772693342490161012373414464785401361122186710744426145385242337610237454110224901337816657644112419076529202192170583323034154623583921171355558078026293450555526527706963402223792490590954972636538127057395769163","171023583398532679386711239941267784062765623696689858645290077011642199651646324646676955701988625242095153878295365334133068324314695282660741691934130921957519553782994262401615031914521307989634726996409007549972082490092007345950"],"CM_log_beta":[22,11],"anti_p_step":21,"tame_correction":11};
"use strict";
function arithmetic(q){
 const mod=x=>(x%q+q)%q,Z=[0n,0n],O=[1n,0n],I=[0n,1n];
 const eq=(a,b)=>a[0]===b[0]&&a[1]===b[1],neg=a=>[mod(-a[0]),mod(-a[1])],add=(a,b)=>[mod(a[0]+b[0]),mod(a[1]+b[1])],sub=(a,b)=>[mod(a[0]-b[0]),mod(a[1]-b[1])],sm=(a,k)=>[mod(a[0]*BigInt(k)),mod(a[1]*BigInt(k))];
 function mul(a,b){if(!a[1]&&!b[1])return [mod(a[0]*b[0]),0n];const x=a[0]*b[0],y=a[1]*b[1];return [mod(x-y),mod((a[0]+a[1])*(b[0]+b[1])-x-y)];}
 const sq=a=>[mod((a[0]-a[1])*(a[0]+a[1])),mod(2n*a[0]*a[1])];
 function invint(a){a=mod(a);let b=q,x=1n,y=0n;while(b){const k=a/b;[a,b]=[b,a-k*b];[x,y]=[y,x-k*y];}if(a!==1n)throw Error("inverse");return mod(x);}
 function inv(a){const d=invint(a[0]*a[0]+a[1]*a[1]);return [mod(a[0]*d),mod(-a[1]*d)];}
 const div=(a,b)=>mul(a,inv(b));
 function pow(a,k){let z=O;for(k=BigInt(k);k;k>>=1n,a=sq(a))if(k&1n)z=mul(z,a);return z;}
 function fpow(a,k){let z=1n;for(a=mod(a);k;k>>=1n,a=mod(a*a))if(k&1n)z=mod(z*a);return z;}
 function fsqrt(a){a=mod(a);const r=fpow(a,(q+1n)/4n);return mod(r*r)===a?r:null;}
 function sqrt(a){if(eq(a,Z))return Z;if(!a[1]){let s=fsqrt(a[0]);if(s!==null)return [s,0n];s=fsqrt(-a[0]);if(s!==null)return [0n,s];return null;}
  const norm=mod(a[0]*a[0]+a[1]*a[1]),s=fsqrt(norm);if(s===null)return null;
  for(const sign of [s,mod(-s)]){const u=fsqrt(mod((a[0]+sign)*((q+1n)/2n)));if(u!==null&&u!==0n){const v=mod(a[1]*invint(2n*u));const r=[u,v];if(eq(sq(r),a))return r;}}return null;
 }
 const pneg=P=>P?[P[0],neg(P[1])]:null,peq=(P,Q)=>!P||!Q?P===Q:eq(P[0],Q[0])&&eq(P[1],Q[1]);
 function padd(P,Q,a){if(!P)return Q;if(!Q)return P;let lam;if(eq(P[0],Q[0])){if(eq(add(P[1],Q[1]),Z))return null;lam=div(add(sm(sq(P[0]),3),a),sm(P[1],2));}else lam=div(sub(Q[1],P[1]),sub(Q[0],P[0]));
  const x=sub(sub(sq(lam),P[0]),Q[0]),y=sub(mul(lam,sub(P[0],x)),P[1]);return [x,y];
 }
 const on=(P,a,b)=>!P||eq(sq(P[1]),add(add(mul(sq(P[0]),P[0]),mul(a,P[0])),b));
 function jdouble(P,a){const [X,Y,z]=P;if(eq(z,Z)||eq(Y,Z))return [O,O,Z];const A=sq(X),B=sq(Y),C=sq(B),D=sm(sub(sub(sq(add(X,B)),A),C),2),E=add(sm(A,3),mul(a,sq(sq(z)))),F=sq(E);
  return [sub(F,sm(D,2)),sub(mul(E,sub(D,sub(F,sm(D,2)))),sm(C,8)),sm(mul(Y,z),2)];
 }
 function jadd(P,Q,a){if(!Q)return P;if(eq(P[2],Z))return [Q[0],Q[1],O];const [X,Y,z]=P,z2=sq(z),U=mul(Q[0],z2),S=mul(Q[1],mul(z,z2)),H=sub(U,X),R=sm(sub(S,Y),2);
  if(eq(H,Z))return eq(R,Z)?jdouble(P,a):[O,O,Z];const HH=sq(H),II=sm(HH,4),JJ=mul(H,II),V=mul(X,II),x=sub(sub(sq(R),JJ),sm(V,2));
  return [x,sub(mul(R,sub(V,x)),sm(mul(Y,JJ),2)),sub(sub(sq(add(z,H)),z2),HH)];
 }
 function pmul(P,k,a){if(k<0n)return pmul(pneg(P),-k,a);let R=[O,O,Z];const bits=k.toString(2);for(const bit of bits){R=jdouble(R,a);if(bit==="1")R=jadd(R,P,a);}if(eq(R[2],Z))return null;const zi=inv(R[2]),z2=sq(zi);return [mul(R[0],z2),mul(R[1],mul(z2,zi))];}
 const ip=P=>P?[neg(P[0]),mul(I,P[1])]:null;
 const betaPoint=(P,a)=>padd(pneg(P),pmul(ip(P),2n,a),a);
 function velu(a,b,P,ell){let R=P,ker=[],ts=Z,ws=Z;
  for(let k=1;k<=(ell-1)/2;k++){if(!R||!on(R,a,b))throw Error("kernel");const u=R[0],v4=sm(sq(R[1]),4),t=add(sm(sq(u),6),sm(a,2));ker.push({u,v4,t});ts=add(ts,t);ws=add(ws,add(v4,mul(u,t)));R=padd(R,P,a);}
  return {a:sub(a,sm(ts,5)),b:sub(b,sm(ws,7)),ker};
 }
 function phi(E,P){if(!P)return null;const ds=E.ker.map(k=>sub(P[0],k.u));if(ds.some(x=>eq(x,Z)))return null;
  const pre=[],invs=[];let prod=O;for(const d of ds){pre.push(prod);prod=mul(prod,d);}let back=inv(prod);for(let j=ds.length-1;j>=0;j--){invs[j]=mul(back,pre[j]);back=mul(back,ds[j]);}
  let x=P[0],fac=O;for(let j=0;j<E.ker.length;j++){const k=E.ker[j],d=invs[j],d2=sq(d);x=add(x,add(mul(k.t,d),mul(k.v4,d2)));fac=sub(fac,add(mul(k.t,d2),sm(mul(k.v4,mul(d2,d)),2)));}
  const R=[x,mul(P[1],fac)];if(!on(R,E.a,E.b))throw Error("Velu image");return R;
 }
 function psi11(x,a,b){const x2=sq(x),x3=mul(x2,x),x4=sq(x2),x6=sq(x3),a2=sq(a),b2=sq(b),v=sm(add(add(x3,mul(a,x)),b),4),v2=sq(v);
  const o3=sub(add(add(sm(x4,3),sm(mul(a,x2),6)),sm(mul(b,x),12)),a2);
  let e4=add(add(x6,sm(mul(a,x4),5)),sm(mul(b,x3),20));e4=sub(e4,sm(mul(a2,x2),5));e4=sub(e4,sm(mul(mul(a,b),x),4));e4=sub(e4,sm(b2,8));e4=sm(sub(e4,mul(a2,a)),2);
  const o33=mul(sq(o3),o3),o5=sub(mul(v2,e4),o33),e6=mul(o3,sub(o5,sq(e4))),o7=sub(mul(o5,o33),mul(v2,mul(sq(e4),e4)));
  return sub(mul(o7,mul(sq(o5),o5)),mul(mul(v2,e4),mul(sq(e6),e6)));
 }
 const discr=(a,b)=>sm(add(sm(mul(sq(a),a),4),sm(sq(b),27)),-16);
 return {q,mod,Z,O,I,eq,neg,add,sub,sm,mul,sq,inv,div,pow,sqrt,fsqrt,invint,pneg,peq,padd,pmul,on,ip,betaPoint,velu,phi,psi11,discr};
}

const assert=(v,m)=>{if(!v)throw Error(m)};
const bigify=x=>Array.isArray(x)?x.map(bigify):typeof x==="string"?BigInt(x):x;
const m43=x=>(x%43+43)%43,mm=(z,w)=>[m43(z[0]*w[0]-z[1]*w[1]),m43(z[0]*w[1]+z[1]*w[0])];
function initial(C){
 const q=BigInt(C.q),A=arithmetic(q),{Z,O,I,eq,neg,add,sub,sm,mul,sq,div,pow,padd,pmul,ip,peq,velu,phi,on,betaPoint}=A;
 const a=[q-1n,0n],P=bigify(C.P),P2=[I,[1n,q-1n]],Q=bigify(C.Q_real),T5=bigify(C.T5_beta),zeta=bigify(C.zeta_Weil);
 assert(q%172n===171n&&((q+1n)/43n)%43n===11n,"same q");
 assert(P&&on(P,a,Z)&&pmul(P,43n,a)===null,"P order43");assert(P[0][1]===0n&&P[1][1]===0n,"P real");
 assert(on(P2,a,Z)&&peq(pmul(P2,2n,a),[Z,Z]),"P2");assert(peq(betaPoint(P2,a),P2),"primary beta P2");
 assert(T5&&on(T5,a,Z)&&pmul(T5,5n,a)===null&&betaPoint(T5,a)===null,"CM5 kernel");
 function miller(P,Q,n){let R=P,f=O;function line(U,V){if(eq(U[0],V[0])&&eq(add(U[1],V[1]),Z))return sub(Q[0],U[0]);const slope=eq(U[0],V[0])?div(add(sm(sq(U[0]),3),a),sm(U[1],2)):div(sub(V[1],U[1]),sub(V[0],U[0]));const W=padd(U,V,a),num=sub(sub(Q[1],U[1]),mul(slope,sub(Q[0],U[0])));return W?div(num,sub(Q[0],W[0])):num}
  for(const bit of n.toString(2).slice(1)){f=mul(sq(f),line(R,R));R=padd(R,R,a);if(bit==="1"){f=mul(f,line(R,P));R=padd(R,P,a)}}assert(R===null,"Miller endpoint");return f}
 assert(eq(neg(div(miller(P,ip(P),43),miller(ip(P),P,43))),zeta),"Weil pairing");assert(eq(pow(zeta,43n),O)&&!eq(zeta,O),"zeta order");
 const E=velu(a,Z,P,43),S=phi(E,ip(P)),P2bar=phi(E,P2);
 assert(Q&&on(Q,E.a,E.b)&&pmul(Q,43n,E.a)===null,"Q order43");assert(Q[0][1]===0n&&Q[1][1]===0n,"Q real");assert(S&&pmul(S,43n,E.a)===null,"S order");
 const Eback=velu(E.a,E.b,S,43),p=[43n,0n],p2=sq(p),p3=mul(p2,p),raw=phi(Eback,Q);
 assert(eq(Eback.a,mul(sq(p2),a))&&eq(Eback.b,Z),"dual model");assert(raw&&peq([div(raw[0],p2),div(raw[1],p3)],P),"dual Q=P");
 const cm=z=>z.map(x=>(x%1849n+1849n)%1849n),cp=(z,w)=>cm([z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0]]);
 let be=[1n,0n],b=[1848n,2n],n=1848n;for(;n;n>>=1n,b=cp(b,b))if(n&1n)be=cp(be,b);
 const log=cm([-(be[0]-1n)/43n,-be[1]/43n]).map(x=>Number(x%43n));assert(JSON.stringify(log)==="[22,11]","CM log");
 const state={q,P,P2,E,S,Q,P2bar,T5,index:0,lines:[],zeta};
 return{A,state,init:{P,Q,S,E},log};
}
function advance(state,A){
 const {q,Z,eq,mul,sq,inv,peq,padd,pmul,ip,betaPoint,velu,phi}=A,a=[q-1n,0n],E=state.E,Pn=betaPoint(state.P,a),En=velu(a,Z,Pn,43),Sn=phi(En,ip(Pn)),five=velu(E.a,E.b,phi(E,state.T5),5),beta=[q-1n,2n],beta2=sq(beta),beta3=mul(beta2,beta);
 assert(eq(five.a,mul(sq(beta2),En.a))&&eq(five.b,mul(sq(beta3),En.b)),"CM5 scale");
 const bi=V=>{const U=phi(five,V);return U?[mul(U[0],inv(beta2)),mul(U[1],inv(beta3))]:null};
 assert(peq(bi(state.S),Sn),"S label");
 const Qn=padd(bi(state.Q),pmul(Sn,-11n,En.a),En.a);
 assert(Qn&&A.on(Qn,En.a,En.b)&&pmul(Qn,43n,En.a)===null,"Q next");
 state.P=Pn;state.E=En;state.S=Sn;state.Q=Qn;state.P2bar=phi(En,state.P2);state.index++;
}
function closed(state,init,A){for(const k of["P","Q","S"])assert(A.peq(state[k],A.pmul(init[k],5n,k==="P"?[A.q-1n,0n]:init.E.a)),"closure "+k);assert(A.eq(state.E.a,init.E.a)&&A.eq(state.E.b,init.E.b),"curve closure")}
function residueLog(v,A,zeta){const sy=A.pow(v,(A.q*A.q-1n)/43n);let u=A.O;for(let j=0;j<43;j++){if(A.eq(u,sy))return j;u=A.mul(u,zeta)}throw Error("mu43 log")}
function stepRobert(state,A){
 const {q,Z,O,eq,mul,inv,pow,padd,pmul,peq,psi11,discr}=A,E=state.E,a=[q-1n,0n],delta=discr(E.a,E.b);
 let Qt=state.Q,step=pmul(state.S,21n,E.a),all=O,weighted=O;
 for(let t=0;t<43;t++){let R=padd(state.P2bar,Qt,E.a),v=O;for(let k=1;k<43;k++){const z=psi11(R[0],E.a,E.b);assert(!eq(z,Z),"psi nonzero");v=mul(v,z);R=padd(R,Qt,E.a)}assert(peq(R,state.P2bar),"scalar cycle");all=mul(all,v);weighted=mul(weighted,pow(v,BigInt(t)));Qt=padd(Qt,step,E.a)}
 assert(peq(Qt,state.Q),"Gamma cycle");let R=padd(state.P2,state.P,a),base=O;for(let k=1;k<43;k++){base=mul(base,psi11(R[0],a,Z));R=padd(R,state.P,a)}
 const ratio=mul(mul(pow(delta,18060n),base),inv(mul(pow([64n,0n],420n),all)));assert(eq(ratio,O),"exact Robert norm");
 const u0=mul(pow([64n,0n],420n),inv(base)),row={index:state.index,base_unit_log:residueLog(u0,A,state.zeta),derivative_log:m43(-residueLog(weighted,A,state.zeta)),norm_ratio:"1"};
 state.lines.push(row);advance(state,A);return row;
}
function stepPrimal(state,A){
 const {q,Z,O,eq,add,sub,mul,sq,pow,peq,padd,pmul,phi}=A,a=[q-1n,0n],E=state.E,T=phi(E,state.Taux||state.T5),T2=padd(T,T,E.a),weights=[];
 for(let k=1;k<43;k++){let u=1;while(u*k*k%43!==1)u++;weights.push(u)}
 let Qt=state.Q,delta=pmul(state.S,21n,E.a),all=O,weighted=O;
 for(let t=0;t<43;t++){let R=padd(state.P2bar,Qt,E.a),u=O;for(let k=1;k<43;k++){const d=mul(sub(R[0],T[0]),sub(R[0],T2[0]));assert(!eq(d,Z),"beta denominator");u=mul(u,pow(d,BigInt(weights[k-1])));R=padd(R,Qt,E.a)}assert(peq(R,state.P2bar),"scalar cycle");all=mul(all,u);weighted=mul(weighted,pow(u,BigInt(t)));Qt=padd(Qt,delta,E.a)}
 assert(peq(Qt,state.Q),"Gamma cycle");let R=padd(state.P2,state.P,a),base=O;for(let k=1;k<43;k++){const d=add(mul(state.auxBeta||[q-1n,2n],sq(R[0])),O);assert(!eq(d,Z),"base denominator");base=mul(base,pow(d,BigInt(weights[k-1])));R=padd(R,state.P,a)}
 const row={index:state.index,base_denominator_log:residueLog(base,A,state.zeta),norm_denominator_log:residueLog(all,A,state.zeta),derivative_denominator_log:residueLog(weighted,A,state.zeta)};
 assert(row.base_denominator_log===row.norm_denominator_log,"beta norm");state.lines.push(row);advance(state,A);return row;
}
function checkR198(C){
 const {A,state,init}=initial(C);for(let j=0;j<44;j++)stepRobert(state,A);closed(state,init,A);
 let om=[1,0],ds=[0,0],us=[0,0];for(const row of state.lines){ds=ds.map((v,k)=>m43(v+om[k]*row.derivative_log));us=us.map((v,k)=>m43(v+om[k]*row.base_unit_log));om=mm(om,[8,25])}
 assert(JSON.stringify(us)==="[0,0]"&&JSON.stringify(ds)==="[0,13]","Robert projection");
 const d0D=mm([0,42],ds),positive=d0D.map(v=>m43(-v)),actualK=mm([0,42],positive),actualQ=actualK.map(v=>m43(v*22));
 assert(JSON.stringify(d0D)==="[13,0]"&&JSON.stringify(actualQ)==="[0,28]","reference and descent");
 return{status:"PASS",psi11_evaluations:79464,all_44_norm_ratios:"1",CM_log_beta:[22,11],Weil_pairing_verified:true,all_three_beta44_closures:"[5]",raw_base_sum:us,raw_derivative_sum:ds,Qq_pure_p_actual_reference:actualQ,positive_secondary_coefficient:13,total_Omega_2_computed:false,rows:state.lines};
}
function checkR201(C){
 const {A,state}=initial(C),{q,Z,O,add,mul,inv,pow,eq,padd,psi11,betaPoint}=A,a=[q-1n,0n],m=(q*q-1n)/43n,e=(1n+2n*m)/43n;
 assert((1n+2n*m)%43n===0n&&m%43n===21n,"m and root exponent");
 let targets=[O,O],corrections=[O,O],full=[O,O],wh=[1,0],rows=[],P=state.P;
 const m1849=x=>(x%1849+1849)%1849,mh=(z,w)=>[m1849(z[0]*w[0]-z[1]*w[1]),m1849(z[0]*w[1]+z[1]*w[0])];
 for(let j=0;j<44;j++){let R=padd(state.P2,P,a),den=O;for(let k=1;k<43;k++){den=mul(den,psi11(R[0],a,Z));R=padd(R,P,a)}
  const u=mul(pow([64n,0n],420n),inv(den)),high=[wh[1],m1849(-wh[0])],low=high.map(x=>x%43),corr=high.map((x,k)=>(x-low[k])/43);
  for(let k=0;k<2;k++){targets[k]=mul(targets[k],pow(u,BigInt(low[k])));corrections[k]=mul(corrections[k],pow(u,BigInt(corr[k])));full[k]=mul(full[k],pow(u,BigInt(high[k])))}
  rows.push({j,low,high,base_log:residueLog(u,A,state.zeta)});wh=mh(wh,[352,197]);P=betaPoint(P,a);
 }
 assert(JSON.stringify(wh)==="[1,0]","Teich closure");assert(A.peq(P,A.pmul(state.P,5n,a)),"CM44 closure");
 const logs=corrections.map(z=>residueLog(z,A,state.zeta)),canonical=targets.map(z=>pow(z,e)),liftRoots=[];
 assert(JSON.stringify(logs)==="[0,3]","high-low logs");
 for(let k=0;k<2;k++){assert(eq(full[k],mul(targets[k],pow(corrections[k],43n))),"high-low identity");assert(eq(pow(targets[k],m),O)&&eq(pow(canonical[k],m),O),"mu_m");
  const gamma=pow(full[k],e*e%m),root=mul(pow(gamma,43n),inv(corrections[k]));liftRoots.push(root);
  assert(eq(pow(gamma,1849n),full[k])&&eq(pow(canonical[k],43n),targets[k])&&eq(pow(root,43n),targets[k]),"roots");assert(eq(root,mul(canonical[k],pow(state.zeta,BigInt(2*logs[k])))),"full Kummer gauge")}
 for(let t=0;t<43;t++){let L=m43(21*t),v=m43(2*t-12);assert(m43(13+11*v)===m43(10-L),"Omega algebra");assert((v===34)===(t===23)&&(t===23)===(L===10),"target")}
 return{status:"PASS",psi11_evaluations:1848,teich_omega:[352,197],power_logs_high_over_low:logs,mu43_root_corrections:[0,6],target_mu_index:23,target_power_residue_log:10,actual_norm_preimage_computed:false,targets,corrections,full_targets:full,canonical_roots:canonical,integral_lift_roots:liftRoots,rows};
}
function checkR204(C){
 const results=[],allRows=[];
 for(let aux=0;aux<2;aux++){const{A,state,init}=initial(C),q=A.q;if(aux){state.Taux=state.T5.map(v=>[v[0],A.mod(-v[1])]);state.auxBeta=[q-1n,q-2n]}
  for(let j=0;j<44;j++)stepPrimal(state,A);closed(state,init,A);
  let weight=[1,0],base=[0,0],derived=[0,0];for(const row of state.lines){base=base.map((x,k)=>m43(x+weight[k]*row.base_denominator_log));derived=derived.map((x,k)=>m43(x+weight[k]*row.derivative_denominator_log));weight=mm(weight,[36,5])}
  const einv=aux?[13,15]:[13,28],bk=aux?[40,39]:[40,4],k=aux?22:21,normcp=mm(base,einv),uncorrected=mm(derived,einv),correction=mm(mm(bk,einv),normcp).map(x=>m43(k*x)),D=uncorrected.map((x,j)=>m43(x-correction[j])),positive=D.map(x=>m43(-x)),actualK=mm([0,42],positive),actualQ=actualK.map(x=>m43(22*x));
  assert(JSON.stringify(base)===JSON.stringify(aux?[31,37]:[31,6]),"base");assert(JSON.stringify(derived)===JSON.stringify(aux?[33,6]:[10,6]),"D raw");
  assert(JSON.stringify(normcp)==="[20,0]"&&JSON.stringify(D)==="[0,38]"&&JSON.stringify(actualQ)==="[24,0]","Euler and actual");
  results.push({auxiliary:aux?"bar_beta":"beta",raw_base:base,raw_D:derived,Euler_correction:correction,corrected_D:D,positive_Qq:actualQ});allRows.push(state.lines);
 }
 return{status:"PASS",auxiliaries:2,denominator_evaluations:158928,all_88_weighted_norm_symbols_equal:true,Weil_pairing_verified:true,all_three_beta44_closures:"[5]",results,positive_primal_secondary_Frobenius:24,actual_L_computed:false,rows:allRows};
}


const out=checkR204(C),clean=JSON.parse(JSON.stringify(out,(_,v)=>typeof v==="bigint"?v.toString():v));
if(process.argv[2]==="--certificate")fs.writeFileSync(process.argv[3],JSON.stringify({...C,expected:clean},null,2)+"\n");
else if(process.argv[2]){const D=JSON.parse(fs.readFileSync(process.argv[2],"utf8"));assert(JSON.stringify(D.expected)===JSON.stringify(clean),"certificate");}
const summary={...clean};for(const k of ["rows","targets","corrections","full_targets","canonical_roots","integral_lift_roots"])delete summary[k];console.log(JSON.stringify(summary));
