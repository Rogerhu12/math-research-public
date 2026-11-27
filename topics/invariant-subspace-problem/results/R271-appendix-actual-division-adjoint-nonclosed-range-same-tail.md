# 原形式除法伴随的同尾奇异列与非闭值域

日期：2026-11-27（台北时间 UTC+8）。

作者：Astra-ISP-8542378f-20261127 / stable_kernel_return；AI-assisted GPT-6 Astra Pro。

**状态：以下两种原模型的真实伴随域内奇异列及非闭值域结论已证明；没有解决两个闭包范围核心，也没有构造未知非零 $W$。**

本稿检查了[实际形式除法闭关系与两个范围核心](../results/R271-appendix-actual-formal-division-closed-relation-and-two-range-cores.md)、[负前缀条件核心](../results/R271-appendix-negative-prefix-extension-and-output-conditioned-division-graph-core.md)和[两条准确 dyadic 图边界](../results/R271-appendix-exact-dyadic-division-graph-boundaries-and-cayley-cost.md)：那些结果使用闭包范围，未将 $\operatorname{Ran}G_0^*$ 本身声称为闭。本稿新增一个实际定义域中的归一列，确认该值域确实不闭。

## 1. 真实定义域与首位对象

仍令 $S=B^*$，$G_0=TJ_B$ 定义在有限坐标向量上。原闭关系给
$$
\mathcal D(G_0^*)=\{y\in\mathcal H:T^*y\in\operatorname{Ran}S\},
\qquad SG_0^*y=T^*y,
\tag{1.1}
$$
以及
$$
S\mathcal H\subset\mathcal D(G_0^*),
\qquad\boxed{G_0^*Sh=T^*h\quad(h\in\mathcal H).}
\tag{1.2}
$$
(1.2) 使用实际有界算子的交换 $T^*S=ST^*$ 和 $S$ 的单射性。下文的所有来源都先写成 $Sh$，所以不只是在形式矩阵上推断其定义域。

按原低位分解，
$$
S=\alpha_0\begin{pmatrix}0&R^*\\I&0\end{pmatrix},
\qquad \|R\|\le\eta_0,
\qquad K=H^2-R,
\tag{1.3}
$$
其中 $\alpha_0=e^{-20}$、$\eta_0=e^{-1070}$。沿用[首位小图](../results/R239-appendix-first-bit-small-graph-and-strong-cross-coupling.md)及[同一 $W$ 的首位来源](../results/R271-appendix-same-w-first-block-domain-and-positive-schur-source-energy.md)的准确算子：
$$
H_N=\sum_{j\ge1}a_jN_j,
\qquad
H_Y=(I-R)\sum_{j\ge1}a_jY_j-R,
\qquad\|H_\bullet\|<13/20.
\tag{1.4}
$$
这里 $N_j,Y_j$（$j\ge1$）指其共同偶、奇位块上原算子的同一个尾作用，没有改换归一化。

令
$$
\widetilde T=\begin{pmatrix}H&I\\R&H\end{pmatrix}.
$$
N 型有 $T_N=\widetilde T$；Y 型有
$$
T_Y=\operatorname{diag}((I-R)^{-1},(I-R)^{-1})\widetilde T.
\tag{1.5}
$$

## 2. 同一个占满尾前缀上的完整估计

在首位之后的尾空间，取
$$
z_q=e_{2^q-1},\qquad q\ge2,
$$
并用 $Q_q$ 表示该尾前 $q$ 位全部占据的投影。高尾的纯创建记为
$$
D_q^*=\sum_{j\ge q+1}a_jE_{j-1}^*,
\qquad
\sigma_q^2=\sum_{j\ge q+1}a_j^2.
\tag{2.1}
$$
因 $z_q$ 在更高尾上是真空，
$$
\|D_q^*z_q\|=\sigma_q,
\qquad \|(D_q^*)^2z_q\|\le\sqrt2\,\sigma_q^2,
\tag{2.2}
$$
后一个式子来自两次纯创建的准确基本对称平方和。积分比较给
$$
\frac1{3(q+2)^3}\le\sigma_q^2\le\frac1{3(q+1)^3}.
\tag{2.3}
$$

下面保留全部原 carry。对 $1\le j\le q$，原逐列二进位式给
$$
\|N_j^*Q_q\|\le\frac{\alpha_{q+1}}{\alpha_j}\le\eta_q,
\qquad
\|Y_j^*Q_q\|\le3\frac{\alpha_{q+1}}{\alpha_j}.
\tag{2.4}
$$
第二式保留 $(I+N_j^*)^{-1}$ 的原范数 $3$。对 $j\ge q+1$，原全算子比较为
$$
\|N_j^*-E_{j-1}^*\|\le\eta_j,
\qquad
\|Y_j^*-E_{j-1}^*\|\le4\eta_j.
\tag{2.5}
$$
又 $\sum_{j\ge1}a_j<13/20$、$\eta_{q+1}\le\eta_q/4$，所以 N 型在整个 $Q_q$ 上有
$\|(H_N^*-D_q^*)Q_q\|\le2\eta_q$。

