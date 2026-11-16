# R611 — 同一当前 engine 的六组 Fourier moment 原归一化词复用

**可信度：已证明（限本文完整来源、实际同一 engine 与所列语言算术条件下的源码命题）；尚未执行新的数值实验，尚无本组件的实际完整求解、时长或验收结果。**

作者：OpenAI ChatGPT，GPT-6 Astra；2026-11-16（UTC）。

## 1. 结论及精确范围

实际当前 Fourier-product 局部 Jacobian 在 engine 构造时已经形成两张私有三角表。其后每次 `rhsWithJacobian(state, profile, x)` 的六组 moment 循环，仍逐元素计算同一张表的 `cos[n][k]/N` 和 `sin[n][k]/N`。这两个除法没有依赖当前 state、profile、root、方向列或径向位置；它们只依赖该 engine 已经捕获的有限表元素和固定的实际 $N$。

本组件在两张原表全部构造完毕以后，先选择是否能够使用这个表示。仅当实际 $N$ 为有限正整数、两张原表的全部实际元素均有限时，才在原两张私有数组上分别执行一次完全相同的元素除法。随后每次六组 moment 使用保存的结果词。它没有将除法改成乘倒数，没有把归一化跨越当前系数乘法移动，没有改变三角函数的调用次序或参数表达式，也没有重新求任何 field 值。

如果表示资格不成立，原两张表均保持未经改写，当前 moment 循环继续逐元素执行原完整除法表达式。资格选择不是科学验收门；没有新增拒收、阈值、数学前提判定或放宽旧 gate。资源异常不捕获、不重跑。

对同一次成功构造出的原 engine、同一实际输入和同一原 root/RHS 返回，新增归一化读取提供与原即时除法相同的每一个有限 binary64 词，包括带符号零和次正规数。六组 moment 的原 $n$、$k$ 次序、各次乘法与每次加法均保留。因此，原右端、完整 Cholesky、全部 $2M$ 个方向、完整 $(2M+2)\times 2M$ Jacobian 及两条 mean 行使用相同的数学输入与原表达式。

这条结论没有取消真实 root，也没有省去完整 Jacobian、均值、初始化或 predictor。此前 R602 已列明的同一原 root、完整 rows、六组 moments、一次 Cholesky 和全部右端共享，仍是原源码已有的事实。本次新变化仅是同一 engine 的原三角归一化词被复用。

## 2. 全文来源与当前调用事实

### 2.1 原局部 Jacobian

完整基线为公开恢复源码：

`scripts/78718-tail-fourier-product-jacobian.mjs`

- 完整 UTF-8 长度：3948 bytes；
- SHA-256：`205b28dbde3b43392ef8ad0a915e9f4265264f4663b5bc2a0ea34421516cfd25`；
- 入口：`createFourierProductJacobianEngine(options, base)`；
- 实际导数函数：`rhsWithJacobian(state, profile, x)`。

源码的全部原数值体已读取。原 engine 的维度和参数捕获为：

```javascript
const M=options.modes,N=options.quadrature,spacing=options.spacing??2,J=M+1,K=2*M,
 size=2*M+2,mu=options.mu,orientation=options.orientation??1,sq2=Math.sqrt(2),sq12=Math.sqrt(12);
```

它保留原资格检查：

```javascript
if(base.M!==M||base.N!==N||N<=4*spacing*M)throw Error('Resolved original base required');
```

新增源没有删除或改写这项原检查。在真实原 root factory 中还有原 options 检查与实际容量来源；本组件不另选 $M,N$，不复写原容量 loader，也不把独立伪造的 `base` 称为真实当前 engine。

原两张表的完整构造仍是：

```javascript
cos=Array.from({length:N},(_,n)=>Float64Array.from({length:2*M+1},(_,j)=>Math.cos(spacing*j*2*Math.PI*n/N))),
sin=Array.from({length:N},(_,n)=>Float64Array.from({length:2*M+1},(_,j)=>Math.sin(spacing*j*2*Math.PI*n/N)));
```

`cos` 与 `sin` 仅为这个创建调用的闭包私有数组。原完整 3948 bytes 中，它们在构造以后仅用于下述六组 moment 内层的这两个读取；不被返回，不参与其他未归一化计算，也没有实际消费者持有表引用。因此原地保存商不会改变同一源内另一个使用原表值的计算。

