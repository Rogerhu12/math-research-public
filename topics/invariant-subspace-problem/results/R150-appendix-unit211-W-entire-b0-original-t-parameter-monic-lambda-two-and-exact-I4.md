# R150 附录：整个 W/b0 的原 t 参数首一 lambda 二次与完整两列均值环境

- 会话：Astra-ISP-8542378f-20261127。
- 日期：2026-11-28（Asia/Taipei）。
- 状态：完整纸面原恒等证明，无新增数学执行。
- 范围：当前正确 W、distinct-singleton、物理 $D\ne0$ 的既有权图，并施加 $b_0=0$。只使用此图已经独立支付的权单位。
- 新结论：存在原三均值的纯权组合
  $q_\lambda=\lambda^2-a(t)\lambda-b(t)$，
  其中 $\deg_ta\le1$、$\deg_tb\le2$。原 $I_4$ 在这个首一二次环境中有精确八行二列呈示；加入完整 NS/PS 后有精确十二行二列呈示。没有对原商作自由假设，没有增加权头或几何首项的逆。

## 1. 原量与已经支付的分母

沿[整个 W 的同 f 原四式与唯一恢复](R150-appendix-unit211-W-original-I4-six-rows-entire-paid-f-head-and-unique-recovery.md)及[整个 b0 的原权曲线与恢复](R150-appendix-unit211-W-entire-b0-two-original-curves-5772-weights-46176-normalized-points.md)，记

$$
p+q=2,\quad pq=Q,\quad \rho=(p-q)/2,\quad
\delta=\rho^2=1-Q,
$$

$$
u=bp+cq,\quad \ell=b+c,\quad m=u-\ell,\quad
M=4bc\delta,\quad V=bX+cY,\quad W_1=bpX+cqY,
$$

$$
s=u-1,\quad T_0=2u-\ell Q-2u^2,\quad
J=2u(1-u)+\ell Q,\quad P_f=T_0(J-Q),
$$

$$
\Phi=T_0+4u-4+Q,\qquad
P_{02}=(2-3u)(2u-\ell Q)-Qu+2u^3.
\tag{1}
$$

原 $u,Q,\delta,bc,M,P_{02},P_f,\Phi$ 均在当前 W 图已付；$m$ 来自正确原等权排除，仍只用于其既有 distinct-singleton、$D\ne0$ 范围。

本条还使用 $2\ell-1$，其准确出处是[整个 W/Lhalf 的完整原排除](R150-appendix-unit211-W-entire-Lhalf-complete-original-exclusion.md)。引用的是整支终证，而非先行的 D/F101 必要覆盖。该终证的三原来源与所有权单位已经独立核清为真正 dual 乘法链，不来自撤回的 compact 一阶平方。

$b_0$ 的定义为

$$
b_0=2m\{A_*T+uQ(3-2\lambda)\ell\},\qquad A_*=4uQ-J.
$$

当前 b0 已刊原返回支付 $A_*$：若它为零，则原 $b_0=0$ 与已付 $muQ\ell$ 迫 $\lambda=3/2$，落既有完整原排除。因此

$$
\kappa=\frac{uQ\ell}{A_*},\qquad T=2\kappa\lambda-3\kappa.
\tag{2}
$$

在逆权坐标 $(u,\nu)$ 中，$A_*=uQ(\nu+2)$、$\kappa=\ell/(\nu+2)$。这里 $\nu+2$ 只在 b0 已付图使用，不外推整个 W。

以下 $A$ 表示同一已付纯权环。采用 $(u,\nu)$ 时，原正反权图的 $d=u\nu-(2u-1)$、$r=2u-1-\nu$ 也按原定义局部化。本条没有新增需要排除的权因子。

## 2. 一般 W 的准确仿射恢复：保留 Phi 修正

原 $E_0,N_0,P_1$ 在当前图给

$$
W_1=T_0/2+2uf,\qquad
QV=Jf-\lambda P_{02}-sT_0+bcQt,
\tag{3}
$$

$$
P_ff+QP_{02}(\ell+T)-(\lambda P_{02}+sT_0)T_0
+bcQ\Phi t=0.
\tag{4}
$$

因此固定 $t$ 时，

$$
\boxed{
\lambda=\frac{Jf-QV+bcQt-sT_0}{P_{02}},\qquad
T=-\ell+\frac{T_0(f-V)+bc(T_0-\Phi)t}{P_{02}}.
}
\tag{5}
$$

第二式中的 $-\Phi$ 项属于一般 W 原式，不能使用 $\Phi=0$ 专属恢复式替换它。

从 $(f,V)$ 到 $(\lambda,T)$ 的线性行列式为

