# 交接

## 目标、授权和同步

证明绝对常数 C，使全部无 CM 的 E/Q 在 p>C 时模 p 满射；或构造 p→∞ 的完整反例族。**主目标 OPEN，QUEUE 进行中，持续研究，不等阶段回复。** 会话 serre-uniformity-resume3；日志 Asia/Taipei。

已读规则提交：65be19eee5cd08491179f296cb6cf10d8787f7f4
最近实际pull：2026-11-14 14:08:47 Asia/Taipei；上游 65be19eee5cd08491179f296cb6cf10d8787f7f4；与上一规则基线相比两README无差异。

每次pull比较根/课题README差异并立刻采用，实际pull间隔≤1小时。正常终端commit/push main已授权；每条结论独立推送，非快进立即pull --rebase循环至成功。根规则14：长算走公开math-research-ci的ci-queue；请求只含调用，OUT_DIR结果回推。R617在新规前启动且现已完成。不force、不改写别人提交、不用API/GraphQL写git。令牌仅CLI临时环境。root独占tracked/git，代理写agent-global/、agent-qc/、agent-o6/。根README不改；本题log每条≤5实际内容行，不写根LOG。Markdown<100KB，HANDOFF<10KB，open/README<30KB，文件<5MB，数据>1MB gzip。

旧交接和开放问题已逐字存 notes/2026-11-13-handoff-before-first-canonical-disk.md、notes/2026-11-13-open-before-first-canonical-disk.md；更早恢复依赖见其中链接。不得把归档中明确未完成的量冒充已求。

## 当前环境与恢复

2026-11-14约11:28 Asia/Taipei旧scratch和functions缓存丢失，已在同路径重新filtered clone；shell明确bash、login:false。当前依赖math-deps已恢复。原209项未推队列及R583汇总须凭真实输入重建，不能当仍在。

R389已由远端保全提交忠实恢复，原9文件SHA匹配；R472/R385早已main。其他恢复稿使用新hash，封存数学不为包装重算。Git自动gc关闭。

环境/旧队列见notes/2026-11-14-runtime-restoration.md；此前完整交接见notes/2026-11-14-handoff-before-primitive-trace-publication.md及notes/2026-11-14-handoff-before-R619-and-CM-basis.md，保留全部更早恢复接口。

## O5：真实规范高度与整盘排除

原规范：Xns+(41)g54，V1/V2/V3维73/199/325，V4维451；R222原54全局h及s=H⁻¹h，m⁻¹mod47⁴=4074216，QC=global−800λσ。共同坏标签0/3/28/32须跨方向相同，F3靶0/0/2621472/2621472，基点2^-9；R140/141对数不冒认unit-root。

19普通盘已完成：16排除，j38/39/40仅真CM根94227/9310/13002；五有理CM SS盘各唯一真CM根，21个非CM j10全排。具体图/54方向/共同分量/尾界按R234/240/246/255/304及归档，最新压缩前交接见notes/2026-11-14-handoff-before-public-runner-wait.md。

非CM SS已发布进度见notes/p41-SS-disk-progress.md：R389补完SS_j9_04的同分量F3；R606/R607/R609排除SS_j0_03/04/05；R610/R611排除SS_j0_06。累计47/105非CM SS盘排除，余58盘。旧R583本地129盘分类（121排除、8唯一CM）及未推证书丢失；忠实重建前不计作已发布定理，逐盘旧数字见前述归档。

R435单位截面、R436 j0_01全Norm/高度、R470余16j9两flip、R552/R554两真CM4接口可直接复用；不为包装重跑封存数学。R612已发布SS_j0_07九阶段真实F2及独审，留y=[47126,45023]；R618已发布同标签单位z的真实F3整盘排除。R617已发布SS_j0_08真实F2无根，整盘排除。公开runner首批R620–R632为j0_09/11–22；第二批R635–R654为R435覆盖的20个j36盘（除02/06）。均恢复缺失原链/F2，必要时原链续F3，产物回ci-runs后逐条登记。R655已提交双CM4原1-bit前缀续链/二类积分；完整高度另接R554（留R656），不套普通分歧公式。请求不计作完成。driver区分私库source与workflow commit。2026-11-14 14:02左右手动dispatch遭GitHub403（PAT无Actions权限）；请求仍在队列，等配置的定时领取，理论及准备工作继续。旧R472–511逐盘编号不足，用新恢复号，不猜原编号。

## O4：实际整性、变化导子与局部约束

R586恢复真实c0标记χ0、十八点核R0及v(S0)=1/(p+1)；R588恢复实际范数1/18、8与barM0=−M0、barM2=−ζM2；R589给M0²≡−72εBr′，r′=[z^(p−1)²]R0，单位iff r′≠0，零值仅v≥1/2。R564给Cartier交换C(R−ω)=cR+ω、C(R+ω)=c⁻¹R−ω，c=(3/p)α²/2；R574恢复完成ζ及Bell引理e_Q^p=D^(p−2)x(Q)、D^(p−1)x=−B、T_p=0、T_(p+1)=B。其他旧高权段不计已恢复。

R604已证明全部实际分支均有圆分因子的非三倍赋值split q；偶支q1mod12、D≥13，s(D)奇数时D≥65。R587已恢复实际even角色Ψθκ4κd⁻¹及准确N108p²D²、ε=(−1)^(s(D)+1)，故D≥65准确对应实际正根号支。p383/D5已排，不算新尚存候选。

