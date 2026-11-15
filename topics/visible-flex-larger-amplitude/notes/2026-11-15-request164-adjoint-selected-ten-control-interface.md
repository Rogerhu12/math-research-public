# Request164：完整离散伴随选择新零 jet 形状，再作独立十坐标真实试探

作者：AI（ChatGPT，amplitude）。日期：2026-11-15。

分类：新独立科学候选的完整源码与 Actions 接口。本文不是已完成运行的结果，也不宣称驻点、响应秩、导数误差证书或非零场。实际 Request164 的结果另记 R364。R350 已明确 actual157 的完整读取范围；这里不再重跑其优化或扩大旧数据运输。

## 1. 本次实际要回答的问题

从 actual157 真实末点的九个 Decimal50 字符串重新构造同一有限字面模型，使用 R351 已发布的完整七状态伴随，评价六个明确的新增 $C^2$ 零二阶 jet 形状。按实际形成的完整三响应选一个形状，再建立有独立 source、schema、控制表和第十坐标 $\xi$ 的新模型。对当前十坐标模型重新形成全部十列 forward 响应，以其真实第十列确定一次下降方向的符号，执行原完整三残差 merit、严格负 slope 和原 20 档 Armijo 试探。

这不是把原九维小步多跑一批。旧九个参数在本次真实方向中保持不变，增加的是独立的新函数系数。也不是仅计算一个伴随分数就声称取得改进：完整新 primal、当前 ten-forward、全部真实试探和原最终消费者都在本次 Actions 内执行。

有限六候选的结果只涉及这个明确 catalogue。全六分数为零、选中方向无严格负 slope、或原 20 档全拒，均不推出所有允许零 jet 控制无下降方向，更不推出九维或连续问题的驻点、秩亏或不可解。

## 2. 真实父来源；不恢复已删除的科学 raw

父为 actual157：

- run 43729310294，source commit c71cbeac7fd13c65cf50c7eb39842e9949737b25；
- 原 producer 为 geometry_20261115_small_core_nine_control_decimal_residual_quadratic_recipe.py，SHA256 54167dff0ce67e9f8fe0fa5d2899c35f0f99534077f2530d90b296eee7537100；
- 原 status 51,842,612 B / 931b013b6cfaba4215065e0734c129ba2089662273427f7ebecc5df4f35ee2b0；
- 原 bounded summary 89,063 B / 7411fd01db054215e5d22293f6a4c239aa482302bf75b4da123f35d500d0cad2；
- 原 chain 29,684 B / 9d8bf161d9b88c0c411d326b1717fd2d32332a49534041ebd495b673a35652bd；
- 参数取原 final.parameters 的九个完整十进制字符串；父 final_relative_trust_radius 为 0.0000390625，仅作来源记录。

这九个旧数值输入和完整 literal binding 已写入 7,483 B 的新 recipe。它们不是重新求得的精确实根，也不是高于原 Decimal50 的有效位承诺。原 status / J / Hessian / merit / FD / 中间 state 不被恢复或冒作当前场。

原四输入从公开历史 commit 8bd267107cc8710d371f3b62c02986655ac965b0 逐 size/SHA 恢复到 RUNNER_TEMP：

| 输入 | 原字节数 | SHA256 |
| --- | ---: | --- |
| accepted | 2614352 | b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff |
| prepared | 4220043 | 0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714 |
| tail_anchor | 6815 | e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51 |
| tail_config | 2161 | 01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5 |

输入相对路径完整保留于 request.inputs；恢复不把数据重新提交 main。另按原 exact_20261114_public_resume.prepare_public_source 恢复 original78 源到独占临时 cache。所有 source pins 在执行前逐字核对。

旧模型 fresh evaluate / first forward 必须重新形成 actual157 的完整 literal binding cc10a080eafa19e282ca22cefa62af57dadaf0ab19e54b0a4e6f7e7188ec32d3。这个比较是有限模型/输入身份合同，不是响应精度或额外秩验收门。旧 second-variation module 在这里用于保留原 binding/source 能力声明；本次不调用旧 Hessian 或 polynomial search。

## 3. 六个新形状与独立十坐标族

对原三支撑 $i=0,1,2$，按 support-major 顺序，每支撑取 $k=3,4$：

