# Added gamma 九维 KKT 的显式初始高度入口

状态：完整独立三源已形成；尚未科学运行。当前执行环境不可用，本修订仅作完整文本生成、逐字一致性与来源核对，尚未执行 Python AST / compile。它不改变已刊 b712 完整 operator、0c488 完整几何 adapter 或所求固定标量度量。

## 1. 本次输入究竟改变什么

新入口采用同一真实参考准备、同一固定材料角、同一十八字 Q、同一两旧支撑与独立 gamma、同一全部外层自由变量及完整九维 KKT / 二十七维角 jet 链。它先完成原参考初点与 Q 的全部校验，再复制自由向量，只把最后一槽 H 换成命令行明确给出的 binary64 常量。

这组合两个已单独研究的选择：独立 gamma 六控制族，以及另一显式自由高度。它不是新的 g，不是移去旧永久位置的理由，也不是根、几何或等距存在证明。一个采用于旧运行的 Jstar 工作字，放入新运行时仅是一个明确常量；本入口不称它等于新运行的准确积分或新工作积分。

新命令使用必填的 `--initial-height-hex`。只接受有限且与 `float.hex()` 完全一致的规范字，避免十进制解析隐去实际输入。高度可以在后续完整方向中变化；它仍是原来的自由变量。代码不以高度输入声明或预先假定几何可行。

本版是明确的 fresh-reference-only 入口：若给任意 restart 或 direct-base-seed 参数，立即拒绝。这样高度替换始终对应已经校验的原 `base.initial()`，没有另一场初点与旧 Q 初点身份混合的分支。

## 2. 原输入校验先于自由点修改

driver 的实际顺序如下：

1. 逐 SHA 校验全部现有来源；读取并完整绑定实际 reference、preparation、carrier、node、scalar 与准备位置全集。
2. 用原 7f26 完整体构造 base，保原全部自由 core、旋转系数与 H。
3. 走与 5134 完全相同的两个互斥 Q 输入分支。旧分支保持原 4dc 严格验证；新分支保持 ea94 的当前 reference / profile / base / initial / chart 十字段验证。
4. 用未改的 b712 构造九维 KKT operator。构造器再校完整来源、模型、Q、支撑、gamma、范数单位与角 jet 维数。
5. 取 `q.initial()`，逐字比较完整 `base.initial()`。旧输入再比 `trace_initial_full_point_sha256`；新输入再比 `initial_full_point_sha256`。修改 H 前原始摘要必须一致。
6. 确认 endpoint 缓存为空、当前点为空、所有 endpoint / KKT / continuation 计数为零。只复制原向量的最后一槽，立即核全非 H 前缀字节相同、原 base 初点未被修改、完整 q / base 模型身份未变。
7. 记录实际初点及高度输入，然后执行原全位置记忆、正权测度、几何预算与完整首次物理读取。任何根失败仍按原完整失败路径保存。

新/旧输入分别从各自原初点字段取身份，并不把修改后的 H 写回 reference 或 Q definition。十八字 Q 是该固定控制输入的常量；本入口从未将它称为修改后实际矩的逆。

## 3. 原物理与求解主体完全保留

`SOURCE_PINS` 与 5134 相同，包含 b712、0c488、7f26、4e65、ea94 及全部旧 Q / 几何 / 谱目标 / QP 来源。本次没有替换 operator 的任何方法，也没有 monkey patch 或改物理 schema 来通过旧 guard。

从 driver 的 `def save_report():` 开始直到 EOF，与 5134 源逐字相同。这覆盖：

- 全场初次统计、根异常报告与首次完整几何筛；
- 原全部带正权 Gram 行、完整 J / J*、原自由量和既定 H² 坐标；
- 192 选择器及追加幅度约束、共同松弛 Phase I、全部选定物理行；
- 每个可接受候选的真目标、真域、全网格与全部永久位置复读；
- 所有拒绝点新位置记忆、父重读、回溯与最终独立复读。

因此该入口没有把新 H 当作已通过的场，也没有跳过首读以回避之前的根失败。根的原物理容差、dimensionless KKT 容差、控制/乘子域、辅助 continuation 数值参数与外层方向预算，仍由全部显式原参数确定。只改变高度输入不会把某次旧 Phi 或根证书带到新初点。

## 4. 完整可归因记录

新增 `initial_height_input` 保留：

- 规范请求字、请求值的准确有理数；
- 原/新完整初点摘要、原/新 H 的 binary64 hex 与准确有理数；
- 原/新非 H 前缀摘要及逐字相同的实际断言；
- 全自由维数、最后槽索引、dtype 和 shape；
- 原/新 model identity、base / fixed profile / Q definition / reference 身份；
- 采用的 Q 输入 schema 及该 schema 的原初点字段名；
- 原初点已验证、原 base 初点逐字相同、首次 endpoint 缓存为空的事实；
- 没有修改 reference、模型、目标或 Q；没有继承旧 Phi、根或几何证书。

