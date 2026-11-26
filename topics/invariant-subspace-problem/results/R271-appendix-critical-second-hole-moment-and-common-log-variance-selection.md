# R271 附录：同一真实残量的二阶物理孔矩与公共对数方差选择

日期：2026-11-26（UTC）。

作者：Astra-ISP-347c-20261126 / r271_source；AI-assisted，GPT-6 Astra Pro。

**状态：以下沿公共方差选择的二阶物理孔矩及其带对数方差积分已证明。**
本稿始终使用原完整 $T_N$ 或 $T_Y$、原 forcing $f_1=e_1$，
以及原未加权 $J=1$ Gram inverse
$$
a_s=(I+T^*T/s)^{-1}f_1,\qquad h_s=Ta_s,\qquad 0<s\le1.
\tag{0.1}
$$
没有更换 forcing、核、最小化度量或物理孔数。
这里的结论是：可在每个趋零的对数方差窗内选一个共同 $s$，
使 $\|\mathcal N^2h_s\|\to0$。它不是全 $s\downarrow0$ 的二阶极限，
也不是完整 $J=\infty$ 或真 $F_0$ 的残量定理。

依赖：

- [原次数缺陷与同一残量的一阶矩](R271-appendix-actual-number-defect-and-uniform-first-moment-of-the-same-residual.md)，尤其原模型、自然域和谱积分；
- [位置权与近二阶物理残量矩](R271-appendix-position-number-pullthrough-and-nearly-quadratic-physical-residual-moments.md) §6，尤其完整 carry/Cayley 的截权相对形式；
- [指数远孔起点的相对全算子 Gram](R271-appendix-exponential-weight-cutoff-relative-global-gram-and-actual-weighted-residual.md) (1.1)、(3.1)、(4.5)、(6.1) 及 §7 的母窗。只用其中任意 $y\ge m+d$ 的相对有限列估计，不用旧 $y=m+d$ 的裸 Gram 比较。

## 1. 原残量的谱归一化

令 $M=\ker T$、$H=T^*T$，并记
$$
\epsilon(s)=\frac{\|h_s\|}{\sqrt s}.
$$
原 $T f_1=\Omega$、$T\Omega=0$、$\|f_1\|=1$。由 $H$ 的谱演算，
$$
\|a_s\|\le1,\qquad
\|h_s\|\le\frac{\sqrt s}{2},\qquad
\epsilon(s)\longrightarrow0,
\tag{1.1}
$$
且
$$
\boxed{
\int_0^\infty \frac{\|h_s\|^2}{s^2}\,ds
=\|(I-P_M)f_1\|^2\le1.
}
\tag{1.2}
$$
确实，$a_s=s(H+s)^{-1}f_1$，故左端的标量乘子为
$\int_0^\infty \lambda(\lambda+s)^{-2}\,ds=1$，适用于 $\lambda>0$，
在 $\lambda=0$ 为零。Tonelli 直接给 (1.2)。
同样，
$s\lambda/(\lambda+s)^2\le1/4$ 且逐点趋零，给 (1.1) 的最后一式。

对每个原 $w\in M$，准确保留
$$
\langle w,a_s\rangle=\langle w,f_1\rangle.
\tag{1.3}
$$

## 2. 一个位置信息随截点变化的原正能量估计

对整数 $y\ge1$ 定义
$$
\omega_i^{(y)}=
\begin{cases}
(i+1)^3,&0\le i<y,\\
1,&i\ge y,
\end{cases}
\qquad
\mathcal W_y=\sum_{i\ge0}\omega_i^{(y)}n_i,
\tag{2.1}
$$
其中 $n_i$ 是原物理第 $i$ 位的占据投影。
不要求这组权在 $i=y$ 单调；位置形式定理只要求逐位
$1\le\omega_i\le(i+1)^3$ 及其实际系数平方和。

写原系数 $a_i=(i+1)^{-2}$，$\eta=e^{-1070}$。位置形式定理给
$$
\mathcal B_y:=T+[\mathcal W_y,T]=D_y+K_y,
\qquad
D_y=\sum_i a_i(1-\omega_i^{(y)})E_i,
$$
$$
\|K_y\|\le2048\eta,\qquad
\|D_yv\|\le\sigma_y\|\mathcal W_y^{1/2}v\|,
\tag{2.2}
$$
其中
$$
\sigma_y^2
=\sum_i a_i^2\frac{(\omega_i^{(y)}-1)^2}{\omega_i^{(y)}}
\le\sum_{i=0}^{y-1}\frac1{i+1}
\le1+\log y.
\tag{2.3}
$$
(2.2) 的 $K_y$ 保留原全部 carry；对于 Y 模型也保留完整
$\mathsf N_i^2(I+\mathsf N_i)^{-2}$ 与两个 resolvent 差项。
由于 $T\Omega=D_y\Omega=0$，准确有 $K_y\Omega=0$。
而 $\mathcal W_y\ge I-P_\Omega$，所以
$$
\boxed{
\|\mathcal B_yv\|
\le C_y\|\mathcal W_y^{1/2}v\|,
\qquad
C_y:=\sigma_y+2048\eta
\le2\sqrt{1+\log y}.
}
\tag{2.4}
$$
最后用 $2048e^{-1070}<1$。

