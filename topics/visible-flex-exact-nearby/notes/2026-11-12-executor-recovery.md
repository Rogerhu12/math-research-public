# 2026-11-12 执行环境丢失后的恢复与重算登记

visible-exact-astra-f6a2。**主目标未完成；继续研究，不以本登记收尾。**

## 1. 已恢复的持久基准

约 07:46 UTC，执行环境整体更换，原仓库、未推文件与所有长任务会话
丢失。最后已核对 HEAD=origin/main 的本题推送为
`f064d89654c5b1becd9e0ffdb90af2229fc88306`，包括 R52、R56、R57，原图
tight root/实标量/对数/局部复图表，原图与 D5 的全核心 target 类型，
原图 MP Taylor 诊断，以及两步实际 ODE/J Newton 的旧对象包。

重新从 main 稀疏克隆后执行显式 pull，得到
`57bcb97e751faa449a74eff8bdb5783b064182e8`。根 README 与本题 README
相对已读 `1606f62b0538521bfe7c90c60a0dbd95f443ef87` 的差异为空。
规矩已读号已更新进 HANDOFF。当前 numpy、scipy、flint 可导入。
各并行者仅编辑本题各自文件；git 同步仍由 root 统一执行。

## 2. 必须重做的未推结果

下列旧 SHA 与数值只用于追踪丢失工作，不是当前可审查证书。源码若
可逐字恢复，先核 SHA；否则明确新版本，再完整重跑。任何严格数值
报告必须由实际运行生成，不能从对话摘要填回 JSON。

### A. 原 sym 对象的完整根 collar

owner：independent_audit。

- 原输入 `type_fixed_step02_analytic_smoothing_inputs.npz`：
  `bd9b4d14b104183f80feaeea4c4c1a5d8c40b511bd58974dbca1bda842474532`。
- 旧 `fourfold_phase_beta_interval.py`：
  `d23c4c5531e2d12deefb1bc93634b25d00417ecbf526e74298efae51e88ad277`。
- 旧 full-collar JSON：
  `7f8dc9e5539e05554b05dbac10b6ea77e8188a9e0030178fdc3ad0ae05967015`。
- 真根以 Arb 区间 Newton 收紧；固定物理 cut 为
  `1072423152036779/4503599627370496`，径向 Taylor 阶24，R=.0006，
  归一 x=4θ 的角宽 .02，2048角节点，192 bits。
- 丢失前完整 collar 位于 `(1305.4032588258,1305.4032592152)`；
  径向余项约1.946e−7，角均值误差约9.57e−14。**这不是完整 β。**
- root 已审查旧数学与源码，并独立重组25个系数球/两类尾；重建源码
  若改字节，必须重审对应差异与重新计算，不授予旧数据认证。

恢复入口 `scripts/fourfold_phase_beta_interval.py --help`。保留无限
primitive/E 尾、真实 R37 全零阶项、准确根 deflation，先完成同一
原图 collar，再付 `[0,cut]` 的连续 bulk。bulk 旧工作未完成，只看到
单点 Arb 与有向 binary64 包含及腰圈小段界；整段不得继承。

### B. R58 与准确仿射第二步对象

owner：constructive_route；point root 由 reproduce_newton 供应。

- R58 旧正文 SHA：
  `3370da60050c37a44b4023a3d87dab097d48b07280cc1ccc7db70a8b384c5977`；
  旧 mixed-jet 源：
  `e49cb20f250301f47930ae269026a4016bb866ccd92ea94869fc7dde6a24b34b`；
  旧 JSON：
  `61ad0ac5dfcd3fe8da9e8ccde31b49ecacdc8be139e724920d169d8d896ec5be`。
- 使用 R57 同一准确 affine 家族 `c(δ)=c0+δv`，而不是逐点 rounded
  控制向量；`|δ|≤binary64(.01)`。根的一阶、二阶隐函数公式与退化商
  `Q(s,δ)=−K0(t(δ)s,δ)/(1−s²)` 的参数二阶界均须重新生成。
- 第二步准确参数
  `δ2=−15291006546051/9007199254740992`。
  原点输入 `0d17500ac49c845b402145c4d0a48170b7163ec0d7e6ed6f0eedcc1c649ca59b`；
  方向输入 `8db5d57d65ea49cfe3a0df250714392300c98feeb2e0de2774aacbb4764d89ab`。
- 旧 exact symmetric geometry 源
  `e155840d8de8a75ca3abcdeaae152e4afd769f0c1e836dab705ca2a9203be707`；
  旧 exact-affine runner 源
  `795b8e5327792220313f33ea7c58501da0a218a3c2c38cefbf804fd5707c1fba`。
  新恢复代码如不同，则明确新 hash、同数学对象。
- 旧 object JSON SHA
  `ad970d3b25a392c4627ca75e8db99c1ed19e735c2779d28b7d9ff4eb10502b57`；
  258点、每块43点、DOP853 tolerance2e−9；全部 dense 段保存准确
  binary64 `t_old,h,y_old,F` 与 accepted 时间/状态。
- 丢失前首块43点两腿完成。旧 forward142段 gzip SHA
  `d533a3c009b6cfb57676b8221742d0018dfae2817c1a736a7b14e5fca78a8e0f`；
  backward177段。其余258点任务中断，全部缺失分支重跑。
