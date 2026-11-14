# R159 的逐行组持久化：原目标不变的 partial normal 与顺序合并

**状态：** 下述可加性与覆盖结论为已证明的有限线性代数，直接应用 R159；实现的小合成保存／回读／求和检查已真实完成。它不是新曲面、BVP 收敛证明或连续误差证书。本组没有计算当前真实场的完整 normal。

## 1. 处理的实际缺口与范围

原 staged25 已有完整 baseline；同输入的 `normal-a01` 在约 cell87 处真实进程终止，未生成完整 normal。因此不能将那个未完成对象交给方向求解，也不能把24历史上算完但未保存的矩阵当成当前现存输入。

本组把 **同一25有限目标**的行拆成独立小片，完成一片即由已闭 `fd2d_gc_normal_checkpoint.py` 无损保存。下一进程只需算缺片，全部齐全后才顺序求和并使用原缩放、阻尼和 Schur／SLSQP 方向。真实 CLI、逐片进程管理、baseline 与输入绑定由 numerical 代理负责。

本组源为 `scripts/fd2d_gc_partitioned_normal.py`，冻结 SHA256：

`5802e1c2d366ff98b48127e8ca0327bb4027b97135bd2dae3032553c9741554c`。

这里使用原25的 `gauss_cell_positive_trace_frozen_operator_compatible`。R165 的新 coast 全 actual 同点细积分并未在本组替换进去。以后选择新有限目标时须显式更换 consumer 与输入身份，不能把两种目标的片混合。

## 2. 片计划和真实行覆盖

接口为：

```python
make_normal_partition(problem, *, node_block=16, cell_block=4,
                      interior_cells=(), interior_block=1)

assemble_normal_tile(problem, vector, descriptor, *,
    curvature_cap=7.2, curvature_weight=1.,
    high_gauss_weight=1., high_codazzi_weight=1.,
    interior_gauss_weight=1., block_cells=2,
    cell_consumer=gauss_cell_positive_trace_frozen_operator_compatible,
    progress=None, binding=None)

merge_normal_tiles(problem, tiles_iterator, plan)
```

后两个接口均返回原 `LocalNormalSystem` 和小 `info` 字典。合并输入是依计划顺序产生 `(descriptor, normal)` 的迭代器，不是将全部 full-shape partial normal 放入内存的列表。

计划的默认顺序严格如下。`N` 为保存网格的节点数，`q` 为每节点 raw 维数，`P` 为全部显式参数数；不由 `K+1` 猜测独立尾参数数。

| 片类 | 覆盖 | 原行标签 | 默认单片上限 |
|---|---|---|---:|
| nodes | 节点 `0,…,N−1` 各一次 | 需要的 `node_G`、`node_high_G`，及各节点 `node_curvature` | 16节点 |
| cells | 单元 `0,…,N−2` 各一次 | `cell_C`、`cell_high_C` | 4单元 |
| boundary | 唯一一片 | 依原顺序 `cut_l`、`central_boundary`、`cut_nm`、`gap` | 唯一组 |
| interior | caller 明确选择的不同单元各一次 | 每单元 `interior_retained`、`interior_high`、`interior_curvature` | 1单元 |

节点 Gauss 行沿用原选择：coast 窗不等于1，且节点小于 `trace_ramp_stop`；准确 cut 不加这些节点 Gauss 行。曲率 active 行数由原消费者真实返回，可以为0，不事先臆定。内部点沿用原 G2、原 P1 两端点拉回与原 `sqrt(weight)` 权。

每个 descriptor 保存 `id/ordinal/kind`、四类显式索引／边界标志、plan SHA、原 mesh 身份、全部 eliminated map 身份、维数及本 helper 源 SHA。生成器和合并器均核对节点与单元各恰一次、唯一边界、所选内部单元无重复且顺序保持。实际 assembly 的 observer 只记录小行账本：标签、依赖节点、行数；每次 `normal.add` 都必须对应下一条账本记录。它不保留所有局部 J。

对当前25保存布局，调用方将明确传入129节点、K31、独立tail16、profile7及54参数，内部单元 `[63,64,73,74,121,122]`。这些是待消费的真实任务设置，**不是本组合成检查计算了其完整矩阵**。CLI 保存的 actual plan 才是该计算的精确分片实体。

## 3. 消元以后可加：完整证明

