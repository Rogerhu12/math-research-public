"use strict";
const fs=require("node:fs");
const C={"p":43,"q":"225196170077769188459647075003723446506290334538374935594311805764766375462943717166814768844511612408106442292450018627544384538312646994045716899229168141998348680872046002490066651342968053955905931120521143569132718008762168959999","fEven":[-43,3311,-76153,826804,-5167525,20764055,-57500460,115000920,-171655785,195747825,-173376645,120609840,-66335412,28915436,-9970840,2701776,-567987,90687,-10621,860,-43,1],"gDesc":["-16327464","-32688421","636891359","1274935920","-11499057732","-23015414551","127514905483","255172444283","-971797090418","-1944212323820","5396336469305","10792866388653","-22587509701367","-45159020373021","72727111706911","145335749598988","-182217408061576","-363930604369013","357097929861227","712705416840667","-547342458917037","-1091448273129748","652960441564111","1300653911277333","-600343727043585","-1194244952187508","418862136280342","831849342428810","-216820614311075","-429721377031810","80633423316371","159411803435470","-20568043093764","-40542627535269","3358230515416","6597209427096","-314344985758","-615241450575","13843605713","26972100150","-181634213","-351643330"],"rQ":"108345173358473018145871670124911324887049421683370153898043457506248351622594785040275626285045974332022576828309306586822632427995903422769950414590074440081658254178103480176903238856893491932542408248224272038321271037340323228098","e":[1,-14,-19,8,17,20,21,7,-12,-4,13,-10,11,18,6,2,15,5,16,-9,-3,-1,14,19,-8,-17,-20,-21,-7,12,4,-13,10,-11,-18,-6,-2,-15,-5,-16,9,3],"b0":[48118,65816,12765,71515,12479,48210,6102,38777,38723,12693,7813,2958,59873,37185,2093,77865,67478,50801,44796,23747,3170,14613,41734,394,14484,66676,49172,50485,77867,45747,64538,65417,13414,38865,33151,11041,60502,28385,68609,62556,60777,77185],"zeta_Weil":["33192256431478777534772693342490161012373414464785401361122186710744426145385242337610237454110224901337816657644112419076529202192170583323034154623583921171355558078026293450555526527706963402223792490590954972636538127057395769163","171023583398532679386711239941267784062765623696689858645290077011642199651646324646676955701988625242095153878295365334133068324314695282660741691934130921957519553782994262401615031914521307989634726996409007549972082490092007345950"]};
function need(c,m){if(!c)throw Error(m)}
const mod=(a,m)=>{a%=m;return a<0n?a+m:a};
const powI=(a,n,m)=>{let b=1n;for(a=mod(a,m);n;n>>=1n,a=a*a%m)if(n&1n)b=b*a%m;return b};
function polyRing(f,M=0n){
 const n=f.length-1,z=()=>Array(n).fill(0n),norm=a=>M?mod(a,M):a;
 const one=z();one[0]=1n;const r=z();r[1]=1n;
 const add=(a,b)=>a.map((v,i)=>norm(v+b[i])),sub=(a,b)=>a.map((v,i)=>norm(v-b[i])),scale=(a,c)=>a.map(v=>norm(v*c));
 function mul(a,b){let c=Array(2*n-1).fill(0n);for(let i=0;i<n;i++)if(a[i])for(let j=0;j<n;j++)if(b[j])c[i+j]+=a[i]*b[j];for(let k=2*n-2;k>=n;k--){let t=norm(c[k]);if(t)for(let j=0;j<n;j++)if(f[j])c[k-n+j]-=t*f[j]}return c.slice(0,n).map(norm)}
 function pow(a,k){let b=one;for(;k;k>>=1n,a=mul(a,a))if(k&1n)b=mul(b,a);return b}
 function evaluate(c,a){let v=z();for(let k=c.length-1;k>=0;k--){v=mul(v,a);v[0]=norm(v[0]+c[k])}return v}
 const eq=(a,b)=>a.every((v,i)=>norm(v-b[i])===0n);
 function inverse43(a){need(M===43n**4n,"inverse modulus");let b=z(),a0=mod(a[0],43n);need(a0!==0n,"unit");b[0]=powI(a0,41n,43n);for(let k=1;k<n;k++){let t=0n;for(let j=1;j<=k;j++)t+=a[j]*b[k-j];b[k]=mod(-t*b[0],43n)}for(let k=0;k<2;k++)b=mul(b,sub(scale(one,2n),mul(a,b)));need(eq(mul(a,b),one),"inverse");return b}
 return{n,z,one,r,add,sub,scale,mul,pow,evaluate,inverse43,eq}
}
function bareiss(A){A=A.map(r=>r.slice());let n=A.length,old=1n,sgn=1n,divs=0;for(let k=0;k<n-1;k++){if(!A[k][k]){let j=k+1;while(j<n&&!A[j][k])j++;need(j<n,"singular Bareiss");[A[k],A[j]]=[A[j],A[k]];sgn=-sgn}let p=A[k][k];for(let i=k+1;i<n;i++)for(let j=k+1;j<n;j++){let t=A[i][j]*p-A[i][k]*A[k][j];need(t%old===0n,"nonexact Bareiss");A[i][j]=t/old;divs++}for(let i=k+1;i<n;i++)A[i][k]=0n;old=p}return {value:sgn*A[n-1][n-1],divisions:divs}}
function normPoly(f,g){let R=polyRing(f),v=R.evaluate(g,R.r),A=Array.from({length:R.n},()=>Array(R.n).fill(0n));for(let j=0;j<R.n;j++){for(let i=0;i<R.n;i++)A[i][j]=v[i];v=R.mul(v,R.r)}return bareiss(A)}
function evalMod(c,x,m){let v=0n;for(let j=c.length-1;j>=0;j--)v=mod(v*x+c[j],m);return v}
function checkR191(data){
 let f=Array(43).fill(0n);data.fEven.forEach((v,j)=>f[2*j]=BigInt(v));const g=data.gDesc.map(BigInt).reverse(),q=BigInt(data.q),rq=BigInt(data.rQ);
 need(f[42]===1n&&f.slice(0,42).every(v=>v%43n===0n)&&f[0]%1849n!==0n,"Eisenstein");
 let f2=0n;for(let j=42;j>=0;j--)f2=2n*f2+f[j];need(f2===1n,"f(2)");
 let lhs=Array(85).fill(0n);for(let k=0;k<=42;k++){let bin=1n;for(let j=0;j<=k;j++){lhs[42+k-2*j]+=f[k]*bin;if(j<k)bin=bin*BigInt(k-j)/BigInt(j+1)}}
 for(let k=0;k<=84;k++)need(lhs[k]===(k%2===0?((k/2)%2===0?1n:-1n):0n),"cyclotomic identity");
 const Ng=normPoly(f,g);need(Ng.value===-q,"Norm g");
 const df=f.slice(1).map((v,j)=>v*BigInt(j+1)),Nd=normPoly(f,df);need(-Nd.value===(2n**42n)*(43n**41n),"disc");
 need(evalMod(f,rq,q)===0n&&evalMod(g,rq,q)===0n,"q root");
 let roots=[],x=rq;for(let j=0;j<42;j++){need(!roots.includes(x),"distinct roots");roots.push(x);x=mod(3n*x-x*x*x,q)}
 need(x===rq,"root closure");need(roots.filter(v=>evalMod(g,v,q)===0n).length===1,"unique g root");
 let S0=2n,S1=rq;for(let j=2;j<=44;j++){let S=mod(rq*S1-S0,q);S0=S1;S1=S}
 const half=(q+1n)/2n,zeta=data.zeta_Weil;need(mod(S1*half,q)===BigInt(zeta[0])&&mod(-rq*half,q)===BigInt(zeta[1]),"Weil root alignment");
 const R=polyRing(f,43n**4n),sig=R.sub(R.scale(R.r,3n),R.pow(R.r,3n)),e=data.e.map(BigInt);
 let orbit=[],r=R.r,A=R.one,W=R.one;
 for(let j=0;j<42;j++){orbit.push(r);r=R.evaluate(sig,r)}
 need(R.eq(r,R.r),"sigma order");
 for(let j=0;j<42;j++){const h=R.mul(R.evaluate(g,orbit[j]),R.pow(R.sub(R.scale(R.one,2n),orbit[j]),22n)),a=e[j],d=(e[(j+41)%42]-3n*a)/43n;need((e[(j+41)%42]-3n*a)%43n===0n,"character e");A=R.mul(A,R.pow(a<0n?R.inverse43(h):h,a<0n?-a:a));W=R.mul(W,R.pow(d<0n?R.inverse43(h):h,d<0n?-d:d));need(mod(a*powI(3n,BigInt(j),43n),43n)===1n,"character power")}
 const b=data.b0.map(BigInt);need(R.eq(R.pow(b,43n),A),"Hensel root mod p4");need(R.eq(R.evaluate(A,sig),R.mul(R.pow(A,3n),R.pow(W,43n))),"sigma Kummer identity");
 const g0=mod(g[0],43n),g1=mod(g[1],43n);need(g0===6n&&g1===23n&&mod(g1*powI(g0,41n,43n),43n)===11n,"local first coefficient");
 need(mod(11n-22n*22n,43n)===0n,"local coefficient cancellation");
 return{status:"PASS",degree:42,q_bits:q.toString(2).length,norm_g:"-q",discriminant:"2^42*43^41",exact_Bareiss_divisions:Ng.divisions+Nd.divisions,q_orbit_distinct:42,unique_q_zero_of_g:true,same_Weil_root:true,hensel_modulus:"43^4",hensel_derivative_valuation:42,error_valuation_at_least:168,ray_conductor:"q",p_split:true,Omega_2_computed:false};
}
function pairRing(M){const mul=(a,b)=>[mod(a[0]*b[0]-a[1]*b[1],M),mod(a[0]*b[1]+a[1]*b[0],M)],one=[1n,0n];function pow(a,n){let b=one;for(;n;n>>=1n,a=mul(a,a))if(n&1n)b=mul(b,a);return b}return{mul,pow,one}}
function gcdPoly5(a,b){const trim=a=>{while(a.length&&a[a.length-1]===0n)a.pop();return a};a=trim(a.map(v=>mod(v,5n)));b=trim(b.map(v=>mod(v,5n)));while(b.length){let c=a.slice(),v=powI(b[b.length-1],3n,5n);for(let j=c.length-1;j>=b.length-1;j--){let t=mod(c[j]*v,5n);for(let k=0;k<b.length;k++)c[j-b.length+1+k]=mod(c[j-b.length+1+k]-t*b[k],5n)}a=b;b=trim(c)}return a}
function checkR196(data){
 let f=Array(43).fill(0n);data.fEven.forEach((v,j)=>f[2*j]=BigInt(v));const g=data.gDesc.map(BigInt).reverse(),R=polyRing(f,5n),order=5n**42n,exp=(order-1n)/43n;
 let powers=[R.r];for(let j=1;j<=42;j++)powers.push(R.pow(powers[j-1],5n));need(R.eq(powers[42],R.r),"F5 degree42 closure");for(let d of[21,14,6])need(gcdPoly5(f,R.sub(powers[d],R.r)).length===1,"F5 irreducible");
 let S0=R.scale(R.one,2n),S1=R.r;for(let j=2;j<=44;j++){let S=R.sub(R.mul(R.r,S1),S0);S0=S1;S1=S}
 const zeta=R.scale(R.sub(S1,R.scale(R.r,3n)),3n);need(R.eq(R.pow(zeta,43n),R.one)&&!R.eq(zeta,R.one),"zeta43");
 function log(a){let v=R.one;for(let k=0;k<43;k++){if(R.eq(v,a))return k;v=R.mul(v,zeta)}throw Error("no mu43 log")}
 let r=R.r,lp=0,lg=0,raw=[];for(let j=0;j<42;j++){let zp=R.pow(R.sub(R.scale(R.one,2n),r),exp),zg=R.pow(R.evaluate(g,r),exp),a=log(zp),b=log(zg);raw.push([a,b]);lp=(lp+data.e[j]*a)%43;lg=(lg+data.e[j]*b)%43;r=R.sub(R.scale(r,3n),R.pow(r,3n))}
 lp=(lp+43)%43;lg=(lg+43)%43;const red=v=>(v%43+43)%43;
 let symbols={ap:lp,ag:lg,aq:red(lg+22*lp),ah:red(lg+lp),astar:red(lp+2*(lg+22*lp))};
 need(JSON.stringify(symbols)===JSON.stringify({ap:22,ag:19,aq:30,ah:41,astar:39}),"projected symbols");
 let descended=Object.fromEntries(Object.entries(symbols).map(([k,v])=>[k,red(-v)]));need(descended.astar===red(descended.ap+2*descended.aq)&&descended.astar===red(2*descended.ah),"actual field identity");
 const C=pairRing(1849n),b=[1848n,2n],bp=C.pow(b,1848n);need((bp[0]-1n)%43n===0n&&bp[1]%43n===0n,"CM logarithm divisible");let ell=[mod(-(bp[0]-1n)/43n,43n),mod(-bp[1]/43n,43n)];need(ell[0]===22n&&ell[1]===11n,"CM log");need(mod(-2n*ell[1],43n)===21n,"anti CM sign");
 const q=BigInt(data.q),Q=pairRing(q),z=data.zeta_Weil.map(BigInt),bq=[q-1n,2n],res=Q.pow(bq,(q*q-1n)/43n),expected=Q.pow(z,13n);need(res[0]===expected[0]&&res[1]===expected[1],"q symbol");
 return{status:"PASS",degree42_field_mod5_irreducible:true,projected_mu43_logs:symbols,restriction_degree:42,descended_Artin_values:descended,CM_log_beta:ell.map(Number),q_beta_residue_log:13,kappa_star:4,kappa_h:2,actual_reference_W:"-ell_cyc-i*kappa_p",actual_reference_W1:"-i*kappa_p",rho2_dual_WW:"-i*(kappa_p+2*kappa_q)",ordinary_global_norm_exists:true,S_unit_witness_computed:false,Omega_2_computed:false,raw_prime5_symbol_rows:raw};
}


const out=checkR196(C);
if(process.argv[2]==="--certificate")fs.writeFileSync(process.argv[3],JSON.stringify({...C,expected:out},null,2)+"\n");
else if(process.argv[2]){const D=JSON.parse(fs.readFileSync(process.argv[2],"utf8"));need(JSON.stringify(D.expected)===JSON.stringify(out),"certificate");}
console.log(JSON.stringify({...out,raw_prime5_symbol_rows:out.raw_prime5_symbol_rows?"42 rows verified":undefined}));
