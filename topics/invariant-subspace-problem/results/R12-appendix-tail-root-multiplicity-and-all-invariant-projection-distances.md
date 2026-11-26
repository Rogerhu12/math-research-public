# 原尾有界根的重数整除与全部普通不变投影的有限头距离

作者：AI-assisted GPT-6 Astra Pro；会话 `Astra-ISP-8542378f-20261127`。日期：2026-11-27（Asia/Taipei）。

**状态：已证明的原算子结构结论。** 本文直接约束任意未知的普通闭 $A$-不变子空间，不要求它受 Deddens 代数保持。对每个原尾 $B_m$，有限重数放大 $I_k\otimes B_m$ 有有界 $q$ 次根，当且仅当 $q$ 整除 $k$。由此，任意 $A$-不变空间不可能通过一个真有限头坐标投影与该坐标的**整个尾空间**有界同构；所有实际不变投影与每个真有限头投影的范数距离都是一。非零真不变投影到原 UHF 代数的距离准确为 $1/2$。

本稿没有把普通不变空间限制为某种图，也没有证明一般不变空间不存在。已有 [R7](R7-weak-projection-support-and-graph-criterion.md) 是一般条件性图判据；[R170](R170-locally-finite-tail-splitting-no-uhf-regularization.md) 的特定核不属于 UHF 结论，也不同于这里针对全部普通不变空间的精确距离。

## 1. 原尾与结论

仍取原 Haar 空间 $K=L^2(\mathbb Z_2,\mu)$，并令
$$
(B_mf)(z)=w_m(z)f(z-1),\qquad
w_m(z)=\alpha_{m+v_2(z)}\quad(z\ne0),\qquad w_m(0)=0,
\tag{1.1}
$$
其中 $m\ge0$、$B_0=A$，原权为
$$
\alpha_j=e^{-L_j},\qquad
L_j=\frac{280}{3}16^j-90\,8^j+300\,2^j-\frac{850}{3}.
\tag{1.2}
$$
每个 $B_m$ 都是原模型的实际尾，不是另换权序列。它非零且拟幂零。记
$$
\beta^{(m)}_n=\|B_m^n\|
=\prod_{a=1}^n\alpha_{m+v_2(a)},\qquad \beta^{(m)}_0=1.
\tag{1.3}
$$
区间同余类计数与原 $A$ 完全相同，证明 (1.3)。特别，沿任意 $n$，至少有 $\lfloor n/2^j\rfloor$ 个因子不超过 $\alpha_{m+j}$，所以
$$
\limsup_{n\to\infty}\|B_m^n\|^{1/n}
\le \alpha_{m+j}^{\,2^{-j}}\alpha_m^{\,1-2^{-j}}
\quad(j\ge0).
$$
由 $2^{-j}L_{m+j}\to\infty$，右端在 $j\to\infty$ 时趋零。这也直接付清每个尾的拟幂零性。

**定理 A：准确有界根重数。** 对每个 $m\ge0$、整数 $k\ge1$、$q\ge2$ 及 $\lambda\ne0$，
$$
\boxed{
\exists X\in B(K^{\oplus k}),\quad
X^q=\lambda(I_k\otimes B_m)
\quad\Longleftrightarrow\quad q\mid k.
}
\tag{1.4}
$$
根不预设是加权复合算子、UHF 元素或多项式极限。

**定理 B：完整尾上的图与精确距离。** 取 $N=2^m$、$m\ge1$，并采用原酉分解
$$
H=\mathbb C^N\otimes K,\qquad
A^N=\beta^{(0)}_{N-1}I_N\otimes B_m.
\tag{1.5}
$$
设 $Q=Q_0\otimes I_K$，其中 $Q_0$ 是秩 $k$ 的正交投影且 $0<k<N$。对每个闭 $A$-不变空间 $M$，映射
$$
Q|_M:M\longrightarrow QH
\tag{1.6}
$$
不可能是有界同构到**整个** $QH$。因此
$$
\boxed{\|P_M-Q\|=1.}
\tag{1.7}
$$
这里允许任意有限头投影，绝不只限物理对角投影。

记原具体 UHF 代数为
$$
\mathfrak U=\overline{\bigcup_{m\ge1}
\big(M_{2^m}(\mathbb C)\otimes I_K\big)}^{\|\cdot\|}.
$$
若 $\{0\}\ne M\ne H$，则
$$
\boxed{\operatorname{dist}(P_M,\mathfrak U)=\frac12.}
\tag{1.8}
$$

