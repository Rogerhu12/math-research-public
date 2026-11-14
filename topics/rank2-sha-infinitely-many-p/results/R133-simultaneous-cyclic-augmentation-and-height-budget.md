# R133. 同一辅助素数的全精度导数、整 CRT 与实际高度

日期：2026-11-12。状态：已证明；没有证明原点的二阶导出消失。

完整证明见
[同一辅助素数的整增广条件](../notes/2026-11-12-simultaneous-cyclic-augmentation-and-height-budget.md)。
取实际循环扩张 $K/F$、$\Gamma=C_m=\langle\sigma\rangle$、
无挠 MW 格 $G$、$W=\ker N$，及原 Heegner 类数二迹点
$X=(1+\tau_3)P[\ell]\in W$（必要时先乘 $2$）。

## 1. 全精度与导数阶准确分离

若 $m=n=p^e$、$p$ 为奇数，令
$D^{(k)}=\sum_{j<n}\binom jk\sigma^j$、$I=\sigma-1$，则
$$
 ID^{(1)}=n-N,\qquad ID^{(2)}=\binom n2-\sigma D^{(1)}.
$$
因此
$$
 D^{(1)}X\in nG\iff X\in IW,
$$
而在 $p$ 进完成中
$$
 D^{(1)}X,D^{(2)}X\in p^eG_p\iff X\in I^2W_p.
$$
第二式使用单位 $((n-1)/2)I-\sigma$，其 augmentation 为 $-1$。
一次导数在全部 $p^M$、$M\le e$ 精度消失，只给第一式；最高
精度已包含低精度，不能由此自动得到第二式。

## 2. 真实 prime-power 迹的整 CRT

对 $p^e\Vert m$，置 $u_p=m/p^e$、$|U_p|=u_p$、
$Q_p=N_{U_p}X$、$\sigma_p=\sigma^{u_p}$。则
$$
 X\in I^kW_p
 \iff Q_p\in(\sigma_p-1)^k(W^{U_p}\otimes\mathbb Z_p).
$$
证明使用整 idempotent $N_{U_p}/u_p$；其补块上的 $I$ 是单位。
所有 $p\mid m$ 的这些条件准确拼成整 $I^k$ 像；若遗漏固定有限
素数，只能先在倒置它们的格中拼接。实际清分母可取 $m_S^k$。
只取次数 $p$ 商时，不能顺便控制次数 $p^2,p^3$ 的块。

## 3. 高度预算按正交和计算

真实整数迹满足
$$
 \sum_{p\mid m}\frac{\widehat h(Q_p)}{u_p^2}
          \le\widehat h(X).
$$
这是不同 prime-power 角色块的正交投影公式。
不能对 $Q_p/u_p$ 应用整数点的 Baker 下界。
全部低导子投影的统一清分母为
$\operatorname{lcm}_{p\mid m}u_p=m$（至少两个素因子时）；
在整个正规表示的增广格上，该分母是尖锐的。

若真实循环轨道的非零低导子块集合为 $\mathcal D$，则
$$
 \dim V_{\rm low}=\sum_{d\in\mathcal D}\varphi(d),\qquad
 |\det(I|V_{\rm low})|=\prod_{p^r\in\mathcal D}p.
$$
故 $I^2$ 的 Gram 行列式增长须除以这个**总维数**取平均，
不是各自的 $p^{4/(p-1)}$ 无权相乘。

最后，固定 $61$ 的真实退化组合
$$
 X'=(\operatorname{Art}(1+2\sqrt{-15})-1)^2X
$$
来自一个非恒定的固定 $X_0(61^2\cdot3N_E)\to E$ 映射，
同时属于全群的 $I^2W$，且 $\widehat h(X')\asymp\log\ell$。
它是对高度预算的实际校准，**没有**替换原 Heegner 映射。
还须由原始映射的新算术输入支付二阶消失或非零测试；主目标仍开。
