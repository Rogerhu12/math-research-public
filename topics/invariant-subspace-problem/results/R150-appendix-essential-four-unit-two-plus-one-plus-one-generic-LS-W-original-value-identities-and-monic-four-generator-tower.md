# R150：全余 W 的原值身份与单首一四生成模型

会话：Astra-ISP-8542378f-20261127。日期：2026-11-27。

## 1. 已成几何二次式与同点值坐标

沿用已刊全余 W 的真实原组合
$$
q_Y=Y^2+\mathcal A(w)Y+\mathcal C(w),
$$
及其同点 $\lambda,T,f,x,y,t$。$Y=y-1$ 已付；$u,\ell,M=4bc(1-Q)$ 等参数单位都有此前完整原出处。仍保留原物理
$$
D=\ell A_\lambda-T^2,\quad
A_\lambda=2\lambda^2-2\lambda+1,\quad
B_\lambda=4\lambda^3-6\lambda^2+3\lambda-1.
$$

采用旧原值式的可逆中心
$$
s=(\ell\zeta-T)/u=-v_1,\qquad m=u-\ell,
$$
$$
v_0=(T+ms)/\ell,\qquad
\zeta=(T+us)/\ell,
$$
$$
h=1+v_0-rs,\quad k_U=1+v_0+rs,\quad r^2=1-Q.
$$
$k_U$ 是原谱值，不与权坐标 k 混同。这只是已刊原值坐标的代入，不另将通用矩身份登记为新的排空。它在本页 W 输入中实际重新乘回，未倒置几何 D。

令
$$
V=(1,\lambda-1-T,h,k_U),\qquad
E_2=\tau(V^2)-2\lambda^2,\quad
E_3=\tau(V^3)-4\lambda^3.
$$
同一个完整原 Gram 与正确双点乘法实际给
$$
\tau(V)=\lambda,\qquad \ell E_2=Ms^2-D, \tag{1}
$$
以及
$$
K-2mDs=\ell(2ms+3\ell+3T)E_2-\ell^2E_3,\quad
K=\ell^2B_\lambda-3\ell T A_\lambda+2T^3. \tag{2}
$$
原 $H_A,H_B$ 与上述两个矩的既有完整身份也实际核验，因此本页的值中心不是额外猜测等式。

## 2. 第二条单首一式及四个生成元

从已成 $q_Y$ 作准确二次除法：
$$
D=d_2q_Y+D_{\rm lin},\qquad D_{\rm lin}=D_0(w)+D_1(w)Y.
$$
由 (1) 得
$$
q_s=s^2-D_{\rm lin}/M
=\frac{\ell}{M}E_2+\frac{d_2}{M}q_Y. \tag{3}
$$
(3) 是本次实际乘回的完整原组合。所有比例分母为已付参数；没有付 $D_{\rm lin}$ 或 D 的范数。反向同样由 (3) 恢复 E2，故没有删除值零面。

两条单首一规则给整个原值输入的规范四生成形式
$$
1,\quad Y,\quad s,\quad Ys.
$$
任何多项式先按 $s^2=D_{\rm lin}/M$ 约化，再按
$Y^2=-\mathcal A Y-\mathcal C$ 约化；过程不需新首项逆。原最终商只宣生成，不假设自由。

记 $h_0=D_0/M,h_1=D_1/M$。真实值列上乘法的符号公式为
$$
M_Y=
\begin{pmatrix}
0&1&0&0\\-\mathcal C&-\mathcal A&0&0\\
0&0&0&1\\0&0&-\mathcal C&-\mathcal A
\end{pmatrix},
$$
$$
M_s=
\begin{pmatrix}
0&0&1&0\\0&0&0&1\\
h_0&h_1&0&0\\-\mathcal C h_1&h_0-\mathcal A h_1&0&0
\end{pmatrix}. \tag{4}
$$
(4) 逐行就是两条单首一关系；它不要求最终原四个生成元线性独立。本次执行没有完成 (4) 的全部展开系数及其后 20 行乘法检查，准确执行边界见第 5 节。

## 3. 原 Delta、相容条件和完整 N4(V) 纠正

本页始终在原 $\Delta=0,W=0$ 分支。沿用
$$
S=2v_0+3-2\lambda,\quad z=(h-1)(k_U-1),\quad
G=\lambda P_{02}-(1-u)T_0,
$$
$$
P_f=T_0(J-Q),\quad P_t=bcQ\Phi,\quad
P_c=QP_{02}(\ell+T)-GT_0,
$$
$$
N_f=(3-4\lambda)Q-Jz+S(2uQv_1+\zeta J),\quad
N_t=bcQS\zeta,
$$
$$
R_1=u(3-2\lambda+v_0+v_1)-\ell Qv_1,
$$
$$
N_c=G(z-S\zeta)+\tfrac12SQT_0v_1
+Q(\lambda-1-T)R_1.
$$
完整原式在本次新坐标中实际返回
$$
P_ff+P_tt+P_c=0,
$$
$$
\frac Q2N_4(V)=N_ff+N_tt+N_c-\frac{Qf}{u^2}H_A. \tag{5}
$$
尤其保留 (5) 中曾经容易遗漏的原第二矩倍数。

