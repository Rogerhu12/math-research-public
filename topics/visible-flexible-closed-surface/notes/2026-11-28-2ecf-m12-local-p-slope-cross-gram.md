# R252 配套：局部 W 范数、准确背景导数包络与 R226 保底入口

本记录扩展 R252 的实际消费者；数学源仍为原 X+C，原 M12 g、材料图、全部 Fourier 通道及保存场完全不变，未加入 Q。程序的不同版本不是一个新的曲面定义。冻结的 R252 v1 及其首场、第二场完整报告均原样保留。

## 1. 局部微分上界的合法 min

R252 的 tail 公式为

\[
\epsilon_I=d_0+\|L_{B,0}\|_{\rm op}+2v_Ip_I+p_I^2
+2\epsilon_up_I+2\epsilon_A\|W_\theta\|_\infty/r_{I,-},
\]

它只要求 \(p_I\) 是该完整径向子片、所有角度上的 \(\|(W_s,W_u/r)\|_F\) 上界。没有要求 p 必须是一个全域最大值。

新版验证器对每个 tail 子片真实调用原 R236 的准确 `one_piece_bound`：准确 Bernstein 提取/升阶、完整 Fourier 平方范数、角 Taylor 和真实材料尺度均保持。因此所得 \(p_I^{\rm loc}\) 对整个子片成立。若另有该场有效全域上界 \(p^{\rm glob}\)，则

\[
p_I=\min(p^{\rm glob},p_I^{\rm loc})
\]

仍是同一实际 W 的有效上界。min 只选择两个已经证明的上界，不把估计较小或有限样本较小作为依据。尾部 C 恒为零；前缀和可能跨越准确 common cut 的区间继续走原完整 C+W 的 R236 局部途径，不把 tail 分解越界使用。

全域保底允许两种明确入口：

- 给定同场 R236 完整报告时，采用它的 Frobenius 上界；
- 未给该报告时，采用同场已完成 R226 的 `target_orthonormal_differential_l1_upper`。由
  \[
  \|(W_s,W_u/r)\|_F\le\|W_s\|+\|W_u\|/r
  \]
  以及 R226 已证明的全域 C+W 微分上界，这同样是有效保底。

第二种入口没有构造一个替身 R236 报告。输出明确写 `fine_metric_sha256=null`、`global_p_budget_source=same-field-R226-differential-l1-implies-Frobenius`，并绑定实际 R226 报告。每片的新局部 R236 receipt 原样保存。`--local-norm-quick` 只决定何时花计算量收紧角范数，不改变已证上界或非线性目标。

全局 p 较大时，旧充分上界中的固定 \(2v_Ip\) 可能单独就接近要求阈值；这只是该上界公式的过估，完全不是实际误差的下界，也不是不可积性结论。局部 p 直接消除此类过估。

## 2. 准确局部 w_r 必须覆盖整条连接

沿用 R252 同一 reviewed 背景 primitive、calibration、原 source 实现及其身份校验。对一个准确目标半径区间 \(J=[r_-,r_+]\)，先由原点-Lipschitz入口选一个提议源点 \(x_*\)。近似逆仅用于选点，不被断言为准确。

原验证器给该**准确源点**的

\[
r(x_*)\in R_*=[R_-,R_+],\qquad w(x_*)\in W_*.
\]

计算完整连接区间

\[
J_*=[\min(r_-,R_-),\max(r_+,R_+)]\cap[r_{\rm cuff},r_{\rm cut}].
\]

取交只使用已知的物理定义域：实际提议点和所有目标点都属于该域，因此所有真实连接都保留。然后实际调用已有 `Background.derivative_range(J_*)`，没有只在 \(x_*\) 处求一次导数。

该既有入口用全部相交源 profile 的准确前向 primitive 给逆像覆盖；近似逆种子仅是提议，每个端点都由准确前向区间检查。它在覆盖的整个源区间上包络

