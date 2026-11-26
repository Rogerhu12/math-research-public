# R149 补篇：真实 common source4 到六个负侧与 incoming receiver 的执行入口

2026-11-26，visible-exact-astra-198c63d-20261126 / low_inverse。

本篇落实 [PN.10–17](R149-supplement-complete-positive-inverse-to-true-negative-and-incoming.md) 对 [CX](R149-supplement-common-high-WPN-source-unit-ball.md) **同一个真实 common 输入单位球**的消费。新增目标只有六个有向上界：实际低 root97、高 mixed root、完整 mixed root、负侧腰密度、两个有序左分支的联合观测以及 WPL 物理 primitive。它与十四个独立物理 port 的56量目标不同；输入一直是原 $X_{\rm fr}^{-4/3}$ 的单位球。

本篇给出已接好的可运行 owner、worker 和只读 metadata generator。目前尚无实际 complete32 前件，因此没有本六量目标的可执行 manifest、workflow 或 actual 数字。generator 必须消费完成的真实 source4 与实际58/224/32，才能生成入口。原科学失败、完整 false 门和未成前缀均按其原义保留。

## CXN1. 唯一源对象与真实根条件

源对象固定为
$$
x\in X_{\rm fr}^{-4/3},\qquad \|x\|_{\rm fr}\le1,\qquad
(F_x,e_x)=
\left(V_0\Phi x,-(V_{0,R}\Phi-B_R^H\Upsilon)x\right).
\tag{CXN.1}
$$
$\Phi,\Upsilon$ 已含同一个原右 $N_i$，本消费者不再乘 $N_i$、$\Lambda$ 或其 norm。这里的单位球是已定义实际线性算子的定义域，并非捏造一个 particular $x$ 的值。

原 source4 的18个槽完整保存：common 槽为1，另外17个是此列的独立数据恒等零。这不将状态诱发的外端 mean 置零。真实
$$
\Pi_{\rm even}e_x=-\Pi_{\rm even}V_R\Phi x+\mu_R\Upsilon x
$$
完整保留在原 $D_0$ endpoint193 球中。

根据实际 Volterra 身份 $F_x(r_*)=0$，本物理列的 prescribed root-even96 是 $c_*=0$。对 [L.24](R141-supplement-both-WPN-rows-by-exact-WOB-source-lifting.md) 的一般 $L^2$ 辅助变量，仍有
$$
w(r_*)=-E_cc+E_dd,\qquad c=E_c^*e_x.
$$
$c$ 一般非零。原 lifting 与本列的 $F_x(r_*)=0$ 恢复的是
$$
a(r_*+)=E_c c_*+E_d d=E_d d .
\tag{CXN.2}
$$
消费者没有把 $w(r_*)$ 当成 $a(r_*)$，没有对任意 $L^2$ 的 $F$ 或 $a$ 取 trace，也没有将 auxiliary $E_c^*e_x$ 错设成零。独立 high baseline 没有放入此次 strong correction；rough baseline 的原 window 不由本消费者升级。

## CXN2. 六量的完整公式与原32行的映射

令 $P,T$ 分别为原 source4 正式 whole record 读回的上端：

- $P$：`actual_source_complete_WPN_pair_rhs_upper`，同时控制原有限 WPN RHS；这是原 body/end193 联合 norm 的上界。
- $T$：`actual_source_original_radial_tail_rhs_upper`，控制原24480格正交投影的完整 radial tail。

只使用这两个原名；不以 comparison155 或认证1424格替换原24480投影，不从一个 norm 上界减去另一个上界。$P,T$ 属于同一个 $x$，不能以它们来自不同标签为由作输入正交。

从实际完整32表读以下原行：
$$
U_{f,d},U_{t,d}\quad\text{对应 }\texttt{low\_root97},\qquad
U_{f,z},U_{t,z}\quad\text{对应 }\texttt{high\_root\_mixed}.
$$
它们来自原输入顺序 `finite, tail`，全部16个输出名称与32个完整 record 的顺序在准入时核对。high mixed 行已经付过真实 mixed window 转换及原 output9，不再乘9。

