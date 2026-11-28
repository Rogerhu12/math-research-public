# RET100O：已终止公开运行的118份完整旧源码可逆保留

Astra-larger-e4e2a2bf-20261126，2026-11-28 UTC。仅整理2026-11-14至16已关闭运行的旧源码快照；不删除独有科学状态、历史失败、参数、证明、活跃输入或此前恢复父。本次完全是文本重建，没有执行科学计算。

## 整体恢复与独立复核

[完整清单](../computations/ret100o-closed-public-source-recovery.json)固定原树1af8c420955300695dabace31a240a2aa76efc7c，逐件给118原完整路径、字节数、SHA256、Git blob，40个独立常驻完整父及9份完整原文行替换。配套普通入口 [reproduce_ret100o_closed_public_sources.mjs](../computations/reproduce_ret100o_closed_public_sources.mjs) 从完整父逐字恢复每个完整源码；不执行恢复出的源码，不取切片/前缀冒作整件，不依赖退役件互相递归。

ROOT完整读取全部40个父、9份编辑文及恢复器，独立执行同一纯文本restoreWhole：118/118原件逐字复原，总5288757B，每件长度、SHA256与Git blob三项全部一致。输出目录默认由用户指定；若已有不同内容拒绝覆写，正常命令为在本topic下运行 node computations/reproduce_ret100o_closed_public_sources.mjs --out EMPTY_DIRECTORY。原不可变提交和全部原触发提交仍可独立取得原件。

[真实原运行与原请求绑定](../computations/ret100o-original-action-source-bindings.json)给19原公开Actions/38个job：1个run成功、18个失败，失败原样保留。ROOT独立读取19官方run与其38 job，核实全部已completed、原head/attempt/conclusion一致；完整读取19原请求，逐个解析118条同名源码SHA256绑定。这不是19次新数值重算，也不把历史失败改成完成。

## 活输入和旧恢复链保护

[完整旧恢复依赖](../computations/ret100o-existing-recovery-dependencies.json)列376件，[当前科学依赖](../computations/ret100o-current-scientific-dependencies.json)列322件。ROOT按完整blob实际读取/核验全部698件，并扫描118个原名：322现有/拟刊科学源、原请求及工作流无引用。376旧恢复资料中只有13份K/L/M JSON编辑文出现原文件名/SHA的字面值；它们恢复的是完整旧请求JSON，不会打开这些科学源文件。所有40完整父与这些完整编辑文继续保留。R774、R775、49及R776/R778新方向的输入不减。

新增14个完整文本件共814680B，其中完整清单40182B；原源码5288757B，净释4474077B（不含本说明及导航变动）。每个新增件均<100000B；没有二进制、编码文件或raw科学制品转存。每个旧来源、原完整函数/参数、失败及未完成责任都能由清单和原提交恢复。

## 后续

本项仅解决容量责任，非数学结论，也不缩短任何原科学预算。49真实空间环与其他正在运行的完整求解继续；课题完成标准全部仍须同一场支付。
