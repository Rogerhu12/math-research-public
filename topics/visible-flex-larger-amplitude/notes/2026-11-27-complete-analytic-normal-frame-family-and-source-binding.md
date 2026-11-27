# 完整六控制解析 normal-frame：独立十四源码、来源闭合与实际费用范围

本件交付完整可执行的十四源码及纯文字再生器，尚未在 Actions 执行。它在完整解析局部 J3 的既刊来源上，进一步把每个 normal frame 的六个控制偏导和所请求的全部角向 jet 显式求出；原固定参考、完整自由变量、全 32 段、角格、两组完整材料地址、已知保护前缀、typed 分离行、Phase I、QP、真实非线性筛和 root-packet 责任均保留。没有据源码结构宣布数值场、连续根支、精度或加速。

配套完整推导为 `2026-11-27-complete-working-normal-frame-analytic-six-control-jets.md`（19,445 字节，SHA256 `ebf46f17d767824673c29dceebac0dc26adb4fd83f9b63775db83f05abcfbe72`）。本说明补充完整运行链、来源变化、纯读接口和可核的费用归属；不替代该全文推导。

## 1. 实际完整父来源与新算术

完整父 normal 为 `04f1d2724e1d93f138d03c558262f53e1dd5433791c081c7f93c37eeab84e21e`，父 driver 为 `0dfb96e53fa92e741e2d94819636486b45c49e341006370d1c6864ce70c36b51`，父 pure 为 `c2a6039633dbb397bdb6f56358153a362ed4e34c8e035a6a739eb23d5a1b785e`。完整父十四件交付清单（十三运行体及相关来源）由既有 blob `21ecee7e4c86200deefe85a671d42350bca39d97` 固定。

旧 `_normal_frame_jets` 通过每个角向 jet 的三个反向积取得相对于六个 U0 分量的完整矩阵。本体对同一个工作表达式逐项求偏导：U1、U2 是独立的局部 jet 槽，但它们及全部 meridian、W、core/cap 数据的外参数计算图继续保留。每一列、每一阶仍调用原完整 `_total`，继而除以真实 S carrier；没有换积分权、节点、cell 宽度或原逐胞/累加顺序。

六个实际工作系数 A、B、Az、Bz、Azz、Bzz 各自使用原值，并各自求自身实现函数的导数。小参数支按其原二进制系数独立 Horner 多项式求导；大参数支对原 sin/cos/sqrt 表达式做完整乘商法则。独立舍入的 Az 不能替 A 的导数，独立舍入的 Azz 也不能替 Az 的导数。新输出的浮点字允许与原反向积不同；准确 Rodrigues、分支接缝、截断、舍入及连续逆函数费用仍没有由此自动支付。

## 2. 完整十四源码

以下字节是 revision2 的终锁字节。每一体均小于 100,000 字节，全部完整保存在同一 `scripts/resume_20261126/` 目录中；没有拆去原纯读校验以压缩源码。

| 完整文件 | UTF-8 字节 | SHA256 |
|---|---:|---|
| `analytic_frame_adjacent_normal_matrices.py` | 36761 | `3788b809c986668042e1c02f927afb85bf45434c4ff69607f9aaa2e2bf142695` |
| `analytic_frame_c1_reuse.py` | 35894 | `f1c74928089b60fb8f5350084ace0805fa956f4b06ac0de3f6a11357dd1aa2fb` |
| `analytic_frame_detached_normal_stage_matrix_reuse.py` | 47775 | `fa06705ebe19153edf455151a19c4217e42b8ab81ae3ffa4c1815701ec135255` |
| `analytic_frame_local_stage_jacobian.py` | 24261 | `894efd3b277b8a8c1fbd4abcd68b573fb09ee10a706a90ded7b2e1894fe3b866` |
| `analytic_frame_source_and_report_binding.py` | 20897 | `78aada58801198f9d3e29696e88f8834658286686728ac8f1b9ab369f827d94f` |
| `analytic_normal_frame_jets.py` | 33705 | `4ed6dfb93bb15b864d79c227b852421bc69b888a32923b98a21fe816da5be3d8` |
| `fullclosed_reference_centred_analytic_frame_material_envelope_so3_qp.py` | 80009 | `55af1d0feadeec46aab81ce72c027fdc25a60bf17fa92a5ee1d02aa358821a06` |
| `immutable_analytic_frame_normal_root_packets.py` | 69148 | `094ca6a87213a8677b46aa9b0ad4c5a4b12f8c4c80437d7b640c47f7793b40f0` |
| `launch_reference_centred_analytic_frame_material_envelope_so3_actions.py` | 21369 | `f429905e37a4dcb41a1cb6a70afb6d55c41ae9553b39ffe4fdfc3c8f753926cb` |
| `read_reference_centred_analytic_frame_material_envelope_so3_report.py` | 97308 | `a9f4f27c46c1f870c276c35613ad71a1e411ac6e2d95556415b5daee31cb6a76` |
| `reference_centred_analytic_frame_smooth_triangle_calibration.py` | 11921 | `fe422dbf2eac68bbc4f54e8fe290ba0e5d1b7a080f12f1d148cffe834957dba0` |
| `so3_reference_centred_analytic_frame_material_envelope_geometry.py` | 68945 | `755f9b7d2250f3d5dfa294ca9e862bf0bdf1786781747d3727e6ce5b750d9f60` |
| `so3_reference_centred_analytic_frame_smooth_triangle_normal_lift_operator.py` | 96558 | `3d8d3ed8f2a21db5731fec87115546502a49b701f7344328e8e36396cba52dbc` |
| `transfer_material_envelope_memory_to_analytic_frame.py` | 63666 | `a9eed46389ce5f4262d6547a10ec42b6200072b185bd747cbb3814c008d81842` |

