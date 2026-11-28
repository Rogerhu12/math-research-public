# 新输入：W/b0 负 e、单位 k 边界的完整 I6+q2 原最低项

日期：2026-11-28。会话：Astra-ISP-8542378f-20261127。

**首次输入，尚未执行。** 本次从完整同点原 Gram 的六式和原 $q_2$ 出发，只处理仍保留的方向
$v(e)<0,\ v(k)=0$。既有三原必要式已证明这里 $\lambda\ne0,\ v(\lambda)=0$；本门加入此前没有在该边界使用的完整 $I_6$，覆盖全部 $t$ 估值和 $t=0$。不重做旧 $q_2,R_6,N_5$ 最低项、旧九个权面、首一 $\lambda$ 投影或旧 cofactor。

## 1. 已付入口与准确原范围

[三原最低项与谱估值限制](../results/R150-appendix-unit211-W-b0-original-initial-ideals-and-two-lambda-valuation-restrictions.md)的唯一 run46157115224 / job141016111136 已给
$$
v(e)<0,\quad v(k)=0\quad\Longrightarrow\quad
\lambda\ne0,\quad v(\lambda)=0.
\tag{1}
$$
其 $\lambda$ 估值为零的 cell 没有关闭。本次只使用 (1) 作为既成范围，不重复其证明目标。

保持当前正确 W、distinct singleton、物理 $D\ne0$ 的整个 $b_0=0$ 已付图。$e=u-1,\ Q=ek$。全部已付权单位与原恢复沿
[整个 b0 的 t 参数原两列环境](../results/R150-appendix-unit211-W-entire-b0-original-t-parameter-monic-lambda-two-and-exact-I4.md)
及其
[完整 I6/q2 原坐标源码](2026-11-28-unit211-W-b0-t-parameter-monic-lambda-two-complete-I6-q2-two-original-targets-8542.py)
使用。本次不执行该源码，也不构造其头逆、首一 $\lambda^2$、十二行或旧两个标量。

既有有限权模型使 $e,k,\lambda$ 为代数数；一般
[固定谱 $P_f$ 图首一 $t^3$](../results/R150-appendix-unit211-general-fixed-spectrum-Pf-chart-original-monic-t-three-corollary.md)
又使同点 $t$ 为代数数。因此可在包含这些坐标的数域上取 $p=1009$ 上方赋值，所有非零坐标的赋值比都为有理数。这个论证不假设旧权分母在该赋值处为单位。

## 2. 同点的七条完整原多项式

用与已有 W 完全相同的权定义
$$
u=e+1,\quad Q=ek,\quad \delta=1-Q,\quad V_{\!b}=uk+2,
$$
$$
\ell=\frac{u((k+2)^2-2ek)}{kV_{\!b}},\qquad
m=u-\ell,\qquad M=\ell(2u-\ell Q)-u^2,\quad bc=\frac{M}{4\delta}.
$$
再令
$$
T_0=2u-\ell Q-2u^2,\quad J=2u(1-u)+\ell Q,\quad
\Phi=T_0+4u-4+Q,\quad P_f=T_0(J-Q),
$$
$$
P_{02}=(2-3u)(2u-\ell Q)-Qu+2u^3,\qquad
A_*=4uQ-J,\quad \kappa=\frac{uQ\ell}{A_*}.
$$
当前 b0 原图已付 $A_*$，故
$$
T=\kappa(2\lambda-3),\qquad w=\lambda-1-T.
$$
原同点恢复为
$$
f=\frac{P_{02}(T_0-2\kappa Q)\lambda
+eT_0^2-QP_{02}(\ell-3\kappa)-bcQ\Phi t}{P_f},
$$
$$
V=\frac{Jf-\lambda P_{02}-eT_0+bcQt}{Q},\qquad
W_1=T_0/2+2uf.
$$
它保留一般 W 的 $\Phi$ 修正；不套用 $\Phi=0$ 的专属公式。

令
$$
x=\frac{(u-\ell Q)V-mW_1}{M},\qquad
y=\frac{\ell W_1-uV}{M},\qquad
X=x+\rho y,\ Y=x-\rho y,\quad \rho^2=\delta.
$$
原权 $b=\ell/2+m\rho/(2\delta),c=\ell/2-m\rho/(2\delta)$，
$p=1+\rho,q=1-\rho,a=1-\ell$，并置
$$
A_1=2f-2V+2bct,\quad r=X-ap-ct,\quad s=Y-aq-bt.
$$
同一个 Gram 的四行为
$$
(0,0,p,q),\quad (0,A_1,r,s),\quad(p,r,0,t),\quad(q,s,t,0).
$$
双数乘法始终为 $(vz)_1=v_0z_1+v_1z_0$。
从该原 Gram 直接定义 $E_1,E_{B,e},E_{B,o}$、完整极化 $N_1$、
完整 weighted $NS,PS$。目标保持
$$
N_1=N_4(g_0+g_1)-N_4(g_0)-N_4(g_1)-4\lambda wP_{02},
$$
$$
NS=bN_4(g_B)+cN_4(g_C)
-2\lambda P_{02}(\ell+2T+A_2),
$$
$$
PS=bP_2(g_B)+cP_2(g_C)
-P_{02}(\ell+3T+3A_2+B_3),
$$
其中 $A_2=2\lambda^2-2\lambda+1$，
$B_3=4\lambda^3-6\lambda^2+3\lambda-1$。

第七式仍是整个 b0 的原必要式
$$
q_2=2a_\Delta/\ell,
$$
$$
a_\Delta=M\ell^2Q(3-4\lambda)+MA_*T^2+
2MuQ(3-2\lambda)\ell T+
(\ell A_2-T^2)(A_*m^2+J\delta\ell^2).
$$
七式按固定顺序 $E_1,E_{B,e},E_{B,o},N_1,NS,PS,q_2$ 使用。
均值、$N_1,q_2$ 对 $(\lambda,t)$ 总次数至多二，$NS,PS$ 至多三。

