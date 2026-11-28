# R1059 — 原 p² 剔除来源与局部 AI 读者的全临界 germ 比较

日期：2026-11-28 UTC。会话 Astra-rank2-Sha-0b097461-20261127。

按根 README 第8条登记完整证明。

本稿核定原同一个 cyclic-$p^2$ 来源的标量和极限。
它证明一个含完整旧项的临界 germ 恒等式，再给出其真实导数。
实际 Weil 字到 class/avatar 的有限对应复用
[R1054§9](R1054-original-p-square-depleted-source-and-exact-conductor-blocks.md)
的完整系数、真实矩阵和标记；本文不更换该对应，不把新 ramified 读者赋予原 canonical 坏条件。

## 1. 同一条商、同一微分及精确旧项

### 1.1 先由 Tate 配对固定内在 KS，而非用周期等式定义导数

沿 R1056(16)及 R997 原正号规范，基准水平 de Rham/Tate 基为
$e_1,e_2$，$\langle e_1,e_2\rangle=+1$，
$\omega_{\rm can}=-ze_1+e_2$。
这里的配对已经用原固定的 Tate/cyclotomic generator 标量化。
若换实际 Tate 标记 $\alpha$，记其配对为
$\kappa_\alpha=\langle e_{1,\alpha},e_{2,\alpha}\rangle$；
它是水平常数，基准 $\kappa_0=1$。

对原 right action 的 $g\in{\rm GL}_2(\mathbf Q_p)$，令
$p^\ell g$ 为定义中选定的整 primitive 矩阵，
$\phi:E\to E'$ 为真实商，$d_\phi=\deg\phi$。
作者2018稿印页18、(27)之前的定义是
$$
 \alpha'=(\check\phi_*)^{-1}\alpha\,p^\ell g
         =d_\phi^{-1}\phi_*\alpha\,p^\ell g .
 \tag{A0a}