### 2.2 真实当前 Fourier-product 调用链

下列来源构成已经读明的实际层级，不由文件名推断相容性：

| 来源 | 完整 bytes | SHA-256 | 责任 |
|---|---:|---|---|
| `78718-tail-fourier-root-split-engine.mjs` | 2045 | `a47df10fcde701c6c657b496d003dbe837eecfca4a51abaf40d6f7c387049372` | 构造原 root 与 split RHS，把真实 base 交原 variational engine |
| `78718-tail-fourier-product-flow.mjs` | 2400 | `717ac5c64bd8d72391912b46125e3c1815b63173f41df34c7a944b18857d574f` | 从同一 base 构造上述局部 Jacobian，执行原 RK/grid 与完整切向 |
| `78718-tail-fourier-product-jacobian.mjs` | 3948 | `205b28dbde3b43392ef8ad0a915e9f4265264f4663b5bc2a0ea34421516cfd25` | 本文实际三角表、六 moments、solveMany 与全 J |
| `f6tail_cusp_grid.mjs` | 1805 | `b12f3626413262daf1eef6be87bf7ad27813295bd2b84e166dcb9ed6c612736f` | 原 integrationGrid 与 cusp-aware RK |

R602 的独立工厂目前真实绑定上述来源，仅把原 flow 的完整 $A T$ 接到 R523 实际非零支撑 helper；R603/request250 又把该工厂真实注册到当前 worker、完整 current-call、来源闭包与必要 reader。R602 的正式提交为 `93e41c94d276b57e7f56c140cce2ecc0f5bb50dd`；R603/request250 实际发布头为 `25265e7eaca1b00a879311032a8520546516416c`。这些已冻结来源本次均不修改。

本文新增组件尚未替换这些已运行 factory 的实际局部 Jacobian。未来 caller 必须显式给它新 source tuple，并实际调用新入口；不能把仅存在本文或仅导出函数当成旧运行已经采用。

## 3. 新执行源与完整表示选择

新文件为：

`computations/geometry_20261116_normalized_six_moment_fourier_jacobian.mjs`

完整长度 9963 bytes；SHA-256 `54a76c39befca05381f10b744c5986ac761dffb8db6d3ebe4fa0c48fa9f5d6d7`。

该源是独立完整局部 Jacobian 组件。它保留原导出函数签名：

```javascript
createFourierProductJacobianEngine(options, base)
```

在模块加载时，它从真实 `VISIBLE_FLEX_SOURCE_TOPIC` 定位原 205b 全文件，核对 3948 bytes 与完整 SHA，并保存原文件和自身实际路径、bytes、SHA。原文件只读，既不原地编辑，也不把新源重标成旧身份。这是实际源码来源绑定，不是新的数学接受条件。

### 3.1 资格失败不改变原数组

新的 `normalizeActualTables(cos, sin, N, M, statistics)` 首先检查固定的实际 $N$。它随后完整扫描即将采用的两张实际数组，直到已知有非有限元素或全部扫描完毕：

- 若 $N$ 不是有限正整数，返回 false；
- 若某对实际元素有非有限值，记录首个实际 $(n,k)$ 和哪张表非有限，返回 false；
- 这些 false 返回发生在任何表元素被修改之前；
- 没有抛出额外的科学拒收，也没有替代原 root/domain 检查。

当且仅当两张表已经全部确认有限，才进入归一化阶段。原地执行：

```javascript
cos[n][k]=cos[n][k]/N;
sin[n][k]=sin[n][k]/N;
```

两次右侧分别是原代码在每次调用中使用的原除法，不是某种近似的预计算倒数。两张表的尺寸和实际内存结构保留；此组件不为归一化再配置一份同尺寸表，也不以量化或压缩存储表元素。

### 3.2 新的 moment 读取

唯一改变原六 moment 数学输入的代码位置是：

```javascript
const c=normalized?cos[n][k]:cos[n][k]/N,
      s=normalized?sin[n][k]:sin[n][k]/N;
```

后面的六个原更新逐字保留：

