# R271 附录：强物理尾位并头后的同一顶部源流与完整两费预算

日期：2026-11-15（UTC）。作者：Astra-ISP-789f / boundary_core；AI-assisted，GPT-6 Astra Pro。

状态：完整证明。本文对原同一个实际顶部 $u_Q$ 作有限个物理尾位的准确重分组。新左源由原相邻总孔层组成；证明其真正左最小性、完整右链与裸商的准确关系、同一未来的两费预算和原负图条件。没有估计新完整 Schur 逆，没有把新联块源当成原某一个单孔源，也没有支付原普通右费或证明 $N=M$。

依赖：[真正最小投影的带权窗口](R271-appendix-true-minimal-projection-weighted-window.md)、[原完整左核的 primitive 坐标](R271-appendix-full-left-primitive-coordinates-and-boundary-schur.md)、[原首物理头与完整／裸右链](R239-appendix-first-physical-head-quotient-gram-for-left-plus-bare.md)。只使用其中固定有限孔层的纯尾满射及其有界最小逆；不使用全孔直和上有界的 $D^\dagger$。

## 1. 两个孔数和同一个物理算子

固定原 $N/Y$ 模型、$m\ge10$ 和 $d=2^m$，令
$$
L_m=A_m+D_m,\qquad
D_m=\sum_{i\ge m}b_iE_i,\qquad b_i=(i+1)^{-2}.
$$
取任意有限整数 $R\ge0$。将原尾位 $m,\ldots,m+R-1$ 保留为有限物理块，写
$$
D_<:=\sum_{m\le i<m+R}b_iE_i,\qquad
D_>:=\sum_{i\ge m+R}b_iE_i,
$$
$$
\mathcal H_{\mathrm{head}}^C
  =\mathbb C^d\otimes(\mathbb C^2)^{\otimes R},
\qquad C=A_m+D_<,\qquad h=d+R.
\tag{1.1}
$$
两个有限块算子交换；$A_m^d=0$、$D_<^{R+1}=0$，故
$$
C^h=0,\qquad L_m=C+D_>.
\tag{1.2}
$$
这是同一 Hilbert 空间内的张量因子重分组。$C$ 一般不是原 $A_{m+R}$，本文没有把它换成该算子，没有加入或删除 carry。

以 $\mathcal N$ 表示原从第 $m$ 位起的总尾孔数，以 $\mathcal N_>$ 表示第 $m+R$ 位以后的远孔数。前 $R$ 位的孔数 $\mathcal N_<$ 满足
$$
\mathcal N=\mathcal N_<+\mathcal N_>,\qquad 0\le\mathcal N_<\le R.
$$
对应物理正交投影因此有准确包含
$$
P_{\mathcal N\le n}\le P_{\mathcal N_>\le n}
\le P_{\mathcal N\le n+R},
\qquad
P_{\mathcal N_> >n}\le P_{\mathcal N>n}.
\tag{1.3}
$$
特别，远孔支撑 $\le n$ 的向量总孔支撑 $\le n+R$。不能把这两个截断当作相等。

## 2. 原同一个 $u_Q$ 的远孔方程和左最小性

令
$$
4d\le Q\le \exp(c_*d^3),\qquad
c_*=\frac{1601}{64},
$$
并取原同一个 $w\in W$ 及已付真正顶部
$$
u=u_Q=P_{V_{m,Q}}w-P_{K_{m,Q}}w.
\tag{2.1}
$$
因此 $u$ 总孔支撑 $\le Q$，原全部低输出为零，且
$$
u\perp K_{m,Q},\qquad
\|u\|\le\|w\|,\qquad
\|u-P_{\mathcal N\le Q}w\|
\le 2\eta_m\|w\|,\qquad \eta_m=e^{-6d^4}.
\tag{2.2}
$$
这里没有为新分组重新选 $w$、$Q$ 或顶部最小者。

记 $u_n=P_{\mathcal N_>=n}u$；本稿的 $u_n$ 专指远孔层。若 $n+R<Q$，该远孔输出的全部总孔层都严格低于 $Q$，故原低输出方程给
$$
C u_n+D_>u_{n+1}=0
\qquad(0\le n<Q-R).
\tag{2.3}
$$
迭代并使用 (1.2)，得到
$$
D_>^h u_j=0\qquad(0\le j\le Q-R).
\tag{2.4}
$$
当 $j<h$ 时仅由孔数成立；当 $j\ge h$ 时用
$D_>^h u_j=(-C)^h u_{j-h}=0$。所以 (2.4) 没有越过原顶部读取一个不存在的低输出方程。

