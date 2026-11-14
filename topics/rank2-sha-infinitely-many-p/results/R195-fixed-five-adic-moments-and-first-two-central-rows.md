# R195. 固定五进矩与原前两条中央行的统一独立性

日期：2026-11-12。**状态：以下共同五进整测度、质量零、
无限矩赋值与前两行独立性已证明。** 本篇单独支付辅助素数
$5$ 的范围；不把 R155 的 $p\ge13$ 假设直接外推，也不把
$E_{17}$ 在 $5$ 处的异常约化当作非异常。

## 1. 原对象与准确结论

始终使用 R162 的同一个有理平面
$$
 A(w)=A_2(z),\qquad B(w)=B(z),\qquad w=z^4,
 \qquad A=w+\cdots,\quad B-A=-22w^2+\cdots .
 \tag{1}
$$
在共同 $E_0:y^2=x^3-x$、$\omega_0=dx/(2y)$ 尺度上，
$$
 A=\vartheta^{68}P(s),\qquad B=\vartheta^{68}Q(s),
 \qquad s=u^4,\quad u=x^{-1/2},\quad \vartheta=\sigma/u .
 \tag{2}
$$
其中 $5P,5Q\in\mathbb Z[s]$，并保留原 $1/5$ 常数。
记
$$
 H_{A,m}=m![z^m]A_2(z),\qquad H_{B,m}=m![z^m]B(z).
 \tag{3}
$$

**定理。** 对每个正整数 $r$，
$$
 \boxed{\begin{aligned}
 v_5(H_{A,4r})&=v_5(H_{B,4r})=v_5(r),\\
 v_5\!\left(
 H_{A,4r}H_{B,8r}-H_{B,4r}H_{A,8r}
 \right)&=1+3v_5(r).
 \end{aligned}}
 \tag{4}
$$
因此原有理行
$$
 R_s^{(r)}=([w^{rs}]A,[w^{rs}]B)
 \tag{5}
$$
的 $R_1^{(r)},R_2^{(r)}$ 对所有 $r\ge1$ 都线性独立。
R190 的首次两个真实中央秩跳因而准确是
$$
                         \boxed{a=1,\qquad b=2.}             \tag{6}
$$
这不使用任何目标素数处的中央失败假设。

## 2. 辅助素数 5 处的真实共同整测度

### 2.1. 固定 sigma、theta 与唯一分母

在 $E_0$ 的整正式参数 $t=-x/y$ 中，R38 的 CM 唯一性证明
适用于每个好普通素数 $q>3$，包括 $q=5$：
$$
 \Sigma(t)=\sigma(\log_{E_0}t)\in t\mathbb Z_5[[t]],
 \qquad D^2\log\Sigma=-x,\qquad \Sigma(it)=i\Sigma(t).
 \tag{7}
$$
这里的外部输入准确为 Blakestad–Grant **2023**，
Theorem 8、Remark 11、Theorem 30：普通整 sigma 的存在唯一性。
原文的假设是 $q>3$、好普通约化；没有非异常条件。
对本曲线，$i\in\mathbb Z_5$ 使常数修正 $c$ 同时变成 $-c$，
唯一性遂迫使 $c=0$，所以这确实是原固定复 sigma 的有理
形式级数，未换成另一二次正规化。

由
$$
 x(t)=\frac{1+\sqrt{1+4t^4}}{2t^2}
$$
可知
$$
 u(t)=x(t)^{-1/2}\in t+t^5\mathbb Z_5[[t^4]],\qquad
 \frac{\Sigma(t)}{u(t)}\in1+t^4\mathbb Z_5[[t^4]].
 \tag{8}
$$
后一商正是 (2) 的 $\vartheta$：它首项一，并满足
$\vartheta^2=x\sigma^2$。因此 (2) 给
$$
 5A_2(\log_{E_0}t),\quad 5B(\log_{E_0}t)
                         \in\mathbb Z_5[[t]].                 \tag{9}
$$
这里只清除一个固定 $5$；没有断言原 $A_2,B$ 的全部
Amice 系数已经五进整。

令 $\mathcal O=\widehat{\mathbb Z_5^{\,\mathrm{ur}}}$。
在同一个普通正式群中选整同构
$$
 t=\exp_{E_0}(\Omega_5\log(1+T)),
 \qquad \Omega_5\in\mathcal O^\times .
 \tag{10}
$$
由 (9)，
$$
 5A_2(\Omega_5\log(1+T)),\qquad
 5B(\Omega_5\log(1+T))
 \tag{11}
