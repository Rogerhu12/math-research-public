# R147 附录：任意可和慢辅助的首位切片消元与全部幂循环性

日期：2026-11-13（UTC）。作者：kernel；提交 Astra-ISP-1cf8c51d 复核。
状态：完整证明。使用 R144/R147 的一变量消元方法，但允许任意有限个慢 $\ell^1$ 辅助模式及任意次数的点态耦合。主行只要求复 $\ell^2$，没有空谱、熵、弱 $\ell^1$ 或辅助快尾假设。一般 Hilbert ISP 仍未完成。

## 1. 两个一变量切片的充分判据

取
$$
u=a_*+\sum_{j\ge0}a_j\chi_j,\qquad a\in\ell^2(\mathbb C),\quad a\ne0,
$$
以及有限个辅助 first
$$
v_\nu=c_{\nu,*}+\sum_{j\ge0}c_{\nu j}\chi_j,\qquad
c_\nu\in\ell^1(\mathbb C),\qquad 1\le\nu\le d.
\tag{1.1}
$$
所有支撑可以任意重叠，系数相位任意。常数辅助模式允许。
记实际全零物理位锚
$$
\beta_\nu=v_\nu(0)=c_{\nu,*}+\sum_jc_{\nu j},\qquad
\beta=(\beta_1,\ldots,\beta_d).
\tag{1.2}
$$

另取任意共同指数权
$$
w=b_*+\sum_jb_j\chi_j,\qquad b\in\ell^2(\mathbb C).
\tag{1.3}
$$
令联合首位和该位系数为
$$
j_0=\min\{j:|a_j|+\sum_\nu|c_{\nu j}|>0\},\qquad h=2^{j_0},
$$
$$
a=a_{j_0},\qquad c=(c_{1j_0},\ldots,c_{dj_0}),\qquad
\tau=e^{-2b_{j_0}}\ne0,\qquad d_0=W_h.
\tag{1.4}
$$
本稿中的单个 $a$ 表示这个首位系数；它可以为零，因为最早非零位可能来自辅助模式。

给定
$$
F(U,V)=\sum_{k=0}^p U^k r_k(V),\qquad p\ge1,
\tag{1.5}
$$
其中 $r_k$ 为标量多项式，并假设
$$
\boxed{r_p(\beta)\ne0.}
\tag{1.6}
$$
定义两个真正的一变量标量多项式
$$
p_0(z)=F(z,\beta),\qquad
p_1(z)=F(z-2a,\beta-2c).
\tag{1.7}
$$

**定理 1.1。** 若
$$
\boxed{\gcd_{\mathbb C[z]}(p_0,p_1)=1,}
\tag{1.8}
$$
则
$$
\boxed{F(u,v_1,\ldots,v_d)e^w\text{ 非零且对原 }A\text{ 循环}.}
\tag{1.9}
$$
允许 $p_0,p_1$ 各自有重根；第二个切片的次数也可以降低。
指数权只在证明中贡献非零因子 $\tau$，不改变 (1.8)。

这里先将全部辅助模式化为真实有界算子，才在剩下的一个闭 first 变量上使用有限自由模。
(1.8) 不是多个独立无界变量的互素判据。

## 2. 与既有范围的关系

无辅助模式时，(1.8) 就是 R144/R147 的 $q(z)$ 与 $q(z-2a)$ 互素判据。

R155 在主 first 空谱时已允许任意 $\ell^1$ 辅助，只需 (1.6)，并不需要 (1.8)。本文真正增加的是不具空谱的主行，例如 R138 的全平面连续谱分支，以及居中有界主行中的相应切片范围。

R154、R157 和 R270 第五附录分别有快模式或快辅助要求；本文辅助尾可以任意慢。
R186 已给一般多模式点态式的有限 gauge 联合循环；本文在 (1.8) 下排的是单个实际闭核。
本文不重复这些旧闭图定理，也不把其联合循环结论当作单向量循环。

