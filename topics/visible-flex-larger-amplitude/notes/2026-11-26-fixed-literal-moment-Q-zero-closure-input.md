# 固定18个字面 moment-Q 参数的新零闭合输入：实际15–16与完整入口

日期：2026-11-26。状态：**完整输入/算法应用说明与已返回的数值证据；新输入的场求解尚未返回，未证明根存在、等距、reach 或课题完成。** 本文不另登记R683/R695已有一般隐式与约束结论；只说明这次实际诊断支持了什么改变、完整源码怎样实现、哪些责任仍属于新输入。

## 1. 实际证据及其边界

来源是公开 Actions [45820592817/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45820592817) 的[第4卷实际阶段14–16](2026-11-26-public-actions-45820592817-1-part-004.md)。原初始参考包为
0f0424cc7403d0ffbca22490fc9d0bc154c52c356278a800553528e77fc386c1，
完整初始自由点为
cd530c070cfa54f122f19fe16e9b312e360f93e072496e445d1cc6c36973c0b3，
固定标量度量身份为
6ffc1f7fc1e6196318dc27da22b6c9ffda3ee64e81223a4c815f6348cf5baebb。

阶段14的完整闭角覆盖满足本初点的全弦长必要条件；它不构造零闭合场。初始高度仍为实际二进制值
0x1.f27228dabd944p+0，即1.9470544370684175。阶段15没有改这个高度、任一core/omega自由量、目标度量或根政策。

阶段15由完整源 trace_zero_initial_endpoint_failure.py
（22440字节，SHA256
73193414b094c05c9d8ce1dd033aab6a18446a88a5d7c4a6f352fcbcd966fb54）
实际重新执行原前8个角的根预算；只加入只读观察，原根方法AST除观察外相同。输出 zero-initial-endpoint-trace-first/report.json 为116138字节，SHA256
26b094fef8baf6ff2ecdda5d1a0f5a8be7383e5171733320be959a22d83cb47e。
其父失败报告SHA256为
4341323c805a3e4f38c20c6e5264e9875b8b717082793ece982c029f488ed744，
原零闭合模型身份为
29f540c6fc265b977a388813dcd0d3faddfd48fd06d40c7f6c4bcae5c848281b。

真实读数如下；它们属于浮点求解轨迹，不是严格奇异值或残差区间：

| 项目 | 实际返回 |
|---|---:|
| 初始工作雅可比最小奇异值 | 0.6001684218904573 |
| 失败角索引 | 5 |
| 该角失败工作雅可比最小奇异值 | 0.0003935073141565039 |
| 该角旧残差范数 | 0.03487958921534087 |
| 最后实际试探alpha | 7.62939453125e-6 |
| 最后实际候选根范数 | 0.5028248375102611 |
| 最后实际候选在0.75球内 | true |
| 最后实际试探残差范数 | 0.03487965558944885 |
| 同次Armijo右端 | 0.034879589188729854 |
| 新工作矩候选的初始雅可比最小奇异值 | 0.9999999999999994 |
| 新工作矩候选的初始雅可比与I之差 | 4.718447854656915e-16 |

失败原因是原完整根回溯未找到下降试探。最后候选本身仍在指定0.75球内；该条证据支持优先检查控制映射和工作雅可比，不能把这次失败归结为最后候选触及半径。也不能从一次浮点轨迹推出真实端点映射必有奇点、没有别的根或不存在满足课题要求的曲面。

阶段15中的新Q仅为候选：报告明确 candidate_Q_installed=false。候选用全922个径向胞、原8阶规则的真实工作矩生成；矩没有严格积分/浮点误差盒。阶段15完整场残差、J、J转置调用均为0，没有新接受checkpoint。上述接近I的读数因此不构成真实端点导数的认证。

阶段16只运行完整纯标准库绑定源 frozen_zero_moment_input.py
（19678字节，SHA256
4dc3e1a8ba8f128e1d05176f4d0f4b18c62d278fed603cc46f7ed686f6e4e611）。
它读取已返回的两个报告和真实来源身份，逐bit核18个数值与18个hex字，不重新计算矩、逆、根、F或J。实际返回 field_calls=root_calls=J_calls=JT_calls=0，无缺失输出或summary错误。完整runner输出9353字节，SHA256
dc65726b72d13c6871be5d00c20999e422ed26ce5cd0a7a19ec7f200b910c75a。
后续公开的小参数文件可有自己的排版与来源说明；不能把重新组织的小文件标成这份9353字节输出的逐字副本。

## 2. 工作矩公式只负责选择新输入

记 $[v]_\times u=v\times u$。若给定两个向量 $\widehat v_1,\widehat v_2$，定义

