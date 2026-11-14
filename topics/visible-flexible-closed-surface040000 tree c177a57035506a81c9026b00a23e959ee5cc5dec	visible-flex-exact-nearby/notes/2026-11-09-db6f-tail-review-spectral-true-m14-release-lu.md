# 独审：true M14/W14 的显式 LU 生命周期完整入口

审查人：`/root/tail_review_continued_2`，2026-11-09。

结论：**PASS，限于新入口的完整源码、原数学门保留、显式运行身份、纯准备及正常负门。**
新入口可作为与原 v1 分开的条件运行分支。此结论没有运行新 Newton
选择、BVP、DN、flow、RK，也没有产生新 CP、系数、tail 响应、root
完成观察或未来正例。`G5=false`，README 完成条件未支付。

## 1. 审查对象和完整阅读范围

完整阅读作者说明、三份新 Python 源码、全部新旧源码差分及发布清单。
数学函数与 helper 的前一完整独审另见
`2026-11-09-db6f-tail-review-newton-release-lu.md`；本次绑定该报告及其
发布清单，补审它怎样接入原 true-M14 程序，而不是把函数级审查直接
视为完整入口审查。

| 本次作者对象 | SHA-256 |
|---|---|
| `db6f-prefix-spectral-true-m14-release-lu.py` | `2db1fe8b9171c3d9a7a4ac0d11311cff8daec1aa36bb8cd91130148903070ed0` |
| `db6f-prefix-prepare-spectral-true-m14-release-lu.py` | `2018226a193294d7791492ec44d595e19ae004079ae717eb5557db249a21949c` |
| `db6f-prefix-audit-spectral-true-m14-release-lu.py` | `ee0d6aeadc4cfbe25ef4788581cebf81d5a50cfdb77b9a47f83d9d6df3071989` |
| `2026-11-09-db6f-prefix-spectral-true-m14-release-lu-implementation.md` | `1bb29288824bd4fd6f9527e194d8051f5ff8a302f9bf1f9b733469ab6b062449` |
| 全部源码差分 | `e886192674b9b53cae602eb5a408ea7fbb2a69cd66656894bc637dc466f4bd47` |
| 作者 10 件 publication | `8fdc29cc861e59b1b4ae3dd2f3d75941ce56b212a9d5c7cb14476fc448571915` |

作者 10 件共 173253 B，逐件重算字节数和 hash；所指函数批次 7 件
也全部重算。另核原 v1 三文件仍为 `d0eba3d8…`、`de3ce21b…`、
`1aa5e539…`，未覆写原身份。独审来源清单包含 131 个唯一实际文件；
这些 hash 是本次读盘值，不是照抄作者声称。

本次还全文检查了 W14 共轭源码及 callback 来源抽取函数，检查所绑
SciPy `_bvp.py` 中 `solve_bvp` 对全局 `solve_newton` 的使用。底层
已审几何、shooting、BVP 公式沿用冻结来源；没有声称重新证明这些
后端的全部数学，也没有复算任何活动 attempt 的数据。

## 2. 数值程序的边界

三份入口源码的改动是显式版本选择和审计身份。唯一计算循环改动仍
是已审单行：当原 Newton 决定 refresh 且尚未达到 8 次分解预算时，
在新 Jacobian/LU 之前令旧局部 `factor=None`。该行删除后原函数逐字
一致，内部 24 次循环、8 次分解、21 档线搜索、接受式、异常分支均
未改。此次入口没有另加默认排序、容差、阻尼、projection 或
Jacobian 修改。

以下旧数学门由源码逐项审查和独立 AST 比对共同核实：

1. `expected_config`、`expected_parser_argv`、`without_io`、typed
   `equal`、`module`、`write_json`、`runtime_callbacks` 七个函数 AST
   完全相同。
2. 原 `runtime_newton` 只改函数名为 `runtime_original_newton` 后 AST
   完全相同，旧函数与原 `install` 的实际来源检查仍在。
3. 关闭审计的 `check_packet`、`polynomial_endpoint`、CLI `main`
   AST 完全相同。
4. `first_packet` 只改本次 selector 文件名，`check_outputs` 只改结果
   身份字符串；把这两个声明的字符串还原后，AST 完全等于原 v1。
5. `check_runtime_records` 仅把旧 Newton 运行身份块换成明确的新身份
   块；全部 W14、原物理 RMS/BC、mesh、14 个物理 callbacks、原
   SciPy 来源及 CP 对应门保留。`final_audit` 保留原关闭链，额外
   检查旧→新转换及共享 STATS 声明，使用明确的新成功状态。

