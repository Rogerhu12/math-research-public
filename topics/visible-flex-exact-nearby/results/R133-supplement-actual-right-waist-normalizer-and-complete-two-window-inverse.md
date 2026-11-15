# R133 补篇：实际真腰单侧系数、两个固定截断及同一归一化逆的双窗口

本篇登记唯一公开运行 [43763134339/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43763134339) 的完整实际结论。新科学 child 返回 $0$，20 个结构门全部通过；真腰的两个固定候选 $J=97$、$J_s=268435456$ 各四个严格测试全部通过。独立的充分 dyadic 规则给出 $J=512$，该行也保留完整四门。三个截断属于同一已知实参考族的真右腰 $r=0+$；本篇不把正截面处的归一化费用移到腰部。

原理论是 [WT](R133-supplement-waist-normalizer-coefficients-from-complete-one-sided-residuals.md)，原双窗口算子恒等式是 [TN](R133-supplement-strict-cut-two-window-normalizers-and-complete-strong-remainders.md)。本篇只使用本次 Actions 已保存的有向球，不在报告阶段重新执行科学算术。

## 1. 唯一实际运行和完整保存

部署 head 为 `7434228ac45d410812b3beee5ac2ac5d506f1884`，自动 push run 从 `2026-11-15T21:20:26Z` 开始，API 于 `21:21:08Z` 更新为 completed/success。job `132962167924` 的所有步骤均 success。worker 于 `21:20:54.252443+00:00` 开始，新科学阶段于 `21:21:01.120660+00:00` 完成；实际只有一个新科学子进程。

| 完整小原件 | Git blob | bytes | SHA256 |
|---|---|---:|---|
| [science](../notes/waist_normalizer_coefficients_ci/run-43763134339-1/actual-scientific-conclusion.json) | `b742d3167f68c05ef197450a3112eb5b8edcacac` | 27619 | `2a406e4506bb5a19646924e2072ec83d8806055a083ba7e1b1acfb9ab21d142d` |
| [execution](../notes/waist_normalizer_coefficients_ci/run-43763134339-1/execution.json) | `14739c6ccfd5134b3ad41b184e9fab81ddf83530` | 16607 | `571e0993583844079d0aad828cd2da093336761429551d1e25b88e912f40fcf7` |
| [worker report](../notes/waist_normalizer_coefficients_ci/run-43763134339-1/actual-result.md) | `016bdbeecd67fadb7643d6605e6479d28106c33b` | 7857 | `3ecbded80f4bbdb431f4cdd4340c87bc2a96cf9add3890e506db3cabbcd324b3` |

实际 source SHA256 为 `7cde6f7f6d03bbfa107a93abdd4ee925b332f47ac7c4a2257d6557e00927a393`，worker 为 `fbcedfe82d591421984d6fe459a60b596490b956a774ecab89603450cb624007`，manifest 为 `4cec7ef0ba21373190dd0bf142d10546823d46bb832a58df66529822990ad125`，理论原件为 `e4e317e896fade7dee1c93303ff8c9ed4c811d35b90cc6bc3ed3cecabdf30da5`。

完整 science 在任何格式大小门和 Git publication 前先原子保存并打印。预 publication science/report payload 为 35809 bytes，SHA256 `c466bd136dca3457f4b94af252eb707c6332708a3c059b7afe53104c3221680a`；用最终 science 原字及删除最后一次 publication README pull 行的 report 可逐字复原同一 hash。相邻 process payload 的打印身份为 14018 bytes、`fec6f20a6d36884da150308724aad94bcd72ff2439dde69a45663a1d9c259715`，留在 execution。完整科学输出没有因包装门丢失。

22 件小文本和四个旧历史字节件共 26 个输入的 role/path/bytes/SHA 均与冻结 manifest 对齐；四历史件的 commit 也相同。10 个 Python 文本的 AST 门通过。runtime 为 Python `3.12.14`、python-flint `0.9.0`，有向算术 320 bits。旧 producer、原 Fourier enclosure、原均值流、旧残差积分、CR、QR、Gram 和 Green 重算次数均为零；新数组 artifact/Release 均为零。

## 2. 同一参考族和右单侧原件

固定内禀参数 $\eta_0$（不同于特征速度 $\eta=-\gamma m$），使用完整连续参考
$$
Q_\delta=Q_0+\delta Z_{\rm can},\qquad |\delta|\le10^{-8}.
\tag{WTA.1}
$$
中心定义 SHA256 为 `440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47`，方向定义为 `6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04`。原物理角频率始终是 $4j$，保留原反射空间及两个独立物理均值。

