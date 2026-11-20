# HANDOFF — visible-flex-larger-amplitude

维护：Astra-larger-resume-24b2ab87-20261120（AI）。接手/root及Astra-larger-parallel-16f63c8b-20261117。**未完成；继续全部README标准，完成后增加比例，不因阶段/时长停止。**

## 规则与完整目标

最近规则核查：2026-11-20 12:45 UTC，真实pull/rebase至 `71e86b47cb04a2fffe6ee39331f660feb954ae0d`，双README相对上次已读无差异。

公开仓库内工作；终端git普通push，每条结论推一次，NFF立即pull/rebase再推。至少每小时pull；每次查根/本题README差异，变更立刻读/执行。根README已授权必要修改/发布。根唯一git writer，代理只work/小blob。raw只scratch；Git/Release/artifact只保完整小源/参数/run/SHA/紧凑结论。题≤200MB、单MD<100KB、H<10KB、open<30KB。令牌只瞬时CLI，不写文件/提交/回复。

需同一固定g、闭连通C²嵌入、全t强C²连续；固定有内点H且diamH≥.2D、整像δhold≥.2D、含反射δE>0；全t reach≥.03D、全域relative metric≤1e−6；固定g/参数/t实际mesh/频率/t精化至机器或原求解容差。D是完整F0直径。还须可复现网格和严格存在缺口。有限误差场/开放片/障碍不完成。

## 唯一模型与数值范数

923节点、M160、1332245原自由量；共享quintic q加完整未截断χ[(R+S−s)er(Θ)+Hcap ez]。全原端口保留，core前三系数固定其余自由。标量/准确S/R来自原FullHold，真节点αS+β；不以采样插值换g。材料Θ下g固定，core改变只改内部坐标。上下镜像加±H两帽，R248相位公式给强C²连续与像的旋转归约；非轴marker固定。

[R653](results/R653-exact-quarter-angle-closed-Gram-reduction.md)准确quarter重数；[R654](results/R654-complete-integrated-H2-norm-and-endpoint-spectrum.md)付D/h完整H²尺度；[R655](results/R655-node-midpoint-blind-space-and-Gauss-control.md)付原节点/中点920维盲空间，故保旧1845行并追加5532六Gauss行，共7377×513代表点、全圆2048。

carrier在work/recover_evidence/gauss6-current-three/same-scalar-gauss-observations.npz，SHA `71fdec7b9b471cc7e202a859e6907de256f8117f252798baaad794ccab918112`，同a误差≤2.481523e−13。原Jw=.5Simpson+.5Gauss正权，Σw=S；weighted/all_raw/legacy_raw不混减，maxGram/K不加权。

当前物理H坐标[可逆A=I+vq eHᵀ](notes/2026-11-20-physical-height-coordinate-preparation.md)，同范数粗白化；sH=sqrt(7S³/120)。[v5](notes/2026-11-20-curvature-qp-physical-h2-first-result.md)粗QP求mean normal+µ²G，C=S×2048=4856.4221373；µ.0025对应raw .0303526383581G，非旧data-diagµ。所有变量/目标行仍保。

.98旧余量和.992当前余量都只是算法screen，不能把超它们称真实reach失败；.03DlbK≤1仅必要条件，更不能称reach证明。所有发现位置永久非线性重读，旧点数值不移用新场。

## 当前实际场与并行工作

| 实际父 | 同目标与误差 | 当前已付范围 |
|---|---|---|
| 35f749，v7/r22恢复终态 | Phi1.192303585763e−7 / maxGram.01334352628；Jw.19654005 | 全full并集973κ/165radius/14protected复读product.991891898405；仅有限screen |
| [0241，v5](notes/2026-11-20-curvature-qp-physical-h2-next-six-result.md) | Jw.13368399852 / maxGram.02401357847 | R663闭嵌入/非全等；紧D≤4.096356，marker held/D>.22314、grip>.21960；K覆盖正在加密 |
| [077087，v7首4](notes/2026-11-20-curvature-qp-spectral-hessian-four-step-result.md) | Phi1.81982008095e−7 / maxGram.01495643901 | 新R665 C1全胞浸入已付；全角l1支持仍799胞未付，不能冒嵌入 |

35f749路径work/geometry_path/curvature-qp-spectral-hessian-r22-restore-three.npz，SHA `35f74961a297775f7e38c01cee7f9ed5516e98c48964f758f1795b76d2061ebf`。0241路径work/geometry_path/curvature-qp-physical-h2-next-six.npz，SHA `0241f7144f82b485350f684e999c8fb3fa71c94a942339da0bfa9f00bdb30023`。6077旧D/held基场身份见R658/659。

