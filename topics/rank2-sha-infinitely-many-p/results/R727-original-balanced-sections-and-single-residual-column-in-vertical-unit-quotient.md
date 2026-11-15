# R727 — 原 d^c 截源与两残列在真实垂直单位商中的单列归约

日期：2026-11-15。**状态：已证明。**

本篇继续 R722/R726 的同一个因子、原两 charge 切向返回和旧预算。
使用 R545 已付的真实截面 $d^c$，截源的两个原点坐标可以用
$d^{2c},d^cF$ 整分裂，只需 $b\ge2$。
两条剩余切向列随后有准确的原来源恒等式：
一条全部落入 R547 的真实饱和单位块，
另一条在同一个商中只剩指定的 $F d^cA$。

这里保留 R547 的原 cube 非单位方向。
不是把整个 $F^2\mathcal H_1$ 的像误称为单位像，
也不是将两个分别饱和的子像之和自动认成饱和。
原全 $\mathcal W_D$ 的指定 forcing 与同一 $R$ 仍须经过剩余全部列。

## 1. 同一来源和原角平衡截面

保 R722 的原对象
$$
P^{\rm fact}=q\,t^rF^3,\qquad q=d^{-C_D}Q,\qquad
d=1+8t,\qquad h_7=7+4t+16t^2,
$$
$$
b=\deg_YF,\quad e=\mathcal EF,\quad
\mathcal E=Y\partial_Y,\quad\delta=t\partial_t,\quad
\mathcal V_F=e\delta-(\delta F)\mathcal E,
$$
$$
\mathcal W_F(H)=F\mathcal EH-2eH.
\tag{1}
$$
$F,Q$、同一整 Hensel 点 $\widetilde P$、
十九角曲面 $X$、曲线 $C$、$\kappa=C^2$、
$\chi=-K_XC$ 以及全部 $\mathcal H_i$ 不变。
继续保 $F(P)=0$、$e(P)$ 和 $Q(P)$ 单位、$f_D<p$ 及原整提升。

R545 已逐角证明可以选择实际整数
$$
\boxed{
\mu_{d,1}\le c\le u_{\rm cap}-\mu_{\infty,1},
\qquad u_{\rm cap}=\max_i(\deg f_i-4i),
}
\tag{2}
$$
并且
$$
\boxed{U=d^c\in\mathcal H_1,\qquad U(\widetilde P)=1,\qquad
\mathcal EU=0.}
\tag{3}
$$
例如固定 $c=\mu_{d,1}$。
这是同一个真实线性系中的来源，不是免费在原格中加入 $d^{-c}$。
R545 的证明使用有效的边界平凡化
$\mathscr D_c=\mathscr D+c\,\operatorname{div}(d)$，
其线束与原 $\mathscr D$ 等价。

以下重点为 $Z>0$，故取 $c=\mu_{d,1}\ge1$。
在原 $p>8b^2+4bu_{\rm cap}$ 的范围，$0<c<p$，
所以 $8c,16c$ 都是单位。
若 $Z=0$，取 $c=0$，本篇两条剩余切向来源直接为零，
正好恢复 R722 的该情形。

## 2. 两 charge 的同 D 截源不再需要 i0 的附加门

只使用原
$$
m_{\rm tan}=Y^2(t-1)^2h_7^2,\qquad
\mathcal T_2(H)=q\,t^{r+1}m_{\rm tan}\mathcal V_FH .
\tag{4}
$$
令
$$
\mathcal H_{\rm cut}
=\{H\in\mathcal H_2:\deg_YH\le2b-2\}.
\tag{5}
$$
这是原逐 charge 整直和因子；
R722 同预算增补已证明
$$
\boxed{\mathcal T_2(\mathcal H_{\rm cut})\subset\mathcal W_{D_0}
\subset\mathcal W_D,\qquad D_0=3b+\deg_YQ.}
\tag{6}
$$

