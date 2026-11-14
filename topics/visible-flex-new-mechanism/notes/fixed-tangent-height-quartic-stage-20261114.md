# 固定 $T,a$ 后的九高度四次 metric 阶段

日期：2026-11-14。状态：**已证明的有限采样代数与约束保持；代码待公开人工检查。** 不包含实际候选评价或新的求解结果。

实现：`scripts/frame_height_quartic.py`。它是已有九高度可行多面体之后的可选接口：先取得独立核过的可行高度系数，再保持同一 $T,a$、全部高度行和原系数盒，最多调用一次 SLSQP 改善直接 metric 成本。是否对实际数据调用，留待已启动的九高度 LP/QP 输出决定。本文件不修改当前公共计算配置，也不添加任何自动实际求解。

## 1. 变量与准确有限变化

固定现有切向场 $T(t,\theta)$、完整度量半径 $a(t)$、不可变高度参考 $b_0$ 和高度基 $C_j(t)=I_j'(t)$。令参考系数为 $c^0$，对应位置和径向速度为 $X^0,U^0=X_t^0$。任意新**绝对系数** $c$ 满足

$$
d=c-c^0,\qquad v(t)=\sum_jC_j(t)d_j,
$$

$$
X(c)=X^0+\Big(\sum_j I_jd_j\Big)e_z,
\qquad U(c)=U^0+v e_z.
$$

这仍是一个共同高度原函数，不逐圈重设中心。定义

$$
e_0=|U^0|^2-1,\qquad q_0=U^0\cdot T,
\qquad u_z=U^0\cdot e_z,\qquad t_z=T\cdot e_z.
$$

则完整有限变化为

$$
e=e_0+2u_zv+v^2,\qquad q=q_0+t_zv.
$$

在现有准确 $G=a^2$ 表示中，$e=E-1$、$q=F/a$。这些式子不线性化参数变化，也不需要每次试探重新求热积分、$\Pi T$ 或几何网格。它们只是对同一已评价的固定 $T,a$ 数组进行代数运算。

## 2. 四次目标和全部解析导数

在固定采样 $(t_i,\theta_k)$ 上，令 $w_{ik}\ge0$ 为冻结权重且总和非零。目标为

$$
J(c)=\frac12\sum_{i,k}w_{ik}(e_{ik}^2+2q_{ik}^2).
$$

默认 $w_{ik}=1/(N_tN_\theta)$，准确复用原求解器的样本均值归一，即使径向节点并不均匀，也不暗改为另一种径向求积权重。若显式提供其他权重，按字面使用并记录，不自动归一。

对每个径向行，压缩角向求和得

$$
J(c)=\sum_i\sum_{m=0}^4 A_{im}v_i^m,
\qquad v_i=\sum_j C_{ij}(c_j-c_j^0),
$$

$$
\begin{aligned}
A_{i0}&=\frac12\sum_kw_{ik}(e_{0,ik}^2+2q_{0,ik}^2),\\
A_{i1}&=2\sum_kw_{ik}(e_{0,ik}u_{z,ik}+q_{0,ik}t_{z,ik}),\\
A_{i2}&=\sum_kw_{ik}(2u_{z,ik}^2+e_{0,ik}+t_{z,ik}^2),\\
A_{i3}&=2\sum_kw_{ik}u_{z,ik},\\
A_{i4}&=\frac12\sum_kw_{ik}.
\end{aligned}
$$

这是精确的次数至多四的多项式恒等式。浮点计算得到的 $A_{im}$ 是这些和式的数值评价，不是有向区间。

对 $v_i$ 求导：

$$
g_i=\sum_kw_{ik}\left[2e_{ik}(u_{z,ik}+v_i)+2q_{ik}t_{z,ik}\right],
$$

$$
h_i=\sum_kw_{ik}\left[2e_{ik}+4(u_{z,ik}+v_i)^2+2t_{z,ik}^2\right].
$$

故

