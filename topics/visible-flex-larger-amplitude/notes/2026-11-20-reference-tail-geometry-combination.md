# R671 新表示的同场几何合并消费者

2026-11-20，Astra-larger-resume-24b2ab87-20261120 / geometry_path。

**状态：已证明接口的完整源码接线；本条没有新的科学执行或新候选数值结论。**
源只消费同一个准确 R671 场的三个公开 Actions 报告，不计算场、不再查询标量 oracle，也不重新覆盖几何域。
它将 [R650](../results/R650-positive-definite-flow-support-reach.md)、
[R661](../results/R661-complete-nonplanar-activity-and-four-fixed-markers.md)、
[R663](../results/R663-complete-closed-embedding-and-fixed-marker-noncongruence.md) 的已有有理组合公式
接到 [R671](../results/R671-exact-reference-tail-affine-lift.md)、
[R674](../results/R674-reference-tail-continuous-profile-and-same-angle-remainders.md)、
[R675](../results/R675-embedded-activity-nonplanarity-from-height-jets.md) 的新表示报告。

## 1. 完整源与实际依赖

新源为
`scripts/resume_20261120/exact_reference_tail_geometry_combine.py`，
SHA256：

`9da689fa2d16ba878e7eac3caf7c33a8d17a2a9940f6d2d6466f8ed536a4ab8f`。

它只从已刊 `actions_closed_geometry_combine.py` 导入 Fraction 端点转换、精确向外十进制显示和文件身份小函数；不调用该源的旧模型消费者。该依赖 SHA256 为

`f61319c27fbbecf3905052d0f0dea81e567900e8757d10fc57d592aa21d08bdb`。

接受的三个报告生产源是：

| 输入 | 完整生产源 | 固定 SHA256 |
|---|---|---|
| first geometry | `exact_reference_tail_interval.py --mode first` | `f1220a2e83578bb186ec1043c5dc5fd70dd988f1a108897537117344590de225` |
| curvature | `exact_reference_tail_interval.py --mode curvature` | 同一 `f1220a2e…` |
| 活动区无平面开片 | `exact_reference_tail_nonplanarity.py` | `b36d387fed072235e1aec8e77da130c9c9be095aed64be46485fc0890b21c09d` |

新 lift 的 canonical factory 源仍为
`exact_reference_tail_lift.py`，SHA256
`2e0219c50543d859a9c649553bc4dde863df24daab26ffa75e5112baa4a90216`。
f122 报告内的原 FullHold / integer / Hold、R657 标量、R670/R672 几何和完整角余项源，以及 canonical dense/batch/observed 身份，逐项与已证明接口匹配。

本源没有覆盖或修改以上已执行字节。本地只做了语法编译与文本调用链核对；没有导入并运行消费者，没有构造或读取新的科学场。

## 2. 同一场与完整覆盖是输入责任

消费者读取实际 bundle 的 H、宽度、R carrier、canonical model JSON 和显式 lambda 标签，并计算实际 bundle、node report 与三个报告的 SHA256。它不读取 q 或计算六 jet。

first 和 curvature 必须同时满足：

- source 是上述 f122，schema 是 `R671-reference-tail-continuous-interval-v1`，mode 分别正确；
- `source_inputs.bundle/node_report.sha256` 对应这次实际文件；
- model JSON 与实际 bundle 完全相等，其 canonical JSON SHA、lambda、M、scalar input、factory 与 operator source 身份一致；
- J 与实际 `true_scalar_nodes` 的长度相同，准确 S/R 盒、H 和宽度一致；
- 全部原胞严格按 `0,...,J-2` 出现在 `covered_cells` 和 `records`，不是一个尾段或一个最坏胞；
- 全模与完整解析角尾已付，旧场证书继承标志为 false；生产环境明确为本公开仓库 Actions。

非平面报告除实际 bundle/node/model 之外，还必须将
`source_inputs.embedding_report.sha256` 绑定到本次传入的 **同一份 first 报告**。
它须实际支付 R675 的完整嵌入前提与全部原胞高 Z 模非零条件，完整见证数为 J−1，覆盖两张镜像活动片，明确排除允许的平帽内部。

lambda 为零时也只接受这套完整 canonical 新报告；不能用旧 eaa/8ca 报告补写新 source 标签。lambda 改变、q/core/H 改变、精化后 mesh/M 改变，或者模型/输入身份改变，都必须重新产生相应实际报告。

R675 当前 b36 源只给其已经证明的高 Z 模充分条件。如果某个原胞高 Z 模六端 jet 全零，消费者将该证明责任保留为未付；不会推断那一胞确有平面开片，也不会自行补用尚未刊出的轴对称尾论证。

## 3. 从完整新场到固定标记闭面

记本次准确未标记闭面报告给出的量为

$$D_0\le D_*,\qquad A_{1/4}F\cdot n\ge\sigma_*,
\qquad |\kappa_i|\le K_*,\qquad \operatorname{dist}(p,S_0)\ge L_*.$$

其中 $A_{1/4}=\operatorname{diag}(1,1,1/4)$，$p$ 是 f122 同场计算的相位见证，仍在 $z=0$。
first 必须给全部原胞的正 E、正法向平方、正支撑、正 core rho 及两张平帽；其完整嵌入标志也必须实际为 true。
曲率必须来自完整原胞的实际第一基本形式计算，零未付正则盒，并包含反射不改绝对主曲率与平帽曲率为零。
无需要求每个报告达到了运行时自行选择的 `.14`、`8.1` 等目标，只消费其实际严格界。

