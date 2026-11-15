# Request181：原 C 完整 112 模态的 Prüfer 实角传播、取向 Robin 行与独立 DN 条件

作者：AI。日期：2026-11-15。本文交付独立源码及公开 Actions 接线；交付时没有执行科学计算，也没有假定 177、179 或本请求已成功。当前请求号为 181，未来实际结果号预留 R385。

## 1. 所解决的具体问题与完整范围

本请求从原配置、两份实际历史 ready、同一原 C 完整六积分和 R312 全部深根族重新开始。它将原 177 的有限比值坐标改成 R380 的完整实角 lift。这样，某个高度或通量分量经过零点时，不必仅因该比值坐标出现极点而停止传播。它不承诺区间宽度改善、全部 112 模态在当前预算内完成，也不把物理高度的零点责任移除。

全部频率为 \(m=2,4,\ldots,224\)，从深端口 \(F=159\)、物理节点 160 起。完整原 160×9 段、六 primitive、原根区间 \([1/2,2]\)、所有可能固定根序列、准确原配置 cut 和全部闭逆像叶保持。零宽共享端点仍归属于每一个相邻闭源片。连续模型是原 convention C，不是旧有限零 J，不是选定一条根序列，也不是新的非零 native 解。

新科学入口只输出原物理 \((u,k=dH/dr)\) 的完整线性族、逐候选取向单位 Robin 行及在条件付清时的线性 cut DN。它没有本次实际 native 的 \(\mu\) 字词输入，故不产生或猜造原 \((Q,\Pi)\) 坐标行。完整非线性尾响应、338×112 endpoint 响应、mean、物理审计、fullDN 和闭场接受均不由本实验支付。

## 2. 冻结运行文件与基线

所有文件为小文本，完整正文保存在公开 Git blob；没有更新分支或派发 Actions。

| 文件 | 字节数 | SHA256 | Git blob |
|---|---:|---|---|
| computations/geometry_20261115_stored_C_finite_head_pruefer.py | 93880 | 250474d748842d9b5423be2123460308ab16419d4b5dac1d8c9967fc208c0122 | e834b59333a34badf9b981ec1eb65cc20432b7bc |
| computations/root_20261115_pruefer_head_scalar_readout.py | 30300 | e020b7e98b190fd8fa62f0fe13dd14980117f8efe2fffbdf23d33bd479e9e257 | 46a0c3942782a4004bec0e201114960818b10e11 |
| computations/public-stored-C-pruefer-head-request.json | 28877 | dc8647bb25a7c12b6c70fa63a65b884044ffcc5dd960d9fdb0642b450555477e | e0702016f7300cdc9d7aaa9525ba1aeba4f9478a |
| .github/workflows/visible-larger-public-stored-C-pruefer-head.yml | 77785 | 9d2c9af83e83af835ec8d26a18b7a691cb0c7d1192b9344d4a3990948e1e9db7 | 59cfb03bd6a199405ee0007bb580178c36efa8a6 |

科学源的准确基线为原 177 的 geometry_20261115_stored_C_finite_head_riccati.py，84732 B，SHA256 34606e3fea2093f78cc3cb88fa6e5f7bcc32112c8f9053484628ad1a16e11124，blob 78d9a16784a9df5a23bedb73b0eea6850085f3f1。原源码不变，仍在新闭包中作为实际来源字节绑定；没有执行原 177 的比值传播。

原 request177 为 25668 B / 1c77c60028ec7bfc3798ff8ceb301f013c10b575ee3c42d055b2c3f209c36b58 / blob 86056b279ac8d988c2a336a7e4b823ac203e1b3b。原工作流为 76744 B / ef3cd2593e219e8be42977fdc14ab50da9d6d2d1ccae9e9a71a53b5d0c332c4c / blob 4c3aa3e1c6ae760c82a2cf49bcf258558e864ebb。本请求保原 17 个 pin，新增角源和必要读回源，完整 source_count=19。原全部物理输入、C 工作参数、原 far 参数字典逐项不变。

