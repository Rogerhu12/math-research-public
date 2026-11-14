# R133 续篇：未加权全频帽核与实际小非线性驱动图

2026-11-13，visible-exact-astra-ac0d / newton_source。

本篇闭合一个实际非线性边值问题：对同一真正旋转目标，在
$I=[3/2,25/8]$ 上保留全部物理 Fourier 模和两个 mean，以四个独立
端口给出唯一小 Codazzi 解。原生区间计算覆盖 whole $\eta$、全部
primitive 尾和663个闭径向盒；它不使用有限 Fourier 求解器的成功
标记来证明存在。

本篇没有把右端线性 regular 坐标 $d_R$ 置零称为真正 nonlinear
regular 条件。右端两个 mean、外尾匹配、内侧 body 匹配及周期
frame/position 的 holonomy 均仍是须联立的真实端口。下面得到的是
完整非线性驱动解图；尚不是闭曲面，也不是 README 的最终完成。

## 1. 目标身份、全部模式和范数

沿用 R133 的实际旋转参考
$g_0=E(r)dr^2+a(r)^2d\theta^2$，其第二基本形式为 $(A_0,0,C_0)$。
记
$$
\gamma=\sqrt E/a>0,\qquad \beta=a'/a,\qquad
\ell=A_0/C_0=K/C_0^2>0,\qquad C_0<0.                 \tag{U.1}
$$
目标对象仍为
`type_fixed_step02_d5_exact_affine_step5_object.json`，SHA256
`91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848`；
$$
\delta=-7789843107295549/4611686018427387904+\eta,
\qquad |\eta|\le10^{-9}.
$$
所有数值门都对这一完整区间成立。

另一个浮点 producer 考察的明确新度量是
$E_\nu=E\exp(\nu h)$，其中
$$
h=4096t^6(1-t)^6,\qquad t=(|r|-1/20)/(13/100)
$$
仅在 $0<t<1$ 非零。因而在本篇整个 $I$ 上，**任意该 $\nu$ 的
$g_\nu$ 都准确等于 $g_0$**，不是近似相等。这个事实只允许复用本篇
外帽；它没有将旧 $g_0$ 的 core/waist 证书移给变化后的条带。

令 $C=C_0+c$，保留 $B$ 的完整 mean。使用物理频率 $m\in4\mathbb Z$
以及通常的复 Fourier 系数。对 $m\ne0$ 定义
$$
b_m=i\operatorname{sgn}(m)\widehat B_m,\qquad
c_m=\widehat c_m,\qquad M=|m|.
$$
这个单位模变换保范数并保持实值共轭条件。零模仍是实际的
$B_0$ 和 $c_0$，不通过此变换删除。

本篇使用有乘法性质的**非齐次**范数
$$
\|f\|_{\mathcal X_s}
=\sum_{m\in4\mathbb Z}(1+|m|)^s\sup_{r\in I}|\widehat f_m(r)|,
\qquad
\|(B,c)\|_s=\|B\|_{\mathcal X_s}+\|c\|_{\mathcal X_s},
\quad s\ge0.                                                   \tag{U.2}
$$
先对每模取径向 supremum，再求和。端口的 $A_s$ 是同样权重的
圆周 Wiener 范数。$1+|m+n|\le(1+|m|)(1+|n|)$ 给出
$\|fg\|_{\mathcal X_s}\le\|f\|_{\mathcal X_s}\|g\|_{\mathcal X_s}$。
本篇实际消费取 $s=2$；不会把齐次 $M^2$ 的常数冒用为 $(1+M)^2$。

## 2. 真正 regular Jacobi 线及逐后缀全频门

令 $q_M$ 是 R133 从真正 R74 regular 入口回传的完整比值，满足
$$
q_M'=M\gamma(q_M^2-\ell)+\beta(\ell-1)q_M.           \tag{U.3}
$$
所有非第四模的实际尾 fee 原样保留。证明及计算都没有用某个
稳定中心代替这条真线。

