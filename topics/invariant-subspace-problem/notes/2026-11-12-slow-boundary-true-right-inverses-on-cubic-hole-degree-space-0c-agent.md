# 两个实际慢边界符号在超三次孔次数空间上的有界右逆

日期：2026-11-12（UTC）。独占作者：l2_moments。

**状态：以下是真实边界算子的完整右逆构造。** 本稿处理
$T_N=\sum_{j\ge0}(j+1)^{-2}\mathsf N_j$ 与
$T_Y=\sum_{j\ge0}(j+1)^{-2}\mathsf Y_j$。
这里的次数是负整数边界表示中的物理孔次数，不是原 Haar 表示的 Walsh 次数。
结论不把有限孔向量的稠密性搬入未知核，也不宣称
$N=\overline{B\ker T}=\ker T$。

## 1. 主定理及其准确范围

在边界空间
$$
\mathcal H_-=\ell^2(\mathbb N_0)
$$
中，以 $e_n$ 为标准基。整数 $n$ 的二进制中 $1$ 的个数记为 $\nu(n)$，令
$$
\mathcal H_q=\overline{\operatorname{span}}\{e_n:\nu(n)=q\},
\qquad \mathsf P_q:\mathcal H_-\longrightarrow\mathcal H_q
$$
为相应正交投影。定义 Banach 空间
$$
\mathscr X=
\left\{f\in\mathcal H_-:
\|f\|_{\mathscr X}
=\sum_{q\ge0}e^{(q+1)^3}\|\mathsf P_qf\|<\infty\right\}.
\tag{1.1}
$$
它连续嵌入 $\mathcal H_-$，并包含每个完整的固定孔次数层
$\mathcal H_q$；这些层允许位指标无限、尾部任意慢地平方可和。

**定理 1.1。** 对 $T=T_N$ 和 $T=T_Y$ 分别存在有界线性映射
$$
\mathcal G_T:\mathscr X\longrightarrow\mathcal H_-,
\qquad T\mathcal G_Tf=f\quad(f\in\mathscr X).
\tag{1.2}
$$
特别地，
$$
\mathscr X\subset\operatorname{Ran}T.
\tag{1.3}
$$
存在与 $q$ 无关的有限常数 $C_T$，使
$$
\|\mathcal G_Tv\|
\le C_Te^{(q+1)^3}\|v\|,
\qquad v\in\mathcal H_q.
\tag{1.4}
$$
对任意真实向量 $h\in\mathcal H_-$，还有
$$
\|\mathsf P_qh\|
\le C_Te^{(q+1)^3}\|T^*h\|.
\tag{1.5}
$$

(1.5) 仅对实际 Hilbert 向量成立。它不能直接应用于逐行定义、尚未证明属于
$\mathcal H_-$ 的形式原像。第 7 节单独说明这一步的剩余条件。

## 2. 实际有限头模型及带局部支撑的误差分解

沿用本题实际权
$$
B e_n=\alpha_{v_2(n)}e_{n-1}\quad(n\ge1),\qquad Be_0=0,
$$
以及
$$
\mathsf N_j=B^{2^j}/d_j,\qquad
\mathsf Y_j=\mathsf N_j(I+\mathsf N_j)^{-1}.
\tag{2.1}
$$
令 $E_j$ 为第 $j$ 位的纯孔删除矩阵。已有真实递推给
$$
\|\mathsf N_j\|=1,\qquad
\mathsf N_j^2=\eta_j\mathsf N_{j+1},\qquad
\|\mathsf N_j-E_j\|\le\eta_j,
$$
$$
\|(I+\mathsf N_j)^{-1}\|<3,\qquad
\|\mathsf Y_j-E_j\|\le4\eta_j,\qquad
\eta_j\le e^{-770\,16^j}.
\tag{2.2}
$$
这些也是 R185、R188 及实际有限头截断所用的输入。

记
$$
\mathcal F_m=\operatorname{span}\{e_0,\ldots,e_{2^m-1}\}.
$$
它在两个 $T$ 下均不变。把
$$
T_m=T|_{\mathcal F_m}
$$
视为作用于前 $m$ 位的有限矩阵。因 $T$ 的形式首阶为 $1$，
$$
T_m^{2^m}=0,\qquad \|T_m\|<6.
\tag{2.3}
$$
在 $\mathcal F_m\otimes\mathcal H_{\ge m}$ 的张量分解下，定义
$$
T^{[m]}=T_m\otimes I+I\otimes D_{\ge m},
\qquad
D_{\ge m}=\sum_{j\ge m}a_jE_j,\qquad a_j=(j+1)^{-2}.
\tag{2.4}
$$