对 Y 型，先将 $\sum_{j\ge1}a_jY_j^*$ 与 $D_q^*$ 比较，(2.4)--(2.5) 的总额小于 $3\eta_q$。另外
$$
\|R^*Q_q\|=\frac{\alpha_{q+1}}{\alpha_0}\le\eta_q,
\qquad
\left\|\sum_{j\ge1}a_jY_j^*\right\|\le3\sum_{j\ge1}a_j<2.
$$
$R^*$ 与所有这些实际算子交换，故 (1.4) 中剩余的 $R^*$ 两项总额小于 $3\eta_q$。可统一采用
$$
\boxed{\|(H_\bullet^*-D_q^*)Q_q\|\le8\eta_q.}
\tag{2.6}
$$

$D_q^*$ 保持 $Q_q$；因此同一个来源 $z_q$ 上，
$$
(H^*)^2z_q-(D_q^*)^2z_q
=H^*(H^*-D_q^*)z_q+(H^*-D_q^*)D_q^*z_q.
$$
由 $\|H\|<1$、$\|D_q^*\|\le1$ 和 (2.6)，有
$$
\boxed{
\|H^*z_q\|\ge\sigma_q-8\eta_q,
\qquad
\|K^*z_q\|\le\sqrt2\,\sigma_q^2+17\eta_q.
}
\tag{2.7}
$$
所有指数小项仍是原实际权；没有把 $H$ 或 $K$ 替成纯尾。由原 $\eta_q\le e^{-77016^q}$ 与 (2.3)，(2.7) 的第一个下界为正，且 $\eta_q/\sigma_q^2\to0$。

## 3. 实际域中的归一奇异列

N 型取
$$
h_q^N=(-H_N^*z_q,z_q),
\qquad y_q^N=Sh_q^N.
$$
原首位矩阵准确给
$$
\boxed{T_N^*h_q^N=(-K_N^{\mathrm{Schur},*}z_q,0),
\qquad
y_q^N=\alpha_0(R^*z_q,-H_N^*z_q).}
\tag{3.1}
$$
这里 $K_N^{\mathrm{Schur}}=H_N^2-R$；本节的 Schur $K$ 不同于别稿中的 carry 记号 $T_N^*-D^*$。

Y 型令
$$
k_q=(-H_Y^*z_q,z_q),
\qquad
h_q^Y=\operatorname{diag}(I-R^*,I-R^*)k_q,
\qquad y_q^Y=Sh_q^Y.
$$
由 (1.5) 和对角因子与 $S$ 的准确交换，
$$
\boxed{
T_Y^*h_q^Y=(-K_Y^{\mathrm{Schur},*}z_q,0),
\quad
y_q^Y=
\operatorname{diag}(I-R^*,I-R^*)
\alpha_0(R^*z_q,-H_Y^*z_q).
}
\tag{3.2}
$$
两种 $h_q^\bullet$ 均是真正的 Hilbert 向量；因此 $y_q^\bullet\in S\mathcal H\subset\mathcal D(G_0^*)$，且 (1.2) 给的是实际算子等式
$$
G_0^*y_q^\bullet=T_\bullet^*h_q^\bullet.
\tag{3.3}
$$
统一有
$$
\|y_q^\bullet\|
\ge(1-\eta_0)\alpha_0(\sigma_q-8\eta_q)>0.
$$
于是令 $\widehat y_q=y_q^\bullet/\|y_q^\bullet\|$，得到
$$
\boxed{
\|\widehat y_q\|=1,
\qquad
\|G_0^*\widehat y_q\|
\le\frac{\sqrt2\,\sigma_q^2+17\eta_q}
{(1-\eta_0)\alpha_0(\sigma_q-8\eta_q)}
\longrightarrow0.
}
\tag{3.4}
$$
来源 $z_q$ 的整数坐标趋于无穷；$H^*,R^*$ 及 Y 型的 $I-R^*$ 均不降低整数坐标。因此 $y_q^\bullet$ 的支撑整体向无穷移出，归一化不改变支撑，故
$$
\boxed{\widehat y_q\rightharpoonup0.}
\tag{3.5}
$$

## 4. 非闭值域及其准确适用范围

$G_0^*$ 闭且单射：若 $G_0^*y=0$，则 (1.1) 给 $T^*y=0$；原 $T^*$ 的逐行首移位非零，所以 $y=0$。

假如 $\operatorname{Ran}G_0^*$ 闭，则其逆作为从该闭 Hilbert 子空间到 $e_0^\perp$ 的闭算子，按闭图定理有界。这将给
$\|y\|\le C\|G_0^*y\|$，与 (3.4) 矛盾。因此
$$
\boxed{\operatorname{Ran}G_0^*\ \text{确实不闭，原两型皆然。}}
\tag{4.1}
$$
也不存在对全部 $h\in\mathcal H$ 成立的无条件估计
$$
\|Sh\|\le C\|T_\bullet^*h\|.
\tag{4.2}
$$
同样不能只在有限坐标向量上恢复 (4.2)：若有限坐标上有该一致估计，$S,T^*$ 的有界性会将它延拓到整个 $\mathcal H$，仍与本稿序列矛盾。

本稿的输出 $G_0^*y_q=T^*h_q$ 明确位于实际 $\operatorname{Ran}T^*\subset M^\perp$。它不声称 $\widehat y_q$ 属于 $W$，不把范围不闭解释为任一闭包核心失败，更不把它当作同一 $u\in\ker K$、$H^*G_{\rm env}u$ 的 $\Gamma(u)$ 发散证据。实际两个闭包核心与真正 $W$ 的来源费用继续开放。
