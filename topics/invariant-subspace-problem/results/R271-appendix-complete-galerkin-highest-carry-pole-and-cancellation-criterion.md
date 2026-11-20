# R271 补录：完整 Galerkin 源的最高 carry 极点与消奇性判据

日期：2026-11-20（UTC）。作者：Astra-ISP-b2a9acde-20261120 / r271_cost，根复核；AI-assisted GPT-6 Astra Pro。

## 0. 用途与边界

本条给出完整真核 Galerkin/MP 系统的一条精确有限维判据。
它检测最高 carry 的简单逆极点是否被原源消去；
不把“逆只有简单极点”偷换为“原费用随 carry 变小”。
原 N、Y 头在偶强段、奇高度下满足本条假设，
由 [奇高度最高 carry 的完整 MP](R271-appendix-odd-height-highest-carry-full-mp-simple-pole.md) 认证。
这里不证明增长强段 $R=d$ 下的残余阶数，也不闭合普通 Hilbert ISP。

## 1. 完整有限维假设

在固定物理 Hilbert 空间上，设
$$
X_t=X_0+tX_1,\qquad0<t<t_0,
$$
其秩对 $t>0$ 恒定，并满足
$$
\|X_t^\dagger\|\le C/t.
\tag{1.1}
$$
假设真核、真范围在零点有满列秩解析框架。
在原最高 carry 族中，这些框架由固定左右剪切与
$G_t=\operatorname{diag}(tI,I)$ 的两级过滤直接构造；
故此处不是额外未经验证的核连续性假设。

记
$$
K=\ker X_0,\qquad Z=\ker X_0^*,\qquad
\mathcal E_1=P_ZX_1|_K,\qquad E=\operatorname{Ran}\mathcal E_1.
\tag{1.2}
$$
假设一阶 Schur 项开齐所有新增秩，即
$$
\operatorname{rank}\mathcal E_1
=\operatorname{rank}X_t-\operatorname{rank}X_0.
\tag{1.3}
$$
原族由 (1.1) 与线性铅笔的 Schur 消元满足此式：
若尚有奇值在二阶才打开，其 MP 必至少损失 $t^{-2}$。

于是完整极限空间为
$$
F_0:=\lim_{t\to0}\ker X_t=\ker(\mathcal E_1|_K),
\qquad
L_0:=\lim_{t\to0}\operatorname{Ran}X_t
=\operatorname{Ran}X_0\oplus^\perp E.
\tag{1.4}
$$
第一式可由一阶核兼容性与维数相同证明；
第二式由消去零阶可逆块后的全部一阶新增范围证明。
特别地
$$
\mathcal E_1^*|_E:E\longrightarrow K\ominus F_0
$$
是双射。

令 $H_t$ 为解析自伴严格正矩阵，且在零点附近 $H_t\ge I$；
原纯高度代表中
$$
H_t=\sum_{j=0}^{r-1}\frac{(C_t^*)^jC_t^j}{j!S^j},
\qquad X_t=C_t^r.
$$
对固定原源 $f$，定义完整 Galerkin 与完整 MP
$$
F_t=\ker X_t,\qquad
a_t=(P_{F_t}H_t|_{F_t})^{-1}P_{F_t}f,
$$
$$
\xi_t=f-H_ta_t,\qquad
q_t=(X_t^*)^\dagger\xi_t.
\tag{1.5}
$$
Galerkin 正交性保证
$\xi_t\in F_t^\perp=\operatorname{Ran}X_t^*$，所以 $q_t$ 是完整真解，
且 $q_t\in\operatorname{Ran}X_t$。

## 2. 解析性与真实极点系数

### 定理 2.1

$a_t,\xi_t$ 在 $t=0$ 解析。
$q_t$ 至多有一个简单极点，可写
$$
q_t=t^{-1}q_{-1}+q_0+tq_1+\cdots.
\tag{2.1}
$$
其真实极点系数由完整空间唯一确定：
$$
\boxed{
q_{-1}\in E,\qquad
\mathcal E_1^*q_{-1}=P_K(f-H_0a_0).
}
\tag{2.2}
$$

**证明。** 取零点满列秩的解析核框架 $Z(t)$。
(1.5) 可写
$$
a_t=Z(t)\bigl(Z(t)^*H_tZ(t)\bigr)^{-1}Z(t)^*f.
$$
零点矩阵仍严格正定，故 $a_t,\xi_t$ 解析，且 $a_0$ 恰为
$F_0$ 上的完整 $H_0$-Galerkin 解。

在原有限矩阵族中，各条目在实参数 $t$ 上是解析有理函数；
固定秩区间上的 MP 也可由满秩 minor、完整范围框架与 Gram 逆写成有理式。
更一般地，解析恒秩框架给出穿孔邻域上的亚纯表达。
(1.1) 与 $\xi_t=O(1)$ 排除二阶及更高的极点，得 (2.1)。

