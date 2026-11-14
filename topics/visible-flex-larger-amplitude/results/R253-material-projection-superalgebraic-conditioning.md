# R253. 固定非恒材料换角的前模投影可以超代数病态

2026-11-14，exact_refinement，AI 辅助。

**状态：已证明的条件定理。** 对任意一个固定的、光滑的、严格正且非恒定的完整材料密度，满足下文奇对称和 $\pi$ 周期条件时，法线角前 $M$ 个非均值余弦模到材料角前 $M$ 个非均值余弦模的方块投影，其最小奇异值随 $M$ 增大至少有超代数小的上界。同一组有限模输入同时适用于连续投影，以及任意固定 $\varepsilon>0$ 下所有偶数 $N\ge(4+\varepsilon)M$ 的精确均匀 DFT。被省略的输出均值也超代数小，因而结论不是把输入能量藏进常数项。

这里的“超代数”指对每个 $q>0$ 都有一个依赖固定映射、$\varepsilon$ 和 $q$ 的常数及起始模数；不指已经给出了实际 $M=112$ 的有效数值界，也不指指数衰减。全文没有使用新的数值计算，不判断本题任何一次有限维 BVP 失败的原因。

[R250](R250-material-angle-square-projection-invertibility.md) 证明这些方块在精确算术下行列式严格为正。本结果与之相容：精确可逆性不提供随模数一致的稳定性。

## 1. 定义、归一化与结论

固定一个 $C^\infty$ 映射 $\Phi:\mathbb R\to\mathbb R$，满足

$$
\Phi(-\varphi)=-\Phi(\varphi),\qquad
\Phi(\varphi+\pi)=\Phi(\varphi)+\pi,\qquad
\rho(\varphi):=\Phi'(\varphi)>0.
\tag{253.1}
$$

再假设 $\rho$ 不是常数。它是偶的、$\pi$ 周期的光滑函数，而且

$$
\frac1\pi\int_0^\pi\rho(\varphi)\,d\varphi=1.
\tag{253.2}
$$

严格正性及周期性给出全局正下界，所以 $\Phi$ 是实线上的保向光滑微分同胚。记 $\psi=\Phi^{-1}$；它也奇对称、满足 $\psi(\theta+\pi)=\psi(\theta)+\pi$，且

$$
\psi'(\theta)=\frac1{\rho(\psi(\theta))}.
\tag{253.3}
$$

映射在整个定理中固定，不随 $M$ 或 $N$ 改变。由一个固定有限核心生成的完整正密度可以满足这些假设；不允许在每个 $M$ 下先截掉不同的核心尾部，再把得到的一列不同映射当作本定理的同一个 $\Phi$。

令

$$
E_M=\operatorname{span}_{\mathbb R}
 \{\cos(2m\varphi):1\le m\le M\}.
$$

对 $a=(a_1,\ldots,a_M)^{\mathsf T}\in\mathbb R^M$，写

$$
q_a(\varphi)=\sum_{m=1}^M a_m\cos(2m\varphi).
$$

以下圆周 $L^2$ 范数均使用概率测度 $d\varphi/(2\pi)$ 或 $d\theta/(2\pi)$。于是

$$
\|a\|_2^2=2\|q_a\|_{L^2(d\varphi/(2\pi))}^2.
\tag{253.4}
$$

连续非均值矩阵为

$$
(P_M)_{jm}
=\frac1\pi\int_0^{2\pi}
 \cos(2m\psi(\theta))\cos(2j\theta)\,d\theta,
\qquad 1\le j,m\le M.
\tag{253.5}
$$

对偶数 $N>4M$，定义 $\theta_\ell=2\pi\ell/N$ 及精确 DFT 矩阵

$$
(P_{M,N})_{jm}
=\frac2N\sum_{\ell=0}^{N-1}
 \cos(2m\psi(\theta_\ell))\cos(2j\theta_\ell),
