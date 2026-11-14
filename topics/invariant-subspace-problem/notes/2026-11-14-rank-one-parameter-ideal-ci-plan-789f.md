# R150 剩余有限异常集：参数域原理想证书入口

日期：2026-11-14 UTC。作者：normal_annihilator / Astra-ISP-789f。

**当前状态（迁移新规）：本课题已迁入公开 math-research-public，现直接使用本仓库自己的 Actions（根规则13）。旧跨仓库代跑 runner 和 ci-queue 不恢复。§3仅为旧投递历史；当前workflow见文末。** 尚无完成的 Gröbner/lift 结论。

本地入口为 `node topics/invariant-subspace-problem/notes/2026-11-14-rank-one-parameter-ideal-runner-789f.js --out /tmp/isp-789f-r150-q0 --characteristic 0 --coordinates original --algorithm slimgb --stage lift`；有限特征另用输出目录及32003。

## 1. 准确目标

已读原中心十七式、$A_y$ 全参数秩分类、泛参数有限 $\Sigma$、逐点小投影秩界、源点四及 $P_\pm,E_8$ 数域证书。所有 $\operatorname{rank}A_y=8$ 的均值及无穷远均已另文关闭。当前只需处理 $g\ne0$、$\operatorname{rank}A_y=9$ 的可能有限异常点，不能从已闭 $\operatorname{ess}T_3\le3$ 支持分类越界。

直接计算全部 $4354$ 阶子式的 gcd 并非唯一入口。若能给九个横向平方在原十七式理想中的显式参数域表示
$$
z_j^2=\sum_{i=1}^{17}c_{ij}(s,M)f_i(s,M),\qquad 2\le j\le10,
$$
且准确提取这些系数的公共分母 $D_*(s)$，则所有 $D_*(s)\ne0$ 的有限参数已有原特征零证明。剩余待算集合可改用 $D_*$ 的根；它不必等于已有最大子式 gcd $\Delta$。分母若只含已经分类的因子，即关闭当前全部有限余点。

## 2. 原输入及降低参数次数

新入口 `2026-11-14-rank-one-parameter-ideal-runner-789f.js` 只调用已发表的原整数系统生成器及可选原二项式平移。每个样本先乘回全部保存的 `scale`，恢复固定 $\det J_3$ 倍原式，再做整数 Newton 插值；只约去一个与参数无关的整数内容，不除任何参数多项式。

原未平移 $M$ 坐标中，十一条 $N$ 的参数次数至多十、六条 $\Gamma$ 至多五，所以只需 $s=0,\ldots,10$ 重建。九个目标使用准确逆二项式横向坐标的平方。平移坐标选项仍保留，可用于另一项算法尝试，其已证参数次数界为二十五。

最初仅作生成检查时，运行 `--generate-only --coordinates original`：约 1.5 秒，重建后在 $s=-1,11,12$ 的全部 $3927$ 个固定倍式系数均准确相符，生成的 Singular 输入为约 174 KB。该初始检查本身没有启动 Gröbner；后续本地与本仓库CI执行状态见文末。

## 3. 已停止的旧跨仓库入口（历史，不再执行）

第一项建议直接求特征零证书，命令只含通用计算参数：

```sh
sudo apt-get update -qq && sudo apt-get install -y --no-install-recommends singular && node topics/invariant-subspace-problem/notes/2026-11-14-rank-one-parameter-ideal-runner-789f.js --out "$OUT_DIR" --characteristic 0 --coordinates original --algorithm slimgb --stage lift
```

可并行开一项有限特征发现计算，将 `--characteristic 0` 改成 `--characteristic 32003`。它只用于了解标准基和可能分母因子，不能提升成特征零分类。每项建议 `timeout_minutes: 350`。

程序先计算原理想标准基，检查九个目标余式，再调用 `lift` 并准确检查 $I C=T$。随后从所有证书系数取分母，移到单参数多项式环求 lcm，剔除已经分类的 $s(s-2)(s+6)P_+P_-E_8$ 因子，输出剩余分母及因子。最高十六式已由原 $J_3$ 唯一解回，输出不遗漏任何原低梯度。

`receipt.json` 记录实际完成标记、原数据及稳定输入哈希、精确身份检查结果；输出证书和标准基压缩后保存，超过仓库单文件限制只保哈希及可复现入口。`denominator.sing` 给下一实际数域任务。若没有 `R150_DONE_EXACT_MEMBERSHIP` 及准确身份检查标记，不能把运行解释为完成。

## 4. 解释边界

只有特征零、全部九个实际原理想身份和其实际分母都得到后，才能做专门化覆盖。有限域标准基、若干整数参数的成功、算法未报错或一般参数下的零余式都不替代这一证书。若残余分母非平凡，仍须逐个不可约因子处理或改取另一证书减少分母；不能从分母出现即宣称存在额外临界点。

Singular 的 `lift`/`liftstd` 采用原生成元变换矩阵语义；参照其官方手册及源码文档：<https://github.com/Singular/Singular>，`doc/reference.doc` 中对应条目。这里只有通用计算接口，没有调用不适用于原系统的文献分类。