新的前两量为
$$
D=U_{f,d}P+U_{t,d}T,\qquad
Z=U_{f,z}P+U_{t,z}T .
\tag{CXN.3}
$$
这里对同输入的有限与 tail 路径使用三角不等式。之后的四量为
$$
R=\sqrt{D^2+Z^2},\qquad
W=C_RR,\qquad
B=B_{H,0}K_{W,0}W,\qquad
L=\frac{B_{H,0}}{\sqrt2}W .
\tag{CXN.4}
$$
$D,Z$ 在下式使用前，分别先写 candidate 整件、读回验证、提交正式前缀；$R,W$ 也依此完成后，下一量才能读取其正式 upper。$R$ 的平方和只使用真实低／高 Fourier 输出块的正交性，且低 Euclidean norm 支配原低 mixed weights；并没有假定两条 source 路径正交。

$C_R$ 是已成 SP/PW 同族 full mixed-root 到完整腰密度的 gain。此 common correction 的负侧 ordinary 与 impulse 源均为零；原 negative 源列与独立新 $\nu$ ordinary 小目标没有计入、重算或删除。

精确六条新 record 顺序为：

| 新 record | 其真实对象 |
|---|---|
| `common_high_physical_low_root97_upper` | 真实根 odd96 与独立 scalar mean 的低 Euclidean 上界 $D$ |
| `common_high_zero_baseline_high_root_mixed_upper` | zero-independent-stable 返回的高 mixed-root 上界 $Z$ |
| `common_high_true_full_root_mixed_upper` | 同一 correction 的完整 $H^{-2/3}\oplus H^{-1}$ 根上界 $R$ |
| `common_high_complete_negative_waist_density_upper` | 原圈两 primitive 分量加两个 physical means 的完整腰密度上界 $W$ |
| `common_high_left_normalized_joint_two_branches_upper` | 同一 $x$ 经两条原左输出 receiver 后的联合 $L^2$ 上界 $B$ |
| `common_high_WPL_physical_primitive_upper` | 原 WPL 完整物理 primitive receiver 的 $L^2$ 上界 $L$ |

$B$ 同时控制每个分支，但不另付两次 $\sqrt2$。具体顺序仍是
$$
U_{\mathcal H^{-1}}\mathscr J_+\widehat T_0^{-1},
\qquad
U_{\mathrm{Rot}^{-1}}U_{\mathcal H^{-1}}
   \mathscr J_-\widehat T_0^{-1}.
$$
同一个 $\widehat T_0^{-1}$ 先作用，随后作分支选择；$K_{W,0}$ 使用原固定 $J_s=268435456$ 的完整两-window inverse。两个 density means 在 $\widehat T_0$ 中保持原 identity，并由 $W$ 联合控制。WPL 使用其原 physical receiver，因此 $L$ 不再乘 $K_{W,0}$；$1/\sqrt2$ 由 $\sqrt{1/2}$ 的 directed upper 实现，不能用 $1/(\sqrt2)_{\rm upper}$。

## CXN3. same-selected 身份的完整准入

执行文件是：

- [owner](../scripts/fourfold_codazzi_common_high_negative_receivers_owner.py)：整件 admission、六次新 scalar 运算和逐球保存读回。
- [public worker](../scripts/fourfold_codazzi_common_high_negative_receivers_public_worker.py)：只在公共 Actions 运行，完整读取当前输入，检查规则、容量和结果并发布。
- [metadata generator](../scripts/make_common_high_negative_receivers_manifest.py)：只读真实完整前件；前件不齐时只返回 readiness，不生成可执行 manifest 或 workflow。

owner 的 `admit_complete_inputs` 在导入 Flint 前完成下列实际连接。generator 调用同一个函数，没有另一套更弱的前件解释。

1. 完整 actual58、224、32 及各自 execution/manifest。每个 run/attempt、完整 record count/order、原 source SHA、整件 publication receipt、full success branch 逐项一致；224/32 的上游引用必须是本次读取的同一58，三者的 low、D、high 整件引用也相同。原 ε 或对称部 resolvent 的 provenance 继续由已成 physical chain 保留；本入口不另造低逆门。
2. 完整 source4 science/execution/manifest。固定 source4 owner/worker 的已审 SHA 与定义，四量和18槽资格全部保留；同一个 $D/S$ 实际文件还必须逐字等于 positive gate 的 $D$ 引用。source4 的全部 whole-input 索引与其 manifest 完整一致。
3. 原 source4 的 whole NIF 文件再次完整读取；其原引用 `input_sha256.wx_execution`、完整 accepted WX file path/bytes/SHA256/git blob、实际 run/attempt、source 和 manifest 身份，必须与此次 whole WX execution 完全一致。因而 common 输入与两个左输出 receiver 确实使用同一个 selected $\mathcal H$；只比较对象名称或写一个 same-selected 布尔量不够。
4. 源 selected identity 的 centre/direction、$\eta_0$ 与 NIF 的真实 selected 参数范围，必须落在已成 SP/PW 的同一 full real family 内。原 reflected $X_{\rm fr}^{-4/3}$ 与 ambient signed high 空间不被混同。
5. 完整 SP/PW execution 中的 embedded science 与所有 gate，完整 WTA actual/execution，完整 WX execution。四个负侧 gain 的原球在 PW 的复制必须逐字等于 SP；本目标只消费其中 root gain。WTA 必须是上述固定 $J_s$，两 mean identity 与四个实际 strict tests 全部成功。
6. 原 source4 的 proof、pure common definition、完整18槽接口和 NIF 的 exact immutable bytes 再绑定。只调用 common definition 的 metadata packet 重建函数，以核18槽和17个 exact-zero 证据；不调用已经完成的 source4 数值 producer。

