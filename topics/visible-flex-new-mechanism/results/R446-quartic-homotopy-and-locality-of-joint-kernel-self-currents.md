# R446 — whole-Q 与三尾 current 联合核的 self 局部性：四次 homotopy、真双端与高 jet 抵消

## 0. 结论和准确范围

本稿给出一个独立纸面定理，解释 [R443](R443-complete-self-image-of-the-paid-joint-kernel-and-forty-nine-formal-directions.md) 中出现的完整局部性。没有运行新的符号、秩、profile 或检查任务，也没有修改或重跑 R443。

取原 $E8\times Z$ 的 144 个响应的一个固定实系数组合

$$
V=\sum_{E,\tau}\lambda_{E,\tau}B_E\tau.
\tag{1}
$$

假设：

1. $V$ 的 **whole universal self-Q 为零**；
2. 对全部三个真实右包尾矩，其完整 ordered current 在
   $\mathcal A_u=6u'u'''-2(u'')^2=0,\ u'\ne0$ 上恒为零。

则 $V$ 的完整 self 累计流，在这些退化点上是一个局部三阶 jet 表达式；施加单点关系 $u'''=(u'')^2/(3u')$ 后，得到局部 Laurent 多项式。所有真实右积分和高于三阶的外 jet 都准确消失。

本定理不单独证明 Laurent 的 $u'$ 分母也消失。R443 的 53 个具体输入已在唯一实际中进一步得到分母阶数全部为零。它也不把“whole-Q 为零”换成一个或有限多个 profile 上的 self 值为零，不把三个 formal 尾 current 核换成少数固定点的零查询。

## 1. 原右锚、E8 分解与十八算子的阶界

记

$$
p=u',\quad r=u'',\quad t=u''',\quad
I(F)(x)=\int_{r_*}^{x}F,\quad J=-I,
$$

$$
j_0=r^2,\qquad j_1=xr^2,\qquad
j_2=x^2r^2+2p^2,\qquad J_j=J(j_j).
\tag{2}
$$

特别保 $J_2$ 的 $2p^2$。原八个二次输出准确写为

$$
q_E=\Phi_E(u,u)=d_E+\sum_{j=0}^2t_{Ej}(x)J_j.
\tag{3}
$$

| $E$ | $d_E$ | $(t_{E0},t_{E1},t_{E2})$ |
|---|---|---|
| $P$ | $0$ | $(1,0,0)$ |
| $R$ | $p^2$ | $(x,0,0)$ |
| $S$ | $0$ | $(0,1,0)$ |
| $L$ | $up-xp^2/2$ | $(-x^2/4,0,1/4)$ |
| $U$ | $xp^2$ | $(0,x,1/2)$ |
| $V=p_1$ | $-u^2/2+xup-x^2p^2/2$ | $(0,-x^2/4,0)$ |
| $T$ | $x^2p^2$ | $(0,0,x)$ |
| $Y=p_2$ | $-xu^2+x^2up-x^3p^2/2$ | $(0,0,-x^2/4)$ |

这是原 [R434](R434-complete-self-kernel-and-three-tail-current-image-on-144-original-responses.md) 使用的 E8 原输出；本表正是 R434/R443 冻结 source 的 quadratic_operators 原定义。这里 $V$ 在表中是算子 $p_1$，(1) 的 $V$ 是完整响应组合，两者由下标区分。

对每个原 $\tau\in Z$，沿 [R258](R258-self-adjoint-hook-green-operator-and-complete-period-interface.md)、[R261](R261-eight-local-self-adjoint-hook-operators-and-full-third-kernel.md)，

$$
\mathscr A_{\tau,u}
 =D^2(a_\tau D^2)+D(b_\tau D)+c_\tau,\qquad
\mathscr A_{\tau,u}u=0.
\tag{4}
$$

$a,b,c$ 都是显式 $x$ 的局部二次 jet 多项式，且

$$
\operatorname{ord}_u a_\tau\le3,\qquad
\operatorname{ord}_u c_\tau\le5.
\tag{5}
$$

八个 $\chi$ 的 (5) 直接见 R261 §3 的完整表；没有从对角近似推阶界。十个旧方向由 $H_0,J_0$ 的原系数和 R258 的 $\delta$ 递推得到。令 $\mathcal D u=x^2p-2xu$，有

$$
D^j(\mathcal D u)
 =x^2u^{(j+1)}+2(j-1)xu^{(j)}
   +j(j-3)u^{(j-1)}.
\tag{6}
$$

