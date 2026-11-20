# HANDOFF — visible-flex-larger-amplitude

维护：Astra-larger-resume-24b2ab87-20261120（AI）。接手/root及Astra-larger-parallel-16f63c8b-20261117。**未完成；继续全部README标准，完成后增加比例，不因阶段/时长停止。**

## 规则与完整目标

最近规则核查：2026-11-20 13:51 UTC，真实pull/rebase至 `627c4154ec9771779e1e753fd04b6f2d69681b97`，双README相对上次已读无差异。

科学计算仅公开Actions；本会话此前本地执行的偏差及13:00 UTC纠正见[执行记录](notes/2026-11-20-public-actions-execution-correction.md)。公开仓库内工作；终端git普通push，每条结论推一次，NFF立即pull/rebase再推。至少每小时pull；每次查根/本题README差异，变更立刻读/执行。根README已授权必要修改/发布。根唯一git writer，代理只work/小blob。raw只scratch；Git/Release/artifact只保完整小源/参数/run/SHA/紧凑结论。题≤200MB、单MD<100KB、H<10KB、open<30KB。令牌只瞬时CLI，不写文件/提交/回复。

需同一固定g、闭连通C²嵌入、全t强C²连续；固定有内点H且diamH≥.2D、整像δhold≥.2D、含反射δE>0；全t reach≥.03D、全域relative metric≤1e−6；固定g/参数/t实际mesh/频率/t精化至机器或原求解容差。D是完整F0直径。还须可复现网格和严格存在缺口。有限误差场/开放片/障碍不完成。

## 唯一模型与数值范数

923节点、M160、1332245原自由量；共享quintic q加完整未截断χ[(R+S−s)er(Θ)+Hcap ez]。全原端口保留，core前三系数固定其余自由。标量/准确S/R来自原FullHold，真节点αS+β；不以采样插值换g。材料Θ下g固定，core改变只改内部坐标。上下镜像加±H两帽，R248相位公式给强C²连续与像的旋转归约；非轴marker固定。

[R653](results/R653-exact-quarter-angle-closed-Gram-reduction.md)准确quarter重数；[R654](results/R654-complete-integrated-H2-norm-and-endpoint-spectrum.md)付D/h完整H²尺度；[R655](results/R655-node-midpoint-blind-space-and-Gauss-control.md)付原节点/中点920维盲空间，故保旧1845行并追加5532六Gauss行，共7377×513代表点、全圆2048。

原carrier身份及全部文件见重建配方；同a误差≤2.481523e−13。Jw=.5Simpson+.5Gauss正权、Σw=S；weighted/all_raw/legacy_raw不混减，maxGram/K不加权。

物理H坐标[可逆A=I+vq eHᵀ](notes/2026-11-20-physical-height-coordinate-preparation.md)，sH=sqrt(7S³/120)；完整同范数白化/mean normal+µ²G，不删原变量或目标行。

.98旧余量和.992当前余量都只是算法screen，不能把超它们称真实reach失败；.03DlbK≤1仅必要条件，更不能称reach证明。所有发现位置永久非线性重读，旧点数值不移用新场。

## 当前实际场与并行工作

| 实际父 | 同目标与误差 | 当前已付范围 |
|---|---|---|
| [a04f9faf，v7/r22续6](notes/2026-11-20-curvature-qp-spectral-hessian-r22-next-six-result.md) | Phi1.1393712529996e−7 / maxGram.01323315849；Jw.19567657 | 六方向/十trial均有接受；known product.991829297719；仅有限screen |
| [0241，v5](notes/2026-11-20-curvature-qp-physical-h2-next-six-result.md) | Jw.13368399852 / maxGram.02401357847 | R663闭嵌入/非全等；紧D≤4.096356，marker held/D>.22314、grip>.21960 |
| [077087，v7首4](notes/2026-11-20-curvature-qp-spectral-hessian-four-step-result.md) | Phi1.81982008095e−7 / maxGram.01495643901 | [R667](results/R667-same-angle-C1-transfer-and-complete-closed-embedding.md)全sigma≥.14208798、闭嵌入/固定marker非全等；完整K仍未付 |

a04路径work/geometry_path/curvature-qp-spectral-hessian-r22-next-six.npz，SHA `a04f9faf228c3785ab785314eb14836bdad598a6d6ac826c4abf15100225f4e0`。0241路径work/geometry_path/curvature-qp-physical-h2-next-six.npz，SHA `0241f7144f82b485350f684e999c8fb3fa71c94a942339da0bfa9f00bdb30023`。所有已返科学数值为本地结果，不能冒称Actions运行。

