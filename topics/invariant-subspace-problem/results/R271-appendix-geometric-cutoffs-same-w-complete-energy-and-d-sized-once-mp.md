# R271 补充：几何起点的原同 W 全塔能量与 R=d 的完整一次 MP 预算

日期：2026-11-26（UTC）。

作者：Astra-ISP-347c-20261126 / r271_source；AI-assisted，GPT-6 Astra Pro。

**状态：已证明。** 新的准确层权允许在任意固定几何增长起点上，同时使用全部 $1\le j<h$ 的原完整头 inverse。与旧 $\tau_{14}$ 无权整行和旧分离高度带分别区别如下：这里可以取 $R=d$，不删除或分离任何高度，代价是原完整 boson 方差取 $s\ge8S_x$。证明仍从同一个实际 $w/u$ 的准确低 forcing 同余出发。随后直接调用已证明的一次完整 MP 定理，不重做其全层 $512^j$ 费用；完整后续修复仍未完成。

依赖：

- [任意几何起点的全部正孔层权整行](R271-appendix-all-positive-far-hole-moving-coherent-rows-and-matched-source-cost.md)，§§1--3、7。
- [旧 $\tau_{14}$ 完整无权行及同 W 能量](R271-appendix-cross-head-all-height-coherent-bessel-and-same-w-full-energy-summability.md)，§§3--6：本稿保其原同源论证，换入新的实际加权代表。
- [旧分离高度带的 $R=d$ 参数门](R271-appendix-separated-height-bands-exact-full-head-bessel-and-d-sized-prefix-budget.md)，§§1--3。
- [固定方差倍数的一次完整 MP](R271-appendix-fixed-variance-full-height-once-mp-and-same-w-summable-correction.md)，§§1--5。

旧无权整行定理在
$e^{(25/2)d_m^3}\le x_m\le e^{13d_m^3}$、$h_m\le2x_m$
的快速起点上，已给全部 $1\le j<h_m$ 的 Bessel 常数 $2$，且没有高度损失。
旧分离高度带稿则在 $m\in4\mathbb N$、$R=d$、$Q=4d$，
只使用互相分离的
$I_m\subset[1,\sqrt{x_m+1}/(8(m+1))]$。
本稿不将这两条已登记结论重新声称为新结果。

## 1. 原同一 w 和准确层权

取原合法母参数族
$$
d_\ell=2^{m_\ell},\quad R_\ell\ge0,\quad
x_\ell=m_\ell+R_\ell,\quad h_\ell=d_\ell+R_\ell,\quad
C_\ell=A_{m_\ell}+D_{[m_\ell,x_\ell)},\quad C_\ell^{h_\ell}=0,
$$
并假设
$$
x_{\ell+1}\ge\lambda(x_\ell+1),\quad\lambda>1,\qquad
h_\ell-1\le2x_\ell,
\tag{1.1}
$$
$$
4d_\ell\le Q_\ell\le e^{(1601/64)d_\ell^3},\qquad
Q_\ell\ge R_\ell+h_\ell-1.
\tag{1.2}
$$
固定同一个原 $w\in W$，记 $W_0=\|w\|$、$g_\ell=P_{x_\ell}w$，
以及原
$$
u_\ell=(P_{V_{m_\ell,Q_\ell}}-P_{K_{m_\ell,Q_\ell}})w,\qquad
\|u_\ell-P_{\mathcal N_{m_\ell}\le Q_\ell}w\|
\le2\eta_{m_\ell}W_0,\qquad
\eta_m=e^{-6(2^m)^4}.
\tag{1.3}
$$
不为不同高度或后续 cut 更换 $w$。一般参数族沿用
$m_\ell\ge10$、$\sum_\ell\eta_{m_\ell}^2<\infty$；
第 5 节的明确选择自动满足。

