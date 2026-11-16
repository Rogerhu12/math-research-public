# R271 附录：固定与缓增终端高度的完整物理真核门及原头行列式常数

日期：2026-11-16（UTC）。作者：Astra-ISP-789f / root、boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：已证明。** 本文对原 N/Y 两型给出整个物理真核的投影上界，保留所有强位状态、远尾 primitive 和零源。它说明：固定测试头并不能使终端核条件免费降为固定高度。若强位数 $R$ 与远孔上界 $J$ 满足 $(R+J)^4=o(\log m)$，则非真空旧头测试在这一完整真核上的投影趋零。

这是有限头模型中一个准确的终端限制，不是原 $M=\ker T$ 的排除结论。原允许增长的 $Q$ 窗口通常远大于本稿范围；当 $R>0$ 时，所研究的远孔限制也不能替换成较大的原总孔限制。

原头与权按 [R239 真实头稿](R239-appendix-true-head-jordan-cost-and-pure-graded-formal-range.md) §1、[低物理孔借位稿](R271-appendix-low-physical-hole-borrow-powers-and-complete-gram-compression.md) §§1--3。终端条件与[同源相容塔稿](R271-appendix-compatible-bernoulli-vacuum-towers-and-same-test-exact-kernel-approximation.md) 中的 $\ker C^{J+1}$ 一致；本文直接从完整物理链证明，而不交换环境逆与受限逆。

## 1. 原模型、全部真核与 forcing

令 $m\ge1$、$d=2^m$，原有限头作用在
$$
\mathfrak h_m=\operatorname{span}\{e_0,\ldots,e_{d-1}\}.
$$
原后移及两型头为
$$
B_me_n=\frac{W_n}{W_{n-1}}e_{n-1},\qquad
W_n=\prod_{i\in\operatorname{bits}(n)}d_i,\qquad
d_i=e^{-\Lambda_i},
$$
$$
\Lambda_i=100\,16^i-105\,8^i+(150i+25)2^i,\qquad d_0=e^{-20},
\tag{1.1}
$$
$$
A_m=F_{N,m}(B_m)
\quad\hbox{或}\quad
A_m=F_{Y,m}(B_m),
$$
$$
F_{N,m}(z)=\sum_{i<m}(i+1)^{-2}\frac{z^{2^i}}{d_i},\qquad
F_{Y,m}(z)=\sum_{i<m}(i+1)^{-2}\frac{z^{2^i}}{d_i+z^{2^i}}.
\tag{1.2}
$$
Y 型代入是准确的有限幂零截断。两型共同满足
$$
F_{N/Y,m}'(0)=d_0^{-1},\qquad \|A_m\|\le6.
\tag{1.3}
$$
后一个界也覆盖 $m=1,2$：此时真实头是 $m=3$ 真实头的不变子空间限制，新增的 $2^i$ 次幂在小头上为零。一般的范数界直接由 $\|N_i\|\le1$、$\sum_i(i+1)^{-2}<2$ 以及
$\|(I+N_i)^{-1}\|<3$ 得到。

取整数 $R,J\ge0$，置 $x=m+R$，将原纯尾按位置分为
$$
E=D_{[m,x)}=\sum_{i=m}^{x-1}b_iE_i,\qquad
D_>=\sum_{i\ge x}b_iE_i,\qquad b_i=(i+1)^{-2}.
$$
这里 $E_i$ 是第 $i$ 个真实 Boolean 位的删除，$\|E_i\|=1$。所以
$$
\boxed{
\|E\|\le\sum_{i=m}^{m+R-1}(i+1)^{-2}
\le\frac{R}{(m+1)^2}.
}
\tag{1.4}
$$
令
$$
C=A_m+E,\qquad
S_x=\sum_{i\ge x}(i+1)^{-4}\le\frac1{3x^3}.
\tag{1.5}
$$
$C$ 作用在旧头与全部 $R$ 个强位上，$D_>$ 作用在其后的无限远尾。二者有界且交换。全部远尾删除本身也有界，因为 $\sum_{i\ge x}b_i<\infty$。

记 $\Pi_j^>$ 为恰有 $j$ 个远孔的物理正交投影，定义闭真核
$$
\mathscr K_{m,R,J}
=
\{v:\Pi_{\le J}^>v=v,\ (C+D_>)v=0\}.
\tag{1.6}
$$
这里没有删去任何远尾 primitive、真零源或强位 nuisance。特别不要求 $v$ 是一个预选相干塔。

forcing 始终是原同一个物理向量
$$
f=i_0g:=g\otimes\Omega_<\otimes\Omega_>,
\qquad g\in\mathfrak h_m,
\tag{1.7}
$$
其中两个 $\Omega$ 分别是强位和远尾真空。先假设
$$
g\perp e_0.
\tag{1.8}
$$
一般 $g$ 的准确版本在 §4。

