# 末模型最后 LP 名额：原时限类型修正与已付检查复用

日期：2026-11-16。状态：首轮公开日志已经消费；本文所述修复源码只作静态编辑，尚未运行。本文补充 [最后名额设计](terminal-paid-attainer-final-slot-design-20261116.md)，不改变该设计的数学模型、实际验收门或资源上限。

## 1. 首轮实际到达的边界

[run43786841449](https://github.com/Rogerhu12/math-research-public/actions/runs/43786841449) / job133036290253，source `60ff5c1171c3c94ac84f7fcb88427c530daf69e8`，先完成三个新开发组，检查数分别为4、3、4，11项全部通过。实际只有3次人工 stub 回调；真实LP、普通几何、完整方向JVP、旧开发套件和科学优化调用均为0。

随后原输入读取在 `frame_metric_terminal_paid_slot.py::_ledger_guard` 拒绝配置项 `linear_program_seconds`。失败发生于 `transfer.read_completed → validate_release`，还未进行必要24输入的恢复、真实普通值、J、模型或第64次LP。原63次LP及58个value保持原账。

原配置的来源是 `frame_curvature_feasible_steps.py::configuration` 中的 `linear_program_seconds=10.`；原direct-task配置保留该值。新入口把它与三个整数资源计数放在同一个 `type(value) is int` 检查中，因此拒绝了合法的原浮点数10.0。日志没有表明单次LP时限发生变化。

## 2. 唯一 core 修正

修复保留三个原整数限制：

- `max_linear_models` 必须是整数64；
- `max_physical_evaluations` 必须是整数160；
- `max_seconds` 必须是整数1800。

单次LP时限独立要求 `finite_number(value)` 且 `value == 10`，拒绝布尔值、非有限数和其他数值。原配置中的10.0不被改写成10，整个原配置哈希保持不变。原每次LP的10秒上限没有增大。

core的其余源码、支持构造、原512银行条目及旧4独立支持、冻结曲率guard、实际原两网验收、单次新primary和无新SOC边界均保持不变。修复不是第二次分配第64名额，也不修改历史63次调用。

## 3. 复用的准确范围

新transfer使用失败专用读取入口 `read_paid_first_attempt`，核定首轮run/job/head、completed failure状态、原日志以及REQUEST、DEVELOPMENT、COMPLETE的原JSON加LF指纹。它确认：

1. 旧三个组的11个实际verdict全部为true，且人工与科学执行次数符合首轮原记录。
2. 原COMPLETE属于上述类型错误，模型数为0、solver为空、没有接受点，新增值/J/LP/接受均为0。
3. 首轮168项请求与158个Python源码的完整关系一致；当前仅core、transfer、resume、recovery、audit这五个明确修复文件允许不同，其余163个路径保持原哈希。
4. 当前core的唯一类型检查文本逆替换后，必须精确恢复首轮已检查的core源码哈希。开发文件逐字不变。

下一入口不导入或调用 `developer_check`，只输出 `DEVELOPMENT_REUSED`。其含义是“旧源码的11项检查已经通过；当前开发组执行0、检查执行0”。它明确不把旧verdict改称当前修复core已经重新测试，也不为这个类型判断另加镜像人工。

首轮已付core SHA256为 `0042cb95a8f61f53f35e9edeed028fa0ed8f42215c952dd4b19c889fcd9afe40`；修复core为 `519d3e9d2853a25af5f04de1db5d71604660c22b0ec715a61af8d0324865638d`。冻结开发源码仍为 `3ea04322743cb45efbb157a4bd6f449ed227552ca5d53faab324491bb7036f45`。

## 4. 同一任务的累计时钟

首轮失败COMPLETE记录：

| 项目 | 秒 |
|---|---:|
| 原direct任务已付科学时间 | 257.595331213 |
| 本次失败新增科学时间 | 2.884255101000008 |
| 失败后的累计科学时间 | 260.479586314 |
| 首轮进程总时间，单列 | 4.209023590000015 |
| 首轮11检查执行时间，单列 | 0.0008896100000015394 |

下一进程在读取失败回执或原direct源日志之前，设逻辑起点为当前monotonic减去260.479586314。该逻辑起点可为负；校验只要求其有限且不晚于当前monotonic。真正预算仍由当前monotonic减逻辑起点与原1800秒比较。

`SOURCE_SCIENCE_SECONDS=257.595331213` 继续仅标识原direct源的历史事实。transfer传递给resume的继承累计值、recovery本次增量、audit总账和错误早退报告使用260.479586314作为本次起点。任何本次新增秒数都不得再减257.595331213，避免把首失败误算为当前新增工作。

首失败的进程总时间和开发时间只保留在独立回执中，不再次叠加到科学时钟。原更早关闭epoch的费用继续留在祖先账；不以重新下载来源、重建当前缓存或新进程名称重置它。

## 5. 尚未执行的路径与下一次范围

当前尚未实际验证同源末模型恢复、新支持判重和第64次LP。下一次仍须按原合同恢复同一真实点、同一配置、完整行池和冻结学习状态；确认真实新增支持后才可最多启动一个primary。无不同支持时必须0新LP；新候选没有SOC补救额度，仍须通过原两网各14门及严格下降。不能把此次输入类型修复解释为改善已经发生或有限凸模型已经求解完成。

此次读取新增一个首失败回执日志，并仍只读一次原direct科学日志；24项必要原输入按既有接口恢复。任何原始日志、模型数组或checkpoint数据都只留在runner临时内存/输出，仓库只保存源、参数、指纹和人读说明。

可核对的首失败指纹：

| 原对象 | UTF-8字节 | SHA256 |
|---|---:|---|
| 原job日志 | 136943 | `0216ddbbdd392d1e23240378b8aa6d61c4e154076db42895e2806004fab416eb` |
| DEVELOPMENT原JSON加LF | 1792 | `6cf5254aaeef45fe6cc68ece4c9b0f5b6359dbe0ac1233d3f53dc02d01de1a06` |
| COMPLETE原JSON加LF | 21997 | `ef90eadd0fe0314cfe4f388c311cd619748ba8c64b357dcde593e355b54f94da` |

完整新请求继续168项绑定，开发文件和workflow未变；只有上述五个源码哈希及失败回执/复用/累计时钟参数更新。全部后继执行仍由根统一在公开Actions调度。
