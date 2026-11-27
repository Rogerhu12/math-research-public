# 实际最大图输入的小指数物理孔矩与临界平方来源核心

日期：2026-11-27（Asia/Taipei）。

作者：Astra-ISP-8542378f-20261127 / stable_kernel_return；AI-assisted GPT-6 Astra Pro。

**状态：以下是实际最大图来源的已证明充分正则性；不声称未知 Green 缺陷或 $W$ 来源自动具有这个物理孔矩。临界等号在本估计中成立，不声称它是所有可能方法的最优阈值。**

记
$$
\kappa_0=2+2\log(3/2),\qquad s_0=\frac{\kappa_0}{14}.
$$
固定原 N 或 Y 模型，$G=G_0^*$、$S=B^*$。取
$$
y\in\mathcal D(G),\quad f=Gy,\quad
T^*y=Sf,\qquad \|e^{s_0\mathcal N}y\|<\infty,             \tag{0.1}
$$
其中 $\mathcal N$ 数全部物理孔，不是首缺位。
令 $h$ 为同一实际对的唯一规范形式来源：
$$
Sh=y,\qquad T^*h=f.                                     \tag{0.2}
$$
本文证明
$$
\boxed{h\in C_2,\qquad
(y,f)\in\mathcal C
=\overline{\{(Sg,T^*g):g\in\mathcal H\}}.}                \tag{0.3}
$$
没有先假设 $h\in\mathcal H$，也没有对物理截断后的 $y$ 假设最大图域。

复用的已付输入是 [R239 A.11 的有限压平机制](R239-appendix-exponential-hole-right-inverses-and-true-tail-regularization.md)、
[原最大图域的准确边界行](R271-appendix-maximal-division-graph-opposite-prefix-regularity.md)，以及
[N/Y 共同平方来源核心](R271-appendix-y-carry-first-gap-row-domain-and-common-square-source-core.md)和
[低余孔稿的同来源换算](R271-appendix-maximal-graph-low-excess-hole-square-cost.md)。
新增的是将这些真实输入合成 (0.1)--(0.3)，并支付 $s=s_0$ 的等号。

## 1. 纯尾创建在每个物理层上的指数逆界

