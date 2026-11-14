# 原 shooting 方程的正则化最小二乘方向：待检方案

状态：**方法方案，未实现 worker，未运行新的全尾、Jacobian 或线性求解。** 2026-11-09，coupled_prefix。当前原 M15 恢复进程由 root 持有，不作修改。

目的只是在同一有限 shooting 方程上寻找较温和的搜索方向。已有 M15 失败态的原 Newton 线性方程残差不超过 $1.61\cdot10^{-9}$，而 $\alpha=1/65536$ 的真实残差才出现微小下降。这支持研究方向的非线性适用范围，**不支持认定 Jacobian 错误或舍入是主因**。正则化没有已观察的收益，亦不证明目标边值有解。

## 1. 完全保留原残差及变量单位

记 $d$ 为数值 stage 数，$K=2M$，原保存状态 $y_n\in\mathbb R^K$，原 `scaleFor(target)` 的正数为 $\sigma_n$。令

$$
z_n=y_n/\sigma_n,\qquad
r_n=\frac{\Phi_n(y_{n+1})-y_n}{\sigma_n},\quad 0\le n<d.
$$

$\Phi_n$ 必须仍是原真实 RK、原角向 moment root 和原 `.05` guard。$t$ 表示进入 tail shooting 的原 Q 边值，即物理 height 除以 $r_{\rm cut}^4$ **一次**。cut 与远端 Robin 行为

$$
r_C=P_Qz_0-t/\sigma_0,\qquad
r_R=C_Rz_d,\qquad C_R=(-G_d\ \ I_M),
$$

其中 $G_d$ 是原对角远端 graph。把这些行合成 $R$，则 $\|R\|_\infty$ 与原程序的 normalized residual 完全同义；没有重新加权接受标准。

由原全 Jacobian $J_n=D\Phi_n(y_{n+1})$ 构造

$$
T_n=\frac{\sigma_{n+1}}{\sigma_n}J_n,
\qquad A_{n,n}=-I_K,\quad A_{n,n+1}=T_n.
$$

另外加入 cut 的 $P_Q$ 和末端的 $C_R$。$A$ 是对 $z$ 的原残差导数；遗漏 $\sigma_{n+1}/\sigma_n$ 会改变问题，不能省略。

## 2. 方向与块结构

对一个正的、仅属于求解算法的 $\lambda$，考虑

$$
(A^TA+\lambda I)\,\Delta z=-A^TR.
$$

这等价于最小化 $\|R+A\Delta z\|_2^2+\lambda\|\Delta z\|_2^2$。它不把原 PDE 改成有正则化项的方程：状态更新后仍重新评价原 $R$。

正规矩阵是块三对角的。若 $D_n$ 为对角块，则

$$
\begin{aligned}
D_0&=(1+\lambda)I+P_Q^TP_Q,\\
D_n&=(1+\lambda)I+T_{n-1}^TT_{n-1}\quad(0<n<d),\\
D_d&=T_{d-1}^TT_{d-1}+C_R^TC_R+\lambda I,
\end{aligned}
$$

上、下相邻块分别是 $-T_n$、$-T_n^T$。右端的正梯度块为

$$
g_0=-r_0+P_Q^Tr_C,\quad
g_n=T_{n-1}^Tr_{n-1}-r_n,\quad
g_d=T_{d-1}^Tr_{d-1}+C_R^Tr_R.
$$

求解右端为 $-g$。$\lambda>0$ 时，实数模型中矩阵正定，因为二次型是 $\|Av\|_2^2+\lambda\|v\|_2^2$。

## 3. 不能把二范数下降当作原最大残差下降

当 $A^TR\ne0$ 时，最小二乘方向对 $\|R\|_2^2/2$ 是严格下降方向；若 $A^TR=0$，它是零方向。对原 $\|R\|_\infty$ 则不保证下降。一个明确的线性反例是

$$
A=\begin{pmatrix}1&0\\-2&1\end{pmatrix},\quad
R=\binom{1}{9/10},\quad\lambda=10.
$$

