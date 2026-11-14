# R578 — 全原临界边界消元、二 jet forcing 与固定极部

日期：2026-11-14。**状态：已证明。**
继续 R577 的同一个原 $\bar P$、临界整基准和完整修正。
原修正的低 $r$ 行可以用固定的实际列整可逆地消去；
其核也有显示的全来源分解。因此完整首次 forcing 化为两个长度
$s-13-r$ 的 jet 方程，未遗漏低角边界或任一其余原列。

此外，所有解的临界支在下一位具有同一个 Laurent 极部，
由原 carry 的首 $r$ 系数准确决定。这个极部给继续采用整临界支
基准的真实限制；它不是原 $d_2$ 非零定理。
同一个 $R$ 的两条十三行和 R577 的全部第三精度仍保留。
主目标未完成，R561 的原非零接口仍开。

## 1. 同一实际范围与固定低行

保 R577 全部假设和记号：
$$
\ell\in\{1,2\},\quad
\bar P\in\ker\bar J,\quad
\ell\le r=\nu\le2,\quad
n_0=s-13>r,\quad D<p.
\tag{1}
$$
$\mathcal O,\mathcal W_D,\mathcal E=Y\partial_Y,t(w),g(w),a$
均不变。$P^{\rm crit}$ 是 R577 的真整来源，
$\widetilde\psi$ 为其整临界支，令
$$
u=\widetilde\psi(0)\in\mathcal O^\times .
$$
仍有
$$
A=P^{\rm crit}|_{\widetilde\psi},\quad
B=(\mathcal E^2P^{\rm crit})|_{\widetilde\psi}
=t^r b(t),\quad b(0)\in\mathcal O^\times,
\quad \eta=\eta_0+p\xi .
\tag{2}
$$
本篇在支上用 $t$ 表示函数；原 carry 算子 $\mathscr S$ 始终先在
$w$ 中按 R577 定义作用，之后才用同一整逆 $w(t)$ 换参。

在原来源上定义整低行映射
$$
\mathcal L_{r,\ell}(R)=
\left(
R|_{\widetilde\psi}\bmod t^r,\
\mathcal ER|_{\widetilde\psi}\bmod t^r,\
\mathcal E^2R|_{\widetilde\psi}\bmod t^\ell
\right).
\tag{3}
$$
这里只去掉三个已知的单位标量 $1,a,a^2/2$；
没有改原 Gaussian 或目标长度。

原前三个权的角因子准确为
$$
q_0=q_1=1,\qquad q_2=(t-1)/(1+8t).
\tag{4}
$$
所以 $q_0,q_1,q_2$ 及 $\widetilde\psi$ 在原点均为单位。
对每个 $0\le j<r$，列
$$
t^jY^nq_n,\qquad n=0,1,2
\tag{5}
$$
都在原 $\mathcal W_D$：$r\le2$，其原次数帽足够，
而 (1) 的双临界条件本来已迫 $D\ge2$。

(5) 在三个同阶低行上的矩阵是
$\operatorname{diag}(q_n(0)u^n)$ 乘 $1,n,n^2$ Vandermonde，
行列式为单位。按 $t$ 阶排列后为单位块三角矩阵。
因此 (3) 整满射，并有只用这些固定实际列的整右逆。
这是物理低行的单位块；不是来源自由性替代全物理像饱和。

## 2. 低行核包含全部原剩余列

令
$$
\mathcal W_D^{(r)}
=\{R\in\mathcal W_D:t^r\mid d^{C_D}R\}.
\tag{6}
$$
这是清角后全局 $t$ 含量子格，不是自由系数共同含量 $\tau$。
它的来源商有限自由。由
$A_n=\lfloor(n+1)/4\rfloor$，
$$
\operatorname{rank}(\mathcal W_D/\mathcal W_D^{(1)})=3,
$$
$$
\operatorname{rank}(\mathcal W_D/\mathcal W_D^{(2)})
=6+m_D,\qquad m_D=\min(4,D-2).
\tag{7}
$$
第二式中 $D\ge2$。$n=0,1,2$ 各给两条系数，
$n=3,\ldots,\min(D,6)$ 各给一条，其余权已经含 $t^2$。
这里的来源余维至多十，不随 $D$ 增长。

