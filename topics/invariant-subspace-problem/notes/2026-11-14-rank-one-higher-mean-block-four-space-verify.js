"use strict";
function verifyRankOneHigherMeanBlocks(){
 const names=["h0","h1","h2","h3","v0","v1","v2","X","Y","Z","U","W","hr","vr","alpha","s"],D=names.length,zk="0".repeat(D);
 const zero=()=>new Map(),cn=n=>n?new Map([[zk,BigInt(n)]]):zero(),variable=i=>new Map([[Array.from({length:D},(_,j)=>i===j?"1":"0").join(""),1n]]);
 const add=(...ps)=>{const r=zero();for(const p of ps)for(const[k,v]of p)r.set(k,(r.get(k)||0n)+v);for(const[k,v]of r)if(!v)r.delete(k);return r},sc=(p,c)=>new Map([...p].map(([k,v])=>[k,v*BigInt(c)]).filter(([k,v])=>v!==0n));
 const mul=(p,q)=>{const r=zero();for(const[k,v]of p)for(const[l,w]of q){const m=[...k].map((e,i)=>(parseInt(e,36)+parseInt(l[i],36)).toString(36)).join("");r.set(m,(r.get(m)||0n)+v*w)}for(const[k,v]of r)if(!v)r.delete(k);return r},prod=(...ps)=>ps.reduce(mul,cn(1)),pow=(p,n)=>prod(...Array(n).fill(p));
 const [h0,h1,h2,h3,v0,v1,v2,X,Y,Z,U,W,hr,vr,alpha,s]=names.map((_,i)=>variable(i)),jets=[X,Y,Z,U],checks=[];
 const eq=(name,p,q)=>{if(add(p,sc(q,-1)).size)throw Error(name);checks.push(name)};
 function block(h,v){let H=zero(),V=zero();for(let i=0;i<h.length;i++)for(let j=0;j<h.length;j++){if(i+j<h.length)H=add(H,prod(h[i+j],jets[i],jets[j]));for(let k=0;k<h.length;k++)if(i+j+k<v.length)V=add(V,prod(v[i+j+k],jets[i],jets[j],jets[k]));}return {H,V};}
 const A=add(cn(1),sc(h0,-6),sc(v0,4)),B=sc(add(v1,sc(h1,-1)),12),C=sc(add(v2,sc(h2,-1)),12),E=sc(add(sc(v2,2),sc(h2,-1)),6);
 let b=block([h0,h1,h2],[v0,v1,h2]);
 let actual=add(pow(X,3),sc(prod(X,b.H),-6),sc(b.V,4),sc(prod(X,hr,W,W),-6),sc(prod(vr,W,W,W),4));
 let want=add(prod(X,add(prod(A,X,X),prod(B,X,Y),sc(prod(h2,Y,Y),6),sc(prod(hr,W,W),-6))),sc(prod(vr,W,W,W),4));eq("n3 order2 complete tensor",actual,want);
 b=block([h0,h1,h2],[sc(v0,2),sc(h1,2),h2]);
 actual=add(sc(pow(X,3),2),sc(prod(X,b.H),-12),sc(b.V,4),sc(prod(X,hr,W,W),-12),sc(prod(vr,W,W,W),8));
 want=sc(add(prod(X,X,add(prod(A,X),sc(prod(h2,Z),-6))),sc(prod(X,hr,W,W),-6),sc(prod(vr,W,W,W),4)),2);eq("n3 order1 complete twice tensor",actual,want);
 b=block([h0,h1,h2,h3],[v0,v1,v2,h3]);
 actual=add(pow(X,3),sc(prod(X,b.H),-6),sc(b.V,4));
 want=add(prod(A,X,X,X),prod(B,X,X,Y),prod(C,X,X,Z),prod(E,X,Y,Y),sc(prod(h3,X,Y,Z),12),sc(prod(h3,Y,Y,Y),4));eq("n4 order3 complete tensor",actual,want);
 b=block([h0,h1,h2,h3],[sc(v0,2),sc(v1,2),sc(h2,2),h3]);
 actual=add(sc(pow(X,3),2),sc(prod(X,b.H),-12),sc(b.V,4));
 want=sc(add(prod(A,X,X,X),prod(B,X,X,Y),sc(prod(h2,X,Y,Y),6),sc(prod(h3,X,X,U),-6),sc(prod(h3,Y,Y,Y),2)),2);eq("n4 order2 complete twice tensor",actual,want);
 const c3=add(prod(A,X,X,X),sc(prod(h2,X,X,Z),-6),sc(prod(vr,alpha,X,W,W),-12),sc(prod(vr,W,W,W),4));
 const r3=add(sc(prod(vr,pow(add(W,sc(prod(alpha,X),-1)),3)),4),prod(X,X,add(prod(add(A,sc(prod(vr,alpha,alpha,alpha),4)),X),sc(prod(h2,Z),-6),sc(prod(vr,alpha,alpha,W),-12))));
 eq("n3 shifted physical cube",c3,r3);
 const c4=add(prod(A,X,X,X),prod(B,X,X,Y),sc(prod(h3,alpha,X,Y,Y),6),sc(prod(h3,X,X,U),-6),sc(prod(h3,Y,Y,Y),2));
 const r4=add(sc(prod(h3,pow(add(Y,prod(alpha,X)),3)),2),prod(X,X,add(prod(add(A,sc(prod(h3,alpha,alpha,alpha),-2)),X),prod(add(B,sc(prod(h3,alpha,alpha),-6)),Y),sc(prod(h3,U),-6))));
 eq("n4 shifted tangent cube",c4,r4);
 const K=[[0,0,0,0,5,-1],[0,0,0,-32,5,-1],[0,0,54,-4,5,0],[0,-32,-4,-8,0,0],[5,5,5,0,0,0],[-1,-1,0,0,0,0]].map(r=>r.map(BigInt));
 function bin(n,k){if(k<0||k>n)return 0n;let r=1n;for(let i=1;i<=k;i++)r=r*BigInt(n-k+i)/BigInt(i);return r}
 function symbolicTaylor(i,l){let r=zero();for(let j=i;j<6;j++)for(let k=l;k<6;k++)r=add(r,sc(pow(s,j-i+k-l),K[j][k]*bin(j,i)*bin(k,l)));return r}
 const q=sc(prod(s,s,add(s,cn(-2)),add(s,cn(6))),-1);
 eq("generic p0 leading",symbolicTaylor(0,2),sc(q,-1));eq("generic p1 leading",symbolicTaylor(1,1),sc(q,2));eq("generic p2 Taylor leading",symbolicTaylor(2,0),sc(q,-1));
 eq("generic top coefficient",sc(prod(h3,sc(q,2),add(pow(sc(q,2),2),sc(prod(sc(q,-1),sc(q,-1)),3))),4),sc(prod(h3,q,q,q),56));
 function numericLeading(source,infinity=false){const ans=[];for(let i=0;i<3;i++){const a=Array(6).fill(0n);if(infinity){for(let k=0;k<6;k++)a[5-k]=K[5-i][k];}else{for(let l=0;l<6;l++)for(let j=i;j<6;j++)for(let k=l;k<6;k++)a[l]+=K[j][k]*bin(j,i)*bin(k,l)*source**BigInt(j-i+k-l);}let o=a.findIndex(x=>x!==0n);ans.push({order:o,coefficient:a[o]});}return ans}
 const contact=[];
 for(const [label,source,inf,orders,coeffs,top] of [
 ["0",0n,false,[4,3,2],[5n,-32n,54n],-234752n],
 ["2",2n,false,[3,2,1],[16n,-16n,-16n],32768n],
 ["-6",-6n,false,[3,2,1],[-144n,144n,144n],-23887872n],
 ["infinity",0n,true,[4,3,2],[-1n,5n,-8n],980n]
 ]){const c=numericLeading(source,inf);if(c.some((a,i)=>a.order!==orders[i]||a.coefficient!==coeffs[i]))throw Error("contacts "+label);const a=c.map(z=>z.coefficient),z=4n*a[1]*(a[1]*a[1]+3n*a[0]*a[2]);if(z!==top||z===0n)throw Error("top "+label);contact.push({point:label,orders,coefficients:a.map(String),top_multiplier:z.toString()});checks.push("original contact and nonzero top "+label);}
 return {status:"PASS",arithmetic:"exact BigInt polynomial identities; original K finite/infinite Taylor contacts",checks:checks.length,identities:checks,contacts:contact};
}
if(typeof module!=="undefined")module.exports={verifyRankOneHigherMeanBlocks};
if(typeof require!=="undefined"&&typeof module!=="undefined"&&require.main===module)process.stdout.write(JSON.stringify(verifyRankOneHigherMeanBlocks(),null,2)+"\n");
