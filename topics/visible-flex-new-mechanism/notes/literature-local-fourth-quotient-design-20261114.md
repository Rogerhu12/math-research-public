# R109 局部第四商 consumer：来源、目标与接口

日期：2026-11-14。本文说明 scripts/literature_local_fourth_quotient.py 的第一轮公开计算。理论来源是 [R109](../results/R109-local-density-of-the-complete-fourth-quotient.md)；本说明不预告计算结果，不声称已支付完整第四周期或 ruling。

## 1. 目标与三个不同的次数

R109 已证明，对真实总矩阵为零的路径，

$$
[V_B]_{\mathcal R_8}
=
\left[\int_B\{v_s-\mathcal B_{m_s}(N_s)\}\,ds\right]_{\mathcal R_8},
\qquad \mathcal R_8=\mathcal B_{E_8}(W).
$$

$m_s$ 是 R73 的点态八矩；$N=P_{\rm acc}+P_h+F_*$ 是 R109 的有限局部第三势。$v_s$ 先作全部真实 $s$ 微分，再将累计 second/third history 的值置零；其导数不随之置零。

本轮只计算上述局部密度的**几何导数权零部分**，保留完整 $-4,-2$ 两个复相位模式。三种次数必须分开：

| 次数 | 本轮范围 |
|---|---|
| profile 次数 | 对 $(f,g)$ 恒为四次齐次 |
| 几何导数权 | 只取 $h_s,k_s,h_{ss},k_{ss},\ldots$ 全零后的局部部分 |
| profile 仿射权 | 按 $\xi$ 权 $+1$、$j$ 阶 jet 权 $-j$、右原函数权 $+1$ 分块；默认只顺序检查 $2,1,0$ |

几何导数权零不意味着将 moving frame 的导数置零。$T_s=kN$ 等框架转动仍全部保留；history 导数也仍含静态非零的点态二阶算子。这不是把原带改成一个平面。

本轮正结果只支付对应局部系数块。其余几何导数权、完整路径约束、第四 ruling 及有限等距族均未计算。改变 $N$ 的参考常势可能在不同几何导数权之间产生仅在总矩阵为零后相消的项，所以单独的零权片不能被冒称为一个与所有势选择无关的完整成本。

## 2. 复用原式，而不是重新编译旧第四目标

调用已发布 R56 原语恢复同一复 profile 的第二、第三场：

$$
A=Y_q,\quad B=\mathcal I H(A,A),\quad
U=\mathcal I H(A,B),\quad V=\mathcal I H(A,\bar B).
$$

只构造这几条低阶场及其真实 cov 导数，不调用旧 constant-pair target，也不调用原完整 fourth forcing 的 compile 分支。所有共轭复用同一组实几何系数和历史，保持同一个右端锚。

先计算每个场的真实分子协变导数及其 $\xi$ 导数，再将所有累计 history 值置零。为避免随后再次对已置零值求导而漏项，第四层直接使用

$$
J_s=\sum C_{ij}
(\nabla_sV_i\cdot V_j+V_i\cdot\nabla_sV_j),
$$

$$
(T_\xi)_s=\sum C_{ij}
((\nabla_sV_i)_\xi\cdot(V_j)_\xi+
(V_i)_\xi\cdot(\nabla_sV_j)_\xi).
$$

这里框架连接反对称，且不依赖 $\xi$，因此上述点积确是普通 $s$ 导数。令 $I(F)=\int_r^\xi F$，则

$$
P=-\frac{I(T_\xi)}{2h},\quad B_0=\frac{J}{2h},
$$

$$
P_s=-\frac{I((T_\xi)_s)}{2h}-\frac{h_s}{h}P,\qquad
(B_0)_s=\frac{J_s}{2h}-\frac{h_s}{h}B_0.
$$

再代 R56 原始 characteristic RHS。这一步没有增加第四 history，也没有把 $P_s,(B_0)_s$ 替成“先置零后的导数”。人工检查使用一个 history 值为零、真实导数非零的自造场，分别比对原 R56 的 $R,P,B,P_s,B_s$。

