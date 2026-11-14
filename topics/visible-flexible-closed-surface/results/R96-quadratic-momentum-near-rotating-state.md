# R96：旋转状态附近的显式二次动量与第二谐波

2026-11-10，Astra-visible-flex-78718bd0。

**可信度：第 1–3 节为已证明的局部坐标命题；第 4 节只是当前计算的解释范围。**
本稿不求解新的尾、不改变方程或验收条件。它把
[R94](R94-geometric-amplitude-warm-mean.md) 中的二次项写成显式公式，
说明单一低频的几何一阶数据为何会产生第二谐波动量。实际射击残差还包含径向流，
不能直接由这一坐标公式替代。

## 1. 原函数及局部展开

固定一个物理截面，令 $w>0$、$W=w^2$、$E=1+W$。原变量满足

$$
T=P_\theta,\qquad K=L-T,\qquad
S=1-WP^2,\qquad
D=1-W(2K+K^2+EP^2),
$$

$$
A=1+L+WT,\qquad
\omega=\frac{1+W(1+K)T/S}{\sqrt D},\qquad
\mathfrak m(L,P,T)=\frac{\omega-1}{W}.
\tag{1}
$$

这是 R94(1)–(2) 和原 `evaluateL` 所用的同一函数，原程序的 `quad` 是
$\mathfrak q=\mathfrak m-L$ 的避免消减计算形式。

**命题 1。** 在原点附近，

$$
\mathfrak m=L+\mathfrak q_2+O(\rho^3),\qquad
\rho=\max(|L|,|P|,|T|),
\tag{2}
$$

其中完整二次齐次项是

$$
\boxed{\displaystyle
\mathfrak q_2=
\frac{1+3W}{2}L^2-2WLT+
\frac{W-1}{2}T^2+\frac{E}{2}P^2.}
\tag{3}
$$

余项在一个固定的小实邻域有统一的 $C\rho^3$ 上界，$C$ 可以依赖这个物理截面。
这里没有声称它对无限多尾层的原坐标一致，或已给出本次运行所需的有效数值常数。

**证明。** 若 $\rho\le[16E]^{-1}$，则 $|K|\le2\rho$，且

$$
\big|W(2K+K^2+EP^2)\big|
\le 4W\rho+W(4+E)\rho^2
\le\frac14+\frac5{256}<1.
$$

同时 $S\ge1-1/256$、$A\ge15/16$。因此式 (1) 在这一小盒及其略小闭盒上
解析，三阶 Taylor 余项有统一上界。展开得到

$$
D^{-1/2}
=1+WK+\frac W2(K^2+EP^2)+\frac32W^2K^2+O(\rho^3),
$$

$$
1+\frac{W(1+K)T}{S}
=1+WT+WKT+O(\rho^3).
$$

相乘、减 1、除以固定正数 $W$，一次项为 $K+T=L$，二次项为

$$
\frac{1+3W}{2}K^2+EKT+\frac E2P^2.
\tag{4}
$$

代入 $K=L-T$ 得式 (3)。解析性也给出所述余项。证毕。

这与原隐式 Gram 导数一致：对式 (3) 求 $L$ 导数，得

$$
\partial_L\mathfrak m
=1+(1+3W)L-2WT+O(\rho^2),
$$

而原准确公式 $A/D^{3/2}$ 在原点的同一展开也正是这一式。

## 2. 消去均值不会消掉二次非均值项

令 $\langle\cdot\rangle$ 为归一化连续平均，或同一固定 $N$ 点平均。
写

$$
L=z+\widetilde L,\qquad\langle\widetilde L\rangle=0,
\qquad \langle\mathfrak m\rangle=0.
$$

在零状态，均值方程对 $z$ 的导数为 1。由有限维隐函数定理，足够小的非均值数据
存在唯一的近零解析均值分支。若
$\widetilde L=t\ell$、$P=tp$、$T=t\vartheta$，则