二次情形包含 R236 的首偏离不晚于首主位定理；同样，[R236 全阶共振加偏离的字符互素判据](R236-appendix-real-dyadic-factor-character-coprimality-and-all-order-deviations.md)还原为本稿的相应两个切片，见 §8.4。两项已发表范围均不重复登记。本文保留的是一般非线性有界辅助耦合，以及对每个允许平移的全部点态幂。

## 3. 有界辅助、共同指数权与真实 Bell 自然域

使用 R176/R186 的实际倾斜局部算子
$$
R_j(b)=V(e^{-2b_j}N_j)
=(I-e^{-2b_j}N_j)(I+e^{-2b_j}N_j)^{-1}.
$$
它们一致有界，属于 $\mathcal A$，字符为 $1$。
取真实倾斜闭 first
$$
X=X_{u,b}.
$$
R176 给 $\operatorname{Dom}X^k$ 的全部自然幂域、伴随核心及有界交换子域交换。
共同指数向量
$$
\xi=e^w
$$
循环，并属于这些全部自然幂域。

辅助的真实倾斜 first 为
$$
Z_\nu=c_{\nu,*}I+\sum_jc_{\nu j}R_j(b)
\in\mathcal A_h:=\overline{\mathbb C[I,A^h]}^{\|\cdot\|}.
\tag{3.1}
$$
级数按算子范数绝对收敛，且
$$
\chi(Z_\nu)=\beta_\nu.
\tag{3.2}
$$
所有这些有界算子保持全部 $\operatorname{Dom}X^k$。

为保留全部重叠修正，写参数为 $(s,t_1,\ldots,t_d)$，置
$$
\ell_j(s,t)=s a_j+\sum_\nu t_\nu c_{\nu j},
$$
$$
\mathcal B_b(s,t)=
\prod_j e^{-\ell_j(s,t)R_j(b)}
\bigl(\cosh\ell_j(s,t)I+R_j(b)\sinh\ell_j(s,t)\bigr).
\tag{3.3}
$$
R145/R186 的一阶消去与平方和预算给 $\mathcal A$ 值范数整单位函数；
在任意参数紧集上，尾因子为 $I+O(|\ell_j|^2)$，逆有同阶预算。
低于 $j_0$ 的因子严格等于 $I$，故
$$
\mathcal B_b(s,t)\in\mathcal A_h.
$$
记
$$
B_{k,\alpha}=\partial_s^k\partial_t^\alpha\mathcal B_b(0,0).
$$
则
$$
B_{0,0}=I,\quad B_{1,0}=0,\quad B_{0,e_\nu}=0,\qquad
\chi(B_{k,\alpha})=0\quad(k+|\alpha|>0).
\tag{3.4}
$$

R186 §10 已通过各通常伴随的有限柱图核心逐阶证明共同自然 jets。
保持完整 $w$ 固定、只截断主／辅助模式时，有限恒等式为
$$
\mathcal B_{b,N}(s,t)^{-1}
e^{w+s u_N+\sum_\nu t_\nu v_{\nu,N}}
=e^{sX_N+\sum_\nu t_\nu Z_{\nu,N}}\xi.
$$
其全部固定阶导数强收敛；伴随核心识别每个混合自然词，辅助有界则把所需域化为主模式的 $\operatorname{Dom}X^p$。
因此准确有
$$
F(u,v)e^w=P(X)\xi,
\tag{3.5}
$$
其中
$$
\boxed{
P(z)=\sum_{k,\alpha}
\frac{B_{k,\alpha}}{k!\alpha!}
(\partial_U^k\partial_V^\alpha F)(z,Z_1,\ldots,Z_d)
\in\mathcal A_h[z].
}
\tag{3.6}
$$
和是有限的；它包含全部纯辅助和混合 Bell 项。
按字符取值得
$$
\chi(P(z))=p_0(z).
\tag{3.7}
$$

