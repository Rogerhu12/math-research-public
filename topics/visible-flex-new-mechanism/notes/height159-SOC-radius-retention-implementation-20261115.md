# 成功 SOC 条件持径：实现与首次公开入口

日期：2026-11-15。状态：新增源码与设计已完成静态审读；新增人工开发及科学阶段尚未执行。本文件不把静态审读称为开发通过。

数学与控制选择见 [成功 SOC 条件持径设计](successful-SOC-radius-retention-design-20261115.md)。本轮只有一个算法变化：在严格限定的完整 SOC 接纳后，可用原接纳中心的真实总步模型质量和实际物理校正范数，把旧控制的减半替换成维持该模型半径。不是直接增长，不增加变量，不改变任何真实几何验收或原 LP。

## 1. 两个新增文件与冻结依赖

新增库 `scripts/frame_metric_height159_soc_hold.py` 包含配置、实际总步诊断、条件控制与旧循环的最小消费版本。新增 driver `scripts/frame_metric_height159_soc_hold_audit.py` 包含第六前缀的严格交接、单新阶段、完整初末评价、原生科学输出及仅新接口的人工开发源码。

原六段恢复链依次为 growth、strip reserve、可逆 SOC 缩放、103、154、159。旧源、旧参数和旧 24 个输入字节流及 SHA 保留；每段在同一个公开任务的临时目录只运行一次以恢复必要输入。新阶段不把原 159 第一次运行的 b429 hash 当强制条件，不重试到旧 hash。前缀若因墙时得到不同合格末态，报告其实际 canonical、控制状态、全部池和与历史的差别；本轮新下降只从这次交接态计算。

旧 159 源锚于 `ef8c1cdb6f83fd96e24215c63d246adb0cbc0121` 的六文件版本。driver 先调用旧 frozen-prefix 源检查，再核原六份 159 源的精确 SHA。新增两个源进入本轮 source map；旧源不改。

## 2. 同一坐标 reference 的交接

`handoff_restored_height159` 接收仍在内存的旧 `FiveHeightField`、`FiveNullHeightGate` 和刚完成的临时 159 报告。它复用同一个 field 和 gate，保留原准确高度 reference 与 H，直接消费原 159 独立坐标。不会把九个依赖有理高度转成九个 binary64 再重建 reference。

交接逐项绑定来源、参数、原输入、初态、159/163 身份、完整 g、不可变 b0、永久 reference、准确 H、全部九高度盒、准确零总积分及固定 c4/c5。它核最后接纳点与最后独立 384/768 门，保全部粗细整数行 ID、分组、原采样坐标、池 hash 与已有行的包含关系。

控制交接从旧 159 的真实继承半径和 streak 出发，只用冻结旧控制函数回放已有 scalar feedback。只有已完成的更新计入；最后模型若未完成，不把它当成功 streak。输入半径低于原最小值时，新阶段按原规则在新 LP 前退出，没有隐含重置。

## 3. 原 base 模型与实际物理范数

原 primary 的 active v、J、soft 标记、完整行映射和外域 rho 上界不变。记录的模型签名已绑定原值/J；新绑定同时记原坐标 bytes hash、物理 SHA、准确坐标定义、M、原物理宽度、原行顺序和两池版本。

仅当原规则接纳完整 SOC 后，从实际存储的 x、y、z 计算 s=z−x 和 c=z−y。新预测使用 v+Js，不使用 y 的实际残差作为原中心值。分母非有限或不超过原 improvement floor 时，新比值不可用；非有限线性预测返回明确不可用诊断，避免把 Inf 写入 JSON。

范数通过原 `subspace.step_norms` 计算，采用真实 M 和原 163 物理盒宽度：body、tail、height 三块分别以 1、8、1/4 合成共同 body 范数。报告还保物理 L1 和无穷范数。SOC 原目标系数为 1；primary 才含物理无穷范数系数 .001。新 guard 不从 SOC objective 推断 block norm。

库要求实际原 base 总步比值至少 1/2、校正共同 body 范数不超过模型半径的 1/10、总步不超过 11/10。完整 primary/SOC、全部新增行包括 soft 均为零、原单位 LP residual、原两网门、真实下降、关联身份和逐项旧缩步理由同时满足才可持径。旧 y 线性 SOC 比值只按其原标签保存。

