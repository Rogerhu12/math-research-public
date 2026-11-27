# Artinian v7 的实际终点与商域表示修正

日期：2026-11-27（UTC+8）；会话：Astra-rank2-Sha-0b097461-20261127，geometry。

**状态：原 v7 已失败，准确原因为有限域表示的 API 假设，不是超时或 OOM。
原 F 的完整几何、四交和 shadow 没有 PASS。**

## 1. 实际运行回执

- 原 source：`6e79456aa2250a589306ba39d983ecdc46a2f267`。
- [run 45838674625 / job 139974211422](https://github.com/Rogerhu12/math-research-public/actions/runs/45838674625/job/139974211422)。
- job：2026-11-26 14:24:24–16:20:03 UTC；数学步骤：14:25:04–16:20:00 UTC；结局 `failure`，host 返回 1。
- GitHub job logs 原始字节（含原 BOM）：4,060,943 B；SHA-256
  `00a364947dc153704528b5a9ef9b857c9a51bbb820d8c742e373d588da359819`。
  日志只在临时目录读取，不入库；上述 API 及 source/run 足以重取。

已实际返回：两原特征零 PASS 认证、全部原正规化乘法与七个椭圆方程，
以及第一张图的 1530 长度厚商预检中的完整 Fitting 分离、整单位逆、
带共同零点的完整分式图和第一基素因子的完整范数层。
最后一条成功阶段是 16:19:56 UTC 的
`original two-chart relative thick norm preflight: pi 1/2, entire H_2`，
整个 306 行 HNF 已返回，商长 306，数学 elapsed 6884.487 秒。
第二个基素因子的商域构造随即失败；这既不是双图预检全部成功，
也不是原 F 的零极除子成功。

准确异常位置：

```
original_ys_artinian_norm_tools.py:524  ActualFiniteFieldQuotient(pi, ...)
original_ys_closed_point_tools.py:119  native_absolute_degree(self.field)
original_ys_closed_point_tools.py:50   card(field) == p**field.degree()
```

异常消息为 `Expected the original native absolute finite-field model;
degree() is not its degree over the prime field.`
`RANK2_TRIANGULAR_ARTINIAN_FAILED` 记录 elapsed 6884.976900202 秒。
后继不得简单重启这份未修改来源。

## 2. 确认的实现原因

`ActualFiniteFieldQuotient` 原先把 `P.quotient(pi).field_extension(...)`
的返回一律视作绝对有限域。Sage 对非素有限域上的多项式扩张可以返回
一般多项式商域；它的 `degree()` 是相对次数，故该返回不满足这里为
绝对坐标编码所需的断言。简单删断言或用相对次数代绝对次数都会误读
后续的坐标、Frobenius 次数和完整残余域次数。

已读官方资料：

- SageMath 10.6 原源码，
  [`polynomial_quotient_ring.py`](https://github.com/sagemath/sage/blob/10.6/src/sage/rings/polynomial/polynomial_quotient_ring.py)，
  `PolynomialQuotientRing_domain.field_extension`。
- SageMath 官方
  [finite field extension 文档](https://doc.sagemath.org/html/en/reference/finite_rings/sage/rings/finite_rings/finite_field_base.html#sage.rings.finite_rings.finite_field_base.FiniteField.extension)：
  对非素底域给多项式时会退回一般商环表示；给整数扩张次数则返回绝对有限域及底嵌入。
- 同页 `free_module` 给指定底嵌入、指定基的向量空间双向映射。

后继须保留原 `P/(pi)`、原底域嵌入和全部正反映射，
另给符合真实绝对坐标接口的表示；不能只更改断言、抛掉二次常数、
任意替换原 omega，或用素域范数代原二次域范数。

## 3. 当前后继

正在构造并证明显式保底域的绝对有限域表示；仅修改相关表示层和真实入口 pin。
全部 306 行、厚度、两个图、原参数与完整 shadow 门保持。
在相同 Sage 10.6 上先执行针对这次真实 API 故障的有限域表示小入口；
它成功也不代表原大链通过。

完整表示同构与厚范数返回已证明于
[R974](../results/R974-original-residue-native-model-and-complete-norm-return.md)。
其第 6 节另追清了人工 1530 长度预检的数据流：它不向原 F/P、四交或
shadow 提供对象，只提供一个单独的 API 回执。按根规矩第 12 条，
后继将把它改成默认不执行的显式选项，并准确记录未执行。
实际原几何和每个厚层的数学返回门不变。v7 的 6885 秒中，
前约 4809 秒是真实来源/正规化/maps 的重生；首图人工预检约耗 2076 秒，
第二图人工预检尚未执行。不能把此前全部 115 分钟都算作人工预检开销。

针对这次真实失败的 API 修正已经在
`run45881262808/job140120885101`（source `cd89412822ef2497f97891969248bfdcc23b52fe`）
实际成功。完整日志 26,655 B / SHA-256
`a1f43397f9376521c630be7562831d6c74de31f8e6400f9366314dfa33afbd1d`；
RESULT 8,315 B / SHA-256
`99ec7d327ac73cfb354805c3fd6397ef0ccad40192956bc55790d06e8750a27a`。
详情见 R974 第 7 节。生产原大链未据此宣称成功。


## 4. v8 的真实终点：原 Frobenius 仍是未完成阶段

2026-11-27 01:05:50 UTC，run45882239615/job140124138541 已完成且 failure；source 为 3b0fe32226b1f91ec37ef68a8d53ff865e9d9b26。数学步骤19:15:47 UTC开始，01:05:47 UTC在21000秒外层 timeout 下退出；01:05:47.9804494 的真实 runner 行明确为 exit124，host 同时记录 signal15。不把它称为数学反例、OOM或通过。

完整最终日志为15,338,257字节，SHA256为0f152e20586ada434972be34134f9632f71ce409dda080948a3ed4f95b479951。日志只留临时工作区，不入仓库。

本次原 maps、两图运输、全零/极 degree612 已经过；positive 三个base-prime的完整厚分解均完成。negative base-prime0的四个真实厚因子分别长2、16、578、16，最后一个于00:42:58完成。随后 negative base-prime1 的306维残余 Frobenius在01:03:46明确完成169行；最后01:05:46仍在原完整306乘法算子的第1538次认证，elapsed20986.06。没有四交、全厚Norm或18×9 shadow的最终回执。

## 5. v9 只接已证明的同原输入后继

[R1008](../results/R1008-complete-original-linear-fiber-frobenius.md)保留v8入口和全部原验收，改变真正瓶颈处的完整线性纤维实现：实际一次根、原常数生成元/omega、两图权、所有46971乘积双序、全部306单位和半线性Frobenius均返回。另完整接入R975的七个全行模aliases及R986的两个原剩余域constructors，未删厚度或范数目标。

待本提交触发的v9仍为r29/q2453/batch64/minimal、shadow、两份原char0 PASS，Sage10.6固定镜像、离线数学/只读源码及host独占read token。source manifest从45份增为49份，新增完整wrapper与三份实际helper。request schema为rank2-original-triangular-artinian-request/v9；linear_algebra为r1008-whole-linear-fibers-pair-reset-native-norm。保21000秒数学/360分钟job和同一个不取消在运行作业的concurrency group。只有v8真终点已取得后才接入；不与其并发启动。

本地仅作AST/JSON/YAML与所有source pin检查；不把这些静态检查记为新数学PASS。新run/source/日志终值须在真实产生后追加。

实际v9已由push触发：run45920983633/job140251398928/source1eeab95eb057de2b6ea6753ff9e36a18bd20bbd2，01:09:56UTC创建；截至01:12UTC checkout及固定镜像成功，原数学step4 in_progress。第一次日志请求返回BlobNotFound，未据此猜数学阶段或PASS。


## 6. v9 已取得的真实首段：仍在运行

2026-11-27 02:36 UTC已读取本次真实日志快照，共4,203,353字节，SHA256为32c6c5f3e7526b4f18883a4563b41f7de53159e55bbbb3e5988e2e9a075c1dc3。日志仅在临时工作区；以下均为已输出的实际阶段，不是workflow回显或预测。

01:10:50两份原characteristic-zero PASS完成认证；本次source仍为1eeab95eb057de2b6ea6753ff9e36a18bd20bbd2，wrapper仍为aec8056ca7cda7a6ab60157aeddd1051dc14b18255e15e0749616db9692ddfdc。原完整乘积块于02:23:46.974完成；实际specialised prime Frobenius从02:23:47.001的第1行到02:23:48.778的第306行，elapsed从4376.793到4378.570，native_constant_degree=2。

快照末尾为02:25:13.119，positive/base-prime0/actual maximal ideal0的完整Hermite已到272/306列，remaining_determinant_degree=0。作业仍在运行；这不是四交、全部厚Norm或18×9 shadow最终PASS。继续消费同一个run45920983633/job140251398928，不启动重复重作。

## 7. 大日志读取故障与限定只读后继

03:05、03:11及03:41UTC专用连接器的完整日志读取均Transport closed；03:41的step4 metadata仍in_progress，不能据它改写§6的实际数学阶段。

为取得原字节快照，新增只读脚本`fetch-original-v9-log-snapshot.py`，固定原run45920983633/job140251398928/source1eeab95eb057de2b6ea6753ff9e36a18bd20bbd2；先核绑定，再GET日志，全字节SHA256/长度并仅输出12000B尾，不写文件、不重算或重启原作业。源码5631B/SHA135b297e0c5ef822f0091c084f32909e6c908fa65db9eb8447f60f8123dba74b。

首次collector run45936742717/job140301575119/sourcea215d51b0c405ccfc33a6cf4c008662971f89e0b在03:53:26UTC实际返回GitHub API HTTP403，collector状态API_READ_ERROR、原数学NOT_ASSESSED。原v9没有因此失败或通过。

后继仅给原small workflow增加actions:read，并在执行step以`RANK2_ACTIONS_READ_TOKEN: ${{ github.token }}`传入内置只读token；不使用用户PAT。脚本仍先匿名，仅401/403才在GitHub API回退该token；下载302改用全新无Authorization请求，不打印签名URL。请求仍固定同一原run/job/source，无新数学运行。实际新快照待回执，不预记阶段。

## 8. 只读后继取得的真实第二快照

2026-11-27 03:57 UTC，collector run45937094533/job140302696286/source d9394ebeb6d5067ae8652d487468fe5ab9f0c7fd 实际success。源码仍为§7的5631B和同一SHA；stdout13858B/SHA5ceec4b08fe1712c9f37524313f606a84d9985d29585faaaccfc92432fe655e1，exit0，outputs_persisted=false。匿名403后实际使用内置只读token；日志下载请求没有携带该Authorization。

所读**原v9**绑定仍严格是run45920983633/job140251398928/source1eeab95eb057de2b6ea6753ff9e36a18bd20bbd2。完整原日志12,606,719字节，SHA256 a310249c57177996b7496ee1fba79ddc1ec7faea02e51cbed030551551facfef，Content-Encoding为identity。脚本流式hash全部原字节，仅在stdout返回最后12000B；不将这份可重算日志存入git。

真实尾的时间为03:42:43.6590447UTC，标签`all original cusps:positive: base-prime 2: actual maximal ideal 2`。已提取Hermite144/306列；随后同尾记录第145列前的完整gcd pivot/whole Popov tail reset，剩余determinant degree1，未将它记作已经提取145列。原run/job/数学step4仍in_progress。

这准确推进了§6的实际阶段记录，但没有四交、全厚Norm或18×9 shadow的终值，也不据日志缓存的末尾时间推断当前执行停顿。继续同一原作业，后续只读摘要无需重算数学或再次获取连接器大响应。

## 9. 同一 v9 的真实第三快照：负向首基素块

2026-11-27 04:27:13UTC，collector run45940009036/job140311911688/source9af127b37bbe87f2cb59418168c12fbe1dfad22f 实际success；源码和固定原run/job/source仍逐字不变。collector stdout13832B/SHA202012bf530d61da302840cecd64e8d0b9c7b5e7d4a566cece33f720106d8051，exit0，无输出文件持久化。

原v9完整字节快照16,808,131B，SHA256 0ef65d77c81711e193b7bd91edf7bdfffb0610dc71e9e82a86184640258561f4。真实尾为04:26:47.7119125UTC，标签`all original cusps:negative: base-prime 0: whole local primary factor 3`；已提取Hermite78/306列，随后是下一列前的全gcd pivot/whole Popov tail reset，remaining determinant degree16。不能把该reset说成已经提取79列。

原数学step4及run/job仍in_progress。此尾证明已到上述负向真实厚因子；它没有包含四交、全厚Norm或18×9 shadow的最终回执，也不以程序顺序猜未读取的最终验收。继续唯一v9，无数学重跑。

## 10. 第四次只读快照准备：保完整终点标记与非零字段

继续同一个run45920983633/job140251398928/source1eeab95eb057de2b6ea6753ff9e36a18bd20bbd2，未重启或重算原数学。只读helper增强为11472字节，SHA-256 `34e10e38ceda6a5ff0c79f491461cbabd5d81bd629cf72b5b373279b11050a5d`。

除原全字节计数/hash与最后12000字节外，下载时逐行读取原代码实际发出的 geometry/intersections/shadow/base/triangular/linear-fiber 终点JSON。每条完整payload保准确字节数和SHA、原始status/布尔门、真实nonzero字段、必要长度账与原emit SHA的匹配情况；未结束行不冒作完整JSON。失败标记和host退出也分别保留。全部原JSON只流经内存，不写输出文件，不打印授权或签名下载URL。

这里已对照唯一v9固定源码：`every_original_geometric_gate_completed_with_exact_successor_bindings` 仅说明外层完整，真正非零须读取原SHADOW/base中的 `original_rational_AJ_detected_nonzero`。collector只投影原字段，不自行推断数学结论。本次真实回执待取得，不能用新reader的存在预记原几何通过。

## 11. 第四次真实字节快照：2026-11-27T04:57:47.0676014Z

collector run `45942929589`、job `140321076833`、source `ec0b092ea48e318d541d26036dddf6d6d6d9b8c4` 实际成功。原v9仍是固定run/job/source，run与数学step4均 `in_progress`，没有终结conclusion。

- 原完整log：18909009字节，SHA-256 `b047820576e07c796e4190dc2e45cc4b2e2c200dca647db7f1f4a0201aa76ea7`。
- 实际可读尾止于 `2026-11-27T04:44:40.1180880Z`，`all original cusps:negative: base-prime 1: actual maximal ideal 2`，Hermite已抽44/306，下一完整gcd/Popov reset已过，剩余determinant degree 8。日志可用尾与读取时刻不同，不据此预测未读阶段。
- 本次完整终点JSON投影为空，parse errors为空、没有未完成尾行；没有四交/全厚Norm/完整shadow终门，更没有原nonzero字段的真实返回。
- collector stdout：14055字节，SHA-256 `5ffd460153aaf6320b1ddd9b1a77becbc1f3c2e8ae6a6f90d86c174bda5518e9`，exit0。源helper SHA仍为§10所记。

本次只读全字节，不重算任何数学，不保存原log或可重算数据文件。唯一v9继续运行，完整终点和原nonzero值仍待；不把collector成功当几何PASS。

## 12. 第五次真实字节快照：2026-11-27T05:27:14Z

collector run `45945876436`、job `140330328944`、source `fc1211c0a08fd9643ade3132e07edd78fc765f3f` 实际成功。同一原v9的run/job/数学step4仍为 `in_progress`，没有conclusion；helper仍为§10的11472B和相同SHA，未重算数学。

原日志共23110630字节，SHA-256 `748bdb5eb859af6c6659a5195842c720bc44871899080c2ad2520a7e171fbba0`。可读尾止于 `2026-11-27T05:17:48.6613019Z`，实际标签为 `all original cusps:negative: base-prime 0: whole local primary factor 1`。Hermite已经抽取188/306列，随后记录第189列前的完整gcd/Popov reset，剩余determinant degree2。此处记录实际标签，不以先后次序猜测未返回的其它全部块。

完整终点JSON、host终门和parse errors仍为空，未结束尾行0；没有四交、全厚Norm、全shadow或原nonzero字段的最终回执。collector stdout14046字节，SHA-256 `1bc51aa1bbf122c3717bff269a136b75bbd74ab74181b5b5ad5fd2222974f2a8`，exit0、outputs_persisted=false。原全部字节只经过流式读取，未存入git。继续唯一v9，外层collector成功不当数学PASS。

## 13. 第六次真实快照：2026-11-27T06:01:27.8682625Z

collector run `45949222673`、job `140340910080`、source `5f2df4435c2d435598c30aaccbeb2ec3ef9ddf0e` 实际success。原run45920983633/job140251398928/source1eeab95eb057de2b6ea6753ff9e36a18bd20bbd2绑定不变；原run/job/数学step4仍in_progress，未返回conclusion。

原完整日志27312505字节，SHA-256 `22371d0db0a1f1b380fd3245a20a3df190a530d2850ecc6614b5e255c094aff7`。可读尾止于 `2026-11-27T05:52:25.0945895Z`，完整标签为 `all original cubic branching:positive: base-prime 0: whole local primary factor 3`，Hermite已经抽取225/306列，剩余determinant degree2。此标签与§12不同，但不以程序顺序代替其它块的完整终门回执。

完整终点JSON、host终门、parse errors均为空，未结束尾行0；仍没有四交、全Norm、全shadow或原nonzero字段的最终返回。helper保持§10的11472字节与同SHA；collector stdout14069字节，SHA-256 `b98c80154a083356c7f995c6a541e390c4a89f07edd4fdcc3f1d58cf9a5adc58`，exit0、outputs_persisted=false。只有流式只读，无数学重算或原日志文件提交。唯一v9继续。

## 14. 第七次只读快照与未激活的完整 projector 后继

2026-11-27 06:29:11.5254128UTC，collector run45952136806/job140350212654/source3bc9c96dfad511c56be4487c1340cfe68fc99a21取得原run45920983633/job140251398928/source1eeab95eb057de2b6ea6753ff9e36a18bd20bbd2的完整日志31514035 B，SHA256 eef3c1abad50318fb3e445e225e89071431b8c251eedb0f5f4e1ee397ae0ff59。原run/job/math step仍in_progress，completed_at/conclusion为null。

末行06:25:55.5503043UTC，all original cubic branching:negative: base-prime 0: actual maximal ideal 1，Hermite138/306、剩余det degree1。全部terminal记录为空、无解析错误、无半截末行；不能据阶段名称推断未读的四交/全Norm/shadow终门。

collector仍为11472 B/SHA256 34e10e38ceda6a5ff0c79f491461cbabd5d81bd629cf72b5b373279b11050a5d；实际stdout14049 B/SHA256 35045042e81ba48a0d81bb1d2aaf339c30ff5630b96acf09f7339a2618e8c8d3，exit0，outputs_persisted=false，mathematics_recomputed=false。请求id为2026-11-27-0631-original-v9-readonly-terminal-snapshot，实际回执时间如上；它不是数学完成回执。

[R1033](../results/R1033-complete-residue-and-thick-projector-hermite-return.md)已证明原剩余核/整个厚projector的直接Hermite，并备新源码与未激活v10请求。旧活跃workflow/request均未改，未启动第二个重数学作业。唯一v9先运行到真正终态，之后消费完整终点再决定后继。
