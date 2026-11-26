# 原 R53 的 λ=1 actual 场到固定问题：两种同场初始化

日期：2026-11-26。会话：Astra-held10-06bbeb39-20261126。

这是既有 R63 及现有源码的接口核查，不新增存在性、BVP 可逆性或收敛结论。
未执行新的 BVP/DN，也没有取得原 R53 的 λ=1/full-DN 新接受场。
本文的输入条件是未来某一**真正通过完整原 full-H/J/audit、最多八次外迭代及原 finite
门**的原 R53 设计返回；metric-only、线性前缀和零求解重表达不满足该条件。

## 1. λ=1 完整 R53 基线已经在工厂定义域内

`warm_supported_core_factory.make_factory` 第199–225行只要求
`curvature_blend=1`、`0<homotopy<=1`，没有 λ=.002 的限制。
它保存整个 `anchor_support_coefficients`，并允许传入实际
`anchor_baseline` 对象；后一分支核完整原 support 系数和 λ。
`SupportedIncrementCore.evaluate` 第148–150行在全部控制为零时直接使用
该 baseline 的 F/Ft/Ftt，不另拟合或截断基线。

v3 的 `make_factory` 第37–47行复用这一基线接口；v4 的 `_basis`
第100–106行在 λ=1 直接返回补弧基。因此，最终原 R53 的 λ=1 完整核本来
就是合法的零 phase 基线，不必先回到 .002，也不应标成 v5 来源。

三个零重表达入口及 v2/v3/v4 model 均无 .002 常数门。它们的限制是
mean1168、线性 DN、已验证的先前 v2/v3 零锚来源和相同锚 λ。
这些是现有执行合同，不能为接新 actual 来源而改写旧记录。

## 2. 两个不同的固定未知空间

设输入最终原 raw 参数为 p，完整实际核心为 Γ*，gauge 为 qg。
冻结整个最终 profile，特别是

\[
\delta_*={\tt physical\_profile.delta}+p_0
          ={\tt frozen\_profile.delta}.
\]

最后的等号须按实际记录核对；不能从更早的线性锚取 δ。

**路线 A：原 R53 support 未知族。** 保原 R53 factory 和全部圆化设置
λ=1、S、b、k。新固定参数的第0项是

\[
\widetilde p_0=\log(q_{\rm actual}/q_{\rm seed}),
\]

高项保持原 support 系数的同一 pscale 坐标。对原 fixed=False 设计，
q_actual=qg，通常该新第0项恰为零；不能把旧加性 δ 数值直接复制进它。
以后释放的是原 support 第一系数 q_actual，不是 phase d1。
`fixed_m3_branch_refinement.py` 第169–190行已有这一解码。

R63 已证明同一固定 a、角图和单位速核心空间中，support 系数可作为解未知，
不进入目标 g。它没有证明新固定问题的 Jacobian 可逆。
原 R53 `curvature_blend=1` 时 k 固定，λ=1 的准确材料圆弧也不要求固定
一次有限近似的所有 support 系数。

**路线 B：固定完整 Γ*，使用补弧 phase 未知族。** 将最终全部 support
系数和完整 R53 设置放入不可变 baseline，新 phase 参数全部置零。
旧高 support 系数已经进入 baseline，不能再把它们当作新 phase 值复制。
设置 qaux=qg，`d_j=phase_scale*p_(j-1)`；以后 d 是新固定问题的解未知。
可直接使用 v3 的补弧 geometry factory，λ=1 时不必再引入 v4 的设计同伦。

两族在这个零锚共享当前完整核心，但其有限未知空间不同。路线 B 不是原
support 空间的可逆换基，也不是 v5。首次 design→fixed 传递应明确为固定
问题初始化；后续精化才比较事先选定的同一完整问题。

## 3. 整个 Cartesian 场的保持条件

首先在同一 M 上传递，保留：

- 原 raw 的 x、Y、cubic，以及 physical 的 x/c；旧 artifacts 不改写；
- 原 literal chart_join、chart_reference_prefix、chart_breaks；
- 完整 angular_chart、qg、warp_reference、核心规范和全部 lift 规则；
- 原源定义的 literal mean 节点、integrand、primitive 起点和 BC normalization；
- 原尾完整背景、cut、有限范围、shooting 划分和固定闭合条件。

固定 δ 后的构造器可能自动选不同的径向 reference，必须恢复上述原字面图。
同 M、相同完整核心、相同 flow/gauge/lift/mean 定义给同一显式 Cartesian 图；
实际程序仍须在该最终输入上检查 raw RHS/BC/RMS、physical 六 jet、完整 metric
以及 cut H 和 full-H 包的真实绑定，不能只凭 d=0 理论签发 accepted。

