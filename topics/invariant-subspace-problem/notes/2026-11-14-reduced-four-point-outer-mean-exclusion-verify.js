function buildOrthogonalSupportEquations() {
 const Z=()=>new Map(),one=new Map([[0,1n]]),v=i=>new Map([[16**i,1n]]),add=(a,b,s=1n)=>{let o=new Map(a);for(let[k,x]of b){let z=(o.get(k)||0n)+s*x;if(z)o.set(k,z);else o.delete(k)}return o},sc=(a,s)=>add(Z(),a,BigInt(s)),mul=(a,b)=>{let o=Z();for(let[k,x]of a)for(let[l,y]of b){let z=(o.get(k+l)||0n)+x*y;if(z)o.set(k+l,z);else o.delete(k+l)}return o},sq=a=>mul(a,a);
 const[f,a,b,c,d,e,r,s]=Array.from({length:8},(_,i)=>v(i)),K=[[f,d,e],[d,a,c],[e,c,b]],tr=add(add(f,a),b),P=[add(b,a,-1n),sc(add(d,mul(r,a)),-2),sc(add(e,mul(s,b),-1n),2)];
 const all=[];
 for(let group=0;group<2;group++){
  let rho=group?s:r,sign=group?-1:1,col=group?2:1;
  const pa=(A,B,k=1n)=>[add(A[0],B[0],k),add(A[1],B[1],k)],ps=(A,k)=>[sc(A[0],k),sc(A[1],k)];
  const pm=(A,B)=>{let bd=mul(A[1],B[1]);return[add(mul(A[0],B[0]),bd,2n),add(add(mul(A[0],B[1]),mul(A[1],B[0])),mul(rho,bd),2n)]},pq=A=>pm(A,A),pc=A=>pm(pm(A,A),A),cp=x=>[x,Z()];
  let Q=P.map((pi,i)=>[add(pi,K[i][0],BigInt(2*sign)),sc(K[i][col],2)]),R=[add(sc(tr,-2),P[0],BigInt(sign)),P[col]];
  const C=pa(pa(ps(pm(Q[0],pa(pq(Q[1]),pq(Q[2]),-1n)),3),ps(pm(cp(r),pc(Q[1])),2)),ps(pm(cp(s),pc(Q[2])),2));
  let pd=Q.reduce((t,qi,i)=>pa(t,pm(cp(P[i]),qi)),cp(Z())),qnorm=Q.reduce((t,qi)=>pa(t,pq(qi)),cp(Z()));
  let cpq=pa(pa(pa(pm(cp(P[0]),pa(pq(Q[1]),pq(Q[2]),-1n)),ps(pm(cp(P[1]),pm(Q[0],Q[1])),2)),ps(pm(cp(P[2]),pm(Q[0],Q[2])),-2)),pa(ps(pm(cp(mul(r,P[1])),pq(Q[1])),2),ps(pm(cp(mul(s,P[2])),pq(Q[2])),2)));
  let qkq=cp(Z());for(let i=0;i<3;i++)for(let j=0;j<3;j++)qkq=pa(qkq,pm(cp(K[i][j]),pm(Q[i],Q[j])));
  let H=pa(pa(pa(pm(R,pd),cpq),pm(cp(tr),qnorm),-1n),qkq);
  all.push({group,C:C.map(p=>[...p].map(([k,c])=>[k,c.toString()])),H:H.map(p=>[...p].map(([k,c])=>[k,c.toString()]))});
 }
 return {variables:["f","a","b","c","d","e","r","s"],data:all};
}

