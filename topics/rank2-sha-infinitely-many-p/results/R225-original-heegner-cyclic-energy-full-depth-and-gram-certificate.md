# R225 — 原 Heegner 循环能量的全深度读出与完整整 Gram 证书

日期：2026-11-13。**状态：同一个原 Heegner 点的全部循环能量、完整 Smith 形式和任意局部深度的有限读出均已证明。仍未证明在联合无穷素数输入上有无穷多个 $k\le2$；主课题未完成。**

本篇继续 O4 的原 $R=D_pQ$，保留全部 $p$ 完成。R172 的两个能量和行列式在这里扩为一个共同的整矩阵：前 $(p-1)/2$ 个循环能量可以整地恢复真实 circulant Gram；其首个非零精度和该精度中的首个非零位置准确恢复任意局部深度 $k$。整个证书使用同一个原点生成格，未更换成饱和 Mordell–Weil 格。

## 1. 原点、完整配对与局部深度

沿用 R130/R139/R157/R172 的真实输入：$p\ge7$ 是所用曲线的好素数，$p$ 在虚二次域 $F$ 不分歧，$L/F$ 的群为
$$
 \Gamma=\langle\tau\rangle=C_p,\qquad
 N_\Gamma=\sum_{j=0}^{p-1}\tau^j .
$$
全部原 nonanomalous、formalizer 单位及有限坏素数排除仍按上述结果保留。取原非扭点
$$
 R=D_pQ,\qquad N_\Gamma R=O,\qquad cR=-\tau^hR,
 \qquad z=\frac{\log_E(R)}p\in I=\ker N_\Gamma
             \subset\mathcal P=\mathcal O_L\otimes\mathbb Z_p .
 \tag{1}
$$
$D_p$ 是原反演对称 formalizer；$R$ 在所有 $p$ 完成都位于 $p\mathcal O$ 形式盘。所有对数、迹和置换作用均在整个 $\mathcal P$ 上进行。

记
$$
 e=p-1,\quad g=e/2,\quad
 K=\mathbb Q_p(\zeta_p),\quad O=\mathbb Z_p[\zeta_p],\quad
 \varpi=\zeta_p^{(p-1)/2}(\zeta_p-1),
$$
$$
 \varpi^*=-\varpi,\qquad
 D=\varpi^2=\zeta_p+\zeta_p^{-1}-2 .
 \tag{2}
$$
这里 $*$ 送 $\zeta_p$ 到 $\zeta_p^{-1}$。为避免混淆，后文以 $d$ 表示循环距离，$D$ 始终表示 (2) 中的谱参数。

在原循环整格 $OR$ 上取完整局部配对
$$
 T(P_1,P_2)=
   \sum_{v\mid p}\operatorname{Tr}_{L_v/\mathbb Q_p}
   \left(\frac{\log_E(P_1)}p\frac{\log_E(P_2)}p\right).
 \tag{3}
$$
R172 已在原局部格上证明：存在真实的非零 $q$，使
$$
 q=\varpi^ku,\qquad k\ge1,\qquad u\text{ 为单位},
