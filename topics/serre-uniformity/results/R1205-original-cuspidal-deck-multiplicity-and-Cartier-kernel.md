# R1205：原最高尖点的自然 deck 重数与 Cartier 核的准确纯化

日期：2026-11-28。会话：Astra-serre-24b8836b-20261126；global_route / root。

**已证明，保持原 $p\equiv11\pmod{12}$ 行。** 原最高 mixed packet 的负自然 deck 部分，纯尖点投影在特征零中的秩准确为 $n=2g-1$。因此 R1204 最后保留的一维商标量是 $0$，不是 $1$：纯尖点 Hodge 格的 generic 底空间恰是原 Cartier 泛函的核。原高 PS 返回不仅落入该核，而且给该纯尖点格的一组实际整基。

这里没有把 $V_m$ 与 $V_1$ 称为同一个全局自守表示。重数比较使用原 full-$p$ 曲线的两个 pairing 平方类组件，以及一个与原 $\delta$ 交换的显式函数。原 $T_*$ 的 packet 单位本身仍不证明其纯尖点投影或指定半秩商上的横截单位。

## 1. 同一个原格和待定标量

保留 R1193、R1195、R1202、R1204 的全部对象：
$$
p=12g-1>37,\qquad
m=(p-1)/2,\qquad n=2g-1,\qquad
m=3n+2.
\tag{1205.1}
$$
原曲线为同一个 $X_1$，原 Jacobian 为 $J_1$，deck 在原参数中为 $\delta(a)=\zeta a$。本篇的正负号始终指自然曲线拉回
$\delta^*$ 的 $\zeta,\zeta^2$ 角色。

写
$$
E=E_m,\qquad U=p e_{V_m}e_N,\qquad q=U/p,
\qquad
a=m^2,\quad b=(m+1)^2=a+p.
$$
R1202 已证明：在原实际最高惯性、负自然 deck 的 $W$-格 $\Gamma$ 上，$q$ 是整幂等元。它的 $W$-秩为
$2n+1$，由 $n+1$ 个 generic 底提升 $\Omega_a$ 与 $n$ 个实际高 PS 提升
$\pi_0^{e_0-p}\Psi_b$ 组成。在这些实际基中，
$$
\bar q=
\begin{pmatrix}
 A&C\\ B_1&D
\end{pmatrix}.
\tag{1205.2}
$$
这里 $A$ 依实际提升选择，不能先视为 generic 底向量的规范算子；$C$ 已由 R1204 完全计算。

置 $B=b_{\rm Ig}^3$，以免将这个多项式变量与上面的惯性权混同。原 generic 负底空间为
$$
\mathcal T=k[B]_{\le n}.
$$
原高 PS 输入空间为 $b_{\rm Ig}^2 k[B]_{\le n-1}$。R1204 给出
$$
C(T)=-3\gamma^2
 \left((1-b_{\rm Ig}^3)T''-4b_{\rm Ig}^2T'
                     -\frac94 b_{\rm Ig}T\right),
\tag{1205.3}
$$
并证明它是单射，且
$$
\operatorname{im}C=\ker\mathfrak c,\qquad
\mathfrak c(S)=[B^{2n+1}](1-B)^{2n+2}Q(B)S(B).
\tag{1205.4}
$$
$\mathfrak c$ 是非零泛函；它来自同一个中心微分
$S(b_{\rm Ig}^3)\,db_{\rm Ig}/(uA)$ 的 Cartier 算子，不是另选的余维一空间。

由 $q^2=q$，
$AC+CD=C$，故 $A$ 保持 $\operatorname{im}C$。它在一维商
$\mathcal T/\ker\mathfrak c$ 上的诱导作用为某个
$\lambda\in\{0,1\}$。R1204 的迹计算已给
$$
\operatorname{rank}_W(q\Gamma)=n+\lambda.
\tag{1205.5}
$$
由于 $2n+1<p$，这里的秩由模 $p$ 迹准确恢复，没有模 $p$ 后相差一个 $p$ 的歧义。以下计算的是 (1205.5) 左边的**原特征零秩**。

## 2. 原 full-$p$ 的两个组件与真正的二次变换

在特征零代数闭包中工作，保留原 full-six tame 来源。先选原六水平的一个 Weil pairing 组件，并对 R970 的图子群在该组件的稳定子取商。R970 的另一六水平组件由原 $h_0$ 重建；这一步是同构，不额外产生重数二。

