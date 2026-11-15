# R648 — 原完整矩阵的带权旗标与全部 Smith 因子

日期：2026-11-15。**状态：已证明。**

本篇把 R646 的全列单射和有限指数界加强为全部 Smith 因子的准确分类。每一条原列先只除去它在原目标中已经具有的明确 $p$ 幂。这个辅助整矩阵的 Smith 因子只有 $1$ 和 $p$。因此，原矩阵的所有较高指数，准确由它的模 $p$ 核相对于原列权旗标的位置决定。

在一个显示的早阶条件下，该旗标交核的全部维数有只含原帽的有限求和式；原 $g/t/q_n/U_0$ 的高尾逐阶保留，并不会改变该式。这个条件在 $p\ge6101$ 时，对全部原范围 $f_D<p$ 自动成立，较小素数仍可使用本文的准确条件。

这里始终是完整 $\mathcal C_p$，没有把除列所得的辅助列赋予新的来源或中央零。旧三块 $M$、同 $R$ 的 $D_\psi^+$ 和旧 $d_2$ 均不由此替代。

## 1. 原列权与一个真正整的辅助矩阵

使用 [R646](R646-original-full-target-ramified-confluent-block-and-smith-bound.md) 的全部记号：
$$
p=6s-1>101,\qquad f_D=\lfloor9D/2\rfloor+4<p,
$$
$$
\mathcal W_D=\bigoplus_{n=0}^D
Y^nq_n(t)\mathcal O[t]_{\le e_{n+1}},
\qquad b_n=A_n+e_{n+1},\quad
A_n=\lfloor(n+1)/4\rfloor.
\tag{1}
$$
原完整矩阵 $M=M_{\mathcal C}$ 仍是
$$
\Phi(P)=c_*w^{13}U_0(w)e^{40a\epsilon}
P(t(w),g(w)e^{a\epsilon})
$$
在原 $\mathcal C_p$ 全标准基上的矩阵。原角因子、$P_{134}$、$U_0$ 及共同 charge 四十不变。

对每个原列 $(n,k)$，唯一写
$$
r_{n,k}=13+A_n+k=u_{n,k}+s j_{n,k},
\qquad 0\le u_{n,k}<s.
\tag{2}
$$
该列可准确分解为
$$
\Phi(Y^nq_nt^k)
=w^{r_{n,k}}V_{n,k}(w)e^{a(n+40)\epsilon},
\tag{3}
$$
其中 $V_{n,k}$ 为原 regular 单位，常数项为单位。它保留原 $t/w$、$q_n/t^{A_n}$、$g^n$ 和 $c_*U_0$ 的全部系数。

在原环中 $w^s=p\epsilon$，所以 (3) **真正整除** $p^{j_{n,k}}$，且其商是
$$
\boxed{
\Phi_0(n,k)
=w^{u_{n,k}}\epsilon^{j_{n,k}}
V_{n,k}(w)e^{a(n+40)\epsilon}\in\mathcal C_p.}
\tag{4}
$$
令 $M_0$ 由这些整列组成。于是准确有
$$
\boxed{M=M_0\operatorname{diag}(p^{j_{n,k}}).}
\tag{5}
$$
(4) 只用来计算同一个矩阵的 Smith 因子。它不是在原函数环中免费增加除以 $p$ 的来源，亦不增加任何算术中央条件。

## 2. 辅助矩阵只有单位与一次 p 因子

R646 取 $\pi^s=p$，并给原目标行的准确权
$$
\omega_m=m-s\lfloor6m/p\rfloor\in[1-s,s-1].
$$
其分歧辅助矩阵
$$
\mathsf A=\operatorname{diag}(\pi^{\omega_m})
M\operatorname{diag}(\pi^{-r_{n,k}})
$$
整且有整左逆。由 (2)、(5)，同一个矩阵也准确等于
$$
\mathsf A=\operatorname{diag}(\pi^{\omega_m})
M_0\operatorname{diag}(\pi^{-u_{n,k}}).
\tag{6}
$$
源权现在全在 $[0,s-1]$。

