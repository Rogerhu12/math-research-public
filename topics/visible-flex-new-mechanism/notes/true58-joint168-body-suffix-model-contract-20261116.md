# true58：完整 168 控制的主体原 selected 池与整个后缀联合模型

日期：2026-11-16。预声明 policy：**true58-joint168-body-suffix-v1**。

本文件约定一次新的公开 Actions 科学范围。源码只作文字构造；发布前不在本地导入、编译、测试或执行模型。真正的值、导数、初始尺度、求解、失败与实际候选检查均属于这一新范围的公开科学钟。

## 1. 新问题与已关闭范围

此前 full62 的 62 个独立控制只以整个后缀 minimax 为后端问题。该范围已经真实结束：run 43916013327 / job 133470222034，SLSQP 原返回 status 0、success true、nit 54、nfev 70、njev 52；其细网格直接 metric 值 0.26600531463999494 高于原预算 0.26600531463999305，所以没有合格候选、没有全主体预测或 actual，accepted index 仍是 58。祖先完整账为 **3757.97482037 秒 / 147 个原 full 值**。父记录只有真实保存的字段与成本；不可由 shape/hash 恢复未输出科学数组。

本轮同时作两项实质改变：

1. 开放原完整 168 个独立控制，而不是从旧 62 维返回点继续。
2. 在同一个实际 q168 上联合约束 accepted58 永久 selected 主体池的全部原 11 组行与整个原后缀的双网格六行。

本轮唯一初点仍是真正 accepted58。旧 full62、full51、whole34、prefix102 的失败、钟停、callback、末已评价点均不能充当本轮新初点或候选。新范围不是给已关闭求解加时、改名重跑、重开旧后缀模型，也不预称 accepted59。

完整主体池仍是有限 selected 池。其后还须原规范全主体预测与至多一次原 actual 双网格检查；离散门不构成全时、全域 reach、embedded 或严格等距结论。

## 2. 三个源码的真实职责与公开接口

源码位于本题 scripts：

- [frame_metric_current168_joint168_body_suffix.py](../scripts/frame_metric_current168_joint168_body_suffix.py)：固定范围、输入身份、完整准确仿射坐标、原盒、norm、边界、模型对象与紧凑摘要。
- [frame_metric_current168_joint168_body_suffix_geometry.py](../scripts/frame_metric_current168_joint168_body_suffix_geometry.py)：共享完整 scalar/frame/角原函数、主体与后缀的值、实际曲率及解析 Jacobian。
- [frame_metric_current168_joint168_body_suffix_solver.py](../scripts/frame_metric_current168_joint168_body_suffix_solver.py)：单一 SLSQP、真实限额、当前缓存、原返回保存、资格判断及失败/部分完成收据。

这是按真实源码职责拆分，每个文件小于 100000 字节；不拆分、压缩、编码或分块转移科学数据。旧来源源码不修改。

外部使用下列接口：

    model = build_joint168_body_suffix_model(
        prepared, completed, first_jet_bounds, metric_bound,
        wall, capture,
        metric_budget=original_budget,
        internal_metric_budget=internal_budget,
        charge_prepare=charge_prepare)

    solution = solve_joint168_body_suffix_once(
        model, wall=wall, charge_solve=charge_solve,
        emit=emit, capture=solve_capture,
        solver_seconds=1200., maxiter=240,
        max_evaluations=480, max_backend_evaluations=960)

    record = joint168_body_suffix_capture_record(
        capture, include_arrays=False)

    summary = model.summary()
    model_record = model.full_record()

模型类为 Joint168BodySuffixModel；模型本身不依赖旧 full62 scope 的账本类。父 wrapper 独占 scope、transfer、audit、actual、report、workflow、request 与所有 Git refs。

solution 保留 status、report、qualified、qualified_candidate、candidate168、candidate、candidate_record、actual_backend_raw170、backend_success、backend_status。qualified 为假时 candidate168/candidate 为 None；有限真实返回的 candidate_record 仍保存，不因不合格丢失原返回坐标。

