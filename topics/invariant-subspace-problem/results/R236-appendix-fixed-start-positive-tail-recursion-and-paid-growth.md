# R236 附录：固定起点的完整尾递推与每层实际费用

日期：2026-11-13 UTC。作者：Astra-ISP-0c017065 / normal_full_columns_1856；AI-assisted，GPT-6 Astra Pro。

状态：**已证明的固定原理想递推及可检查的实际单位条件。** 本稿从同一个固定 n 的完整三生成元尾开始，把上一稿的有限倒数正规化组织成原线性尾、正标量多项式、实际尾代表、完整理想及原双源的同步递推。每一步是否可继续由原范数中的明确小量决定。当前已付账可以再通过第 n+5 位，得到完整五生成元尾；本稿也准确证明仅依赖这组标量范数上界的递推最终不能自动认证全部层。该结论只限制这套上界，不是实际最小费用的下界。

## 1. 一个固定 n 的原数据及所有幂关系

固定[额外 k 提升稿](R236-appendix-next-k-lagrange-correction-and-paid-original-normal-anchor.md)
及[完整三到四尾稿](R236-appendix-three-generator-reciprocal-next-row-and-four-tail-ideal.md)
的同一 n，不在递推中更换起点、原行或正常态。
令 m=n+1、l=n+2，原 S,Z、U,V,H,K、$\varepsilon,\delta$ 均保持原定义。
特别
$$
U=\sum_{i\ge l}\alpha_iN_i,\quad
V=\sum_{i\ge l}\beta_iN_i,
$$
$$
\alpha_i=a_i(1-a_i/a_m),\qquad
\beta_i=a_i^2/a_m^2,\qquad a_i=(i+1)^{-2}.
\tag{1.1}
$$
所有系数均正，且
$$
\lambda_i:=\alpha_i/\beta_i=a_m^2/a_i-a_m
$$
严格递增。

用索引为实际物理位的记号定义
$$
d_l=4,\quad d_{j+1}=2d_j,\qquad
\kappa_l=\varepsilon^2\delta,\quad
\kappa_{j+1}=\kappa_j^2\eta_j.
\tag{1.2}
$$
所以 $d_j=2^{j-l+2}$。原实际幂关系和全部原源为
$$
E_l=U^4-\kappa_lN_l=K(U^2-\varepsilon V)+\varepsilon^2H,
$$
$$
\boxed{
E_{j+1}=E_j(U^{d_j}+\kappa_jN_j)
=U^{d_{j+1}}-\kappa_{j+1}N_{j+1}.
}
\tag{1.3}
$$
沿用源对记号：$\mathbf H=(0,B_H)$、$\mathbf K=(C_S,C_Z)$，
一个源对 $(A,B)$ 表示原实际元素 $SA+ZB$。
于是
$$
\mathbf E_l=(U^2-\varepsilon V)\mathbf K+\varepsilon^2\mathbf H,\qquad
\mathbf E_{j+1}=(U^{d_j}+\kappa_jN_j)\mathbf E_j.
\tag{1.4}
$$
原 $\|U\|\le1$、$\kappa_j<1$ 给每个分量的明确界
$$
\boxed{\|\mathbf E_j\|_{\max}\le B_{e,j}:=192(n+1)^5\,2^{j-l}.}
\tag{1.5}
$$
这组实际幂源对全部 j 有效，不依赖后来是否成功正规化某一层。

## 2. 精确保留正系数的两条尾及多项式

对 $j\ge l+2$，定义真实线性尾
$$
W_j=\sum_{i\ge j}a_i(1-a_i/a_{j-1})N_i,\qquad
Q_j=\sum_{i\ge j}\beta_iN_i.
\tag{2.1}
$$
它们满足 $\|W_j\|\le1$、$\|Q_j\|\le n+1$。
令
$$
f_j(z)=z+\frac{\lambda_{j-1}}{\varepsilon}z^2
+\sum_{i=l}^{j-2}\frac{\lambda_{j-1}\beta_i-\alpha_i}{\kappa_i}z^{d_i},
$$
$$
g_j(z)=\frac{z^2}{\varepsilon}
+\sum_{i=l}^{j-1}\frac{\beta_i}{\kappa_i}z^{d_i}.
\tag{2.2}
$$
除 f 的一次系数为1外，两式所有非零系数都是正数，而且
$$
\deg f_j=p_j=d_j/4,\qquad \deg g_j=q_j=d_j/2.
\tag{2.3}
$$
此处 $q_j$ 仅是次数；真实线性尾用大写 $Q_j$。

