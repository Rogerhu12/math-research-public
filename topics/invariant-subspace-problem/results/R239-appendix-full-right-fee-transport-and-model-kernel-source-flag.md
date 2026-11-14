# R239 附录：普通完整右费双向运输与模型全核源原像旗

日期：2026-11-13（UTC）。作者：Astra-ISP-0c017065 / boundary_nonprimitive_1856；AI-assisted，GPT-6 Astra Pro。

状态：本文以完整右零源核的全部 primitive 参数，证明同一个原源及其天然四块模型源的普通完整右费双向运输，不增加头条件数。对于模型源落在其全部核头的原像旗，原普通右费与裸费仅差指数小左费；于是该原像旗的两费用可付一个趋于 $1/2$ 的常数。没有证明整个源空间或模型完整负图实际族的两费用比较；普通 ISP 与 $N=M$ 仍为 OPEN。

## 1. 同一个原坐标与两个天然源

沿四块比较及天然旗运输稿，固定
$$
m\ge8,\quad d=2^m,\quad h=d/4,\quad 4d\le q\le e^{d^3/4}.
$$
原头 $A=A_m$，模型 $T=A_\square$，尾始终是原 $D_m$，右域始终是同一个物理宽度 $d$ 联合旗。模型右域只将首源限制到其天然闭源空间，并不删除任何右零源核或高出生自由部分。

给定原 $r$，令
$$
a=\Gamma r,\qquad r=\mathcal B_Aa,\qquad
g=\mathcal B_Ta,\qquad \|a\|\le\mu_A(r).
\tag{1.1}
$$
$g$ 正是此前天然左 Schur 后的模型源，因为该 Schur 只改变 $\ker\mathcal B_T$。

记 $C_A=P_{>q}\mathcal E_A^{\rm full}$，$C_T$ 同理。右规范链分别为 $-C_Aa$、$-C_Ta$。此前已经给
$$
\|C_A-C_T\|\le\rho,
\qquad
\rho=216\eta_{m-3}(2048q^2)^3dh(h+1)^2e^{11d^4/40}
\le e^{-d^4/20}.
\tag{1.2}
$$
平坦运输稿还核实：将 primitive 输入孔数上界扩大到 $q+d$，仍使用同一个 $\rho$，因为
$$
512\sqrt{q+3d-1}(m+q+3d-1)^{3/2}
\le512\sqrt{14}\,q^2<2048q^2.
\tag{1.3}
$$
没有把 $q+d$ 当作新的合法上窗参数。

## 2. 完整右零源核的全部参数和合法旗

对严格降头 $H=A$ 或 $T$，任意右零源核 $z$ 的 primitive 参数在第 $q+j$ 层满足
$$
\xi_j\in\mathscr H_{\le d-j}\otimes K_{q+j},
\qquad 1\le j\le d.
\tag{2.1}
$$
完整 Taylor 递推给
$$
z=Z_H^+\xi
=\sum_{j=1}^{d}\sum_{k\ge0}(-H)^kQ_k\xi_j.
\tag{2.2}
$$
第 $j$ 层输入的 $k$ 次提升只在右段 $j+k$，头不超过 $d-j-k$，尾核阶不超过 $k+1\le j+k$。它自动在 $j+k>d$ 时为零，故 (2.2) 保留原全部短尾核阶与第 $d$ 段终端；没有越出物理右旗。

首段 primitive 被 $D$ 杀掉，其余输入从更高段开始，所以 (2.2) 的首源为零。逆向每个完整右零源核都由 $\xi=P_0z$ 唯一给出。

由 (1.3)，在这个共同参数域上
$$
\boxed{\|Z_A^+-Z_T^+\|\le\rho.}
\tag{2.3}
$$
所有 $q+j$ 的 primitive 都在这里，未只使用右首段的参数。

## 3. 普通完整右最小费的双向运输

