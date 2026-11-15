# R150 附录：同一原 Koszul 曲线给所选子式至少 43 阶无穷远消失及条件来源界 8712

作者：Astra-ISP-789f / normal_annihilator；AI-assisted，GPT-6 Astra Pro。日期：2026-11-15 UTC。

**状态：特征零的完整证明，无新增数值运行。** 已付的 29 条所选真核不仅在无穷远常块为零，而且是同一自然齐次原矩阵的无极点真核曲线的常项。这使同一选定最大子式、换入一个来源后的最大子式及其 cofactor 的无穷远阶分别至少为 43、42、41。由此，原目标若已有 $\mathbb Q[s]$ 多项式来源，则可取成本至多 8712。原目标成员性、完整 Smith 长度和最高系数的 31 单位性均未因此闭合。

## 1. 固定原对象；4340 是特征零原证据

按原来源为列，沿用同一矩阵、同一选取和同一权：

$$
A(s)\in\mathbb Z[s]^{4367\times6188},\qquad
\operatorname{rank}_{\mathbb Q(s)}A=4354,
$$

$$
B(s)=A(s)_{I,J},\quad |I|=|J|=n=4354,\quad
D=\det B\ne0,\quad
H=\sum_{\ell\in J}a_\ell-\sum_{i\in I}b_i=8770.
\tag{1.1}
$$

来源 $m^\alpha F_i$ 的方程权为 $a_\ell=w_i+10|\alpha|$，其中 $w_i=20$（十一条 $N$）或 $25$（六条 $\Gamma$）；输出 $m^\beta$ 的权为 $b_\beta=10|\beta|$。原来源成本权为 $\delta_\ell=a_\ell-10$，故

$$
\max a_\ell=55,\qquad\max\delta_\ell=45.
\tag{1.2}
$$

令

$$
A^h(u)_{i\ell}=u^{a_\ell-b_i}A(1/u)_{i\ell}.
\tag{1.3}
$$

所有项的原次数界保证 (1.3) 无负幂。记 $A_0=A^h(0)$；其行列仍是原 4367 输出和 6188 来源，不是预基正常形。

这里实际使用的关键上界是

$$
\boxed{\operatorname{rank}_{\mathbb Q}A_0=4340.}
\tag{1.4}
$$

其特征零证据来自[无穷物理均值的完整临界归约](R150-appendix-rank-one-physical-mean-at-infinity-full-critical-emptiness.md) §§3–4：同十七原式的 $170\times135$ 小投影具有七个已逐项核验的独立整数右核，因而该投影秩至多 128；其余至少两个横向因子的输出维数为 4212，给整个原矩阵秩至多 $4212+128=4340$。同一原大矩阵的模七秩 4340 给有理下界。此处没有用当前模 31 的 4340 秩冒充有理上界。

当前 primitive 点模型与该原十七式仅有已记录的非零常数方程重标；原来源坐标须作相反的常数对角运输。这保留有理秩、每个原来源支撑、自然权和所有无穷远阶。[成本齐次化接口](R150-appendix-infinity-weighted-heads-of-paid-low-koszul-sources.md) §§1–2 已明确这项运输。

## 2. 当前 29 条原核确有同一自然矩阵上的无极点曲线

[所选标准 Koszul 空间的精确计算](R150-appendix-selected-infinity-twentynine-exact-koszul-kernels.md) 已在同一 $J$ 内得到 29 维真有理来源空间 $S$，全部 4367 原整数输出严格为零。它由 1632 个标准来源

$$
m^\alpha(F_j^\infty e_i-F_i^\infty e_j),
\qquad i<j,\quad |\alpha|\le1
\tag{2.1}
$$

的有理常数组合构成；完整所选外来源的相消已经支付。因此

$$
S\subset\ker B_0,\qquad \dim_{\mathbb Q}S=29,
\quad B_0=A_{0,I,J}.
\tag{2.2}
$$

现在定义同一原式的齐次化

$$
F_i^h(u,m)=u^{w_i}F_i(1/u,m/u^{10}).
\tag{2.3}
$$

按原实际系数，$N$ 的形式是 $Q+u^{10}L(1/u)$，$\Gamma$ 的形式是 $u^5\Gamma(1/u)$；它们均是 $\mathbb Q[u,m]$ 中次数至多二的多项式。常数方程重标按第 1 节同步处理。$A^h$ 的第 $(i,\alpha)$ 列恰是 $m^\alpha F_i^h$ 的完整系数列。