function cayleyReducedSupportEquations(data) {
 const R=64,Z=()=>new Map(),co=n=>new Map(n?[[0,BigInt(n)]]:[]),v=i=>new Map([[R**i,1n]]),add=(a,b,s=1n)=>{let o=new Map(a);for(let[k,x]of b){let z=(o.get(k)||0n)+s*x;if(z)o.set(k,z);else o.delete(k)}return o},sc=(a,s)=>add(Z(),a,BigInt(s)),mul=(a,b)=>{let o=Z();for(let[k,x]of a)for(let[l,y]of b){let z=(o.get(k+l)||0n)+x*y;if(z)o.set(k+l,z);else o.delete(k+l)}return o},sq=a=>mul(a,a),pow=(a,n)=>{let o=co(1);for(let i=0;i<n;i++)o=mul(o,a);return o};
 const[q,D,X,Y]=Array.from({length:4},(_,i)=>v(i)),qm=add(q,co(-1)),qp=add(q,co(1)),rN=add(mul(qm,X),mul(qp,Y)),sN=add(mul(qm,X),mul(qp,Y),-1n);
 const f4=sc(mul(add(sq(q),co(1)),add(add(mul(qm,sq(X)),mul(qp,sq(Y)),-1n),mul(mul(D,X),Y),2n)),-1);
 const d4=add(add(mul(sq(qm),X),mul(sq(qp),Y),-1n),mul(D,add(X,Y,-1n)),2n);
 const e4=add(add(sc(mul(sq(qm),X),-1),mul(sq(qp),Y),-1n),mul(D,add(X,Y)),2n);
 const vals=[f4,sc(add(co(1),D),4),sc(add(co(1),D,-1n),4),sc(q,4),d4,e4,rN,sN];
 const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b)[a,b]=[b,a%b];return a};
 const reduce=poly=>{let out=new Map(poly);let go=true;while(go){go=false;let chosen;for(let[k,c]of out){let xd=Math.floor(k/(R**2))%R,dd=Math.floor(k/R)%R;if(xd>=2&&dd>=2){chosen=[k,c];break;}}if(chosen){go=true;let[k,c]=chosen;out.delete(k);let shift=k-2*R-2*R**2;out=add(out,new Map([[shift+2*R+2*R**3,-c],[shift+2*R**2,c],[shift+2*R**3,c],[shift,2n*c]]));}}return out};
 const divideLinear=(poly,index,root)=>{let power=R**index,groups=new Map();for(let[k,c]of poly){let e=Math.floor(k/power)%R,key=k-e*power;if(!groups.has(key))groups.set(key,[]);let a=groups.get(key);a[e]=(a[e]||0n)+c;}let out=Z();for(let[key,arr]of groups){let max=arr.length-1,b=arr[max]||0n;for(let i=max-1;i>=0;i--){if(b)out.set(key+i*power,b);b=(arr[i]||0n)+BigInt(root)*b;}if(b!==0n)return null;}return out};
 const strip=poly=>{let factors=[];for(const [idx,root,label]of[[0,1,"q-1"],[0,-1,"q+1"],[1,1,"D-1"],[1,-1,"D+1"],[1,0,"D"],[2,0,"X"],[3,0,"Y"]]){let n=0;while(poly.size){let q=divideLinear(poly,idx,root);if(q===null)break;poly=q;n++;}if(n)factors.push([label,n]);}let g=0n;for(let c of poly.values())g=gcd(g,c);if(g>1n)for(let[k,c]of poly)poly.set(k,c/g);return {factors,g:g.toString(),polynomial:[...poly].map(([k,c])=>({powers:Array.from({length:4},(_,i)=>Math.floor(k/(R**i))%R),c:c.toString()}))}};
 const substitute=poly=>{let out=Z();for(let[key,c]of poly){let er=Math.floor(key/(16**6))%16,es=Math.floor(key/(16**7))%16,t=co(BigInt(c)*(2n**BigInt(4-er-es)));for(let i=0;i<8;i++){let e=Math.floor(key/(16**i))%16;if(e)t=mul(t,pow(vals[i],e));}out=add(out,t);}return strip(reduce(out));};
 return {variables:["q","D","X","Y"],constraint:"(1-D^2)(X^2+Y^2)+2",data:data.data.map(g=>({group:g.group,C:g.C.map(substitute),H:g.H.map(substitute)}))};
}

