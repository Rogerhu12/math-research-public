# R462 — 同一准确 C 下旧模态完整远端族与新增模态传播的联合

作者：geometry agent（AI）。日期：2026-11-16。

**状态：已证明（限下述条件命题），另交三个独立执行源码；未执行。** 本文没有实际新的 M、父对象、行值、时间收益或接受结果。现有 R450/R456 仍只实现固定 112 的 same-far；现有 R442/R457 仍实际传播其完整 M。本文的 sampler/client/worker 使用独立来源，尚未注册进原 M driver/owned caller；不修改上述已发表源或 request207 首版，也不把旧输出改名为本次增 M 联合。

所回答的问题是：在同一 job 保留了原完整 112 模态的远端族、原 numerical rows、全部误差与 raw 时，增加 M 是否必须再次传播旧 112 模态？结论是在下述准确对象、坐标和来源条件下不必。**新增模态仍须真实传播，全 M 的适用条件、完整新采样及全 native/BVP/J/FD/final 责任不减少。** 该条件不是原求解的新门；不能满足时可保诚实未付或沿原完整 M 路径计算。

## 462.1 固定的准确对象与两种不同的深端来源

令 $\mathcal C$ 为同一 R286 约定 C 下全部允许准确根选择所定义的径向函数族。它由同一原 ready/config、160×9 有限头、原 warp、cut/cuff 与原累计 primitive 定义固定。索引 $\zeta$ 表示一个允许的全局根选择；本文所有包含都对同一个 $\zeta$ 一致解释，不在每模态、每单元或每一级另选中心。

令旧模态数 $M_0=112$，旧物理频率集合

$$I_0=\{2,4,\ldots,224\}.$$

新模态数为明确有限整数 $M_1>M_0$，完整新集合与新增集合为

$$I_1=\{2,4,\ldots,2M_1\},\qquad I_+=I_1\setminus I_0.$$

M 是有限场分辨率，不进入原准确 C 的定义。改变 M 不自动给更高频率一个已付深端结论：原 R312 统一常数的已证范围是旧 112；新增频率必须由 R442 的真实全 M 适用范围覆盖。这里采用最窄的实际执行方案：仍从同 C 真实产生完整 M 深端结果，保其全部 mode rows、实际 `exact_theorem_applicability`、原 R312/R442 proof 身份和所有失败/后缀；只是有限头 ODE 不再对旧频率重复运行。

旧频率的原完整有限远端族继续由它实际旧深端 proof 和旧传播来源支持；不能把它们重标成由新 R442 deep rows 重新传播的结果。新深端适用条件成立并不要求新、旧两个合法区间盒逐字相等；二者分别包含同一准确函数族的相应对象。联合来源明确保存这种区别，不人为把两盒取某个共同中心。

## 462.2 真实原源的可分离位置

实读的完整已发表路径如下，均未执行或修改：

- [R450 固定112复用证明](R450-same-family-finite-far-reuse-and-fresh-native-sampling.md) 与 `geometry_20261116_current_C_same_far_resampling.py`。
- R456 `geometry_20261116_current_C_same_far_registered_resampling.py` 的 `bind_original_far`、`fresh_grid`、`sample/configure`。
- R442 `geometry_20261116_stored_continuous_C_M_far_graph.py` 的 `requested_modes/finite_mode_bound` 与完整深端输出。
- R442 `geometry_20261116_stored_C_finite_M_head_pruefer_positive.py` 的 `bind_inputs`、`initial_column`、完整原 C/stream/cut/far binding。
- R442 `geometry_20261116_current_C_M_pruefer_joint_radial_sampling.py` 的 `choose_far_radius`、`finite_point_required`、`point_column`、`prepare_far_tubes`、`oriented_unit_far_row`、`momentum_rows`、`radial_grid` 和 `main`。

实际 `point_column(far,data,required,by_panel,geometry,args,budget,…,r_far,mu)` 对一个给定 $m$ 推进。其准确系数来自同 C 几何和该 $m$，初列来自该频率的真深端 row，目标是显式 `r_far`，动量坐标是显式 `mu`。它不读其它模式的数值行，也不读未来的 `steps` 或角积分 N。

