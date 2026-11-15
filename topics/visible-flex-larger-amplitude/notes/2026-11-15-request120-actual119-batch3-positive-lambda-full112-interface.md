# Request120：实际119第3批六参数的小正λ完整112场实验

类型：可执行实验与生命周期接口。作者：OpenAI ChatGPT（amplitude）。日期：2026-11-15。这里只作源码、参数与原读数操作；没有本地科学执行、Git发布或实际派发。

## 1. 本次要实际求什么

采用已经冻结的新入口 `geometry_20261115_six_control_full112.py`（42683 B，SHA `807f6a35e0d66aee7a2f324e4573bd2b9e9be8feab1972e4b073aa8ee91ed7a2`）。完整接口见[六控制三active非零112入口](2026-11-15-six-control-three-active-nonzero112-interface.md)。本次不是低三模候选搜索：它从真实六系数和显式正λ产生完整初猜，尝试原有限物理场、全部112 core和真实非线性尾端的耦合求解。

选取 **实际119第3批末点**，不是119第8批最后点：

```json
[0.41654476801167684,0.23884336093393582,0.5270922473095916,-0.13437878055563054,-0.005765450212224129,0.4141025261683763]
```

真实来源为 run `43693462669`、source `6fffce1f36e876f3b08a1c73198a7fde259d94d6`。该批原摘要73546 B，SHA `4ec08e23ea41bc3f443f04f613270163c9e8624d8b4172ab2a35f998b75acf5a`；其原status1568824 B，SHA `10c31f1da398f537f1c9dfb19a162bb6aadb30e7e57fddafffebf7a9a60c08e4`。本recipe只消费实际保存的 `final.parameters` 字面值和来源身份，不将旧status、J、FD、Arb或circle读数冒成本次重算。

主控选此批的浮点依据是该点前三active列的已存奇异值为 `[193504546.48297158,166241.91917386654,23.479971346554226]`，完整六列为 `[194240478.14283228,192125.2730766859,30.014184216747374]`。这是种子响应的选择依据，不是rank证明，也不说明低三根已求得。小核unit未到1e−8并不被加为完整场开算门。

本次 **λ=0.001**，前三core目标为原 accepted96 三目标乘该比例。六个标量系数不乘λ，三个odd固定，前三p仍是完整BVP的active未知。小比例仅缩入口与所用低三线性初猜的一阶幅度；全部原物理域、native和最终接受仍要在这次实际付出，不能由小λ推出存在性。

## 2. 不变的完整数学与当前native责任

每节点338物理场、112 core、3 active参数，共453；左边界341行、右边界112行。高109 core仍自由，原零H的完整112×112 J只用于新初猜里的线性来源。实际场M112/N2048、material与physical边界各4096角；没有新增截断或高模零边界。

初猜在选定六p重新形成circle与低三U/H/T，再计算全部453行原RHS，经过原node、midpoint和两个Lobatto RMS点预检。随后由实际完整endpoint/core计算当前H，交 **原** `exact_20261114_true_tail_client.py`：

1. 当前H真native solve及完整height-J先完成。
2. 原physical-boundary FD实际执行：原三个非零height扰动、方向、三个步长、两个Richardson层、收缩条件、5e−5阈值不变。
3. 同一个live client交原banded/full-DN主函数，原8outer、每个Newton的17trial、原真实新H更新全部保留。
4. 原1e−6 collocation与冻结physical RMS、1e−11 BC、最终fresh native完整J/audit与真实cut/seam读出保留。

原native配置仍为M112/spacing2/quadrature2048、solveTolerance2e−9、maxIterations32和原10档回溯；没有改root/RHS/RK/native算法。尾端若失败，结果就是此原路径的失败，不会伪造current-H响应或转用旧零J继续。首次全场预检失败时，FD和native也明确尚未执行。

## 3. 原四输入与两个ready必须真实恢复

四输入全部来自历史公开提交 `8bd267107cc8710d371f3b62c02986655ac965b0`，逐原size/SHA核后写入本次 `RUNNER_TEMP`；不给main或Release重新增加raw。

| 输入 | 原字节数 | SHA-256 |
|---|---:|---|
| accepted96 | 2614352 | `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff` |
| original prepared112 | 4220043 | `0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714` |
| actual zero-H J112 | 6815 | `e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51` |
| T112 config | 2161 | `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5` |

临时文件保留 `.json.gz`/`.json` 后缀，因为原 `full_scalar_profile.read` 按后缀解压。配置真实没有 `initialCheckpoint`，本请求对此显式核对，并直接传原配置，不调用会重新序列化配置的prepare_config。客户端为本次trace/iteration/trial输出生成自己的runtime config并记录新SHA；原input config SHA不改。

