# 新加速度方向 J 的一般 pure 原式：只消费一条已知候选关系

日期：2026-11-14。**最小后继推导和设计；新研究尚未运行。** 本目标承接 R138 的实际阳性，使用 R136/R133/R131 的已发数据；不展开全部 14 族，不重做 m8，不重建任何响应公式。

## 1. 选择的唯一新方向

[R136](../results/R136-acceleration-coefficient-beyond-response-and-G-orbit.md) 已定义并证明

$$
J=\operatorname{gr}_{-2}
\left([h^{-4}k^0\omega^0(\log h)^0]\bar A_{hh}\right)
\in U\setminus\bigl(R+\operatorname{span}\operatorname{Orb}G\bigr).
\tag{1}
$$

这里 $\operatorname{gr}_{-2}$ 是真 profile 仿射权，不是相位模式。完整 $J$ 同时有 $-4,-2$ 两个相位分量；本轮唯一研究对象是其一般 pure 分量 $J_{-4}$。

原 R136 导出中的 `family_0051_-4` 和 `selected_0000_-4` 是同一个已发原根：

- family `A_hh`，state_key `[-4,0,0,0]`，顺序 $(h,k,\omega,\log h)$；
- 整个状态根自身只有真权 $-2$，无需新投影；
- 80 个原 terms，原 hash `2efefe7d9d902bb0050e4f19fc16b09060216c2376530d920ef265ee9ce96ad3`。

与之配对的 mixed 原根有 317 项，hash `70f565c5c6d7075ec99bc383fc0ee66e914aff06fbc273bc3c1e431123d7c979`；本轮不重新评价或归约该 mixed 根。

## 2. 为什么这个目标仍有用

[R138](../results/R138-general-pure-G-identity-and-affine-orbit-kernel.md) 已证明整个 G 仿射轨道的一般 pure 部分在 $\pi R$ 中，因而

$$
\pi\bigl(R+\operatorname{span}\operatorname{Orb}G\bigr)=\pi R.
$$

但 R136 的完整非成员不自动给 $J_{-4}\notin\pi R$。新 J 可能有一般 pure 响应表示，同时保留一个超出整个 G 轨道的 pure 恒零完整商代表；也可能产生尚未处理的一般 pure 商。

R133 已证明 $\Pi_8 J\in T=\Pi_8 R$。因此其已发准确 packet 可提供一个确定的有限有理候选

$$
\Pi_8J=\sum_{i\in S}a_i\Pi_8C_i,
\qquad C_i\in R_{-2},\ a_i\in\mathbb Q.
\tag{2}
$$

下一问题不是重新求 (2)，而是只检查

$$
\boxed{J_{-4}-\sum_{i\in S}a_i(C_i)_{-4}=0}
\tag{3}
$$

作为任意同右 collar 复 profile 的原算子身份。若 packet 原来就是零，则 S 为空，(3) 进一步缩为原 $J_{-4}=0$；仍必须由原式证明，不能由尾代入推断。

候选固定后，其正确性只由整条原差的 sound 归约决定。旧幂尾系数是选取候选的依据，不作为一般 profile 证明的前提。

## 3. 与 R133 的同一几何系数对齐

R129 的最高导数部分写成

$$
L_4=B_hh_{sss}+B_kk_{sss}+A_{hh}h_{ss}^2+\cdots,
\qquad B_h=\beta_{hh}h_s+\beta_{hk}k_s.
$$

减去 $D_s(B_hh_{ss}+B_kk_{ss})$ 后

$$
\bar A_{hh}=A_{hh}-\beta_{hh}.
\tag{4}
$$

这两项都是 R134 已提取的完整 $v_4$ 原系数。$B_{m_2}N_2$ 只含速度四次，R130 的 $\Gamma(m_2)$ 只含速度二次，均不改 (4)。因此 R133 中的十键

$$
(-4,0,0,0,0,2,0,0,0,0)
$$

恰是本轮 J 的 m8 packet；十键顺序是 $(h,k,\omega,h_s,k_s,h_{ss},k_{ss},\log h,h_{sss},k_{sss})$。不能误取 $h_s^2$ 项或把第三 jet 端势直接当成 J。

已从 R133 完整证书的 `acceleration_quadratic` 几何组只读提取该键，`geometry_coefficient_index=81`。其 `complete_remainder=[]`，`complete_polynomial_difference_zero=true`，固定候选为：

| R116 全局原列 i | 二次索引 | 第三索引 | $a_i$ |
|---:|---:|---:|---|
| 0 | 0 | 0 | `52417629565513761/1575930037032578608` |
| 6 | 6 | 0 | `1097809599290443/196991254629072326` |
| 12 | 4 | 1 | `74015947055645095/37822320888781886592` |
| 13 | 5 | 1 | `164536405113426417/12607440296260628864` |
| 26 | 2 | 3 | `18912999385454629/3151860074065157216` |
| 34 | 2 | 4 | `-6818100659546139/787965018516289304` |

