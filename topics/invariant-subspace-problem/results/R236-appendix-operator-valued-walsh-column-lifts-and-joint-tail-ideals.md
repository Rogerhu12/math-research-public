# R236 附录：算子系数 Walsh 首列提升、联合最大子式与精确一次尾交

日期：2026-11-13 UTC。作者：normal_complex / Astra-ISP-0c；root 与 central_review 已全文独立核验。

状态：**已证明的辅助结论。** 全文保留真实 carry。本文把有限头、真实尾算子系数的线性方程转为原交换代数的右因子，并在首形式阶为一时准确计算联合理想与下一尾代数的交。没有得到正常态锚的一致下界，也没有关闭普通 ISP。

## 1. 模型、已证输入与新增范围

沿用原 Haar 表示
$$
\mathscr H=K_n\otimes\mathscr H_n,\qquad
K_n=(\mathbb C^2)^{\otimes n},\qquad H_n=2^n,
$$
以及实际范数代数
$$
\mathcal A=\overline{\mathbb C[I,A]}^{\|\cdot\|}.
$$
本篇用 $H_n$ 表示有限头维数，用 $\mathscr H_n$ 表示尾 Hilbert 空间。

真实归一化幂与尾代数为
$$
A^{2^n}=d_n I_{K_n}\otimes\widehat N_n,\qquad
\mathcal B_n=\overline{\mathbb C[I,\widehat N_n]}^{\|\cdot\|}.
\tag{1.1}
$$
据 R124 §2，$I_{K_n}\otimes\mathcal B_n\subset\mathcal A$。
对实际多项式直接作头分块，再取范数极限，亦得
$$
\mathcal A\subset M_{H_n}(\mathcal B_n).
\tag{1.2}
$$
矩阵条目是尾上的有界算子，矩阵范数始终是其在
$K_n\otimes\mathscr H_n$ 上的算子范数。

引用的完整已证输入：

- [R124：dyadic 余数缩放等距因式](R124-dyadic-residue-factorization-and-order-one-kernels.md) §2：真实尾代数及有界余数分解。
- [R253：正部分迹与相位乘积消元](R253-positive-tail-partial-traces-and-dyadic-phase-product-elimination.md) §§1–6：真实尾识别、同一正常正态的部分迹、非零相位乘积及尾真空必要界。
- [实际有限头源稿](R236-appendix-exact-head-vacuum-column-and-carry-cost.md) §4.8：标量有限头 Walsh 提升与实际正常泛函接口。

本文的新提升允许**算子值尾系数**，并保完整列算子范数。
它不使用物理首列的 $W_s^{-1}$ 除法费用。
R124 的物理基底除法仍正确，但不是下面首列选择所需的预算。

## 2. 对任意尾向量准确成立的 Walsh 首列

写
$$
V_j=(I-N_j)(I+N_j)^{-1},\qquad
V_F=\prod_{j\in F}V_j.
$$
在第 $j$ 位物理分块中，
$$
N_j=\begin{pmatrix}0&t_j\\ I&0\end{pmatrix},
\qquad t_j=\eta_j N_{j+1}.
$$
所有矩阵条目作用在第 $j$ 位之后，且 $\|t_j\|\le\eta_j<1$。

把该位改写到正交基
$$
\Omega_j=(e_0+e_1)/\sqrt2,\qquad
\chi_j=(e_0-e_1)/\sqrt2
$$
中，直接求逆得
$$
V_j=
\begin{pmatrix}
0&-I\\ I&2K_j
\end{pmatrix},
\qquad
K_j=(I+t_j)(I-t_j)^{-1}.
\tag{2.1}
$$
因此，对任意其余位向量 $h$，
$$
V_j(\Omega_j\otimes h)=\chi_j\otimes h.
\tag{2.2}
$$
此式不要求 $h$ 为真空，也没有把 $V_j$ 当成局部张量矩阵。

