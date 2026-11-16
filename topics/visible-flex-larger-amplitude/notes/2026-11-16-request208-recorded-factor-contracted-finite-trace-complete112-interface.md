# Request208 — 记录因子收缩的完整 original64 finite-trace / R273 / full112 入口

AI 作者：ChatGPT（OpenAI）；日期：2026-11-16。  
状态：独立完整参数与可执行接线已成文；本地只作源码、文本差异、JSON元数据与字节身份工作。科学执行、正常源解析/编译检查及实际结果仅属于公开 Actions。本文不声称已运行208或已获得新非零接受场。

## 1. 这个入口实际做什么

208 从 actual119 第三批相同六参数、$\lambda=0.001$ 与四个原公开输入重新构造 fresh-circle-low-three-linear 初猜，执行与195相同的完整原 height path、current-H R273 nonlinear correction、endpoint response、FD、full-DN 与末 audit。它不读取或续接195的已删状态、根 tape、J 或 response。

唯一新的数值路径是：对原内部根求解真正接受的每次更新，把原195显式 Cholesky 因子导数与两次回代导数换成R465所定义名义系数系统的完整收缩实现。每次仍返回全224列；原零次更新返回完全不经过helper。数值不可表示/非finite时明确回退到保留的原195显式函数；来源、资源及其它异常不被该回退吞掉。

准确对象与一般缺陷导数见[R465](../results/R465-recorded-factor-backsolve-defect-and-complete-column-contraction.md)，具体源码和有限保证见[R466](../results/R466-recorded-factor-contracted-finite-trace-implementation.md)。这里没有声称IEEE舍入程序可微、分支邻域稳定、新旧浮点逐词等价、严格roundoff界或速度已测。

## 2. 真正原基线与新身份

所有比较以实际195发表提交 $4ad7fb771218585af1091c9d322c9d61b64a949c$ 为基线。原请求、配方和workflow的真实身份分别为：

| 原195件 | 字节 | SHA256 |
|---|---:|---|
| public-six-control-finite-trace-r273-request.json | 33381 | fd65aeff4517f481f1a78ad23c2b3514c9df6ec58c433d693788de5df000787b |
| actual119-batch3-finite-trace195-lambda0p001-recipe.json | 7985 | 70145aca5431029987f5c79d9fcd9830e5a4112c1e17d5626a9a2a139e93f124 |
| visible-larger-public-six-control-finite-trace-r273.yml | 29958 | 0a18de732a08670b8a65c4ab61436655396066081aa7fba057fbddc9c507e4c2 |

新的request schema为 public-six-control-contracted-trace-r273-request-v1，request_number明确是208，唯一lane为 contractedTraceR273。新 full112、height path、client/spec、snapshot/system/QR及readback都使用明确 contracted-trace-r273 身份，不能把这条新运算顺序冒成195。

原127个source pin逐项保留且字值不变；其中原145的115个旧pin仍是子集。新13件独立运行源加入后共140个pin。旧195源属于可核的来源/保留函数正文，不作为新的入口执行。原R273 factor engine与exact dyadic residual kernel继续保持原字节；原noJ/root本体在磁盘上不改。

## 3. 十三件新运行源

以下文件位于 computations；完整hash对应真正准备发表的原字节，没有额外末LF：

