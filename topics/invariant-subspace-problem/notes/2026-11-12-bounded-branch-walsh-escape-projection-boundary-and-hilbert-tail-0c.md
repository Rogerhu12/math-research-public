# R198：有界一阶分支的高位 Walsh 逃逸、投影边界与普通 Hilbert 尾下界

日期：2026-11-12（UTC）。作者：root。

状态：完整实际证明。
本稿把未知有界一阶不变限制转化为一个强收敛的投影逃逸定理。
同一列高位 Walsh 酉算子对该一阶的所有有界不变分支同时有效，
并给出准确的交换子平方极限、一个分裂的 C* 边界及不依赖图范数的有限头尾下界。
结论没有排除任意慢尾分支，也没有将固定数量高位的渐近交换误用到增长数量的高位。

## 1. 设置

固定实际闭第一阶
$$
X=X_u,\qquad u=a_*+\sum_{j\ge0}a_j\chi_j,\qquad
a\in\ell^2\setminus\ell^1.
$$
使用 R125 的真实闭算子分解
$$
X=X_0+K,\qquad
X_0=\overline{a_*I+\sum_ja_jS_j},\qquad
S_j=I-2E_j,\qquad K\in B(H).
\tag{1.1}
$$
这里 $E_j=e_{10}^{(j)}$ 为物理位升算子。
记
$$
g=\|a\|_2,\qquad k=\|K\|.
$$
有限柱属于 $X$ 与 $X^*$ 的共同核心。
R161 给完整域等式及有界自交换子形式，特别：
若 $M\subset H$ 闭且 $A$ 不变，
$$
M\subseteq\operatorname{Dom}X,\qquad X|_M\in B(M),
\tag{1.2}
$$
则对某个有限 $L_M$，
$$
M\subseteq\operatorname{Dom}X^*,\qquad
\|X^*x\|\le L_M\|x\|\quad(x\in M).
\tag{1.3}
$$
例如可取 $L_M^2=\|X|_M\|^2+\|C_a\|$。
不要求 $X^*M\subseteq M$。

记满足 (1.2) 的全部闭不变空间为 $\mathcal B_X$，
包括零空间；$P_M$ 为其正交投影。
原问题中 monic 多项式核和相应 Bell 共振核属于这一类，
但本稿不预设这些核非零。

$\mathfrak U$ 为物理局部矩阵的 UHF 范数闭包，包含 $\mathcal A$。
记 $\mathscr H_m$ 为低 $m$ 位有限柱空间，$Q_m$ 为其正交投影。

## 2. 高位移动柱向量的统一实际误差

对有限 $J\subseteq[m,\infty)$，令
$$
U_J=M_{\chi_J},\qquad
\lambda_J=2\sum_{j\in J}a_j.
$$
$U_J$ 是自伴酉算子，且把有限柱映到有限柱。
物理单个位恒等式为
$$
\chi_jS_j\chi_j=2I-S_j.
$$
若 $v\in\mathscr H_m$，则 $S_jv=\chi_jv$ 对 $j\in J$ 成立。
所以在这个明确公共域上，
$$
(X-\lambda_J)U_Jv
=
U_JXv-2U_J\sum_{j\in J}a_j\chi_jv+[K,U_J]v.
\tag{2.1}
$$
不同 $\chi_jv$ 两两正交，故
$$
\boxed{
\|(X-\lambda_J)U_Jv\|
\le\|Xv\|+(2g+2k)\|v\|.
}
\tag{2.2}
$$
右侧与 $J$ 的大小和位置无关。
真实 carry 只进入已证明有界的 $K$，未被丢弃。
本式没有把任意无界算子的域交换推广到所有向量。

## 3. 同一列 Walsh 酉算子使所有有界分支投影消失

因为 $\sum_j|a_j|=\infty$，把复平面分为有限个角宽小于 $\pi$ 的扇区，
至少一个扇区内的模长和发散。
沿该扇区中心方向投影后，存在 $c>0$ 使所取项的实投影至少为 $c|a_j|$。
因此对每个 $m,n$，都能选有限
$$
J\subseteq[m,\infty),\qquad
\left|2\sum_{j\in J}a_j\right|\ge n.
$$

