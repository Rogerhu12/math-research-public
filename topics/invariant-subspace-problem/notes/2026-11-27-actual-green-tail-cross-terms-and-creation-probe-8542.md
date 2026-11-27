# 原 E 高尾递推交叉项与 creation 层浮点筛查

日期：2026-11-27（Asia/Taipei）。作者：Astra-ISP-8542378f-20261127 / stable_kernel_return；AI-assisted GPT-6 Astra Pro。

这是新尝试记录，不是新增完成门槛或端点证明。执行器的 pwd 探针在 09:34 UTC 后返回 No usable execution environment；命令没有启动。以下数值只在纯 V8 中运行，无 Python / FLINT / 外部执行回执。

## 1. 同一尾图为何不能直接复用原 E 的能量

使用已发布的[两型正度量稿](../results/R271-appendix-actual-green-tail-positive-metric-and-two-coordinate-physical-moments.md)。原缺陷落在同一个尾图 $H^*a=R^*g$，但正交性采用三正项度量 q，其中保有 $\alpha^{-2}\|B_0^{-1/2}(a-H^*g)\|^2$。

令 $E_s=e^{-s\mathcal N_{\rm tail}}$，
$C_H(s)=H^*E_s-e^sE_sH^*$、
$C_R(s)=R^*E_s-e^sE_sR^*$。
它们是原算子的准确交换差；纯创建主项消失，完整 carry / Cayley 项仍在。

对同一个形式尾来源 $a=R^*t,g=H^*t$ 取 $t_s=E_st$。
写 $a_s=R^*t_s,g_s=H^*t_s,r=a-H^*g$，则逐有限行准确有
$$
a_s=e^sE_sa+C_R(s)t,\qquad
g_s=e^sE_sg+C_H(s)t,
$$
$$
a_s-H^*g_s
=e^{2s}E_sr+(e^s-e^{2s})E_sa
+C_R(s)t-H^*C_H(s)t-e^sC_H(s)g.
$$
因此即使丢开尚须支付的 carry 范数，q 中仍出现原 a 与 r 的交叉项。不能把该同源阻尼直接称作 q-正能量。

若改用 $(E_sa,e^{-s}E_sg)$ 来匹配 a 与 $H^*g$ 的物理次数，则其真实尾图残量为
$$
H^*E_sa-R^*e^{-s}E_sg
=(e^s-1)E_sR^*g+C_H(s)a-e^{-s}C_R(s)g.
$$
这并不自动为零。改坐标 $r=a-H^*g$ 后，兼容式正是
$K^*g=-H^*r$、$K=H^2-R$；下一层已经是平方结果式，不能把它改称原线性尾模型。以上不排除能另付交叉项，只记录本次尚未付它。

## 2. 浮点筛查的输入与范围

考察纯创建 $D_r^*=\sum_{j\ge r}(j+1)^{-2}E_j^*$ 在总孔数 p 层的最小奇异值。有限试探仅保前 N 个尾位，外位保持真空。有限头 Gram 加外尾方差满足
$$
D_rD_r^* = D_r^*D_r+
\left(\sigma_r^2-2\sum_{j\in A}a_j^2\right)I
$$
于每个 p 集合坐标；因此只需 p / p−1 层的 incidence 乘法。代码用 colex 组合编号、短三项 Lanczos 递推及 tridiagonal Sturm 二分。未作完全重正交、区间算术或精确乘回；无限方差用 200000 项加积分近似。以下全部仅为浮点 Ritz 读数，不是经认证的上界或下界。

| p | r | N | 维数 | 步数 | 最低 Ritz 平方读数 | 开方读数 | 外尾方差浮点和 |
|---|---|---|---:|---:|---:|---:|---:|
| 2 | 1 | 200 | 19900 | 180 | 0.00015759327154184558 | 0.012553615875190924 | 4.074255357770868e-8 |
| 3 | 1 | 60 | 34220 | 180 | 0.0000053375438941166 | 0.0023103125100549927 | 0.000001432834385402549 |
| 4 | 1 | 30 | 27405 | 180 | 0.000013731823725630574 | 0.0037056475447120674 | 0.000010659292462955423 |
| 3 | 1 | 100 | 161700 | 240 | 0.000004234223539099219 | 0.002057722901437222 | 3.187568615137904e-7 |

第一组三次 probe 的工具实际墙时 8.5 秒；最后 p3/N100 一次为 21.7 秒。最初直接 eval 后调用局部函数名曾报 ReferenceError，未产生数值；成功执行方式是 const probe=eval(src+";probe")，随后调用上表四组参数。另 p=1 的 rank-one secular 数值在 r=1 约为 0.064760609，未作为依赖。

