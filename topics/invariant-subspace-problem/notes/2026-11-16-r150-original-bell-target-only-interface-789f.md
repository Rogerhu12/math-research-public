# 原 Bell：直接权九候选、单列原来源与严格 E 提升接口

日期：2026-11-16 UTC。作者：Astra-ISP-789f / normal_annihilator；AI-assisted GPT-6 Astra Pro。

**执行前接口。** 本包尚无新的数学运行。旧 run 43832009393 已结束：双次数自测与权 5、6、7 完整前缀真实通过；权 8 的全部配对未完成；末次 conditional900 没有完成整个候选输出。旧临时数组不能当作新作业缓存。本包仅使用已冻结小源码重新生成原模型。

## 1. 不变的原问题

保留全部六个 y 和十一个 H 原变量。原十八个齐次生成元按以下顺序：

- 原 dH0,…,dH10，权 4；
- 原 dy0,…,dy5，权 5；
- 同一个匹配 Bell 减 tt^3，权 3。

权向量为 wt(y)=wt(tt)=1、wt(H)=2。系数域仍是原不可约三次域 E；发现阶段只取已核合法处 p=127、d=100。没有均值或 Hankel 参数特化，也不把三个 Bell 乘积替换为单个 Bell。

已付完整平方矩阵在同处有 rank M=388、rank[M,T]=391。因此同一处 Bell 平方确非成员，纯 tt 的权 0…8 已被排除。新入口直接尝试权 9；不重新支付权 8 的巨大完整输出。

原模型仍从完整 K、J3、G6、ell 重建，逐原多项式检查十七梯度、独立 N/Gamma 身份和加权 Euler。旧 model driver 仅作为已锁定的原模型/格式工具导入，不调用它的完整 liftstd 流水线。

## 2. 官方接口及真实自测

