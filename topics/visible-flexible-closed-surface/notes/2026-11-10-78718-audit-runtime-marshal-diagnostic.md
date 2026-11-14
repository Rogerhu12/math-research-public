# run02 原函数 marshal 差异：限定诊断、独立重现及旧门实测拒绝

审者：Astra-visible-flex-78718bd0 / independent_audit，2026-11-10。
审者未参与 run02 或后续候选的种子选择、节点预算决定、调参或优化。
本次只审运行代码身份的诊断事实，不运行候选数学求解或最终全链独跑。

## 0. 结论与边界

**冻结诊断的限定结论通过源码审查和真实独立重现。**
同一实验进程中，新鲜导入与同源重编译的四个原函数，其诊断所列代码字段
递归相等；新鲜导入的原始 marshal 摘要均与 run02 记录一致，
但三个函数的 marshal v4 字节不同。
这一现象不是一般代码等价性定理，也不把原失败候选改为成功。

独立补做的旧源码身份谓词实际调用显示：在该旧谓词自身的编译/持有上下文
中，四个原函数都被原摘要比较拒绝，包括在原诊断上下文中 v4 字节相等的
solve_bvp。因此不能把某一诊断上下文中的相等外推成旧门通过。
两组观察均在同一声明解释器路径和固定原 SciPy 源文件下成立，不矛盾。

全部旧门、旧源码和原记录保持原样。本审没有采用新的身份替代规则；
未来另名 driver/preparer/auditor 与规范化身份模块尚须各自冻结和完整审查。
本次不替未来实现预先发放通过结论。

## 1. 实际审查对象及输入身份

完整读取并审查
[78718-diagnose-runtime-marshal-v1.py](../scripts/78718-diagnose-runtime-marshal-v1.py)，
5332 B，SHA256
68a8b42162577582bbf69aaf021e69d3348819de9cc731bdfc1af0858a377258。

原作者诊断为
[numerical-run02-marshal-diagnostic-01.json](2026-11-10-78718-numerical-run02-marshal-diagnostic-01.json)，
14150 B，SHA256
a23f037cf90618abcc5549802371f7fb450ed7fe5fe68ed358f7b812fb906db4。
报告内容在终端内解析和比较，没有把报告数组或候选数据输出到对话。

诊断所读 run02 reproduction 为 153415 B，SHA256
1addc01f67b705da3a44cbbbd62a94f48d991969bbb1c6b8e5be4db9166e1add。
它所指 launch 的 SHA256 为
b935a5863a88e6c4541357a558c6b3874ed3ba89174b65032b0494425681c671。
本审独立重跑前，实际核对该 launch 的长度和 SHA256 与 reproduction
内原有绑定相同，然后使用 launch.command[0] 指定的解释器启动诊断。

实际解释器路径是
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python；
报告的 Python 版本是 3.12.14，optimize=0，marshal.version=4。
“同解释器”在此首先指两种代码对象确实在同一个 Python 进程中比较；
另核其可执行路径与绑定 launch 一致。它不是对某个未记录二进制镜像或
全部历史环境的额外认证。

原 SciPy 源为运行环境的 scipy/integrate/_bvp.py，硬编码且实际匹配的
SHA256 为
59afffb3607b272ae77f346d86428e43eca359fe90f2605da60a9571e60970d2。

## 2. 诊断源码实际做了什么

程序先检查输出文件不存在，读取 reproduction 和它引用的 launch，
要求 sys.executable 与 launch.command[0] 完全相同。
随后正常导入 scipy.integrate._bvp，并对模块源文件实际计算固定 SHA256。
对四个原函数记录，要求保存的 filename 与当前模块文件解析为同一路径。

每次重编译使用原源字节、记录中的原始 filename 字符串、exec 模式和
dont_inherit=True。它从模块代码常量中寻找唯一同名顶层 CodeType；
没有执行重编译得到的科学模块或函数。
现场对象取自新鲜导入模块中相同函数的 __code__。