\qquad 1\le j,m\le M.
\tag{253.6}
$$

这里使用精确逆映射值和精确求和；浮点逆映射及舍入误差不在本定理中。相应输出均值记为

$$
m_M(a)=\frac1{2\pi}\int_0^{2\pi}q_a(\psi(\theta))\,d\theta,
\qquad
m_{M,N}(a)=\frac1N\sum_{\ell=0}^{N-1}q_a(\psi(\theta_\ell)).
\tag{253.7}
$$

**定理 253-A。** 在上述假设下，任意固定 $\varepsilon>0$ 都存在一列实向量 $e_M\in\mathbb R^M$，$\|e_M\|_2=1$，使对每个 $q>0$，存在 $C_q<\infty$ 和 $M_q$，对所有 $M\ge M_q$ 都有

$$
\|P_Me_M\|_2+|m_M(e_M)|\le C_qM^{-q},
\tag{253.8}
$$

以及

$$
\sup_{\substack{N\ {\rm even}\\N\ge(4+\varepsilon)M}}
\left(\|P_{M,N}e_M\|_2+|m_{M,N}(e_M)|\right)
\le C_qM^{-q}.
\tag{253.9}
$$

向量 $e_M$ 可以依赖固定的 $\Phi$ 和 $\varepsilon$，但不依赖 $N$，也不依赖所要求的指数 $q$。特别地，同一列 $e_M$ 同时给出全部代数阶的界，并且

$$
\sigma_{\min}(P_M)\le C_qM^{-q},
\qquad
\sup_{\substack{N\ {\rm even}\\N\ge(4+\varepsilon)M}}
\sigma_{\min}(P_{M,N})\le C_qM^{-q}.
\tag{253.10}
$$

同时控制输出均值意味着：即使在非均值方块上方加上完整的均值输出行，所构造的无源均值输入仍满足同样的超代数小输出估计。

## 2. 在密度小于 $1$ 的区域选固定窗口

由 $\rho$ 非恒、连续及平均值为 $1$，必有 $\rho<1$ 的开区间。偶性与 $\pi$ 周期性把该区域反射、平移到 $[0,\pi/2]$；开性保证可以选取一点 $\varphi_0\in(0,\pi/2)$ 且 $\rho(\varphi_0)<1$。

固定 $\varepsilon>0$。利用连续性，选取包含 $\varphi_0$、闭包位于 $(0,\pi/2)$ 的小开区间 $I$，并选常数 $\rho_-,\rho_+$，使在 $\overline I$ 的某个开邻域上

$$
0<\rho_-\le\rho(\varphi)\le\rho_+<1,
\qquad
\rho_+<(1+\varepsilon/2)\rho_-.
\tag{253.11}
$$

这是可能的：当 $I$ 缩小时，上下界都可以任意接近同一个正数 $\rho(\varphi_0)<1$。

取非零、非负的 $\eta\in C_c^\infty(I)$，并作偶的 $\pi$ 周期化

$$
w(\varphi)=
\sum_{k\in\mathbb Z}
\bigl(\eta(\varphi-k\pi)+\eta(-\varphi-k\pi)\bigr).
\tag{253.12}
$$

在每个有界区间上只有限多个求和项非零。故 $w$ 是非零、光滑、偶的、$\pi$ 周期函数。其支撑在 $I$、$-I$ 的周期复制内，(253.11) 由 $\rho$ 的对称性在整个支撑的一个固定开邻域上成立。

选择固定载波比率 $\mu$ 满足

$$
\rho_+<\mu<
\min\{1,(1+\varepsilon/2)\rho_-\}.
\tag{253.13}
$$

右端严格大于 $\rho_+$，故可选。再固定

$$
0<\nu<\min\{\mu,1-\mu\}.
\tag{253.14}
$$

