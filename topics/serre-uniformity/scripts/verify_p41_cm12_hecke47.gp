\\ Independent group-law Velu and full batch-inverse Eisenstein verification.
p41_verify_cm12_hecke47(input,cert,path)={
  my(q=47^4,order=4,f=sum(k=1,81,input[1][k]*'t^(k-1)),z=ffgen(Mod(1,47)*f),u=Mod(Mod(1,q)*'t,f),
    ew=sum(k=1,80,input[3][k]*u^(k-1)),ii=sum(k=1,80,input[4][k]*u^(k-1)),
    u2=Mod(Mod(1,q)*'s,'s^2+1),ev=varhigher("c12verify",'t),eps=Mod(Mod(1,q)*u^0*ev,ev^order),
    P,Q,PP,QQ,r,AA,BB,add,expected,vals,gh,raw=matrix(order,73),score,v,w,h,coef,C);
  P=vector(2,j,sum(k=0,order-1,sum(l=1,80,input[5][j][k+1][l]*u^(l-1))*eps^k));
  Q=vector(2,j,sum(k=0,order-1,sum(l=1,80,input[6][j][k+1][l]*u^(l-1))*eps^k));
  PP=vector(2,j,sum(k=0,order-1,sum(l=1,80,cert[2][j][k+1][l]*u^(l-1))*eps^k));
  QQ=vector(2,j,sum(k=0,order-1,sum(l=1,80,cert[3][j][k+1][l]*u^(l-1))*eps^k));
  r=sum(k=0,order-1,Mod(cert[4][k+1],q)*eps^k);
  AA=sum(k=0,order-1,Mod(cert[5][k+1],q)*eps^k);BB=sum(k=0,order-1,Mod(cert[6][k+1],q)*eps^k);
  if(r^3+eps*r+1!=0||polcoef(lift(r),0,ev)!=Mod(-1,q),error("independent CM12 kernel"));
  if(AA!=eps-5*(3*r^2+eps)||BB!=1-7*r*(3*r^2+eps),error("independent CM12 target coefficients"));
  add=p41j_add(P,[r,0],eps,u,z,order);expected=[P[1]+add[1]-r,P[2]+add[2]];
  if(PP!=expected,error("independent Velu P by group law"));
  add=p41j_add(Q,[r,0],eps,u,z,order);expected=[Q[1]+add[1]-r,Q[2]+add[2]];
  if(p41j_mul(QQ,2,AA,u,z,order)!=expected,error("independent Velu Q and Weil scale"));
  vals=p41j_eisenstein(PP,QQ,AA,u,z,order);
  gh=vector(42,k,lift(Mod(matrix(2,2,i,j,input[10][i][j]),41)*Mod(p41m_geometry()[3][k],41)));
  for(k=1,73,score=eps*0;v=input[7][k][1];w=input[7][k][2];
    for(l=1,42,h=gh[l];score+=vals[p41m_idx(h[1,1]*v[1]+h[1,2]*v[2],h[2,1]*v[1]+h[2,2]*v[2])]*
      vals[p41m_idx(h[1,1]*w[1]+h[1,2]*w[2],h[2,1]*w[1]+h[2,2]*w[2])]);
    for(j=0,order-1,coef=polcoef(lift(score),j,ev);raw[j+1,k]=(trace(ew*coef)-trace(ii*ew*coef)*u2)/4));
  C=matrix(73,73,i,j,input[8][i][j][1]+input[8][i][j][2]*u2);raw=raw*C;
  if(p41m_encode(raw)!=cert[1],error("independent all73 CM12 jets"));
  write(path,["PASS"]);print("Independent actual2-isogeny group-law and all73 Eisenstein jets PASS ",getwalltime());
};
