
const cData=[[5,1,0,"8"],[5,0,0,"-8"],[4,2,1,"-4"],[4,1,1,"20"],[4,1,0,"-24"],[4,0,0,"16"],[3,2,2,"-16"],[3,2,1,"20"],[3,2,0,"2"],[3,1,1,"-32"],[3,1,0,"16"],[3,0,0,"-8"],[2,3,1,"-2"],[2,2,2,"24"],[2,2,1,"-14"],[2,2,0,"-4"],[2,1,1,"12"],[1,3,3,"-4"],[1,3,1,"4"],[1,2,2,"-10"],[1,2,1,"2"],[0,4,3,"1"],[0,4,2,"-1"],[0,3,3,"3"],[0,3,2,"-1"]];
const gData=[[5,1,0,"8"],[5,0,0,"-8"],[4,1,1,"20"],[4,1,0,"-24"],[4,0,0,"16"],[3,2,2,"-16"],[3,2,1,"12"],[3,2,0,"2"],[3,1,1,"-32"],[3,1,0,"16"],[3,0,0,"-8"],[2,2,2,"24"],[2,2,1,"-10"],[2,2,0,"-4"],[2,1,1,"12"],[1,3,3,"-4"],[1,3,1,"2"],[1,2,2,"-10"],[1,2,1,"2"],[0,3,3,"3"],[0,3,2,"-1"]];
function from(a){return new Map(a.map(([i,j,k,v])=>[[i,j,k].join(","),BigInt(v)]));}
function add(a,b,scale=1n){const z=new Map(a);for(const[k,v]of b){const w=(z.get(k)||0n)+scale*v;if(w)z.set(k,w);else z.delete(k);}return z;}
function mul(a,b){const z=new Map();for(const[ka,va]of a)for(const[kb,vb]of b){const aa=ka.split(",").map(Number),bb=kb.split(",").map(Number),k=aa.map((v,i)=>v+bb[i]).join(",");const w=(z.get(k)||0n)+va*vb;if(w)z.set(k,w);else z.delete(k);}return z;}
const T0=from([[1,0,0,"2"],[2,0,0,"-2"],[0,1,1,"-1"]]);
const JminusQ=from([[1,0,0,"2"],[2,0,0,"-2"],[0,1,1,"1"],[0,1,0,"-1"]]);
const expected=mul(from([[0,2,1,"-1"]]),mul(T0,JminusQ));
const actual=add(from(cData),from(gData),-1n);
if(add(actual,expected,-1n).size)throw Error("exact global polynomial identity failed");
return {schema:"isp-general-head-c-minus-g-integer-unit-identity-v1",inputPrimitiveC_SHA256:"18b4fd473f7a525b6f306d74f73acbff57a7d04bd630d2bc8eb2bd05402af238",inputPrimitiveG_SHA256:"291f6ddfe3fa39774a49878db6541c41d7b051f83d33363da0d23e7a31c46aad",bothNumeratorContents:"1/2",identity:"primitiveC-primitiveG=-Q^2*ell*T0*(J-Q)",rationalNumeratorIdentity:"c_n-g_n=-(1/2)*Q^2*ell*T0*(J-Q)",integerTerms:actual.size,allIntegerCoefficientProductsExact:true,parameterUnitsPreviouslyProved:true,ordinaryISPClaim:false};
