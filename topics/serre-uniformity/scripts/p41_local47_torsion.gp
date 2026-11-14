\\ Actual 41-torsion over the unramified degree-80 ring modulo 47^4.
\\ All inversions in the local ring are lifted from the residue field.
p41l_inv(v,u,z)={
  my(w=z^0*subst(lift(lift(v)),'t,z),b);
  if(w==0,error("not a unit in the unramified local ring"));
  w=1/w;b=subst(w.pol,'t,u);
  for(j=1,3,b*=2-v*b);
  if(v*b!=1,error("Newton inverse"));b;
};
p41l_add(P,Q,A,u,z)={
  my(s,xx,yy);
  if(P==[0],return(Q));if(Q==[0],return(P));
  if(P[1]==Q[1],
    if(P[2]+Q[2]==0,return([0]));
    if(P!=Q,error("same x but neither equal nor opposite"));
    s=(3*P[1]^2+A)*p41l_inv(2*P[2],u,z),
    s=(Q[2]-P[2])*p41l_inv(Q[1]-P[1],u,z)
  );
  xx=s^2-P[1]-Q[1];yy=s*(P[1]-xx)-P[2];[xx,yy];
};
p41l_mul(P,n,A,u,z)={
  my(Q=[0]);if(P==[0],return(P));if(n<0,P=[P[1],-P[2]];n=-n);
  while(n,if(n%2,Q=p41l_add(Q,P,A,u,z));n\=2;if(n,P=p41l_add(P,P,A,u,z)));
  Q;
};
p41l_vec(a)={vector(80,j,lift(polcoef(lift(a),j-1)));};
p41l_pairlog(ew,v)={for(j=0,40,if(ew^j==v,return(j)));error("pairing logarithm");};
p41l_pointcoords(E,P,Q,ew,V)=[p41l_pairlog(ew,ellweilpairing(E,V,Q,41)),p41l_pairlog(ew,ellweilpairing(E,P,V,41))];
p41l_curve(A,B,f,u,z,phi,cm)={
  my(E=ellinit([A,B]),Ez=ellinit([A,B],z),m=(47^40-1)/41,P,Q,ew,xx,yy,
     psi,psip,P4,Q4,qx,qy,ew4,cmu0,cmu,U,F,R,aa,ee,check,cmvec=[],Urows=[],ne=[]);
  if(ellap(E,47)!=0,error("chosen curve is not trace zero"));
  P=ellmul(Ez,random(Ez),m);while(P==[0],P=ellmul(Ez,random(Ez),m));
  Q=[P[1]^47,P[2]^47];
  if(ellmul(Ez,P,41)!=[0]||ellmul(Ez,Q,41)!=[0],error("finite 41-torsion"));
  if([Q[1]^47,Q[2]^47]!=ellmul(Ez,P,-47),error("finite Frobenius companion"));
  ew=ellweilpairing(Ez,P,Q,41);if(ew==1||ew^41!=1,error("finite primitive Weil pairing"));
  xx=subst(P[1].pol,'t,u);yy=subst(P[2].pol,'t,u);
  psi=elldivpol(E,41,'x);psip=deriv(psi);
  for(j=1,3,xx-=subst(psi,'x,xx)*p41l_inv(subst(psip,'x,xx),u,z));
  for(j=1,3,yy-=(yy^2-xx^3-A*xx-B)*p41l_inv(2*yy,u,z));
  if(subst(psi,'x,xx)!=0||yy^2!=xx^3+A*xx+B,error("torsion Hensel equations"));
  qx=subst(lift(xx),'t,phi);qy=subst(lift(yy),'t,phi);P4=[xx,yy];Q4=[qx,qy];
  if(p41l_mul(P4,41,A,u,z)!=[0]||p41l_mul(Q4,41,A,u,z)!=[0],error("actual lifted 41-torsion"));
  if([subst(lift(qx),'t,phi),subst(lift(qy),'t,phi)]!=p41l_mul(P4,-47,A,u,z),error("lifted companion matrix"));
  ew4=subst(ew.pol,'t,u);for(j=1,3,ew4-=(ew4^41-1)*p41l_inv(41*ew4^40,u,z));
  if(ew4==1||ew4^41!=1,error("lifted Weil pairing"));
  if(cm,
    cmu0=(-1+sqrt(-3*P[1]^0))/2;
    U=Mod(Mat([p41l_pointcoords(Ez,P,Q,ew,[cmu0*P[1],P[2]])~,p41l_pointcoords(Ez,P,Q,ew,[cmu0*Q[1],Q[2]])~]),41);
    if(U^2+U+matid(2)!=matrix(2,2),error("CM finite action"));
    F=Mod([0,-47;1,0],41);if(F*U!=U^2*F,error("CM Frobenius conjugation"));
    R=2*U+matid(2);R/=R[2,1];aa=R[1,1];ee=aa^2+R[1,2];ne=[lift(aa),lift(ee)];
    cmu=subst(cmu0.pol,'t,u);for(j=1,3,cmu-=(cmu^2+cmu+1)*p41l_inv(2*cmu+1,u,z));
    check=p41l_add(p41l_mul(P4,lift(U[1,1]),A,u,z),p41l_mul(Q4,lift(U[2,1]),A,u,z),A,u,z);
    if([cmu*xx,yy]!=check,error("lifted CM column1"));
    check=p41l_add(p41l_mul(P4,lift(U[1,2]),A,u,z),p41l_mul(Q4,lift(U[2,2]),A,u,z),A,u,z);
    if([cmu*qx,qy]!=check,error("lifted CM column2"));
    cmvec=p41l_vec(cmu);Urows=vector(2,i,vector(2,j,lift(U[i,j])));
  );
  [A,B,0,lift(Mod(1728*4*A^3,47)/Mod(4*A^3+27*B^2,47)),
   vector(2,i,p41l_vec(P4[i])),vector(2,i,p41l_vec(Q4[i])),p41l_vec(ew4),cmvec,Urows,ne];
};
p41_local47(path)={
  my(f,z,u,phi,records);
  setrand(41047);f=lift(ffinit(47,80,'t));z=ffgen(Mod(1,47)*f);u=Mod(Mod(1,47^4)*'t,f);
  phi=u^47;for(j=1,3,phi-=subst(f,'t,phi)*p41l_inv(subst(deriv(f),'t,phi),u,z));
  if(subst(f,'t,phi)!=0,error("unramified Frobenius"));
  records=[p41l_curve(0,1,f,u,z,phi,1),p41l_curve(1,32,f,u,z,phi,0)];
  write(path,[vector(81,j,polcoef(f,j-1)),p41l_vec(phi),records]);
  print("Two actual 41-torsion bases over the unramified degree-80 ring mod47^4 verified, including Frobenius and the CM level structure.");
};
