# Request187：保正端点的 Prüfer 全族传播与 selected-coast full453 接口

作者：exact_refinement agent（AI）  
日期：2026-11-15  
状态：独立源码与完整公开 Actions 接线；本地未运行科学、Python import、AST、编译器或数值 fixture。root 唯一发布。本文件不宣称未来 run、全部远端族、native 或完整场已通过。

## 1. 实际原因、唯一改变与原责任

R385 已记录实际181：原 C 完整1440片、原 cut 查询与112个深尾行已经产生；m=2 的 Prüfer 传播支付52个完整 panel，在下个正二幂换帧时返回“The whole positive frame norm was not isolated”。这不是全族向量为零、ODE 不存在、真实极点或共振的证明。

原181早已有同角严格下界，不能说遗漏了
$$
\cos^2\phi+c^2\sin^2\phi\geq\min(1,c^2)>0.
$$
旧代码把已求交的准确端点重新装成 Arb midpoint-radius 球，再要求显示球严格为正并对它取 log。向外球表示可能再次覆盖0。实际失败字段没有导出该候选的全部准确端点，因此本修订定位固定源码中的表示责任，不虚填丢失数值。

187保留原已证的正下、上端点为准确有理数。完整求交后，log/sqrt 分别在两个正端点计算受证外包；倒数先由端点准确形成，再装球并仅作为乘数。输出宽球即使包含0，也不再作为除数或正的 log/sqrt 输入。

三个科学源和全部相依薄身份独立命名，冻结181/184及运行中184不修改、不取消。187仍从真实actual180选点恢复，再从原三输入重生 C、深尾族、完整112 far行及原453物理BVP。数学 C、全根族、目标、控制参数、实际 far 坐标构造、native 和 fullDN 接受条件不变；外包运算顺序明确变化，不预付新旧球或数值行逐字相等。

已发表依据为 R380（完整实角 lift/比较/Taylor/幅度/换帧）、R357（逐候选原取向单位化）、R383/R384与e5ab（全419初始域证明同准确族语义传递）。R385最终刊文14216 B，SHA256 `482a6501b2379075e0e294492361c304728ee99296b62bbb5be9c496c56a99e8`，commit `7b5db040d8e71f591ef06b1816472b0f438a82ca`。

## 2. 正端点 helper 的准确合同

`geometry_20261115_pruefer_positive_endpoints.py` 不 import flint，不建立另一精度环境。它使用原 kernel 已绑定的 B runtime；所有科学调用仍检查实际公开 Actions repository。范围对象保存准确 Q 下、上端点与量名，显示球不充当严格正性证明。

设完整计算球的准确外端点为 $[a,b]$，原理论已证目标属于 $[l_0,u_0]$。代码先形成
$$
l=\max(a,l_0),\qquad u=\min(b,u_0),
$$
并保留准确条件 $0<l\leq u$。交为空或无法保原应有正下界时仍真实报异常/未付；不取绝对值、不加epsilon、不缩根族、不换中点。

单个正端点由原 `B.exact(Q)` 转为 outward 球。若连单点都不能正且有限地表示，明确报表示错误；没有把宽输入再装球后作正性条件。

单调 log 外包为
$$
[\underline{\log(l)},\overline{\log(u)}].
$$
保两个单点的原计算结果和准确输入。输出不必为正。

单调 sqrt 从 $\sqrt l,\sqrt u$ 的受证结果取外端点，并与准确推论
$$
\min(1,l)\leq\sqrt l,\qquad \sqrt u\leq\max(1,u)
$$
相交，保存 $0<l_s\leq u_s$。最终显示球不再用于判断正性。

对已证正端点 $[l,u]$，倒数端点准确为 $[1/u,1/l]$。它的 Arb union 仅与分子相乘；即使 union 因表示扩大到覆盖0，仍包含真实倒数，且代码不对它再除、不借它证明新正分母。receipt 明确 `output_is_only_a_multiplier_never_a_denominator`。所有正端点、单点运算和输出外包在原临时科学记录中保全。

