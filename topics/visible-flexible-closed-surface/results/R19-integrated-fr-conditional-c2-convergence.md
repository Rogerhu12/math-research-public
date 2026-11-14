# R19：积分 quartic-Fr 表示的条件式 C² 收敛

状态：**已证明，独立全文审查 PASS。** 只证明数值表示本身的性质；不证明本题非线性源解、Fourier 极限或无限尾存在。

作者：`/root/tail_theory`，2026-11-09。

## 1. 单个径向系数的表示

设 $F\in C^2([a,a+L])$，$L>0$，并写 $Y=F'$、$f=F''$、$t=(r-a)/L$。取

$$
u_0=Y(a),\quad u_1=Y(a+L),\quad u_m=Y(a+L/2),\quad
f_0=f(a),\quad f_1=f(a+L).
$$

使用三次 Hermite 基函数

$$
H_{00}=2t^3-3t^2+1,\quad H_{01}=-2t^3+3t^2,
$$
$$
H_{10}=t^3-2t^2+t,\quad H_{11}=t^3-t^2,
\qquad b=t^2(1-t)^2.
$$

令

$$
B=16u_m-8(u_0+u_1)-2L(f_0-f_1),
$$
$$
P(t)=H_{00}u_0+H_{01}u_1+L(H_{10}f_0+H_{11}f_1)+Bb.
$$

则 $P$ 在两端匹配 $Y$ 与其物理 $r$ 导数，并满足 $P(1/2)=u_m$。相应五次位置函数定义为

$$
\widetilde F(r)=\widetilde F(a)+L\int_0^t P(s)\,ds.
$$

这就是当前完整尾导出器保存的积分 Fr 定义。跨的右端位置由积分给出，随后作为下一跨的左端位置；不把独立舍入的点坐标当作下一跨的定义。

## 2. 精确数据的误差界

记本跨的模连续度

$$
\omega=\sup_{x,y\in[a,a+L]}|f(x)-f(y)|.
$$

若上述五个导数数据精确，则

$$
\|\widetilde F'-F'\|_\infty\le3L\omega,
\qquad
\|\widetilde F''-F''\|_\infty\le\frac{11}{2}\omega.
\tag{1}
$$

**证明。** 插值精确再现关于 $r$ 的仿射 $Y$，故可减去 $Y(a)+Ltf_0$。写

$$
h(t)=Y(a+Lt)-Y(a)-Ltf_0
=L\int_0^t(f(a+Ls)-f_0)\,ds.
$$

于是 $|h(t)|\le Lt\omega$，$|h(1)|\le L\omega$，且
$d=L(f_1-f_0)$ 满足 $|d|\le L\omega$。减去仿射函数后的插值为

$$
Q(t)=H_{01}h(1)+H_{11}d+Bb,
\qquad B=16h(1/2)-8h(1)+2d.
$$

由

$$
16h(1/2)-8h(1)
=8L\left(\int_0^{1/2}(f(a+Ls)-f_0)\,ds
-\int_{1/2}^1(f(a+Ls)-f_0)\,ds\right)
$$

可得 $|B|\le10L\omega$。在 $0\le t\le1$ 上，

$$
|H_{01}|\le1,\quad |H_{11}|\le4/27,\quad b\le1/16,
$$
$$
|H'_{01}|\le3/2,\quad |H'_{11}|\le1,\quad
|b'|\le\sqrt3/9<1/5.
$$

因此

$$
|Q-h|\le(2+4/27+5/8)L\omega<3L\omega,
$$

以及

$$
|Q'/L-(f(a+Lt)-f_0)|
\le(3/2+1+2+1)\omega=11\omega/2.
$$

这给出 (1)。证毕。证明只用 $f$ 的连续性，不要求临界点上存在第三阶导数。

## 3. 导数数据误差与机器精度下限

现在三个 $u$ 数据各有绝对误差不超过 $\varepsilon_1$，两个 $f$ 数据各有绝对误差不超过 $\varepsilon_2$；$L$ 是比较所用的真实精确跨长。插值算子的线性性给出附加误差

