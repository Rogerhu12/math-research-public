# q060 真锚的 M8 圆弧初猜：完整原域通过，未解 BVP

**可信度：启发式/有限数值证据。** 按已冻结的唯一 q 与完整两jet规则，
单次最小初猜实际完成；原核心数值正性与初始 Frenet 域通过，
八个尾高度分量重新编码后与旧 actual 锚逐位全同。
初始 collocation RMS 仍为 `1.4166287468767744`，没有形成新接受解。
本次没有调用 BVP、实际 DN、参数扫描或原 `restart`。

## 实际输入与物理系数

使用 `q060_circle_trace_design.py` SHA
`2d9054efe56f8c0374b4cf12708a162de87e8857f90489d9c6674085f859b92e`，
与 metadata 阶段逐位同源。
输入为原 q060 已接受余弦 M8/25 态锚，
以及冻结 plan `ce2533b9bb0342fdcb6a7c81560281e8ef47ace3798e0e9e79fc1b44a176d1fc`。
新设计身份为 `19d09a8199b4f91ab2479f736dc7763d506b8eae1af671ea5369927cbc80171a`。

本次实际调用了独立原 `native_reference()`；
执行记录明确 `native_reference_constructed=True`。
这与原 binding 的静态 metadata 旗 False 分开。
旧 core、旧 Flow 和完整 physical quintic 没有被新 factory/lift 修改。
新 Flow 单独安装一次实际 integral core lift。

新 M8 控制空间为 `B2..B6,T,U`，目标设置仍是
`lambda=1,a=.21,bp=.32,bc=.4,center=pi/3,eta=0,lock=True`。
唯一主矩幅值为 `.05210565550627671`。
使用原最终 `delta=.06104275721220832`、原 chart、`warp_reference=.06` 和
`Lbin=1.3602524132788236`；新 `p0=0`，未重复施加旧历史 delta 参数。

| 完整中心两jet映射 | 实际读数 |
|---|---:|
| 旧完整七系数核心中心 `h` | `.9405029417351826` |
| 旧完整七系数核心中心 `rho` | `1.4606246268051888` |
| 新 zero-trace 参考中心 `h` | `.9406765345322124` |
| 新 zero-trace 参考中心 `rho` | `1.4168452440502137` |
| 新 `t=A` | `.04377938275497506` |
| 新 `u` | `−.00017359279702988673` |
| 新 `B=u−t` | `−.04395297555200495` |
| 新完整中心 `h / rho` 相对旧值的差 | `0 / 0` |

旧全部七个物理控制均进入旧中心值。
新自由空间仅保留旧五个前导系数，移出旧 $c_7,c_8$；
它们没有被先从旧参考图或旧中心值删除。
新坐标链仍为 $c=p_{\rm controls}\,\mathrm{pscale}$。
collector 核对全部七个实际乘积与记录逐位同；
五个保留控制相对意图原值的最大重编码差为 `6.776263578034403e-21`。
全部物理控制、参数和尺度在紧凑记录中完整列出。

## 原数值门及初始残差

合并 T/U 后的解析组合导数界按已登记新 core 计算，未拆列丢掉抵消。
`rho>1e-5`、原值余量和每扇区最大格点数 32768 都没有改。

| 实际有限读数 | 数值 |
|---|---:|
| 数值 `rho` 充分下界 | `.49475279238494585` |
| 每扇区所用格点数 | `512` |
| `rho` 采样最小 | `.496879221074452` |
| 新圆弧半径读数 | `1.4606246268051888` |
| 初始网格节点数 | `271`，来自 257 点加原 profile 接点 |
| collocation RMS | `1.4166287468767744` |
| collocation residual 最大 | `.004882920486310857` |
| 初始 boundary residual | `9.183586165393577e-12` |
| 初始 Frenet margin 采样最小 | `.002485877078970633` |
| C² 入口修复后的系数误差 | `0` |

core guard 是保留原门的数值充分判据，不是完整曲面或 libm 的严格证书。
零中心差和零入口误差也只是实际有限求值结果。

4096 角点回投在 C² 修复前的表示部分位置/角一阶/角二阶分量差分别为
`.0001858625006072312`、`.005381401046062384`、`.21694413331065499`。
这里只比较 `geo+完整25态 Fourier 场`。
平均高度不在该状态中，本次 `mean_height_reconstructed=False`；
真实平均高度仍须原 `flow.height_integral` 重建。
没有计算完整三维图的 metric，也不能据这些表示差作全图误差或同 g 收敛断言。

## 完整八项 H 编码

原实际尾的完整 H 通过 `H_old/(sigma*q_new)` 重编码。
再按原式乘回后的八项全部与原 H 逐位相同：

- 改变分量列表 `[]`；
- 最大差 `0`；
- 两边 binary64 SHA 都为
  `36f201a193e1fd50b764af622d81d0b359e1a1a29e0f2608c2ebb73b06e6b2df`。

原全 H、实际乘回的全 H 和八项比较都在紧凑记录中保留。
相对单纯回投末端系数的覆盖差最大为 `2.371692252312041e-19`。
本次只读取原已接受 response 与 208 项 Jacobian 作初始残差的 affine 锚；
虽然 H 相同，也没有伪造一次新的 native 调用或新的尾求解事件。

## 退出证据与复现

独立 observer `resume_n4/observe_command_live.py` 没有改子命令。
终态工具 chunk `3b93aa` 返回 `exit 0`；
observer 于 `2026-11-18 01:37:17 UTC` 记录 `child_returncode=0`，
子命令观察时长约 `4.0020 s`，探针自身约 `3.1740 s`。

运行目录为 `m3_work/q060-circle-trace-initializer-v1/`，
其中 `resource.json`、`resource-live.json`、完整合并 stdout/stderr 日志和结果均保留。
原始结果 SHA 为
`974ee6c90a142e983e91acfa8cd86bdda6aaa8ff9f7b7a33823480aad2a78538`。
collector 仅读已完成结果、observer、全部绑定源及实际 H/参数链，未重跑数值探针。

```bash
python topics/visible-flex-held-10pct/scripts/resume_n4/observe_command_live.py \
  --out /workspace/scratch/7322d0dee069/m3_work/q060-circle-trace-initializer-v1/resource.json \
  --log /workspace/scratch/7322d0dee069/m3_work/q060-circle-trace-initializer-v1/stdout.log -- \
  python topics/visible-flex-held-10pct/scripts/resume_m3/q060_circle_trace_design.py \
  --reference-binding /workspace/scratch/7322d0dee069/math-research-public/topics/visible-flex-held-10pct/scripts/resume_closed/q060_cosine_reference_binding.json \
  --out /workspace/scratch/7322d0dee069/m3_work/q060-circle-trace-initializer-v1/initializer.json \
  --evaluate-initializer \
  --evaluation-plan /workspace/scratch/7322d0dee069/m3_work/q060-circle-trace-design-plan.json
```

已完成目录禁止覆盖；复现时只给输出使用新路径，参数与冻结计划不变。
新增记录为 `collect_q060_circle_trace_initializer.py` 和
`q060_circle_trace_initializer_terminal.json`。
新圆弧空间的完整 BVP、actual 联立、完整 metric 及几何比例仍未完成；
本条不继承 R38/R40/R41 数值预算。
