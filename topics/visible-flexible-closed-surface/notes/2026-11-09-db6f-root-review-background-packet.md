# 实际物理半径上的背景多项式供应包：独立审查

2026-11-09，Astra-visible-flex-db6f0b0e/root。作者为 tail_theory；审查者未实现 producer。**方法通过全文审查；绑定的三跨试算经独立重跑，所有数组逐值一致。** 全域正式运行仍须检查覆盖并送入另已独审的 metric/曲率 consumer，本稿不单独宣称全尾过门。

最终审读 `scripts/db6f-tail-background-packet.py` 的 SHA256 为 `75ef3b0426f31926d2e529d18f3b57beda8bc40fdca0cf7f9c26bf33442db1b7`。数学输入链为：已审有限 calibration、精确径向归一化 $\alpha$、全部背景 $|w_r|<24$ 与内尾 cap/曲率界、原函数方法，以及 stable source 的精确代数恒等式。相关审稿为 `db6f-audit-high-order-and-tight-alpha`、`db6f-root-review-background-primitive`、`db6f-audit-stable-source`、`db6f-audit-background-coarse-packet`，均在本目录的同日期文件中。

## 1. 同一背景与精确半径

正式输入是旧 int2 宏观有限尾 manifest，以及完整 raw 0/1 的 stable 原函数表。旧 manifest 的半径节点定义为保存的精确二进数。对于增量格式，代码从精确内锚点累积每个保存二进增量乘共同有理比例，并核外锚点精确相等。物理子盒由这些有理半径和二进局部端点构成，未把数值显示半径重新当作另一套几何。

producer 绑定 manifest、原函数、源文件和 calibration 的 hash，并核固定物理参数。原函数所使用的 source model 由明确元数据选择；stable 模型只改变等价多项式的区间求值，目标 $g$ 不变。正式有限半径位于 $(r_{\rm cuff},r_{\rm cut}]$，圆领外端被检查属于已证内尾。

## 2. 近似逆函数只作提案

在物理盒 $r(\tau)=r_l+(r_r-r_l)\tau$、$0\le\tau\le1$ 上，程序以数值逆像和导数中心值建议三次 Bezier 控制点。随后把四个控制点视为精确二进有理数，并明确检查

$$
0\le a\le b\le c\le d\le1.
$$

故其多项式 $x_{\rm app}(\tau)$ 单调且始终位于 $[a,d]$，与 source 的定义域一致。程序的近似逆解本身没有证明效力，也不要求它满足数值求根容差。

对每一片可能被 $x_{\rm app}$ 经过的原函数叶，将其已审多项式与 $x_{\rm app}$ 复合，减去精确线性 $r(\tau)$，以向外 Bernstein 系数界和原函数余项包围径向残差。每个叶多项式在整个 $[0,1]$ 上求界虽可能很宽，但对该叶实际负责的子集仍有效；对所有可能叶取最大值覆盖全部 $\tau$。原函数叶很多时，改用单调性给出的范围差。两种方法都是独立上界，取较小者合法。因此返回的 $\delta_r$ 满足

$$
|r_{\rm exact}(x_{\rm app}(\tau))-r(\tau)|\le\delta_r.
$$

## 3. 斜率多项式及相位误差

若整个提案源区间位于同一个解析 cap 分支，则在源区间中心以 normalized jets 作有限 Taylor 展开。函数值余项由全区间第 $p$ 槽绝对值乘源坐标最大半径的 $p$ 次幂控制。中心只需是合法的二进数；最大半径以精确有理差重新计算，所以不依赖中点恰好可表示。若分支未被证明固定，则直接用函数值区间作零次包。

把源 Taylor 多项式与 $x_{\rm app}$ 复合，得到 $W(\tau)$。由于完整精确背景已有 $|w_r|<24$，有

$$
|w(r(\tau))-W(\tau)|
\le R_{\rm Taylor}+24\delta_r.
$$

此法即使物理盒跨 source profile 接口仍有效：提案点及目标半径都属于同一完整背景，而 Lipschitz 估计连接这两个实际物理半径。不把所选 profile 误认为目标物理盒的真实逆像分支。

## 4. $w_r$ 的局部 Taylor 包

令 $q(x)=w_x(x)/r_x(x)$。只有当强锚点证明整个物理盒位于单个 profile 内，且提案区间与真逆像包的凸包中 cap 和 $|w_x|$ 分支都固定，才采用此路线。这里要求解析的是组成 $q$ 的全部项，不仅是 $w$。

