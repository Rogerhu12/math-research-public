# R62：有限矩阵放大与所有非零二元解析芽的单射稠密性

日期：2026-11-12（UTC）。子任务：`literature`。**状态：已证明的中间结论。**

本条先沿用 R60 的实际加权 odometer $A$ 与原临界对数 $L$；第 9 节将同一结论扩至 R61 的全部复幂次渐近尾对数。它把 R60 的标量核消除证明放大到有限矩阵，再由一个自含的局部解析因式分解，证明每个非零收敛二元解析芽 $F(z,w)$ 的算子值 $F(A,L)$ 都单射且值域稠密。特别地，任何非零有限和

$$
\sum_{j=1}^s c_j e^{\alpha_j A+\beta_j L}h
$$

在参数对 $(\alpha_j,\beta_j)$ 两两不同、$h$ 对 $A$ 循环时仍循环。

这里的“非零”首先指解析芽本身非零；证明同时说明其算子值必非零。这比仅由 R32 的代数无零因子推出结果更强，也没有把代数无零因子误当作具体 Hilbert 表示中每个元素都单射。本条的解析芽像仍是 $\mathcal A$ 中稠密、第一纲的真子代数，故没有覆盖任意 $X\in\mathcal A$，更没有解决完整 Hilbert 不变子空间问题。

依赖：R9/R11 的实际模型及循环性；R24 的双线性对称性；R32 的谱与解析闭包；R50/R60 的明确进位误差；R60 §§1–3 的加权 Bernstein–Walsh 不等式及严格负常数证书。新的矩阵放大、解析芽演算、局部因式分解及其应用均在下文给出完整证明。

## 1. 固定模型与需要复用的严格估计

记

$$
H=L^2(\mathbb Z_2,\mu),\qquad
\mathcal A=\overline{\mathbb C[I,A]}^{\|\cdot\|}.
$$

$A$ 单射、值域稠密、拟幂零。常向量 $1$ 对 $A$ 及 $A^*$ 都循环。共轭与双线性型为

$$
Cf(y)=\overline{f(-1-y)},\qquad
B(f,g)=\langle f,Cg\rangle.
$$

内积按第一变量线性约定。$CA^*C=A$；对每个 $X\in\mathcal A$ 都有 $CX^*C=X$。

设 $a_j$ 为赋值层权，$\eta_j=a_{j+1}/a_j$，且 $a_0<1$。R60 使用的严格界为

$$
\eta_j\le e^{-770\,16^j}. \tag{1.1}
$$

令 $A_k$ 为删除全部 $v_2(y)\ge k$ 权的截断。它只作用于前 $k$ 个二进位，满足

$$
A_k^{2^k}=0,\qquad
\|A-A_k\|=a_k,\qquad
\|A_k^n\|\le\|A^n\|\quad(n\ge0). \tag{1.2}
$$

最后一个不等式可直接从路径权看出：$A_k^n$ 的每个非零路径与 $A^n$ 的相同路径有相同权，另一些路径被置零。因此其权乘积的本质上确界不超过 $A^n$ 的本质上确界。这里无需假设 $A$ 与 $A_k$ 交换。

沿用 R60 的

$$
\delta_j=\frac{2}{(j+2)^2+1},\qquad
\Delta=\sum_{j\ge0}\delta_j\le2,
$$

以及作用于第 $j$ 位的 $E_j=e_{10}$。R60 给出 $A_k$ 的无常数项多项式 $G_k$，使

$$
T_k=G_k+\sum_{j\ge k}\delta_jE_j,
\qquad
\|L-T_k\|\le22\eta_{k-1},
\qquad
\|G_k\|\le\tfrac83\Delta. \tag{1.3}
$$

原临界对数 $L\in\mathcal A$、$c_0(L)=0$，故 R32 给 $r(L)=0$。本条仅使用这些已证明的具体事实，不把任意 $\mathcal A$ 元素都假设为有相同进位误差。