若 $b\ge2$，(3) 给
$$
\boxed{
H^{(0)}=U^2=d^{2c},\qquad H^{(1)}=FU=d^cF
\in\mathcal H_{\rm cut}.
}
\tag{7}
$$
在同一原点坐标
$$
\Lambda(H)=\left(H(\widetilde P),
\frac{(\mathcal EH)(\widetilde P)}{e_0}\right),
\qquad e_0=e(\widetilde P),
$$
(7) 分别取 $(1,0),(0,1)$。
因此
$$
\boxed{
\mathcal H_{\rm cut}
=\mathcal H_{\rm cut}^{00}
\oplus\mathcal O H^{(0)}\oplus\mathcal O H^{(1)}.
}
\tag{8}
$$
这里 $\mathcal H_{\rm cut}^{00}=\ker\Lambda$。

这保 R722 原同预算单位块，只把分裂截面换为已经支付的 (3)。
不再需要低 charge 选择中的 $b\ge i_0+2$；
在原几何和角平衡条件下，$b\ge2$ 已足够。

对相对 $J$ 和完整原 $M$，切向单位块的准确长度仍分别为
$$
T_1=s-r-1,\qquad T_1=s-r-14.
\tag{9}
$$
保 $T_1>2\kappa,\ h>\kappa$ 时，
$\mathsf M_0\mathcal T_2$ 在 $\mathcal H_{\rm cut}^{00}$ 上
仍是原整饱和单位块，$\mathsf M_0=J$ 或 $M$；
未将两种长度互换。

## 3. 关键实际 H1 截面及全部十九角

定义
$$
\boxed{
A=t^2Y^2(t-1)^2h_7^2d^{c-1}
=t^2m_{\rm tan}d^{c-1}.
}
\tag{10}
$$

**引理 1。** 在 $c\ge1,b\ge2$ 下，$A$ 是同一原 $\mathcal H_1$ 的整截面，
而且
$$
\mathcal EA=2A,\qquad A\in t^2\mathcal O[t,Y].
\tag{11}
$$

**证明。** 将 $A=U N$，其中
$$
N=\frac{t^2Y^2(t-1)^2h_7^2}{d}.
\tag{12}
$$
$U$ 已属于 $\mathcal H_1$。
因为 $c\ge1$，$A$ 没有新 $d$ 分母。
它唯一的 $Y$ 次数为二，满足 $2\le b$；
相应 $t$ 次数为 $c+7\le u_{\rm cap}+7<u_{\rm cap}+8$，
所以原 ambient 帽成立。

还须逐条保持中间角。用原链的序号 $j$，准确有：

| 原例外链 | 序号 | $v_j(N)$ |
|---|---:|---:|
| $0$ 的 $Y=\infty$ 链 | $1\le j\le4$ | $2j-2$ |
| $h_7$ 每个根的 $Y=\infty$ 链 | $1\le j\le4$ | $2j-2$ |
| $1$ 的 $Y=\infty$ 链 | $1\le j\le3$ | $2j-2$ |
| $d=0,\ Y=0$ 链 | $j=1,2$ | $2-j$ |
| $t=\infty,\ Z=0$ 链 | $j=1,2$ | $j+2$ |

前十五项直接读相应有限参数与 $Y$ 的原权 $(j,-1)$；
$d$ 链用 $(v(d),v(Y))=(j,1)$。
无穷远取 $\zeta=1/t,\ Y=\zeta^4Z$；
(12) 为 $\zeta Z^2$ 乘原局部单位，
该链上 $(v(\zeta),v(Z))=(j,1)$，给最后一行。
十九个值全部非负，
故乘 (12) 不降低 $U$ 已满足的任何中间角条件。
再结合已核的原纤维/ambient 帽，即得 $A\in\mathcal H_1$。
(11) 直接由 (10) 成立。证毕。

### 三 charge 版本的准确例外

不能把此引理未经修改用于
$m_{{\rm tan},3}=Y^3(t-1)^2h_7^3d^2$。
其对应 $A_3/U$ 在 $0$、$1$ 的第一中间角分别有值 $-1$；
这些负一必须由同一个 $F$ 的实际余量另付。
本篇不假定该余量，也不声称三 charge 的无条件 $\mathcal H_1$ 包含。
以下所有结论只使用 (4)、(10)。

