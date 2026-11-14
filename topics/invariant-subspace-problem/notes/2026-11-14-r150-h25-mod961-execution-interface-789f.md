# R150：H0 保根集多项式的可恢复来源及原十七式模 961 入口

本文件给出下一次唯一有界执行的准确接口。截至冻结时，所有输入已验证、
两份 C++ 均已在每项 `30 秒 / 512 MiB` 内编译成功；**没有执行本入口的数学阶段**。
此前短运行已经完成全部九列 `GQ=NF(v)`，未完成 `VQ`。

## 1. 唯一新执行

```sh
python3 topics/invariant-subspace-problem/notes/2026-11-14-r150-h25-mod961-runner-789f.py \
  --t96-recovery-root RECOVERY \
  --out OUTPUT \
  --seconds 300 \
  --memory-mib 512 \
  --compile-seconds 30
```

默认 `notes-root` 为 runner 所在目录；可显式指定。
`image-inputs`、`selected-inputs` 默认分别为该目录中的
`r150-h25-image-and-vq-prefix-789f/` 与 `r150-h25-selected-inputs-789f/`。
若本次限额未完成，可在后继授权执行中用
`--resume-checkpoint PATH_TO_SOURCE_VQ_CHECKPOINT_BIN` 恢复同一输入的真实数组。
它不能读取旧失败运行中未保存的 `700` 行。

编译和输入解压在数学计时之前。两段实际数学 `source -> original`
共享 `300` 秒；各子进程地址空间上限 `512 MiB`。
每个子进程的 `timeout` 等于共享截止时间实际剩余量，另有
`10` 秒强制终止宽限。大数组原子检查点是执行的一部分，不另放宽数学预算。
最终 SHA、压缩与分片是保存工作，不是重复计算。

## 2. 已完成输入；不重算旧数学

T96 恢复来自 run `43597823809`、artifact `14114364261`，需要真实：

- `reweighted-basis.bin`；
- `nf-normal-forms.bin`、`nf-reduction.bin`；
- `nf-forward.bin`、`nf-backward.bin`；
- `normal-form-input.txt` 或同内容的 `native-normal-form-input.txt`。

所有文件的准确 SHA 固定在 runner 的 `ARTIFACT_INPUTS` 中。
若原 artifact 不含 model，按已有流程从仓库保存的
`native-normal-form-input.txt` 补入；程序仍检查同一 SHA。

已完成的 H0 像商输入如下，全部保原 `2..10` 九目标标签：

| 输入 | 未压缩字节数 | SHA256 |
|---|---:|---|
| `combined-rhs-normal-forms.bin` | 542640 | `581ce943262ba4dea66e9562889ec8cdd62e3808e34a8aeff33afb966c84bdf4` |
| `image-image-quotients.bin` | 806105 | `c3dc4656e8cf56b579913002c4b210775420eeb7870d68993f135965b075a99c` |
| `image-image-remainders.bin` | 110 | `09bc43a84b590f93e885b57ead50f48a4047b2a5498c664d1e4a7a835193dd6a` |

原 `200` 核恢复中只需成本 `85` 的最后两列。配套抽取器没有计算 NF 或
Bockstein，只完整核原文件 SHA 后无损复制选定列及其 trace，保留全部
`6188` 行字典。所选标签严格为
`[2192,2275,85,1241,3485]`、`[2193,2276,85,1242,3497]`。

| 新紧凑输入 | 未压缩字节数 | SHA256 |
|---|---:|---|
| `cost85-selected-original-kernels.bin` | 626592 | `5cf08a41a81647dab8522c84e64de2ea442103063f6d870a820d5dd18bb226c7` |
| `cost85-selected-normal-reduction.bin` | 1258828 | `a489146317d14a3225c864e4b945c5c405b72ebbd03b1e2cbff8ff8dd71b8932` |

两列 trace 分别有 `157334`、`157365` 个真实步骤。紧凑数据 gzip 总计
`1,203,863` 字节。原完整输入的 SHA 和逐文件压缩 SHA 在
`selected-inputs-receipt.json` 中。因此本次无需下载或重建原 `200` 列大恢复。

其他输入均已在仓库：第一原来源 `x0`、第一残差的原预基 trace、
原整数模 `961` 模型，以及既有 bitplane 头文件。runner 逐个验原始 SHA。

## 3. 第一段：真实 VQ、核正规化与原 2195 行身份