\[
w_r=\frac{w_x}{A+\alpha B},
\]

仅在分母已证明为正时相除；未能收紧或覆盖不足时返回原全局范围。所有可能相交的 profile 均取并，接口与分支由原已审的区间模型覆盖。

若所得准确向外区间为 D，则

\[
K_I=\min\left(24,\max_{d\in D}|d|\right)
\]

是整条连接上 \(|w_r|\) 的上界。这里只在完整连接位于原 outer 分支范围时启用局部导数收紧；内侧继续保留原点入口使用的准确有理常数 601/100。没有把一个二进显示的 6.01 当成新的准确阈值。

由均值/积分不等式，对所有 \(r\in J\)，

\[
w(r)\in W_*+[-K_Id_I,K_Id_I],
\qquad
d_I=\max_{a\in\{r_-,r_+\},b\in\{R_-,R_+\}}|a-b|.
\]

dI 完全准确有理。最后与原点入口给出的全局 Lipschitz 包络取交：两者都包含真实 w(J)，交仍合法；若交为空则程序报错，不能把不一致结果继续当作证书。输出逐片保存准确连接区间、准确 w_r 区间、KI 和 dI，以便重放。

此改动只收紧 R252 径向冻结误差中的 \(\Delta w\)。A、B、N 的完整交叉 Gram 分子、全部角 Fourier 卷积、材料角误差、Taylor/Laurent 尾、舍入、V×W 与 W² 预算均不删除。

## 3. 实际 M48 完整消费

新版冻结验证器 `2ecf-m12-tail-cross-gram-local-certificate.py` 已对实际 M48 场

`6aafee941eefdada991efa93316f89f9ddbdcd57f05c8bf33a51d19fe74e3d61`

完整自然退出 0，用时 369.532723842 秒。该场使用同一 487 元 unique mesh、既有局部三重 knot 及 M48 的完整 146 个角通道。验证未改变保存的 coefficients 或 knots。

本次原 487 元被完整覆盖为 488 子片：158 个采用原 R236 前缀/准确交界途径，330 个采用 R252 全角交叉 Gram。486 个原元素整片通过，另 1 个元素二分为 2 片，最大实际深度为 1。182 个 tail 子片启用了第二节的准确局部背景导数收紧，其余保持原全局点-Lipschitz包络。

得到严格全域、全时相对 Gram 算子界

\[
\boxed{\epsilon\le
\frac{78935327931739959379617}{79228162514264337593543950336}
<10^{-6}.}
\]

显示值为 \(9.963039079383969\times10^{-7}\)。最坏为前缀原元素 16。所有子片、所有角盒及端点均通过；原固定 cuffs/caps 和完整相位族的延续范围同 R252。

本次明确采用 R226 保底入口：

\[
p^{\rm glob}_{R226}=
\frac{255116356579520618111}{500000000000000000000000}
\simeq5.102327131590413\times10^{-4}.
\]

这只是全域有效保底，实际 V×W、W² 等余项使用每片重新证明的局部 p。此次所有 tail 子片的局部 p 最大值为

\[
\frac{1688022843399138140343223}{79228162514264337593543950336}
\simeq2.130584365244145\times10^{-5},
\]

前缀/交界的完整局部 p 最大值为

\[
\frac{19224365970337710259167}{39614081257132168796771975168}
\simeq4.852912237331399\times10^{-7}.
\]

这些范数也是连续界，没有用数值观察压低。最终报告中的 `fine_metric_sha256` 为 null；其 `global_p_budget_source` 明列 R226 的有效 l1→Frobenius 入口，没有事后把后来返回的 R236 报告添加成已消费输入。

## 4. 与后来 R236 的关系和未完成范围

本次完整验证之后，driver 的原全局 R236 也返回了同一 M48 场的

\[
p_{R236}\simeq2.104776146665369\times10^{-5},
\qquad
\epsilon_{\rm triangle}\simeq4.212168822431749\times10^{-5}.
\]