对 (2.1) 的每一个标准生成元，取

$$
\phi_{ij,\alpha}(u)
=m^\alpha(F_j^h(u,m)e_i-F_i^h(u,m)e_j).
\tag{2.4}
$$

其来源乘子次数至多三，所以 (2.4) 完整落在原 6188 来源字典中；它没有负的 $u$ 次数，且

$$
A^h(u)\phi_{ij,\alpha}(u)=0,\qquad
\phi_{ij,\alpha}(0)=m^\alpha(F_j^\infty e_i-F_i^\infty e_j).
\tag{2.5}
$$

使用构成 $v\in S$ 的同一有理常数组合，得到 $\phi_v(u)$，满足

$$
A^h(u)\phi_v(u)=0,\qquad \phi_v(0)=\iota_Jv.
\tag{2.6}
$$

这里 $\iota_J$ 把所选来源嵌入全部原来源。**只在常项要求支撑于 $J$。** 曲线的高次项可以使用 $J$ 外来源；下面证明会完整保留这一点。精确的 29 维自由坐标归一仅作常数有理换基，因而不改变 (2.6)。所以不能把本条假设弱化成“有 29 个常块核”或“有有限模精度核”。

## 3. 一般的完整曲线与方阵阶数引理

设 $A^h(u)$ 是任意完整原矩阵，$C(u)$ 是其 $n'$ 阶方阵子矩阵。设

$$
r=\operatorname{rank}_{\mathbb Q}C(0),\qquad
R\ge\operatorname{rank}_{\mathbb Q}A^h(0).
$$

若存在一个 $s'$ 维子空间 $S'\subset\ker C(0)$，每个 $v\in S'$ 都是某条完整原核曲线的常项，且该常项支撑在 $C$ 的来源列中，则

$$
\boxed{v_u\det C(u)\ge n'+s'-R.}
\tag{3.1}
$$

零行列式按无穷阶解释。

证明如下。写 $A^h=A_0+uA_1+\cdots$、$\phi_v=v+uv_1+\cdots$。由完整身份得

$$
A_1v=-A_0v_1.
\tag{3.2}
$$

方阵的一阶连接是

$$
\beta_C:\ker C(0)\longrightarrow\operatorname{coker}C(0),
\qquad v\longmapsto[C_1v].
\tag{3.3}
$$

对 $v\in S'$，(3.2) 在所选输出上说明其像属于

$$
\operatorname{im}(A_0|_{\text{所选输出}})
\big/\operatorname{im}C(0).
$$

这个空间维数至多 $R-r$。因此

$$
\dim\ker\beta_C\ge s'-(R-r).
\tag{3.4}
$$

另一方面，以常数可逆行列变换把 $C(0)$ 化为秩 $r$ 的单位块。消去该单位块后，完整局部 Schur 块为 $uT(u)$，其大小是 $n'-r$，且 $T(0)$ 表示 (3.3)。故