固定标记的输入条件准确为

$$\beta=1/4,\qquad H>1,\qquad R>9/20.$$

取 R661 原有的四张图，上帽中心为 $(a,0,H),(0,a,H),(-a,0,H)$，下帽中心为 $(0,0,-H)$，其中

$$a=3/20,\qquad (b_1,b_2,b_3,b_4)=(1/25,9/200,1/20,11/200),\qquad h=1/1000.$$

在各所属平帽的外法向加准确图

$$u_i(x)=h\left(1-\frac{|x-c_{i,xy}|^2}{b_i^2}\right)^4_+.$$

这是输出报告中明确给定的新帽定义，并非对实际 q 数组做某种隐含改写。
支撑盘互不相交、位于半径 1/5 内、与边缘共同平领保持准确 C²；四个半径互异，中心差向量行列式绝对值为 $4Ha^2>0$。
已有准确组件界为

$$\sigma_{\rm marker}\ge64/267,\qquad K_{\rm marker}\le5.$$

因此对 **同一活动场加这四张实际固定图**，使用

$$D_m=D_*+1/500,\qquad
\sigma_m=\min(\sigma_*,64/267),\qquad
K_m=\max(K_*,5),\qquad L_m=\min(L_*,H-1/1000).$$

最后的 $L_m$ 是沿用旧消费者的保守预算：见证在 $z=0$，新帽离它至少 $H-h$；对当前向外非负图实际上可以取 H，但本接口不需要这项微小收紧。
握持区取上帽半径 9/20 的固定图面，其相反边缘点距离仍为 9/10，且具有相对内部。

标记后的嵌入并非仅从原嵌入自动继承。所有活动片与图帽共同给正支撑 $\sigma_m$、浸入、闭球拓扑和准确 C² 接口，再按 R650 的正定流投影证明标记后的完整闭面嵌入。
原活动片的相位旋转与材料重参数化按 R248，A 与其旋转交换；帽图固定，因此这些输入对全部相位保持，且族在强 C² 拓扑下连续。

## 4. reach、振幅和非全等的准确组合

$A_{1/4}$ 的最大特征值为 1，R650 给

$$r_m=\min(\sigma_m,1/K_m),\qquad
\operatorname{reach}(S_t^{\rm marked})\ge r_m\quad\text{对全部 }t.$$

同场完整见证与固定握持区给

$$\frac{\delta_{\rm hold}}D\ge\frac{L_m}{D_m},\qquad
\frac{\operatorname{diam}F_0(H_{\rm grip})}D\ge\frac{9/10}{D_m},\qquad
\frac{\operatorname{reach}}D\ge\frac{r_m}{D_m}.$$

将 JSON 的每个有限 binary64 端点转换为其 **准确 binary 有理数**，再用 Fraction 完成加减、min/max、倒数、除法及对 $1/5,1/5,3/100$ 的比较；不先转成显示用小数再比较阈值。
报告同时给准确分数和向外二十位十进制显示。

正 Euclidean 商距离另需 R675 的同场活动片无平面开片，以及 $L_m>0$。
四个互异支撑圆与仿射独立中心结合 R238/R661 迫使两个成员间的欧氏全等固定四中心，包含反射分支亦只能是恒等；正见证排除两像相同。
R238 的刚体紧性论证于是给 $\delta_E>0$。消费者不给未经计算的数值 $\delta_E$ 下界。

## 5. 公开 Actions 的完整消费命令

下面命令使用同一个实际 bundle、node report 以及已返回的完整新表示报告。路径由公开请求填写，不使用历史候选 SHA 代替本轮实际值：

```bash
python REPO/topics/visible-flex-larger-amplitude/scripts/resume_20261120/exact_reference_tail_geometry_combine.py \
  --repo REPO \
  --bundle RUNWORK/tail-current/final.npz \
  --node-report RUNWORK/fullclosed_solver/data/fullclosed-hold-warm.json \
  --first-geometry RUNWORK/tail-current/first-geometry.json \
  --curvature RUNWORK/tail-current/curvature.json \
  --nonplanarity RUNWORK/tail-current/activity-nonplanarity.json \
  --out RUNWORK/tail-current/combined-geometry.json
```

first/curvature 的生成参数和完整 source provenance 必须保留在各自报告与原 Actions 请求中；其径向/角向精度可各自不同，只要报告覆盖同一完整准确场。
R675 生成命令为同目录的 `exact_reference_tail_nonplanarity.py --repo REPO --bundle ... --node-report ... --embedding-report ... --out ...`。
固定 dependency 通过当前 checkout 中已刊的小源取得，消费源不下载旧 raw 数据。

缺失或不完整的界、身份不符、标记条件未付、某项比例下界不足都会在 `unpaid_reasons` 留下明确记录；自然返回报告不等于这些条件已经成功。
每次使用新的输出路径，完整 raw 报告留在本次 Actions 工作目录；只发布 source、实际参数、run 和输出 SHA。

## 6. 明确未支付的责任

源的 `metric_certified`、`fixed_metric_refinement_certified`、`topic_completion_certified` 始终为 false。
固定帽图采用其自身共同诱导度量，活动区保留原固定 g；没有声称非零帽图对旧平盘度量仍然等距。
全部等距误差、固定同一度量与参数范围的精化下降、导出网格，以及数值证据与严格存在性之差，仍由各自消费者和求解序列实际支付。
此文件本身也不宣称已经有非零 lambda 候选通过 first、curvature、R675 或三个几何比例。

执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
