# 直接 canonical CSC foundation v2：完整独立静态审查

**结论：接受当前 v2 的函数源码、canonical 布局证明和纯检查器设计；实际 Python、运行绑定及数值三数组重放均未完成。**  
审查人：`/root/tail_review_continued_2`，2026-11-09。作者：`/root/coupled_prefix`。本审查未参与具体实现。已全文读 v2、历史 v1、纯检查器、完整方法、来源/变换清单及 publication role 勘误，并核对相关冻结 SciPy 源码。

这是未安装的函数模块审查。它不构成新 BVP 入口，不替代 selector/preparer/runner/final auditor 的完整来源链，也没有运行 Newton、SuperLU、矩阵、BVP、DN、RK 或几何后台。完整静态核查未发现阻断；下文严格区分已证明的布局与源语句等价、实际完成的文本重放，以及尚未执行的运行门。

## 1. 固定批次与版本身份

批次清单：

- `notes/2026-11-09-db6f-prefix-direct-csc-foundation-publication.json`。
- commit `df4f14c37015743f7b1b7936d31cbdeb2b84f42b`，blob `fa7dce5a614110967b62cd71558fab7deb103d17`。
- SHA-256 `88e06471439caceaf85871d1e9cc2936f37fa2a5f1d5028d8c3d0f141ddcb74f`。

五件源码/说明均已由本审查人在其各自固定提交全文取回，并独立核长度、Git blob 和 SHA-256，全部一致：

| 文件（题目目录下） | 固定 commit | bytes | SHA-256 |
|---|---|---:|---|
| `scripts/db6f-prefix-direct-csc-foundation.py` | `05ef1c42268872bb8b5ccf4094a2709f9606735a` | 17,269 | `cc837e05dbce4f8e8fe906b74b6d139dd126efea0fed04187f1395bde0a02e54` |
| `scripts/db6f-prefix-direct-csc-foundation-v2.py` | `5b7a715833357675cbe5d9944ce54a165997473a` | 17,550 | `8e2bb061ef1fee94672601132cedb8ca7565d4006a327474f039f501e5f516cf` |
| `scripts/db6f-prefix-check-direct-csc-foundation.py` | `cbd77df636c629c3bbd5c1cf6aab6838149f3bb8` | 19,402 | `e437630f9718a898b31d16b21a2616034b0984d17a6b05ac5913f6cc7ec509dd` |
| `notes/2026-11-09-db6f-prefix-direct-csc-foundation-sources.json` | `f95a5bf8c5522f0ea6e5301156fa7ff912881b77` | 7,798 | `336d21ae0809cfc3d6eb4da286e0a2e26fc5fcdf52c29255ebf57d84a98f03dc` |
| `notes/2026-11-09-db6f-prefix-direct-csc-foundation-method.md` | `df6acfbcacd8409bef103776178d2faad13517d6` | 11,261 | `864a6bcc0c5440431f15363ab90517fb55686b28006a164714f012352013a295` |

最终目标 v2 的 Git blob 是 `71f91271133dacd85e4d8d63a7ec3b757222d453`；检查器 blob 是 `aefd12d209e86017afe9550f12f3b6c08c42ce42`。历史 v1 未修改，也不作为拟运行版本。

另读 role 勘误：

- `notes/2026-11-09-db6f-prefix-direct-csc-publication-role-erratum.md`。
- commit `1887f119654bf3098a6a7f957a62d1da105ea5bb`，blob `bd2d6c6eda663add0dfc1b6f95f1d96daad53e54`。
- SHA-256 `bb47bafdaeac6f5409e6d23c3c123f0d716b21a4af89535e0eb22fabd3e83e61`。

原 publication 中检查器被误标成 historical v1，是文件名后缀分类错误。实际检查器的固定哈希、`FOUNDATION_SHA256` 和默认目标路径均指向 foundation v2；其报告 schema-v1 只是检查器报告首版。该勘误没有改源码或未执行状态，可与原清单合读。

## 2. 原始数学与官方源码绑定

数学依据仍是已独审的 weighted BVP block-factorization 稿及记号勘误，完整独审固定于：

