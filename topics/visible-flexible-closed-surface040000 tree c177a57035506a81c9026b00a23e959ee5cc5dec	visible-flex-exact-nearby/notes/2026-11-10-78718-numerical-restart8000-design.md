# 新身份 M14/W14 restart8000：设计与未付状态

日期：2026-11-10。会话：Astra-visible-flex-78718bd0。
本稿冻结设计，后续源码身份/实际检查另列；在完整审查与 root 实际启动前不表示准备已通过。

## 固定祖先与唯一数值政策变更

run02 的退出2及 weighted RMS 超容差保持失败，不重写旧 launch、gate 或报告。
原 97 绑定的 affine reference 与 run02 的 direct-CSC 祖先仍由其原
`h.validate_inputs` / `validate_inputs` 验证。新入口另外绑定 run02 的失败 CP、
全部四块 quintic、其自有 audited tail_0003、root 实际非零退出观察。
暖启动只把同物理问题的已保存值当初猜，不把失败状态改为成功。

原 preserve-restart 与原 W14/SciPy 的只读四扫实际给下一初猜 6344 节点，
255 个区间各需1点，建议网格6599。root 已接受新数值预算 max_nodes=8000，
其余 M14/N512、tol=2e−9、bc_tol=1e−8、physical_bc_tol=2e−11、
原固定 g 与所有 profile/chart/port/时间范围、tail depth12/P8/S32、
全部原 nonlinear outer/末包/后端连续认证门保持。
主运行继续使用 6 GiB DATA 与 Node1536；预算不是收敛或内存保证。

## 新文件与变更边界

新 driver/preparer/auditor 以 78718 身份命名，冻结旧对应源码和逐项变更账本。
旧数值源码、保存/重启函数、tail 客户端、Newton、CSC foundation/selector、
原生产链均不修改。新原生主循环仍调用原 `db6f-prefix-coupled.py::main` 与
`solve_with_actual_tail`；声明 argv 仅改独立输出、尾配置 I/O、失败 CP restart、max_nodes。
新 config 除 I/O 字段外必须逐字同原 config，initialCheckpoint 为真实 tail_0003。

新纯 preparer 不构造 candidate、不执行 restart/RHS/矩阵/solver/tail，
仅验证冻结输入/closed failure evidence、原 CSC 小检查回执与新 canonical 检查，再写小元数据。
driver 首次真实 BVP 前记录所有原回调、原 Newton 到 release-LU 的明确选择、
原 direct-CSC 选择。每次 BVP 前后都核对，结束仍恢复原 prepare_sys。
新输出审计沿用原成功的 CP/outer/physical residual/末包/PP/全部参数与状态门，
仅节点上限改为新声明的8000。final 仍强制 root 的真实自然 exit0 及逐文件绑定。

## Canonical CodeType 身份

run02 的 marshal v4 差异属于同源 code 的表示问题；旧 gate 不改，
v0 在四个函数中的一致性也不当作一般定理。
新 stdlib 小模块为 live CodeType 的全部构造语义字段给严格的类型化编码：
参数计数、locals/stack/flags、co_code、递归 co_consts、names/varnames、
filename/name/qualname/firstlineno、linetable/exceptiontable、freevars/cellvars，
并保留派生 co_lnotab。常量区分 None/Ellipsis/bool/int/float/complex/str/bytes/
tuple/frozenset/嵌套 code；float/complex 使用 IEEE 原位字节，未知类型拒绝。
frozenset 按其成员的完整编码排序；不记录对象引用共享或 intern 布局。

每个新 canonical 记录同时绑定实际源码文件 SHA、模块/qualname/filename/行号、
原 raw marshal SHA 和 canonical 摘要。运行中从实际 live 函数捕获；出口从绑定
源码用同 filename、dont_inherit=True 重编译取得目标 code，再核 canonical。
原 raw 记录保留，与 live raw 摘要对应；不要求不可规范化的 raw 字节等于重编译 raw。
原 selector 对 globals/defaults/闭包别名/后端对象身份的检查全部继续执行。

小检查必须实际显示同源编译/导入一致，以及源码、字节码、常量、参数/变量布局、
filename/name/qualname、行表/异常表等实质改变会拒绝。包含 NaN payload/±0 与
嵌套 code 的位值/类型检查；不调用数学 RHS/BVP/DN/Jacobian 或新 CSC 矩阵。
源码、精确差分、检查配方与真实回执交给 root 及未参与优化者全文独审。

## 未付门

本稿本身未证明新实现正确、未通过新 preparer、未启动新求解。
下一真实入口由 root 在上述来源和出口门审清后启动。
若真实成功，仍需本次自有最后尾包和完整新图连续认证/原2e−9终门/网格，
最后由未参与优化者从原始种子完整独跑；restart成功不替代该最终独跑。
