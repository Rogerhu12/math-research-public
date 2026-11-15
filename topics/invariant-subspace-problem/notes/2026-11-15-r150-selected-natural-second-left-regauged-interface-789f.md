# 同一所选自然参数第二左 jet：恢复模 31 单位规范，保留两个校正嵌入

作者：Astra-ISP-789f / normal_annihilator。  
AI-assisted，GPT-6 Astra Pro。  
日期：2026-11-15。

**状态。** 这是已完成第二右端之后、于新规范启动前冻结的可执行接口；后续真实结果以同run的实际回执及正式结果稿为准。主程序仅人工读核；本地执行环境不可用，因此不声称本地 AST 或数值检查已完成。旧第一阶精确结果及旧第二右端的实际回执均已在仓库。所有可重算矩阵仅在同一 Actions 会话的临时目录；长期只保存源码、参数、实际 run、小回执和 SHA256。

## 1. 已完成的旧入口与真实停止点

实际运行是 `run43702348535`，步骤 `selected-natural-second-left-unit-pipeline`，执行源码提交为 `ea3ff9d14e123e71846430a25986547a8e24b562`。主线小回执为：

`notes/r150-infinity-remote-session-789f/43702348535-selected-natural-second-left-unit-pipeline.json`。

本次实际数学时间为 1.826085337999757 秒，墙钟为 1.9179355440001018 秒。它完整生成了全部 4354 个原所选来源上的第二右端；在旧校正矩阵恒零的 1736 行上，33 个第二头右端组成的矩阵 $T_{\rm high}$ 的精确有理秩为零。其后实际将旧 $M_0$ 每行除以**仅该行 $M_0$ 系数**的最大公因子，所得模 31 秩为 1545，故按入口规定停在：

`status=completed`，`outcome=mod31-unit-profile-incomplete`。

此前已付的 $\operatorname{rank}_{\mathbb Q}M_0=1546$ 不受这个有限域规范退化影响。本次未调用单位块求解；`fullSelectedSecondConnectionComputed=false`，`selectedSecondConnectionRankExactly9=false`。秩 1545 不能当成有理第二阶障碍，也不能把 $T_{\rm high}=0$ 当成第二阶相容。

两份已完成的临时数据为：

| 旧临时相对路径 | 字节数 | SHA256 |
|---|---:|---|
| `prepared/complete-original-second-left-forcing.json.gz` | 8,998,620 | `8ae7ffef9d7b0a56156f72b002956d4d8843cda66c00b07bff045f9ebd77f4f3` |
| `prepared/complete-old-zero-row-second-head-restriction.json.gz` | 366 | `182f9bd91e7a95bff65f1a579d6a6d0490f869e817bd0e7ae5ba87c706d3114e` |

它们的共同绑定为 `7f7343b09d76063b26020ceaea1031cc450597b3bdf7745cc56b9061b642f632`。新程序锁定上述实际字节；完整 $HF,T$ 不重算、不缩放换义。

## 2. 旧第一阶来源与必须保留的两个嵌入

令 $B(u)=B_0+uB_1+u^2B_2+\cdots$ 是同一原自然参数、同一 $I,J$ 的 $4354$ 阶方阵。原常数余空间维数为 36。以 $\Lambda$ 表示已保存的完整有理左核基，以 $E_{\rm old}$ 表示旧规范的 1546 个校正输出坐标嵌入。

已完成的第一阶整数矩阵 $X,C$ 满足逐原列的精确恒等式

$$
B_0^T E_{\rm old}X+B_1^T\Lambda C=0,
$$

其中 $C$ 的 33 个头独立。以 $F$ 表示补齐这 33 个头的三个原常核坐标，则完整第一阶族为

$$
\lambda_0=\Lambda Cc,\qquad
\lambda_1=E_{\rm old}Xc+\Lambda Ft+\Lambda Cy.
$$

旧入口已经保存

$$
HF=B_1^T\Lambda F,\qquad
T=B_1^TE_{\rm old}X+B_2^T\Lambda C
$$

在全部 4354 个原来源上的整数系数。新程序只更换**第二校正**的坐标嵌入 $E_{\rm new}$，求

$$
M'_0x'_2+HFt+Tc=0,\qquad M'_0=B_0^TE_{\rm new}.
$$

对应的真实第二左 jet 为

