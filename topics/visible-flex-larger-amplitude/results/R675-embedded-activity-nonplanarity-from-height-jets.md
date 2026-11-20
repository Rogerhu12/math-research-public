# R675. 同场嵌入加高度角模三 jet，支付全部活动片无平面开片

日期：2026-11-20。会话：Astra-resume-public-20261120 / fullclosed_solver。

**状态：完整条件定理与小型公开 Actions 消费者；没有执行新候选的科学计算。** 本条由已经支付的同一场全局嵌入性，直接消去旧 R661 非平面核的轴迹数值查询。对 R671 非多项式解析尾同样适用；不要求径向解析，也不把旧多项式 lift 的轴迹证书复制到新场。

本条支付的是 R661 固定帽 marker 论证所需的“活动片无平面开片”条件。实际候选须先有同一 bundle / model 的完整嵌入报告，并实际通过下述有限非零系数条件。两平帽本来允许是平面；本条不排除它们，也不单独声明 marker 构造、reach、等距或 Euclidean 幅度数值已经完成。

## 1. 对象与充分条件

在上活动片 $0<s<S$，采用原旋转 $\phi$ 正交架。$\nu_m=2m$，$m=1,\ldots,M$。完整场具有形式

$$
F(s,\phi)=q(s,\phi)+f(s)e_r(\delta(\phi))+Z(s)e_z,
\qquad Z=Hh+k,
\tag{1}
$$

$$
\delta(\phi)=\sum_{m=1}^M d_m\sin(2m\phi),
$$

$$
\begin{aligned}
q_R(s,\phi)&=R_0(s)+\sum_{m=1}^M R_m(s)\cos(2m\phi),\\
q_T(s,\phi)&=\sum_{m=1}^M T_m(s)\sin(2m\phi),\\
q_Z(s,\phi)&=Z_0(s)+\sum_{m=1}^M Z_m(s)\cos(2m\phi).
\end{aligned}\tag{2}
$$

$q_R,q_T$ 是旋转架分量，转到世界坐标还要乘 $e_R(\phi),e_T(\phi)$。新 $f,h,k$ 是径向函数，R671 的原全部角模和解析 $e_r(\delta)$ 都保留。

每个原闭胞 $[s_i,s_{i+1}]$ 中的每个 $Z_m$ 是原共享三 jet 定义的唯一五次 Hermite 多项式。原胞宽严格为正。两活动片在 core 镜像拼接，并在末圈接两平帽；原 R671 完整端口保持。参数球中，同一 $0<s<S$ 上的角 $\phi$ 与 $\phi+\pi$ 是不同点。

假设：

1. 包括镜像与两帽的**同一个准确场**已经证明是嵌入；这可以由 R670/R674 新连续首 jet 支持报告支付。
2. 对每个原胞 $i$，存在至少一个 $m\ge1$，使六个真实 Hermite 数据中至少一个严格非零：

$$
Z_m(s_i),\ Z_m'(s_i),\ Z_m''(s_i),\
Z_m(s_{i+1}),\ Z_m'(s_{i+1}),\ Z_m''(s_{i+1}).
\tag{3}
$$

**结论。** 两活动片没有落在任一仿射平面内的非空相对开片。更强地，完整闭面中任一平面开片都不能与活动片内部相交。这个结论排除从 core、原 mesh 接缝或新 cutoff 接缝“漏入”的平面开片；本来允许的平帽内部除外。

## 2. 全局嵌入已经保证两条轴迹非零

在准确的 $\phi=0,\pi/2,\pi,3\pi/2$ 上，每个 $\sin(2m\phi)$ 都为零，所以 $\delta=q_T=0$。这是准确三角恒等式，不依赖普通 libm 对 $\sin(m\pi)$ 的舍入值。

定义

$$
r_0(s)=q_R(s,0)+f(s),\qquad
r_{90}(s)=q_R(s,\pi/2)+f(s).
$$

世界坐标中的两组相反点为

$$
F(s,0)=(r_0,0,z_0),\qquad F(s,\pi)=(-r_0,0,z_0),
\tag{4}
$$

$$
F(s,\pi/2)=(0,r_{90},z_{90}),\qquad
F(s,3\pi/2)=(0,-r_{90},z_{90}).
\tag{5}
$$

其中每组的两个高度相同，来自 cosine 的半周周期和径向 $Z$。

若 $r_0(s)=0$，(4) 的两个不同参数点重合，违背嵌入性。故对每个 $0<s<S$，$r_0(s)\ne0$；同理由(5)得 $r_{90}(s)\ne0$。只需非零，不需另证明正值或一个定量下界。这里没有调用新的 $a/I$ oracle、轴迹区间或数值搜索。

## 3. 角向解析延拓把任意平面开片化为水平面

反设某个活动开片落在平面

$$n_xx+n_yy+n_zz=c,\qquad n\ne0.$$

取它在活动参数域内的一个开矩形 $I\times J$，其中 $I\subset(0,S)$ 可以缩小到一个原胞的内部。对固定 $s\in I$，式(1)作为 $\phi$ 的函数是实解析的：$q$ 是有限三角多项式，$\delta$ 亦然，$\sin\delta,\cos\delta$ 是它们的实解析复合。径向 $f,Z$ 在此只是常数。

因此平面等式若在非空角开区间 $J$ 成立，就对该 $s$ 的整圈成立。分别将(4)、(5)中的等式相减，得到