$$
h_{i,k}(s)=w_i^2\,64x^3(1-x)^3(2x-1)^k,\qquad
x=\frac{s-\ell_i}{w_i},\quad 0<x<1,
$$

在支撑外为零。$w_i$ 是原 source 中记录的 width；准确实表达的右端是 $\ell_i+w_i$。原 recorded right 单列为 metadata，不偷换两种字面端点。

因公共因子在两端有三阶零点，新增项本身具有准确实意义下的零 $0,1,2$ jet。这里仅断言这个新增多项式项的拼接性质；不借此证明原有限 Gauss / independently returned ap 表满足连续导数恒等式，也不替原 scalar 家族补付全局 $C^2$ 证书。函数形式独立同样不证明完整响应增加秩。

新参数顺序明确为：

~~~text
[p1,p2,p3,theta1,theta2,theta3,eta1,eta2,eta3,xi]
~~~

每个候选有自己的 support / power / source / definition 和 sampled-table identity。被选中后，真实 scalar 为原九族再加 $\xi h_{i,k}$；$\xi$ 从字符串 0 起步。old-nine helpers 从未接收 ten-vector。

独立 schema：

- family：R259-nine-plus-selected-power-C2-ten-control-circle-family-v1；
- scalar：complete-old-nine-plus-selected-power-C2-scalar-v1；
- declared expression：complete-selected-power-ten-control-real-expression-v1；
- persistent model：ten-control-selected-power-persistent-decimal50-literal-circle-model-v1。

source-bound view 只替换原 affine scalar 的额外第十项和维数合同。原 699 nodes / 698 cells、半径递推、完整三模 $2\times2$ 传递、原 real-domain guards、全部 112 行终端责任不变。对新 literal model，所有非 shape 输入数组与原模型逐 raw SHA 相同；新 controls 前九列也必须与原表逐字相同，第十列是实际新 family 的 binary64 node/mid 采样，再作准确 Decimal.from_float 提升。

因此新 primal 是 Decimal50 对明确 binary64 字面系数的持久评价；不是把控制表、mesh、J 或连续 ODE 重新精确构造。它不是区间导数，也不是离散舍入映射的数学导数。

## 4. 伴随、候选选择和真实符号必须分开

当前原九点重新评价后，R351 helper 完整形成：

- 698 个七状态 / 十局部输入的真实有限链线性化；
- 全部反向递推、原 start 项和直接 terminal / profile / ratio 项；
- 原全部 112 终端字面 J 与原三残差选择；
- 原九列伴随与已经计算的同点完整九列 forward 对照；
- 六个新 shape 的三响应与完整 112 行局部 forward 响应。

这些对照不重新调用原九参数 FD，也不把局部形成顺序与原全程 forward 冒作逐字相等。actual differences、word mismatches、源身份与 coverage 均保留；它们不是额外阻塞 gate。

候选分数的源定义是

$$
\mathrm{score}(h)=
\frac{|F^\mathsf T v_h|}{\max(1,\|v_h\|_2)}.
$$

只在完整返回的有限分数里取最大，完全相等时取最先 catalogue index。零分数仍可入选；不会因形成的伴随梯度为零，就在原十坐标 primal/forward 之前断言没有候选。

选中后，fresh ten-model 的全部十列 forward 再给出当前第十列 $v_\xi$。真实方向只有第十分量非零：

$$
d_\xi=-0.01\,\operatorname{sign}(F^\mathsf T v_\xi),\qquad d_0=\cdots=d_8=0.
$$

0.01 是本次新独立实验的显式 Decimal 字符串幅度。父 radius 只记录，不伪称继承，也不把新 $\xi$ 当旧 scaled coordinate。实际原 full3 slope 再由当前三响应形成；非有限或不严格负时如实保留原因，不生成伪接受点。

score 使用的伴随响应、同局部线性化 forward 和当前 ten-forward 是三个有独立形成来源的读数。选择分数不等于导数误差证书。最终真实方向以 fresh ten-forward 的符号为准，不用旧 score 的符号代替。

## 5. 真实原线搜索与最终责任

本次只执行一次新形状方向。原 20 档 $\alpha=2^{-j}$，$j=0,\ldots,19$，对同一独立十坐标模型重新评价；所有旧九分量保持原持久字符串数值。每档保参数、完整三残差、原 full112 residual、实际 merit、scalar / circle 最小值、真实 domain exception 和原因。

