// Exact rational certificate. Execute with new Function(code + "\nreturn report;")().
// Coordinates are realified: original x_j=i^j y_j, W_(2,m)=i^m w_m, j=0,...,5.
const cases = [
  {
    "s": 5,
    "p": "32/5",
    "q": "8/5",
    "P": [
      "-8/5",
      "32/5",
      "-5",
      "1"
    ],
    "conics": [
      [
        "1512",
        "-9368",
        "4725",
        "13280",
        "-11320",
        "2075"
      ],
      [
        "127048",
        "-806992",
        "413625",
        "1178600",
        "-1013155",
        "186750"
      ]
    ],
    "resultant": [
      "1844968",
      "-8965304",
      "12107253",
      "-6107580",
      "990895"
    ],
    "resOverP": [
      "-1153105",
      "990895"
    ],
    "x": [
      "1",
      "230621/198179",
      "412768/198179",
      "904952/198179",
      "11260192/990895",
      "6128928/198179"
    ],
    "w": [
      "16101657680/39274916041",
      "21318672120/39274916041",
      "33195718080/39274916041",
      "55301741120/39274916041",
      "98165985280/39274916041",
      "190011932160/39274916041",
      "410280140800/39274916041",
      "992389914624/39274916041",
      "2640175763456/39274916041",
      "37530157944832/196374580205",
      "22220856922112/39274916041"
    ],
    "bellDiagonal": [
      "7071600681/39274916041",
      "-13205390519/39274916041",
      "-25954548736/39274916041",
      "-1622159296/39274916041",
      "-5216864295936/981872901025",
      "-6877955415040/39274916041"
    ]
  },
  {
    "s": -27,
    "p": "864/5",
    "q": "-864/5",
    "P": [
      "864/5",
      "864/5",
      "27",
      "1"
    ],
    "conics": [
      [
        "69589152",
        "123291072",
        "10243385",
        "54331840",
        "8793640",
        "310775"
      ],
      [
        "1728149472",
        "3072671712",
        "255091835",
        "1359453760",
        "220082465",
        "7780800"
      ]
    ],
    "resultant": [
      "38451050784",
      "63279413568",
      "30836339469",
      "4101949340",
      "143682655"
    ],
    "resOverP": [
      "222517655",
      "143682655"
    ],
    "x": [
      "1",
      "-44503531/28736531",
      "132810784/28736531",
      "-861353568/28736531",
      "975250368/3504455",
      "-90028238400/28736531"
    ],
    "w": [
      "683860887117640/825788213913961",
      "-22949602239620/22318600376053",
      "1138708823114240/825788213913961",
      "-2185722638778240/825788213913961",
      "8976203492106240/825788213913961",
      "-3233342470533120/43462537574419",
      "485309595928412160/825788213913961",
      "-4038737054248747008/825788213913961",
      "35800112287540887552/825788213913961",
      "-92781780780486868992/217312687872095",
      "4031045067765070872576/825788213913961"
    ],
    "bellDiagonal": [
      "-541933560321319/825788213913961",
      "-15623861829501/43462537574419",
      "-313702637517824/825788213913961",
      "-228689222750493696/825788213913961",
      "-10062325801021722624/1086563439360475",
      "42993573877092814848/825788213913961"
    ]
  }
];
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b)[a,b]=[b,a%b];return a||1n;}
function R(a,b=1n){if(b<0n){a=-a;b=-b;}const g=gcd(a,b);return[a/g,b/g];}
const Z=()=>R(0n),add=(a,b)=>R(a[0]*b[1]+b[0]*a[1],a[1]*b[1]),neg=a=>[-a[0],a[1]],sub=(a,b)=>add(a,neg(b)),mul=(a,b)=>R(a[0]*b[0],a[1]*b[1]),div=(a,b)=>R(a[0]*b[1],a[1]*b[0]);
const parse=s=>{const[a,b="1"]=s.split("/");return R(BigInt(a),BigInt(b));};
const show=a=>a[1]===1n?String(a[0]):a[0]+"/"+a[1];
const eq=(a,b)=>a[0]*b[1]===b[0]*a[1];
const K=[[0,0,0,0,5,-1],[0,0,0,-32,5,-1],[0,0,54,-4,5,0],[0,-32,-4,-8,0,0],[5,5,5,0,0,0],[-1,-1,0,0,0,0]].map(row=>row.map(x=>R(BigInt(x))));
const mv=(M,v)=>M.map(row=>row.reduce((s,a,j)=>add(s,mul(a,v[j])),Z()));
const mm=(A,B)=>A.map(row=>B[0].map((_,j)=>row.reduce((s,a,k)=>add(s,mul(a,B[k][j])),Z())));
const dot=(u,v)=>u.reduce((s,a,j)=>add(s,mul(a,v[j])),Z());
const tr=M=>M.reduce((s,row,i)=>add(s,row[i]),Z());
const zero=v=>v.every(a=>a[0]===0n);
const checks=cases.map(o=>{
const x=o.x.map(parse),w=o.w.map(parse),H=Array.from({length:6},(_,i)=>Array.from({length:6},(_,j)=>w[i+j]));
const kx=mv(K,x),F=div(dot(x,kx),R(2n)),KH=mm(K,H),KH2=mm(KH,KH);
const Q=add(sub(mul(F,F),mul(R(2n),dot(kx,mv(H,kx)))),mul(R(2n),tr(KH2)));
const gradX=mv(K,mv(H,kx)).map((a,i)=>sub(mul(R(2n),mul(F,kx[i])),mul(R(4n),a)));
const gradW=Array.from({length:11},(_,m)=>{
const Hm=Array.from({length:6},(_,i)=>Array.from({length:6},(_,j)=>R(i+j===m?1n:0n)));
return add(mul(R(-2n),dot(kx,mv(Hm,kx))),mul(R(4n),tr(mm(mm(mm(K,Hm),K),H))));
});
const C=x.map((a,i)=>x.map((b,j)=>sub(mul(a,b),mul(R(2n),H[i][j]))));
const bellDiagonal=C.map((row,i)=>row[i]);
const hn=sub(mul(x[0],x[2]),mul(x[1],x[1]));
const s=parse(String(o.s)),p=parse(o.p),q=parse(o.q);
const tripleRemainders=[
 add(add(neg(mul(s,s)),mul(R(4n),s)),sub(mul(R(5n),p),R(27n))),
 add(add(add(mul(mul(s,s),s),mul(R(-3n),mul(s,s))),mul(R(22n),s)),add(add(mul(R(-5n),mul(s,p)),neg(p)),mul(R(4n),q))),
 sub(add(add(add(add(mul(R(5n),mul(s,s)),neg(mul(p,mul(s,s)))),neg(mul(mul(s,s),s))),mul(R(6n),mul(s,p))),add(mul(R(-32n),p),mul(R(5n),mul(p,p)))),mul(add(mul(R(3n),s),R(5n)),q))
];
const result={s:o.s,F_zero:F[0]===0n,Q_zero:Q[0]===0n,all_6_x_derivatives_zero:zero(gradX),all_11_W_derivatives_zero:zero(gradW),not_on_RNC:hn[0]!==0n,isotropic_triple_remainders_zero:zero(tripleRemainders),all_coordinate_Bell_squares_nonzero:bellDiagonal.every(a=>a[0]!==0n),listed_diagonal_values_exact:bellDiagonal.every((a,i)=>eq(a,parse(o.bellDiagonal[i]))),bell_submatrix_0_1_5:[0,1,5].map(i=>[0,1,5].map(j=>show(C[i][j])))};
result.PASS=Object.entries(result).filter(([k,v])=>typeof v==="boolean").every(([k,v])=>v);
return result;
});
const report={all_pass:checks.every(c=>c.PASS),checks};