内部 emit 只发一次 **NONLINEAR_RESULT**，且仅在真正 OptimizeResult 已返回时。SOLVE_TRACE、BODY_SOLUTION、MODEL、MODEL_PARTIAL、SOLVE_PARTIAL、COMPLETE、FINAL 均由父 wrapper 按其所有权输出，不能重复同 tag。

## 3. 准确独立坐标与物理 172 仿射像

后端变量依次为

\[
x=(z_0,\ldots,z_{167},K,h)\in\mathbb R^{170}.
\]

令 Q 将一个实际 binary64 解释为其准确有理数。每一个独立坐标按

\[
q_i=\operatorname{RN}\!\left(Q(q_{58,i})+\frac14Q(z_i)\right)
\]

由准确有理和作一次 binary64 舍入。不能先舍入增量再相加，也不能为符合约束修改真实返回 z、K 或 h。

原独立布局完整保留：

| 独立索引 | 原物理意义 |
|---|---|
| 0–80 | 原 9 个径向函数 × 9 个 u 角模式 |
| 81–152 | 原 9 个径向函数 × 8 个 v 角模式 |
| 153 | 原 W5 B3 normalized Q 角方向 |
| 154–158 | 原完整五维 exact-null height |
| 159–162 | 原新增 body u 四模式 |
| 163–166 | 原新增 body v 四模式 |
| 167 | 原 body height 方向 |

令 F 为原 field.full_coefficients(·, exact=True) 所定义的 168 到 172 的准确仿射映射。前 154 个物理行保持恒等；九个 physical height 行使用原永久参考加原完整 H9×5；末九个 body 行保持恒等。

未舍入物理点与实际物理点分别为

\[
p_{\rm ideal}=F(q_{58})+Pz,\qquad
P=\frac14\,DF,\qquad
p_{\rm actual}=F(q_{\rm RN}).
\]

其中实际九个 physical height 坐标是已舍入独立 q 的**准确有理仿射值**，不能把 172 个物理坐标分别 RN 后冒充同一个 F(q)。源码保留完整 H，包括前三个 null 方向的有理积分补偿和最后两个方向在 physical 行 162 上的 -3/2、-5/4 系数。

candidate_record 同时输出：

- 原始 backend170 的值、准确 binary64 有理数与身份；
- 未舍入独立 168、未舍入物理 172；
- 真正 once-rounded 独立 168 及其准确物理 172；
- 两种点的原盒判断、违反索引、K/h 准确区间；
- 未舍入物理 norm、真正舍入后物理 norm、二者与原 raw h 的准确差；
- 原 F/H 身份、原 accepted58 身份以及规范预测尚未执行的事实。

后端使用这一平滑仿射参数族的原解析导数；每个值请求使用实际 once-rounded q。解析导数不是离散 RN 阶梯映射的导数，也不是对舍入误差的严格包络。所有真正舍入门独立在原返回上判断。

## 4. 原盒、物理 norm 与保留的有限范围

原完整 172 物理坐标下界、上界逐个不变。344 个原盒线性行之外，全部 172 个非零物理增量行各保留两条 norm 约束：

\[
4(Pz)_j-h\le0,\qquad -4(Pz)_j-h\le0.
\]

因而线性行数为

\[
344+344+4=692.
\]

最后四行为 K、h 的上下界。本轮固定

\[
K\in[1000/61,58],\qquad
0\le h\le
\frac{18014398507545773}{281474976710656}.
\]

该 hmax 是本范围明确保留的有限限制，不声称足以覆盖完整 168 控制的原盒。不能沿用旧 free36 字段名中“box sufficient”几个字，把旧子空间的界外推为本轮完整原盒的充分界。

