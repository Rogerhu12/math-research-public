# R163：全部惰性 $p$ 的原始伴随 Robert 生成元

日期：2026-11-12；会话：serre-uniformity-resume2。

**状态：已证明。** 本文将
[R161](R161-strict-adjoint-selmer-line-and-tate-support-orthogonality.md)
中 $p=43$ 的实际 Robert 生成元推广到每个
$$p>37,\qquad p\equiv3\pmod4.$$
对
$$
A:y^2=x^3-x,\quad K=\mathbb Q(i),\quad
T=K(A[p])=K((1+i)^3p),
$$
取一次实的 $0\ne P\in A[p]$，令
$$
P_2=(i,1-i),\quad
v_{11}=\frac{64^{10}}{\psi_{11}(P_2+P)},\quad
\chi(a)=a^{p-1}\quad(a\in\mathbb F_{p^2}^{\times}).
$$
则
$$
\boxed{e_\chi[v_{11}]\ne0
\quad\text{于 }(T^\times/T^{\times p})\otimes_{\mathbb F_p}\mathbb F_{p^2}.}
\tag{163.1}
$$
按 R161 的实际复共轭作用，$i e_\chi[v_{11}]$ 唯一下降为
$\mathbb Q$ 上的类，且准确生成其固定一维空间 $\mathcal D_p$。
因此 R161 的有限域公式和实际支撑正交条件，对所有这些 $p$
都可以直接使用同一个除法多项式 $\psi_{11}$，
不再需要先搜索某个局部非零值才能证明生成性。

本结果不声称每个局部投影都非零，也不阻止多个支撑项相消。
它提供的是一个全 $p$ 的真实生成元，而不是变化分母的统一排除。

## 1. 准确表示与最小严格 Selmer 零群

保留 R161 记号：
$$
V=A[p],\quad J=[i],\quad
\operatorname{ad}^0V=\mathbb F_p(\eta)J\oplus W,\qquad\eta=\chi_{-4}.
$$
把 $W$ 写成 $D_z(v)=z\bar v$ 后，
$$
a:z\longmapsto a^{1-p}z,\qquad
\tau:z\longmapsto\bar z.
\tag{163.2}
$$
它是完整
$$G=\operatorname{Gal}(T/\mathbb Q)
=\mathbb F_{p^2}^{\times}\rtimes\langle\tau\rangle$$
的绝对不可约二维表示。
Cartan 上的两个特征 $a^{1-p}$ 和 $a^{p-1}$ 不同，被 $\tau$ 交换。
将 $W$ 乘 $\eta$ 不改变同构型：$z\mapsto iz$ 给所需 intertwiner。

R161 用最小有限平坦 $R=T=\mathbb Z_p$、Conrad 的 local flat
切线及 Poitou–Tate，证明了
$$
H^1_{\mathcal F_0}(\mathbb Q,W)=0,\qquad
\dim\mathcal D_p=1.
\tag{163.3}
$$
这里 $\mathcal F_0$ 在 $p$ 取**零局部条件**，
在 $2$ 取整个 $H^1(\mathbb Q_2,W)=0$，
其余有限处取不分歧条件。
后文的类群消失使用这条准确严格条件，而非只使用
“某个一般 Selmer 群有限”。

令
$$
\mathcal O=\mathbb Z_p[i],\qquad
\widetilde\chi:C=\operatorname{Gal}(T/K)\to\mathcal O^\times
$$
为 $a^{p-1}$ 的 Teichmüller 提升。
其 Frobenius 共轭是 $\widetilde\chi^p=\widetilde\chi^{-1}$。
本文的整 $\widetilde\chi$ 分量均先扩系数到 $\mathcal O$ 再投影；
模 $p$ 时回到 $\chi$。

## 2. 所需 $p$ 类群分量为零：特征素数处的完整论证

记 $\mathcal A_T=\operatorname{Cl}(T)\otimes\mathbb Z_p$。我们证明
$$
\boxed{\mathcal A_T^{\widetilde\chi}
=\mathcal A_T^{\widetilde\chi^p}=0.}
\tag{163.4}
$$

