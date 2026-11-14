# 新节点的 R230 有限场：连续径向内部采样尚不过度量与曲率门

2026-11-14，geometry_design，AI 辅助。

**状态：实际数值诊断。** 原点公式在577个节点的度量残差接近机器精度，不等于把这些节点作 C2 插值后仍等距。本次明确构造 R230 的未投影有限场，并在原冻结 g 下计算其内部采样；不把数值采样称为严格连续界。

## 对象与执行

位置/径向一阶/竖向二阶采用本轮 `tailnodes-r2` 的全部577节点。水平二阶按 R230 (2.1)–(2.2) 的非均匀共享差分定义；其余按 (3.1)–(3.2) 作五次 Hermite，角方向保留完整512点 cardinal 多项式，包括 Nyquist。圆框 $r(\cos\theta,\sin\theta,0)$ 始终解析保留，避免先相减大圆框造成短径向间隔的消去误差。

固定目标度量直接用原 frozen A 工厂逐点评价，每个原 stage 的 $x=0,1/16,1/8,1/4,3/8,1/2,5/8,3/4,7/8,15/16,1$，共6336径向位置，每处512角节点。角导数从同一 cardinal 多项式计算，没有混用独立保存的角 jet 列。

实际终端退出0，主评价墙钟53.996秒。结果为：

| 量 | 最大采样值/位置 |
| --- | --- |
| 相对度量算子误差 | $8.152721048134474\times10^{-4}$ |
| 度量最坏点 | stage56、$x=.5$、$r=.1814459822220788$、$\theta=0$ |
| 两主曲率绝对值最大值 | $13.168404605384044$ |
| 曲率最坏点 | stage28、$x=.5$、$r=.2816053898916996$、$\theta=0$ |

所以当前这一**明确的有限插值场**尚不能过 $10^{-6}$ 度量门，也不能用节点形式曲率 $7.99349$ 代替它的真实插值曲率。小摘要见 [Hermite metric summary](2026-11-14-geometry-resume-A577-Hermite-metric-summary.json)。这些采样值不是精确极值，更不是精确尾不存在的证据。

最坏点的误差几乎全在径向 $rr$ 度量分量；结合圆框已解析保留，它提示下一次适当的表示应把旋转背景的原高度原函数也保留，仅对非轴扰动作 Hermite。此处这是待计算的修正方向，没有把尚未执行的新表示宣布成功。

## 可复现入口

新增 [background reader](../computations/geometry_20261114_A_tail_metric_background.mjs) 只评价原冻结背景，无新点根或ODE。新增 [finite-field consumer](../computations/geometry_20261114_A577_Hermite_metric.py) 读取真实节点和背景点表，输出完整576 stage 的诊断及最坏点。

```bash
node --expose-gc --max-old-space-size=192 \
  topics/visible-flex-larger-amplitude/computations/geometry_20261114_A_tail_metric_background.mjs \
  --repo-root REPO --source-topic SOURCES/topics/visible-flexible-closed-surface \
  --out WORK/background-samples.json
python topics/visible-flex-larger-amplitude/computations/geometry_20261114_A577_Hermite_metric.py \
  --complete WORK/nodes/complete.json --background WORK/background-samples.json \
  --angles 512 --out WORK/Hermite-metric512.json
```

背景原始 profile 保存的是 `logw`；背景 reader 明确使用原 root 几何同式 $w=\exp(\mathrm{logw})$、$w^2=\exp(2\mathrm{logw})$、$E=1+w^2$。第一次未作此扩展的尝试在 source check 处退出，未产生错误背景表；最终输出绑定原 config SHA。

下一阶段主线仍是 R225 大核心及真实强幅候选。本项保留一个具体未通过的有限场诊断，避免后续误把节点通过当成已经闭合整个尾面。
