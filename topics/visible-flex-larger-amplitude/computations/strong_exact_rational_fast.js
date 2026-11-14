"use strict";
/* Exact rational arithmetic. Only powers of two are stripped before the
   ordinary Euclidean gcd; no rounding or arithmetic tolerance is used. */
function assert(ok,message){if(!ok)throw Error(message);}
function gcd(a,b){
 a=a<0n?-a:a;b=b<0n?-b:b;
 if(a===0n)return b;if(b===0n)return a;
 // gcd(2^r*A,2^s*B)=2^min(r,s)*gcd(A,B), with A,B odd.
 const pa=a&(-a),pb=b&(-b),common=pa<pb?pa:pb;
 a/=pa;b/=pb;
 while(b){const t=a%b;a=b;b=t;}
 return a*common;
}
class Rat{
 constructor(n,d=1n){n=BigInt(n);d=BigInt(d);assert(d!==0n,"zero rational denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);this.n=n/g;this.d=d/g;}
 add(q){q=Q(q);return new Rat(this.n*q.d+q.n*this.d,this.d*q.d);}
 sub(q){return this.add(Q(q).neg());}
 mul(q){q=Q(q);return new Rat(this.n*q.n,this.d*q.d);}
 div(q){q=Q(q);return new Rat(this.n*q.d,this.d*q.n);}
 neg(){return new Rat(-this.n,this.d);}
 abs(){return this.n<0n?this.neg():this;}
 cmp(q){q=Q(q);const x=this.n*q.d-q.n*this.d;return x<0n?-1:x>0n?1:0;}
 eq(q){return this.cmp(q)===0;}
 toString(){return this.n.toString()+"/"+this.d.toString();}
 toJSON(){return this.toString();}
}
function Q(x){
 if(x instanceof Rat)return x;
 if(typeof x==="bigint")return new Rat(x);
 if(typeof x==="number"){assert(Number.isSafeInteger(x),"internal noninteger Number");return new Rat(BigInt(x));}
 assert(typeof x==="string","exact input must be a rational or decimal string");
 if(/^[+-]?\d+\/[+-]?\d+$/.test(x)){const p=x.split("/");return new Rat(BigInt(p[0]),BigInt(p[1]));}
 const m=/^([+-]?)(\d+)(?:\.(\d*))?(?:[eE]([+-]?\d+))?$/.exec(x);
 assert(m,"invalid exact decimal: "+String(x));const e=Number(m[4]||"0")-(m[3]||"").length;
 assert(Number.isSafeInteger(e)&&Math.abs(e)<=10000,"decimal exponent out of range");
 let n=BigInt(m[2]+(m[3]||""));if(m[1]==="-")n=-n;
 return e>=0?new Rat(n*10n**BigInt(e)):new Rat(n,10n**BigInt(-e));
}

if(typeof module!=="undefined")module.exports={Q};
