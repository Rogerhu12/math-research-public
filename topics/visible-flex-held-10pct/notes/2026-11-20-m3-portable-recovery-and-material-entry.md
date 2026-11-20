# m3：失去旧 scratch 后的最短恢复入口与新材料曲率核

维护：Astra-held10-1b6d88ec-20261120 / m3_continue。**状态：工程恢复与有限初值观察；没有合格闭面。**

## 1. 原 λ=.82 终态仍未知

当前文件系统没有 `/workspace/scratch/7322d0dee069`。原 `trace-path-lam082-native-coupled-v1` 的 raw、observer、返回 checkpoint 均不可读。不能由此把旧作业写成数值失败或成功，也不能把新计算说成接到了原 Newton 控制流。

原公开记录保留的是源、参数、哈希和标量；它们足以再生计算输入，却不包含完整场。继续工作时允许再生必要数组，但不将已经登记的结论重新记为新数学结果。

## 2. 可搬迁的恢复入口

`scripts/resume_m3/portable_bootstrap.py` 从已提交的 `m3_source_recovery_manifest.json` 恢复 70 个原源文件，再安装既有 sparse-v2 全节点线性求解。随后由公开的物理参数生成原 m3 的两份有限线性端口，并从 `fast45-reference-profile.json` 生成数值角图。它不需要任何旧 scratch 路径或旧 launch-plan。

本次实际完成的源恢复 manifest SHA-256 为
`8e177f9cd0ab54d6db1d29baff4faad5ba5fda5f073c4743ab55d35dda73576e`。
原 sparse-v2 stage 源恢复为
`fdf5943ea9655f98cacd2c749d0155cfad08111c88915ce31b2c832bea68d68e`，
与既有记录相同。

新生成角图 SHA-256 为
`dc85dda524e03896b4afa552bd1f859b73cf96f88033565ff910e227034f2f93`；
它不是旧未保存角图 `14f326e2…` 的逐字恢复。新图由既有公开线性构造给出，本次记录其自身身份；不移用旧数组的逐位结论。物理度量仍由明确的 meridian/tail 参数定义，角图是数值坐标。

复现输入的一条命令（在仓库根目录，输出目录须不存在）：

```bash
python topics/visible-flex-held-10pct/scripts/resume_m3/portable_bootstrap.py \
  --repo "$PWD" --workdir /tmp/held10-m3-recovery
```

`portable_prefix_solve.py` 直接读取这些源、物理轮廓、角图、端口和可选 raw 初值。原 Frenet 方程、初边值条件、实际尾容差及 8 次 outer 预算保持。每次内层返回立即保存完整 raw，然后才作实际尾/C²图/metric；有限线性端口和真正非线性尾明确分开。没有要求重演旧 metadata 层或重新审查已证明结论。

## 3. 本次必要再生的实际观察

从公开 q=.06 全部控制和线性场冷启动，415 节点初态实际通过 Frenet 域检查。随后线性端口 BVP 在 90.72 秒时于原 RMS 的附加采样点遇到 `margin=-8.147854868378467e-6`，未返回接受态。这是新冷启动的失败，不推翻原 q=.06 真联立锚。

恢复入口随后加入此前已有的五点域检查：原 collocation 返回 tuple/Jacobian/merit/tolerance 不变，只在试步时同步检查原 RMS 的另外两个点，避免域错误到 RMS 后才逃逸。这不降低任何接受门。

## 4. 新材料曲率核已经进入原几何方程

几何线的新 `resume_transfer/material_curvature_core.py` 在单位材料弧长上规定保护弧的常曲率；其 q 与 corrections 是**材料曲率参数**，不能称为旧支撑函数 Fourier 系数。独立 `material_core_factory.py` 将旧数值 pscale 用可逆对角链式变换改为每列 .01 的实际曲率控制，并同步变换位置及两 jet 的参数导数。