使用已完整证明的 R380，results/R380-continuous-C-Pruefer-angle-lifts-and-oriented-Robin-enclosures.md，19469 B / 8a51036fd130c80365284c2e4678c3aa765d177471b4d16df0f4c85add016fa9 / blob de13e3b3a1485861e486a63627c538cdb15905ec。R375、R347、R324、R312 和原 C 的 R286/R297/R306 来源仍显式保留。证明来源不是另一个实验成功标签。

## 3. 原 C 与深根族的实际输入

公开 Actions 按原 8bd267107cc8710d371f3b62c02986655ac965b0 历史 commit 恢复且核对完整原字节：

| 输入 | bytes | SHA256 |
|---|---:|---|
| 原 T112-config.json | 2161 | 01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5 |
| 原 closure ready | 109004 | 563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6 |
| 原 strong ready | 29774 | c1c44f2384845c25d2dcb0ec7127934fa46b54aa74613efcd6f9f6bcf0eb541d |

同 job 重算原 f12f7470… v3 六积分，原 query 1303 B / 4e59c69fae54045e100180e2d7576b848423a503394ff0b4dd87f6e219b7fd59 保持“准确 binary64 配置 cut 的点 query在前、原整个自然域 query在后”。没有读取任何已删 raw 的 hash 来恢复数值，也没有复用 177 的传播盒。

随后用原 fe66789e… far 源重新生成同 C、同 source/run 的全部 112 深端行。新 binder 验证当前 cover/far 的 producer、schema、run/source、完整输入闭包和全部原流字节。原 work/query/runtime 字段仅在数学对象比较中被排除；各实际字段仍保全，不丢实际预算来源。

输入 C 或深端未完整时，新角源保留实际 facts、原错误、全部未启动模态及未付 cut 范围，不能从 step 绿色推断已进行传播。原 cut 未完整或不在已付原自然域内也不虚造候选。

## 4. 新状态、原方程与初始完整族

原连续通量坐标为 \(Z=(u,j)\)，其中 \(j=wk\)。在原源参数 \(x\) 上：

$$
Z_x=
\begin{pmatrix}
0&D/w\\
m^2q/R&0
\end{pmatrix}Z,\qquad D=R_x>0,\quad q=w_x.
$$

这些系数完整来自原 GeometryCache 的同 C 范围，完整可能 cap 分支、原 primitive 双端半径包围和准确局部源长度不变。不额外乘一次 length，也不重施旧 \(\Pi\) 端口因子。

新状态为

$$
Z=\rho\,\operatorname{diag}(1,2^b)(\cos\phi,\sin\phi),\qquad \rho>0,\quad \phi\in\mathbb R.
$$

初始原 \(Q_F=1\) 保留为

$$
u_F=r_F^4,\quad k_F=u_Fs_F,\quad
\phi_F=\arctan(w_Fs_F),\quad
\log\rho_F=4\log r_F+\tfrac12\log(1+(w_Fs_F)^2).
$$

\(s_F\) 是完整原 R312 斜率盒，不取 midpoint、不选择子族。初始 atan 合法是因为原高度 \(u_F>0\)，整个初始角在 \((-\pi/2,\pi/2)\)。之后保存的是实角，不将其约化到主值区间、模 \(\pi\) 或模 \(2\pi\)。

对固定二幂平衡，\(\alpha=2^bD/w>0\)、\(\beta=2^{-b}m^2q/R\)：

$$
\phi_x=\beta\cos^2\phi-\alpha\sin^2\phi,\qquad
(\log\rho)_x=(\alpha+\beta)\sin\phi\cos\phi.
$$

正幅度只存准确 factor-chain 与 log 区间，不强制把可能极大或极小的原 \(Q_F=1\) 列整体展开。振幅有限但幅度范围宽不会自行变成“唯一真实列”。

## 5. 全局角比较与完整 Taylor 责任

每个完整闭 panel 的 \(\alpha,\beta\) 区间端点转换成准确有理数。下、上自治场分别为

