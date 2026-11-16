# R510 — 冻结 220 来源合同的 JSON 分类薄修与同一时钟接线

**可信度：已证明，限本文明确的来源、字节变换与控制流条件命题；Request 222 尚未实际执行。** 本文不给出新 C、参数域、far、BVP、闭面、误差、reach 或 held 的数值结论。

作者：OpenAI / ChatGPT amplitude agent（AI）。日期：2026-11-16。

## 1. 实际问题与修复对象

R506 已记录实际 220 的独立终态：run 43833995131，实际 source
`3ea0620a199e08deb542eaca10b4cee2db5dd45b`。第六个来源生成器在
`required_public_sources` 中遇到 R503 的 JSON 政策文件，原生成器只允许
Python 或 JavaScript 源文件 basename，因而抛出：

`ValueError: Use an explicit local Python or JavaScript source basename`

该错误发生于第六层 46 个视图生成之前。它不构成任何数学候选的否定。
本文不再次读取该 run 的日志，不恢复已消失的 runner 原件。R506 的原必要
范围、未返完整物化结果的边界，仍以其独立结论为准。

新 222 只改变一项来源分类：R503 JSON 从这一“可执行源码输入名单”移出，
仍是外层完整字节绑定的政策输入。原生成器的 Python/JavaScript 限制不放宽；
原四个 outer 文件、全部 46 个当前视图的期望全文，以及此前 133 个视图均保留。

关键原件：

| 原件 | bytes | SHA-256 |
|---|---:|---|
| 220 请求全文 | 99218 | `f6ca63871733d3f5e48ef3eb8d540fc137806ceb1ae74cef01af6b21e25f3aba` |
| 220 第六层计划 | 66325 | `14970cc2fea0f5245218ae0752e5659747a69d6d5a22d25252fe166a48c7a786` |
| R503 JSON 政策计划 | 18919 | `2f6113ce7b1928d2954d8768d2117db4452abf89cbb7f2f8b1a57719228e9dd3` |
| 原 R496 生成器 | 11895 | `4d4c507edd571b67655fd2e66fb4bcfa173b1239928443831a81a925c4869ec4` |

新完整第六层计划为
`notes/request222-coast-base-source-only-repair-plan.json`，
66182 bytes，
`7a74a8e65b7283bfe9acb36a27a38dbef01e8ee0507eff0ac4c3548015288ddf`。
它比原计划少 143 bytes。删去的唯一完整 descriptor 是上述 R503 JSON；
原 124 项 literal patch、364 项 application 与全部 46 个输出 descriptor 不变。

## 2. 名单变换命题

设 $P$ 是完整原计划文本，$J$ 是上表 R503 JSON 的 descriptor，
$P'$ 是已明确给出的新计划文本。新 entry 读取两个完整原件并检查：

1. 原件分别满足原、新全文 bytes 与 SHA；
2. 指定原 literal 出现恰一次，替换后的全部字节恰等于 $P'$；
3. 原 `required_public_sources` 恰包含一个 $J$；
4. 新名单恰是按原次序去掉 $J$ 后的名单；
5. 移除该成员后，两份完整 JSON 对象的其余成员相等。

由第 2 项，新计划不是由重新排版、重新求值或近似重建得到的未绑定文本。
由第 4、5 项，其余五个源码输入和所有生成内容保持原合同。原生成器仍逐项
核五个源码输入，随后按原顺序和原 occurrence count 形成全部视图。

上述比较均是公开源码/参数的来源绑定，不计算科学数据，不加入新的数学接受
条件。该命题也不声称未来生成器一定完成：缺文件、实际来源不符、资源中断或
其他原异常仍按真实返回记录。

## 3. 真正派生的 220 元数据合同

新入口不把改变后的请求继续标成原 `f6ca...`。实际派生 220 请求为：

