# 准确端点覆盖、真实 R6 域和有限 retarget 预算

状态：本文件列出的有限域与有限多项式预算已证明并真正执行。
完整两腿覆盖由同一冻结源后台继续，未完成清单不计作全支证明。

## 1. 当前覆盖程序与真实根口径

`scripts/fourfold_phase_sharp_time_domain_cover.py` 实现 R65：先分别对准确
τ 两端计算 t sinτ 的有向界，再枚举全部相交 common spans；使用准确 PiTime
处理 ±π/2。每个 span 或重新验证，或在绑定同一实际 δ5、同一多项式 germ 后
用 |c新−c旧|+R新|h新|≤R旧|h旧| 继承已证复圆盘。负侧同时反射 c、h 与 span。
失败尝试保留，随后准确二分；每段闭覆盖由 Fraction 验证首端0、末端1与所有
相邻端点完全相同。仅完整 1100 请求全部通过才能标 whole_both_branches。

根包始终先以 Q512 付出，可独立选 Q256 表示同一个真无限场。Q256 只影响其
自己的 FFT／原函数尾，不改变曲面或根。此前 Q256 自行缩根失败已另存；没有
通过放宽紧根或把低精度根伪作同一 root 来避开检查。

160 bits、时间 m41、场 N512/Q256 下：forward286 与287各两个真实 germ 通过；
forward547 的整段普通域未过，准确二分后左半重新验证通过，右半由既有 turn
圆盘的准确包含继承。共三段请求均完成，有且仅有一个未过的父尝试保留。
报告索引 `type_fixed_step02_d5_exact_affine_step5_sharp_time_domain_pilot.json.gz`。

## 2. 第419段的真实大时间域

同一 δ5、同一准确时间两端、同一个实际主 germ，物理 θ 带1/64，外带1/32。
选择 R=6、S=8、几何 R0=1/125、RE=7/1000，根包仍来自同一 Q512 真根。

m33 的实际初试：Re(−K0)>.5673185 已过，D 下界 −.0019342 未过。
完整未知时间尾约 .0368283。失败源／报告保留。

随后独立 m41 真重算通过：

$$
|D|>0.0312065399,\qquad
\operatorname{Re}(-K_0)>0.567724945,
\qquad |d\theta/d\tau|<32.586821.
$$

完整 θ 一／二导粗模界仍大（约5.123e6、1.572e12），不能直接拿去作可用流指数。
此处主要交付是完整复时间 R6 的真实场模界，可直接用于实际时间 Cauchy／DFT 尾。
若后续时间场 evaluator 采用 R6，必须给它相应 R0=.008、RE=.007；旧默认
RE=.0025 拒绝较大的真实径向像是合理检查，不能删除。

通过叶报告
`step5_sharp_time_domain_R6_order40/forward_0419_r.json.gz`，SHA256
`c255d96333fae4f006d0bc53bf4c81ad197ad2a00831f1c03965032b039a69da`。
它的 exact_time_endpoints 用 PiTime 字典保存；本段两个 pi_coefficient 都准确为0。
旧 R3/三-germ 报告仍有效并保持原字节；新准确端点门只减少了多付的 germ。

## 3. 准确 retarget 初差的 Wiener 界

准确有限函数为

$$a(x)=h_5(x)/4-U_{4f,\mathrm{start}}(x),$$

不是简单的 $(h_5-h_4)/4$。保存输入包含完整有限初值差，degree516、分母2^122。
对其准确非负 Fourier 系数 $a_k$，程序逐项有向求和

$$
\|\partial_x^j a\|_{A_s}
=\mathbf1_{j=0}|a_0|+2\sum_{k=1}^{516}k^j|a_k|e^{ks}.
$$

全部系数为准确整数除以2^122，复模和指数由 Arb 外包。此有限恒等式没有未知尾。
在归一初值角 x 带1/128，
$\|a\|<6.457458\times10^{-11}$、$\|a_x\|<1.714377\times10^{-8}$；
在 x 带1/64，二者分别小于 $6.522366\times10^{-10}$、$2.156595\times10^{-7}$。
文件还给出0至3阶全部预算。

保持原准确定义
$\Delta Y_f=Q_fa$、$\Delta Y_b=Q_bQ_{f,\mathrm{end}}a$，则 Banach 代数与乘积法则给

$$
\|\partial_x\Delta Y_f\|
\le\|Q_{f,x}\|\|a\|+\|Q_f\|\|a_x\|,
$$

$$
\|\partial_x\Delta Y_b\|
\le\|Q_{b,x}\|\|Q_{f,\mathrm{end}}\|\|a\|
+\|Q_b\|(\|Q_{f,\mathrm{end},x}\|\|a\|
          +\|Q_{f,\mathrm{end}}\|\|a_x\|).
$$

这些 Q 是已定义的 finite Bernstein/Fourier 参考权，未声称是已验证 Jacobian。
其自身全时间复带模界仍须另付，才能把旧有限参考的 Yx 正性转给新参考。
本项不是实际参数微分或真流误差。

## 4. 重放与继续

三个域 pilot 用 `fourfold_phase_sharp_time_domain_cover.py`；每个索引记录了
全部准确参数、源／依赖／输入 SHA 和叶文件。普通 pilot 参数为
`--legs forward --segments 286,287,547 --primitive-nodes 256 --root-nodes 512
--angles 512 --bits 160 --max-depth 5`；种子为 forward2、548 的真 turn 报告
及 forward3 的普通报告。R6 两次则是 `--segments 419 --primitive-nodes 512
--root-nodes 512 --angles 512 --bits 192 --time-radius 6 --larger-time-radius 8
--radial-radius 1/125 --E-radius 7/1000 --max-depth 0`，时间阶分别32和40。
统一 `--retarget data/phase_ring_continuation/step5_retargeted_reference/descriptor.json`。

有限 a 预算入口：`fourfold_retarget_initial_correction_budget.py --descriptor
data/phase_ring_continuation/step5_retargeted_reference/descriptor.json --out <new.json>`。

完整两腿后台使用同一覆盖源、默认 R3/S4、Q512根/Q256场，逐叶 gzip 保存到
`step5_sharp_time_domain_full/`，总索引
`type_fixed_step02_d5_exact_affine_step5_sharp_time_domain_full.json.gz`。
这两个 live 输出不在本冻结清单；要续算使用完全相同参数及 `--resume`。
当前实际已付局部域继续接真场与残差，不在本有限检查点结束。