function pTrim(p){while(p.length>1&&!p.at(-1)[0])p.pop();return p;}
const pAdd=(a,b)=>pTrim(Array.from({length:Math.max(a.length,b.length)},(_,i)=>add(a[i]||Z(),b[i]||Z())));
const pNeg=a=>a.map(neg),pSub=(a,b)=>pAdd(a,pNeg(b));
function pMul(a,b){const c=Array.from({length:a.length+b.length-1},Z);a.forEach((u,i)=>b.forEach((v,j)=>c[i+j]=add(c[i+j],mul(u,v))));return pTrim(c);}
function pDiv(a,b){a=a.map(x=>[...x]);const q=Array.from({length:Math.max(1,a.length-b.length+1)},Z);while(a.length>=b.length&&a.some(x=>x[0])){const i=a.length-b.length,c=div(a.at(-1),b.at(-1));q[i]=c;for(let j=0;j<b.length;j++)a[i+j]=sub(a[i+j],mul(c,b[j]));pTrim(a);}return{q:pTrim(q),r:a};}
const pEval=(p,t)=>p.reduceRight((s,c)=>add(mul(s,t),c),Z());
const conics=[
[-279,-242,-65856,521,-46784,271360],
[-1769,2738,-16087680,-969,19820160,140341248]
].map(row=>row.map(n=>R(BigInt(n))));
const conicsExact=report.checks.every((o,k)=>{
const C=o.bell_submatrix_0_1_5.map(row=>row.map(parse));
const raw=[C[0][0],mul(R(2n),C[0][1]),mul(R(2n),C[0][2]),C[1][1],mul(R(2n),C[1][2]),C[2][2]];
const scale=div(raw[0],conics[k][0]);
return scale[0]!==0n&&raw.every((a,i)=>eq(a,mul(scale,conics[k][i])));
});
const deltaCubic=["52565262336","6080833024","-43931504","3725"].map(parse);
const numA=["-271360","46784","-521"].map(parse);
const den=["-112640","800"].map(parse);
const numB=pAdd(numA,pMul([R(0n),R(1n)],den));
function substituteConic(c){const terms=[pMul(numA,numA),pMul(numA,numB),pMul(numA,den),pMul(numB,numB),pMul(numB,den),pMul(den,den)];return terms.reduce((s,t,j)=>pAdd(s,t.map(a=>mul(c[j],a))),[Z()]);}
const remainders=conics.map(c=>pDiv(substituteConic(c),deltaCubic).r);
const intervals=[[-9,-8],[144,149],[11600,11700]];
const signs=intervals.map(([a,b])=>[pEval(deltaCubic,R(BigInt(a))),pEval(deltaCubic,R(BigInt(b)))]);
const signsOpposite=signs.every(([a,b])=>a[0]*b[0]<0n);
const denRoot=R(704n,5n),noDenRoot=pEval(deltaCubic,denRoot)[0]!==0n;
const candidateReport={node_conics_exact:conicsExact,candidate_conic_numerators_zero_mod_cubic:remainders.every(zero),cubic_three_disjoint_real_root_intervals:signsOpposite,denominator_nonzero_on_all_cubic_roots:noDenRoot,intervals,endpointValues:signs.map(row=>row.map(show)),conicRemainders:remainders.map(row=>row.map(show)),deltaCubic:deltaCubic.map(show),numA:numA.map(show),denominator:den.map(show),numB:numB.map(show),scope:"The candidate vanishes at the two explicitly checked extra critical points and on the RNC. No assertion of a complete critical-locus classification, Jacobian membership, or cyclicity of F^2."};
report.candidate=candidateReport;
report.all_pass=report.all_pass&&conicsExact&&remainders.every(zero)&&signsOpposite&&noDenRoot;

