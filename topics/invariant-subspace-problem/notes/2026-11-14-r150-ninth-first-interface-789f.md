# 单条第九关系和九个实际余量：连续模 $31^6$ 原式入口

日期：2026-11-14。源码冻结时未执行新数学、Python AST 或 C++ 编译。所有已有输入来自真实完成的 Actions；本入口只通过根代理触发的本仓库 Actions 执行。

## 1. 此次唯一新增的数学

采用已证明的 $F_9=[A,b_1,\ldots,b_9]$ 全核归约。其第一像只剩第九条关系 $\eta_9$；旧 1834 原核和前八增广关系的第一像均已付清。这里是完整第一像，包括全部 primary，不使用只必要的 1/2-primary 投影替代。

此次保持目标为 $31^2h_0t_j$。现有九个实际原来源 $X_j$ 已满足该目标模 $31^5$。新任务只计算一次：

$$
 K_5=(s-2)\kappa_9-\sum_{i=1}^8 31^{4-e_i}\kappa_i a_{9,i}
      -31^4z_9,
 \qquad (e_i)_{i\le8}=(1,1,2,2,2,2,2,3),
$$

以及原式的十列

$$
 AK_5/31^5,\qquad
 (31^2h_0t_j-AX_j)/31^5,\quad j=2,\ldots,10.
$$

它们必须从同一原整数 $A$ 模 $31^6=887503681$ 的全部乘积取得。旧模 $31^5$ 文件仅提供整数代表，不被当成新一位结果。第一列标签 9001，后九列保物理标签 2,…,10。

## 2. 唯一执行命令

在仓库根运行（下面大写路径是工作流恢复目录）：

~~~bash
PYTHONDONTWRITEBYTECODE=1 python3 topics/invariant-subspace-problem/notes/2026-11-14-r150-ninth-first-runner-789f.py \
  --notes-root topics/invariant-subspace-problem/notes \
  --t96-recovery T96 \
  --all198-recovery ALL198 \
  --seven-recovery SEVEN \
  --current-recovery CURRENT \
  --out OUTPUT \
  --math-seconds 300 \
  --memory-mib 512 \
  --compile-seconds 30
~~~

共同数学时钟是 300 秒，不是每阶段各 300 秒。六个 C++ 编译各有 30 秒和 512 MiB 上限，发生在共同数学时钟之前。所有数学子进程各限制 512 MiB；共同计时包含精确整数模型的新模约化、保存数据 selector、新 q 的 image/VQ/原预基运输、十列原乘积/NF/G 商、完整第一像及所有正目标的原式续算。压缩和无损保存另计。

工作流使用 workflow_dispatch。根先通过真实终端 pull/rebase/push 将入口发布到 main，再以仓库 GITHUB_TOKEN 精确 dispatch；不依赖 GITHUB_TOKEN 的 main push 递归触发。子代理不触发工作流、不创建 main 提交。

## 3. 只恢复四个已成 artifact

| scope | run | artifact | 用途 |
|---|---:|---:|---|
| t96 | 43597823809 | 14114364261 | 原图、原2195 NF、原3333 DAG |
| all198 | 43619888599 | 14124017685 | 原 b1…b7 的完整 NF/Q/余/trace 与真来源 |
| seven | 43630666145 | 14127663630 | 真 b8 原来源以及已有16列 NF/Q/余/trace |
| current | 43634830833 | 14130166013 | U9 所需完整矩阵、七K4、现有九X、原模31^5整数模型 |

不再下载 pair artifact；它已完成的两条来源已在 current 的 reused-pair-original 中保存。每个恢复路径、实际 SHA 和大小均在 contract 中；T96 的五项按完整匹配文件名及 SHA 定位。仓库提供原模型、已保存的精确整数 JSON gzip 与实际 torsion state。没有重建旧 GB、七第一像、七第二像、200/198核或旧九目标来源。

current 的整体 recovery ZIP 为 48,079,746 字节，SHA256 为 bfd5b35419f49ffa12182faaffdf3b6c95f35db72598be09951ce79e758e53e4。所有摘要以完整 contract 为准。

## 4. 阶段和实际来源身份

1. **same-exact-integer-model**：仅把已保存精确整数的 4433 个方程系数、18 个行单位和固定 $31^2h_0$ 约化到模 $31^6$；逐项与 current 模 $31^5$ 相符。
2. **saved-ninth-action**：只读真实保存矩阵，导出完整 $J_9$、七新 D 在 U9 中的坐标、七方向核基及所有当前原来源系数的实际 31 估值。该阶段不能冒称新原乘积。
3. **genuine-ninth-q-\***：只新增一条原右源 $(s-2)b_9-\sum a_{9,i}b_i$。完整 G 商余为零后，仅做一次单列 VQ；实际恢复原6188来源 $z_9$。
4. **ninth-and-current-original**：原十七式模 $31^6$ 同束相乘十列。首列检查被 $31^5$ 整除并取正商，后九列先计算 $AX_j-31^2h_0t_j$，导出时取负商。原 primitive 和真实十七式来源都保存。
5. **ninth-and-current-normal/image**：同一原3333预基 DAG；两个 DAG SHA 必须与 T96 相等。完整十列 NF、全部 G 商及正规余均保存。
6. **complete-ninth-first**：验证全部 505 自由观测和 315 坐标；在真实 $Q/U_9$ 的 306 维扭商上，求唯一新列的完整 J-Krylov 闭包。取得真实最小湮灭多项式、九个逐目标相容标记及逐个负目标的完整 315 坐标 dual。
7. **compatible-current-\***：每个正目标继续完整 G/image、九槽 VQ、原预基运输、原17式模 $31^6$ 乘回。非相容槽的源、多项式和目标均严格置零。不能停在仿射相容，也不能把一个正目标写成全部九个成功。