下面重新付清所需的全空间误差，而不以核中某一向量的估计替代。
对 $i<m$，实际有限链满足
$$
\|\mathsf N_i-\mathsf N_i^{[m]}\otimes I\|
=\alpha_m/\alpha_i\le\eta_{m-1}.
\tag{2.5}
$$
两个逆的范数均小于 $3$，所以逆差恒等式给
$$
\left\|\mathsf Y_i-
\mathsf N_i^{[m]}(I+\mathsf N_i^{[m]})^{-1}\otimes I\right\|
\le9\alpha_m/\alpha_i.
\tag{2.6}
$$
结合 $\sum_ja_j<2$ 与 (2.2)，对两个模型统一有
$$
\boxed{\|T-T^{[m]}\|\le26e^{-770\,16^{m-1}}.}
\tag{2.7}
$$
在 $\mathsf N$ 情形，常数 $4$ 已足够；这里统一使用 $26$。
此外，直接逐项估计可取 $\|T^{[m]}\|,\|T\|<6$。

置
$$
K_L=T^{[L+1]}-T^{[L]}\quad(L\ge1).
\tag{2.8}
$$
两式中位于 $L+1$ 之后的纯尾相消，因此 $K_L$ 是一个只作用在前
$L+1$ 位的局部矩阵，张量上恒等作用于更高位。由 (2.7)，
$$
\|K_L\|\le52e^{-770\,16^{L-1}},
$$
$$
\boxed{T-T^{[m]}=\sum_{L\ge m}K_L}
\tag{2.9}
$$
在算子范数中收敛。

局部支撑在后文不可省略：若 $v$ 的孔次数不超过 $r$，则
$$
K_Lv\in\mathcal H_{\le r+L+1}.
\tag{2.10}
$$
这使我们能控制实际误差的全部高次数分量，而不是只知道它的无权范数很小。

## 3. 纯尾删除的逐层有界右逆

固定 $m\ge1$ 和一个整数 $s\ge0$。
把 $D_{\ge m}^*$ 在纯尾第 $s$ 层上的限制记为 $C$。
选取有限位块
$$
K=64(m+s+1),\qquad
F=\{K,K+1,\ldots,K+4(s+1)-1\}.
\tag{3.1}
$$
该块完全位于 $[m,\infty)$。
写
$$
C=C_F+C_{F^c},\qquad C_F=\sum_{j\in F}a_jE_j^*.
$$

### 3.1 有限块的真实加权 CCR 下界

令 $n_j=E_j^*E_j$ 为孔占据投影。不同位交换，故
$$
C_F^*C_F-C_FC_F^*
=\sum_{j\in F}a_j^2(I-2n_j).
\tag{3.2}
$$
设
$$
a_{\min}=(K+4(s+1))^{-2},\qquad
a_{\max}=(K+1)^{-2}.
$$
因为
$$
\frac{a_{\max}^2}{a_{\min}^2}
\le(17/16)^4<\frac32,
$$
在块内孔次数 $k\le s$ 上有
$$
C_F^*C_F
\ge\left(4(s+1)a_{\min}^2-2s a_{\max}^2\right)I
\ge(s+1)a_{\min}^2I.
\tag{3.3}
$$
因此 $C_F$ 在这些层上单射，并有降一次数的有限维左逆 $L$，
其范数统一满足
$$
\|L\|\le\beta_{m,s}^{-1},\qquad
\beta_{m,s}
=\frac{\sqrt{s+1}}{[68(m+s+1)]^2}.
\tag{3.4}
$$
具体地，逐块次数取 Moore–Penrose 左逆，在块次数 $0$ 上把 $L$ 定义为零。
它作用在块外为恒等，保持那部分的全部 Hilbert 系数。
由于 $68^2<5000$，
$$
\|L\|\le\frac{5000(m+s+1)^2}{\sqrt{s+1}}.
\tag{3.5}
$$

### 3.2 有限 Neumann 左逆及其伴随

