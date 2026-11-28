# 新输入：第二 NV 头与 ell=3/2 的完整四次常数代数、原 NV 二次及有限原值返回

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127 / literature_deddens。日期：2026-11-29（Asia/Taipei）。

**状态：未执行的新原目标。** 范围严格为正确 Phi、原 $D\ne0$ 图内
$$
B_2=\ell(3-2\lambda)+2T+2m\sigma=0,\qquad \ell=\frac32 .
\tag{1}
$$
本输入没有把一般第二头、第一头或整个 $\ell=3/2$ 图宣布排除。先用两个完整原矩准确构造四次常数代数；再用新的完整缩放 Gram 返回一个至多 $u^2$ 的必要式。只有它在相应整个常数域非零时，才进入保全部 $u,t$ 重数的有限环境，试事前固定的原正幂目标。

源码：2026-11-28-unit211-Phi-zero-corrected-second-NV-head-ell-three-halves-whole-quartic-original-values-8542.py。

源码 Git blob：c8e84e799c516e8d5fba5b88268440dcbd2b306d。

源码 SHA256：e9939ac41af3e0a5ef9080ef008519dc65cccb45fe1cd30f22a24d80767acfcb。

零依赖，固定 **120 秒 / 1 GiB**，外层 135 秒。无素数、数值根、选点或泛域 gcd；原几何 $D,t,f-u$ 均不倒置。不执行旧六列、二十列、八条奇部列或任何已冻目标。任一实际失败都保留最后完整返回，不续轮、换算法或扩预算。

## 1. 原单位和全部 rho 选择

正确 Phi 的定义
$$
L=Q-2(u-1)(u-2),\qquad \ell=L/Q
$$
使 (1) 上
$$
Q=-4(u-1)(u-2),\quad
\delta=1-Q=(2u-3)^2,\quad
m=\frac{2u-3}{2},\quad
M=2(2u-3)^2 .
\tag{2}
$$
原 $\rho^2=\delta$ 有两个分量。取 $\rho=2u-3$ 时
$$
b=1,\quad c=\frac12,\quad a_0=-\frac12,\quad
p=2u-2,\quad q=4-2u.
\tag{3}
$$
另一分量准确地交换两个 singleton 标签；全部原 $B,C$ 条件同时保留，故同一输入覆盖两个选择。没有挑选某个复数权根。

已付 $u,Q,\delta,K_w=Q+4(u-1)$ 给本次纯 $u$ 单位支持
$$
U(u)=u(u-1)(u-2)(u-3)(2u-3).
\tag{4}
$$
其中 $K_w=-4(u-1)(u-3)$。$P_{02}=3(u-1)Q$、$M=2\delta$ 的分母也由 (4) 支付。这里没有反演某个新 $u$ 多项式首项。

当前正确 Phi 中，$\lambda\ne0$ 是非零孤立 mean 图的既有单位，$D\ne0$ 是本物理图条件。[整个正确 $t=0$ 排除](../results/R150-appendix-unit211-Phi-zero-true-entire-tzero-original-exclusion.md)与[整个正确 $f=u$ 排除](../results/R150-appendix-unit211-Phi-zero-true-entire-fu-original-exclusion.md)给 $t(f-u)\ne0$。本次只在最后正目标使用这些原非零条件；不把它们作为几何逆输入。

旧 [rank-one 碰撞 c-half 排除](../results/R150-appendix-unit211-Phi-zero-rank-one-value-complete-c-half-exclusion.md)另要求 $TB_3-A_2^2=0$ 并取 $h=1$，不覆盖 (1)。本输入没有使用那条附加前提或重跑它的源。

## 2. 两个完整原矩的准确四次代数

