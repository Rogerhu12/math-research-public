# 固定 $T,a$ 的九列高度可行多面体：一次 LP/QP 与完整重构

状态：**已实现独立公开 Actions 接口，尚无本接口的公开人工或研究运行回执**。本次只改变所选场的九个高度系数；不改变 $u,v$、度量、核心、准确帽或不可变 $c_0$。先在原 $[-1,1]^9$ 内检查可行性，不自动扩大系数盒，也不启动联合度量求解。

新文件：

- `scripts/frame_height_polytope.py`：17617 字节，SHA256 `6babe655e5d2ae48a54a4b2dad24685c433bd0d8ea902e231ffe0a64cd0afd8c`。
- `scripts/frame_height_polytope_audit.py`：28426 字节，SHA256 `b43189a3cfc82ca8569f6f28469946ef2ac03605c4b2bd0eecebe1385476a502`。

本地只做源码 AST 语法检查和公开 JSON 的读取解析；没有重新评价任何真实候选几何或运行研究优化。

## 1. 实际证据决定本次范围

公开 run43627111925 的 [完整报告](actions-43627111925-1-short_entry_audit/frame-entry-short-bounded-initial-audit.json.gz) 及 [科学摘要](actions-43627111925-1-short_entry_audit/frame-entry-short-bounded-initial-audit-summary.json) 表明，短 $\ell=81/1000$ 的两种表示都未通过 B7 单列初值步骤。

paired 的单列阻断在材料点 $t=27/80,\theta=\pi$：

$$
z=-0.008378686701374954,\qquad
I_4=0.0028397457348716825,
$$

故所选 $z\ge0$ 样本门要求 $\Delta c_4\ge2.950505954982465$。bounded 的阻断在 $t=33/100,\theta=\pi$：

$$
z=-0.007068638169461988,\qquad
I_4=0.002065049403530647,
$$

要求 $\Delta c_4\ge3.422987439126942$，都超过原系数盒的容量。第五高度系数原值准确是 $-1+2^{-53}$，因此准确上调容量为 $2-2^{-53}$，报告的 binary64 上界显示为 $2$。单独帽高门所需增量约 $1.07$；失败原因是 B7 在较早的 $t\approx.33$ 处累计积分还小，不能由此推出九列总容量不足。

两场 160×768 样本的直接度量误差分别约 $1.460$ 和 $1.341$，仍由入口控制；新高度可行性步骤不自动修好这一缺口。选 bounded 只作为本次明确的默认输入，不声称它已经可嵌入或优于 paired 的每一个几何指标。

这里的 $z\ge0$ 是**当前正侧镜合结构选定的分离 screen**。有限样本上的单列空集，不是一般曲面嵌入或所有等距族不存在的结论。没有把负 $z$ 的一次浮点评价升级为连续交叉证书。

## 2. 九列支撑与保持的条件

高度速度基是原五次 clamped B 样条 $B_{j+3}$ 乘已冻结入口权 $W_4$。当前 $\ell=.081$，入口结束于 $117/1000$。原九列支撑依次为：

| 局部列 $j$ | 原支撑左端 | 原支撑右端 | 原未加权全积分 |
|---:|---:|---:|---:|
| 0 | $9/250$ | $9/25$ | $27/500$ |
| 1 | $9/250$ | $441/1000$ | $27/400$ |
| 2 | $9/250$ | $261/500$ | $81/1000$ |
| 3 | $117/1000$ | $603/1000$ | $81/1000$ |
| 4 | $99/500$ | $171/250$ | $81/1000$ |
| 5 | $279/1000$ | $153/200$ | $81/1000$ |
| 6 | $9/25$ | $423/500$ | $81/1000$ |
| 7 | $441/1000$ | $423/500$ | $27/400$ |
| 8 | $261/500$ | $423/500$ | $27/500$ |

积分公式为 $(k_{i+6}-k_i)/6$。前三列穿过入口权区，其**实际加权积分**必须按冻结模型的 $I_j$ 取得，不能直接套表中原积分；其余六列不受入口权影响。所有实际 $C_j,I_j$ 非负，故较早的前三、四列能够补足单列 B7 在 $.33$ 附近贡献很小的问题；是否能同时满足球与全部高度行，仍须运行本次多面体步骤。