旧 full-range actual 43615655870 保存的是完整 DAG 的摘要、hash 与计数，没有序列化全部原节点。本 consumer 因而不声称从该报告读到了不存在的节点；它复用公开原语恢复所需低阶表达式，并首次为本局部目标输出可独立消费的原始 profile DAG。

## 3. 真实局部势、八矩与完整 W

完整外槽/内槽不同的第三局部密度来自已发布的 producer.compile_colored_local。采用同一 raw_decomposition 提取 $P_{\rm acc},P_h,R$，再调用真实 R79 端点势函数：

$$
F_*(k,\omega)=\int_1^k a_*(v,1)\,dv+
2\int_1^\omega b_*(k,u)\,du.
$$

这是整个一形式的实际代表，不是只取三个形式 moment，也不是单独的 $+1\to-1$ 端差。基准常势没有设零。

点态 $m_s$ 直接使用 R73 的八坐标闭式；只把几何导数权零的部分用于本轮。它不是拟合矩阵或一个周期的积分矩阵。

$W$ 的 36 个完整第三模板消费公开 v2 回执：

- run 43633746055；
- source 26c3f2c0308d179a094d3967cfb7189db426081e；
- 157380 字节；
- SHA256 7c2cb9fece518fb6fbb15b6b4e034565dfcc5a10cf0e103a7011cd56dc4ac960。

恢复时对全部 152 原模板的内容 hash 比对，然后选择回执中保留的 36 个原模板。已发表的 116 条完整原式依赖被消费，不重复研究编译。真实独立性另由 R87 的原式有理评价子式保证，不是由本轮正规形 rank 单独推出。

$N$ 的每个几何系数先模这个真实 $W$ 化简。每条化简都从原始彩色三线性表达式重新核验

$$
N_\alpha=\widehat N_\alpha+\sum_jc_{\alpha j}\tau_j.
$$

因此用 $\widehat N$ 替换 $N$ 只给局部第四密度加 $\mathcal R_8$ 中的项。此步骤减少后续昂贵的双线性代入，保留全部外槽。

## 4. 每个分块如何给可靠结论

完整响应使用八个独立的 $E_8$ 坐标，不沿用旧物理七维子空间的限制。对仿射权 $\ell$，只构造满足

$$
\operatorname{wt}(E_i)+\operatorname{wt}(\tau_j)=\ell
$$

的响应列。两个复模式共用同一组有理系数。

响应列之间的正规形依赖会从原始模板重新验证；因此成功的丢列关系给一个可靠的实际函数 span 上界，但不把剩余代表的 rank 自动叫作真实维数。

对局部密度的每个几何单项系数：

1. 保留它的原始两个模式与内容 hash。
2. 在该权响应 span 中做同组有理系数消元。
3. 若余项为零，从原始两模式和原始第三模板重新验证完整函数身份。
4. 若余项非零，只报告尚未获得身份，保存余项 hash 和有限预览，不宣称实际非成员。

即使将来某个局部系数被严格分离，也仍须处理总矩阵为零、端点和真实路径积分的约束，才能推出非零的 $\mathcal U_4/\mathcal R_8$ 成本。不能把局部系数的符号或非成员直接提升为真实路径不存在。

默认在第一个含未解决系数的块后停止继续计算其他权；已完成块独立保存。该停止是单个有界 Actions 计算的诊断边界，不是整个研究任务结束。

## 5. 原式导出与其他 consumer 的共同接口

两个导出都采用

    visible-flex-R109-local-fourth-quotient-static-v1-original-expressions

schema。正文为 UTF-8 JSON，再用确定性的 gzip 压缩；记录原始和压缩字节及 SHA256。

**早期 W-only 导出：** 36 模板的全部来源 hash 核对后立即写出，早于 $N$ 降维和第四目标代入。其 content_scope 为 W-only，包含 roots 的 W0 至 W35、完整可达 profile atom DAG、每个原式的原始内容 hash，以及 bound_W 的来源和保留索引。后续预算退出不会删除它。

主报告的字段为：

    portable_W_expression_export