然后仍保留所有 $p$-Weil pairing 组件，并仅在 $p$ 水平除去标量子群 $\mathbf F_p^\times$。所得 compactified 曲线记为 $\mathscr X$。它在几何上有两个开闭组件：
$$
\mathscr X=\mathscr X_+\sqcup\mathscr X_-.
\tag{1205.6}
$$
这里也没有额外的几何连通分支：所选六水平组件的稳定子包含 $\Gamma(6)$，而其中 $u(6)=\left(\begin{smallmatrix}1&6\\0&1\end{smallmatrix}\right)$、$l(6)=\left(\begin{smallmatrix}1&0\\6&1\end{smallmatrix}\right)$ 的幂模 $p$ 给全部上下初等幺幂元，生成 $\operatorname{SL}_2(\mathbf F_p)$。因此固定 $p$-Weil pairing 的覆盖连通；再除标量后准确留下上述两个平方类组件。

其标号是
$e_p(P,Q)$ 相对于固定本原 $\zeta_p$ 的指数之平方类。标量换基
$(P,Q)\mapsto(tP,tQ)$ 将该指数乘 $t^2$，所以平方类正是除标量后保留的标号。原
$$
G=\operatorname{PGL}_2(\mathbf F_p)
$$
作用运输这两个组件；其稳定子为
$\operatorname{PSL}_2(\mathbf F_p)$。整个论证始终在这两个组件的并上进行，不将移动 pairing 组件的元素当作单个组件的自同构。

定义真正的全局局部常数函数
$$
\epsilon|_{\mathscr X_+}=1,\qquad
\epsilon|_{\mathscr X_-}=-1.
$$
若
$$
\eta(g)=\det(g)^m\in\{\pm1\},
$$
则由实际换基的 Weil pairing 公式，
$$
g^*\epsilon=\eta(g)\epsilon.
\tag{1205.7}
$$
令 $M=H^0(\mathscr X,\Omega^1)$。乘 $\epsilon$ 为一个可逆线性映射
$T_\epsilon$，并满足
$$
g^*T_\epsilon=\eta(g)T_\epsilon g^*.
\tag{1205.8}
$$
所以这是原几何 Hodge 表示与其 $\eta$-twist 的实际同构。

必须同时保留原 deck。所选六水平组件上，原 $\delta$ 是独立的 mod-two order-three deck；R970 §5 的图子群在该组件的 mod-three 侧经 $\vartheta$ 的像为 $A_3$，故这个 order-three 元素正规化该图子群。它只改变原 prime-to-$p$ 标记，与 $p$ 水平换基交换，并保持 $p$-Weil pairing 平方类。因而
$$
\delta^*\epsilon=\epsilon,\qquad
\delta^*T_\epsilon=T_\epsilon\delta^*.
\tag{1205.9}
$$
若改用全部六水平组件描述，须连原 $h_0$ 重建同时运输 $\delta$，结果相同。这里没有将两个不同素数的 pairing 组件混作一个计数因子。

## 3. 有限尖点 twist 与原正规化子重数

按 R1029、R1195 的原有限类型约定，
$V_r$ 对应非分裂 Cartan 字符
$$
\theta_r=\widetilde\omega_2^{\,r(p-1)}
$$
以及其 Frobenius 共轭 $\theta_r^{-1}$。二次 determinant 在
$\mathbf F_{p^2}^\times$ 上为 $\theta_{m+1}$，故
$$
V_1\otimes\eta
 =V_{m+2}
 \simeq V_m,
\tag{1205.10}
$$
最后一步使用 $m+2\equiv-m\pmod{p+1}$。这只是一个准确的有限群表示恒等式。

由 (1205.8)–(1205.9)，每个自然 deck 角色上的 multiplicity space 都有
$$
\dim\operatorname{Hom}_G(V_m,M)_{\delta^*=\zeta^j}
 =
\dim\operatorname{Hom}_G(V_1,M)_{\delta^*=\zeta^j}.
\tag{1205.11}
$$
原正规化子固定线在 $V_1,V_m$ 中均为一维，因为 $1,m$ 都是原允许的奇数；这是 R1029 (1029.5) 的实际 Cartan-normalizer character 计算。

需要区分两种箭头。$T_\epsilon$ 本身一般不将 $N$-固定向量送到 $N$-固定向量，因为 $\eta|_N$ 非平凡。上式比较的是整个 $G$ 表示中的 multiplicity spaces，再用两种类型各自的真实一维 $N$-固定线计算原商的 Hodge 重数。没有声称一个未经证明的 $N$-固定线逐向量同构。

