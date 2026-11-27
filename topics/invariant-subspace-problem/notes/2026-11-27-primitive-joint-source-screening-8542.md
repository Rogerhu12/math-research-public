# 真实 primitive 联合来源：有限浮点筛查与两个文献接口的适用域

日期：2026-11-27（Asia/Taipei）。作者：Astra-ISP-8542378f-20261127 / stable_kernel_return；AI-assisted，GPT-6 Astra Pro。

**状态：探索记录。40 次有限浮点探针已在本会话 V8 中执行；没有区间算术、精确正性证书或一般比较常数。本文不关闭任何原 Schur 或同 $w$ 来源。**

## 1. 实际检查的有限矩阵

取原正权 Boolean 删除 $D=\sum_{i=0}^{n-1}b_i E_i$，物理第 $p$ 孔层 $H_p$。记
$$
U_{h,p}=\ker(D^h|_{H_p})\ominus\ker(D^{h-1}|_{H_p}),
\qquad p=s+h-1.
$$
代码由 $\operatorname{Ran}(D^h|_{H_p})^*$ 和
$\operatorname{Ran}(D^{h-1}|_{H_p})^*$ 的正交差构造该空间；没有以纯 primitive 压缩逆代替完整层。

随后形成原第一下降
$$
A_h=P_{U_{h-1,p-1}}D|_{U_{h,p}},\qquad
A_{h+1}=P_{U_{h,p}}D|_{U_{h+1,p+1}},
$$
并用 Jacobi 浮点对角化检查
$$
Q_{n,s,h}=\left(\frac h{h-1}\right)^2A_h^*A_h-A_{h+1}A_{h+1}^*.
$$
这是已知平方必要下界所对应的候选上界。下列输出没有证明它在任何连续参数区间中为正。

固定输入为依次执行的五组 $(n,s,h)$：
$(5,1,2),(6,1,3),(7,2,2),(8,2,3),(8,3,2)$，每组 8 次。
唯一伪随机状态初值为 $159221$；每个权依次用
$$
r\leftarrow(1664525r+1013904223)\bmod2^{32},\qquad
b_i=\exp(-3r/2^{32}).
$$
组与组之间不重置状态。所有输入可由这两个整数及固定组序重建。

表中第三列是构造出的中间空间维数；后两列分别是浮点最小特征值
$\lambda_{\min}(Q_{n,s,h})$ 与 $\lambda_{\min}(A_h^*A_h)$。

| 序号 | $n,s,h$ | 维数 | 候选差的最小特征值 | 分母 Gram 的最小特征值 |
|---:|:---:|---:|---:|---:|
| 1 | 5, 1, 2 | 4 | 0.05486700769452820 | 0.02026381495479390 |
| 2 | 5, 1, 2 | 4 | 0.1530417203517380 | 0.05358366163943275 |
| 3 | 5, 1, 2 | 4 | 0.6027947482704036 | 0.2256351583521967 |
| 4 | 5, 1, 2 | 4 | 0.1928220453173331 | 0.06804150741360043 |
| 5 | 5, 1, 2 | 4 | 0.1895023499735140 | 0.06150557792643750 |
| 6 | 5, 1, 2 | 4 | 1.266696475567920 | 0.3825425000094141 |
| 7 | 5, 1, 2 | 4 | 0.06431073094391632 | 0.02323744528247148 |
| 8 | 5, 1, 2 | 4 | 1.023851283871713 | 0.3017220202757143 |
| 9 | 6, 1, 3 | 5 | 0.2525911483072834 | 0.1610531272631978 |
| 10 | 6, 1, 3 | 5 | 0.08686870581435538 | 0.05795025515744386 |
| 11 | 6, 1, 3 | 5 | 0.1368079360303175 | 0.08313542625281156 |
| 12 | 6, 1, 3 | 5 | 1.067354791702314 | 0.7022414929899189 |
| 13 | 6, 1, 3 | 5 | 0.02971099505636696 | 0.02364656686764055 |
| 14 | 6, 1, 3 | 5 | 0.2242832716042774 | 0.1513505106545900 |
| 15 | 6, 1, 3 | 5 | 0.2161467037480803 | 0.1355911306548374 |
| 16 | 6, 1, 3 | 5 | 0.06983366200436519 | 0.05273182389476878 |
| 17 | 7, 2, 2 | 14 | 0.06810572913903777 | 0.02736081845241711 |
| 18 | 7, 2, 2 | 14 | 0.02967177457786196 | 0.01167284408901450 |
| 19 | 7, 2, 2 | 14 | 0.04274589826464967 | 0.01574462625980335 |
| 20 | 7, 2, 2 | 14 | 0.1746123026612214 | 0.05894171554285987 |
| 21 | 7, 2, 2 | 14 | 0.06178329408109526 | 0.02639933841465115 |
| 22 | 7, 2, 2 | 14 | 0.03138955980751416 | 0.01182409609916351 |
| 23 | 7, 2, 2 | 14 | 0.05802942991848632 | 0.02215363763799397 |
| 24 | 7, 2, 2 | 14 | 0.06175050076798412 | 0.02455127612011892 |
| 25 | 8, 2, 3 | 20 | 0.08041463206601489 | 0.06263176387230497 |
| 26 | 8, 2, 3 | 20 | 0.02677341718764235 | 0.02237750169139215 |
| 27 | 8, 2, 3 | 20 | 0.1748064622743013 | 0.1060398295567495 |
| 28 | 8, 2, 3 | 20 | 0.1579218413358046 | 0.1068924382982391 |
| 29 | 8, 2, 3 | 20 | 0.1009719973154292 | 0.07487706362411616 |
| 30 | 8, 2, 3 | 20 | 0.1924122610442787 | 0.1347417663861479 |
| 31 | 8, 2, 3 | 20 | 0.03364197261884502 | 0.02720389847405429 |
| 32 | 8, 2, 3 | 20 | 0.1002651157361996 | 0.07361502856284917 |
| 33 | 8, 3, 2 | 28 | 0.01551508165110481 | 0.005666582192807895 |
| 34 | 8, 3, 2 | 28 | 0.04748963305501037 | 0.01402087757734009 |
| 35 | 8, 3, 2 | 28 | 0.05901214063619536 | 0.02184162470354438 |
| 36 | 8, 3, 2 | 28 | 0.03370806037907991 | 0.01109522702829916 |
| 37 | 8, 3, 2 | 28 | 0.007784682526819756 | 0.002964536378218727 |
| 38 | 8, 3, 2 | 28 | 0.009592029125542663 | 0.003639795599029557 |
| 39 | 8, 3, 2 | 28 | 0.01211719268317464 | 0.004536521872325385 |
| 40 | 8, 3, 2 | 28 | 0.01014284695217289 | 0.003791606565579033 |