$$
\|\delta\widetilde F'\|_\infty
\le3\varepsilon_1+\frac L2\varepsilon_2,
\tag{2}
$$
$$
\|\delta\widetilde F''\|_\infty
\le\frac{47}{5L}\varepsilon_1+\frac{14}{5}\varepsilon_2.
\tag{3}
$$

**证明。** 系数 $B$ 的误差至多 $32\varepsilon_1+4L\varepsilon_2$。又有

$$
H_{00},H_{01}\ge0,\quad H_{00}+H_{01}=1,
\quad |H_{10}|+|H_{11}|=t(1-t)\le1/4,
$$

结合 $b\le1/16$ 得 (2)。同时

$$
|H'_{00}|+|H'_{01}|=12t(1-t)\le3,
\qquad |H'_{10}|+|H'_{11}|\le2.
$$

结合 $|b'|<1/5$，物理导数须除以 $L$，所得系数为
$3+32/5=47/5$ 和 $2+4/5=14/5$，即 (3)。证毕。

此处没有把源 RK/shooting 误差等同于舍入误差。若尚未取得真实的 $\varepsilon_1,\varepsilon_2$，(2)–(3) 只是条件式传递。它也说明，固定精度下无限缩短跨并不能自动改善二阶误差：$\varepsilon_1/L$ 会被放大。

## 4. 整个区间与固定有限 Fourier 表示

在紧区间 $I$ 上取任意有限分割，每个节点的 Fr/Frr 数据在相邻跨共享，位置由上述积分递推。于是 $\widetilde F\in C^2(I)$ 恰好成立。对精确数据，设最大跨长为 $h$，并令

$$
\omega_F(h)=\sup_{x,y\in I,\ |x-y|\le h}|F''(x)-F''(y)|.
$$

由连续性 $\omega_F(h)\to0$。若内端值精确，(1) 给出

$$
\|\widetilde F-F\|_\infty\le3|I|h\omega_F(h),\quad
\|\widetilde F'-F'\|_\infty\le3h\omega_F(h),\quad
\|\widetilde F''-F''\|_\infty\le11\omega_F(h)/2.
$$

有数据误差时逐跨加入 (2)–(3)，位置误差再沿全区间积分；内端值误差直接加到位置界。特别地，若最大跨长趋零，最大 $\varepsilon_{2,i}$ 趋零且最大 $\varepsilon_{1,i}/L_i$ 趋零，内端误差也趋零，则该表示在 $C^2$ 中收敛到给定的 $F$。

固定有限 Fourier 集合时，对每个实系数或复系数分量应用以上结论即可。角导数仅乘有限的 $m$、$m^2$；例如把各系数的三类径向误差之和乘 $(1+|m|)^2$ 后求和，就控制位置及全部一、二阶混合导数。因此它对当前有限 XYZ Fourier 表示给出条件式完整 $C^2$ 收敛。

## 5. 本题的适用边界

本引理说明：对于已存在的固定 $C^2$ 源图，积分 Fr 五次表示没有一个必须靠改变物理度量、层尺度或形状参数才能压低的固有误差。临界加密只改变分割。

它并未证明该源图满足精确等距方程，也未证明 Galerkin/Fourier 极限或真实无限非线性尾存在。当前 exact-sum 半径与数值源半径之间的差也须另付；(1)–(3) 的源数据都须在相同物理半径上解释。实际 stage Fr 端迹校正属于新有限图定义，其大小仍须记录并随真实源求解加密检查。

## 独立审查记录

未参与本引理推导或积分尾表示实现的 coupled_prefix 已全文核对所有基函数、四个误差常数、跨间 C² 拼接及数据误差的 1/L 放大条件，结论 PASS。审稿为 `notes/2026-11-09-db6f-prefix-review-integrated-fr-convergence.md`，绑定原稿 SHA256 `cdd5c371ba8e7a2356b2209506904b82c26d76882bc701e8e82ac543e017f8e3`；正式版本只更新标题、状态和本段，证明未改。审查者参与过本题前缀求解，所以这项组件独审不冒充最终完整构造的未参与者复跑。