$$
f_-(\phi)=\beta_-\cos^2\phi-\alpha_+\sin^2\phi,\qquad
f_+(\phi)=\beta_+\cos^2\phi-\alpha_-\sin^2\phi.
$$

两个角方程在整个实轴有界且全局 Lipschitz，不存在有限比值的极点责任。下解从完整 incoming angle 的下端开始，上解从上端开始；标量比较保留每个原可能根序列的完整轨道。

每个常系数场 \(A\cos^2\phi-B\sin^2\phi\) 通过

$$
H=\begin{pmatrix}0&B\\ A&0\end{pmatrix},\qquad
\gamma=\max(|A|,|B|)
$$

的完整矩阵指数推进原单位初列。原 taylor_exponential 正文不变：同时计算端点指数和 \(t\in[0,h]\) 的闭管，保全部级数及真实 remainder。原初列的 cos/sin 区间全部参与矩阵作用，不能仅给一个选中分量贴 tail。工作误差字段是 Taylor 截断界，不是全部输出 interval 宽度的上界。

新参数明确规定 \(h\gamma\le1/4\)。由 R380，

$$
v_0^\top e^{tH}v_0\ge e^{-\gamma h}\cos(\gamma h)>0
$$

在全闭段成立。源码把直接 dot 区间与此已证正范围相交，然后用 cross/dot 的 atan 得到唯一小连续增量，进一步与 \([-\gamma h,\gamma h]\) 相交，并加回原实角。atan 仅用于有正 dot 的小增量，不把整个角主值化。

上下自治角各自单调或恒定，所以端点包围还给全闭管

$$
\phi([0,h])\subset[\min(L_0,L_h),\max(U_0,U_h)].
$$

这里不假设真实变系数角单调。幅度率使用该完整角管和完整 \(\alpha+\beta\)，端点 log 增量为 \(h\Gamma\)，闭管增量为
\([\min(0,h\Gamma_-),\max(0,h\Gamma_+)]\)。

Taylor 工作目标未达时继续按原子分裂；到最大深度，只有已获得完整有效区间传播时才保留 valid-coarse。任何 coefficient/角 lift 包围异常、预算停止或不完整 transaction 都保留准确未付前缀、栈和后缀，不宣称数学反例。

## 6. 二幂换帧保全角 lift 与幅度

从 \(b\) 换到 \(b'\)，令 \(c=2^{b-b'}>0\)。新角是准确连续实 lift

$$
F_c(\phi)=\phi+\arctan\frac{(c-1)\sin\phi\cos\phi}
{\cos^2\phi+c\sin^2\phi}.
$$

分母的相关下界是 \(\min(1,c)>0\)；且

$$
F_c'(\phi)=\frac{c}{\cos^2\phi+c^2\sin^2\phi}>0.
$$

源码分别计算 incoming 实角两个准确端点的 \(F_c\)，用严格单调性保完整角区间。幅度增加
\(\tfrac12\log(\cos^2\phi+c^2\sin^2\phi)\)，在完整旧角盒上外包，相关下界 \(\min(1,c^2)>0\)。每次换帧都有原指数、准确 c、两端 lift 和完整 log shift 记录，全部进入 amplitude factor-chain。

换帧不要求高度或通量分量隔零，也不凭主值角挑短弧。因 log 与角可能失相关，区间可能变宽，但不丢原族。

## 7. 全部 cut 候选、取向单位行与 DN 的分责

原 associate_cut_leaves、源片顺序、零宽共享端点和闭交集算法不变。每个真实 cut 候选使用对应 whole-step 角管及同源正 \(w\)，令 \(K=2^b/w>0\)。原物理列除以正幅度后为
\((\cos\phi,K\sin\phi)\)，原物理 Robin 行除以同一正幅度为

$$
R=(-K\sin\phi,\cos\phi).
$$

其相关范数满足

$$
\|R\|^2=K^2\sin^2\phi+\cos^2\phi
\ge\min(1,K_-^2)>0.
$$