为给 (3) 的核而不只给维数，设 $3\le n\le\min(D,6)$，
$$
\kappa_n=\left.(q_n/t)\right|_{t=0}=7(-1)^{B_n},
\qquad B_n=\lfloor(n+1)/3\rfloor .
$$
令 $L_{n,u}(Y)$ 为 $Y^n$ 在 $Y=u$ 的二次 Taylor 多项式：
$$
L_{n,u}(Y)=l_0+l_1Y+l_2Y^2,
$$
$$
l_0=\frac{(n-1)(n-2)}2u^n,\quad
l_1=n(2-n)u^{n-1},\quad
l_2=\frac{n(n-1)}2u^{n-2}.
$$
把它写回原三条实际列，
$$
\widehat L_{n,u}=l_0+l_1Y-l_2Y^2q_2(t),\qquad
Q_n=Y^nq_n-\kappa_n t\widehat L_{n,u}.
\tag{8}
$$
这些 $Q_n$ 全在原预算内，且
$$
Q_n=\kappa_n t\{Y^n-L_{n,u}(Y)\}\pmod{t^2}.
\tag{9}
$$
因为花括号在 $Y=u$ 有三重零，$Q_n$ 的三个支上 Euler jet
均在 $t^2$ 中。因此
$\mathcal L_{2,2}(Q_n)=0$，也有 $\mathcal L_{2,1}(Q_n)=0$。

当 $(r,\ell)=(2,1)$ 时还需保一条真实列
$$
Q_{\rm quad}=t(u^2-2uY-Y^2q_2(t)).
\tag{10}
$$
其最低项是 $t(Y-u)^2$，所以前两个支上 jet 在 $t^2$ 中，
第三个在 $t$ 中；它属于 $\ker\mathcal L_{2,1}$。
不能在 $\ell=2$ 时把它算进核。

于是有准确整直和：
$$
\boxed{
\begin{aligned}
\ker\mathcal L_{1,1}&=\mathcal W_D^{(1)},\\
\ker\mathcal L_{2,2}
&=\mathcal W_D^{(2)}
 \oplus\bigoplus_{n=3}^{\min(D,6)}\mathcal OQ_n,\\
\ker\mathcal L_{2,1}
&=\mathcal W_D^{(2)}
 \oplus\bigoplus_{n=3}^{\min(D,6)}\mathcal OQ_n
 \oplus\mathcal OQ_{\rm quad}.
\end{aligned}}
\tag{11}
$$

**证明。** (9)–(10) 已证明所列向量在核内。
模 $\mathcal W_D^{(2)}$ 后，逐个 $Q_n$ 的高权首系数为单位，
先唯一消去所有 $n=3,\ldots,\min(D,6)$ 的边界系数。
剩下的六条边界由 (5) 的三个 $2$-jet 整可逆控制。
若 $\ell=2$，没有剩余；若 $\ell=1$，唯一剩余由 (10)
的单位第三 $t$ 行给出。$r=1$ 时三条边界的 Vandermonde
本来可逆，核恰为 (6)。这同时证明直和、整性及约化保持。
没有遗漏可与低行抵消的其它原列。证毕。

## 3. 固定边界只由真实 carry 决定

R577 的首 forcing 是
$$
\mathcal F_P=
\left(
\overline{\pi_{n_0}A/p},\
\pi_{n_0}\overline{aB\xi+\mathscr SA},\
a\pi_\ell\overline{\mathscr S(B\eta_0)}
\right).
$$
因为 $A,B$ 被 $t^r$ 整除，低 $r$ 行中
$A/p$ 和 $B\xi$ 都为零。
定义准确的低 carry 多项式
$$
\alpha(t)=
\bigl(\overline{\mathscr SA}\bigr)(w(t))\bmod t^r,\qquad
\beta(t)=
\bigl(\overline{\mathscr S(B\eta_0)}\bigr)(w(t))
\bmod t^\ell.
\tag{12}
$$
它们来自同一个原 $A,\eta_0$，不由自由 $\xi$ 代替。

