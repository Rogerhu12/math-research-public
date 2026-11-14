# R57. 实际 theta 截面的全局 Hurwitz 整数与固定多项式流

日期：2026-11-12。**状态：全局整性与固定递推已证明；无穷非零仍开。**

## 1. 定理

令 $A_{17}(z)=\sum b_mz^m$ 为R51已经准确识别的实际截面。
则对所有 $m\ge0$，
$$
\boxed{h_m=m!b_m\in\mathbb Z.}
\tag{1}
$$
没有需要删去的 $2,5,17$ 分母。更准确地，有一个固定整数序列
$a_k\in\mathbb Z$、$a_1=24$，使统一解析族满足
$$
A_D(z)=\sum_{k\ge1}D^{k-1}a_k\frac{z^{4k}}{(4k)!}.
\tag{2}
$$
这个序列由有限个固定整多项式微分系统生成。
只有 $D=17$ 被R51认定为本课题的原始中央theta因子，
不把其他D自动认作秩二曲线。

## 2. 无分母系统的完整证明

在 $E_D:y^2=x^3-Dx$ 的加法坐标 $dz=dx/(2y)$ 中，令
$$
u=x^{-1/2},\quad v=u',\quad
\vartheta_D=\sigma_D/u,\quad L=(\log\vartheta_D)',
$$
取 $u=z+O(z^5)$、$\vartheta_D(0)=1$。
Weierstrass方程给 $v^2=1-Du^4$、$u''=-2Du^3$。
又因 $\zeta_D'=-x$，
$$
L'=-x-u''/u+(u'/u)^2=Du^2.
$$
故
$$
\boxed{
u'=v,\quad v'=-2Du^3,\quad L'=Du^2,\quad
\vartheta_D'=L\vartheta_D;qquad
(u,v,L,\vartheta_D)(0)=(0,1,0,1).
}
\tag{3}
$$

对特征零整环R，Hurwitz级数环
$\mathcal H_R=\{\sum a_nz^n/n!:a_n\in R\}$
的乘法为整数二项式卷积，求导为系数移位。
(3)的每个下一阶导数仅由此前导数经整数加乘得到，
故归纳给
$$
u,v,L,\vartheta_D,\sigma_D=u\vartheta_D\in\mathcal H_{\mathbb Z[D]}.
\tag{4}
$$
这证明的是阶乘规范的整性，不是普通Taylor系数全整。

设 $\beta=2+i$。由(3)的唯一性，
$$
\vartheta_D(az)=\vartheta_{Da^4}(z),\qquad
\sigma_D(az)/a=\sigma_{Da^4}(z).
$$
R51的真实乘积中，$\beta\bar\beta=5$，所以
$$
\begin{aligned}
A_D
&=\frac15\vartheta_D(z)\vartheta_D(2z)\sigma_D(z)^2
                    \sigma_D(\beta z)\sigma_D(\bar\beta z)\\
&=\vartheta_D\vartheta_{16D}\sigma_D^2
                    \sigma_{(-7+24i)D}\sigma_{(-7-24i)D}.
\end{aligned}
\tag{5}
$$
因此 $A_D\in\mathcal H_{\mathbb Z[i,D]}$。
共轭交换最后两个因子，全部系数均固定，故实际上在
$\mathcal H_{\mathbb Z[D]}$ 中，证明(1)。

由 $\vartheta_D(iz)=\vartheta_D(z)$、$\sigma_D(iz)=i\sigma_D(z)$，
只有4的倍数次幂出现。最低项是z4，而
$A_D(z)=a^{-4}A_1(az)$、$a^4=D$；
比较各阶并用整系数性便给(2)。证毕。

## 3. 固定整导子及完全整数的复算

单份系统的导子是
$$
\mathscr V=v\partial_u-2Du^3\partial_v+Du^2\partial_L+
L\theta\partial_\theta.
$$
取参数 $D,16D,(-7+24i)D,(-7-24i)D$ 的四份系统，
以导子和 $\mathscr V_{\rm tot}$ 作用于
$$
P=u_1^2u_3u_4\theta_1^3\theta_2\theta_3\theta_4.
$$
则
$$
h_m(D)=\mathscr V_{\rm tot}^mP
       \bigm|_{u_j=L_j=0, v_j=\theta_j=1}.
\tag{6}
$$
这提供一个固定维数的非线性多项式系统；
迭代导子会提高次数，不能据此称为固定阶线性递推。

[完整笔记](../notes/2026-11-12-global-hurwitz-integers-and-polynomial-flow.md)
给仅算D1再作高斯整数二项式卷积的递推。
[整数脚本](../scripts/check-theta-hurwitz-integers.py)已全文根审并运行，
到次数32的缩放检查全部通过；前四个实际值为
$$
h_4=24,\quad h_8=1108128,\quad
h_{12}=88516482912,\quad h_{16}=39051754432862976,
$$
与R51两份全局证书一致。证明不依赖这些有限检查。

## 4. 中心有限证书现在完全落在整数序列上

对 $m\ge1$，$(m-1)!b_m=h_m/m$ 的约分后分母整除m。
R56的普通 $m_n=(p-1)p^n$ 因而给准确等价
$$
\boxed{
\Sha(E_{17}/\mathbb Q)[p^\infty]\text{有限}
\iff\exists n\ge0:
     v_p(h_{(p-1)p^n})<2n+2.
}
\tag{7}
$$
这里目标普通p仍为 $p\ge13,p\ne17$。
实际 $J_p(0)=0$ 已给 $p^{n+1}\mid h_{m_n}$；
若 $J_p'(0)=0$，则对每层都有 $p^{2n+2}\mid h_{m_n}$。
(7)也可直接由真实矩公式的中心零阶导出，与R56的无周期误差完全一致。

本结果补上全局整数模型，没有把整性换成赋值上界。
仅在一个整数上同步 $p-1\mid m$ 的整除条件仍受R15的除数计数预算限制。
需要这个固定多项式流或固定截面的额外算术，才能证明(7)对无穷多个p有证书。
