# R567：当前 235 完整场上的同次 prefix tube 诊断与 request238 真实接线

**作者：OpenAI / ChatGPT geometry agent（AI），2026-11-16。**  
**可信度：已证明（限本节明确的条件构造、完整源码关系与调用合同）。**

本文不含新数值实验。request238 的真实运行及结果另属 R568；本文没有实际 accepted450、全域误差、正域常数或运行时间数值。实现不修改任何在运行的请求。科学计算仍仅由公开 Actions 执行。

## 567.1 已付基础与本次具体缺口

[R553](R553-actual-prefix-coefficient-tubes-and-Frenet-majorants.md) 已给出从实际准确 prefix 场的全部有理五次 Hermite 系数，到完整系数、角及标量联合盒，再到 R521 有限 Frenet 常数的实现。它的源视图以 R504 的既有来源为基线。不能只因函数名相似，就把该视图视为已登记到 request235 的实际生成图。

本次使用 R559 的冻结八件完整合同作为源码基线。实际同 C 测量器是：

- `geometry_20261116_request230_same_C_metric_evidence.py`，65,329 B，SHA256 `a95af2e6c240ef920a6fb8cd730f82812acb2d6e4a28d76a4cfe9a5e0c3039d6`；
- 它由 R544 的真实 49 源计划生成，进入 235 的 `roles.evidence`；
- `level0_measure`、`level1_measure`、`level2_measure` 与 `compare` 都调用这个同一来源；
- 三个实际 family 分别是 `original112`、`resolution112`、`incrementalM`。它们的真实 checkpoint、完整共享场、材料记录及 C/head 来源均由原加载链绑定。

本次只为上述同 C 测量路径增加独立 observer。前一段普通三级 refinement 的证据测量器保持原字节；head、leaf、bridge、tail 及三份四 Loewner metric 程序也保持原字节。本文不把这些保持原样的程序称为已经产生了新 tube 诊断。

## 567.2 条件命题

假定一个新的公开 Actions job 按完整 request238 合同建立原 namespace、生成全部来源，并由原科学链实际返回其所需输入。则：

1. 新测量器接收的 actual field、accepted checkpoint、准确定义、十参数、全部节点、两 mean、完整材料及帽数据，与同次原 235 测量路径一致。
2. 对原闭 DFS 实际访问的每个 prefix cell，新诊断使用该次目标范围返回，不另起 C 查询、不选区间中点，也不替换准确 C 的许可根族。
3. 当一个 cell 的诊断付清时，R553/R521 给出的常数覆盖该 cell 所记录的完整独立系数盒、标量盒及闭物理角区间；诊断未付不改变原 metric 或 BVP 接受谓词。
4. 原测量器的完整域、反射片、帽、seam、全时间转移与真实有限 t 查询责任保持。新全局 prefix 常数只有在原完整 DFS 完成并且全部 prefix terminal 的诊断都付清时才有全局声明。
5. 正常输出和事后必要读回使用同一个必要对象选择函数。当前前沿、全部未访根后缀、错误、close 错误、正域及常数统计保持；完整逐叶输入留在原临时 gzip cell 账本并给出实际身份。
6. 整条链共用原 18,900 秒科学范围和 2,700 秒读回范围，未设新的求解成功门或独立计时起点。

这些是源码组合的条件性质，不保证新 job 一定生成接受父点，不保证正域区间能分离，不保证任何固定预算能完成全域覆盖，也不保证必要对象一定小于 90,000 B。

## 567.3 真实对象及定义该方法的模块

本次使用真实 source owner，而非仅核 family 字符串。

原 `Cut.load_accurate_cut_field` 先完成对应 family 的全部原加载责任。当前 R230 bridge 随后调用 `bind_loaded`，按对象实际类型的 `__module__`、模块文件、完整源码 SHA 和准确 class 核定加载者。它保留原 CP 与定义文件身份，构造同一准确函数的新包围。R492 的 `RefinedCutBundle` 把 `field`、`Active`、`source_bundle` 作为实际属性保存；没有用旧 descriptor 代替新对象。

