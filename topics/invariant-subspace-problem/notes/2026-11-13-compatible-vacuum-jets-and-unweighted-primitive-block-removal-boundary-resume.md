# 相容真空 jets 与真实最小修复中一个坏原始块的无权消去

日期：2026-11-13（UTC）。作者：boundary_resume / Astra-ISP-0c。状态：以下真空原像和原始块小修复已证明；完整补空间的最小能量及原无权 $N=M$ 仍开放。

本稿使用[局部最小能量与真实投影约束](../results/R239-appendix-local-minimal-energy-lower-bound-and-true-projection-constraints.md)中的相邻配对纯核/共纯核。新的结论是：那一块在全低输出空间会产生真正的 $\log^{4/3}$ 坏能量，但对任意真实 $w\in M$，其实际残量分量可用范数趋零的合法高尾修复消去；不需要对 $w$ 的 Hilbert 尾另加正则性。

## 1. 后尾真空的渐近最优相容原像

设
$$
D_J=\sum_{j\ge J}a_jE_j,\qquad
a_j=(j+1)^{-2},\qquad S_J=\sum_{j\ge J}a_j^2.
$$
给定整数 $d\ge1$，假设 $J^{3/4}\ge2d$。令
$$
\varepsilon=J^{-1/4},\qquad n_0=J,\quad
L_i=\lceil\varepsilon n_i\rceil,\quad n_{i+1}=n_i+L_i,
\quad I_i=[n_i,n_{i+1}-1].
$$
这些有限块分割整个后尾，且 $L_i\ge J^{3/4}$。

在第 $i$ 块上写
$$
D_i=\sum_{j\in I_i}a_jE_j,\quad
C_i=\sum_{j\in I_i}a_j^{-1}E_j^*,\quad
U_i=\sum_{j\in I_i}a_j^{-2},\quad
\sigma_i=\frac{L_i^2}{U_i}.
$$
记下降阶乘 $(L)_t=L(L-1)\cdots(L-t+1)$。定义
$$
b_{i,0}=\Omega_i,\qquad
b_{i,t}=\frac{C_i^t\Omega_i}{t!(L_i)_t}
\quad(1\le t\le d).
\tag{1.1}
$$
有限块的准确关系
$[D_i,C_i]=L_i-2\mathcal N_i$ 给
$$
D_iC_i^t\Omega_i
=t(L_i-t+1)C_i^{t-1}\Omega_i,
$$
故
$$
\boxed{D_ib_{i,t}=b_{i,t-1}.}
\tag{1.2}
$$

同时
$$
\|b_{i,t}\|^2
=\frac{e_t((a_j^{-2})_{j\in I_i})}{(L_i)_t^2}
\le
\frac1{t!\sigma_i^t}
\left(\frac{L_i^t}{(L_i)_t}\right)^2.
$$
因 $t\le d\le L_i/2$，
$$
2\log\frac{L_i^t}{(L_i)_t}
=2\sum_{k<t}-\log(1-k/L_i)
\le\frac{2t(t-1)}{L_i}.
$$
所以
$$
\|b_{i,t}\|^2
\le\frac{\exp(2t(t-1)/L_i)}{t!\sigma_i^t}.
\tag{1.3}
$$

块内系数比满足
$a_{\max}/a_{\min}\le(1+\varepsilon)^2$。若
$S_i=\sum_{j\in I_i}a_j^2$，Cauchy--Schwarz 与最大/最小值比较分别给
$$
(1+\varepsilon)^{-4}S_i\le\sigma_i\le S_i.
$$
置
$$
\sigma=\sum_i\sigma_i,\qquad p_i=\sigma_i/\sigma.
$$
则 $\sum_ip_i=1$，并有
$$
(1+\varepsilon)^{-4}S_J\le\sigma\le S_J.
\tag{1.4}
$$

对 $0\le t\le d$，在无限张量尾空间定义
$$
b_t=
\sum_{\substack{(t_i)\ {\rm 有限支撑}\\t_i\ge0,\ \sum_i t_i=t}}
 \bigotimes_i p_i^{t_i}b_{i,t_i}.
\tag{1.5}
$$
不同多重指标的各块孔次数不同，因此求和项互相正交。
由 (1.3)，总指数损失至多
$2\sum_it_i(t_i-1)/L_i\le2d^2/J^{3/4}$。
多项式展开给准确标量求和
$$
\sum_{\sum t_i=t}
 \prod_i\frac{p_i^{2t_i}}{t_i!\sigma_i^{t_i}}
=
\frac1{t!}\left(\sum_i\frac{p_i^2}{\sigma_i}\right)^t
=\frac1{t!\sigma^t}.
$$
这既证明 (1.5) 在 Hilbert 范数下收敛，也给
$$
\boxed{
\|b_t\|^2\le
\frac{K_{J,d}}{t!\,S_J^t},
\quad
K_{J,d}:=
\exp\!\left(\frac{2d^2}{J^{3/4}}+
             \frac{8d}{J^{1/4}}\right).
}
\tag{1.6}
$$
这里用了 (1.4) 及 $4d\log(1+\varepsilon)\le8d\varepsilon$。

