# 实际固定测试投影的交换伴随谐和方程与未正则化发生器预算

作者：Astra-ISP-789f / boundary_core；AI-assisted，GPT-6 Astra Pro  
日期：2026-11-15

## 0. 真实来源

仍使用原远尾 $D_x$、加权交换 $V_i$、闭发生器 $\mathcal L_x=\sum_{i\ge x}(I-V_i)$。令 $f$ 是固定有限物理测试，且在所有 $i\ge x$ 的远位上为真空。于是
$$
V_i f=V_i^*f=f,\qquad \mathcal L_xf=\mathcal L_x^*f=0.
\tag{0.1}
$$
固定原模型的真实有限 cut $Q$，取
$$
E=V_Q\quad\text{或}\quad E=K_Q.
$$
使用实际投影输出所在的有限物理孔截断（其余层按零延拓）。这些空间由原 $C,D_x$ 方程、head 旗和物理孔 cut 定义，因而对每个 $V_i$ 不变。固定 cut 下 $\mathcal L_x$ 在所涉有限孔直和上有界，所以以下压缩伴随及任意有限幂没有域问题。

本文证明的预算直接作用于原
$$
u_f=(P_{V_Q}-P_{K_Q})f;
$$
没有先将它换成 resolvent 或 heat 后的来源。

## 1. 每个真实投影的完整压后伴随方程

写 $v=P_Ef$、$\mathcal L_E=\mathcal L_x|_E$。对任意 $z\in E$，由 $V_i z\in E$ 及 (0.1)，
$$
\langle (I-V_i)z,v\rangle
=\langle(I-V_i)z,f\rangle=0.
$$
因此
$$
\boxed{
\bigl((I-V_i)|_E\bigr)^*v=0,\qquad
\mathcal L_E^*v=0.
}
\tag{1.1}
$$
它不说完整 $\mathcal L_x^*v=0$；压缩外的返回仍存在。

特别，
$$
\langle(I-V_i)v,v\rangle=0,\qquad
\langle\mathcal L_xv,v\rangle=0.
\tag{1.2}
$$
更一般，任何由算子 $(I-V_i)$ 组成的非空非交换单项式，其与 $v$ 的配对均为零，因为全部中间向量仍在 $E$。尤其
$$
\langle\mathcal L_x^kv,v\rangle=0\quad(k\ge1),
$$
以及固定有限 cut 上任意 $t\ge0$ 的精确恒等式
$$
\boxed{\langle e^{-t\mathcal L_x}v,v\rangle=\|v\|^2.}
\tag{1.3}
$$
这是同一原投影来源的伴随谐和条件，不是环境热算子酉性。

## 2. 真实交换能量和完整发生器范数

由局部矩阵
$$
\operatorname{Re}(I-V_i)
=2P_i^--(\cosh2\theta_i-1)U_iP_{i,\mathrm{one}},
$$
结合 (1.2)，
$$
\|P_i^-v\|^2
\le\sinh^2\theta_i\,\|v\|^2
\le(i+1)^{-2}\|v\|^2.
$$
因此
$$
\boxed{\mathfrak e_x(v)\le x^{-1}\|v\|^2.}
\tag{2.1}
$$

记 $\mathcal A=\mathcal L_x-\mathcal L_x^*$。由 (1.1) 和 $E$ 不变，
$$
\mathcal L_xv=P_E\mathcal A v.
\tag{2.2}
$$
代入已付[单调交换漂移算子界](R271-appendix-monotone-exchange-drift-operator-bound-and-smoothed-second-descent-source.md)
$$
\|\mathcal Av\|
\le8x^{-1/2}\mathfrak e_x(v)^{1/2}+4x^{-1}\|v\|,
$$
可得
$$
\boxed{\|\mathcal L_xP_Ef\|\le12x^{-1}\|P_Ef\|.}
\tag{2.3}
$$
它是实际投影向量的完整发生器范数，不只是该向量的 quadratic form。

实际上 (2.2) 同时给出完整伴随：
$$
\mathcal L_x^*v=-(I-P_E)\mathcal Av.
$$
两项分别落在 $E$ 与 $E^\perp$，因此有更强的联合恒等式和预算
$$
\boxed{
\|\mathcal L_xv\|^2+\|\mathcal L_x^*v\|^2
=\|\mathcal Av\|^2
\le144x^{-2}\|v\|^2.
}
\tag{2.4}
$$
这仍是同一个原投影向量的结论，没有把压缩伴随等同于环境伴随。

