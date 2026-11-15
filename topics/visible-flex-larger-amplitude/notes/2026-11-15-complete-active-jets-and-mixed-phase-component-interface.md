# 同场完整活动片区间 jet、连续球与 mixed 责任接线

2026-11-15，geometry 与 ChatGPT /root（GPT-6 Astra Pro），AI 辅助研究。**状态：source-only；本条没有真实接受场、没有新数值运行，也不构成完整闭面证书。** 交付两个独立入口，旧原生求解、旧 shared-B loader、旧 R241/R24 空间路线及其验收字段都不修改。完整临时输出按 README 第 15 条可重算、不进入 Git 或 Release；只保源码、参数、真实 run、输出 SHA 与紧凑结论。

## 1. 找到的准确生产者边界

现有链确有全场有限表达式，而现有点值 `jets()` 并不是连续区间包围。新入口使用以下边界：

| 对象 | 实际来源 | 新解释规则 |
|---|---|---|
| 完整 prefix | 同一 `load_shared_bundle` 返回的 `saved.quintic.x/nodal`，含实际 R249 选择 | 每组共有节点的全部值、一阶、二阶数值作为精确二进制有理数，定义唯一实 quintic；导数由该多项式求出 |
| 完整 native/collar | 同一 `A.tail.node_coefficients(index)`，三组全部 Cartesian FFT 幅度 | 保每个实际节点的全部 $0\ldots N/2$ 模，包括均值及 Nyquist；精确同节点 Hermite/collar，非 truncated cardinal witness |
| 几何背景 | 同一 `A.shared_background` 的 exact descriptor、全部节点及幂系数 | 使用唯一 $B,B',B''$；原目标度量表不换成 $B'$ |
| 材料角 | 完整 actual core 与已有严格正密度证明 | 直接复合完整 $\Phi(\phi)$，不 FFT 截断复合角，也不数值求逆 |
| 配准 | 原唯一 `saved.registration` | 记录角的准确实 $\cos\beta,\sin\beta$ 与全部平移；不把打印的近似矩阵当精确正交阵 |
| 完整 cut correction | 原 cut 的全部 prefix/node jets 与原 $W,v,b$ | R279 所列整个角函数的 Hermite 校正，包含均值和平移 |
| 两个帽 | 已冻 `geometry_20261115_fixed_cap_rational_balls.py` | 同一 plan/assembly、原图参数、完整上下帽 quadtree，不造帽数据 |

九个原 defining/kernel 源已从实际公开 commit `763f5d841ac86548aca689fd0154ce31875b5dd9` 的小源码对象逐 SHA 核对。它们由新源 `SOURCE_PINS` 明列；旧 loader 内部还执行其原全部来源核。当前新增源码不是那个历史 commit 的内容，最终身份以本次交付 SHA 为准。

这不是把相邻采样位置加一个未经证明的误差半径。新的活动球直接包围已经声明的精确有限场。原 renderer 的浮点多项式系数、求值、FFT 构造和点值报告仍具有自己的数值范围；本入口不声称它们与准确实函数逐 bits 相等。

## 2. 所包围的函数和真实导数

### 2.1 Prefix 与配准

对每个共有径向区间，令 $H_j(s)$ 是从实际全部三阶节点数据定义的唯一 quintic。节点数据只是多项式的定义系数；保存的一阶、二阶节点数据不被当成整个区间上的独立导数函数。用所有场模构成

$$R=\sum_{m=0}^{M}r_m(s)\cos(2m\phi),\quad T=\sum_{m=1}^{M}t_m(s)\sin(2m\phi),\quad Z=\sum_{m=0}^{M}z_m(s)\cos(2m\phi).$$

原 Cartesian 表达为 $(R\cos\phi-T\sin\phi,R\sin\phi+T\cos\phi,Z)$。对 XY 先减原平移 $c$，再右乘原 row-vector 旋转

$$\begin{pmatrix}\cos\beta&-\sin\beta\\\sin\beta&\cos\beta\end{pmatrix}.$$