$$
\nabla J=C^Tg,\qquad \nabla^2J=C^T\operatorname{diag}(h_i)C.
$$

$2e$ 项可能为负，不能把这一四次阶段称为凸优化。其 Hessian 有负特征值的人工数组例被纳入开发检查。这里不保证局部算法到达全局最小值。

实现采用未展开的平方表达式评价 cost/gradient/Hessian，以减少在 $e,q$ 很小时的多项式相消；同时独立提供角压缩后的 Horner 评价用于人工交叉核对。两者描述的是同一个有限采样目标，不是不同物理模型。

## 3. 完整约束沿用，不另造门

`FixedTangentHeightQuartic` 必须消费已有 `HeightPolytope` 对象，并核对其参考 $X$、径向和角向节点与 metric 数据逐项相同。其输入 $C$、$U^0$、$T$、权重复制后只读，并记录形状、字节 SHA、原始完整多面体 SHA、绝对参考系数和来源。

原多面体是

$$
Ac\le b,\qquad \ell_j\le c_j\le u_j.
$$

其中包括固定角样本的 signed-$z$、球半径和共同帽高行。新阶段直接将**原完整** $A,b,\ell,u$ 传给 SLSQP；没有去掉不方便的行，没有扩盒、投影或自动改变 cap margin。固定的水平样本若已经违反球条件，原多面体不会允许选中初态，新阶段也不会启动。

这里的 $c^0$ 是生成 $U^0,X^0$ 的参考系数；开始优化的可行点 $c^{\rm init}$ 可以是上一 LP/QP 提案，两者不能混淆。若使用重新评价后的 $U(c^{\rm init})$，就必须相应重新锚定整个参考和多面体，不能仍把它误标为 $U^0$。本接口避免这种隐式重锚：保持原 reference，代数评价任意可行 initial。

有限样本、浮点行和已声明容差内的通过，并不是全曲面连续的球界、嵌入或 reach 证明。若以后改变 $u,v$，当前多面体和四次系数都失效，必须重建；共同帽高的全局仿射公式本身仍有效。

## 4. 单次求解与候选选择

接口为

```python
objective = FixedTangentHeightQuartic(data, C, unchanged_polytope)
proposal = propose_height_quartic(objective, feasible_initial)
```

主检查顺序如下：

1. 初态必须由原多面体独立判定为可接受；否则零次优化并保存原因。
2. 保存可行初态和其 metric 成本；零预算时保留它，不运行求解器。
3. 最多一次 `minimize(..., method='SLSQP')`，使用真实 `LinearConstraint` 和原 `Bounds`，解析梯度，不依靠 `keep_feasible`。
4. 逐次评价独立检查原行和原盒，只把可接受候选纳入 best。算法可能评价不可行 trial，这不等于将它作为输出。
5. 返回、预算退出或异常后，再核选中点。异常保存已有可行 best，不冒称优化成功。每十个新 trial 或六十秒保存一次中间记录。

参数只决定一个受限数值阶段的预算；不自动加第二次 SLSQP，不更改角网格或高度参考后重新优化。报告保留 `slsqp_calls`、初态评价、trial 计数、返回点重核、优化器状态、原行/盒结果和准确 binary64 系数及差值。数值目标下降只在同一冻结目标内部比较。

## 5. 与完整目标及几何的区别

本阶段只最小化直接 metric 的 $J$，不把原 `smooth_positive` ball/strip 项伪称为四次多项式。虽然原 sampled ball/height 行保留，完整平滑形状成本仍可能变化。$y$ 与水平投影在固定 $T,a$ 下不变，所以单靠高度阶段不能修复 strip 越界。

提案不直接改任何物理状态。后续公共 driver 必须按返回的准确 absolute coefficients 重建完整 geometry，再报告：

- 原直接 metric 与完整平滑目标；
- 原帽高、signed-$z$、球和 strip 样本；
- 面积、曲率、镜像点对法弦筛；
- 同一物理系数下需要的评价精化。