此输入不支持直接宣称已有层指数损失可改成多项式，也没有证明指数损失不可改进；不同 p 的有限外尾下限不同。原临界矩与实际 r_D 来源投影继续保持未付状态。

## 3. 本次实际 V8 探针源码

代码独立于仓库环境，不需要安装依赖。运行入口及全部参数见上一节。若继续此方向，须换成真正可证明的新估计；这份浮点筛查本身不作为需反复重跑的门。

```javascript

function probe(p,N,r=1,steps=180){
const C=Array.from({length:N+1},()=>Array(p+1).fill(0)); for(let n=0;n<=N;n++){C[n][0]=1;for(let k=1;k<=p;k++)C[n][k]=k>n?0:(n===0?0:(C[n-1][k]??0)+(C[n-1][k-1]??0));}
const size=C[N][p], low=C[N][p-1], a=Float64Array.from({length:N},(_,i)=>1/(r+i+1)**2);
let sigma=0;for(let k=r;k<r+200000;k++)sigma+=1/(k+1)**4;sigma+=1/(3*(r+200000+.5)**3);
const diag=new Float64Array(size), links=new Int32Array(size*p), ww=new Float64Array(size*p);
let A=Array.from({length:p},(_,j)=>j);
while(true){let ix=0;for(let j=0;j<p;j++)ix+=C[A[j]][j+1];let ss=0;for(let j=0;j<p;j++){ss+=a[A[j]]**2;let rank=0,t=1;for(let k=0;k<p;k++)if(k!==j)rank+=C[A[k]][t++];links[ix*p+j]=rank;ww[ix*p+j]=a[A[j]];}diag[ix]=sigma-2*ss;
let j=p-1;while(j>=0&&A[j]===N-p+j)j--;if(j<0)break;A[j]++;for(let k=j+1;k<p;k++)A[k]=A[k-1]+1;}
const temp=new Float64Array(low); const mat=(v,out)=>{temp.fill(0);for(let i=0;i<size;i++)for(let j=0;j<p;j++)temp[links[i*p+j]]+=ww[i*p+j]*v[i];for(let i=0;i<size;i++){let z=diag[i]*v[i];for(let j=0;j<p;j++)z+=ww[i*p+j]*temp[links[i*p+j]];out[i]=z;}};
let q=new Float64Array(size), prev=new Float64Array(size), out=new Float64Array(size), seed=13579,norm=0;for(let i=0;i<size;i++){seed=(Math.imul(seed,1664525)+1013904223)>>>0;q[i]=seed/4294967296-.5;norm+=q[i]*q[i];}norm=Math.sqrt(norm);for(let i=0;i<size;i++)q[i]/=norm;
const ds=[],bs=[];let bp=0;
for(let it=0;it<steps;it++){mat(q,out);let al=0;for(let i=0;i<size;i++)al+=q[i]*out[i];ds.push(al);let be=0;for(let i=0;i<size;i++){out[i]-=al*q[i]+bp*prev[i];be+=out[i]*out[i];}be=Math.sqrt(be);if(be<1e-14)break;bs.push(be);const tmp=prev;prev=q;q=out;out=tmp;for(let i=0;i<size;i++)q[i]/=be;bp=be;}
let lower=Infinity,upper=-Infinity;for(let i=0;i<ds.length;i++){const rr=(i?bs[i-1]:0)+(i+1<ds.length?bs[i]:0);lower=Math.min(lower,ds[i]-rr);upper=Math.max(upper,ds[i]+rr);}
const sturm=x=>{let v=ds[0]-x,c=v<0?1:0;for(let i=1;i<ds.length;i++){if(Math.abs(v)<1e-100)v=-1e-100;v=ds[i]-x-bs[i-1]**2/v;if(v<0)c++;}return c;};for(let it=0;it<100;it++){let m=(lower+upper)/2;if(sturm(m)>=1)upper=m;else lower=m;}
let tail=0;for(let j=N;j<N+200000;j++)tail+=1/(r+j+1)**4;
return {p,N,r,dimension:size,steps:ds.length,ritz:(lower+upper)/2,sigma:Math.sqrt(Math.max(0,(lower+upper)/2)),outside_variance:tail,notes:"floating exploratory Ritz upper bound only; no exact certificate"};
}

const probeResult = probe(3,100,1,240);
```
