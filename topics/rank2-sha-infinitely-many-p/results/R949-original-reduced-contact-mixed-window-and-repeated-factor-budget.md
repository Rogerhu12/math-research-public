# R949 — 原四长一短的约化接触能量与真实重复因子预算

日期：2026-11-26；会话 Astra-rank2-Sha-7d29daa5-20261126。

**状态：下列同一原完整格上的有限不等式及重复因子必要条件已证明。**
本篇继续 R946，但不把已经被六重近根否定的十三倍常数用于任意重数。
对实际物理接触处的约化来源，四长 $S$、一短 $L$ 给准确的锐界
$10S+15\min(L,S/5)$；原十九角完整成本为 $3B_D^2+8D$。
这在显示的自然预算中排除约化的 $q=2$ 候选，迫其在物理点有真正的重复几何因子。
对任意重数，另外保留全部重复因子的自交与线性成本，给一个不删重数的有限必要式。

这些都是原首核的条件。没有从五个中央零制造深核，没有把局部模型当作原全局来源，
也没有把 R947 的扩大格免费代入旧十九角模型。

## 1. 原矩阵、真实长度和目标点

沿 [R946](R946-original-four-long-sharp-ten-root-energy-and-full-linear-cost.md)、
[R943](R943-original-e89-fifth-central-full-selmer-and-five-axis-gate.md) 的原 canonical 格
$\mathcal W_D=H^0(X,\mathcal O_X(B_D))$、十九角曲面和全部固定坏素数门。
取
$$
p=6s-1>211,\qquad N=s-13,\qquad1\le\ell<N,
\qquad f_D=\lfloor9D/2\rfloor+4<p,\quad D<p.
\tag{1}
$$
设非零 $\bar P\in\ker\bar M_5^{\rm orig}$，并用同一个单位角分母清理
$$
\widehat P=d^{C_D}\bar P,\quad
r=\operatorname{ord}_t\widehat P,\quad
M_D=f_D+C_D=5D+4-(D\bmod2).
\tag{2}
$$
R946 已证 $1\le r\le M_D$。因为 $\mathcal E=Y\partial_Y$ 与 $t,d$ 交换，
原完整物理首核的五行准确给
$$
(\mathcal E^i\widehat P)(t,g)\in t^N\quad(0\le i\le3),\qquad
(\mathcal E^4\widehat P)(t,g)\in t^\ell.
\tag{3}
$$
这里只采用已证明的物理窗口，不把三个长窗加一短窗改称四个长窗。
原前缀十三和全部五十二跨界成本继续在矩阵中保留。

若 $r\ge N$，只得到 R946 的简单有限界；以下设
$$
S=N-r>0,\qquad L=\max(0,\ell-r),\qquad
f=t^{-r}\widehat P.
\tag{4}
$$
于是 $0\le L\le S<s$。取同一低轴 $g\bmod t^s$ 的任意多项式延拓 $g_0$；
所有结果只读到 $s$，并不延长原 ODE。由于 $g_0$ 是单位，
Euler 到普通导数的单位下三角变换给
$$
\partial_Y^i f(t,g_0)\in t^S\quad(0\le i\le3),\qquad
\partial_Y^4 f(t,g_0)\in t^L.
\tag{5}
$$
第四普通导数的运输只用到已经深于 $L$ 的前三条导数；阶乘 $2,6,24$ 均为单位。

若同一 $\bar P$ 的非零 charge 差有公因数 $q$，$1\le q\le D<p$，则
$$
\widehat P(t,\zeta Y)=\zeta^{n_*}\widehat P(t,Y)
\quad(\zeta\in\mu_q).
\tag{6}
$$
所以 (5) 在所有不同的原物理单位点 $P_\zeta=(0,\zeta)$、轴 $\zeta g_0$ 上成立。
$q$ 是实际支持的公因数，不是可以任意增加的评价点数。

## 2. Gauss 下界与一个完整的整数计数恒等式