- 99330 bytes；
- SHA-256：
  `2d1c3a7d56093f0009367bce0e201af14692b51541b759aa3d60b7737dfdaad2`；
- 它保留原内部 schema、request_number 220 与原来源名称；
- 新公开入口为 request_number 222，实际 run/source 取本次 Actions 环境。

内部 220、205 数字在这里表示被复用的源码接口，不是原 220、205 run 的身份。
新 entry 的独立 receipt 明确列出实际入口号 222、原祖先、实际派生文本及实际
run/source。原 composer 的 `explicit220_composition` 标签仍是该冻结模块
的来源标签，不被解释为本次工作流编号。

派生请求只通过 11 项公开的 literal 替换生成。其内容是：

- 第六层 `plan` 指向新计划；
- 第三个 `public_source_plan_copies` 指向新计划的真实 notes 原件；
- 新计划作为一个额外公开文件加入 source map；
- 相应来源计数及 `actual_source_groups` 随真实并集更新。

旧第六层计划仍完整保留为历史公开 pin。R503 JSON 也仍在完整公开 source map，
且 entry 实际读取其全部字节。原角色字典、native 注册字典、execution 与
refinement_work 逐对象保持；当前候选、科学参数、预算与原门没有改变。

来源计数因此为：

| 集合 | 原 220 | 真派生 220 |
|---|---:|---:|
| 公开文件 | 278 | 279 |
| 历史及当前实际生成源 | 179 | 179 |
| 完整运行 source map | 457 | 458 |
| 当前第六层输出 | 46 | 46 |

新 metadata entry 由独立小 222 请求直接绑定，属于外层来源编排；不冒称它是
被原 458 项数学/运行源码 map 遍历过的额外科学源。

## 4. 固定 caller 的路径约束与真实工作视图

原 composer 的 `compose` 要求：

- `comp == HERE == GITHUB_WORKSPACE/topic/computations`；
- 请求路径是该 workspace 中固定的 220 notes 路径，或 namespace 中唯一副本；
- 实际请求字节等于该 workspace 固定路径中的字节；
- CLI 的请求 SHA 也等于这些真实字节的 SHA。

简单把新 JSON 放到另一文件名再传入旧 caller，不能满足此实际合同。
本文不修改四个 caller，也不在内存中替换常量或导入规则。

新 entry 建立独立临时工作视图：

`$RUNNER_TEMP/request222-runtime-metadata-workspace`

当前 Git checkout 的所有已检出普通文件被逐字节复制并形成临时完整索引；
不复制 Git 对象数据库，不复制本次科学 raw。原 checkout 中的请求、计划与
源码文件均不改写。工作视图中的固定 220 请求路径才被替换为上节的派生文本。
该替换先核工作副本仍是原完整请求，再原子装入新字节。

视图的 `.git` 是指向当前原 Git 对象目录的标准 gitdir 文件；entry 不创建
或更新 branch/ref/index，不发布 commit。原历史源读取仍是本次真实 HEAD 的
Git 对象读取。原规则 runner 在自己的独立 mirror 中执行原同步，不把本临时
metadata 工作副本推回仓库。

原 Git checkout 路径另记为 `primary_checkout`，
真实临时视图记为 `actual_working_view`。原 `f6ca...` 原件还保留在
`source-preparation222/frozen220-request.json`。不得对工作视图中的派生请求
使用这个原 hash。

每个 workflow shell run 明确读取
`$RUNNER_TEMP/request222-runtime-env.sh`。该脚本设置真实
`GITHUB_WORKSPACE`、`VISIBLE_COMPUTATIONS`、`VISIBLE_BASE`，
并切换到该实际工作目录。GitHub 保留变量不通过 `GITHUB_ENV` 伪改；
该文件只追加普通 VISIBLE/REQUEST222 元数据变量。所有实际 driver、checkpoint、
loader 看到同一真实 HERE，没有“新文件在另一目录却标旧 computations”的问题。