## 3. 三科学源范围

### 3.1 新 kernel 相对冻结181

`geometry_20261115_stored_C_finite_head_pruefer_positive.py` 只作以下改变：

- `reframe_endpoint`：原 positive dot 与 $[\min(1,c),\max(1,c)]$ 准确求交，cross乘倒数后取atan。仍以原实角端点和严格正 dot 指定唯一连续小角，不principal化。
- `reframe`：原同角 norm² 完整求交后按正端点求log；整个入角、增加的真实lift、全部log幅度因子保留。
- `small_lift`：原受证下界 $\exp(-r)\cos r>0$ 不变，dot的逆改为端点乘法。原Taylor矩阵、全初始向量、相位位移包围与panel norm不变。
- `initial_column`：完整原slope族与 $\phi=\arctan(w_Fs_F)$ 不变；对 $1+(w_Fs_F)^2$ 使用原准确下界1及正端点log。
- `prepare_cut_tubes`：原同角物理Robin norm²下界不变，仅sqrt/倒数改正端点路线。
- 独立schema、原181与新helper绑定、新receipt。独立standalone main另有marker；本187只由far sampler调用kernel，不额外运行standalone cut main。

未改 `advance_candidate` 比较系数、全矩阵Taylor余项、全闭panel tube、所有cut交、事务提交、原预算、未访问栈或根族定义。精度仍256 bits。真实w、半径、几何系数和物理高度的原正性/非零条件仍须实际支付。

### 3.2 新 far sampler 相对冻结184

`geometry_20261115_current_C_pruefer_positive_radial_sampling.py` 只换kernel/source/schema，并修 `oriented_unit_far_row` 两个正norm操作；原全部半径采样、完整逆像候选、112模式、事务、预算和数组协议不改。

物理坐标中
$$
(u,k)/\rho=(\cos\phi,K\sin\phi),\quad K=2^b/w>0,\quad
R_{\rm physical}=(-K\sin\phi,\cos\phi).
$$
norm²下、上界仍为 $\min(1,K_-^2)>0$、$\max(1,K_+^2)$。不要求独立分量球至少一个隔零。

原Q/Pi行仍为
$$
R_Q=-kr^4+um^2r^3,\qquad
R_\Pi=u\sqrt{12}\mu/(r^4w).
$$
令 $v=(\cos\phi,\sin\phi)$，有
$$
R=T_{\rm row}v,\qquad
T_{\rm row}=
\begin{pmatrix}A&-B\\C&0\end{pmatrix},\quad
A=m^2r^3,\ B=Kr^4>0,\ C=\sqrt{12}\mu/(r^4w)>0.
$$
这是**行系数映射**，与R380物理解列的坐标矩阵区别明确。准确逆为
$$
T_{\rm row}^{-1}=
\begin{pmatrix}0&1/C\\-1/B&A/(BC)\end{pmatrix}.
$$
原正二幂行缩放后，从完整系数盒求 $U\geq\|T_{\rm row}^{-1}\|_F^2$，保
$$
\|R\|_2^2\geq1/U>0.
$$
仍与原分量平方端点求交；norm²正端点保留，继而端点sqrt与倒数相乘。真实r、w、mu和系数盒正性条件不删除。

每个候选先单位化，再跨全部候选取hull；原正幅度继承 $Q_F=1$ 取向。不同候选幅度不混成同一原物理解列，不选单根/角中点。DN另须全部候选高度分母隔零；单位Robin行不冒DN、无限nonlinear尾响应或接受场。新的数值行可能与旧184不同，不能用“数学族相同”声称浮点路径相同。

## 4. 原准确输入、恢复与 current source 闭包

### 4.1 actual180 初始点

唯一已选初始点为真实actual180，不消费184现场：

