# 固定背景的高阶区间积分与紧径向归一化

2026-11-09，`/root/tail_theory`。本文给出固定背景 $\alpha$ 的完整计算定义、余项和当前区间。初等组件、内尾 A 临界值算法已有交叉独审；高阶 source/Taylor 积分及本文最终组合正在由未参与者独审。独审完成前不把本稿作为已审定理升级。

## 1. 固定的数学对象

使用正式宏观 checkpoint `2026-11-09-db6f-prefix-flat-v17v18-coupled-m8-q10-fine_tail_0017.json.gz`，SHA256 `d23b03e4ce5cd7aaf4ac9d1134f8a23ee274be3a1d0a0192a7b294f1195e43f0`。有限 cells 0–159 的 source calibration 是表 `2026-11-09-db6f-tail-finite-source-calibrations.json` 中的**固定二进有理几何系数**，表 SHA256 `bcfaba00aec62290b5b29432836c9e76ef6cf0d582b06c046677b0f8688ca9f4`；不要求它们成为另一个精确方程的根。所有 source 长度、半径、对数、指数、cap 和 warp 积分均按精确解析公式定义。

沿旧 source 坐标 $x$，径向速度是

$$r_x=A_x+\alpha B_x,$$

$$A_x=(1-\chi)r_{o,x}j_0+
 \frac{\chi|w_x|}{6(1+w^2)^{3/2}},\qquad
B_x=\frac{\chi r_{o,x}}{1+w^2}\,\omega.$$

这里 $j_0$ 只在 cell 0 最外保护 port 使用，$\omega$ 的非单位权重也只在 cell 0；其余定义与已审背景稿相同。令 $r_d$ 是 cell 160 的外边界旧半径。唯一满足 cut 半径 $c$ 的归一化为

$$\alpha=\frac{L-A}{B},\qquad
L=c-r_d,\quad A=\sum_{n=0}^{159}\int A_xdx,\quad
B=\sum_{n=0}^{159}\int B_xdx.$$

此前粗界已经独审证明分子和分母为正。本文以真正的积分包围缩紧该数，数值 Gauss 积分仅作比较。

## 2. 高阶积分的包含性

`db6f_tail_interval_source.py` 实现 normalized jet：第 k 个系数是 $f^{(k)}/k!$。加法、乘法卷积、倒数、指数和平方根的递推均来自形式幂级数恒等式。常数项输入整个区间 $[l,u]$ 时，逐项向外运算同时包围该区间每一点的这些导数。source 参数不确定性也向外传递，未用浮点单点当精确解析函数值。

令 $m=(l+u)/2,h=(u-l)/2$，偶数阶数 $p=12$。若整个区间处于一个解析 cap 分支，且 A 的 $w_x$ 符号已确定，Taylor 定理给

$$\int_l^u f(x)dx\in
\sum_{0\le k<p,\ k\text{ even}}[f^{(k)}(m)/k!]\frac{2h^{k+1}}{k+1}
+[f^{(p)}([l,u])/p!]\frac{2h^{p+1}}{p+1}.$$

因为 p 为偶数，余项中的 $(x-m)^p$ 非负，区间乘法方向如式所示。奇数 Taylor 项的积分为零。若 cap 分支或绝对值符号不能严格确定，程序继续二等分；达到工作阈值时改用始终有效的朴素包围 $[f([l,u])](u-l)$。没有跨过非解析接口使用 12 阶余项。

中间 cap 多项式只在其 $t\in[0,1]$ 子集求值；不确定盒同时并入实际可能的外侧分支。$S$ 常数项利用其单调性缩紧，高阶系数仍来自完整多项式微分。完全饱和且 cap 常数的区间直接使用固定二进 cap，导数为零。返回非有限或反序区间时不能进入证书。

所有默认端点是二进有理，起始分段 16，停止宽度 $2^{-44}$，所以端点、中点和宽度均精确表示。接受容差只决定计算量，最终证书就是实际向外区间，与是否达到某个期望误差无关。初等函数由 `db6f_tail_interval_elementary.py` 的有理 Taylor/atanh 级数包围；其独审见 `2026-11-09-db6f-audit-inner-variation-and-elementary.md` §4。

当前完成的全量输出为：

| 量 | 认证下界 | 认证上界 |
|---|---:|---:|
| cell 0 的 A | 0.20356892342054078 | 0.20356892342060912 |
| cells 0–15 的 B | 0.0018001260794424448 | 0.0018001260794424686 |

对应 `2026-11-09-db6f-tail-high-order-A0.json` 和 `2026-11-09-db6f-tail-high-order-B0-15.json`。每个 profile 的区间、叶节点数、分支处理和源文件 hash 均在各自输出里。

## 3. 内 A 和剩余 B

cells 1–159 的 A 采用独立作者的临界值算法，已由本文作者独审及完整复跑：

$$A_{inner}\in[0.0706548168707253,\ 0.07065481687073313].$$

它精算 cells 1–39 的全部 raw 极值，再加 cells 40–159 的显式全变差余项和保护 port 的旧径向余项。见 `2026-11-09-db6f-tail-review-inner-A.md`。没有将 Gauss 值并入此区间。

