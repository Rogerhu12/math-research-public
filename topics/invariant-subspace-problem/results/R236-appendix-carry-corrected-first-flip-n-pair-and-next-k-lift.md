# R236 附录：原 N 型第一翻转双行的精确 carry 修正与下一 k 提升

日期：2026-11-13 UTC。作者：Astra-ISP-0c017065 / normal_full_columns_1856；AI-assisted，GPT-6 Astra Pro。
状态：**已证明的指定实际 gauge 范围。** 本文将[十五阶反演/实际固定点构造](R236-appendix-next-k-lagrange-correction-and-paid-original-normal-anchor.md)扩展到第一翻转真正产生的两条 $N_j$ 行，完整保留第二行的移位 carry 系数。仍以该特定翻转已合法产生同一个非零正常见证为前提；没有证明总可选到该翻转，也没有扩展为一般 $Q_j/H_\zeta$ 行。

## 1. 指定翻转所给的真实双行

固定 $j_0\ge0$，$a_j=(j+1)^{-2}$，定义原 N 型二次式
$$
X=\sum_{j\ge j_0}a_jN_j,\qquad
Y=\sum_{j>j_0}a_j^2N_j,
$$
$$
B_0=\sum_{j\ge j_0}a_j^2N_j^2,\qquad
T_N=X^2-B_0+Y.
$$
取 $\zeta^{2^{j_0}}=-1$、$\zeta^{2^{j_0+1}}=1$ 的 dyadic gauge。
因低于 $j_0$ 的系数为零，它只改变参与这些行的第 $j_0$ 个 $N_j$ 的符号。
准确有
$$
D=\gamma_\zeta X-X=-2a_{j_0}N_{j_0},
\quad\gamma_\zeta Y-Y=0,
\quad\gamma_\zeta B_0-B_0=0.
$$
因此原一次因子为 $S=X-a_{j_0}N_{j_0}$。

**以下明确假设这一特定 gauge 已通过原核配对步骤产生同一个非零正正常 $\rho$。**
具体可用的输入是 $M=\ker T_N\ne0$ 且原双线性配对 $B(M,U_\zeta M)\ne0$；
这里使用的确切已发表步骤是
[R236《迟首二次核与同一个正正规两行湮灭者》§3 与 §5](R236-appendix-late-support-quadratic-kernels-and-positive-joint-first-annihilators.md)：
§3 的原 C 对称配对只要求此处的实际身份 $\gamma_\zeta T_N-T_N=2DS$；
§5 在真旗上构造同一个正向量态。该稿 §4 的选相位存在性没有在本文调用。

为明确 N 版本的适用，直接列出该两步：$M_\zeta=U_\zeta M$，
原对称配对给 $B(DSM,M_\zeta)=0$。
$D=-2a_{j_0}A^{2^{j_0}}/d_{j_0}$，由原归一化远尾弱单位，
$\overline{DM}=M$；因 $S$ 与 $D$ 交换且有界，故 $B(SM,M_\zeta)=0$。
假设的 $B(M,M_\zeta)\ne0$ 迫 $N_0=\overline{SM}\subsetneq M$。
$M,N_0$ 都对完整 $A'$ 不变。取任意 $0\ne h\in M\ominus N_0$，
则同一 $\rho=h\otimes h$ 对每个 $R\in A'$ 满足
$\langle SRh,h\rangle=\langle T_NRh,h\rangle=0$。
这完整给出本文使用的同一正正常态，并未假定该特定 $\zeta$ 总可满足非零配对。
原二次见证身份于是给该同一 $\rho$ 湮灭
$$
S=\sum_{j\ge n}a_jN_j,
\qquad
Z=Y-B_0+a_{j_0}^2N_{j_0}^2,
\quad n=j_0+1\ge1.
$$
使用每个真实 $N_j^2=\eta_jN_{j+1}$，第二行恰为
$$
\boxed{
Z=a_n^2N_n+
\sum_{j>n}(a_j^2-a_{j-1}^2\eta_{j-1})N_j.
}
\tag{1.1}
$$
同态保持也可直接由
$$T_N=S(X+a_{j_0}N_{j_0})+Z$$
验证：同一个态湮灭 $S\mathcal A'$ 与 $T_N\mathcal A'$，便湮灭 $Z\mathcal A'$。
没有把这些 carry 项从正常配对中删除。

## 2. 实际修正比仍严格递减

