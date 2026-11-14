# Direct CSC 原函数/v2 小合成字节对照：未执行的运行说明

日期：2026-11-09。作者会话：db6f / coupled_prefix。

## 当前状态

本批新增 scripts/db6f-prefix-test-direct-csc-bytes.py，SHA256 197da92ec9ca8768c1b5a876aeed2b5164056fa7e3a3b3d790cd9eb626ee5bbc，26045 字节。已按新路径保存，并从固定 commit 4fb8b855e7df8ef5c68c797f13da70640900bbfe 完整回读。**脚本尚未执行，未产生任何通过报告。**

测试目标仅为已静态独审的 foundation v2，SHA256 8e2bb061ef1fee94672601132cedb8ca7565d4006a327474f039f501e5f516cf。测试不修改该模块，不安装 prepare_sys，不调用主曲面的任何输入、对象、BVP、DN 或 RK；也不调用 SuperLU 或线性求解。它的成功不能代付完整入口、真实候选或 G5。

环境仍不可用。本批只有源码与计划的保存／回读，不做执行器探针、Python 导入、factory 或矩阵计算。

## 参照函数与独立输入

参照矩阵直接由固定官方原 construct_global_jac 生成，其 i_jac/j_jac 也来自原 compute_jac_indices。测试不使用新 column_segments 或另一份新枚举算法来生成 expected。

脚本先核原 _bvp.py 的完整 SHA256 59afffb3607b272ae77f346d86428e43eca359fe90f2605da60a9571e60970d2，并用该源文件编译得到的 code object 核两条实际调用的原函数、globals、defaults 和 closure。新的 factory 自己继续核六份官方模块、原 callback 和 CSC 构造方法来源。原 NumPy、COO/CSC 类的运行引用也核同。

每个输入由固定的小 dyadic 配方生成，不读任何数据文件，不依赖 RNG。每个 Seed 包含一组只读一维根缓冲及输入视图的形状、元素偏移和元素步长。测试先核各视图没有内部地址重叠、没有越界，再分别复制每个完整根缓冲，以同一视图描述重建 original 与 direct 两套可写输入。两次运行的任意根缓冲互不共享，且都不共享只读 Seed。

两次调用前比较全部根和视图的 shape、strides、dtype、字节 SHA，以及 np.shares_memory 给出的完整别名关系；调用后再次比较所有根与所有输入视图，最后核只读 Seed 的完整摘要未变。原函数和 v2 各调用一次。不会把原函数已改写的数组继续喂给新版。

h 始终为正常正 float64。其他输入都是有效形状的普通实／复 ndarray；不扩展到对象 dtype、第三方数组子类、视图内部地址重叠或任意非法回调行为。异常／分配失败的时序不要求相同。

## 15 个固定的小合成场景

| 场景 | 目的 |
|---|---|
| real64_normal | 普通实数及一次可观测中点更新 |
| real64_signed_zero | 显式结构零和负实零 |
| float32_k0_m2 | 无参数、两端点、float32 最终存储 |
| complex64_k0 | 无参数、complex64 最终存储 |
| complex128_signed_zero | 复数实／虚分量的符号零 |
| float32_parameter_promotes_to_float64 | 原参数表达式与 h 导致的最终 dtype 提升 |
| real32_boundary64_parameter_complex128 | 第一次与第二次 hstack 的不同 dtype |
| complex64_mixed_boundary_parameter128 | 复数 A/B、混合边界及更高精度参数 |
| mixed_signed_zero | 实／复转换同时保留符号零 |
| full_boundary_alias_real64 | D/E 与参数中点完全共享底层区域 |
| partial_boundary_F_alias_real64 | D/E 部分重叠；F 也读更新后的共享区域 |
| negative_Fortran_alias_real64 | 中点负步长、D 负列步长及 E 的 Fortran 布局 |
| full_boundary_alias_complex128 | 同一别名读取时序的复数场景 |
| node_and_boundary_alias_real64 | 参数节点、中点和边界共享根缓冲 |
| W14_dimensions_two_nodes | 43 状态／14 参数，使用 2 个节点的小矩阵 |