## 5. 字节与来源保持的条件结论

四个冻结 outer 源为：

| 源 | bytes | SHA-256 |
|---|---:|---|
| composer | 47343 | `f3e8ce8ebdfdd7df7f2ccd78da7c203f185de3f9c17403e0fb489e2f5cf18fca` |
| owned roles | 25670 | `4afc01350bbaa239556f3b3edab6260b727e772df3b04351e357b0831149efc3` |
| joint refinement | 48824 | `7dbc1dc3a52a812eef742e892601a539bd8908cf62179e0c68527f6a0b5af55b` |
| necessary reader | 42493 | `e887a1ced3906a4975d34815c12900a2b817318c02e9354db2e23883b7309a1c` |

在 entry 返回 completed=true、随后原物化/绑定过程实际完成的条件下：

1. 原四个源码仍具有表中全文身份；
2. 原 278 个公开输入仍按各自原身份存在，新计划是唯一追加的运行公开项；
3. 原 133 个生成项与当前 46 个项仍按原完整 descriptor/occurrence count 生成；
4. 传给 `H.bind_request`、各 CLI、reader 与原 composer 的 SHA 均是真派生
   `2d1c...`，不是祖先 `f6ca...`；
5. 原 composer 重新形成当前 derived205，保存其真实 bytes/SHA；没有把原
   220 run 的旧 derived205 哈希填作本次结果；
6. 原 R503 政策 JSON 仍作为完整文件付真实 byte binding。

该结论只说明来源组合忠实。它不证明解析导数准确性、rank、非线性下降、
数值误差、域条件或后续完成；它也不把 source-syntax 成功等同于科学通过。
原两份已经披露的历史语法错误 owner 仍仅按原完整历史 pin 保留，当前调用
不转向它们，原其他实际源码语法步骤保持。

## 6. 唯一时钟覆盖新增准备工作

令 $t_0$ 是新 entry 在创建唯一原 namespace 前紧接记录的时间。
它早于新增的源码/计划读取、复制、请求形成与 owner bootstrap。

entry 不调用原 `initialize` 来产生第二个较晚起点。它调用原 composer 的
`stage_public_source_plans`、`compose`、`formed_owner_source` 等元数据
函数，沿原 bootstrap 的完整字节及既有 Actions-only syntax 操作，最后用
同一个 $t_0$ 写出原 deadline schema。

原 startup resource receipt 保持：

$$
T_{\rm science}=t_0+18900,\qquad
T_{\rm readback}=t_0+18900+2700.
$$

其 `request_sha256` 是本次实际 derived205 的 SHA；不是原 220 请求 SHA，
也不是旧 run 的 derived205 SHA。recipe SHA 仍是原
`d926cecf92f35cf4c7ae8cc86ad243287846d73df98c78e8ba1005c568ab8811`。

namespace-start receipt、entry 结果、实际 deadline 三者保留同一 $t_0$。
后续原 owner、BVP、精化及必要读回继续消费该真实 deadline。
因此复制和准备耗时进入原 elapsed，不靠后移时间得到额外科学预算。

这不新增原本不存在的“全部前置阶段统一绝对 kill”承诺。原 C/采样阶段的
计时语义、原 BVP 启动预算分配、原后继 remaining-time clipping、job 360 分钟
及其真实未访范围均保持。各 cap 仍是上限，不能相加成新的许可总时长。

## 7. 保持的科学路径与未付责任

实际科学 argv/模型仍来自被冻结的完整 220 合同：

- R503 的新准确初猜政策不变：原 actual202 投影后显式把 coast 支撑 2 的
  p3、theta3、eta3 置正零，其余七词保持；后续仍原三 active p、七冻结 shape；
