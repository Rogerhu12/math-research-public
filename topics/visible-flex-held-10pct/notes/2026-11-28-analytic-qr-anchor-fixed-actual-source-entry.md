# 真 QR / full-DN 锚之后的独立原 support 固定 g 入口

2026-11-28；源码准备，尚无真 λ=1 输入，未调用 BVP 或 native。原五个 `chord_fixed_support_actual_*` 数值源和原四个 `fixed_actual_*` reader 已从公共提交恢复，并逐项核对原 SHA 不变。本组不改这些文件，也不把 QR 执行重贴为旧 7a/streamed 执行。

## 首锚与数据身份

新模型 KIND 为 `original_r53_literal_fixed_metric_qr_anchor_actual_dn_v1`。首输入必须在明确的 `--origin-repo` 中通过 `tail/qr_actual_coupled_prefix.py` 的真实 `accepted_coupled`：λ=1、原 support、完整 prefix CSR/QR 执行侧录、native4、chord3、原 8outer、原全部有限门和最终 physical-H 包都由该 provider 核验。返回 provenance 的 `source_kind` 必须准确为 `actual_lambda_one_qr_chord_final_physical_height`。

原设计 run、完整 raw、实际 physical 文件、耦合 summary、完整 final physical-H binding/packet 均保持原身份。新 `fixed_problem` 保存明确 QR 源种类及完整已核 provider provenance；每次后继固定 g 精化继续核同一 problem 和完整祖先链。不能把仅 linear-DN、λ<1、仿射边界、未审计尾包或旧低 λ 数值记录当作这个首锚。

数值首次转换仍沿原已审模型：冻结锚的真实物理 δ、完整 profile、字面径向 chart、角图、gauge q、warp reference、完整尾背景和 finite mean 节点数。构造器使用原 `fixed=True` 支持曲线族，参数零明确变为 `log(q_actual/q_seed)`；原全部高支持控制与 exact core lift 保留。物理 q_aux 可变，gauge q 和目标 g 不变。

## 求解和精化合同

新五源与旧五源的数学部分相同，差别仅为新 provider/KIND/来源字段、对应模块路径和资源所有者记录的 entry SHA。第一次先做同 M 的严格径向精化；后继可用原完整升模与 literal mesh 保留入口。`tol` 必须比前一真实接受值更严格，BC/physical BC 不能放宽，原完整 native 的 solveTolerance=`2e-9`、完整 shooting state、全部 height Jacobian、audit 和最多八次原 outer 保留。

原资源路径仍是完整 CSR、完整 QR、factor-only mmap、全部原 RHS64/Jac32、异常安全批处理、真实完整 nodal 检查点和原门。映射逻辑大小不冒充 RSS 信用；实际 page release 失败会停止。新 launcher 要求显式选 `--own-child-session` 或 `--inherit-owned-session`，只在确认本子进程终态后清理它唯一的临时 mapped 目录。它不删除接受场或原检查点。

raw H 与最终物理 quintic 端点 H 分别绑定；只有字节相等才复用同一完整实际包，否则原数值入口重新支付完整 H/J/audit。新接收器完整核参数语义、原网格/频率/mean、全部状态、原误差门和最后 physical-H 身份。

本组没有把 R85 的旧点 J/V/q 列或 R92 的旧弦算子搬到一个尚未出现的 λ=1 场。以后如选择完整弦加速，必须用真正 λ=1 来源重新绑定完整计算坐标、M、mesh、pscale、响应列与原回代；R92 只支持保全部未知/方程的显式网格延伸。当前数值入口保留原完整求解器作为真实可执行路径。

## 表示和连续证书入口

四个新 reader 只接受上述新 KIND 的真正数值返回，使用当前已核 physical 文件的完整终端 H。它们保留原 Cartesian 公式、共同 mean、完整尾谱、cut 两 jet、held-frame、完整网格拓扑及 5 MB 网格限制，报告传播新的 QR 首锚/固定 g/最终 physical-H/实际源 SHA。

新 mesh 入口没有沿用旧 $9/20$ 相位终点或旧 $k=.2,S=.5$ 的 frame 专用门。它要求显式 `--phase-end`，并接受精确有理 `--held-width`；R87 的调用为 `--phase-end 4/5 --held-width 27/50`。入口直接复用已登记的 `material_circle_phase_contract.py`，在真实新 source 通过自身 gate 后核实际 $k,S,b$、`homotopy=curvature_blend=1` 及整个 grip sweep 严格落于真实圆弧窗。刚体 frame 仍是原 $R_{-(1-k)\alpha}G_\alpha+O-R_{k\alpha}O$，只取消了不适用于 R87 的旧参数专用门；没有改变全模位置公式、拓扑、PLY 限制或 source/full-H 接收条件。报告保存 exact phase、held width、实际 binary 参数和 phase-contract 源 SHA；这里只准备接口，不凭此宣称存在真正的 $\lambda=1$ 场。

每个新场仍须实际生成自己的完整尾、连续几何/metric/cut 与加密证据；没有继承旧 λ=.002 raw-H 的 R73–R90 数值界。旧 loader、原 `accepted_original` 及旧已执行 source labels 都未更改。

## 文件与当前验证

数值入口为 `qr_fixed_support_actual_model.py`、`qr_fixed_support_actual_resources.py`、`qr_fixed_support_actual_step.py`、`qr_fixed_support_actual_acceptance.py`、`run_qr_fixed_support_actual_once.py`。表示入口为 `qr_fixed_actual_cartesian_prefix.py`、`qr_fixed_actual_prefix_continuous.py`、`qr_fixed_actual_closed_map.py`、`qr_fixed_actual_export_closed_mesh.py`，均在 `scripts/resume_20261128/analytic/`。

九源真实 `py_compile` 成功；step、launcher、continuous、closed-map、mesh 五个 CLI 的 `--help` 实际 exit 0。没有构造假 λ=1、没有正向数据验收、没有运行新 J/BVP/native/几何证书。完整旧/新 source SHA 和实际工具终态见同名 JSON。真正首锚到来后，调用方从其已核 summary 取 actual run、原 port/baseline/native manifest/final packet，设置独立新运行目录和以该 final packet 为初猜的 runtime config，再交给新 launcher；不能按旧 M24 或 mean1168 假设补输入。

其中 mesh 的旧准备版在发布前由 root 发现上述相位专用门风险，现只修改这一个新源，旧九源和其余八个新源保持原字节。修订版 `py_compile` 真返回 exit 0（工具片段 `d7caff`），新版 `--help` 真返回 exit 0（`7896b6`），明确列出必选 `--phase-end`。未添加假正向输入或重复数学测试。
