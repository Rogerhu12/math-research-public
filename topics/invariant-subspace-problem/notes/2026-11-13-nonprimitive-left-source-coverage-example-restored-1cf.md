# 工作笔记：完整 primitive 坐标没有自动控制全部左质量

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / boundary_rebuild。

状态：**已证明的范围检查。** 本稿重建环境丢失前尚未发布的非primitive覆盖例，保原实际头和原连续尾；它不是真实 $W$ 来源，也不是三 Gram 比较的反例。

固定原模型之一、$m\ge5$、$d=2^m$ 及任意合法 $q\ge4d$。记
$$
A=A_m,\quad D=D_m,\quad \nu_m=\|D_m\|\le m^{-1}.
$$
原第一条上对角线的前两项及第二列写成
$$
Ae_1=e_0,\qquad Ae_2=\beta e_0+\eta_0e_1,
\qquad \eta_0>0.
$$
这里 $\beta,\eta_0$ 都是与 $m\ge2$ 无关的原固定头系数。令
$$
c_1=\frac{e_2-\beta e_1}{\eta_0},\qquad Ac_1=e_1.
$$
没有省略这个可能很大的固定头范数。

选择
$$
f\in(\ker D^2\ominus\ker D)\cap\mathcal H_q,\qquad \|f\|=1.
$$
这种 $f$ 存在：取非零 $g\in\ker D\cap\mathcal H_{q-1}$，再归一化 $D_q^\dagger g$；固定孔满射保证有定义，单步MP保证与 $\ker D$ 正交。primitive 层非零可在足够大的有限位置集上由删除映射的维数差直接得到。

取实际源 $r=e_0f\in\mathscr R_q$。一个明确左可行向量是
$$
\ell=e_1f\big|_q-c_1Df\big|_{q-1}.
$$
相邻 $D/A$ 项准确相消，最下面由 $D^2f=0$ 消失；顶端源是 $e_0f$。所以 $\ell\in\mathscr V_q$、$E_q\ell=r$。

令 $\Pi$ 为原左零源空间 $\ker E_q$ 的正交投影。任何 $u\in\ker E_q$ 的顶层满足 $Au_q=0$，故其顶层只有第零头。因此 $e_1f|_q\perp\ker E_q$，真正左最小者准确为
$$
v=E_q^\dagger r
=e_1f\big|_q-(I-\Pi)(c_1Df\big|_{q-1}).
$$
两项仍正交：原第二项与 $e_1f$ 正交，而 $\Pi$ 的顶层只有第零头。于是
$$
\boxed{
1\le\mu_q(r)^2
=1+\|(I-\Pi)(c_1Df)\|^2
\le1+\|c_1\|^2\nu_m^2.
}
$$

由于 $P_{\ker D}f=0$，整个原尾 primitive 投影只读取第二项，故
$$
\boxed{
\|P_{\ker D}v\|
\le\|c_1\|\nu_m\le\frac{\|c_1\|}{m}.
}
$$
沿 $m\to\infty$、任意合法 $q=q_m$ 选取这样的源，左费趋于一，但全部primitive坐标的范数趋于零。因而不能从 $p=P_{\ker D}v$ 直接推出一个与头 $m$ 无关的反向重建常数；完整坐标映射的非primitive部分确实需要分析。

另一方面，任何裸可行右输入 $a$ 都满足 $Da_1=r$。因此
$$
\boxed{\alpha_q(r)\ge\nu_m^{-1}\|r\|\ge m.}
$$
该例的裸费很大，明确不在原真实小裸费来源锥内。它既没有给实际 $W$ 向量，也没有否定 $\mu\le C_m(\alpha+\lambda_{\rm flat})$，更没有否定原所需的允许增长 $C_m$。