- 同 C/cut/完整域记录、全部 112 far、原数值代表行、真实 453→同十词 fresh450；
- 每个实际场的 radial/atlas/shared/metric/reach，以及独立 held；
- R456 五因素均为 2 的真实 112 后继，然后真实 R462/R463/R464 M128 union；
- M 层继承实际父分辨率，四非径向因素为 1，不伪造原 112 far 的新 M 传播；
- R459 实际误差/t 比较与 R461 有限显示分别保持原范围。

原 32 GiB startup 和 2 GiB live free-space 条件、原采样工作与 depth2、
完整 FD、原 full-DN/RMS/边界/最终 fresh/audit 条件全部保持。
全解析 338×112 J 不被额外添加成原 full-DN 的前门。
完整程序返回、声明布尔与真正接受条件仍分别读取。

首次闭面实际 A/B、全构造、共同材料责任继续由原 caller 记录。B 缺失不能
冒作已付材料测量，也不增加求解/held 成功前门。有限显示不支付连续全 t
或面内误差。本文不声称新初猜已经全域合法，也不预报任何实际接受。

## 8. 读回、失败与清理

新 entry 只增加独立、单份、至多 90000 bytes 的不可变来源摘要。
其内容包含：

- 原/新请求和计划的真实来源；
- 原四个 outer 实际工作文件身份；
- 实际副本索引身份与复制数量，不搬其完整大表；
- 真实 derived205/composition/deadline/env receipts；
- 全部实际准备错误、complete 状态及唯一开始时间。

过大返回 70，不分块、编码或借重算压缩科学数据。此摘要没有“科学成功”
或“所有进程已静止”的冒名布尔。

它成功后生成 `request222-repair-readback-complete.json`。
新 cleanup 命令核该 marker 的 actual run/source/entry-request/summary 身份，
再以 `exec` 委托原 220 reader 的 cleanup。后者的原九个必要范围、真实
PID/startticks/后代 session/unknown 检查与所有原清理条件完整保留。
新的 metadata marker 不能替代这些条件。缺 marker、缺原必要范围或 unknown
进程时，不删除科学 raw；剩余寿命按真实 runner 销毁处理。

临时源码工作视图不是科学输出。其未被原科学 namespace 清理函数删除的部分
保留到 runner 销毁；不打包上传 artifact，不提交 raw，不把失败现场的 SHA
当作可恢复的数据副本。

## 9. 实现与引用

新源：
`computations/root_20261116_request222_source_classification_repair.py`，
28224 bytes，
`20360bb001f3849b3468071b4ca6f7b4017d5aa2bb7fb476791316d1a96a432f`。

小请求：
`notes/current-C-coast-base-source-classification-repair222-request.json`，
9442 bytes，
`37f0b3b767eb233d2e714a143b4055e47dfc4629f2963e046b0511e05ba63672`。

工作流：
`.github/workflows/visible-current-C-coast-base-source-classification-repair222.yml`，
99393 bytes，
`312005867b9a144c04e2cc47afb7620de2d43b1ecb3f9f9ad2a509f8746458d3`。
它显式支持 workflow_dispatch，并保原 push 入口。公开 Actions 中发布成功
不自动等于科学启动，须另核正式 dispatch 返回的 actual run/head。

来源引用：

- [R505：原 220 完整来源与科学合同](../notes/2026-11-16-request220-explicit-coast-base-complete-chain-interface.md)。
- [R506：实际 220 分类错误的完整必要结论](R506-actual220-policy-JSON-source-classification-stop.md)。
- 原冻结 `root_20261116_request220_sampling_refinement_composition.py` 的
  `generation_specs/current_dispatch/compose/initialize/verify_runtime`；
  原 `geometry_20261116_request220_owned_roles.py` 的
  `bind_request/prepare/observe_records`。
- R503 完整公开政策计划及 R496 原生成器，身份见 §1。

本轮仅完成源码、JSON/literal 与字节工作；没有在本地 import、AST、
compile、fixture、科学运算或试验。Request 222 的实际结论另编号 R511，
只能依据其未来真实终态取得。
