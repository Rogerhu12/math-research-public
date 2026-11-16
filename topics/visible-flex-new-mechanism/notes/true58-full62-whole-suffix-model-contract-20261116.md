# 原 62 个有效后缀控制的完整后缀 minimax：模型合同

日期：2026-11-16。策略：`true58-full62-whole-suffix-v1`。

本文件只固定一个新科学问题、源级实现和计费/输出边界。它不是一次
已经执行的计算，不宣称新的实际接受索引或主课题完成。模块和合同的
制作、纸读没有执行科学代码、导入、编译、开发测试或数值查询；
实际工作只准在本公开仓库自己的新 GitHub Actions 范围内执行。

## 1. 为什么是一个新问题，以及关闭的祖先

此前 whole34 保原 R0 的 34 方向问题已经关闭；其大 MODEL/J/TRACE
正文当前不能恢复，绑定、大小和 hash 不能变成免费数组。随后释放
原 R0 的 17 方向，求原末 51 个 u/v 系数的 whole-suffix 问题也已关闭：

- run `43910342020`，research job `133450221925`；
- source `077d1dbb9c184cf4c6edf3e4c20014880d810283`；
- 单 solver 钟在 362.24296968 秒处停止，没有 OptimizeResult，
  没有实际返回 raw53，没有可推广的 candidate；
- 新科学 410.626657796 秒；新 180 个 q、179 次 J、2864 个导数块；
  没有 whole-body prediction 或原 actual pair；
- 累计 3642.4396103470003 秒 / 147 个原 full 值，接受索引仍为 58。
  末 callback 输入不等于末完整评价点，不能把任一者冒作返回。

该范围的初末科学数组只输出绑定，不能作为本新范围的免费输入。
完整关闭依据为
[full51 钟停记录](true58-full51-whole-suffix-clock-stop-no-return-20261116.md)
以及已闭提交 `60a8e49fae1fe91c186f8614806a637447cf8ef3`。

本范围进一步开放两个原准确零积分的尾部高度坐标和原 complete
body 的九个坐标，共新增 **11 个真实可影响后缀的控制**。因此实际
新问题为 62 个控制加 K、h，共 64 变量，唯一初点仍是真实接受 58。
它不延长、不重启、不从末评价点续跑旧 whole34 或 full51。

本次读取原坐标/基函数源码的固定公开 head 为
`f574177a77ec20aa1f459ea2b0fde21794862ea6`。实际 Actions 还必须
按请求 manifest 绑定全部新旧源码；不得拿此说明代替 source receipt。

## 2. 原坐标的实际布局，以及排除的四个零列

这里全部索引为 Python 从 0 起、半开区间。

| 独立 q168 行 | 原始含义 | 本范围 |
| --- | --- | --- |
| 0…80 | 9 径向 × 9 角向的原 u | 只开放 54…80 |
| 81…152 | 9 径向 × 8 角向的原 v | 只开放 129…152 |
| 153 | 原 normalized-Q 的 v 列 | 固定 |
| 154…158 | 原五个准确零积分高度坐标 | 只开放 157、158 |
| 159…162 | 原 complete body 的四个 u 模式 | 全开放 |
| 163…166 | 原 complete body 的四个 v 模式 | 全开放 |
| 167 | 原 complete body 的零总量高度坐标 | 开放 |

原 prefix102 是 u 的前六径向列和 v 的前六径向列：
独立 0…53 与 81…128。它们在 s≥153/200 的两阶径向 jet 准确为零。
此外，q153 的 normalized-Q 径向因子用原第一 retained quintic B3，
也在本后缀为零；q154…156 的前三个 null-height 方向在准确
\([9/250,\,9/250+7(81/1000)]=[.036,.603]\) 内紧支撑，
其密度、所需导数和准确紧支撑 primitive 在本后缀均为零。

因此，不能把这四列放入优化器来宣称增加有效自由度。实际非零
控制顺序是：

\[
{\cal I}=(54,\ldots,80;\ 129,\ldots,152;\
157,158;\ 159,\ldots,167),\qquad |{\cal I}|=62.
\]

源码依据为原
`frame_entry_single_q.py` 的 normalized-Q 径向定义、
`frame_height_null_coordinates.py` 的准确五高度基、
`frame_direct_reference_geometry159.py` 的直接 reference+null 高度求值，
以及
`frame_complete_body_extension168.py`、
`frame_complete_body_extension168_joint_selected.py` 的 body9 布局。
这些旧文件不在本范围修改。