[先前完整数学审稿](https://github.com/Rogerhu12/math-research/blob/82c2ce3ed327c2e5299e17352ceb459740b9bb73/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-tail-review-weighted-bvp-block-factorization.md)。

本批没有采用那份稿中的平衡 QR 替代算法。它仅把同一个 collocation Jacobian 的 COO/hstack 装配换成 canonical CSC 直接装配；原线性求解、Newton merit 和迭代规则不属于这份模块的修改范围。

本审查实际从 `scipy/scipy@v1.17.0` 取得下列完整文本，逐项核对来源 ledger 的 blob、长度、SHA-256：

| 官方路径 | bytes | SHA-256 |
|---|---:|---|
| `scipy/integrate/_bvp.py` | 41,294 | `59afffb3607b272ae77f346d86428e43eca359fe90f2605da60a9571e60970d2` |
| `scipy/sparse/_coo.py` | 74,635 | `95e4bcd796900894acea3256a7b5a4cab654427bb9fcb9f0e57ec9fb40dc6898` |
| `scipy/sparse/_compressed.py` | 52,058 | `d8d847ceb10469b91dc2f64e2be7ec3af04e1a099db9fbb91fb32526f860dc0f` |
| `scipy/sparse/_sputils.py` | 21,095 | `b1cdc32d7e49fab5add7ec14f0858321275186e083362e6cc2628f6fef5a641f` |
| `scipy/sparse/_csc.py` | 11,162 | `88c462e71172169295fa8e1f7ff23d4a3c0037e847a7b6037e74c812ee236552` |
| `scipy/sparse/_base.py` | 58,343 | `e6d70fd65f0378f198cdf0c83986aa3b477f87da47137037ef6056d42481fd1b` |
| `LICENSE.txt` | 1,531 | `221e59f5e910fd7f94e44f0dac77436a11338c285c6346232e4a850a50da0e94` |

上述单件均小于 100KB，只有源码文本，没有主优化数组或数据包。特别核对了原 `compute_jac_indices`、原两完整函数、回调函数、CSC 三数组构造分支、COO 压缩分支、索引 dtype 选择及所绑定的支持方法。复制源码保留了许可证。

`_bvp.py` 的全文件哈希与此前实际冻结的本地文件相同；这一事实不独自证明整个安装包、NumPy、BLAS 或 SuperLU 的运行身份。当前也没有实际安装环境可以调用验证工厂。

## 3. 完整文本变换已由审查人实际重放

在 `functions.exec` 的 JavaScript 隔离运行时，审查人从上述固定原源抽取完整函数，按冻结清单逐项要求唯一出现并替换，然后与 v2 的完整对应函数逐字比较；另对完整历史 v1 作三处替换并比较整个 v2 文件。

实际回执：

- 身份：`tail-review-direct-csc-full-text-replay-01`。
- UTC：2026-11-09 23:23:28。
- constructor：3 项正文替换及明确的新签名/简短 docstring，完整新函数一致。
- prepare：2 项替换，完整新函数一致。
- v1→v2：3 项替换，完整文件一致。
- 状态：`PASS_TEXT_ONLY`；调用实际完成。
- Python、Python AST、foundation import、factory、矩阵和 solver：均未调用。

抽取函数哈希：

| 完整函数 | SHA-256 |
|---|---|
| 原 `construct_global_jac` | `f209e18f334535a5b5fbe571ac4a875dccef89ab5b77b94977023f4b0919b916` |
| 原 `prepare_sys` | `2e2a6f40f709556a98065b41491e1d90980fa68d8f0c9e59e15928732f144e54` |
| 新 `construct_global_jac` | `2361d669b2e6a836effb3d9db227e63ec0739a41c3894150e61badd6c9da1afd` |
| 新 `prepare_sys` | `e95c8ba1141a8c3620f069af1abc6066c1a84580d6ba1d02f240f13d2b76946f` |

这项实际文本重放证明所声明的源语句差分闭合；它不是 Python AST 检查器已运行，更不是 NumPy 字节等价测试。没有为不可用的终端制造退出码。

## 4. canonical 布局的完整核对

设
\[
n\ge1,\quad m\ge2,\quad k\ge0,\qquad
N=nm+k,\quad L=(2n+k)N.
\]
未知量依次是 \(m\) 个节点向量和 \(k\) 个参数。旧六块为 \(A_i,B_i,C_i,D,E,F\)，所有边界行共 \(n+k\) 条。

原 `compute_jac_indices` 的六组 row-major 坐标分别与原 values 中 \(A,B,D,E,C,F\) 的 C-order 展平一一对应。新生成器按列枚举：

- 节点 \(j>0\) 的第 \(a\) 个分量先给 \(B_{j-1}[:,a]\)，行 \((j-1)n,\ldots,jn-1\)。
- 若 \(j<m-1\)，再给 \(A_j[:,a]\)，行 \(jn,\ldots,(j+1)n-1\)。
- 首节点列追加 \(D[:,a]\)，末节点列追加 \(E[:,a]\)，边界行从 \((m-1)n\) 开始。
- 参数列按区间顺序给全部 \(C_i[:,a]\)，最后给 \(F[:,a]\)。

每一列的行范围严格递增且互不重叠。\(m\ge2\) 使两个端点是不同列组，故不会将 D/E 落在同一列；\(k=0\) 时没有参数列，但每端仍有完整的 \(n\) 条边界行。\(m=2\) 也没有特殊漏列：首端为 A+D，末端为 B+E。

原图案无重复坐标。显式位置数为
\[
2(m-1)n^2+2n(n+k)+(m-1)nk+k(n+k)
=(2n+k)(nm+k).
\]
每一列都有位置，最后一行和最后一列都由结构位置覆盖。因此原 COO 推断的形状确实为 \(N\times N\)，即便数值全为零；新显式 shape 不改变这一点。

`_assemble_csc` 逐段把相同块的同一列写入 data，写入对应行号，首次遇到每列时写 indptr。列号连续性和最终 \(L,N\) 的检查覆盖生成器的总长度。k=0 时 D/E 的 count 与 n 相等，代码选择 node_rows 而非同长度 boundary_rows，二者都是同一个 \(0,\ldots,n-1\) 行模板，内容一致。

所有显式结构零保留。标记 `has_sorted_indices=True` 与 `has_canonical_format=True` 有上述数学布局支持；没有通过设置标志来掩盖一个未经解释的未排序模式。实际 Python 生成器和 SciPy 输出仍待运行核验，但静态布局证明完整。

## 5. 原浮点运算链与副作用时点

完整变换证明保留了：

- df_dy 与 df_dy_middle 的原 transpose；
- h 的原维数扩展；
- A/B 的原 identity 初始化、各次加减和乘除顺序；
- 原 `stacked_matmul` 调用；
- 参数中点的 `df_dp_middle += 0.125 * h * T` 恰好一次；
- 原 C 表达式及其评价时点。

原导数在当前状态、当前参数和实际 collocation 中点评价；没有把线性修正变量用作 Jacobian 的评价点。新 prepare 不增删或重新计算这些回调。

v2 的 D/E 快照是必要的普通 ndarray 语义修订。原 first hstack 在参数中点原地更新前已经读取并复制 D/E；如果这些输入与 `df_dp_middle` 共用底层数据，延迟到最后才读取会改变成功装配的结果。v2 在原 first-hstack 位置先执行
`dbc_dya.copy()` 和 `dbc_dyb.copy()`，再进入原参数计算，正确保留这一时点。

A/B 则是本函数原代码新分配的独立数组，调用者的既有输入不可能预先别名到它们。F 仍在中点原地更新之后被读取，与原第二次 hstack 一致。原 df_dp_middle 与其他输入之间的别名、副作用及 C 的后续读取顺序，均由逐字保留的原算术继续决定。

这是针对合法普通 ndarray 输入上成功装配的等价分析。新分配和内存异常发生时点不同，不声称失败后的局部副作用或 MemoryError 路径逐字等价。当前实际 W14 合同是原回调的普通有限 float64 数组；未扩大到任意数组子类和第三方重载行为。

历史 v1 已保留，仅作未安装历史源码。作者自审后的 v2 是唯一当前目标，不能以 v1 的存在作运行资格。

## 6. 两次 dtype 提升和索引 dtype

原装配先把 A/B/D/E 合成 base dtype，再在 \(k>0\) 时与 C/F 形成 final dtype。新代码使用
\[
d_0=\operatorname{result\_type}(A,B,D,E),\qquad
d_1=\operatorname{result\_type}(d_0,C,F).
\]
每段 A/B/D/E 先转成 \(d_0\)，再赋入 \(d_1\) 的最终缓冲；C/F 直接赋入最终 dtype。k=0 只有第一次提升。这样保留了原中间转换，没有把两次提升合成一次而潜在改变数值转换。

D/E 的复制发生在早期，复制仍保留其原 dtype；原地参数更新不改变它们已经快照的值。F 的晚读取及其 dtype 参与顺序也与原流程相容。实际 mixed real/complex、别名和有符号零的字节比较仍未运行，不据纸面分析冒认这些测试已通过。

索引使用原
\[
\operatorname{get\_index\_dtype}(\text{maxval}=\max(N,L)).
\]
已核官方实现：普通四字节 intc 环境按是否越过 int32 范围及数组内容选择 int32/int64；若 intc 字节宽度不为 4，它直接选 int64。原 COO 先依据坐标及 shape 选型，压缩时还使用 \(\max(\mathrm{nnz},N)\)。本图坐标不超过 \(N-1\)，最后指针恰为 L，故新上界覆盖且匹配所需范围。

CSC 三数组构造分支会再检查数组及 shape 的索引类型；新 indices/indptr 已含同样的实际界。这里没有假定当前恢复环境必然为 int32，也没有实际调用过 NumPy 的 dtype 选择函数。

## 7. prepare_sys 的变化范围与闭包

原 prepare 的两处变化仅为：

1. 删除 `compute_jac_indices(n,m,k)`。
2. 从 constructor 调用中删除相应的两个全局索引参数。

其余完整函数已由实际文本重放确认一致，包括 x_middle、col_fun、sys_jac 的参数与返回二元组、fun_jac/bc_jac 分支、有限差分备用分支，以及节点、中点、边界回调的次序。

新 sys_jac 不创建、捕获或保留原两条大型 COO 索引。它捕获新 constructor 和已验证的原回调函数；新 constructor 捕获其 NumPy、CSC、stacked_matmul 与 dtype 选择依赖。这里是明确的新函数身份，不能说仍在调用原 prepare/construct。

模块不读取、选择、包装、替换或调用 solve_newton。原 Newton 与 release-LU Newton 的选择仍属于将来的显式入口，当前 factory 的来源账本不覆盖它，也不覆盖主 W14 的物理 callback 选择。

## 8. 未来 factory 的实际来源门静态核对

顶层只有标准库导入、常量、NamedTuple 与函数定义；没有 NumPy/SciPy 导入、矩阵分配或 factory 调用。

将来显式调用 `make_functions(backend)` 时，它会：

- 要求 backend 名称为 `scipy.integrate._bvp`。
- 读取六个指定模块的完整源文件并逐一核固定 SHA。
- 只 compile 已核源，不执行它，以获得原函数 code 对象。
- 核 NumPy 命名空间、原 CSC 类对象和有限差分 EPS 值。
- 对原 stacked_matmul、collocation_fun、两种估计 Jacobian 回调及 get_index_dtype 核实际 function 类型、code、globals、defaults、kwdefaults 与无闭包条件。
- 对 CSC 的原 constructor、check_format、prune、继承的 _get_index_dtype 及 _swap 作同样的实际方法核对，并比较最终类上解析到的方法对象。
- 返回两条新函数和来源账本，不安装到任何原模块属性。

已对照源码核其显式默认值：估计函数的 `(None,)`、get_index_dtype 的 `((),None,False)`、CSC constructor 的 `(None,None,False)` 及 `maxprint=None`、check_format 的 `(True,)` 等与冻结定义一致。所选关键方法没有这里会被误拒的零参数 super 闭包；`_swap` 是静态函数。当前未发现会使正常冻结源码必然失败的静态身份矛盾。

factory 自身记录 foundation 文件哈希及新函数 code 哈希，最终调用方仍须把这些实际字段与已冻结 v2 绑定。它不是完整安装器或最终 auditor，不能由其返回账本推断所有主求解、Newton、尾部和物理源都已核。它也没有在当前环境实际调用过。

## 9. 纯 Python 检查器的设计及尚未执行状态

检查器绑定 v2 全 SHA，默认路径指向 v2。在导入其标准库定义前核完整哈希并禁写 pyc；最终恢复 bytecode 标志和清理自己的临时模块名。它只把六个 SciPy 源文件当文本读取，不导入科学计算模块。

静态调用链中实际被调用的 foundation 函数只有 `dimensions` 和 `column_segments`。不调用 factory、assembler 或返回的数值函数。完整源码中没有间接的矩阵/solver 路径被 main 触发。

其预定检查包括：

- 原两完整函数的唯一替换重放和 AST 相等。
- 无原全局 COO/hstack/compute_jac_indices 构造。
- 顶层标准库和无原命名空间安装。
- 36 组小整数维数，与独立旧六块 row-major COO 标签排序作逐条对比。
- 8 个非法维数和 5 个损坏符号布局。
- \(m=5047,6344,6500\) 只算整数大小，不枚举这些大布局。
- int32 长度阈值两侧的整数公式，不调用真实 dtype。
- 拒绝覆写既有输出，并把新文本报告限制在 100KB 以下。

已独立对照旧 `compute_jac_indices`，确认检查器的六块参考标签确实对应原 COO，而非把新 canonical 枚举复制成 expected。小布局只含整数坐标和符号标签，不是新几何数据。负例覆盖数目缺失、行/列损坏和块标签错误。

上述是完整源码审查的结论，**不是这些 Python 检查已执行**。其将来生成的 `PASS_SOURCE_AND_INTEGER_LAYOUT_ONLY` 字段目前只是源码中的报告模板，不能被引用成现成运行产物。本次实际完成的 V8 文本重放已在第 3 节单列，不混为 Python/AST 重放。

## 10. 内存与完整入口边界

\(n=43,k=14\) 时 \(L=100N\)。在 \(m=6500\) 时
\(N=279514,\ L=27951400\)，若原两坐标数组为 int64，则它们合计 447,222,400 bytes。新的 D/E float64 快照为
\[
2(n+k)n\cdot8=39,216\ {\rm bytes}.
\]
这些都是静态大小公式；未测量 RSS 或 DATA 峰值。

直接装配不创建旧两条全局 COO 坐标和全局 hstack values 缓冲，但最终 data/indices/indptr、原导数、A/B/C、中间乘积、Newton/SuperLU 因子以及其他进程仍然存在。小片段 cast、行模板和 constructor 也有其分配。不能由所省坐标内存保证任何资源 cap、成功网格大小或 BVP 收敛。

后续完整入口仍需明确新的 selector/preparer/runner/final auditor 身份，原物理共轭、未知参数、边界条件、outer 流程、真实非线性 DN/J、容差和最终 seam 门均不因本模块而改变。基础函数的静态接受不授权偷偷替换原来源标签或失败后回退另一数学路径。

实际数值开发验证仍未付：

- 原、新 CSC 的 data/indices/indptr、dtype、结构零和 canonical 标志；
- 普通合法输入的别名及参数中点副作用；
- 原线性求解和 weighted step² merit 的实际使用；
- 明确选定 Newton 身份的完整调用轨迹；
- 主数学候选、闭图、连续误差和 G5。

本批不宣称其中任何一项已通过。作者另行准备的小合成字节检查源须作为新批次审查；保存检查源本身也不会支付运行门。

## 11. 判定与封存

静态接受目标仅为
`db6f-prefix-direct-csc-foundation-v2.py`
SHA `8e2bb061ef1fee94672601132cedb8ca7565d4006a327474f039f501e5f516cf`，以及上述冻结检查器、方法和来源说明合读后的设计。历史 v1 不作为当前目标，publication 的检查器 role 依独立小勘误解释。

已完成：全部新文件身份核验、官方来源绑定、全文静态审查，以及真实 V8 完整文本变换重放。未完成：Python/AST 检查、实际 factory、三数组字节、任何矩阵或 solver 调用。没有把静态没有发现错误写成运行通过。

本文件只新建小文本 note，创建后在实际固定提交处全文回读；原源、旧清单和勘误均不覆写。没有执行器探针、数据文件传输、主数组读取或隐式安装。HANDOFF、LOG、results 和主线状态由 root 统一维护。