实际新旧准备 metadata 逐类型相等的项目包括 settings、W14、旧真
CP、它自己的最终 tail warm、全部冻结物理字段和原 21 callbacks。
原参考索引名称虽含 affine，其实际 CP 和自有 final tail 来源均
保留；没有用 affine01 或 true01 失败输出替代初值。

因此，仍是 M14、43 states、14 个参数、13 scales，prefix angular
512/audit angular 1024、原 W14 最大权 2048、原 seed mesh 保留、
max nodes 6500、`tol=2e-9`、`bc_tol=1e-8`、physical BC `2e-11`。
tail 仍 Nθ512、depth12、P8/S32、audit32、36 次迭代、shooting
tolerance `2e-9`、原默认 floor `.05` 和原全模初边界修正。
warmup 显式空；原最多 8 轮实际 DN 外层、原 Node 1536、原最终
Jacobian/audit 请求不变。

这些数值是绑定程序和准备包的设置，不是本次已达到的数值结果。

## 3. 实际函数选择顺序与全局解析

原 `db6f-prefix-coupled.py` 的 `main` 导入原 `install, STATS`，
并在进入 `solve_with_actual_tail` 前调用一次原 `install()`。
新 runner 只替换原 `runner.solve_bvp` 调用槽为自己的 `selected`；
原 tail client、真实外层、chart、边界条件、物理 C²插值及保存函数
仍为绑定原件。

`selected` 的真实源码顺序是：

1. 核原 BVP 的 tol、bc_tol、max_nodes 与 kwargs 集合。
2. 核对象固定 M14/N512 属性及全部 14 个实际物理 callbacks。
3. 首次进入时，执行完整原 Newton gate，明确确认当前 SciPy 指针
   指向原 `f6curve_domain_newton.solve_newton`。
4. 核新 helper 的 `select_newton` 来源，再显式选择新定义，保存
   `before_selection_original_runtime` 和 `selected` 两套记录。
5. 检查新 runtime；完成首个真实 DN 包的只读关闭与绑定；进入原
   W14 selected solver。
6. 每次真实调用均在 `finally` 再检查新 runtime，并写实际记录。

首次真实 DN 发生在第一个 BVP 前；保存首包只支付首包。它不支付
inner 收敛、outer 收敛、最后 seam 或完整闭图。

**先创建 W14 solver 再选择新 Newton 不会固定捕获旧 Newton。**
W14 的源码导入并保存原 SciPy `solve_bvp` 函数，然后调用它；冻结
SciPy 源码中的 `solve_bvp` 在实际运行时使用模块全局名
`solve_newton`，该名既不是其参数，也没有在函数体内成为局部赋值。
故对该模块全局槽位的显式选择会作用于随后真正的 BVP 调用。
本结论来自读取/AST 检查，没有执行 solver factory。

选择后，新函数保持明确的新模块身份
`db6f_lu_lifetime_selected_definition_v1`。原函数导出没有被覆盖，
原 install 没有被改写；每次前后 gate 都核 SciPy 当前指针、新旧
源码、相同 NumPy/splu 以及共享 STATS 对象。若原 install 又覆盖
当前指针，新 gate 会拒绝。程序没有临时恢复旧身份来掩盖新函数。

## 4. STATS 和完整关闭证据

此前已审 helper 在变更 SciPy 指针之前设置
`derived.STATS = original.STATS`，并核原函数 globals 使用的也是
该对象。新入口没有重建字典或清零计数，因此原 main 已导入的
STATS 引用与新函数更新的是同一个字典，原 CP 的
`newton_domain_audit` 仍能记录实际新函数计数。

新运行的来源不能用旧 v1 的 gate 冒充：launch schema、actual
command、来源闭包、程序成功/失败状态及审计成功状态均声明新
版本。新 launch 保留原 21 个 callback，另外明确登记新 Newton、
`select_newton`、`Selection.check` 三个 callback。本次独立从 AST
重提取所有 24 个函数的完整来源片段、首行和 hash，逐项吻合。

新 `check_newton_lifetime_record` 要求严格 8 键记录，核原定义、新
函数完整 callback identity、11 参数签名、新 module、实际 helper
身份、唯一原 SciPy 来源，以及 `original_STATS_alias is True` 和
`changed_runtime_identity is True`。原→新 transition 还单独核
原模块名和原签名，不能仅把原 hash 字符串改名就通过。