$$
$$
 \boxed{\quad
 T(fR,f'R)=\frac2p\operatorname{Tr}_{K/\mathbb Q_p}
                        (f(f')^*c_0),\qquad
 v_\varpi(c_0)=2k .
 \quad}
 \tag{4}
$$
其中：

- $p$ 在 $F$ 分裂时，原未分歧次数 $p$ étale 代数的自对偶正规整基给 $q\in\varpi O$、$c_0=qq^*$；
- $p$ 在 $F$ 惰性时，$K'=F_vK$ 是未分歧二次域扩张，$q\in\varpi O_{K'}$，原反射关系给
  $c_0=qq^*=-\operatorname{Nm}_{K'/K}(q)\in K$。

两种情形的 $c_0$ 都被 $*$ 固定。在第一种情形，自对偶正规整基的改选只使 $q$ 乘一个整单位，所以 $k$ 不依赖这项选择。式 (4) 中的 $1/p$ 是准确的 Fourier 迹公式；本文不将 Fourier 特征基冒称为整基。

## 2. 完整循环核与准确周期边界

对 $1\le r\le g$ 定义同一个整数群环元
$$
 \kappa_d=d(p-d)\quad(0\le d<p),\qquad
 K_r=\sum_{d=0}^{p-1}\kappa_d^r\tau^d,\qquad K_0=N_\Gamma .
 \tag{5}
$$
定义原对数能量
$$
 \mathcal E_r=
 \frac1{(2r)!}\operatorname{Tr}_\Gamma(zK_rz)
 =\frac1{(2r)!}\sum_{j,l=0}^{p-1}
                 \kappa_{\,j-l\bmod p}^{\,r}\tau^jz\,\tau^lz .
 \tag{6}
$$
因为 $2r\le p-1$，全部 $(2r)!$ 都是 $\mathbb Z_p$ 单位。式 (6) 是整二次式，属于 $\mathcal O_F\otimes\mathbb Z_p$；由 (1) 的反射与距离的对称性，它被 $c$ 固定，故准确属于 $\mathbb Z_p$。这包括 R164/R172 的原 $\mathcal E_1,\mathcal E_2$。

为计算 $K_r$，令
$$
 L_r(X)=
 2\sum_{a=0}^{\lfloor r/2\rfloor}
       \binom r{2a}(X-1)^{r-2a}(p^2-4X)^a-2X^r
       =\sum_{j=0}^{r-1}c_{rj}(p^2)X^j .
 \tag{7}
$$
所有 $c_{rj}(p^2)$ 都在 $\mathbb Z[p^2]$。最高项 $X^r$ 相消；在 $r\ge2$ 时，
$$
 c_{r,r-1}=-2r-8\binom r2=-2r(2r-1).
 \tag{8}
$$
$r=1$ 时 $L_1=-2$，也与相同最高系数公式相容。

**周期差分恒等式。** 在完整整数群环中，
$$
 \boxed{\quad
  (\tau+\tau^{-1}-2)K_r
    =\sum_{j=0}^{r-1}c_{rj}(p^2)K_j+J_r\cdot1,
 \qquad
 J_r=(p-1)^r-(-p-1)^r .
 \quad}
 \tag{9}
$$

**证明。** 对非边界循环距离，置 $X=d(p-d)$。有
$$
 (d+1)(p-d-1)=X+(p-2d)-1,\quad
 (d-1)(p-d+1)=X-(p-2d)-1,
$$
且 $(p-2d)^2=p^2-4X$。将两个 $r$ 次幂相加再减 $2X^r$，恰为 (7)。

当 $d=p-1$ 时，形式上的 $d+1=p$ 与循环上的 $d+1=0$ 都使 $\kappa=0$，故没有修正。只有 $d=0$：形式上的 $d-1=-1$ 给 $-p-1$，循环上的 $d-1=p-1$ 给 $p-1$。两者的 $r$ 次幂之差恰为 $J_r$，并出现在群环常数项。这证明 (9)，包括完整的 $K_0=N_\Gamma$ 项。$\square$

由奇次幂展开，
$$
 \frac{J_r}{p}
  =2\sum_{\substack{1\le a\le r\\a\ \mathrm{odd}}}
             \binom ra(-1)^{r-a}p^{a-1}\in\mathbb Z[p^2].
 \tag{10}
$$
不能先在完整置换格上删掉 (9) 的 $N_\Gamma$ 项。下一节才在非平凡特征块代入 $\tau=\zeta_p$；在该块 $N_\Gamma(\zeta_p)=0$。

## 3. 谱主部的最高项与准确归一化

**引理 1。** 存在 $b_{rj}\in\mathbb Z[p^2]$，使
$$
 \frac{K_r(\zeta_p)}p
       =\sum_{j=1}^r b_{rj}D^{-j},
 \qquad
 b_{rr}=(-1)^{r+1}(2r)! .
 \tag{11}
$$

**证明。** $r=1$ 时 (9) 给 $DK_1(\zeta_p)=2p$，故 $b_{11}=2$。归纳使用
$$
 D\,\frac{K_r(\zeta_p)}p
 =\sum_{j=1}^{r-1}c_{rj}(p^2)\frac{K_j(\zeta_p)}p+\frac{J_r}p .
$$
(10) 保证所有系数为整多项式，除以 $D$ 只增加一阶负幂。最高的 $D^{-r}$ 仅来自 $j=r-1$；其系数是
$$
 -2r(2r-1)\,(-1)^r(2r-2)!
       =(-1)^{r+1}(2r)! .
$$
这证明 (11)。$\square$

特别，若
$$
 \alpha_{rj}=b_{rj}/(2r)!,
$$
则对整个 $1\le r\le g$ 有
$$
 \alpha_{rj}\in\mathbb Z_p,\qquad
 \alpha_{rr}=(-1)^{r+1}.
 \tag{12}
$$
头三个准确式为
$$
 \frac{K_1(\zeta_p)}p=\frac2D,\qquad
 \frac{K_2(\zeta_p)}p=-\frac{24}{D^2}-\frac4D,
$$
$$
 \frac{K_3(\zeta_p)}p=
 \frac{720}{D^3}+\frac{180+12p^2}{D^2}
                         +\frac{6+2p^2}{D}.
 \tag{13}
$$
第三式也展示不能在全精度公式中删掉 $p^2$ 修正。它的归一化只在 $p\ge7$ 时使用，此时 $6!$ 仍为单位。

由 (4)、(6)，两个局部情形统一为
$$
 \boxed{\quad
 \mathcal E_r=
 \frac1{p(2r)!}\operatorname{Tr}_{K/\mathbb Q_p}
                         \bigl(K_r(\zeta_p)c_0\bigr)
 =\sum_{j=1}^r\alpha_{rj}
       \operatorname{Tr}_{K/\mathbb Q_p}(c_0D^{-j}) .
 \quad}
 \tag{14}
$$
惰性情形的 $c_0=-\operatorname{Nm}(q)$ 保留了原负号。对 $r=1,2$，(14) 正是 R172 的两种完成下的公式。较大的 $j$ 可以使某个被取迹的元素不整；(6) 已保证整个能量整，本文不将这些单项无条件模 $p$ 约化。

## 4. 同一个完整 circulant Gram 的整恢复

令
$$
 t_d=T(R,\tau^dR)\qquad(0\le d<p).
 \tag{15}
$$
原配对对称且 $\Gamma$ 不变，故
$$
 t_{p-d}=t_d,\qquad
 \sum_{d=0}^{p-1}t_d=0,\qquad
 t_0=-2\sum_{d=1}^g t_d .
 \tag{16}
$$
因为 $\operatorname{Tr}_\Gamma(z\tau^dz)$ 被原反射固定，全 $F/\mathbb Q$ 迹给
$$
 t_d=2\operatorname{Tr}_\Gamma(z\tau^dz).
$$
式 (6) 因而准确成为
$$
 \boxed{\quad
 \mathcal E_r=\frac1{(2r)!}
                   \sum_{d=1}^g\kappa_d^r t_d
                   \qquad(1\le r\le g).
 \quad}
 \tag{17}
$$
这里的 $2$ 与 $d,p-d$ 两项准确抵消，没有删掉任何一个 $p$ 完成。

令 $M_{rd}=\kappa_d^r/(2r)!$。其行列式为
$$
 \det M=
 \left(\prod_{r=1}^g\frac1{(2r)!}\right)
 \left(\prod_{d=1}^g\kappa_d\right)
 \left(\prod_{1\le d<d'\le g}(\kappa_{d'}-\kappa_d)\right).
 \tag{18}
$$
模 $p$ 时 $\kappa_d=-d^2$；$1\le d\le g$ 给两两不同的非零平方。因此
$$
                         M\in\operatorname{GL}_g(\mathbb Z_p).
 \tag{19}
$$

所以全部能量向量 $(\mathcal E_1,\ldots,\mathcal E_g)$ 与同一个原 Gram 的半行 $(t_1,\ldots,t_g)$ 是共同的整单位变换；在每个模 $p^N$ 精度都可双向恢复。再由 (16) 恢复 $t_0$，即可恢复所有
$$
                T(\tau^iR,\tau^jR)=t_{j-i\bmod p}.
 \tag{20}
$$
$R,\tau R,\ldots,\tau^{p-2}R$ 是 $OR$ 的 $\mathbb Z_p$ 基，所以对应的 $(p-1)\times(p-1)$ 主子矩阵正是原配对的整 Gram。完整 $p\times p$ circulant 只多出已知的 $N_\Gamma R=0$ 关系。没有将一组未知新点当作独立源。

特别，全部 Gram 条目生成的值理想准确等于全部能量生成的理想：
$$
 (\,T(P_1,P_2):P_1,P_2\in OR\,)
              =(\mathcal E_1,\ldots,\mathcal E_g)\subset\mathbb Z_p .
 \tag{21}
$$

## 5. 原整配对的全部 Smith 指数

**定理 1。** 写
$$
 n=2k-1=e v+t,\qquad 0\le t<e .
 \tag{22}
$$
由于 $n$ 为奇数、$e$ 为偶数，实际上
$$
                  t\in\{1,3,\ldots,e-1\}.
 \tag{23}
$$
原 $OR$ 上配对 (3) 的非零 Smith 因子准确为
$$
 \boxed{\quad
      p^v\text{ 重 }e-t,\qquad
      p^{v+1}\text{ 重 }t .
 \quad}
 \tag{24}
$$

**证明。** 由
$\Phi_p'(\zeta_p)=p\zeta_p^{-1}/(\zeta_p-1)$，
$O/\mathbb Z_p$ 的 different 为
$$
                 \mathfrak D_{K/\mathbb Q_p}
                       =\varpi^{e-1}O .
$$
对于普通迹配对，$O$ 的对偶是 $\mathfrak D^{-1}$。在 (4) 中，$*$ 是整单位基变换；标量 $2c_0/p$ 将源 $O$ 送到 $\mathfrak D^{-1}$。因此配对映射的 cokernel，作为 $\mathbb Z_p$ 模，准确同构于
$$
 \frac{\mathfrak D^{-1}}{(2c_0/p)O}
       \simeq O/\varpi^{\,2k-1}O .
 \tag{25}
$$
因为 $k\ge1$，这是整配对的有限 cokernel，绝非从非整 Fourier 基得到的假整格。

在 $O/\varpi^{ev+t}O$ 的逐 $p$ 商中，前 $v$ 层维数是 $e$，下一层维数是 $t$，之后为零；这里用 $pO=\varpi^eO$，只差一个单位。因此其 $\mathbb Z_p$ elementary divisors 正是 (24)。$\square$

由 (21)、(24)，
$$
 \boxed{\quad
 v=\min_{1\le r\le g}v_p(\mathcal E_r)
     =\left\lfloor\frac{2k-1}{p-1}\right\rfloor
     =\left\lfloor\frac{k-1}g\right\rfloor .
 \quad}
 \tag{26}
$$
某些 $\mathcal E_r$ 可以准确为零，按赋值 $+\infty$ 处理；全部不可能同时为零，因为 (25) 的配对非退化。

模 $p$ Gram 的秩 $\rho$ 准确为
$$
 \rho=
 \begin{cases}
     p-2k,&1\le k\le g,\\
     0,&k\ge g+1.
 \end{cases}
 \tag{27}
$$
特别 $\rho=0$ 时，只能得到 $k\ge(p+1)/2$，不能反向给 $k$ 或全局指数 $a$ 一个上界。

## 6. 首个最低赋值能量准确恢复任意 k

**定理 2（完整有限读出）。** 令 $v$ 如 (26)，并置
$$
 r_0=\min\{\,1\le r\le g:v_p(\mathcal E_r)=v\,\}.
 \tag{28}
$$
则准确有
$$
 \boxed{\qquad
       r_0=\frac{t+1}2,\qquad
       k=g v+r_0 .
 \qquad}
 \tag{29}
$$

**证明。** 将 (22) 重写为 $2k-ev=t+1=2r_*$，其中
$r_*=(t+1)/2\in\{1,\ldots,g\}$。由 (4)，
$$
 c_v=\frac{c_0}{p^v},\qquad
 v_\varpi(c_v)=2r_*,
 \qquad c_v=D^{r_*}a_v,\quad a_v\in O^\times .
 \tag{30}
$$
所有除 $p^v$ 后的能量都整，已由 (26) 或整 Gram 的共同因子证明。

若 $r<r_*$，(14) 的每个 $c_vD^{-j}$ 都在 $\varpi O$ 中。对于任意 $y\in O$，
$$
       \operatorname{Tr}_{K/\mathbb Q_p}(y)
                         \equiv-\bar y\pmod p .
 \tag{31}
$$
事实上所有 $p-1$ 个共轭模 $\varpi$ 相同，迹在 $\mathbb Z_p$ 中，而
$\varpi O\cap\mathbb Z_p=p\mathbb Z_p$。因此
$$
                     p^{-v}\mathcal E_r\equiv0\pmod p
                                \qquad(r<r_*).
 \tag{32}
$$
在 $r=r_*$ 时，仅最高项 $j=r_*$ 能留下非零剩余类。由 (12)、(31)，
$$
 \boxed{\quad
 p^{-v}\mathcal E_{r_*}
    \equiv(-1)^{r_*}\,\overline{a_v}\ne0\pmod p .
 \quad}
 \tag{33}
$$
这证明 $r_0=r_*$，从而得到 (29)。对于 $r>r_*$，无需将可能非整的各个迹项分别约化；共同整性已经足够。$\square$

在第一精度层 $v=0$，若 $k\le g$，则 $r_0=k$。此时
$c_0=qq^*=(-1)^kD^kuu^*$，所以
$$
 \mathcal E_1,\ldots,\mathcal E_{k-1}\equiv0\pmod p,\qquad
                       \mathcal E_k\equiv\bar u^{\,2}\ne0\pmod p .
 \tag{34}
$$
惰性情形的原反射保证 $\bar u^2\in\mathbb F_p^\times$；它可以是非平方，但绝非零。式 (34) 对两种真实完成都适用。

(29) 同时处理任意深的 $k$，包括模 $p$ Gram 秩为零的全部情况。它不把“某个能量非零”误作“前两个能量中有单位”。

## 7. 原全局有理参数的任意精度实现

以上证书不用无限精度对数作为黑箱。取 R161 的原奇参数
$$
 u_{17}=-x/y,\qquad
 u_{389}=-2x/(2y+1).
 \tag{35}
$$
在原好约化模型上，其不变微分有
$$
 \omega=\left(\sum_{m\ge0}\beta_{2m}u^{2m}\right)du,\qquad
 \beta_0=1,\quad \beta_{2m}\in\mathbb Z_p\cap\mathbb Q .
 \tag{36}
$$
系数整来自整形式群的不变微分；只出现偶次幂来自
$u(-P)=-u(P)$ 与 $[-1]^*\omega=-\omega$。故
$$
       \log_E(P)=\sum_{m\ge0}\frac{\beta_{2m}}{2m+1}u(P)^{2m+1},
 \qquad
       v_p\!\left(\frac{\beta_{2m}}{2m+1}\right)
                                  \ge-v_p(2m+1).
 \tag{37}
$$
这证明所用分母界，没有假定形式对数本身系数全整。

对整数 $N\ge0$，定义同一个全局代数点上的有限有理表达式
$$
 z^{[N]}(P)=\frac1p\sum_{m=0}^{N}
               \frac{\beta_{2m}}{2m+1}u(P)^{2m+1}.
 \tag{38}
$$
它只用奇参数次数至多 $2N+1$。在 $P=R$ 的每个 $p$ 完成，
$u(R)\in p\mathcal O$。对每个省略的奇数 $j\ge2N+3$，
$$
 v_p\!\left(\frac{\beta_{j-1}u(R)^j}{pj}\right)
       \ge j-1-v_p(j)\ge\frac{j-1}2\ge N+1 .
 \tag{39}
$$
中间不等式来自 $p\ge3$ 时 $v_p(j)\le(j-1)/2$：若
$v_p(j)=a\ge1$，则 $j\ge3^a\ge2a+1$。因此准确有
$$
 \boxed{\quad
 z^{[N]}(R)\in\mathcal P,\qquad
 z^{[N]}(R)-z\in p^{N+1}\mathcal P .
 \quad}
 \tag{40}
$$
所以 $2N+1$ 的明确截断成本不但支付模 $p^N$，还支付模 $p^{N+1}$。$N=0$ 的原奇参数已经足以首层测试；R164 给出的 $p^2$（E17 的 $p^4$）更强误差与此相容。

令
$$
 I_{r,N}=\frac1{(2r)!}\sum_{j,l=0}^{p-1}
       \kappa_{\,j-l\bmod p}^{\,r}\,
       z^{[N]}(\tau^jR)z^{[N]}(\tau^lR),
                    \qquad1\le r\le g .
 \tag{41}
$$
该表达式在 $\Gamma$ 下不变。$z^{[N]}$ 是奇有理函数，故由
$cR=-\tau^hR$ 和对称核，它也在 $c$ 下不变。因此
$$
 I_{r,N}\in\mathbb Q\cap\mathbb Z_p,\qquad
                    I_{r,N}\equiv\mathcal E_r\pmod{p^{N+1}} .
 \tag{42}
$$
第二式由 (40) 和整二次式 (6) 直接得到；$(2r)!$ 在全部所用范围都是单位。

这里没有声称 $N_\Gamma z^{[N]}(R)=0$ 是特征零等式。它只在相应精度成立；本文对有限截断仅使用 (42)，不会以假精确范数零删除群环边界项或补造 $t_0$。

于是有一个必终止的有限程序：

1. 从 $N=0$ 开始，以 (38)、(41) 计算所有 $I_{r,N}\bmod p^{N+1}$。
2. 若全部为零，增加 $N$。
3. 第一次不全为零时必有 $N=v$。取最小的 $r$ 使
   $p^{-N}I_{r,N}\not\equiv0\pmod p$；它就是 $r_0$。
4. 输出准确的 $k=gN+r_0$，以及 (24) 的全部 Smith 指数。

终止来自原非扭点的 $k<\infty$ 与 (26)，并非预先假定目标两量中有一个单位。程序保留原全部共轭点、完成和同一个 $D_pQ$。

## 8. 与原两步 Sha 门及真实全局指数的关系

由 (27)、(29)、(34)，
$$
 \boxed{\quad
 (\mathcal E_1,\mathcal E_2)\not\equiv(0,0)\pmod p
 \iff k\le2
 \iff \operatorname{rank}_{\mathbb F_p}(T\bmod p)\ge p-4
 \iff v=0,\ r_0\le2 .
 \quad}
 \tag{43}
$$
这准确保留 R130/R161 的原半局部第二增广测试。

若原实际全局指数满足
$$
 Q=\delta^aS,\qquad
 \delta=\tau^{(p-1)/2}(\tau-1),\qquad S\in A(F),
$$
则对 $S$ 使用同一个 formalizer，R164/R172 给
$$
                    k=a+k_S,\qquad k_S\ge1 .
 \tag{44}
$$
故完整读出还给一个实际有限上界
$$
                          a\le g v+r_0-1.
 \tag{45}
$$
当 (43) 成立时，$a\le1$，并在原 R125/R146/R156 的各自已付假设下推出原
$\Sha(E/\mathbb Q)[p^\infty]=0$。

若只知道模 $p$ Gram 秩 $\rho>0$，则
$a\le(p-\rho-2)/2$；若 $\rho=0$，该式不能用作上界，须继续
(38)–(42) 的真实精度。也不能从 (45) 反向认定局部深度全部来自全局 $a$：
$k_S-1$ 是原始 Mordell–Weil 点的局部整指数，仍单独存在。

本篇给出了同一个原 Heegner 点的全深度有限证书及完整整格识别。
**尚未支付的跨素数输入仍是：在 O4 已构造的同一联合无穷集合上，
无穷多个素数的该证书首个非零精度为零，且首个非零位置不超过二。**
非扭性保证有限程序终止，不保证这个指定早期位置；一般高度非退化、
别处 CM 极点或已知 Selmer 长度也不替代它。

## 9. 依赖

- [R130：原全部完成的 formalizer 与第二增广测试](R130-semilocal-formal-parameter-second-augmentation-test.md)。
- [R161：原循环二次不变量与全局有理参数](R161-integral-cyclic-invariants-and-actual-second-moment.md)。
- [R164：真实全局 delta 原像与整深度](R164-global-delta-preimages-and-cyclic-energy-depth.md)。
- [R168：同一 Heegner 配对的高度变化](R168-cyclic-energies-and-heegner-height-variation.md)。
- [R172 的完整证明](../notes/2026-11-12-norm-one-height-variation-nondegeneracy.md)，特别 §§2–3、6–7 的原半局部格、自对偶正规整基、Fourier 迹及不同理想。

(7)–(45) 的新增周期差分、完整 Smith、Vandermonde、首层位置和有限精度成本均在本文直接证明。它们不调用新的非零定理或泛化曲线模型。
