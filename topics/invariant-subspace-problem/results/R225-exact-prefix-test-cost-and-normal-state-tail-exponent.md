# R225：指定正柱测试的精确指数成本与正常态尾下界

日期：2026-11-13（UTC+8）。作者：normal_states。

状态：以下成本渐近与正常态必要条件完整。本稿计算的是指定测试族的精确成本，不断言所有可能的主理想测试都具有相同的最小成本，也不把尾速率必要条件当成任意正常态不存在。

## 1. 结论

令 $a_j=(j+1)^{-2}$，逐位任取 $X_j=N_j$ 或 $Y_j$，系数均为正，置
$$
S=\sum_{j\ge0}a_jX_j,\quad
L_m=\sum_{j<m}a_jX_j,\quad U_m=\sum_{j\ge m}a_jX_j,
$$
$$
c_m=\langle U_m\Omega_{\ge m},\Omega_{\ge m}\rangle,
\quad R_m=(c_mI+L_m)^{-1},\quad J_m=SR_m.
\tag{1.1}
$$
其中 $\Omega_{\ge m}$ 是原 Haar 物理参考尾；$U_m$ 精确只作用于该尾。本轮 R215 已证明 $J_m\in S\mathcal A$ 及对低 $m$ 位 Haar 柱投影 $P_m$，
$$
\|P_mJ_mP_m-P_m\|\le\tfrac14\quad(m\ge2).
\tag{1.2}
$$
同一计算逐位用于混选时完全不变，不需要混选后的 $S$ 全空间单射或稠密像。

定义
$$
I(u)=\int_0^1\operatorname{arsinh}\!\left(\frac{u}{2x^2}\right)dx,
\qquad
\mathsf F=\max_{u\ge0}\{I(u)-u/2\}.
\tag{1.3}
$$
该最大值在唯一 $u_*>0$ 取得，且
$$
\int_0^1\frac{dx}{\sqrt{4x^4+u_*^2}}=\frac12,
\qquad
\mathsf F=\operatorname{arsinh}(u_*/2)+u_*/2.
\tag{1.4}
$$
用于识别的近似值为
$$
u_*=1.834113905607801084\ldots,\qquad
\mathsf F=1.738548574853664733\ldots.
$$
证明不依赖这些小数。

**定理1.1。** 一致于逐位的 $N/Y$ 选择，
$$
\boxed{
\log\|R_m\|=\mathsf Fm+O(\log^2(m+2)),\qquad
\log\|J_m\|=\mathsf Fm+O(\log^2(m+2)).
}
\tag{1.5}
$$

**定理1.2。** 若 $\rho\ge0$ 为原 Haar 空间上的迹类算子，$\operatorname{Tr}\rho=1$，且
$$
\operatorname{Tr}(\rho SF)=0\quad(F\in\mathcal A),
\tag{1.6}
$$
定义
$$
q_m=\operatorname{Tr}(\rho(I-P_m)).
$$
则存在不依赖 $\rho$ 或混选的绝对常数 $C>0$，使对全部充分大 $m$，
$$
\boxed{
q_m\ge\exp\bigl(-2\mathsf Fm-C\log^2(m+2)\bigr).
}
\tag{1.7}
$$
特别
$$
\boxed{
\limsup_{m\to\infty}\frac{-\log q_m}{m}\le2\mathsf F
=3.477097149707329465\ldots.
}
\tag{1.8}
$$
量词包括任意秩的正常正状态；对正有限秩状态同样成立。

## 2. 尾标量与一个保真头/纯中段模型

由真实递推和 Haar 期望，
$$
\langle N_j\Omega,\Omega\rangle
=\frac12+\frac{\eta_j}{2}\langle N_{j+1}\Omega,\Omega\rangle,
$$
而 $Y_j\Omega=(1-\chi_j)/2$ 给期望准确等于 $1/2$。所以若
$s_m=\sum_{j\ge m}a_j$，有
$$
\frac{s_m}{2}\le c_m\le\frac{s_m}{2}(1+e^{-77016^m}),
\qquad \frac1{m+1}\le s_m\le\frac1m.
$$
这里直接使用 $j\ge m$ 时 $\eta_j\le e^{-77016^m}$ 和 $\|N_{j+1}\|\le1$，不需要另加实际 $\eta_j$ 的单调性假设。
因此
$$
\beta_m:=mc_m=\frac12+O(m^{-1}),\qquad
\frac1{2(m+1)}\le c_m\le\frac1m.
\tag{2.1}
$$