原接受式保持：

$$
W(p+\alpha d)\le W(p)+c_A\alpha\,F(p)^\mathsf T J(p)d,
\qquad W=\tfrac12\sum_{a=1}^3 F_a^2.
$$

$c_A$ 是原 binary64 0.2 的准确提升，即 $3602879701896397/18014398509481984$，不是数学 $1/5$。严格负 slope 与原有限算术 Armijo 原样执行，不额外添加 rank、响应对照阈值、inner-target 或“至少下降多少”的新门。有限舍入可能使微小 Armijo 右端与起点相同；报告只给原实际词，不据 accepted 标记伪造准确实下降。

本次没有 normal 曲线，也不把旧 normal 轨迹改名。新增系数、完整状态和所有试探由新 source 自己产生。若全 20 档拒绝，保留新族初点；若一个接受，则保留该实际 ten-state；未访问后缀明确记录。

初末责任：

1. Decimal50 全十列当前 forward 和三个原步长的中央 FD，初末各 30 列检查。
2. 明确投影为 binary64 的全十列原 complex response 与三个原步长 FD，初末各 30 列检查。
3. 新 scalar 族的 fresh Arb 160 bits / depth 14 全区间 a 与原独立返回 ap 检查。
4. 固定三个 odd、三个 quadratic 和一个新 shape 系数，保原三 active 控制、112 tail/field 和原 453 方阵物理 circle 消费者，完整原 node/mid/RMS/FFT 责任不减。
5. 原 Decimal unit/full112 停止 flags 与 binary64 投影对应 flags 各自记录。

合计 120 个原 FD 列检查，12 个原 level；FD 数值不作为新接受门。全部 projected scalar / circle 消费者只证明/记录其实际 projected 点的对应范围，不能反标持久 Decimal 点。任何投影值均不回写 Decimal owner。

原 112 固定零 anchor J 继续完整消费，但这不是新 g 的当前 nonlinear native 解，不付新 tail Schur，不付真实 nonlinear fullDN/finalJ/audit。因此 native_nonlinear_solver_called、nonzero_field_completed 和 success 均保持 false。低三候选接受不能冒成原问题最终完成。

## 6. 运行入口与闭包

当前 producer schema 为 R259-adjoint-selected-ten-control-one-real-full3-direction-v1，status 为 adjoint-selected-ten-control-status.json。原 actual157 current closure 41 件原样保留，再加入 family、model、R351 helper、当前 producer，形成真实 consumed closure 45 件。

完整 request 源表保留原 107 件，加四件当前 consumed 源及新 metadata wrapper，合计 112。support 保留原 9 件，再加当前 reader，合计 10。历史 reader/optimizer 作为明确 ancestry/hash baseline，不被误执行。当前 wrapper 不导入任何科学模块。

唯一 push trigger 为本题 computations/public-adjoint-selected-ten-control-request.json。新 workflow 与所有原请求独立，不改旧 157 或 167 文件。

实际科学 CLI 在本仓 Actions 内由 wrapper 形成：

~~~text
python -u geometry_20261115_adjoint_selected_ten_control_recipe.py
  --accepted <已核原accepted临时文件>
  --prepared <已核原prepared临时文件>
  --tail-anchor <已核原tail-anchor临时文件>
  --tail-config <已核原T112-config临时文件>
  --parameter-recipe <本次7483B源码recipe>
  --parameter-recipe-sha256 76a93aa076d0a55781fdb3228a895b25583591b269fa5a866ea8068392946820
  --out <RUNNER_TEMP下独占science目录>
  --backtracks 20 --decimal-digits 50
  --interval-bits 160 --interval-depth 14 --wall-seconds 2400
~~~

runtime 沿原 Python 3.12.14、numpy 2.3.5、scipy 1.17.0、python-flint 0.9.0；BLAS / OMP / MKL 单线程。Decimal 为标准库，50 digits / ROUND_HALF_EVEN。

## 7. 资源边界、规则同步与退出语义

资源和数学预算分列：

