# R686：完整曲率的准确分块覆盖、自然返回与同场续接

2026-11-26，Astra-larger-e4e2a2bf-20261126 / geometry。

**状态：已证明的分域覆盖与调度接口；源已静态审读及通过 `py_compile`，尚无新科学运行、数值或加速结论。**

新源为 `scripts/resume_20261126/actions_batched_closed_curvature.py`。
它支持原多项式 lift 和 R671 canonical reference-tail bundle，复用：

| 角色 | 实际数学源 SHA256 |
| --- | --- |
| R670 完整场/角界 | `eaa9a579eea227cbf348138295534144c39d07b669ea1c9ff494f22baa4ae599` |
| R672 完整曲率形算子 | `8ca81feefda43fd4423bee1877c8e9198c7774afae0cf8cc2227424765dac385` |
| R674 准确参考尾连续六jet | `f1220a2e83578bb186ec1043c5dc5fd70dd988f1a108897537117344590de225` |

不改这三个已刊源，不把新的 producer SHA 冒充为其中任何一个。
科学工作只在 `Rogerhu12/math-research-public` 的真实 Actions 执行。

## 1. 每个任务的真实域

旧8ca/f122一次返回一个完整原胞；本入口把一次任务进一步限定为

$$
C_{i,p}\times[j/r,(j+b)/r]\times\text{完整角圆},
$$

其中 $i$ 是准确符号节点的原胞，$p$ 是该胞内准确 lift 分片，
$r$ 是声明的 dyadic 径向分割数，$1\le b\le\texttt{radial-block}$。
分片均由原数学源给出。R671场的分片包含 scalar segments、原chi断点和两个eta断点；
不存在只采样断点或跨越断点偷用同一解析式的情形。

任务的角域仍为原完整闭角覆盖及既有对称性延拓，不是若干角点。
原全部Fourier模、完整Laurent支撑、指数余项及R671标量余项保持。
每个有限角层的 `Q`、保留模数 `L`、原 `M` 均真实记录；`L<M` 的全部有限尾仍支付。
可以显式选 `L=M` 消除该有限尾，这没有改变物理场、网格或目标g。
默认层级保留旧计划，不预报哪种新层级更快。

任务实际包含不超过原内存分组准则的变换组：通常
`8 * (degree+1) * b * Q <= 2^20`；极大Q至少保留一个径向小片。
这只限制一次科学任务的作用域和中间数组，不是运行时间上界。
未测得任何每块必在600或900秒内完成的承诺。

## 2. 多项式块的完整证明

设原准确分片的归一化径向变量为 $u\in[0,1]$。
R672的 `piece_definitions` 已给所有物理六jet的Bernstein系数以及解析角尾乘子。
对任务中的每个小片

$$
u\in[j/r,(j+1)/r]
$$

直接调用原 `Reader.restrict`，参数为准确有理数 $j/r,(j+1)/r$ 的向外包围。
Bernstein de Casteljau 限制恒等式把原多项式准确限制到这个闭子区间；
原区间实现逐次向外包围每次加乘除，因此新控制点包住相同准确多项式，
没有修改系数或额外插值。先取得物理导数再限制，所以没有漏掉参数变换因子。

对每个限制后的控制点与每个真实角盒，仍由R670的 `angle_boxes` 包围保留模，
另加完整有限高尾和解析lift尾。解析尾的径向标量先限制再取绝对值，
因此它支付的正是这一子片；没有把一个旧大盒的余项任意缩小。
逐径向子片对其控制点取凸包，得到 $V,T,AA,VT,EE$ 在整个子片和整个角盒上的界。

令 $N=T\times V$、$E=|V|^2$、$W^2=|N|^2$。
如原R672实现，同时用 $E|T|^2-(V\cdot T)^2$ 包围 $W^2$，取两个合法区间的交。
可选首jet报告已经由相应原reader验证同一真实bundle/node/model，
它的整胞 $E,W^2$ 下界当然也适用于本块。取下界的较大者仍然有效。
若所得整块 $E,W^2$ 下界严格正，原R672 `shape_upper` 对真实欧氏第一、第二形式
给该块全部位置的主曲率绝对值上界；存在未付角盒时，该块上界保持null。
这证明每个有效返回严格覆盖其声明的整块域。