真实 `radial_grid(r_far,r_cut,steps,M)` 在全模式行形成之后执行。M 在该函数中用于完整 mode-count 说明；576 stage 的实际半径字由实际两端点和原 binary64 运算次序形成，steps 决定原 RK/audit 参数字集合。随后所有真实场样本、node μ 和 port、全 M native 矩阵重新产生。

因此已有源确有“单模态完整远端族”与“后继完整有限非线性程序”的分界。它不是靠低成本猜测，也不是仅从数学形式推断代码已经泛化。下文同时列出当前不能直接复用的实际绑定/索引断口。

## 462.3 单模态物理列不依赖所保留的其它模态数

对于固定准确 $C_\zeta$ 和物理频率 $m$，令 $w_\zeta(r)$ 为原径向背景。原零响应齐次方程在物理坐标中是

$$
u_{rr}+\frac{w_r}{w}u_r-m^2\frac{w_r}{rw}u=0.
$$

用通量 $j=wu_r$、原有限头参数 x，以及 $D=R_x$、$q=w_x$，它成为

$$
\frac{d}{dx}\binom{u}{j}
=\begin{pmatrix}0&D/w\\m^2q/R&0\end{pmatrix}\binom{u}{j}.
\tag{462.1}
$$

式462.1含 m 和同一 C，**不含全系统截断数 M**。所选原深端 admissible 列来自同一完整根族和同一原 $Q_F=1$ 正取向合同。对任何包含该 m 的更大有限系统，这仍是完全相同的单模态物理对象。

原 Prüfer 表示保持

$$ (u,j)=\rho\,\operatorname{diag}(1,2^b)(\cos\phi,\sin\phi),\qquad \rho>0.$$

完整 lift、正幅度、二幂换帧和每个可能反像候选的误差仍分别由原 R380/正端点与 R357 证明支付。增加 M 不授权丢掉某个候选、缩窄旧角盒或用数值中心代替全族。

这个单模态独立性只用于远端边界族。后继非线性 native 方程可耦合不同频率，故它不允许复用旧响应、旧 J、旧 H、旧 QR 或非线性收敛结论。

## 462.4 必须同时固定真实物理远端和同一个 μ 字

令 $r_f$ 是旧完整采样器实际使用的正 binary64 远端字，视为准确二进有理；令 $\mu_f>0$ 为旧 node-mu 末字，同样作为准确坐标常数。旧完整 far point enclosure、所有反像闭叶、原数值四分量及其误差仍在本 job，不能只有 SHA。

原坐标变换为

$$H_m=r^4Q_m,\qquad H_{m,r}=m^2r^3Q_m+\frac{\sqrt{12}\mu}{r^4w}\Pi_m.$$

把同列关系 $uH_{m,r}-u_rH_m=0$ 除去准确正幅度，得到原同取向行

$$
R_m=\left(
m^2r_f^3\cos\phi-\frac{2^br_f^4}{w}\sin\phi,
\frac{\sqrt{12}\mu_f}{r_f^4w}\cos\phi
\right).
\tag{462.2}
$$

式462.2第二分量显式含 $\mu_f$。新增模式也必须把**同一个旧 $r_f$ 字和同一个旧 $\mu_f$ 字**作为参数交给真实 `point_column/prepare_far_tubes/oriented_unit_far_row`，不能先重新 `choose_far_radius` 或重取 far midpoint/exp 再复制旧 Q/Pi 行。

旧 $\mu_f$ 是明确有限动量坐标的合法正常数，不要求它恰好等于某个准确 C 成员的函数值。旧 far 四项包围继续说明原数值代表与全部准确量的差。冻结这个表示不会收窄准确族；它只固定坐标。除 far 外的新网格点仍重新取原实际数值样本和坐标字，所有 port 用新相邻字形成。

若希望改 $r_f$ 或 $\mu_f$，便不满足本薄复用条件，不能把它包装为 same-far。必须按真实新坐标重新传播/变换并支付全部误差，本文未实现或假定该更宽转移。

## 462.5 旧行误差的包含保持

对 $m\in I_0$，令 $\mathcal I_m$ 为原全部候选，准确单位取向行

