# R849 — 原完整潜在 CM 池、二处三阶固定性与属七的实际核

日期：2026-11-16。**状态：下述原层级的完整 CM 来源分类、群作用及属七必要结构已证明。**

本篇继续 R847 的同一个原有限 Hom 表达。
核心不是假设整个像曲线的 Jacobian 为 CM，而是先确定
\(J_0(10404)\) 中**全部几何 \(E_0\)-isotypic 部分**。
在该部分的 \(R=\omega^2\) 全纯块上，
原二处 \(S_3\) 表示准确为
\(\epsilon\oplus\mathbf1^{\oplus6}\)，没有标准二维表示。
这给实际 Jacobian 核的约束，排除属七的四种候选，
并精确限定另外两种候选的非 $E_0$ 幂核。

它不证明剩余候选存在，不证明原端点非零，也不辨认 R814 的指定 canonical 类。

## 1. 原来源、群及两个不同的商

保持
$$
K=\mathbf Q(\omega),\quad E_0:y^2=x^3+1,\quad
N=10404,\quad M=2601,
$$
$$
X=X_0(N),\quad C=X_0(M),\qquad
\Phi=(F,aq_0,aq_2):X\to E_0^3.
\tag{1}
$$
\(F,a\) 是 R841 完整有理 Hecke packet 中的实际 Hom，
原所有系数、Artin 数据、\(q_0(z)=z\)、\(q_2(z)=4z\) 均不变。
设像生成整个 \(A=E_0^3\)，正规化为 \(D\)。

沿 R847，原 \(R:z\mapsto z+1/3\) 在 \(D\) 上给 \(v\)，
原 \(S,w_4\) 给忠实
$$
G=\langle S_D,(w_4)_D\rangle\simeq S_3,
\qquad c=S_D(w_4)_D,\quad c^3=1.
\tag{2}
$$
\(v\) 与 \(G\) 交换，合成忠实的 \(C_3\times S_3\)。
目标的全纯表示是
$$
H^0(A,\Omega^1)
  =(\epsilon\oplus\rho)_{v=\omega},
\tag{3}
$$
其中 \(\epsilon\) 为 sign，\(\rho\) 为标准二维表示。

下文分别写
$$
B=D/\langle v\rangle,\qquad D_c=D/\langle c\rangle,\qquad
D_G=D/G.
\tag{4}
$$
尤其 \(D_G\) 与 \(B/G=D/(G\times\langle v\rangle)\)
是不同的曲线；二者之间仍有原三阶 \(v\) 商。
所有后文的亏格或微分不变量都按(4)分别计算。

## 2. 为什么没有遗漏潜在 CM、非 CM 或诱导因子

记 \(J^{(0)}\) 为 \(J(X)_{\overline{\mathbf Q}}\)
的整个几何 \(E_0\)-isotypic 部分。
因为 \(E_0\) 定义于 \(\mathbf Q\)，这个同源部分的中心幂等元
由 \(G_{\mathbf Q}\) 保持，故 \(J^{(0)}\) 在有理同源范畴中下降到
\(\mathbf Q\)。不能只找几个已知 CM 新形式便宣称穷尽它。

对 \(J(X)\) 的任一有理 newform 因子 \(A_f\)，
若它与 \(E_0\) 在某有限扩域上有非零 Hom，
Ribet 的 *Twists of Modular Forms and Endomorphisms of Abelian Varieties*，
Theorem (4.7)（印刷第55页），给完整判据：
两者或者有同一个 CM 二次域，或者相应新形式在系数嵌入后互为
Dirichlet twist。后一种对 \(E_0\) 也仍有同一 \(K\)-CM self-twist。
因此该 \(f\) 必为 \(K\)-CM；其它 CM 域、非 CM 或潜在四元数因子
都不能给一个遗漏的 \(E_0\) 因子。

也可直接看到本应用的机制。
在 \(E_0^d\) 上的中心 \(K\) 作用不受同源坐标变换影响；
其 Galois 作用恰为 \(K/\mathbf Q\) 的作用。
所以中心 \([\omega]\) 在 \(G_K\) 上固定，复共轭将它换成
\([\omega^2]\)。它与整个有理 Hecke 因子作用交换。
平凡 nebentypus 的系数域为全实域；在每个二维 newform 实现中，
中心 \(K\) 的两个特征因复共轭交换而各为一维。
故该实现限制到 \(G_K\) 分裂为两个角色，
原二维表示是从 \(K\) 诱导的。
权二与代数 Hecke 角色的对应遂给同一 \(K\)-CM theta form。
这里讨论的是整个 newform 实现，不以一个选定 \(q\)-系数
或某个局部标量替代潜在 Hom 的分类。

