# Request142：完整九方向重新形成响应、保留原 normal 求解的一批实际入口

作者：AI（/root/amplitude）。日期：2026-11-15。

## 1. 当前交付和实际依据

本交付是可直接由本公开仓库 Actions 执行的独立候选算法入口。它从 [R307](../results/R307-actual138-complete-normal-trace-selection-and-thirty-two-batches.md) 的真实 actual138 第32批末九参数和末半径开始，只执行一批原八方向。没有填写未来 run、job、结果或接受声明。

actual138 原32批均完成，256方向均各有一次原外接受，但原 merit 从保存的 fresh 初值 `4.963213836829283` 到末值 `4.963213789290057`。R299 在358次外试探中的259次改变返回点，然而已接受返回点所对应的同次 working return 也都通过原 Armijo 界，直接救回数为0。末保存3×9响应的 condition 为 `1756532079795.7976`；这些原有限诊断不证明精确秩、根不存在或完全停滞。它们支持现在直接试验不同的响应形成路径，而不是再排32批相同极小步。

唯一数学算法变化是外方向响应：采用已发布 [R310](../results/R310-complete-nine-directional-response-basis-and-finite-error.md) helper，沿完整九维基分别重新调用原 complex evaluate，并沿实际形成的方向再调用一次。原 [R299](../results/R299-same-normal-trace-full-merit-selection.md) normal helper 的源字节、所有原实数域、外 Armijo、半径更新和末端责任均保留。实际 normal 轨迹会受新方向和新 target 影响，不声称与138逐值相同。

## 2. 真实初始来源：不是已接受非零场

短配方只读取以下已经发表的原字段，不恢复、重造或冒用已删除的原 status/J/状态数组：

- repository：`Rogerhu12/math-research-public`；
- run：`43710284131`；source：`0be175792723e0663809146e3922e7052e906c09`；
- compute/report jobs：`132800138064`、`132801971383`；
- 原 producer：`geometry_20261115_small_core_nine_control_same_trace_merit_recipe.py`；
- 原 producer SHA256：`e8704af6daa13eac4d0301a6ef1debdca4c9cb0b10a806544644a2e1d162329a`；
- 原 schema：`R259-nine-control-full-three-two-normal-same-trace-merit-carried-radius-trust-recipe-v1`；
- 第32原 status：973393 B，SHA256 `42df80cf0bdfd42a107b20d2ab994d92be64b8ab148ef54b915008a8a938e134`；
- 第32原 primary：67945 B，SHA256 `2dab4f53ee03392f7888ff3386b56b8ea6253a8d90897d560f53f076e7aca409`；
- 原 complete view：294395 B，SHA256 `ee50d014b20bf667c145249ab0c1685cc269e7f15aea3b85c3d382b0cd4b76d4`。

原字段为 `final.parameters` 与 `final_relative_trust_radius`。完整初猜为：

```json
{
  "parameters": [
    0.3055213765780896,
    0.21645017443068498,
    0.34270035782290403,
    -0.06322330093655137,
    -0.017474512907261836,
    0.9376116549666047,
    1.0751305682653982,
    0.6886902199638585,
    0.9385448548742756
  ],
  "relative_trust_radius": 3.814697265625e-7
}
```

这是原同一九族的有限初猜，原 native、unit、full112、nonzero 和 success 并未被本配方改为通过。新 entry 必须 fresh evaluate、fresh description、fresh 原九轴 J；父 merit、J、FD、Arb 和圆检查均不复用。跨运行同一点不承诺有限数组逐位复现。

配方有独立文件字节身份，不能把它称为原 status：`actual138-final-nine-control-directional-response-recipe.json`，2449 B / `29bf38f8a91063cbe0a6982bc015684e512fbdbbb65ac97dcb8703f9ce5ea1ac`。它携原半径，不重置为0.1、不取下界、不修复零值。若以后显式 own-schema 原配方的半径为0，原正半径方向要求按真实结果停止。

## 3. 文件和来源身份

六运行文件都小于100KB。Git blob 仅保全独立小文本对象，没有更新 ref、分支、PR 或 dispatch。