function verifyCayleyMeanAndConstantIdentities(cayley) {
 const R=64,Z=()=>new Map(),co=n=>new Map(n?[[0,BigInt(n)]]:[]),v=i=>new Map([[R**i,1n]]),add=(a,b,s=1n)=>{let o=new Map(a);for(let[k,c]of b){let z=(o.get(k)||0n)+s*c;if(z)o.set(k,z);else o.delete(k)}return o},sc=(a,s)=>add(Z(),a,BigInt(s)),mul=(a,b)=>{let o=Z();for(let[k,c]of a)for(let[l,d]of b){let z=(o.get(k+l)||0n)+c*d;if(z)o.set(k+l,z);else o.delete(k+l)}return o},sq=a=>mul(a,a),pol=z=>new Map(z.polynomial.map(t=>[t.powers.reduce((s,e,i)=>s+e*R**i,0),BigInt(t.c)]));
 const red=poly=>{let o=new Map(poly);while(true){let chosen;for(let[k,c]of o)if(Math.floor(k/R)%R>=2&&Math.floor(k/R**2)%R>=2){chosen=[k,c];break}if(!chosen)break;let[k,c]=chosen;o.delete(k);let sh=k-2*R-2*R**2;o=add(o,new Map([[sh+2*R+2*R**3,-c],[sh+2*R**2,c],[sh+2*R**3,c],[sh,2n*c]]));}return o};
 const[q,D,X,Y]=Array.from({length:4},(_,i)=>v(i)),qm=add(q,co(-1)),qp=add(q,co(1)),rn=add(mul(qm,X),mul(qp,Y)),sn=add(mul(qm,X),mul(qp,Y),-1n),U=add(sq(X),sq(Y)),V=add(sq(X),sq(Y),-1n),W=mul(X,Y),zeta=add(sq(q),co(-1)),E=add(sq(D),co(-1));
 const a4=sc(add(co(1),D),4),b4=sc(add(co(1),D,-1n),4),c4=sc(q,4),h4=co(4),del4=sc(D,4);
 const f4=sc(mul(add(sq(q),co(1)),add(add(mul(qm,sq(X)),mul(qp,sq(Y)),-1n),mul(mul(D,X),Y),2n)),-1),d4=add(add(mul(sq(qm),X),mul(sq(qp),Y),-1n),mul(D,add(X,Y,-1n)),2n),e4=add(add(sc(mul(sq(qm),X),-1),mul(sq(qp),Y),-1n),mul(D,add(X,Y)),2n),Z4=sc(zeta,8);
 const R1=add(add(add(sc(mul(a4,f4),4),mul(sq(rn),sq(a4))),sc(mul(mul(rn,a4),d4),4)),Z4,-4n);
 const R2=add(add(add(sc(mul(b4,f4),4),mul(sq(sn),sq(b4))),sc(mul(mul(sn,b4),e4),-4)),Z4,-4n);
 const L1=add(add(sc(mul(h4,d4),2),sc(mul(c4,e4),-2)),mul(rn,add(Z4,mul(h4,del4),-1n)),-1n);
 const L2=add(add(sc(mul(c4,d4),2),sc(mul(h4,e4),-2)),mul(sn,add(Z4,mul(h4,del4))),-1n);
 const Dp=add(pol(cayley.data[0].H[0]),pol(cayley.data[0].C[0]),-1n),Dm=add(pol(cayley.data[1].H[0]),pol(cayley.data[1].C[0]),-1n);
 const S1=add(sc(mul(zeta,add(U,mul(q,V))),-1),sc(mul(mul(sq(D),D),W),4));
 const zminus=add(zeta,sq(D),-2n),zplus=add(zeta,sq(D),2n);
 const S2=add(mul(D,add(add(sc(mul(mul(U,zeta),add(sq(q),co(1))),-1),sc(mul(mul(q,zminus),V),2)),sc(add(sq(D),zeta,-1n),8))),sc(mul(mul(zeta,zminus),W),-2));
 const J=add(mul(mul(mul(E,sq(zminus)),zplus),W),mul(mul(D,zeta),add(add(sq(zeta),mul(zeta,sq(D)),4n),sq(sq(D)),-4n)));
 const checks={
 "Cayley R1":red(R1).size===0,"Cayley R2":red(R2).size===0,"Cayley L1":red(L1).size===0,"Cayley L2":red(L2).size===0,
 "Dsum=16(c^2-1)S1":red(add(add(Dp,Dm),sc(mul(zeta,S1),16),-1n)).size===0,
 "Ddiff=8S2":red(add(add(Dp,Dm,-1n),sc(S2,8),-1n)).size===0,
 "eliminate V to J":red(add(mul(E,add(mul(zeta,S2),sc(mul(mul(D,zminus),S1),2))),sc(J,2))).size===0};
 const Ep=add(pol(cayley.data[0].C[1]),pol(cayley.data[0].H[1]),-3n),Em=add(pol(cayley.data[1].C[1]),pol(cayley.data[1].H[1]),-3n);
 for(const[name,p]of[["Cp0",pol(cayley.data[0].C[0])],["Cm0",pol(cayley.data[1].C[0])],["rEp",mul(rn,Ep)],["sEm",mul(sn,Em)]]){let flip=Z();for(let[k,c]of p){let e=Array.from({length:4},(_,i)=>Math.floor(k/R**i)%R);flip=add(flip,new Map([[e[0]+e[1]*R+e[3]*R**2+e[2]*R**3,e[0]%2?-c:c]]));}checks["sign symmetry "+name]=red(add(p,flip,-1n)).size===0;}
 return{checks,all:Object.values(checks).every(Boolean)};
}

