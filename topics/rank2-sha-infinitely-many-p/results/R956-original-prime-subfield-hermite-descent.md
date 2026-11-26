# R956 — 原 F 整模的精确素域下降与完整附加块返回

- 日期：2026-11-26。
- 状态：**完整整模证明；既有公开 API 的新增回归已实际成功。**
- 本条不声称原 F 除子、原四交、有限 shadow 或非零性已计算完成。
- 原唯一 F v3 作业仍按其已检出的 source 运行，不因本条改变或重启。
- 直接依赖：R942 §11 完整有界 HNF、R925 完整原仿射结构、
  R927 原低权 F 整理想、R924 原截面环嵌入。

## 1. 确实存在的原素域矩阵

记同一原素域为 \(f=\mathbf F_r\)，同一原常数域为
\(k=\mathbf F_{r^2}\)，同一基参数为 \(t\)，且
\[
R_0=f[t]\subset R=k[t].
\]
这里的包含是给定原 \(k\) 的唯一素域嵌入，不选择另一个二次域或根。

目前单 F 路径的以下源链明确给出 \(f\)-结构，
不是根据“F 应定义在有理数上”猜测：

| 实际源 | 完整来源事实 |
|---|---|
| `original_low_f_complete_divisors.py::build_original_low_f_complete_kernel` | 在原 `maps["original_fp"]` 上重建全部 \(1429\times1260\) 混合矩阵及 \(144\) 维全核 \(K\)；随后才 `K.change_ring(k)`。原选定 \(a,b\) 是同一核的第一行。 |
| `original_section_ring_embedding.py::build_original_y_section_basis` | \(666\) 原 M2 行的全部坐标 reader、源 jets 和 flat 均在原 \(f\) 上；只有最后坐标注入给定 \(k\)。 |
| 同文件 `build_original_section_ring_embedding` | 三个原退化拉回的全部 \(120\times666\) 系数及原对数微分乘数 \(j\) 在同一 \(f\) 上。 |
| `original_affine_multiplication.py` 及原 fast adapter | 原 \(46971\) 对称基乘积的全部结构常数在同一 \(f\) 上；原 \(k\) 仅作常数扩张。fast contraction 的素域运算不等于 HNF 已下降。 |
| `original_low_f_operator_recipes.py` | 全 \(324\) 原 R2 乘积、全部 \(1890\) 加权坐标及原 \(144\times324\) 核仍按原顺序全乘，故各 \(b_i\) 两图坐标都在原 \(f\)。 |

因此当前 F 路径 `complete_first_factor_divisor` 中，
首个以及后续每个 \(M_{b_i}\) 的全部 \(306\times306\) 条目
都属于 \(R_0\)。它们与此前完整 \(B\) 基堆叠的行模也有同一素域结构。
现有 bounded reducer 在输入 `rows.base_ring()` 上直接运算；
R956 之前没有逐系数素域下降门。

原 \(y_F\) 的尺度也完整保留。实际源定义
\[
a=\pi_2^*A/J^5,\qquad b=\pi_2^*B/J^2,
\]
其中 \(a,b\in R_0^{306}\)，且
\[
y_F=\frac{a}{\theta_{17}^3q_0b},\qquad
q_0=-t^3(t^2-9)^3(t^2-1),\quad \theta_{17}^6=17.
\]
另一图的对应标量为
\[
-\theta_{17}^3s(1-9s^2)^3(1-s^2).
\]
原 `OriginalFraction.__init__` 只消全部坐标共同的首一
scalar polynomial，再按分母首项常数归一。
该首一公因子在 \(f[t]\)，故真正保存的两图坐标满足
\[
D\in R_0^{306},\qquad N\in\theta_{17}^{-3}R_0^{306}.
\]
这说明实际 \(M_D\) 也可下降；并不意味着含 \(M_N\) 的每个混合块
都已在素域。新实现不改任何原函数对象、分子分母尺度或坐标表达；
只有整个 LEFT 及整个 attached 都通过下一节的门才下降。
尤其不会把 \(\theta_{17}^3\) 或附加块的真二次坐标抹掉。

