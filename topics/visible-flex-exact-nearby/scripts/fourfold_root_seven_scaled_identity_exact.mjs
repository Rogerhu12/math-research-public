#!/usr/bin/env node
// Exact algebra only; actual root fields and native FFT are separate executions.
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

function scaledChecks(){
 const G0=scale(one,"-1/32"),k0=scale(one,2);
 const G=plus(G0,shift(plus(scale(one,"1/7"),scale(cos(1),"2/11")),2),
               shift(scale(cos(2),"1/13"),4),shift(scale(cos(1),"3/17"),6));
 const q=plus(scale(sin(1),"2/5"),shift(scale(sin(2),"1/7"),2),
               shift(scale(sin(1),"1/19"),4));
 const k=plus(k0,shift(scale(cos(1),"1/11"),2),shift(scale(cos(2),"1/23"),4));
 const S=plus(scale(sin(1),"1/29"),shift(scale(sin(2),"1/31"),2),
               shift(scale(sin(3),"1/37"),4));
 const rec=[];
 for(const dd of ["1","1/1024","3/8192"])for(const sigma of [-1,1]){
  const d=Rat.p(dd),rinv=Rat.p(1).div(d);
  const rows=p=>Array.from({length:4},(_,n)=>scale(coeff(p,2*n),d.pow(n)));
  const Gw=rows(G),qw=rows(q),kw=rows(k),Sw=rows(S);
  const B1=plus(scale(Gw[1],rinv.mul(-1)),scale(dt(times(qw[0],Gw[0])),"-2/3"));
  const B=plus(shift(scale(Gw[0],"-1/3"),-3),shift(B1,-1));
  const v=plus(shift(scale(q,2),1),shift(scale(k,-2*sigma),2));
  const independent=plus(shift(G,-4),scale(ds(B),-1),
     scale(dt(times(v,B)),-1),dt(S));
  let predicted=poly(),wrongScale=poly();
  const row=(a,n)=>a[n]||poly();
  for(let n=0;n<4;n++){
   const even=plus(scale(row(Gw,n+2),rinv.pow(2)),
      scale(dt(times(row(qw,n+1),Gw[0])),rinv.mul("2/3")),
      scale(dt(times(row(qw,n),B1)),-2),dt(row(Sw,n)));
   const odd=plus(scale(dt(times(row(kw,n+1),Gw[0])),rinv.mul(Rat.p(-2*sigma).div(3))),
      scale(dt(times(row(kw,n),B1)),2*sigma));
   predicted=plus(predicted,shift(scale(even,rinv.pow(n)),2*n),
                              shift(scale(odd,rinv.pow(n)),2*n+1));
   const wrongEven=plus(row(Gw,n+2),
      scale(dt(times(row(qw,n+1),Gw[0])),rinv.mul("2/3")),
      scale(dt(times(row(qw,n),B1)),-2),dt(row(Sw,n)));
   wrongScale=plus(wrongScale,shift(scale(wrongEven,rinv.pow(n)),2*n),
                               shift(scale(odd,rinv.pow(n)),2*n+1));
  }
  const error=plus(independent,scale(predicted,-1));
  if(error.size)throw Error("full seven-field scaled density identity failed");
  if(dd!=="1"&&!plus(independent,scale(wrongScale,-1)).size)
    throw Error("missing radial scale factor was not detected");
  rec.push({radial_scale:dd,sigma,all_coefficients_exactly_equal:true,
    physical_theta_multiplier:4,monomials:predicted.size,
    largest_physical_theta_mode:Math.max(...[...predicted.keys()].map(x=>Math.abs(Number(x.split(",")[1])))),
    missing_scale_factor_detected:dd==="1"?null:true});
 }
 const freeCut=Rat.p("-1/16").mul("-1/3").sub(Rat.p("1/2").div(4));
 if(!freeCut.eq("-5/48"))throw Error("complete free Tricomi cut normalization failed");
 return {kind:"R106_exact_scaled_seven_field_counterterm_checks",complete:true,
  arithmetic:"exact reduced Gaussian rationals in V8 BigInt",
  cases:rec,free_Tricomi_complete_cut_sminus3:freeCut.str(),
  actual_geometry_computed:false,native_FFT_executed:false,
  all_passed:true};
}

export {scaledChecks};
if(process.argv[1]&&import.meta.url===pathToFileURL(process.argv[1]).href){const out=scaledChecks();out.provenance={source:'scripts/fourfold_root_seven_scaled_identity_exact.mjs',source_sha256:crypto.createHash('sha256').update(fs.readFileSync(fileURLToPath(import.meta.url))).digest('hex')};const text=JSON.stringify(out,null,2)+'\n';if(process.argv[2])fs.writeFileSync(process.argv[2],text);else process.stdout.write(text);}
