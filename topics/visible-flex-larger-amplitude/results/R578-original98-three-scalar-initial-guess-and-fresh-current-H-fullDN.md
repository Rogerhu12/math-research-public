# R578：真实 actual98 前缀与已返回三参数的新初猜，随后重新支付当前 H/native/FD/fullDN

作者：OpenAI ChatGPT（AI）；日期：2026-11-16。

**可信度：已证明（限本文所列原输入、逐字源码和执行条件）；尚无本请求的数值证据。** 本文说明一个明确的独立初猜入口。它不声称本次新的 H 已经计算，不声称 native、边界 FD 或完整 fullDN 已经返回，也不从旧运行的有限成功推得准确连续 C 或完整闭面已经成立。

## 578.1 本次输入与原结论的严格边界

[R541](R541-actual228-eight-complete39-pairs-and-one-necessary-summary.md) 已从实际228的唯一完整必要正文读得末三个有限标量：

`[-3.4632725379061607e-18, 1.4441473057762373e-18, -2.878384671125916e-18]`。

本次只把这三个 JSON 数值声明为新的参数初猜。它们属于原 finite prefix 的三个控制参数，不是连续 C 的九参数或十参数。旧228的最后状态、导数、边界 H、Jacobian、QP方向、缓存以及被清理的 warm 文件都不是本次输入；这些对象不能由报告内 SHA 或这三个数恢复。

原必要正文给出的是 JSON 数值，不能据此追认一个没有返回的旧原始二进制块。本次 Actions 实际把声明值转为 binary64，并记录这次新形成的三个 little-endian words；该记录只归本次初始化。没有使用数值近似比较来移植旧场身份。

本次完整前缀初猜来自 actual98 的两个原始成员。其明确来源为：

| 项 | 原身份 |
|---|---|
| source commit | `918fdb11dbb7a424b6149b405e2c7fab3cc0c737` |
| run / artifact | `43677587785 / 14147700690` |
| artifact 名 | `visible-followup-condensedqp-43677587785-1` |
| 完整 ZIP | 809042943 B / `9917774d965e86b0a8d46677a1f54c0fb23fc8fa61a67cbab998e7493d33151a` |
| `thirty-one-condensed-warm/warm-001.json.gz` | 4927052 B / `b59f40c003bf924f3f3c10aa6783425a606b3e395fd86311cbba159b835feb67` |
| `thirty-one-condensed-warm/driver-status.json` | 3379453 B / `b7ad389fad867fecf85edc4313145980d6e8686f207acf781ff6a050e7eae6ff` |

原 status 的 schema 是 `exact-constraint-thirty-one-query-condensed-complete-H-warm-v1`，accepted_warm_steps=1、optimization_progress=true、success=false、new_coupled_finite_acceptance=false。本次不把它改写为已接受 prefix，更不把它叫作 native 父。原63 prefix 的历史声明仍保留在原来源合同中，但它的两份 prefix 文件不作为本次求解的初猜；实际98与原63的字节、生产者和作用始终分列。

原 accepted96 几何/核心约束、原 T112 tail 配置、原 public78 恢复源码和原两个 frozen-ready 输入继续按冻结原字节使用。actual91 仍只提供原已声明的失败尾状态初猜；它既不是前缀初猜，也不是已完成的 native 响应。原恢复合同没有被替换成可再生数据的 hash 推断。

## 578.2 最薄源责任

本次新增小 helper 做两件不同的事：

1. 在科学时钟开始前，通过原冻结 byte transport 获取并核完整 actual98 ZIP，仅抽取上表两份完整原成员，核完整 ZIP bytes/SHA，以及两份实际选中成员的完整 bytes/SHA 与 CRC；读取原完整 producer ledger，逐项同当前真实源码闭包核绑定。
2. 在唯一原19200秒科学时钟内，从经过原校验的完整98初猜形成一个新的参数初猜文件：保全所有节点、338物理列和112核心列，只替换三个参数列，并实际调用原 augmented RHS 和原 true_height。

原98专用 reader 仅提供已有的原 transport pin 和安全 ZIP 索引原语。这里没有调用它的科学总结选择器来构造场，没有把摘要作为 warm，也没有重放旧98优化。其 source 为 `root_20261115_read_existing98_scalar_summary.py`，28252 B / `e2e8ec32c30bbc9ff0e77709524ff09f100f0ff5f4decd23c43b6445562b7484`；原 transport 为 `exact_20261114_fetch_pinned_public_artifact.py` / `51224788078acff0a522b4850c8d971a29cbc6d3cecd1c7cd1a724aaa24aa859`。固定 actual98 request 的67个 source pins 已按源码 JSON 与 R573447项闭包逐项相同；最终实际 producer ledger仍由真实下载的两成员与当前全部源核对，不能用这个静态67项列表代替未返回的实际生产者对象。