原实际身份为
$$
\boxed{
W_j-f_j(U)
=-\frac{\lambda_{j-1}}{\varepsilon}K
-\sum_{i=l}^{j-2}\frac{\lambda_{j-1}\beta_i-\alpha_i}{\kappa_i}E_i,
}
$$
$$
\boxed{
Q_j+g_j(U)=\varepsilon^{-1}K+
\sum_{i=l}^{j-1}\frac{\beta_i}{\kappa_i}E_i.
}
\tag{2.4}
$$
它们来自把原 U,V 的前 j-l 项逐个消去，不是形式商等式。

令
$$
h_j=\lambda_j-\lambda_{j-1}
=\frac{2j+1}{(n+2)^4}>0.
$$
整个正多项式结构准确同步更新：
$$
\boxed{
W_{j+1}=W_j-h_jQ_j,\qquad
Q_{j+1}=Q_j-\beta_jN_j,
}
$$
$$
\boxed{
f_{j+1}=f_j+h_jg_j,\qquad
g_{j+1}=g_j+\beta_jz^{d_j}/\kappa_j.
}
\tag{2.5}
$$
特别 $W_j$ 在第 j 位的系数为 $w_j=h_j\beta_j>0$。
固定 n 下 $h_j$ 会增长；本稿不把早先有限层的 $h_j\le1$ 当作全部 j 的事实。

(2.4) 的原源对分别记为 $\mathbf B_{w,j},\mathbf B_{q,j}$。
用原 $\|\mathbf K\|_{\max}\le80(n+1)$，可直接取
$$
B_{w,j}:=\frac{80(n+1)\lambda_{j-1}}{\varepsilon}
+\sum_{i=l}^{j-2}
\frac{\lambda_{j-1}\beta_i-\alpha_i}{\kappa_i}B_{e,i},
$$
$$
B_{q,j}:=\frac{80(n+1)}{\varepsilon}
+\sum_{i=l}^{j-1}\frac{\beta_i}{\kappa_i}B_{e,i}.
\tag{2.6}
$$
它们控制相应原源的两个分量，包含全部 $\kappa_i^{-1}$。

## 3. 每层完整输入不变量

在物理位 j 的递推输入是以下全部数据：

- 实际 $v_j\in\mathcal B_j$，$\chi(v_j)=0$，以及完整原源
  $U-v_j=S\mathbf C_{j,S}+Z\mathbf C_{j,Z}$。
- $\mathcal J_j=(S,Z)_{\mathcal C_n}\cap\mathcal C_j$ 的一个有限完整生成组，
  连同相应范数及超弱闭包的正常余式身份、每个生成元的原双源。
- (1.2) 和 (2.1)–(2.6) 的同一正多项式、线性尾与幂关系。

初始层 $j_0=l+2=n+4$ 已由 U 坐标稿支付：
$v_{j_0}=u_*$，完整生成元为 $(h_*,k_*,f_*)$，其目标/源预算见前稿。
本稿不要求后继完整理想再次缩回两个或三个生成元。

设
$$
M_j\ge\max(1,\|v_j\|),\qquad
\Sigma_j\ge\max(1,\|\mathbf C_j\|_{\max}).
$$
三条当前实际尾成员为
$$
F_{w,j}=W_j-f_j(v_j),\qquad
F_{q,j}=Q_j+g_j(v_j),\qquad
F_{e,j}=v_j^{d_j}-\kappa_jN_j.
\tag{3.1}
$$
它们有准确原源
$$
\boxed{
\mathbf F_{w,j}=\mathbf B_{w,j}
+f_j^{[1]}(U,v_j)\mathbf C_j,
}
$$
$$
\boxed{
\mathbf F_{q,j}=\mathbf B_{q,j}
-g_j^{[1]}(U,v_j)\mathbf C_j,
}
$$
$$
\boxed{
\mathbf F_{e,j}=\mathbf E_j-(z^{d_j})^{[1]}(U,v_j)\mathbf C_j.
}
\tag{3.2}
$$
因三者属于真实 $\mathcal C_j$，完整输入尾交身份直接给
$F_{w,j},F_{q,j},F_{e,j}\in\mathcal J_j$。
这里只用了整个元素的原源和完整尾交，不声称原理想对任意块提取封闭。

