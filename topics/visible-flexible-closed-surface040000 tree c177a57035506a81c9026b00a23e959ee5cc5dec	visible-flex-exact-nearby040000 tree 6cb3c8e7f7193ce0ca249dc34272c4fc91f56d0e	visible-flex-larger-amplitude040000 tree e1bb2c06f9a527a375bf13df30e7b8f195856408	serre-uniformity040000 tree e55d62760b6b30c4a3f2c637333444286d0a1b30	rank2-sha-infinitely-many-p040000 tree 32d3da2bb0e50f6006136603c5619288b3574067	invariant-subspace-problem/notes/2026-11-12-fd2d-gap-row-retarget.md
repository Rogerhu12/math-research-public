# R159 消费补充：在同一完整场上只替换中央 gap 目标行

2026-11-12，Astra-visible-flex-fd2d。此接口服务 R168 允许的较小 gap 设计；本次没有更改主 BVP 的目标，也没有计算新的物理方向或曲面。

## 准确代数与适用范围

记当前中央轴差为 $G(p)=A(p)-B(p)$，完整中央参数导数为 $v=\nabla_pG$，其余参数分量为零。现有 raw / grouped stream 都把唯一 gap 行写为

$$r_d=(G-d)/d,\qquad J_d=(0,v^T/d),\qquad d>0.$$

该行不依赖 raw 场未知量，因此 R159 的中央场消元不会给它添加 field 列。现有 `RawLiftedDAE` 初始化只将目标存为 `self.gap`；固定 `FixedBalancedGeometry`、角图、物理 profile、lifting 和实际参数向量均不依赖这个目标值。完整场和其他有限行保持时，更换 $d_0$ 为 $d_1$ 的未缩放 normal 准确为

$$
H_{pp}^{(1)}=H_{pp}^{(0)}+J_{p,1}^TJ_{p,1}-J_{p,0}^TJ_{p,0},
$$
$$
g_p^{(1)}=g_p^{(0)}+J_{p,1}^Tr_{d_1}-J_{p,0}^Tr_{d_0},
$$
$$
c_p^{(1)}=c_p^{(0)}+J_{p,1}^{\odot2}-J_{p,0}^{\odot2},\qquad
\|F_1\|^2=\|F_0\|^2+r_{d_1}^2-r_{d_0}^2.
$$

这里 $c_p$ 是 R159 消元后的参数列平方范数。$H_{ff},H_{fp},g_f,c_f$ 以及全部行数、局部映射保持不变。证明只是把完整行和分离成共同的其他行加唯一 gap 行，然后逐项展开；没有删除任何场—参数交叉项。$H_{pp}$ 的差在实数算术中秩至多一，浮点减加不宣称与重新装配逐位相同。

这属于**同一场上的新有限目标**，不是一次新的接受态，也不是旧目标下的继续。实现要求完整未缩放 normal、唯一 gap 行和完全相同的输入 binding；新 binding 只允许改变 `mathematical_settings.gap`。不能用此接口把旧25目标变成 R165、把129节点变成131节点、换接受态、换 $g$、调整 curvature cap 或更改任一其他有限行。

## 可执行接口

`scripts/fd2d_gc_gap_row_retarget.py` 提供：

- `gap_retarget_binding(old_binding, new_target)`：生成只改变正 gap 目标的定义。
- `replace_gap_row_in_place(normal, actual_gap=..., central_gap_gradient=..., old_binding=..., new_binding=...)`：在调用者独占的**内存** normal 上作上述替换。中央导数必须是该绑定场的完整现有 `axes['gap_jacobian']`，未除目标值。

输入磁盘 checkpoint 不会被修改。返回的 normal 使用独立的 derived schema，保留完整 parent info 和替换证据，明确没有重新组装一套旧 tile。它不冒充原 `merged_normal_binding`，后续持久化须显式绑定这个派生实体和新目标。该接口不自动接入任何活动 stage。

参数列平方范数发生变化后，必须重新作列缩放、阻尼和 Schur 消元，并让 QP 的 `preserve_gap` 使用新目标。不能把旧 scaled Schur 包改一个标签后继续。真正试步仍须按新目标计算完整实际 F；任何同态值包转存都应明确替换实际 gap 残差和身份。$d=0$ 不在此标准化中，R166 的固定正尺度零-gap 表示是另一接口。

## 本次真实检查

最终小检查 `fd2d-gap-row-retarget-check-v3.py` 使用一致的四节点、K2、五参数消元布局，真实 session `64935`、chunk `3aa8dd → 8d9b50`，exit **0**。三个目标 .8/.75/.9 分别与原 `LocalNormalSystem.add` 独立重新装配全部小行比较，normal、gradient、列平方范数及残差平方和最大归一差为 `1.8518445499218924e-16`；全部 field 块、arrow 和 field gradient/norm 字节不变，未更换目标时数值字节全部不变。无关有限定义变更在任何数值改动前被拒绝。

首个通用小行布局检查 `66941 / 837087` 真0，但它的两条初始参数导数并非其 K1 示例的专属中央布局；只记通用 row replacement 检查。第二个检查器改成正确 K2 后，错误地仍把“坏 modes”设成2，导致该负例根本没有改变输入，实际 `6159 / 696be4` exit **1**。第三版只修这一检查器构造，helper 始终未改。三份源码和真实回执均保留。

本次没有重算任何物理 F/J、大 normal、BVP 或 body；尚未将该 helper 用于真实主态的目标变更。R168 的真实高度、全核 held 球、全局 reach 和闭合条件都未因此支付。