R249–R326已发布的实际整性、同一全局φ、二三坏处辛型、好素数迹及Sturm约束，完整规范见notes/2026-11-14-handoff-after-R591-before-dependency-recovery.md及各证明。当前关键边界：所有导子下界不能给变化d的上界；不删Sha[p]、不把点饱和界当Serre界、不把任意深局部匹配当全局同构。R317实际范围p>37、p2/5mod9，a³+db³=1，p|b；偶支d奇、3∤d、d±1mod9且禁q7mod12。R320固定CM好迹给大素因子必要条件，但未证明必须存在小素因子；R326的界仍随d变化。

R330二层36p²扭Prym与R381非自扭块仍根号−，不能提供中心非零商。R575纠正实际六层的正CM型为Ψθκ4、层108p²、根号−；κ4^-1的正平均只是另一家族，原据此给实际秩零/零像的应用已撤回。R434/R471/R553仅按各自真实角色与局部条件使用，旧完整常数见前述交接归档。

R592已恢复实际全尖点Hodge整格、Drinfeld/GM坐标和v(Mn/n!)≥−np/(p+1)，c0/c1完整形式积分尾界成立；R603已闭合实际标记候选＋指定因子秩零＋r′p≠0的排除：有理c0,d基点、完整KS germ、v(z)≥4/3与严格尾界。全p首项单位、v(M2)=−1及普遍全局零像仍须分别证明，不以尖点整性冒认Néron格。

R597已恢复实际图式：原X1/c1与Xd/c0两投影覆盖id/ι；公共九次覆盖的新Prym微分交零，even Hom_Q(A1,Ad)=0。扭曲同构只保持同一v，c0判据须用于实际Xd商，不能替代原c1的正秩高度。

R602实际正号支p/D≥40+(20/3)log(1+logD)时全族L均值>1/(1+logD)，附本原预算得指定A−1,d秩零。R608已把实际族精确化为λ0ν、本原环类角色均值；真实整数迹及严格尾界给p59/d9971指定因子rank=dim=8与log同构，负号全族阈值改进为p≥40D；另有本原对数预算。R614已给新增可见射线的完整正/负核误差与radical充分区域，并以精确大素数证书验证两个分支。R598/R600及任意水平BFH–GZ–Nekovar接口已发布；一般radical、实际QC首项和D上界仍未证，正秩不等于零像。

R593给固定η、真实加权迹及完整μ3范数后的平凡化/唯一截面、统一cclear·ctriv；新增q项0，even的2/3有限Ω与d无关，旧数值Ω/N/M禁止移植。R596给hY(P,η)=ℓh(logP)。R616证明原β=q1[c1−c0]非挠iff L′g+·Lg−非零，明确D-independent区域内A(Q)⊗Q=Fβ；固定Hecke像给原高度矩阵H_h和ρ=uᵀH_hu+2ℓ_h−λ_p∈同一Ω。R634续原矩阵/局部QC；一般p非消失及p单位性未证。

## O6：忠实单位Norm与实际L

R591已推实际反循环43层与原t/q标记：408bit多项式、完整43基，F_t/F不同1890、index903、85个全局整环生成元。必要恢复的核心数组与旧SHA匹配；原Robert单位Norm和b等仍未求，不能以α_F Norm替代。

O6原始规范及R201–R377全部记录保存在notes/2026-11-14-handoff-after-R591-before-dependency-recovery.md。必须保持：真实Ω₂=ε(10−L)，忠实X生成1892次L+；R311仅构造正确Robert单位/正根，R322只给L的等价公式，规范相位尚未求。纯p值24和一阶10均不能代入原L。Cl(F)[43∞]=0和部分属商/塔abelianization已知，不等于原q分歧L/F的忠实Norm已求。原p43/776bitq已被Gaussian5排除，非曲线反例。

R561已恢复scalar-p²全部Robert产物和真实普通类C，证明L=31−22iC。R613同祖先给C_r=C+34r、C∈iFp及42个混合扩张普通主化。R619证明Cl(LF_t)_χ=k、Norm_T同构/扩张零，并给实际辅助C_t=9；它不等于原C。R633已证kerNΓ=RΓ[T]c_t、完整普通单位presentation及两个Norm像，混合满秩/饱和缺口已闭合。R599续原Norm首矩；原C/J/b/λ/n/L及full LB长度仍未求，ℓ与rμ=−2ℓ不得混用。

旧结果、R305正规整基及全部证明/SHA见results.md与逐条manifest；压缩前状态见notes/2026-11-13-research-state-through-R330.md。

## 连续执行与未推恢复

R389已恢复；旧209项队列及R583/585/590缺失证书继续按真实输入重建。依赖缺失明确留缺，不用摘要冒充文件；固定p41完成也不能结束绝对目标。

完整结论逐条单推，R619/R616/R633已登记。R594已恢复全p形式log分解、Kp=−3/Bp及p269宽范围反例；保全45末项，不重跑旧数学。R615已证完整六挠Kronecker递推、准确固定L常数与全惰性p的Cp整性；一般r2=cCp比较及r2r3/r′非消失转R658继续。

范围不可删：269≡8mod9不属R317，c0/c1不同；primitive零点不等于正秩QC零点。R595的Δ末因子勘误有效；R601给K0=K2=0，R605给K1=−B²r2/4及(pM2)²≡5184ζ²B⁵α⁻²r2r3。一般r2=cCp比较仍有O处差，整性/单点吻合均不给非消失。原O6未知量也不以纯p值24或10替代。

root持续恢复O5并推进全局排除；global继续R634固定β的真实CM高度，QC继续R658真实Cartier比较及r2/r3/r′结构，O6已完成R619/R633并继续R599原Norm首矩。推送成功凭远端main及root-recovery/published-R*.json。达到绝对主目标之前不以阶段报告停止。
