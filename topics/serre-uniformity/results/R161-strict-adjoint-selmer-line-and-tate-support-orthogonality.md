# R161：严格特征素数条件、唯一伴随对偶线与实际 Tate 支撑正交

日期：2026-11-12；会话：serre-uniformity-resume2。

**状态：已证明，并完成 $p=43$ 的原始 Robert 单位精确证书。**
本文对 [R157](R157-first-adjoint-character-and-cubic-denominator-support.md)
的首次非 CM 伴随差异保留二维分量，得到一个依赖于固定 $A,p$ 的
一维对偶 Selmer 空间，以及实际最小 Tate 支撑必须满足的正交关系。
它比只构造一般射线角色多使用了实际表示在 $p$ 的完整局部同构。

固定
$$
A:y^2=x^3-x,\qquad K=\mathbb Q(i),\qquad
p>37,\quad p\equiv3\pmod4.
$$
令 $V=A[p]$、$J=[i]$，并定义
$$
W=\{D\in\operatorname{End}_{\mathbb F_p}(V):
       \operatorname{tr}D=\operatorname{tr}(JD)=0\}.
\tag{161.1}
$$
这是二维 $G_{\mathbb Q}$-表示。主要结论如下。

1. 只要求在 $2,p$ 外不分歧、在 $p$ 不加局部限制的空间
   $$
   \mathcal D_p=
   \{d\in H^1(\mathbb Q,W(1)):
          d\text{ 在每个有限 }q\ne2,p\text{ 不分歧}\}
   $$
   准确为一维。其在 $2$ 的局部值自动为零，在 $p$ 的局部值非零。
   该线准确来自 $T=\mathbb Q(A[p])$ 的全局单位，而不是待选的
   辅助 Selmer 类。

2. 对 R19 任一实际原始解对应的 $E$，令
   $$
   n=\min_{q\mid Z}v_p(pv_q(Z)),\qquad
   R=\prod_{\substack{q\mid Z\\v_p(pv_q(Z))=n}}q.
   \tag{161.2}
   $$
   首次差异的 $W$ 分量 $c_W$ 在 $p$ 局部为零，并在每个 $q\mid R$
   有非零奇异分量。任取 $0\ne d_p\in\mathcal D_p$，必有
   $$
   \boxed{\sum_{q\mid R}
   \langle(c_W)^{\mathrm s}_q,(d_p)^{\mathrm f}_q\rangle_q=0.}
   \tag{161.3}
   $$
   上标 $\mathrm f$ 表示不分歧子空间，$\mathrm s$ 表示其商；
   配对为有限—奇异局部 Tate 配对。