### 1.1 尾范数与 BW 常数

记

$$
C_m=\sum_{j\ge m}\delta_jE_j,\qquad
F_m(t)=\|e^{-tC_m^*}1\|,
$$

$$
h(u)=\frac12\int_1^\infty
\log\left(1-\frac{u}{x^2}+\frac{u^2}{2x^4}\right)dx.
$$

令 $M=m+2$。R60 已证明，对 $1\le u\le20$，

$$
e^{Mh(u)-14}\le F_m(uM^2/2)\le e^{Mh(u)+14},
\qquad
F_m(uM^2/2)\ge e^{-10M-14}. \tag{1.4}
$$

对于区间 $[1,20]$，置

$$
g_0=\log\frac{\sqrt{20}+1}{\sqrt{20}-1},
\qquad
d\omega_0(u)=\frac{\sqrt{20}\,du}
{\pi u\sqrt{(u-1)(20-u)}}.
$$

$\omega_0$ 是概率测度。若 $p$ 为次数至多 $d$ 的多项式，则

$$
\log|p(0)|\le d g_0+
\int_1^{20}\log|p(u)|\,d\omega_0(u). \tag{1.5}
$$

R60 的完整证书给出

$$
J:=g_0+\int_1^{20}h(u)\,d\omega_0(u)
\le-\frac{51746665241}{375000000000}<-\frac{13}{100}. \tag{1.6}
$$

后面的矩阵维数只增加 $o(M)$ 的多项式次数，不改动 $h$、$\omega_0$ 或负常数 $J$。

## 2. 解析芽的范数演算与截断误差

记 $\mathbb C\{z,w\}$ 为原点附近收敛的二元幂级数环；矩阵系数的单变量解析芽作同样理解。

### 引理 2.1：二元解析芽可在 $(A,L)$ 上作范数绝对收敛的演算

对任意 $F\in\mathbb C\{z,w\}$，其 Taylor 级数

$$
F(z,w)=\sum_{p,q\ge0}f_{pq}z^pw^q
$$

在 $(A,L)$ 上绝对范数收敛，并定义含幺代数同态

$$
F\longmapsto F(A,L)\in\mathcal A. \tag{2.1}
$$

若 $F(0,0)\ne0$，则 $F(A,L)$ 在 $\mathcal A$ 中可逆。

**证明。** 在一个闭双圆盘上使用 Cauchy 系数界，存在 $K,\rho,\sigma>0$，使

$$
|f_{pq}|\le K\rho^{-p}\sigma^{-q}.
$$

由于 $r(A)=r(L)=0$，对任意 $0<\epsilon<\rho$、$0<\theta<\sigma$，存在有限常数 $C_A,C_L$ 满足

$$
\|A^p\|\le C_A\epsilon^p,\qquad
\|L^q\|\le C_L\theta^q
\quad(p,q\ge0).
$$

于是

$$
\sum_{p,q}|f_{pq}|\,\|A^pL^q\|
\le KC_AC_L
\sum_{p,q}(\epsilon/\rho)^p(\theta/\sigma)^q<\infty.
$$

$A,L$ 交换，绝对收敛允许重新排列 Cauchy 乘积，因此 (2.1) 乘法相容。每个有限和属于 $\mathcal A$，故极限也属于它。若 $F(0,0)\ne0$，则 $1/F$ 是一个解析芽，乘法相容给

$$
F(A,L)(1/F)(A,L)=I.
$$

此证明不要求两个算子范数位于原解析芽的收敛圆盘内；使用的是它们幂的任意小指数界。证毕。

### 引理 2.2：解析矩阵函数的统一截断界

若 $M(z)$ 是一个 $r\times r$ 矩阵值解析芽，则存在有限常数 $K_M,B_M$，与 $k$ 无关，使

$$
\|M(A)-M(A_k)\|\le K_M a_k,
\qquad
\sup_k\|M(A_k)\|\le B_M. \tag{2.2}
$$

