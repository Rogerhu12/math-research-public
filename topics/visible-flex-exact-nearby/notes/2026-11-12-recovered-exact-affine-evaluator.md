# 执行器恢复后的 exact-affine evaluator 与真实射线重跑

2026-11-12。状态：**源码已恢复，小型同对象回归已重新执行；全射线重跑进行中。**
原执行器中未推送的 trace 和 R58 输出已经丢失。这里的新源与新报告不
冒用旧文件哈希，旧结果只作为恢复记录；数值证书必须重新运行。

## 1. 同一个准确数学对象

使用原点 full-inputs `type_fixed_step02_d5_jet_interval_inputs.npz`
（SHA `0d17500ac49c845b402145c4d0a48170b7163ec0d7e6ed6f0eedcc1c649ca59b`）
和参数方向 `type_fixed_step02_d5_actual_parameter_direction.npz`
（SHA `8db5d57d65ea49cfe3a0df250714392300c98feeb2e0de2774aacbb4764d89ab`）。
准确参数为
$$
\delta_2=-\frac{15291006546051}{9007199254740992}
=\operatorname{binary64}(-0.001697642753711981).
$$
先定义准确 affine 原始样条 $S_0+\delta V$ 与均值 $\alpha_0+\delta w$，
再乘冻结背景权重并明确作 $a,\beta$ 偶对称、$\gamma$ 奇对称。
$Z$ 是冻结偶斜率从零点的准确积分，角位置为无限 R33 primitive。
三个均值变化连同实际相位变化一起改变
$g_0(\delta)=\langle |F_x|^2\rangle dx^2+a^2d\theta^2$。
这不是把控制值预先舍入得到的 rounded predictor。

对象 JSON 是恢复后新写的 schema 2 文件，SHA
`aa5df888dbf672c9e221f03e80cfa06c3c9c94a5dd7dd4f29fe15b1d795d99b1`。
旧 `ad970...` JSON 字节不在当前输出中，不能仍将它写成当前来源 SHA。
numerical 已实际重跑该同一数学点的 interval Newton 紧根证书，报告
`type_fixed_step02_d5_exact_affine_step2_root_tight.json` 的 SHA 仍准确为
`c2cfad858f64a0082d131eb492993c6a237ab249220dfe61593323c8d1cdfeeb`。
参考 root center 取报告中数值；整个有向 root 区间才是已证明的根包络。

## 2. evaluator 的实际导数与回归

`fourfold_phase_symmetric_geometry.py` 直接读冻结 BSpline 输入。
纯径向位置 jet 由 finite DFT primitive 近似；含角导数的 jet 使用
准确单位切向量表达式，例如
$F_\theta=aT$、$F_{x\theta}=a_xT+aT_x$。
参数列对同一表达式解析微分，不用有限差分生成参数方向。
有限差分只用作数值回归。

主速度采用同一法向约定
$C=F_\theta\times F_x$、$m=C\cdot F_{x\theta}$、
$n=C\cdot F_{\theta\theta}$、$G=C\cdot C$，所以
$$
v=b+\epsilon w\sqrt{-K_0},\qquad b=-m/n,\quad w=G/n.
$$
这里 $G$ 是实际叉积平方，不是目标度量行列式 $Ea^2$。
主速度与角/参数导数不需要面积平方根；面积平方根仅用于打印
采样 $N=n/\sqrt G$ 的诊断。

五个指定核心点的重新回归保存在
`2026-11-12-recovered-exact-affine-geometry-preflight.json`：

- 十个显式反射 jet 比较的浮点差均为零；
- raw 主变量的通用公式比较中 $m,n,m_\theta,n_\theta,m_\delta,n_\delta$
  差均为零，$G$ 与面积平方值的差不超过 $2.23\times10^{-16}$；
- 解析参数六 jet 与步长 $2\times10^{-6}$ 中心差分的最大差小于
  $1.21\times10^{-9}$；
- quarter $Q=256$ 与 $512$ 的十 jet 差最大约 $1.42\times10^{-13}$。

这些是浮点检查，不能代替连续无限角尾、算术误差或 ODE 认证。
特别是含角 jet 使用无限公式，不会把 finite primitive 的角导数
当成准确 $aT$；二者的误差必须在正式证明中另付。

## 3. moving-root 参数列和稠密参考

`fourfold_phase_exact_affine_nodes.py` 在 $x=t\sin\tau$ 中积分
$\theta,\log J$ 及固定 $x$ 的参数变分。分支结束后补足两个移动
端点项
$$
z_{\mathrm{end}}+t'\bigl(-Jv_{\mathrm{start}}
 \operatorname{sign}\tau_{\mathrm{start}}+
 v_{\mathrm{end}}\operatorname{sign}\tau_{\mathrm{end}}\bigr).
$$
完整 return 的参数列按 $J_2z_1+z_2$ 合成。这里保存的第三个积分
状态仍是固定 $x$ 的变分，不能和补完端点的最终列混为一行。

每个完成分支都保存 accepted times/states、DOP853 的
`dense_t_old, dense_h, dense_y_old, dense_F` 和其 SciPy 源码 SHA。
把保存 binary64 当准确 dyadic 后，nested formula 定义一个准确的
分段七次参考多项式；它与真实 ODE 解之间的误差尚未得到认证。
不假定保存的 `h` 等于两个 dyadic 时间端点的准确差，也不假定
相邻参考多项式没有跳跃。`fourfold_dense_trace_jumps.py` 对这些
端点关系作准确 Fraction 计算，报告必须在新 trace 上重新生成。

文件超过 1 MB 则 gzip，单件不超过 5 MB；如整分支超过上限，runner
按 accepted steps 切成 128 段块。每个完成分支写独立重启 manifest，
重启检查对象、源码、根、H、精度、节点及初值，不能复用另一张图。

## 4. 重新执行入口

在课题目录执行小型 evaluator 回归：

    OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
    python scripts/fourfold_phase_symmetric_preflight.py \
      --object data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step2_object.json \
      --out notes/2026-11-12-recovered-exact-affine-geometry-preflight.json

同对象 258 条真实 ray：

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
    python scripts/fourfold_phase_exact_affine_nodes.py \
      --object data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step2_object.json \
      --root-certificate data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step2_root_tight.json \
      --dyadic-conjugacy data/phase_ring_continuation/type_fixed_step02_d5_actual_Newton129_step2_dyadic_H.json \
      --out notes/2026-11-12-D5-exact-affine-step2-Hnodes258.json \
      --trace-dir data/phase_ring_continuation/exact_affine_step2_dense258 \
      --progress notes/2026-11-12-D5-exact-affine-step2-Hnodes258-progress.json \
      --rays 258 --block-size 43 --tolerance 2e-9 --resume

第一分支完成后，jump 重跑入口为

    OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
    python scripts/fourfold_dense_trace_jumps.py \
      --trace data/phase_ring_continuation/exact_affine_step2_dense258/block_0000_forward.npz.gz \
      --out data/phase_ring_continuation/exact_affine_step2_dense258/block_0000_forward_jumps.json

后续再做真实节点共轭 Newton；参数坐标使用准确 $\delta_2$，不再用
旧 global-$p$ 标签替代。新 H 和新参数点都须各自定义、各自重算。
当前仍欠 R60 的真实 ODE/线性残差、初值复管、全参数 Taylor 与
Wiener 费用，不能把本批恢复工作称为共轭、PDE 或闭曲面完成。