递推中的 $x^2Da-Da[\mathcal D u]$ 抵消最高的输运项，不增加 $a$ 的 jet 阶；$b$ 额外只有 $2a'$，$c$ 额外只有 $2b'$。原 $a$ 阶不超过 3、$b$ 阶不超过 4、$c$ 阶不超过 5 的界因而沿十个旧方向保持。对八个 $\chi$，后文只需 (5) 与完整 (4)，不需要重算 $b=d-a''$ 的消项。

设

$$
h_\tau=(a_\tau r)'+b_\tau p.
$$

(4) 给出

$$
h_\tau'=-c_\tau u.
\tag{7}
$$

由右端阶数不超过 5，局部多项式 $h_\tau$ 的阶数必不超过 4；若有最高 jet $u^{(m)},m\ge5$，其导数中的独立 $u^{(m+1)}$ 项无法被右端吸收。这个论证不除 $u$。

## 2. 一个保原双端的齐次原函数引理

对局部有限 jet 密度 $F(x,u,\ldots,u^{(M)})$，记 Euler 算子

$$
\mathcal E(F)=\sum_{m=0}^M(-D)^m
 \frac{\partial F}{\partial u^{(m)}}.
$$

若 $F$ 对所有 profile jets 齐次次数为 $d>0$，则逐项分部恒等式给

$$
dF-u\mathcal E(F)=D\mathcal B_F,
\tag{8}
$$

$$
\mathcal B_F=
\sum_{m=1}^M\sum_{k=0}^{m-1}
 (-1)^k u^{(m-1-k)}
 D^k\!\left(\frac{\partial F}{\partial u^{(m)}}\right).
\tag{9}
$$

若 $\int F=0$ 对每个真紧 profile 成立，原紧支变分给 $\mathcal E(F)=0$，于是

$$
DF^{[-1]}=F,\qquad
F^{[-1]}=\frac{\mathcal B_F}{d}.
\tag{10}
$$

$F^{[-1]}$ 仍为齐次 $d$ 的局部多项式，因此在两个真实平 collar 都为零。特别地

$$
I(F)=F^{[-1]}
\tag{11}
$$

保留的是原右锚的准确原函数，不是模一个任意常数的形式等号。

若 $F$ 阶数不超过 $m$，(10) 的局部原函数经恒等消项后阶数不超过 $m-1$：否则 $D F^{[-1]}$ 的最高独立 jet 不能出现在 $F$ 中。这一阶界论证只是多项式恒等式，不需另做任何科学求值。

后文分别使用 $d=2$ 和 $d=4$。四次密度的因子是准确的 $1/4$。

## 3. whole-Q 先使三个尾密度具有真局部原函数

原响应的完整 whole-Q 身份为

$$
Q_V(u)=-\frac14\int
 \sum_{E,\tau}\lambda_{E,\tau}c_{\tau,u}\,q_E(u).
\tag{12}
$$

这来自原 $2K$ self 的真实左二次系数，见 [R297](R297-ordered-platform-matrix-surjective-pure-zero-responses-and-real-control.md) 及 R434 的完整 Q 接口。它不是将 Q 的密度误当为已积分的 $I(cq)$。

取 $u$ 完全在 $w$ 左方。局部二次 $c_\tau$ 与 E8 内层的混合槽，在不交支撑上没有交叉。$q_E(w)$ 在整个左包上是由 $\mu(w)$ 决定的真实二次尾

$$
p_E(n)=\sum_{j=0}^2t_{Ej}(x)n_j,
\qquad n=\mu(w),
$$

而 $q_E(u)$ 在右包上真为零。由 (12) 的 $a^2b^2$ 系数得到

$$
Q_V(au+bw)\big|_{a^2b^2}
 =-\frac14\int
 \sum_{E,\tau}\lambda_{E,\tau}
 c_{\tau,u}\,p_E(\mu(w)).
\tag{13}
$$

左端在 whole-Q 假设下恒零。

这里无需把物理三矩先任赋。固定一个非零右包，选三个不同的真实平移中心。其矩向量为

$$
(m_0,\ m_1+\xi m_0,\ m_2+2\xi m_1+\xi^2m_0),
\qquad m_0>0.
$$

三个不同 $\xi$ 的 Vandermonde 给真实三矩基。任意紧 $u$ 右侧的零 collar 中可安置这三个有限小包。因此从 (13) 的三个实际值准确推出

$$
\int C_j(u)=0\quad\hbox{对所有真紧 }u,\qquad
C_j=\sum_{E,\tau}\lambda_{E,\tau}c_\tau t_{Ej},
\quad j=0,1,2.
\tag{14}
$$