固定一次选取
$$
J_n\subseteq[n,\infty),\qquad
|\lambda_n|:=\left|2\sum_{j\in J_n}a_j\right|\ge n,\qquad
U_n=U_{J_n}.
\tag{3.1}
$$
这列只依赖 $a$，不依赖任何 $M\in\mathcal B_X$。

现固定 $M\in\mathcal B_X$，记 $P=P_M$、$L=L_M$。
(1.3) 意味着 $X^*P$ 是全域有界算子，范数不超过 $L$。
对 $z\in\operatorname{Dom}X$，伴随定义给
$$
PXz=(X^*P)^*z,\qquad \|PXz\|\le L\|z\|.
\tag{3.2}
$$
这是一个真实的域内恒等式；
没有要求 $PX$ 本身按原自然定义处处有定义。

对固定有限柱 $v$，充分大的 $n$ 使 $J_n$ 位于其头之外。
将 $P$ 作用到 (2.1)，使用 (3.2)，得到
$$
\boxed{
|\lambda_n|\,\|PU_nv\|
\le\|Xv\|+(L+2g+2k)\|v\|.
}
\tag{3.3}
$$
故 $PU_nv\to0$。
由于 $\|PU_n\|\le1$ 且有限柱稠密，延拓到全部固定向量：
$$
\boxed{P_MU_n\longrightarrow0\quad\text{强}.}
\tag{3.4}
$$
再乘左侧酉算子，得到
$$
\boxed{U_nP_MU_n\longrightarrow0\quad\text{强}.}
\tag{3.5}
$$
算子自伴，所以 (3.5) 亦为强* 收敛。

对每个固定 $M$，常数 $L_M$ 可以不同；
同一列 (3.1) 仍使全部 $M\in\mathcal B_X$ 各自满足 (3.4)—(3.5)。
这里不声称在所有分支上按 $L_M$ 一致收敛。

## 4. 交换子平方的准确强极限与最大非一致性

仍固定 $P=P_M$，置
$$
D_n=[P,U_n]=PU_n-U_nP.
$$
$P,U_n$ 自伴，直接相乘得
$$
D_n^*D_n
=P+U_nPU_n-PU_nPU_n-U_nPU_nP.
\tag{4.1}
$$
由 (3.5)，右侧除 $P$ 外各项强趋零。
因此
$$
\boxed{[P,U_n]^*[P,U_n]\longrightarrow P\quad\text{强}.}
\tag{4.2}
$$
等价地，对每个固定 $x\in H$，
$$
\boxed{\|[P,U_n]x\|\longrightarrow\|Px\|.}
\tag{4.3}
$$

投影与自伴酉算子的交换子范数不超过1。
确切地，相对于 $PH\oplus(I-P)H$，
它的两个非零块分别为 $PU_n(I-P)$ 和 $-(I-P)U_nP$，
二者互为负伴随，且各范数至多1。
若 $M\ne0$，取单位 $x\in M$，(4.3) 给
$$
\boxed{\|[P_M,U_n]\|\longrightarrow1.}
\tag{4.4}
$$

更强，对每个固定 $m$ 和每个 $x\in M$，
$$
\boxed{
\sup_{\substack{J\subseteq[m,\infty)\\J\ {\rm finite}}}
\|[P_M,U_J]x\|=\|x\|.
}
\tag{4.5}
$$
上界因为 $[P,U_J]x=-(I-P)U_Jx$；
下界用 (3.1) 中充分大的 $n$ 即得。

R164/R178 给每个固定高位数的 Walsh pattern 渐近交换，
而 (4.5) 说明在假设非零有界分支存在时，
这种结论不能统一扩张到所有高尾有限集合。
由于 $a_j\to0$ 而 $|\lambda_n|\to\infty$，必有 $|J_n|\to\infty$，
两类极限没有冲突。

若使用 R164 的 Calkin 忠实代数，
$P_M,U_n$ 及其交换子都属于该代数，
于是每个交换子的范数等于本质范数；
(4.4) 同时给本质范数趋于1。
这一附带结论不用于后面的证明。

## 5. 全部有界分支的共同 C* 边界

