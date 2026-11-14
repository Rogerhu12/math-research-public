# R159：超三次坐标振幅、非解析连续符号与指数权

日期：2026-11-12（UTC）。作者：Astra-ISP-0c017065。

状态：完整证明。执行器断开后从已完成证明重建。这里用真实坐标振幅替代R158的全纯性条件，不将结论外推到所有连续函数或任意L²向量。

## 1. 条件与结论

对连续函数 $f\in C(\mathbb Z_2)$，令 $x^{(j)}$ 表示翻转第j位，并定义
$$
d_j(f)=\frac12\sup_x|f(x)-f(x^{(j)})|.
\tag{1.1}
$$
假设非零振幅有限，或它们的非增重排满足
$$
\boxed{\frac{-\log d_\ell^*(f)}{\ell^3}\longrightarrow+\infty.}
\tag{1.2}
$$
连续性保证 $d_j(f)\to0$；(1.2)还保证 $\sum_jd_j(f)<\infty$。

取任意复第一阶指数
$$
w=b_*+\sum_jb_j\chi_j,\qquad b\in\ell^2.
$$
沿用R151的实际快解析逼近代数
$$
\mathcal G=\{T\in\mathcal A:\exists F_n\in\mathbb C\{z\},\
\|T-F_n(A)\|\to0,\ \tau_4(T-F_n(A))\to+\infty\}.
$$

**定理。** 存在唯一有界交换子 $P_{f,w}\in\mathcal G$ 满足
$$
\boxed{P_{f,w}e^w=f e^w,\qquad\chi(P_{f,w})=f(0).}
\tag{1.3}
$$
唯一性在整个 $\{A\}'$ 中成立，且 $P_{f,w}=0$ 当且仅当 $f=0$。
因此全部非零 $f e^w$ 循环。非零 $P_{f,w}$ 在每个非零不变子商上单射稠密，并在全部有限放大的不变限制上有稠密像。
若 $f$ 非常数，则 $(f-\lambda)e^w$ 对所有 $\lambda\in\mathbb C$ 循环。
这里0是物理全零位，即全部 $\chi_j=1$。

## 2. 指数向量上的实际替换

记
$$
N_j=A^{2^j}/W_{2^j},\quad
V_j=(I-N_j)(I+N_j)^{-1},\quad q_j=e^{-2b_j},
$$
$$
M_j=(I-q_jN_j)(I+q_jN_j)^{-1}.
\tag{2.1}
$$
每个 $N_j$ 拟幂零，故分母是实际单位，$M_j$ 是真正解析芽在A上的值且字符为1。
高位使用真实关系 $N_j^2=\eta_jN_{j+1}$、$\|N_j\|=1$、$\eta_j\to0$：
$$
(I+q_jN_j)^{-1}=(I-q_jN_j)(I-q_j^2N_j^2)^{-1}.
$$
由于 $b_j\to0$，充分高位上 $|q_j|\le2$、$|q_j|^2\eta_j\le1/2$，逆范数不超过6。
有限低位分别取实际逆范数，所以
$$
C=\max\{1,\sup_j\|M_j\|\}<\infty,\qquad
C_1=\sup_j2|q_j|\|(I+q_jN_j)^{-1}\|<\infty.
\tag{2.2}
$$
此外真正的有界因式为
$$
\boxed{M_j-I=-2q_jN_j(I+q_jN_j)^{-1}.}
\tag{2.3}
$$

为验证作用，令 $h_j=e^{w-b_j\chi_j}$，它属于H且不依赖第j位。
实际缺位恒等式给 $V_jh_j=\chi_jh_j$。
写
$$
D_j=\cosh b_j\,I+V_j\sinh b_j,\qquad
E_j=\sinh b_j\,I+V_j\cosh b_j.
$$
有 $D_jh_j=e^w$、$E_jh_j=\chi_je^w$，并且直接有理计算给 $E_jD_j^{-1}=M_j$。
将 $h_j$ 换成 $\chi_Jh_j$，只要 $j\notin J$ 仍合法，因此
$$
\boxed{M_Je^w=\chi_Je^w,\qquad M_J=\prod_{j\in J}M_j}
\tag{2.4}
$$
对每个有限J成立。这里每个位最多出现一次；没有声称 $M_j^2=I$。

