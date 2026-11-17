# R642：规范化 pulse 前缀的连续圆柱图嵌入

作者：Astra-larger-parallel-16f63c8b（GPT-6 Astra Pro，AI辅助），2026-11-17。

**已证明。** 对下述固定精确共同五次场，全部818胞的有向区间计算给

$$
.998<\lambda<1.002,\qquad |\lambda_s|<.04,\qquad C_G>.1645.
$$

因此已登记的同一规范化 pulse 前缀是整个 $[0,1]\times S^1$ 上的 C² 嵌入。结论使用与 R638/R640 相同的标准 IEEE binary64 基础运算假设，覆盖全部径向位置和角度；它不认证闭面、度量误差、曲率、reach 或全弯曲参数族。

## 1. 固定对象

沿用 [R640](R640-certified-cylindrical-embedding-of-the-pulse-prefix.md) 的同一未规范化场 $F$：M320、$s\in[0,1]$、819个节点、818个唯一 Hermite 五次胞元。完整保存的 binary64 节点和0/1/2jet均作为精确实数；没有用新 RHS 重算旧段二jet。输入压缩文件 SHA256 为 `26e53e8cdbdf6205a8bd9b2976cd4bcd36ad8734b0aca69512d705d826c5af72`，x/Y/D/DD 的 little-endian float64 绑定为 `840193a1cdb37f79d04f5f36f5a0c485c4eb50f3fd2a103af8c4c267d5232793`。

固定构造角数 $N=4096$，$\phi_j=2\pi j/N$，令

$$
q_j(s)=|F_\phi(s,\phi_j)|,\quad
b(s)=N^{-1}\sum_{j=0}^{N-1}q_j(s),\quad
c(s)=(0,0,Z_0(s)),\quad \lambda(s)=a(s)/b(s).
$$

这里 $Z_0$ 是旋转坐标中 $Z$ 的常数 Fourier 系数。$a$ 是既有声明的精确 C² 标量：旧节点的精确有理 Hermite，接以相同 .99 精确末节点为初始 jet 的解析弧及 pulse 曲率积分。有限 Gauss 或浮点 Profile 返回值不是本证明的标量定义。

本条证明的是已登记规范化像

$$G(s,\phi)=c(s)+\lambda(s)(F(s,\phi)-c(s)),$$

以及 [R638](R638-global-positive-arclength-coordinates-for-two-prefixes.md) 中同一构造角数的 $\widetilde F(s,\phi)=G(s,\psi(s,\phi))$。其中 $q_N=I_Nq$ 的均值准确等于上式的有限和 $b$，不是用连续速度积分替换该均值。

## 2. 把缩放变化实际计入图判据

沿用 R640 的 $Q=R^2+T^2$、$A=R d_T-Td_R$、$B=R V_T-TV_R$、$C=V_Z A-d_Z B$，其中 $d=F_\phi$、$V=F_s$ 均写在旋转坐标中。直接微分给

$$
Q_G=\lambda^2Q,\quad A_G=\lambda^2A,\quad B_G=\lambda^2B,
$$

$$
\boxed{C_G=\lambda^3C+\lambda^2\{(1-\lambda)c_s+\lambda_s(Z-c)\}A.}
\tag{1}
$$

公式中的 $c,c_s$ 在标量高度项内表示 $Z_0,Z_0'$。$\lambda_s$ 项必须保留；没有从有限采样显示的微小位移推断嵌入。

每个构造节点的 $q_j$ 严格正时，

$$
b_s=\frac1N\sum_j\frac{d(s,\phi_j)\cdot V_\phi(s,\phi_j)}{q_j(s)},\qquad
\lambda_s=\frac{a_s b-a b_s}{b^2}.
\tag{2}
$$

本次程序用整个径向子胞上的有向区间真实包围 (2)，包括分母和两项之间的相减，不用径向有限差分。

## 3. 精确标量的低成本全域包围

