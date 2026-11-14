# R239 附录：增长模型核幂的底链条件数与原同源可付源图

日期：2026-11-14（UTC）。作者：Astra-ISP-0c017065 / boundary_nonprimitive_1856；AI-assisted，GPT-6 Astra Pro。

状态：本文把全尾低头的裸到完整右界推广到天然四块模型的增长核幂。只估计完整 Jordan 基在每条串底部的限制条件数；三串耦合的这个条件数是四次多项式，不使用整个低头或整串的巨大条件数。随后把同一个模型源的两种右费运输回原源，并只与原完整平坦向量配对，得到真正原源图的两费用界。该图包含旧全部模型核头旗及全深度物理低头带。实际余源仍是 M 度量正交条件，未被当作坐标消失。普通 ISP 和无权 $N=M$ 仍 OPEN。

依赖：[全尾低头源带](R239-appendix-full-tail-low-head-source-strip-and-bare-to-complete-right-bound.md)、[四块完整延拓比较](R239-appendix-four-block-head-comparison-and-quarter-depth-source-elimination.md)、[完整右旗费用运输](R239-appendix-full-right-fee-transport-and-model-kernel-source-flag.md)、[模型天然旗与裸链参数化](R239-appendix-natural-four-block-free-flag-and-bare-chain-transport.md)、[天然模型源及完整核头流](R239-appendix-degenerate-head-full-source-flow-and-model-window-family.md)。

## 1. 一个只需底链条件数的精确引理

令 $T$ 是物理 $d$ 头上的严格降头幂零矩阵，尾仍为原 $D$，$\nu=\|D\|<1$。选择一组完整 Jordan 链基
$$
T=S\left(\bigoplus_\beta J_{\ell_\beta}\right)S^{-1},
\qquad v_{\beta,i}=Se_{\beta,i},
\quad Tv_{\beta,i}=v_{\beta,i-1}.
$$
每条链按其实际顶部生成，所以
$$
v_{\beta,i}=T^{\ell_\beta-1-i}v_{\beta,\ell_\beta-1},
\qquad
\operatorname{supp}_{\rm head}v_{\beta,i}
\subseteq\{0,\ldots,d-\ell_\beta+i\}.
\tag{1.1}
$$
这是严格降头的直接后果，不要求链基正交。

令 $P_K$ 为各串底部 $\min(K,\ell_\beta)$ 个抽象正交坐标的投影，记
$$
\kappa_{S,K}=\|S|_{P_K}\|\,\|(S|_{P_K})^{-1}\|,
\tag{1.2}
$$
逆只在真实像 $\ker T^K$ 上取。对天然源空间
$$
\mathscr R_{T,q}
=S\left[\bigoplus_{\beta,i}
e_{\beta,i}E_{\ell_\beta-i-1,q}\right],
$$
有
$$
\boxed{
\lambda_T(g)\le\kappa_{S,K}\sqrt{\gamma_K(\nu)}\,\alpha_T(g),
\quad g\in\mathscr R_{T,q}\cap\ker T^K,
\qquad \gamma_K(\nu)=\sum_{j=0}^{K-1}\nu^{2j}.
}
\tag{1.3}
$$
两种右最小者都在指定的原宽度 $d$ 环境右旗中取，只限制源为天然源。

证明沿全尾低头稿，但这里核对退化头的所有额外条件。任意同源裸链仍有
$$
D^ja_j=(-T)^{j-1}g,
\qquad
\sum_j\|(D^j)^\dagger T^{j-1}g\|^2\le\alpha_T(g)^2.
\tag{1.4}
$$
因为 $g\in\ker T^K$，每个 $(D^j)^\dagger T^{j-1}g$ 都在 $\ker T^K$，故只需 (1.2) 的受限逆。

