\\ Actual weight-two evaluation model for X_ns^+(41), modulo 47^e.
\\ Read p41_local47_torsion.gp first; its local-ring inverses are used below.
p41m_idx(i,j)=lift(Mod(i,41))+41*lift(Mod(j,41))+1;
p41m_pair(a)=[lift(polcoef(lift(a),0)),lift(polcoef(lift(a),1))];
p41m_encode(M)=vector(matsize(M)[1],i,vector(matsize(M)[2],j,p41m_pair(M[i,j])));
p41m_batch_inverse(a,u,z)={
  my(n=#a,prefix=vector(#a),out=vector(#a),b=u^0);
  for(i=1,n,prefix[i]=b;b*=a[i]);b=p41l_inv(b,u,z);
  forstep(i=n,1,-1,out[i]=b*prefix[i];b*=a[i]);
  if(b!=1,error("batch inverse"));out;
};
p41m_eisenstein(P,Q,u,z)={
  my(Ps=vector(40),Qs=vector(40),num=List(),den=List(),iv,pe=vector(40),qe=vector(40),
     ep,eq,ev=vector(1681,i,u^0*0),idx);
  Ps[1]=P;Qs[1]=Q;
  for(k=1,39,Ps[k+1]=p41l_add(Ps[k],P,1,u,z);Qs[k+1]=p41l_add(Qs[k],Q,1,u,z));
  for(side=1,2,
    my(base=if(side==1,P,Q),multiples=if(side==1,Ps,Qs));
    for(k=1,39,
      if(k==1,listput(num,3*base[1]^2+1);listput(den,2*base[2]),
        listput(num,multiples[k][2]-base[2]);listput(den,multiples[k][1]-base[1]));
    );
  );
  for(i=1,40,for(j=1,40,listput(num,Qs[j][2]-Ps[i][2]);listput(den,Qs[j][1]-Ps[i][1])));
  num=Vec(num);den=Vec(den);iv=p41m_batch_inverse(den,u,z);
  for(k=1,#num,num[k]*=iv[k]);
  ep=sum(k=1,39,num[k])/41;eq=sum(k=40,78,num[k])/41;pe[1]=ep;qe[1]=eq;
  for(k=1,39,pe[k+1]=pe[k]+ep-num[k];qe[k+1]=qe[k]+eq-num[39+k]);
  if(pe[40]!=-ep||qe[40]!=-eq,error("Eisenstein oddness on the two axes"));
  for(k=1,40,ev[p41m_idx(k,0)]=pe[k];ev[p41m_idx(0,k)]=qe[k]);
  for(i=1,40,for(j=1,40,ev[p41m_idx(i,j)]=pe[i]+qe[j]-num[78+40*(i-1)+j]));
  for(i=0,40,for(j=0,40,if(ev[p41m_idx(-i,-j)]!=-ev[p41m_idx(i,j)],error("Eisenstein oddness"))));
  ev;
};
p41m_geometry()={
  my(H=List(),idx,negidx,nm,nsq,ns,gg=vector(820),a,b,aa,ee,ss,c,w,v,g,
     R0=Mod([0,35;1,0],41),tau=vector(820),R,T,F=R0);
  for(a=0,40,for(b=0,40,
    idx=a+41*b;negidx=lift(Mod(-a,41))+41*lift(Mod(-b,41));if(idx>negidx,next);
    nm=lift(Mod(a^2-35*b^2,41));
    if(nm==1,listput(H,lift(Mod([a,35*b;b,a],41))));
    if(nm==40,listput(H,lift(Mod([a,-35*b;b,-a],41))));
  ));H=Vec(H);if(#H!=42,error("SL2 normalizer modulo signs"));
  nsq=select(e->kronecker(e,41)==-1,[1..40]);ns=concat(vector(41,a,vector(20,j,[a-1,nsq[j]])));
  for(n=1,820,
    aa=ns[n][1];ee=ns[n][2];ss=sqrt(Mod(ee/Mod(35,41),41));
    for(c=0,40,
      my(delta=ss+ee*c^2);
      if(delta==0||issquare(delta),w=sqrt(delta);v=w+aa*c;
        g=Mod([v,(aa*v+(ee-aa^2)*c)/ss;c,(v-aa*c)/ss],41);break);
    );
    R=Mod([aa,ee-aa^2;1,-aa],41);
    if(matdet(g)!=1||g*R0/g!=R/ss,error("actual SL2 coset representative"));gg[n]=lift(g);
    T=F*R/F;T/=T[2,1];aa=lift(T[1,1]);ee=lift(T[1,1]^2+T[1,2]);
    tau[n]=20*aa+setsearch(nsq,ee);
    if(!tau[n],error("Frobenius necklace"));
  );
  if(sum(n=1,820,tau[n]==n)!=22,error("Frobenius fixed fibre points"));
  for(n=1,820,if(tau[tau[n]]!=n,error("Frobenius involution")));
  [ns,gg,H,tau];
};
p41_makdisi47(input,path,precision=4)={
  my(modulus=47^precision,f=sum(k=1,81,input[1][k]*'t^(k-1)),z,u,phi,P,Q,ew,ii0,ii,ff2,u2,
     ev,reps=List(),signed=vector(1681),neg,E,aa,bb,power,HA,HB,B0,B1,geom,ns,gg,H,tau,gh,
     pairs=List(),v,ww,M,score,g,j1,j2,sgn,M0,inds,cols,rows,V,PV,C,C0,W,Y,Frob,
     det0,fields=input[6],record,tn,fac,Lfactor=1);
  if(precision<1||precision>4,error("available input precision is four"));
  z=ffgen(Mod(1,47)*f);u=Mod(Mod(1,modulus)*'t,f);
  P=vector(2,j,sum(k=1,80,input[2][j][k]*u^(k-1)));
  Q=vector(2,j,sum(k=1,80,input[3][j][k]*u^(k-1)));
  ew=sum(k=1,80,input[4][k]*u^(k-1));phi=sum(k=1,80,input[5][k]*u^(k-1));
  ii0=sqrt(-z^0);
  for(k=0,79,if(polcoef(ii0.pol,k)!=0,if(lift(polcoef(ii0.pol,k))>23,ii0=-ii0);break));
  ii=subst(ii0.pol,'t,u);for(k=1,3,ii-=(ii^2+1)*p41l_inv(2*ii,u,z));
  if(ii^2!=-1||subst(lift(ii),'t,phi)!=-ii,error("quadratic unramified generator"));
  ff2=ffgen(Mod('s^2+1,47));u2=Mod(Mod(1,modulus)*'s,'s^2+1);
  ev=p41m_eisenstein(P,Q,u,z);
  print("Actual1680 weight-one values modulo47^",precision," ",getwalltime());
  for(j=1,1680,
    neg=lift(Mod(-(j%41),41))+41*lift(Mod(-(j\41),41));
    if(j<neg,listput(reps,j+1);signed[j+1]=#reps;signed[neg+1]=-#reps);
  );reps=Vec(reps);if(#reps!=840,error("signed torsion representatives"));
  E=Mod(matrix(80,840,i,j,lift(polcoef(lift(ev[reps[j]]),i-1))),modulus);
  aa=vector(159);bb=vector(159);power=u^0;
  for(k=1,159,aa[k]=trace(ew*power)/4;bb[k]=-trace(ii*ew*power)/4;power*=u);
  HA=matrix(80,80,i,j,aa[i+j-1]);HB=matrix(80,80,i,j,bb[i+j-1]);
  B0=(E~*HA)*E;B1=(E~*HB)*E;
  print("Actual relative trace Gram matrices ",getwalltime());
  geom=p41m_geometry();ns=geom[1];gg=geom[2];H=geom[3];tau=geom[4];
  gh=vector(820,n,vector(42,k,lift(Mod(gg[n]*H[k],41))));
  setrand(41047);
  while(#pairs<100,
    v=[random(41),random(41)];ww=[random(41),random(41)];
    if(lift(Mod(v[1]*ww[2]-v[2]*ww[1],41))!=0,listput(pairs,[v,ww]));
  );pairs=Vec(pairs);M=matrix(820,100);
  for(n=1,820,
    for(k=1,100,
      v=pairs[k][1];ww=pairs[k][2];score=u2^0*0;
      for(l=1,42,
        g=gh[n][l];
        j1=signed[p41m_idx(g[1,1]*v[1]+g[1,2]*v[2],g[2,1]*v[1]+g[2,2]*v[2])];
        j2=signed[p41m_idx(g[1,1]*ww[1]+g[1,2]*ww[2],g[2,1]*ww[1]+g[2,2]*ww[2])];
        sgn=sign(j1*j2);j1=abs(j1);j2=abs(j2);score+=sgn*(B0[j1,j2]+B1[j1,j2]*u2);
      );M[n,k]=score;
    );
  );
  M0=matrix(820,100,n,k,ff2^0*subst(lift(lift(M[n,k])),'s,ff2));
  inds=matindexrank(M0);rows=Vec(inds[1]);cols=Vec(inds[2]);
  if(#rows!=73,error("actual weight-two rank is not73"));
  det0=matdet(vecextract(M0,rows,cols));
  print("Actual mod47 rank73, unit minor ",det0," ",getwalltime());
  V=vecextract(M,"..",cols);PV=vecextract(V,rows,"..");
  C0=vecextract(M0,rows,cols)^-1;
  C=matrix(73,73,i,j,subst(C0[i,j].pol,'s,u2));
  for(k=1,2,C=C*(2*matid(73)-PV*C));
  if(PV*C!=matid(73),error("lifted evaluation inverse"));
  W=V*C;
  if(vecextract(W,rows,"..")!=matid(73),error("normalized evaluation basis"));
  Y=matrix(820,73,n,k,subst(lift(W[tau[n],k]),'s,-u2));Frob=vecextract(Y,rows,"..");
  if(W*Frob!=Y,error("actual Galois descent of the complete evaluation space"));
  if(Frob*matrix(73,73,i,j,subst(lift(Frob[i,j]),'s,-u2))!=matid(73),error("quadratic descent cocycle"));
  for(k=1,#fields,
    record=fields[k];fac=Pol(record[1],'y);tn=Pol(record[2][2],'y)/record[2][1];
    Lfactor*=polresultant(fac,'x^2-tn*'x+47,'y);
  );
  if(poldegree(Lfactor)!=108||polcoef(Lfactor,107)!=81||polcoef(Lfactor,0)!=47^54,error("actual local factor"));
  for(k=0,108,if(denominator(polcoef(Lfactor,k))!=1,error("local factor integrality")));
  for(k=0,54,if(polcoef(Lfactor,k)!=47^(54-k)*polcoef(Lfactor,108-k),error("local factor functional equation")));
  write(path,[precision,p41l_vec(ii),pairs,rows,cols,ns,vector(820,n,vector(2,i,vector(2,j,gg[n][i,j]))),
    vector(42,n,vector(2,i,vector(2,j,H[n][i,j]))),tau,
    [lift(polcoef(det0.pol,0)),lift(polcoef(det0.pol,1))],p41m_encode(C),p41m_encode(W),p41m_encode(Frob),Vec(Lfactor)]);
  print("Complete actual evaluation model saved modulo47^",precision," ",getwalltime());
};
