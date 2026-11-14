#!/usr/bin/env node
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

const inputs={"EStar":[{"real":"-461/1442","delta":"423/1442"},{"real":"99/206","delta":"45/206"},{"real":"-235/1442","delta":"-481/1442"},{"real":"-1/7","delta":"4/7"},{"real":"9/1442","delta":"13/1442"},{"real":"-27/721","delta":"10/721"}],"Q0":[{"real":"-8/7","delta":"-3/7"},{"real":"1","delta":"0"},{"real":"-1/2","delta":"1/2"},{"real":"0","delta":"0"},{"real":"-1/14","delta":"-3/14"},{"real":"13/14","delta":"-3/14"}],"Qb":[{"real":"11/14","delta":"-23/14"},{"real":"19/2","delta":"7/2"},{"real":"5/2","delta":"11/2"},{"real":"0","delta":"0"},{"real":"1/7","delta":"24/7"},{"real":"-215/14","delta":"27/14"}],"Y":[{"real":"0","delta":"1"},{"real":"0","delta":"2"},{"real":"5/2","delta":"1/2"},{"real":"5/2","delta":"-1/2"},{"real":"1","delta":"0"},{"real":"2","delta":"0"}],"W":[{"real":"0","delta":"1"},{"real":"0","delta":"2"},{"real":"5/2","delta":"1/2"},{"real":"5/2","delta":"-1/2"},{"real":"0","delta":"3"},{"real":"4","delta":"0"}],"Wp":[{"real":"2","delta":"2"},{"real":"0","delta":"2"},{"real":"2","delta":"2"},{"real":"0","delta":"0"},{"real":"3","delta":"1"},{"real":"4","delta":"0"}],"E41554":[["59","15"],["-1","-68"],["-46","15"],["158","0"],["-82","-60"],["-8","23"]],"K113918":[["163","83"],["-7","-98"],["-46","107"],["0","0"],["276","170"],["42","-63"]]};
function qr(s){const a=s.split("/");return q(a[0],a[1]||1);}
const fromD=o=>c(qr(o.real),qr(o.delta));
const fromO=o=>c(sub(qr(o[0]),div(qr(o[1]),q(2))),div(qr(o[1]),q(2)));
const toO=x=>[qs(add(x[0],x[1])),qs(mul(q(2),x[1]))];
const E=inputs.EStar.map(fromD),Q0=inputs.Q0.map(fromD),Qb=inputs.Qb.map(fromD),Y=inputs.Y.map(fromD),W=inputs.W.map(fromD),Wp=inputs.Wp.map(fromD);
const EE=inputs.E41554.map(fromO),KK=inputs.K113918.map(fromO);
const om=c(q(-1,2),q(1,2)),del=c(0,1),g103=ca(c(11),cm(c(2),om));
const L=E.map(x=>cm(c(721),x)),N=1090152n,mod=2n*N;
if(!ce(dot(L,L),c(N)))throw Error("degree");
for(const a of [Q0,Qb,Y,W,Wp])if(!ce(dot(E,a),c()))throw Error("orthogonal");
const ints=L.map(toO);if(ints.some(r=>r.some(x=>x.includes("/"))))throw Error("not CM integral");
const parity=ints.map(r=>r.map(x=>Number((BigInt(x)%2n+2n)%2n)));
if(parity.some(r=>r[0]===0&&r[1]===0))throw Error("unexpected even coefficient");
const e=cd(ca(c(3),cm(c(8),om)),c(1106)),k=cm(e,cd(ca(c(233),cm(c(24),om)),c(721)));
for(let i=0;i<6;i++)if(!ce(E[i],ca(cm(e,EE[i]),cm(k,KK[i]))))throw Error("E/K transportation mismatch");
const mmO=(a,b,m)=>[((a[0]*b[0]-a[1]*b[1])%m+m)%m,((a[0]*b[1]+a[1]*b[0]-a[1]*b[1])%m+m)%m];
const odd=N/8n,gg=[1n+2n*odd,N],gg2=mmO(gg,gg,mod),gg4=mmO(gg2,gg2,mod);
if(gg[0]%16n!==11n||gg[1]%16n!==8n||gg[0]%odd!==1n||gg[1]%odd!==0n)throw Error("CRT representative");
if(gg2[0]!==1n+N||gg2[1]!==0n||gg4[0]!==1n||gg4[1]!==0n)throw Error("full center");
const anchor=cm(c(42),cm(del,g103));
if(!eq(norm(anchor),q(N,2)))throw Error("Theta anchor");
const frame=[Y,W,Wp,Q0,Qb,E],inv=cinv(frame),G=frame.map(a=>frame.map(b=>dot(a,b)));
const gamma=ca(c(3),om),Tc=Y.map((x,i)=>cs(cm(gamma,x),c(i===3?34:0))),C=[c(q(1,2)),c(),cm(c(q(1,2)),cm(om,om)),cm(c(q(-1,2)),om),c(q(-1,2)),c()];
const TcCoords=mm([Tc],inv)[0],CCoords=mm([C],inv)[0];
return {Tc_in_common_frame:TcCoords.map(cj),C_in_common_frame:CCoords.map(cj),input_coordinates:["xi1","xi2","xi3","x","c","d0"],E_star:inputs.EStar,L721E_star_CM:ints,L_mod2:parity,degree:String(N),degree_factorization:"2^3*3^3*7^2*103",ordinary_modulus:String(mod),g_representative:gg.map(String),g_square:gg2.map(String),g_fourth:gg4.map(String),base_pi_mod27:["1","0"],pi_mod49:["2","0"],pi_mod103:["1","0"],g_mod16:["11","8"],Theta_CM_anchor:toO(anchor),anchor_norm:qs(norm(anchor)),whole_core_square:"identity by full Heisenberg center and nonzero Theta anchor",E_star_in_E41554_K113918:[toO(e),toO(k)],retained_Y_W_Wprime_Gram:G.slice(0,3).map(r=>r.slice(0,3).map(cj)),full_frame:frame.map(r=>r.map(cj)),full_frame_inverse:inv.map(r=>r.map(cj)),full_frame_determinant:cj(cdet(frame)),hidden_rectangular_core:"chi^(a+b)*lambda^(a+b+2c)",common_even_depth_core:"lambda^(6n) at common depth 2n",warning:"No one-layer scalar assigned; original Tc/Z and U hidden terms must be retained."};

})();
process.stdout.write(JSON.stringify(certificate,null,2)+"\n");
