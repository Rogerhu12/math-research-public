# 真 full-H 尾的完整 1152 段共享 C² 定义已返回

## 实际对象与范围

本次已经得到完整有限尾，来源仍是新真实 λ=0.002、M24 前缀的全部 raw `candidate_H`，factor=1；不是八轮 coupled 后的 physical H，也不是 λ=1 解。真 full-H shooting 接受包见 `2026-11-28-tail-actual-complete-fullH.md`。

完整 bundle：

`/workspace/scratch/7c4e33ee17de/held10-design-work/tail-fullheight-ulp-geometry-chunks-20261128-b/steps/complete-map-001/geometry-bundle.json`

SHA256：`3b312be557d67cda05624e41d46266925fbe3836c48759c613ede6cf52c70b98`。

所有 1,152 段均有真实 stage 文件；保原 N512 所定义的完整 Fourier 表示，平面 degree 254、170 个平面模与25个高度模。完整 manifest 中1124段各17个节点、28段各18个节点，准确总数为18,460个 quintic span。额外28个 stationary 节点由原 exporter 已经插入，原全谱/两jet校验始终包括它们；此前18,432是误用统一16-span乘法的摘要计数，现按真实 manifest 更正，场和已付证书没有改。完整索引实际检查了1,153个唯一边界节点及1,151处相邻完整 Cartesian 两jet，保留同一个原始全局 cumulative mean；未丢模、未重置 mean。

## 已完成段的恢复与真实工程退出

原 stage0 文件和原 stage0 证书均保留原字节；原首次导出留下的89段与上一真实完成的16段共同作为105段内侧后缀，未重算。新独立 v2 共真实导出余下1,046段，177个新原子进程正常返回。另有两次原 Node 子进程 −9：第19批保留758..749共10段，第47批保留532..526共7段；仅保其实际完整已登记文件，并把后续批量依次缩为8、4，未将 −9 记成数学失败。最终两个部分包的真实原状态仍保留。

观测到的 `RUSAGE_CHILDREN.ru_maxrss` 最大值为366128 KiB；这是已退出子进程的累计最大单进程量，不是同时驻留总量的证明。

## 真实 anchor 来源，不能照抄旧描述

原 `Pipeline.merge_maps` 确实执行了完整合并，因此 bundle 的 producer 仍是该未改动原函数。其 inherited `construction` 字符串仍称 stage0 为 “sole explicit anchor”；**这个旧字符串不足以描述本次分批执行来源**。独立、绑定完整 bundle SHA 的实际组装记录是：

`/workspace/scratch/7c4e33ee17de/held10-design-work/tail-fullheight-ulp-geometry-chunks-20261128-b/complete-map-assembly-observation.json`

SHA256：`319086f04a628d76dfc453ecdb3be91e3246df98bbcadada999f64049c72fb80`。

该记录逐一冻结181个实际来源 component manifest、179份实际 anchor 输入及两次新 −9 终态。每个额外 anchor 都来自同一场上一批真实已保存的公共节点，并非引入另一个独立场或任意新边界值。全部组件 stage refs 与最终 manifest 逐项相同，所有跨批两jet由原最终索引再核；没有为了改描述而覆写原 bundle 或活源码。

## 尚未声称的结论

这是完整有限 C² 尾定义的真实返回，尚不是整个尾的连续metric/reach证明，也不是整个闭曲面的完成。原 `seam_certify_tail_geometry_v2.py` 正沿此同一完整 bundle 顺序检查所有剩余段和 deep collar，保原 stage0 证书复用及全部原门。初期已有部分连续上界超过门；超过门的上界不能写成实际误差的下界。后续会保留每个真实证书并针对具体未过项继续处理。

同名 JSON 给出来源、SHA、小标量与真实部分终态；所有 stage 数据和大索引只在 scratch，未进入 Git。
