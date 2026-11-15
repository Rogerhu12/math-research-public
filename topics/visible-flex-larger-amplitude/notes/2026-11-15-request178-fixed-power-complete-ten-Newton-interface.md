# Request178：固定支撑1/k4、完整十维联合Newton的可执行接口

作者：ChatGPT（/root/amplitude）；2026-11-15。此文件说明冻结源码、真实参数来源与唯一请求接线，不预填未来 run 或科学结果。所有数值方向、模型求值、FD、Arb和圆检查只在本仓公开 Actions 执行；本地仅源文本、JSON、SHA、AST/YAML/Bash语法操作。

## 1. 本次实际改变与不变责任

本请求从 actual157 的真实末九个 Decimal50 参数词重新构造原有限模型，添加独立 ξ=0；固定 [R373](../results/R373-actual164-r3-six-shapes-and-twenty-full-merit-rejections.md) 实际所选 catalogue index3，即 support index1、power4。函数仍为冻结0924族原函数，未重新运行六候选选择，也未把164已经清理的 J、状态或参数文件作为输入。

本次改变的是方向机制：允许十个坐标联合变化，完整 fresh3×10响应形成固定物理尺度的最小范数Newton方向，径向clip后按原真实full3门试探；只有记录到Newton算术失败或其实际形成的斜率不严格为负，才使用完整缩放Cauchy回退。不是只改变ξ的再次回溯，不是延长相同微步批数，也不借174的602站形状或其方向替换本形状。

选择依据是R373和[R376](../results/R376-actual174-all-station-odd-signsum-and-twenty-full-merit-rejections.md)的真实单形状/单ξ全3拒绝。它们不证明联合Newton一定接受。条件线性代数、严格下降与有限余项边界完整见已发表 [R378](../results/R378-fixed-shape-ten-coordinate-minimum-norm-Newton-and-Cauchy-descent.md)。

完整三残差、原未加权merit、原strict slope、20档真实Armijo、原有限primal域、初末全部120列FD、160bit/14depth scalar Arb、完整453圆与112终端责任保留。没有形状独立→响应补秩推断，没有奇异值阈值/拟合精度/伴随一致性新增科学门。原高模Schur、当前非线性native、完整非零场和相应final audit仍未由此入口完成。

## 2. 原父点与独立参数

唯一当前初始父为 actual157：

- run `43729310294`；source `c71cbeac7fd13c65cf50c7eb39842e9949737b25`。
- status51842612 B / `931b013b6cfaba4215065e0734c129ba2089662273427f7ebecc5df4f35ee2b0`。
- 原summary89063 B / `7411fd01db054215e5d22293f6a4c239aa482302bf75b4da123f35d500d0cad2`；chain29684 B / `9d8bf161d9b88c0c411d326b1717fd2d32332a49534041ebd495b673a35652bd`。
- 九参数的50位十进制原字符串逐字保存在8891 B配方；追加 ξ 字符串 `0`。没有把有限旧值重新标成已证明的高精度精确值。
- 父relative radius `0.0000390625` 仅provenance，不作为本次trust radius。

固定形状的独立证据为actual164r3/run43743904448/source257b227a49034faaf1979bfe093122e7d06e1785，原status565694 B/0f9c86d1…、summary89762 B/33ca4bc6…。完整tuple在recipe和producer的 `FIXED_SHAPE` 同时绑定；只消费该已公布的形状选择事实，当前所有方向重新形成。没有future174/178父。

本版producer严格支持这一个真实actual157初始配方。若178实际接受后继续，须将真实输出词、来源与所选尺度责任显式接入后续入口/配方；不能将本版硬锁误当任意own-schema恢复器，也不能仅改标签而声称消费了已清理的状态。8方向是本次有限预算，不是研究完成标准。

## 3. 物理尺度、Π、Q与实际方向

设完整原三残差为 $F\in\mathbb R^3$，完整当前响应 $J\in\mathbb R^{3\times10}$。本次物理尺度在开头一次形成：

