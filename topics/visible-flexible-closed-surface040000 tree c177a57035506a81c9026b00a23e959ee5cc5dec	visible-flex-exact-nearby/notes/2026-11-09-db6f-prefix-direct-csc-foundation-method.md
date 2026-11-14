# W14 直接 canonical CSC：未安装的 foundation v2 与纯检查器

日期：2026-11-09。作者会话：db6f / coupled_prefix。

## 1. 交付与当前边界

本批只提供函数、来源门和纯源码／整数布局检查器。没有安装到 SciPy，没有改任何旧 selector、运行入口、原 Newton、SuperLU 或 merit，也没有调用矩阵、BVP、DN、RK、几何导出或连续认证。

采用版本是：

| 文件 | SHA256 | 字节 |
|---|---|---:|
| scripts/db6f-prefix-direct-csc-foundation-v2.py | 8e2bb061ef1fee94672601132cedb8ca7565d4006a327474f039f501e5f516cf | 17550 |
| scripts/db6f-prefix-check-direct-csc-foundation.py | e437630f9718a898b31d16b21a2616034b0984d17a6b05ac5913f6cc7ec509dd | 19402 |

历史 v1 是 scripts/db6f-prefix-direct-csc-foundation.py，SHA256 cc837e05dbce4f8e8fe906b74b6d139dd126efea0fed04187f1395bde0a02e54。它未安装、未调用。作者在冻结后自审发现“原第一次 hstack 提前读取边界块”的别名范围，遂保留原件并另建 v2；不能继续把 v1 作为拟运行版本。

完整来源及三处 v1→v2 文本替换见同目录的 db6f-prefix-direct-csc-foundation-sources.json。原始数学依据是已全文独审的 db6f-prefix-weighted-bvp-block-factorization.md 及其 notation-erratum。评价点始终是当前加权状态和当前参数，线性未知量只是待求修正。

## 2. 唯一装配变化

设 n≥1、m≥2、k≥0，未知量依次为 m 个 n 维节点向量以及 k 个参数。令

$$
N=nm+k,\qquad L=(2n+k)N.
$$

这里 L 是显式存储位置数，包含数值为零的位置。原 Jacobian 的区间块为 A_i、B_i、C_i，边界块为 D、E、F：

$$
A_i x_i+B_i x_{i+1}+C_i\xi=b_i,\qquad
D x_0+E x_{m-1}+F\xi=b_{\rm bc}.
$$

A/B 的形状为 (m−1,n,n)，C 为 (m−1,n,k)，D/E 为 (n+k,n)，F 为 (n+k,k)。所有 n+k 条边界行及 k 个参数列完整保留。

新 column_segments 按以下顺序枚举单列中的片段：

| 列 | 片段及严格递增行范围 |
|---|---|
| 节点 j 的分量 a，j>0 | B_(j−1)[:,a]，行 (j−1)n 到 jn−1 |
| 同一节点列，j<m−1 | A_j[:,a]，行 jn 到 (j+1)n−1 |
| 节点 0 的列 | 上述 A 后接 D[:,a]，起始行 (m−1)n |
| 节点 m−1 的列 | 上述 B 后接 E[:,a]，起始行 (m−1)n |
| 参数 q 的列 | C_0[:,q] 到 C_(m−2)[:,q]，再接 F[:,q] |

节点列的 B 在 A 前。边界行在所有区间行之后。m≥2 保证两个端点不同，不会在同一列重叠 D/E。k=0 时参数部分为空；D/E 仍各有 n 行。n≥1 时每个列都有显式位置，最后位置使原 COO 推断的形状确为 N×N，即使所有数值都为零也如此。

因此无重复坐标，单列行号严格递增，按列排列恰为原 COO 转 CSC 再排序、去重后的 canonical 次序。计数为

$$
2(m-1)n^2+2n(n+k)+(m-1)nk+k(n+k)=(2n+k)(nm+k).
$$

新装配直接分配 data、indices、indptr；不创建全局 COO 两坐标数组，不通过 hstack 拼接全局 values，不删结构零。column_segments 是生成器，不缓存全体片段。它只另用长度 n 和 n+k 的整数行模板。

这给出存储布局的精确命题。实际 NumPy/SciPy 的 data、indices、indptr 三数组逐字节对照仍未运行，不能把纸面布局证明写成那项测试已通过。