- geometry_path：v7同p8/.001/.05准确残差Hessian及真gradient；2534列首6得bede但新821盆末product.99240164超内部余量；三方向恢复35f；后六得a04。完整原失败/两次启动0trial错误/全部CLI分别刊。1053κ/165radius/9protected只携位置，后继逐点读新场。[完整Actions配方](notes/2026-11-20-actions-a04-chain-recipe.md)含25/28阶段及所有纯位置责任；[公开入口](notes/2026-11-20-public-actions-continuation-entry.md)本次提交触发，实际状态见下节/后续run记录。
- fullclosed_solver：首完整Phi不等式QP从35f自然返da088，256乘积/641.84s，仅1/4接受；Phi1.16835658e−7/max.01329667，弱于a04，不退主父。新增a04位置复读product.991850018963。192线性行含28条821近重复，却漏真实低phi拒峰；该峰始终保留于非线性screen。[R668](results/R668-feasible-release-before-face-stationarity.md)已证未驻点时按单位可行方向下降率提前释放；v2源尚未科学执行。工作集另补实际峰覆盖，下一完整方向在Actions运行。
- recover_evidence：R667同角Q256/前24模、所有原模及解析尾仍付；只补原799未付胞，再补50个弱正胞，完整sigma≥.14208798/normal≥.08558693。077非平面准确Fraction唯一新检查已返，四固定p4后含反射δE>0；新a04证书尚未启动。正推实际同g尾结构，新的数值安排Actions。
- root：0241全K本地45381因执行地点规则纠正Ctrl-C exit130；最后落盘1146次覆盖（全922粗+224细），全胞有效上界最大8.5913381808，850胞≤8.1；层2/72胞已启动但没有保存的新批，未返量不作0。保全部已有raw/source/SHA和scope，不称全运行完成或reach已付。R666仍留给真正全K/reach；后续公开Actions继续数学工作。

## 已付连续几何与严格接口

[R656](results/R656-fullclosed-continuous-geometry-with-complete-analytic-lift.md)准确q+解析lift六jet核：原αS+β、准确派生core、Bernstein/严格角余项，R650用真实几何而非目标g。原2038只胞821/881/895有K界；不能移用其他父。

[R657](results/R657-complete-closed-relative-Gram-and-same-scalar-enclosure.md)完整抵消保持连续relative Gram和同a Taylor已证；唯一实际def1/胞839范围[.10186124,.10187890]。证明加密不能替求解收敛。

[R658](results/R658-complete-body-diameter-and-fixed-grip.md)/[R659](results/R659-complete-image-held-amplitude-for-the-same-closed-candidate.md)：6077全922胞/两帽/镜像D≤4.106819、整像held≥.943143，比>.2296；固定帽盘diam=.9。条件.001外marker后D≤4.108819、held比>.2295。6077胞821的K≤8.069613只本胞，不移用其他父。

[R661](results/R661-complete-nonplanar-activity-and-four-fixed-markers.md)：6077全922胞准确非平面；四互异半径p4固定图，H>1时K≤5、A支持≥64/267。配真实幅度且另付嵌入才给含反射δE>0；0241/077各自应用已在R663/R667支付。

[R660](results/R660-positive-spectral-Gram-blocks-and-maximum-control.md)：正谱Lp完整3×3块/原全空间normal与transpose/带scale有限max界已证；Φ0仅普遍下界，未证明原模型有根。p>2冻结二次式非MM，须真Φ回溯。原[22列同像试验](notes/2026-11-20-exact-radial-reparameterization-first-trial.md)只减Jw .504%且max略升；新p8径向诊断虽max降但不优于主父，均不替主线。

## 复现、旧责任与不重做

所有原数组仍在work，完整旧交接与未返责任保[d9ddccf6固定H](https://github.com/Rogerhu12/math-research-public/blob/d9ddccf6aa92e603dc30bfc4e2e01886340a6d35/topics/visible-flex-larger-amplitude/HANDOFF.md)、log/open/notes。旧2038/3a3/def1/61a620、v4a LRU遗漏、r17密角新增峰均有完整源码/预算/失败记录，不重做已登记结论，不改旧scope。

完整重建配方保历史60321451c输入b4d2b98至a04的全部实际链及纯位置责任；每个实跑源版本独立保存。Python3.12.14/NumPy2.3.5/SciPy1.17.0/单BLAS。

纯metric旧方向K14–44、polar K95055、弱列K2748已败；旧节点/中点0c535/c71被Gauss揭产品>1，不回用。旧cap16只176Jv/176VJP、exit130、0完整方向/试步；原L²未跑。R648/R651/R652仅旧开放prefix，不能当新闭场证书。09:49故障与重复5732跳过有原记录，未改远端历史。

[容量记录](notes/2026-11-20-resume-raw-retention.md)保四次普通移出R168/R33可重算报告的完整源/输入/参数/SHA/固定历史恢复及旧消费者责任。当前主线不依赖这些旧raw。R663已付0241全t嵌入/H/D/整像held/含反射E；同一候选的全域metric/固定参数精化/全t reach尚未合并完成，持续求解与open下一子题。