这里的矩阵算子作用于 $H\otimes\mathbb C^r$。

**证明。** 写 $M(z)=\sum_{n\ge0}M_nz^n$，取 $\rho,K>0$ 使 $\|M_n\|\le K\rho^{-n}$。固定 $0<\epsilon<\rho$。由 (1.2) 和拟幂零性，存在 $C_\epsilon$，使对全部 $n,k$，

$$
\|A^n\|,\ \|A_k^n\|\le C_\epsilon\epsilon^n.
$$

对不必交换的 $A,A_k$ 使用通常的差幂恒等式，得到

$$
\begin{aligned}
\|A^n-A_k^n\|
&\le\sum_{j=0}^{n-1}
\|A^{n-1-j}\|\,\|A-A_k\|\,\|A_k^j\|\\
&\le nC_\epsilon^2\epsilon^{n-1}a_k.
\end{aligned}
$$

因此可取

$$
K_M=C_\epsilon^2\sum_{n\ge1}n\|M_n\|\epsilon^{n-1}<\infty,
\qquad
B_M=C_\epsilon\sum_{n\ge0}\|M_n\|\epsilon^n<\infty.
$$

这些级数也证明 $M(A)$ 的演算有定义。$A_k^{2^k}=0$，故 $M(A_k)$ 实际为有限多项式矩阵。证毕。

## 3. 有限矩阵放大的单射与稠密定理

**定理 3.1。** 设 $M(z)$ 是 $r\times r$ 矩阵值解析芽，且 $M(0)$ 幂零。则

$$
S=L\otimes I_r-M(A) \tag{3.1}
$$

在 $H\otimes\mathbb C^r$ 上单射且值域稠密。

### 3.1 真正的头部幂零阶

取整数 $d\ge1$ 使 $M(0)^d=0$；总可取 $d=r$。置

$$
R_k=G_k\otimes I_r-M(A_k).
$$

矩阵的每个条目都是 $A_k$ 的多项式。把这些条目模去理想 $(A_k)$ 后，$G_k$ 的像为零，$M(A_k)$ 的像为 $M(0)$。因此 $R_k^d$ 的每个条目都被 $A_k$ 整除，即存在矩阵算子 $V_k$，其条目仍为 $A_k$ 的多项式，且

$$
R_k^d=(A_k\otimes I_r)V_k.
$$

右边两个因子交换；由 $A_k^{2^k}=0$，

$$
R_k^{d2^k}=0. \tag{3.2}
$$

此处没有把矩阵 $M(A_k)$ 自身的范数小当作幂零性的理由，也没有把低位头部的阶误记成 $k+1$。其阶是至多 $d2^k$。

对 $m>k$ 定义

$$
H_{k,m}=R_k+
\sum_{j=k}^{m-1}\delta_jE_j\otimes I_r,
\qquad
\widetilde T_k=H_{k,m}+C_m\otimes I_r.
$$

中间段作用于与 $R_k$ 不相交的二进位，且其幂零阶至多 $m-k+1$。由二项展开，

$$
H_{k,m}^{\,d2^k+m-k}=0. \tag{3.3}
$$

另外 $H_{k,m}$ 与 $C_m\otimes I_r$ 交换。

### 3.2 实际矩阵算子的误差仍超快

由 (1.3)、(2.2)，以及 $a_k=a_{k-1}\eta_{k-1}\le a_0\eta_{k-1}$，有

$$
\|S-\widetilde T_k\|
\le22\eta_{k-1}+K_Ma_k
\le K\eta_{k-1},
\qquad K=22+K_Ma_0. \tag{3.4}
$$

由 (1.3) 和 (2.2)，可固定一个有限常数 $B$，使对所有 $k<m$，

$$
\|H_{k,m}\|\le B,
\qquad \|C_m\otimes I_r\|\le B. \tag{3.5}
$$