因此新代码的坐标为 $x'=\cos\beta(x-c_x)+\sin\beta(y-c_y)$、$y'=-\sin\beta(x-c_x)+\cos\beta(y-c_y)$。平移只作用于函数值，随后由同一表达式求导，完整 $z_0$ 始终保留。

场模数 $M$ 与 core 模数独立读实际对象，不硬编码 112，也不把 core 维度强行当作场维度。

### 2.2 全材料角尾、collar 与完整 cut

取规范化物理角 $q\in[0,1]$，$\phi=2\pi q$，并令

$$\theta=\Phi(\phi)=\phi+\sum_{m=1}^{k}\frac{(1-4m^2)c_m}{2m}\sin(2m\phi).$$

已有完整 core 的 $\rho=\Phi'>0$ 证明保证此参数覆盖同一材料圆；新代码保全部实际 core。它不采用一个有限 $\theta$ 带宽替代此复合。

令 $U(r,\theta)$ 为全部实际 FFT 节点定义的 Cartesian Hermite 函数，$Q=\operatorname{diag}(1,1,-1)$。未校正尾是

$$G(r,\theta)=(r\cos\theta,r\sin\theta,B(r))+Q\,U(r,\theta).$$

collar 的六项节点数据为 cuff 端全部 $0/1/2$ jet 为零、inner 端等于原第一个完整 native 节点，宽度使用准确节点差。$B$ 来自同一准确共有节点 descriptor。材料角复合用 $G(r,\Phi(\phi))$，其所有导数由该表达式形成。

原 $v=A.ap<0$、$b=A.app$ 在这里**仅是已声明有限 seam chart 的两个固定系数**。未证明有限 Gauss 算式所给 $a$ 的准确导数等于返回的 `ap`，所以本入口不作该推断、不用 `a/ap/app` 三个标签代替一个函数的导数。它使用 R279 已声明的准确 cut 目标

$$C_0=F(L,\phi),\quad C_1=F_s(L,\phi)/v,\quad C_2=F_{ss}(L,\phi)/v^2-bF_s(L,\phi)/v^3.$$

这些是固定 cut chart $r(L)=r_c,r'(L)=v,r''(L)=b$ 的目标数据。局部可取具有这些 jet 的光滑单调坐标；这里不将该局部坐标误称为原有限标量算法的准确半径函数。

令 $a=r_c-W$，三个权重是从 $a$ 端零 $0/1/2$ jet 到 $r_c$ 端依次选择对应 jet 的准确 Hermite 多项式。完整有限表达为

$$\widetilde G(r,\phi)=G(r,\Phi(\phi))+\sum_{\ell=0}^{2}w_\ell(r)\bigl[C_\ell(\phi)-\partial_r^\ell G(r_c,\Phi(\phi))\bigr].$$

新解释器直接计算此式，因此 cut target 中的平移、完整均值、非线性材料角和两个径向目标均未丢弃。没有把 cut difference 的角样本当 Fourier 系数。

准确 patch 起点是 $F(r_c)-F(W)$，不是重新把二进制浮点减法结果提升为实数。所有实际 prefix 节点、tail 节点、$B$ 节点、cuff、inner 和准确 patch 起点都进入径向分片。闭分片边界重复覆盖，不由一侧采样跳过另一侧。下片仅按原全部 $z\mapsto-z$ 反射定义。

## 3. 六 jet 区间与有理球

`Jet2` 保存 $(f,f_u,f_q,f_{uu},f_{uq},f_{qq})$，不是 factorial-scaled Taylor 系数。乘法和一元复合逐项使用普通链式法则，例如

$$\partial_{uq}(fg)=f_{uq}g+f_ug_q+f_qg_u+fg_{uq},\qquad \partial_{uq}h(f)=h''(f)f_uf_q+h'(f)f_{uq}.$$

