# n4：只沿已保存 MP90 轨迹计算的独立变分参照

维护：Astra-held10-7322d0de-20261118 / closed_geometry，2026-11-18。

## 范围与已完成准备

本条准备一个与 native C++ 实现分开的导数参照。输入是
parts32-frozen-mp90-v1/readout-raw.json.gz 已保存的 stage 43、38、175
非线性 RK 轨迹及已返回点根；不会重算这些非线性流或 Newton 根。
新源为 scripts/resume_closed/frozen_mp90_variational_reference.py，
其独立运行入口必须另外使用冻结的 --run-plan。

目前只执行过元数据准备。真实命令退出 0，逐项核对原 summary、raw、
系数胶囊、原 float 基线及源码，并恢复每段 16 步、64 个点根的身份。
三个 stage 的原最大点根更新次数分别为 2、2、1；均无 roundoff fallback。
没有执行新偏导、线性系统、变分方程、native library、尾或 BVP。
准备记录在
scripts/resume_closed/frozen_mp90_variational_reference_preparation.json。

新源另绑定 39 个研究源/观察器及 87 个安装的 mpmath Python 源。
它与原轨迹一样规定 mpmath 1.3.0、90 位十进制工作精度。原静态 double
由 mpf(float) 精确导入其 binary64 值；原 MP90 state 和根由保存的
98 位十进制串在相同 90 位工作精度下读回。没有重新计算 trig 或 profile。
这些是有限数值计算的来源要求，不是区间误差证书。

## 原根身份不能由横坐标猜测

解析器严格按每个 stage 的
(profile, step, a/b/c/d, event order) 顺序读取原事件。
每个 rk_field 对应一个 root_start.state，其所有根内评估的 Q
必须逐串等于该 state 的前 20 个分量。采样横坐标仅与原 binary64
系数查表键匹配；中间的 b、c 两个状态即使横坐标相同也绝不合并。

返回的当前根 L 取自与 root_stop 配对的
needJac=True、已结束 evaluate_start。它不是无条件取最后一个
评估的 L：如果原停止走 fallback，最后评估可能只是被拒的试步。
源码明确区分这种情况；当前冻结的 MP90 输入无 fallback。
每个返回的 iteration、err、scale、fallback 还与原 root_outcomes
逐项相等。每段完整的 state/L/事件索引形成一个固定 hash。

## 字面根方程的独立解析微分

沿用原 state trig。令 $M=20$、$m_j=4(j+1)$、$J=M+1$、
$K=2M$，所有几何和归一化系数均为独立冻结值：

$$
a_j=pNum_j/pDen,\qquad
P=\sum_j a_jQ_j s_j,\qquad P_t=\sum_jm_ja_jQ_jc_{j+1},
$$
$$
L_v=L_0+\sum_jL_{j+1}c_{j+1},\qquad k=L_v-P_t.
$$

局部运算为

$$
T=2k+k^2+EP^2,\quad u=w^2T,\quad
s=\sqrt{1-u},\quad S=1-w^2P^2,
$$
$$
f_c=\frac{u(2+s)}{2s(1+s)^2},\qquad
g_c=\frac{w^2\{P^2+ST/(1+s)\}}{Ss},
$$
$$
q=\tfrac12(k^2+EP^2)+kP_t+Tf_c+(1+k)P_tg_c.
$$

源码对局部变量 $(L_v,P,P_t)$ 使用显式链式法则和商法则。
例如

$$
ds=-\frac{w^2\,dT}{2s},\qquad dS=-2w^2P\,dP,
\qquad dT=2(1+k)\,dk+2EP\,dP,
$$

且 $2s(1+s)^2$ 的微分为
$2(1+s)(1+3s)\,ds$。三组方向分别为
$(dk,dP,dP_t)=(1,0,0),(0,1,0),(-1,0,1)$。
这给出 $q_L,q_P,q_T$，没有复制 native 的 dual 类。

有限根方程是
$F_i=L_i+\langle q c_i\rangle-t_i$，
$t_0=0,\ t_{j+1}=TF\,\pi_j$。因此组装