$$
\det\frac{\partial(\lambda,T)}{\partial(f,V)}
=-\frac{P_f}{P_{02}^2}\in A^\times.
\tag{6}
$$

所以 (5) 是 $A[t]$ 上的双向仿射坐标变换。由 (2) 得整个 b0 上的显式恢复

$$
\boxed{
f=
\frac{
P_{02}(T_0-2\kappa Q)\lambda
+sT_0^2-QP_{02}(\ell-3\kappa)
-bcQ\Phi t
}{P_f},
}
\tag{7}
$$

$$
\boxed{
V=\frac{Jf-\lambda P_{02}-sT_0+bcQt}{Q}.
}
\tag{8}
$$

二者都是 $\lambda,t$ 的仿射式，全部系数只在 $A$ 中。式 (7) 的 $t$ 系数为 $-bcQ\Phi/P_f$，是当前 W 的旧权单位。因此从旧 b0 的 $(\lambda,f)$ 到新的 $(\lambda,t)$ 也是真正双向仿射变换；逆式正是由 (4) 解原 $t$。没有丢失旧原四式的任何分支。

原 $X,Y$ 和全部 Gram 条目则仍由

$$
X=\frac{W_1-qV}{b(p-q)},\qquad
Y=\frac{pV-W_1}{c(p-q)}
\tag{9}
$$

唯一恢复。在不选择 $\rho$ 根的原偶奇系数环中，等价地

$$
X=x+\rho y,\quad Y=x-\rho y,\qquad
x=\frac{(u-\ell Q)V-mW_1}{M},\quad
y=\frac{\ell W_1-uV}{M},
$$

$$
A_1=2f-2V+2bct,\quad
r_B=X-(1-\ell)p-ct,\quad
r_C=Y-(1-\ell)q-bt.
\tag{10}
$$

因此本条所有换元都保持同一个原 Gram 点。

## 3. 固定 t 的三个真均值头

保留 $t$ 为系数参数，令

$$
\mathcal R=
4(f-u)(V-f)+bct^2+
t\left(4bcu-\ell V+
\frac{m}{2\delta}(T_0+4uf-2V)\right).
\tag{11}
$$

由完整正确 dual 乘法，在已恢复的 $E_0=0$ 图上有普通多项式身份

$$
2\mathcal R+E_1-bE_B-cE_C=0.
\tag{12}
$$

特别是 germ 平方的一阶分量为 $2d_0d_1$；(12) 的来源没有使用错误的 $d_1^2$ 代换。自由原来源见[整个 W 的原 alpha/chi 坐标](R150-appendix-unit211-W-global-original-alpha-chi-polynomial-coordinates.md)中先于 W 权特化的均值恒等式。

令 $E_{B,e}=(E_B+E_C)/2$、$E_{B,o}=(E_B-E_C)/(2\rho)$，于是

$$
bE_B+cE_C=\ell E_{B,e}+mE_{B,o},
$$

$$
\mathcal E=
\begin{pmatrix}\mathcal R\\E_{B,e}\\E_{B,o}\end{pmatrix}
=
C\begin{pmatrix}E_1\\E_{B,e}\\E_{B,o}\end{pmatrix},
\quad
C=\begin{pmatrix}
-1/2&\ell/2&m/2\\0&1&0\\0&0&1
\end{pmatrix}.
\tag{13}
$$

$C$ 是纯权可逆矩阵；$E_1$ 始终作为真实独立均值保留。

三个式子对 $(f,V)$ 都是二次。其二次头矩阵 $H$ 按列 $(f^2,fV,V^2)$ 定义，且

$$
\boxed{\det H=\frac{32uQ(2\ell-1)}{M^2}\in A^\times.}
\tag{14}
$$

为明确 (14) 不依赖 $\Phi=0$，给出完整头计算。设 $\Delta=p-q$，

$$
\alpha=\frac{2u}{b\Delta},\quad
\beta=-\frac q{b\Delta},\quad
\gamma=-\frac{2u}{c\Delta},\quad
\eta=\frac p{c\Delta}.
$$

则 $X^{[1]}=\alpha f+\beta V$、$Y^{[1]}=\gamma f+\eta V$。真原均值的固定 t 二次部为

$$
\mathcal R^{[2]}=4f(V-f),
$$

$$
E_B^{[2]}=-2(\alpha f+\beta V)^2+4f(\alpha f+\beta V),
$$

$$
E_C^{[2]}=-2(\gamma f+\eta V)^2+4f(\gamma f+\eta V).
$$

设 $S=\alpha+\beta$、$U=\gamma+\eta$，直接展开得

$$
\det H_{\mathcal R,B,C}
=-16\{\beta^2U(2-U)-\eta^2S(2-S)\}.
$$