$$2n_xr_0(s)=0,\qquad2n_yr_{90}(s)=0.$$

由第2节，$n_x=n_y=0$，从而 $n_z\ne0$；这个平面只能是水平面。注意这里没有要求 $s\mapsto F$ 解析，完全不用跨 FullHold 或 $\eta$ 分段做径向解析延拓。

## 4. 一个准确非零高度角模即排除水平面

若 $F_z(s,\phi)$ 在 $I\times\mathbb S^1$ 为常数，则由 cosine 模的线性独立性，对每个 $m\ge1$ 都有

$$Z_m(s)=0\qquad(s\in I).$$

新 $Hh+k$ 以及旧 $Z_0(s)$ 都不依赖角，不能抵消任何 $m\ge1$ 项。

设 $I$ 所在原胞为 $i$。由(3)选择一个非零 Hermite 数据对应的 $Z_m$。严格正的胞宽保证给定六个数据的五次 Hermite 多项式唯一；若多项式恒为零，六个数据必全零。因此该 $Z_m$ 不是零多项式。非零实多项式不可能在任何非空开区间上恒为零，与前式矛盾。

数据是保存的有限 binary 自由参数，被解释为准确实数；“非零”使用准确的等于零判断，不引入浮点阈值。极小但非零的值足够支付这里的定性条件，却不自动给定量 Euclidean 距离下界。

## 5. core、接缝、镜像和帽的范围

core 曲线、原 mesh 接缝、$\eta/\chi$ 接缝以及帽边圈在参数球中都是一维集合，没有二维内部。任何与活动内部相交的曲面开片，其参数原像都含有一个第3节所用的开矩形，并可进一步避开有限原节点。故不能用恰处于这些接缝来逃避证明。

下活动片是上活动片的固定 $z$ 镜像。镜像保持嵌入与平面性质，将非零 $Z_m$ 数据变号而不变为零；同一结论适用。原材料相位换元和水平刚体旋转也保持“存在平面开片”与否，因此相位族继承同一个定性结论。

两帽内部当然可以是平面开片，本条明确排除它们。若一个平面开片包含帽边圈的相对邻域并进入活动片，则它会包含活动开矩形，已被排除。因此 R661 需要识别的平面部件没有活动片中另外长出的平面开片。

这只支付 R661 marker 论证的一个条件。四个固定 marker 的具体构造、参数、支持预算和其它身份条件仍须按 R661/R663 在同一场上应用；本条本身不输出“marker 已构造”或正 Euclidean 幅度的数值。

## 6. 小型同场消费者

完整源为 `scripts/resume_20261120/exact_reference_tail_nonplanarity.py`：

- 9392 bytes。
- SHA256：`b36d387fed072235e1aec8e77da130c9c9be095aed64be46485fc0890b21c09d`。
- 当前仅经 AST 语法核对；未导入或执行科学代码。

它要求实际新首几何报告的 schema 为 `R671-reference-tail-continuous-interval-v1`、`mode=first`、完整原胞覆盖，并核对实际 bundle SHA、node report SHA 与 canonical `model_identity_sha256/model_definition`。消费者绑定的完整新首几何源 SHA 为

`f1220a2e83578bb186ec1043c5dc5fd70dd988f1a108897537117344590de225`。

嵌入报告来自这个源的实际输出；没有从候选的旧标签猜测嵌入。原节点宽度再以 Fraction 和同一个准确 $S$ 盒验证为正，这是 Hermite 唯一性的有限代数条件，不是重做几何证书。

消费者对每个胞只检查两个端点、三个径向 jet 的所有 $Z_{m\ge1}$ 槽，选择一个准确非零见证。raw 记录以紧凑列表保存 `[cell,node,derivative_order,mode,binary_hex]`，不保存逐点诊断表。它不计算 $F$、曲率、Gram、角变换、scalar 或 embedding。

若完整嵌入尚未付，或某胞六个端点 jet 的全部非零高度角模都为零，输出 `unpaid_hypothesis`。后者只说明本充分条件未付，不说明存在平面开片；例如真正的弯曲轴对称片可以没有任何非零高度角模。本程序不把这种情形误报为几何失败。

两个条件都满足时，输出 `activity_nonplanarity_certified=true`，并明确 `known_flat_cap_interiors_excluded=true`、`scalar_oracle_calls=0`、`field_evaluations=0`。源码还保持 marker 构造、reach 与 metric 标签为 false；这里只交付 R661 所需的条件。

## 7. 公开 Actions 命令与科学状态

```bash
python "$REPO/topics/visible-flex-larger-amplitude/scripts/resume_20261120/exact_reference_tail_nonplanarity.py" \
  --repo "$REPO" \
  --bundle "$NEW_R671_BUNDLE" \
  --embedding-report "$SAME_FIELD_FIRST_GEOMETRY_REPORT" \
  --node-report "$WORK/fullclosed_solver/data/fullclosed-hold-warm.json" \
  --out "$WORK/reference-tail-activity-nonplanarity.json"
```

实际科学消费只允许在 `Rogerhu12/math-research-public` 的公开 GitHub Actions。完整 raw 报告留在该 job 的 work，公开结论引用其实际 run、候选/model/source SHA 和返回状态即可。无需另加轴迹 oracle、独立 fixture 或重复嵌入计算。

截至本条撰写，本文和源码只支付定理与实现；任何具体新候选是否满足假设，仍须登记其公开 Actions 的真实结果。

执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
