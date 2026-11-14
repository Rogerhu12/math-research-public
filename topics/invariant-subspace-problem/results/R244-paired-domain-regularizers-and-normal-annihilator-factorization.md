# R244：配对域正则器与正常湮灭态的较弱分解接口

日期：2026-11-13（UTC+8）。作者：normal_states。

状态：完整充分判据。它将共同列图的全域有界正则化削弱为有限个指定输入的配对域条件。尚未为任意有限秩正见证构造这样的正则器；不把一般正常性当作域条件。

## 1. 实际最小闭乘子及单端图配对

令 $H=L^2(\mathbb Z_2,\mu)$，$\mathfrak C=\{A\}'$，
$\mathcal A=\overline{\mathbb C[I,A]}^{\|\cdot\|}$，
$$
(Cf)(y)=\overline{f(-1-y)},\qquad B(f,g)=\langle f,Cg\rangle.
$$
$B$ 连续对称双线性，$\langle\cdot,\cdot\rangle$ 对第一变量线性。每个 $F\in\mathfrak C$ 都为 $C$ 对称：
$$B(Fu,v)=B(u,Fv).$$
$\mathfrak C$ 交换，$1$ 对 $A$ 循环；R88 给有界多项式强逼近。

记 $\mathscr D$ 为有限物理柱向量。对 $g\in\mathscr D$，有实际有界乘子 $X_g\in\mathcal A$，且 $X_g1=g$。给定任意 $f\in H$，在 $\mathscr D$ 上定义
$$
X_{f,0}g=X_gf.
\tag{1.1}
$$
有限柱配对直接证明它可闭：若 $g_n\to0$ 且 $X_{f,0}g_n\to v$，则对任意有限柱 $z$，$B(v,z)=\lim_n B(g_n,X_zf)=0$；有限柱稠密及 $B$ 非退化给 $v=0$。记其最小闭包为 $X_f$。不假设一般 $X_f$ 已最大 $C$ 自伴，也不把未知最大图和最小图等同。

**引理 1.1。** 对任意 $f\in H$、$g\in\operatorname{Dom}X_f$ 和 $F\in\mathfrak C$，
$$
\boxed{B(Fg,f)=B(FX_fg,1).}
\tag{1.2}
$$

**证明。** 先设 $g\in\mathscr D$。由 $g=X_g1$、交换性及 $C$ 对称，
$$
B(Fg,f)
=B(FX_g1,f)
=B(1,FX_gf)
=B(FX_gf,1).
$$
右侧即 $B(FX_{f,0}g,1)$。一般 $g$ 取有限柱图逼近 $g_n\to g$、$X_{f,0}g_n\to X_fg$。因为 $F$ 有界且 $B$ 连续，两端取极限即可。证毕。

这条恒等式只要求一个输入在已定义的最小图域中；并不要求 $f,g$ 同时满足次数指数矩，也不需要将 $F$ 强行放进未知的无界乘积域。

## 2. 有限秩状态的配对正则器

固定
$$
\rho=\sum_{i=1}^d f_i\otimes f_i\ge0,\qquad
\phi(F)=\operatorname{Tr}(\rho F)
=\sum_{i=1}^d\langle Ff_i,f_i\rangle.
\tag{2.1}
$$
对 $R\in\mathfrak C$，只要求以下有限个域条件：
$$
\boxed{Rf_i\in\operatorname{Dom}X_{Cf_i}\quad(1\le i\le d).}
\tag{2.2}
$$
条件可能依赖选择的正秩一分解；只需存在一个满足条件的分解，不宣称每个分解都自动满足。

定义
$$
h_{\rho,R}:=\sum_{i=1}^d X_{Cf_i}Rf_i\in H.
\tag{2.3}
$$
引理1.1立即给，对每个 $F\in\mathfrak C$，
$$
\boxed{
\phi(RF)=B(Fh_{\rho,R},1),\qquad
B(h_{\rho,R},1)=\phi(R).
}
\tag{2.4}
$$
确切地说，
$$
\langle FRf_i,f_i\rangle
=B(FRf_i,Cf_i)
=B(FX_{Cf_i}Rf_i,1),
$$
再求和。$F$ 与 $R$ 的交换性保证左侧为 $\phi(RF)$。

若另一种合法分解产生 $h'$，则 $B(A^n(h-h'),1)=0$ 对全部 $n$ 成立。$C$ 对称及 $1$ 的循环性迫 $h=h'$。因此一旦 (2.4) 有 $H$ 向量实现，该向量唯一；域条件的表达方式不会改变它。

## 3. 对单射慢符号的精确排除条件

固定 $S\in\mathfrak C$，假设它在全 $H$ 上单射。若 $\rho$ 满足
$$
\phi(SF)=0\qquad(F\in\mathcal A),
\tag{3.1}
$$
则由 R88 的强多项式逼近和有限秩泛函的强连续性，
$$
\phi(SF)=0\qquad(F\in\mathfrak C).
\tag{3.2}
$$
此处只是把指定右因子强逼近，不要求原理想有统一有界的强逼近单位。

**定理 3.1。** 若 $R$ 满足 (2.2)，则
$$
h_{\rho,R}=0,\qquad
\phi(RF)=0\quad(F\in\mathfrak C).
\tag{3.3}
$$

