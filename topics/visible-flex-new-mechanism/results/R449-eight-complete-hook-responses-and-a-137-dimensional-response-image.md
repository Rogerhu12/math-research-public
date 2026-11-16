# R449：八个完整 hook 响应的真独立性与 144 响应的至少 137 维像

日期：2026-11-16。**完整纸面证明；不执行新的符号、profile、秩、积分或开发计算。** 本文只用 R434/R443 已付准确映射、原八二次算子和完整 hook 原式。

新结论是：R443 退化 self-current 核中的前八列，虽然所有已用退化点诊断都看不见，却是八个真正独立的完整响应。因此原 144 标签的完整响应像维数至少 137；再加原 K11 后至少 148，且 K11 与整个 144 响应像交零。这不是固定实际圆上的评价秩，更不是实际路径控制截面。

来源：[R255 原八算子及完整响应](R255-explicit-third-diagonal-kernel-and-complete-hook-response-formula.md)、[R434 完整 Q/三尾 current](R434-complete-self-kernel-and-three-tail-current-image-on-144-original-responses.md)、[R435 K 链](R435-complete-local-self-currents-and-joint-actual-internal-flux-control.md)、[R443 新完整 self 像](R443-complete-self-image-of-the-paid-joint-kernel-and-forty-nine-formal-directions.md)。原 hook 局部恢复以 [R444(12)—(15)](R444-original-hook-response-action-and-the-highest-second-period-blind-row.md) 的明确公式为准。

## 1. 完整响应空间和三层已付诊断

令 $Z$ 为 R255 的原十八维第三对角核，$E=E_8$。固定原十八标签与八标签的次序，定义

$$
\beta:\mathbb R^{144}\longrightarrow\mathcal R,
\qquad e_{E,\tau}\longmapsto\mathcal B_E\tau,
\qquad \mathcal V=\operatorname{im}\beta .
\tag{1}
$$

这里的像是完整 universal canonical 响应函数空间，保 seed 槽、相位槽及全部原尾，不是仅其 Af 点值。所有 144 标签都 pure 零，但不预设它们完整独立。

R434 已付第一层 whole-Q 映射秩为59，输入系数核85。限制到这个核，原完整三尾 Af-current 映射的秩为32，输入系数核53。R443 再对这53个准确原组合取完整 self-current 的 Af 评价，得到秩38、输入核15。于是有精确系数空间旗标

$$
\mathbb R^{144}\supset N_Q\supset N_{QC}\supset N_{QCS},
\qquad \dim N_Q=85,\quad\dim N_{QC}=53,\quad\dim N_{QCS}=15.
\tag{2}
$$

第三层必须用 R443 的完整同锚 self，不用旧 Q 密度作其原函数；所有局部性、零分母和 fresh 证据均由那次唯一原运行继承，不重算。

每层诊断都由完整响应函数决定。如果一个原144系数组合给完整零响应，它的 whole-Q、三尾 current、完整 self-current 都为零。因此

$$
\ker\beta\subset N_{QCS}.
\tag{3}
$$

仅由(2)(3)先有 $\dim\mathcal V\ge129$。以下证明 $N_{QCS}$ 内至少还有八个**完整非零且独立**的像，从而加强这个下界。

## 2. 八个原 hook 列的完整 self-current

令

$$
\mathfrak H=C(P,S)-3C(P,R),\qquad
L_u(w)=\mathfrak H(w;u,u),
$$
$$
p=u',\qquad r=u'',\qquad t=u''',\qquad A_u=6pt-2r^2.
\tag{4}
$$

原 hook 的系数为 $a=A_u,c=0$，且 $(A_ur)'+b_up=0$。对任意 $E\in E_8$，记 $q_E=\Phi_E(u,u)$。R443 完整 Green 式或 R444(15)准确给

