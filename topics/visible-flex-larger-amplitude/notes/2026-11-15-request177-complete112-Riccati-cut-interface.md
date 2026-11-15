# Request 177：同一连续 C 的全 112 两图 Riccati 比较、完整 cut 族与必要读回接口

作者：AI。日期：2026-11-15。

状态：独立科学源和公开 Actions 接线。本文没有实际 run、当前输出 SHA 或成功证书；本地只做源码文本构造、原字节身份和静态字段检查，Python AST、bash/Node 语法检查及全部科学计算均由公开 Actions 实际执行。R375 已独立发表，不以本请求的运行或新增 fixture 作为其证明前置条件。

本请求从原完整深根族重新传播同一声明 C 的全部频率 $m=2,4,\ldots,224$，目标是原 binary cut 的完整闭逆像族。它没有把 R358 或 R368 的继承宽盒缩小，也没有沿用旧尾的零 J、far graph 或任何非零 $H$。新方法替换的是有限头区间传播表示和存在证明：保留完整系数闭包，使用两个自治 Riccati 比较解夹住真实比值。完整 DN 仍须逐个真实 cut 候选支付高度隔零；非线性尾与完整 BVP 不由本请求推得。

## 1. 冻结运行文件与来源

| 文件 | bytes | SHA-256 |
|---|---:|---|
| `computations/geometry_20261115_stored_C_finite_head_riccati.py` | 84732 | `34606e3fea2093f78cc3cb88fa6e5f7bcc32112c8f9053484628ad1a16e11124` |
| `computations/root_20261115_riccati_head_scalar_readout.py` | 28810 | `13cf5b44d3da7d8aa9fdf48a1bb735e450c30e6c6db4f7d038a183e1ba56e88f` |
| `computations/public-stored-C-riccati-head-request.json` | 25668 | `1c77c60028ec7bfc3798ff8ceb301f013c10b575ee3c42d055b2c3f209c36b58` |
| `.github/workflows/visible-larger-public-stored-C-riccati-head.yml` | 76744 | `ef3cd2593e219e8be42977fdc14ab50da9d6d2d1ccae9e9a71a53b5d0c332c4c` |

完整包含、闭时段存在、变图、幅度和 cut 责任见 [R375](../results/R375-continuous-C-two-chart-Riccati-comparison-and-cut-cover.md)，22,953 B / `c05a22becdc752bb87b7152761ae6b8ef02b30084bd09de62c7b305701609fec`，已发表 commit `58bbcda6c3af3a0e9afa7e8cbeedcd0873996f13`。原 R286、R297、R306、R312、R324、R347 均在当前 request 与 workflow 中逐 SHA 保留；并未把原科学源改写为新 schema。

本次科学入口为 `geometry_20261115_stored_C_finite_head_riccati.py`。它显式保存原 f12f 连续 C producer、fe667 深端 producer、4531 原通量传播器和 5440 前一射影传播器的身份。前两项生成本 job 的实际输入；后两项供来源与原合同核对，不把旧传播输出当作本次初始族。

最后相对主控已读数学稿只有科学 stdout 的 END marker 更正：BEGIN 与 END 现在均为 `R375_CONTINUOUS_C_RICCATI_HEAD_SUMMARY`。另将 request 中 `local_defect_bits_scope` 的一个表述由 relative 修正为 **absolute**，对应源码真实的 $2^{-\mathrm{bits}}$ 常数 barrier Taylor 列误差工作目标；没有更改科学运算。当前表中均为这两项修正后的最终身份。

### 1.1 完整 direct source closure

本次是 17 个 direct pins：保原 162 的连续 C、深端、旧通量/射影与 rules/恢复来源，去掉旧读回入口，新增本 Riccati 科学源和必要摘要 reader。全部原公式的更深恢复来源另由 `source-dependencies.json` 和原 public resume 验证。