K 下端点只向内取 binary64：若最邻近 binary64 小于准确 1000/61，取其向正无穷的下一个值。同一个向内值用于后端 Bounds 和线性 K 行；原准确 1000/61 仍用于最终比较。

168 个独立变量的后端边界来自原物理盒的 168 个恒等或符号锚行。对每个锚行 p_j=c+σq_i，σ∈{−1,1}，先把其准确 q 区间向内包为 binary64 端点，再准确转换 z=4(q−q58)，再次向内包给后端 Bounds。前三个 null-height 锚符号是 -1，不能当作 +1。

未成为独立锚的 physical 行 157、158、159、162 仍在完整线性原盒及准确返回原盒中。该保守接线只用于原盒，不添加数值容差，不裁剪返回点，也不声称独立 Bounds 已覆盖每条耦合 height 行。

未舍入 norm 的后端线性行继续用原 LP_ROW_TOLERANCE 判断。准确物理舍入可能使实际 norm 比未舍入 norm 多一个或若干 ulp；本轮不事后增加 h、不更改 raw170 来修补这一点。最终必须另有

\[
4\|F(q_{\rm RN})-F(q_{58})\|_\infty\le Q(h)
\]

的准确真值。若不成立，真实返回不合格，两个 norm 数值与差照实保存。

## 5. 同一个 q 下的全部行与两种曲率角色

原 selected 池固定于 accepted58 的真实顺序和版本：

| 网格 | 原 selected 行数 | 永久 pool version |
|---|---:|---:|
| coarse | 4454 | 15 |
| fine | 4549 | 14 |

每个原 row ID 的含义不变：group × (Nr Ntheta) + radial_index × Ntheta + theta_index。全部 11 组保留：两条 metric proposal、signed height、ball、两条 strip、mirror polynomial、四条原未平方 PSD。不能只截取其中 curvature 或 metric 行。

后缀保留原二进制径向身份中 s≥153/200 的全部 **21 行**，包括原 radial ID 141，且两角网格分别完整 384、768 点。后缀每点保留两条 metric proposal 和四条未平方 PSD，共

\[
21(384+768)\times6=145152
\]

条。主体池有 9003 条，所以非线性 154155 条，连同线性共 **154847 条、170 列**。

源码行序为 coarse 主体池、coarse 后缀六行、fine 主体池、fine 后缀六行、692 条线性。主体池内部原顺序不变，后缀为径向主序、角度次序、每点六行。

主体曲率一直使用原硬 cap 58；只有后缀的曲率 epigraph 使用变量 K。前缀、其它主体点不偷偷受一个更低的全主体 K 约束，也不因后缀优化而删除主体原硬门。

## 6. 内部 metric 余量与最终原预算的明确区别

本轮原最终 metric budget 为

\[
b=0.26600531463999305.
\]

后端求解行使用

\[
b_{\rm int}
=\operatorname{RN}\!\left(Q(b)-1/100000000\right).
\]

父 wrapper 在新科研钟内形成这个值，builder 以相同准确有理式绑定。原 b 还必须等于已付 prefix 输入所记录的原 budget 身份。

设原 e=|X_s|²−1、f=X_s·T，原固定平滑 epsilon 不变。两条求解行是

\[
b_{\rm int}-\frac{e+\sqrt{e^2+4f^2+\epsilon^2}}2,\qquad
b_{\rm int}-\frac{-e+\sqrt{e^2+4f^2+\epsilon^2}}2.
\]

这是额外严格的内部求解要求，不是放宽接受标准。最后在真正返回上计算的未平滑

\[
\eta=\frac{|e|+\sqrt{e^2+4f^2}}2
\]

只与原 **b** 逐位比较，**不添加 tolerance，也不再与 b_int 作新的准确终门**。内部求解行仍受预先固定初始行尺度与原 SLSQP ftol；把 b_int 再作严格终门会重建贴边舍入拒绝，因此本合同明确不这样做。