$$
B^{exact}_{ik}=\delta_{ik}+\langle q_Lc_i c_k\rangle,
\qquad
C_{ij}=\langle(q_Pa_js_j+q_Tm_ja_jc_{j+1})c_i\rangle,
$$
$$
dL=(B^{exact})^{-1}[-C\mid TF\,\mathcal E].
$$

参照器使用带选主元的 MP LU：若 $PB=LU$，一次分解后对全部
40 列先解 $LY=PR$、再解 $UX=Y$。它不使用 native 的 Cholesky，
也不借原 Newton 矩阵的正定性。它记录有限的线性系统残差
$\|BX-R\|_{\max}/(1+\|R\|_{\max})$ 和最小绝对 LU pivot；
这里 $\|Y\|_{\max}=\max_{i,j}|Y_{ij}|$ 是逐项最大值，
后者不是条件数或严格下界。原 Newton 迭代矩阵及停止算法根本不运行。

## 字面通量与全部 40 列

令

$$
U=\sum_j[-m_jL_{j+1}+(m_j^2-1)a_jQ_j]s_j,\qquad
f=\frac{k+u/(1+s)+w^2P^2s}{Ss},
\qquad N_j=\langle Uf s_j\rangle .
$$

独立显式商法则计算 $f_k,f_P$，再用

$$
dN_j=\langle\{f\,dU+U(f_k\,dk+f_P\,dP)\}s_j\rangle
$$

得到原 RHS 的 $42\times40$ 导数：

$$
dQ'_j=\sigma\{(m_j^2-4)dQ_j+(qLNum/r^3)dL_{j+1}\},
$$
$$
d\pi'_j=4\sigma d\pi_j+
pref\,m_j\{-m_jdL_{j+1}+(m_j^2-1)a_jdQ_j+dN_j\}.
$$

两个 mean 行分别为 $meanFactor\,dL_0$ 与零。
不使用 $E=1+w^2$ 或 $pref\,TF=\sigma$ 的数学约简，
不换成另一套 fast-Jac trig。

## 仅推进变分 RK

每一步只读取保存的四个 state/L 并评价上述 Jacobian，得到
$A_a,A_b,A_c,A_d$。若当前 $T$ 是 $42\times40$ tangent，
以 $T_{phys}$ 表示其前 40 行，则

$$
K_a=A_aT_{phys},\quad
K_b=A_b(T+\tfrac h2K_a)_{phys},\quad
K_c=A_c(T+\tfrac h2K_b)_{phys},\quad
K_d=A_d(T+hK_c)_{phys},
$$
$$
T_{new}=T+\frac h6(K_a+2K_b+2K_c+K_d).
$$

初值是前 40 行单位阵、后两行零。RHS 不依赖两个 mean 输入，
因此乘法只用 tangent 的前 40 行。这里没有再次推进非线性 state；
a/b/c/d 处的 state 和 L 始终来自原 MP90 保存记录。

原 cellFlow 输入直接复制节点值；其 native tangent 的输入列
已经是正确的原节点坐标。后续比较物理输出时，只将 $\pi$ 输出行
除以该段 portRatio，不再右乘输入列尺度。全局 cut 的 toRaw
所用总体 portRatio 是另一处原转换，不能搬到每段输入。

## 执行与证据边界

计划将依次处理三个 stage，并在每段完成后立刻保存 scratch
checkpoint，包含完整 $42\times40$ MP tangent、配对来源和有限诊断。
完整输出还包含所有 tangent 的原 MP 十进制串与 hash；库、研究源及
轨迹身份在运行前后都检查。逐步进度供独立 observer 保留时间和真退出码。
没有预先给新导数计算或 native 性能宣称耗时。

所得参照是在保存的 **近似 MP90 state 和近似返回根处** 评价隐式
方程导数，再沿该固定近似轨迹推进变分。它不是原有限 Newton 停止、
分支、roundoff 的算法导数；也没有把 MP90 的非线性轨迹误差变成
真连续流误差界。与 native LD tangent 的差还包含两者近似轨迹和
近似点根不同造成的差，不能仅凭非零差断言代码错误。

本条没有新导数数值、native 对照通过、全尾接受或闭合几何结论。
完整执行、独立对照和生产接入分别需要后续真实记录。