| 源文件 | SHA-256 |
|---|---|
| `geometry_20261115_stored_continuous_E_cover_v3.py` | `f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df` |
| `geometry_20261115_stored_continuous_E_cover_v2.py` | `004010b681aa35635e15b229a3e5b78602b3ec480a631a761e42f6c7d563b6ea` |
| `geometry_20261115_stored_continuous_E_cover.py` | `9aa0da45027afa37ca329eab73e5e93e788f2bbafb908b9e8c2960f537a427ed` |
| `tail_frozen_geometry.mjs` | `db6664fcd7be618d2b684c39c01c53d97833d11e14af206b12c71e4b058713e3` |
| `strong_frozen_calibration_factory.mjs` | `77e9d2fc0e277ef69c9a4300ceba2d3d6b03056fc6a4868fab049a1a1c290247` |
| `closure_bounded_point_cache.mjs` | `35289a4de44ec409bc211f82c7a1bee81a10c6bc1c5fb31e4ca9a8634cc09043` |
| `exact_20261114_closed_background.mjs` | `be358bf780c88ebd85cdf07d9e8d2cc3b37ca20a4d8ea3a1ba69e7c40c2c4e1b` |
| `exact_20261114_public_resume.py` | `11399783f01b145ee3f23d88213af368daee9c16dfb858b40dd7316870b300a5` |
| `source-dependencies.json` | `7de25376ab0ec10277840ccdca8ec6b46b41bee6add97acd9d38c06bbc8cd941` |
| `root_20261114_current576_rules_runner.py` | `3b8b6dd5eb5df373ffa14525f02e1a0376bafc2da91ce564631f771752e2afde` |
| `geometry_20261115_stored_C_v3_cut_twojet_readout.py` | `1c39b242224824b361cbe5d28ea838b7e4824f5506a05302c662f045f735aeed` |
| `geometry_20261115_stored_continuous_C_far_graph.py` | `fe66789e7d94ab014662250e90642ab7fda3084b39c00b93836459220b33bb2a` |
| `geometry_20261115_stored_C_finite_head_flux.py` | `4531b5b35093fa9c0010f9fdbd6700dcf4b099c076b5a3d69d20ccafda8af87d` |
| `geometry_20261115_stored_C_finite_head_projective.py` | `5440e2e0457b360120c180a2531e3db899d8534cf6366183fd68d111ede18216` |
| `root_20261115_current_C_native_scalar_readout.py` | `2f2386afab07e5acc9b6ec155f782cb1ba1c8df5a879607effd5985c151784ff` |
| `geometry_20261115_stored_C_finite_head_riccati.py` | `34606e3fea2093f78cc3cb88fa6e5f7bcc32112c8f9053484628ad1a16e11124` |
| `root_20261115_riccati_head_scalar_readout.py` | `13cf5b44d3da7d8aa9fdf48a1bb735e450c30e6c6db4f7d038a183e1ba56e88f` |

保留的 `root_20261115_current_C_native_scalar_readout.py` 只作为已冻结来源身份，本新 reader 不 import 它，也不调用旧 multipart 输出。完整新 reader 只使用 Python 标准库。

### 1.2 三原件和原查询

三原件均由真实历史 `8bd267107cc8710d371f3b62c02986655ac965b0` 恢复，目标路径、原 bytes/SHA 和两个 ready 的 Git blob 都在 request 中，不依赖当前 main 常驻 raw。

| 原件角色 | runtime basename | bytes | SHA-256 |
|---|---|---:|---|
| config | `tail-config.json` | 2161 | `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5` |
| calibration_ledger | `ledger-ready.json` | 109004 | `563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6` |
| stored_reference | `stored-ready.json` | 29774 | `c1c44f2384845c25d2dcb0ec7127934fa46b54aa74613efcd6f9f6bcf0eb541d` |