以下暂省去 $\ell$。沿原尾令
$$
D=D_x,\quad S=S_x,\quad
\nu_j^2=(j!)^2e_j((i+1)^{-4}:i\ge x),\qquad
\omega_j^2=\frac{S_{x+j-1}}{jS_x},\quad 1\le j<h.
$$
$\omega_j$ 是本稿层权，不是物理创建向量。原归一化 coherent 行为
$\beta_{x,j}=\nu_j^{-1}D^jP_{\mathcal N_{\ge x}=j}$，
完整加权行是
$\mathcal B_x=(\omega_j\beta_{x,j})_{j\ge1}$。
已付
$$
\sum_\ell\|\mathcal B_{x_\ell}w\|^2
\le\mathcal B_\lambda W_0^2,\qquad
\mathcal B_\lambda=\frac{1+\lambda^{-3/2}}{1-\lambda^{-3/2}}.
\tag{1.4}
$$

## 2. 加权完整 Gram 及原物理同源代表

在整个原强头空间上定义
$$
H^\omega=I+\sum_{j=1}^{h-1}\frac{\omega_j^2}{\nu_j^2}(C^*)^jC^j,
\qquad a^\omega=(H^\omega)^{-1}g,
\qquad
\Delta^\omega=\|g\|^2-\langle g,a^\omega\rangle .
\tag{2.1}
$$
这是新的正算子，但最小化始终用原未加权头内积；没有改变物理内积。

取准确物理代表
$$
F^\omega=i_0a^\omega+
\sum_{j=1}^{h-1}
\frac{\omega_j^2(-C)^ja^\omega\otimes(D^*)^j\Omega}{\nu_j^2}.
\tag{2.2}
$$
其正高度部分正好为
$$
F^{\omega,+}=\mathcal B_x^*\xi,\qquad
\xi_j=\frac{\omega_j(-C)^ja^\omega}{\nu_j}\quad(1\le j<h),
\qquad \xi_j=0\quad(j\ge h).
\tag{2.3}
$$
由原完整正规方程，
$$
\boxed{
\Delta^\omega=
\|g-a^\omega\|^2+
\sum_{j=1}^{h-1}\frac{\omega_j^2\|C^ja^\omega\|^2}{\nu_j^2}
=\|g-a^\omega\|^2+\|\xi\|^2.
}
\tag{2.4}
$$
因为 $0<\omega_j\le1$ 且原远孔层正交，
$$
\boxed{
\|i_0g-F^\omega\|^2
=\|g-a^\omega\|^2+
\sum_{j=1}^{h-1}\frac{\omega_j^4\|C^ja^\omega\|^2}{\nu_j^2}
\le\Delta^\omega.
}
\tag{2.5}
$$
本稿不把 $F^\omega$ 声称为某个原物理真核投影，也不把 (2.5) 改写成错误的等式。

原逐列低 forcing 恒等式对
$j\le Q-R$ 同时给
$$
P_V(D^*)^ji_0=(-1)^jP_Vi_0(C^*)^j,
$$
且 $P_K$ 有同一身份。它的中间向量总孔支撑至多 $R+j-1<Q$。
代入 (2.2) 与 $H^\omega a^\omega=g$，准确得到
$$
\boxed{
P_VF^\omega=P_Vi_0g,\qquad
P_KF^\omega=P_Ki_0g.
}
\tag{2.6}
$$
全部列的原总尾孔数不超过 $R+h-1\le Q$。

## 3. 任意几何起点的完整同 W 能量可和

对 (1.3) 配对，(2.6) 与 (2.5) 给
$$
|\langle w,i_0g-F^\omega\rangle|
\le2\eta_mW_0\sqrt{\Delta^\omega}.
$$
另一方面，由 $g=P_xw$ 和 (2.3)，左边准确为
$$
|\Delta^\omega-\langle\mathcal B_xw,\xi\rangle|.
$$
结合 $\|\xi\|\le\sqrt{\Delta^\omega}$，
$$
\boxed{
\sqrt{\Delta^\omega}\le\|\mathcal B_xw\|+2\eta_mW_0.
}
\tag{3.1}
$$
零缺陷情形也直接成立。故
$$
\boxed{
\left(\sum_\ell\Delta_\ell^\omega\right)^{1/2}
\le\left(\sqrt{\mathcal B_\lambda}
 +2\sqrt{\sum_\ell\eta_{m_\ell}^2}\right)W_0.
}
\tag{3.2}
$$
特别，(2.4) 中完整 inverse 之后的头误差与全部正高度能量一起可和。
(2.3)、(1.4) 还给整个物理正高度级数的有界合成：
$$
\left\|\sum_\ell F_\ell^{\omega,+}\right\|^2
\le\mathcal B_\lambda\sum_\ell\|\xi_\ell\|^2
\le\mathcal B_\lambda\sum_\ell\Delta_\ell^\omega .
\tag{3.3}
$$
有限和先成立，平方可和来源的无限和按有界合成算子取原范数极限。