在向内方向 $t=R-r$，将向量场除以正数 $M\gamma$，得
$$
\frac{q_t}{M\gamma}=\ell+\zeta q-q^2,\qquad
\zeta=-\frac{\beta(\ell-1)}{M\gamma}
\in\operatorname{hull}\!\left(0,-\frac{\beta(\ell-1)}{4\gamma}\right).
                                                               \tag{U.4}
$$
每个实际闭盒上，以 $\ell_\pm,\zeta_\pm$ 定义两个正比较根
$$
r_-={2\ell_-\over\sqrt{\zeta_-^2+4\ell_-}-\zeta_-},\qquad
r_+={\zeta_++\sqrt{\zeta_+^2+4\ell_+}\over2}.       \tag{U.5}
$$
对第 $i$ 个盒，取真实入口区间及从 $i$ 到 $R$ 所有盒的比较根
的 hull，再将下、上端分别乘 $1-2^{-128}$、$1+2^{-128}$。
得到 $q_{-,i},q_{+,i}$。向内逐盒归纳可用，因为下一后缀的区间
包含在当前后缀区间内；每盒的两个向内边界严格符号均以 Arb
单独核过。于是同时覆盖所有 $M\ge4$，而不是只覆盖表中有限低模。

由此定义逐盒下界
$$
\begin{split}
\sigma_{D,i}&=\gamma_-q_{-,i}
 +\tfrac14\min(0,\inf(-2\beta)),\\
\sigma_{C,i}&=\gamma_-q_{-,i}
 +\tfrac14\min(0,\inf[\beta(\ell+1)]).
\end{split}                                                     \tag{U.6}
$$
原生报告保留全部局部根、严格边界 margin 和这两条下界。
在 $[3/2,25/8]$，实际有
$$
\sigma_D>4.66079943,\qquad \sigma_C>2.10306552,
\qquad q_M<1.05975182.                                          \tag{U.7}
$$
这一步仅在明确通过的后缀使用。将同一粗门推广到整个
$[.239,25/8]$ 的一次 native 检查有39个 $\sigma_C$ 非正盒，位于
中间较宽的正帽比较区；拒绝原样保留，不据此宣称实际算子有坏谱。

## 3. 未加权的两条准确三角方程

对完整强制 Jacobi 系统，令 $d_m=b_m+q_Mc_m$。R133 的消去给
$$
\begin{split}
d_m'&=\mu_{D,M}d_m+f_{b,m}+q_M f_{c,m},
&\mu_{D,M}&=M\gamma q_M-2\beta,\\
c_m'&=-\mu_{C,M}c_m+M\gamma d_m+f_{c,m},
&\mu_{C,M}&=M\gamma q_M+\beta(\ell+1).
\end{split}                                                     \tag{U.8}
$$
在本篇区间，$\mu_{D,M}\ge M\sigma_D>0$、
$\mu_{C,M}\ge M\sigma_C>0$。定义
$$
K_D(r,t)=\exp\!\left(-\int_r^t\mu_{D,M}\right)\ (r\le t),\quad
K_C(t,r)=\exp\!\left(-\int_t^r\mu_{C,M}\right)\ (t\le r).
$$
给定两个非零模端口 $d_m(R)=d_{R,m}$、$c_m(L)=c_{L,m}$，准确解为
$$
\begin{split}
d_m(r)&=K_D(r,R)d_{R,m}
 -\int_r^R K_D(r,t)[f_{b,m}+q_Mf_{c,m}](t)\,dt,\\
c_m(r)&=K_C(L,r)c_{L,m}
 +\int_L^r K_C(t,r)[M\gamma d_m+f_{c,m}](t)\,dt.
\end{split}                                                     \tag{U.9}
$$
右端驱动积分的负号保留。这里未乘 $a^2$，也无需在终点再付
$a(R)^{-2}$。一般源由 $A_{s-1}$ 到 $A_s$ 的非零模增益分别可取
$5/(4\sigma_D)$、$5/(4\sigma_C)$；因本篇用非齐次权，明确支付
$(1+M)/M\le5/4$。

