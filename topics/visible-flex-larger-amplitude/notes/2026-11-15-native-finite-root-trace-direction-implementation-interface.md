# 原113有限 root 轨迹的完整方向变分：独立实现与实际输入接口

类型：源码、数学接口与尚未执行的实验设计。AI 协作：ChatGPT，2026-11-15 UTC。

## 1. 本次交付与当前状态

本次实现 R283 已证明的固定轨迹实表达式变分。它接收一个**真实现场的完整113格式 packet**，在显式选定的原或 refined root policy、显式选定的当前点，对 packet 中完整577节点方向做一次方向计算。所有576段、226维局部状态、两条均值、112条cut、129024条stage及112条far行都在计算范围内。

代码已完成源码恒等核、Python AST、Node语法和C++ `-fsyntax-only`。没有导入或执行任何科学模块，没有运行packet、root、RHS、RK、矩阵动作、FD或native求解。因此本稿没有实际变分数值、通过率、时间成绩或新成功锚。

原113两源、原native循环、118及119均不修改。本交付没有workflow、request编号或派发。主控可以在已有真实当前点可供给时，独立安排一次公开Actions诊断；它不作为现有任务的等待条件或新接受门。

| 新文件 | 字节 | SHA256 |
|---|---:|---|
| `geometry_20261115_native_trace_variation128.cpp` | 34622 | `8c40b4c7ed214a16afd06cd0157bf861822cb217a72bd0117bbed7f2c954204d` |
| `geometry_20261115_native_trace_variation128.py` | 21410 | `8229212bb6804db7eee99ea661a490d3cced756e8a98471c09e22ad74cdb8b76` |
| `geometry_20261115_native_trace_variation128_bridge.mjs` | 15077 | `61e21ded03f1569c7d05742d3059553d1f3830c52a62643fd64883bc821c83a7` |

实验组件本身的五源闭包为上述三源加以下两份原文件；实际调用它的native worker还有自己的原完整来源闭包，不能把五源说成构造物理场所需的全部来源。

| 原文件，保持逐字不变 | SHA256 |
|---|---|
| `geometry_20261115_native_primal128.cpp` | `1b59cd1059c147f3fedf28a663fed25049c80a42d782838506aba4a7b7df591d` |
| `geometry_20261115_native_primal128_bridge.mjs` | `3655c81a5771deaa26a0d22b8fc4bbbead0302cd06983ddd4f5d12eded44ebe8` |

理论依据为 [R283](../results/R283-finite-root-trace-differentiation-with-literal-tables.md)，并保留两份既有范围说明：[有限root轨迹设计](2026-11-15-native113-finite-root-trace-variation-design.md)、[128状态与最终审计缺口](2026-11-15-native128-state-variational-and-final-audit-gaps.md)。

## 2. 微分对象：实际有限程序的固定轨迹实表达式

设113格式packet中的各个binary64字面值分别代表一个固定实数。cosine、sine、gram三表独立；`r, dr, w, w2, E`分别固定；没有用三角恒等式重建gram，也没有用`w*w`或`1+w2`重建输入字段。

一次实际RHS中，形状输入是 $y=(Q,\Pi)$。原源码以

$$
t_0=0,\qquad t_{j+1}=\gamma\Pi_j,\qquad
F(e,y)=e+q(t(y)+e,Q)
$$

定义残差，并以另一个实际函数

$$
C(e,y)=\texttt{root\_matrix}(\texttt{root\_evaluate}(e,y).\mathrm{rows})
$$

形成Newton矩阵。本实现没有把 $C$ 定义成 $F_e$，也没有声称实际输入上已经测得二者的差异。

原root从 $e_0=0$ 出发。每次实际选择的回溯因子 $alpha_i=2^{-k_i}$ 在固定轨迹模型中是常数。仅在原比较接受该因子后，传播

$$
\dot F_i=D F(e_i,y)[\dot e_i,v],\qquad
\dot C_i=D C(e_i,y)[\dot e_i,v],\qquad
\dot e_{i+1}=\dot e_i-\alpha_i\dot s_i.
$$

