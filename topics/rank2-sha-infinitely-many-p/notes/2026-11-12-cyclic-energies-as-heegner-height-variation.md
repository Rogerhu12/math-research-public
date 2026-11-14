# 原循环二次量作为同一 Heegner 配对的 p 进高度变化

日期：2026-11-12。**已证明。** 本篇给 R161/R164 的两个实际
二次量一个全局高度解释，保留全部 p 完成、原类群与 U 的双重迹、
循环核和规范常数。它确实产生固定 weight 2 的高度生成级数；
该级数仍是未知二次量乘原 newform，尚未给无穷多个 p 的单位性。
这里不把复高度的正定性用于 p 进局部对数乘积。

## 1. 原点和循环核

使用 R130/R139/R146 的实际 E17 或 E389 输入。
$F$ 是原虚二次 Heegner 域，$L/F$ 是原次数 p 的环类子扩张，
$\Gamma=\langle\tau\rangle=C_p$，$p\ge7$。
取已经付清的反演对称整数群环 formalizer $D_p$，并记
$$
 R=D_pQ,\qquad
 z=\frac{\log_E R}{p}\in
 \mathcal P=\mathcal O_L\otimes\mathbb Z_p,\qquad
 N_\Gamma z=0 .
 \tag{1}
$$
原 $Q$ 已包含固定挠点消去和完整类群迹。
$R$ 在全部 p 完成属于形式群；即使 p 在 $L/F$ 完全分裂，
(1) 也保留全部完成。复共轭满足
$c\tau c=\tau^{-1}$、$cR=-\tau^eR$，其中 e 是原标记允许的平移。

对 $r=1,2$ 定义
$$
 \kappa_r(d)=\{d(p-d)\}^r,\qquad
 K_r=\sum_{d=0}^{p-1}\kappa_r(d)\tau^d ,
 \tag{2}
$$
其中 d 总取 $0,\ldots,p-1$。原对数二次量为
$$
 \mathcal E_r(z)
 =\frac1{(2r)!}\sum_{j,k=0}^{p-1}
     \kappa_r(j-k)\tau^jz\,\tau^kz
 =\frac1{(2r)!}\operatorname{Tr}_{L/F}(zK_rz).
 \tag{3}
$$
核满足 $\kappa_r(-d)=\kappa_r(d)$，所以循环平移和反射都保持 (3)。
由 $cR=-\tau^eR$ 得
$$
           \mathcal E_r(z)\in\mathbb Q_p,\qquad
 \operatorname{Tr}_{F/\mathbb Q}\mathcal E_r(z)=2\mathcal E_r(z).
 \tag{4}
$$
这里的迹是 p 半局部代数的迹，包含 F 在 p 的所有完成。

R161 的全局奇有理参数版本满足
$I_r^{\rm rat}\equiv\mathcal E_r(z)\pmod p$；
R164 实际给出差在 $p^2$，E17 还可加强到 $p^4$。
本篇使用 (1) 的确切对数 norm-zero 关系。
有理参数列的迹通常只有模 p 为零，不替代 (1)。

## 2. Coleman–Gross 自高度的规范与变化

固定定义于 $\mathbb Q_p$ 的 Néron 微分 $\omega$ 和 Hodge 补空间
$$
 H^1_{\rm dR}(E/\mathbb Q_p)
       =\mathbb Q_p[\omega]\oplus W_0 .
$$
令 $[\eta_0]\in W_0$ 为唯一满足
$$
                     [\eta_0]\cup[\omega]=1
 \tag{5}
$$
的类，并用只在 O 有二阶极点的第二类微分代表它。
对 $\lambda\in\mathbb Q_p$ 置
$$
 \eta_\lambda=\eta_0+\lambda\omega,\qquad
 W_\lambda=\mathbb Q_p[\eta_\lambda].
 \tag{6}
$$
每个 $W_\lambda$ 都是 Hodge 补空间；椭圆曲线的一维补空间自动
各向同性。ordinary 时可令 $W_0$ 为 unit-root 线，但本节变化
公式本身只需 good reduction。

所有高度均取相同的 $\omega$-对偶切向基点和相同切向规范。
Balakrishnan–Besser（2015）Theorem 4.1，在本文的 (5) 约定下给
未施加局部数域迹的自高度 Coleman 函数
$$
             \tau_\lambda(P)
                   =-2\int_O^P\omega\int_O^\bullet\eta_\lambda .
 \tag{7}
$$
切向正则化的共同项在差中消失。迭代积分的 shuffle 恒等式给
$$
  \tau_\lambda(P)-\tau_0(P)
   =-2\lambda\int_O^P\omega\int_O^\bullet\omega
   =-\lambda\{\log_E(P)\}^2 .
 \tag{8}
$$
因此自高度变化中没有额外的 2。

