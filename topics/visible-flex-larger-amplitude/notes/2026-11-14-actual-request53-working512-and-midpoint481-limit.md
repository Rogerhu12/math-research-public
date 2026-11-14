# Actual53：512工作行把当前 QP 残差降到浮点小量；真实回溯仍由未建模中点481限制

**分类：启发式/数值证据，不是存在性、等距性或闭曲面完成证明。**  
**作者：ChatGPT（amplitude；root 负责唯一原包下载、raw 文件审计与发布）。**  
**日期：2026-11-14。**

本轮从实际51保存的场继续同一冻结十五查询入口，只把工作行预算由256改为512。实际完整局部 QP 的最终违例和 KKT 诊断已很小，全向量修复仅为 `0.9999999999987809`，没有再发生大幅径向缩小。但原非线性回溯仍退到 $\alpha=1/64$ 才接受暖场：最近失败 $1/32$ 的15个已建模完整角网格全正，唯一坏的原 collocation 中点是481。这区分了当前模型的求解精度和原未建模域查询的限制。

实际新暖场仍 `success=false`、`new_coupled_finite_acceptance=false`。没有在当前非零 $H$ 上完成 native tail，没有完整 BVP、闭组装或全族 held 幅度结论。

## 1. 实际运行与原件身份

- Public Actions run：[43634517255](https://github.com/Rogerhu12/math-research-public/actions/runs/43634517255)。
- 数值 job：`132568287151`。
- source：`dd3156cfe7e5197029ce45fff5beb53115de3680`。
- 原父恢复通过；warm step `19:53:54Z` 至 `20:03:18Z` success。
- 原 FD step 至 `20:03:44Z` success；publish 至 `20:04:08Z` success；job `20:04:10Z` success。
- 原 artifact：`14130276143`，`visible-followup-condensedqp-43634517255-1`，418958662 B。
- 原 ZIP SHA256：`2aee9406e2025bc8d7c61060a053715ad9e26d8b51f43ee297d7cb586d4f566d`，root 唯一下载已核。

公开小件目录：

[public-actions-43634517255-1-condensedqp](public-actions-43634517255-1-condensedqp/)。

| 实际文件 | 字节数 | SHA256 |
|---|---:|---|
| `fifteen-condensed-warm/warm-001.json.gz` | 4760111 | `e71a5fec344326df3b6c69ec6d298f5079034fb86eb2fa505008c35682010d32` |
| 原 `fifteen-condensed-warm/driver-status.json` | 1251975 | `6170aba505c2eeb5db9411f13ad502363fe1593a7d4d63faa5f0d0a37fb34938` |
| `fifteen-condensed-warm/model-000.json` | 614607 | `43ee3bce4d195131984bca43b559b449574070dc1cc177a55488d0dbdae97362` |
| `fifteen-condensed-warm/condensed-QP-summary.json` | 88441 | `0c52a588909d75b6b898f722efc301a0e7019500da52ccda150df9afb56bf5d0` |
| `fifteen-condensed-warm/condensed-versus-C-comparison.json` | 19261 | `8144e399f6794fa01787e00390e6c107484b98f0e161aa07d320e5a37a045b6a` |
| `physical-response/response-check.json` | 634024 | `3fc6cf8f83ebdee75499064b697ac02c28120ebf44df2bc8727224ae7bbbca84` |

原 status 超过1 MB，公开件是157158 B的 `driver-status.json.gz`。下轮必须透明解压恢复上表原 JSON 字节再核 SHA；不能把压缩件 SHA 当作原 status SHA，也不能重新格式化 JSON 后冒充原件。

## 2. 真父链、范围与固定数学源

实际父 pair 为51：

- warm `b6620a0ce55be257fc58c29e88187cc602ad08b46c4424903ffddc003b5b1595`；
- status `267451f8eb91ca568ff187bfb39dbd32b22ca844788e1e88165910190ad6f685`。

父完整 `optimization_warm` 与本次 `resume_producer` 逐值相同；父 status identity 与父 warm 一致。本次 B 基点 mesh/states/RHS 来自这个真父场，转换原 JSON binary64 后分别与保存 B 数组原字节相同：

| 数组 | shape | B 基点字节身份 SHA |
|---|---|---|
| mesh | 699 | `7cef3604718c2d21dc4f0c866d29a08dc05b1596b49e4ea81a415cf9a9dc68bb` |
| states | $699\times453$ | `fc68d378519687bd11dab90a373bc31753ce7d78059b717766381de6775ec99f` |
| RHS | $699\times453$ | `13cb5ba4b3f7ad144d2cc4d3339c3c0c21451e933e9cadf0b5be3cfefefebd50` |

原十五查询和三个源仍为 [十五查询接口](2026-11-14-fifteen-query-condensed-warm-interface.md) 的冻结版。没有新增中点、角点、频率或节点：11个原左 RMS 查询469、470、471、472、473、475、477、479、480、481、482，加4个原中点473、475、477、482；每个查询2048角，总30720行。完整 B 支持469–483共15个物理节点及3个全局控制，局部5073维；完整未知维仍236036。

C 基线只修正471–482及全局 $p$ 的4059维，469、470、483等外部原方向贡献完整进入仿射 offset。R270 候选则保留完整外部条件最优响应，不把 C 的固定支持误当 H 的自由度。

本轮继续 $\lambda=270$、原 LSMR200、C Hildreth200、局部 dual200、600秒候选/90秒试步保留/30秒恢复保留、原17个试步上限。唯一优化参数变化是 `max-working=512`。但父场和本轮固定权重也随实际续接更新，因此51和53不是同一个 $A,b,W_r$ 的预算配对试验，不能跨轮直接相减 merit 来当作只改预算的增益。

## 3. 原基点、原算子和 B 实测检查

本轮新的固定权重 merit 为 `44.11665947585927`。基点原读数：

| 原读数 | 值 |
|---|---:|
| 完整物理 col 最大绝对值 | `0.007110002311305403` |
| 完整边界最大值 | `6.280522697136224e-8` |
| 左边界、常值行 | 0、0 |
| 原4096均匀物理角 $\rho_{\min}$ | `0.16604058243275` |
| 原节点/中点域失败 | 0 / 0 |
| 两个原 RMS 分数各698查询失败 | 0 / 0 |

B model：`6639ba739dd61b263bd51f62bcf08b0eb94e15be841e8d1ab941e534c1cedacc`。原 A 的88次 Jacobian 调用中只捕获所需原块，实际15个节点/15个版本；原返回 J/P 未改，没有第二次完整 J。保存 B shape为 $30720\times236036$、局部 $30720\times5073$。

原 Actions 已保存的实现检查：

- B 伴随最大归一化误差 `5.232211578097483e-18`，local/full作用差0。
- 真实本轮 LSMR 全方向经原 nonlinear Hermite/control complex 链的 B 导数相对误差 `8.716450228259142e-13`；另一个 seeded 方向 `8.443645936121466e-13`。
- 原物理 collocation 独立 complex 方向误差 `8.673617379884035e-19`。其范围只包含全部 free inlet core 与全局 controls、内部物理坐标方向为0；不能冒称独立检遍全部内部方向。
- 完整算子/域导数实现检查均通过各自原阈值。

原 LSMR200的 `istop=7`；预条件 normal `0.0005567785769203882`、原正阻尼 gradient L2 `2461.8811589717343`，raw方向 $g^Tz=-1.2195977776012468$、模型下降 `0.6098723715204994`。它是完整 H 后续的原候选输入，最终选用的是凝聚 H 方向，不能据 raw LSMR 停止状态归因最终非线性域失败。

## 4. C 基线与完整外部响应

C 的已组装 binary64 局部行中，有50个 computed-zero row 带负的完整 outside offset。这个说法限定实际浮点局部子问题，未排除除法 underflow，不上升为原实数问题不可行定理。

完整 offset 重构的保存差为 `5.684341886080802e-14`，candidate 全 B 重构差 `6.394884621840902e-14`。C 修正写回前，外部 raw 坐标逐字保留；随后原全向量 radial 可以改变它们。C 在200 sweeps停止，原 projected candidate 的全向量径向系数 `0.0022179262660410267`，原 raw-ray 系数 `9.256132689815404e-5`。同一完整目标下，C 得 `44.11521876754913`、下降 `0.001440708310091185`，作为真实基线保留。

本轮 R270 凝聚身份：

`f4cd3e8d30bb5063000420d48d9d53489947d5774a3d3396dc26fe1994772ce1`。

原完整 $g=A^Tb$ 仍保留，原仿射构造读回误差 L2 `1.973200778272714e-10`，原 $g$ L2 `785806.956372628`。没有用近似计算中心抹掉线性项。左外部468节点、右外部215节点、109个 free core 均按完整方根链消去；3个全局 scalar 控制仍在5073维局部问题中。

一次完整因子化、215个右反向 front、一次完整最终恢复。凝聚用时 `13.936778859000015` 秒，局部 QP `155.886456684` 秒，含 factor/condensation/QP/recovery 的 helper `202.68722154600005` 秒；原报告最大 RSS `3921092 KiB`。512次 local inverse、1543次 local H action 都是真正该模型的保存记账，不是旧 full-H 的1200 action 上限。

唯一完整恢复的原读回：

| 原报告量 | 值 |
|---|---:|
| local mismatch L2 | `2.5724538558479214e-17` |
| local mismatch Linf | `7.741881137904305e-18` |
| 原 H residual L2 | `1.4501088854219254e-9` |
| 原 H relative residual L2 | `1.8454080591250133e-15` |
| exterior gradient L2 | `1.4501087851401163e-9` |
| 同向量 supplied/frozen A、AT差 | 0、0 |

没有强制覆盖恢复向量的局部坐标。`factor_input_identity=null`，其 `74234...` SHA只是 JSON null 身份，不能当成唯一模型ID。九原输入与四因子数组的保存 identity、三次因子字节重核均保留；完整因子仅在内存，`file=null`，没有独立 raw 因子文件审计。

## 5. 512工作行终止的实际含义

literal stop仍是 `maximum-working-row-budget`，工作行确为512，但最后一轮已与51的明显违例不同。

stage511新增 row28531：中点477、angle1907。最后200 dual sweeps的最大 coordinate update为 `6.675590651684963e-16`，归一化 working slack最小 `-5.342948306008566e-16`，归一化 complementarity `4.033565408206712e-17`。

最后未修复点的完整30720行：

- 220个负 slack、6个零；最小 `-1.2256862191861728e-13`；最大相对违例 `2.217215008199189e-12`。
- 最坏相对 row24598：**原中点475、angle22**，$c=0.05528044031154511$；该行已经在512工作集中，不是未加的严重遗漏行。
- local stationarity L2 `1.6281646490085172e-11`，complementarity `1.8175504529001278e-16`。

实际最终局部 feasible segment 参数1，local最终 radial系数1；其全行最小 slack `1.0547118733938987e-15`、无负行，local stationarity `5.027404364691492e-9`。完整恢复后原 B 重读有浮点小违例，原全向量径向系数为 `0.9999999999987809`，最终 segment仍1。最终全30720行最小 slack `1.1379786002407855e-15`、无负行。

真实完整 H 与 C 在**同一个当前模型**比较后选择 H：

| 最终原完整读数 | 值 |
|---|---:|
| 原完整阻尼目标 $f$ | `43.76086286961156` |
| 原完整模型方向导数 | `-0.7019440297794628` |
| 原阻尼模型下降 | `0.3557966062476628` |
| 实际原完整 stationarity L2（含相应非负乘子） | `9.590119450215969e-7` |
| 实际 complementarity | `2.2411733154051266e-14` |
| 多证据点 R267 raw lower 最大值 | `43.76086286961154` |
| 最终 R267 raw gap | `1.4210854715202004e-14` |
| raw distance bound | `6.243977557169486e-10` |

这些后验数值没有外包浮点求值误差，**不是认证下界或精确最优性证明**。尤其不能把极小打印 gap当机器精度的严格证书。但它们已经不支持把最近真实域失败继续归为“大径向损失、working遗漏严重违例或原 H 逆不准”。本轮没有据此改科学门。

## 6. 原17次上限内实际执行的7次试步

所有7次原节点域、原均匀角 $\rho$ 门和边界有限性都通过。下表的失败来自原中点 RHS；在这些 nonfinite trial 上，原引擎尚未计算实际 merit 或两个 RMS 层，因此不能发明失败步的 merit 或 RMS 结果。

| $\alpha$ | 原 nonfinite midpoint 索引 | 已建模真实查询的失败 | 实际结果 |
|---|---|---|---|
| 1 | 473、475、477、480、482 | 多个原左 RMS、四个原中点 | 拒绝 |
| 1/2 | 473、475、477、482、483 | 左 RMS482、四个原中点 | 拒绝 |
| 1/4 | 481、483 | 15个完整角网格全正 | 拒绝 |
| 1/8 | 481 | 15个完整角网格全正 | 拒绝 |
| 1/16 | 481 | 15个完整角网格全正 | 拒绝 |
| 1/32 | 481 | 15个完整角网格全正 | 拒绝 |
| 1/64 | 无 | 15个完整角网格全正 | 两原 RMS 层均通过，接受暖场 |

最近失败 $1/32$：

- 原中点481，$s=1.2267614462385934$，原有限输入产生 nonfinite RHS；
- 原2048角 $\beta^2_{\min}=-0.07069334664841675$，angle948，$\phi=2.9084275738311756$，12个负角；
- 这个中点尚未在十五查询内。已有左 RMS481是不同原查询，不能替代中点481；
- 所有已建模真实角均正，其中左 RMS482最小 `0.001691593979525452`，原中点482最小 `0.3003120554819608`；
- 同步保存的全30720行线性预测 $\beta^2$ 最小 `0.0016810437135996135`，也全正。

较大 $1/4$ 步另有中点483失败。$1$、$1/2$ 时已建模中点也会发生非线性域失败。因此增加481的模型约束只是最近有实据的下一步，并不预言 $\alpha=1$ 可行，也不替代原完整域回溯。

接受 $1/64$ 的原读数：

| 量 | 值 |
|---|---:|
| 固定权重 merit 起点 | `44.11665947585927` |
| 实际 merit 终点 | `44.105521474605546` |
| 实际下降 | `0.01113800125372677` |
| 同方向原模型预测下降 | `0.010933835998186387` |
| 实际/预测比 | `1.018672792931433` |
| 完整物理 col 最大值 | `0.007109981682135472` |
| 完整边界最大值 | `6.1823900322767e-8` |
| 原左边界、常值行 | 0、0 |
| 原两个 RMS 分数各698查询 | 均0失败 |

原输出尚未记录物理 col 最大值的 argmax，不能猜它与481或任一高模重合。新准备的 [只读最大项观察器](2026-11-14-original-collocation-argmax-observer-interface.md) 尚未在本轮运行；不得将其未来输出冒称53结果。

## 7. 实际新暖场与新 FD

暖场保存 `optimization_progress=true`、`accepted_warm_steps=1`，elapsed `562.204670453` 秒，仍为未接受完整 BVP 的优化暖场。

FD 真正读取新 warm SHA `e71a5fec...`、完整实际 producer和原真实 zero-H T112 J 的**明确 affine map**，执行原全部方向、步长、两级 Richardson：

- fourth-order 最大相对误差 `7.165083799852089e-10`；
- second-order 最大相对误差 `9.883378566810663e-6`；
- 原阈值仍 `5e-5`，原 contraction 检查保留；
- `implementation_check_passed=true`；耗时 `23.995504722000078` 秒；
- `current_H_equals_affine_anchor=false`，`nonlinear_native_at_current_H_solved=false`。

这是真实新场的原边界实现检查，不是把旧 FD 的 SHA 重标。没有把 ready 线性图当真 J，没有完成新非零尾或新增完整 BVP 接受。

## 8. 实际字节审计范围

[actual53 前缀原件审计](2026-11-14-actual53-prefix-byte-audit.json)：72362 B，SHA256 `d6c48b991452aa7da64bc4fe3756f23cfd7721ab40eb2dedf96eb989019ea7a4`。

已逐项核：

- 137个 domain NPZ、880个 NPY：压缩文件 SHA、NPY shape/dtype/原 payload 身份；15组完整 B、$\Gamma$、$\Pi$和全部 $\beta$ 由原分块字节顺序重组核 hash。
- 88个凝聚 NPZ、88数组；42个完整数组引用重组为38个不同完整数组，身份全一致。
- 9个原中点 observer 报告、15个 NPZ、45数组；原 NaN/nonfinite 位串保留，原 finite 与 residual unchanged flags全true。
- 44个当前数学/FD source SHA；完整父51 pair、整个父 producer；当前 status identity、实际 warm 和FD完整 producer。
- 父原 JSON 数值重序列化为实际 binary64 后，仅比较 bytes 与保存 B 基点，没有重新计算任何科学数组。

本地工作只读取、解析和散列原产物；没有新的矩阵作用、dot/norm、SVD、RHS、FD、QP或 native 求解。完整 factor raw文件未导出，不能把内存 factor identity 报告冒成独立 raw 因子文件审计。`condensed-root` 的14个 raw输出由root另行审计，不与上述NPZ工作混报。

[actual53 root raw字节审计](2026-11-14-actual53-root-byte-audit.json)：5800 B，SHA256 `731a542e112ca784b259fcaf42ba8fd5cecd99c70baf327a1ff4b003d325e6c4`。root按原 `status.output_arrays` 对全部14个原raw文件、217496448 B逐个核 size/shape/raw SHA，全部一致；包括局部root、完整仿射、原gradient与恢复输出，不是未导出的完整factor文件审计。两份审计均只处理原件字节，不补造科学结果。

## 9. 有实际支持的后继

从本轮真实 warm/status pair 继续，最近失败支持只新增**原 collocation 中点481的全部2048角**，形成16个 typed query。原同次捕获中已含节点481与482，完整B支持469–483及3全局控制仍是5073维，无需增加原J、节点或频率。原512预算、$\lambda=270$、dual/C/LSMR预算、原完整模型/外部恢复、17次试步、全部原域和新FD保持。

该下一配置尚未执行，不能当成已经排除中点483或已解决原非线性域。下一次同时记录原已返回 col 的全范围 argmax及本模型原 row weight，能定位仍约 `.00711` 的另一个实际瓶颈；观察器不调用额外 RHS/J，也不改变数学门。本轮现有证据不支持仅继续提高512工作行来解释最近失败。