完整锁表 `complete-analytic-normal-frame-family-delivery-v2.json` 同时列所有远端未引用 blob、实际本地路径、公开目标路径、57 个完整来源 role 和纯源检查结果。根代理是唯一 ref 写入者；这些 blob 本身不表示已提交、已准入或已执行。

## 3. 每层改变与原完整函数保留

新 normal 的原 61 个方法中，仅 constructor、`_normal_frame_jets` 和 metadata 改变：constructor 核完整新 helper，模型新增 `analytic_normal_frame` 定义；frame 方法只转交完整新 helper；metadata 追加实际计数。其余 58 个完整方法 AST 与 04f1 相同，包括 `_run_chain`、`_get_roots`、完整角向隐式链、fields、J/J*、所有原方程、回溯和最终 endpoint 原方程复读。

新局部 J3 的 20 个函数体 AST 全同父；C1 的数学 template、scope、缓存字比较和所有活动图规则保持，只有来源定义及首次完整 frame 的说明改为实际当前 analytic/full-AD-fallback。detached 和 adjacent 的数学函数保持，其定义明确当前 frame 来源。calibration 的 12 个函数体 AST 全同父。geometry 只改当前来源和实际 C1 等号，全部扫描、旧前缀、新 typed 行及真筛函数保持。

Driver 从带缩进的 `def save_report(` 起，到完整 EOF 的全部字节与父 0dfb 相同；该后缀已经包含原两个只读 packet 钩子，完整 SHA256 为 `d4420ab62c512f350f6f6c2a12e47da5272ac8088b24f9fe338fd9cb3a316376`。只在首 F 前加载完整来源、构造算子和报告新定义。没有改科学预算、μ、范数、p、目标、分离策略或接受条件。

## 4. 来源、纯读取与父场迁移

原 48 个 driver 来源 role 全保，另外增加当前完整 analytic-frame helper 和八个明确历史父来源，共 57 个。完整调用者 SOURCE_PINS 仍被 packet 逐 role 核验。packet 原四个完整 normal 注册项保留，另加当前 normal、J3、frame、adjacent 和 calibration 的真实来源；记录当前 frame 计数，捕获前后不调用 F/J/root、不提升角向 order。

Pure 原来接近 100 KB。为继续保留所有校验，完整 `independent_chart_binding` 函数逐字移入独立小 binding 模块；reader 对该实际函数 codefile SHA 和全模块 SHA 同时核验，随后仍做完整 fixed target、whole reference、模型、chart、scalar、支持 seed、frame/C1/矩阵和材料包络交叉等号。不是删除 target 校验，也不因新 helper 自报身份就接受另一个场。

新 binding 明确列三条可迁移完整父家族：cc0a/104e、95559/f382、0dfb/c2a；每条先调用它原来的完整 pure reader并核原所有政策来源。只有明确的当前来源、schema、frame/matrix 工作政策及 calibration 来源字段可不同；完整 base、目标、chart、seed、自由空间、共同 partition 等仍逐对象相等。没有推断迁移前后浮点场值相同，后继须重读真实基线。自身 restart 保原同 source/model/norm/current-point 和完整 typed 来源守卫。

当前十四体完整保留原独立 7c 输入责任。09 的真实公开输入已经由其独立 producer/binder 绑定；把该目标用于本算法，需要 geometry 负责的完整新上层来源派生，不能把 7c 字段换标签或把新 hash 直接称相同数学 g。此交付不重跑 09 的已完成必要输入。

## 5. 实际计数与失败含义

新增 helper 单独记录每个 order 的完整 frame 请求数、完整角块/角 jet、活动/无梯度请求、六列开始/返回、原 `_total` 调用与真实角向量数、六系数值/导数调用、完整原 AD fallback 开始/返回/失败、实际反向积，以及实际旧 normal counter 增量。`frame_call_seconds` 包括该完整调用的输入/word 检查、计算和输出检查费用；没有用理论少了几次 AD 来填实际秒数。

原 normal 的 `frame_reverse_angle_products` 仅在确实执行原反向积时增加；解析成功不能伪记成完成了原反向积。C1 旧键 `original_frame_evaluations` 在新完整 policy 中明确解释为当前完整 frame 方法调用，不能误读为 AD 次数。最后调用记录保其 own point、order、完整 previous-word 摘要、来源及失败；纯读不跨点回填，不把未返回 frame 的槽补零。