写 $g'=S^{-1}g$。其坐标只在 $i<K$，且
$g'_{\beta,i}\in E_{\ell_\beta-i-1,q}$。令
$u_{\beta,i}=(D^{i+1})^\dagger g'_{\beta,i}$，则 $u_{\beta,i}\in E_{\ell_\beta,q+i+1}$。构造
$$
c'_t=(-1)^{t-1}\sum_{\beta}\sum_{i\ge t-1}
e_{\beta,i-t+1}D^{i+1-t}u_{\beta,i},\qquad c_t=Sc'_t.
\tag{1.5}
$$
所有 $t>K$ 项为零，且首输出为 $g$、内部及末输出均为零。
尾核阶为 $\ell_\beta-i-1+t$；(1.1) 对其物理头的上界是
$d-\ell_\beta+i-t+1$，二者恰互补到原 $E_{d-j}$ 旗。因此 (1.5) 真正落在原全部段、头和尾联合旗。

每个 $c'_t$ 都在 $P_K$ 坐标中，故用 $\|S|_{P_K}\|$ 即可。再从 (1.4) 的第 $i+1$ 项抽取各串第零坐标，得到
$$
\sum_{\beta,i}\|u_{\beta,i}\|^2
\le\|(S|_{P_K})^{-1}\|^2\alpha_T(g)^2.
$$
抽象坐标的正交性和 $D$ 的范数界给 (1.3)。这个证明没有要求 $\ker T^K$ 在原物理内积中约化任何源 Gram。

## 2. J_h 与 J_3 耦合的完整三条链

考虑
$$
J_h\otimes I_3+I_h\otimes J_3,
\qquad h\ge4,
$$
用 $e_i\otimes f_j$ 表示抽象正交基。取三条链，底部分别为
$$
v_{0,0}=e_0f_0,\qquad
v_{1,0}=e_1f_0-e_0f_1,\qquad
v_{2,0}=e_2f_0-e_1f_1+e_0f_2.
$$
完整链长度为 $h+2,h,h-2$。其全部列可明确选成
$$
\begin{aligned}
v_{0,j}={}&
\frac{(h+1-j)(h-j)}{h(h+1)}e_jf_0
+\frac{2(h+1-j)}{h(h+1)}e_{j-1}f_1
+\frac2{h(h+1)}e_{j-2}f_2,
&&0\le j\le h+1,\\
v_{1,j}={}&
\frac{(h-1-j)(j+1)}{h-1}e_{j+1}f_0
+\left(-1+\frac{2j}{h-1}\right)e_jf_1
-\frac2{h-1}e_{j-1}f_2,
&&0\le j\le h-1,\\
v_{2,j}={}&
\frac{(j+1)(j+2)}2e_{j+2}f_0
-(j+1)e_{j+1}f_1+e_jf_2,
&&0\le j\le h-3.
\end{aligned}
\tag{2.1}
$$
越出 $0\le i<h$ 的 $e_i$ 项取零。直接作用 $J_h+J_3$ 给 $v_{\beta,j-1}$，并杀掉三个底向量。三个底向量处于不同总度，线性独立；取一个假设链列关系中的最大链高并作用相应幂，可逐次排除所有系数。因此这些列组成完整 Jordan 基 $U_h$。

## 3. 底 K 层的条件数只有四次多项式

设 $1\le K\le h-2$。底 $K$ 层列都支持在低头 $e_0,\ldots,e_{K+1}$，且总度至多 $K+1\le h-1$。

对总度 $2\le s\le h-1$，三条链对应列
$v_{0,s},v_{1,s-1},v_{2,s-2}$ 在正交行
$e_sf_0,e_{s-1}f_1,e_{s-2}f_2$ 中的矩阵是
$$
M_s=
\begin{pmatrix}
\dfrac{(h+1-s)(h-s)}{h(h+1)}&
\dfrac{s(h-s)}{h-1}&\dfrac{s(s-1)}2\\[2mm]
\dfrac{2(h+1-s)}{h(h+1)}&
\dfrac{2s-h-1}{h-1}&-(s-1)\\[2mm]
\dfrac2{h(h+1)}&-\dfrac2{h-1}&1
\end{pmatrix}.
\tag{3.1}
$$
准确有
$$
\boxed{\det M_s=-1.}
\tag{3.2}
$$
可直接展开；也可先核 $s=2$，再用降低算子在相邻三维总度块间的上三角矩阵（对角全为一），得到行列式不变。

