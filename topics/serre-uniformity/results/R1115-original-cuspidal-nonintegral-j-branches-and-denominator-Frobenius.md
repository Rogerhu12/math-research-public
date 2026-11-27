# R1115：原 cuspidal 候选的完整非整 j 局部分支与分母 Frobenius 约束

日期：2026-11-27（Asia/Taipei）。  
会话：Astra-serre-24b8836b-20261126；global_route，o2 独立纸核。

**已证明。** 对每个 $p>37$ 和一个固定的原 forced-good 全局标签，
在每个 $\ell\ne p$ 处是否存在与该标签相容、且 $j$ 非整的
$\mathbf Q_\ell$ 点，有一个精确的有限 Galois 判别。
$\ell\equiv1\pmod p$ 时，它要求同一个原 cusp 上的全部 Kummer
类同时消失；$\ell\equiv-1\pmod p$ 时，所有这些标签都在原 cusp
圆盘上相容；其它同余类没有非整 $j$ 分支。

原标签的非零坐标给这个 cusp 条件一个无条件的秩下界。
因此同一个全局候选的分母素数，受到一个明确的 Frobenius
共轭稳定集合限制，不仅受到 $\ell\equiv\pm1\pmod p$ 限制。
固定 $p=47$ 时，本子模块就是完整实际 $V$，每个 cusp 条件准确有
秩十，对全部 $235$ 个原候选成立。

这里的局部存在不等于全局有理点存在；允许分母素数的集合仍有
正密度，本文不证明分母为空、非 CM 点不存在或盘内唯一。
全文无数学程序执行。

## 1. 同一原候选、函数基及 cusp 类

置
$$
F=\mathbf Q(\zeta_p)^+,\quad K=\mathbf Q(\zeta_p),\quad
G=\operatorname{Gal}(F/\mathbf Q),\quad m=(p-1)/2,\quad
r=\lfloor p/4\rfloor-1.
\tag{1115.1}
$$
令
$$
\mathcal J=\{1\le j\le r:\ p\nmid B_{p-1-2j}\},\qquad
\chi_j=\omega^{-2j},\qquad
W=\bigoplus_{j\in\mathcal J}V_{\chi_j}.
\tag{1115.2}
$$
R1062 保证这些 forced 角色实际出现，R1069 保证其原 global-to-$p$
localization 为同构。本篇固定这个实际子覆盖；一般 $p$ 时不把
它冒称全部 $V$ 或全部 $W_{\rm good}$。

采用 R1064/R1070 的原函数基 $u_j$ 及 R1069 的同一个圆单位
$$
\eta_a=\zeta_p^{(1-a)/2}\frac{1-\zeta_p^a}{1-\zeta_p},
\qquad
\beta_j=e_{\chi_j}[\eta_a]\ne0.
\tag{1115.3}
$$
$a$ 是原来选定的奇整数，生成 $G$。
固定原全局候选
$$
\phi_c(u_j)=c_j\beta_j,\qquad c_j\in\mathbf F_p.
\tag{1115.4}
$$
若它来自 R1071 的某个原 $p$-圆盘，就使用那个圆盘的确定坐标，
不重新定标。任意原有理点给出这样一个候选。
一般完整标签只能推出其 (1115.4) 限制；下面所有局部等价首先指
这个明确的 $W$-标签。§7 的 $p=47$ 应用另付 $W=V$。

原 cusps 写作 $c_h=\sigma_hc_1$，$h\in G$。
保 R1064 的非平方 $\delta$ 及原范数坐标。
在 $F^\times/F^{\times p}$ 的加法记号中，置
$$
\varpi_1=(1-\zeta_p)(1-\zeta_p^{-1}),\qquad
\xi_j=e_{\chi_j^2}[\varpi_1],\qquad
a_j=\frac m2\chi_j(-\delta)^{-1}.
$$
全部 $\chi_j^2$ 非平凡，因为 $2r<m$。
所以 $\xi_j$ 是一个真正的全局单位类：其 $p$ 位 valuation 在
非平凡投影下消失，整数指数提升可调至 augmentation 恰为零。
允许 $\xi_j=0$，不预设 irregular 时的圆单位非零。

