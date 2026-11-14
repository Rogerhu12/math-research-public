# R239 附录：同未来带支付的两源头负图与连续两下降 Schur

日期：2026-11-14（UTC）。作者：Astra-ISP-0c017065 / boundary_nonprimitive_1856；AI-assisted，GPT-6 Astra Pro。

状态：本文把全尾首两源头的 $\lambda/\alpha$ 界用于实际来源，得到代价仅为 $\|D\|$ 倍同一未来带的两头负图校正。这一结论不要求两个右 Gram 约化物理第二头。校正后可对 $L+B$ 真正消去前两源头，全部裸交叉项仍保留；对应两下降变分式的首右源准确接上同一个实际二阶行。未证明最终余费用上界，普通 ISP 与无权 $N=M$ 仍 OPEN。

依赖：[全尾首两头完整右界](R239-appendix-full-tail-low-head-source-strip-and-bare-to-complete-right-bound.md)、[同未来带双投影](R239-appendix-future-band-projection-angle-and-complete-common-cost-negative-graph.md)、[正 resolvent 校正](R239-appendix-positive-resolvent-negative-source-defect-correction.md)、[真实两下降度量](R239-appendix-two-physical-heads-and-true-two-descent-metrics.md)。

## 1. 任意近共同右费用子空间的实际缺陷界

在同一原源空间上记
$$
L=J_{\rm left}^{-1},\qquad B=J_b^{-1},\qquad G=F_fF_f^*,
\qquad B\preceq G^{-1}.
$$
令闭子空间 $X$ 满足
$$
\lambda(s)\le c_X\alpha(s)\quad(s\in X),\qquad c_X\ge1.
\tag{1.1}
$$
裸度量归一为
$$
u=B^{1/2}r,\quad H=B^{-1/2}LB^{-1/2},\quad
C=B^{1/2}GB^{1/2}\preceq I,\quad
W_X=B^{1/2}X.
$$
因为 $B^{1/2}$ 有界可逆，$W_X$ 闭。(1.1) 恰给
$$
\langle(C^{-1}-I)w,w\rangle
\le(c_X^2-1)\|w\|^2\quad(w\in W_X).
\tag{1.2}
$$
不要求 $W_X$ 约化 $C$，更不要求 $X$ 约化 $B,G$。

若 $r$ 来自真正顶部最小者的前缀，且完整未来带 $y$ 处于顶部支持内，同未来带定理给
$$
(I-C)^{1/2}z=C^{1/2}(I+H)u,
\qquad \|u\|^2+\|z\|^2\le\|y\|^2.
$$
固定参数下 $C$ 有界严格正。因此
$$
(I+H)u=(C^{-1}-I)^{1/2}z.
$$
取 $W_X$ 上的投影，并对 (1.2) 的受限算子取伴随，准确得到
$$
\boxed{
d_X:=P_{W_X}(I+H)u,
\qquad
\|d_X\|\le\sqrt{c_X^2-1}\,\|z\|
\le\sqrt{c_X^2-1}\,\|y\|.
}
\tag{1.3}
$$
这是真实子空间上的压缩逆角估计，不是将 $W_X$ 当作 $C$ 的谱子空间。

同一关系还给原两费的直接界：
$$
C^{1/2}Hu=(I-C)^{1/2}z-C^{1/2}u.
$$
行算子 $[-C^{1/2},(I-C)^{1/2}]$ 的范数为一，因而
$$
\chi(r)^2=\|u\|^2+\|C^{1/2}Hu\|^2
\le2(\|u\|^2+\|z\|^2)\le2\|y\|^2.
\tag{1.4}
$$
下文的累计原两费预算直接由此式和同一未来带的重叠计数得到。


## 2. 全正 resolvent 校正与原源条件