本源是自含定义，没有历史数据依赖或已有大系数输入。每条完整原有理式的权分母都检查为原已付；分子仅剥旧已付权因子，再清有理常数成 primitive 整系数多项式，并实际乘回完整原尺度。没有除 $t,\lambda$ 的原多项式首项，也没有除原物理 $D$。

所用权支持是 $e,k,u,\delta,V_b,k+4,P_{02},M,k+2,\ell,m,2\ell-1,A_*$，以及当前 W 原恢复图已经支付的 $P_f,\Phi$；没有新增权单位。把 $P_f,\Phi$ 显式列入，避免把它们尚未展开的因子错误地当作未付分母。

## 3. 整条 t 估值直线和 t 恰零

设 $v(e)=-c,\ v(k)=0,\ c>0$，并使用 (1)。
若 $t\ne0$，令 $\tau=v(t)/c\in\mathbb Q$。

对七式每一完整多项式
$$
F=\sum c_{ijlm}e^ik^j\lambda^lt^m
$$
取
$$
h_m=\min_{c_{ijlm}\ne0}(-i),\qquad
\mu_F(\tau)=\min_m(h_m+m\tau).
$$
准确枚举七条下包络的全部有理断点，其并集分成断点、所有有界和无界开区间。每个开区间选一个固定有理代表，仅识别在整个区间不变的最低项集合。没有选择若干经验 $t$ 值代替全部估值。

$t=0$ 单独取七式的 $t$ 常数系数再取最低项。这里不借用任何别图的 $t\ne0$ 排除，也不把零 $t$ 当成环面。

primitive 整系数均为 $1009$-整。每个最低几何面须含一个 $1009$-单位系数；否则整个 cell 保留，不猜更高阶、不换素数。若含单位，真实最低赋值等于 $c\mu_F(\tau)$，其模最低式必须在实际 leading residues 上为零。

最低式的整数化准齐次作用允许规范 $e$ 的 leading residue 为 1。剩余变量是非零的 $k,\lambda,t$ leading residues；对于 $t=0$ 分支只剩非零 $k,\lambda$，所有式与乘子始终独立于第三变量。

每个最低式只除公共环面单项式和非零 $\mathbb F_{1009}$ 常数。源码实际乘回该规范化身份，记录除去的单项式、常数及 profile；没有除任何其它非单项式因子。

## 4. 固定原 Laurent 行运算及完整七源

规范后的最低多项式记为 $F_0,\ldots,F_6$。
行运算始终同时携带七个 Laurent 乘子
$$
g=\sum_{i=0}^6 A_iF_i,\qquad
A_i\in\mathbb F_{1009}[k^{\pm1},\lambda^{\pm1},t^{\pm1}].
\tag{2}
$$
初始标签是相应标准基。$t=0$ 分支中的所有 $t$ 指数始终为零。

单项式顺序固定为 $(k,\lambda,t)$ 的 graded reverse lexicographic 顺序，禁止根据结果更换。初始原行按上述七式顺序进入。之后 S-pair 按 LCM 总次数和固定行编号排序。

每步只做以下合法操作：用已有行的单项式倍减去可约最高项；若得到余式，再除余式公共单项式和非零最高常数。原标签同步执行同一 Laurent 运算。公共单项式只在当前 leading-residue 环面内为单位。剥单项式可能暴露新的可约最高项，程序继续普通余式约化，直到该新行不能再约。

每条新行在加入前，都以完整稀疏 Laurent 多项式乘法逐项返回 (2)，而不只核一个最高项或模矩阵秩。若得到常数 1，实际返回
$$
1=\sum_{i=0}^6 A_iF_i.
\tag{3}
$$
合前面的每条原最低式规范化尺度，这就是七条完整原必要条件的最低项单位来源，排除该整个估值 cell。

若固定行算法结束而没有得到 1，只记录保留的准确 profile；不把它称为已证明可解的剩余初始概形，也不需要宣称本过程已构造整个 Laurent 饱和理想的标准基。证明排除只依靠实际 (3)。如果时间或内存触界，只保此前已经完整返回的 cell，不恢复同一输入。

## 5. 整条方向的结论条件

只有全部非零 $t$ 断点、开区间以及 $t=0$ 都有完整原单位返回，才可记这一条 $(-1,0)$ 方向关闭。与 (1) 合用时，旧已排的其它 $\lambda$ 估值不会遗漏。

若仅部分 cell 完成，准确保留余项；不得由算法未找到单位声称存在原点。其它五条旧方向完全不变。即使整条新方向排除，也不声称 $e,k$ 全为 $1009$-单位、所有旧分母整、有限 DVR 原模型、W/b0 为空或 ordinary ISP 完成。

## 6. 冻结身份和唯一资源

源 basename：

2026-11-28-unit211-W-b0-negative-e-full-I6-q2-original-initial-t-valuation-8542.py

源 blob：b33c1abc4ebeaf2ad7f84ff883a56155352df81e。

源 SHA256：54e04e96a39f0caca9e59d55ba3636f27cf8678c7cfeffbecb6212ce8756af0d。

UTF-8：16507 字节。零依赖。唯一首次预算 **180 秒 / 4 GiB；外层 195 秒**。

记录只含原参数定义、每式 profile、断点与保留范围、七源返回标志、乘子 profile 和资源回执。完整系数与可重算缓存均不保存。源码尚未执行，不预言 cell 数、任何单位返回或方向排除。
