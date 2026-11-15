# 连续 C 原准确根族：完整112模态深端图生产器接口

- 作者：AI（geometry）。
- 状态：独立源码已完成；本地只做文本、AST和身份检查，没有导入科学模块或执行区间算术。
- 源码：[geometry_20261115_stored_continuous_C_far_graph.py](../computations/geometry_20261115_stored_continuous_C_far_graph.py)。
- 源码身份：16,333 B，SHA256 fe66789e7d94ab014662250e90642ab7fda3084b39c00b93836459220b33bb2a。
- 完整证明：[R312](../results/R312-continuous-C-complete112-zero-tail-and-head-connection.md)，26,907 B，SHA256 036289ed624b59456cfee700217f442d26104cae76bf33d9affd8ec618c9ac73。
- 连续目标定义：[R286](../results/R286-original-stored-continuous-integral-and-metric-bridge.md)。模型选择、原finite求值器和真实积分对象的区别继续保留。

## 1. 这份源直接生产什么

本源对原来的全部物理频率 $m=2,4,\ldots,224$，在一个明确深端 $F\ge159$，生产属于声明 $\mathcal C$ 的真实线性远端图的区间包围。它使用 R312 的统一定理和实际冻结参数，逐模态输出完整 Robin 行以及该深端的物理 $dH/dr$ 斜率区间。每个区间同时包含同一原准确根族内的每一种固定根选择。

这项结果有确定的对象和端点：source cell $n$ 从内向外连接 $U_n$ 到 $U_{n-1}$；数学端口 $F$ 对应 physical node $F+1$；无限深部分是全部 $n\ge F+1$。默认 $F=159$ 正好是完整深尾 $n\ge160$ 的外边界。参数 $F$ 是原胞元编号，不是有限shooting图中的另一套stage编号。

源码不选择某个无限根序列，也不运行有限 RK 校准。它没有计算浅160层的基本矩阵，没有把深端斜率当作物理cut的斜率，没有复用旧finite readylineargraph或旧零形状J。输出完成表示本次112条深端包围齐全；它不表示新非零native解、完整DN可微性、BVP或闭曲面已经完成。

此处准确根族并非没有存在性依据的占位集合。原输入由冻结 R286 binder核实，并要求其准确根存在条件已满足；R312在整个无限半线上证明有界加权解和深端高度投影非零。因此“没有算根值”不会被写成“从零个unresolved假定存在”。

## 2. 完整来源闭包

新源只在具备以下两项环境字段的公开Actions内执行科学算术：

- GITHUB_ACTIONS=true；
- GITHUB_REPOSITORY=Rogerhu12/math-research-public。

此检查位于原binder导入和python-flint初始化之前。这里没有绕过repo约束的本地模式。

### 2.1 四个本题Python来源

| 文件 | SHA256 | 本次用途 |
|---|---|---|
| geometry_20261115_stored_continuous_C_far_graph.py | fe66789e7d94ab014662250e90642ab7fda3084b39c00b93836459220b33bb2a | 新112模态深端包围 |
| geometry_20261115_stored_continuous_E_cover_v3.py | f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df | 原输入binder、Arb初始化/准确常数/输出字典 |
| geometry_20261115_stored_continuous_E_cover_v2.py | 004010b681aa35635e15b229a3e5b78602b3ec480a631a761e42f6c7d563b6ea | v3 binder绑定的实际136原来源 |
| geometry_20261115_stored_continuous_E_cover.py | 9aa0da45027afa37ca329eab73e5e93e788f2bbafb908b9e8c2960f537a427ed | v3 binder绑定的原连续C来源 |

新源不调用三个E生产器的main、ContinuousHead、SixPrimitiveIntegrator、inverse或query流程。保留其来源不代表本次重复跑过积分，更不代表139已经有任何结果。

### 2.2 binder原九公式来源

runtime-computations下的四件：