function invariantLastBranchEquations(cayley) {
 const B0=64,Z=()=>new Map(),co=n=>new Map(n?[[0,BigInt(n)]]:[]),add=(a,b,s=1n)=>{let o=new Map(a);for(let[k,c]of b){let v=(o.get(k)||0n)+s*c;if(v)o.set(k,v);else o.delete(k)}return o},sc=(a,s)=>add(Z(),a,BigInt(s)),mul=(a,b)=>{let o=Z();for(let[k,c]of a)for(let[l,d]of b){let v=(o.get(k+l)||0n)+c*d;if(v)o.set(k+l,v);else o.delete(k+l)}return o},pow=(a,n)=>{let o=co(1);for(let i=0;i<n;i++)o=mul(o,a);return o},sq=a=>mul(a,a);
 const pol=z=>new Map(z.polynomial.map(t=>[t.powers.reduce((s,e,i)=>s+e*B0**i,0),BigInt(t.c)]));
 const q= new Map([[1,1n]]),D=new Map([[64,1n]]),X=new Map([[64**2,1n]]),Y=new Map([[64**3,1n]]);
 const rN=add(mul(add(q,co(-1)),X),mul(add(q,co(1)),Y)),sN=add(mul(add(q,co(-1)),X),mul(add(q,co(1)),Y),-1n);
 const Ep=add(pol(cayley.data[0].C[1]),pol(cayley.data[0].H[1]),-3n),Em=add(pol(cayley.data[1].C[1]),pol(cayley.data[1].H[1]),-3n);
 const inputs=[["Cp0",pol(cayley.data[0].C[0])],["Cm0",pol(cayley.data[1].C[0])],["rEp",mul(rN,Ep)],["sEm",mul(sN,Em)]];
 const radix=32,Q=new Map([[1,1n]]),DD=new Map([[32,1n]]),U=new Map([[32**2,1n]]),V=new Map([[32**3,1n]]),W=new Map([[32**4,1n]]);
 const vf2=add(sq(U),sq(W),-4n);
 const reduceV=p=>{let o=Z();for(let[k,c]of p){let n=Math.floor(k/(32**3))%32;o=add(o,mul(new Map([[k-(n-n%2)*32**3,c]]),pow(vf2,Math.floor(n/2))));}return o};
 const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b)[a,b]=[b,a%b];return a};
 const results=[];
 for(const[name,poly]of inputs) {
  let flip=Z();for(let[k,c]of poly){let es=Array.from({length:4},(_,i)=>Math.floor(k/(64**i))%64);flip=add(flip,new Map([[es[0]+es[1]*64+es[3]*64**2+es[2]*64**3,es[0]%2?-c:c]]));}
  let sym=add(poly,flip),maxpow=0;
  for(let[k,c]of sym){let ix=Math.floor(k/(64**2))%64,iy=Math.floor(k/(64**3))%64;if((ix+iy)%2)throw Error("not even "+name);maxpow=Math.max(maxpow,Math.floor(ix/2)+Math.floor(iy/2));}
  let inv=Z();for(let[k,c]of sym){let es=Array.from({length:4},(_,i)=>Math.floor(k/(64**i))%64),ix=Math.floor(es[2]/2),iy=Math.floor(es[3]/2),odd=es[2]%2,term=new Map([[es[0]+es[1]*32+odd*32**4,c*(2n**BigInt(maxpow-ix-iy))]]);term=mul(term,pow(add(U,V),ix));term=mul(term,pow(add(U,V,-1n),iy));inv=add(inv,term);}
  inv=reduceV(inv);
  const d=new Map([[1,1n]]),t=new Map([[32,1n]]),uu=new Map([[32**2,1n]]),ww=new Map([[32**3,1n]]),q2=add(co(1),mul(sq(d),t)),Jnum=add(sc(mul(d,ww),4),mul(t,uu),-1n);
  let converted=Z();for(let[k,c]of inv){let es=Array.from({length:5},(_,i)=>Math.floor(k/(32**i))%32),[nq,nd,nu,nv,nw]=es;if(nv>1||nq%2!==nv)throw Error("invariance failed "+name+" "+es);let term=new Map([[nd+nu*32**2+nw*32**3,c]]);term=mul(term,pow(q2,Math.floor(nq/2)));term=mul(term,nv?Jnum:t);converted=add(converted,term);}
  let maxE=0,maxB=0;for(let[k,c]of converted){let nu=Math.floor(k/(32**2))%32,nw=Math.floor(k/(32**3))%32;maxE=Math.max(maxE,nu+nw);maxB=Math.max(maxB,nw);}
  const dtD=new Map([[1,1n]]),dtT=new Map([[64,1n]]),EE=add(sq(dtD),co(-1)),AA=add(add(sq(dtT),dtT,4n),co(-4)),BB=mul(sq(add(dtT,co(-2))),add(dtT,co(2)));
  let final=Z();for(let[k,c]of converted){let nd=k%32,nt=Math.floor(k/32)%32,nu=Math.floor(k/(32**2))%32,nw=Math.floor(k/(32**3))%32;let term=new Map([[nd+nw+(nt+nw)*64,c*(2n**BigInt(nu))*(nw%2?-1n:1n)]]);term=mul(term,pow(AA,nw));term=mul(term,pow(EE,maxE-nu-nw));term=mul(term,pow(BB,maxB-nw));final=add(final,term);}
  let minD=Math.min(...[...final.keys()].map(k=>k%64)),minT=Math.min(...[...final.keys()].map(k=>Math.floor(k/64)));let shifted=Z();for(let[k,c]of final)shifted.set(k-minD-minT*64,c);
  let g=0n;for(let c of shifted.values())g=gcd(g,c);if(g)for(let[k,c]of shifted)shifted.set(k,c/g);
  results.push({name,maxE,maxB,removedD:minD,removedT:minT,g:g.toString(),polynomial:[...shifted].map(([k,c])=>({d:k%64,t:Math.floor(k/64),c:c.toString()}))});
 }
 return results;
}