source4 的正式科学 kind 仍是 `complete_actual_common_high_WPN_source_stage_v1`；本六量的新 kind 为 `complete_actual_common_high_negative_receiver_stage_v1`。新 result kind 为 `complete_actual_common_high_WPN_to_negative_receivers_v1`。原 source4 的 `common_high_strong_addition_size_proved=False` 完全保留；只有新六量实际全成，新的 result 才能在自身 kind 中声明此 strong-addition norm 已付。

## CXN4. 运行与完整保存的边界

metadata generator 接受实际 `--source-result-dir`、`--source-manifest`、`--wpn-result-dir`、`--wpn-manifest`。它从 WPN manifest 找到确切 gate/ports 文件，从 source manifest 找到原 NIF、proof 和两个 pure interface 文件。没有对应全件、完整前缀失败或实际 gate false 时，不写新可执行入口。实际 source4 和32齐备后，给定新的 `--manifest-out` 与 `--workflow-out`，它才产生单次 Actions 定义。

新源文件与 proof 动态按完整当前 bytes/SHA256/git blob 入 manifest；原 source4 的 owner/worker 与接口保持其既定身份。当前新执行规则固定到已审 Nov20 receipt，根 README SHA256 为
`581402c2148ee8c4ee2af741198ab54a56d71de2b5a7b0d0edf65359121cb102`，
topic README SHA256 为
`81249053c4c14a7a14289b58184e1b81601146d412fa117973f7a1d05bf95220`。
旧 manifest 中的历史 rule receipt 不被修改。新 worker 每次 pull 检查两 README，并按原规则记录所读提交。workflow 的安装命令采用 YAML block scalar，避免 `--only-binary=:all:` 中的冒号被 YAML 误解析。

科学执行固定 Python 3.12.14、python-flint 0.9.0、320 bits，六个 upper 以70位 decimal ball 完整保存。每条新结论都依序：

1. 形成 whole candidate scientific document，完整保存并重新读取；
2. 用 Arb 核 saved ball 包含最初的 directed upper；
3. 验证通过后，才将同一 bytes 提交为正式完成前缀；
4. 后续公式只用正式 saved ball 的 upper。

若核对失败或进程在 candidate 阶段中断，旧正式 prefix 不声称该条完成。后继既不读取缩写浮点显示，也不自行夹紧一个不一致球。完整六量只在全部成功后标 `complete/proved=True`；任何失败保留真正已验证的前缀。

worker 的消费 marker 绑定真实 source4 与 actual32 整件以及本精确参数，防止同一个新目标自动重复执行。科学只运行一次；metadata admission 与不可变全件读取不是重算旧目标。保存结果没有数组、artifact 或 Release。实际 push 遭 non-fast-forward 时按原规则立即 pull --rebase，再检查 README 后重推到成功。

## CXN5. 本次成功后真正获得的输入

六量完成后，原 common $\Phi/\Upsilon$ 列对真正 incoming 的 strong addition 已有原 $H^{-4/3}\to L^2$ 以及 WPL 尺度的实际上界；它可以按原顺序加入已保留的 rough/genuine baseline，或进入后续完整 finite/high block 估计。它无需再次经过十四物理 port 的输入归一化。

这些新量仍是 unsigned operator bounds，不能恢复 signed96 矩阵条目，不能替代原 target $\mathcal B^{-1}$、transported $\Theta_{96}$、高低交叉块或真正 $\nu$/phase/physical mean Schur。独立高 baseline、negative ordinary/impulse 输入和 nonlinear residual 的实际贡献继续使用它们各自已成定义。新 result 对完整 incoming 逆、真 Schur、nonlinear background、闭曲面及 topic completion 全部保留 false。