反过来，每个 \(K\)-CM newform 的阿贝尔簇在一个固定有限扩域上
同源于 \(E_0\) 的幂。因此上述分类双向成立。
随后必须把它的全部 old copies 加回；第4节将逐一保留。

## 3. 所有可能的原 CM 新形式恰有十八条

令 \(\psi_0\) 为原 \(E_0\) 的 type-\((1,0)\) Hecke 角色，
导子为 \(2\delta\)，\(\delta=1+2\omega\)。
取 R806/R844 的同一个 \(\eta=\eta_{10}\)，
它是 conductor \(34\) 的十八阶反循环角色，
并准确生成 \(H_{34}/K\) 的全部角色群。

设一个平凡 nebentypus 的 \(K\)-CM weight-two newform 的 level
整除 \(N\)，其 primitive 角色为 \(\psi\)。
由精确导子公式
$$
N_\psi=|D_K|\,\mathrm N_{K/\mathbf Q}(\mathfrak f_\psi)
\mid 10404,
\tag{5}
$$
有 \(\mathfrak f_\psi\mid2\delta17\)。
平凡 nebentypus 要求有限角色在有理数上的限制等于
\(\chi_K\)；故三处的单位角色是唯一非平凡的
\((\mathcal O_K/\delta)^\times\) 角色。
于是三处导子恰为 \(\delta\)，并与 \(\psi_0\) 的单位角色相同。

所以 \(\chi=\psi/\psi_0\) 是有限角色，导子整除 \(34\)，
在有理 idèle 上平凡。它准确因子化过 order \(34\) 的
ring-class 群，而非任意较大的 ray-class 群。
R844 已从完整局部单位和类数证明该群为 \(C_{18}\)，
\(\eta\) 为 faithful 角色。因此全部可能恰为
$$
\boxed{\psi_k=\eta^k\psi_0,\qquad k\in\mathbf Z/18.}
\tag{6}
$$

各 primitive level 也完全确定：

| \(k\) | 数目（含全部系数嵌入） | \(\mathfrak f_{\psi_k}\) | \(N_{\psi_k}\) |
|---|---:|---|---:|
| \(0\) | \(1\) | \(2\delta\) | \(36\) |
| \(1,4,7,10,13,16\) | \(6\) | \(17\delta\) | \(2601\) |
| 其余非零 \(k\) | \(11\) | \(34\delta\) | \(10404\) |

确实 \(\eta\) 在17处的单位角色准确为十八阶，
所以除 \(k=0\) 外均有精确17导子。
在2处它的单位角色为三阶；
R826 的实际 \(\eta^{-2}\psi_0\) 在2处完全抵消，
故抵消条件准确为 \(k\equiv1\bmod3\)。
其它两种余类均保原2导子。
三处 \(\eta\) 不分歧，并未改变前述精确 \(\delta\) 导子。
这同时保留各角色在三处 uniformizer 上的真实值；
本篇只按导子分类，没有把“不分歧”改写成“角色恒1”。

不同 \(k\) 的 type-\((1,0)\) 角色给不同 normalized theta forms；
它们可以属于同一个有理 Galois packet，但全部嵌入均已计入。
不存在再靠换一个 finite coefficient field 增加的新形式。

## 4. 全部 old copies 与原 \(R=\omega^2\) 块

对 \(f_k=\theta(\psi_k)\)，使用真实几何 old 微分
$$
f_{k,d}(Q)\frac{dQ}{Q}
:=d\,f_k(Q^d)\frac{dQ}{Q},
\qquad d\mid N/N_{\psi_k}.
\tag{7}
$$
new/old 分解的完整 divisors 为
$$
\begin{array}{c|c}
N_{\psi_k}&d\\ \hline
36&1,17,289\\
2601&1,2,4\\
10404&1.
\end{array}
\tag{8}
$$
特别所有允许的 \(d\) 都素于3；没有遗漏一个来自较低三处
conductor 的 \(d=3\) 副本。

