# 同原 no-J primal 的新变分推进：完整条件论证与第 71 轮接口

作者：geometry；日期：2026-11-14。分类：有限算法的条件同一性证明、独立实现及公开 Actions 试验接口。

当前状态：源码已写完并仅通过 AST/Node 语法检查；没有本地计算。本次只证明指定冻结源码下的表示/调用关系，不宣布新候选已实际返回、收敛或通过最终审计。实际第 69 轮已确认相同状态的原 no-J 与旧 with-J 有不同返回值，见 [69 实际结论](2026-11-14-actual69-same-state-noJ-withJ-discrepancy.md)。

## 1. 精确对象

令 $M=112$、$K=2M=224$、$d=K+2=226$。原每个 shooting cell 的输入是完整 $d$ 维 typed state：前 $K$ 项来自该 cell 的 inner node，两项 mean 初值为原 `+0`。它沿原 profile 顺序和原普通 step 顺序推进；两项 mean 在各 profile/step 间继续，不重置。只有 cell 出口的 Pi 行除以原 `portRatio`；两个 mean 状态都不除。

原 core 的 no-J 分支调用 `engine.rk4(state,profile,k/steps,1/steps)`。实际 engine 是 `78718-tail-fourier-root-split-engine.mjs` 构造的 Fourier-root/split-RHS engine，按配置可再有原 `withCuspAwareRK` 包装。

新模块只提供替代 `flowStateWithJacobian`。`base.root`、`base.rhs`、`base.rk4` 是原函数对象，调用后仍以原引用返回。它不修改原 no-J 验收函数、g/H、目标、sigma、graphs/gains、far 边界、guard、容差、回溯 alpha 或最终审计。它产生**新的** Jacobian，不能声称是旧 saved J 的逐字再现。

冻结依赖：

| 源 | SHA-256 |
| --- | --- |
| 原 Fourier root momentum | `cbf753894f32e3460e646725757cbaed1f227b166f9693dda54829ee46ecfc88` |
| 原 Fourier root split engine | `a47df10fcde701c6c657b496d003dbe837eecfca4a51abaf40d6f7c387049372` |
| 原 product Jacobian | `205b28dbde3b43392ef8ad0a915e9f4265264f4663b5bc2a0ea34421516cfd25` |
| 原 local cusp helper | `b12f3626413262daf1eef6be87bf7ad27813295bd2b84e166dcb9ed6c612736f` |

原 `product-J` 与 cusp helper 从已恢复的同一公开 78-source 中导入，不复制成另一套数学公式。

## 2. ordinary 与 cusp 调度完全列明

设原普通 step 数为整数 $q>0$。对每一个 profile，原 core 的每次调用使用 JavaScript 实际运算

```javascript
x = k / q;
h = 1 / q;
```

候选也逐次执行这两个表达式，不写成 `k*(1/q)`，不从前一个 x 累加 h，不预建整体 `integrationGrid`。

若 `cuspAwareFlow!==true`，原 step 就是 `(x,h)`，候选同样直接使用它。

若启用 cusp，候选调用**原** `splitIntegrationInterval(x,x+h,profile.integrationBreakpoints)`。因此：

1. 原严格内点比较、排序、可能的方向反转都由同一个函数执行。
2. 若该原局部 grid 长度为 2，使用原 x/h；绝不将 h 改为 `grid[1]-grid[0]`。
3. 否则逐原局部 grid 相邻项调用，使用原 `grid[j]` 和 `grid[j+1]-grid[j]`。
4. 不全局去重，不删原可能重复的 cusp 点，不擅自删零长子步，不把某普通 interval 的 `x+h` 改成下一 interval 的 `(k+1)/q`。
5. profile 边界按原列表顺序重启 k，而完整 226 状态继续；不把两个 mean 清零。

这覆盖有/无 cusp、cusp 在普通端点附近、重复点及所有 profile 边界。证明不借用“两个网格在实数上相同”来忽略实际 double 运算。当前真实第 61 轮 profile 均由原工厂固定；没有新增或移动其任何零点。

## 3. 单步 primal 的逐运算关系

对一个实际局部 `(profile,x,h)`，记原 RHS 返回向量为 $f(y,x)$。这里先按同一原 `root` 求出 rt，再以 rt 为 `knownRoot` 调同一原 split RHS。这恰是原 no-J wrapper 的两次调用次序，不增加一次根求解。

候选完整执行原 state 语句的同一括号：

```javascript
const a = field(state, p, x), t = new Float64Array(size);
for (let j=0; j<size; j++) t[j] = state[j] + h*a.ds[j]/2;
const b = field(t, p, x+h/2);
for (let j=0; j<size; j++) t[j] = state[j] + h*b.ds[j]/2;
const c = field(t, p, x+h/2);
for (let j=0; j<size; j++) t[j] = state[j] + h*c.ds[j];
const d = field(t, p, x+h);
const nextState = Float64Array.from(state,
  (v,j) => v + h*(a.ds[j]+2*b.ds[j]+2*c.ds[j]+d.ds[j])/6);
```