令 $c_T=F_T^\dagger g$ 是天然模型的真正完整右最小链。它与 $-C_Ta$ 同源，所以
$$
c_T=-C_Ta+Z_T^+\xi,
\qquad \xi=P_0c_T.
\tag{3.1}
$$
右规范链的所有项都至少提升一次，故 $P_0C_Ta=0$，这证明参数正是 $P_0c_T$。特别
$$
\|\xi\|\le\|c_T\|=\lambda_T(g).
$$
以同一个 $a,\xi$ 定义
$$
\widetilde c_A=-C_Aa+Z_A^+\xi.
$$
§2 逐项保证其原完整旗及终端合法；首源准确为 $r$。于是
$$
\begin{aligned}
\lambda_A(r)
&\le\|\widetilde c_A\|\\
&\le\lambda_T(g)+\rho\|a\|+\rho\|\xi\|.
\end{aligned}
$$
得到
$$
\boxed{\lambda_A(r)\le(1+\rho)\lambda_T(g)+\rho\mu_A(r).}
\tag{3.2}
$$

反向取原最小链 $c_A=F_A^\dagger r$，写
$c_A=-C_Aa+Z_A^+\zeta$，其中 $\zeta=P_0c_A$、$\|\zeta\|\le\lambda_A(r)$。
把同一个 $\zeta$ 送入模型，得到天然源 $g$ 的合法完整右链。因此
$$
\boxed{\lambda_T(g)\le(1+\rho)\lambda_A(r)+\rho\mu_A(r).}
\tag{3.3}
$$
这两式没有使用任何未知的源逆压缩比较，也未支付一次额外 Jordan 条件数。它们比较的是普通右费 $\lambda$，与此前平坦费 $\lambda_{\rm flat}$ 的 Riesz 运输不同。

## 4. 模型全部核头源的原像旗

令
$$
\mathscr S_{0,T}=\ker T\cap\mathscr R_T
$$
为模型全部核头的天然源空间，定义
$$
\boxed{
\mathscr K_{\rm ker}
=\{a\in\mathscr U:T\mathcal B_Ta=0\},
\qquad
\mathscr X_{\rm ker}=\Gamma^{-1}\mathscr K_{\rm ker}.
}
\tag{4.1}
$$
这是有界映射的核及其有界同构像，所以闭。Taylor primitive 唯一性给准确坐标
$$
\boxed{
\mathscr K_{\rm ker}
=\bigoplus_{t=0}^{d-2}
\bigl(\ker T^{t+2}\cap\mathscr H_{\ge t+1}\bigr)
\otimes K_{q-t}.
}
\tag{4.2}
$$
它包含天然零源旗、原首头对角及先前模型物理首源原像旗；不将这些和声明正交。

若 $a\in\mathscr K_{\rm ker}$，则 $T^{t+2}a_t=0$。右规范链的第 $t$ 个输入在越过 $q$ 后只剩 $k=t+1$ 一项。因此 $C_Ta$ 只有右首段，且
$$
D(C_Ta)_1=-g.
$$
每一项至少提升一次，所以 $(C_Ta)_1\perp\ker D$。由同一个完整 MP 逆的唯一性，
$$
\boxed{-C_Ta=(D^\dagger g,0,\ldots,0),
\qquad g=\mathcal B_Ta\in\mathscr S_{0,T}.}
\tag{4.3}
$$
这是一条模型完整最小链和裸最小链。没有要求 $\mathscr S_{0,T}$ 约化模型的两个右 Gram。

## 5. 原普通右费与裸费的准确近接

