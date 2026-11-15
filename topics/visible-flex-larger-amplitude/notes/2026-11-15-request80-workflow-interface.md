# 第80轮：独立阻尼候选的工作流接线

状态：仅源码、格式、身份与语法核对；尚未运行第80轮科学计算。所有文件仅在 `/tmp/visible-larger-request80/`，根负责最终复制、提交、同步与唯一派发。

## 1. 不可变基线与目的

基线是第78轮实际提交 `11b5d25c436d84d734a73d4609092bde749daea5` 的两个原件；制作草稿时，当前公开工作树的对应 Git 对象与它们逐字相同。

| 原件 | 字节 | SHA256 |
| --- | ---: | --- |
| `visible-larger-public-small-core-resonance.yml` | 12424 | `1fd040e6e308d48fee5f8fb69067661f7538968723017ef144598c17c8f2c00b` |
| `public-small-core-resonance-request.json` | 13899 | `30c288e9fe929eb9220240d982b6121645519f49bfdae7d143a4725b25e2be82` |

第78轮原诊断的八次候选均在 $2^{-17}$ 接受，原三个方程仍有大残差。第80轮把候选方向改成已独立冻结的列尺度正阻尼最小二乘方向；它继续消费同一原模型、完整原零尾 Jacobian、原最终 FD／Arb／圆参考函数。这里没有把新入口标为旧 Newton 源未改变，也没有预先声明候选通过。

## 2. 唯一触发与文件定位

最终建议写入原有两个仓库位置：

- `.github/workflows/visible-larger-public-small-core-resonance.yml`
- `topics/visible-flex-larger-amplitude/computations/public-small-core-resonance-request.json`

工作流仍只由第二条路径在 `main` 的 push 触发。没有新增并发工作流或第二个请求路径；同一个 `smallcoreresonance` job、concurrency group、artifact 名及 publisher lane 均保留。

新入口必须另存 `computations/geometry_20261115_small_core_damped_search.py`，13733 B，SHA256 `1691c7d9aad782f9f1a6308ca16fa9630a44988a1b99decdca594a412cdb1728`。原 `geometry_20261114_small_core_resonance.py` 保持 SHA256 `3b9c45abed425a92be662c3547d088a3074ebcc5923c23ac2ef7aaf003124bd5`，留在同目录供新入口按真实 SHA 导入。请求中的 `source_pair` 分别标识这两个对象。

源清单为原68项逐值不动，再加新入口一项，共69项。publisher 仍为 `22e640bb764936215e0bf0d2a4cefcb69808e27b2c81cf0c6b94a751a1e5b9ca`；不需要修改 publisher 或增加 lane。原 source-dependencies、公用恢复入口及恢复后原78源的核验均保留。

## 3. 真实父输入

新增且唯一替换旧父状态的 sparse 路径是：

`topics/visible-flex-larger-amplitude/notes/public-actions-43662193286-1-smallcoreresonance/resonance/resonance-status.json`

完整原件50438 B，SHA256 `09031496410951afc018b223b921db111a43b3e0852592b87aafd5351b4f0c40`。草稿和新入口均核整文件；`final.parameters` 按原值读取：

```json
[0.09365081258727412, -0.13201200770909496, -0.12389206129693811]
```

没有重新优化或推算这一三元组，也没有把第78轮零核心圆参考作为非零解输入。第78轮的 `diagnostic_completed=true`、`success=false` 与 `native_nonlinear_solver_called=false` 的范围保持。

四个原数学输入的路径、字节数和 SHA 与第78轮逐字相同：accepted96、prepared112、真实完整 T112 零响应及原 T112 配置。工作流实际起步会读四个全文件并核其字节；本地草稿检查仅把它们与第78轮已存描述器交叉绑定，没有声称本次又下载或重审四个大型原件。

## 4. 命令与预算

科学 step 从请求构造下面的实参；运行前另存完整 argv 和两源身份。