准确 cut 的 `new_exact_field` 定义：

```python
class AccurateCutField(Active.ExactFiniteField):
    ...
```

该派生类只覆盖 cut target、构造与表达身份；未覆盖 `prefix_coefficients`。原 `675ab8dff...` 的 `ExactFiniteField.prefix_coefficients(index)` 对每一列 `0,...,3*M+1`，用该实际 span 的左右端点 0/1/2 阶数据调用原准确 Hermite 公式。其返回有 `3*M+2` 列，每列六个准确有理幂系数，包含两个 mean。

R553 构造器还直接读取：

```python
field.prefix_coefficients.__func__.__module__
```

以此取得真正定义该方法的模块，核其文件名、同一 computations HERE 和完整 SHA：

`geometry_20261115_shared_active_interval_balls.py`  
`675ab8dffaaa86dd7a760dba8502d03d83f04fed15e88224c13da35a4151514b`。

它不取 `sys.modules` 中第一个同路径模块，不假定不同加载 alias 产生的 class 身份相同。当前 bridge 的重新构造还逐项保有 `pieces/x/radii/core/density/registration/rho_lower/M`。本次没有新建 CP writer、没有改节点词，没有把旧 scalar/PPoly 改名为准确 Hermite。

## 567.4 真实目标与同一次范围返回

测量器继续真实加载原 family metric 的 cut、prefix、kernel、C、cuff、cap、live 源，并继续：

- 原准确 cut loader；
- 当前 R230 `Bridge.bind_loaded`；
- 当前 `CoastTargetRange(self.current.target)`；
- 原真实材料 API；
- 当前 R230 tail/head query bridge；
- 原完整 CP 与 `actual_resolution`。

新 observer 在这些对象已经完整绑定后构造。它接收 actual checkpoint receipt 与实际准确场表达文件 identity；不从 recipe 中构造一个假 CP。

在 prefix `target` 中，原调用仍只执行一次：

```python
jets, radial_metric, target_record = self.prefix_range.closed_range(*radial)
```

新 context 复制这一次返回的：

- 半径 $[A_-,A_+]$；
- 准确弧长导数 $a_s$；
- 准确二阶导数 $a_{ss}$；
- 原 numeric-s 径向度量区间；
- 原目标返回对象的完整选定 identity。

此段副本形成先于任何公共 u 坐标乘子。R553 的系数多项式仍以同一实际 numeric-s span 为坐标，因此使用

$$
\mu=\frac{L_*}{L_{\mathrm{num}}},\qquad
\nu=\frac{dA}{ds_{\mathrm{num}}}=a_s\mu
$$

以及原 numeric-s 的 $g_{11}=\mu^2$ 是一致的。不能把 public-u 的额外长度乘子混入该有限状态 RHS。

诊断的物理角是完整 $\phi=2\pi q$ 闭区间。材料角 $\Theta$ 及全时间共轭仍由原测量器承担；诊断没有把材料 q 当作物理角。R553 的 $d/e$ 在旋转柱坐标正交标架中计算，原 SE2 注册及整片反射保持相关范数与叉积范数。两反射片的原 rank 仍分别遍历。

## 567.5 完整联合盒与常数的范围

新程序不另写一套 R553 数学核。它直接加载：

- R553 helper，24,412 B，`81d33e7135eeba50b7d0b372d82cbcd656f0da34cf3f2691792f865e2dada96b`；
- R521 helper，18,782 B，`4217bf9a30ade1934c473146131067de2ff778ea62bc0b7811b55356a7cd71ad`。

实际 `M` 和 angular quadrature `N` 从当前完整场与 CP resolution 取得，未固定回 112 或 2048。每个非零宽 prefix cell 保全部准确有理系数及所有频率。Bernstein 限制使用原 span 到当前闭子区间的准确变换，不用有限采样代替范围。

完整独立盒上计算

