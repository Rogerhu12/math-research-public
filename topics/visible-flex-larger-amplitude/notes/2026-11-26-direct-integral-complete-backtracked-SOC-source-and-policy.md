# 同一 direct integral 场的完整后退锚 SOC：源码应用与执行责任

日期：2026-11-26。本条是已证同父全半空间修正的一次完整应用及新的明确选锚政策，不重复登记R683/R685，也不声称新的数值收敛或连续几何定理。实际后继参数依据run05实际8/11；新四源尚未科学执行。

## 1. 为什么在这个实际父接此完整政策

实际05的第二个direct integral方向由完整606返回，末父`f1e504f8a2fab97b564efb11c8aca27dc319e207e28006c8b3f24e87f0eb3c30`，报告`18257406f36e68f7401a3a87c8f0f4f34866f774688a90e30eaa9354c90368b7`。当前完整模型`9b4958325403bd74616c5875ca54f027981d2d55c9c56634dc81f8cd0d2123c7`、固定目标`e71b374557c5efa07ce2b5795c73f3e5b3a50d10d125b40c1f1682af37742350`、integral范数`c06a7abc532243cc3faee0b123a4d5c7f6c109527e426dc764b1205af528c8d9`和实际末mu0.01均有真实报告。

完整纯归因11表明alpha=.5至.03125的Phi都真下降，前四个都仅reach真筛失败，.03125才全部通过。最近较大拒绝ray为.0625，reach g=.18635382498788267；.5的reach g=6.960628223861761，不能把它们当同尺度锚。当前拒绝极值在径向cell237等处，不能套用原jet-sum方向cell0/1解释。新完整QP仍须从实际末父重新求方向，自行找到自己的最近拒绝锚；旧alpha和旧物理梯度不会直接代入。

另一实际normalized-parent分支的04实际44/45已经以相同选锚政策真接受一次SOC，但它的源、物理模型、目标、范数和cache不属于这里。这里只复制该完整line-search控制逻辑，不继承其场、向量、cache或证书。

## 2. 新完整四源和精确派生

| 文件 | 字节 | SHA256 |
|---|---:|---|
| `fullclosed_axisymmetric_so3_backtracked_soc.py` | 71419 | `450a4341ba425544ccb641094e242bb332563835c567af4062a62e278a6647a6` |
| `launch_axisymmetric_so3_backtracked_soc.py` | 9972 | `b550dcffdaffd993f89ee493c82bcc96b9e680428262230ddb546cf688eb1c20` |
| `derive_axisymmetric_so3_backtracked_soc.py` | 14384 | `72079e54639a6fd38f64eb42065eb461f326756a05b497fc29b14ba84bf23e5a` |
| `read_axisymmetric_so3_backtracked_soc_report.py` | 49044 | `b706d6193f95b61b6282a57719401e379545649656fbe6ddf9560c938a4edf31` |

均在`scripts/resume_20261126/`。driver schema为`complete-independent-axisymmetric-fixed-deep-so3-backtracked-separation-SOC-v1`，pure schema为`actual-complete-independent-axisymmetric-SO3-backtracked-SOC-scalar-readout-v1`。

科学主体来自完整359f：
`359ffc94df1b33485c2cda4de0f5662ef7bc802c588f583a023fcd5723a7872d`。完整选锚段22,445字节逐字取自完整892f：
`892f349b140f9a77fde37fc490d7cbb078cfdb21f8b31b7743e50ec6cf5712a8`。准确修改仅为新文案/schema、同范数和同政策restart守卫、报告政策字段，以及该完整ray/SOC/最终候选选择段。完整driver实际全文由pure deriver重建并与交付字节相等；不是以局部AST片段假装完整source已核。

全部20项direct SOURCE_PINS与359f逐项相等。原7f物理operator、2240世界geometry、完整02875 typed行helper、原QP/谱Hessian/centered统计/历史walker均保持原字节。normalized缓存和其额外内点Phase I没有导入；direct的完整CommonSlackRows原函数保持。全部原顶层接口与main内局部统计/真geometry函数逐体AST相同。02875与892f使用的e716 helper在bind_anchor、freeze_qp_prefix、seed_before_qp、extend_from_rejected_geometry、propose、cache_state、qp_metadata七个实际调用核心方法上AST相同；来源验证部分仍用真实direct 02875，绝不改成normalized标签。

新入口完整保留1,333,370自由量、原freecore/H、所有共享径向jet和角模式、所有正权metric行及均值/交叉项。新guard显式要求restart的真实coordinate norm identity等于当前构造的完整norm identity；此处并非允许原jet-sum自由点自动带着旧mu迁到integral。当前实际606 integral父通过旧6d完整reader的source/场守卫后，再由新body核同模型/目标/carrier/完整norm。自己续接还要求同完整source-role集合、同最大轮数/tau/内缩/读回容差和后退政策。旧606、359f、892f源保持原字节。

## 3. 精确同父约束和真可行fallback

设当前完整父为$x$，原QP全坐标方向为$p$，原lift为$T$。每个约束先在当前$x$读取真实值与完整Jacobian；其正行尺度不变。当前QP所有原行、已发现位置线性化和新增幅度行形成固定前缀。原始回溯按$1,1/2,1/4,\ldots$逐个完整读取域、同Phi和全部geometry/幅度/永久位置，直到出现真可行ray。只把这个ray作为暂存fallback；原$x$仍未更新。