| 角色 | 文件 | UTF-8 B | SHA256 | Git blob |
|---|---|---:|---|---|
| producer | `geometry_20261115_small_core_nine_control_directional_response_recipe.py` | 50186 | `5acf5b029a756a356a3de3d598211eaa89df4a7670fc703f2d3567488e09bae4` | `23fded0d61e03a1a149b3de677495b8c9ebd4139` |
| reader | `root_20261115_small_core_nine_control_directional_response_scalar_readout.py` | 33152 | `f3a236a3b1a18ad8eacaafe32e166cb8c5d7c96d1cd9a7a6573f0105156073f6` | `eb8581b23dbf960d5149106c892d4d70f51163e3` |
| wrapper | `geometry_20261115_nine_control_directional_response_temporary_batch.py` | 57190 | `5c482ac3504686b32c945d6ec0b589e5f986f07accce158e6a61712b37f77f4d` | `43702c507d2a87fde442a675c5de674dd023b17c` |
| recipe | `actual138-final-nine-control-directional-response-recipe.json` | 2449 | `29bf38f8a91063cbe0a6982bc015684e512fbdbbb65ac97dcb8703f9ce5ea1ac` | `6d15db3678f84426a6f6ae20c0ed0a43d8e59686` |
| request | `public-nine-control-directional-response-request.json` | 53230 | `84f03b2e8e9a19b8be1141d5903aef095a3aeb9a7535b577190777cd02d3d394` | `2f5c7327464a0083f2c29ffe1bcdf4e862e2762f` |
| workflow | `visible-larger-public-nine-control-directional-response.yml` | 22475 | `f6a49341e26bc97f9cb7f76fece6c564982d4ed39b94a7c03a02bcab19e7db94` | `4d51bb322d92ea88fe27acd5272a55b1ec1c78ee` |

发布位置：

- 三 Python 入口、短 recipe 和 request：`topics/visible-flex-larger-amplitude/computations/`；
- workflow：`.github/workflows/visible-larger-public-nine-control-directional-response.yml`；
- 本接口：`topics/visible-flex-larger-amplitude/notes/2026-11-15-request142-complete-nine-directional-response-interface.md`。

已发表 helper 不另改写：

- R310：`geometry_20261115_nine_control_directional_complex_response.py`，20172 B / `50044473f14b34c9451360debaa1ec9189f0a7924957098cafc37df3f849643f`。
- R299：`geometry_20261115_nine_control_same_trace_full_merit_candidate.py`，19265 B / `d4c9cd448b81e3c506984a273cb0e050cf806ebc109ad4d2b140cec9fa8d2cbf`。
- 原九 family：`geometry_20261115_small_core_nine_control_family.py`，SHA256 `086572f9a9fc172d671f050e9b343b66c4a57c5c88867537a1e8a3daa5ab9629`。
- 原九算法祖先824c、原 carried-radius ed786 和 actual138 e870 均保原来源身份，不调用其 main 冒本入口。

request 保留 actual138 全90项 source pin、全部4项 support pin，再增加 R310 helper、新 producer、新 wrapper 和新 reader，成为93+5。原参数来源 producer 完整29项闭包逐项保留；当前 producer 增加 helper 与自身，成为31项。历史原九26项仍是明确的子闭包。wrapper 和 workflow 均逐文件核实际 SHA；这些都是已有来源责任，不是额外数学精度门。

## 4. 完整外方向及保留的原 metric

设原完整三残差为 $r=F(p)$，原九轴 pilot 为 $J_0$，原参数尺度为 $S_j=\max(1,|p_j|)$。当前真实域上的 $r$ 和 $J_0$ 仍由原模型形成。

新 helper 以 $J_0\operatorname{diag}(S)$ 的行平衡转置作完整 pivoted Householder QR。零 pilot 行仅在选基的 row scale 用1，不删除该行，不按 R 对角截秩。全部九个 Q 列保留。令 $V=\operatorname{diag}(S)Q$，并实际形成 $G=V/S$。

对每个完整物理基列 $V_j$，调用同一个已绑定原模型：

$$
K_j=\operatorname{Im}F(p+i h V_j)/h,\qquad h=10^{-25}.
$$

这里 $h$ 是原 source 的 literal，不自适应改变、不归一化方向。新 $K$ 不是把已形成的九个大轴列相加；同时保存原 $J_0V$ 供解释，未用它替换 $K$。即使某个 pilot 方向很弱或在 pilot 中为零，也仍实际付它的原响应。

外方向求解完整12×9正阻尼系统：

$$
\min_w\ \|r+Kw\|_2^2+\mu^2\|Gw\|_2^2,
\qquad d=Vw.
$$

全部原三残差和九参数列都在。下块保实际 $\mu G$，不因有限 Q 来自 QR 就偷换成 $\mu I$。使用完整 pivoted QR 和9×9三角回代，没有 normal matrix、rcond 或奇异值截断。半径检查使用实际形成的 $d/S$，不是假设与有限 $Gw$ 逐位相等。

阻尼 floor 仍为原 pilot 尺度的 machine-epsilon 量；原至多64次上界 bracket、64次 geometric refinement 的结构保留。正阻尼和完整 metric 的精确换基等价见R310；有限 QR、矩阵乘积和原 complex 链仍有舍入，并不因这个恒等式就成为精确原导数。