新的 `packed-image-source-checkpoint` 保持之前的准确算法：
读取实际 `G=RV`，按每行原首系数同时规范化 `G,V`，对已保存商 `Q`
计算九列 packed 卷积；再用全部 `1174` 个零输出核行正规化来源。
每个原 `2195` 来源的编号、原行、权重都来自同一 T96 字典。

若像行次数为 `d`，原图证明其来源成本至多 `d+96`。本 RHS 参数次数
至多 `86`，故临时来源成本严格有界于 `182`。完整核正规化不增加成本。
原来源权重仍按原模型核对；不假设实际最终成本为 `86`。

最后独立读取全部原 `R`，逐系数核验

\[
RC=NF(v),\qquad
v_j=(s-2)(r_j-c_{1j}b_1-c_{2j}b_2).
\]

成功必须有 final marker `packed-image-source-convolution-complete`、
`fullNormalFormDecompositionIdentity=true`、
`standardKernelNormalForm=true`、`completeRHSInImage=true`。
此时 `originalSeventeenEquationTransported` 仍严格为 `false`。

### 真实检查点

每 `100` 个像行及捕获终止信号后的下一行边界，原子写出：

- 已完成像行数及下一行；
- 所有 `2195` 个原来源的实际 packed 累积数组；
- 原编号、原行、权重、各数组跨度；
- 所有输入 SHA 与来源源码 SHA 导出的统一绑定值。

同一个检查点可跳过已经完成的卷积行。输入或源码绑定不一致时拒绝恢复。
检查点不是核正规形，也不是完整来源恒等式；元数据明确为 `VQ-only`。
一旦满 `1021` 行，其检查点也可供后继只重做核正规化及最终乘回。

## 4. 第二段：原预基补偿和原十七式模 961

记此前实际原来源与 Bockstein 为

\[
r_j=(h_0t_j-Ax_{0,j})/31\bmod31,
\qquad b_i=A\widehat\kappa_i/31\bmod31.
\]

第一段 `C` 使用的原预基补偿为

\[
J_v-HC=(s-2)(J_r-c_1J_{b_1}-c_2J_{b_2})-HC.
\]

程序读取全部 `25,305,683` 个原来源正规化步骤以及原
`1,010,703` 个 backward 和 `782,976` 个 forward 步骤，精确运输到原行。
所得 `z` 仍保完整 `6188` 行字典。临时来源成本上界 `182` 使原系数
次数不超过 `172`，因为最小原行权重为 `10`。

最终原整数模型的候选来源是

\[
X_j=(s-2)(x_{0,j}+c_{1j}\widehat\kappa_1+c_{2j}\widehat\kappa_2)
       +31\widehat z_j\pmod {961}.
\]

`x0` 与两个核使用此前实际保存的 `0..30` 整数代表。
`c1*kappa+c2*kappa` 先作整数运算再模 `961`，不能先模 `31` 丢掉进位。
本段还显式乘以每个原方程的单位 `D/content_i mod961`，保存原有理方程
来源，并逐系数检验该运输与原整数模型相容。

成功必须实际乘回全部原 `6188` 行、全部 `4367` 输出分量和九个目标，
得到 `A_original Y=H0*t mod961`；不能用第一段的正规形式替代。
严格成功 marker 为 `h25-full-original-seventeen-mod961-complete`，并要求：

- `fullOriginalSeventeenEquationIdentityMod961=true`；
- `fullOriginalMacaulayIdentityMod961=true`；
- `originalRowScaleTransportVerified=true`；
- `allWeightedBoundsVerified=true`；
- `characteristicZeroIdentityAsserted=false`。

## 5. 输出和保存

`OUTPUT/results/` 包含两段日志、原生完整回执、总回执、恢复 manifest、
所有实际二进制证书的无损 gzip 及必要分片。任何单片最多
`4,500,000` 字节；manifest 保存每片 SHA、完整压缩流 SHA、未压缩 SHA，
可顺序拼接后解压。没有仅写临时路径而丢弃大证书的分支。

`OUTPUT/recovery/source/` 保留部分或完整 `VQ` 检查点、完整标准来源和
来源回执；`OUTPUT/recovery/original/` 保留实际恢复的原校正 `z mod31`、
原整数模型来源 `X mod961`、原有理十七式来源 `Y mod961` 及原生回执。
无论成功或失败，整个 `OUTPUT` 都应保为 artifact，小结果逐条入库。

即使两段全部成功，也仅得到这个固定 `H0` 的真实模 `961` 证书。
特征零理想包含、全部异常参数及无穷远点仍必须按原任务继续处理。