若不为零，Nakayama 引理使
$\operatorname{Cl}(T)/p\operatorname{Cl}(T)$ 含相应 Cartan 型。
该类群本来是 $\mathbb F_p[G]$ 模，且 $p\nmid|G|$，故完全可约。
$\tau$ 交换 $\chi,\chi^p$，所以它有一个非零 $G$ 等变商
同构于 (163.2) 的 $W$。这不是只在 $G_K$ 上挑选一个没有
有理下降的单特征商。

由 Hilbert 类域，该商给一个非零同态
$$
h:G_T\longrightarrow W
$$
在 $T$ 的每个有限位置都不分歧，并对 $G$ 等变。
因 $H^1(G,W)=H^2(G,W)=0$，它唯一下降为非零
$$c\in H^1(\mathbb Q,W).$$

在 $p$ 处，$A$ 好超奇异，模 $p$ 惯性给完整 Cartan $C$。
故 $T$ 在 $p$ 的惯性群为 $C$，阶 $p^2-1$ 与 $p$ 互素。
$h$ 在 $T$ 的局部惯性上为零，所以其局部值由
不分歧 Frobenius 商生成。
惯性 $C$ 对这个不分歧商的共轭作用平凡；
等变性迫使其值落在
$$W^C=0.$$
因此 $h$ 在整个 $T$ 的该局部分解群上为零。
限制映射
$$
H^1(\mathbb Q_p,W)\longrightarrow H^1(T_{\mathfrak P},W)
$$
的核来自阶与 $p$ 互素的有限分解群的 $H^1$，亦为零，
从而
$$\operatorname{loc}_p(c)=0.$$
这里没有把“在 $T_p$ 不分歧”直接误写成“在 $\mathbb Q_p$ 为零”；
中间使用了实际完整 Cartan 惯性、无不变量和限制映射的核。

在 $2$，R161 的 $H^1(\mathbb Q_2,W)=0$ 给局部值零。
在 $q\ne2,p$，$T/\mathbb Q$、$W$ 和 $h$ 都不分歧，
因此 $c$ 满足不分歧条件。于是 $c$ 落在 (163.3) 的零群，
矛盾。这证明 (163.4)。

## 3. 角色的导子是 $(1+i)^2p$，不是 $(1+i)^3p$

置 $\pi=1+i$，$\mathfrak m=\pi^3p$。
R70 的 primary Artin 同构为
$$
\operatorname{Cl}_{\mathfrak m}(K)\simeq\mathbb F_{p^2}^{\times}.
$$
其 CRT 表示来自
$$
(\mathcal O_K/\pi^3)^\times\times
(\mathcal O_K/p)^\times
$$
再商掉对角的 $\mu_4$。
若第一坐标是单位根 $\zeta$ 的像，第二坐标为 $a$，
primary 标签为 $a/\zeta$。因此 $\chi$ 在二进单位群上的限制是
$$
\zeta\longmapsto \zeta^{-(p-1)}=\zeta^2.
\tag{163.5}
$$
它杀掉 $-1$，不杀掉 $i$。
$(\mathcal O_K/\pi^2)^\times$ 阶为二，$i$ 的像非平凡；
模 $\pi$ 的单位群则平凡。
所以二进导子准确为 $\pi^2$。
$p$ 处 $\chi$ 在剩余域单位群上的阶为 $p+1$，
非平凡且 tame，故该处导子准确为 $p$。于是
$$
\boxed{\mathfrak f_\chi=\pi^2p.}
\tag{163.6}
$$