$$U_{m,i}(\zeta)=R_{m,i}(\zeta)/\|R_{m,i}(\zeta)\|_2.$$

原完整来源已证明每个分母严格正，给完整盒 $\mathbb U_m$ 和实际数值字 $\widehat u_m=(\widehat a_m,\widehat b_m)$，以及原误差盒 $\mathbb E_m$，使

$$U_{m,i}(\zeta)\in\mathbb U_m,\qquad U_{m,i}(\zeta)-\widehat u_m\in\mathbb E_m$$

对所有允许 $\zeta$ 和所有可能反像候选 i 成立。旧行的全候选、取向、norm、spans、commits、deep proof 和 numeric representation 均属于这个断言，不能只拷两个数字。

若准确 C、m、$r_f$、$\mu_f$ 和原深端合同不变，462.1与462.2所定义的准确行集合就未变。原数值两个字也未变，所以原差值集合未变。故原包含式在新 M 中逐模态原样成立。

旧数值代表不必位于单位行盒内，更不必由一个共同全局 $C_\zeta$ 同时实现；原 joint source 已明确记录此限制。本文既不加强它，也不因新 M 重新选出一个“更漂亮”的旧代表。

## 462.6 新模态的完整责任

每个 $m\in I_+$ 必须使用本次真实 R442 全 M deep row，保它实际的适用范围/全根族包围和 source/proof identity；然后沿同 C 完整源片及**旧实际 far 点的全部可能逆像闭叶**，真实执行原 R380 正幅度/全 lift 比较。

旧逆像叶可以复用，因为它们描述的是同一准确径向函数族在同一个准确半径的全部反像，定义不含 m 或 M。必须保原完整 leaf span、每个实际 source panel、source piece 和闭端点，并与本次使用的完整 C cover 字节和语义 binding 相符。不能把一片 nominal inverse 或旧代表角当作新模态全部路径。

每个新增模式仍须：

- 从它自己真实 deep row 初始化，不从旧 m 的列或低频延拓。
- 完整覆盖所有 required panels 和 far inverse candidates。
- 保原 prepared/commit 事务，只有 commit 范围属于已付传播。
- 对每个候选先用其正幅度/相关 norm 下界形成同取向单位行，再作完整 hull。
- 只在全部族/候选责任已付后形成本模式的实际 joint nominal row，并保相对**整个**准确单位行族的误差。
- 任何失败保当前频率、stack、last-paid、未提交 span、未访 source/模式后缀，不能因为其它频率已完成而将新全 M 标 complete。

本次仍可重新给全 M deep 适用条件，而仅对 $I_+$ 支付有限头传播。它并不把旧行的证明来源换成新 deep 文件；新全M deep中旧索引可真实存在但未作为本次新传播的初列使用，必须如实说明。

## 462.7 联合定理及不能冒领的共同实现

**命题。** 若462.1–462.6的全部来源/包含条件成立，则按物理频率顺序联合旧 $I_0$ 完整行族与新 $I_+$ 完整行族，得到完整 $I_1$ 的合法有限远端近似和逐行误差。

**证明。** 对任意同一个允许 $\zeta$，每个旧频率真实单位行由462.5落在其原盒和原误差盒内；每个新增频率真实单位行由462.6落在本次新盒和新误差盒内。两集合不相交且并为 $I_1$，所以所有行同时包含该 $\zeta$ 的相应准确值。各行的独立区间外包可再形成 Cartesian 外包；丢失跨行相关性只会扩宽，不会遗漏任何真实全向量。证毕。

这个结论是**所有真实共同 C 向量被联合外包包含**。它不等价于“联合盒中的每个向量都来自某一个共同 C”，更不等价于实际数值代表矩阵就是某个共同 C 的准确边界矩阵。不能由全行 complete、单位行各自 norm=1 或 native 小残差推出后者。

同样，所用有限物理 far 近似不是已证无限非线性 DN；原高频/截断/几何误差责任保留。联合不生成新响应/J/H 或接受证书。

## 462.8 新矩阵的准确索引嵌入

新有限状态顺序是

$$z=(Q_1,\ldots,Q_{M_1},\Pi_1,\ldots,\Pi_{M_1}).$$