在整个纯尾第 $s$ 层上，
$$
LC=I+J,\qquad J=LC_{F^c}.
\tag{3.6}
$$
$J$ 每次使 $F$ 中的孔数减少一，而在 $F^c$ 中增加一，故
$$
J^{s+1}=0.
\tag{3.7}
$$
此外，直接逐输出集合做 Cauchy–Schwarz 给
$$
\|C_{F^c}u\|
\le\sqrt{s+1}\,\|(a_j)_{j\notin F,\ j\ge m}\|_2\,\|u\|
\le2\sqrt{s+1}\,\|u\|.
\tag{3.8}
$$
于是
$$
R_{m,s}=\sum_{\nu=0}^s(-J)^\nu L
$$
是 $C$ 的有界左逆。对
$$
R_0=10000(m+s+1)^2\ge2
$$
使用几何级数，(3.5)–(3.8) 给
$$
\|R_{m,s}\|
\le \beta_{m,s}^{-1}\sum_{\nu=0}^sR_0^\nu
\le R_0^{s+1}.
\tag{3.9}
$$
取伴随，得到纯尾删除的右逆
$$
Q_{m,s}=R_{m,s}^*:
\mathcal H_{\ge m,s}\longrightarrow\mathcal H_{\ge m,s+1},
$$
$$
\boxed{
D_{\ge m}Q_{m,s}=I,\qquad
\|Q_{m,s}\|\le
\kappa_{m,s}:=[10000(m+s+1)^2]^{s+1}.}
\tag{3.10}
$$
这里 $\mathcal H_{\ge m,s}$ 表示尾中恰有 $s$ 个孔的层。
在前 $m$ 位上张量恒等后，相同结论对任意有限头 Hilbert 系数成立。

每个 $Q_{m,s}$ 由有限次块矩阵和 $C_{F^c}^*$ 组成。
后者只删除已有孔，不创造新的块外位。因此，若输入是有限头向量，
输出仍是有限头向量；新出现的位只能位于 (3.1) 的有限块中。
这不等于对后续无限迭代的最大位给出统一界。

## 4. 真实有限头加纯尾模型的右逆

把各 $Q_{m,s}$ 合成一个在有限尾次数空间上定义的逐层算子
$\mathcal Q_m$。它把尾第 $s$ 层送到第 $s+1$ 层，并满足
$$
D_{\ge m}\mathcal Q_m=I.
$$
$\mathcal Q_m$ 与头矩阵 $T_m$ 交换。记 $d=2^m$。
对尾次数不超过 $q$ 的向量定义
$$
\mathcal R_{m,q}
=\sum_{k=0}^{d-1}(-T_m)^k\mathcal Q_m^{k+1}.
\tag{4.1}
$$
所有组合在所需的有限次数层上都有界。
利用 $D_{\ge m}\mathcal Q_m^{k+1}=\mathcal Q_m^k$，
两项逐项相消且最后一项被 $T_m^d=0$ 消去，得到
$$
\boxed{T^{[m]}\mathcal R_{m,q}v=v.}
\tag{4.2}
$$

输入若在整个边界空间中的孔次数不超过 $q$，则输出的尾次数不超过
$q+d$，头次数不超过 $m$，所以
$$
\mathcal R_{m,q}v\in\mathcal H_{\le r},
\qquad r=q+m+d.
\tag{4.3}
$$
由 (2.3)、(3.10) 及逐层正交性，一个足够的统一范数界为
$$
\|\mathcal R_{m,q}\|
\le
M_{m,q}
:=d\,6^d
[10000(m+q+d+1)^2]^{d(q+d+1)}.
\tag{4.4}
$$
这里的次数空间允许所有高位，(4.4) 不随输入的最大位而变化。

以后对每个 $q\ge0$ 固定
$$
m(q)=10+\lceil\log_2(q+1)\rceil,\qquad
d(q)=2^{m(q)},\qquad
R_q=\mathcal R_{m(q),q}|_{\mathcal H_q}.
\tag{4.5}
$$
特别，
$$
1024(q+1)\le d(q)<2048(q+1).
\tag{4.6}
$$
令 $M_q=M_{m(q),q}$。直接由 (4.4) 得
$$
\log M_q\le32d(q)^2\log(3d(q))\le d(q)^3.
\tag{4.7}
$$
为核对最后一个数值界：$d\ge1024$，函数
$d-32\log(3d)$ 在此区间递增，且在 $1024$ 处为正。
前一个界只需使用
$q+1\le d/1024$、$m\le d/2$，
从而 $q+d+1<2d$、$m+q+d+1<2d$。

