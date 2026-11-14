# 真 M14/W14 候选的实际闭图入口

2026-11-09，`/root`。**状态：条件执行协议；未产生新 CP、几何导出或全域证书。**
本稿尚待全文独立审查。它将已审的通用几何链明确接到当前 M14/W14 入口，不改旧 M15 协议，
不将已闭首 DN、活动 BVP 或资源失败改称成功。

## 1. 候选身份必须先真正关闭

原 `db6f-prefix-spectral-true-m14.py` 的一次运行，只有 root 真实观察到工具
退出，并由 `db6f-prefix-audit-spectral-true-m14.py --mode final`
连同 `--observed-execution` 正常通过后，才能进入本协议的正入口。
要绑定实际 CP、它的全部物理 PPoly 分片、原 outer 边界检查、它自己的最后
Jac/audit 响应、原数学来源、运行期 Newton 与14个物理回调。
捕获异常的程序返回、首 DN 或旧 true seed 都不能代替。

原 v1 的正常门仍严格要求原 Newton。拟议的释放旧 LU 版本若以后完成，
必须使用它另经全文独审的新 selector/preparer/auditor、实际运行身份和真实
root 退出观察；不能把新函数注入后伪报本稿的旧 v1 来源。

当前 M14 的尾角求积已经是512。无需先另造一档256求解来支付既有 G5。
M14 是 Fourier 未知模数，W14 是常正对角配点坐标权重；权重不会增加模数。
它仍须给真实新图到原 $2\cdot10^{-9}$ 的完整误差下降账本，保留旧 M14
非单调和失败记录。可选的原生径向加密不是自动新增验收门。

## 2. 源诊断与真正输入文件

关闭后先检查本次 CP 的原物理残差、真实 BC、实际保存 PPoly 的 metric
诊断及本次最后尾响应的原 audit。它们只能作为定位和决定计算顺序的诊断，
不能替代全域连续误差证明；浮点样本越门也不单独宣称精确方程不存在。
如果明显的源误差平台尚在，优先继续求解/离散误差研究，不指望区间包装改变图。

`db6f-prefix-endpoint-critical-increment-export.mjs` 的第一个位置参数应当是
**CP 的 `tail_seam.tail_record` 指向的最后真实尾响应文件**。
该导出器取 `rec.response`，再取其 `checkpoint`，要求实际 `parameters` 与
`states`；完整 prefix CP 自身不是这个 staged-tail checkpoint。
因此完整 prefix CP 和最后尾响应两者都必须在入口清单绑定，不能只拿一个
单独成功的尾包启动最终闭图链。

本稿不填入尚不存在的 CP/最后尾文件名，也不创建占位成功包。

## 3. 已有动态 M 导出器的 M14 设置

已审 endpoint exporter 从实际尾 checkpoint 读取 M，以 `K=2*M` 解释状态，
以保存的 rawNode 和 P 匹配 stage 布局。对 M14/P8，不需要改几何公式。
同一初档取：

| 字段 | 值 | 性质 |
|---|---:|---|
| export depth | 8 | 同一无限物理背景的数值表示截断 |
| steps | 32 | 每 stage 普通表示节点的基本档 |
| flow-steps | 32 | 显式固定导出时的积分上限参数 |
| angular-nodes | 512 | 导出 engine 与 Fourier 提取共同使用 |
| degree | 192 | 平面 signed 模截断 |
| grid / critical-cells | critical / 0 | 保留原内部 cusp 节点规则 |
| critical-base-steps | 64 | raw0 的基本表示网格 |
| critical-ratio | .05 | 已审内部 critical 节点提案 |
| endpoint-ratio | .025 | raw0/segment7/rawLeft0 的恢复起点提案 |
| difference-step | .00005 | 原源二阶有限差分诊断设置 |
| audit-angular-nodes | 128 | 明确记录的导出样本诊断 |
| audit-fractions | .25,.5,.75 | 样本诊断位置 |

height 模为 $0,3,\ldots,42$，平面模为 $|m|\le192$ 且
$m\equiv1\pmod3$。所以系数数为 $128+15=143$，每行 stride 为
$3+4\cdot143=575$。1000行原始 f64 为4,600,000字节，低于5MB；
仍须在实际运行后核每件文件，超过1MB的数据压缩，不把数组读入对话。
已有 P8 节点提案的21,031节点只是同布局的规划检查，不能声称未来新导出已生成。

以上是明确的初档。表示节点还会改变局部重新积分路径，不能叫严格的纯插值
比较；原生 shooting 的32步没有因为导出局部细分就变成64步真联解。
若实际导出需要进一步加密，要另存新图并重做对应证书。

## 4. 本张图的连续验证与公共接缝

导出后先核 finished、输入/源 hash、全部分片尺寸/有限性/共享行、完整C3模式、
正精确半径增量、归一恒等式及本次 collar。不可换成另一次源提取的端迹包。

`db6f-tail-transfer-background-v3.py` 只转移同一冻结背景的 $w,w_r$ 值包。
它按数值字段白名单比较物理参数；M 是允许比较的数值字段，没有 M15 专属门。
六个背景定义 hash 保持原值，新有限图由新的 manifest hash 单独绑定。
配套使用已审 `db6f-audit-closed-budget-transfer-v3.py`，不得伪留旧转包身份。

随后用本张图的新背景包实际计算完整尾的 metric 和曲率，包括 collar；
旧 M12 的 metric、曲率或 support 数值不随背景转包自动转移。
先作实际第一界及原正常连续后台，再依据未解盒选择必要的局部精化。

prefix 的 exact bridge、目标 metric 转移、保存几何和公共 cut 都必须来自
本次真实 CP。`db6f-root-common-cut-v2.py` 会从实际尾的完整 signed 模
自动提高柱模，故 degree192 不能接一份遗漏相应模的旧公共接缝图。
重新计算新公共图的 geometry、metric、moment 和 closed budget。

`db6f-root-whole-metric-reach-v2.py` 合并同一实际图的所有界，其普通阈值
仍是 README 的 $10^{-6}$，并明确保留 G5=false。
所以还必须运行已审 `db6f-audit-terminal-error-gate.py` 的正常入口，按精确
$1/500000000=2\cdot10^{-9}$ 比较新完整实际上界与真实旧误差下界。
不能把 whole 程序退出0当成 G5 已付。

## 5. 全时族、最终复算与仍然开放的缺口

全时结论继续只由同一已审材料相位/空间旋转作用、完整C3系数和公共两 jet
给出，固定帽必须逐点不动；几个 t 的网格不能替代全时证明。
最终网格来自这张新冻结闭图，重做闭流形/PL嵌入/固定帽核对并保持单件小于5MB。

未参与优化者须从原真 seed 和已封存的实际求解入口重跑，随后独立完成导出、
背景转包、连续证书、闭图预算和网格。不能从最终成功 CP 作零步复用冒充原求解复算。
若使用新 Newton 身份，独立复算也必须重放该已审版本的实际计算。

上述链条全部完成后，才可对照 README 作最终判断。数值近似与严格无限非线性
尾存在性之间的缺口仍须如实说明；当前此稿只提供具体入口，没有完成 G5。