$$
\widehat J=\bigl[-[\widehat v_1]_\times,\;-[\widehat v_2]_\times\bigr],
\qquad
G=\widehat J\widehat J^T
=\sum_{i=1}^2\bigl(|\widehat v_i|^2I-\widehat v_i\widehat v_i^T\bigr).
$$

在 $G$ 可逆的条件下，其右逆的两块为

$$
Q_i^0=[\widehat v_i]_\times G^{-1},
\qquad
\sum_i-[\widehat v_i]_\times Q_i^0=I.
$$

等式直接来自 $-[v]_\times^2=|v|^2I-vv^T$。这里没有新增存在性定理；这是选择端点控制输入的有限维代数恒等式。

实际阶段15按原总积分函数计算全922胞上的工作量
$\widehat v_i=\operatorname{quad}(b_iT_0)$，再按明确的轴对称输入选择其x、z工作分量，把y分量置为准确零。原工作y读数仍保留在runner报告里。其工作逆运算的输出已经返回；本轮新科学输入直接采用该输出的18个准确二进制字，不把它们重新解释成未知真实积分矩的准确逆。

因此，后续数学模型中的 $Q_i^0$ 是下节的固定实矩阵，每个系数是对应有限binary64字代表的准确实数。新模型的定义不再依赖如何重算那次浮点逆。即使原工作矩有积分/舍入误差，这18个准确控制参数仍然定义一个明确的新模型；误差会影响该模型是否好求解，却不会允许把工作恒等式冒作真实导数恒等式。

## 3. 已实际返回的全部18个固定参数

新的定义身份为
05dc5ed735db9860ae745eeb4caecde142111ff13f40b33bd8e29701039b968e。

两个矩阵按行排列，下面的18个字符串全部来自实际16；符号和字面binary64值均保留：

| 矩阵/行 | 第0列 | 第1列 | 第2列 |
|---|---|---|---|
| Q0，第0行 | 0x0.0p+0 | -0x1.f54b784ca956ap-1 | 0x0.0p+0 |
| Q0，第1行 | 0x1.972524c4f8e87p+0 | 0x0.0p+0 | -0x1.e6c4f7d8b8182p+0 |
| Q0，第2行 | 0x0.0p+0 | 0x1.956cca02ca83bp-3 | 0x0.0p+0 |
| Q1，第0行 | 0x0.0p+0 | -0x1.7be87d3213c4cp-1 | 0x0.0p+0 |
| Q1，第1行 | 0x1.03bb57b63d53dp-1 | 0x0.0p+0 | 0x1.41266339b41f3p+1 |
| Q1，第2行 | 0x0.0p+0 | -0x1.3dc38eaa8f3a4p-1 | 0x0.0p+0 |

精确相对bubble节点保持

$$
(1/32,\;1/4,\;15/32),
\qquad
(17/32,\;3/4,\;31/32).
$$

同一完整base模型身份为
9d4ccb16efe9a0c0f5b077c0e8919e76d1d04b06e669588b32e2de78c92f0258。
上述目标、reference、base、原trace/原模型/原初点来源与节点，同18字一起构成恰好10个键的完整definition。definition按UTF-8、键排序、无额外分隔空白、禁止NaN的JSON作SHA256；路径和运行时cache不进入数学定义。

原trace路线同时核26b094的完整bytes和已返回的definition05dc。小参数文件路线同时核该小文件自己的完整bytes和同一definition05dc。两条路线不是接受不加来源约束的任意18数；纯binder核完整键集合、精确字、旧报告来源、全参考/标量/base身份和bubble节点。新算子再以实际base核同一个definition。

## 4. 完整角向延拓与导数

令 $\theta_0(\phi)$ 为已经固定的材料图，$\rho_0=\theta_{0,\phi}$。记
$R(\phi)=R_z(\theta_0(\phi))$，
$Z=[e_z]_\times$。定义

$$
Q_i(\phi)=R(\phi)Q_i^0R(\phi)^T,
\qquad
W(s,\phi)=b_1(s)Q_1(\phi)+b_2(s)Q_2(\phi).
$$

新零闭合切向量仍由原完整公式产生：

$$
T(s,\phi)=\exp\!\bigl([W(s,\phi)z(\phi)]_\times\bigr)T_y(s,\phi),
\qquad
C(z,x,\phi)=\Gamma_x(\phi)+\int_0^S T(s,\phi)\,ds-P_x(\phi).
$$

只有真正解出同一端点方程的分支才有该闭合结论；有限工作残差自身不等于准确闭合。原数值入口仍保留径向Gram行，未因准确公式的单位切向量恒等式删行。

由于两个 $Q_i^0$ 在全部当前core、omega、H自由量上恒定，且 $\theta_0$ 是固定参考图，控制映射的完整显式导数为