## 2. 顶方程迫使真正底源位于一个有限头

置 $K=R+J$。对任意 $v\in\mathscr K_{m,R,J}$，写
$$
v=\sum_{j=0}^J v_j,\qquad v_j=\Pi_j^>v,
\qquad a_0=v_0\in\mathfrak h_m\otimes\mathcal H_<.
$$
完整核方程逐个物理远孔层给
$$
D_>v_{j+1}=-Cv_j\quad(0\le j<J),
\qquad Cv_J=0.
\tag{2.1}
$$
由于 $C$ 与 $D_>$ 交换，
$$
D_>^jv_j=(-1)^jC^ja_0.
$$
把顶方程再左乘 $D_>^J$，得到准确的终端条件
$$
\boxed{C^{J+1}a_0=0.}
\tag{2.2}
$$
$J=0$ 时它就是原顶方程 $Ca_0=0$。

强位删除满足 $E^{R+1}=0$，且 $C,E$ 交换。于是
$$
A_m^{R+J+1}a_0=(C-E)^{R+J+1}a_0=0:
\tag{2.3}
$$
二项展开中，$E$ 次数至少 $R+1$ 的项为零；其余项的 $C$ 次数至少 $J+1$，由 (2.2) 为零。

因为 $A_m=B_mU_m(B_m)$、$U_m(0)=d_0^{-1}\ne0$，有限幂零代数中的 $U_m(B_m)$ 可逆，故
$$
\ker A_m^r
=\ker B_m^r
=\operatorname{span}\{e_0,\ldots,e_{\min(r-1,d-1)}\}.
$$
因此令 $t=\min(K,d-1)$，便有
$$
\boxed{
a_0\in
\operatorname{span}\{e_0,\ldots,e_t\}\otimes\mathcal H_<.
}
\tag{2.4}
$$
这是从完整真核导出的实际底源支持，不是对压缩逆作出的支持猜测。

所有 (2.1)--(2.4) 都是有界算子在 Hilbert 空间中的等式。各远孔层可以无限维；本论证没有使用 $D_>^\dagger$，因而也没有省略其自然定义域或值域条件。

## 3. 原头非零奇值的完整行列式估计

对 $1\le t<d$，令 $A^{[t]}$ 为 $A_m$ 在
$\operatorname{span}\{e_0,\ldots,e_t\}$ 上的实际限制。它与以后增加的头长无关。考虑准确的方阵
$$
T_t:
\operatorname{span}\{e_1,\ldots,e_t\}
\longrightarrow
\operatorname{span}\{e_0,\ldots,e_{t-1}\},
\qquad
T_t=A^{[t]}|_{\{e_0\}^{\perp}}.
\tag{3.1}
$$
因为 $A_m$ 严格降低整数索引，(3.1) 包含这一输入子空间的**全部**输出，没有丢掉任何边界行。

按输入 $e_1,\ldots,e_t$、输出 $e_0,\ldots,e_{t-1}$ 排列，$T_t$ 上三角，对角元由 (1.3) 精确给出
$$
(T_t)_{n-1,n}=\frac{W_n}{d_0W_{n-1}},
\qquad
|\det T_t|=\frac{W_t}{d_0^t}.
\tag{3.2}
$$
令 $\mu_t=\sigma_{\min}(T_t)>0$。其余 $t-1$ 个奇值至多为
$\|T_t\|\le6$，所以
$$
\boxed{
\mu_t^{-1}\le
6^{\,t-1}\frac{d_0^t}{W_t}.
}
\tag{3.3}
$$
这是真实矩阵的最小奇值界，不是某个一维列范数的替代。

原权还给 $0<\Lambda_i\le100\,16^i$。上界等价于
$150i+25\le105\,4^i$，可从 $i=0,1$ 及随后归纳直接核验。因此
$$
-\log W_t
=\sum_{i\in\operatorname{bits}(t)}\Lambda_i
\le100\sum_{i\in\operatorname{bits}(t)}(2^i)^4
\le100t^4.
$$
又 $(t-1)\log6+t\log d_0=(t-1)\log6-20t\le0$，于是
$$
\boxed{\mu_t^{-1}\le e^{100t^4}\le e^{100K^4}.}
\tag{3.4}
$$

(3.1) 在全部强位空间上张量恒等后仍给
$$
\|(I-P_{e_0})a_0\|
\le\mu_t^{-1}\|A_ma_0\|.
\tag{3.5}
$$
(2.4) 正是 (3.5) 的支持依据。$P_{e_0}$ 这里只投旧头真空，保留全部强位状态；没有把它换成所有强位也真空的投影。

## 4. 整个物理真核投影的上界