令
$$
F=T^{\mathbb F_p^\times},\qquad
H=K(\pi^2p).
$$
$\chi$ 的核是 $\mathbb F_p^\times$，故
$$
[F:K]=p+1,\qquad
F\subset H\subset T,\qquad
[T:H]=2,\qquad[H:F]=(p-1)/2.
\tag{163.7}
$$
$\widetilde\chi$ 在 $\operatorname{Gal}(F/K)$ 忠实，
且 $F/K$ 的导子同为 (163.6)。
所有这些扩张次数都是 $p$ 单位。
理想类的扩张与范数之复合为 $[T:F]=p-1$，
故 $\operatorname{Cl}(F)$ 的相关 $p$ 分量注入到 $T$；
由 (163.4) 得
$$
\bigl(\operatorname{Cl}(F)\otimes\mathcal O\bigr)^{\widetilde\chi}=0.
\tag{163.8}
$$

## 4. 有限 Gras 等式与一个固定辅助理想

令 $\mathcal E_F=\mathcal O_F^\times$，
$\mathcal C_F$ 为 Rubin 的椭圆单位群。
Rubin (1991), Theorem 3.3（印刷页 35），在当前条件下给
$$
\#(\mathcal E_F/\mathcal C_F)^{\widetilde\chi}
=\#(\operatorname{Cl}(F)\otimes\mathbb Z_p)^{\widetilde\chi}.
\tag{163.9}
$$
与 R65 相同，其单位根限制针对基域 $K$ 的 Hilbert 类域：
此处该域就是 $K$，单位根数为四；并且 $p\nmid[F:K]=p+1$。
所以全部假设满足，没有 ordinary 假设，也没有要求
$p$ 在 $K$ 分裂。

原定理可先作用于不可约 $\mathbb Z_p$ 型 $\chi\oplus\chi^p$。
(163.8) 使右边为一；左边长度非负，
因此扩系数后两个单特征的商都为零，不需要假设不同特征长度相同。
Dirichlet 定理给每个非平凡 Cartan 特征的单位分量秩一，
单位根的 $p$ 部分不在 $\chi$ 分量。
于是
$$
(\mathcal E_F\otimes\mathcal O)^{\widetilde\chi}
=(\mathcal C_F\otimes\mathcal O)^{\widetilde\chi}
\simeq\mathcal O.
\tag{163.10}
$$

用
$$
u_{\mathfrak a}=
N_{H/F}\Psi(1;\mathfrak f_\chi,\mathfrak a^{-1}\mathfrak f_\chi),
\qquad(\mathfrak a,6\mathfrak f_\chi)=1
\tag{163.11}
$$
表示基本 Robert 单位。$\mathfrak f_\chi$ 含两个不同素理想，
所以这些值确为全局单位。

这些 $u_{\mathfrak a}$ 的 $\widetilde\chi$ 投影生成
(163.10)。理由可完整表述如下。
Oukhaba–Viguié (2013), §4 印刷页 155 给出所有 Robert 范数
生成元的描述，Remark 4.3 说明它与 Rubin 的群之差被 $[F:K]$
杀掉，故当前 $p$ 进分量相同。
若生成元来自 $F\cap K(\mathfrak n)\ne F$，
因 $\widetilde\chi$ 在 $\operatorname{Gal}(F/K)$ 忠实，其投影为零。
否则 $F\subset K(\mathfrak n)$，导子性质给
$\mathfrak f_\chi\mid\mathfrak n$。
逐个使用 Robert 范数关系降到 $\mathfrak f_\chi$，
所得项是 (163.11) 乘群环中的 Euler 因子，未作任何除法。
Rubin 生成元中的 $\sigma-1$ 也不改变该分量：
$\widetilde\chi$ 非平凡，故可选一个
$\widetilde\chi(\sigma)-1$ 为 $\mathcal O$ 单位。

Stark–Robert 关系给交叉恒等式
$$
(N\mathfrak b-\widetilde\chi(\sigma_{\mathfrak b}))
 e_{\widetilde\chi}u_{\mathfrak a}
=
(N\mathfrak a-\widetilde\chi(\sigma_{\mathfrak a}))
 e_{\widetilde\chi}u_{\mathfrak b}
