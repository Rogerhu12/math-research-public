# R139：固定 CM 曲线的全部奇数层像与完整尖点轨道数

日期：2026-11-12；会话：serre-uniformity-astra-resume2。

**状态：已证明。** 它说明在 R128 剩余的层中，并入固定的三层不会增加 Galois 尖点轨道。本文没有给出新的有理点排除，也不声称所有使用模单位的方法都不可能奏效。

令
$$A:y^2=x^3-x,\quad K=\mathbb Q(i),\quad\mathcal O=\mathbb Z[i],
\quad\mathfrak f=(1+i)^3.$$
令 $m\ge3$ 为奇数；$X_A^u(m)$ 表示固定任意合法 Weil 乘子 $u$ 的完整层扭曲，其几何曲线为 $X(m)$。不同乘子平方类 $u\in(\mathbb Z/m)^\times/((\mathbb Z/m)^\times)^2$ 可给不同的有理扭曲，合数层不只保留正负两类；本文的轨道计数对每一个分别成立。$m=1$ 是 $X(1)$ 的单个有理尖点，下面的向量计数专指 $m\ge3$。

## 1. 在 $K$ 上的完整奇数层像

**命题 139.1。** 对每个奇数 $m$，有
$$\rho_{A,m}(G_K)=(\mathcal O/m\mathcal O)^\times.\tag{1}$$
右边作用在自由秩一的 $\mathcal O/m\mathcal O$ 模 $A[m]$ 上。

**证明。** CM 自同态
$$[i](x,y)=(-x,iy)$$
定义于 $K$。因此 Galois 像包含在右边；$A[m]$ 的秩一结构也可由复一致化 $A(\mathbb C)\simeq\mathbb C/\Lambda$、其中 $\Lambda$ 是一个秩一 $\mathcal O$ 模，直接得到。

实际点
$$P=(i,1-i)\in A(K)$$
满足
$$[2]P=(0,0),\qquad[1+i]P=(1,0),$$
故
$$[1+i]^2P=(0,0)\ne O,\qquad[1+i]^3P=O.$$
所以 $\mathcal O P=A[\mathfrak f]$，且这个阶八的群全部定义于 $K$。这不仅是一个抽象的八整除条件，还给出了准确的 CM 理想湮灭子。

设 $\mathfrak q\nmid2m$ 是 $K$ 的素理想。其 Frobenius 是 $\mathfrak q$ 的唯一生成元 $\pi_{\mathfrak q}$，满足
$$\pi_{\mathfrak q}\equiv1\pmod{\mathfrak f}.\tag{2}$$
这里可以直接核定生成元的方向。若其下有理素数 $q\equiv1\pmod4$，约化为普通情形，Frobenius 与 $i$ 交换，因而属于 $\mathcal O$，范数为 $q$；Frobenius 在微分上的作用为零，故它落在所选择的 $\mathfrak q$ 中，而不是其共轭理想中。它又固定 $A[\mathfrak f]$，故满足 (2)。若 $q\equiv3\pmod4$，则剩余域是 $\mathbb F_{q^2}$，$a_q(A)=0$ 给其 Frobenius 等于 $-q$，它也正是理想 $(q)$ 满足 (2) 的生成元。四个单位在 $(\mathcal O/\mathfrak f)^\times$ 中互异，而后者恰有四个元素，所以这样的生成元唯一。

现取任意 $c\in(\mathcal O/m\mathcal O)^\times$。由中国剩余定理，存在 $\alpha\in\mathcal O$ 满足
$$\alpha\equiv c\pmod m,\qquad\alpha\equiv1\pmod{\mathfrak f}.$$
理想 $(\alpha)$ 与 $2m$ 互素。将其分解成素理想，并把相应 Frobenius 在 $A[m]$ 上的像相乘。由 (2) 和唯一性，所得乘积为 $\alpha\bmod m=c$。所有这些像都属于 Galois 像，所以像包含任意 $c$。这证明 (1)。证毕。

等价地，模 $\mathfrak f m$ 的射线类群经 primary 生成元映到 $(\mathcal O/m)^\times$；类数一及 $(\mathcal O/\mathfrak f)^\times=\mathcal O^\times$ 使该映射为同构。若希望用单个素理想实现指定元素，也可对这一射线类应用素理想分布定理。本文只需整群满像，前面的素理想 Frobenius 乘积已经足够。

以上只使用真实 Frobenius、自同态、$\mathbb Z[i]$ 的唯一分解和 CRT。它也解释了为什么不能在不同奇素数层之间任意加入一个未经证明的共同指数二限制。

## 2. 尖点上的 Galois 模