第一列各项绝对值不超过 $1$，第二列依次不超过 $s,1,1$，第三列不超过 $s(s-1)/2,s-1,1$。所以
$$
\|M_s\|\le3(s+1)^2.
$$
每个二阶子式的绝对值至多 $2(s+1)^2$；由 (3.2) 的伴随矩阵公式，
$$
\|M_s^{-1}\|\le6(s+1)^2.
\tag{3.3}
$$
总度零是 $[1]$，总度一的完整二阶块行列式也为 $-1$，并有更小的同类界。底 $K$ 层在最后两个总度块中只保留部分列；删列不会降低其最小奇异值低于完整 $M_s$ 的最小奇异值。

各总度块互相物理正交。因此
$$
\boxed{
\|U_h|_{P_K}\|\le3(K+2)^2,\qquad
\|(U_h|_{P_K})^{-1}\|\le6(K+2)^2,
\qquad
\kappa(U_h|_{P_K})\le18(K+2)^4.
}
\tag{3.4}
$$
加上另一个独立的 $J_h$ 串，条件数上界不变。这里完全没有 $(h-1)!(h+1)!$ 或全串指数条件数。

## 4. 原天然四块头的底链费用

回到 $m\ge8,d=2^m,n=m-2,h=d/4$，模型为
$$
T=A_\square=I_4\otimes A_n+
(bE_0+cE_1)\otimes I_h,
\qquad b=(m-1)^{-2},\quad c=m^{-2}.
$$
既有高二位 $3\oplus1$ 相似 $S_{\rm hi}$ 满足
$$
\kappa(S_{\rm hi})=\frac{m^2(m-1)^2}{2}.
\tag{4.1}
$$
原低头的无缩放上三角相似为 $A_n=V_nJ_hV_n^{-1}$。

取二进制小头 $H=2^\ell\le h$，明确要求 $3\le\ell\le n$，且 $K+2\le H$。这里有精确的一致性
$$
\boxed{V_n|_{H_H}=V_\ell,\qquad V_n^{-1}|_{H_H}=V_\ell^{-1}.}
\tag{4.2}
$$
证明：链矩阵 $K_n$ 的第 $j$ 列是 $(A_n^*)^je_0$，它是下三角的；其前 $H$ 阶主块正是 $K_\ell$，因为提升头指标的路径一旦离开前 $H$ 头便不能返回。对下三角块取逆伴随得到 (4.2)。

由 §3，耦合链底 $K$ 层只用这些低 $H$ 头，故完整模型 Jordan 基 $S$ 在底 $K$ 层的限制条件数满足
$$
\boxed{
\kappa_{S,K}
\le9m^2(m-1)^2(K+2)^4
\exp(221H^4/16).
}
\tag{4.3}
$$
所有映射在各自实际像上取逆；没有把非正交高二位或耦合链基当成等距。

于是对全部天然模型源 $g\in\ker T^K$，由 (1.3)，
$$
\boxed{
\lambda_T(g)\le C_{m,H,K}\alpha_T(g),
\qquad
C_{m,H,K}:=
\frac{9m^2(m-1)^2(K+2)^4}{\sqrt{1-m^{-2}}}
e^{221H^4/16}.
}
\tag{4.4}
$$
此式允许所有原天然尾核阶，不要求 $g$ 为 primitive。

## 5. 原源中的准确模型核幂预像旗

固定同一个原源 $r$，令 $a=\Gamma_qr$ 为强制 primitive 坐标，$\mathcal B_T$ 为模型的真实 Taylor 源映射，定义
$$
g=\mathcal B_Ta\in\mathscr R_{T,q},
\qquad
\boxed{\mathscr X_{T,K,q}
=\{r\in\mathscr R_q:T^K\mathcal B_T\Gamma_qr=0\}.}
\tag{5.1}
$$
这是原源上的闭线性子空间，不是物理源头投影。

