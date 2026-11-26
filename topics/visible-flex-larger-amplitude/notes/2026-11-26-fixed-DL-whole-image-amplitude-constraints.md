# 新均值设计的固定 D/L 幅度保护：完整导数与同场范围

2026-11-26，Astra-larger-e4e2a2bf-20261126 / geometry（AI 辅助）。

**状态：以下预算蕴含和全自由导数为解析推导；实际e3d69d2e新均值场的完整first已返回，选择Dmarked=4.2、L=.9、Hmin=1.01预算，尚未执行新增幅度保护方向。** 实现由独立的完整原自由量 cotangent helper 与求解 driver 接线完成。本文不把旧 `7fd` 等场的约 `.228` 握持比继承给新场，不在有限点筛选后宣称已经支付连续幅度。

新角均值目标释放了原固定径向/角向均值条件，故不能只追逐其 relative residual：增大 H 或某些方向的长度，可能使相对残差变小而让真实直径增长。下列保护固定的是一组完整几何证书预算，不能随 trial 的自身尺寸重新归一化并放松。

本条复用 [R658](../results/R658-complete-body-diameter-and-fixed-grip.md)、[R659](../results/R659-complete-image-held-amplitude-for-the-same-closed-candidate.md) 的完整像/直径策略及 [R661](../results/R661-complete-nonplanar-activity-and-four-fixed-markers.md) 标记。新增内容是它们对当前 canonical R671 全自由变量的显式约束、core 见证点的额外链式法则与 solver/连续证书的范围区分；没有重新认领旧数值结论。

## 1. 固定预算的含义

统一使用下列记号，避免把 body 与 marked 直径混在同一个变量里：

$$
h=1/1000,\qquad
\overline D=\text{带四个固定标记的完整闭面直径预算},
$$

$$
\overline B=\overline D-2h>0,\qquad
\overline L\ge\overline D/5>0.
\tag{1}
$$

$\overline L$ 是本文选择的**完整像见证距离**预算。它不是某个已假定的实际 Hausdorff 幅度，更不是核心点位移的大小。两预算在一个设计/固定目标精化分支内是明确常数；所有导数中 $\dot{\overline B}=\dot{\overline L}=0$。

对未标记活动部分及两平帽，要求完整连续范围满足

$$
|X|\le\overline B/2,\qquad
|X-\sigma p|\ge\overline L\quad(\sigma=\pm1).
\tag{2}
$$

再要求

$$
H-h\ge\overline L,\qquad \overline D\le9/2,
\qquad H>1,\quad R>9/20.
\tag{3}
$$

这里 R 是**原固定 FullHold 的准确终端半径**，不是新增求解变量。S、lift 宽度、$\lambda$ 和 $\eta$ 的物理端点同样按当前分支固定；H、全部内部共享三 jet 和全部非固定 core 系数保持自由。

(2) 第一项给未标记完整直径 $D_0\le\overline B$。事实上当前未标记闭模型关于中心反演对称：水平半转改变 world x/y 符号，镜像半面改变 z 符号，故每个 X 的 −X 也在完整像内，从而 $D_0=2\sup|X|$。这个等式不适用于已加四个不对称标记的像；标记后只用已证明的安全界

$$D_{\rm marked}\le D_0+2h\le\overline D.$$

R659 的见证 p 属于相位 $\pi/2$ 的活动像。标记不改变活动部分；新帽点的竖直距离至少 H−h。因此 (2)–(3) 给

$$
\delta_{\rm hold}\ge
\operatorname{dist}(p,S_0^{\rm marked})
\ge\overline L\ge\overline D/5
\ge D_{\rm marked}/5.
\tag{4}
$$

半径 $9/20$ 的固定握持区包含未被小图修改的外圆，故其直径至少 $9/10$；由 $\overline D\le9/2$，

$$\operatorname{diam}F_0(H_{\rm grip})\ge9/10
\ge\overline D/5\ge D_{\rm marked}/5.$$

这只支付幅度与握持比例的蕴含。全域嵌入、reach、非平面/非全等以及固定目标等距仍分别需要自己的实际证据。

**必要性的精确边界。** 在选定常数及 (2) 的这套全域证书中，每个有限点的对应不等式都是必要条件。因此违反一个点就足以否定当前候选满足这套固定预算。但这不是所有可能构造达到 README 握持幅度的全局必要条件：另一见证点、另一个相位或另一个完整像论证仍可能成功。尤其见证 p 的距离小，不等价于实际完整 Hausdorff 幅度必小。

## 2. 见证点会随全部自由 core 改变

原准确 core 接口给

$$
r_0=1+\sum_{j=1}^{M}c_j,\qquad
F_0(0,0)=(r_0,0,0),\qquad
p=(0,r_0,0)\in S_{\pi/2}.
\tag{5}
$$

这里和式包含**全部 M 个 core 系数**。前 K=3 个固定项的方向为零，但其后所有自由项都进入方向