## 4. 两条剩余来源的完整恒等式

由 (3)，
$$
\mathcal V_FU=e\delta(d^c)=8ctd^{c-1}e.
$$
因此 (7) 的两条切向来源准确为
$$
\boxed{
\begin{aligned}
\mathcal T_2(H^{(1)})&=8c\,q t^r eFA,\\
\mathcal T_2(H^{(0)})&=16c\,q t^r eUA.
\end{aligned}}
\tag{13}
$$
这里多出的公共 $t^{r+2}$ 来自 (10)，不只是约化后的消失阶估计。

因 $\mathcal EA=2A$、$\mathcal EU=0$，
原垂直算子给两个整恒等式
$$
\begin{aligned}
\mathcal W_F(FA)&=2F^2A-eFA,\\
\mathcal W_F(UA)&=2FUA-2eUA.
\end{aligned}
$$
所以
$$
\boxed{
\begin{aligned}
\mathcal T_2(H^{(1)})
&=8c\,q t^r\{2F^2A-\mathcal W_F(FA)\},\\
\mathcal T_2(H^{(0)})
&=16c\,q t^rFUA-8c\,q t^r\mathcal W_F(UA).
\end{aligned}}
\tag{14}
$$
引理1保证 $FA,UA\in\mathcal H_2$、$F^2A,FUA\in\mathcal H_3$。
因此 (14) 中每一项均由原 R495/R547 返回同一 $\mathcal W_D$，
不增加 charge，不依靠物理评价后的拟合。
这是特征零整来源身份，自动保模 $p^2,p^3$。

## 5. 选择真正单位块时必须保原 cube

R547 的整个呈示
$$
(H,K)\longmapsto q t^r\{\mathcal W_FH+F^2K\},
\qquad H\in\mathcal H_2,\ K\in\mathcal H_1,
\tag{15}
$$
含原 $K=F$，其来源恰为 $P^{\rm fact}$。
在该显示子格中，这一最后方向的 Smith 因子为 $p$，不是单位。
因此不能把 (15) 的整个像当作本节要商去的饱和单位块。

现在明确选择一个包含 $A$、排除 $F$ 的实际整补。
取任一 $i_*$ 使 $f_{i_*}(0)\in\mathcal O^\times$；
这样的系数由 $F(P)=0,e(P)\ne0$ 存在。
在原多项式呈示中定义
$$
\lambda(K)=\frac{[t^0Y^{i_*}]K}{f_{i_*}(0)},\qquad
\mathcal L=\ker\lambda\subset\mathcal H_1.
\tag{16}
$$
则
$$
\boxed{
\lambda(F)=1,\quad\lambda(A)=0,\quad
\mathcal H_1=\mathcal L\oplus\mathcal OF,\quad A\in\mathcal L.
}
\tag{17}
$$
第二式使用 $A$ 的真实 $t^2$ 因子。
这里不是只在约化后任选一个不保持高位的补空间。

无额外 $t$ 的垂直联合块使用的准确长度为
$$
T_0=s-r\quad(J),\qquad T_0=s-r-13\quad(M).
\tag{18}
$$
保 R547 的实际强门
$$
\boxed{T_0>2\kappa,\qquad h>\kappa,\qquad T_0-h>\kappa.}
\tag{19}
$$
此时
$$
\boxed{
\mathsf B_{\rm v}:
(\mathcal H_2/\mathcal OF^2)\oplus\mathcal L
\longrightarrow\mathscr T_0,\qquad
(H,K)\mapsto
\mathsf M_0\bigl(qt^r(\mathcal W_FH+F^2K)\bigr)
}
\tag{20}
$$
为同一原完整目标中的分裂整单射，
全部 $(5\kappa+3\chi)/2$ 个因子为单位。

这是 R547 已证明的真实物理核：
(15) 模 $p$ 的核准确由 $(F^2,0),(0,F)$ 给出；
(17) 排掉第二条，第一条则是整来源的零关系。
所以 (20) 约化满列秩，得到整左逆和自由余核。
原 cube 并未在此过程中删除。