$$
W_s=b_1'Q_1+b_2'Q_2,
\qquad
W_\phi=\rho_0[Z,W],
$$

$$
W_{\phi\phi}
=\rho_{0,\phi}[Z,W]
+\rho_0^2[Z,[Z,W]].
$$

证明是对 $R Q_i^0R^T$ 逐次求导，利用 $R_\phi=\rho_0 ZR$；$b_i$ 不依赖 $\phi$。代码的 _W 逐项实现这些矩阵式，未把角导数换成有限差分。这里的 $\rho_0$ 和 $\rho_{0,\phi}$ 都属于固定材料图；当前core影响 $\Gamma_x$、原完整 $T_y$ 和端点条件，由原实际链处理。

根和其一、二角导数继续由原3维根方程及完整6×6/9×9下三角隐式系统处理。数值Newton迭代保持detach；完整一阶JVP/VJP来自原隐式surrogate，包含当前全部自由core、omega与H，而非把有限步Newton轨迹当准确隐函数。新Q没有在每个自由点重新取矩/逆，故没有漏掉一个本应存在的 $D_xQ$ 支路。

这个变化可能改变6个bubble旋转轴组合中被3个根坐标选中的子空间，也改变同一个根坐标球对应的物理控制集合。因此新输入的数值球半径0.75不能继承旧端点轴输入的IFT球、范数余量或已接受场；完整新源/新模型和真实新baseline都有独立身份。

### 4.1 反射协变

每个字面矩阵在 $(0,0),(0,2),(1,1),(2,0),(2,2)$ 五个位置都准确为零。令 $M=\operatorname{diag}(1,-1,1)$，则逐项得到 $M Q_i^0 M=-Q_i^0$。在固定图满足原反射关系 $\theta_0(-\phi)=-\theta_0(\phi)$ 时，

$$
Q_i(-\phi)=-M Q_i(\phi)M.
$$

若根坐标按polar向量变换为 $z(-\phi)=Mz(\phi)$，则 $Wz$ 按旋转轴所需的axial规律变换为 $-M(Wz)$；利用
$M[u]_\times M^T=\det(M)[Mu]_\times$
即得旋转后的切向量与端点方程的相容性。半转由 $R_z(\pi)$ 的正常共轭关系处理。代码严格拒绝禁位的非零值，不擅自把小浮点数剪成零。

这证明的是方程协变。若要把相邻角的工作根拼成全角连续、二次可微且有反射对称的同一根分支，仍须完整存在/唯一性盒、角覆盖和工作分支关联。没有由稀疏模式自动得到全0.75球唯一性。

## 5. 完整入口及本次实际参数

新完整入口采用原reference0f042、原完整初点cd530与同一固定标量6ffc。首轮没有改变H，没有导入606路线已经接受的hDelta末场，也没有用旧Phi当新baseline。

两份完整科学源由原5b4/b4d全体独立派生，原文件不改。新operator的48个未改函数、geometry的37个未改函数保持原AST；新driver从内部 def save_report(): 起直到文件末尾与原b4d逐字相同。其余变化是完整新source/model/input绑定、构造器的固定Q参数和明确的报告字段。原全部自由量、母范数、阻尼、全C公共slack Phase I、永久点、完整grid/任意点几何及幅度回溯均保留。有限C或有限几何筛仍不是连续证书。

首轮参数保留原实际wide尝试的完整数值设置：

- 新根政策明确为半径0.75、残差容差2e-12、最多24次Newton、18次回溯、Armijo常数1e-4；两个准确wide支撑节点如上。原默认半径0.5不会被隐式使用。
- metric方向1次、每次最多16次QP推进，mu=0.01；restoration最多4方向、每方向64次，阻尼0.01。迭代上限不视为驻点。
- N=2048完整角，radial Gauss阶8、stage block64、angle block8、jet-sum母范数、径向norm长度0.05、angular transition24。
- 固定p=4、epsilon=0.001、scale=0.05、legacy fraction0.5；真实新initial/final必须用同一新Phi比较。
- 原reach比0.03及0.992有限筛安全系数；marked直径预算4.2、witness下界0.9、height floor1.01。所有原几何和幅度真筛都保留。
- 直接入口读取真实26b094及434132报告，并显式要求已返回的definition05dc。其纯reader的parent使用实际reference包，所以初始根失败时仍可完整归因，不需要捏造final.npz。

完整两步参数文件为 zero-moment-Q-complete-first-ready.json，13345字节，SHA256
b934a3ba5a557c54a38ff5b1dbaf5d32604757b3cf91cb3e598038edb904d498。
它相对未获actual16时的ready只增加显式expected-definition参数及说明；其余科学参数和纯reader步骤不变。

## 6. 完整小源身份与已完成的静态检查