若 $P$ 为原整 primitive 向量且 $M_0P\in p^e\mathcal C_p$，
用 R646 的整左逆得到
$$
\operatorname{diag}(\pi^{u_{n,k}})P
\in\pi^{se+1-s}\mathcal O'^{N_D}.
$$
左边至少一个坐标的赋值不超过 $s-1$，故
$se+1-s\le s-1$，即 $e\le1$。R646 的全列单射同时适用于 $M_0$。所以：

**引理 1。** $M_0$ 的全部 Smith 因子都恰为 $1$ 或 $p$，没有零因子。

记原坐标格为 $\mathcal A=\mathcal O^{N_D}$，并置
$$
K=\ker(\bar M_0:\mathcal A/p\mathcal A\longrightarrow\bar{\mathcal C}_p).
\tag{7}
$$
在 $M_0$ 的有理像中取整饱和，拉回原坐标空间，得到
$$
\mathcal L=\{x\in\mathcal A\otimes K_0:M_0x\in\mathcal C_p\}.
$$
这里 $K_0=\operatorname{Frac}\mathcal O$，与 (7) 的核 $K$ 区分。
由引理 1，准确有
$$
\boxed{\mathcal L=\mathcal A+p^{-1}\widetilde K,}
\tag{8}
$$
其中 $\widetilde K$ 可取 $K$ 的任意整提升。改变提升只改变一个 $\mathcal A$ 元素，故右边与选择无关。这是实际物理像的饱和，由引理 1 支付，并非从来源自由性推得。

## 3. 一个一次饱和格与带权旗标的准确 Smith 引理

按原权 $j_{n,k}$ 定义
$$
F_J=\operatorname{span}_k\{\bar e_{n,k}:j_{n,k}\le J\},
\qquad F_{-1}=0,
$$
$$
c_j=\#\{(n,k):j_{n,k}=j\},\qquad
d_J=\dim_k(K\cap F_J),\qquad
\delta_j=d_j-d_{j-1}.
\tag{9}
$$

**引理 2。** 原矩阵 $M$ 的 Smith 指数准确为：

- 每个权 $j$ 有 $c_j-\delta_j$ 个指数等于 $j$；
- 同一权另有 $\delta_j$ 个指数等于 $j+1$。

等价地，指数 $e$ 的准确重数为
$$
\boxed{\mu_e=c_e-\delta_e+\delta_{e-1},}
\qquad c_e=\delta_e=0\text{ 于未出现的权},\quad\delta_{-1}=0.
\tag{10}
$$

**证明。** 令
$\mathcal D=\bigoplus\mathcal O\,p^{j_{n,k}}e_{n,k}$。
由 (5)、(8)，原矩阵的非零 Smith 因子等于格包含
$\mathcal D\hookrightarrow\mathcal L$ 的不变因子。

保持旗标 $F_J$ 的抛物群在具有固定数列
$\dim(K\cap F_J)$ 的子空间上可将 $K$ 化为坐标子空间。
具体做法是在每个 $K\cap F_J$ 中扩充前一层的基，
再在每层 $F_J$ 扩充为全基。所得基变换保持全部 $F_J$。
它可提升为一个整可逆矩阵，且保持 $\mathcal D$：
按权递增分块，取保持旗标的块上三角提升；从较高权列到较低权行的任意系数均保 $\mathcal D$，反向块取零，块对角为整单位。

因此，在一个同时保持 $\mathcal A,\mathcal D$ 的整基中，
$K$ 每权恰占 $\delta_j$ 个坐标。
(8) 说明这些坐标在 $\mathcal L$ 中的基是 $p^{-1}e$，
其余仍是 $e$。
于是 $p^j e\in\mathcal D$ 对前者给指数 $j+1$，
对后者给指数 $j$，正是 (10)。
目标有理像外的自由余核不改变这些因子。证毕。

这也说明为什么只知道 $\dim K$ 不够：它在原权旗标中的准确位置才决定全部高指数；但不需要在 (8) 之外再补一个未定的二阶延拓。

## 4. 原全部 regular 高尾的模 p 形状

