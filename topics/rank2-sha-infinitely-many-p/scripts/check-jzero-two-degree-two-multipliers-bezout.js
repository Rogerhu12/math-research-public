"use strict";
// Exact fixed integer certificate for R366. No target-prime sampling.
function add(a,b){const r=Array(Math.max(a.length,b.length)).fill(0n);for(let i=0;i<r.length;i++)r[i]=(a[i]||0n)+(b[i]||0n);return trim(r);}
function scale(a,c){return trim(a.map(x=>x*c));}
function trim(a){while(a.length>1&&a[a.length-1]===0n)a.pop();return a;}
function mul(a,b){const r=Array(a.length+b.length-1).fill(0n);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)r[i+j]+=a[i]*b[j];return trim(r);}
function equal(a,b){a=trim(a.slice());b=trim(b.slice());return a.length===b.length&&a.every((x,i)=>x===b[i]);}
function assert(ok,label){if(!ok)throw Error(label);}
const certificate = {
  "m": 68,
  "P5": [
    "1453933568",
    "-110145744",
    "3286830",
    "-48315",
    "350",
    "-1"
  ],
  "P11": [
    "143746751770690322432",
    "-25128299125929231616",
    "1962971811893150432",
    "-90505446934949816",
    "2738004949542940",
    "-57094912473038",
    "837797842035",
    "-8654615013",
    "61705710",
    "-289300",
    "803",
    "-1"
  ],
  "U": [
    "72481798322203529923681046985187211520",
    "-11502810853413039056123710243243036384",
    "804300560683587649508117438895826552",
    "-32651930132562937473107831542877340",
    "852887020985620225381628743709150",
    "-14988288513162240742534504932451",
    "179598313397055640038302844861",
    "-1449995207939593618688897870",
    "7554162979292297085413300",
    "-22948575824487295830355",
    "30890608812371990457"
  ],
  "V": [
    "-733120702162865882540879760",
    "43728349002672218202947326",
    "-951021737129710830630203",
    "8955130032482784153334",
    "-30890608812371990457"
  ],
  "C": "57898118088659915362886263937901527040",
  "verified": true
};
function check(){
 const m=68n,P=[[1n],[68n,-1n]];
 for(let r=1;r<11;r++)P.push(add(mul([m+BigInt(r),-1n],P[r]),scale(P[r-1],-m*BigInt(r))));
 const expected5=certificate.P5.map(BigInt), expected11=certificate.P11.map(BigInt);
 assert(equal(P[5],expected5),"P5 recurrence");
 assert(equal(P[11],expected11),"P11 recurrence");
 const U=certificate.U.map(BigInt),V=certificate.V.map(BigInt),C=BigInt(certificate.C);
 assert(equal(add(mul(U,P[5]),mul(V,P[11])),[C]),"Full Bezout identity");
 assert(C!==0n,"Nonzero fixed integer");
 // Verify recurrence agrees with the defining falling-factorial formula.
 for(let r=0;r<=11;r++){
   let a=[0n], falling=[1n],choose=1n;
   for(let j=0;j<=r;j++){
     if(j){falling=mul(falling,[1n-BigInt(j),1n]);choose=choose*BigInt(r-j+1)/BigInt(j);}
     a=add(a,scale(falling,(j%2?-1n:1n)*choose*(m**BigInt(r-j))));
   }
   assert(equal(a,P[r]),"Falling-factorial definition at r="+r);
 }
 return {checks:16,P5_degree:P[5].length-1,P11_degree:P[11].length-1,constant:C.toString(),status:"PASS"};
}

console.log(JSON.stringify(check(),null,2));
