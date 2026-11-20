# R671 新解析尾的完整连续首几何与六 jet 核

日期：2026-11-20。会话：Astra-larger-resume-24b2ab87-20261120 / geometry_path。

**状态：实现已完成；仅作 Python 语法编译与源码对照，尚未执行新的科学计算。** 新文件为 `scripts/resume_20261120/exact_reference_tail_interval.py`。它读取新 canonical bundle，重新支付该新场的连续界，不继承原 $\lambda=0$ 场的任何候选证书。

本文件实现 [R671](../results/R671-exact-reference-tail-affine-lift.md) 的准确参考尾。完整纸面余项推导见 [R674：连续 profile 与同角余项](../results/R674-reference-tail-continuous-profile-and-same-angle-remainders.md)。原径向和角核来自 [R657](../results/R657-complete-closed-relative-Gram-and-same-scalar-enclosure.md)、[R670](../results/R670-direct-same-angle-first-geometry-with-complete-tails.md)、[R672](../results/R672-complete-lowmode-sixjet-curvature-with-laurent-remainders.md)；此处只替换新 profile 及其逐导数误差，并保留全部原 $q$ 模和完整解析角尾。

## 1. 实际模型与输入身份

同一固定 $\lambda$ 的场为

$$
F=q+f e_r(\Theta)+(Hh+k)e_z,
$$

$$
f=(1-\lambda)\chi(R+S-s)+\lambda\eta a,
\qquad h=(1-\lambda)\chi+\lambda\eta,
\qquad k=-\lambda\eta I,
\qquad I(s)=\int_s^S\cos\alpha(u)\,du.
$$

新 reader 要求 bundle 带 `reference_tail_model_json` 与 `reference_tail_lambda`。若还带 driver 的 `exact_tail_lambda`，两者必须一致。canonical 定义必须准确匹配当前 mesh 字节摘要、$M$、node report、原 scalar 输入及已刊 factory 源。`dense/batch/observed` 三个实际底层源的 SHA 也逐一核对，`observed` 的两处来源声明必须一致；不能把任意外部 operator 以相同 schema 冒成这里的准确物理表示。

$\eta$ 的物理端点来自 canonical 定义的 `eta_start_symbolic`、`eta_end_symbolic`，即准确有理对 $(\alpha,\beta)$ 所表示的 $\alpha S+\beta$；节点编号只用于确认这些物理点属于当前网格。这样后续径向细分或 $M$ 补零可以明确更新载体字段，保持同一物理 $\eta$。不能把旧编号当作新网格上的物理位置。

连续核本身只需：当前 bundle、当前 node report、原 scalar 输入以及已刊源码。它不需要优化所用的 Gauss carrier。可选 `--reference-carrier` 必须匹配当前 bundle 的 `reference_tail_carrier_sha256`，且完整 `model_definition_json` 与当前 canonical 模型相同。只有其 `reference_active=true` 行可作为已付整数 oracle anchor；inactive 的零占位不代表 $a$ 或 $I$。

所有旧源均按既定 SHA 载入。原 factory 的 SHA 为 `2e0219c50543d859a9c649553bc4dde863df24daab26ffa75e5112baa4a90216`；R657 scalar 为 `f572c39c7c54f78c360194fd86a1eeba62335ca23f41062f6a7892653ef9a68e`；R670 首几何为 `eaa9a579eea227cbf348138295534144c39d07b669ea1c9ff494f22baa4ae599`；R672 六 jet 为 `8ca81feefda43fd4423bee1877c8e9198c7774afae0cf8cc2227424765dac385`。新报告使用新执行源的 SHA，不冒充其中任何一个旧源。

## 2. 新径向核

每个原胞先与原 scalar 全部分段、$\eta$ 两端点、旧 $\chi$ 断点相交。所有切分位置保持准确 $\alpha S+\beta$。之后每一层指定的径向二分，把每个解析片切成闭子片，并在该子片的准确符号中点建立新的 Taylor 模型。

默认 degree5；本实现开放的 degree 范围为3至8。由原准确曲率积分得到 $\alpha$ 的至多6次 power 系数；R657 的递推给出 $\sin\alpha$、$\cos\alpha$ 的 Taylor jet。原 FullHold 整数 oracle 在同一个 anchor 给出 $a_*$ 与累计高度，$I_*$ 由整数向外减法“总高度减当前位置高度”得到。不会将两个普通浮点积分相减作为函数定义。

由同一 power jet 解析形成 $A^{(r)}$、$J^{(r)}$，$r=0,1,2$，再分别转换到本片 Bernstein 系数。不会对已经含重复 anchor 区间的 Bernstein 控制点做差分；因此不会把本来应消去的常数误差放大为 $1/h$ 或 $1/h^2$。