原第二盘界保证 $V_{n,k}$ 的系数满足 R646 使用的估计
$$
v_p(v_l)\ge-\lfloor6l\tau_2\rfloor,\qquad
\tau_2=\frac{2p-1}{p(p^2-1)}.
$$
在原单指数基中，第 $l$ 项的系数是
$v_l p^{\lfloor6l/p\rfloor}$。
若 $l\ge s$，记 $q=\lfloor6l/p\rfloor\ge1$；则
$$
6l\tau_2<(q+1)p\tau_2<q\qquad(p>101).
$$
故其赋值至少为一。由此整个原 regular 单位准确满足
$$
\boxed{\bar V_{n,k}\in k[w]/w^s,\qquad \bar V_{n,k}(0)\ne0.}
\tag{11}
$$
这里只对同一完整目标取模 $p$；高尾在整矩阵 (4) 中仍保留。

R633 已证明 $k[w,\epsilon]$ 在 $\bar{\mathcal C}_p$ 中的实际像为
$$
\mathscr B=k[w,\epsilon]/\langle w^u\epsilon^h:6u+h\ge p\rangle.
\tag{12}
$$
所以 (4) 的整个模 $p$ 像都在该真子空间中。
以 $u$ 递增排列 (12) 的行，固定 $u$ 有
$$
h_u=p-6u,\qquad0\le u<s
\tag{13}
$$
条行。原列的首块为
$$
\lambda_{n,k}\epsilon^{j_{n,k}}
e^{\bar a(n+40)\epsilon}\pmod{\epsilon^{h_u}},
\tag{14}
$$
其余 $\bar V_{n,k}$ 系数只进入更大的 $u$。
$w^s=0$ 在此模 $p$ 子空间中成立，所以不会在这个阶段绕回较低 $u$。
这支付真实块三角性，而不是把 $q_n/g/t$ 高尾删去。

## 5. 早阶门下，全部旗标交核有准确求和式

保 R633 的原角阶计数
$$
m_r=\#\{n:A_n\le r\le b_n,\ 0\le n\le D\},
\qquad m_r=0\text{ 若 }r<0.
$$
定义
$$
N_{u,J}=\sum_{j=0}^J m_{u+js-13}.
\tag{15}
$$
这是权 $\le J$ 的真实列在首块 $u$ 中的数目；没有将不存在的角列补入。

令
$$
u_*=A_D+13,\qquad
C_u=\sum_{n=0}^D
\left(1+\left\lfloor\frac{b_n+13-u}{s}\right\rfloor\right)_+ .
$$
本文的明确早阶门是
$$
\boxed{
C_u\le p-6u
\quad\text{对全部 }0\le u<\min(u_*,s).
}
\tag{E}
$$

**定理 1。** 在 (E) 下，对全部 $J\ge0$，
$$
\boxed{
d_J=\sum_{u=0}^{s-1}(N_{u,J}-h_u)_+.
}
\tag{16}
$$
将 (16) 代入 (9)–(10)，即得到原 $M_{\mathcal C}$ 全部 Smith 因子的准确分类。

**证明。**
当 $u<u_*$ 时，同节点的低 $j$ 可能不在原帽内。
R646 用于独立性证明的补齐合流族有 $C_u$ 列。
(E) 使这整个补齐族已经在首 $h_u$ 行独立，
所以原任一权前缀的实际首块均全列独立，
且 $N_{u,J}\le h_u$。这里只证明原列独立，不把补齐列当作可用来源。

当 $u\ge u_*$ 时，
$13+A_n\le u$ 对所有 $n$ 成立。
故固定节点的实际权准确是
$j=0,\ldots,\min(J,\lfloor(b_n+13-u)/s\rfloor)$，
原族本身就是完整合流族。
R646 已付 $C_u\le p$，节点及所有阶乘均为单位。
因此其首 $h_u$ 行秩恰为 $\min(N_{u,J},h_u)$。