$$
S_j=0.01\max(1,|p_{157,j}|),\quad j=1,\ldots,9,
\qquad S_{10}=0.01.
$$

0.01在源中由明确十进制字符串形成，尺度以后不随接受点重置。设 $A=J\operatorname{diag}(S)$，缩放trust radius为1。这个参数度量不重加权任何残差行，也不改变目标函数。

复用冻结433d源的完整 column-pivoted Householder `qr_factor(A.T)`；输入10×3，返回完整Q10×10、R10×3和三个原方程的pivot索引。约定是：

$$
A^T\Pi=Q_{[:,0:3]}R_{[0:3,:]},
\qquad \Pi e_j=e_{\mathrm{pivot}[j]}.
$$

原factor逐reflector执行 `Q <- Q*H`，返回Q，不返回转置Q。实际以正向代入解下三角式
$R^T y=-F[\mathrm{pivot}]$，随后 $z_N=Q_{[:,0:3]}y$。没有把pivot反置，没有沿九/十个物理列误用三方程排列，没有形成正规矩阵。

准确满行秩条件下，这是使 $Az=-F$ 的最小Euclidean范数z，等价于最小 $\|S^{-1}d\|$ 的完整Newton物理方向。实际执行使用50位有限Q/R，保存而不掩盖：

- 完整Q/R、pivot、三个对角词、置换RHS和三角解；
- 原三角残差 $R^Ty+F[\mathrm{pivot}]$；
- 未clip的完整原残差 $Az_N+F$；
- 实际未clip范数、$\theta=\min(1,1/\|z_N\|)$及clip后残差 $A(\theta z_N)+\theta F$；
- 完整十个物理分量 $d=S(\theta z_N)$、原 $Jd$ 三分量、实际 $F^T(Jd)$及完整线性预测merit。

只有重新形成的完整有限方向/action/slope均finite且原slope<0才进入原真实trial。没有以精确QR恒等式替代形成的残差，也不把50位clip范数变成区间半径证书。

若所需R对角实际为0、QR/三角解算术失败，或完整Newton提案无严格负的原形成斜率，记录完整原因后形成全十列Cauchy：

$$
g=A^TF,\quad
\tau=\min\left(1/\|g\|,\|g\|^2/\|Ag\|^2\right),\quad
d=-\tau Sg.
$$

其完整g10、Ag3、分子、分母、boundary length、实际τ、方向和原slope都保存。准确 $g\ne0$ 时 $Ag\ne0$ 的条件证明见R378。若有限形成的分母为0，源码明确用boundary长度作为有限提案并标注该分支；仍须原finite strict slope，不能借此宣称准确秩亏。若无finite非零形成g或Cauchy算术失败/非负slope，则真实停止并保全部失败，不推出准确驻点。

Newton已通过strict slope但其20档全被拒时，本次不偷偷追加第二套20档Cauchy试探、不在同点机械重试。下一策略须依据原结果另行明确。

## 4. 原full3回溯及状态所有权

每个outer开始由真实持久状态取p10、F3、W；第0方向使用刚完成initial十轴description中的fresh3×10；后续每方向都从当前接受点重新调用完整十列forward。原forward的primal词比较仅保存，不将它覆盖owner的真实primal状态或增加精度门。

原20档 $\alpha=2^{-j}$、$j=0,\ldots,19$，真实试探沿直线 $p+\alpha d$。没有normal弯曲修正，因而不会把ambient线性模型误称为曲线路径模型。每档都用原独立十模型重新evaluate，所有旧九及新ξ可变化；完整112右残差仍形成。

原接受式不变：

$$
W(p+\alpha d)\le W(p)+c_A\alpha F^TJd,
\quad W=\tfrac12\sum_{i=1}^3F_i^2,
$$

其中 $c_A$ 是原binary64 0.2准确lift
`0.200000000000000011102230246251565404236316680908203125`，
不是替换成数学1/5。实际非finite/原primal-domain异常和完整merit拒绝分别记录，不能以只改善第一残差接受。

