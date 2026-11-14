# 二阶周期障碍的六项 Volterra 形式与有限多项式几何系数

**状态：已证明下面的代数及周期分部积分恒等式。** 它把完整二阶周期障碍化成有限个几何积分，不证明这些系数能同时消失，不证明非零参数下存在精确等距族。约定与 `literature-second-order-moments-20261114.md` 相同；本文是对该文 range 公式的独立推导与化简。

## 1. 固定渐近叶的导数

记 $k=\kappa$，$v=h^2>0$，$w=h^2-ku$，
$$z=\xi+\omega=h/u,\qquad \omega_s=k_s/(2h),\qquad
D=\partial_s|_\xi=\partial_s+c\partial_u,\quad c=Du.$$
所有几何函数沿周期 $s$ 光滑，$h,\omega$ 周期，活动条带中 $z>0$。记
$$K=\frac{wk-u}{u^2}+D\left(\frac c{u^2}\right)
=kz^2-\frac{k^2+1}{h}z-D^2(z/h).$$

对单个 profile $\phi\in C_c^\infty((\ell,r))$，取 $H=dY_\phi\cdot dY_\phi$，以及从 $\xi=r$ collar 起积分的法向坐标分量
$$\rho(s,u)=\frac12\int_{h/(r+\omega)}^u|Y_{\phi,u}(s,\tilde u)|^2d\tilde u.$$
单个平方 $H$ 一般不满足两端固定的第一相容条件；这里先定义其二次障碍表达式，最终对满足三矩相等的两个平方作差，或做交叉极化。

主体 note 中 $\mathcal A=H_F-\rho_s$、$\mathcal B=H_E/2+(wk-u)\rho$。由于 $D\rho=\rho_s+c\rho_u$，以及 $H(D,D)=H_E+2cH_F+c^2H_G$，有
$$\mathcal B+c\mathcal A=\frac12|DY_\phi|^2+(wk-u)\rho-cD\rho.$$
沿闭合 $\xi$ 叶分部积分，得到
$$\boxed{\mathcal O_\phi(\xi)=\oint\left\{\frac{|DY_\phi|^2}{2u^2}+K\rho\right\}ds.}\tag{1}$$
这是主体 note 的完整周期条件的二次表达；符号与从 $\xi=r$ 向 $\xi$ 积分的正 $u$ 方向相容。

## 2. 截断三个矩时必须保留的边界项

