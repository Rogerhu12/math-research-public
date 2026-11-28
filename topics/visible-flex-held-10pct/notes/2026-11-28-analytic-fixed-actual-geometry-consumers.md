# 自身 KIND 的 fixed actual-DN 返回：Cartesian、连续证书及闭图网格入口

日期：2026-11-28。状态：**独立入口准备完成；未有真正该 KIND 的正向返回，因此没有新几何数值、证书或网格。** 原五源 `chord_fixed_support_actual_*` / `run_chord_fixed_support_actual_once.py` 的字节全部保持。

## 1. 已解决的实际接线阻断

原 design gate 与此前 7a reader 都不接受 `original_r53_literal_fixed_metric_actual_dn_v1`。本次给这一真实数值模型单独提供合法入口，保留原 `run.json` 的 KIND、所有 actual-DN / fixed-g 标记及来源，不改旧 gate、不改 run、不把它冒名为 design 或 7a 返回。

另一项真实依赖是跨冻结源码树的导入顺序。fixed 返回的原 7a 锚可能在保留的旧树，而新 numerical/geometry adapter 在显式新树。原锚 gate 会检查实际加载的 `actual_cartesian_prefix.SCRIPTS`。因此四个新模块在顶层均不导入几何 provider；先递归执行真实 fixed gate，回到原 7a 锚并选择其真实树，然后才加载已经核定字节的几何代数。当前树和旧树的共享表示代码同时核 SHA，实际 provider 路径进入新报告。没有通过重标路径或修改旧 gate 绕过这个检查。

## 2. 四个独立源及接口

目录均为 `scripts/resume_20261128/analytic/`。

| 源 | 接口与作用 |
| --- | --- |
| `fixed_actual_cartesian_prefix.py` | `accepted_fixed(run)` 保持自身 gate；`load_fixed_prefix(run)` 用实际 fixed=True flow 重建原 Cartesian 表示；`load_complete_tail(bundle,index,record,view,provenance)` 读全部有限尾和均值，并检查最终 physical-H 身份 |
| `fixed_actual_prefix_continuous.py` | `geometry / tables / metric / cut / preflight` 五个 CLI；复用原区间公式和完整 proof loops，在独立 namespace 只更换真实 source 初始化及来源输出 |
| `fixed_actual_closed_map.py` | `load_closed_map(...)` 与 CLI；原完整 atlas、cut Hermite、短柱、深端 collar、反射和可选 canonical R67 marker，显式记录 cut width |
| `fixed_actual_export_closed_mesh.py` | 闭图 PLY CLI；原 ring 拓扑、全部保存谱的 vector 评价、held frame、双精度坐标与严格 5 MB 门均沿用 |

四源 SHA 和准备检查的绝对路径见同名 JSON。

## 3. 同一 g、physical H 与完整表示

新 reader 首先调用既有 `accepted_actual_input`，递归检查实际 predecessor/原 7a 锚、原 full-DN/八次 outer 预算及全部真实数值门。自身记录中的 `fixed_problem`、完整 `frozen_profile`、字面径向 chart、angular chart、gauge q、warp reference、λ=1、finite mean count、GL6 和 `p0=log(q_actual/q_seed)` 语义不变；δ 不再是设计未知。当前 `physical.npz` 的 SHA 从实际文件重新计算。记录本身不被回写。

尾高只取该返回 `result.height_reference` 所绑定的**最终保存 physical quintic 端点 H**。raw candidate H 单独保留；二者即便逐字节相等，也仍分别记录其角色。完整尾包必须恰好绑定同一 physical reference、factor=1、原 source port，且 request/checkpoint/endpoint 三份完整 H 的字节一致。原 packet、finite spectrum、每个完整 stage、共同 node index、整条 mean chain、manifest、真实 representation provider 和 producer 均保持身份检查。跨树 producer 只允许实际已绑定的 reader/numerical/original-anchor 三棵树及核定字节；不重写 bundle 的原路径。