写 $Z=\sum_{j\ge n}c_jN_j$，令 $r_j=c_j/a_j$。
则
$$
r_n=a_n,
\qquad r_j=a_j-e_j\quad(j>n),
\qquad e_j=\frac{(j+1)^2}{j^4}\eta_{j-1}>0.
$$
记 $g_j=a_j-a_{j+1}$。对 $j\ge1$，
$$
e_j\le4j^{-2}\eta_{j-1},\qquad g_j\ge(18j^3)^{-1},
$$
故
$$
\frac{e_j}{g_j}\le72j\eta_{j-1}
\le72e^{-769}<1/100.
\tag{2.1}
$$
最后一步用 $\log j\le16^{j-1}$ 和原 $\eta_{j-1}\le e^{-77016^{j-1}}$。
因此对 $j>n$，
$$
.99g_j\le r_j-r_{j+1}\le1.01g_j,
$$
而在第一处
$$
g_n\le d:=r_n-r_{n+1}\le1.01g_n.
\tag{2.2}
$$
特别整个实际 $r_j$ 严格递减且为正。

## 3. 两次尾交、整体符号与原双源

仍令 $m=n+1$、$l=n+2$、$x=n+1\ge2$，并定义
$$
b_j=a_j(r_n-r_j),\qquad b_m=a_md>0,
$$
$$
P_m=(r_nS-Z)/b_m=N_m+V,
\qquad V=\sum_{j\ge l}\beta_jN_j,quad
\beta_j=\frac{a_j(r_n-r_j)}{a_md}>0.
$$
这次取正的另一行
$$
U=\sum_{j\ge l}\alpha_jN_j,\qquad
\alpha_j=\frac{a_j(r_m-r_j)}d>0.
\tag{3.1}
$$
若 $F=\sum_{j\ge m}a_jN_j$，则 $F=a_mP_m-U$。
因此 $H,K$ 仍具有同样的准确形式
$$
\varepsilon=\eta_na_n^2=\eta_n/x^4,quad\delta=\eta_m,
\qquad H=V^2-\delta N_l,\qquad K=U^2+\varepsilon V.
$$
但原源中的符号必须相应改变。令
$$
E=a_m^2P_m-2a_mU-\varepsilon I,
$$
则
$$
\boxed{
H=(V-N_m)(r_nS-Z)/b_m,
\qquad
K=(F-a_nN_n)S-(r_nS-Z)E/b_m.
}
\tag{3.2}
$$
直接由 $(F-a_nN_n)S=F^2-\varepsilon N_m=K+P_mE$ 核验。
完整两次尾交仍为 $(S,Z)\cap\mathcal C_l=(H,K)$。

写
$$
H=SH_S+ZH_Z,\qquad K=SK_S+ZK_Z.
$$
全部四个实际源为
$$
H_S=r_n(V-N_m)/b_m,\qquad H_Z=-(V-N_m)/b_m,
$$
$$
K_S=F-a_nN_n-r_nE/b_m,\qquad K_Z=E/b_m.
\tag{3.3}
$$
由 (2.2) 与正系数求和，可取
$$
\|U\|\le.505<1,quad\|V\|\le5x^2,\qquad b_m^{-1}\le8x^5,
$$
$$
\|H_S\|\le48x^5,quad\|H_Z\|\le48x^7,quad
\|K_S\|\le74x,quad\|K_Z\|\le72x^3.
\tag{3.4}
$$
说明：未修正 $r_j=a_j$ 时，$\|U\|\le1/2$、$\|V\|\le4x^2$；
(2.2) 将每个 $U$ 系数夹在其原值的 $[.99/1.01,1.01]$ 倍、每个 $V$ 系数夹在 $[1/1.01,1.01]$ 倍。
其余界用 $\|V-N_m\|\le6x^2$、$\|E\|\le9/x^2$ 即得。

## 4. 下一两位的正行列式与纯尾

令
$$
\alpha=\alpha_l,\ \beta=\beta_l,\quad
\alpha_1=\alpha_{l+1},\ \beta_1=\beta_{l+1},
$$
并写 $U=\alpha N_l+\alpha_1N_{l+1}+p$、
$V=\beta N_l+\beta_1N_{l+1}+q$。
直接消元给
$$
\boxed{
\Delta=\beta\alpha_1-\alpha\beta_1
=\frac{a_la_{l+1}(r_l-r_{l+1})}{a_md}>0.
}
\tag{4.1}
$$
令 $\lambda=\alpha_1/\beta_1$、$\nu=\Delta/\beta_1$。
则
$$
\lambda=a_m\frac{r_m-r_{l+1}}{r_n-r_{l+1}}\le a_m\le x^{-2},
\qquad 0<\nu=\lambda\beta-\alpha\le3x^{-2}\le1.
\tag{4.2}
$$
这里 $\beta\le3$ 由 (2.2) 及未修正系数的显式式子得到。