\tag{163.12}
$$
于单位分量的加法记号。
该式可将两个 Stark–Robert 幂关系交叉相乘得到。
即使相关射线域单位根数含 $p$ 因子，也没有非法除以它：
在无挠的 $\mathcal O$ 单位特征模中，乘该非零整数是单射，
所以可以消去；可能的单位根项在此特征分量为零。

取固定 $\mathfrak b=(11)$。
R70 的算术 Artin 取向给 $\rho(\sigma_{(11)})=-11$，
故
$$
\widetilde\chi(\sigma_{(11)})=1,\qquad
N(11)-\widetilde\chi(\sigma_{(11)})=121-1=120\in\mathcal O^\times.
\tag{163.13}
$$
由 (163.12)，每个 $e_{\widetilde\chi}u_{\mathfrak a}$
都是 $e_{\widetilde\chi}u_{(11)}$ 的整倍数。
由于它们生成 (163.10)，得到
$$
\boxed{e_{\widetilde\chi}u_{(11)}
\text{ 是 }(\mathcal E_F\otimes\mathcal O)^{\widetilde\chi}
\text{ 的基。}}
\tag{163.14}
$$

## 5. 从 $\pi^2p$ 回到实际 $A$ 的 $\pi^3p$ 单位

这一步不能使用新增素数的 Euler 因子。
Oukhaba–Viguié 原刊 §4、印刷页 155 的完整范数式是：
若 $\mathfrak m=\mathfrak n\mathfrak q$，
$$
N_{K(\mathfrak m)/K(\mathfrak n)}
\Psi(1;\mathfrak m,\mathfrak b^{-1}\mathfrak m)^{r_{\mathfrak n}/r_{\mathfrak m}}
=
\begin{cases}
\Psi(1;\mathfrak n,\mathfrak b^{-1}\mathfrak n),
   &\mathfrak q\mid\mathfrak n,\\
\Psi(1;\mathfrak n,\mathfrak b^{-1}\mathfrak n)^{1-\sigma_{\mathfrak q}^{-1}},
   &\mathfrak q\nmid\mathfrak n,
\end{cases}
\tag{163.15}
$$
其中 $r_{\mathfrak a}$ 是基域单位根 $\mu_K$
约化到 $(\mathcal O_K/\mathfrak a)^\times$ 的核阶。

本题 $\mathfrak n=\pi^2p$、$\mathfrak m=\pi^3p$、$\mathfrak q=(\pi)$，
属于第一行。两模数都含 $p>37$，所以没有非平凡
$\mu_4$ 元素模它们为一，即
$$r_{\pi^2p}=r_{\pi^3p}=1.$$
因此准确有
$$
N_{T/H}\Psi(1;\pi^3p,(11)^{-1}\pi^3p)
=\Psi(1;\pi^2p,(11)^{-1}\pi^2p).
\tag{163.16}
$$
没有 $1-\sigma_\pi^{-1}$，没有残留单位根阶数的 $p$ 因子。

由 R70，左边的原始 Robert 值经过一次兼容的 Cartan 共轭，
与本文 $v_{11}=64^{10}/\psi_{11}(P_2+P)$
只差十二次单位根；该差在当前特征模中为零。
再取 $N_{H/F}$，(163.16) 给
$$N_{T/F}e_{\widetilde\chi}v_{11}
=e_{\widetilde\chi}u_{(11)}
\tag{163.17}
$$
至多乘一个来自所选共轭的非零 Teichmüller 单位。

范数与扩张映射在该分量的复合为 $[T:F]=p-1$，
是 $\mathcal O$ 单位；取不变量也因该次数与 $p$ 互素而精确。
因此 (163.14)、(163.17) 说明
$$
e_{\widetilde\chi}v_{11}
\text{ 生成 }(\mathcal E_T\otimes\mathcal O)^{\widetilde\chi}.
\tag{163.18}
$$
模 $p$ 后仍非零，(163.1) 得证。

## 6. 对实际支撑筛的统一输入及其界限