其最高 $z^p$ 系数准确为
$$
L=\sum_\alpha\frac{B_{0,\alpha}}{\alpha!}
(\partial^\alpha r_p)(Z_1,\ldots,Z_d).
\tag{3.8}
$$
所以
$$
\chi(L)=r_p(\beta)\ne0.
$$
$\mathcal A_h$ 的唯一字符性质使 $L$ 为该代数中的真实单位。
特别，最高系数一般不是未经 Bell 修正的 $r_p(Z)$。

R176 的最高系数单位定理因此适用：
$$
T=P(X),\qquad\operatorname{Dom}T=\operatorname{Dom}X^p
\tag{3.9}
$$
是实际闭、稠密定义、原空间 $C$ 自伴的算子。
$\xi$ 的多项式轨道是图核心，且
$$
[\,F(u,v)e^w\,]_A=\overline{\operatorname{Ran}T}.
\tag{3.10}
$$

## 4. 首位形式系数：辅助位移和指数因子均保留

记 $c_h$ 为 R32 的真实连续形式系数映射。
在最低联合位，
$$
R_{j_0}(b)=I-\frac{2\tau}{d_0}A^h+O(A^{2h}).
\tag{4.1}
$$
这里及本节的 $O(A^{2h})$ 只表示正式系数计算；后文实际有界除法另证。

对局部函数
$$
H(\ell,R)=e^{-\ell R}(\cosh\ell+R\sinh\ell)
$$
直接在 $R=1$ 展开，得到
$$
c_h\bigl(H(\ell,R_{j_0}(b))\bigr)
=\frac{\tau}{d_0}(e^{-2\ell}-1+2\ell).
\tag{4.2}
$$
其他非平凡物理位从 $2h$ 或更高阶开始。
范数整收敛及形式系数连续性允许取极限和参数导数，因此
$$
c_h(\mathcal B_b(s,t))
=\frac{\tau}{d_0}
\left[
e^{-2(sa+t\cdot c)}-1+2(sa+t\cdot c)
\right].
\tag{4.3}
$$
特别，当 $k+|\alpha|\ge2$，
$$
c_h(B_{k,\alpha})
=\frac{\tau}{d_0}(-2)^{k+|\alpha|}a^k c^\alpha.
\tag{4.4}
$$
同时由 (3.1)，
$$
c_h(Z_\nu)=-\frac{2\tau c_\nu}{d_0}.
\tag{4.5}
$$

在 (3.6) 中，首形式阶只有两种贡献：$B_{0,0}=I$ 项中的有界辅助变化，
以及其余 $B_{k,\alpha}$ 的首项。两个正阶因子相乘不会贡献 $h$ 阶。
有限 Taylor 公式于是给
$$
\boxed{
c_h(P(z))
=\frac{\tau}{d_0}
\left[
p_1(z)-p_0(z)+2a\,p_0'(z)
\right].
}
\tag{4.6}
$$
辅助的一阶 Taylor 项在 (4.4) 的二阶以上和与 (4.5) 之间准确抵消。
式 (4.6) 的 $p_1$ 必须包含整个 $\beta-2c$，不能只平移主变量。

## 5. Gauge 差的实际有界 $A^h$ 因子

固定 dyadic $\zeta$，假设 $\zeta^h\ne1$。
R176 的完整域恒等式给
$$
U_\zeta XU_\zeta^*=X+D_\zeta,\qquad
U_\zeta\operatorname{Dom}X^n=\operatorname{Dom}X^n.
\tag{5.1}
$$
$D_\zeta$ 是有限真解析和，只改变满足 $\zeta^{2^j}\ne1$ 的有限低位。
其首阶至少为 $h$，且
$$
D_\zeta=A^h d_\zeta(A),\qquad
c_h(D_\zeta)=-\frac{2\tau a}{d_0}(\zeta^h-1).
\tag{5.2}
$$
$a=0$ 时这个首系数为零，不影响实际因式分解。