原查询文件 `original-stored-continuous-E144-queries.json` 为 1,303 B / `4e59c69fae54045e100180e2d7576b848423a503394ff0b4dd87f6e219b7fd59`。第一个查询仍是 config 实际 binary64 `rCut` 对应的准确 dyadic 点；第二个仍为原 natural whole domain。没有用名义 radius 重归一 cut，也没有从区间中随意选一个 radius 替换真实输入。

实际 source run、result SHA、所有临时流的身份由同一 job 运行时形成；此接口不填未来值。原前缀、接受场、positive-lambda 解、非零 $H$ 或最终几何数据均不是本次输入。

## 2. 同一 C 对象与已付/未付边界

模型保持 R286 的 `original-exact-root-family` 声明 C，不是把原有限 adaptive/48-selector 求值器换个标签。所有 $n\ge160$ 的真实深根仍保其完整规定族；这里不通过数值中点选择一条无限根序列。完整有限头为 $160\times9=1440$ 原片，全部六 primitive 同时保留：

`A, B, sqrtE_A, sqrtE_B, w_A, w_B`。

原 f12f v3 的 cap/cusp/flat/valley/保护端处理、R306 三端点 primitive 的严格条件、原积分工作判据和 callback ResourceStop 还原均不变。实际 finite-head prefix 不足时不得称自然 $R_{\rm out}$；自然外端无平延拓许可。完整 cut 读回仍读取同 job 所有真实点逆像叶的 $E,E_r,E_{rr}$，给完整 dyadic hull，没有新增 derivative-width 门。

深端生产器按 R312 全部 112 模态、port 159 / physical node 160 生成独立行与完整根族误差。该层只付深端，不预付有限头非共振、cut DN 或无限非线性尾。有限头输入绑定逐项核：

- 本 job cover result 与全输入 binding，原模型/公式/物理参数；
- 本 job far result 与全部 112 原行、源身份、同一 C 输入；
- 原 cut 点叶流及全部 head/deep 关联、完整 source panel；
- 原实际 config、两个 ready、运行源码、R375 证明；
- 本次预算作为运行元数据保留，不借它改变模型身份。

与原 binder 一样，`original_core` 比较只从对象等式中剥离 query_input/runtime/work_parameters；实际这些字段仍完整记入结果。它不是忽略未知物理参数或允许借旧科学数组。

## 3. 物理坐标与两图状态

沿原单调 source 参数 $x$，记 $D=R_x>0$、$q=w_x$，保原严格 $R>0,w>0$。物理状态是 $u=H$ 与 $k=dH/dr$；内部通量 $j=wk$。原完整方程：

$$
\frac{d}{dx}
\begin{pmatrix}u\\j\end{pmatrix}
=
\begin{pmatrix}
0&D/w\\
m^2q/R&0
\end{pmatrix}
\begin{pmatrix}u\\j\end{pmatrix}.
$$

不再乘一个旧 source length，也不借旧 $\Pi$ port。$q$ 允许变号，系数必须从同一整闭面板的真实 C 包围形成。

保存原 $Q_F=1$ 列的准确非零因子分解：

$$
Z=a\,\operatorname{diag}(1,2^b)e_i(z),\qquad
e_0(z)=(1,z)^T,\quad e_1(z)=(z,1)^T.
$$

其中 $a$ 不物化为巨大矩形球，而独立保存 sign、$\log|a|$、准确二幂变化和完整因子链身份。这个分解没有宣称新的归一列等于原 $Q_F=1$ materialized column。

初始仍取原深端的完整族：$a=r_F^4>0$、$b=0$、$V=(1,w_F\,\mathrm{slope})$。未选择一个深根中点；初始 slope 的全部严格区间误差进入 ratio。

面板内 $b$ 固定，令

$$
\alpha=2^bD/w,\qquad \beta=2^{-b}m^2q/R .
$$

