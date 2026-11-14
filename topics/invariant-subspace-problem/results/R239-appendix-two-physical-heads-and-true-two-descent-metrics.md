# R239 附录：两物理头的无小枢轴消元与真正两下降度量

日期：2026-11-14（UTC）。作者：Astra-ISP-0c017065 / boundary_nonprimitive_1856；AI-assisted，GPT-6 Astra Pro。

状态：本文继续原首头商的真实行图度量，把下一步准确改写成尾算子 $D^2$ 的原像问题。只使用原 $Ae_1=e_0$，不除以第二个微小相邻头系数。原左负 Schur、完整右 Q 块及裸右 Q 块都保留真实变分域；三者分别与明确的两下降参照图费相差同一个有界因子 $1+\|D\|^2+\|b\|^2$。该二次型比较不被误用于非交换的平坦源运输。尚缺这些实际两下降余问题上的完整左／两右费上界；普通 ISP 与 $N=M$ 仍 OPEN。

依赖：[原首头商及同未来带](R239-appendix-first-head-quotient-and-actual-row-graph-metrics.md)、[原首头共同右度量](R239-appendix-first-source-head-metric-splitting-and-middle-band-schur-amplification.md)。所有下式均在同一个原 regular $A=A_m$、$D=D_m$、物理内积和合法窗中。

## 1. 两个首物理头与一个真实二阶行

把原前三块写成
$$
A=
\begin{pmatrix}
0&1&b\\
0&0&c\\
0&0&A_2
\end{pmatrix}
\quad\text{于 }\mathbb Ce_0\oplus\mathbb Ce_1\oplus H_2,
\qquad H_2=\operatorname{span}(e_2,\ldots,e_{d-1}).
\tag{1.1}
$$
$b,c$ 保留原整行的所有长跳。定义
$$
\boxed{g=c+bA_2=(A^2)_{0,H_2}.}
\tag{1.2}
$$
不把 $g$ 简化成一个相邻项。例如原低四头中的 $c e_2=\eta_0$ 虽很小，但 (1.2) 在 $e_3$ 上还含两个真实长跳的和；下文从不使用 $\eta_0^{-1}$。

沿首头商稿，原 $Q$ 源写为 $x=(x_1,x_2)$，其中
$$
x_1\in E_{d-2,q},\qquad
x_2\in\mathscr R_{2,q}
=\bigoplus_{i=2}^{d-2}e_iE_{d-i-1,q}.
\tag{1.3}
$$
其左负 Schur 为 $S^-$，完整右 Gram 块为 $G_1$，裸右逆 Gram 块为 $B_1$。记 $\nu=\|D\|$。

对 $p\ge0$ 写
$$
D_p=D:\mathcal H_{p+1}\to\mathcal H_p.
$$
对 $p\ge1$，本文的两下降算子准确为
$$
T_p=D_{p-1}D_p:\mathcal H_{p+1}\to\mathcal H_{p-1}.
\tag{1.4}
$$
$T_p^\dagger$ 是这个真幂映射的真正 MP 逆，不是 $D_p^\dagger D_{p-1}^\dagger$。固定孔层的满射性保证它有界。

## 2. 左负 Schur 的精确两头消元

给定余头轨道
$$
h=(h_0,\ldots,h_q)\in V_{A_2,q},
\qquad A_2h_q=x_2,\qquad ch_q=x_1,
\tag{2.1}
$$
令商的第一个头为 $z_p\in\mathcal H_p$。首头商的真实权能量为
$$
\sum_{p=0}^q
\left[\|h_p\|^2+\|z_p\|^2+
\|R_p(z_p+bh_p)\|^2\right],
\qquad D_{p-1}z_p=-ch_{p-1}\quad(1\le p\le q).
\tag{2.2}
$$
原最小首头补全为 $u_p=-R_p(z_p+bh_p)$，位于孔层 $p+1$。于是
$$
z_p=-D_pu_p-bh_p.
\tag{2.3}
$$
再用余头方程 $D_{p-1}h_p=-A_2h_{p-1}$，得到
$$
D_{p-1}z_p=-T_pu_p+bA_2h_{p-1},
$$
所以第二头方程恰为
$$
\boxed{T_pu_p=gh_{p-1}\quad(1\le p\le q).}
\tag{2.4}
$$
孔 $p=0$ 没有这一约束。

