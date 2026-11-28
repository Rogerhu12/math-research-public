# 第59批旧完整生成输出保全：81个分段中间件与4个完整派生结果

作者：/root/construction（GPT-6 Astra Pro，AI辅助）。日期：2026-11-28。

## 1. 本批结论和精确范围

本批为原始源码、完整参数、实际返回、后续读取关系和原字恢复均已有记录的85个旧生成文件准备普通退存，毛移除1,033,272字节。它们包含真实数值中间状态和派生结果，不能称为纯行政收据。根README第15节及本轮明确授权允许对这类可由完整已提交源码和参数再生的旧输出作普通提交退存；此前第56、57批只选metadata，是各批范围，不构成全局禁止。

这里只交付完整来源与恢复材料，不写引用、不执行删除，也没有运行任何科学计算。最终实施者须以当前树的路径、Git blob和长度匹配本批精确条目。科学源、证明、原参数、输入定义、实际资源记录以及现行科学分支均不在删除列表。

|生成组|文件数|毛字节|本批对象|
|---|---:|---:|---|
|cut Taylor，cell16至真实cut12，m2/m4|36|99,971|逐cell/segment中间件|
|outer Taylor，cells11/10，m2/m4|18|89,805|18个完整分段中间件|
|two-cell adjoint|18|234,193|18个逆序完成分段|
|cell11 adjoint|9|49,625|9个逆序完成分段|
|R97第六恢复窗口|1|126,530|完整full46源转移输出|
|三个真实端点共同质量两列|1|110,005|完整齐次点读出|
|R148对原cell9/8/7的后验消费|1|144,541|完整后验主包|
|signed46 geometry v3|1|178,602|完整几何生成主包|
|合计|85|1,033,272|全部由账本逐文件列明|

两个完整JSON分别为[来源与输入登记](../computations/legacy-exact-generated-outputs-retention-59-source-input-registry.json)和[原参数、实际结论及删除条目](../computations/legacy-exact-generated-outputs-retention-59-provenance.json)。后者的delete_entries就是唯一操作清单，每条同时带原blob、长度、恢复提交和已知SHA256。总表给本批所有工件的完整身份及扣除工件后的净容量。

## 2. 原字身份与完整输入恢复

85个候选的共同原字恢复提交为21f20cda2fc197ac87905980700a2d4a007fa3b2，课题树为b358e3957782cf8f649825d9ab7a887e24e8a6e2。每个候选均已从该树核到完整blob与长度。30个文件的SHA256来自已读的小型原manifest或原完成说明；其余55个没有可据的小型完整SHA记录，账中明确为null，没有读取大输出补值，也没有从运行成功、文件名或Git SHA1推算SHA256。

恢复某个候选时，按账本的restore_commit和完整仓库路径取回整个Git blob，保持原字节。来源登记中的输入有自己的恢复提交，不能假定候选提交或当前main仍包含以前已退的原始输入。多数旧输入明确恢复于60321451c058c6a51da58c37ae5ec6f2d1145f74；R83另保其已核的4bcf0ccd2d663f0b1aec4f264efd48959106e875。旧gzip也按压缩原字恢复，不先解压重写。

本批登记完整24个已全文读取的生成器、导入源、源码身份依赖及资源包装器，30个保留证据记录和82条分组输入恢复记录；这些输入记录允许同一文件因不同真实角色出现。旧ret44、ret45及R87的完整登记按whole文件引用，保留它们的全部源、原命令、配置、生成片关系和消费者说明，没有把它们替成简略参数摘录。

特别保留的原输入包括完整ready、原head/source ledger、原low46列及columns01–08、原port norms、所有真实源片、R87的全18锚、refined cell10全部9组、原M20 response和原family。原port-norms文件只是依赖，不在本批移除范围。parent91、唯一不可再生输入、ports/Nelder未闭对象和所有活跃输入均不纳入。

## 3. 四组Taylor/adjoint中间件

四个完整原入口依次是closure_taylor_cut_slope_v2.py、closure_outer_taylor_shared_flow.py、closure_outer_two_cell_adjoint.py和closure_outer_adjoint_source.py。实际命令、全部资源记录以及四份完整config对象已原样置入provenance。256bit、24阶Taylor、100余项位、160根预算及原initial-parts、全modes/cells、全输入和源SHA均不缩减。