| 层 | 明确限制与责任 |
| --- | --- |
| producer | status 建立后的 2400 s deadline；逐候选、真实 trial、helper cells 检查；原信号 handler 写 partial |
| whole child | 从启动含 imports/setup 起 2400 s；为长 FD block 提供明确外部 wall boundary |
| termination | SIGTERM 后 90 s 原 checkpoint 宽限，仍未退出才 kill |
| reader | 300 s metadata-only；另 30 s 退出宽限 |
| Actions science step | 50 min |
| compute job | 65 min；独立 report job 10 min |

whole-child 时间包括前置 source/输入绑定，故可能早于 producer 自身 checkpoint clock；两者都明示在 request.resource_contract。没有把等待当成 Armijo 拒绝，也不把 budget partial 当六候选不能下降。

原 rules runner 3b8b6dd5... 的 initialize / 2700 s 真 pull-rebase / 规则差异停止逻辑未改。只以实际 checkout 中已读 README 全文更新内存 BASELINES。当前根/题 blobs 为 21bd547f... / bff8aea2...。HANDOFF 保原唯一规则同步记录与原大小限制；setup 继续 merge.stat=false，避免历史 raw 删除造成 diffstat 读负担。

wrapper 不建立脱离原 runner 的新 process group；科学子进程剥离 Git/Actions token 环境变量。数学代码仍只在公共 Actions 执行。

“catalogue 完成但没有完整有限候选”“没有严格负方向”“全部真实档拒绝”“真实 accepted 后 final 检查完成”“资源 partial”“工程 exception”“readback incomplete”各有独立原字段。不以 workflow/report success 自动推出 science/native success。完整输出目录也不被当成 accepted field。

## 8. 一份紧凑读回，而不是大型 raw 重建协议

reader 只导入标准库，读取完整当前 status，执行原 JSON、shape/coverage 和 byte identity 操作；不重新求数值响应、norm、FD、优化或区间。

单份 hard bound 为 90,000 ASCII JSON bytes。预定保留：

- 六候选各实际完整三响应、局部 forward 对照、分数/梯度、实际 shape 定义、全 112 响应身份；
- 原九列伴随/已形成 forward 的必要 $3\times9$ 矩阵与真实差值；
- 原 adjoint coverage、终端/初值贡献、所有已记录 mismatch indices、未访问 cell 后缀；
- 初末 Decimal 与 projected binary64 的完整 $3\times10$ 响应；原已有条件数/奇异值只按原词读；
- 全 12 FD level 的原 maximum/flags、120 列索引覆盖、全部真实 exceptions/failures；
- 全部最多 20 个真实 trial 的原值、理由和未访问范围；
- 原最终 flags、实际 Arb scalar 字段、实际 circle node/mid/RMS domain 字段与 square/frozen-seven 身份；
- 原 status、source closure、recipe/input、event ledger、所有未传输表的准确身份。

不传全 FD 扰动表、698 local matrices / adjoint arrays、每候选 112 响应全表、全部 FFT 大表。它们在 Actions 中按实际源码形成并被 metadata reader 读取/取身份，但 root 并未因此逐值核过。完整 status 读取不等于全原事件 ledger 独立复算；ledger 的生产者 byte receipt与来源明确保留。

required key/shape 检查只定义“当前读回 complete”含义，不改变科学接受。部分 status 按实际已到阶段处理；若 source/schema 错、字段缺失或摘要超限，打印具体 metadata error/section byte counts 和原 status 身份，诚实标记未完整运输。不会把大表编码、压词典或切片搬进工具，也不会清掉已取得数值再宣称 success。

独立 report job 只接一个 compact_summary 和 bytes/SHA，验证原 compute-to-report 字节身份，再打印 BEGIN_VISIBLE164_COMPACT_SUMMARY / END_VISIBLE164_COMPACT_SUMMARY。ASCII 90 KB 对应的 UTF-16 输出大小也远小于 Actions job output 限制。

工程 stdout/stderr 在清理前单独保留原文与字节身份；可能按小原错误文本记录输出，范围仅工程错误日志，不借此运输科学大阵。reader failure 不会遮去 producer 在 status 建立前的真实 traceback。

## 9. 临时生命周期与既有规则 15

所有原输入、original78 cache、scientific status、projection calls、完整 event ledger、区间 leaf 和 circle 临时文件只在本 request 独占 RUNNER_TEMP 下。

顺序固定：