反向，从任意满足 (2.4) 的 $u_p$ 按 (2.3) 定义 $z_p$，原方程成立。若 $u_p$ 含 $\ker D_p$ 分量，删去该分量不改变 $z_p$ 或 (2.4)，并严格减少物理能量；故真实最小值自动选 $u_p\perp\ker D_p$。这正是原 MP 首头补全，不另加未经支付的条件。

旗也自动保持：$gh_{p-1}\in E_{d-2,p-1}$，所以 (2.4) 迫 $u_p\in E_{d,p+1}$；继而 $z_p\in E_{d-1,p}$。当 $p=0$，下述无约束最小者属于 $\operatorname{Ran}D_0^*$，且孔数本身保证所有短旗合法。

因此有精确变分式
$$
\boxed{
\langle S^-x,x\rangle
=\min_{h\ {
m 满足}\ (2.1)}
\sum_{p=0}^q\left[\|h_p\|^2+
\min_{\substack{T_pu_p=gh_{p-1}\ (p\ge1)}}
\bigl(\|u_p\|^2+\|D_pu_p+bh_p\|^2\bigr)\right].
}
\tag{2.5}
$$
内层在 $p=0$ 对全部 $u_0\in\mathcal H_1$ 最小化。固定参数下目标强制、约束闭，最小值均取得。式 (2.5) 没有用任何头逆。

## 3. 精确局部正 resolvent 与有界比较

任取 $D_p$、$w\in\mathcal H_p$，定义
$$
E_p=(I+D_pD_p^*)^{-1},\qquad
k_p=D_p^*E_pw,\qquad Q_p=(I+D_p^*D_p)^{-1}.
$$
直接展开并使用 $(I+D_p^*D_p)D_p^*=D_p^*(I+D_pD_p^*)$，得
$$
\boxed{
\|u\|^2+\|D_pu+w\|^2
=\langle E_pw,w\rangle+
\|Q_p^{-1/2}(u+k_p)\|^2.
}
\tag{3.1}
$$
若 $T_pu=f$，准确极小值为
$$
\boxed{
\langle E_pw,w\rangle+
\left\langle
(T_pQ_pT_p^*)^{-1}(f+T_pk_p),\,
f+T_pk_p\right\rangle.
}
\tag{3.2}
$$
这里 $f+T_pk_p$ 保留全部平移，不把两项分开估计后再假定有相消。

有界正因子给
$$
\frac1{1+\nu^2}T_pT_p^*
\preceq T_pQ_pT_p^*\preceq T_pT_p^*.
\tag{3.3}
$$
但更方便的比较不需要 (3.2) 中的交叉项：若 $\zeta=T_p^\dagger f$，则每个可行 $u$ 有 $\|u\|\ge\|\zeta\|$；上界直接取同一个可行 $u=\zeta$。因此，对任意有限段族 $f_p,h_p$，
$$
\begin{aligned}
\sum_p(\|h_p\|^2+\|\zeta_p\|^2)
&\le \sum_p\left[\|h_p\|^2+
\min_{T_pu_p=f_p}\bigl(\|u_p\|^2+\|D_pu_p+bh_p\|^2\bigr)\right]\\
&\le (1+\nu^2+\|b\|^2)
\sum_p(\|h_p\|^2+\|\zeta_p\|^2).
\end{aligned}
\tag{3.4}
$$
最后一步是
$\sum_p\|D_p\zeta_p+bh_p\|^2
\le(\nu^2+\|b\|^2)\sum_p(\|\zeta_p\|^2+\|h_p\|^2)$。
无约束段取 $\zeta_0=0$，同一上下界仍成立。

据此定义真正两下降左参照型
$$
\ell_2(x)
=\min_{h\ {
m 满足}\ (2.1)}
\left[\sum_{p=0}^q\|h_p\|^2+
\sum_{p=1}^q\|T_p^\dagger gh_{p-1}\|^2\right].
\tag{3.5}
$$
则
$$
\boxed{\ell_2(x)\le\langle S^-x,x\rangle
\le C_b\ell_2(x),\qquad C_b=1+\nu^2+\|b\|^2.}
\tag{3.6}
$$
这个常数不含孔数 $q$、$\eta_0^{-1}$ 或完整 $A^{-1}$。例如仅使用既有 $\|A_m\|\le6$、$\nu\le1$，就有 $C_b\le38$；保实际行范数时更小。

## 4. 完整右 Q 块的相同两下降结构