每个 \(f_k\) 的完整 CM 理想展开均仅在
\(n\equiv1\bmod3\) 上有支撑。
因此对原 \(R_N:Q\mapsto\omega Q\)，
$$
R_N^*\bigl(f_{k,d}(Q)dQ/Q\bigr)
 =\omega^d f_{k,d}(Q)dQ/Q.
\tag{9}
$$
故整个 \(J^{(0)}\) 的 \(R=\omega^2\) 全纯块准确只有
$$
\boxed{
f_{0,17}\quad\text{和}\quad
f_{k,2}\ (k=1,4,7,10,13,16).
}
\tag{10}
$$
这是七维完整空间；同时
$$
H^0(J^{(0)},\Omega^1)^{R=1}=0.
\tag{11}
$$

现在支付 (10) 上整个二处群，而非只付 \(c\) 的阶。

- 对 \(f_{0,17}\)，原 \(E_0\) 在2处有 conductor exponent2，
  \(U_2=0\)，所以其完整 Fourier 展开只有奇指数。
  \(17\) 仍为奇数，故 \(S^*=-1\)。
  它在2处是 R831 §4 的同一唯一 cuspidal sign type；
  该证明给 partial \(w_4=-1\)。
  在其它有限位，原 \(\mathcal W\) 位于 level \(N\) 的相应
  \(K_0\) 中，固定所有17-old 向量，不添额外相位。
  因而这一线为 \(\epsilon\)。

- 对六条 \(f_{k,2}=2f_k(Q^2)\)，\(S^*=+1\)；
  R831 的完整曲线身份 \(q_1w_4=q_1\) 给 \(w_4^*=+1\)。
  这是实际中间 old 副本，不依赖对该新形式的其它坏位作符号猜测。
  六条线均为 \(\mathbf1\)。

所以有完整表示等式
$$
\boxed{
H^0(J^{(0)},\Omega^1)^{R=\omega^2}
 \simeq\epsilon\oplus\mathbf1^{\oplus6},
\qquad c^*=1\text{ 于此整个块}.
}
\tag{12}
$$
尤其 sign 只出现一次，standard \(\rho\) 完全不出现。

## 5. 真正可应用于原核的“单一 CM type”引理

设 \(T\) 是 \(J(X)\) 的一个实际几何阿贝尔子商，
由原 \(R,c\) 保持，且 \(R\) 在 \(H^0(T,\Omega^1)\) 上
全部为 \(\omega^2\)。
则 \(T\) 几何同源于 \(E_0^{\dim T}\)。

一个直接证明是把 \(T(\mathbf C)\) 写成
\(\mathbf C^d/\Lambda\)。
其 \(K\) 作用在整个切空间上为同一复嵌入，
\(\Lambda_{\mathbf Q}\) 是 \(d\) 维 \(K\)-向量空间。
取 \(K\)-基后，该格与 \(\mathcal O_K^d\) 的复像可公度；
于是给到 \(E_0^d\) 的同源。
这里是被实际单一 Hodge 特征强迫的结论，
不是对任意带 \(K\)-作用的阿贝尔簇作 CM 断言。

故 \(T\) 落在第2–4节的完整 \(J^{(0)}\) 中；
由(12)及特征零下同态的微分忠实性，
$$
\boxed{c|_T=1.}
\tag{13}
$$
如果 \(T\) 还由 \(G\) 保持，其全纯 \(G\) 模必须是
\(\mathbf1,\epsilon\) 的和，且来自原源的 \(\epsilon\)
总 multiplicity 至多为1。
同理，一个 \(R=1\) 的几何 \(E_0\) 子商由(11)直接排除。

本引理允许任意固定有限定义域，也允许先通过原有限
\(X\to D\) 的 Jacobian 推拉进入 \(J(X)\)。
其次数只给同源，不影响这些特征；
没有把 \(K\)-上的原 Hom 完备性误当成全部几何 Hom 完备性。

## 6. 属七的全部候选与实际 equivariant 核

现假定原生成项的 \(g(D)=7\)。
仍写
$$
V_i=H^0(D,\Omega^1)^{v=\omega^i},\qquad
g_0=\dim V_0=g(B).
$$
由 R847 的完整循环覆盖式和 \(\dim V_1\ge3\)，
全部候选为

