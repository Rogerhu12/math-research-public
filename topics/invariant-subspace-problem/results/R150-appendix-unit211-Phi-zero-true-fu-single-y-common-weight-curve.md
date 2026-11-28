# R150 补充：正确 Phi 的 f=u 单坐标原恢复与同一六次权曲线

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。作者：GPT-6 Astra Pro（AI-assisted）。

## 1. 新原结论

保持当前正确原 unit211 的
$$
\Phi=0,\qquad f=u,\qquad Q(1-Q)P_fP_{02}bcD\ne0.
$$
[正确整 t=0](R150-appendix-unit211-Phi-zero-true-entire-tzero-original-exclusion.md)和[本 f=u 支的整个 u=3/2](R150-appendix-unit211-Phi-zero-fu-entire-u-three-half-original-exclusion.md)已经排除。

本条将全部原点恢复为一个自由变量 y，并从同一原 Gram 的五个真实条件得到必要权方程
$$
\boxed{\Psi(u,Q)=0,}
\tag{1}
$$
其中
$$
\begin{aligned}
\Psi={}&Q^3+(-10u^2+24u-15)Q^2\\
&+(32u^4-152u^3+276u^2-228u+72)Q\\
&-32u^6+224u^5-672u^4+1104u^3\\
&-1040u^2+528u-112.
\end{aligned}
\tag{2}
$$
这是双次数 $(6,3)$、总次数 6、16 项的完整 QQ 多项式。三个新原 cofactor 只是 (2) 的非零常数倍；本次没有得到两个独立权曲线，不证明权点总数有限或整个 f=u 排空。

## 2. 全原点的单变量恢复

令
$$
s=u-1,\quad h=2u-3,\quad \delta=1-Q,\quad
L=Q-2s(u-2)=\ell Q,\quad K=Q+4s,
$$
$$
A=4s^2-Q,\qquad \theta=u-L,\qquad
M_n=2uL-L^2-u^2Q=4bcQ\delta.
$$
实际只使用
$$
Q\delta sKLM_nh\ne0.
\tag{3}
$$
其中 h 的支付仅来自本 f=u 支的整纤维排除；不把它外推到整个 Phi。没有倒 $u,A,B,u-\ell,u+Q-1$ 或任何旧头。

取
$$
y=A+2L\lambda.
$$
完整恢复为
$$
\lambda=\frac{y-A}{2L},\quad
A_1=\frac{2sy}{Q},\quad
T=-\frac LQ-\frac{Ky}{2QL},
$$
$$
t=\frac{2\delta(2\theta y+LA)}{M_nh},\quad
V=u-\frac{sy}{Q}+bc\,t,\quad
W=\frac{4u^2-K}{2}.
\tag{4}
$$
在自由 t 下先写 $v_n=uQ-sy+bcQt,\ z=Qt$。正确原 germ 组合给完整恒等式
$$
R=\frac{sz}{\delta}
 \left(-bc\,h\,z+\theta y+\frac{LA}{2}\right).
\tag{5}
$$
当前原点 $t\ne0$，所以 (5) 与 (4) 的 t 恢复等价。源先在自由 t 下完整返回 (5)，再代入 (4)，没有通过一个未付首项删去权纤维。

原 $P_1$ 在 Phi 上是
$$
P_f u+QP_{02}(\ell+T)
-\bigl[\lambda P_{02}+(u-1)T_0\bigr]T_0=0,
$$
其中 $T_0=-K,\ P_{02}=2sL,\ P_f=4s^2K$。它和原 $E_0/N_0$ 给 (4) 的其余恢复；本次均以完整原式乘回。

## 3. 同一完整 Gram 与五行

令 $m=u-\ell,\ M=M_n/Q$，
$$
x_0=\frac{\theta V-mW}{M},\qquad
y_0=\frac{\ell W-uV}{M},\quad
X=x_0+\rho y_0,\quad Y=x_0-\rho y_0,\quad \rho^2=\delta,
$$
$$
b=\ell/2+\rho m/(2\delta),\quad c=\bar b,\quad
p=1+\rho,\ q=1-\rho,\ a=1-\ell,
$$
$$
r=X-ap-ct,\qquad s_1=Y-aq-bt.
$$
完整四行是
$$
(0,0,p,q),\quad(0,A_1,r,s_1),\quad
(p,r,0,t),\quad(q,s_1,t,0).
\tag{6}
$$
使用真实 dual 乘法以及原迹
$$
(vw)_1=v_0w_1+v_1w_0,\qquad
\tau(v)=av_0+v_1+bv_B+cv_C,
$$
由 (6) 直接构造
$$
E_{\rm e},\quad E_{\rm o},\quad N_1,\quad NS,\quad PS.
\tag{7}
$$
本次完整返回 $E_0,N_0,P_1$、$E_1=bE_B+cE_C$、共轭与完整 weighted 值；没有采用旧错误 $R_{\rm bad}$，也没有只返回某个 D 倍数。