$$\dot r_0=\sum_{j=K+1}^{M}\dot c_j,
\qquad\dot p=(0,\dot r_0,0).\tag{6}$$

不能只用低模、只对固定前三项求导，也不能沿用上一父的 p。每个真正的 nonlinear trial 都必须用自己的实际 core 重算 (5)。这既是距离值的要求，也是完整 Jacobian/transpose 的要求。

在 canonical R671 模型，core 处的 $\chi$、$\eta$ 与解析尾不改变原接口；故 (5) 与 $\lambda=1$ 的新尾相容。它来自准确相位像的一个点，不依赖把某个材料标签固定成同一个物理角。

## 3. 旋转架与 quarter 对称

现有 `point_adapter.fields_at` 返回的是旋转 $\phi$ 正交架中的六 jet。world p 在该架的分量为

$$
u_\phi=(\sin\phi,\cos\phi,0),\qquad
p_{\rm rot}(\phi)=r_0u_\phi.
\tag{7}
$$

所以在原 point pullback 接口中必须使用

$$w_\sigma=X_{\rm rot}-\sigma r_0u_\phi.$$

把 world 向量 $(0,r_0,0)$ 直接从旋转架 X 中相减，会产生错误的函数和错误梯度。本文的 $u_\phi$ 按当前观察地址的物理角固定；求导时只改变场系数，不改变这个地址。准确连续证书另行覆盖所有物理角，因此没有将有限地址移动误作全材料覆盖。

完整 R671 对称类中，x 反射固定 p，y 反射交换 p 与 −p，水平半转也交换二者，z 镜像固定 p。故 quarter 中对**两个符号分别检查**，正好覆盖完整角轨道与镜像半面。单独一个符号的 quarter 最小值不覆盖整圆；正的 orbit multiplicity 是积分权，不能替代这里的两个不等式。

扫描时可以使用等价式

$$
\min_{\sigma=\pm1}|w_\sigma|^2
=|X|^2+r_0^2-2|r_0(X\cdot u_\phi)|
$$

快速定位最坏点，但导数与永久约束记录应保留实际 $\sigma$ 分支。两分支相等时，不能凭 `abs` 的任意单个导数删掉其中一条。

## 4. 完整原自由量梯度

采用无量纲 $g\le0$ 约束

$$
g_D=4|X|^2/\overline B^2-1,
\qquad
g_{L,\sigma}=1-|w_\sigma|^2/\overline L^2.
\tag{8}
$$

其准确方向导数为

$$
\dot g_D=\frac{8X\cdot\dot X}{\overline B^2},
$$

$$
\dot g_{L,\sigma}
=-\frac{2w_\sigma\cdot\dot X}{\overline L^2}
 +\frac{2\sigma(w_\sigma\cdot u_\phi)}{\overline L^2}\,\dot r_0.
\tag{9}
$$

因此原完整六 jet cotangent 中只需要非零位置槽：

$$
\xi_D=8X/\overline B^2,\qquad
\xi_{L,\sigma}=-2w_\sigma/\overline L^2.
$$

将这些位置 cotangent 交给 canonical R671 的实际 `point_adapter.pullback_at`。它已经包含：两个原胞端点全部自由共享三 jet、core 受限端口的导数、全部自由 core 对 $\Theta/\rho$ 与解析 lift 的支路，以及真实 H 高度支路。R671 的固定 k 偏置影响当前实际 X，但对自由变量没有额外导数；不得忘记它来求值一个旧场。

然后，**只对距离约束**，在完整原 packed gradient 的全部自由 core 槽各加

$$a_\sigma=\frac{2\sigma(w_\sigma\cdot u_\phi)}{\overline L^2}.$$

已有 `fullclosed_point_cotangent_observed.pullback` 的 packing 明确为

```python
gradient[:problem.M-problem.K] += a_sigma
```

这个前缀是原自由 core 块，不是末尾块，也不是某个 coarse 子空间。它只支付新见证 p 的变化；原 pullback 中的场/角 lift core 支路不能因此删除，也不能再重复添加。

全部原梯度形成之后，若当前求解坐标为 $\dot x=Tz$，再计算 $T^*\nabla g$；不能先在删减 coarse 变量上构造一个不完整的 p 梯度。对应 QP 行为

$$ (T^*\nabla g)^Tz\le -g(x).$$

同一次 QP 的 T、预算和父场固定；最后的 nonlinear line search 仍在真实新场上重算约束，而非把线性模型值当成接受条件。

## 5. 帽与高度的标量行

R 固定，H 自由。平帽的最大原点半径平方为 $R^2+H^2$，故显式帽行可取

$$
g_{\rm cap}=4(R^2+H^2)/\overline B^2-1,\qquad
\dot g_{\rm cap}=8H\dot H/\overline B^2.
\tag{10}
$$

见证到标记帽的竖直保护为

