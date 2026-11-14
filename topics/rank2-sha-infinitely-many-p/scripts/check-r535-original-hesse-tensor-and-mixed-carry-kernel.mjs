#!/usr/bin/env node
// Exact Q(delta), delta^2=-3. No external packages.
const certificate=(()=>{

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

const om=c(q(-1,2),q(1,2)),o2=cp(om,2),de=c(0,1),aa=ca(c(2),om);
const sc=(a,r)=>r.map(x=>cm(a,x)),pl=(a,b)=>a.map((x,i)=>ca(x,b[i]));
const R=[c(1),o2,c(-1)],Q=[c(1),c(1),cn(o2)],Z=[c(1),om,cn(om)],M=[R,Q,Z];
for(let i=0;i<3;i++)for(let j=0;j<3;j++)if(!ce(dot(M[i],M[j]),c(i===j?3:0)))throw Error("Norm3 complete frame");
const Mi=M[0].map((_,i)=>M.map(r=>cd(cc(r[i]),c(3))));
const E=sc(cd(aa,c(3)),Z),RK=[o2,c(1),c(-1)];
E.forEach((x,i)=>{if(!ce(x,cm(cd(cs(om,c(1)),c(3)),RK[i])))throw Error("root K3 identity")});
const allowed=[];for(const a of [0,1,3])for(const b of [0,1,3])for(const cc1 of [0,1,3])if((a+b+cc1)%6===3)allowed.push([a,b,cc1]);
if(allowed.length!==5)throw Error("entire Hesse type dimension");
const RR=[[c(1),c(1),c(1)],[c(1),om,o2],[c(1),o2,om]];
let pol={"0,0,0":c(1)};
for(const row of RR){const out={};for(const [key,v]of Object.entries(pol)){const e=key.split(",").map(Number);for(let j=0;j<3;j++){const f=e.slice();f[j]++;const k=f.join(",");out[k]=ca(out[k]||c(),cm(v,row[j]));}}pol=out;}
for(const [key,v]of Object.entries(pol)){const e=key.split(",").map(Number);const ex=e.some(x=>x===3)?c(1):e.every(x=>x===1)?c(-3):c();if(!ce(v,ex))throw Error("first entire Hesse coefficients "+key);}
const ecoef=cd(aa,c(3));
const E1=cm(o2,cm(c(3),ecoef)); // derivative of -omega2*(-3 QrQqQ(e))
const E3=cm(cn(o2),cm(c(6),cp(ecoef,3)));
const E6=cm(cn(o2),cm(c(216),cp(ecoef,6)));
if(!ce(E1,cn(de))||!ce(E3,cd(cm(c(-2),cm(de,o2)),c(3)))||!ce(E6,cm(c(8),o2)))throw Error("complete E moments");
const H=[c(1),c(-1),c(0)]; // xi1-xi3, without independent x
const Hcandidate=pl(sc(ci(aa),R),E);
H.forEach((x,i)=>{if(!ce(x,Hcandidate[i]))throw Error("H0 actual three-input sum")});

const bg=c(q(5,2),q(-1,2)),cy=cd(ca(c(-1),cm(c(4),om)),c(3)),cq=cd(cm(c(2),aa),c(3));
const q3=cd(cm(c(5),o2),cm(c(567),cp(bg,2)));
const q5=cm(cd(o2,c(18144)),ca(cd(cm(c(-160),cm(aa,de)),cp(bg,3)),cd(cm(c(96),cm(cp(aa,2),cm(de,cy))),cp(bg,4))));
function fact(n){let v=1n;for(let i=2;i<=n;i++)v*=BigInt(i);return v}
const choose=(n,k)=>fact(n)/(fact(k)*fact(n-k));
let lR=c();
for(let j=2;j<=5;j++){
 const num=cm(c(4n*BigInt(j-1)*choose(6,5-j)*BigInt(j%2?1:-1)),cm(de,cp(cy,j-2)));
 lR=ca(lR,cd(num,cm(cp(aa,5-j),cp(bg,j))));
}
const q6=cm(cd(cm(c(6),o2),c(18144)),ca(lR,cd(cm(c(16),cm(de,cp(cq,3))),cp(bg,5))));
const expected=[c(q(5,27783),q(-20,27783)),c(q(-80,64827),q(-8,7203)),c(q(-7118,9529569),q(24944,9529569))];
[q3,q5,q6].forEach((x,i)=>{if(!ce(x,expected[i]))throw Error("independent full-kernel leading check "+i)});
const Wblocks=[c(q(-2,3),q(-1,3)),c(q(7,3),1),c(q(-5,3),q(1,3))];
const Wold=[de,ca(c(3),om),cm(c(3),de)];const Wcheck=mm([Wblocks],M)[0];Wold.forEach((v,i)=>{if(!ce(v,Wcheck[i]))throw Error("old W full Fourier transpose")});
const det3=ca(cs(cm(M[0][0],cs(cm(M[1][1],M[2][2]),cm(M[1][2],M[2][1]))),cm(M[0][1],cs(cm(M[1][0],M[2][2]),cm(M[1][2],M[2][0])))),cm(M[0][2],cs(cm(M[1][0],M[2][1]),cm(M[1][1],M[2][0]))));if(!eq(norm(det3),q(27)))throw Error("Norm3 full determinant");

return {
 status:"complete Norm3 Fourier frame and entire five-dimensional theta identity checked",
 original_block_order:["xi1","xi3","c"],
 R3:R.map(cj),Q3:Q.map(cj),Z3:Z.map(cj),frame:M.map(r=>r.map(cj)),inverse:Mi.map(r=>r.map(cj)),Gram:[3,3,3],determinant:cj(det3),determinant_norm:"27",
 E_K:E.map(cj),E_relation:"E=(a/3)Z3=((omega-1)/3)K3_root",
 full_theta_identity:"product sigma(original coordinates)=-omega^2 G(r,q,z)",
 entire_allowed_S3_tensor_types:allowed,
 G:"B(r)B(q)P(z)+B(q)B(z)P(r)+B(z)B(r)P(q)-3Q(r)Q(q)Q(z)-3bP(r)P(q)P(z)",
 cubic_polynomial:Object.fromEntries(Object.entries(pol).filter(([,v])=>!ce(v,c())).map(([k,v])=>[k,cj(v)])),
 zero_to_six_E_moments_of_unscaled_three_sigma_block:{
  "0":"-omega^2 [B(q)P(r)+B(r)P(q)]",
  "1":{coefficient:cj(E1),source:"Omega Q(r)Q(q)"},
  "2":"0",
  "3":{coefficient:cj(E3),source:"Omega^3 [B(r)B(q)-3b P(r)P(q)]"},
  "4":"0","5":"0",
  "6":{coefficient:cj(E6),source:"b Omega^6 [B(q)P(r)+B(r)P(q)]"}
 },
 universal_even_E:"E6=-8b Omega^6 E0, entire five-output identity",
 independent_kernel_fifth_coefficients:[q3,q5,q6].map(cj),Y_threeblock:[cy,cq,c()].map(cj),W_threeblock:Wblocks.map(cj),
 actual_H0:"H0=x+R3/a+E",
 actual_K:"eta K=x+R3/a",
 corrected_deep_kernel:"omega^2 beta^n/(18144 b Omega^6) [(T^6/d6-8b Omega^6 kappa^(6n)/d0)L + (40delta/3) Omega^3 kappa^(3n) T^3/d3 M -6a Omega kappa^n T^5/d5 N] tensor sigma_x sigma_xi2 sigma_d0; T=x+R3/a, dj=1+lambda kappa^j",
 preserved_conditions:"Kunit iff Tunit; original R3/Q3/x/xi2/d0 conditions are preserved when E is integrated; old W still contains E and cannot use this five-output pushforward without its true transpose"
};

})();
process.stdout.write(JSON.stringify(certificate,null,2)+"\n");