## 4. 返回原未加权完整 Fock Gram：固定倍数 8 已够

由准确层权及原尾积分比较，
$$
\omega_j^{-2}\le j(1+j/x)^3\le27j
\qquad(1\le j<h,\ h-1\le2x),
$$
而 $\nu_j^2\le j!S^j$。对 $j\ge2$，$8^j\ge27j$；
$j=1$ 则直接有 $\omega_1^2/\nu_1^2=1/S$。
因此
$$
\boxed{
I\preceq H_C(s)
:=\sum_{j=0}^{h-1}\frac{(C^*)^jC^j}{j!s^j}
\preceq H^\omega
\qquad(s\ge8S_x).
}
\tag{4.1}
$$
这里比较的 $H_C(s)$ 正是原完整未加权 Fock Gram。

令 $a_s=H_C(s)^{-1}g$、
$E_j(s)=\|C^ja_s\|^2/(j!s^j)$、
$\delta(s)=\|g\|^2-\langle g,a_s\rangle$。正逆 Loewner 序和原正规方程给
$$
\boxed{
\delta(s)=\|g-a_s\|^2+\sum_{j=1}^{h-1}E_j(s)
\le\Delta^\omega,\qquad s\ge8S_x.
}
\tag{4.2}
$$
所以对任何先于全部 cut 固定的合法 $s_\ell\ge8S_{x_\ell}$，
$$
\sum_\ell\left[
\|g_\ell-a_{s_\ell}\|^2+
\sum_{j=1}^{h_\ell-1}E_{\ell,j}(s_\ell)
\right]\le\sum_\ell\Delta_\ell^\omega<\infty.
\tag{4.3}
$$
没有把 $H^\omega$ 的 inverse 直接当作 $H_C(s)$ 的 inverse。

完整导数仍是
$$
\frac{d}{d\log s}\langle g,H_C(s)^{-1}g\rangle
=\mu_1(s):=\sum_{j=1}^{h-1}jE_j(s).
$$
故任取固定于该头的 $\Lambda_\ell>1$，可在
$[8S_{x_\ell},8\Lambda_\ell S_{x_\ell}]$ 内选同一次方差，使
$$
(\log\Lambda_\ell)\mu_{1,\ell}(s_\ell)\le\Delta_\ell^\omega.
\tag{4.4}
$$
例如 $\Lambda_\ell=x_\ell$ 时方差上端趋零，并得
$\sum_\ell(\log x_\ell)\mu_{1,\ell}(s_\ell)<\infty$。
所有该头的 $Q$、cut 和 partial 共同使用已选的这一方差。

## 5. 原 R=d 全高度小强段及全部母支持

一个明确选择是对所有整数 $m\ge10$ 取
$$
d=2^m,\qquad R=d,\qquad x=m+d,\qquad h=2d,\qquad Q=d^2h=2d^3.
\tag{5.1}
$$
此时 $R$ 偶，$h-1<2x$，且
$$
x_{m+1}\ge\frac32(x_m+1).
$$
最后一式等价于 $d\ge m+1$，在本范围成立。
因此 (1.4) 可取固定 $\lambda=3/2$。

