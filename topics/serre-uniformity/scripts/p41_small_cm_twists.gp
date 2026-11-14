\\ R79: exact nonvanishing for the two CM divisors in the T2 translation.
\\ PARI/GP 2.19.0; reconstructs the real star-minus, new, Fricke-plus space.
\\ Its H=T2+2*T3 is in exactly the basis used by R74's JSON certificate.

default(parisizemax,536870912);
default(parisize,67108864);

require(condition,label) = {
  if(!condition, print("FAIL: ",label); quit(1));
};
twist_row(M,P,D) = {
  my(m=abs(D), out=vector(matsize(P)[2]));
  for(a=1,m-1,out+=kronecker(D,a)*mseval(M,P,[a/m,oo]));
  out;
};
krylov_row_matrix(v,H) = {
  my(n=matsize(H)[1], out=matrix(n,n), row=v);
  for(i=1,n,out[i,]=row;row=row*H);
  out;
};

gettime();
M=msinit(1681,2,-1);
require(msdim(M)==143 && msstar(M)==-matid(143),"star-minus space");
N=msnew(M);
require(matsize(N[1])[2]==117,"new cuspidal dimension");
W=msatkinlehner(M,1681,N);
P=N[1]*matker(W-matid(117));
require(matsize(P)[2]==54,"new Fricke-plus dimension");
require(msatkinlehner(M,1681,P)==matid(54),"Fricke-plus restriction");
T2=mshecke(M,2,P);
T3=mshecke(M,3,P);
H=T2+2*T3;
require(T2*T3==T3*T2 && denominator(H)==6,"same Hecke generator as R74");
require(trace(T2)==-8,"geometric T2 trace");
cp=charpoly(H);
require(poldegree(gcd(cp,deriv(cp)))==0,"54 distinct Hecke eigenvalues");
v4=twist_row(M,P,-4);
v8=twist_row(M,P,-8);
require(denominator(v4)==1 && denominator(v8)==1,"integral twist rows");
K4=krylov_row_matrix(v4,H);
K8=krylov_row_matrix(v8,H);
d4=lift(matdet(Mod(K4,1009)));
d8=lift(matdet(Mod(K8,1009)));
require(d4==414 && d8==520,"finite-field Krylov determinants");
require(matrank(K4)==54 && matrank(K8)==54,"exact rational ranks");
require(qfbclassno(-4)==1 && qfbclassno(-8)==1,"class numbers");
require(kronecker(-4,41)==1 && kronecker(-8,41)==1,"41 split");
require(kronecker(-4,47)==-1 && kronecker(-8,47)==-1,"47 inert, not split");
print("All exact checks passed; elapsed milliseconds: ",gettime());
print("D=-4,-8 Krylov determinants mod 1009: ",[d4,d8]);
print("CERTIFICATE_BEGIN");
print("{");
print("\"pari_version\":",version(),",");
print("\"level\":1681,\"weight\":2,\"star\":-1,\"fricke\":1,\"new\":true,");
print("\"dimension\":54,\"hecke_generator\":\"T2+2*T3\",\"hecke_denominator\":6,");
print("\"trace_T2\":-8,\"modulus\":1009,");
print("\"hecke_reference\":\"p41_twist_certificate.json\",");
print("\"hecke_reference_sha256\":\"1c0feeac934b5fa55f78b8ee318a829f2212d4f87b95532e4881ac72980e1ceb\",");
print("\"twist4_exact\":",v4,",");
print("\"twist8_exact\":",v8,",");
print("\"krylov_determinants_mod\":[414,520]");
print("}");
print("CERTIFICATE_END");
quit;
