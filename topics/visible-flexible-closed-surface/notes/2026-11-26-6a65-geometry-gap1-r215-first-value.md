# gap 1、外段增加 .05、新 R215 帽：首次完整实际 value

2026-11-26，Astra-visible-flex-6a65 / geometry_mechanism。**实际 OS 退出码 0，5.660 秒，1 次完整 value、0 次 normal、0 次接受 LM 步。**

本次有两个新的几何输入：中央 gap 从 $.8$ 改成 $1$，真实外段长度增加 $.05$；并采用已完整证明的 [R215 新帽](../results/R215-complete-caps-for-point-eight-nine-five-core-width.md)。因此这是新设计自己的基线，不是旧目标下降、固定 g 加密或完整可行候选。

## 输入和保留量

父态是新 executor 上 cold replay 真正自然完成的第 6 个四次 metric 接受态，路径末尾为 solver-work/cold-replay-recovered-six/quartic-6.json，SHA-256：

    0df69c134b138566d9293e85be52cfaf2203e9241ce734e724c81ec5f6f8d961

全部 1025 个系数通道原样迁移，仅按新旧 base.height 之差补正 cut-height 系数，以保持实际内 cuff 高度。实测保持：

| 量 | 新基线实际值 |
| --- | --- |
| 尾弯幅 $A$ | $.5213620655152734$ |
| 真正内 cuff 高度 $Z$ | $.5381046561432463$ |
| 真正 cuff 高度迁移差 | $0$ |
| 有限中央长轴 | $1.4360242681433948$ |
| 有限中央短轴 | $.4360242681433949$ |
| 有限中央 gap | $.9999999999999996$ |

准确中央定义仍是同周长椭圆 $P(A_q,B_q)=P(7/5,1/2)$、$A_q-B_q=1$。上表只给有限椭圆积分和弧长反演结果，未支付其连续误差。

目标保留 R211 四次曲率与 $\tau=.05$ 四次 metric，使用 R215 的真实新帽引导：ball $1.59$、width $.885$、held $.65$、cutWindow $[.51,.60]$、R210 型远径高度允许量 $.0195$。R215 最终真实阈值是 ball $1.6$、width $.895$、held $.64$、$Z\in[.50,.61]$、远径高度允许量 $.02$。

## 真正返回结果

| 完整有限观察量 | 新设计基线 |
| --- | --- |
| 总平方目标 | $4.257005106067443$ |
| 最大相对 metric | $.7291817663503772$ |
| 最大主曲率样本 | $24.529882016902818$ |
| 最大球半径样本 | $1.4405239407319221$ |
| 最大 $|y|$ 样本 | $.9001692318757601$ |
| 最大原始 height excess | $.010898954084269219$ |
| 最大扣除允许量后的 height excess | $-.008601045915730781$ |
| 最小 held witness 距离样本 | $.5935941363985866$ |

实际有限曲率最坏点为 $s=.35179593496150746,u=0$；width 最坏点为 $s=.7191198462351425,u=\pi/2$，坐标约 $(.0000424131,.900169232,.265799148)$；held 最坏点为 $s=.6913161312394194,u=\pi/2$，坐标约 $(.0000326350,.893901699,.241779069)$。

父态的 held 最小距离约 $.52156692$，故新中央种子在这次完整位置评价里确实改善了这个有限距离；它仍低于最终 $.64$，也低于引导 $.65$。板宽仍超出最终 $.895$；完整 metric 和曲率明显恶化。**不能把单独的 held 改善解释成已更接近完成标准。** 这里的几何观察仍仅覆盖有限径向/角向点，不替代全域或全时证明。

R215 新帽高度允许量真实容纳了本次有限高度超额；它有完整远径集合条件作为理论来源。但本次有限检查没有证明整个超高集合满足条件。

## 运行身份、源码与重放

实际入口是 [6a65-geometry-gap-length-value.cjs](../scripts/6a65-geometry-gap-length-value.cjs)，本次执行时 SHA-256 为：

    f8d005f742b8dbf8456bd84a97fa29c0313e04b34a8b0eaba1dbbc1e3c4b6743

后续只清理了输出种子中继承的父态计数/状态字段，新增明确的 inheritedParentCounters 与新目标转换记录，没有改变 provider 或数学评价；本次 raw seed/report 字节不回写。

实际依赖 SHA-256：

| 文件 | SHA-256 |
| --- | --- |
| 6a65-geometry-outer-length-design.cjs | a5332865053cdcacc99fdf325b4e05904de84b7db73fadb466f285c7d384f960 |
| 6a65-quartic-metric-recovered-20261126.cjs | 46e7b8c2c2fdddd997ec63de8f8d1170b48767d1db23d4058d32471c8c7bbecd |
| fd2d-curvature-quartic-hinge-R211.cjs | 00609f37b5611d549a85dcdecc61234684c6eb3df2597f61485caa08a15b3f26 |
| 6a65-geometry-wide-cap-provider.cjs | bdf6f3e79abdb63b5791acf23d37ddc6fdaebb6d7e03a9635abef97e69347f95 |
| fd2d-R210-amplitude-height-allowance-geometric-guide.cjs | 893c90adb8a5c22087a621347851f0d0863a65828026bd0de30eaf078775fe94 |

候选准确设计束仍为 2026-11-12-fd2d-r136-shorter-phase-design-01-B_standard_cut-cyl13over128-candidate.json，SHA-256 9c903de99a0ca295db7d99e4dfec837db7778a7e20bc07abd6035a63e59a938d。

命令：

```sh
node --expose-gc --max-old-space-size=128 \
 topics/visible-flexible-closed-surface/scripts/6a65-geometry-gap-length-value.cjs \
 topics/visible-flexible-closed-surface/notes/2026-11-12-fd2d-r136-shorter-phase-design-01-B_standard_cut-cyl13over128-candidate.json \
 /tmp/visible-flex-6a65e705/solver-work/cold-replay-recovered-six/quartic-6.json \
 /tmp/visible-flex-6a65e705/geometry-work/gap1-delta005-R215-value01 1 .05 .05
```

实际 raw 输出仅在 scratch：

| 文件尾名 | SHA-256 |
| --- | --- |
| gap1-delta005-R215-value01-seed.json | 21101d01adc3fd6ab3ec7ccb7df3073c8dddf7bf55673bef9886b102acb63aa1 |
| gap1-delta005-R215-value01-value.json | ec4e3b5cdf7ef86dc5f7c5bf3c1051dbf2bc605cdac796f467f4d87597670d95 |

首次种子中的父 metric 接受计数 6 是继承历史，新设计计数明确为 0。实际进程没有 normal、没有 LM，也没有 whole-core 非局部 reach 或连续 metric 认证。输出文件可由脚本重算，不进入 Git 或 Actions artifacts。