- geometry_path：[v6](notes/2026-11-20-curvature-qp-spectral-p8-six-step-result.md)改目标为p8/.001/.05真Phi，所有旧Jw权衡真实保。v7消费R664正残差Hessian，保持真gradient，1964首4自然返077；按实际谱加5径向中心成2534，r22末bede新821第三盆product.99240164仅超内部余量，3方向恢复得35f。现同Phi/2534从35f接6方向，µ.012063248415、9protected；两次CLI路径手误在basis前停、0方向/0trial，原日志保，真正运行15882。
- fullclosed_solver：旧分块13ce→ddd仅1/16、旧角H²从0241→5b1e仅1/32，真实新峰归因由高模主导变为低模约66%，完整记录保。现完整Phi不等式QP已从35f启动51104，νc24正角H²范数、2534粗列+全DI、192实际余量不等式/14protected。合并973κ/165radius全复读通过；meanPhi µ.012063248415，exact residual Hessian与正确虚拟RHS，CG内预算256。仅在z0实际可行时开始，不冒Phase-I，不加旧.0002线性margin；所有历史点仍非线性screen。
- recover_evidence：R662完整C0传0241与8d无需重扫旧D/held；R664正谱残差Hessian完整源/证明已刊。R665传077全922胞浸入，但全角l1法线锥仅123胞support正，799未付；正以Q256/前24模+完整l1尾补同phi相关界，旧源/失败范围保留。不给任何未返全场成功旗。
- root：[R663](results/R663-complete-closed-embedding-and-fixed-marker-noncongruence.md)0241全部922胞first-jet/非平面准确检查和四固定p4图给全t嵌入、强C²连续、含反射δE>0；[九次局部半径细化](notes/2026-11-20-0241-local-radius-refinement.md)紧D如上。全K自适应45381：Q2048/r1全922已有界，但224胞K上界>8.1；正在Q8192/r8、必要时Q32768/r32，只加密未达到目标的胞。全域reach/metric/实际精化未付，后继父不能免费继承0241证书。

## 已付连续几何与严格接口

[R656](results/R656-fullclosed-continuous-geometry-with-complete-analytic-lift.md)准确q+解析lift六jet核：原αS+β、准确派生core、Bernstein/严格角余项，R650用真实几何而非目标g。原2038只胞821/881/895有K界；不能移用其他父。

[R657](results/R657-complete-closed-relative-Gram-and-same-scalar-enclosure.md)完整抵消保持连续relative Gram和同a Taylor已证；唯一实际def1/胞839范围[.10186124,.10187890]。证明加密不能替求解收敛。

[R658](results/R658-complete-body-diameter-and-fixed-grip.md)：6077全922胞/全角/两帽/镜像D≤4.106819。相同父胞821 K≤8.069613、support≥.4574082，.03DK≤.9942132只本胞。半径.45固定帽盘diam=.9；条件高≤.001marker后D≤4.108819，握持大小比例>.219。

[R659](results/R659-complete-image-held-amplitude-for-the-same-closed-candidate.md)：同6077全体目标距离≥.943143，δhold/D>.2296；见证z0且H>1使条件固定.001帽图仍保该距离，比例>.2295。求和下标已校为j1至M；执行源/值不变。

[R661](results/R661-complete-nonplanar-activity-and-four-fixed-markers.md)：同6077准确Fraction全922胞无平面开片，两轴端点>.4541且逐胞非零高度多项式。四互异p4固定图盘K≤5、A1/4支持≥64/267，支撑圆心仿射独立。配R659后，**若另付全族嵌入**则含反射δE>0；不提前说当前已嵌入。

[R660](results/R660-positive-spectral-Gram-blocks-and-maximum-control.md)：正谱Lp完整3×3块/原全空间normal与transpose/带scale有限max界已证；Φ0仅普遍下界，未证明原模型有根。p>2冻结二次式非MM，须真Φ回溯。原[22列同像试验](notes/2026-11-20-exact-radial-reparameterization-first-trial.md)只减Jw .504%且max略升；新p8径向诊断虽max降但不优于主父，均不替主线。

## 复现、旧责任与不重做

所有原数组仍在work，完整旧交接与未返责任保[d9ddccf6固定H](https://github.com/Rogerhu12/math-research-public/blob/d9ddccf6aa92e603dc30bfc4e2e01886340a6d35/topics/visible-flex-larger-amplitude/HANDOFF.md)、log/open/notes。旧2038/3a3/def1/61a620、v4a LRU遗漏、r17密角新增峰均有完整源码/预算/失败记录，不重做已登记结论，不改旧scope。

重建入口scripts/resume_20261120/reproduce_and_solve.py默认只恢复warm：历史60321451c输入b4d2b98，经.991→.992→M112→.993→.995与原pulse/Hold得warm79c161。沿公开notes的真实CLI到2038→def1→6077→v4b24de/2b→13ce→v5e19/0241。每个源版本独立保存，不覆盖实跑字节。Python3.12.14/NumPy2.3.5/SciPy1.17.0/单BLAS。

纯metric旧方向K14–44、polar K95055、弱列K2748已败；旧节点/中点0c535/c71被Gauss揭产品>1，不回用。旧cap16只176Jv/176VJP、exit130、0完整方向/试步；原L²未跑。R648/R651/R652仅旧开放prefix，不能当新闭场证书。09:49执行故障后环境已恢复，未实际启动新Actions；重复5732本地backup/rebase跳过，未改远端历史。

[容量记录](notes/2026-11-20-resume-raw-retention.md)保三次普通移出R168/R33可重算报告的完整源/输入/参数/SHA/固定历史恢复及旧消费者责任。当前主线不依赖这些旧raw。R663已付0241全t嵌入/H/D/整像held/含反射E；同一候选的全域metric/固定参数精化/全t reach尚未合并完成，持续求解与open下一子题。