形成实际 $d$ 后再独立调用一次原 complex evaluate：

$$
a=\operatorname{Im}F(p+i h d)/h.
$$

返回原外层使用 $a$，同时完整分别保存 $J_0d$、$Kw$、$a$ 和它们已计算的差值。这些动作一致性读数不增加 gate，不设置改善 margin、不用旧动作作隐藏 fallback。每个成功方向最多增加九次基响应和一次实际方向响应，原八方向最多80次额外 complex model call；不是80次新真实外试探。零方向的 helper 线性特例不调用 evaluate，真实调用数按保存报告读出。

## 5. Pilot normal plane、直接 target 与曲线起点导数必须分开

原 normal frame 的计算仍取 $C_0=J_0[1:,:]$ 和原完整9×2平面 $P=\operatorname{diag}(S)N$。R299 原 normal helper 的 fresh derivative 仍是原 model.jacobian 的全部九轴列及完整 projected2×2 QR。本实验不调用 R310 可选的 `normal_directional_response`。

目标变为同一原三残差的两个分量：

$$
c(p)+\alpha a_c,
\qquad q(\alpha,w)=p+\alpha d+Pw.
$$

原 full real merit 仍是 $\tfrac12\|F(q)\|^2$，残差不被 target 或0覆盖。原外层计算 slope $r^Ta$ 并保其非有限或非负停止；真实原候选需满足原

$$
W(q)\le W(p)+0.2\alpha r^Ta.
$$

这只是以数值直接动作替换原数值轴列组合的独立候选算法，不把有限 $r^Ta$ 声称为真实曲线导数。

在R310明确的理想光滑模型下，如果真实 $CP$ 非奇异且内层真正解到相应方程，则

$$
q'(0)=d+P(CP)^{-1}(a_c-Cd).
$$

只有真实 $a_c=Cd$ 时才能推出 $q'(0)=d$。此次 finite normal correction 仍有实际 tolerance error；stored pilot $C_0$ 和直接 $a$ 并不自动等于真实 DF。源码明确把原起点 readback 字段命名为 `formed_pilot_path_origin_*`，另保 `actual_direct_complex_action_used_for_target`、`pilot_axis_J_times_predictor` 和 `target_action_minus_pilot_axis_action`。这个报告不是新的接受门或IFT证书。

## 6. 原完整搜索和最终责任

source-only 对比已确认，新 producer 从 `slope = float(residual@action)` 起，原实数试探、接受、半径更新、最终 description/FD/Arb/圆检查以及 except/finally 尾逐字与 actual138 一致；`norm`、`next_radius`、`full_column_qr_solve` 和 `load_selector` 保原函数。

保留：

- 八个完整方向预算，已接受和整方向拒绝都计一次；
- 每方向20个原外 alpha $2^{-j}$，$j=0,\ldots,19$；
- 每外试探原12次 normal Newton、每次20次真实 inner backtrack，原目标绝对误差 `1e-8` 仅用于内层停机；
- inner target flag 为false不新增外门，原 R299 只从该次已完成 working trace 的实际 finite state 选 full-merit最小者，原 working return 赢平局；
- 不救回未完成 working call，不把异常点当候选，不添加 model.evaluate/J 给 selector；
- 原相对半径规则：accepted backtrack、预测比率等按原函数更新；整方向20档全拒则quarter，仍不收该试探点；
- fresh 初末九列、每列三档原 real FD，完整 scalar Arb 域、原453维圆检查和完整112原 residual/final flags；
- 原 unit/full112 停止、不接受时的 wrapper 停止、真实异常和资源partial的区分；
- 没有 native nonzero solve，没有完整非零场成功声明，没有新rank、最小奇值、FDagreement或候选进步阈值门。

单批调用可形成真实末p和真实末半径的新短 recipe供后继读取，但当前 request 不会启动第二批。即使0个接受、方向形成失败或原停止提前到来，也保实际已做行与未执行计划责任，不伪造八个方向或新完成状态。

## 7. 可执行接线、预算和临时生命周期

唯一 push trigger 为：

```
topics/visible-flex-larger-amplitude/computations/public-nine-control-directional-response-request.json
```

新 workflow 名字为 `visible-larger-public-nine-control-directional-response.yml`；不修改 actual138 workflow。runtime 为 Python3.12.14、NumPy2.3.5、SciPy1.17.0、python-flint0.9.0，原单线程环境保留。

编排入口完整 CLI：

```text
python -u geometry_20261115_nine_control_directional_response_temporary_batch.py
  --request <current-checkout/computations/public-nine-control-directional-response-request.json>
  --request-sha256 <SHA256 of those complete request bytes>
  --repository-directory <fixed science checkout>
  --original-input-paths <request-owned RUNNER_TEMP path map>
  --rules-directory <request-owned rule-sync>
  --out <fresh request-owned RUNNER_TEMP/nine-control-directional-response-temporary-batch>
```

