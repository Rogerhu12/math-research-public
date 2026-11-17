# R623. 有限材料角高度的平面圈唯一性与最高模缺陷传递

日期：2026-11-17。会话：Astra-larger-parallel-16f63c8b / constructive_model。

**状态：已证明的模型筛选及条件估计；不是闭曲面构造，也不是本课题完成。**

本条区分材料角与几何角。结论只针对在旋转度量的材料角中带宽有限的**高度函数**，不针对经非线性材料角换元后的有限物理 Fourier 场。它不要求每层数值近似字面精确等距，也不否定随带宽增加的收敛近似。现有 R257 处理恒速平面闭曲线的有限 Cartesian Fourier 圆障碍，本条的对象和方程不同。

## 1. 问题与准确最高模方程

设 $J=[s_0,s_1]$ 是紧区间，$a\in C^2(J)$，且

$$
a>0,\qquad a'\ne0\quad\text{于 }J.
$$

在 $J\times\mathbb S^1$ 上取旋转度量

$$
g=ds^2+a(s)^2d\theta^2.
$$

设实高度函数在共同材料角中有有限 Fourier 表示

$$
z(s,\theta)=\sum_{j=-N}^N c_j(s)e^{ij\theta},
\qquad c_j\in C^2(J;\mathbb C),\quad c_{-j}=\overline{c_j}.
\tag{1}
$$

若 $z$ 是某个 $C^2$ 等距浸入的一个欧氏坐标，则它满足 Darboux 恒等式