| 文件 | SHA256 |
|---|---|
| tail_frozen_geometry.mjs | db6664fcd7be618d2b684c39c01c53d97833d11e14af206b12c71e4b058713e3 |
| strong_frozen_calibration_factory.mjs | 77e9d2fc0e277ef69c9a4300ceba2d3d6b03056fc6a4868fab049a1a1c290247 |
| closure_bounded_point_cache.mjs | 35289a4de44ec409bc211f82c7a1bee81a10c6bc1c5fb31e4ca9a8634cc09043 |
| exact_20261114_closed_background.mjs | be358bf780c88ebd85cdf07d9e8d2cc3b37ca20a4d8ea3a1ba69e7c40c2c4e1b |

source-topic/scripts下两件：

| 文件 | SHA256 |
|---|---|
| closing_weighted_tail.mjs | 740e672edee58cff7a15f89d75e181577dd439c1c62777c57d0d0ab1af32141e |
| closing_recalibrated_tail.mjs | 4a109f26b0e6c9741dfff678c0fe42da4935bfda9c605e55688e97848aef0dd6 |

source-topic/repro/source-root/topics/large-amplitude-twist-flex/scripts下三件：

| 文件 | SHA256 |
|---|---|
| tailnext_balanced_tail.mjs | 928567418f411b70c4040be9ee08be2a78b65e147b8d0c5728f4cf6766a28888 |
| general_root_smooth_tail_cells.cjs | d074799099e27401456449343c8f490ec60cdec7eb0d02758f024f541d409575 |
| f6tail_cusp_grid.mjs | b12f3626413262daf1eef6be87bf7ad27813295bd2b84e166dcb9ed6c612736f |

共十三个源码文件。另绑定原source-origin.json、config、ledger-ready、stored-ready及两篇证明，不将它们混计为源码。

原source revision仍是原ready保存的869436630c99aa5a68afb55bd8877c826034d117。原source-origin、两份ready的source hash、160行浅表、保存warp系数和历史fingerprint由同一冻结binder核实。历史fingerprint仅按原件身份绑定；本次没有重跑原factory来重算指纹。

R286 proof的实际SHA为81d061a6db372a531a119d54298a68d1b9804a7e08fea0fd33bc5fe75a809efb。R312 proof按本页首部精确字节锁定。

## 3. 实际输入与CLI

需要三份已经存在的原输入：完整config、原calibration ledger ready、原stored reference ready。每份CLI SHA绑定实际文件字节；如果文件为gzip，SHA仍指压缩文件，并另记录解码长度和SHA。重复JSON键或非有限JSON数字按原binder拒绝。

调用模板如下；ACTUAL字段只能来自实际文件，不能用未来占位值调度：

~~~sh
python computations/geometry_20261115_stored_continuous_C_far_graph.py \
  --config "$ACTUAL_CONFIG" \
  --config-sha256 "$ACTUAL_CONFIG_SHA256" \
  --ledger-ready "$ACTUAL_LEDGER_READY" \
  --ledger-ready-sha256 "$ACTUAL_LEDGER_READY_SHA256" \
  --stored-ready "$ACTUAL_STORED_READY" \
  --stored-ready-sha256 "$ACTUAL_STORED_READY_SHA256" \
  --runtime-computations "$ACTUAL_COMPUTATIONS" \
  --source-topic "$RESTORED_ORIGINAL_TOPIC" \
  --proof results/R286-original-stored-continuous-integral-and-metric-bridge.md \
  --tail-proof results/R312-continuous-C-complete112-zero-tail-and-head-connection.md \
  --far-port 159 \
  --precision-bits 256 \
  --out "$REQUEST_TEMP/continuous-C-deep-far"
~~~

out必须为全新目录，且不能包含上述五个原输入/证明路径。读取来源和输出属主分开；本脚本不执行Git或网络操作。

runtime是python-flint==0.9.0；precision-bits显式设置，支持128至8192。提高该值只是区间求值工作精度，不改变原BVP容差或添加接受门。该薄源没有需要人为扩大到1800秒的积分预算，也不枚举48步selector树。它只有完整112行的有限区间求值。

