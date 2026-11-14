\\ Actual coarse CM jets on the evaluation model, with no division by a stack parameter.
p41j_inv(v,u,z,order)={
  my(v0=polcoef(lift(v),0),b=p41l_inv(v0,u,z),current=1);
  while(current<order,b=b*(2-v*b);current*=2);
  if(v*b!=1,error("formal-series inverse"));b;
};
p41j_add(P,Q,A,u,z,order)={
  my(s,xx,yy);
  if(P==[0],return(Q));if(Q==[0],return(P));
  if(P[1]==Q[1],
    if(P[2]+Q[2]==0,return([0]));
    if(P!=Q,error("formal equal x"));
    s=(3*P[1]^2+A)*p41j_inv(2*P[2],u,z,order),
    s=(Q[2]-P[2])*p41j_inv(Q[1]-P[1],u,z,order)
  );
  xx=s^2-P[1]-Q[1];yy=s*(P[1]-xx)-P[2];[xx,yy];
};
p41j_mul(P,n,A,u,z,order)={
  my(Q=[0]);if(P==[0],return(P));if(n<0,P=[P[1],-P[2]];n=-n);
  while(n,if(n%2,Q=p41j_add(Q,P,A,u,z,order));n\=2;if(n,P=p41j_add(P,P,A,u,z,order)));
  Q;
};
p41j_psi41(x,A)={
  my(out=vector(42),q=4*(x^3+A*x+1),m);
  out[1]=0;out[2]=x^0;out[3]=x^0;
  out[4]=3*x^4+6*A*x^2+12*x-A^2;
  out[5]=2*(x^6+5*A*x^4+20*x^3-5*A^2*x^2-4*A*x-8-A^3);
  for(n=5,41,
    m=n\2;
    if(n%2,
      if(m%2==0,out[n+1]=q^2*out[m+3]*out[m+1]^3-out[m]*out[m+2]^3,
        out[n+1]=out[m+3]*out[m+1]^3-q^2*out[m]*out[m+2]^3),
      out[n+1]=out[m+1]*(out[m+3]*out[m]^2-out[m-1]*out[m+2]^2)
    );
  );out[42];
};
p41j_lift_point(P,eps,epsvar,order,u,z)={
  my(one=eps^0,x=one*P[1],y=one*P[2],derivative,inverse,value,coeff,rhs,yy=vector(order),inversey);
  derivative=polcoef(lift(p41j_psi41(x+eps,0*eps)),1,epsvar);
  inverse=p41l_inv(derivative,u,z);
  for(k=1,order-1,
    value=p41j_psi41(x,eps);coeff=polcoef(lift(value),k,epsvar);x-=coeff*inverse*eps^k;
  );
  if(p41j_psi41(x,eps)!=0,error("formal division-polynomial Hensel lift"));
  rhs=x^3+eps*x+1;yy[1]=P[2];inversey=p41l_inv(2*P[2],u,z);
  for(k=1,order-1,
    yy[k+1]=(polcoef(lift(rhs),k,epsvar)-sum(j=1,k-1,yy[j+1]*yy[k-j+1]))*inversey;
  );
  y=sum(k=0,order-1,yy[k+1]*eps^k);
  if(y^2!=rhs,error("formal curve equation"));
  if(p41j_mul([x,y],41,eps,u,z,order)!=[0],error("formal actual41-torsion"));[x,y];
};
p41j_eisenstein(P,Q,A,u,z,order)={
  my(Ps=vector(40),Qs=vector(40),num=List(),den=List(),prefix,back,pe=vector(40),qe=vector(40),
     ep,eq,ev=vector(1681,i,A^0*0),idx);
  Ps[1]=P;Qs[1]=Q;
  for(k=1,39,Ps[k+1]=p41j_add(Ps[k],P,A,u,z,order);Qs[k+1]=p41j_add(Qs[k],Q,A,u,z,order));
  for(side=1,2,
    my(base=if(side==1,P,Q),multiples=if(side==1,Ps,Qs));
    for(k=1,39,
      if(k==1,listput(num,3*base[1]^2+A);listput(den,2*base[2]),
        listput(num,multiples[k][2]-base[2]);listput(den,multiples[k][1]-base[1]));
    );
  );
  for(i=1,40,for(j=1,40,listput(num,Qs[j][2]-Ps[i][2]);listput(den,Qs[j][1]-Ps[i][1])));
  num=Vec(num);den=Vec(den);prefix=vector(#den);back=A^0;
  for(k=1,#den,prefix[k]=back;back*=den[k]);back=p41j_inv(back,u,z,order);
  forstep(k=#den,1,-1,num[k]*=back*prefix[k];back*=den[k]);
  if(back!=1,error("formal batch inverse"));
  ep=sum(k=1,39,num[k])/41;eq=sum(k=40,78,num[k])/41;pe[1]=ep;qe[1]=eq;
  for(k=1,39,pe[k+1]=pe[k]+ep-num[k];qe[k+1]=qe[k]+eq-num[39+k]);
  if(pe[40]!=-ep||qe[40]!=-eq,error("formal weight-one oddness"));
  for(k=1,40,ev[p41m_idx(k,0)]=pe[k];ev[p41m_idx(0,k)]=qe[k]);
  for(i=1,40,for(j=1,40,ev[p41m_idx(i,j)]=pe[i]+qe[j]-num[78+40*(i-1)+j]));
  for(i=0,40,for(j=0,40,if(ev[p41m_idx(-i,-j)]!=-ev[p41m_idx(i,j)],error("formal full oddness"))));ev;
};
p41j_frob(v,phi,eps,epsvar,order)=sum(k=0,order-1,subst(lift(polcoef(lift(v),k,epsvar)),'t,phi)*eps^k);
p41_cm3_makdisi47(input,path,precision=4,coarse_order=3)={
  my(modulus=47^precision,order=3*coarse_order,f=sum(k=1,81,input[1][k]*'t^(k-1)),u,z,phi,
     epsvar=varhigher("eps",'t),eps,P0,Qold,Q0,wold,ew,cmu,ii,u2,adjustment=0,D,U,Unew,R,aa,ee,cmindex,g,H,gh,
     P,Q,C,Frob,pairs=input[10],ev,raw,score,v,w,h,cj,coarse,normalized,pivot=0,tangent=0,
     inverse0,denominator,normalizer,unitnorm,Fnew,coef,ct1,ct2,expectedP,expectedQ);
  if(precision<1||precision>4||coarse_order<1,error("precision"));
  z=ffgen(Mod(1,47)*f);u=Mod(Mod(1,modulus)*'t,f);eps=Mod(u^0*epsvar,epsvar^order);
  phi=sum(k=1,80,input[2][k]*u^(k-1));
  P0=vector(2,j,sum(k=1,80,input[3][j][k]*u^(k-1)));
  Qold=vector(2,j,sum(k=1,80,input[4][j][k]*u^(k-1)));
  wold=sum(k=1,80,input[5][k]*u^(k-1));cmu=sum(k=1,80,input[6][k]*u^(k-1));
  U=Mod(matrix(2,2,i,j,input[7][i][j]),41);ew=sum(k=1,80,input[8][k]*u^(k-1));
  ii=sum(k=1,80,input[9][k]*u^(k-1));u2=Mod(Mod(1,modulus)*'s,'s^2+1);
  for(k=1,40,if(wold^k==ew,adjustment=k;break));if(!adjustment,error("actual Weil pairing match"));
  Q0=p41l_mul(Qold,adjustment,0,u,z);D=Mod([1,0;0,adjustment],41);Unew=D^-1*U*D;
  R=2*Unew+matid(2);R/=R[2,1];aa=lift(R[1,1]);ee=lift(R[1,1]^2+R[1,2]);
  cmindex=0;for(n=1,820,if(input[14][n]==[aa,ee],cmindex=n;break));if(!cmindex,error("actual CM necklace"));
  g=Mod(matrix(2,2,i,j,input[13][cmindex][i][j]),41);H=p41m_geometry()[3];
  gh=vector(42,k,lift(g*Mod(H[k],41)));
  P=p41j_lift_point(P0,eps,epsvar,order,u,z);Q=p41j_lift_point(Q0,eps,epsvar,order,u,z);
  expectedP=p41j_mul(vector(2,j,p41j_frob(P[j],phi,eps,epsvar,order)),adjustment,eps,u,z,order);
  if(expectedP!=Q,error("formal Frobenius first column"));
  expectedQ=p41j_mul(P,35*adjustment,eps,u,z,order);
  if(vector(2,j,p41j_frob(Q[j],phi,eps,epsvar,order))!=expectedQ,error("formal Frobenius second column"));
  ct1=vector(2,j,subst(lift(P[j]),epsvar,cmu^2*eps));ct2=vector(2,j,subst(lift(Q[j]),epsvar,cmu^2*eps));
  for(j=1,2,
    expectedP=p41j_add(p41j_mul(ct1,lift(Unew[1,j]),cmu^2*eps,u,z,order),
                      p41j_mul(ct2,lift(Unew[2,j]),cmu^2*eps,u,z,order),cmu^2*eps,u,z,order);
    expectedQ=if(j==1,[cmu*P[1],P[2]],[cmu*Q[1],Q[2]]);
    if(expectedP!=expectedQ,error("actual CM unit on the deformation"));
  );
  print("Actual CM torsion deformation, Weil adjustment=",adjustment,", necklace=",[aa,ee]," ",getwalltime());
  ev=p41j_eisenstein(P,Q,eps,u,z,order);
  print("All1680 actual formal weight-one values through A^",order-1," ",getwalltime());
  raw=matrix(order,73);
  for(k=1,73,
    score=0*eps;v=pairs[k][1];w=pairs[k][2];
    for(l=1,42,
      h=gh[l];score+=ev[p41m_idx(h[1,1]*v[1]+h[1,2]*v[2],h[2,1]*v[1]+h[2,2]*v[2])]*
                         ev[p41m_idx(h[1,1]*w[1]+h[1,2]*w[2],h[2,1]*w[1]+h[2,2]*w[2])];
    );
    for(j=0,order-1,cj=polcoef(lift(score),j,epsvar);raw[j+1,k]=(trace(ew*cj)-trace(ii*ew*cj)*u2)/4);
  );
  C=matrix(73,73,i,j,input[11][i][j][1]+input[11][i][j][2]*u2);
  Frob=matrix(73,73,i,j,input[12][i][j][1]+input[12][i][j][2]*u2);
  raw=raw*C;
  for(j=0,order-1,if(j%3!=2,for(k=1,73,if(raw[j+1,k]!=0,error("CM weight-two stack congruence")))));
  coarse=matrix(coarse_order,73,j,k,raw[3*j,k]);
  if(coarse*Frob!=matrix(coarse_order,73,j,k,subst(lift(coarse[j,k]),'s,-u2)),error("CM coarse rational descent"));
  for(k=1,73,coef=p41m_pair(coarse[1,k]);if((coef[1]^2+coef[2]^2)%47,pivot=k;break));
  if(!pivot,error("no unit CM point coordinate"));
  denominator=sum(j=0,coarse_order-1,coarse[j+1,pivot]*'x^j)+O('x^coarse_order);
  coef=p41m_pair(coarse[1,pivot]);inverse0=(coef[1]-coef[2]*u2)/Mod(coef[1]^2+coef[2]^2,modulus);
  normalizer=inverse0;my(current=1);while(current<coarse_order,normalizer*=2-denominator*normalizer;current*=2);
  normalized=matrix(coarse_order,73,j,k,polcoef((sum(l=0,coarse_order-1,coarse[l+1,k]*'x^l)+O('x^coarse_order))*normalizer,j-1));
  if(coarse_order>=2,
    for(k=1,73,coef=p41m_pair(normalized[2,k]);if((coef[1]^2+coef[2]^2)%47,tangent=k;break));
    if(!tangent,error("no nonzero coarse tangent"));
  );
  Fnew=D^-1*Mod([0,35;1,0],41)*D;
  write(path,[precision,coarse_order,adjustment,[aa,ee],cmindex,
    vector(2,i,vector(2,j,lift(Unew[i,j]))),vector(2,i,vector(2,j,lift(Fnew[i,j]))),
    vector(2,i,vector(order,j,p41l_vec(polcoef(lift(P[i]),j-1,epsvar)))),
    vector(2,i,vector(order,j,p41l_vec(polcoef(lift(Q[i]),j-1,epsvar)))),
    p41m_encode(raw),p41m_encode(coarse),pivot,tangent,p41m_encode(normalized)]);
  print("Actual coarse CM point and tangent through t^",coarse_order-1," saved; pivot=",pivot,", tangent=",tangent," ",getwalltime());
};