cut Taylor的实际返回为exit0，261.737039566秒，峰30,384KiB；保留10项原门及全部7,533个Taylor片、16根括片、7,117次拒绝的记录。它只加强列出的齐次线性斜率，保完整真无穷列Wronskian和共同精确斜率余项。旧r1退出1的整个资源JSON也保留，不把较早失败抹成r2成功，不补未知失败原因。原数学范围见[R65](../results/R65-local-taylor-flow-true-wronskian-and-shared-slope.md)。

outer Taylor实际exit0，110.074442148秒，峰30,824KiB；cells11/10全部18段、两频率两基列、全局p/mu11与真正共享S0均保。它的完整forcing、外侧非线性问题和whole46/高频字段原本为false，继续为false。完整26,327字节终报告和两个completed-cell报告留在当前树，本批只退18个逐段件。

two-cell adjoint实际exit0，813.361701011秒，峰30,972KiB；全部10,793个原材料片、位置子片和两种终端状态读出均保。cell11 adjoint实际exit0，235.948048830秒，峰31,116KiB；全部5,545个原位置及9个逆段均保。它们各自的22,721和10,800字节完整终报告均留在当前树，完整外侧Green/Schur、full46和无限频义务没有因退存变成已付。

必须保留[R73](../results/R73-two-cell-signed-source-boundary-budget.md)的后续修正：旧two-cell adjoint的原中心值早于R63 far项E10,m的补充；其源核的历史范围不等于补齐后的中心结论。完整closure-two-cell-parameter-budget-r2.json（86,276字节，blob03ea82235831fd40dd6b377ed2b4f3e4b835f2a1）和原修正源继续留存。本账明确这条归属，不将早期中心值升级成完整全局证书。

这81个中间件确实可被原入口的--resume读取，所以并非“没有消费者”。任何历史恢复都要提供完整原状态、完整config及原列数据，原守卫不变。要重现最终结果也可以从完整原入口和全部原输入重新走其全段算法；不能用本账中的摘要代替一个数值checkpoint。

## 4. R97：第六恢复与第五窗口未知身份分开

本批只退2026-11-13-root-r97-full46-recovered-r1.json。完整11,395字节入口root_full46_source_cut_transfer_recovered_v2.py、四个固定whole输入、完整真实资源和[R97证明](../results/R97-full46-modewise-true-cut-source-transfer.md)都保留。四输入是完整R83、R92、R94、R78，原source严格验证各自wholeSHA。

第六窗口资源记录exit0、0.08721923828125秒和13,384KiB。源码完整保Fraction算术、192位向上dyadic、28位向上显示、全部213行、46偶模、3个高块、mean和single-cuff项；如aggregate门失败，其原入口退出2。因此本次原exit0的意义仅属于这个完整恢复入口。

旧第五窗口的原源码SHA仍未知。旧小manifest当时将recovered_v2标为prepared/not executed，是那时的记录；不能把这个后来完成的第六窗口文件反贴到第五窗口，或把未知原source补成f989a3f2。旧第五窗口的所有已知输出身份、实际退出与未解决的来源边界继续保在原manifest/final-state。新的第六窗口输出SHA256没有可用的小型记录，本账保持null，恢复仍精确使用其126,530字节Git blob06932b3a50e10ba53694e56639ef0f2f7d5c4700。没有据此宣称middle joint反馈、完整cut一致性或闭面完成。

## 5. 三胞元齐次点读出与严格旧审计

本批110,005字节完整主包来自inner_true_three_cell_two_column_point_homogeneous.py，其完整源码和三份helper/full input pins已全文读取。原5个输入的固定blob、wholeSHA和实际scratch别名都在登记中；原density、positive comparison、ready、cell12和cell13完整panels均可原字取回。

原实际为exit0，2.544522829秒，峰31,492KiB，7,799门。它消费cell12/13/14原9矩阵覆盖的每胞元11窗，保cell12/13全部1,873+1,975片和node15原半径包围。共同U+V输入质量只消费一次；点态Vprime是实际端点上界，不是全胞元下界。自身source、far、无限带、完整mean和逆仍未由此支付，不能称新的完整cut或闭面。完整[点读出证明](2026-11-13-inner-three-cell-point-homogeneous-r1-proof.md)保持原字。