设
$$
T=\sup_{i}{\gamma_{+,i}\over\sigma_{C,i}},\quad
K_D^N=\sup_i {\gamma_{+,i}+q_{+,i}|\beta|_{+,i}/4\over\sigma_{D,i}},\quad
K_C^N=\sup_i {|\beta|_{+,i}\over4\sigma_{C,i}},\quad
q_+=\sup_i q_{+,i}.                                             \tag{U.10}
$$
这些局部比值避免将不同径向盒的不相干极值放在同一个分母。
例如 $M\gamma\le T\mu_{C,M}$，故相关积分核的总质量不超过 $T$。

## 4. 准确非线性源和两个真实 mean

Gauss 方程可以准确写为
$$
A=A_0-\ell c+Q(B,c),\qquad
Q(B,c)={B^2+\ell c^2\over C_0+c}.                              \tag{U.11}
$$
因此完整 Codazzi 非线性源是
$$
f_{b,m}=-M\gamma Q_m,\qquad f_{c,m}=\beta Q_m\quad(m\ne0).
                                                               \tag{U.12}
$$
这个 $-M$ 号来自 $i\operatorname{sgn}(m)$ 与角导 $im$ 的乘积。
全部 $Q$ 模均参与；没有把有限候选产生的高模再截掉。

给定 $Q$，(U.9) 和 (U.10) 直接给
$$
\begin{split}
\|d_{\ne0}\|_s&\le\|d_R\|_{A_s}+K_D^N\|Q_{\ne0}\|_s,\\
\|c_{\ne0}\|_s&\le\|c_L\|_{A_s}+T\|d_{\ne0}\|_s
                         +K_C^N\|Q_{\ne0}\|_s,\\
\|B_{\ne0}\|_s&=\|b_{\ne0}\|_s
                    \le\|d_{\ne0}\|_s+q_+\|c_{\ne0}\|_s.
\end{split}                                                     \tag{U.13}
$$

零模则是另外两条准确方程
$$
(a^2B_0)'=0,\qquad
(a^2C_0c_0)'=a^2C_0\beta Q_0.                                 \tag{U.14}
$$
注意式中的第一个 $C_0$ 是旋转参考，不是零模下标。也可将权记为
$w=a^2|C_0|>0$；它满足 $w'/w=\beta(\ell+1)$。
指定独立端口 $B_0(R)=b_{0R}$、$c_0(R)=c_{0R}$ 后，
$$
B_0(r)={a(R)^2\over a(r)^2}b_{0R},\qquad
c_0(r)={w(R)\over w(r)}c_{0R}
       -\int_r^R {w(t)\over w(r)}\beta(t)Q_0(t)\,dt.             \tag{U.15}
$$
本区间逐盒严格验证 $\beta<0$。于是两个边界比都不超过1，并且
$$
\int_r^R {w(t)\over w(r)}|\beta(t)|\,dt
\le {1\over1+\ell_-}=:K_0^N.                                 \tag{U.16}
$$
这里使用 $(w(t)/w(r))'=\beta(\ell+1)w(t)/w(r)$，积分总质量至多1。
所以 mean 的非线性源已实际支付，不是把 $Q_0$ 或 $c_0$ 设为0。
若还指定一般强制 mean 源，其两个核分别不超过
$1/(2\beta_*)$ 和 $1/[\beta_*(1+\ell_-)]$，其中
$\beta_*\le-\beta$。

合并 (U.13)–(U.16)，记
$$
H_C=1+q_+,\qquad H_D=1+(1+q_+)T,
$$
$$
K_{\ne0}^N=H_DK_D^N+(1+q_+)K_C^N,\qquad
K^N=\max(K_{\ne0}^N,K_0^N).                                   \tag{U.17}
$$
因为 $\|Q\|_s=\|Q_{\ne0}\|_s+\sup|Q_0|$，完整非线性驱动算子满足
$$
\|\mathcal T(B,c)\|_s
\le H_C\|c_L\|_{A_s}+H_D\|d_R\|_{A_s}
          +|b_{0R}|+|c_{0R}|+K^N\|Q(B,c)\|_s.                 \tag{U.18}