D 已成全域值门 $7,6,19,83$ 只用作这两个固定函数的完整 Wiener 状态界。本次没有把 D 的 $10^{-10}$ 参数差费用扩大到 $10^{-8}$。较大实族和真腰的完整 $m,q,n_g$ 球来自原 SP 同族回执。原 SP 的族身份和腰部因子、原 D 的四个完整状态球在新 science 中均逐字复制，并已与旧 execution 比对。

旧 body 第一个自然件是 8201 bytes，SHA256 `feb3bbf9294dc995b88f5dc7c1e2ba866d3bd8c22dc84834dda7591cc9f644f0`，恰为 SP 已成功恢复的同一首件。body 与 raw7296 第 0 行的真实闭区间均为
$$
\left[0,\frac{7686143364045647}{36893488147419103232}\right],
\tag{WTA.2}
$$
原 scalar germ 均为
$$
\left[0,\frac{2609037194989121}{1152921504606846976}\right].
\tag{WTA.3}
$$
它们包含真实右腰且位于 $\nu$ bump 的支撑 $[1/20,9/50]$ 之外。这里 $F_\nu=0$ 是原支撑恒等式，不是舍去一个小源。

背景 raw7296 容器的三部分按原 SHA、字节偏移和整体 SHA 原样恢复为 4592623 bytes、`6f52030b7954f049a8e42a5a513a1f69b553819065b0c8b2245fa173e514cbb1`。完整 7296 行分割与 6143 个接口身份核验后，只取第 0 行保存的闭区间残差，未重做任何旧积分。两种 canonical repair 都是原 piece 上的常量，因此其右径导为零；修补后的状态值仍完整计入 $7,6,19,83$ 门。

| 原源 | 实际保存的有向球 |
|---|---|
| raw background $R_U$ | `[2.05750058807419822961826637385385611940000011589055329159374179262454526e-8 +/- 3.08e-80]` |
| raw background $R_V$ | `[9.01244023575352345138830944221156772590000015893911079890986619031080678e-9 +/- 4.55e-81]` |
| raw response 完整 nonmean | `[8.45911410560968393139665451698591120672000004080483447051301463649028450e-6 +/- 4.64e-78]` |
| raw response 独立 mean | `[2.37212132546713143482397301081351925770873047157401192210826790523812608e-8 +/- 4.98e-80]` |

原背景 residual 乘 $\alpha$ 恰一次；原 raw physical response 不乘 $\alpha$。response 采用 `uncorrected_response_nonmean.A0_sup` 和独立 `response_mean_residual`，没有用后来 mean-completed 的替身。

## 3. 单侧径导和完整 normalizer 系数

以 WT 的完整 moving PDE 与原 Wiener primitive $\|I\|\le1/4$，原 piece 常 offset 的径导为零，故保存的 raw 源直接给真实单侧径导。令 $M=7,P=6$，$b=|\beta|$，$B=b\max(1,|K|)$，$G=|\gamma|\max(1,|K|)$，则
$$
R_Q=bM+B(M^3+M^2P/4)+GMP+\alpha(R_U+R_V),
\tag{WTA.4}
$$
$$
R_Z=(169B+6G)\,19+(49B/4+7G)\,83
 +R_{\rm nonmean}+R_{\rm mean}.
\tag{WTA.5}
$$
同族右导界为 $R_Q+10^{-8}R_Z$。完整 $m_r=\langle v_r\rangle$ 随后进入 $\eta_r=-(\gamma_r m+\gamma m_r)$。$D_1\le B(7+19\cdot10^{-8})^2$ 使用实际 Wiener 投影收缩；它不是从一般 $L^\infty$ 投影界取得。$q_r,q_{rr}$、$W_r,B_r,S_r$ 和 $E$ 均按 WT20–26 保留，不只由腰部零阶状态猜径导。

下表是本次新组合的实际完整球；所有其他组成球与原 intrinsic jets 留在 science 的 `complete_waist_coefficient_bounds` 与两个原行 receipt。