对 $r\in\mathscr X_{\rm ker}$，原规范链与 (4.3) 的差给
$$
\lambda_A(r)\le\|D^\dagger g\|+\rho\|a\|.
\tag{5.1}
$$
两个规范链的首输出准确满足
$$
g-r=D(C_A-C_T)a|_1.
$$
施加同一个 $D^\dagger$，其与 $D$ 的复合是正交投影，故
$$
\|D^\dagger(g-r)\|\le\rho\|a\|.
\tag{5.2}
$$
任何原裸链的首段都经 $D$ 映到 $r$，所以
$\|D^\dagger r\|\le\alpha_A(r)$。结合 (5.1)–(5.2)，得到
$$
\boxed{
\alpha_A(r)\le\lambda_A(r)
\le\alpha_A(r)+2\rho\mu_A(r),
\qquad r\in\mathscr X_{\rm ker}.
}
\tag{5.3}
$$
左侧为原可行集的准确包含方向，右侧为本稿新估计；所有费用仍属同一个原源 $r$。

原完整双配对给
$$
\mu_A(r)^2
\le\lambda_A(r)\lambda_{{\rm flat},A}(r).
$$
由 (5.3)，若 $\chi_A^2=\alpha_A^2+\lambda_{{\rm flat},A}^2$，则
$$
\mu_A^2
\le\tfrac12\chi_A^2+2\rho\mu_A\chi_A.
$$
解这个标量二次不等式得
$$
\boxed{
\mu_A(r)\le\left(\rho+\sqrt{\rho^2+\tfrac12}\right)\chi_A(r),
}
\tag{5.4}
$$
$$
\boxed{
\mu_A(r)^2\le c_\rho\chi_A(r)^2,
\qquad
c_\rho=\left(\rho+\sqrt{\rho^2+\tfrac12}\right)^2
\le\tfrac12+2\rho.
}
\tag{5.5}
$$
末式用当前 $\rho<1/4$。这个常数趋于 $1/2$，没有未知角度或原头逆范数。

## 6. 准确覆盖数与两费用投影的范围

模型 Jordan 串长度为 $h+2,h,h-2,h$。在模天然零源旗
$\mathscr Y_t=\ker T^{t+1}\cap\mathscr H_{\ge t+1}$ 后，(4.2) 每个 $t$ 的头维数等于
$$
\dim(\ker T\cap\operatorname{Ran}T^{t+1})
=\#\{\ell\in(h+2,h,h-2,h):\ell\ge t+2\}.
$$
因而为
$$
\begin{cases}
4,&0\le t\le h-4,\\
3,&t=h-3,h-2,\\
1,&t=h-1,h,\\
0,&t\ge h+1.
\end{cases}
\tag{6.1}
$$
这个陈述是有限头商维数；它不把不同尾短旗或非正交 Jordan 核头当作正交物理模式。

可沿闭旗 $\mathscr X_{\rm ker}$ 作真正
$\mathfrak M=B_A+L_AG_AL_A$ 正交投影。若原源还需保留真正原负图 $\mathscr N_A$，则改沿闭交
$\mathscr N_A\cap\mathscr X_{\rm ker}$ 投影。因为 (5.5) 对该交仍成立，投影分量 $s$ 满足
$$
\chi_A(r)^2=\chi_A(s)^2+\chi_A(r-s)^2,\qquad
\mu_A(s)\le\sqrt{c_\rho}\chi_A(r).
\tag{6.2}
$$
在后一种投影中，$s$ 和 $r-s$ 继续属于原负图；但剩余条件是到该交的真实 $\mathfrak M$ 正交，不是 (4.2) 坐标为零。

这些投影可作用于已付的原实际窗口族，保留其同一强极限与累计两费用。本文未给其余源的上界，也未把 (3.2)–(3.3) 与 (5.5) 外推成整个模型完整四核头负图的比较。那一实际族上的温和常数仍是下一准确问题。


依赖的实际常数、扩域 primitive 与同源空间见[四块比较](R239-appendix-four-block-head-comparison-and-quarter-depth-source-elimination.md)、[完整平坦运输](R239-appendix-natural-four-block-flat-dual-transport-with-one-head-condition.md)及[完整退化头源流](R239-appendix-degenerate-head-full-source-flow-and-model-window-family.md)。