本次实际初值为：n=3，q=.01（保护弧 κ=.92）、材料半宽 .20、过渡宽 .25、M8、角点 256、所有曲率控制零；使用原轮廓和本次再生角图。它于 5.64 秒完成初态检查，415 节点完整 Frenet RHS 有限，最大模约 4.59300523。未提升任何 domain floor。

原 M8 投影在入口的误差为位置 `1.251133010567255e-5`、一阶 `3.8651854404201107e-4`、二阶 `.012606921562159767`、metric `8.009470162903704e-6`。生产表示使用原未投影 reference lift；因此入口公式保留原积分核，但这些数值不构成积分误差或全图 metric 证书。对应 probe 记录 SHA-256：
`8cc2a86727f78972f4ca94dafa906d1882005d55111fa96e6c5bd7954a77a649`。

源身份：

| 文件 | SHA-256 |
|---|---|
| portable_bootstrap.py | `577f05cb4d55995715998f09f4489f20e4c60a5aac10bd0daacdf8ba4208e827` |
| portable_prefix_solve.py | `d3f06f485b36682648428ffc7a3a990b49add4685a8d832be0ee261680fafef9` |
| material_core_factory.py | `f6fb2fd2fad6ce76ac9317f7e12dabba333a522e861e0fa3909436f542e55333` |

本条发布时该新核的有限线性端口 BVP 已启动，尚无终态；后续按实际返回单独登记。真正非线性尾、全图 metric、加密收敛、闭合与 10% 几何全部仍待完成。可再生数组只留 scratch。

## 5. 新核 probe 与完整线性 BVP 的命令

下面承接第2节的 bootstrap 输出。全部核心标量见已提交的
`scripts/resume_m3/material_core_q010.json`；物理 meridian 与 tail 参数来自
`resume_closed/q060_cosine_reference_binding.json`，数值角图由
`nonlinear_tail/m3_coupled_seed_deliverable/fast45-reference-profile.json` 再生。
这条命令没有 `--tail-config`，所以只求有限线性端口，不能当成实际尾接受。

```bash
HELD_REPO="$PWD"
HELD_WORK=/tmp/held10-m3-recovery
HELD_SCRIPT="$HELD_REPO/topics/visible-flex-held-10pct/scripts/resume_m3"
HELD_ARGS=(
  --source-topic "$HELD_WORK/runtime-source/bundle/topics/visible-flexible-closed-surface"
  --short-bridge "$HELD_WORK/runtime-source/bundle/topics/visible-flex-larger-amplitude/computations/root_short_bridge.py"
  --profile "$HELD_WORK/inputs/q060-profile.json"
  --chart "$HELD_WORK/inputs/reference/chart.json"
  --port "$HELD_WORK/inputs/q060-port.json"
  --core-module "$HELD_SCRIPT/material_core_factory.py"
  --core-config "$HELD_SCRIPT/material_core_q010.json"
  --amplitude .01 --warp-reference .01
  --modes 8 --angular 256 --audit-angular 512
  --nodes 401 --max-nodes 6000 --tol 1e-6 --bc-tol 1e-7 --physical-bc-tol 2e-9
)
python "$HELD_SCRIPT/portable_prefix_solve.py" "${HELD_ARGS[@]}" \
  --outdir "$HELD_WORK/material-probe" --probe-only
python "$HELD_SCRIPT/portable_prefix_solve.py" "${HELD_ARGS[@]}" \
  --outdir "$HELD_WORK/material-linear"
```

本次实际 scratch 采用等价的手工 bootstrap 路径：source 为
`/workspace/scratch/1b6d88ecddf3/m3-work/runtime-source/bundle/topics/visible-flexible-closed-surface`，
输入在 `m3-work/bootstrap/`，probe 和 BVP 输出分别在
`m3-work/material/q010-probe/` 与 `m3-work/material/q010-linear/`。
完整实际命令、各输入哈希和运行标量保存在各自 `run.json`。
probe 的真实 tool session 为35274，exit0；当前BVP session为10685，尚待真实终态。