由 $P_0D^tQ_s=\delta_{ts}$ 的完整 primitive 身份，(5.1) 等价于
$$
\boxed{T^{t+K+1}a_t=0\quad(0\le t\le d-2).}
\tag{5.2}
$$
它包含旧 $K=1$ 的全部模型核头预像旗，亦包含天然模型零源旗。

它还包含全尾低头稿的整个物理前 $K$ 头源带 $\mathscr X_{K,q}$：其准确 $\Gamma$ 坐标第 $t$ 层最高头不超过 $t+K$，而严格降头 $T^{t+K+1}$ 杀掉这个头旗。因此
$$
\boxed{\mathscr X_{K,q}\subseteq\mathscr X_{T,K,q}.}
\tag{5.3}
$$
这个包含是代数上的原源包含，没有用两个源旗之间未付的夹角。

## 6. 同一个实际源的两种右费用运输

令 $p$ 是原左最小者 $v=E_Ap$ 的全部 primitive 参数，故
$$
\|p\|\le\|v\|=\mu_A(r),\qquad p-a\in\mathscr F_A\subseteq\mathscr F_T,
\qquad \mathcal B_Tp=g.
$$
完整延拓比较在所有 primitive 输入孔数 $\le q+d$ 上给
$$
\|E_A^{\rm full}-E_T^{\rm full}\|\le\rho,
\qquad \rho\le e^{-d^4/20}.
\tag{6.1}
$$
因此完整右链运输已经证明
$$
\lambda_A(r)\le(1+\rho)\lambda_T(g)+\rho\mu_A(r).
\tag{6.2}
$$

为明确这里不先作另一个左 Schur，直接运输同一个裸候选。原裸最小者准确写作
$$
P_L[-C_Ap+Z_A^+u],\qquad \|u\|\le\alpha_A(r),
$$
其中 $u$ 是其首右 primitive。把同一个 $p,u$ 换成模型延拓，得到源仍为 $g$ 的合法模型裸链。由 (6.1)，
$$
\boxed{\alpha_T(g)
\le(1+\rho)\alpha_A(r)+\rho\mu_A(r).}
\tag{6.3}
$$
没有逐窗更换 $p$，没有运输一个不稳定的裸投影，也没有引入模型平坦源。

若 $r\in\mathscr X_{T,K,q}$，以 $C=C_{m,H,K}\ge1$ 简写 (4.4)，则
$$
\boxed{
\lambda_A(r)\le A_C\alpha_A(r)+\delta_C\mu_A(r),
\quad A_C=C(1+\rho)^2,
\quad\delta_C=\rho[1+C(1+\rho)].
}
\tag{6.4}
$$
与同一个原 $c_A^\flat$ 配对，得到
$$
\mu_A(r)^2\le\lambda_A(r)\lambda_{{\rm flat},A}(r)
\le\tfrac12A_C\chi_A(r)^2+
\delta_C\mu_A(r)\chi_A(r).
$$
故准确的原两费界为
$$
\boxed{
\mu_A(r)\le
\frac{\delta_C+\sqrt{\delta_C^2+2A_C}}2\,\chi_A(r)
\quad(r\in\mathscr X_{T,K,q}).
}
\tag{6.5}
$$
全过程使用原 $G_A,L_A,c_A^\flat$；不由模型两二次型近似推断 flat 运输。

## 7. 一个实际增长 K 与全部原窗的预算

令
$$
\ell=\lfloor3m/4\rfloor-2,\qquad H=2^\ell,\qquad K=H-2.
\tag{7.1}
$$
当 $m\ge8$，有 $\ell\ge3$、$K\ge1$、$K\le h-2$ 和 $H\le d^{3/4}/4$。所以 (4.4) 给
$$
C\le
\frac{9m^2(m-1)^2H^4}{\sqrt{1-m^{-2}}}
\exp(221d^3/4096)
\le e^{d^3/16}.
\tag{7.2}
$$
最后一个显式预算可这样核：前因子对数不超过
$\log(18m^4d^3)\le d$；而
$d\le(35/4096)d^3$ 对 $d\ge256$ 成立。