高度的主除子公式不依赖补空间，故两个局部高度之差下降为
$E$ 上的双线性配对。对 (8) 作带 $1/2$ 的 polarization，得到
$$
 \Delta_\lambda h^{\rm pre}_v(P,Q)
   :=h^{\rm pre}_{v,\lambda}(P,Q)-h^{\rm pre}_{v,0}(P,Q)
   =-\lambda\log_E(P)\log_E(Q).
 \tag{9}
$$
这里说的是**高度之差**下降为双线性配对；
不把单个局部自高度函数本身误说成群上的二次型。
若两除子支撑相交，使用相同切向规范后 (9) 仍成立。

## 3. 全局 cyclotomic 高度、全部完成和因子 2

对任意包含实际点的数域 M，本文使用**未除以 $[M:\mathbb Q]$**
的 Coleman–Gross cyclotomic 全局高度 $h^M_\lambda$。
idele class character 取范数到 $\mathbb Q$ 后的 p 进 cyclotomic
对数。在 $v\mid p$ 的局部线性泛函为
$\operatorname{Tr}_{M_v/\mathbb Q_p}$；其余地方的高度在 (6)
下不变。因此
$$
 \Delta_\lambda h^M(P,Q)
  =-\lambda\sum_{v\mid p}
      \operatorname{Tr}_{M_v/\mathbb Q_p}
      \bigl(\log_E(P_v)\log_E(Q_v)\bigr).
 \tag{10}