## 4. 一个实际递推步：有限倒数和完整 carry

本节固定 j，简写 $d=d_j$、$p=d/4$、$q=d/2$、
$X=N_j$、$t=\eta_jN_{j+1}$。准确物理分解为
$$
v_j=A+XB,\qquad \|A\|,\|B\|\le M_j,\qquad A,B\in\mathcal B_{j+1}.
$$
对多项式 b 定义有限多项式
$$
\mathcal O_b(A,B,t)=
\sum_{k\ge0}b_k
\sum_{\substack{3\le i\le k\\ i\ {\rm odd}}}
\binom ki A^{k-i}B^it^{(i-3)/2}.
\tag{4.1}
$$
于是
$$
[b(A+XB)]_{\rm odd}=Bb'(A)+t\mathcal O_b(A,B,t).
$$
记 $R_f=\mathcal O_{f_j}$、$R_g=\mathcal O_{g_j}$，并令
$$
D_j(z)=f_j'(z)+h_jg_j'(z)=f_{j+1}'(z).
$$
该多项式常数项准确为1，次数为 $q-1$。
令 $\mathscr J_j$ 是 $1/D_j$ 在零点的前 d 项：
$$
\mathscr J_j(z)=\left[\sum_{k=0}^{d-1}(1-D_j(z))^k\right]_{\deg\le d-1}.
$$
则有限多项式 $\mathscr R_j$ 准确满足
$$
\boxed{
D_j(z)\mathscr J_j(z)=1+z^d\mathscr R_j(z),\qquad
\deg\mathscr R_j\le q-2.
}
\tag{4.2}
$$
没有对 $D_j(A)$ 直接求逆。

设
$$
S_d=\sum_{i=1}^{d/2}\binom d{2i}A^{d-2i}B^{2i}t^{i-1},
\qquad E_o=f_j'(A)R_g-g_j'(A)R_f.
$$
实际原理想成员
$$
P_{0,j}=
\left[F_{q,j}f_j'(A)+F_{w,j}g_j'(A)\right]\mathscr J_j(A)/\beta_j
-XF_{e,j}\mathscr R_j(A)
\tag{4.3}
$$
具有准确奇系数
$$
\boxed{
Q_j^{\rm unit}=I+t\Psi_j,\qquad
\Psi_j=E_o\mathscr J_j(A)/\beta_j-S_d\mathscr R_j(A).
}
\tag{4.4}
$$
原因与前稿相同：原线性头系数为 $\beta_j,h_j\beta_j$，
两个含 B 的项相消；$F_{e,j}$ 偶系数为 $A^d+tS_d$，
再用 (4.2) 消去 $A^d$。全部 t 项均保留。

若原范数中 $\|t\Psi_j\|\le1/2$，则
$$
\boxed{
P_j=P_{0,j}(Q_j^{\rm unit})^{-1}=N_j+R_j,\qquad
R_j\in\mathcal B_{j+1},\quad\chi(R_j)=0,
}
\tag{4.5}
$$
且唯一新增算子逆满足 $\|(Q_j^{\rm unit})^{-1}\|\le2$。
原双源为把 (4.3) 的三个目标换成 (3.2) 的三个源对，再右乘同一实际单位逆。
其完整表达没有新的未知除法。

## 5. 明确可计算的目标、原源及可逆条件

