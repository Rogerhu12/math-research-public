# R150：四个真实第二 Bockstein 来源的有界连续计算接口

**状态：可复现源码与输入准备完成；新第二 Bockstein 数学尚未执行。**

数学范围见 `2026-11-14-r150-full-first-bockstein-kernel-and-second-interface-789f.md`。本次只先计算四个新核关系作为充分性入口，不把它们称为完整第二像；前 198 个高来源继续保留。

## 1. 唯一一次运行

```bash
python topics/invariant-subspace-problem/notes/2026-11-14-r150-four-second-bockstein-runner-789f.py \
  --notes-root topics/invariant-subspace-problem/notes \
  --t96-recovery /path/to/original-t96-recovery \
  --selected-inputs topics/invariant-subspace-problem/notes/r150-four-second-bockstein-inputs-789f \
  --out /path/to/four-second-bockstein-output \
  --math-seconds 300 --memory-mib 512 --compile-seconds 30
```

需要 `g++`、`python-flint==0.9.0`、GNU `timeout` 与 `prlimit`。T96 来源仍为运行 `43597823809` 的 recovery artifact `14114364261`。原模型文本若不在 artifact，runner 从仓库 `native-normal-form-input.txt` 搜索相同 SHA 的唯一内容。

每个编译阶段分别限 30 秒、512 MiB。输入验证、解压和编译后启动一次共享 300 秒数学计时；每个子阶段只拿实际剩余时间。超时先发 SIGTERM，给保存检查点 10 秒宽限，再强杀。最后无损压缩和清单属于保存步骤，不冒算数学完成。任何退出零仍须匹配该阶段完整 marker、必要真字段和实际输出文件。

## 2. 真正复用的原输入

完整图 SHA256 为 `bb2b36e3b083bf3b66e692f3fdef603941ef3c9c0a1b8fa7a74fad6722fb56ce`；原 2195 来源正常形为 `eeba714c9a9675a8fdac31bf3cd105f50bc5b26de7940301549d903d964d3840`；完整原来源 normal trace 为 `e977b75f618f30d00fd4edca3bdcadba1e5553a956bf4d781ee45df0d15c1e8b`。全部已有图、来源正常形和第一 Bockstein 均不重算。

紧凑输入选择器 `2026-11-14-r150-four-second-bockstein-selected-inputs-789f.py` 从旧 200 列中只读取第 199、200 列，再并上既有最后两列。这里只作逐字节选择和整数存储宽度改变。实际用时 3.2485930350012495 秒，未作新 Bockstein 运算。其五个 gzip 共 2,944,098 字节，每个均小于 5 MB：

| 原内容 | 未压缩 SHA256 |
|---|---|
| 四列原 6188 来源，保标签 2275–2278 | `c6ebd427d59033755a8f9852f64d7509f249727e05c0d62834537aa0a3bdbf7f` |
| 四列第一像的原正常形 | `7f716fd2ed58088c1e8d8d2e4f77771d65d6b039418e884b226991b3a58afdcc` |
| 相同完整 $G$ 的四列商系数 | `934c42fb9979b91743af2d4e66bdcf5ed30f99555ba35aa6cec01a5e33fec667` |
| 四列完整不可约余 | `eec6e8ae82e3bb3581e1817e85a479bc1951d6b819273c1df4bde7e72fbd0cdd` |
| 四列完整原预基约化记录 | `2705394b3744d8a1140edcbf3a269c9739ed6a39a6ceda63cb2cfb3f644922f2` |

完整原输入绑定、选择标签、实际原行映射和压缩 SHA 在 `r150-four-second-bockstein-inputs-789f/selection-receipt.json`。

其余输入直接使用此前落库的实际 $X\bmod961$、实际 $r_2$ 的正常形/商/余/trace、完整第一像、315 状态及原整数模型模 29791。**不重新算 $r_2$，也不重放旧 200 个核方向。** 实际 $X$ 的 SHA 是 `6ff5083ce8567c5a333acb8e26bba9e3bb64a53c5dda8d693c1411b163566e32`。运行时只换统一头，全部原行记录及每个系数原字节保留。

## 3. 四列来源的计算顺序与真实成本

对四个关系 $S_{200},S_{201},S_{202},S_\ell$，原来源成本上界分别为 $86,86,86,87$。原第一像满足

$$
\operatorname{NF}(\beta_i)=GQ_i+\rho_i.
$$

新正常形与种子商先按四个关系线性组合。**只对组合后的 $\rho_i$ 再约化**，补上商系数；全部 $GQ=\operatorname{NF}(A\widehat S/31)$ 会独立逐系数乘回。这样保留旧 $Q_i$，没有重做旧的长 image division。

随后使用真实图源 $V$ 作 $VQ$，再由完整 1174 个真核来源求标准源。图的显式移位给来源成本不超过 $87+96=183$。这一步保存完整 2195 来源，并独立核对原 $RC=\operatorname{NF}(A\widehat S/31)$。接着完整回放 $B(J_{\beta S}-HC)$ 和原前后两个 DAG，恢复真正原 6188 来源 $q_i$；实际成本重新读出，不拿 183 当实际成本。

原整数计算阶段取

$$
K_i^{(2)}=\widehat S_i-31\widehat q_i\pmod{29791}.
$$

