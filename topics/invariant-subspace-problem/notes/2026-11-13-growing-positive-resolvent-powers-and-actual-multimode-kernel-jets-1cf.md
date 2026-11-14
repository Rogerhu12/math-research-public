# 工作引理：变化的正预解幂在真实多模式核内支付线性增长的全部词深度

日期：2026-11-13（UTC）。normal_resume_1cf / Astra-ISP-1cf8c51d。
状态：已核技术引理；root 与 kernel 全文独立核查。本稿本身不宣称零参数核已经排除。
这里保留原完全居中的两行及任意复指数权，并逐项支付原矩阵池证明所需的正则化、反射词和局部配对。
不使用未知核上的通常伴随或 $C$ 不变性。

## 1. 正 first 与实际倾斜 first 必须区分

固定非负 $a,b\in\ell^2$，记
$$
X_+=X_{\sum_j a_j\chi_j},\qquad
Y_+=X_{\sum_j b_j\chi_j}.
$$
它们是 R128 的原最大增生 first。
在完全居中的例子中，原模式为
$$
u=-\kappa_a+\sum_j a_j\chi_j,\qquad
z=-\kappa_b+\sum_j b_j\chi_j.
$$
给定固定复 $\ell^2$ 指数权 $w=w_*+\sum_j w_j\chi_j$，设
$$
t_j=e^{-2w_j},\qquad R_j(w)=V(t_jN_j).
$$
R186 §10 的真实有限位恒等式和 $\ell^2\times\ell^2$ 绝对收敛给
$$
Z_1=X_{u,w}=X_+-\kappa_a I+H_{a,w},\qquad
Z_2=X_{z,w}=Y_+-\kappa_b I+H_{b,w},
\tag{1.1}
$$
$$
H_{a,w}=\sum_j a_j(R_j(w)-V_j),\qquad
H_{b,w}=\sum_j b_j(R_j(w)-V_j)\in\mathcal A.
$$
这些固定有界扰动与全部原 first 完整域交换。
不把 $Z_1,Z_2$ 直接称为最大增生算子。

令 $\mathcal D_s$ 为 $X_+,Y_+$ 的全部长度至多 $s$ 的自然词共同域，包含所有词序及其低阶子词。
R186 §§3.1—3.3 给其完备共同图、词序一致及全部 $A'$ 保域。
同一节的双向有限展开给
$$
\mathcal D_s(X_+,Y_+)=\mathcal D_s(Z_1,Z_2).
\tag{1.2}
$$
还允许加入有限个真正有界的 $A'$ 模式；它们不消耗无界词深度。

## 2. 变化正则器、准确混合字界与强单位

固定一个次数上界 $D\ge1$，取整数
$$
q_r=(8D+8)r,\qquad \epsilon_r=r^{-2}\quad(r\ge1),
$$
$$
Q_x(\epsilon)=(I+\epsilon X_+)^{-1},\qquad
Q_y(\epsilon)=(I+\epsilon Y_+)^{-1},
$$
$$
\boxed{\mathcal R_r=Q_x(\epsilon_r)^{q_r}
Q_y(\epsilon_r)^{q_r}.}
\tag{2.1}
$$
所有因子都是 $A'$ 中的收缩，单射且稠密像；因 $A'$ 交换而真正互相交换。
对每个自然字 $W$，长度 $s\le q_r$，逐次保留足够多的预解因子，并用
$$
X_+Q_x(\epsilon)=\epsilon^{-1}(I-Q_x(\epsilon)),\qquad
Y_+Q_y(\epsilon)=\epsilon^{-1}(I-Q_y(\epsilon)),
$$
准确得到
$$
\boxed{
\mathcal R_rH\subset\mathcal D_{q_r},\qquad
\|W(X_+,Y_+)\mathcal R_r\|\le(2/\epsilon_r)^s.
}
\tag{2.2}
$$
这里每一步的下一输入属于对应闭 first 的实际域。
这也是 R186 (3.5) 对共同因子 $Q_xQ_y$ 的直接应用，不是无界形式约分。
在 (1.1) 中双向展开固定有界交换扰动，遂有
$$
\boxed{
\|W(Z_1,Z_2)\mathcal R_r\|
\le(C_w+2/\epsilon_r)^s\le(C_w+2r^2)^s
\quad(s\le q_r).
}
\tag{2.3}
$$