令
$$
t_X=B^{-1/2}(I+H)^{-1}d_X,
\qquad r_X=r-t_X.
$$
则
$$
\boxed{P_{W_X}(I+H)B^{1/2}r_X=0,}
\tag{2.1}
$$
等价地，
$$
\boxed{\langle(L+B)r_X,s\rangle=0\quad(s\in X).}
\tag{2.2}
$$
同一个正算子计算给
$$
\boxed{
\chi(t_X)^2+2\mu(t_X)^2\le\|d_X\|^2,
\qquad \mu(t_X)\le\tfrac12\|d_X\|.
}
\tag{2.3}
$$
因为 $C\preceq I$，左式在裸归一中至多为
$\langle(I+H)^2(I+H)^{-1}d_X,(I+H)^{-1}d_X\rangle$。
第二式是 $H(I+H)^{-2}\preceq I/4$。

若一个旧负图的测试子空间包含在 $X$ 中，(2.2) 自动保留该负图条件。这里仍不提供普通完整右费 $\lambda(t_X)$ 的上界。

## 3. 原全尾首两头只损失 ν 倍未来带

令
$$
X_2=e_0E_{d-1,q}\oplus e_1E_{d-2,q},\qquad \nu=\|D_m\|\le1/m.
$$
全尾低头稿已证明
$$
\lambda(s)\le\sqrt{1+\nu^2}\,\alpha(s)\quad(s\in X_2).
$$
因此 (1.3) 的缺陷系数恰为 $\nu$，不是一个增长头条件数。令 $r_2=r-t_2$ 为上面的校正，则
$$
\boxed{
\langle(L+B)r_2,s\rangle=0\quad(s\in X_2),
}
\tag{3.1}
$$
$$
\boxed{
\chi(t_2)^2+2\mu(t_2)^2\le\nu^2\|y\|^2,
\qquad \mu(t_2)\le\tfrac12\nu\|y\|.
}
\tag{3.2}
$$
原第一源头包含在 $X_2$，所以旧真实负源图保留。第二源头并未被声明约化 $B$ 或 $G$。

对同一个原顶部的全部合法窗口，用 $y_q$ 表示各自未来带。若
$$
\sum_q\|y_q\|^2\le d\beta_m^2\|w\|^2,\qquad
\sup_q\|y_q\|\le\beta_m\|w\|,\qquad \beta_m\to0,
$$
并且原左向量满足 $\sup_q\|E_q^\dagger r_q-w\|\le\beta_m\|w\|$，则无需删除任何窗口，便有
$$
\boxed{
\sum_q\chi(r_{2,q})^2
\le(\sqrt2+\nu)^2d\beta_m^2\|w\|^2,
}
\tag{3.3}
$$
$$
\boxed{
\sup_q\|E_q^\dagger r_{2,q}-w\|
\le(1+\nu/2)\beta_m\|w\|.
}
\tag{3.4}
$$
累计平方费用除以 $d$ 后仍趋零；不声称未归一的总和必趋零。新族满足 (3.1)，不被免费当作同一个逐孔源流。

## 4. 两头负图上的真 L+B Schur：保留所有裸交叉

令 $P_2$ 为到物理源子空间 $X_2$ 的正交投影，$Q_2=I-P_2$。写
$$
\mathcal D=L+B
=\begin{pmatrix}\mathcal D_{22}&\mathcal D_{2R}\\
\mathcal D_{R2}&\mathcal D_{RR}\end{pmatrix}.
$$
对满足 (3.1) 的 $r_2=(x,y)$，准确有
$$
x=-\mathcal D_{22}^{-1}\mathcal D_{2R}y,
\qquad
R_2y=(x,y).
$$
定义
$$
\mathcal S_2=\mathcal D_{RR}
-\mathcal D_{R2}\mathcal D_{22}^{-1}\mathcal D_{2R},
\qquad B_2^{\rm eff}=R_2^*BR_2.
$$
于是
$$
\boxed{
\mu(r_2)^2+\alpha(r_2)^2=\langle\mathcal S_2y,y\rangle,
\qquad
\mu(r_2)^2=\langle(\mathcal S_2-B_2^{\rm eff})y,y\rangle.
}
\tag{4.1}
$$
更强的原向量身份是
$$
\boxed{Lr_2=\iota_R\mathcal S_2y-BR_2y.}
\tag{4.2}
$$
故原两费用准确为
$$
\boxed{
\chi(r_2)^2=\langle B_2^{\rm eff}y,y\rangle+
\|G^{1/2}(\iota_R\mathcal S_2y-BR_2y)\|^2.
}
\tag{4.3}
$$
这里的 $BR_2y$ 必须整个保留，不能只取某个物理头块，也不能删除它与第一项向量的交叉相消。