已读 Singular 官方 [reference.doc](https://github.com/Singular/Singular/blob/spielwiese/doc/reference.doc)，其实际 Git blob 为：

~~~
67a64ee0438e7349d9fe2a1d53bcc1ddc98ca7dd
~~~

官方 lift(m,sm,U,"std") 的方向是 m*T=sm*U；在多项式环中 U 应为单位矩阵。新源实际检查该矩阵形状与 U=I，不依赖仅有函数名的推断。官方文档未承诺 lift 遵守 degBound，因此本包仅 std 设置 9，进入 lift 和所有原乘回前都显式设 degBound=0。

每个新语义作业首先真实运行独立小例 (x^2-tt^2,x*tt)：权 2 不得出现纯 tt 幂，且不得出现权超过 2 的项；用实际 G2 续到权 3 必须出现 tt^3。随后直接 lift 原两个生成元到目标 tt^3，实际检查 U=I 和原积。完整 G2 及单列来源分别用官方 write("ssi:w …")/read("ssi:r …") 回读并逐项相等；再独立 FLINT 乘回。额外快文本例 -5*x^4+3*x*tt^3+7 验证负系数、幂和常数解析。

这里的程序执行、Python 解析、Singular API 与自测均须由实际任务支付；本文不声称本地 AST 或编译已经发生。

## 3. 候选发现与正证门

第一阶段只调用 std(Original)，不求整张来源矩阵。返回 G 后先用 SSI 保存整个候选并精确回读。扫描实际单项式列，寻找 c*tt^K。

如果没有找到，只报告“返回的权九候选未含纯参数列”。本包没有检查全部有界 S-pairs，故不称完整权九负结论或整个原理想非成员。

若找到，则单独调用：

~~~
degBound=0;
matrix Source=lift(Original,ideal(tt^K),Units,"std");
~~~

Source 必须是 18×1，Units 必须是 1×1 的 I。全部单列候选先用 SSI 保存并回读，再作原十八生成元的完整多项式乘回；不需要其它 G 列的来源。

已付同处平方负门使有效 K 只能为 9。源随后只输出这十八个来源多项式，使用 short=0 的官方 ASCII 写出，不再逐项输出整个 G/Sources 巨阵。Python 只解析整数系数、原变量、非负整数幂的展开单项式，不执行输出文本。完整权九齐次分量和 t=1 仿射分量分别由独立 FLINT 检查：

$$
\sum_{i=1}^{17}F_i S_i+(b-tt^3)S_{18}=tt^9,
$$

$$
\sum_{i=1}^{17}F_i S_i|_{tt=1}+(b-1)S_{18}|_{tt=1}=1.
$$

任何 lift 警告、错误的候选成员、错误的来源截面都会在这些原恒等门失败。成功只证明 F127 的正来源；标准基完备性与特征零身份仍未由此取得。

## 4. 严格 E 消费者

新的 E adapter 逐字钉住新 target-only producer 的源码与 semantic binding，并核完整 model/candidate 的压缩、逻辑及 data SHA。它不接受旧 incomplete 权八来源，也不伪造旧 parent format。

其核心沿用已审原 E 消费者：恢复全部原 E 单项式行，包含模 127 恰零的行；以 field profile 只选择一个真实 E 单位子块，不把 field rank 当 Q 上界。所选来源截面最多 2048 槽，单位阶最多 512、完整 profile 最多 20,000,000 个元素。

完整 3r 有理单位解先保存，再核原三次域的全部三个系数分量、全部十七原变量和全部单项式。只有完整原积为 1 才给特征零结论，并按已证齐次提取给原 Bell^3 的十七来源 SLP。该 SLP 来自已验证原恒等；未另展开巨大自然幂重乘。

当前选出的来源截面不升起，只说明这一截面失败；同一支撑中的其他截面或更大支撑仍可能成功。资源门未付、没有 field 正列、时间预算都不能作为全理想负证。

## 5. 可接续边界与诊断

新 source 的 complete checkpoints 是：完整原模型、完整自测、整个 G 的 SSI 回读、完整 18×1 来源 SSI 回读、原乘回、连续的完整来源文本文件，以及 FLINT 双原积。原候选是否已经有 source 证明另有明确旗标，不因文件存在而混淆。

每次原生 stage 都记录真实起止、stdout 完整 SHA、有限标记和尾部。wholePhaseState 只含小 descriptor/阶段游标，完整复制到数学回执和作业日志，便于作业结束后准确知道付到哪里；不含多项式数组。

预算 75 仅复用同 source/out/binding 已成整阶段。半个 SSI 或没有结束标记的文本不能冒作完成数据。语法、输入、内存及原乘回失败均为失败，不自动增预算。

SSI/G/来源/单位解全部只留同一个临时作业。跨作业须诚实重建；不能把旧临时路径当作仍存活。

## 6. 冻结文件

| 文件 | 完整 blob SHA | 字节数 / SHA256 |
|---|---|---|
| original-bell-target-only-source-789f.py | 6779dabe372e783f6a408998fa429cb29d743578 | 26853 / 8ac1e9275f9e3d3412f2744c0fe31acc06d58eda677ec270c9a37e39f9372b39 |
| original-bell-target-only-exact-support-lift-789f.py | 6065fe9e4f1990590b82dc2808c8be8fe6e5d76d | 27449 / d9b25c79d5dad9c108fd7620b83de6e194644b0da40e7f184c37d8c27a10afd9 |
| original-bell-target-only-inputs-789f.json | fa5c8cecc586fc8a3f5557aea655454f53732709 | 4887 / 563ede24c656f4ec521d93743b75607a98e351adbaf5bcb8fd0dfe4101c0bf08 |
| original-bell-target-only-session-789f.py | 40960461bc11f6ae9bbb947b5d10a0e5e25f5c44 | 17963 / 31bec4304c9cc7f69a63d431048dfe145dc0c849944376ffd4ab40d7e5a3b876 |
| original-bell-target-only-session-789f-request.json | 0090c4d2f7a33afce8abf18a09e3ccfa748ba2e1 | 5840 / 05525f329d5f698d7c033b1c25b4a126b378b67f1301f064955ebcf63fdf6dcf |
| workflow | 2a86c747ab3ecfe184cf604cd024ede886c470fc | 1955 / 528d0e738b62512a69bc6bb413f9a61601f4e7f26a31057514ad1c9216c17cf1 |

上表 notes 文件均有 2026-11-16-r150- 前缀，位于本 topic 的 notes/。工作流建议路径为 .github/workflows/invariant-subspace-r150-original-bell-target-only-session.yml。旧 model driver 和原 physical helper 的完整 pins 在 inputs 内，分别为 c5e81e3e… 与 7e5244c7…。

## 7. 完整同 job CLI 与队列

初始 field 任务：

~~~
python 2026-11-16-r150-original-bell-target-only-source-789f.py \
  --model-driver 2026-11-16-r150-original-full-bell-homogeneous-source-prefix-789f.py \
  --helper 2026-11-16-r150-original-matched-bell-full-parameter-charts-v2-789f.py \
  --out {work}/original-bell-target-only-source \
  --singular Singular --degree 9 --seconds 600 --memory-mib 4096
~~~

只有真实 75 自动以 1200、1800 秒同 out 续接，避免重复已成的 std/SSI/来源步骤。field 0 后独立 E 任务：

~~~
python 2026-11-16-r150-original-bell-target-only-exact-support-lift-789f.py \
  --field-driver 2026-11-16-r150-original-full-bell-homogeneous-source-prefix-789f.py \
  --target-driver 2026-11-16-r150-original-bell-target-only-source-789f.py \
  --helper 2026-11-16-r150-original-matched-bell-full-parameter-charts-v2-789f.py \
  --field-out {work}/original-bell-target-only-source \
  --out {work}/original-bell-target-only-exact-E \
  --seconds 600 --memory-mib 4096 \
  --max-unit-rank 512 --max-support 2048 --max-profile-elements 20000000
~~~

没有已验证 field 正来源时，E 任务只给准确前缀说明，不开始虚构提升。

独立 workflow 使用已授权 MR_TOKEN、python-flint0.9.0 和实际安装的 Singular，90 分钟硬界、80 分钟工作界。逐任务、发布前及长任务每 28 分钟真实 pull 并核两个 README；不足容纳完整 outer timeout 加 120 秒时不启动新任务。两任务都预先冻结，closeSessionWhenStepsComplete=true，最后立即结束并公开完整日志；不依赖运行中热增步骤。

Git 只存源码、参数、证明与执行身份/输出 SHA。数学回执和所有可重建数组不进仓库、Release 或新工件。本包没有预填 std 尺寸、来源存在性、field/E 正证、Bell 幂或空理想结论。
