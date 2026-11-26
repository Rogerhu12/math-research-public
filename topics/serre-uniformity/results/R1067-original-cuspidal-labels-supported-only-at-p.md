# R1067：原 cuspidal Kummer 标签只在 p 支撑及唯一 regular 全局提升

日期：2026-11-27（Asia/Taipei）。  
会话：Astra-serre-24b8836b-20261126；global_route / root。

**已证明。** 对每个 $p>37$，完整原曲线
$X=X_{\rm ns}^+(p)$ 的 R1062 规范 cuspidal Kummer 标签实际属于
$F(\{p\},p)$；原先保留的 $2,3$ 可以同时严格删去。
证明作用于规范函数 $u^m/A(u)$，包括原有理点在好素约化到 cusp 的情形，
不要求 $j$ 整，不限制 $I_p$ 或正规化子二次域。

若 $p$ regular，则在全部非平凡 cusp 角色上，新的全局标签到
$p$-local 标签是同构。于是每个实际 $p$-disk 标签恰有一个全局候选，
候选总数至多
$$
p\,n_{\mathbf Q_p}(p)\le \frac{2p^{3/2}\log(4p)}{\pi},
$$
不再有 R1065 的 $p^{\kappa_p}$ 因子。本文还给出这些同一候选的圆单位
坐标，以及在 $\ell\equiv1\bmod p$ 的辅助素处必须满足的显式幂剩余等式。
R1064 的真实辅助覆盖、可见角色和 Weil 范围同时扩展到所有 $\ell\ne p$，
包括 $2,3$。

这不是非 CM 点排除；没有证明上述候选的辅助共同像为空。
全部证明为纸面论证，无数学程序执行。

## 1. 原对象与不变的规范化

沿用 R1062、R1064、R1065：
$$
m=(p-1)/2,\qquad F=\mathbf Q(\zeta_p)^+,\qquad
G=\operatorname{Gal}(F/\mathbf Q)=\mathbf F_p^\times/\{\pm1\},
\qquad K=F_{\mathfrak p}.
\tag{1067.1}
$$
$\mathfrak p$ 是唯一 $p$ 位。$\Sigma$ 为原全部 $m$ 个几何 cusps；
它们在 $F$ 上有理，并构成一个简单传递的 $G$-轨道。

$U$ 是 cusp-supported modular units 模去 $F^\times$，
$U_p$ 由 $\operatorname{div}u\in p\operatorname{Div}^0_\Sigma$ 定义。
原模块
$$
V=U_p/pU\simeq C_\Sigma[p],\qquad V^G=0
\tag{1067.2}
$$
及实际 $G$ 作用保持 R1062 的定义。每个非平凡偶角色至多一维；
下面允许任意实际 $G$-子模块 $W\subset V$，包括完整 $V$ 及 forced 子模块。

对 $u\in U_p$ 的函数代表，写
$$
\operatorname{div}u=p\sum_{c\in\Sigma}n_c[c],\qquad \sum_c n_c=0.
$$
在各 cusp 取任意 $F$-rational uniformizer $t_c$，置
$$
a_c(u)=\left.(u/t_c^{pn_c})\right|_c,\quad
A(u)=\prod_{c\in\Sigma}a_c(u),\quad
f_u=u^m/A(u).
\tag{1067.3}
$$
真正标签是
$$
\Phi_x([u])=[f_u(x)]\in F^\times/F^{\times p}.
\tag{1067.4}
$$
换 $t_c$ 只改变一个 $p$ 次幂；$u$ 的常数倍在分子与全部 $m$ 个
leading coefficients 中准确相消。$u\mapsto[f_u]$ 在函数域中已是
$G$-equivariant，故本篇没有另选基点或重定义标签。

对 $S_p=\{\mathfrak p\}$，记
$$
F(S_p,p)=
\{a\in F^\times:\ v_{\mathfrak q}(a)\in p\mathbf Z
                     \text{ 对所有 }\mathfrak q\ne\mathfrak p\}/F^{\times p}.
\tag{1067.5}
$$
第一项主张是所有原非 cusp $x\in X(\mathbf Q)$ 的 (1067.4)
均落在 $\operatorname{Hom}_G(V,F(S_p,p))$。

## 2. 允许 wild stabilizer 的相对曲线商引理

本节的群必须逐点固定底环。它不适用于同时非平凡地作用于分歧基域的群。