由 R1064 (1064.24)，原 cusp 的真实规范标签准确为
$a_j\chi_j(h)\xi_j$。因此其在原 twist $Y_{W,\phi_c}$ 中的
纤维类是
$$
\boxed{\quad
\gamma_{h,j}=a_j\chi_j(h)\xi_j-c_j\beta_j,
\qquad
B_{c,h}=\operatorname{span}_{\mathbf F_p}
             \{\gamma_{h,j}:j\in\mathcal J\}.
\quad}
\tag{1115.5}
$$
这里已经包含全部 cusp leading coefficients 的归一化。
没有用未归一化 Siegel 常数或单个 division polynomial 代替它。

## 2. 原整模型上，非整 j 恰对应 cusp 圆盘

R1067 §§2–3 给原完整 $X=X_{\rm ns}^+(p)$ 在每个 $\ell\ne p$ 的
smooth proper coarse 模型；全部 cusp 闭包 finite étale。
该证明包括 $\ell=2,3$，没有以 tame stabilizer 假设跳过它们。

忘掉 level 的 $j$-态射从实际 full-level compactification 到
$\mathbf P^1_{\mathbf Z_\ell}$ 定义，并沿原有限群商下降。
其极点只在 cusp 边界。
这一点也可在原 Tate chart 直接检查：在包含 $\zeta_p$ 的未分歧
底环上，原 cusp 参数是 $t=q_{\rm Tate}^{1/p}$；R1067 中 quotient
在 cusp 处 étale，故 cusp width 仍为 $p$，且
$$
j=t^{-p}+744+O(t^p).
\tag{1115.6}
$$
换成任意整相对参数只改 leading unit，不引入 vertical 极点。
在非 cusp 开集，$j$ 是实际 generalized-elliptic-curve
moduli 的整函数。因此对任意非 cusp 的 $x\in X(\mathbf Q_\ell)$，
properness 给的 section 满足
$$
v_\ell(j(x))<0
\quad\Longleftrightarrow\quad
\bar x\text{ 是一个 }\mathbf F_\ell\text{-rational cusp}.
\tag{1115.7}
$$
从 Tate 曲线方向看，负赋值的 $j$ 给 $|q_{\rm Tate}|<1$，
所以 full-level 提升在 (1115.6) 的边界约化；商后仍是该 cusp。
这没有假定所给 $\mathbf Q_\ell$ 点本来有一个全水平基。

原 cusp 集是 $G$ 的简单传递集合。它在 $\ell$ 处的 Frobenius
作用是 $\sigma_\ell$，所以
$$
\Sigma(\mathbf F_\ell)\ne\varnothing
\quad\Longleftrightarrow\quad
\ell\equiv\pm1\pmod p.
\tag{1115.8}
$$
满足此式时，全部 $m$ 个 cusps 均在 $\mathbf F_\ell$ 上有理，
其完成局部环为 $\mathbf Z_\ell[[t_h]]$。
原 $j$ 在此环中为 $t_h^{-p}$ 乘单位，因而
$$
v_\ell(j(x))=-p\,v_\ell(t_h(x))
\quad\text{对非 cusp 的 }x\text{ 在该圆盘中成立}.
\tag{1115.9}
$$
特别 $p>37$ 时 $2,3$ 均不是 $\pm1\bmod p$；
这两个素数没有例外的非整 $j$ 分支。

## 3. 同一 cusp 的完整标签与整圆盘 Hensel 等价

R1067 §7 已付原 $Y_{W,\phi_c}\to X$ 在所有 $\ell\ne p$
延拓为有限 étale torsor：原规范函数的水平和垂直 divisor 均为
$p$ 倍，常数 twist 只在 $p$ 支撑。
因此不能在本节另加 $2,3$，或忽略 twist 的整延拓。

