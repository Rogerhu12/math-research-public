# HANDOFF — visible-flex-larger-amplitude

维护：ChatGPT /root（GPT-6 Astra Pro，AI-assisted）。**课题未完成，持续执行至全部README标准；不能在阶段、预算结束或下一步建议处停下等回复。** 每条结论立即推送；结果和原始身份以所链接正式笔记为准。

## 规矩与工作环境

规则同步记录：2026-11-15 07:14:11 UTC 真实 git pull --rebase origin main 后核双README；根74c08a36f6c997d0bc1e64a7956b42276f5fa5d7、题bff8aea253a9e6a7a4fac28d810ac454c5499fec未变，已读提交 1986ce1273dd6873b852c75043e4020e62bb3dc4。

只在公开 `Rogerhu12/math-research-public` 工作；全部科学计算、数值运算、科学模块导入及RHS/J/ODE/RK/优化只在该仓库Actions。本地只读源码/实际原标量、写代码/证明、语法与元数据检查、Git。PAT仅命令行瞬时环境，不写文件/提交/连接器/回复。

根137c5a的第15条：可由源和参数重算的数据、证书、Actions输出不存Git或Release；保代码、参数、run、SHA及诚实紧凑结论。课题≤200MB，普通main删除保留历史，不force、不改写历史、不分片绕限。旧Release迁移和publisher22e已取消。根第12条：完整证明直接results/index，不加独立冻结/复审/字节审计门。公式用$或$$。

每次push前及至少每小时真实pull --rebase；核双README blob，变化只读差异、立即遵守并更新上方唯一记录。NFF立即pull/rebase再推，循环至成功。root唯一Git/H/open/log/workflow发布者；子代理只在/tmp写草稿。

终端必须显式 shell=bash、login=false、workdir=/tmp。当前blob:none稀疏克隆 `/tmp/visible-larger-root-git-106`；旧workspace满且旧checkout无.git。rebase可清掉稀疏范围外的工作文件：用git show读已提交源，草稿留/tmp，git add --sparse。不开维护/gc；pull --no-stat、merge.stat=false防无关大blob读取。

临时工具 `/tmp/visible-larger-sync-push.py` 用RESEARCH_PAT环境执行真实pull、README差异检查、H记录和NFF重推；`visible-larger-api.py jobs RUNID`、`visible-larger-job-log.py JOBID` 只取实际元数据/完成日志。工具stdout科学值仅原值读取。本轮110运行中日志endpoint返回404，不重复探测、不重跑科学来拿日志。H<10000B、每MD<100KB、open宜<30KB；不写根LOG。

## 真正完成标准

目前只有大幅开放前缀接受。须固定g、连通闭C²嵌入与强C²的全t族；固定有内点H且diamH≥.2D；整像Hausdorff δhold≥.2D，含反射δE>0；全t reach≥.03D；全域相对metric算子误差≤1e−6。D取整个闭F0。冻结g/所有p/t范围后精化至机器或原solver容差，交数个各<5MB网格并明确数值到严格存在的缺口；最低标准后继续加强比例。不增六/九jet机器门。

当前M112/T112/N2048、699节点、453状态、236036free，前三core固定；scalar.99/cut.3/三控制，不能替T96或零H。四原输入及历史恢复见当前request。M96分量metric不是算子证书；每新模型fresh W/J，不跨模型相减merit。

## 正在推进的三条实际路线

### 110：同31查询的真实连续批次（运行中）

run43685348016 / source8d4a3af1d553cd85cfa9694ec8cfaf1c0b66ce3f / job132724561759，06:25:12UTC启动。sourcea1ba1cd8/requestef159a8a/workflow3363acf2；[完整接口](notes/2026-11-15-request110-same31-real-pair-batch-lifecycle.md)。最多8批、科学175min/job185min，每批原1-model1200s/λ270/512×200/17trial和全部门不变；必须新warm原FD通过才传同job真实warm/status。每批源/输入新评价，已消费临时数据删除，最后无raw保存。45min原规则监控保持。

107raw已删，110从actual98 artifact14147700690重建新支线；未读回110完成批。107同31原1/8接受/新FD通过，最近1/4仅已选LEFT464 RMS失败，仍非BVP/native，详见[实际107](notes/2026-11-15-actual107-same31-eighth-step-and-selected-left464.md)。

### 113：完整原始残差binary128（历史输入修复已发布）

103相邻词无改善，同freshJ完整R273后十档仍全拒，无finalJ/audit；见[实际103](notes/2026-11-15-actual103-neighbor-rejection-and-complete-R273-trials.md)，不是普遍精度底线。

[113完整接口](notes/2026-11-15-complete-binary128-native-primal-experiment-interface.md)：CPP1b59cd10/bridge3655c81a/probeba3564ca及28源pin不变。真实__float128113位覆盖e=L−target、226态RK、节点+αdelta及129248残差；原geometry/角表/scales精确提升。原noJ k/steps+cusp子步，不冒withJ n*h逐位相同或连续ODE。两root配置原8e−14/5e−12与1e−28/5e−27，先两base再十α；7200s只独立child，导出/额外64base/初J/R273另计，step320min/job350。partial/error后回同R273方向，原64的32×10/eta1/tol2e−9/finalJ/audit保留；旧64J不是一致128J，无新接受锚。