最终返回 $L=t+e_n$ 和原角向rows的方向。第0次残差检查就返回时，$n=0$，严格使用 $\dot L=\dot t$；不会补一次隐式根求解。正常返回与原fallback都按其实际返回位置处理。成功返回的更新数属于0至29；原30轮耗尽不被改称成功。

实现中的方向数值仍有binary128舍入。它是R283固定轨迹实表达式的数值链式法则计算，**不是IEEE离散舍入映射的导数**，也不是带认证误差界的精确导数。没有证明实际浮点选择的轨迹在某邻域内稳定，或证明原实算术程序会选同一轨迹。被拒绝的候选只决定轨迹、保留原记录，不额外传播其输出方向。

## 3. C++实现：原primal与显式变分的分工

### 3.1 原113源直接包含

新C++在同一翻译单元中包含原113 CPP，仅把它的`main`符号重命名。原`Problem`解析器、`root_evaluate`、`root_matrix`、二进制格式、字面常量、域判断、平方根和格式化函数直接复用。旧main不执行。

实际primal root控制流保留原目标、原30轮、原20档、严格残差比较、正常停止和fallback。原Cholesky及两次代回的primal函数体逐字复制，只扩展返回对象以暂存实际factor、前代回向量和最终step；没有再做一次primal分解来猜其值。原RHS在取得root后的完整primal函数体同样逐字保留，只把已经计算的flux一起返回。

原RK的 `state + h*a/2`、`state + h*b/2`、`state + h*c` 和 `state + h*(a+2*b+2*c+d)/6` 的值表达式、次序和完整226行保留。几何取packet中的g0/g1/g1/g2，没有重新调用profile求值。

### 3.2 F与C分别求方向

`F_direction`按原momentum/角和、原有理式、原cosine投影、最后加e的顺序做前向一阶传播。每个除法直接使用商法则；没有引入例如 $\dot u/u$ 这类原分子为零时无定义的表达式。

`C_direction`从实际root rows的值与方向出发，按原`am, dm, value`和**独立gram表**累加，再用原lower-triangle分支装配。单位阵部分的方向为零。它不使用一个另外推导的理想隐式Jacobian。

双数的值分量会重算这些同序表达式；原函数的返回值仍是权威primal。代码逐字比较所有原F残差词、每个角点10个rows字段、C的全部上下三角装配词和RHS/flux词。发生不一致时，独立诊断报告`primal-shadow-word-mismatch`及部分产物身份，不能继续声称沿同一primal程序。该源码一致性错误只属于独立诊断；不改变原native接受门。

这些shadow运算是新的科学算术，并不是“零计算字节读者”。`F_direction_calls`、`C_direction_calls`与原root angular evaluation计数分开，不能把它们隐去，也不能把shadow重算说成又调用了原root选支。

### 3.3 逐Cholesky与两次代回

令实际下三角factor为 $R$，实际前代回向量为z，实际返回step为s。实现沿原索引次序传播：

$$
\begin{aligned}
\dot v_{ij}&=\dot C_{ij}-\sum_{k<j}(\dot R_{ik}R_{jk}+R_{ik}\dot R_{jk}),\\
\dot R_{ii}&=\dot v_{ii}/(2R_{ii}),\\
\dot R_{ij}&=(\dot v_{ij}-R_{ij}\dot R_{jj})/R_{jj},\quad i>j,\\
\dot z_i&=\bigl(\dot F_i-\sum_{k<i}(\dot R_{ik}z_k+R_{ik}\dot z_k)-z_i\dot R_{ii}\bigr)/R_{ii},\\
\dot s_i&=\bigl(\dot z_i-\sum_{k>i}(\dot R_{ki}s_k+R_{ki}\dot s_k)-s_i\dot R_{ii}\bigr)/R_{ii}.
\end{aligned}
$$

没有用一次 $C^{-1}(\dot F-\dot C s)$ 浮点解替代这些循环。该恒等式在实算术中成立，但两种浮点算法并不逐字相同。因子只在当前root更新的内存中保留，用完释放；这里没有声称从原113导出了已有factor文件。

### 3.4 完整RHS、RK与shooting

RHS继续使用原split flux、完整shape和两条均值。局部接口`Pair`有两个长度226的向量；没有把两条均值混回shape root。global stage以完整实际node n+1的224形状词为输入，其两均值初值与初始方向均为0。每个原RK步骤都传播完整226行。