例如取 $B=(8/3)\Delta+B_M+\Delta$ 即可。$B$ 可以依赖给定解析矩阵，但不依赖尺度 $m,k$。

现在令

$$
M_*=m+2,\qquad
k=\left\lfloor\frac34\log_2M_*\right\rfloor.
$$

本节暂以 $M_*$ 记尺度，避免与矩阵函数 $M(z)$ 混淆。则

$$
2^k\le M_*^{3/4},\qquad
16^{k-1}\ge M_*^3/256.
$$

因此 (1.1) 给

$$
\eta_{k-1}\le e^{-3M_*^3}. \tag{3.6}
$$

### 3.3 用同一尾部范数控制一个标量多项式

设 $S\mathbf f=0$。对实数 $t\ge0$，利用头、尾交换，直接对
$e^{(t-s)H_{k,m}}e^{-s(C_m\otimes I_r)}\mathbf f$ 求导，得到

$$
e^{tH_{k,m}}\mathbf f-e^{-t(C_m\otimes I_r)}\mathbf f
=\int_0^t e^{(t-s)H_{k,m}}
e^{-s(C_m\otimes I_r)}\widetilde T_k\mathbf f\,ds.
$$

由 (3.4)–(3.6)，

$$
\left\|e^{tH_{k,m}}\mathbf f-e^{-t(C_m\otimes I_r)}\mathbf f\right\|
\le Kt e^{Bt-3M_*^3}\|\mathbf f\|. \tag{3.7}
$$

这里仅用 $\widetilde T_k\mathbf f=(\widetilde T_k-S)\mathbf f$；不需要 $S$ 与 $\widetilde T_k$ 交换。

对 $1\le u\le20$ 取 $t=uM_*^2/2\le10M_*^2$。固定的 $B,K$ 不影响最高次负项，所以当 $m$ 足够大时，

$$
10KM_*^2e^{10BM_*^2-3M_*^3}\le e^{-20M_*}. \tag{3.8}
$$

固定单位向量 $v\in\mathbb C^r$，定义

$$
p_{m,v}(u)=
\langle e^{uM_*^2H_{k,m}/2}\mathbf f,1\otimes v\rangle.
$$

由 (3.3)，它是次数至多

$$
n_m=d2^k+m-k-1\le M_*+dM_*^{3/4} \tag{3.9}
$$

的复多项式。对实区间 $[1,20]$，尾部对偶估计为

$$
\begin{aligned}
|\langle e^{-t(C_m\otimes I_r)}\mathbf f,1\otimes v\rangle|
&\le\|\mathbf f\|\,
\|e^{-tC_m^*}1\otimes v\|\\
&=\|\mathbf f\|F_m(t).
\end{aligned}
$$

结合 (1.4)、(3.7)–(3.8)，且对大尺度使用
$e^{-20M_*}\le e^{-10M_*-14}\le F_m(t)$，得到

$$
|p_{m,v}(u)|\le
2\|\mathbf f\|e^{M_*h(u)+14}
\quad(1\le u\le20). \tag{3.10}
$$

若 $\mathbf f=0$ 已无事可证；否则应用 (1.5) 与 (1.6)，有

$$
\begin{aligned}
|\langle\mathbf f,1\otimes v\rangle|
&=|p_{m,v}(0)|\\
&\le2\|\mathbf f\|
\exp\left(14+n_mg_0+M_*\int h\,d\omega_0\right)\\
&\le2\|\mathbf f\|
\exp\left(14-\frac{13}{100}M_*+dg_0M_*^{3/4}\right)
\longrightarrow0.
\end{aligned}
$$

因此 $\langle\mathbf f,1\otimes v\rangle=0$。对全部坐标向量 $v$，可知 $\mathbf f$ 的每个分量均与 $1$ 正交。

算子 $S$ 与 $A\otimes I_r$ 交换，所以每个 $(A\otimes I_r)^n\mathbf f$ 也在 $\ker S$。重复上述结论，得到