| \(g_0\) | \((r_1,r_2)\) | \((\dim V_1,\dim V_2)\) |
|---:|---:|---:|
| \(0\) | \((3,6)\) | \((3,4)\) |
| \(0\) | \((6,3)\) | \((4,3)\) |
| \(0\) | \((9,0)\) | \((5,2)\) |
| \(1\) | \((3,3)\) | \((3,3)\) |
| \(1\) | \((6,0)\) | \((4,2)\) |
| \(2\) | \((3,0)\) | \((3,2)\) |

若 \(g_0=3\)，三阶覆盖不分歧且非平凡，
两个非平凡特征各为 \(g_0-1=2\)，不满足 \(\dim V_1\ge3\)。

原 \(q:J(D)\to A\) 是 \(G\times\langle v\rangle\)-等变满同态。
其连通核 \(K_D\) 由该有限群保持。
利用平均极化作等变 Poincaré 分解，
可在有理同源范畴中保整个核及其 \(G\)-isotypic 子因子。
其非平凡 \(v\) 部分的全纯模是
$$
\bigl(V_1-(\epsilon\oplus\rho)\bigr)\oplus V_2.
\tag{14}
$$
这是真实阿贝尔核的表示，不是虚拟减维后任意造一个新来源。

对 \(c\) 的阶3作用，Riemann–Hurwitz 始终给
$$
g(D_c)=\dim H^0(D,\Omega^1)^c\le3.
\tag{15}
$$

### 6.1. \(\dim V_1=3,\ g_0\le1\) 的两种候选不可能

此时(14)的整个非平凡 \(v\) 核只在 \(V_2\)，
故第5节迫 \(c\) 在它上面恒等。
而原目标 \(\epsilon\oplus\rho\) 的 \(c\)-不变量有一维。
因此
$$
g(D_c)\ge1+\dim V_2\ge4,
$$
与(15)矛盾。
这排除 \((g_0,r_1,r_2)=(0,3,6),(1,3,3)\)。

### 6.2. \(\dim V_1=4\) 的两种候选不可能

此时 \(V_1-(\epsilon\oplus\rho)\) 仅一维，
必为 \(\mathbf1\) 或 \(\epsilon\)，所以 \(c\) 在它上面恒等。
若 \(V_2\) 包含一个 \(\rho\)，
对 \(K_D\) 的非平凡 \(v\) 部分施有理 central projector
\(e_\rho\in\mathbf Q[G]\)，便得到一个非零阿贝尔因子，
其全纯 \(v\)-特征全部为 \(\omega^2\)，
而 \(c\) 按 \(\rho\) 非平凡作用。
这违反(13)。
故 \(V_2\) 没有 \(\rho\)，全部由一维角色组成，\(c\) 恒等。
于是
$$
g(D_c)\ge2+\dim V_2\ge4,
$$
再次违反(15)。
这排除 \((0,6,3),(1,6,0)\)。

所以原属七项只可能有下面两种实际结构：
$$
\boxed{
\mathrm{I}:\ (g_0,d_\omega,d_{\omega^2};r_1,r_2)
 =(0,5,2;9,0),
}
\tag{16}
$$
$$
\boxed{
\mathrm{II}:\ (g_0,d_\omega,d_{\omega^2};r_1,r_2)
 =(2,3,2;3,0).
}
\tag{17}
$$
后两节进一步给它们实际 Jacobian 核的结构，
而不把这两个必要条件当成存在证明。

## 7. 第一种：明确九分支模型与 balanced abelian-surface 核

在(16)中，\(B\simeq\mathbf P^1\) 上的忠实 \(S_3\)
可用 R847 的规范
\(c(x)=\omega x,\ s(x)=1/x\)。
九个分支点全为同一个 \(v\)-monodromy。
原 \(S\)-固定的 cusp 像是一个分支点，
所以分支集包含一个大小3的特殊轨道。
由完整轨道大小 \(2,3,3,6\)，九点集恰为一个特殊三点轨道
及一个泛型六点轨道。

