# R141 补充：同选定成员的真实外 Robin 与物理均值两值实际完成

2026-11-20，维护会话 `visible-exact-astra-ac637-20261120`。

## OA.1 完整实际结果

[公开 Actions 44769445246/1](https://github.com/Rogerhu12/math-research-public/actions/runs/44769445246)
已完成唯一科学 child，18/18 门为 true，两个完整新 scalar 均保存、原子读回，
并核包含原 directed upper。完整原件为：

| 文件 | bytes | SHA256 |
|---|---:|---|
| [selected-physical-outer-values.json](../notes/selected_physical_outer_values_ci/run-44769445246-1/selected-physical-outer-values.json) | 33599 | `db6f827c7eaa410a7769c673eba39838b6f35ba7e683c99cea62c8e0dcda3caa` |
| [execution.json](../notes/selected_physical_outer_values_ci/run-44769445246-1/execution.json) | 13544 | `70ad7e1994a5ab228ac202d1ab1ce64a4db6ca0c279a2ae260c309479b357674` |

科学 `complete=proved=true`，execution `complete=true`，两者 `failure=null`，
child 返回 0，无 timeout。触发提交
`3814487cdd407f87210901779af452ef76cac207`；实际科学 checkout
`b0a543e7b1d0488eb1ac8dfe31a4cb21cef3ddf0`。
Python 3.12.14、python-flint 0.9.0、320 bits、四线程环境均为 1。
数学时间约 0.017978238 秒，完整 child 约 0.205160745 秒。

这里消费的是 [O.1–14 的完整实际值公式](R141-supplement-selected-physical-outer-residual-values.md)，
不是把 DN 导数或背景半径改成边界残差。candidate、连续中心、完整193态方向、
固定内禀 $\eta_0$ 与同一物理外图的所有原身份和适用域保持不变。
原 implicit $\delta_*$ 只由 $|\delta_*|<9.368259853002\cdot10^{-11}<10^{-10}$
限制进入本次 uniform 球；没有用半径端点取代它。

## OA.2 两个完整物理上界

对于同一个原许可背景 $f_B$、$\|f_B\|_{\dot A^2}\le2^{-60}$，
保持原 physical-circle 归一化测度、完整物理 Fourier 尾和独立 mean，实际得到

$$
\boxed{\|r_B\|_{H^{-5/6}(\theta)}<1.259356\cdot10^{-15},
\qquad |r_C|<2.048247\cdot10^{-19}.}
\tag{OA.1}
$$

两个输出的原字段和完整球为：

| 字段 | 原完整保存 ball |
|---|---|
| `complete_selected_physical_Robin_Hminus5over6_upper` | `[1.2593558904591647170632173328315176115213117140340709172940136044814134387920173e-15 +/- 1.14e-96]` |
| `complete_selected_independent_physical_mean_residual_upper` | `[2.0482466897431893464180361586220460496755669823926758504328164690258183086614462e-19 +/- 3.11e-99]` |

(OA.1) 仅是向外简写；消费者使用整球的 upper。
Newton 符号与真实定义为

$$
r_B=-\{J_\theta B_{\delta_*}+Q_\theta\mathcal Z_{\delta_*}
                 -d(\mathcal Z_{\delta_*},f_B)\},
$$
$$
r_C=-\{m_{\delta_*}^{-1}-C_{ref}
                 -c_0(\mathcal Z_{\delta_*},f_B)\}.
\tag{OA.2}
$$

物理均值是准确的 $1/m$，不是 $m$ 的差，也不是 $m-1$。
两上界都未除以原幅度，未提前乘未知 endpoint 坐标的 $\Theta$。
后继 [真实物理源对](R141-supplement-actual-physical-source-pairs-and-reusable-bounds.md)
必须仍按原 WOB high affine 与 raw low endpoint 两条路径各自接入。

## OA.3 同物理角与完整 mean 的已付变化

本次先保存了三个完整预算阶段：moving increment、same physical inverse angle、
fixed-$\theta$ 的 $B/C/1/m$ 差。原球给出的方便范围包括

$$
\Delta B<4.707213\cdot10^{-19},\qquad
\Delta C<4.973087\cdot10^{-19},\qquad
\Delta(1/m)<2.391152\cdot10^{-23}.
\tag{OA.3}
$$

这些是 (O.3–10) 的不同预算，不能互相替代或将其中某项设零。
真实 $|v|$ gap 的保存 lower 大于 5.79999999999，原逆角导数的 lower
大于 0.999999999998；同物理角的 inverse lift 差完整 upper
小于 $1.191907\cdot10^{-19}$。

原 F.20 的实际非线性端值给 $R_B^0,R_C^0$，旧 whole DN 给 $T,M$。
本次按原 O.12 得到新的实际值

$$
R_B^{sel}=R_B^0+\Delta B+(1+T)\Delta C,
\qquad
R_C^{sel}=R_C^0+\Delta(1/m)+M\Delta C.
\tag{OA.4}
$$

物理 $B$ 的变化由同角商差和两个真实 inverse-angle lifts 控制；
primitive 的 $1/4$ 与独立 moving mean 两项均已付。
原 full-family $C$ 费用有明确“共同同伦导数界乘方向幅度”的定义，故只该项
缩 $1/100$；连续 repair 不缩。全物理 $\mathcal Z$ 线段处于原 $10^{-12}$
图域，$f_B$ 完全相同，允许使用原两个完整 DN 行。
这不是从一个任意有限差值上界反推导数，也不是假设同阶复合算子差小。

## OA.4 原件与全部门的保留

[首次 manifest](../notes/2026-11-20-R141-selected-physical-outer-values-inputs.json)
13704 bytes，SHA256
`d7f5bdffb5c51258c1883f6bdabc24002a7dc5f6d4b00a7779bc7e8f7932c762`。
23 个当前输入逐 bytes/SHA/blob 固定并与实际 receipt 一致。
唯一历史原件是完整 raw boundary gzip：84003 bytes，SHA256
`bb2767633225f19f27c6c2646ac47c1142352a3a03882c916868e079f0fb055a`，
commit `46f127c7153f5393dcd2a00f42d4c1d3662c294d`，
blob `aded3d60581649518060190c49e7d0524365ada5`。
原容器完整恢复，没有重做任何原 physical Fourier 矩或端点 producer。

原 raw 13 门、repaired outer 25 门、whole-family outer 25 门、exact full193
direction endpoint 14 门、NIF 16 门及 WOBSA 18 门全部在准入时保留。
19 条完整旧 interval 与非零独立 $Z_m$ 准确有理数完整复制在结果中；
whole native/process 与 actual/execution 的身份绑定没有变为孤立数字准入。
所有旧 producer、old scientific import、old successful target、新数组、
artifact 和 Release 计数均为 0。

execution 记录 5 次 pull 后 README 检查，完整保留首条与末三条；
留存 receipt 的实际 diff 及相对已读规则提交
`96edc677044b6ad7c7fd3aa2f65bf77d9c0e27a1` 的 diff 均为空。
这里不声称已独立恢复未在小 execution 中留存的第二条。

## OA.5 继续独立的七项义务

原结果明确保持以下七项未完成：实际 height RHS；far regular label/height gauge；
已知 $Z$ proposal 的真实 $\nu$ 响应边界 discrepancy；negative/germ/interface/root
输入；两条完整 WPN RHS；全无限维逆；非线性解。

特别地，$2^{-60}$ 只是同一个允许背景的半径，不能作为 Newton height RHS。
角共轭 $\mathcal H_*$ 也不是外高度。对纯 $\nu$ 的显式 exterior 源为零，
并不使已知 proposal $Z$ 的边界 discrepancy 自动为零。
本次两值加上 [NA 普通正侧七源](R141-supplement-actual-complete-positive-Newton-source.md)
只填入其各自的真实源槽；low193、97+96 物理外行、future224/future32、
全部 matching 与最终固定度量可见闭族仍需原各门全部闭合。