function verifyLastFourPointElimination(cayley,invariant,expected,modCertificate) {
 const trim=a=>{while(a.length>1&&a.at(-1)===0n)a.pop();return a};
 const gz=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b)[a,b]=[b,a%b];return a};
 const prim=a=>{a=trim(a);let g=a.reduce((s,c)=>gz(s,c),0n);if(!g)return[0n];if(a.at(-1)<0n)g=-g;return a.map(c=>c/g)};
 const add=(a,b,s=1n)=>trim(Array.from({length:Math.max(a.length,b.length)},(_,i)=>(a[i]||0n)+s*(b[i]||0n)));
 const mul=(a,b)=>{let c=Array(a.length+b.length-1).fill(0n);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)c[i+j]+=a[i]*b[j];return trim(c)};
 const prem=(a,b)=>{a=a.slice();while(a.length>=b.length&&!(a.length===1&&!a[0])){let k=a.length-b.length,c=a.at(-1),lc=b.at(-1);a=a.map(x=>x*lc);for(let i=0;i<b.length;i++)a[i+k]-=c*b[i];a=prim(a);}return prim(a)};
 const gcd=(a,b)=>{let degrees=[];a=prim(a);b=prim(b);while(!(b.length===1&&!b[0])){degrees.push([a.length-1,b.length-1]);[a,b]=[b,prem(a,b)];}return {gcd:prim(a),degrees}};
 const divide=(a,b)=>{a=a.slice();let q=Array(a.length-b.length+1).fill(0n);while(a.length>=b.length&&!(a.length===1&&!a[0])){let k=a.length-b.length;if(a.at(-1)%b.at(-1))throw Error("nonintegral exact division");let c=a.at(-1)/b.at(-1);q[k]=c;for(let i=0;i<b.length;i++)a[k+i]-=c*b[i];trim(a);}if(a.some(x=>x))throw Error("nonzero division remainder");return trim(q)};
 const bp=z=>new Map(z.polynomial.map(t=>[t.d+64*t.t,BigInt(t.c)])),ba=(a,b,s=1n)=>{let o=new Map(a);for(let[k,c]of b){let v=(o.get(k)||0n)+s*c;if(v)o.set(k,v);else o.delete(k)}return o};
 const out=p=>[...p].map(([k,c])=>({d:k%64,t:Math.floor(k/64),c}));
 function extract(poly,shift){let A=Array(10).fill(0n),B=Array(10).fill(0n);for(const z of out(poly)){let d=z.d-shift;if(d!==0&&d!==2)throw Error("nonlinear x equation");(d===0?A:B)[z.t]+=z.c}let g=[...A,...B].reduce((s,c)=>gz(s,c),0n);return {A:trim(A.map(c=>c/g)),B:trim(B.map(c=>c/g))};}
 const rows=[extract(ba(bp(invariant[0]),bp(invariant[1])),1),extract(ba(bp(invariant[2]),bp(invariant[3])),1),extract(ba(bp(invariant[2]),bp(invariant[3]),-1n),0)];
 const checks={};
 checks["all four invariant transformations have allowed denominators"]=invariant.every(p=>p.maxE===2&&p.maxB===2&&p.removedD===5&&p.removedT===1);
 checks["three exact linear-in-x coefficient rows"]=JSON.stringify(rows.map(r=>({A:r.A.map(String),B:r.B.map(String)})))===JSON.stringify(expected.rows.map(r=>({A:r.A,B:r.B})));
 const p01=prim(add(mul(rows[0].A,rows[1].B),mul(rows[0].B,rows[1].A),-1n)),p02=prim(add(mul(rows[0].A,rows[2].B),mul(rows[0].B,rows[2].A),-1n));
 checks["first primitive determinant"]=JSON.stringify(p01.map(String))===JSON.stringify(expected.minors[0].p);
 checks["second primitive determinant"]=JSON.stringify(p02.map(String))===JSON.stringify(expected.minors[1].p);
 const G=gcd(p01,p02);
 checks["exact QQ gcd is (t+2)^2"]=JSON.stringify(G.gcd.map(String))===JSON.stringify(["4","4","1"]);
 const Q0=divide(p01,[4n,4n,1n]),Q1=divide(p02,[4n,4n,1n]);
 checks["exact quotient coefficient arrays"]=JSON.stringify(Q0.map(String))===JSON.stringify(modCertificate.quotient0)&&JSON.stringify(Q1.map(String))===JSON.stringify(modCertificate.quotient1);
 const P=103n,mod=a=>(a%P+P)%P;
 checks["degrees remain 16 and 15 modulo 103"]=Q0.length===17&&Q1.length===16&&mod(Q0.at(-1))===12n&&mod(Q1.at(-1))===3n;
 const BZ=add(mul(modCertificate.bezout0.map(BigInt),Q0),mul(modCertificate.bezout1.map(BigInt),Q1)).map(mod);
 checks["explicit mod103 Bezout identity"]=BZ[0]===1n&&BZ.slice(1).every(x=>x===0n);
 return {checks,all:Object.values(checks).every(Boolean),euclidean_degree_trace:G.degrees,gcd:G.gcd.map(String),quotient_degrees:[Q0.length-1,Q1.length-1]};
}