给定一个 $\mathbf F_\ell$-rational cusp $c_h$，
由 (1115.8)，$F$ 在 $\ell$ 完全分裂。
torsor 在整个 $c_h$ 的 $\mathbf Q_\ell$ residue disc 上的类
等于其特殊纤维类。可以直接用 (1115.6) 的整参数证明：
去掉规范函数的参数 $p$ 次幂后，余下
$a_hv(t_h)$，其中 $v(0)=1$；若 $t_h\in\ell\mathbf Z_\ell$，
则 $v(t_h)\in1+\ell\mathbf Z_\ell$。
由于 $p$ 在 $\mathbf Z_\ell$ 中可逆，$p$ 次幂映射在这个 principal
unit 群上是同构，所以没有额外的深层 Kummer 条件。
在一般下降记号中，这正是 finite étale torsor 的 Hensel 性质。

于是
$$
\begin{split}
&\exists x_\ell\in(X\setminus\Sigma)(\mathbf Q_\ell):
 \bar x_\ell=c_h,\ v_\ell(j(x_\ell))<0,\
 \Phi_{x_\ell}|_W=\operatorname{loc}_\ell\phi_c\\
&\qquad\Longleftrightarrow\qquad
Y_{W,\phi_c}|_{c_h}(\mathbf F_\ell)\ne\varnothing.
\end{split}
\tag{1115.10}
$$
若右边成立，整个原 residue disc 都相容；
取任意 $t_h=\ell^n$ 乘单位、$n\ge1$，便给负赋值 $-pn$ 的
非 cusp 局部点。这里只构造局部点。

当 $\ell\equiv1\bmod p$，$F,K$ 均在 $\ell$ 完全分裂。
选择一个实际剩余嵌入 $\zeta_p\mapsto z$ 后，
(1115.10) 准确等价于
$$
\operatorname{loc}_{\ell,z}\gamma_{h,j}=0
\quad\text{对全部 }j\in\mathcal J.
\tag{1115.11}
$$
必须是同一个 $h$ 同时满足所有等式；
不允许每个角色另选一个 cusp。

当 $\ell\equiv-1\bmod p$，$F$ 仍完全分裂，
但 $\mathbf F_\ell^\times/\mathbf F_\ell^{\times p}=0$。
(1115.5) 中的类都是单位，故它们的 localization 全为零，
对每个 $c$ 和每个 $h$ 都成立。
等价地，原 $H_W=\operatorname{Hom}(W,\mu_p)$ 的 Frobenius
在每个分量上为 $-1$，所以 $H^1(\mathbf F_\ell,H_W)=0$。
因此这些素数处全部 $m$ 个原 cusp 圆盘都与每个原候选相容。
这条不可删除的分支阻止从本篇推出分母消失。

## 4. 逐候选的无条件秩下界

对 $b\in G$，实际 Galois 作用给
$$
\sigma_b\gamma_{h,j}=\chi_j(b)\gamma_{bh,j}.
\tag{1115.12}
$$
因为 $\xi_j$ 的角色是 $\chi_j^2$，$\beta_j$ 的角色是 $\chi_j$。
所以所有 $B_{c,h}$ 维数相同，记为 $\rho_c$。

令
$$
s(c)=\#\{j\in\mathcal J:c_j\ne0\}.
$$
则无条件有
$$
\boxed{\rho_c\ge s(c).}
\tag{1115.13}
$$
证明只取 $c_j\ne0$ 的行，假设它们有非零线性关系。
取系数非零的最小指标 $j$，投影到 $\chi_j$。
别的 $\beta_i$ 只能在 $i=j$ 贡献；
别的平方源 $\xi_i$ 若贡献，必须
$2i\equiv j\pmod m$。由于 $2i\le2r<m$，
此式只能是 $i=j/2<j$，其系数已为零。
所以只剩 $-c_j\beta_j$ 乘非零系数，与 $\beta_j\ne0$ 矛盾。
本证明不要求任何 $\xi_i$ 非零，也不假设 regularity。