该对象含 filename、stored_bytes、stored_sha256、raw_bytes、raw_sha256、root_count、profile_atom_count、content_scope。没有另一个 manifest；主报告本身同时记录 source_hashes、github_run_id、github_sha 和 github_repository。

**完整局部目标导出：** 在所有权分块之前保存，content_scope 为 W-and-local-static-density。除 W0 至 W35 外，还包含每个局部几何系数和模式对应的原始根及 geometry_key。主报告字段为：

    portable_original_expression_export

其余元数据与 W-only 相同。未来本脚本的 input-export 模式只接受这一完整类型，明确拒绝把 W-only 当成已完成局部目标。

共同解码接口为

    decode_expressions(ring, data) -> dict[str, Expr]

解码逐根重新计算 original_root_sha256；原函数按有向 DAG 恢复，不通过正规形重写。每个右原函数必须具有严格正的 profile 次数。尾系数 consumer 可只取 W0 至 W35，忽略局部目标根，并独立绑定源报告的原字节、run、commit 及上述两组 hash。

## 6. 第一次公开运行

新的最终文本是在执行环境断连后从完整上下文重建，加入早期 W-only 输出。它不是与此前本地人工版 d17c613ea3429d84e5818aed4465b63fa3a30592fb3c33e068e9e81fa156a02f 逐字相同的文件。旧版人工输出为 3359 字节、SHA256 f763f735401f0ad63aa560c385b16aaf661d1d311f6411731a285d9970a4058e；其中包含 history 真导数、势、点态 trace、六分之一因子和人工 DAG 往返检查。这个旧回执不冒充新源码已执行。

所以新公开 job 先顺序执行语法和人工检查；通过后，才执行研究目标：

    python -m py_compile topics/visible-flex-new-mechanism/scripts/literature_local_fourth_quotient.py

    python topics/visible-flex-new-mechanism/scripts/literature_local_fourth_quotient.py --toy-only --output /tmp/local-fourth-development.json

    python topics/visible-flex-new-mechanism/scripts/literature_local_fourth_quotient.py --weights 2,1,0 --max-seconds 300 --memory-mib 1024 --output /tmp/local-fourth-quotient.json

真正研究入口同时要求 GITHUB_ACTIONS=true 和 GITHUB_REPOSITORY=Rogerhu12/math-research-public。未满足时拒绝运行。root 负责将本次输出按公开工作流收集、核验与登记。

续接现成完整导出时，额外传入 input-export 和其已公开 SHA256；源依赖、类型、36 模板原 hash 和全部局部原根 hash 都必须匹配。该模式跳过低阶恢复、$v$ 和 $N$ 的重编译，只对指定新权执行消费。

## 7. 预算与失败回执

默认限制为 300 秒、1024 MiB RSS 轮询阈值、400000 个系数节点、100000 个 profile atom、100000 个单表达式项、每个 normalizer 1000000 次重写，以及消元时 8192 位有理数界。RSS 是显式轮询而非操作系统硬隔离；计时与内存钩子同时覆盖原继承编译器。

主报告与单块各至多 250000 字节；完整压缩导出至多 3500000 字节；早期 W-only 至多 1000000 字节；所有本次输出合计预算 4800000 字节并为主报告预留空间。若这些上限不能同时满足，保留已完成输出并给明确资源退出，不无界提高预算。

completion 区分 complete、toy_passed、resource_limit、implementation_check_failed 和 output_limit。成功的原式导出、完成块与当前 phase 会在失败回执里保留。没有完整实际输出前，不报告局部块已通过。

## 8. 保留的数学范围

本轮不构造或评价任何具体 profile，不数值积分几何，不拟合真实桥。它是有来源的准确原式分块消费。它不会把代表余项当作非成员，不把所有局部系数当作独立真实控制，也不会把一个几何导数权片等同完整第四商。

尚欠几何导数权二、四及可能的端点/局部积分相消；总矩阵零下的真实成本集合；完整第四 ruling；更高阶与收敛；闭嵌入、reach 和宏观幅度。完整研究继续由这些实际结果决定下一具体目标。
