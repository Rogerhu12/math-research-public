# R792 — 原常数 charge 非零窗口的完整 r/k 分类与三次因子排除扩展

日期：2026-11-15。**状态：以下来源分类、全素数排除扩展和剩余最低 charge 界已证明。**

本文继续同一原来源的有限纤维窗口，不另设 $m_q=0$。
只要 $q(t,0)\ne0$，原常数 charge 就迫使 $r\in\{2,3,4\}$、$k_{\rm carry}=0$，并仍迫 $F(t,0)$ 为固定 $d$ 的幂。
在原 $\mathbf F_p$ 系数范围，全部可能归一因子落入十三个显示系数格。
其中 r=2 的五格与 R782 完全相同，所以 R788 的 b=3 全素数排除扩展到这一整个常数 charge 非零范围。

这里的 scalar 返回只用于因子存在性的必要条件。
它不替换已经固定的 $P_2=P^{\rm fact}+pR$；
特别 $m_q=1$ 时，R782 的第三块不变结论不能照搬。
常数 charge 为零的余支仍用原最低非零 charge 处理，不能免费除 Y。

## 1. 同一原格与实际零角预算

保持 R768 的原范围：
$$
P^{\rm fact}=qt^rF^3\in\overline{\mathcal W}_D,\qquad
q=d^{-C_D}Q,\qquad d=1+8t,\qquad Q\in\mathbf F_p[t,Y],
\tag{1}
$$
$$
0\le k_{\rm carry}<\ell\le r\le13<h,\qquad
p=6s-1>101,\qquad f_D<p,
\tag{2}
$$
$$
b=\deg_YF,\quad b_0=\deg_YF(0,Y)>4k_{\rm carry}+2,\quad
F(0,1)=0,\quad F_Y(0,1)q(0,1)\ne0.
\tag{3}
$$
F 是原 primitive 不可约因子，原几何整性、精确接触和所有长度门继续保留。
本篇的 r/k 分类不先指定 $\ell=1$；
只有应用 R788 时才再次使用该篇的 $r=2,\ell=1,s=2h+2$。

沿 R782，令
$$
h_7=16t^2+4t+7,\qquad
A_n=\left\lfloor\frac{n+1}{4}\right\rfloor,\quad
B_n=\left\lfloor\frac{n+1}{3}\right\rfloor,\quad
C_n=\left\lfloor\frac n2\right\rfloor,
$$
$$
f_n=\left\lfloor\frac{9n}{2}\right\rfloor+4,\qquad
q_n=(th_7)^{A_n}(t-1)^{B_n}d^{-C_n},\qquad
e_{n+1}=f_n-3A_n-B_n+C_n.
$$
原第 n 条系数是 $q_n\mathbf F_p[t]_{\le e_{n+1}}$。
等价的完整 Gauss 条件为
$$
\begin{array}{c|c|c}
\text{角}&v(\sum P_nY^n)&\text{下界}\\ \hline
0,\ h_7(\alpha)=0&\min_n(4\operatorname{ord}_\alpha P_n-n)&-2\\
1&\min_n(3\operatorname{ord}_1P_n-n)&-1\\
d=0&\min_n(2\operatorname{ord}_dP_n+n)&0\\
\infty&\min_n(9n-2\deg_tP_n)&-8 .
\end{array}
\tag{4}
$$
保仅有 d 极和原 Y 次数帽时，(4) 是原十九角的双向识别。

记
$$
m=-v_0(F),\qquad m_q=-v_0(q).
$$
由 (3)，$m\ge b_0$；又 $q(0,Y)$ 不是零多项式，所以 $m_q\ge0$。
乘法赋值精确相加，给出
$$
\boxed{3m+m_q\le4r+2,\qquad
r\ge3k_{\rm carry}+2.}
\tag{5}
$$
后一式由 $b_0\ge4k_{\rm carry}+3$ 直接得到。

## 2. 非零常数 charge 强制 r≤4 及固定常数因子

本节唯一新增假设为
$$
\boxed{q_0(t):=q(t,0)\ne0.}
\tag{6}
$$
F 不是 Y，故 $F_0(t):=F(t,0)\ne0$。
原第零条系数恰为次数至多四的多项式，因此
$$
0\ne t^rq_0(t)F_0(t)^3\in\mathbf F_p[t]_{\le4}.
\tag{7}
$$
q0 只在 d 有极，在 t=0 正则；F0 是多项式。
所以 (7) 在零点的阶至少 r，得 $r\le4$。
联 (5) 立刻得到
$$
\boxed{r\in\{2,3,4\},\qquad k_{\rm carry}=0.}
\tag{8}
$$