另一个不同的满秩条件是：
若取全部 $1\le j\le r$，且全部 $\xi_j\ne0$，
则不论 $c_j$ 是否为零，都有 $\rho_c=r$。
此时对关系取最大指标 $j$，投影到 $\chi_{2j}$。
平方角色之间无碰撞，而可能的另一普通角色只能来自
$i=2j>j$，所以只有第 $j$ 项，矛盾。
regular $p$ 时该非零条件已由 R1064 (1064.25) 和 §5 支付；
不能仅由 (1115.13) 或“forced-good”一词推出它。

## 5. 精确的同点 Frobenius 判别及密度

把 (1115.5) 看作 $K^\times/K^{\times p}$ 中的类；
$F\to K$ restriction 的单射由 norm 乘二保证。
置
$$
B_c=\sum_{h\in G}B_{c,h},\quad t_c=\dim_{\mathbf F_p}B_c,\quad
M_c=K(\epsilon^{1/p}:[\epsilon]\in B_c).
$$
每个类可选实际全局单位代表。由 (1115.12)，$B_c$ Galois-stable，
所以 $M_c/\mathbf Q$ 是有限 Galois 扩张，在 $p$ 外未分歧，且
$$
H_c=\operatorname{Gal}(M_c/K)=\operatorname{Hom}(B_c,\mu_p),
\qquad |H_c|=p^{t_c}.
\tag{1115.14}
$$
配对是 R1112 的原 arithmetic Frobenius/Kummer residue 配对。

定义
$$
S_c=\bigcup_{h\in G}
 \operatorname{Ann}_{H_c}(B_{c,h})\subset H_c.
\tag{1115.15}
$$
(1115.12) 保证整个并集在
$\operatorname{Gal}(M_c/\mathbf Q)$ 下共轭稳定。
对 $\ell\equiv1\bmod p$，(1115.10)–(1115.11) 准确给
$$
\boxed{
\begin{array}{c}
\exists x_\ell\in(X\setminus\Sigma)(\mathbf Q_\ell),\
 v_\ell(j(x_\ell))<0,\
 \Phi_{x_\ell}|_W=\operatorname{loc}_\ell\phi_c
\\[2pt]\Longleftrightarrow\\[-1pt]
\operatorname{Frob}_\ell(M_c/\mathbf Q)\subset S_c.
\end{array}}
\tag{1115.16}
$$
选择别的 $\zeta_p$ 剩余嵌入只共轭 Frobenius，不改变此判据。

各 annihilator 的大小恰为 $p^{t_c-\rho_c}$，所以 Chebotarev 给
允许的 split 非整分支素集合准确 Dirichlet 密度
$$
\delta_c^+=\frac{|S_c|}{(p-1)p^{t_c}}
 \le\min\left\{\frac1{p-1},\,\frac1{2p^{\rho_c}}\right\}.
\tag{1115.17}
$$
并集中的不同 cusp 可相交，本文不把这个上界写成等号。
在 split primes 中，相容 cusp 圆盘数的 Dirichlet 平均值准确为
$m/p^{\rho_c}$，因为对每个固定 $h$，其 annihilator 的相对比例
都是 $p^{-\rho_c}$；这个平均式是对共轭不变函数
$g\mapsto\#\{h:g\in\operatorname{Ann}(B_{c,h})\}$ 的群平均，
不需假定各 cusp 条件独立。

把 $\ell\equiv-1\bmod p$ 的整支加回，得到本原候选
允许非整 $j$ 局部分支的素集合 $\mathcal P_c$：
$$
\delta(\mathcal P_c)=\frac1{p-1}+\delta_c^+
 \le\frac1{p-1}
   +\min\left\{\frac1{p-1},\,\frac1{2p^{\rho_c}}\right\}.
\tag{1115.18}
$$
若 $s(c)>0$，右边可用 $s(c)$ 代替 $\rho_c$。
若 $s(c)=0$，保留 (1115.17) 的最小值，不能用一个过大的松界
声称新的筛选力。

这些是“允许的分母素集合”的密度，不是某个固定有理数有限
分母支撑的密度。零元素总属于 $S_c$，所以 (1115.17) 本身也是
正密度集合；本文没有证明它为空。

## 6. 原全局有理点的实际分母约束

