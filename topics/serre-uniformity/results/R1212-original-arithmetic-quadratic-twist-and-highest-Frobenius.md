# R1212：原两组件的算术二次变换与最高尾 Frobenius 的完整规范

日期：2026-11-28。会话：Astra-serre-24b8836b-20261126；global_route / root。

**已证明，保持原 $p\equiv11\pmod{12}$ 行。** R1205 的两平方类函数不仅比较有限群重数：它给原完整 full-level Jacobian 上的实际代数自同构，并准确交织原 prime-to-$6p$ Hecke 与二次 Galois 字符。原最低、最高有限尖点类型的整个 multiplicity realization 因而互为 $\chi_p$-twist。另在同一个原普通尾上，最高 gap 的 Frobenius 首项、算术运输和极化配对都有明确单位规范。

这两个结论分别是实际特征零来源与实际特殊晶体来源。本文不把它们拼成一个尚未证明的、原纯尖点 Lie 格上的单位比较；尤其不宣称特殊配对限制到 $\ker\mathfrak c$ 后仍完美。

## 1. 同一个原 full-level 来源

保留
$$
p=12g-1>37,\qquad m=(p-1)/2,\qquad
n=2g-1,\qquad e_0=m(p+1),\qquad \pi_0^{e_0}=p.
\tag{1212.1}
$$
六水平采用 R970 的原图子群、原 $h_0$ 组件回返以及原 deck $\delta$。在几何上先保留所有 $p$-Weil pairing 组件，仅除去 $p$ 水平标量子群。R1205 §2 已从 $\Gamma(6)$ 的实际上下幺幂元证明，此时准确有两个开闭组件：
$$
\mathscr X=\mathscr X_+\sqcup\mathscr X_-,\qquad
G=\operatorname{PGL}_2(\mathbf F_p).
\tag{1212.2}
$$
可以先取一个六水平 pairing 组件再由 $h_0$ 重建，也可以始终在全部六水平组件上取原图子群不变量。以下证明使用后一种描述；它与 R970 (970.18g) 的原单组件算子完全相容。

固定原本原 $\zeta_p$。对一个标记 $(P,Q)$，写 $e_p(P,Q)=\zeta_p^a$，定义
$$
\epsilon(P,Q)=\left(\frac ap\right),\qquad
\eta(g)=\det(g)^m\in\{1,-1\}.
\tag{1212.3}
$$
标量换基将 $a$ 乘平方，故这是 (1212.2) 上的真正局部常数函数。它在两个组件上分别为 $1,-1$，不是只定义于一个开集的函数。

在 $\operatorname{Jac}(\mathscr X)=\operatorname{Jac}(\mathscr X_+)\times\operatorname{Jac}(\mathscr X_-)$ 上令
$$
\mathcal E=( [1],[-1]).
\tag{1212.4}
$$
这是实际代数群自同构，$\mathcal E^2=1$，保持乘积极化。它在 Hodge、Betti、étale 以及存在的 crystalline realization 上的作用均为乘 $\epsilon$，记为 $T_\epsilon$。这里没有以有限表示中的一个任选 intertwiner 代替原代数来源。

R1205 的实际换基与 deck 计算给
$$
g^*T_\epsilon=\eta(g)T_\epsilon g^*,\qquad
\delta^*T_\epsilon=T_\epsilon\delta^*.
\tag{1212.5}
$$
六水平回返 $h_0$ 只作用于 prime-to-$p$ 标记，故也与 $T_\epsilon$ 交换。六水平的两个组件不会另添一个重数二。

## 2. 原 Hecke 的确切二次字符

令 $\ell\nmid6p$ 为素数。在全部组件并上，取原循环 $\ell$-同源对应，写两投影为 $s,t$；$s$ 记 source，$t$ 记 target。对其一个几何点 $\varphi:E\to E'$，实际 Weil 配对满足
$$
e_p(\varphi P,\varphi Q)=e_p(P,Q)^{\ell}.
$$
所以在整个对应上准确有
$$
t^*\epsilon=\eta(\ell)s^*\epsilon,
\qquad \eta(\ell)=\left(\frac\ell p\right).
\tag{1212.6}
$$
无论使用原 $s_*t^*$ 还是对偶方向 $t_*s^*$，投影公式给相同的符号，因为 $\eta(\ell)^{-1}=\eta(\ell)$。保持原归一的 raw adelic Hecke $A_\ell$，得到
$$
A_\ell T_\epsilon=\eta(\ell)T_\epsilon A_\ell.
\tag{1212.7}
$$
这是真正 pull–trace 的等式：没有只在半单化特征系统上比较特征值，也没有除掉同源次数。