R1029 §2 已排去原水平上的 unramified 旧型：去掉 $p$ 水平后的原 tame 曲线是 $\mathbf P^1$，其 weight-two Hodge 空间为零。R1030／R1195 将原最低型与 $e_{V_1}e_N$ 的角识别。故 (1205.11) 右边就是 R1029 的实际最低型 $e_1$ Hodge 重数，而非另一个 level-one 模块。

## 4. 最低型的自然负 deck 维数准确为 n

R1029 (1029.14) 给原最低型的整 Hodge 格及其特殊纤维：
$$
(e_1\omega_{\mathcal J})\otimes k
 =(\omega_{\mathcal J}\otimes k)_{w=m}.
\tag{1205.12}
$$
右边准确是全部 generic SS 尾的最低一形式。原 SS 集
$A(b)=bQ(b^3)=0$ 有一个固定点 $b=0$ 与 $n$ 个三元 $\delta$-轨道。每个三轨在自然 Hodge 中各贡献三个 deck 角色一次。

固定尾的角色不能由协变晶体的标签猜出。在原 $b=0$ 全参数中，$\delta$ 的形式参数线性项为 $\zeta^2$，所以
$\alpha,\beta$ 同乘 $\zeta^2$；Cartan 商满足
$$
V\longmapsto\zeta V,\qquad U_{\rm tail}\longmapsto U_{\rm tail}.
$$
原 generic 尾坐标
$X=V^2,\ Y=U_{\rm tail}V$ 遂给
$$
X\longmapsto\zeta^2X,\qquad Y\longmapsto\zeta Y,\qquad
\delta^*(X^j\,dX/Y)=\zeta^{2j+1}X^j\,dX/Y.
\tag{1205.13}
$$
最低层 $j=0$ 的自然角色是 $\zeta$。因此
$$
\boxed{\quad
\operatorname{rank}(e_1\omega_{\mathcal J})_{\delta^*=\zeta}=n+1,
\qquad
\operatorname{rank}(e_1\omega_{\mathcal J})_{\delta^*=\zeta^2}=n.
\quad}
\tag{1205.14}
$$
deck 阶三为单位，整投影与 base change 交换，故这是特征零 Hodge 的同一维数。

还有一个防止逆号混用的核对。R1037 (1037.23) 的原实际 Lie 作用为
$\delta_*a(b)=\zeta a(\zeta b)$，在次数 $<3n+1$ 的多项式模型上同样给正 $n+1$、负 $n$。原 Abel–Jacobi 映射与 $\delta_*$ 相容至一个平移；平移在不变微分上恒等，因此实际 cotangent pullback 对应自然曲线 $\delta^*$，具有同一个特征值。这里使用的是实际 Lie 线性映射的转置，不是人为规定的 contragredient 表示。R1035 (1035.3) 中协变 Dieudonné 在曲线晶体上的 $(\delta^{-1})^*$ 约定仍保持原样；没有把那个晶体标记误作本段的自然 Hodge 作用。

## 5. 原最高纯尖点的准确秩与整基

由 (1205.11)、(1205.14)，最高型 $V_m$ 的自然负 deck Hodge multiplicity 准确为 $n$。

还须把它接到原 $\Gamma$。$\Gamma$ 的 generic 底基
$\Omega_a$ 与重标后的实际 PS 基
$\pi_0^{e_0-p}\Psi_b$ 在反转 $\pi_0$ 后张成原 $E_m$ 全部负 deck Hodge 空间。它们的不同 $\pi_0$ 因子只选择同一个实际惯性权的 $W$-格，不改变特征零张成空间。$q=e_{V_m}e_N$ 在这个空间上正是原纯尖点投影。因此
$$
\boxed{\quad
\operatorname{rank}_W(q\Gamma)=n,\qquad \lambda=0.
\quad}
\tag{1205.15}
$$
这是真实特征零重数的结论，不是将特殊纤维中 generic 尾的
$n+1$ 维直接称为纯尖点维数。