数学/shape/source 错误诚实失败。通过完整输入守卫之后，解析数值不可用时可对同一完整角批、同一完整阶数执行原完整 AD frame。一次失败里先前已经发生的解析列/积分费用和实际 fallback 费用都保留。完整 caller 的真实 root/几何/Φ 筛继续决定结果，helper 成功不等于求解成功。

新的纯读根键为 `analytic_normal_frame`；实际值在其 `latest_actual_diagnostics.actual_counts`、`latest_actual_diagnostics.frame_call_seconds` 和 `latest_actual_diagnostics.last_call`，其中 `latest_actual_diagnostics` 在没有实际完整 metadata 时可为 None。原 driver 报告对应的是 `latest_operator_metadata.analytic_normal_frame.actual_counts` 等，不把两种层级混用。公共 summary 应只选来源 SHA、计数、秒数、布尔、own-point/word SHA 和已有标量错误，不把完整控制字、矩阵或逐角数组转成字符串公刊。原 `analytic_stage_jacobian` readout 保留，内部同时保 frame 的实际归因。

## 6. 真实修复记录：revision1 未准入

原候选全十四体已保存但未执行；geometry 独立核查发现 GeometryScreen 从祖先完整体继承的 C1 source literal 仍为 ba3d，而当前真实 C1 为 f1c749。该等号会在新首 screen 拒绝正确新对象。revision2 精确替换该 literal为当前完整 C1 SHA，另只递归更新 geometry→driver→launcher/reader 的三处来源 pin；十个运行体字节完全不变。旧 guard 没有移除，旧父政策依然分别核其原来源。不能把 revision1 的静态数学审当成首场已通过。

## 7. 已实际做过的验证与待实际事实

实际完成的本地工作仅为：完整源码 AST/compile、无重复 literal key/尾空白、完整 source-role/policy 读取、12 个原方法 runtime canonical-AST 合同对照、J3/C1 方法守卫对照、完整父→子函数差异、原 driver 后缀及完整 chart 校验迁移逐字比较、四处 revision2 精确文本差异、两个独立 Python 进程的全十四体再生。再生器对全部父源、helper 和每一个输出完整 SHA/bytes 硬核，并稳定序列化 set literal，避免 Python hash 随机化造成假同源。没有 import 科学模块，没有本地 F/J/root/QP/区间计算，没有缩小问题的 fixture。

完整再生器为 `derive_complete_analytic_frame_family.py`，36,446 字节，SHA256 `1d3909fe814b69a85708bbb7f3ae5c22c5bd215b08290a4ef697e69aa37b8f9c`。以已刊十三完整父目录与本 helper 为输入，输出独立目录；`--verify-existing` 逐字核十四完整结果。配套 `verified-reproduction.json` 保全部来源 pin 和实际检查结果。

接续工作应在公开 Actions 运行真实 09 全问题入口，读取原完整阶段、frame/J3/C1/矩阵计数、成本与真实结果；尚无本版本耗时、首场、方向或接受结论。若仍慢，依据实际计数定位后继成本，不以源码推测替代实际返回。完整连续费用、有限数值精化及全域完成标准继续原样承担。

## 8. root 全体再生、原未准入来源与实际09接续

root 完整读19,445-byte公式推导及33,705-byte helper 的六系数导数、六列全部角jet、原_total逐列归约、完整AD fallback和计数读回；只核代数与源码，没有科学执行。随后使用本仓库实际完整父源运行36,446-byte再生器，真实exit0，14个全部结果逐字SHA匹配；再独立流式核57个实际source roles，全部与当前源码相符。完整driver的原科学suffix与两个只读hook保留。

这次精准C1来源守卫修复也说明此前已刊解析J3 geometry7817的祖先literal不能据其两份ready文件存在视作可运行准入；原候选、原全源码、原参数及缺陷记录均保留，没有覆写旧身份。新geometry755f核真正f1c749，旧95559实际使用ba3d不受这个新族适配遗漏影响；不把静态遗漏倒推成07取消原因或任何未返回科学异常。完整修后14体独立刊出，09使用它们仍须真实306b/9e3d/2518目标上层，不能冒原7c输入。

09实际3已经真返完整dc5与全90词、目标canonical7c766/绑定21a44，两5e373原卷在runner冻结；本包不重跑该输入。接下来完整09上层及原全参数只依据这些真实文件接入，首场、frame/J3成本、完整方向和几何结果由真实Actions返回后记录。锁表与纯检查输出是scratch来源元数据，完整14源、全文推导和全再生器在仓库；没有把任何科学raw数组另存入Git。

本次全空白检查只报告全文推导、4ed6 helper和1d3909再生器各自已锁的末尾空行；原完整字节及所有来源SHA保持。排除这一明确EOF类别后，其余空白检查通过；没有为格式而改掉被完整依赖的源码。
