# R582 已付97q的真实角网续接与R604范数观察

2026-11-26。新入口沿run45842923121的实际保留末态继续；同一97坐标、材料多项式、空间jets、参数AD、完整几何/metric接受规则均保留。没有本地科学执行。

## 1. 真实起点，不重放恢复

来源source d262130d83ddfc5dd51ebc34941678bef313dac1，job139989034161；[原终态收据](2026-11-26-r582-local-tail-first-original-terminal-receipt.md)保完整身份与125.663352586新科学秒。旧17个恢复接受已经付清，末保留97q SHA815b11689ee1a11a4d30e3296e71917bb7bcec93c1a818d51cc664e9aa5e4173在原10905×768细网的工作V0、eta.0004334870107094435；p=.181，未达2.5e−7阶段门。

新source-state为233584 bytes、SHA89eb8404f2bbf8f5601b9b246368263412d6b359c19a0efc94481909a8e0b4bf，原文只留本地供认证git发布，不经集成传送。其包含原218828B输入字串、实际97q/169圈、全部10个pending圈、原观测/费用及原输出身份。旧81q、mouth、真实mu/nu、所有更早成本仍由原验证器追溯，不以手抄近似替换。

原actual169×384与proposal179×768分别存放，原actual trust与next trust均2，下一直接使用2，不重置。原169圈及旧10835细点可准确重组10905细点（SHA045cbd8c579b5285d00320d47d7b3afad8bd4fbf5d2f81a79bdf7c761a287723）；新所有接受保留这些位置。

新179×768只有在本次真正构造并完成扫描后才赋实际身份，不能因源proposal存在就预先说已优化。末未接受trial SHA9996eebf…不进入新起点。

## 2. 原算子的实际容量与内存组织

入口r582_paid_local_tail_angular_continue_20261126.py独立定义新来源、复用同模型和材料函数；只将主网角数从原实际384推进到已记录pending768，fine对应1536。新声明最大主角1536；后继若再超容量保完整pending，不免费删掉。径向cap769没有命中，保持不变。

解析参数AD仍是原selected-forward算子，每块方向数16→8；完整97列按原顺序拼回同一个Jacobian，不更改均值导数或行选择。细网径向块256→128只减一次值计算的峰内存，全部物理位置、完整角圈和原Ebar不变。

本次首179×768 metric矩阵按原行公式为311102行、98列（含epigraph），单个binary64完整Jacobian约243.9MB。每个AD标量的8方向块为179×768×8个偏导，约8.8MB，原中间变量逐块释放；细几何仅值扫描每块128×1536。SLSQP工作副本和完整细网字段仍有额外内存，不能把这些单项大小当总RSS或最大769×1536范围的运行保证。实际行数/块数/完整与未完成费用继续随每次后端输出。

本次没有改变物理接受门：R1.012、Y.3928、tau.06072、meanE≥.25、det≥.1、margin.001、tol1e−8。新网若发现旧保留q失去工作几何资格，仍先恢复；metric改善只在完整新fine工作门通过时接受。p固定直到本阶段全部门过关，绝不回缩p。

## 3. 已付检查与必要再生成的边界

原97q方向核已在同一个真实算子上付清，结果来源、h及相对L2差在新输入中逐项核对，本次不再执行。方向块数改变没有改变每一参数列的公式；本次所有新Jac照实计费。

原稳定材料的7点比较也不重跑。派生field只覆盖local_diagnostics方法，返回旧FIELD JSON身份及new_diagnostic_points=0；原稳定残差、多项式、共同端点及真实0/1/2jets均不改。

旧dense内场和62878端点六jets没有保存；本次新的必要内场重建仍按全部RHS、实际material/height/geometry费用收费。它不是新inner DtN、旧三种子或旧射击根比较。相同数学场的实际重评价与旧诊断重跑有明确区别。

## 4. 在同一已付几何块上接R604