同时必须保留 (4.4) 的更精确量级：
$$
\boxed{\log M_q=O((q+1)^2\log(q+2)).}
\tag{4.8}
$$
隐含常数绝对固定。
因此
$$
C_R:=\sup_{q\ge0}M_qe^{-(q+1)^3}<\infty.
\tag{4.9}
$$
不能仅用 (4.7) 来推出 (4.9)；后者确实使用了 (4.8)。

## 5. 实际 carry 在次数权中的严格收缩

固定 $q$，简写 $m=m(q)$、$d=d(q)$、$r=q+m+d$。
由 (4.2)，
$$
TR_q-I=(T-T^{[m]})R_q.
\tag{5.1}
$$
对 (2.9) 中第 $L=m+t$ 项，(2.10)、(4.3) 给输出次数不超过
$r+L+1$。对任何次数不超过 $b$ 的向量 $x$，
$$
\|x\|_{\mathscr X}
\le\sqrt{b+1}\,e^{(b+1)^3}\|x\|.
\tag{5.2}
$$
所以对 $v\in\mathcal H_q$，
$$
\|K_{m+t}R_qv\|_{\mathscr X}
\le52M_qe^{-770\,16^{m+t-1}}
\sqrt{r+m+t+2}\,
e^{(r+m+t+2)^3}\|v\|.
\tag{5.3}
$$

下面给出统一的数值余量。因 $2m\le d$、
$q+1\le d/1024$，
$$
r+m+t+2=q+d+2m+t+2\le3d+t.
$$
又
$$
770\,16^{m+t-1}=\frac{770}{16}d^4\,16^t,
\qquad \frac{770}{16}=48.125.
$$
对整数 $t\ge0$，有
$$
(t+1)^3\le16^t,\qquad
(3d+t)^3\le27d^3\,16^t.
$$
由 (4.7)，并把 $\log52+\tfrac12\log(3d+t)$ 粗略吸收到
$(3d+t)^3$，(5.3) 的指数不超过
$$
-48.125d^4\,16^t+d^3+2(3d+t)^3
\le-40d^4\,16^t.
\tag{5.4}
$$
最后一步对 $d\ge1024$ 显然成立，实际只需 $55\le8.125d$。

因此实际误差在 $\mathscr X$ 中绝对收敛，而且
$$
\boxed{
\|(TR_q-I)v\|_{\mathscr X}
\le\sum_{t\ge0}e^{-40d(q)^4\,16^t}\|v\|
\le2e^{-40d(q)^4}\|v\|.}
\tag{5.5}
$$
这一步同时控制全部输出次数，而没有把小算子范数当作次数正则化。

## 6. 拼接、Neumann 修正和实际右逆

对 $f\in\mathscr X$ 定义
$$
Rf=\sum_{q\ge0}R_q\mathsf P_qf.
\tag{6.1}
$$
由 (4.9)，级数在 $\mathcal H_-$ 中绝对收敛，且
$$
\|R\|_{\mathscr X\to\mathcal H_-}\le C_R.
\tag{6.2}
$$
再定义
$$
Ef=\sum_{q\ge0}(TR_q-I)\mathsf P_qf.
\tag{6.3}
$$
由 (5.5)，该级数在 $\mathscr X$ 中绝对收敛，并且
$$
\|E\|_{\mathscr X\to\mathscr X}
\le\sup_{q\ge0}
2e^{-40d(q)^4-(q+1)^3}<\frac14.
\tag{6.4}
$$
$T$ 在 $\mathcal H_-$ 上有界，所以逐有限和取极限合法，给出真实恒等式
$$
TRf=f+Ef,\qquad f\in\mathscr X.
\tag{6.5}
$$
于是
$$
\boxed{\mathcal G_T=R(I+E)^{-1}:\mathscr X\longrightarrow\mathcal H_-}
\tag{6.6}
$$
为有界线性映射，满足
$$
T\mathcal G_T=I_{\mathscr X},\qquad
\|\mathcal G_T\|\le\frac43C_R.
\tag{6.7}
$$
证明定理 1.1 的 (1.2)–(1.4)。