为核强趋 $I$，先取
$f\in\operatorname{Dom}X_+\cap\operatorname{Dom}Y_+$。
预解恒等式和收缩性给
$$
\|(Q_x(\epsilon)^q-I)f\|\le q\epsilon\|X_+f\|,
\qquad
\|(Q_y(\epsilon)^q-I)f\|\le q\epsilon\|Y_+f\|.
$$
因此
$$
\|(\mathcal R_r-I)f\|
\le q_r\epsilon_r(\|X_+f\|+\|Y_+f\|)
\longrightarrow0.
$$
该共同域稠密，而 $\|\mathcal R_r\|\le1$，故
$$
\boxed{\mathcal R_r\longrightarrow I\quad\text{SOT on }H.}
\tag{2.4}
$$
关键是 $q_r\epsilon_r=(8D+8)/r\to0$，不是把固定参数的越来越高预解幂当作强单位。

## 3. 原规范核的保持，不先假设核属于自然域

设 $\mathsf T$ 是实际完整 Bell 或其准确共振变换的 R186 规范最大实现。
它在共同自然域上由总无界次数至多 $D$ 的多项式
$$
P(Z_1,Z_2;\mathbf B)
$$
给出，$\mathbf B$ 为有限个有界 $A'$ 系数或模式。
令 $M=\ker\mathsf T$。

R186 (4.4) 用固定共同分母写
$$
\operatorname{Graph}\mathsf T=\{(f,g):F_Pf=R_0^Dg\},
\quad F_P,R_0\in A',\quad R_0\text{ 单射}.
$$
所以 $M=\ker F_P$。
$\mathcal R_r\in A'$ 与 $F_P$ 交换，严格得到
$$
\boxed{
\mathcal R_rM\subset M\cap\mathcal D_{q_r},
\qquad \mathcal R_rf\to f\quad(f\in M).
}
\tag{3.1}
$$
同一有界图等式还给 $\mathsf T\mathcal R_rf=\mathcal R_r\mathsf Tf$ 于整个最大域。
所有 $A'$ 系数保每个 $\mathcal D_s$，并与其全部自然词交换。

若 $f\in M$，则对 $\mathcal R_rf$ 所需的有限多项式和中间词可以逐项使用；
在长度预算内，自然 $P$ 恰为 $\mathsf T$，且
$$
P(Z;\mathbf B)\mathcal R_rf=0.
\tag{3.2}
$$
$Z_i$ 作用于 $M$ 中合法的自然域向量后仍在 $M$，这是 R186 (5.4) 的有界核方程证明。
不推出 $M\subset\mathcal D_1$，更不推出 $Z_i|_M$ 有界。

下文所有输入先形成于 $M$ 内，再在最左侧作有限反射。
从未使用 $\mathcal R_r^*$ 保持 $M$。

## 4. 真实高位反射的联合导数误差

§§1—3 的正则器结论允许任意有界 $A'$ 系数；从本节起，直到局部四次配对，只对下面明确的实际 Bell 局部系数使用额外估计。任意 $A'$ 元素不自动具有这项性质。

本节只对实际 Bell 所出现的局部形式使用反射误差：
倾斜 first、有限条可和 first，以及固定次数的
$$
\sum_j d_j\,p(R_j(w)),
\qquad d\in\ell^2,\quad p\text{ 固定多项式或同一小圆上的实际有理函数}.
$$
相应级数若作为有界模式使用，另保留其既有绝对收敛条件。
不把任意 $A'$ 系数的反射变化都免费纳入。