在stage n末，只有Pi的值与方向除以该段原port ratio；均值不缩。原full shooting及其方向是

$$
\begin{aligned}
r_\mathrm{cut}&=Q_0-t_\mathrm{cut},&a_\mathrm{cut}&=v_{Q_0},\\
r_n&=\Phi_n(x_{n+1})-x_n,&a_n&=T_n v_{n+1}-v_n,\\
r_\mathrm{far}&=\Pi_{576}-G_\mathrm{far}Q_{576},&a_\mathrm{far}&=v_{\Pi_{576}}-G_\mathrm{far}v_{Q_{576}}.
\end{aligned}
$$

**入端是node n+1，出端是node n。** cut和far不投影、清零或删行。本次是固定target/几何/far graph的状态方向；没有同时微分physical H或改变graph。

行序为112 cut、576×224 stage、112 far，共129248。cut用原sigma0；stage n用原sigma n；far用原sigma576。所有sigma仍由packet逐词提供。完整raw residual/action先形成，之后才作规范化读数，没有先把矩阵系数除sigma舍入成另一个目标。

## 4. 真正输入接口与尚不存在的输入

### 4.1 新packet桥

原113 bridge在结束时会删除它拥有的packet。因此不能假称实际113已经留下一个可下载的packet，也不能从原摘要还原未保存数组。新桥的private `writePacket`函数体与原3655版本逐字相同，但它是在**新的实际调用现场**创建packet，并给出自己的来源身份。没有声称新packet与已删除的旧113 packet逐字相同。

公开函数为：

```javascript
writeNativeTraceVariationPacket(
  dn, args, delta, splitIntegrationInterval, identity, outputDirectory
)
```

调用者必须提供原现场的`dn`、`args.states/target/scales/M/K/depth/it`、完整577×224 `Float64Array`方向、原cusp拆分函数，以及实际来源字典。这个模块不创建native worker、不造初猜、不调用solve/root/RHS/J，也不决定方向。

必须具备的`identity`键沿已有113调用现场：

| 键 | 必须来自实际调用 |
|---|---|
| `source_sha256`, `hook_sha256` | 调用者完整来源 |
| `native_call` | 正整数 |
| `nonlinear_iteration` | 与`args.it`相同的非负整数 |
| `original_cuspAwareFlow` | 原现场确认true |
| `fresh_snapshot_result_sha256` | 本次已实际形成的快照SHA |
| `complete_current_array_sha256` | 完整当前快照的原bytes身份 |
| `complete_current_delta_sha256` | 实际全部577方向行SHA |

四个直接交叉键是`base-states`、`cut-target`、`original-scales`、`original-far-graph`；方向另核完整delta。调用前后重新hash同一原数组，确认独立实验没有改写它们。其他原snapshot身份仍完整保留在`actual_call_identity`。

新binding schema为`native-finite-root-trace-packet-binding-v1`，包含实际packet文件/bytes/SHA、三张独立表SHA、每段schedule汇总SHA、原两源SHA、新writerSHA和原当前点身份。packet仍为`QPR11301`格式，不发明压缩state或截断方向。

### 4.2 packet中的精度边界

此入口的base、delta、几何、角表、target、sigma、far仍是**真实binary64词的准确提升**。选择`base`时使用提升后的base；选择`trial:k`时在binary128内形成

$$
\bar x=\operatorname{fl}_{128}(x_\mathrm{base}+2^{-k}\delta),\quad k=0,\ldots,9.
$$

随后计算的是该已形成当前点处、沿完整delta的固定trace数值方向。它不对`alpha==0`调度分支或状态形成的舍入映射求导，也不声称这是尚未实现的高精度native状态所有者。未来若原生迭代持有binary128节点，则须另做保留128词的真实输入格式；不能把那些节点先转回Float64再冒原128状态。

## 5. 可执行CLI及编译

三新源与两原源放在同一`computations`目录。launcher只有stdlib依赖；C++使用GNU `g++`、libquadmath、OpenMP；Node桥仅用builtin模块。编译命令沿113：

