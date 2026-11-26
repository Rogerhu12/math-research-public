# R582 有限非圆入口的 radius-only 最小修补

接原 run `45824332845` / job `139924470256` 的自然实现失败，详见
`2026-11-26-r582-finite-resonant-first-original-receipt.md`。原 field、
Model、driver 均冻结不改；新独立 wrapper 绑定原三份 SHA。

## 1. 只去掉不需要的高度积分

原 `angular_radial_jets` 的公式只用参考半径 a、a_s、a_ss，但通过
`ContinuousMean.jets` 额外计算了 H 和 z 的 jets，导致细网构建中的
QUADPACK 异常。新 `RadiusOnlyField.reference_radius_jets` 逐项复制
该接口已有的半径计算顺序：

\[
 \alpha=\beta P_a,\quad
 a_b=(1-\chi_b)r_{core}+\chi_b(r_c+L-s),\quad
 a=e^{\alpha}a_b,
\]

先按原式取 a 的三 jets，再乘固定 `exp(mu*psi)` 及其完整一、二
导数，保留原先分两次 exponentiation 的浮点运算顺序。这个接口
不需要 H、z 或 ν 的任何值。u/v 的二导商法、core 角 forcing 扣除
及原完整 material Hermite 表示全部原样。

wrapper 只替换 driver 的 `ResonantField` 类、input 审核和 schema，
其余 fixed-p stage、hard rows、全部细观察点、margin、epigraph、
接受规则、首次必要 AD 方向核、clock 和 checkpoint 不改。
特别不删近重复位置，也不把 4811 已付观察网改稀来避免异常。

## 2. 旧科学已经发生，必要再求值仍须计费

原 run 已完成 160 段/960944 RHS 的新 dense 场、2510/206 RHS 的
两条 s-ODE 和 62878 个 Hermite 端点。完整 mesh/六 jets hash 是
`0d222bd12ce8a61d0c88264c6fb5c82066f0ca058855b5bf7a670a53b483a991`，
但整份数组没有持久化。新正式 run 为得到几何所需内场必须再次求值；
新费用另记，并输出新 mesh 是否与已付 hash 完全一致，不宣称免费。

stdin 在原 96819 B 小输入的基础上只增加真实失败 origin 和成本
ledger。移除这两个新增元数据后，必须准确还原原 SHA
`387d58a18278b1b46cbbe6e834d24d42c8eeb84bf9d3e95e3030d629dac51852`。
因此 q、μν、M169/factor8 口、λ、原 4811 点和旧账均不可暗改。
新 stdin 是 98910 B /
`187a463fdd777d2884310ac0793ed96583d5216d47407795b53daae633c46ac4`。

原 `70.62187625499996` 秒科学时间、71.301830 秒 child wall、完整
field/model/原权计数保留且时钟类型分开。未重做旧 inner DtN、旧三
种子比较、圆核恢复或真 core root 优化。原有限非圆后端尚未进入，
所以本次首次几何/AD/优化不是重复一个已经完成的有限 stage。

## 3. 文件及状态

- `scripts/r582_finite_resonant_radius_only_20261126.py`
- `computations/request-r582-finite-radius-only-20261126.json`
- `.github/workflows/visible-r582-finite-radius-only-20261126.yml`

旧三份科学源及全部传递依赖仍逐一绑定。新 request 是单 lane，
2400 秒科学预算/50 分钟 job，真实双仓 pull/规则检查、固定 runtime、
stdout only 无 artifact/cache。此处只作源码/AST/hash/sparse/input
静态核；不额外执行一个预检科学 run。正式运行结果及全部新费用
再据自然终态原 stdout 登记。

原数值 Hermite 零尾与数学无限 kernel 的差、ODE/primitive 误差、
固定 g 精化、整个非圆族及全 reach 缺口完全保留。