取
$$
h=h(m)=1+\lceil\log_{16}(4(m+1))\rceil=O(\log m).
$$
对充分大的 $m$ 有 $h<m$。定义保真低头与纯中段
$$
K_m=H_h+\sum_{h\le j<m}a_jE_j,
\qquad H_h=\sum_{j<h}a_jX_j^{[h]}.
\tag{2.2}
$$
$K_m$ 精确只作用于低 $m$ 位；低于 $h$ 的全部 carry 被保留，第 $h$ 位后改用纯矩阵。

本轮逐项 carry 预算给
$$
\|L_m-K_m\|\le26e^{-77016^{h-1}}
\le26e^{-3080(m+1)}=:\varepsilon_m.
\tag{2.3}
$$
这来自低头差至多 $18e^{-77016^{h-1}}$ 与纯中段差至多 $8e^{-77016^{h-1}}$。

R215 的统一预解界同时给
$$
\|R_m\|,\|(c_mI+K_m)^{-1}\|
\le D_m:=4(m+1)e^{256(m+1)}.
$$
因此实际逆差满足
$$
\boxed{
\|R_m-(c_mI+K_m)^{-1}\|
\le\varepsilon_mD_m^2
\le416(m+1)^2e^{-2568(m+1)}.
}
\tag{2.4}
$$
下文先求 $K_m$ 的预解成本，再用 (2.4) 转回 $L_m$。

## 3. 变分常数的性质

对 $u>0$，可对积分直接求导：
$$
I'(u)=\int_0^1\frac{dx}{\sqrt{4x^4+u^2}}.
\tag{3.1}
$$
它连续且严格递减，$u\downarrow0$ 时趋于无穷，$u\to\infty$ 时趋于0。前者由 $x=\sqrt u\,v$ 得到，后者由 $I'(u)\le1/u$ 得到。因此唯一 $u_*$ 满足 $I'(u_*)=1/2$，且它是严格凹函数 $I(u)-u/2$ 的唯一最大点。

有 $I(0)=0$，且
$$
I(u)\le\log(1+u)+2,
\tag{3.2}
$$
因为 $\operatorname{arsinh}(u/(2x^2))\le\log(1+u)+2|\log x|$ 于 $0<x\le1$。故最大值有限。小 $u$ 时 $I'(u)\to\infty$ 又给 $\mathsf F>0$。

分部积分准确给
$$
I(u)=\operatorname{arsinh}(u/2)+2uI'(u),
$$
代入 $u_*$ 即得 (1.4)。

对 $\beta>0$，记
$$
F(\beta)=\max_{u\ge0}\{I(u)-\beta u\}.
$$
在 $\beta\in[1/4,3/4]$ 上，所有最大点满足 $u\le4$，因为 $I'(u)\le1/u$。因此
$$
|F(\beta)-F(1/2)|\le4|\beta-1/2|.
\tag{3.3}
$$
这个显式 Lipschitz 界用来控制缓慢变化的 $c_m$。

## 4. 模型预解的上界

头与中段精确交换，因此 Laplace 积分给
$$
\|(c_mI+K_m)^{-1}\|
\le\int_0^\infty e^{-c_mt}\,
\|e^{-tH_h}\|\,
\left\|e^{-t\sum_{h\le j<m}a_jE_j}\right\|dt.
\tag{4.1}
$$
纯矩阵单因子的精确奇异值为
$$
\log\|I+wE_j\|=\operatorname{arsinh}(|w|/2).
$$
故纯中段的对数范数至多
$$
\sum_{n=1}^m\operatorname{arsinh}(t/(2n^2)).
$$
令 $t=m^2u$。因被积函数随 $x$ 递减，其右 Riemann 和准确满足
$$
\sum_{n=1}^m\operatorname{arsinh}\!\left(\frac{m^2u}{2n^2}\right)
\le m I(u).
\tag{4.2}
$$