`field` 的 ds 就是原 RHS 本次返回的对象，不是重新计算或平均后的副本。它在 root 和 RHS 都返回之后才保存额外副本。原 reusable `t` 的分配及三次写入顺序保持，因此 `h*a/2` 没有改成 `(h/2)*a`。所有 $d$ 项均写入，均值和背景均值也保留原次序。

### 条件命题 A：成功返回的 primal bytes 相同

假设：使用上述指定原 backend、相同 options/profile/初始有限 raw state、同一 JavaScript Number/Float64Array 运行时；原 root/RHS/几何函数只具有其已读源码中的行为；新切向和记录阶段没有抛出使调用提前终止的异常。则候选 `flowStateWithJacobian(...).state` 的完整 $d$ 个 double words 与按原 core no-J 分支循环调用原 `rk4` 的最终 words 相同。

**证明。** 先按 §2 得到完全相同的局部调用序列。对第一个 field，两路径以相同数值和 x 调同一个 root，再用其结果调同一个 RHS。原 RHS 中传入 knownRoot 的短路只避免了同一次 root 的重复调用，并不改任何 RHS 算式；所以 ds 相同。额外复制不写回原对象。两条路径逐 j 执行相同的乘/除/加语句，故 reusable t 的全部 words 相同。依次对 b/c/d 重复，最终 `Float64Array.from` 的每个 callback 同输入同括号，得到相同 `nextState`。候选切向阶段不改这一数组；于是可对下一子步、下一普通 interval 和下一 profile 归纳。完整 226 words 相同即推出原 Pi 出口除法结果相同，以及原 `meanHeight=state[K]+state[K+1]` 的同一次加法结果相同。证毕。

该命题是指定实现的有限算术同一性，不是“理想 RK4 误差趋零”的替代论证。它也不声称候选一定能成功形成 J：原 product-J 的线性代数、内存/记录或程序异常仍可让新 with-J 提前失败，实际试验必须保留此事实。

## 4. root、几何 memoization 和别名为何不污染 primal

已读原源码支持以下有限范围：

- 每次 root 新建当前 Q/target/L，`evaluateL` 新建 B/rows；root 迭代把 L 换为新 trial，不回写先前捕获的 L。
- 原 geometry 返回 `{...g,w,w2,E:1+w2}`；product-J 真正读取的 `r/drdx/w/w2/E` 是当前对象中的 Number 值。
- 原 rows 的 `P/Pt/L/K/U/S/D/A/sd/quad` 是标量；原 product-J 只读这些值和 B。其 `solveMany` 新建工作 L/X，不原地修改输入 B。
- 原 split RHS 新建 d/nonlinearFlux；statistics 只累计 evaluations/root residual/fallback 诊断，不进入 RHS 的算式或根策略。
- 原 profile memoization 的命中/淘汰影响分配，不改变原缓存公式。本命题只针对其实际被 root/RHS 使用的数值，不泛称任意 profile 的全部 nested metadata 都不可变。

候选每个 field 在原 root/RHS 返回后复制：完整 field state、derivative、L、g 中实际需要的五标量、B、rows 标量、minA/minD/err/scale。复制发生在原 reusable t 再次写入前，故不会把 b 的输入事后误读成 c/d 的输入。

完整 primal 单步先完成，随后才形成四个 local A。此阶段导入原 product-J factory，但给它的是 feed-only `root`/`rhs`：这两个函数只返回指定捕获对象和 derivative，并检查 state/profile/x/root 身份。它们不调用真实 root/RHS/profile，不访问原几何缓存，不改 statistics，不回写捕获数组。原 product-J 的两次读取计数保留为来源契约。

切向矩阵完全独立于 primal state。可选 `onStep` 观察器只收到完整副本；不交出原 profile、root/cache 对象或运行中的 state/T，因此观察器不能通过普通返回对象修改后续推进。任意外部恶意全局修改或运行时故障不属于命题前提，也没有伪装成已排除的数学风险。

## 5. 新切向的完整数学式及其准确含义

固定一个实际局部 h，令 $A_a,A_b,A_c,A_d$ 为原 local product-J 公式在上述四个**当前捕获**状态/root 的 $d\times K$ 矩阵。它们的列只针对 shape 输入；两项 mean 不反馈 shape。令 $P$ 取完整矩阵的前 K 行，当前切向 $T\in\mathbb R^{d\times K}$。定义

$$
U_a=A_aPT,\quad
T_b=T+\frac h2U_a,\quad U_b=A_bPT_b,
$$

$$
T_c=T+\frac h2U_b,\quad U_c=A_cPT_c,\quad
T_d=T+hU_c,\quad U_d=A_dPT_d,
$$

$$
T_+=T+\frac h6(U_a+2U_b+2U_c+U_d).
$$

cell 首端初始化为 $T=[I_K;0;0]$。这是对原无 mean 反馈的 RK4 组成逐级使用链式法则所得的完整变分式；每个 profile/子步继续此 T，不重置 mean 切向。最后仅 shape Pi 输出行除原 portRatio，均值行不缩放，原 cut 的单独坐标约定也不被改写。