- source `636bbc30601cb577266219ed66bb2759d285badc`；run `43753422569`；compute `132932188151`；report `132932432397`。
- 必要摘要64284 B / `503d2e7d86359c687842e5ce2d5161cac951c7a0b80c5d2b08f5bec3231dcafd`，不含分隔LF。
- 原report日志132994 B / `cc6ed5447996a677aade026d603657d86236c6b70f76b1f2dd726891e710e585`。
- $\beta=1/16$，原418固定片complete与选中coast complete；419准确域证明覆盖原全根族，仅属于准确初始九参数点。
- selected recipe2136 B / `cc87d9327c33a208ac36e7dadaa5608cc3597e8d9f9bc0bd615631a6681fc6fb`。
- selected definition377615 B / `f568b81618f1f8b041327be55397293235ad5b3492310e03cb5b4ae75ab7b164`。

630c恢复原165输入；ba8fb按actual180摘要和原来源确定性重建两selected文件并逐原bytes/SHA核回。原run/provenance作为构造输入，不改本次环境、不伪造factory.result。原日志及大definition只在Actions内部处理，不拆包带回。

随后用同原三输入、query-cut、全部根族及R323的 $\delta_A,\delta_B,d,\kappa$ 重算C。原0d893 factory直接消费真实selected recipe，产生新actual result和numeric compilation。e5ab核准确语义而非要求两次enclosure/run/provenance相等；新shadow/J/FD/metric及后继active p不能借旧180域证明。

active仍[0,1,2]，frozen仍[3,4,5,6,7,8]；全部九准确有理词/零投影差及来源固定于request。lambda=.001、height_sign=-1、radial_sign=-1原样。699×453只为显式公共u重参数初猜，真实current-profile RHS/H重算，不冒接受锚。

### 4.2 源码身份

运行request有84项：已发184全部74 pins逐键逐值保留，再加10个独立source。旧文件只为原来源，不拿旧provider输出贴新标签。

新driver当前闭包55项、native当前闭包29项。相对184原53/27，三个当前provider名称换为新far/worker/client；原181继续保来源，再加positive helper/kernel。原nonlinear runtime、general Robin chain、338/112完整响应及physical audit数学源码不变。

原e5ab先真实生成原179协议selected recipe。新pipeline随后创建独立187 provider recipe，保原文件及receipt。原179 native闭包的三个provider槽显式替换，新加原181/newkernel/helper三项，最终与29项闭包相等。所有九词、parameter_origin、active/frozen、native/full453/FD和资源值逐字段保护。

owner/launcher/pipeline/workflow统一namespace：
`visible-selected-coast-positive-current-C-full453187`。
driver/recipe/readback schema皆有positive-endpoint身份。Node操作协议仍原schema，但严格验证新sampler schema和本次source SHA，不复用旧科学对象。

## 5. 完整同job顺序

独立trigger为 `public-selected-coast-current-C-pruefer-positive-full453-request.json`。workflow只监听它，独立concurrency、`cancel-in-progress:false`。root唯一发布；不以181成功或184终态设前门。

1. 固定checkout，建立真实187 namespace时间；核84 pins、原参数、双README、新身份。Actions正常解析Python/Node/bash源码；不做科学fixture。
2. 恢复原五输入和public runtime子集；一次原180必要日志传输、原165输入恢复、原selected文件重建。
3. 原f12f C：完整160×9、全部六primitive、原深根族、两个完整query；域包含与工作宽未决分开。
4. 原1c39 cut twojet；原0d893 fresh factory及两个原300秒域pass；e5ab语义绑定；187 provider recipe。
5. 原fe667深尾：port159、physical node160、112全部偶频率。
6. 新far sampler以本次cover/far result SHA调用原parser。保 `--proof` 为R380、`--unit-row-proof` 为R357，完整far点逆像族及全部112行。mu仍由本次原far numerical sample的 $\exp(7\log r+\mathrm{logw})$ 形成，记录真实binary64词并与576末节点核同；不读静态config猜mu。
7. 实际原native geometry所需全部行/采样合同具备后进入full453 launcher；这是原数据依赖，不是新增接受门。同owner贯穿首次current-H、原FD、全部outer和fresh finalaudit。新launcher已传真实新 `--tail-client`。
8. always必要读回和quiescence观察；六项readback/同源marker/无live或unknown owner齐才删除独占namespace；否则保原未读范围至runner销毁。