每个 $C_j$ 是局部二次密度，阶数不超过 5。用 (10) 的二次版本，存在真局部、齐次二次、阶数不超过 4 的 $\nu_j$，满足

$$
\nu_j=I(C_j),\qquad \nu_j'=C_j,\qquad
\nu_j(\ell)=\nu_j(r_*)=0.
\tag{15}
$$

这一步已经保留 whole-Q 的不交有序缺陷。没有假定任何单个 $J_j$ 左紧。

## 4. 剩余完整原函数的四次 homotopy

将 (3) 代入原内层。逐项按原右锚分部：

$$
\begin{aligned}
I\!\left(\sum\lambda c_\tau q_E\right)
 &=I\!\left(\sum\lambda c_\tau d_E+
                    \sum_j C_jJ_j\right)\\
 &=\sum_j\nu_jJ_j+I(H),
\end{aligned}
\tag{16}
$$

其中

$$
H=\sum_{E,\tau}\lambda_{E,\tau}c_\tau d_E
       +\sum_{j=0}^2\nu_jj_j.
\tag{17}
$$

符号由 $J_j'=-j_j$ 决定，所以 (17) 的第二项是加号。

$H$ 是**局部四次**密度，阶数不超过 5。两个端点的 $\nu_jJ_j$ 都为零：右端 $J_j=0$；左端虽然 $J_j=\mu_j(u)$ 可非零，(15) 给 $\nu_j=0$。故 whole-Q 的 (12) 同时给

$$
\int H=0.
\tag{18}
$$

令

$$
M=\frac14\mathcal B_H.
$$

由四次版本 (8)—(11)，

$$
M'=H,\qquad
M(\ell)=M(r_*)=0,\qquad
\operatorname{ord}_u M\le4,
\tag{19}
$$

以及完整原函数身份

$$
\boxed{\displaystyle
I\!\left(\sum\lambda c_\tau q_E\right)
 =M+\sum_{j=0}^2\nu_jJ_j.}
\tag{20}
$$

此处既没有删去真实左常数，也没有用“积分为零”直接把原函数置零。非零的局部 $M$ 和三个 $\nu_jJ_j$ 都保留。

## 5. 完整 self 累计流的全部四阶 jet 抵消

沿 R443 的完整 $2K$ 规范，self 累计流为