对比范围是以下十八个字段：
co_argcount、co_posonlyargcount、co_kwonlyargcount、co_nlocals、
co_stacksize、co_flags、co_code、co_consts、co_names、co_varnames、
co_filename、co_name、co_qualname、co_firstlineno、co_linetable、
co_exceptiontable、co_freevars、co_cellvars。

deep_equal 先检查对象类型一致；CodeType 递归按上述字段比较，
tuple 递归逐项比较，其它类型使用 Python 的相等比较。
所以报告中的“字段递归相等”准确指这个明示谓词。
它不是通用的常量逐位编码：例如 Python 的浮点相等不区分正负零，
也不是对任意容器的完整对象共享图核验。
这不损坏本诊断实际报告的谓词事实，但不能把它冒称为已完成的
规范化、逐位 CodeType 身份协议。

对每个现场对象与重编译对象，程序实际调用 marshal.dumps 的版本 0—4，
记录长度、SHA256 和首差位置/字节；另计算默认 marshal 摘要与原记录比较。
它也直接记录 CodeType 的 == 比较结果。
程序显式的文件写入是独占创建一个小报告；没有选择新 factory、改安装函数、
调用数学回调、DN、Jacobian 构造器或 BVP。

程序未在内部强制四个键集合的完整性；但本次固定 reproduction 中恰为
prepare_sys、construct_global_jac、compute_jac_indices、solve_bvp，
本审已经实际核对。这是对这份固定输入的诊断审查，不能把程序直接视为
接受任意外来 reproduction 的通用成功门。

## 3. 真实独立重跑及精确结果

审者先核诊断源码的冻结 SHA，再以绑定 launch 的实际解释器执行同一源码，
只把输出换到自己的新路径：
[独立 marshal 重跑报告](2026-11-10-78718-audit-runtime-marshal-replay-01.json)。

工具回执 017712，自然 exit 0，0 solver calls、0 callback calls。
报告 14150 B，SHA256
a23f037cf90618abcc5549802371f7fb450ed7fe5fe68ed358f7b812fb906db4。
本次报告与原作者诊断**完整字节相同**，不是复制原报告；
实际执行后在终端重新比较两文件，且核了打印摘要与新文件本身的哈希一致。

四个 fresh imported 默认摘要都匹配原记录；
四个 CodeType 的 == 与十八字段递归谓词都为真；
marshal v0 对四个函数全部等字节。

| 原函数 | 原诊断/独立重跑的 v4 等字节 | 该上下文的首差位置 |
| --- | --- | --- |
| prepare_sys | 否 | 162 |
| construct_global_jac | 否 | 1156 |
| compute_jac_indices | 否 | 1080 |
| solve_bvp | 是 | 无 |

前三项的首差字节分别为 250/122、225/97、250/122。
这只是实际观察到的编码差别，不由这些数值单独证明其全部内部成因。
本审不声称已经审计此运行版本的 CPython C 实现，更不声称任何
marshal 版本对所有等值 CodeType 都规范化。