令
$$
J_E=\prod_{j\in E}M_{\chi_j},\qquad m_E=\min E.
$$
对全部实际局部因子，把选中位的 $t_jN_j$ 改成 $-t_jN_j$ 得带帽表达。
R260 §§2—4 的真正最高物理位壳在这里可同时对 $X_+,Y_+$ 求导。
具体地，每个非零差壳 $B_{\ell,E}$ 局部支撑在前 $\ell+1$ 位，且必有 $\ell\ge m_E$，并满足
$$
\|B_{\ell,E}\|\le C\eta_{\ell-1}.
\tag{4.1}
$$
其与两个 closed tail first 完整交换，故
$$
\|\operatorname{ad}_{X_+}^{i}\operatorname{ad}_{Y_+}^{j}B_{\ell,E}\|
\le d_{x,\ell}^{\,i}d_{y,\ell}^{\,j}\|B_{\ell,E}\|,
$$
$$
d_{x,\ell}+d_{y,\ell}\le C_0+C_1\sqrt{\ell+1}.
\tag{4.2}
$$
所有导数保每个所需共同词域；由两个尾的域交换及有限归纳支付。

对这些算子定义联合解析导数范数
$$
\|B\|_\partial
=\sum_{i,j\ge0}
\frac{\|\operatorname{ad}_{X_+}^{i}\operatorname{ad}_{Y_+}^{j}B\|}{i!\,j!}.
$$
真实 Leibniz 与闭图极限的证明逐项等同 R260 §4，给幺 Banach 代数和乘积范数界。
两导数在该实际共同域上交换，来自 $X_+Y_+=Y_+X_+$ 在 $\mathcal D_2$ 上的等式。
由 (4.1)—(4.2)，全部反射差误差都满足
$$
\boxed{
\|E_{E}\|_\partial\le
C\sum_{\ell\ge m_E}\eta_{\ell-1}e^{C\sqrt{\ell+1}}
\le C'e^{-c16^{m_E-1}}=:\varepsilon_{m_E}.
}
\tag{4.3}
$$
同时
$$
\|\partial^{(i,j)}E_E\|\le i!j!\varepsilon_{m_E}.
\tag{4.4}
$$
这里无 $\max E$ 费用。

正规排序最终使用 $Z_i=X_i+H_i$（把常数也收入 $H_i$），而上面的导数按正 $X_+,Y_+$ 定义。
不能因 $\partial H_i=0$ 就声称 $H_i$ 与误差壳交换。
准确地，$H_i$ 与两正 first 完整域交换，所以
$\operatorname{ad}_{H_i}$ 与两导数交换；又
$$
\|\operatorname{ad}_{H_i}^{\,s}B\|_\partial
\le(2\|H_i\|)^s\|B\|_\partial.
$$
将 $\operatorname{ad}_{Z_i}=\operatorname{ad}_{X_i}+\operatorname{ad}_{H_i}$
作真正二项式展开并除以阶乘求和，得到
$$
\boxed{
\|B\|_{\partial Z}
\le e^{2\|H_1\|+2\|H_2\|}\|B\|_\partial.
}
\tag{4.5}
$$
特别全部倾斜联合导数仍由固定常数乘 $i!j!\varepsilon_{m_E}$ 控制；
原共同词域不变由 (1.2) 支付。
这正是 §5 按 $Z_1,Z_2$ 正规排序时使用的误差预算。

有限反射也双向保持每个 $\mathcal D_s$。
一个直接域证明是先在 $\max E+1$ 处分离有限有界头：
原两 first 是两个真正闭尾 first 的有界交换扰动，故共同词域不变；
$J_E$ 与两个尾完整交换。
高位无关的定量估计则使用 (4.3)，不能用这个最大位的粗头范数。

## 5. 为什么 reflected jets 只需线性词深度

假设
$$
|E|\le Kr,\quad m_E\ge\mu N,\quad r\asymp\sqrt N,
\tag{5.1}
$$
并且全部原 first 在选中位上的系数绝对和一致有界。
本例 $a_j,b_j=O(N^{-1})$ 于固定倍数 $N$ 的池，给更强的 $O(r/N)$；
可和高矩行由全局 $\ell^1$ 范数支付。
因此所有带帽 first 增量及带帽有界模式范数都有固定上界。