固定 $r\ge1,p\ge0$，令
$$
D_r=\sum_{j\ge r}(j+1)^{-2}E_j,\qquad
L_p=\left\lceil\frac32(p+2)\right\rceil,\qquad
t=(r+L_p)^{-2}.
$$
只在有限位集 $F=\{r,\ldots,r+L_p-1\}$ 上定义
$$
\Delta e_A
=\prod_{j\in A\cap F}\frac{a_j}{t}\ e_A,\qquad a_j=(j+1)^{-2}.
$$
这是实际有界正可逆算子，$\Delta\ge I$；不使用无限张量相似。
置
$$
C'=\Delta^{-1}D_r^*\Delta=\sum_{j\ge r}b_jE_j^*,
\quad b_j=t\ (j\in F),\quad b_j=a_j\ (j\notin F).
$$
全部 $b_j\le t$。保留压平块之后的正方差，若 $x=r+L_p$，则
$$
t^{-2}\sum_{j\ge r+L_p}a_j^2
\ge\frac{x^4}{3(x+1)^3}\ge\frac{x-3}{3}.
$$
在物理孔数 $p$ 层，原精确交换子因而给
$$
(C')^*C'
\ge\left[L_p-2p+\frac{r+L_p-3}{3}\right]t^2 I
\ge t^2I.                                               \tag{1.1}
$$
最后一步直接由 $L_p\ge3(p+2)/2$ 得出。

在该层上，$\Delta$ 的最大特征值不超过前 $p$ 个最大因子的乘积：
$$
\|\Delta|_{\mathcal H_p}\|
\le\left[\frac{(r+L_p)^p r!}{(r+p)!}\right]^2
\le e^{\kappa_0p+16/3}.                                 \tag{1.2}
$$
为核最后一步，$p\ge1$ 时用
$\sum_{i=1}^p\log(r+i)\ge p\log(r+p)-p$，以及
$r+L_p\le\frac32(r+p)+4$；
再用 $\log(1+u)\le u$ 即得。$p=0$ 直接成立。

由 $\Delta\ge I$，方向准确为
$$
\|D_r^*u\|=\|\Delta C'\Delta^{-1}u\|
\ge t\|\Delta^{-1}u\|
\ge t e^{-\kappa_0p-16/3}\|u\|.
$$
所以
$$
\boxed{
\|u\|
\le e^{16/3}(r+L_p)^2e^{\kappa_0p}\|D_r^*u\|
\quad(u\in\mathcal H_p\text{ of the high tail}).}          \tag{1.3}
$$
这一步使用创建的下界，不是把删除的任意右逆费用误当成创建范数。

## 2. 对原实际图对作低孔/高孔分割

令 $V_r$ 为低 $r$ 位全零的投影。原边界行保全部 carry 给
$$
\|D_r^*V_ry\|
\le8\eta_{r-1}\|y\|+\alpha_r\|f\|,
\qquad \eta_j=\alpha_{j+1}/\alpha_j.                     \tag{2.1}
$$
不同物理输入层经 $D_r^*$ 后仍正交。因而对每个整数 $P\ge0$，
$$
\|V_r\mathsf P_{\le P}y\|
\le e^{16/3}(r+L_P)^2e^{\kappa_0P}
       \left(8\eta_{r-1}\|y\|+\alpha_r\|f\|\right).        \tag{2.2}
$$
这没有把 $V_r\mathsf P_{\le P}y$ 另行放入 $\mathcal D(G)$。

另一方面，设 $Y_s=\|e^{s_0\mathcal N}y\|$，则
$$
\|V_r\mathsf P_{>P}y\|\le e^{-s_0(P+1)}Y_s.              \tag{2.3}
$$
记
$$
\ell_j=-\log\eta_j,\qquad
P_r=\left\lfloor\frac{\ell_{r-1}}{\kappa_0+s_0}\right\rfloor.
$$
因为 $s_0/(\kappa_0+s_0)=1/15$，(2.2)--(2.3) 及
$\alpha_r\le\eta_{r-1}$ 给
$$
\boxed{
\|V_ry\|\le
\eta_{r-1}^{1/15}
 \left[8e^{16/3}(r+L_{P_r})^2(\|y\|+\|f\|)+Y_s\right].} \tag{2.4}
$$
取整误差在 (2.3) 中由 $P_r+1>\ell_{r-1}/(\kappa_0+s_0)$ 直接支付，没有额外未定常数。

给出一个粗但明确的统一多项式预算。原归一化有
$$
\ell_j=1400\,16^j-630\,8^j+300\,2^j\le1700\,16^j.
$$
又 $\kappa_0>2$，故 $P_r<850\,16^{r-1}$，以及
$$
r+L_{P_r}\le1280\,16^{r-1}.
$$
定义
$$
A_y=\|y\|+\|f\|+Y_s,\qquad
C_0=8e^{16/3}1280^2+1.
$$
于是
$$
\boxed{
\|V_ry\|\le C_0\,16^{2(r-1)}\eta_{r-1}^{1/15}A_y
\qquad(r\ge1).}                                         \tag{2.5}
$$

## 3. 临界等号的原 $\alpha$ 归一化

沿用
$$
b_0=\eta_0,\quad b_q=q^{-2}\eta_{q-1}\ (q\ge1),\qquad
\|h\|_{C_2}^2=\sum_{q\ge0}b_q^2\|P_qh\|^2.
$$
$P_q$ 是来源 $h$ 的首缺位 $q$ 块，
$P_q^+=V_q-V_{q+1}$ 是输出 $y$ 的正整数赋值 $q$ 块。
从同一 $Sh=y$ 准确有
$$
b_q\|P_qh\|
=\frac{b_q}{\alpha_q}\|P_q^+y\|
=\frac1{q^2\alpha_{q-1}}\|P_q^+y\|\quad(q\ge1).          \tag{3.1}
$$
真空已由最大图域排除，而 $q=0$ 项单独为
$(b_0/\alpha_0)^2\|P_0^+y\|^2$，不能漏掉。

置 $A_j=-\log\alpha_j$。原准确权式给
$$
A_j=\frac{280}{3}16^j-90\,8^j+300\,2^j-\frac{850}{3}.
$$
关键是保留次主项：
$$
\boxed{
\frac{\ell_j}{15}-A_j
=48\,8^j-280\,2^j+\frac{850}{3}
=:d_j.}                                                \tag{3.2}
$$
特别地
$$
d_0=\frac{154}{3},\qquad d_1=\frac{322}{3},\qquad
d_j\ge30\,8^j\quad(j\ge2).                               \tag{3.3}
$$
因此恰在 $1/15$ 次幂时，主 $16^j$ 指数虽抵消，真实次主 $8^j$ 仍给严格且可和的衰减。

由 (2.5)、(3.1)--(3.3)，
$$
\boxed{
\|h\|_{C_2}^2
\le K A_y^2<\infty,}                                    \tag{3.4}
$$
其中可取
$$
K=\left(\frac{b_0}{\alpha_0}\right)^2+
C_0^2\sum_{j\ge0}\frac{16^{4j}}{(j+1)^4}e^{-2d_j}.
$$
这是明确的有限常数；例如 $j\ge2$ 的和可由
$\sum 16^{4j}e^{-60\,8^j}$ 控制，逐项比值最终且事实上从 $j=2$ 起小于 $1/2$。
不需要把临界条件加强成 $s>s_0$。

## 4. 回到原图核心及真正缺陷

两模型已付的共同 $C_2$ 来源核心将 (0.2)、(3.4) 直接送回
$(y,f)\in\mathcal C$：
N 型使用 $K_N:C_2\to\mathcal H$ 与严格升孔 $D^*$；
Y 型使用完整的 $D^*-V_b$ 加余 carry 证明。
所有物理层之所以是 Hilbert 向量，仍由每层只含 $q\le p$ 的有限首缺位块保证；没有省去 Y 的 Cayley 逆或 primitive。

所以若
$$
(y,f)\in\mathcal E=\operatorname{Graph}G\ominus\mathcal C
\quad\text{且}\quad \|e^{s_0\mathcal N}y\|<\infty,
$$
则 $(y,f)=0$。

在已付闭坐标表示 $R:F\to Y$、
$T^*R=S(I+Z),\ T|_F=-BR$ 中，这给出一个同源的可检验充分输入：
$$
\|e^{s_0\mathcal N}Rv\|<\infty\quad\Longrightarrow\quad v=0.
$$
它不说明任意 $Rv$ 具有该矩，也不说明物理孔平滑保留 $Y$。
实际 $Z=0$、同 $W$ 的 $\Gamma$ 和最终 $N=M$ 仍须另行支付。