**证明。** 将每个 stage RHS 视为已选 regular branch 上的实可微映射，固定 h 与由 profile 决定的端点。对 $y_b=y+(h/2)f_a(y)$ 求输入微分得到 $T_b$；再对 $f_b(y_b)$ 用链式法则得到 $U_b$；c/d 同理；对最终 RK 加权和求微分得到最后一式。只有前 K 状态进入原 RHS，所以每次局部乘法均为 $A_iP T_i$，而不是把两项 mean 列虚构进原 local-J。线性出口 port 变换最后作用即可。证毕。

这里必须保留两个范围：

1. 以上精确链式法则是 regular branch 的理想实函数/所选固定 step schedule 的陈述；不是对含逐操作舍入、根停机判定或分支切换的字面浮点程序宣称经典导数存在。
2. 实际保存的 local A 与完整 T 都来自原有限角公式和浮点计算，其数值误差仍需原 fresh 模型/非线性试探检验。命题 A 的 primal 字节同一性不自动给出 J 的精度、非奇异性、Newton 收敛或最终闭面结论。

这保留 R266/R272 已明确的 computed-J 与真实导数区分。没有提高/降低原 g、容差、阈值或完成标准。

## 6. 独立源码与第 71 轮最薄真实试验

新模块 basename：`geometry_20261114_noj_matched_variational_engine.mjs`，8,624 字节，SHA-256 `f9b292c4c3f80d1d7b3030ea0350416746795377833661af8d3095e349a73ad9`。

Actions-only 测试入口：

- `geometry_20261114_noj_matched_variational_probe.py`。
- `geometry_20261114_noj_matched_variational_probe_hook.mjs`。

它们复用第 69 轮已冻 `bind_inputs` 进行同一实际第 61 轮末态原件绑定，不重写那套父件规则；只通过新请求循环调用所选 cell 的原 no-J 流与候选 with-J 流。原 constructor/ready/源码/容量/H/target/sigma/far 仍核全。没有完整 evaluate/solve 或旧 J payload 读取。

真实第 69 轮最大 cusp 路径差在 stage11，最大 ordinary 差在 stage12，故本轮建议恰这两个实际 case：

```bash
python topics/visible-flex-larger-amplitude/computations/geometry_20261114_noj_matched_variational_probe.py \
  --native-directory "$ACTUAL61/native-current576-damped" \
  --native-result-sha256 b8754cc3c6f9635bd2f37da56d39811c2c8ef5442aa7947df89078cb416715ef \
  --snapshot-directory "$ACTUAL61/native-current576-damped/iteration-003/snapshot" \
  --snapshot-result-sha256 5e801fe00f206b4dec50c64ac0fcfb8e1fe9225a7d37280e4da9bd4875709286 \
  --source-topic "$PUBLIC78/topics/visible-flexible-closed-surface" \
  --stage 11 --stage 12 --node-heap 6144 \
  --out "$VISIBLE_OUT/noj-matched-variational-probe"
```

输入清单与 69 相同，只需其选择提取件；没有再次下载/展开全部父 J 或因子。固定 seed raw 为 `b34daaf8ad1841b452707c669236ba38731d1f97506af4bbfe1a22e39d814013`，只是失败末态初猜/诊断，不是成功 anchor。

每个 case 保存原 input226、原 noJ 完整返回226、新 candidate 返回226、新完整226×224切向、原和新 post-port shape out、候选 post-port224×224 J、每个真实 step/profile/ordinary/subindex/x/h 与四field的state/derivative/local-A原hash、完整mean/guard报告。raw 一律 `large-arrays/`，artifact-only。

比较字段含完整 226 state bits、post-port shape bits、mean correction state、background mean state以及原 `meanHeight=state[K]+state[K+1]` 的 bits。不同只如实报告，没有 epsilon 门，也不把字节相等冒数学收敛。任一原/新 flow 异常保留真实 phase/stack 与已产生证据；原输入和另一独立 case 不被改写。成功退出只表示所请求 case 返回并完成记录。

## 7. 完整单请求续解的后续切点

若实际第 71 轮支持此实现，后继可把这个新 flow 安装到原 worker 的每个 unique engine，只替 `flowStateWithJacobian`，保原 no-J/RHS/root 函数引用。实际第 61 轮失败末态以原 raw bits 注入初猜，原 H/目标/far/sigma 和 32 轮/十试探/`2e-9` 不变。

新的 fresh-withJ snapshot 必须明确新 flow/source 身份，不能保留“flow 未改变”或“仅 correction 改变”的旧整体范围标签。每轮当前完整 J/r/state 进入新 R273 current576 adapter/QR；它仍只替换非线性 correction，不替换最终 endpoint sensitivity 或 fresh audit。新 final sensitivity 应使用真实新 flow 的已完成 J，final audit 仍原 no-J rk4。若其中任一步失败，应保存其真实失败，不能把通过单段位对照或接受一次 trial 当作完成 native 响应。

完整续解已获源准备授权，但当前只完成候选及最薄试验入口；实际是否派续解由公开试验/回执决定。此分工不增加独立审查门。