对任意 $E\in\mathcal A_h$，R124 的真实有限余数分解（R139 引理 1.1 使用同一计算，下面也明确包括 $h=1$）给
$$
\gamma_\zeta(E)-E=A^h E_\zeta,\qquad E_\zeta\in\mathcal A_h.
\tag{5.3}
$$
具体地，若 $\zeta$ 的阶为 $N>h$，将 $E$ 写成实际有限分解
$$
E=\sum_{r=0}^{N/h-1}A^{rh}E_r,\qquad E_r\in\mathcal A_N.
$$
零余数在差中消失，其他有限项都可提取 $A^h$。
这是真正的有界分解，并非从零字符猜测可除 $A^h$。

定义
$$
P_\zeta(z)=(\gamma_\zeta P)(z+D_\zeta).
\tag{5.4}
$$
由 (5.1)，在整个自然 $\operatorname{Dom}X^p$ 上
$$
P_\zeta(X)=U_\zeta T U_\zeta^*.
\tag{5.5}
$$
(5.2)、(5.3) 及有限差幂展开给
$$
\boxed{
P_\zeta(z)-P(z)=A^h J_\zeta(z),\qquad
J_\zeta\in\mathcal A_h[z],\quad \deg J_\zeta\le p.
}
\tag{5.6}
$$

现在才取差商的字符。
由 (4.6)，系数 gauge 差的首项是
$(\zeta^h-1)c_h(P(z))$；
主变量位移的首项是
$c_h(D_\zeta)p_0'(z)$。
两项中的导数准确抵消：
$$
\boxed{
\chi(J_\zeta(z))
=\frac{\tau(\zeta^h-1)}{d_0}
[p_1(z)-p_0(z)].
}
\tag{5.7}
$$
这就是所需的两个一变量切片。共同指数权留下 $\tau\ne0$，不会改变互素性。

## 6. 最高系数单位与真实有限 Bézout 证书

由 (1.8)、(3.7)、(5.7)，
$$
\gcd\bigl(\chi(P),\chi(J_\zeta)\bigr)=1.
\tag{6.1}
$$
$P$ 的最高系数 $L$ 是真实 $\mathcal A_h$ 单位，所以
$$
\mathcal A_h[z]/(P)
$$
是以 $1,z,\ldots,z^{p-1}$ 为基的自由 $\mathcal A_h$ 模。
可先用 $L^{-1}P$ 作首一长除法，其生成理想与 $(P)$ 相同。

乘以 $J_\zeta$ 的线性映射由 $p\times p$ 的 $\mathcal A_h$ 矩阵表示。
取字符后，它是在 $\mathbb C[z]/(p_0)$ 中乘以 $\chi(J_\zeta)$，
由 (6.1) 可逆。
所以矩阵行列式字符非零，因而是 $\mathcal A_h$ 单位；
伴随矩阵给真实有界系数逆。

将逆作用于常数类，得到
$$
\alpha_\zeta(z)P(z)+\beta_\zeta(z)J_\zeta(z)=1,
\tag{6.2}
$$
其中 $\deg\beta_\zeta\le p-1$；
因 $\deg J_\zeta\le p$，可取 $\deg\alpha_\zeta\le p-1$。
系数都属于 $\mathcal A_h$。

乘以 $A^h$ 并用 (5.6)，得到完整有界系数消元式
$$
\boxed{
A^h=(A^h\alpha_\zeta(z)-\beta_\zeta(z))P(z)
+\beta_\zeta(z)P_\zeta(z).
}
\tag{6.3}
$$
这里只使用 $P$ 与对应的同一个 $P_\zeta$。
没有用多变量互素替代单位理想，也没有把多个不同 gauge 的核当作同一个配对目标。

## 7. 全部深定义域中的跨核配对与排核

