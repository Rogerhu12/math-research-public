# 从实际115四控制末点续接116：同源码、显式半径重置

类型：实际原读数与可执行接口。作者：exact_refinement。日期：2026-11-15。

## 1. 本次执行什么

116从实际115的四个末参数重新评价同一四控制模型，再执行一个原八方向批次。科学 family、search、reader 三份源码不变；完整三方程、7×4正阻尼QR、两维 normal 校正、两维 tangent、原未加权 merit、`.2` Armijo、原域及全部最终检查不变。这里只更换真实参数 recipe、请求号、来源绑定及工作流说明。

**信赖半径明确重置为0.1。** 实际115保存的末半径是0.0125；冻结入口 `main` 强制 `--initial-relative-radius 0.1`，且短 recipe 只保存参数与来源，不承载信赖算法状态。因此116不是在原进程内继续第九方向，也不声称恢复了0.0125。该初始化变化在 request 的 `trust_radius_restart` 和执行日志中单列；不修改已冻结入口来绕过其要求。

本次不执行 native、不构造非零幅场、不开始 full-DN，不把小核搜索点称为已接受的完整场。115八个方向实际全部接受，足以支持继续同一明确算法的一次尝试；它并不保证116继续下降或最终达到共振条件。

## 2. 实际115来源及全部外试探