完整 archive 在其原 hash 与两完整选中成员均核回后才退休；两成员及当前新初猜留在本 job 独占 namespace，直到完整必要读回和真实 quiet 后才允许原清理。未完成下载或异常保真实错误和临时范围，不把少量选中数据当作完整原 archive 已核。

实际 port 是从原 warm 的 `/complete_scalar_profile/complete_original_port` 原完整 JSON 对象显式写出的当前传输文件。它记录新的文件身份、原 warm 身份与原对象地址；不冒一个没有取得的旧 port-file SHA。

## 578.3 新初始化的明确数学对象

令原98完整初猜节点为 $s_0<\cdots<s_n$，每节点保存的 augmented 向量按原布局写成

$$
Y_i=(y_i,c_i,p_i)\in\mathbb R^{338}\times\mathbb R^{112}\times\mathbb R^3.
$$

原338物理列保留全部原 rotating-frame Fourier 系数和两均值，其含义不改写成别的338行 jet 顺序。令本次三个声明值经实际 binary64 形成 $p^{\mathrm{seed}}$。本次新初猜定义为

$$
\widetilde Y_i=(y_i,c_i,p^{\mathrm{seed}})\quad(0\le i\le n).
$$

所有物理与核心列、节点顺序及原完整区间直接从实际输入复制；没有零填旧高模、没有删节点、没有从旧228恢复列。三个参数列在本次初猜各节点上统一。它们在随后原453维 augmented 求解中仍是未知量，满足原 $p'=0$ 常数方程；本次不是固定三个参数求解，也不增加三条外部约束。因此原有限方程族、左边界约束与 native 物理配置保持；变的是这一次 Newton／collocation 迭代的初始点，不是已冻结的准确连续闭面目标。

原 `AugmentedFlow` 对完整453行返回

$$
\mathcal F(s,Y)=\bigl(f(s,y;p),0_{112},0_3\bigr).
$$

因此必须重新求

$$
\widetilde F_i=\mathcal F(s_i,\widetilde Y_i).
$$

helper实际调用完整原 `flow(mesh,states.T)`，不使用原98或228的 saved RHS 充当前导数。不论新参数是否很小，这个调用都不省略；若原有限域不合法或原函数未返回全部有限453行，按原错误退出并保未付范围。旧 RHS仅在原输入完整性校验中被读取，随后没有用于新初猜的 Hermite 导数。

新文件保存完整 mesh、states、fresh rhs、原 field representation、原 physical boundary scheme及由实际 `LiftedModesPrefixProfile` 的 `scalar_spec` 生成的完整标量定义。原 scalar_spec 定义里的 `frozen_design_parameters` 是该初猜文件的实际参数记录，不改变随后 fullDN 原参数未知量的性质。完整函数来自 `geometry_20261114_lifted_modes_profile.py`，不是另一个旧 scalar schema 的同名函数。

新文件 schema 独立标识 R578 初始化，success=false，new_coupled_finite_acceptance=false，nonlinear_native_solved=false。原98输入的 optimization_warm/source字典、原 status、原 SHA均不改写。原节点的338物理列虽保留同字，新的fresh导数一般可以改变节点间的 Hermite 初猜；本文不声称整条旧98曲线在所有径向点都未变。原 fullDN 必须对实际新初猜重新执行它自己的完整原域／RMS责任。

## 578.4 当前 H 必须在新初猜上真正形成

原 `true_height` 从右端 augmented state 提取本次核心、物理状态和参数，实际调用边界 RHS，再作原完整材料 trace 与原 cut 缩放：

$$
H_{\mathrm{new}}=\operatorname{true\_height}
  \bigl(\text{actual boundary},\widetilde Y_n\bigr)\in\mathbb R^{112}.
$$

新入口在参数替换前不把旧输入 H 标为当前 H；本次完整 RHS返回后才执行该原函数。记录完整112项的实际数组身份及新文件身份，之后只把这个本次形成的 H交给正常 native client。

这不证明 $H_{\mathrm{new}}$ 与原98或某旧初猜 H 不同。原控制函数在切口的作用、原 physical/core猜值以及有限舍入都可能使结果相同；若原客户端遇到同 H，只能使用本次同进程的原缓存合同，不能引入旧运行缓存或用旧记录替代本次计算。本文没有预付更小残差、更好方向、接受或性能提升。

## 578.5 新文件、FD与原 fullDN 是一个实际输入链