Python 3.12 官方 marshal 文档把它定位为内部代码序列化格式，并说明
版本会引入引用/递归等表示特性，没有提供“相等代码对象必有唯一字节”的
本次所需保证：
[官方 marshal 文档](https://docs.python.org/3.12/library/marshal.html)。
该文档仅作格式用途背景；本次具体结论由上述固定环境中的真实执行支付。

## 4. 旧谓词为什么仍必须按原样拒绝

已读取旧 auditor 的 _compiled_runtime_record 及其调用环境。
该谓词对记录模式、模块、限定名、实际源路径和首行号核验后，
从固定源文本编译并取得指定代码对象，最后原样要求：

记录中的 code_sha256 等于 SHA256(marshal.dumps(重编译代码对象))。

旧函数没有采用本诊断的 deep_equal，更没有接受“字段相等则忽略摘要”。
完整 CSC 身份门还要核三个存储 helper、两个选中 factory 函数、
原回调/工厂 provenance、选中的 Newton 身份及恢复过程；
这些均不能由四个原函数诊断替代。

原作者已保存一次真实拒绝记录
[numerical-run02-runtime-audit-rejection-01.json](2026-11-10-78718-numerical-run02-runtime-audit-rejection-01.json)，
901 B，SHA256
f8fe0851ffc75d529fcb08c45c153aaf0da9266cff7ab9fc50ce4d22fedac6c7。
记录明确是原代码摘要门抛 ValueError，完整通过报告未写出。
它列出的先前局部门完成项，不等于整体出口通过；
主 solver 的失败与这个事后运行身份拒绝也不能混为同一个原因。

为核实当前旧谓词而非仅作静态推断，本审另保存并实际运行
[最小旧谓词探针](2026-11-10-78718-audit-original-runtime-gate-probe.py)，
4067 B，SHA256
77823494569ed99ba70e8dd0e2d5ab8611fb5e9e0add8dab7a20436a2fd5ae90。

它只导入旧定义并分别调用四个原函数记录的 _compiled_runtime_record；
不调用整个 first/final auditor，不执行 validate_inputs 之后的数学
关闭流程，也不构造 candidate、factory、Jacobian 或 solver。
它先核输入 launch 绑定和实际解释器，并对下列四个旧源在执行前后
分别核同一 SHA256：

| 旧文件 | SHA256 |
| --- | --- |
| db6f-prefix-audit-spectral-true-m14-direct-csc.py | b6222f3394c53eebd8409c922ed2e009de85b4bcdbfa5a6e8c8d57b2294967e0 |
| db6f-prefix-spectral-true-m14-direct-csc.py | b6fd772b5f44819186fc7e31af370ffa199bfa5c9b14a2722b36345bcf26cd24 |
| db6f-prefix-direct-csc-entry-gates.py | d110a15669612ae75207d98b46b8ee31c41d5f98dc8a9b693a06a4cbc399606b |
| db6f-prefix-spectral-affine-replay.py | ad219dbab80278670665ac3cb5401cb55daf33834cea8495dd16bf1c1396e4bd |

工具回执 0c0d55，探针自身自然 exit 0。
这仅表示诊断运行正常，**不是旧门 exit 0 或候选通过**。
四次实际旧谓词调用均抛出 ValueError：
Runtime function code digest differs from pinned source。

独立记录为
[旧谓词实际探针报告](2026-11-10-78718-audit-original-runtime-gate-probe.json)，
2290 B，SHA256
bcdc6db3f79cad468b1bfd5b7d1403204a0c73c82121829708f7202b67796417。
旧源执行前后均保持字节身份，0 solver calls、0 callback calls。

## 5. 两个不同上下文不能合并成一项更强结论

第 3 节中 solve_bvp 的两个 v4 字节相同；
第 4 节中旧谓词对其记录摘要仍拒绝。
这两件事比较的编译对象持有方式、调用栈和当前运行对象环境不同。
因此必须分别记录，不能把前者解释为后者应当接受，更不能把四项旧拒绝
改写成“只有三项失败”。

本次实测足以证明这两种特定代码比较上下文给出上述不同字节结果，
并说明旧原始序列化摘要门依然拒绝。
它不证明代码的全部运行语义、闭包值、全局绑定、选中函数、物理方程、
数值残差或数学终门已经审完；也不证明字节差异只有某一个内部引用位的原因。

同样，v0 在这四对对象上相同，不等于可以未经审查把旧门切到 v0。
字段谓词相等也不等于可以直接忽略原记录，或从固定源重建一份新身份
冒称其在原 run02 运行时被实际捕获。

## 6. 对下一独审的交接范围

本次允许采用的中间结论是：冻结只读诊断的现场观测可独立重现，
旧身份谓词在当前独立调用中仍全部拒绝，run02 失败状态不变。
没有改写旧 gate、原 reproduction、原 launch、原 factory 或原 driver。

后续另名程序应作为新的明确身份单独审查；在其作者冻结源码与变更账本前，
本审没有猜审或预先接受任何尚未完成部分。
新实现即使解决了该身份比较，也仍必须通过自己声明的完整输入、运行身份
和出口门，并且不能把失败 run02 祖先的局部检查当成其新数学成功。

审者继续保持未参与候选优化的角色。没有选择种子或节点预算，
没有运行数学候选，也没有提前消耗最终原种子全链独跑任务。
