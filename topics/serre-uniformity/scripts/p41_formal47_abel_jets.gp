\\ Actual order-three jets at54 Galois-stable nonspecial Abel points.
p41a_lift(P,eps,ev,u,z,order)={
  my(x=P[1]*eps^0,y,dd,iv,rhs,yy=vector(order),iy,value);
  dd=polcoef(lift(p41c4_psi41(x+eps,1,32)),1,ev);iv=p41l_inv(dd,u,z);
  for(k=1,order-1,value=p41c4_psi41(x,1,32+eps);x-=polcoef(lift(value),k,ev)*iv*eps^k);
  rhs=x^3+x+32+eps;yy[1]=P[2];iy=p41l_inv(2*P[2],u,z);
  for(k=1,order-1,yy[k+1]=(polcoef(lift(rhs),k,ev)-sum(j=1,k-1,yy[j+1]*yy[k-j+1]))*iy);
  y=sum(k=0,order-1,yy[k+1]*eps^k);
  if(y^2!=rhs||p41c4_psi41(x,1,32+eps)!=0,error("actual Abel jets Hensel equations"));
  if(p41j_mul([x,y],41,eps^0,u,z,order)!=[0],error("actual Abel jets41-torsion"));[x,y];
};
p41a_eisenstein(P,Q,A,u,z,order,ev)={
  my(Ps=vector(40),Qs=vector(40),ds=List(),prefix,iv,back,slopes=vector(78),pe=vector(40),qe=vector(40),
     d,num,den,kidx=0,out=vector(1681,i,0*A),ep,eq,b);
  Ps[1]=P;Qs[1]=Q;
  for(k=1,39,Ps[k+1]=p41j_add(Ps[k],P,A,u,z,order);Qs[k+1]=p41j_add(Qs[k],Q,A,u,z,order));
  for(side=1,2,my(base=if(side==1,P,Q),multiples=if(side==1,Ps,Qs));
    for(k=1,39,d=if(k==1,2*base[2],multiples[k][1]-base[1]);listput(ds,polcoef(lift(d),0,ev))));
  for(i=1,40,for(j=1,40,listput(ds,polcoef(lift(Qs[j][1]-Ps[i][1]),0,ev))));
  ds=Vec(ds);prefix=vector(#ds);iv=vector(#ds);back=u^0;
  for(k=1,#ds,prefix[k]=back;back*=ds[k]);back=p41l_inv(back,u,z);
  forstep(k=#ds,1,-1,iv[k]=back*prefix[k];back*=ds[k]);if(back!=1,error("Abel constant batch inverse"));
  for(side=1,2,my(base=if(side==1,P,Q),multiples=if(side==1,Ps,Qs));
    for(k=1,39,kidx++;
      if(k==1,num=3*base[1]^2+A;den=2*base[2],num=multiples[k][2]-base[2];den=multiples[k][1]-base[1]);
      b=iv[kidx]*A^0;for(j=1,2,b*=2-den*b);if(den*b!=1,error("Abel series inverse"));slopes[kidx]=num*b));
  ep=sum(k=1,39,slopes[k])/41;eq=sum(k=40,78,slopes[k])/41;pe[1]=ep;qe[1]=eq;
  for(k=1,39,pe[k+1]=pe[k]+ep-slopes[k];qe[k+1]=qe[k]+eq-slopes[39+k]);
  for(k=1,40,out[p41m_idx(k,0)]=pe[k];out[p41m_idx(0,k)]=qe[k]);
  for(i=1,40,for(j=1,40,kidx++;num=Qs[j][2]-Ps[i][2];den=Qs[j][1]-Ps[i][1];
    b=iv[kidx]*A^0;for(h=1,2,b*=2-den*b);if(den*b!=1,error("Abel cross inverse"));
    out[p41m_idx(i,j)]=pe[i]+qe[j]-num*b));
  for(i=0,40,for(j=0,40,if(out[p41m_idx(-i,-j)]!=-out[p41m_idx(i,j)],error("Abel full oddness"))));out;
};
p41a_trace_block(Es,H,degree,gh,pairs,signed,first,last)={
  my(G=(vecextract(Es[1],"..",[first..last])~*H)*Es[degree+1],M=matrix(#gh,73),v,w,g,j1,j2,sgn,score);
  for(j=1,degree,G+=(vecextract(Es[j+1],"..",[first..last])~*H)*Es[degree-j+1]);
  for(n=1,#gh,for(k=1,73,v=pairs[k][1];w=pairs[k][2];score=0;
    for(l=1,42,g=gh[n][l];
      j1=signed[p41m_idx(g[1,1]*v[1]+g[1,2]*v[2],g[2,1]*v[1]+g[2,2]*v[2])];
      if(abs(j1)>=first&&abs(j1)<=last,
        j2=signed[p41m_idx(g[1,1]*w[1]+g[1,2]*w[2],g[2,1]*w[1]+g[2,2]*w[2])];
        sgn=sign(j1*j2);score+=sgn*G[abs(j1)-first+1,abs(j2)]));
    M[n,k]=score));M;
};
p41a_trace_coefficient(Es,H,degree,gh,pairs,signed)={
  my(M=matrix(#gh,73));for(block=0,3,M+=p41a_trace_block(Es,H,degree,gh,pairs,signed,1+210*block,210*(block+1)));M;
};
p41_formal47_abel_jets(input,path)={
  my(q=47^4,order=4,f=sum(k=1,81,input[1][k]*'t^(k-1)),z=ffgen(Mod(1,47)*f),u=Mod(Mod(1,q)*'t,f),
    phi=sum(k=1,80,input[2][k]*u^(k-1)),P0=vector(2,j,sum(k=1,80,input[3][j][k]*u^(k-1))),
    Q0=vector(2,j,sum(k=1,80,input[4][j][k]*u^(k-1))),ew=sum(k=1,80,input[5][k]*u^(k-1)),
    ii=sum(k=1,80,input[6][k]*u^(k-1)),u2=Mod(Mod(1,q)*'s,'s^2+1),
    epsvar=varhigher("eps",'t),eps=Mod(u^0*epsvar,epsvar^order),P,Q,ev,reps=List(),signed=vector(1681),neg,
    Es,aa=vector(159),bb=vector(159),power=u^0,HA,HB,GR,GI,T,gh,pairs=input[7],points=input[14],
    M,score,v,w,g,j1,j2,sgn,C,A,W,coeffs=vector(order),tau=input[15],basejets=input[16]);
  P=p41a_lift(P0,eps,epsvar,u,z,order);Q=p41a_lift(Q0,eps,epsvar,u,z,order);
  if(vector(2,j,p41j_frob(P[j],phi,eps,epsvar,order))!=Q,error("Abel jets FrobP"));
  if(vector(2,j,p41j_frob(Q[j],phi,eps,epsvar,order))!=p41j_mul(P,35,eps^0,u,z,order),error("Abel jets FrobQ"));
  print("Actual108 Abel fibre torsion through t^3 ",getwalltime());
  ev=p41a_eisenstein(P,Q,eps^0,u,z,order,epsvar);
  for(j=1,1680,neg=lift(Mod(-(j%41),41))+41*lift(Mod(-(j\41),41));
    if(j<neg,listput(reps,j+1);signed[j+1]=#reps;signed[neg+1]=-#reps));
  reps=Vec(reps);if(#reps!=840,error("Abel signed torsion"));
  Es=vector(order,k,Mod(matrix(80,840,i,j,lift(polcoef(lift(polcoef(lift(ev[reps[j]]),k-1,epsvar)),i-1))),q));
  ev=0;
  for(k=1,159,aa[k]=trace(ew*power)/4;bb[k]=-trace(ii*ew*power)/4;power*=u);
  HA=matrix(80,80,i,j,aa[i+j-1]);HB=matrix(80,80,i,j,bb[i+j-1]);
  gh=vector(#points,n,vector(42,k,lift(Mod(matrix(2,2,i,j,input[9][points[n]][i][j]),41)*Mod(matrix(2,2,i,j,input[10][k][i][j]),41))));
  C=matrix(73,73,i,j,input[8][i][j][1]+input[8][i][j][2]*u2);
  A=matrix(73,73,i,j,input[11][i][j][1]+input[11][i][j][2]*u2);
  for(degree=0,order-1,
    GR=p41a_trace_coefficient(Es,HA,degree,gh,pairs,signed);
    GI=p41a_trace_coefficient(Es,HB,degree,gh,pairs,signed);
    M=(GR+u2*GI)*C;
    if(degree==0&&M!=matrix(#points,73,n,k,input[13][points[n]][k][1]+input[13][points[n]][k][2]*u2),error("Abel actual constant"));
    if(degree==1&&M!=matrix(#points,73,n,k,basejets[points[n]][k][1]+basejets[points[n]][k][2]*u2),error("Abel actual first jet"));
    if(M*A!=matrix(#points,73,n,k,subst(lift(M[tau[n],k]),'s,-u2)),error("Abel actual coefficient Frobenius"));
    coeffs[degree+1]=p41m_encode(M);GR=0;GI=0;
    print("Actual108x73 Abel coefficient ",degree," PASS ",getwalltime());
  );
  write(path,[vector(2,i,vector(order,j,p41l_vec(polcoef(lift(P[i]),j-1,epsvar)))),
    vector(2,i,vector(order,j,p41l_vec(polcoef(lift(Q[i]),j-1,epsvar)))),coeffs]);
};
