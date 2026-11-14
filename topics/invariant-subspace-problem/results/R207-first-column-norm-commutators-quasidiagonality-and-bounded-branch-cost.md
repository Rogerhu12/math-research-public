# R207：实际一阶的有限头范数交换子、共同准对角序列与有界分支的延拓成本

日期：2026-11-12（UTC）。作者：critical_kernel。

状态：完整实际接口与有界分支必要条件；不排除一般慢平方核。已对 R125、R161、R172 正文作查重：它们分别给有限柱图核心、与 $N_j$ 的交换子、固定正则器幂图核心；本稿补出同一个条件期望序列的明确范数交换子及分支成本估计。

## 1. 记号和主结论

记 $\mathsf P_m$ 为前 $m$ 个物理位的条件期望，即到有限柱空间
$$
\mathcal F_m
=H_{[0,m)}\otimes\mathbb C\Omega_{\ge m}
$$
的正交投影，$\operatorname{rank}\mathsf P_m=2^m$。
这不是某个未知不变子空间的投影。

取任意复 $\ell^2$ 一阶
$$
X=a_*I+\sum_{j\ge0}a_jV_j,\qquad
V_j=(I-N_j)(I+N_j)^{-1},
$$
其中 $X$ 按 R125 的真实闭实现理解。置
$$
g=\|a\|_2,\qquad g_m=\|a_{\ge m}\|_2.
$$

**定理1.1。** 对 $m\ge1$，$[X,\mathsf P_m]$ 在
$\operatorname{Dom}X$ 上延为有界有限秩算子，并且
$$
\boxed{\|[X,\mathsf P_m]\|\le\varepsilon_m:=g_m+2\delta_m\longrightarrow0,}
\tag{1.1}
$$
其中可取
$$
\delta_m=
18\alpha_m\sum_{j<m}\frac{|a_j|}{\alpha_j}
+8\sum_{j\ge m}|a_j|\eta_j.
\tag{1.2}
$$
相同的界适用于 $[X^*,\mathsf P_m]$。
因此对每个 $h\in\operatorname{Dom}X$，
$$
\mathsf P_mh\to h,\qquad X\mathsf P_mh\to Xh.
\tag{1.3}
$$
这是真实向量的有限头图逼近，不是截断系数算子
$\sum_{j<m}a_jV_j$ 在任意域向量上的收敛。

**定理1.2。** 若 $\lambda\in\rho(X)$，则有界逆
$L_\lambda=(X-\lambda I)^{-1}$ 满足
$$
\boxed{
[L_\lambda,\mathsf P_m]
=-L_\lambda[X,\mathsf P_m]L_\lambda,\qquad
\|[L_\lambda,\mathsf P_m]\|
\le\|L_\lambda\|^2\varepsilon_m.
}
\tag{1.4}
$$
特别，所有非负不可和 $\ell^2$ 一阶的正逆，以及由有限个这类逆与 UHF 元素
生成的 $C^*$ 代数，都对同一有限秩序列 $\mathsf P_m$ 准对角。

**定理1.3（有界分支成本）。**
设 $0\ne M$ 为闭 $A$ 不变子空间，
$$
M\subseteq\operatorname{Dom}X,\qquad X_M=X|_M\in B(M).
$$
置 $s_m=a_*+\sum_{j<m}a_j$。
若 $s_m$ 最终位于 $\rho(X_M)$，记
$R_m=\|(X_M-s_mI)^{-1}\|$。
则对单位物理全零头向量
$$
e_{0,m}=e_0^{\otimes m}\otimes\Omega_{\ge m}
$$
及每个固定整数 $p\ge1$，有第6节明确给出的界
$$
\boxed{\|P_Me_{0,m}\|\le R_m^p E_{m,p}.}
\tag{1.5}
$$
其中
$$
E_{m,p}=C_pg_m^p+
h_m\sum_{k=1}^p\binom pk
L_m^{\,k-1}C_{p-k}g_m^{p-k},
\tag{1.6}
$$
$$
L_m=6\sum_{j<m}|a_j|,\qquad
h_m=6\alpha_m\sum_{j<m}\frac{|a_j|}{\alpha_j},
\qquad C_0=1.
\tag{1.7}
$$
常数 $C_p$ 为 R181 的真实中心幂常数，独立于 $m$。
若 $R_m$ 一致有界，(1.5) 给系数尾的全部固定幂小量。
对典型交替幂尾，它迫使有限头到 $M$ 的任何右逆范数快于全部多项式增长。