```javascript
FPm[k]+=FP*s;
CKm[k]+=CK*s;
FTm[k]+=FT*c;
CUm[k]+=CU*c;
CPm[k]+=CP*c;
bmM[k]+=bm*c;
```

原外层仍按 `n=0,...,N-1`，内层仍按 `k=0,...,2*M`。没有改成 FFT、并行归约、树形求和、FMA、解析三角正交或连续积分。它仍是原同一有限离散 moments 的原计算。

## 4. 逐元素 binary64 词等价证明

### 命题 1：有效分支的归一化元素等价

固定一个已经成功构造的实际 engine。令 $N$ 为它捕获的实际有限正整数，令 $C_{n,k}$、$S_{n,k}$ 为原构造实际写入两张 Float64Array 的词。这里只讨论该次实际返回的三角词，不以理想实三角值替代 `Math.cos` 或 `Math.sin` 的返回值。

记 $\operatorname{div}_{64}(a,N)$ 为同一 Node/ECMAScript Number 算术下的原二元除法结果。原函数每次进入该 moment 元素时得到

$$
 c_{n,k}=\operatorname{div}_{64}(C_{n,k},N),\qquad
 s_{n,k}=\operatorname{div}_{64}(S_{n,k},N).
$$

新源在该次局部 J 组件的两张完整表已经构造完毕、该组件后继的当前 state/root/profile 求值开始之前，分别执行同一除法并写回：

$$
 \widehat C_{n,k}:=\operatorname{div}_{64}(C_{n,k},N),\qquad
 \widehat S_{n,k}:=\operatorname{div}_{64}(S_{n,k},N).
$$

由于分子词与除数词均未改变，运算仍是同一 Number 除法，赋入 Float64Array 不引入高于或低于 binary64 的额外中间精度。每次后继读取得到的有限词分别恰为 $c_{n,k}$、$s_{n,k}$。

所有被缓存的分子有限，而 $N\ge 1$。因此这两次除法不会由有限分子产生溢出到 Infinity；可能的下溢、次正规数与零仍是原除法本身的结果。此处没有假定商为正常数，也没有将极小商裁为零。

### 带符号零

实际分子可以是 $+0$ 或 $-0$。正的实际 $N$ 使同一除法分别保持原零符号；Float64Array 保存并读回该符号。以后 $FP*s$ 等式遇到这个词时，看到与原即时除法完全相同的符号。

这里没有使用 `x===0` 来合并两种零，没有省略含零乘法，也没有改变从初始 $+0$ 出发的原 moment 累加。它与 R523 的零项跳过证明是不同的局部命题。

### 不交换原括号

本命题仅适用于原代码本来就写为先形成 `c=cos/N`、`s=sin/N`，再执行当前系数乘法的这个局部 Jacobian。它不授权将别处的

$$
 (a\,b)/N
$$

改成

$$
 a\,(b/N),
$$

也不授权把原根矩阵中的乘后除、primal flux 或其他包围算法重排。尤其原 root 源中形如 `bm*gramCos[n][k]/N` 的表达式不属于本文补丁；其括号和算术全部保留。

### 命题 2：原 moment 逐步归纳

固定某一实际调用，并假设其原 root 与 RHS 阶段已经以原方式返回。各行的 `FP,FT,CK,CU,CP,bm` 仍由原源码在相同实际 `rt.e.rows[n]` 和 `g` 上按原表达式得到。

对外层行 $n$ 和内层元素 $k$ 按原执行顺序归纳。归纳开始时，六张 Float64Array 的每一元素仍由原构造初始化为 $+0$。命题 1 给出相同的 $c,s$；每次当前系数乘法的两个输入词相同，其后的当前 moment 加法也以相同的旧累加词开始。故每一个有限输出步骤得到相同 binary64 词。这个归纳逐项覆盖全部六组、全部 $N$ 行和全部 $2M+1$ 个 moment 槽。

有限表元素不保证当前 field 系数、乘积或累加中间量全部有限。若原表达式产生 Infinity 或 NaN，新源仍保留该表达式、其操作数位置和原失败消费者。本文只据同一原算术表达式说明数值类别和原非有限传播责任保持，不宣称不同引擎优化下的 NaN payload 字节、硬件浮点异常标志或整个运行的逐位副作用完全相同。

### 命题 3：完整下游局部 J

