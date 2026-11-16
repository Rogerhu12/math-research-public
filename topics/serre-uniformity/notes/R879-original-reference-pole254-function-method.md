# R879 — 原参考单极函数的执行契约

日期：2026-11-16。数学依据为 results/R879-original-reference-pole254-pencil-from-completed-syzygies.md，
SHA256 5f0988a85734f2c1e311dd6f55d0caa111011a8dc2ee119a20114effe7226055。
本次仅将已完成的 R872 配对核与局部系数用于一个新的563×418系统；成功时给原
O_Y(254P0) 的源绑定函数 v0 和铅笔 (1,v0)。不计算九个域范数或 Hecke 活跃支持。

## 1. 已完成输入和准确系数的含义

唯一数学 producer 是已完成 R872 run43830071469/source
a07453ec81e832b0aeef99bded2efaa763adaf13。原 core 为
0e5897512a2f45baaed9cd1b6b2badcb6bf6ee2b100fcd45db871ad9f6db1874；
原最终证书为17961字节/b2837667ae100ef8c7f27494eb447201e3b6204da553d337d78e9a163d90c0e5，
完整 manifest 为48387字节/5001e5be47484c649a28afb82c89cf95995f0a3a0d05498173bbb680451cbb80。

本次保持原素点1000000753、原 zeta 根549966761、正常基次数
(0,1^144,2^127)，以及正常行在外、z次幂在内的 V2/V3 顺序。原82尺度不再乘除。

输入 paired_kernel 的两个字段
V3_kernel_basis_mod_prime 与 paired_u_multiplier_coordinates_mod_prime 是690×418的 S/T。
它们的准确特征零意义是同一文件 exact_kernel_definition 给出的完整 unit-solve 基，
满足原全部 u T+b S=0。原模矩阵是这个准确基的合法约化；不得将矩阵条目直接写成准确
特征零系数。

输入 V2_jets 是原273×418局部矩阵，只读取其前19行。anchor_u 给原 u 的418坐标、
准确源和已验证的第272阶单位。其余小输入绑定原点、局部参数、146核、b、962铅笔
证书与固定除子。旧 stage 均保持旧配置、原文件名、字节和SHA。

标准库 wrapper 只用 Range 读取 manifest、metadata、最终证书和所选小 stage，
不读取原122MB输入包。原 source-inventory 与 input-receipt 保留，以区分已读原件和
未重新读取的已认证外部 unit-solve 依赖。此小包不声称已经再次展开原 W 或旧准确逆。

## 2. 新系统及一次单位解

从原 V3 顺序逐正常行抽出最高幂 3-epsilon_i 的行，依次形成272条 S 条件、272条 T 条件。
其余418行按原 V2 顺序抽为 S_low。只新计算 J[0:19] S_low，加入为最后19行。
右端前562项零、最后一项1。保存完整563×418矩阵与所有行号，不另做旧乘法。

原证明给矩阵准确秩291和系统相容。按 transpose 的左至右 pivot 选择291行，再在
该291×418矩阵选择原顺序291列。联合单位矩阵消元给所选291方块的模逆，
准确核两侧乘回；保非零行列式。其余127坐标置零，仅求这一个非齐次解。
实际仍将解乘回原全部563行。若当前约化未达291秩，保存实际秩和诚实失败终点；
若超过理论上界，直接报源/实现不符，不伪称合法新结果。

准确特征零解是原所选方块逆作用原右端的 unit-solve 表达式。
几何准确秩及已证明相容性保证此表达式满足全部原行；有限域乘回另外检查实现。
不需要重新解原146或418空间，不构造参考128基。

## 3. 输出函数与原框架

新解 c 给 f=S_low c、g=T_low c。只新做这两次矩阵向量乘法，保存原 V2 坐标及
每正常行的次数不超过2-epsilon_i的三层系数。继承准确原全局关系 u g+b f=0；
不重新展开两个 V4/V5 乘积。

输出 v0=(f/tau^2)/(u/tau^2)=f/u。全局配对关系排除所有非P0极点；
分子第0至17阶为零、第18阶为1，分母恰第272阶，故原极除子恰254P0。
(1,v0) 因而全局生成同一个参考 O_Y(254P0)。

原 t=a^3 框架单位保为 leading(t/x)^254/U272，尚不展开，不设置为1。
单独 v0 的 Q 定义性不声明；它是原 K 上的准确函数和参考线丛的有效生成元。
K 上生成不能改变原 Hecke 对应或 -3 下降。

## 4. 配置、断点与完成字段

RESULT 为 R879-original-reference-pole254-pencil；
FINAL 为 p41-original-reference-pole254-pencil-certificate.json。
核心 CLI 是 --config --output --budget-minutes。
所有工作阶段在根目录 R879-reference-*.json.gz，无子目录或新外部大数组。

数学 tag 绑定新 core SHA、本文和三篇证明、R872实际证书/完整manifest/所选文件指纹、
九项 inputs、原素点和完整策略。运行预算、artifact运输位置、rules读取记录不进入数学身份。
数学 core 不导入或调用旧 core；wrapper 只导入哈希绑定的标准库 R824 Range helper。

四个主要阶段为 source-audit、system、unit-solution、function-and-pencil。
每个完整阶段先原子落盘，再推进 current。stage_manifest 以实际完整清单哈希命名；
current.complete 为 false，不进入完整数学清单。旧 incomplete FINAL 不限制后来完整
current；true FINAL 的所有引用必须逐一吻合。原同 core/tag 续算复用每个完成阶段。

标准库 wrapper 检查真实 run/core/manifest 与选择清单，保最小一日输入carrier。
外部超时为预算加900秒，先SIGTERM、短宽限后kill，始终写真实退出码并保已成产物。
缺 core receipt 只在非成功且 run.core_receipt_sha256=null 时诚实接受，不补造回执。

成功要求291单位子式、全部563行、原第272阶单位和准确全局来源均通过。
最终 actual_reference_pole254_function_certified 与
actual_reference_basepoint_free_pencil_certified 才可为 true。
characteristic_zero_reference_coefficients_expanded、
reference_complete_128_basis_computed、original_t_frame_scalar_expanded、
five_original_Lj_RR128_computed、nine_field_norms_or_Hecke_action_computed、
active_eta_support_or_height_computed 始终为 false。

所有新算术只在公开 Actions；本地只允许文本/AST/纯IO。机器矩阵、向量、回执仅一日
artifact，Git只保源码、参数、证明和简明实际结果登记。