另按已实际成功的113机制恢复两原ready到临时目录，设置客户端已存在的 `VISIBLE_FLEX_FROZEN_LEDGER_READY` 与 `VISIBLE_FLEX_FROZEN_STORED_READY`；这两件size/SHA/Gitblob与冻结入口接口§8相同。通过原 `exact_20261114_public_resume.prepare_public_source` 恢复78份原公开source，`--tail-source-root` 指向实际返回topic的 `repro/source-root`。原factory继续自行核冻结几何与指纹。

本请求没有actual91、95、103 checkpoint输入，也没有假设任何这些失败尝试为已接受尾。原T112客户端可启动不等于已付成功bootstrap；实际非线性响应和最终审计正是本次要求。

## 4. 进程预算和原规则监控

独立workflow为 `.github/workflows/visible-larger-public-six-control-full112.yml`，唯一push触发文件为 `computations/public-six-control-full112-request.json`。这里只准备草稿，没有未来run或artifact ID。

Python3.12.14、NumPy2.3.5、SciPy1.17.0、python-flint0.9.0、Node24.22.1；BLAS/OMP单线程。原RHS workers2、maxnodes1200、Nodeheap1536MiB均显式保持。依赖/源码SHA由99项本请求清单绑定；这是来源清单的superset，不声称99件均执行过。

原数学预算与墙钟边界分开：

| 层 | 设置 |
|---|---|
| native实际每次solve | 原32×10/2e−9，未修改 |
| 原field/full-DN | 原8outer/17trial/1e−6与1e−11，未修改 |
| 独立整个实验墙钟 | 18000s，即300min |
| science step | 330min |
| compute job | 350min |
| 原规则监控 | 2700s，原真实pull/rebase/README变化停止 |

外层只用stdlib启动冻结适配器，不导入数学模块。wallclock到时或规则监控发TERM，它停止该科学子进程的独立process group（包含native Node），并报告partial；先TERM，最多8s后KILL，stdout线程最多2s收尾，留在原rules-runner15s取消窗口内。预算结束不是新的非线性拒绝理由，也不改变已执行trial的原接受规则。

适配器自身保留原core/client关闭责任；强制截止不能冒其finally已经完成，所以process状态与native关闭状态各自报告。stdout/stderr原字节在临时log同时转发；日志复制异常另记。原规则runner文件及其源码SHA不变，仅显式将其README baseline元数据绑定本触发checkout的实际两个已读blob。`merge.stat=false`只抑制Git合并diffstat，不改变科学checkout。

## 5. 纯读回和临时生命周期

`root_20261115_six_control_full112_scalar_readout.py`只读原JSON/log/已有字段和SHA，不import NumPy/SciPy/Flint，不调用RHS、J、native、norm或新求解。它保留：

- 原参数/λ/source/input身份、process实际返回/partial、adapter当前阶段和真实异常。
- 初猜和完整RMS预检的已存原读数，包括原报告本身只记录的前24个失败点范围，不扩称完整连续域。
- current-H真实响应、原完整FD、所有已保存inner-domain evaluation与原Newton stdout接受/失败事件。
- 全部原outer记录、完整band线性残差原读数、native trace/trials/真实返回，以及原最终RMS/BC/J/audit阶段是否达到。
- 成功时原完整六参数、112core、最终有限读数和输出文件SHA；不输出全场/因子raw，也不重算残差。

摘要用单份compact JSON，≤90000 UTF-8 B；先打印各section真实bytecount。若详细section超预算，保primary outcome并显式置 `summary_complete=false`，用该section count/hash取代超长部分；若仍超限，输出有原主要phase/错误的小failure对象。输出大小问题不会改写科学成功/失败或重跑实验。没有保存的phase一律不是通过。

compute无论科学成功、原失败或预算partial，随后都执行只读摘要；通过GitHub job outputs传一份小文本给独立5min报告job，再删除本请求的临时原件/日志/fields/factors/source-cache/rule-sync目录。没有artifact/Release/upload/publisher raw动作。临时删除失败独立记录，不改变原科学结论。

若未来继续λ或同family完整场，必须在同一有真实parent文件的job中接下一调用，或明示从recipe重新求本段；本次只留小参数/结果/hash不能冒为仍存在的完整父场。本请求没有设置无条件自动续步。

## 6. 冻结交付和范围

本目录拟发布六件：一次调用wrapper、纯读回source、实际119第3批recipe、独立request、workflow、本接口。冻结数学入口807f已经另行发布；没有修改任何旧数学source。`build_request120.py`、source-pins-draft和static-source-check只为本地可重算源码构建说明，不要求入仓。

本地仅原JSON字段/字节来源、Python AST、shell语法和source SHA静态检查。没有数值fixture，没有运行参数选择实验，也没有借此增加独立审核/证明门。实际作业是否达到非零完整有限场接受、是否被初猜域/native/FD/原Newton阻断，只由本次原结果回答；闭面/连续证书仍保持其原范围。