直接有理restriction与旧 `radial_parts` 的重复二分可能产生不同浮点区间宽度；
本入口只主张两者都包围同一准确场，不主张字节相等或新界必定更紧。

## 3. R671块的完整证明

对于准确eta起点以前的整原胞，R671的场表达与原多项式场恒等。
本入口只在原 `_old_formula_applies(cell)` 的条件下使用第2节的分块公式。
即使提供了R671首jet报告，也仍取该报告实际已证明的同场整胞下界，
没有把该报告改写成R670的旧producer身份。

其余胞对每个声明的径向小片，直接调用冻结f122的
`subpiece`、`piece_definitions(..., 'curvature')` 和 `_field_batch`。
这些调用重新在该准确小片形成共同标量Taylor jet、独立导数余项和完整角尾；
这正是R674已经证明的完整六jet包围。随后使用与第2节相同的真实形算子公式。
标量积分及角变换仍是新的Actions科学计算，不在本地预跑。

## 4. 完整原胞和全闭面的合并

固定原胞 $C_i$ 和一个层级 $(Q,r,L)$。
只有该层级的全部准确lift片、各片从 $j=0$ 到 $r-1$ 的所有闭径向小片
都已有实际有效返回时，才得到此层级的完整原胞界

$$
K_{i,Q,r,L}=\max_B K_B,
\qquad E_{i,Q,r,L}=\min_B E_B>0,
\qquad W^2_{i,Q,r,L}=\min_B W_B^2>0.
$$

少一个块、只返回部分块、存在未付浸入盒，均不成为完整原胞曲率界。
同一胞不同完整层级都包围同一准确场，因此可以分别取

$$
K_i=\min_{\text{已付完整层}}K_{i,Q,r,L},\quad
E_i=\max_{\text{已付完整层}}E_{i,Q,r,L},\quad
W_i^2=\max_{\text{已付完整层}}W^2_{i,Q,r,L}.
$$

这些量可来自不同完整层，三条不等式仍各自对整个原胞成立。
源码每个实际块返回后增量更新这一合并，不反复扫完全部旧计算。

令 $V$ 为有完整曲率界的原胞集合，$P=\{i\in V:K_i\le K_{\rm goal}\}$。
只有 $V$ 是全部原胞，才输出全域 `continuous_curvature_upper`。
全闭面的平帽曲率为0，镜像和准确活动相位保持主曲率绝对值，故全胞最大值
覆盖原完整闭族的曲率；嵌入、固定marker、reach、metric和精化责任仍分别保留。

完整cuff胞的面积下界还可按原准确接口
$|F_\phi\times F_s|^2=R^2\rho^2$ 给 $|\rho|$ 的正下界。
连续rho无零且均值1，所以rho为正。输出用有理dyadic向下平方根，
不添加新的场评估。没有完整cuff界时此项为null。

## 5. 自然返回、journal与公开小结

默认 `--budget-seconds 600` 只停止**新任务接纳**，已经接纳的至多workers个块自然返回。
不因正常预算发送kill、SIGINT或SIGTERM。这样外部控制器可把每批自然退出
作为一个stage立即发布，不需要改stdout转发机制。
若外部硬时限仍中断一个块，该块没有完整返回，后继会重新支付这一未付块；
此前实际返回块的字节不由推断补造。

每个完成块先原子写入仓库外journal的独立小JSON，才记入父汇总。
journal header绑定新producer、实际输入及源SHA、准确模型、参数与本Actions run。
`--resume` 重新读取实际raw并验证域，跳过已经完整返回的相同任务；
它可继续新的显式层级或新的原胞子集，不重算已达当前目标的整胞。
输入、模型或固定读法参数变动必须使用新journal。
异常退出的具体块/配置也单独记录；后继不无条件重试同一个已失败配置，
其域仍为未付，可以由新的显式精度层覆盖。异常不被改写成数学曲率反例。

公开 `--out` 不含逐块/逐胞原始表，只给两条有明确域的数学结论：

1. $V$ 上的统一曲率上界 $U_V=\max_{i\in V}K_i$，统一E/W²正下界及V的区间字符串。
2. $P$ 上对应的统一界 $U_P$ 与P的区间字符串。

