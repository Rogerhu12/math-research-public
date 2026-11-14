# R149 补稿：中心化倾斜 Bell 系数保留有限交集支路

日期：2026-11-12。作者：l2_moments。独立补稿，避免改动正在审读的 R149 主稿。
状态：完整证明待交叉核验。

## 1. 结论

保持 R149 的 $u,v$、$X=X_u$ 空谱及非零多项式 $q$。
令 $w$ 为任意复 $\ell^2$ 第一 chaos，常数项也任意。
则 R149 的两个非平凡支路均可加上指数权：
$$
\boxed{q(u)v e^w\text{ 循环},}
\tag{1.1}
$$
只要 $v$ 非常数，且满足以下任一条件：

- $h_v\le h_u$，允许任意无限重叠；
- $I=\{j:a_jb_j\ne0\}$ 有限，不要求首位顺序。

若 $v$ 为非零常数，结论也成立，见 §6。
当 $q$ 为非零常数时，直接使用 R147 的 $ve^w$ 循环性。
以下设 $\deg q=p\ge1$，归一化为首一，并设 $v$ 非常数。

第一支路已包含于 R150 的矩形次数定理；本稿额外保留了
$h_v>h_u$ 时有限交集的完整覆盖。

## 2. 倾斜一次项必须先中心化

写
$$
u=a_*+\sum_j a_j\chi_j,\quad
v=b_*+\sum_j b_j\chi_j,\quad
w=c_*+\sum_j c_j\chi_j.
$$
使用 R145/R147 的函数
$$
H(z,V)=e^{-zV}(\cosh z\,I+V\sinh z)
$$
以及范数整单位
$$
\mathcal B(s,t,\tau)=\prod_jH(sa_j+tb_j+\tau c_j,V_j).
$$
令
$$
B_w=\mathcal B(0,0,1),\qquad
\xi=B_w^{-1}e^w,\qquad
\widetilde B(s,t)=\mathcal B(s,t,1)B_w^{-1}.
\tag{2.1}
$$
$\xi$ 循环；R145 的整轨道给它全部 $X=X_u$、$Z=X_v$ 的混合自然域。

一般 $\widetilde B$ 的一次导数并不为零。定义有界交换子
$$
A_0=\partial_s\widetilde B(0,0),\qquad
C_0=\partial_t\widetilde B(0,0).
\tag{2.2}
$$
R147 的对数导数公式给
$$
A_0=\sum_j a_j H'(c_j,V_j)H(c_j,V_j)^{-1},
\quad
C_0=\sum_j b_j H'(c_j,V_j)H(c_j,V_j)^{-1}.
\tag{2.3}
$$
高位项分别由常数乘 $|a_jc_j|$、$|b_jc_j|$ 控制，故两和算子范数绝对收敛。
低位非零项有限，单独保留。
因活跃位分别从 $j_u,j_v$ 起，
$$
A_0\in\mathcal A_{h_u},\qquad C_0\in\mathcal A_{h_v},
\qquad \chi(A_0)=\chi(C_0)=0.
\tag{2.4}
$$

中心化为
$$
\widehat B(s,t)=e^{-sA_0-tC_0}\widetilde B(s,t),
\qquad X'=X+A_0,\quad Z'=Z+C_0.
\tag{2.5}
$$
于是 $\widehat B(0,0)=I$，且两个一次导数均为零。
有界交换扰动保持全部自然幂域；$\xi$ 仍处于 $X',Z'$ 的全部混合词域。

## 3. 新空谱逆及第二模式的有效首项

$X'$ 仍为空谱。具体对任意 $\lambda$，令
$R_\lambda=(X-\lambda)^{-1}$。R134 给 $R_\lambda$ 有界拟幂零，且与 $A_0$ 交换，所以
$$
X'-\lambda=(I+A_0R_\lambda)(X-\lambda)
$$
有有界逆 $R_\lambda(I+A_0R_\lambda)^{-1}$。
置
$$
R'=(X')^{-1}.
$$
它有界、属于全交换子且拟幂零。这里同样不要求 $R'\in\mathcal A$。