每个固定 $y$ 的权有界，且 $[\mathcal W_y,T]$ 有界；
旧自然域证明因此给 $a_s\in\operatorname{Dom}\mathcal W_y$，
$h_s\in\operatorname{Dom}\mathcal W_y$。
这里可以直接在实际域上配对，不对未截断的立方位置权施加伴随。

原正规方程为
$$
(T^*T+s)a_s=sf_1.
$$
将其与 $\mathcal W_y a_s$ 配对并取实部。
由
$$
T\mathcal W_y a_s
=(\mathcal W_y+1)h_s-\mathcal B_y a_s
$$
以及 $\|\mathcal W_y^{1/2}f_1\|=1$，若记
$$
X=\|\mathcal W_y^{1/2}a_s\|,
\qquad
Y=\|(\mathcal W_y+1)^{1/2}h_s\|,
$$
则
$$
sX^2+Y^2
=s\,\operatorname{Re}
\langle\mathcal W_y^{1/2}f_1,\mathcal W_y^{1/2}a_s\rangle
+\operatorname{Re}\langle h_s,\mathcal B_ya_s\rangle
\le(s+C_y\|h_s\|)X.
\tag{2.5}
$$
对右端减去 $sX^2$ 完成平方，得到新的直接估计
$$
\boxed{
\|(\mathcal W_y+1)^{1/2}h_s\|
\le\frac{\sqrt s+C_y\epsilon(s)}2.
}
\tag{2.6}
$$
不需要假设 $\mathcal W_y$ 与 $T$、$H$ 或其逆交换。

## 3. 原指数孔权和全部比较参数

固定
$$
K=2^{40},\qquad
y=y_s=\lceil K/s\rceil,\qquad
m=4\left\lfloor\frac{\log_2y}{8}\right\rfloor,
\qquad d=2^m,\qquad n=d/2.
\tag{3.1}
$$
于是
$$
m\in4\mathbb N,\quad m\ge20,\qquad
\frac{\sqrt y}{16}<d\le\sqrt y,\qquad
m+d\le y.
\tag{3.2}
$$
此外
$$
\frac K y\le s\le\frac{K+1}y\le\frac{2K}y.
\tag{3.3}
$$
特别，$y$ 是相对 Gram 定理允许的任意较远孔起点；
这里绝未将旧起点 $m+d$ 误写成 $y_s$。

由 $n^3>y^{3/2}/32768$、$y\ge2^{40}$，
$$
12n^3>384y>\log(y+1).
$$
所以同时满足
$$
y<e^{12n^3}\le e^{12d^3}.
\tag{3.4}
$$
有限列 $J=1$ 的精确条件也成立：
$$
1/s\le y/K\le y<e^{12d^3}
<\mathscr R_m^2=e^{417d^3/4}.
\tag{3.5}
$$

现在使用相对 Gram 定理的原定义
$$
\boxed{\Gamma_y=32^{\mathcal N_{\ge y}}.}
\tag{3.6}
$$
它不是 $32^{\mathcal N_{\ge y}/2}$。
原有限列定理 (4.5) 在 $J=1$ 给
$$
\|\widehat\Gamma_y\mathcal R_{T,1}
H_{T,1}^{-1}\Gamma_y^{-1}\|\le9/8.
$$
由于 $\Gamma_yf_1=f_1$，取其真实第一个正高度分量，
$$
\boxed{\|\Gamma_yh_s\|\le\frac98\sqrt s.}
\tag{3.7}
$$
这里仅使用正向孔权及其闭自然域结论。
不存在把两向共轭中的另一方向当成 $\Gamma_yh_s$ 的步骤。

这些比较参数也能放入原高度与支持母窗。
例如令 $h=d+y-m$，取 $J_{\rm flag}$ 为不小于 $h+y-1$ 的最小偶数，
令 $r=J_{\rm flag}+1$，再取
$$
R=576(m+1)^2y^2,\qquad x=m+R,\qquad Q=R+r.
\tag{3.8}
$$
则 $r$ 为奇数、$r\le3y$、$R$ 为偶数，并且
$$
r\le1+\left\lfloor\frac{\sqrt{x+1}}{8(m+1)}\right\rfloor,
\qquad
Q\le600(m+1)^2y^2.
\tag{3.9}
$$
由 $m+1\le\sqrt y$ 和上述 $n^3$ 下界，
$$
\log(4Q)\le\log2400+3\log y<4y<26n^3.
$$
故 $Q<e^{26n^3}/4$，也有 $x+1\le Q<e^{26n^3}/4$。
最高 carry 置零、把基头改为 $m-1$ 后，
强长度变为 $R+1$，所需母支持准确为
$Q\ge(R+1)+(r-1)=R+r$，已由 (3.8) 支付。

