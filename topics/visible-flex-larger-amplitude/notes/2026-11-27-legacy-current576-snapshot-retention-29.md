# 第29次旧派生清单保留处理：八份完整 current576 snapshot 清单

本次只从当前树移出八份已生成的 `array-manifest.json`，合计 **1,369,660 bytes**。完整原请求、原 `current-solve-spec.json.gz`、所有原 context/result/状态、已有 payload、完整源和其他 sibling 均保留原处。本次没有运行旧数学程序、改变旧结论或把派生输出重命名为原始输入。

## 1. 精确历史恢复

以下原字节全部保在已公开固定提交 `612d82679c59a11778e4218e36c23b348609a52f`。先查大小，再流式核 whole SHA；没有把大清单的数组逐条读到会话或整份解析。当前文件 Git blob 与固定历史 blob 大小也逐件核过。

| topic 相对路径 | bytes | SHA256 |
|---|---:|---|
| `notes/public-actions-43675377211-1-current576native/native-word-first-current576/iteration-000/snapshot/array-manifest.json` | 171210 | `47b636d88b8890d6c8087a78421d94faf4ae2ec2cf705fe1d9af904ca6c7d42f` |
| `notes/public-actions-43657001633-1-current576native/native-noj-primal-current576-damped/iteration-000/snapshot/array-manifest.json` | 171210 | `95543c3f91bfb0a8d58b7fda7af5427674cf59d3a6febbdc464a083fca471dec` |
| `notes/public-actions-43657001633-1-current576native/native-noj-primal-current576-damped/iteration-001/snapshot/array-manifest.json` | 171210 | `bc1e18e89c1c865b3824d4e01669c4ed653e7cba29c085a0d86ef39b3fa3bf70` |
| `notes/public-actions-43657001633-1-current576native/native-noj-primal-current576-damped/iteration-002/snapshot/array-manifest.json` | 171210 | `47e84aeae29a1736217ff3d0774d38a1dbc1a0337501c098c3f8c1820434a610` |
| `notes/public-actions-43645948199-1-current576native/native-current576-damped/iteration-000/snapshot/array-manifest.json` | 171205 | `5176cf368eb5098f531ed71d96694065cd899a454547c6fb8a6ee228be4dda7d` |
| `notes/public-actions-43645948199-1-current576native/native-current576-damped/iteration-001/snapshot/array-manifest.json` | 171205 | `411acc2e8d1cb9df40e6bda7b363bd65296bed7fbd4988d68180acf9d8338737` |
| `notes/public-actions-43645948199-1-current576native/native-current576-damped/iteration-002/snapshot/array-manifest.json` | 171205 | `8d2ea11a514e38e6c11ca05a4f0696715edfc8e7e2822a9fa01b7ed65eee8cd6` |
| `notes/public-actions-43645948199-1-current576native/native-current576-damped/iteration-003/snapshot/array-manifest.json` | 171205 | `a7525246aabfeab518e3f7f9cda6529da4f60b032c1834acc7b3686679ee24bc` |

全部 Git blob、完整三个原请求对象、原spec whole身份及源版本保在[完整来源/参数账本](../computations/legacy-current576-snapshot-retention-29-provenance.json)。该账本55022 bytes，SHA256 `3c30ec4e8d3ad145c04767c7f1d42c11aea25fa25dcf45a9351702d3d1b2181f`。原请求本体和全部spec也保留原文件；不以表格或元数据代替原完整输入。

## 2. 原请求与实际来源版本

三条来源分别是 request95（run43675377211、源提交90da0e1195100053583134f2714aa3b43ff6282d）、request73（run43657001633、源提交9515d5aaf7c68f8efd366438d6bd81ce73c3486f）、request61（run43645948199、源提交cf6b51193255dfc713610d2919598451ccdd49e2）。完整原请求为11813、8653、13197 bytes，原24/18/14项来源、真实父输入、完整参数和所有范围字段均保留。

原参数包括完整576 stage/577 node/224 shape、全部129248 equation、原32次非线性/10次trial/2e−9容差、eta1、所有原penalty/constant和原输入word责任；request95的单字候选仅是原实际输入选择，不被本次改成求解成功。完整请求的历史artifact字段照历史保存，不授权本次新增raw上传。三个spec压缩文件的11562、50477、12754原字节及全部内容都留在原位置；本次没有解压大参数树或提取部分来替代完整spec。

56项来源声明中54项与当前完整源相同，另两项是行政发布器的实际旧版本。root分别从其原source commit取得完整小源码并核字节：

| 原提交 | bytes | 原发布器SHA256 |
|---|---:|---|
| `9515d5aaf7c68f8efd366438d6bd81ce73c3486f` | 12620 | `627393d1ba77b5e13dcf34da64204d0554a7c009770a2d80a1353c3f16b007fe` |
| `cf6b51193255dfc713610d2919598451ccdd49e2` | 10413 | `dff4c62358d6680134d2d94a0bd2eb6e332011ec67ee1ca0c390aee2cfb65aa4` |

当前发布器为14455 bytes/22e640bb764936215e0bf0d2a4cefcb69808e27b2c81cf0c6b94a751a1e5b9ca；不能冒作两份旧源。账本完整保原blob/commit/size/SHA。全部30种当前完整源及原数学hook已核；没有由来源核验虚称重演旧科学或恢复其大payload。

## 3. 为什么这是派生输出；完整生产函数已读

root完整读取 `geometry_20261114_native_current576_damped_solve_hook.mjs` 的实际 `captureCurrent`（4549-byte函数），以及noJ/word-first两个完整函数的全部差异（各5364 bytes）。三份完整hook分别为44103/53665/61870 bytes，whole SHA依次为 `0933ee819ce56be648f17e2e876372e943059f19c79fed701bda60ec11cf66dc`、`099798e9c57f09b82f7532ea184d124446aeeb2cdbafe452390cb794b8db405d`、`932961ef9f267f95f5de6bb28791ed43ef2c66d15b18b55823bc3f2384545bc3`。

函数只接收原真实evaluate已经返回的完整ev/states，要求全部576 flows/residuals与577 states。它保存全部十组数组：base states、stage residuals/out/J、原scales、cut/end residual、far graph、physical height与target，再将真实arrays记录及source/调用/迭代序号写成manifest。原cut是当前真实减法；不是由零值或旧缓存补造。两个后继保新flow安装收据等号、原完整数据和原metadata，没有新增RHS/J/ODE调用。这证明候选是原真实输出清单，不能把它当原始数学输入重新归类。

## 4. 恢复与后继读者的真实责任

需要原清单时，在scratch/runner用 `git show 612d82679c59a11778e4218e36c23b348609a52f:topics/visible-flex-larger-amplitude/<表中路径>` 恢复并核完整SHA。仅此操作恢复清单字节，不自动恢复其枚举的所有科学数组、父artifact或缺失payload。旧动态reader仍须明确读取它真正需要的完整恢复路径，不能缺文件就换空集合、删行或默认通过。

本次没有声称所有动态消费者不存在；有些后继原请求确实引用旧snapshot，本次完整保留这些请求及全部历史恢复定位。若重做旧科学，仍只在公开Actions使用完整原源、真实全部父输入及原参数；不把再次浮点运行预报为逐字重现旧输出。现有08/09计算、未知历史/typed和课题全部完成标准不改变。