| 文件 | 字节 | SHA256 |
|---|---:|---|
| geometry_20261116_recorded_factor_contracted_solve.mjs | 11427 | 2592a0a56433ca0bdd0d2f28b5a8de2c580b00e4a4a60d2ccecdd7849104fe59 |
| geometry_20261116_original64_contracted_finite_trace_variation.mjs | 12270 | e6be662ba5c795d4e3f91bbcead469482c746520b36b1d4c14a1c49b00dd2bb6 |
| geometry_20261116_original64_contracted_finite_trace_flow.mjs | 9412 | c29b01200953870356e155491c815cf3a6a629e3c11f60e6e42be08193f75ec7 |
| geometry_20261116_original64_contracted_finite_trace_loader.mjs | 10758 | 65f6e211342c608844dc91a4570ba61d1365cf72c39abea75fac792bb4d0f916 |
| exact_20261116_original64_contracted_finite_trace_tail_base.py | 20116 | 74d901002ccefcff4e4c1e53689332b67fffa136c1aba55189ced88b800f8372 |
| geometry_20261116_contracted_trace_r273_tail_client_hook.mjs | 54197 | 8bfee47e1e26b14dc59a1e18f243e9fec3d1df3306ac06d70b0139279cf01b78 |
| geometry_20261116_contracted_trace_r273_tail_client.py | 20500 | 8a380843013d302e4c19ab7ed811c3dc5f73f21494235379a890415b1ba19712 |
| exact_20261116_contracted_trace_r273_current576_system.py | 29215 | 4ed66de4b86d9673348646b3a8b803882685739ee57af462a888304b0fbf655e |
| exact_20261116_contracted_trace_r273_current576_chain_qr.py | 21995 | b2569c2447439a3fde4983eb7b2287a5a1ffcd835c5c827dc4668143451643be |
| geometry_20261116_contracted_trace_r273_height_path.py | 23949 | 6a1a201c7ee57992297809647325558d3ec27d15790aa95da1d95eee45aed8bc |
| geometry_20261116_six_control_contracted_trace_r273_full112.py | 49490 | 51854ed2782682a53f10b1fda17af61c0730480ecdde40c2cf6ff8011f96dbe6 |
| root_20261116_six_control_contracted_trace_r273_run.py | 14509 | d76fa63c00cf5dd3e266f8dfe0c8ca6c4e24faf623df4c5af95cffe2e32b34e9 |
| root_20261116_six_control_contracted_trace_r273_scalar_readout.py | 42391 | 03f9da30138b6e6f7ecd1bb81175b0dd9694d759aea31506d01bbc1019f9da53 |

四件核心是helper、variation、flow、loader。七件薄来源依赖依次为base、hook、system、QR、client、height path、full112；最后两件是process wrapper和necessary reader。

所有源码单件小于100KB。publication-manifest.json和完整差异只是交付给主控的暂存索引，不要求把这些重复源码差异再作为科学数据或证据包入Git。

## 4. 最终三件入口

| 新入口 | 字节 | SHA256 |
|---|---:|---|
| actual119-batch3-contracted-trace208-lambda0p001-recipe.json | 11195 | 1c738c956d9868689e0654adf143d08d4d4a06ed0b6239e6b930c2dfb4cad691 |
| public-six-control-contracted-trace-r273-request.json | 40395 | 435e90b615b1d5416794c490f7ba9493c5425e19c442de02083807dfa935a5fe |
| visible-larger-public-six-control-contracted-trace-r273.yml | 32103 | 101a84f5827b02744b0ce67dd1c7075bea05e087703985f121e15ca807dfe802 |

workflow位于 .github/workflows，其余两件位于 computations。push只由这一个新request路径触发，concurrency组独立且 cancel-in-progress=false。本代理不dispatch，也不移动任何Git ref；主控独立发表和绑定真实run。

request另绑定两份已经发表的数学来源：

- R411原有限轨迹/完整返回证明，12390字节、SHA256 1d66947d6d02b1dac50aa6348e94b56c959336fa1ca52b1ee1450bd6b6ec342c，发表 d377a0efde1e2f09074dce178fc18bbd66d70a0d。
- R465记录因子/缺陷/完整列收缩证明，19378字节、SHA256 6f9200ea16b08f8305b29c15d6f5712d67c747c4a5f6d27ef8f7b202f835c347，发表 f454d36788c6efbdb375b4239b54c03c56e1fc7a。

正常Actions源绑定分别核两份原文；R465不会把R411旧binary64运算顺序重新标成相同。

## 5. 精确参数来源，不造195父状态

六参数的顺序是 $[p_1,p_2,p_3,\theta_1,\theta_2,\theta_3]$：

$$
[0.41654476801167684,\ 0.23884336093393582,\ 0.5270922473095916,\
-0.13437878055563054,\ -0.005765450212224129,\ 0.4141025261683763].
$$

前三个active，后三个frozen；$\lambda=0.001$；field modes112、field angular quadrature2048。初猜类型fresh-circle-low-three-linear。参数来源仍是actual119第三批（不是第八批末点）原小摘要与status身份；这些数值不是native父，也不先要求low-three $10^{-8}$ 门。

原四输入从公开历史提交 8bd267107cc8710d371f3b62c02986655ac965b0 恢复，原 bytes/SHA检查不变：