令 $h=(h_1,\ldots,h_{d-2})$ 是余头 $A_2$ 的完整右链，首源为 $x_2$：
$$
D_qh_1=x_2,\qquad
A_2h_j+D_{q+j}h_{j+1}=0,
$$
并保原第 $j$ 段头 $2\le i\le d-j$、尾旗 $E_{d-i,q+j}$。置 $h_{d-1}=0$。

把原第 $j$ 段第一个剩余头记为 $z_j$，下一段第零头记为 $u_j$。因原首源为 $(0,x)$，第一段第零头的最小值为零。其余第一行方程准确给
$$
z_j=-D_{q+j}u_j-bh_j\qquad(1\le j\le d-1).
\tag{4.1}
$$
第一个剩余源条件 $D_qz_1=x_1$ 于是成为
$$
\boxed{T_{q+1}u_1=-x_1-bx_2.}
\tag{4.2}
$$
所有后续方程给
$$
\boxed{T_{q+j}u_j=gh_{j-1}\quad(2\le j\le d-1).}
\tag{4.3}
$$
这里 $T_{q+j}=D_{q+j-1}D_{q+j}$ 的输入孔层为 $q+j+1$；没有错开首源。

反向由 (4.1)–(4.3) 重建，得到原完整合法链。因为每个右端属于 $E_{d-2,q+j-1}$，$u_j\in E_{d,q+j+1}$、$z_j\in E_{d-1,q+j}$；最末段只有第零头，自动封口。最小者的 $u_j$ primitive 分量仍为零。

故完整右费准确为
$$
\boxed{
\langle G_1^{-1}x,x\rangle
=\min_h\sum_{j=1}^{d-1}
\left[\|h_j\|^2+
\min_{u_j\ {
m 满足}\ (4.2),(4.3)}
\bigl(\|u_j\|^2+\|D_{q+j}u_j+bh_j\|^2\bigr)\right].
}
\tag{4.4}
$$
定义参照首项和后续项
$$
\zeta_1=T_{q+1}^\dagger(-x_1-bx_2),\qquad
\zeta_j=T_{q+j}^\dagger gh_{j-1}\quad(j\ge2),
$$
$$
k_2(x)=\min_{h\ {
m 余头完整链，源}\ x_2}
\sum_{j=1}^{d-1}(\|h_j\|^2+\|\zeta_j\|^2).
\tag{4.5}
$$
同一个 (3.4) 给
$$
\boxed{k_2(x)\le\langle G_1^{-1}x,x\rangle\le C_b k_2(x).}
\tag{4.6}
$$

## 5. 裸右 Q 块的真实幂逆及投影

现在令 $h$ 为同一余头的裸低链。第 $j$ 段仍在上述最大旗中，另满足
$h_j\perp E_{j-1,q+j}$；内部方程残差属于 $E_{j-1,q+j}$。仍置 $h_{d-1}=0$。

原下一段第零头 $u_j$ 必须满足
$$
u_j\in E_{d,q+j+1}\cap E_{j,q+j+1}^\perp.
\tag{5.1}
$$
第一个剩余头 $z_j$ 在第 $j$ 段的低旗中，所以第一行的低输出方程准确给
$$
\boxed{
z_j=-(I-P_{j-1,q+j})D_{q+j}u_j-bh_j.
}
\tag{5.2}
$$
首段 $j=1$ 没有该输出投影，故仍须
$$
T_{q+1}u_1=-x_1-bx_2,\qquad u_1\perp E_{1,q+2}.
\tag{5.3}
$$
这保留 $\ker T_{q+1}\cap E_1^\perp$ 中的真实自由量，不能提前固定为 $T_{q+1}^\dagger$。

对 $j\ge2$，第一个剩余头的上一行低方程与余头裸方程给
$$
T_{q+j}u_j-gh_{j-1}\in E_{j-2,q+j-1}.
\tag{5.4}
$$
说明：把 (5.2) 代入后，被截掉的项
$D_{q+j-1}P_{j-1,q+j}D_{q+j}u_j$
属于 $E_{j-2}$；余头方程的残差也在同一个 $E_{j-2}$。剩下的真实头行正是 $g=c+bA_2$。

(5.1)、(5.4) 具有唯一解
$$
\boxed{
u_j=(D^j:\mathcal H_{q+j+1}\to\mathcal H_{q+1})^\dagger
D^{j-2}gh_{j-1}\quad(2\le j\le d-1).
}
\tag{5.5}
$$
因为 (5.4) 等价于 $D^ju_j=D^{j-2}gh_{j-1}$，而 (5.1) 恰要求 $u_j\perp\ker D^j$。右端在 $E_{d-j,q+1}$，因此再乘 $D^{d-j}$ 还给 $u_j\in E_d$。这是幂的真正 MP 逆和完整合法旗，不是顺次逆。