## 2. 每个实际尾的完整交换子确实交换

为了后面合法使用字符，先把原[收缩多项式逼近](R12-appendix-contractive-polynomial-density-of-full-haar-commutant.md)逐尾支付。令
$$
\mathscr C_m=\{B_m\}'\subset B(K).
$$
它是含单位的范数闭代数。本节证明它交换；不能仅凭 $B_m$ 是一个算子就假定其完整交换子交换。

固定 $m$，再将尾分成低 $\ell$ 位与其后真尾。置 $D=2^\ell$，令 $J_{m,\ell}$ 为低头加权 nilpotent 链：
$$
J_{m,\ell}e_s=\alpha_{m+v_2(s+1)}e_{s+1}\quad(0\le s<D-1),
\qquad J_{m,\ell}e_{D-1}=0.
$$
原进位身份为
$$
B_m=J_{m,\ell}\otimes I+e_{0,D-1}\otimes B_{m+\ell},
\qquad
\|B_m-J_{m,\ell}\otimes I\|=\alpha_{m+\ell}.
\tag{2.1}
$$

将 $Y\in\mathscr C_m$ 写作真尾块 $Y_{rs}$。由
$YB_m^s(e_0\otimes h)=B_m^sY(e_0\otimes h)$ 得
$$
Y_{rs}=
\frac{\beta^{(m)}_r}
{\beta^{(m)}_s\beta^{(m)}_{r-s}}Y_{r-s,0}
\quad(r\ge s),
\tag{2.2}
$$
$$
Y_{rs}=
\frac{\beta^{(m)}_r\beta^{(m)}_{D-1}}
{\beta^{(m)}_s\beta^{(m)}_{D+r-s}}
B_{m+\ell}Y_{D+r-s,0}
\quad(r<s).
\tag{2.3}
$$
因此上三角块满足
$$
\|Y_{rs}\|\le
\frac{\alpha_{m+\ell}}{\beta^{(m)}_{D-1}}\|Y\|
\quad(r<s).
\tag{2.4}
$$

令 $\mathcal T_\ell(Y)$ 是把 $Y$ 压到低 $\ell$ 位柱空间后，再提升为尾恒等的有限头算子。压缩收缩，故
$$
\|\mathcal T_\ell(Y)\|\le\|Y\|,
\qquad \mathcal T_\ell(Y)\longrightarrow Y\quad\mathrm{SOT}.
\tag{2.5}
$$
第二式先在有限柱向量上成为原柱空间正交投影的强逼近，再用统一范数界推广；不需要 $Y$ 交换。

置
$$
y_d=\langle Y_{d0}\mathbf1,\mathbf1\rangle,\qquad
p_\ell(z)=\sum_{d=0}^{D-1}\frac{y_d}{\beta^{(m)}_d}z^d.
$$
由 (2.2)，$p_\ell(J_{m,\ell})$ 正是压缩矩阵的全部下三角部分。由 (2.4) 与幂的 telescoping，
$$
\|p_\ell(B_m)-\mathcal T_\ell(Y)\|
\le
\frac{\alpha_{m+\ell}}{\beta^{(m)}_{D-1}}
\left(D+\frac1{(1-\alpha_m)^2}\right)\|Y\|.
\tag{2.6}
$$
这里保留了完整原低头条件数，不能只用 $\alpha_{m+\ell}\to0$。

确切地，原显式权给 $20\,16^j\le L_j\le100\,16^j$，而
$$
-\log\beta^{(m)}_{D-1}
=\sum_{r=0}^{\ell-1}2^{\ell-r-1}L_{m+r}
\le\frac{100}{14}16^m(16^\ell-2^\ell).
$$
所以
$$
\frac{\alpha_{m+\ell}}{\beta^{(m)}_{D-1}}
\le \exp\!\left[-\frac{90}{7}16^{m+\ell}\right].
\tag{2.7}
$$
于是 (2.6) 右端趋零。结合 (2.5)，每个 $Y\in\mathscr C_m$ 都是 $B_m$ 的一致有界多项式的强极限。

若 $Z\in\mathscr C_m$，则 $Zp_\ell(B_m)=p_\ell(B_m)Z$。对每个固定输入取强极限，得到 $ZY=YZ$。因此
$$
\boxed{\mathscr C_m\text{ 是含单位的交换 Banach 代数，对每个 }m\ge0.}
\tag{2.8}
$$