第二头上 $h+k=2\lambda-1$。令
$$
y=h+1,\qquad v=k-1,\qquad \lambda=(y+v+1)/2,\qquad
N(y)=y^2-8y+7.
$$
两个原矩在 (3) 中是
$$
E_2=(h-1)^2+\frac12(k-1)^2-A_\lambda,\qquad
E_3=(h-1)^3+\frac12(k-1)^3-B_\lambda,
$$
其中 $A_\lambda=2\lambda^2-2\lambda+1$、
$B_\lambda=4\lambda^3-6\lambda^2+3\lambda-1$。直接普通多项式恒等式给
$$
2E_2=N-2yv,\qquad
7=2E_2+y(8+2v-y).
\tag{5}
$$
因此 $y$ 在原两矩商内真可逆，而不是新增一个需要保留的头开图。

令
$$
P_4(y)=5y^4-48y^3+180y^2-276y+147.
$$
第二条普通原身份为
$$
\boxed{P_4=6(N+2yv+2y^2)E_2-8yE_3.}
\tag{6}
$$
源码在任何商、因式选择之前，直接返回 (5)、(6) 的全部二元多项式系数。

反向在 $y$ 单位处，$v=N/(2y)$，而 (6) 给完整 $E_3$。由于 $P_4(0)=147\ne0$，$y$ 在 $\mathbb Q[y]/P_4$ 中也是真单位。因此准确有
$$
\boxed{
\mathbb Q[y,v]/(E_2,E_3)\simeq
K_4:=\mathbb Q[y]/P_4.}
\tag{7}
$$
$5$ 是有理单位，故 $K_4$ 自由秩四。此处没有假定 $P_4$ 不可约或平方自由，全部重数已经在 (7) 中保留。

在同一代数内，
$$
h=y-1,\qquad k=\frac{y^2-6y+7}{2y},
$$
$$
\lambda=\frac{3y^2-6y+7}{4y},\quad
T=\frac{5y^2-16y+7}{4y},\quad
w=\lambda-1-T=\frac{3-y}{2}.
\tag{8}
$$
源码对每个整个 QQ 不可约因子域重新核两个原矩及
$$
D=\frac32 A_\lambda-T^2=\frac12(h-k)^2.
\tag{9}
$$
若某完整常数因子上 $\lambda$ 或 $D$ 恒零，只有依据本图既有物理非零条件，才移除该整个因子；不计算或使用 $D^{-1}$。

## 3. 新完整 NV 的 u 二次原身份

本节是新的完整原值来源，不是旧小六列的再次消元。

记
$$
j=h+\frac k2=T+\frac32,\quad
r=h+k+hk,\quad R=(1-h)(1-k).
$$
原 $P_1,N_0$ 恢复在 (2)–(3) 化成
$$
E:=\frac{A_1}{2}
=-\frac{3(u-1)(u-2)}{u-3}\,j,
$$
$$
f=3(u-2)\lambda+\frac{3(u-2)^2}{u-3}\,j-(u-3),
\quad V=f+\frac t2-E,\quad
W_1=\frac{T_0}{2}+2uf,\quad T_0=4(u-1)(u-3).
\tag{10}
$$
全部分母只用 (4)。两线性均值给
$$
X=\frac{W_1-qV}{2\rho},\qquad
Y=\frac{pV-W_1}{\rho}.
\tag{11}
$$
以同一完整 Gram
$$
g_0=(0,0,p,q),\quad
g_1=(0,2E,X+p/2-t/2,Y+q/2-t),
$$
$$
g_B=(p,X+p/2-t/2,0,t),\quad
g_C=(q,Y+q/2-t,t,0)
\tag{12}
$$
及真正 dual germ 乘法
$(v_0w_0,v_0w_1+v_1w_0,v_Bw_B,v_Cw_C)$ 定义原 $N_4$。

物理向量为 $\mathbf V=(1,w,h,k)$。原矩给
$\tau(\mathbf V)=\lambda$、
$\tau(\mathbf V^2)=2\lambda^2+E_2$。逐项展开完整 $N_4$，得到
$$
\boxed{
N_4(\mathbf V)+2fE_2
=2\{-rf+RE+w[u(1+h-2k)+2(k-h)]\}.}
\tag{13}
$$
可直接核其来源：$d_1=f+E+u/2-t/2$，且
$$
\tau(\mathbf V D_K\mathbf V)
=2E+2hX+kY+2w(ph+qk/2)+(hk-h-k)t.
$$
完整 $N_4$ 中的 $X,Y$ 系数因 $h+k=2\lambda-1$ 合成 $-2hkV$。把 $d_1,V$ 代回后，所有 $t$ 项精确消掉。并且
$ph+qk/2=u(2h-k)+2(k-h)$，给出 (13)。
这里保留了 $-2fE_2$ 的完整原误差；没有先删掉它再称普通原身份。