随后取原 full-six 图子群不变量。它与 $A_\ell$ 及 $T_\epsilon$ 的交换均由 disjoint-level 的实际对应保证；若在一个六水平组件上写算子，须用 R970 的真实 $h_0^{\epsilon_\ell}A_\ell$。由于 $h_0T_\epsilon=T_\epsilon h_0$，仍有
$$
\boxed{\quad
T_\ell^{\rm orig}T_\epsilon
 =\eta(\ell)T_\epsilon T_\ell^{\rm orig}
\quad}
\tag{1212.8}
$$
作为**完整 $G$-multiplicity 来源**上的等式。原同源微分或 norm 约定中的共同标量同时乘两边，不改变此式。

这里只在全部 $p$ pairing 组件并上使用 $A_\ell$。把一个 nonsquare pairing 回返矩阵提前加到单组件算子，再把它误称为与 $T_\epsilon$ 交换，会漏掉 (1212.8) 的字符。原正规化子商上的解释在 §4 单独处理。

## 3. 实际 Galois 下降也是同一个字符

对 $\sigma\in G_{\mathbf Q}$，由原 Weil 配对的 Galois 相容性，
$$
\epsilon(\sigma(P,Q))
 =\left(\frac{\bar\chi_{\rm cyc}(\sigma)}p\right)\epsilon(P,Q).
$$
令
$$
\chi_p(\sigma)
 =\bar\chi_{\rm cyc}(\sigma)^m.
\tag{1212.9}
$$
则实际代数自同构满足
$$
\sigma(\mathcal E)=\chi_p(\sigma)\mathcal E,
\qquad
\sigma T_\epsilon=\chi_p(\sigma)T_\epsilon\sigma.
\tag{1212.10}
$$
第一式中右边的负号指复合整个 Jacobian 的 $[-1]$。因此这不是仅有 cohomology 上偶然的反交换关系；$\mathcal E$ 在二次域上定义，并按 (1212.10) 真正下降为二次 twist 的同构。因为 $p\equiv3\pmod4$，这里的二次域是
$$
\mathbf Q(\sqrt{-p}),\qquad
\chi_p(\operatorname{Frob}_\ell)=\left(\frac\ell p\right)
\quad(\ell\ne p).
\tag{1212.11}
$$
六水平 Galois 回返仍只作用于六标记，故与此构造交换；它不会将 $\chi_p$ 改成 $\chi_p\chi_{-3}$。若分开自然 deck 的两个非平凡角色，则在定义 $\zeta_3$ 的域上读取；完整 realization 的 (1212.10) 仍是 $G_{\mathbf Q}$ 的等式。

## 4. 先作完整 multiplicity，再作原 N 固定线

令 $E$ 为两种有限类型的共同特征值域，或先取任一共同分裂数域。R1205 (1205.10) 的有限恒等式是
$$
V_m\simeq V_1\otimes\eta.
\tag{1212.12}
$$
对同一个原 full-level realization $H$，写
$$
\mathcal M_r=\operatorname{Hom}_{E[G]}(V_r,H_E).
$$
取一次 (1212.12) 后，$T_\epsilon$ 给完整的、可逆的映射
$$
\boxed{\quad
\mathcal M_1\otimes\chi_p\ \simeq\ \mathcal M_m.
\quad}
\tag{1212.13}
$$
它在 Hodge realization 上保持原自然 $\delta$ 角色，在 étale realization 上满足 (1212.10)，在 Hecke 上满足 (1212.8)。不同一次 intertwiner 的选择只改变一个固定 $E^\times$ 标量；不改变这些精确相容性。

如果只取特征值域而不先取分裂域，也无额外 Schur 指数门：两种实际 $V_r$ 的 $N$-固定空间都为一维。简单 $E$-代数的 $e_N$ 角因此具有 reduced rank $1$；一个含 reduced rank $1$ 幂等元的中心简单代数必 split。这给两种 $E$-模型，并将 (1212.13) 写在该同一个 $E$ 上。

原商的类型部分满足
$$
e_{V_r}H_E^N\simeq V_r^N\otimes_E\mathcal M_r,
\qquad \dim_E V_r^N=1.
\tag{1212.14}
$$
所以选两条实际固定线的非零 $E$-向量后，可在特征零回收原商的同一类型 realization，所得全部 away-$6p$ Hecke 系统与 Galois 系统准确按 $\chi_p$ 对应。