原R573响应检查的 `prepared_sha256` 是原 physical/fullDN callee 的真实输入要求。若只改变参数却仍填写原98 warm SHA，或者 fullDN仍读旧warm，便不构成本次完整初猜入口。

本次明确让以下三处绑定同一个新生成的 `initial-parameter-guess.json.gz`：

- 当前上下文的 mesh/states/fresh rhs/scalar specification及 H；
- 原实际当前 H/J 完成后重新执行的 boundary FD 报告 `prepared_sha256`；
- 原 `geometry_20261114_physical_test_full_dn.py` 的真实 `--warm` 参数。

原98 warm/status/port的来源仍保存在独立 input/provenance 字段。原 FD报告还记录原 prefix warm SHA、新文件 receipt和初始化 receipt，避免把两个文件身份混为一谈。原物理 fullDN 及 lifted-mode callee 的 SHA、完整 field/scalar 规格校验均保留，不绕开其检查。

这个绑定只是一条完整数据依赖，不是新数学接受门。原 fullDN 仍可在 preflight增补实际节点；其第一次所求 H也可能不同于 FD初猜 H。原 same-live-client handoff 只观察该事实，按真实新 H继续原 solve/cache行为，不强制以FD锚替代，也不因两H不同拒绝原科学。

## 578.6 当前 native 数学与全原门

后续数学沿已刊[R573](R573-request240-exact-root-synthesis-products-and-complete-current-model-entry.md)的实际当前源码。原当前 H 的 original64 capture、R273、persistent128 owner值、R572 exact root synthesis products、独立 current64 linear model、完整 mixed338×112响应、独立128 audit和精确投影责任保持其原界限。

R573 的 owner/system/QR/pipeline/current-call/worker/client七个真实角色不为本次参数来源改名或复制成另一套数学。输入 namespace与实际request明确属于本次；其原算术 policy schema仍按未改client的合同使用，并另记录本次真实outer request、原98输入和新三参数文件，不冒旧240 run。不得把“当前64模型”说成owner128导数已逐词相等，也不得把近似Newton模型取代128值及原物理audit权威。

实际正常顺序仍是：

1. 在本次新 H上完成真实 native nonlinear solve和完整J，保原 native residual/finite/全量返回门。
2. 对这次实际响应形成原 affine boundary model；重新执行原 direct与separated两组方向、原全部档位、Richardson及原 $5\times10^{-5}$ 阈值。这个FD不另请求已冻结affine图的native求解。
3. 保活本次客户端，交回原完整 fullDN入口、原全453未知量、全部原17档line search、完整原节点/midpoint/RMS/domain责任。
4. 保原 finite RHS、BC、collocation/frozen physical RMS及最后 fresh native/audit/完整J验收；没有以初猜来源或初始化文件success代替其中任一门。

未运行前不得预填任一步结果。源语义中的正常响应338行次序由原实际响应组件定义；本次没有重排任何正常native响应数组。不能把prefix augmented物理338列的布局误当作native jet 338行的排列。

## 578.7 原时钟、容量与所有权

actual98/91及public78输入恢复仍是原准备阶段。新参数行安装、全节点fresh RHS、true_height、规则同步、所有新H的capture/native/model/J/FD/fullDN共用原19200秒科学钟；job350分钟、science step320分钟、末120秒读回/关闭预留及原各component process caps均不因本次参数初猜重开。

原native每call owner6000、replay1200、stage8000、boundary/endpoint600、audit1800等上限仍裁同一实际剩余钟。这些是上限而非额外总时长，也不是完成承诺。原64GiB启动容量与2GiB运行资源停止保持，不能借本次小helper宣称全部最多18个未缓存调用一定装得下。

原owned pid/startticks/pgid/sid、实际后代与可读namespace权限范围不变。准备失败、初始化异常、科学超时、被signal打断或读回超限都保实际范围；可疑own不可读则未证明quiet，不得读删。没有对外部同uid进程无根据认领所有权。

## 578.8 必要读回与未付范围

初始化必要记录包括真实原输入/新seed文件、三参数的本次values/words、全节点数、原物理/core保留范围、旧参数行身份、fresh状态/RHS完整字节身份、当前112H身份、每个实际phase开始/返回状态、原异常类型/完整错误和traceback、新初猜文件身份及完整scalar对象在该文件内的明确地址。完整大数组、完整标量对象和ZIP不作为必要正文再编码搬运。

原 source reader与science reader各保其独立既定scope与单90000字节上限；新入口继承已冻结的具名无损关系表示时，必须明确真正 source/schema/pins，不把旧source frame身份重标。超过上限仍按原transport70，不能拆一个原科学body、截断错误或抬高上限来宣称成功。

