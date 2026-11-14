# Request17：实际 warm 下降、域限制与合法续接

本记录只分析已完成的公开 Actions `43598917532` / job
`132459290659`，源码提交 `4b8b2bfdd417f76574dcc2a8e2353c4c2dce3e21`。
artifact `14116526155` 的原 ZIP 为 25,507,381 bytes，SHA256
`5a0bddbd39739ed94e382d6a8b7fd74dec3ca19febbf9369d20667b9506e8242`。
下列数值均来自该 artifact 的 `constrained-warm/`、
`physical-response/response-check.json` 和
`full-DN112/RMS-domain-preflight.json`，本地没有重新求解或做新的科学数值实验。

## 1. 实际完成了什么

精确约束坐标保留全部 M112 物理场、109 个自由高 core 系数和 3 个全局
scalar 控制。左端约束及跨节点常数条件由坐标恒等满足；699 个原节点保留。
初次入口投影的实际最大改变为 `3.469446951953614e-18`，所以不称初始所有
状态逐位不变。三个模型共用时 `633.0520121760001 s`，各保存一次真实 merit
下降。它们仍明确标记 `success=false`、`new_coupled_finite_acceptance=false`。

每个模型的行权重固定于其自身线性化与所有 trial，下一模型会重新取权重。
因此只能在同一行中比较 before/after，不将跨行 before 的差当作同一目标函数的下降。

| 模型 | 接受方向的 damping | 实际 alpha | 同模型 merit before | 同模型 merit after | 实际下降 | 实际/预测下降 |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 10 | `2^-14` | 44.44787720229487 | 44.44721499298322 | 0.0006622093116490646 | 1.0000162700833308 |
| 1 | 30 | `2^-15` | 44.44736933003768 | 44.44719408791289 | 0.00017524212479003154 | 1.0000371333209068 |
| 2 | 90 | `2^-15` | 44.44724777852967 | 44.44715711179736 | 0.00009066673231217237 | 1.0000347877000708 |

模型 0 的第一方向 damping=1，17 个原 backtrack 未通过完整域检查，随后
damping=10 才取得上表下降。四次 LSMR 都在 80 次迭代以 `istop=7` 停止。
这不是线性方程或完整 BVP 已求解的标志。

原物理 collocation 最大绝对残差只从 `0.0071105950777444905` 变为
`0.007110547307418288`；完整右边界最大残差从
`9.607979083759376e-8` 变为 `9.606803272021844e-8`。
没有达到原 `1e-6` RMS / `1e-11` BC 接受门。

## 2. 限制下降的是 turn 内的实际 RMS 查询点

最靠近成功步的拒绝不是 merit 比率失败，也不是末端 bridge 的节点失域。
三个接受方向的前一档 alpha 均已节点、中点有限、真实 merit 下降，但在
同一个原 Lobatto RMS 点失域：

- interval `473`，端点 `1.1993469629899143`、`1.2043314144896742`；
- fraction `0.17267316464601146`，实际 `s=1.2002076440044023`；
- physical angle `phi=0`；
- `a=1.1899847955223861`，`a'=-0.14863126227800036`，
  `a''=-2.472231719360121`。

模型 0 / 1 / 2 在接受前一档的该点 `beta^2` 分别为
`-0.055896145729418256`、`-0.004695716326368338`、
`-0.0022482035027562297`。再半步才全部有效。
最终 warm 的原 full-DN preflight 在该点给出正侧最小值
`beta^2=0.0007799746649373995`。它比该 warm 的节点最小值
`0.005147953492641522` 和中点最小值 `0.005147035027030511` 小。
这再次说明节点/中点有限不能替代原 RMS 两组查询。

四次 LSMR 的 normal residual `normar` 依次为
`0.16486672958449408`、`0.05085701358489482`、
`0.027985778897540607`、`0.0019230086170690438`。
最后一次 `normA=30.19738497029573`、`normr=9.269469348690304`，
故 `normar/(normA*normr)` 约 `6.87e-6`，仍高于其原 `atol=1e-7`。
这给出增加内层工作量的具体动机；不能仅因为带正则项的 `normr` 大就断言
LSMR 不足。最后一次 80 步用时 `8.636328602999924 s`，比整模型组便宜。

另一方面，实际预测比率已近 1，三组独立中心差分的 merit slope 与原
`gdot` 一致。向量方向差分在更小步长时误差上升，不能把它改称机器精度
的全方向验证。当前数据直接支持的是：域边界限制了这些真实下降方向，
而不是宣告阻尼或原下降公式错误。

## 3. 已检查的实现与文件身份