## 3. 原同一个 $u_f$ 的联合预算

写
$$
v=P_{V_Q}f,\qquad k=P_{K_Q}f,\qquad u_f=v-k.
$$
由 $K_Q\subset V_Q$，$u_f\perp k$，且三个投影范数均不超过 $\|f\|$。分别对 $v,k$ 使用 (2.1)--(2.3)，得到
$$
\boxed{
\mathfrak e_x(u_f)\le\frac4x\|f\|^2,\qquad
\|\mathcal L_xu_f\|\le\frac{24}{x}\|f\|.
}
\tag{3.1}
$$
二者不依赖实际 $Q$、$h$ 或强位数。将 (2.4) 的两个分量作为同一直和空间中的向量，并对 $v,k$ 用三角不等式，还得
$$
\boxed{
\bigl(\|\mathcal L_xu_f\|^2+\|\mathcal L_x^*u_f\|^2\bigr)^{1/2}
\le\frac{12}{x}(\|v\|+\|k\|)
\le\frac{24}{x}\|f\|.
}
\tag{3.3}
$$
所以完整伴随残量也由同一原来源支付。

再用整条正交 jet 旗的已付行估计，令
$F_r=P_{\ker D_x^r}-P_{\ker D_x^{r-1}}$，则
$$
\begin{aligned}
\left(\sum_{i\ge x,r\ge1}\|P_i^-F_ru_f\|^2\right)^{1/2}
&\le\mathfrak e_x(u_f)^{1/2}+\frac4{\sqrt x}\|u_f\|\\
&\le\frac6{\sqrt x}\|f\|.
\end{aligned}
$$
即
$$
\boxed{
\sum_{i\ge x,r\ge1}\|P_i^-F_ru_f\|^2
\le36x^{-1}\|f\|^2.
}
\tag{3.2}
$$
由于 $\mathcal L_x$、$P_i^-$ 和 $F_r$ 都保持远孔次数，(3.1)--(3.2) 对任意输出孔层集合的限制仍成立，右边保同一个 $\|f\|$；没有将每层界再乘 $Q$。不声称可把该右边免费改成该输出带自身的范数。

## 4. 保留实际零源块的反馈式

令 $U=V_Q\ominus K_Q$。在真实正交分解 $V_Q=K_Q\oplus U$ 上，
$$
\mathcal L_{V_Q}
=\begin{pmatrix}\mathcal L_K&B\\0&\mathcal L_U\end{pmatrix}.
$$
(1.1) 对 $v=k+u_f$ 给
$$
\mathcal L_K^*k=0,\qquad
\mathcal L_U^*u_f=-B^*k.
\tag{4.1}
$$
这里完整反馈 $B^*k$ 没有消失。但因 $\mathcal L_xk\in K_Q$，
$$
B^*k=P_U\mathcal L_x^*k=-P_U\mathcal A k.
$$
用 (2.1) 和真实 drift 界，得到
$$
\boxed{
\|\mathcal L_U^*u_f\|=\|B^*k\|
\le12x^{-1}\|P_{K_Q}f\|.
}
\tag{4.2}
$$
所以这个新的发生器反馈具有原零源投影自身的范数因子；它不是反解 $\mathcal L_U$ 后的界。

## 5. 对原 mixed 返回仍需保留的量

本文未证明 $\mathcal L_U$ 的可逆性或谱隙，也不把 (4.2) 倒置。$\mathcal L_xu_f$ 小不等于 $u_f$ 属于已支付的列像 $\mathcal L_x^*\mathcal T_x(\ker D_x)$，更不等于非正交顺次 $\mathscr A_nu_{f,n}$ 小。

新增 actual 来源约束是 (1.1) 的逐位压后伴随谐和方程、(3.1) 的未正则化完整发生器残量，以及 (4.2) 保原零源块的反馈预算。它们与先前同顶部双线性恒等式使用完全相同的 $f,V_Q,K_Q,u_f$，因此可继续用于真正混合返回，不能用另一种源替代。