$$
\langle A^nf_j,1\rangle=0
\quad(n\ge0,\ 1\le j\le r).
$$

$1$ 对 $A^*$ 循环，故全部 $f_j=0$。这证明 $S$ 单射。

### 3.4 转置矩阵给稠密值域

在 $H\otimes\mathbb C^r$ 上逐坐标施加共轭 $C$，记为 $C_r$。由 $L,A$ 的 $B$ 对称性及范数演算，

$$
C_rS^*C_r=L\otimes I_r-M(A)^T.
$$

转置矩阵函数 $M(z)^T$ 仍是解析芽，其常数项仍幂零。因此已经证明的单射部分适用于它，给

$$
\ker(C_rS^*C_r)=\{0\}.
$$

故 $\ker S^*=0$，即 $\overline{\operatorname{Ran}S}=H\otimes\mathbb C^r$。定理 3.1 得证。

## 4. 所需的局部解析因式分解：完整构造

为避免只以名称调用 Weierstrass 准备定理，下面证明所需的二维特例。

**引理 4.1。** 若解析芽 $G(z,w)$ 满足 $G(0,w)$ 不恒零，且它在 $w=0$ 的零点阶数为 $r\ge1$，则在原点附近有

$$
G(z,w)=U(z,w)
\left(w^r+\sum_{j=0}^{r-1}b_j(z)w^j\right), \tag{4.1}
$$

其中 $U,b_j$ 均解析，$U(0,0)\ne0$，且 $b_j(0)=0$。

**证明。** 取充分小的 $\rho>0$，使 $G(0,w)$ 在 $0<|w|\le\rho$ 没有零点。对充分小的 $|z|$，圆周 $|w|=\rho$ 上仍无零点，且 $G(z,w)$ 与 $G(0,w)$ 的差小于 $|G(0,w)|$。由辐角原理，或对这两个函数作连续非零边界同伦，$G(z,\cdot)$ 在圆内恰有 $r$ 个零点（按重数计）。

对 $1\le n\le r$ 定义

$$
s_n(z)=\frac{1}{2\pi i}\int_{|\xi|=\rho}
\xi^n\frac{\partial_wG(z,\xi)}{G(z,\xi)}\,d\xi.
$$

这些是 $z$ 的解析函数，并由留数等于上述 $r$ 个零点的 $n$ 次幂和。Newton 恒等式以 $s_1,\ldots,s_r$ 的多项式表达基本对称函数，故存在解析系数的首一多项式

$$
W(z,w)=w^r+\sum_{j<r}b_j(z)w^j,
$$

其根（含重数）恰为圆内这些零点。$z=0$ 时全部根为零，故 $W(0,w)=w^r$。

对 $|w|<\rho$ 令

$$
U(z,w)=\frac{1}{2\pi i}\int_{|\xi|=\rho}
\frac{G(z,\xi)}{W(z,\xi)(\xi-w)}\,d\xi.
$$

边界上 $W$ 无零点，所以这个式子关于 $(z,w)$ 联合解析。固定 $z$ 后，$G(z,\cdot)$ 与 $W(z,\cdot)$ 在圆内具有完全相同的零点及重数；一元可去奇点定理说明其商在圆内解析。Cauchy 公式因此给 $U(z,w)=G(z,w)/W(z,w)$，从而 (4.1) 成立。特别地

$$
U(0,0)=\lim_{w\to0}G(0,w)/w^r\ne0.
$$

缩小邻域后 $U$ 处处非零。证毕。

任意非零 $F\in\mathbb C\{z,w\}$ 都可先唯一取出最大的共同 $z$ 幂：

$$
F(z,w)=z^\nu G(z,w),\qquad G(0,w)\not\equiv0. \tag{4.2}
$$