在 $[0,s_b]$、$s_b=$保存的 binary .99 上，geometry.knots 的每个 $a,a',a''$ 都视为精确有理数。首节点为 $s=0$，initial_law 的精确 jet 恰为 $(1,0,k_0)$，与保存值相同。每个标量胞元的六个五次 Bernstein 控制值及五个四次导数控制值由三jet向外计算；导数升为五次。它们的凸包覆盖全胞。一个几何子胞可能与多个标量胞相交，程序取所有相交标量胞的并集包围，未要求两种网格重合。

在 $[s_b,1]$，从保存的精确末节点定义

$$K=-a''(s_b)/\sqrt{1-a'(s_b)^2}.$$

有向计算验证 $3/2<K<7/2$。到保存的 .995 cut 之前曲率恒为 $K$；其后首 ramp 的基曲率在 $[3/2,K]$，负 pulse 是

$$-5\{S(t/w)-S(t/w-1)\},\qquad w=\text{binary } .005,$$

其中 $S$ 在 $[0,1]$ 外截为0或1，内为 $10u^3-15u^4+6u^5$。因 $S'=30u^2(1-u)^2\ge0$，花括号在 $[0,1]$ 内。故整个 $[s_b,1]$ 均有 $|\kappa|\le7/2$，继而 $|a''|=|\kappa\cos\alpha|\le7/2$。特别地这也覆盖 $1-(\text{binary } .995)>\text{binary } .005$ 的极小末段，不误当恰好处在 first-half 内。

记 $\Delta=s-s_b\ge0$。对任一子胞的 $\Delta$ 区间，严格使用

$$
a(s)\in a_b+a'_b\Delta+[-\tfrac74\Delta^2,\tfrac74\Delta^2],\qquad
a'(s)\in a'_b+[-\tfrac72\Delta,\tfrac72\Delta].
\tag{3}
$$

(3) 来自 Taylor 积分余项，与 Gauss 求积误差无关。它虽比 [R636](R636-certified-inward-reference-radius-and-length.md) 的精细积分法宽，仍足以支付本条嵌入预算。

## 4. 径向与全角连续覆盖

沿用 R640 的共同五次 Bernstein 和有向 FFT 方法。每个几何胞元作两次 midpoint de Casteljau，分成4个闭子胞；对每个子胞、全部4096个构造角节点，六个控制值的凸包同时包围 $R,T,d,V,V_\phi,Z-Z_0$。$c_s$ 则直接取导数常数系数的 Bernstein 凸包。

速度范数用有向平方、加法与平方根包围；$b,b_s$ 的有限和使用显式二叉树有向加法，再除精确4096。没有把 NumPy reduction 或库 FFT 的误差忽略。所有速度下端实际保持正，故 (2) 分母合法。

为覆盖角节点之间的全部角度，设 $g=(1-\lambda)c_s+\lambda_s(Z-c)$。由 (1)，

$$
(C_G)_\phi=\lambda^3C_\phi+\lambda^2gA_\phi
+\lambda^2\lambda_s Z_\phi A.
\tag{4}
$$

每个子胞已知的 $\lambda,\lambda_s,c_s$ 区间与整胞 Fourier 系数 l1/Bernstein 界，向上给出

$$
L_G=\Lambda^3 L_C+\Lambda^2\bigl(E L_A+\Lambda_1 U_{Z_\phi}U_A\bigr),
$$

其中 $\Lambda\ge|\lambda|$、$\Lambda_1\ge|\lambda_s|$、$E\ge|g|$；$L_C,L_A,U_{Z_\phi},U_A$ 按 R640 的旋转导数恒等式计算。由任意角距最近4096节点至多 $\pi/4096$，从 (1) 的区间网格下端再扣 $\pi L_G/4096$。该扣量和每一步浮点运算都向外舍入。这里仅对有限线性分量变换，乘积从未截断为4096角的 Fourier 多项式。

全部818胞实际运行438.26秒，得到：

| 连续量 | 有向包围 |
|---|---:|
| $\lambda$ | $[.9980897959430556,1.0019550909080441]$ |
| $\lambda_s$ | $[-.022858934970211887,.03711001447452569]$ |
| $C_G$ 的全域下界 | $.1645639919897565$ |
| 构造节点速度 $q_j$（全部 $s$）的下界 | $.16601843096426697$ |
| $|(C_G)_\phi|$ 的全域上界 | $150.17524437828803$ |

最后一胞 $[.9999843749999884,1]$ 的第四子胞是最差处：径向盒的角网格下界为 $.2797469618359191$，向上角覆盖损失为 $.11518296984616257$，向下相减得到表中严格全域下界。该子胞的 $\lambda$ 盒为 $[.9999209569589337,1.0002224495553422]$。角变换区间的最大宽度小于 $6.067\times10^{-9}$。

表中端点均表示输出 binary 数的精确值。以 Fraction 精确比较这些端点与 $.998,1.002,.04,.1645$，得到开头的保守有理不等式。构造节点的 $q_j$ 下界只用于有限均值及其导数；全角的 $q_N$ 正性继续调用 R638，没有把节点速度下界冒成全角下界。

## 5. 嵌入结论与范围

R640 已严格证明 $Q>.1872$、$A>.1770$ 和每条原圈的绕轴度数为1。本次实际 $\lambda>.998$、$C_G>.1645$ 给

$$Q_G>(.998)^2(.1872)>.1864,\qquad A_G>(.998)^2(.177)>.1762.$$

由于 $\beta_G=\beta_F$，度数仍为1且 $\partial_\phi\beta_G=A_G/Q_G>0$。并且

$$\partial_\phi\beta_G\,\partial_s Z_G-\partial_s\beta_G\,\partial_\phi Z_G=C_G/Q_G>0.$$

直接调用既有 [R9](R9-cylindrical-graph-global-embedding.md)，得到 $G$ 为整个带边前缀上的 C² 嵌入。R638 已支付 $\psi$ 为全域 C² 角坐标微分同胚，因此 $\widetilde F$ 也是同一像的 C² 嵌入。

这条结论不认证度量误差、曲率、reach、闭合或全弯曲参数族；没有把带边前缀当成 README 完成的闭曲面。所有这些条件保持待付。

## 6. 可复现来源

证书源 [normalized-graph-interval.py](../notes/2026-11-17-parallel-geometry-normalized-graph-interval.py)，SHA256：

~~~text
0e9185242c05893197332fb376ff06a277279cdfa00808e50a1553342a9c93e4
~~~

原有有向算术/变换唯一运行依赖为 [arclength_interval_positive.py](../scripts/parallel_20261117_arclength_interval_positive.py)，SHA256 `f512c96cbc1fb3896fc144c5e9d8d29aaa80e321d08d9cdbf1745beb54a5c57d`。标准 IEEE binary64 基础四则/平方根及 nextafter 的算术假设同 R638/R640。入口绑定原输入和该依赖，出口检查源及输入未变化。输出完整报告 SHA256 为

~~~text
b9813c624e47c05d6ad8cfb21ee026f9e12c83755e4e88f968748eba9a6784a6
~~~

复现时将 `$T` 换成本题目录，输入和输出保留仓库外：

~~~sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 python \
  "$T/notes/2026-11-17-parallel-geometry-normalized-graph-interval.py" \
  --topic "$T" --input /scratch/parallel-pulse-a5-complete-base.json.gz \
  --out /scratch/parallel-pulse-a5-normalized-graph-interval.json \
  --radial-subdivisions 4
~~~

原数据生成配方与父来源沿用 R638/R640；全部 raw 及逐胞输出不入库。只读核对另检查了本条新均值导数、缩放率、(4)、旧标量相交胞和跨 origin 的并集覆盖，未重审已有 FFT 基础。

另提供独立可导入 [normalization-interval-tools.py](../notes/2026-11-17-parallel-geometry-normalization-interval-tools.py)，SHA256 `a685b93e888e55e8b2dc4e0505e977a6ac0f2db88c18f2db2b5889d6a7dd02d8`。其 `ScalarEnvelope(I,data).at((slo,shi))` 返回同一 $a,a'$ 包围；`speed_mean_jets`、`scaling_jets` 返回有限均值及缩放的0/1/可选2jet，供后继真实曲率计算。该 helper 不在本次818胞证书的运行依赖中，也不自行声明曲率或 reach 证书。