$$g_H=\overline L+h-H\le0,\qquad\dot g_H=-\dot H.$$

H 的原 packed 梯度可以通过

```python
problem._free_adjoint(np.zeros((problem.J, 3, problem.n)), height_cotangent)
```

取得，不猜测其打包位置。以上算式中的 R 在数值 solver 中使用其原 carrier；严格完整 first 最终使用同一个准确 FullHold R 盒，数值行不被冒称为 outward 证书。

单独 $H\ge\overline L+h$ 未必保证 $H>1$。若沿用现行 R661 的统一支持下界 $64/267$ 与新合并器，则必须保留已有严格 H>1 条件，或明确固定一个 $H_{\min}>1$ 的保护；可以将下限取为 $\max(H_{\min},\overline L+h)$。不要把 H=1 的非严格数值行当作已满足 R661 的严格输入。R>9/20 则来自固定准确 R 的已证下端，不作为自由变量的伪梯度。

## 6. 由实际 first 选预算，不转移旧比值

首次新均值场之后的 f122 完整 first 是一次新的必要几何观察，目标是防止新目标通过长度增长退化；并非为重复旧百分之一 metric 失败而重跑昂贵完整 K。它读**该实际新 bundle**及其 node/profile，返回

$$D_+={\tt continuous\_diameter\_upper},\qquad
L_-={\tt continuous\_fixed\_witness\_distance\_lower},$$

以及 `exact_height`、`witness_radius_exact`、准确 R/S、完整域和源/输入身份。浮点端点按其准确 binary Fraction 值消费。由同场结果构成

$$D_{m,+}=D_++2h,\qquad L_{m,-}=\min(L_-,H-h).$$

若要让当前父已被严格证明处在预算内，需实际核

$$
D_{m,+}\le\overline D\le9/2,\qquad
\overline D/5\le\overline L\le L_{m,-},
\qquad H>1,
$$

并完成 first 的完整闭面/正支持等原 scope 检查。只有这些真实同场条件支付后，才可把它作为已认证的可行起点。

若返回的 $L_{m,-}/D_{m,+}$ 小于 1/5 或 D 上界过大，这本身**不证明真实场失败**：上/下界可能太松。先检查实际有限必要点是否已违反预算，或在有必要时细化同场 first。若真实点已违反则不能称原点可行，需要明确的可行性恢复或换用一个实际重新核验的父；不得借用另一 bundle 的 `.228`，也不能把 QP 的零步默认视作可行。

预算一旦确定，记录其准确有理值、来源 first/bundle/node/profile SHA、使用的 R661 标记参数和当前固定模型身份。此后每个 trial 的 X、H、全部 core 和 $p(c)$ 重新计算，但预算本身固定。任何更改预算都需要明确说明它与真实20%目标的关系，不以新场自己增长后的尺寸再定义更宽阈值。

实际预算来源为[最新同场完整first](2026-11-26-actual-first-mean-face-PCG-and-amplitude.md)：bundle `e3d69d2e383a8d57876a3427b635f9528e2f0b145a7594e41913c89222c2dd60`，Dbody上界4.118090829150488、witness下界.9387771461187304、H准确4229322458036129/2251799813685248；node/profile/first完整SHA见该记录。CLI三预算按传入binary64的准确dyadic值解释，B取Dmarked−2/1000的向下浮点界，高度费用向上；5L≥Dmarked用准确Fraction检查。完整解析导数helper额外验证原free layout及prepared.height==x[-1]后才使用H末槽，等同原free_adjoint，并非无根据猜槽。

## 7. 有限求解筛与最终全域证书

QP 可选取最坏或近活跃的若干 D/L 行构造方向，但每个实际接受 trial 的非线性必要筛应覆盖：原完整正权径向观察集与原完整 quarter 角轨道、两个距离符号、caps/H 标量行，以及全部永久记忆的原/新 off-grid 地址。不能只检查选入当前 QP 的行。新坏地址必须按原物理位置记住，真正网格精化时按已有迁移规则保留。

该有限筛只检验选定完整条件的必要输入。候选变化后，即便全部点通过，也仍必须由新的同场 f122 完整 first 对全部径向/角闭盒、镜像与两帽支付 D/L；R686/实际消费者另外支付 K/reach；R689 及固定目标求解精化另外支付等距。这里没有通过数值筛省掉 README 的全域责任。

可按实际需要在公开 Actions 中运行新的 dp 支路独立方向诊断；它是可选的实现诊断，不增加求解的必过门槛，不阻断真实新父继续求解，也不替代以上解析导数证明。若运行，方向须包含自由 core，complex trial 的 p 也按全部 trial core 重算，平方范数使用双线性 $\sum_iw_i^2$ 的解析延拓，而非共轭 `vdot`。否则一个冻结 p 的错误参考会错误地赞同同样遗漏 dp 的实现。诊断可分别记录两个距离符号、半径与 H/cap 行的实际返回；本文没有提前填写这些数值。
