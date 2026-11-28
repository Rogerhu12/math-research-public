# 完整偏导输入到直接映射 CSR：原公式与同对象接入

会话：Astra-held10-7c4e33ee-20261128 / analytic。2026-11-28。

**可信度：完整存储接线及真实源码准备。** 本条没有新的全 Jacobian/BVP、求解接受或实际内存收益；真正小输入位同检查由 design 的统一实算另行登记。旧 source、科学 kind 和全部验收门不改。

## 1. 原全部区间依赖

SciPy 原 `prepare_sys` 先求全部节点与全部中点的 $dY,dP$，再求全部 BC 导数，最后调用 `construct_global_jac`。本入口保留这一顺序、四个完整数组的形状、真实原批次和全部参数，输入可由独立 provider 写成可读写的 C-order memmap。

令第 $i$ 个区间的 $L,R,C$ 分别为左节点、右节点、中点的 $dY$，$p_L,p_R,p_C$ 为相应全部参数导数。原完整块是

$$
A_i=-I-\frac{h_i}{6}(L+2C)-\frac{h_i^2}{12}CL,
$$
$$
B_i=I-\frac{h_i}{6}(R+2C)+\frac{h_i^2}{12}CR,
$$
$$
p_C\leftarrow p_C+\frac{h_i}{8}C(p_L-p_R),\qquad
P_i=-\frac{h_i}{6}(p_L+p_R+4p_C).
$$

实现沿已冻结 `design/direct_csr_collocation.py` 的原运算次序：分别初始化、原地减/加和原 `stacked_matmul`；保留调用者可见的中点参数数组原地更新。$n>50$ 仍逐节点原 `np.dot`；$n\le50$ 仍原 whole-grid `einsum`，不借换小批次改变该分支顺序。

完整系统阶数 $N=nm+k$，每行保留 $w=2n+k$ 个条目，包括显式零。区间行的列依次是 $[in,(i+2)n)$ 与全部 $k$ 参数；最后 $n+k$ 条 BC 行的列依次是首端全部 $n$ 未知、末端全部 $n$ 未知及全部参数。故 stored entry 数准确为 $Nw$。所有节点、中点、末端行与参数列都保留。

## 2. 直接预分配输出与唯一 backing

独立源：`scripts/resume_20261128/analytic/complete_streamed_csr_assembly.py`，SHA `242d00c55b68083611e49eabef7ec86c8a4f5128254a03b26e8a0c3121beaca3`。

`construct` 保原 14 个位置参数，新增关键词 `storage_directory`、`radial_block`、`record`、`release_inputs` 和 `disk_margin_bytes`。`data/indices/indptr` 三阵直接位于一次真实 `posix_fallocate` 的自有文件，不先创建完整匿名 CSR。每区间块完成全部 $A/B/P$ 和列位置后，再 flush 与逐页建议回收。完整 indptr 以有界整数块填写；不保旧完整 COO 索引副本。

`release_inputs()` 在一个完整区间块写完后调用，供 provider 刷新真实中点参数写入并释放四个输入映射的驻留页；它不删除完整输入文件。输入仍保原 C-order strides，不能将文件布局变化偷当算法变化。

输出以 `csr_matrix(..., copy=False)` 构造，并核三阵都共享同一 backing。保存完整三个数组的逐块 SHA；所有数组哈希都按块读取和释放页，不建立第二份大数组。`AssembledCSRStore` 只保元数据、backing 和矩阵弱引用，不保四个输入偏导数组。矩阵强持 store，store 不强持矩阵；最后矩阵引用消失才清自己唯一 backing。

## 3. 不再复制第二份 CSR 的原 QR 接入

`adopt_store_for_before_qr` 要求真实矩阵正是此分支刚返回的完整 CSR、维数相同、从未被采用/原零压缩，且当前三阵 SHA 仍与组装返回一致。它返回同一个 backing/store，**不再复制整个 CSR**。

`AdoptedBeforeQRMappedBlockQR` 使用与原 `BeforeQRMappedBlockQR.__init__` 同一个 code object，仅把原 CSR-store 构造器显式指向 adopter、factor-store 指向已冻结回收 v3。原 CSR 实例的原 `eliminate_zeros` 仍执行恰一次；实例 `prune` 保原全部检查，只保相同前缀 view；之后全部 mapped arrays readonly。原区间局部性、末端行、QR、缩放、原 solve、全部残差和迭代修正未改。

`adopted_factor_additional_backing_upper_bound` 只估计此时新增的完整 factor/manifest/journal，不再次要求一份 CSR 文件；现有 backing 字节不作为 RAM 信用。较广的即时-record mapper 是独立准备分支，当前 adopter 没有暗中改用它。

## 4. 生命周期、预算和来源

`owned_storage_root(outdir)` 创建独立 `complete-jacobian-storage` 所有权记录；唯一数据目录名为 `complete-jac-csr-*`。该目录内只有 `all-arrays.bin/layout.json`；小 journal 在其同级。`cleanup_joined_child` 只在工具确实观察到子进程终态后清本分支的确切自有目录，原字段/检查点/source 都不在删除域内。旧 factor owner/cleanup 不放宽，本分支的 CSR owner 单独保留。

四个完整偏导输入的逻辑量是 $8n(n+k)(2m-1)$ B。$M=32,n=97,m=1185$ 时为 237146376 B，完整 CSR 预分配为 312283136 B，原 factor/manifest/journal 新增上界为 424174666 B。若三类文件都重叠，加原 512 MiB 外余量及 CSR 16 MiB 小元数据预算共 1527252306 B，另加 provider 的真实页 padding 和小元数据。

只有原 `sys_jac` 返回后，provider 实际观测四输入已无引用、自有 partial 文件确已删除，才可按前后不同阶段取较大者；对应主项为 1290105930 B，仍另付 provider 小余量。这是磁盘生命周期计算，不是 RSS 节省证明。外层仍保真实 RAM/磁盘门和全部科学门，不把 mmap 逻辑长度当可用内存。

## 5. 真实准备回执与待付范围

`held10-analytic-work/complete-streamed-csr-preparation-20261128-a/preparation.json`：compile、`--help`、`--describe` 三次实际 exit 0，2.4727229889995215 s，子进程峰 62380 KiB；原顶层 constructor code identity 与 solve identity 均为真。没有构造测试矩阵或 BVP。

design 负责实际原批次 provider/driver，以及从真 97ec 场取得的一个小完整块输入，统一比较全部 $dY/dP$、CSR 三阵、原参数中点副作用、原零压缩及必要的原方向。该检查和下一完整求解的真实结果不得预先写成已付，也不得从这里推出原非线性问题的可解性或不可能性。