在任一 $P_\zeta$ 附近写 $X=Y-\zeta g_0(t)$。
去掉不经过该点的整单位后，tame Puiseux 分裂写成
$$
f(t,\zeta g_0+X)=U(t,X)\prod_{\alpha=1}^a(X-\alpha_\alpha(t))^{m_\alpha},
\qquad U(0,0)\ne0.
\tag{7}
$$
这里 $\alpha_\alpha$ 是不同根差，$m_\alpha$ 是真实重数。
原 $D<p$ 保分裂 tame；可选一个有限 Puiseux 扩张同时容纳所有根。
允许某根差恒为零。记
$$
h_\alpha=\operatorname{ord}_t\alpha_\alpha>0,\qquad
\bar h_\alpha=\min(h_\alpha,s),\qquad
d_{\alpha\beta}=\operatorname{ord}_t(\alpha_\alpha-\alpha_\beta).
\tag{8}
$$
根差恒为零时 $h_\alpha=\infty$；不同根之间的距离仍按真实差读取。
改变 $g_0$ 的 $t^s$ 以上项不改变所有 $\bar h_\alpha$ 或 $d_{\alpha\beta}$。

对实数 $x>0$，给 $X$ Gauss 权 $x$、给 $t$ 权一。
可先取有理 $x$，其余由连续性得到。
整单位 $U$ 的 Gauss 值是零；乘法性由非零首形式的乘积非零直接给出。
因此
$$
F(x)=\sum_\alpha m_\alpha\min(h_\alpha,x)
=\min_j\bigl(v_t([X^j]f)+jx\bigr).
\tag{9}
$$
(5) 使 $j=0,1,2,3$ 的系数赋值至少 $S$，$j=4$ 至少 $L$，
其余系数整。故
$$
\boxed{F(x)\ge G(x):=\min(S,L+4x,5x).}
\tag{10}
$$
这是完整 Gauss 多边形必要式；没有把未读高系数置零。

在 $0<x\le s$ 定义实际带重数根计数
$$
M(x)=\sum_{h_\alpha\ge x}m_\alpha,\qquad
F(x)=\int_0^xM(y)\,dy.
$$
对任意非负整数 $m$，有
$$
3m^2-2m=m+6\sum_{j\ge1}(m-j)_+.
\tag{11}
$$
求和只有有限项。对每个 $j\ge1$ 和 $0\le x\le s$，
$$
\int_0^s(M(y)-j)_+\,dy
\ge\int_0^x(M(y)-j)\,dy=F(x)-jx.
\tag{12}
$$
因此其左端至少为 $\sup_{0\le x\le s}(G(x)-jx)$。

置 $\lambda=\min(L,S/5)$、$H=(S-\lambda)/4$。
所有所需拐点 $\lambda,H$ 都在 $[0,S]\subset[0,s]$。
若 $L\le S/5$，$G$ 的斜率依次是五、四、零，拐点是 $L,H$；
由 (12)，$j=1,2,3$ 的三个下界为 $S-jH$，$j=4$ 的下界为 $L$。
又 $\int_0^sM\ge G(H)=S$。
若 $L\ge S/5$，$G=\min(S,5x)$，相应四个下界是 $S-jS/5$。
代入 (11) 并完整求和，两种情形统一给
$$
\boxed{\int_0^s(3M(x)^2-2M(x))\,dx
\ge10S+15\min(L,S/5).}
\tag{13}
$$
证明对达到或超过 $s$ 的接触同样成立；没有因截断漏掉最近根，也没有使用 $x>s$。

## 3. 约化物理接触的锐利能量

先假设 (7) 中经过每个 $P_\zeta$ 的实际根均有 $m_\alpha=1$。
这是对原几何非垂直分量重数的条件；不要求曲线在物理点只有一条分支。
其他不经过物理点的重复分量是单位因子，不影响此条件。

由 $d_{\alpha\beta}\ge\min(h_\alpha,h_\beta)$，
$$
\mathscr E_\zeta
:=\sum_\alpha\bar h_\alpha+
 6\sum_{\alpha<\beta}d_{\alpha\beta}
\ge\int_0^s\bigl(M(x)+6\binom{M(x)}2\bigr)\,dx.
$$
结合 (13)，得到
$$
\boxed{\mathscr E_\zeta\ge\Phi(S,L):=
10S+15\min(L,S/5).}
\tag{14}
$$
这与 R946§3.4 的六重反例没有冲突：该反例不满足本节的约化假设。