反设 $M=\ker T\ne0$。它闭且 $A$ 不变。
取基础 first 的固定正则器 $R=R(t)$；
R140/R183 的参数单位关系及 R88 给
$$
R^nH\subseteq\operatorname{Dom}X^n,\qquad
\overline{R^nM}=M\quad(n\text{ 固定}).
\tag{7.1}
$$
倾斜只是有界交换扰动，故同一个正则器适用。
它与 $T$ 完整域交换，因此 $R^nM\subseteq M$。

对固定 $\zeta^h\ne1$，取
$$
f\in R^{2p}M,\qquad g\in U_\zeta R^{2p}M.
$$
(5.1)、(5.5)、(7.1) 给
$$
f,g\in\operatorname{Dom}X^{2p},\qquad
P(X)f=0,\qquad P_\zeta(X)g=0.
\tag{7.2}
$$
(6.3) 中所有词的次数至多 $2p-1$，均在这些真实域上有定义。
有界系数保持全部自然幂域并与 $X$ 交换；它们与 $X$ 都对原双线性配对
$$
\mathcal B(f,g)=\int_{\mathbb Z_2} f(y)g(-1-y)\,d\mu(y)
$$
对称。因此
$$
\begin{aligned}
\mathcal B(A^h f,g)
&=\mathcal B(P_\zeta(X)\beta_\zeta(X)f,g)\\
&=\mathcal B(\beta_\zeta(X)f,P_\zeta(X)g)=0.
\end{aligned}
\tag{7.3}
$$
这里 $\beta_\zeta(X)f\in\operatorname{Dom}X^p$，
由 $f\in\operatorname{Dom}X^{2p}$ 及 $\deg\beta_\zeta\le p-1$ 明确保证。

先以两端深域在对应闭核中的稠密性延拓，再用 R23 的
$\overline{A^hM}=M$，得到
$$
\boxed{\mathcal B(M,U_\zeta M)=0\qquad(\zeta\notin\mu_h).}
\tag{7.4}
$$
没有假设 $CM=M$，也没有把一般全空间分子的稠密像外推到未知限制。

为完成原空间排核，任意 $f,g\in M$ 的反射乘积
$f(y)g(-1-y)\in L^1$ 的 dyadic Fourier 支撑由 (7.4) 包含于有限群 $\mu_h$。
柱条件期望的 $L^1$ 收敛使它成为模 $h$ 的柱函数。

若 $M\ne0$，取可数稠密族定义其总本质支撑。$A$ 的权几乎处处严格为正，
$AM\subseteq M$，而 odometer 保测遍历，故此总支撑全测。
在每个模 $h$ 柱上，可以选 $f_r,g_r\in M$ 使
$f_r(y)g_r(-1-y)$ 在正测集非零；这个乘积既是柱常数，便在整柱非零。
对任意 $f\in M$，$f(y)g_r(-1-y)$ 也为柱常数，所以该柱上的 $f$ 是 $f_r$ 的标量倍数。
于是 $\dim M\le h$。

原 $A$ 单射且拟幂零，不存在非零有限维不变空间。因此 $M=0$。
原空间的完整 $C$ 自伴性给 $T$ 值域稠密，再用 (3.10)，得到 (1.9)。
特别，输出自动非零。定理证毕。

## 8. 全部幂、有限候选值与二次旧范围

### 8.1 同一个切片证书给全部平移幂

定义
$$
\Delta_F(z)=p_0(z)-p_1(z).
$$
若 $\Delta_F\not\equiv0$，令
$$
\mathcal E_F=\{p_0(z):\Delta_F(z)=0\}.
\tag{8.1}
$$
该集合有限，且
$$
|\mathcal E_F|\le\deg\Delta_F\le p.
\tag{8.2}
$$
非零常数 $\Delta_F$ 时，$\mathcal E_F$ 为空。