**整性界必须保留。** $\eta|_N$ 非平凡，故 $T_\epsilon$ 一般把 $N$-固定线送到 $N$ 的 $\eta$-线，不直接送到另一条 $N$-固定线。由 (1212.14) 回收的箭头仅在特征零使用；本篇没有证明其在原 $p$-整 $N$-角上为单位，也没有把它称为 R1211 的实际 $q\Gamma$ 的整同构。

一个可直接使用的谱结论是：原最高类型的 CM/non-CM 系统与最低类型一一对应，CM 的二次数域不变。若某系统为
$\operatorname{Ind}_{G_K}^{G_{\mathbf Q}}\theta$，扭曲后正是
$\operatorname{Ind}_{G_K}^{G_{\mathbf Q}}(\theta\,\chi_p|_{G_K})$；反向同理。因此此处不新增一个 CM 域，也不会把 non-CM 系统变为 CM。它仍不指定原给定商 $C$ 的整数尺度或原 $\beta$ 的像。

## 5. 同一个原最高 gap 的直接 Čech Frobenius

以下转到原普通 SS 尾；不以 §4 的有限 twist 搬运其局部参数。R1021、R1036 的实际曲线为
$$
D_s:\quad Y^2=X(X^{m+1}+A_s),\qquad
A_s=-3C_s^2\in\mathbf F_p^\times.
\tag{1212.15}
$$
在原无穷远分支取 $z=X^{-1/2}$，保持 $Y$ 的原 leading 号。最高一形式及其对偶 gap 是
$$
\omega_{h,s}=X^{(m-1)/2}\frac{dX}{Y}
 =-2(1+A_sz^{p+1})^{-1/2}dz,
\qquad f_{h,s}=[z^{-1}].
\tag{1212.16}
$$
使用与 R1036 相同的杯积顺序，
$$
\langle\omega_{h,s},f_{h,t}\rangle=2\delta_{st},
\qquad \operatorname{Res}_\infty(z^{-1}\omega_{h,s})=-2.
\tag{1212.17}
$$
可在实际 affine 尾与形式无穷远圆盘的 Čech 复形中计算。令
$$
G_s=X^{(m-1)/2}Y
 =z^{-p}(1+A_sz^{p+1})^{1/2}.
$$
$G_s$ 在 affine 尾正则，$z^{-p}-G_s$ 在形式圆盘正则。因此 $f_U=-G_s$、$f_V=z^{-p}-G_s$ 满足
$f_V-f_U=z^{-p}$。原总微分约定下，Frobenius 的 Čech 类
$(0,0,z^{-p})$ 减去 $d(f_U,f_V)$，正好得到 $dG_s$。直接微分：
$$
dG_s=
\frac{pX^{(3m+1)/2}+mA_sX^{(m-1)/2}}{2Y}\,dX.
$$
所以
$$
\boxed{\quad
\bar F(f_{h,s})=\frac{mA_s}{2}\omega_{h,s}
             =-\frac{A_s}{4}\omega_{h,s}.
\quad}
\tag{1212.18}
$$
这里 $F$ 的模 $p$ 映射杀 Hodge，故该计算不依赖把 $f_{h,s}$ 提升到 de Rham 晶体时的 Hodge 加项。它也没有更改原 gap、Serre 号或原曲线。

## 6. 原算术运输、canonical Igusa 相位和特殊 Gram 矩阵

取 R1036 的实际算术下降 $\alpha$，其在 $W(k)$ 上为 $p$-Frobenius，且 $\alpha(\pi_0)=\pi_0$。保持原 ordinary node
$$
W_s=\pi_0/z_s,\qquad u=\tau_sW_s+\cdots,
\qquad \tau_s=B_s^2,
\tag{1212.19}
$$
其中 R1200 的 canonical source 是
$$
B_s=2(1-s^3)h_p'(s),\qquad
C_s^2=\gamma^2/B_s^{2p},\qquad \gamma^{p-1}=-1.
\tag{1212.20}
$$
$u$ 是同一个原 Cartier–Weil character 所定义的 Igusa 坐标，构造与算术下降相容；不是另外选的 Hasse 根。对 (1212.19) 施 $\alpha$，得到真实 leading 运输
$$
\alpha(z_s)=\frac{\tau_s^p}{\tau_{s^p}}z_{s^p}
                 +\text{不改变该 gap 的高项}.
\tag{1212.21}
$$
最高相反惯性格在每尾只有这一条 gap 线；故 higher 项在该角色的 $H^1(\mathcal O)$ 类中不留下另一个项。

定义同一个原归一基
$$
\widetilde f_s=\tau_sf_{h,s},\qquad
\widetilde\omega_s=\tau_s^{-1}\omega_{h,s}.
\tag{1212.22}
$$
由 (1212.21)，$\alpha\widetilde f_s=\widetilde f_{s^p}$，且杯积规范仍为 $2$。最高 Hodge 线的对应运输由同一杯积与惯性角色决定。

