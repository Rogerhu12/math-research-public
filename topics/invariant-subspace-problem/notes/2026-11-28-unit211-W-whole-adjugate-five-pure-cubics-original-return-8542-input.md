# 首次新输入：全 W 原伴随式的五个纯 λ,T 三次条件

- 会话：Astra-ISP-8542378f-20261127。
- 日期：2026-11-28（UTC）。
- 范围：当前已付 W 权图，仍保其原物理 $D\ne0$ 范围。
- 状态：未执行。下文给出新原恒等式的纸面证明，执行只构造本次五式的具体系数并逐原来源返回。
- 新源：2026-11-28-unit211-W-whole-adjugate-five-pure-cubics-original-return-8542.py。
- 冻结 source blob：cebfb2552a229648f8918eec165eac462ba86fcb。
- source SHA256：436753912eaf238b024541b1595840b53b0e61d8ad431c80506218cc050807d1；17016 字节。
- 预算：180 秒、4 GiB；自含，无外部源码依赖。无预记运行结论。

## 1. 已有输入和真正新目标

[全图 f 唯一恢复](../results/R150-appendix-unit211-W-original-I4-six-rows-entire-paid-f-head-and-unique-recovery.md) 给出原四式理想中的

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

[纯原理想定理](../results/R150-appendix-unit211-W-pure-weight-f-head-exact-lambda-T-original-ideal.md) 与首次 run 46134694458 已给出完整原 $I_{11}$ 的十一条纯式。**这十一式继续保留**；本次只添加五条次数较低的原必要条件，不宣称这五式单独与完整系统等价。

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

## 5. 首次执行具体核对内容

源直接从实际 $B$ 构造完整伴随矩阵，核
$B\operatorname{adj}(B)=\operatorname{adj}(B)B=\Delta_BI_3$ 的全部 18 个坐标，随后核 (4) 的三个完整原四源表示。

对 (7)、(11) 每次核全部二次系数及重建恒等式。对五条新式，每条均先用其完整四或六原源向量乘回，再逐 $f$ 系数核零，最后核几何总次数不超过 3。输出保留其约分分子/分母及各原乘子的次数、项数、字节数、SHA256；所有最终分母用此前固定已付权表逐因子乘回。没有假设候选五式非零，若其中某式恒零，按真实零式记录。

原 $I_{11}$ 十一式的完整等价表示继续作为后继输入。五式即使具体输出非零也只新增必要条件；本次不计算新权投影，不宣称 W 空，不新增点数或方案长度界。所有可重算大系数只在首次进程内形成，不写缓存、不分片传送。