在它之前所有已经实际Phi下降、域合法、完整geometry拒绝的ray中，取最近的较大alpha，固定$d=\alpha p$及完整$x+Td$字节。若预算内没有真可行fallback，本次不以任意大拒绝ray开启该SOC策略。若原ray直接可行而此前没有符合条件拒绝ray，则按原真筛接受原ray。

对每个有限typed约束，以当前父所固定的正行尺度定义完整函数$\gamma_i$，记$C_i=D\gamma_i(x)T$、$b_i=-\gamma_i(x)$，固定锚真读值$r_i=\gamma_i(x+Td)$。这里$r_i$是锚处真实规范化约束值，不是Taylor余项；另行记录的非线性余项为$r_i-(C_i d-b_i)$。代码使用同一明确内缩$\eta=\tau\lVert d\rVert^3+\kappa\max_i(r_i)_+$，每次完整修正要求

$$
C_i e\le\min\{b_i-C_i d,\,-r_i-\eta\}.
$$

所有旧前缀行与后续分离新行一同进入原全半空间projection。新的真实拒绝极值只提供地址；完整父值和完整梯度仍在相同$x$重新读取，simple curvature分支的实际合法性守卫不删，最大直径partner在当前父完整选择，freecore/Theta/H及held witness点的额外导数全部保。新parent bound为负时明确不能把零步称可行；代码记录需要真实restoration/另一父，不把这种状态伪称数值投影可行。

后续修正仍针对同一原$d$，不把上次修正改成新父或新锚。每个候选重新计算自己的$Az$、同父模型预测、真Phi/domain和全部geometry/幅度。观察违例比例1/8内缩是一项明确数值政策，不是已证三阶全域余项界；最终必须真筛，绝不放宽.992、reach、D/L/H或原物理约束。有限行投影及数值容差都不能取代连续几何证书。

## 4. 新发现位置之后，fallback也必须重新付真读

原ray首次通过只是provisional。第一份完整修正候选通过时，将它与原fallback按此前实际同Phi排序；每个待选择完整点都在全部最新永久集合上重新读取域、Phi和geometry/幅度。拒绝SOC找到的极值即使该SOC未被接受，也进入永久集合。旧fallback的passed标志不能绕过这些新位置。

候选读回记录完整point/原parent字摘要、前后永久计数、全screen点摘要、各自Phi/domain/g，以及候选的实际失败类别。只在最终选择通过后，唯一一次更新$x$。若两个候选都失败，则继续本次原ray剩余预算，保所有新位置，不另外换第二个SOC锚。相同数学Phi才可排序；correction独立预测不冒原方向预测，SOC采用时保持当前真实mu，原alpha=1的阻尼规则原样保留。

完整pure reader分别读取provisional值、最终readback值和唯一accepted记录，逐项核锚顺序、最近eligible条件、同$x/d$、完整字节摘要及永久集合计数；不以accepted字段孤立自报成功。Phase I仍用原direct完整all-C公共slack语义，与物理真g分开。reader不会把normalized的内点margin要求套到该直接分支。

## 5. 最小完整公开Actions参数与历史

完整参数文件`resume-20261126-direct-integral-backtracked-SOC-after-actual8-ready.json`，15,950字节，SHA256 `306b1ebd986954a071460a9267939dd75fd3cdbfb902d4ab11ff4697b787819a`。它含一个完整科学和一个完整pure步骤，科学父为实际8 f1e5/182574。mu=.01、integral规范参数.05/24、N2048/block64×8、原径向积分8和原inverse参数、1×64 metric及4×64 restoration、15ray/8SOC、tau0/内缩.125/读回2e−11、全部原QP容差、p4/epsilon.001/scale.05与原D/L/H/reach阈值不变。

九个必读manifest为reference locations、当前run的完整direct首报告、旧direct-SOC报告、angular-unit报告、第一/第二integral报告、gamma-H报告、normal报告、normal-H报告；最后三者实际05编号12/15/17，均已真实产报告。旧字段和source路径名称不改变地址语义；所有来源位置重新读值，不能继承旧梯度或证书。若任何明确依赖不存在或不合法，入口应诚实失败，不能悄悄省掉。

pure admission parent用已存在f1e5，避免科学未生成新final便阻断归因。完整输出均新路径，旧359f候选ready保留历史而不冒本新政策已排或已运行。

## 6. 实际静态核与未解决责任

四源AST/compile/py_compile、重复literalkey/尾空白检查已实际通过；完整pure deriver已从完整359f、892f、02875及原launcher重建两全体字节并成功verify-existing。新launcher与driver静态flags仅差既有install/print两个纯入口开关；实际完整ready的stdlib --print-command返回0。未导入科学模块、未本地运行fixture/F/J/QP/根/interval。

尚未获得新方向的QP驻点、SOC成本或真收益；actual05原Pg/tol显示原64步未驻，不能预填改后更快或更准。本入口仅把一个有实际依据的完整非线性globalization政策正确接到当前同g/同norm/同空间。最终低误差全域metric、全t几何、0.2D幅度、reach及固定参数精化依然全部未完成。
