# R61：径向斜率与中心速度联合投影、必要下界和局部重构

日期：2026-11-14。repo_sources 独立推导，root 与 mechanism 全文交叉复核。本文只有纸面恒等式与证明，没有评价研究候选、没有执行优化，也不改变已冻结源码。

本稿接 [R57](R57-direct-reconstructed-metric-and-auxiliary-frame-space.md) 和 [R59：逐圈中心速度消元](R59-scalar-center-speed-elimination-and-metric-lower-bounds.md)。目的在于区分给定角切向本身的相容性与目前选择的径向半径、中心速度。它不给一个已经可拼接的中心函数或度量。

## 1. 准确重构与放开径向斜率的范围

设角平均为归一化积分，角变量为周期为 $2\pi$ 的 $\theta$。取

$$
|T|=1,\qquad \langle T\rangle=0,\qquad
P=\Pi T,\qquad Q=\Pi T_t,
$$

其中 $\Pi$ 是准确的零均值周期原函数。于是

$$
\langle P\rangle=\langle Q\rangle=0,\qquad
X=aP+ze_z,\qquad U=X_t=a'P+aQ+be_z,\quad b=z'.
\tag{1}
$$

参考度量为 $dt^2+a(t)^2d\theta^2$，且

$$
E=|U|^2,\qquad q:=F/a=U\cdot T,\qquad G/a^2=1.
\tag{2}
$$

以下首先固定一条圈上的 $T,T_t$ 和正数 $a$，把两个实数 $a'$、$b$ 暂时放开。

**如果整个参考函数 $a(t)$ 已冻结，其导数 $a'(t)$ 也已经确定。** 联合消元在这种情形下只是扩大可选集合得到的必要下界；不能把消元得到的新 $a'$ 当作同一个 $g$ 内可以直接采用的参数。若在设计 $g$，各圈选出的 $a'$ 仍必须是同一个 $a$ 的真正导数。

## 2. 两维函数子空间的准确投影

在实 Hilbert 空间 $L^2(S^1,d\theta/(2\pi))$ 中定义

$$
f_1=P\cdot T,\qquad f_0=Q\cdot T,\qquad f_2=T_z,
\qquad \mathcal S=\operatorname{span}\{f_1,f_2\}.
$$

令 $x=a'/a,\ y=b/a$。由 (1)–(2) 有

$$
\boxed{q=a(f_0+xf_1+yf_2).}
\tag{3}
$$

因此