定义实际 C* 代数
$$
\mathfrak D_X
=C^*(\mathfrak U,\{P_M:M\in\mathcal B_X\}).
$$
高位 $U_n$ 最终与每个固定局部矩阵严格交换。
由局部矩阵的范数稠密性，
$$
\|U_nCU_n-C\|\to0\qquad(C\in\mathfrak U).
\tag{5.1}
$$
结合 (3.5)，对任意有限*多项式，
共轭强*极限等于固定 UHF 系数、将全部 $P_M$ 置零后的值。
乘法极限合法，因为每个有限词的因子统一有界。

强极限的范数下半连续性给置零映射的收缩性，
也给表达式无歧义性。
按范数闭包延拓，得到满的含单位*同态
$$
\boxed{
\Pi_X:\mathfrak D_X\longrightarrow\mathfrak U,\qquad
\Pi_X|_{\mathfrak U}=\mathrm{id},\quad
\Pi_X(P_M)=0.
}
\tag{5.2}
$$
对整个 $\mathfrak D_X$，
$$
\boxed{U_nTU_n\to\Pi_X(T)\quad\text{强*}.}
\tag{5.3}
$$
即使分支族不可数，每个稠密*多项式仍只使用有限个生成元，
所以这一延拓没有可数性缺口。

令 $\mathfrak I_X$ 是 $\mathfrak D_X$ 中由所有 $P_M$ 生成的闭双边理想。
显然 $\mathfrak I_X\subseteq\ker\Pi_X$。
商 $\mathfrak D_X/\mathfrak I_X$ 由 UHF 的像生成；
而 (5.2) 使这个像等距并有左逆，故商恰为 UHF。
因此
$$
\boxed{\ker\Pi_X=\mathfrak I_X,\qquad
\mathfrak I_X\cap\mathfrak U=\{0\}.}
\tag{5.4}
$$
这是一个由真实酉共轭实现的分裂 C* 扩张。
若没有非零有界分支，理想为零；本稿没有反过来证明该理想为零。

## 6. 有限个分支总像不能包含非零 UHF 的整像

取 $0\ne F\in\mathfrak U$，以及有限多个
$M_1,\ldots,M_d\in\mathcal B_X$。
则
$$
\boxed{\operatorname{Ran}F\not\subseteq M_1+\cdots+M_d.}
\tag{6.1}
$$

证明：设行算子
$$
R:H^d\to H,\qquad R(x_1,\ldots,x_d)=\sum_iP_{M_i}x_i.
$$
若范围包含成立，对每个 $x$ 选 $Fx$ 在 $(\ker R)^\perp$ 中唯一的最小范数原像 $Bx$。
这个全域线性映射图闭：
$x_n\to x$、$Bx_n\to y$ 时，$Ry=Fx$ 且 $y\perp\ker R$。
故闭图定理给 $B$ 有界，$F=RB$。
于是
$$
FF^*\le\|B\|^2RR^*=\|B\|^2\sum_iP_{M_i}.
$$
两侧属于 $\mathfrak D_X$。
施正的*同态 $\Pi_X$，得到 $FF^*\le0$，矛盾。

没有假定总像闭，也没有把一个代数和的闭包替换成它本身。
(6.1) 不排除某个有限和稠密但非闭。
更一般，以任意有限个 $\mathfrak I_X$ 元素的像代替 $M_i$，同一证明仍成立。

## 7. 不依赖伴随图尾的有限头 Hilbert 距离下界

本节只使用 $x$ 的普通 Hilbert 范数有限头逼近。
令
$$
A_m=\sum_{j<m}|a_j|,\qquad
b_m=L_M+|a_*|+3A_m+3g+3k.
\tag{7.1}
$$
对 $v\in\mathscr H_m$，由 $\|S_j\|<3$ 和高尾正交性，
$$
\|Xv\|\le(|a_*|+3A_m+g+k)\|v\|.
\tag{7.2}
$$
因此 (3.3) 的有限 $J$ 版本给
$$
\|P_MU_Jv\|
\le \frac{b_m}{2|\sum_{j\in J}a_j|}\|v\|.
\tag{7.3}
$$