$$
本不等式同时保留一般反射扇区、所有负频率及两个 mean。

## 5. 全频非线性收缩定理

设 $C_*\le\inf_I|C_0|$、$\Lambda=\max(1,\sup_I\ell)$，并取
$0<\rho<C_*$。在完整闭球 $\|(B,c)\|_s\le\rho$ 内，Neumann 级数和
Banach 代数不等式给
$$
\|Q(B,c)\|_s\le {\Lambda\rho^2\over C_*-\rho},
                                                               \tag{U.19}
$$
$$
\|Q(B,c)-Q(\widetilde B,\widetilde c)\|_s
\le\Lambda\left({2\rho\over C_*-\rho}
             +{\rho^2\over(C_*-\rho)^2}\right)
\|(B-\widetilde B,c-\widetilde c)\|_s.                          \tag{U.20}
$$
这里用 $\|B\|^2+\ell_+\|c\|^2\le\Lambda(\|B\|+\|c\|)^2$。

因此，只要四端口的线性预算为 $H$，并满足
$$
H+K^N{\Lambda\rho^2\over C_*-\rho}<\rho,\qquad
L_N:=K^N\Lambda\left({2\rho\over C_*-\rho}
             +{\rho^2\over(C_*-\rho)^2}\right)<1,              \tag{U.21}
$$
(U.9)、(U.15) 定义的完整算子在闭球上有唯一固定点。
这是所有物理 Fourier 模的 Banach 固定点，不是有限模式极限的假定。

连续系数和逐模积分核给径向连续性；绝对可和的统一上界允许将
Fourier 和与积分交换。对 $s=2$，角向二导绝对一致收敛，Codazzi
方程又给连续径向一导。Gauss 方程由 (U.11) 准确成立。
在单连通角图内，可以用同一 R126 frame 方程重建相同 $g_0$ 的
$C^2$ 浸入。要下降为完整圆周上的浸入，仍须真实 frame/position
monodromy 为恒等；本篇四个独立端口没有替代这个条件。

解对四端口连续，且两组合法端口的解差满足
$$
\|\Delta(B,c)\|_s\le
{H_C\|\Delta c_L\|_{A_s}+H_D\|\Delta d_R\|_{A_s}
      +|\Delta b_{0R}|+|\Delta c_{0R}|\over1-L_N}.             \tag{U.22}
$$
严格球内的端口依赖还由解析 Neumann 级数及
$\|(I-D\mathcal T)^{-1}\|\le(1-L_N)^{-1}$ 给出。
同样，whole $\eta$ 的统一收缩结合逐模连续性给参数连续解图；
这里不声称尚未验证的参数高阶导数界。

## 6. 已实际通过的预算

`fourfold_codazzi_cap_unweighted_nonlinear_budget.py` 以320位 Arb
消费已经完成的 R133 v2 全帽报告；不是重采样浮点系数。它重核
原 producer、原失败 checkpoint、全部依赖和 theorem SHA；保留
原始实际 germ，并重新核完1334盒的全频 Riccati 后缀面。
在选出的663个真闭盒上得到以下有向外包：

| 常数 | 严格可用界 |
|---|---:|
| $q_+$ | $<1.05975182$ |
| $T$ | $<2.42228744$ |
| $K_D^N$ | $<1.34980636$ |
| $K_C^N$ | $<0.60557186$ |
| $K_0^N$ | $<0.52345582$ |
| $K^N$ | $<9.33173766$ |
| $\ell_-$ | $>0.91038091$ |
| $\ell_+$ | $<1.09717032$ |
| $C_*$ | $>0.17053380$ |
| $\beta_*$ | $>4.94269564$ |

