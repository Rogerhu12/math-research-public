# R671 新解析尾：完整自由空间 Phi–QP 接线

日期：2026-11-20。会话：Astra-resume-public-20261120 / fullclosed_solver。

**状态：完整新源码与可重建命令已写成，只做源码阅读、AST 与 argv 参数核对；没有执行新科学计算。** 后续迁移、真实场读出和方向求解仅在本仓库公开 GitHub Actions 运行。旧 `.992/.998` 对照、旧完整空间 driver 与正在运行的重建链均保持原字节。

本条接 [R671](../results/R671-exact-reference-tail-affine-lift.md) 的新表示与 `exact_reference_tail_lift.py` 工厂，不登记新接受点，也不继承旧场的有限点通过标签或连续证书。

## 1. 完整新源及身份

新源放在 `scripts/resume_20261120/`：

| 源文件 | 字节数 | SHA256 |
|---|---:|---|
| `fullclosed_gauss_exact_tail_inequality_qp.py` | 44585 | `b1b0725acffde7958d9a4ad245057ea243d4319bde15bd9a7778ade3b0f844e8` |
| `launch_full_phi_exact_tail_actions.py` | 8415 | `c9ba1d73db3e3608dffa1dbc9aeeda2a355d2ff4c2b9fc8eed2140c985869ec7` |

依赖工厂当前完整源码 SHA256 为 `2e0219c50543d859a9c649553bc4dde863df24daab26ffa75e5112baa4a90216`；运行时再次记录实际 factory/source/input SHA。它的接口和 scalar carrier 误差范围由相应工厂说明完整给出。

新 launcher 仅通过旧 `launch_full_phi_qp_actions.py --print-command` 获取原完整参数列表；不导入科学模块。随后替换 driver 路径，显式增加 R671 参数，保留全部旧求解参数和永久位置输入。实际子进程限制为一条 BLAS 线程，要求 `GITHUB_ACTIONS=true`，且拒绝覆盖已有输出。准备模式不创建输出目录或读取场数组。

已做的参数核对仅为：一个含显式 `lambda=1`、`source_lambda=0`、`nodal-projection` 的准备命令产生 59 个合法 driver flag；coarse 源为 v3，QP 源为 R668 v2。它不测试新模型、数值导数、可行性或收敛。

## 2. 哪些物理入口使用新表示

固定本次模型参数 $\lambda$，实际场是

$$
F=q+f_\lambda e_r(\Theta)+(h_\lambda H+k_\lambda)e_z.
$$

全部旧自由变量和原 $a\rho$ 分母保留；$\lambda$ 不是此次 QP 的未知量。新报告使用 `original_free_coordinates_preserved`，不把旧物理仿射空间称为不变。

| 消费处 | 实际绑定 |
|---|---|
| 全部原节点/中点及 Gauss 行的 residual/Jv/VJP | `ctx.create_pair` 返回的 observed 对象 |
| 构造 coarse $B/B^T$ 的原节点模板 | 同一 `ctx.create_pair` 返回的 native 对象 |
| 全观察网格位置、速度和二阶导数 | context-owned `six_jets`，含 $k,k_s,k_{ss}$ |
| 几何 working rows 的 stage 场 | `geometry_module.fields_block = exact_tail.fields_block_observed` |
| 全部永久任意点真读、曲率/半径 cotangent | `exact_tail.point_adapter(original_point_module)` 的隔离命名空间 |
| 物理高度方向 | native 的新 `_lift_scalar` 给出 $B_H=(q_Z=b-h_\lambda,H=1)$ |
| 同范数 coarse 白化 | 用该实际 $B_H$ 的 `PhysicalHeight` 与原完整 DI/角尺度 |
| 接受点与终态 NPZ | `ctx.bundle_arrays(problem,x)` 加本次源与 profile SHA |

固定的 $k$ 没有独立自由变量方向，因此 Jv/VJP 和点 cotangent 只需要前六 scalar 列 $(h,h_s,h_{ss},f,f_s,f_{ss})$。但所有基场必须含 $k_s$，所有几何读出必须含 $k,k_{ss}$；否则 Gram 微分和曲率会针对另一个场。新 driver 没有只更换 residual。

上述 native 对象仅生成原节点结构上的 $B/B^T$，不用于替换全 Gauss 目标。旧 `geometry-observed-source` 路径保留在完整参数/身份列表中以便与旧 launcher 对应，但不会加载；报告明确把它列为兼容性身份。真正 stage 几何适配来自新 factory。

## 3. 高度坐标和白化没有遗漏新的补偿

令

$$
b(s)=10(s/S)^3-15(s/S)^4+6(s/S)^5,
\qquad B_H=(q_Z=b-h_\lambda,H=1).
$$

