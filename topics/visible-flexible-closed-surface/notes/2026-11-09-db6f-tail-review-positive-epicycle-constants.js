"use strict";
// Exact rational gates for the independently reviewed positive epicycle.
// No geometry arrays, sampling, PDE, BVP, matrix solver, or file I/O.
function positiveEpicycleRationalReview() {
  const checks=[];
  function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){const t=a%b;a=b;b=t;}return a;}
  function Q(n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return[n/g,d/g];}
  function D(s){const [a,b=""]=s.split(".");return Q(BigInt(a+b),10n**BigInt(b.length));}
  const add=(a,b)=>Q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
  const neg=a=>Q(-a[0],a[1]);
  const sub=(a,b)=>add(a,neg(b));
  const mul=(a,b)=>Q(a[0]*b[0],a[1]*b[1]);
  const div=(a,b)=>Q(a[0]*b[1],a[1]*b[0]);
  const sq=a=>mul(a,a);
  const cube=a=>mul(sq(a),a);
  const fourth=a=>sq(sq(a));
  function gate(name,a,op,b){const x=a[0]*b[1],y=b[0]*a[1];const ok=op==="<"?x<y:op===">"?x>y:op==="="?x===y:false;if(!ok)throw Error(name);checks.push(name);}
  const one=Q(1n),two=Q(2n),three=Q(3n),six=Q(6n);
  const el=D("0.707"),eh=D("0.708"),pl=D("0.516"),ph=D("0.518"),ql=D("0.855"),qh=D("0.857");
  gate("eta lower",sq(el),"<",Q(1n,2n));
  gate("eta upper",sq(eh),">",Q(1n,2n));
  const den=e=>sub(add(one,mul(six,e)),mul(three,sq(e)));
  const p2=e=>div(mul(two,sub(one,sq(e))),den(e));
  gate("denominator lower endpoint",den(el),">",Q(0n));
  gate("denominator upper endpoint",den(eh),">",Q(0n));
  gate("p lower",p2(eh),">",sq(pl));
  gate("p upper",p2(el),"<",sq(ph));
  gate("q lower",sub(one,sq(ph)),">",sq(ql));
  gate("q upper",sub(one,sq(pl)),"<",sq(qh));
  const jm=sub(mul(sub(el,three),qh),mul(eh,ph));
  const jp=add(mul(sub(eh,three),ql),mul(eh,ph));
  const wl=sub(Q(10n),mul(six,eh)),wh=sub(Q(10n),mul(six,el));
  gate("J interval order",jm,"<",jp);
  gate("J strictly negative",jp,"<",Q(0n));
  gate("speed squared lower",sub(wl,sq(jm)),">",Q(3n,10n));
  gate("speed squared upper",wh,"<",six);
  const cm=sub(Q(19n),mul(Q(9n),eh));
  const zp=mul(mul(three,wh),qh);
  const cubicUpper=j=>add(mul(j,sub(cm,sq(j))),zp);
  gate("triple product upper at J lower",cubicUpper(jm),"<",Q(-1n));
  gate("triple product upper at J upper",cubicUpper(jp),"<",Q(-1n));
  gate("six sqrt six below fifteen squared",Q(216n),"<",Q(225n));
  const Rlo=add(Q(1n,2n),mul(sub(mul(three,el),Q(3n,4n)),sq(pl)));
  const Rhi=add(Q(1n,2n),mul(sub(mul(three,eh),Q(3n,4n)),sq(ph)));
  const Plo=div(mul(mul(pl,ql),add(Q(3n,2n),el)),two);
  const Phi=div(mul(mul(ph,qh),add(Q(3n,2n),eh)),two);
  const Ahi=div(mul(mul(ph,qh),sq(sub(one,el))),Q(4n));
  const Bhi=div(mul(mul(eh,sq(ph)),sub(one,el)),Q(28n));
  const Chi=div(mul(mul(eh,sq(ph)),add(one,eh)),Q(20n));
  const Ulo=div(mul(mul(mul(el,pl),ql),sub(three,mul(two,eh))),three);
  const Vhi=div(sq(ph),Q(24n));
  gate("R lower",Rlo,">",D("0.86"));
  gate("R upper",Rhi,"<",D("0.88"));
  gate("P lower",Plo,">",D("0.48"));
  gate("P upper",Phi,"<",D("0.5"));
  gate("A upper",Ahi,"<",D("0.01"));
  gate("B upper",Bhi,"<",D("0.003"));
  gate("C upper",Chi,"<",D("0.017"));
  gate("U lower",Ulo,">",D("0.16"));
  gate("V upper",Vhi,"<",D("0.012"));
  const radialLo=sub(D("0.86"),add(add(D("0.5"),D("0.01")),add(D("0.003"),D("0.017"))));
  const radialHi=add(D("0.88"),add(add(D("0.5"),D("0.01")),add(D("0.003"),D("0.017"))));
  gate("horizontal radius lower ledger",radialLo,"=",D("0.33"));
  gate("horizontal radius upper ledger",radialHi,"=",D("1.41"));
  const h1=mul(two,mul(D("0.48"),D("0.86")));
  const h2=mul(two,add(add(mul(D("0.017"),D("0.88")),mul(D("0.5"),D("0.01"))),mul(D("0.88"),D("0.003"))));
  const h3=mul(two,add(mul(D("0.017"),D("0.01")),mul(D("0.5"),D("0.003"))));
  const h4=mul(two,mul(D("0.017"),D("0.003")));
  gate("h1 lower ledger",h1,"=",D("0.8256"));
  gate("h2 upper ledger",h2,"=",D("0.0452"));
  gate("h3 upper ledger",h3,"=",D("0.00334"));
  gate("h4 upper ledger",h4,"=",D("0.000102"));
  const monotonic=sub(sub(sub(h1,mul(Q(4n),h2)),mul(Q(9n),h3)),mul(Q(16n),h4));
  gate("radial monotonic ledger",monotonic,"=",Q(153277n,250000n));
  gate("radial monotonic lower",monotonic,">",Q(3n,5n));
  gate("height denominator",sub(D("0.16"),mul(two,D("0.012"))),">",D("0.13"));
  const cosBound=div(mul(two,D("1.41")),Q(3n,5n));
  const sinBound=div(add(one,mul(D("0.024"),cosBound)),D("0.13"));
  gate("cosine chord coefficient",cosBound,"=",Q(47n,10n));
  gate("sine chord coefficient",sinBound,"=",Q(214n,25n));
  gate("cubic angle chord coefficient",add(sq(cosBound),sq(sinBound)),"<",Q(100n));
  const radialLip=add(add(D("0.5"),D("0.01")),mul(two,add(D("0.003"),D("0.017"))));
  gate("radial Lipschitz ledger",radialLip,"=",D("0.55"));
  gate("first angle chord bound",div(add(one,mul(Q(10n),radialLip)),D("0.33")),"<",Q(20n));
  gate("first angle arc bound",mul(Q(10n),Q(22n,7n)),"<",Q(32n));
  gate("base center reach reciprocal",mul(Q(16n),sq(Q(32n))),"=",Q(16384n));
  gate("perturbed chord coefficient",sub(Q(1n,32n),Q(1n,64n)),"=",Q(1n,64n));
  gate("perturbed center reach reciprocal",mul(Q(17n),sq(Q(64n))),"=",Q(69632n));
  const w=Q(1n,1000000n),tubeRatio=mul(mul(two,w),Q(69632n));
  gate("two-width tube ratio",tubeRatio,"<",Q(1n,5n));
  gate("projection factor",div(one,sub(one,tubeRatio)),"<",Q(5n,4n));
  gate("original angle coefficient",mul(Q(64n),Q(5n,4n)),"=",Q(80n));
  const vBound=add(add(one,Q(5n,4n)),mul(mul(mul(two,w),Q(4n)),Q(80n)));
  gate("radial coordinate difference coefficient",vBound,"<",three);
  gate("material angle coefficient",mul(Q(4n),Q(80n)),"=",Q(320n));
  gate("global material chord coefficient",add(sq(three),sq(Q(320n))),"<",sq(Q(321n)));
  const plusAbsJLower=add(mul(sub(three,eh),ql),mul(el,pl));
  const minusAbsJUpper=sub(mul(sub(three,el),qh),mul(el,pl));
  gate("speed at cosine plus one",sub(wh,sq(plusAbsJLower)),"<",Q(2n,5n));
  gate("vertical direction at cosine plus one",mul(eh,sub(qh,pl)),"<",Q(1n,4n));
  gate("speed at cosine minus one",sub(wl,sq(minusAbsJUpper)),">",three);
  gate("vertical direction at cosine minus one",mul(el,add(ql,pl)),">",Q(9n,10n));
  gate("torsion polynomial offset",mul(mul(three,wl),ql),">",Q(14n));
  gate("sqrt thirteen upper squared",sq(Q(11n,3n)),">",Q(13n));
  gate("three sqrt three lower squared",Q(27n),">",Q(25n));
  const absTripleUpper=sub(div(mul(mul(two,Q(13n)),Q(11n,3n)),Q(5n)),Q(14n));
  gate("absolute triple product upper",absTripleUpper,"<",six);
  gate("curvature at cosine plus one exceeds three",cube(Q(2n,5n)),"<",Q(1n,9n));
  gate("curvature-direction ratio at cosine minus one",div(Q(6n,5n),Q(9n,10n)),"<",two);
  gate("initial metric radius below three halves squared",add(one,sq(w)),"<",Q(9n,4n));
  gate("M remains away from zero",sub(Q(2n,3n),Q(1n,120n)),">",Q(1n,2n));
  gate("central curvature cutoff separation",cube(add(one,sq(w))),">",fourth(add(one,div(sq(w),Q(4n)))));
  gate("sphere length upper",mul(mul(two,Q(22n,7n)),Q(5n,2n)),"<",Q(16n));
  gate("small cone angle below six",mul(Q(32n),w),"<",six);
  return {status:"PASS_EXACT_RATIONAL_GATES_ONLY",checks:checks.length,
    audited_note_commit:"0239fffd6e5206dfadb778db4ba5a057e01cfc5a",
    audited_note_blob:"24c70487248a1766119cb06d1299d9686901205c",
    proves_analytic_existence:false,proves_embedding:false,
    geometry_arrays:0,pde_runs:0,numerical_solver_calls:0};
}
if(typeof module!=="undefined"&&module.exports)module.exports=positiveEpicycleRationalReview;
if(typeof require!=="undefined"&&typeof module!=="undefined"&&require.main===module){
  console.log(JSON.stringify(positiveEpicycleRationalReview(),null,2));
}