首跑run43687907457/source7308ea/job132732158878在首快照前从HEAD取已清理JSON失败，无J/方向/128残差；CPP编译成功，summary942b3c55，见[实际故障](notes/2026-11-15-actual113-first-run-missing-historical-input.md)。[工程修复](notes/2026-11-15-native113-frozen-input-restoration-interface.md)已发布 requestce294b5e/workflowdb8a479b：8bd26710原两ready只临时恢复到原client两env，ledger109004B/563a9997、stored29774B/c1c44f23，三科学源不变；owned只读父目录修权限清理。第二run43688981685/source8d68a39e79eb1f0c976868d69f87d27fa3f2acbb/job132735373768，07:13:29UTC启动；历史两件恢复步骤运行中，科学结果待读。

### 114已完成，115扩独立控制（exact_refinement准备）

106/108/112已正式，不能盲续旧半径预算。112仅六极小接受且末方向全拒，完整身份见[实际112](notes/2026-11-15-actual112-tiny-acceptances-and-final-twenty-trial-rejection.md)。[控制全链结构](notes/2026-11-15-small-core-control-structure-and-post112-options.md)已说明3p不是独立模态，圆R传播耦合全链。

[实际114](notes/2026-11-15-actual114-normal-correction-and-one-tiny-acceptance.md)：run43687426018/source dc032461b/compute132730710123/report132730985417。8方向155候选，仅dir5/trial14原接受，另7方向各20拒。W6958.225762769883→6958.225762766608；接受时inner tol=false，未加内层门。dir2全步已到后两式目标而第一式更差，故不盲重同策略，亦非无根证明。最终p与全值见note/actual114 recipe；全部final false，4487评价零异常/592J。summary86389B/c4eca98c（不含LF）、status7197627B/4e7ee4fa、trace7626013B/64a8e728；155核心外表完整，省略seed/frame等，非全status复核。

115准备第二实际支撑的θ·b₂(2x−1)，actual114末p+θ0；独立4控制profile/完整3×4 J/7×4正阻尼QR，原三式W/.2Armijo/真实域责任不变。θ是新设计参数，不冒固定g；原平方物理终检必须冻结当前θ为base后保持3活动p/K3/T112，重新付新标量域，不把k4冒旧方阵。函数独立不保证响应补秩。尚未发布新request/运行。

## 几何下游：实际接受场仍缺

R277/R278/R279/R280/R281完整证明已登记，不再加证明审批或旧fixture。R279有限完整jet→连续曲率条件，R280 joint端点门，R281两RP1图精确Sturm闭区间换门；它们不是当前场证书。109三有理例全匹配；111 depth2五叶全付、depth1两未付，偶重根准确保留。[实际111](notes/2026-11-15-actual111-exact-phase-switch-and-unresolved-budget.md)：run43685039861/source77d65ad2/job132723637032；summary7898B/7279b591。

[固定帽球及真实链边界](notes/2026-11-15-R281-actual-closed-cover-boundary-and-fixed-cap-balls.md)已发布 sourcea3ada50b/interface499e1078：从SHA绑定原shared plan/assembly精确有限graph导完整闭disk位置/法向球，归一化误差付清，原H只须有限，存储kappa只诊断。source-only/noactualfield。旧v3是静态base+R24，不是mixed consumer；worst≤128非全对。[完整活动jet球与mixed入口](notes/2026-11-15-complete-active-jets-and-mixed-phase-component-interface.md)已发布 source675ab8df/dbdedb45：准确共有节点/全FFT/B/materialcut/SE2表达自行求六jet，完整单位法向归一化；全部活动×两帽rank含未访问后缀。原phase_rule已核RαA∪C，共同cuff零弦仍为未付local责任。无实际场/run，未撤原static+R24。geometry续局部图/路径的完整责任。

完整闭面driver54079bcd/interface12d84a2a/workflow998ba5ad待真实fullDN+自身final audit/config/port：完整physical/material/z0/mean/ninejets/唯一SE2→R249首单元/shared quintic B/两帽；g不换成B′，held独立于reach预算全读。R274/R258adaptere372待同场见证。same-g v4冻结g/所有p/t，K=k=0、activep空、T=M/state4M+2；699二分1397+knots须prepare/fullDN两处max_nodes>1200。有限phi不冒有限theta，数值不冒严格存在。

## 已付事项与重做边界

95至114既往实际结果均已有正式note，勿重复旧审计。102v3整体model-vs-nested差异源于原writer顶层装饰，非科学门；104普通清理后课题168796207B，未知JSON未全分类，详见各note。未推草稿为115及geometry，无本地科学结果。下一实际结论立即写note/H/open/log并推，然后继续，不发阶段结束答复。
