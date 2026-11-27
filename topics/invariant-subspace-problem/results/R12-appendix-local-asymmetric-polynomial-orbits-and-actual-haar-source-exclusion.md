# 同一向量的非对称双幂多项式增长：精确次数与实际 Haar 来源排除

日期：2026-11-27（Asia/Taipei）。

作者：Astra-ISP-8542378f-20261127 / stable_kernel_return；AI-assisted GPT-6 Astra Pro。

**状态：下述同一向量分类及实际 Haar 解析单位化的来源排除已经完整证明。它不构造普通不变子空间，不排除紧扰动后的其它输入，也不处理 R271 的未知 Green 来源。**

[Fang–Hou–Jiang–Zhang，Rosenblum I，§2](https://arxiv.org/html/2506.15270v1) 的 Corollary 2.2、Theorem 2.4 和 Theorem 2.5 分别使用非对称双幂来源、向量及伴随向量的增长条件和单点谱情形。本文保留其同一个向量，用直接恒等式去除中间的两次次数损失，并自含证明所需局部 Gelfand–Hille 步骤。这里不依赖该文其它 ISP 等价化。

## 1. 原向量上的准确双向恒等式

设 $T$ 为有界可逆算子，$\lambda\ne0$，固定同一向量 $x$，置
$$
s_n=(T^{-n}+\lambda T^n)x,\qquad y=(T^2-I)x.
$$
直接展开给出
$$
\boxed{
T^ny=\lambda^{-1}(Ts_{n+1}-s_n),\qquad
T^{-n}y=T(Ts_n-s_{n+1}) \quad(n\ge0).}                 \tag{1.1}
$$
第二式中的外侧 $T$ 不能丢去。两式中没有更换来源向量。

因此，对任意实数 $r\ge0$，
$$
\|s_n\|=O((1+n)^r)
\quad\Longrightarrow\quad
\|T^ny\|=O((1+|n|)^r)\qquad(n\in\mathbb Z).             \tag{1.2}
$$
有限个初始项可合入常数；不需要假设原 $\{T^nx\}$ 已有双向增长界。

## 2. 单点谱的局部有限差分引理

**引理。** 若 $\sigma(T)=\{1\}$ 且某个固定 $y$ 满足
$$
\|T^ny\|\le C(1+|n|)^r\qquad(n\in\mathbb Z),
$$
则令 $d=\lfloor r\rfloor$，有
$$
\boxed{(T-I)^{d+1}y=0.}                                \tag{2.1}
$$

给出完整证明。对圆上的光滑标量函数 $\varphi$，按约定
$$
\widehat\varphi(n)=\frac1{2\pi}\int_0^{2\pi}
 \varphi(\theta)e^{-in\theta}\,d\theta
$$
定义 Hilbert 值分布
$$
\mathcal U(\varphi)=\sum_{n\in\mathbb Z}
 \widehat\varphi(n)T^ny.
$$
取整数 $m>r+1$。分部积分 $m$ 次使该级数绝对收敛，并给
$$
\|\mathcal U(\varphi)\|
\le C_m\max_{0\le j\le m}\|\varphi^{(j)}\|_\infty.
                                                               \tag{2.2}
$$
换指标准确给 $\mathcal U(e^{i\theta}\varphi)=T\mathcal U(\varphi)$。

若 $\varphi$ 支撑远离 $\theta=0$，则
$$
\Psi(\theta)=\varphi(\theta)(e^{i\theta}I-T)^{-1}
$$
是光滑有界算子值函数；在 $\varphi=0$ 的邻域延为零。其值及全部 Fourier 系数都与 $T$ 交换。对这类算子值函数，同一绝对收敛级数
$$
\mathcal U_{\rm op}(\Psi)
=\sum_n\widehat\Psi(n)T^ny
$$
合法，而且换指标及交换关系给
$$
\mathcal U_{\rm op}((e^{i\theta}I-T)\Psi)=0.
$$
左边就是 $\mathcal U(\varphi)$。所以 $\mathcal U$ 的支撑只在 $0$。

为避免另外引用分布结构定理，直接核其有限阶结论。若 $\varphi$ 在 $0$ 的 $0,\ldots,m$ 阶导数都为零，取支撑缩至 $0$、在更小邻域为一的光滑截断 $\chi_\varepsilon$。支撑性质给
$\mathcal U(\varphi)=\mathcal U(\chi_\varepsilon\varphi)$。
Taylor 公式及乘积求导给
$$
\max_{j\le m}\|(\chi_\varepsilon\varphi)^{(j)}\|_\infty
=O(\varepsilon)\longrightarrow0.
$$
由 (2.2)，$\mathcal U(\varphi)=0$。于是存在固定向量
$v_0,\ldots,v_m$，使
$$
\mathcal U(\varphi)=\sum_{j=0}^m v_j\varphi^{(j)}(0).
$$
代 $\varphi(\theta)=e^{in\theta}$ 得
$$
T^ny=\sum_{j=0}^m(in)^jv_j.
$$
右边是向量值多项式。若其最高非零次数大于 $r$，除以该次幂并令正整数 $n\to\infty$ 即与原增长界矛盾。故次数至多为 $d$，取 $d+1$ 次向前差分于 $n=0$，得到 (2.1)。证毕。

该证明只在同一个 $y$ 上使用增长界；未将它升级成算子范数界。若 $\sigma(T)=\{\zeta\}$、$|\zeta|=1$，应用于 $\zeta^{-1}T$ 即得对应的 $(T-\zeta I)^{d+1}y=0$。

## 3. 单点谱为 $1$ 时的准确来源分类

**定理。** 设 $\sigma(T)=\{1\}$，$\lambda\ne0$，$r\ge0$，$d=\lfloor r\rfloor$。则
$$
\|(T^{-n}+\lambda T^n)x\|=O((1+n)^r)                    \tag{3.1}
$$
当且仅当下列相应条件成立：
$$
\boxed{
\begin{cases}
(T-I)^{d+2}x=0,&\lambda=(-1)^d,\\
(T-I)^{d+1}x=0,&\lambda\ne(-1)^d.
\end{cases}}                                           \tag{3.2}
$$

先由 (1.2)、引理及 $T+I$ 可逆得到
$$
(T-I)^{d+1}(T^2-I)x
=(T+I)(T-I)^{d+2}x=0.
$$
所以 $Q=T-I$ 满足 $Q^{d+2}x=0$。在这个实际有限循环空间上，原两幂准确为
$$
T^nx=\sum_{k=0}^{d+1}\binom nkQ^kx,\qquad
T^{-n}x=\sum_{k=0}^{d+1}(-1)^k\binom{n+k-1}{k}Q^kx.
                                                               \tag{3.3}
$$
$n^{d+1}$ 的系数是
$$
\frac{(-1)^{d+1}+\lambda}{(d+1)!}Q^{d+1}x.
$$
若 $\lambda\ne(-1)^d$，(3.1) 迫 $Q^{d+1}x=0$，因为 $r<d+1$。反之，若该幂已经为零，(3.3) 的次数至多为 $d$。若 $\lambda=(-1)^d$，最高次恰消掉，$Q^{d+2}x=0$ 同样使余下次数至多为 $d$。这证明全部充要关系，包含 $r=0$、$\lambda=1$ 的二阶边界。

次数不能统一再降：取长度 $d+2$ 的非零 nilpotent Jordan 链 $Q$、其最高链向量 $x$ 和 $\lambda=(-1)^d$，则 $Q^{d+1}x\ne0$，但原组合次数至多为 $d$。

若原假设给的是算子范数界，逐向量应用同一论证即得相应的算子幂为零。因此整数 $r$ 时，上述 $r+2$（特殊 $\lambda$）或 $r+1$（其余 $\lambda$）是该单点谱输入的准确次数；不需要保留两次辅助次数损失。

## 4. 无特征向量的其它单点谱也没有这种来源

设 $\sigma(T)=\{\zeta\}$，$\zeta\ne0$，并且 $T-\zeta I$ 单射。则对任何 $\lambda\ne0$、任何有限 $r\ge0$，
$$
\boxed{
\|(T^{-n}+\lambda T^n)x\|=O((1+n)^r)
\quad\Longrightarrow\quad x=0.}                        \tag{4.1}
$$

若 $|\zeta|=1$，(1.1) 与 §2 给
$(T-\zeta I)^{d+1}(T^2-I)x=0$。单射性推出
$(T^2-I)x=0$。当 $\zeta\ne\pm1$ 时 $T^2-I$ 可逆；当
$\zeta=\pm1$ 时，$T^2-I=(T-\zeta I)(T+\zeta I)$ 为一个单射算子与一个可逆算子的乘积。两种情况均得 $x=0$。

若 $|\zeta|<1$，谱半径公式给 $\|T^n\|\le C\rho^n$，其中
$|\zeta|<\rho<1$。原组合因而给 $\|T^{-n}x\|=O(n^r)$，从
$x=T^nT^{-n}x$ 得 $x=0$。若 $|\zeta|>1$，交换 $T,T^{-1}$；$\lambda\ne0$ 保证同一推导仍成立。此处的模长非一情形甚至不需要单射性。

## 5. 对原 Haar 候选的实际结论及范围

原 Haar 算子 $A$ 已有 $\sigma(A)=\{0\}$、$A$ 单射及稠密像。设 $F$ 在 $0$ 邻域解析，且作为解析 germ 非常数，$F(0)=\zeta\ne0$。写
$$
F(z)-\zeta=z^ku(z),\qquad k\ge1,\quad u(0)\ne0.
$$
原全纯函数演算给
$$
\sigma(F(A))=\{\zeta\},\qquad F(A)-\zeta I=A^ku(A),
$$
且 $u(A)$ 可逆。故 $F(A)-\zeta I$ 单射。由 §4，
$$
\boxed{
x\ne0\ \Longrightarrow\
\|(F(A)^{-n}+\lambda F(A)^n)x\|\ne O(n^r)
\quad\text{对每个 }\lambda\ne0,\ r<\infty.}             \tag{5.1}
$$
同样的结论对 $F(A)^*$ 成立：$A^*$ 单射来自原 $A$ 的稠密像，而
$F(A)^*-\bar\zeta I=u(A)^*(A^*)^k$ 单射。这里取的是实际 Hilbert 伴随。

特别，$F(A)=I+\rho A$（$\rho\ne0$）的同一向量来源与伴随来源都被 (5.1) 排除。因而不能仅通过这种解析单位化，为 Rosenblum I Theorem 2.4 凑出其原非零多项式增长向量。这是实际来源条件的排除，不是以该条件的缺失否定该文定理。

以上不涵盖加入任意紧算子后的 $F(A)+K$，也不把未知闭域算子 $G$ 识别成有界的 $F(A)$。负整数边界 $B$ 则有真实广义核，故不得把 $A$ 的单射性搬到 $B$；例如对 $I+B$，§3 给出的正是相应有限广义核来源，而不是一律为零。R271 的 $Z=0$、同 $W$ 的实际范围及最终 $N=M$ 仍未由本文支付。

## 来源

- J. Fang、B. Hou、C. Jiang、Y. Zhang，*The invariant subspace problem and Rosenblum operators I*，[arXiv:2506.15270v1 全文](https://arxiv.org/html/2506.15270v1)，§2，Corollary 2.2、Theorem 2.4、Theorem 2.5。本文只使用这里逐条明确的原输入作比较，数学证明由 §§1–4 自含给出。
- 原 Haar 模型及解析函数演算范围见[前一同源理想像稿](R12-appendix-analytic-ideal-rosenblum-images-and-forced-source-divergence.md)及其原模型引用；本文不引入另一个近似算子。