## 3. 字符压缩与等长 Jordan 块

每个非零含单位的交换复 Banach 代数有一个非零连续乘法泛函。可取一个极大理想：它必闭，否则其闭包含单位的邻域，从而原理想含可逆元；商是复 Banach 除环，由 Gelfand--Mazur 定理为 $\mathbb C$。该字符 $\chi$ 满足 $\chi(I)=1$、$|\chi(T)|\le\|T\|$。

对 $\mathscr C_{m+1}$ 的任意这样的字符，拟幂零性明确给
$$
|\chi(B_{m+1})|
\le \|B_{m+1}^r\|^{1/r}\longrightarrow0,
\qquad
\boxed{\chi(B_{m+1})=0.}
\tag{3.1}
$$
没有把字符认作正常态、点取值或 Haar 积分。

现在假设 $X^q=\lambda(I_k\otimes B_m)$。因 $X$ 与其幂交换且 $\lambda\ne0$，
$$
X(I_k\otimes B_m)=(I_k\otimes B_m)X.
$$
所以 $X$ 的 $k\times k$ 块都属于 $\mathscr C_m$。

再将每个 $B_m$ 分成第一位与其后尾：
$$
B_m=
\begin{pmatrix}
0&B_{m+1}\\
\alpha_mI&0
\end{pmatrix},
\qquad B_m^2=\alpha_m I_2\otimes B_{m+1}.
\tag{3.2}
$$
每个 $\mathscr C_m$ 元素与 (3.2) 的平方交换，故其 $2\times2$ 块均属于 $\mathscr C_{m+1}$。于是 $X$ 可看成 $\mathscr C_{m+1}$ 上的 $2k\times2k$ 矩阵。对每个块施加同一个 $\chi$ 是真正的矩阵代数同态。记所得复矩阵为 $Z$，由 (3.1)--(3.2)，
$$
\boxed{Z^q=I_k\otimes
\begin{pmatrix}0&0\\\lambda\alpha_m&0\end{pmatrix}.}
\tag{3.3}
$$
右端是 $k$ 个非零的长度二 Jordan 块，秩恰为 $k$；没有任何长度一剩余块。

为完整核对根的重数限制，(3.3) 给 $Z^{2q}=0$，所以 $Z$ 的 nilpotent Jordan 块长度 $s_i$ 均在 $[1,2q]$ 中。又
$$
\sum_i s_i=2k,\qquad
\sum_i\max(s_i-q,0)=\operatorname{rank}Z^q=k.
$$
对 $1\le s\le2q$，
$$
\max(s-q,0)\le s/2,
$$
且等号当且仅当 $s=2q$。上述两个和达到等号，所以每个 $s_i=2q$。因此 $2q$ 整除 $2k$，即
$$
q\mid k.
\tag{3.4}
$$

反过来，若 $k=q d$，在 $K^{\oplus q}$ 上定义有界 companion
$$
C_q(B_m)(x_0,\ldots,x_{q-1})
=(B_mx_{q-1},x_0,\ldots,x_{q-2}).
$$
直接逐坐标计算得 $C_q(B_m)^q=I_q\otimes B_m$。取 $d$ 个直和，再乘以任意 $\lambda^{1/q}$，即得 (1.4) 所需根。定理 A 得证。

## 4. 任意普通不变空间的完整有限头图均不可能

取定理 B 的 $M,Q$。反设 $L=Q|_M$ 为从 $M$ 到整个 $QH$ 的有界同构，令 $V=L^{-1}$。这是满射到整个 $k$ 重尾空间的假设；仅有 $L$ 有下界并不够。

因为 $A(M)\subseteq M$，可以在 $QH$ 上定义实际有界算子
$$
T=L(A|_M)V.
$$
相似的幂与原 (1.5) 给
$$
\begin{aligned}
T^N
&=L(A^N|_M)V\\
&=Q\,\beta^{(0)}_{N-1}(I_N\otimes B_m)V\\
&=\beta^{(0)}_{N-1}(I_N\otimes B_m)QV\\
&=\beta^{(0)}_{N-1}(I_k\otimes B_m)
\quad\text{在 }QH\simeq K^{\oplus k}\text{ 上}.
\end{aligned}
\tag{4.1}
$$
第三行合法，因为 $Q$ 是纯有限头投影；第四行使用 $QV=I_{QH}$。定理 A 强迫 $N\mid k$，与 $0<k<N$ 矛盾。这证明 (1.6)。