所有 40 个浮点输出为正。最小候选差为
$0.0077846825268197565$，出现在第 37 次输入。
这不是认证下界：正交化秩阈值、累计舍入及 Jacobi 终止误差没有得到严格控制。较早一次展示用的排序比较函数写错，只影响展示顺序；本文按原执行顺序列出原存储值，不使用该排序。

## 2. 完整无依赖 JavaScript 复现源码

以下函数返回记录数组。它保留原实现的两遍正交化、秩阈值 $10^{-22}$ 与 Jacobi 阈值 $10^{-13}$；这些阈值是算法选择，不是数学证书。输出可用 JavaScript 的 JSON 序列化查看。

```javascript
function runPrimitiveProbe() {

function pc(x){let n=0;while(x){x&=x-1;n++;}return n;}
function masks(n,p){const a=[];for(let x=0;x<(1<<n);x++)if(pc(x)===p)a.push(x);return a;}
function deriv(b,p,k){const n=b.length,cols=masks(n,p),rows=masks(n,p-k),fac=Array.from({length:k},(_,i)=>i+1).reduce((a,c)=>a*c,1);return rows.map(j=>cols.map(i=>{if((i&j)!==j)return 0;let d=i^j,v=fac;for(let t=0;t<n;t++)if(d&(1<<t))v*=b[t];return v;}));}
function dot(a,b){let z=0;for(let i=0;i<a.length;i++)z+=a[i]*b[i];return z;}
function basis(rows,initial=[]){const q=initial.map(a=>a.slice()),fresh=[];let rem=rows.map(a=>a.slice());while(rem.length){let best=-1,bn=0,bv;for(let i=0;i<rem.length;i++){let v=rem[i].slice();for(let rep=0;rep<2;rep++)for(const r of q){const a=dot(v,r);for(let j=0;j<v.length;j++)v[j]-=a*r[j];}const nn=dot(v,v);if(nn>bn){bn=nn;best=i;bv=v;}}if(bn<1e-22)break;for(let j=0;j<bv.length;j++)bv[j]/=Math.sqrt(bn);q.push(bv);fresh.push(bv);rem.splice(best,1);}return fresh;}
function uh(b,p,h){const older=basis(deriv(b,p,h));return basis(deriv(b,p,h-1),older);}
function mul(A,x){return A.map(a=>dot(a,x));}
function adjBlock(b,p,h){const old=uh(b,p-1,h-1),cur=uh(b,p,h),D=deriv(b,p,1);return {old,cur,A:old.map(r=>cur.map(c=>dot(r,mul(D,c))))};}
function symEig(A){A=A.map(r=>r.slice());const n=A.length;for(let st=0;st<100*n*n;st++){let p=0,q=1,v=0;for(let i=0;i<n;i++)for(let j=i+1;j<n;j++)if(Math.abs(A[i][j])>v){v=Math.abs(A[i][j]);p=i;q=j;}if(v<1e-13)break;const th=0.5*Math.atan2(2*A[p][q],A[q][q]-A[p][p]),c=Math.cos(th),s=Math.sin(th),app=A[p][p],aqq=A[q][q],apq=A[p][q];A[p][p]=c*c*app-2*s*c*apq+s*s*aqq;A[q][q]=s*s*app+2*s*c*apq+c*c*aqq;A[p][q]=A[q][p]=0;for(let k=0;k<n;k++)if(k!==p&&k!==q){let a=A[k][p],d=A[k][q];A[k][p]=A[p][k]=c*a-s*d;A[k][q]=A[q][k]=s*a+c*d;}}return A.map((r,i)=>r[i]).sort((a,b)=>a-b);}
function test(b,s,h,C){const p=s+h-1,z=adjBlock(b,p,h),w=adjBlock(b,p+1,h+1);const gram=z.cur.map((_,i)=>z.cur.map((_,j)=>z.A.reduce((a,r)=>a+r[i]*r[j],0)));const cross=z.cur.map(c=>w.cur.map(d=>dot(c,mul(deriv(b,p+1,1),d))));const N=cross.map(a=>cross.map(b=>dot(a,b)));const diff=gram.map((r,i)=>r.map((x,j)=>C*x-N[i][j]));return{n:b.length,s,h,dim:z.cur.length,min:symEig(diff)[0],denmin:symEig(gram)[0],weights:b};}
let seed=159221;
function random01(){
  seed=(Math.imul(1664525,seed)+1013904223)>>>0;
  return seed/4294967296;
}
const out=[];
for(const [n,s,h] of [[5,1,2],[6,1,3],[7,2,2],[8,2,3],[8,3,2]]){
  for(let trial=0;trial<8;trial++){
    const b=Array.from({length:n},()=>Math.exp(-3*random01()));
    out.push(test(b,s,h,(h/(h-1))**2));
  }
}
return out;
}
```