九列保持入口和尾的速度一、二 jet，因而保位置 $C^2$ 接口。改变高度系数只改变单一共同原函数，尾部得到一个共同平移量，不会逐圈重新选择帽高。核心、帽形和完整 $g$ 均不变。较早列会改变入口后的 $b$，所以真实 $E,F$ 和曲率需要完整重构，不能沿用原场结论。

## 3. 每径向行的准确线性压缩

固定当前 $T,a$，令当前高度系数为 $c^0$，当前位置样本为 $X^0_{ij}$。侧号 $\sigma=\pm1$，定义

$$
G_{ij'}=\sigma I_{j'}(t_i),\qquad
s^0_{ij}=\sigma z^0_{ij},\qquad
\zeta_{ij}=s^0_{ij}-(Gc^0)_i.
$$

任意新高度系数 $c$ 的有符号高度为

$$
s_{ij}(c)=\zeta_{ij}+(Gc)_i.
$$

所有水平坐标不变。若某个固定水平样本已经有 $x^2+y^2>R_{\rm ball}^2$，任何竖直高度变化都不能使它入球，接口直接保存该固定水平阻断，不调用 LP。

否则令

$$
q_{ij}=\sqrt{R_{\rm ball}^2-(x^0_{ij})^2-(y^0_{ij})^2}.
$$

在一行所有角样本上同时要求选定 $s_{ij}\ge z_{\min}$ 与入球，等价于

$$
\ell_i\le (Gc)_i\le u_i,
$$

其中

$$
\ell_i=\max_j\{z_{\min}-\zeta_{ij},-q_{ij}-\zeta_{ij}\},
\qquad
u_i=\min_j\{q_{ij}-\zeta_{ij}\}.
$$

每行只需两条线性不等式。实现保存取得每个极值的原材料点索引与数值；没有只保一组任意挑选的角点。实数算术下这与原完整角样本约束等价，浮点压缩仍如实标记为数值结果。

共同帽高另给

$$
h_{\rm base}+\lambda\cdot c\ge h_{\rm target},
\qquad
\lambda_j=\sigma I_j(L).
$$

本次采用 R66 的所选上支和 $.001$ 明确余量；$\tau=.061$ 是选定 reach 设计值。与原九维系数盒相交后得到凸多面体。默认 160 条径向行只产生 $321$ 条线性行，未知数仍为九个。

**该多面体冻结当前 $u,v$。** 这不同于只含共同帽高的 Gate：后者的行不依赖当前 $u,v$，而这里的 $\zeta_{ij}$ 依赖 $T$ 的完整角原函数。以后联合优化改变 $u,v$ 时，必须重新计算局部高度与球条件，不能把这组冻结的行当作仍有效。

## 4. 阶段一：统一高度松弛 LP

将所有线性行写成 $Ac\le d$，先求

$$
\min s,\qquad
Ac-s{\bf1}\le d,\qquad s\ge0,\qquad -1\le c_j\le1.
$$

统一松弛 $s$ 的量纲是高度，各行没有暗用不同归一化。系数盒保持原样，完全不松弛。实现使用一次 `linprog(method="highs")`，明确时间与可行容差，并保存原始状态码、消息、求得的 $s$、未加松弛时的全部行检查以及最显著的 LP marginals。

有有限解或库报告 success 都不够：只有 $s$ 与实际原行残差通过声明的浮点门，才继续下一步。若失败，保存阻断行及原盒内每一行的独立容量筛；**不调用 QP、不应用高度步、不扩大盒**。数值 marginals 不是严格 Farkas 证书，也不能作为连续曲面不存在的证明。

另外，各行在盒内的最小值

$$
\min_{c\in[l,u]} A_i c
=\sum_j\min(A_{ij}l_j,A_{ij}u_j)
$$

可直接给出某一行单独已经无法支付的数值证据。本接口报告它，但不把“每行独立均可支付”误当成多行交集必非空。

## 5. 阶段二：温和高度初值 QP

LP 提供数值可用点后，只做一次严格凸距离 QP：