具体地，写 $F=\sum_{p\ge0}z^pF_p(w)$，取首个非零 $F_p$ 的下标 $\nu$。这是有限整数；除去有限次 $z$ 因子保持局部解析性。若随后 $G(0,0)\ne0$，则 $G$ 已是单位；否则适用引理 4.1。

## 5. 每个非零解析芽的算子值都单射且稠密

**定理 5.1。** 对任意非零 $F\in\mathbb C\{z,w\}$，

$$
\boxed{
\ker F(A,L)=\{0\},\qquad
\overline{F(A,L)H}=H.
} \tag{5.1}
$$

因此解析芽演算 $\mathbb C\{z,w\}\to\mathcal A$ 不仅有定义，而且是单射代数同态。

**证明。** 使用 (4.2)。若 $G(0,0)\ne0$，则 $G(A,L)$ 由引理 2.1 可逆；$A^\nu$ 单射，所以 $F(A,L)$ 单射。

其余情形由引理 4.1 写

$$
F(z,w)=z^\nu U(z,w)P(z,w),
\quad
P(z,w)=w^r+\sum_{j=0}^{r-1}b_j(z)w^j,
\quad b_j(0)=0.
$$

$U(A,L)$ 可逆；故只需证明 $P(A,L)$ 单射。假设 $P(A,L)f=0$，并在 $H\otimes\mathbb C^r$ 中定义

$$
\mathbf f=(f,Lf,\ldots,L^{r-1}f)^T.
$$

取伴随矩阵（行列按 $0,\ldots,r-1$ 编号）

$$
M(z)=\begin{pmatrix}
0&1&0&\cdots&0\\
0&0&1&\cdots&0\\
\vdots&&\ddots&\ddots&\vdots\\
0&\cdots&0&0&1\\
-b_0(z)&-b_1(z)&\cdots&-b_{r-2}(z)&-b_{r-1}(z)
\end{pmatrix}.
$$

当 $r=1$ 时此矩阵只含条目 $-b_0(z)$。由于全部 $b_j(0)=0$，$M(0)$ 是幂零 Jordan 块。由 $P(A,L)f=0$，直接逐行验证

$$
(L\otimes I_r-M(A))\mathbf f=0.
$$

定理 3.1 给 $\mathbf f=0$，所以 $f=0$。这证明单射性。

又由引理 2.1，$F(A,L)\in\mathcal A$，故 R24 的双线性对称性给

$$
CF(A,L)^*C=F(A,L).
$$

其单射性等价于伴随单射，因此其值域稠密。

若非零解析芽的算子值为零，它会有整个非零 Hilbert 空间作为核，矛盾。因此演算同态单射。证毕。

## 6. 循环性、有限指数和及代数独立性

**推论 6.1。** 若 $h$ 对 $A$ 循环，$0\ne F\in\mathbb C\{z,w\}$，则 $F(A,L)h$ 非零且对 $A$ 循环。

**证明。** 令 $X=F(A,L)$。它单射、值域稠密并与 $A$ 交换，故

$$
\overline{\{p(A)Xh:p\in\mathbb C[z]\}}
=\overline{X\{p(A)h:p\in\mathbb C[z]\}}
=\overline{XH}=H.
$$

单射性同时保证 $Xh\ne0$。证毕。

**推论 6.2。** 若 $(\alpha_j,\beta_j)\in\mathbb C^2$ 两两不同，$c_j$ 不全为零，则

$$
\sum_{j=1}^s c_j e^{\alpha_jA+\beta_jL}h
$$

对每个循环 $h$ 都非零且循环。

**证明。** 解析芽

$$
F(z,w)=\sum_{j=1}^s c_j e^{\alpha_jz+\beta_jw}
$$

不恒零：选择 $\lambda$ 避开有限多个值，使全部 $\alpha_j+\lambda\beta_j$ 两两不同；在直线 $(z,w)=(t,\lambda t)$ 上，若 $F$ 恒零，则在 $t=0$ 的前 $s$ 个导数构成 Vandermonde 方程，迫使全部 $c_j=0$。矛盾。推论 6.1 即得结论。证毕。