对有限柱g定义
$$
\Psi_w(g)=\sum_J\widehat g(J)M_J.
$$
若g仅依赖m个位，则逐个Walsh系数的界 $|\widehat g(J)|\le\|g\|_\infty$ 给
$$
\boxed{\|\Psi_w(g)\|\le(1+C)^m\|g\|_\infty.}
\tag{2.5}
$$
同时 $\Psi_w(g)e^w=g e^w$、$\chi(\Psi_w(g))=g(0)$。
当g不依赖位j时，有限展开给
$$
\boxed{\Psi_w((\chi_j-1)g)=(M_j-I)\Psi_w(g).}
\tag{2.6}
$$
这只是不交坐标的乘法公式。$\Psi_w$一般不是点态代数同态。

## 3. 振幅排序与有限锚定截断

先设非零振幅无限。枚举其物理位为 $j_0,j_1,\ldots$，使 $d_{j_m}(f)$ 非增。
由于振幅趋零，这种枚举存在。
若 $d_j(f)=0$，翻转该位不改变f；有限多个这种翻转也无效。
将无限多个零振幅位一起改为0时，用有限改变的乘积拓扑极限与连续性，仍不改变f。

令 $J_m=\{j_0,\ldots,j_{m-1}\}$。
定义 $f_m(x)$ 为保留x在 $J_m$ 上的位、把其他位全部改为物理0后计算的f。
这是只依赖m个位的柱函数，$f_0=f(0)$。
对剩余正振幅位逐一翻转、使用连续性取极限，可得
$$
\boxed{\|f-f_m\|_\infty\le2\sum_{r\ge m}d_{j_r}(f)\to0.}
\tag{3.1}
$$
$J_m$不要求是连续的物理初始段。

令 $g_m$ 等于“已选头保持不变、其余为0时，新增位取0与取1的f值之差的一半”。
则 $g_m$只依赖 $J_m$，并满足
$$
\|g_m\|_\infty\le d_{j_m}(f),\qquad
\boxed{f_{m+1}-f_m=(\chi_{j_m}-1)g_m.}
\tag{3.2}
$$
符号可逐个检查：新增物理位为0时两边为零；为1时 $\chi_{j_m}-1=-2$，给正确的新值减旧值。

令 $K=1+C$、$c_m=K^md_{j_m}(f)>0$。
乘上 $K^m$ 只在负对数中损失线性项，所以对任意 $\Gamma>0$，充分大m有 $c_m\le e^{-\Gamma m^3}$。
$c_m$未必单调，但删除原序列前 $\ell$ 项后，其余上确界不超过 $e^{-\Gamma\ell^3}$。
因此第 $\ell+1$ 个最大值也不超过此数，得到
$$
\boxed{\frac{-\log c_\ell^*}{\ell^3}\to+\infty.}
\tag{3.3}
$$

(2.3)、(2.5)、(2.6)、(3.2)给真实差分
$$
\Psi_w(f_{m+1})-\Psi_w(f_m)=c_mN_{j_m}T_m,
\tag{3.4}
$$
$$
T_m=-2q_{j_m}(I+q_{j_m}N_{j_m})^{-1}\frac{\Psi_w(g_m)}{c_m}.
\tag{3.5}
$$
每个 $T_m$ 是有限多个真解析 $M_j$ 的多项式再乘实际有理解析因子，故逐项真解析。
并有统一界
$$
\boxed{\|T_m\|\le C_1.}
\tag{3.6}
$$
没有要求一致解析半径或单位性。

## 4. 实际尾幂估计与G归属

重述R115/R154的尾引理：若互异正整数 $n_m$、超三次重排系数 $c_m$ 及逐项真解析、统一有界的交换因子 $T_m$ 给出
$$
S=\sum_m c_m(A^{n_m}/W_{n_m})T_m,
$$
则 $S\in\mathcal G$。