图 0 为 $z'=\beta-\alpha z^2,\ (\log|a|)'=\alpha z$；图 1 交换 $\alpha,\beta$。换图只能发生在原面板端点，且完整旧 ratio 盒严格隔零。当前确定性工作选择是其绝对值严格下界大于 1 时换图；否则保原图。合法变换准确为 $z_{\rm new}=1/z$、$a_{\rm new}=az$，sign 与 log 同步，绝不先裁剪原盒再称其隔零。

二幂 balance 改变也准确保原列。图 0 的 ratio 乘 $2^{b-b'}$、幅度不变；图 1 的 ratio 乘 $2^{b'-b}$、幅度乘 $2^{b-b'}$，相应 log 加 $(b-b')\log2$。两操作的全输入盒、输出盒和依据留原 ledger。

## 4. 完整闭面板比较与真实存在范围

以整面板系数盒 $\alpha\in[\alpha_l,\alpha_u]$、$\beta\in[\beta_l,\beta_u]$ 为准。图 0 下/上比较方程分别为

$$
l'=\beta_l-\alpha_u l^2,\qquad
v'=\beta_u-\alpha_l v^2 ,
$$

初值分别取完整继承 ratio 盒下、上端。图 1 按 R375 交换系数。由于 $z^2\ge0$，$\beta$ 变号不破坏这些上下不等式。真实可变系数没有被一个中点常数矩阵替代；其全部变化由比较端点支付。

每个自治 barrier $y'=A-By^2$ 通过完整常数线性系统求包围：

$$
\binom p q
=\exp\!\left(t\begin{pmatrix}0&B\\A&0\end{pmatrix}\right)
\binom1{y_0},\qquad y=q/p .
$$

原二乘二 Taylor exponential 的全矩阵余项乘完整 $(1,y_0)$ 范数；末值与整个 $0\le t\le h$ 的闭管分别外包。只有上下两个 barrier 的整个闭管分母都严格正，才支付比值、比较和真实原分母不会先为零的存在责任。只检查 $t=h$ 不足，本源没有这么做。

自治 barrier 在无极点的唯一解区间内单调或恒定，因此以其原初、末端极值形成整管；不假设真实可变系数 ratio 单调。若全闭分母未证，则分裂当前原面板；若达到 depth/resource 限制，保留原 state、stack 和 suffix，记 partial，不从准确基本矩阵可逆推区间可除。

`--local-defect-bits 12` 在本独立方法里的明确含义是**绝对** Taylor 列误差工作目标 $2^{-12}$，不是原中点 Duhamel 相对误差、不声称 12 bits 本身提供准确解证书。完整比较包含和余项严格外包才是数学依据。原 norm $1/2$、24 项、depth32 作为工作策略保留；work goal 未达时仍可在全部严格存在条件成立且源码允许的范围保 coarse-valid 包围，不能把它当更窄已付盒。

对幅度，整 ratio 管与整系数盒形成 $\Gamma$，包围真正 log 导数。末 log 由 $\log|a_0|+h\Gamma$ 包围；整管由

$$
\log|a_0|+
[\min(0,h\Gamma_l),\max(0,h\Gamma_u)]
$$

包围。所有此前 uncertainty 同时保留。该 $a(t)$ 是整个面板上的非零函数，不是随 cut 候选任意换一个常数；sign 不变，所有 frame/chart 因子另有原记录。

## 5. 原 cut 全逆像与 indexed Robin family

原 cut 可能有多个 source piece、多个闭参数片或共享端点，全部由原完整逆像叶关联。当前 producer 的原叶具有其既定正宽生成合同；闭面板/叶的交集允许等于一个端点，源只跳过空交集 `left>right`，不漏掉相等闭端点。若将来上游改变叶类型，仍必须沿真实关联规则处理，不借本接口扩张已核 source。

对每个已付面板的整归一通量管 $(T_0,T_1)$、固定 $b$、同一正 $w$，原物理列满足

$$
(u,k)=a(t)\bigl(T_0,\;2^bT_1/w\bigr).
$$