对远孔 cut $n$，定义真正左空间、源及零源核
$$
\mathscr V_n^C
=\{v:P_{\mathcal N_>\le n}v=v,\
P_{\mathcal N_><n}(C+D_>)v=0\},
\qquad E_n^Cv=Cv_n,
$$
$$
\mathscr R_n^C=E_n^C\mathscr V_n^C,\qquad
\mathscr K_n^C=\ker(C+D_>)\cap\{\mathcal N_>\le n\}.
\tag{2.5}
$$
$\ker E_n^C=\mathscr K_n^C$。固定 $m,R,n$ 时，$\mathscr R_n^C$ 闭且 $E_n^C$ 到它有有界右逆，证明和自然域见 §3。记
$$
U_n^C=(E_n^C)^\dagger,\qquad
L_n^C=(E_n^C(E_n^C)^*)^{-1}.
$$

若 $n+R\le Q$，由 (1.3)
$$
\mathscr K_n^C\subseteq K_{m,Q}.
\tag{2.6}
$$
故 (2.2) 的原正交性给
$P_{\mathcal N_>\le n}u\perp\mathscr K_n^C$。
结合 (2.3)，真实联块源
$$
r_n^C=C u_n
\tag{2.7}
$$
满足
$$
\boxed{
U_n^Cr_n^C=P_{\mathcal N_>\le n}u,\qquad
\mu_n^C(r_n^C)^2
=\|P_{\mathcal N_>\le n}u\|^2.}
\tag{2.8}
$$
这是原同一顶部产生的真正左最小代表，不是选取某个可行左向量后重新假设最小。

还可写明它读取哪些原坐标。将前 $R$ 位的占据集合记为 $I$；令 $u_{p,I}^{\rm old}$ 是原总尾孔数 $p$、该集合恰为 $I$ 的分量，则
$$
(r_n^C)_I
=A_m u_{n+|I|,I}^{\rm old}
+\sum_{\substack{m\le i<m+R\\i\notin I}}
 b_i u_{n+|I|+1,I\cup\{i\}}^{\rm old}.
\tag{2.9}
$$
因此它是总孔层 $n,\ldots,n+R$ 的准确物理联块，还保留强位内部删除项。它不是原单层源 $r_p=A_m u_p^{\rm old}$ 的简单重命名。

## 3. 固定自然域、闭源和完整右链

以下所有尾算子只作用第 $m+R$ 位以后的原 Boolean 空间。置
$$
E_{a,j}^{>}=\ker D_>^a\cap\mathcal H_j^{>},
\qquad E_{0,j}^{>}=\{0\}.
$$
原固定孔层满射结论同样适用于平移后的连续尾 $D_>$。在本稿每一个固定 $m,R,n$ 中，只使用有限多个孔层 $0,\ldots,n+h$ 的最小逆及真幂最小逆；这些各自在其完整固定层上有界。不给这些界作 $m,R,n$ 一致声明。

为核闭源，可对有限矩阵 $C$ 取任意固定 Jordan 相似，块长为
$\ell_\gamma\le h$，对应链向量为 $v_{\gamma,i}$，
$C v_{\gamma,i}=v_{\gamma,i-1}$。
同一低输出递推逐块给准确源
$$
\mathscr R_n^C
=\bigoplus_\gamma\ \bigoplus_{i=0}^{\ell_\gamma-2}
v_{\gamma,i}\,E_{\ell_\gamma-i-1,n}^{>}.
\tag{3.1}
$$
这里直和表示该有限可逆头变换下的直和；它一般不是物理正交直和。各尾核闭，有限头变换有界可逆，故 (3.1) 闭。原首头构造中取固定层 $(D_>^j)^\dagger$ 的明确右逆，逐块应用后给 $E_n^C$ 的有界右逆。本文没有估计或使用这个 Jordan 相似的条件数。