文件均位于本课题 scripts/resume_20261126/；ready由root纳入公开计算请求。新执行model/source绝不冒用原5b4/b4d身份。

| 完整文件 | 字节 | SHA256 |
|---|---:|---|
| frozen_zero_moment_input.py | 19678 | 4dc3e1a8ba8f128e1d05176f4d0f4b18c62d278fed603cc46f7ed686f6e4e611 |
| so3_zero_closure_moment_operator.py | 55610 | 44ac53f1fcecceae55ed3b3230e1925292ce76ced85dc75f08e15ff0b70f5e4e |
| so3_zero_closure_moment_geometry.py | 46504 | e4a3271d829a1fc52080b0ac1bdb719f5a13065f23223e64288c77ea6bbc514c |
| fullclosed_zero_moment_so3_qp.py | 58216 | ff500abfa24de27c22f8a8993b9104cc265c5c96289a927c18755d318fbf0766 |
| launch_zero_moment_so3_actions.py | 13127 | 082bb92e0e9f01067cf1bd8ecaae65cb559e38bba90dd79b97bf492c11d758f4 |
| read_zero_moment_so3_report.py | 30004 | c942aa60db84698215e53dd2427a19c693ca73e6c3c8553ef0b73fa75edf295a |
| derive_zero_moment_complete_entry.py | 16116 | 95e866d937e344ee7edc1081a28b699c9e1c16f04bbc4b95759d622afe3a2a43 |

可移植deriver只接受原b4d完整driver、2741完整launcher及b25完整reader的真实SHA；随后完整生成新三个正文，并检查预定未改函数/主体。它不是运行时注入片段或给原模型换标签。已在本地进行纯标准库AST、compile、字面重复dict-key、完整派生字节和未改函数比较；已实际执行纯 --print-command。这些检查没有导入NumPy/Torch，没有产生F/J、根或矩的科学数值。阶段16的纯参数抽取则已经在公开Actions真实执行。

新report保存完整Q定义及其身份、实际输入文件来源、实际新model、原根算法出处、当前与全部尝试根计数；新reader严格核完整source及模型字段并保存初始失败状态。moment_Q_recomputed_from_current_field=false、Q_input_recomputed_at_current_point=false与“工作逆不是连续证书”的字段各按其真实所在层读取，不把model和metadata键混用。

## 7. 新输入仍要承担的责任

本说明写作时，实际返回只到阶段16；新moment-Q场尚未返回。将采用新输入，不等于它已成功闭合或改进了metric。

原5b4专属的连续root/outward消费者不能通过伪装source或复制旧数值结论接44ac。新输入要认证真实端点导数和误差，必须针对这18个字面矩阵完整支付 $W,W_s,W_\phi,W_{\phi\phi}$ 的界；例如先由准确矩阵系数给谱范数的可靠上界，再应用真实bubble、固定rho0和交换子界。候选工作导数与I相差4.7e-16不能替代全径向积分、浮点、core逆图和全角误差费用。

新的根分支需要真实same-field残差/导数包围、局部唯一性盒、相邻角全包含拼接及数值分支关联；原0.75只是数值搜索政策。真正被接受的metric方向仍需同一新Phi下降、完整域与全几何/幅度检查。其后全域相对metric、全部t的嵌入/reach、固定同一g的网格/频率/t精化仍是原题完成标准，本文没有降低任一项。

后续动作应由这套完整新源的真实返回决定。若仍失败，应读取新模型的实际端点残差/雅可比/支撑几何或完整约束归因，再改变输入或求解方向；没有理由把本条已登记的工作矩诊断反复重算当作进展。

## 8. 已发表完整小参数文件与执行登记

完整18字及来源已经由真实终端提交 [ca7a4607](https://github.com/Rogerhu12/math-research-public/commit/ca7a460703a86324926b4ab69144428a578a1f47) 发表为 [frozen-zero-moment-Q-actual16-parameters.json](../computations/frozen-zero-moment-Q-actual16-parameters.json)，3618字节、SHA256 `df11d8a4b36eb9ce113b5961863191c9b58cb2473af9c48e1714026041a42e2c`。它是明确的新紧凑序列化，完整definition仍为05dc5ed7；不是原9353字节runner输出的逐字副本。两完整科学步骤使用原trace路线，并显式锁同一definition，已追加到03b活动队列；本登记没有新求解结果。

两个泡泡的支持仍避开中圈与帽端，且各支持边界的值、一阶、二阶均为零；替换固定Q不会改变这项端口结构。准确闭合及端口结论仍以完整端点方程存在光滑解为前提。root已完整阅读上述矩阵/导数/协变说明、全部新物理源相对原源的差异、reader/launcher和完整ready，并核实际字节身份；本地只作代码/文本/元数据工作。