$$
\begin{aligned}
\lambda_0&=\Lambda Cc,\\
\lambda_1&=E_{\rm old}Xc+\Lambda Ft+\Lambda Cy,\\
\lambda_2&=E_{\rm new}x'_2+E_{\rm old}Xy+\Lambda e.
\end{aligned}
$$

这里 $y\in\mathbb Q^{33}$、$e\in\mathbb Q^{36}$ 全保留。第二阶中的 $y$ 项恰为

$$
B_1^T\Lambda Cy+B_0^TE_{\rm old}Xy=0.
$$

因此 $X$ 的旧坐标始终由 $E_{\rm old}$ 解释；绝不把其 1546 个数字直接放入 $E_{\rm new}$。源码和每个最终候选都记录两个坐标字典及完整上述公式。

## 3. 从已付完整模 31 常数余空间选择新规范

本轮同一 32 层重建留下的 `complete-selected-cokernel36-field31.json.gz` 包含完整的 $585\times29$ 原低余空间矩阵 $L$ 和 $29\times26$ 缺失三行条件核 $Z$。$L_S=LZ$ 是同一 $I$ 上全部 26 个非纯切向低阶常数左核。

新程序先验证该文件的实际字节与 `rebuilt-first-stage-cache.json` 中的记录相同，并锁定实际第一连接回执：

- 文件：`rebuilt-first/selected-natural-first-connection-f31-receipt.json`；
- 字节数：10,251；
- SHA256：`ba9dd3e9204ec20a7d74310c6414e69d3f00db961051e8ecc88ca90be29743d2`；
- 第一连接绑定：`c11dd73f0b8f469a8c1abee84de0b8ff7a38906a992376a16129a44fcad8607b`。

实际完成门槛包括：

1. $L_S$ 有 26 列满秩，且所选 $I$ 删除的三行全部为零。
2. 对 $L_S^T$ 作模 31 行约化，选取实际 26 个输出坐标 $G'$，核其 $26\times26$ 取值行列式非零。
3. 在同一 $I$ 内、normal 次数为 1 至 3 的全部 1572 个输出坐标中去掉 $G'$，得到 1546 个新坐标 $E_{\rm new}$。
4. 从原 17 式整系数常数项重新构造 $M'_0$；同时核全部 $4354\times26$ 个原来源对 $L_S$ 的模 31 产品为零。
5. 在**未除行公因子**的 $M'_0$ 上选真实模 31 行基，必须得到 1546 行。随后实际核这些行的 $M'_0$ 公因子均不被 31 整除，再核除公因子后的 $1546$ 阶单位块行列式非零。

这些是运行中的实际门槛；本接口不预填其数值。原完整常核只有 10 个纯切向自由坐标和上述 26 个低阶坐标，新规范若通过这些门槛，便在同一个 normal 次数至多 3 的校正支持内恢复了一个模 31 单位补空间。没有换素数，也没有扩展第二校正支持。

正向构造只需实际求解 $M'_0x'_2+HFt+Tc=0$。若要把任意已有 $\lambda_2$ 转到此规范，所差必须作为完整常核 $\Lambda e$ 运输；不能省略旧嵌入与新嵌入之别。程序本轮输出上述明确的正向完整来源公式。

## 4. 单位块、有理解算与完整原乘回

原单位 worker 保持字节不变：

`notes/2026-11-15-r150-selected-second-left-unit-solve-worker-789f.py`。

它的 blob 为 `3caf55504906b0d6f7240c5f54e55f675dde488a`，字节数为 16,244，SHA256 为 `a706713bb49b292c7256aa67b5cb1d75b81003175ef0b87e094e4f0efc03a8a9`。该 worker 此前仅通过 AST，尚无新规范的数学执行。

每个选中行以其 $M'_0$ 系数的最大公因子 $g_i$ 同时除矩阵和右端；右端允许有理数。它使用 Python-flint 0.9.0 的 `solve(...,algorithm="dixon")` 求全部 36 个右端，**先**完整保存每列分子 $N_j$ 与正分母 $D_j$，**后**逐原未除 $g_i$ 的 1546 行验证

$$
M'_{0,R}N_j+D_jR_j=0.
$$

外层继续在全部 4354 个原来源上形成

$$
S_j=M'_0N_j+D_jR_j,\qquad R=[HF,T].
$$

完整 $S$ 的有理核向量 $\gamma$ 给出的原变量是

$$
x'_2=N\gamma,\qquad (t,c)=\operatorname{diag}(D_1,\ldots,D_{36})\gamma.
$$