原 $u=bp+cq$ 给

$$
2c\Delta-p+2u=p(2\ell-1),\qquad
2b\Delta-2u+q=-q(2\ell-1),
$$

所以括号共同分子为

$$
q^2(p-2u)(2c\Delta-p+2u)
-p^2(2u-q)(2b\Delta-2u+q)
=2uQ(2\ell-1)\Delta.
$$

再由 $(E_B,E_C)$ 到偶奇行的行列式 $-1/(2\rho)$，以及 $\Delta=2\rho$、$M=4bc\delta$，得到 (14)。整个计算未使用 $\Phi$ 权关系。

这些偶奇系数都在 $A$ 中；在 $\rho^2=\delta$ 的首一二次扩张中完成的显示身份也准确降回 $A$，没有选择某个符号的 $\rho$。同一自由头另见[正确 Phi 的 t 参数三生成纸证](R150-appendix-unit211-Phi-zero-corrected-whole-t-parameter-three-mean-generators-and-monic-lambda-cubic.md)；本篇只引用其通用头计算，不借用 Phi 的权支付或恢复式。

## 4. 三个二次乘积的完整原回写

把 (13) 的三均值写成

$$
\mathcal E
=
H\begin{pmatrix}f^2\\fV\\V^2\end{pmatrix}
+L(t)\begin{pmatrix}1\\f\\V\end{pmatrix}.
$$

由 (14)，定义

$$
\mathbf r=-H^{-1}L(t)\begin{pmatrix}1\\f\\V\end{pmatrix}.
$$

则有完整普通多项式身份

$$
\boxed{
\begin{pmatrix}f^2\\fV\\V^2\end{pmatrix}
-\mathbf r=H^{-1}\mathcal E.
}
\tag{15}
$$

$\mathbf r$ 的每一项对 $f,V$ 仿射；常数系数的 $t$ 次数至多二，$f,V$ 系数的 $t$ 次数至多一。理由是原三均值对 $(f,V,t)$ 的总次数至多二，而 $H$ 完全是纯权矩阵。

(15) 是原三均值的完整来源定义，不是仅在某个域或一组数值解上降次，也不要求 $1,f,V$ 在原商里自由。

## 5. 新的整个 b0 首一 lambda 二次

置

$$
j_f=\frac J{P_{02}},\qquad j_V=-\frac Q{P_{02}},\qquad
c(t)=\frac{bcQt-sT_0}{P_{02}},\qquad
\mathbf w=(j_f^2,2j_fj_V,j_V^2).
$$

由 (5)，

$$
\lambda=j_ff+j_VV+c(t).
$$

先不使用任何原均值，将这个准确坐标身份平方，并用 (15) 得

$$
\lambda^2-\{\mathbf w\mathbf r+2c(t)\lambda-c(t)^2\}
=\mathbf wH^{-1}\mathcal E.
\tag{16}
$$

现在施加 b0 的准确仿射恢复 (7)–(8)。因 $\mathbf r$ 对 $f,V$ 仿射，(16) 大括号对 $\lambda$ 至多一次，因此唯一写成

$$
\mathbf w\mathbf r+2c(t)\lambda-c(t)^2=a(t)\lambda+b(t),
$$

其中

$$
a,b\in A[t],\qquad \deg_ta\le1,\quad \deg_tb\le2.
\tag{17}
$$

于是

$$
\boxed{
q_\lambda(\lambda,t)=\lambda^2-a(t)\lambda-b(t)
=\frac{(J^2,-2JQ,Q^2)}{P_{02}^2}\,
H^{-1}C
\begin{pmatrix}E_1\\E_{B,e}\\E_{B,o}\end{pmatrix}.
}
\tag{18}
$$

右侧各原式都在同一 b0 仿射坐标中。乘子是纯权行，不含 $\lambda,t,f,V$；其全部分母属于已经列明的旧权单位。式 (18) 的 $\lambda^2$ 系数准确为 1，不是“某非零头”或一个只在补图非零的系数。

本条没有选取并反演一个单独原均值的 $\lambda^2$ 头，没有使用交叉头补图，也不依赖新三常数域执行。它来自整个三头矩阵的已付行列式与同点坐标恒等式。

## 6. 同一个原 I4 的八行二列精确呈示

在新 $A[\lambda,t]$ 坐标中，记

$$
F_1=E_1,\quad F_2=E_{B,e},\quad
F_3=E_{B,o},\quad F_4=N_1.
$$

前三均值为总次数至多二；完整极化 $N_1$ 也为总次数至多二：原 $v_0$ 对几何变量常数、$v_1$ 仿射，完整 $N_4(v_0+v_1)-N_4(v_0)-N_4(v_1)$ 的混合部至多二，减去的 $4\lambda(\lambda-1-T)P_{02}$ 仍为二次。没有改用 $N_1$ 的部分或最高项。

