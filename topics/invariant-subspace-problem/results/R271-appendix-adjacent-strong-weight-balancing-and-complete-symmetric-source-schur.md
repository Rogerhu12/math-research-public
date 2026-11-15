# 相邻强尾位配平：固定对称测试的真投影比较与全部反对称通道的 Schur 预算

日期：2026-11-15（UTC）。作者：Astra-ISP-789f / literature_audit；AI-assisted，GPT-6 Astra Pro。

**状态：已证明。** 本文对原尾 $b_j=(j+1)^{-2}$ 的任意有限个相邻强位作精确对角相似，将每对两权换成其几何平均。完整相似的条件数可以随强位数增长，但在全部配对交换对称的输入上，真实核投影的变化不超过
$$
\epsilon_m=\sqrt{e^{2/m}-1}.
$$
此界独立于强位数、孔数、出生和原头维数。所有反对称通道都保留；其最小回返能量由同一个真实 Schur 补支付，至多为 $e^{2/m}-e^{-2/m}$ 倍的对称源能量。

这是一条针对固定测试及其真实变分问题的比较，不是对整个源空间的相似条件数估计。它没有直接比较原普通右费与 $LGL$，也没有证明 $N=M$。

依赖的物理源与窗口仅用于应用部分：
[原首物理头完整商 Gram](R239-appendix-first-physical-head-quotient-gram-for-left-plus-bare.md)、
[同一 top 的强尾扩块源流](R271-appendix-strong-tail-block-same-top-source-flow-and-exact-two-fee-budget.md)。
本文的比较引理及其常数在下文自足证明。

## 1. 一个保留完整 nuisance 的正变形引理

设 $\mathscr H$ 为 Hilbert 空间，$P$ 为正交投影，$S$ 为有界、正、自伴、可逆算子。假定有 $K\ge1$ 满足
$$
P S^{\pm2}P\preceq K P,\qquad
P S^{\pm1}P\succeq P.
\tag{1.1}
$$
从
$$
P(S^{\pm1}-I)^2P
=P S^{\pm2}P-2P S^{\pm1}P+P
\preceq(K-1)P
$$
得到
$$
\|(S-I)P\|,\ \|(S^{-1}-I)P\|\le\epsilon,\qquad
\epsilon=\sqrt{K-1}.
\tag{1.2}
$$

令 $\mathscr K\subseteq\mathscr H$ 是被 $P$ 约化的闭子空间。由于 $S$ 可逆，$S\mathscr K$ 仍闭。记
$$
\Pi=P_{\mathscr K},\qquad \widetilde\Pi=P_{S\mathscr K}.
$$
则
$$
\boxed{\|(\widetilde\Pi-\Pi)P\|\le\epsilon.}
\tag{1.3}
$$

证明如下。对 $f\in\operatorname{Ran}P$，按
$$
f=f_0+f_1,\qquad f_0=\Pi f,\quad f_1=(I-\Pi)f
$$
作正交分解。由于 $\mathscr K$ 约化 $P$，两个分量都在 $\operatorname{Ran}P$。

首先 $Sf_0\in S\mathscr K$，所以
$$
\|(I-\widetilde\Pi)f_0\|
\le\|f_0-Sf_0\|
\le\epsilon\|f_0\|.
\tag{1.4}
$$
其次 $f_1\perp\mathscr K$，且 $S^{-1}$ 自伴，因此
$$
\langle S^{-1}f_1,Sk\rangle=\langle f_1,k\rangle=0
\quad(k\in\mathscr K).
$$
故 $S^{-1}f_1\in(S\mathscr K)^\perp$，从而
$$
\|\widetilde\Pi f_1\|
\le\|f_1-S^{-1}f_1\|
\le\epsilon\|f_1\|.
\tag{1.5}
$$
在
$$
(\widetilde\Pi-\Pi)f
=-(I-\widetilde\Pi)f_0+\widetilde\Pi f_1
$$
中，两项分别属于 $(S\mathscr K)^\perp$ 和 $S\mathscr K$，确实正交。平方相加即得 (1.3)。证明没有在 $P^\perp$ 上估计 $S$ 或 $S^{-1}$。

对一般 $f$，正交投影之差的范数至多一，所以还可用
$$
\|(\widetilde\Pi-\Pi)f\|
\le\epsilon\|Pf\|+\|(I-P)f\|.
\tag{1.6}
$$

## 2. 完整 Schur 补及实际回返能量