对真实低头使用 R215 的单因子估计，
$$
\log\|e^{-tH_h}\|
\le h\log(2(1+3t))+2(\log_+(3t))^{4/3}.
$$
$h=O(\log m)$，且 $t=m^2u$，所以对所有 $u\ge0$，存在绝对常数 $B$ 使
$$
\log\|e^{-m^2uH_h}\|
\le B\log^2(m+2)+B\log(m+2)u.
\tag{4.3}
$$
可由 $\log(1+3m^2u)\le\log(1+3m^2)+\log(1+u)$、$\log(1+u)\le u$，以及
$\sup_{u>0}(\log(1+u))^{4/3}/u<\infty$ 逐项得到。

把 (4.2)—(4.3) 代入 (4.1)，置
$$
\beta'_m=\beta_m-B\log(m+2)/m=\frac12+O(\log m/m),
$$
得到
$$
\|(c_mI+K_m)^{-1}\|
\le m^2e^{B\log^2(m+2)}
\int_0^\infty e^{m(I(u)-\beta'_m u)}du.
\tag{4.4}
$$
对充分大 $m$，$\beta'_m\in[1/4,3/4]$。由 (3.2)，可固定大 $R$，使 $u\ge R$ 时 $I(u)\le u/8$。于是在 $[0,R]$ 上用最大值界，在尾部用 $e^{-mu/8}$，得到
$$
\int_0^\infty e^{m(I(u)-\beta'_m u)}du
\le(R+8)e^{mF(\beta'_m)}.
$$
最后使用 (3.3)，
$$
\boxed{
\log\|(c_mI+K_m)^{-1}\|
\le\mathsf Fm+O(\log^2(m+2)).
}
\tag{4.5}
$$

## 5. 正锥与有限头真空给匹配的下界

低于 $h$ 的物理全1真空被 $H_h$ 杀掉；在该低头真空张量中段空间的子空间上，$K_m$ 精确限制为
$$
D_{h,m}=\sum_{h\le j<m}a_jE_j.
$$
逐位符号酉共轭把 $D_{h,m}$ 变为 $-D_{h,m}$，故
$$
\|(c_mI+K_m)^{-1}\|
\ge\|(c_mI+D_{h,m})^{-1}\|
=\|(c_mI-D_{h,m})^{-1}\|.
\tag{5.1}
$$

$D_{h,m}$ 是有限物理坐标正锥上的正算子。逐项比较幂级数给
$$
0\le e^{tD_{h,m}}
\le c_m e^{c_mt}(c_mI-D_{h,m})^{-1}.
$$
正算子的 $\ell^2$ 范数单调，所以
$$
\|(c_mI-D_{h,m})^{-1}\|
\ge c_m^{-1}e^{-c_mt}\|e^{tD_{h,m}}\|.
\tag{5.2}
$$

在 (5.2) 中取 $t=m^2u_*$。有限 Riemann 和的误差满足
$$
0\le mI(u_*)-
\sum_{n=1}^m\operatorname{arsinh}\!\left(\frac{m^2u_*}{2n^2}\right)
\le m\int_0^{1/m}\operatorname{arsinh}\!\left(\frac{u_*}{2x^2}\right)dx
=O(\log(m+2)).
$$
再删去前 $h=O(\log m)$ 项，损失至多
$h\operatorname{arsinh}(m^2u_*/2)=O(\log^2m)$。因此
$$
\log\|e^{m^2u_*D_{h,m}}\|
\ge mI(u_*)-O(\log^2(m+2)).
$$
由 $\beta_m=1/2+O(1/m)$，(5.1)—(5.2) 给
$$
\boxed{
\log\|(c_mI+K_m)^{-1}\|
\ge\mathsf Fm-O(\log^2(m+2)).
}
\tag{5.3}
$$
结合 (4.5) 与实际逆差 (2.4)，得到 (1.5) 关于 $R_m$ 的部分。

## 6. $J_m$ 的成本不能在此族中消失

置 $Q_m=(c_mI+K_m)^{-1}$，并定义模型测试
$$
\widetilde J_m=(K_m+U_m)Q_m
=I+(U_m-c_mI)Q_m.
\tag{6.1}
$$
$Q_m$ 只作用低 $m$ 位，$U_m-c_mI$ 只作用尾。因此这是实际 Hilbert 张量积，而有准确范数等式
$$
\|(U_m-c_mI)Q_m\|=\|U_m-c_mI\|\,\|Q_m\|.
\tag{6.2}
$$
$U_m$ 拟幂零，故 $U_m-c_mI$ 的谱半径为 $c_m$。另一方面 $\|U_m\|\le3/m$，所以
$$
\frac1{2(m+1)}\le c_m\le\|U_m-c_mI\|\le\frac4m.
\tag{6.3}
$$
由 (6.1)—(6.3)，在指数级的 $\|Q_m\|$ 前只损失多项式因子与加法常数1，因而
$$
\log\|\widetilde J_m\|=\mathsf Fm+O(\log^2(m+2)).
$$
最后
$$
\|J_m-\widetilde J_m\|
\le\|S\|\,\|R_m-Q_m\|+\|L_m-K_m\|\,\|Q_m\|
\le7\varepsilon_mD_m^2,
$$
由 (2.4) 指数趋零。这给 (1.5) 关于 $J_m$ 的部分。

因此不能在这一个 $J_m$ 测试族中把指数成本删除。本文没有推导“所有可能的 $S\mathcal A$ 测试都至少有该成本”。

## 7. 正常正湮灭态的尾限制

设 (1.6) 成立，置 $\delta_m=\sqrt{q_m}$。Hilbert–Schmidt 分解给
$$
\|\rho-P_m\rho P_m\|_1\le2\delta_m.
$$
(1.2)、正性与 $\phi(J_m)=0$ 因而给
$$
\frac34(1-\delta_m^2)\le2\|J_m\|\delta_m.
\tag{7.1}
$$
从 (7.1) 可统一推出
$$
\delta_m\ge\frac1{4(1+\|J_m\|)}.
\tag{7.2}
$$
确实，若 $\delta_m\ge1/2$，右边不超过 $1/4$；否则左边至少 $9/16$，所以
$\delta_m\ge9/(32\|J_m\|)\ge1/(4(1+\|J_m\|))$。

平方 (7.2) 并用 (1.5)，便有 (1.7)—(1.8)。所有代价只来自固定算子族，故误差常数不依赖 $\rho$ 或其秩。

若 $\rho=M^{-1}\sum_{\nu=1}^d x_\nu\otimes x_\nu$，其中
$M=\sum_\nu\|x_\nu\|^2>0$，则同一结论准确写成
$$
\frac{\sum_\nu\|(I-P_m)x_\nu\|^2}{\sum_\nu\|x_\nu\|^2}
\ge\exp\bigl(-2\mathsf Fm-C\log^2(m+2)\bigr).
$$
有限秩本身不保证任何相反的通用尾上界，故这里依然不能排除任意有限秩见证。

## 8. 结果的使用范围

本稿将原 $R215$ 的粗指数柱尾限制提升到由有限区间变分式 (1.3) 决定的常数，并同时给出该指定 $R_m,J_m$ 族的匹配下界。它比只使用全符号精确预解型后代入 $c_m\sim1/(2m)$ 更精细，因为有限头截断在尺度 $m$ 上改变了积分上限。

该差别必须保留：全符号对应积分区间 $(0,\infty)$，本稿前缀对应 $(0,1)$。没有把两个常数混用，也没有把全空间范数测试向量搬到未知 Haar 子空间。正常态、有限秩接口与普通 Hilbert ISP 的剩余缺口维持原状。