所以两个独立分量盒同时含零也不使准确行变零。源码将直接 norm² 盒与准确相关上下界相交，再先对**每个候选**形成 \(R/\|R\|\)。只有之后才合并不同候选的单位行盒。正 \(\rho\) 保证与原 \(Q_F=1\) 行取向相同；不把不同幅度的原未归一列直接 hull 成一列。

完整候选矩形 hull 本身仍可能包含零向量；这不否定每个实际单位行非零，也不提供可无条件使用的单个 Dirichlet 图。DN 必须另证每一个候选的完整 \(\cos\phi\) 区间不含零，才逐候选计算

$$
k/u=K\sin\phi/\cos\phi
$$

并合并全部合法商。存在未付高度条件时，单位 Robin 族与其完整空间覆盖仍可成立，DN 仍为 null/partial。不能由某个 interval 含零推断实际共振或非存在。

本独立入口没有 native far 的实际 \(\mu\) 字词。geometry 的 179 只有在实际 sample(r_far) 后才形成 mu_far 的原浮点字词并与最终 577 节点数组核同；它不是静态 core 键。R380 的原 \((Q,\Pi)\) 可逆变换仍是明确后继合同，此处不猜 mu、不套旧 J、不将物理单位行冒成原 native 行。

## 8. 原子提交、部分范围和不变函数

原 journal 顺序保留：所有区间运算、cut 行、DN/单位行 hull 和新状态先准备；panel/cut 原行先写；最后写 commit；commit 到 live state assignment 之间没有资源检查或科学运算。新单位行 hull 与原 phase/log、cut coverage、DN、计数一同提交。未 commit 的预备行不支付前缀，也不覆盖已接受状态。

正常末状态保完整实角、正 log 幅度、二幂、全 factor-chain；失败保 last paid、完整当前 panel 栈、后续 required panel suffix、所有未启动频率。下一个模态始终从原深端行开始，不将上一模态或旧 run 的传播盒重用为更窄初值。

纯文本比较确认 41 个原函数/类正文不变，包括原 JSON/descriptor 绑定工具、Budget、GeometryCache、矩阵 Taylor、associate_cut_leaves 和 pending_description。riccati_coefficients 只有函数名变为 pruefer_coefficients，数值正文相同。新的实质函数为角/正幅度换帧、全局角 barrier、advance_candidate、候选/初值记录和单位物理 Robin 形成；完整 propagate_mode 只接这些新状态及 transaction 内的 unit-row hull。

完整科学源相对原 177 的 diff 已给 blob 32f8d72fff70d914ba01bc2b8a75899e04ef7ff6，58256 B。新源整体不是原算法的逐字同一版本；它是 R380 已证对象的一次独立区间实现。

## 9. 实际 CLI 与预算

主科学 CLI 由 request 原字段逐项组成：

```text
python geometry_20261115_stored_C_finite_head_pruefer.py
  --cover-directory <same-job>/continuous-E
  --cover-result-sha256 <actual original result bytes SHA at runtime>
  --far-directory <same-job>/deep-far
  --far-result-sha256 <actual original result bytes SHA at runtime>
  --code-directory <fixed checkout>/computations
  --proof <fixed checkout>/results/R380-continuous-C-Pruefer-angle-lifts-and-oriented-Robin-enclosures.md
  --precision-bits 256 --budget-seconds 14400
  --max-panels 25000000 --max-depth 32 --local-defect-bits 12
  --panel-norm-limit 1/4 --taylor-terms 24
  --max-geometry-cache-records 65536 --free-bytes-reserve 2147483648
  --out <fresh owned namespace>/finite-head
```

C 重建仍为 3600s/256bits/200000 source panels/200000 query nodes，全部积分参数不变；原 far 为 159/256bits；新传播 14400s/25M attempts，精度和全部 112 范围不变。唯一相较原 177 的该数值参数变化是 panel_norm_limit 从 1/2 变为 1/4，以直接支付 R380 小段正内积条件。它是算法的区间步长条件，不是新增原 BVP 接受门。