所有整数乘法、减法和进位均在模 29791 中完成。每个原输出系数都检查可除 961，再输出

$$
d_i=AK_i^{(2)}/961\pmod{31}.
$$

这同时是四个原模 961 核来源的真身份。$K_i^{(2)}$ 保存其模 29791 代表，保证后续使用的是与 $d_i$ 完全配对的同一来源，不能在中途另取模 961 代表而漏掉下一位进位。

新 $d_i$ 才需要新正常形。该阶段重建的常数预基必须与旧前后 DAG 的 SHA 完全相同；不会重建原 2195 来源正常形。四列的成本至多 183，原正常形和 trace 的一字节参数指数足够。后继九列混合若次数更高，另有 `R150NX31` 的两字节长度格式，不会截断指数。

## 4. 全商判据与同一任务内的后续

四列保留全部 820 标准坐标、全部 505 观测方程，再运输到实际 315 维扭结状态。以完整第一像两列及四个新列生成真正的 $J$ 循环模，直到闭合，并在全部 315 坐标验证 $J$ 不变性。

若某个目标不在此像内，输出完整双证书和四列数据。结论只为这四个来源不足；`remaining198DirectionsComputed=false` 和 `fullSecondBocksteinImageClaimed=false` 始终保留。

若全部九个 $r_{2,j}$ 都在此像内，runner 读取实际多项式 $a_{ij},f_{ij}$，**不停在仿射相容**，继续以下实际来源链：

$$
\bar A z_j=r_{2,j}-\sum_i a_{ij}d_i-\sum_{\lambda=199}^{200}f_{\lambda j}\beta_\lambda,
$$

$$
Y_j=X_j+\sum_i\widehat a_{ij}K_i^{(2)}
+31\sum_\lambda\widehat f_{\lambda j}\widehat K_\lambda
+961\widehat z_j\pmod{29791}.
$$

该余量的 $Q$ 仍复用已保存 $r_2$、新 $d_i$ 和旧 $\beta_i$ 的商，只消组合余。然后第二次实际 $VQ$、完整核约化、完整原预基运输，最后将九列 $Y$ 逐系数乘回全部原 6188 行，并核对原有理十七式的 $D/\operatorname{content}_i$ 单位运输。

Krylov 只在完整 315 空间内选独立列，所以所用多项式指数至多 314。保守取余量成本不超过 $183+315=498$，图源暂时成本不超过 594。实际计算会报告每列真正成本；没有声明此界对移动层或其他参数统一。所有长度均按这一次有穷界分配；每进程地址空间硬限 512 MiB。

## 5. 检查点与输出

输出有三层：`results/` 为小回执与无损证书分片，`recovery/` 为全部实际中间流，`bin/` 为本次编译执行文件。各主要阶段为

1. `relations-image`：四关系 $GQ$ 完整身份。
2. `relations-source`：四列真实 $VQ$ 与原 $RC$ 身份。
3. `relations-original`：四列原 6188 来源 $q_i$。
4. `delta-original`：四个真实 $K_i^{(2)}$ 和除以 961 的全原余。
5. `delta-normal`、`delta-image`：四个真实第二像的完整商记录。
6. `quotient-test`：完整 $J$ 模、九个相容性及正来源多项式或负双证书。
7. 相容后继续 `nine-image`、`nine-source`、`nine-original`、`final-original`。

两次 $VQ$ 都每 100 行、最终 1021 行和捕获的终止边界保存**真实 partial 数组、下一行位置、输入 SHA 绑定**，不是只保存哈希。原内容保留在 `recovery/`；完成阶段还存有输入内容及源代码绑定的缓存。恢复时将旧 recovery 交给 `--resume-recovery`，完整阶段先核所有输出 SHA 后复用；未完成的 $VQ$ 从已保存的真实数组续算。

任何失败都保留实际中间流。大 gzip 按最多 4,500,000 字节无损分片，清单同时含原文件、整压缩流和每片 SHA。不得以“Actions 步骤成功”代替数学 marker。

顶层 `four-second-bockstein-pipeline-receipt.json` 的合法完成分支：

- `status=completed, outcome=four-column-insufficiency-only`：四列已完整计算，部分目标仍不相容；没有排除其他 198 个来源。
- `status=completed, outcome=full-original-mod29791-certificate`：还必须有 `fullOriginalMod29791IdentityVerified=true`，最终原乘回回执中的完整十七式和完整 Macaulay 身份均为真，并附每列实际来源成本。

其他状态均不是完成。即使第二分支成立，也只给一次原有限模身份，特征零的 R150 原理想包含及主课题仍然未闭合。

## 6. 已完成的准备验证

本地以外层 60 秒、每个编译 30 秒、每进程 512 MiB 运行 `--prepare-only`，输入 SHA 全部通过，六个执行文件全部编译成功，分别用时 4.537、6.086、4.815、5.872、4.664、5.361 秒。回执明确为 `prepared-no-mathematics-executed`；无新数学执行。详见 `r150-four-second-bockstein-preparation-789f/`。

完整源码、依赖、输入和小回执的冻结 SHA 见 `2026-11-14-r150-four-second-bockstein-frozen-manifest-789f.json`。原 `forward`、`backward` 的操作计数仍分别为 782976 和 1010703，不把字节数混作操作数。