每个真实 cut 候选保非除式行

$$
[-2^bT_1/w,\ T_0]
$$

以及其 index、真实非零幅度/sign/log、整管与实际 leaf intersection。不同候选的比例可以不同；不得把这些行先 hull 成“原 materialized 列”。

每个候选只有完整 $T_0$ 严格隔零时，才形成物理 DN 商

$$
D_m=\frac{2^bT_1}{wT_0}.
$$

再对所有合法候选的实际商作 hull；完整 DN 还须全部原逆像叶覆盖且每个候选商合法。若部分候选未付，保已得合法商的 partial hull，不能将它提升为完整 DN。分母盒含零只说明当前包含未证明可除，不是准确共振的反证或证明。

full-cut 与168/169所需的指定物理 far 单位取向行是不同目标。本源不调用新单位行采样器，不借 R357 把本次 cut 结果冒为完整 nonlinear native 几何已就绪。

## 6. 临时账本、事务与全 pending

所有大原件只在本次 owned 临时目录保存。主要 schema 是
`R375-original-C-complete112-Riccati-cut-family-enclosure-v1`。

完整 payload 仍保每个已访问 panel 的同 C 系数、两个 barrier 的全初值/系数/矩阵误差/闭分母、整比值管、幅度、frame/change、实际 cut 交集和未付条件。表中的 scope 不等于把大阵全部传回聊天。

| 原 ledger 名 | 数学/运行责任 | 新 reader 返回范围 |
|---|---|---|
| `coefficient_boxes` | 原整闭面板几何与系数包围 | 完整流 SHA/bytes/行数，未逐值独核 |
| `accepted_panels` | 准备的完整 panel/barrier/状态记录 | 完整流 SHA/bytes/行数；prepared 不自动是 paid |
| `projective_panel_commits` | 原事务最终落定的 spans、state/factor chain | 完整流 SHA/bytes/行数及明确 commit 语义 |
| `cut_tube_contributions` | 逐候选整管、商、行族和原 leaf index | Actions 逐行解析；必要整数范围/计数/身份，不搬全候选矩阵 |
| `cut_leaf_coverage` | 全闭 cut 每叶的已覆盖区间与未付 | Actions 逐行解析；完整必要覆盖/未付范围 |
| `complete112_mode_status_and_columns` | 全112实际 started/complete、末状态、DN/partial、error | 全112紧凑原字段，完整 DN dyadic endpoints |
| `complete_unpaid_scope` | 当前 stack、未访 source suffix、未启动模态、失败事务 | 必要原 stack/suffix/未付原文范围完整 |

原 writer 先 prepare coefficient/panel/cut 等记录，再提交 state 与 commit。只有 commit span 中的 prepared 行才是 paid prefix。若 I/O 或算术异常发生在 prepare 后，保原 transaction 未提交身份；新 reader 不把 prepared 行数当已接受 panel 数。

所有112模态有实际 started 与完整状态范围；当前中断模式保 last-paid、当前 stack、剩余原 source 区间；其后未启动模式另列。全局 budget/DiskStop/PanelUnpaid 与原数学隔零未付分别记录。若上游 C/deep 不足而无法启动，仍保真实缺口，不模拟 mode 数值。

## 7. 单份必要读回协议

新 reader 的输出 schema 为
`request177-actual-finite-head-complete-scope-readout-v1`，
reader schema 为
`request177-Riccati-head-necessary-scalar-readback-v1`。

CLI：

```text
python root_20261115_riccati_head_scalar_readout.py
  --base <owned-base>
  --request <frozen-request>
  --computations <actual-source-directory>
  --linear-step-outcome <actual-step-outcome>
  --out <owned-base>/riccati-scalar-readout
```

