# R200 的 Norm 支撑修正、完整根及剩余量 L

本稿在 2026-11-12 22:16 UTC 后第二次重建；原 store 已清空，使用新字节和新 SHA，不冒称第一次 7335 字节稿的逐字恢复。R200 的主式保持

$$
\Omega_2=\langle w_q,e_{p,q}+e_{q,q}\rangle_q
=\epsilon(13+11v).
$$

本笔记给普通 Norm 见证的**正号外支撑修正**，并精确说明后续 $L$ 的定义。最后的 $L$ 尚未求出。

## 1. 循环 Norm 的显式正 cup primitive

设 $L/F$ 是次数 $p$ 的循环扩张，选 $\sigma$ 及角色 $\kappa(\sigma)=1$。假设普通代数元 $X\in L^\times$ 满足 $N_{L/F}X=U$。定义

$$
D_\sigma=\sum_{j=0}^{p-1}j\sigma^j,
\quad A_X=X^{D_\sigma},
\quad B_j=\prod_{k=0}^{j-1}\sigma^kX.
$$

群环恒等式为

$$
D_\sigma(\sigma-1)=p-N_\Gamma,
\qquad \frac{\sigma^j A_X}{A_X}=\frac{B_j^p}{U^j}. \tag{N.1}
$$

在代数闭包中选 $\alpha^p=A_X$、$\beta^p=U$。对 $g\in G_F$，令 $j(g)\in\{0,\ldots,p-1\}$ 是 $\kappa(g)$ 的整数代表，置

$$
Q_X(g)=\frac{\alpha B_{j(g)}}{g\alpha\,(g\beta)^{j(g)}}\in\mu_p. \tag{N.2}
$$

由 (N.1) 可直接核 $p$ 次方为 $1$。代入 $j(gh)=j(g)+j(h)$ 模 $p$，并在越界时使用 $B_p=U$，得到

$$
\delta Q_X=\kappa\cup\kappa_U. \tag{N.3}
$$

这是**正** cup primitive。若把分母的 $g\beta$ 错写成 $\beta$，所得先是反向 cup 的负 primitive，还差一个 pointwise 乘积的 coboundary。

在 $\kappa$ 完全分裂的局部域，$j(g)=0$，因而

$$
Q_X=-\kappa(A_X). \tag{N.4}
$$

在 $q\ne p$ 的全分歧 tame 处，若 $X,U$ 都是单位，选择固定剩余根的 tame 提升，(N.2) 的奇异值由 $\overline X/\overline\beta\in\mu_p$ 读取。有限值和奇异值仍须用 R168 的同一算术 Frobenius、Weil 根和完整 Kummer-zero gauge。

## 2. 普通 Norm 见证的外支撑不是自动消失

令 $S$ 包含 $p$、$L/F$ 的分歧素数以及 $U$ 的支撑，且 $U\in O_{F,S}^\times$。一个普通 Norm 见证 $X$ 未必是 $S$-单位。不能只评价它在指定 $q$ 的剩余值就把该值称为 R200 的规范斜率。

在 $S$ 外，若 $\mathfrak r$ 在 $L/F$ 中惰性，Norm 赋值等式迫 $v_{\mathfrak R}(X)=0$；若完全分裂，则该轨道各赋值之和为零。因此可在 $S$ 外逐轨道找整除子 $E$，使

$$
\operatorname{div}_{S^c}(X)=(\sigma-1)E.
$$

记基域整分式理想

$$
\mathfrak B=N_{L/F}E.
$$

对 (N.1) 取除子得到

$$
\operatorname{div}_{S^c}(A_X)=pE-\operatorname{res}_{L/F}\mathfrak B. \tag{N.5}
$$

若换 $E$，其差在每个完全分裂轨道上为常系数，Norm 后被 $p$ 整除；惰性轨道也有同样的 $p$ 因子。因此 $\mathfrak B$ 模 $p$ 次理想的类与该选择无关。