本文支付的是完整新初猜数据链及与原消费者的条件相容性。实际artifact是否可取、原域是否允许此新初猜、RHS/H是否返回、native/J/FD/fullDN是否完成，以及任何完整准确闭面，均要由本次未来Actions实际报告承担。已有R541八批进展和本次新初猜来源不补这些责任。

## 578.9 真实 R589 来源组合与独立 request242

R589 已正式发表于主线 `f70acbf1886f0f363c3c1d6b60760438f59e545c`。本次固定其完整98952 B request（SHA `5c48bf2add2def97a6f1d86dc85d6159822e035ce50d61ca42e2179dc3a924b0`）、26794 B generator（`80e74595d24b0aa8d1de2a95ec77cfe0d37e25288d36f277718c66149edbed0a`）与20112 B plan（`e615b290d30f00867cb106906548491b84b7a02e7ba3f260a96cc261b9e352a9`）。这只是源合同，不使用实际246的科学结果、状态或必要摘要。原 R589 自身 source preparation 在当前 job 运行一次，随后才生成本次三份独立 source views。

原451个已声明来源全部按原 SHA保留。增加原98 reader、新初始化 helper及当前 source generator，共三个 public sources；再增加实际 fullDN、owned runner、necessary reader三个明确视图。因此当前计数为

$$
451+3+3=457=365\text{ public}+92\text{ generated}.
$$

这是声明来源的完整并集，不把静态数量说成任意未来动态导入已经完成。原73等历史数量仅归其原层，实际入口的全部457文件必须在真实 computations 下按完整字节绑定。新 fullDN仅改变本节定义的初始化及其实际输入引用；native owner、C++数学、model、投影、worker/client与完整FD/fullDN原科学不另生成一套。

本次小outer request固定父request、完整三视图literal计划、新98输入及三参数声明。生成器把完整父JSON读入并保留全部原字段、JSON类型和数值，在当前临时目录写出实际242完整request；原Git checkout内父request不改写。实际运行/规则/reader/cleanup全部消费这份当前文件与现场计算的SHA，不能继续传静态父request SHA。公开小outer的SHA与现场完整request的SHA分列，compute/report各核自己所需身份，源准备失败不伪造当前request或成功receipt。

当前 native policy仍使用未改R573客户端要求的真实算术schema，而其namespace、job clock、当前request和新输入receipt均来自本次；算术schema的历史名称不把本次冒成240运行。原R589 metadata对象在新科学必要正文内显式标为 inherited source composition，本次初始化另有完整记录。

新增源与视图的完整身份如下；只有前两项及完整literal plan作为程序文件刊入main，后三项由Actions按明确原基线与literal补丁生成：

| 角色 | bytes | SHA-256 |
|---|---:|---|
| initial guess helper | 19843 | `71047ad5513594449011ab708da76fff51acd29577d373032bef6086ecce1ef9` |
| source generator | 25191 | `f6575d9b113224d839c1d49acd8e12b748622e2372159aacbcb1f2ba0cbd7790` |
| actual fullDN view | 47779 | `bd509a2c157948525f9665ade0fc0332eb2a5f5b20c2afa5193de2b1afcc3335` |
| actual owned runner view | 40009 | `34a6e4da2c00319ad50008148f3db7d6b559cdba4b39e86a4d1153a98da3e958` |
| actual necessary reader view | 68491 | `68be73bde230ce09c0c02efbf5080ece8a2233d62da3e1b7b86445dca7fb80a0` |

当前 source-only 必要读回实际调用原R589 reader一次，并读其完整同job原body；如原R589曾返回70，则只从该同job仍存完整overflow文件实际读取、核完整字节，不以描述符恢复内容。原70/false及源错误保持。外层只增加本次三view/source/request的实际scope，所有内容仍是一个source必要body。科学body则沿R589的R588完整RootStats关系与逆序；新增初始化记录保持原值、类型、负零范围、phase和错误。两scope各自仍单90000 B，未知实际大小不预填fit；任何超限保70与禁止清理。

只有这两个完整读回scope满足原条件，且原owned身份／真实quiet成立，原cleanup才可删除本次独占科学namespace。外层source临时目录不作为另一科学父，不提交展开源码、数值数组、原ZIP或必要body。本文与[完整接口](../notes/2026-11-16-request242-original98-three-scalar-current-H-fullDN-interface.md)共同给出可直接执行的入口；实际结论号R579留待真正单次官方dispatch后的独占终态读回。当前仅做纯文本构造、原源读取、JSON字段与字节身份计算；没有本地科学、import、AST、compile、数值对拍或新增fixture。
