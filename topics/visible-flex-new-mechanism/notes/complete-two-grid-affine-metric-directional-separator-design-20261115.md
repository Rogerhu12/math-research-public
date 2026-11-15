# 完整两网 affine-e/f 方向分离器：新模型设计（2026-11-15）

**状态：纸面与源码接口设计，尚未执行新人工或研究。** 当前模型事实来自公开 run 43722283235/source bb33192ccd5866280ffed6c13a02febd29d8f361；原始数据已完整消费，见[首 actual](affine-spectral-metric-model-first-actual-20261115.md)。本稿提出一个明确新增机制。所有新执行仍仅由本公开仓库 Actions 完成。

## 1. 本次真正未付的问题

首 affine 阶段已经在每次返回前准确评价全部 **已选** 行的 $\phi_\pm(e+de\,p,f+df\,p)$，因此没有把切面 LP 的低估当成该 selected 模型的实值。然而模型没有覆盖所有原有限网格行。第6模型的已选 actual smooth slack 为0.006401949477886082，全两网为0.006417428768619948，差 $1.5479290733866335\,10^{-5}$；同点还有4个已选曲率行真失败。第5模型没有上述遗漏，主误差是已选 $e,f$ 的真实非线性。

新增目标是：**在相同接受中心与当前方向 $p$，用解析 JVP 评价两张完整原网的 affine-e/f 范数，并返回真实最大值及其原行 ID。** 它不增加参数，不放宽原曲率门，不修第5模型的非线性误差，也不声称会提前发现首 actual 的特定第6漏行——旧报告没有保存那个原行的中心 de/df，不能事后推定。

继续保持：固定 $g,b_0$、同 runtime Field、精确 $H$/参考、159独立/163物理坐标、完整粗384/细768原角网、160原径向点、原两网14门、原11行组与池整数ID、原实际 SOC 方程与全部17持径条件、原精确物理盒，以及每阶段 **12次共享LP／120 active秒／40共享完整值**。每 outer 仍最多3次 primary inner LP。没有扩容量或信任半径重置。

## 2. 精确有限模型和四个新增凸函数

设 $x$ 是冻结接受中心，$\mathcal G_c,\mathcal G_f$ 是原两张完整有限网格，原点 $i$ 有

$$
U_i=X_s(x;i),\quad T_i=T(x;i),\quad
e_i=|U_i|^2-1,\quad f_i=U_i\cdot T_i.
$$

方向 $p\in\mathbb R^{159}$ 的真实解析一阶值为

$$
\dot e_i[p]=2U_i\cdot\dot U_i[p],\qquad
\dot f_i[p]=T_i\cdot\dot U_i[p]+U_i\cdot\dot T_i[p].
\tag{1}
$$

仅在参数上取 affine，而保留谱范数：

$$
E_i(p)=e_i+\dot e_i[p],\quad
F_i(p)=f_i+\dot f_i[p],\qquad
\phi_\sigma(E,F)=\frac{\sigma E+\sqrt{E^2+4F^2+\varepsilon^2}}2,
\quad\varepsilon=10^{-8}.
\tag{2}
$$

各点函数凸。定义恰好四个凸函数

$$
\Psi_{\gamma,\sigma}(p)
=\max_{i\in\mathcal G_\gamma}\phi_\sigma(E_i(p),F_i(p)),
\qquad \gamma\in\{c,f\},\quad \sigma\in\{+,-\}.
\tag{3}
$$

新完整模型的最小 epigraph slack 是

$$
\rho_{\rm full}(p)=
\max\{0,\rho_{\rm out},
\Psi_{c,+}(p)-\eta_*,
\Psi_{c,-}(p)-\eta_*,
\Psi_{f,+}(p)-\eta_*,
\Psi_{f,-}(p)-\eta_*\},
\quad \eta_*=13/50.
\tag{4}
$$

外域 $\rho_{\rm out}$ 完整保留；它虽已被相同全网最大值覆盖，仍按原常域证明显式保留。原 support 外方向严格为零，不能把它删出检查或改成可优化变量。

新模型的初始值采用同一完整原网的 $\rho_{\rm full}(0)$。同时记录旧 selected 初始slack和两者差；不能默认旧 selected 集必然含全部初始最大行。原 primary 的 hard rows、原 scalar rows、盒、物理尺度和 norm auxiliary不改变。

### 2.1. 真正的分离切面

设 $i_*$ 是 (3) 在当前 $p_*$ 的一个最大点。按原 flat row ID 递增打破浮点并列。则

$$
g_{i_*}=
\phi_E(E_{i_*},F_{i_*})\,de_{i_*}
+\phi_F(E_{i_*},F_{i_*})\,df_{i_*}
\tag{5}
$$