定义
$$
F_u=3\lambda(u-2)(u-3)+3j(u-2)^2-(u-3)^2,\qquad
E_u=-3j(u-1)(u-2),
$$
$$
\boxed{
G(u)=-rF_u+RE_u+
w(u-3)\{u(1+h-2k)+2(k-h)\}\in K_4[u].}
\tag{14}
$$
于是 $\deg_uG\le2$。在原两矩商中，
$$
(u-3)N_4(\mathbf V)=2G(u).
\tag{15}
$$

源码没有只按 (14) 的纸式猜原来源。它在每个整个常数域的普通 $K[u,t]$ 中取
$$
H=(2u-3)(u-3)
$$
并构造 $H$ 倍的完整 (12)。在这个普通多项式环中，$X,Y$ 的尺度只作精确整除并乘回，禁止任何非常数 $u$ 逆。对固定 $\mathbf V$，$N_4$ 对 Gram 线性，所以程序完整核
$$
\boxed{N_{4,Hg}(\mathbf V)=2(2u-3)G(u).}
\tag{16}
$$
同时核 $F_{2,Hg}=2(2u-3)F_u$。这在普通 $K[u,t]$ 中保每一系数，且没有物理 $t=0$ 专门化。

## 4. 完整常数域、u 主分量和单首一 t²

首先对固定 $P_4$ 作一次完整 QQ 因式分解并把所有因子及重数乘回。每个不可约因子 $\varphi$ 的计算始终在
$$
K_\varphi=\mathbb Q[y]/\varphi
$$
中进行，保其全部复数嵌入，不选根。所有实际常数逆由整个域的 Bézout 及乘回支付。

对相应完整 $G_\varphi(u)$：

- 若恒为零，保留该整个常数因子，后续有限 $u$ 环境不成立，不另选目标。
- 若是非零常数，(15) 直接排该整个因子。
- 否则用其真实非零常数域首项首一化，保整个 $u$ 多项式。

仅对 (4) 的旧纯 $u$ 单位作重复 gcd 主分量删除，直至余首一 $g(u)$ 与 (4) 真互素；每次商、乘积及最后 Bézout 都返回。这样移除的是完整物理不可能主分量，不只移除某个幂次，也不从模因子识别 QQ 支。

剩余系数环
$$
A_\varphi=K_\varphi[u]/g(u),\qquad \deg g\le2
\tag{17}
$$
保所有 $u$ 重数。每个原分母，包括 $u-3,\rho,Q,\delta,P_{02}$，都须在整个 (17) 中完成真逆及乘回。若有任何未付分母，程序不把它局部化后丢掉坏分量。

随后在 $A_\varphi[t]$ 中重新构造未缩放的真 Gram (12)，核
$$
E_0=0,\quad F_2=2f,\quad P_2(g_0)=P_{02},\quad
N_4(g_0)=2\lambda P_{02},\quad P_{\rm jet}=3wP_{02},
$$
以及完整 $N_4(\mathbf V)=0$。两个原矩在常数域中也已准确返回。

