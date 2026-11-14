\\ R85: actual necklace polarization on modular symbols, then inert-CM coordinates.
\\ No field/type identification by numerical eigenvalues or dimensions.
default(parisizemax,536870912);
default(parisize,67108864);
require(condition,label)={if(!condition,print("FAIL: ",label);quit(1));};
twist_row(M,P,D)={
  my(m=abs(D),v=vector(matsize(P)[2]));
  for(a=1,m-1,v+=kronecker(D,a)*mseval(M,P,[a/m,oo]));v;
};
krylov(v,H)={
  my(n=#v,K=matrix(n,n),w=v);
  for(i=1,n,K[i,]=w;w=w*H);K;
};
mob(G,z)={
  if(z==oo,if(G[2,1]==0,oo,G[1,1]/G[2,1]),
    if(G[2,1]*z+G[2,2]==0,oo,(G[1,1]*z+G[1,2])/(G[2,1]*z+G[2,2])));
};
encode_polynomial(f,m)={
  my(d=denominator(Vec(f)));
  [d,vector(m,j,d*polcoef(f,m-j))];
};

gettime();
M=msinit(1681,2,-1); N=msnew(M);
W=msatkinlehner(M,1681,N);
P=N[1]*matker(W-matid(117));
require(msdim(M)==143 && matsize(P)[2]==54,"actual space");
require(msstar(M)==-matid(143) && msatkinlehner(M,1681,P)==matid(54),"signs");
H=mshecke(M,2,P)+2*mshecke(M,3,P);
require(denominator(H)==6,"Hecke denominator");
v4=twist_row(M,P,-4); v3=twist_row(M,P,-3); v7=twist_row(M,P,-7);
require(v4==mseval(M,P,[1/4,3/4]),"cyclic path for chi_minus4");
require(lift(matdet(Mod(krylov(v3,H),1009)))==92,"D=-3 nonvanishing");
require(lift(matdet(Mod(krylov(v7,H),1009)))==483,"D=-7 nonvanishing");

\\ On the split-normalizer curve, lambda*phi has coefficient 20 on the base
\\ pair and 1 on every {a,b} with a square and b nonsquare. On Fricke-plus,
\\ q^dagger*q is twice this operator. A right-coset representative acts
\\ contragrediently on symbols, hence g^-1, then diag(41,1) conjugation.
p=41; vk=40*v4; paths=0;
{for(a=1,p-1,if(kronecker(a,p)==1,
  for(b=1,p-1,if(kronecker(b,p)==-1,
    C=lift(1/Mod(a-b,p)); A=lift(Mod(a*C,p));
    while(gcd(A,C)!=1,A+=p);
    be=bezout(A,C); D=be[1]; B=-be[2];
    k=lift(Mod(1-D,p)/Mod(C,p)); D+=C*k; B+=A*k;
    require(A*D-B*C==1,"SL2 integral lift");
    require(lift(Mod(A/C,p))==a && lift(Mod(B/D,p))==b,"correct unordered pair");
    G=[p*D,-B;-p^2*C,p*A];
    vk+=2*mseval(M,P,[mob(G,1/4),mob(G,3/4)]);
    paths++;
  ));
));}
require(paths==400 && denominator(vk)==1,"actual integral polarization row");

cp=charpoly(H); fac=factor(cp);
F2='x^2-40*'x+80;
F3='x^3-83*'x^2+2035*'x-12769;
F4='x^4-48*'x^3+544*'x^2-1792*'x+256;
F6='x^6-94*'x^5+3159*'x^4-45828*'x^3+275615*'x^2-613310*'x+212521;
expected=['x-32,'x-16,'x-25,'x-36,F2,F4,F3,F6];
out=vector(8);
{for(i=1,8,
  f=fac[i,1]; m=poldegree(f);
  V=matker(subst(f,'x,H)); C=matinverseimage(V,H*V);
  require(matsize(V)[2]==m && V*C==H*V,"factor restriction");
  w4=v4*V; K=krylov(w4,C);
  ck=((K~)^-1*(vk*V)~)~;
  c3=((K~)^-1*(v3*V)~)~;
  c7=((K~)^-1*(v7*V)~)~;
  kap=sum(j=1,m,ck[j]*'x^(j-1));
  R3=sum(j=1,m,c3[j]*'x^(j-1));
  R7=sum(j=1,m,c7[j]*'x^(j-1));
  require(subst(expected[i],'x,Mod(kap,f)/2)==0,"R71 minimal polynomial on the actual factor");
  fy=subst(f,'x,'y);
  r3=nfroots(fy,'x^2-Mod(subst(1800*R3,'x,'y),fy)/Mod(subst(kap,'x,'y),fy));
  r7=nfroots(fy,'x^2-Mod(subst(200*R7,'x,'y),fy)/Mod(subst(kap,'x,'y),fy));
  require(#r3==2 && #r7==2,"nonzero coordinate squares");
  require(Mod(subst(kap,'x,'y),fy)*r3[1]^2==1800*Mod(subst(R3,'x,'y),fy),"D=-3 scale");
  require(Mod(subst(kap,'x,'y),fy)*r7[1]^2==200*Mod(subst(R7,'x,'y),fy),"D=-7 scale");
  out[i]=[Vec(f),encode_polynomial(kap,m),encode_polynomial(lift(r3[1]),m),encode_polynomial(lift(r7[1]),m),Vec(expected[i])];
);}
print("Actual correspondence and all coordinate identities passed; milliseconds: ",gettime());
print("CERTIFICATE_BEGIN");
print("{");
print("\"pari_version\":",version(),",");
print("\"level\":1681,\"weight\":2,\"star\":-1,\"fricke\":1,\"new\":true,");
print("\"dimension\":54,\"hecke_generator\":\"T2+2*T3\",\"hecke_denominator\":6,");
print("\"hecke_reference\":\"p41_cm_ratio_certificate.json\",");
print("\"hecke_reference_sha256\":\"28f49fe984a43b2e9f556e7030f1afa14cc777c304cde8e8a2731c11afad9899\",");
print("\"path_count\":400,\"base_pair_coefficient\":40,\"other_pair_coefficient\":2,");
print("\"twist3_exact\":",v3,",\"twist7_exact\":",v7,",");
print("\"krylov_determinants_mod1009\":[92,483],");
print("\"polarization_row_exact\":",vk,",");
print("\"one_algebraic_square_root_no_point_sign\":true,");
print("\"fields\":[");
{for(i=1,8,
  print("{\"factor_descending\":",out[i][1],",");
  print("\"kappa_denominator\":",out[i][2][1],",\"kappa_numerator_descending\":",out[i][2][2],",");
  print("\"root3_denominator\":",out[i][3][1],",\"root3_numerator_descending\":",out[i][3][2],",");
  print("\"root7_denominator\":",out[i][4][1],",\"root7_numerator_descending\":",out[i][4][2],",");
  print("\"minimal_polynomial_half_kappa_descending\":",out[i][5],"}",if(i<8,",",""));
);}
print("]");
print("}");
print("CERTIFICATE_END");
quit;