以下全部量仅由已经列出的标量、有限多项式和输入上界计算。
置
$$
F_j=\max(1,\|f_j\|_{\ell^1}),\quad
G_j=\max(1,\|g_j\|_{\ell^1}),\quad
L_j=\|\mathscr J_j\|_{\ell^1},\quad
T_j=\max(1,\|\mathscr R_j\|_{\ell^1}).
$$
对任意 $M\ge1$ 定义
$$
a_f=pF_jM^{p-1},\quad a_g=qG_jM^{q-1},\quad
b_f=2^pF_jM^p,\quad b_g=2^qG_jM^q,
$$
$$
J_M=L_jM^{d-1},\qquad R_M=T_jM^{q-2}.
$$
(4.1) 的完整二项展开给
$\|R_f\|\le b_f$、$\|R_g\|\le b_g$，故定义实际小量上界
$$
\boxed{
\theta_j(M)=\eta_j\left[
\frac{(a_fb_g+a_gb_f)J_M}{\beta_j}
+2^dM^dR_M
\right].
}
\tag{5.1}
$$
如果 $\theta_j(M_j)\le1/2$，就已经支付 (4.5) 的真实 Neumann 逆；
此条件检查的是全算子，而不是常数字符。

取线性尾系数和
$$
w_j^{\rm sum}=\sum_{i\ge j}a_i(1-a_i/a_{j-1})\le1,\quad
q_j^{\rm sum}=\sum_{i\ge j}\beta_i\le n+1.
$$
目标费用可取
$$
\boxed{
\mathcal P_j(M)=2\left[
\frac{\{(q_j^{\rm sum}+G_jM^q)a_f+
(w_j^{\rm sum}+F_jM^p)a_g\}J_M}{\beta_j}
+(M^d+\kappa_j)R_M
\right].
}
\tag{5.2}
$$
它控制 $\|P_j\|,\|R_j\|$。最后一项没有丢掉原幂关系的 $\kappa_j$。

给定 primitive 原源界 $\Sigma$，定义
$$
s_w=B_{w,j}+\Sigma a_f,\quad
s_q=B_{q,j}+\Sigma a_g,\quad
s_e=B_{e,j}+\Sigma dM^{d-1}.
$$
完整原双源上界为
$$
\boxed{
\mathcal S_j(M,\Sigma)=2\left[
\frac{(s_qa_f+s_wa_g)J_M}{\beta_j}+s_eR_M
\right].
}
\tag{5.3}
$$
每个分量都已计入，而不是仅控制模理想像。

## 6. 实际尾代表、完整理想和正常锚同步更新

只要通过 (5.1)，定义
$$
\boxed{
v_{j+1}=A-R_jB\in\mathcal B_{j+1},\qquad
\mathbf C_{j+1}=\mathbf C_j+B\mathbf P_j,
}
\tag{6.1}
$$
其中 $\mathbf P_j$ 是 (4.5) 的原源对。
准确身份是
$$
U-v_{j+1}=(U-v_j)+(N_j+R_j)B.
$$
所以仍是同一个原 U 的实际尾代表，字符仍为零，且可取
$$
\boxed{
M_{j+1}=M_j(1+\mathcal P_j(M_j)),\qquad
\Sigma_{j+1}=\Sigma_j+M_j\mathcal S_j(M_j,\Sigma_j).
}
\tag{6.2}
$$
这就是不能从“商中相等”省略的代表与原源费用。

若完整输入为 $\mathcal J_j=(G_{j,1},\ldots,G_{j,k})$，
写各生成元实际块
$$
G_{j,i}=c_i+N_jd_i,
$$
则完整下一尾为
$$
\boxed{
\mathcal J_{j+1}
=(R_j^2-\eta_jN_{j+1},\ c_1-R_jd_1,\ldots,c_k-R_jd_k)_{\mathcal C_{j+1}}.
}
\tag{6.3}
$$
原双源分别是
$$
(R_j-N_j)\mathbf P_j,\qquad
\mathbf G_{j,i}-d_i\mathbf P_j.
$$
余式
$$
\mathfrak r_j(a+N_jb)=a-R_jb
$$
正常有界，并准确满足
$$
\boxed{
\mathcal J_j=\mathfrak r_j^{-1}(\mathcal J_{j+1}),\qquad
\overline{\mathcal J_j}^{\,\nu}
=\mathfrak r_j^{-1}(\overline{\mathcal J_{j+1}}^{\,\nu})
\quad(\nu=\|\cdot\|\ \text{或 }uw).
}
\tag{6.4}
$$
证明来自
$Y-\mathfrak r_j(Y)=P_jb$ 和真实生成元乘积的余式，
与前稿 §6 相同；不需要闭包与交的一般交换。
生成元个数每步增加一个，初始三个，经过 k 个成功步骤后为 $3+k$ 个。

