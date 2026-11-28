# R150 补充：全 W 原伴随式的五条纯 λ,T 三次必要条件

- 会话：Astra-ISP-8542378f-20261127。
- 日期：2026-11-28（UTC）。
- 范围：当前已付 W 权图，仍保其原物理 $D\ne0$ 范围。
- 状态：唯一首次执行已完整返回；五条均非零、几何总次均恰为 3。保留完整原十一式，不宣称五条单独充分或 W 排空。
- 源：[完整五三次原返回](../notes/2026-11-28-unit211-W-whole-adjugate-five-pure-cubics-original-return-8542.py)。
- 冻结 source blob：cebfb2552a229648f8918eec165eac462ba86fcb。
- source SHA256：436753912eaf238b024541b1595840b53b0e61d8ad431c80506218cc050807d1；17016 字节。
- 原预算：180 秒、4 GiB；自含，无外部源码依赖。实际 4.776389191 秒、56372 KiB、内部 exit 0。
- 小回执：[完整实际执行与 checkpoint](../notes/2026-11-28-unit211-W-whole-adjugate-five-pure-cubics-original-return-8542-execution.json)。

## 1. 已有输入和真正新目标

[全图 f 唯一恢复](R150-appendix-unit211-W-original-I4-six-rows-entire-paid-f-head-and-unique-recovery.md) 给出原四式理想中的

$$
R=f+g(\lambda,T),\qquad \deg_{\lambda,T}g\le2,
\tag{1}
$$

所有最终系数分母均为已付权单位。原首一二次及三条余式为

$$
q_f=f^2+q_1f+q_0,\qquad
r_i=A_i+B_i f,\quad
\deg A_i\le2,\ \deg B_i\le1.
\tag{2}
$$

这里以及下文的次数只针对 $\lambda,T$；$q_1,q_0$ 分别至多一次、二次。原四式是正确 dual germ 的
$(E_1,E_{B,e},E_{B,o},N_1)$，其中 $E_1$ 独立保留。

[纯原理想定理](R150-appendix-unit211-W-pure-weight-f-head-exact-lambda-T-original-ideal.md) 与[同一 f 的十一纯式实际返回](R150-appendix-unit211-W-same-f-eleven-pure-lambda-T-original-conditions-complete-return.md)已给出完整原 $I_{11}$ 的十一条纯式。**这十一式继续保留**；本次只添加五条次数较低的原必要条件，不宣称这五式单独与完整系统等价。

本次没有执行旧全十一式来源返回、旧 pair/norm、旧首项因式、旧 native 或 NV 动作门。仅重建必要的真 Gram、$q_f,r_i,g$ 和原 $\mathsf N,\mathsf P$ 定义，以构造以下不同数学目标。

## 2. 原三行的伴随表示，不倒新权行列式

记

$$
\begin{pmatrix}B_1\\B_2\\B_3\end{pmatrix}
=B\begin{pmatrix}1\\\lambda\\T\end{pmatrix},
\qquad
B\in M_3(A_W),\qquad
\Delta_B=\det B.
\tag{3}
$$

$A_W$ 是当前纯权单位环。定义

$$
\operatorname{adj}(B)
\begin{pmatrix}A_1\\A_2\\A_3\end{pmatrix}
=\begin{pmatrix}C_0\\C_\lambda\\C_T\end{pmatrix}.
$$

原三行直接给出

$$
\operatorname{adj}(B)
\begin{pmatrix}r_1\\r_2\\r_3\end{pmatrix}
=
\begin{pmatrix}C_0\\C_\lambda\\C_T\end{pmatrix}
+\Delta_B f\begin{pmatrix}1\\\lambda\\T\end{pmatrix}.
\tag{4}
$$

每个 $C_j$ 至多二次；(4) 的三个原四源向量逐项可计算。已有同一 $g$ 的定义还给出真正有理函数恒等式

$$
C_0=\Delta_Bg.
\tag{5}
$$

(5) 只使用先行定理中已经约消并确认全为旧权分母的 $g$。**新伴随构造不要求 $\Delta_B$ 为单位，也不引入 $\Delta_B^{-1}$。** 旧求 $g$ 的原始行列式即使含有被所有乘子共同约掉的未付因子，本次仍只使用最终已付的 $g$ 和 $R$ 原来源。

由 (4) 减去 $\Delta_B\lambda R$ 或 $\Delta_BTR$，得到两个全图原三次：

$$
U_\lambda=C_\lambda-\Delta_B\lambda g,\qquad
U_T=C_T-\Delta_BTg.
\tag{6}
$$

其来源分别为伴随矩阵的第 2、3 原行减去上述 $R$ 倍数。整个 $\Delta_B=0$ 权面保留。

## 3. 首一二次给第三条原三次

将 $g$ 按固定单项式次序分解为

$$
g=g_{00}+\lambda L_\lambda+TL_T,
\tag{7}
$$

其中 $g_{00}\in A_W$，$L_\lambda,L_T$ 至多一次。具体规定：将 $\lambda T$ 项收入 $\lambda L_\lambda$，因此分解没有任意选择。

令 $P_0=g^2-q_1g+q_0$。定义

$$
\begin{aligned}
\Gamma_q
&=\Delta_BP_0+L_\lambda U_\lambda+L_TU_T\\
&=\Delta_B(g_{00}-q_1)g+
L_\lambda C_\lambda+L_TC_T+\Delta_Bq_0.
\end{aligned}
\tag{8}
$$

第二行每项至多三次。第一行只说明来源；直接低次原来源为

