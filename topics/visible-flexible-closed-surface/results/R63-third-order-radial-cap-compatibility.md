# R63：径向帽的三阶共振必要条件与完整核心积分

**状态：已证明；数学正文完整未参与者独立审查通过，root 已全文回读原稿与审稿。**

2026-11-10；Astra-visible-flex-78718bd0 / geometric_closure。

本稿继续 [R60 全二阶帽](R60-second-order-radial-cap-matching.md)，
把下一道三阶条件化为一个明确标量积分，并把球心无限区间贡献写成有限和。
这是固定旋转基态、指定一阶方向及参数正则性下的必要条件，不是非线性存在定理。
作者的浮点探索仅保存在 notes，未进入以下已证命题。

## 1. 准确范围

在 $0\le r<T$、$u\in\mathbb R/(2\pi\mathbb Z)$ 上，
记 $g=dr^2+a(r)^2du^2$、$b=(1-a_r^2)^{1/2}>0$，
$P=aa_{rr}/b^3$、$R=b/a^2$，并令
$\mathcal L_n h=(h_r/R)_r+n^2Ph$。基态第二形式为
$L_0=-a_{rr}/b,M_0=0,C_0=ab$；各阶变量为 $x_j=am_j,\zeta_j=bc_j/a$。

沿用二阶帽稿的开柱入口、圆球开核心、实单谐波
$n\ge2$、$D_n=0$ 与 $D_{2n}\ne0$。记一阶与二阶的规范分量为

$$
x_1=p\sin(nu),\quad\zeta_1=v\cos(nu),
\qquad
x_2=y\sin(2nu),\quad\zeta_2=z_0+z\cos(2nu).
\tag{1}
$$

其中 $v(0)=1,p(0)=0$；$z_0$ 是由真实柱边总转角及正则中心唯一确定的
零模，$(z,y)$ 是倍频非共振边值问题的唯一解。

下述必要条件适用于一个参数 Taylor 系数可与所需空间导数交换、前三阶系数空间光滑的真实共同
度量帽族，其入口为同材料周长 $2\pi$ 的平面单位速率闭柱边，且第一阶
曲率变化为 $\cos(nu)$。这里只谈该准确旋转基态和该第一阶方向，
例如在每个固定 $C^k$ 范数中对参数三次可微足够；仅逐点三次可微而不能交换空间导数者不在证明范围。
不排除其他基态、非径向度量、其他一阶方向或较低参数正则性的连续族。

## 2. 从 Gauss 方程取得三阶源

用无阶乘 Taylor 系数写

$$
L_\tau=L_0+\tau\ell_1+\tau^2\ell_2+\tau^3\ell_3+o(\tau^3),
$$

对 $M,C$ 使用同样约定。由于基态 $M_0=0,C_0=ab,L_0=-a_{rr}/b$，
Gauss 方程的三阶系数为

$$
ab\ell_3-\frac{a_{rr}}b c_3+\ell_1c_2+\ell_2c_1
=2m_1m_2.
$$

因此

$$
\ell_3=\frac{a_{rr}}{ab^2}c_3+S^{(3)},
\quad
S^{(3)}=\frac{2m_1m_2-2(a_{rr}/(ab^2))c_1c_2-Sc_1}{ab},
\tag{2}
$$

这里 $S=S_0+S_2\cos(2nu)$ 是已解二阶的真实强迫。
用 $\sin u\sin2u=(\cos u-\cos3u)/2$、
$\cos u\cos2u=(\cos u+\cos3u)/2$ 逐项展开，得到

$$
S^{(3)}=T_n\cos(nu)+T_{3n}\cos(3nu),
\tag{3}
$$

$$
\boxed{
T_n=\frac{py}{a^3b}
-\frac{a_{rr}v}{b^5}(2z_0+z)
-\frac v{b^2}\left(S_0+\frac{S_2}2\right),
}
\tag{4}
$$

$$
T_{3n}=-\frac{py}{a^3b}
-\frac{a_{rr}v}{b^5}z-\frac{vS_2}{2b^2}.
\tag{5}
$$

在入口开柱 $S_0=S_2=p=y=0,a_{rr}=0$，故两项源都为零。

## 3. 三阶 $n$ 模的必要兼容条件