| 字段 | 实际有向球 |
|---|---|
| `background_right_derivative_pair` | `[43.6623647661545321749230049495448531065569649045231359714068136168501553 +/- 3.28e-71]` |
| `response_right_derivative_pair` | `[721.898855869173538777180215870375584911344368297416510092266323326131386 +/- 2.93e-70]` |
| `selected_right_derivative_pair` | `[43.6623719851430908666583927213470118103128140179668189455719145395133886 +/- 5.97e-72]` |
| `eta_r_abs` | `[45.2981530611176689069935561599685504344453262079681869730482961776188263 +/- 1.91e-71]` |
| `D0` | `[0.00268484136692867766330942391751945656670067026814568797759440193321044643 +/- 2.24e-75]` |
| `D1` | `[0.0107393654677147106532376956700778262668026810725827519103776077328417857 +/- 2.90e-74]` |
| `S_star` | `[0.0554341146409436338579209817531159870016158509032190029195577495557667871 +/- 4.70e-74]` |
| `Sphi_star` | `[0.0332766745641705283129027678331592917429669059471838457609973990920011594 +/- 6.21e-75]` |
| `Sr_star` | `[253.720367998052961200175252994034202423772233532352464143360594471905774 +/- 1.67e-70]` |
| `E_star` | `[253.857525910324387876419960360072481104055105633392356120163042033422005 +/- 1.57e-70]` |
| `S2_star` | `[123.812846552682080530055342636577433438445265924987475513987523972518649 +/- 4.77e-70]` |

## 4. 两个固定截断与独立充分 dyadic

令 $P_J$ 为原 moving 角下的完整双 sign 高频投影。采用 WT/TN 同一有序归一化
$$
T_J(0)=
\bigl(1+P_JS(0)IP_J\bigr)
\bigl(1+P_JS_2(0)I^2P_J\bigr).
\tag{WTA.6}
$$
两个因子保持这个次序。同一个 $T_J(0)^{-1}$ 分别在 $L^2$ 和 $H^{-4/3}$ 有界；不是两个不同的解算子。第二因子的强余项通过原 $H^{-1/3}$、$H^{2/3}$ 中间窗收费。

四个实际严格比值如下，每个都是该行自身的完整有向界：

| $J$ | $\tau_{1,0}$ | $\tau_{2,0}$ | $\tau_{1,-4/3}$ | $\tau_{2,-4/3}$ |
|---:|---|---|---|---|
| 97 | `[0.000142871429486968128499796344724525739694886213668090213710200385453007183 +/- 3.69e-76]` | `[0.000822436274794625362220050899647793558284921789808876312001723907777916420 +/- 3.69e-76]` | `[0.0120183237660447514029315992506483994196229514858385199937715208330132678 +/- 3.23e-74]` | `[0.192854547219583905879257205182456933246365619953739958633465673781422382 +/- 1.71e-73]` |
| 268435456 | `[5.16270423689332174676665866310857115328459543205974650751405857091460257e-11 +/- 2.76e-83]` | `[1.07390525771225848099661144757572950185526132753528988634020572394167864e-16 +/- 1.68e-88]` | `[1.01299668617210338751097052446181352960416575642507588166947060081187231e-9 +/- 9.58e-82]` | `[2.97803616093941360665336006992607926458987736053869760318968412843030448e-15 +/- 2.67e-87]` |
| 512 | `[2.70674387895232587196879793716386655281327396988374037693153074002767515e-5 +/- 3.67e-77]` | `[2.95192829496102525067461353866046508403885998547047318253487405711456894e-5 +/- 3.73e-77]` | `[0.000812046924079927857371454173047525928793972640751983223513500986768129740 +/- 1.87e-76]` | `[0.00172631365328579912758284164889164019755556246225548140825508298097713264 +/- 4.07e-76]` |

因此得到：

| 类型 | $J$ | 四门 | 同一 inverse 的 $L^2$ 界 | 同一 inverse 的 $H^{-4/3}$ 界 |
|---|---:|---:|---|---|
| 固定 | 97 | 4/4 | `[1.00096612269379297817936401925742673552788148477445503005683433807057395 +/- 3.19e-72]` | `[1.25400510828652591141670567284938011296814631825019265910291449850087015 +/- 2.64e-72]` |
| 固定 | 268435456 | 4/4 | `[1.00000000005162714976212434574168267309450987447983775254451895627383971 +/- 1.98e-72]` | `[1.00000000101299966523442963090937318034346889981759512567447276505471203 +/- 1.45e-72]` |
| 独立充分 dyadic | 512 | 4/4 | `[1.00005658912487559660349064778091828440430961783754156279430886579368359 +/- 5.77e-73]` | `[1.00254341125907042785970011104589113163406039351091166806942781419773227 +/- 2.78e-72]` |

独立规则的 $512$ 是 WT30 所定义的充分 dyadic 选择。它并不声称为最小可逆截断，也没有覆盖两个固定候选的原结果；事实上固定 $97$ 已独立通过。

完整有限修正与强余项同时保留：