## 3. 原浮点语句、两次 dtype 提升与 v2 读取时序

新 construct_global_jac 从冻结原函数逐句保留全部 A/B/C 算术，包括：

- 两个原 transpose 与 h 的维度扩展；
- identity 初始化与各次 -=、+= 的原顺序；
- 原 stacked_matmul 调用、原除法和乘法次序；
- df_dp_middle += 0.125 * h * T 恰好一次；
- 原 C 块表达式，不重复评价任何回调。

原两次 hstack 的 dtype 逻辑也保留。令 D0 为 A/B/D/E 共同 dtype，D1 为 D0 与 C/F 的共同 dtype。新装配按原顺序用 np.result_type 得到 D0、D1；每个 A/B/D/E 小片段先 astype(D0, copy=False)，再赋入 D1 的最终缓冲。C/F 直接赋入最终 dtype。k=0 时只有 D0。这样不把原两次提升合并成一次。当前 W14 的适用输入是原回调产生的普通、有限、实 float64 数组；本批没有扩大为任意第三方数组子类行为的兼容声明。

v2 还保留了第一次 hstack 的读取时序。原 first hstack 在参数中点的原地更新前，已经复制了 D/E 的值。如果 D/E 的底层存储与 df_dp_middle 意外重叠，仅在最后装配时读取 D/E 就不能无条件等价。

v2 在原 first-hstack 位置做 dbc_dya.copy()、dbc_dyb.copy()，然后才进入原参数块计算。A/B 已由原代码分别新分配，无此别名问题；F 仍在参数更新后读取，和原第二次 hstack 相同。这里不假定当前 W14 实际发生别名，也不把这种潜在别名当旧算例的失败原因。n=43、k=14 的两份边界快照合计

$$
2(n+k)n\cdot8=39216\ {\rm bytes}.
$$

原浮点表达式顺序没有改变，但分配时间点和内存异常的发生位置会改变。本方案只主张有效输入上成功装配的等价；不会把 MemoryError 后的异常时序或部分副作用冒称逐字相同，也不授权失败后偷偷回退使用另一 Jacobian。

## 4. 索引 dtype 与 pinned SciPy 依赖

新代码调用原 get_index_dtype(maxval=max(N,L))，不固定 int32。

被冻结原 _coo.py 先按坐标内容及形状选择索引类型，压缩时又使用 max(nnz,N)。本图所有坐标处于 [0,N−1]，最后指针为 L，故直接构造所需范围是 max(N,L)。若原 np.intc 的字节宽度不是 4，原 get_index_dtype 会选 int64；新代码沿用同一函数。超过 32 位长度界的情况也由它处理。实际环境中的类型选择仍应由后续运行记录，不能仅据常见平台推定。

原冻结本地 _bvp.py 的完整字节与官方 scipy/scipy 的 v1.17.0 同文件 SHA256 一致。这里用于定位完整源码，不由单个文件的相同 SHA 推断整个安装包的版本。foundation 的来源门还绑定 _coo.py、_compressed.py、_sputils.py、_csc.py、_base.py 的完整哈希。来源 ledger 给出官方固定 ref 和完整 SHA。复制的 SciPy 代码保留 BSD 许可声明。

## 5. prepare_sys 与函数绑定

模块顶层只导入标准库并定义常量、类型和函数。顶层不导入 NumPy/SciPy，不调用 factory。

make_functions(backend) 是未来显式调用的绑定函数，返回：

1. 新 construct_global_jac；
2. 新 prepare_sys；
3. 来源和实际函数身份账本。

它本身不安装，不替换任何 backend 属性，也不调用 callback、矩阵或 solver。它将来会读取并核对指定源码，编译文本以比较实际 Python 函数 code、globals、defaults、kwdefaults，并核原 CSC 类及关键构造方法身份；编译不是执行源码。它验证原 NumPy 命名空间、有限差分 EPS、原 callback 和 get_index_dtype 的身份，记录 NumPy/SciPy 版本字符串及新函数 code 哈希。这项实际绑定门目前没有调用。

新 prepare_sys 只从原函数删去 compute_jac_indices 语句，并从新 constructor 调用中删去两个不存在的全局索引参数。其余回调顺序、估计导数分支、用户 fun_jac/bc_jac 分支、x_middle、col_fun/sys_jac 签名及返回二元组保持原样。原两条大型索引不在这里创建，因而也不会被 sys_jac 闭包保留。