原输入沿R286要求orientation=+1、protectCell=160、无rejoin、a=11/4、etaPower=3/2、R=64、160个正浅校准行以及lengthScale=1。当前输入需要 $0<d_0\le1/10$、$0<c_0\le1/16$；这些正是证明已有的原根族范围。源码不会把不在该范围的别种profile静默改写成它。

## 4. 实际区间计算

记 $\delta_n=d_0 2^{-n}$、$c_n=c_0 2^{-n/2}$。在端口F，程序按R286准确实表达计算

$$
s_F=3d_0 2^{-F}
+\frac{6c_0d_0\,2^{-3(F+1)/2}}{1-2^{-3/2}},
\qquad r_F=r_c e^{s_F/\sqrt{12}},
$$

$$
\mu_F=\epsilon_{\rm phys}\delta_F^{11/4},
\qquad w_F=\mu_F/r_F^7 .
$$

这里的 $r_F$ 在保持raw的深域，由原连续定义直接给定；它不是整个有限头的 $R_{\rm out}$，也不是把名义rCut当成真实cut。完整w的有限头cap/flat/warp仍属于后续有限头责任。

全部112个mode统一使用同一原准确mode2根序列。计算参考谱只为形成已证明的包络，不用65/64替换实际根。令

$$
\nu=\frac{m^2(m^2-1)}{12},\quad d=2^{-11/4},\quad
H=65\nu(1+d/64)-1-d,
$$

$$
L=\frac{H+\sqrt{H^2-4d}}2,\qquad S=d/L .
$$

为避免大数相减，参考图用准确恒等式

$$
s_m=-d+\frac{d+S}{(65/64)\nu}.
$$

对mode2直接保参考值0。R312的统一扰动包络为

$$
\varepsilon_F=2^{-16-\lfloor(F-159)/2\rfloor},\qquad
|\mathfrak g_{m,F}-s_m|<20\varepsilon_F .
$$

本源对 $m>2$ 输出包含该开误差界的闭Arb区间；所有sqrt、exp、log、商及区间并集均在Arb外包中完成。若当前工作精度不能严格包住必要的正数/有限值，输出partial或错误，不把中点当证明。

对于mode2，原每层准确根使下左元严格为零；由R312半线唯一性有 $\mathfrak g_{2,F}=0$。程序输出这个准确0，明确其依据为准确根定义。它不声称旧finite RK校准也有相同零残差。

真实原变量图为 $\Pi_m=\nu\mathfrak g_{m,F}Q_m$。深端物理高度使用 $u=r^4Q$，所以

$$
\frac{k_F}{u_F}
=\frac{m^2+\sqrt{12}\nu\mathfrak g_{m,F}}{r_F},
\qquad k=dH/dr .
$$

每行同时输出原坐标Robin $(-\nu\mathfrak g,1)$ 和深端物理Robin $(-k_F/u_F,1)$。deep_port文字是合同的一部分，不能在下游改成cut而跳过完整有限头。

## 5. 输出文件与逐行身份

输出共三项：

| 路径 | 内容 |
|---|---|
| input-binding.json | 实际原三输入、原source-origin、十三源关系、两proof、模型/根族/端口定义和实际运行时 |
| large-arrays/complete112-deep-far-rows.jsonl | 按m=2到224递增的全部完整行；若异常保已经写出的行 |
| result.json | 完整范围、行流receipt、完成前缀、未付suffix、错误与明确未付事项 |

input-binding的schema为R312-original-C-root-family-deep-far-input-binding-v1。原R286 binder的完整字典放在original_C_input_binding中，不把它的integral_strategy字段误写成本次已执行积分。

result的schema为R312-original-C-root-family-complete112-deep-far-enclosure-v1。每行schema为R312-original-C-one-mode-deep-far-enclosure-v1。

每条Arb数值保存lower和upper的准确dyadic结构：mantissa是十进制整数字符串，binary_exponent是整数；display只供人读，不能作为下一步严格区间输入。行流receipt含相对file、bytes、rows及SHA256。结果绑定完整行流，不只给几个极值。

完整行包含：