## 5. 原二阶行准确接通左轨与裸右轨

现在使用两下降稿的原物理头分解
$$
A=\begin{pmatrix}0&1&b\\0&0&c\\0&0&A_2\end{pmatrix},
\qquad g=c+bA_2.
$$
为了不与 §4 的 $B_2^{\rm eff}$ 混淆，仍以 $B_1$ 表示原裸度量在第一源头正交补上的块；$S^-$ 为消掉第一源头后既有左负 Schur。

原第一源头约化 $B$，所以先消它，再消第二源头的 Schur 结合律给
$$
\boxed{
\langle\mathcal S_2y,y\rangle
=\min_{x_1\in E_{d-2,q}}
\left[\langle S^-(x_1,y),(x_1,y)\rangle+
\langle B_1(x_1,y),(x_1,y)\rangle\right].
}
\tag{5.1}
$$
这一步使用 $S^-+B_1$，不是将第二个裸块误换成完整右块。

左变分的余头轨 $h^-\in V_{A_2,q}$ 满足
$$
A_2h^-_q=y,\qquad ch^-_q=x_1.
\tag{5.2}
$$
其两头变量满足 $D^2u^-_p=gh^-_{p-1}$，并按原两下降式支付
$\|u^-_p\|^2+\|Du^-_p+bh^-_p\|^2$。

裸右余头轨 $h^+$ 的首源为 $y$；其首个两下降变量原来满足
$$
D^2u^+_1=-x_1-by.
$$
把 (5.2) 代入，首源准确变为
$$
\boxed{D^2u^+_1=-gh^-_q.}
\tag{5.3}
$$
以后各段保持原式
$$
D^2u^+_j-gh^+_{j-1}\in\ker D^{j-2},\qquad
u^+_j\perp\ker D^j\quad(j\ge2),
\tag{5.4}
$$
且首段仍保留 $u^+_1\perp\ker D$ 内的 $\ker D^2$ 自由量。所有物理尾核上界、输出投影和原能量均与两下降稿相同。

因此 (5.1) 可在 $h^-,h^+$ 及其两下降变量上联合最小化，并完全删除中间符号 $x_1$：约束只保 $A_2h^-_q=y$、裸右首源 $y$，以及 (5.3)–(5.4)。若把右侧轨道整体变号，它的首两下降方程与左侧准确接成同一个实际行 $g$ 的连续递推。

这里的“接通”是一个真正同边界变分身份，不是估计后猜测的相消。它保留右首两下降变量的自由量和所有裸输出投影，尚不把这些真实最小费用换成无权真幂参照费用。

## 6. 现在的具体余问题

原实际族可用 (3.2) 的小量校正进入两头负图，保全部合法窗、原强极限和归一累计两费用。余量的完整左费用及平坦费用由 (4.1)–(4.3) 给出，而其边界变分由 (5.1)–(5.4) 使用同一个 $g=(A^2)_{0,H_2}$。

尚未证明的是 $\mathcal S_2-B_2^{\rm eff}$ 在这一实际族上被 (4.3) 温和控制。第二头被真正消元，却没有消失为物理零坐标；其由全部 $L+B$ 交叉项决定的反馈仍完整保留。