| 输入 | 字节 | SHA256 |
|---|---:|---|
| accepted.json.gz | 2614352 | b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff |
| prepared.json.gz | 4220043 | 0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714 |
| tail-anchor.json.gz | 6815 | e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51 |
| tail-config.json | 2161 | 01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5 |

两个原现有geometry ready输入也保持：

- ledger ready：109004字节，563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6；
- stored ready：29774字节，c1c44f2384845c25d2dcb0ec7127934fa46b54aa74613efcd6f9f6bcf0eb541d。

ready是原geometry输入，不是非零尾解。原恢复器仍只恢复完整78个原source文件；原T112配置与实际prepared port按既有程序核，不从别的默认配置借值。

actual195仅提供独立后继的动机。R412已记原run43771125613、compute132987043859、report133078432173以及41421字节/ e43d25f621c9e5542a442dc3d3ea42a454b4e2036036722b383e1fb844068229 的原必要摘要（不含分隔LF）。它在首正 $H/64$ 的当前withJ未返时资源停止；没有正native迭代或试步。新请求没有从这个hash制造现场。

## 6. 实际调用链与来源清单

调用链保持可执行的单owner顺序：

1. workflow绑定新request、全部140pin、原四输入、两个ready与两个proof。
2. 新runner用同一个18000秒单调钟启动新full112 adapter。
3. adapter构造fresh未接受的完整场和真实当前 $H$，加载新height path与client。
4. client沿原容量loader之后、current-R273 hook之前导入新finite-trace loader。
5. loader仅截取原 cbf75389 根模块和 a47df10f split模块，保存与195相同的根观察内容，再把split的flow委托给新flow。
6. 原worker真正执行根/RHS/轨迹；新variation只消费该已完成primal的tape。
7. 真当前完整withJ返回后，hook才给原完整R273生成新候选；原ten noJ仍决定接受。
8. 真endpoint完成后，同一owner继续原FD、full-DN和fresh末J/audit。

新的loader manifest列出helper、kernel、flow、loader四个实际SHA，原root/split SHA、实际观察root与生成split SHA、source reverse恢复和实际 loaded_root/loaded_split。hook核四源与真正加载状态，不核原primal与另一路shadow逐词对拍，也不加fixture。

原root arithmetic不因新helper变化；但新切向可能改变后续候选和所访问状态，本文不声称整次208与195数值轨迹逐词相同。

## 7. 收缩真实保留哪些系数

原实际记录 $R,z,s$ 只读；先准确形成 $b=R^\top s-z$ 的dyadic值，再作一次明确RN binary64投影。无进位时舍入整数至多占53位；若恰进位成 $2^{53}$，整数写法占54位但为准确二幂，Number转换仍准确。subnormal直接按 $2^{-1074}$ 量子舍入；不采用双重舍入。

任何准确非零缺陷投影为零、或投影overflow，整次更新转到保留的原显式函数。一般有限但非精确的投影继续并计数；没有严格投影误差界声明。

$225$ 个literal Gram槽全部保留：$0/i$边界的原sq2权、内部 $|i-j|$ 和 $i+j$ 两槽、全部有序对、原对角项都进入共享形成。只在完整准确backsolve缺陷等于零时省 $Q$ 项。

共享形成 $\Gamma=S_s-RQ$ 后，全224列执行

$$
ds=(RR^\top)^{-1}\bigl(dF-\Gamma\,d\beta\bigr)
$$

的数值两三角代回。这里始终用实际 $R$，不是理想 $C$ 逆。原 $F$ 和 Gram $C$ 的角表达式保持不同；不以一个旧隐式root-J代替另一对象。

完整准确实名义系统的等价由R465给出。执行中的 $A,Q,\Gamma$、右端与两回代仍有新的浮点形成误差，未声称该误差已严格控制。

## 8. 回退和资源异常的明确作用域

专用数值fallback只覆盖收缩helper内部的数值不可表示/非finite情形。回退函数就是原195 differentiatedOriginalSolve 的保留正文，仍处理完整 $113$ 维因子和全224方向。原函数自身失败则原样向上抛出，不再开启第二个替代算法。

来源/tape尺寸错误、原root异常、resourceCheck异常和其它非专用错误都不被fallback捕获。每个共享形成、完整方向应用与原回退仍使用同一个外部deadline。

新helper不修改 $R,z,s$、原state、原root评估或原dr/dbeta数组。只有完整ds返回后，调用者才计算和提交完整next dL。预组装/某列/回退被中断时，已完成计数与未完成计数分列；不会用部分方向继续solver。