允许 $Q_E\in A'$ 是矩阵块形成的有限 $N_j$ 多项式。
把它的实际绝对系数和记为 $H_N$，特别 $\|Q_E\|\le H_N$；
$\partial Q_E=0$，且它保 $M$ 与全部共同词域。
取
$$
v_{E,r}=J_EQ_E\mathcal R_rf,\qquad f\in M.
$$
把一个长度 $s$ 的 first 词移过最左 $J_E$，
每个 first 变为“原 first＋有界交换增量＋(4.3) 的误差”。
再用
$$
Z_iB=BZ_i+[Z_i,B]
$$
把无界字移到右侧。
每个原 first 字至多被使用一次：它或者留在右侧，或者在移位时转为一次系数导数。
因此右侧 first 字数与系数总导数阶都不超过原长度 $s$。

可以采用如下粗而足够的有限计数。
至多 $(C(s+1))^s$ 个正规排序项；
每个导数阶乘乘积至多 $s!$；
固定数量的模式与带帽增量只另付 $C^s$。
用 (2.3)，对 $s\le4Dr$ 得
$$
\boxed{
\|W(Z_1,Z_2)v_{E,r}\|
\le H_N\exp[C_Dr\log(r+2)]\|f\|.
}
\tag{5.2}
$$
若展开中指定至少一个真实反射误差因子，则同一界额外乘
$\varepsilon_{\mu N}$。
固定 $D,K,\mu,w,a,b$ 后，$C_D$ 不依赖 $N,E,f$。

完整次数至多 $D$ 的 $P$ 的 $r$ 次实际作用，包含至多 $Dr$ 个 first 字。
正规排序不会增加这个数目。
旧矩阵块证明同时使用的
$$
(\gamma_E P)^r,\quad P^rJ_EQ_E\mathcal R_rf,\quad
P^{r-j}D_0P^jJ_EQ_E\mathcal R_rf
\quad(0\le j\le r)
$$
也各只有至多 $Dr$ 个 first 字；固定局部 $D_0$ 的正规排序导数仍只消耗已有字。
用 $4Dr$ 是有明确余量的统一预算，而 (2.1) 取 $q_r=(8D+8)r$ 更大。
不存在把 $r$ 次反射再误算为需要 $r^2$ 层原 first 域的步骤。

在真正的平方零顶部计算中，各高次差分都带重复 $N_j$；
转回原模型 $N_j^2=\eta_jN_{j+1}$ 后，
它们的系数多项式作用于上述输入也只使用 $O(Dr)$ 层。
故除原矩阵输入成本外，所有这类 carry 项最多另付
$$
\eta_{\mu N}\exp[C_Dr\log(r+2)]H_N\|f\|.
\tag{5.3}
$$
这条陈述并不取消原矩阵恒等式的检查；它只准确替换旧“核内 first 有界”所提供的深词预算。

## 6. 局部四次衰减与原 C 配对，完全不使用反射侧正则器

