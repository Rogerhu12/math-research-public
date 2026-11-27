# 最大实际图来源在低余孔扇区中的首缺位平方费用

日期：2026-11-27（Asia/Taipei）。

作者：Astra-ISP-8542378f-20261127 / stable_kernel_return；AI-assisted GPT-6 Astra Pro。

**状态：本文无条件支付实际最大图来源的一部分 $C_2$ 逆权，并证明物理孔数有界的实际输入 $y$ 已在原图核心。没有把余下扇区的同一来源费用写成已付，也没有证明完整图核心、同 $W$ 的 $\Gamma$ 或 $N=M$。**

两型 $T_N,T_Y$ 都使用原全部 carry。记 $S=B^*$、$G=G_0^*$，取任意实际最大图对
$$
y\in\mathcal D(G),\qquad f=Gy,\qquad T^*y=Sf.
$$
域的真空条件 $y_0=0$ 已付，故存在唯一规范形式来源 $h$，满足
$$
Sh=y,\qquad T^*h=f.                                      \tag{0.1}
$$
此处未预设 $h\in\mathcal H$。

沿用[相反前缀图正则性](R271-appendix-maximal-division-graph-opposite-prefix-regularity.md)、
[临界来源与总孔核心](R271-appendix-critical-fifteen-sixteenths-carry-domain.md)，以及
[Y 型共同平方来源核心](R271-appendix-y-carry-first-gap-row-domain-and-common-square-source-core.md)。

## 1. 不同于指数前缀界的原 creation 能量

$\mathsf P_p$ 表示总物理孔数 $p$ 的正交投影，$V_r$ 表示低 $r$ 位全空；记
$$
D_r=\sum_{j\ge r}a_jE_j,\qquad a_j=(j+1)^{-2},\qquad
\sigma_r^2=\sum_{j\ge r}a_j^2.
$$
在高尾物理孔数 $p$ 层上，精确 Boolean 交换子为
$$
D_rD_r^*-D_r^*D_r
=\sum_{j\ge r}a_j^2(I-2n_j).
$$
因为 $p$ 个占据位的加权和最多为最大的 $p$ 个权之和，对任意该层向量 $g_p$，
$$
\boxed{
\|D_r^*g_p\|^2
\ge\left(\sigma_r^2-2\sum_{j=r}^{r+p-1}a_j^2\right)\|g_p\|^2
=(2\sigma_{r+p}^2-\sigma_r^2)\|g_p\|^2.}                   \tag{1.1}
$$
负右边当然仍成立；只在下面明确的正区间使用。

给定
$$
0<c<2^{1/3}-1,\qquad
\zeta_c=\frac{2/(1+c)^3-1}{3}>0,\qquad
m_r=\lfloor cr\rfloor-1.
$$
当 $m_r\ge0$ 且 $0\le p\le m_r$ 时，$p+1\le cr$。积分界
$$
\sigma_{r+p}^2\ge\frac1{3(r+p+1)^3},\qquad
\sigma_r^2\le\frac1{3r^3}
$$
给
$$
2\sigma_{r+p}^2-\sigma_r^2\ge\frac{\zeta_c}{r^3}.          \tag{1.2}
$$

前稿已经保原 carry 证明
$$
\|D_r^*V_ry\|\le8\eta_{r-1}\|y\|+\alpha_r\|f\|,
\qquad \eta_j=\alpha_{j+1}/\alpha_j.                     \tag{1.3}
$$
$D_r^*$ 将不同物理孔层送到不同的正交层；因此可以从整个 (1.3) 中保留任意一批来源层，而不用对截断后的 $y$ 假设另一个最大图域条件。由 (1.1)--(1.3)，
$$
\boxed{
\|V_r\mathsf P_{\le m_r}y\|
\le\frac{r^{3/2}}{\sqrt{\zeta_c}}
 \left(8\eta_{r-1}\|y\|+\alpha_r\|f\|\right).}             \tag{1.4}
$$
这是 $\eta_{r-1}$ 级别的实际低孔前缀界，不是把已付的 $e^{-\gamma r}$ 界改名。

## 2. 同一个规范来源的准确孔数换算

$P_q$ 表示 $h$ 的首缺位 $q$。其坐标指标 $n$ 的低 $q$ 位全一，第 $q$ 位为零；$S$ 将其送到指标 $n+1$，其 $2$-进赋值正是 $q$，权恰为 $\alpha_q$。

若 $s(n)$ 是总物理孔数，则
$$
s(n+1)=s(n)-q+1.                                         \tag{2.1}
$$
因此输出 $y$ 的物理孔数是来源 $h$ 的总孔数减首缺位再加一；不能用总孔数本身替换它。

记
$$
P_q^+=V_q-V_{q+1},\qquad
b_0=\eta_0,\quad b_q=a_{q-1}\eta_{q-1}=q^{-2}\eta_{q-1}
\quad(q\ge1),
$$
$$
\|u\|_{C_2}^2=\sum_{q\ge0}b_q^2\|P_qu\|^2.
$$
由 (0.1)，每一个固定 $q$ 块 $P_qh$ 已在 $\mathcal H$，准确满足
$$
\|P_qh\|=\alpha_q^{-1}\|P_q^+y\|.                        \tag{2.2}
$$
这里不从逐块有界推出全部 $C_2$ 和可收敛。

