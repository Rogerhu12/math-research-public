# Request93：actual92 → 非精确p3恢复的唯一公开Actions接线

日期：2026-11-15（UTC）。作者：/root GPT-6 Astra Pro。本文记录已冻结的执行接口；不预填新run/job/artifact或数学成功。完整新算法、线性normal correction、保留d3及原验收语义见[科学接口](2026-11-15-inexact-p3-restoration-search-interface.md)。所有数学只在本公开仓库Actions执行。

## 1. 源、请求及唯一触发

| 仓库目标 | bytes | SHA256 |
|---|---:|---|
| `computations/geometry_20261115_small_core_inexact_p3_restoration.py` | 45133 | `ce93a364f8423c89e9e696e1e2c96662b61c6daaf225bd51c44fcd572e05654e` |
| `.github/workflows/visible-larger-public-small-core-resonance.yml` | 20198 | `6872ff02d77a40478057989f72549ce7fff4ec4ae14ed9f4fc3f9a3309a350f4` |
| `computations/public-small-core-resonance-request.json` | 19846 | `9a5f4f3fb275bc4ce9440a0d48fd962e75a275ed3e3508c5805d97b64e57b6d4` |

唯一push触发仍是main上的 `topics/visible-flex-larger-amplitude/computations/public-small-core-resonance-request.json`；沿用smallcoreresonance job/concurrency且cancel-in-progress=false。不另dispatch、不加平行数值lane、不改别的课题。原71个source pin逐字节保留，仅添本独立新源，合计72；源自身直接校验十二个既有文件并连自身记录十三个身份。

原3b9方程/J/description/Arb/circle函数仍直接执行。3b48只核父来源，ec9/1691仅保更早来源；旧92搜索不被偷作新实现。请求的 `scientific_source_unchanged=false` 和新schema明确说明算法变化。完整科学源diff为 `source-from-actual92.diff`；接线和请求完整diff分别为 `workflow-from-actual92.diff` / `request-from-actual92.diff`，均已由root完整读取（工作流另逐行完整阅读）。

## 2. 唯一真实父及四输入

父是实际92：run43672921972 / source1755a4f414a77d41d85eae9a0e1625f55a74be90 / job132686715503，所有步骤成功。其原artifact14144239294、676336 B、完整ZIP SHA f10832bad2ebf3b48a4da501bc0a50b7556e7a839eb86ddd532cab497338d74a，已唯一完整取回。

checkout及pin步骤直接读取其已公开原status：

```text
topics/visible-flex-larger-amplitude/notes/public-actions-43672921972-1-smallcoreresonance/small-core-p3-inner-root/p3-inner-root-status.json
498765 bytes
e822be884ac07e2b2c46ac7aba7f589ba5233e86cdbb33ad9c95108cc8dca01e
```

它保持旧schema `R278-original-three-equation-approximate-p3-inner-root-LM-v1` 和producer3b48。pin步骤核完整SHA/size、旧schema/producer、完成与non-native flags、所有consumed源、原四输入和 `final.parameters`；额外无损副本写为 `prior-candidate/actual92-p3-inner-root-status.json`。新科学源再独立校验同一父，只有最后实际接受参数是初猜，不继承未接受内点。

四输入完整SHA/size及路径保原accepted/prepared/true-zero T112 anchor/config，和92的请求逐结构相同。原78源码恢复只运行一次。Python3.12.14、NumPy2.3.5、SciPy1.17.0、python-flint0.9.0、三个单线程环境变量、action pins、checkout无持久凭据均保留。

## 3. 唯一科学命令和预算

命令仍一次subprocess调用，四输入原CLI和新父SHA之外显式提供：

```bash
--damping 0.1 --candidate-steps 8 --backtracks 20 \
--inner-newton-steps 12 --inner-backtracks 20 \
--candidate-resonance-tolerance 1e-8 --interval-bits 160 --interval-depth 14
```

output为 `small-core-inexact-p3-restoration/inexact-p3-restoration-status.json`，新schema `R278-original-three-equation-inexact-p3-restoration-LM-v1`。job60分钟与科学step45分钟均未改变；本轮没有第二次自动科学重试。

内层仍实际尝试原1e-8目标。最后有限实际点及其同点原J/J33可以进入完整三项merit试验，不能因未达到内层目标就称根或跳过原外层验收。线性方向显式含-d3/J33 normal项；真实恢复位移与alpha*v分别记录。原最终unit/full112阈值、description三档FD、Arb和完整零核心圆检查保持同源同定义。小核candidate不是BVP/native接受，success仍false。

## 4. 读回、失败及完整输出

always读回只用stdlib读取现有status。它复制原初末描述、当前全三方程merit、停止原因、每档实际接受/拒绝、真实d3、实际总位移、恢复位移以及内层两个不同标志：`usable_inner_root` 和 `usable_restoration_point`。新initial_projection为performed=false，明确父没有先被未验收点替换。

读回大于90000 B时仍把完整派生读回保存于large-arrays，普通读回保关键标量、实际位移和完整文件descriptor；原status与全部inner报告从不因展示体积截断。原完整模型/J轨迹留在artifact-only的large-arrays。父原件、所有内层完整报告、错误、原命令、source/input身份都随完整artifact always上传，30天保留、compression1、原upload action不变。

发布器仍 `root_20261114_publish_actions.py`，SHA `22e640bb764936215e0bf0d2a4cefcb69808e27b2c81cf0c6b94a751a1e5b9ca`。普通pull/rebase、两README检查、现有体积规则与partial失败保全均不改。没有引入新native/SDK/网络存储实验或科学审核门。

## 5. 已付静态范围

root完整读新源相对已完整读92的全部diff、两份完整算法/接线接口、新完整workflow和全部request diff。独立静态回执核72源、原四输入、真实92完整status/三参数binary64身份、十三直接来源闭合、七shell语法块和四inline Python AST。原十个utility/observer AST及整个原最后diagnostic阶段AST与92相同。

新公式、同点J身份、真实位移记录与去除内层资格硬门均只做源码检查；没有本地导入数学源、构造fixture、执行矩阵/范数/求根或重算92。静态检查是实现记录，不是未来科学成功，也不构成额外数学验收。

回执 `2026-11-15-request93-root-static-readback.json`：23595 B，SHA `3eeac349d83d57c8884c8f0d4377a358884d7ee27183ea5be97b8b00f9f9842b`，117项全部通过。