新增 body9 与原旧51不同，它在 body 内部也有真实支持；后缀合格
不能证明 body 其余部分合格。尤其，不能由支撑或后缀目标推断原
全体 metric 最大值一定下降。外部原全体预测和原十四门仍不可少。

## 3. 准确的 168→172 映射与一次舍入

设 \(q_{58}\) 是按原完整日志恢复的实际 binary64 独立 168 向量。
\(E\in\mathbb Q^{168\times62}\) 在第 c 列、第 \({\cal I}_c\) 行
置 \(1/4\)，其余为零。后端输入为

\[
x=(z_0,\ldots,z_{61},K,h)\in\mathbb R^{64}.
\]

每个后端 binary64 先解释为自己的准确有理值。未舍入独立点和
真正用于几何的点分别为

\[
q_{\rm ideal}=Q(q_{58})+E\,Q(z),\qquad
q_{\rm actual}=\operatorname{RN}(q_{\rm ideal}),
\]

每个改变的独立坐标只把准确公共和转成一次 binary64；其他独立
坐标保 q58 的原字节。不得先舍入增量再加，不能 clip、投影或
改写实际后端返回。

原完整物理映射 \(F:\mathbb Q^{168}\to\mathbb Q^{172}\) 是
原 159→163 准确仿射 null-height 映射与 body9 identity 的直和：

- 物理 0…153 为独立 0…153；
- 物理 154…162 为永久原 reference-height9 加原准确
  \(H_{9\times5}\) 乘独立 154…158；
- 物理 163…171 为独立 159…167。

本范围消费并记录完整 \(H_{9\times5}\)，未以浮点九高度投影替代。
特别是其末两列非零项为

\[
H_{6,3}=1,\quad H_{8,3}=-\frac32,\qquad
H_{7,4}=1,\quad H_{8,4}=-\frac54.
\]

因此 \(P=F_{\rm lin}E\in\mathbb Q^{172\times62}\) 有 63 个非零行，
而不是简单的 62 个物理 identity 行。除各 primary 行的 \(1/4\)
外，物理第 162 行必须含

\[
(Pz)_{162}=-\frac38z_{51}-\frac5{16}z_{52}.
\]

primary 物理行顺序为
\((54,\ldots,80;\ 129,\ldots,152;\ 160,161;\ 163,\ldots,171)\)。
这些 62 个独立方向在原准确仿射物理映射下线性独立，不重建旧
34 维 R0 核，也不再施加旧 R0 等式。

必须分别保存和使用：

\[
p_{\rm ideal}=F(Q(q_{58}))+P\,Q(z),\qquad
p_{\rm actual}=F(Q(q_{\rm actual})).
\]

第二个公式使用原 `full_coefficients(..., exact=True)`/
`exact_heights`。**不能把 172 个理想物理行分别 RN 后还当成原
准确仿射 image**。特别是 actual 的九高度仍为准确有理仿射值，
不是九个各自舍入的 binary64。盒与范数终门均检查 actual 这一定义；
原总高度和 body 零总量恒等式保留。raw64、ideal168、ideal172、
actual168、actual172、准确舍入差、物理增量和状态 hash 均有保存字段。

唯一初点为 \((z,K,h)=(0,58,0)\)，准确恢复 q58。q_R 只作已付的
几何基准，不作初点；没有多初点、phase-I 重启或从旧末点接续。

## 4. 目标、原盒、原范数和显式保留的有限 h 上限

唯一目标仍为

\[
\min(K+10^{-6}h),\qquad
\frac{1000}{61}\le K\le58,\qquad
0\le h\le
h_{\max}=\frac{18014398507545773}{281474976710656}.
\]

这个 hmax 是已付 free/R1/R2 绑定中的同一准确数。其旧推导只覆盖
旧51 active rows，本合同**仅将它明确保留为本新范围的有限限制**；
不声称它足以覆盖新增 11 方向在整个原物理盒内的一切可能幅度。
不重新计算旧 hmax，也不无依据扩大。若这一有限范围以后不足，
需要另一个明示的新科学域问题。

