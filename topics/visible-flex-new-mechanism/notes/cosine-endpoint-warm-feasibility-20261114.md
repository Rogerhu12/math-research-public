# 端点准确消元后的暖启动与全角可行性修复

日期：2026-11-14。本记录交付一个**新的几何设计运行器**，不是已冻结点的固定度量精化，也没有报告本地研究求解成功。新脚本 `../scripts/space_star_cosine_endpoint_feasible.py` 独立导入既有准确消元定义，不修改已经发布的 `space_star_cosine_endpoint_design.py`。

## 1. 实际失败所揭示的问题

公开 Actions `43598398961` 的输出在 `actions-43598398961-1-cosine_endpoints/`。主设计 JSON 和独立 32768 格验证均已实际读取。

| 量 | 实际结果 |
| --- | --- |
| SLSQP | 10 次迭代、46 次目标评价，`Positive directional derivative for linesearch` |
| 选中自由系数 | 回到纯 \(H_1=0.15\)、\(H_4=H_5=H_6=0\) 的原初值 |
| 6144 点的最小 \(J\) | −198.20425502437084 |
| 6144 点的最大 \(|q_\ell|\) | 9960.212751218542 |
| 6144 点的最大中心主曲率 \(\lambda_0\) | 10944.110614354473 |
| 尖点、谷点的准确 \(q_\ell\) 分子 | 均严格为零 |
| 独立连续验证 | 6074 格没有正 \(J\) 证书；全宽浸入未通过 |

这说明两个端点的准确消元确实生效，但没有控制中间角度。把原来的巨大违反点直接交给带自由 epigraph 的 SLSQP，没有形成可用核心。该点不进入真实单射验证，也不原样重跑。

## 2. 暖输入的身份和投影

新的默认运行使用更早的实际自由六模点：

`actions-43597247312-1-cosine_core/cosine-core-a65-b12-h15.json`。

从该报告的**准确冻结物理身份**读取系数，而不是从终端小数复制后假称同一参数。运行器检查报告自身的物理身份 hash，并要求相同的 \(a,b,w\)、余弦高度类型及模数。

只保留实际 \(H_1,H_4,H_5,H_6\) 作为自由变量的暖值。\(H_2,H_3\) 由先前定义的准确有理线性映射重新计算：

\[
 \sum_{j=1}^6 \sigma^j j^2(U_\sigma+9j^2R_\sigma)H_j=0,
 \qquad \sigma=\pm1.
\]

这是明确改变了物理曲线的**新设计投影**。旧点的曲率、\(J\)、高度或排除结论都不转移到投影后的点。报告保存源文件 SHA256、原准确身份、保留和重算的谐波、offset 处理前后的自由系数、任何盒约束截断量。

自由 offset 默认重新把投影后的取样高度范围居中；它仍是后续求解的自由变量。`--offset-policy source` 可保留源 offset，`--fixed-offset` 可明确固定。以上选择都进入实际模型身份和运行定义。

六模时未知数仍为四个自由高度加 offset，共五个可行性变量。派生 \(H_2,H_3\) 的物理界保持此前明确扩大的 \(\pm0.5\)，不会因为只给自由变量设置 bounds 而漏掉这两项。

## 3. 固定曲率预算的第一阶段

第一阶段先固定一个正目标 \(K\)。全宽唯一非零主曲率满足

\[
 \max_{|s|\le w}|\lambda(s,\phi)|
 =\frac{\lambda_0(\phi)}{1-w|q_\ell(\phi)|},
 \qquad \lambda_0=\kappa+\tau^2/\kappa.
\]

因此在 \(\kappa>0\) 时，一个不需要先除以可能为负的 \(J\) 的充分设计条件是

\[
 \boxed{\lambda_0/K+w|q_\ell|\le1.}
 \tag{1}
\]

(1) 若成立就同时给 \(J\ge\lambda_0/K>0\) 和全宽曲率上界 \(K\)。它准确等价于固定 \(K\) 时的 \(KJ-\lambda_0\ge0\)，这里的实质变化是**移去初始阶段的自由 epigraph、按物理尺度归一化，并先解可行性**，不是声称改写一个等价不等式本身会消除非凸性。

默认 `--target-curvature planned` 取

\[
 K\le\frac1{0.03D_{\rm budget}},
\]

其中 \(D_{\rm budget}\) 是同一公开平面支持见证及 padding 所允许的完整直径预算。计算使用区间下端，再向下取一个 binary64 数；这是保守设计值。也可显式传入一个正数作为新的设计目标，运行器不会暗中扫多个 \(K\)。保守目标下求解失败不是一般不存在证明。

其他约束同时保留：

\[
 J\ge J_{\min},\quad \kappa\ge\kappa_{\min},\quad
 |z|+\text{角插值余项}\le H_{\rm budget},
\]

以及全部物理高度系数界与准确尖点转向界。连续 all-support 门另见现有推导；本设计器并没有把仅有尖点条件当作所有支持方向均通过。

所有约束按各自尺度无量纲化：曲率预算除以 \(K\)，\(J\) 使用单位尺度，\(\kappa\) 除以其正下限，高度除以高度预算，系数及尖点分别除以各自上界。对无量纲违反量 \(x\) 采用

\[
 h_\mu(x)=\frac{x+\sqrt{x^2+\mu^2}}2,\qquad
 h_\mu'(x)=\frac12\left(1+\frac{x}{\sqrt{x^2+\mu^2}}\right).
\]

在 \(x<0\) 时实现改用数学相同的稳定式

\[
 h_\mu(x)=\frac{\mu^2}{2(\sqrt{x^2+\mu^2}-x)}
\]