$$
v_u\det C
=(n'-r)+v_u\det T
\ge(n'-r)+\dim\ker\beta_C.
\tag{3.5}
$$

合并 (3.4) 即得 (3.1)。这里未要求曲线的高次项留在方阵来源中，也未把整个 $A_0$ 的像免费商掉；它恰贡献了 $R-r$ 这一可能损失。

## 4. 同一子式、换列子式及 cofactor 的三个实际阶

对 $B^h$，取 $n'=4354$、$s'=29$、$R=4340$，得

$$
\boxed{v_\infty(D_h)\ge43,\qquad \deg D\le H-43.}
\tag{4.1}
$$

现在将 $B$ 的某个来源列换为任意原来源。对 $S$ 加上“被换出来源的常项坐标为零”这一标量条件，仍有至少 28 维。将新列的常项系数置零，就把这个子空间嵌入新方阵的常块核；原曲线仍是完整原矩阵的真曲线。于是每个非零换列子式满足

$$
\boxed{v_\infty(D_{\rm replace,h})\ge4354+28-4340=42.}
\tag{4.2}
$$

若交换造成重复来源列，则该行列式恒零，次数估计自动成立。

对任意 cofactor，同时删去一个来源列和一个输出行。同一单坐标条件保留至少 28 维，删输出行不会破坏原身份。方阵大小为 4353，故

$$
\boxed{v_\infty(D_{\rm cofactor,h})\ge4353+28-4340=41.}
\tag{4.3}
$$

(4.1)–(4.3) 是三个不同下界。这里没有将 cofactor 误记为 42 阶，也没有将换列子式误记为 43 阶。

## 5. 消去已付公共因子后的精确降度

沿用[公共子式因子的条件降度](R150-appendix-common-minor-factor-conditional-source-cost8740.md)。已付的有限公共因子 $K(s)$ 次数为 60，整除每个原最大子式；不宣称它就是完整 gcd。令

$$
d_*=D/K,\qquad q=\deg d_*.
$$

同一 $D$ 的非零模 31 约化被 315 次的完整模 31 最大子式 gcd 整除，所以 $\deg D\ge315$，即 $q\ge255$；没有把这些模 31 因子提升到特征零。由 (4.1)，

$$
\boxed{255\le q\le H-43-60=8667.}
\tag{5.1}
$$

对任一原来源列 $A_\ell$，记

$$
P_\ell=\operatorname{adj}(B)(A_\ell)_I/K.
$$

换列子式的公共因子给 $P_\ell\in\mathbb Q[s]^{4354}$；完整泛秩与 $I$ 上的单射性给全部 4367 输出的身份

$$
A_JP_\ell=d_*A_\ell.
\tag{5.2}
$$

由 (4.2)，逐个基来源坐标 $j$ 有

$$
\deg(P_\ell)_j\le H-a_j+a_\ell-42-60.
\tag{5.3}
$$

现在假设原目标 $b_\nu=h_0t_\nu$ 已属于 $\operatorname{im}_{\mathbb Q[s]}A$，其中 $2\le\nu\le10$，$\deg h_0=24$。其真实目标权满足

$$
\deg(b_\nu)_i+b_i\le\tau_\nu=44+2\nu\le64.
\tag{5.4}
$$

把任一已有解的非基系数除以 $d_*$，利用 (5.2) 将商移入基来源，得到同一目标的解 $y$，且 $\deg y_\ell<q$ 对 $\ell\notin J$ 成立。在这个已有成员性的前提下，

$$
T_\nu=\operatorname{adj}(B)(b_\nu)_I/K
\in\mathbb Q[s]^{4354},
$$

$$
d_*y_j=(T_\nu)_j-\sum_{\ell\notin J}(P_\ell)_j y_\ell.
\tag{5.5}
$$

cofactor 的 (4.3) 给

$$
\deg(T_\nu)_j\le H-a_j+\tau_\nu-41-60.
\tag{5.6}
$$

因此非基来源成本至多

$$
q-1+45\le8667+44=8711.
\tag{5.7}
$$

基来源的目标项成本至多

$$
H+\tau_\nu-41-70-q
\le8770+64-41-70-255=8468;
\tag{5.8}
$$

换列转移项成本至多

$$
H+\max a_\ell-42-71
=8770+55-42-71=8712.
\tag{5.9}
$$

合并得到

$$
\boxed{
h_0t_\nu\in\operatorname{im}_{\mathbb Q[s]}A
\ \Longrightarrow\
\exists y^{(\nu)}:\ Ay^{(\nu)}=h_0t_\nu,\quad
\operatorname{cost}(y^{(\nu)})\le8712.
}
\tag{5.10}
$$

这是原来源的共同条件界，不改变乘子次数至多三，不丢另外 13 个输出，不预先假定目标成员性。它严格改进仅由 29 个常块核得到的条件界 8726。

## 6. 一般可提升常项维数及尚未闭合处

证明实际给出一个可继续使用的参数。若同一所选常块内已付 $s$ 维真来源空间，每一条都有 (2.6) 那样的同一自然矩阵无极点曲线，则

$$
v_\infty(D_h)\ge s+14,\quad
v_\infty(D_{\rm replace,h})\ge s+13,\quad
v_\infty(D_{\rm cofactor,h})\ge s+12,
\tag{6.1}
$$

同一降度推得条件成本至多 $8741-s$。当前真正支付的是 $s=29$。即使以后先证明有 36 条常块核，也不能直接取 $s=36$：还要证明额外七条属于完整原核曲线的常项像。泛参数核维数、有限模精度或单个无穷远常核本身均不足。

本条不证明 $v_\infty(D_h)$ 的准确值，不证明 $D$ 的最高系数为 31 单位，也不把现有模 $31^6$ 的全九目标来源换成特征零来源。若另付最高系数单位，则含零因子的有限环降度可沿已有证明使用相同 8712 界；固定目标乘子的全精度条件仍须独立支付。下一步仍是实际原矩阵的成员性或完整无穷远 Smith/原来源曲线接口。