三阶 Codazzi 与二阶具有相同线性部分，所以 $n$ 模的 $\zeta_3$ 满足

$$
\mathcal L_n\zeta_{3,n}=(a^2a_rT_n)_r-n^2aT_n,
\qquad (\zeta_{3,n})_r(0)=0.
\tag{6}
$$

由于 $v$ 本身满足柱端零导数与中心正则性，将 (6) 乘以 $v$ 并用
Green 恒等式得到必要条件

$$
\boxed{\quad
\mathfrak C_n(a)=
\int_0^T\bigl(a^2a_rv_r+n^2av\bigr)T_n\,dr=0.
\quad}
\tag{7}
$$

这里完整端点项为
$(v(\zeta_{3,n})_r-\zeta_{3,n}v_r)/R$ 和 $va^2a_rT_n$。
入口由开柱条件为零。中心对真正光滑变分有
$\zeta_{3,n}=O(\rho^2)$、$(\zeta_{3,n})_r=O(\rho)$，
同时 $v=O(\rho^n),v_r=O(\rho^{n-1}),R\asymp\rho^{-1}$，
故 Green 端项为 $O(\rho^{n+2})$。
由第 5 节的准确球核心表达，$T_n$ 在 $n=2$ 时为 $O(\rho^2)$，
在 $n>2$ 时至多为 $O(\rho^{3n-6})$，所以另一个端项也趋零，
被积函数绝对可积。这支付了 (7) 的真实中心取极限。

三阶入口曲率的 $n$ 振幅是 (6) 解的自由初值，但在共振情况下给它
加上任意常数倍 $v$ 都不改变 (7)。因此不能用这个边界振幅自动消去
三阶兼容。

## 4. 该标量不依赖遗漏的二阶齐次自由度

二阶源只含 $0,\pm2n$。零模由平面闭柱边总曲率和中心条件唯一决定；
$2n$ 模因 $D_{2n}\ne0$ 唯一决定。其他二阶分量只能是正则且柱端满足
零混合曲率的齐次解，其频率 $k$ 必须共振。

第一阶的支集为 $\{\pm n\}$。一个二阶频率 $k$ 在 (2) 的乘积中影响
$n$ 频率，当且仅当 $k=0$ 或 $k=\pm2n$。这些分量均已唯一确定。
所以即使真实族二阶另含其他共振齐次模态，(7) 仍是同一个标量。
这里不需要额外假设真实帽族具有 $n$ 折旋转对称。

二阶加上同一 $n$ 模只对应参数重标等部分自由度；它不影响这个三阶
$n$ 条件。若第一阶振幅改为 $c$，二阶规范解乘 $c^2$，积分 (7)
乘 $c^4$，因此非零振幅不能改变其是否为零。

## 5. 球核心的实际三阶源

在球核心有

$$
v=d t^n,\quad p=-\sigma d t^n,
\quad z=d_2t^{2n},\quad y=-\sigma d_2t^{2n},
$$

以及二阶稿的

$$
z_0=\frac{d^2}{4}
\left(\frac{t^{2n-2}}{2n-2}-\frac{t^{2n+2}}{2n+2}\right),
\quad
S_2=0,\quad S_0=\frac{\sigma^3d^2t^{2n}}{a^4}.
\tag{8}
$$

因此最高频源也精确消去：

$$
T_{3n}=0
\quad\text{在整个球核心上}.
\tag{9}
$$

但共振 $n$ 模源一般不消失。下面改用轴高坐标以写出它的完整积分。

## 6. 只需二阶导数的轴高 ODE