设 $R$ 为完备 DVR，剩余域代数闭，$\varpi$ 为 uniformizer。
设 $\mathscr C/R$ 为光滑、泛纤维几何连通的曲线，有限有效群 $H$ 通过 $R$-自同构作用。
在相对有限商 $\mathscr Y=\mathscr C/H$ 的一个闭点上，
取逆像闭点 $x$ 及其稳定子 $I$。光滑性给
$$
A=\widehat{\mathcal O}_{\mathscr C,x}=R[[t]].
$$
$I$ 在这个完成环上的作用仍有效：若一个原有效自同构在完成环上为恒等，
局部环向其完成环的单射使它在函数域上也为恒等，从而在整条曲线上恒等。

令 $n=|I|$，定义
$$
s=\prod_{g\in I}g(t)
   -\left.\prod_{g\in I}g(t)\right|_{t=0}\in A^I.
\tag{1067.6}
$$
第二项属于 $R$，所以确被 $I$ 固定；无需 $I$ 固定 $t=0$ 这个 section。
每个 $\overline{g(t)}$ 都是 $k[[t]]$ 中阶一的参数，故
$$
s(0)=0,\qquad \bar s=t^n\cdot\text{unit}.
\tag{1067.7}
$$
在 $R[[S]][[T]]$ 中对 $s(T)-S$ 作 Weierstrass 准备与除法，
得到
$$
B=R[[s]]\hookrightarrow A,\qquad
A\text{ 是 }B\text{ 上秩 }n\text{ 的有限自由模}.
\tag{1067.8}
$$
也就是说，$1,t,\ldots,t^{n-1}$ 是一组 $B$-基。
这里的 distinguished degree 由 (1067.7) 准确给出，允许剩余特征整除 $n$。

Artin 固定域定理又给
$$
[\operatorname{Frac}A:\operatorname{Frac}(A^I)]=n.
$$
与 (1067.8) 比较得
$\operatorname{Frac}(A^I)=\operatorname{Frac}B$。
$A^I$ 对 $B$ 整，而 $B$ 正规，故
$$
A^I=R[[s]].
\tag{1067.9}
$$
商点上应先取全部逆像闭点的完成环乘积；群在这些因子上传递，
其不变量等于其中一点的稳定子不变量。
完成是平坦基变换，有限群不变量是有限 equalizer 的核，
所以完成与此不变量运算相容。
因此 (1067.9) 正是 $\mathscr Y$ 的完成局部环，而非另一个形式商。

对一般有限剩余域，可先作严格 henselian 化、完成，再在几何闭点上作上述论证。
光滑性沿忠实平坦基变换下降。结论是：
$$
\boxed{\mathscr C/H\text{ 在这些几何纤维点处仍光滑。}}
\tag{1067.10}
$$
若 $\mathscr C$ proper，有限商也 proper。这里没有使用 $|H|^{-1}$，
所以真实 $2,3$ stabilizers 不构成例外。
R1065/EP 在 $p$ 处的基域 Galois 商并非 $R$-linear，
不能套用本引理把其坏约化删去。

## 3. 完整原 X 在所有 l 不等于 p 处的好模型

固定 $\ell\ne p$，在包含 $\zeta_p$ 的严格未分歧完备底环 $R$
上考虑固定 Weil-pairing component 的 full-level compactification $\mathscr X(p)$。
Deligne–Rapoport [DR, IV Theorem 2.5] 给 proper smooth 与 finite étale cusps；
[DR, IV Theorem 2.7、Corollary 2.9] 在 $p\ge3$ 时给实际 projective smooth scheme。

原几何 normalizer 群为
$$
\Gamma=(N_{\rm ns}\cap\operatorname{SL}_2(\mathbf F_p))/\{\pm I\},
\qquad |\Gamma|=p+1.
\tag{1067.11}
$$
它在固定 Weil component 上有效且 $R$-linear。
泛纤维的商准确是完整 $X_{\rm ns}^+(p)$ 的该基变换。
因此 §2 给出 smooth proper coarse 商，特别包括 $\ell=2,3$。

还须保全部 cusp sections。full-level curve 的几何 cusp 在
$\operatorname{PSL}_2(\mathbf F_p)$ 中的稳定子是阶 $p$ 的 unipotent 群。
它与阶 $p+1$ 的 $\Gamma$ 相交平凡。
full-level cusp scheme 本身 finite étale，群在它上的作用是离散且随底环运输的；
泛纤维上没有的稳定子不会只在特殊纤维突然出现。
所以 $\Gamma$ 在全部 cusp scheme 上自由，
其商仍 finite étale，且不同 cusp 轨道没有碰合。