是该分支最大函数的一个 subgradient；全空间上

$$
\Psi_{\gamma,\sigma}(p)\ge
\phi_\sigma(E_{i_*}(p_*),F_{i_*}(p_*))
+g_{i_*}\cdot(p-p_*).
\tag{6}
$$

只需为这个真实原点补一次完整159 de/df行，就能加入正确的原单位约束

$$
g_{i_*}\cdot p-\rho\le
\eta_*-\phi_\sigma(E_{i_*}(p_*),F_{i_*}(p_*))
+g_{i_*}\cdot p_*.
\tag{7}
$$

不是对新未知的网格插值，也不是把有限采样当连续曲面证书。正负分支的原行组分别仍为0/1。

每次 inner 最多新出现四个 branch-attainer ID。原 selected 违规切面照旧保留；若新增attainer已经有原 selected de/df，直接复用该准确行。相同切面的原数组哈希按冻结 solver 的规则去重，不能仅按行ID去掉不同接触点的有效切面。

## 3. 一次方向 JVP：只使用真实原径向场和完整角投影

旧 SingleQProblem.geometry 没有单方向入口；jacobian=True会构造完整163列。FiveHeightField随后拼成159列。因此禁止把一个方向伪装成新旧163 state，也不更改旧grid的参数个数。

本次直接使用已发表原导数式。对 $u$、$v$ 两个切向场，在冻结当前 state 的原完整角网，令

$$
\delta q=\sum_{\ell,m}R_{q,\ell}(s)Y_{q,m}(\theta)p_{q,\ell m},
\qquad
\delta q_s=\sum_{\ell,m}R'_{q,\ell}(s)Y_{q,m}(\theta)p_{q,\ell m}.
\tag{8}
$$

$u$ 为9径向×9角列，$v$ 为9×8，再单独加原 $Q$ 一列。所有 $R,R'$、角基和 $Q$ 准确使用冻结 SelectedRadialJacobian._families 的原入口，绝不从有限差分生成。null高度五坐标独立处理。

从原 target_frame 的 Tpart、Ts_value_part 有

$$
\delta T=\sum_{q=u,v}T_q\,\delta q,\qquad
\delta T_s=\sum_{q=u,v}
\bigl((T_s)_q\,\delta q+T_q\,\delta q_s\bigr).
\tag{9}
$$

这里 $(T_s)_q$ 正是冻结 frame 中 Ts_value_part，包含当前全部场的链式导数。先在全部原角点形成 (9)，再用**同一个** periodic_operator(order=-1)：

$$
\delta U
=a_s\Pi_N(\delta T)+a\Pi_N(\delta T_s)
+e_z\sum_{\ell=1}^5D_\ell(s)p_{154+\ell-1}.
\tag{10}
$$

$D_\ell$ 为原 exact-null 高度密度，不是将 $H p$ 四舍五入成九新高度系数。式 (10) 不要求或使用 $\partial_\theta\Pi_N=\mathrm{id}$；原zero/Nyquist处理全部保留。粗、细各自用完整384/768角网，不能先挑点再投影。

式 (1) 中 $U,T$ 来自实际 current159 ordinary cache，特别 $U$ 包含当前五null高度。不能改用 reference163 的旧 $U$。当重放标量场时，reference163只用于当前154切向系数和原参考高度；它不提供新高度普通值。

### 3.1. 批次、身份和不变的普通值

按原 owned radial width（1至16）流式处理全部径向行，每批 query保留原首末径向端以满足旧grid API。每个 owned点恰覆盖一次、每批完整角网。使用旧普通值binding/标量重放验证同 current state、$H$、全网及 source；不调用 ordinary geometry，不构造 full-grid×159 derivative tensor。

冻结中心持有明确的 ordinary cache reference及只读 $U,T,e,f,a,a_s$ 标量/向量副本。新 actual candidate覆盖objective当前cache后，accepted-base oracle仍只读自己的中心，不能悄悄线性化于试算点。缓存key包含 center159、step159、坐标/参考/配置/两网/原评价定义的SHA；同center相同步长可复用。新center或任一身份改变即废止缓存。

各步只保存四个最大值、四个原行/坐标、对应 $e,f,\dot e,\dot f,E,F$、覆盖/重放/耗时/计数和哈希；无需保存全网机器payload。JVP是新研究计算，计入同一120秒active预算，单列导数不冒作 ordinary physical-value调用，40完整值账不增加。原始科学所有计数仍须完整单列展示。

## 4. 对冻结 inner solver 的最小接口