const EXPECTED={"rows":[{"A":["-1536","1280","-896","-448","1056","80","-264","-68","20","-2"],"B":["0","-1536","1664","320","-32","240","-296","-116","-14","-1"],"scale":"2"},{"A":["0","384","-1024","320","688","-328","-136","48","19","-4"],"B":["0","-384","704","-384","-32","296","-148","-20","24","4"],"scale":"2"},{"A":["-1024","896","384","-288","64","72","-8","-14","4"],"B":["512","-1152","192","352","144","104","-76","-14","5"],"scale":"2"}],"minors":[{"i":0,"j":1,"p":["0","-589824","983040","376832","-1171456","8192","356352","171008","195072","-263168","-157440","111424","36960","-17312","-1712","1236","-98","5","12"]},{"i":0,"j":2,"p":["393216","-425984","-425984","32768","143360","411648","235520","-157696","-228608","-17024","76928","14208","-14704","-3048","1288","104","-85","3"]},{"i":1,"j":2,"p":["0","196608","-98304","-540672","147456","497664","87040","-230912","-232192","107008","129280","-36352","-28832","7384","2996","-726","-111","36"]}],"gcd":["4","4","1"]};
const MODULAR_CERTIFICATE={"quotient0":["0","-147456","393216","-262144","-129024","196608","-75264","68864","-1280","-81728","42688","5600","-7032","1304","26","-43","12"],"quotient1":["98304","-204800","73728","-14336","31744","74752","-23808","-34304","-16896","21216","2240","-3992","-244","480","-97","3"],"p":103,"degrees":[16,15],"leading":[12,3],"resultant":52,"bezout0":[66,11,31,91,26,93,63,96,59,72,43,42,8,92,74],"bezout1":[27,78,75,42,54,20,80,80,20,98,47,53,21,13,83,13],"bezout_check":[1]};

function runCompleteFourPointVerification() {
  const original=buildOrthogonalSupportEquations();
  const cayley=cayleyReducedSupportEquations(original);
  const meansAndConstants=verifyCayleyMeanAndConstantIdentities(cayley);
  const invariant=invariantLastBranchEquations(cayley);
  const elimination=verifyLastFourPointElimination(cayley,invariant,EXPECTED,MODULAR_CERTIFICATE);
  if(!meansAndConstants.all || !elimination.all) throw new Error("Exact four-point exclusion certificate failed");
  return {
    arithmetic:"JavaScript BigInt over Z; final explicit Bezout check modulo 103",
    means_and_constant_identities:meansAndConstants,
    elimination,
    all:true
  };
}

console.log(JSON.stringify(runCompleteFourPointVerification(),null,2));
