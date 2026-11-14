# 六点函数的均方恒等式及其边界

日期：2026-11-13。R174 的独立附注，不修改其已冻结正文。

沿用 R174 的 $k=\mathbb F_{p^2}=\mathbb F_p(\tau)$、$\tau^2=z$ 非平方、$p+1=3d$、$H=\overline C^3$、$T_H=H\setminus\{c_\infty\}$ 的仿射参数和 $A_H$。定义
$$F_a(w)=\sum_{\kappa\in\mu_6}
\psi(-\operatorname{Tr}(\tau w\kappa))
A_H\left(N(w\kappa-a)/a\right).$$
上横线在本篇恒等式中表示圆分系数的形式复共轭；模一个指定素理想时，不能未经论证认为该素理想也由此共轭保持。

有精确恒等式
$$
\boxed{\sum_{w\in k}F_a(w)\overline{F_a(w)}
=6p^2(d-1)-6p(d-2)F_a(a).}
\tag{1}
$$

## 证明

展开 $A_H$，单项相位是
$$\frac ta Nw-\operatorname{Tr}((t+\tau)\kappa w)+at.$$
均方中的两个参数记为 $(t,\kappa)$ 和 $(s,\lambda)$。若 $t=s$，加性正交仅在 $\kappa=\lambda$ 时有贡献，总计 $6(d-1)p^2$。

若 $t\ne s$，对 $w$ 的各向异性二元二次 Gauss 和为 $-p$。置 $r=\kappa/\lambda\in\mu_6$；对每个 $r$ 有六对 $(\kappa,\lambda)$。完成平方后的相位为
$$a(\operatorname{Tr}r-2)\frac{ts-z}{t-s}
-a\operatorname{Tr}(\tau r).$$
参数
$$q=\frac{ts-z}{t-s}$$
来自 Cartan 商 $c_t c_s^{-1}$ 的仿射参数取负。由于 $H$ 对乘法和取逆封闭，$q\in T_H$。对每个固定 $q$，恰有 $d-2$ 对 $t,s\in T_H$：在 $H$ 中固定一个非单位商，有 $d$ 对有序因子，排除因子之一为单位的两对。

所以非对角贡献为
$$-6p(d-2)\sum_{r\in\mu_6}
\psi(-a\operatorname{Tr}(\tau r))
A_H(a(\operatorname{Tr}r-2)).$$
$T_H=-T_H$，故 $A_H(-y)=A_H(y)$；并且 $N(r-1)=2-\operatorname{Tr}r$。这最后一和恰为 $F_a(a)$，证明 (1)。

## 为什么它本身不排全支撑式

若某个剩余嵌入下有 R174 的全支撑式
$$F_a(w)=p\,1_{w\in a\mu_6},$$
并且其共轭式在该嵌入下也成立，则均方左边为 $6p^2$，右边也恰为
$$6p^2(d-1)-6p^2(d-2)=6p^2.$$
因此即使补足共轭的同素理想接口，(1) 也不给矛盾。只用对角值、总和或均方会丢失需要排除的完整支撑信息；下一步须利用全函数等式本身。

本篇用的是实际 $H$ 乘法所给的每个商 $d-2$ 对计数，不适用于任意人为三分割。它不提供新的分母上界或完整非消失结论。