在固定有限扩域上选择坐标，但保一个可能的 cubic twist \(d\)，
得到实际模型
$$
\boxed{
D:\quad
y^3=d(x^3-1)(x^6-a x^3+1),
\qquad d\ne0,\quad a^2\ne4.
}
\tag{18}
$$
原 lift 准确可写为
$$
v(x,y)=(x,\omega y),\qquad
c(x,y)=(\omega x,y),\qquad
s(x,y)=(1/x,-y/x^3).
\tag{19}
$$
特别 \(c\) 的 \(y\)-相位不是自由选择：
写成 \(\omega^k y\) 后，
\(scs=c^{-1}\) 强制 \(2k\equiv0\bmod3\)，故 \(k=0\)。

完整全纯基为
$$
V_1:\ \frac{x^jdx}{y^2}\ (0\le j\le4),\qquad
V_2:\ \frac{x^jdx}{y}\ (0\le j\le1).
$$
(19)逐项给
$$
\boxed{V_1=\epsilon\oplus\rho^{\oplus2},\qquad V_2=\rho.}
\tag{20}
$$
因此
$$
g(D_G)=0,\qquad g(D_c)=1.
\tag{21}
$$
后一个实际商有方程
$$
D_c:\quad y^3=d(U-1)(U^2-aU+1),\qquad U=x^3,
$$
是 \(j=0\) 椭圆曲线；原第一坐标 \(F\) 从这个商因子化。
这里的椭圆商不是原后两个点的一个未指定二同源核。

有理群代数的 standard 块为 \(M_2(\mathbf Q)\)；
结合原满同态 \(q\)，其实际同源分解给
$$
\boxed{
J(D)\sim E_0^3\times T^2,\qquad \dim T=2,
}
\tag{22}
$$
其中 \(T\) 的原 \(K\)-作用有 Hodge signature \((1,1)\)。
理由是 standard multiplicity 因子的维数为3，
其 \(v\)-signature 为 \((2,1)\)；
去掉原 standard 目标中的一个 \(E_0\) 后，
剩下实际二维因子 \(T\)。
这里不把 \(T\) 的 balanced signature 当作单一 CM type。

而且
$$
T\not\sim E_0^2.
\tag{23}
$$
否则 \(T^2\) 的 \(V_2=\rho\) 将落到完整几何
\(E_0\) 池，与(12)无 standard 矛盾。
所以原属七的这一分支必须保一个真实的非 \(E_0\)-幂核，
不能把它继续化为七份原 \(j=0\) 椭圆曲线。

## 8. 第二种：两个不同商、唯一 sign 核与非 \(E_0\) 的 genus-two 因子

在(17)中，
\(V_1=\epsilon\oplus\rho\) 已由原目标占满；
\(V_2\) 整体是第5节的单一 CM type 核。
由(12)，它只可能为
$$
\mathbf1^{\oplus2}\quad\text{或}\quad\mathbf1\oplus\epsilon,
\tag{24}
$$
而不能为 \(\epsilon^{\oplus2}\)，因为原整个池的 sign 仅一重。

这两种情况下 \(c\) 固定 \(V_2\)，目标另贡献一维不变量。
(15)迫
$$
V_0^c=0,\quad V_0=\rho,\qquad
g(D_c)=3.
\tag{25}
$$
此时 Riemann–Hurwitz 为
\(12=3(2\cdot3-2)\)，
故 \(D\to D_c\) 是不分歧的真实三阶覆盖。
同时
$$
g(B/\langle c\rangle)=0,\qquad g(B/G)=0.
\tag{26}
$$

现在计算的是另一个商 \(D_G\)。
若(24)第一种成立，则 \(g(D_G)=2\)，
其全部全纯微分上 \(v\) 为标量 \(\omega^2\)。
一个阶3自同构不可能在 genus-two 曲线的 canonical projective
space 上恒等：canonical map 为二次映射，其自同构核至多阶2。
因此第一种不成立，准确剩
$$
\boxed{
V_2=\mathbf1\oplus\epsilon,\qquad
g(D_G)=1,\qquad D_G\text{ 为 }j=0\text{ 椭圆曲线}.
}
\tag{27}
$$
这个 \(D_G\) 在原 \(v\) 下的三阶商才是(26)的有理曲线；
不能把两者直接相等。

(12)还确定其 \(\epsilon\) 部分的真实来源：
它的拉回正是唯一 level36 的 \(17\)-old
\(f_{0,17}\) 线。
\(\mathbf1\) 部分则落在六个 level2601 的 middle-old 线所张空间；
本篇不由一维数目替它指定某个单独 \(\eta\) 标签。