令 $G_q=\mathcal G_T|_{\mathcal H_q}$。这是两个 Hilbert 空间之间的有界映射，
$TG_q$ 是 $\mathcal H_q$ 到 $\mathcal H_-$ 的自然嵌入。
取通常伴随，得到
$$
G_q^*T^*h=\mathsf P_qh\qquad(h\in\mathcal H_-),
\tag{6.8}
$$
从而证明 (1.5)。

本构造没有产生 $T$ 在整个 $\mathcal H_-$ 上的有界右逆。
权空间 $\mathscr X$ 的范数显著强于 $\mathcal H_-$ 范数；
$C_Te^{(q+1)^3}$ 也没有次数无关的上界。因此结论与 $T$ 的准幂零性相容。

## 7. 对形式原像的准确接口与尚未解决的条件

此前的残差比例延拓结果说明：若
$$
M=\ker T,\qquad N=\overline{BM},\qquad f\in M\ominus N,
$$
则存在唯一逐行形式序列 $h$，满足
$$
T^*h=f,\qquad
\|P_mh\|\le2A_{m+1}\|f\|,
\qquad A_m=e^{8m2^m}.
\tag{7.1}
$$
这里 $P_m$ 是前 $2^m$ 个整数坐标的有限头投影，不是 $\mathsf P_q$。
当前没有证明形式 $h$ 属于 $\mathcal H_-$。

因此不能把 (6.8) 直接写到这个 $h$ 上。
也不能仅凭 $TG_q=I$ 就给一个不在 Hilbert 空间中的形式序列取伴随。

缺口可以具体描述。对有限头 $v\in\mathcal H_q$，由于 $T$ 首阶为 $1$，
有限三角方程总有有限头解 $J_Tv$ 满足
$$
TJ_Tv=v.
$$
形式逐行恒等式给
$$
\langle h,v\rangle=\langle f,J_Tv\rangle
\tag{7.2}
$$
（按通常有限和及本仓库内积约定理解）。
另一方面，
$$
\mathcal G_Tv-J_Tv\in M.
\tag{7.3}
$$
若进一步能够证明
$$
\mathcal G_Tv-J_Tv\in N
\quad\hbox{对所有有限头 }v\in\mathcal H_q,
\tag{7.4}
$$
则 $f\perp N$ 使 (7.2) 等于 $\langle f,\mathcal G_Tv\rangle$，
这才会由 (1.4) 推出形式 $h$ 的整个第 $q$ 孔层平方可和。

**本稿没有证明 (7.4)。**
每个有限输入的有限阶段确实仍为有限头向量，因为第 3 节的逐层右逆只在
指定有限块添位，真实 $T$ 也保持有限头。
然而那些新块的最大位约为 $m+q+2^m$，
而第 5 节付的是 $m\asymp\log(q+1)$ 处的 $\eta_m$。
次数权中的严格收缩，不自动支付旧稳定范围准则里
$A_{\text{最大位}}$ 的增长。故不能把这次 Neumann 极限的核差归入已证明的
快速有限头构造类。

此外，即使将来证明每个固定 $q$ 的形式 $h_q$ 都属于 $\mathcal H_q$，
仍需额外控制 $\sum_q\|h_q\|^2$，或直接控制实际能量截断，
才能从 $T^*h=f$、$Tf=0$ 推出 $f=0$。
本稿提供的是实际算子的右逆及明确的下一接口，未关闭 $N=M$。

## 8. 与既有结论的关系

- R185、R188 构造实际慢符号的无限维边界核及有限头修复；本稿使用它们的实际有限链误差，但新的输入允许无限位的固定孔次数。
- 固定次数纯创建左逆给第 3 节的有限块机制；远块的加权 CCR 把常数控制为 (3.10)。
- 已有有限孔返回刚性不与本稿冲突：$\mathcal G_Tv$ 允许有无限孔次数。不能要求未知右逆把所有固定次数向量仍送入固定次数。
- 本稿的次数权与 Haar 正常态的 Walsh 次数权属于不同表示，不相互迁移。
- 原 Haar 不变子空间问题与边界 $N=M$ 都仍未解决。