固定预算限制 N≤128、显式位置数 L≤20000；当前最大实际模板是 N=100、L=10000。这只是测试规模限制，不是主数学或真实 BVP 的新门槛。没有从主数据缩减或截取任何矩阵。

混合 dtype 场景只宣称上述普通 ndarray 和指定常见实／复类型；不外推到所有平台长双精度、非法转换或特殊数组子类。真正的最终 dtype 由原函数结果给出，并同时核其符合该固定场景声明。

## 实际恢复后要比较什么

每个场景中，以原函数为参照逐项核：

1. CSC 类型、完整 N×N 形状以及显式位置数 L，包含零值位置；
2. data、indices、indptr 的 dtype、dtype.str、shape、strides 和全部原始字节；
3. sorted 与 canonical 标志；
4. 显式零数量、实部负零以及复数虚部负零；
5. 所有输入视图及每个根缓冲的调用后完整字节，覆盖 df_dp_middle 的原地修改和共享视图的副作用；
6. 对规定的非零参数场景，确认 df_dp_middle 确实改变，避免无变化输入使“更新一次”的比较失去区分力；
7. 别名场景中，确认调用者看到的 D/E 确实发生变化；再从原参照矩阵取边界块，核它仍对应更新前 D/E 快照。该辅助检查只对本测试相同 float64/complex128 别名类型使用，不替代两次 dtype 提升的整个矩阵对照。

纯零场景另外核只有 A/B 的 ±I 对角位置非零。原 sparse conversion 不调用 eliminate_zeros；官方 csr_sum_duplicates 对无重复条目直接保存该条目的值，只有确有重复才相加。这是源码范围说明，实际符号位仍以测试结果为准。固定官方 csr.h 文本 SHA256 为 2064bcb579658d0a94ce04e8f4955f307f985a63ec15db293f2cd6018a2b0e7a。

原 prepare_sys、construct_global_jac、compute_jac_indices、solve_newton、原四个 callback，以及原 NumPy/COO/CSC 全局引用在 factory 前后和每个场景后都核对象身份不变。没有 install 或 monkeypatch。

## 运行清单与真实证据

另存的 planned-run JSON 是未执行计划，不是实际 launch 或批准记录。环境恢复后，owner 应先核实际路径、源码 SHA、输出未占用及独立全文审查；然后才可执行：

    python3 /ABS/REPO/topics/visible-flexible-closed-surface/scripts/db6f-prefix-test-direct-csc-bytes.py \
      --foundation /ABS/REPO/topics/visible-flexible-closed-surface/scripts/db6f-prefix-direct-csc-foundation-v2.py \
      --out /ABS/REPO/topics/visible-flexible-closed-surface/notes/NEW-direct-csc-byte-test.json

前一纯源码／整数 checker 也仍需独立实际运行，它与本测试职责不同。此处不重复启动任何待完成任务。

本脚本在导入 NumPy/SciPy 前拒绝已有输出。输出仅是小型 JSON 元数据：源码身份、版本、各场景哈希与计数，不写数值数组。报告上限为 100000 字节，超过即报错，不截断。

若自然完成，应有独立观察到的工具 exit 0、报告状态 PASS_SMALL_SYNTHETIC_CSC_BYTES_AND_ALIAS_EFFECTS、15 个完成场景，以及原／新各 15 次完成构造。报告中的 script_return_code 只是程序自己打算返回的码；真正工具退出必须由 launcher 另录，不可用文件存在或程序字段代替。

失败时保留真实 stage、异常类型／文字、已完成场景和尝试／完成次数。源码门失败、fixture 未按预期发挥作用、字节差异或资源错误都只是本次合成检查失败，不自动证明主曲面不存在。不要补写通过报告。

factory_provenance 是比较开始前产生的快照，其 pending 字段不被重写；测试自己的顶层结果另行记录。这避免将一个后来的测试结果伪装成 factory 当时已有的证据。

即使本小测试日后实际通过，真实 W14 callback、完整 selector/preparer/runner/final-auditor 新来源，以及主问题的完整数值与连续证书仍须分别完成。当前 G5 没有因本脚本而关闭。