(3.8) 仅核对相容母窗；本稿的 $a_s$ 始终是 (0.1) 的 $J=1$ 原全算子源。
没有把它改成 $J_{\rm flag}$ 的压缩源或宣称它本身具有有限 $Q$ 的准确物理代表。
原物理运输及同 $u$ 身份仍按其各自已证公式和同一个 forcing 使用。

## 4. 真正二阶总物理孔矩

记
$$
A_y=\mathcal N_{<y},\qquad B_y=\mathcal N_{\ge y},
\qquad \mathcal N=A_y+B_y.
$$
若某物理基向量在前 $y$ 位有 $a$ 个孔，则
$$
\mathcal W_y
\ge\sum_{j=1}^a j^3
=\frac{a^2(a+1)^2}{4}
\ge\frac{a^4}{4}.
$$
这些都是同一物理孔基上的非负对角量。因此由 (2.6)，
$$
\|A_y^2h_s\|
\le2\|\mathcal W_y^{1/2}h_s\|
\le\sqrt s+C_y\epsilon(s).
\tag{4.1}
$$

对于整数 $b\ge1$，有
$$
b^2\le32^{b-1}.
$$
在 $b=1$ 取等；相邻项 $b^2/32^b$ 的比值不超过 $4/32=1/8$。
$b=0$ 时左端为零。因此 (3.7) 给
$$
\|B_y^2h_s\|
\le\frac1{32}\|\Gamma_yh_s\|
\le\frac9{256}\sqrt s.
\tag{4.2}
$$
它也直接证明所用无限远孔二阶自然域。

由于 $(a+b)^2\le2a^2+2b^2$，结合 (4.1)--(4.2)，得到
$$
\boxed{
h_s\in\operatorname{Dom}\mathcal N^2,\qquad
\|\mathcal N^2h_s\|
\le3\sqrt s+
4\sqrt{L_s}\,\epsilon(s),
\quad
L_s:=1+\log\frac{K+1}{s}.
}
\tag{4.3}
$$
这里 $1+\log y_s\le L_s$，而 $2+9/128<3$。
这是原同一个残量的点态界；右端保留实际谱量 $\epsilon(s)$，
没有给它填入未经证明的移动参数速率。

## 5. 方差积分及每窗的一个公共选择

由 $(u+v)^2\le2u^2+2v^2$，(4.3) 给
$$
\|\mathcal N^2h_s\|^2
\le18s+32L_s\frac{\|h_s\|^2}{s}.
\tag{5.1}
$$
用 (1.2) 积分，
$$
\boxed{
\int_0^1
\frac{\|\mathcal N^2h_s\|^2}{sL_s}\,ds
\le50.
}
\tag{5.2}
$$
更准确的右端是
$18/[1+\log(K+1)]+32\|(I-P_M)f_1\|^2$。
所有被积函数都可先以有限物理孔截断表示，再作单调极限；
(5.2) 不要求预先知道 $\mathcal N^2h_s$ 的图范数连续性。

令
$$
L\ge L_0:=1+\log(K+1),\qquad
I_L=\int_{e^{-2L}}^{e^{-L}}\frac{\|h_s\|^2}{s^2}\,ds.
\tag{5.3}
$$
由 (1.2)，$I_L\to0$。
在 $s=e^{-\ell}$、$L\le\ell\le2L$ 上，$L_s=L_0+\ell\le3L$。
对 (5.1) 作普通 $\ell$ 平均，所以至少有一个
$$
s_L\in[e^{-2L},e^{-L}]
$$
满足
$$
\boxed{
\|\mathcal N^2h_{s_L}\|^2
\le\frac{18e^{-L}}{L}+96 I_L
\longrightarrow0.
}
\tag{5.4}
$$
同一个 $s_L$ 还保 (1.1)、(1.3) 及 (4.3) 的全部原参数。
因任意物理前缀的孔数平方都不超过 $\mathcal N^2$，
这一次选择同时控制所有前缀孔矩，不需要为每个前缀重新选方差。

## 6. 范围

(5.4) 将此前全 $p<2$ 的真实物理矩，
补到可在每个对数方差窗内共同选择的二阶端点。
原 $a_{s_L}\to P_Mf_1$ 仍按未加权强收敛成立；
$f_1$ 与每个原 $w\in M$ 的配对没有改变。

本稿没有证明 $\|\mathcal N^2h_s\|\to0$ 对全部 $s\downarrow0$ 成立：
(1.2) 本身不蕴含 $L_s\epsilon(s)^2\to0$。
也没有把二阶矩改成指数孔权清除预算，
没有给修正后真核向量的孔正则性，
没有支付 $S_x$ 处原真 $F_0$ 的绝对 $\mathcal Z_\gamma$、
全物理 MP 返回或完整帽费用。
普通 Hilbert ISP 和 $N=M$ 仍保持未决。
