# 中心 $C_0,D_0$ 与 symmetric $J_0$ 的同一有限密度身份链

2026-11-12，independent-audit。读源基点
93bbc1b548afd86ace4f397b545476172d370eb1。
本篇核对的是已经实际执行的选择器、累加器和保存输入的来源链；没有在失联环境中重新读取、解压或比较全部大二进制系数。

## 1. 两条计算共有的准确 g0 选择

小文件

    data/phase_ring_continuation/step5_complete_flow_ci_43301401638/parameter-input-selection.json

实际保存 complete=true，g0_index_sha256 为

    4174c3edde41f5c8ab12b036d4760c20ec987e475158aa2855ea08158ff7cb45

并记录中心索引

    data/phase_ring_continuation/step5_complete_flow_ci_43301401638/center_index.json.gz
    e6159a89b7f26c875d916138076af51f582dd24370b701ee9fe14603a9605585

与 uniform 索引

    data/phase_ring_continuation/step5_complete_flow_ci_43301401638/uniform_index.json.gz
    2b27ebc85cd593a1c72041e25dd7cc8939cc6db7a90d16ca095824407dcbb24b

都含 555 叶、550 个完整段。其实际生成源是
scripts/fourfold_ci_complete_parameter_flow_v2.py，SHA256

    b451f9b92c6ef69c242161e887890fc69133fecaba010c841ce0512199400e9b

该源的 build_indices 不是比较总费用后接受，而是：

1. 从已完成的 g0/index.json.gz 逐项建立唯一的
   (segment, Fraction(left), Fraction(right)) 选择，并核每叶文件 SHA。
2. 对前 32 段恢复的原始选择和以后各已完成 block，要求参数项的 g0 SHA
   等于此 selected g0 项的 SHA。每个准确时间子区间只允许唯一匹配。
3. 对每一项调用 validate_parameter_report(path, selected_g0_path,...)，
   再核参数报告全部 dependency SHA、准确参数、固定参考、条带及时间接缝。
4. 输出中心和 uniform 索引的每一行，直接写入 selected g0 的路径与 SHA；
   不从参数报告复制一个未经比对的 g0 声明。
5. 完整遍历到准确 $\pi/2$ 后才保存 complete=true 和
   original_mathematical_validator_applied_to_every_leaf=true。

validate_parameter_report 位于
scripts/fourfold_parameter_density_cover_efficient_v4.py，SHA256

    62ec86efa70ce9e2ebd1c427e524cd35bb97f99b69db93c5b0f8d337f7dfea00

它核 reference_certificate_sha256==sha(selected_g0)，并核完整
reference identity、几何参数盒、三个条带和需要的参数阶数。
因此中心参数输入与原完整 g0 索引逐叶绑定，不能只由总 local fee 相等代替。

## 2. 首积分的生成不是另选的 g0 近似

实际参数流水线调用

    fourfold_parameter_local_integrals.parameter_local_from_g0_norms

该源 SHA256 为

    4a24cba92bac0b0e025ec9d208907feae9aa4bee2ca1e2ec02036d2b9a979cd7

它执行：

- 读取 g0_report.first_integral_file；
- 核保存文件 SHA、完整 reference/source identity；
- 将保存的全部 Fourier 球系数直接作为 first[0]；
- 只对 g1、g2 计算新的首积分；
- 返回的 local[0] 和 local[1] 准确为零，保留的是参数二阶 $2J(g_1,g_1)$；
- 原 g0 local J 仍完整进入 remaining_local_J0_J1_J2_fees[0]。

已读的以下保存版本都调用此同一 helper，而不重新构造另一个 g0 密度：

| 参数源 | SHA256 |
|---|---|
| fourfold_parameter_density_pipeline.py | 4114fd9e82772fd58107b2adfd0905c230e937062d5a969d9ce874f14f1ed4ce |
| fourfold_parameter_density_pipeline_l2_v2.py | 7268d4fb5e751bb7a5491f361d665277d8ba89e75f7ccea4c8e253346d07e05a |
| fourfold_parameter_density_pipeline_l2_v3.py | 613e8c97fbc7b66dac3983212996eb093fb019dd755ebae0775a25e7e24169ef |
| fourfold_parameter_density_pipeline_efficient_v4.py | 7cd6b61fed53602353e0d18f9ebee8a5f9942b8244fb35b3fb6b37757730df3e |
| fourfold_parameter_density_pipeline_efficient_v5_initial.py | 77d6b1caf1b0898222aa2840c61431d5d7fdca1d70e5285243f5cfc5a823b852 |
| fourfold_parameter_density_pipeline_efficient_v5.py | bee932df5c1d63860a900898cf0b9f288c49462361d08fbf0545bd900ff340fb |

更早的完整 rectangle 入口也只从同一 g0 报告的
density_exact_rectangle 重新读取准确系数，并检查 coefficient_digest；
其首积分仍是相同有限密度的准确积分。本次不依据未经付费的新采样或拟合。