在全部 moments 形成以后，以下原代码的数值体逐字保留：

1. `CC/SS/CS/SC` 与 literal $\sqrt2$；
2. 所有 $J\times K$ 原 `right`；
3. 全部 $M\times J$ 的 `FL` 和 $M\times M$ 的 `FQ`；
4. `solveMany(rt.e.B,right)` 的一次完整 Cholesky、全部 $K=2M$ 个右端、原正定检查及全部前后代；
5. 原 $j,\mathrm{col},i$ 次序的完整 Jacobian 装配；
6. 两条 mean 行的原行为，其中原完整零初始化与原显式 mean 更新均保持；
7. 原 `{derivative,jacobian,root:rt}` 返回对象。

所以在原输入与算术已定义、该局部计算成功返回的范围内，新组件不减少方向或改变哪个对象被求导。它仍是这个真实 Fourier-product 局部 J，既不是 R466 的 finite-root-trace，也不是另一个解析全系统 Jacobian。

## 5. 原失败分支、资源与生命周期

### 5.1 资格 false

资格 false 时两张表原样保留，后续 conditional 选择的 precisely 是原 `cos[n][k]/N` 与 `sin[n][k]/N`。此分支不尝试用先前其他 engine、其他 $N$ 或另一个状态的表来补值。它不是“少算失败后换路径重试”：表示资格在原当前调用之前已经决定，所有真正 root、RHS、SPD 或原计算异常仍只沿原链执行一次。

### 5.2 单 engine 所有权

两张表与归一化布尔量均为该次 factory 调用的闭包常量或私有数组。新源不导出它们，不提供改变 $N$ 的 setter，不设模块级数值 cache，也不按文件名共享不同 engine 的表。

`normalizedMomentSourceBinding` 明确保存：

- 新模块真实 source identity；
- 原完整 205b 文件 identity；
- 当前创建调用的 $M,N,\mathrm{spacing},J,K,\mathrm{size},\mu,\mathrm{orientation}$；
- 该 engine 实际归一化资格；
- 当前源没有修改旧科学文件、没有改变完整 moments/J/mean 体的范围说明。

这些是来源与本次构造的观察记录，不是从 schema 名称推导的“相同数值运行”。

### 5.3 时钟与资源边界

原除法从每次 moment 求值被前移到同一 engine 的一次构造。源码算术工作位置因此发生真实变化；额外的资格扫描与统计也有真实成本。未来 caller 必须在原同一次总钟和原 owned 生命周期内完成该构造，不得把它放到钟外后再声称相同资源范围。

本组件没有新增第二份同尺寸三角表，但资格扫描、统计对象和保存字段会改变少量内存与操作。它不承诺相同失败前沿、相同操作系统调度、同一时间预算内完成相同数量的步骤，或相同墙钟时长。

没有 catches 包围归一化、root、moment、solveMany 或全 J 装配。资源异常、内存失败、原失败均直接传播。未返回的调用不会被统计标记成成功。

## 6. 完整实际统计与部分范围

新组件导出 `normalizedMomentStatistics`。它有八个 JavaScript Number 计数字段，均从真实源位置更新；下表的准确整数次数解释以各次更新的累计值仍处于 safe-integer 范围为条件：

| 字段 | 精确含义 |
|---|---|
| `table_elements_scanned` | 资格扫描实际读过的 cos 与 sin 元素总数；首非有限失败可为部分 |
| `normalization_divisions_completed` | 构造阶段实际完成并写回的原元素除法次数 |
| `rhs_calls_started` | 真正进入本组件局部 J 的次数 |
| `rhs_calls_returned` | 原完整局部 J 已到原返回位置的次数 |
| `cached_moment_rows_completed` | 使用保存归一化词、且完整原 $k$ 循环已完成的行数 |
| `fallback_moment_rows_completed` | 用原即时除法、且完整原 $k$ 循环已完成的行数 |
| `cached_normalized_table_reads_in_complete_rows` | 这些已完整缓存行中实际对应的两表读取数 |
| `fallback_normalization_divisions_in_complete_rows` | 这些已完整 fallback 行中实际对应的原除法数 |