继续采用 §1 的假设，写
$$
\mathscr K=\mathscr K_0\oplus\mathscr K_1,\qquad
\mathscr K_0=\mathscr K\cap\operatorname{Ran}P,\quad
\mathscr K_1=\mathscr K\cap\ker P.
$$
在这两个真实物理子空间的等距坐标中，令
$$
M=P_{\mathscr K}S^2|_{\mathscr K}
=\begin{pmatrix}M_{00}&M_{01}\\M_{10}&M_{11}\end{pmatrix}.
$$
$M_{11}$ 有正下界，故所有反对称自由量的完整最小化为
$$
E=M_{00}-M_{01}M_{11}^{-1}M_{10},
$$
$$
\langle Ex,x\rangle
=\min_{y\in\mathscr K_1}\|S(x+y)\|^2,\qquad
y_{\min}=-M_{11}^{-1}M_{10}x.
\tag{2.1}
$$
则
$$
\boxed{K^{-1}I_{\mathscr K_0}\preceq E\preceq K I_{\mathscr K_0}.}
\tag{2.2}
$$

上界取 $y=0$，再用 (1.1)。下界可直接以同一源的对偶向量证明：对 $x\in\mathscr K_0$ 及任何 $y\in\mathscr K_1$，
$$
\|x\|^2
=\langle x,x+y\rangle
=\langle S^{-1}x,S(x+y)\rangle,
$$
而 $\|S^{-1}x\|^2\le K\|x\|^2$。Cauchy–Schwarz 给
$$
\|S(x+y)\|^2\ge K^{-1}\|x\|^2.
$$
对全部 $y$ 取最小值得 (2.2)。特别，证明没有把允许的 nuisance 换成较小的零源类。

还得到真实非约化回返项的定量预算：
$$
0\preceq M_{01}M_{11}^{-1}M_{10}
=M_{00}-E
\preceq(K-K^{-1})I_{\mathscr K_0},
\tag{2.3}
$$
$$
\boxed{\|S y_{\min}\|^2
=\langle M_{01}M_{11}^{-1}M_{10}x,x\rangle
\le(K-K^{-1})\|x\|^2.}
\tag{2.4}
$$
这里 $S y_{\min}$ 是完整最小回返列，不能替换成未经 Schur 消元的单个坐标逆。

若 $\mathscr K_0$ 再由某个有界下方有界的真实源列 $T_0$ 参数化，$G_0=T_0^*T_0$，则同一合同给
$$
K^{-1}G_0\preceq T_0^*E T_0\preceq K G_0,
$$
而 (2.3) 右端变成 $(K-K^{-1})G_0$。在同一个可行仿射源集合上继续消去对称零源，双边常数仍为 $K^{\pm1}$：这是把上述逐向量不等式对同一个集合取下确界，不能换源。

## 3. 原相邻两权的精确配平

固定 $m\ge1$，原尾为
$$
D_m=\sum_{j\ge m}b_jE_j,\qquad b_j=(j+1)^{-2}.
$$
$E_j$ 是占据 $0/1$ 位上的删除：$E_j e_1=e_0$、$E_j e_0=0$。取前 $R$ 个尾位作为强块，$R$ 任意有限。把其中的位按
$$
(j,j+1)=(m+2\ell,m+2\ell+1),\qquad
0\le\ell<\lfloor R/2\rfloor
$$
配成相邻对。若 $R$ 奇，最后一个未配对位保持原权。

对一对置
$$
x=j+1,\quad r_x=\frac{x}{x+1},\quad
a_x=\frac1{x(x+1)},\quad
\theta_x=\log\frac{x+1}{x}.
$$
原两权为 $x^{-2}$、$(x+1)^{-2}$，其几何平均恰为 $a_x$。在原正交占据基
$$
(e_{00},e_{10},e_{01},e_{11})
$$
中定义
$$
S_x=\operatorname{diag}(1,r_x,r_x^{-1},1).
\tag{3.1}
$$
直接逐基向量检查可得
$$
S_x^{-1}\bigl(x^{-2}E_j+(x+1)^{-2}E_{j+1}\bigr)S_x
=a_x(E_j+E_{j+1}).
\tag{3.2}
$$

令 $U_x$ 交换这一对位，$P_x=(I+U_x)/2$。其对称像的正交基为
$$
e_{00},\quad (e_{10}+e_{01})/\sqrt2,\quad e_{11}.
$$
在这三个坐标上精确有
$$
P_x S_x^{\pm1}P_x
=\operatorname{diag}(1,\cosh\theta_x,1),
$$
$$
P_x S_x^{\pm2}P_x
=\operatorname{diag}(1,\cosh(2\theta_x),1).
\tag{3.3}
$$
反对称的一维通道没有删去；(3.3) 只是原正算子的压缩，后续使用 §2 的完整逆消元。

