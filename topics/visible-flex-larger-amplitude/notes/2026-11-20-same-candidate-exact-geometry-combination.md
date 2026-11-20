# 同候选 R670／R672 的准确 R650 几何合并接口

2026-11-20，Astra-resume-public-20261120 / recover_evidence。

**状态：已证明的现有定理合并接口；没有新增候选应用。** 本文不占 R666，不重复计算任何位置、导数、标量积分或角变换。它把 [R670](../results/R670-direct-same-angle-first-geometry-with-complete-tails.md)、[R672](../results/R672-complete-lowmode-sixjet-curvature-with-laurent-remainders.md) 的同一准确候选报告接入 [R650](../results/R650-positive-definite-flow-support-reach.md)。实际全域曲率／reach 应用仍待当前公开 Actions 返回。

## 1. 消费对象与完整范围

输入是实际 bundle、其准确节点／标量报告、完整首 jet 几何报告及完整曲率报告。两份几何报告必须与当前文件的 bundle SHA、节点报告 SHA 一致，全部原胞索引完整，并绑定各自已证明的源码和依赖。准确 $S,R$ 盒与实际节点报告比较；R672 的完整 scalar identity 与该实际报告逐项一致。$H,w,J,M$ 必须对应同一实际模型。

程序只读取 bundle 的少量字面标量和模型标签，不读取或重建场 jet。$H,w$ 与报告的准确有理值比较；半径 carrier 与准确节点报告的 carrier 对应。原同一数学节点仍是 $\alpha_iS+\gamma_i$，不是把 carrier 的舍入差当作新的准确胞宽。

对于 R671 标签，reference_tail_lambda、exact_tail_lambda，以及 reference_tail_model_json 内的 lambda_value，只要存在就必须一致为0；非零、缺值或冲突不能消费原多项式 lift 证书。已声明的新 R671 表示在 $\lambda=0$ 确实为原算子，允许这一情形。消费者不把同一数组字节但采用不同解析 lift 的两个场视作同一个数学对象。

首 jet 输入可以是原 R670，或另行证明的同候选半径续化报告。后一种报告以自己的真实源码 SHA 标记，保留最初 R670 报告的路径、实际 SHA 和原源码 SHA；消费者核对最初报告确为同一 bundle／节点的完整范围。更紧直径可以合并，而 R672 可继续使用原 R670 的 $E,W^2$ 下界，不需要改写已经运行的源码。

报告未完成或某项条件未付时，输出具体未付原因。曲率报告缺失不抹去已完整支付的首 jet 嵌入、握持和幅度结论；它只使依赖全域曲率的 reach 结论保持未付。这里没有额外独立重跑或人工审查步骤。

## 2. 标记后的同一完整闭族

固定本条使用的工具矩阵

$$
A=\operatorname{diag}(1,1,1/4),\qquad
\lambda_{\max}(A)=1.
$$

设完整首 jet 报告给原场的直径上界 $D_0>0$、统一 $A$ 支持下界 $\sigma_0>0$、固定相位见证到相位0整像的距离下界 $L_0\ge0$。完整曲率报告给实际欧氏主曲率共同上界 $K_0\ge0$。

使用 [R661](../results/R661-complete-nonplanar-activity-and-four-fixed-markers.md) 的同一四个固定 $p^4$ 帽标记：共同高度 $h=1/1000$、圆心和四个互异半径保持原准确参数。在 $H>1,R>9/20$ 时，标记图真实正则、准确 $C^2$ 拼接，且

$$
\sigma_{\rm marker}\ge64/267,\qquad
|\kappa_{\rm marker}|\le5.
$$

因此整个标记后闭族可取

$$
D_* = D_0+2h=D_0+1/500,\qquad
\sigma_*=\min(\sigma_0,64/267),\qquad
K_*=\max(K_0,5). \tag{1}
$$

直径式来自每个点位移至多 $h$，任意点对距离增加至多 $2h$；它不需要原直径最大点的位置。支持与曲率式逐片取最坏界，原平帽及全部接缝也已支付。

原准确端口保证同一闭参数球的 $C^2$ 接合。如果完整首 jet 下界已经给 $W^2>0$，则特别在末圈有

$$
W^2(S,\phi)=R^2\rho(\phi)^2>0.
$$

$\rho$ 连续且全角平均值为1，所以 $\rho>0$。这也可由 R672 的末胞界支付。因而材料角换元正则、平盘图册有效，不要求原 R670 的某个较松直接角盒先独立给正 $\rho$。

由 R650 的正定流投影论证，$\sigma_*>0$ 给完整标记后嵌入。全部活动相位由 R248 的材料换元与水平旋转生成，$A$ 与该旋转交换；帽和标记固定。支持与欧氏曲率保持，已付准确接口给全族强 $C^2$ 连续。这里不需要抽样若干相位代替全 $t$。

## 3. reach、held 与握持比例

将式(1)直接代入 R650，

$$
\operatorname{reach}\ge r_*:=\min\{\sigma_*,K_*^{-1}\}.
$$

所以对实际标记后直径 $D\le D_*$，

$$
\boxed{\frac{\operatorname{reach}}D
\ge \frac{\min(\sigma_*,K_*^{-1})}{D_*}.} \tag{2}
$$