这两处严格余量同时承担不同的作用：$\mu>\rho_+$ 让换角后的局部载波频率超过所有保留的材料角模；$\mu<(1+\varepsilon/2)\rho_-$ 让它低于最近 DFT alias 频带；$\nu$ 则为把窗口截为有限源频率留下空间。

## 3. 先截断窗口，得到严格的有限源模

因为 $w$ 光滑、偶且 $\pi$ 周期，其 Fourier 展开为

$$
w(\varphi)=b_0+\sum_{k=1}^\infty b_k\cos(2k\varphi).
$$

对任意正整数 $r$，对系数积分分部 $r$ 次给出 $|b_k|\le C_r k^{-r}$；周期边界项全部相消。因此对

$$
w^{[K]}(\varphi)=b_0+\sum_{k=1}^K b_k\cos(2k\varphi)
$$

以及任意 $s>0$，选择整数 $r>s+1$ 并求和可得

$$
\|w^{[K]}-w\|_\infty\le C_sK^{-s}.
\tag{253.15}
$$

令

$$
\ell_M=\lfloor\mu M\rfloor,\qquad K_M=\lfloor\nu M\rfloor,
\qquad
q_M(\varphi)=w^{[K_M]}(\varphi)\cos(2\ell_M\varphi).
\tag{253.16}
$$

由 (253.14)，充分大的 $M$ 满足

$$
1\le \ell_M-K_M,\qquad \ell_M+K_M\le M.
\tag{253.17}
$$

乘积恒等式

$$
\cos(2k\varphi)\cos(2\ell_M\varphi)
=\tfrac12\cos(2(\ell_M+k)\varphi)
 +\tfrac12\cos(2(\ell_M-k)\varphi)
$$

说明 $q_M$ 严格属于 $E_M$，没有常数项，也没有任何大于 $M$ 的源模。这里使用的是已经截断的窗口；没有把一个紧支光滑窗口本身冒作有限 Fourier 多项式。

辅助函数

$$
u_M(\varphi)=w(\varphi)\cos(2\ell_M\varphi)
$$

一般不是有限模，但由 (253.15) 和 $K_M\asymp M$，对每个 $s>0$，

$$
\|q_M-u_M\|_\infty\le C_sM^{-s}.
\tag{253.18}
$$

设 $a_M$ 为 $q_M$ 的 $M$ 个非均值系数。为证明归一化不会放大误差，注意

$$
\|u_M\|_{L^2}^2
=\frac12\|w\|_{L^2}^2
 +\frac12\int_0^{2\pi}
     w(\varphi)^2\cos(4\ell_M\varphi)\frac{d\varphi}{2\pi}
\longrightarrow \frac12\|w\|_{L^2}^2>0.
\tag{253.19}
$$

最后一项由对光滑周期函数 $w^2$ 分部积分趋零。(253.18)、有界性及 (253.4) 于是给出

$$
\|a_M\|_2=\sqrt2\,\|q_M\|_{L^2}\longrightarrow\|w\|_{L^2}>0.
\tag{253.20}
$$

定义 $e_M=a_M/\|a_M\|_2$。对尚未满足上述充分大条件的有限个 $M$，任取一个单位向量作为 $e_M$，不影响任何渐近结论。这列输入只由 $\Phi,\varepsilon,w,\mu,\nu$ 决定，独立于 $N$ 及稍后所需的衰减阶数。

## 4. 对全部保留频率及全部 alias 的统一非驻相界

先对尚未截断窗口的换角函数

$$
v_M(\theta)
=u_M(\psi(\theta))
=A(\theta)\cos(2\ell_M\psi(\theta)),
\qquad
A(\theta)=w(\psi(\theta))
\tag{253.21}
$$

估计。$A$ 固定、光滑，其支撑邻域上由 (253.3)、(253.11) 有

$$
\frac1{\rho_+}\le\psi'(\theta)\le\frac1{\rho_-}.
\tag{253.22}
$$

取 Fourier 系数约定