独立 `initial_free_point` 保留修改后当前完整向量身份，在任何 F / 根读取前生成。它不计算物理场。报告初次成功 statistics 的当前点摘要与 H，或初次失败 snapshot 的当前点摘要，必须与这份记录相同。

所有旧完整 gamma snapshot 字段、latest metadata 和二者各自点身份，沿 42c0 真实接口保留。若初次根失败，各数值空读数继续为 null；纯 reader 不从其他点或旧 H 报告补值。九维 KKT 已算矩阵仍只存在 runner 原报告中，公开摘要不传原矩阵或失败原始科学数组。

## 5. 新 reader 的独立职责

reader 严格固定本次新 driver 全体 SHA、新 report schema 和所有原 source pins。它保 42c0 原两模式 Q binder、模型 / g / norm / snapshot / 失败合同，并增加纯 JSON 与来源核验：

- 确认 fresh-only，没有 restart / direct-base-seed；
- 确认旧/新 Q 对应的原初点摘要与未改 reference 初点摘要相同；
- 确认记录中的唯一改变位置是末 H，非 H 摘要、dtype、shape、模型与全部目标身份一致；
- 规范 hex 和 Fraction 表达逐项一致；
- 若 H 字改变，当前摘要必须改变；若 H 字未变，当前摘要必须保持；
- 初次实际成功或失败的当前点身份必须属于修改后的初点。

这是对已记录完整来源和运行断言的纯归因。reader 不重新生成完整自由向量，不重算 F / 根 / J，也不把 JSON 摘要自身提升为连续证明。

## 6. 来源闭包与完整文件

父三入口：

| 文件 | 父 SHA256 |
|---|---|
| fullclosed_zero_gamma_kkt_so3_qp.py | 5134d34d4f4393fc57d86eed329bd107b631b693668d1d04d602af5f286dc3f5 |
| launch_zero_gamma_kkt_so3_actions.py | e0925d2628bf88760042dcdc3d998ec3a4ff51977d49a4568f6a543bf5fa4bb0 |
| read_zero_gamma_kkt_so3_report.py | 42c0c0f043cbbbc0335a8faed9d91f9f6583cb7501d40dca0fcef6b834d69e14 |

显式 H 输入原则来源是已刊 `fullclosed_zero_moment_height_so3_qp.py`，完整 SHA256 为 `34c9273aad6ccc3299c8b64ac250a37b3ae758eec34945ef00a4b14a3acaf1b3`。本次明确扩到 dual input，并选择 fresh-only 合同；没有更改其历史字节或冒充同一入口。

| 完整新文件 | 字节 | SHA256 |
|---|---:|---|
| fullclosed_zero_gamma_kkt_height_so3_qp.py | 71325 | 8f37529deaa8e07d4561e00371b39b82cb641a4e52e0790d41555b2ae9e320a9 |
| launch_zero_gamma_kkt_height_so3_actions.py | 15993 | da41136c61e333cf4835e7209565b5502deac8d2a6bcc91d6cc4a863c2228953 |
| read_zero_gamma_kkt_height_so3_report.py | 48971 | c3fdd83c29dabeb00974899bb183360da01c57fcf364704759efcc1ac643b9ec |

这三份是完整源，不是片段。纯文本已核 driver 的原全科学 suffix 一致；launcher 的 parse_args 去掉 install / print 两项后与新 driver 完全一致；未发现尾空白。当前无可用执行环境，因此尚未实际执行本次新文件的 AST / compile / argv，更未做科学测试或造 fixture。后续真实 Actions 将给出实际字段与失败/成功，不在此预写结果。

## 7. 同 g 历史与实际运行参数

run05 计划必须读取本运行真实再生的位置与所有必要方向报告。已明确的最少闭包为 reference locations，以及独立 3 / 17 / 21 / 26 / 30 对应的五份物理报告；如还有真实新增的必要后继，控制器必须显式追加。新 raw 身份不是删除旧同 g 永久点的理由。

计划继续完整 N=2048、M=160、J=923、P=7377 的原观测与全部自由量；首预算保持父 gamma 的一条 metric 方向最多 16 步、最多四条 restoration 每条 64 步、15 次 ray 试点，mu=.01、p=4、epsilon=.001、scale=.05、原几何 / 幅度预算。高度是额外明确的初始自由点参数，不调整这些值，也不是收敛或完成标准。

若首 KKT 仍失败，这只说明本次数值入口在其实际预算和选枝方法下没有返回原方程的可用根。未判明的端点可达性、KKT 曲率退化、跨角分支、其他 E/B、全局几何和固定问题精化仍保其原范围，不能由这份实现记录宣布任何一个已解决。
