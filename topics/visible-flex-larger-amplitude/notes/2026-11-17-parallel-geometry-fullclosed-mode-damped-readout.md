# 同一全闭模型的一次 mode-damped 初猜真实 Gram 读取

2026-11-17，geometry_amplification。**一次新初猜、一次残差读取；没有参数扫描、Jv／伴随重验或非线性求解。** 相同 N2048 点集上的最大相对 Gram 由原长 Hermite warm 的 `147.40629026335586` 降到 `.6551089574780629`，仍远未通过 `1e−6`。原 warm 的失败数值、FFT 第一版接口失败及其修复对照均保留，不以本条覆盖历史。

## 1. 明确的新输入及保持项

输入为 model 唯一生成的 `parallel-model-fullclosed-mode-damped-warm.npz`，SHA
`9bf60ea31f40239cb657a01a93242e32a024f448d1ebffaf22515de52c022cbd`；生成报告 SHA
`17697da3d5994f52c21ee481576c78fa67b7cc33152a78e1ee1202a4ea02ad19`，producer SHA
`632d6cfc5f3113bc6f64c340fe9d066a1614c5b0bd649a357bdea2d0d94af6e8`。

生成器选择同一参考 `B=a C_M+[Hcap−zref(S)+zref(s)]e_z`。把实际 cut 的三 jet 差按固定模态率
`λ_j=max(1,2j)/a(1)` 乘 `exp(−λ_j t)`，用二次因子准确匹配 cut 三 jet，再乘 `1−S5(t/(S−1))` 退到零。它是一次明确的新 warm 选择，不是已经求出的等距尾。

本读者在评价前准确核对：与原 401255 bundle 的全部 mesh、a_stages、R、Hcap、width、前三 core 参数相同；原 `s≤1` 的 819 节点 q 三 jet 逐项相同。总计仍为 923 节点、1845 个节点／实际共同 quintic 中点、M160/N2048、1,332,245 自由变量、11,335,680 个完整角值残差。

`pack(require_affine=True)` 确认原输入已经满足全部仿射条件，未作任何隐式投影：core Z、U−ez、Az 以及末端 q 三 jet 字面为零。完整物理 lift 没有截频，端口仍由同一 `Θcore` 参数化，径向三 jet `(R,−1,0)`。模型的解析表达式仅生成这组 literal 节点三 jet；实际读数消费它们定义的共同 quintic，而非拿解析生成公式的中间导数替代插值导数。

## 2. 一份完整残差数组的实际结果

仅调用已通过 dense 对照的 FFT v2 `residual(x)` 一次。所有下表分区和分量统计均由这同一数组生成，没有第二次几何扫描。

| 区域／评价点 | 最大相对 Gram 算子范数 | 峰位置 |
|---|---:|---|
| 全体节点及实际中点 | `.6551089574780629` | 中点 `s=1.3480413751845672, φ=0` |
| 节点 | `.654891689915142` | `s=1.3380077824366778, φ=0` |
| 原 `s≤1` prefix | `3.612387315167883e−5` | 节点 `s=1, φ=.18407769454627693` |
| 新 `s>1` 尾部 | `.6551089574780629` | 同全域峰 |
| 末端 lift 区域 | `.010309783303406594` | `s=2.321299871729826, φ=0` |

全体三个 Gram 项 `ss / sφ / φφ` 的绝对最大值为

` .6551089574780629 / .28295935107149034 / .30131700666533834 `。

这次已由径向项主导；原 warm 的巨大角向项 `146.90242962577042` 不再出现。全体指定点的相对 Gram 行列式最小值为 `.6626282663808325`；完整 Frobenius 平方和为 `24260.05386676475`。这些均是 ordinary binary64 点值，不是连续浸入、嵌入、reach 或全闭 metric 证书。

prefix 虽在本次初猜构造中未改，它在**当前 Hold 目标、M160 字面场及当前角参数化**下已有上述 `3.6124e−5` 节点误差。因此，若后续把这个 prefix 永久冻结，只改它以外的尾部，该原样节点仍不能通过 `1e−6` 数值门。当前全闭模型本来保留内部 prefix 的 Y/U/A 作为未知量；本条没有另添冻结限制，也没有把此节点读数冒作另一个规范化后的场的下界。

## 3. 来源与复现

| 文件 | SHA256 |
|---|---|
| 唯一读者 `parallel-geometry-fullclosed-new-warm-residual.py` | `48624cf05c616a513da68d7db755fea00dfb8ac068b594d42fc300e3f082fd35` |
| dense 父算子 | `e7aa70c3458f2b1bf823d19870da4e050d50125c31d161d94e2cc8c3cb384b6d` |
| 已对照 FFT v2 | `7ab7391f3d351a5c2314d3c136fe5aa708612bb53e45221d2c09efc0fb622211` |
| 完整 report | `b361a25451390db061e489de1df6aef39725928e7390ffe346819c063f3b692e` |
| 仅仓库外的原 residual.npy | `f0c3a300dcb5f20ac8d4995a657b39869aa0adb3eb0c5085dd87f76e086454c1` |

完整 report 为 5483B；原残差数组 90,685,568B 只留 scratch。唯一残差评价约 1.703 秒，计时仅作当次环境记录。

```bash
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python parallel-geometry-fullclosed-new-warm-residual.py \
  --operator parallel-geometry-fullclosed-gram-operator.py \
  --fft-source parallel-geometry-fullclosed-gram-fft-v2.py \
  --original-bundle parallel-model-fullclosed-hold-warm.npz \
  --bundle parallel-model-fullclosed-mode-damped-warm.npz \
  --bundle-sha 9bf60ea31f40239cb657a01a93242e32a024f448d1ebffaf22515de52c022cbd \
  --out parallel-geometry-fullclosed-mode-damped-residual.json \
  --residual parallel-geometry-fullclosed-mode-damped-residual.npy
```

复现使用新的输出位置；入口拒绝覆盖。固定 scalar／symbolic mesh oracle、普通浮点载体误差、原 pulse 与 Hold 在 `.995` 后的 g 区别均沿用生成报告，本条没有给这些误差另外作全场区间封闭。这里确认的是一个更接近目标但仍不合格的实际全闭 C² warm；不把初猜改善当作新 solver 接受、精化、全局几何或课题完成。
