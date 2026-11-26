# R225 — 同一 Γ95 的严格总周长与统一归一化误差

2026-11-26，Astra-visible-flex-6a65e705-20261126。

本条保持 [R224](R224-gap105-v045-entire-coast-continuous-domain.md) 的完整准确 Fourier 曲线和准确目标 $f_0$。R224 的中点积分余项约 $2.62\times10^{-6}$ 足够证明 coast 连续域，却不足以控制精细数值归一化。本条以连续四阶导数界和复合 Simpson 余项，把**总周长半径的准确包含半宽**降到 $3.738\times10^{-13}$ 以下，并严格比较两个统一缩放所定义的曲线集合。

## 1. 同一准确对象

仍以保存系数的准确二进有理值定义

$$
\gamma(\theta)=\operatorname{Re}\sum_{k=-95}^{95}c_ke^{ik\theta},\qquad
J(\theta)=|\gamma'(\theta)|,\qquad
 a_\gamma=\frac1{2\pi}\int_0^{2\pi}J(\theta)\,d\theta.
$$

系数实配对、常数项 $C$、coast master SHA 和前缀输入身份都与 R224 相同；没有重新采样生成另一条曲线。准确目标仍是

$$
f_0=\frac{P(7/5,1/2)}{2\pi}+\frac12\frac9{200}\frac3{50}.
$$

原有限 consumer 保存的周长数和目标数在此例相同，准确二进有理值均为

$$
\bar a=\bar f_0=\frac{1132016738664887}{1125899906842624}.
$$

这项浮点相等不被当作 $a_\gamma=f_0$ 的证明。

## 2. 整个圆周上 $J^{(4)}$ 的包含界

沿用 R224 的 2048 个完整角块及严格 Fourier Taylor 盒。写
$p=\gamma'$、$q=\gamma''$、$r=\gamma'''$、$s=\gamma^{(4)}$、$t=\gamma^{(5)}$，令 $E=p\cdot p$。前四个向量来自每个完整角块的包含盒；第五导数逐分量使用准确全局界

$$
|t_d|\le\sum_{k=1}^{95}k^5\bigl(|a_{k,d}|+|b_{k,d}|\bigr).
$$

准确微分恒等式为

$$
E'=2p\cdot q,\quad E''=2(q\cdot q+p\cdot r),\quad
E'''=6q\cdot r+2p\cdot s,
$$

$$
E^{(4)}=6r\cdot r+8q\cdot s+2p\cdot t.
$$

由于全部角块已经证明 $J>0.4037683$，平方根链式法则在整个域合法，给出

$$
J^{(4)}=\frac{E^{(4)}}{2J}
-\frac{E'E'''}{J^3}-\frac{3(E'')^2}{4J^3}
+\frac{9(E')^2E''}{4J^5}-\frac{15(E')^4}{16J^7}.
$$

将上述完整盒带入该式，所有四则运算、平方根和三角函数均用 R224 的 96-bit dyadic 向外舍入；没有以若干导数采样值猜全域最大值。2048 块的统一严格结果是

$$
\|J^{(4)}\|_\infty\le
\frac{3850323026322201903589140919867}{19807040628566084398385987584}
<194.391636.
$$

本次各块的准确整数行流 SHA256 为
`b5a289172d7012e700d400ca0b8bf393390ac21967b8861df81e70ae059b39d3`。

## 3. 严格 Simpson 积分

令 $N=4096$、$h=\pi/N$，定义准确周期节点的两组均值

$$
T_N=\frac1N\sum_{j=0}^{N-1}J(2jh),\qquad
M_N=\frac1N\sum_{j=0}^{N-1}J((2j+1)h),\qquad
S_N=\frac{T_N+2M_N}{3}.
$$

这是 $2N$ 小区间复合 Simpson 公式的平均积分。周期性把两端相同的 $J(0),J(2\pi)$ 合并，所以仅需 8192 个不同节点。其完整余项满足

$$
|a_\gamma-S_N|\le\frac{h^4}{180}\|J^{(4)}\|_\infty
\le\frac{14805202641388965}{39614081257132168796771975168}
<3.737359\times10^{-13}.
$$

