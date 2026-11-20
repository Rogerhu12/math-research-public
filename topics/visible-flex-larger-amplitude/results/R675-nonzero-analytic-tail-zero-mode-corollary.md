# R675 补充：非零解析尾即使所有高度角模为零，也没有平面开片

日期：2026-11-20。会话：Astra-larger-resume-24b2ab87-20261120 / fullclosed_solver。

**状态：完整条件命题与独立 v2 消费者草案，仅 AST；没有科学执行。** 已刊 R675 的 b36d 源、first/K 的 f122 源和现有几何合并器均保持冻结。本条增强只用于今后需要时，不给当前计算增加启动条件。

原 [R675](R675-embedded-activity-nonplanarity-from-height-jets.md) 用每个原胞一个非零高度角模支付充分条件。对非零 R671 解析尾，这不是必要条件：未来某段若精确变成轴对称参考尾，所有高 $Z$ 模可以为零，但曲面仍不是平面。以下命题直接排除这种尾部水平开片，不需要另查 $a/I$ 数值。

## 1. 局部命题

在同一准确闭嵌入上，沿用 R675 的全部角奇偶性。设某原胞的一个径向开区间在 Hold 的单个解析段内，并避开有限个 $\eta/\chi$ 断点；在该区间中

$$
F_z(s,\phi)=q_Z(s,\phi)+Hh(s)-\lambda\eta(s)I(s),
\qquad I'(s)=-\cos\alpha(s).
\tag{1}
$$

假设：

- $\lambda\ne0$；$\eta$ 是不恒零的多项式。
- $q_{Z,0}$、$h$ 在该局部区间都是多项式。
- $\alpha$ 是非恒定实多项式。

那么该区间上的活动面不存在任何非空平面开片，无需假设任何高度角模非零。

证明的前半完全复用 R675：准确嵌入保证同一纬圈的两组相反轴点不重合；固定 $s$ 的角解析延拓迫使任何平面开片只能是水平面。由角 Fourier 唯一性，水平片上的所有非零高度角模都为零，而其零模必须满足

$$P(s)-\lambda\eta(s)I(s)=c,\qquad P=q_{Z,0}+Hh.\tag{2}$$

缩小到 $\eta\ne0$ 的开区间，可得 $I=(P-c)/(\lambda\eta)$ 为有理函数；微分后 $\cos\alpha$ 也为有理函数。下面的引理排除这个可能。

## 2. 非恒定多项式的 cosine 不可能是有理函数

设 $p$ 是非恒定实多项式。若在一个实开区间有 $\cos p=U/V$，其中 $U,V$ 为多项式、$V$ 不恒零，则整个函数

$$V(z)\cos p(z)-U(z)$$

有积聚零点，故恒为零。于是 $\cos p$ 作为有理函数的所有有限极点都可去；它必是多项式。

但设 $p(z)=a_dz^d+O(z^{d-1})$，$d\ge1$、$a_d\ne0$。可选复射线 $z=re^{i\theta}$，使 $\operatorname{Re}(ia_de^{id\theta})>0$。沿该射线，$e^{ip(z)}$ 按 $\exp(c r^d+O(r^{d-1}))$ 增长，而 $e^{-ip(z)}$ 衰减。因此

$$\cos p(z)=\tfrac12(e^{ip(z)}+e^{-ip(z)})$$

不可能只有多项式增长，矛盾。引理和第1节命题得证。

此论证只在一个解析子段内进行。它不要求跨原 Hermite 节点、Hold 接段或 cutoff 作径向解析延拓。任一非空二维开片都能缩小到这样的开矩形，有限接缝没有二维内部。

## 3. 现有准确 FullHold 为什么满足这个结构条件

固定 FullHold 源 SHA256 为

`a1ed8fa5d2186f400ea50a1d609574ec6996e59317a57638a6820a59cf0e7670`。

其准确 cut 是源码 `Fraction(float(.995))`，并非另换成十进制有理数。cut 之后由三条多项式 ramp 和两个常曲率段组成：负常曲率为 $-5/2$，正常曲率为 $3/2$；fall 末值为 $-5/2$，rise 连接 $-5/2$ 与 $3/2$，out 从 $3/2$ 降到 0。每段的曲率多项式都不恒为零。孤立零点不构成开区间；终点曲率为零也不产生平面开领。

因此每个开解析段的角函数 $\alpha$ 都是非恒定多项式。其常数项可能依赖准确初始标量或 $\pi$，不影响引理；证明不要求这些常数是有理数。

已冻结新 first 源 `f1220a2e83578bb186ec1043c5dc5fd70dd988f1a108897537117344590de225` 在建立同场连续报告时，已经核对 canonical FullHold/输入/节点身份，并要求 $\eta$ 从 Hold 内部的原节点开始，且在 out ramp 之前达到 1。对每个 $s>\eta_{\rm left}$，准确 smoothstep $\eta(s)>0$；在每个有限局部段上它是次数至多五的多项式。

R671 的 $h=(1-\lambda)\chi+\lambda\eta$ 同样分段多项式。原 $q_{Z,0}$ 仍是每原胞的五次 Hermite 多项式。因此，只要 canonical $\lambda>0$，**每个在 $\eta$ 起点之后的原胞内部自动满足本命题**。无需角模非零，也无需新的轴迹或标量 oracle。$\eta$ 起点之前的原胞继续使用 R675 非零高 $Z$ 模充分条件。

## 4. 独立消费者草案

源 `scripts/resume_20261120/exact_reference_tail_nonplanarity_v2.py`，11532 bytes，SHA256

`df8f3f1e876d3bc7f970de1748aa3e9f46a5b9d71193d0ea94d69aa1672036ea`。

它仍先绑定同一实际 bundle/node/model 和同一完整新 first 报告，且只有后者支付嵌入时才输出活动片非平面结论。有限系数扫描不变；对高 $Z$ 六端 jet 全零的胞，仅在下列条件下使用新的替代证明：准确 canonical $\lambda>0$、$\eta$ 两端节点/符号身份相符、准确 $\eta_{\rm left}>\mathrm{cut}$、scalar source 为上述固定 FullHold、并且该胞在 $\eta$ 起点之后。

新 schema 为 `R675-reference-tail-embedded-activity-nonplanarity-v2`。输出同时保留：

- `selected_witness_count`：确实用非零高 $Z$ jet 支付的胞数。
- `analytic_tail_zero_high_Z_cells` 和 `analytic_tail_cell_count`：用本推论支付的零高模尾胞。
- `paid_cell_count`：两种互斥支付方式的总数，应为 $J-1$。
- `all_cells_nonzero_height_mode_condition_paid`：旧充分条件本身是否全付；不会因新证明通过而伪改为 true。
- `all_cells_nonplanarity_alternatives_paid` 和同场 `activity_nonplanarity_certified`：完整替代结论。

它不计算 $F$、不调用 scalar oracle，仍明确零新场评价。旧 v1 consumer 和只认 b36d 的几何合并器不会自动消费 v2；如实际需要使用此增强，应在另一个明确版本中核新 source/schema 以及两类胞覆盖总数，不把旧的“高 $Z$ 见证数 $J-1$”偷换成已通过。

两平帽内部仍排除；镜像与全相位继承按 R675。新结论仍只是 marker 论证中的非平面活动片条件，不独自支付带 marker 嵌入、reach、metric 或数值 Euclidean 幅度。截至撰写没有候选已实际消费此 v2 草案。

执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