常数对这些局部条件是锐利的。当 $0<L<S/5$ 时，取
$$
f=X^5-t^LX^4-t^S.
$$
Newton 两段给四个接触 $(S-L)/4$ 的不同根及一个接触 $L$ 的根。
四个近根的首差分别是非零四次根，故两两距离为 $(S-L)/4$；
其余四个交叉距离为 $L$。前四行深 $S$，第四普通导数深 $L$。
于是能量恰为
$$
S+36(S-L)/4+24L=10S+15L.
$$
$L=0$ 时只留四个经过物理点的根，另一个是整单位，能量为 $10S$。
当 $S/5\le L\le S$ 时，取 $f=X^5-t^S$；
五根不同、接触和距离都为 $S/5$，第四普通导数恒为零，能量恰为 $13S$。
这些例子只证明局部界锐利，不宣称属于原十九角来源格。

## 4. 同一原十九角支付全部成本

记 $C_i$ 为原截面中经过至少一个 $P_\zeta$ 的实际几何整非垂直因子的严格变换。
在第3节假设下，每个这样的 $C_i$ 在原截面中恰出现一次。
沿 R680/R837/R946 的同一个已付 forcing 截面和完整判别式，有
$$
C_i\text{ nef},\qquad b_i=\deg_YC_i,\qquad
\sum_i b_i\le D,\qquad
B_D-\sum_iC_i\text{ 有效},
\tag{15}
$$
以及
$$
\sum_{\zeta}\left(
 \sum_{\alpha\in C_i}\bar h_\alpha+
 6\sum_{\substack{\alpha<\beta\\\alpha,\beta\in C_i}}
 d_{\alpha\beta}\right)
\le3C_i^2+L_{\rm pole}\cdot C_i,
\qquad L_{\rm pole}\cdot C_i\le8b_i.
\tag{16}
$$
跨两个不同因子的全部局部交叉和由真实交数 $C_iC_j$ 支付。
因此同一个有效 nef 类 $\mathscr C=\sum_iC_i$ 给
$$
\sum_{\zeta\in\mu_q}\mathscr E_\zeta
\le3\mathscr C^2+8\sum_i b_i
\le3B_D^2+8D.
\tag{17}
$$
最后一步使用 $B_D-\mathscr C$ 有效且 $B_D,\mathscr C$ 均 nef。
未使用第二份来源预算，未向原矩阵添加任何因子列。

**定理1。** 在 (1)—(6) 和第3节的实际约化接触条件下，
$$
\boxed{
q\left(10(N-r)+15\min\left((\ell-r)_+,\frac{N-r}5\right)\right)
\le3B_D^2+8D.
}
\tag{18}
$$
其中 $r<N$；$r\ge N$ 的情形仍按第1节单独处理。
所有 $s$ 截断、十九角、真实重数条件、固定前缀和线性极成本都已支付。

例如，若 $N>M_D$ 且
$$
q\left(10(N-M_D)+15\min\left((\ell-M_D)_+,
                  \frac{N-M_D}5\right)\right)>3B_D^2+8D,
\tag{19}
$$
则同一个原首核中没有满足约化接触条件的非零向量。
这是全有限参数的充分排除式，不需要先取极限；
其单调性只用 $r\le M_D$ 与 (14) 对两个变量分别单调。

## 5. 显示窗口内 q=2 必有实际重复因子

现在只讨论实际满足下列预算的一族参数：
$$
D\longrightarrow\infty,\qquad
\frac{\ell}{N}\longrightarrow x\in(0,1),\qquad
4N+\ell=\dim\mathcal W_D+o(D^2).
\tag{20}
$$
R946 的原十九角计数给
$$
\dim\mathcal W_D=\frac12B_D^2+O(D),\qquad
B_D^2=\frac{47}{12}D^2+O(D).
$$
因为 $r\le M_D=O(D)$，在 (20) 中
$$
\frac SN\to1,\quad \frac LN\to x,\qquad
N\sim\frac{B_D^2}{2(4+x)}.
\tag{21}
$$
原目标的固定十三行和平移五十二均只改变此处的固定项；
它们在有限不等式 (18)—(19) 中没有消失。

若实际 $q=2$ 且接触约化，(18) 与 (21) 必须满足
$$
10+15\min(x,1/5)\le3(4+x).
\tag{22}
$$
直接分两段比较，(22) 在且仅在本次需要的开区间
$$
\boxed{\frac16<x<\frac13}
\tag{23}
$$
内被严格反向违反。因此：

**推论2。** 对满足 (20)、(23) 的充分大参数，
每个 charge 差公因数为二的非零原五块首核向量，
必须有一个穿过物理单位点的几何整因子，以至少二重出现在原截面中。
只在别处有重复因子不能绕过这个结论。