它完整读取本 job 已存在的必要原件，核 descriptor 的 bytes/SHA；mode/cut/leaf/unpaid 全原行都在 Actions 解析，coeff/prepared/commit 仅作全流 hash/count，没有数值复核宣称。输出是**一份不超过 90,000 B（含 LF）的必要 JSON**，BEGIN/END 为 `REQUEST177_FINITE_HEAD_NECESSARY_SUMMARY`。GITHUB_OUTPUT 仍是：

- `finite_head_summary`；
- `finite_head_summary_bytes`；
- `finite_head_summary_sha256`。

不会再使用 multipart、编码或拆大 payload 重建协议。各 mode 使用固定27列紧凑数组，保原 frequency、started/complete、全 cut 隔零与商 flags、各实际分裂计数、错误、完整 DN 的原 dyadic endpoints、仅已合法部分的原 hull、末 chart/balance/sign、ratio/log 的原显示串、last-paid 和整原 mode 行 SHA。Ratio/log 只返回显示串的范围在 schema 明示，不能冒完整原 dyadic witness 已返回。

必要摘要还保全部 pending stack、source suffix、未启动范围、实际 last failure barrier 的原系数/初值/闭分母/误差和 transaction 身份。全候选矩阵、所有幅度步原数值、完整 scientific stdout/stderr 与大见证不作为返回数据；它们在 Actions 内按实际读到的全字节保身份/行数，错误只保选定必要原文与明确 excerpt/omission。原解析失败不改写成数学失败。

若原最终 result 不存在，reader 仍读真实已落盘必要流和异常身份；有多少实际范围就报多少，不能凑出112完整。若解析错误或必要摘要超预算，则退出非零并不写完成 marker。超限不是截断 trial/mode 或扩预算，而是明确必要读回未完成；不得因此主动删除未读 payload。

只有正常必要读回完成才写 `riccati-scalar-readout/readback-complete.json`，schema 为 reader schema 加 `-complete-marker`，绑定同一 job/source 和本次完整 readback index。它证明本文声明的必要摘要范围已读，绝不将未返回大阵冒独立逐值审计。

C、cut、deep far 的原独立小 block 仍保留，report 分别核原 SHA/schema 后打印；没有新拼成一个大总 JSON。工作流 report 的原成功/失败仅传播实际阶段与读回范围，不把 reader exit0 当完整 cut DN 成功。

## 8. 科学 CLI、固定工作策略与运行时输入

线性入口：

```text
python geometry_20261115_stored_C_finite_head_riccati.py
  --cover-directory <same-job-cover>
  --cover-result-sha256 <actual-cover-result-sha256>
  --far-directory <same-job-deep-far>
  --far-result-sha256 <actual-far-result-sha256>
  --code-directory <actual-computations>
  --proof <R375-proof>
  --precision-bits 256
  --budget-seconds <min(14400, startup-remaining)>
  --max-panels 25000000
  --free-bytes-reserve 2147483648
  --max-depth 32
  --local-defect-bits 12
  --panel-norm-limit 1/2
  --taylor-terms 24
  --max-geometry-cache-records 65536
  --out <new-owned-linear-directory>
```

两个 result SHA 由本次真实文件产生；缺任一不能借历史结果补填。运行 require_actions 约束仓库 `Rogerhu12/math-research-public`，原科学子进程无 GitHub token。

| 阶段 | 保留/明确工作参数 | Actions 硬 timeout |
|---|---|---:|
| 原 v3 连续 C | 256 bits、六 primitive、1440片、3600 s、200000 integral panels、200000 inverse nodes；原96/80/24 bit目标、100000 eval、depth48、query12、guard8全保 | 75 min |
| 原 cut 两 jet 读回 | 所有点叶原 dyadic hull，不添加宽度门 | 10 min |
| R312 全112深端 | port159、256 bits、原完整根族 | 5 min |
| 本 R375 有限头 | 14400 s 内部计时、25M面板 attempts、2GiB实际可用储备、原32/1/2/24/12策略 | 250 min |
| 必要线性/规则读回 | 单份90KB，实际错误/未付范围 | 30 min |
| compute job | 全链 | 360 min |
| report job | 原必要小块复读与 scope | 5 min |