该已发尾多项式有六项，$r$ 次数从 25 到 30、总次数均为 30。上述大有理系数是原证书的确定表示，不把它们改成数值近似，也不先假定它们对一般 profile 有效。

候选来源为 run 43653293263/source 2f0add61f44365d713abf836beaa8b0be2806a3d 的 `notes/actions-43653293263-1-derivative_m8_geometry_ibp/geometry-ibp-certificate.json.gz`，483512 bytes/SHA `a62173b39804ab7f3b0c1f14a23f840a81813717bb8ce88d7659c0e64e90e2f1`，解压 4472950 bytes/SHA `3e0b01e2d7e3ed6634420524ea99ab8d4a9a56c280dd9a2da35365dca02067c7`。本次只解析已发条目，没有执行几何 IBP、代入或旧列消元。

## 4. 全部原响应已经存在，无需生成新列

[R131](../results/R131-third-G-translation-separation-and-111-query-control.md) 的 G³ actual 已保存真权 $-2$ 的完整 E8×W36 **50 个原响应列**，两个模式均在完整 original export 中。R133 的全局列号 i 可唯一还原为

$$
\text{third index}=\lfloor i/8\rfloor,
\qquad\text{quadratic index}=i\bmod8.
$$

按这对真实索引匹配 R131 `column_records`，然后仅使用 (2) 所需的 $-4$ 原根。必须区分 R131 的本权块列号与 R116 的全局 288 列号；不能直接把两个整数索引当作同一列。

每个所需原根按列记录的 `original_mode_sha256` 与 portable DAG 内容 hash 核对。输入保全 50 列只用于原件完整性；本轮不重求 40 维上界、不重验证旧十依赖、不重新评价 N³G，也不把纯投影的维数冒称 40。

因此新增研究只有：从已保存原函数按固定有理 $a_i$ 形成一条原差，再作一次 sound 同右锚 IBP/shuffle。**新 forcing、v4、N 响应、W、响应公式、profile 评价、幂尾代入全部为零。**

## 5. 两份必要原式输入

### J 原根

run 43654534244，source 1177f251dc3d9455adf88b585e4c0e4bd6f7e69b，lane acceleration_layer_mixed。

目录：`notes/actions-43654534244-1-acceleration_layer_mixed`。

| 文件 | bytes | SHA-256 |
|---|---:|---|
| `acceleration-layer-mixed.json` | 57753 | `baccbf48f39a7fb3296ca4e8a933d18f246a8db317423846e66d9c46374b2745` |
| `receipt.json` | 35241 | `3c147ca2edaa03d4c27fa0694adca26764c0f98c8fde363387359d8fddccc494` |
| `acceleration-layer-mixed-original-expressions.json.gz` | 318634 | `b3227509c891a2e86e9bcc7823e3d6b3abb0a9ff80975b2e1162a0911739146e` |
| 上行解压原文 | 1909429 | `7c1e0bda999d2c8958d7e5fdf6d9460f30eb6003eb1c69172ba1ca948dfeac38` |

生产者 `literature_acceleration_layer_mixed.py` 为 47656 bytes，SHA `271dd150fe95d280fdf3cad0f5bbb5b5fde6f81631a96e7fdbfeb628711ebf7c`。schema 是 `visible-flex-complete-acceleration-layer-mixed-v1-original-expressions`；完整导出含 314 组两模式状态根及 10 组已选权根，共 648 roots。

### 真权 −2 原响应

run 43653293263，source 2f0add61f44365d713abf836beaa8b0be2806a3d，lane g_translation_successor。

目录：`notes/actions-43653293263-1-g_translation_successor`。

| 文件 | bytes | SHA-256 |
|---|---:|---|
| `G-third-translation.json` | 25014 | `b183b6815e831b989bca6a09ff3da5818462ed613acfd417a704683106992eb3` |
| `receipt.json` | 34619 | `a7709ce89ca7ead632a13c14ac0c0a5d906ef34c03f22e499952518c807ee523` |
| `G-third-translation-original-expressions.json.gz` | 157782 | `226ea60c21cac82674cd58df491e554eb226431953f4306f0c2c630e1228358e` |
| 上行解压原文 | 889438 | `eb5f3314780df65d36159083a7a498e0945822e0f06f630bc7a1accb179c42a7` |