$$
\min_c \frac12\sum_j d_j^2(c_j-c_j^0)^2,
\qquad Ac\le d,\quad c\in[l,u],\quad d_j>0.
$$

默认 $d_j=1$。它的作用是从可行多面体中选择改动较小的高度初值，**不是声称已经最小化真实度量误差**。SLSQP 接收真正的线性约束和解析梯度；不依赖 `keep_feasible`。每个完成的试探都独立检查原行与系数盒，只在通过数值门的点中选取最低距离成本者。预算或异常保留已可用 LP 点，不在返回后默默投影。

当前不增加第三次四次式 metric 优化。固定 $T,a$ 的确可以用完整准确四次目标做低成本后续高度优化；本次先取得可行性和完整重构证据，只有真实输出显示距离 QP 初值值得继续时再明确启用。

## 6. 唯一实际应用与重构

driver 严格读取三个公开输入的原始 decoded SHA：

- 原独立高度 selected：`c1d81da9640c4fa2598a94e54b1e203e028c3bf914afeba5e25944b4360c6f46`；
- 原不可变 $c_0$：`6ff0b179af88589c1d87ee3408f068f14b02c310e2a9b300759426fa4550f1e3`；
- 已完成 short report：`9d64a1ea03745405bd72fce6078eace92e02f3987be6ae079b75f0b71f69502c`。

它回放整个 short state、所有准确系数、25 件冻结旧实现、完整 $g$、原 $c_0$ 与准确网格，再构造 polytope。输入支持 gzip，hash 指向解压后的原字节；存储字节另行绑定。

若有选中系数，只应用一次完整九列高度变化，然后完整调用权威 geometry。逐项核