```bash
python -u "$VISIBLE_COMPUTATIONS/geometry_20261115_small_core_damped_search.py" \
  --accepted "$ACCEPTED96" \
  --prepared "$PREPARED112" \
  --tail-anchor "$ACTUAL_T112_ZERO" \
  --tail-config "$ACTUAL_T112_CONFIG" \
  --parent-status "$ACTUAL78_STATUS" \
  --damping 1 \
  --candidate-steps 8 \
  --backtracks 20 \
  --candidate-resonance-tolerance 1e-8 \
  --interval-bits 160 \
  --interval-depth 14 \
  --out "$VISIBLE_OUT/small-core-damped-search"
```

上述大写输入名仅是说明占位；实际工作流用请求内四个原路径和固定父状态路径，不依赖未设置的环境变量。旧 `--parameters` 与 `--newton-steps` 不再传给新入口。`--damping` 在请求里精确保存字符串 `"1"`，是显式系数，没有隐藏默认值。

原60分钟 job、45分钟科学 step、Python 3.12.14／NumPy 2.3.5／SciPy 1.17.0／python-flint 0.9.0、单线程 BLAS、699站点、M=T=112、2048／4096角网格和原 RHS worker 数均不改。候选预算仍八轮、每轮最多二十个原回溯；不限制为必须用完，也不提高原候选阈值。新方向最多八次6×3最小二乘，原模型求值的保守调用计数见独立算法接口。

原规则由新源直接复用：原三个方程及 Jacobian、未加权 merit、实际 `r @ (J @ d)` 符号检查、原0.2 Armijo、原域异常、原二十个 alpha，以及最终 FD／Arb／完整零核心圆参考。rank、奇异值、增广 L2 模型均只报告，未成为新接受门。最终 `success=false` 的诊断范围不变。

## 5. 输出和失败保全

新状态文件是 `small-core-damped-search/damped-search-status.json`，schema 为 `R259-original-three-equation-column-scaled-LM-candidate-v1`。完整父状态原字节既由绑定 step 保存在 `prior-candidate/`，也由新入口保存在自己的输出目录内。

最终 Arb、完整圆参考、全部候选方向和原试步记录均由入口原样写入独立输出。工作流的 `always()` 读者只复制已存在字段，明确新增方向、阻尼、父状态和两源身份；不存在状态时保留真实 log／partial 文件。读者不会填造候选值或把 workflow success 当科学完成。完整 artifact step 上传整个原 lane 目录，保留所有原件和失败，不只上传小 summary。超过90000 B 的复制摘要才转到 artifact 的 `large-arrays/`，原科学状态、Arb、圆参考文件不删除或截断。

上传与 publisher 的 action／命令、artifact 保留期、普通 pull/rebase/README 检查均与第78轮逐字相同。科学 step 未提供 token 环境变量；仅原 publisher step 沿用 token。

## 6. 本地静态证据与交付

`2026-11-15-request80-static-check.json` 记录21项核对全部通过：69个源完整 SHA、Python 源 AST、7个 shell block 的 `bash -n`、4段内嵌 Python AST、唯一正确 trigger、checkout仅替父状态、原 runtime／预算／权限／artifact／publisher 保持、真实父状态原字节及参数三元组、源对身份和新 CLI。

本地未导入科学 producer，未计算模型、FD、Arb、范数、SVD、Jacobian 或新圆参考。两个差异文件包含基线到草稿的完整文本 diff；不是只列摘要。

交付包括工作流草稿、request、`workflow-from-actual78.diff`、`request-from-actual78.diff`、静态证据和本接口。`build_request80.py` 是元数据草稿生成器，含生成时刻；冻结后不要为了核验而重跑它，应运行只读的 `check_request80.py`。

算法细节、正阻尼方向的条件下降恒等式、尺度单位、非有限与 rank 范围见 [独立阻尼候选接口](2026-11-15-small-core-damped-search-interface.md)。第78轮原实际数值与身份见 [第78轮正式结论](2026-11-15-actual78-small-core-eight-tiny-Newton-steps.md)。