因 $q_t\in\operatorname{Ran}X_t$，有
$q_{-1}=\lim tq_t\in L_0$。
比较 $X_t^*q_t=\xi_t$ 的 $t^{-1}$ 系数，得
$X_0^*q_{-1}=0$，所以由 (1.4)
$$
q_{-1}\in L_0\cap Z=E.
$$
再比较常数系数：
$$
X_0^*q_0+X_1^*q_{-1}=\xi_0.
$$
投影到 $K$，第一项消失；
因为 $q_{-1}\in Z$，第二项恰为
$\mathcal E_1^*q_{-1}$。得到 (2.2)。
右侧在 $K\ominus F_0$，因为 $\xi_0\perp F_0$；
$\mathcal E_1^*|_E$ 双射，故唯一性成立。证毕。

这里 $E$ 是零点固定的一阶 Schur 新方向；
没有把它未经比较地等同于 $t\ne0$ 时某个移动的小奇值谱投影。

## 3. 极点消失等价于退化完整核 Galerkin 解的兼容性

定义退化处较大的完整核 $K=\ker X_0$ 上的解
$$
a_{\rm full}=(P_KH_0|_K)^{-1}P_Kf.
\tag{3.1}
$$

### 定理 3.1

以下条件等价：
$$
q_t=O(1);
\qquad
P_K(f-H_0a_0)=0;
\qquad
a_{\rm full}\in F_0.
\tag{3.2}
$$
此外，$a_0$ 是 $a_{\rm full}$ 在 $H_0$ 内积下到 $F_0$ 的正交投影。

**证明。** 定理 2.1 说明第一项等价于 $q_{-1}=0$，
而 (2.2) 与 $\mathcal E_1^*|_E$ 的单射性说明它等价于第二项。
若第二项成立，则 $a_0\in F_0\subset K$ 满足完整 $K$-Galerkin 方程，
由严格正定唯一性 $a_0=a_{\rm full}$，于是第三项成立。
反之，若 $a_{\rm full}\in F_0$，它也满足 $F_0$-Galerkin 方程，
故 $a_0=a_{\rm full}$，第二项成立。

对任意 $v\in F_0$，两条 Galerkin 方程相减得到
$$
\langle H_0(a_{\rm full}-a_0),v\rangle=0.
$$
这正是最后的投影断言。证毕。

等价地，真实极点由整个核中的投影损失决定：
$$
\mathcal E_1^*q_{-1}
=P_KH_0(a_{\rm full}-a_0).
\tag{3.3}
$$
例如在 $E\ne0$ 时，
$$
\|q_{-1}\|
\ge \frac{\|a_{\rm full}-a_0\|}{\|\mathcal E_1\|},
\tag{3.4}
$$
因为 $P_KH_0|_K\ge I_K$。
因此完整核损失只要非零，就有实际逆极点；
不能用“最高 carry 很小”略去它。

## 4. 改善到 $q_t=O(t)$ 的准确下一阶条件

写 $\xi_t=\xi_0+t\xi_1+\cdots$。

### 定理 4.1

在同一完整系统中，
$$
\boxed{
q_t=O(t)
\quad\Longleftrightarrow\quad
\xi_0=0\ \text{且}\ P_K\xi_1=0.
}
\tag{4.1}
$$

**证明。** 若 $q_t=O(t)$，由 $X_t^*q_t=\xi_t$ 可知
$\xi_0=0$，且 $\xi_1=X_0^*q_1$，所以 $P_K\xi_1=0$。

反之，$\xi_0=0$ 先由 (2.2) 给 $q_{-1}=0$，
故 $q_t=q_0+tq_1+\cdots$。
常数项给 $X_0^*q_0=0$，而 $q_0\in L_0$，所以 $q_0\in E$。
一次项投影到 $K$ 给
$\mathcal E_1^*q_0=P_K\xi_1=0$；
单射性推出 $q_0=0$。证毕。

常用的完整残差二阶界 $\xi_t=O(t^2)$ 是 (4.1) 的充分条件，
但不是必要条件：只需一次残差在 $K$ 上消失。
反过来，仅知道完整 MP 至多损失 $t^{-1}$，连 (3.2) 都不能省略，
更不能直接宣布 (4.1)。

## 5. 对原纯远孔费用的含义

若 $S,x,r$ 固定，原远孔因子 $\sigma_{x,r}$ 与最高 carry 参数 $t$ 无关。
若 $q_{-1}\ne0$，则
$$
\kappa_{m,r}(t)^2
=\sigma_{x,r}^2t^{-2}\|q_{-1}\|^2+O(t^{-1}).
\tag{5.1}
$$
若要在移动 $m,R,r$ 的原参数处得到小费用，必须控制 (3.3) 的真实源损失、
其次控制下一阶系数和随参数增长的常数。
固定小头的精确消奇性不能代替这些控制。

真实八维 N 头 $m=3,R=0,r=3$ 已有显式非零极点下界，
说明 (3.2) 在原多 carry 族中并非自动成立。
增长强段下的目标应是量化旧 carry 使 (3.3) 变小的阶数，
或证明某些允许高度的完整兼容性，而不是把未证兼容性当成核旗定义的一部分。
