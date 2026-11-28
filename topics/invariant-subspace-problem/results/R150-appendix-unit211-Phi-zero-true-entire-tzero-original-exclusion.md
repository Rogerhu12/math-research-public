# R150 补充：正确原 Phi 图整 t=0 分支的完整排除

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

## 1. 完整结论与适用范围

采用真正 dual 乘法、原 unit211 Gram、全部原均值、原值矩及 N/P 值和一阶 jet。在当前非零孤立均值、非零基点最高值的归一图中，假设
$$
\Phi=0,\qquad Q(1-Q)P_fP_{02}bcD\ne0,\qquad
D=\ell A_2-T^2,
\tag{1}
$$
其中
$$
A_2=2\lambda^2-2\lambda+1,\quad
B_3=4\lambda^3-6\lambda^2+3\lambda-1,\quad
w=\lambda-1-T.
$$
则
$$
\boxed{t\ne0.}
\tag{2}
$$
故原坐标 $z=Qt$ 也可在此整个图上作为单位。

这里不假定旧错误 first-head 的任一单位，不使用其 H1/H42、583 次权模型或 NP5 后继。本条使用更正后的原均值和新完整原 weighted N/P 身份。结论不排除 $D=0$ 碰撞图，也不宣称整个 Phi 或普通不变子空间问题已经完成。

$\lambda\ne0$ 是本条的既有原层条件，并非一个新消去假设。原 [U 值坐标层 §1](R150-appendix-essential-four-unit-two-plus-one-plus-one-original-U-value-atlas.md) 明确令 $V=U/U_0$、$\lambda=m/U_0$，其中 $m=\tau(U)$、$P_0=-U_0^3\ne0$。此前[零孤立点均值层的完整排除](R150-appendix-essential-four-unit-two-plus-one-plus-one-nonzero-base-highest-zero-isolated-mean-exclusion.md)已经支付 $m=0$；其原源直接使用真正 Frobenius 乘法，独立于后来更正的 compact E1。本条不重跑该零均值分支。

## 2. t=0 的完整原分解

记 $V=bX+cY$，$v_n=QV$，$p-q=2\rho$、$\rho^2=1-Q$。更正后的真实均值组合在 $t=0$ 为
$$
R_{2,\mathrm{true}}=8\rho Q^2(f-u)(V-f).
\tag{3}
$$
由 (1)，$\rho Q\ne0$。若 $V=f$，原
$$
A_1=2f-2V+2bc\,t
$$
给 $A_1=t=0$。[原 bipartite Gram 的两个完整 jet 身份](R150-appendix-unit211-original-bipartite-Gram-jets-force-value-discriminant-zero.md)随即给
$$
T=-\ell,\qquad A_2=\ell,\qquad D=0,
$$
与 (1) 矛盾。因此所有尚可能的 $t=0$ 原点都满足
$$
f=u.
\tag{4}
$$
这一步保留 (3) 的两因子；没有把 $f-u$ 或 $V-f$ 当作整个原系统的单位。

在 (4) 上，[完整原 weighted N/P 与两 jet 身份](R150-appendix-unit211-original-tzero-fu-weighted-NP-value-branches.md)给
$$
(2\lambda-1)w=0,\qquad \lambda(2\ell-1)=0.
\tag{5}
$$
由于当前原层 $\lambda\ne0$，故 $\ell=1/2$。下面分别保留 $2\lambda-1=0$ 和非零的两支。

## 3. 半值半权支

若 $\lambda=\ell=1/2$，上述完整 weighted P 身份
$$
P_{02}\{(1-2\ell)\lambda+2\ell-3A_2-B_3\}-4\ell u^3=0
\tag{6}
$$
直接化为 $-2u^3=0$，所以 $u=0$。

在真正 $\Phi=0$ 图，
$$
\ell=1-\frac{2(u-1)(u-2)}Q.
\tag{7}
$$
故 $Q=8$。由原 $P_1$ 与 $f=u$ 的准确恢复
$$
T=-\ell-\frac KQ\lambda-\frac{KA}{2\ell Q^2},
\quad K=Q+4(u-1),\quad A=4(u-1)^2-Q,
\tag{8}
$$
得到 $T=-1/2$，于是 $D=\ell A_2-T^2=0$。这排除整条 (1) 内的半值半权支，未假定 $u\ne0$。

## 4. 半权且 w=0 的完整参数恢复

余支满足
$$
\ell=\frac12,\quad \lambda\ne\frac12,\quad w=0,\quad T=\lambda-1.
\tag{9}
$$
令
$$
s=u-1,\quad r=u-2,\quad h=2u-3,\quad
\Theta=2hr,\quad N=u^2-6u+6.
$$
由 (7)，
$$
Q=4sr,\quad L=\ell Q=2sr,\quad K=4s^2,
$$
$$
M_n=2uL-L^2-u^2Q=-8s^3r,\quad A=4s,\quad P_{02}=sQ.
\tag{10}
$$
$Q\ne0$ 已付 $s,r\ne0$。把 (9) 代入原 (8)，不除 $h$ 就得到
$$
\Theta\lambda=N.
\tag{11}
$$
若 $h=0$，则 $u=3/2$，而 $N=-3/4$；(11) 不相容。因此 $h$、$\Theta$ 在本支非零。再由
$$
2N-\Theta=-2u(u-1)
\tag{12}
$$
和 $\lambda\ne1/2$，得到 $u\ne0$。这些单位仅在此分支支付；尤其未把一般 Phi 的 $u=0$ 面无证删去。