接受后只有该真实candidate成为state，记录完整十词和本档α；后续形成全部新响应。原unit tolerance触达会结束outer并仍执行原全部final；没有strict方向或整20拒绝则停止，未启动outer和未访trial后缀明确保存。最多8方向，最多每方向20实际trial；预算没有保证接受次数，也没有成功预填。

## 5. 完整模型/终态边界

重用的两冻结数值源：

| 作用 | 源 | SHA256 |
|---|---|---|
| 原九族+一支撑power的完整十族 | geometry_20261115_adjoint_selected_ten_control_family.py | `09240b33b82be3f595e82df05d93b309baefd6eeb74f1c34ba3a095cb2548016` |
| 独立十坐标Decimal50字面链 | geometry_20261115_adjoint_selected_ten_decimal_model.py | `8cb8352b76be0770ab565de3b24907faa302a86a75660b9f5ffaa9a23cc6a9b7` |
| 完整Householder QR arithmetic | geometry_20261115_nine_control_decimal_curved_search.py | `433d5ddd2587efa581fb28ea151ddf3cec5b6a63eb5017340375d1f19b6d98d0` |

433d的旧curved-search main不执行，只调用完整qr_factor。原41源祖先仍为setup/原方程/字面binding服务；旧157 Hessian与residual-quadratic优化器不执行，second-variation模块仅被原binding/schema来源链保留，没有额外Hessian调用。

原old9 literal binding准确保 `cc10a080eafa19e282ca22cefa62af57dadaf0ab19e54b0a4e6f7e7188ec32d3`。比较沿已实际修好的 `k.encoded(actual)==k.encoded(expected)` 完整规范JSON字节，不退回Decimal-vs-string普通dict误比较。四个输入与十个原数组descriptor仍逐一绑定。

699节点/698cell/七状态/完整112固定尾J/原终端形成均保留；没有静默删除高109行，亦没有高模Schur或当前native完成声明。新十族所有旧p FD、搜索、最后scalar/圆评价都使用同一个固定support1/k4函数，不重选形状。

producer从 `final-full-ten-forward-FD-and-original-projection-final-consumers` 到诊断完成的完整源码块与冻结164r2原块逐字相同：

- initial/final Decimal十轴×原3档，共60列；initial/final binary64投影十轴×3档，再60列；每列失败/异常按原源完整保存。
- 最后重新完整forward、原112右残差及三单位残差标志，不借初值报告。
- binary64投影明确记录所有持久词/hex/投影差，不采用投影替换Decimal owner。
- scalar_spec/新族Arb160bit、depth14；原453维圆的node/mid/RMS/FFT与原3active/112tail责任。
- 原任一最终消费者实际失败、资源未付、规则退出均原样区分。数学C²局部零jet不冒原返回a/ap准确兼容、完整Frenet连续域或字面roundoff外包。
- `native_nonlinear_solver_called=false`、`nonzero_field_completed=false`、总 `success=false` 保诊断范围；原unit/full112 flags分别以真正末状态计算。即使低三达标，也不能因此假造已接受非零native父。

## 6. 45源闭包与唯一配方/请求

当前producer闭包是原41加四件：既有0924family、8cb8model、新scaled-Newton search、新producer；共45。相对164r3，R351伴随不再被本入口调用，不进入当前闭包；新source身份完整入ledger，不能冒旧单ξproducer。

workflow源表112个=原157的107个不变基线加family/model/search/producer/wrapper五件；支持表10个=原9个历史读回/规则基线加本reader。这里大量旧脚本只作固定来源闭包或原source恢复；本workflow不执行它们的历史科学入口。当前闭包每项必须出现在全源表并逐SHA匹配。

四输入仍从历史公开commit
`8bd267107cc8710d371f3b62c02986655ac965b0`
临时恢复：accepted b4d2b98a…、prepared 0f94dd88…、tail_anchor e788a28d…、config01930f3b…。不把已从main删掉的可重算数据重新保存到main/Release。

本次冻结文件：