还须付全部高尾的可解性，不能只把首块秩相加。
在这个后半段，原 $r=u+js-13\ge A_D$，
所以 $m_r=\#\{n:b_n\ge r\}$。
原 $b_n$ 严格递增，故 $m_{r+1}\ge m_r-1$。
又由原十二余类直接给 $3A_D+B_D-C_D\ge0$，故 $e_{D+1}\le f_D<p<6s$，
$$
r_{\max}=13+b_D=u_*+e_{D+1}<u_*+6s.
$$
所以 $u\ge u_*$ 时最多出现 $j=0,\ldots,5$ 六个层。
于是
$$
N_{u+1,J}\ge N_{u,J}-6,\qquad h_{u+1}=h_u-6,
$$
从而 $N_{u,J}-h_u$ 在后半段不减。

因此，在第一次 $N_{u,J}\ge h_u$ 以前，所有原首块全列独立；
一个全核向量的这些系数逐阶被迫为零。
从第一次达到该不等式起，每个后续首块都全行满射。
此前选择的自由系数通过 (11) 产生的全部高尾成为已知右端，
可用后续同一原块的单位主元逐阶解掉。
每阶恰留下 $N_{u,J}-h_u$ 个自由参数，没有遗漏末端行。
这证明 (16)。证毕。

特别，这个证明保持同一个真实列组合贯穿所有 $u$；
没有把不同阶段的修正各自独立选择后相加。

## 6. 早阶门在全部充分大素数范围自动成立

本节给无需逐 $D$ 验证 (E) 的一个明确充分范围：
$$
\boxed{p\ge6101,\quad f_D<p\quad\Longrightarrow\quad(E).}
\tag{17}
$$
这个常数只为完整统一门，不声称最优。

R646 已付
$b_n\le25n/6+16/3$。若 $b_n+13\ge u+js$，则
$$
n\ge\frac{6u+j(p+1)-110}{25}.
$$
置
$$
D^\flat=\frac{2(p-4)}9,\qquad
U^\flat=\frac{D^\flat+1}{4}+12=\frac{2p+433}{36}.
$$
原 $D<D^\flat$，且 (E) 所需 $u\le A_D+12\le U^\flat$。
按各 $j$ 计数并仅放松为实数，得
$$
C_u\le B(u):=
\sum_{j\ge0}
\left(D^\flat+1-
\max\!\left(0,\frac{6u+j(p+1)-110}{25}\right)\right)_+.
\tag{18}
$$
当 $p\ge6101$ 时，$j\ge6$ 的项即使在 $u=0$ 也为零。
因此 $B(u)+6u$ 在 $u\ge0$ 上分段线性且递增：
每个非恒定项的斜率至多损失 $6/25$，总共最多六项，
总斜率至少 $6-36/25>0$。

在 $u=U^\flat$，六个 $j=0,\ldots,5$ 的内层数全为正，
且外层亦全为正；直接求和得到
$$
B(U^\flat)=\frac{49p+686}{75}.
$$
所以
$$
\begin{aligned}
p-6u-C_u
&\ge p-6U^\flat-B(U^\flat)\\
&=\frac{2p-12197}{150}>0
\qquad(p\ge6101).
\end{aligned}
$$
这证明 (17)，包括所有原 $D$，没有用素数样本推断。
较小素数只需保持 (E) 的准确有限不等式；本文不预设它自动成立。

## 7. 与原首 Bockstein 数目的核对及范围

(16) 的 $J=0$ 给真正单位块损失；把 $j\ge1$ 的原列全部计入，
(10) 的指数零、一次和至少二的数目分别恢复 R620/R633 的原公式。
尤其在两篇条件同时成立时，
$$
\#\{e=0\}=N_D-k_m,\qquad
\#\{e=1\}=k_m-\kappa_D,\qquad
\#\{e\ge2\}=\kappa_D.
$$
这里不再把最后一项混入零方向。本文还用全部 $d_J$ 将它准确细分到各个指数。

对 $p\ge6101$，全部原范围中指数至多六；
各个指数的数目只需原 $b_n,A_n$ 的整数计数。
这并不意味着原 higher forcing 与 $g$ 无关：
结论限于完整目标的 Smith 型，完整像本身、具体来源向量和旧短目标余类仍依赖原全部系数。

R637 仍需要在旧三块及两组十三行内比较同一个实际修正 $R$。
本篇的合流行和辅助 $p$ 除列都不能作为旧问题中的免费新来源；
也没有把原两条或三条完整中央失败传播到任意乘积。
