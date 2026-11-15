# 108：从实际 106 短 recipe 转入完整三参数正阻尼信赖方向

类型：算法实现与运行接口；作者：exact_refinement；日期：2026-11-15。

## 1. 实际起点与范围

实际 106 为 run `43682474213`、source `500fb2acf7a005f928b217412647b445899a48aa`。根已取得其独立 report job 的原短摘要：20,624 B，SHA256 `f022add6da826a5d54a0f3e0863393a7fd54e8fcecfd87065efba784b94a6b0c`。13 批中的前 12 批因八步预算停止；最后一批的原 20 次回溯全拒绝，参数未再改变。这里没有从时间、job 颜色或先前批次推定求根成功。

原末参数为：

```json
[0.46303192429838314,-0.1928229026382781,0.6316434990702386]
```

原末 full3 merit 为 `6958.2257628163525`，原三个 unit 值为 `[-117.96801026297652,0.008956951016303328,1.2620775966464774e-9]`。unit、完整 112 行候选标志和 native 完成均未通过。原末报告的三个奇异值为 `[344085545.0083041,430001.95976659097,0.0011209130688844945]`，condition 为 `306968983197.53705`。这些原数值不证明局部极小，也不证明浮点分辨率已构成无法逾越的下界；原相对有限差分检查亦不等于弱奇方向的误差外包。

108 是已授权的新方向策略：完整三个参数一同进入正阻尼信赖模型、直接进行原非线性回溯；不再执行 p3 内层恢复或除以 J33。它不是仅将先前固定 eta 改名，也不将旧 p3 恢复后的失败方向原样重跑。未执行任何本地科学计算；最终结果只能来自后续公开 Actions。

## 2. 完整原方程与新方向

令当前真实返回的三个 unit 方程为 r(p)，J 为同一当前点的原完整 3×3 参数 Jacobian。每次当前点和 J 均由冻结原 CircleReference 重算；初始 recipe 只提供参数，不提供可复用的旧 J、旧 merit 或旧状态。

采用明确的参数尺度：

```
S_j = max(1, |p_j|), d = S z, A = J S,
||z||_2 <= Delta, Delta_initial = 0.1, Delta_max = 1.
```

这是参数空间的算法尺度，不对三个原残差重新加权。每个方向解同一个完整线性模型：

```
min_z ||A z + r||_2^2 + mu^2 ||z||_2^2,  mu > 0.
```

代码字段 `positive_damping_mu` 指增广矩阵的对角系数；`objective_penalty_coefficient_mu_squared` 指目标中的惩罚系数。两者分别保存，不能将 mu 和 mu² 混为一物。

形成完整 6×3 矩阵 `[A; mu I]` 与六维右端 `[-r;0]`，调用 SciPy 的列主元 Householder QR（economic），再对全部 3×3 上三角 R 作完整三角解，并还原三个列置换。没有 normal matrix、Riccati、lstsq 默认 rcond 或 SVD 截秩。SVD 仅仍存在于原最终 description 的诊断；不用于新方向截断任何列。若实际 R 非有限或对角为零，记录明确方向模型失败，保已接受点；不静默丢弃弱列。

精确算术下，正 mu 给出：

```
z^T (A^T A + mu^2 I) z = ||A z||^2 + mu^2 ||z||^2 > 0  (z != 0).
```

故该完整增广问题唯一。其精确驻点满足 `r^T Jd = -||A z||^2 - mu^2||z||^2`；实际二进制64解仍独立计算原 `r^T Jd`。仅有限且严格负的实际斜率进入原 Armijo 回溯；不以理想恒等式覆盖实测斜率，也不将模型残差或条件数增添为原非线性验收门。

mu 的初始正下限是 `eps64 * max(1, ||A||_F)`。若该实解已在半径内，即保留；否则在同一固定 J/r 下最多 64 次增大上界，再最多 64 次几何区间细化，始终保留实际计算的半径内上界解。近边界条件为实测长度至少 `0.999 Delta`，或区间无法继续细分。正则化参数搜索不调用新非线性 evaluate，不是 eta 扫描试验。该有限迭代不声称精确求得信赖域最优乘子；若没有形成半径内有限完整解，诚实停止方向模型。

## 3. 原实际回溯、半径更新与停止