$$
\mathfrak S_V
 =2\left\{
  \sum\lambda a_\tau(pq_E''-rq_E')
  +\sum\lambda q_Eh_\tau
  +u\left(M+\sum_j\nu_jJ_j\right)
  \right\}.
\tag{21}
$$

(3) 中 $d_E$ 只含 $u,p$，所以 $q_E'$ 的外 jet 阶不超过 2，$q_E''$ 不超过 3。由 (5)，(21) 的第一项不含 $u^{(4)}$。其余项最多含四阶外 jet。

现在逐项取最高 jet 系数，所有 $J_j$ 均作为原 primitive 保留：

$$
\frac{\partial h_\tau}{\partial u^{(4)}}
 =-u\,\frac{\partial c_\tau}{\partial u^{(5)}}
\tag{22}
$$

来自 (7)；同时 (15)、(17)、(19) 给

$$
\frac{\partial\nu_j}{\partial u^{(4)}}
 =\sum\lambda t_{Ej}\frac{\partial c_\tau}{\partial u^{(5)}},
\qquad
\frac{\partial M}{\partial u^{(4)}}
 =\sum\lambda d_E\frac{\partial c_\tau}{\partial u^{(5)}}.
\tag{23}
$$

第二式中 $\nu_jj_j$ 不含 $u^{(5)}$，所以没有漏项。合并 (22)—(23)：

$$
\begin{aligned}
\frac12\frac{\partial\mathfrak S_V}{\partial u^{(4)}}
&=-u\sum\lambda q_E c_{\tau,u^{(5)}}\\
&\quad+u\sum\lambda
 \left(d_E+\sum_jt_{Ej}J_j\right)c_{\tau,u^{(5)}}=0.
\end{aligned}
\tag{24}
$$

这是原 complete current 的准确抵消，发生在 Af 代入**之前**。没有用退化关系的导数消 $u^{(4)}$，也没有将其列为可忽略高频余项。

因此 (21) 的全部系数只依赖 $x,u,p,r,t$，剩余可能的非局部量仅为原三个 $J_j$。

## 6. 三个剩余原尾的系数恰是完整 ordered current

将 (3) 及其两次真导数展开，(21) 唯一地写为

$$
\mathfrak S_V=\mathfrak L_V+\sum_{j=0}^2\mathfrak C_jJ_j,
\tag{25}
$$

其中局部部分可完整取

$$
\begin{aligned}
\frac12\mathfrak L_V
={}&\sum_{E,\tau}\lambda a_\tau
 \left\{pd_E''-rd_E'
 +\sum_j\left[
 (rt_{Ej}-2pt_{Ej}')j_j-pt_{Ej}j_j'
 \right]\right\}\\
&+\sum_{E,\tau}\lambda d_Eh_\tau+uM,
\end{aligned}
\tag{26}
$$

尾系数为

$$
\boxed{\displaystyle
\mathfrak C_j=
2\left\{
 \sum_{E,\tau}\lambda
 \big[a_\tau(pt_{Ej}''-rt_{Ej}')+t_{Ej}h_\tau\big]
 +u\nu_j
\right\}.}
\tag{27}
$$

(24) 也分别证明这些局部系数的四阶 jet 已消；故 $\mathfrak L_V,\mathfrak C_j$ 都至多三阶。它们分别齐次五次和三次。

对真实右包三矩 $n$，由 (15) 直接得到

$$
\begin{aligned}
\mathfrak C_V(n)
&=2\sum\lambda
 \left[a_\tau\{p\,p_E(n)''-r\,p_E(n)'\}
       +p_E(n)h_\tau\right]\\
&\quad+2uI\!\left(\sum\lambda c_\tau p_E(n)\right)\\
&=\sum_{j=0}^2n_j\mathfrak C_j.
\end{aligned}
\tag{28}
$$

这正是 [R434](R434-complete-self-kernel-and-three-tail-current-image-on-144-original-responses.md) 的原完整三尾 $\mathcal K$。该文坐标按 R433 的 $\mathcal K/4$ 编码，所以 (27) 的完整系数是其对应坐标函数的四倍；零核当然相同。没有把 ordered 的 $1/4$ 偷移到 self 的 $2K$ 上。

根据本稿第二个假设，

$$
\left.\mathfrak C_j\right|_{\mathcal A=0,\ p\ne0}=0,
\qquad j=0,1,2.
\tag{29}
$$

于是 (25) 给出要求的完整结论：

$$
\boxed{\displaystyle
\left.\mathfrak S_V\right|_{\mathcal A=0,\ p\ne0}
 =
 \mathfrak L_V\!\left(x,u,p,r,\frac{r^2}{3p}\right).}
\tag{30}
$$

右端是局部 Laurent 多项式，没有积分字，也没有高于三阶的外 jet。积分字内部从未施加 $t=r^2/(3p)$，单点 Af 关系也从未被微分。

## 7. 与实际 53 列、忠实表示和剩余任务的关系

R443 的输入正是原 144 标签中满足本稿两个假设的 53 条准确系数组合。因此 (30) 给它们的纸面局部性说明；它不依赖该次 self rank 的数值，也不把原 53 条关系重新计算一次。

本稿解释以下三件不同的事：

1. whole-Q 的 universal 假设使 $I(\sum c_\tau q_E)$ 的非局部结构降为准确的 (20)；
2. 原 Green 自伴身份使四阶外 jet 经 (24) 消失；
3. 全三尾 current 核使三个剩余 $J_j$ 的系数在退化点经 (29) 消失。

只知某个完整 self 的积分或有限 natural 值为零，不能代替第一步；只知某些实际 suffix $n_i$ 上的 current 为零，不能自动代替全部三个系数的 formal 核。

(30) 本身还允许 $p^{-1}$。在 $p\ne0$ 上，Laurent 系数比较依自由紧 jet 实现仍是忠实的；若科学表示暂留未约化的非局部词，它应被分类为表示未决，而不是立刻解释成真正非局部函数反例。R443 已在其完整原式中得到更强的 53 列全部无分母、无残余，其像 38、加 K 后 49；这些具体维数仍来自那唯一已付实际。

本稿没有把自由退化 jet 的恒等式变成任何已冻结母包的满秩评价，也不把共同 cap、全部实际根、平台、完整 period 或 13 行同规范条件免费清除。对于更大的 $\mathcal R\cap\ker E$ 或原 $\Theta_{71}(\ker\Pi_{71})$ 外部响应，本稿只在它们另行具备 (3)—(5) 的准确结构时才适用；没有证明 144 加 K 已覆盖全部原响应核。