在 cusp 处 quotient map 本身 étale。可使用原 Tate 参数 $q^{1/p}$
的整 cusp chart，也可使用任意整相对参数；两者的 leading ratio 是单位。
本篇后面的计算只需要整参数存在，且 (1067.3) 已支付所有参数变化。

全 normalizer 的 determinant 满射给出原 $\mathbf Q$ 下降；
局部也可先对包含 $\zeta_p$ 的有限未分歧扩张作上述商，再作有限 étale descent。
因 smoothness、properness 与 finite étale boundary 均能下降，所得是原
$X/\mathbf Q_\ell$ 的 smooth proper 模型。
泛纤维几何连通，proper smooth 的几何连通分量数局部常数；
故特殊纤维几何连通，因光滑而几何不可约。

在 $F$ 上，全部 $m$ 个 cusp 泛点已 rational，
其 finite étale 闭包分裂为互不相交的 sections。
于是原 $X_F$ 在每个 $\mathfrak q\nmid p$ 都有 smooth proper、
几何不可约特殊纤维及全部互不相交的 cusp sections。
这些局部模型也可黏合为 $\mathcal O_F[1/p]$ 上的模型。

这严格加强了 R1062 中保守使用的 $\mathcal O_F[1/(6p)]$ 模型，
并没有引用“stack smooth 所以 coarse smooth”这一在 wild 情形下未付款的捷径。

## 4. 规范标签在 2、3 的垂直项也准确抵消

固定任意 $\mathfrak q\nmid p$，现在允许 $\mathfrak q\mid2$ 或 $3$。
令 $\mathcal O=\mathcal O_{F,\mathfrak q}$，$\pi_{\mathfrak q}$ 为 uniformizer，
$Y$ 为 §3 模型的唯一特殊纤维。在 regular surface 上有
$$
\operatorname{div}_{\mathscr X}(u)
 =p\sum_{c\in\Sigma}n_c\mathscr C_c+bY,\qquad b\in\mathbf Z.
\tag{1067.12}
$$
水平部分没有其它成分；垂直部分只有一个几何不可约纤维。

在每个 cusp section 附近选整参数 $t_c^{\rm int}$。
其它 cusp sections 不交，故
$$
u=\pi_{\mathfrak q}^{\,b}(t_c^{\rm int})^{pn_c}\epsilon_c,
\qquad\epsilon_c\text{ 为局部单位}.
\tag{1067.13}
$$
由此该整参数下的 leading coefficient valuation 恰为 $b$。
若 (1067.3) 最初用了别的全局参数，它与整参数的 leading ratio
属于 $F_{\mathfrak q}^\times$，所以改变的 valuation 是 $pn_c$ 的整数倍。
因此对原同一个全局 $A(u)$ 仍有
$$
v_{\mathfrak q}A(u)\equiv mb\pmod p.
\tag{1067.14}
$$

对非 cusp $x\in X(\mathbf Q)$，properness 给 $\mathcal O$-section。
将 (1067.12) 拉回：
$$
v_{\mathfrak q}u(x)=b+pI_x,\qquad
I_x=\sum_c n_c(\mathscr C_c,x)\in\mathbf Z.
\tag{1067.15}
$$
这包含 section 与 cusp 闭包相交的情形；只要求泛点不是 cusp。
所以
$$
v_{\mathfrak q}f_u(x)
 \equiv m(b+pI_x)-mb=0\pmod p.
\tag{1067.16}
$$
若在此位统一使用整参数，则左边准确为 $mpI_x$；
原全局参数至多再改一个 $p$ 倍。
所有 $m$ 个 cusp leading coefficients 都参与 (1067.14)，
没有仅证明某个未归一化 $u(x)$ 为 unit。

于是无条件得到
$$
\boxed{\quad
\Phi_x\in\mathscr L^0_{p,V}:=
\operatorname{Hom}_{\mathbf F_p[G]}(V,F(S_p,p))
\quad(x\in X(\mathbf Q)\setminus\Sigma).
\quad}
\tag{1067.17}
$$
这同时适用于非整 $j$、完整 $I_p$ 及变化的 normalizer 二次域。
对任意 $W\subset V$ 取限制亦成立。

