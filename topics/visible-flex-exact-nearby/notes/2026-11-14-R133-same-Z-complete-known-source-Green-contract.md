# 同一连续 $Z$ 的完整已知源到原连续有限 Green 的消费合同

此消费者只重新传播已知源。原完整 6391 个连续 Green ports、5970 个 projector 格、全部真实界面及两端 source unit profiles 逐字节复用，不重新求 Riccati，不重新算 projector，也不重新算任何 body/cap 源格。

## 1. 三个真实完整输入

原完整有限 Green 来自公开 run 43601964129，native SHA256 为
`fd6c1f4baa4ec86aab08d4925a0ec9565c3791cbe470b77c2e41549d8f071de6`，
原 artifact process SHA256 为
`297cb4c9b8f58bbaacbcf1d0be594f43ea385420f8ea58fbb14e83bf84a63a1c`。
其科学源、core、worker、manifest 和全部科学门均按原身份验证。

新的 body 输入必须是全部 7721 行 mixed $Z$ 源的实际 finish，含 1147 个新紧支撑格与全部复用行，科学源固定为
`90c90fb1b21806e803e61d5f850b1d8057fcadc577452d3454b05348500a697f`。
新的 cut 输入必须是全部 1977 单列格与同 $Z$ 边界的实际 finish，含 1961 新格与旧 16 格，其科学源固定为
`103d4d0a05c41ffc3b14c45f72a1f1a07ee30869395e1676558ad5cd22f4dc64`。
两个 run 的完整 native SHA 由实际成功 process 绑定并记录，不能把尚在运行或失败前缀当完整输入。

三份输入必须使用同一 ac1 连续 M32 修补背景、相同物理 $\eta_0,\nu$，以及完整连续方向定义
`6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04`。
固定背景的 source 已包含真实 raw mean、中心修补差源和 $Z$ 的完整片内常量修补；两端也必须是相同 $Z$ 的来源，不能混用 $q^*$ 边界。

## 2. 原正 Green 与新的分布源

设一条原连续片 $I=[r_l,r_r]$ 的真实径向权为 $\rho$，其端值来自原准确有理数。该片在原 source 行 $i$ 内，新的已证 low193 来源满足
$$
\|F_Z(r)\|_{\mathrm{pair},L^2_\varphi}\le E_i.
$$
完整 weighted 方程 $y=\operatorname{diag}(1,\rho)h$ 给
$$
f_I=g_I=\max(1,\rho(r_l),\rho(r_r))E_i. \tag{G.1}
$$
使用完整 pair 上界给两个互补投影分别收费是安全的。独立 even mean 留在同一 193 态中；没有从 nonmean 源免费删 mean。

消费者按已核 signed Riccati 正 Green 合同读取每个原有向 port 系数，核整条 suffix 的无 pole 门、正分母、正跳分母和原腰闭合。新的 body 通道取 $z_R=0$，逆向以 (G.1) 传播 $z$，到真正 $0^-$ 后取
$$
p_0\le \frac{D_0z_0}{1-D_0\rho_0}. \tag{G.2}
$$
这里分母使用原已证的 `final_waist_closure_margin` 正下界，不把 $0^+$ 与原腰 frame 混用。随后按同一完整片和所有界面正向传播 $p$。

连续 $Z$ 的物理 trial 跳准确为零，所以新增体源通道的界面 affine 负荷 $a=b=0$。但是 projector 的 $P^-/P^+$ 角跳仍全部存在，每个 secant、tangent 和有向分母均原样消费，包括腰末端零长度跳。不能因为 $Z$ 连续就删除 projector 跳。

## 3. 两端真来源与保守非负余量

原两端 unit profiles 已按真实完整边界系统及 $L_0,D_0,L_R,D_L$ 计算。它们分别乘同 $Z$ 实际来源
$$
g_0,\qquad g_R=\|(g_{\mathrm{odd}},g_{\mathrm{mean}})\|_2. \tag{G.3}
$$
单位沿原证明的准确取消：$B_R(Rh_{\rm orth})=B_{\rm true}h_{\rm orth}$。因此 (G.3) 不再乘一次径向权。独立 mean 行和全部 96 个腰 odd 行保留。