- mode_index、physical_frequency、准确整数nu、far_port和physical_node；
- ideal参考的大/小特征值及归一特征值；
- ideal_balanced_graph、theorem_graph_error_bound；
- actual_balanced_Pi_over_nu_Q、actual_original_Pi_over_Q；
- actual_deep_port_slope_per_unit_physical_height；
- 两种Robin行、准确根族包围理由，以及没有进行有限头传播的标志。

所有完成状态按实际循环产生。未访问的mode_suffix保留全部剩余频率，不用“最大112”替代完整枚举，也不把已经有某几行视作完整矩阵。

## 6. stdout与Rule15

完整result写出后，生产器形成一份不含112行payload的摘要，按以下边界输出：

~~~text
BEGIN_R312_CONTINUOUS_C_DEEP_FAR_SUMMARY
{one complete compact JSON object}
END_R312_CONTINUOUS_C_DEEP_FAR_SUMMARY
~~~

随后打印该摘要的bytes/SHA与实际result receipt。摘要90,000B上限是传输限制；超过时返回70并打印真实大小/hash，保临时完整result，不改科学判断、不切开或省略未知行。正常完整112行返回0；科学区间异常/未完成suffix返回2。

本源不安装artifact SDK，不上传，不自行删除来源，也不改Git。原始行流和输入复制属于调用workflow拥有的可重算临时数据。公开后只保存源、参数、运行编号、摘要及输出SHA；workflow应在标量读回后清理自己创建的临时输出。不能由退出0推出曲面或BVP成功。

## 7. 明确保留的有限头和cut责任

后继可以直接消费每行的原坐标图或深端物理Robin，继续R312的同一连续对象。若从F>159出发，先完整保留F到160的实际准确根胞元，再接原浅160层；不得因深端包络可用而跳过这些胞元。

物理有限头方程仍是

$$
\frac{d}{ds}\binom uk
=
\begin{pmatrix}
0&D\\
m^2q/(rw)&-q/w
\end{pmatrix}\binom uk,\qquad
D=R_*'(s)>0,\quad q=w_s .
$$

它要求来自同一C的实际完整w、真实累计R*和全部分支。其基本矩阵行列式不为零只保证完整状态传递可逆，不能保证cut的高度分量非零。由真实传递得到cut列(h,l)后，Robin $hk-lu=0$ 总有效；只有每个请求模态的h均已证明非零，才能写完整cut DN对角l/h。

本源因此固定保留：

- finite_head_propagation_performed=false；
- protected_head_join_verified_by_this_producer=false；
- natural_outer_radius_computed=false；
- requested_cut_domain_verified=false；
- cut_height_denominators_verified=false；
- cut_DN_matrix=null；
- actual_nonlinear_DN_existence_or_differentiability_proved=false；
- full_BVP_or_closed_surface_accepted=false。

这些字段不是新增BVP门，而是准确区分本次已生产量和尚未生产量。准确目标仍是显式声明C；old_finite_selector_reinterpreted_as_certified_continuous_C=false。即使日后完整E闭覆盖成功，也不能仅凭其schema填上这里的有限头传递和非共振责任。

## 8. 本地检查和下一可执行点

本次本地只解析Python AST、检查源码常量/文本与冻结binder字段、核对proof公式引用及计算来源，没有调用上述任何数学函数，没有输出任何实际Arb行。没有新fixture，没有实际E/query或接受场，也没有伪造请求编号和运行结果。

最薄公开执行可复用132/136/139已明确的同一原config、两ready、source恢复与sourcepins；它只新增本生产器和R312 proof。实际每份输入应按该次运行的原文件SHA传入。本源不要求等待139的数值结果，因为它只消费原输入metadata和已证明的raw深域公式；同样也不宣称自己的深域结果解除139尚未完成的有限头E责任。

此生产器给出了新C零线性响应的一段实际可计算数据。完整后继仍须完成同C有限头、真实cut域及所需非共振，再接原完整112二维边界消元；旧finite常数不得冒充这些新系数。尚未有任何实际成功场，此处没有1e-6、2e-9、K、D或reach的通过结论。