这同时支付局部曲率和全局唯一最近点责任，不能只用 $1/K_*$ 代替 R650 的完整最小值。

原固定见证点位于 $z=0$。未改活动片上的距离下界仍是 $L_0$；标记帽的高度绝对值至少 $H-h$，故一个统一且保守的整像下界为

$$
L_*=\min(L_0,H-h). \tag{3}
$$

原相位公式保证该见证属于相应另一相位的活动像，固定帽标记不改变见证。因此

$$
\boxed{\frac{\delta_{\rm hold}}D\ge\frac{L_*}{D_*}.} \tag{4}
$$

固定握持区仍取上帽 $|x|\le9/20$ 的带标记图，具有相对内点。其边界相反两点位于原平帽部分，距离准确为 $9/10$，所以

$$
\boxed{\frac{\operatorname{diam}F_0(H_{\rm grip})}D
\ge\frac{9/10}{D_*}.} \tag{5}
$$

式(4)、(5)在首 jet 已证明标记后完整嵌入时即可返回，不依赖曲率预算是否已付。式(2)须有同一候选的完整 $K_0$，不从局部界或有限点峰值补齐。

阈值比较准确使用

$$
\frac{\min(\sigma_*,K_*^{-1})}{D_*}\ge\frac3{100},\qquad
\frac{L_*}{D_*}\ge\frac15,\qquad
\frac{9/10}{D_*}\ge\frac15. \tag{6}
$$

若一个已证明下界低于阈值，只说明此界尚未支付目标，不声称真实几何不满足目标。

## 4. 同候选非平面与含反射的严格非全等

原 R670 调用准确非平面系数证明器时已经核对其 bundle 和准确节点报告。消费者读取该同场摘要：源码身份、成功返回、全部原胞数量和无平面开片结论；不重新执行非平面扫描。

在这一非平面输入、完整标记后嵌入以及 $L_*>0$ 下，R661／[R663](../results/R663-complete-closed-embedding-and-fixed-marker-noncongruence.md) 的四个互异半径、仿射独立圆心给 R238 的刚性标记条件。任意欧氏全等，包括反射，必须逐个固定四圆心，所以只能是恒等；正的整像分离见证又排除两像相同。再由 $O(3)$ 与有界平移的紧性，得到严格 $\delta_{\rm E}>0$。

消费者记录原 R670 已报告的嵌入和非全等布尔值，同时按本次已付几何条件给合并后的结论。若非平面摘要未付，reach、held 或握持的有效界仍可保留，只有对应非全等结论保持未付。

## 5. 准确算术与实现范围

源码为 [actions_closed_geometry_combine.py](../scripts/resume_20261120/actions_closed_geometry_combine.py)。

本版源码 SHA-256 为 f61319c27fbbecf3905052d0f0dea81e567900e8757d10fc57d592aa21d08bdb。它绑定原 R670 源 eaa9a579eea227cbf348138295534144c39d07b669ea1c9ff494f22baa4ae599、原 R672 源 8ca81feefda43fd4423bee1877c8e9198c7774afae0cf8cc2227424765dac385，以及独立半径续化源 0faa98e102a5c3ef9c121911313e83f5831474b8be091a161615f000bcbf5369。续化报告保留实际新源码身份，不冒充原 R670 执行。

JSON 中的向外浮点端点由 Python 正常读回 binary64，再用 Fraction(float) 转为那个 binary 数的准确有理值。不能把端点的十进制展示串当作另一个准确几何界，也不消费旧报告已经舍入的比例。式(1)至(6)只用准确有理四则、min/max 和比较；全部标记常数都是准确 Fraction。

输出每个标量的准确分数及由整数除法得到的20位十进制向下／向上表示。两个十进制串只包围该准确报告标量，不代表对真实几何另外得到一条上界。最终目标布尔值完全由准确分数决定，允许等号。

示例调用如下，路径由本次实际公开 Actions 决定：

~~~bash
python topics/visible-flex-larger-amplitude/scripts/resume_20261120/actions_closed_geometry_combine.py \
  --bundle "$WORK/geometry_path/curvature-qp-spectral-hessian-r22-union-next-four.npz" \
  --node-report "$WORK/fullclosed_solver/data/fullclosed-hold-warm.json" \
  --first-geometry "$WORK/postprocess/continue-direct-first-geometry.json" \
  --curvature "$WORK/postprocess/current-full-curvature.json" \
  --out "$WORK/postprocess/current-exact-geometry-combination.json"
~~~

半径续化成功后，--first-geometry 可改为其完整兼容报告；同候选 $K$ 报告无须重算。输出保留实际文件身份、源报告 run、完整／未付范围、所有式(1)至(6)标量、全 $t$ 几何布尔值和未付原因，raw 只留 runner。

源码不进行场值、六 jet、标量 ODE、三角变换或非平面重算。此时仅完成纸面推导与源码静态检查，没有执行这个消费者得到新的候选比例。

无论几何目标是否全部通过，输出始终保持以下三项为 false：完整共同度量证明、固定度量下的实际精化收敛证明、课题完成。R666 只有在真实全域曲率及该合并计算返回后，才能登记具体 reach 应用。


执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