## 3. 自动可支付的扇区

置 $q_c=\lceil2/c\rceil$。定义规范形式来源的一个坐标投影
$$
\Pi_ch=
\sum_{q<q_c}P_qh+
\sum_{q\ge q_c}P_q\mathsf P_{\le q+m_q-1}h.               \tag{3.1}
$$
小 $q$ 有限块全部保留；大 $q$ 只保留
$s(n)-q+1\le m_q$ 的真实坐标。

由 (2.1)--(2.2)，大 $q$ 项准确为
$$
b_q^2\|P_q\mathsf P_{\le q+m_q-1}h\|^2
=\left(\frac{b_q}{\alpha_q}\right)^2
 \|P_q^+\mathsf P_{\le m_q}y\|^2.
$$
应用 (1.4)，再用 $(u+v)^2\le2u^2+2v^2$，得到
$$
\boxed{\|\Pi_ch\|_{C_2}^2
\le K_c(\|y\|+\|f\|)^2,}                                \tag{3.2}
$$
其中可取明确的有限常数
$$
K_c=
\sum_{q<q_c}\left(\frac{b_q}{\alpha_q}\right)^2+
\frac{128}{\zeta_c}\sum_{q\ge1}\frac1q
       \left(\frac{\alpha_q}{\alpha_{q-1}^2}\right)^2+
\frac{2}{\zeta_c}\sum_{q\ge1}\frac1q\eta_{q-1}^2.          \tag{3.3}
$$
延长正项和至全部 $q\ge1$ 只增大常数。第一项包含 $q=0$，因此没有漏掉该块。

为直接核实收敛，原 $\alpha$ 的准确归一化给
$$
-\log\alpha_q
=\frac{280}{3}16^q-90\,8^q+300\,2^q-\frac{850}{3}.
$$
所以对 $q\ge1$，
$$
-\log\frac{\alpha_q}{\alpha_{q-1}^2}
=\frac{3920}{3}16^{q-1}-540\,8^{q-1}+\frac{850}{3}
\ge\frac{2300}{3}16^{q-1}.
$$
结合 $\eta_{q-1}\le e^{-770\,16^{q-1}}$，(3.3) 的两个无限和分别至多为
$$
\frac{e^{-4600/3}}{1-e^{-23000}},\qquad
\frac{e^{-1540}}{1-e^{-23100}},
$$
因为 $16^j\ge1+15j$。所有估计保留同一个 $h$，没有改成无关的通用来源。

例如 $c=1/5$ 时，$\zeta_c=17/324,\ q_c=10$；除前十个完整首缺位块外，自动支付的扇区是
$$
q\ge10,\qquad s(n)\le q+\lfloor q/5\rfloor-2.
$$

## 4. 有界物理孔输入的原图核心

**推论。** 若实际 $y\in\mathcal D(G)$ 还满足
$$
\mathsf P_{\le P}y=y
$$
（$P$ 为某个有限整数），则其规范形式来源 $h\in C_2$，并且
$$
(y,Gy)\in\mathcal C
=\overline{\{(Sg,T^*g):g\in\mathcal H\}}.                 \tag{4.1}
$$

事实上，对足够大的 $q$，有 $m_q\ge P$，故这些 $P_qh$ 全部已被 (3.1) 保留。剩余只有有限个 $q$，由 (2.2) 各自具有有限费用；所以整个 $h\in C_2$。

这里使用的是已证明的共同平方来源图核心：
对 N 型，$K_N:C_2\to\mathcal H$ 有界，所以
$D^*h=f-K_Nh\in\mathcal H$。各物理来源层在 $\mathcal H$，因为总孔 $p$ 层只含 $q\le p$ 的有限个首缺位块。总孔截断 $h^{\le p}$ 满足
$Sh^{\le p}\to y$、$K_Nh^{\le p}\to K_Nh$，以及
$D^*h^{\le p}=\mathsf P_{\le p+1}D^*h\to D^*h$。
对 Y 型，直接使用已付的完整共同平方来源核心；它以
$D^*-V_b$ 的严格升孔身份和完整余 carry 证明相同结论，不要求另外假设 $K_Yh\in\mathcal H$。

最后按每个实际 $h^{\le p}\in\mathcal H$ 的有限坐标逼近，得到 (4.1) 的原核心身份。
注意本推论限制的是 $y$ 的孔数，不是 $h$ 的孔数；由 (2.1)，即使 $P=1$，$h$ 仍可含无界总孔层，所以这没有重复“来源 $h$ 有限孔”的旧核心。

若 $(y,f)\in\mathcal E$ 且 $y$ 的物理孔数有界，(4.1) 与 $\mathcal E\perp\mathcal C$ 立即给 $(y,f)=0$。

## 5. 未支付部分

(3.2) 只控制实际坐标扇区 (3.1)。余部可以同时有较大的总孔数和较小的首缺位；本文没有给其 $C_2$ 和任何上界。

实际缺陷的两条耦合方程、同 $W$ 的来源以及完整图核心仍须处理该余部。物理孔截断后的任意 $y$ 不会仅因 Hilbert 收敛就自动留在 $\mathcal D(G)$；本文也没有作这个推断。