选择 $\alpha,\beta$ 的整多项式提升，并把 $\beta$ 在
$t^\ell,\ldots,t^{r-1}$ 的系数取零，记为 $\beta^\sharp$。
这是选定低行右逆，不是新增一个要求所有修正都满足的第三行。
置
$$
x_0=\frac{3\alpha-2\beta^\sharp}{2a},\qquad
x_1=\frac{2(\beta^\sharp-\alpha)}a,\qquad
x_2=\frac{\alpha-2\beta^\sharp}{2a},
$$
$$
\boxed{
R_{\rm bd}
=\sum_{i=0}^2
Y^iq_i(t)\,
\pi_r^t\left(\frac{x_i(t)}
{\widetilde\psi(t)^i q_i(t)}\right).
}
\tag{13}
$$
$\pi_r^t$ 为取 $t$ 次数 $<r$。
所有被取逆因子是单位，(13) 只用 (5) 的真实列。

Vandermonde 反解直接给
$$
R_{\rm bd}|_{\widetilde\psi}=0\bmod t^r,\qquad
\mathcal ER_{\rm bd}|_{\widetilde\psi}
=-\alpha/a\bmod t^r,
$$
$$
\mathcal E^2R_{\rm bd}|_{\widetilde\psi}
=-2\beta/a\bmod t^\ell.
\tag{14}
$$
所以它消去的正是原 forcing 的全部低行。

当 $r=\ell=1$ 时没有任何低边界自由度。
在剩余域中 $\bar u=1$，
(13) 就是同一原三列的明确组合
$$
\boxed{
\bar R_{\rm bd}
=\frac{3\alpha-2\beta}{2a}
+\frac{2(\beta-\alpha)}aY
-\frac{\alpha-2\beta}{2a}Y^2q_2(t).
}
\tag{15}
$$
这里 $\alpha,\beta$ 是原两个 carry 常数；
该组合不是任意选出的低阶示例。

## 4. 完整首次问题化成两个短 jet

记 $\mathcal K_{r,\ell}=\ker\mathcal L_{r,\ell}$，
其全部真实来源已由 (11) 列明。
定义整有限矩阵
$$
\boxed{
\mathcal D_\psi:\mathcal K_{r,\ell}
\longrightarrow
\left(\mathcal O[t]/t^{n_0-r}\right)^2,\qquad
R\longmapsto
\left(t^{-r}R|_{\widetilde\psi},\
t^{-r}\mathcal ER|_{\widetilde\psi}\right).
}
\tag{16}
$$
两个目标除法都由 (3) 的核条件实际保证。
特别 $Q_n$ 或 $Q_{\rm quad}$ 通常没有全局 $t^r$ 因子；
(16) 不是在来源中免费除 $t^r$。

将 R577 的前两 forcing 行去掉单位 $a$ 并用原整 $w(t)$
改写为 $t$-jet，记为
$$
f_0=\overline{A/p}\bmod t^{n_0},\qquad
f_1=\overline{B\xi+a^{-1}\mathscr SA}\bmod t^{n_0}.
$$
这些式子只在 R577 已付的截断范围读取。
由 (14)，下式的除法整且有唯一余类：
$$
\boxed{
\mathcal G_P=
-\left(
t^{-r}(f_0+\bar R_{\rm bd}|_\psi),\
t^{-r}(f_1+\mathcal E\bar R_{\rm bd}|_\psi)
\right)\bmod t^{n_0-r}.
}
\tag{17}
$$

**定理。** 原完整首次提升可解，当且仅当
$$
\boxed{\mathcal G_P\in\operatorname{im}\bar{\mathcal D}_\psi.}
\tag{18}
$$
若 $\bar S$ 解 (18)，同一个原修正可取
$$
R=R_{\rm bd}+S,\qquad S\in\mathcal K_{r,\ell}
$$
的整提升，且原第三块已经由 (13)–(14) 全部支付。

证明：任何原解的低行均为 (14)，所以它与 $R_{\rm bd}$
之差约化后在 (3) 的核；(11) 给该核的全部实际整提升。
减去 (14) 后，两条剩余高行准确就是 (16)–(17)。
反向按同一等式组合即可。此处既未丢掉边界核，
也未把核交与来源子格和擅自交换。

第二分量中的 $\xi$ 现在以
$-\, (B/t^r)\xi$ 出现，其系数仍为原单位。
它仍是原算术轴的固定函数，不能为满足 (18) 另选。
(18) 是完整实际像判据，不是已经证明其非零。