$$
对应两个范数至多一的 $\mathcal O$ 值 Amice 测度
$\widetilde\mu_A,\widetilde\mu_B$，准确有
$$
 \int_{\mathbb Z_5}x^m\,d\widetilde\mu_F
       =\Omega_5^m\,\widetilde H_{F,m},\qquad
 \widetilde H_{F,m}=5H_{F,m}.
 \tag{12}
$$
同一 $\Omega_5$ 保留在所有矩中。

### 2.2. 曲线尺度与单位质量零

实际原曲线截面记为 $S_{17},S_{34}$，共同 $E_0$ 尺度上
未经 $[2]$ 缩放的第一条截面记为 $A_0$，故
$A_2(z)=A_0(2z)/16$。既有准确尺度式是
$$
 S_{17}(z)=17^{-1}A_0(17^{1/4}z),\qquad
 S_{34}(z)=34^{-2}B(\sqrt{34}\,z).
 \tag{13}
$$
两个根可取在有限未分歧五进扩张中，都是单位。
相容选取
$$
 \Omega_5=17^{1/4}\Omega_{17,5}
          =\sqrt{34}\,\Omega_{34,5}.
 \tag{14}
$$
例如 (13)–(14) 直接给级数恒等式
$$
 A_0(\Omega_5\log(1+T))
 =17S_{17}(\Omega_{17,5}\log(1+T)).
 \tag{15}
$$
这里没有把可能不属于 $\mathbb Z_5$ 的 $17^{1/4}$ 当成
$\mathbb Z_5$ 上测度的乘法推前。真正的 $A_0\mapsto A_2$
则是合法的 $[2]_*/16$，它保持单位区间并把质量乘 $1/16$。
$B$ 的比较常数为 $34^2$，也为五进单位。

现在独立证明原单位质量为零。两曲线在 $5$ 处均好普通，
但准确迹为
$$
 a_5(E_0)=-2,\qquad a_5(E_{17})=-4,\qquad
 a_5(E_{34})=-2 .
 \tag{16}
$$
所以 $E_{17}$ 的确异常：$a_5\equiv1\pmod5$。
本段不调用 R40/R118 的非异常 Selmer 控制定理。

Agboola–Howard **2006**，Theorem 2.1.1，在 $q>3$ 好普通处
插值无穷型 $(k,j)$ 满足 $0\le-j<k$ 的字符。因此中心
$(1,0)$ 本就在其范围内，中心 Katz 值等于非零周期因子、
有限 Euler 因子与 $L(E,1)$ 的乘积。R51/R115 的原复平方
公式在 $m=0$，结合 $S_{17}(0)=S_{34}(0)=0$，给
$$
 L(E_{17},1)=L(E_{34},1)=0 .
$$
于是各实际中心 Katz 值都是零。这里不要求 Euler 因子为
单位；异常性不会把零值变成非零值。

还须把这个中心值与**单位质量**连接，不能只用截面总质量。
令 $\nu_E$ 是 $S_E(\Omega_{E,5}\log(1+T))$ 的原有界测度，
并记
$M_{E,m}=\int_{\mathbb Z_5}x^m\,d\nu_E$。
R46/R118 的正权平方插值在 $q=5$ 同样成立：它只用
Katz 插值、固定复平方恒等式与有界性，不用非异常性。
准确地，对 $m>0,\ 4\mid m$，
$$
 \mathscr F_E(6^m-1)
 =c_E\,b_E^m
 \left(1-\frac{\pi_E^m}{\bar\pi_E^{m+1}}\right)^2M_{E,m}^2,
 \qquad c_E\ne0,\quad b_E\in\mathcal O^\times .
 \tag{17}
$$
在原规范中可取 $b_{17}=136$、$b_{34}=68$，实际都属于
$\mathbb Z_5^\times$（不只是一般的 $\mathcal O^\times$）；
$c_{17}=57800f_{17}\Omega_{17,5}$，
$c_{34}=\kappa_{34}68\Omega_{34,5}$。
这些固定常数只要求非零，允许有限的 $5$ 分母或正赋值。

取 $m_n=4\cdot5^n$。单位区间的 $x^{m_n}$ 一致趋于一，
非单位矩的赋值至少 $m_n-O(1)$，而 (17) 的 Euler 修正
亦趋于一。由 $b_E\in\mathbb Z_5^\times$，其四次幂在
$1+5\mathbb Z_5$ 中，故 $b_E^{m_n}\to1$；另有
$6^{m_n}-1\to0$。于是直接取
极限得到
$$
 0=\mathscr F_E(0)=c_E\,\nu_E(\mathbb Z_5^\times)^2 .