namespace 18,900 s 是**启动时预算裁剪计划**：原 rules startup 之后，按本次实际剩余给 linear 的 budget；它不是 namespace 绝对 kill timer。科学源内部线性时钟始于输入 binding/runtime setup 后，setup 不计入该 14,400 s。真正外层硬限为各 step/job timeout。2700 s 读回余量也是资源计划，不是无条件保证；延迟或外层超时必须如实保为 partial。

初始化可清 runner 已知未用 SDK 临时资源并要求32GiB工作空间，这是明确工程资源条件，不是数学失败。线性 Budget 实际检查输出盘 free bytes；储备不足立即保原状态/stack/suffix后停止。25M不是完成保证；R358/368 的首停止条件不是大cap耗尽，本次提出的是表示变化而非仅增加预算。

## 9. Workflow、所有权、规则和清理

新 push trigger 仅为本 request；独立 concurrency，原156/162/168/169 workflow不改。唯一 owned base 为 `visible-stored-C-Riccati177`。其 casing 在入口、reader、cleanup一致。

Actions preflight对实际 request身份、17direct sources、query、全部原证明、README、所有 Python/Node/bash 来源做本次检查。原 public78 恢复只一次，原三个数据输入只恢复一次。这里是来源核与语法检查，不是增加科学验收门；本稿未声称本地执行过这些命令。

rules runner 仍是冻结3b8源，2700 s周期真实 pull/规则比较；其 mirror clone 位于 owned output外的 sibling临时目录。原stdout规则回执可读，不能把该动作写成本地 pull。原 science 启动 argv 继承162已修复的 exact token forwarding，不在 rules与owner间再插一个无对应 parser 的裸 `--`。

内嵌 owner helper 只作本 request namespace/进程管理，原精确 bytes/SHA 在 workflow 解包后核验：10,317 B / `6fa34de9499cab8248702f6d7f8e3b050666e35a3067dd8fd8335edc5dd82e9a`。它的修改限本独立 namespace/label，原专属 session/PGID、PID/start_ticks 和信号传播责任保留。父 Python可能继承 runner公共PGID，所以父仅以PID/start_ticks核；只有真正 setsid/start_new_session的科学组才按整个自有PGID确认停止。

读回前若无法证明相关原流已静止，fallback只保 owner原身份、必要错误和未读范围，非零退出，不解析正在写的科学流、不发完成marker。Fallback没有调用旧helper拆大输出；不得将活流SHA当完整文件身份。

主动 cleanup 必须同时满足 C/cut/far/linear四项真实读回 success、新完成marker与实际owner quiescence；只删除本177 namespace及声明的自有输入/恢复临时目录。任一失败都不主动删未读输出，raw仅随 runner销毁。没有upload-artifact、Release、raw Git发布；保留的公开内容仅源码、参数、run、输出SHA和必要结论。

## 10. 原责任不变与本次交付范围

R375 已支付条件性包含与全闭段存在证明。它不预言原完整系数盒一定在 depth32内被处理，也不预言112个完整cut DN全部隔零。实际运行必须给全部paid/partial范围；未启动、域不足、barrier分母未付、算术异常、资源耗尽与读回失败分开。

本请求没有新接受场，也没有原 $H$、native correction、$\eta=0$敏感度、338响应、FD、完整453 BVP或同g精化。旧32轮/10档/严格下降/$2\times10^{-9}$及所有metric、closed、reach目标均不在本次改写。最终任何新场仍须用其真实来源重新支付原目标责任。

本次 source-only交付包括科学源、必要reader、request、workflow及本完整接口；完整差异和静态文本检查回执只作临时审读，不将可重算大数据或重复fixture入库。R379保留为未来实际177结果号；此处不填真实run/source/result、任何分母隔零数或完成结论。