若 $x\in X(\mathbf Q)$ 的原 $W$-标签为 $c$，则对每个
$\ell\ne p$，负 $j$ 赋值必须满足 (1115.9) 和 (1115.16)。
R1065 §§2–3 的实际最小正则模型又给 $j(x)\in\mathbf Z_p$：
所有 $\mathbf Q_p$ sections 落在 smooth 外端，那里原
$j$-态射的特殊值有限。

因此写约分后的 $j(x)$，存在互素整数 $A,B$、$B>0$，使
$$
j(x)=\frac A{B^p},\qquad
\{\ell:\ell\mid B\}\subset\mathcal P_c.
\tag{1115.19}
$$
$B=1$ 和 $j=0$ 当然允许。
$p$ 次幂分母与 $\ell\equiv\pm1$ 是原 cusp 宽度的局部事实；
本篇新增的是同一个实际全局候选 $c$ 对
$\mathcal P_c$ 的具体 Kummer-Frobenius 限制。

一般 $W$ 只是原 good 模块的子模块，因此 (1115.19) 是完整
有理点的必要条件，不能说它付清其它角色的局部条件。
也不能从每个 $\ell$ 分别存在 (1115.16) 的局部点，
推出一个共同的全局有理点。

## 7. 原 p47 的完整十角色：每个 cusp 条件秩十

R1072 已认证 $p=47$ 时
$$
V=W=\bigoplus_{j=1}^{10}V_{\omega^{-2j}},
$$
全部十角色 good，全部 $235$ 个原 $p$-圆盘给出 $235$ 个互异
完整全局候选。因此本节的 (1115.16) 检查的是全部原 $V$，
不再只是一个有缺失角色的投影。

这些 $\chi_j^2$ 的偶指数为
$$
42,38,34,30,26,22,18,14,10,6.
\tag{1115.20}
$$
前五个的 Bernoulli-good 性已经包含在 R1072 原回执中。
其余五个由 NIST DLMF Table 24.2.3 的准确值给出：
$$
B_6=\frac1{42},\quad B_{10}=\frac5{66},\quad
B_{14}=\frac76,\quad B_{18}=\frac{43867}{798},\quad
B_{22}=\frac{854513}{138}.
$$
全部分母与 $47$ 互素；后两个分子准确为
$43867=47\cdot933+16$、$854513=47\cdot18181+6$，
其余分子也非零模 $47$。
所以 (1115.20) 的全部十个圆单位分量都非零：
这里只用 R1062 的 Bernoulli-unit 圆单位局部式及
R1064 (1064.26)，不把这些平方角色全部宣为 $V$ 中的角色。

§4 的最大指标证明遂给
$$
\boxed{\rho_c=10\quad\text{对全部 }235\text{ 个原候选成立}.}
\tag{1115.21}
$$
不需要逐候选重新运行一个秩程序，也不要求其 $c_j$ 全非零。
于是对每一个候选，(1115.18) 为
$$
\delta(\mathcal P_c)\le
 \frac1{46}+\frac1{2\cdot47^{10}}.
\tag{1115.22}
$$
其中 $\ell\equiv-1\bmod47$ 的 $1/46$ 分支准确保留。
例如只知道分母素数全在这个分支，仍与本篇的全部条件相容；
不据 (1115.22) 推断原有理点的 $j$ 必整。

## 8. 多候选的共同 cusp 排除素与边界

这一节只排 cusp 圆盘，不排 affine 有限域点。

对一个实际有限候选集合 $\mathcal C$，把全部 $B_c$ 及所用
原 $\beta_j$ 放进同一个 Kummer 空间，得到一个共同有限
Galois 扩张 $M/K$。每个 $B_{c,h}$ 在该空间中仍有原秩，
其 annihilator 仍有相对比例 $p^{-\rho_c}$。
若所用 good 角色数为 $d$，全部 $\beta_j$ 读数非零的
Frobenius 子集比例准确为 $(1-1/p)^d$。
所以同时满足
“全部原读数非零”及
“没有任何 $c\in\mathcal C$ 与任何一个 cusp 相容”
的 split primes，Dirichlet 密度至少为
$$
\frac1{p-1}
\left((1-1/p)^d-\sum_{c\in\mathcal C}\frac m{p^{\rho_c}}\right),
\tag{1115.23}
$$
只在括号为正时断言正密度。
证明是对这些实际 annihilator 子空间取并集的计数上界，
没有假设不同候选或不同 cusp 事件独立。
每个事件已由 (1115.12) 保证共轭稳定，
因此可以对同一个有理辅助素应用 Chebotarev。