该旧报告保持原样，未把失败字段改为通过。它不作为本次新版验证的输入。新版验证给出另一个完整而更精确的上界。

这里有一个可以准确检查的预算原因：在真实 cuff 的半径下界上，R252 的统一源微分量满足 \(v>0.0233\)。用后来 R236 的全局 p，则旧公式仅 \(d_0+2vp\) 的常数部分就大于 \(1.006546884346\times10^{-6}\)。这说明该**充分上界表达式**不能靠继续二分来完成这个角落，并不说明实际误差大于 \(10^{-6}\)。本记录的局部 p 与准确局部 slope 给出了保持同一场、同一 g 的实际解决办法。

本场独立 G8/N1536 观察的 metric 峰为 \(6.072530818126161\times10^{-10}\)，属于有限数值观察。它与本记录的完整连续上界分别保留。这里没有执行另一轮 Newton，没有宣称准确等距，也没有由此把 README #5 的整个同 g 真实加密收敛标准判为完成。

新 M48 场的完整几何必须另外消费该 field 自己的 R249/R253 结果；本记录不借首场或 C2 第二场的 reach/held 证书。

## 5. 身份、复现与数据范围

| 本次实际输入/输出 | SHA256 |
|---|---|
| M48 field | `6aafee941eefdada991efa93316f89f9ddbdcd57f05c8bf33a51d19fe74e3d61` |
| M48 grid | `5f366284b435c8911fa1bddcc9bef4cc92c646f06730a959bd4c773b4c3cd7cd` |
| M48 solver result | `c0ca3ce3832b12c188dca87218d87639cbe266c27c129323505ad1d12225b9c2` |
| 同场 R226 | `565a8a5b49e3352cbf09cb5f0bfed4cd0c37ea8348cc1299d46256979bd57d0d` |
| 原 tail 查询报告 | `7d75c93355fb5b79077c8b606294487c02f591e70e40111cac97abcf924da6d2` |
| 原 reviewed 背景 primitive | `28577da04035f91bcd5dc310094d5844347cbeb78d6213dcba0232b62acf56e9` |
| 新验证器源代码 | `138062ba3e48e7aecafdc3e38283c0833a0ffdf9e088832901930de49b393942` |
| 本次完整 cross-Gram 输出 | `da4cdc5c98c68aca4f82433b0672ea6fdbb0a31fada016676ca6dc13963e5f7e` |
| 后来返回、未作本次输入的 R236 | `8e0924c0e0cc52d926342adfb4547d717bfdbfb4982a3ecf8e031b63f2b2bc88` |

实际采用 128 角盒、8 阶角 Taylor 余项、18 阶 Laurent phase 展开、`--local-norm-quick 0.00001`、`--full-surface --max-radial-depth 7`。复现入口为：

```sh
OPENBLAS_NUM_THREADS=1 python scripts/2ecf-m12-tail-cross-gram-local-certificate.py \
  --scripts scripts \
  --data /tmp/m12-prefix-data.npz.gz \
  --field /tmp/h2-c2-m48-03/result.json.field.npz \
  --grid /tmp/h2-c2-m48-03/grid.json \
  --result /tmp/h2-c2-m48-03/result.json \
  --correction-bounds /tmp/h2-c2-m48-03/correction-bounds.json \
  --query-report /tmp/h487-base/entire-half-exact-tail-queries.json \
  --primitive /tmp/2026-11-09-db6f-tail-background-primitive-stable-depth4.json.gz \
  --full-surface --max-radial-depth 7 --local-norm-quick 0.00001 \
  --out /tmp/h2-c2-m48-full-cross-local.json
```

完整输出 1,099,349 bytes 为可重生逐片记录，只保存在 scratch，不进入 git 或 Release。仓库保存本说明、源代码及必要输入/输出身份。原 R252 v1 源码和两份已完成旧场证据不被覆盖。
