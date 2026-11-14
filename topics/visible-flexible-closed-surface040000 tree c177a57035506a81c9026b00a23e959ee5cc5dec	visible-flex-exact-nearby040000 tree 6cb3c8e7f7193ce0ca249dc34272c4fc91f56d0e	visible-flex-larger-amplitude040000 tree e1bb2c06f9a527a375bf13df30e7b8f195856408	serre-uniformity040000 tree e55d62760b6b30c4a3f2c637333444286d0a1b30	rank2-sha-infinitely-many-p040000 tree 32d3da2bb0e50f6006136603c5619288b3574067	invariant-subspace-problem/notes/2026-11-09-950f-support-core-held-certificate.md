# 当前实际支持系数的中央核心与握持见证

会话 Astra-visible-flex-950f9f73，2026-11-09。状态：完整条件证明及有理复算，待独审；不是完整闭曲面解。

## 1. 有限支持函数的精确几何

给定有限实数 $c_1,\ldots,c_M$，定义
$$h(\phi)=1+\sum_{j=1}^M c_j\cos(3j\phi),\quad
u(\phi)=(\cos\phi,\sin\phi),\quad
v(\phi)=(-\sin\phi,\cos\phi),$$
$$\gamma(\phi)=h(\phi)u(\phi)+h'(\phi)v(\phi),\qquad
\rho(\phi)=h+h''=1-\sum_j((3j)^2-1)c_j\cos(3j\phi).$$
若
$$L:=1-\sum_j((3j)^2-1)|c_j|>0,$$
则 $\gamma'=\rho v$ 处处非零。对固定方向 $u(t)$，
$$\frac{d}{d\phi}[\gamma(\phi)\cdot u(t)]=\rho(\phi)\sin(t-\phi).$$
故它在 $\phi=t$ 有全圆唯一最大值 $h(t)$，在 $\phi=t+\pi$ 有唯一最小值。这同时证明曲线单射和严格凸性：若两参数给同一点，以第一参数的法向取支持方向，违反唯一最大值。曲线闭合来自公式的周期性。

曲率为 $1/\rho$，因而全圆有
$$|\kappa|\le L^{-1}.$$
其周长精确为 $\int_0^{2\pi}\rho\,d\phi=2\pi$。若另有 $1-\sum_j|c_j|>0$，全圆支持为正，原点在内部。

## 2. 半个三重周期的精确径向差

再假设
$$c_1>\sum_{j=2}^M j^2|c_j|.$$
由 $|\sin(jx)|\le j|\sin x|$，$h'(\phi)$ 在每个三重周期内的符号与 $-\sin(3\phi)$ 相同。这一不等式可由有限几何级数
$\sin(jx)/\sin x=\sum_{k=0}^{j-1}e^{i(j-1-2k)x}$ 的模长界得到；零分母处用连续性。

又因
$$\frac{d}{d\phi}|\gamma|^2=2\rho h',$$
半周期端点给精确最大/最小半径：
$$R=1+\sum_jc_j,\qquad r=1+\sum_j(-1)^jc_j,$$
$$\Delta=R-r=2\sum_{j\ \mathrm{odd}}c_j>0.$$
这里端点 $h'=0$ 且 $h>0$，所以半径就是相应的 $h$ 值。

## 3. 对完整相位族的条件 held 下界

假设初始完整曲面包含中央柱 $\gamma\times[-\ell,\ell]$，其余点都满足 $|z|\ge\ell$，并且允许的相位包含中央柱绕轴转过 $\pi/3$ 的状态。该状态含点
$$p=(R\cos(\pi/3),R\sin(\pi/3),0).$$
原中央柱在方向 $u(\pi/3)$ 上的支持不超过 $r$，故 $p$ 到原柱的距离至少为 $R-r=\Delta$。它到其余原像的距离至少为 $\ell$。于是
$$\delta_{\rm hold}\ge\min\{\Delta,\ell\}.$$
此处没有刚体配准，也没有推出 $\delta_E>0$。固定握持区、非全等标记、精确共同metric和完整闭合仍是额外条件。

若中央截面实际使用另一个与 $\gamma$ 的 Hausdorff 距离至多 $\varepsilon$ 的平面曲线，并且仍按同一相位刚体旋转，则相同论证给
$$\delta_{\rm hold}\ge\min\{\Delta-2\varepsilon,\ell\}$$
（仅当右边为正才有意义）。这不能免除实际 $C^2$ 接缝核查。

## 4. M12 冻结前缀的系数证书

`scripts/950f-root-support-certificate.py` 把保存的每个 binary64 系数作为精确二进有理数，以 Fraction 逐项计算以上严格条件。输入是 `notes/2026-11-09-950f-prefix-adaptive-fixed-m12-summary.json`；输入哈希和全部精确分数见 `notes/2026-11-09-950f-root-m12-support-certificate.json`。

得到全圆曲率半径下界约 $0.3494885244$、绝对曲率上界约 $2.861324279$，以及精确支持差的浮点显示
$$\Delta\approx0.15995094481729163.$$
取 $\ell=4/25$ 后，若最终完整曲面的 $D\le31/10$，则有
$$\frac{\delta_{\rm hold}}D\ge
\frac{\Delta}{31/10}\approx0.05159707897>0.05.$$
允许的最大直径是 $20\Delta\approx3.19901889635$；此为条件预算，不是当前完整曲面的直径认证。

当前 M12 前缀的联合球包络采样给 $2\max|F|\approx3.02237695237$，只是留有余量的线索，不是连续上界，也未包含实际非线性尾、帽和标记。最终非线性耦合若改变核心系数，应以新系数重新执行本证书；不能把这里的数值当作与耦合无关的定理。