$$
\widehat v_M(n)=\frac1{2\pi}\int_0^{2\pi}
v_M(\theta)e^{-in\theta}\,d\theta,
\qquad n\in\mathbb Z.
$$

展开余弦后，出现两个相位

$$
\Xi_\pm(\theta)=\pm2\ell_M\psi(\theta)-n\theta.
\tag{253.23}
$$

需要统一处理的频率是

$$
n=\tau\,2j+kN,\qquad
0\le j\le M,\quad \tau\in\{-1,1\},\quad k\in\mathbb Z,
\quad N\ge(4+\varepsilon)M.
\tag{253.24}
$$

$j=0$ 包含输出均值。设 $C_0=4+\varepsilon$。

### 4.1 主频带 $k=0$

在振幅支撑邻域上，

$$
|\Xi_\pm'|
\ge 2\ell_M/\rho_+-2M
\ge (2\mu/\rho_+-2)M-2/\rho_+.
\tag{253.25}
$$

(253.13) 使第一项系数严格为正，所以充分大的 $M$ 下存在固定 $c_0>0$，使 $|\Xi_\pm'|\ge c_0M$。此界同时涵盖两种相位符号、两种 $\tau$ 和全部 $0\le j\le M$。

### 4.2 所有非零 alias $k\ne0$

由 $\ell_M\le\mu M$，令 $B=2\mu/\rho_-$，则 (253.13) 给出

$$
2+B<4+\varepsilon=C_0.
\tag{253.26}
$$

对任何非零 $k$，反三角不等式给出

$$
\begin{aligned}
|\Xi_\pm'|
&\ge |n|-2\ell_M/\rho_-\\
&\ge |k|N-(2+B)M\\
&\ge \left(1-\frac{2+B}{C_0}\right)|k|N.
\end{aligned}
\tag{253.27}
$$

最后一步使用 $|k|N\ge C_0M$。因此全部 alias 离开局部载波有一个与 $j,k,N,M$ 无关的严格相对间隙。

合并两种情形，令

$$
\Lambda=M+|k|N.
$$

则支撑邻域上有 $|\Xi_\pm'|\ge c\Lambda$，其中 $c>0$ 固定。另一方面，对每个固定的导数阶数，归一化相位 $\Xi_\pm/\Lambda$ 的各阶导数在该邻域上一致有界：一阶中 $|n|/\Lambda\le2$，更高阶只含 $2\ell_M\psi^{(r)}/\Lambda$；$\psi$ 固定光滑，$\ell_M\le\mu M\le\mu\Lambda$。

由此，对任意正整数 $L$，在振幅支撑内重复分部积分 $L$ 次得到

$$
\left|\widehat v_M(\tau\,2j+kN)\right|
\le C_L(M+|k|N)^{-L}.
\tag{253.28}
$$

为明确此步骤的统一性，可以在每个固定支撑区间内写 $\zeta=\Xi_\pm/\Lambda$，从 $A_0=A$ 递归定义