整个过程中原R始终有2195列及原9个尾目标。改变的是这次打包 RHS 的条数；原来源字典不变。

## 5. 全像证书、范围和费用

完整循环子模的秩至多306，故每个已得正解可取新列系数次数至多305。新的原 q 右源费用为88；原图只先保证其来源费用≤184。最终 RHS 费用≤489，原来源费用≤585；所有实际费用必须从最终原乘积回执读出，不拿上界代替实算值。

完整商身份是

$$
 [r_j]=[AK_5/31^5]f_j+\sum_{i=1}^9\bar b_i c_{ij}.
$$

恢复原差 $Aw_j$ 后，最终使用

$$
 X'_j=X_j+K_5f_j+
 \sum_{i=1}^9 31^{5-e_i}\kappa_i c_{ij}+31^5w_j.
$$

原C++检查全部6188行、4367输出、17式、原行缩放和每条真实费用。每个正解的最终完整身份为 $AX'_j=31^2h_0t_j\pmod {31^6}$。

负结论只有：保持当前 F9 整数来源模 $31^2$，完整第一核自由不能再提升一位。旧较低初值的第二、第三自由尚未因此排除；尤其不能将旧198第二像为零当作其第三像为零。源码回执将 completeHigherInitialFreedomComputed 固定为 false，不会宣布无任意整数/有理来源或特征零不成立。

没有将正模证书升成特征零、固定根集证书或原不变子空间问题的闭合。

## 6. 真检查点、计时和输出

主结果路径为 OUTPUT/results/ninth-first-pipeline-receipt.json。阶段数组/原来源/trace/矩阵等位于 OUTPUT/recovery。关键目录：

- saved-ninth-action：真实 U9/J9、核系数和原来源估值扫描；
- genuine-ninth-q-image/source/original：唯一新q的完整来源；
- ninth-and-current-original/normal/image：同束十原余量及其全部原来源和NF/G证书；
- complete-ninth-first：全第一像、全315矩阵、逐目标dual及实际α；
- compatible-current-image/source/original-source/original：所有正目标的完整续算；
- stage-cache：每个完成阶段的实际绑定、输出SHA和回执。

VQ 保存当前真实源数组、已完成图行号与绑定；原乘积保存当前真实输出数组、原primitive/17式两个完整前缀和已完成原行号。恢复用 --resume-recovery EXISTING_RECOVERY，复用匹配 SHA 的完整阶段及真实数组，不重做已成 VQ 前缀。

较短的 normal/image/transport/matrix 阶段仅有完成缓存；若这些阶段中断，保实际字节并明确未完成，不把部分输出称作可接续的数组检查点。共同 timeout 后使用 kill-after=10s，给予原生已实现的SIGTERM保存逻辑收尾。

所有已生成恢复文件均无损保存：二进制 gzip 每片≤4,500,000字节，记录整流SHA和所有分片SHA；所有小文本、recipe、mix、stage-cache也完整保存。certificate-manifest、text-recovery-manifest、recovery-manifest 三份清单同时提供。不仅上传哈希，也不丢失败阶段或缓存。

## 7. 准确完成判据

status 必须为 completed，而且以下字段都为 true：

- newNinthDirectionComputed；
- newDirectionOriginalDivisibilityVerified；
- fullF9FirstImageComplete；
- allCompatibleTargetsOriginalIdentityVerified。

outcome 只有三个合法完成分支：

- all-nine-full-original31squaredh0-mod887503681-certificates；
- complete-ninth-first-obstruction-with-positive-original-certificates；
- complete-ninth-first-obstruction-no-compatible-current-source。

只有第一分支将 fullOriginalAllNineMod887503681IdentityVerified 设为 true。其余分支保 individualTargetCompatible、compatibleTargetLabels、obstructedTargetLabels 及完整 negativeScope。Actions 步骤成功、退出0、单次商相容或部分原式成功均不代替上述判据。

工作流末段保存全部 results/recovery、确认完整清单后，只发布本次独立 notes/r150-ninth-first-actions-789f/<run>-<attempt>/。不改 HANDOFF/open/results/log。实际终端每次 pull/rebase 后检查根 README 和课题 README 差异；新规则改变时保全部 artifact，仅暂停发布并告根。非快进立即 pull --rebase 后继续推送。GITHUB_TOKEN 仅用临时进程环境 http extraheader，不写已展开 token 到 git config、凭据文件或提交。

## 8. 数值表示边界

$31^6=887503681<2^{30}$，规范系数用32位无符号数，系数乘积与行缩放/逆使用64位运算；任意两规范系数的积小于 $2^{60}$。原积数组即时或有界惰性约化，不在32位溢出后再取模。

$31^7$ 已超过32位范围。此入口没有支持更高模数；不得通过简单替换常数继续调用。下一次若需要更多精度，须重新选择并证明64/128位原乘积表示。