原完整 lower172/upper172 一字不改，理想物理点与实际舍入后的准确
物理点都必须在盒中。后端线性模型有：

- 每个原物理行的上下界，共 344 行；
- 每个实际非零物理方向行的正负范数约束，共 \(2\times63=126\) 行；
- K、h 的四个区间行。

因此线性行数为 **474**。未舍入的线性范数条件准确为

\[
h\ge4\|Pz\|_\infty
 =\max\!\left(\|z\|_\infty,\
 \left|-\frac32z_{51}-\frac54z_{52}\right|\right).
\]

原线性可行性仍用原 `LP_ROW_TOLERANCE`，不另加容差。
`backend_norm_epigraph_exact_pass` 单独报告准确真假，不能由
容差通过宣称准确 \(h\ge4\|Pz\|_\infty\)。

由于独立一次舍入会改变实际物理增量，资格还必须准确满足

\[
4\|p_{\rm actual}-F(Q(q_{58}))\|_\infty\le Q(h_{\rm raw}).
\]

该门不会因为 rawh 只差 ulp 就放宽；不事后抬 h。
理想和实际物理增量也都必须在显式 hmax 内。初点 z=h=0 自身准确
可行。没有通过强制正舍入余量破坏唯一零初点；因此后端线性门通过
仍可能被准确舍入后范数终门拒绝，这一风险没有被虚称已经消除。

为避免旧 full51 的独立原盒端点问题，本范围把原盒 62 个 primary
物理行转成保守 backend bounds。对相应独立坐标 i、primary 行 j，
原准确关系为 \(p_j=o_j+q_i\)，其中固定 offset
\(o_j=p_{58,j}-q_{58,i}\)。先把原 \([\ell_j-o_j,u_j-o_j]\)
的两个独立端点向盒内取 binary64，再把允许 z 区间
\(4(q_{\rm endpoint}-q_{58,i})\) 向内取 binary64。
这些界含真实零初点，并充分保证独立 RN 后的所列 primary 行不出盒。

耦合物理 row162 不能由上述独立界自动保证；其完整原线性行和
准确 terminal gate 全保留。此充分接线未改变原盒、未增容差。
K 下端只向内取最小足够 binary64，h 上端向内取最大不超原准确数的
binary64，linear row、backend bound、绑定和最终准确区间一致。

## 5. 全部 21 后缀径向行与两套完整角网

只使用原已付 radial 中准确 binary64 身份满足 \(s\ge153/200\)
的全部 21 行，含原 ring141；保原粗 384 和细 768 两个 theta 网及
各自的完整 \(\Pi_N\)，不重造网、不换同值浮点表达式、不减角向点。

每个实际点保原两条 metric proposal row 和四条未平方曲率 PSD row，
合计

\[
21(384+768)\times6=145152
\]

条非线性行，加原 474 线性行，总 **145626** 行。

曲率始终用 actual first form
\(I=\begin{pmatrix}E&F\\F&G\end{pmatrix}\)，保实际 G；
二次基本形式的 numerator 也取完整真实位置二 jet。
目标谱条件等价地使用

\[
Kq I\pm N\succeq0,
\]

按原 curvature_scale 缩放，分别保 trace 和 determinant。
不平方后删掉符号或 trace，不把 G 设成 1，不用仅某个方向的曲率
替代完整主曲率。原直接 principal-curvature 查询、unsmoothed eta、
normal-area 的独立门同在资格中；normal-area 失败属于真实域失败，
不能伪造一行有限 residual 继续。

严格 metric 预算使用原已付 budget：
binary64 `0.26600531463999305`，由 root audit 与原 SOURCE_ETA−1e−7
绑定，模块另与 prefix 原准确 binary64 budget 绑定。这个字段只是一
个相同浮点预算的记录，不代表连续上界证明。

最终必须同时通过：

1. 原两网 unsmoothed eta ≤预算；
2. 原四条未平方 PSD 行在实际返回 K 下的原容差；
3. 原直接 \(|\kappa_i|\le K+\) 原 direct tolerance；
4. 原 hard58 cap；
5. 原正常正面积域门。

仅有某个 smooth proposal residual 好看、K 下降、部分网合格或
backend status 好看，都不能成为后缀资格。

## 6. 已付四输入与真正新付的内容