所求方向为 $\Delta z=(1/23,-17/230)^T$。原最大分量的方向导数为 $1/23>0$；因此充分小正步长也会增加最大残差，尽管二范数目标下降。

所以候选 $\lambda$ 应先作便宜的线性检查：计算原十档 $\alpha=2^{-k}$ 的 $\|R+\alpha A\Delta z\|_\infty$，至少有一档严格小于原值才值得尝试该方向。这个检查只筛方向，不保证真实残差会下降。真正接受仍必须是原真实 `evaluate(...,false)` 成功通过全部 root guards，且其最大残差严格下降；不改原十档步长或阈值，不使用 surrogate residual 验收。

## 4. 第一次有限诊断应怎样选 $\lambda$

先以一个已冻结输入作单次方向比较，建议采用中断前 $s=.25$ 的 iteration-4 CP，而非读活动文件。其 minA 约 $.91456$，有已知原方向回溯记录；它仍是未收敛态。必须使用原全 Jacobian，不同时引入 stale/deep Jacobian 缓存。

一个具体但尚未试验的量级选择是

$$
\gamma=\frac{\|A\|_F^2}{(d+1)K},\qquad
\lambda/\gamma\in\{10^{-10},10^{-8},10^{-6},10^{-4},10^{-2},1,10^2\}.
$$

这些只是有限方向候选，不是新的物理或成功条件。七个带状线性系统共用同一 $R,A$，不额外调用原 RK。报告每个候选的线性最大残差预测、$\|\Delta z\|_2$、$\|\Delta z\|_\infty$、与原 Newton 方向的大小比和线性系统 backward error。优先比较能够在线性模型下降、同时显著减小更新幅度的候选；若没有这种候选，应如实留下负结果，不扩成无界参数扫描。

未来首次实际测试最多挑两个候选方向，分别按原真实残差判据检验。只有比原方向得到可辨的残差下降或允许更大的有效步长，才值得另行冻结一个 worker 派生。当前没有授权或执行这些测试。若固定候选量级受强尺度差异影响，可后续改用指定 $\|\Delta z\|_2$ 的信赖域参数求取；这也是另一项数值选择，不能事后把它说成当前已实现方法。

## 5. 内存、数值条件与停止边界

当前 M15 有 $d=864,K=30$，未知量共 25,950。保存全部 $T_n$ 需要约 6.22 MB；完整对角/相邻正规块约 12.45 MB。对应标量半带宽是 59，单个三角 band 存储约 12.46 MB。额外矩阵存储在几十 MB 量级，不需要建立 $25950^2$ 稠密数组。块构造及一次带状分解的工作在约 $10^8$ 标量运算量级；尚未量测具体运行时间，不能预称比原算法更快。

正规方程会平方未正则化问题的条件数。很小 $\lambda$ 时应检查 backward error 和 Cholesky 状态；不能因为矩阵在实数中正定就忽略浮点失败。必要时用等价增广最小二乘系统 $[A;\sqrt\lambda I]$ 的带状/稀疏 QR，并对同一线性目标核验。原日志 `chartCondition≈39850.69` 只是局部 Riccati chart 的指标，**不是** $A$ 的整体条件数，不能用它宣称正规方程精度。

实际 state 更新必须是 $y_n\gets y_n+\alpha\sigma_n\Delta z_n$。原 minA/minD 仅由当前真实评价报告，不把线性系统或旧 Jacobian 的值当当前余量。若真实下降失败，刷新原全 Jacobian后再作有限决策；不降低 guard、不放松原 residual 容差、不把线性模型的小残差当成真实收敛。

最终成功仍要求原全域 residual 小于 $2\cdot10^{-9}$，并以原全 Jacobian 和原 audit 重核。**真正 DN 的 heightJetJacobian 必须由原线性化方程计算，不能由带 $\lambda I$ 的方向系统充当物理 DN 导数。** $s<1$ 仍只是 warm；此方向方案本身不支付实际 prefix 联解、全图 metric 收敛、无限尾存在性或 README G5。