$$
主极化将同调 Tate 基与所用 de Rham 基相连；
在此识别下，$\phi^*$ 对应 $\check\phi_*$，所以
$$
 \phi^*e'_i=\sum_j(p^\ell g)_{ji}e_j,\qquad
 d_\phi\kappa_{\alpha'}
 =\langle\phi^*e'_1,\phi^*e'_2\rangle
 =p^{2\ell}\det(g)\kappa_\alpha .
 \tag{A0b}
$$
中间等号是 Poincaré 配对的实际同源公式
$\langle\phi^*u,\phi^*v\rangle=d_\phi\langle u,v\rangle$；
它不是只按矩阵 determinant 猜出的尺度。

因 $e_i$ 水平，
$$
 {\rm KS}_{\rm pol}(\omega_{\rm can}^{\otimes2})
 =\langle\omega_{\rm can},\nabla\omega_{\rm can}\rangle
 =\kappa_\alpha\,dz .
 \tag{A0c}
$$
先以 $\nabla$ 和实际 CM 分解投影，再以极化的
$\mathrm{KS}_{\rm pol}^{-1}$ 定义内在代数 CM 导数 $\mathcal D$。
标量 book 算子 $\delta_{\rm book}$ 则读 $dz$ 的系数。
所以每次由标量算子转为内在算子须乘 $\kappa_\alpha^{-1}$。
由于 $\kappa_\alpha$ 水平，逐次严格得到
$$
 \boxed{\ 
 \theta(\delta_{3,{\rm book}}^nF_0)(y_\alpha)
   =\kappa_\alpha^n\,\Omega_\alpha^{3+2n}
      (\mathcal D_3^nf)(E,\omega_E).
 \ }
 \tag{A0d}
$$
右边的 $\mathcal D$ 已由 universal curve、极化、连接及 CM
splitting 独立定义；本式没有反过来定义一个方便的
$r_n^{\rm alg}$。AI 的代数 CM 导数正用这一连接与 KS。

对实际基准 $g_2^2=\operatorname{diag}(1,p^2)$，
$\ell=0,d_\phi=p^2,\det(g_2^2)=p^2$；
(A0a)给
$\alpha'=(q_C\alpha_1/p^2,q_C\alpha_2)$，故
$\kappa_{\alpha'}=\kappa_0=1$。
因此该基准确实没有遗漏一个额外的非单位 $p^{2n}$。
若另从非规范化标记开始，则必须先保其共同
$\kappa_0^n$；这里使用的 $\kappa_0=1$ 来自原 R1056(16)
的固定正号 frame，而非把书中某个别的常数设为1。

对单位 $g_t$，$\ell=0,d_\phi=1$，
$\kappa_{\alpha g_t}=N(t)\kappa_\alpha$。
又 $\Omega_{0,t}=\Omega_0/\bar t$，所以原 spherical 来源满足
$$
 \theta(\delta_{3,{\rm book}}^nF_0)(yg_t)
   =N(t)^n\bar t^{-3-2n}
           \theta(\delta_{3,{\rm book}}^nF_0)(y).
 \tag{A0e}
$$
完整 tensor pullback 必须连
$j_t(n)=N(t)^{-n}\bar t^{3+2n}$；
它与(A0e)的全部因子恰相消。
特别 $t=c\in\mathbf Z_p^\times$ 时，scalar 变化是 $c^{-3}$，
并非只按一个 weight-$3+2n$ 系数猜测。
$\Omega_\Gamma(A,\mathfrak t)$ 在书(5.75)、Definition8.10中
另比较指定有限层余切参数与 classical normalization；
本文不用该参数比较，也不声称 $\Omega_\Gamma=1$。
(A0a)--(A0d)在同一个极化 KS 上直接支付所需内在归一。

### 1.2 同一商的正权逐点式

固定 $p>211$ 惰性、原 weight-three $f$，以及原全部 tame level。
对每个实际 cyclic-$p^2$ 核 $C$，记
$$
q_C:E_0\longrightarrow E_C,\qquad
q_C^*\omega_C=c_C\omega_0.
$$
$\omega_0,\omega_C$ 为已经指定的好整模型微分。
使用书版正向周期和 AI marked differential：
$$
\omega_0=\Omega_0\omega_{{\rm can},0},\quad
\Omega_{C_0}=p^{-2}c_{C_0}\Omega_0,\quad
\omega_{{\rm AI},C}=\Omega_{{\rm AI},C}\omega_C,\quad
d_C=\Omega_{{\rm AI},C}c_C,\quad u_C=d_C\Omega_0.
\tag{A1}
$$
$\Omega_{C_0}$ 是基准核的真实 book 周期；
在 $yg_tg_2^2$ 上裸周期是
$p^{-2}c_C\Omega_0/\bar t$，必须连(A0e)的配对因子，
不能把(A1)的基准式原封搬到裸 $yg_t$ 点。
此处 $u_C$ 是真实单位。固定第一层 $C_1$ 后，
写 $q_C=\varphi'_C\circ q_1$，marked 选择满足
$(\varphi'_C)^*\omega_{{\rm AI},C}=\omega_1$，
$q_1^*\omega_1=d_{C_1}\omega_0$，所以
$$
d_C=d_{C_1},\qquad u_C=u_{C_1}.
\tag{A2}
$$
(A2)仅说同一个 wild block 内相同，不说 $p+1$ 个不同
第一层 block 的单位相等。

令 $w_n=3+2n$，并以(A0d)的内在 CM 算子定义
$r_{C,n}=(\mathcal D_3^nf)(E_C,\omega_C)$。
对基准核 $C_0$，有
$$
R^{\rm new}_{C_0,n}
 =p^{4n+2}\theta\bigl((g_2^2)^*
                    \delta_{3,{\rm book}}^nF_0\bigr)(y)
 =p^{-4}(c_{C_0}\Omega_0)^{w_n}r_{C_0,n}.
\tag{A3}
$$
这里用的就是 $\kappa_{C_0}=1$ 与
$p^{4n+2}p^{-2w_n}=p^{-4}$。
对一般实际核 $C=C_t$，$R^{\rm new}_{C,n}$ 表示在 $yg_t$
的同一表达式连 $j_t(n)$、全部 level 和 coefficient transport
完整拉回原基后的值。由(A0e)同样严格为
$p^{-4}(c_C\Omega_0)^{w_n}r_{C,n}$。
这不是将裸 $yg_t$ 标量假装不变，也不将所有 $r_{C,n}$
改为原 maximal-CM 点的 Taylor 系数。

AI Appendix A 的 $V_H=\varphi^*/p$ 与 KS 给
$\nabla V=pV\nabla$，故在同一内在 KS 规范下
$$
\mathcal D_3^n V^2=p^{2n}V^2\mathcal D_3^n.
\tag{A4}
$$
在 actual incoming canonical $p^2$ 路径上，
$(E_C,\omega_{{\rm AI},C})$ 经 $V^2$ 返回
$(E_0,d_C\omega_0)$。保全原 full9 的两次 central/diamond
作用后，其平方为 $+1$；$a_p=0,\epsilon(p)=-1$ 给
$f^{[p]}=f-p^2V^2f$。因此
$$
\begin{split}
p^{-4}u_C^{w_n}\,
 \mathcal D_3^n f^{[p]}(E_C,\omega_{{\rm AI},C})
 &=R^{\rm new}_{C,n}
   -p^{2n-2}\theta(\delta_3^nF_0)(E_0).
\end{split}
\tag{A5}
$$
逐项核对如下。第一项按
$\mathcal D_3^nf(E_C,\omega_{{\rm AI},C})
=\Omega_{{\rm AI},C}^{-w_n}r_{C,n}$
与 $d_C=\Omega_{{\rm AI},C}c_C$ 恰给(A3)。
第二项按(A4)为
$$
-p^{-4}u_C^{w_n}p^2p^{2n}d_C^{-w_n}r_{0,n}
=-p^{2n-2}\Omega_0^{w_n}r_{0,n}.
$$
这已包括 KS determinant 的费用，不再乘一次 $p^{2n}$。

与真实 bad depleted 来源比较时还有一个不可省的差。
将 $yg_t$ 上各个实际裸 $Q_t$ 来源记为
$F_{0,C},A_C=-F_{0,C}+B_C$，其 unflat 值添上标
$\,{}^{\rm raw}$。令
$$
\mathfrak j_C(n)=N(t)^{-n}\bar t^{3+2n},\qquad
R_{0,C,n}=\mathfrak j_C(n)R^{\rm raw}_{0,C,n},\qquad
R_{A_C,n}=\mathfrak j_C(n)R^{\rm raw}_{A_C,n}
        =R^{\rm new}_{C,n}-R_{0,C,n}.
\tag{A5a}
$$
基准核取 $t=1$。全部原 level、tame、Artin/Cor 和
coefficient transport 仍包含在 $C$ 及来源中。
(A5)的准确形式是
$$
\boxed{\quad
p^{-4}u_C^{w_n} I_C^{\rm AI}(n)
 =R_{A_C,n}+(1-p^{-2})R_{0,C,n}
 =\mathfrak j_C(n)\bigl(R^{\rm raw}_{A_C,n}
                    +(1-p^{-2})R^{\rm raw}_{0,C,n}\bigr),
\quad
I_C^{\rm AI}(n)
 =\mathcal D_3^nf^{[p]}(E_C,\omega_{{\rm AI},C}).
\quad}
\tag{A6}
$$
所以 AI 归一化与原 bad depleted 在正整数权并非逐点相同。
后面只能在完整原权下处理最后这个旧项。

(A5)--(A6)是点值标量式；它们没有消去 toric 权中的
$N(\mathfrak a)^n$、$\iota(a_p)^{-1}$、有限 character 或 Haar。
这些属于实际外系数，必须在下文的 $\lambda_C(j)$ 内逐个保留。

## 2. 固定 Teich 分量和实际正整数逼近

令 $\mathcal I$ 是实际有限 CM/level/word 集合。
对 $C\in\mathcal I$，保留同一个 bounded bad-$Q_2$ 来源
$A_C(Q)$ 及旧来源 $F_{0,C}(Q)$。
这是各点实际 good pullback/source 返回的裸输入，不是从
period unit 或有限字非零推导 boundedness。
尤其，不把 $\mathfrak j_C(n)R^{\rm raw}_{A_C,n}$ 自动视为
另一个有界 Amice 测度的矩。$\bar t/t$ 未必在
$\mathbf Z_p$；R1058 的 Möbius 小盘互绕也没有支付一个
whole-unit-disc 的 $Q\mapsto Q^{\bar t/t}$ 有界代换。
因此 $\mathfrak j_C(j)$ 始终是下文明确保留的解析外权。

设其系数界为 $m_C>-\infty$，实际 Maass 常数为
$\mathfrak c_C$，满足
$v_p(\mathfrak c_C)>-1/(p-1)$。
在原 maximal-CM $b=2$ 基中其估值正好是 $2$。
对旧来源作同样记号。集合有限，所有一致尾估计可取最小界。

取正整数 $D$，$p\nmid D$，使其包含
$6$、$p^2-1$，以及实际有限个单位 $u_C$ 与所有外权中单位
的 residue orders。每个 $\mathbf C_p$ 单位的 residue 在
$\overline{\mathbf F}_p^\times$ 中都有有限阶；
不需要谎称这些单位处于某个共同固定代数扩域。

再取一个统一 $e\ge0$，使每个
$u_C^{Dp^e}$ 及外权所需单位的对应幂进入
$v_p(x-1)>1/(p-1)$ 的 exponential 圆盘，并锁定所有
$p$-power finite 相位。再增大 $e$，使实际有限个 AI
局部 evaluation 与外系数都在该同一参数盘解析。这样在
$$
j=-2+Dp^e z,\qquad z\in\mathbf Z_p
\tag{A7}
$$
上，$u_C^{3+2j}$ 有唯一与正整数权一致的局部解析分支。
它在 $j=-2$ 等于 $u_C^{-1}$；关于 $j$ 的导数为
$2\log\langle u_C\rangle\,u_C^{3+2j}$。
这里 log 杀掉实际 Teich/root-of-unity 部分；其估值不预设非负。

对每个 $z$，令 $a_l\in\{0,\ldots,p^l-1\}$ 为 $z\bmod p^l$，
取
$$
n_l=-2+Dp^e(a_l+p^l).
\tag{A8}
$$
于是 $n_l\ge0$（略去有限个初项）、$n_l\to+\infty$，
在固定 Teich 分量中 $n_l\to j$，且 $n_l\equiv4\bmod6$。
所有所需 prime-to-$p$ finite phases 恒定；
$p$-power finite phases 也由上述深度锁定。
尤其 $u_C^{w_{n_l}}\to u_C^{3+2j}$。
这个构造并没有对 $p^{n_l}$ 定义一个解析延拓。

## 3. 完整 Maass 极限，而非只留最高微分项

对上述一个实际 bounded 来源 $A$，记其 full Amice measure 为
$\mu_A$，$m_h=\int_{\mathbf Z_p}x^h\,d\mu_A(x)$。
该实际裸来源的 unflat Maass 值是
$$
R^{\rm raw}_{A,n}
 =\sum_{i=0}^n c_i(n)\mathfrak c^i m_{n-i},\qquad
c_i(X)=\binom{X+2}{i}\binom Xi\,i!.
\tag{A9}
$$
对固定 $i$，沿(A8)，在 $\mathbf Z_p$ 上一致有
$$
x^{n_l-i}\longrightarrow
 {\bf1}_{\mathbf Z_p^\times}(x)\,
 \omega(x)^{-2-i}\langle x\rangle^{j-i}.
$$
在 $p\mathbf Z_p$ 上，一致收敛由 $n_l-i\to+\infty$ 给出；
在单位上由固定 Teich 分量和 $n_l\to j$ 给出。
所以 fixed-$i$ 的 full moments 收敛到真实 unit moments。

另一方面，(A9)第 $i$ 项的估值统一至少
$$
m_A+v_p(i!)+i\,v_p(\mathfrak c)\longrightarrow+\infty.
\tag{A10}
$$
原 $\binom{n_l+2}{i},\binom{n_l}{i}$ 均为整数；
$i>n_l$ 时原项为零。由(A10)可交换极限与整个 $i$ 和，
得到恰好 R1056 的完整 flat germ
$$
\lim_lR^{\rm raw}_{A,n_l}
 =\mathcal M_A(j)
 =\sum_{i\ge0}c_i(j)\mathfrak c^i
       \int_{\mathbf Z_p^\times}x^{j-i}\,d\mu_A.
\tag{A11}
$$
这里 $x^{j-i}$ 同时保两坐标，不能只记其 $p$-adic 指数。
此 proof 对实际有限字/原点集合逐个成立，有限总和仍可交换。
乘以在(A7)上有界的实际解析外系数也同样成立。

同 R1056 §2，在一般显示的半径条件下，导数尾的估值至少
$$
m_A+v_p(i!)+i\,v_p(\mathfrak c)-\lfloor\log_p i\rfloor
 \longrightarrow+\infty.
$$
这直接支付一致 $C^1$ 极限；不据此泛称任意这样的半径都已经
给出同一个刚性解析意义的 Tate 圆盘。

本题实际 $b=2$ 来源有 $v_p(\mathfrak c)=2$，可进一步直接
支付本稿所需的刚性解析 germ。完整多项式为
$$
c_i(X)=
 \frac{\displaystyle\prod_{r=0}^{i-1}(X+2-r)
                  \prod_{r=0}^{i-1}(X-r)}{i!}.
\tag{A10a}
$$
其分子在 $\mathbf Z_p[X]$。在(A7)的闭参数盘
$z\in\mathcal O_{\mathbf C_p}$ 上有 $|j|\le1$，于是
$c_i(j)$ 的 Gauss 估值至少 $-v_p(i!)$。
真实 unit moment
$\int\omega(x)^{-2-i}\langle x\rangle^{j-i}\,d\mu_A$
在该盘是有界解析函数：$x\in\mathbf Z_p^\times$ 给
$v_p(\log\langle x\rangle)\ge1$，而
$\langle x\rangle^{Dp^ez}$ 的 exponential 系数一致收敛。
其 Gauss 估值至少 $m_A$。因此(A11)第 $i$ 项的 Tate
范数估值统一至少
$$
 m_A+2i-v_p(i!)\longrightarrow+\infty.
 \tag{A10b}
$$
(A11)是在 Tate 代数中收敛的解析函数，而非仅有点值极限。
分子多项式的一阶导数仍整；moment 导数另外乘
$\log\langle x\rangle$。故关于 $j$ 的整个导数级数也满足
同类界，(A14)--(A16)可逐项求导。
外部有限单位幂则由(A7)所选更小 exponential 盘支付。
这里的强解析性严格限定实际 $v_p(\mathfrak c)=2$ 的应用；
没有将一般 $C^1$ 半径扩大。

## 4. 整个临界 germ 的同源恒等式

对每个实际 marked $C$，以
$I_C^{\rm AI}(j)$ 记 AI 局部解析 CM-evaluation family，
其正整数值必须正好是(A6)显示的完整值。
这里仅使用实际 marked evaluation 与 CM splitting；
不凭同一 Hecke 标签替换来源或宣布另一个 global L-function 相等。

尤其，AI 的全局 Heegner 假设
$\mathcal O_K/\mathfrak N\simeq\mathbf Z/N\mathbf Z$
不能免费用于本篇含惰性 $2$ 的 full2/full9 来源。
这里使用其局部连接、canonical subgroup、marked differential
及固定 classical weight $3$ 的局部 evaluation 构造：
Definition4.24、Definition5.2、Remark5.3，以及
Proposition5.6证明中的逐点解析性；固定 classical 单变量的
$p^2$ conductor 范围见 Definition5.7前的说明。
这些在同一个 prime-to-$p$ finite étale level cover 上拉回：
通用椭圆曲线、极化 KS、Gauss--Manin 连接、$V$ 和实际
CM splitting 均逐点兼容，局部半径保持。
完整 full2/full9/17 标记、vector-valued 分量及 projector
逐分量原样保留，不以降层抹掉有限字。
本段不调用 AI Theorem7.1，也不声称已得到一个满足其全局
Heegner 条件的新 $L_p$。

(A6)使用 basic marked $\omega_{{\rm AI},C}$。
若改用 actual global 标记 $\omega_{a_t}=t\,\omega_{{\rm AI},C}$
及 $a_{t,p}=t^{-1}$，则本文的
$I_C^{\rm AI}(j)$ 恰须写成
$t^{3+2j}(\mathcal D_3^jf^{[p]})(E_C,\omega_{a_t})$。
这个 $t^{3+2j}$ 连实际 avatar、原有限字一起运输；
它不是(A0e)的 book tensor 因子，也不代替 $N(t)^{-j}$。
下文 $\lambda_C$ 与 $I_C^{\rm AI}$ 总是以同一标记约定配对。

令 $\lambda_C(j)$ 为已逐字识别的原有限 toric 外系数，
保所有有限角色、$\iota(a_p)^{-1}$、$N(\mathfrak a)^j$、
Haar、Artin/Cor、矩阵基变换及标记运输。
若在向量基中运输给矩阵，逐个矩阵项纳入同一个有限集合，
不能将它误作同一标量不变性。
要求 $\lambda_C$ 取真实对应的局部解析 branch。
另将实际 book tensor 因子单列为
$$
\Lambda_C(j)=\lambda_C(j)\mathfrak j_C(j),\qquad
\mathfrak j_C(j)=N(t)^{-j}\bar t^{3+2j}.
\tag{A11a}
$$
这是两侧外权的真实关系。$\lambda_C$ 乘 basic AI 读者，
$\Lambda_C$ 乘裸 $Q_t$ Amice 读者；两者不冒作同一权，
也没有将 $\mathfrak j_C$ 吞进测度。

将(A6)沿(A8)取极限，依(A11)得到对整个(A7)成立的精确式
$$
\boxed{
p^{-4}\sum_C\lambda_C(j)u_C^{3+2j}I_C^{\rm AI}(j)
 =
 \sum_C\Lambda_C(j)\mathcal M_{A_C}(j)
 +(1-p^{-2})\,\mathcal O(j),
}
\tag{A12}
$$
其中保留的旧 germ 是
$$
\mathcal O(j)=\sum_C\Lambda_C(j)\mathcal M_{F_{0,C}}(j).
\tag{A13}
$$
因此所需旧项消去有两种严格可接受的支付方式：

1. 已证明在每个 $C_1$ block 中，包含所有 avatar/tensor 后，
   整个旧正权项的 actual primitive-wild 加权和为零。
   此时对所有 $n_l$ 是精确零，故(A13)是零 germ。
2. 已证明(A13)本身是 R1052 的同一完整原 toric germ，
   或其已经识别的有限解析倍数/有限和。
   必须保同一实际 outer weights；仅来源未改动、总 conductor
   或抽象 wild 标签相同均不足够。

若只证明(A13)在 $j=-2$ 为零，则(A12)只在值上去旧项，
导数仍须保 $\mathcal O'(-2)$。
不得把 $\mathcal O$ 的一个所选 scalar 零扩成每个 block 零。

(A12)先对(A7)每个 $z\in\mathbf Z_p$ 用真实正整数序列证明。
两边已在同一个闭参数盘上解析；这些值含聚点，故一变量恒等
原理给整个解析 germ 身份，可以在其成立范围内求导。
没有使用 $p^{2j}$ 的不存在的权插值，也没有从单个临界值猜整个比较。

## 5. 端点与全部一阶费用

写
$$
I_C^Q=\int_{\mathbf Z_p^\times}x^{-2}\,d\mu_{A_C}(x),
$$
$$
L_C^Q=
 \int_{\mathbf Z_p^\times}x^{-2}\log\langle x\rangle\,d\mu_{A_C}(x)
 -\sum_{i\ge1}(i+1)(i-1)!\mathfrak c_C^i
       \int_{\mathbf Z_p^\times}x^{-2-i}\,d\mu_{A_C}(x).
\tag{A14}
$$
完整 Maass 两个数分别是
$\mathcal M_{A_C}(-2)=I_C^Q$ 与
$\mathcal M_{A_C}'(-2)=L_C^Q$。
这些 $I_C^Q,L_C^Q$ 都属于实际裸来源。
令 $\ell_C=\log\langle u_C\rangle$；另有完整 determinant 导数
$$
\frac{\mathfrak j_C'(-2)}{\mathfrak j_C(-2)}
 =-\log\langle N(t)\rangle+2\log\langle\bar t\rangle,\qquad
\Lambda_C'
 =\mathfrak j_C\bigl(\lambda_C'
       +\lambda_C[-\log\langle N(t)\rangle
                      +2\log\langle\bar t\rangle]\bigr).
\tag{A14a}
$$
所有 log 按(A7)的同一分量取值。
(A12)的端点为
$$
\sum_C\Lambda_C(-2)I_C^Q
 =
 p^{-4}\sum_C\lambda_C(-2)u_C^{-1}I_C^{\rm AI}(-2)
 -(1-p^{-2})\mathcal O(-2).
\tag{A15}
$$
对整个 germ 求导，恰给
$$
\begin{split}
\sum_C\{\Lambda_C'(-2)I_C^Q+\Lambda_C(-2)L_C^Q\}
={}&p^{-4}\sum_Cu_C^{-1}
 \bigl\{\lambda_C(-2)(I_C^{\rm AI})'(-2)\\
&\hspace{18mm}
 +[\lambda_C'(-2)+2\lambda_C(-2)\ell_C]\,
            I_C^{\rm AI}(-2)\bigr\}\\
&-(1-p^{-2})\mathcal O'(-2).
\end{split}
\tag{A16}
$$
这是完整一阶式；没有删 $2\ell_C I_C^{\rm AI}$、
外 $\lambda'/N$、(A14a)的真实 tensor 导数
或任何 $c_i'(-2)$ 项。
若改用原 $j(u)=(p^2-1)u-2$，两边整体导数再乘
$p^2-1$，并对外权取该相同参数；没有自由改换角导数。
$p^{-4}$ 和 $1-p^{-2}$ 的估值成本同样保留。

## 6. 同一 wild restriction 内的整 tame 矩阵

固定一个非平凡 wild restriction $\vartheta|_{T_1}$。
其 $p+1$ 个 tame extensions 可先选一个 extension，再以
$T_2/T_1$ 的全部 characters 标记。固定这个规范后的 tame
Fourier 矩阵记为 $\mathcal F$；分母 $p+1$ 是 $p$ 单位，
所有 finite phases 均为单位，原 paired tensor 仍在输入中。

在第一层 block 基中，单位权恰为
$\operatorname{diag}(u_{C_1}^{3+2j})$。在 tame character 基中，
完整矩阵是
$$
M(j)=\mathcal F\,
  \operatorname{diag}(u_{C_1}^{3+2j})\,\mathcal F^{-1},
\qquad
M(j)^{-1}=\mathcal F\,
  \operatorname{diag}(u_{C_1}^{-3-2j})\,\mathcal F^{-1}.
\tag{A17}
$$
故在(A7)所选盘，$M(j)$ 的值是整可逆矩阵；以 $z$ 为小盘参数，
其整个解析矩阵及逆也整。这不要求不同 $C_1$ 的 $u$ 相同。
其关于 $j$ 的真实导数为
$$
M'(j)=\mathcal F\,
 \operatorname{diag}(2\log\langle u_{C_1}\rangle
                        u_{C_1}^{3+2j})\,\mathcal F^{-1}.
\tag{A18}
$$
不从(A17)擅推 $M'(j)$ 在原 $j$ 参数下具有单位或整性界；
把小盘参数 $z$ 的导数换回 $j$ 时须保 $Dp^e$。

若 $\mathbf A,\mathbf I_{\rm AI},\mathbf O$ 分别表示这同一
wild block 的完整 $Q$、AI 和旧-source covector，其中
$\mathbf A,\mathbf O$ 必须先在外权中包含
$\mathfrak j_C(j)$（仍不是新 Amice 测度），
(A12)逐坐标就是
$$
\mathbf A(j)
 =p^{-4}M(j)\mathbf I_{\rm AI}(j)
  -(1-p^{-2})\mathbf O(j).
\tag{A19}
$$
外部原 toric covector 再作用于(A19)时，其自身导数仍保留。
只有已支付的同一旧向量或实际 scalar 组合可被消去。
这确实允许 tame mixing，而非把 unit period 强设成共用标量；
它不赋原 canonical 坏条件给全部 $\vartheta$，
也不证明新临界值或新导数非零。

## 7. 可直接消费的范围

本稿付清实际 Tate/cup/KS 规范(A0a)--(A0e)、点式(A6)、
同 source 旧项、合法 Teich 逼近、
完整 Maass 尾、两侧真实外权(A11a)、整个 germ(A12)、
端点(A15)和全斜率(A16)。
结合已经支付的 actual finite Weil→class/AI avatar 以及(A13)
的实际消去，才能将新的 ramified $Q$ 读者送到同一 AI germ。
若(A13)仍未识别，则(A12)保留它，是精确的剩余项。

这条比较不使用 CM 主单位等于 $Q$-root rotation；
R1058 仅提供完整运输与根平均互绕。也不把新 p² 解析读者
改名成原 $S/T$ canonical Newton 读者。

### 精确来源

- [R1056](../results/R1056-original-flat-amice-critical-slope-and-bol-primitive.md)
  §§1–2、5：同一个 actual bounded 来源、全部 Maass 系数、
  derivative tail 和真 unit projector。
- [R1052](../results/R1052-original-unmodified-b2-toric-flat-vanishing.md)：
  仅其明示的全部原 toric 权下 unmodified 分支恒零。
- [R1058](../results/R1058-original-cm-principal-unit-mobius-and-centered-root-trace.md)：
  centered Möbius、determinant、全盘 root-average 互绕；
  不作 root/CM 分支同一化。
- D. Kriz, 作者2018稿 §2.4，印页18、(27)之前的
  $\alpha'=(\check\phi_*)^{-1}\alpha p^\ell g$ 定义：
  [作者原稿](https://arxiv.org/pdf/1805.03605)。
  基准 KS 正号使用书版及 R1056(16)，不沿用2018的相反符号。
- F. Andreatta–A. Iovita, *Katz type p-adic L-functions for primes
  p non-split in the CM field*, CMH99 (2024),641–716，
  Appendix A、Definition4.24、Definition5.2/Remark5.3、
  Proposition5.6的局部证明、Definition5.7/Remark5.8、Proposition5.9；
  本文只使用上述可拉回的局部输入，不套全局 Heegner 定理：
  [已发表全文](https://ems.press/content/serial-article-files/48931)。

全部为纸笔等式与一致收敛证明，无新增数学执行。


## 8. 真负端点到同一有限图；全部旧项及向外费用

本节把(A15)的值端接到同一个实际 Coleman--AJ 读者。
来源、各点的 bounded $Q_2$ 输入、$(A7)$ 的权分量及全部外权均
保持前七节。新的 $\psi_4^2$ 来源使用原 degree17 图和两个
full2 取向；它不被替换成 $\psi_{27}^2$ 的旧54图。
本节不需要将 $Q\mapsto\zeta_pQ$ 解释成单条 CM 同源。

### 8.1. 局部 CM 负二阶是哪个原函数

先在原共同 full tame 模空间上令
$\mathcal H=R^1\pi_*\Omega^\bullet$，把实际 weight3 形式 $f$
按本来的正号 KS 写成 $\mathcal H$-值微分，记其
Frobenius-rigid Coleman primitive 为 $G$。
若实际形式是 $-\delta f_4(\tau/6)$，则这个完整有限级来源、
变量倍率和 $-\delta$ 均在 $f,G$ 内；不以首系数1的另一形式
代替它。

固定原 R997§4 的完整多项式规范：
$Q(\Phi)[f]=0$，$Q(\Phi)$ 在局部解析水平截面上可逆，
且 $Q(1)\ne0$；要求 $Q(\Phi)G$ 在指定宽开集上 rigid analytic。
权重分离给这样的 $Q$。剩余全局 rigid 水平差由该有限级
通用椭圆曲线的实际 monodromy 排除。
这既不任设局部常数，也不使用“负权就没有 slope-zero
子空间”的说法。比较任一具体 Frobenius lift 时，
用其有限次幂的真实特征值和 $1-\Phi$ 的可逆性，
不把 slope-zero 与 Frobenius 固定向量混同。

在 conductor-$p^2$ 的 actual canonical chart，
AI2024 Propositions7.6--7.8 的局部证明可随原 prime-to-$p$
有限 étale level cover 拉回。这里只用连接、marked differential、
CM splitting 及该 chart 内的解析截面，仍不调用其全局
Heegner-character Theorem7.1。

为核符号和阶乘，在 CM 点附近取
$\langle\omega,\eta\rangle=1$ 的水平基，令
$\omega'=\omega+b\eta$、$b(x_C)=0$。
则
$\nabla\omega'=\eta\,db$、$\nabla\eta=0$，
正号 KS 为 $\mathrm{KS}((\omega')^2)=db$。
写
$$
 G^{[p]}=g_0\omega'-g_1\eta,\qquad
 f^{[p]}=h(\omega')^3 .
$$
原连接方程逐项给
$\partial_b g_0=h$、$\partial_b g_1=g_0$，
而在 CM 点
$\langle G^{[p]},\omega'\rangle=g_1$。
AI Proposition7.8 的 $r=k-2=1$、$j_{\rm AI}=1$
准确选这个槽，系数是 $+1/1!$。
因此 basic marked 微分下，前文的同一解析族满足
$$
 \boxed{\quad
 I_C^{\rm AI}(-2)
    =\left\langle G^{[p]}(E_C),
                       \omega_{{\rm AI},C}\right\rangle .
 \quad}
 \tag{A20}
$$
这里的 $G^{[p]}$ 是上面的 Frobenius-rigid $G$ 的完整剔除，
不是另取一个局部双原函数。AI Proposition7.6 先在其实际宽开集
识别这一截面，再由 Proposition7.8 的局部计算评价。
正号也同 R1056(16)--(20)及原 Tate 关系
$\langle G^{[p]},\omega\rangle=\theta^{-2}f^{[p]}$ 一致。
只用后一个 cusp 关系本身不足以支付其它 residue disc；
本段使用的是前述同一个 Coleman 截面。

这里采用 Proposition7.8 证明中同一个 marked differential 的
局部式，不从文字提取中跨两个微分的 $\Omega$ 幂次反推归一。
实际缩放可以独立核定：若
$\widetilde\omega=\Omega\omega$、
$\widetilde\eta=\Omega^{-1}\eta$，则
$
 G=g_0\omega-g_1\eta
   =g_0\Omega^{-1}\widetilde\omega
       -g_1\Omega\widetilde\eta,\qquad
 \widetilde g_1=\Omega g_1
       =\langle G,\widetilde\omega\rangle .
$
因此 weight $-1$ 的同一负二阶值随微分乘 $\Omega$，
而不是 $\Omega^{-1}$。这项直接的同质性校验连同
$p704$--$705$ 的局部 GM 推导确定(A20)；
不据 PDF 文字提取的幂次声明原文有错。

若用实际 idelic 微分
$\omega_{a_t}=t\,\omega_{{\rm AI},C}$，
weight $-1$ 的值乘 $t$。R1054(48)在 $n=-2$ 的 avatar
因子 $t^{-1}$ 恰好将它送回(A20)，没有留下一个未记的 $t$。

### 8.2. incoming 旧项、cup 次数和绝对 p 幂

沿(A1)--(A2)记
$$
 q_C:E_0\longrightarrow E_C,\qquad
 q_C^*\omega_{{\rm AI},C}=d_C\omega_0,\qquad
 u_C=\Omega_0d_C,\qquad \deg q_C=p^2 .
$$
AI 的两步 canonical incoming 指向 $\widehat q_C:E_C\to E_0$，
其 $\mathcal H$-值 $V^2$ 正是
$p^{-2}\widehat q_C^*$。理由是每个
$V_H=\phi^*/p$，并且 $\nabla V=pV\nabla$；
从 $f^{[p]}=f-p^2V^2f$ 转为 primitive 时，
两次连接费用恰把显示的 $p^2$ 消去。
故当前 $a_p=0,\epsilon(p)=-1$ 下，
$$
 G^{[p]}(E_C)
   =G(E_C)-p^{-2}\widehat q_C^*G(E_0,[p^2]\ell).
 \tag{A21}
$$
所有 level 沿 actual isogeny 运输，原 level deck 仍保留。
这里不声称 $p^2\equiv1\pmod9$，也不把全部 level 字面认同。
在当前完整来源的本征块上，单步 central diamond 的特征为
$\epsilon(p)=-1$，因此两步作用为 $\epsilon(p)^2=+1$；
Coleman 唯一性使同一个 $G$ 具有这个实际来源特征。
只有先作用这条完整本征向量及其两步 diamond 后，
(A21)的末值才返回原 $G(E_0,\ell)$。
后续几何 level 的重标仍在原有限和内。

因此，在同一 $H^1_{\rm dR}$ 上
$$
 q_C^*G^{[p]}(E_C)
       =q_C^*G(E_C)-G(E_0).
 \tag{A22}
$$
这里用的是
$q_C^*\widehat q_C^*=[p^2]^*=p^2$，
不是 $H^2$ 上的 $p^4$。
(A21)也由同一个 Frobenius-rigid 规范识别，故(A22)
没有附加一份任意水平向量。

Poincaré 配对满足
$\langle q_C^*a,q_C^*b\rangle=p^2\langle a,b\rangle$。
结合 $q_C^*\omega_{{\rm AI},C}=d_C\omega_0$ 与(A20)--(A22)，
得到完全固定的点式
$$
 \boxed{
 p^{-4}u_C^{-1}I_C^{\rm AI}(-2)
  =p^{-6}\Omega_0^{-1}
       \left\langle q_C^*G(E_C)-G(E_0),\omega_0\right\rangle .
 }
 \tag{A23}
$$
这个 $p^{-6}$ 包含本篇的 $p^{-4}$ 和 cup 的 $p^{-2}$；
$d_C$ 已准确消去，未将它或 $\Omega_{{\rm AI},C}$ 猜成单位。

### 8.3. 同一有限 flat 值及原完整补项

允许原有限 word 集合包含不同的 tame CM 基点，
以 $i$ 标记，写其真实微分和 book 周期为
$\omega_i,\Omega_i$；$C$ 跑该基点的实际 cyclic-$p^2$ 核。
记 $\lambda_{i,C}$、$\Lambda_{i,C}$ 为(A11a)的同一外权，
不把 $\mathfrak j_{i,C}$ 吞进 Amice 测度。
将(A23)逐项代入(A15)，严格得到
$$
 \begin{split}
 \sum_{i,C}\Lambda_{i,C}(-2)I^Q_{i,C}
  ={}&p^{-6}\sum_{i,C}
       \lambda_{i,C}(-2)\Omega_i^{-1}
       \left\langle q_{i,C}^*G(E_{i,C})-G(E_i),
                                      \omega_i\right\rangle\\
    &-(1-p^{-2})\mathcal O(-2).
 \end{split}
 \tag{A24}
$$
$\mathcal O$ 是(A13)的完整旧 germ；(A24)没有重新定义它。
尤其不能把每个原点的旧 flat 值分别设零。
只有 R1054§9.7 已付的 full-avatar wild 正交，
或(A13)已经识别为 R1052 的同一整个 toric germ时，
才按原证明删除对应旧项。

现在取一条真实原图
$\varphi_i:A\to E_i$，记
$$
 m_i=\deg\varphi_i,\qquad
 \varphi_i^*\omega_i=e_i\omega_A,\quad e_i\ne0 .
$$
为避免与外系数混用，$e_i$ 在这里只表示这个实际微分倍率。
原图和复合图均取完整修正：
$$
 \Delta_i=\Gamma_{\varphi_i}
       -m_i(E_i\times O_A)-(O_i\times A),\qquad
 \Delta_{i,C}=\Gamma_{q_{i,C}\varphi_i}
       -m_ip^2(E_{i,C}\times O_A)-(O_{i,C}\times A).
 \tag{A25}
$$
使用同一 source 二形式 $\Omega_{\rm geom}$ 及原 $\omega_A$，
记相应 actual proper AJ 值为 $\mathcal J_i,\mathcal J_{i,C}$。
局部 residue/投影公式在这些已同调零的图上给
$$
 \mathcal J_i
   =\langle\varphi_i^*G(E_i),\omega_A\rangle,\qquad
 \mathcal J_{i,C}
   =\langle\varphi_i^*q_{i,C}^*G(E_{i,C}),\omega_A\rangle .
$$
在惰性处采用已付的 proper finite-polynomial/局部图比较：
先保实际 $1-\Phi$ 或 $P(\Phi)$ 分母，再读杯积。
没有将 R997§1 的 ordinary 范围直接改为 inert。
对新的 $\psi_4^2$ 曲面，
原图文稿(21)已给
$[G|_{E_i}]=p\,\xi_{i,p}/(p+1)$，
因此上述式子与其 proper fp 公式(29)完全同一，
不另丢掉 $p/(p+1)$。

再次只对 $\varphi_i$ 使用 cup 自然性，得到
$$
 \left\langle q_{i,C}^*G(E_{i,C})-G(E_i),\omega_i\right\rangle
    =\frac{e_i}{m_i}
                  (\mathcal J_{i,C}-\mathcal J_i).
$$
故(A24)给真实有限图返回
$$
 \boxed{\;
 \sum_{i,C}\Lambda_{i,C}(-2)I^Q_{i,C}
  =p^{-6}\sum_{i,C}
       \frac{\lambda_{i,C}(-2)e_i}{m_i\Omega_i}
                   (\mathcal J_{i,C}-\mathcal J_i)
    -(1-p^{-2})\mathcal O(-2).
 \;}
 \tag{A26}
$$
$e_i/m_i$ 是原图的实际费用；没有因“degree17”就擅设
原模型微分的拉回为1。若采用原图文稿规定的
$\varphi_i^*\omega_i=\omega_A$，则此费用恰为 $1/17$；
同时 $\Omega_i$ 必须使用该同一个微分。

### 8.4. exact-p² 字的真正向外图表达

在固定底曲线 $E_i$ 上加 $C$，其实际两退化映射给
$$
 G^{\rm out}(E_i,C)
       =G(E_i)-p^{-2}q_{i,C}^*G(E_{i,C}),\qquad
 \mathcal J^{\rm out}_{i,C}
       =\mathcal J_i-p^{-2}\mathcal J_{i,C}.
 \tag{A27}
$$
后式是原固定底曲线的修正图对
$d_0^*\Omega_{\rm geom}-p^{-2}q^*d_2^*\Omega_{\rm geom}$
的 actual AJ 值，正是已付的两个 universal 退化映射。
它没有把 incoming 点与 outward 点混为同一个模点。

恒等式
$\mathcal J_{i,C}-\mathcal J_i
 =(p^2-1)\mathcal J_i-p^2\mathcal J^{\rm out}_{i,C}$
代入(A26)。若该完整读者采用 R1054(49)的 exact-wild 权，
则在每个基点的完整 local orbit 中，
$\sum_C\lambda_{i,C}(-2)=0$，同时同一 full-avatar 证明给
$\mathcal O=0$。
于是获得与同一个 flat 读者相等的真正 finite outward 式：
$$
 \boxed{\;
 \sum_{i,C}\Lambda_{i,C}(-2)I^Q_{i,C}
   =-p^{-4}\sum_{i,C}
        \frac{\lambda_{i,C}(-2)e_i}{m_i\Omega_i}
                       \mathcal J^{\rm out}_{i,C}.
 \;}
 \tag{A28}
$$
(49)原有的 $1/[p(p+1)]$ 及每个字符仍在 $\lambda$ 中，
没有在(A28)再除一次。
若另添依赖 $C$ 的外权，使上述完整 wild 正交不再成立，
就使用(A26)--(A27)的全式，而非继续删掉 $\mathcal J_i$。

这是先由 actual positive source、同一 Amice 极限及 local GM
建立的**整个有限读数**身份。
它不要求逐个 $Q$ 根点就是同一个 CM 商点，
也没有用局部 Hom 一维性替换原全有限来源。

### 8.5. 全 tame、Artin 和两组实际图的范围

$p$ 与原 $2,3,17$ 素，故对所有实际 $\varphi_i$，
每个 $C\subset E_i[p^2]$ 唯一对应 $D\subset A[p^2]$，
且规范商方块严格交换：
$q_{i,C}\varphi_i=\varphi_{i,D}q_D$。
全部 full2/full9 基及微分同时运输。
几何 Galois 只重标 $(i,C)$；外系数保原约定，不被私自共轭。
因此(A24)--(A28)可逐项施全部原 Artin、Cor、
有限 tame projectors 及其规定次序。

对目前 $\psi_4^2$ 输入，$i$ 包含原十八个 cyclic17 核、
两个真实 full2 sign 取向及全几何 Galois 标号；
$m_i=17$，原 $Q_\tau/e_A^-$ 先作、sign 后作。
$1/2$ 取向差和 $1/6$ Artin projector仍只出现原来的那一次，
即原整个 $1/12$ 和。实际形式仍是
$f_{\Omega_4}=-\delta f_4(\tau/6)$，
primitive 同比例，不能把这个源改成 $f_4(q)$后沿用(A26)的数。

若对旧 $\psi_{27}^2$ 来源使用同样局部论证，则必须从其原
$f_{\Omega_S}=-\delta f_{27}(\tau/3)$、
degree34、全部54图、原 $Ph$ 和 $1/18$ Artin 权重新保留
这同一输入。两组模形式、图和投影不同；这里不建立它们之间
的新 cycle 或 canonical 等式。

(A26)支付值端的完整旧项，
(A28)支付 exact-$p^2$ 的 actual outward 图读者。
权导数仍严格是(A16)：含
$(I_C^{\rm AI})'(-2)$、$2\log\langle u_C\rangle$、
$\lambda_C'$、$\mathfrak j_C'$ 以及全部 Maass correction。
有限图的值恒等式不允许将这些导数项改为同一固定 AJ 数。
将这个新 ramified 值或导数再回到原 fixed rank2 canonical
$J'$，仍须给出同一来源的实际补偿关系。

本节的原文与已付依据：

- AI2024，Propositions7.6--7.8（印页700--705）的局部
  negative-iterate/CM 计算、Appendix A 的 $V_H=\phi^*/p$；
  [出版全文](https://ems.press/content/serial-article-files/48931)。
- R997§§3--6：原杯积、正号KS、完整 Coleman 多项式规范
  和实际微分倍率；其 ordinary 图定理的范围保持原样。
- R1054§§2、6、9：同一 full9 中心、actual positive 比较、
  全 $p^4$ 字与 full-avatar wild 权。
- [新 psi4 曲面与图](../notes/2026-11-27-original-psi4-sign-surface-fulllevel-graphs-and-fp.md)
  §§5--8；[同一 psi4 图的 proper 比较](../notes/2026-11-27-original-psi4-full-graphs-artin-and-geometric-newton-cross.md)
  §§4--5。只消费这两篇已付的 actual proper/有限对应部分，
  不消费后者待付的 usual/flat 或 canonical cross。