两个切片 $p_0-\lambda$、$p_1-\lambda$ 有共同根，
恰当且仅当 $\lambda\in\mathcal E_F$。
对于每个整数 $m\ge1$，多项式 $(F-\lambda)^m$ 的两个切片是这两者的 $m$ 次幂，
最高主系数在 $\beta$ 处仍非零。
因此
$$
\boxed{
\lambda\notin\mathcal E_F
\Longrightarrow
(F(u,v)-\lambda)^m e^w\text{ 循环，对全部 }m\ge1.
}
\tag{8.3}
$$
这不是从循环向量点乘或取极限得到，而是分别对每个有限次数使用完整深域消元。
若 $\Delta_F\equiv0$，本判据不提供上述有限候选结论。

### 8.2 线性辅助的明确首位条件

取一个居中有界辅助
$$
v=\sum_j c_j(\chi_j-1),\qquad c\in\ell^1,
$$
以及 $F(U,V)=U^p+V$。这时 $\beta=0$，
$$
p_0(z)=z^p,\qquad p_1(z)=(z-2a)^p-2c,
$$
其中单个 $c$ 为联合首位的辅助系数。
故
$$
\boxed{
c\ne\frac{(-2a)^p}{2}
\Longrightarrow
(u^p+v)^m e^w\text{ 循环，对全部 }m\ge1.
}
\tag{8.4}
$$
$a=0$ 时 $c\ne0$ 自动成立。

若 $p\ge2$、$a\ne0$，则
$$
\Delta_F(z)=z^p-(z-2a)^p+2c
$$
次数恰为 $p-1$，所以 (8.3) 对这一族最多留下 $p-1$ 个标量候选值。

$p=2$ 时，(8.4) 是 $c\ne2a^2$。
若写 $c_j=2a_j^2+\varepsilon_j$，首偏离不晚于首主位便满足这个判据。
这正是 R236 最新首支撑二次定理的已覆盖部分，不重复作为本稿新例。

### 8.3 任意非线性有界辅助多项式

仍取一个有界辅助，令 $F(U,V)=U^p+r(V)$。
对 $\lambda=r(\beta)$，
$$
p_0(z)-\lambda=z^p.
$$
所以充分条件精确为
$$
\boxed{
(-2a)^p+r(\beta-2c)-r(\beta)\ne0.
}
\tag{8.5}
$$
成立时
$$
\bigl(u^p+r(v)-r(\beta)\bigr)^m e^w
$$
对全部 $m\ge1$ 循环。没有给 $r(v)$ 省略其点态 Bell 修正。

### 8.4 R236 全阶共振加偏离判据的准确归属

R270C 的 $F_q=\sum q_kF_k$ 可视为主变量 $u$ 及有限个有界辅助
$v_n=\sum_j a_j^n(\chi_j-1)$ 的点态多项式；$n\ge2$ 保证这些行可和。
再加任意 $v_c=\sum c_j(\chi_j-1)$。