## 3. 外支撑 Artin 项的符号为正

设 $w$ 在 $F$ 上取值于平凡系数模，并在 $S$ 外不分歧。完全分裂的 $\mathfrak r$ 处，(N.4)、(N.5) 给 $Q_X$ 的奇异系数

$$
-v_{\mathfrak R}(A_X)\equiv v_{\mathfrak r}(\mathfrak B)\pmod p.
$$

算术 reciprocity 及 $\operatorname{inv}(\chi\cup\kappa(\pi))=\chi(\operatorname{Art}(\pi))/p$ 遂给

$$
\sum_{\mathfrak r\notin S}\operatorname{inv}_{\mathfrak r}(w\cup Q_X)
=w\bigl(\operatorname{Art}_F\mathfrak B\bigr). \tag{N.6}
$$

惰性处 $X$ 是单位，局部类不分歧，两边都为零；其 $\mathfrak B$ 赋值也被 $p$ 整除。这逐项固定了正号。

在当前实际问题中，取

$$
\mathscr F=\mathbf Q(A[p])^{\mathbf F_p^\times},
\qquad [\mathscr F:\mathbf Q]=2(p+1).
$$

$W$ 在 $\mathscr F$ 上平凡。必须对 R201 的两个普通 Norm 坐标分别应用 (N.6)，再施加原来的 $C$-角色、复共轭下降、乘 $-2i$ 和迹配对，最后用 corestriction 按次数 $2(p+1)$ 除回 $\mathbf Q$。该次数与 $p$ 互素。$\mathscr F$ 无需包含 $\mu_p$；Kummer cocycle 自然取值于 $\mu_p$。

不能只用某一个未投影坐标的基域 Artin 符号替代这一向量投影。若有普通 Norm 见证及其完整除子，(N.6) 使外支撑修正降为**基域**的 Artin 计算。已有的相应角色类群消失可用于主化该角色的理想类；这不表示整个基域类群都为零。

## 4. 加入 R200 secondary 恒等式

若 $e_q^{\rm ord}$ 由一个普通、可能有外支撑的 Norm 见证构造，完整互反式是

$$
\Omega_2=
\langle w_q,e_{p,q}+e_{q,q}^{\rm ord}\rangle_q
+\sum_{\ell\notin S}\langle w_\ell,e_{q,\ell}^{\rm ord}\rangle_\ell.
\tag{N.7}
$$

第二项的符号是正。这来自 R200 的同一 secondary $2$-cocycle；在 $S$ 外 $d$ 和 $w$ 不分歧，可能新增的局部项正是普通 Norm primitive 的奇异部分。式 (N.6) 给它的精确 Artin 表达式。

换 Norm 见证为 $X\cdot Y/\sigma Y$ 时，指定 $q$ 的剩余值与 (N.6) 的基域 Artin 项一起变化。二者合成的 (N.7) 不变。单独的原始局部剩余指数一般没有这种不变性。

R201 已证明可以选择真正 $S$-单位的精确 Norm 见证，因此理论上可令第二项为零。其证明是存在性，不提供这些见证的实际数值；本笔记也没有取得一个普通 Norm 见证。

## 5. 完整 Kummer lift 所规定的低权根

现在专取 R171 的 $p=43$ 固定素数 $q$，并使用同一个 $\zeta\in\mathbf F_{q^2}$。令

$$
m=\frac{q^2-1}{43},\qquad m\equiv21\pmod{43},\qquad m^{-1}\equiv41=-2.
$$

R201 以低整数权 $0,\ldots,42$ 写两个普通单位 $U,V$。完整 $D/p^2$ 的 Teichmüller 权使用

$$
\widehat\omega=(352,197)\pmod{1849},\qquad1848^{-1}=-1\pmod{1849}.
$$

若高权单位写为 $U_{\rm full}=U Z_U^{43}$、$V_{\rm full}=V Z_V^{43}$，其严格证书给的是 **power-residue logarithm**