```bash
g++ -O3 -std=gnu++17 -fopenmp -fno-fast-math \
  -ffp-contract=off -frounding-math \
  geometry_20261115_native_trace_variation128.cpp -lquadmath \
  -o "$RUNNER_TEMP/owned-build/trace-variation-evaluator"
```

实际编译由launcher在自己新建的临时build目录完成；它核原CPP SHA，记录新CPP/launcher/bridge/原bridge SHA、编译命令、编译日志SHA、可执行文件SHA，C++另记真实`__VERSION__`。要求原113的16字节、113有效位binary128与8字节、53有效位double；要求little endian和FE_TONEAREST。不能把long double替代为“128”。

CLI：

```bash
python computations/geometry_20261115_native_trace_variation128.py \
  --packet "$ACTUAL_PACKET" \
  --packet-binding "$ACTUAL_PACKET_BINDING" \
  --expected-packet-sha256 "$ACTUAL_PACKET_SHA256" \
  --expected-binding-sha256 "$ACTUAL_BINDING_SHA256" \
  --expected-cpp-sha256 8c40b4c7ed214a16afd06cd0157bf861822cb217a72bd0117bbed7f2c954204d \
  --policy "$EXPLICIT_ROOT_POLICY" \
  --state-point "$EXPLICIT_STATE_POINT" \
  --seconds "$EXPLICIT_SECONDS" --threads "$EXPLICIT_THREADS" \
  --out "$RUNNER_TEMP/new-trace-result"
```

所有`ACTUAL_...`均需先由真实新packet产生，示例不是待填伪run/伪结果。`policy`必须显式为`original`或`refined`：前者使用packet中原binary64 `8e-14/5e-12`的提升；后者使用原113同一refined定义`strtoflt128("1e-28")/strtoflt128("5e-27")`。每次CLI只选一个policy与一个点，不自动扫描或再做FD。`state-point`必须显式为`base`或`trial:0`至`trial:9`。线程1至4，科学墙钟预算60至14400秒。

这是独立计算，不默认替换原113的任何参数。未在本稿选定一个新实际run、policy、点或预算。

可选的同步observer封装为：

```javascript
runNativeTraceVariation128(
  dn, args, delta, splitIntegrationInterval, identity,
  {seconds, threads, policy, state_point, launcher_sha256, cpp_sha256, python},
  emit
)
```

它只创建自己拥有的RUNNER_TEMP子目录，将新CLI子进程stdout/stderr引到原worker的日志流；不写worker JSON协议stdout。调用者若把此独立observer装入native流程，仍应像113一样把它的失败单独记录并继续返回原方向，不把实验失败当native新拒绝条件。当前没有任何冻结hook导入或调用新函数。

## 6. 输出、完整性与错误保全

C++完整或部分报告schema为`native-finite-root-trace-direction-binary128-v1`；launcher摘要为`native-finite-root-trace-direction-launch-summary-v1`。主要原子输出：

| 原临时文件 | 完整形状 | 解释 |
|---|---|---|
| `current-states.f128` |577×224| 本次实际形成的128当前点 |
| `input-direction.f128` |577×224| 原完整delta的逐词提升 |
| `primal-residual.f128` |129248×1| 原行序的新128primal残差 |
| `directional-residual.f128` |129248×1| 所有cut/stage/far方向 |
| `stage-full-output.f128` |576×226| port前完整段输出，含两均值 |
| `stage-full-direction.f128` |576×226| 对应完整方向，含两均值 |

每个实际启动的stage另有`root-trace-stage-n.jsonl`。每条root记录含stage/RK步/field地址、每个实际迭代残差与scale、所有实际回溯的返回或域拒绝、被选alpha索引、正常/fallback/失败、接受更新数、原primal是否已选择返回以及方向是否完整返回。没有预定实际迭代数、没有裁掉大于某序号的root或高模。

`root_statistics`是原primal计数；`variation_statistics`单列F/C/factor/两次代回计数、n=0返回、0..29成功更新数直方图、0..19接受backtrack直方图、所有shadow字比较。未有已返回root的minD/S/A写null，不把初始哨兵当作观测值。