生产者 `literature_G_translation_successor.py` 为 39670 bytes，SHA `a4583ea776facd4ec4d92a121fed2e79af8de20d57bffc5fa22e47a8026ef406`。schema 是 `visible-flex-G-translation-successor-original-v1-original-expressions`；102 roots 包含全部 50 列两模式和原 N³G 两模式。

两组 main/receipt/run/source/driver、完整压缩与原文 hash、每个原 root 身份必须全部匹配。读取已经完成的原数据；不调用这两个生产者的研究入口。

## 6. 判定和下一层解释

只在本公开 Actions 做真正原式操作。原差在任何归约前完整导出；同锚 normalizer 保全部未消项。

如果 (3) 准确为零，则存在已明确给出的 $C\in R$ 使

$$
J-C\in U\cap\ker\pi,
\qquad[J-C]\ne0\quad\text{于 }U/(R+\operatorname{span}\operatorname{Orb}G).
$$

完整非零来自 R136；新的 pure 阳性并不把该完整方向变成响应成员。J 的真实仿射轨道随后也具有 pure 响应表示，但其实际有符号控制、正性或联合可达性仍须另外支付。

如果 NF 非零，只记录这条候选关系未决。不能因为 R136 的完整非成员就将其自动升级为 pure 非成员；也不能因为 (2) 阳性而删去一般 pure 未消项。根据原余式的具体结构再选择下一必要门，不预先展开全部 50 pure 列或所有 314 状态系数。

上述六个候选系数已经从已发 R133 gzip 提取；新消费者把它们作为明示固定有理配置，数学判定仍仅靠 (3) 的原式证明。无需为了选候选再次载入或重算 R133 大 packet。本设计没有改变任何已发生产者、workflow、状态或结果。

## 7. 已完成的新消费者与公开入口

新源码 `scripts/literature_general_pure_J_identity.py` 为 **24639 bytes**，SHA-256 `ddacad3474844368e3546f4e4b0f92e71eb276363cd283ad4f300259e8161f63`。只复用已冻结的 R138 normalizer/输出工具、五族原件接口和 G³原件接口，不调用任何旧研究入口。

已只读核对 G³原件中的真实映射：

| R116 全局列 | G³本权块列 | 原 pure root |
|---:|---:|---|
| 0 | 0 | `column_000_-4` |
| 6 | 34 | `column_034_-4` |
| 12 | 26 | `column_026_-4` |
| 13 | 30 | `column_030_-4` |
| 26 | 16 | `column_016_-4` |
| 34 | 17 | `column_017_-4` |

新脚本逐项按 `(quadratic_index,third_index)` 匹配并核原根 hash，而不是依靠此表的数字位置。五族的全部 648 原 hash 和响应块全部 102 原 hash 由冻结 decoder 恢复检查；数学操作只涉及上述六列和唯一 J 根。

本地已实际完成语法检查和三项**新**人工接口：区分 global/block 编号、拒绝重复真实算子标签、准确有理符号组合并保留故意加入的未消项。开发报告 **15552 bytes**，SHA `82b96202c59640d04e0135886668dcb30bd40bf2960414e4f3f5d34c26500f90`；三项全过，耗时 0.006781231000786647 秒，RSS 18.25 MiB。没有加载研究原件，没有本地研究，也没有重跑 R138 六旧人工。

只有在 `GITHUB_ACTIONS=true` 且仓库为 `Rogerhu12/math-research-public` 时可运行真正目标。默认 180 秒、RSS polling 1024 MiB、40 万系数节点、10 万 atoms、10 万 terms、25 万 IBP calls。实际 CLI 为：

```bash
python topics/visible-flex-new-mechanism/scripts/literature_general_pure_J_identity.py \
  --family-directory topics/visible-flex-new-mechanism/notes/actions-43654534244-1-acceleration_layer_mixed \
  --response-directory topics/visible-flex-new-mechanism/notes/actions-43653293263-1-g_translation_successor \
  --max-seconds 180 --memory-mib 1024 \
  --output general-pure-J-identity.json
```

两个目录下的全部实际 run/source/main/receipt/export SHA 已作为固定原件身份写在源码；参数只更改文件所在目录，不解除任何来源门。Actions sparse 只需这两个数据目录和现有 scripts；不需要 R133 大 packet、R138 actual 或旧第三模板原目录。

主报告限 90000 bytes。`general-pure-J-identity-certificate.json.gz` 先保存完整 J、六原响应和整条原差八个 roots，再保存完整归约 word；上限 2500000 bytes。超过主限的完整报告可另存 gzip，上限 2000000 bytes，总潜在输出限 4.8 MB。预算退出保原差而不报告数学否定；正常 NF 非零也只报告该候选未决。结果编号由 root 预留为 **R143**，当前没有实际结果。
