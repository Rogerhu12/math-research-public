# λ1、a=.01：前缀仍失败，完整 metric 与真实尾已返回

状态：**完整失败终态，不是可接受圆弧锚点**。本条接已登记的小半宽入口：从原 accepted raw `λ=.02/M16` 的物理输入出发，只把新的精确圆弧半宽从 `.21` 改为 `.01`，其余 `q=.03991248545080898`、主过渡 `.32`、控制过渡 `.4`、共享 C² 初猜、二阶数值 rho guard 与原 BVP/尾门保持。原输入本身的完整 metric 也未过门；“accepted”仅指其有限原求解门。

## 1. 原求解的实际终态

运行目录：`m3_work/beta4625-q039912-raw-lam1-a001-b032-w040-m16-c2guard`。观察器 session `19739` 于 `2026-11-18 00:42:39 UTC` 记录真实进程 `exit 0`；总观察时长 `1696.1787343 s`。程序正常结束并保存失败结果，退出码不表示数学接受。原 worker 关闭时也为 `exit 0`，4 次调用，stderr 为 0 字节。

| 项目 | 原运行终态 |
|---|---:|
| inner success | false |
| 原停止原因 | The maximum number of mesh nodes is exceeded. |
| 最后节点数 / 原节点上限 | 3129 / 6000 |
| 最大 RMS collocation residual | 0.3830013242682846 |
| Newton calls / accepted steps | 2 / 9 |
| domain rejects / merit rejects / no-step | 69 / 39 / 1 |
| 最小已接受步长 alpha | 9.5367431640625e−7 |
| 最终 delta | 0.06085676603520699 |
| actual q | 0.03991248545080898 |

节点上限停止指原求解器的继续加点决策超过允许数量，不是已经把网格填到 6000。69 次域拒的具体类型没有逐试步记录，不能把它们全部归给核心正性或 Frenet 条件。

最终物理 quintic 快照 SHA 为 `0335bc65c1afbdfc0dde956fb26fa856394332e7091310b854933887da26717c`。它保存全部 49 个状态、最终原数值审计和失败状态，不是已接受前缀，也不声称恢复原始 raw cubic 逐位表示。

## 2. 完整有限前缀/接缝审计

与前一条 `a=.21` 运行的后续审计异常不同，本次完整数值审计确实返回并写入 checkpoint：

| 项目 | 数值 |
|---|---:|
| prefix metric FFT l1 | 0.02365060682715134 |
| flow defect | 0.16165252292080387 |
| Cartesian Darboux FFT l1 | 692.7768979576163 |
| finite root margin | 0.0023874201547310347 |
| physical boundary residual max | 9.178156919089987e−7 |
| 径向 / 角向审计点数 | 6406 / 1024 |
| cut metric FFT l1 | 0.0017519831731487882 |
| cut metric C1 FFT l1 | 0.05062256445445718 |
| mean first mismatch | −0.0003194090490491741 |
| mean second mismatch | 0.007484585416743128 |
| nonmean second mismatch | 0.00018019788467541625 |

完整 metric 远高于原 `1e−6` 门，且 inner 本身失败；因此不能把尾部成功或较小半宽初猜的较低 RMS 当作新圆弧解。

最终核心通过的是原定义配套的**数值**正性充分 guard：rho 下界 `0.42855111058414996`，同次核心采样 rho 范围约 `[.44838347,1.51657219]`，只用每扇区 512 点；它不是严格全曲面证书。完整 15 个失败态控制系数已按原尺度记录，但不拿它们冒充 accepted continuation 锚点。

## 3. 四次实际尾请求均独立保留

| 调用 | 实际 residual | Jacobian / audit |
|---|---:|---|
| 1，原初始 H | 1.3784657706205187e−9 | 无 Jacobian；返回完整有限 audit |
| 2，逐位相同初始 H | 1.3784657706205187e−9 | 800 项有限 Jacobian |
| 3，失败前缀后的新 H | 1.1906778568368796e−9 | 原实际尾，无 Jacobian/audit 请求 |
| 4，接缝审计的 H | 1.6406173126730715e−9 | 800 项有限 Jacobian，并返回完整有限 audit |

四次都由原 worker 返回 `converged=true` 且 residual 严格小于 `2e−9`；最终尾的 `minA=.7401165444106715`、`minD=.9993892232793832`。这些尾结论不代替前缀门。

调用 3、4 的实际高度向量有 9 个分量的末位差异，最大绝对差 `1.3234889800848443e−23`，所以记录分别绑定它们的完整 H 哈希，没有称二者逐位相同。collector 初版误把这两个 H 假设为相同，因而只读断言拒绝；核对原保存请求后改成显式记录差异，再执行成功。这个记录修正未重跑或修改任何 solver、源输入或数学状态。

## 4. 复现入口与界限

原入口、完整命令和全部输入来源已在 `circle_halfwidth_a001_entry_record.json` 绑定。本条 collector `collect_small_halfwidth_terminal.py` 只读已经完成的文件，核来源 SHA、完整物理系数块、原残差停止门、实际 Jacobian/audit 和 H 身份；输出为 `circle_halfwidth_a001_terminal_record.json`。完整数据仍只在 scratch，不提交可再生数组。

小半宽 `.01` 没有继承最终 `.21` 的持握窗口或比例；本结果也没有为固定 g 或升到下一半宽提供 accepted 锚点。它具体排除了这次预声明的新初猜/有限设置直接给出合格圆弧解的判断。接下来的两圆弧迹方向属于另一个明示的新有限控制空间，不与本次失败状态或原 raw span 混同。
