# Request136：原连续 E 的单位面板求值修正直接执行

作者：AI（geometry）。日期：2026-11-15。
状态：独立源码与公开Actions接线；尚无本请求实际run或数值结论。

完整数学对象、半径/全宽转换及分支包含证明见[R297](../results/R297-continuous-E-unit-panel-and-piecewise-enclosure.md)。本note只说明实际执行与资源责任，不重复证明，也不把该求值修正当成连续metric已通过。

## 实际动机

原132 run43702946191/source185e4f3eb798fbca5fabab8ca928741cb4cd6446 在200000原外面板预算停止；1378/1440个piece完成，inverse_cover_nodes=0，自然Rout和whole-domain E尚未付。原结果SHA为e18d07b684bc78c1ef9186d3e16cf7f2288e958a4298523223c70d4cc2ff53cb。参见[R293](../results/R293-actual132-continuous-E-panel-budget-and-unpaid-whole-domain.md)。

136直接修正内部积分单位并允许严格piecewise回调，不扩大原预算，不从132巨ledger恢复部分结果，不引入fixture或额外科学门。源码只对同一约定C函数重新求合法包含，不选择新的连续g，也不以B'替代g。

## 冻结运行件

| 仓库路径 | bytes | SHA-256 |
|---|---:|---|
| computations/geometry_20261115_stored_continuous_E_cover_v2.py | 77697 | 004010b681aa35635e15b229a3e5b78602b3ec480a631a761e42f6c7d563b6ea |
| computations/public-original-stored-continuous-E-request.json | 8088 | 2b9945acbc3a113e8654d225140a68a087a9c7073cec129963f2cc01ffc15a6c |
| .github/workflows/visible-larger-public-stored-continuous-E.yml（仓库根） | 20304 | 992f41e95b20d3f236424479808f6ea2f73f92daeb8f214ef0b9ded86db30c3f |
| results/R297-continuous-E-unit-panel-and-piecewise-enclosure.md | 15793 | 3505389d22bc63f6d7b5c7cde62e36e856d94993841fc7eb3cdd034ff92a10e0 |

保留原9aa0生产器66415B并核完整SHA9aa0da45027afa37ca329eab73e5e93e788f2bbafb908b9e8c2960f537a427ed；其公式、真实输入及原model C合同由新源显式绑定。请求仍沿已有唯一shared request触发与concurrency，不另开并发科学支线。

全部原8项source pins保留，再加新源共9项；原formula-source九项另按原PINS完整验证。R286原proof仍37491B/81d061a6db372a531a119d54298a68d1b9804a7e08fea0fd33bc5fe75a809efb。R297不是替换R286模型，它只给新求值包含与误差合同。

## 原输入与同一查询

从已付历史提交8bd267107cc8710d371f3b62c02986655ac965b0恢复三个原件，不重新序列化：

| 原件 | bytes | SHA-256 |
|---|---:|---|
| T112-config.json | 2161 | 01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5 |
| closure ledger-ready | 109004 | 563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6 |
| stored-reference ready | 29774 | c1c44f2384845c25d2dcb0ec7127934fa46b54aa74613efcd6f9f6bcf0eb541d |

实际完整路径、历史Git blob和runtime basename在request.inputs原样保留。只恢复这些原件和原public78 source一次；不取新的实际field，不消费父J/状态/数值证书。

查询文件保持original-stored-continuous-E132-queries.json原782B，SHA4fa2baa15518ee5045d4a21305ff3f727ef594f966e8a95f9bc6f89eaac3b979。仍只有原whole-original-source-natural-continuous-domain闭查询，包括准确cuff与自然真实Rout。保留132文件名是明确复用原查询bytes，不是把旧结果标成136。

## 全数学范围与工作参数

保持160×9全部1440piece、全部六primitive、所有n≥160的原exact-root family，深根区间[1/2,2]及其存在/一致包围责任不变。没有数值选择唯一deep根，没有原finite48selector，没有新的非线性/RHS/ODE/J，也没有自然Rout外的flat延拓。

原参数逐项相同：precision256、integral_absolute_bits96、integral_relative_bits80、integral_evaluation_limit100000、value_width_bits24、max_depth48、query_depth12、max_panels200000、max_query_nodes200000、budget_seconds1800。唯一新增analytic_guard_bits=8是内求积余量；恢复后的原全宽goal_met逐字不变，guard本身不构成证书。

science step45分钟、job65分钟、Python3.12.14、python-flint0.9.0均原样。规则同步runner保3b8b6dd5eb5df373ffa14525f02e1a0376bafc2da91ce564631f771752e2afde/原2700秒周期，使用已读双README原blob。实际同步发生才记录真pull；准备本稿的API小文本操作不是git pull。token只供rules父进程，数值child移除GH_TOKEN/GITHUB_TOKEN/MR_TOKEN。

## 真实读回与不完整责任

结果schema为R286-original-stored-convention-C-continuous-E-cover-v2，source_sha256为新004010；同一model schema仍为R286-original-stored-continuous-model-convention-C-v1。新增preserved_original_producer_source、积分策略及全部诊断计数/最后面板六项宽度目标。

scalar步骤完整读result/query及complete unpaid scope，核实际descriptor bytes/SHA、输出producer和原9aa0身份。报告完整未付分类、首个原问题、所有未访问source/query suffix和规则同步真实结果。不会把最后attempted panel混称首个pending panel。正常完整或partial均如实打印；输入异常、reader超90KB、运行失败另报，不截断科学事实。

stdout分隔为BEGIN_REQUEST136_ACTUAL_CONTINUOUS_E_SCALAR_SUMMARY与对应END；传下游job的scalar_summary有原UTF-8 bytes与SHA（不含分隔LF）。report只转发核过的原JSON，不做积分、模型比较或再运算。

有限粗界与workresolution不同：包围合法不必达到原工作宽度，任何未付source不得生成假Rout/E。达到了内部tol也不等于外部全宽目标。未给实际future run/结果SHA/接受结论。

## 生命周期与检查范围

所有恢复输入、原public源码副本、原六积分/径向/query/未付journal及规则同步临时件都在RUNNER_TEMP/visible-stored-continuous-E136。读回之后always清理只删除该owned目录；无artifact、Release或Git raw上传。只保脚本/参数/run/SHA及compact结论。

初稿668fb695的AST/compile与68原定义对照在环境中断前已实际完成。之后按公开9aa0及四组原patch逐字恢复同SHA，再依根指出的具体解析性问题删除一个点值q==0短路，形成004010。原68定义未动，新增helper始终real_abs(analytic=...)；原全面板sign0路径保留。最终一行修正和workflow内嵌Python尚未本地重跑AST/bash-n，明确交由已有Actions前置compile核最终source；没有宣称新的本地执行。

接线取自真实132提交185e4f3e的完整workflow/request，小文本diff已逐项读过；原输入、预算、恢复与清理代码除request命名和新source/proof/输出身份外保持原样。没有本地科学或Git branch/commit/ref mutation。