$$
特征零且 $c_E\ne0$，所以原两条单位质量均为零。
再用 (13)–(15)、$[2]_*/16$ 及固定乘数 $5$，严格得到
$$
 \boxed{\qquad
 \widetilde\mu_A(\mathbb Z_5^\times)
 =\widetilde\mu_B(\mathbb Z_5^\times)=0.
 \qquad}                                                     \tag{18}
$$
这只取了完整正权插值的一个极限，没有在非单位区间定义
$5^t$ 的解析延拓，也没有预设任何未知中央导数非零。

## 3. 原低权整数证书

R57 的无分母 Hurwitz 流为
$$
 u'=v,\quad v'=-2u^3,\quad L'=u^2,\quad
 \vartheta'=L\vartheta,\qquad
 (u,v,L,\vartheta)(0)=(0,1,0,1).
 \tag{19}
$$
代入 (2)，准确得到
$$
 \begin{array}{c|rr}
 m&H_{A,m}&H_{B,m}\\ \hline
 4&24&24\\
 8&1042944&155904
 \end{array}
 \tag{20}
$$
原行列式是
$$
 \Delta_0=24(155904-1042944)
          =-21288960,\qquad
 v_5(\Delta_0)=1,\qquad \Delta_0/5\equiv3\pmod5 .
 \tag{21}
$$
四个原矩都是五进单位。因此把两个函数都乘 $5$ 后，
四个 $\widetilde H$ 的赋值均为一，而
$$
 v_5\det\begin{pmatrix}
 \widetilde H_{A,4}&\widetilde H_{B,4}\\
 \widetilde H_{A,8}&\widetilde H_{B,8}
 \end{pmatrix}=3.                                            \tag{22}
$$
两行各乘一次 $5$，所以行列式的成本是两层，不是一层。

随附脚本使用 (19) 的整数流，并独立以 R162 的有理
$s$ 级数和真正 $w(s)$ 反演核对 $w^0,w^1,w^2$。
$A_2$ 还与 R57 的实际六因子乘积按 $2^{m-4}$ 缩放校准。
(16) 的三个有限域点数也直接枚举。没有输入中心导数值。

## 4. 全部正整数 r：整差商而非样本外推

把 R193 §§2–4 的通用引理用于 (12)、(18)，取 $q=5$。
其实际解析单位矩是
$$
 \widetilde J_F(t)=
 \int_{\mathbb Z_5^\times}
             \exp\!\left(t\log(x^4)\right)d\widetilde\mu_F .
 \tag{23}
$$
常数项为零，$t^k$ 系数的赋值至少 $k-v_5(k!)$。
所以 $\widetilde J_F(t)/(5t)$ 是整 Tate 函数，其线性系数
在 $5\mathcal O$，所有二次及以上系数在 $25\mathcal O$。
(22) 使两行的实际整差商在除一次 $5$ 后为单位。

对正整数 $t$，完整矩与 (23) 的差准确属于
$5^{4t}\mathcal O$。不等式
$4t>2+2v_5(t)$ 使行列式误差严格深于主项。于是该引理给
$$
 \begin{aligned}
 v_5(\widetilde H_{F,4r})&=1+v_5(r),\\
 v_5\det(\widetilde H_{4r},\widetilde H_{8r})
                         &=3+3v_5(r).
 \end{aligned}
$$
分别除回一次及两次固定 $5$，即为 (4)。
因此 (6) 现在是无例外的统一行号结论。

## 5. 目标惰性 p 处的准确两层成本

取 R189 的目标惰性素数 $p=4r-1\ge7$，排除 $p=11$。
令
$$
 \Delta_p
 =H_{A,p+1}H_{B,2p+2}-H_{B,p+1}H_{A,2p+2}\ne0 .
 \tag{24}
$$
因为 $v_p((p+1)!)=1$、$v_p((2p+2)!)=2$，
R190 的首次两行等式准确成为
$$
 \det(q_1,q_2)=\omega_2\det(R_1^{(r)},R_2^{(r)}),\qquad
 v_p\det(q_1,q_2)=v_p(\Delta_p)-2 .
 \tag{25}
$$
这里 $v_p(\omega_2)=1$；没有漏掉原两个阶乘。

如果两个完整中央导数都为零，R185 给 $q_1\in p\mathbb Z_p^2$、
$q_2\in p^2\mathbb Z_p^2$，故
$$
 Q'=\begin{pmatrix}p^{-1}q_1\\p^{-2}q_2\end{pmatrix}
 \in M_2(\mathbb Z_p),\qquad
 e'=v_p\det Q'=v_p(\Delta_p)-5\ge0.                           \tag{26}
