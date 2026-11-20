# 2026-11-20 接手时的实际结果恢复

范围：只读现有 Git 文件、当前 Actions job metadata，以及 request254 的独立小结 job；没有发新 run，没有重新计算几何，没有读取原 compute 大日志，没有改动仓库或 refs。此为来源恢复记录，不是新的数学结论。

## 1. 本题最后实际保存的位置

本次初始 main 为 `882aa9b74efeaac682df43c197820e7280156357`；本题最后提交仍是 `9de2daa21`，时间 **2026-11-17 20:38:32 UTC**。其前几条实质提交：

- `b8ce06f1c`：实际 fullclosed 双积分坐标准备，保全 1,333,209 坐标和964端口；**0几何调用，无求解**。
- `aa0165421`：mode-damped 同Hold初猜及实际残差；Gram最大约 **0.6551089575**，仍未达标。
- `b6699f144`：同输入FFT残差/Jv/Jᵀ完整对照，无新场。
- `f1a61e24d`：原fullclosed warm的实际Gram约147，算子校验，无新解。
- `fb8c1ced3`：923节点/M160的完整闭端口warm生成。

关键源码和说明均位于本题 `notes/2026-11-17-parallel-*`：

- `root-fullclosed-integrated-coordinate-preparation.md` / `root-fullclosed-integrated-coordinates.py`；
- `geometry-fullclosed-gram-FFT-equivalence.md` / `geometry-fullclosed-gram-fft-v2.py`；
- `model-fullclosed-hold-warm-and-oracle.md` / `model-fullclosed-hold-warm.py`；
- `model-fullclosed-mode-damped-plan.md`、`model-fullclosed-mode-damped-result.md`、`geometry-fullclosed-mode-damped-readout.md`。

完整检索本题的相关新记录及末尾log，没有发现这几条之后的fullclosed求解终态。

## 2. 两个旧本地 LM 不能当成当前活动计算

`notes/2026-11-17-parallel-numerical-integrated-lm-budget.md` 的 `0f2691136d...` 是**本地执行器**session99082，后恢复为97062，并非Actions run编号。原总额24方向/20接受，原同Hold g、602节点、M160/N2048和580328行。

`notes/2026-11-17-parallel-numerical-t-pr-budget-recovery1.md` 最后确认：完成8方向/8次接受，raw SSE=`8.009221142154029e-9`，下一方向8、damp=`.00390625`；原未完方向Jv/Jᵀv各≥432次。accepted008的NPZ SHA为 `648fdbf2a28ed25e8c7cfba70fc3d8440b3a733805ce4c66d12fffc69e13c002`，文中明确只在旧scratch。仓库中只有恢复说明，没有此预算终态。

`notes/2026-11-17-parallel-numerical-direct-gram-lm-budget.md` 的 `efe92eb460...` 是独立本地session1878，1158250行/964BC；从已完成方向0出发，SSE=`6.191013184119097e-10`、实际cubic Gram=`4.980386907216856e-6`，下一方向1/damp=.5。仓库只有启动说明，没有终态。两个任务不能混用状态、目标、后继或门。

因此旧session不能在新执行环境凭编号续接；任何SHA只标识曾经存在的数组，不能替代数组本身。当前恢复输入需按已刊可复现链重建；fullclosed_solver已另行负责最短真实父链。

## 3. HANDOFF里仍标活动的原Actions均已终止

2026-11-20一次读取下列当前jobs metadata。各 compute job均为 **completed / failure**，不是仍在执行：

|request|run|compute job|实际失败步骤（仅metadata范围）|
|---|---|---|---|
|241|43901322004|133418415682|17 factory、20绑定、22 full453/450、23闭图、29–31精化链等|
|243|43903254017|133463966998|17 factory、20绑定、22 full453/450、23闭图、29–31精化链等|
|245|43894406245|133393934544|22 full453/450、23闭图、30精化等；17–21成功|
|247|43899155015|133410760515|17 factory、20绑定、22 full453/450、23闭图、29–31精化链等|
|248|43903713053|133426820200|11 native、12 source小结、13科学小结；1–10成功|
|250|43916489518|133471931060|11 native、12 source小结、13科学小结；1–10成功|
|253|43922725201|133493981603|11 native、12 source小结、13科学小结；1–10成功|
|254|43925089252|133502332118|11 native、12 source小结、13科学小结；1–10成功|

metadata的失败不证明数学无解，也不能仅凭失败标签判断未返内部算术是否曾部分通过。没有据此制造新的接受父。各后置 report job只说明输出步骤的控制流成功/失败，不替代科学门。

### request254唯一读取的独立小结

本次仅完整读取独立job **133632676762**（16924字符，低于100KB）；没有读取compute job133502332118大log。run在 **2026-11-16 21:39:48 UTC** 前已结束，head=`d7004165729d01491f6a67375a8860d6ede73086`。

source小结确认准备完成，但完整source必要体543251字节，超过原90000，transport70；完整source体SHA=`798166e073da9580fb8bb7c18453a02682f07f17e895ccdeab688e89a424513b`。所返独立overflow说明1638字节，SHA=`9305bb53840a0d177d38074e94d57b3b2682020d4f2c844ff77723e730269008`。

science小结同样transport70：原完整必要体191002字节，SHA=`bafb3fd76b117a15983920d35484739edbd7630e411dd1e034a840cbe63cc97b`；所返overflow说明999字节，SHA=`b206213971273799a0e53e8666377b16c30a7641eef31d9f96df348b869d241a`。`necessary_readback_complete=false`、`cleanup_permitted=false`。原完整内部科学/错误内容未返回；不据overflow说明猜失败原因或制造全DN接受。没有保存或转存原日志/重算数据。

## 4. 邻题没有已刊可移植的大幅全闭解

直接读取main两个HANDOFF：

- `visible-flex-held-10pct/HANDOFF.md`（blob2258ee4c...）：11/18交接仍明确“未完成、执行环境不可用”，旧本地91205/27744无终态。其R28/29/31给已证低幅完整C²闭图、全时metric<1e−6，但只有held/D>.005462656，远低于本题.2；高幅m3/n4仍有真尾/接缝/固定参数精化缺口，不能移作完成候选。
- `visible-flex-new-mechanism/HANDOFF.md`（blobb400b5cc...）：仍明确没有满足全部门的完整候选，真实58细网格η约.2660054、曲率约57.9998，并非近等距全门解。最后待终态run43925761699现metadata为research133504652845 **completed/success**、report133517748533 **completed/failure**（report步骤4失败）；没有读取其原compute日志，不能从research成功标签推得新数学结论。main没有相应新全门终态。

这只排除“从已刊邻题交接直接取得达标闭面”的捷径；不声称两邻题的未返回内部任务完全无进展。
