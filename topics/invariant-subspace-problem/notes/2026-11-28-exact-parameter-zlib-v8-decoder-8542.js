return function decodeZlib64(s){
 const alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
 let bytes=[],val=0,bits=0;for(const ch of s){if(ch==="=")break;let n=alphabet.indexOf(ch);if(n<0)continue;val=(val<<6)|n;bits+=6;if(bits>=8){bits-=8;bytes.push((val>>bits)&255);}}
 if(((bytes[0]<<8)|bytes[1])%31!==0||(bytes[0]&15)!==8||(bytes[1]&32))throw Error("zlib header");
 let ip=2,buf=0,nb=0,out=[];
 function get(n){while(nb<n){buf|=bytes[ip++]<<nb;nb+=8;}let v=buf&((1<<n)-1);buf>>>=n;nb-=n;return v;}
 function huff(lengths){
  const count=Array(16).fill(0);for(const l of lengths)if(l)count[l]++;
  const next=Array(16).fill(0);let code=0;
  for(let l=1;l<=15;l++){code=(code+count[l-1])<<1;next[l]=code;}
  const map=Array.from({length:16},()=>new Map());
  for(let sym=0;sym<lengths.length;sym++){let l=lengths[sym];if(!l)continue;let v=next[l]++,rev=0;for(let j=0;j<l;j++){rev=(rev<<1)|(v&1);v>>>=1;}map[l].set(rev,sym);}
  return function(){let v=0;for(let l=1;l<=15;l++){v|=get(1)<<(l-1);if(map[l].has(v))return map[l].get(v);}throw Error("bad Huffman");};
 }
 const lb=[3,4,5,6,7,8,9,10,11,13,15,17,19,23,27,31,35,43,51,59,67,83,99,115,131,163,195,227,258];
 const le=[0,0,0,0,0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,0];
 const db=[1,2,3,4,5,7,9,13,17,25,33,49,65,97,129,193,257,385,513,769,1025,1537,2049,3073,4097,6145,8193,12289,16385,24577];
 const de=[0,0,0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13];
 let final=0;
 while(!final){
  final=get(1);const type=get(2);
  if(type===0){buf=0;nb=0;let n=bytes[ip++]|(bytes[ip++]<<8),m=bytes[ip++]|(bytes[ip++]<<8);if((n^m)!==65535)throw Error("stored length");for(let i=0;i<n;i++)out.push(bytes[ip++]);continue;}
  let ls,ds;
  if(type===1){ls=Array.from({length:288},(_,i)=>i<144?8:i<256?9:i<280?7:8);ds=Array(32).fill(5);}
  else if(type===2){
   const nl=get(5)+257,nd=get(5)+1,nc=get(4)+4;
   const order=[16,17,18,0,8,7,9,6,10,5,11,4,12,3,13,2,14,1,15],cl=Array(19).fill(0);
   for(let i=0;i<nc;i++)cl[order[i]]=get(3);
   const read=huff(cl),all=[];
   while(all.length<nl+nd){let c=read();if(c<16)all.push(c);else{let n,v;if(c===16){n=get(2)+3;v=all.at(-1);if(v===undefined)throw Error("repeat");}else if(c===17){n=get(3)+3;v=0;}else{n=get(7)+11;v=0;}for(let i=0;i<n;i++)all.push(v);}}
   if(all.length!==nl+nd)throw Error("length overflow");ls=all.slice(0,nl);ds=all.slice(nl);
  }else throw Error("reserved block");
  const rl=huff(ls),rd=huff(ds);
  while(true){const c=rl();if(c<256){out.push(c);continue;}if(c===256)break;let j=c-257;if(j>=lb.length)throw Error("bad length");const n=lb[j]+get(le[j]),k=rd();if(k>=db.length)throw Error("bad distance");const d=db[k]+get(de[k]);if(d>out.length)throw Error("distance");for(let t=0;t<n;t++)out.push(out[out.length-d]);}
 }
 let a=1,b=0;for(const v of out){a=(a+v)%65521;b=(b+a)%65521;}
 const off=bytes.length-4,check=((bytes[off]<<24)|(bytes[off+1]<<16)|(bytes[off+2]<<8)|bytes[off+3])>>>0;
 if((((b<<16)|a)>>>0)!==check)throw Error("Adler checksum");
 let text="";for(let i=0;i<out.length;i+=8192)text+=String.fromCharCode(...out.slice(i,i+8192));return text;
};