# 外部 cell 11 的真实正权积分：正式恢复记录

作者：tail_refinement（GPT-6 Astra Pro，AI-assisted），2026-11-12。

**已完成这个胞元的全部背景范围与五正积分。** 这不是完整径向解或 Darboux 缺陷证书。已得到 5,545 个覆盖整个 cell 11 的真实 source 面板，全部九个源段、17 个 R26 父面板及其准确积分和约束都保留；五个全胞元 R48 积分均有严格正下端。

## 实际执行与退出状态

数学程序是 `computations/tail_outer_positive_moment_panels.py`，本次实际 SHA 为 `d5fb54fe3e0e8db26cabe83fbab6c59ef9f085ce98d2ad26afe9453b50a25d9b`。精度 192 bit，log 范围预算 $1/8$、单一 source $u$ 范围预算 $1/32$，真实 `g`、frozen alpha、cap 分支及全部 R26 输入不变。

第一次 shell 启动因环境没有 `/usr/bin/time` 而退出 127，研究程序尚未启动。随后改用仓库原 `strong_resource_run.py` 的 `wait4` 资源包装，session `18001` 完成数学计算及全部父积分交集，但在最终保存后发现单 gzip 包为 8,082,721 字节，按仓库单文件上限明确退出 1。耗时 37.545 秒，user 5.692 秒，峰 RSS 56,772 KiB，没有 signal。

完整 JSON 保留于本地 `.partial`，SHA 为 `af14424853ec8c6bfe8f60342a49b9b0227088ff90fa72c4de573bc44e22728e`。它没有缺失末尾，也不是中间面板拼凑。**没有重新积分。** 新标准库程序 `tail_outer_compact_completed_panels.py` 把完整结果按原九段拆成各自小于 5 MB 的 gzip，并只删除可重建的 `display` 字符串。

第一次纯序列化 session `20823` 退出 1，是因为核对发现零端点的 Arb union 外舍入使部分积分盒的保存下端略负。真实积分由正密度定义，负的只是有效包围盒下端，不能据此宣称积分负或原包围失效。于是保留全部原数值，把额外守卫改为“区间有序且包含非负值”，而完整总积分及 `w,r_x,r,u_x` 仍要求严格正下端。

第二次纯序列化 session `88345` 正式退出 0：51.610 秒 wall、8.257 秒 user、峰 RSS 15,924 KiB。全部九段重放后，原与新包的**所有非 `display` 字段**逐项 canonical JSON 哈希完全相同：

`970c593945ee3827b8695960ba1c8dcaf306c4c338dc13705bf95fe49d2169cd`。

## 正式结果

主记录是 [cell 11 完整分包 manifest](2026-11-12-tail-outer-positive-moments-cell11-compact-r2-manifest.json)，SHA 为 `ed68183d518c7abf99c84dd0aeab04b559993f9114d1ee153b1d2ca9c3d3fc4b`。

| 原始 source 段 | 完整面板数 | gzip 字节数 |
|---:|---:|---:|
| 0 | 1 | 1,425 |
| 1 | 1,054 | 1,462,058 |
| 2 | 16 | 22,029 |
| 3 | 1,887 | 2,483,360 |
| 4 | 16 | 22,842 |
| 5 | 1,775 | 2,434,095 |
| 6 | 16 | 22,108 |
| 7 | 779 | 1,050,104 |
| 8 | 1 | 1,448 |

总压缩大小 7,499,469 字节，单个最大包 2,483,360 字节。主记录列出每件 SHA、全部 17 个父区间、实际子面板数、精确 dyadic 子宽度和、与原父积分区间的交集。以下七项均真：完整九段覆盖、全部父面板覆盖、父积分和相交、五个总积分严格正、全部必要背景范围严格正、部分积分盒有序、全部非展示值精确保留。

42 个部分积分盒下端略负的情况单独记录。后续 R48 评估可按已证明的非负积分定义相交，但不能在读取时误称原保存值非负。完整总积分未遇到该问题，尤其实际 $I_b>0$ 已支付。

## 恢复命令

若本地完整 `.partial` 尚在，只有如下纯序列化步骤需要执行；须使用新的输出前缀：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python computations/strong_resource_run.py \
  --out notes/2026-11-12-tail-outer-positive-moments-cell11-repack-resource.json -- \
  python computations/tail_outer_compact_completed_panels.py \
  --input notes/2026-11-12-tail-outer-positive-moments-cell11-r1-cell011.json.gz.partial \
  --radius-ledger notes/2026-11-12-root-real-outer-radius-v4-recovered-full.json \
  --out-prefix notes/2026-11-12-tail-outer-positive-moments-cell11-repack \
  --rss-limit-mib 100
```

若执行器丢失，只要九包与 manifest 仍可取得，它们就包含原完整数学数据，不必重新积分。主代理正式发布这些包后可从相应 Git 检查点恢复；本文不把“已落盘”提前写成“已推送”。只有九包也不可用时，按[原算法及命令](2026-11-12-tail-outer-positive-moment-proof-and-plan.md)先真算 cell 11，再分包；不能凭本摘要或哈希补造区间。

下一实际门是把同一 R48 候选接到这些连续面板，恢复完整 mean，并计算全频真实缺陷。当前没有把 13 个端点的角向通过记录改写为整胞元轨道证书，也没有运行 109 locator。此处背景积分与 q003/R39 同 g，可共用；候选场与真头参数域的适用对象仍必须分别核对。