$$
\boxed{
\min_{a',b\in\mathbb R}\langle q^2\rangle
=a^2\,\operatorname{dist}_{L^2}(f_0,\mathcal S)^2.
}
\tag{4}
$$

这是真实函数子空间的距离，并不假设 $f_1,f_2$ 线性独立。证明只是把 (3) 的两个实系数看成到有限维闭子空间的正交投影。

写出 Gram 矩阵及交叉矩

$$
G=\begin{pmatrix}
\langle f_1^2\rangle&\langle f_1f_2\rangle\\
\langle f_1f_2\rangle&\langle f_2^2\rangle
\end{pmatrix},\qquad
h=\binom{\langle f_1f_0\rangle}{\langle f_2f_0\rangle},
\qquad n=\langle f_0^2\rangle.
$$

用 $G^+$ 表示准确的 Moore–Penrose 伪逆，则

$$
\boxed{\rho:=\operatorname{dist}(f_0,\mathcal S)^2
=n-h^{\mathsf T}G^+h\ge0.}
\tag{5}
$$

这里 $h$ 总在 $G$ 的值域内。若 $v\in\ker G$，则
$\|v_1f_1+v_2f_2\|_2^2=v^{\mathsf T}Gv=0$，从而
$v^{\mathsf T}h=\langle(v_1f_1+v_2f_2)f_0\rangle=0$。
因此正常方程 $G(x,y)^{\mathsf T}=-h$ 可解，而且全部最小点是

$$
\binom xy=-G^+h+\ker G.
\tag{6}
$$

如果 $G$ 正定，最小点唯一，为 $-G^{-1}h$。如果秩为一，必须保留 (6) 的一维自由度。若 $G=0$，则 $f_1=f_2=0$，下界为 $a^2n$；此时只有 $f_0=0$ 才能消去 $F$，而消去以后 $x,y$ 仍未被 $F$ 决定。

对连续函数，$\rho=0$ 等价于 (6) 的某个最小点使 $q$ 全角为零；这里使用连续性把几乎处处零提升为逐点零。

## 3. 真正相对度量误差的必要下界

令

$$
\eta(\theta)=
\left\|\begin{pmatrix}E-1&q\\q&0\end{pmatrix}\right\|_{\mathrm{op}}
=\frac{|E-1|+\sqrt{(E-1)^2+4q^2}}2.
$$

逐点有 $\eta\ge |q|$。所以对任意实数 $a',b$，

$$
\boxed{\sup_\theta\eta\ge a\sqrt{\rho}.}
\tag{7}
$$

若要求全角误差不超过 $\varepsilon$，必有
$\rho\le\varepsilon^2/a^2$。若 $\rho>0$，则在当前 $T,T_t,a$ 下，即使把径向斜率和中心速度都自由化，也不能得到准确等距。

这个下界没有把各圈独立挑出的 $a'$ 或 $b$ 拼起来。它忽略形状包络、端口、导数一致性和中心积分，因而只能作为必要门。放开变量使可选集合扩大，下界弱于或等于只允许当前 $a'$、仅消去 $b$ 时的最优 $F$ 下界。

## 4. 全角 E 条件不能被投影替代

假设 $\rho=0$，取 (6) 中的一个解，并定义

$$
D(\theta)=Q+xP+ye_z.
$$

此时 $D\cdot T=0$，且 $U=aD$。准确 $E=1$ 还要求

$$
\boxed{|D(\theta)|^2=a^{-2}\quad\text{在整个角圈上}.}
\tag{8}
$$

不能只检查 $\langle|D|^2\rangle=a^{-2}$。当 $G$ 正定时，$x,y$ 已由 $F$ 唯一确定，所以 (8) 是额外的全角条件；不再有可任意调整的逐角中心速度。

在奇异情形，必须沿 (6) 的整个仿射解集再检查 (8)。伪逆给出的最小欧氏范数系数只是一个代表，未必是满足 $E$ 或端口的那个代表。

## 5. 允许设计整个 a 时的径向一致性

考虑一个开放径向区间，其中 $G(t)$ 正定，$\rho(t)=0$。令 $x(t),y(t)$ 为唯一投影系数，并设

$$
S(t)=\langle|Q+xP+ye_z|^2\rangle.
$$

如果该区间上确有准确等距实现，则必须同时满足：

1. $S>0$，且 $|Q+xP+ye_z|^2=S$ 全角成立；
2. $a=S^{-1/2}$，$b=ay$；
3. $x=a'/a$，即

$$
\boxed{S'=-2xS.}
\tag{9}
$$

第三项把不同径向圈耦合起来。逐圈的投影解和角常量条件本身不会自动给出 (9)。规定的入口半径还必须等于入口处的 $S^{-1/2}$；不能再任意乘一个半径常数而保持已经固定的单位径向坐标。

反过来，若上述条件准确成立，并且由此定义的 $a$ 为 $C^2$、$b$ 为 $C^1$，而 $T$ 联合 $C^2$，取一个共同的

$$
z(t)=z(t_0)+\int_{t_0}^t b(s)\,ds,\qquad X=a\Pi T+ze_z
$$

就有 $E=1,F=0,G=a^2$，得到该开放区间上的准确 $C^2$ 等距浸入。证明直接代入 (1)、(3)、(8)、(9)；其中 $a>0$ 保证面积元非零。

这只是带明确正则性前提的局部重构判据，不支付端口匹配、全局单射、两侧闭合、共同固定片、reach 或宏观位移。核心、平帽或其他位置的 Gram 秩可能下降，不能把正定分支的逆矩阵公式未经检查延伸过去；应回到 (4)–(6) 和实际端口条件。

## 6. 一个独立的 E 均值必要门

由 $\langle P\rangle=\langle Q\rangle=0$，

$$
\langle E\rangle
=(a')^2p+2aa'c+a^2d+b^2,\qquad
p=\langle|P|^2\rangle,\quad
c=\langle P\cdot Q\rangle,\quad
d=\langle|Q|^2\rangle.
$$

这里 $p>0$：否则连续的 $P$ 全零，便与 $P_\theta=T$、$|T|=1$ 矛盾。对实数 $a',b$ 完全平方得到

$$
\min_{a',b}\langle E\rangle
=a^2\left(d-\frac{c^2}{p}\right)\ge0.
$$

所以另有

$$
\boxed{\sup_\theta\eta\ge
\max\left\{0,\ a^2\left(d-\frac{c^2}{p}\right)-1\right\}.}
\tag{10}
$$

(7) 和 (10) 的最小点未必相同。可以取两个必要下界的最大值，不能把两项当作同时达到的最优解，也不能无证明地把它们相加。

## 7. 后续数值诊断的边界

若以后在公开 Actions 中实现，只需固定状态的 $P,Q,T,a$ 及角积分。应记录 Gram、交叉矩、函数残差、采用的秩判断及当前真实 $a',b$，并与 GH、周期原函数和角积分的同参数加密分开。

有限采样 Gram 的小特征值不是准确函数线性相关的证明。尤其不能把一个数值小特征值直接截成零，再把抬高的投影残差当作严格下界：这会缩小被允许的真实子空间，可能造成假排除。病态情况下应报告秩未认证；严格下界需要连续积分的定向包围和合法的矩阵误差控制。

同样，浮点计算 (5) 若因消差出现负数，截为零只能是显示或离散诊断约定，不是准确误差证书。未经连续认证，不得将采样结果改称题目已经排除或通过。

本文不选择新的优化权重或预算，不改变任何实际系数，也不把一个逐圈松弛最优点当作完整连接。