$$
\Delta X=(I\Delta c)e_z,\quad
\Delta X_t=(C\Delta c)e_z,\quad
\Delta X_{tt}=(C'\Delta c)e_z,
$$

而三个含角导数的 jet 不变；同时核所有 $u,v$ 与度量系数逐位不变、$T$ 样本逐位不变。重新报告实际帽高、最低有符号 $z$、球、strip、$E,F,G$、曲率、浸入、镜合样本法弦与全部端口二 jet。

最后固定同一完整状态，只把角向 $\Pi$ 从 384 加到 768。原不可变 $b_0$ 与基积分没有改变，原 short report 的 Nb/GL 有限对照作为来源保留，不重复扫描；这并不是连续误差界。稀疏/密查询的全二 jet 再次比较，防止共同帽高被查询网格改变。

每个 checkpoint 同时写完整 JSON 和小 summary，后者绑定完整文件的 SHA/字节数。没有 joint $u,v$ solve，没有 metric design，也没有每次精化重新优化。

## 7. 公开 Actions 命令与开发范围

先执行完整人工入口：

```bash
python topics/visible-flex-new-mechanism/scripts/frame_height_polytope_audit.py \
  --check-only --out "$RUNNER_TEMP/height-polytope-development.json"
```

人工覆盖：已知二变量凸 QP、原盒不可行、固定水平出球、角压缩等价、严格人工 short-state/gzip 回放、一次 LP/QP 后完整几何重构、六 jet、summary 字节绑定、坏状态拒绝与 Actions guard。不伪造环境，不读取真实候选。实际回执前不得将它标成 passed。

随后只有在实际公开 lane 中运行：

```bash
python topics/visible-flex-new-mechanism/scripts/frame_height_polytope_audit.py \
  --input topics/visible-flex-new-mechanism/notes/actions-43618467921-1-independent_height_solve/frame-independent-height-bounded.json \
  --anchor-input topics/visible-flex-new-mechanism/notes/actions-43604231319-1-ellipse_enriched/frame-ellipse-enriched-fixed.json \
  --short-audit topics/visible-flex-new-mechanism/notes/actions-43627111925-1-short_entry_audit/frame-entry-short-bounded-initial-audit.json.gz \
  --expected-input-sha256 c1d81da9640c4fa2598a94e54b1e203e028c3bf914afeba5e25944b4360c6f46 \
  --expected-anchor-sha256 6ff0b179af88589c1d87ee3408f068f14b02c310e2a9b300759426fa4550f1e3 \
  --expected-short-sha256 9d64a1ea03745405bd72fce6078eace92e02f3987be6ae079b75f0b71f69502c \
  --case bounded_short --height-lower=-1 --height-upper=1 \
  --tau 61/1000 --height-margin 1/1000 --minimum-signed-height 0 \
  --out "$RUNNER_TEMP/height-polytope-bounded-audit.json"
```

实际 driver 严格拒绝任何与这三个 decoded SHA 不同的字节流。

参考：SciPy 官方 [HiGHS linprog](https://docs.scipy.org/doc/scipy/reference/optimize.linprog-highs.html) 与 [SLSQP](https://docs.scipy.org/doc/scipy/reference/optimize.minimize-slsqp.html)。官方资料用于核 API 与状态语义；几何结论只来自本题推导和实际输出，不能从库的 success 推出。

## 8. 首次公开人工通过并启用唯一实际stage

run43629562872/source46d6140c已success。已知两变量QP误差3.33e−16，角约束压缩与完整角集合差0；人工完整replay一步的六jet最大差7.41e−16，坏状态/gzip/summary/真实guard检查全部通过。不是实际曲面优化。现据此仅请求一次bounded_short真实height_polytope_audit，原输入/原盒/固定T/a/g不变；最多一LP一距离QP，最终完整重构和384→768同态检查。

## 9. 首次实际输入回放失败与准确修复

公开 run43629844644/source6eceaa9009bf0df900c5bed4aa038cc51e34e527 在输入 loader 处失败，未进入 LP、候选 geometry 或任何参数步骤。前面的三输入字节、完整状态和固定 $g$ 回放已经通过；失败是把所选 bounded 模型重建的网格**全部元数据**与原共享网格直接比较。

原 short driver 先以 paired 模型构造一个共享网格，再用同一网格评价 paired 和 bounded。网格的 `structural_partition.source_height_base_definition_sha256` 因而绑定 paired 的不可变高度参考。bounded 的准确坐标、构造断点与采样规则相同，但它自己的高度参考 hash 不同；这个字段还会改变外层 `definition_sha256`。这是可定位的 provenance 差异，不是重新选择采样点的理由。

本次修复保留严格检查：

1. 先按原 driver 的真实顺序重建 paired 网格，与公开网格完整字典逐项相等。
2. 再重建所选模型的网格，分别核两个网格自己的 digest 以及各自实际不可变高度参考 hash。
3. 只有这两个已解释的字段可以不同：高度参考来源 hash 及其派生网格 digest；删除这两项后，准确节点、全部结构来源和所有采样规则必须完整相等。
4. 回执同时记录两个完整网格 hash、原共享网格所有者及准确坐标相同的结论，不篡改原公开 provenance。

人工 fixture 已改为与实际相同的“paired 建网格、bounded 使用”路径；增加准确节点篡改拒绝、输入 loader 失败仍写出小 JSON 与绑定 summary 的覆盖。每个输入阶段都记录已通过的 raw SHA，异常报告明确声明 geometry/LP/QP 尚未启动。首次失败的日志与原人工回执全部保留，不能把旧人工通过当成已覆盖这条新路径。

修后源码为 28426 字节、SHA256 `b43189a3cfc82ca8569f6f28469946ef2ac03605c4b2bd0eecebe1385476a502`。本次只有 AST 语法检查；新人工路径尚待公开 Actions 实际回执。线性多面体、LP、QP、目标、系数盒和所有几何公式均未改变。

## 10. 修复公开人工通过并重新请求真实stage

公开 run43630530984/sourcec4cbe7f3fec9580d0ca4d9f7cc06c5360f803adc 已success。共享paired网格在bounded中逐节点回放、不同但分别准确的参考provenance、篡改实际坐标拒绝、输入失败小JSON及绑定摘要全部通过；六jet最大差7.41e−16、人工两变量QP差3.33e−16。修复后的driver仍为b43189a3；现立即请求同一bounded_short实际stage，不改变数学问题、原盒或冻结g。公开输出见 [开发回执](actions-43630530984-1-height_polytope_development/height-polytope-development.json)。