实际 $\eta_j\le e^{-770\cdot16^j}$，而
$$
\left\|\begin{pmatrix}0&-1\\1&2\end{pmatrix}\right\|=1+\sqrt2.
$$
由 (2.1)，
$$
\|V_j\|\le1+\sqrt2+\frac{4\eta_j}{1-\eta_j}<3.
\tag{2.3}
$$
各 $V_j$ 属于交换代数 $\mathcal A$。
在每次使用 (2.2) 时，尚未选取的那一位仍为 $\Omega_j$，所以逐位得到
$$
V_F(\Omega_{<n}\otimes h)=\chi_F\otimes h
\quad(F\subset[0,n),\ h\in\mathscr H_n).
\tag{2.4}
$$

定义等距列
$$
e_n:\mathscr H_n\longrightarrow\mathscr H,\qquad
e_nh=\Omega_{<n}\otimes h.
$$
式 (2.4) 表明，全部 $V_Fe_n\mathscr H_n$ 是相互正交的
$H_n$ 个 Walsh 头分量，其直和为整个 $\mathscr H$。

## 3. 算子系数首列提升及完整列范数

### 3.1 提升的定义与费用

取任意
$$
U\in M_{H_n}(\mathcal B_n).
$$
把它的 Walsh 首列写成
$$
Ue_n=\sum_{F\subset[0,n)}\chi_F\otimes u_F,
\qquad
u_F=(\langle\chi_F|\otimes I)Ue_n\in\mathcal B_n.
\tag{3.1}
$$
定义
$$
\boxed{
\mathfrak L_n(U)=\sum_{F\subset[0,n)}
V_F(I_{K_n}\otimes u_F)\in\mathcal A.
}
\tag{3.2}
$$
所有系数都在真实尾代数中，故每项及总和确属原 $\mathcal A$。
由 (2.4)，
$$
\mathfrak L_n(U)e_n=Ue_n.
\tag{3.3}
$$

算子行 $[V_F]_F$ 满足
$$
\|[V_F]_F\|^2
=\left\|\sum_F V_FV_F^*\right\|
\le\sum_F\|V_F\|^2
\le\sum_F9^{|F|}=10^n.
\tag{3.4}
$$
而真实系数列满足准确恒等式
$$
\sum_Fu_F^*u_F=e_n^*U^*Ue_n.
\tag{3.5}
$$
将 (3.2) 看作该算子行与系数列的乘积，即得
$$
\boxed{
\|\mathfrak L_n(U)\|
\le K_n\|Ue_n\|\le K_n\|U\|,
\qquad K_n=10^{n/2}.
}
\tag{3.6}
$$
这里使用的是算子行列 Cauchy–Schwarz，不是逐项估计后遗漏系数数目。

更一般地，对任意有限组 $U_1,\ldots,U_s$，
$$
\boxed{
\left\|\operatorname{col}_{i=1}^s\mathfrak L_n(U_i)\right\|
\le K_n\left\|\operatorname{col}_{i=1}^s U_i e_n\right\|
\le K_n\left\|\operatorname{col}_{i=1}^s U_i\right\|.
}
\tag{3.7}
$$
证明是将 $[V_F]_F$ 重复为块对角行算子，并使用
$$
\sum_{i,F}u_{iF}^*u_{iF}
=e_n^*\left(\sum_iU_i^*U_i\right)e_n.
$$
因此 $s$ 不额外进入提升常数。

### 3.2 忠实首列与左模性质

若 $R\in\mathcal A$ 且 $Re_n=0$，则 $R$ 与所有 $V_F$ 交换，
故
$$
RV_Fe_n=V_FRe_n=0.
$$
由 (2.4) 的完整直和，
$$
\boxed{R=0.}
\tag{3.8}
$$
因此 (3.3) 对 $U=R\in\mathcal A$ 给
$$
\mathfrak L_n(R)=R.
\tag{3.9}
$$
它是从 $M_{H_n}(\mathcal B_n)$ 到 $\mathcal A$ 的有界线性投影。

对 $S\in\mathcal A$ 和任意 $U\in M_{H_n}(\mathcal B_n)$，
两实际算子 $\mathfrak L_n(SU)$ 与 $S\mathfrak L_n(U)$
在 $e_n\mathscr H_n$ 上相同；再用 (3.8)，得到
$$
\boxed{\mathfrak L_n(SU)=S\mathfrak L_n(U).}
\tag{3.10}
$$
只需且只主张这个**左** $\mathcal A$ 模性质；
没有声称对任意矩阵 $U$ 也有右模性质。