令
$$
v=P_{\mathscr K_{m,R,J}}f,\qquad a_0=\Pi_0^>v.
$$
对 $J\ge1$，(2.1) 的第一行以及 $D_>:\mathcal H_1^>\to\mathcal H_0^>$ 的准确范数 $\sqrt{S_x}$ 给
$$
\|Ca_0\|\le\sqrt{S_x}\,\|v_1\|\le\sqrt{S_x}\,\|v\|.
\tag{4.1}
$$
当 $J=0$ 时，$\|Ca_0\|=0$，故 (4.1) 仍成立；这一情形可把右端的 $\sqrt{S_x}$ 删除。

由 $A_ma_0=Ca_0-Ea_0$、$\|a_0\|\le\|v\|$，
$$
\|A_ma_0\|\le(\sqrt{S_x}+\|E\|)\|v\|.
\tag{4.2}
$$
另一方面，真正正交投影满足
$$
\|v\|^2=\langle f,v\rangle
=\langle g\otimes\Omega_<,a_0\rangle.
$$
因 $g\perp e_0$，可以在该配对中的 $a_0$ 上插入 $I-P_{e_0}$。结合 (3.5)、(4.2)，若 $K\ge1$，
$$
\|v\|^2
\le
\|g\|\,\mu_t^{-1}(\sqrt{S_x}+\|E\|)\|v\|.
$$
$v=0$ 时结论直接成立；否则除以 $\|v\|$ 并平方，得到
$$
\boxed{
\|P_{\mathscr K_{m,R,J}}i_0g\|^2
\le
e^{200K^4}
\left(\sqrt{S_{m+R}}+\frac{R}{(m+1)^2}\right)^2
\|g\|^2,\qquad K=R+J\ge1,\quad g\perp e_0.
}
\tag{4.3}
$$
$J=0$ 时可删去 $\sqrt{S_{m+R}}$。$K=0$ 时 (2.4) 直接给非真空 forcing 的投影为零，无需定义 $\mu_0$。

对一般 $g$，全物理真空 $\Omega=i_0e_0$ 属于 $\mathscr K_{m,R,J}$。因此其真空分量与非真空分量在投影后仍正交，准确有
$$
\boxed{
\begin{aligned}
&\|P_{\mathscr K_{m,R,J}}i_0g
-\langle g,e_0\rangle\Omega\|^2\\
&\quad\le
e^{200K^4}
\left(\sqrt{S_{m+R}}+\frac{R}{(m+1)^2}\right)^2
\|(I-P_{e_0})g\|^2.
\end{aligned}
}
\tag{4.4}
$$
该范数控制的是完整物理投影。没有先选一个相干子族再将其投影误认成完整真核投影，也没有从 ambient 逆的单边序推出受限逆的下界。

## 5. 固定与缓增高度，以及不覆盖的原窗口

固定 $R,J$ 时，(4.3) 给
$$
\|P_{\mathscr K_{m,R,J}}i_0g\|^2
=O_{R,J}(m^{-3})\|g\|^2
\quad(g\perp e_0).
\tag{5.1}
$$
若 $J=0$，相应上界为 $O_R(m^{-4})$。

更一般地，若 $K_m=R_m+J_m$ 满足
$$
K_m^4=o(\log(m+1)),
$$
则 (4.4) 的系数仍趋零，且对所列全部旧头 forcing 统一。一个显式版本是
$$
K_m^4\le\frac{\log(m+1)}{100},\qquad m\ge3.
$$
此时 $e^{200K_m^4}\le(m+1)^2$、$R_m^2\le K_m^2\le\sqrt{\log(m+1)}/10$；由 $(a+b)^2\le2a^2+2b^2$ 及 $S_{m+R}\le1/(3m^3)$ 得
$$
\boxed{
\|P_{\mathscr K_{m,R_m,J_m}}i_0g\|^2
\le\frac2m\|g\|^2
\quad(g\perp e_0).
}
\tag{5.2}
$$
这只使用实际整数 $R_m,J_m$，没有隐含连续高度。

最后核清两个 cut。每个 $\mathscr K_{m,R,J}$ 向量最多有 $R$ 个强孔及 $J$ 个远孔，所以
$$
\mathscr K_{m,R,J}\subseteq K_{m,R+J}.
\tag{5.3}
$$
$R=0$ 时准确为 $\mathscr K_{m,0,J}=K_{m,J}$。$R>0$ 时反向包含一般不成立：较大的总孔窗口允许远孔数超过 $J$。因此不能把 (4.3) 的上界直接搬到 (5.3) 右侧。

本稿解释的是实际终端门：即使 forcing 只占一个固定低头，完整正规方程仍可能需要增长的终端高度及中间 source Schur。原合法增长 $Q$、原 $T-\mathcal L_m$ 的 carry 修复和同一 $w$ 的来源，均没有因 (4.3) 而自动受到排除或支付。特别，本文没有从这些较小模型真核投影的趋零推出原 $M=\ker T$ 只有真空，也没有证明普通 ISP 或 $N=M$。
