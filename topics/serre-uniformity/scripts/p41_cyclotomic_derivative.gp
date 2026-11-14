\\ R77: first 47-adic derivative digit on all 54 actual eigensymbols.
\\ PARI/GP 2.19.0; no overconvergent-symbol routines or coefficient splitting.
\\ Run: gp -q -f p41_cyclotomic_derivative.gp

default(parisizemax,536870912);
default(parisize,67108864);

require(condition,label) = {
  if(!condition,print("FAIL: ",label);quit(1));
};

json_matrix(A) = {
  my(n=matsize(A)[1], out="[");
  for(i=1,n,if(i>1,out=concat(out,","));out=concat(out,Str(Vec(A[i,]))));
  concat(out,"]");
};

krylov_row_matrix(v,H) = {
  my(n=matsize(H)[1],out=matrix(n,n),row=v);
  for(i=1,n,out[i,]=row;row=row*H);
  out;
};

gettime();
M=msinit(1681,2,1);
require(msdim(M)==144 && msstar(M)==matid(144),"actual star-plus space");
Nnew=msnew(M);
require(matsize(Nnew[1])[2]==117,"new dimension");
W=msatkinlehner(M,1681,Nnew);
P=Nnew[1]*matker(W-matid(117));
require(matsize(P)[2]==54,"new Fricke-plus dimension");
require(msatkinlehner(M,1681,P)==matid(54),"Fricke-plus sign");
generator_values=mseval(M,P);
require(#generator_values==54 && #generator_values[1]==287,"path generators");
require(denominator(generator_values)==1,"ALL generator values integral");
require(matrank(Mod(P,47))==54,"basis independent modulo 47");
central=mseval(M,P,[0,oo]);
require(central==vector(54),"central value vanishes by Fricke-plus");
T2=mshecke(M,2,P);T3=mshecke(M,3,P);T47=mshecke(M,47,P);
H=T2+2*T3;
require(denominator(H)==2 && denominator(T47)==2,"operator denominators");
require(H*T47==T47*H,"ordinary root commutes with H");
Hm=Mod(H,47);Tm=Mod(T47,47);
require(lift(matdet(Tm))==28,"ordinary T47 unit");
print("Initialized integral symbols; elapsed milliseconds: ",gettime());

S2=Mod(vector(54),47);
class_weights=Mod(vector(46),47);
class_sums=matrix(46,54);
{for(a=1,47^2-1,if(a%47,
  a0=a%47;
  weight=Mod((lift(Mod(a,47^2)^46)-1)/47,47)/46;
  values=mseval(M,P,[a/47^2,oo]);
  require(denominator(values)==1,"integral path evaluation");
  S2+=weight*Mod(values,47);
  class_weights[a0]+=weight;
  class_sums[a0,]+=values;
));}
require(lift(class_weights)==vector(46),"weight sums on every mod47 class");
S1=Mod(vector(54),47);
{for(a0=1,46,
  v1=mseval(M,P,[a0/47,oo]);
  require(class_sums[a0,]==v1*T47-central,"exact T47 path-distribution relation");
  S1+=class_weights[a0]*Mod(v1,47);
);}
require(lift(S1)==vector(54),"second ordinary-root term cancels");
R=S2*Tm^(-2)-S1*Tm^(-3);
K=krylov_row_matrix(R,Hm);
detK=lift(matdet(K));
require(matrank(K)==54 && detK==21,"derivative row cyclic modulo47");
require(R*Tm^2==S2,"ordinary-root factor retained");
print("Derivative digit R = Lprime/47 mod47: ",lift(R));
print("Krylov rank and determinant mod47: ",[matrank(K),detK]);
print("All exact checks passed; path computation milliseconds: ",gettime());

print("CERTIFICATE_BEGIN");
print("{");
print("\"pari_version\":",version(),",");
print("\"level\":1681,\"weight\":2,\"star\":1,\"fricke\":1,\"new\":true,");
print("\"dimension\":54,\"path_generator_count\":287,\"generator_value_denominator\":1,");
print("\"modulus\":47,\"hecke_generator\":\"T2+2*T3\",\"operator_denominators\":[2,2],");
print("\"hecke_matrix_mod\":",json_matrix(lift(Hm)),",");
print("\"ordinary_matrix_mod\":",json_matrix(lift(Tm)),",");
print("\"weighted_path_sum_mod\":",lift(S2),",");
print("\"second_term_mod\":",lift(S1),",");
print("\"derivative_digit_mod\":",lift(R),",");
print("\"krylov_determinant_mod\":21,\"ordinary_determinant_mod\":28");
print("}");
print("CERTIFICATE_END");