三模型原 augmented block 与约化 action 的最大相对差不超过
`8.728705718947608e-16`；三类伴随内积的规范化误差不超过
`2.2767938663694886e-18`。独立原 nonlinear collocation 的 global-core/control
complex-step 检查为 `8.673617379884035e-19`；其范围不冒称覆盖所有内部物理方向。

在实际 `warm-003` 上重新进行完整 Rphi Richardson FD，最大误差
`9.51710770488038e-10`，通过原 `5e-5` 实现门。此报告明确使用真实零 H 的
完整 J 作为 affine map，没有宣称新 H 的 native 解已完成。

| 文件 | SHA256 |
|---|---|
| `constrained-warm/optimization-intent.json` | `3ccf461af1d3f6d928837f52e0b6b830ff3737c43863eed0cf919c470102d347` |
| `constrained-warm/model-000.json` | `79e8d64eacd1992138b328fd62e9046362f690fd9b8e2221f06f757017fdfd07` |
| `constrained-warm/model-001.json` | `f33f2a9c5b45b27f81cbbccaeea552d6472c4fb67423927293d902e56e410a23` |
| `constrained-warm/model-002.json` | `1a6b9946512b95b2bb1ae1b92b28ff864472927899ca2b7a85311b9bb4e02e79` |
| `constrained-warm/warm-003.json.gz` | `5d1c452291099ad18b1a619ba3794614b04a0c620b8ed0f28887a84731ef7886` |
| `physical-response/response-check.json` | `2cd0dc68993ee5b4391fc18d96729ea7a2aaacbf9764923853844035d0866bbb` |
| `full-DN112/RMS-domain-preflight.json` | `853521aa164f99e6601ad0033fe62221330f3371766150a47bb142be5d8267cf` |

`warm-003.json.gz` 为 4,702,259 bytes，完整保留。其 scalar 参数为
`[-8.110228194716162e-20, 2.246526817231686e-20, -7.837363822225848e-20]`。
实际 producer ledger 的全部九个源 SHA 已逐一与冻结源码核对相同。
后续重启应继续核此 ledger，不能仅信任文件名或 `optimization_warm.schema`。

## 4. 最小的有依据续接及分支

已选定、尚未执行的 request18 同源续接是从上述 `warm-003` 只接一个模型，将
`--lsmr-iterations` 从 80 改为已允许的 200。初始 `--damping 270`
是原更新规则对最后一次 `90`、`alpha<.25` 给出的值，不能重新默认成 1。
保留全部原输入 SHA、699 节点、频率、真实零 J affine 参考和原门。

```sh
python computations/geometry_20261114_constrained_trust_warm.py \
  --accepted "$ACCEPTED96" --prepared "$ORIGINAL699" \
  --tail-anchor "$COMPLETED_ZERO112" --tail-config "$CONFIG112" \
  --resume "$REQUEST17_WARM003" --out "$FRESH_WARM_OUT" \
  --iterations 1 --lsmr-iterations 200 --damping 270 \
  --damping-attempts 5 --line-search-steps 17 \
  --budget-seconds 1200 --jac-workers 2 --angles 4096
```

本轮只做 warm，不自动重发相同的失败 native 请求。这检验更充分的同一
正阻尼最小化是否改变 interval473 的限制方向，不预言
它必定改善。若仍只有约 `2^-15` 的步、且该点余量继续趋零，仅追加模型或
抬阻尼没有足够证据。此时合理的新算法方向是将实际 Hermite RMS 查询点的
`beta^2` 完整导数纳入局部可行方向计算；须包括两端实际 RHS、全局 p 和
非线性中间值链式项，并独立验证。该约束是 warm 优化方式，不能替代或
放宽原完整方程、域、RMS、BC、真实尾及最终 audit。当前未实现或调度此分支。

后续每次新 warm 必须重新生成与其真实 SHA 绑定的 FD 报告，不能修改旧报告
中的 SHA 冒充实测。原四输入继续为：

- accepted `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff`；
- original699 `0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714`；
- completed zero112 `e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51`；
- config112 `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5`。

## 5. 与首个非零 native 请求分开

本次 full-DN 在第一次真实非零 H 请求失败，尚未进入 inner collocation。
没有新的成功 H/J 或 final audit 可作为下一 affine anchor；失败回执完整保留，
不能把它包装成已完成 native map。该独立失败由 native 回执记录详述。
微小 H 不能阈值归零。几何侧核实 terminal 的 112 个非均值 z 系数均非零，
原 MaterialTrace 已将均值投影列显式置零，所以也不能把它解释为 z0 漏入
后删除。

以上 warm 续接若执行，仅改善原 affine 参考下的完整初猜；新 H 仍须真实
native 求解，之后才可能进入原 full-DN 全流程。没有完整接受父场之前，
不能用这些 warm 启动宣称已接受的同 g 精化或闭面幅度结论。
