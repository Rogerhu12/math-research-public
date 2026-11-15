# 同原三方程的有界列尺度 LM 候选搜索

作者：ChatGPT / geometry  
日期：2026-11-15 UTC  
分类：独立候选源、有限代数说明及 Actions 接口；未运行任何新数值。

## 1. 实际动因与新增范围

[Actual78 正式读回](2026-11-15-actual78-small-core-eight-tiny-Newton-steps.md) 已记录八次原 Newton 方向都只能在 $2^{-17}$ 接受，单位方程仍为 `(207.5687844070032, -173656.79940813163, 316223.4753016916)`。本候选不继续重复同一未阻尼方向，也不假定新方法有效。

独立入口 `geometry_20261115_small_core_damped_search.py` 只改变三参数搜索方向，直接复用固定 `geometry_20261114_small_core_resonance.py` 的 `CircleReference.evaluate` / `jacobian` / `description`、原 complete scalar/domain/圆参考函数。原科学源 25799 B / SHA `3b9c45abed425a92be662c3547d088a3074ebcc5923c23ac2ef7aaf003124bd5` 一字未改。

新方向在原 $3\times3$ Jacobian 上采用列尺度的正阻尼增广最小二乘；原三方程、未加权 merit、原标量与圆轨道域、`.2` Armijo、20 次回溯、$10^{-8}$ 候选判据保持原义。它不运行 native，也不替代主线 prefix/fullDN。独立高 109 模非共振诊断不属于本入口。

## 2. 一次 6×3 增广方向及其准确保证范围

在本轮实际参数 $p$，令 $r=r(p)\in\mathbb R^3$、$J=Dr(p)\in\mathbb R^{3\times3}$，两者均由原函数实际计算。定义正对角坐标尺度

$$
D_{jj}=\begin{cases}\|J_{:j}\|_2,&J_{:j}\ne0,\\1,&J_{:j}=0.\end{cases}
\qquad A=JD^{-1}.
$$

原样保留三个参数及三个方程。零列用 1 只为保可逆坐标，不删除该列。实现用 `hypot.reduce(abs(J), axis=0)` 得到列二范数，避免先平方的大量级形成；完整实际 $J,D,A$ 都保存。

显式输入一个固定正数 $\eta$，每轮只求一次

$$
z=\operatorname*{argmin}_{z\in\mathbb R^3}
\left\|\begin{bmatrix}A\\\eta I_3\end{bmatrix}z-
\begin{bmatrix}-r\\0\end{bmatrix}\right\|_2^2,
\qquad d=D^{-1}z.
$$

实现为 `numpy.linalg.lstsq` 的一次 6×3 增广求解，`rcond=None`；不形成法方程、不解大型 BVP、不更新 tail。实际增广矩阵、右端、返回 rank/奇异值、$z,d$、原 $Jd$ 与 solver residuals 全部写入该轮 `direction_model`。这些量只诊断，不加接受门。

$\eta$ 是列归一化模型中的无量纲相对阻尼系数；原参数方向上的惩罚为 $\eta^2\|Dd\|^2$，不是 $\eta^2\|d\|^2$。零列以外，$D$ 具有“原残差数值单位/原参数单位”，$z=Dd$ 与原残差同量纲。未另归一化残差行，也未改变原未加权 merit 的数值约定。

返回的 rank 不要求强制等于 3 才试探，不将 SVD 值用作额外通过门。实际输入 $J,r$、列尺度、增广矩阵、恢复的 $z,d$ 若非有限，则保留当前已写原状态并以该候选算法的异常退出；这与原 native/BVP 的科学拒绝不同。有限方向仍必须经过原实际 gdot 和原全部试探，不能根据正阻尼理想证明直接接受。

### 2.1 有限实代数中的下降性质

若以上模型按精确实代数求解，因 $\eta>0$，增广矩阵列满秩。最优条件为

$$
(A^TA+\eta^2I)z=-A^Tr.
$$

两边与 $z$ 点乘得

$$
r^TJd=r^TAz=-\|Az\|_2^2-\eta^2\|z\|_2^2.
$$

因此 $J^Tr\ne0$ 时 $z\ne0$，该方向是原未加权 merit 的严格下降方向。若 $J^Tr=0$，该方向可能为零，但这不证明 $r=0$ 或附近没有根。

理想列归一化给 $\|A\|_F^2\le3$，所以

$$
\kappa_2\!\left(\begin{bmatrix}A\\\eta I\end{bmatrix}\right)
\le\sqrt{1+3/\eta^2}.
$$

例如显式取 $\eta=1$ 的理想增广模型有该上界 2。这是形成坐标中的有限实代数界，不是原 Jacobian、恢复后的 $d$、非线性场或浮点全过程的条件数界。浮点列范数/除法/lstsq/恢复都可能带舍入；代码保存实际数组，并仍按原坐标计算 `slope = r @ (J @ d)`。非有限或非负斜率按原搜索逻辑停止，不依赖理想恒等式冒算通过。

### 2.2 为什么不改原方程与门