### 3.3 真实矩阵证书的提升

设 $S_1,\ldots,S_s,D\in\mathcal A$，
$U_i\in M_{H_n}(\mathcal B_n)$，并有
$$
D-\sum_iS_iU_i=E.
$$
令 $u_i=\mathfrak L_n(U_i)$。由 (3.9)–(3.10)，
$$
D-\sum_iS_iu_i=\mathfrak L_n(E),
$$
从而
$$
\boxed{
\left\|D-\sum_iS_iu_i\right\|\le K_n\|Ee_n\|,
\qquad
\|\operatorname{col}u_i\|
\le K_n\|\operatorname{col}U_ie_n\|.
}
\tag{3.11}
$$
特别，若矩阵等式无残量，便得到无残量的原交换代数等式。

这一步不能改为直接用正常泛函测试 $\sum_i S_iU_i$：
一般 $U_i$ 不在 $\mathcal A'$。
合法右因子是提升后的 $u_i\in\mathcal A$。
上述证明没有使用无限相位酉或不受控的物理首列逆权。

### 3.4 完整源最优化的等价字典

对 $D\in\mathcal A$，设 $c_n(D)$ 是下列尾系数列解的最小费用：
$$
c_n(D)=
\inf\left\{
\|\operatorname{col}_{i,F}b_{iF}\|:
\sum_i S_i\left(\sum_F\chi_F\otimes b_{iF}\right)=De_n,\
b_{iF}\in\mathcal B_n
\right\}.
\tag{3.12}
$$
列算子作用于 $\mathscr H_n$；无解时下确界为 $+\infty$。
另设真实右因子费用
$$
c_{\mathcal A}(D)=
\inf\left\{
\|\operatorname{col}_i u_i\|:
D=\sum_iS_iu_i,\ u_i\in\mathcal A
\right\}.
$$
实际解取首列给 $c_n(D)\le c_{\mathcal A}(D)$。
反之，把任一列解补成矩阵 $U_i$，或直接按 (3.2) 提升该列，
(3.8) 付整个算子等式，(3.7) 付费用。因此
$$
\boxed{
c_n(D)\le c_{\mathcal A}(D)\le K_n c_n(D).
}
\tag{3.13}
$$
这是全部算子值列解的字典，不只某个 Cramer 候选。
它没有给出 $c_n(D)$ 本身的上界。

## 4. 全部最大子式都是合法的真实尾目标

固定两行 $S,Z\in\mathcal A$，记
$$
\mathcal I=S\mathcal A+Z\mathcal A.
$$
在第 $n$ 个头分块中形成矩形矩阵
$$
\mathcal R_n=[\,S\ \ Z\,]\in M_{H_n,2H_n}(\mathcal B_n).
$$
取任意 $H_n$ 个列的集合 $J$，令 $B_J$ 为所得方阵，置
$$
\delta_J=\det B_J\in\mathcal B_n.
$$
矩阵条目互相交换，所以代数伴随矩阵恒等式准确成立：
$$
B_J\operatorname{adj}B_J=\delta_J I_{H_n}.
$$
把伴随矩阵嵌回被选择的 $2H_n$ 个行，分成上下两块 $U_J,W_J$，得到
$$
SU_J+ZW_J=I_{K_n}\otimes\delta_J.
\tag{4.1}
$$
由 §3，存在实际 $u_J,w_J\in\mathcal A$ 使
$$
\boxed{
I_{K_n}\otimes\delta_J=Su_J+Zw_J.
}
\tag{4.2}
$$

取
$$
M=\max(1,\|S\|,\|Z\|).
$$
各伴随条目至多是 $(H_n-1)!$ 个、每个范数不超过
$M^{H_n-1}$ 的乘积之和。矩阵范数至多为维数乘最大条目范数，
而选列嵌入保持伴随矩阵的算子范数。因此
$$
\boxed{
\|\operatorname{col}(u_J,w_J)\|
\le K_n H_n!M^{H_n-1},
\qquad
\|\delta_J\|\le H_n!M^{H_n}.
}
\tag{4.3}
$$
此粗界不要求某个子式可逆。