保留 frame_metric_affine_spectral_model.solve_affine_primary 原代码。新 CompleteGridAffineModel 是 AffineSpectralModel 的显式子类，拥有一份原 selected模型和一份完整oracle：

- primary仍是同一个原映射LP；原 scalar软行、硬行、box/norm与尺度字节不改。
- evaluated(p)用于 inner分离时，返回“原 selected $\phi$ 列 + 四个 $\Psi$”的向量及全slack。
- cuts(p,indices) 对旧列调用原切面公式；对后四列使用其真实attainer原行和 (7)。不同列给同一切面时仍由旧hash去重。
- slack(p) 始终返回 (4)，包括返回后实际总步长 $z-x$ 的预测。
- summary明确两个计数：原 selected scalar rows、4个全网max函数；不把4解释成只检查4个网格点。
- 同一接受中心的新增 de/df cache仅含真正请求过的新原行。不会把预测违约传给原 actual learn_pool API；旧池容量/ID/学习历史不变。

因旧 frozen inner只消费这个协议，可以直接复用其每次solver前计费、每outer最多3次、总12次、残差/盒判定及incumbent规则。不复制优化循环、不 monkeypatch旧模块或旧源。

**返回前全epigraph修复**仍取

$$
\widehat\rho=\max\{\rho_{\rm full}(p),\rho_{\rm LP}\}.
\tag{11}
$$

原 norm auxiliary与LP报告原值保留，向上修复后重新核所有原单位行、界和全部已加cut。不得默认任意LP的非最小rho等于旧scalar最小slack。

旧 gap规则不变，只把实评slack替换为 (4)：

$$
\max(0,\rho_{\rm full}-\rho_{\rm LP})
\le \max\{10^{-9},(\rho_{\rm full}(0)-\rho_{\rm full}(p))_+/8\}.
\tag{12}
$$

gap通过是完整**有限**网格affine模型的浮点停止准则；不是凸优化精确最优、真实几何可行或连续网格证书。若3次inner或原预算先到，只允许按原规则返回已完整实评/上调/残差核过且模型改善超过原floor的incumbent，准确标记inexact。失败和异常仍保最后真实接受点，不能宣所有异常都回proposal。

### 4.1. incumbent与以后切面

每条未来切面是原某个 $\phi_i$ 的全局支撑线，故若早期候选已经满足 (11)，它自动满足后来所有数学切面；冻结solver最终仍以真实浮点数组重新验证，而不是仅依理论跳过残差。

从同一完整模型生成的incumbent可以比较其 repaired objective。换center、J、grid、配置或pool重建会结束此模型，不能继承这份论证或绑定。

## 5. 外层、真实值与 SOC 完整保留

新objective继承当前 AffineSpectralHeight159Objective，只覆盖创建primary模型和误差报告；冻结 run_affine_spectral_recovery 原外层继续使用实际普通值、原门、原行学习、真实回退、原SOC构造与17条件控制。

必须保持 AffineSpectralModel 子类身份，以满足冻结 actual_total_step_diagnostic 的显式type门。primary.affine_spectral_model与information里的binding都指同一完整模型；signature包含完整oracle/grid/selected来源，不能使SOC误认旧selected模型。

同实际步长比较时，冻结SOC仍由原scalar minimum slack构造其实际RHS；新全affine slack只是诚实预测/诊断，不用一次LP辅助rho替代。完整全affine至少包含旧selected数学范数，故数学上不小于相同步长的selected scalar切线最小slack，但浮点实际值与比较布尔仍分别报告，不用文字抹掉舍入。base-total gain不有限或不超过原floor时，原拒绝/不可持径规则照用，不除零。

原函数少数固定metadata标签是“selected-only／inner无J”。新wrapper在报告中将这些旧字面保存在 inherited_frozen_labels，并显式改写为本次真实范围与新计数；不得留下“0 inner Jacobian”却实际作了JVP/新行J的错误。只改输出解释，不改验收或controller。

## 6. 本次可以准确验证的两种误差

旧四项分账继续调用**原 selected模型**，而非把四个max分支混成旧行序。记原selected affine slack为 $\rho_S$，新完整 affine为 $\rho_M$，selected actual smooth为 $\rho_A$，完整 actual smooth为 $\rho_F$，完整 true为 $\rho_T$：

$$
\rho_T-\rho_{L,S}
=(\rho_S-\rho_{L,S})+(\rho_A-\rho_S)
+(\rho_F-\rho_A)+(\rho_T-\rho_F).
\tag{13}
$$

新增加的确切覆盖差与完整实际残差是

$$
d_{\rm omitted,aff}=\rho_M-\rho_S,\qquad
d_{\rm geom,full}=\rho_F-\rho_M,
\tag{14}
$$