定义
$$
E_\Delta=\Phi N_f-S\zeta P_f,\qquad
E_C=\Phi N_c-S\zeta P_c.
$$
实际核
$$
fE_\Delta+E_C
=\Phi\left(\tfrac Q2N_4(V)+\frac{Qf}{u^2}H_A\right). \tag{6}
$$
在当前原 Delta 零分支，必须分别保留 $E_\Delta=E_C=0$。在一般尚未分 Delta 的 LS 图，(6) 只是保留原 N4(V) 与 H_A 的准确组合身份；只有 Phi 非零且原矩成立时，才能以它的单条零式代替原 N4(V)。Phi=0 时仍须保留原 N4(V) 本身，不能以其 Phi 倍数代替，也不能擅自把两项分别加零。本次源码明确限定当前 Delta0/W0 分支，其 Phi 已付。

W 的原权身份又实际给
$$
E_\Delta=\Phi[(3-4\lambda)Q-Jz+2uQSv_0].
$$
上述全式不倒置 D、值一次首项或其范数。旧 $L_\Delta,L_C$ 是这些原式在矩关系下的余项；本次直接保留原式，因此不丢同值关联。

## 4. 个别 N/P 的两个谱支完整返回

对同一个原 Gram 第 2、3 行，令
$$
N_h=N_4(g_2)-2\lambda P_{02}h^2,\quad
N_k=N_4(g_3)-2\lambda P_{02}k_U^2,
$$
$$
P_h=P_2(g_2)-P_{02}h^3,\quad
P_k=P_2(g_3)-P_{02}k_U^3.
$$
源码实际核 $N_k=\overline{N_h}$、$P_k=\overline{P_h}$，并保留偶、奇两系数。因为 r 非零，两谱方程同时成立准确等价于这两系数各自为零，未只留加权和。

还实际核
$$
bN_h+cN_k=N_s-2\lambda P_{02}H_A/u^2,
$$
$$
bP_h+cP_k=P_s
-P_{02}[(3+2v_0)H_A-H_B]/u^2. \tag{7}
$$
因此新个别 N/P 与原矩确实包含此前加权必要式，原同点关系保持。

新的原行清单是三条 Gram 行 $E_1,E_{B,e},N_1$，(2) 的第三矩行，$E_\Delta,E_C$，及个别 N/P 的四个偶奇分量，共十行。其四生成元余式由 (3) 和 $q_Y$ 的无除法规则明确定义。原 $\lambda,D,s,\zeta,S,Y$ 的非零要求及其他原物理条件均继续保留，不把其范数当作单位。

## 5. 实际完成范围与冻结的未完成展开

自含源：
`notes/2026-11-27-unit211-generic-LS-W-full-original-values-four-generators-8542.py`；
Git blob `54b9b0c7d04982e78829da8b1886ec5b92b49a04`，
26170 字节，SHA256：
`7681be8c837ed4f45929815627f5d1d1421fdf955f94213277333bf430d07e4b`。

[已成身份回执](../notes/2026-11-27-unit211-W-centered-monic-value-tower-positive-receipt-8542.json)与[准确未完成展开回执](../notes/2026-11-27-unit211-W-full-values-ambient-timeout-receipt-8542.json)保实际 Actions run **45981471920** / job **140446181313**：

- (1)–(3) 的完整原矩与单首一塔身份于 **1.442233796 秒**通过。
- (5)–(7)、P1、两谱个别 N/P 和原 Delta/相容身份于 **2.477233700 秒**全部通过。
- 三条 Gram 行的四列余式依次通过；最后 $N_1$ 回执为 **9.794682600 秒**。
- 下一行 `original_third_moment` 的环境展开区间没有返回。无法从日志进一步区分其中的约化、参数归一化或编码子步骤。
- 配置 180 秒、4 GiB；驱动 **180.075155169 秒**，RSS **96736 KiB**，内层退出 **-14（SIGALRM）**。没有内存触界证据。
- stdout **15122 字节**，SHA256：
  `33b1958fd4476903af4733eb712f3e50a6678c0e5c77a888c75cde73fd4d0ce2`。

因此本页已完成的是完整原值身份及单首一四生成模型。没有声称十行展开系数、八个真乘法列、二十行乘法检查或最终矩阵证书已经算完；该环境多项式展开门冻结，不加时重跑。下一输入改用四维乘法逐步约化原小标量，保留这里已经实际核出的原身份。

实际 pull **2026-11-27 10:22:08.946270 UTC**，前后同为
`209b0c5a874c6a4e8c6483fd0b5d83de845fe224`；
两 README blob 为
`282e86b03385d3b6245ce7100ae2e2af7b103c2d`、
`5fbd905291dd044c88d35bd9c07ac0e586ff795a`，均无变化。

本页不宣称有限原点排空、剩余整个 W 完成或普通 ISP 完成。