若 F0 在 d 以外有任何零，则 (7) 除 $t^r$ 外另含其三重零。
若该零是 t=0，总零阶至少 $r+3$；否则总次数同样至少 $r+3$。
因 $r\ge2$，二者都超过四，且没有 d 以外的极可抵消。
故准确有
$$
\boxed{F_0=\lambda d^c,\qquad
\lambda\in\mathbf F_p^\times,\quad c\ge0.}
\tag{9}
$$
该结论没有使用 $m_q=0$，也没有先假设 $q_0(0)\ne0$。

置
$$
G=\frac{F}{\lambda d^c},\qquad G(t,0)=1,\qquad
A=q_0F_0^3.
$$
由 (7)，
$$
\boxed{A\in\mathbf F_p[t],\qquad \deg A\le4-r.}
\tag{10}
$$
A 可能在零点消失。取 q 的常数 charge 只能提高 (4) 每个赋值，
所以有真实来源返回
$$
\boxed{t^rAG^3=t^rq_0F^3\in\overline{\mathcal W}_{3b}.}
\tag{11}
$$
这使用全部原系数列的双向 Gauss 识别，不是仅在一个较大多项式空间中成立。

可以从 A 删除它在 t=0 的全部因子：
删除后零角仍由
$$
4r+3v_0(G)=4r-3m\ge-2
$$
支付，其他有限角不受影响，无穷远预算只改善。
还可删去所有不在 $(t-1)h_7d$ 上的因子；
若 G 没有 d 亏损，d 因子也可删去。
因此存在一个 $A_*(0)\ne0$ 的固定角 mask，使
$$
\boxed{t^rA_*G^3\in\overline{\mathcal W}_{3b},
\qquad \deg A_*\le4-r.}
\tag{12}
$$
(12) 保同一 F 的曲线和接触，但通常是一个新的 cube 来源。

## 3. 全部角亏损与十三个原系数格

因 G 的常数 charge 为1，定义非负整数
$$
m_\alpha=-v_\alpha(G),\qquad m_1=-v_1(G),\qquad
\delta_d=-v_d(G),\qquad\delta_\infty=-v_\infty(G).
$$
(12) 的准确预算是
$$
\boxed{
\begin{aligned}
3m_\alpha&\le4\operatorname{ord}_\alpha A_*+2,\\
m_1&\le\operatorname{ord}_1A_*,\\
3\delta_d&\le2\operatorname{ord}_dA_*,\\
3\delta_\infty+2\deg A_*&\le8-2r .
\end{aligned}}
\tag{13}
$$
零角另保 (5)，不能由表中其他角代替。

在原 $\mathbf F_p$ 上，$p\equiv5\bmod6$ 使 h7 不可约，
两个几何 h7 角有同一个亏损 $m_h$。
所有可能由下表覆盖；亏损列均为上界，允许格彼此重叠。

| r | 零角指标 m | mask $A_*$ | $m_h$ | $m_1$ | $\delta_d$ | $\delta_\infty$ |
|---|---|---|---:|---:|---:|---:|
| 2 | 3 | 1 | 0 | 0 | 0 | 1 |
| 2 | 3 | $t-1$ | 0 | 1 | 0 | 0 |
| 2 | 3 | $(t-1)^2$ | 0 | 2 | 0 | 0 |
| 2 | 3 | $h_7$ | 2 | 0 | 0 | 0 |
| 2 | 3 | $d^2$ | 0 | 0 | 1 | 0 |
| 3 | 3 或 4 | 1 | 0 | 0 | 0 | 0 |
| 3 | 3 或 4 | $t-1$ | 0 | 1 | 0 | 0 |
| 4 | 3、4、5 或 6 | 1 | 0 | 0 | 0 | 0 |

这给五加四加四个带零角指标的系数格。
证明只需 (10)、(13)：r=3 时 mask 次数至多一，
一个 d 因子不足以支付任何正整数 $\delta_d$，故可删除；
不可约 h7 需要次数二，不能出现。
r=4 时次数帽为零，所有其他亏损均为零。
r=2 则正是 R782 的原五型。
由 (5)，相应 $m_q$ 仍须满足 $0\le m_q\le4r+2-3m$；
特别 r=2 必有 $b_0=m=3$、$m_q\in\{0,1\}$。