为便于原证据接续，消费者还保留原 `known_original_trial_jumps` 的非负 profile 作为额外上界余量。这不宣称该原 raw/$q^*$ 跳就是 $Z$ 的真实跳；它仅给正 majorant 加一个已有、非负的额外负荷。因正 Green 比较，加入它只能增大合法上界。所有真实 projector 界面仍分别收费，没有把这项 surplus 当作忽略真实跳的理由。

四个相互可加通道因此为：新的完整同 $Z$ body 源、原 trial-jump 非负余量、同 $Z$ 腰来源、同 $Z$ 真实 cut 来源。旧的粗 body 源 profile 不再叠加，否则会重复计算同一已知残差；中心修补也已经包含在新 $Z$ 源中，不再单列重复收费。

## 4. 逐片恢复普通 pair 范数并积分

每个片上把四个通道的正界分别相加为 $p_\Sigma,q_\Sigma$，则
$$
\|h(r)\|_{\mathrm{pair},L^2_\varphi}^2
 \le \max(1,\rho_{\min}^{-1})^2
       \big(p_\Sigma^2+q_\Sigma^2\big). \tag{G.4}
$$
其中 $\rho_{\min}$ 取原片端值之最小，沿原权函数合同严格控制整片。使用原真实径向长度积分 (G.4)，分别得到整个 inner $[0,9/10]$ 与负区安全窗的普通 pair $L^2$ 上界；各通道的 $L^2$ 贡献也独立保存，方便识别预算实际由哪一项控制。

负区安全窗保持原精确上端
$$
R_{\rm phase}=\frac{2383968743003}{10000000000000}.
$$
所有原 ports 已在这个点切开。消费者若发现任一片跨过该端点，则失败，不能按端点采样代替完整区间，也不能把只付负区的结果说成整个帽的响应误差。

这个负区范数使用归一化角测度、完整 independent even mean。是否低于 $1/200$ 仅作为**有限 193 系统**的实际算术条件记录；尚未合上高反馈时，该条件不等于真正 PDE 响应门已通过。

## 5. 完整高来源和严格结论范围

body 的 known high $97\le j\le160$ ordinary pair 来源和 cut 的完整 known high 来源分别原样输出，不送入有限 193 Green 后就宣称已付全系统。任何 $H^{1/3}$ 转换、完整高解算子、低高反馈及实际 coupled response 仍须独立支付。原 cap 是完整 homogeneous 真帽定义，但只取其 low97 边界系统形成的有限主体逆，不能据此把未知 high 输入设零。

若新消费者成功，它只证明当前同背景完整 finite193 压缩响应相对于同一 $Z$ 的一个明确上界。它不单独证明完整 PDE 逆、真正 $q_\nu-Z$、非线性背景转移或真正参数 Schur。由于这次直接消费同 $Z$ 的源和两边界，**本条已知有限源证书**不再需要额外补一次 $q^*-Z$ 的费用；这一点不免除未知高反馈或其他背景费用。

## 6. 实际过程与数据保存

workflow 仅选择本公开仓库、main 上实际成功的两个完整 finish artifacts。若其中一个尚未完成，记录没有开始新数学；另一个完整 DAG 成功事件会再次触发消费者，不能把等待检查称为科学结果。

已经成功的同一输入 Green 来源消费，通过未改的数学身份重新核验后逐字节复用原 native，不重复传播。每十分钟依 reviewed driver 真实 pull 并检查两个 README。所有失败前缀、实际 child 退出码、真实 native 与完整 profiles 均保留。新 plaintext 摘要写出前逐件验证 UTF-8 字节数不超过 60000；大 native 保原字节并沿既有 lossless parts 机制发布，集成不搬运二进制。
