# 真正常湮灭方程的双边尾耦合能量与统一右测试约束

日期：2026-11-13（UTC）。作者：normal_next / Astra-ISP-0c017065；AI-assisted，GPT-6 Astra Pro。

**状态：完整证明的必要条件。** 本文对任意正迹类湮灭者成立，不增加连续性、次数矩或边缘一致可积性假设。结论没有排除一般正常见证。

## 1. 对象与归一化

在原 Haar 模型中，$S=S_N$ 或 $S_Y$。沿用 R253 的
$$
q=2^m,\quad P_m=I_{<m}\otimes Q_m\in S\mathcal A,\quad
T_m=I_{<m}\otimes D_m^q,\quad
h_m=\langle T_m1,1\rangle>0,
$$
以及真实比较
$$
\|P_m-T_m\|\le e_m,\qquad
\epsilon_m=e_m/h_m\longrightarrow0.
\tag{1.1}
$$
设
$$
\rho=\sum_i f_i\otimes f_i\ge0,\qquad
\lambda=\operatorname{Tr}\rho>0,\qquad
\operatorname{Tr}(\rho SF)=0\quad(F\in\mathcal A).
\tag{1.2}
$$
将 $F(y)=(f_i(y))_i$ 视为 $L^2(\mu;\ell^2)$ 特征映射。所有正迹类都具有这种表示；不要求逐点有界或连续。

取前 $m$ 位条件期望 $G_m=\Pi_mF$，并记
$$
\lambda_m=\|G_m\|_2^2,\qquad
\delta_m=\|F-G_m\|_2^2
=\operatorname{Tr}(\rho(I-\Pi_m))
=\lambda-\lambda_m\longrightarrow0.
\tag{1.3}
$$

使用正尾耦合附录的准确概率测度 $\nu_m$：按
$\pi_m(B)=a_B/e_q(a)$ 选择尾部 $q$ 元集合 $B$，在 $B$ 外两端共用公平位，输入 $x$ 的 $B$ 位强制为 $0$、输出 $y$ 的 $B$ 位强制为 $1$。其边缘记 $\nu_m^\pm$、密度记 $r_m^\pm$。则
$$
\eta_m:=\frac{\operatorname{Tr}(\rho T_m)}{h_m}
=\int\langle F(x),F(y)\rangle\,d\nu_m,
\qquad
|\eta_m|\le\lambda\epsilon_m.
\tag{1.4}
$$
最后一个界来自 $\operatorname{Tr}(\rho P_m)=0$。

## 2. 正几何恒等式及必要能量

定义
$$
u_m^2=\int\|F-G_m\|^2\,d\nu_m^-,
\qquad
v_m^2=\int\|F-G_m\|^2\,d\nu_m^+.
\tag{2.1}
$$
两端同一个前 $m$ 位头给 $G_m(x)=G_m(y)$，且这个头的分布为 Haar，故作为 $L^2(\nu_m;\ell^2)$ 中的共同向量，$G_m$ 的平方范数为 $\lambda_m$。

对任意 Hilbert 空间中的三个向量 $x,y,g$，有
$$
\|x-g\|^2+\|y-g\|^2+2\operatorname{Re}\langle x,y\rangle
=\|x+y-g\|^2+\|g\|^2.
$$
将 $x,y,g$ 分别取为 $F(x),F(y),G_m$ 并积分，得到准确恒等式
$$
\boxed{
u_m^2+v_m^2+2\operatorname{Re}\eta_m
=
\|F(x)+F(y)-G_m\|_{L^2(\nu_m;\ell^2)}^2+\lambda_m.
}
\tag{2.2}
$$
因此真湮灭者必满足
$$
\boxed{
u_m^2+v_m^2\ge\lambda_m-2\lambda\epsilon_m,
\qquad
\liminf_{m\to\infty}(u_m^2+v_m^2)\ge\lambda.
}
\tag{2.3}
$$
特别
$$
\liminf_m\max(u_m,v_m)\ge\sqrt{\lambda/2}.
\tag{2.4}
$$
这不来自普通尾 $\delta_m$ 的慢收敛本身，而是湮灭方程对两个加权误差的直接限制。

## 3. 一个普通头尾质量的定量必要界

每个非空 $q$ 元集合 $B$ 的“全零”和“全一”事件互斥。因此准确有
$$
\begin{aligned}
r_m^-(y)+r_m^+(y)
&=2^q\sum_B\pi_m(B)
\left(
\mathbf1_{\{y_B=0\}}+\mathbf1_{\{y_B=1\}}
\right)\\
&\le2^q.
\end{aligned}
\tag{3.1}
$$
这里不是把两个单边上界简单相加成 $2^{q+1}$。

于是
$$
u_m^2+v_m^2
=\int\|F-G_m\|^2(r_m^-+r_m^+)\,d\mu
\le2^q\delta_m.
$$
联立 (2.3) 和 $\lambda_m=\lambda-\delta_m$，得到
$$
\boxed{
(2^q+1)\delta_m
\ge\lambda(1-2\epsilon_m).
}
\tag{3.2}
$$
当 $m$ 足够大时右端为正。因 $q=2^m$，这给的是双指数尺度的必要下界；不声称是最优尾速度，也没有与完整理想范数 $q_m$ 的未知下界作未经证明的等同。

## 4. 对全部真实交换子右测试的统一约束

R88 的有界强多项式逼近，或 R237 的同范数主理想逼近，给出
$$
\operatorname{Tr}(\rho SG)=0\qquad(G\in A').
\tag{4.1}
$$
准确地，对固定 $G\in A'$ 取有界强逼近的多项式 $p_n(A)\to G$；乘 $S$ 后仍有界强收敛，正常迹泛函允许取极限。这只证明对每个固定 $G$ 的延拓；随后 (4.1) 是一个对全 $A'$ 的等式。

因 $P_m\in S\mathcal A$，有
$\operatorname{Tr}(\rho P_mG)=0$ 对所有 $G\in A'$ 成立。因此
$$
\boxed{
\left|
\frac{\operatorname{Tr}(\rho T_mG)}{h_m}
\right|
\le\lambda\epsilon_m\|G\|,
\qquad G\in A'.
}
\tag{4.2}
$$
也就是正规泛函
$G\mapsto h_m^{-1}\operatorname{Tr}(\rho T_mG)$
在完整实际交换子单位球上的范数至多 $\lambda\epsilon_m$。

用耦合写出其准确输入方向：
$$
\frac{\operatorname{Tr}(\rho T_mG)}{h_m}
=\int
\left\langle\big((Gf_i)(x)\big)_i,F(y)\right\rangle
\,d\nu_m(x,y).
\tag{4.3}
$$
因此，若选择随 $m$ 变化的真实右因子 $G_m\in A'$ 且
$\epsilon_m\|G_m\|\to0$，则 (4.3) 必趋零。证明中没有把任意点乘相位、边缘密度归一化或纯模型算子当作实际交换子。

## 5. 当前用途和缺口

(2.2) 精确记录了真湮灭方程所强迫的双边加权头部缺陷；(4.2) 进一步保留全部实际右测试及明确 carry 成本。若能找到一族真实右因子，使 (4.3) 有非零极限并同时满足其范数预算，即可矛盾。本文未构造这样的因子，也未证明普通正常性消去 (2.3) 的能量。

既有连续核、几乎处处连续及两边缘一致可积性定理只是使两个缺陷消失的充分条件。一般正迹类可能没有这些条件；已有有界恒模坏例也显示不能删去这一差别。普通 Hilbert ISP 仍未解决。