## 3. 联合硬核问题仍保持原形式

回读 [完整硬核纤维笔记](2026-11-14-bosonic-hardcore-first-edge-789f-next.md) 后，首边的准确未付项仍是
$$
\Gamma_1=I+L_s^*L_s,\qquad
\Gamma_2=2I+4L_s^*L_s+M_s^*M_s,
$$
$$
M_s^*M_s\succeq(L_s^*L_s)^2-2L_s^*L_s-I.
$$
$M_s$ 是该笔记式 (3.4)–(3.7) 中同时包含下一 primitive 自由量与零模式修正的**一次联合 MP**。本文没有将它们分开优化。旧笔记已排除单模式玻色嵌入、抽象 HL/HR 和单独 $\mathsf K$ 逆度量行估计的自动推论；此处只引用这些已登记边界。

## 4. 本轮读到的文献不能直接替代原来源费用

### 4.1 层依赖 Markov 度量

Anari–Liu–Oveis Gharan–Vinzant，
[Log-Concave Polynomials II, arXiv:1811.01816v3](https://arxiv.org/html/1811.01816v3)，
Theorem 1.1 给齐次强对数凹分布所定义的 down-up Markov 链谱界。
该链使用各层的概率权与转移归一化。本文没有证明其度量与上述未归一的完整 MP、固定 primitive 来源相同，也没有得到可用于原两形式来源的比较常数。故该定理没有被计作原首边证明。

### 4.2 原 ruler 权不是任意正参数的 $\epsilon$-star-shaped 权

Thomas，
[Closed ideals in the Banach algebra $\ell^1(\omega)$ when $\omega$ is $\epsilon$-star shaped](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/38EA008451377E4B25BFF3EE98CF432C/S0013091500019489a.pdf/div-class-title-closed-ideals-in-the-banach-algebra-span-class-sup-1-span-when-is-star-shaped-div.pdf)，
Proc. Edinburgh Math. Soc. 41 (1998), 161–176，
Definition 1.4 的条件为：对全部 $m<n$，
$$
\omega(n)^{1-\epsilon(n-m)/n}\le\omega(m),\qquad 0<\epsilon\le1.
$$
原边界权
$$
\beta_n=\prod_{\nu=1}^n\alpha_{v_2(\nu)}
$$
在 $m=2^j,\ n=2^j+1$ 满足 $\beta_n/\beta_m=\alpha_0=e^{-20}$。
因此这个条件会要求
$$
20\ge\epsilon\,\frac{-\log\beta_{2^j+1}}{2^j+1}.
$$
原四次幂下降界 $-\log\beta_n\ge(95/32)n^4$（已在实际方向交织稿中登记）使右边对固定 $\epsilon>0$ 趋无穷，矛盾。故不能把该文的闭理想结论套到原权。本文也没有以另外的等价或更大 Banach 代数的闭包替换原 Hilbert 闭包。

## 5. 仍在推进的实际目标

本轮没有得到一般首边、全部高度统一常数或同 $w$ 的源费用上界。后续仍须控制完整联合项，或只对原实际两形式来源证明足以在合法母窗内求和的估计；不能把本表的正浮点输出、文献中的另一种层度量或闭包值域视为这一步已经完成。
