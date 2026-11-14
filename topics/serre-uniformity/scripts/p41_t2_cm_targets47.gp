\\ The three nonself T2 target points needed for F2 at the two CM points.
p41_t2_cm_targets47(input,path)={
  my(q=47^4,f=sum(k=1,81,input[1][k]*'t^(k-1)),z=ffgen(Mod(1,47)*f),u=Mod(Mod(1,q)*'t,f),
    phi=sum(k=1,80,input[2][k]*u^(k-1)),ew=sum(k=1,80,input[3][k]*u^(k-1)),
    ii=sum(k=1,80,input[4][k]*u^(k-1)),u2=Mod(Mod(1,q)*'s,'s^2+1),
    C=matrix(73,73,i,j,input[6][i][j][1]+input[6][i][j][2]*u2),
    Fmodel=matrix(73,73,i,j,input[7][i][j][1]+input[7][i][j][2]*u2),
    epsvar=varhigher("t2cmt",'t),eps=Mod(Mod(1,q)*u^0*epsvar,epsvar),records=List(),cases=input[10],
    c,A,B,rr,v,AA,BB,P,Q,PP,QQ,iv,Ft,expected,vals,gh,score,va,vb,h,coef,raw,W,jval);
  for(n=1,#cases,c=cases[n];A=c[2];B=c[3];rr=Mod(c[7],q)*u^0;v=3*rr^2+A;
    if(rr^3+A*rr+B!=0,error("Actual T2 CM target kernel"));
    AA=-4*A-15*rr^2;BB=22*B+14*A*rr;
    P=vector(2,j,sum(k=1,80,c[4][j][k]*u^(k-1)));Q=vector(2,j,sum(k=1,80,c[5][j][k]*u^(k-1)));
    iv=p41l_inv(P[1]-rr,u,z);PP=[P[1]+v*iv,P[2]*(1-v*iv^2)];
    iv=p41l_inv(Q[1]-rr,u,z);QQ=[Q[1]+v*iv,Q[2]*(1-v*iv^2)];QQ=p41l_mul(QQ,21,AA,u,z);
    if(PP[2]^2!=PP[1]^3+AA*PP[1]+BB||QQ[2]^2!=QQ[1]^3+AA*QQ[1]+BB,error("Actual T2 CM target equation"));
    if(p41l_mul(PP,41,AA,u,z)!=[0]||p41l_mul(QQ,41,AA,u,z)!=[0],error("Actual T2 CM target41-torsion"));
    Ft=Mod([1,0;0,21],41)^-1*Mod(matrix(2,2,i,j,c[6][i][j]),41)*Mod([1,0;0,21],41);
    for(j=1,2,expected=p41l_add(p41l_mul(PP,lift(Ft[1,j]),AA,u,z),p41l_mul(QQ,lift(Ft[2,j]),AA,u,z),AA,u,z);
      if(expected!=vector(2,k,subst(lift(if(j==1,PP[k],QQ[k])),'t,phi)),error("Actual T2 CM target Frobenius")));
    vals=p41a_eisenstein(vector(2,j,PP[j]*eps^0),vector(2,j,QQ[j]*eps^0),AA*eps^0,u,z,1,epsvar);
    gh=vector(42,k,lift(Mod(matrix(2,2,i,j,input[8][c[8]][i][j]),41)*Mod(matrix(2,2,i,j,input[9][k][i][j]),41)));
    raw=matrix(1,73);
    for(k=1,73,score=0*eps;va=input[5][k][1];vb=input[5][k][2];
      for(l=1,42,h=gh[l];score+=vals[p41m_idx(h[1,1]*va[1]+h[1,2]*va[2],h[2,1]*va[1]+h[2,2]*va[2])]*
        vals[p41m_idx(h[1,1]*vb[1]+h[1,2]*vb[2],h[2,1]*vb[1]+h[2,2]*vb[2])]);
      coef=polcoef(lift(score),0,epsvar);raw[1,k]=(trace(ew*coef)-trace(ii*ew*coef)*u2)/4);
    W=raw*C;
    if(W*Fmodel!=matrix(1,73,i,j,subst(lift(W[i,j]),'s,-u2)),error("Actual T2 CM target model descent"));
    jval=6912*AA^3*p41l_inv(4*AA^3+27*BB^2,u,z);
    listput(records,[c[1],lift(lift(AA)),lift(lift(BB)),lift(lift(jval)),c[8],
      vector(2,j,p41l_vec(PP[j])),vector(2,j,p41l_vec(QQ[j])),p41m_encode(W),vector(2,i,vector(2,j,lift(Ft[i,j])))]);
    print("Actual T2 CM target ",c[1]," complete73 values PASS ",getwalltime());
  );
  write(path,Vec(records));
};

