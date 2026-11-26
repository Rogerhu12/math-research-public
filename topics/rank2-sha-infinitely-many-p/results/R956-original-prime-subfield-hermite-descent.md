# R956 — 原 F 整模的精确素域下降与完整附加块返回

- 日期：2026-11-26。
- 状态：**完整整模证明；§§1–4 的严格下降 API 已实际成功；§5 的共同常数扩展亦已实际通过，见§5.4；§7整条原像下降及其新增API亦已实际通过，见§7.5。**
- 本条不声称原 F 除子、原四交、有限 shadow 或非零性已计算完成。
- 原唯一 F v3 作业仍按其已检出的 source 运行，不因本条改变或重启。
- 直接依赖：R942 §11 完整有界 HNF、R925 完整原仿射结构、
  R927 原低权 F 整理想、R924 原截面环嵌入。

## 1. 确实存在的原素域矩阵

记同一原素域为 $f=\mathbf F_r$，同一原常数域为
$k=\mathbf F_{r^2}$，同一基参数为 $t$，且
$$
R_0=f[t]\subset R=k[t].
$$
这里的包含是给定原 $k$ 的唯一素域嵌入，不选择另一个二次域或根。

目前单 F 路径的以下源链明确给出 $f$-结构，
不是根据“F 应定义在有理数上”猜测：

| 实际源 | 完整来源事实 |
|---|---|
| `original_low_f_complete_divisors.py::build_original_low_f_complete_kernel` | 在原 `maps["original_fp"]` 上重建全部 $1429\times1260$ 混合矩阵及 $144$ 维全核 $K$；随后才 `K.change_ring(k)`。原选定 $a,b$ 是同一核的第一行。 |
| `original_section_ring_embedding.py::build_original_y_section_basis` | $666$ 原 M2 行的全部坐标 reader、源 jets 和 flat 均在原 $f$ 上；只有最后坐标注入给定 $k$。 |
| 同文件 `build_original_section_ring_embedding` | 三个原退化拉回的全部 $120\times666$ 系数及原对数微分乘数 $j$ 在同一 $f$ 上。 |
| `original_affine_multiplication.py` 及原 fast adapter | 原 $46971$ 对称基乘积的全部结构常数在同一 $f$ 上；原 $k$ 仅作常数扩张。fast contraction 的素域运算不等于 HNF 已下降。 |
| `original_low_f_operator_recipes.py` | 全 $324$ 原 R2 乘积、全部 $1890$ 加权坐标及原 $144\times324$ 核仍按原顺序全乘，故各 $b_i$ 两图坐标都在原 $f$。 |

因此当前 F 路径 `complete_first_factor_divisor` 中，
首个以及后续每个 $M_{b_i}$ 的全部 $306\times306$ 条目
都属于 $R_0$。它们与此前完整 $B$ 基堆叠的行模也有同一素域结构。
现有 bounded reducer 在输入 `rows.base_ring()` 上直接运算；
R956 之前没有逐系数素域下降门。

原 $y_F$ 的尺度也完整保留。实际源定义
$$
a=\pi_2^*A/J^5,\qquad b=\pi_2^*B/J^2,
$$
其中 $a,b\in R_0^{306}$，且
$$
y_F=\frac{a}{\theta_{17}^3q_0b},\qquad
q_0=-t^3(t^2-9)^3(t^2-1),\quad \theta_{17}^6=17.
$$
另一图的对应标量为
$$
-\theta_{17}^3s(1-9s^2)^3(1-s^2).
$$
原 `OriginalFraction.__init__` 只消全部坐标共同的首一
scalar polynomial，再按分母首项常数归一。
该首一公因子在 $f[t]$，故真正保存的两图坐标满足
$$
D\in R_0^{306},\qquad N\in\theta_{17}^{-3}R_0^{306}.
$$
这说明实际 $M_D$ 也可下降；并不意味着含 $M_N$ 的每个混合块
都已在素域。新实现不改任何原函数对象、分子分母尺度或坐标表达；
只有整个 LEFT 及整个 attached 都通过下一节的门才下降。
尤其不会把 $\theta_{17}^3$ 或附加块的真二次坐标抹掉。