在 (1212.22) 中，(1212.18) 给
$$
\bar F\widetilde f_s
 =\frac{q_{h,s}}4\widetilde\omega_s,\qquad
q_{h,s}=-A_s\tau_s^{p+1}=3\gamma^2 B_s^2.
\tag{1212.23}
$$
最后等号逐项使用 (1212.20)，没有将 $B_s^p$ 换成 $B_s$。又 $A_s,C_s^2,\gamma^2\in\mathbf F_p$，(1212.20) 迫 $B_s^2\in\mathbf F_p$。原 $\mathbf F_p$ 模型的 $B_{s^p}=B_s^p$ 进而给
$$
q_{h,s}=q_{h,s^p}\in\mathbf F_p^\times.
\tag{1212.24}
$$

令 $M^{\rm gen}_h$ 为同一普通尾 Jacobian 乘积的最高两惯性角色晶体。该定义只取原 generic 尾的直接因子，尚未把纯尖点 projector 加到整个好约化模型上。R1036 §§2–3 的真实 Hermitian 态射证明的是每个 $\operatorname{Jac}(D_s)$ 上的完整
$F^2=-p\alpha^2$，所以可直接限制到这里：
$$
\Pi_h=F\alpha^{-1},\qquad
\Pi_h^2=-p,\qquad \Pi_h^\dagger=-\Pi_h.
\tag{1212.25}
$$
没有从有限表示的 quadratic twist 推断这个平方号。

在其原 gap 格 $M^{\rm gen}_{h,L}$ 上定义
$$
B_h(v,w)=\langle\Pi_hv,w\rangle.
\tag{1212.26}
$$
这是 $W$-双线性的对称型。最高两惯性角色没有其它普通尾 Hodge 混合项；(1212.18) 为单位，故 $F(M^{\rm gen}_{h,L})=M^{\rm gen}_{h,H}$，而极化在两格之间完美。因此 $B_h$ 整且完美。它的实际模 $p$ 矩阵是
$$
\boxed{\quad
\bar B_h(\widetilde f_s,\widetilde f_t)
 =\frac{q_{h,s}}2\,\mathbf1_{t=s^p}
 =\frac{3\gamma^2B_s^2}{2}\,\mathbf1_{t=s^p}.
\quad}
\tag{1212.27}
$$
其中已包含 $\alpha^{-1}$ 的指标置换。外部系数随后按双线性作用，不再多取一个 $p$ 次幂。

### 6.1 自然 deck、算术半线性与配对的槽

本段的 $\delta$ 均表示自然曲线拉回 $\delta^*$。实际算术下降与原 deck 系数给
$$
\alpha\delta\alpha^{-1}=\delta^p=\delta^{-1},\qquad
F\delta=\delta F.
\tag{1212.27a}
$$
第二式是晶体 Frobenius 对原几何态射的自然性；$F$ 为 $\sigma_W$-半线性，故它将自然 $\zeta$ 角色送到 $\zeta^p$ 角色。第一式中的 $\alpha$ 也为 $\sigma_W$-半线性，因此 $\alpha$ 本身保持每个已标记的自然 deck 特征子空间。由此
$$
\Pi_h\delta=\delta^{-1}\Pi_h,\qquad
B_h(\delta v,w)=B_h(v,\delta w).
\tag{1212.27b}
$$
后一式使用原极化 $\delta^\dagger=\delta^{-1}$，不是说 $B_h$ 为同时作用两槽的 $\delta$-不变量。

因此两个不同自然 deck 特征子空间对 $B_h$ 正交；每个特征子空间内可以非退化。原固定 $s=0$ 尾在最高 Hodge 线上有角色 $\zeta^m=\zeta^2$，在 gap 线上有相反角色 $\zeta$。故普通尾的最高 Hodge 正、负维数为 $n,n+1$，而其 gap 正、负维数为 $n+1,n$；这与 (1212.27b) 和 ambient 完美性相容，不能误作一个两空间等维的 cross pairing。

对任意剩余域系数 $a_s,b_s$，真正的式子是
$$
\bar B_h\left(\sum_s a_s\widetilde f_s,
                \sum_t b_t\widetilde f_t\right)
 =\frac12\sum_s q_{h,s}a_sb_{s^p}.
\tag{1212.27c}
$$
它在两槽均为 $k$-线性。只有另外限制到满足 $b_{s^p}=b_s^p$ 的原算术下降向量时，才能把右边写成带 $p$ 次幂的形式；不能因此把 $B_h$ 改称一槽半线性的 Hermitian 型。

