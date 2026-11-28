# Phi=0 首个原二次头开图：同一原理想 D 返回及六次必要方程

> **2026-11-28 更正：本页经旧紧凑 R2 / Rbar 导出的原必要性、有限性、点数与排除声明已撤回。** 二重点一次坐标的平方被误写为 d1²，真实值为 2d0d1；完整更正和依赖边界见[原定义更正](../notes/2026-11-28-unit211-dual-germ-compact-mean-definition-correction-and-dependency-quarantine-8542.md). 已实跑的旧定义矩阵等式、次数与失败记录保留，不能再据此推原 Gram 条件或支付新模型单位。下文保留为原记录。


数据保存说明（2026-11-28）：可重算载荷已按根规矩8/15从main移除，相关旧链接只定位既有历史；当前保留生成源、参数定义、run与SHA，原数学及执行身份不变。


日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

## 1. 结论与范围

在
[R150-appendix-unit211-Phi-zero-monic-twelve-original-four-rows-and-quadratic-head-charts.md](R150-appendix-unit211-Phi-zero-monic-twelve-original-four-rows-and-quadratic-head-charts.md)
的第一个真实二次头 $H_{6,4}\ne0$ 的图上，实际原解必须满足一个已精确保存的参数方程
$$
P_6(u,Q,\lambda)=0.
$$
它的三变量次数为
$$
(\deg_u,\deg_Q,\deg_\lambda)P_6=(39,20,6),
$$
共 3101 项。

该必要方程来自真实原单位
$$
D=\ell(2\lambda^2-2\lambda+1)-T^2
$$
的完整原理想返回。它没有把未付 cofactor 主元当成单位，也没有假定三生成元构成自由模。

范围仅是 $H_{6,4}\ne0$。整个 $H_{6,4}=0$ 权曲线仍保留；其中四头同时为零的十权异常集合由另一结果准确给出，不能用这十点替代整个首头零曲线。本结果没有排除整张开图或整个 $\Phi=0$ 面。

## 2. 原四式及实际三个生成元

在原已付权单位处局部化，并只在本图加入 $H_{6,4}^{-1}$，记所得参数环为 A。保持
$$
z=Qt,\qquad f=-P_c/P_f.
$$
用已付紧凑原恒等式，令
$$
q_1=R_2/(2\rho),\quad q_2=W_4,\quad
q_3=O_8/\rho,\quad q_4=N_1^*.
$$
这些都是关于 $(T,z)$ 至多二次的真实原式，系数属于 A。这里没有解原 $N(V)$ 线的 $S_nZ$ 分母。

记前三式在 $(T^2,Tz,z^2)$ 上的矩阵为 L，在 $(1,T,z)$ 上的矩阵为 C。因本图真实头非零，源以完整三阶伴随矩阵恒等式求出
$$
\begin{pmatrix}T^2\\Tz\\z^2\end{pmatrix}
\equiv
-L^{-1}C\begin{pmatrix}1\\T\\z\end{pmatrix}
\pmod{(q_1,q_2,q_3)}.
$$
全部九个系数身份均实际乘回。记右端的三行为 $r_{TT},r_{Tz},r_{zz}$，并定义
$$
M_T=\begin{pmatrix}0&1&0\\r_{TT}\\r_{Tz}\end{pmatrix},
\qquad
M_z=\begin{pmatrix}0&0&1\\r_{Tz}\\r_{zz}\end{pmatrix}.
$$
这里每个 $r$ 是三个参数系数，不是单个矩阵条目。

令 $v=(1,T,z)^{\mathsf T}$，则
$$
M_Tv\equiv Tv,\qquad M_zv\equiv zv
\pmod{(q_1,q_2,q_3)}.
$$
这两个身份保留了完整原方程来源；没有把未核的乘法歧义设为零。

## 3. 三条真正的原理想行

对原 $q_4$ 使用同一三条规则得到余行 $r_0$：
$$
q_4\equiv r_0v\pmod{(q_1,q_2,q_3)}.
$$
因此 $r_0v$ 属于 $I=(q_1,q_2,q_3,q_4)$。

另外
$$
(M_TM_z-M_zM_T)v\equiv0\pmod{(q_1,q_2,q_3)}.
$$
这是把同一原二次规则分别用于 $T^2z$ 与 $Tz^2$ 的两个顺序所得。交换子的第一行恒为零；其第二、三行 $r_1,r_2$ 都是实际原理想行。