旧四个完整科学来源按原请求固定 run/job/source 和全文 hash 恢复：
接受58、永久55/原 reference、free36 的完整 MODEL 与 RING_SOLUTION，
以及 prefix102 的完整 MODEL/COMPLETE/FINAL。旧 whole34 和 full51
关闭日志只作为成本祖先，不能提供未恢复或仅有 binding 的科学数组。

具体付清可复用的 prefix 数据只有它真正保存的内容：

- `new_paid_input.fixed_metric` 的 a、a_s、a_ss；
- `fixed_height_derivatives` 的 q_R 基准 b、b_s；
- 两网原 theta、完整 radial；
- `original_families` 中原角向与角向一阶基；
- `source_scalar_fields` 中 q_R 的 u/v value、s、ss、theta；
- `fixed_suffix_full_arrays` 中全部后缀 T、位置二 jets（不含 X）、
  metric e/f/eta、normal_area、principal_curvatures、scaled_PSD_rows，
  以及其原 radial_ids 和 theta。

完整 payload、dtype、shape、数组 hash 和实际坐标身份必须已有；
缺数就真实失败。报告里列出元数据不等于全文数组已经恢复。

本范围的 prepare 恰调用一次外层 `charge_prepare`。它包含新问题
所必需的新 P172×62、原盒/范数线性 rows、inward anchor bounds，
以及此前没有保存为可免费输入的以下基数据：

- 原 full spline B9/B10/B11 直到 s 二阶的 jet；
- 原两个 tail null-height 的 b、b_s；
- 原 body P5/P8 的 0、1、2 阶径向 jet。

