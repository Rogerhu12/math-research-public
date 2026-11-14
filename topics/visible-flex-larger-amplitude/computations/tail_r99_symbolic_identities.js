function sha256(text) {
  const bytes=[];
  for(const ch of text){const c=ch.codePointAt(0);if(c<128)bytes.push(c);else if(c<2048)bytes.push(192|(c>>>6),128|(c&63));else if(c<65536)bytes.push(224|(c>>>12),128|((c>>>6)&63),128|(c&63));else bytes.push(240|(c>>>18),128|((c>>>12)&63),128|((c>>>6)&63),128|(c&63));}
  const bitLength=bytes.length*8;
  bytes.push(128);while(bytes.length%64!==56)bytes.push(0);
  const hi=Math.floor(bitLength/4294967296),lo=bitLength>>>0;
  for(let j=3;j>=0;j--)bytes.push((hi>>>(8*j))&255);
  for(let j=3;j>=0;j--)bytes.push((lo>>>(8*j))&255);
  const h=[0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19];
  const k=[0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2];
  const ro=(v,n)=>(v>>>n)|(v<<(32-n));
  for(let off=0;off<bytes.length;off+=64){
    const w=new Array(64);
    for(let j=0;j<16;j++)w[j]=((bytes[off+4*j]<<24)|(bytes[off+4*j+1]<<16)|(bytes[off+4*j+2]<<8)|bytes[off+4*j+3])>>>0;
    for(let j=16;j<64;j++){const x=w[j-15],y=w[j-2];w[j]=(w[j-16]+(ro(x,7)^ro(x,18)^(x>>>3))+w[j-7]+(ro(y,17)^ro(y,19)^(y>>>10)))>>>0;}
    let [a,b,c,d,e,f,g,hh]=h;
    for(let j=0;j<64;j++){const t1=(hh+(ro(e,6)^ro(e,11)^ro(e,25))+((e&f)^((~e)&g))+k[j]+w[j])>>>0;const t2=((ro(a,2)^ro(a,13)^ro(a,22))+((a&b)^(a&c)^(b&c)))>>>0;hh=g;g=f;f=e;e=(d+t1)>>>0;d=c;c=b;b=a;a=(t1+t2)>>>0;}
    [a,b,c,d,e,f,g,hh].forEach((v,j)=>{h[j]=(h[j]+v)>>>0;});
  }
  return h.map(x=>x.toString(16).padStart(8,"0")).join("");
}

// Exact finite consumer for the published complete cell0/seg7 candidate.
// Plain JavaScript BigInt only: no Node API, floating acceptance, ODE or source evaluation.
// The caller must bind the exact input hashes and store the output.
// Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.

function verifyR99Identities(rawSource) {
  const expected="85bf30e818e7ab92107a5f5a537225afb9273877327bf6e0092b303b01a1b5d8";
  if (sha256(rawSource)!==expected) throw Error("The frozen full finite-J source changed");
  const names=["k","c","kx","cx","T","P","z","ell","s","U"];
  const n=names.length, empty=()=>Array(n).fill(0).join(",");
  const constant=v=>new Map(v===0n?[]:[[empty(),v]]);
  const variable=name=>{const e=Array(n).fill(0);e[names.indexOf(name)]=1;return new Map([[e.join(","),1n]]);};
  const add=(...a)=>{const r=new Map();for(const p of a)for(const [m,c]of p){const v=(r.get(m)||0n)+c;if(v===0n)r.delete(m);else r.set(m,v);}return r;};
  const scale=(p,c)=>new Map([...p].map(([m,v])=>[m,v*c]).filter(([,v])=>v!==0n));
  const mul=(a,b)=>{const r=new Map();for(const [ma,ca]of a)for(const [mb,cb]of b){const ea=ma.split(",").map(Number),eb=mb.split(",").map(Number);const key=ea.map((v,i)=>v+eb[i]).join(",");const v=(r.get(key)||0n)+ca*cb;if(v===0n)r.delete(key);else r.set(key,v);}return r;};
  const square=a=>mul(a,a),one=constant(1n);
  const [k,c,kx,cx,T,P,z,ell,s,U]=names.map(variable);
  const E=add(one,z),K=add(k,c),Kx=add(kx,cx);
  const lnm=add(k,mul(E,T)),L=add(one,K,mul(E,T));
  const linear=add(kx,mul(ell,add(scale(k,2n),T)));
  const quadratic=add(mul(lnm,kx),scale(mul(mul(E,s),square(U)),-1n),
    mul(ell,add(square(k),mul(z,square(P)),mul(k,T))));
  const implemented=add(linear,quadratic,mul(linear,c),mul(lnm,cx),
    mul(cx,add(one,c)),mul(ell,add(scale(c,2n),square(c))));
  const direct=add(mul(L,Kx),
    mul(ell,add(scale(K,2n),T,square(K),mul(z,square(P)),mul(K,T))),
    scale(mul(mul(E,s),square(U)),-1n));
  const expansionDifference=add(implemented,scale(direct,-1n));
  const physicalLeft=mul(L,add(mul(ell,add(one,K)),Kx));
  const phiNumerator=add(
    mul(ell,add(one,mul(z,add(mul(add(one,K),T),scale(square(P),-1n))))),
    mul(mul(E,s),square(U)));
  const physicalDifference=add(physicalLeft,scale(phiNumerator,-1n),scale(direct,-1n));
  const meanIndices=[names.indexOf("c"),names.indexOf("cx")];
  const meanTerms=[...implemented].filter(([m])=>meanIndices.some(i=>Number(m.split(",")[i])>0)).length;
  if(expansionDifference.size||physicalDifference.size||!meanTerms) throw Error("An exact complete-mean polynomial identity failed");
  return {
    schema:"r99-full-mean-polynomial-identities-v1",
    author:"tail_refinement (GPT-6 Astra Pro, AI-assisted)",date:"2026-11-12",
    arithmetic:"Exact BigInt polynomial addition and multiplication; zero means no remaining monomial",
    actual_input_sha256:expected,input_source:"computations/tail_outer_substage_span_refinement.py",
    variable_order:names,definitions:{K:"k+c",Kx:"kx+cx",E:"1+z",L:"1+K+E*T",ell:"w_x/w",s:"r_x/r"},
    full_finite_J_monomials:implemented.size,monomials_containing_c_or_cx:meanTerms,
    complete_mean_expansion_difference_monomials:expansionDifference.size,
    physical_hrr_identity_difference_monomials:physicalDifference.size,
    gates:{complete_frozen_source_hash:true,all_c_and_cx_terms_retained:meanTerms>0,
      full_finite_J_equals_complete_formula:expansionDifference.size===0,
      physical_second_derivative_identity:physicalDifference.size===0},
    actual_execution:"functions.exec V8 exact BigInt; no Node, Python, shell or Arb execution",
    scientific_source_or_integral_rerun:false,solution_existence_or_error_gate_claimed:false
  };
}
