\\ Actual T2 branch P_minus3 -> P_minus12, in the fixed level41 model.
p41c12_velu(P,r,v,A,u,z,order)={
  my(d=p41j_inv(P[1]-r,u,z,order));
  [P[1]+v*d,P[2]*(1-v*d^2)];
};
p41_cm12_hecke47(input,path)={
  my(q=47^4,order=4,f=sum(k=1,81,input[1][k]*'t^(k-1)),z=ffgen(Mod(1,47)*f),u=Mod(Mod(1,q)*'t,f),
    phi=sum(k=1,80,input[2][k]*u^(k-1)),ew=sum(k=1,80,input[3][k]*u^(k-1)),
    ii=sum(k=1,80,input[4][k]*u^(k-1)),u2=Mod(Mod(1,q)*'s,'s^2+1),
    ev=varhigher("c12ep",'t),eps=Mod(Mod(1,q)*u^0*ev,ev^order),P,Q,r=Mod(-1,q)*eps^0,v,AA,BB,vals,gh,
    pairs=input[7],C,Frob,raw=matrix(order,73),score,v1,v2,h,coef,Jsrc,Jtgt,targetF);
  P=vector(2,j,sum(k=0,order-1,sum(l=1,80,input[5][j][k+1][l]*u^(l-1))*eps^k));
  Q=vector(2,j,sum(k=0,order-1,sum(l=1,80,input[6][j][k+1][l]*u^(l-1))*eps^k));
  for(k=1,3,r-=(r^3+eps*r+1)*p41j_inv(3*r^2+eps,u,z,order));
  if(r^3+eps*r+1!=0,error("CM12 actual2-kernel lift"));
  v=3*r^2+eps;AA=-4*eps-15*r^2;BB=22+14*eps*r;
  P=p41c12_velu(P,r,v,eps,u,z,order);Q=p41c12_velu(Q,r,v,eps,u,z,order);
  Q=p41j_mul(Q,21,AA,u,z,order);
  if(P[2]^2!=P[1]^3+AA*P[1]+BB||Q[2]^2!=Q[1]^3+AA*Q[1]+BB,error("CM12 actual target curve"));
  if(p41j_mul(P,41,AA,u,z,order)!=[0]||p41j_mul(Q,41,AA,u,z,order)!=[0],error("CM12 actual41-torsion"));
  targetF=Mod([1,0;0,21],41)^-1*Mod(matrix(2,2,i,j,input[11][i][j]),41)*Mod([1,0;0,21],41);
  for(j=1,2,my(lhs=vector(2,k,p41j_frob(if(j==1,P[k],Q[k]),phi,eps,ev,order)),
    rhs=p41j_add(p41j_mul(P,lift(targetF[1,j]),AA,u,z,order),p41j_mul(Q,lift(targetF[2,j]),AA,u,z,order),AA,u,z,order));
    if(lhs!=rhs,error("CM12 target Frobenius torsion")));
  print("Actual rational2-isogeny branch, target curve and full torsion jets PASS ",getwalltime());
  vals=p41a_eisenstein(P,Q,AA,u,z,order,ev);
  gh=vector(42,k,lift(Mod(matrix(2,2,i,j,input[10][i][j]),41)*Mod(p41m_geometry()[3][k],41)));
  for(k=1,73,score=eps*0;v1=pairs[k][1];v2=pairs[k][2];
    for(l=1,42,h=gh[l];score+=vals[p41m_idx(h[1,1]*v1[1]+h[1,2]*v1[2],h[2,1]*v1[1]+h[2,2]*v1[2])]*
      vals[p41m_idx(h[1,1]*v2[1]+h[1,2]*v2[2],h[2,1]*v2[1]+h[2,2]*v2[2])]);
    for(j=0,order-1,coef=polcoef(lift(score),j,ev);raw[j+1,k]=(trace(ew*coef)-trace(ii*ew*coef)*u2)/4));
  C=matrix(73,73,i,j,input[8][i][j][1]+input[8][i][j][2]*u2);raw=raw*C;
  Frob=matrix(73,73,i,j,input[9][i][j][1]+input[9][i][j][2]*u2);
  if(raw*Frob!=matrix(order,73,i,j,subst(lift(raw[i,j]),'s,-u2)),error("CM12 actual model Frobenius descent"));
  Jsrc=6912*eps^3*p41j_inv(4*eps^3+27,u,z,order);
  Jtgt=6912*AA^3*p41j_inv(4*AA^3+27*BB^2,u,z,order);
  if(polcoef(lift(Jtgt),0,ev)!=Mod(54000,q)||polcoef(lift(Jtgt),1,ev)!=Mod(-118800,q),error("CM12 actual coarse tangent"));
  write(path,[p41m_encode(raw),vector(2,j,vector(order,k,p41l_vec(polcoef(lift(P[j]),k-1,ev)))),
    vector(2,j,vector(order,k,p41l_vec(polcoef(lift(Q[j]),k-1,ev)))),
    vector(order,k,lift(lift(polcoef(lift(r),k-1,ev)))),
    vector(order,k,lift(lift(polcoef(lift(AA),k-1,ev)))),vector(order,k,lift(lift(polcoef(lift(BB),k-1,ev)))),
    vector(order,k,lift(lift(polcoef(lift(Jsrc),k-1,ev)))),vector(order,k,lift(lift(polcoef(lift(Jtgt),k-1,ev)))),
    vector(2,i,vector(2,j,lift(targetF[i,j])))]);
  print("Actual P_minus12 full73 coordinates and three derivatives PASS ",getwalltime());
};