清掉实际 (3) 分母，并且只剥五行全部系数中的已付内容后，记多项式行为
$$
E,\ O,\ N,\ S,\ P.
$$
实际 y 次数是
$$
2,\ 2,\ 2,\ 3,\ 3.
\tag{8}
$$
每行的单位尺度都逐式返回。两种 $\rho$ 嵌入与所有参数首项退化均保留。

## 4. 三个完整原 cofactor

本次固定三个矩阵：
$$
(E,O,N)\quad\text{在 }(1,y,y^2)\text{ 上};
$$
$$
(E,yE,O,S),\qquad(E,yE,O,P)
\quad\text{在 }(1,y,y^2,y^3)\text{ 上}.
\tag{9}
$$
分别取三阶、四阶、四阶 adjugate 第一行，返回
$$
\sum_i\Omega_i(E,O,N,S,P)_i=D(u,Q).
\tag{10}
$$
重复 E 的两个乘子先在同一个原坐标合并。只将全部五个真实乘子的共同内容同步从乘子和 D 中精确除去，并把 (10) 全式乘回。因此共同内容的零集不会被丢掉；这不是约去原方程中的未付因子。

最终只剥 (3) 的已付权因子，并重新返回相对于 (7) 未约原式的完整五项组合。实际三个目标为
$$
\boxed{\frac{\Psi}{4},\qquad
       \frac{9\Psi}{64},\qquad
       \frac{\Psi}{64}.}
\tag{11}
$$
它们的三个 pair gcd 也都正是同一个六次曲线的常数倍，故 (1) 是本次唯一新的权支持，而不是三个独立的截断条件。

由第一个完整原组合，$\Psi$ 本身落在 (4) 恢复后的原五式理想中；特别 (1) 是真正特征零原必要式。没有使用模空性、未付头逆或物理 D 的范数逆。

## 5. 确定的有限层级与保留范围

(2) 对 Q 首一。因此未作几何局部化的必要权环
$$
\mathbb Q[u,Q]/(\Psi)
$$
以 $1,Q,Q^2$ 为 $\mathbb Q[u]$ 上的自由基。相应地，每个固定复 u 至多有三个 Q 值满足本必要权方程。

这不意味着 u 已有限，也不意味着整个原商已是该自由模：原参数开集与其余原条件仍须保留。更不假设在每个固定权上至少有一条 y 多项式非零；当前所有整 y 纤维、所有头零点和 $\Psi=0$ 的整个曲线均保持开放。

## 6. 唯一实际运行

[冻结源](../notes/2026-11-28-unit211-Phi-zero-true-fu-single-y-original-scalar-cofactors-8542.py)为 9662 B，SHA256
`9d591ab41ed41cc7dbee8ac3e9ce326ef68348455751ae9ad1cea954a7d463cb`。

唯一运行 46116345726 / job 140890945856 实际正常退出 0；耗时 0.207064155 秒，峰值 40804 KiB，限额 120 秒、1 GiB。源提交及执行前实际 pull 后主线都是
`ba9c766f01c2b90166a7f5c0b86c058e490f4a89`；读取时刻 2026-11-28 06:23:15.886579 UTC，两 README blob 无变化。

实际完成 16 项原检查、58 次完整精除乘回。三阶原目标的未缩放 $\Psi/4$ 有 16 项，其哈希为
`73bbd9835fce4caa3b26b90c7dd4e413a888e4967f5ea675bb8a16594f682223`。stdout 5423 B，SHA256
`0524af740c0bb9a062b780f6ab6fddfc7772cf9b39e916e7b42594baf13dd19a`。

[小回执](../notes/2026-11-28-unit211-Phi-zero-true-fu-single-y-original-scalar-cofactors-8542-execution.json)保留全部真实次数和比例。没有重放已冻 GB、旧头或已成 cofactor；本条不声称整个 Phi 或 ordinary ISP 完成。