同理，若 $\beta_1,\ldots,\beta_s$ 两两不同，$a_j(z)$ 是不全为零的一元解析芽，则

$$
\sum_{j=1}^s a_j(A)e^{\beta_jL}h
$$

非零且循环：对每个固定的小 $z$ 使用一元指数函数的 Vandermonde 独立性，可知 $\sum a_j(z)e^{\beta_jw}$ 不恒零。

定理 5.1 还直接给出：$A,L$ 在收敛解析芽意义下没有非零关系。特别地，它们代数独立；对固定循环 $h$，全部有限单项式向量 $A^pL^qh$ 线性独立。这里的“代数独立”不否认 $L$ 是 $A$ 的多项式的**范数极限**；有限多项式关系、收敛解析芽关系和任意范数极限是三个不同条件。

## 7. 严格范围：解析芽像是稠密第一纲真子代数

记

$$
\mathcal G=\{F(A,L):F\in\mathbb C\{z,w\}\}\subset\mathcal A.
$$

**命题 7.1。** $\mathcal G$ 在 $\mathcal A$ 中稠密，却是第一纲的真子集。

**证明。** 它包含全部 $A$ 的多项式，故在 $\mathcal A$ 中稠密。

对整数 $q,N\ge1$，令

$$
K_{q,N}=
\left\{\sum_{p,n\ge0}c_{pn}A^pL^n:
|c_{pn}|\le Nq^{p+n}\right\}.
$$

上述系数界保证该级数定义一个解析芽，故 $K_{q,N}\subset\mathcal G$。反之，每个解析芽由双圆盘上的 Cauchy 系数估计属于某个这样的集合，所以

$$
\mathcal G=\bigcup_{q,N\ge1}K_{q,N}. \tag{7.1}
$$

每个 $K_{q,N}$ 在算子范数下紧。确实，固定 $\epsilon=1/(2q)$；由拟幂零性，有常数 $C_A,C_L$ 使

$$
\|A^pL^n\|\le C_AC_L(2q)^{-(p+n)}.
$$

故所有允许系数级数的尾部都一致受可和级数
$NC_AC_L\sum_{p,n}2^{-(p+n)}$ 控制。对任意一列允许系数，用对角子列令每个系数在其紧圆盘内收敛；统一尾界把逐项收敛提升为算子范数收敛，极限仍在 $K_{q,N}$。这证明紧性。

$\mathcal A$ 是无穷维 Banach 空间：$A$ 的幂线性独立，因为一个非零多项式可写成 $z^\nu u(z)$、$u(0)\ne0$；则 $A^\nu u(A)$ 单射且非零。无穷维 Banach 空间中的紧子集没有内点，因此每个 $K_{q,N}$ 都无处稠密。Baire 定理与 (7.1) 给 $\mathcal G$ 第一纲且不能等于 $\mathcal A$。证毕。

因此本条确实覆盖一个大的显式解析族，但不能通过“这些元素在 $\mathcal A$ 中稠密”把单射性传给任意范数极限。对一般 $X\in\mathcal A$，缺少的仍是不同于本条有限解析变量控制的新性质。

## 8. 无零因子的正确使用：一个仍未证明的足够分母性质

这部分只陈述逻辑边界与充分条件，不将条件登记为本模型的已证事实。

R32 证明 $\mathcal A$ 没有零因子；它直接给出的只是

$$
\ker X\cap\mathcal A1=\{0\}
\quad(0\ne X\in\mathcal A).
$$

因为若 $XY1=0$，则 $XY$ 与 $A$ 交换并杀死循环向量 $1$，所以 $XY=0$；进而 $Y=0$。不能仅由 $\mathcal A1$ 稠密就得到 $\ker X=0$。

一个真正足够的新性质为：对每个 $f\in H$，存在已知单射的 $Y\in\mathcal A$ 及 $Z\in\mathcal A$，使