$$
这个未归一化约定还给出：若点已定义在 M 上，则
$$
          h^{M'}_\lambda(P,Q)
              =[M':M]h^M_\lambda(P,Q).
 \tag{11}
$$

在所有 p 完成都使用同一个定义于 $\mathbb Q_p$ 的 (6)。
特别是 p 在 F 分裂时，两处补空间变化使用**同号 $\lambda$**。
复共轭交换这两处，并把两个点各变成负的 Galois 平移；
双线性乘积的两个负号抵消。因此这种变化保持复共轭，
两处贡献相加。选择反号会是另一种 height variation，
不能用于下面的 cyclotomic 公式。

对 (10) 取 $M=L$、$P=R$、$Q=K_rR$，结合 (1)、(3)、(4)，
得到精确等式
$$
 \boxed{\quad
 \mathcal E_r(z)=
  -\frac{
    h^L_\lambda(R,K_rR)-h^L_0(R,K_rR)}
        {2\lambda p^2(2r)!},
              \qquad r=1,2,\quad\lambda\ne0 .
 \quad}
 \tag{12}
$$
分母中的 2 来自 $F/\mathbb Q$ 的迹，而非漏掉的 polarization。
取 $\lambda=1$ 时，$2(2r)!$ 在 $p\ge7$ 为单位；
(10) 同时证明分子实际被 $p^2$ 整除。
配对中的两个点是 $R,K_rR\in E(L)$，没有引入任意的局部原像。

## 4. 保留完整类群、U 以及双重 Heegner 迹

令 $H_\ell$ 为原完整环类域。
在已经建立的实际分裂中，记
$$
 V_0=C_\ell\times U,\qquad |V_0|=h_Fu=[H_\ell:L],
 \qquad
 Q=[t_0]\sum_{a\in V_0}P_\ell^a .
 \tag{13}
$$
这里 $P_\ell$ 是原 CM 点在固定 newform 椭圆商上的像，
已按共同 cusp 归零；$\Gamma$ 使用已付清的真实提升。
$D_p$ 与这些 Galois 作用交换。

由 (11) 以及高度的双线性，(12) 的分子准确展开为
$$
 \begin{split}
 \Delta_\lambda h^L(R,K_rR)
  =\frac{t_0^2}{h_Fu}
   \sum_{a,b\in V_0}\sum_{d=0}^{p-1}\kappa_r(d)\,
    \Delta_\lambda h^{H_\ell}
       (D_pP_\ell^a,D_pP_\ell^{b\tau^d}).
 \end{split}
 \tag{14}
$$
这是保留原 kernel 的 pair-of-Heegner 配对。
不能删去 U，也不能把双和换成一次全类迹。
系数 $1/(h_Fu)$ 来自未归一化高度的域扩张，
不是重新定义原 Q 的平均；双和本身含 $(h_Fu)^2$ 对。
R154 把 $C_\ell$ 吸收到固定映射中时，仍须按实际定义域
保留对应的 (11)。

$D_p$ 在 L 上 formalize R；它未必使每个
$P_\ell^a\in E(H_\ell)$ 分别进入形式群。
(14) 不要求后者：局部椭圆对数和全局高度均定义在这些实际点上，
只有 (1) 和 (12) 的整性使用了 R 的 formal 性质。

## 5. 确实存在的固定 weight 2 高度级数

取原 newform 椭圆商
$$
 \pi_J:J_0(N)\longrightarrow E,\qquad
 \pi_JT_n=[a_n(f)]\pi_J ,
 \tag{15}
$$
其中坏处也使用对应的标准 Hecke 算子。
在本节回到原 level N 商，避免把固定辅助 old level 的算子
无说明地当作 (15)。
令
$$
 Z_\ell=D_p[t_0]\sum_{a\in V_0}
                    ([x_\ell^a]-[\infty])\in J_0(N)(L);
 \qquad \pi_JZ_\ell=R .
 \tag{16}
$$
Hecke 算子与 Galois 作用交换，故
$$
 \begin{split}
 \mathcal Z_{r,\lambda}(q)
  &:=\sum_{n\ge1}
       h^L_\lambda(R,\pi_JT_n(K_rZ_\ell))q^n\\
  &=h^L_\lambda(R,K_rR)\,f(q).
 \end{split}
 \tag{17}
$$
从而
$$
 \boxed{\qquad
 -\frac{\mathcal Z_{r,\lambda}-\mathcal Z_{r,0}}
               {2\lambda p^2(2r)!}
             =\mathcal E_r(z)\,f .
 \qquad}
 \tag{18}
$$
这是一条真实的、保留全部原迹与循环核的固定 level N、
weight 2 生成级数。取 $\lambda=1$ 时其 q 系数在 $\mathbb Z_p$。
其存在不与 R165 的**线性等变** heart 维数界冲突：
这里先作了不变二次配对。

但 (17) 来自原 Hecke 本征关系，(18) 的新级数只是
**未知标量 $\mathcal E_r(z)$ 乘 f**。
首 Fourier 系数仍是待证的同一个二次量；没有独立的单位系数。
这个标量随 $(p,\ell,Q)$ 变化，并非固定有理数。

## 6. 原 p 进 Gross–Zagier 输入与尚未支付的比较

Disegni（2017）§5.3 的 Lemma 5.3.1、Proposition 5.3.2
确实把 CM 点之间的 p 进高度组织成 Hecke 生成级数。
因此二次配对与模形式的接口是实际的。
但其用于 Gross–Zagier 主公式的 E-isotypic 高度采用
ordinary 的规范 Panchishkin/unit-root 分裂；
这里依据 §4.1 的规范选择及 Lemma 5.3.1 之后对目标 A 分量的限定。
Lemma 5.3.1 本身允许任意 Hodge splitting，
不能把引理之后的额外限定反写成该引理的假设。
不能把任意 (6) 的高度都代入同一条 L 导数公式，
再相减而声称得到 (12) 的已知值。
该文在扩域时常使用除以次数的归一化；
本文 (11)、(14) 明确使用未归一化高度，不能混用常数。

进一步使用 toric/character 公式至少须保持：
原阶 p 字符的整格、$\kappa_r$ 的 Fourier 权、
$C_\ell\times U$ 的双迹、(14) 的域次数，
以及 (12) 的 $p^2$ 归一化。
单个复字符的非零高度，或复高度的正定性，
都不自动给这个带符号的 p 进局部加权和为单位。

本篇已经把 $I_1,I_2$ 接入原 Heegner 点的真实高度变化；
尚未证明无穷多个 p 上两者至少一个非零模 p。
下一输入必须给 (18) 一个独立、可控的 Fourier 系数或
适用于这两个补空间及原权重的精确 L 函数比较。

## 来源及核查

1. J. S. Balakrishnan、A. Besser，
   *Coleman–Gross height pairings and the p-adic sigma function*，
   J. reine angew. Math. **698**（2015），89–104，
   DOI 10.1515/crelle-2012-0095。
   [作者全文](https://arxiv.org/pdf/1201.6016v2)。
   已独立读 §2 的局部迹与补空间、Theorem 4.1 及其证明
   （作者版印 pp.8–9），以及 Corollary 4.2。
   (5)、(7) 采用该原文的杯积方向；(8)–(12) 在本篇直接推导。
2. D. Disegni，*The p-adic Gross–Zagier formula on Shimura curves*，
   Compositio Math. **153**（2017），1987–2074。
   [作者全文](https://disegni-daniel.perso.math.cnrs.fr/pyzz-pst.pdf)。
   已独立读 §4.1 的分裂与域扩张规范，
   §5.3 Lemma 5.3.1、Proposition 5.3.2；
   本篇没有把其规范高度公式扩展到任意 $W_\lambda$。
3. 内部依赖：R130/R139 的原 formalizer，
   R154 的完整类群商，R157 的复共轭与反射，
   R161 的两个实际循环量及有理参数，R164 的对数整格。
   R165 仅用于说明其线性范围不排除本篇二次构造。