$$
A_{r+1}=-\frac{d}{d\theta}
   \left(\frac{A_r}{i\zeta'}\right).
$$

$\zeta'$ 在支撑邻域上的统一正下界，以及 $\zeta$ 各阶导数的统一上界，归纳给出每个固定 $r$ 的 $\|A_r\|_{L^1}\le C_r$。积分等于 $\Lambda^{-L}\int A_Le^{i\Lambda\zeta}$。振幅在这些区间的边界附近恒为零，故无边界项。可以只在支撑邻域内定义倒数；支撑之外可能出现的驻点与此积分无关。最后对有限个区间及两种相位求和，得到 (253.28)。

这不是只对最近的一对 alias 的估计，而是具有足以对所有 $k\in\mathbb Z$ 求和的统一衰减。

## 5. 连续输出、DFT alias 和有限窗口误差

### 5.1 连续输出

由 $k=0$ 的 (253.28)，对所有 $0\le j\le M$，

$$
|\widehat v_M(2j)|+|\widehat v_M(-2j)|
\le C_LM^{-L}.
\tag{253.29}
$$

第 $j\ge1$ 个实余弦系数是 $\widehat v_M(2j)+\widehat v_M(-2j)$；均值是 $\widehat v_M(0)$。因此每一个所需输出标量都有同一阶界。

### 5.2 精确离散求和与全部 alias

每个固定 $M$ 的 $v_M$ 是光滑周期函数，Fourier 级数绝对收敛。把该级数代入有限均匀求和，并使用单位根正交性，严格得到

$$
\frac1N\sum_{\ell=0}^{N-1}
v_M(\theta_\ell)e^{-in\theta_\ell}
=\sum_{k\in\mathbb Z}\widehat v_M(n+kN).
\tag{253.30}
$$

对于 $n=\pm2j$、$0\le j\le M$，由 (253.28)，任意整数 $L>1$ 下，

$$
\begin{aligned}
\sum_{k\in\mathbb Z}
 |\widehat v_M(\pm2j+kN)|
&\le C_L\sum_{k\in\mathbb Z}(M+|k|N)^{-L}\\
&\le C_LM^{-L}
 \left(1+2C_0^{-L}\sum_{k=1}^\infty k^{-L}\right).
\end{aligned}
\tag{253.31}
$$

括号是与 $M,N,j$ 无关的有限常数。这证明精确 DFT 的每个保留余弦系数及其均值均为 $O_L(M^{-L})$，且对所有允许的 $N$ 一致。偶数条件保证与本课题/R250 的网格和对称空间完全一致；上面的 alias 估计本身不依赖任何未说明的“没有混叠”假设。

### 5.3 恢复严格有限的源多项式

令真正使用的换角函数为

$$
f_M(\theta)=q_M(\psi(\theta)).
$$

由 (253.18)，不论连续还是任意离散角点，

$$
\|f_M-v_M\|_\infty
=\|q_M-u_M\|_\infty\le C_sM^{-s}.
\tag{253.32}
$$

对均值泛函，此替换造成的误差至多为上式右端；对归一化为 $1/\pi$ 的连续余弦系数或 $2/N$ 的 DFT 余弦系数，误差至多为右端的两倍。这里直接使用上确界范数，故没有随 $N$ 增大的因子，也不需要对截断余项逐一分析 alias。

取 $s=L$，(253.29)—(253.32) 说明实际有限输入 $a_M$ 的全部 $M$ 个输出坐标及均值，每个都不超过 $C_LM^{-L}$。从逐坐标界转换为 Euclidean 范数必须支付维数因子：

$$
\|P_Ma_M\|_2,\ \|P_{M,N}a_M\|_2
\le C_L\sqrt M\,M^{-L}.
\tag{253.33}
$$

均值单独仍为 $C_LM^{-L}$。由 (253.20) 归一化，再对任意给定 $q>0$ 选择整数 $L>q+\tfrac12$，就得到 (253.8)—(253.9)。最小奇异值不超过任一单位输入的输出范数，所以 (253.10) 随之成立。定理 253-A 证毕。

所有实际输入 $q_M$ 均实、偶、$\pi$ 周期；$\psi$ 的奇对称及 $\pi$ 平移关系使 $f_M$ 也实、偶、$\pi$ 周期。因此连续正弦系数为零，偶数原点对齐均匀网格中的正弦系数也由反射配对精确为零。构造没有把未记录的奇对称输出作为漏洞。

## 6. 条件数增长，而非整个矩阵一起缩小

**推论 253-B。** 在定理 253-A 的假设下，任意固定 $\varepsilon>0$ 和 $q>0$，存在 $c_q>0$ 与 $M_q$，使对所有充分大的 $M$，

$$
\kappa_2(P_M)\ge c_qM^q,
\qquad
\inf_{\substack{N\ {\rm even}\\N\ge(4+\varepsilon)M}}
\kappa_2(P_{M,N})\ge c_qM^q.
\tag{253.34}
$$

本题的精确可逆性已经由 R250 给出；即使不引用它，也可把奇异矩阵的条件数定义为 $+\infty$，以下证明仍成立。

**证明。** 只需给最大奇异值一个与 $M$ 无关的正下界。由 (253.1)，$\psi$ 将 $[0,\pi/2]$ 严格递增地映至自身。令

$$
x=\cos(2\theta),\qquad
u(x)=\cos\!\left(2\psi\!\left(\tfrac12\arccos x\right)\right),
\qquad
d\omega(x)=\frac{dx}{\pi\sqrt{1-x^2}}.
$$

$u$ 是 $[-1,1]$ 到自身的严格递增连续双射。$\omega$ 是概率测度且 $\int x\,d\omega=0$。逐四分之一圆换元给出，所有 $M\ge1$ 的同一左上角元素为

$$
b=(P_M)_{11}
=2\int x u(x)\,d\omega(x)
=\iint (x-y)(u(x)-u(y))\,d\omega(x)d\omega(y)>0.
\tag{253.35}
$$

最后严格正是因为 $u$ 严格递增，$x\ne y$ 时被积函数为正，而对角线的乘积测度为零。故 $\sigma_{\max}(P_M)\ge b$。

同一个固定光滑函数的均匀 Riemann 和收敛给出 $(P_{M,N})_{11}=b_N\to b$，这里 $b_N$ 不依赖 $M$。所以存在固定 $N_0$，对全部 $N\ge N_0$ 都有 $b_N\ge b/2$。由于 $N\ge C_0M$，充分大的 $M$ 下此界对全部允许的 $N$ 同时成立，故 $\sigma_{\max}(P_{M,N})\ge b/2$。结合 (253.10) 即得 (253.34)。证毕。

## 7. 假设边界及本课题中的使用范围

1. **固定映射是实质条件。** 证明中的窗口、非驻相间隙、各阶导数常数及归一化下界都针对同一个 $\Phi$。若核心 $c=c_M$ 随分辨率改变，要对整个映射族重新证明这些量的一致界；不能直接套用本定理的常数。
2. **非恒密度是实质条件。** 若 $\rho\equiv1$，奇对称强迫 $\Phi(\varphi)=\varphi$；此时连续矩阵为单位阵，$N>4M$ 的精确 DFT 矩阵也为单位阵。不存在本构造所需的 $\rho<1$ 窗口。
3. **固定过采样余量是实质条件。** 结论对每个固定 $\varepsilon>0$ 成立，常数不宣称在 $\varepsilon\downarrow0$ 时一致。只有 $N>4M$、但 $N-4M=o(M)$ 的序列没有被本证明覆盖。
4. **光滑性支付全部衰减阶。** 这里假设 $C^\infty$，因此窗口截断和非驻相可以使用任意有限次数的分部积分。有限正则性只能在可用导数阶内给相应有限代数阶估计。
5. **无有限 $M$ 的数值病因结论。** $\rho$ 非恒但接近常数时，允许窗口和频率余量可能很小，起始模数及常数可能很大。此定理既没有计算真实 $P_{112}$ 的最小奇异值，也没有证明其近核必然进入真实完整 BVP 的允许方向。
6. **材料高度块不等于完整方程。** 真实右边界还包含高度导数的材料换角、原有限流的截投影、真实尾 DN、核心和标量剖面的导数，以及全段 collocation 方程。R250 的可逆性和本定理的病态上界都不能替代这些完整算子的实际核验。连续圆锚中的某些形式因子恒等式，也不能越过实际中间截投影直接当作有限矩阵等式。
7. **不改变冻结度量或完成标准。** 本文只描述一个固定材料坐标转换的有限方块。它不构造新的闭曲面，不证明全频尾匹配或全连续几何界，不放宽同一 $g$ 下等距误差收敛、$C^2$ 及本课题其余完成条件。

