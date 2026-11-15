# Request106：冻结求解器的有界短配方批次续接

类型：实现接口与已有数值来源记录；不是新数学结论或验收证书。
作者：ChatGPT / exact_refinement。日期：2026-11-15。

## 1. 实际起点与目标

首批从 actual105 的三个真实末参数出发：
`[0.4976392922339909, -0.2670862030502635, 0.5984780843750176]`。

实际105为 run `43680931993`、source `28b59a6f4ac64fdf1614773d9ca46aab8000ae9e`、
job `132711175414`。主控已读原状态835048 B /
`2f8ad3440983f11c33ba630856439a1637a5563bcb6caa786c449f679d631cb7`
及短日志摘要59328 B /
`73774bce7071455595bc339d56ba8fccfa1000787c1e48b1ba05b67cb4cd377e`。
原8步全部接受，前六次1/16、后二次1/8；原38次外试探有30次拒绝。
原merit从13116.490604299248到11845.748285989865；原停止原因为八步预算完成，
unit/full112/native标志仍未通过。这些是既有Actions原读数，不是在本地重新计算。
来源：[actual105 Actions](https://github.com/Rogerhu12/math-research-public/actions/runs/43680931993)。

短recipe明确是初猜参数和来源信息，不伪装成未保存的完整父status。
新的每一批都重新调用冻结3169入口，对当前三个参数重新evaluate、完整J、原FD和最终检查。
前一批的J、merit、场或FD不作为本批值复用。
跨批同参数重新评价可能有末位差；既有13116.490604299248与更早读数不能被强制覆盖成相同数值。

## 2. 固定算法与唯一续接条件

科学入口仍为
`geometry_20261115_small_core_inexact_p3_eta_0p01_recipe.py`，
47106 B / `3169b2d3ea821a244d9f27611cd6c5cb3b239cf0e7f9bbbd7f49ac9d5f1dc9ee`。
本请求不改它、ce93、f43或原3b9源。

每批显式保持：

- eta文本0.01；完整实际非零d3的normal-plus-Schur方向。
- 原outer8次方向、每次最多20个回溯；原inner12次更新、每次最多20个回溯。
- 原完整三残差merit、真实full-J方向斜率、0.2 Armijo。
- 原unit1e-8与完整112候选标志各自口径，inner阈值不另作为outer资格门。
- 原最终真实参数FD、scalar Arb160bits/depth14、原零core circle检查。

只有原child状态完整返回，并且
`search_stop_reason == "explicit outer direction budget completed"`、
`original_unit_stopping_tolerance_met is False`，才进入下一批。
最多64批。任一原非预算停止、原unit停止或异常均停止，不强行越过。
本编排不重算任何科学判据；源与输入身份检查只防止错误文件接线。

每批结束从该批实际status的`final.parameters`写下一短recipe，并记录该真实文件的
bytes/SHA和实际打印短摘要的bytes/SHA。同run内不同批由这些真实SHA区分。
原state/残差/J不塞入recipe。任何情况下均不把该搜索说成原native/BVP或闭场完成。

## 3. 两个job及规则同步

独立触发文件为
`computations/public-small-core-recipe-batches-request.json`；
独立workflow为
`.github/workflows/visible-larger-public-small-core-recipe-batches.yml`。
只有该request的main push触发，独立concurrency且不取消既有任务。
本源准备没有发布ref或dispatch。

compute job350分钟、科学step320分钟，仅是整体运行上限，不缩减任何一批的原预算。
沿105使用固定checkout/setup版本、Python3.12.14、NumPy2.3.5、SciPy1.17.0、
python-flint0.9.0、BLAS1。只blob:none/depth1/sparse检出，禁gc/maintenance。
四数学输入SHA与原78文件恢复不变；main删除的可重算输入从明确历史
`8bd267107cc8710d371f3b62c02986655ac965b0`逐原件恢复，不写Git或Release。

规则监控复用原
`root_20261114_current576_rules_runner.py` /
`3b8b6dd5eb5df373ffa14525f02e1a0376bafc2da91ce564631f771752e2afde`。
如已公开103接线，只在内存将其BASELINES替换成触发checkout的实际两README全文，
按Git blob核根`74c08a36f6c997d0bc1e64a7956b42276f5fa5d7`、
题`bff8aea253a9e6a7a4fac28d810ac454c5499fec`。原2700秒、独立镜像、
真实pull/rebase、普通H规则行commit/push、NFF循环及规则变化停child逻辑不改。

H必须已有唯一“规则同步记录：”行且不超过10000 B；本workflow不绕过或编造此记录。
compute的contents:write仅供该规则同步；科学checkout始终固定。
GH_TOKEN只给此step的process environment，原helper仅用于Git子进程，不写令牌文件。
正常周期网络同步失败按原helper保科学继续并在最后报错；
真正README变化则打印差异并终止该science进程组，供主控按新规接续。
发生外部超时/取消时只报告已有完成批及真实partial状态，不把未结束批说成完整。

report job以`needs: compute`且`if: always()`运行，无checkout、科学包、写权限。
compute最终reader把不足90000 B的compact JSON经GITHUB_OUTPUT多行协议传给report；
report只校该输出bytes/SHA，打印BEGIN_VISIBLE106_SCALAR_SUMMARY/END标记和元数据。
该SHA范围是UTF-8 JSON字符串，不含日志分隔LF。
主控只取report job的小日志，无需读取计算job全部试探日志。

## 4. 日志与可重算输出

每个完成批的全部原outer/inner试探字典、所有布尔flags、标量、理由和三参数保留在compute日志。
紧凑记录只省略长度大于3的纯数字数组，逐项标明原JSON路径/长度；
原完整封装文件的path/bytes/SHA仍在本批清单。没有伪称永久保全这些raw payload。

完整原输出在RUNNER_TEMP中本批独立TemporaryDirectory内生成；
打印原摘要、试探和所有原文件SHA后正常删除这棵raw目录。
OUT仅覆盖保留最后短recipe、最后compact batch摘要以及最多64条run/参数/hash概览。
无upload-artifact、Release、旧22e publisher或raw提交步骤。
全部重算脚本、实际输入身份、参数、每批完整command、run/source和输出SHA可追溯。

最坏预算计数可达10240次outer试探、2457600次inner试探；
这不是实际次数预测。因此长日志不是新字节审核门。
最终reader用64批定列短表保原merit/p/停止原因/两候选flags和status/summary SHA，
另保最后原flag树、最后原unit3/完整J/FD、scalar/circle原字段。
若非关键细节使读数超过90000 B，明确以其bytes/SHA和compute日志位置代替，
不会改变已经发生的科学结果或把漏项冒成已通过。

## 5. 源闭包与CLI

105的74项主pins原样保留，再加批次runner形成75项主pins。
每个科学child仍报告自身真实15项闭包；不把编排、规则同步或reader混进child闭包。
另列2项workflow support：原3b8和新只读scalar reader；总77个被显式钉住的文件。
旧22e仅来源身份，完全不执行。

批次CLI：
```text
python geometry_20261115_small_core_recipe_batches.py
  --accepted ORIGINAL_ACCEPTED --prepared ORIGINAL_PREPARED
  --tail-anchor ORIGINAL_TRUE112_ANCHOR --tail-config ORIGINAL_CONFIG
  --parameter-recipe actual105-explicit-parameter-recipe.json
  --parameter-recipe-sha256 eafa6814cf2ad6d5da28905c4b78cafcc88c7e1b22b592a5909093d54dd49558
  --max-batches 64 --out FRESH_DIRECTORY
```
子进程全部原科学参数固定于该薄runner中，没有新的lambda扫描/归一化/阈值。
新request可仅从实际未来短recipe续接，不需要保存旧raw status。

## 6. 文件身份与静态范围

以下路径除workflow外均相对本课题根：

| 路径 | UTF-8 bytes | SHA-256 |
|---|---:|---|
| `computations/geometry_20261115_small_core_recipe_batches.py` | 15998 | `0805b44dfc6210fe370e055e5696e8c5444a2855071385cc8e9f5e5dc2d0329f` |
| `computations/actual105-explicit-parameter-recipe.json` | 1260 | `eafa6814cf2ad6d5da28905c4b78cafcc88c7e1b22b592a5909093d54dd49558` |
| `computations/root_20261115_small_core_batch_scalar_readout.py` | 9739 | `c5ce576626326a30015cc20ee2b2c4b22cab97070b14561aac96f0c9b1cfcd3f` |
| `.github/workflows/visible-larger-public-small-core-recipe-batches.yml` | 13202 | `f9494887d2e167104604c09f9777c6ca0c3514c2114ec519e3079b40278f8839` |
| `computations/public-small-core-recipe-batches-request.json` | 22175 | `540a17f5581d0a7da073c0391e03b09829a91d8e759d27ea1e8e5ac95d391d17` |

准备时只进行了公开小源码读取、JSON解析、字符串构造、身份计数和UTF-8/SHA工作；
因本地环境不可用，没有声称本地Python AST/import、bash-n、任何科学数值或运行成功。
工作流开头将实际AST/compile全部75主源和2支撑源；实际科学结果只能以未来Actions为准。
没有新增独立复核、批准或科学接受门。