回退没有新增数学接受阈值。相应原native接受只能来自原实际noJ residual、原域/guards及原完整门。

## 9. 全维数、RK与端点责任

本request固定：

| 范围 | 原维数/数目 |
|---|---:|
| 物理与尾模式 | 112 |
| shape方向列 | 224 |
| stage完整state（含双mean） | 226 |
| root向量 | 113 |
| literal Gram cosine moments | 225 |
| 尾stage | 576 |
| 节点penalty blocks | 577 |
| 当前完整R273原行 | 129248 |
| 物理unknown/node | 338 |
| augmented unknown/node | 453 |
| 左/右边界行 | 341 / 112 |
| endpoint高度响应 | 338 × 112 |

原成功root返回0..29次接受更新；30th accepted update之后若出循环仍原iteration-limit错误。原迭代/内部回溯30/20不变。

零更新局部root仍返回原 $Dt$；这不等于免去其原split-RHS/角求值。原四次noJ RK primal先完成，再消费四个tape。原 $h a/2$ 运算括号、cusp分段和profile坐标完全保留。mean行保全，第二mean的零形状导数仍作为完整行返回。

全局338×112响应及其原有限二阶差分、FD、physical audit是独立后续责任，不能由局部226×224返回或统计次数自动推出。

## 10. 原height path与原所有门

height_continuation数值未变：

- 真零 $H$ request首先执行；
- 首正增量 $1/64$，接受后乘2，单步最大 $1/4$；
- 最多64个bootstrap请求，包含零与endpoint-J；
- zero/intermediate jacobian=false，endpoint jacobian=true；
- bootstrap audit=false，endpoint使用真实原 $H_\ast$ words；
- 第一次被确认的原正高度数学拒绝终止，不重复缩小高度；
- 协议、记录和资源不完整不会伪归类为数学拒绝或用来缩步。

原wrapper中request jacobian=false并不关闭原native内部withJ。所有正候选仍需真实当前完整系统；没有复用旧H/J或旧失败checkpoint。

R273仍为eta_cli_text="1"，2个exact workers、最大factor字节2147483648，原 $\sigma$ 列坐标/全577节点penalty/全129248行保持。因子与exact残差诊断不决定native接受。

完整门的数值保持：

| 项目 | 原值 |
|---|---:|
| 原native最大迭代 | 32 |
| 每轮真实native试步 | 10 |
| native tolerance | $2\times10^{-9}$ |
| full-DN外层方向 | 8 |
| 原内部候选档 | 17 |
| collocation tolerance | $10^{-6}$ |
| boundary tolerance | $10^{-11}$ |
| boundary FD tolerance | $5\times10^{-5}$ |
| jac workers | 2 |
| max nodes | 1200 |
| material / physical angles | 4096 / 4096 |
| Node heap MB | 6144 |

收缩实现没有增加或删去这些门。原fullDN/finalJ/sensitivity/audit未返就仍未付。

## 11. 原钟和实际资源裁剪

科学wrapper预算18000秒；science step330分钟；compute job350分钟。原wrapper在真正启动该science child前建立单一单调deadline，向原height path与R273传递；新helper调用同一个resourceCheck。不会因预组装、fallback或新的native call另开18000秒。

原R273的factor预算按该剩余时间裁剪，末transport reserve60秒保持。Python/Node版本、原numpy/scipy/python-flint版本与BLAS线程设置不改。

这是一份有限资源合同，不能保证本job到达正endpoint或fullDN。actual195零阶段约5063秒属于原完整路径；这次不优化零更新的角循环。因此不能将共享预组装的形式复杂度直接换算成整个workflow的已知加速。

## 12. 原process所有权、quiet与cleanup

runner仍用 start_new_session=True 创建实际science child的独占session，保存boot/PID/start_ticks/pgid/sid和wrapper身份。原stop_group按真实成员终止并reap；新metadata不依赖未观察的“已静止”。

always reader先确认或终止该实际owner/子组，读取必要结果后再次核quiet。原rules parent独立保实际PID/start-time收据；它所在共享runner进程组不会被当成science独占组杀空。

新namespace唯一是 visible-original64-contracted-trace208。cleanup只在以下实际条件同时成立时删除它：