当首偏离不早于首主位，记 $\alpha=a_{j_a}$、$\delta=c_{j_a}$。
在联合首位翻转后，有限阶生成式满足
$$
\exp\!\left[t(z-2\alpha)
+\sum_{n\ge2}\frac{2^{n-1}}n\,t^n(-2\alpha^n)\right]
=(1-2\alpha t)e^{tz}.
$$
这里只取到 $\deg q$ 阶的 jets。因此两个切片准确为
$$
p_0(z)=q(z),\qquad p_1(z)=q(z)-2\alpha q'(z)-2\delta.
$$
故本稿判据恰还原 R236 已发表的
$\gcd(q-\lambda,\alpha q'+\delta)=1$。
若首偏离更早，则该位主系数为零，切片差为非零常数，全部 $\lambda$ 均通过。
这些单次循环范围归 R236 原定理；本稿 §8.1 另外对相应
$(F_q+v_c-\lambda)^m e^w$ 的每个有限 $m$ 付完整点态幂域消元。
$p=1$ 仍须检查切片差，不能忽略 $\alpha+\delta=0$ 的退化。

## 9. 一个不依赖旧尾预算的不可约慢耦合族

固定
$$
\frac12<\sigma<1,\qquad
u=\sum_{j\ge0}(-1)^j(j+1)^{-\sigma}\chi_j,
$$
以及
$$
v=\sum_{j\ge0}(j+1)^{-11/10}(\chi_j-1).
\tag{9.1}
$$
主行属于 $\ell^2\setminus\ell^1$，辅助属于 $\ell^1$，二者支持完全重叠。
联合首位 $j_0=0$，$a=c=1$，$\beta=0$。

取不可约多项式
$$
F(U,V)=U^3+V^2.
$$
其两个切片为
$$
p_0(z)=z^3,\qquad p_1(z)=(z-2)^3+4.
$$
$p_0$ 只有根 $0$，而 $p_1(0)=-4\ne0$。
因此对任意复 $\ell^2$ 指数权 $w$，
$$
\boxed{
(u^3+v^2)^m e^w\text{ 循环，对全部整数 }m\ge1.
}
\tag{9.2}
$$
$U^3+V^2$ 在 $\mathbb C[U,V]$ 不可约：若作为 $V$ 的首一二次式可约，
则 $-U^3$ 必须是 $\mathbb C[U]$ 中的平方，而其在 $U=0$ 处阶数为奇数。

这里至少有如下明确的旧假设失效：

- 主行的正、负相位质量都发散，任一固定方向的相位缺陷和都发散，故不属 R134/R138 的空谱锚。
- 主幅度满足 $\sup_{k\ge N}k\rho_k=\infty$，不属 R268 所列熵主行准则。
- 辅助是多项式慢尾，不属超三次快辅助；并且
  $|c_j|/|a_j|^3=(j+1)^{3\sigma-11/10}\to\infty$，
  不满足 R270 对这种最高主根重数所要求的逐位高次小辅助条件。
- 本例是三次主项与平方辅助的真实点态耦合，不是两个不交模式的点态乘积。

这个例子的有限平移候选还能准确写出：
$$
\Delta_F(z)=6z^2-12z+4,
\qquad
z=1\pm\frac1{\sqrt3},
\qquad
\mathcal E_F=
\left\{2-\frac{10}{3\sqrt3},\ 2+\frac{10}{3\sqrt3}\right\}.
$$
因此对每个 $\lambda\notin\mathcal E_F$，全部
$(u^3+v^2-\lambda)^m e^w$ 也循环。两个列出的值只是本判据未排除的候选，不是已证非循环的例子。

(9.2) 只排除此类切片互素耦合的核，不能由它推出一般两个独立无界慢模式或一般不可约多项式无核。

## 10. 保留的缺口

辅助绝对可和用于得到真正有界的 $Z_\nu$，继而把全部 Bell 系数收进 $\mathcal A_h$ 并只留下一个闭变量。若辅助也仅平方可和且无界，两个多元多项式互素不保证单位理想，本证明不能直接使用。

最高主系数条件 (1.6) 用于真实单位及有限自由模。最高系数字符为零的情形没有在本文中被任意除掉。

普通单模式的两根平移碰撞仍可能使 $p_0,p_1$ 有共同根；首偏离较晚的二次共振也可能保留这一碰撞。本稿没有清空这些候选，研究需继续。

主要依赖：

- [R144：一模式平移消元](R144-first-mode-shift-resultant-cyclicity.md)。
- [R147：任意第一阶指数权](R147-exponential-weighted-first-mode-polynomial-cyclicity.md)。
- [R155：空谱锚及有界辅助的真实最高系数](R155-empty-anchor-bounded-auxiliary-polynomials.md)。
- [R176：自然幂、完整闭图和指数倾斜](R176-natural-polynomial-maximal-graphs-and-bell-domains.md)。
- [R186：共同自然域与全混合 Bell jets](R186-multimode-common-domains-maximal-polynomial-graphs-gauge-cyclicity.md)。
- [R236：已覆盖的首支撑二次范围](R236-appendix-earliest-support-dyadic-quadratic-cyclicity.md)。