## 2. 纯跨真空块交换子的准确范数

在 Walsh 基上写
$$
S_j=I-2E_j=c_j-c_j^*+2n_j,
$$
其中 $c_j,c_j^*,n_j$ 分别为单坐标创建、删除、占据算子。
令 $X^0$ 为对应纯闭一阶，则
$$
X=X^0+K,\qquad
K=\sum_j a_j(V_j-S_j)\in\mathfrak U.
\tag{2.1}
$$

低于 $m$ 的全部纯项与 $\mathsf P_m$ 交换；
高于等于 $m$ 的占据对角项也与它交换。
在尾空间分解
$$
H_{\ge m}=\mathbb C\Omega_{\ge m}\oplus\Omega_{\ge m}^\perp
$$
上，剩余交换子只有两个跨块：
$$
[X^0,\mathsf P_m]
=I_{[0,m)}\otimes
\begin{pmatrix}0&\ell_a\\v_a&0\end{pmatrix},
\tag{2.2}
$$
其中
$$
v_a=\sum_{j\ge m}a_j\chi_j,\qquad
\ell_a(z)=\sum_{j\ge m}a_j\widehat z(\{j\}).
$$
这里 $\ell_a$ 在整个真空正交补上作用，只读取第一次数部分。
两者范数都等于 $g_m$。
两个输入块及两个输出块分别正交，所以
$$
\boxed{\|[X^0,\mathsf P_m]\|=g_m.}
\tag{2.3}
$$
对复系数，上下两个块不必互为伴随；其相同范数仍使 (2.3) 成立。

(2.2) 先在有限柱上逐项计算，随后按 $\ell^2$ 收敛定义右侧有界算子。
它的秩至多为 $2^{m+1}$，因此不涉及任何无界创建和的全域运算。

## 3. 实际进位的有限头预算

对 $j<m$，用边界 $N_m^{[m]}=0$ 递归定义真实有限链截断
$$
N_j^{[m]}=E_j+\eta_jE_j^*N_{j+1}^{[m]}.
$$
它只作用于位 $[j,m)$。
实际进位式逐步相减给
$$
N_j-N_j^{[m]}
=\frac{\alpha_m}{\alpha_j}
E_j^*E_{j+1}^*\cdots E_{m-1}^*N_m.
\tag{3.1}
$$
所以差的范数不超过 $\alpha_m/\alpha_j$。

这些有限链是实际归一化幂的有限头矩阵，范数至多1，
且其平方范数不超过 $\eta_j$。
由 $\eta_*=\sup_j\eta_j<1/4$，
$$
\|(I+N_j^{[m]})^{-1}\|<3.
$$
令
$$
V_j^{[m]}=(I-N_j^{[m]})(I+N_j^{[m]})^{-1}.
$$
利用 $V(N)=2(I+N)^{-1}-I$ 的准确逆差公式，
$$
\boxed{\|V_j-V_j^{[m]}\|\le18\,\alpha_m/\alpha_j.}
\tag{3.2}
$$

定义只作用前 $m$ 位的有界算子
$$
K^{[m]}=\sum_{j<m}a_j(V_j^{[m]}-S_j).
$$
它与 $\mathsf P_m$ 严格交换。
R125 的 $\|V_j-S_j\|\le8\eta_j$ 及 (3.2) 给
$$
\|K-K^{[m]}\|\le\delta_m
$$
其中 $\delta_m$ 正是 (1.2)。
因而
$$
\|[K,\mathsf P_m]\|\le2\delta_m.
\tag{3.3}
$$