上述源按已运行 F v3 source
`77d09068ff2324c7c301c144e4c3586437f4ad59` 核对；
低 F helper 的原 Git blob 为
`0d1e78eb0665a0d00c1d3339cb2674529c5d0eb4`。
源码可直接在
[该固定提交的 scripts](https://github.com/Rogerhu12/math-research-public/tree/77d09068ff2324c7c301c144e4c3586437f4ad59/topics/rank2-sha-infinitely-many-p/scripts)
复核。

## 2. 全行模下降引理

设 \(A_0\in R_0^{m\times n}\)，\(m\ge n>0\)，
\(A=\iota(A_0)\) 在 \(R\) 上有满列秩 \(n\)。
\(R=R_0\otimes_f k\) 是忠实平坦扩张，而且
\[
R\otimes_{R_0}\operatorname{row}_{R_0}(A_0)
=\operatorname{row}_{R}(A).
\tag{1}
\]
这里没有只保 \(f\)-线性来源；右侧仍允许**全部 \(k[t]\) 来源系数**。
满列秩在扩张前后相同，因为非零极大子式在注入后仍非零，
而扩张不会把一个恒等于零的子式变成非零。

令 \(H_0\) 是 \(A_0\) 的完整上行 HNF。
完整 elementary 行运算以及仅删除恒零行证明
\[
\operatorname{row}_{R_0}(H_0)=\operatorname{row}_{R_0}(A_0).
\]
由 (1)，\(H=\iota(H_0)\) 的行模准确等于原
\(\operatorname{row}_R(A)\)。
首一对角、上三角及各列余式次数在系数注入下保持，
所以 \(H\) 本身就是原 \(R\) 上唯一的规范 HNF。
这不是比较行列式次数后猜测两个整模相等。

对已有 API 支持的方形 LEFT \(m=n\)，再给完整附加块
\(B=\iota(B_0)\in R^{n\times q}\)，其中 \(q\) 任意。
素域 backend 对**整个** \([A_0\mid B_0]\) 同步做同一个
\(U_0\in\mathrm{GL}_n(R_0)\)，得到
\[
H_0=U_0A_0,\qquad Z_0=U_0B_0.
\tag{2}
\]
把 (2) 经同一原嵌入送回：
\[
H=\iota(U_0)A,\qquad Z=\iota(U_0)B.
\tag{3}
\]
因此原全部附加列和来源返回完整保留。
没有只下降 LEFT 后把 attached 按不相同的变换处理，
也没有只保 attached 的素域分量。
不另累计完整 \(U_0\)；仍沿用 R942 已证的实际全块同步操作。

次数、每个零条目及原行列顺序在注入下不变。
R942 的 LEFT 上界
\[
\max(D,2\delta+1)
\]
及完整 attached 上界
\[
\max(D,2\delta+1)+(n-1)D-\delta+\deg B
\]
逐字适用。\(\delta=\dim_k(R^n/\operatorname{row}A)\)
也等于 \(\dim_f(R_0^n/\operatorname{row}A_0)\)；
不混淆它们与 \(R\)-模组成长度。

## 3. 实现的逐系数接受门和失败返回

只改已有 `complete_degree_bounded_row_hermite` 函数内部。
函数名和对象绑定不变，所有已有消费者的 `is` 门继续有效。

对调用者给定 \(k\)：

1. 只在它确为二次有限域时尝试；素域输入或其他既有输入直接走原 backend。
2. 取这个 \(k\) 自带的 `prime_subfield()`，不调用另一个有限域构造器。
3. 对 LEFT、attached 的每个原行、原列、每个多项式系数 \(c\)，
   在原给定坐标检查非素域坐标为零、\(c^r=c\)，
   并核 \(k(c_0)=c\)。
4. 每个完整多项式都从下降系数重新注入原 \(R\)，要求与原多项式精确相等；
   位置和矩阵形状完全不变，零行也保留。
5. **任意一个** LEFT 或 attached 系数失败，
   立即对未经改动的两个原输入执行原 \(k[t]\) backend。
   不按单行缩放、不取某个投影、不改原函数或进行经验容错。

只有所有输入检查通过，原有完整 bounded 算法才在 \(R_0\) 工作。
原算法主体、全部行操作、source/attached 同步、
最终每条原来源返回以及次数断言保持。
结束后完整 \(H_0,Z_0\) 经同一嵌入回到**原来的 \(R\) 对象**，
再次对所有原 LEFT 行做完整 HNF 除法；规范 HNF 条件也在原 \(R\) 复核。

原 receipt 的 input、attached、结果 HNF、结果附加块与首一行列式
hash 均继续按**原 \(k\) 的坐标编码**计算。
操作流中每个素域行操作系数也先注入原 \(R\) 再 hash，
不把一份只编码 \(f\) 的流假装成原 \(k\) 编码。
新增 nested receipt 另存素域输入/结果摘要及每个接受门；
任何实际真二次系数的 fallback 原因都有明确记录。

这保留完整数学身份并把部分已有矩阵交给素域多项式 backend。
尚无原矩阵执行时间回执，因此不写加速倍数或资源承诺。

## 4. 复用现有公开 API 的三个必要回归

只扩 `check-original-bounded-hermite-api.py` 与它已有 request，
不新增 workflow，不启动第二份原正规化。
request v2 仍给定原小例 \(k=\mathbf F_{29}[a]/(a^2-2)\)。
原全部 bounded/triangular/affine/full306 回归继续运行；新增：

- 在该给定二次域中，用全部素域系数的 LEFT 和完整非方形附加块
  \(B=[I\mid AX]\)。返回原 \(R\) 后从附加块取 \(U\)，核
  \(UA=H\)、\(Z=[U\mid HX]\)、\(U\) 幺模及原全部 hash。
- 令 LEFT 有实际非素域系数 \(a\)，要求真正 fallback，
  仍与官方完整 HNF 相等并完整核 \(UA=H\)。
- LEFT 全素域但附加块含 \(at\)，要求 attached 触发真正 fallback，
  并核所有返回列准确等于原 \(UB\)。

这些只检新字段返回风险与原算法接口；
不宣称生成了原 \(Y\)、F 除子或有限 shadow。

当前 F workflow 的 push paths 不包含本 bounded helper 或这个 API reader/request；
已核其固定 `.github/workflows/rank2-sha-original-low-f-divisors.yml`。
本次发布不会重启仍在运行的原 F 作业。
未来同一原生产入口自然读取新 source；必须等对应真实数学回执。

## 附录：现有三角原像的完整来源次数粗界与可选阶段规约

本附录只补 R942 §8 现有算法的数学上界，不修改该算法，不把未观察到的
性能问题写成事实。

设目标 \(H\) 完整上 HNF，\(h_j=H_{jj}\)，
\(d_j=\deg h_j\)，\(D=\sum_jd_j=\deg\det H\)，源秩为 \(r\)。
每一步开始，完整余式 \(W\) 的第 \(j\) 坐标次数小于 \(d_j\)。
因此该列中原 \(r\) 个残余及附加 \(-h_j\) 的次数至多 \(d_j\)。

先给不依赖任何黑箱次数约定的界：
令 \(\tau_{j,i}\) 是实际第 \(i\) 个二行操作矩阵中最大非负条目次数，
则完整附加来源 \(P\) 的每个中间条目满足
\[
\deg P\le \sum_{j,i}\tau_{j,i}.
\tag{4}
\]
因为每步完整来源只左乘该多项式二行矩阵，
最大次数至多相加；换行和非零常数倍不增加次数。

现固定实现的标准 extended-Euclidean 返回满足
\[
\deg s,\deg t,\deg(a/g),\deg(b/g)\le d_j
\]
（零系数忽略）；可整除情形的商也次数至多 \(d_j\)。
这里不能只从 \(sa+tb=g\) 推出次数界：
给任何 Bézout 对添加 \((qb/g,-qa/g)\) 会任意增大次数。
使用的是标准 Euclidean 对的次数性质。

为核准这里的实际库输入，已读 Sage 10.6 的
[finite-field polynomial 路由](https://github.com/sagemath/sage/blob/10.6/src/sage/rings/polynomial/polynomial_ring.py)、
[polynomial template 的 xgcd](https://github.com/sagemath/sage/blob/10.6/src/sage/rings/polynomial/polynomial_template.pxi)、
[NTL linkage](https://github.com/sagemath/sage/blob/10.6/src/sage/libs/ntl/ntl_ZZ_pEX_linkage.pxi)，
以及它声明版本 NTL 11.5.1 的
[XGCD / XHalfGCD 原源码](https://github.com/libntl/ntl/blob/91acd5b3a7df709c0d8bf88a99a24bc340dc34f7/src/ZZ_pEX.cpp)。
该返回由 Euclidean 二行矩阵的分块乘积组成；
商次数相加沿严格下降的余式次数望远镜消去，
给出上述界。NTL 该文件的 Git blob 为
`96a1c307d7c862c9635404717c90aa40c4e3481d`。
这不是对任意只承诺 Bézout 身份的替代 API 作性能假设；
若未来改算法后端，(4) 仍成立，较简的下一界须再核系数次数。

每列最多 \(r\) 次二行消元，故保守地有
\[
\boxed{\deg P\le (r+1)\sum_{\text{已处理 }j}d_j\le(r+1)D.}
\tag{5}
\]
现算法因此不能被描述成已证存在“跨列指数膨胀”。
它最后才作完整 HNF；该末次阶段的 LEFT 界由 R942 §11 给
\[
\max((r+1)D,\,2D+1).
\]
若 \(D=0\)，所有规范余式列为零，来源始终为 \(I_r\)。

另一方面，在某个完整列约束之后，若将整个 \(P\) 作
**unshifted weak-Popov** 规约，同时把同样行操作作用到整个 \(W\)，
并只减原完整 \(H\) 行重新取余，则原不变量
\(W\equiv PM\pmod{\operatorname{row}H}\) 和全部来源行模都保持。
这里没有删任何源行，也没有丢任何附加坐标。

设当时来源指数次数为 \(\delta_j\le D\)。
完整方阵的互异 unshifted leading positions 占满所有列；
把行按 leader 排序，行最高次系数矩阵为下三角、对角非零。
故
\[
\deg\det P=\sum_i\deg(\text{row}_iP)=\delta_j,
\qquad \deg P\le\delta_j\le D.
\tag{6}
\]
这个结论专用于 **unshifted** 完整弱 Popov，不把任意 shift 的
weak-Popov 条件误当条目次数帽。
(6) 只说明阶段规约若以后需要，数学上可合法压低来源次数；
当前未新增该实现、未修改现有三角入口，亦未声称有实际性能收益。

## 源码与执行状态

本条证明和实现经 root/global 两路复核；以下保留源码身份；后面的实际回执来自公开作业。

- `scripts/original_degree_bounded_row_reduction.py`：23467 B，SHA256 `7a815e44e4fb5c52d4be124cedbda08e8597c1f262470c8e1e143c7561c9a192`。
- `scripts/check-original-bounded-hermite-api.py`：14042 B，SHA256 `bf7e4dad2292bf6ed0f8dc8afc70fc38c3f0a19b20a577a0dcade64996823c96`。
- `ci/original-bounded-hermite-api-request.json`：395 B，SHA256 `3c51a2beb9443d51d027acfd9e242d17dcd7087d0077c95efd4678ed7d956a8e`。
- 复用原 `.github/workflows/rank2-sha-bounded-hermite-api.yml`（blob `878d91d43ddb9cc0261ff9a443f6d51d69f2b894`），只检查新增真实域返回风险及原全部接口；原 F v3 不变。

## 既有 API 的实际回执

2026-11-26 10:47:27 UTC，原 workflow 的 run `45804356890` / job `139855545149` 成功完成，source `11fe8b583f23057712b962474fda76ad5682781c`。固定 Sage10.6、离线只读源，14份脚本 AST 与全部来源绑定通过；数学 reader 用时 `34.519377524999996` 秒。

新增三门全部实际通过：给定 F29² 中全素域 LEFT 和完整非方形 attached 经原嵌入返回，明确取出 U 验 UA=H、Z=[U|HX]；LEFT 真二次系数完整回退；仅 attached 真二次系数完整回退且所有列等于原 UB。全部原 field hash、完整整模包含、原环对象与附加列顺序已核。原自适应 shift、完整306算法例、一般矩形原像、重复非分裂厚因子和完整仿射图接口也继续通过。

- Manifest SHA256：`736715cabf460365b318c7a0ff0c452bca1f51153d1d61bad96945b2dd091a3c`。
- 规范 RESULT：14228 B，SHA256 `e131fcba22ae5e2e07c2d3962ef1f3ffbd146b7221efa55981e0bf6f4741bda4`，与 reader 自报摘要相等。
- 完整 job 日志按工具 UTF-8 保 BOM：294028 B，SHA256 `efd35f8000b04d3d32551d6922acbe180c22d124ae348f5aef7e33f66843675b`。

这次执行检验的是本节真实返回风险和既有接口；没有重建原 Y、原映射、F 除子或 shadow，不能据其用时推断原306的加速倍数。未保存可重算日志或输出数据。

## 已审后继原 Artinian 入口 v5（尚未触发）

本小 API 成功后，后继真实入口固定同一 bounded 源摘要 `7a815e44…c1c9a192`，保 R955§6 的45份来源及所有旧 pins/原main/四交/九对/全厚Miller门。新增门只读实际 `geometry["F_poles"]`，并要求其函数对象正是原 `six["F_y"]`：两图的真实分母逐系数落在原Fp；其真正 paired graph 的 `complete_denominator_image` 来源摘要必须等于同一原 MD operator，形状306×306、完整像与所有来源回投均核，且 R956 的 `applied` 和原域返回门确实通过。含真二次系数的其它块仍允许完整 fallback，不把它们全强称可下降。

root 已沿原 `complete_paired_fraction_graph`、`zero_pole_ideals`、geometry direct cache 与实际 embedding context 核准每个键、对象和 MD 来源连接。该 MD 调用实际不带 attached；后续含 MN 的全附加求解不被此门替代。

| 待接路径（课题目录内） | Git blob | 字节数 / SHA256 |
|---|---|---|
| `scripts/produce-original-triangular-artinian-shadow.py` | `7df9e025dfab74f037c5eb11a5bde5c5e5594583` | 22186 / `1e857feb4af384f3855a1a67e15552c3cb12064b62faf258e8e75a344f265c7b` |
| `scripts/launch-original-triangular-artinian-shadow.py` | `53b5bcf6684da98806d38187b9576fb919873a3f` | 10309 / `fde822004fe398ec93384ca063870ef3e51bbba7ecd26255df1a666545499de3` |
| `ci/original-triangular-artinian-shadow-request.json` | `3f3970dbbcc0196fca9fcf780a675c26796b7a24` | 827 / `c5286d90af616689070aae1c1f7dfede64cde60cb313eef66663bffe2f8b682a` |

workflow 仍为 R955§6 的 blob `5713d440f42e1bd2f638944ce2dc9d3d4ddd1d5b`。r29/q2453/batch64/minimal/两份原 PASS pins 不变。上述三份源码暂只以不可变 blob 持有，不挂触发路径；当前唯一 F 的实际终点之前不并开第二份原306。原 F/完整 shadow 的真实结果尚未取得。