每个表格的完整系数如下：
$$
a_n=\max\left(0,\left\lceil\frac{n-m}{4}\right\rceil\right),\quad
b_n=\max\left(0,\left\lceil\frac{n-m_h}{4}\right\rceil\right),\quad
c_n=\max\left(0,\left\lceil\frac{n-m_1}{3}\right\rceil\right),
$$
$$
z_n=\left\lfloor\frac{n+\delta_d}{2}\right\rfloor,\qquad
K_n=\left\lfloor\frac{9n+\delta_\infty}{2}\right\rfloor,\qquad
r_n=t^{a_n}h_7^{b_n}(t-1)^{c_n}d^{-z_n},
$$
$$
\boxed{
G=1+\sum_{n=1}^bY^nr_n p_n,\qquad
\deg p_n\le K_n-\deg_t r_n.}
\tag{14}
$$
负次数帽的组为空；有理函数的次数保分母成本。
(14) 由每个固定角的整除条件和无穷远次数帽双向推出，
含全部允许乘子，不只一组试验列。

F primitive 又给
$$
\boxed{c\le\left\lfloor\frac{b+\delta_d}{2}\right\rfloor,}
\tag{15}
$$
因为某个 Fn 在 d 处为单位，故 $2c-\delta_d=v_d(F)\le b$。
不可约、$F_Y(0,1)\ne0$、准确 b0 及真实接触仍须另行满足。
表格没有自动赋这些性质。

在扩大的剩余域上，(8)–(13) 同样成立；
但 h7 分裂时必须按其各不可约因子分别记录角亏损，
不能把本表的十三格称为该域的完整列表。

## 4. 原因子的小成本返回和实际接触矩阵

r=2 的五型分别使用 R787 的
$$
L_*=t,\ t,\ t(t-1),\ t,\ td.
$$
r=3 或4 的每格均可取
$$
\boxed{L_*=t,\qquad L_*G\in\overline{\mathcal W}_b.}
\tag{16}
$$
确实零角为 $4-m\ge-2$，h7 角至少0，t=1 角至少−1，
d 角至少0，无穷远至少−2；且只允许 d 极。
这逐项支付原 (4)，不增加 Y 次数，也不增加原接触的精确 h。
乘 L 后在原点的接触才是 h+1。

对任一格，使用同一低轴
$$
\rho=d\Theta^{17},\qquad g\equiv\rho\bmod t^s,\qquad h<s.
$$
其原因子接触恰为完整非齐次系统
$$
\boxed{
\sum_{n=1}^b\sum_{j=0}^{K_n-\deg r_n}
x_{n,j}[t^{\,i-j}](r_n\rho^n)
=-\mathbf1_{i=0},\qquad 0\le i<h.}
\tag{17}
$$
这里没有独立化各幂的高尾。
在 R795 的交数门适用时，(16) 可用于其同一个来源限制论证；
未达到门时，不能凭十三格或参数数目假设接触核一维。

## 5. R788 的原 b=3 全素数排除扩展

再加回 R788 的准确窗口
$$
r=2,\quad\ell=1,\quad k_{\rm carry}=0,\quad
s=2h+2,\quad p=12h+11,\quad
b=b_0=3,\quad h\ge C^2+14.
\tag{18}
$$

**推论。** 在 (1)–(3)、(6)、(18) 下，不存在原强接触因子 F。
所以 R788 的排除不只适用于 $m_q=0$，
还适用于 $m_q=1$ 中 $q(t,0)\ne0$ 的全部候选。

**证明。** (9)、(12) 和表格说明同一个 G 仍处于
R782 的原五个完整格，几何曲线 C、准确自交数和接触均未改变。
可直接沿用 R788 的两个最大有理子式、准确十九角和剩余 p=311 判定。

也可将 (12) 写成 $t^2q_*F^3$，
其中 $q_*=A_*/(\lambda^3d^{3c})$ 在零点为单位，
故 $m_{q_*}=0$。
由 (15) 及 d² mask 的实际补偿，
$q_*$ 的 d 分母可装进原 $C_{3b}$ 帽；
其余 Gauss 条件已由 (12) 支付，且 $f_{3b}\le f_D<p$。
于是同一个 F 满足 R788 的全部因子存在性假设，矛盾。$\square$

R788 的公开执行无需重新运行：所用的五格、同一 $\rho$、
完整几何类和有限非齐次右端都没有改变。
其 producer、run43735456684、job132876943772 及全部 hash
仍由该篇完整记录。本篇没有新的数值结论或未执行的检查。

这个推论只排除 (18) 的 b=3。
它不排除 b≥4，也不把 r=3、4 的表格自动认作无解。