来源为[实际115公开Actions](https://github.com/Rogerhu12/math-research-public/actions/runs/43689328906)，触发源码 `c9eb007df84297f5345d0e7fab42b845df0bf912`。主控已读出的原完整短摘要为69,434字节，SHA256为 `282c363f6a1c518d3e37ca4cdca78cdc0c741e9c079ab6cb3331352a2279b2b1`，口径不含日志分隔换行。原临时 `four-control-curved-status.json` 为1,069,255字节，SHA256为 `b542147b089985e5ce0e90623d32b4fd4eabf77e2fea07c1d50914c1cb7d2696`；按规则15不另保存该可重算原件。

下表全部数值直接抄自该摘要，没有在本地重算 merit、导数、范数、差值或比例。

| 方向 | 实际外试探α，按顺序 | 接受α | 接受后原W | 下一半径 |
|---:|---|---:|---:|---:|
| 0 | 1 | 1 | 5883.214943282955 | 0.2 |
| 1 | 1 | 1 | 3370.2619959119575 | 0.4 |
| 2 | 1，1/2 | 1/2 | 1350.5772213810976 | 0.2 |
| 3 | 1，1/2，1/4 | 1/4 | 1282.3514920878781 | 0.1 |
| 4 | 1，1/2 | 1/2 | 1253.7265270235346 | 0.05 |
| 5 | 1，1/2 | 1/2 | 1242.0218709138594 | 0.025 |
| 6 | 1，1/2 | 1/2 | 1238.1089135124219 | 0.0125 |
| 7 | 1 | 1 | 1236.0078724708558 | 0.0125 |

实际初W为6958.22576276662，停止原因是 `explicit total direction budget completed, counting accepted and rejected directions`。14个外试探均记录返回点；没有全20拒绝的方向。原评价记录有627次尝试、613次返回、14次异常及92次完整J返回；14次异常集中在方向3的α=1内层原 node/mid scalar 域检查，不是14个外试探均异常。该外试探保留最后有限候选后按原完整三方程条件拒绝。

方向3最终α=1/4接受时，实际 normal target error 为 `[5.37443822085093e-11, 2.2759042179879615e-08]`，内层 `tol=false`。因此实际执行确实没有把内层1e−8变成外层新门。方向7α=1的原W为1236.0078724708558，原Armijo界为1237.2429806376065，内层误差 `[8.953263824773572e-11, -9.324725176414802e-09]`。

115末四参数为：

```json
[0.43415584380328803, 0.1757884505633052, 0.573987809246338, 0.03007332272935495]
```

末原单位方程为 `[-49.71935400957918, -0.03977199754487137, -8.125719463311133e-06]`；完整112右行的前三项为 `[-22.965735025212034, 0.0023741700030656824, -1.2781802727164869e-07]`，其余109项保存为−0。原单位停止、完整112候选、非零幅场、native标志全部仍为false。高109消去与非共振未由115支付。

完整3×4的初奇异值为 `[345349560.07360065, 439358.39688958373, 83.72860814512897]`；初前三列为 `[344085694.6146413, 430002.42443254485, 9.800236811437901e-05]`。完整3×4的末奇异值为 `[233550527.85554808, 320897.86799005524, 6.40795078841513]`；末前三列为 `[233540375.779129, 320726.1179390794, 5.331001439612569]`。

原实差分步长 `2e-5、1e-5、5e-6` 在初末都覆盖四列且 `valid=true`，初最大相对误差依次为 `7.604888749352694e-09`、`1.9135175596157784e-09`、`4.671911468013092e-10`；末依次为 `5.96058093387618e-09`、`1.4981256973518257e-09`、`4.090722506312614e-10`。初末SVD/FD都是普通浮点数值读回，不是区间横截性或确切秩证明；实际接受仍按原full3门，而当前unit阈值尚未通过。

115新标量实表达式域报告843个叶、0未决；它明确不包含字面binary64舍入包络，也不证明返回 `ap` 等于有限Gauss `a` 的导数。实际θ冻结平方 circle 视图完整有限，原物理配点最大缺陷 `4.3237982638721917e-16`；它仍是零core reference，不能作非零场父件。θ冻结后不同加法顺序的实际scalar node差为 `5.551115123125783e-17`，源未声称逐位同路。

## 3. 116短recipe及22→22来源

新文件 `actual115-explicit-four-control-parameter-recipe.json` 为1,507字节，SHA256为 `3cab39d56ecdd754689266a2b87c20b2a58d5268df426766446b698dc1a4ce1d`。schema仍为 `R259-explicit-four-control-odd-shape-recipe-v1`，五个顶层键完整保留：`schema/origin/literal_parameters/input_sha256/family`。

`origin.producer_file` 现在是当前冻结四控制入口，`origin.producer_schema` 为 `R259-four-control-full-three-two-normal-curved-trust-recipe-v1`，source SHA为 `3ca1bdf723e7c44f808ed786ccda854775c262d28ce92804fde2c8ca86cad160`。原115 run/source/status/summary身份完整列入recipe。它是公开原摘要中四个字面参数的可追溯转录；不是伪造的父status，也不需要恢复已按规则15删除的原status。

冻结入口 `recipe_input` 已有 `origin.producer_file == ENTRY` 分支：该分支以当前 `sources` 完整22项作为origin closure。故116是 **origin22/current22**；115最初从114接入的origin18仅属过去来源，不继续冒作116父闭包。本地核对了115摘要的 `consumed_source_sha256` 与request当前22项完整一致。该核是原字符串/字节身份比较，没有科学运算。

主request保留原79项主来源和2项工作流支持pin；其中科学两源及reader为：

| 角色 | 文件 | 字节 | SHA256 |
|---|---|---:|---|
| 同一新scalar family | `geometry_20261115_small_core_four_control_family.py` | 36157 | `9222390b73abbd2e8bc4a1f8e9d8b861cd66b4a927b21629deb2e6b70073dd11` |
| 同一search入口 | `geometry_20261115_small_core_four_control_curved_recipe.py` | 51709 | `3ca1bdf723e7c44f808ed786ccda854775c262d28ce92804fde2c8ca86cad160` |
| 同一只读摘要器 | `root_20261115_small_core_four_control_curved_scalar_readout.py` | 18169 | `c0602e7ac54dd9bafefbedf7d0f52abf0b77324769be0cd9d29970c249e0269d` |

reader的版本schema仍含 `request115` 前缀，因为源码保持不动；实际 `run_id/source_commit` 来自116运行环境，report标记改为 `BEGIN_VISIBLE116_SCALAR_SUMMARY`。该版本标签不表示重新读取115输出。

## 4. 输入、执行与原门

四数学输入不变：accepted `b4d2b98a…`、prepared `0f94dd88…`、真实112零尾J anchor `e788a28d…`、tail config `01930f3b…`，完整路径、字节与SHA列在request。缺失时从已固定历史commit `8bd267107cc8710d371f3b62c02986655ac965b0` 恢复原文件，不读取另一次运行的替代值。真实尾J全部112×112项仍由原模型使用；原ready linear graph没有替代它。

CLI仍是冻结入口，四原输入加新recipe及其SHA；参数原样：

```text
--initial-relative-radius 0.1
--candidate-steps 8 --backtracks 20
--normal-iterations 12 --normal-backtracks 20
--normal-target-tolerance 1e-8
--candidate-resonance-tolerance 1e-8
--interval-bits 160 --interval-depth 14
--out <new-temporary-root>/small-core-four-control-curved
```

每次重新评价四控制点、全3×4响应与四列实FD；每次实际接受后原模型重新形成J。保原完整三行未加权W、当前真实 `rᵀJv`、`.2` Armijo及全部scalar/node/mid域责任。12×20 normal计算努力保持原1e−8内部停止值，未达点仍只由实际外层全三条件决定；绝不把目标二行覆盖成零。

α=0为原点且无normal修正；α>0时使用完整四坐标 `q=p+αv+SNw`，目标 `c(p)+α(Jv)[1:]`。非法直接seed仍结束该α，本次未添加曲线细分。原正阻尼7×4QR保全部四列，无SVD截秩、normal matrix或J33除法。半径限制预测坐标，不假称校正后实际非线性位移必在该球内。

原8个方向预算同时计接受与全拒方向，20个α保留；最大160外试探、38,560个直接seed与内层试探评价、1,920次内层完整J调用的既有上界不变，且不含J内部complex steps与最终检查。科学step75分钟、compute90分钟、report10分钟；超时是资源中断，不是不存在根或原回溯全拒。

## 5. 工作流与规则15

继续同一独立路径 `.github/workflows/visible-larger-public-small-core-four-control.yml`，同一触发 `computations/public-small-core-four-control-request.json`，`request_number=116`。同一concurrency且不取消既有运行。未创建第二科学lane，也未重跑115原状态。

Python3.12.14、NumPy2.3.5、SciPy1.17.0、python-flint0.9.0、BLAS1、原checkout/setup pins、公开78源恢复、关闭gc/maintenance、`merge.stat false`均保留。原规则runner `3b8b6dd5…` 在独立镜像执行初始及每2700秒真实pull/rebase并更新唯一H规则行；双README固定已读blob为根 `74c08a36…`、题 `bff8aea2…`，变更按原规则停止并输出差异。科学checkout不被该同步改变。

只在compute临时目录产生完整原状态与事件，再由同一reader输出≤90,000字节的原scalar摘要，经 `GITHUB_OUTPUT` 交独立report。report核完整输出字节数/SHA后打印116标记。超限走原诚实fallback，不能把缺完整状态当成功。原每外试探stdout仍保；没有artifact、Release、旧publisher或raw入Git，临时科学目录在读出后删除。只公开脚本、recipe、request、run/输出SHA与紧凑结论。

## 6. 与未来完整场接口的界限

本次继续四控制搜索，没有把它直接当平方边值问题。`ThetaFrozenProfile` 当前只在最终零core circle读出固定实际θ、保三active p/三core targets/全部112右行；它不把尚未满足的低三共振或非零native任务变为已付。

全3×4满行秩不自动保证固定θ后的前三列可用。未来若需选择另一个非零3×3 minor，可以固定其余一个设计坐标并保三active坐标，但必须新建明确的参数顺序、冻结值与scalar/profile身份；不得静默改当前115冻结θ视图。当前115前三列和完整四列数值都已按原读出保存，116仍执行同一四控制策略，尚未选择另一个三参数图。

完整非零λ分支仍须当前family下的高109责任、完整112原边界及新实际H的native/full-DN/finalJ/audit；旧81在旧78参数的高块结果不能跨当前p/θ继承。有限低三阈值、当前circle有限、全区间scalar域结果均不自动完成这些责任。

## 7. 冻结与本地范围

三个执行小件：recipe SHA `3cab39d5…`；request31,136字节/SHA `45cd4dd96234893f968b35cdb39b4aad805c4b55a26eb2168ccd092bc4325175`；workflow16,329字节/SHA `9cabbd3c7179656674910516b31da12d2387988099f0fe10e08cb19dcfcbfaf2`。完整源pins均在request，来源定义与实际115一致。

本地只读115原JSON、核字面/IEEE参数转录与SHA、解析元数据、编译AST及执行 `bash -n`。三个原family/search/reader文件逐字SHA复核；79+2 pin映射与实际成功115完全相同，未声称本次本地重读了81个全部payload。Actions仍完整核81个实际文件。

8个shell block与5个inline Python block已静态通过；没有科学模块import、模型构造、RHS/J/ODE/矩阵或范数执行，没有Git mutation、下载或dispatch。两个diff、builder、静态回执只作临时可重得材料，不作为新的数学门，也不入库保存可重算结果。