另一种只用于存在性的完整延伸是：对 $v\in\mathscr V_n^C$，取每层 primitive 坐标 $p_j=P_{\ker D_>}v_j$，沿固定层顺次最小逆 $Q_t$，则
$$
\mathcal Z_Cp=\sum_{t=0}^{h-1}(-C)^tQ_tp
\tag{3.2}
$$
满足 $(C+D_>)\mathcal Z_Cp=0$，其低远孔截断就是 $v$，支撑不超过 $n+h-1$。这由
$D_>Q_t=Q_{t-1}$、$P_{\ker D_>}Q_t=0$ 及 $C^h=0$ 的有限望远镜直接得到。这里只用有限层的顺次逆，不将其当作真幂 MP 逆，也不宣称 (3.2) 的范数小。

完整右链使用同一个统一宽度 $h$，保全部段及原物理内积。令 $\mathcal Y_{n,h}^{C,\rm full}$ 为所有 $c=(c_1,\ldots,c_h)$，满足
$$
c_j\in \ker C^{h-j+1}\otimes E_{h,n+j}^{>},
\qquad
C c_j+D_>c_{j+1}=0\ (1\le j<h),\qquad Cc_h=0,
$$
$$
F_nc:=D_>c_1\in\mathscr R_n^C.
\tag{3.3}
$$
该空间闭。统一保 $h$ 段，不把非正交 Jordan 块各自截到其最短长度后删掉物理交叉。

(3.2) 给每个 $r\in\mathscr R_n^C$ 的同源完整右候选，因此
$F_n:\mathcal Y_{n,h}^{C,\rm full}\to\mathscr R_n^C$ 有界满射。定义
$$
G_n^C=F_nF_n^*,\qquad
\lambda_n^C(r)^2=\langle(G_n^C)^{-1}r,r\rangle.
\tag{3.4}
$$
伴随在 (3.3) 的完整右核与原物理内积中取。完整最小链为
$F_n^\dagger r$，不先压一个较小 primitive 族。

这些自然旗也可直接由完整物理核核查：把任意左可行 $v$ 与负的同源完整链 $-c$ 拼合，得到有限支撑的 $(C+D_>)$ 核。终端向左递推强制
$C^{h-j+1}c_j=0$；完整核的逐孔递推强制 $D_>^hc_j=0$。故 (3.3) 保的是同一物理完整链，并非额外扩大某个受限逆域。

## 4. 真裸商及完整高返回不被删除

在第 $j$ 段取原正交低投影
$$
P_j^{\rm lo}=I-P_{E_{j-1,n+j}^{>}}.
$$
未来高出生直和 $\bigoplus_{j=1}^h E_{j-1,n+j}^{>}$ 对头算子 $C$ 及向左删除 $D_>$ 共同不变；第一段高空间为零。

定义裸链空间 $\mathcal Y_{n,h}^{C,\rm bare}$ 为满足
$$
b_j\in\ker C^{h-j+1}\otimes
       (E_{h,n+j}^{>}\cap E_{j-1,n+j}^{>\perp}),
$$
$$
C b_j+P_j^{\rm lo}D_>b_{j+1}=0\ (1\le j<h),
\qquad Cb_h=0,\qquad F_n^b b=D_>b_1\in\mathscr R_n^C
\tag{4.1}
$$
的全部链。它是闭 Hilbert 子空间。

投影 $c_j\mapsto P_j^{\rm lo}c_j$ 将 (3.3) 送到 (4.1)，源不变。反向也必须付清存在性。给 (4.1) 的 $b$，置
$$
k_j=C b_j+D_>b_{j+1}\in E_{j-1,n+j}^{>}
\quad(1\le j<h),\qquad k_1=0.
$$
又 $k_j\in\ker C^{h-j}$。依次取
$$
y_1=0,\qquad
y_{j+1}=-(D_>|_{\mathcal H_{n+j+1}^{>}})^\dagger
             (k_j+C y_j).
\tag{4.2}
$$
固定层右逆在头上为单位。归纳给
$$
y_j\in E_{j-1,n+j}^{>}\cap\ker C^{h-j+1}.
$$
确实，输入属于 $E_{j-1}^{>}\cap\ker C^{h-j}$，其最小原像属于
$E_j^{>}\cap\ker C^{h-j}$。因此 $c=b+y$ 满足全部完整内部方程，
$Cy_h=0$、$Cb_h=0$ 给真末端封口，且 $D_>c_1=D_>b_1$。这证明准确的满射
$$
P^{\rm lo}\mathcal Y_{n,h}^{C,\rm full}
=\mathcal Y_{n,h}^{C,\rm bare}.
\tag{4.3}
$$
这里只证明有限层 (4.2) 的有界性；没有给其统一小费用。特别不能由 (4.3) 把最小完整链的高返回平方置零。

