# R68. 补弧坐标控制基的多项式下界与原控制基的指数近核

维护：Astra-held10-06bbeb39-20261126。2026-11-26 UTC。

本条证明一个实际影响当前求解的表示区别。R65 的全周期正弦乘补弧窗在连续曲率范数中有明确的指数近核；把正弦坐标放在补弧本身，可得到每个有限阶的多项式下界。新族保留实际零控制锚点、固定目标度量、旋转闭合和最终准确保护弧。**它不证明完整 BVP 的逆界、存在性、任何新接受场或 10% 完成。**

独立审阅：actual_tail 逐项核验下述两个界、常数、奇偶性和零控制转换范围。数学推导不使用采样奇异值作为证明。

## 1. 固定的真实窗口与新族

令

$$
P=\frac{2\pi}{3},\qquad c=P/2,\qquad 0<S<c,\qquad L=c-S,\qquad 0<b<L,
$$

其中当前固定数据为 $S=.5,b=.2$。数据中的有限小数解释为已冻结实数；$P,L$ 及以下频率中的 $\pi$ 为真实常数。浮点求值误差须在实际图认证时另付。

对 $u\in[0,P)$，令 $v=u$ 于 $u\le c$，否则 $v=u-P$。保护弧是 $|v|\ge L$；补弧是 $-L<v<L$。定义原来的九次平滑窗

$$
S_9(t)=126t^5-420t^6+540t^7-315t^8+70t^9,
$$

$$
W(v)=S_9\!\left(\min(1,\max(0,(L-|v|)/b))\right),\qquad
D_1=\frac{630}{256b}.
$$

这与 R65 的真实补弧窗完全相同，因为
$|u-c|-S=L-|v|$。只改变正弦展开的坐标与频率。令

$$
\omega_j=\frac{j\pi}{L},\qquad
\Psi_j(v)=\frac{W(v)\sin(\omega_jv)}{\omega_j+D_1},\qquad
B_j=\Psi_j',\qquad j\ge1.
\tag{1}
$$

在补弧外把 $\Psi_j$ 定义为零，再作 $P$ 周期延拓。$W$ 为偶函数，$\Psi_j$ 为奇函数，$B_j$ 为偶函数，并且

$$
\int_0^P B_j(u)\,du=0,\qquad \|B_j\|_\infty\le1.
\tag{2}
$$

后一式来自
$\|W'\|_\infty=D_1$、$0\le W\le1$，以及

$$
|B_j|\le\frac{\omega_j+D_1}{\omega_j+D_1}=1.
$$

窗在 $|v|=L$ 五阶消失，又有 $\sin(\omega_jL)=0$，故外端点的零延拓至少 $C^5$。在平顶与过渡带的内部拼点一般只保证 $C^4$；**不把整个 phase 称为 $C^5$**。全局 $C^4$ 已足以给下述核心 $C^5$ 正则性。

固定一个真实接受的 R53 零控制锚点及其完整支撑向量 $b_*$，定义

$$
\Phi(u;\lambda,d)=\phi_{\rm base}(u;\lambda,b_*)
                    +\sum_{j\ge1}d_j\Psi_j(u).
\tag{3}
$$

取一个与阶数无关的系数空间，例如
$\sum_j(1+\omega_j^4)|d_j|<\infty$；有限阶一律严格补零嵌入。式 (1) 的所有频率、归一化和窗口均不依赖截断阶数。

R65 的旋转闭合积分和参数 jet 公式直接适用，只需把其 phase basis 换成 (1)。若 $\Phi'>0$，得到三重旋转、反射对称、周长 $2\pi$ 的严格凸单位速闭核心。一个充分条件是
$\kappa_{\rm base,min}-\sum_j|d_j|>0$；更精细的连续曲率验收仍可另行计算。

在 $\lambda=\lambda_*$、$d=0$ 时，完整核心及全部已有空间 jet（$F,F_u,F_{uu}$ 等）仍是原基准，数值入口可以字面委托原对象。新的参数 jet 按新 basis 计算，不声称旧 Jacobian 不变。$\lambda=1$ 时，保护弧内全部 $\Psi_j$ 恒为零，因此准确曲率仍为固定 $k$。R63 的目标度量与未知核心无关，完整 $\delta$、物理尾、材料图、gauge 和 mean1168 均可保持不变。

**跨族转换范围。** 新旧有限 span 不相同。当前可直接用已接受的 $d=0,\lambda=.002$ 锚点作同图转换；不能把一个非零 v2 控制向量原样搬入 (1)，也不能把它置零后声称同一图。后者必须另付完整转换和实际验收。

## 2. 新曲率控制算子的定量下界

所有本节范数均在真实补弧 $[-L,L]$ 上。对 $d\in\mathbb R^M$，置

$$
f(v)=\sum_{j=1}^M\frac{d_j}{\omega_j+D_1}\sin(\omega_jv),
\qquad h=Wf.
$$

正交性和 Cauchy–Schwarz 给

$$
\|f\|_2^2=L\sum_{j=1}^M\frac{d_j^2}{(\omega_j+D_1)^2},
\qquad
\|f\|_\infty^2\le\frac ML\|f\|_2^2.
\tag{4}
$$

取 $\eta=L/(4M)$。两个端部长度 $\eta$ 的条带总共最多含
$2\eta M/L=1/2$ 的 $L^2$ 质量。因此

$$
\int_{-L+\eta}^{L-\eta}|f|^2\ge\frac12\|f\|_2^2.
$$

多项式 $S_9(t)/t^5$ 在 $[0,1]$ 的四次 Bernstein 系数为