$$
z_{ss}(z_{\theta\theta}+aa'z_s)
-\left(z_{s\theta}-\frac{a'}a z_\theta\right)^2
=-aa''\left(1-z_s^2-\frac{z_\theta^2}{a^2}\right).
\tag{2}
$$

这里不是额外的存在假设：等距浸入时 $\nabla_g^2z$ 等于第二基本形式乘法向量的相应欧氏分量，$1-|\nabla_gz|^2$ 等于该分量的平方；结合 Gauss 方程及 $K_g=-a''/a$ 得到 (2)。证明后续只使用 (2)，所以也适用于并未预设已重建浸入的准确 Darboux 解。

令 $m\ge1$ 是 (1) 当前最高正频率，记 $c=c_m$。取 (2) 的 $e^{2im\theta}$ 系数，得到

$$
(aa'c'-m^2c)c''
+m^2\left(c'-\frac{a'}a c\right)^2
=aa''\left(c'^2-\frac{m^2}{a^2}c^2\right).
\tag{3}
$$

逐项核对如下。$z_{ss}$ 在模式 $m$ 的系数是 $c''$；第二个括号的系数是 $aa'c'-m^2c$；混合项的系数是 $im(c'-a'c/a)$。平方后 $i^2=-1$，故 (3) 左边的平方项取正号。右边模式 $2m$ 的系数是 $aa''(c'^2-m^2c^2/a^2)$。模式和为 $2m$ 时两项只能都是 $m$，所以所有低模及 $c_0$ 都不进入 (3)。该推导允许复 $c$，无需事先选择纯 cosine 相位。

## 2. 对最高模方程的定量唯一性

定义有限常数

$$
\mu=\min_J |aa'|>0,\qquad
B=\max_J\left|\frac{a'}a\right|,
\qquad A_1=\max_J|aa''|,
\qquad A_2=\max_J\left|\frac{a''}a\right|.
$$

任选

$$
L\ge \frac{2m^2}{\mu},\qquad L>0,
$$

并置

$$
C_0=A_1+\frac{m^2A_2}{L^2}
+m^2\left(1+\frac B L\right)^2,
\qquad C=\max\left(2L,\frac{4C_0}{\mu}\right).
\tag{4}
$$

更一般地，令 $r\in C(J;\mathbb C)$，假定 (3) 的左边减右边等于 $r$。则

$$
Y(s)=\max\{L^2|c(s)|^2,|c'(s)|^2\}
$$

满足对 $s\ge s_0$ 的估计

$$
Y(s)\le e^{C(s-s_0)}Y(s_0)
+\frac4\mu\int_{s_0}^{s}e^{C(s-u)}|r(u)|\,du.
\tag{5}
$$

**完整证明。** 因 $c\in C^2$，$Y$ 局部 Lipschitz，因此只需证明几乎处处的微分不等式。若 $|c'|\ge L|c|$ 且 $Y>0$，则

$$
|aa'c'-m^2c|
\ge\mu|c'|-m^2|c|
\ge\frac\mu2|c'|>0.
$$

由带余项的 (3) 和三角不等式，

$$
|c''|\le \frac{2C_0}{\mu}|c'|
+\frac{2|r|}{\mu|c'|}.
$$

因此在 $|c'|^2$ 是最大分支的点，

$$
\left|\frac d{ds}|c'|^2\right|
\le2|c'||c''|
\le\frac{4C_0}{\mu}Y+\frac4\mu|r|.
$$

在 $L^2|c|^2$ 是最大分支的点，

$$
\left|\frac d{ds}L^2|c|^2\right|
\le2L^2|c||c'|\le2LY.
$$

两分支相等处，Lipschitz 最大值的上导数受相应分支导数最大值控制。若 $Y=0$，两平方分支的导数均为零，未使用除以 $|c'|$ 的公式。故几乎处处

$$
Y'\le CY+\frac4\mu|r|.
$$

乘以 $e^{-Cs}$ 后积分即得 (5)。以上实际证明了绝对导数版本，所以倒转径向方向后同一估计成立。证毕。

特别地，当 $r=0$ 且 $c(s_*)=c'(s_*)=0$ 时，在 $s_*$ 左右分别应用 (5)，得到 $c\equiv0$ 于整个 $J$。这里没有用到解析唯一延拓、椭圆性或 $a''$ 的符号；允许 $a''$ 无限次变号。

## 3. 有限带宽准确高度不可能从径向平面圈启动

**定理。** 在第 1 节条件下，若 (1) 满足准确 Darboux 方程 (2)，并在某个 $s_*\in J$ 满足

$$
c_j(s_*)=c'_j(s_*)=0\qquad (j\ne0),
\tag{6}
$$

则 $z$ 在整个 $J\times\mathbb S^1$ 上仅依赖 $s$。

**证明。** 若最大频率为 $N$，第 2 节对 (3) 给出 $c_N\equiv0$；实值条件给 $c_{-N}\equiv0$。把这对模式从表示中删去，对余下最高模重复同一论证。有限归纳后所有非零模式都消失。证毕。

特别地，高度在一个径向端附近恰为角无关常数时必满足 (6)。结论也适用于“与一个径向高度的一阶 jet 匹配”，不要求整个开圈都是平面。

对常用的半径坐标度量

$$
g=E(r)dr^2+r^2d\theta^2,\qquad E\in C^1,\quad E>0,
\qquad r\in[r_-,r_+],\quad r_->0,
$$

取 $ds=\sqrt{E(r)}\,dr$ 后 $a(s)=r$ 且 $a'=1/\sqrt E>0$。只要换元后满足上述 $C^2$ 正则性，定理覆盖整条环带；不能通过选择符号反复变化的 $E'$ 或 Gauss 曲率而绕开它。

## 4. 对非零最高模的残差下界

若 $Y(s_0)=0$、$|r|\le\varepsilon$，(5) 给出

$$
Y(s)\le\frac{4\varepsilon}{\mu C}
\left(e^{C(s-s_0)}-1\right).
$$

因此一旦某处 $|c(s)|\ge\eta>0$，必有

$$
\varepsilon\ge
\frac{\mu C L^2\eta^2}
{4\left(e^{C(s-s_0)}-1\right)}.
\tag{7}
$$

这是**这个固定带宽表示**的准确最高 Fourier 缺陷的条件下界，非浮点采样断言。$m$ 增大时常数很差，不能从 (7) 推出全带宽逼近的统一正误差地板。它没有将 Darboux 缺陷未经证明地等同于课题 README 的全域相对 Gram 误差。

## 5. 对构造路线的具体作用及尚未解决的部分

1. 直接尝试 $z=b(s)+c(s)\cos(m\theta)$ 并让 $c,c'$ 在一个平面圈为零，在 $a'\ne0$ 区域内不可能产生非径向的准确解。无需继续在这一个有限维准确 ansatz 内调参。
2. 不能把“仅保留少数材料模的准确闭合解”当作现有非轴对称完整场的便宜替代。可用的表示必须允许无限材料谱，或允许谱数随精化增加；有限物理角参数化经非线性角换元可以具有无限材料谱。
3. 定理不处理 $a'=0$ 的纬圈，不能据此排除其它度量或其它拓扑；更不能推出闭曲面刚性。
4. 固定 $g$ 后，随着径向与角分辨率增加，数值误差下降至求解容差仍然完全符合原 README。每层有限近似无需满足 (2) 的字面零残差。
5. 目前没有从本条得到满足 $\delta_{\rm hold}/D\ge0.2$、reach$/D\ge0.03$ 的闭面。它是一条路线筛选和误差传递结果；后续正向研究需使用无限材料谱，并实际解决两侧平面圈及全局几何。

## 6. 已核文献边界

- I. Kh. Sabitov, *Bendable Surfaces without Visible Deformations of Their Shape*, Mathematical Notes 110 (2021), 126–134, DOI [10.1134/S0001434621070130](https://doi.org/10.1134/S0001434621070130)。[MathNet 作者摘要](https://www.mathnet.ru/eng/mzm13037)明确其滑动弯曲保持像集；这本身不能提供本题要求的正 Hausdorff 形变。
- I. Kh. Sabitov, *Infinitesimal Sliding Bendings of Compact Surfaces and Euler's Conjecture*, Siberian Mathematical Journal 64 (2023), 1213–1228, DOI [10.1134/S0037446623050130](https://doi.org/10.1134/S0037446623050130)。[MathNet 作者摘要](https://www.mathnet.ru/eng/smj7815)声明其关于亏格零旋转曲面的结论限定于滑动弯曲类，不能当作一般闭曲面可弯曲/不可弯曲的定理。
- Ivan Izmestiev, Arvin Rasoulzadeh, Jonas Tervooren, *Isometric Deformations of Discrete and Smooth T-surfaces*, [arXiv:2302.08925v1](https://arxiv.org/abs/2302.08925v1), 2023，§5.2–5.4，特别是 Theorems 5.4–5.7。显式局部族尚需另付整圈周期、闭面光滑性及嵌入条件；Theorem 5.6 的旋转子类把原角参数除以 $\sqrt{1+t}$，不直接保持整圈周期。
- Hussein Nassar, *Isometric Deformations of Surfaces of Translation*, [arXiv:2310.08505v1](https://arxiv.org/abs/2310.08505v1), 2023，Theorem 4 及其后讨论（PDF pp. 10–11）。一般公式不保持闭合；在高度极值处可能出现新的折痕。不能将其局部/分片光滑存在式直接作为本题闭 $C^2$ 候选。

本条 (3)–(7) 的证明由上文直接给出，不把这些文献的局部存在结果作为证明中的外部输入。