设本片半径上界为 $R_*$，完整 Bell 导数界为 $B_5$，则逐导数截断误差为

$$
|a^{(r)}-A^{(r)}|,\ |I^{(r)}-J^{(r)}|
\le \frac{B_5 R_*^{6-r}}{(6-r)!},\qquad r=0,1,2.
$$

三个误差分别应用 Taylor 定理；没有对 $C^0$ 误差求导。anchor 与所有 Taylor 系数的区间宽度仍留在多项式系数里，误差项只支付截断余项。

$\eta$ 是准确 quintic，$\eta A,\eta J$ 次数至多10。乘积使用准确有理 Bernstein 权重，$q$ 与各 profile 升到统一 degree10 后，先合并 $q_{Z0}+Hh-\lambda\eta J$ 和相应水平系数，再做角包围。高度部分直接计算

$$
(1-\lambda)H\chi-\lambda\eta(J-H)
$$

以保留共同项抵消。$h$ 没有近似余项，$k$ 与完整竖直 profile 的误差相同。误差按 Leibniz 公式付给每一阶，而不是只付位置误差。

在 $\eta=0$ 的整胞，当前新场准确等于旧公式在**当前 $q,H$** 上的场。因此首几何和曲率可以调用原公式重新计算这些胞；这不是复用旧候选报告。这里也不查询 prefix 上未定义的 $I$。默认有非零 $\eta$ 的尾胞才调用新整数 anchor。

## 3. 全角尾和六 jet

对有限多项式部分，使用原 R670 的完整 Laurent 系数和同角闭弧变换。首先合并全部原有限 $q$ 与有限 lift 系数，然后才把 $L+1,\ldots,M$ 付为尾和；没有删除原高模。解析 lift 的 Laurent $>M$ 尾及实相位指数余项继续完整支付。

设 $e_{f,r}$、$e_{Z,r}$ 为新径向标量误差，$\varepsilon_r,\varepsilon_\rho,\varepsilon_B$ 为三个完整角乘子误差。六 jet 的额外水平误差为

| jet | 水平误差 | 竖直误差 |
|---|---|---|
| $X$ | $|\widehat f|\varepsilon_r+e_{f,0}$ | $e_{Z,0}$ |
| $V$ | $|\widehat f_s|\varepsilon_r+e_{f,1}$ | $e_{Z,1}$ |
| $T$ | $|\widehat f|\varepsilon_\rho+e_{f,0}R_\rho$ | $0$ |
| $AA$ | $|\widehat f_{ss}|\varepsilon_r+e_{f,2}$ | $e_{Z,2}$ |
| $VT$ | $|\widehat f_s|\varepsilon_\rho+e_{f,1}R_\rho$ | $0$ |
| $EE$ | $|\widehat f|\varepsilon_B+e_{f,0}R_B$ | $0$ |

这里 $R_\rho\ge|\rho|$、$R_B\ge\sqrt{|\rho|^4+|\rho_\phi|^2}$。这是准确恒等式

$$
fL-\widehat fL_{\rm fin}=\widehat f(L-L_{\rm fin})+(f-\widehat f)L
$$

的界，scalar 误差乘的是真实乘子模，故不遗漏两种余项的交叉。$e_{f,r}$ 是径向误差，不对其作角导。

角变换内存预算使用本次实际控制点数 `degree+1`，没有保留旧核写死的7。每个 batch 包围同一组径向子片、同一组闭角弧，支持函数、距离、法向与形算子的组合仍有同角相关性。

## 4. 可导入接口

```python
reader = module.ReferenceIntervalReader(
    repo=repo, bundle=bundle, node_report=node_report,
    scalar_input=scalar_input,
    reference_carrier=reference_carrier_or_None,
    angles=256, low_modes=24, angular_taylor_degree=12,
    scalar_degree=5, radial_block=4, panels=128, beta='1/4')
reader.set_resolution(1024, 48)
first = reader.first_cell(cell, 4)
curvature = reader.curvature_cell(cell, 4)
```

`pieces(cell)` 返回与 scalar/$\eta$/$\chi$ 共同分割后的准确片；`subpiece(cell,piece,j,count)` 返回其符号子片。`profile_controls(piece, include_target=True)` 返回：

- `f/h/k/z`：每个标量的0、1、2阶 Bernstein 区间数组；其中 `z=Hh+k` 已合并；
- `f_error/z_error/k_error`：对应三阶的完整统一误差，`h_error` 为零；
- `reference_a_jets/reference_I_jets/reference_jet_errors`：活动参考尾的共同 Taylor jet 与逐导数截断误差；
- `a_poly0/a_error0`：同一个目标 $a$ 的多项式与误差，可直接交后续 R657 分子消费者；
- `detail`：真实符号 anchor、所属解析段、半径及完整导数界。