每个摘要同时列原预算、内部预算、各自余量及实际 η 极大点。全主体两个完整有限网格的 η 都检查原 b，而不只查 selected 池的 metric 行。这是必要有限门；它仍不能替代规范的原完整预测与 actual14。

主体 group≥2 的后端 residual 只平移其原配置中已有的行 tolerance，使 residual≥0 对应原硬门；没有增大任何 tolerance。原始未平移值与原门判断另保留。后缀 PSD 的原 tolerance、normal area floor、独立 principal-curvature tolerance 也完全不变。

## 7. 允许读取的已付输入与不能免费恢复的内容

父 transfer 继续从原完整日志取真实 accepted58、free36、prefix102 数据。后继 closed scope 的绑定与成本可以读，未输出数组不能当作新模型免费输入。

prepared 至少包含 field168、q168、cfg、gate、radial、theta、fine_theta、原 lower172/upper172、physical_map_exact172x168、coarse_pool/fine_pool、source_binding，以及 replay.source_checkpoint 中的两个原 pool version。

completed 提供真实 state168、unaccepted_ring_state168、receipt、accepted_cache、paid_free_model、paid_prefix_model。q_R 只用作已付 scalar 数组的原身份，不是唯一初点、accepted 状态或假造的完整主体 geometry。

父 wrapper 在 builder 前一次绑定两份真正 accepted58 first jets 和一份固定 metric。builder 验证同一 q、原径向/角度、物理参考与绑定，并直接使用：

- 全网格 U、T、e、f；
- 固定 a、a_s、a_ss；
- 两个永久 selected payload 中真正保存的 X、Xs、Xt、Xss、Xst、Xtt、T 及原 point/pool 身份；
- prefix102 new_paid_input 中 q_R 的全网格 u/v value、s、ss、theta；
- prefix 已付 first6 原 W2/W5 径向数组和完整原 u/v 角模式/角导数；
- q_R 的 height b、b_s 以及对应固定网格身份。

selected payload 必须通过原 bind_selected_current168_geometry 按真实 pool 顺序、版本、configuration、物理状态与 owner SHA 绑定。其 saved point_ids 只代表原 selected 点，不可伪装为全网格 X 或二 jets。

q58、q_R、原准确 172 盒、原配置与 fixed budget 的已付身份在 builder 中逐项连接。无完整字段时真实 fail；不能由摘要、图形、checksum 或剩余 callback 造输入。

## 8. 必须新付的准备与共享实际值链

原 true57_nonlinear168 的 geometry/model/line/solver 各自带有 old57、旧半径或固定七 alpha 等域断言。本轮不修改这些旧断言后冒称原 oracle；只使用原低层几何、导数与约束公式构造新的明确计算次序。

一次 charge_prepare 付如下原来未保存的必要输入：

1. 原最后三条 quintic 径向函数的完整查询网格 0/1/2 jets。依据原准确支持，它们非零时已位于原 entry 权重恒 1 区；first6 已付加权数组不重新查询。
2. 原 normalized Q 的两角网格 value/first。其径向三 jets 直接是已付 v 的第一列 W5 B3，不另查同一径向。
3. 原 body P5/P8 0/1/2 jets。
4. 完整五条 null-height primitive、b、b_s 及原 body height primitive、b、b_s。
5. 完整准确 P、692 条线性行、向内锚边界与数据索引。

对每个实际 q，原 scalar 函数由已付 q_R scalar 加完整 168 个原线性系数变化形成。u/v 所有旧径向列、Q 列、新 body 列分别保留原支持；没有一个共同 body 支持遮罩删除其它原列。所有 height 变化经原准确 null map 输入。

共享的 frame、Ts、Tss、Ttheta 与同一完整角原函数 Pi_N 为主体与后缀共同生成。真正 q58 已付 T 不重形成；为了以后取增量，需要的新 baseline 导数 frame 与 Pi_N(T)、Pi_N(Ts) 支付一次，失败不静默重试。