每个方向最多 20 个原比例 `alpha=2^-j, j=0..19`，直接形成 `p+alpha*d` 并调用原完整 evaluate。完整第三分量保持真实返回值，既不置零，也不再作 p3 恢复。

实际接受仍为原条件：

```
W(p_trial) = 0.5 * r(p_trial)^T r(p_trial),
W(p_trial) <= W(p) + 0.2 * alpha * (r(p)^T J(p)d),
```

并由原 evaluate 保持原标量/circle 域。每个实际 trial 保存 alpha、真实参数及二进制64位移、三个实际 unit 值、原 merit、原 Armijo 右端、接受布尔、拒因或原异常。计算 stdout 也逐条输出这些有界实测字段。没有新增只看下降率、线性 residual、condition 或模型 ratio 的接受条件。

只有真实接受以后才更新下轮半径。若 alpha<1，或实际/预测减少比小于 .25、无定义/非有限，半径减半；若该比值>.75 且实测 full step 长度至少 .8 Delta，半径至多加倍到 1；否则保持。预测减少来自未重新加权的 `r+alpha*Jd`。ratio 仅影响后继方向尺度，不拒绝已通过原 Armijo 的候选。

最多八个外层方向；可能明确停止于原 unit 阈值、八步预算、方向模型失败、实际非下降斜率、或完整二十次直接回溯耗尽。初始半径每次显式 recipe 运行重置为 .1；当前 schema 不声称跨 run 继承先前半径。

## 4. 原最终检查保持，原未完成项保持

初始和末点 description 仍调用原完整 J、原独立实参数有限差分及原全 112 行读出；scalar-domain 仍 160 bits、depth 14，circle 检查仍调用原完整函数。真正的原 112×112 零尾 J 全部消费，不能以 profile slope 冒充它。

以下两个原判据分别保留同一原阈值 `1e-8`，互不替换：

- 迭代早停：所有原 unit 方程的绝对值最大值不超过阈值。
- 末候选标志：完整 112 行 recorded right residual 的绝对值最大值不超过阈值。

原 3b9 的实际对角尾结构与非零低三 target 适用范围仍由原源保持。三个参数搜索改变设计参数，不据此宣称已经存在一个固定 metric 下的完整非零场。高 109 free-core 消元、区间横截性、非零 lambda 解、真实 native 和原完整 BVP/large-amplitude 完成都仍未由本入口支付。原 `success=False` 不被求根诊断完成的进程退出 0 覆盖。

## 5. recipe、完整来源与四输入

`actual106-explicit-parameter-recipe.json` 是实际 106 最末报告中的完整短 recipe：1,130 B，SHA256 `b60de33fc17d1b0df84b7e44f41710e25074fa3e8618964f3c3a920d58279fb9`。其旧 status 记 433,023 B / `ea8746ced258cbffb31f978d977614ab17f46a1202ebd51affb337beb636af9d`；批次摘要记 21,083 B / `1f5af4b0c58675040b1e58c7649555c1bec0db90cc5bb870f423f72d0cc56890`。这两个大对象已按规则不保存，本入口不声称再次读取它们。来源 tuple 与源闭包是追溯信息；参数由当前 recipe 的完整实际 bytes/SHA 绑定。

入口允许两种诚实来源：冻结 3169 recipe producer，或本新 producer 的精确 own schema/source。旧来源闭包 15 件；新实际 producer 闭包 16 件。二者不混淆。新源只导入旧 3169 中的原 source checker、原模型加载器和只读观察器/record helpers；旧 3169 main、Schur、p3 restoration 类均不调用。

四数学输入沿原路径、原 bytes 与完整 SHA：

| 输入 | bytes | SHA256 |
|---|---:|---|
| accepted | 2614352 | b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff |
| prepared | 4220043 | 0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714 |
| true T112 anchor | 6815 | e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51 |
| T112 config | 2161 | 01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5 |

当前 main 若已删除可重算原件，只在 Actions 用普通 public git show 从真实历史 `8bd267107cc8710d371f3b62c02986655ac965b0` 恢复，并逐完整 bytes/SHA 核对。原 78 数学文件仍经冻结 `prepare_public_source` 恢复，设置 `VISIBLE_SOURCE_TOPIC`，不新增私有源。

## 6. 新源与 CLI