真逆像 $x_{\rm true}$ 由已审 `inverse_cover` 包围；在两种源点的共同盒上，区间运算证明 $r_x\ge m>0$。中值定理和径向残差给

$$
|x_{\rm true}-x_{\rm app}|\le\delta_r/m.
$$

在提案源盒展开 $q$，并在共同盒以 Jet 的一阶槽给 $|q_x|\le L_q$。因此最终多项式 $Q(\tau)$ 满足

$$
|w_r(r(\tau))-Q(\tau)|
\le R_{q,\rm Taylor}+L_q\delta_r/m.
$$

在 cap、绝对值临界点或不确定 profile 接口处，该高阶推理不启用。代码遍历所有可能相交 profile，以条件逆像包求 $w_x/r_x$ 的范围并取 hull；当来源覆盖不充分或正分母未证实时，退回已审全域 $[-24,24]$。

## 5. 内尾分类与审查发现的边界漏洞

内尾满足 $0\le w\le1/49$、$|w_r|<6.01$，但此界必须按**整个实际物理盒**分类。早期 hash `b2470bf48321a5a87ce40e370660fa8d719197a565d67850da09964c12014e0e` 曾在 `derivative_polynomial` 中仅凭提案 profile 的编号 $n\ge1$ 便使用内尾界；这不能覆盖跨 raw 1 / raw 0 接口的盒，故该版不获方法通过声明。

最终版本以 raw 0 内边界的强锚下界作阈值，只有盒的外端也低于该阈值时才直接采用内尾界；另一许可情况是强锚证明整盒位于一个 $n\ge1$ profile 内。部分原函数表若未有任何一个 profile 强覆盖整盒，直接退全域界，避免遗漏表外可能分支。

完整原函数表更深侧的粗包判定同时在每个自适应子盒执行。这修复了一个工作量问题：跨表边界的原 span 可能只有约 $6\times10^{-14}$ 的外端薄片需要精化，内侧子盒若反复把逆像钳在 0，残差不会随该盒缩小。旧运行被中断并保留，不作全域证书；新判定使用已有内尾定理，未改变目标函数。

## 6. 降阶、舍入与完整覆盖

在 $0\le\tau\le1$ 上，从区间系数多项式删除次数 $k>d$ 的项，只增加

$$
\sum_{k>d}\max\{|c_k^-|,|c_k^+|\}
$$

到统一余项即可。代码以向外区间加法累积该和，分别支付 $w$ 与 $w_r$ 的删除项，并在加入后才检查细分容差。正式保留次数为 8。容差只决定是否继续细分；即使达到最大深度仍未满足预期宽度，保存的实际区间与余项仍有效，`unmet_tolerance_rows` 明确记录此事。

各物理 span 由精确二进二分得到无缝子区间。完整选择另加入圆领，数据行保留原 span 编号和局部端点；consumer 必须核所有 span、局部左右端点、无重叠缺口，以及使用全部 $w/w_r$ 余项。它不能仅信任 producer 的 `finished`。该 consumer 的表示层、覆盖逻辑及三条度量/曲率公式已由不同作者独立审查，本稿不重复代付其输出。

数组保存前检查有限值与区间顺序，NPZ 超过 1 MB 再 gzip，最终单个文件小于 5 MB。hash 绑定压缩后的实际文件；只有完整、可装入的合并包才具有 `data_file/data_sha256`，否则明确要求分片 consumer。

## 7. 独立重跑与结论

最终独立命令使用同一 int2 manifest、完整 stable depth2 原函数、order=8、output-degree=8，以及 spans 4509,4510,4511。输出 `2026-11-09-db6f-root-review-background-packet-rerun-v2.json/.npz`，与作者 `2026-11-09-db6f-tail-background-packet-final-pilot-v2` 比较。全部数组、输入链与数学源 hash 逐项一致；9 行均满足请求宽度，最大 $w$ 余项 $1.032335\times10^{-7}$，最大 $w_r$ 余项 $0.037170$。机器审查记录另存同名 `db6f-root-review-background-packet.json`。

**最终冻结 producer 的方法与绑定试算 PASS。** 正式全包正在计算，必须继续核其实际覆盖与全部输出，再与显式有限扰动合成完整尾的连续 metric/实际曲率证书；当前不宣称 reach 或 README 全部完成。