令 $\phi,\phi'$ 等不带自变量时均在当前 $\xi$ 取值，并记
$$J_0(\xi)=\int_\xi^r(\phi'')^2d\eta,\quad
J_1(\xi)=\int_\xi^r\eta(\phi'')^2d\eta,$$
$$J_2^*(\xi)=\int_\xi^r\eta^2(\phi'')^2d\eta
+2\int_\xi^r(\phi')^2d\eta.$$
以 $z_\eta=\eta+\omega$，$A=\phi'-z_\eta\phi''$，$B=\phi-z_\eta\phi'+z_\eta^2\phi''/2$，有
$$\int_\xi^r\frac{A^2}{z_\eta^2}d\eta=J_0+\frac{\phi'^2}{z},$$
$$\int_\xi^r\frac{AB}{z_\eta^2}d\eta
=-\frac{J_1+\omega J_0}{2}+\frac{\phi\phi'}z-\frac34\phi'^2,$$
$$\int_\xi^r\frac{B^2}{z_\eta^2}d\eta
=\frac{J_2^*+2\omega J_1+\omega^2J_0}{4}
+\frac{\phi^2}z-\phi\phi'+\frac z2\phi'^2.$$
这些式子可由主体 note 的三个积分逐项保留左端项得到，也可直接对 $\xi$ 求导并在 $\xi=r$ 比较零初值验证。

由 $du=-h z_\eta^{-2}d\eta$ 及 $Y_u$ 的两分量公式，
$$\rho=\frac h8J_2^*+\frac{h\omega-k}{4}J_1+
\frac{(h\omega-k)^2+1}{8h}J_0
+\frac u2\phi^2-\frac w{2h}\phi\phi'+r_2\phi'^2,\tag{2}$$
其中
$$r_2=\frac{hz}{4}-\frac{3k}{8}+\frac{k^2+1}{8hz}.$$

## 3. 沿渐近叶的平方只涉及 $\phi,\phi'$

按 $(T,N,B)$ 的分量次序，直接对公开无穷小弯曲公式求导得
$$DY_\phi=\phi U+\phi' V,$$
$$U=(0,u,c),\qquad
V=\left(\frac{z_s}{2z^2},-\frac h2,
-\frac{h_s}{2}+\frac{h z_s}{z}-\frac{k z_s}{2z^2}\right).\tag{3}$$
这里 $z_s=\omega_s=k_s/(2h)$。例如 $Y$ 的 $T$ 分量为 $-\phi'/(2z)$，其导数给 $V_T$；$N$ 分量来自标架的导数；$B$ 分量的 $\phi'$ 系数就是 $-D(w/(2h))$。

代入 (1)–(3) 得到六项形式
$$\boxed{\mathcal O_\phi=A_0\phi^2+A_1\phi\phi'+A_2\phi'^2
+B_0J_0+B_1J_1+B_2J_2^*.}\tag{4}$$
所有系数只依赖基面几何，不依赖 profile。下面证明它们都是低次 $\xi$ 多项式。

## 4. 三个局部多项式

完整周期积分后的系数为
$$\boxed{A_0(\xi)=\frac12\oint k(hz-k)\,ds,}\tag{5}$$
$$\boxed{A_1(\xi)=-\frac12\oint\frac{k}{h}\{1+(hz-k)^2\}\,ds,}\tag{6}$$
以及
$$\boxed{\begin{aligned}
A_2(\xi)=\oint\bigg[&\frac{khz^3}{4}
-\frac{5k^2+1+h_s^2/h^2}{8}z^2
+\frac{k(k^2+1)}{2h}z-\frac{(k^2+1)^2}{8h^2}\\
&+\frac{h_szz_s}{4h}-\frac{k h_sz_s}{4h^2}
+\frac{(k^2+1)h_s^2}{8h^4}\bigg]ds.
\end{aligned}}\tag{7}$$
因此 $\deg A_0\le1$、$\deg A_1\le2$、$\deg A_2\le3$。

**(5) 的完整化简。** 由 $|U|^2=u^2+c^2$，局部被积式满足
$$\frac{|U|^2}{2u^2}+\frac{Ku}{2}
=\frac{kw}{2u}+\frac12D(c/u).$$
最后项周期积分为零，且 $w/u=hz-k$。

**(6) 的完整化简。** 令 $d_1=w/(2h)$。由 $V_N=-h/2$、$V_B=-Dd_1$，
$$\frac{U\cdot V}{u^2}-Kd_1
=-\frac h{2u}-d_1\frac{wk-u}{u^2}-D(d_1c/u^2).$$
非导数两项等于 $-k\{1+(w/u)^2\}/(2h)$，即 (6)。

**(7) 的完整化简。** 写 $K=K_0-D^2(z/h)$，$K_0=kz^2-(k^2+1)z/h$。周期分部积分给
$$A_2=\oint\left\{\frac{|V|^2}{2u^2}+K_0r_2+(Dr_2)D(z/h)\right\}ds.$$
利用 $k_s=2hz_s$，
$$Dr_2=\frac{h_sz}{4}-\frac{hz_s}{2}+\frac{kz_s}{2z}
-\frac{(k^2+1)h_s}{8h^2z}-\frac{(k^2+1)z_s}{8hz^2}.$$
展开 $|V|^2/(2u^2)+(Dr_2)D(z/h)$ 后，所有含 $z^{-1}$、$z^{-2}$ 的项及纯 $z_s^2$ 项抵消，剩下
$$\frac{z^2}{8}-\frac{h_s^2z^2}{8h^2}
+\frac{h_szz_s}{4h}-\frac{k h_sz_s}{4h^2}
+\frac{(k^2+1)h_s^2}{8h^4}.$$
而
$$K_0r_2=\frac{khz^3}{4}-\frac{5k^2+2}{8}z^2
+\frac{k(k^2+1)}{2h}z-\frac{(k^2+1)^2}{8h^2}.$$
相加即得 (7)。这是直接代数证明；另用独立 SymPy 表达式作了差为严格零的辅助检查，没有把数值消差当成证明。

## 5. 三个截断矩系数

令 $d=h\omega-k$。由 (2)，
$$B_2=\frac18\oint Kh\,ds,\quad
B_1=\frac14\oint Kd\,ds,\quad
B_0=\frac18\oint K\frac{d^2+1}{h}\,ds.\tag{8}$$
$K$ 是 $\xi$ 的二次多项式，所以三个 $B_j$ 都是至多二次多项式。为降低数值微分阶数，可把 (8) 中的 $-D^2(z/h)$ 分部积分一次；例如
$$B_2=\frac18\oint\left\{khz^2-(k^2+1+h_s^2/h^2)z+\frac{h_sz_s}{h}\right\}ds,$$
$$B_1=\frac14\oint\left\{K_0d+(h_s\omega-hz_s)
\left(\frac{z_s}{h}-\frac{zh_s}{h^2}\right)\right\}ds,$$
$$B_0=\frac18\oint\left\{K_0\frac{d^2+1}{h}
+D\left(\frac{d^2+1}{h}\right)
\left(\frac{z_s}{h}-\frac{zh_s}{h^2}\right)\right\}ds.$$
这些版本只需 $h,k,\omega$ 及一阶导数。

系数并不独立。有以下可用于实现检查、减少设计变量的恒等式：
$$A_1'=-2A_0,\qquad B_2''=-A_1''/4,\qquad A_2'''=6B_2''.$$
若写 $A_1=a_{10}+a_{11}\xi+a_{12}\xi^2$，则 $B_0,B_1,B_2$ 的 $\xi^2$ 系数依次是 $-a_{10}/4,-a_{11}/4,-a_{12}/4$。等价地，
$$B_0''+\xi B_1''+\xi^2B_2''=-A_1(\xi)/2.$$
此外，$A_2$ 的 $\xi^2$ 系数等于 $B_2$ 的 $\xi$ 系数加 $A_0(0)$。每条关系直接由 (5)–(8) 比较幂次得到，不另加对称性假设。

## 6. 对实际求解的作用与尚未解决的条件

对两个 profile 作极化即可得到交叉通道；三个 $J$ 也相应改为 $\int\phi''\psi''$、$\int\xi\phi''\psi''$、$\int\xi^2\phi''\psi''+2\int\phi'\psi'$。因此一组有限几何积分就足以快速评估所有 $\xi$ 的完整二阶周期障碍。

三矩圆路径仍须满足两个**函数**条件：$\mathcal O_f=\mathcal O_g$ 和 $\mathcal O_{f,g}=0$。低次几何系数不把这两个条件自动变成三矩相等。一个新的可执行设计目标是调基面几何，令 (4) 的全部多项式系数为零；若能做到，所有三矩圆路径均通过二阶周期条件。但其可行性尚未证明。比如 $h$ 为常数且选 $\omega=k/(2h)$ 时，$A_0$ 的常数项为 $-\oint k^2/4$，不能随意假定可消。

即便两通道都严格为零，所得也仅是 $L_X Z=H$ 的二阶可解性；还需高阶相容性或非线性求解与固定度量加密，才能得到本课题要求的有限族。

## 来源

- Ghomi、Qiu、Raffaelli、Zhang，*Nonrigidity of smooth tight surfaces*，2026，公开预印本 <https://arxiv.org/html/2611.17269v1>，§2 的基面和无穷小弯曲公式。
- 本课题 `notes/literature-second-order-moments-20261114.md` 的三矩与完整线性 range 推导；本文独立核对其符号并进一步推导 (1)–(8)。