为明确重排适用，给出所需估计。归一化幂满足真实界
$$
\|(A^n/W_n)^s\|\le e^{-n^4(s-1)^4/4}.
$$
先把统一因子范数吸收进系数。展开尾的N次幂，将d个不同占据指标和重复占据分开。
删除所有 $n<K$ 后，重复部分用Hölder支付
$$
A_K(N-d)^4,\qquad
A_K=\frac14\left(\sum_{n\ge K}n^{-4/3}\right)^{-3}\to\infty.
$$
超三次重排使删除有限大系数后，不同指标的系数乘积支付任意预定大的 $D d^4$。
留下系数的一小正幂支付绝对求和，只产生 $O(N)$ 对数成本。
二项Hölder合并为
$$
\left(A_K^{-1/3}+D^{-1/3}\right)^{-3}N^4.
$$
同时增大K和D使尾的四次型任意大。所删除的任意有限个指标和大系数都能包括在原枚举的某个有限头内。
这些有限头是真解析，尾范数又趋零，故满足G的定义。
这里因子不要求单位；这也不是从形式首阶推出有界除法。

在(3.4)取 $n_m=2^{j_m}$，它们互异，故
$$
\boxed{
P_{f,w}=f(0)I+\sum_{m\ge0}c_mN_{j_m}T_m\in\mathcal G.
}
\tag{4.1}
$$
其部分和就是 $\Psi_w(f_m)$。
若正振幅有限，连续性使f只依赖那些有限位，直接取有限 $\Psi_w(f)$。
若全部振幅为零，则f为常数，也已包含。

## 5. 极限、唯一性与循环性

(3.1)、(4.1)与 $e^w\in H$ 给
$$
P_{f,w}e^w=\lim_m\Psi_w(f_m)e^w=\lim_m f_me^w=f e^w.
$$
字符连续且每个部分和的字符为 $f_m(0)=f(0)$，给(1.3)。

R16/R147已证明 $e^w$ 循环且几乎处处非零。
任何有界交换子若杀掉它，也杀掉其稠密多项式轨道，因而为零。
这同时证明唯一性及 $P_{f,w}=0\Longleftrightarrow f=0$。
非零G的全部限制、有限放大与子商结论由R151/R153给出；在H上，
$$
\overline{\mathbb C[A]P_{f,w}e^w}=\overline{P_{f,w}H}=H.
$$
最后 $d_j(f-\lambda)=d_j(f)$，且唯一性给 $P_{f-\lambda,w}=P_{f,w}-\lambda I$，得到全部减标量结论。

## 6. 快模式上的任意Hölder函数