## 6. q(t,0)=0 时的原最低非零 charge 与移动因子界

现在去掉 (6)，改令
$$
j=\operatorname{ord}_Yq\ge1,\qquad q=\sum_{n\ge j}q_n^{\,q}(t)Y^n.
$$
因 $q(0,1)\ne0$，某个 $n\ge j$ 的系数在 t=0 非零，
所以 $m_q\ge j$。
联 (3)、(5)，得到真实有限界
$$
\boxed{
1\le j\le4r+2-3m\le4r-12k_{\rm carry}-7\le45.}
\tag{19}
$$
原最低 charge 恰为
$$
P_j=t^r q_j^{\,q}(t)F_0(t)^3.
\tag{20}
$$
仍写
$$
F_0=\lambda d^cH,\qquad d\nmid H,
$$
并把 H 规范成 monic；允许 H 在 t=0 有零。
因为 (20) 是原第 j 条系数，
$d^{C_j}P_j$ 为次数至多 $f_j+C_j$ 的多项式。
又 $t^rH^3$ 与 d 互素，而 $q_j^{\,q}$ 的极只可能在 d，
所以 $t^rH^3$ 实际整除这个多项式。
因此
$$
\boxed{
\deg H\le
\left\lfloor\frac{f_j+C_j-r}{3}\right\rfloor.}
\tag{21}
$$
这是一条保原最低 charge 的因子界；
不能从 (20) 免费除 $Y^j$ 后套用常数 charge 的四次帽。

特别在 r=2 中，(5) 给 $m=3,m_q\le1$，
而 (19) 迫 $j=m_q=1$。
每个正 t=0 系数的 Y 次数均不超过1，且常数 charge 已为零，
所以
$$
\boxed{
q=Y\widetilde q,\qquad
\widetilde q(0,Y)=c_q\in\mathbf F_p^\times,\qquad
-v_0(\widetilde q)=0,\qquad \deg H\le2.}
\tag{22}
$$
令
$$
\widehat G=\frac{F}{\lambda d^c},\qquad
\widehat G(t,0)=H,\qquad
A_1=\lambda^3d^{3c}\widetilde q(t,0).
$$
原 j=1 条没有 d 分母，次数帽为8，
故 (20) 及互素性精确给
$$
\boxed{
A_1\in\mathbf F_p[t],\quad A_1(0)\ne0,\quad
\deg A_1\le6-3\deg H,\quad
t^2YA_1\widehat G^3\in\overline{\mathcal W}_{3b+1}.}
\tag{23}
$$
最后一个来源结论仍由最低非零 charge 的投影提高全部 Gauss 值证明。
H 的移动根、可能的零点根及所有原角成本都保留。
(23) 不能换成原五格，R788 也未覆盖它。

## 7. 同一首次修正与当前准确边界

上述 scalar 投影、删 t 因子和删冗余 mask 是因子存在性的操作。
对已经固定的原 $P_2=P^{\rm fact}+pR$，
它们一般改变指定 forcing，不能重选 R 或高轴消去差异。

尤其 r=2、$m_q=1$ 时，
$q-q(t,0)$ 在 t=0 可以有非零 Y 项；
R782§8 用于第三块不变的“每个系数被 t 整除”已经不成立。
故该篇 (35)、(36) 的特定运输不在这里扩展。
原第三 $w^{13}$ 单位行、完整 first-normal、两条十三行 carry
以及 p³ 的同一个 R 都必须按原输入重新读取。

本篇完成的是：
常数 charge 非零窗口的全部 r/k 限制、十三格的完整原系数来源、
原 b=3 全素数排除的有效扩展，以及零常数余支的真实有限最低 charge 界。
尚未解决的是这些剩余格的强接触、(23) 的移动常数因子范围、
以及原同一个 R 的指定完整配对；主目标仍未完成。

依赖：
[R491](R491-valuated-source-factor-lifts-and-homogeneous-joint-obstruction.md)；
[R768](R768-finite-fiber-normal-residue-and-original-global-pole-divisor.md)；
[R782](R782-original-r2-five-profile-factor-and-inhomogeneous-contact-gate.md)；
[R787](R787-original-factor-return-and-whole-square-source-normal-kernels.md)；
[R788](R788-original-cubic-factor-all-prime-exclusion.md)；
[R790](R790-original-cube-full-forcing-and-factor-contact-bockstein-pairing.md)；
[R795](R795-original-factor-contact-one-dimensional-kernel-and-unit-next-row.md)。