foundation 故意不读取、验证、安装或包装 solve_newton。后续完整入口必须另行明确选择原 Newton 或已经独审的 release-LU Newton，不能用本 foundation 的来源门代付那一身份。

## 6. 纯检查器及现有实际证据

检查器是标准库 Python 程序。将来运行时，它：

- 只以文本读取六个 pinned SciPy 源文件；
- 按完整 SHA 验新 foundation，关闭 pyc 写入后仅导入其标准库定义；
- 对原／新两个完整函数做唯一文本替换重放及 AST 相等检查；
- 检查新源码中没有 compute_jac_indices、coo_matrix 或 np.hstack 构造；
- 只调用 dimensions 和 column_segments，不调用 make_functions 或 _assemble_csc；
- 用独立的原 COO 六块行优先符号枚举，排序后比较 36 个小维数组合的所有整数位置和块条目标签；
- 覆盖 m=2、k=0、k>n、n=43，并检查 8 个非法维数、5 个损坏符号布局；
- 对 5047/6344/6500 节点只算整数大小，不枚举那些大布局；
- 核 32 位长度阈值两侧的整数公式，明确没有实际 dtype 调用；
- 只向一个不存在的新小 JSON 路径写报告，或输出到 stdout。

环境恢复并获得允许后，纯检查命令模板为：

    python3 /ABS/REPO/topics/visible-flexible-closed-surface/scripts/db6f-prefix-check-direct-csc-foundation.py \
      --scipy-source-root /ABS/INSTALLED/scipy \
      --out /ABS/REPO/topics/visible-flexible-closed-surface/notes/NEW-direct-csc-source-integer-check.json

该命令目前未执行。不能把源代码内将来生成的 PASS_SOURCE_AND_INTEGER_LAYOUT_ONLY 字段当现成报告。

本批已经实际做的是 functions V8 中的完整文本重放：原 construct 的三项指定替换、原 prepare 的两项指定替换，以及完整 v1→v2 三项替换均精确匹配；所有新文件都先核新路径不存在，并在保存后按固定 commit 全文回读相同。没有运行 Python、Python AST checker、foundation import、factory、NumPy/SciPy、矩阵或 solver。来源 ledger 如实逐项记录这些界限。

## 7. 内存量与下一入口

本批消除的是原大型 COO 坐标构造及全局 hstack 缓冲，不是全部 BVP 内存。n=43、k=14、m=6500 时 L=27951400；若原两条坐标为 int64，它们合计 447222400 字节。新最终 data/indices/indptr 仍必须存在，原导数、中间 A/B/C、T、Newton/SuperLU 因子及其他进程也仍消耗内存。新的 D/E 快照和小片段转换有自己的分配。不能由这些静态字节数保证某个 DATA 上限或 cgroup 峰值。

完整新入口尚未编写，也未获运行资格。后续最小接线必须满足：

1. 新 selector 明确取得本 v2 factory 返回函数，记录完整实际身份；若显式安装新 prepare_sys，就记录被替换的原函数和恢复策略，不能冒称仍用原 prepare_sys。原 construct_global_jac 可留在原模块中，实际新闭包调用的是明确返回的新函数。
2. 原 W14 正对角共轭、物理回调、未知参数、BC、八轮 outer、真 nonlinear DN/J、最终 audit seam、原容差与 guard 均不改变。原 SuperLU 调用与 weighted step² merit 保持原样。
3. 纯准备器、运行清单与 final auditor 增加新的 foundation、实际 prepare/construct、六源和 runtime identity；保持原尾八源与物理输入来源，不把新来源标签冒充旧来源。
4. 恢复后先实际核有效输入下两种 CSC 的 data/indices/indptr、dtype、结构零与 canonical 标志，再核所选原线性求解和调用轨迹。这个开发验证不能替代完整图、等距误差或 G5 证据。
5. 未完成上述完整入口及独立审查前，不运行 BVP/DN，不从本函数模块的存在推断任何研究完成结论。

这份新方法与 source ledger 不更新 HANDOFF、LOG 或 results。当前冻结 metric、已有算例和已关闭失败记录均保持原身份。