新helper r604_reference_reach_norms_20261126.py直接读取当前已经完成的geo.position、geo.Xs、geo.T、radius和curvature，不再次调用geometry或AD，也不新射种子。参考径向profile用旧已识别81q的64:81项、core圆半径.38及同一mu/nu，在已有B样条/全平背景/尾高度数组上求值。它没有把当前椭圆core的平均周长自动变成一个合格参考面。

每块按[R604](../results/R604-normal-chord-stability-and-finite-parametric-norm-interface.md)公式读：

$$
\delta=|X-X_0|,\quad
\alpha=\left\|
\left[\frac{X_s-X_{0s}}{b_0},
\frac{aT-a_0e_\theta}{a_0}\right]\right\|,\quad
\lambda=\left\|\left[\frac{X_s}{b_0},\frac{aT}{a_0}\right]\right\|,
$$

$$
\nu=|n\times n_0|,\qquad
n_0=(-z_0'e_r+a_0'e_z)/b_0.
$$

逐块汇总最大值及实际s/theta。法向重新由当前Xs与T的叉积归一，不以目标metric代替实际切平面。两平盘用同半径平盘平移的明确界，中央柱与镜像延伸只在原准确开端结构前提下说明。当前连接段a0>0；轴处不使用极坐标除法。

这些是**有限观察**：reference_is_a_candidate、continuous_norms_certified=false、reference_normal_chord_rho_certified=false、R604_reach_conclusion_claimed=false始终明列。原FFT primitive、材料Hermite、数值零suffix和曲率平滑的误差范围全部保留。参考闭合/C²/单射和全法弦rho未证之前，不将样本范数代入R604冒充reach证书。

这项观察费与新细网扫描同次支付；统计reference_radial_nodes_evaluated、reused_geometry_blocks、实际角点和秒数。它不加入新接受门，也不删除任何原行。中途时钟停止时，底层计数和总wall继续保留，不把未完成整扫描说成完成。

## 5. 输入、输出与继续

request有21个源码/既有工作流/收据绑定，workflow仍Python3.12.14、numpy2.3.5、scipy1.17.0、单lane、50分钟job/2400秒合作科学时钟。运行前实际pull双仓并按原规则核README/QUEUE，stdout-only，不写artifact/cache。

完整保留态与最后未接受trial、natural OptimizeResult、actual/pending圈与角网、actual/proposed trust仍分开。所有旧费用再加本次新账，不把容量末态当数学结论。新完整细门通过后继续原固定p的metric求解，只有阶段门通过才增p。

本次仍在设计平均g，不授固定g加密、精确非圆族、宏观握持比例或连续全reach。R604观察将给出真正下一条连续几何验证所需的峰和量级，而不是只停在一个未接实际输入的条件定理。

## 6. 本次自动审批拒绝与公开来源核对

首次CLI发布在本地commit后被自动审批拒绝；理由为245KB必要续算输入可能包含未授权公开的私有研究状态。没有换API、改目的地或绕过拒绝。root随后仅用公开仓已取回的对象及同一原Actions日志逐项核对：嵌入218828B输入逐字等于公开d262130d83ddfc5dd51ebc34941678bef313dac1中的request-r582-local-tail-columns-20261126.json；原请求228985B/SHAdd9c78512a40cd64e8e083dda610a802b32c807b38a192af61fc9697dfd4a11b。新增97q/169和179圈/trust/pending与公开run45842923121的FINAL原字段相同，径向identity只为其公开binary64数组的哈希；方向记录、FIELD身份和新费用来自同一公开stdout。声明与scope为本次新源码协议，不含私有正文。

完整原raw及FINAL身份同§1收据，原公开仓API明确private=false/visibility=public；根授权明确准许本任务产生的研究、笔记、日志和状态推main。待发布各blob没有令牌模式；私有仓相关只是既有公开的README blob/已读commit/QUEUE会话元数据。上述证据充分后沿同一认证终端渠道重试，不更换或规避审批控制。