## 5. 两条真实原均值的低次精确返回

以下定义使本次一元证书可直接重建，不依赖预存大系数。设 $\delta=1-Q$，并定义
$$
v_0=Q(2u-1)-4s^3,\quad v_1=-2sL,\quad
V_N=v_0\Theta+v_1N,
$$
$$
N_N=Q(-K+4u^2)\Theta-2V_N,\qquad m_N=uQ-L,
$$
$$
S_N=2L\delta V_N-m_NN_N,\qquad
D_N=-2m_NV_N+LN_N.
\tag{13}
$$
由原 $E_0/N_0$ 图，$v_n=V_N/\Theta$、$n_n=N_N/\Theta$。定义
$$
\begin{aligned}
P_W={}&-2QM_nLK\Theta^2-4L\delta V_N^2-LN_N^2\\
&+4m_NV_NN_N+8QM_nuV_N\Theta,
\\
P_O={}&2QM_n^2(Q-L)s\Theta^2-4Q^2M_n^2u\Theta^2\\
&+QM_nS_N\Theta+2QM_n^2V_N\Theta\\
&+QM_n(u+1)D_N\Theta-S_ND_N.
\end{aligned}
\tag{14}
$$
这里 $P_W=\Theta^2QW_4$、$P_O=\Theta^2Q^2(1-Q)\overline O$，其中 $W_4,\overline O$ 正是正确原均值的加权、奇部组合。它们的原来源已由[正确四头源](../notes/2026-11-28-unit211-Phi-zero-corrected-dual-germ-four-original-quadratic-heads-8542.py)与七变量真实乘法身份支付；没有使用错误的 $R_{2,\mathrm{bad}}$。

将 (10)、(13) 代入 (14)，完整的一元多项式等式为
$$
P_W=512u^2s^5r^5F_2,\qquad
P_O=-6144us^6r^6F_4,
\tag{15}
$$
其中
$$
F_2=u^2-4u+2,
$$
$$
F_4=u^4-\frac{11}{2}u^3+\frac{29}{3}u^2-\frac{22}{3}u+2.
\tag{16}
$$
这些都是完整乘回身份。可手算先化
$$
V_N=4usr^2(3u-5),\qquad
N_N=8sr^2(13u^2-27u+12)
$$
再回 (14)，即得 (15)。整个复数参数域保留，没有只作有限域测试或范数筛选。

由第 4 节，(15) 的有理常数、$u,s,r$ 都非零。所有原点因而必须同时满足 $F_2=F_4=0$。但精确有
$$
F_4-\left(u^2-\frac32u+\frac53\right)F_2
=\frac{7u-4}{3},
\tag{17}
$$
$$
49F_2-(7u-24)(7u-4)=2.
\tag{18}
$$
因此明确的完整 Bézout 身份是
$$
\begin{aligned}
1={}&
\frac{49+3(7u-24)(u^2-\frac32u+\frac53)}2\,F_2\\
&-\frac{3(7u-24)}2\,F_4.
\end{aligned}
\tag{19}
$$
乘子次数分别为 $3,1$。这排除 (9) 的全部原复点，包含所有原首项可能退化的纤维。

## 6. 合成与实际证据

第 2 节覆盖 $t=0$ 的两因子，原 weighted N/P 给 (5)，既有原层 $\lambda\ne0$ 给半权。第 3 节关闭半值支，第 5 节关闭其余半权支。因此 (2) 已完整证明。

本次新小源：
[2026-11-28-unit211-Phi-zero-tzero-halfweight-wzero-original-return-8542.js](../notes/2026-11-28-unit211-Phi-zero-tzero-halfweight-wzero-original-return-8542.js)。

- Git blob：983373ab9f98e415a03a2927f6489a62d69fd3b8。
- SHA256：7ad8f7be3eb5b20bc738d9f82b72da17594aa70d51bcccf61bf4ce2c3de325f3。
- 6060 字节，自含纯 V8 BigInt 有理多项式运算。
- 首次实际 10 ms，22748 次有理运算、573 次多项式乘法、49 次完整除法乘回。
- 原清式次数为 $14,17,9$；仅删除已证明非零的原分支因子后为 $2,4,6$。
- 前两项完整 QQ Bézout 已返 $1$，乘子次数为 $3,1$；第三项系数为零。
- [小执行回执](../notes/2026-11-28-unit211-Phi-zero-tzero-halfweight-wzero-original-return-execution-8542.json)。

源也保存了第三条完整 weighted P 清式
$$
-P_{02}(2N-\Theta)^2(N+\Theta)-2u^3\Theta^3,
$$
但终端 Bézout 不需要它。源回执中的“originalPhiExcluded=false”准确指该源只处理 (9)，并非整个 Phi；本文的整 $t=0$ 结论由已经完成的不同原来源合成，未把源标志改成整 Phi 排空。

此前 bf3 的二元纯权 Buchberger 门在 120 秒边界停止，没有返 $1$；该失败仍冻结。本条使用完整原 weighted N/P 的新输入及显式一元 (19)，不续跑、重排或扩大那个失败门。当前整个 Phi 的 $t\ne0$ 原值系统仍继续开放。