因此
$$
\delta_C\le3\rho C\le e^{-d^4/25}<1,
\qquad A_C\le4C.
$$
对 $C\ge1$，
$(1+\sqrt{1+8C})/2\le2\sqrt C$，故 (6.5) 特别给
$$
\boxed{\mu_A(r)^2\le4C\chi_A(r)^2
\quad(r\in\mathscr X_{T,K,q}),\qquad C\le e^{d^3/16}.}
\tag{7.3}
$$
这是对每个原合法 $q$ 的实际源图上界，未改变头、尾或窗宽。

## 8. 原 M 投影与多数实际窗口

令原负图为 $\mathscr N_q=\ker P(L_A+B_A)$，定义
$$
\mathscr Z_{T,K,q}=\mathscr N_q\cap\mathscr X_{T,K,q}.
$$
对同一个实际族 $r_q\in\mathscr N_q$，作真正
$\mathfrak M_q=B_A+L_AG_AL_A$ 正交投影 $z_q$ 到这个闭子空间，并置 $r'_q=r_q-z_q$。则
$$
r'_q\in\mathscr N_q,\qquad
\chi(r_q)^2=\chi(z_q)^2+\chi(r'_q)^2,
\qquad \mu(z_q)^2\le4C\chi(z_q)^2.
\tag{8.1}
$$
准确余条件为
$$
\boxed{\langle\mathfrak M_qr'_q,s\rangle=0
\quad(s\in\mathscr Z_{T,K,q}).}
\tag{8.2}
$$

以原顶部的实际窗口 $I_m=\{4d,\ldots,Q-d\}$、
$Q=\lfloor e^{d^3/4}\rfloor$、$n_m=|I_m|$ 为例，既有预算为
$$
\sup_{q\in I_m}\|E_q^\dagger r_q-w\|\le\beta_m\|w\|,
\qquad
\sum_{q\in I_m}\chi(r_q)^2\le2d\beta_m^2\|w\|^2,
\qquad\beta_m\to0.
$$
因此 $\sum_q\mu(z_q)^2\le8Cd\beta_m^2\|w\|^2$。至少一半窗口满足
$$
\mu(z_q)\le4\sqrt{Cd/n_m}\,\beta_m\|w\|.
$$
在这个多数集合 $J_m$ 上，
$$
\boxed{
\sup_{q\in J_m}\|E_q^\dagger r'_q-w\|
\le(1+4\sqrt{Cd/n_m})\beta_m\|w\|,
\qquad
\sum_{q\in J_m}\chi(r'_q)^2\le2d\beta_m^2\|w\|^2.
}
\tag{8.3}
$$
由 (7.2)，
$$
\boxed{Cd/n_m\le2d\,e^{-3d^3/16}\longrightarrow0.}
\tag{8.4}
$$
所以保留原强极限和归一累计两费用，无需任何额外尾下降速率。新族只被声明满足 (8.1)–(8.3)，不被免费当作共同的逐孔源流。

## 9. 精确新增范围与剩余接口

此次所付的是原源图 (5.1) 的增长模型核幂：在真实 primitive 坐标中，每一层满足的是 $T^{t+K+1}a_t=0$，模型底部有四条完整链，所有天然尾核阶均保留。它同时包括旧全部模型核头旗和全深度低物理头宽带，不需先估这两者的夹角。

余源的条件是 (8.2)。特别，不能据此说模型源 $\mathcal B_T\Gamma r'_q$ 没有 $\ker T^K$ 分量，也不能从图正交推断任何物理坐标为零。接下来的未付输入，是这一更大实际源图的度量补空间中的完整左费用比较。