新 q 的完整一 jets 使用

\[
U(q)=U_{58}
+a_s\,[\Pi T(q)-\Pi T_{58}]
+a\,[\Pi T_s(q)-\Pi T_{s,58}]
+[b(q)-b_{58}]e_z,
\]

而 T(q) 是同一 q 的真实 frame。主体 selected 位置使用

\[
X(q)=X_{58}
+a\,[\Pi T(q)-\Pi T_{58}]
+[c(q)-c_{58}]e_z,
\]

其中 c 的增量为原完整 null/body primitive。这样无需重算已保存 q58 的 X 或假造未存的全网格 X。

主体 unique selected points 与全部后缀 points 先合成一个 union。初始 q58 的真正 selected 二 jets 直接复用；只为缺少的后缀点计算新的二 jets。之后所有新 q 的 union 二 jets 由同一 frame、Pi_N、固定 a 及真实 height 得到，actual G、法面积和 principal curvatures 在同一 union 上形成。

这一增量顺序与原场在实数数学上相同，binary64 加法结合顺序可能不同于 canonical ordinary geometry。源码、binding、summary 明说这一点。新模型合格仅授外部 canonical 全主体预测与原 actual14；不把内部 regrouped eta 或曲率当作原最终 accepted 证据。

本实现不调用 field.geometry 的原 full ordinary oracle，原 full ordinary 调用数为 0；但 baseline、scalar/frame、角原函数、完整一 jets、selected/suffix 二 jets、实际 curvature、value 和 J 全是新增科学工作。原 actual/full 值计数 0 绝不等于新科学工作 0。各组件实做次数、失败、秒数与峰 RSS 均单列。

## 9. 实际曲率与共享解析 J

原曲率构造完整保留。用 A=X_s、T=X_t/a 与三项归一二 jets形成法向 w=A×T、q=|w|；第一形式

\[
G=\begin{pmatrix}E&F\\F&G_{22}\end{pmatrix},
\quad E=A\cdot A,\quad F=A\cdot T,\quad G_{22}=T\cdot T.
\]

不能以 G22=1 替掉实际浮点值。第二形式先用原未单位化法向构成，再按原实现的 qG±K^{-1}N 形成四条 trace/determinant PSD 行。两个 trace 和两个 determinant 分别保留，不能只比较平方谱、合并符号或漏掉 normal area。

独立 principal_curvatures 由原完整实际形式计算，后缀同时检查返回 K 与原 hard58，主体 unique selected 点检查 hard58。所有原 floor 与 tolerance 不变。

解析 J 按 owned radial block 形成原 u、v、Q、height 四族。一个物理族的完整角 kernels 和 virtual position jets 同时供应主体与后缀；不能先各算一份再称共享。u/v 的原 radial-major/mode-minor 次序、body 前四角模式和 1/4 独立尺度都明确展开。

完整六条 height 变化对 X、Xs、Xss 的贡献分别为 primitive、b、b_s；不能只保 Xs 而漏 X 对 signed-height、ball、strip、mirror 的影响。其它 angular jets 对 height 为原准确零。

主体 shape/mirror 导数沿原 selected_physical_derivatives；metric 沿原 spectral_parameter_rows；曲率保留对完整实际 G、法面积、二形式的所有导数。原主体 hard58 与后缀当前 K 分别装配，K 导数只存在于后缀四条 PSD 行，h 只在线性 norm 行。

J 的全列为 170。后缀中其余 106 个控制的零值只来自原函数的真实支持，不通过缩短后端变量列表删除；同一列对主体的非零作用照常保留。

## 10. 有界缓存、重复访问与两个输入上限

缓存只存在于同一科学进程的 RAM，科学数组写盘数为 0，不使用 actions/cache、artifact 或 Release 留存中间数组。

三个缓存层级分开：

- 当前实际 q168 的几何；
- 同一当前 q 的 K 无关物理微分输入；
- 当前 q+K 的完整最终 J。