并核

$$
\rho_T-\rho_M=d_{\rm geom,full}+(\rho_T-\rho_F),\qquad
d_{\rm geom,full}=(\rho_A-\rho_S)+(\rho_F-\rho_A)-d_{\rm omitted,aff}.
\tag{15}
$$

所有项都在同一接受中心、同一实际总步长和原行定义下取得；不能比较不同最大点的单行误差冒充最大值差。完整 $d_{\rm geom,full}$ 可正可负。一次成功覆盖不能保证原曲率PSD或直接κ门通过。

保留全部norm direct/stable舍入报告与epsilon偏差，不裁负值。只实际有fine时作完整两网分账；coarse-only保准确部分范围，不借缺失fine。每次调用和cache命中、oracle/选行J耗时分别记录。

## 7. 来源复用与新增文件范围

拟新增四个独立源，不修改上述冻结源：

1. frame_complete_affine_metric_oracle.py：完整方向JVP、四max、同center绑定/缓存、新attainer de/df及 CompleteGridAffineModel。
2. frame_metric_height159_complete_affine.py：新配置/显式objective子类、(13)–(15)、冻结outer调用和准确metadata。
3. frame_complete_affine_metric_development.py：只下节新增人工。
4. frame_metric_height159_complete_affine_audit.py：必要旧九阶段输入生产一次、严格same runtime handoff、唯一新增stage、临时输出/摘要。

前三个核心已有依赖为本次已付的 SelectedRadialJacobian/SelectedMetricObservables、AffineSpectralModel、FiveHeightField/原null basis、原SingleQ/EntryRepair/target_frame/periodic_operator、原mapped LP/true门。实际部署给完整递归SHA，不用历史根hash猜当前。

新的第九恢复是刚已付的完整affine阶段，包含其八段必要输入生产，全部各一次。新driver必须在显式编排中持有同一 prepared runtime，不从JSON重造新 Field/H，不向旧driver注入 monkeypatch。原完整池/capacity history/source/accepted159/精确163/固定metric/b0/全两网/真实controller逐项核后续接；原终点低于min或不可用仍按原门退出，不重置。复现过程中浮点终点不强迫等于历史run。

源、设计、参数和人读结论入库；研究完整输出仅runner临时，发布source/run/size/SHA。98个research参数和24旧输入保持原数学含义，只有out改新临时名；新增策略由冻结新源定义，不加求解器预算旗标。

## 8. 最小新增开发检查（仅Actions）

不重旧35项或旧scientific suites。新增检查只覆盖新功能：

- 小全网JVP：真实原8/16角、小合法径向fixture，独立方向159对原全J收缩或新小有限差分核 de/df；明确只人工有全参数参照，生产无此张量。含u/v/Q/null混合方向、正负side、当前非零null高度及原边界。
- 原Π顺序与grid绑定：全角后收缩、端/外域方向零、错误中心/参考/角网拒绝、coarse裁剪cache/fine完整cache。
- 完整4max和subgradient：小标记数组中selected遗漏真正最大点、分支tie原ID、attainer换位、同ID切面复用、相同切面hash去重；每个新cut接触值/全凸不等式用人工有限点。
- 冻结inner协议：selected+4行拼接、共用ledger、最多3inner/12总、全rho上调、早期incumbent对后来全网cut仍满足、预算/失败诚实返回；stub次数与真实LP0分开。
- 误差 (13)–(15)：已知人工分量、coarse-only不填fine、同step缓存命中、真实候选cache替换后中心仍不变。
- 新第九handoff/字典pipeline：旧九恢复每段一次、same Field/H、真实controller逐条重放、原错优先传播、没有强迫历史stateSHA、临时out cleanup。

所有人工入口只验证新接口和公式，不把其成功当实际模型收益。

## 9. 首 actual 必须给出的内容与边界

必须完整打印新开发各组/异常，九恢复与唯一新阶段分账；每个outer/inner的LP ordinal、4max原行坐标、JVP覆盖/hash/费用、旧selected与全网slack、接触与追加cut、gap/返回rho/原残差；每次真实trial的(13)–(15)、原14门与精确盒、实际SOC调用及RHS/17条件。若预算未完或错误，只报已观察的范围。

最有用的实际问题是：当前提案遗漏的 **affine** 最大行是否在试算前被识别并切回？如果仍有实际漏峰，(15)能判断它来自完整e/f非线性或模型gap，而不把旧selected漏行笼统归因于曲率。未执行前不宣速度、下降或收敛改善；即使全网模型可行，主课题完成标准仍远未自动满足。