$$126,\quad21,\quad6,\quad9/4,\quad1.$$

全部至少为 $1$，故 $S_9(t)\ge t^5$，进而在上述内部区间

$$
W\ge w_M:=\min\!\left(1,\frac{L}{4Mb}\right)^5,\qquad
\|h\|_2\ge\frac{w_M}{\sqrt2}\|f\|_2.
\tag{5}
$$

$h$ 为奇函数，且 $h(0)=h(L)=0$。分别在两个半区间应用长度 $L$ 的 Dirichlet Poincaré 不等式，得到
$\|h'\|_2\ge(\pi/L)\|h\|_2$。这里使用了奇性；仅使用整个长度 $2L$ 的区间只能得到一半的常数。

合并 (4)、(5)：

$$
\boxed{\left\|\sum_{j=1}^M d_jB_j\right\|_{L^2(-L,L)}
\ \ge\
\frac{\pi}{\sqrt{2L}\,(\omega_M+D_1)}
\min\!\left(1,\frac{L}{4Mb}\right)^5\|d\|_{\ell^2}.}
\tag{6}
$$

所以每个有限阶的曲率列严格线性无关，且下界只按 $M^{-6}$ 量级下降。对应 Gram 矩阵有 $M^{-12}$ 量级下界。这不意味着完整 Frenet BVP、边界 Schur 补或某个具体离散 Jacobian 有同一下界。

## 3. 原全周期控制族的明确指数近核

原 R65 曲率列为

$$
\widetilde B_j(u)=
\frac{d}{du}\left(\frac{W(u)\sin(3ju)}{3j+D_1}\right).
$$

取整数 $N\ge1$，定义

$$
Q(u)=\frac{1-\cos(3u)}2,\qquad
f_N(u)=\sin(3u)Q(u)^N.
$$

$f_N$ 是最高模态阶数不超过 $N+1$、角频率不超过 $3(N+1)$ 的三重正弦多项式。在 $W$ 或 $W'$ 非零处，离保护弧中心至少为 $S$，故

$$
Q(u)\le q_*=\cos^2(3S/2)<1.
$$

利用 $Q'=(3/2)\sin(3u)$：

$$
\|(Wf_N)'\|_{L^2(0,P)}
\le\sqrt P\left[(D_1+3)q_*^N+\frac32Nq_*^{N-1}\right].
\tag{7}
$$

另一方面，在 $u=c\pm x$、
$1/(6\sqrt N)\le x\le1/(3\sqrt N)$ 的两小区间上，

$$
|\sin(3x)|\ge\frac1{\pi\sqrt N},\qquad
Q(u)^N\ge(1-1/(4N))^N\ge3/4.
$$

两区间总长为 $1/(3\sqrt N)$，所以

$$
\|f_N\|_{L^2(0,P)}
\ge\frac{\sqrt3}{4\pi}N^{-3/4}.
\tag{8}
$$

写 $f_N=\sum_{j=1}^{N+1}a_j\sin(3ju)$，取
$d_j=(3j+D_1)a_j$。由完整周期上的正交性，

$$
\|d\|_2\ge(3+D_1)\sqrt{2/P}\,\|f_N\|_2.
$$

故原连续列算子的最小奇异值满足

$$
\boxed{
\sigma_{\min}(\widetilde B_1,\ldots,\widetilde B_{N+1})
\le
\frac{4\pi P}{(3+D_1)\sqrt6}N^{3/4}
\left[(D_1+3)q_*^N+\frac32Nq_*^{N-1}\right].}
\tag{9}
$$

这是明确的指数近核，与 R65 已证的有限单射相容。它不能直接当作某个采样矩阵的奇异值界，更不是当前 M24 的精确数值。

## 4. 本次真实有限诊断

[源](../scripts/resume_20261126/probe_phase_basis_conditioning.py)与
[实际小记录](../notes/2026-11-26-phase-basis-conditioning-execution.json)
只计算两个声明 basis 的等权采样 $L^2$ 列矩阵，不运行 BVP，不读未接受场，也不改正在运行的 v2 provider。

8192 与 16384 两档角点分别计算；以下列第二档：

| M | 原全周期 basis 的采样条件数 | 新补弧 basis 的采样条件数 |
|---:|---:|---:|
| 8 | 约 $5.01\times10^4$ | 4.4673 |
| 16 | 约 $2.65\times10^{10}$ | 24.7296 |
| 24 | 最小奇异值已进入 binary64 舍入尺度 | 87.5199 |
| 32 | 同上 | 237.624 |
| 48 | 同上 | 1099.71 |
| 64 | 同上 | 3517.18 |

新族两档结果稳定。原 M24 及以上打印出的条件数随等价浮点三角评价发生明显变化，不能把 $10^{15}$ 量级打印值当成严格数值或 BVP 实际病因的证明。式 (6)、(9) 与这些诊断的身份分开。

复现命令（只写小标量记录，无场或网格数组）：

~~~bash
python scripts/resume_20261126/probe_phase_basis_conditioning.py \
  --out WORK/phase-basis-conditioning.json
~~~

当前真实 v2 的 $\lambda=.004$ 与 $.003$ 已分别以 RMS
$.1246462379$、$.0625026082$ 未过原门，失败场未晋源；记录见
[真实失败](../notes/2026-11-26-warm-v2-lambda-failures.json)。
这促使另起新族进行真实求解，而非沿原近核方向盲目升 M。新族仍须先通过零锚同图原门，再实际改变 $\lambda$；最终 full H、共同 Cartesian 二jet、固定问题加密、全时几何和 10% 标准全部保留。
