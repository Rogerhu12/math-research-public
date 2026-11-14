# 第 67 轮：同 actual64 / 二十查询模型的单值阻尼 27 接口

- 作者：exact_refinement；FD 与只读 observer 薄入口由 amplitude 提供。
- 日期：2026-11-14（UTC）
- 类型：独立源码与运行接口；本说明不包含尚未发生的第 67 轮数值结论。

## 1. 明确的实验对象

第 67 轮与第 66 轮从同一个 actual64 父 warm/status 出发，使用相同完整二十查询 B、相同 6,763 维局部声明布局、相同原完整物理方程和算法预算。唯一声明的算法参数变化是阻尼由 270 改为 27。

这不是扫描，也不是从第 66 轮新 warm 续接。实际第 65 轮已经表明：旧第 63 轮目标 row 的小响应在完整未约束阻尼中心中存在，B 校正对该 row 很小；但全中心违反 2,802 条 B 行。因此本次保留完整 B，并将改变阻尼当作一个需要真实回执的单值实验，没有改善或单行单调保证。

固定父文件：

| 角色 | SHA256 |
|---|---|
| actual64 warm | `3b25ea84dfababece99e1dc098d56cdcebd94737e428e509140e818d48e8eb1e` |
| actual64 status | `037fb9eeaeb196f74976188efb9515736396f2c86a44fde4e93251e92ca01466` |

新 warm schema 为 `exact-constraint-twenty-query-lambda27-condensed-complete-H-warm-v1`。当前入口仅允许这个固定父 pair；没有默许未来 own-schema 续接或使用第 66 轮输出的分支。

## 2. 冻结的三份新源码

全部文件在本题 `computations/`：

| 文件 | 字节数 | SHA256 |
|---|---:|---|
| `geometry_20261114_twenty_query_lambda27_condensed_warm.py` | 14,799 | `c425a9576b49e6d97325769470e5fbd1c635248024372fe0c5aac3a9befd3ef5` |
| `geometry_20261114_twenty_query_lambda27_condensed_response.py` | 2,624 | `8416bcb6ed57f1c2042032e22d1e637ed40fac0fbf0d676a6009b91f5535d9d9` |
| `geometry_20261114_twenty_query_lambda27_collocation_observer_warm.py` | 16,748 | `798fafd5fe2163151674a500719d10c5574b9d0c8948701d79a45145faab22ea` |

原二十查询 warm 文件不改，其 SHA 是
`9d750fcba45624f23dbae19ca44fded0437f1f5dc15943879cbf046064fe22ee`。
原完整试探引擎不改，其 SHA 是
`7d75a44a2e5a736c68e440ffc1a55533f9ea7aa6bbed4430980dc0ad974b0152`。

原二十查询 domain SHA 仍为
`16157412cbb4af0d01ade0cb3e373413fda175059186ccf17ef3b1d727d27ce1`。
原完整 QR、R270 库、局部 QP 及其它依赖沿原完整 FROZEN/source ledger 逐项绑定。新 wrapper 同时将旧二十查询生产器的完整文件加入自己的依赖，不能仅保一个未绑定的运行时函数名。

## 3. 为什么这是薄入口

新 warm 在 Actions 中读出冻结二十查询生产器的全部七个顶层函数。它把这些函数放入独立私有 global 映射，以便当前 schema、当前源 SHA、SOURCE_NAMES 和 FROZEN 真正属于这个新生产器，原二十查询模块自身不改。

七个函数中，五个函数字节完全保留。只有 `_run_engine` 和 `main` 的两处当前元数据声明被替换：

- 原“lambda、LSMR、projection、17 trials 均不变”的合并声明改为“LSMR、projection、17 trials 不变”，并显式记录单阻尼合同；
- 原“lambda、row/chart weights 均不变”的声明改为“row/chart weights 不变”，并显式记录新阻尼。

原 full-angle `main` 只有四处声明/入口限制改变：默认 damping、固定实验值比较、错误说明、intent 的 damping_model 文本。它们从 270 对应到 27。所有其它数值及原非线性试探语句都能通过这四处逆替换逐字恢复。

新的 engine 函数仍使用原 engine 的 live global 映射，因此原二十查询入口安装的完整 B、observer、linearization 和 selector 回调仍实际生效。临时 `engine.main` 在外层 `finally` 中恢复；原二十查询生产器自己的 callback/global 恢复范围保持。

源码变换在本地只做 AST、字符串计数和逐字逆变换核验，没有导入科学模块或执行任何被提取的科学函数。完整 source-only receipt 文件为 `lambda27-source-only-static-receipt.json`，4,948 B，SHA `a6b5ffe2f75687a9def2cb3655c7ea0adcceda7f972b2ce483bd33c84bf161eb`。实际 Actions 还会生成当前 source/父身份绑定的 `single-damping-source-binding.json`。

## 4. 完整模型与 C/QR/局部根

方向仍使用原完整 236,036 维模型，

$$
\frac12\|Az+b\|^2+\frac12\lambda^2\|z\|^2,
\qquad g=A^Tb,
\qquad Bz\ge-c.
$$

完整 g 没有被省略。B 仍包含原 20 组、每组 2,048 个角，共 40,960 行。实际查询端点为 467…483、485、486；R270 的声明局部布局是完整节点 467…486 加三个全局 p，共 6,763 维。节点 484 是显式零 B 列块，但保留完整 H 耦合与自由响应，不固定为零。原 baseline C 投影仍只修节点 471…482+p 的 4,059 个坐标，保留全部 outside 原始贡献。

C 继续按原完整列公式

$$
C_j=\sqrt{\|A_{:j}\|_2^2+\lambda^2}
$$