每个常数由真实 stored scalar 的 `as_integer_ratio()` 转准确有理数；所有超越函数由 Arb 作用于完整闭区间。$\pi$ 与配准角的三角函数也保区间，不能用固定 float 常数代替准确值。入口运行时才导入 numpy/flint 和原几何 loader；本次只作 AST/小源码静态核，没有导入运行这些计算。

Arb 的 midpoint/radius 构造及运算作外向包围；输出的 `lower().fmpq()` 与 `upper().fmpq()` 是可保全的有理端点。接口依据 [python-flint 的 arb 文档](https://python-flint.readthedocs.io/en/stable/arb.html) 与 [精度/区间语义](https://python-flint.readthedocs.io/en/stable/general.html)，不是通过本地数值实验推测 API。现有本库公开工作流使用 `python-flint==0.9.0`；所需完整 loader 的 numpy/scipy 等依赖仍沿原闭面入口。

设位置三分量区间为 $[l_i,u_i]$。取有理中心 $p_i=(l_i+u_i)/2$，并用冻结 R62 整数平方根上界给

$$\epsilon\ge\sqrt{\sum_i((u_i-l_i)/2)^2}.$$

则整闭 cell 的像位于 $B(p,\epsilon)$。中心无需属于实际像。

单位法向不能由未归一化叉积的球冒充。先以同一 jet 形成 $N=F_u\times F_q$ 和 $\Delta=N\cdot N$。只有区间下界 $\Delta_->0$ 才形成

$$n=N/\sqrt\Delta.$$

对这**整个归一化表达式**逐分量包围，再由上述 midpoint/半对角公式得到有理中心 $n_0$ 与半径 $\eta$，保证每个实际单位法向都在 $B(n_0,\eta)$。$n_0$ 不要求单位；归一化误差已包含在完整区间除法中。若叉积下界不正，保存全部已有 jet 和原因，**不**输出可用法向球、不推断实际退化。不同片的参数叉积可能与统一外法向相差一个全局符号；R281 的平方内积测试对此不变，代码没有因此宣称跨片的外法向规范已付。

若 caller 明确传入原候选 $K>0$，同一完整二阶 jet 额外计算 R279 的 $A_K,B_K$ 区间。仅三个严格下界同时正才记该 cell 曲率严格小于 $K$。此读回不控制球的导出，也不成为原非线性求解或原 cover 的新验收条件；固定帽、全部接缝与其余原曲率责任仍单列。非严格边界或区间未定不称曲率反例。

在这些固定有限表达式上，所有分母只是原非零宽度、cut chart 常数以及已经严格分离零的法向长度。分片细化、工作精度随 depth 增加，使自然区间包围收缩。若整个所需闭分片确有严格浸入余量，足够有限细化能付该正下界；若另有严格 $K$ 余量，R279 检查同理。这里不从 $C^2$ 标签单独声称一个有效余量，也不预填实际 $K$。

## 4. 从实际 family 到完整 mixed 责任

原已发布 `exact_20261114_refined_closed_assembly.py` 的 plan 原文明确：活动片为 $R_\alpha F_0(s,\theta-\alpha)$，固定帽不动；原 render 的相应范围先 shift 活动角，再旋转，最后恢复全部固定标签。shared wrapper 保该 plan 字段不变。新源核这个真实 `phase_rule`、原 z 轴以及上下反射身份，不只靠法向符号不变性猜 family。

由材料角平移满射，活动像为 $R_\alpha A$，固定像仍是实际带标记的 $C$。因此新 R281 输入确是活动球及其法向一起旋转、同场固定帽球保持不动。它不是将旧未标记静态基面的某对中心单独旋转一端。

第二入口要求三个实际输入：新活动 result、已冻两帽 result，以及**同一场**原 shared continuous cover result。它交叉核完整 checkpoint/config/tail/readout/port、闭面文件 SHA、shared B、配准、inlet 选择和均值规范。$\tau$ 只取原 `marker_budget.target_reach` 这个实际二进制值的精确有理解释；不重算直径、不选择新 $\tau$，也不把原 `required_unmarked_reach` 错当 marked mixed 的目标。

完整枚举为全部 $N_A$ 活动闭 cell 与全部 $N_C$ 帽闭 cell 的笛卡尔积，

$$\operatorname{rank}=iN_C+j,\qquad 0\le i<N_A,\quad0\le j<N_C.$$

每个 rank 保存独立结果。输入活动流的 sheet、piece、两个 dyadic 索引及准确闭区间按完整生成规则重新核对；没有使用旧 `worst` 的至多 128 对，也没有使用每坏对至多四个 child 的展示清单。正常全部处理或资源终止均有准确总数。终止时保半开未访问后缀 $[k,N_AN_C)$；不通过简单 `finished` 名称冒充全覆盖。

可用球的非局部对直接复用 R281 原来源和内核：原整相位两端门、距离门、joint 门仍保 OR，必要时两 RP1 图闭有理区间逐 Sturm 细分，完整返回原证据。任何未决结果保原义。

### 4.1 不能交给严格相位门的 cuff 责任

活动 collar 的闭 cell 含 cuff，且同侧帽闭 box 触及原 cuff 圆时，完整相位 product 含某个共同材料点的零弦。R281 的严格距离/非 double-normal 充分门不能支付这个整个 product；该事实不代表曲面不嵌入。

代码按准确 box 的半径平方最小/最大值识别这类责任，将其完整 rank 留在 ledger，并标成 `original_local_chart_responsibility`，不记通过，也不悄悄丢掉。跨 cuff 局部图/真实短路径及其曲率余量仍属于 R241/R248 已有责任。现旧公开 cover 只保聚合计数和截短失败例，并未给出可由此新全cell布局直接导入的全部逐对局部支付清单；本入口不伪造这样的生产者。

这就是当前仍有的最小实质接口缺口：若要把新 mixed 组件升为完整 direct marked 路线，需要旧 local owner 对相应完整 product 真实给出可用局部图/路径覆盖，或沿原已经完整支付的 unmarked+R24 路线传递。**旧路线完全保留，不因本组件未付局部责任而被撤销。** 此外 active-active 两端共同旋转可约去相位、fixed-fixed 不动，但仍需它们完整原空间责任；本组件不替它们宣称成功。

新结果分别报告完整笛卡尔积、R281 已付、缺活动球、相位未决、明确局部责任及未访问 suffix。即使所有非局部对通过，也不把 `numerical_cover_budget_passed`、正则性、同 $g$、原曲率预算、完整目标像 held 或 $\delta_E$ 更名为已证明。没有新的求解 acceptance gate。

## 5. CLI 与真实输入

活动片入口：

```sh
python computations/geometry_20261115_shared_active_interval_balls.py \
  --directory ACTUAL_SHARED_RENDER --basename surface \
  --source-directory ACTUAL_ORIGINAL_CLOSED_RENDER --source-basename surface \
  --descriptor ACTUAL_SHARED_BACKGROUND_DESCRIPTOR \
  --checkpoint ACTUAL_ACCEPTED_COMPLETE_PREFIX \
  --port ORIGINAL_PORT --config ORIGINAL_NATIVE_CONFIG \
  --tail-response ACTUAL_FINAL_NONLINEAR_AUDITED_RESPONSE \
  --complete ACTUAL_COMPLETE_RADIAL_READOUT --source-topic ORIGINAL_RESTORED_SOURCE \
  --depth REQUESTED_DEPTH --precision-bits 192 --sqrt-bits 128 \
  --max-cells 1000000 --budget-seconds 3600 \
  --out "$RUNNER_TEMP/active-continuous-balls"
```

`--curvature-upper` 为可选的原候选有理值；没有默认科学 $K$。`--code-directory` 默认入口所在计算源目录。原 loader 自身会验证实际接受、完整 tail response/J/audit、当前完整 source/H/mean/SE2、原 closed 与新 shared 数据之间的身份；这里没有给当前未接受解造替身。loader 原本会按其定义重建 prefix 二阶节点和读 FFT 节点，所有这些操作也只能在 Actions；本次并未执行。其全部有限源数据来自当前 recipe 的临时输出，不要求把原件重新保存 main。

活动输出 `result.json` 绑定 `input-binding.json`、`exact-field-expression.json` 和 `active-cells.jsonl.gz`。后者每行保完整六 vector intervals、叉积与归一化区间、球和未决原因。每个实际 FFT 节点的全系数 SHA/shape/原 readout SHA 保在 expression；全部共有 prefix 节点哈希、全部 radial pieces、core、SE2 与 cut chart 也完整保全。深度 $d$ 的确定计划数为 $2P4^d$，其中 $P$ 是实际全部径向分片数。资源预算不删片、不变模数、不放松任何原门。

mixed 入口：

```sh
python computations/geometry_20261115_complete_mixed_phase_component.py \
  --active-result "$RUNNER_TEMP/active-continuous-balls/result.json" \
  --active-result-sha256 ACTUAL_ACTIVE_RESULT_SHA \
  --fixed-caps ACTUAL_FIXED_CAP_BALLS --fixed-caps-sha256 ACTUAL_CAP_RESULT_SHA \
  --original-cover ACTUAL_SHARED_CONTINUOUS_COVER \
  --original-cover-sha256 ACTUAL_ORIGINAL_COVER_SHA \
  --max-pairs 1000000 --budget-seconds 3600 \
  --sqrt-bits 128 --phase-max-depth 16 --phase-max-cells 131070 \
  --out "$RUNNER_TEMP/complete-mixed-component"
```

future SHA 均来自实际输出，不预编。`complete-mixed-pairs.jsonl.gz` 保存全部已处理 rank 的原 R281 完整记录或未决责任；result 保完整未处理后缀。大型 payload 不进入发布目录。紧凑 stdout 仅计数/状态/hash，不保存 raw 在 Git/Release。

## 6. 本次实际验证范围与下一步

本次只完成原小源码/已发布 source identity 读取、Python AST、全字段与数学表达式的静态核。没有造 accepted 场、没有运行 Arb/FFT/RHS、没有新增合成 fixture，也没有 Actions 调度或 Git mutation。两入口是参数化实现，当前不存在可冒称执行成功的场结果。

最小真正执行应等待原流程自然产生一个真实完整接受场及其现有 closed/shared 临时对象，然后沿上面原 loader 直接产连续球和完整 mixed 责任；这不是额外的前置机器验收门。该接线使原来“需正确连续球”的接口获得具体同场生产者，同时准确保留尚未支付的局部接缝/完整全局责任。

依赖说明及已有证明分别见 [R248](../results/R248-finite-C2-phase-family-and-global-reductions.md)、[R249](../results/R249-shared-node-inlet-parity-normal-form.md)、[R279](../results/R279-finite-field-direct-continuous-curvature-certificate.md)、[R281](../results/R281-exact-rational-phase-disjunction-and-finite-cover.md) 与 [固定帽球接口](2026-11-15-R281-actual-closed-cover-boundary-and-fixed-cap-balls.md)。

## 7. 本次公开源码身份

| 完整入口 | 字节 | SHA256 |
|---|---:|---|
| `geometry_20261115_shared_active_interval_balls.py` | 33310 | `675ab8dffaaa86dd7a760dba8502d03d83f04fed15e88224c13da35a4151514b` |
| `geometry_20261115_complete_mixed_phase_component.py` | 22006 | `dbdedb450ca2280f37802258377e5fd8728b9f20ce2545f22ec141b6965bc3ed` |

root已逐段读完整两源、此接口及相应原生产者，核六jet乘积/链式法则、全部cut三权、法向完整归一化、两反射片、原旋转family和完整rank未访问后缀。Arb外向区间及精确端点API已对官方文档核对；这里没有把静态检查当实际执行。可重算的本地静态receipt不提交。没有实际run或场输出SHA可报告；待原流程自然产生真实完整接受场后，直接执行此参数化入口，继续支付明确保留的local与全局责任。