任意有限尾系数组合 $\delta=\sum_J b_J\delta_J$，
$b_J\in\mathcal B_n$，仍有真实证书，
例如由 (4.3) 支付的总费用为
$$
K_nH_n!M^{H_n-1}\sum_J\|b_J\|.
\tag{4.4}
$$
这里没有把组合系数或可能的消去损失藏入常数。

令 $\mathcal F_n$ 为全部最大子式生成的范数闭尾理想。
则准确有
$$
I_{K_n}\otimes\mathcal F_n
\subset\overline{\mathcal I}^{\|\cdot\|}.
\tag{4.5}
$$
没有声称最大子式理想一定等于全部尾交。
抽象地，最大子式给呈示模的一个消去理想，未必等于其完整湮灭理想。

### 4.1 与相位乘积、铅笔行列式的关系

由 Cauchy–Binet，$\det(S+tZ)$ 的每个 $t$ 系数是 (4.2)
中某些最大子式的带符号和。所以全部子式保留了这些铅笔证书，
而不必只选择一个参数 $t$。

当 $S\ne0$ 时，选择全部 $S$ 列给一个非零子式。
具体说，先对多项式 $S=p(A)$ 使用
$A^{H_n}=d_nI\otimes\widehat N_n$ 的有限伴随矩阵：
多项式恒等式给
$$
I_{K_n}\otimes\det S
=\prod_{\zeta^{H_n}=1}\gamma_\zeta(S).
\tag{4.6}
$$
这也可在形式域中把 $x^{H_n}-d_nz$ 的根代入 $p$ 后相乘核对。
对一般 $S\in\mathcal A$，多项式范数逼近同时保持有限行列式和有限乘积，
故 (4.6) 仍成立。
R253 §3 的忠实形式首项证明右边非零。
因此 $\mathcal F_n\ne0$，且包含 R253 的单行相位乘积尾理想。

本文不据此断言不同 $n$ 的 $\mathcal F_n$ 互相嵌套。
下一节使用的是本来就嵌套的完整尾交。

## 5. 同一个正正常态及完整尾交

设
$$
\rho\ge0,\quad \rho\ne0,\quad
\tau=\operatorname{Tr}\rho,\qquad
\phi_\rho(SR)=\phi_\rho(ZR)=0\quad(R\in\mathcal A).
\tag{5.1}
$$
若原假设在全部 $\mathcal A'$ 成立，自然包含 (5.1)。
定义正部分迹
$$
\rho_n=\operatorname{Tr}_{K_n}\rho.
$$
每个 (4.2) 及其任意尾右倍数都给
$$
\operatorname{Tr}(\rho_n\delta_J b)=0
\quad(b\in\mathcal B_n).
\tag{5.2}
$$
没有改变原 $\rho$，也没有以某个 Cramer 系数右乘它来声称新泛函为正。

定义完整的范数闭尾交
$$
\mathcal J_n=
\{b\in\mathcal B_n:I_{K_n}\otimes b
\in\overline{\mathcal I}^{\|\cdot\|}\}.
\tag{5.3}
$$
它是闭尾理想，包含 $\mathcal F_n$，并被同一 $\rho_n$ 湮灭。
令
$$
q_n^{\rm joint}
=\sup_{\substack{b\in\mathcal J_n\\\|b\|\le1}}
|\langle b\Omega_n,\Omega_n\rangle|.
\tag{5.4}
$$
若 $S\ne0$，R253 §6 的循环性与 $C$ 对称性证明逐项适用于非零
$\det S\,\mathcal B_n\subset\mathcal J_n$，故 $q_n^{\rm joint}>0$。
将各尾交提升回原空间后，
$$
I_{K_{n+1}}\otimes\mathcal J_{n+1}
\subset I_{K_n}\otimes\mathcal J_n.
$$
所以
$$
1\ge q_0^{\rm joint}\ge q_1^{\rm joint}\ge\cdots>0.
\tag{5.5}
$$