令 $a=r_{cuff}$、$q=2^{-3/2}$，并记

$$T_N=6\delta_0 2^{-N}+
 \frac{6\delta_0c_0 2^{-3N/2}}{1-q},\qquad
R_N=a\exp(T_N/\sqrt{12}).$$

这就是 cells $n\ge N$ 的总 source log 长度及 cell N 的外半径。因此 cells 16–159 的旧径向总宽度严格为

$$\Delta R=R_{16}-R_{160}.$$

已审的有限 source 盒给 $w\le W_n=1280\,2^{-7n/4}$，所以该区间内 $w\le W_{16}=1280\,2^{-28}$。它的所有权重是 1，除了 cell 159 第一个 port 外 $\chi=1$。该 port 删除的 B 不超过删除的旧径向长度；由已审保护端估计，它小于

$$P=\frac{1}{48000\,2^{238}}.$$

因此无需继续求积，就有

$$\frac{\Delta R}{1+W_{16}^2}-P
 \le B_{16:159}\le\Delta R.$$

为避免从两个接近 0.15 的半径相减，账本计算

$$\Delta R=a\{\operatorname{expm1}(T_{16}/\sqrt{12})
-\operatorname{expm1}(T_{160}/\sqrt{12})\}.$$

对精确有理 $0\le x\le1/64$，取正项级数至 12 阶。首个遗漏项为 $x^{13}/13!$，后续项比不超过 $x/14$，所以

$$\sum_{k=1}^{12}\frac{x^k}{k!}
 \le e^x-1\le
\sum_{k=1}^{12}\frac{x^k}{k!}
+\frac{x^{13}/13!}{1-x/14}.$$

`db6f-tail-tight-alpha.py` 在 Fraction 上逐项计算该式，再按 expm1 的单调性处理输入区间。它同时得到极小的 $R_{160}-a$，在 $L=c-R_{160}$ 中保留该项；没有把它设为零。

## 4. 完整组合及归一化误差

全部加法、商和最后端点转换使用精确 Fraction 或已有向外区间后端，当前输出 `2026-11-09-db6f-tail-tight-alpha.json` 给

$$A\in[0.27422374029126606,\ 0.2742237402913423],$$

$$B\in[0.0018001498727290097,\ 0.0018001498727290345],$$

$$\boxed{\alpha\in[97.64534740775791,\ 97.64534740780157]}. $$

内部有理端点的宽度小于 $4.364\cdot10^{-11}$。保存的数值参数 $\widehat\alpha=97.64534740777785$ 落在此区间内，而且

$$|\alpha-\widehat\alpha|<2.371\cdot10^{-11}.$$

如果两个背景都使用**同一精确 source 函数和同一内锚点**，只把全局归一化参数从 $\alpha$ 换成 $\widehat\alpha$，则相同 source 坐标的径向差满足

$$|r_\alpha(x)-r_{\widehat\alpha}(x)|
\le B\,|\alpha-\widehat\alpha|<4.268\cdot10^{-14}.$$

已审整个旋转背景曲率证明给 $|w_r|<24$。在两个定义域的公共物理半径上，由单调径向坐标和中值定理，斜率差小于 $1.025\cdot10^{-12}$。再用 $w\le16/15$，目标径向系数 $E=1+w^2$ 的相对算子误差贡献小于 $2.185\cdot10^{-12}$。

最后这组数**只计归一化参数的误差**。真实保存的数值 source 还经过浮点 exp/log、source 半径计算和逐段径向 primitive 求积；它们与精确对象的差必须另行包围，不能由这一个数自动认证。共同半径范围的端点也要通过接口或锚点补丁处理。

## 5. 复算和剩余接口

高阶积分按脚本帮助中的正式默认参数分别选择 `--integrands A --a-cells 0` 与 `--integrands B --b-cells 0:16`。最终组合命令为：

```sh
python scripts/db6f-tail-tight-alpha.py \
  --checkpoint notes/2026-11-09-db6f-prefix-flat-v17v18-coupled-m8-q10-fine_tail_0017.json.gz \
  --calibrations notes/2026-11-09-db6f-tail-finite-source-calibrations.json \
  --cell-zero-A notes/2026-11-09-db6f-tail-high-order-A0.json \
  --inner-A notes/2026-11-09-db6f-audit-inner-warp-variation.json \
  --outer-B notes/2026-11-09-db6f-tail-high-order-B0-15.json \
  --numerical-bookkeeping notes/2026-11-09-db6f-tail-background-split.json \
  --out notes/2026-11-09-db6f-tail-tight-alpha.json
```

下一接口应对连续审计的每个物理径向盒提供真正的 $w(r),w_r(r),h(r)$ 区间。可选择近似 inverse $x(\tau)$，严格包围 $r_{true}(x(\tau))-r_{linear}(\tau)$，再利用上述 Lipschitz 常数纠正 $w$；这样无需把数值 inverse 或径向求积表冒充精确函数。本文不认证非线性无限尾、完整尾 metric/曲率、接缝、闭曲面 reach 或 README 完成。