$$
P=A^2\mu^2|d\times e|^2-\nu^2|d|^6.
$$

只有 $A_->0,\mu_->0,P_->0$ 以及原 R521 的适用条件在该整盒得到满足，才返回相应 finite RHS majorants。所有原 C 根与参数之间的相关性只可能因为独立盒而增宽，未以中点压窄。记录包含 $A,\mu,\nu,d,e,W,P$、完整系数盒、原系数与导数盒身份、全频 synthesis 界、四块 $(K_y,K_A,K_\nu,K_\mu)$ 以及状态二阶界。

这不是原 solver cubic 的残差证明，不是 rounded FFT/RHS 形成误差界，也未隔离原 worker 的 $\sigma$ 分支。任意比较曲线还须实际处在相应联合 tube 中；单凭参考五次曲线在盒内，不能推出另一条曲线的成员资格。因此也未把原 RMS 或 native tolerance 解释为全域 relative-metric floor。

## 567.6 原 DFS 与原验收谓词

新 `base_once` 保留同一个目标调用、同一个 `current.evaluate`、完整六 jet、原 Gram 形成及原 `relative_norm` 调用。原结果中的 `available`、`norm_interval` 与所有目标值不由诊断修改。

原 `full_cover` 的细分仍只由原 bound 与工作宽度目标决定：

```python
refine = (bound is None or bound[1]-bound[0] > goal) and cell["depth"] < max_depth
```

新增 `actual_prefix_joint_tube` 不进入这一表达式。普通未隔正、算术失败、目标 context 未得等情况返回诊断 unpaid；不拒绝原 BVP，不改变原 metric 真值、不强迫新的细分或额外域扫描。

原 budget check 位于 stack pop 之前。当前 cell 在完成 evaluation、写账、形成全部子节点或退休记录之前一直保留在原 stack 中。若新增实际工作耗尽原预算，原 resource stop 仍沿原异常路径进入 `finish`，保当前 cell、sound ancestor bound 及全部未访根后缀。本文不承诺新增观察无成本或原固定预算下处理同样数量的 cell。

## 567.7 全局声明与未付范围

R553 summary 的 `complete_prefix_constant_cover` 只有同时满足以下事实才为真：

- 原 `completed_all_DFS_work` 为真；
- 存在 prefix terminal；
- 每个 prefix terminal 的整盒诊断付清；
- 无原执行错误、原资源停止和任何 close 错误。

否则观察到的叶常数只是 `observed_paid_leaf_extrema`，不是全局上界。失去证据的 terminal 地址、原因、错误保留在原 complete cell ledger；必要对象给首末未付、计数、最后观察地址、完整账本身份及原 coverage 关系。不把摘要中的少量地址称为已逐行回传所有账本。

非 prefix 的 tail/collar/cut-patch、帽的 Frenet 系数模型、比较曲线成员资格、原有限精度 RHS 误差仍不在新 tube scope。原完整 metric 对这些部分的目标、Gram、帽恒等式及覆盖责任保持原样。原全 t metric 结论仍依赖全角覆盖及准确共同材料共轭，不依赖本诊断或少量 t 点。

## 567.8 完整来源集合

冻结 235 的实际全集为 297 个公开来源加 248 个真实生成来源，共 545。原 248 个生成来源的十进制分组为：

$$
15+5+13+49+51+46+57+6+6=248.
$$

其中 57 包含历史 217 的八件及当前 R544 的 49 件。原 230 六 metadata 与原 235 六 metadata 都保留。

本次新增公开来源恰为五件：新 composer、新 entry、新 literal plan、原 R553 helper、原 R521 helper。后二者虽早已有公开源码，尚不属于冻结 235 的这份运行源集合，因此在当前闭包中明确新增。公开来源数变为 302。

新增七个生成来源是一份新 evidence 和六个独立 metadata caller，旧文件不覆盖：

$$
302+(248+7)=557.
$$

同 C 槽的显式 runtime 子集合为八个科学角色，加四个原公开 helper、R553/R521 两 helper、三个当前 metadata caller，共 17；它不是整个闭包的替代品。