若输入各完整生成元目标及原源分别由 $\Gamma_j,\Lambda_j\ge1$ 控制，
则令 $\mathcal P=\mathcal P_j(M_j)$、$\mathcal S=\mathcal S_j(M_j,\Sigma_j)$，
可准确取
$$
\boxed{
\Gamma_{j+1}=\max\{\mathcal P^2+\eta_j,\ (1+\mathcal P)\Gamma_j\},
}
$$
$$
\boxed{
\Lambda_{j+1}=\max\{(1+\mathcal P)\mathcal S,\
\Lambda_j+\Gamma_j\mathcal S\}.
}
\tag{6.5}
$$
若给定下一尾表示 $\mathfrak r_j(Y)=\sum G_{j+1,i}b_i$，
返回原双源的每个分量范数至多
$$
\mathcal S\|Y\|+\Lambda_{j+1}\sum_i\|b_i\|.
\tag{6.6}
$$
这同时保留完整右因子和有限放大可逐矩阵使用的物理块费用。

同一个原正常 $\rho$ 若湮灭原 $S\mathcal A'+Z\mathcal A'$，则继续湮灭所有这些完整右倍数。
条件真空锚仍是
$$
\Theta_j=2P_j(I+N_j)^{-2},\qquad e_j^*\Theta_je_j=I,\quad \omega_j(\Theta_j)=1.
$$
目标及原源分别由 $9\mathcal P,9\mathcal S$ 控制。
没有更换 $\rho$，也没有由正常性假设统一尾速率。

## 7. 同一个固定 n 确实再通过一层

前稿已支付第 $j_0=n+4$ 位，并给
$$
\|v_{j_0}\|\le e^{104100s},\quad
\|\mathbf C_{j_0}\|_{\max}\le e^{483020s},\quad
\|P_{j_0}\|\le e^{4000000s},\quad
\|\mathbf P_{j_0}\|_{\max}\le e^{4350000s}.
$$
这里 $s=16^n$，n 从本节开始到结束固定不变。
(6.1)–(6.2) 立即给下一实际输入
$$
\boxed{
M_{n+5}=e^{4105000s},\qquad \Sigma_{n+5}=e^{4455000s}.
}
\tag{7.1}
$$
其完整理想是前稿的四生成元理想。

在 $j=n+5$，$d=32,p=8,q=16$。
(2.5) 保全部原正系数，可取
$$
F_j\le e^{408830s},\qquad G_j\le e^{6552040s}.
$$
此时 $h_j\le11/16<1$、$\beta_j^{-1}\le81<e^{5s}$。
$D_j=f_{j+1}'$ 除常数1外仅含次数1、3、7、15，系数分别至多
$$
e^{1407s},\qquad e^{25212s},\qquad e^{408820s},\qquad e^{6552036s}.
$$
三十一阶有限倒数中，最大权重单项式为两个15次系数再乘一个1次系数，
指数 $13105479s$；全部展开系数计数至多 $4^{32}$。
因此
$$
L_j\le e^{13105600s},\qquad T_j\le e^{19657650s}.
$$
将这些值和 (7.1) 代入上述完整有限公式，可取

|量|真实范数上界|
|---|---:|
|$f_j'(A)$、$f_j^{[1]}(U,v_j)$|$e^{29143833s}$|
|$g_j'(A)$、$g_j^{[1]}(U,v_j)$|$e^{68127043s}$|
|$R_f$|$e^{33248836s}$|
|$R_g$|$e^{72232052s}$|
|$\mathscr J_j(A)$|$e^{140360600s}$|
|$\mathscr R_j(A)$|$e^{77127650s}$|
|$\Psi_j$|$e^{242000000s}$|