对 (6) 中的主体，也可用显示的有限自由“除去内容”呈示计算：
$$
t^{-r}\mathcal W_D^{(r)}
=
\bigoplus_{n=0}^D
Y^nq_n\,t^{m_n-r}\mathcal O[t]_{\le e_{n+1}-m_n},
\quad m_n=\max(r-A_n,0).
\tag{19}
$$
它仅是通过乘回 $t^r$ 识别原子格的计算呈示；
不把右侧误称为原 $\mathcal W_D$，也不增加中央条件。

## 5. 所有实际解共有的下一位极部

设 (18) 可解，并保取定的同一个 $R$。
在 $\mathcal O((t))$ 中，$B=t^r b$ 可逆。
对 $Q_2=P^{\rm crit}+pR$ 的临界分支作一次真实展开，
$$
\psi_{Q_2}=\widetilde\psi\exp(pv)\pmod{p^2}.
$$
由 $\mathcal EP^{\rm crit}|_{\widetilde\psi}=0$ 得
$$
\boxed{v=-\frac{\mathcal ER|_{\widetilde\psi}}B\pmod p.}
\tag{20}
$$
(14) 以及 (11) 对任意剩余修正均保持
$\mathcal ER|_\psi\equiv-\alpha/a\bmod t^r$。
所以 Laurent 极部准确为
$$
\boxed{
\operatorname{pp}_{t=0}(v)
=\operatorname{pp}_{t=0}\left(\frac{\alpha}{aB}\right).
}
\tag{21}
$$
它对 (18) 的所有解及任何再加的 $p^2$ 原修正都相同。

特别，存在与原 $\psi$ 同余的**整**临界支模 $p^2$，
准确等价于 $\alpha=0$ 于 $k[t]/t^r$。
当 $\alpha\ne0$，不能在下一位重新套用 R577 的整临界基准，
同时丢掉 (21)；原多项式来源和原 $M$ 提升本身并未因此被排除。

再加入任意原 $p^2S$，在同一个 Laurent 临界支上，
临界值的第三精度为
$$
\boxed{
(P^{\rm crit}+pR+p^2S)|_{\psi_{Q_3}}
=
A+pR|_{\widetilde\psi}
+p^2\left(
S|_{\widetilde\psi}
-\frac{(\mathcal ER|_{\widetilde\psi})^2}{2B}
\right)\pmod{p^3}.
}
\tag{22}
$$
二次项的符号由
$Bv^2/2+v\mathcal ER=-(\mathcal ER)^2/(2B)$ 给出。
因此第二精度系数的极部也固定：
$$
\boxed{
-\frac12\operatorname{pp}
\left(\frac{\alpha^2}{a^2B}\right).
}
\tag{23}
$$
(21) 与 (23) 不能混同：
$r=2$、$\operatorname{ord}\alpha=1$ 时前者可非零，
而后者已经没有极部。
Laurent 极部只限制临界坐标的整延拓；
未证明它是某条杀掉全部原列的 $C_2(M)$ 左行。

## 6. 原同一 R 的 carry 与真正第二障碍

实际修正始终是 (18) 的同一个
$R=R_{\rm bd}+S$。
回 R577 (18)–(24) 时，必须将此整个 $R$
沿原 $g$ 评价，保两条十三行高尾、原 $U_0$ 和初始自由行。
(16) 中的目标除法以及 (21) 的 Laurent 改写，
都不能替代原
$$
\left(
\overline{\frac{J_A(P^{\rm crit})+pJ_A(R)}{p^2}},\
\overline{\frac{J_B(P^{\rm crit})+pJ_B(R)}p}
\right)\in C_2(M).
$$
特别，R577 的
$\mathscr S(B\eta_0^2)/2$、
$\mathscr S^2(B\eta_0^2)/2$ 和三次正规混合项继续保留。

本篇付清了低行右逆和所有原剩余来源的准确范围，
并指出同一 carry 强制的极部；
未判定 (18) 的实际非零或其任一解的原第二障碍。
下一步须在 (11)、(16) 的这个完整来源上比较特定
$\mathcal G_P$，或把 (21)–(23) 接到真正全原左行，
不能只看源端自由度、局部极部或单个 unit。