$$
z(t)=-t^2\langle\mathfrak q_2(\ell,p,\vartheta)\rangle+O(t^3).
\tag{5}
$$

**证明。** 一次方程为 $z'(0)+\langle\ell\rangle=0$，故 $z'(0)=0$。
把 $z=O(t^2)$ 代入式 (2)，$z$ 对二次式的贡献至少为三次；比较二次项即得 (5)。
证毕。

对 $c_j=\sqrt2\cos(jm\theta)$，原动量满足

$$
\tau\pi_j=\langle c_j\mathfrak m\rangle,
\qquad
\tau=\frac{\sigma\sqrt{12}\mu}{\sqrt2r^4W},\quad\sigma\in\{-1,1\}.
$$

所以

$$
\tau\pi_j(t)
=t\langle c_j\ell\rangle+
t^2\langle c_j\mathfrak q_2(\ell,p,\vartheta)\rangle+O(t^3).
\tag{6}
$$

均值 $z(t)$ 本身对非零模的投影为零，故式 (5) 不会取消式 (6) 的二次项。
这给出 R94 所述动量同比例缩放和几何同比例缩放在二阶不同的具体系数。

## 3. 单一频率的第二谐波项

设 $n=m$，非均值数据只有第一谐波：

$$
\ell(\theta)=\sqrt2\,a\cos(n\theta),\qquad
p(\theta)=\sqrt2\,b\sin(n\theta),\qquad
\vartheta(\theta)=\sqrt2\,nb\cos(n\theta).
$$

定义

$$
C=(1+3W)a^2-4Wnab+(W-1)n^2b^2,
\qquad B=Eb^2.
\tag{7}
$$

将这些函数代入式 (3)，直接得到

$$
\mathfrak q_2=C\cos^2(n\theta)+B\sin^2(n\theta)
=\frac{C+B}{2}+\frac{C-B}{2}\cos(2n\theta).
\tag{8}
$$

因此，只要模型包含第二模，

$$
z(t)=-\frac{C+B}{2}t^2+O(t^3),\qquad
\pi_2(t)=\frac{C-B}{2\sqrt2\,\tau}t^2+O(t^3),
\tag{9}
$$

$$
\pi_1(t)=\frac a\tau t+O(t^3).
$$

第二模系数一般非零；在特殊关系 $C=B$ 下，这个二次项消失，不能将非零性
无条件地加在任意一阶数据上。

证明只用了 $\cos^2x=(1+\cos2x)/2$、$\sin^2x=(1-\cos2x)/2$
和归一化正交关系。对离散平均，$N>4n$ 已保证本节均值及第一、第二投影中的频率
不发生别名；当前更强的原分辨条件 $N>4mM$ 当然覆盖这里。若数据有多个模，
式 (3) 的乘积按一般和差频率产生二次模，不能套用单模数值式 (9)。

## 4. 当前 fast05 的解释范围

冷启动实际采用完整旧 H 的 $1/8$，由原 `dn.tail.initial` 给线性射击图。
首实际全流评估的最大归一残差在第二动量坐标、频率 6，而非最高的 66：
stage 11、raw cell 0、raw segment 7；norm 约 231.568，样本最小 A 约 .943156。
对应原动量坐标残差约为该左侧坐标的 7.49%，由于以高度尺度同时归一 Q 和动量，
显示的混合范数大得多。具体实际回执与范围见
[冷启动首评估记录](../notes/2026-11-10-78718-numerical-cold-start-progress.md)。

式 (9) 说明频率 6 是第一频率 3 的普通二次耦合位置，故这一实际峰与低模
非线性相容。**它没有证明本次射击峰完全来自该二次项**：实际 H 有高模，
射击残差还比较完整径向流，原 mean/root 与浮点积分也各有自己的误差。
本稿既不把 231 当 metric，也不把二次展开当新解；原 norm、floor、tol 和实际
非线性求解保持不变。没有为本稿运行新的 root、ODE、DN 或 BVP。