对 dyadic $\zeta$，记
$$
D'_u=\gamma_\zeta(X')-X',\qquad
D'_v=\gamma_\zeta(Z')-Z'.
$$
这些差有界，并保持一阶定义域。
R139 对 (2.4) 的真实差除法给
$$
D'_u=A^{h_u}d'_u,\qquad d'_u\in\mathcal A_{h_u}.
\tag{3.1}
$$
不要求 $d'_u$ 是标量收敛解析芽。
真实逆恒等式仍成立：
$$
\gamma_\zeta(R')-R'=-\gamma_\zeta(R')D'_uR',
\qquad R'=\gamma_\zeta(R')(I+D'_uR').
\tag{3.2}
$$
$\gamma_\zeta(R')$ 因酉共轭仍拟幂零。

设 $b=b_{j_v}\ne0$、$c=c_{j_v}$、$d=W_{h_v}$。
R147 的倾斜一次系数给
$$
c_{h_v}(C_0)=\frac{2b(1-e^{-2c})}{d}.
$$
结合 $Z$ 的首 gauge 差，得到
$$
\boxed{
D'_v=A^{h_v}d'_v,\qquad
\chi(d'_v)=-\frac{2be^{-2c}}{d}(\zeta^{h_v}-1).
}
\tag{3.3}
$$
所以 $\zeta^{h_v}\ne1$ 时 $d'_v\in\mathcal A_{h_v}$ 是真实单位。

## 4. 中心化后，混合余项再次降低一个 $X'$ 次数

令
$$
\widehat B_k=\partial_s^k\widehat B(0,0),\qquad
\widehat G_k=\partial_s^k\partial_t\widehat B(0,0).
$$
$\widehat B_0=I$、$\widehat G_0=0$。
由 R145 的混合生成函数恒等式，或在原倾斜恒等式中逐项代入
$X=X'-A_0$、$Z=Z'-C_0$，得到
$$
q(u)v e^w
=B_w\bigl[P_q(X')Z'\xi+C_q(X')\xi\bigr],
\tag{4.1}
$$
其中
$$
P_q(z)=\sum_{k=0}^p\frac{\widehat B_k}{k!}q^{(k)}(z),\qquad
C_q(z)=\sum_{k=0}^p\frac{\widehat G_k}{k!}q^{(k)}(z).
$$
$P_q$ 首一次数 $p$，$C_q$ 次数至多 $p-1$。
所有中间向量均在 §2 的混合自然域内。

由 $X'$ 空谱，R149 §4 的有限有界因式分解给
$$
J=P_q(X')^{-1}=(R')^pU^{-1}\in\{A\}',
\qquad
K=JC_q(X')=R'D
\tag{4.2}
$$
为真实有界算子；后一等式指自然多项式的有界延拓。
于是
$$
\boxed{JB_w^{-1}[q(u)v e^w]=(Z'+K)\xi.}
\tag{4.3}
$$

### 4.1 无限交集且 $h_v\le h_u$

$\widehat B_k$ 属于 $\mathcal A_{h_u}$。
为确认混合系数也如此，对数导数给
$$
\begin{aligned}
\partial_t\widehat B(s,0)
={}&\widehat B(s,0)\sum_j b_j\Bigl[
H'(c_j+sa_j,V_j)H(c_j+sa_j,V_j)^{-1}\\
&\hspace{105pt}-H'(c_j,V_j)H(c_j,V_j)^{-1}
\Bigr].
\end{aligned}
\tag{4.4}
$$
此和在每个紧 $s$ 集按范数收敛：高位差由常数乘
$|s|\,|a_jb_j|$ 控制，有限低位另外保留。
若 $a_jb_j=0$，相应项为零。
所以非零项只涉及 $j\ge j_u$，乘上同属该尾代数的
$\widehat B(s,0)$ 后，$\widehat G_k\in\mathcal A_{h_u}$。

因此 $D$ 与 R149 一样由 $R'$、这些尾系数及一个明确单位逆有限构成。
用 (3.1)—(3.2) 和 R139，有限望远镜及单位逆差给
$$
\gamma_\zeta(D)-D=A^{h_u}E_\zeta.
$$
从而
$$
\gamma_\zeta(K)-K
=A^{h_u}\gamma_\zeta(R')\bigl(E_\zeta-d'_uR'D\bigr).
\tag{4.5}
$$
结合 $h_v\le h_u$ 和 (3.3)，$Z'+K$ 的差为
$A^{h_v}$ 乘“单位加拟幂零项”，故为 $A^{h_v}$ 乘有界交换单位。

### 4.2 有限交集，不限制首位顺序

若 $I$ 有限，(4.4) 是有限和。由
$$
H'(z,V)H(z,V)^{-1}
=(I-V^2)e^{-zV}\sinh z\,H(z,V)^{-1},
\tag{4.6}
$$
每个括号都含同一个 $I-V_j^2$ 因子。
对 $j\in I$，有 $2^j\ge h_v$，所以 R149 的真实式
$$
I-V_j^2
=A^{h_v}\frac{4A^{2^j-h_v}}{W_{2^j}}(I+N_j)^{-2}
$$
使每个 $\widehat G_k$ 真实地等于 $A^{h_v}$ 乘一个有界交换子。
因此 (4.2) 可写为
$$
K=A^{h_v}R'L.
\tag{4.7}
$$
不需要对 $\gamma L-L$ 额外作有界除法。直接由 (3.2)，
$$
\gamma K-K
=A^{h_v}\gamma(R')
\bigl[\zeta^{h_v}\gamma L-(I+D'_uR')L\bigr].
\tag{4.8}
$$
故即使 $h_v>h_u$，结合 (3.3) 仍得到同一个单位差判据。

## 5. 真实闭域排核及循环传递

置 $T=Z'+K$，其域为 $\operatorname{Dom}Z$。
它是第一阶闭算子的有界交换扰动，故闭、$C$ 自伴、有限柱为图核心，且全交换子保持域。
两种支路都已证明
$$
\gamma_\zeta(T)-T=A^{h_v}\mathcal U_\zeta,
\qquad \mathcal U_\zeta\in\{A\}'^\times
\quad(\zeta^{h_v}\ne1).
$$
R149 §7 的真实限制稠密性及有限 Fourier 论证遂给
$\ker(T-\lambda)=0$ 对所有 $\lambda$ 成立。

取原第一阶 $Z$ 的共同正则化 $R_v(t)$。
$TR_v(t)$ 是有界单射交换子，因 $C$ 对称性值域稠密。
$\xi$ 循环，所以 $(TR_v(t))\xi$ 循环。
又 $\xi\in\operatorname{Dom}T$ 且域交换给
$$
(TR_v(t))\xi=R_v(t)T\xi.
$$
有界交换子保持循环空间，因此 $T\xi$ 循环。
(4.3) 的两个有界因子再把该结论传回 $q(u)v e^w$，证明 (1.1)。

## 6. 常数第二因子及范围

若 $v$ 为非零常数，用倾斜单模式中心化
$X'=X+A_0$，它仍空谱。
相应首一 $P_q(X')$ 有有界逆 $J$，而
$q(u)e^w=B_wP_q(X')\xi$。
于是 $JB_w^{-1}[q(u)e^w]=\xi$ 循环，给出结论。

这里的中心化不能省略：未经中心化时
$\partial_t\widetilde B(0,0)$ 一般非零，混合余项可能仍有 $X^p$ 项，
不能直接声称除去 $P_q(X)$ 后余项总含空谱逆的正幂。
本稿先将这两个有界一次项放进 $X',Z'$，才恢复了所需次数下降。

没有证明一般乘以 $e^w$ 保持任意 $H$ 向量的循环性。
论证只在已建立全部混合域的整基向量 $\xi$ 上进行，
且点态向量的 $L^2$ 可积性来自有限 Rademacher 矩与指数矩。