还可写一个不带 $\sqrt m$ 损失的简单上界。因为
$$
\frac{\alpha_m}{\alpha_j}
\le\eta_{m-1}\eta_*^{\,m-1-j},
$$
Cauchy–Schwarz 给
$$
\alpha_m\sum_{j<m}\frac{|a_j|}{\alpha_j}
\le\frac{g\,\eta_{m-1}}{\sqrt{1-\eta_*^2}}.
$$
因此
$$
\delta_m\le
\frac{18g\,\eta_{m-1}}{\sqrt{1-\eta_*^2}}
+8g_m\|\eta_{\ge m}\|_2\longrightarrow0.
\tag{3.4}
$$
这里用的都是实际有限链差，不把任意 UHF 逼近误差当作已知尾率。

## 4. 真实域、逆及共同准对角代数

在有限柱上合并 (2.2) 与 (3.3)，得到
$$
X\mathsf P_mh=\mathsf P_mXh+B_mh,\qquad
\|B_m\|\le\varepsilon_m.
\tag{4.1}
$$
$\mathsf P_mH$ 是有限维有限柱空间，包含于 $\operatorname{Dom}X$，
所以 $X\mathsf P_m$ 为全域有界有限秩算子。
取 R125 的有限柱图核心逼近任意 $h\in\operatorname{Dom}X$，
(4.1) 的两端都可取极限，故它在完整真实域成立。
另一个有限秩项 $\mathsf P_mX$ 的有界延拓是
$(X^*\mathsf P_m)^*$，所以 $B_m$ 也为有限秩。
通常伴随公式给
$$
[X^*,\mathsf P_m]=-B_m^*
\quad\text{于 }\operatorname{Dom}X^*.
$$
这证明 (1.1)；再用 $\mathsf P_m\to I$ 强和 $\varepsilon_m\to0$
得到 (1.3)。

若 $L_\lambda=(X-\lambda I)^{-1}$ 有界，$\mathsf P_m$ 保持真实域，
故在 $L_\lambda H=\operatorname{Dom}X$ 上作标准逆交换子计算，
得到完整全域恒等式 (1.4)。
所有乘积中的无界项都先在其实际域内取消。

定义
$$
\mathfrak Q_{\mathsf P}
=\{T\in B(H):\|[T,\mathsf P_m]\|\to0\}.
$$
这是范数闭、含单位的 $C^*$ 代数。
每个有限头物理算子与充分大的 $\mathsf P_m$ 严格交换，
所以 $\mathfrak U\subseteq\mathfrak Q_{\mathsf P}$。
(1.4) 把每个存在的真实第一阶有界预解放入这个代数。

特别，对任意非负 $a\in\ell^2\setminus\ell^1$，
$L=(I+X_a)^{-1}$ 满足 (1.4)；
有限个这样的正逆、UHF 元素及其伴随、范数闭包，都使用同一序列。
这与 R204 的范数不可分正逆族相容；
共同准对角不意味着该代数范数可分。

这里没有推出任意未知不变投影 $P_M$ 属于 $\mathfrak Q_{\mathsf P}$。
强高位渐近交换代数 $\mathfrak E$ 与本稿范数条件是不同接口。

## 5. 有界分支的统一有限列残差

设 $M$ 满足定理1.3。
即使没有给一个全空间有界实现 $Y$，(4.1) 也给
$$
\boxed{
\|X\mathsf P_m|_M-\mathsf P_mX_M\|
\le\varepsilon_m.
}
\tag{5.1}
$$
两边是从 $M$ 到全空间的有界算子。
它不是 $M$ 内部的压缩等式，因为 $\mathsf P_m$ 不必保持 $M$。

若进一步 $X_M=Y|_M$，其中 $Y\in\mathcal A\subseteq\mathfrak U$，
则
$$
\boxed{
\|(X-Y)\mathsf P_m|_M\|
\le\varepsilon_m+\|[Y,\mathsf P_m]\|\longrightarrow0.
}
\tag{5.2}
$$
这是全部单位核向量共享的有限列近核误差，
不需要假设这些向量具有统一的 Hilbert 尾收敛率。