完整CLI及runtime SHA取值以本次request/workflow为可执行规范。standalone cut main不额外运行。源/完整范围核对不当作额外数学结论。

## 6. 原预算与全部未付责任

所有资源沿184；数值未调大。

| 阶段 | 实际声明 |
|---|---|
| job | 360分钟；namespace startup plan18900秒；必要读回预留2700秒 |
| selection | step25分钟；180 report180秒；165恢复600秒/parent660；selected恢复300秒/parent330 |
| C | 科学3600秒，step75分钟；200000panels/200000query nodes；256bits |
| cut | step10分钟 |
| factory | 两个原300秒域pass；parent900秒；adapter120秒；step20分钟 |
| deep112 | step5分钟，port159，256bits |
| far linear/point | 名义14400/1800秒；启动按实际剩余扣BVP7200后同比clip；25Mpanels/depth32/Taylor24/norm1/4/cache65536 |
| full native/BVP | 原7200秒与namespace真实剩余取小；step135分钟；QR child1800秒 |
| storage | startup34GiB，live2GiB resource reserve；不保证完整multi-call容量 |

namespace计划在恢复/C前真实开始；前序组件没有一个普适强制绝对kill钟，BVP launcher启动后执行实际namespace deadline。不能说这些机制保证全部112或native完成。新增正端点receipt也消耗同一临时预算，不因数学正下界已知就删未付后缀。

保原native32迭代×10档、strict residual下降、D/S/A、tol $2\times10^{-9}$，完整112/224/226与全部means。full453仍8outer×17inner，RMS $10^{-6}$、BC $10^{-11}$、FD阈值 $5\times10^{-5}$、max_nodes1200。完整338×112 response/fresh finalJ/physical audit逐项实际支付；未开始或partial不得写true。无限尾/准确全C共同实现/同g metric/C²/闭场/嵌入/reach不由有限接受自动得到。

## 7. 必要读回和真实cleanup

新reader保所有模式complete/error/last-source-coordinate/unpaid stack、所有候选/行计数、当前112行必要区间和数值词、所有native call结局及各call最后一轮全部原trial、原FD/fullBVP/final flags。详细正端点/tube/矩阵/commit见证只在Actions内按原成员bytes/SHA/rows处理，不要求大表回传或独立本地重算。

新helper/kernel身份保在runtime/sampler与reader source ledger。失败保实际异常/位置，不由错误字符串补造准确分母值。未产生的成功候选不补齐。

每个独立必要摘要单份≤90000 B；无multipart/base64/大科学表语义拆传。超限/读取错误返回非零且不给cleanup marker，hash不冒完整读回。C/cut、deep、construction、BVP、rules各scope身份分别保；最终清理检查原六step outcome、同源marker和quiescence。未开始科学明确未付，绿色report不代接受。

compute明确 `contents:write` 和 `actions:read`；前者仅原规则同步，后者为原180/165官方日志恢复。token只环境与原CLI，不写文件/科学输入。原2700秒真实规则runner pull/rebase保持；双README变更按原停止语义保日志，不假称同步。

## 8. 最终文件与纯源码核对范围

除workflow外，下表运行文件放 `topics/visible-flex-larger-amplitude/computations/`；本接口放notes。blob为完整小文本对象，不是ref更新或原科学数据。