Cartesian 构造沿用 `ActualR53CartesianPrefix`，包括完整解析 core lift、中心 two-jet 修补、真实 radial chart、所有保存 Fourier 分量及原 finite mean 的共同 Hermite 表示。这个共同 Hermite 表示仍是原已声明的新有限图，不能把 source primitive 的旧连续界移给它。

`FrozenTarget` 由该自身 fixed=True 模型的实际 flow 和该原 run 构造，不借原 design 的参数零列解释目标 g。所有 `geometry/tables/metric/cut` 报告传播完整 fixed problem、实际 physical 文件、最终 physical-H binding 和 adapter/provider SHA。继承未修补区域时，先检查这些自身来源字段全部一致，再执行原精确叶覆盖和同图/同 target 门。

闭图和 mesh 的数值 atlas 方法均继承原公式。cut 宽度是显式输入，本次未为任何新 fixed 场选择或证明宽度。已知另一个 λ=.002 场的 `.12` 结果不在本入口继承范围内。完整尾的 physical-R 与保存半径是否相同，也没有仅因本 reader 构造成功而被宣称已证。

## 4. 后继实际命令合同

以下 `RUN` 必须是真正该自身 KIND 的已接受 `run.json`；`BUNDLE` 必须由它最终 physical-H 生成。`OUT` 均是新的源码树外目录。它们是未来真实输入的命令模板，本次没有代入伪造输入运行。

```bash
python fixed_actual_prefix_continuous.py preflight --source-run RUN --outdir OUT_GATE
python fixed_actual_prefix_continuous.py geometry --source-run RUN --outdir OUT_GEOMETRY
python fixed_actual_prefix_continuous.py tables --source-run RUN --outdir OUT_TABLES
python fixed_actual_prefix_continuous.py metric --tables OUT_TABLES/summary.json --outdir OUT_METRIC
python ../geometry/cartesian_prefix_curvature_rounding.py --certificate OUT_GEOMETRY/summary.json --out OUT_CURVATURE
python fixed_actual_prefix_continuous.py cut --tables OUT_TABLES/summary.json --geometry-bundle BUNDLE --base-metric OUT_METRIC/summary.json --base-geometry OUT_GEOMETRY/summary.json --base-curvature OUT_CURVATURE --cut-width WIDTH --outdir OUT_CUT
python fixed_actual_closed_map.py --source-run RUN --geometry-bundle BUNDLE --cut-width WIDTH --cylinder-half-length .0025 --canonical-r67-marker --outdir OUT_MAP
python fixed_actual_export_closed_mesh.py --source-run RUN --geometry-bundle BUNDLE --cut-width WIDTH --frame held --cylinder-half-length .0025 --outdir OUT_MESH
```

几何/角表/metric 的其余选项、角谱和连续误差门均取原 CLI。每个新返回必须重付它自己的完整连续几何及 metric；图/mesh 输出的 completion、reach、held、非全等、C²-limit 标记均不因表示成功自动置真。

## 5. 本次真实检查与范围

四源均实际编译成功；八个 CLI/help 调用均 exit 0；独立导入四源后，`actual_cartesian_prefix` 和 `actual_closed_map_v2` 均尚未被预缓存，保住先验真实 gate 的顺序。静态检查原四个 proof main 的每个限定替换位置都恰出现一次。五个已冻结 numerical 源 SHA 与此前准备记录一致。

实际准备输出：`held10-analytic-work/fixed-actual-geometry-entry-preparation-20261128/validation.json`，SHA `56ad979c07d631c49523164b836e0808a385dd842436f9d3aac61aefc2a77bbe`。

本次没有 BVP/J、native tail 解、假正向输入、区间场生成、闭图 query、mesh 生成或任何已接受 fixed-DN 数值。实现现在已能接实际返回，数学精化、同图证书及 README 完成义务仍需真实计算和证明。