h 不进入非线性物理 J。相同 q 改变 K 时，物理 kernels/位置微分可以复用，但 PSD 行及其物理列、K 列必须按当前 K 重组；不能复用 K58 的整张最终 J。

只保留当前完整 backend residual，避免归档最多 960 份十多万行值向量。初始与最后完成的数组引用只供真实完成绑定；不为报表重算已淘汰 J 或 geometry。

淘汰后重访问若真的执行新几何或导数，实做成本与重算次数另记，即使 distinct-q 计数不增加，也不说该次科学免费。

本轮上限分别为：

| 项目 | 上限与含义 |
|---|---|
| distinct 新物理点 | 480 个准确实际 q168 字节身份；包括必要 true58 联合初始化 |
| distinct 后端输入 | 960 个 literal backend170 字节身份，任何 callback 首次出现都计数 |
| 单后端 maxiter | 240 |
| 单求解钟 | 1200 秒 |
| 外部科学总钟 | 1800 秒 |

同 q 的新 K/h 会增加 backend 输入，未必增加新物理点；值与 PSD/J 重组仍全计时。当前值命中、几何命中、物理导数命中、最终 q+K J 命中分别记录。计数不混作 solver nfev/njev，也不把某个组件调用冒作原 full ordinary 值。

## 11. 单后端、初始尺度与真实停止

目标固定为 K+1e−6 h，唯一 backend 调用为 scipy.optimize.minimize(method="SLSQP")。无 phase-I 重启、无另一初点、无旧优化回放、无七 alpha 线搜索会话。

初始 x0 是 z168=0、K=58、h=0。初值和第一次解析 J 在此新联合问题中真实取得；每行尺度一次固定为

\[
\max(1,|r_i(x_0)|,\max_j|J_{ij}(x_0)|).
\]

以后不更新尺度。J 仅因这次初始尺度需要或后端真实请求才计算，不为检查、展示或另做数值差分运行 J。

solver 以真实科学总钟和单求解钟检查。库调用不可抢占时，可以实报 overrun；不将超时账截成预算，不伪造成功返回。若钟停或异常发生在 minimize 返回前，没有 OptimizeResult，就保存“无后端原返回”，不能把末 callback 或末已评价点升级成 raw returned。

每次真实后端输入、值请求、J 请求、迭代的顺序、身份、阶段与状态都保存。每次值/J 保留全部组件成本差分；所有组件的 started/completed/failed/seconds 累计完整。逐块细事件只保留最近 **32 条**，并明确被替换的事件数与保留范围；这个有界窗口不称为全部逐块 trace 正文。任何真正失败/停止的 error、具体 phase、当前输入身份与已完成字段独立保存，不依赖窗口是否还留着较早事件。

## 12. 原返回、部分 J 与输出大小

一旦 minimize 真正返回，先保存整个实际 OptimizeResult 原字段和 literal raw170，再作 decode、终门、外部决策或后置时钟检查。保留 status、success、message、nit/nfev/njev、backend elapsed 及所有实际存在的额外字段；内部 QP multipliers 不称严格证书。不补写未返回字段。

有限返回即尽力保存 q168、准确 physical172 与原盒/norm/K/h 真值，包括 failed status 或不合格结果；不能仅保“passed”布尔量而丢原返回。

大几何、J、尺度、partial 数组只保 shape/dtype/hash、实际完成范围、成本和归属，不输出大数组数值，不承诺后继免费恢复。完整 raw170、准确 q168/172、全部 OptimizeResult 字段和逐次紧凑记录例外完整输出。

J 开辟 np.empty 后未写区域不得哈希、输出、填零或当作完成。主体 pool 行不连续，partial 逐块保存其**实际 row_indices 与列范围的身份**；失败只给这些真正已填元素的绑定，不能取最小/最大行的包围区间冒充都已写。已完成整张 J 才给完整矩阵绑定。

