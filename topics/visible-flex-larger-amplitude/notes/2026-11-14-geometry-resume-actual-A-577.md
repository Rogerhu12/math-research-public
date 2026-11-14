# 已接受 A 的全部 577 个实际尾节点已读出

作者：geometry_design，AI 辅助，2026-11-14。

**状态：新数值读出实际完成；这不是新的闭曲面解或严格连续误差结论。**

## 本次完成的计算

从原已接受 A 的完整 M32、576 段 shooting 状态、原完整 J 和原有均值增量出发，重新评价全部 577 个径向节点、每节点原有 512 个角节点，输出 Cartesian 位置、一阶 jet 和竖向二阶 jet 的全部 12 列。输入 A 的 SHA256 仍为 `917d859e8a73fa663db1839e354909ae4f174bad1895f8717c20705cdd702aaf`。

这次实际运行由既有 owned wrapper 观察到正常退出 0；墙钟 69.461338471 秒，峰值 RSS 181532 KiB。程序 4411 项原输入、数值布局和源身份检查全部通过，完成节点序号正好为 0 至 576。新的点根调用 1154 次、RHS 577 次；没有新 RK、ODE flow、shooting/BVP Newton 或变分 flow，点根内部 Newton 按原公式执行。

| 有限节点上的诊断 | 数值 |
| --- | ---: |
| 原点公式最大相对度量算子误差 | $1.4786489140807087\times10^{-16}$ |
| 形式竖向曲率最大值 | $7.993491041955345$ |
| 最大点根相对残差 | $7.742832390102141\times10^{-14}$ |
| 最大 Darboux 残差 | $3.5743543629857207\times10^{-12}$ |
| 原递增 stage 顺序的完整均值高度 | $0.022683979296285784$ |

径向节点从 `0.30000000000000004` 严格递减至 `0.05056158669090205`，576 个间距均为正；最小间距约 $6.0281831207\times10^{-8}$，最大间距约 $0.0180671104073$。这消除了先前未实际检验的重复半径或倒序疑问，允许按 R230 建立有限分段场，但本次没有据此宣称连续插值度量误差通过。

完整结果 `geometry-work/tailnodes-r2/nodes/complete.json` 的 SHA256 和小摘要见 [577-node summary](2026-11-14-geometry-resume-actual-A-577-summary.json)。577 个压缩数值节点合计 14967739 字节，可由下述固定源码和输入重新产生，不新增上传廉价大表。

## 修正的实际入口错误

第一次实际运行在读入源清单后退出 1，尚未计算新节点。原 reader 把 `source-dependencies.json` 的所有 91 件源都限制在 `topics/visible-flexible-closed-surface/` 下，但该固定清单还包含 `topics/continuous-flexibility-swarm/...` 等真实依赖。

新副本 [geometry_20261114_actual_A_tail_allnodes_firstjet_readout.mjs](../computations/geometry_20261114_actual_A_tail_allnodes_firstjet_readout.mjs) 只修正这一个路径解析：以实际统一源树根为基准，保留每件清单的完整仓库相对路径、原 SHA256 和字节数核对。数值公式、原输入、误差门、角节点、径向节点及调用限制均未改变。原失败保留在 `geometry-work/tailnodes-r1/owned-resource.json` 和 `owned.log`。

## 复现

先按原 `prepare-source-dependencies.py` 从 revision `869436630c99aa5a68afb55bd8877c826034d117` 恢复91源。本轮统一源树在 `/workspace/scratch/ffc1334c1988/source-dependencies`。随后运行：

```bash
python topics/visible-flex-larger-amplitude/computations/root_actual_A_tail_readout_owned.py \
  --prefix WORK/owned --timeout-seconds 3600 --rss-limit-kib 393216 -- \
node --expose-gc --max-old-space-size=192 \
  topics/visible-flex-larger-amplitude/computations/geometry_20261114_actual_A_tail_allnodes_firstjet_readout.mjs \
  --repo-root REPO \
  --source-topic SOURCES/topics/visible-flexible-closed-surface \
  --first-node 0 --last-node-exclusive 577 --out-dir WORK/nodes
```

`WORK/nodes` 须不存在，以免覆盖实际原件。新源码 SHA256 为 `aa6678f2411b1f4f106b64c75c25a3961cb680d8ba80f23b6218a3694527b0d2`。

## 仍然独立的数学问题

完整均值使用原有限 stage 积分，内节点576为零锚；实际前缀的整体高度和刚体框架还须接回。各节点的有限浮点列不能自动当成相互准确的导数。水平 rr 尚未生成，连续 Hermite/cardinal 场的误差、同一个固定 g 的频率和网格精化、平帽闭合、全闭 D、握持 Hausdorff 振幅以及全部 t 的 reach 均未由这次节点读出推出。尤其当前 A 的核心差仍约 .250638，远未达到整个闭面 .2D。

下一实际工作是用这些新节点建立明确的有限 C2 场并评价径向插值误差，同时继续 R225 完整大核心的短入口和真实增幅设计。