用大写 $A(Z)=a(r(Z))$，撇号表示 $d/dZ$，记
$\Lambda^2=1+(A')^2=b^{-2}$。一阶系统精确成为

$$
v'=\frac{np}{A^2},\qquad p'=-nAA''v.
\tag{10}
$$

令

$$
H_0=bS_0=\frac12\left(\frac{p^2}{A^3}-A''v^2\right),
\qquad
H_2=bS_2=-\frac12\left(\frac{p^2}{A^3}+A''v^2\right).
\tag{11}
$$

二阶方程是

$$
z_0'=A'H_0,\qquad
z'=\frac{2ny}{A^2}+A'H_2,
\qquad
y'=-2nAA''z-2nA\Lambda^2H_2.
\tag{12}
$$

对 $H_3=bT_n$，(4) 成为

$$
H_3=\frac{py}{A^3}-A''v(2z_0+z)
-\Lambda^2v\left(H_0+\frac{H_2}2\right).
\tag{13}
$$

因为 $dr=dZ/b$、$a_r=bA'$、$v_r=bv'$，(7) 精确化为

$$
\boxed{\quad
\mathfrak C_n=
\int\bigl(nA'p+n^2A\Lambda^2v\bigr)H_3\,dZ.
\quad}
\tag{14}
$$

所有 ODE 系数及积分只需 $A,A',A''$。不需要对插值数据求三阶、四阶
数值导数，也不需要把球心奇点作为数值网格端点。

## 7. 球核心贡献是一个有限和

设数值桥在球核心某处 $t=t_*>0$ 结束。该处之后直到中心的全部贡献
可精确积分。由

$$
A=\frac{2\sigma t}{1+t^2},\quad
A'=\frac{t^2-1}{2t},\quad
A''=-\frac{\sigma^2}{A^3},\quad
|dZ/dt|=\frac{4\sigma t}{(1+t^2)^2},
$$

得到

$$
H_3=
\frac{d^3}{32\sigma}t^{3n-5}(1+t^2)^3
\left(\frac{2-n}{n-1}-2t^2-\frac{n+2}{n+1}t^4\right)
+\frac{dd_2}{4\sigma}t^{3n-3}(1+t^2)^3.
\tag{15}
$$

式 (15) 也证明了第 3 节的中心阶数；在 $n=2$ 时常数括号的首项
为零，必须保留这个准确抵消。

定义两个低次多项式

$$
B_n(s)=(1+s)\bigl((n+1)+(n-1)s\bigr)=\sum_{j=0}^2b_js^j,
$$

$$
E_n(s)=B_n(s)\left(\frac{2-n}{n-1}-2s-\frac{n+2}{n+1}s^2\right)
=\sum_{j=0}^4e_js^j.
\tag{16}
$$

将 (15) 代入 (14) 后，球核心贡献准确为

$$
\boxed{
\mathfrak C_n^{\rm core}
=\frac{n\sigma d^4}{16}
\sum_{j=0}^4\frac{e_jt_*^{4n-4+2j}}{4n-4+2j}
+\frac{n\sigma d^2d_2}{2}
\sum_{j=0}^2\frac{b_jt_*^{4n-2+2j}}{4n-2+2j}.
}
\tag{17}
$$

分母对全部 $n\ge2$ 都非零。这是准确有限和，不是截断球心尾或
设置任意小半径截止。桥段与核心的 $d,d_2$ 必须来自同一已匹配解，
不能逐段独立选择。


## 8. 完整审查、证据身份与范围

作者 `geometric_closure` 的冻结原文
`notes/2026-11-10-78718-geometry-cubic-cap-v1.md`，8,656 B，SHA256
`bae8d9f081f85d08cf81539bcb01cb93b2125a1e774aee302abdf5ae86f9cbb9`。
其第8节只含作者的浮点探索，正式结果不据它断言任何精确共振零点。

未参与者 `independent_audit` 对第1–7节全部数学正文逐式重推，完整审稿
`notes/2026-11-10-78718-audit-cubic-cap.md`，14,263 B，SHA256
`a20fcc04f6982eb39f1462edf2454dca07caa27a1b3e7c87b60636d1d58fcb57`。
审者实际重放作者精确代数脚本，五项 PASS、自然 exit0；
这只核谐波展开、核心源、核心被积函数和 n=2 抵消，
不替代 Green 端项、真实空间光滑性及二阶自由度的纸面论证。

root 实际全文读原稿和完整审稿（本轮读取回执53cb43、236fbd），
独立核对 Taylor 系数约定、Gauss 源、模态选择、中心端项阶数、轴高的 b 因子
及核心积分方向，接受所述必要条件。正式版补明算子定义与参数正则性的准确含义。

本定理没有证明条件充分，未证明任何具体精确帽上该标量为零或非零，
不提供非线性帽、闭面、固定开 H、可见幅度或 G5。
独立者未参与本题新数值主候选的构造和调参。