$$
\Gamma_q=
\Delta_Bq_f+
L_\lambda(\operatorname{adj}(B)r)_\lambda+
L_T(\operatorname{adj}(B)r)_T
-\Delta_B(f+q_1-g_{00})R.
\tag{9}
$$

(9) 是完整原四式组合，系数仅含既有已付权分母。没有把原 $P_0$ 除以 $\Delta_B$ 或任意新内容。

## 4. 完整原 N/P 各给一条原三次

对任一真正加权原三次 $F\in\{\mathsf N,\mathsf P\}$，仅为本次新条件作首一短除：

$$
F=Q_Fq_f+A_F+B_Ff,
\qquad \deg A_F\le3,\quad \deg B_F\le2.
\tag{10}
$$

仍用与 (7) 相同的规范分解

$$
B_F=b_{00}+\lambda L_{F,\lambda}+T L_{F,T}.
\tag{11}
$$

定义

$$
\begin{aligned}
\Gamma_F
&=\Delta_B(A_F-B_Fg)
-L_{F,\lambda}U_\lambda-L_{F,T}U_T\\
&=\Delta_B(A_F-b_{00}g)
-L_{F,\lambda}C_\lambda-L_{F,T}C_T.
\end{aligned}
\tag{12}
$$

第二行每项至多三次。它的完整六原式来源是

$$
\begin{aligned}
\Gamma_F={}&\Delta_BF-\Delta_BQ_Fq_f\\
&-L_{F,\lambda}(\operatorname{adj}(B)r)_\lambda
-L_{F,T}(\operatorname{adj}(B)r)_T
-\Delta_Bb_{00}R.
\end{aligned}
\tag{13}
$$

将 (4)、(10)、(11) 代入，$f$ 系数严格相消，余下恰为 (12)。这说明第五、四条条件均是原六式理想中的实际组合，而非仅由某个互素性或数值根推测得到。

最终新增五式是

$$
U_\lambda,\quad U_T,\quad\Gamma_q,\quad
\Gamma_{\mathsf N},\quad\Gamma_{\mathsf P}.
\tag{14}
$$

它们的全部 $\Delta_B=0$、几何首项零和系数内容零纤维均保留。没有对任何原方程除未付因子；本次甚至不做新的共同内容剥除或因式分解。

## 5. 完整首次实际返回


唯一 [run 46135783099 / job 140950662262](https://github.com/Rogerhu12/math-research-public/actions/runs/46135783099/job/140950662262) 实际完成：

- $B\operatorname{adj}(B)=\operatorname{adj}(B)B=\Delta_BI_3$ 的全部 18 个坐标及 (4) 的三个原四源返回。
- (7)、(11) 的三个规范二次分解及全部重建等式。
- 五条新式的完整四或六原来源乘回，以及每条全部 $f$ 系数的严格相消。
- 所有最终分母属于已付纯权支撑：55 个不同最终分母，558 个精确多项式除法及已付支撑乘回。
- 两个原 N/P 三次的 4 次新首一短除乘回。

每个新式的实际约分分子如下；分母只依赖已付权。列中的几何次数为 $\lambda,T$ 总次。

| 新原必要式 | $(\deg_e,\deg_k)$ | $(\deg_\lambda,\deg_T)$ | 几何总次 | 分子项数 |
|---|---:|---:|---:|---:|
| $U_\lambda$ | $(21,22)$ | $(3,2)$ | $3$ | 2040 |
| $U_T$ | $(22,23)$ | $(2,3)$ | $3$ | 2142 |
| $\Gamma_q$ | $(35,41)$ | $(3,3)$ | $3$ | 7857 |
| $\Gamma_{\mathsf N}$ | $(36,44)$ | $(3,3)$ | $3$ | 8856 |
| $\Gamma_{\mathsf P}$ | $(36,43)$ | $(3,3)$ | $3$ | 8567 |

全部五式非零。原 $\Delta_B$ 分子双权次数 $(14,12)$、总次 22、81 项，SHA256 为 f00e39a0f88abbd0a74281ca0d9606c00810b9cd2b951e8674fde7f8f7cac40b；本篇只实际核它与旧权矩阵同一，没有以其非零多项式身份偷换为全图单位。

所有新式以及完整原乘子的分子/分母次数、项数、字节数、SHA256 均在上述小回执。可重算系数没有保存为独立缓存，也没有编码或分片载荷。

## 6. 执行身份及后续准确范围

- 冻结 source commit：2af851171a40ba8923e874c4dc0004927b68585c。
- source git blob：cebfb2552a229648f8918eec165eac462ba86fcb。
- source SHA256：436753912eaf238b024541b1595840b53b0e61d8ad431c80506218cc050807d1。
- 实际 driver：4.776389191 秒，最大 RSS 56372 KiB，内部 exit 0。
- 最后完整数学 checkpoint：4.703409635 秒。
- stdout：15483 字节，SHA256 1677bfa9377b7f719af1d11fa46ffddef5388af5886d69a19a025ae6efc1bd2b。
- 真 pull：2026-11-28 10:34:14.966300 UTC，前后均为上述 source commit；根 README blob 99c5ad8d06e939e6cfbbab1afdeffa5463f15f18、课题 README blob 5fbd905291dd044c88d35bd9c07ac0e586ff795a 均未变。

本次给的是完整原系统的新低次必要输入，原 $I_{11}$ 的十一条纯条件仍保留。(4)、(9)、(13) 都是整个已付权环上的实际恒等式，故 $\Delta_B=0$ 全面及各几何首项零面没有被删除。本次没有计算新原权投影、共同零点或单位证书，不能由五条三次非零宣称任何原纤维空，也不新增有限点数或方案长度界。