## 3. 两个零阶累加器的准确递推相同

scripts/fourfold_forward_density_cover_v10.py，SHA256

    cce56487c244a0f5823edc85835cbe9124c9df0f04afc1fa4117531f3db7c1ff

的 validate_saved 读取同一 first_integral_file，核其 SHA、identity 和
density_coefficient_sha256，然后按准确时间顺序调用 add_ordered_segment。
对每叶首积分 $G_\nu$，其数学递推为

$
 C^{+}=C+G_\nu,\qquad D^{+}=D+(G_\nu)'C .
$

scripts/fourfold_parameter_density_accumulate_v2.py，SHA256

    2c8f3799bfb41b7cb8d5f44364bbf72ed44dc1fd8eb7e5d58f710c627f635f17

先逐叶核 g0_report_sha256、reference_certificate_sha256 和
R82_local_inputs.same_g0_certificate_sha256 三者一致，然后读取
first_coefficients、retained_local_second_coefficients，调用
advance_parameter_integrals。其零阶部分准确是

$
 C_0^{+}=C_0+G_\nu,\qquad
 D_0^{+}=D_0+(G_\nu)'C_0+J_{\nu,0}^{\rm retained}.
$

上一节给 $J_{\nu,0}^{\rm retained}=0$，所以两者的准确有限多项式相同：
$
 C_0=\sum_\nu G_\nu,\qquad
 D_0=\sum_{\mu<\nu}(G_\nu)'G_\mu.                         \tag{I1}
$
全部正负频卷积、常数模和积频率均保留；这里没有额外物理角因子 4。

两条实现可能以不同精度、括号顺序产生不同的球端点或球中心；不需要这些
JSON 字节彼此相等。它们围住的是 (I1) 中同一准确有限函数。
原 endpoint 的 coefficient_selection_fees[0] 以中心累加器的球为准，
完整支付其准确 dyadic 中心与 (I1) 的差。

## 4. symmetric J 正是这个同一序列的局部补项

已运行的

    notes/2026-11-12-ci-local-J0-symmetric-summary.json

绑定原 g0 index SHA 4174c3ed...，以及

    data/phase_ring_continuation/step5_complete_flow_ci_43301401638/g0/ordered_accumulator.json.gz
    52fb2fa12b20f02e3aed3e7a2fbbe36e64586ed264080d05dda19de9aba3b0fd

生成源 scripts/fourfold_saved_first_local_J0_symmetric_ci.py 的 SHA256 为

    cde8f8d49e7d3af519ec504d2b000a07c3bfde3b49dd4f3e2c7df86a49a9c3b4

该源先核 accumulator.identity.leaves==index.leaves，
再对每个实际处理叶核原报告 SHA、其首积分文件 SHA、source 的相关函数
AST 相同、以及首积分的 density_coefficient_sha256 与原报告一致。
对实际处理的 330 叶，它准确补入
$\tfrac12(G_\nu)'G_\nu$ 的全部 Fourier 系数；225 个未处理叶保留完整旧费。
被减掉的是旧显式正预算中的已证下界，而不是拿两个函数范数相减。

因而本次 split-Wiener 可以保持原有限 $C_0+D_0$ 完全不变，将
$
 J_{\rm total}=\sum_{\rm processed}\tfrac12(G_\nu)'G_\nu
              +J_{\rm brackets/unprocessed}
$
看成相对于 (I1) 的同一真实误差。完整 symmetric correction 的 Wiener 范数与
剩余 bracket/未处理费是原条带 $3/1024$ 上的费用。
不需要也没有把 improved_W 的系数替换进旧 P0 或预 Newton。

## 5. 已执行证据与范围

同目录 execution.json 真实记录：

- g0 cover_v10：returncode 0；
- parameter-input-selection：returncode 0；
- center-chronological：returncode 0；
- hybrid-chronological：returncode 0；
- 当时 actual-endpoint 最后因旧 R31 预算未通过返回 2。

原 execution.complete=false 被原样保留，不能改写成整个旧运行成功。
随后 fourfold_ci_inspect_complete_flow_v2.py 核完整 artifact SHA 和所有输出
inventory 字节，确认 g0、center、hybrid 的 complete/whole_forward_leg/550段，
并保存真实 endpoint 的 complete_true_center_return=true、
complete_true_uniform_parameter_box=true 与 actual_R31_accepted=false。
其小 summary SHA256 是 f25a3692b36390b3ae8dd7699d4e0ec0c2e74561ac238b11352f1d532a8bfc52。

因此本篇的身份结论基于已执行的逐叶选择器和保存的来源证明，
不是只核总 fee 或抽看一个相同零模。它不声称本次失联期间重新计算了
全体 C/D，也不支付新 R31 的数值门或任何 PDE 逆。
