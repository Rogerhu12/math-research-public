// Original h* integer audit. ChatGPT (AI), root. 2026-11-16.
export function auditOriginalHstar(input,point="63",prime="127") {
 const b=a=>a.map(BigInt),mul=(a,b)=>{let c=Array(a.length+b.length-1).fill(0n);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)c[i+j]+=a[i]*b[j];return c;};
 const f=b(input.FPlus),g=b(input.FMinus),e=b(input.E8),h=mul([0n,0n,0n,1n],mul(mul(f,f),mul(mul(g,g),e)));
 if(h.length!==24||h.some((v,i)=>v!==BigInt(input.hStarCoefficients[i])))throw Error("Original coefficient identity");
 const x=BigInt(point),p=BigInt(prime),ev=a=>a.reduceRight((u,v)=>u*x+v,0n),mod=v=>((v%p)+p)%p;
 const vals={FPlus:ev(f),FMinus:ev(g),E8:ev(e),hstar:ev(h)};
 if(vals.hstar!==x**3n*vals.FPlus**2n*vals.FMinus**2n*vals.E8)throw Error("Horner identity");
 let inverse=1n;while(inverse<p&&mod(inverse*h[23])!==1n)inverse++;if(inverse===p)throw Error("Nonunit leading coefficient");
 return {all24OriginalCoefficientsMatched:true,values:Object.fromEntries(Object.entries(vals).map(([k,v])=>[k,String(v)])),mod127:Object.fromEntries(Object.entries(vals).map(([k,v])=>[k,String(mod(v))])),monicAt63:String(mod(vals.hstar*inverse))};
}