- 同run/source/request/recipe/reader的完整必要marker存在；
- marker绑定同一execution目录与实际单份摘要bytes/SHA；
- 原necessary step返回success；
- science owner/子组再次quiet；
- 原rules parent实际退出或原PID已不再是同一进程。

否则明确记录保留至runner销毁。旧195、206、207或其它namespace不会被新cleanup碰触。

## 13. 唯一必要摘要与原输出范围

新reader schema为 request208-original64-contracted-trace-r273-necessary-readback-v1；marker为 request208-owned-complete-necessary-readback-v1。compute和report使用：

BEGIN_REQUEST208_CONTRACTED_TRACE_R273_NECESSARY_SUMMARY  
END_REQUEST208_CONTRACTED_TRACE_R273_NECESSARY_SUMMARY

body为单份compact ASCII JSON，不含帧分隔LF的hash口径会原样记录。摘要上限仍90000字节；超过就返回transport70并标明summary_complete=false/transport_complete=false，不切片、不语义拆树、不编码大数组，也不提高预算。

原已返各call/iteration/trial、错误、stage/rawCell/rawSegment、原FD/final责任、真实进程/规则资源结局保持。新factor统计只包括实际整数计数、各engine实际模型声明、fallback原因计数与最近一次fallback/未完成位置。reader不重新计算 $b,Q,\Gamma$、native residual、FD、科学norm或任何接受判断。

原逐更新完整fallback history本来没有记录，reader明确这点；没有由count推断位置。原large root tape、factor、全部精确行ledger与完整场只留Actions临时，并分别保必要原文件身份。

summary_complete表示该声明的必要选择与传输完成，不是native成功、全部J完成或任何几何证书。

## 14. 实际执行命令合同

workflow调用原3b8规则监控器，真正science命令为新wrapper，核心参数形状如下：

~~~text
python -u COMPUTATIONS/root_20261116_six_control_contracted_trace_r273_run.py
  --request COMPUTATIONS/public-six-control-contracted-trace-r273-request.json
  --recipe COMPUTATIONS/actual119-batch3-contracted-trace208-lambda0p001-recipe.json
  --inputs-directory VISIBLE_MATH_INPUTS
  --source-topic VISIBLE_SOURCE_TOPIC
  --out VISIBLE_BASE/execution
~~~

这些占位是workflow实际环境路径的说明，不能据此在本地运行。wrapper内部明确传新full112、client及对应SHA，并从request给全部原执行参数，不依赖未来人为补数值。

正常Actions前置只作已有source/recipe/输入身份和Python/Node/shell语法工作；没有新增科学fixture、数值对拍或独立审查通过条件。原规则监控器内容保持原字节，只有原允许的已读README baseline在实际copy上显式绑定，不隐改原来源。

## 15. 全差异和发表映射

以真实195字节为基线，完整纯文本差异分成：

- core-four-relative-to-published195.diff：原3核心的完整差异加新helper全文；
- thin-seven-relative-to-published195.diff：七薄source完整差异；
- runner-relative-to-published195.diff、reader-relative-to-published195.diff；
- recipe-relative-to-published195.diff、request-relative-to-published195.diff、workflow-relative-to-published195.diff。

旧fallback函数、原角部分/Gram方向、原split方向与noJ RK算术正文保持原文；source/schema/manifest/调用点差异全部在这些完整文件中。不是只给抽样段或把未经核对旧cache当实际基线。

主控可先独立发表R466说明与13运行源/配方，再单独发表208request/workflow/interface触发一次新科学。所有source SHA以真实文件为准，暂存manifest不充当科学已执行凭证。

## 16. 后续真实结果的限界

208若资源先到，应保真实最后phase、最后完整/未返原call、所有实际试步与未开始后缀，不能由pipeline绿色或helper调用计数推断native成功。

若方向完整返回，仍只说明这一次新数值实现完成了该层；原noJ trial和所有原终端门继续独立裁定。若原fallback被触发，必须按记录说明其原因和是否完整返回，不能把整次运行统一标成全收缩。

若最终全部原科学门实际通过，才按它们各自原scope报告。本文目前没有新J、FD、positive/native/fullDN/audit或性能结果；R467留给该唯一实际208读回。

本接口不修改206/207，不接尚未实现的零形状快捷路径，也不把其它连续C、M精化或闭面结果转成这个旧六参数有限尾问题的证明。