对物理模式 $m=2(i+1)$，零基 i 的完整行仅在列 i 与 $M_1+i$ 有两个系数。旧112矩阵的 Pi 列从112开始，新矩阵的 Pi 列从 $M_1$ 开始；不能把旧112×224原矩阵整体放到新矩阵的前224列。

令 $J_i:\mathbb R^2\to\mathbb R^{2M_1}$ 是把两个分量放到 i 和 $M_1+i$、其余为零的坐标嵌入。它是线性等距嵌入，因此

$$J_i(U_{m,i'}-\widehat u_m)=J_i(U_{m,i'})-J_i(\widehat u_m).$$

原两分量误差盒在该两列原样保留，其余零列的误差准确为零；这不需要任何新数值容差。旧两个实际 little-endian 字逐bytes保留，包括负零。其它明确零列按新矩阵布局产生。新增行按本次原数值行形成器的真实两个字填入对应位置。

新完整 $M_1\times2M_1$ 矩阵必须保每行来源和字身份；旧矩阵本身 bytes/SHA继续保在旧来源里，新矩阵当然有自己的不同尺寸/bytes/SHA。把“旧系数字保持”写成“整个旧矩阵bytes直接等于新矩阵”是错误的。

## 462.9 现有代码不能直接被当作该联合实现

真实断口如下，不是新的科学门：

1. **R450/R456 `bind_original_far`。** 它要求 `MODES=2..224`、旧 schema、完整112 geometry 和原 `actual_original_input_binding == data['binding']`。新 R442 data 的 deep source、模式数和 proof 不同，不能拿新 data 硬填这个等式，也不能改旧对象的字段冒原 bytes。最薄实现应先按原旧合同完整绑定旧 far，再另读完整新 M 输入，最后比较同一 C/cover/cut/far 坐标子合同并保存两个独立完整 binding。
2. **M `momentum_rows`。** 原实现枚举 rows 从0开始，并按 `m=2*(index+1)` 和 `len(result)==M` 解释完整集合。直接传新增后缀会错误映成从 m=2 开始；传全旧rows又会重新形成旧代表。新薄形成器须使用真实 `physical_frequency//2-1` 的全局索引，只对新增频率调用原 `N.form`，旧两个数值字与全误差保持原件。
3. **`radial_grid` 之前的 anchor。** 原 main 会 `choose_far_radius`、重新 `InverseSampler.sample(far)` 和形成 μ。联合分支必须显式使用已绑定原 far/μ/样本/全部叶，不能只是跳过传播循环却仍偷偷改远端表示。
4. **完整 geometry/result 来源。** 新输出是联合对象，必须独立 schema/source，列清复用和新算模式、两类 ledger 根目录/身份、实际新矩阵与全 M dimension；不能继续使用 R450 的 `M_changed=false` 或原 M sampler 的“本次全M传播”表述。
5. **后继 caller/worker/client。** 旧 M worker/client/owner按其原 sampler身份绑定；联合来源必须另明确注册才能执行新 native。不能 monkeypatch旧源全局后仍声称原source未变。本条不要求复制或改写原数学 kernel。

## 462.10 最薄独立执行组合

据现有函数边界，本次实现限制为一个独立联合 sampler 与必要来源薄层，保持原 M native/QR/bridge/完整 BVP 数学本体：

- `geometry_20261116_current_C_incremental_M_far_union.py`：`sample` 完整绑定、联合与新采样；`configure` 只产生真实新 client 配置；`readback` 仅读原元数据。
- `geometry_20261116_current_C_incremental_M_native_worker.mjs`：完整原 M worker 的独立 sampler/result/geometry/source 身份视图。
- `geometry_20261116_current_C_incremental_M_tail_client.py`：完整原 M client 的独立 config/worker/source 身份视图。

它们具体实现如下，最后完整 BVP owned caller 的注册仍单列未付：