原设计源 M40 的默认 mean 是1936，但实际记录优先。若后续升 M，固定序列
仍保这个 N_source，不能自动改为1168或16(3M_new+1)。审计角网格与定义
Cartesian 图的 mean 网格必须分开。

保存 prefix 与 tail 的原实际场不自动支付两者之间的 C² 接缝。原 generic
tail 的64M均值审计与 prefix 的 N_source 不是字面同一规则；该同场接口仍须支付。

## 4. 现入口的窄阻塞及可复用部分

`fixed_m3_branch_refinement.py` 第127–128行明确拒绝 actual 尾，且第203行
之后通过物理坐标重采样新图。它可以说明路线 A 的参数语义，但不能直接
作为 original full-DN 的固定精化 CLI 或无求解同图转换。

`warm_zero_control_reexpression_v2.py` 预设线性 terminal，并用线性 model
测 BC；v3/v4 又要求先前真实接受的 v2/v3 零锚。不能把实际 full-DN 源送入
这条线性链来制造新的“已接受线性来源”。

`warm_actual_dn_refine_model.py` 第18–21行只列 v2/v3，第47–58行只接受
既有 warm actual 两种 KIND，第81–82/96行硬限1168，第22–28行还保留
已接受 linear_source 身份。直接改 kind 或假造 linear_source 均不合法。

最窄适配是明确的 original-R53-actual 来源 gate 与 geometry specification：
绑定最终 run/raw/physical/full-H、实际 δ、全部原 support 基线及 N_source，
不附线性接受宣称。按路线 A 或 B 构造 fixed=True 模型后，可复用完整 lift、
真实 TailMixin/full-H 和原最多八次外迭代。首步把映射场当**未接受初猜**真求解即可，
无需先创造名义上已接受的重表达。若另作无求解重表达，则须保真实源 solver
provenance、solver_invoked=false，并使用同一最终 full-H 包重核非线性 terminal，
不能用线性 DN 代替。

原生尾 M≤64 的硬限制仍在；不能截断更高 M 来源。范围/mean/完整基线不变
也不自动构成 C² Cauchy 证明，既有实际精化与连续几何义务继续有效。

## 5. 本次核对的源码绑定

路径相对本课题。源码 SHA-256 在恢复环境中重新实读核对；未改这些文件。

| 文件 | SHA-256 |
|---|---|
| results/R63-fixed-metric-and-solution-core-variables.md | e60f2bedc9717aecb30f9ecd0f7b50650212dc72e55435237cee14c60f96a5aa |
| scripts/resume_transfer/material_flattened_support_core.py | 1d655f2bdad53e1d320c1115a9873abe399a9b7ba930722c415d02dedb9b1f20 |
| scripts/resume_20261126/warm_supported_core_factory.py | 9192499334d9f8603c812cd95964cc660a065132a82ce240fe2331f64c9b14dc |
| scripts/resume_20261126/warm_complement_core_factory_v3.py | 84380c0786e04ec87e5b6b17f766d88ce4626fab65ee8460badd99dcd42951f7 |
| scripts/resume_20261126/warm_homotopy_core_factory_v4.py | f303897c231639b2dd68854d7bf37cc8862eea4e52b468d5be84c856e84fbcb5 |
| scripts/resume_20261126/fixed_m3_branch_refinement.py | fa71d41534d17e543a27fa22fb8637d1b3ff08ef13b6d0c7db323ef2ea907297 |
| scripts/resume_20261126/warm_zero_control_reexpression_v2.py | e3e3520200124c0669c04ffcc618eb05785c7077fb7e23b2ca4b97383d67672e |
| scripts/resume_20261126/warm_fixed_m3_model_v2.py | 1fde1a0bbc064ad0167ee6d5eba5789392522abf679471455699bfa25b69e438 |
| scripts/resume_20261126/warm_fixed_m3_model_v3.py | ddf02e1a89013aaf369b3c3ef4a268b7b82e28fd246b8f071a7c45c561c5bcb8 |
| scripts/resume_20261126/warm_fixed_m3_model_v4.py | 5eb1a30dc861747bde158315b845a62bf666c32ad1b59a033daeafe41da7fabe |
| scripts/resume_20261126/warm_actual_dn_refine_model.py | 45195b5b2a80a509dbc1882cd8b92a52813c2984198fee61bdafc3f52b7dc3c1 |
