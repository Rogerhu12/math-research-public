# Actual57：完整阻尼链的线性读回变小，原非线性试探仍未下降

- 分类：**数值证据**，以及完整保存原件的字节审计。不是精确 PDE/连续几何证明，也不是 accepted native tail。
- 作者：ChatGPT / exact_refinement。
- 日期：2026-11-14（UTC）。
- 本次科学计算：[公开 Actions run 43637356027](https://github.com/Rogerhu12/math-research-public/actions/runs/43637356027)，source `adbdf144b14ae7adc71df09948a5c05f8a30e8b8`，workflow `visible-larger-public-damped-chain.yml`。
- 原科学小报告：[QR summary](public-actions-43637356027-1-dampedchain/native-damped-chain-qr/summary.json)。原十次试探另见 [actual57 trial 结论](2026-11-14-actual57-original-ten-trial-no-decrease.md)。
- 完整字节审计：[summary](actual57-byte-audit/summary.json)、[压缩完整清单](actual57-byte-audit/detail.json.gz)、[方向 IEEE 字分类](actual57-byte-audit/direction-word-classification.json)。

## 1. 实际结果及其对象

本次在 [actual54 的完整新 1372 段原坐标 binary64 J 系统](2026-11-14-actual54-direct-LD1372-solver-and-exact-readback.md) 上，实际执行了 [R273](../results/R273-complete-native-damped-square-root-chain.md) 的完整平方根链，显式取 $\eta=1$。所有原 cut/stage/far 方程、完整 112 个非零模式、原 scales 和每节点一次的阻尼块都保留；没有形成正规矩阵，没有使用 Riccati 显式逆，也没有截秩或额外 ridge。

完整恢复方向后，对保存的新 1372 段原坐标矩阵、原 $r$ 和原 $\sigma$ 的 **307552 行**做了实际 exact dyadic/rational 读回。原尺度最大线性缺陷为：

$$
\frac{699312416480120096786111433487362430967080090584930471835702328725191863}
{172158805543955255640294873119220975642909490522664474650320992189310917312249856}.
$$

原 Actions 给出的显示值为

```text
4.062019449255373658353140097416567722241435168126706612197946812E-9
```

但同一次 Actions 随后把该方向的原 577 节点限制交给原十次非线性试探，十次完整 no-J 求值均返回与原基态完全相同的 norm：`0.04177307820740199`；均记录 `residual-not-decreasing`，没有 native 接受。该原试探事实及其字节审计由独立 trial note 负责。

因此，本次已经得到一个在指定 **新 1372 段有限线性矩阵**上显著减小保存残差的阻尼方向；尚未把这个改善转化成原 576 段非线性函数的下降。不能把两个不同对象的 norm 当作同一个接受量。也不能只依据十次 norm 相同就断言方向为零、试探状态逐位不变，或确定某一个数值机制为唯一原因。

## 2. 固定的输入与实际有限模型

本次直接复用 actual54 已完成的 868 个 direct-longdouble 后一次转 binary64 的单步 J，以及原 actual28 的其余 504 个宏段 J。原 1373 节点基态、全部 $r$、cut/far、$H$、scales 和映射全部原样沿用；没有新的 RHS、J、ODE 步、root 或基态求值。完整输入 binding 与 actual54 逐字段相同，压缩文件 SHA 亦相同：

```text
input-binding.json.gz
32cb5a0b92ab4ce642b65c0b75ba010ff26dcab5cbf77b1b847b5b469ea5279f
```

实际原坐标矩阵 identity 为：

```text
76f30d775c0255dd127b08fa279e59fcaaa4a79a50b72bc7adc8231e436f6999
```

它不是原 actual28 的 576 段有限矩阵，也不是较早 actual41 的原短步矩阵 `e929e642…`。本次所有 exact 读回明确绑定 `76f30d…`，未把新目标冒充旧目标。

方向模型采用 $T_n=\sigma_n I$、$\delta=Tz$：

$$
f_\eta(z)=\tfrac12\lVert W(A_{1372}Tz+r)\rVert_2^2
+\tfrac12\eta^2\lVert z\rVert_2^2,\qquad \eta=1.
$$

实际形成阶段使用原 f64 输入，经 `longdouble` 乘除后一次转 f64，产生有限系数 $V_n$ 和 $\rho_n$；$-I$、cut 的 $[I,0]$、far 的 $[-G,I]$ 使用对应的符号消去。工作类型报告为 `float128`、16 字节存储，但 **有效 significand 为 64 bits**，不冒称 IEEE quad 的 113 位精度，也不声称所形成的权重是精确有理数的正确舍入。

该实际 formed-model identity 为：

```text
9acfd78fe864d48f4fd182c6209802b665ff678f8e365cb19f52598eac14dd43
```

形成阶段记录的非零转 binary64 零次数为 0。这是 underflow 计数，不是所有形成误差为零的证明。

## 3. 完整平方根链与常数项

实际报告和独立保存字节核对支持以下完整结构。

| 项目 | 实际记录 |
|---|---:|
| 段数 | 1372 |
| 节点数 | 1373 |
| 每节点 Q/Pi 分量 | 224 |
| 原方程行数 / 未知数 | 307552 / 307552 |
| 增广最小二乘行数 | 615104 |
| 每节点一次的 $\eta I$ 块 | 1373 |
| QR 调用数 | 2745 |
| 形成系数调用数，含原模型读回 | 2744 |
| 全部保存的纯常数行 | 307552 |
| 因子与常数 raw 总字节数 | 1106785792 |
| 完整三角回代次数 | 1373 |

所有节点均保存 `[R,S,a]`，末节点保存 `[R,a]`；各次正交压缩留下的全部纯常数行也逐项保存。没有只保三角未知量部分而丢弃纯常数能量。字节审计确认全部 R 的数学下三角为字面零，完整因子、affine 列与常数 payload 的 shape/bytes/SHA 均匹配清单。

原报告的最小绝对三角对角元为 `1.1915065260525806`，原字节 `ccdca5256910f33f`。它是原执行的数值读数，不是新增截断阈值，也不单独证明浮点因子的整体精度。

回代报告为 `1.144118585000001` 秒。进度日志在完成第 1372 个 stage front 时记录 `18.068210577000002` 秒，该行位于最终 far front 之前；不能把它无说明地当作包含全部最终工作的独立总计。`factor_summary.elapsed_seconds=67.650068896` 在 finally 中更新，覆盖该对象寿命内的 exact/model 后续读回；完整方向程序 `elapsed_seconds=74.95725455`、最大 RSS `226648 KiB`。这些不同范围保持原义，不相减推导未保存的计时。

## 4. 同一个 formed-model 的原数值读回

以下全部来自 Actions 在同一份 formed f64 系数上用 longdouble 做的完整 A/AT 读回。它们针对恢复前的 $z$；不是独立 interval certificate，也不是原非线性 norm。

| 字段 | 原保存十进制显示 |
|---|---|
| base objective | `0.003420352300689565896` |
| 最终 objective | `3.8972814706899724766e-17` |
| model drop | `0.0034203523006895269232` |
| formed residual L2 norm | `7.2027801975672714756e-09` |
| formed residual infinity norm | `4.0620194492553738307e-09` |
| 全 307552 维未预条件 model gradient L2 norm | `2.0454062922084908859e-06` |
| 因子中变量项平方和 | `4.1847269869525674693e-35` |
| 完整纯常数项平方和 | `7.794562941379949817e-17` |
| formed energy 减 factor energy | `-4.8677879344387386186e-32` |
| 三角因子 residual infinity norm | `3.8302829874839461333e-18` |

小的三角 residual 不替代完整梯度；本次保存了两者。这里也没有用这些显示值自行构造后验误差界，更没有把 model objective 下降解释为原 infinity-norm 必须下降。精确 R273 定理与这组有限精度读数的范围分开。

## 5. 恢复后的方向不是零方向

保存的完整 $z$ 与实际一次 binary64 乘法恢复的 $\delta$ 身份为：

| 保存对象 | SHA-256 |
|---|---|
| 完整 `[1373,224]` scaled $z$ | `39f638be0fc404d1e24b5acfdc7d98dbd39be8e93ba3d5d48a720a22ec3d07a4` |
| 完整 `[1373,224]` 原坐标 $\delta$ | `2c5d9ffdf6caf815e8104c38df8f7e33451db00df0779d5614afab8eabcd6773` |
| 原 `[577,224]` 节点限制 | `5b6e7bb4205ce79c6d0f20b63e491def9747e95a3272e8add1712595ea1c4a85` |

独立 IEEE 字分类直接读取原 raw，不做任何加乘或范数，核得：

| 对象 | 有限非零字 | 正零字 | 负零字 | 有非零字的节点 |
|---|---:|---:|---:|---:|
| 完整 $z$ | 307474 | 39 | 39 | 1373 |
| 完整 $\delta$ | 307474 | 39 | 39 | 1373 |
| 577 节点限制 | 129170 | 39 | 39 | 577 |

这三个对象没有 nonfinite 或非零 subnormal 字。原报告的恢复中“非零 $z$ 变成零 $\delta$”计数为 0，直接配对字分类也吻合。没有用本地乘法重做 $\sigma z$；原恢复舍入仍属于这次有限方向定义。

按已存 `old_to_new` 选择完整 $\delta$ 的字节区间，全部 577 节点逐字等于被送入原 trial 的限制对象；两个完整 checkpoint 及其显式负零列也与 raw 相符。由此可以排除“保存的限制方向本身全为零”这一解释。**不能由这些非零字进一步断言原浮点试探的 $y+\alpha\delta$ 在所有位置都会变化**；本地未形成该射线，也未借 norm 相同反向推断实际状态。

## 6. 全部原坐标 exact 行账

本次 exact oracle 在恢复后的原坐标 raw $\delta$ 上，先精确形成保存数组的

$$
e_n=J_n\delta_{n+1}-\delta_n+r_n
$$

及 cut/far 行，再精确除以实际保存的对应 $\sigma$。它不先将 $J/\sigma$ 或 $r/\sigma$ 转成另一份 f64 matrix，也不把 $\eta$ 行混入原方程缺陷。

实际覆盖 1372 个 stage、全部 307552 行和报告中的 68841584 个原乘积位置。完整账本是 1374 个依次排列的 cut/stage/far 块，压缩 12727955 字节；原 compressed SHA 为：

```text
d8b7dab5ae3143aa609dd64ea1f2809392528180a69a00e8248d068b33c8fb84
```

该账本的所有行均保留紧凑 dyadic 精确表达，不只保存 worst row。独立字节审计完整读了账本的 27026355 个解压字节，SHA 为 `f7091004993460994f1bde58f8f4c6de8b35952aff28ef6d10afdaa8c5d6103a`。审计核了全部行序、sigma/J/direction identity、每个原 maximum 记录在对应行的逐字出现以及 full-report 的复制一致性；没有在本地重新点积、求 Fraction 或重新选最大值。

原保存 maxima 的位置及显示值为：

| 原 exact 项 | 原保存位置 | 原显示值 |
|---|---|---|
| 完整方向全局最大绝对缺陷 | new stage 97 / old stage 8 / step 10 / Q1，全局行 21840 | `4.062019449255373658353140097416567722241435168126706612197946812E-9` |
| cut 最大绝对缺陷 | node 0 / Q1 | `1.169740192381171238186123152519305292972199454213331668818425808E-11` |
| far 最大绝对缺陷 | node 1372 / mode 1 | `3.244012540785489636006597150457854567897035383646942740947128792E-18` |
| 同保存基态 $r$ 的全局 scaled norm | new stage 120 / old stage 10 / step 11 / Pi95 | `4.177307820740198810865391958317089789308602682333899003945437350E-2` |

cut/far 分量并未被事后清零或投影；对应方程仍是阻尼模型中的原行。

全局 worst row 的未缩放精确 dyadic 表达原样保存为：

```text
["0x6552f06d1760cb464f300b4dbe8320804553f7ead6e38f8e198dabddbcb7", -314]
```

对应 sigma 原字节为 `8b69667b2b3bf73c`。其完整 224 个 J 行元素、下一节点全 224 个方向字、当前方向字与原 $r$ 字均已核到原件。该 J 块在 actual54 的 `stage-008-shape-jacobians-000010.f64le`，401408 字节，SHA：

```text
74b74ceb4e3fe73e45dbc682e031413b00c48ae0445e17e352210828efdb557a
```

这里只声称已保存有限数组的 exact residual，不声称这些 J 是原数学 flow 的无误差导数，更不声称得到连续等距或 reach 证书。

## 7. 完整原件审计与可核验身份

本次 artifact 名为 `visible-mainline-dampedchain-43637356027-1`。根唯一下载的 ZIP 为 845612536 字节，SHA：

```text
226227489fb0e4111061ac03c8bfe204a8a53cda16e6bb731d2656569288aec8
```

其中本 note 负责的 `native-damped-chain-qr/` 目录包含 2772 个文件。审计完整核过 2761 个 array descriptor，其中 2760 个 f64 数组及一个全行整数账本；全部 raw payload、gzip CRC、shape、byte count、SHA 与保存的 IEEE 分类吻合。所有 1373 个因子与常数项、9 个原非 J 输入数组、完整/限制方向和两 checkpoint 均包含在范围内。另一目录的原 trial 字节证据由独立 trial note 负责，不重复冒称由本次 factor 审计覆盖。

原输入 binding 与 actual54 完全相同，9 个原非 J 输入数组也与 actual54 原件 SHA 相同。1372 个形成记录的原 J hash、前后 sigma 字及 canonical model identity 全部核对。**formed $V/\rho$ 本身只导出了 hash 清单，未另存全部 payload；本审计核其账本和 source 中重复形成的身份合同，没有在本地重形成系数。** 因子数学精度与 model/gradient 结果仍是原 Actions 的数值报告，不由字节完整性自动证明。

关键结果文件为：

| 文件 | 字节数 | SHA-256 |
|---|---:|---|
| `result.json.gz` | 4712 | `c6feb54847e96778b076076ba17b4ccd666c2548c72f8c36414b2897d176cdc1` |
| `factor-report.json.gz` | 2012 | `cccecf50ac1d448e097eb5c79c43bbad29f214de70fbe3db4803fa5311a14838` |
| `factor-index.json.gz` | 138663 | `bbba3b46e9e324aa2ca2a76ee487ca4087af2ed5a9f53360ccc7e5cd5a63cd0e` |
| `formed-stage-inventory.json.gz` | 200056 | `f49e2c275c5d10ab198a513e09672778c50baf55c4aa1b32403caa021053036f` |
| `exact-original-readback.json.gz` | 423620 | `029897e6e0ceb2e30042252b2260511d2bd263a461e143fe6e787ab80c4b263b` |
| `output-array-manifest.json.gz` | 133187 | `8a77b6b6365562ae3d41b3ff4832576f0bd880f41f2b5ed0a8fdefa86a650401` |

科学 producer 为 `exact_20261114_native_damped_chain_qr.py`，SHA `9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33`。独立 byte auditor SHA 为 `5618d29c41d95d668c959b05cee8295ce4285b2a50961277f557f8cfb717b440`；仅使用标准库的文件 hash、CRC、JSON 相等、索引与 IEEE 字分类，没有 import 或运行数学 producer。

## 8. 下一计算的明确区分

本次已证明到证据层面的事实是：完整阻尼平方根链能够在 `76f30d…` 这份新 1372 段有限矩阵上产生有上述小 exact 缺陷的非零方向；原 576 段非线性试探仍没有下降。它尚未给出该 577 限制方向在 **原 actual28 576 段保存矩阵**上的完整线性缺陷，因此也不能把本次 $4.06\times10^{-9}$ 的值移植到那份矩阵。

据此已选的后继是直接在同一 actual28 原 576 段保存 J/r/scales/cut/far/H 上应用完整 R273、仍显式取 $\eta=1$。同一未来 Actions 中，还将对本次真实 577 限制方向计算原 576 段全部 129248 行 exact 读回，作为同目标比较。两者都不需要新的 RHS/J，也不把线性读回增加为原 trial 的门。

这个后继改变的是线性方向所对应的有限系统，尚未运行的结果不能写入本 note。原 nonlinear 十次 no-J / guard / strict norm 仍裁定该候选是否被接受。当前证据没有给出唯一失败机制，也没有完成课题的固定度量全闭全时族、幅度、reach 或收敛验收。