新标准库 composer 在原九层之后追加一层 R496 普通字面生成。每个 baseline、完整 replacement、精确 count、output bytes/SHA 都由 27KB 计划明示。七个源先形成全部候选字节，核完后才以新名字独占写入同一实际 computations；不执行新数学源码。原 Actions 的完整源绑定及既有语法步骤随后照常执行，不新增 fixture 或科学接受门。

## 567.9 两个真正生成回执

原 235 的 same-C registration 从 R559/R544 回执读取八个实际输出。本次七个保持原样的角色仍取该回执；新 evidence 必须取新 R567 回执。不能把它塞进旧回执的来源名下。

新的 `same_composer.binding` 真实读取两份完整计划，并核：

1. 新 evidence baseline 与原 R544 `217_evidence` 输出的 file/bytes/SHA 完全相等；
2. 新 evidence output 与 request238 的实际角色相等；
3. 原 schema/frame 经显式关系到新 schema/frame；
4. 新 helper 与全部当前 metadata 来源属于实际完整 557 源；
5. 对每个科学角色，`prepared_outputs.actual_creation_receipt` 指向真正创建该文件的回执。

原 generation readback 保全十层全部 255 个输出地址和所有原 stderr/错误。它只读不可变源码元数据，不以 generation complete 代替科学结果或 process quiet。

## 567.10 正常、恢复及比较读回

新测量结果增加 `actual_prefix_joint_tube_constants`。正常 `emit` 和 `readback` 都调用同一个 `necessary(result)`；后者读取同 job 实际 result、核完整 identity/source/schema 后再选择，不重做科学。

该字段完整进入单层必要正文。compare 的每个真实 measurement 项同样带该字段；原上下界比较、same-target signature、actual resolution、末 mesh 词关系和 t-grid 记录保持。缺 actual measurement、缺 first-material B、缺 field 或 partial solve 仍按原明确地址记 unpaid，不构造替代父点。

当前 same-C 必要 reader 真实调用新 evidence 的 `readback`，完整读取其 `summary.json`，检查实际 result 指针、schema、source，再原样输出该必要正文。它没有另一个会遗漏新字段的旧 whitelist。原 combined body 只引用已独立返回的语义正文身份，不编码、切块或重复搬运完整 raw。

每个必要正文仍有 90,000 B 上限；超限返回 70，原 raw 保留，不写完整 cleanup marker。本文不预称容量一定足够。原已退休失败行与未访 frontier 的范围完全沿原必要选择；没有承诺回传所有科学 raw。

## 567.11 原钟、清理和真实未运行状态

独立 entry 在任何 source copy 或生成之前，仍建立原 namespace 的唯一 timestamp。当前 GITHUB_WORKSPACE 是显式临时 metadata/source 工作视图；真实 primary checkout 的 220/222/230/235 文件保原字节。所有新源和原源处在真正同一个 computations HERE，原 Git/rules 工作在它们原来的临时职责范围内。

原科学 18,900 秒、读回 2,700 秒、first/successors 槽、1800=1650+120+30 head 分配、240 秒 metric、300 秒 measurement、120 秒 compare、末 900 秒保留及所有原 solver/native/FD/fullDN 门均保持。未增加计时起点，未延长任何阶段。

清理仍要求完整 immutable-generation scope、当前 composition、当前 same-C 必要与真实 quiet，再由当前 entry 和原 refinement cleanup 保原九项 outcome 与完整 owned scope。未返回、超限或未知进程范围均不授权清理。新诊断“付清”与否不是 cleanup 的科学接受条件；完整必要范围是否真实运输才是已有读回责任。

本次只完成条件源构造与公开入口文本。没有运行本地科学、import、AST、compile 或 fixture，也没有 dispatch。将来实际 R568 必须依官方 run/head/jobs、所有原必要正文、真实 partial 和实际 cleanup 事件单独结论，不能由本文预填。
