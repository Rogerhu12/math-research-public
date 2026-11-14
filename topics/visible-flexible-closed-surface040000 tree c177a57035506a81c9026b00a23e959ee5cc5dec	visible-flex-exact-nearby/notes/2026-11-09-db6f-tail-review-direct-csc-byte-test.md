# 完整静态独审：direct CSC v2 的原函数字节与别名副作用测试

独立审查人：tail_review_continued_2；原冻结批次日期：2026-11-09。
本审查已读完整测试源码、完整方法说明、未执行运行清单和出版清单。
没有参与这份测试的具体实现；没有修改作者源码或旧文件。

**接受这份测试和计划的静态范围，没有发现阻断性源码问题。**
它以实际官方原函数作参照，原版和新版使用相同初始字节与别名关系的独立可写输入，
比较完整 CSC 三数组和所有调用者可见副作用。
**Python、NumPy/SciPy 导入、factory、矩阵构造、测试主函数和数值求解均尚未实际执行。**
本报告不把源码接受或文本哈希通过标成15场景运行通过。

## 1. 固定文件与完整阅读范围

出版清单：
[de107df51fad5fd41598428f7f04f67863f647a7](https://github.com/Rogerhu12/math-research/blob/de107df51fad5fd41598428f7f04f67863f647a7/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-direct-csc-byte-test-publication.json)，
blob 8249d41a258fa96c81150ca01d5db4ce87403fd6，1,899 B，
SHA-256 89b843c32dd7cb9184aac616aaeca49949c9526a46c5e43be34cb0f36868d019。

该清单绑定以下3件，合39,192 B：

| 文件 | 固定提交 | Git blob | 字节 |
|---|---|---|---:|
| scripts/db6f-prefix-test-direct-csc-bytes.py | 4fb8b855e7df8ef5c68c797f13da70640900bbfe | abb5f27a8926652933c827d85c0bbcea54fe8601 | 26045 |
| notes/2026-11-09-db6f-prefix-direct-csc-byte-test-plan.md | e38667630145d094523e64abcd3dcb4f39cdd926 | 29320562def56ab47b25736ad308b3ac4073e343 | 7772 |
| notes/2026-11-09-db6f-prefix-direct-csc-byte-test-planned-run.json | 70305f7e40c3416a182da71b8ace812bd8a860f7 | bd8b0b0664df1f710f8ef85caf32a73c13bed90b | 5375 |

按表顺序的完整 SHA-256：
- 197da92ec9ca8768c1b5a876aeed2b5164056fa7e3a3b3d790cd9eb626ee5bbc。
- a6431c443165cbb41b80f374c1bd4cac46690cc456e5bb9e0b136de5d7af54ba。
- f205bbefdee7fd8d1e875b677ab3d0b4b86ae3dabc648341e278ae248babe944。

测试的唯一目标是 foundation v2：
scripts/db6f-prefix-direct-csc-foundation-v2.py，
固定提交5b7a715833357675cbe5d9944ce54a165997473a，
blob71f91271133dacd85e4d8d63a7ec3b757222d453，17,550 B，
SHA-256 8e2bb061ef1fee94672601132cedb8ca7565d4006a327474f039f501e5f516cf。
其完整静态独审已固定在
[398944aa07f18b8d44e614aa86cfe1bea14454ec](https://github.com/Rogerhu12/math-research/blob/398944aa07f18b8d44e614aa86cfe1bea14454ec/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-tail-review-direct-csc-foundation-v2.md)，
SHA-256 0cc7ed169f1c7606e86e6c50107afe70e51e84a28acc5be3f7aeacbdaed9e90b。

本次另外读取官方 SciPy v1.17.0 的
[scipy/sparse/sparsetools/csr.h](https://github.com/scipy/scipy/blob/v1.17.0/scipy/sparse/sparsetools/csr.h)，
核其完整文本 SHA-256 2064bcb579658d0a94ce04e8f4955f307f985a63ec15db293f2cd6018a2b0e7a，
blob997ffdde6b34c88ca3329adf7ee2d29757f94f8c，50,275 B，
并逐项读了相关 csr_sum_duplicates 函数。
其余六份官方源和原 construct、indices 的数学结构沿用上述已完成的完整 foundation 审查，
没有把本次文本读取冒充这些库的实际加载。

## 2. 参照是原调用路径，没有用新枚举器生成 expected

测试先核官方 _bvp.py 完整文件 SHA：
59afffb3607b272ae77f346d86428e43eca359fe90f2605da60a9571e60970d2。
随后从该完整源编译 code object，
核实际被调用的 construct_global_jac 与 compute_jac_indices：

- 是真正的 Python FunctionType；
- code object 等于固定源的同名函数代码；
- globals 正是该实际模块命名空间；
- defaults、kwdefaults 和 closure 都符合原始无附加状态身份。

原矩阵的行列索引直接由该实际原 compute_jac_indices 产生，
矩阵直接由该实际原 construct_global_jac 产生。
测试没有把新 column_segments 或其另一个重写版当作原版 expected。

_bvp 的 np、coo_matrix、csc_matrix 也核为实际导入引用。
新 make_functions 则继续执行 foundation v2 自己的完整源与实际 callback/CSC 方法门。
因此磁盘文件哈希与实际函数来源没有被混为一件事。

这仍是计划执行时的检查设计；本次没有调用 compile、factory 或 Python 函数。
实际运行环境能否通过所有来源门仍未支付。

## 3. 输入 Seed、独立根缓冲与相同别名关系

Seed 为每个输入给 shape、根缓冲标识、元素偏移及元素步长。
初始数值由固定 dyadic 配方产生，无 RNG、无主研究文件、无存储的数值 fixture。
h 单独设为正常正 float64，其他输入为指定常见实/复浮点普通 ndarray。

每个视图先用小整数地址枚举核：
元素数量正确、内部没有自重叠、所有地址在所指根缓冲内。
根缓冲随后设为只读。

instantiate 对每个完整根缓冲作一次新 copy，
再用同一 View 描述构造 numpy.ndarray。
于是每个运行内部的别名关系保持，
而两个运行使用互不共享、也不共享只读 Seed 的可写根缓冲。
independent_cohorts 还用 np.shares_memory 实际核上述独立性。

调用前的 snapshot 包含：
所有根缓冲和所有输入视图的 shape、strides、dtype、C序字节 SHA，
以及全部输入两两相交内存的 alias_pairs。
两套快照必须完全相同。

因此新版不会接收原版已经原地更新过的输入。
仅复制各个视图、破坏别名关系的常见测试错误在这里没有发生。
根缓冲完整字节的比较还覆盖视图之外的间隙，
而各个视图的比较保留其逻辑元素与步长信息。

## 4. 四类别名地址和读取时序

以下地址均以共享根中的元素序号计；已按源码逐项手核。
同一类型的复数实例使用同样布局。

| 模式 | 共享根大小 | 中点参数视图地址 | D / E / F 的关键关系 |
|---|---:|---|---|
| full_boundary | 6 | 0至5 | D和E都覆盖0至5；两边界与中点完全共享 |
| partial_boundary_and_F | 20 | 4至11 | D为0至7，E为8至15，F为6至13 |
| negative_and_fortran | 12 | 5,4,3,8,7,6 | D为1,0,3,2,5,4；E为6,9,7,10,8,11；F为3,4,5 |
| node_and_boundary | 12 | 2至7 | 参数节点为0至7；D为2至7，E为5至10，F为9至11 |

所有单视图内部地址均互异且不越界。
第三类真的具有中点负步长、D负列步长和E的Fortran布局；
不是仅给场景起了这些名字。
第四类使参数节点和中点共享根，
能够暴露中点原地更新后再次读取节点数组时的副作用差异。

原版和新版各执行一次；
调用前另存 D/E 快照，
调用后要求中点确实发生变化，且每个别名场景的调用者 D、E 也确实变化。
这使测试具有区分力，不会用一次零更新轻易通过“读取时序一致”。

对这些非零别名场景，测试还从原参照矩阵取真正边界块，
验证其值来自更新前 D/E。
该辅助检查没有用新枚举器；
并且只用于全部相关边界类型同为 float64 或 complex128 的场景，
所以一次 astype(final dtype) 不会漏掉混合类型时两次 promotion 的语义。

F 与参数节点的更新后读取不靠上述边界快照辅助测试覆盖：
完整原/新 CSC 字节和完整根缓冲/输入视图副作用都会一并比较。
基础模块 v2 在原首次 hstack 位置复制 D/E 的修订因此得到针对性的真实测试设计。
v1 的延后读取缺口没有被重新引入目标身份。

## 5. 15个场景的范围与有效形状

源码固定15个场景，没有命令行选项可跳过其中某一场景：

| ID | 主要覆盖 |
|---|---|
| real64_normal | 正常实数与可观测中点更新 |
| real64_signed_zero | 显式结构零及实负零 |
| float32_k0_m2 | 无参数、两个节点、float32存储 |
| complex64_k0 | 无参数、complex64存储 |
| complex128_signed_zero | 复数实部与虚部负零 |
| float32_parameter_promotes_to_float64 | h与参数运算导致的最终提升 |
| real32_boundary64_parameter_complex128 | 两次 hstack 的不同 dtype |
| complex64_mixed_boundary_parameter128 | 复数主块与混合边界/参数 |
| mixed_signed_zero | 混合实复转换及符号位 |
| full_boundary_alias_real64 | 完全共享边界的实数版本 |
| partial_boundary_F_alias_real64 | 部分重叠并含F |
| negative_Fortran_alias_real64 | 负步长及Fortran布局 |
| full_boundary_alias_complex128 | 完全共享边界的复数版本 |
| node_and_boundary_alias_real64 | 参数节点/中点/边界共同根 |
| W14_dimensions_two_nodes | n=43、m=2、k=14的小模板 |

各输入的形状符合原 construct 契约：
h为m-1，df_dy为n×n×m，df_dy_middle为n×n×(m-1)，
参数导数和边界导数的n+k行也正确。
k=0时参数对象为None，原分支不使用它们。

预算N=nm+k<=128、L=(2n+k)N<=20000只限制这个测试。
W14两节点案例为N=100、L=10000，
没有从真实大网格截取数组，也不是改写主BVP的max_nodes或其他数学门。

混合类型的中点目标使用能接受相应原地更新的常见实/复类型；
测试没有故意让复数增量写进实数组而把应有异常错当作实现失败。
float32无参数的A/B及边界保持原存储类型；
带参数时原h表达式导致更高精度参数块，
最终dtype由原函数结果先实际核对，再与新版字节相等。

这些是有限个有效普通 ndarray 场景。
本报告不据此宣称所有NumPy子类、对象dtype、长双精度平台、
内部自重叠视图、非法回调输入或分配失败时序均等价。

## 6. 完整 CSC 与副作用比较的强度

对每个场景，compare_csc 检查：
格式为CSC、完整N×N形状、显式存储L个位置，
sorted和canonical标志为真。
data、indices、indptr分别比较dtype对象与dtype.str、
shape、strides和全部原始C序字节。

这比矩阵稠密化后数值接近更强：
索引dtype、明确保留的结构零、精度提升和符号零都会被检查。
主要对照没有稠密化，也没有浮点容差。

正负零由实部/虚部分别赋值生成，
避开使用 a+1j*b 形成复数时可能改变符号位的额外运算。
完整原始字节比较之外还记录并比较零数量、
实部负零数和复数虚部负零数。
要求符号零的场景必须真的含有所需负零。

纯零输入的非零输出只应来自各间隔A/B的±I，
测试核数量2n(m-1)。
其他条目继续明确存储，不调用eliminate_zeros。
已读官方 csr_sum_duplicates：先令 x=Ax[jj]，
只有存在相同列索引的后续条目才执行加法；
无重复时直接保存x。该函数源码也明确保留显式零。
这支持测试意图，但真正运行的符号位仍须以未来原始字节结果为准。

主调用后，两个运行的全部根缓冲和全部输入视图快照必须完全一致，
只读Seed摘要也必须不变。
因此不仅比较df_dp_middle本身，
也比较所有共享视图和根中未被视图覆盖区域的调用者可见效果。
D/E辅助稠密边界检查只出现在非零别名案例，
不拿稠密化结果判断符号零案例。

## 7. 运行边界、对象身份与失败记录

execute 仅在显式运行main时导入NumPy/SciPy。
它记录factory前原prepare_sys、construct、indices、solve_newton、
四个callback以及np/COO/CSC引用；
factory后和每个成功场景后必须仍是原对象。
没有install、monkeypatch或SuperLU调用。

临时foundation模块名须未占用；
在finally中移除临时sys.modules项并恢复dont_write_bytecode原值。
即使场景失败，也会执行这一清理。
这项临时导入只是未来测试自身的函数模块加载，不替换原数学入口。

attempt和completed计数分别在调用前后更新；
只有一个场景全部核完才追加到cases。
失败报告保留真实stage、异常类型/文字和已完成计数。
因此原构造成功、新构造失败、或构造都成功但字节不符，
不会被压成一个虚假的完整通过记录。

顶层PASS状态只在固定15场景循环全部完成后设置。
script_return_code只是脚本打算返回的码，
必须由真实启动工具另行观察自然退出。
输出存在、内部返回字段或一个预填的状态都不能代替实际外部exit。

factory_provenance保持比较前的快照，其中pending字段不被后改。
顶层测试报告另记后续结果，并明确该快照发生于比较前。
这两个时间身份并不矛盾；也不允许在运行尚未发生时填充顶层PASS。

## 8. 输出和计划的准确范围

main在科学库导入前拒绝已有输出，
最后以独占创建模式写新小JSON。
报告只含源码/版本、哈希、形状、dtype、计数和场景元数据，
不输出数值数组。UTF-8达到100000 B即拒绝，不截断假装完整报告。

运行清单中的工作目录、绝对路径和输出名都是恢复后的待核模板。
它明确标注实际输出未占用尚未核、Python/factory/matrices全false、
外部退出为null。
这与当前环境不可用的事实一致，不是实际launch或通过凭据。

方法、清单和源码所列原源SHA、foundation v2 SHA、15案例数及原/新各15调用
全部相互一致。
“测试尺度”没有被搬成新的主问题完成门；
即使它将来通过，也不能据此关闭主G5或批准未审的完整入口。

## 9. 本次实际执行的只有纯文本绑定检查

独立文本检查身份：
tail-review-direct-csc-byte-test-static-binding-01。

clock工具实际返回2026-11-09 23:57:37 UTC。
functions.exec 在JavaScript/V8中读取已取回的小文本，
计算完整UTF-8字节数与SHA-256，
核出版清单的3件文件与固定回读全文完全匹配，
并核未执行计划的15案例/15+15调用数、目标v2身份和false/null执行字段。
全部一致，functions.exec实际正常完成。

这不是Python AST检查、原/新函数编译或矩阵运行。
本次没有执行测试源码、foundation factory、SciPy构造器、
任何NumPy数组算术、SuperLU、线性求解、BVP/DN/RK或主研究数据读取。
不存在可报告的Python工具exit0或15场景实际PASS。

## 10. 后续真正通过还需什么

静态全文审查可以接受这份测试设计与其未执行清单。
环境恢复后仍须先核真实源码身份、实际路径及新输出未占用，
实际执行原/新小矩阵和完整别名副作用比较，
独立观察工具自然退出，再封报告完整哈希和15场景身份。
前一份纯源码/整数checker也仍需要其自己的真实执行。

本报告不代付这些尚未发生的动作，
不代付真实W14 callback/入口安装/主轨迹，
不将有限合成测试外推为所有可能输入的机器字节定理，
也不更改foundation v2、旧LU入口、数学算法或任何主终门。