由此得到精确裸变分式
$$
\boxed{
\langle B_1x,x\rangle
=\min_{\substack{h\ {
m 余头裸链，源}\ x_2\\u_1\ {
m 满足}\ (5.3)}}
\sum_{j=1}^{d-1}
\left[\|h_j\|^2+\|u_j\|^2+
\|(I-P_{j-1,q+j})D_{q+j}u_j+bh_j\|^2\right],
}
\tag{5.6}
$$
其中 $j\ge2$ 的 $u_j$ 固定由 (5.5) 给出。反向重建 (5.2) 即可逐行核查所有裸方程，因此没有省略可行链。

定义两下降裸参照型 $b_2(x)$：在 (5.6) 中，把 $u_1$ 取为
$T_{q+1}^\dagger(-x_1-bx_2)$，其余仍取 (5.5)，删除最后一个非负平方，再对合法 $h$ 最小化。则
$$
\boxed{b_2(x)\le\langle B_1x,x\rangle\le C_b b_2(x).}
\tag{5.7}
$$
下界使用 $\|u_1\|\ge\|T_{q+1}^\dagger(-x_1-bx_2)\|$；上界在同一个合法 $h$ 上取该 $u_1$，并用 (3.4) 中同一范数估计。投影只减小 $D u_j$ 的范数，故因子没有增加。

## 6. 真正两下降参照图中的返回差

对同一个合法 $h_{j-1}$，令
$\zeta_j=T_{q+j}^\dagger gh_{j-1}$。当 $j\ge2$，(5.5) 还准确写成
$$
\boxed{u_j=(I-P_{j,q+j+1})\zeta_j.}
\tag{6.1}
$$
因为两边都正交于 $\ker D^j$，经 $D^j$ 映到同一个 $D^{j-2}gh_{j-1}$。因此参照图中的损失恰为
$$
\boxed{\|\zeta_j\|^2-\|u_j\|^2
=\|P_{j,q+j+1}\zeta_j\|^2.}
\tag{6.2}
$$
对 $j=2$，$\zeta_2\perp\ker D^2$，所以参照图这一项没有差；其真正高返回从 $j\ge3$ 开始。

这个说法只针对参照图的同一个候选余头轨道。真实完整最优 $u_j$ 仍可加入 $\ker D^2$ 来优化 (4.4) 的最后平方；真实裸式则含 (5.2) 的输出投影。二者并不因 (6.2) 而相同，更不能把两个最小值之差换成 (6.2) 的最小值。原真实高返回全部保留在 (4.4)、(5.6) 中。

## 7. 与原三费用的接口及不能免费作的运输

对同一个原负源 $r=(r_0,x)$，首头商稿仍给
$$
\mu_A(r)^2=\langle S^-x,x\rangle-\kappa,
$$
$$
\chi_A(r)^2
=2\kappa+\langle B_1x,x\rangle+
\langle G_1S^-x,S^-x\rangle,
\qquad \kappa=\|R_qr_0\|^2.
\tag{7.1}
$$
本文的 (2.5)、(4.4)、(5.6) 是这三个原算子的准确物理表示。
(3.6)、(4.6)、(5.7) 则在同一个固定源 $x$ 上给出明确、有界的二次型比较。若把参照型表示为算子 $L_2,K_2,B_2$，有
$$
L_2\preceq S^-\preceq C_bL_2,\qquad
K_2\preceq G_1^{-1}\preceq C_bK_2,\qquad
B_2\preceq B_1\preceq C_bB_2.
\tag{7.2}
$$
这些 Loewner 比较不允许把原平坦费用
$\langle G_1S^-x,S^-x\rangle$
直接换成 $\langle K_2^{-1}L_2x,L_2x\rangle$；$S^-$ 与 $L_2$ 一般不交换，并且实际共同费用规范图也须用原算子定义。

接下来的准确问题是：利用实际二阶行 $g=(A^2)_{0,H_2}$、原余头轨道和 (5.5) 的真幂逆，控制 (7.1) 中的左量。本文已经把一次继续消元中的巨大 $R_p$ 行权，换成同一实际两下降原像及一个不含微小头枢轴的常数；没有声称两下降原像本身已在一般非 primitive 来源上廉价。