$$
\mathfrak S_{E,\mathfrak H}(x)
=\int_\ell^x p\{2L_u(q_E)\}''
=2A_u\{p q_E''-r q_E'\}.
\tag{5}
$$

同一左平端给积分常数零，$q_E$ 的真实左二次尾仍保留。因显式 $A_u$ 因子，这八列在每个 Af 退化点上的 self-current 为零；R443 的 $F_0,\ldots,F_7$ 正是它们。它们也在 R434 的 whole-Q/三尾 current 核中，所以

$$
H_E:=\mathcal B_E\mathfrak H\in\beta(N_{QCS}).
\tag{6}
$$

但(5)不能推出完整 $H_E$ 为零。下面直接证明 $E\mapsto H_E$ 单射。

## 3. 完整零响应迫单包二次输出的左尾为零

假设常系数 $E=\sum_X\alpha_X X$ 满足

$$
\mathcal B_E\mathfrak H=0
\quad\text{作为完整 universal 响应函数}.
\tag{7}
$$

取 seed $f=u$、相位变量 $\phi=0$。完整原式 R255(31)给

$$
\mathcal B_E\mathfrak H(u^2,0)=2L_u(\Phi_E(u,u)).
\tag{8}
$$

这个取值仅用于 universal 函数身份的纸面判别，不声称 $\phi=0$ 是当前实际非退化圆的相位。因此(7)迫(8)为零，进而由(5)

$$
A_u\{p q_E''-r q_E'\}=0
\quad\text{在整个查询区间}.
\tag{9}
$$

选择一个固定正宽、正幅的偶单峰紧 bump $u_0$，支撑内部实解析，端点平坦，内部只有一个 $p=0$ 点，且该点 $r\ne0$。例如同原光滑端类的 $\exp[-c/(1-y^2)]$（$|y|<1,c>0$）经正宽及正幅缩放具有这些性质。仅考虑其在原允许区间内的一个开区间平移族 $u_a(x)=u_0(x-a)$；不修改任何实际冻结母库。

在支撑内部 $A_u$ 实解析，且在单峰点 $A_u=-2r^2\ne0$，所以其非零集合稠密。式(9)与连续性给

$$
p q_E''-r q_E'=0
\tag{10}
$$

在整个支撑内部成立。在单峰点两侧分别有 $p\ne0$，故

$$
\left(\frac{q_E'}p\right)'=0,
\qquad q_E'=c_-p\ \text{或}\ c_+p.
$$

$q_E''$ 光滑，单峰点 $r\ne0$，所以两侧极限 $c_-r,c_+r$ 相等，得到同一个常数 $c=c(u)$。继续积分并跨峰点用 $q_E$ 连续性，得到

$$
q_E=c(u)u+d(u)
\quad\text{在整个支撑内部}.
\tag{11}
$$

原右锚在支撑右侧，八个原二次式均在右 collar 真零。右端 $u$ 及其 jets 平零，因而 $d(u)=0$。由(11)，$q_E,q_E',q_E''$ 在左端也全为零。

另一方面，$q_E$ 在左 collar 是原八式给出的二次多项式。一个二次多项式在该端点的值、一导、二导全为零，必恒零。因此(7)迫这个平移 bump 族中每个成员的**整个原二次左尾**都为零。

这一步没有假设单包三矩为零；恰恰利用其非零真实尾排除(7)。也没有从 Af 点的零值反推(10)：先用了完整响应为零，使(9)在所有点成立。

## 4. 原八个左尾与三矩平移族迫全部系数零

记原三矩

$$
M_0(u)=\int r^2,\quad
M_1(u)=\int xr^2,\quad
M_2(u)=\int(x^2r^2+2p^2).
\tag{12}
$$

R255(4)的八个真实左尾依次为

| $X$ | $\Phi_X(u,u)$ 的原左尾 |
|---|---|
| $P$ | $M_0$ |
| $R$ | $xM_0$ |
| $S$ | $M_1$ |
| $L$ | $-x^2M_0/4+M_2/4$ |
| $U$ | $xM_1+M_2/2$ |
| $V$ | $-x^2M_1/4$ |
| $T$ | $xM_2$ |
| $Y$ | $-x^2M_2/4$ |

这里 $V=\Phi_{p_1},Y=\Phi_{p_2}$，同名约定与 R443/R444 一致。对(11)已经证明的零左尾分别取二次、一次、常数系数，得

$$
\begin{aligned}
\alpha_L M_0+\alpha_V M_1+\alpha_Y M_2&=0,\\
\alpha_R M_0+\alpha_U M_1+\alpha_T M_2&=0,\\
\alpha_P M_0+\alpha_S M_1+
 (\alpha_L/4+\alpha_U/2)M_2&=0.
\end{aligned}
\tag{13}
$$

固定偶 bump 的 $M_0=m_0>0$、$M_1=0$、$M_2=m_2>0$。对平移 $u_a$，准确换元给

$$
(M_0,M_1,M_2)=(m_0,am_0,a^2m_0+m_2).
\tag{14}
$$

$a$ 在一个非空开区间变化，所以这些三矩向量张成 $\mathbb R^3$：若一个线性函数在(14)上恒零，其关于 $a$ 的二次多项式三个系数依次为零。

于是(13)的第一行迫 $\alpha_L=\alpha_V=\alpha_Y=0$，第二行迫 $\alpha_R=\alpha_U=\alpha_T=0$，第三行再迫 $\alpha_P=\alpha_S=0$。因此 $E=0$，证明

$$
\boxed{\dim\mathcal B(E_8,\mathfrak H)=8.}
\tag{15}
$$

这是完整 universal 八响应的真独立性。R444 已证明它们在当前固定圆的 period 商中反而全由合法 $L_f$ 像给出，两者没有矛盾：不同观测可以有不同核。

## 5. 原 144 响应像至少 137 维

由(6)(15)，$\beta(N_{QCS})$ 至少八维。限制(1)到十五维空间 $N_{QCS}$，其核仍是 $\ker\beta$，因为(3)。故

$$
\dim\ker\beta
=15-\dim\beta(N_{QCS})\le7.
\tag{16}
$$

因此

$$
\boxed{137\le\dim\mathcal V\le144.}
\tag{17}
$$

同样可写为已付逐层诊断的三个商维数与末完整核：

$$
\dim\mathcal V
=59+32+38+\dim\beta(N_{QCS}).
\tag{18}
$$

没有把八个看不见的方向再错误加到某个已经包含它们的秩上：129 是三层诊断的像维数，八个完整方向位于其核；(16)明确给出了正确的线性代数位置。

R443 的另七条输入依赖，仅说明退化 self-current 零，尚未证明它们完整为零、彼此有怎样的完整关系，或是否落在这八个 hook 像中。因此本文不把(17)下界升为等号，不称恰有七个真实响应关系。

## 6. K11 与全部 144 响应像交零，增广像至少 148 维

令 $\mathcal K$ 为 R435 的十一维完整 K 链。其 whole-Q、三尾 Af-current 都为零；其 self-current 的11列已经在 R443 的新 union 中与38维 $\mathscr S_{53}$ 交零。

若 $K\in\mathcal K\cap\mathcal V$，取 $\lambda\in\mathbb R^{144}$ 使 $K=\beta\lambda$。因为 $K$ 的前两层诊断为零，必有 $\lambda\in N_{QC}$。所以 $K$ 的 self-current 既在 K11 self 像中，又在 $\mathscr S_{53}$ 中。R443 的准确 union 秩49迫它为零；K11 self 独立再迫 $K=0$。于是

$$
\boxed{\mathcal K\cap\mathcal V=\{0\},\qquad
\mathcal K+\mathcal V=\mathcal K\oplus\mathcal V.}
\tag{19}
$$

故完整增广响应像满足

$$
\boxed{148\le\dim(\mathcal K+\mathcal V)\le155.}
\tag{20}
$$

相应155维原系数到完整响应的核与(1)的核相同，维数至多7。R443 的49维只描述其中保 whole-Q/current 后的**退化 self-current 像**；(20)描述整个完整响应空间。两个数字不应互相替换。

## 7. 对当前主问题的准确用途与边界

(15)—(20)解释了 R443 那十五条退化 self 核关系为何不能被称为十五条完整响应恒等式，并给完整 144 模块的下一最小未付问题：判定余下完整核的至多七维，须用原完整成本，不能再只看 Af self。

本文未扩大固定镜点的49列评价秩，未改变 R444/R445 的最高规范盲行，也没有以 universal 真独立授 actual 有号负成本。原型、重复次数乘基准、桥、whole $J^+$ 与同一合法窗口的联合实现仍须保留。

[R247](R247-complete-response-Jacobi-presentation-and-pure-kernel-decomposition.md) 的全 $\mathcal R$ 228—232范围仍按原稿，不由(20)改成全空间分类。特别 $\mathcal R_{71}\cap\ker\pi$ 还有未证明由本144和K11覆盖的部分。当前真实全部 Af 根、两个 period 特解、同一个十三行规范、高阶收敛及同g有限嵌入族依旧未完成；继续 open 的这些具体问题。