上述源按已运行 F v3 source
`77d09068ff2324c7c301c144e4c3586437f4ad59` 核对；
低 F helper 的原 Git blob 为
`0d1e78eb0665a0d00c1d3339cb2674529c5d0eb4`。
源码可直接在
[该固定提交的 scripts](https://github.com/Rogerhu12/math-research-public/tree/77d09068ff2324c7c301c144e4c3586437f4ad59/topics/rank2-sha-infinitely-many-p/scripts)
复核。

## 2. 全行模下降引理

设 $A_0\in R_0^{m\times n}$，$m\ge n>0$，
$A=\iota(A_0)$ 在 $R$ 上有满列秩 $n$。
$R=R_0\otimes_f k$ 是忠实平坦扩张，而且
$$
R\otimes_{R_0}\operatorname{row}_{R_0}(A_0)
=\operatorname{row}_{R}(A).
\tag{1}
$$
这里没有只保 $f$-线性来源；右侧仍允许**全部 $k[t]$ 来源系数**。
满列秩在扩张前后相同，因为非零极大子式在注入后仍非零，
而扩张不会把一个恒等于零的子式变成非零。

令 $H_0$ 是 $A_0$ 的完整上行 HNF。
完整 elementary 行运算以及仅删除恒零行证明
$$
\operatorname{row}_{R_0}(H_0)=\operatorname{row}_{R_0}(A_0).
$$
由 (1)，$H=\iota(H_0)$ 的行模准确等于原
$\operatorname{row}_R(A)$。
首一对角、上三角及各列余式次数在系数注入下保持，
所以 $H$ 本身就是原 $R$ 上唯一的规范 HNF。
这不是比较行列式次数后猜测两个整模相等。

对已有 API 支持的方形 LEFT $m=n$，再给完整附加块
$B=\iota(B_0)\in R^{n\times q}$，其中 $q$ 任意。
素域 backend 对**整个** $[A_0\mid B_0]$ 同步做同一个
$U_0\in\mathrm{GL}_n(R_0)$，得到
$$
H_0=U_0A_0,\qquad Z_0=U_0B_0.
\tag{2}
$$
把 (2) 经同一原嵌入送回：
$$
H=\iota(U_0)A,\qquad Z=\iota(U_0)B.
\tag{3}
$$
因此原全部附加列和来源返回完整保留。
没有只下降 LEFT 后把 attached 按不相同的变换处理，
也没有只保 attached 的素域分量。
不另累计完整 $U_0$；仍沿用 R942 已证的实际全块同步操作。

次数、每个零条目及原行列顺序在注入下不变。
R942 的 LEFT 上界
$$
\max(D,2\delta+1)
$$
及完整 attached 上界
$$
\max(D,2\delta+1)+(n-1)D-\delta+\deg B
$$
逐字适用。$\delta=\dim_k(R^n/\operatorname{row}A)$
也等于 $\dim_f(R_0^n/\operatorname{row}A_0)$；
不混淆它们与 $R$-模组成长度。

## 3. 实现的逐系数接受门和失败返回

只改已有 `complete_degree_bounded_row_hermite` 函数内部。
函数名和对象绑定不变，所有已有消费者的 `is` 门继续有效。

对调用者给定 $k$：

1. 只在它确为二次有限域时尝试；素域输入或其他既有输入直接走原 backend。
2. 取这个 $k$ 自带的 `prime_subfield()`，不调用另一个有限域构造器。
3. 对 LEFT、attached 的每个原行、原列、每个多项式系数 $c$，
   在原给定坐标检查非素域坐标为零、$c^r=c$，
   并核 $k(c_0)=c$。
4. 每个完整多项式都从下降系数重新注入原 $R$，要求与原多项式精确相等；
   位置和矩阵形状完全不变，零行也保留。
5. **任意一个** LEFT 或 attached 系数失败，
   立即对未经改动的两个原输入执行原 $k[t]$ backend。
   不按单行缩放、不取某个投影、不改原函数或进行经验容错。

只有所有输入检查通过，原有完整 bounded 算法才在 $R_0$ 工作。
原算法主体、全部行操作、source/attached 同步、
最终每条原来源返回以及次数断言保持。
结束后完整 $H_0,Z_0$ 经同一嵌入回到**原来的 $R$ 对象**，
再次对所有原 LEFT 行做完整 HNF 除法；规范 HNF 条件也在原 $R$ 复核。

原 receipt 的 input、attached、结果 HNF、结果附加块与首一行列式
hash 均继续按**原 $k$ 的坐标编码**计算。
操作流中每个素域行操作系数也先注入原 $R$ 再 hash，
不把一份只编码 $f$ 的流假装成原 $k$ 编码。
新增 nested receipt 另存素域输入/结果摘要及每个接受门；
任何实际真二次系数的 fallback 原因都有明确记录。

这保留完整数学身份并把部分已有矩阵交给素域多项式 backend。
尚无原矩阵执行时间回执，因此不写加速倍数或资源承诺。

## 4. 复用现有公开 API 的三个必要回归

只扩 `check-original-bounded-hermite-api.py` 与它已有 request，
不新增 workflow，不启动第二份原正规化。
request v2 仍给定原小例 $k=\mathbf F_{29}[a]/(a^2-2)$。
原全部 bounded/triangular/affine/full306 回归继续运行；新增：

- 在该给定二次域中，用全部素域系数的 LEFT 和完整非方形附加块
  $B=[I\mid AX]$。返回原 $R$ 后从附加块取 $U$，核
  $UA=H$、$Z=[U\mid HX]$、$U$ 幺模及原全部 hash。
- 令 LEFT 有实际非素域系数 $a$，要求真正 fallback，
  仍与官方完整 HNF 相等并完整核 $UA=H$。
- LEFT 全素域但附加块含 $at$，要求 attached 触发真正 fallback，
  并核所有返回列准确等于原 $UB$。

这些只检新字段返回风险与原算法接口；
不宣称生成了原 $Y$、F 除子或有限 shadow。

当前 F workflow 的 push paths 不包含本 bounded helper 或这个 API reader/request；
已核其固定 `.github/workflows/rank2-sha-original-low-f-divisors.yml`。
本次发布不会重启仍在运行的原 F 作业。
未来同一原生产入口自然读取新 source；必须等对应真实数学回执。

## 附录：现有三角原像的完整来源次数粗界与可选阶段规约

本附录只补 R942 §8 现有算法的数学上界，不修改该算法，不把未观察到的
性能问题写成事实。

设目标 $H$ 完整上 HNF，$h_j=H_{jj}$，
$d_j=\deg h_j$，$D=\sum_jd_j=\deg\det H$，源秩为 $r$。
每一步开始，完整余式 $W$ 的第 $j$ 坐标次数小于 $d_j$。
因此该列中原 $r$ 个残余及附加 $-h_j$ 的次数至多 $d_j$。

先给不依赖任何黑箱次数约定的界：
令 $\tau_{j,i}$ 是实际第 $i$ 个二行操作矩阵中最大非负条目次数，
则完整附加来源 $P$ 的每个中间条目满足
$$
\deg P\le \sum_{j,i}\tau_{j,i}.
\tag{4}
$$
因为每步完整来源只左乘该多项式二行矩阵，
最大次数至多相加；换行和非零常数倍不增加次数。

现固定实现的标准 extended-Euclidean 返回满足
$$
\deg s,\deg t,\deg(a/g),\deg(b/g)\le d_j
$$
（零系数忽略）；可整除情形的商也次数至多 $d_j$。
这里不能只从 $sa+tb=g$ 推出次数界：
给任何 Bézout 对添加 $(qb/g,-qa/g)$ 会任意增大次数。
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

每列最多 $r$ 次二行消元，故保守地有
$$
\boxed{\deg P\le (r+1)\sum_{\text{已处理 }j}d_j\le(r+1)D.}
\tag{5}
$$
现算法因此不能被描述成已证存在“跨列指数膨胀”。
它最后才作完整 HNF；该末次阶段的 LEFT 界由 R942 §11 给
$$
\max((r+1)D,\,2D+1).
$$
若 $D=0$，所有规范余式列为零，来源始终为 $I_r$。

另一方面，在某个完整列约束之后，若将整个 $P$ 作
**unshifted weak-Popov** 规约，同时把同样行操作作用到整个 $W$，
并只减原完整 $H$ 行重新取余，则原不变量
$W\equiv PM\pmod{\operatorname{row}H}$ 和全部来源行模都保持。
这里没有删任何源行，也没有丢任何附加坐标。

设当时来源指数次数为 $\delta_j\le D$。
完整方阵的互异 unshifted leading positions 占满所有列；
把行按 leader 排序，行最高次系数矩阵为下三角、对角非零。
故
$$
\deg\det P=\sum_i\deg(\text{row}_iP)=\delta_j,
\qquad \deg P\le\delta_j\le D.
\tag{6}
$$
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


## 5. 原 F 的统一非素域附加常数与完整返回

本节在 §§1–4 已执行的严格下降上扩展一个实际来源明确的情形。
原 LEFT 仍必须逐系数属于原素域；只允许**整个附加块**共同提取
一个经全部系数验证的非零原常数。原函数、原源行、原值及原场均保留。

### 5.1 原 paired graph 的实际第二次分母规约

§1 已沿原七映射与两图源码核准，对原 $F_y$ 有
$$
D\in f[t]^{306},\qquad
N=\gamma N_0,\quad N_0\in f[t]^{306},\qquad
\gamma=\theta_{17}^{-3},\quad \theta_{17}^6=17,
\tag{7}
$$
其中 $f=\mathbf F_r$，$k=\mathbf F_{r^2}$ 是调用者已经固定的原域，
同一 $\theta_{17}\in k$ 沿原嵌入固定。由整基乘法表也在 $f[t]$，
$$
M_D\in\operatorname{Mat}_{306}(f[t]),\qquad
M_N=\gamma M_{N,0},\quad M_{N,0}\in\operatorname{Mat}_{306}(f[t]).
\tag{8}
$$
这里不替换 $N/D$，也不把 $F_y$ 缩放成另一个函数。

原 `complete_paired_fraction_graph` 实际先取
$H_D=\operatorname{HNF}(M_D)$，再求完整原像
$$
\mathcal Y
 =\{y\in k[t]^{306}:yM_N\in\operatorname{row}_{k[t]}(M_D)\},
\tag{9}
$$
用其规范 HNF $Y$ 作最后完整左除法
$$
X M_D=Y M_N .
\tag{10}
$$
该最后调用规约的 LEFT 为 $M_D^{\mathsf t}$，
**整个 attached 为 $(Y M_N)^{\mathsf t}$**，不是第一次无附加块的 $M_D$ HNF。

证明 $Y$ 在素域。令 $R_0=f[t]$，$R=k[t]$，
$I_0=\operatorname{row}_{R_0}(M_D)$。先对原 $R_0$ 映射
$$
R_0^{306}\longrightarrow R_0^{306}/I_0,\qquad y\longmapsto yM_{N,0}
$$
取完整核 $\mathcal Y_0$。$R_0\to R$ 平坦，故扩张后完整核恰为
$R\mathcal Y_0$。又 $\gamma\in k^\times$，$RI_0$ 对 $\gamma^{\pm1}$
稳定，故乘 $\gamma$ 不改变这个核，得到
$$
\mathcal Y=R\mathcal Y_0 .
\tag{11}
$$
完整原像含 $\det(M_D)R^{306}$，因此满秩。
$\mathcal Y_0$ 的首一规范 HNF 经同一嵌入仍是 $R$ 的首一规范 HNF；
由规范形唯一性，原程序最后的 $Y$ 就是这一个素域矩阵。
这里用的是完整核与全 HNF，未从秩或函数域解猜测整原像。

于是 (10) 的整个附加块确为
$$
(YM_N)^{\mathsf t}
 =\gamma (YM_{N,0})^{\mathsf t},\qquad
(YM_{N,0})^{\mathsf t}\in\operatorname{Mat}_{306}(f[t]).
\tag{12}
$$
这正是旧严格规则会回退、而本节可完整下降的实际输入。
$\gamma$ 在两个原域都是真二次常数：
$r=29$ 时 $17^2=-1$，故 $17^{14}=-1$；
$r=41$ 时 $17^2=2,17^4=4,17^{16}=10$，故 $17^{20}=-1$。
因此 $17^{-1}$ 在 $f$ 非平方，
而 $\gamma^2=17^{-1}$，所以 $\gamma\notin f$。

(11) 是源身份的证明，不宣称现有一般三角原像的每一个中间量均已实施素域算法。
本节实际新增的优化点是 (10) 的完整分母/附加块规约；
当前仍运行的旧原 F 作业不受改变。

### 5.2 一条常数线的完整判定与同步变换

给定原输入
$$
A\in\operatorname{Mat}_n(R_0),\qquad
B\in\operatorname{Mat}_{n\times b}(R).
$$
新规则先完整核 $A$；任何真非素域 LEFT 系数立即对两个未经修改的原输入
执行原 backend。LEFT 从不按行、列或常数重新缩放。

若附加块所有系数都在 $f$，取 $\gamma_B=1$，保持 §§1–4 的原路径。
否则只把遇到的第一个非素域非零系数当作候选 $\gamma_B$，
接着对**全部原行、全部原列、每个系数** $c$ 验证
$$
c/\gamma_B\in f,\qquad
(c/\gamma_B)^r=c/\gamma_B,\qquad
\gamma_B\,\iota(\bar c)=c.
\tag{13}
$$
每个完整多项式重新注入原 $R$ 并乘回 $\gamma_B$，
必须与原多项式精确相等。零矩阵取 $\gamma_B=1$。
(13) 成功当且仅当全部附加系数包含于同一条 $f$-常数直线；
只检一个样本绝不构成接受。

对实际 (12)，候选可能为 $\gamma_B=a\gamma$，
其中 $a\in f^\times$ 是首个样本的素域因子；
无需声称候选一定等于规范 $\theta_{17}^{-3}$。
整个算法只需要 $B=\gamma_B\iota(B_0)$。
在同一实际原场检查 $\gamma_B/\theta_{17}^{-3}\in f^\times$
即可把未来生产回执连接回 (12)。

成功后同一 bounded 算法对 $[A\mid B_0]$ 运行。
所有换行、行加法及非零常数行倍只由 LEFT 决定，
仍完整同步作用于每条附加来源。
若全操作为 $U_0\in\mathrm{GL}_n(R_0)$，则
$$
H_0=U_0A,\qquad Z_0=U_0B_0.
$$
完整返回定义为
$$
H=\iota(H_0),\qquad Z=\gamma_B\iota(Z_0).
\tag{14}
$$
由于常数与全部行操作交换，
$$
\boxed{H=\iota(U_0)A,\qquad Z=\iota(U_0)B.}
\tag{15}
$$
所以原 source/attached 逐行身份恰好保留，
不是只保持附加块所张空间。此证明也涵盖任意非方形附加宽度。
后续完整 back substitution 仍解 $HV^{\mathsf t}=Z$，
并对所有原行验证 $VM_D=YM_N$，不修改 RHS 的归一化。

$\gamma_B$ 是非零常数，故所有多项式次数不变，
R942 的 LEFT、attached、$\delta=0$ 与自适应 shift 上界全部照旧。
原输入、原附加、完整 HNF、完整返回附加块、首一行列式 hash
仍按原 $k$ 坐标计算。全部操作系数仍先注入原 $R$ 后写操作流 hash；
同一 LEFT 的操作流不因附加共同常数改变。
新增字段单独记录候选位置/坐标/摘要、全部比值检验和常数完整乘回。

任一比值失败时，两个完整原输入未被修改；
不保留部分下降结果，不按行选不同常数，
不把混合的两个 $f$ 方向投影成一个方向。
例如一个非零素域系数与一个真二次系数共存的块就一定完整回退。
因此本节不放宽原源合法性门，只增加有完整逆返回的实现路径。

### 5.3 既有小 API 与后继真实执行的边界

原 `check-original-bounded-hermite-api.py` 的 v3 request 增加以下实际返回门，
仍与全部旧 bounded/triangular/affine/full306 算法例同次执行：

1. 在原给定 $\mathbf F_{29}[a]/(a^2-2)$ 内取真实 $\theta_{17}^6=17$，
   令 $\gamma=\theta_{17}^{-3}$，现场核 $\gamma^2=17^{-1}$、
   $\gamma^{29}\ne\gamma$。对原素域 $A$ 与完整
   $B=\gamma[I\mid AX]$，要求所有列返回
   $Z=\gamma[U\mid HX]$，并从其前两列还原 $U$ 验 $UA=H$。
2. 同一原二次系数环的官方 `hermite_form(transformation=True)`
   独立返回 $H_{\mathrm{official}},U_{\mathrm{official}}$，
   要求 $H_{\mathrm{official}}=H$ 及
   $U_{\mathrm{official}}B=Z$。这核的是完整附加值，非只有 HNF 或维数。
3. 对完整非方形 RHS $\gamma VA$ 调用原
   `full_polynomial_left_division`，要求返回原 $\gamma V$，
   每行乘回同一个 $A$，并核对应原 source/solution hash。
4. 保持真二次 LEFT 回退；含原恒等块的附加矩阵再加真二次系数时，
   要求两个独立方向触发完整 fallback，且全部列仍等于原 $UB$。

这次只更新 bounded helper、既有 reader 和 request；
当前61份本课题 workflow 的完整 push 区段均已核读，
无通配或无 paths 的 push。
这三路径只命中原
`.github/workflows/rank2-sha-bounded-hermite-api.yml`，
不触发原 F、Artinian 或六 P 重型作业。

源码身份：

- `scripts/original_degree_bounded_row_reduction.py`：26458 B，
  SHA256 `41be1b362e024ba847240c7bd928ae4e991b3c160d1c3556f7d8837d9b1788fa`。
- `scripts/check-original-bounded-hermite-api.py`：17846 B，
  SHA256 `a56509132452cc63f26f990c5afbe48446686d1ac7c512f9bc7b4d2baeafed08`。
- `ci/original-bounded-hermite-api-request.json`：447 B，
  SHA256 `34102686cfaad18f267ea34065c85f8a7e937efef8dada8b78760fa01aaff3ce`。

本节新增分支的独立真实回执见§5.4；不以原v2回执代替。
后继原 Artinian v6 将保全部45份来源、既有原 PASS pins、全七式/两图/四交/厚商门，
并增加 (10) 的实际常数恢复门；在真实原306执行前不宣称该门已通过。


### 5.4 新共同常数路径的实际公开回执

source `6e18843738b5700ac5f58ac69b8b41f70440ac7f`，
[run45832239579](https://github.com/Rogerhu12/math-research-public/actions/runs/45832239579)，
job `139951704598`，2026-11-26 13:46:40 UTC 实际结束，结论 **success**。
同一 Sage10.6、离线只读源挂载、14份数学源码 AST 均通过；
数学执行25.649820739999996秒。只运行原小 API，未重生原几何。

实际原二次域中的 $\theta_{17}$ 坐标为 $(0,21)$，
$\theta_{17}^{-3}$ 为 $(0,8)$。完整共同常数下降与完整非方 RHS 左除法
都实际进入单常数路径，并返回原多项式环；所有附加列和每一原 source 行
精确回乘。官方二次域全 HNF/变换也返回同一结果。
同一 LEFT 的全操作流摘要与未提常数原例相同；
真二次 LEFT 与两个独立附加方向均完整回退，未丢任何系数。
全部旧三类接口及完整306维算法例仍通过；该306维例不是原 F 的306维整模。

- 实际 source-manifest SHA256：
  `1ecc3be36e62e510f3ccf0c5c572d743824f41541aba0554a626d2c31a2c32c3`。
- 原 result 对象的准确原字符串（无末 newline）26543字节，SHA256：
  `ad156b7c83a498437e13a750bfe040618bc7facb6e71cfd92205f2be8cdda6e7`。
- 完整 job log 326690字节，SHA256：
  `1598f075d2359bcdbee811198c5593932a6add1328b46ab045c6c25c6dd6faf5`。
- 同一 LEFT 全操作流 SHA256：
  `7dd4c258aef2a468104087309d50ae6e2b63a7901ecd02aff6c0f64758daf0d4`。
- 真实非方完整除法每原 source SHA256：
  `7362f43a1806e4a2be23ee5f0eab7e5da1981fdc1424d006cc0ba4232bb1bc96`；
  全 solution SHA256：
  `6e4409940f51774c6b464ef116ef041403d4a2d4a97841aa904cec39c9d99892`。

该回执只确认已证明算法的实际实现路径和原域返回。
原 F 的两图、四交、厚度、完整除子和 shadow 仍须由后继真实原作业取得，
不能把此处算法例的成功转写为原几何成功。


## 6. 已审持有的原 Artinian v6（未触发）

在§5.4真实小 API 通过后，后继只替换共同常数 helper pin、实施标识、
request版本，并在原 $F_y$ 两图的实际完整 paired graph 后加入如下门：

1. 从同一 `six.artin_constants["theta17"]` 取得原 $\theta_{17}$，
   对每个原 $N$ 系数验证除 $\theta_{17}^{-3}$ 后在原素域，并完整乘回。
2. 完整原像 receipt 必须将原 $M_N$ 与原 $Y$ 的摘要准确连接；
   最后完整左除法 receipt 必须将原 $M_D$ 与原 $X$ 摘要连接，
   并返回每个原 source 行，不改源行或目标。
3. 实际 $(YM_N)^{\mathsf t}$ 整块必须进入已通过的小 API 路径；
   原306维 LEFT/全attached/全操作/hash/原环返回全部逐项核。
4. 候选 $\gamma_B$ 不被误定为恰等于 $\theta_{17}^{-3}$；
   要求其比值 $\gamma_B/\theta_{17}^{-3}\in\mathbf F_r^\times$，
   从真实原二次域坐标恢复并核每个乘回身份。

相对§4的45源列表逐项相同，全部旧绑定、两份原 PASS pins、
$r=29$、q2453、batch64、minimal、shadow/artinian、
全七映射/两图/四交/厚商/完整 Tate 迹及18×9门保持。
三份最新不可变源码如下；§4的v5仅为历史版本，不再选作后继。

| 路径 | blob | 字节 / SHA256 |
|---|---|---|
| `scripts/produce-original-triangular-artinian-shadow.py` | `b27129766ae5b336f7f1eb233115329bda7028bb` | 27682 / `e3b8bd5135087ffc5d4d80a7680a776ef31b6ea9baefa09e9e8119363932e8cf` |
| `scripts/launch-original-triangular-artinian-shadow.py` | `b95137b9e98162cfaf51efdd5ae88d3d13fc3ccf` | 10316 / `8df6cf6c56a9b1056e5f7c389d6b486eff98f7bc65cd7c19d30f3523fb81311c` |
| `ci/original-triangular-artinian-shadow-request.json` | `edfdfc0b4018c39ff65b43dbe4f9113712f2af4b` | 834 / `27354233d51e947d828914c240e21822798c54c3ba80552fdd51e354db0e525e` |

workflow 仍为 blob `5713d440f42e1bd2f638944ce2dc9d3d4ddd1d5b`。
本节只登记已审源码；尚未挂到触发路径，尚无v6执行回执。
继续等唯一原F作业的真实终点，按其实际结果接入，不并开同一原306重算。


## 7. 同一完整矩形原像的素域与单常数下降

本节补足§5.1实际原 F 链中仍在二次域工作的一个完整阶段，
不改变已审 v6 或正在运行的原 F 作业。
原 `complete_triangular_preimage(H,M)` 从
`R=H.base_ring()` 起，在这个原二次域的多项式环内做
全部余式、逐列 `quo_rem/xgcd`、完整残余行和完整来源行更新。
此前 R956 只可能在最后的来源 HNF 才尝试素域下降；
即使最终规范原像在素域，中间来源行也可能混有原常数及其逆，
所以末次 HNF 的接受门不保证已经降低整条列约束链的域成本。

### 7.1 完整矩形原像及规范源基

令 $f=\mathbf F_r\subset k=\mathbf F_{r^2}$，
$R_0=f[t]\subset R=k[t]$ 都取调用者原嵌入，且
$$
H\in\operatorname{Mat}_{n}(R_0)
$$
为完整、首一、非退化上行 HNF。令原 $M$ 有 $r_0$ 行、$n$ 列，
不要求 $r_0=n$，只在**全部**系数通过
$$
M=\gamma\,\iota(M_0),\qquad
M_0\in\operatorname{Mat}_{r_0\times n}(R_0),\quad
\gamma\in k^\times
\tag{16}
$$
后接受。$H$ 本身不作任何常数缩放。
设
$$
\mathcal P_0
=\ker\{R_0^{r_0}\xrightarrow{\,M_0\,}
               R_0^n/\operatorname{row}_{R_0}H\}.
$$
原完整原像恰为
$$
\boxed{\quad
\mathcal P
=\{v\in R^{r_0}:vM\in\operatorname{row}_RH\}
=R\otimes_{R_0}\mathcal P_0 .
\quad}
\tag{17}
$$
证明：$R$ 平坦，故保完整映射核；常数 $\gamma$ 是 $R$ 单位，
乘它不改变 $R^n/\operatorname{row}_RH$ 中的零条件。
$\det(H)R_0^{r_0}\subset\mathcal P_0$，故原像总为满源秩 $r_0$，
包括 $M_0=0$ 的情形。没有假设 $M$ 自身满秩。

对原 R942 的完整逐列算法只换系数环，
仍保每一来源行与每个厚目标因子。
其返回的规范 HNF $Y_0$ 经同一嵌入仍满足原 HNF 条件，
由规范形唯一性
$$
Y=\iota(Y_0)
\tag{18}
$$
就是全部原 $\mathcal P$ 的规范源基。
**返回的来源 $Y$ 不乘 $\gamma$。**
后继 paired solver 仍收到未改的原 $M_N$，
因此其真实 RHS 仍为 $YM_N$，原 $X$ 的尺度没有变化。

接受门复用§5已经实际通过的纯系数转换函数：
第一矩阵是整个 $H$，第二矩阵是整个矩形 $M$。
该转换函数不做行操作、也不要求两个矩阵同行数；
完整 HNF 函数对 attached 同行数的要求是另外的调用者约束。
本节明确记录第二矩阵的角色为**原 operator**，
不把它冒称为一个同行附加变换块。
每个 $H$ 系数原本就须在素域；
每个 $M$ 系数除同一候选 $\gamma$ 后都须在素域，
每个完整多项式都乘回原值。任何一项失败，
完整原 $H,M$ 原封送入原二次域流程。

### 7.2 原域全列操作的精确提升

需要区分真正执行的素域操作流与其在原域上的完整解释。
假设一列开始时，素域算法保有完整来源 $P_0$ 和残余 $W_0$，
满足
$$
W_0\equiv P_0M_0\pmod{\operatorname{row}H}.
$$
对应原域残余是 $\gamma W_0$，
来源仍是 $P_0$，因为完整 HNF 余式运算与常数相乘交换。

素域该列的实际附加阵为
$$
\mathscr A_0=
 \begin{pmatrix}W_0&P_0\\-H_j&0\end{pmatrix}.
$$
原问题的同一附加阵为
$$
\mathscr A=
 \begin{pmatrix}\gamma W_0&P_0\\-H_j&0\end{pmatrix}.
$$
先只把末尾那一个目标行 $[-H_j\mid0]$ 乘 $\gamma$，
得到残余块 $\gamma\binom{W_0}{-H_j}$，
而完整来源块 $\binom{P_0}{0}$ 未变。
接着逐个应用素域实际算法的完整幺模行操作 $U_0$；
原残余块始终是素域残余块乘 $\gamma$，
原来源块则始终等于原嵌入下的素域来源块。
这些都是全行操作，保全部 $r_0$ 个来源坐标。

素域归约结束时首行主元为首一 $g$、其余 $r_0$ 行该列为零。
对应原主元是 $\gamma g$。只把即将舍去的**非核首行**
乘 $\gamma^{-1}$ 后，原主元恢复为首一 $g$，
全部保留的零行及其完整来源投影不变。
所以原域全操作为
$$
\operatorname{diag}(\gamma^{-1},1,\ldots,1)\,
 \iota(U_0)\,
\operatorname{diag}(1,\ldots,1,\gamma).
\tag{19}
$$
其行列式等于 $\det(U_0)$，确为原 $R$ 单位。
两次额外操作从不缩放保留的来源核行。
原完整一列核的投影仍因 $H_{jj}\ne0$ 而单射，
故所有 $r_0$ 条零行确实生成整个下一原像，不是只生成一个包含子模。

同时
$$
\gcd(H_{jj},\gamma W_{0,1j},\ldots,\gamma W_{0,r_0j})_{\rm monic}
=\gcd(H_{jj},W_{0,1j},\ldots,W_{0,r_0j})_{\rm monic},
$$
每层首一指数因子 $H_{jj}/g$ 原样保留。
逐列完整返回的来源基与累计首一行列式因此和原问题严格一致，
包含所有非分裂因子及重复层；未进行多项式因子分解。

### 7.3 实现与两个不可混淆的操作流

`complete_triangular_preimage` 的公开函数名、函数对象和所有消费者接口保持。
只有完整系数门成功时，内部 $H_0,M_0,W_0,P_0$ 与所有
`quo_rem/xgcd`、源行更新及余式规约改在 $R_0$ 工作。

最终先把完整 $P_0$ 注入原 $R$，再调用已通过的 R956 HNF API。
这个调用的实际算法仍在素域，但旧
`complete_source_basis_reduction` receipt 的来源与输出 hash
继续准确按**原 $k$ 坐标**记录。
返回后实际计算全部
$$
Y\,M\quad\hbox{并逐行除以完整原 }H,
\tag{20}
$$
要求全部余式为零；同时核原 $R$ 对象、$r_0\times r_0$ 完整形状、
首一 HNF 与原累计首一 index 相等。不是用 $YM_0$ 的返回替代 (20)。

原 target/operator/result/index 哈希仍指
$H,M,Y,\det(Y)$ 的原给定域表示。
每列 `whole_residual_column_sha256` 继续编码真正的
$\gamma W_0$；另列 native 残余摘要作区分。

实现分别维护：

- native 操作流：记录真正执行的素域完整操作及其素域系数编码；
- 原域提升操作流：将每个 native 操作系数注入原域，
  并在每个非零列加入 (19) 的前后两次原常数单位操作。
  原 `full_operation_stream_sha256` 和 `operation_counts` 指这一份。
  新 `native_full_operation_stream_sha256` 及
  `native_operation_counts` 指前一份。

这两份摘要从不冒称相同。
原域流是经 (19) 完整证明的提升，不假称逐层额外物化并重复计算了所有原域大行。
receipt 明确区分这一情形与完整 fallback 时的直接原域执行。
附加的 scale 次数恰为每个非零列二次，其余操作计数相同。
若没有任何非零约束列，额外次数为零；零源返回全部 $I_{r_0}$。

这针对真实原 F 的整条列约束链中的二次域多项式费用。
尚无实际原306耗时回执，因此不写加速倍数或资源保证。

### 7.4 复用已有三角原像小 API

只改三个已有触发路径：
`scripts/original_triangular_preimage_tools.py`、
`scripts/check-original-triangular-preimage-api.py`、
`ci/original-triangular-preimage-api-request.json`。
当前本课题61份 workflow 的完整 push paths 已核：
三者仅命中
`.github/workflows/rank2-sha-triangular-preimage-api.yml`
（blob `b3f30906e51d0287cb38757767eef6b94f47b433`）。
不改 bounded helper 本体，也不触发其独立小 API、原 F 或 Artinian 重型作业。

新 request v2 保原给定 $k=\mathbf F_{29}[a]/(a^2-2)$ 和旧完整两个 preflight。
在同一公开 job 现场生成一个原素域不可约三次 $q$，
并核它在原二次域仍不可约；目标分别保 $q^2$、$q^3$ 和 $(t-1)^3$ 全厚度。
给原 $\theta_{17}^6=17$、$\gamma=\theta_{17}^{-3}$，
测试完整 $3\times2$ 的 $\gamma M_0$。
官方原域完整 kernel basis of $\binom M{-H}$
经全部来源投影和完整 HNF 后必须逐项等于本算法的 $Y$；
其**全部目标坐标**也一并返回，逐行核 $YM=AH$。
另核零来源、真二次目标 H、包含两个独立常数方向的 M 的完整 fallback。

同一个 $M_0$ 与 $\gamma M_0$ 的规范源基必须相同；
native 操作流相同，原域提升流则准确含额外单位操作，分别核摘要与计数。
所有原输入/输出/index、最后完整 source HNF 和原 M 回乘也逐项核。

源码身份：

- 原像 helper：23261 B，SHA256
  `f1f3f7925bfdc32e771111c4a512a81470229473fd25f9193cd3a6f38a22d9fd`；
- 既有 API reader：13309 B，SHA256
  `ba3d9df5ad66255289eea8c1c492e0ceead2dd57944eade1c1fc9404df235fa3`；
- request v2：347 B，SHA256
  `76faf3a6849e211a8925aa97056aabb13265bbad1f5c18bb4856c3b627737c0c`。

本节的独立真实公开 API 回执已取得，见§7.5。
后继原 Artinian v7 可在通过后固定新增 preimage pin，
并在同一原 $F_y$ 两图要求真实 $H_D,M_N,Y$ 来源链进入上述接受门；
源数仍45，原 bounded pin与全部真实 PASS pins 不变。
当前v6仅为已审持有版本，在新回执之前不因本节改变选择或触发原306。


### 7.5 完整原像下降的实际小 API 回执

source `6ae52365ac2b87197085d8bec545ad5f9eec6800`，
[run45836149006](https://github.com/Rogerhu12/math-research-public/actions/runs/45836149006)，
job `139965432077`，2026-11-26 14:10:21 UTC 实际完成，**success**。
13份源码 AST 通过，数学 reader 0.492784613000012秒。
真 $3\times2$ 单常数源、原两域均不可约的三次因子全二/三厚层、
全部官方原域 kernel/source/target 坐标返回、零源及两类完整 fallback
全部实际通过。旧两套完整接口也通过；没有重算原几何。

同次真实 $\theta_{17}=(0,21)$、$\gamma=(0,8)$。
真共同常数例的两条非零列，native 操作计数
add4、bezout2、swap2、scale0；原域提升恰另有scale4。
完整两流分开记录，全部源坐标不缩放，最后按原 $M,H$ 实际回乘。

- 完整 source-manifest 3214字节，SHA256
  `20665ba352448fd752c3cb3a5e8cec3d925f162dfbb065b90b9c6716c724dd9b`。
- 原 result 字符串（无末newline）69477字节，SHA256
  `84f5c76b4741535683457d6a64ac8add20741310beda88f697d2a08e606b2082`。
- 完整 job log 含原BOM，181357字节，SHA256
  `b3803f3bb805c2bbfe2b4a034c49e9ac0ccceb3e5ad6929cf81bd8819562467f`。
- native 全操作流
  `4f011d8cd983f1ce95a801c449d74517fb069fbb2e073fe5866dc49dea58ef12`；
  原域完整提升流
  `37341f1e708b80e339b41f559c7db66d2eaf29cc7b37ba0f9ea5262db5cfdd70`。
- 全部原目标坐标 SHA256
  `136251e379749a3ba320bee4d63fd02d6a4e316628b36ffaf00e9780d8928ff7`。

这些是同一完整算法和实际返回的回执，原306几何仍没有由此冒记成功。

## 8. 原 Artinian v7 的完整输入与实际启动

v7相对§6的v6只增加§7完整 preimage pin和实际原F两图门：
原 $H_D,M_N,Y$ 的全部摘要必须连接，原306源/目标全形状、
真正素域工作环、$\gamma_B/\theta_{17}^{-3}\in\mathbf F_r^\times$、
原 $M_N$ 完整回乘、native/原提升两流及每个非零列两次额外单位操作
都逐项要求。最终来源 HNF 的原哈希和规范 $Y$ 再次连接。
它不要求新算法的非规范中间 $P$ 与旧算法字面相同；
原 $H_D,M_N$ 和最终规范 $Y$ 才是相同的实际对象。

45份 source、已通过的 bounded pin、原两份 PASS pins、
r29/q2453/batch64/minimal以及全部旧原门不变。

| 路径 | blob | 字节 / SHA256 |
|---|---|---|
| `scripts/produce-original-triangular-artinian-shadow.py` | `d066359fafcbc377757bb4782f84656f8b44d984` | 31897 / `90111bcd9191c91e58d6ec124ea75cc07ce44ab1a37b59c97eca6608a4089f96` |
| `scripts/launch-original-triangular-artinian-shadow.py` | `69ef54575a71bf1ab91cda87959ad6e0ae1f2d47` | 10317 / `156d2ff1fb58dd46b462f3ee08fb8019d9be5a278001917a0fccc4345c8c0486` |
| `ci/original-triangular-artinian-shadow-request.json` | `975bced4fb2130a46ca47209f30fe17b29426fda` | 835 / `aec8f1d46935ffc9686f86c66bb79774aa2a5906af656d39fc826e76ccd37050` |

workflow仍为 `5713d440f42e1bd2f638944ce2dc9d3d4ddd1d5b`。
2026-11-26 14:24 UTC，原F v3已实际350分钟超时，完整日志与已见瓶颈见
[几何记录§4](../notes/2026-11-26-geometry-7d29.md)。
本次将以上三份v7源码及原审定workflow同时挂入实际触发路径，
启动唯一后继原306/全厚shadow作业；source/run/job在平台生成后登记。
workflow为1654字节，SHA256
`4f81e15af934ae89cd98722427853679581297c1a424a7e4372ff79fc1ff8622`，
四个准确push paths、ubuntu-latest、360分钟job、21000秒host，权限只读。
原F实际θ17=[5,10]而tiny为[0,21]；本v7从原same six.artin_constants读取，
核θ17^6=17并逐系数/全部Frobenius返回，不假定特定域生成元或纯虚坐标。
原全部门与两份原PASS pins保持；不能把两个小API的成功当原除子或shadow成功。

### 8.1 v7 实际 source/run/job

source `6e79456aa2250a589306ba39d983ecdc46a2f267`，
[run45838674625/job139974211422](https://github.com/Rogerhu12/math-research-public/actions/runs/45838674625/job/139974211422)，
2026-11-26 14:24:22 UTC启动。14:25 UTC实际checkout及固定Sage镜像步骤成功，
原两PASS认证与完整数学step4运行中。只启动这一份原306；
运行状态不等于任何后续数学门已通过。