- 旧 rounded/mirror uniform129 和 staggered129 虽完成，不能当准确
  sym affine 返回。旧错位误差 `7.88466e−5` 仍是否决记录。

### C. D5 affine 实连续输入包

owner：reproduce_newton。

以下三个源可尝试逐字恢复；报告须实际重算。

| 源 | 原 SHA256 | 结论范围 |
|---|---|---|
| fourfold_phase_affine_root_point.py | 3227cb85a8153a1860384ece21fb2e262a8cb88da9fd24f59b3e3ddef75eebd3 | 准确 δ2 真根的区间 Newton |
| fourfold_phase_affine_target_type.py | 8acf9d7c89e7a80028d1efae565dcab962b4e7f56b5226bbd99d4b7d1ca3205e | 全 affine 参数、全核心 target K0 仅±t |
| fourfold_phase_affine_scalar_gate.py | 2b1fc7dd1ac47da22669ecf46f1dd1f75d3b8f372560eca4c00ddd68e12a0e65 | 全 affine 参数的 Fz/r、Fx,z、area |

旧 point-root JSON
`c2cfad858f64a0082d131eb492993c6a237ab249220dfe61593323c8d1cdfeeb`；
旧根 binary 区间 `[.23839687378106797,.23839687378107466]`。
旧全 target JSON
`96ffed8f00e574701472dc9af94451549beab261a98a0ba5c59c37d373af7336`；
172个 accepted 闭 span，准确有理覆盖。旧 scalar JSON
`d59cddb24b41f0d3862472785ad14da428b07b91944b065349c107486afb6c8c`。
完整 support/h/ζ 程序中断，最后看到50/169单元通过；**无完成报告**。
恢复后从头算；随后才组装该族 ground-state/log/复图表，不能从原图搬值。

### D. R59 移动相位 frame 的宽复角门

owner：root；reproduce_newton 独立代数与实现审查。

旧新源 `fourfold_phase_modulus_characteristic_strip.py` SHA
`6eec35d4153c3c7cfaff4fc8c1be8e465022152b466f89d4061775804d1c9d75`。
`n=−a²(PcQ−uv)`；边界上有向计算 ReP，用周期条带调和最小值原理
控制内部，结合 c/Q/v 的复包络给 **模长** 下界。
物理 θ 宽1/64、整个 R57 独立控制盒。10个关键单元 probe 已通过；
完整592单元任务仅看到500/592通过便丢失，**不存在完整证书**。
重建后全跑，并保存所有失败项；不能把新模长门称成 Re n<0。

旧直接 Re n 二阶门在1/128有31/592失败、最大上界约.12244；
该失败原因仍保留。新 moving-frame 公式的11个符号恒等式已由独立
源 `fourfold_phase_frame_algebra_check.py` 审查（SHA
`a97ff3ccdea1104bb8cdaaa6a510f2abd9795feebcb1854066f9f7583e2de15c`）。
新连续场分母门也不能替代真实返回、参数二阶或全频误差。

### E. R60 与 dense reference 的准确小预算

R60 已重建正文。旧 SHA
`d42242494e8dc5b5d036d005bf80fb5167996c3dfc08b8e1eb0156c9afa71fb5`。
它是依赖实际 `e0,e1,B2,fp,fzp,fpp` 输入的定理；这些输入仍欠。
旧审核指出每段 reference 必须连续，真正跳跃单列费用；重建稿已明文。

旧 `fourfold_dense_reference_weights.py` SHA
`71e237b34c29435c3f857b14ba06562c469c665ebd16022b24ebb32b35a8a252`。
对每个准确 DOP853 多项式的 log-J 做 Fraction 仿射坐标变换和 Bernstein
包络，取 `q=exp L>0`、`q′/q=L′`；不把 q 当真实 Jacobian。
准确 dyadic H 文件仍在已推基准，SHA
`58375d24a99ba0f43b29143fe22f950a6e74e4fec2b94123d68b078fcf088260`。
旧首forward q界约 `.5486313774..3.702298599`，初值 H/4 费用
`<3.897835e−17`，均需对恢复的 trace 重新算。
旧准确 endpoint jumps 第一腿最大 θ/logJ/p 总量约
`1.56e−20/8.24e−18/3.39e−21`，第二腿
`0/1.14e−17/4.24e−21`，同样重新计算。

### F. D5 MP β 诊断

已推 `fourfold_phase_beta_taylor.py` 可重放：D5原点输入，MP50、Q256、
角512、G12、degree8/12、η=1/2048。旧运行约1222秒，β约37.0259215，
只是诊断，不是区间，不属于新 δ2 对象。旧报告丢失，按实际命令重跑。
原图约36.801611的已推诊断保留；两图不能混用。

## 3. 保存策略与当前缺口

先提交可审查的源码、证明及恢复说明，再运行长任务；完成的数值块
单独冻结并推送。超过1MB的纯数据 gzip，每文件不超过5MB；Markdown
不超过100KB、HANDOFF保持10KB以内。实时进度、未完成报告、pycache
不混入完成清单。每次 pull 检查两 README diff，至少每小时一次。

下一步是重建并验证这些实际输入，继续真实返回/完整β/参数KAM、完整
低模反馈与 ordinary-source 逆、真帽、Killing匹配、定量非线性收敛，
最后在同一个精确闭嵌入族上支付固定H、5%位移、δE与reach。任何恢复、
离散诊断或条件定理都不满足 README 的完成标准。