$4d\le Q\le e^{(1601/64)d^3}$，
且 $Q\ge R+h-1$，故 (1.2) 完全保留。
若同时保旧真帽和所有右段，可取
$$
Q/2\le n\le Q-R-2h-1.
$$
其整数个数为 $N=d^3-5d>0$，并有
$$
h/N=\frac2{d^2-5}\le\frac3{d^2}.
\tag{5.2}
$$
所以相同的平方可和未来带误差仍可用。
这没有调用不同基头的免费改组或删除某些高度。
这里只支付来源和窗口，不据 (5.2) 宣称帽后的逆已付。

与旧分离高度带方案不同，(4.3) 在 (5.1) 中覆盖整个
$1\le j<2d$，包括其未覆盖的中、高段。其完整源始终是同一个 $P_xw$。

## 6. 原一次完整 MP 现可直接用于 R=d

记旧已付固定常数
$$
c_*=2\cdot512^2,\qquad K_*=1+47616c_* .
$$
对每个 (5.1) 的头，取
$$
s_m\in[c_*S_x,2c_*S_x],\qquad
a_m=H_C(s_m)^{-1}g_m,\qquad
f_m=\sum_{j=0}^{h-1}
\frac{(-C)^ja_m\otimes(D_x^*)^j\Omega}{j!s_m^j}.
$$
因 $c_*\ge8$，(4.2)--(4.3) 给完整正能量
$\epsilon_m=\sum_{j=1}^{h-1}E_{m,j}(s_m)$ 可和。
旧一次完整 MP 定理于是原样适用：
$$
q_{1,m}=D_x^\dagger(C+D_x)f_m,\qquad
\boxed{\|q_{1,m}\|^2\le K_*\epsilon_m.}
\tag{6.1}
$$
该调用保留原全层 $512^j$、全部 $j<h$ 以及 $C^h=0$ 的准确 top；
不另取 primitive 逆，不重证旧一次 MP。

令 $z_{1,m}=f_m-q_{1,m}$。原恒等式和 (4.2) 给
$$
(C+D_x)z_{1,m}=-Cq_{1,m},
$$
$$
\boxed{
\sum_m\|z_{1,m}-i_0g_m\|^2
\le2(1+K_*)\sum_m\Delta_m^\omega,\qquad
\sum_m\|(C+D_x)z_{1,m}\|^2
\le49K_*\sum_m\Delta_m^\omega .
}
\tag{6.2}
$$
这里只使用原 $\|C\|\le7$。所有向量只涉及有限个远孔层，
故 (6.1) 的整个 $D_x^\dagger$ 自然域已由旧定理支付。

还可在同一固定窗 $[c_*S_x,2c_*S_x]$ 中一次选择
$\mu_{1,m}(s_m)\le\Delta_m^\omega/\log2$。
新整行稿的实际物理合成式因而同时给原 $f_m$ 的全部正高度部分可和；
该选参仍先于这个头的全部 cut。

本节的 $f_m$ 保原 $P_V/P_K/u$ 身份。
一次修正后的 $z_{1,m}$ 只携带上述已付误差，
其剩余真实残量仍是 $-Cq_{1,m}$。完整 $CD_x^\dagger$ 循环、
最终真空约束、原物理核距离和稳定范围结论均未由本补充消去。


## 7. 同一小强段直接支付任意 M 来源的完整头矩

在本节只取 (5.1) 的 $R=d$ 参数，但放宽为任意原 $w\in M=\ker T$，
不要求 $w\in W$。仍令 $g_m=P_xw$。以下不使用 (1.3) 的 $W$ 特殊正交性，
也不改变原 $T$。

原逐位 carry 界为
$$
T-L_m=\sum_{L\ge m}K_L,\qquad
\|K_L\|\le52e^{-770\,16^{L-1}},\qquad L_m=C+D_x.
$$
非负尾和直接给
$$
\|T-L_m\|\le104e^{-(385/8)d^4}.
\tag{7.1}
$$
这是原 N/Y 的共同已付范数界，不作任何 MP 小扰动。

