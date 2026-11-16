# 原 cubic 原函数格的零 charge 与真实四列负水平不变量

日期：2026-11-16。**状态：下列原次数四的准确计算、全原函数格的负水平消失及剩余来源商上的四个真实读取已证明。未赋这些读取满射，未将它们与三尾视为独立变量。**

沿用[原 charge 四十 cubic 原函数格](2026-11-16-r872-native-cubic-euler-primitive-and-tail-nullspace.md)
及[全局三倍水平消失](2026-11-16-r872-primitive-value-image-and-cubic-horizontal-vanishing.md)的假设。
记
$$
L=E+40,\quad \mathscr J_3=L^{-1}(\mathscr V_3),\quad
z_-=C\cdot H_-\ge0,\quad H_-=(Y=0)^{\rm strict}.
$$
源仍是原 $\mathcal W_D$，$p>D+40$，且
$\deg_YF(0,Y)=3$。特别每个 $LW=F^3A$ 的真实全局商满足
$$
A\in H^0(X,\mathcal O_X(B_D-3C)),\qquad A\in t^2k[[t]][Y].
\tag{1}
$$

## 1. 原 $B_D$ 在负水平上的次数准确为四

写
$$
c_n=\lfloor n/2\rfloor,\qquad c=c_D.
$$
原 $n$ 列的角因子和帽是
$$
q_n(t)=(t h_7)^{\lfloor(n+1)/4\rfloor}
       (t-1)^{\lfloor(n+1)/3\rfloor}d^{-c_n},
$$
$$
\deg_t(q_n P_n)\le\lfloor9n/2\rfloor+4 .
$$
清同一个真实分母 $d^c$ 后，第 $n$ 个系数的次数帽变成
$\lfloor9n/2\rfloor+4+c$。
因此原曲面类中
$$
u_D=\bigl(\lfloor9D/2\rfloor+4+c\bigr)-4D=2c+4 .
\tag{2}
$$

有限正角 $d=0$ 的第一重数是
$$
\min_{0\le n\le D}\{n+c-c_n\}=c .
$$
底无穷远用原 $T=1/t,\ Z=t^4Y$：
清分母后的第 $n$ 项之最小 $T$ 阶为
$u_D+4n-\lfloor9n/2\rfloor-4-c=c-c_n$，
故其第一正角重数同样为 $c$。
两次最小值都由原 $n=0$ 列达到，并非仅上界。

以 R815/R833 的真实负水平类
$H_-=S_0-E_{d,1}^*-E_{\infty,1}^*$ 读取，得到
$$
\boxed{B_D\cdot H_-=u_D-c-c=4.}
\tag{3}
$$
在该同一框内，原零 charge 来源恰为
$$
\boxed{[Y^0]\mathcal W_D=k[t]_{\le4}.}
\tag{4}
$$
清分母框只在前面带固定 $d^c$，不增加可选系数。
所以 (3) 与 (4) 是同一原负水平线束的完整读取。

## 2. 若 $z_-\ge1$，整个原函数格的零 charge 恒为零

令 $R_0$ 是严格负水平上 $t=0$ 的点。
原 $t=0$ 四步链位于 $Y=\infty$，故 $(t,Y)=(0,0)$ 没有被这十九次吹起。
因此 (1) 在 $R_0$ 的原框确实给
$$
A|_{H_-}\in
H^0\!\left(H_-,\mathcal O_{H_-}(B_D-3C)(-2R_0)\right).
$$
这一线束的次数准确是
$$
4-3z_--2=2-3z_- .
\tag{5}
$$
即使 $R_0\in C\cap H_-$，这个额外二阶仍来自真实商 $A$，
不能只取它与 $3(C\cap H_-)$ 的最大值而漏掉相加的阶。

若 $z_-\ge1$，(5) 为负，故 $A|_{H_-}=0$。
原 $E$ 线性化在 $H_-$ 的权为零，因此 (1) 的原限制恒等式为
$$
40\,W|_{H_-}=(F|_{H_-})^3(A|_{H_-}).
$$
$40$ 为单位，得到完整结论
$$
\boxed{
z_-\ge1\quad\Longrightarrow\quad
W|_{H_-}=0\ \text{对全部 }W\in\mathscr J_3.
}
\tag{6}
$$
等价地，原有理多项式的零 charge 系数恒等为零：
$$
\boxed{[Y^0]W(t,Y)=0.}
\tag{7}
$$
它不是仅在有限交点处消失，也不需要先假设 $W\in K_1$。

若 $z_-=0$，同一论证只给
$$
\dim\operatorname{res}_{H_-}\mathscr J_3\le3;
$$
在原 (4) 中其像包含于 $t^2k[t]_{\le4}$。
这里没有证明等号或任意三个系数可以赋值。

## 3. 剩余首核商上的四个实际读取

仍假设 $z_-\ge1$。由 (7)，零 charge 限制下降为
$$
\mathcal W_D/\mathscr J_3\longrightarrow k[t]_{\le4}.
$$
对于真正 $K_1$，原 $t^0$ 帽只有 charge $40,41,42$；
三个长块的常数行给单位 Vandermonde，
故原 $t^0$ 多项式整体为零。
特别零 charge 多项式的常数项为零。

因此有准确的同源读取
$$
\boxed{
\rho_-:
K_1/(\mathscr J_3\cap K_1)\longrightarrow
t\,k[t]_{\le4},\qquad
[W]\longmapsto[Y^0]W .
}
\tag{8}
$$
目标最多四维，其坐标就是同一个原 $W$ 的 $t,t^2,t^3,t^4$ 系数。
没有把 (8) 认成满射，也没有证明它与原
$\Pi=(W_{2,s-3},W_{2,s-2},W_{2,s-1})$ 可以分别指定。

式 (8) 是在完整剩余来源商中可保留的真实边界数据。
负水平上读取更高法向 jet 的行仍须用同一 $W$；
(6) 不能直接删掉那些法向或 conductor 项。
前注的 $3D_-$ 消失仍按完整 Cartier 理想使用。

本注没有扩大 $\mathcal W_D$、原 $M$ 或中央池；
同一个 $P,R,S$ 的其它 normal/carry 及指定 forcing 均保留。
这是原 Gauss 类和原源值的符号推导，无新增数值运行。