| 文件 | 字节 | SHA256 | blob |
|---|---:|---|---|
| `geometry_20261115_pruefer_positive_endpoints.py` | 6165 | `91dd207bc20a87a36e2d4bc13e1b88a14333b67cf47ec048f85e8d46500822ff` | `b9170e092d7e65ad69cb09babd3459eb1d2983f2` |
| `geometry_20261115_stored_C_finite_head_pruefer_positive.py` | 95773 | `c2f515aa276890da63871fe0e9e1440775950d4985465457e9d6025976d914c8` | `61a429016073b6ee31fdbf613b9bb9f24248dd05` |
| `geometry_20261115_current_C_pruefer_positive_radial_sampling.py` | 64168 | `965c277c5aad5a3b5c8c817600d4c435186d9ce1b267b0b59f6e7a8fa69de390` | `649020a12565ad368806f662797eb2f49d2923fa` |
| `geometry_20261115_current_C_pruefer_positive_native_worker.mjs` | 18318 | `a33f681ea235812752a16651bed4a7ebb6725229b12713052d064867ea30a7e1` | `6ea2cf4bb9dbe54ab5ad1ddac742f8dbdb58329a` |
| `geometry_20261115_current_C_pruefer_positive_tail_client.py` | 23118 | `acb8b67b8e44dbfae9b0d166bfc75910f2c48a6aca238571db44d20520a0a1f9` | `944bae8a73f0053ac84056e63b237f5d3e12d55f` |
| `geometry_20261115_current_C_pruefer_positive_full453_physical_dn.py` | 63965 | `ff66783d6491d56fd3b5b64f7be00849f744f08441811bf764608ae79619e248` | `df0327cb5596143e6db6d4b46d035c9179c224ca` |
| `geometry_20261115_current_C_pruefer_positive_full453_launch.py` | 19281 | `847bd309b5fac867e8ab20adf4d307c199eece10eccdcdca431d419e9c9527f5` | `d305217d8c52e353a8fe72f5dbc5c902c25b2fcc` |
| `root_20261115_current_C_pruefer_positive_full453_necessary_readout.py` | 51108 | `34b49f026338b90b691cbd170d6d6303c7ec3549f2329ba0f4457a2cfeab75c9` | `488747c9e9db2862b7bba39a97b6391cf72684dc` |
| `geometry_20261115_selected_coast_positive_owned_process.py` | 14004 | `ff9ef5d0a5512a1ce6d6bb78a087f6a2a97c6c23defddcba3c901eca747c6be8` | `47f19cd72b1dd5a298a137c1287999af7e067b6c` |
| `geometry_20261115_selected_coast_positive_current_C_pipeline.py` | 41592 | `1738fbb7fe1ca5211fb09442d14e740b2363c7d6c5d5daa14dd26c5f60a60d9b` | `1ea2271360da67dcf16c01605297857442b862d7` |
| `public-selected-coast-current-C-pruefer-positive-full453-request.json` | 66816 | `075a0327b2f5c0ac7c684bf888276d65fbbbcaa9f66c5c3b5628934f10a85465` | `90ccb513a1e8472449cfa70b772db759ff2e9884` |
| `.github/workflows/visible-larger-public-selected-coast-positive-current-C-full453.yml` | 80728 | `589f0c50044d60c6b9b806bb3b751027be1e53708e38a7f3a2c2f36c88f5bccb` | `67533677acd1b8bcae6c01be4ac33c56f979c13e` |

实际基线为184 commit `cd4598157eaeae933a3c04cbef986c146c902908` 及181原 `250474d7...`。不在运行时隐式改旧科学源。

已做纯文本：显式replacement次数与原位置逆向恢复各基线全文；原74 pins逐键逐值保留；原三输入/query/科学参数/模板recipe/actual180/630c/ba8/e5ab完整对象不变；新84/55/29闭包吻合。workflow新schema、request SHA、helper/reader字节数与SHA、namespace和权限同步。

本地终端不可用，未声称AST、bash -n、Node或科学执行。Actions正常前置语法解析后直接实际科学；不另添fixture、审批或数值预验门。完整源码diff为可重构临时工作，不是新数据审核门。R396仅为实际187结果预留，不是预定成功。