## 6. 同一整商中准确只剩一条指定列

取 (20) 的整个整目标商
$$
\pi_{\rm v}:\mathscr T_0\longrightarrow
\mathscr Q_{\rm v}:=\mathscr T_0/\operatorname{im}\mathsf B_{\rm v}.
\tag{21}
$$
这是有限自由整模。
因为 $A\in\mathcal L$、$FA,UA\in\mathcal H_2$，
(14) 给真正的全精度身份
$$
\boxed{
\begin{aligned}
\pi_{\rm v}\mathsf M_0\mathcal T_2(H^{(1)})&=0,\\
\pi_{\rm v}\mathsf M_0\mathcal T_2(H^{(0)})
&=16c\,\pi_{\rm v}\mathsf M_0(qt^rFUA).
\end{aligned}}
\tag{22}
$$
定义唯一显示的剩余列
$$
\boxed{
z_c=\pi_{\rm v}\mathsf M_0(qt^rFUA).
}
\tag{23}
$$
它由同一个 $F$、实际角整数 $c$、明确 (10) 和原评价给定，
不是任意填入的一条商方向。

由 (8)，整个切向截源在这个商中的像准确为
$$
\boxed{
\pi_{\rm v}\mathsf M_0\mathcal T_2(\mathcal H_{\rm cut})
=
\pi_{\rm v}\mathsf M_0\mathcal T_2(\mathcal H_{\rm cut}^{00})
+\mathcal O\,(16c\,z_c).
}
\tag{24}
$$
这在整系数及模 $p,p^2,p^3$ 下同时成立。
没有声称 $z_c$ 非零、是单位列、或已经属于前一项；
这三种可能仍需真实同源评价判定。

同样不能将 (20) 的单位数与 R722 的切向单位数直接相加。
在 (21) 之后，
$\pi_{\rm v}\mathsf M_0\mathcal T_2|_{\mathcal H_{\rm cut}^{00}}$
可能有新的交、核或非单位因子，
它不因商前是单位块而自动保饱和。
(24) 的意义是去掉第二个指定余列所需的成本已经由真实整身份支付。

## 7. 原首核、指定 forcing 和同一个 R

R722 的原首核维数不等式是在原切向矩阵中成立。
(22) 的第一条却来自**来源本身**落入 (20) 的子格：
消元时它的剩余来源坐标也为零。
所以它不产生一条新的非零 $\ker\bar J$ 或 $\ker\bar M$ 元素，
不能把这个精确重叠错误加入原核维数。

对 R726 的指定目标，正确接续是：
先将其整个 (21) 高尾公式、两条十三行和全部原低行
同其他原列一并运输到 (21)；
再在 (24) 的整像及其余全部 $\mathcal W_D$ 列中求同一个原像。
R726 已证它退出切向 $00$ 单位块；
但商去 (20) 后能否为零或落在 (24)，并未由此判定。

对同一个
$$
P_2=P^{\rm fact}+pR,
$$
(20) 的 Schur 消元只给一个确定的整基变换。
因为 $P^{\rm fact}$ 在原首核中，
消去其单位行时的来源修正系数被 $p$ 整除；
因此约化候选保持，第一修正按同一个基变换运输，
不成为两个可独立选择的 $R$。

原 $P_{134}/U_0$、$U_1/p$、两条十三行 carry、
原低行右逆的高尾、最后 cube 的 $p$ 因子和第三精度 $d_2/G_2$ 全部保留。
(22)–(24) 没有新增中央零，
也没有将任何指定子像商中的非零当成完整 $\mathcal W_D$ 余类非零。

依赖：[R545](R545-angular-balanced-connection-and-full-physical-unit-block.md)；
[R547](R547-zero-charge-vertical-unit-block-and-actual-cubic-schur-column.md)；
[R722](R722-actual-tangent-two-constant-kernel-and-specified-residual-columns.md)；
[R722 同预算增补](../notes/2026-11-15-r722-original-budget-truncated-tangent-unit-block.md)；
[R726](R726-low-ell-three-charge-multiplier-and-actual-forcing-unit-block.md)。