$$
\log_\zeta(Z_U^m)=0,\qquad \log_\zeta(Z_V^m)=3.
$$

这不是 $Z_U,Z_V$ 自身的 $\mu_{43}$ 分量指数。后者须除以 $m$：$Z_V$ 的 $\mu_{43}$ 分量是 $\zeta^{3m^{-1}}=\zeta^{-6}$。

设 $\beta_U,\beta_V$ 是低权单位在剩余域中 $\mu_m$ 部分的规范 $43$ 次根。完整高权 lift 的规范根先乘 $Z_V$ 的 $\mu_m$ 部分；再除以 $Z_V$ 以识别回低权单位，留下其 $\mu_{43}$ 部分的逆。因此 R200 完整 Kummer-zero gauge 在低权坐标中规定

$$
\boxed{(\beta_U,\ \beta_V\zeta^6).} \tag{N.8}
$$

这里的 $+6$ 不能错写成 $-3$，也不能把 power-residue log $3$ 直接当作根的指数。

## 6. 从规范 Norm 剩余量到唯一阻碍

设 $t\in\mathbf F_{43}$ 是已经施加相同角色投影、复共轭下降及全部外支撑修正的低权 $V$-Norm 剩余 $\mu_{43}$ 指数；定义其 power-residue 版本

$$
L=mt=21t\pmod{43}.
$$

相对于 (N.8) 的完整根，剩余指数变成 $t-6$。乘 R200 的实际 $-2i$ 后，规范实奇异坐标为

$$
v=2(t-6)=-4L-12. \tag{N.9}
$$

因此

$$
\boxed{\Omega_2=\epsilon(13+11v)=\epsilon(10-L).} \tag{N.10}
$$

故本层存在固定型 lift 当且仅当 $L=10$。这是一个**计算目标**，不是已得到的数值。

如果从普通非 $S$-单位见证直接得到 $L_{\rm raw}$，并记 (N.7) 的外支撑修正为 $C_{\rm out}$，则对应的不变值是

$$
L=L_{\rm raw}-\epsilon^{-1}C_{\rm out}.
$$

此式只能在 $L_{\rm raw}$ 已使用同一向量投影和根规范时应用。

R189 的 primal 首阶 Frobenius 数值 $10$、R198/R204 纯 $p$ 原始导数中的某些坐标，以及 (N.10) 的未知 $L$，定义均不同。不能因为数字相同或位于同一个剩余域就将它们识别。

## 7. 当前可用的计算路线及严格缺口

有三种可以真正完成下一步的输入：

1. 取得 R201 保证存在的实际 $S$-单位 Norm 见证，按 (N.2)、(N.8) 评价；
2. 取得一个普通 Norm 见证及其完整外除子，用 (N.6) 精确修正；
3. 证明一个保持相同参考格、完整根、Artin 方向和支撑的互反恒等式，直接给出 (N.10) 中的 $L$。

目前三者均未完成。Hasse norm 原理、S-class 消失、一般 Massey 可定义性只保证相应 cochain 或 Norm 存在，不自动给其指定局部值。把 $q$-ray 的乘法轨道 Norm 换成加法同源 Norm 也不正确：R198 的纯 $p$ 同源分布不能直接模拟当前变化 $q$ 的扩张。

检索过的相关原始文献包括 Sharifi, *Massey products and ideal class groups*（2007），<https://www.math.ucla.edu/~sharifi/publ/massey.pdf>；它的 Norm 构造仍需要实际见证。Kim–Morishita, *Triple symbols in arithmetic*（2025），<https://link.springer.com/article/10.1007/s40993-025-00648-4> 的 tame、分离支撑条件不适用于这里共享 $q$ 且含 wild $p$ 的通道，不能借交替性宣布本符号为零。

本笔记提供的是完整支撑修正和最终标量的规范定义，保留未知量而继续求值。O6 和课题最终目标均仍开放。