最终关闭依然从 root 的真实外部观察开始：正确 stem、
`observed-process-completed`、`observer=/root`、真实非空 receipt、
正整数 session id 和实际 exit0。guard-child 的记录、程序内部
requested exit、文件存在和捕获异常后的退出都不能替代这一门。
随后逐项重读本次 reproduction、全部来源、CP、summary、系数、
真实 final outer、own final seam 和 first-request binding，核
原 finite gates：

- 原物理 RMS≤`2e-9`，真实 outer BC≤`1e-8`；
- 最后 shooting residual 严格 `<2e-9`；
- 全部 43 states 的有限 float64 五次系数、连续覆盖的 mesh、各
  压缩块 hash/bytes 且单件 `<5000000 B`；
- 14 个参数、13 scales、原保存表示实际高度 roundtrip；
- 616 Jacobian、17 jets、8 audit、865×28 staged states、13×28
  raw mirror、896 角度 seam；
- 原固定物理定义、实际调用顺序与每次前后新身份。

原 history 最后一基点 norm 不被误要求等于最后 shooting residual；
outer 内层节点高度也不被误要求逐位等于随后物理五次表示的端值。
上述保留项由旧 `check_packet` 和 `check_outputs` 的 AST 一致性
提供直接源码证据。

## 5. 独立实际执行与来源闭合

只使用未用 stem
`2026-11-09-db6f-tail-review-spectral-true-m14q512-release-lu-pure-01`。
作者 stem 没有重用，任何已绑定作者文件均未改。

| 操作 | 实际 tool receipt | 实际退出 | 观察结果 |
|---|---|---:|---|
| 原新准备器，独立 unused stem | `659f7d` | 0 | 117 bindings、24 callbacks，仅 3 件 metadata |
| 原新 final auditor，正常 `--check-current-gate` | `c8f67d` | 2 | `NOT_READY_OR_REJECTED`，缺 root 实际观察；零求解、未读活动 trace |
| 独立标准库 source/AST/metadata checker | `f9b97a` | 0 | 5 组检查、131 来源、全部通过 |

独立 prepare 的 launch SHA 为
`ad8472a422abd09268afe7dad2b6045f1ebf8b4e640f8f04e0dae099cea54a7d`；
preparation SHA 为
`8abbb83b01a20e6f9de4547ad1cad14f05a98c783f990b33b21eb0eb68510f63`；
config SHA 为
`2f6b09eb4d49c5ac1d49d04f8bb635ab2d86b2324c50c28db0ac016d2972a075`。
独立 checker 报告 SHA 为
`fe47ee7a6d9fe2f24a1cc7144111a1f0ddbdbc71e267b4af0fce1ce5fbde371e`；
来源清单 SHA 为
`f7dce9cba37d99447764a3217ca96a1306d29e33bc1aaf343171545877753feb`。

两份实际准备结果除新 stem、由该 stem 决定并已各自重算的 config/
launch identity，以及路径排序中的相应位置外，逐类型完全相同。
对准备目录再检查，实际只有上述三个文件；缺观察负门没有写新
输出。独立 checker 没有导入任何项目/solver 模块，只使用标准库
读字节、JSON 和 AST；所有数值求解、install、selection 计数均为 0。

独立 checker 在冻结前有两次自己的实现性失败：`dbfdaa/exit1`
尚未忽略 Python qualname 的 `<locals>` 标记；`c1d72c/exit1`
尚未把新 stem 的 config binding 在路径排序中移动的情况标准化。
后者经 `8d9eb9/exit0` 只读差异定位，证实唯一差别是同一 binding
集合的排序。仅修正未封存的独立 checker，再得 `f9b97a/exit0`；
作者源码、gate 和真实数据均未因此修改。这些失败不作为作者问题，
也没有从失败文件倒推任何求解成功。

## 6. 结论的实际限度

该完整备用入口的源码和来源闭合通过独审；若 root 选择实际运行，
应使用独立新 stem 和完整新 launch，并由 root 另行绑定真实资源/
空间 guard 和实际工具观察。本次没有运行这一分支，不能以纯
准备或 source review 为它填写运行成功。

解除旧局部 LU 引用不保证 allocator 立即归还内存，更不保证
3/4 GiB 预算能过；新网格首次分解本来没有旧 factor。来源也没有
提供失败发生在首次还是后续 refresh 的足够证据。原 v1 的关闭
失败和活动尝试不混入本批判断。

即便以后有限联解通过，本入口仍不支付新的完整 XYZ、公共 C²切口、
连续全域 metric/κ、reach/whole budget、normal `2e-9` 终门、旧
收敛比较、最终独立复算及精确极限的缺口。没有构造新的完成门，
也没有撤销 README 的任何完成门。