已提交inner_three_cell_point_saved_audit.py严格钉原主包c10a92…、资源0ac54f…和原positive comparison cf2937…。旧独立审计的完整2,086字节输出及1,471字节资源也有固定恢复；其277门通过是原历史事实，本次没有重跑。未来如用该原审计，先恢复原主包和原资源的整个字节，不能拿新耗时或新JSON排序的文件冒原哈希。

## 6. R148后验：全部旧流与线性障碍范围

原8,552字节完整producer没有省略的数值CLI；它固定读取原R148 sparse posterior、实际资源和独立saved audit，再消费真实9→8→7完整主包、每个资源、全部profile片以及cell7真正completed segment4。source里的绝对scratch路径和全常量均保；完整ret44来源账保存其原目录/输入映射及全signed生产顺序。尚未入Git的原工作片必须由完整原生产者生成，不能从摘要构造。

实际4,842门通过，exit0，46.351416349秒，峰39,548KiB；全部3,930原子步（1,377、1,316、1,247）和46模都保。它以精确有理比例更新原初K不确定性，原初P误差为0，真实线性中心和原正profiles不替换，不是新的ODE求解。[完整证明](2026-11-13-exact-resume-outer9to7-r148-update-proof.md)保留cell7线性参考的严格下界|K2|≥0.066343455961862849>1/128，以及该障碍不等于非线性PDE无解的限定。

本批只移除该144,541字节主后验。三个更新cell cooutputs已在ret44退存，不能再次计入毛退容量。ret44中当时的retained_full_primary字段是旧树状态；现在由本批精确候选记录承接原字恢复，不静默修改旧台账，也不删除原proof/参数/资源。

## 7. signed46几何：完整原生成范围和后续有序读者

原完整closure_outer_physical_green_signed_profiles_v3.py生成同R88中心的真实m2/m4线性列、原m6…m40候选、全部20非零输入、mean及46输出。原resource完整保--chunk-rows32、--rss-kib98304、全部路径和其他原参数；默认256bit、Taylor24、根160、余项100仍由完整source保留。没有只恢复一个mode或一个summary。

实际exit0，1047.293958664秒，峰35,416KiB；全18组、原10,793个材料片、10,870个Taylor片和8根括片均由[原完成说明](2026-11-13-root-signed46-producers-complete.md)记录。69次局部拒绝由后续细化替代。此前其他丢失进程的终态仍unknown，不能据本次formal0猜旧进程终止原因。

7个显式输入、18个原R87锚、refined cell10的9个源组以及cell11的9个原源组都有完整blob/长度/wholeSHA恢复记录。源和whole input守卫均保。原554件、155,670,827字节生成目录manifest仍完整在树，其124,050字节正文没有在本轮读取。本批只退178,602字节主包，不碰这个完整生成列表，也没有把既有大量原工作片冒充成新的Git输入。

后续root_outer_fixed_centre_low46_ordered_v2.py按原两遍顺序消费全部signed数据、P/K/C/U、LR−Z0和当前片部分积分。原完成说明明确：未来完整重跑可使用新输出目录及完整新primary与实际formal0资源，但必须给新身份；不能改旧primary绝对路径后仍称旧SHA。若旧reader硬钉7b785c…，则先按本批记录恢复旧完整primary。没有从本条推出有序消费成功、外侧非线性解、46-cut自映或闭面完成。

## 8. 实施与未做的工作

固定候选树只是完整恢复锚，根实施时对fresh树逐条比path/blob/bytes，只删除完全匹配的85条，并将本批四个完整工件同次保留。并发改动不覆盖、不强推。台账不宣称已实施；最终实际提交和容量由根记录。

原全文源、全参数、实际退出和失败/未知、旧数值结论、完整输入恢复及已知消费者全部保。没有读取任何候选数值正文，没有读取或解压≥100,000字节/二进制正文，没有本地数值运算、AST、fixture、科学重跑或新Actions任务。源码阅读与文本哈希用于保全，不等于新科学进展。

重新生成是未来需要原输出时的完整恢复途径，不是本次退存前新增的机械门。只要历史reader要求原字，就用固定Git原字；若真正新运行产生新时间、RSS、gzip或路径metadata，诚实记录新whole身份，不编造与旧字一致。所有原数学及未付责任仍按原证据解释。

R167、额外linear-centre cut及尚未找到准确完整writer的Hermite M64/curvature24大结果不在这一批。它们不会因为容量紧张或名字相似而被纳入。当前保全优先交付已闭合、可立即实施的净容量，后续其他对象另立完整记录。