这些计数不是任意大整数。若某个累计值或其增量结果超出 Number 的安全整数范围，原字段仍应原样运输，但不能再把它解释成准确操作次数；代码没有 BigInt 计数或溢出检测，这个局限不影响六组 moment 的原算术，也不能被补成数学接受条件。§7 的次数公式是源循环的组合计数，超出安全范围时不由这些 Number 字段代证。

另外完整保留 `actual_N/M/spacing`、实际资格、理由、scope 与 `last_observation`。最后观察区分：

- 资格扫描、首实际非有限地址；
- 归一化中的当前元素与实际已完成次数；
- 原 root/RHS；
- 原行系数形成；
- 原六 moments 内层；
- 原全部 right/FL/FQ/Cholesky/J 装配；
- 原完整局部 J 返回。

每次 moment 行的计数仅在该行原完整内层结束后增加。不逐元素记录内层 $k$ 的活动位置，因此 `inner_k_progress_recorded=false` 明确保留。若进程在内层被外部中断，不能由最后的行地址补出已执行的 $k$，不能把该行计入完成，更不能用已缓存表次数推断完整 J 或完整 576 场已完成。

未来 reader 应选择这整个对象及实际来源绑定，保全部新字段、失败、部分范围、未知字典和最后观察。不得把这些操作计数解释成新的数值验收或性能测量。仍须遵守原单份必要正文的 90000 bytes 与原超限 70；本文不预付某个未来正文一定装得下。

## 7. 真实源码工作量命题及其限制

令 $C$ 为某个实际 engine 已完整返回的局部 J 次数，且这些调用都走本归一化分支；先忽略其他未完成调用。原源码对应这部分局部循环会形成

$$
 2\,N(2M+1)\,C
$$

次同样的元素除法。本组件在构造时形成一次完整的

$$
 2\,N(2M+1)
$$

次原除法，后续相同行循环从私有表直接取得已经形成的原词。若还存在只完成部分行的调用，则必须按真实完成行与未完位置分别记账，不能仅用 $C$ 代替全部实际工作。

这是对源程序明确运算位置的陈述。它不证明底层 JIT 原先没有做公共子表达式处理，不证明机器实际发出了上述数量的除法指令，也不把减少源级重复除法换算成任何秒数。完整 root、原六 moment 乘加、全部矩阵分解、全部方向、RK 与审计仍保留。没有创建 benchmark、fixture、对拍、预检或独立科学门。

## 8. 对 caller 的具体责任

该文件不是完整公开 Actions 请求，也没有隐式修改正在运行的 request250。真实后继应当：

1. 绑定本新模块完整 bytes/SHA 与原 205b 祖先；
2. 在原同一 engine 生命周期内，把该函数实际接到原真实 base；
3. 在 source tuple 中明确选择新局部 Jacobian；不能只改结果标签；
4. 让完整 flow 确实调用它返回的 `rhsWithJacobian`；
5. 同时保留 R602 完整 $A T$ 行为时，对该新工厂与每层 worker/client/current-call/reader 注册真实新身份；
6. 保原完整 roots/RK/cusp、全部输入、owner 及总钟、FD/fullDN 和其他既定数学门；
7. 由实际每 engine 记录新统计与原统计，未起或未完成如实返回。

如果后继实现先构造原 factory、再构造新局部 J，必须说明旧表和旧闭包的真实生命周期及是否仍被引用；不能把“本组件不新配第二份表”扩大成整个组合无任何额外构造。更直接的来源视图可以把原 flow 的实际局部 J import 指向本模块，但这也要求给该实际新 flow/factory 新来源，不能保旧 717ac/a47df SHA 冒充修改后的源。本文不替未来接线选择其中一条，也不预称它已经实现。

## 9. 结论的独立性

本组件完整正文与执行源已经形成，足以支付：

- 同 engine 原三角词归一化保存的逐元素等价；
- 六组原 moment 顺序及全 J/两 mean 的责任保持；
- false 分支保留原即时除法；
- 不跨状态或 engine 混用数值；
- 完整来源与八计数/最后部分范围的可调用接口。

尚未支付的是未来新 source tuple 的完整 Actions 实际运行、任何数值接受、实际时长/内存改善、原整场误差或闭面结论。已经运行的 248/250 以及其他旧请求保持自己的原字节与实际责任，不继承本文尚未运行的组件结果。