不假设 regular 时，仍须保完整 exact sequence
$$
0\longrightarrow
\mathcal O_F[1/p]^\times/
       (\mathcal O_F[1/p]^\times)^p
\longrightarrow F(S_p,p)
\longrightarrow\operatorname{Cl}(\mathcal O_F[1/p])[p]
\longrightarrow0.
\tag{1067.18}
$$
本篇不从支撑缩小推断 irregular class-group 项消失。

## 5. Regular p：实际全局候选的唯一性与准确数量

以下假设 $p$ regular。R1065 §5 已用 Kummer criterion 与 degree-two
extension/norm 完整证明
$$
\operatorname{Cl}(F)[p]=0.
\tag{1067.19}
$$
令 $E=\mathcal O_F^\times$，$E_p=\mathcal O_F[1/p]^\times$。
唯一 $p$ 素位的 valuation module 是 trivial $G$-module。
完整 valuation exact sequence 张量 $\mathbf Z_p$ 后为
$$
0\longrightarrow E\otimes\mathbf Z_p
\longrightarrow E_p\otimes\mathbf Z_p
\longrightarrow\mathbf Z_p[\mathfrak p]\longrightarrow0.
\tag{1067.20}
$$
右侧 free，模 $p$ 不引入 Tor；$p\nmid|G|$ 允许整角色分解。
因此每个非平凡偶 $\chi$ 满足
$$
F(S_p,p)_\chi=(E/E^p)_\chi,\qquad
\dim_{\mathbf F_p}F(S_p,p)_\chi=1.
\tag{1067.21}
$$
R1062 §9 的原 circular-unit 对数计算，连同 regular Bernoulli 单位性，
已证明这条 global-unit 线向
$(K^\times/K^{\times p})_\chi$ 非零；后者也准确一维。
故 (1067.21) 的 localization 是同构。

因为 $W^G=0$，得到真正全局标签的同构
$$
\boxed{\quad
\operatorname{loc}_{\mathfrak p}:
\mathscr L^0_{p,W}:=\operatorname{Hom}_G(W,F(S_p,p))
 \xrightarrow{\;\sim\;}
\operatorname{Hom}_G(W,K^\times/K^{\times p}).
\quad}
\tag{1067.22}
$$
这个结论只在 regular $p$ 断言。它既保留 R1062 的 ambient 满射边界，
又严格消除了 R1065 因暂时容许 $2,3$ 而产生的额外全局核。

令 $Y_{W,\phi}\to X$ 为 R1064 的实际 twist。
其 $p$-点存在当且仅当 $\phi_{\mathfrak p}$ 属于
$\Phi_p(X(\mathbf Q_p))|_W$，所以由 (1067.22)
$$
\#\{\phi\in\mathscr L^0_{p,W}:Y_{W,\phi}(\mathbf Q_p)\ne\varnothing\}
 =\#\bigl(\Phi_p(X(\mathbf Q_p))|_W\bigr)
 \le p\,n_{\mathbf Q_p}(p).
\tag{1067.23}
$$
使用 R1065 §9 的准确 supersingular 类数计数：
$$
\boxed{\quad
\#\{\text{实际 }p\text{-local 非空的允许全局 twists}\}
 \le \frac{2p^{3/2}\log(4p)}{\pi}.
\quad}
\tag{1067.24}
$$
旧的 $p^{\kappa_p}$ 因子已删除，对 $2,3$ 在 $G$ 中的阶没有额外假设。
不同原圆盘可以有相同标签；因此不声称每个圆盘给不同 twist。

R1066 又给每个原圆盘一个实际 $\mathbf Q_p$-CM 代表，
判别式 $D'\le4p^{3/2}/\sqrt3$。
把该代表在指定 $\mathbf Q_p$ embedding 的局部标签通过
(1067.22) 逆像，便给对应的唯一全局候选。
这不是取 CM 数的 norm，也不把高次数 CM 代表称为 $\mathbf Q$ 点，
更不声称其所有全局共轭的 Kummer 类都等于这个候选。

## 6. 同一候选的实际圆单位坐标