每项严格有 $t$ 个后尾孔。由 (1.2)，对固定目标多重指标，删除一孔的全部来源系数相加恰为 $\sum_ip_i=1$。先截有限块，再用上述范数收敛及 $D_J$ 有界取极限，得到
$$
\boxed{
b_0=\Omega,\qquad D_Jb_t=b_{t-1}\quad(1\le t\le d).
}
\tag{1.7}
$$
特别 $D_J^tb_t=\Omega$。反过来，任何满足这个等式的 $t$ 孔原像都由 Cauchy--Schwarz 满足
$$
\|b_t\|^2\ge
\|(D_J^*)^t\Omega\|^{-2}
\ge\frac1{t!S_J^t}.
\tag{1.8}
$$
所以 (1.6) 不仅保留阶乘，而且整个同一相容族在
$d^2/J^{3/4}+d/J^{1/4}\to0$ 时同时渐近达到这个真空能量下界。

## 2. 配对原始块的准确斜投影

回到原全整数选择 $m=m(q)$、$d=2^m$、$J=m+2q$。
在前缀 $I=[m,J-1]$ 上取原稿的单位向量 $h=h_{m,q}$、$g=g_{m,q}$；
这里先不附加后尾真空。它们严格有 $q$ 孔，且
$$
D_Ih=0,\qquad D_I^*g=0,\qquad
\rho=\langle h,g\rangle\ge e^{-2/(m+1)}.
$$
定义前缀斜投影并在原头与后尾张量恒等：
$$
\boxed{\Pi=\rho^{-1}|h\rangle\langle g|.}
\tag{2.1}
$$
有
$$
\Pi^2=\Pi,\qquad \|\Pi\|=\rho^{-1}\longrightarrow1,
$$
$$
D_I\Pi=\Pi D_I=0,\qquad
[D_m,\Pi]=[A_m,\Pi]=[L_m,\Pi]=0.
\tag{2.2}
$$
注意完整 $D_m\Pi$ 一般并非零；(2.2) 的零等式只对前缀
$D_I$ 成立。完整后尾删除仍作用于 $\Pi$ 的像。

$\Pi$ 保持尾孔次数。若 $v\in\mathscr V_{m,q}$，它在 $q$ 以下各层均被 $\Pi$ 杀掉，并且
$$
\Pi v=\frac{x_g(v)}{\rho}\otimes h\otimes\Omega_J,
\quad
x_g(v)=(I_{\rm head}\otimes
 \langle g\otimes\Omega_J,\cdot\rangle)v_q.
\tag{2.3}
$$
因此 $\Pi v$ 仍在同一低输出精确核，且对 $r=A_mv_q$，
$$
r^\Pi:=\Pi r
=A_mx_g(v)/\rho\otimes h\otimes\Omega_J.
\tag{2.4}
$$

## 3. 这一块的真正有限和无限最小能量

先对任意原头向量 $x$ 取 $v=x\otimes h\otimes\Omega_J$，
并记
$$
Q_{A,J}(x)=
\sum_{t=1}^{d}
 \frac{\|A_m^t x\|^2}{t!S_J^t}.
$$
原配对观测对任意有限宽度或无限高尾可行修复给
$$
\lambda^{[\infty]}(v)^2\ge\rho^2Q_{A,J}(x).
\tag{3.1}
$$

用 §1 的同一相容族定义
$$
c_t=(-1)^{t-1}A_m^t x\otimes h\otimes b_t,
\qquad c=\sum_{t=1}^{d}c_t.
\tag{3.2}
$$
由 $D_Ih=0$、(1.7) 及 $A_m^d=0$，
$$
D_mc_1=A_mx\otimes h,\qquad
D_mc_{t+1}=-A_mc_t,\qquad A_mc_d=0.
$$
所以 $L_mc=A_mv$。它严格支持尾孔 $q+1,\ldots,q+d$；
$D_m^dc=0$ 也准确成立，因为 $b_t$ 只有 $t$ 孔，且 $t=d$ 项本来为零。
各 $c_t$ 互相正交，故 (1.6) 给
$$
\|c\|^2\le K_{J,d}Q_{A,J}(x).
$$
于是
$$
\boxed{
\rho^2Q_{A,J}(x)
\le\lambda^{[\infty]}(v)^2
\le\lambda^{[d]}(v)^2
\le K_{J,d}Q_{A,J}(x).
}
\tag{3.3}
$$
对于原自适应 $d=O((\log q)^{1/3})$、$J=m+2q$，
有 $K_{J,d}\to1$ 且 $\rho\to1$。
因此 (3.3) 是对全部头向量 $x$ 统一的渐近精确二次型，而非某个候选右逆的单侧粗界。零二次型时两边都准确为零。

