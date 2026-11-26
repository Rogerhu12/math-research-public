# R582 radius-only 正式有限非圆运行：原始终态收据

日期：2026-11-26；会话：Astra-new-mechanism-0105020f-20261126。
本记只解析已自然结束的原 stdout，没有本地重建几何、运行求解或重算旧种子。

## 1. 原身份与自然终态

- run `45827253372`，job `139934478969`，attempt 1，lane `actual-resonant-radius-only`；
  [原 run](https://github.com/Rogerhu12/math-research-public/actions/runs/45827253372)。
- source `d4a5b41506139a2bd7ad6d53a473e1766f536377`；新 wrapper SHA256
  `445e3ac5098cbaaa08f080e1be5d8172e576f72a00b825b2cb000adad83725d2`。
- request `request-r582-finite-radius-only-20261126.json`，106167 bytes，SHA256
  `d2dfbc420b74f7b5de9b84d7ea84b802ffeb0e9b5cafaa6857d7f370a8aad708`。
- stdin 参数 98910 bytes，SHA256
  `187a463fdd777d2884310ac0793ed96583d5216d47407795b53daae633c46ac4`。
- 原 job log 12912168 bytes，SHA256
  `0f8c0ea00bf770412d0b532dc8d28dd1d7ff0c8c2c51a874e11023e9a2432feb`。
  此 hash 含下载文件开头 UTF-8 BOM；下列 JSON hash 只涵盖 tag 后 JSON 的原 UTF-8 字节。
  原日志只留 scratch，不入 Git、不上传 raw blob。
- `FINITE_RESONANT_FIELD`：115583 bytes，SHA256
  `6dad4e428e5988907880351acae932a82fafae903d39d3d7d380e873368dc889`。
- 首 `FINITE_RESONANT_START`：199882 bytes，SHA256
  `afbe697a0e558a5dc5d68b0f0a0a8f12f8924574c602e5b116e280b878666a86`。
- `FINITE_RESONANT_FINAL`：447283 bytes，SHA256
  `397a1a6fb7999c36f4849956ef6b820ba615118ce9733ebf0e6356a6ecbfb169`。
- 自然终止 `fixed_p_backend_stalled_without_qualified_progress`，stage 0、outer 14、
  phase `geometry_restoration`；进程 returncode 0 / Actions success 不是科学过门。
  科学计时 **214.6783520880001 s**；入口子进程墙钟
  `13:15:14.062393–13:18:49.444892 UTC`，**215.382499 s**，与科学计时分列。

## 2. 固定的新有限非圆范围

本次沿用已付真实共振圆背景、M169/factor8 尾口、固定
`mu=-0.040019082162222074`、`nu=-0.048942275258064924`、核心归一
`7.136787019826327`。核心始终 **p=0.181, q=0.18, rounding=0.2**，
epsilon 的实际 binary64 值 `0.0010000000000000009`；没有缩回圆点或推进到下一 p。
当前 stage eta 门 `2.5000000000000047e-7`，原目标 p=0.8 未达到。

几何预算仍 R=1.012、Y=0.3928、tau=0.06072、mean-E floor=0.25、
det floor=0.1、working margin=0.001、feasibility tolerance=1e-8。
81 个物理变量，原 beta/B-spline 8 径向基、4 角模；改变 q/p 时均值度量仍会改变，
没有固定 g 加密结论。

wrapper 只将 seed 商法所需 a 的三 jets 改为相同公式和运算顺序的直接半径求值，
去掉上次失败的不必要 H 积分；原物理位置、空间导数、参数 AD、接受门及全部旧 4811
细读位置不删。新 dense/Hermite 重建实付，重建 mesh hash 与首失败运行完全相等：
`0d222bd12ce8a61d0c88264c6fb5c82066f0ca058855b5bf7a670a53b483a991`。
这不构成其准确性证书。

## 3. 真正观察到的失败与实际保留 q

首完整细网为 **10821 径向 × 192 角**。原首 q hash
`233e8fdb8760c8104af902361db9a77f90d986250ff383da886130bec0e652c2`；
eta=`0.9960025919156961`、曲率峰=`8413.028681444834`、
无 margin 几何违反量=`509.83910153733035`。因此巨大尾部峰在首完整扫描已出现，
不是最后新增网格或 optimizer 后才出现。

首 coarse 108×96 只有 geometry cover `38.746976248535724`、metric cover
`0.003834826144980985`。首 callback 保留过一次
`working_geometry_restoration_only`，其完整细读 V 只下降约 `7.7e-12`；
它未过任何完整几何门。实际 q 最大坐标变化 `1.4252295798961034e-5`，
不能称 q 逐项未变，也不能称实质几何改善。

随后实际约束升级为 **124×192**，完整细读为 **10835×384**。
末态保留的 81q hash 为
`d4afde612de65692d4f0184948565ca13b39a4bc04d85429a9103fae7e41f2b0`；
`qualified_on_this_fine_grid=false`，终态标签为
`retained_input_requalified_on_actual_new_fine_grid`，是重新观察后的失败保留态。

| 终态实际保留 q 的完整细网量 | 值 |
| --- | ---: |
| eta | 0.9960025919156725 |
| eta attainer s, theta | 0.8691932771929971, pi/2 |
| 最大绝对主曲率 | 8413.02868144471 |
| 曲率 attainer s, theta | 0.8716776757406842, pi/2 |
| 无 margin 几何违反量 | 509.8391015373228 |
| working 几何违反量 | 509.84010153732277 |
| ball radius | 0.7542664394980477 |
| 最大 abs(y) | 0.38897753056901385 |
| mean E 最小 / 最大 | 0.4908197573397897 / 162.4420311093704 |
| det 最小 | 0.4306939312338985 |
| area 最小 | 0.16464270208465276 |
| z 最小 | 0.02 |

唯有 curvature 两组违反；其余所列有限网格几何行通过。所有量仍为有限网格观察。
124 个实际约束径向 binary64 SHA256
`ba94cc842802e847e2d65a73a0a2eda0d29fe50a81ae77dfca99a4ddf512f059`；
10835 个细读径向 SHA256
`5205d5a834717e06250bcbb1f98bec1139130ed42c20ed7e77d274ccf6346f52`。
末态 pending 径向为空、pending 角升级 false；proposal 节点同实际节点，
不能把 proposal 一般标签作为另一次已优化网格。

outer 1–14 各自然返回两次函数/两次 Jacobian，未再接受 q；trust 从 0.01 逐次减半。
最终实际 backend trust=`1.220703125e-6`，下一 proposal=`1e-6`，二者分开。
末 natural OptimizeResult 为 status 0 / success true / nit=nfev=njev=2，
extra=`509.84010153732254`；它仅成功停在松弛的几何恢复问题。
末 trial q hash
`23dc41c1d4a0e6be821ad4570c6a1585fe572c766b0733063b228a45d3717a5f`
明确 `not_accepted`，不替代实际保留 q。

## 4. 全部实际新成本与算子核

- 15 个已闭 outer，14 次自然 backend 返回，43 次已完成 callback 扫描；
  58 次完整 fine 扫描、2494 个完整径向块、628402 个细读径向点。
- 29 个完整参数 Jacobian、174 个方向块、32 次 backend value evaluations；
  Jacobian 日志逐次实际秒数之和 **39.55630442399956 s**。
  初行数 19008，末行数 42656，block size 16。不能累加日志中的每 outer 累积字段冒独立成本。
- 本次唯一必要方向核 step=2e-6：全部 19008 行相对 L2 差
  `4.105144714340377e-8`、最大绝对差 `0.00024200583786881946`；
  核后同一正式 run 自动继续。分块值重建最大差始终 0；这不是严格导数误差界。
- 新 dense 外传 160 段、**960944 RHS**；新 core forward 1 次 /2510 RHS，
  新短 backward 1 次 /206 RHS。原 inner DtN、原三 seed 比较、旧 24/48/96 拟合均 0 次重跑。
- raw material 候选 63045，实际 Hermite 端点 62878；dense radial 查询 62443；
  material queries 164355；新增 radius-only reference queries 164355。
- material endpoint 观察 2956 个加邻接中点等组成5911个有限观察点；
  未选端点最大所见 jet `7.838393053637985e-13` 不是区间误差上界。
- height queries 3166、cache hits 375、QUADPACK RHS 235893；
  actual weight calls 1023386；30 次模型网构造尝试、164355 个径向准备点，
  174 次 AD block /2540 次 value geometry 调用尝试、44 次 geometry cache hit。
- dense scale 下非零 jet 变成浮点零 274689 个分量。`uncomputed_inner_tail_query_points=0`
  只说明本轮取样分支计数，不消除实际数值 seed 的零后缀。

首失败已付 **70.62187625499996 s** 仍列在 prior ledger，未抵扣、未并入本次时间；
原 true-s/paid-mouth/三 seed 成本也保留。没有 raw/端点大数组入库。

## 5. 失败所限定的范围与未付事项

尾部 s≈0.869–0.872 的二阶几何失败是真实这次数值材料曲面的观察。
此前只在 mouth/core 观察的归一场幅、C2 值不是整个 tail 的上界。
原日志保存 mesh hash 而不保存全部 62878 端点六 jets，所以不能从原日志断言
巨大曲率来自真实 ODE 场、Hermite 插值、短段浮点相消或它们的组合。
特别是原 endpoint 基按独立 O(value) 项求和再除 width^2 的实现，没有连续 C2 稳定性保证；
1e-13 的材料结点合并阈值不能充当这种保证。

进一步只解析原5911个材料观察位置：它们由2956个选定端点和全部邻接中点组成。eta峰 s=0.8691932771929971 位于该列表 index2074（从0计），是选定端点本身；原 searchright 对此取 t=0，value/first/second 直接恢复该端的共享 jets。因此严重一阶 metric/mean-E 失利不能仅用区间内两个 O(value) 二导项相消解释。曲率峰位于已选端点 0.8716724063923024 与 0.8716820788524953 之间，仍欠原dense/同多项式稳定求值的局部六jet对照。后续须同时核实际seed一阶量和新的尾部校正能力。

数值 seed 有零 suffix，从 s=`0.8936970895024391` /u=`1006.8799923538346`
开始未表示无限内尾；它与准确 R582 无限 flat 核不是同一个已认证 C2 函数。
DtN/ODE/Hermite/高度求积及 FFT primitive 的误差仍未严格包住。
本轮没有有限等距族、宏观非圆、固定 g 收敛、连续全点几何或完整 all-pair reach 结论，
README completion=false。此失败范围闭账，不重跑已付15个 outer/43个 callback。

## 6. 运行中真实 pull 与规则身份

public 实际 pull `13:15:03.669545–13:15:03.986130 UTC`，
before=after=`d4a5b41506139a2bd7ad6d53a473e1766f536377`；
根/课题 README diff 均空，blob 分别
`282e86b03385d3b6245ce7100ae2e2af7b103c2d`、
`d0432faff569c8e9af7ed4809847e12880976c11`。
private 实际 pull `13:15:06.949694–13:15:07.693536 UTC`，
before=after=`a425ec63d36b3d204d35a07c24ae76f6394fcc24`；
根 blob `5ba164843b1f5802184178a82d786264404873a3` 未变，QUEUE 唯一且仍本会话进行中。
该子进程约215秒自然结束，不触及一小时检查间隔。