记 $\Pi_n=I_{K_n}\otimes|\Omega_n\rangle\langle\Omega_n|$、
$\delta_n=\operatorname{Tr}(\rho(I-\Pi_n))\downarrow0$。
R253 §5 的正部分迹估计为
$$
\|\rho_n-\tau|\Omega_n\rangle\langle\Omega_n|\|_1
\le2\sqrt{\tau\delta_n}.
$$
测试 $\mathcal J_n$ 的单位球得
$$
\boxed{
\tau q_n^{\rm joint}\le2\sqrt{\tau\delta_n},
\qquad
q_n^{\rm joint}\longrightarrow0.
}
\tag{5.6}
$$
它至少与单行相位理想的必要条件一样强。
所缺的仍是某个实际联合尾目标的正常锚一致下界；
每层子式非零与 (5.5) 的严格正性都不是这种一致下界。

## 6. 首阶一时，联合尾交的准确两生成元递推

### 6.1 单位奇块的完整代数消元

现只剥一个实际位，写
$$
\mathcal A_{\rm cur}=\mathcal B\oplus N\mathcal B,
\qquad
N^2=t=\eta\widehat N_{\rm next}.
\tag{6.1}
$$
这里 $\mathcal B$ 是下一真实尾代数。
R124 的偶、奇余数分解表明 (6.1) 是具有有界系数映射的拓扑直和。

设
$$
S=C+ND,\qquad Z=E+NF,\qquad
C,D,E,F\in\mathcal B,
\qquad D\in\mathcal B^\times.
$$
置
$$
G=D^{-1}C,\qquad
h=G^2-t,\qquad k=E-GF.
\tag{6.2}
$$
则
$$
\boxed{
(S\mathcal A_{\rm cur}+Z\mathcal A_{\rm cur})\cap\mathcal B
=h\mathcal B+k\mathcal B.
}
\tag{6.3}
$$

先由全部实际交换关系得到
$$
h=-(N-G)D^{-1}S,\qquad
k=Z-FD^{-1}S.
\tag{6.4}
$$
因此右边包含于左边。

为证反向，定义有界线性余式映射
$$
r(C_0+ND_0)=C_0-GD_0.
$$
它在 $\mathcal B$ 上为恒等，且
$$
R-r(R)=(N+G)D_0\in S\mathcal A_{\rm cur}.
\tag{6.5}
$$
对任意 $a,b\in\mathcal B$，直接计算
$$
r((N+G)(a+Nb))=-hb,
$$
$$
r(Z(a+Nb))=ka-(Gk+hF)b.
\tag{6.6}
$$
所以 $r(S\mathcal A_{\rm cur}+Z\mathcal A_{\rm cur})
\subset h\mathcal B+k\mathcal B$，而对属于 $\mathcal B$ 的元素，
$r$ 不改变它，反向包含得证。

这些等式也给闭理想的准确版本：
$$
\boxed{
\overline{S\mathcal A_{\rm cur}+Z\mathcal A_{\rm cur}}
\cap\mathcal B
=\overline{h\mathcal B+k\mathcal B}.
}
\tag{6.7}
$$
证明不交换“交”与“闭包”：由 (6.5)–(6.6) 先得
$$
S\mathcal A_{\rm cur}+Z\mathcal A_{\rm cur}
=r^{-1}(h\mathcal B+k\mathcal B).
$$
连续性给一个方向；若 $r(R)$ 是右侧理想的范数极限，
把该极限加回固定的 $R-r(R)$ 即给另一个方向。
最后限制到 $\mathcal B$ 得 (6.7)。

### 6.2 同一正态保持与实际源费用

由 (6.4)，原正态湮灭 $S$、$Z$ 的实际右理想时，
它的下一尾正部分迹湮灭 $h$、$k$ 的全部尾右倍数。
这里用 $D^{-1}$ 只是选择一个实际有界测试；
保持同一正态并不要求各步 $\|D^{-1}\|$ 一致有界。