令
$\operatorname{bot}:\Gamma/p\Gamma\to\mathcal T$
为原 generic 底读取。R1204 已证明
$\operatorname{bot}(\bar q\,\pi_0^{e_0-p}\bar\Psi)=C(T)$，
且这些返回有 $n$ 个独立像。因此
$$
\boxed{\quad
\operatorname{bot}:\ q\Gamma/pq\Gamma
 \xrightarrow{\ \sim\ }\ker\mathfrak c.
\quad}
\tag{1205.16}
$$
具体地，任取原高 PS 输入空间的一组基 $T_1,\ldots,T_n$，取对应实际整提升 $\Psi_i$；则
$$
q(\pi_0^{e_0-p}\Psi_1),\ldots,
q(\pi_0^{e_0-p}\Psi_n)
\tag{1205.17}
$$
是 $q\Gamma$ 的一个 $W$-基。证明是其底返回由 (1205.3) 单射而线性独立，再用 (1205.15) 与 Nakayama。此处所有 $q$ 的整性都来自 R1202，未将 $p^{-1}$ 有理 projector 直接作用于整个原整 Hodge 格。

若改变最高 generic 提升，底作用 $A$ 仍可改变；但它在
$\mathcal T/\ker\mathfrak c$ 上始终为零。返回空间 (1205.16) 及纯尖点格的秩不依赖这项选择。

## 6. 对同一原点差的准确后果及未付范围

保持原
$P=(p-1)D_0$ 与 R1196、R1199 的全图首对数泛函
$\mathcal V_m$。R1201 已付原
$$
T_*=(B-1)^n
$$
的 packet 值为一个明确单位。现在真正需要读取的纯尖点首列，准确是
$$
\boxed{\quad
\mathcal V_m\big|_{\ker\mathfrak c},
\quad\text{等价地逐个读取 }\mathcal V_m(C(T_i)).
\quad}
\tag{1205.18}
$$
这些值必须保留原高 PS 返回、三个支持尾的 Čech transitions 与全图 Serre 配对；不能只留下 generic 参考项。

特别，若 $\mathfrak c(T_*)\ne0$，则 $T_*$ 不可能是任何原纯尖点整 Hodge 向量的 generic 底。这不说其实际有理尖点投影为零；它说该投影会改变底，且不能以 packet 单位原封不动地推出尖点单位。若 $\mathfrak c(T_*)=0$，则 (1205.16) 保证有实际纯尖点整提升具有这个底；R1196 (1196.20) 已证明原 $\mathcal V_m$ 对同底最高 eigenlift 独立，所以该纯尖点提升的同一首值就是 R1201 的明确单位。这个条件式不需要再除 $p$，但也不据此把它运输到任意预先指定的 $C$。

本篇不证明 $\mathcal V_m|_{\ker\mathfrak c}$ 为零或非零，不预设原 PS 点差为挠，不将 $V_m=V_1\otimes\eta$ 的有限恒等式外推成指定 $\mathbf Q$-简单商的全局二次 twist。同一 $C$ 的 MW 饱和空间和原 CM Abel 列仍须用实际 Hecke、极化与格运输完成。

## 来源与逐项核验

- [R970](R970-original-Cartier-packet-and-high-CM-congruence-ideal.md) §§2–3、5：原 full-six 两 pairing 组件、图子群、$h_0$ 重建和独立 mod-two deck。本文另直接构造 $p$ 水平两个平方类组件上的函数，不借六水平重数重复计数。
- [R1021](R1021-actual-full-p-affine-tail-rigidity-and-quotient-parameter.md)：原 full-$p$ framing、level 作用及全部 Weil 分支。
- [R1029](R1029-original-lowest-inertia-type-integral-Hecke-splitting.md) (1029.5)、(1029.6)、(1029.12)–(1029.16)：实际正规化子固定线、原旧型排除、最低型整 Hodge。
- [R1035](R1035-original-lowest-type-integral-Lie-comparison-by-two-PD-thickenings.md) (1035.1)–(1035.3)、[R1037](R1037-original-Hodge-graph-operator-and-primitive-MW-annihilator.md) (1037.23)：实际 Lie 与协变晶体的两种准确作用，本文以原 Abel 映射核自然 Hodge 号。
- R1193、R1195、R1202：原最高 mixed packet、整有限角、$q\Gamma$ 的实际整性与完整 generic 张成空间。
- [R1204](R1204-original-PS-return-Cartier-kernel-and-cuspidal-quotient.md)：同一个原高 PS 返回、$\operatorname{im}C=\ker\mathfrak c$ 及最后一维商。

全部论证为原来源上的纸面推导；未运行数学程序，未新增有限素数扫描。此结论缩小了原首列的真实目标，没有宣布 Serre 主目标完成。