例如 $B_{w,j},B_{q,j},B_{e,j}$ 在此有限层全部小于 $e^{7000000s}$，
所以 (5.3) 中没有遗漏早期幂源费用。
当前真实 carry 满足
$$
u_{n+5}\ge(1400\cdot16^5-630\cdot8^5)s=1447362560s.
$$
因此
$$
\boxed{
\theta_{n+5}(M_{n+5})\le e^{-1205362560s}<1/2.
}
\tag{7.2}
$$
新目标及原双源可统一取
$$
\boxed{
\|P_{n+5}\|,\|R_{n+5}\|\le e^{243000000s},\qquad
\|\mathbf P_{n+5}\|_{\max}\le e^{244000000s}.
}
\tag{7.3}
$$
这是同一个固定原理想的又一次成功步骤。
第 $n+6$ 位的完整五生成元尾已经由 (6.3) 确定；
其全部目标可用 $e^{487000000s}$、全部原源可用 $e^{488000000s}$ 控制。
下一实际 primitive 输入可取
$$
\boxed{M_{n+6}=e^{248000000s},\qquad \Sigma_{n+6}=e^{249000000s}.}
\tag{7.4}
$$

## 8. 这组标量范数账的增长边界

本节说明当前已付界的逻辑范围，不给实际最优费用下界。

首先，幂关系小参数具有精确可解的增长。
令 $K_j=-\log\kappa_j$，则
$$
K_l=2u_n+u_{n+1}+8\log(n+1),\qquad K_{j+1}=2K_j+u_j.
$$
由原 $u_j=1400\,16^j-630\,8^j+300\,2^j$，
$$
\boxed{
K_j=100\,16^j-105\,8^j+(150j+c_n)2^j,
}
$$
$$
c_n=2^{-l}K_l-100\,8^l+105\,4^l-150l.
\tag{8.1}
$$
所以固定 n 时 $K_j\sim100\,16^j$。
这一式保留原 carry，不用一个任意抽象超小参数替代。

但有限倒数的评价次数随层增长。由 (5.1) 的第一项，主范数幂为
$$
\boxed{M_j^{\,p_j+q_j+d_j-2}=M_j^{\,7d_j/4-2}.}
\tag{8.2}
$$
(6.2) 送回 primitive 时再乘 $M_j$。
若始终采用 (5.2)、(6.2) 给出的这一组标量主上界，
则由于 $F_j,G_j,L_j\ge1$、$\beta_j\le1$，数值上界本身满足
$$
\boxed{
\log M_{j+1}\ge(7d_j/4-1)\log M_j.
}
\tag{8.3}
$$
注意：这是**所选上界序列**的下界，不是实际 $\|v_j\|$ 的下界。
从 $j_0=n+4$ 起 $d_{j_0+k}=16\cdot2^k$，故
$$
\log M_{j_0+k}\ge
(\log M_{j_0})\,27^k\,2^{k(k-1)/2}.
\tag{8.4}
$$
而 $u_{j_0+k}\le1400\,16^{j_0+k}$。
把 (8.4) 代入同一数值上界 (5.1)，其 $\theta_j$ 最终必超过1。
所以不增加实际结构估计时，这套仅由单一范数 M 传递的证明不能认证全层。

目前粗圆整账更早就显示这个界线。
在 (7.4) 后，$j=n+6$ 时 $d=64$，(8.2) 为 $M^{110}$，于是 (5.1) 的数值上界至少为
$$
\eta_{n+6}M_{n+6}^{110}
\ge\exp\big((27280000000-23488102400)s\big)
=\exp(3791897600s)>1.
\tag{8.5}
$$
因此 (7.4) **不能直接认证**再下一步的 Neumann 小量。
(8.5) 没有证明真实 $\|t\Psi\|>1$，也没有排除更小的代表、实际幂范数或其他原双源修正。

本稿的完整递推继续保留了可以改进的位置：
一是实际 primitive $v_j$ 的幂而非单一 $\|v_j\|$ 上界；
二是同一完整尾理想中的更便宜 primitive 代表；
三是原双行的特殊系数允许的其他实际正规化。
这些都必须保原来源、真实单位、完整理想和同一正常锚，不能只由商像相等代替。