## 4. 旧控制、接受与预算不变的范围

新库先调用旧 `next_mapped_trust`，保其完整返回记录。普通 primary-only 路径准确返回旧半径/streak；新增条件不通过时也准确返回旧结果。只在规定的完整 SOC 情形覆盖为原模型半径并把 streak 清零。

旧循环中的真实值调用、全网条件、接纳次序、新行返回、LP 方程、SOC 实际 y 残差、抛物回退和预算逻辑保持。新增记录发生于已经接纳的完整 SOC 后，不新增 geometry/Jacobian/LP/value 调用。其数组运算与记录费用仍计入同一活动墙时。

共享预算仍为 12 次 LP、40 次完整粗细值、120 秒活动时间；单 LP 上限和原最小/最大半径不变。块半径仍为 T=B/8、H=4B。原真实门仍包括两网旧度量预算 167/625、硬曲率 58、正则、球、内条带、signed-z、镜像、帽高和准确物理盒，新目标仍为 13/50。

不声称 selected-J 成本减少；完整原 163 列几何 Jacobian 仍先计算再映射 159 列。没有同时改变所用取样、连续误差假设或物理模型。

## 5. 输出与可消费性

本轮接线 lane 为 `metric_height159_soc_hold`，报告顶层唯一新 stage 为 `metric_height159_soc_hold_stage`。临时主文件名为 `metric-height159-soc-hold-audit.json`，语义摘要为同 stem 加 `-summary.json`，开发结果为 `metric-height159-soc-hold-development.json`。

新 driver 保原 98 个实际 CLI 项，仅 `--out` 改为新输出名。公开任务先以同一 driver 的 `--check-only` 执行新增开发，成功后执行唯一实际链。由根代理维护 [实际 request](../computations/request-continuation.json)、workflow 和 metadata-only publisher；本文件不预告首次执行通过。

每个前缀分别打印初末完整门、原始 source/config/raw SHA、实际 canonical、控制状态和费用。新阶段原生 stdout 保旧所有 model/trial/SOC/dual/floor/defect/accepted/初末门，并逐模型追加：

- 原 primary 与 y 线性 SOC 的旧 ratio 和逐项缩步原因；
- 原 base 实际总步的 rho、分母、真实下降、ratio 与不可用原因；
- 实际校正/总步的三物理块、物理无穷范数和 L1；
- 模型/行池/坐标/M/宽度关联，全部新增行与遗漏硬行；
- 新 guard 每一布尔量、全部失败条件、旧与新半径/streak、持径或回落理由。

未完成模型明确无完成的控制更新，不能据部分记录推断持径。打印只消费已计算记录，不重评几何。日志总规模受原 12 LP / 40 values 限制。原完整 machine payload 和摘要仅临时，按根 README15 不提交或保存；发布仅来源、参数、run 和输出 SHA，以及另写的人类科学结论。

## 6. 新增开发源码范围

库新增纯数组开发覆盖：可持径成功、y 比值接近 1 但原 base 比值不足、零/负/非有限分母、尾块 8 倍权重、依赖九高度放大、新增 soft 行、遗漏硬行、缺 fine、其它缩步原因、原单位 residual/solver 失败、未接纳点、原模型/数组不变、普通 primary 控制结果不变。

driver 新增人工 IO 使用明确的新小数组族，不加载实际研究向量；六个旧科学入口在测试中 stub，只覆盖新调用顺序和清理。开发核同一个 reference/H 与非零五高度独立末态的交接、错误 source/状态/有理高度/池/控制/门拒绝、唯一顶层 stage、失败小 JSON、checkpoint 保留、原生新 guard 输出和 summary binding，以及完整 evaluation-only 新主链。旧人工套件不调用。所有新布尔输出均显式转为 native bool。

本地只进行了源码读写与静态语法解析；上述开发函数尚未执行，首次真实结果以公开 Actions 为准。

## 7. 后继判据

新阶段仍从本次恢复初态独立记真实两网最大度量下降，保 1e−4 的非接纳参考。持径次数、未来实际余差和原门失败将回答该控制改变是否有作用。若仍只有很小下降，不能据此延长旧预算或宣告连续等距/reach；后继应依据实际域峰、物理块使用和曲率余差重新选择问题。
