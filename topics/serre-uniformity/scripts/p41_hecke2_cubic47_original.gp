\\ Actual order-three jets for all three normalized 2-isogenies.
p41h2c_encode(M)=vector(matsize(M)[1],i,vector(matsize(M)[2],j,lift(M[i,j])));
p41h2c_velu(P,root,tt,eps,ev,u,z)={
 my(d=P[1]-root,b=p41l_inv(polcoef(lift(d),0,ev),u,z)*eps^0);
 for(k=1,2,b*=2-d*b);if(d*b!=1,error("T2 cubic unit denominator"));
 [P[1]+tt*b,P[2]*(1-tt*b^2)];
};
p41_hecke2_cubic47(input,path)={
 my(q=47^4,order=4,f=sum(k=1,81,input[1][k]*'t^(k-1)),z=ffgen(Mod(1,47)*f),u=Mod(Mod(1,q)*'t,f),
 ii=sum(k=1,80,input[2][k]*u^(k-1)),ew=sum(k=1,80,input[3][k]*u^(k-1)),
 ev=varhigher("ep",'t),eps=Mod(u^0*ev,ev^order),P,Q,P0,Q0,root0=Mod(input[6][1],q)+Mod(input[6][2],q)*ii,
 root,iv,tt,A,B,vals,reps=List(),neg,Es,aa=vector(159),bb=vector(159),power=u^0,HA,HB,check);
 P=vector(2,j,sum(k=0,3,sum(h=1,80,input[4][j][k+1][h]*u^(h-1))*eps^k));
 Q=vector(2,j,sum(k=0,3,sum(h=1,80,input[5][j][k+1][h]*u^(h-1))*eps^k));P0=P;Q0=Q;
 root=root0*eps^0;iv=p41l_inv(3*root0^2+1,u,z);
 for(k=1,3,root-=polcoef(lift(root^3+root+32+eps),k,ev)*iv*eps^k);
 if(root^3+root+32+eps!=0,error("T2 actual cubic kernel equation"));
 tt=3*root^2+1;A=1-5*tt;B=32+eps-7*root*tt;
 P=p41h2c_velu(P,root,tt,eps,ev,u,z);Q=p41h2c_velu(Q,root,tt,eps,ev,u,z);
 check=p41j_add(P0,[root,0*eps],eps^0,u,z,order);
 if(P!=[P0[1]+check[1]-root,P0[2]+check[2]],error("T2 independent addition Velu P"));
 check=p41j_add(Q0,[root,0*eps],eps^0,u,z,order);
 if(Q!=[Q0[1]+check[1]-root,Q0[2]+check[2]],error("T2 independent addition Velu Q"));
 Q=p41j_mul(Q,21,A,u,z,order);
 if(P[2]^2!=P[1]^3+A*P[1]+B||Q[2]^2!=Q[1]^3+A*Q[1]+B,error("T2 cubic target curve"));
 if(p41j_mul(P,41,A,u,z,order)!=[0]||p41j_mul(Q,41,A,u,z,order)!=[0],error("T2 cubic target torsion"));
 vals=p41a_eisenstein(P,Q,A,u,z,order,ev);
 for(k=1,1680,neg=lift(Mod(-(k%41),41))+41*lift(Mod(-(k\41),41));if(k<neg,listput(reps,k+1)));
 reps=Vec(reps);if(#reps!=840,error("T2 cubic odd representatives"));
 Es=vector(order,n,Mod(matrix(80,840,i,j,lift(polcoef(lift(polcoef(lift(vals[reps[j]]),n-1,ev)),i-1))),q));
 for(k=1,159,aa[k]=trace(ew*power)/4;bb[k]=-trace(ii*ew*power)/4;power*=u);
 HA=matrix(80,80,i,j,aa[i+j-1]);HB=matrix(80,80,i,j,bb[i+j-1]);
 write(path,[p41h2c_encode(HA),p41h2c_encode(HB),vector(order,n,p41h2c_encode(Es[n])),
 vector(2,j,vector(order,n,p41l_vec(polcoef(lift(P[j]),n-1,ev)))),
 vector(2,j,vector(order,n,p41l_vec(polcoef(lift(Q[j]),n-1,ev)))),
 vector(order,n,p41l_vec(polcoef(lift(root),n-1,ev)))]);
 print("Actual normalized2-isogeny cubic jets, independent Velu addition and1680 Eisenstein jets PASS ",getwalltime());
};