本节仍假设 regular $p$。选择奇整数 $a$，其模 $p$ 的类在 $G$ 中生成 $G$，
并定义真正的实圆单位
$$
\eta_a=\zeta_p^{(1-a)/2}\frac{1-\zeta_p^a}{1-\zeta_p}\in E.
\tag{1067.25}
$$
不使用可能不是 global unit 的 $\eta_a/a$。
对每个实际出现的非平凡 $\chi$，置
$$
e_\chi=\frac1m\sum_{h\in G}\chi(h)^{-1}\sigma_h,\qquad
\beta_\chi=e_\chi[\eta_a]\in E/E^p.
\tag{1067.26}
$$
群环系数在 $\mathbf F_p$ 中解释。
$a$ 生成 $G$ 使 $\chi(a)-1\ne0$；
R1062 的 regular 局部计算使 $\beta_\chi$ 的 localization 非零，
所以它是 (1067.21) 的实际基。

在每条 $W_\chi$ 上固定 R1062/R1064 的函数基 $u_\chi$。
对原 $p$-disk 取任一 lift $x_p$；存在唯一 $c_\chi(x_p)\in\mathbf F_p$ 使
$$
\Phi_{x_p}(u_\chi)
 =c_\chi(x_p)\operatorname{loc}_{\mathfrak p}\beta_\chi.
\tag{1067.27}
$$
R1065 的 disk 恒定性保证 $c_\chi$ 不依赖该 lift。
同一个唯一全局候选准确为
$$
\phi_{x_p}(u_\chi)=c_\chi(x_p)\beta_\chi.
\tag{1067.28}
$$
这给全部原角色的明确 global-unit 坐标；没有另加未知的 $2,3$ 单位或
class-group lift。式 (1067.27) 是所需真实局部读数，
本篇并未凭标签计数声称已经算出所有 $c_\chi$。

## 7. 所有 l 不等于 p 的真实 étale twists 与辅助条件

§3–4 同时支付 R1064 辅助覆盖在 $2,3$ 处原先保留的接口。
在 $\mathfrak q\nmid p$ 的好模型上，
$\operatorname{div}(u^m/A(u))$ 的水平部分为 $mp\sum n_c\mathscr C_c$，
垂直系数由 (1067.14) 是 $p$ 倍。
调整一个局部 $p$ 次幂后，全部 divisor 系数都是 $p$ 的倍数。
局部从方程 $z^p=f_u$ 中去掉这些参数的 $p$ 次幂，
留下对单位取 $p$ 次根；因 $p$ 在此底环可逆，这是有限 étale。

常数 twist $\phi\in\mathscr L^0_{p,W}$ 在该位也有 $p$ 倍 valuation，
所以相同论证适用所有这些 twists。
$F/\mathbf Q$ 在 $\ell\ne p$ 未分歧，
实际 $G$-descent isomorphisms 沿规范化唯一延拓，
再由有限 étale descent 给原 $\mathbf Z_\ell$ 上的 finite étale cover。
因此
$$
\delta_\ell:X(\mathbf F_\ell)\longrightarrow
H^1(\mathbf F_\ell,H_W)
\tag{1067.29}
$$
在每个 $\ell\ne p$ 都是实际定义的完整点标签，
包括 cusp 的 leading-coefficient 值。

在 forced 角色 $W_{\chi_j}$、$\chi_j=\omega^{-2j}$ 上，
dual group 的角色仍为 $\omega^{2j+1}$，故
$$
H^1(\mathbf F_\ell,H_{\chi_j})=
\begin{cases}
\mathbf F_p,&\ell^{2j+1}\equiv1\pmod p,\\
0,&\text{否则}.
\end{cases}
\tag{1067.30}
$$
现在 (1067.30) 同样可用于 $\ell=2,3$。
可见不意味着标签非零，也不意味着 $\delta_\ell$ 满射。

R1064 的 visible quotient 证明逐项适用：
若可见角色数为 $s$，其 cover 几何连通、次数 $p^s$，
genus 为 $1+p^s(g_X-1)$；好模型上的 proper smooth 特殊化保几何连通。
于是
$$
\ell+1>2\bigl(1+p^s(g_X-1)\bigr)\sqrt\ell
\tag{1067.31}
$$
时，每个允许 twist 的该 visible quotient 都有 $\mathbf F_\ell$ 点。
$s=0$ 时不增加原 $X(\mathbf F_\ell)$ 本身之外的 Kummer 条件。
这些边界没有改变，改变的是它们现在覆盖全部 $\ell\ne p$。

## 8. 完全分裂辅助素的显式同标签方程

给定 regular $p$ 的某个原 $p$-disk，用 (1067.27) 固定其全部 $c_\chi$。
再选有理素数 $\ell\equiv1\bmod p$，以及
$z\in\mathbf F_\ell^\times$ 的一个原始 $p$ 次根。
$z$ 指定 $F$ 的一个 $\ell$ 上剩余嵌入；$z$ 与 $z^{-1}$ 给同一实嵌入。

