# 固定 CM 多项式单位条件的稀疏坏集

日期：2026-11-14。状态：已证明。供 R605 及后续固定系数比较使用。

## 1. 固定多项式引理

令 $K=\mathbf Q(\omega)$、$\omega^2+\omega+1=0$。
对每个当前普通素数 $p$，保原规范
$\pi_0\bar\pi_0=p$ 和整数迹
$$
a_p=\pi_0+\bar\pi_0\in\mathbf Z,\qquad |a_p|\le2\sqrt p.
$$
普通地点始终取 $(\pi_0)$，不交换共轭。
设 $F(T)\in K[T]$ 是一个**固定的非零多项式**。

选择固定正整数 $D$，使 $G=DF\in\mathcal O_K[T]$。
排除有限集 $p\mid D$，并令
$$
H(T)=G(T)\bar G(T)\in\mathbf Z[T]\setminus\{0\}.
$$
这里共轭只作用于固定系数，形式变量 $T$ 不动。

**引理。** 当 $X\to\infty$ 时，
$$
\boxed{
\#\{p\le X:\ v_{\pi_0}(F(\bar\pi_0))>0\}
=O_F(\sqrt X\log X).
}
$$
如需把非整的固定系数也计入，额外坏集仅是固定分母素数。

**证明。** 在原地点
$\bar\pi_0\equiv a_p\bmod\pi_0$。因此上述整除条件蕴含
$$
\pi_0\mid G(a_p),\qquad p\mid H(a_p).
$$

先考虑 $H(a_p)\ne0$。
只有 $O(\sqrt X)$ 个整数 $a$ 满足 $|a|\le2\sqrt X$。
若 $d=\deg H$，固定系数给
$|H(a)|\le C_H(1+|a|)^d$。
每个非零整数 $H(a)$ 的不同素因子数至多
$\log_2\max(2,|H(a)|)=O_H(\log X)$。
逐 $a$ 求和，得到 $O_H(\sqrt X\log X)$。

必须另外处理 $H(a_p)=0$，不能把零整数当作只有有限素因子。
$H$ 非零，所以其整数根 $a_0$ 只有有限个。
写 $\pi_0=u+v\omega$，则
$$
a_0=2u-v,\qquad p=u^2-uv+v^2
=\frac{a_0^2+3v^2}{4}.
$$
当 $p\le X$ 时，只有 $O(\sqrt X)$ 个可能的整数 $v$；
每个 $v$ 决定至多一个 $p$。
故每个固定整数根分支也只有 $O(\sqrt X)$ 个坏素数。
合并两个部分和固定分母素数，即得结论。证毕。

这一证明使用原 CM 迹与范数，不把 $a_p$ 当作任意有限域参数，
也没有依赖素数采样。

## 2. 固定 lambda/kappa 有理式

保原
$$
\lambda=-\bar\pi_0^{-1},\qquad
\kappa=\pi_0/\bar\pi_0=p\lambda^2.
$$
在原普通地点，$\bar\pi_0,\lambda$ 为单位，$\kappa\in p\mathcal O$。

设
$$
R(L,U)=A(L,U)/B(L,U)\in K(L,U)
$$
是固定有理式，选择固定多项式代表 $A,B$，
且 $A(L,0),B(L,0)$ 都不恒等于零。
先清固定系数分母。令
$$
F_A(T)=T^{m_A}A(-1/T,0),\qquad
F_B(T)=T^{m_B}B(-1/T,0),
$$
其中 $m_A,m_B$ 取足够大的固定整数，使二者为非零多项式。

由第一节，对除 $O(\sqrt X\log X)$ 个素数以外的当前普通处，
$A(\lambda,0),B(\lambda,0)$ 都是单位。
又有
$$
A(\lambda,\kappa)\equiv A(\lambda,0)\pmod p,\qquad
B(\lambda,\kappa)\equiv B(\lambda,0)\pmod p.
$$
所以完整实际分母为单位，且
$$
\boxed{R(\lambda,\kappa)\in\mathcal O^\times.}
$$
这支付了实际有理式，而不是只说其模 $p$ 分子非零。

若先有固定可见的 $\kappa$ 次数
$A(L,U)=U^rA_0(L,U)$、
$B(L,U)=U^sB_0(L,U)$，
且 $A_0(L,0),B_0(L,0)$ 非零，则同一论证给
$$
v_p(R(\lambda,\kappa))=r-s
$$
在上述稀疏坏集之外成立。
固定 CM 单位或原 $\Omega$ 的固定幂可保留为外部单位。

该结论适用于**固定有限组**这种有理式：
取所有固定多项式的坏集之并，仍是
$O(\sqrt X\log X)$。
若系数或次数随 $p$、未固定的深度 $n$ 或无界指标改变，
不能使用这里的统一计数。

## 3. 与原固定 ray 的无穷交

沿本题已经支付的 ray-class/Chebotarev 结论，
任意此前合法固定细分的原 ray，在 $p\le X$ 中仍有
$$
c\,\operatorname{Li}(X)+o(X/\log X),\qquad c>0,
$$
个相应普通素数；此前固定坏集只删有限个。
而
$$
\sqrt X\log X=o(X/\log X).
$$
故再删除上述固定有限组多项式的坏集，仍留下无穷素数，
并保持原 ray 内的相对密度一。

这是“原固定 ray 减去一个显示计数的稀疏集合”的结论，
**不是**宣称该单位条件在原 ray 的每一个素数上成立。
若后续采用本引理，应在其量词中明确保留这项删除，
无需为了全 ray 断言而另造一个未证明的 CRT 细分。

## 4. 不适用的原目标

原 $I_1,I_4$、随 $p$ 变化的 Cartier/forcing 多项式、
$\mathcal R_i=D^{p-c_i}q_i$、高阶 prime-diagonal 系数，
没有在这里被识别为固定 $F(\bar\pi_0)$。
因此本引理不能据此证明这些指定值非零。

它只给已经展开成**固定** $\lambda,\kappa$ 有理式的实际系数
提供无穷多个单位地点；原中央、全部混合切集和补偿仍须逐项支付。