## 5. 后继参数域覆盖

如实际分母有额外因子，可用不同坐标/项序产生第二份原生成元证书，并按[逐目标 Bézout 拼接](2026-11-14-rank-one-certificate-open-cover-789f.md)取共同未覆盖根；该代数接口不预判任何当前计算结果。

## 本地执行恢复（2026-11-14 06:34 UTC）

官方通用 Linux 压缩包 `Singular-4.4.0-x86_64-Linux.tar.gz` 已在本环境用户可写目录解包，`Singular --version` 确认为4.4.0。来源：[官方用户目录安装说明](https://www.singular.uni-kl.de/public/pages/singular-download/109.html)、[官方二进制目录](https://www.singular.uni-kl.de/ftp/pub/Math/Singular/UNIX/)。保持包内目录结构，未改变系统包权限、代理或TLS。

本轮二进制位置 `/tmp/isp-789f-singular-runtime/singular-4.4.0/bin/Singular`；以临时 PATH 前置后运行本稿既有特征0命令，输出 `/tmp/isp-789f-r150-q0`。工具输出/receipt必须检查后才能判为完成；工作目录临时文件若失去，按上述官方来源重新解包，再从仓库脚本重放。有限域32003任务后于06:43 UTC启动，Singular子进程限1 GiB，输出 `/tmp/isp-789f-r150-p32003`；它仅供发现，不是特征零证明。

## 本仓库自有 Actions 与本地失败回执（迁移后）

根规则13现授权直接运行本仓库六课题的计算。新增 `.github/workflows/invariant-subspace-r150-parameter-ideal.yml` 以本工作流/原runner的路径push或手动触发，两个矩阵任务分别特征0和32003，单次计算330分钟、整任务350分钟。只用本仓库源，不读取或代跑其他仓库任务。工作流精确调用同一原17式入口；输出保存到本题 `notes/r150-actions-789f/<run>-<attempt>/char<characteristic>`，并保留30天artifact。

输出回推使用进程环境中的Actions token；每次实际pull先比较本仓库根/课题README的原始指纹，变化则保artifact交当前会话读取新规，不盲推。非快进立即rebase重推；所有同步检查提交号写入该次输出回执。凭据不写文件。压缩/5 MB限额和重建哈希继续遵守根规则8。

本地特征0实际从06:33:51至06:46:36，在 `R150_BEGIN_BASIS` 后异常结束；`exitCode=null`、无完成标记、无原理想身份，具体终止信号旧runner未记录，不能确定原因。[原始失败回执](2026-11-14-r150-local-q0-incomplete-789f.json)已保存。新runner开始记录子进程终止信号和临时输出位置，CI结束时可保尚未完成的中间输出，但任何这种文件都不算已证明证书。

## 失败分支恢复与当前调度（2026-11-14 07:30 UTC）

原运行43568673309的32003任务于07:19:38记录运行器收到shutdown信号，进程退出143；保存/上传步骤被跳过。原因未知，不能据此认定OOM。公开job日志的哈希、准确错误行和源提交保存在[中断回执](2026-11-14-r150-ci-p32003-shutdown-789f.json)。同运行的特征0任务保留继续执行。

当前工作流改为明确选择特征、原/平移坐标和算法的 `workflow_dispatch`，不因每次维护workflow或runner就重复启动两项长计算。失败的发现分支下一次取32003、translated、slimgb；原十七式仍由同一可逆二项式换元给出，没有删方程或改变数学目标。现有3927个额外整数系数重建检查同样通过，生成式170219字节（原）及392204字节（平移）；后者横向线性项恰九变量，切向两变量的线性项为零。该结构选择不预判计算能否完成。

为使下一次运行器中断仍有输入证据，昂贵计算之前先上传输入重建回执/规则指纹，并把实际计算输出同时写日志和公开job流；每45秒记录Singular进程的内存/存活状态。只给Singular子进程12 GiB虚拟地址上限，给16 GB运行器保留进程服务余量；这不改变精确多项式输入，失败依旧按不完整处理。原lift身份与实际分母判据完全不变。

## Git push 的明确请求入口（手动API不可用）

本次 `workflow_dispatch` 实际返回403：当前PAT不能访问该手动调度API。未重试同一受限API。仓库内容写入和已有本库push工作流路径可用，且根README13已授权本课题直接使用本库Actions，因此当前以本题 [请求记录](2026-11-14-r150-ci-request-789f.json) 的一次Git push触发。只有该文件变更会自动启动；维护workflow/runner本身不会产生重复任务。

选择步骤读取同一提交中的明确特征/坐标/算法，只接受现有选项，计算步骤仍调用原runner和原证书判据。本次只重算32003平移分支，不取消旧特征0任务。计算前artifact、资源心跳、12GiB Singular上限和完成/不完整回执机制不变；之后由实际run状态登记运行号。

当前恢复运行已实际启动：[43572522972](https://github.com/Rogerhu12/math-research-public/actions/runs/43572522972)，源提交f4d370049b6631a11b4cc24281c51504aded9f46。选项步骤成功、特征32003平移输入artifact已上传，实际原消元任务运行中；未有完成证书。

## 2026-11-14 08时段：恢复运行实际失败

恢复运行43572522972已完成：有限素数32003、translated、slimgb在12GiB地址空间限制下于07:55:15明确报`Singular error: no more memory`、`halt 14`。其[实际回执](r150-actions-789f/43572522972-1/char32003/receipt.json)与[心跳/错误日志](r150-actions-789f/43572522972-1/char32003/execution.log)已由本库Actions自动回存；未生成任何有效成员证书或分母。原43568673309特征0在当时继续，最终状态见下一节。此失败是该实现配置的内存障碍，不能推目标不在理想；后续需要改变代数消元路径，不重复同配置展开。

## 原特征零运行的最终故障记录（08:13:51 UTC）

再次查询确认43568673309/132368030036已于08:13:51失败。实际check注释是hosted runner与服务器失去通信，具体原因未知；不能据此认定OOM。job日志端点现返回HTTP404/BlobNotFound，计算步骤元数据仍停在in_progress、后续保存上传pending，未观测到有效原I*C=T证书。[状态与准确注释回执](2026-11-14-r150-ci-char0-lost-communication-789f.json)保源提交、时间及请求结果。两条旧分支均已结束；后续改代数消元路径，不将失联计作数学失败或重复同配置大展开。

## 原生常单位预基与有限模新请求（2026-11-14 10:00:26 UTC）

[原生预基完整证明](../results/R150-appendix-native-constant-prebasis-and-original-module-reduction.md)已实际完成原F31[s]全部3333常枢轴行，保存可回放原行操作；参数次数≤10，受限6.039秒。完整95 MB基在另一个60秒/512MiB进程实际载入Singular并核完所有单位主项。大基只在临时目录重建。

新增本库专用 `.github/workflows/invariant-subspace-r150-finite-module.yml` 与明确请求 `2026-11-14-r150-module-ci-request-789f.json`。本次只请求31/annihilator/constant+native-f31，原生60秒/512MiB，余模Singular1800秒/4096MiB；源17式/6188行/九目标和原行身份判据不变。读取预基前匹配原数据/profile/基哈希，仅允许未专门化F31[s]。源输入先上传，实际回执/有限输出回推本题并记录逐次README指纹；大基不上传。

当前仅请求提交，尚待实际run号；Ann和九目标成员证书仍未得。有限特征仅发现，后续全复参数结论仍需char0原行lift及实际分母，不以素数结果替代。

实际运行现已启动：[43583257344](https://github.com/Rogerhu12/math-research-public/actions/runs/43583257344)，源`934582f3f9cdba01d64cfe35b215bd05082624fe`，创建10:01:17 UTC。启动时状态in_progress；最终实际结果见下一节。

## 43583257344 的实际正常形超时（2026-11-14 10:31:37 UTC）

[原始回执](r150-module-actions-789f/43583257344-1/char31/receipt.json)记录exitCode=124、status=failed-or-incomplete，运行1800秒，无完成标记、无准确原行身份。[实际日志](r150-module-actions-789f/43583257344-1/char31/execution.log)已到CONSTANT_PRECONDITIONER_READY，未到REDUCED_COMPONENTS或BEGIN_BASIS。因此完整3333预基加载成功，实际阻塞在reduce(M,B0)/reduce(T,B0)正常形阶段，尚未进入1034分量标准基。[CI outcome](r150-module-actions-789f/43583257344-1/char31/ci-outcome.json)的step_outcome=failure、complete=false；工作流continue-on-error可能使API步骤conclusion看似success，不能改写本次数学状态。

后继改为原生分层正常形，使用已证明的2195条原来源压缩，保完整F31[s]系数和可回放常单位行操作。先作≤60秒/512MiB的有界探测；不再次运行原30分钟Singular reduce。最小Ann和九目标证书尚未得到，有限特征结果仍不能替代特征零覆盖。

## 全部原生正常形完成，改进余模导入（2026-11-14 10:51 UTC）

[完整新附录](../results/R150-appendix-native-layered-normal-forms-for-all-original-parameter-sources.md)和[实际全量回执](2026-11-14-r150-native-normal-form-receipt-789f.json)保2195原来源、九目标、全部1034分量、最高参数45次。实际54.8127秒、地址空间上限512MiB，原前向DAG哈希不变，新增同次数常反向DAG和全部正常形来源轨迹；原式FC+B(hJ−HC)=hT已写全。

有限模runner新增`--normal-forms-file`并比对所有原来源/映射/哈希，仅允许F31[s]未专门化annihilator，避免错误复用6188列lift。本库workflow新增native-nf-f31模式，可从全量NF直接进入std，运行器差异下原生阶段设120秒/512MiB；本次请求文件没有变，不会自动发起长任务。

198MB逐向量表达式在一次60秒/1GiB导入探测中只到BEGIN_NATIVE_NORMAL_FORMS，没有完成导入；std未开始。原NF已完成无须重算，下一步从同一33MB紧凑系数文件改导入格式，保全部参数系数、来源和物理目标。