body profile 为原
\(P_m(\xi)=\xi^m e^{-\xi/(1-\xi)}\)，
\(\xi=(s-9/250)/(81/100)\)，端外作原零延拓。
u 用 m=5，v 用 m=8；body height 的中心增量为
\((81/100)\gamma P_8\)，所以 b 增量为 \(\gamma P_8'\)，
b_s 增量为 \(\gamma P_8''/(81/100)\)。
不得把 height 误作 P8 本身或多除/少除一次 length。
后缀曲率只需这些导数；本模块不为出报告另求不需要的中心 primitive。

角向直接复用已保存的原 sin(2jθ) 前四列和一阶导数；它们就是原
body 四模式的源码定义，不另做旧角向三角查询。原 null-height
`values` 在本后缀按原准确 compact support 跳过前三个高度零列。

新 initial q58 的后缀 geometry、其 J、实际迭代新几何/J、缺失的 I/II
代数输入、K 变动后的曲率 row/J 重组，均在真实同一总钟内计费；
不得因有坐标或基函数源码就称科学派生数组已免费恢复。

## 7. 增量值语义、固定行与高度导数

q_R 的保存值只读。新值把保存的 q_R u/v scalar fields 加上
\(q_{\rm actual}-q_R\) 的原 tail 和 body 基增量；
b、b_s 也在保存的 q_R 基准上加 q157、q158、q167 的准确坐标变化
对应的原高度基增量。若高度坐标实际没有变化，直接复用原 b、b_s。

这与原完整场在数学上是同一个场；浮点求差、乘加和求和分组
**不是原 canonical whole-body 的逐位执行次序**。不能把增量 predictor
合格升级成 canonical actual 接受。候选最终交的是已固定的 actual q168，
外部原 canonical 预测/原 actual14 再独立把关，不能重解码或改系数。

对每个原 radial binary64，只有它同时不小于原 spline、null-height、
body 的准确和实际 binary64 右端点时，才能判为全62方向的固定行。
共同准确右端为 \(423/500\)。固定行依然保在全部 21 行中：

- T、jets、e/f/eta、normal-area、principal 和 cap58 PSD 可读原已付值；
- 物理 62 列导数由严格零支持给零；
- **当前 K 的 PSD 和 K 导数仍需组装**，不能原封保 K58 的 PSD。

新 I/II 若原未保存，第一次从保存 jets 形成时是真新代数工作，
同钟计费；不为得到 I/II 重做已保存的 eta、area、principal 或 frame。
fixed/mutable 行按原身份合并，没有裁掉失败行。

## 8. 64 列解析链与缓存的准确所有权

对每个真可变径向块，u 的旧27+body4 与 v 的旧24+body4 共用原
完整角向 \(\Pi_N\) 导数链。保持 \((R,R_s,R_{ss})\) 对应的完整位置
二 jet 导数，按原 radial-major/mode-minor 列序收缩；body 取同一
angular virtual 三 jet 的前四角列乘原 P5/P8 径向，不漏交叉项。

三个高度 backend 列的实际作用是

\[
\partial X_s=e_z\,b_{\rm basis}/4,\qquad
\partial X_{ss}=e_z\,(b_s)_{\rm basis}/4,
\]

其余 X_t、X_st、X_tt 和 T 导数为零。这里的前两个 basis 已包括
原第9物理高度列的精确补偿，不是只扰动某个单独物理高度。

全部 62 列都进入 metric e/f 的链和 actual I/N/area 的完整曲率链，
K 为第62列、h 为第63列（从0起）。K 的谱导数按当前 K 形成，
h 只进入原固定线性范数/区间行。
解析链在实际解码场上使用原连续坐标方向；不把 binary64 RN 视为
处处可微映射，不以此免除真实候选的准确舍入终门。

缓存分层：

- 几何与 K 无关的物理导数输入按 actual q168 字节身份；
- 同 q 的新 K 可复用那些几何/导数输入，但必须重新形成依赖 K 的
  PSD 和最终 64 列 J；
- 完整最终 J 的键含 actual q168 和当前 K 的 binary64 字节，
  不能仅按 q 复用整张 J；h 只影响固定线性行；
- 仅保当前 q 的几何/导数块、当前 q+K 的最终 J、初末真正已算数组
  为输出绑定所需的引用，以及有明确 backend 上限的已算 residual
  向量。无无限科学数组归档、无磁盘 cache、无 artifacts/actions-cache
  上传、无报告时重算。

淘汰后再次访问同 q 或同 q+K 若实际重算，执行次数、耗时和重复计数
都必须增加；“distinct q 未增加”不等于零科学工作。已算 value
命中可读，已淘汰 J 不为报告补算。过程 RSS 和所有真实 CPU/墙钟工作
仍在总预算内。初末 binding 与小元数据可以留，但 hash 不是未来
可恢复科学数组的凭据。

初始行尺度只由这一次实际初值与实际完整初 J 形成：
\(\max(1,|r_i(x_0)|,\max_j|J_{ij}(x_0)|)\)，随后固定。
不由全域峰所在位置推断初始 suffix 预算通过；实际初值亲自决定。

## 9. 唯一后端、实际点数与原返回

外层新科学总钟最多 1800 秒；单 solver 上限 1200 秒，SLSQP
maxiter=320，ftol=1e−9，原目标 regularizer=1e−6 不变。
原 scope 计数器、原 actual pair 上限和累计祖账由 root wrapper 执行。

本模块恰一次调用
`scipy.optimize.minimize(method="SLSQP")`，唯一 q58 初点，无重启。
两种上限分别记录，不能混用：

- 最多 640 个不同 actual q168、且真正需要新几何的物理点；
  字面 paid q_R 复用单列，不收费冒成新几何；
- 最多 1280 个不同 literal backend64 字节输入，含同 q 的新 K/h，
  包括 objective、constraint、J 和 iteration callback 的首次访问。

重复执行的真实 cost 另计，不因 distinct 上限不增而免费。
initial J 和后端实际请求的 J 都计入；不提前扫描未请求 J，
不为保存末状态补跑 J。时钟在真实调用边界核对，单个不可抢占的
后端调用可能超过标称秒数；如发生，必须报告真实 overrun，不截断账。

OptimizeResult 一返回，就先保存完整原对象和全部字段、实际 raw64、
status/success/message/nit/nfev/njev、实际耗时，然后才做 decode、
门和时钟。若实际返回有有限 raw64，不论 status 是否合格，都保存
其 once-rounded q168 和准确 physical172。所有 multipliers 如有
保原返回，不称其为严格证书。

如果真实钟停或异常在返回前发生，则没有原 OptimizeResult；
保最后实际 backend 输入、最后真正完整评价、已算 J/partial 的完成范围，
并分别标明。不得造一个 failure OptimizeResult、冒最后迭代为 raw 返回，
或把停止状态改成后端 status0。

## 10. 资格、输出和未来输入边界

可交外部的 candidate 必须来自实际有限、success=true、status0 的
原 OptimizeResult，并通过：

- 原 scaled residual ftol；
- 原 unscaled linear-row tolerance；
- 理想和实际准确 original172 box、K/h 区间及本范围 hmax；
- actual rounded physical norm≤实际 rawh 的准确终门；
- 第5节的两个完整角网、全21行、全部 unsmoothed/unsquared/area 门。

不从失败 status 或未返回向量造候选。资格只授权外部唯一一次原
canonical whole-body prediction；通过其原门后才可至多一个原
actual pair。原完整接受十四门、内外全域/reach/metric/embedded
条件不删不改，accepted_count 只能由外层实际接受事实改变。
后缀成功也可能只成为下一真实联合问题的输入，不预称 59 或完成。

输出使用紧凑但完整的文本协议，目标整个新研究 stdout<96MiB。
每次实际输入/值/迭代保存必要状态、坐标 hash、约束/极值摘要和组件成本。
大 J、初末几何、导数输入和 partial 只输出 shape/dtype/hash、
确实完成的 row/column 范围和真实计费；不输出大数组、不制造截断片段。
初末已有值没有时不补算。partial 的 np.empty 未填写区域既不 hash
也不输出；只能绑定真正已完成的块。

完整原 OptimizeResult（包括它实际返回的数值字段）和 raw64 保留，
最后实际返回 q168/physical172 的小完整记录保留。
原 result 只由模块 emit 一个 `NONLINEAR_RESULT`；
root caller 负责唯一的 `MODEL`、`SOLVE_TRACE`、`BODY_SOLUTION`
及相应异常 partial、COMPLETE/FINAL，避免同 tag 重复。
若 emit 自身失败，实际已保存的未发出 result 仍在 capture 中；
不能以有 receipt 字段名就虚称完整输出存在。

这些紧凑 bindings 不是下一范围免费科学数组。当前进程结束后不承诺
恢复本次 derived arrays；若未来确实需要而没保全文，必须另明新范围
并如实付费。旧 249MB trace 的模式不再沿用。

## 11. 源文件和稳定接口

职责拆分为两个真实源码文件，各小于 100,000 UTF-8 字节：

- `scripts/frame_metric_current168_full62_whole_suffix.py`：
  原完整来源恢复、准确坐标/原盒模型、新高度/body 输入、全后缀值和
  解析 J、模型绑定/摘要；
- `scripts/frame_metric_current168_full62_whole_suffix_solver.py`：
  单后端、时钟/点数、真实原返回、缓存访问与紧凑 capture。

这是按职责拆源码，不拆科学数据、不编码/分块绕输出限制。
两个新文件都由请求 manifest 和 model implementation_hashes 绑定。
旧源只导入使用，不修改。core 通过 lazy import 暴露以下固定 API，
避免导入时循环或执行科学工作：

~~~python
build_full62_whole_suffix_model(
    field, accepted_state168, ring_candidate168,
    paid_free_model, paid_free_solution, paid_prefix_model,
    cfg, lower172, upper172, source_receipt, wall, capture=None,
    *, metric_budget, charge_prepare)

solve_full62_whole_suffix_once(
    model, *, wall, charge_solve, emit=None, capture=None,
    solver_seconds=1200., maxiter=320, max_evaluations=640,
    max_backend_evaluations=1280)

full62_whole_suffix_capture_record(capture, *, include_arrays=False)

model.summary()
model.full_record()
~~~

builder/solve capture 必须是各自新的空 dict，wall/charge 为外层原接口。
prepare 恰调用一次、solve 恰调用一次；全部运行中 value/J 内部实际
执行计数进 model/capture，外层同一总钟覆盖执行和输出。

solve 返回保 `status`、`report`、`qualified`、
`qualified_candidate`、`candidate168`、`candidate`、
`candidate_record`、`actual_backend_raw64`、
`backend_success`、`backend_status`。
candidate168 只有真正资格通过才非空；candidate_record 可以包含
实际失败返回的完整 decode，不能据它存在就送 actual。

`summary`、`full_record`、`capture_record` 只读取已算事实，
不请求科学求值；即使 legacy include_arrays=True 也不输出大数组，
该参数的实际含义会明记。root 在 solve 后和 finally 读取已有真实
summary/capture，保 0 solver、0 J、partial 或无返回的实际事实。