R161 §7 已逐式证明，在联合的单位作用和系数共轭下
$$\tau(e_\chi[v_{11}])=-e_\chi[v_{11}].$$
因此 $i e_\chi[v_{11}]$ 给正下降。
由 (163.1) 和次数二的限制映射单射，这个有理类非零；
R161 的 $\dim\mathcal D_p=1$ 遂给
$$
\boxed{\mathcal D_p=\mathbb F_p\,d_p^{\mathrm{Rob}}
\quad\text{对每个 }p>37,\ p\equiv3\bmod4.}
\tag{163.19}
$$

所以对每个候选惰性素数 $q\equiv-1\bmod4p$，
只需在 $\mathbb F_{q^2}$ 中计算
$$
S_q=
\sum_{a\in\mathbb F_{p^2}^{\times}}
a^{1-p}\log_{\zeta_q}
\left(\psi_{11}(P_2+[a]P_q)^{(q^2-1)/p}\right).
\tag{163.20}
$$
它在所选基下属于 $\mathbb F_p$，
且 $\operatorname{loc}_q(\mathcal D_p)=0$ 当且仅当 $S_q=0$。
投影中的 Robert 倒数、$[T:K]^{-1}$ 和 $\mathbb Q_q/K_{(q)}$
的因子二沿用 R161，均未丢失。

对实际最小 Tate 支撑 $R$：
若全部素因子在 $K$ 惰性，则
$$
\#\{q\mid R:S_q\ne0\}\ne1.
\tag{163.21}
$$
这就是 R161 的实际全局正交条件现在对所有 $p$ 的完全明确输入。

注意额外的惰性有理辅助素数 $\ell$ 满足
$\widetilde\chi(-\ell)=1$，
所以若以新增 $(\ell)$ 的范数强行替代原始导子单位，
会乘上零因子 $1-\widetilde\chi(-\ell)^{-1}=0$。
本证明不作这样的归一化。
反过来，全局生成性并不迫使 (163.20) 的每个局部值非零；
R161 的 $p=43,q=27691$ 就给出了准确零值。
多个非零局部项也仍可能相消，故 (163.19)–(163.21)
不能单独完成 O6。

## 7. 已核来源

- K. Rubin, *The “main conjectures” of Iwasawa theory for imaginary
  quadratic fields*, Inventiones Mathematicae **103** (1991), 25–68，
  Theorem 3.3（印刷页 35），
  [DOI](https://doi.org/10.1007/BF01239508)、
  [原刊档案](https://gdz.sub.uni-goettingen.de/id/PPN356556735_0103)。
  本文复用 R65 §4 已核定的有限 Gras 定理；条件针对基 Hilbert
  类域的单位根数，不能擅自换成更大除法域的单位根数。
- H. Oukhaba and S. Viguié, *On the Gras Conjecture for Imaginary
  Quadratic Fields*, Canadian Mathematical Bulletin **56** (2013), 148–160，
  [原刊全文](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/0148F81E2EC11C708E2769B9AF48720C/S000843950000062Xa.pdf/on-the-gras-conjecture-for-imaginary-quadratic-fields.pdf)。
  引言印刷页 148 明确重述 Rubin 定理的条件；
  §4 印刷页 155 给 Stark–Robert 幂关系、全部范数生成元、
  (163.15) 的两分支；Remark 4.3 给两个椭圆单位群在
  反转扩张次数后的相等。
- [R65](R65-elliptic-unit-first-second-derivatives.md) §4：
  有限 Gras 指数及固定辅助理想的交叉关系；
  本文重新核对了非忠实角色的实际导子，不能直接套它原来的
  忠实 $\rho^p$ 情形。
- [R70](R70-robert-unit-finite-field-certificates.md) §1–3：
  当前 $A$ 的 primary 算术 Artin 方向、准确 $\pi^3p$ 除法域、
  原始点和 $\psi_{11}$ 公式。
- [R161](R161-strict-adjoint-selmer-line-and-tate-support-orthogonality.md)：
  最小严格 $W$ 群为零、固定对偶线维数一、
  正下降与有限域局部坐标，以及实际 Tate 支撑正交。