只有全部576stage及规范化读回完成，`complete`才为true。若全部行已形成、但规范化scalar溢出，保全部数组并单独写`all_stage_rows_computed=true`与`scalar_readback_error`。未完成stage的数组保NaN占位，必须连同`rows_completed`/stage错误解释；不能以数组文件存在冒全行有效。

成功完整报告还提供：原sigma下primal范数、方向范数、一次`r+a`的单位步affine范数；每个的实际最坏行；历史watch行2539/2536/2762/2128的原residual/action/sigma及规范化字面读数；两均值总和与方向。**`r+a`只是固定轨迹模型读出，不是实际非线性trial，也不决定接受。** 此处所有新乘除/范数都仅由Actions中的C++产生，launcher不重算。

正常退出0表示这一个独立方向计算完整；显式资源预算导致部分结果退出3；其他独立实现或原分支错误退出2。预算耗尽、原root失域、无fallback回溯失败、30轮耗尽、SPD失败、shadow不一致和非有限方向分别保原错误，不合并成“数学不存在”或“native失败”。若外部超时导致最后一条JSONL不完整，launcher仍逐件hash现有临时文件，明确没有完成语义解析。

## 7. Rule15生命周期与读回

所有新执行只允许`GITHUB_ACTIONS=true`且repo为`Rogerhu12/math-research-public`。新out必须位于实际RUNNER_TEMP下且尚不存在。launcher只删除自己新建的work/build目录；不会删除调用者提供的packet。

新桥的同步封装则拥有更外一层临时目录。它等消费者结束、核返回binding及原数组未变后，删除自己拥有的packet、结果和日志副本。没有upload-artifact、Release上传、Git写或token读取。原native输入数组与方向保留在调用进程中，不被删除或重写。

清除前，launcher形成每个完整或部分输出的路径、bytes、SHA与完整raw形状，保临时manifest和完整报告SHA；stdout以`NATIVE_TRACE_VARIATION`标记输出紧凑原scalar与身份，最大90000 bytes。若全部576段的纯metadata过长，只从stdout去掉段metadata表，保完整summary bytes/SHA及原汇总；不能补零或改称完整数据已公开保存。再次超限时给明确fallback及SHA，原source可重算。所有删除都只影响可重算临时输出，不销毁输入来源或宣称上传成功。

短报告属于独立新科学结果；packet byte-map、输出SHA及JSON结构核属于随后字节处理，二者标签分开。

## 8. 资源结构与剩余风险

方向数固定为1。每个实际使用的F/C角和的结构成本为 $O(NM)$；每个接受root更新的原分解与因子方向成本为 $O(113^3)$，两次代回各 $O(113^2)$。每段每原RK步有4次root；完整次数由实际packet schedule决定，不捏造运行次数。原回溯只执行其原primal候选，方向传播不为每个被拒候选再生成一套矩阵。

内存按一个当前root的实际factor、前代回/step及各方向、角rows工作；不保存一个224列局部J，更不复制576个full J或1372系统。packet的三张Q提升表为 $N(4M+2)$ 个binary128数；每线程还有原和方向角rows、几份113×113工作阵及226向量。实际峰内存、文件量和耗时尚未测量，不能把source-only分析冒容量实测。完整JSONL trace的长度由实际迭代/回溯决定；它逐stage写临时文件，读回hash后删除。

仍未支付的责任必须逐项保留：

1. binary128方向计算的误差界、真实分支邻域稳定性、有限literal模型与连续root/原数学tail的等同；
2. 全部224输入列的每段矩阵、其完整全局求解、binary128状态持有与真正高精度native十试探；
3. physical H的target/geometry/graph依赖、完整112外部敏感度、cut jets、endpoint J及fresh audit；
4. 连续同一stored g的interval包围、完整fullDN及原闭场/metric/final证明。

更换为一个方向接口不能把这些责任付掉。若原成功轨迹导数数值可用，下一步可显式扩展成复用primal trace的多方向/全列实现；那是后续实现选择，尚未包含在本次源或结果中。

`source-only-check.json`与`check_source_only.py`是临时静态回执/重现脚本，36项包括原packet writer函数体、原SPD primal全函数体、原RHS-after-root全函数体、F/C关键表达式、RK值式、完整行方向及三语言语法。它们没有执行任何科学函数，不是新的数学接受门；可由发布源码重得。