`piece_definitions` 形成完整有限 Fourier 控制点与逐项尾预算，`blocks` 对需要的六 jet 做同角包围。`mode='curvature'` 直接复用 R672 的真实第一形式 Gram–Schmidt 形算子公式；不会用目标 $g$ 替代真实第一形式。

可选 `first_geometry_report` 只能来自同一个新源、本 candidate bundle SHA、本 node report SHA、同 canonical 模型且覆盖全部原胞。它只提供本场已付 $E,W^2$ 下界。旧 eaa 报告即使 $q$ 字节相同也不能作为非零 $\lambda$ 场的这个输入。

## 5. Actions CLI 与完整参数

先由已刊 `launch_full_phi_exact_tail_actions.py` 生成实际新场。以下路径中的 `candidate` 与 `reference_profile` 必须指向该次新场的真实输出，不是旧 `c4a3` 文件。原重建的两个固定输入默认位于：

```text
RUNWORK/fullclosed_solver/data/fullclosed-hold-warm.json
RUNWORK/fullclosed_solver/data/pulse-a5-complete-base.json.gz
```

首几何完整命令模板：

```bash
python "$repo/topics/visible-flex-larger-amplitude/scripts/resume_20261120/exact_reference_tail_interval.py" \
  --repo "$repo" --bundle "$candidate" \
  --node-report "$runwork/fullclosed_solver/data/fullclosed-hold-warm.json" \
  --scalar-input "$runwork/fullclosed_solver/data/pulse-a5-complete-base.json.gz" \
  --reference-carrier "$reference_profile" \
  --mode first --cells all \
  --levels 256:1:24,512:2:32,1024:4:48,2048:8:64,4096:16:96 \
  --angular-taylor-degree 12 --scalar-degree 5 --radial-block 4 --panels 128 \
  --beta 1/4 --target-support .14 --target-diameter 4.1 \
  --out "$runwork/postprocess/reference-tail-first-geometry.json"
```

可省略 `--reference-carrier`：此时所有新中心由原整数 oracle 查询。给它只是复用同一个准确中心已有的盒，不改变目标或任何公式。

随后曲率命令保留上述必需输入、level与全部 degree/块/原oracle参数，明确改为：

```text
--mode curvature --target-curvature 8.1
--first-geometry-report RUNWORK/postprocess/reference-tail-first-geometry.json
--out RUNWORK/postprocess/reference-tail-curvature.json
```

这里 `8.1` 是请求的候选界，尚未有运行结果。未付胞只在下一层细化；每个实际 pass 的角数、径向数、保留角模与累计耗时均保存在报告。每32胞及每层结束写一次完整 raw 进度报告，最终报告绑定实际 bundle/source/model SHA；raw 留同一 Actions 工作目录，不入 Git 或 Release。

源码也提供 `--mode metric --target-metric 1e-6`：这是用新完整 field 盒直接计算相对 Gram 的严格、可能较宽的连续界。它明确不声称已实现 R657 的紧分子多项式抵消。`a_poly0/a_error0` 和全部 profile 已为后续该消费者准备，不能把这份宽界的未通过叫作原方程无解。报告的 `metric_certified` 只在完整覆盖且上界不超过 README 的 $10^{-6}$ 时为真；不会把更宽的命令行目标冒成完成标准。任何一次界都不替代固定参数网格/频率精化的真实求解收敛。

CLI 本身核对公开仓库 Actions 环境。交付时没有调用上述任何命令，没有新 candidate 数值、run 编号、几何界或求解接受结论可登记。

## 6. 结果范围

首几何完整覆盖后，原 R670 两盘、镜像、支持嵌入、全直径及两符号固定见证距离公式可用于这个实际新场。新报告可据实给出完整嵌入和 held/D 界；曲率消费者另付真实六 jet。它们都不独自宣称 reach。

旧 `fullclosed_nonplanar_coefficients.py` 的水平轴 trace 用旧 $\chi(R+S-s)$，并将原胞称为多项式；非零 $\lambda$ 下不能原样沿用。此 reader 不调用它，`nonplanarity_certified`、marker 与含反射 Euclidean shape 距离标签均保持未付。后继 R675 消费者采用更直接的论证：本场完整嵌入一旦已付，两组相反轴点不能相同；固定 $s$ 的角实解析性配合每原胞至少一个非零高 $Z$ 模，排除平面开片。这只需当前场高 $Z$ 三 jet 与同场完整 embedding 报告，无须重复轴 trace 的 $a/I$ oracle。该消费者实际返回前不移用旧 marker 证书。

本实现不更改原求解自由变量、帽接口、core、固定 $g$ 或完整问题标准。它只使 R671 的真实解析尾能够进入已证的连续几何计算。

执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