源保留这两条歧义作为额外行，并未要求 $M_T,M_z$ 在一个假定自由的三维代数中先验交换。因此，即使 $1,T,z$ 在原商中线性相关，此原理想来源仍成立。

把三行组成
$$
B_0=\begin{pmatrix}r_0\\r_1\\r_2\end{pmatrix}.
$$
目标 D 的同一规则余行是
$$
d=\ell(2\lambda^2-2\lambda+1)(1,0,0)-r_{TT}.
$$
所以 $dv\equiv D\pmod I$。

## 4. 最后分母的完整取消

源在参数分式域中先计算
$$
\alpha=dB_0^{-1}
$$
并完整验证 $\alpha B_0=d$。这只是构造多项式身份的中间步骤，不把 $\det B_0$ 加入原单位。

令 B 为三个 $\alpha_i$ 最后分母的最小公倍式，并逐项乘回 $\beta_i=B\alpha_i$。源实际验证三个完整系数身份
$$
Bd=\sum_{i=0}^2\beta_i r_i.
$$
由上一节的原理想来源，随即有
$$
BD\in I
$$
于本图的 A[T,z] 中。所有临时分母均已清除。

实际公共分母 B 的次数为 $(46,29,6)$，5148 项；三个清分母原行乘子的次数分别为
$$
(41,25,6),\quad(49,28,5),\quad(51,26,5).
$$
源没有只检查某个原点上的数值，而是检查了全部三个参数多项式系数的完整乘积。

在真实原解上 $D\ne0$，故 $B=0$。最后仅除去已付权单位因子，且每次除法乘回，得到上述 $P_6$。本次实际剥除来自 $u-1,Q,1-Q,\ell,T_0$；没有把任何新增未知因子作单位。最终源虽允许剥本图头因子，但实际日志没有发生额外头因子的剥除。

因此每个本图实际原解都满足 $P_6=0$。这里没有宣称 $P_6$ 关于 $\lambda$ 的首项已付为单位，也没有由“六次”直接推出全局首一有限代数。

## 5. 精确可恢复输入

完整 3101 项多项式保存在：

[2026-11-27-unit211-Phi-zero-first-quadratic-head-actual-D-core-exact-input-8542.json](https://github.com/Rogerhu12/math-research-public/blob/3b9cda56dfa6a1ae9d4ca2a35fa81798a5f156c9/topics/invariant-subspace-problem/notes/2026-11-27-unit211-Phi-zero-first-quadratic-head-actual-D-core-exact-input-8542.json)。

其规范 profile SHA256 为
d12d36de38995832f521156d012ce93b6160dc7b1d870903923051ac5da0bf15。

profile 的原上下文是 $(u,Q,\lambda,T,z)$，最后两指数恒为零；载荷按前三变量保存，JSON 已明确记录这两个补零位置。压缩前完整系数载荷 86039 字节，SHA256 为
9e50cc2a30cf8500b7bef25f8e579334c2b46f8d896662759cdc0ec85f35542c。
源已解压、重建并完整比较该多项式。

此原理想返回只使用四个原二次式和真 D 单位。原矩条件 $F_6$、原 $N(V)$ 线及个别 NB/PB 条件还可以给进一步限制，本文没有冒称已完成它们在这个新三生成元图中的全部返回。

## 6. 实际执行

源：
[2026-11-27-unit211-Phi-zero-first-quadratic-head-three-original-rows-D-input-8542.py](../notes/2026-11-27-unit211-Phi-zero-first-quadratic-head-three-original-rows-D-input-8542.py)。

- blob：e6d789552dd958e63269ecb6e1f01e3605ff2eff。
- SHA256：100ce4dfb7380da1591cd453aae392e2dafcaaceb3a601c4500d07852841ecaf。
- run/job：46032433800 / 140619343997。
- source commit：d144b463b611689a97727e9550cad261db7ea8a5。
- 内层：1.510052183 秒 / 48712 KiB / exit 0。
- stdout：45741 字节，SHA256 267eee48d5639bd131f51688fda3d6df03e331f75d2ba21cb39281dff87bdaff。

前三原均值规则在 0.057 秒返回，完整原行 DAG 在 0.116 秒返回，D 目标的完整公共取消在 1.372 秒返回。全部结果来自本次新三行输入；没有重放旧六行 cofactor、失败的几何逆代入或完整大投影。普通 ISP 尚未完成。