wrapper 按原 `science_argv` 传四真实数学输入、完整短 recipe/SHA 和原全部 options，显式传 `--initial-relative-radius 3.814697265625e-7`。producer 实际源和schema是本文件表中的新身份；reader只读这个producer生成的 `nine-control-directional-response-carried-radius-status.json`。

四原输入仍从真实公开历史 `8bd267107cc8710d371f3b62c02986655ac965b0` 临时恢复并核原bytes/SHA；原78公开数值 source 使用已有 `prepare_public_source` 恢复。input hashes：

| 输入 | SHA256 |
|---|---|
| accepted | `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff` |
| prepared | `0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714` |
| tail anchor | `e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51` |
| tail config | `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5` |

原 job90min / scientific step75min 保留，CHAIN 的3600s只在完整批之间检查；现在最多一批，不在八方向之间引入新截断。没有 child timeout 或新 process session。超时/规则中断如实partial，不称科学全拒或无根。

原3b8规则 runner 源不改，2700s真实 pull/rebase/README差异处理保留。显式 reviewed root/topic blobs为 `21bd547f56590b7f2dd279d0297efb289a9b2783` / `bff8aea253a9e6a7a4fac28d810ac454c5499fec`；只将已读当前全文设入原runtime BASELINES。原唯一“规则同步记录：”与H字节上限保留。setup保 `git config --global merge.stat false`，不改变科学或同步规则。

完整 child status先临时保存，reader与wrapper均在清理之前消费。已完成的原 primary、各 lossless方向组和全部normal记录进入 compute原stdout；独立 report仅传小chain索引。原 request-owned 输入/source-cache/科学payload消费后按属主、symlink和RUNNER_TEMP范围责任清理。无 raw artifact、Release、main数据上传；没有未来原始数组恢复声明。

## 8. 完整输出、失败和90KB边界

新 reader按已返回原字段保：

- 每方向的原p、r、九轴pilot J、半径和原reason；
- 所有完整Q/R/V/G/K、九个原 complex probe、增广12×9与全部QR和阻尼search；
- 实际方向的独立complex probe、三种动作、原slope与pilot曲线起点读回；
- 各原外试探17列、每个seed读数、全部R299 normal迭代/试探/异常/候选样本/working return；
- 所有原初末9列FD、Arb、完整圆与原final flags，实际status/source/input/recipe身份。

producer 在helper调用前即挂 `complete_directional_response_probe_readback`。若新helper中途异常，已经完成或正在失败的原probe、实际实/虚输入与方程或原exception都仍挂在本方向；未成功返回的helper内部basis/QR报告不被捏造成完整结果。此时原stop/异常路径继续决定结果。

reader无科学计算，只取完整direction_model与curve_frame记录，不用旧pick表删掉新矩阵或失败字段。所有normal记录仍完整；每个JSON片段≤90000 B，跨片有完整路径、顺序、字节数、SHA和整组canonical identity。单个大方向不是删字段的理由。primary若需移动具名字段，原lossless协议保其完整组；真正不可表示时诚实失败，不冒complete。

wrapper只保一个完整计划行，已启动但未完与未启动为原null/phase，无自填科学值。原 `original_stop`、`science_argv`、`genuine_next_recipe` 和reader GITHUB_OUTPUT三键协议逐字保留。stdout prefix另标当前producer，最终report为 `BEGIN_VISIBLE142_CHAIN_SUMMARY` / `END_VISIBLE142_CHAIN_SUMMARY`。

## 9. 本地所做和后续实际判断

本地只做source/JSON/字节/AST和Bash语法。三新Python AST、8个shell块、5个inline Python语法与50项源/metadata关系通过；没有导入科学模型、没有新dot/norm/J/FD/Arb/QR、没有fixture或数值运行。

独立目录 `/tmp/visible-nine-directional142/` 含相对138的五个完整diff及source-only静态回执。它们供root直接读差异，不构成额外数学审批或执行门。R310 helper、R299 helper和0865 family原字节未改；93+5中原90+4逐项一致。

实际结果需要回答的是：在同一九族原方程下，新完整response/direct action是否改变真实方向和实际外接受；如果成立，原merit下降是多少、normal修正与半径如何演化。如果probe或方向失败，读真实失败阶段和已做工作；如果还是小步或下降很慢，直接响应内部的强消去、原normal轴列形成、近似曲线导数和非线性几何仍各自未被证明解决。不能仅因新K与pilot不同就宣称导数更准，也不能仅因原FD整列相对误差小就认证弱切向动作。先付这一真实八方向批，再决定下一独立改动。