未修正的行列式是
$$
\Delta_0=
\frac{x^2(x+1)^4(2x+5)}{(x+2)^4(x+3)^4(2x+1)}
\ge(1944x^2)^{-1}.
$$
由 (2.2)，$\Delta\ge(.99/1.01)\Delta_0$，所以
$$
\boxed{\Delta^{-1}\le2000x^2\le e^{10\,16^n}.}
\tag{4.3}
$$
所需真实远尾是
$$
\boxed{
W=p-\lambda q
=\sum_{j\ge l+2}\frac{a_j(r_{l+1}-r_j)}{r_n-r_{l+1}}N_j.
}
\tag{4.4}
$$
其系数为正且逐项不超过 $U$ 的对应系数，故 $\|W\|\le.505<1$。
同时 $\|p\|\le1$、$\|q\|\le5x^2$。

## 5. 同一个十五阶实际固定点适用，所有原源保留

现在使用上一稿的全部具体定义，而不是直接套一个未付的商逆：
$$
\kappa_0=\varepsilon^2\delta,quad
\kappa_1=\kappa_0^2\eta_l,quad
\kappa_2=\kappa_1^2\eta_{l+1},\qquad T=\kappa_2N_{l+2},
$$
$$
f(z)=z+(\lambda/\varepsilon)z^2+(\nu/\kappa_0)z^4.
$$
原 $E_0,E_1,E_2$ 与 $W-f(U)=-(\lambda/\varepsilon)K-(\nu/\kappa_0)E_0$ 身份完全相同。
由 $\|U\|,\|W\|\le1$、$\lambda,\nu\le1$、$\varepsilon\|V\|<1$，
上一稿 §§4–6 的全部真实系数界、球半径、$\kappa_2\le e^{-6123600\,16^n}$、
收缩常数与差商单位 $\|D^{-1}\|\le2$ 原样成立。
因此同一指定球内存在已付的 $u_*\in\mathcal B_{l+2}$，以及明确源
$$
U-u_*=HA_H+KA_K,\qquad
\|A_H\|+\|A_K\|\le e^{483010\,16^n}.
\tag{5.1}
$$
这里 $A_H,A_K$ 正是上一稿 (6.2) 的实际式，不是另选的来源。

仍定义
$$
R_*=(\beta p-\alpha q-\beta u_*-\alpha u_*^2/\varepsilon)/\Delta,
$$
$$
F_*=[\beta+(\alpha/\varepsilon)(U+u_*)]/\Delta,quad
G_*=F_*A_K-\alpha/(\varepsilon\Delta).
$$
则 $P_*=N_{l+1}+R_*$ 的全部**当前原 S,Z** 源为
$$
\boxed{
\mathcal U_*=H_SF_*A_H+K_SG_*,\qquad
\mathcal V_*=H_ZF_*A_H+K_ZG_*.
}
\tag{5.2}
$$
(3.3)–(3.4) 付出了这次整体符号改变后的全部原来源。

由于 $\alpha/\varepsilon\le x^4\eta_n^{-1}\le e^{1404\,16^n}$，
$\Delta^{-1}\le e^{10\,16^n}$，且原系数的总范数至多 $242x^7$，
上一稿的大余量仍给同一保守结论
$$
\boxed{
\|R_*\|\le e^{210000\,16^n},\qquad
\|\mathcal U_*\|,\|\mathcal V_*\|\le e^{590000\,16^n}.
}
\tag{5.3}
$$
分阶计数中的标量系数和 $\Delta^{-1}$ 均只另付 $O(\log(n+2))$，
所以较准确的指定目标/原源界仍为
$$
21u_n+8u_{n+1}+O(\log(n+2)),\qquad
51u_n+23u_{n+1}+O(\log(n+2)).
\tag{5.4}
$$

## 6. 同态、同锚和未闭的量词

本文从 §1 固定的同一个正常见证出发。
(5.2) 给 $P_*=S\mathcal U_*+Z\mathcal V_*$，因此
$$
\Theta_*=2P_*(I+N_{l+1})^{-2}
$$
仍有准确条件真空锚 $e^*\Theta_*e=I$，并由该同一 $\rho$ 湮灭。
目标范数至多 $e^{211000\,16^n}$；两个原源分别再乘范数小于9的实际因子。
不存在跨 gauge 换密度，也没有将 (1.1) 的极小 carry 项作为误差丢掉。

仍未证明第一翻转必给非零核配对；一般存在性所选的另一 $\zeta$ 不自动属于此范围。
本文只覆盖明确的 N 型二次式与这里的辅助系数，不把它替代一般 Cayley $Q_j$ 行。
固定 n 之后的全部未来低费用与反向完整理想度量仍按上一稿的未闭范围保留。