工作流保持原 360min job，C step75min、far5min、linear250min、complete readback30min，以及预留 2GiB 可用磁盘和启动时 32GiB 资源检查。namespace 从创建时记 18900s 科学窗口及 2700s 读回计划；在原规则同步启动后，将 linear 的实际预算裁成 min(14400, namespace 剩余)。这个 namespace 计时是启动预算裁剪，不是后台绝对 kill；linear 内部钟仍从 source/input binding 和 runtime setup 后开始。真实硬限制是原 step/job 超时，读回预留不是无条件完成保证。

同原 runner 3b8b6d…，三科学阶段都保原 2700s 真实 pull/rebase/README 变化停止。固定科学 checkout 不随监控 checkout 改变。token 仅原规则父进程可见，数学 child 清掉 GH_TOKEN/GITHUB_TOKEN/MR_TOKEN。本工作流仍记录 owner PID/start_ticks/pgid；有 live/unknown owner 时不把正在写的流视为关闭，不清理它。

没有使用 177、179 的结果或成功标签作为前置，也不等待它们的数学结论。没有预填未来 run、SHA 或成功范围。

## 10. 必要完整读回与清理

独立 reader 按实际 result 描述符读取所有 mode、cut candidate、cut leaf、unpaid JSONL，并以原字节和整数元数据核完整计数。大 coefficient/prepared/commit 流只读全部字节/hash/count，不冒逐数值独立审计。

单份必要摘要保所有 112 status、实际完整 DN 的原 dyadic endpoints；完整 DN 尚未有时保对应单位物理 Robin hull 的原 endpoints；原实角/log 的 display 明确只是原 display；保完整当前栈、未启动频率、未付空间后缀、候选高度/商/单位行计数、原错误及其未导出正文范围。没有重新求积分、ODE、norm 或区间界。

每份必要摘要最多 90000 B，溢出明确 exit70/读回未完，不拆包、不把 raw 科学表改编码搬出。科学 producer 的 result、全 ledger 和 reader 的摘要均先在 Actions 临时目录形成并记身份。原 C、cut-twojet、deep 和新 finite-head 分别有独立必要摘要，不合成大 primary。

清理仍必须同时满足：四个实际读回 step success、本 source/run 的 readback-complete marker、所有原 owner quiescent。失败则明确保留到 runner 销毁，不主动删除未读 raw。只保脚本、参数、run、输出 SHA 和紧凑结论；没有 upload-artifact、Release、Git raw 或大数据分片。

complete-families、height-isolated、all-DN、readback-complete、procedure/step 结果是不同字段。绿色 metadata/readback 不能替代任何科学字段。

## 11. 本次交付实际核对与未付事项

实际已做：完整原 177 科学源/reader/workflow/request 文本读取；四个新小文本的 UTF8 bytes/SHA；完整差异；原 17 pins、全部三输入字典、全部 C 参数和 far 参数逐项保留；41 源段逐字一致；新 schema、CLI、19闭包、request SHA 两处、inline lifecycle SHA 两处一致。新 inline lifecycle 为 10317 B / 6d2b6e23efbe04feb4ed2202959e2c9c42ccf1470e8beb0ca34d1889f2aac354，只按独立 181 namespace/source 身份适配原 owner 逻辑。

没有本地 Python AST、编译、fixture 或科学运行。原 Actions source step 将执行明确源码/inline Python AST 和 bash -n 解析，之后直接真实计算；没有新增独立人工审批门。当前没有任何新数字说明 181 会收窄、会达到 cut、会证明 DN 或会改善 native。

剩余真实风险包括完整区间角/幅度相关性损失、C 系数盒宽、Taylor/atan 范围在极窄数值情况下未隔正、空间细分成本、全部 112 模态与同 job 资源、末 DN 高度条件及尚未提供的 native \(\mu\)。每项都沿实际原范围保 partial/unresolved，不用“角没有极点”替代它们。

本文和源码为可复现脚本/参数接口。完整 diff、纯文本核对回执及临时源码稿均可从这些公开源重新得到，不作为应永久存储的可重算数据。