~~~text
恢复并核原输入/source
→ 原规则 runner 内执行真实科学 child
→ 完整 status 的紧凑只读结论
→ always recovery/report（不重跑 science）
→ 原工程 stdout/stderr
→ 仅属主匹配、无跟随 symlink 的 request-owned cleanup
~~~

清理不跨 repo checkout，不上传 raw artifact，不写 Release，不提交可重算 raw。Git 历史输入对象只落 ephemeral runner 对象缓存。预算、规则变化或工程中断时能保多少 status/原文就如实读多少；未执行的 final consumer 不填造数值。

## 10. 冻结八件与发布路径

除 .github/workflows 一项外，下表路径相对 topics/visible-flex-larger-amplitude/。每份均小于 100 KB；这里只保源码/参数/接口对象，未改变任何 ref。

| 文件 | B | SHA256 | Git blob |
| --- | ---: | --- | --- |
| computations/geometry_20261115_adjoint_selected_ten_control_family.py | 18392 | 09240b33b82be3f595e82df05d93b309baefd6eeb74f1c34ba3a095cb2548016 | 8f567085c2ffa94718c0095b3da57d2f14ba5980 |
| computations/geometry_20261115_adjoint_selected_ten_decimal_model.py | 10479 | 8cb8352b76be0770ab565de3b24907faa302a86a75660b9f5ffaa9a23cc6a9b7 | 9dbe4849f8b01b8c89790e4e903e8432c7593a40 |
| computations/geometry_20261115_adjoint_selected_ten_control_recipe.py | 35469 | 9da7ebacbf40ff65733d518169c028a82f9060770c62ab89562b29f87793a782 | c98e69d4d1c124faeede187e44ebe9122281b9e8 |
| computations/root_20261115_adjoint_selected_ten_control_scalar_readout.py | 28130 | fd01706a6f2c7aa8559ebfdce11a94a60e9c1382648c7c6b152e0dbff85f6fe2 | 597c6a071739fac88195c96c2ea932dff8fd830d |
| computations/geometry_20261115_adjoint_selected_ten_control_temporary.py | 19031 | 573d323a6a22be4735e08d8eb9a956eb844b46f7f7408b6323941eefe878cff5 | f4cc69a953508cd62c2bcead3f2e44b0891d5f1d |
| computations/adjoint-selected-ten-control-actual157-parameters.json | 7483 | 76a93aa076d0a55781fdb3228a895b25583591b269fa5a866ea8068392946820 | c7e101c1fecca01b4a91d81aef3d688a79c57601 |
| computations/public-adjoint-selected-ten-control-request.json | 40956 | 9c9d27d1c52caaed9f863dad12a5e5db38a3d26e749e7133dc562d469f6e3d5f | 04fc84123973a3a93b7b938a0d9eef9655010333 |
| .github/workflows/visible-larger-public-adjoint-selected-ten-control.yml | 20752 | 4bf554950117ac67b4a9abfae90b1a9fe7a035cdecc0f8138ddb7df406a71abb | 276f85e795baba01a7d2b84bde924b4bc2ba0e11 |

R351 helper 仍为已发布的 35,419 B / 12a95d40929cc7799761e56c33eadc9e5fbe16fa3eacf0d0be94c56ea3452b0f，不修改。

完整文本差异可由下列固定基线重建：

- family 相对冻结 086572f9 的九族，新增独立 class / shape / 维数 view，原源不动；
- Decimal model 相对冻结 2422be0c，原有限链 body 通过准确 source-bound view 引用，仅额外 affine 项和维数；
- producer / reader / wrapper / recipe / request 相对 actual157 同名角色；
- workflow 的基线已从 c71cbeac7fd13c65cf50c7eb39842e9949737b25 实取，22,302 B / 905e137e0d4724f9aa2a7d60aadb265e1643e73afa543a17ff4527aa883aceaf，不使用未发布旧草稿身份。

当前 source-level 工作只包括原文读取、明确替换/JSON合同核对、完整差异与 SHA。终端不可用期间未声称本地 AST/编译或运行；未 import 科学模块、未执行任何 fixture/科学数值。工作流执行前的 AST 检查属于公开 Actions 中的 source 工程检查，不增加数学门。

本接口没有未来 run ID、未来 selected shape、未来 accepted 参数或未来 FD 数值。实际完成后依据原 compact conclusion 写 R364，再据真实新增响应/真实 line-search 结果决定后继。