设原加权有限残差按原行组写成 $r_b$，其对原 raw 与全部物理参数的 Jacobian 为 $J_b$。令 $E$ 是 R159 既定的精确方向映射：

- 中央固定节点的 raw 方向由中央参数基映入相同全局参数列；
- cut 的固定 raw 列删除；
- 完整帽支撑在 coast 平台内的无效 raw $l$ 列删除；
- terminal trace gauge 用 $d l_{\rm raw}=-d n_{\rm raw}$，实际保留列为 $J_n-J_l$。

写消元后 $A_b=J_bE$，将其列分为自由场 $f$ 和全局参数 $p$。**参数列的中央贡献必须先合入 $A_b$，然后才平方求和**。例如本来就有的参数列 $B$ 与中央映射项 $C$ 应贡献 $(B+C)^T(B+C)$；分别平方再加会漏交叉项。

对互不重叠且穷尽全部行的片集合 $\mathcal T$，令

$$
H_T=\sum_{b\in T}A_b^TA_b,\qquad
g_T=\sum_{b\in T}A_b^Tr_b,\qquad
\nu_T=\sum_{b\in T}\operatorname{colsum}(A_b\odot A_b),\qquad
R_T^2=\sum_{b\in T}r_b^Tr_b.
$$

因为这只是有限和的重分组，实数算术下

$$
H=\sum_T H_T,\quad g=\sum_Tg_T,\quad
\nu=\sum_T\nu_T,\quad \|r\|^2=\sum_TR_T^2.
$$

每个节点行只依赖本节点和 $p$，每个 Codazzi 或内部点行只依赖相邻两个节点和 $p$，边界只依赖其指定节点和 $p$。故 $H_{ff}$ 的非零位置仍仅为对角节点块和相邻上／下块；添加内部 Gauss／曲率行不改变这一结论。每片足以保留：

$$
H_{ff}^{\rm diag},\ H_{ff}^{\rm upper},\ H_{fp},\ H_{pp},\
g_f,\ g_p,\ \nu_f,\ \nu_p,\ R^2
$$

以及实际行数、块数与各标签行数。相邻下块由上块的转置表示，不另存、不丢失。上述各量逐项相加就是原完整未缩放 normal，证毕。

具体 assembly 复用已闭 `stream_positive_trace_normal` 的 `node_indices/cell_indices/include_boundary` 子集接口；它不在每片重复调用含全部 interior 的 whole wrapper。interior 片独立调用 `interior_gauss_curvature`，从其真实全列 J 取 `[left q,right q,all P]` 后交给同一个原 `normal.add`。因此真实中央映射和 gauge 恰由同一个已闭 `EliminatedFieldMap` 执行。

## 4. 缩放、阻尼及浮点意义

必须先合并完整的 $\nu$，再使用原式

$$
S_{ii}=1/\max(\sqrt{\nu_i},10^{-12}),\qquad
\widetilde H=SHS+\lambda I,\qquad
\widetilde g=Sg.
$$

每片单独缩放、添加阻尼或先做 Schur 消元再相加都不是上述恒等式，本 helper 不做这些操作。完整对象仍是原 `LocalNormalSystem`，原方向入口可直接读取；全部约束、参数盒、gap 条件、Armijo 真 trial 均保持其原职责。

实数意义的同方向不等于 binary64 的逐位同方向。片内原局部乘积不改，片间求和改变了浮点加法的括号。如果无溢出等异常、采用标准相对误差模型，$T$ 个既有浮点片量的串行求和有逐项 $\gamma_{T-1}\sum|a_T|$ 界；这不消除各片原乘法／求和本身的舍入，也不自动控制病态 normal 的求解方向。实际方向仍须由保存矩阵按原算法计算，并用真实有限目标线搜索。本组没有因分片而放宽任何物理约束或接受条件。

## 5. 身份、传输和未完成对象

片内固定绑定包含：准确 packed `vector` 的 shape/dtype/字节 SHA，原各权及求积设置，显式 consumer 的模块／函数／源 SHA，caller 提供的严格 JSON `binding`，本源 SHA。plan 另外绑定 mesh 及所有消元映射字节，包括 `field_maps` 和 `parameter_maps`。动态缓存安装后的 `type(problem)` 类名不作为数学身份；按同一函数构造的缓存／非缓存视图可恢复同一片。