但是，若要对源范数或归一目标锚作估计，这个费用必须保留。
例如对 $b,c\in\mathcal B$，
$$
hb+kc
=S\{-D^{-1}[(N-G)b+Fc]\}+Zc.
\tag{6.8}
$$
故一个直接源预算为
$$
\|D^{-1}\|\big[(\|N\|+\|G\|)\|b\|+\|F\|\|c\|\big]+\|c\|.
\tag{6.9}
$$
本文没有把该式中的单位逆或递推后系数免费吸收。

### 6.3 首形式阶一可无限递进，首阶更高不据此归一

若 $S$ 对当前 $\widehat N_{\rm cur}$ 的形式首阶恰为一，
则偶块 $C$ 的常数字符为零，奇块 $D$ 的常数字符非零。
下一尾代数由拟幂零算子单生成，只有常数字符；
因此 $D$ 在该 Banach 代数中为单位。

此时 $G$ 的字符为零，所以
$$
h=G^2-\eta\widehat N_{\rm next}
$$
对下一实际归一化尾变量的首形式阶仍为一，
首系数准确为 $-\eta\ne0$。
于是可以从 $(S_0,Z_0)$ 逐位递推
$$
S_{j+1}=G_j^2-\eta_j\widehat N_{j+1},
\qquad
Z_{j+1}=E_j-G_jF_j.
\tag{6.10}
$$
反复使用 (6.3) 和 (6.7)，得到对每个有限 $n$ 的准确身份
$$
(S_0\mathcal A+Z_0\mathcal A)\cap
(I_{K_n}\otimes\mathcal B_n)
=I_{K_n}\otimes(S_n\mathcal B_n+Z_n\mathcal B_n),
\tag{6.11}
$$
以及
$$
\boxed{
\mathcal J_n
=\overline{S_n\mathcal B_n+Z_n\mathcal B_n}.
}
\tag{6.12}
$$
因此在首阶一的假设下，§5 的完整联合尾理想不是仅由某个
行列式子理想代替，而是由 (6.10) 精确给出。

没有把任意首阶 $r>1$ 的元素改成首阶一：
R124 已明确，零余数块的零字符并不自动允许再有界除一个 $A$。
即使在首阶一范围，(6.10) 也没有给 (6.9) 的统一预算或
$q_n^{\rm joint}$ 的一致正下界。

## 7. 完整实际交换子的同一提升与尾交

前面特意先在范数代数中给出所有实际恒等式。
下面说明它们还可在完整实际右因子空间中使用。

置
$$
\mathcal C_n=\{\widehat N_n\}'\subset B(\mathscr H_n).
$$
从 $A$ 的有限头矩阵条目属于 $\mathcal B_n$ 得
$$
I_{K_n}\otimes\mathcal C_n\subset\mathcal A'.
\tag{7.1}
$$
反过来，若 $R\in\mathcal A'$，则
$[R,A^{2^n}]=0$。对其每个有限头矩阵条目使用 (1.1)，得
$$
\mathcal A'\subset M_{H_n}(\mathcal C_n).
\tag{7.2}
$$
R88 已证明原 $\mathcal A'$ 交换，所以由 (7.1)，$\mathcal C_n$ 亦交换。

在 (3.1)–(3.2) 中允许 $U$ 的条目属于 $\mathcal C_n$。
所有 $I\otimes u_F$ 由 (7.1) 属于 $\mathcal A'$，故
$$
\mathfrak L_n:M_{H_n}(\mathcal C_n)\longrightarrow\mathcal A'
$$
定义良好。(2.4)、(3.4)–(3.7) 与条目是否是范数多项式极限无关，
因此完整 tuple 范数仍为 $K_n=10^{n/2}$。