避免相减消去。默认 \(\mu=10^{-6}\)。外层正部近似光滑；原始 \(|q_\ell|\)、高度余项的绝对值仍采用既有分段解析 Jacobian，不把它们说成处处光滑。

`scipy.optimize.least_squares(method='trf')` 在明确自由参数盒内最小化上述残差。每个完整角向块与少数系数/尖点约束块具有可比较的总体权重。**选点不按 RMS 判断可行**：所有评价中保存最大无量纲违反最小的点，并逐块记录最大违反。这个阶段的优化器终止成功不等于约束通过。

## 4. 第二阶段和固定参数输出

只有已见最优点的最大无量纲违反不超过 `--epigraph-start-max-violation`（默认 \(10^{-4}\)）时，才启动第二阶段 SLSQP。否则保留明确失败的最优诊断点并跳过 epigraph，避免再次从坏浸入初值做同类优化。

第二阶段使用同一无量纲约束，目标为 \(T/K\)，并限制 \(0<T\le K\)。选点规则是：采样可行点优先，再取更小 epigraph；如果没有采样可行点，则取最大无量纲违反最小的点。全过程只运行一个指定暖源、一个指定 \(K\)、一个 case。

选中的实际 binary64 自由系数转成 `Fraction.from_float`，然后通过**定义模型用的同一准确有理消元映射**产生完整六模高度。offset 同样准确冻结。完整物理身份仍为现有独立 `space_star_cosine_verify.py` 可消费的 schema。

最终还保存 6144 点的冻结参数审计、准确端点零分子检查、尖谷独立公式审计及浮点线性映射与准确冻结映射的差。连续验证、全宽嵌入、完整面 reach 与课题完成标志都保持为假。真实验证仍要另跑固定参数的独立 32768 格程序。

首评价、每十评价、或距上次保存至少六十秒时原子保存 best checkpoint。两个阶段及各块违反都有记录；不会因为第二阶段未开始而丢失第一阶段的实际结果。

## 5. 已执行的合成开发检查

文件 `cosine-endpoint-feasibility-check-20261114.json` 只使用人工 \(a=0.07,b=0.005\) 的六模小输入，不读取真实暖源进行本地几何求解。

| 检查 | 自由 offset | 固定 offset |
| --- | --- | --- |
| 第一阶段残差方向 Jacobian 相对误差 | \(5.47\times10^{-9}\) 以下 | \(7.54\times10^{-9}\) 以下 |
| 第二阶段归一约束方向 Jacobian 相对误差 | \(4.68\times10^{-8}\) 以下 | \(6.50\times10^{-8}\) 以下 |
| 固定 \(K\) 预算等价式差 | \(1.78\times10^{-15}\) 以下 | \(1.78\times10^{-15}\) 以下 |
| 暖输入自由系数准确保持 | 通过 | 通过 |
| 不同宽度的暖身份拒绝 | 通过 | 通过 |

另外检查了 \(x\in\{-10^4,-1,0,1,10^4\}\) 的稳定正部及导数范围。总体 `passed: true`，`research_geometry_evaluated: false`，`optimization_performed: false`。这里没有把 Jacobian 检查当作真实几何可行性。

独立只读复核：`repo_sources` 已逐块核对 \(5N+2m+2\) 个约束的 scales/weights 与原始排列相符、固定 \(K\) 预算等价、解析链式 cap 列和第一阶段删列、最大无量纲违反选点及第二阶段启动门；并核对暖身份绑定、\(H_2,H_3\) 重算、offset/截断记录和不继承旧证书的语义。没有运行研究计算。若未来源自由系数是任意非 binary64 有理数，转成 float 是新设计初值的明确舍入，不是源点的准确延续。

## 6. 单 lane 的公开 Actions 命令

```bash
OPENBLAS_NUM_THREADS=1 python topics/visible-flex-new-mechanism/scripts/space_star_cosine_endpoint_feasible.py \
  --check-only --out "$RUN_DIR/cosine-endpoint-feasibility-check.json"

OPENBLAS_NUM_THREADS=1 python topics/visible-flex-new-mechanism/scripts/space_star_cosine_endpoint_feasible.py \
  --a .65 --b .12 --height-modes 6 --half-width .02 \
  --warm-input topics/visible-flex-new-mechanism/notes/actions-43597247312-1-cosine_core/cosine-core-a65-b12-h15.json \
  --offset-policy auto --target-curvature planned \
  --angles 768 --dense-angles 6144 --j-floor .3 --kappa-floor .1 \
  --height-reserve .02 --tip-budget planned --derived-coefficient-bound .5 \
  --feasibility-max-nfev 500 --epigraph-max-iterations 300 \
  --checkpoint-every 10 --checkpoint-seconds 60 \
  --planar-report topics/visible-flex-new-mechanism/notes/actions-43590239302-1-star_core/star-core-geometry-grid.json \
  --out "$RUN_DIR/cosine-endpoint-warm-a65-b12.json"

OPENBLAS_NUM_THREADS=1 python topics/visible-flex-new-mechanism/scripts/space_star_cosine_verify.py \
  --input "$RUN_DIR/cosine-endpoint-warm-a65-b12.json" --nodes 32768 \
  --planar-report topics/visible-flex-new-mechanism/notes/actions-43590239302-1-star_core/star-core-geometry-grid.json \
  --out "$RUN_DIR/cosine-endpoint-warm-a65-b12-N32768.json"
```

只有新冻结点的正 \(J\)、曲率/厚度必要门和包络预算得到实际证据后，才应启用已经冻结的 `cosine_core_embedding.py`。两侧连接的正交 frame 表示是之后的独立工作，不能由此次核心设计的采样结果代替。