在全部头位、强位和远尾的原物理空间上置
$$
S_{m,R}=\bigotimes_{\ell<\lfloor R/2\rfloor}S_{m+2\ell+1},
\qquad
P_{m,R}=\prod_{\ell<\lfloor R/2\rfloor}P_{m+2\ell+1},
\tag{3.4}
$$
其余因子均取恒等。这里下标 $m+2\ell+1$ 表示该对的 $x=j+1$。有限个张量因子使 $S_{m,R}$ 有界正可逆；$P_{m,R}$ 是正交投影。

由 (3.3)，
$$
P_{m,R} S_{m,R}^{\pm1}P_{m,R}\succeq P_{m,R},
$$
$$
P_{m,R} S_{m,R}^{\pm2}P_{m,R}
\preceq K_{m,R}P_{m,R},
\quad
K_{m,R}=\prod_{\ell<\lfloor R/2\rfloor}
\cosh(2\theta_{m+2\ell+1}).
\tag{3.5}
$$

最后，$\log\cosh t\le t^2/2$ 可由
$(\log\cosh t)''=\operatorname{sech}^2t\le1$ 和零点处的函数值、导数均为零积分得到。再用 $\log(1+1/x)\le1/x$，
$$
\log K_{m,R}
\le2\sum_{\ell<\lfloor R/2\rfloor}(m+2\ell+1)^{-2}
\le2\sum_{j\ge m+1}j^{-2}
\le\frac2m.
\tag{3.6}
$$
因此全部 $R$ 一致地
$$
\boxed{
1\le K_{m,R}\le e^{2/m},\qquad
\epsilon_{m,R}:=\sqrt{K_{m,R}-1}\le\epsilon_m.
}
\tag{3.7}
$$
与整个 $S_{m,R}$ 的条件数不同，(3.7) 不随 $R$ 增大而变坏。

## 4. 同一真实算子、完整核与原孔截断

保留原有限头 $A_m$，不修改其 carry、物理基或任何头权。将 §3 中每对强位的权换成 $a_x$，得到 $\widetilde D_m$；未配对位及所有远尾权不变。记
$$
L_m=A_m+D_m,\qquad \widetilde L_m=A_m+\widetilde D_m.
$$
由 (3.2)，
$$
\boxed{L_m S_{m,R}=S_{m,R}\widetilde L_m.}
\tag{4.1}
$$
$S_{m,R}$ 只在强位对角作用，因而同时与原总孔投影、远尾孔投影以及全部物理头投影交换。

配平模型的每个强对交换 $U_x$ 与 $\widetilde L_m$、$\widetilde D_m$、总孔数和远尾孔数都对易。故由这些算子的核、孔截断、共同不变高出生空间及闭和构成的每个真实物理空间均约化 $P_{m,R}$。

特别，下列空间逐个满足精确的像关系 $\mathscr S=S_{m,R}\widetilde{\mathscr S}$：

1. 完整纯尾核 $\ker L_m$。
2. 原有限总孔核
   $$
   K_{m,Q}=\ker L_m\cap\mathcal H_{\le Q}.
   $$
3. 原左低方程空间
   $$
   V_{m,Q}
   =\{v\in\mathcal H_{\le Q}:P_{<Q}L_mv=0\}.
   $$
4. 只在远尾计孔的扩块左空间及真核：
   $$
   C=A_m+D_<,\qquad L_m=C+D_>,
   $$
   $$
   V_n^C
   =\{v\in\mathcal H_{\mathrm{far}\le n}:
                   P_{\mathrm{far}<n}L_mv=0\},
   \qquad
   K_n^C=\ker L_m\cap\mathcal H_{\mathrm{far}\le n}.
   \tag{4.2}
   $$
   每对都位于强块内，故其交换不改变远孔数。
5. 原 joined 物理空间 $M_q=K+\mathcal H_{\mathrm{hi},q}$，其中采用原完整核及原高出生空间的既有闭和定义。这里
   $$
   \mathcal H_{\mathrm{hi},q}
      =\bigoplus_{j=1}^{d}
           \bigl(\ker D_m^{j-1}\cap\mathcal H_{q+j}\bigr)
   $$
   连同原头因子或原输入头旗。逐幂相似把每个真实核旗映到配平核旗，故整个和的像关系成立；闭性也由有界可逆 $S_{m,R}$ 保持。

第 5 项并没有宣称原正交低出生投影与 $S_{m,R}$ 对易。它使用物理空间的准确像，再重新取真实正交投影。因此没有把「环境取商后取核」换成「真核取商」。

## 5. 真投影、同一 top 及固定测试的统一结论