| 角色 | basename | bytes | SHA256 |
|---|---|---:|---|
| search | geometry_20261115_fixed_power_ten_scaled_newton.py | 15144 | `6b55a6d223f0103bb0396a578d89cfd06c6b4888d38dbb4d518eaa3ecb6f2861` |
| producer | geometry_20261115_fixed_power_ten_joint_newton_recipe.py | 30304 | `3e5c8a34f5043fac35addf09627e16e59dcfc7287bb7ec087805be5dcac1474e` |
| reader | root_20261115_fixed_power_ten_joint_newton_scalar_readout.py | 38363 | `0610bc3ff66494370018df8c8cd5cb04371fe33c1e48b7160033cbf4e951221a` |
| wrapper | geometry_20261115_fixed_power_ten_joint_newton_temporary.py | 19273 | `9bb076c098115d701804cfbdf32cb4c1af0689c5e060e6e9dc55a0b2646ee224` |
| recipe | fixed-power-ten-joint-newton-actual157-parameters.json | 8891 | `c8bb1ca8dfbd745845fab11e421ca9189bfdd20af101931c5ddb7a4ab8cd37a7` |
| request | public-fixed-power-ten-joint-newton-request.json | 44351 | `f7b24f5754b4461b5d2fc0a93ccd044e1699932f0a4e7dd4e420b21ae3edb438` |
| workflow | visible-larger-public-fixed-power-ten-joint-newton.yml | 22327 | `799e0b79be2d3c7f4de3e34c57cb7b6712bfdaa885bdcacf7f5bb873491141f3` |

其中workflow正式路径为 `.github/workflows/visible-larger-public-fixed-power-ten-joint-newton.yml`；其余运行件在 `topics/visible-flex-larger-amplitude/computations/`；本接口在notes。对应科学schema `R259-fixed-power-ten-scaled-minimum-norm-Newton-full3-v1`，status `fixed-power-ten-joint-newton-status.json`；wrapper schema `request178-one-fixed-power-ten-joint-Newton-temporary-experiment-v1`，reader schema `request178-fixed-power-complete-ten-Newton-compact-readback-v1`。

唯一push触发路径是 `topics/visible-flex-larger-amplitude/computations/public-fixed-power-ten-joint-newton-request.json`，不改164/174旧workflow或请求。当前无未来run/artifact数字。recipe原字节8891、SHA c8bb1ca8…，workflow字面长度与pin由实际最终文本生成，避免旧常数残留。

## 7. 原公开Actions执行/清理

Python3.12.14、numpy2.3.5、SciPy1.17.0、python-flint0.9.0；BLAS/OMP/MKL均1线程。checkout/setup-python保持原固定action commit。git关闭自动gc/maintenance，并设置 `merge.stat false`；仅临时原输入Git对象缓存，没有历史rewrite。

原78公开源码恢复保持完整原机制，路径为request独占RUNNER_TEMP目录。原3b8规则runner同进程组执行，2700秒真实pull/rebase/README差异检查；只把已读reviewed root/topic21bd547f…/bff8aea…原全文作为本次baseline，不改runner源码或规则。HANDOFF唯一规则行与大小界限仍原检查。

实际科学命令由wrapper形成：

```text
python -u geometry_20261115_fixed_power_ten_joint_newton_recipe.py
  --accepted <原完整输入> --prepared <原完整输入>
  --tail-anchor <原完整输入> --tail-config <原完整配置>
  --parameter-recipe <8891字节本次配方>
  --parameter-recipe-sha256 c8bb1ca8dfbd745845fab11e421ca9189bfdd20af101931c5ddb7a4ab8cd37a7
  --out <request-owned/science> --directions 8 --backtracks 20
  --decimal-digits 50 --interval-bits 160 --interval-depth 14
  --wall-seconds 2400
```

producer墙钟2400秒；whole-child同2400秒，SIGTERM给予原checkpoint、grace90秒后才kill。whole-child包括import/setup/final；producer自己的checkpoint钟在身份/setup前置后启动，二者范围分别明示。metadata reader300秒、grace30秒；科学step50分钟、整个compute65分钟、report10分钟。保原资源合同，不把墙钟耗尽解释为数学拒绝或无下降。