$$
特别第一原行必须在 $p\mathbb Z_p^2$，且
$v_p\det(R_1,R_2)\ge2$。本篇不以固定辅助位的 (4)
替代这些随 $p$ 变化的赋值条件。

由原整数流，$25\Delta_p$ 是非零整数；固定 theta 增长界和
Cauchy–Stirling 估计给
$$
 \log\max(1,|5H_{F,m}|)
       \le\frac m2\log m+O(m).
$$
对 (24) 的两个次数相加，得到
$$
 \boxed{\qquad v_p(\Delta_p)\le
                      \left(\frac32+o(1)\right)p.\qquad}      \tag{27}
$$
常数只依赖原两条函数；有限小素数可另吸收到固定常数倍 $p$。
这比 R193 的六行窗口缩小了次数成本，但仍不是目标 $p$
上的单位性。

以下读取原源时取 $D\ge1$、所需精度 $K\ge1$。
若 $Q'$ 的 Smith 指数为 $\kappa'_1\le\kappa'_2$，
则 $\kappa'_1+\kappa'_2=e'$。R189 的联合 Hasse 源恢复
最大非零 Smith 指数准确为
$$
                    \kappa'_2+\lfloor\log_pD\rfloor.          \tag{28}
$$
在同篇的带号规范中，置
$t_D=\lfloor2(D-1)/r\rfloor$。因只需 $N=1,2<p$，
全部 Hasse 行的额外读取成本为
$$
 \epsilon_{\rm all}(D,2)
       =t_D+\left\lfloor\frac{D+t_D}{p-1}\right\rfloor .
 \tag{29}
$$
所以，要由未除 $p$ 的实际加权 core 恢复原非常数系数
模 $p^K$，足够的共同精度是
$$
 K+\kappa'_2+\lfloor\log_pD\rfloor+3+
 t_D+\left\lfloor\frac{D+t_D}{p-1}\right\rfloor .
 \tag{30}
$$
其所用原 Cartan 矩形可限为
$i\le D-1,\ l\le2r+2D-2$。这是准确的输入 core 到原源
的逆成本；仍须把输入 core 与同一个完整曲线前缀的真实
观测比较，不能把 (30) 直接算作最终饱和 jet 的净收益。

## 6. 依赖、原始来源与复算

- [R38 的普通 sigma 原证明](../notes/2026-11-12-fixed-sigma-height-and-inert-denominator.md)，
  §1 的命题明确包含每个好普通 $q\ge5$。
- Clifford Blakestad、David Grant，*On the universal p-adic sigma
  and Weierstrass zeta functions*，J. Number Theory **249** (2023)，
  348–376：Theorem 8、Remark 11 在印刷页 357；
  Theorem 30 在印刷页 373。
  [作者提供的出版全文](https://euclid.colorado.edu/~grant/publications/P_adic_sigma_function-published)。
- Adebisi Agboola、Benjamin Howard，*Anticyclotomic Iwasawa theory
  of CM elliptic curves*，Ann. Inst. Fourier **56** (2006)，1001–1048：
  $q>3$ 好普通的总假设在印刷页 1002；
  Theorem 2.1.1、式 (2.2) 在印刷页 1016，含 $(k,j)=(1,0)$。
  [正式出版全文](https://www.numdam.org/article/AIF_2006__56_4_1001_0.pdf)。
- [R51 的原全部权平方公式](R51-explicit-theta-section-and-central-square-constant.md)、
  [R115 的第二实际截面及平方公式](R115-e34-explicit-degree68-theta-section.md)、
  [R118 完整平方插值证明 §4](../notes/2026-11-12-e34-rank-two-and-central-slope-criterion.md)。
  本篇在 $5$ 处只使用这些解析恒等式，不使用其非异常 Selmer 判据。
- [原两个曲线尺度](../notes/2026-11-12-two-rank-two-theta-linear-convolution.md) §3；
  [R162 的准确 P、Q](R162-actual-theta-plane-nonlinear-flow-and-lagrange-jets.md)。
- [R193 的通用整差商引理](R193-fixed-ordinary-moments-and-six-central-rows.md)；
  [R185 的实际完整中央权](R185-integral-axis-stokes-functional-and-complete-central-tests.md)、
  [R190 首次跳跃等式](R190-central-projection-of-square-theta-sections.md)、
  [R189 完整 Hasse 与 core 成本](R189-complete-central-hasse-families-and-weighted-core.md)。
- [固定五进低权校准脚本](../scripts/check-fixed-five-adic-central-minor.py)。

本篇严格缩短了每个目标素数所需的原中央窗口，并给其确定的
恢复成本；两个完整中央导数的跨素数非同时消失仍待证明。