另一方面，若 $M\ne0$，则
$$
\mathsf P_mM=\mathcal F_m.
\tag{5.3}
$$
证明：若有限柱 $v\in\mathcal F_m$ 正交于 $\mathsf P_mM$，
则 $v\perp M$。
$M^\perp$ 对 $A^*$ 不变，而每个非零有限柱对 $A^*$ 循环，
所以这样的 $v$ 只能为0。有限维像遂为整个 $\mathcal F_m$。

(5.3) 只保证每个固定 $m$ 存在有界右逆
$J_m:\mathcal F_m\to M$。
它不保证这些右逆的范数一致；下面给一个真正来自分支方程的增长下界。

## 6. 全零物理头的全部中心幂估计

令
$$
e_{1,m}=e_1^{\otimes m}\otimes\Omega_{\ge m},\qquad
s_m=a_*+\sum_{j<m}a_j.
$$
分解
$$
X-s_mI=H_m+Z_m,\qquad
H_m=\sum_{j<m}a_j(V_j-I),\qquad
Z_m=\sum_{j\ge m}a_jV_j.
\tag{6.1}
$$
$H_m$ 有界，并与真实尾 $Z_m$ 在全部自然幂域上交换。
实际高位尾作用保持低头不变。

设 $\Pi_{1,m}$ 为物理全1头柱投影。
由实际进位递推，
$$
\|N_j\Pi_{1,m}\|\le\alpha_m/\alpha_j,\qquad j<m.
$$
有界逆与 $N_j$ 交换，所以
$$
\|(V_j-I)\Pi_{1,m}\|\le6\alpha_m/\alpha_j.
$$
因此
$$
\|H_m\|\le L_m,\qquad
\|H_m\Pi_{1,m}\|\le h_m,\qquad
\|H_m^k\Pi_{1,m}\|\le L_m^{k-1}h_m\quad(k\ge1),
\tag{6.2}
$$
其中 $L_m,h_m$ 如 (1.7)。
没有把低头误差错误地估成单一 $a_m$。

R181 的实际中心幂估计应用于尾真空，给
$$
\|Z_m^r\Omega_{\ge m}\|\le C_rg_m^r,\qquad r=0,1,\ldots.
\tag{6.3}
$$
该式不需要全平面相位假设；真空的中心本来就是0。
实际尾幂域、有限柱高次域以及低头与尾的域交换都已包含于该接口。

在准确域内用 (6.1) 的二项式，
结合尾幂保持 $\Pi_{1,m}$，得到
$$
\|(X-s_mI)^pe_{1,m}\|
\le C_pg_m^p+
h_m\sum_{k=1}^p\binom pk
L_m^{k-1}C_{p-k}g_m^{p-k}
=E_{m,p}.
\tag{6.4}
$$

本题共同共轭 $C$ 把物理全1头变成全0头，且
$X^*=CXC$，包含全部定义域。
因此
$$
\boxed{
e_{0,m}\in\bigcap_p\operatorname{Dom}(X^*)^p,\qquad
\|(X^*-\overline{s_m}I)^pe_{0,m}\|\le E_{m,p}.
}
\tag{6.5}
$$
这是直接沿真实通常伴随域得到的估计，不把 $X^*$ 的像假设留在 $M$。

## 7. 从 M 的有界作用提取投影与右逆成本

设 $P=P_M$。
由于 $X$ 在全部 $M$ 上定义、保持 $M$ 且限制有界，
对 $z\in\operatorname{Dom}X^*$ 和 $h\in M$，
$$
\langle h,X^*z\rangle
=\langle X_Mh,z\rangle
=\langle h,X_M^*Pz\rangle.
$$
所以
$$
\boxed{PX^*z=X_M^*Pz.}
\tag{7.1}
$$
这里 $X_M^*$ 是 $M$ 上的通常有界伴随；
没有声称它等于全空间 $X^*|_M$。