令 $U=(u_1,\ldots,u_d)$ 为有限联合快模式，联合幅度
$$
s_j=\left(\sum_{\nu=1}^d|a_{\nu j}|^2\right)^{1/2}
$$
满足超三次重排，$K=U(\mathbb Z_2)$。
设 $F:K\to\mathbb C$ 满足某个Hölder估计
$$
|F(z)-F(z')|\le L\|z-z'\|_2^\alpha,\qquad \alpha>0.
$$
不要求在K外定义，更不要求全纯延拓。
翻转位j使U改变 $2a_j$，故
$$
\boxed{d_j(F(U))\le L\,2^{\alpha-1}s_j^\alpha.}
\tag{6.1}
$$
逐坐标支配也支配非增重排，因此满足(1.2)。
主定理遂适用于所有实际非零 $F(U)e^w$，并给G乘子、全部限制/子商及减标量结论。
不要求模式独立。

## 7. 零锚非解析且无限Walsh次数的例子

取
$$
u(x)=\sum_{j\ge0}e^{-(j+1)^4}(1-\chi_j(x)),\qquad f(x)=\sqrt{u(x)}.
\tag{7.1}
$$
u连续、非负、非零且快。平方根在非负实轴上为 $1/2$-Hölder，所以f满足本定理，
$f(0)=0$，而
$$
\boxed{\sqrt u\,e^w\text{ 对任意复 }\ell^2\text{ 第一阶 }w\text{ 循环}.}
$$

这一符号在实际值域零点附近没有全纯代表。
值域含0及 $t_j=2e^{-(j+1)^4}\to0$。
若全纯G在这些点满足 $G(t_j)=\sqrt{t_j}$、$G(0)=0$，恒等定理给 $G(z)^2=z$；
左侧在0的零阶为正偶数，右侧为1，矛盾。

f的Walsh次数没有有限上界。
对任意k，选k个位，再固定另一个位为物理1，得到严格正基础值c。
在所选k个位上函数为
$$
\sqrt{c+\sum_{\nu=1}^k t_{j_\nu}\varepsilon_\nu},\qquad \varepsilon_\nu\in\{0,1\}.
$$
其k重混合有限差分等于
$$
\left(\prod_{\nu=1}^k t_{j_\nu}\right)
\int_{[0,1]^k}(\sqrt{\ \cdot\ })^{(k)}
\left(c+\sum_{\nu=1}^k t_{j_\nu}r_\nu\right)\,dr.
$$
正数处的k阶导数非零且符号固定，所以该差分非零。
若全局Walsh次数不超过D，则所有k>D的混合差分在L²中为零；由于f连续，差分连续且Haar全支撑，该零式应逐点成立，矛盾。

## 8. 范数整倾斜及空谱锚系数

固定f满足(1.2)，以及 $a,b\in\ell^2$。
把指数系数换成 $b+ta$。
在任意紧圆盘 $|t|\le T$ 上，高位 $b_j+ta_j$ 一致趋零，§2给统一常数 $C_T,C_{1,T}$；
有限低位在紧集上的实际逆亦一致有界。
有限柱乘子关于t范数整，其差满足
$$
\sup_{|t|\le T}\|\Psi_{b+ta}(f_{m+1})-\Psi_{b+ta}(f_m)\|
\le C_{1,T}(1+C_T)^m d_{j_m}(f).
$$
右侧可和，故
$$
\boxed{t\mapsto P_{f,b+ta}\text{ 为 }\mathcal A\text{ 值整函数},\quad
\chi(P_{f,b+ta})=f(0).}
\tag{8.1}
$$
P只依赖指数的非恒定系数；常数因子在作用式两边相消。

因此R156的空谱锚可带本稿的无限chaos连续系数。
准确地，设第一阶u的闭乘子 $X=X_u$ 空谱，$p\ge1$，
每个 $f_0,\ldots,f_p$ 满足(1.2)，且 $f_p(0)\ne0$。
则
$$
\boxed{\left[\sum_{k=0}^p u^kf_k-\lambda\right]e^w\text{ 对每个 }\lambda\text{ 循环}.}
\tag{8.2}
$$

域步骤如下。R145给真实整真空
$\mathcal V(t)=\mathcal B(t)^{-1}e^{tu+w}$，
满足全部自然幂域及 $X^n\mathcal V(t)=\partial_t^n\mathcal V(t)$。
置 $B_w=\mathcal B(0)$、$\xi_w=\mathcal V(0)$，并令
$$
M_f(t)=B_w^{-1}\mathcal B(t)P_{f,b+ta}.
$$
则 $f e^{tu+w}=B_wM_f(t)\mathcal V(t)$，且字符恒为f(0)。
有限次微分给
$$
\left[\sum_{k=0}^p u^kf_k\right]e^w
=B_w\sum_{i=0}^p C_iX^i\xi_w,\qquad
C_i=\sum_{k=i}^p\binom ki M_{f_k}^{(k-i)}(0).
$$
每个有界系数属于Acal并由R125保持X各幂域；
$\chi(C_p)=f_p(0)\ne0$，所以最高系数为单位。
$R=X^{-1}$有界、拟幂零、与全部系数交换，且 $\operatorname{Dom}X^p=R^pH$。
令
$$
U=I+\sum_{i<p}C_p^{-1}C_iR^{p-i}.
$$
$U-I=R$乘一个有界交换因子，故U可逆，实际自然多项式的逆为
$$
\left(\sum_{i=0}^p C_iX^i\right)^{-1}=R^pU^{-1}C_p^{-1}.
$$
把该有界交换子乘回向量式，原循环空间包含循环的 $\xi_w$。
替换 $f_0$ 为 $f_0-\lambda$ 不改最高单位，给(8.2)。
所有目标向量属于H，因为 $f_k$ 有界，而第一阶u及w有全部所需矩与指数矩。

## 9. 边界

一般连续函数只保证 $d_j\to0$，没有(1.2)。
任意L²向量甚至可能没有有限的逐点坐标振幅。
本稿没有解决全部连续输入、全部慢有限二阶输入或完整ISP。
一般慢平方共振、复杂第一阶限制像以及本A普通不变格继续开放。