报告不导入科学模型重算，不另跑验算。include_arrays 参数仅兼容调用，不改变大数组只给绑定的规则。总 stdout 目标小于 96 MiB；父 scope 自行保留原科学钟、COMPLETE/FINAL 与原接受缓存必要信息。

## 13. 准确资格与外部原接受

只有以下条件全部成立，solution 才把真正返回 q168 交给外部：

1. 存在真正有限 raw170，原 success true 且 status 0。
2. 所有固定尺度模型 residual 满足原 SLSQP ftol；线性原 residual 满足原 LP_ROW_TOLERANCE。
3. 未舍入及真正舍入物理172全部在原准确盒内，K/h 在准确保留范围。
4. 真正 rounded physical norm 准确不超过原 raw h；不修 h。
5. 两完整网格原未平滑 η 均不超过原 b，原 selected 主体 hard 行/实际 PSD/area/direct58 门与全部后缀当前 K 的实际 PSD/area/direct 曲率门成立。

第 5 项使用源码实际得到的同 q 几何。内部 b_int 只通过第 2 项参与求解残差，不另作无容差终门。

通过这些仍只是一个内部联合候选。外部继续以相同 once-rounded q168、原准确 physical172、原 g/b0/c0 与所有原 source 身份作唯一 canonical 全主体预测；其通过后才允许至多一个原 actual coarse/fine pair。原 14 个接受门、原 true58 计数、原全部累计成本及原失败含义不变。任何外部门失败都不能由“solver success”覆盖，也不复跑本轮另找一个未返回点。

## 14. 直接来源

本合同的坐标与公式直接承接以下原公开源码，而不靠旧优化摘要猜测：

- [frame_complete_body_extension168.py](../scripts/frame_complete_body_extension168.py)：完整 168 独立控制、固定参考、body P5/P8 与 physical172。
- [frame_height_null_coordinates.py](../scripts/frame_height_null_coordinates.py)：原准确 H9×5 和 null-height 仿射定义。
- [frame_complete_body_extension168_joint_selected.py](../scripts/frame_complete_body_extension168_joint_selected.py)：原 first-jet 身份、全 168 解析方向、原角径向族。
- [frame_complete_body_extension168_selected_cache.py](../scripts/frame_complete_body_extension168_selected_cache.py)：原 selected-only payload 与 owner/pool/version 绑定。
- [frame_metric_spectral_recovery.py](../scripts/frame_metric_spectral_recovery.py)：原 spectral proposal 与其解析导数。
- [frame_metric_budget_restoration_rows.py](../scripts/frame_metric_budget_restoration_rows.py)：全部原 11 组、真实曲率/area 与原 tolerance 角色。
- [frame_selected_row_radial_jacobian.py](../scripts/frame_selected_row_radial_jacobian.py)、[frame_entry_single_q.py](../scripts/frame_entry_single_q.py)：完整角 kernels、virtual position jets、原 Q 方向及径向展开。
- [frame_curvature_mixed_grid_steps.py](../scripts/frame_curvature_mixed_grid_steps.py)、[frame_curvature_psd.py](../scripts/frame_curvature_psd.py)：原 shape/mirror 导数与完整未平方 PSD。
- [frame_metric_current168_fixed_ring_prefix102.py](../scripts/frame_metric_current168_fixed_ring_prefix102.py)：已付 q_R scalar 输入、原网格与预算身份。
- [frame_metric_current168_full62_whole_suffix.py](../scripts/frame_metric_current168_full62_whole_suffix.py)：已关闭范围的完整原返回语义与原末控制接口；不执行该旧 solver。

父 request 绑定三份新源码、父 wrapper/workflow、设计与本合同的实际 bytes/SHA/blob；所有旧来源哈希保持原值。此文的作用是把一次新的真实联合几何问题及其费用、输入、输出、接受范围说清楚，不生成任何新的科学结果。