对 (6.5) 的全幂域向量迭代 (7.1)，有
$$
(X_M^*-\overline{s_m}I)^pPe_{0,m}
=P(X^*-\overline{s_m}I)^pe_{0,m}.
$$
若 $s_m\in\rho(X_M)$，取有界逆即得
$$
\|Pe_{0,m}\|\le R_m^pE_{m,p},
$$
证明 (1.5)。

每个 $Pe_{0,m}$ 都非零：
否则非零有限柱 $e_{0,m}$ 属于 $A^*$ 不变的 $M^\perp$，
与其 $A^*$ 循环性及 $M\ne0$ 矛盾。

若 $J_m:\mathcal F_m\to M$ 满足 $\mathsf P_mJ_m=I_{\mathcal F_m}$，
取伴随给
$$
J_m^*Pe_{0,m}=e_{0,m}.
$$
所以
$$
\boxed{
\|J_m\|\ge\frac1{\|Pe_{0,m}\|}
\ge\frac1{R_m^pE_{m,p}}.
}
\tag{7.2}
$$
这是对每个固定整数 $p$ 同时成立的真实必要界。

若 $X_M=Y|_M$ 且 $Y\in\mathcal A$，
则 $\sigma(Y|_M)=\{\chi(Y)\}$。
当 $s_m\to s\ne\chi(Y)$ 时，
$Y-s_mI$ 在全空间为 $\mathcal A$ 单位，
其逆保持 $M$，且有一致范数界。
因此这里的 $R_m$ 可由一个只依赖 $Y$ 和该标量极限的常数控制。

## 8. 交替慢幂尾的具体后果

取
$$
a_j=(-1)^j(j+1)^{-\sigma},\qquad
\frac12<\sigma\le1,\qquad a_*=0.
$$
普通部分和趋于
$$
s_\infty=\sum_{j\ge0}(-1)^j(j+1)^{-\sigma}\in(0,1),
$$
因为项严格递减，交错级数的和严格位于0和首项1之间。
而
$$
g_m^2=\sum_{j\ge m}(j+1)^{-2\sigma}
\le C_\sigma(m+1)^{1-2\sigma}.
\tag{8.1}
$$

考虑真实慢平方共振的危险分支
$$
M\subseteq\ker(X-Y),\qquad
Y=(I-B_2)^{1/2}\in\mathcal A,\qquad \chi(Y)=1,
$$
其中保留真实 Bell 系数 $B_2$。
R144/R176 的安全因子和自然域论证说明，若相应平方核非零，
它确属于这个有界分支；本稿不重复该因子证明。

因为 $s_\infty\ne1$，第7节的 $R_m$ 一致有界。
实际 $\eta_{m-1}$ 比任意 $m$ 的负幂更快；
由 (3.4) 对 $h_m$ 的同一界及 $L_m\le6g\sqrt m$，
对每个 $N>0$ 选择充分大的固定 $p$，(6.4)–(7.2) 给
$$
\boxed{
\|P_Me_{0,m}\|=O_N(m^{-N}),\qquad
\|J_m\|\ge c_Nm^N
\quad(m\text{ 充分大}).
}
\tag{8.2}
$$
常数允许依赖 $N,\sigma,Y$；
不存在从该式得到某个统一有限上界的步骤。

## 9. 尚未跨越的边界

1. $\mathsf P_m$ 对每个第一阶确实给真实图逼近，但不必保持未知 $M$。
2. (5.2) 给统一有限列近核；(5.3) 给每个有限头满射。
   两者之间必须支付右逆成本，(7.2)–(8.2) 说明这个成本能够被迫非常大。
3. 没有证明 $P_M$ 与 $\mathsf P_m$ 在算子范数下渐近交换。
   因而也没有从正逆的共同准对角性推出其未知核投影的准对角性。
4. (6.5) 只使用明确的物理全零头测试向量。
   不将该估计升级成整个全零头柱上任意尾向量的一致界。
5. 本稿不推出慢平方核为零，也不把任何非零有限柱近核当作真实核。