沿用 R193 的有限集合代价
$$
r_a(m,t)=
\min\left\{|J|:J\subseteq[m,\infty)\text{有限},
\left|\sum_{j\in J}a_j\right|\ge t\right\}.
$$
非绝对可和性使它对每个正 $t$ 都有限。
取 $J$ 达到 $r=r_a(m,b_m)$，则 (7.3) 右侧不超过 $\|v\|/2$。

令
$$
T_J=\prod_{j\in J}V_j.
$$
R193 的实际不同位公式给
$$
T_Jv=U_Jv\quad(v\in\mathscr H_m),\qquad
\|T_J\|\le6^r,\qquad T_JM\subseteq M.
\tag{7.4}
$$
现在取单位 $x\in M$，置
$$
v=Q_mx,\qquad \epsilon=\|(I-Q_m)x\|,\qquad
\|v\|=\sqrt{1-\epsilon^2}.
$$
由 $T_Jx\in M$，
$$
\operatorname{dist}(U_Jv,M)
\le\|T_J(v-x)\|\le6^r\epsilon.
$$
另一方面，(7.3) 和正交投影给
$$
\operatorname{dist}(U_Jv,M)
\ge\frac{\sqrt3}{2}\|v\|.
$$
解这个实际不等式，得到
$$
\boxed{
\|(I-Q_m)x\|
\ge\frac{\sqrt3}{\sqrt{4\cdot6^{2r_a(m,b_m)}+3}}
\ge\frac12\,6^{-r_a(m,b_m)}.
}
\tag{7.5}
$$

(7.5) 不要求 $x\in\operatorname{Dom}\Lambda^{1/2}$，
不要求已知 $X^*(I-Q_m)x$ 的速度，
也不由一个图核心的无速率逼近推断任何速度。
其代价是所需的系数质量 $b_m$ 随有限头增长，
因此与 R193 固定阈值的图尾下界是不同的约束。

## 8. 交替幂尾的直接普通尾后果

取
$$
a_j=(-1)^j(j+1)^{-s},\qquad \tfrac12<s<1.
$$
有 $A_m\le C_s(m+1)^{1-s}$，因而
$b_m\le C_{M,s,a_*}(m+1)^{1-s}$。
在 $[m,C(m+1)]$ 中选全部偶数位。
积分比较给，增大固定 $C$ 后，
这些正项的和至少为 $b_m$，
而所取位数至多 $C'(m+1)$。
于是
$$
r_a(m,b_m)\le C'(m+1).
$$
(7.5) 给
$$
\boxed{
\|(I-Q_m)x\|\ge c_M e^{-C_M(m+1)}
\qquad(x\in M,\ \|x\|=1).
}
\tag{8.1}
$$
所以普通有限头尾若满足
$$
\|(I-Q_m)x\|\le C e^{-c(m+1)^t},\qquad t>1,
$$
则非零 $x$ 不属于任何这样的有界分支。
这里无需先证明它有任何次数算子图范数。

端点 $s=1$ 仍由 (7.5) 完整控制。
一个明确但不追求最优的量化为：$A_m\le1+\log(m+1)$，
取偶数位直到 $C(m+1)^8$，
其和至少为 $3\log(m+1)$ 加任意预定常数（增大 $C$）。
故 $r_a(m,b_m)\le C'(m+1)^8$，
并得普通尾下界 $c_Me^{-C_M(m+1)^8}$。
不能将这个粗端点界误写成 R193 的指数图尾界；
二者使用的范数与阈值均不同。

## 9. 剩余缺口

本稿给出的投影逃逸和准确交换子极限，
说明未知有界分支必须在增长数量的高位 Walsh 变换下极不稳定。
这并不与任何已证固定数量高位或规范 gauge 渐近交换冲突。

普通尾下界 (7.5) 与图尾下界一样，
仍允许任意慢的实际 Hilbert 尾。
共同 C* 理想 $\mathfrak I_X$ 若非零，是一个由这些未知投影生成的真理想；
没有从其与 UHF 零交推出它不存在。

原慢共振单核、一般限制像以及完整 Hilbert 不变子空间问题仍未解决。
本稿不把投影逃逸、有限总像障碍或快速尾排除类当作最终排核。