因为 $h_\lambda$ 在原节点划分上分段五次，$q_Z=b-h_\lambda$ 由原共享三 jet 精确表示。实际方向 $\delta F=b(s)e_z$。令 $v_q=B_H-e_H$，则

$$
A=I+v_qe_H^T,\qquad e_H^Tv_q=0,
\qquad A^{-1}=I-v_qe_H^T.
$$

完整右变换与转置仍为

$$
T(z_i,z_c)=A\,\mathrm{DI.lift}(z_i)+BRz_c,
$$

$$
T^Tg=\bigl(\mathrm{DI.pullback}(A^Tg),\ R^TB^Tg\bigr).
$$

这里 $R$ 是在同一新范数下的 coarse 白化。高度尺度继续使用

$$
\int_0^S|b''(s)|^2\,ds=\frac{120}{7S^3},
\qquad s_H=\sqrt{\frac{7S^3}{120}}.
$$

其余尺度沿用已声明的 $\nu_c=24$ 正角转折：在原 $A/E/D$/core 尺度上除以 $\sqrt{1+(\nu/24)^2}$，高度尺度不另改。原全部 $A/E/D$、端口投影和粗附加列都保留。这个坐标范数不是精确几何弯曲能量；改变 lift 后也不宣称相同 $\mu$ 具有旧场的相同经验效果。

原正谱目标参数 $p=8,\epsilon=.001,\mathrm{scale}=.05$ 和正 residual Hessian 桥不变。桥外系数仍为 $1600/C_0$，$C_0=(\sum_s w_s)N_{\mathrm{full}}$，$w_s$ 是原正混合径向权。QP 阻尼项为 $\mu^2\|z\|^2/2$，按相同 mean-Phi 单位解释，不再乘除一次 $C_0$。虚拟 RHS 范数仍不是实际 Phi。

## 4. 初猜、真正筛选与输出身份

输入旧父首先只用于读取实际 $q/H$。`keep-q` 保留这些坐标；`nodal-projection` 使用工厂的明确有限角节点投影。两者都是新表示下的初猜，不算已接受方向，不能声称连续场相等。

canonical `reference_tail_lambda` 优先决定输入模型参数；它与补充的 `exact_tail_lambda` 冲突时立即报错。显式 `--source-lambda` 也必须与实际 tag 一致。非零 source lambda 由工厂核对原 `reference_tail_model_json` 中的 scalar、mesh、$\eta$ 和各源身份；不得仅改 SHA 或标签来冒充同一场。

迁移后，driver 重新计算端口结构、全部当前 metric 行、全观察网格六 jet、所有输入永久曲率与半径位置。新场必须实际通过所声明的有限点 screen，才从 $z=0$ 开始可行 QP；这里没有 Phase-I 实现。若初猜未通过，报告保留新初猜和真实失败读数并写明没有进入线性迭代，不能借旧父通过标签继续。

新完整 QP 与原 driver 保持：

- 所有当前线性行使用真实非负余量，边界余量可以为零；R668 v2 可在合法下降方向上提前释放负乘子面。
- bounded working set 只影响线性模型，所有永久位置继续参与每次真实非线性筛选。
- 真正回溯用新场的实际 Phi、正 metric、曲率及半径；新增真实峰进入永久记忆。
- 数值 `.992` 等 margin 只是算法选择，README 的最终 reach 标准不变。有限点乘积不等于连续 reach。

报告中的 `affine` 针对**实际迁移后**坐标和新 core/cap lift；旧父 pack 检查单独存为 `parent_coordinate_check`。所有 $\lambda$（包括直接使用原类的 $\lambda=0$）都显式用 `2*(J-1)` 读取帽节点，不把最后新增 Gauss 行冒充帽。context 自身的 `nonlinear_solve_performed=False` 仅说明 factory 构造不求解；driver 的真实方向表是后继求解状态。

NPZ 通过工厂白名单保留必要原 scalar 字段、当前 $q/H$/core 及新 canonical 模型 tags；旧场诊断/证书不复制。raw `exact-tail-lift-profiles.npz`、其 JSON manifest、各方向数组、接受点与 `final.npz` 留在本 Actions work。公开结论只保留小源码、参数、run 与实际 SHA。

旧独立 `full_phi_saved_ray_slope.py` 只会构造旧 lift，不能直接消费新 R671 bundle。旧 coarse `ArbitraryField`、旧多项式连续 Gram/曲率内核同样需要明确新表示适配；本条不把它们列作已兼容，也不继承相应旧证书。

## 5. 完整可重建 Actions 命令

`REPO` 是当前源码 checkout，`WORK` 是同 job 已重建的实际数据目录。`PARENT`、`MANIFEST`、`MU` 必须来自当时真实输出；不能用旧哈希或旧数值冒充新的父。以下 `885`、`lambda=1` 是一个明确的未试算模型参数，$\eta$ 终点由工厂准确查出原符号 $S-\mathrm{width}$ 节点，当前为 894。