定义
$$
B_n^C=(F_n^b(F_n^b)^*)^{-1},\qquad
\alpha_n^C(r)^2=\langle B_n^Cr,r\rangle.
\tag{4.4}
$$
因 $F_n^b$ 有界满射，这些是完整源上的有界严格正算子。准确两费为
$$
\operatorname{flat}_n^C(r)^2
=\langle G_n^C L_n^C r,L_n^C r\rangle,\qquad
\Xi_n^C(r)^2=\alpha_n^C(r)^2+\operatorname{flat}_n^C(r)^2.
\tag{4.5}
$$
普通 $\lambda_n^C$ 与已付裸 $\alpha_n^C$ 始终分开；全部因子次序保留。

## 5. 同一未来同时支付 bare 与 flat

以下取
$$
0\le n,\qquad n+h+R<Q,
\qquad
Y_n=(u_{n+1},\ldots,u_{n+h}).
\tag{5.1}
$$
这个严格不等式保证 (2.3) 还可读到远孔 $n+h$ 行，即可使用真实
$u_{n+h+1}$，而其远孔层不超过 $Q-R$。

先置
$$
b_{n,j}=-P_j^{\rm lo}u_{n+j}.
\tag{5.2}
$$
由 (2.4)，它在 $E_h^{>}$ 中。对 $1\le j\le h$，(2.3) 给
$$
C^{h-j+1}u_{n+j}
=(-D_>)^{h-j+1}u_{n+h+1}\in E_{j-1,n+j}^{>}.
$$
因而 $C^{h-j+1}b_{n,j}=0$。共同高出生商将 (2.3) 变成 (4.1) 的全部内部方程；第一段没有高商，故
$$
D_>b_{n,1}=-D_>u_{n+1}=C u_n=r_n^C.
$$
末端准确是
$$
C b_{n,h}
=-P_h^{\rm lo}C u_{n+h}
=P_h^{\rm lo}D_>u_{n+h+1}=0,
\tag{5.3}
$$
因为 (2.4) 给 $D_>u_{n+h+1}\in E_{h-1}^{>}$。没有以形式幂零或一个不存在的顶部方程替代这一步。

所以 (5.2) 是同源真裸候选，得到
$$
\boxed{\alpha_n^C(r_n^C)^2\le\|b_n\|^2\le\|Y_n\|^2.}
\tag{5.4}
$$

对 flat，任取 $c\in\mathcal Y_{n,h}^{C,\rm full}$，写 $z=F_nc$。
把 $U_n^Cz$ 与 $-c$ 拼合，得到真正 $(C+D_>)$ 核。它远孔支撑
$\le n+h$，总孔支撑 $\le n+h+R<Q$，因此属于原 $K_{m,Q}$。
由原 $u\perp K_{m,Q}$ 与 (2.8)，
$$
\langle L_n^Cr_n^C,F_nc\rangle=\langle Y_n,c\rangle.
$$
于是有完整物理投影身份
$$
\boxed{
F_n^*L_n^Cr_n^C
=P_{\mathcal Y_{n,h}^{C,\rm full}}Y_n,
\qquad
\operatorname{flat}_n^C(r_n^C)^2
\le\|Y_n\|^2.}
\tag{5.5}
$$
该投影保留全部右零源自由量和完整高返回。合并即得
$$
\boxed{\Xi_n^C(r_n^C)^2\le2\|Y_n\|^2.}
\tag{5.6}
$$

还保留真实负图。令
$$
X_{0,n}^C=\mathscr R_n^C\cap
         (\ker C\otimes\mathcal H_n^{>}).
$$
对 $z\in X_{0,n}^C$，单段链
$c_1=D_>^\dagger z,\ c_j=0\ (j>1)$
同时是完整与裸的最小链：第一段范数已达到 $D_>c_1=z$ 的最小值，其余段为零。它在 $\ker C$ 中，全部自然旗满足。利用 (5.2) 的同源性及裸最小者对零源链的正交，得到
$$
\langle B_n^Cr_n^C,z\rangle=-\langle Y_n,c(z)\rangle.
$$
与 (5.5) 相加：
$$
\boxed{
(L_n^C+B_n^C)r_n^C\perp X_{0,n}^C.}
\tag{5.7}
$$
这是新联块的准确负图正规方程。它不是 $r_n^C$ 的头支撑结论，也没有把 $M_3/M_2$ 度量正交换成坐标消失。