## 4. 任意真实核的这一块有无权小修复

现取任意 $w\in M=\ker T$，$v=v_{m,q}(w)$。
原真实相容性已付清
$$
Z_t(v):=\frac{\|A_m^t x_g(v)\|}{\sqrt{t!}S_J^{t/2}}
\le\|P_{q+t}^{(m)}w\|
 +e^{-72d^4}\|w\|
\qquad(1\le t\le d).
\tag{4.1}
$$
其中归一化小分母已经支付，未把 $\eta$ 小直接当作小原像。

对 (2.4) 取 (3.2) 中 $x=x_g(v)/\rho$，记所得合法修复为
$c^\Pi$。由 (1.6) 和有限序列 Minkowski 不等式，
$$
\boxed{
\begin{aligned}
\|c^\Pi\|
&\le \frac{\sqrt{K_{J,d}}}{\rho}
 \left(\sum_{t=1}^d Z_t(v)^2\right)^{1/2}\\
&\le\frac{\sqrt{K_{J,d}}}{\rho}
 \left[
 \|P_{[q+1,q+d]}^{(m)}w\|
 +\sqrt d\,e^{-72d^4}\|w\|
 \right].
\end{aligned}
}
\tag{4.2}
$$
尾孔超过 $q$ 必使原总孔超过 $q$，故该上界至多为
$$
(1+o(1))
 \left[\tau_q(w)+\sqrt d\,e^{-72d^4}\|w\|\right]
\longrightarrow0.
\tag{4.3}
$$
这一结论对每个真实 Hilbert 核向量成立，不要求任何指定尾衰减速度。

这里没有声称 $\Pi$ 保持真实 $\ker T$。它与混合 $L_m$ 交换；
真实 $T$ 的误差全部通过 (4.1) 进入 (4.2)。

## 5. 可以从原最小能量中删去这个分量

令 $\lambda_q^\Pi(w)$ 为同一合法窗口内源 $r^\Pi$ 的最小修复范数，
令 $\lambda_q^{\rm rem}(w)$ 为源 $(I-\Pi)r$ 的最小修复范数。
由于 $\Pi v$ 和 $(I-\Pi)v$ 都是同一低方程核向量，二者的
$D^d$ 约束均由已证链身份自动满足。

原 Gram 表示的最小解算子是线性的：
$F^*\mathsf G^{-1}r$。因此
$$
\boxed{
|\lambda_q(w)-\lambda_q^{\rm rem}(w)|
\le\lambda_q^\Pi(w)
\le\|c^\Pi\|\longrightarrow0.
}
\tag{5.1}
$$
这使用一个明确可行的小修复及最小解线性性，不是把某个
Gram 非对角块直接删除，也没有遗漏 Schur 补。

对 $\Pi$ 源本身，(3.3) 更准确给
$$
\sum_{t=1}^d Z_t(v)^2
\le(\lambda_q^\Pi(w))^2
\le\frac{K_{J,d}}{\rho^2}\sum_{t=1}^d Z_t(v)^2.
\tag{5.2}
$$
因此这部分真正最小能量已被实际未来尾控制，任何慢 Hilbert 尾都不构成障碍。

## 6. 推广到任意受控的中间原始投影

上述机制不要求前缀像只有一维。设 $P$ 是前缀
$I=[m,m+2q-1]$ 上的有界投影，满足
$$
\operatorname{Ran}P\subseteq\mathcal H_q(I),\qquad
P=P\,P_q(I),\qquad D_IP=P D_I=0.
\tag{6.1}
$$
在原头和后尾张量恒等。则 $P$ 与 $L_m$ 交换，而 $Pv$ 的后尾仍是真空。
§3 的同一 $b_t$ 可作用于向量值的 $Pv$，得到 $Pr$ 的合法修复。

对原真实恒等式
$A^t-(-D)^t=\sum_{j<t}A^{t-1-j}(-D)^jL$
作用于 $w$ 后再施加 $P$。由于 $P D_I=0$，删除幂只剩
$P D_J^t$；在所选总层上其后尾源恰有 $t$ 孔，范数至多
$\|P\|\sqrt{t!}S_J^{t/2}$。按 (4.1) 相同预算，得到
$$
\boxed{
\lambda_q^{P}(w)
\le
\sqrt{K_{J,d}}\,\|P\|
 \left[
 \|P_{[q+1,q+d]}^{(m)}w\|
 +\sqrt d\,e^{-72d^4}\|w\|
 \right].
}
\tag{6.2}
$$
故任何范数一致有界的这类前缀原始投影族，都可对任意真实核消去其残量分量，而不增加尾正则假设。

当前仍未证明这些受控原始块组成覆盖全部实际 $D^d$ 残量的稳定分解。匹配块、一般原始向量之间的框架常数，以及其余纯删除链，都必须另付；不能从单块或 (6.2) 直接跳到完整 $\lambda_q(w)$ 的控制。
