# 两个独立显式对称输入的整个实核心 target 型别

状态：**两份连续有向证书均完成。** 原 step02 图的 $|x|\le.25$
与新 D5 图的 $|x|\le\mathrm{binary64}(.24)$ 分别恰有一对 target
简单根 $\pm t$；各自满足

$$
K_0<0\quad(|x|<t),\qquad
K_0>0\quad(t<|x|\le R).
$$

这里始终取各自真实无限 R33 图的

$$
g_0=E(x)dx^2+a(x)^2d\theta^2,\qquad
E=\langle F_x\cdot F_x\rangle,\qquad
K_0=\frac{C}{2aE^2},\quad C=a'E'-2a''E.
$$

这是输出径向 target 度量的型别。实际非径向曲面的 Gaussian 曲率
仍是另一项；此处没有将两种曲率或两种输入相互替换。

## 1. 准确对象与各自结果

| 项目 | 原 sym step02 | 新 sym D5 |
|---|---|---|
| frozen inputs SHA256 前缀 | `bd9b4d14b104183f` | `0d17500ac49c845b` |
| 来源 checkpoint SHA256 前缀 | `05d3e59cf338c5d2` | `0dcfb37f84a1b3d6` |
| 正半核心右端 $R$ | $.25$（准确） | binary64 $.24$ |
| root isolator | 原宽区间 $[.2383698,.2383701]$ | $[.2383968,.2383972]$ |
| 复用的实 collar 左端 | $.23788166874999997$ | $.23815285937499997$ |
| 复用的实 collar 右端 | $.23885823125000002$ | $.23864114062500003$ |
| collar 上 $K_0'$ 下界 | $>45.9092$ | $>53.1248$ |
| collar 外通过的闭单元数 | 176 | 172 |
| 实际二分次数 | 1 | 2 |
| 失败 / 未覆盖单元 | 0 / 0 | 0 / 0 |

表中的 isolator/collar 端点按各自 JSON 所存的准确 binary64 实数解释。
D5 右端的准确值是
$1080863910568919/4503599627370496$。
原图随后另有紧根证书
`type_fixed_step02_symmetric_root_tight_interval.json`，可将其同一个
根收紧至输入 binary64 区间
$[.23836991573145,.23836991573148]$；本分类不需要假定一个近似根准确。

令各自 collar 为 $[c_-,c_+]$，全区间输出给出以下安全十进制界：

| 连续量 | 原 sym step02 | 新 sym D5 |
|---|---:|---:|
| $\sup_{[0,c_-]} C$ | $<-.11683867$ | $<-.00313059$ |
| $\sup_{[0,c_-]} K_0$ | $<-.02335894$ | $<-.00062550$ |
| $\inf_{[c_+,R]} C$ | $>.07207487$ | $>.02824792$ |
| $\inf_{[c_+,R]} K_0$ | $>.01433210$ | $>.00563487$ |
| 全正半核心 $a$ 下界 | $>1.06884310$ | $>1.06872290$ |
| 全正半核心 $E$ 下界 | $>1.22913334$ | $>1.22859827$ |

D5 的负侧严格区下界较保守，来自一整个较宽径向单元的区间包络。
它是严格有效的统一界，不是实际 $K_0$ 最接近零位置的浮点估计。

## 2. 有限覆盖怎样证明整个核心只有两根

每个输入都先按其已付定义显式平均 $a,\beta$ 的偶部、$Z,\gamma$
的奇部；高度取保存 slope 的准确积分。没有施加 Gaussian 卷积。
随后使用同一个 root evaluator 的直接区间 DFT、三角舍入和完整
无限 primitive 尾，计算 $E,E',E'',C,C',K_0,K_0'$。

径向分割包含全部原、反射 knots，以及 $0,c_-,c_+,R$。
闭单元使用 `ClosedSpline` 的准确有理中点及完整多项式 Taylor
包络；因此共同 knots 的低阶 jet 由连续性准确覆盖。若某个单元
尚不能确定符号，才将它二分。每个最终通过单元同时满足
$a_->0$、$E_->0$，以及对应的严格 $C$ 符号。

根 collar 整段复用各自已付的唯一简单根和严格单调证书，不对真实
零点反复细分。由 $C$ 或 $K_0$ 在 collar 严格递增及根的存在，
collar 内根左负、根右正，且没有第二根。外侧所有闭单元均已排除
零点，所以正半核心只剩这一个简单根。

最终报告还将每个单元端点还原为准确 Fraction，分别检查
$[0,c_-]$、$[c_+,R]$ 的首端、末端及每一对相邻端点严格相等。
只有两个闭域全覆盖、无 pending、无失败时，程序才给出“两根”
结论。当前两份报告的 `exact_dyadic_outside_collar_coverage` 都为 true。

显式反射使 $a,E,C,K_0$ 为准确偶函数，故负侧恰有镜像简单根。
腰圈 $x=0$ 属于已证严格负区，不能额外出现根。无需假定原二进制
knots 或旧近似镜像射线已经具有准确对称性。

## 3. 冻结文件与精确重放

共同源 `scripts/fourfold_phase_core_target_type.py` 的 SHA256：

`2e77aa2b5db816224d185a3ffb5eb20ab5b8dfca584dfc392c940f18ad811662`。

原图永久报告
`data/phase_ring_continuation/type_fixed_step02_core_target_type.json`
（191908 bytes），SHA256：

`4e2531b6465b6ea37ade5b3eeb9af6e3cf189c73588420683bfafe8e9965e185`。

D5 永久报告
`data/phase_ring_continuation/type_fixed_step02_d5_jet_core_target_type.json`
（187665 bytes），SHA256：

`135e996917a25d4ad2ebebf415081582970959bba70583eff18e65e603e88dbe`。

从仓库根分别执行：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python topics/visible-flex-exact-nearby/scripts/fourfold_phase_core_target_type.py \
  --inputs topics/visible-flex-exact-nearby/data/phase_ring_continuation/type_fixed_step02_analytic_smoothing_inputs.npz \
  --root-certificate topics/visible-flex-exact-nearby/data/phase_ring_continuation/type_fixed_step02_symmetric_root_interval.json \
  --right .25 --out /tmp/visible-step02-core-target-type.json

OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python topics/visible-flex-exact-nearby/scripts/fourfold_phase_core_target_type.py \
  --inputs topics/visible-flex-exact-nearby/data/phase_ring_continuation/type_fixed_step02_d5_jet_interval_inputs.npz \
  --root-certificate topics/visible-flex-exact-nearby/data/phase_ring_continuation/type_fixed_step02_d5_jet_symmetric_root_interval.json \
  --right .24 --out /tmp/visible-D5-core-target-type.json
```

可加 `--resume`；输入、源、root 证书、全部依赖或算法参数变化会被
拒绝恢复，避免混合不同版本。每10次尝试及每次需二分时保存进度。
两份报告都保留每个闭单元的完整目标 jet 区间和无限角误差预算。

结论只覆盖各自所列核心。外部正帽、全体实际 Gaussian 曲率型别、
参数管中根的一致分类、精确等距方程与闭合可见等距族仍需单独构造。
