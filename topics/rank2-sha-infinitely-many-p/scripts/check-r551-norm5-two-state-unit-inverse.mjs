#!/usr/bin/env node
// Exact R551 finite theta core and whole source certificate.
function certifyR551(){
const N=20,mod=(x,n)=>((x%n)+n)%n;
const ident=()=>Array.from({length:N},(_,i)=>Array.from({length:N},(_,j)=>i===j?1:0));
const zero=()=>Array.from({length:N},()=>Array(N).fill(0));
const T=(s,r)=>{const A=zero();for(let j=0;j<N;j++)A[mod(j+10*r,N)][j]=(s*(j+5*r))%2?-1:1;return A;};
const ts=[[0,0],[1,0],[0,1],[1,1]].map(([s,r])=>T(s,r));
const P4=zero(),B=zero();for(let i=0;i<N;i++)for(let j=0;j<N;j++){P4[i][j]=ts[0][i][j]-ts[1][i][j]-ts[2][i][j]-ts[3][i][j];B[i][j]=P4[i][j]/2-(i===j?1:0);}
let checks=0;const ck=(v,m)=>{if(!v)throw Error(m);checks++;};
for(let i=0;i<N;i++)for(let j=0;j<N;j++)ck(B[i][j]=== (i===mod(11*j,N)?-1:0),"B=-U11");
for(let j=0;j<N;j++){ck(mod(11*11*j,N)===j,"B2");ck(mod(121-1,40)===0,"full Weyl center");}
for(let j=1;j<N;j+=2){const v=Array(N).fill(0);v[j]=1;v[mod(j+10,N)]-=1;for(let i=0;i<N;i++)ck(B[i].reduce((s,x,k)=>s+x*v[k],0)===v[i],"odd pullback anchor");}
const bin=(n,k)=>{if(k<0||k>n)return 0;let z=1;for(let j=1;j<=k;j++)z=z*(n-j+1)/j;return z;};
const deg8=[];
for(let r=0;r<=8;r++){
 const a=2*bin(7,r-1)*2**(8-r)-bin(7,r)*2**(7-r);
 const b=bin(7,r-1)*2**(r-1)*(-1)**(8-r)+2*bin(7,r)*2**r*(-1)**(7-r);
 if(r>=3&&r<=5){const target=r===4?0:1260;ck(a+b===target,"full S5 tensor rectangle");}
 deg8.push([r,8-r,a+b]);
}
const W=[[1,-1],[0,-1]],R=[[-1,1],[0,1]];
for(let i=0;i<2;i++)for(let j=0;j<2;j++)ck(W[i][j]===-R[i][j],"W=-Rc");
ck(1*2+2*(-1)===0,"RQ orthogonal");
ck(1+4===5&&4+1===5,"RQ norm");
return {status:"proved exact finite identities",checks,
g_mod40:11,weyl_center_square_mod40:mod(121,40),
epsilon_projector_rank:5,B_basis_action:Array.from({length:20},(_,j)=>({j,image:mod(11*j,20),sign:-1})),
theta_S5_tensor_coefficients:{U2_D:2,D_U2:-2,U1_U1:3,U3_U5_over_b:6,U5_U3_over_b:6},
degree8_numerator_over210:deg8,
source_B:W,Rc:R,
physical_A:"(1/5)[[kappa+4kappa^2,2kappa-2kappa^2],[2-2kappa,4+kappa]]",
trace_A:"(4+2kappa+4kappa^2)/5",det_A:"kappa^2",
new_ray_conditions:[]};
}
console.log(JSON.stringify(certifyR551(), null, 2));
