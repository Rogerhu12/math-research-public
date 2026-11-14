# R150 附录：内均值两点余类的三坐标非零奇点全部排除

日期：2026-11-13（UTC）。作者：normal_resume_2220 / Astra-ISP-1cf8c51d。

状态：**已证明的进一步排除。** 在非割线均值、第三矩本质维数三且均值位于该本质空间的原完整临界点中，除已分类的 $W_\pm$ 分支之外，剩余平面三次曲线的奇点不可能同时具有三个非零坐标。本稿仍保留奇点落在任一支持点极线坐标轴上的情形；不将本项排除表述为整个内均值余类已经排除。

## 1. 同一原剩余类

采用[内均值全等向归约](R150-appendix-inside-mean-critical-support-is-isotropic.md)、[双 jet 排除](R150-appendix-inside-mean-double-jet-residual-exclusion.md)及[两点极线限制](R150-appendix-inside-mean-reduced-support-and-simple-polars.md)。这些结果将尚未分类的原完整临界点准确限制为
$$
W=W^{\perp_K},\quad W\cap v(\mathbb P^1)=s+t,\quad s\ne t,
\quad W=\mathbb Cy\oplus\operatorname{span}\{v(s),v(t)\},
$$
其中交除子准确长二，$s,t$ 均为有限点且不属于 $\{0,2,-6\}$，并且 $k(s,t)=0$。真实累积量仍是
$$
H=h_s v(s)^2+h_t v(t)^2,\qquad
V=v_s v(s)^3+v_t v(t)^3,
\qquad (h_i,v_i)\ne(0,0)\quad(i=s,t).
\tag{1.1}
$$
除去准确共同因子 $G(z)=(z-s)(z-t)$ 后，令
$$
A(z)=\frac{k(s,z)}{G(z)},\quad B(z)=\frac{k(t,z)}{G(z)},
\quad P(z)=\frac{y^{\mathsf T}Kv(z)}{G(z)}.
$$
均按二元三次式齐次化。它们定义无基点的双有理三次参数化，像为不可约平面三次曲线
$$
\mathcal C(Y,X,Z)=Y^3-6Y(h_sX^2+h_tZ^2)+4(v_sX^3+v_tZ^3)=0.
\tag{1.2}
$$
上述极线限制已经证明 $A,B$ 互素，且各自无重根。平面曲线是有理三次曲线，故必有奇点；例如用平面三次曲线的算术亏格为一、无基点双有理参数域为 $\mathbb P^1$ 可得，或直接对其三次消去式应用判别式。

本稿假设其奇点 $[Y_0:X_0:Z_0]$ 满足 $Y_0X_0Z_0\ne0$，并导出矛盾。

## 2. 奇点归一化与两个参数化不变量

分别缩放三个坐标，使奇点变为 $[1:1:1]$。奇点的三个一阶方程准确给出
$$
a+b=\frac12,\qquad
\mathcal C=Y^3-6Y(aX^2+bZ^2)+4(aX^3+bZ^3).
\tag{2.1}
$$
这里 $a=h_sX_0^2/Y_0^2$、$b=h_tZ_0^2/Y_0^2$；奇点方程同时使相应三次系数等于 $a,b$。若 $a=0$，则原 $h_s=v_s=0$，违背 (1.1)；$b=0$ 同理。因此 $ab\ne0$。在仿射图 $Y=1$、$X=1+x,Z=1+z$ 上，方程变成
$$
6ax^2+6bz^2+4ax^3+4bz^3=0.
$$
其二次项非退化，故该奇点确为普通节点。

由通过节点的直线 $[x:z]=[r:u]$ 求第三个交点，得到如下无基点三次参数化（共同符号无关）：
$$
\begin{aligned}
Y&=-2(ar^3+bu^3),\\
X&=ar^3+3bru^2-2bu^3,\\
Z&=-2ar^3+3ar^2u+bu^3.
\end{aligned}
\tag{2.2}
$$
它的有理逆为 $[X-Y:Z-Y]$。无基点性也可直接检查：若 $Y=0$ 且 $X=Z=0$，则 $r,u\ne0$，随后 $r=u$，与 $a+b=1/2$ 冲突。因此 (2.2) 与原参数化只差一个 $\mathrm{PGL}_2$ 参数变换以及三个坐标各自的非零缩放。

对两个二元三次式 $A=\sum_{i=0}^3a_i r^iu^{3-i}$、$B=\sum_{i=0}^3b_i r^iu^{3-i}$，定义
$$
\mathfrak a(A,B)=3a_0b_3-a_1b_2+a_2b_1-3a_3b_0,
\qquad
\mathfrak d(A,B)=[\lambda^2\mu^2]\operatorname{disc}(\lambda A+\mu B).
\tag{2.3}
$$
这两个量的零性均不随共同参数变换及分别非零缩放而改变。第一式是三次张量用交替二形式作三次收缩；$M\in\mathrm{GL}_2$ 使它乘以 $\det(M)^3$。第二式由二元三次判别式的根差乘积公式，使其乘以 $\det(M)^6$。分别把 $A,B$ 缩放为 $cA,dB$ 时，二者分别乘以 $cd,c^2d^2$。这些是多项式身份，故也包括三次首系数为零的参数图。

将 (2.2) 的 $X,Z$ 代入，准确得到
$$
\boxed{\mathfrak a(X,Z)=0,\qquad \mathfrak d(X,Z)=0.}
\tag{2.4}
$$
这一身份事实上对任意 $a,b$ 成立。可直接用系数
$$
X=(-2b,3b,0,a),\qquad Z=(b,0,3a,-2a)
$$
展开核对。因此原物理极线 $A,B$ 也必须同时满足 (2.4)。