所以不能把 $\gamma$ 本身误当作原 $t,c$。每个候选先保存完整来源，然后逐原 4354 个来源核对 $M'_0x'_2+HFt+Tc=0$，并核 $c$ 的独立自由坐标。前三个补头的残差秩必须实际为 3；该检查排除了把残差核维数直接当第二头维数的混淆。

已付同一常数 31 单位模型给第二连接的特征零秩下界 9。若完整原式核验产出 24 个独立第二头，则有上界 $33-24=9$，于是此同一所选方阵的真第二连接秩恰为 9。若得到少于 24 个，只完成当前 normal 次数至多 3 的校正族；不得声称完整第二像已计算，也不得否定允许 normal 次数 4 及以上的左校正。

## 5. CLI、输入与恢复

主源码：

`notes/2026-11-15-r150-selected-natural-second-left-regauged-runner-789f.py`  
blob：`2a9d0e7e4a746c9fe0388d0d5de10e14f919e12b`  
字节数：29,455  
SHA256：`785da98d3114adf28b6d85b7f67937e8e277f2fc627bda0427f96a960d72651e`。

同一会话的准确命令为：

```text
python -B {scripts}/2026-11-15-r150-selected-natural-second-left-regauged-runner-789f.py
  --first-out {work}/selected-natural-first-left-envelope
  --rebuild-root {work}/selected-natural-u-rebuilt
  --previous-out {work}/selected-natural-second-left-unit
  --primitive-equations {primitive}
  --unit-worker {scripts}/2026-11-15-r150-selected-second-left-unit-solve-worker-789f.py
  --out {work}/selected-natural-second-left-regauged
  --seconds 300
  --memory-mib 2048
```

这不是新的历史输入下载入口。它使用当前会话的 9 份已付原第一阶输入，加旧 forcing、旧高行回执、重建的 field cokernel、重建第一回执和其 stage cache，共 **14 个实际输入文件**；全部实际字节身份进入新绑定。单位 worker 身份及新主源码身份另入绑定。路径不进入数学绑定，预算不进入数学绑定。

共享数学预算为 300 秒，每进程地址空间上限 2048 MiB。没有编译。准备、实际单位解、全原残差与候选乘回共用同一时钟；时间到保已完成真实文件。完整单位解只要已返回并保存，后续恢复直接读它，不重算解。所有 4354 残差列与最终候选都有按完成列保存的绑定和哈希。

主回执为：

`selected-natural-second-left-regauged-pipeline-receipt.json`。

准备完成的输出为：

- `prepared/same-support-field-unit-gauge.json.gz`；
- `prepared/second-left-m0-unit-input.json.gz`；
- `prepared/prepare-second-left-receipt.json`。

后续目录为 `unit-solve/`、`full-products/`，沿原 worker 和完整原乘回格式。全部大文件只保当前 job 临时目录。退出后可按已提交源码、输入参数及各阶段 SHA 重算，不把这些数组另存 Git、Release 或永久附件。

## 6. 完成定义与范围

最终主要 outcome 为：

| outcome | 准确含义 |
|---|---|
| `same-selected-second-rank-nine-proved` | 24 个独立头与全部原第二左 jet 产品已完成，真第二连接秩恰为 9。 |
| `restricted-second-left-support-only` | 当前 normal 次数至多 3 的完整校正族已计算，独立头少于 24；更高支持仍开。 |
| `checkpointed-time-budget` | 只表示实际时限停止，按保存阶段续接。 |
| `failed-or-incomplete` | 输入、算术或接口未完成，不能报告数学成功。 |

只有第一分支会给 `selectedSecondConnectionRankExactly9=true`、`completeSelectedSecondHeadSpaceProved=true`；须同时读 `all4354OriginalSecondLeftProductsZero`、`allHeadProjectionFreeCoordinatesIndependent` 和 `fullOriginalSecondJetProductCoordinates`。两个完成分支均保留 `oldFirstKernelFreedomDimension=33`、`lastCorrectionKernelFreedomDimension=36` 和 `oldAndNewCorrectionEmbeddingsKeptDistinct=true`。

无论本轮完成分支如何，`leadingUnitProved=false`。第二阶结果不能自动推出整个所选行列式的特征零无穷远长度等于模 31 的 243，也不能推出参数最高系数为 31 单位，更不能作为原九目标的特征零多项式来源证书。
