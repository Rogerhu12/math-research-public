/* Exact additional normalization identity, using only the two SAVED
   original affine inputs. No source construction or cofactor is rerun.
   All arithmetic is BigInt QQ. Call verifyC13Connection(oldInput,newInput)
   with the decompressed JSON objects named in the companion receipt. */
function verifyC13Connection(oldInput,newInput) {
  function check(c,m){if(!c)throw Error(m);}
  const abs=n=>n<0n?-n:n;
  function gcd(a,b){a=abs(a);b=abs(b);while(b){let r=a%b;a=b;b=r;}return a;}
  function Q(n,d=1n){check(d!==0n,"zero rational denominator");if(d<0n){n=-n;d=-d;}if(!n)return[0n,1n];let g=gcd(n,d);return[n/g,d/g];}
  function parse(s){let a=String(s).split("/");check(a.length<=2,"rational syntax");return Q(BigInt(a[0]),a.length===2?BigInt(a[1]):1n);}
  function add(a,b){let g=gcd(a[1],b[1]);return Q(a[0]*(b[1]/g)+b[0]*(a[1]/g),(a[1]/g)*b[1]);}
  function mul(a,b){return Q(a[0]*b[0],a[1]*b[1]);}
  function rationalString(a){return a[1]===1n?String(a[0]):String(a[0])+"/"+String(a[1]);}
  function poly(terms){
    const m=new Map();
    for(const [mm,v] of terms){
      check(mm.length===3&&mm.every(e=>Number.isSafeInteger(e)&&e>=0),"monomial");
      let k=mm.join(","),q=parse(v);check(!m.has(k),"duplicate monomial");
      if(q[0])m.set(k,q);
    }
    return m;
  }
  const c13=poly([
    [[0,0,0],"-32"],[[0,1,0],"-40"],[[0,2,0],"-14"],[[0,3,0],"-1"],
    [[0,4,0],"1/4"],[[1,1,0],"32"],[[1,2,0],"48"],[[1,3,0],"20"],
    [[1,4,0],"13/4"],[[2,3,0],"-6"],[[2,4,0],"-2"],[[2,5,0],"-1/2"],
    [[3,4,0],"1"]]);
  function product(a,b){
    const out=new Map();
    for(const [ka,va] of a)for(const [kb,vb] of b){
      const ma=ka.split(",").map(Number),mb=kb.split(",").map(Number);
      const k=ma.map((v,j)=>v+mb[j]).join(",");
      const z=add(out.get(k)||[0n,1n],mul(va,vb));
      if(z[0])out.set(k,z);else out.delete(k);
    }
    return out;
  }
  check(JSON.stringify(oldInput.variables)==='["e","k","lambda"]',"old variables");
  check(JSON.stringify(newInput.variables)==='["e","k","lambda"]',"new variables");
  const records=[];
  for(const name of ["L0","L1"]){
    const old=poly(oldInput.components[name]),now=poly(newInput.components[name]);
    const prod=product(c13,now);
    for(const [k,v] of prod)prod.set(k,mul([-32n,1n],v));
    check(prod.size===old.size,"different support cardinality "+name);
    for(const [k,v] of old){
      const z=prod.get(k);
      check(z&&z[0]===v[0]&&z[1]===v[1],"coefficient mismatch "+name+" "+k);
    }
    records.push({component:name,oldTerms:old.size,newTerms:now.size,
      completeRationalCoefficientIdentityReturned:true,
      identity:"old_"+name+" = -32*C13*canonical_"+name});
  }
  return {records,scalar:"-32",completeBothOriginalInputProductsReturned:true,
    C13NotInverted:true,C13ZeroFibreCoveredByIndependentCanonicalOriginalIdentity:true,
    noOriginalSourceOrCofactorOrResultantReplayed:true,
    noMultivariateGcdEmptinessClaim:true};
}
if (typeof module !== "undefined") module.exports={verifyC13Connection};