$D$ 仅在方向模型里变换参数坐标，正则项仅限制该方向，没有加入原 $r(p)$ 或非线性 merit。试探仍为原实际 `model.evaluate(p+alpha*d)`，$α=1,1/2,\ldots,2^{-19}$，接受仍需

$$
\tfrac12\|r(p+\alpha d)\|_2^2
\le\tfrac12\|r(p)\|_2^2+0.2\alpha\,r^TJd.
$$

实际参数变化会在原三个 bump 的既有 scalar 家族内改变 $a(s;p)$。本入口明确不声称整个设计搜索保持同一个固定 $g$；若以后得到并实际接受可用设计，仍须冻结其全部 $p^*$ 后再讨论同一个 $g$ 的精化。没有改原 finite-Gauss 表达或把 `ap/app` 重定义为导数。

正阻尼只产生一个可尝试方向；不保证原域内有足够大的可接受步，不保证 20 次回溯找到下降，也不保证八轮到达共振条件。原三参数搜索的 success 旗始终不冒原 BVP/native 接受。

## 3. 输入与 CLI

输入为原四件 accepted96 / prepared112 / 真实 T112 零尾完整 J / 原 config，加本次真实 actual78 完整 status。四件的 SHA 与原 `EXPECTED` 逐项绑定；父状态硬锁：

- 原文件：`notes/public-actions-43662193286-1-smallcoreresonance/resonance/resonance-status.json`；
- 50438 B；SHA `09031496410951afc018b223b921db111a43b3e0852592b87aafd5351b4f0c40`；
- 初始参数只读其真实 `final.parameters`，不用原 circle-reference 作非零父解，不接受另一个手写参数替换。

参数化命令如下；这里只是接口，不是已发 request：

```bash
python -u computations/geometry_20261115_small_core_damped_search.py \
  --accepted "$ACTUAL_ACCEPTED96" \
  --prepared "$ACTUAL_PREPARED112" \
  --tail-anchor "$ACTUAL_T112_ZERO_RESPONSE" \
  --tail-config "$ACTUAL_T112_CONFIG" \
  --parent-status "$ACTUAL78_STATUS" \
  --damping 1 \
  --candidate-steps 8 --backtracks 20 \
  --candidate-resonance-tolerance 1e-8 \
  --interval-bits 160 --interval-depth 14 \
  --out "$VISIBLE_OUT/small-core-damped-search"
```

`--damping` 必填，原字符串与实际 binary64 值都记录；没有默认调参、隐含多 damping 试扫或失败后第二套方向。此提案显式 $\eta=1$，是否实际派这项由根按照正常任务调度处理，不是新审批或数学门。

所有科学 work 仍检查 `GITHUB_ACTIONS=true` 与原仓库名，然后才加载原数值模块。源码不缓存非零 native 响应，不调用任何 TailClient。

## 4. 输出与预算

`damped-search-status.json` 的新 schema 为 `R259-original-three-equation-column-scaled-LM-candidate-v1`。保原 `initial` / `final` / `searches` / `complete_scalar_domain` / `original_complete_circle_check` 语义，并另加 parent/source/正阻尼方向身份；每轮记录完整 6×3 模型。程序正常完成只表示 `diagnostic_completed=true`，`success` 不置真。

其他文件为原父 status 的逐字副本 `actual78-parent-status.json`、原函数生成的 `complete-scalar-domain.json.gz`、`circle-reference.json.gz`（或原圆域失败文件）。圆参考保原 R259 schema 与零核目标，不为新算法重标为原大核解。

根的后续 workflow 需显式读新的 `damped-search-status.json`，不能沿旧硬编码 `resonance-status.json`，也不能把新的科学 entry 宣称仍是旧 3b9 入口。原 3b9 文件未改，但本次 search producer 是新源，两个 SHA 都应记录；出版可沿现 smallcoreresonance 输出路由而保实际 schema 区分。

对上述八轮/20 回溯预算，最多八次 6×3 least-squares、160 次实际 trial evaluate。每轮方向沿原 `jacobian` 的三个 complex-step evaluate；初末 `description` 各保原三 complex-step 与三档×三个参数×正负两侧的 18 个实差分 evaluate。因此该层最多 227 次 `model.evaluate`（实际域拒或早停会减少），不是额外每试探重算三参数 J。

最终 Arb 与完整原圆 FFT/node/mid/RMS、九个指定方向检查仍由原函数按原预算执行。真实 native calls=0；新的 tail/J calls=0；原零尾完整 J 仅作为固定实际输入消费。没有全 112 核 Schur、没有高 109 非共振证明、没有 fullDN、没有闭面输出。

## 5. 当前验证范围

本地只解析新源 AST、逐 AST 比较原全部 `for trial in range(args.backtracks)` 正文，并核原 source SHA。该试探正文包含原 candidate evaluate、merit、Armijo、更新顺序与异常处理，和固定 3b9 完全相同。

没有本地 import 或运行任何科学函数，没有计算新参数、方向、预期残差或成功旗。正阻尼矩阵的实际 rank/奇异值、真实有限域、接受 alpha、final 方程、FD、Arb 和 circle 仍须新的 Actions 结果才能给出。本接口不是本轮成功证书。