固定 $47$，取 R1072 的全部 $235$ 个候选，(1115.23) 给
$$
\frac1{46}
 \left((46/47)^{10}-\frac{235\cdot23}{47^{10}}\right)>0.
\tag{1115.24}
$$
其正性可直接纸核：
$(46/47)^{10}\ge1-10/47=37/47$，
而 $235\cdot23<47^3$。
所以存在正密度辅助素，原全部 $235$ 个候选在这些素数处保持
彼此不同，同时没有一个可通过原 $23$ 个 cusps 的任何一个。
这付清一个真实的“同一点”边界排除，而不以逐角色的不同 cusps
拼接出假相容。

还可要求在 R1112 §8 的实际 full47 场 $E$ 完全分裂。
该场在 $K$ 上次数与 $47$ 互素，而 $M/K$ 是 $47$-扩张，
故 $M\cap E=K$。同一计数在分裂于 $E$ 的 primes 中不变，
(1115.24) 的分母 $46$ 换成 $[E:\mathbf Q]$。
因此八 CM 普通、全 Hecke 一次分裂、十原圆单位非零和上述
共同 cusp 排除之间没有新的 Galois 冲突。

一般全 $p$ 时，若只取 $\rho_c\ge4$ 的实际候选子集，
R1065/R1069 的候选数上界小于 $p^2$，而 $m<p$，
所以 (1115.23) 中的扣除项小于 $1/p$。
又 $(1-1/p)^d>1/2$，故对这个子集也得到正密度共同 cusp
排除素。由 (1115.13)，原 forced-good 坐标至少四个非零的
候选属于该子集。未满足这个条件的候选仍须保留。

本节没有最小辅助素的有效上界，也没有断言这些 primes 落在
R1064 的有限有效筛选范围。事实上足够大的好 primes 上每个
twist 都有 affine 点，并不与 cusp 全部排除矛盾。
本文不改变已经执行的 $283,4513$ 筛选、对数、高度或正在运行的
Miller 计算；没有搜索或运行替代辅助素。

## 来源与审核范围

- R1064 §§1–5：同一真实 torsor、原 cusp 标签
  $(m/2)\chi(h)\chi(-\delta)^{-1}e_{\chi^2}[\varpi_1]$，
  完整 norm 和原 $\chi^2$ 方向。
- R1067 §§2–4、7：所有 $\ell\ne p$ 的实际 smooth proper 模型、
  finite étale cusp 边界及全部规范 twists 的整延拓；
  其中已亲读的 Deligne–Rapoport IV Theorem 2.5/2.7、VII
  Corollary 2.4–2.5 给原 full-level/Tate chart。
- R1065 §§2–3、R1069：原 $p$-local 候选、$p$ 处整 $j$ 及
  forced-good 的唯一全局单位坐标。
- R1072：固定 $47$ 的完整 $V$、235 个实际候选和原 good 回执。
- R1112：实际 Kummer pairing、$\omega\chi^{-1}$、
  arithmetic Frobenius、共轭稳定集的 Dirichlet 密度；
  本篇只消费其已证明的一般理论，不重跑计算。
- NIST DLMF §24.2(iv), Tables 24.2.1、24.2.3：
  https://dlmf.nist.gov/24.2#T3 ，已亲读 $B_6,B_{10},B_{14},B_{18},B_{22}$
  的准确分数。这里只用这五个值，余数的短乘法在 §7 明列。

o2 已独立纸核 (1115.12) 的真实 Galois 方向、
(1115.13) 无回卷的最小指标证明及并集密度；
regular/fullforced 的满秩另外保原平方圆单位非零前提。
数学程序执行为零。