3. 若 $R$ 的全部素因子在 $K$ 惰性，则
   $$
   \boxed{\#\{q\mid R:\operatorname{loc}_q(d_p)\ne0\}\ne1.}
   \tag{161.4}
   $$
   特别地，$R=q$ 为单个惰性素数时，必须
   $\operatorname{loc}_q(\mathcal D_p)=0$。
   这里 $R$ 只保留最小 $p$-赋值的 Tate 支撑；允许 $Z$ 还有更高
   $p$-赋值的素因子。

4. 当 $p=43$，一个明确的原始 Robert 单位生成 $\mathcal D_{43}$。
   在全部已指定基下，其局部投影的未除单位因子坐标为
   $$
   \begin{array}{c|rrrr}
   q&859&1031&27691&49019\\ \hline
   S_q&33&16&0&20.
   \end{array}
   \tag{161.5}
   $$
   因此这些 $q$ 中前三个非零列对应的单最小支撑均不可能。
   $859,1031$ 已受 R157 的大小界排除；$49019$ 的排除还使用了
   本文实际对偶线。$S_{27691}=0$ 仅表示这一必要条件不排除它，
   不构造实际 $E$。

主目标仍未解决：(161.3) 可以在多个非零项间抵消，(161.4) 也允许
全部局部值为零；没有由此获得变化 $R,p$ 的统一不存在结论。

## 1. 两个伴随分量与精确局部维数

取一次实的非零 $p$ 挠点 $P$，把 $V$ 识别为
$\mathbb F_{p^2}$，$P$ 对应 $1$、$[i]P$ 对应 $i$。
复共轭 $\tau$ 作用为 $z\mapsto\bar z=z^p$。R70 证明完整像为
非分裂 Cartan 正规化子，且
$$
C=\operatorname{Gal}(T/K)=\mathbb F_{p^2}^{\times}.
$$
Cartan 元素 $a$ 在 $V$ 上作用为乘 $a$，圆分特征为
$\omega(a)=a^{p+1}$。

每个 $W$ 元素唯一写成反线性算子
$$
D_z(v)=z\bar v,\qquad z\in\mathbb F_{p^2}.
$$
因此
$$
a:D_z\longmapsto D_{a^{1-p}z},\qquad
\tau:D_z\longmapsto D_{\bar z}.
\tag{161.6}
$$
并有正交直和
$$
\operatorname{ad}^0V=\mathbb F_p(\eta)J\oplus W,
\qquad \eta=\chi_{-4}.
\tag{161.7}
$$
迹配对 $\operatorname{tr}(DD')$ 在 $W$ 上非退化，给
$W^\vee\simeq W$，故其 Tate 对偶为 $W(1)$。
在 $G_K$ 上，$W(1)$ 的两个特征为 $\psi^2,(\psi^c)^2$；
不是 $V$ 本身，也不是 R65 的 $V(-1)$。

为便于后文追踪，列出需要的维数，均在 $\mathbb F_p$ 上计算。
$q$ 行只用于实际分母素数，因而已经满足 R132 的同余条件。

| 处 | $h^0(W)$ | $h^0(W(1))$ | $h^1(W)$ | $\dim H^1_{\mathrm f}(W)$ | $\dim H^1_{\mathrm s}(W)$ |
|---|---:|---:|---:|---:|---:|
| $p$ | $0$ | $0$ | $2$ | 后文的 flat 线为 $1$ | 此行不使用不分歧商 |
| $2$ | $0$ | $0$ | $0$ | $0$ | $0$ |
| $q\mid Z$、$q$ 在 $K$ 惰性 | $1$ | $1$ | $2$ | $1$ | $1$ |
| $q\mid Z$、$q$ 在 $K$ 分裂 | $2$ | $2$ | $4$ | $2$ | $2$ |

$p$ 处，$V$ 的两个 tame 惯性特征为 niveau $2$ 的
$\omega_2,\omega_2^p$；故 $W$ 的特征为
$\omega_2^{1-p},\omega_2^{p-1}$，$W(1)$ 的特征为
$\omega_2^2,\omega_2^{2p}$，都无惯性不变量。
局部 Euler 特征公式和 Tate 对偶给 $h^1(W)=2$，
同样 $h^1(W(1))=2$。

$2$ 处，R114 的完整惯性像为 $Q_8$。其共轭作用在
$\operatorname{ad}^0V$ 上分成三个非平凡一维 $Q_8/\{\pm1\}$ 特征，
所以 $W^{I_2}=W(1)^{I_2}=0$；圆分特征在 $I_2$ 平凡。
局部 Euler 特征公式直接给两侧整个 $H^1$ 都为零。
这也可由 wild inertia 的 $Q_8$ 像和阶与 $p$ 互素的平均说明。

若 $q$ 惰性，R132 给 $q\equiv-1\bmod p$，
$F=\bar\rho_A(\operatorname{Frob}_q)$ 满足
$F^2=1$、$\operatorname{tr}F=0$、$FJ=-JF$。
它在 $W$ 上有特征值 $1,-1$；在 $W(1)$ 上则交换这两条线。
若 $q$ 分裂，R132 的原始 Tate 特征线给
$F=\epsilon_q I$、$q\equiv1\bmod p$，故两表示都在 $q$ 平凡。
其余表格值由
$$
H^1_{\mathrm f}(\mathbb Q_q,W)=W/(F-1)W,\qquad
H^1_{\mathrm s}(\mathbb Q_q,W)\simeq
\operatorname{Hom}(I_q,\mathbb F_p)\otimes W
\text{ 的 Frobenius 不变量}
$$
以及局部对偶得到。特别地，惰性一维结论不能移植到分裂二维行。

无穷处 $\tau$ 在 $W$ 上特征值为 $1,-1$，所以
$h^0(\mathbb R,W)=1$；$p$ 为奇数使 $H^1(\mathbb R,W)=0$。
全局 $H^0(\mathbb Q,W)$ 与 $H^0(\mathbb Q,W(1))$ 均为零。

## 2. 特征素数处：flat 切线在 $W$，且恰一维

使用 Conrad，*Ramified deformation problems*，
Duke Math. J. **97** (1999), 439–513，Theorem 4.1.2(ii)；
[作者全文](https://math.stanford.edu/~conrad/papers/ramdef.pdf)
中该定理位于作者页 30，紧接 Theorem 4.1.1 的 flat 环
$\mathcal O[[T_1,T_2]]$。

取底域 $\mathbb Q_p$，其绝对分歧指数 $e=1<p-1$。
$A[p]$ 是好超奇异椭圆曲线的 $p$ 挠点，有限平坦模型和 Cartier
对偶均连通，且定理的 Dieudonné exactness 条件由实际 $p$-divisible
group 的 $p$ 挠点满足。局部残余表示绝对不可约。
固定圆分行列式后，Conrad 给整个有限平坦变形函子的环
$$
R^{\mathrm{flat},\det=\chi_p}_p\simeq\mathbb Z_p[[t]].
\tag{161.8}
$$
因此其切空间
$L_p\subset H^1(\mathbb Q_p,\operatorname{ad}^0V)$ 准确为一维。
这是真正对有限 Artin 系数环的结论，不只比较特征零点。

还需确定 $L_p$ 落在 (161.7) 哪一项。以下直接计算避免从
“一维”推测其所在分量。

在 $B=\mathbb F_p[\varepsilon]/(\varepsilon^2)$ 上取
Fontaine–Laffaille 权 $0,1$ 模，基为 $e_1,e_2$：
$$
\operatorname{Fil}^1=Be_1,\quad
\varphi_1(e_1)=e_2,\quad
\varphi_0(e_1)=0,\quad
\varphi_0(e_2)=-e_1+t e_2,\qquad t\in\varepsilon\mathbb F_p.
\tag{161.9}
$$
$\varphi_0|_{\operatorname{Fil}^1}=p\varphi_1=0$，
两个 Frobenius 像生成整个模。$t=0$ 确实对应当前 $A[p]$：
它有整 Fontaine–Laffaille 提升，$\varphi$ 矩阵为
$\left(\begin{smallmatrix}0&-1\\p&0\end{smallmatrix}\right)$，
满足 $\varphi^2=-p$；R157 的 filtered $\varphi$ 唯一性及
绝对不可约残余下的稳定格唯一性将其识别为 $A$ 的局部格。
所以这是实际的有限平坦一阶变形；
Fontaine–Laffaille 原刊 §9.11、Proposition 9.12 给权 $0,1$
模与有限平坦群的对应，Theorem 6.1 给所用完全忠实性。
其行列式模由
$$
\varphi_1(e_1)\wedge\varphi_0(e_2)=e_1\wedge e_2
$$
固定，故行列式不随 $t$ 变化，并等于残余圆分行列式。

$t=\varepsilon$ 不是平凡变形：同构必须保持 $\operatorname{Fil}^1$，
故将 $e_1$ 送到单位倍 $u e_1$，再由 $\varphi_1$ 将 $e_2$
送到同一个 $u e_2$；$\varphi_0$ 随即迫使参数 $t$ 不变。
所以这个非零方向生成整个一维切线。

$\eta|_{G_{\mathbb Q_p}}$ 是未分歧二次特征。
张量此角色把两个 $\varphi_i$ 同时乘 $-1$；改基
$e_2'=-e_2$ 后，(161.9) 的参数恰变成 $-t$。
另一方面 $J$ 实现残余自扭曲 $V\simeq V\otimes\eta$。
局部绝对不可约性说明这条 intertwiner 空间只有一维，
故在伴随切空间上的作用正是 $\operatorname{Ad}(J)$。
其中任意标量差都在伴随作用中消去；无需额外指定自扭曲矩阵平方。
$\operatorname{Ad}(J)$ 在 $\mathbb F_p(\eta)J$ 上为 $+1$，
在 $W$ 上为 $-1$。因此
$$
\boxed{L_p\subset H^1(\mathbb Q_p,W),\qquad\dim L_p=1.}
\tag{161.10}
$$
一维 $\eta$ 分量的 fixed-determinant flat 切线为零。

## 3. 最小 $R=T$ 与唯一严格对偶线

定义 $W$ 的最小 flat Selmer 条件 $\mathcal F$：

- 在 $p$ 取 (161.10) 的 $L_p$；
- 在 $2$ 取整个 $H^1=0$，即固定最小局部型；
- 在其余有限素数取不分歧子空间；
- 在无穷处取 $H^1=0$。

R114 §2–3 已逐项核对最小 Taylor–Wiles 变形定理：
固定圆分行列式，$2$ 处相同完整 $Q_8$ 惯性核和最小型，
$p$ 处有限平坦，除此以外不分歧。残余表示在
$\mathbb Q(\sqrt{-p})$ 上绝对不可约，因为该二次域在 $2$ 不分歧，
其绝对 Galois 群仍包含忠实的 $Q_8$ 惯性像。
唯一层 $32$、权 $2$ 归一化形式为 $f_A$，系数环为 $\mathbb Z_p$；
通过完整 $R=T$ 得到的是
$$
R^{\min}=\mathbb T^{\min}=\mathbb Z_p.
\tag{161.11}
$$
这里使用 Dieulefait–Taixés i Ventosa (2009)，§3 Theorem 3、
§4 Proposition 3 和 Lemma 1 所述已发表输入。
不能仅由唯一特征零形式取代 (161.11)。

因此整个最小 fixed-determinant 伴随切空间为零。
局部条件按 (161.7)、(161.10) 分裂，故
$$
H^1_{\mathcal F}(\mathbb Q,W)=0.
\tag{161.12}
$$

记 $\mathcal F^\perp$ 为 $W(1)$ 上逐处局部 Tate 正交条件。
Poitou–Tate 的 Selmer 维数公式给
$$
\begin{split}
\dim H^1_{\mathcal F}(\mathbb Q,W)
-\dim H^1_{\mathcal F^\perp}(\mathbb Q,W(1))
={}&h^0(\mathbb Q,W)-h^0(\mathbb Q,W(1))\\
&+\sum_v(\dim\mathcal F_v-h^0(\mathbb Q_v,W)).
\end{split}
\tag{161.13}
$$
全局两项为零；$2$ 项为零；$p$ 项为 $1$；
无穷项为 $-1$；其余不分歧项各为零。
所以右边为零，结合 (161.12) 得
$$
H^1_{\mathcal F^\perp}(\mathbb Q,W(1))=0.
\tag{161.14}
$$
这里 $p$ 处的正交条件是二维 $H^1(\mathbb Q_p,W(1))$
中的一条线，并未被当成整个空间。

现在把 primal 的 $p$ 条件从 $L_p$ 缩成 $0$，其余条件不变，
记为 $\mathcal F_0$。其全局 Selmer 仍为零。
对偶的 $p$ 条件恰扩大到整个二维 $H^1$，因此对偶 Selmer
就是本文定义的 $\mathcal D_p$。在 (161.13) 中右端减少 $1$，
准确得到
$$
\boxed{\dim_{\mathbb F_p}\mathcal D_p=1.}
\tag{161.15}
$$
若这条线有非零类在 $p$ 局部为零，它就在 (161.14) 中，
矛盾。更准确地，它的非零局部值不属于 $L_p^\perp$。
这说明 (161.15) 不是凭空指定的一条线，也不是只证明维数至多一。

## 4. 实际首差类与全部局部项

设 $E$ 为 R19 任一实际三族原始解。R114、R128 给准确深度 (161.2)。
选择整基使 $\rho_E\equiv\rho_A\bmod p^n$，定义
$$
c_E(\sigma)=
\frac{\rho_E(\sigma)\rho_A(\sigma)^{-1}-1}{p^n}\bmod p.
\tag{161.16}
$$
相同行列式使它取值于 $\operatorname{ad}^0V$，
且为真正一阶 cocycle。令
$$
c_E=x_EJ+c_W
$$
为 (161.7) 的两项投影；$x_E|_{G_K}$ 就是 R157 的反循环角色
$\kappa$。

### 4.1 $p$ 处是零类，而非仅满足 flat

R157 §2 已给出完整局部证明，关键环节重列如下。
$p\ge5$ 时好超奇异曲线 $A,E$ 都有 $a_p=0$。
采用反变 $D_{\mathrm{cris}}^*$ 规范，其 Frobenius 满足
$\varphi^2=-p$；每条 $\operatorname{Fil}^1$ 非零向量 $v$
和 $\varphi v$ 都组成基，因此两个 filtered $\varphi$ 模同构。
Fontaine 的完全忠实性给有理局部 Tate 模同构。
niveau $2$ 残余表示局部绝对不可约，使稳定整格唯一到位似，
故可得到整局部同构。

还必须对齐给定的模 $p^n$ 全局同构。
局部残余 endomorphism 只有标量，逐级减标量再除 $p$ 得
$\operatorname{End}_{G_{\mathbb Q_p}}(A[p^n])=\mathbb Z/p^n$。
所以整局部同构乘一个标量单位即可与给定有限层同构精确一致。
其首差是局部 coboundary，从而
$$
\operatorname{loc}_p(c_W)=0.
\tag{161.17}
$$
反变规范和该格子论证均不可省去。

### 4.2 其余各处

$2$ 处整个 $H^1(\mathbb Q_2,W)$ 为零。
$q\nmid2pZ$ 时两个表示都不分歧。
$q\mid Z$ 的惯性是实际 Tate 扩张：
$$
\rho_E(\sigma)|_{I_q}\sim
\begin{pmatrix}1&p\,v_q(Z)t_p(\sigma)\\0&1\end{pmatrix}.
\tag{161.18}
$$
非分裂乘法扭曲在惯性平凡，不改变该式。

若 $v_p(pv_qZ)>n$，(161.16) 在惯性为零。
若 $q\mid R$，取 $t_p(\sigma)=1$，
$D=c_E(\sigma)$ 是非零秩一 nilpotent。
写
$$
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
D=xJ+\begin{pmatrix}a&b\\b&-a\end{pmatrix}=xJ+D_W.
$$
则
$$
D^2=(a^2+b^2-x^2)I=0.
\tag{161.19}
$$
若 $x=0$，$-1$ 非平方迫使 $a=b=0$；若 $D_W=0$，
$J^2=-1$ 迫使 $x=0$。两者都矛盾。因此
$$
x\ne0,\qquad D_W\ne0
\quad(q\mid R).
\tag{161.20}
$$
特别地 $c_W$ 每个最小支撑的奇异坐标都非零。
这是真正实际 Tate nilpotence 的限制；不是一般放松 Selmer 类
自动具有的性质。

## 5. Poitou–Tate 正交与惰性符号

把 $\mathcal F_0$ 在 $q\mid R$ 的条件放松为整个局部 $H^1$，
记所得 Selmer 空间为 $H_R$。§4 给 $c_W\in H_R$。
Selmer 条件比较的精确序列为
$$
0\longrightarrow H_R
\longrightarrow \bigoplus_{q\mid R}H^1_{\mathrm s}(\mathbb Q_q,W)
\xrightarrow{\ \Lambda_R\ }\mathcal D_p^\vee
\longrightarrow(\mathcal D_p^R)^\vee
\longrightarrow0,
\tag{161.21}
$$
其中
$$
\mathcal D_p^R=
\{d\in\mathcal D_p:\operatorname{loc}_q d=0\ \forall q\mid R\},
$$
而
$$
\Lambda_R((z_q))(d)=
\sum_{q\mid R}\langle z_q,\operatorname{loc}_q d\rangle_q.
$$
左端没有遗漏最小全局类，因为
$H^1_{\mathcal F_0}(\mathbb Q,W)=0$。
公式亦直接由全局杯积互反得到：$p$ 和 $2$ 项为零，
其余非支撑素数两类都不分歧，局部配对为零。
故 (161.3) 成立。

如果 $\mathcal D_p$ 至少在一个 $q\mid R$ 局部非零，
$\Lambda_R$ 的秩为 $1$；否则其秩为 $0$。
因此本文也准确确定了可能的奇异向量空间：
$$
\dim H_R=\sum_{q\mid R}\dim H^1_{\mathrm s}(\mathbb Q_q,W)
-\begin{cases}1,&\exists q\mid R:\operatorname{loc}_q d_p\ne0,\\
0,&\text{全部局部值为零}.
\end{cases}
\tag{161.22}
$$
这个空间包括很多一般变形类；只有实际 $c_W$ 还满足 (161.19)。

### 5.1 惰性素数的两个 Tate 符号

设 $q\mid R$ 在 $K$ 惰性，取 $F=\bar\rho_A(\operatorname{Frob}_q)$，
并令
$$
K_q=JF\in W.
$$
它满足 $K_q^2=1$、$\operatorname{Ad}(F)K_q=-K_q$，
生成奇异的一维方向。记
$\epsilon_q=+1$ 表示 $E$ 在 $q$ 分裂乘法，
$\epsilon_q=-1$ 表示非分裂乘法。
这里与“$q$ 在 CM 域惰性”是不同的两种判别。

在兼容 CM 的基中可以写
$F=\operatorname{diag}(1,-1)$，
$K_q=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)$。
Tate 惯性像的核是 Frobenius 特征值
$\epsilon_q q=-\epsilon_q$ 的环面线。于是
$$
D=x_qJ+\epsilon_qx_qK_q,\qquad x_q=\kappa(\sigma)\ne0,
\tag{161.23}
$$
即分裂时为非零下三角 nilpotent，非分裂时为非零上三角 nilpotent。
固定相同 tame 基并令
$a_q(d_p)=\langle K_q,\operatorname{loc}_q d_p\rangle_q$，
当全部 $q\mid R$ 惰性时，(161.3) 写成
$$
\boxed{\sum_{q\mid R}\epsilon_qx_q a_q(d_p)=0.}
\tag{161.24}
$$
配对定义保留了局部 reciprocity 的方向；
改变 tame 生成元会同时改变坐标与对偶基，不影响等式或零性。

一维局部配对非退化，故
$a_q(d_p)\ne0\iff\operatorname{loc}_q d_p\ne0$。
每个 $\epsilon_qx_q$ 非零，立即得到 (161.4)。
不能在多个非零项时阻止抵消。

### 5.2 单个分裂素数只能得到二次型条件

若 $R=q$ 且 $q$ 在 $K$ 分裂，局部两个空间都是二维，
不能由 (161.3) 推出 $\operatorname{loc}_q d_p=0$。
在固定 $\mu_p$ 基后把这个局部值记为 $z\in W$，令
$$Q(D)=-\det D,\qquad Q(aH+bK)=a^2+b^2.$$
若 $z\ne0$，正交条件迫使 $D_W$ 位于直线
$\mathbb F_pJz$。而 $Q(Jz)=Q(z)$，
(161.19) 又给 $Q(D_W)=x^2$ 为非零平方。因此必要条件是
$$
\boxed{z=0\quad\text{或}\quad Q(z)\in\mathbb F_p^{\times2}.}
\tag{161.25}
$$
改变单位根基、$d_p$ 的非零标量或兼容标架都只把 $Q(z)$
乘一个平方；该判据不依赖这些选择。本文的有限域实算专门用于
惰性一维情形，没有把它冒充 (161.25) 的分裂计算。

## 6. 这条对偶线准确由全局单位给出

令 $G=\operatorname{Gal}(T/\mathbb Q)$，阶为 $2(p^2-1)$，与 $p$ 互素。
Kummer、inflation–restriction 和取不变量的精确性给自然单射
$$
\left(\mathcal O_T^\times/(\mathcal O_T^\times)^p\otimes_{\mathbb F_p}W\right)^G
\hookrightarrow H^1(\mathbb Q,W(1)).
\tag{161.26}
$$
这一步中 $W(1)$ 的 $(1)$ 已由 Kummer 的 $\mu_p$ 提供，
所以张量的是 $W$，不能再次额外扭曲。

该像在 $2,p$ 外不分歧：$T/\mathbb Q$ 在这些素数不分歧，
剩余特征不为 $p$ 时单位的 $p$ 次 Kummer 扩张也不分歧。
所以 (161.26) 的像包含在 $\mathcal D_p$。

还可准确计算其维数。$T$ 全虚，Dirichlet 单位表示为
$$
\mathcal O_T^\times\otimes\mathbb Q_p
\simeq\operatorname{Ind}_{\langle\tau\rangle}^{G}\mathbf1-\mathbf1.
\tag{161.27}
$$
采用 $W$ 的 Teichmüller $\mathbb Z_p$ 提升：
Cartan 特征 $a^{1-p}$ 提到 $\mathbb Z_{p^2}$ 的 Teichmüller 单位，
$\tau$ 仍作用为共轭。两个 Cartan 特征不同且被 $\tau$ 交换，
所以该提升绝对不可约，没有额外 endomorphism 维数因子。
$W$ 无平凡分量，且 $\dim W^\tau=1$，
故 (161.27) 中 $W$ 的重数为一。
由于 $p\nmid|G|$，整格的投影和不变量取法精确，模 $p$ 重数保持；
单位根的可能 $p$ 挠元只给一维圆分角色，不含 $W$。
因此 (161.26) 左端准确一维，结合 (161.15) 得
$$
\boxed{
\left(\mathcal O_T^\times/(\mathcal O_T^\times)^p\otimes W\right)^G
\simeq\mathcal D_p.}
\tag{161.28}
$$
这证明全 $p$ 的单位来源，但并未自动宣布某个预选 Robert 单位
投影非零。下面用实际局部计算证明 $p=43$ 时选定单位确为生成元。

## 7. 原始 Robert 单位、正确特征和有理下降

R70 已证明
$$
T=K((1+i)^3p),\quad P_2=(i,1-i),\quad
v=\frac{\Delta_A^{10}}{\psi_{11}(P_2+P)},\quad \Delta_A=64.
\tag{161.29}
$$
这里 $P$ 是 §1 固定的实 $p$ 挠点。
$v$ 与 Robert 的规范单位只差十二次单位根；
导子有 $2,p$ 两个不同素因子，所以它确为全局单位。
$p>37$ 使十二次单位根在模 $p$ Kummer 群中为零。

由 (161.6)，本次单位特征和投影为
$$
\chi(a)=a^{p-1},\qquad
\xi=e_\chi[v]=\frac1{p^2-1}
\sum_{a\in\mathbb F_{p^2}^\times}a^{1-p}[\sigma_a v].
\tag{161.30}
$$
这是正确的 $W(1)$ Kummer 数据；R70 的 $\rho^p$ 特征属于另一表示。
R70、R65 加入的额外 $(7)$ Euler 因子在此为
$$1-\chi(-7)^{-1}=0.$$
所以必须使用 (161.29) 的原始单位，不能沿用已经乘该因子的 $u_1$。

$\psi_{11}$ 在 $[i]$ 下不变，且 $\tau P_2=[i]P_2$，
所以精确有
$$\tau v=\sigma_{-i}v.$$
在 Kummer 张量坐标中，$\tau$ 同时作用于单位并对系数取
$\bar z=z^p$。把 (161.30) 的下标换成 $b=-i\bar a$，
因 $i^{1-p}=-1$ 得
$$
\tau\xi=-\xi,\qquad \tau(i\xi)=i\xi.
\tag{161.31}
$$
这里第二个等式使用 $\tau(i)=-i$。
因此 $i\xi$ 唯一下降为某个
$$d^{\mathrm{Rob}}_p\in H^1(\mathbb Q,W(1)).$$
它属于 (161.28)；非零时便生成 $\mathcal D_p$。
没有把未下降的 $\tau$ 负分量直接当成有理类。

### 7.1 有限域公式及 $Q/K$ 的因子二

取素数 $q\equiv-1\bmod4p$。R70 的全部原始导子挠点在
$k_q=\mathbb F_q[i]$ 有理。选 $0\ne P_q\in A(\mathbb F_q)$，
使同一全局 $P$ 在所选 $T$ 素点约化为 $P_q$；
Cartan 对非零挠点传递，所以可逐处作此选择。
这样局部 Frobenius 在 $T/\mathbb Q$ 的像就是固定的 $\tau$。
不同 $q$ 的素点选择互不冲突，不要求一个全局元素同时搬动各素点。

固定全局原始单位根
$$\zeta_0=e_p(P,[i]P),$$
再在每个 $q$ 选证书中的原始根 $\zeta_q$，写
$\bar\zeta_0=\zeta_q^{k_q}$，其中 $k_q\in\mathbb F_p^\times$。
定义
$$
\psi_{11}(P_2+[a]P_q)^{(q^2-1)/p}
=\zeta_q^{\ell_q(a)},\qquad
S_q=\sum_{a\ne0}a^{1-p}\ell_q(a).
\tag{161.32}
$$
$Q_a=P_2+[a]P_q$ 的整数阶为 $4p$，故 $\psi_{11}(Q_a)\ne0$，
上述对数始终存在且唯一。

Robert 的倒数给一个负号，$[T:K]^{-1}\equiv-1\bmod p$
给另一个负号；常数 $\Delta_A^{10}$ 的非平凡特征投影为零。
因此 $\xi$ 的局部 Kummer 坐标恰为 $S_q$。
从 $P_q$ 实有理、$\tau P_2=[i]P_2$ 得
$$
\ell_q(-i\bar a)=-\ell_q(a),\qquad S_q=\bar S_q\in\mathbb F_p.
\tag{161.33}
$$

在 $W(1)$ 坐标上，$\operatorname{Frob}_q$ 作用为 $z\mapsto-\bar z$，
其不分歧正特征线是 $i\mathbb F_p$。
所以 $d_p^{\mathrm{Rob}}$ 限制到 $K_{(q)}$ 的 Frobenius 值为
$iS_q/k_q$。限制从 $\mathbb Q_q$ 到该未分歧二次扩张把
不分歧 Frobenius 类乘 $1+\operatorname{Frob}_q=2$，
故有理层坐标为
$$
\boxed{d_p^{\mathrm{Rob}}(\operatorname{Frob}_q)
=\frac{iS_q}{2k_q}
\quad\text{于所选不分歧商。}}
\tag{161.34}
$$
$2k_q$ 是单位。因此无需给不带规范基的数值冒名：
$$
\operatorname{loc}_q(d_p^{\mathrm{Rob}})=0
\quad\Longleftrightarrow\quad S_q=0.
\tag{161.35}
$$
改变 $P_q$、单位根基或素点只改变非零基因子与可能的共轭，
不改变零性。

## 8. $p=43$ 的完整精确证书

代码及小型输出：

- [标准库核验器](../notes/verify_r161_adjoint_unit_residues.py)；
- [四处证书与首次零值有限搜索](../notes/r161_adjoint_unit_residue_certificates.json)。

从仓库根目录可执行：
```bash
python3 topics/serre-uniformity/notes/verify_r161_adjoint_unit_residues.py --check
```
也可在命令末尾指定单个 $q$；`--search` 按递增次序计算至首个零。

算法复用 R70 已写明的除法多项式递推和实际曲线加法，
但对每一个 $a=u+vi\ne0$ 使用本次正确权
$$
a^{1-p}=\frac{a}{\bar a}
=\frac{u^2-v^2+2uvi}{u^2+v^2}.
\tag{161.36}
$$
每处完整枚举 $1848$ 个点。程序还用独立的有限域幂法重算
所有权、逐项检查 (161.33)，并对 $P_q\mapsto[b]P_q$
检查完整求和按 $\chi(b)$ 变换；不是只检查最终虚部为零。

使用试除到平方根的确定性素性判断，所有域运算均为整数模运算。
证书的四处如下：

| $q$ | $P_q$ | $\zeta_q$ | $S_q$ | 局部是否为零 |
|---:|---|---|---:|---|
| $859$ | $(209,268)$ | $97+829i$ | $33$ | 否 |
| $1031$ | $(808,263)$ | $825+475i$ | $16$ | 否 |
| $27691$ | $(6698,18165)$ | $21904+6578i$ | $0$ | 是 |
| $49019$ | $(11536,29305)$ | $19416+40301i$ | $20$ | 否 |

因为 $859$ 的局部值非零，$d_{43}^{\mathrm{Rob}}\ne0$。
结合准确维数 (161.15)，它就是 $\mathcal D_{43}$ 的生成元。
这是生成性的证明，未用类数猜测、椭圆单位指数猜测或 $p$ 进近似。

搜索还完整检查了 $q\le27691$、$q\equiv-1\bmod172$ 的全部
$36$ 个素数；前 $35$ 个投影非零，第 $36$ 个为零。
完整 $(q,S_q)$ 表及对数表 SHA 均保存在 JSON。
核验器的 `--check` 会重新计算这全部 $36$ 行，
不把文件中的“第一个”标记当作证明。

$49019$ 在 R70 的 $V$ 基类上投影为零，
在本次 $W(1)$ 的真实对偶类上却非零。
两个结果涉及不同特征，完全相容；本文没有修改先前证书。
由 (161.4)，不可能有实际解的最小支撑
$$R=49019\quad\text{或}\quad R=27691\cdot49019.$$
第二个结论用到这两个因子均在 $K$ 惰性，
以及两个局部值中恰有一个非零。
更高 Tate 指数的其他分母素数不影响这两个判断。

## 9. 来源与尚未得到的结论

- B. Conrad, *Ramified deformation problems*, Duke Mathematical Journal
  **97** (1999), no. 3, 439–513，
  [DOI](https://doi.org/10.1215/S0012-7094-99-09718-1)；
  [作者全文](https://math.stanford.edu/~conrad/papers/ramdef.pdf)，
  Theorem 4.1.1、Theorem 4.1.2(ii)，作者页 26、30。
  用于完整 fixed-determinant flat 环及其切空间维数。
- J.-M. Fontaine and G. Laffaille, *Construction de représentations
  $p$-adiques*, Annales scientifiques de l'É.N.S. (4) **15** (1982),
  547–608，
  [原刊全文](https://www.numdam.org/item/10.24033/asens.1437.pdf)，
  Theorem 6.1（印刷页 581）、§9.11 与 Proposition 9.12
  （印刷页 604–605）。用于 (161.9) 的真实有限平坦实现及完全忠实性。
- L. Dieulefait and X. Taixés i Ventosa, *Congruences between modular forms
  and lowering the level mod $\ell^n$*, JTNB **21** (2009), 109–118，
  [DOI](https://doi.org/10.5802/jtnb.660)、
  [作者全文](https://arxiv.org/pdf/0801.0104)，
  §3 Theorem 3、§4 Proposition 3 和 Lemma 1。完整假设在 R114 及 §3 核对。
- 局部 Tate 对偶、Poitou–Tate Selmer 条件比较与维数公式，
  可见 B. Mazur and K. Rubin, *Kolyvagin Systems*, Memoirs AMS
  **168** (2004), no. 799，Theorem 2.3.4 与 Proposition 2.3.5
  （印刷页 17）；
  [作者版本](https://webusers.imj-prg.fr/~christophe.cornut/ES/Ref/KolySys.pdf)。
- 原始 Robert 单位的单位性、准确导子、primary Artin 方向和
  $\Delta_A^{10}/\psi_{11}$ 公式沿用 R70 §1–3：
  K. Rubin (1991) 印刷页 28–31，Robert 范数约定参见
  Oukhaba–Viguié (2013) §4。本文在 §7 保留本次不同特征与下降符号。
- [R114](R114-exact-cm-congruence-depth-from-minimal-deformations.md)、
  [R128](R128-all-odd-congruence-depth-and-split-prime-power-exclusion.md)、
  [R132](R132-maximal-congruence-level-and-split-multiplicative-prime-bound.md)、
  [R157](R157-first-adjoint-character-and-cubic-denominator-support.md)：
  分别提供最小变形、准确奇层同余、实际支持素数同余和首次差类。

本文得到的是实际曲线必须满足的新全局对偶约束及明确排除实例。
它没有使 $\mathcal D_p$ 的局部值在所有可能素数上非零，
也没有禁止多个非零项抵消。一般 $p$ 的具体 Robert 投影若未计算，
不能仅凭单位空间一维就宣布该特定单位非零。
没有使用辅助曲线的秩假设，没有把 (161.22) 当成实际椭圆曲线存在，
也没有从一次有限素数搜索推出统一排除。