同样，(1212.25) 的准确半线性等式始终是 $F^2=-p\alpha^2$。在原 $\mathbf F_{p^2}$ 晶体来源上 $\alpha^2$ 是真实系数平方 Frobenius；线性化后才得到 $\Pi_h^2=-p$。最后，若借主极化改写为 R1035 的协变晶体和实际 $\delta_*$，须按 (1035.3) 同时换成 $(\delta^{-1})^*$；本文没有混用这两个标签。

## 7. 原中心底的同源坐标及准确后继边界

R1193／R1199 对同一个最高中心层
$$
\eta_S=\frac{S(b)}{uA(b)}\,db
$$
给原 SS 底系数
$$
L_s=\frac{mS(s)}{2\tau_sA'(s)}.
$$
所以用 (1212.22) 可直接写为
$$
\Omega_S^{\rm gen}
 =\sum_{s\in S}\frac{mS(s)}{2A'(s)}\,
                    \widetilde\omega_s.
\tag{1212.28}
$$
这是原 normal 与同一特殊晶体的坐标字典。结合 (1212.27)，后继比较无需再猜普通节点的单位或 Frobenius 指标。

本篇留下的是以下具体接口，而非有限类型识别：

1. R1205 的负纯尖点 Hodge 格确以 $\ker\mathfrak c$ 为 generic 底；但 (1212.27) 限制到其相关子空间可能退化，不能由整 ambient Gram 的行列式为单位排除。
2. R1211 已使 $q$ 在整个最高惯性 $W$-Hodge 格上整，正 deck 仍有 $\pi_0\,db/u$ ghost。它不自动给整个 $R$-晶体或 BT 群上的整 $q$，也不自动给实际 Lie 格到 $M^{\rm gen}_{h,L}$ 的单位比较。
3. (1212.13) 保完整原 Hecke、Galois、自然 deck 和 CM/non-CM 分类，但通过 $N$ 固定线回收时只作有理比较。不能用它无声消掉 R1195 的一个 $p$ 或 R1190 的实际格损失。
4. R1210 的纯尖点完整首对数单位与其实际二次 CM profile 已经成立。要将它用于全部 MW，仍须在同一个纯 Lie 格上支付极化、$\Pi_h$、split-Hecke 平衡及原完整 $\log\beta$ 的运输；aggregate 两列的单位 minor 本身不代这一步。

## 来源

- [R1205](R1205-original-cuspidal-deck-multiplicity-and-Cartier-kernel.md)，§§2–4：同一 full-six/full-$p$ 两平方类组件、原有限 twist、自然 deck 与实际 $N$ 固定线。
- [R970](R970-original-Cartier-packet-and-high-CM-congruence-ideal.md)，(970.18a–h)、§5：完整六水平组件、真实 $h_0$、raw Hecke 和 multiplicity 的准确回收。本篇另外给出 $p$-平方类上的实际 Hecke/Galois 两条等式。
- [R1021](R1021-actual-full-p-affine-tail-rigidity-and-quotient-parameter.md)、[R1200](R1200-original-canonical-Igusa-Weil-phase-and-rational-packet-pairing.md)，(1200.12)、(1200.16)：同一 affine 尾、原 source/target、canonical $\tau_s=B_s^2$ 与固定 Weil 根。
- [R1036](R1036-original-integral-alternating-test-and-complete-MW-annihilation.md)，§§1–4、(1036.2)：原杯积号、实际算术下降以及整个 ordinary-tail Jacobian 的 Hermitian Frobenius 平方。本文最高 gap 的 (1212.18) 为独立直接 Čech 计算。
- [R1193](R1193-original-highest-primitive-packet-and-simple-Cauchy-CM-jet.md)、[R1199](R1199-original-highest-packet-complete-generic-pairing-and-kernel-log.md)：原中心底到 SS 尾的实际 normal 系数。
- [R1210](R1210-original-pure-cuspidal-return-log-unit.md)、[R1211](R1211-original-whole-highest-character-projector-integrality.md)：已付的纯尖点首对数和整个最高 Hodge 角色整性；本文不将这些范围扩成尚未证明的实际 Lie 单位比较。

全文为代数几何来源与纸面计算；没有数学程序执行，没有重跑已登记窗口。Serre 主目标仍 OPEN。

root独立逐节纸核：两平方类来源、真实Hecke pull–trace、Galois下降、N角Schur论证、direct Čech号以及R1036/R1200的原Fp下降与canonical相位均核准；没有增加实际纯Lie格比较。