先在几何上把所选扭曲识别成 $X(m)$。$\mathrm{SL}_2(\mathbb Z)\to\mathrm{SL}_2(\mathbb Z/m)$ 满射（后者由可提升的初等矩阵生成），而 $\infty$ 的整数稳定子为 $\{\pm\left(\begin{smallmatrix}1&n\\0&1\end{smallmatrix}\right):n\in\mathbb Z\}$。取矩阵的第一列，得到完整 $\Gamma(m)$ 尖点集合
$$\operatorname{Cusps}(X(m))=\{v\in(\mathbb Z/m)^2:v\text{ 原始}\}/\{\pm1\}.
$$
原始是指对每个 $\ell\mid m$，两个坐标不同时被 $\ell$ 整除。这里模去的是**一个全局**正负号，不能在 CRT 的每个因子中独立模去正负号。CRT 后每个局部原始对的数量为 $\ell^{2n}-\ell^{2n-2}$；因 $m$ 奇，负号对原始向量的作用无固定点。因此尖点总数为
$$c(m)=\frac12m^2\prod_{\ell\mid m}(1-\ell^{-2}).\tag{3}$$
在扭曲模型上，一个与 Galois 作用相容的描述是：Tate 退化的分量群给出一个原始商
$$A[m]\longrightarrow\mathbb Z/m,$$
并将这个商与其负号视为同一尖点。因此尖点集合是 $A[m]^*$ 的原始元素模 $\{\pm1\}$。Weil 配对给
$$A[m]^*\simeq A[m]\otimes\chi_m^{-1}.$$
若 $\sigma\in G_K$ 在 $A[m]$ 上作用为 $a\in(\mathcal O/m)^\times$，则其在这个对偶模上的作用可写为
$$a/N(a)=\overline a^{-1}.$$
这是单位群的一个自同构，所以命题 139.1 仍给出完整 Cartan 作用。乘子 $u$ 只影响这一标记的选择，不改变原始商的轨道。$G_\mathbb Q\setminus G_K$ 在 $\mathcal O/m$ 上交换共轭的两个分量，并可再乘一个单位；下面的赋值标签不受后一个单位影响。

## 3. 所有奇数 $m$ 的准确轨道数

写 $n_\ell=v_\ell(m)$。若 $\ell\equiv3\pmod4$，则
$$\mathcal O/\ell^{n_\ell}\mathcal O$$
是非分歧二次局部环。一个向量原始，当且仅当对应环元素是单位。因此该处只有一个 Cartan 轨道。

若 $\ell\equiv1\pmod4$，则
$$\mathcal O/\ell^{n}\mathcal O\simeq
(\mathbb Z/\ell^n)\times(\mathbb Z/\ell^n).$$
记零坐标的截断赋值为 $n$。原始向量的两个截断赋值为
$$(0,k)\quad\text{或}\quad(k,0),\qquad0\le k\le n,$$
其中 $(0,0)$ 只计一次。单位群在每个这样的标签内传递，故恰有 $2n+1$ 个 Cartan 轨道。共轭交换两个标签；其唯一固定标签是 $(0,0)$。

**定理 139.2（准确计数）。** CRT 给出全部局部标签的乘积。模去全局 $\pm1$ 不会合并两个不同标签，也不会破坏每个标签内的传递性。复共轭在所有分裂素数处**同时**交换标签。因此，设
$$r(m)=\prod_{\substack{\ell\mid m\\\ell\equiv1\ (4)}}(2n_\ell+1),$$
空积取一，则 Burnside 计数给出
$$
\boxed{\#\bigl(G_\mathbb Q\backslash\operatorname{Cusps}(X_A^u(m))\bigr)
=\frac{r(m)+1}{2}.}
\tag{4}
$$
唯一被共轭固定的 Cartan 轨道，是所有分裂素数处都具有标签 $(0,0)$ 的那个轨道。不能把各分裂素数上的交换当作彼此独立的 Galois 元素。

特别地，尖点只有一个 $G_\mathbb Q$ 轨道，**当且仅当 $m$ 没有模四余一的素因子**。在这种情况下，该唯一闭点的次数就是 (3)；当 $m\ge3$ 时次数至少为四，所以没有有理尖点。

## 4. 对实际剩余分支的含义

**推论 139.3（实际剩余层）。** R128 令 $M=pg$，并证明实际 $E$ 满足 $E[M]\simeq A[M]$，且 $M$ 的全部素因子模四余三。因此，对每一个奇数 $m\ge3$、$m\mid M$ 和每个需要保留的 Weil 乘子扭曲，都有
$$\#\bigl(G_\mathbb Q\backslash\operatorname{Cusps}(X_A^u(m))\bigr)=1.$$
尤其在 $g=3$ 时，由 $p$ 改为 $3p$ 后，虽然曲线的几何亏格和尖点数增加，Galois 尖点轨道数仍为一。标准 Runge 方法要求的额外尖点轨道并未由这一操作产生；也没有因此得到一个秩零商或非整点排除。

这是一条轨道结构结论，而非任何形式的 Runge 不可能性定理。它不排除另有对应、非交换商、积分模型或高度输入可利用；这些需要独立证明。R130 的固定 $m$ 有限性仍成立，但式 (4) 没有使其界统一于变化的 $m$。

所用内部接口：R70 §1 的 $A$ 的 CM 层规范、R128 的最大奇层同余、R130 的完整层扭曲及 Weil 乘子范围。这里将奇数层满像和尖点计数直接证明，未引用新的未发表全局排除。