**物理输入与传递依赖不能只靠这些局部数组猜测。** 正式 CLI 将共同 `ctx.binding`、baseline residual 身份、actual plan 及 actual tile/merge/io 源身份放入所有片相同的 `binding`。传输层再以 `{'common': common_binding, 'descriptor': descriptor}` 绑定该片的准确位置。合并器比较所有片的共同 state binding，并核对有序 descriptor；不同场、参数、权或 consumer 的片不能混入。

保存／回读完全复用已闭源 `fd2d_gc_normal_checkpoint.py`：原数值 dtype、小于1MB的有界 NPZ 片、逐片 SHA、typed metadata、先完成目录后原子改名。这里只保存实际得到的 partial normal，不把中断前未闭存的内存状态补写成存在。

合并器读取一片、核绑定和行账本、加进总和、释放该片，再读下一片。它只保存小 descriptor/计数摘要，不排序／缓存所有矩阵。缺片、重复、错序、额外片或映射不同都不能返回 `complete=True`。只有计划全部片被消费且确认输入迭代器结束后，才产生完整未缩放对象。

## 6. 唯一小合成检查与真实失败记录

本检查是6节点、每节点5个 raw 分量、4个全局参数、K1、16工作角的 **合成行 fixture**。原映射含两个中央节点、一个 coast 无效 $l$ 节点、一个 terminal trace pair 和固定 cut；自由节点宽度为 `[0,0,5,3,4,0]`。源使用明确固定 seed 的小随机行；边界列采用原中央／cut结构。为测试 tile public API，仅在 checker 进程中替换新模块引用的两个 assembly 入口为合成行，**不调用真实物理 BVP／Codazzi，不修改任何已闭源**。

第一次 `6232 / 066750 → 49f68f` 真实 exit1，14.753867526 s。9片都已保存／回读且合并走完，最后写报告时 `numpy.bool` 不能 JSON 序列化。旧 checker、console、exit receipt、plan 及已生成片均保留；未产生的报告不冒成已保存。

第二次仅另名 `fd2d-metric-partitioned-normal-check-v2.py`，把该比较结果显式转成 Python `bool`；partition helper、normal、transport 源均未改变。`6584 / 9e027f → 78675a` 真实 exit0：

| 项目 | 实际读数 |
|---|---:|
| 片数 / 行数 / 原局部块数 | 9 / 105 / 32 |
| 保存回读数组、映射、typed metadata | 全部逐位一致 |
| 各类行数及顺序 | 与原逐行构造一致 |
| 中央到参数、coast删除、trace耦合、cut固定 | 均实际核对一致 |
| 分片和与原逐行和的最大 scale 归一差 | $2.220446049250313\times10^{-16}$ |
| 内部用时 / wrapper用时 | 3.388038299 s / 11.885113392 s |
| 峰 RSS | 70140 KiB |
| 缺末片／重复首片 | 均真实拒绝返回完整对象 |

这里归一分母为每项 `max(1,maxabs(reference),maxabs(merged))`。它是这一次小数组实际实现证据，不是所有物理输入误差的统一上界。报告为 `notes/2026-11-12-fd2d-metric-partitioned-normal-02-report.json`。

可重做命令（输出 stem 须选未存在的新名字，因为 transport 不覆写已闭目录）：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
python scripts/fd2d-metric-partitioned-normal-check-v2.py \
  --out-prefix notes/2026-11-12-fd2d-metric-partitioned-normal-repeat
```

本组合计90个可重生 checkpoint 小文件共940984字节。为遵守根规11，不把这两套合成中间数据重复入库；保留生成脚本、两个准确plan、报告／真实失败／退出收据及逐文件 SHA 清单。它们目前本地确实存在，源丢失后的重做不依赖对话中的数组。
重新执行会产生新的计时和元数据身份；清单中的旧 SHA 标识本次真实实体，不声称下一运行的元数据逐位相同。

## 7. 下一真实执行的界限

numerical 代理接上述冻结 helper，真实生成当前25的 plan，逐片运行并保存，然后按 plan 迭代加载合并。只有那一轮的真实退出／manifest才能说明当前物理场的 normal 已存在；本组合成检查没有预付它，也没有产生新方向、trial、accepted 场或强目标解。后续 R165 改用全 actual 同点细积分时，应使用该新目标自己的完整 baseline、片身份和实际 line search。