取准确有理数
$$
\rho=1/500,\qquad \|c_L\|_{A_2}\le1/2000,
$$
$$
\|d_R\|_{A_2}\le10^{-6},\qquad
|b_{0R}|\le10^{-6},\qquad |c_{0R}|\le10^{-6}.                  \tag{U.23}
$$
完整 native 实际给出
$$
H<0.001037865217,\qquad
H+K^N\Lambda\rho^2/(C_*-\rho)<0.001280867047<0.002,
$$
$$
L_N<0.244443689<1,\qquad
|C_0+c|>0.16853380.                                            \tag{U.24}
$$
因而 (U.23) 的**每组**四独立端口都有唯一上述小解，而不是只对
某个选定的有限谱端口成立。

## 7. 真正完整候选在 $r=3/2$ 的输入消费

输入文件为
`notes/2026-11-13-R133-compact-metric-outer-mean-m64-candidate.npz.gz`，
SHA256
`4046eb7ac8da162ab9aad9fcb4991933200abdbc2c22ed6329d49bb13d72b856`。
producer 保留其全部64个物理 cosine 模，取精确切口 $L=3/2$。
候选存储中每个 double 都解释为准确 dyadic；径向 cubic 的四个
系数在准确 $L-r_i$ 上用 Arb Horner 求值，并乘 metadata 中
$\alpha=0.65$ 的**实际 double 所代表的准确有理数**。
报告列出所有64个完整非零模系数的有向盒。

由此定义一个明确有限 Fourier 输入 $c_L$。其物理频率是
$4,8,\ldots,256$，更高输入频率准确为0；这只是边界输入有限，
不限制 (U.11)–(U.21) 的非线性解含有的无限高模。
对实 cosine 系数 $c_j$，非齐次 $A_2$ 范数准确为
$$
\|c_L\|_{A_2}=\sum_{j=1}^{64}(1+4j)^2|c_j|.
$$
native 给
$$
\|c_L\|_{A_2}<0.000298228692<0.0005,
\qquad\text{输入余量}>0.000201771308.                           \tag{U.25}
$$
所以这个实际候选的完整非零 $C$ 端口确实可消费。它的 mean
$c_0(L)$、其 $B(L)$、其浮点方程残差及 finite-BVP 成功标记均没有
用于存在证明；前两个量是本篇准确解图的输出，仍须与内侧 body
联立匹配。可取另外三个端口为0来得到一个具体驱动问题，也可
取 (U.23) 中任意值；取0只指定驱动问题，不能被称作已完成外尾。

本输入来自新 $\nu$ 浮点支路，但在 $r\ge.18$ 参考度量与
$C_0$ 准确不变。对于每个 whole-$\eta$ 目标，使用同一个确定的
非零有限输入，加上该目标自身的旋转 mean $C_0$；不存在把
浮点中心的 primitive 误差或旧 waist 解偷渡到区间证明的问题。

## 8. 已付接口和仍须联立的接口

本篇付清的是整个 $[3/2,25/8]$、全部角模、两个 mean 的真实
非线性 Codazzi 解算，以及四端口解图的强范数预算。它可替换
此前在这个小外帽区间只有线性 Jacobi 源图的部分。

真正外尾仍须代入 R119 的完整 nonlinear regular 条件，连同两个
mean/holonomy 行；不能把线性 $d_R=0$ 或某个标签取0当成该条件。
在 $r=3/2$ 仍须匹配本篇输出的 $B$、mean 和框架/位置数据。
在 $r<3/2$ 的 core、第一 turning、内侧正帽大扰动以及新 $\nu$
条带没有由本篇自动获得全频逆。完整闭曲面、reach、固定 grip
和可见位移仍待这些真实接口闭合。

原生结果文件：

- `notes/2026-11-13-R133-unweighted-driven-cap-r15-native.json.gz`；
- `notes/2026-11-13-R133-unweighted-full-cap-rate-rejection-native.json.gz`；
- 完整源码/结果/证明清单见
  `notes/2026-11-13-R133-unweighted-driven-cap-manifest.json`。