对 $h\in G$ 选择代表，令 $e_{\chi,h}\in\mathbf Z$ 是
$m^{-1}\chi(h)^{-1}\in\mathbf F_p$ 的任意整数提升。置
$$
B_{\chi,z}=
\prod_{h\in G}
 \left(
 z^{h(1-a)/2}\frac{1-z^{ha}}{1-z^h}
 \right)^{e_{\chi,h}}
 \in\mathbf F_\ell^\times.
\tag{1067.32}
$$
每个括号非零；$a$ 为奇整数使指数确为整数。
用 $-h$ 替 $h$ 时括号不变，正是 $\eta_a$ 的实性。
改变 $e_{\chi,h}$ 的 $p$ 倍只改变一个 $p$ 次幂，
所以 $[B_{\chi,z}]$ 是 $\beta_\chi$ 的准确 residue class。

对该剩余嵌入，把原 $u_\chi$ 调整 vertical order 后约成 $\bar u_{\chi,z}$；
其除子是 $p$ 倍 cusp divisor。
对同一个 $y\in X(\mathbf F_\ell)$，在非 cusp 取实际值，在 cusp 取
同一整参数的 leading coefficient，统一记作 $\operatorname{ev}_y$。
若原有理点同时位于所选 $p$-disk、在 $\ell$ 处约成 $y$，
则必须有
$$
\boxed{
\left(
\frac{\operatorname{ev}_y(\bar u_{\chi,z})^m}
     {\prod_{c\in\Sigma}\operatorname{lc}_c(\bar u_{\chi,z})}
\right)^{(\ell-1)/p}
=
B_{\chi,z}^{\,c_\chi(\ell-1)/p}
\quad\text{在 }\mu_p(\mathbf F_\ell).
}
\tag{1067.33}
$$
这个等式对全部实际 $\chi$ 和全部剩余嵌入 $z$ 同时成立，
而 $y$ 必须是同一个有限域点。不能逐角色或逐嵌入另挑约化点。
$c_\chi$ 和群环系数的不同整数提升均不改变 (1067.33)。

式 (1067.33) 的右边仅由同一个原 $p$-disk 的规范标签和圆单位决定，
左边是 R1064 同一覆盖的原有限点读数。
这是可直接用于辅助排除的准确关系，
不是把 CM 共轭平均或一个任意 $S$-unit 代替原全局候选。
本文尚未证明对每个非 CM 候选存在一个 $\ell$ 使所有 $y$ 均不满足该式；
这仍是 O0 的实际未解输入。

## 来源与核读范围

- P. Deligne and M. Rapoport, *Les schémas de modules de courbes elliptiques*,
  in *Modular Functions of One Variable II*, Lecture Notes in Math. 349 (1973),
  143–316，[作者全文](https://www.math.uni-bonn.de/people/rapoport/myalggeom/preprints/Lesschemas.pdf)。
  本篇实读 IV Theorem 2.5（PDF 第68页／印刷210页）、
  IV Theorem 2.7、Corollary 2.9（PDF 第68–69页／印刷210–211页），
  以及 VII Corollary 2.4–2.5（PDF 第158–159页／印刷300–301页）的 cusp 完成环与稳定子。
  它们只提供 full-level 的 proper smooth scheme 和 finite étale cusps。
  本篇 §2 自证允许 wild stabilizer 的 coarse quotient；
  没有直接由一般 smooth stack 推 coarse smooth。
- R1062：全部实际 cusp 模块与 Galois 方向、无基点归一化、
  exact Kummer sequence，以及 regular circular-unit 局部非零。
- R1064：真实连通 $\mathbf Q$-torsor、twists、cusp 纤维、
  finite-field visibility 与 visible quotient。
- R1065 §§5、9：regular 时的 real class-group 项付款、
  原 $p$-disk 标签恒定及 $p\,n_{\mathbf Q_p}(p)$ 的准确界。
- R1066：同一个原 $p$-disk 的有界判别式 CM 代表；
  本篇只使用其指定局部 embedding，不取全局 norm 代替局部值。

局部商引理由 global_route 推导，root 与 o2_high_coefficient
分别纸核 Weierstrass 秩、Artin 固定域及完整 orbit completion；
原模型和全部 leading-coefficient 赋值相消由 root 独立核准。
