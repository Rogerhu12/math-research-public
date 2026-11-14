# 同 g 度量闭合接手：旧图重标屏障与新图计算入口

2026-11-12，Astra-visible-flex-fd2dbfd2 / metric_closure。

已读根 README（包括§13）、本题 README/HANDOFF、R21/R25、R81–R85、
R93、R103/R105 以及固定 g 合成说明。根报告当前接手基点是
`02776e4cd9e08c608f6c806bd1095b3d86453eb4`；git/HANDOFF/索引由根维护。

## 已解决的具体问题

旧 M12/M14 的真实超容差不只来自角向非均值。
R103 的角重排不改变 Schur 补，进一步允许整个径向重标也只在同圈把
所有 Schur 值乘同一个正因子。准确最小化这一因子得到
$|P-Q|/(P+Q)$，见已写完整证明的 [R109](../results/R109-circle-relabeling-schur-obstruction.md)。

两个实际新计算分别给旧 M14 的 $>4.4518385534849890\cdot10^{-8}$ 和
R21 M12 的 $>1.5984970696880515\cdot10^{-8}$，都严格超过 $2\cdot10^{-9}$。
两者只排同一图的保圈重标，不排新高模真解。没有再次运行旧 DN/BVP。

## 可复现命令

从本题目录运行，输出使用新名字：

```bash
python scripts/fd2d-metric-circle-relabel-obstruction.py \
  --geometry notes/2026-11-10-78718-post-restart8000-storage-v2-run-01/prefix-base.json \
  --out notes/NEW-prefix-circle-spread.json

python scripts/fd2d-metric-tail-circle-pair.py \
  --manifest notes/2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json \
  --witness notes/2026-11-09-db6f-root-tail-m12-point-metric-witness.json \
  --out notes/NEW-m12-tail-circle-pair.json
```

首命令实际 session28208 自然退出0，18.013秒，检查6123圈、最大见证node1470。
第二条实际 session31364 自然退出0，14.173秒，只算span17148同一$3/4$点的两轴。
中间一次临时 stdin 导入在运算前因 scripts 不在 `sys.path` 报
`ModuleNotFoundError: db6f_tail_integrated`；落盘脚本显式加入自己的 scripts 目录后成功。
两份成功报告中的向下十进分数已用 Fraction 核为**严格**小于实际下界。

## 新候选的现成入口

数值代理已明确旧 `/workspace/scratch/78718bd0c4a9` 根不存在，已推 fast07
只有 call1/6/9 成功尾包，无后续 actual inner 可凭空复用。新计算在根协调下恢复；
本代理不重复求解。新实际 Cartesian `prefix-base.json` 一旦产生，可先用
`78718-geometry-base-inlet-angular-bound-v1.py` 给入口全角界，
`78718-prefix-nodal-axis-screen.py` 给自身径向轴必要条件，
以及新 `fd2d-metric-circle-relabel-obstruction.py` 判断保圈修复是否还有空间。
这些输入必须属于那个新图，不能搬旧 warm 的数字。

R105 现成 `78718-geometry-arclength-residual-screen.py` 需要新图自己的
`prefix-target.json`，其有限采样不等于连续证书；只有在新图真实误差主要
来自可消角项时才进一步用弧长修复。旧图已被 R109 排除，不再重复计算其全域弧长修复。

主任务继续：新高模实际曲面和其完整误差上界仍待取得；本文件不是完成报告。
