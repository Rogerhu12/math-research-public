#!/usr/bin/env node
// Exact algebra checks only; no actual-geometry sampling is claimed.
import fs from 'node:fs';
import crypto from 'node:crypto';
import {pathToFileURL,fileURLToPath} from 'node:url';
class Rat {
 constructor(n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}let a=n<0n?-n:n,b=d;while(b){let q=a%b;a=b;b=q;}this.n=n/a;this.d=d/a;}
 static p(v){if(v instanceof Rat)return v;let s=String(v).trim();if(s.includes("/")){let [a,b]=s.split("/");return Rat.p(a).div(Rat.p(b));}let m=s.match(/^([+-]?)(\d*)(?:\.(\d*))?(?:[eE]([+-]?\d+))?$/);if(!m||!(m[2]||m[3]))throw Error("bad rational "+s);let n=BigInt((m[2]||"0")+(m[3]||""));if(m[1]==="-")n=-n;let p=Number(m[4]||0)-(m[3]||"").length;return p>=0?new Rat(n*10n**BigInt(p)):new Rat(n,10n**BigInt(-p));}
 add(v){v=Rat.p(v);return new Rat(this.n*v.d+v.n*this.d,this.d*v.d);}
 sub(v){v=Rat.p(v);return new Rat(this.n*v.d-v.n*this.d,this.d*v.d);}
 mul(v){v=Rat.p(v);return new Rat(this.n*v.n,this.d*v.d);}
 div(v){v=Rat.p(v);return new Rat(this.n*v.d,this.d*v.n);}
 abs(){return new Rat(this.n<0n?-this.n:this.n,this.d);}
 pow(k){return new Rat(this.n**BigInt(k),this.d**BigInt(k));}
 lt(v){v=Rat.p(v);return this.n*v.d<v.n*this.d;}
 le(v){v=Rat.p(v);return this.n*v.d<=v.n*this.d;}
 eq(v){v=Rat.p(v);return this.n*v.d===v.n*this.d;}
 str(){return this.d===1n?String(this.n):`${this.n}/${this.d}`;}
 decimalUpper(digits=22){if(this.n<0n)throw Error("positive display required");let scale=10n**BigInt(digits),z=(this.n*scale+this.d-1n)/this.d;return (z/scale).toString()+"."+(z%scale).toString().padStart(digits,"0");}
}