**证明。** 对 $F=A^nS$ 使用 (2.4)，并由 (3.2)，有
$$
0=\phi(RSA^n)=B(SA^nh_{\rho,R},1)
=B(Sh_{\rho,R},A^n1).
$$
循环性迫 $Sh_{\rho,R}=0$；全空间单射性给 $h_{\rho,R}=0$。代回 (2.4) 即得 (3.3)。证毕。

因此，下列任一额外条件都能排除非零 $\rho$：

1. 存在满足 (2.2) 的 $R$，并且 $\phi(R)\ne0$。
2. 存在满足 (2.2) 的 $R$，且
   $$I\in\overline{R\mathcal A}^{\mathrm{SOT}}.$$
3. 存在一族均满足 (2.2) 的 $R_\alpha$，并且
   $$\phi(R_\alpha)\longrightarrow\operatorname{Tr}\rho>0.$$
   特别，对有限秩 $\rho$，$R_\alpha\to I$ 于 WOT 或 SOT 已足够。

第2项由 (3.3) 与强连续性得到 $\phi(I)=0$；第3项则与每个 $\phi(R_\alpha)=0$ 矛盾。第1项最弱：不必先证明所选 $R$ 是普遍分母，也不必要求它在全 $H$ 单射或稠密像。

本定理只用 $S$ 的全空间单射性和固定第二因子为 $1$ 的配对分解；没有将 $S$ 的全空间稠密像搬到未知不变限制。

## 4. 为什么这比共同图全域正则化弱

[R242](R242-minimal-witness-module-rank-and-vertical-graph-obstruction.md) §5 的充分条件要求某个共同闭列乘子 $T$ 满足
$$RH\subseteq\operatorname{Dom}T,\qquad TR\in B(H,H^{(d)}),$$
再要求 $R$ 的强主理想中有 $I$。它同时控制所有 $u\in H$。

这里仅检查 $d$ 个指定输入 $Rf_i$，并分别使用 $d$ 个闭乘子 $X_{Cf_i}$。不要求任何 $X_{Cf_i}R$ 全域，也不需要它们是有界算子。甚至可以用第3节第1项或第3项替代普遍强单位条件。

这是一条严格较弱的假设路线；本稿没有声称它与慢符号的普遍分母性质等价，也没有证明任意有限秩状态都能找到所需 $R$。既有正一阶预解式的图核心定理只适用于已证明的乘子或混合词，不能直接填补 (2.2)。

## 5. R230 正则类正是 R=I 的已闭情形

R230 构造
$$
\mathscr H_9=\{f:\sum_{p\ge0}9^p\|P_pf\|<\infty\}
$$
并证明任意 $f,g\in\mathscr H_9$ 都满足
$$g\in\operatorname{Dom}X_f,\qquad X_fg=f\odot g.$$
$C$ 保持 $\mathscr H_9$。因此若 (2.1) 中全部 $f_i\in\mathscr H_9$，可直接取 $R=I$；(2.3) 正是 R230 的
$$h_\rho=\sum_i f_i\odot Cf_i.$$
某个 $r>9$ 的 Walsh 次数指数矩是基无关的充分条件。全部任意相位 R16 乘积的有限张成已由 R230 覆盖，不属于本稿新的未解对象。

一般 $f\in H$ 未必在 $\operatorname{Dom}X_{Cf}$ 中。[R240](R240-cyclic-positive-functional-without-fixed-vacuum-factor.md) 的实际固定真空正秩一反例说明：这个缺口不能靠正常性、秩一、点态连续或严格正下界消除。

## 6. 迹类的可数扩展及量词边界

若
$$\rho=\sum_{i\ge1} f_i\otimes f_i,\qquad
\sum_i\|f_i\|^2<\infty,$$
并有 $R\in\mathfrak C$ 满足全部配对域条件以及
$$
\sum_i\|X_{Cf_i}Rf_i\|<\infty,
\tag{6.1}
$$
则 (2.3) 绝对收敛，(2.4) 仍成立。左侧由
$\|RF\|\sum_i\|f_i\|^2$ 控制，右侧由 (6.1) 控制。

对 (3.2)，R88 的一致有界多项式强逼近允许逐项支配极限，因此这个可数版本也有效。但一般迹类泛函不对任意无界 WOT/SOT 逼近网连续；不能从 $I\in\overline{R\mathcal A}^{\mathrm{SOT}}$ 单独推出第3节第2项的迹类版本。迹类情形可直接使用 $\phi(R)\ne0$，或明确假设 $\phi(R_\alpha)\to\operatorname{Tr}\rho$，或使用一致有界强逼近。有限秩主目标没有这个额外问题。

## 7. 当前最小待证命题

对一个假想有限秩正湮灭见证，足够证明存在 $R\in\mathfrak C$，使
$$
Rf_i\in\operatorname{Dom}X_{Cf_i}\quad\text{对每个 }i,
\qquad \operatorname{Tr}(\rho R)\ne0.
$$
或者构造一列具有这些配对域条件且在该状态上趋于单位的 $R_n$。

这不要求固定产品共同源，不要求未知子商的共轭，不要求正共轭变形保湮灭，也不要求将任意无界共同图全域有界化。当前只把它确定为一个真实且较弱的充分接口；存在性仍待证明。