令 $e=L_mw=(L_m-T)w$，并按原从 $x$ 起的真实远孔数写
$w_j=P_{\mathcal N_{\ge x}=j}w$、$e_j=P_{\mathcal N_{\ge x}=j}e$。
原行方程为
$$
Cw_j+D_xw_{j+1}=e_j .
$$
因为头、尾算子交换，完整迭代准确给
$$
\boxed{
C^jg_m=(-D_x)^jw_j+
\sum_{k=0}^{j-1}(-D_x)^kC^{j-1-k}e_k,\qquad j\ge1,
}
\tag{7.2}
$$
输出远真空仍按原等距识别。不假设 $w$ 有有限孔支撑。

用原 $\|C\|\le7$、$\|D_x\|\le1/x$，有
$$
\left\|C^jg_m-(-D_x)^jw_j\right\|
\le2\,7^{j-1}\|T-L_m\|\,\|w\|.
\tag{7.3}
$$
实际 $\nu_j$ 可由前 $j$ 个远位的一个真实集合直接下界：
$$
e_j(x)\ge\prod_{i=x}^{x+j-1}(i+1)^{-4}
\ge(x+j)^{-4j},\qquad
\nu_j\ge\frac{j!}{(x+j)^{2j}}.
\tag{7.4}
$$
在 (5.1) 中 $x\le2d$、$j<h=2d$。由 $\omega_j\le1$，
将 (7.3) 同时除以全部 $\nu_j$ 后得到
$$
\begin{aligned}
&\left(\sum_{j=1}^{h-1}
\left\|
\frac{\omega_j C^jg_m}{\nu_j}
-(-1)^j\omega_j\beta_{x,j}w
\right\|^2\right)^{1/2}\\
&\quad\le208\sqrt{2d}\,7^{2d}(4d)^{4d}
e^{-(385/8)d^4}\|w\|
\le e^{-47d^4}\|w\|.
\end{aligned}
\tag{7.5}
$$
最后一步可直接核：对 $d\ge1024$，
$\log(4d)\le d/2$、
$\log208+\tfrac12\log(2d)\le d$，
所以前因子的对数至多 $2d^2+5d\le d^3\le d^4$，
而 $385/8-1=377/8>47$。
因此完整高度的归一化没有吞掉原 carry 余量。

定义未经重新最小化的实际头矩能量
$$
\mathcal E_m^\omega(w)=
\sum_{j=1}^{h_m-1}
\frac{\omega_{x_m,j}^2\|C_m^jP_{x_m}w\|^2}{\nu_{x_m,j}^2}.
$$
对同一个 $w$，将 (7.5) 放入新的整个移动行 (1.4)，在跨 $m$ 的 Hilbert 直和中用一次三角不等式，得到
$$
\boxed{
\left(\sum_{m\ge10}\mathcal E_m^\omega(w)\right)^{1/2}
\le\left(
\sqrt{\mathcal B_{3/2}}+
\sqrt{\sum_{m\ge10}e^{-94(2^m)^4}}
\right)\|w\|,
\qquad w\in M.
}
\tag{7.6}
$$
这是真正对 $P_xw$ 本身的全部幂矩，而非先过一个 inverse 后的能量。

由 (4.1)，任取同一合法 $s_m\ge8S_{x_m}$，
$$
\boxed{
\sum_{m\ge10}\sum_{j=1}^{h_m-1}
\frac{\|C_m^jP_{x_m}w\|^2}{j!s_m^j}
\le\sum_{m\ge10}\mathcal E_m^\omega(w)<\infty.
}
\tag{7.7}
$$
并且对原完整最小者 $a_m=H_{C_m}(s_m)^{-1}P_{x_m}w$，
正算子不等式 $I-H^{-1}\preceq H-I$ 使其
$\|P_{x_m}w-a_m\|^2+\sum_{j\ge1}E_{m,j}(s_m)$
也受同一个右端控制。因此 (4.3) 的这个小强段结论还扩至所有 $w\in M$，
无需将 $M$ 和 $W$ 混同。

本节没有将零行固定为 $P_xw$ 的物理列免费赋予原 $P_V/P_K/u$ forcing。
若需要该准确身份，仍用前文原完整 inverse $a_m$ 和相应物理代表。
完整幂矩、一次小残量与稳定范围中的真正核仍是不同接口。