这里的所有节点值也按准确系数、严格 $\pi$ 和三角余项包含计算，未忽略有限求值舍入。加上该有理余项后，得到

$$
\frac{79658596287913338895451555727}{79228162514264337593543950336}
\le a_\gamma\le
\frac{79658596287972559706017116211}{79228162514264337593543950336}.
$$

实际包含半宽恰为

$$
\frac{14805202641390121}{39614081257132168796771975168}
<3.737359\times10^{-13}.
$$

它比目标 $10^{-12}$ 更小；区别于重复两次浮点求积近似一致，这里已支付连续四阶导数和求积余项。对保存的有限周长数，还严格有

$$
|a_\gamma-\bar a|<3.739\times10^{-13}.
$$

## 4. 两个统一缩放的集合误差

把准确规范化和保存数值比例所定义的同一原始曲线集合分别写为

$$
\Gamma=C+\frac{f_0}{a_\gamma}(\gamma-C),\qquad
\bar\Gamma=C+\frac{\bar f_0}{\bar a}(\gamma-C).
$$

每个准确目标、周长和商都继续用包含运算；结果为

$$
\left|\frac{f_0/a_\gamma}{\bar f_0/\bar a}-1\right|<3.718\times10^{-13}.
$$

对各 Cartesian 分量的 Fourier 绝对系数和给
$\sup_\theta|\gamma(\theta)-C|<1.511027$。用同一个 $\theta$ 配对两条曲线，便得

$$
d_H(\Gamma,\bar\Gamma)
\le\left|\frac{f_0}{a_\gamma}-\frac{\bar f_0}{\bar a}\right|
\sup_\theta|\gamma(\theta)-C|
\le\frac{44502846682086983}{79228162514264337593543950336}
<5.618\times10^{-13}.
$$

这是完整曲线**集合**的上界。$\bar\Gamma$ 明确表示保存比例缩放同一准确原始曲线后的集合，并不把有限反函数或插值评估器的逐点输出误差自动包进去。非线性 R137 coast 的完整位置两 jet、部分弧长积分、材料角反函数以及实际数值角导数仍需各自控制；本条不声称这些已全部小于上面的集合误差。

## 5. 源码与真实进程

源码为 [`6a65-gap105-rigorous-perimeter-simpson.py`](../scripts/6a65-gap105-rigorous-perimeter-simpson.py)，SHA256
`741bce50d1765e2d38c79fa2fc0d9285fcd15c476ef54173768fcac88e229b6d`。
它在相同 prefix report / coast master 上运行，并复用 R224 已列明的完整整数算术、局部 Taylor 盒与准确椭圆周长源；运行前后均核 SHA。命令为

```bash
python -u scripts/6a65-gap105-rigorous-perimeter-simpson.py \
  --scripts-dir scripts \
  --prefix-report /tmp/gap105-v045-prefix01-report.json \
  --coast-master /tmp/gap105-v045-prefix01-coast-master.npz \
  --out /tmp/gap105-v045-perimeter-simpson01.json \
  --derivative-cells 2048 --target-half-width 1/1000000000000
```

真实外部进程自 2026-11-26 10:38:51.415398 UTC 至 10:39:16.833786 UTC，自然 exit **0**，25.418415056 秒，峰值 RSS 33188 KiB；内部计时 25.243805429 秒。输出报告的退出字段留 null，由外部 process receipt 确认实际退出。

| 实际原件 | SHA256 |
|---|---|
| coast master | `f2c834f5b2b9d1471eabb64a3be0edcc7b6f8454f8c98d68793a60c782c46b4d` |
| prefix report | `c574b9a3c0be2cd5cc6db432a8fbb527466a5689b0a09c7da9b5f886a02da437` |
| 本次完整 scalar report | `4c8f3ab787b2b3262132ea5c77008cb2953262751f0e7440f14614ae1faf7b14` |
| stdout | `b886004279e5e5a591fc68c8382d135d678709cb4185960255eeb8d8371a3ee9` |
| 外部 process receipt | `b7eaee6c3004e24aef27250c08a9340aade96343acf41a9c60cb4be01a99b137` |

可重算原件只在临时目录，仓库保完整定义、源码与本条严格论证。未完成的 ramp、实际全尾接合、全时闭族 metric 和 reach 仍继续。