const integerRepresentatives=[
["990895","1153105","2063840","4524760","11260192","30644640"],
["143682655","-222517655","664053920","-4306767840","39985265088","-450141192000"]
].map(row=>row.map(parse));
const recurrenceChecks=cases.map((o,k)=>{
const x=o.x.map(parse),w=o.w.map(parse),s=parse(String(o.s)),p=parse(o.p),q=parse(o.q);
const valid=v=>v.every((a,i)=>i<3||eq(a,add(sub(mul(s,v[i-1]),mul(p,v[i-2])),mul(q,v[i-3]))));
const H=Array.from({length:6},(_,i)=>Array.from({length:6},(_,j)=>w[i+j]));
const ns=integerRepresentatives[k],coordinates=ns.every((a,i)=>eq(div(a,ns[0]),x[i]));
return {s:o.s,x_recurrence:valid(x),H_recurrence:valid(w),H_K_x_zero:zero(mv(H,mv(K,x))),integer_projective_coordinates_exact:coordinates};
});
report.recurrences=recurrenceChecks;
report.all_pass=report.all_pass&&recurrenceChecks.every(o=>Object.entries(o).filter(([k,v])=>typeof v==="boolean").every(([k,v])=>v));

if (typeof module !== "undefined") module.exports={report,cases};
if (typeof require !== "undefined" && require.main === module) console.log(JSON.stringify(report,null,2));