为了由此得到精确距离，反设 $\delta=\|P_M-Q\|<1$。若 $x\in M$，
$$
\|(I-Q)x\|\le\delta\|x\|,\qquad
\|Qx\|\ge\sqrt{1-\delta^2}\|x\|,
$$
故 $Q|_M$ 单射且有下界。满射也必须单独证明：在 $QH$ 上，
$$
\|QP_MQ-I_{QH}\|\le\delta<1,
$$
所以 $QP_MQ$ 可逆。给定 $y\in QH$，取
$$
x=P_M(QP_MQ|_{QH})^{-1}y\in M,
$$
即有 $Qx=y$。所以 $Q|_M$ 的确是到整个 $QH$ 的有界同构，与 (1.6) 矛盾。

任意两个正交投影的距离至多一，故 (1.7) 成立。此论证对 $M=0,H$ 也给同一距离，但下一节的 UHF 距离要求 $M$ 非零且真。

## 5. 到整个原 UHF 代数的准确距离

设 $\{0\}\ne M\ne H$，记 $P=P_M$。因 $(1/2)I\in\mathfrak U$，
$$
\operatorname{dist}(P,\mathfrak U)\le\|P-\tfrac12I\|=\tfrac12.
\tag{5.1}
$$

反设存在 $Y\in\mathfrak U$ 使 $\|P-Y\|=\delta<1/2$。取自伴部分 $Y_0=(Y+Y^*)/2$，仍有 $\|P-Y_0\|\le\delta$。自伴谱扰动给
$$
\sigma(Y_0)\subset[-\delta,\delta]\cup[1-\delta,1+\delta].
$$
在这个分离谱上截取高支，得到
$$
Q=\mathbf1_{(1/2,\infty)}(Y_0)\in\mathfrak U.
$$
该指标函数在 $\sigma(Y_0)$ 上连续，故这里是合法的连续函数演算。逐谱点有 $\|Y_0-Q\|\le\delta$，于是
$$
\|P-Q\|\le2\delta<1.
\tag{5.2}
$$
$P$ 非零且真，迫使 $Q\ne0,I$。

每个 UHF 投影 $Q$ 可由真有限头投影范数逼近。确切地，取有限头自伴 $Y_j\to Q$，当误差小于 $1/2$ 时按同样的谱切分取
$Q_j=\mathbf1_{(1/2,\infty)}(Y_j)$。它们属于相同有限头矩阵代数，且
$$
\|Q_j-Q\|\le2\|Y_j-Q\|\longrightarrow0.
$$
充分大时 $Q_j\ne0,I$，并由 (5.2) 得 $\|P-Q_j\|<1$，违反 (1.7)。因此 (5.1) 的下界也是 $1/2$，证明 (1.8)。

此外，[R164](R164-invariant-projections-high-bit-essential-rigidity.md) 已证明，包含 $\mathfrak U$ 和所有实际 $P_M$ 的 $C^*$ 代数在 Calkin 商下完全等距。因此本稿同样有
$$
\|P_M-Q\|_{\rm ess}=1,\qquad
\operatorname{dist}(P_M,\mathfrak U+\mathcal K(H))=\frac12
\quad(0<M<H).
\tag{5.3}
$$
第二式的下界是
$\|P_M-Y-K\|\ge\|P_M-Y\|_{\rm ess}
=\|P_M-Y\|\ge1/2$；上界仍用 $(1/2)I$。它不把紧扰动当成可忽略的普通不变性误差。

## 6. 对后续原空间工作的含义

本稿已经使用了真正的 $A$ 不变性，完整尾上的根确由同一个未知 $M$ 的限制构造。它排除以有限头自由尾为底空间的任何有界图修正，包括离一个真有限头投影任意小的范数修正；这里无需控制 Deddens 成本。

仍可能存在的普通不变空间，其有限头坐标必须至少有核、未满的像或无界逆，不能先用一个有限头坐标将它等同于完整原尾。本文没有将这种必要退化变成矛盾，也没有排除以未知真尾不变空间为底空间的闭图。后者没有定理 A 中的整重数目标，必须保留实际底空间与域。