例如可取 $x=1/5$。此时 $p/D^2\to235/84$，
约化接触的左侧总能量主项为 $(65/21)B_D^2$，
严格超过右侧 $3B_D^2$，余量为 $(2/21)B_D^2$。
与此同时，R946 的全部重数界 $10qS\le3B_D^2+80D$
在此区间排除 $q\ge3$：由 (21) 它要求 $q\le3(4+x)/5<3$。
所以剩余候选准确缩到 $q=1$，或带物理重复因子的 $q=2$。

这不证明中央必要系统已经产生一个首核，也不把这里的重复因子
自动识别成 R948 的指定 $F$。其零角、局部光滑性及全部源帽必须实际核对之后，
才可使用 R948 的相继限制或其它首次修正公式。

## 6. 任意重数的完整对角成本

还可保留全部重数，而不在需要时才删去重复层。
对 (7) 的真实 $m_\alpha$ 定义计数能量
$$
\mathscr V_\zeta=
 \sum_\alpha(3m_\alpha^2-2m_\alpha)\bar h_\alpha+
 6\sum_{\alpha<\beta}m_\alpha m_\beta d_{\alpha\beta}.
\tag{24}
$$
(11) 的逐高度恒等式与非阿基米德距离直接给
$$
\mathscr V_\zeta\ge\int_0^s(3M(x)^2-2M(x))\,dx
\ge\Phi(S,L).
\tag{25}
$$
这里的系数是用于证明的交数权，没有把一个重复根改成若干不同的实际根。

把所有有关实际几何因子写为 $C_i^{m_i}$，仍记 $b_i=\deg_YC_i$。
同一因子的每个局部分支都带相同 $m_i$。
置 $c_i=3m_i^2-2m_i\ge m_i^2$，
$\mathscr C_m=\sum_i m_iC_i$，故 $B_D-\mathscr C_m$ 有效且
$\mathscr C_m^2\le B_D^2$。
将 (16) 乘 $c_i$，其内部交叉系数 $6c_i$ 支付 (24) 所需的 $6m_i^2$；
不同因子之间仍用原 $6m_im_jC_iC_j$。
所以
$$
\begin{aligned}
q\Phi(S,L)
&\le3\sum_i c_iC_i^2+
 6\sum_{i<j}m_im_jC_iC_j+
 8\sum_i c_i b_i\\
&=3\mathscr C_m^2+
 6\sum_i m_i(m_i-1)C_i^2+
 8\sum_i(3m_i^2-2m_i)b_i.
\end{aligned}
$$
得到不删任何重数的有限必要界
$$
\boxed{
q\Phi(S,L)\le
3B_D^2+
6\sum_i m_i(m_i-1)C_i^2+
8\sum_i(3m_i^2-2m_i)b_i.
}
\tag{26}
$$
对重复项的第二个和不能无证写成 $O(D)$。
若另已知所有这些 $m_i\le M$，才可用
$\sum_i(3m_i^2-2m_i)b_i\le(3M-2)D$；
一般情形完整保留 (26)。

例如，在 (20)、$x=1/5$、$q=2$ 下，
若另已付 $\max_i m_i=o(D)$（固定重数上界是其特例），
末项才是 $o(B_D^2)$。此时 (26) 给准确必要条件
$$
\boxed{
\liminf_{D\to\infty}
\frac{\sum_i m_i(m_i-1)C_i^2}{B_D^2}\ge\frac1{63}.
}
\tag{27}
$$
因此在这个已注明重数范围内，不能只用一项自交可忽略的重复尾巴规避约化排除。
(27) 不给一般来源免费添加重数上界；未付该条件时仍使用 (26)。

## 7. 接续范围

本篇的新增内容是 (13)—(19) 的锐利混合窗、(23) 的约化 $q=2$ 排除，
以及 (26) 的实际重复因子预算。全部来自原完整来源与有限根接触；
没有新的数学执行、素数样本、生成系数或外部猜想。

后续须处理这些真实重复因子的完整来源帽和仿射修正，
并继续 $q=1$ 的一般有限类。R946§3.4 的任意重数反例保持，
R948 的全来源过滤保持，其明确前提不能从“出现某个重复因子”自动获得。
R947 的全部五源规范化、固定返回、实际导子费用也继续保持。
主目标的无穷通常全 Sha 有限尚未由这些首核必要条件证明。