```bash
python "$REPO/topics/visible-flex-larger-amplitude/scripts/resume_20261120/launch_full_phi_exact_tail_actions.py" \
  --repo "$REPO" --work "$WORK" \
  --bundle "$PARENT" \
  --carrier "$WORK/recover_evidence/gauss6-current-three/same-scalar-gauss-observations.npz" \
  --manifest "$MANIFEST" \
  --node-report "$WORK/fullclosed_solver/data/fullclosed-hold-warm.json" \
  --scalar-input "$WORK/fullclosed_solver/data/pulse-a5-complete-base.json.gz" \
  --eta-start-node 885 --lambda-value 1 --source-lambda 0 \
  --migration nodal-projection --damping "$MU" \
  --directions 1 --maxiter 256 --active-rows 192 \
  --reach-safety-factor .992 --active-band .025 \
  --outdir "$WORK/exact-tail-full-phi-first"
```

重复 `--manifest` 可以加入更多完整永久位置参数，不覆盖原集合。若父已是匹配的 R671 模型，应声明它真实的 source lambda，并选择清楚的迁移方式。加 `--print-command` 只构造完整 argv；实际执行还会写完整 command plan、全部输入/源 SHA、GitHub run/commit，再调用新 driver。

默认完整参数由冻结旧 launcher 明确给出：原 observed/dense/batch、DI/helper、R668 QP/行选择源、m12/r22 coarse、全部谱目标与容差、15 次真实回溯、目标 $5\times10^{-7}$。因此没有隐含的旧环境绝对路径、未保存脚本或额外 fixture。当前只完成新实现接线，尚无新科学结果。

## 6. 对实际源码的连接核对

以下只来自完整相关源码的文本与 AST 核对，不是数值检查或新的启动门槛。

非零分支的 MRO 是 `ReferenceTailMixin → ObservationMixin → BatchedMixin → ClosedGram`。构造时 `_reference_ready=False`，先由原类建立字面旧表；Observation 扩为全部当前行后，Reference 才替换为共同九列表。native 对象复用该表的 legacy 前缀并核其旧六列字面一致，避免分别构造两个新模型。

`set_base`、未缓存 residual、Jv 和 VJP 都通过动态 `_first_batch_uncached/_first_batch` 取基场，因此固定 $k_s$ 恰进入一次实际 $F_s$，也进入谱桥用来形成 block Hessian 的真实残差。core 方向仍给

$$
\delta F_s=\delta q_s+f_s\delta\Theta\,e_\theta+h_s\delta H\,e_z,
\qquad
\delta F_\phi=\delta q_\phi+
f(\delta\rho\,e_\theta-\rho\delta\Theta\,e_r).
$$

VJP 中相同 $f_s,f$ 的角度项、$\rho$ 项和原 $a\rho$ 分母项全部保留；固定 $k$ 的方向导数为零不等于把它从基场删除。

任意点 adapter 克隆并重绑定原模块中函数的 globals，所以 `witness_geometry` 和 working-row 函数实际调用新的 `fields_at/pullback_at`。前者读完整九列，后者以同一点的新前六列构造 stage view，然后执行完整自由 core/node/H 的原准确转置。stage working rows 则直接读新 `six_jets` 与 `lift_scalar`，没有另一个旧任意点实例。

物理高度列来自 native 的新节点 profile；coarse 范数的字面式是 `DI.inverse(A^-1 B)/scale`，与完整空间使用的 $A$ 相同。NPZ 的 canonical lambda、补充 lambda 与模型 JSON 在非零迁移时相互核对；从零模型迁移也不会继承旧场几何值。

本轮找到并修正的具体报告问题是：$\lambda=0$ 返回的原类，其旧 `affine_diagnostics` 把最后 Gauss 行作帽。新 driver 对所有 $\lambda$ 均用 `2*(J-1)` 覆写为真正帽三 jet；非零工厂自身也使用同一帽索引。没有修改已发布旧源，当前未发现其它连接不匹配。实际有限精度导数、迁移可行性和下降仍以公开 Actions 的真实结果为准。

## 7. 本轮明确排队

本条发布时在同一公开run44748103105/1排入continue-R671-full-phi-first-01，父为实际c4a3f010691c8e9d1a1d9a8b26bfe4bc9b136efecf8fc3a9426ecddf28289080，完整返回manifest db108e8241b7c4b8a9ba4e1f4c48d26415e9c2ca002a042d45c11b9e7bc2fa1d。固定lambda=1、eta_start_node=885、source_lambda=0、nodal-projection，明确mu=.0007539530259341321，1完整方向/256步/192行/.992与.025，全部7377观察行、2048圆周角及永久点保持。原node/scalar/carrier均来自同job已有重建链。精确完整命令和输出路径入computations/resume-20261120-followups.json；这是新场准备与求解请求，不是已接受结果。

执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