$$
Yf=Z1. \tag{8.1}
$$

若本模型满足它，则任意 $0\ne X\in\mathcal A$ 都单射。证明是：$Xf=0$ 蕴含 $XZ1=XYf=0$，循环性给 $XZ=0$，无零因子给 $Z=0$，再由 $Y$ 单射给 $f=0$。本条定理增加了大量可用的单射分母 $Y=F(A,L)$，却**没有**证明每个 $f$ 都有 (8.1) 的表示。

R34 已证明一般向量对应的模映射 $p(A)1\mapsto p(A)f$ 可闭；这并不自动给出 (8.1)，不保证有预解点，也不保证一个有界预解算子落入 $\mathcal A$。R38 甚至给出完整交换子严格大于 $\mathcal A$ 的实际见证。因此可闭性、代数无零因子和双线性对称性各自都不能省去这个表示问题。

本条止于定理 5.1 的无条件新范围，以及 (8.1) 的明确充分性；任意有限 R16 产品和、任意 $X\in\mathcal A$、任意非零 $f\in H$ 的循环性仍未由此得到。

## 9. 对 R61 全部复幂次渐近尾的同一矩阵结论

**定理 9.1。** 把本条的 $L$ 换成 R61 定义的任意临界对数：底参数 $s_j,t_j$ 有界，差满足
$$
s_j-t_j\sim c(j+2)^{-p},\qquad c\ne0,\quad1<p\le12/5,
$$
并允许 R61 中明确的标量解析单位前因子。则定理 3.1、定理 5.1 以及第 6–7 节的全部结论仍成立。

**证明。** R61 给 $A_k$ 的无常数项多项式 $G_k$，使
$$
\left\|L-G_k-\sum_{j\ge k}\delta_jE_j\right\|
\le C_0\eta_{k-1},\qquad \sup_k\|G_k\|<\infty.
$$
对给定解析矩阵 $M(z)$，本条引理 2.2 不变。因此在 $M(0)^d=0$ 时，真实头部
$$
R_k=G_k I_r-M(A_k)
$$
仍满足 $R_k^{d2^k}=0$。添加 $k\le j<m$ 的中间位后，指数多项式的次数至多 $m+d2^k-k-1$，实际算子误差仍为 $O(\eta_{k-1})$。

令 $M_*=m+2$、$k=\lfloor(3/4)\log_2M_*\rfloor$，并取 R61 的复时间 $\tau=M_*^p u/c$。对给定 $p$ 选择其已认证区间 $[a,b]$：$p\le2$ 时为 $[1,20]$，$p>2$ 时为 $[1/10,30]$。Duhamel 误差的范数仍受
$$
C|\tau|e^{B|\tau|}\eta_{k-1}
\le\exp\{-3M_*^3+O(M_*^p+\log M_*)\}
$$
控制；因为 $p\le12/5<3$，这比 $e^{-C_1M_*}$ 更小。R61 的复尾范数正是
$$
\|e^{-\overline\tau C_m^*}1\|
=\exp\{M_*h_p(u)+o(M_*)\},
$$
误差对所选区间一致。把 $1$ 换成 $1\otimes v$ 不改变这个范数。故第 3 节的标量多项式界变成
$$
|p_{m,v}(u)|\le2\|\mathbf f\|
\exp\{M_*h_p(u)+o(M_*)\}.
$$
应用对应区间的同一外域估计，常数项不超过
$$
2\|\mathbf f\|\exp\left\{
-\frac1{2000}M_*+dg_{a,b}M_*^{3/4}+o(M_*)\right\}\longrightarrow0.
$$
随后由 $A^*$ 的循环向量排除矩阵核；逐坐标共轭与转置仍给稠密值域。第 4–7 节仅需这些矩阵结论、$L\in\mathcal A$ 及 $r(L)=0$，三者现都成立，因而逐字适用。证毕。