| 新文件 | bytes | SHA256 |
|---|---:|---|
| geometry_20261115_small_core_full3_trust_recipe.py | 27258 | 5d3540150390f0e820200ba4a210eb2bc8d06bc025a0a677160df97d72e6f4c1 |
| root_20261115_small_core_trust_scalar_readout.py | 12547 | e5c3fd705228010593bffc406215c3c3e5fa3248295f3977bfd4cae21055b5b3 |

科学 CLI：

```bash
python -u geometry_20261115_small_core_full3_trust_recipe.py \
  --accepted "$ACCEPTED" --prepared "$PREPARED" \
  --tail-anchor "$TAIL_ANCHOR" --tail-config "$TAIL_CONFIG" \
  --parameter-recipe actual106-explicit-parameter-recipe.json \
  --parameter-recipe-sha256 b60de33fc17d1b0df84b7e44f41710e25074fa3e8618964f3c3a920d58279fb9 \
  --initial-relative-radius 0.1 --candidate-steps 8 --backtracks 20 \
  --candidate-resonance-tolerance 1e-8 --interval-bits 160 --interval-depth 14 \
  --out NEW_EMPTY_DIRECTORY
```

实际输出 status 为 `full3-trust-status.json`，schema `R259-original-full-three-parameter-positive-trust-recipe-v1`。完整 J/r、方向、正 mu/惩罚系数、完整增广 QR/置换、同线性模型阻尼搜索、每个实际非线性 trial、原最终读出和真实调用 ledger 暂存本 run。模型驻点读出属于普通浮点诊断，不是误差外包。

## 7. 独立工作流与当前存储规则

新路径：

- `.github/workflows/visible-larger-public-small-core-full3-trust.yml`
- `topics/visible-flex-larger-amplitude/computations/public-small-core-full3-trust-request.json`

仅该 request 的 main push 触发，独立 concurrency，不取消正在运行的同类科学。旧 74 主 pins 保留并增加新科学源，共 75；元数据支持额外 2 件（原 3b8 rules runner 与新短 reader）。Python 3.12.14、NumPy 2.3.5、SciPy 1.17.0、python-flint 0.9.0、BLAS 单线程保持。compute 上限 60 分钟，科学 step 45 分钟；这不是科学步数/回溯预算的替换。

原 rules runner 3b8 的代码、真实 pull/rebase、每 2700 秒同步与 README 改变则停科学的行为不修改。启动时仅将其内存中的旧 README baseline 显式改为本次已读实际 74c08a36 / bff8aea2 两文件完整 bytes，并重新核 Git blob。必须已有恰一条 H 规则同步记录且 H 不超过 10,000 B，不绕过。rules 镜像独立，科学 checkout 的触发 commit 不改变。setup 增加 `git config --global merge.stat false`，避免已删除大批可重算文件的 pull diffstat 干扰日志；gc/maintenance 仍关。

原科学 stdout 留 compute job；独立 readout 只读取原字段和文件 SHA，不做科学算术。将不超过 90,000 B 的 JSON 经 GITHUB_OUTPUT 传给独立 report job，根只需读取该小 job 的：

```
BEGIN_VISIBLE108_SCALAR_SUMMARY
<实际原标量 JSON>
END_VISIBLE108_SCALAR_SUMMARY
```

报告保每个外层的实际 J、方向、斜率/步长/mu、全部实际 trial 列表、原末 flags/参数/J/FD/scalar/circle、真实规则同步与 status/hash。可选重复因子/文件目录若超预算按明确 SHA 缩短；若仍超限，以诚实 metadata-over-budget 记录及原 status SHA 报告，不能由读出失败改称科学失败或成功。reader 的逐字文件哈希是元数据工作；短科学标量全部复制原报告，未另计算。

不执行旧 publisher，不 upload-artifact，不向 Git/Release 写可重算 raw。短读出交接完成后删除该运行自己目录中的临时科学输出；scripts、recipe、request、run/source、输出 SHA 与紧凑正式结论由主控按新规则记录。没有未来 run、状态或验收被预写。

## 8. 静态验证与交付边界

附 source/工作流差异和独立静态回执，验证新两 Python AST、工作流各 Bash 语法及其 Python heredoc AST、真实 recipe 字节、75+2/16+15 身份映射、完整 QR 三列和不调用旧 p3 的实际 AST。没有 import 新科学模块、执行模型/QR/FD/Arb、或构造任何新的求解数值；静态核不是额外科学接受门。主控拥有 Git 发布与 Actions 调度。