## 3. 原极线的不变量与两变量消去

原核为
$$
k(s,z)=-(s-z)^2q(s,z),
$$
$$
q(s,z)=s^3z+sz^3-3s^2z^2+s^3+z^3-3s^2z-3sz^2-5s^2-5z^2+22sz.
$$
置 $\sigma=s+t,\ \pi=st$。正交性 $q(s,t)=0$ 写成
$$
Q(\sigma,\pi)=\sigma^3+(\pi-5)\sigma^2-6\sigma\pi-5\pi^2+32\pi=0.
\tag{3.1}
$$
令 $\alpha=s+1,\ \beta=-3s^2-3s-5,\ \gamma=s^3-3s^2+22s$。由 $q(s,t)=0$，原 $A$ 的升幂系数准确为
$$
\begin{aligned}
a_0&=s(\gamma+\beta t+\alpha t^2),\\
a_1&=s(\beta+\alpha t)-(\gamma+\beta t+\alpha t^2),\\
a_2&=s\alpha-(\beta+\alpha t),\qquad a_3=-\alpha.
\end{aligned}
\tag{3.2}
$$
$B$ 的系数由交换 $s,t$ 得到。这些式是 $-(z-s)q(s,z)/(z-t)$ 的无余项除法，不是对极线的独立选择。

直接从 (3.2) 展开 (2.3)，有
$$
\mathfrak a(A,B)=(s-t)\bigl(J(\sigma,\pi)-11Q(\sigma,\pi)\bigr),
$$
$$
J(\sigma,\pi)=5\pi^2+10\sigma\pi-10\sigma^2+94\pi-78\sigma+160.
\tag{3.3}
$$
因此 $s\ne t$、(3.1)、(2.4) 共同迫 $J=0$。

记 $C(\sigma,\pi)=\mathfrak d(A,B)$。其精确多项式可按 (3.2) 及普通三次判别式
$$
\operatorname{disc}(ar^3+br^2u+cru^2+du^3)
=b^2c^2-4ac^3-4b^3d-27a^2d^2+18abcd
$$
逐项定义；[随稿精确验证器](../notes/2026-11-13-inside-mean-interior-node-exclusion-verify.py)同时给出其完整展开并核对以下消去身份。故 (2.4) 还要求 $C=0$。

现在令
$$
D(\sigma)=\sigma^2+4\sigma+126,\qquad
N(\sigma)=-\sigma^3+15\sigma^2+78\sigma-160.
$$
准确身份 $Q+J=D\pi-N$ 给出 $D\pi=N$。两个一元多项式满足
$$
\operatorname{Res}(D,N)=9894948\ne0.
\tag{3.4}
$$
所以在任何共同零点上 $D\ne0$，且 $\pi=N/D$。定义整数多项式
$$
J_0(\sigma)=D^2J(\sigma,N/D),\qquad
C_0(\sigma)=D^5C(\sigma,N/D).
\tag{3.5}
$$
前者准确为
$$
J_0=-15\sigma^6-292\sigma^5-1645\sigma^4+5144\sigma^3
 +95744\sigma^2-539776\sigma+773120.
\tag{3.6}
$$
后者的升幂系数为
$$
\begin{aligned}
(&-171358224271872000,331164158599944960,-267625642369121088,\\
&112294111432922880,-22960520222398752,787818839251584,\\
&427361676961632,-3291008231424,-14334240742560,-193719686544,\\
&303061145292,19364473776,-5071394574,-1105984752,\\
&-98959884,-4725600,-101250).
\end{aligned}
\tag{3.7}
$$

## 4. 完整次数保持的非零结果式证书

模素数 $103$，(3.6)、(3.7) 的最高系数均非零，次数仍准确为 $6,16$。它们的 Sylvester 行列式为
$$
\operatorname{Res}(J_0,C_0)\equiv39\pmod{103},
\tag{4.1}
$$
特别不为零。这里还有一个无需数值判断的短证书：令 $U,V$ 的升幂系数分别为
$$
\begin{aligned}
U:&\ (-46,7,37,-8,-26,15,-35,31,1,38,-36,15,32,47,2,-15),\\
V:&\ (-29,28,46,-38,-40,19).
\end{aligned}
$$
则
$$
U J_0+V C_0\equiv1\pmod{103}.
\tag{4.2}
$$
次数保持与 (4.1) 说明原整数 Sylvester 行列式非零；因此 $J_0,C_0$ 在 $\mathbb C$ 上没有公共根。结合 (3.4)、(3.5)，$Q,J,C$ 在 $\mathbb C^2$ 亦没有公共零点。这与原极线必须满足的 (2.4) 矛盾。

随稿验证器只使用 Python 标准库的整数、有理数及有限域运算：从 (3.2) 计算两个不变量，核对 (3.3)、(3.5) 的全部系数，用 Sylvester 消元计算 (3.4)、(4.1)，并逐系数核对 (4.2)。[完整精确回执](../notes/2026-11-13-inside-mean-interior-node-exclusion-verification.json)记录 PASS；这些有限身份正是上面消去证明的一部分。

## 5. 结论及保留范围

原剩余不可约三次曲线的奇点不能有 $Y_0X_0Z_0\ne0$。证明保留了原 $H,V$ 的最小两点支撑、原极化核、原参数化和全部降秩系数；没有用任意三次式替换物理极线。

本稿尚未排除 $Y_0X_0Z_0=0$ 的奇点，需要从同一原三次方程及无重互素极线继续处理。故没有在这里宣称内均值分支全部为 $W_\pm$，也没有将本项支撑排除升级为全局 Jacobian 自然幂归属或实际 Bell 算子的逆。