整胞集合最多是922个编号，域本身是覆盖责任；这些域与少量统一界不能还原
逐胞曲率值或原始数组。相应输入/源、journal摘要、实际run和本批成本同时记录。
这些小结可以作为明确域上的已付结论登记；仅有 $P$ 不满全域时不声称完成。

当前实现的程序性续接是**同runner真实journal**。
小结已具有跨job数学合并所需的域与统一界，但自动跨job compact导入尚未实现，
输出明确 `compact_cross_job_import_implemented=false`。
不把丢失的旧runner-local raw当作存在，也不把重建后不同字节的场混作同一场。

## 6. 完整调用与下一批

下列变量须由实际新求解返回设置。`BUNDLE`是该实际新场，`NODES`是它的准确节点报告；
R671还须给原scalar输入，reference carrier与同场首jet报告可以按实际存在情况提供。
没有提供可选报告时不继承旧场的界。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python "$REPO/topics/visible-flex-larger-amplitude/scripts/resume_20261126/actions_batched_closed_curvature.py" \
  --repo "$REPO" --bundle "$BUNDLE" --node-report "$NODES" \
  --scalar-input "$SCALAR_INPUT" --reference-carrier "$REFERENCE_CARRIER" \
  --first-geometry-report "$FIRST_REPORT" \
  --journal "$WORK/new-member-curvature-journal" \
  --out "$WORK/new-member-curvature-batch-01.json" \
  --levels 256:1:24,512:2:32,1024:4:48,2048:8:64,4096:16:96 \
  --target 81/10 --taylor-degree 12 --scalar-degree 5 --panels 128 \
  --radial-block 4 --workers 4 --budget-seconds 600 --beta 1/4
```

第二批使用相同实际输入、相同journal以及 `--resume`，换一个新out：

```bash
# 其余输入与第一批相同。
--resume --journal "$WORK/new-member-curvature-journal" \
--out "$WORK/new-member-curvature-batch-02.json"
```

原多项式bundle可省略scalar输入和reference carrier，`--model auto`会选原模型；
有canonical R671 tag时必须采用R671 reader，不会误走旧lift核。
如果只是要先处理确定的几何瓶颈，`--cells` 支持 `880-921` 等准确原胞集合；
同journal中此前已付的其他胞仍保留，最终完整性按全部原胞并集判断。

4进程只是独立分块的调度参数。不同worker返回顺序不改变取max/min的准确有理合并，
不存在异步写共享场或修改原目标。实际加速、峰值内存与每批返回量须由新Actions报告。
`maximum_worker_peak_rss_kib`是单worker历史最大值，明确不是同时总RSS。

## 7. 控制器输出字段

每批 `outputs` 只需列该批新out；journal继续留在当前runner，不被cleanup模式删除。
已附 `computations/resume-20261126-curvature-summary-fields.json`，其值均为控制器可直接读取的标量路径。
其中 `uniform_domains_json` 是有语义的两个覆盖域与统一界，
不含逐胞raw；`valid_cell_ranges`、`target_paid_cell_ranges`等是区间字符串。
完整原始数据仍按根规矩15不入Git/Release/artifact。

新几何合并器须诚实识别本schema和新producer，而不是把其输出标签伪装成8ca/f122。
也可直接在实际同场返回后按R650与R661进行有证明的数学合并；
无论如何，只有完整K的真实返回才支付相应曲率责任。

## 8. canonical 双标签的实际读取修正

初版c9fb源码错误地把带非零 `exact_tail_lambda` 补充标签的合法canonical bundle也拒绝。现ee3744b3版本只在缺canonical模型而出现任一非零lambda标签时拒绝；合法canonical双标签交冻结f122的 `_read_model` 核mandatory reference标签、optional标签与模型身份一致性。此为静态发现的入口修正，无科学运行或K数值改变；全部包围公式保持。

## 同场真实直径消费入口

后继[完整first／分批K／非平面／四标记合并接口](../notes/2026-11-26-same-field-batched-curvature-geometry-consumer.md)按同场实际D精确设置K目标，保本R686 producer和显式完整胞域；这是本条实际消费链，尚无新场证书返回，也不占用R666。