令

$$
h_i=[\lambda^2]F_i\in A,\qquad
r_i=F_i-h_iq_\lambda=A_i(t)+B_i(t)\lambda.
\tag{19}
$$

因总次数至多二，

$$
\deg_tA_i\le2,\qquad \deg_tB_i\le1.
$$

由 (18)，$q_\lambda\in(F_1,F_2,F_3)$；由 (19)，反向每个 $F_i=h_iq_\lambda+r_i$。所以完整原理想具有双向等式

$$
\boxed{I_4=(F_1,F_2,F_3,F_4)
=(q_\lambda,r_1,r_2,r_3,r_4).}
\tag{20}
$$

这里不需要某个 $h_i$ 为单位。

首一环境

$$
B=A[t][\lambda]/(q_\lambda)
$$

是自由二坐标环境，基为 $(1,\lambda)$；原方程商是它的进一步商，未被假设自由。在 $B$ 中，理想 $(r_i)$ 作为 $A[t]$ 模恰由八行生成：

$$
(A_i,B_i),\qquad (bB_i,A_i+aB_i),\qquad 1\le i\le4.
\tag{21}
$$

它们的完整原来源分别为 $r_i$ 与 $\lambda r_i-B_iq_\lambda$，因为

$$
\lambda r_i-\{bB_i+(A_i+aB_i)\lambda\}=B_iq_\lambda.
\tag{22}
$$

因此 (21) 是原 $I_4$ 的精确呈示，不只是同点必要秩条件。原均值商在 $A[t]$ 上至多二生成，但未宣称其自由秩等于二。

## 7. 完整 NS/PS 与十二行二列呈示

在同一仿射原 Gram 中，完整加权 NS、PS 的总 $(\lambda,t)$ 次数至多三。对任意一个 $F\in\{NS,PS\}$，只用首一式 (18) 作唯一普通除法：

$$
F=Q_Fq_\lambda+A_F(t)+B_F(t)\lambda.
\tag{23}
$$

由于 (17) 的总次数界，降次不增加总次数，因此

$$
\deg_tA_F\le3,\qquad \deg_tB_F\le2.
$$

把这两条余式及其 $\lambda$ 倍加入 (21)，得到十二行二列的精确原 $I_6$ 呈示。每条新行的来源仍是完整 $F$ 与原三均值组合 (18)，不把部分 NS/PS 或一个标量 cofactor 当充分条件。

完整个别 N/P 与 NV 尚须继续同点加入；本篇没有展开或执行这些新余式，也没有宣称已经实际算出十二行系数、它们的 cofactor 或新的权曲线。这里给出的是它们完整、可再生的原代数定义与双向证明。

## 8. 全范围与后继接口

本条出现的分母可以逐层追踪：

1. $X,Y$ 的原偶奇恢复只用 $\delta,M$，或在首一二次扩张中用已付 $b,c,p-q$；
2. 原 $E_0/N_0/P_1$ 换元使用 $P_{02},P_f,Q$；与旧 $(\lambda,f)$ 图双向互换还用旧 $\Phi,bc$；
3. b0 的 $T$ 恢复只增加本支已经支付的 $A_*=uQ(\nu+2)$；
4. 三均值头逆只用原 $\delta,M$ 以及 $uQ(2\ell-1)$；
5. $\lambda$ 首一化与后面的所有短除法不增加任何分母。

原权坐标本身的旧分母仍按 $A$ 的定义保留。没有倒 $t,\lambda,D$、原个别均值头、叉积某一项或它们的范数。未知权头零支从未被删掉；$t=0$、$\lambda$ 特殊值等形式纤维也都留在多项式身份中，物理图的既有排除另行适用。

这是在 $A[t]$ 上的二生成环境，不因而宣称对纯权环 $A$ 有限。物理 $D\ne0$ 等几何局部化不能不经证明地保留该有限模性质；(18)–(23) 先在尚未反演这些几何量的必要原多项式商中成立，实际物理点继承这些关系。

本篇没有新的执行回执，没有复跑旧 qf、三头投影、全 G5、五三次、C2/Loww、冻结 PRS 或任何旧矩阵门。后继唯一新的计算可直接构造 (18) 的必要系数和原 $N_1$/NS/PS 余式，再决定原值消元；尚未运行的内容不记为完成。

所有有限性讨论只涉及这里明确的规范比值/Gram 坐标。没有在本条加入原 $U_0$ 三次尺度，也不把这些坐标的生成数外推为未规范化算子的计数。