原source/输入检查与fresh输出目录检查仍在数值执行之前；任何startup缺项都应由always读回保错误原文。科学完成/partial后先原status→reader，再完整producer/reader stderr与失败stdout，最后只清理request-owned科学树、四输入和78源码缓存。错误文本采用已付的双层ASCII+原字节范围，不用于搬运科学大数组。空/非UTF8/长单行错误仍可准确回读，不能只SHA后删除错误。

没有artifact/Release/raw上传，没有新Git数据；临时数据只能在当前job消费完后清理。report仅转发compute的单份compact与准确SHA，不运行或恢复科学。

## 8. 单份科学读回：完整标量与明确未搬范围

新reader是纯stdlib元数据程序，不import数值源。完整原status在Actions内读取，检查branch已有实际矩阵/向量shape；没有重算norm、J、FD、slope、merit、rank或间隔。正常单摘要ASCII hard bound **90000 B**；没有未来未实测的大小保证。reader与wrapper均实际检查最终大小；超限输出明确小错误摘要+section字节/原身份，返回工程失败，不截trial、不拆大科学数据、不冒complete。

保留：

1. 全部8计划outer，实际每个stop/accept/α/accepted词、未启动outer与每个已启动方向未访trial列表。
2. 每个实际方向的完整F3、W、十个d、三项Jd、原strict slope；真实selected kind、Newtonclip/三角与原模型三残差、Cauchy原分子/分母/长度和完整失败异常。每个完整Q/R及原方向模型有canonical身份。
3. 全部实际trial用公开列名加行表，列为direction/trial/α/accepted/actual_merit/actual_unit_equations/original_Armijo_bound/原有限域flag/reason。每个实际异常保完整原文，不重复每行slope或完整十参数/112向量；这些原完整表在Actions读取并保whole-trial身份。
4. 最后一个实际方向的完整J3×10与A3×10、固定S10、Q实际前三列、R实际前三行、完整原解/残差及失败。其余7个Q列以及更早大factor/112表只身份；条件最小范数证明不要求伪称下游逐值看了这些大表。
5. initial/final完整3×10和投影J、原三残差/112前三行/完整112身份、原FD12 level/120列覆盖、所有真实FD失败/异常，以及原域/453圆/终flags。
6. 全部source/recipe/input/status/ledger/规则来源与wrapper实际结果。相同初末值只能在**实际完整规范字节比较相同且无异常、全部FD已处理之后**以明确同摘要pointer/reference代替重复；不等值一律保留。本规则沿174已实际付的机制，当前178不预假定初末相同。

canonical身份是JSON/字节事实，不是准确科学值证书。metadata complete不表示任何数学final已通过；同样，readback超限或缺项不是科学拒绝。所有未来实际成功/失败依原单摘要与错误行记录。

## 9. 完整差异与静态范围

已交两件科学差异：新增search全文，以及producer相对164r2的完整diff，47546 B / `d08b935373d2f7ce6c88952613cb32a101d6831c53331fc641c910ffb622c7ed`。reader/wrapper/recipe/request/workflow相对164r3（recipe原7483文本）完整五diff合计94501 B / `a4a807e0ff5de505b7b6cf931f4df1ccef18d777d83f011a01b43e3dcb238aa8`。没有用笼统“数学不变”覆盖新方向差异。

恢复的本地终端只对4个新Python做 `ast.parse`、YAML解析、9个shell块 `bash -n` 与6个inline Python AST；未import/编译执行任何科学模块，未构造数值fixture。源码内POLICY/CONTRACT/fixedshape、41/45闭包与7件当前字节pin、最终recipe长度8891全部静态对齐。原最终消费者块对164r2逐字相同；全部112旧来源文件未在本地重新下载/哈希，不冒新全source审计。Actions仍按原工作流真实核全部112+10字节。

临时交付目录 `/tmp/visible-fixed-power-ten178/`，所有正式文本均小于100KB并可用独立Git blob保全；root是唯一commit/ref/dispatch负责人。这些语法/元数据检查不是新的数学验收门。