若 $R\in\mathcal A'$ 且 $Re_n=0$，它仍与所有
$V_F\in\mathcal A$ 交换，故 (3.8) 仍成立。
因此
$$
\mathfrak L_n|_{\mathcal A'}=I,\qquad
\mathfrak L_n(SU)=S\mathfrak L_n(U)
\quad(S\in\mathcal A',\ U\in M_{H_n}(\mathcal C_n)).
\tag{7.3}
$$
这直接给出 §3.3 的实际残量界及 §3.4 的完整右因子字典：
$$
\boxed{
c_n^{\mathcal C}(D)
\le
\inf_{\substack{D=\sum_iS_iu_i\\u_i\in\mathcal A'}}
\|\operatorname{col}u_i\|
\le K_n c_n^{\mathcal C}(D).
}
\tag{7.4}
$$
$c_n^{\mathcal C}$ 的定义是 (3.12) 中将尾系数代数换为
$\mathcal C_n$。它不要求候选右因子具有范数多项式逼近。

同理，§4 的交换条目行列式与 Cramer 证明对
$S,Z\in\mathcal A'$ 和 $\mathcal C_n$ 系数成立。
若 $\phi_\rho$ 湮灭全部 $S\mathcal A'+Z\mathcal A'$，
对应完整尾交
$$
\mathcal J_n'=
\{b\in\mathcal C_n:
I_{K_n}\otimes b\in
\overline{S\mathcal A'+Z\mathcal A'}^{\|\cdot\|}\}
\tag{7.5}
$$
仍被同一个正部分迹 $\rho_n$ 湮灭，
其真空测试量满足 $0\le q_n\le1$、(5.5) 的非增性及 (5.6)。
当 $S\in\mathcal A$ 非零时，原相位乘积保证每层严格正性。
这里没有把形式首项理论扩展到任意 $\mathcal A'$ 元素。

最后核对 §6 的完整交换子版本。
在一次物理分块
$N=\left(\begin{smallmatrix}0&t\\I&0\end{smallmatrix}\right)$ 中，
任意有界矩阵 $R$ 满足 $RN=NR$ 当且仅当
$$
R=\begin{pmatrix}a&tc\\c&a\end{pmatrix},
\qquad at=ta,\quad ct=tc.
\tag{7.6}
$$
由于 $t=\eta\widehat N_{\rm next}$ 且 $\eta\ne0$，这给出
$$
\{N\}'=\mathcal C_{\rm next}\oplus N\mathcal C_{\rm next},
\tag{7.7}
$$
系数 $a,c$ 是真实块压缩，范数均不超过 $\|R\|$。
对仍属于实际范数代数的 $S,Z$，若 §6 的 $D$ 是单位，
余式映射的完整计算可逐字在 $\mathcal C_{\rm next}$ 中进行：
$$
\boxed{
(S\{N\}'+Z\{N\}')\cap\mathcal C_{\rm next}
=h\mathcal C_{\rm next}+k\mathcal C_{\rm next},
}
\tag{7.8}
$$
并有相应的范数闭包等式。
若初始 $S$ 的首形式阶为一，$S_j,Z_j,G_j,D_j^{-1}$
始终留在真实范数尾代数，所以原形式首阶与单位论证仍合法；
全部测试系数则可取完整 $\mathcal C_j$。

因此 §6 的两生成元递推还准确描述 (7.5)，
而非仅描述范数多项式右因子生成的子理想。
(6.9) 中的实际单位逆费用依然存在；
以上范围扩展没有给它们统一上界，也没有给尾真空锚下界。

## 8. 已付内容与下一实际缺口

本文已付：

1. 对所有尾向量成立的实际 Walsh 首列、完整算子值列提升及 $K_n=10^{n/2}$ 费用；
2. 任意有限头矩阵右证书到原实际交换理想的合法转换，以及完整列最优化字典；
3. 全部最大子式的真实尾证书，同一个正正常态的部分迹湮灭关系；
4. 首形式阶一时完整联合尾交的两生成元递推，含闭包及所有单位逆的作用位置；
5. 同一首列提升、源最优化与一次尾交在完整实际交换子 $\mathcal A'$ 上的版本。

本文没有用有限矩阵解的存在替代原实际正常锚。
后续可在 §3.4 的完整列空间中优化真实尾目标，或在 §6 的两行递推中估计
$q_n^{\rm joint}$；都必须同时保留源费用、归一目标及同一正态的量词。