不能把 height-polytope 通过、局部 quartic 成本下降或 SLSQP 的 success 当作等距、嵌入、reach 或课题完成。

## 6. 逐圈无约束必要下界诊断

同一组五个系数还给一个无需再次优化的放松：允许每个径向行的 $v_i$ 独立取任意实值，暂时去掉径向共同基、系数盒、帽高和形状约束。正权行的四次首项 $A_{i4}>0$，故其全实轴最小值必在三次方程

$$
4A_{i4}v^3+3A_{i3}v^2+2A_{i2}v+A_{i1}=0
$$

的实根中取得。逐圈最小值之和在数学上是当前固定 $T,a$ 全局受约束目标的必要下界。每圈除以该行权重总和后，记最小值为 $J_i^*$；在 $G/a^2=1$ 表示下，$\sup_\theta\eta\ge\sqrt{J_i^*}$，因为 $\eta^2\ge(e^2+2q^2)/2$。

实现通过现有五系数求三次根，在数值实根处用未展开平方式评价并比较，保存最小值、最差径向行、三次导数残差，以及对应的自由速度变化。**这些浮点根和极小值只是上述数学放松的数值估计，不是严格下界证书。** 近重根和系数求和都未作有向误差包围；它们不会进入候选接受门，更不会据此单独宣布路线排除。

若输入提供原共同速度 $b$，同时输出

$$
W=U^0-b e_z,\qquad S=\langle |W|^2\rangle_\theta,
\qquad \langle W_z\rangle_\theta.
$$

准确 $\Pi$ 模型有 $\langle W_z\rangle=0$，从而等距必须 $S+b^2=1$、$|b|\le1$。有限评价时另报告扣去角均值后的自由最小平均能量

$$
S_{\rm proj}=\left\langle
|U^0-\langle U_z^0\rangle e_z|^2\right\rangle,
$$

及 $\max(S_{\rm proj}-1,0)$ 的样本下界估计，避免把数值均值误差直接当成准确零。还记录无约束逐圈最优速度是否违反 $|b|\le1$；违反只说明该放松最优点不满足准确单位径向速度的必要条件，不排除其他可行速度。所有诊断保持原系数和原约束不变。

## 7. 人工开发检查及状态

CLI 只支持明确的人工 `--check-only`，没有实际文件输入或实际模型求解路径。预备检查包括：解析梯度/Hessian 的方向差分，factored 与 Horner 的全系数交叉核对，非零 $q$ 和非均匀权重，已知两变量正分支解，逐圈已知零极小值与 $S$，真实行/盒筛、零预算、不可行初态，以及第二次评价故意失败时仍保留初态。修改参考 $X$ 会被拒绝。

```bash
python topics/visible-flex-new-mechanism/scripts/frame_height_quartic.py \
  --check-only --out "$RUNNER_TEMP/frame-height-quartic-check.json"
```

截至写入，仅做本地静态语法检查和纸面代数核查；所有人工数值检查及今后实际阶段仍由公开仓库 Actions 执行。是否启用实际阶段，等待当前九高度可行 LP/QP 的真实报告，不重跑原大维数 250 次求解。

API 依照当前已使用的 [SciPy SLSQP 官方说明](https://docs.scipy.org/doc/scipy/reference/optimize.minimize-slsqp.html)；运行时 NumPy/SciPy 版本和源码 SHA 随报告记录，不以文档版本代替实际运行身份。

## 8. 公开人工已通过

run43631537869/source4e60f25c3c145f715c5bde6f8ed7bf76b393cdc9的height_quartic_development成功。梯度方向差8.62e−12、Hessian方向差2.67e−11，factored/Horner差≤1.34e−15；已知正支解差6.75e−7且直接metriccost4.16e−13，非凸Hessian见证−.88，逐圈零极小/S、完整门/失败保初态均通过。没有真实高度优化。九高度实际初值已由43630874689取得，下一driver将调用一次本阶段并完整几何重建。