沿[全权原首一 t 二次](../results/R150-appendix-unit211-Phi-zero-corrected-whole-monic-t-quadratic-exact-ten-columns-and-four-generator-NV-head.md)，取
$$
\mathcal R=(E_B+E_C/2-E_1)/2,\qquad
E_{Bo}=(E_B-E_C)/(2\rho),
$$
$$
q_t=\gamma_R\mathcal R+\gamma_OE_{Bo},\quad
\gamma_R=-\frac{B_q}{\ell bc(u-1)Q},\quad
\gamma_O=-\frac{8\delta}{\ell},
$$
$$
B_q=Q^2+(2u^2-3)Q+2(u-1)(2u-1)(u-2).
\tag{18}
$$
源码实际核 $q_t$ 的 $t^2$ 首项为一，并返回对真实 $E_1,E_B,E_C$ 的全部三个乘子。整个 $t$ 环境
$$
B_\varphi=A_\varphi[t]/q_t
\tag{19}
$$
确为单首一自由二元代数，所有重根仍保留。其作为 QQ 向量空间的维数是
$N=2\deg\varphi\deg g\le16$。这里并未声称加入原条件后的真实商自由。

## 5. 八条完整原行和事前固定正目标

只输入同一 Gram 的下列八条原必要式：
$$
E_1,\ E_B,\ E_C,\ N_1,\
N_4(g_B)-2\lambda P_{02}h^2,\
N_4(g_C)-2\lambda P_{02}k^2,\
P_2(g_B)-P_{02}h^3,\
P_2(g_C)-P_{02}k^3.
\tag{20}
$$
其中 $E_1$ 使用真正 $\operatorname{vm}(d,d)[1]=2d_0d_1$；
$N_1$ 使用完整极化
$N_4(g_0+g_1)-N_4(g_0)-N_4(g_1)-4\lambda wP_{02}$。
两 singleton 的完整值都保留，不仅是加权和或奇部。

每条 (20) 乘 (19) 的全部 QQ 基，再仅按首一 $q_t$ 作普通除法。由于 (19) 是真实代数，这 $8N$ 条列准确生成其原理想作为 QQ 模；并非把某个裸乘法矩阵假定为自由结合代数。各余式通过 (18) 反传为 (20) 的八原普通组合。

执行前固定目标为
$$
1,\quad U^1,\quad U^2,\ \ldots,\ U^N,\qquad
U=\lambda D\,t(f-u).
\tag{21}
$$
逐个目标只有在完整 QQ 原列组合返回后，才把其首一除法商和 (18) 的原乘子加回，最终在整个 $A_\varphi[t]$ 中返回
$$
U^n=\sum_{i=1}^8\Omega_i(t)F_i(t).
\tag{22}
$$
完整 $t$ 多项式再次乘回，而不只比较 $q_t$ 的两个余坐标。QQ Gaussian 只用于选择原列的有理组合，不把 Gaussian 余行当成新原输入；程序另返回整个 QQ 向量和 (22)。

因为 (21) 在当前物理图是非零原目标，任何实际 (22) 足以排相应整个常数分块。$n=0$ 是直接返 1。若全部预定幂未返，保留该整个有限分块及其原值纤维；不能只由 rank、有限维数、模 $D=0$ 或预计 nilpotence 宣称排除。

## 6. 全重数与原题范围

若 $P_4$ 中 $\varphi$ 的重数为 $e>1$，先在其整个剩余域返回 (22)。原 CRT 主分量内，$\varphi$ 是幂零理想。只在已付原单位局部化中，(22) 使相应有限原理想模 $\varphi$ 为单位；有限几何级数把单位提升到该主分量。这里不会把一个单独 $\varphi$ 当作整个未分块环中的幂零元。所有 $u$ 重数已由 (17) 原样保留，(19) 的 $t$ 重数也保留。

若所有常数因子均通过其原单位条件、完整 NV 常数、旧单位主分量移除或实际 (22) 关闭，才排整个 (1)。只要有一个因子未关闭，整个 (1) 就继续保留其未闭部分。无论结果如何，本输入不把一般 $\ell=3/2$、第一 NV 头、第二头其余权点或整个 Phi 宣称为空。

本次只有新四次原矩身份、新完整缩放 NV 二次、这些新完整常数纤维中的八原值目标。没有重放第一头已冻三 scalar gcd、旧二十列、八条奇部列或最新小六列与两个 cofactor。输出仅元数据、profiles、实际原返回及统计；不存系数载荷、编码缓存或继承失败门中间态。
