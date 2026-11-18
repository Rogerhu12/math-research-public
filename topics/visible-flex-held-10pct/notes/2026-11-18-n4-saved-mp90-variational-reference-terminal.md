# n4：保存 MP90 轨迹上的独立全列变分已完成

分类：**数值证据**。这是三个既定 stage 的有限变分参照，不是新的非线性尾求解、连续误差证书或本课题完成候选。

## 1. 真实执行与范围

已发布的 [执行计划](2026-11-18-n4-saved-mp90-variational-reference-plan.md) 使用冻结源 `scripts/resume_closed/frozen_mp90_variational_reference.py`（SHA-256 `a939698dbdd6b2712c42befef492d9b5637856bf3614b004f0a64d28017be22c`）及 plan `d4f43809f46fd06a79ac8afce95431fa13a4009268fe3a59e035db01d0af82b4`。本次只执行该计划一次：实际会话 **72556**、启动 chunk `27f51b`、终态 chunk `25f90d`，真实退出码 **0**。observer 在 **2026-11-18 02:41:25 UTC** 记录子进程退出，总观察时间 `422.59483448999526 s`；数学源计时 `420.5857133850004 s`。

原三段 MP90 的非线性轨迹、所有 root 的近似状态和返回的近似 $L$ 均复用。新工作是在这些保存点上计算显式商法则/链式偏导、独立带主元的 MP LU 线性解，以及沿原四场 RK 轨迹的变分递推。每段有 16 步、64 个已配对的原 root 点；同横坐标的 b、c 场仍是两个独立点。没有重新调用非线性 RHS/root/flow，没有加载 native 库，没有调用 DN 或 BVP。

所求对象是隐式矩方程在**已保存的近似根**处的方程 Jacobian 所定义的变分，并非对有限 Newton 停止决策逐步微分。MP90 轨迹自身也只是有限精度近似；下面的小线性残差不能消除该限制。

## 2. 三个完整 $42\times40$ 矩阵

全部 40 个原 stage 输入方向已保留；输出含前 40 个场分量及两个 mean 行。最后 mean RHS 是冻结系数，所以最后 mean 行的 40 个保存值均为零。完整矩阵以 98 位十进制字符串写入每段检查点和合并 raw，未收入 Git。

|stage|新变分点数|本段秒数|最大条目绝对值|最大缩放线性残差|最小绝对 LU 主元|
|---|---:|---:|---:|---:|---:|
|43|64|137.910580033|$3.66195276533123717\times10^{10}$|$2.9665083384\times10^{-91}$|0.9999038913758602533|
|38|64|133.795960492|$2.63661545100106944\times10^{10}$|$2.8541046970\times10^{-91}$|0.9998236155597815142|
|175|64|148.698962308|$3.88985286428835186\times10^9$|$4.7892194315\times10^{-94}$|0.9999999996535660606|

表中线性量在每个点按

$$
\frac{\max_{ij}|(B X-R)_{ij}|}{1+\max_{ij}|R_{ij}|}
$$

计算，再在本段 64 个点取最大。主元是同一执行中 LU 的实际对角条目最小绝对值；两者都只是有限算术诊断。特别地，主元接近 1 不是矩阵条件数结论，表中条目很大也不单独证明病态。

## 3. 冻结探针 floor 与生产 floor

本次复用的 `capsule-coefficients.json.gz` 的 `root_rules.floor` 是 **0.1**，由原冻结探针直接调用一般 root engine 的默认值形成。绑定的原失败 tail checkpoint `b4356eabf97014127a364ef34b7951a930f4b184d8c6f4c4db83c161b2cbbb5e` 则在 `response.checkpoint.parameters.projectionFloor` 保存 **0.05**，其 `config` 无 `projectionFloor` 键。生产 `createCompactTailShooting` 的参数默认值和冻结探针默认值不同。

这里始终保持原 capsule 的 **0.1** 域检查，未改旧源或原执行。现有三个 stage 的参照及逐位基线仍有其原范围；接入完整生产尾部须另行显式绑定 **0.05**。本条不能被写成已验证整个生产尾的原门。

## 4. 文件、复现与只读终态检查

scratch 根为 `/workspace/scratch/7322d0dee069/closed_work/n4-mp90-variational-reference-v1/`。

|文件|SHA-256|
|---|---|
|`reference-summary.json`|`07e09ac83186987a4622805b3a603efa7d4712e65d44c160ec29b115f646f550`|
|`reference-raw.json.gz`|`4ad1e37379b6ffb98ae173f1176e7e228a8d0658b21e6cb9bc6fa08148db4316`|
|`reference-stage-43.json.gz`|`d2bcca448d6b5a721798dd59504b8ae2c017e11f6cd2970341140ffcde4f9023`|
|`reference-stage-38.json.gz`|`15bbb8439fec588ed055f5136ff1c5be62bce988a66bfe4aa1adda6f5a1df920`|
|`reference-stage-175.json.gz`|`dc7e621e4b3bcbd9acdde6faf10f1e775e4cbc1516f9d2421f383abe961b22f1`|
|`resource.json`|`803d799873ccadfc95b937b935b91d660549a80d8381a4d130cd345e383e399f`|
|`process.log`|`a5b2f3ad872a07a25fb7f2db5c4811e6e463e1d271d70e2aa352f3934701c2e1`|

实际数学命令及 observer 命令完整保存在 `launch-command.json`（SHA-256 `8f39eecc608d0ec0364c8a895082982ef6ff8e80d11f46bcf1dc8e3efa2dd1cc`）。执行源拒绝覆盖已有输出；不为核对本条重跑导数或流。

新只读 collector `scripts/resume_closed/record_frozen_mp90_variational_reference.py` 的 SHA-256 是 `61d34212aa3eba2ef2851f7bc92fb9a4c1ec21a46df304293adec9c9e27f7e47`。它核对 39 个研究源、87 个 mpmath 源、原 6 项引用、完整日志顺序、3 个检查点/合并 raw 的一致性、全部 5040 个保存数的可解析性和矩阵序列哈希；不导入数学执行模块。只读运行 chunk `d1857f` 真实退出 0，`0.096712135 s`，生成 `scripts/resume_closed/frozen_mp90_variational_reference_terminal.json`（SHA-256 `5f09136a446a30fc2870aa384487955d32941c30f6fca2fe79a93d9e33f8aaeb`）。

只读复核命令（输出路径须未存在）：

```bash
python topics/visible-flex-held-10pct/scripts/resume_closed/record_frozen_mp90_variational_reference.py \
  --output /absolute/new/path/mp90-variational-terminal.json
```

此处尚未完成 native 全列对照。随后应只读取已保存的 native 与 MP 矩阵，保留原输入列坐标，物理输出只对 $\pi$ 行除 `portRatio`，并分别报告两 mean 行；不得把逐项有限差异自动升级为 DN 验收或连续误差界。