对 §4 的任何一个空间记原正交投影为 $P_{\mathscr S}$，配平模型中的为 $P_{\widetilde{\mathscr S}}$。§1 直接给
$$
\boxed{
\|(P_{\mathscr S}-P_{\widetilde{\mathscr S}})P_{m,R}\|
\le\epsilon_{m,R}\le\sqrt{e^{2/m}-1}.
}
\tag{5.1}
$$
此式对全部 $R,Q,n,q$ 一致。特别适用于任何固定低物理头、强位真空及远尾真空测试；这些测试属于 $\operatorname{Ran}P_{m,R}$。

原最小 top 投影算子为
$$
U_{m,Q}=P_{V_{m,Q}}-P_{K_{m,Q}},
$$
因为 $K_{m,Q}\subseteq V_{m,Q}$。扩块版本同样置
$$
U_n^C=P_{V_n^C}-P_{K_n^C}.
$$
它们都是实际正交投影，不是单纯首头坐标截断。两次使用 (5.1) 得
$$
\boxed{
\|(U_{m,Q}-\widetilde U_{m,Q})P_{m,R}\|,
\ \|(U_n^C-\widetilde U_n^C)P_{m,R}\|
\le2\epsilon_m.
}
\tag{5.2}
$$
所以对同一个原测试 $f$，原 $u_Q=U_{m,Q}f$ 与配平问题中由同一 $f$ 得到的实际最小 top 满足 (5.2)。这里比较的是两条真实最小者，没有先挑选一条较小模型中的可行链来替代它们。

同理，任何已证明是嵌套投影之差的物理 gap，例如 $P_{M_q}-P_{K_{m,q+d}}$，在 $\operatorname{Ran}P_{m,R}$ 上的原/配平之差范数至多 $2\epsilon_m$。

对一般固定物理 $f$，每个单投影有更明确的界
$$
\|(P_{\mathscr S}-P_{\widetilde{\mathscr S}})f\|
\le\epsilon_m\|P_{m,R}f\|+\|(I-P_{m,R})f\|.
\tag{5.3}
$$
投影之差应用可把右侧两项各乘二。由于 $P_{m,R}$ 恒等作用于第 $m$ 位之后的真空扇区，
$$
\sup_{R<\infty}\|(I-P_{m,R})f\|\longrightarrow0
\quad(m\to\infty)
\tag{5.4}
$$
对每个固定 $f$ 成立：先以有限位物理向量逼近 $f$，再令 $m$ 越过其支撑；全部 $P_{m,R}$ 都是收缩。因此原与配平各类真实投影在固定测试上强接近，且对任意允许的移动孔窗口及强位数一致。

## 6. 保留所有反对称来源的源度量预算

在 §4 任一配平物理闭空间内，按全部交换对称扇区及其正交补分解。把对称物理源列保持不变，只对全部允许的反对称 nuisance 作真实最小化。§2 给其完整有效 Gram
$$
e^{-2/m}G_{\mathrm{sym}}
\preceq G_{\mathrm{eff}}
\preceq e^{2/m}G_{\mathrm{sym}}.
\tag{6.1}
$$
并有同源实际最小反对称回返能量
$$
\|S_{m,R}y_{\min}\|^2
\le\bigl(e^{2/m}-e^{-2/m}\bigr)
      \|x_{\mathrm{sym}}\|^2.
\tag{6.2}
$$
若还存在对称零源，须在同一个源集合上继续 shorting；(6.1) 的常数保持。此处 $G_{\mathrm{sym}}$ 是真正对称物理列的 Gram，不是把原完整 Gram 先压缩到一个猜测的小源再取逆。

这一比较不要求强位数小、原头次数小、源出生固定或原尾权条件数有界。所用小参数是所有相邻配对的平方对数差之和，(3.6) 已直接对原连续尾支付。

## 7. 已付范围与仍缺的比较

本稿支付了同一个固定物理测试的真投影变化、真实最小 top 的变化，以及完整反对称 nuisance 的正 Schur 费用。特别，强块中所有反对称 primitive 通道都保留到了最小化中。

它尚未把扩块源 $r_n^C$ 与某一个原总孔源 $r_p$ 认同：该源仍由原总孔 $n,\ldots,n+R$ 的联合分量组成。它也没有把 (5.2) 的小物理误差乘上未经估计的 $G_1$、普通右最小逆或 $L$。

尤其，(6.1) 这样的源 Gram 双边比较不能直接交换 $LGL$ 中的非交换因子。因此本文不声称原两费比较已自动传到配平模型，更不声称只需考察无反对称自由量的普通右链。下一步仍须在同一实际源与完整 Schur 中支付扩块所需的 bare/flat 或普通右费用。一般 Hilbert ISP 与原 $N=M$ 仍开放。