class C {
 constructor(re=0,im=0){this.re=Rat.p(re);this.im=Rat.p(im);}
 static p(z){return z instanceof C?z:new C(z);}
 add(z){z=C.p(z);return new C(this.re.add(z.re),this.im.add(z.im));}
 neg(){return new C(this.re.mul(-1),this.im.mul(-1));}
 sub(z){return this.add(C.p(z).neg());}
 mul(z){z=C.p(z);return new C(this.re.mul(z.re).sub(this.im.mul(z.im)),this.re.mul(z.im).add(this.im.mul(z.re)));}
 zero(){return this.re.eq(0)&&this.im.eq(0);}
 record(){return {real:this.re.str(),imaginary:this.im.str()};}
}
function poly(terms=[]){const p=new Map();for(const[s,k,c]of terms){const key=s+","+k;p.set(key,(p.get(key)||new C()).add(c));}for(const[k,v]of p)if(v.zero())p.delete(k);return p;}
function plus(...ps){return poly(ps.flatMap(p=>[...p].map(([key,c])=>[...key.split(",").map(Number),c])));}
function times(p,q){const out=[];for(const[a,x]of p)for(const[b,y]of q){const[i,j]=a.split(",").map(Number),[n,k]=b.split(",").map(Number);out.push([i+n,j+k,x.mul(y)]);}return poly(out);}
function scale(p,c){return poly([...p].map(([key,x])=>[...key.split(",").map(Number),x.mul(c)]));}
function shift(p,n){return times(p,poly([[n,0,1]]));}
function ds(p){return poly([...p].map(([key,x])=>{const[n,k]=key.split(",").map(Number);return[n-1,k,x.mul(n)];}));}
function dt(p){return poly([...p].map(([key,x])=>{const[n,k]=key.split(",").map(Number);return[n,k,x.mul(new C(0,4*k))];}));}
function coeff(p,n){return poly([...p].filter(([key])=>Number(key.split(",")[0])===n).map(([key,x])=>[0,Number(key.split(",")[1]),x]));}
const one=poly([[0,0,1]]);
const sin=k=>poly([[0,k,new C(0,"-1/2")],[0,-k,new C(0,"1/2")]]);
const cos=k=>poly([[0,k,"1/2"],[0,-k,"1/2"]]);
function recordPoly(p){return [...p].sort((a,b)=>a[0].localeCompare(b[0])).map(([key,c])=>({s_power:Number(key.split(",")[0]),fourier_mode:Number(key.split(",")[1]),...c.record()}));}
function computeChecks(){
 const commonG1=plus(scale(one,"3/7"),scale(sin(1),"1/9"));
 const q=plus(sin(1),scale(cos(2),"1/3"),shift(scale(cos(1),"1/5"),2),shift(scale(sin(2),"1/11"),4));
 const krest=plus(shift(scale(cos(1),"1/7"),2),shift(scale(sin(2),"1/17"),4));
 const cases=[
  {name:"real trigonometric nonzero radial jets",G0:scale(one,"-1/32"),k0:scale(one,2),expect_constant:true},
  {name:"nonconstant leading factors with exactly constant product",G0:poly([[0,-1,"-1/16"]]),k0:poly([[0,1,1]]),expect_constant:true},
  {name:"nonconstant leading product keeps the logarithmic residual",G0:plus(scale(one,"-1/32"),scale(cos(2),"1/7")),k0:scale(one,2),expect_constant:false}
 ];
 const records=[];
 for(const row of cases)for(const sigma of[-1,1]){
  const G=plus(row.G0,shift(commonG1,2),shift(scale(cos(2),"1/13"),4),shift(scale(sin(3),"1/23"),6));
  const k=plus(row.k0,krest),q0=coeff(q,0);
  const B1=plus(scale(commonG1,-1),scale(dt(times(q0,row.G0)),"-2/3"));
  const B=plus(shift(scale(row.G0,"-1/3"),-3),shift(B1,-1));
  const v=plus(shift(scale(q,2),1),shift(scale(k,-2*sigma),2));
  const actual=plus(shift(G,-4),scale(ds(B),-1),scale(dt(times(v,B)),-1));
  const G2=shift(plus(G,scale(row.G0,-1),shift(scale(commonG1,-1),2)),-4);
  const q1=shift(plus(q,scale(q0,-1)),-2);
  const k1=shift(plus(k,scale(row.k0,-1)),-2);
  const regular=plus(G2,scale(dt(times(q1,row.G0)),"2/3"),
    shift(scale(dt(times(k1,row.G0)),Rat.p(-2*sigma).div(3)),1),
    scale(dt(times(q,B1)),-2),
    shift(scale(dt(times(k,B1)),2*sigma),1));
  const rootProductDerivative=dt(times(row.k0,row.G0));
  const expectedLog=shift(scale(rootProductDerivative,Rat.p(-2*sigma).div(3)),-1);
  const defect=plus(actual,scale(regular,-1),scale(expectedLog,-1));
  if(defect.size)throw Error("exact identity failure "+row.name);
  const finiteRoot=scale(rootProductDerivative,Rat.p(2*sigma).div(9));
  if(row.expect_constant&&(expectedLog.size||finiteRoot.size))throw Error("constant root product gate failed");
  if(!row.expect_constant&&(!expectedLog.size||!finiteRoot.size))throw Error("broken identity was not detected");
  if([...regular].some(([key])=>Number(key.split(",")[0])<0))throw Error("regular source has a negative power");
  records.push({name:row.name,sigma,all_identity_coefficients_exactly_zero:true,
    regular_monomials:regular.size,largest_s_power:Math.max(...[...regular].map(([key])=>Number(key.split(",")[0]))),
    true_root_product_constant:row.expect_constant,
    logarithmic_source:recordPoly(expectedLog),
    finite_lower_boundary_constant:recordPoly(finiteRoot)});
 }
 return {kind:"R106_exact_Laurent_counterterm_identity_checks",complete:true,
  arithmetic:"Gaussian rationals, reduced BigInt, complete signed Laurent convolutions",
  geometric_candidate_computed:false,root_disk_numerics_proved:false,
  cases:records,all_passed:records.length===6,
  proof:"results/R106-supplement-analytic-root-transport-counterterm.md"};
}

export {computeChecks};
if(process.argv[1]&&import.meta.url===pathToFileURL(process.argv[1]).href){const result=computeChecks();result.provenance={source:'scripts/fourfold_root_counterterm_identity_exact.mjs',source_sha256:crypto.createHash('sha256').update(fs.readFileSync(fileURLToPath(import.meta.url))).digest('hex'),execution:'Exact computeChecks; the finite six cases contain no sampled geometry.'};const out=JSON.stringify(result,null,2)+'\n';if(process.argv[2])fs.writeFileSync(process.argv[2],out);else process.stdout.write(out);}
