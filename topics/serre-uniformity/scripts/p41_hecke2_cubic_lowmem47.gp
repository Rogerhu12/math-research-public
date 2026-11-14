\\ Same1680 Eisenstein jets, with one40-denominator row retained at a time.
p41h2c_invbatch(ds,u,z)={
 my(n=#ds,prefix=vector(#ds),iv=vector(#ds),back=u^0);
 for(k=1,n,prefix[k]=back;back*=ds[k]);back=p41l_inv(back,u,z);
 forstep(k=n,1,-1,iv[k]=back*prefix[k];back*=ds[k]);
 if(back!=1,error("T2 low-memory constant batch inverse"));iv;
};
p41h2c_eisenstein_matrices(P,Q,A,u,z,order,ev,q)={
 my(Ps=vector(40),Qs=vector(40),ds=List(),iv,slopes=vector(78),pe=vector(40),qe=vector(40),
 d,num,den,kidx=0,E=vector(order,n,matrix(80,1681)),ep,eq,b,value,idx,neg,reps=List());
 Ps[1]=P;Qs[1]=Q;
 for(k=1,39,Ps[k+1]=p41j_add(Ps[k],P,A,u,z,order);Qs[k+1]=p41j_add(Qs[k],Q,A,u,z,order));
 for(side=1,2,my(base=if(side==1,P,Q),multiples=if(side==1,Ps,Qs));
  for(k=1,39,d=if(k==1,2*base[2],multiples[k][1]-base[1]);listput(ds,polcoef(lift(d),0,ev))));
 iv=p41h2c_invbatch(Vec(ds),u,z);ds=0;
 for(side=1,2,my(base=if(side==1,P,Q),multiples=if(side==1,Ps,Qs));
  for(k=1,39,kidx++;
   if(k==1,num=3*base[1]^2+A;den=2*base[2],num=multiples[k][2]-base[2];den=multiples[k][1]-base[1]);
   b=iv[kidx]*A^0;for(j=1,2,b*=2-den*b);
   if(den*b!=1,error("T2 low-memory base series inverse"));slopes[kidx]=num*b));
 ep=sum(k=1,39,slopes[k])/41;eq=sum(k=40,78,slopes[k])/41;pe[1]=ep;qe[1]=eq;
 for(k=1,39,pe[k+1]=pe[k]+ep-slopes[k];qe[k+1]=qe[k]+eq-slopes[39+k]);
 slopes=0;iv=0;
 for(k=1,40,for(side=1,2,idx=if(side==1,p41m_idx(k,0),p41m_idx(0,k));value=if(side==1,pe[k],qe[k]);
  for(n=1,order,for(h=1,80,E[n][h,idx]=lift(polcoef(lift(polcoef(lift(value),n-1,ev)),h-1))))));
 for(i=1,40,
  iv=p41h2c_invbatch(vector(40,j,polcoef(lift(Qs[j][1]-Ps[i][1]),0,ev)),u,z);
  for(j=1,40,num=Qs[j][2]-Ps[i][2];den=Qs[j][1]-Ps[i][1];
   b=iv[j]*A^0;for(h=1,2,b*=2-den*b);
   if(den*b!=1,error("T2 low-memory cross inverse"));
   value=pe[i]+qe[j]-num*b;idx=p41m_idx(i,j);
   for(n=1,order,for(h=1,80,E[n][h,idx]=lift(polcoef(lift(polcoef(lift(value),n-1,ev)),h-1))))));
 for(k=0,1680,neg=lift(Mod(-(k%41),41))+41*lift(Mod(-(k\41),41));
  for(n=1,order,for(h=1,80,if((E[n][h,k+1]+E[n][h,neg+1])%q,error("T2 encoded full oddness"))));
  if(k<neg,listput(reps,k+1)));
 reps=Vec(reps);if(#reps!=840,error("T2 encoded odd representatives"));
 vector(order,n,matrix(80,840,h,j,E[n][h,reps[j]]));
};