固定前 $h$ 位的局部矩阵 $D_0$。
对于实际 Bell / 共振多项式，逐个有限低位置 $R_j(w)=I$：
所有低头差由
$$
R_j(w)-I=-2t_jN_j(I+t_jN_j)^{-1}
=A\,D_j,\qquad D_j\in\mathcal A
$$
准确提出一个 $A$。
有限多项式相减给共同深域上的
$$
P=P_{\mathrm{tail},h}+A\,U_h(Z_1,Z_2),
\qquad\deg U_h\le D.
\tag{6.1}
$$
其有界系数在 $A'$ 中，$P_{\mathrm{tail},h}$ 与 $D_0$ 完整尾域交换；
所有显示的实际多项式彼此交换。
故在已付词域上
$$
\operatorname{ad}_{P}^{r}D_0
=\operatorname{ad}_{AU_h}^{r}D_0.
$$
第 $j$ 项形如
$$
A^j U_h^jD_0 A^{r-j}U_h^{r-j}.
$$
展开 $U_h$，再把 first 字移过固定 $D_0$。
其联合导数由固定真实头给几何界。
两边的 $A$ 幂仍准确保留；因此 R109 的实际四次幂界与
$j^4+(r-j)^4\ge r^4/8$ 给
$$
\boxed{
\|(\operatorname{ad}_{P}^{r}D_0)v_{E,r}\|
\le H_N
\exp[-5r^4/6+105r^3+C_{D,D_0}r\log(r+2)]\|f\|.
}
\tag{6.2}
$$
有限矩阵池平均若绝对输入总预算为 $A_N$，将 $H_N$ 换成 $A_N$ 即可。
新增 $O(r\log r)$ 完全低于原四次主项。

R186 给原全 $H$ 上的完整 $C$ 自伴 $\mathsf T$。
对任意 $g\in M$，用已付的全部中间自然词，
$$
B(D_0P^rv_{E,r},g)
=(-1)^rB((\operatorname{ad}_P^rD_0)v_{E,r},g).
\tag{6.3}
$$
逐项解释为展开 $\operatorname{ad}_P^r$ 后，把左侧每个正次 $\mathsf T$ 用完整 $C$ 对称移至 $g$，由 $\mathsf Tg=0$ 消去。
不要求 $Cg\in M$，不把任何 $R_r^*$ 施于未知核，也不把 $D_0$ 当作保核。
$\mathcal R_r$ 只在右输入 $f$ 上，并由 (3.1) 付其核保持。

## 7. 给后续矩阵池的准确接口

若真实有限矩阵池构造已经给出：
其常数单位方向在全空间成立，输入 $Q_E$ 是有界交换子；
顶部提升为一个一致有界的纯池平均 $\mathcal C_N$；
全部非顶部项由上述反射和 carry 控制；
且
$$
\mathcal C_N\rightharpoonup cI,\quad c\ne0,\qquad
\log A_N=o(r^4)
$$
（或原可用小固定 $\theta$ 支付的 $O(r^4)$），
则用输入 $\mathcal V_N\mathcal R_rf$ 时，
$$
P^r\mathcal V_N\mathcal R_rf-\mathcal C_N\mathcal R_rf\to0.
$$
(2.4) 与 $\sup\|\mathcal C_N\|<\infty$ 给
$\mathcal C_N\mathcal R_rf\rightharpoonup cf$。
(6.2)—(6.3) 因而仍能执行原局部全矩阵配对。
这里并未用假定未知核 first 有界来取得该非零极限。

接入具体零参数前，仍须单独付清原 ordinary-to-resonant 有限逆、所选单位偏导及所有跨池矩阵下界。
本引理支付的是这五个原先容易混淆的域与增长点。

依赖：R128 正 first 与真实预解；R186 §§2—5、10 的共同域、最大核、有界倾斜与全 $C$ 自伴；
R260 §§2—4 的最高物理位壳及真实导数代数；R236 多辅助矩阵 §§5—9 的有限顶部计数；R109 的实际 $A$ 幂界。


## 可核原始依据

- [R128](../results/R128-first-chaos-invariant-parts-and-resolvent-regularization.md)：正 first 的实际收缩预解。
- [R186](../results/R186-multimode-common-domains-maximal-polynomial-graphs-gauge-cyclicity.md)：共同自然词、规范最大图与完整 C 自伴。
- [R260](../results/R260-arbitrary-span-derivation-budgets-and-sorted-bell-kernels.md)：真实最高物理位壳和导子代数。
- [R236 矩阵池](../results/R236-appendix-multiple-summable-auxiliary-matrix-blocks-and-exact-pool-averages.md)：实际顶部计数、反射符号及局部配对。
- [R109](../results/R109-invariant-restriction-exact-quartic-type.md)：原 A 的四次幂费用。