重建。故 C 在本次并不与 C270 字节相同；完整平方根 QR 和 R270 局部 root 也重新生成，不能复用旧 270 的 factor/root。

完整 A/b/g/B/Wr/S 在同基点及同查询数学下预期相同，但这必须由实际第 66/67 轮原件读回比较。完整 B/model 的元数据 SHA 可能因为新 producer/source provenance 而改变；该变化不能单独证明科学 B 数组改变，也不新增跨运行接受门。

## 5. 原预算和原非线性门

本次入口将第 66 轮声明的实验参数显式固定为：

- 一个模型、LSMR 最大 200 次、原 baseline projection 最大 200 sweeps；
- 局部 QP 最大 512 working rows、200 dual sweeps；
- condensed budget 600 秒，原 trial reserve 90 秒，完整恢复 reserve 30 秒；
- 总预算 1,200 秒，原 17 档试探，原角网格 4,096，Jacobian workers 2；
- 保留完整局部 root 输出。

这些是该单参数对照的输入范围，不是新科学接受阈值。原模型残差、B/slack、真实节点和中点域、原完整 RMS/BC、原 merit 下降、预测比率、独立方向核验和后续真实 FD 全部沿原代码。

阻尼罚项仍不加入真实非线性 merit。完整 H 候选与原 C 候选必须按相同的新阻尼目标比较。候选失败或预算终止仍沿原 C 后备路径，不能借新入口制造接受状态。

## 6. 具体 CLI

从第 66 轮相同公开输入准备流程取得 accepted、prepared、真实 T112 affine anchor/config 及 actual64 两个原文件。使用只读 collocation observer 包裹新数学入口：

```bash
python computations/geometry_20261114_twenty_query_lambda27_collocation_observer_warm.py \
  --accepted "$VISIBLE_ACCEPTED" \
  --prepared "$VISIBLE_PREPARED112" \
  --tail-anchor "$VISIBLE_ZERO112_ANCHOR" \
  --tail-config "$VISIBLE_TAIL_CONFIG" \
  --resume "$ACTUAL64_WARM" \
  --expected-resume-sha 3b25ea84dfababece99e1dc098d56cdcebd94737e428e509140e818d48e8eb1e \
  --parent-status "$ACTUAL64_STATUS" \
  --expected-parent-status-sha 037fb9eeaeb196f74976188efb9515736396f2c86a44fde4e93251e92ca01466 \
  --out "$VISIBLE_OUT/twenty-lambda27-condensed-warm" \
  --damping 27 --iterations 1 --lsmr-iterations 200 \
  --projection-sweeps 200 --line-search-steps 17 \
  --budget-seconds 1200 --angles 4096 --jac-workers 2 \
  --condensed-budget-seconds 600 \
  --condensed-trial-reserve-seconds 90 \
  --condensed-recovery-reserve-seconds 30 \
  --condensed-max-working 512 --condensed-dual-sweeps 200 \
  --condensed-store-root
```

这里的路径变量只是由原准备步骤提供的真实路径，不是未来身份占位 SHA。独立实际准备与恢复原 78 个公开源的流程沿第 66 轮，`VISIBLE_SOURCE_TOPIC` 同样指向原恢复树。

成功写出 warm 后，先读取原 `driver-status.json` 的实际 `accepted_warm_steps`、`latest_warm_file` 和 `latest_warm_sha256`，使用实际新 warm 做原完整 FD：

```bash
python computations/geometry_20261114_twenty_query_lambda27_condensed_response.py \
  --accepted "$VISIBLE_ACCEPTED" \
  --prepared "$VISIBLE_OUT/twenty-lambda27-condensed-warm/warm-001.json.gz" \
  --tail-anchor "$VISIBLE_ZERO112_ANCHOR" \
  --tail-config "$VISIBLE_TAIL_CONFIG" \
  --out "$VISIBLE_OUT/physical-response" --angles 4096
```

这仍是原完整 affine Rphi FD，原方向、步长、Richardson 与阈值不变。它不是新 native tail solve，也不能将旧 FD success 改标签。

## 7. 原件、元数据和输出

原 warm/source producer 子树逐字保留。新当前身份记录原值 270、新值 27 及两者 binary64 bits、同 actual64 父 pair、源变换身份和完整单参数范围。原来自历史 producer 的 lambda270 信息作为真实历史保留；它不再被描述为当前入口的未变阻尼。

原 `condensed-QP-result.json.gz`、`condensed-QP-summary.json`、完整 array manifest、`condensed-live-model-binding.json`、原 model/direction/trial/observer/warm/status 路径和字段继续输出。本次 binding 和 direction 的实际 damping 应为 27，完整当前 source 身份为本三源。

`condensed-arrays/` 和 `condensed-root/` 继续使用完整 artifact 策略，不能因大文件而省略 g、root、恢复方向或完整 readback。新原 source-binding receipt 是小文本。新 observer 的十二个读数函数与原二十查询版逐 AST 相同；新 FD 的数学正文除当前报告身份键外逐 AST 相同。

## 8. 实际回执应回答的问题

实际第 66/67 轮原报告将给出：同基点原 A/b/g/W/S 与完整 typed B 的数组身份，新 C/factor/root 的实际记录，完整模型方向、可行恢复和同 f 选择，原 17 档真实 trial、最大完整 collocation 行及新 warm FD。

两轮的不同 runtime 时长可能影响各自原预算内的执行进度，应如实读取，不保证所有迭代数相同。模型最优性后验继续沿原 ordinary-float 范围，不因改变阻尼变成区间证书。

本接口没有提前指定第 67 轮结果，也没有承诺降低阻尼会改善 row 155819、接受 alpha 或 full-DN。最终结论只能来自实际原件。