## 6. 全部 cut 与不交网格的同源总预算

取整数 $n_0\ge0$，令
$$
\mathcal I=\{n:n_0\le n\le Q-R-h-1\},\qquad
N_{\rm cut}=Q-R-h-n_0,
$$
并假设 $N_{\rm cut}>0$。每个远孔层在 $Y_n$ 中至多出现 $h$ 次，因此
$$
\boxed{
\sum_{n\in\mathcal I}\Xi_n^C(r_n^C)^2
\le2h\,\|P_{\mathcal N_> >n_0}u\|^2.}
\tag{6.1}
$$
对同一余数类的网格 $n=n_0+kh$，未来带两两正交，故还有
$$
\boxed{
\sum_{\substack{n\in\mathcal I\\n\equiv n_0\pmod h}}
\Xi_n^C(r_n^C)^2
\le2\,\|P_{\mathcal N_> >n_0}u\|^2.}
\tag{6.2}
$$
不在不同 cut 重选来源，也不累计 $N_{\rm cut}$ 次母误差。

以 $\mathcal N_{\rm all}$ 记原所有物理位的总孔数，并置
$$
\tau=\|\mathbf1_{\{\mathcal N_{\rm all}>n_0\}}w\|,
\qquad \beta=\tau+2\eta_m\|w\|.
$$
由 (1.3)、(2.2)，
$$
\|P_{\mathcal N_> >n_0}u\|\le\beta,
$$
而对所有 $n\in\mathcal I$，
$$
\boxed{
\mu_n^C(r_n^C)\ge\|w\|-\beta,\qquad
\sum_{n\in\mathcal I}\Xi_n^C(r_n^C)^2\le2h\beta^2.}
\tag{6.3}
$$
这里 $P_{\mathcal N_>\le n}$ 的物理像支撑 $\le n+R\le Q$，所以对低部分的 (2.2) 误差正是 $2\eta_m$，未引入某个新的未知截断误差。

## 7. 强位数为逆芽尺度时的准确剩余门槛

可取固定常数 $c_0>1$，
$$
\rho_m=e^{-25d^3/2},\qquad
R_m=\lceil c_0\rho_m^{-1}\rceil,\qquad
h_m=d+R_m,\qquad n_0=4h_m,
$$
$$
Q_m=\lfloor e^{c_*d^3}\rfloor.
\tag{7.1}
$$
则
$$
\|D_>\|\le\sum_{i\ge m+R_m}(i+1)^{-2}
\le\frac1{m+R_m}<\rho_m/c_0.
\tag{7.2}
$$
同时 $R_m+h_m+n_0=o(Q_m)$，所以 (6.3) 有
$N_{\rm cut}\sim Q_m$；固定 $w$ 时 $n_0\to\infty$，故 $\beta_m\to0$。

若后续在这些同一实际联块源上证明
$$
\mu_n^C(r_n^C)^2\le\kappa_m\,\Xi_n^C(r_n^C)^2
\qquad(n\in\mathcal I),
\tag{7.3}
$$
则 (6.3) 给
$$
N_{\rm cut}(\|w\|-\beta_m)^2
\le2\kappa_m h_m\beta_m^2.
\tag{7.4}
$$
因此 $\kappa_m h_m/N_{\rm cut}=O(1)$ 已是足够门槛。特别
$\kappa_m=O(\rho_m^{-1})$ 将给
$$
\frac{\kappa_m h_m}{N_{\rm cut}}
=O\!\left(\frac{\rho_m^{-2}}{Q_m}\right)
=O(e^{-d^3/64})\longrightarrow0.
\tag{7.5}
$$

本文只支付 (2.8)、(4.3)、(5.4)–(6.3) 及该准确量级转换；(7.3) 未证明。
尤其 (7.2) 不能独自控制 $C$ 的完整物理最小逆：强位的全部 nuisance、左 Schur 和高返回仍必须保留。新 $\lambda_n^C$ 的物理链也可跨越多个原总孔层，不能据此声称原某个单源 $r_p$ 的普通 $\lambda_{m,p}$ 已受控制。这里提供的是保同 $w$、同 $u_Q$、全部完整右自由量的实际扩块比较入口。