| $J$ | 首因子有限支持上界 | 两因子有限支持上界 | 首因子完整 finite 强费 | 完整 forward 强余项 | 同一 inverse 强余项 |
|---:|---:|---:|---|---|---|
| 97 | 288 | 672 | `[1.19799717764451335461906954895268267793953187530931247470457614619502245 +/- 5.09e-73]` | `[187.709933761138428870062137842950415306137445837155117646683593050075552 +/- 4.12e-70]` | `[190.189624722695650960921249661538382176888566668319062276029914052026293 +/- 2.37e-70]` |
| 268435456 | 268435647 | 268436031 | `[117.023111237886734421298860566901573746092660087755442710784036993127838 +/- 3.72e-70]` | `[0.00327438226436580828500666866443520314906180527611991833742102908210576056 +/- 2.16e-76]` | `[0.00327551054353549047673164798411679271670642990346779958828383330037921951 +/- 2.32e-75]` |
| 512 | 703 | 1087 | `[1.61303340671635978989372718965680221184947901562512373064942123670019675 +/- 1.94e-72]` | `[30.9180978096947815088353958945699586236325360066181189786392551009988176 +/- 3.56e-71]` | `[30.9533963070767230093933720267374515987666198307134332947262962074724015 +/- 7.96e-72]` |

支持上界以 quarter Fourier label $|j|$ 表示，物理频率仍为 $4j$。首项是 $J+191$，两因子是 $J+575$。这些有限修正不是零，也不能因 $J_s$ 很大而从完整 matching 系统删除。

## 5. 真实已付接口

本篇实际支付的是同一 known reference、真实 $r=0+$、原 moving 角下的 endpoint normalizer。对
$$
\mathcal Y_0=L^2_{\phi,0}(\mathbb C^2)\oplus\mathbb C^2
$$
可按原恒等式扩展为
$$
\widehat T_J^{-1}=\operatorname{diag}(T_J^{-1},1_{\mathbb C^2}).
\tag{WTA.7}
$$
完整低频补空间及两条物理 mean 保持身份。若接 [SF](R133-supplement-complete-strict-first-symbol-propagation-defect.md) 的实际试探，必须使用相同的 $J_s=268435456$。$T_{J_s}^{-1}PT_{J_s}=P$，故试探的 $P$ 仍留下；不能把它改写为完整 Id 后删去 mean 行。

接四个 waist receiver 时，真实腰部角变换和它的 inverse 仍按各自窗口收费，不能借 P22 处的角界。共同 root gauge 与共同输入 chart 是右乘因子，不能与本篇的腰部左 inverse 交换。PW 的七类独立输入端口、actual Poisson 内已有的稳定 trace、完整有限 head 和两条 mean 仍保持原定义。

本篇未证明区间 normalizer inverse、incoming/outgoing 逆、扩大 finite Schur 逆、未知 PDE 解或全几何闭合。$J=97$ 的成功只属于式 (WTA.6) 的真腰 normalizer，不自动支付实际 incoming 图的 $97$ 门。

## 6. 20 个结构门的完整实际结果

1. pinned public runtime and320-bit directed arithmetic：`true`。
2. same manifest source parameters and five complete mathematical inputs：`true`。
3. complete original D state conclusion and unchanged continuous definitions：`true`。
4. complete fixed raw-plus-repair state bounds reused without enlarging D parameter fees：`true`。
5. complete original SP waist conclusion and unchanged source identity：`true`。
6. same complete real selected family physical frequencies and two waist means：`true`。
7. same original body identity full raw193 response and complete dependency hashes：`true`。
8. exact original bodyrow0 bytes and prior SP successful restoration receipt：`true`。
9. complete original one-row natural part without requiring global completion：`true`。
10. true right-waist bodycell in original scalar germs and outside nu support：`true`。
11. exact complete raw7296 index and three original byte parts：`true`。
12. full original compressed raw container restored byte for byte：`true`。
13. same raw candidate amplitude nu and complete primitive residual object：`true`。
14. complete original7296 partition and6143 interfaces checked without new integration：`true`。
15. actual first raw closed row contains the true right waist and complete residual：`true`。
16. complete waist mean curvature and intrinsic-speed directed lower gates：`true`。
17. all four raw residual species finite with full response mean and one base amplitude：`true`。
18. complete right-waist wide coefficients finite with all radial and mean terms：`true`。
19. both fixed waist cutoffs retained and a separate complete sufficient dyadic test：`true`。
20. only new waist scalar combinations with old fields means and finite ports preserved：`true`。

所有原成功数学继续冻结。本次完整新结论已保存，后续消费者只读小回执即可。