实际 Jacobian 分解为
$$
\boxed{J(D)\sim E_0^5\times J(B).}
\tag{28}
$$
其中 \(g(B)=2\)，\(G\) 在 \(H^0(B,\Omega^1)\) 上为 \(\rho\)。
\(B\) 的 hyperelliptic 六分支点在其阶3商上恰分为两个三点轨道；
在固定有限扩域上可写成
$$
B:\quad Y^2=X^6+bX^3+1,\qquad b^2\ne4.
\tag{29}
$$
原二阶元素是 reciprocal lift 的两种符号之一，
符号仅交换两个椭圆商。
R843 的自含 quotient 与 polarized-dual 计算适用于(29)，
给两个真实3同源椭圆商，因而
$$
\boxed{J(B)\sim E^2,\qquad J(D)\sim E_0^5\times E^2.}
\tag{30}
$$
这里 \(E\) **不能**几何同源于 \(E_0\)：
否则 \(v\) 在 \(J(B)\) 上恒等，会给(11)中不存在的
\(R=1\) 几何 \(E_0\) 子商。
没有把(29)与旧属四的另一个 genus-two quotient 认同，
也没有把 R844 的 CM order17 结论移到这里。

## 9. 回原来源的范围

本篇最先支付的是原层级上的完整几何 CM 池(12)，
包括所有有限定义域后可能出现的 \(E_0\) 因子及全部 old multiplicities。
第5节只在被**实际核的单一 Hodge type**强迫时调用它。
没有对任意 \(K\)-作用或整个 \(J(D)\) 作 CM 假设。

结合 R847，原生成项均有 \(g(D)\ge7\)。
若等号成立，则只有(16)、(17)两种精确结构，
并分别保(22)或(30)的额外非 \(E_0\)-幂部分。
这比只列 Riemann–Hurwitz 的候选更强，
但仍不排除这些剩余来源，也不证明原有限组合或其
critical Abel–Jacobi 值非零。

原 \(q_0,q_2\)、完整 \(\Gamma\) 与 Artin 系数未变；
原 \(6^{-2}\)、\(12^{-2}\)、\(D_X=1632,D_C=816\)
以及有限推前次数全按 R831/R841 保留。
本篇没有用群代数表示更换原 cycle，没有删除最高投影，
也没有由同源分解认定 R814 canonical 比例。

无新增数值运行、目标素数扫描或可重算数据。

## 10. 依据

- K. A. Ribet, *Twists of Modular Forms and Endomorphisms of Abelian Varieties*,
  Math. Ann. **253** (1980), 43–62，Theorem (4.7)，印刷第55页：
  <https://math.berkeley.edu/~ribet/Articles/annalen_253.pdf>。
  本篇应用其几何共同因子判据，且明确处理 Dirichlet-twist 备选；
  不从一个非 CM newform 的系数域维数推断其绝对简单性。
- A. O. L. Atkin–J. Lehner, *Hecke operators on \(\Gamma_0(m)\)*,
  Math. Ann. **185** (1970), 134–160：
  <https://link.springer.com/article/10.1007/BF01359701>；
  原 new/old 分解用于(7)–(8)，指定二处符号另由 R831 付清。
- [R806](R806-original-type-four-order-eighteen-and-negative-two-katz.md)、
  [R844](R844-original-genus-four-cm-order-seventeen-and-two-neighbors.md)：
  原完整 \(\eta\)、局部单位、faithful \(H_{34}\) 与全部有限角色。
- [R826](R826-fixed-low-weight-cm-triple-and-fourth-de-rham-slot.md)、
  [R831](R831-original-dyadic-old-space-and-unique-endpoint-class.md)：
  原 level2601 packet、二处抵消、真实 old 微分与 partial \(W_4\)。
- [R841](R841-original-cubic-normalizer-and-endpoint-chow-purity.md)、
  [R847](R847-original-dyadic-s3-and-genus-seven-lower-bound.md)：
  完整实际 Hom、同一 \(S_3\)、两个 monodromy 除子及循环覆盖维数式。
- [R843](R843-actual-genus-four-quotient-and-cm-three-isogeny.md)：
  仅将其自含 \(Y^2=X^6+bX^3+1\) 的两个椭圆商及3同源计算用于(29)；
  不搬用任何旧 CM order 或原定义域认定。