1. 读原 same-job完整112 sampler/geometry/row文档/矩阵/far样本与全部原账，沿原旧合同确认原 complete 范围。旧大账逐完整流bytes/SHA/行数绑定；小 mode/row/anchor对象完整读入，不能只相信旧 summary。
2. 读实际新完整 M deep 与同一原 C cover/point query；原 `bind_inputs` 支付全M适用条件、原1440片、同自然域cut与完整根族。保两个完整 binding，新 union binding 只把同一 C/raw/坐标关系逐项连接。
3. 以旧 far 真实全 inverse leaves 构造新 required/by_panel；仅对新增 m 调原 `point_column`，保持同一个 old μ。
4. 当旧完整族与所有新增完整族均有时，形成完整联合行文档和新 $M_1\times2M_1$ 字矩阵。旧行源/误差不改，新行各自保 `N.form` 与全候选误差。
5. 按明确新 N/steps 调原新 M `radial_grid`，除已声明旧 far 点外，其余每个实际 node/field radius 真走原 `InverseSampler.sample`。实际四分量、数值word差、node μ/port 与全field occurrence完整产生。
6. 新 worker/client诚实绑定union sampler，保原完整 M native 残差/敏感度/两mean 算法。后继独立 owner/driver 仍须真实注册该 tuple 并重新运行完整 $(3M+2)\times M$ 端响应、新 frozen $(4M+2)$ BVP/FD/fullDN/final/audit；本包不包含这项尚未完成的调用者接线，原接受公式不变。

原 source loaders 可能用相同临时模块 tag。薄实现应在完成旧 binding并把所需值保为原 JSON/bytes后，再加载新 M runtime，或明确独立模块名；不能让一个新 class 的 source 身份冒成先前旧 class。该工程安排不改变数学核。

源码的 `bind_old` 先用旧 `data` 调原 R456 `bind_original_far`；`bind_union` 保新旧完整 binding 并比较同一原 C/cover/cut 子合同。`new_numeric_rows` 使用实际全局频率索引，`materialize_rows` 逐旧字重排 Π 列；`fresh_grid` 仅预置原 far 样本，其余原网格仍走真实完整逆像采样。`configure` 明记新 caller 注册仍须完成，既不调用 native，也不声称已运行 BVP。源码及全部实际 pin/CLI/输出合同见同行接口；完整数学结论不以未来运行成功为前提。

## 462.11 原钟、资源与必要读回

旧传播的完整读入也消耗本 job实际时间和盘预算；复用不承诺零成本。原18900科学钟、实际deadline、读回预留及 TERM/KILL/quiet 合同不能重新开始。新增传播的work计数只记实际新增模式；旧 accepted panels/时长仍在旧来源中，不能并为本次新算数量。

原旧 binding 中途停止时保当前文件/已读字节/未读流后缀。新增模式停止时保原完整传播栈、last-paid、当前事务、全未访模式。新grid尚未启动时整份grid责任未付；启动后保真实node/stage/field地址和完整后缀。全部必要错误/未付保留，成功大数组只保原身份范围，原raw在同job真正所有读回/quiet以前不删。

单90KB是传输限制，不是科学接受门。极端未付范围超过它仍须诚实70，不分块编码大raw，不以只剩身份冒已读必要正文。这里没有新增fixture、独立audit门或固定数值成功前置。

## 462.12 当前结论和未付项

已经证明：同准确 C/全根族、同物理 far 字、同正 μ 字、同单模态取向与完整旧误差下，增 M 不改变旧单模态的准确远端族；旧系数按新 Pi 列偏移准确嵌入可与真实新增模式构成合法全 M 外包。原代码具有按模式推进的真实函数边界，所需新来源/索引断口也已精确定位。

已提供而未执行：独立增 M union sampler、完整 CLI、原绝对钟的协作检查、新 config 与 native worker/client 来源视图。尚未完成：原 M driver/owned caller 对此 tuple 的真实注册；任何实际新 M 行/网格/native/BVP；节省时间效果。协作检查没有替代外层 OwnedChild 的硬终止、join、quiet 和必要读回责任。原 R450/R456 `M_changed=false` 保原义，原 R442/R457 完整 M 路径仍可继续实际运行；request207 不等待本探索。

准确全局 C realization、无限非线性 DN、旧/新准确场的度量/reach/held/δE及真正同g精化证据，仍由各自原责任完成。联合远端族的成功不能替代其中任何一步。
