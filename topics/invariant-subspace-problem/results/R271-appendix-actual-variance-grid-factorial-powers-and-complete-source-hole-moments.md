# R271 附录：原全算子阶乘幂、实际方差网格与完整源的物理孔矩

日期：2026-11-26（UTC）。

作者：Astra-ISP-347c-20261126 / r271_source；AI-assisted，GPT-6 Astra Pro。

**状态：以下原边界 $T_N/T_Y$ 阶乘幂预算、实际离散方差的辅助能量可和性及完整源的物理孔矩选择已证明。**
本稿把完整 Gram 源的连续方差选择，落到真正
$$
S_x=\sum_{i\ge x}(i+1)^{-4}
$$
的离散网格。所有源仍由同一个 $f_1=e_1$ 和同一个原全算子 $T$ 定义。
不将此完整空间结果改称真 $F_0$ 的压缩源结果。

依赖：

- [完整 Gram 的位置能量与二阶物理孔矩](R271-appendix-complete-gram-position-energy-and-common-second-hole-moment.md)，尤其原全源、$\mu_T$、完整 $T/L$ 比较和低头项；
- [指数远孔相对全 Gram](R271-appendix-exponential-weight-cutoff-relative-global-gram-and-actual-weighted-residual.md)，尤其有限/无限列的原 inverse、两向闭域及母支持；
- [原次数缺陷](R271-appendix-actual-number-defect-and-uniform-first-moment-of-the-same-residual.md) 中的原边界 $\mathsf N_i,\mathsf Y_i$ 身份；
- [R236 分阶阶乘幂预算](R236-appendix-factorial-cumulant-powers-and-joint-resolvent-budgets.md) §§3--6 提供头尾指数估计的机制。下面对本稿的边界算子重新给出直接证明，不把 Haar 模型的结论自动运输到此处。

## 1. 原边界基移位的完整四次幂界

原
$$
\mathsf N_i^2=\eta_i\mathsf N_{i+1},\qquad
\|\mathsf N_i\|=1,
$$
$$
-\log\eta_i=1400\,16^i-630\,8^i+300\,2^i
$$
给
$$
1070\,16^i\le-\log\eta_i\le1700\,16^i.
\tag{1.1}
$$
下界在 $i=0$ 为等式；$i\ge1$ 时除以 $16^i$ 后仅前两项就至少为 $1085$。

令 $B=\mathsf N_0$，$c_0=1$，$c_{i+1}=c_i^2\eta_i$。
原平方关系逐次给
$$
B^{2^i}=c_i\mathsf N_i,\qquad
-\log c_i
=\sum_{j<i}2^{i-1-j}(-\log\eta_j)
<122\,16^i.
\tag{1.2}
$$
所有 $\mathsf N_i$ 因此仍是同一个实际 $B$ 的多项式。

若整数 $r\ge2$、$2^k\le r<2^{k+1}$，
则 $\|B^r\|\le c_k\le\eta_{k-1}$。
因为 $16^{k-1}>r^4/256$，得到
$$
\|B^r\|\le e^{-1070r^4/256}.
$$
连同 $r=0,1$，保守写成完整界
$$
\boxed{\|B^r\|\le e\,e^{-r^4}\quad(r\ge0).}
\tag{1.3}
$$
这里没有把二进位的真实幂范数换成一个错误的精确平滑式。

## 2. 原 N/Y 的实际正主控与阶乘幂

令 $a_i=(i+1)^{-2}$。在原物理孔基的逐坐标非负锥上，
$\mathsf N_i$ 是正算子。定义
$$
M_N=\sum_i a_i\mathsf N_i,\qquad
M_Y=\sum_i a_i\mathsf N_i(I-\mathsf N_i)^{-1}.
\tag{2.1}
$$
原
$$
\mathsf Y_i=\mathsf N_i(I+\mathsf N_i)^{-1}
$$
的完整绝对范数收敛展开给
$$
|T_Yv|\le M_Y|v|,\qquad
|T_Y^jv|\le M_Y^j|v|.
\tag{2.2}
$$
这里的正性是坐标锥正性，不是自伴正性。
原平方关系给
$$
\|(I-\mathsf N_i)^{-1}\|
\le\frac{2}{1-\eta_i}<3,
$$
故 (2.1) 的和按算子范数收敛。N 模型直接用 $M_N=T_N$。

以下统一写 $M=\sum_i a_i F(\mathsf N_i)$，
其中 $F(z)=z$ 或 $z/(1-z)$。
实际平方关系和偶奇幂分开给
$$
\|e^{z\mathsf N_i}\|
\le(1+|z|)e^{|z|\sqrt{\eta_i}}.
$$
又
$F(\mathsf N_i)=\mathsf N_i+E_i'$、$\|E_i'\|\le3\eta_i$，
且两个加数交换。因此对 $t=|z|$，
$$
\|e^{za_iF(\mathsf N_i)}\|
\le(1+ta_i)\exp(4ta_i\sqrt{\eta_i}).
\tag{2.3}
$$

取最小整数 $h\ge1$ 使
$$
535\,16^h\ge2\log(2+t).
$$
原高尾仍保全部 carry，由 (2.3) 得
$$
\|e^{zM_{\ge h}}\|
\le \prod_{i\ge h}(1+ta_i)
\exp\!\left(4t\sum_{i\ge h}a_i\sqrt{\eta_i}\right)
\le e\,e^{4\sqrt t}.
\tag{2.4}
$$
这里
$\sum_{i\ge h}a_i\sqrt{\eta_i}\le2(2+t)^{-2}$，
而单调积分给
$\sum_{j\ge1}\log(1+t/j^2)\le\pi\sqrt t<4\sqrt t$。

原低头有准确因子
$$
M_{<h}=B U_h,\qquad
\|U_h\|\le6e^{122\,16^{h-1}},
\tag{2.5}
$$
且 $B,U_h$ 交换。由 $h$ 的最小性，
$$
\ell:=\log(2+t\|U_h\|)
\le126+2\log(2+t).
$$
(1.3) 与
$-r^4+r\ell\le-r^4/2+\ell^{4/3}$ 给
$$
\|e^{zM_{<h}}\|
\le2e\,e^{\ell^{4/3}}.
\tag{2.6}
$$
两个真实头尾部分交换，所以可相乘。
例如令
$$
A_0=2^{1/3}126^{4/3},\qquad
B_0=2^{5/3}(8/3)^{4/3},
$$
$$
K_0=2e^{\,2+A_0+\sqrt2 B_0},\qquad
C_0=4+B_0,\qquad D_0=(eC_0/2)^2.
\tag{2.7}
$$
用 $\log u\le(8/3)u^{3/8}$ 可得
$\ell^{4/3}\le A_0+B_0\sqrt2+B_0\sqrt t$，
因此
$$
\|e^{zM}\|\le K_0e^{C_0\sqrt{|z|}}.
$$
对整函数用 Cauchy 系数估计，圆半径取 $(2j/C_0)^2$，
再用 $(j!)^2\le j^{2j}$，得到
$$
\boxed{
\|T_N^j\|,\ \|T_Y^j\|
\le K_0\frac{D_0^j}{j!}
\quad(j\ge0).
}
\tag{2.8}
$$
(2.2) 支付了 Y 的全部 Cayley 项；没有把 Y 换成 N 后省略其余项。

## 3. 同一全源的辅助能量导数

保留原
$$
\mathcal H(s)=\sum_{j\ge0}\frac{(T^*)^jT^j}{j!s^j},
\qquad a(s)=\mathcal H(s)^{-1}f_1,
\qquad k(s)=\mathcal R_{T,\infty}(s)a(s).
$$
记
$$
\mu_\nu(s)=\sum_{j\ge1}
\frac{j^\nu\|T^ja(s)\|^2}{j!s^j}
\quad(\nu=1,2).
$$
前稿已付
$$
\int_0^\infty\mu_1(s)\frac{ds}{s}
=1-\|P_{\ker T}f_1\|^2\le1.
\tag{3.1}
$$

设
$$
G=\mathcal R^*N_{\rm aux}\mathcal R,\qquad
G_2=\mathcal R^*N_{\rm aux}^2\mathcal R.
$$
所有算子均有界，且
$$
G\mathcal H^{-1}G
=\mathcal R^*N_{\rm aux}
P_{\operatorname{Ran}\mathcal R}
N_{\rm aux}\mathcal R
\preceq G_2.
\tag{3.2}
$$
对 $t=\log s$，$\mathcal H'=-G$、$G'=-G_2$、
$a'=\mathcal H^{-1}Ga$。因此准确有
$$
\frac{d\mu_1}{dt}
=-\mu_2+2\|\mathcal H^{-1/2}Ga\|^2,
\qquad
\boxed{\left|\frac{d\mu_1}{d\log s}\right|\le\mu_2.}
\tag{3.3}
$$
这不是将辅助次数等同于物理孔数；它只用于控制实际方差网格的插值。

## 4. 完整辅助尾降到 $O(s^{-1/3})$

由 $\|a(s)\|\le1$ 和 (2.8)，
$$
\frac{\|T^ja(s)\|^2}{j!s^j}
\le K_0^2\frac{(D_0^2/s)^j}{(j!)^3}.
$$
置
$$
\alpha=(e^5D_0^2)^{1/3},\qquad
b=\lceil2\log K_0\rceil+32,\qquad
J(s)=\lceil\alpha s^{-1/3}+b\rceil.
$$
当 $j>J(s)$ 时，由 $j!\ge(j/e)^j$，
右端至多为 $e^{-j}$。
同时 $J(s)\ge32$，故
$$
\sum_{j>J(s)}j^2e^{-j}
\le2(J(s)+2)^2e^{-J(s)}
\le e^{-J(s)/2}.
$$
于是存在这里已经明确的固定常数
$$
C_1=\alpha+b+1,\qquad c_1=\alpha/4>0
$$
使所有 $0<s\le1$ 都满足
$$
\boxed{
\mu_2(s)\le C_1s^{-1/3}\mu_1(s)
+e^{-c_1s^{-1/3}}.
}
\tag{4.1}
$$
这里的正尾误差未被省去。

## 5. 原实际 $S_x$ 网格及正插值误差

对整数 $x\ge1$，
$$
\frac1{3(x+1)^3}\le S_x\le\frac1{3x^3},
\qquad
S_x-S_{x+1}=(x+1)^{-4}.
$$
令
$$
\ell_x=\log(S_x/S_{x+1}).
$$
用 $\log(1+u)\ge u/(1+u)$ 和 $\log(1+u)\le u$，
逐项得到
$$
\boxed{\frac3{16x}\le\ell_x\le\frac{12}{x}.}
\tag{5.1}
$$
在 $S_{x+1}\le s\le S_x$ 上又有
$$
3^{1/3}x\le s^{-1/3}\le5x.
$$
结合 (3.3)、(4.1)，
$$
\left|\frac{d\mu_1}{d\log s}\right|
\le Bx\,\mu_1(s)+e^{-c_1x},
\qquad B=5C_1.
$$
Gronwall 在这个实际网格单元内给
$$
\boxed{
\mu_1(S_x)
\le M_0\big(\mu_1(s)+\ell_xe^{-c_1x}\big),
\qquad M_0=e^{12B}.
}
\tag{5.2}
$$
它包含必须支付的正插值误差。

将 (5.2) 对整个单元积分，并用 (5.1)，
$$
\frac{\mu_1(S_x)}x
\le\frac{16M_0}{3}
\left[
\int_{S_{x+1}}^{S_x}\mu_1(s)\frac{ds}{s}
+\ell_x^2e^{-c_1x}
\right].
$$
所有单元不相交，(3.1) 和 $\sum x^{-2}<2$ 遂给
$$
\boxed{
\sum_{x\ge1}\frac{\mu_1(S_x)}x<\infty.
}
\tag{5.3}
$$
例如上界 $1600M_0$ 足够。
常数虽然保守，但不依赖 $x$，故能合法用于后面的共同选择。

## 6. 物理截点与小比较头的共同母窗

这里的 $x$ 是实际物理远孔起点。
为保 $R=x-m\ge d$，不能使用前稿为了方便而取的
$d\asymp\sqrt{K/s}$。
在 $s=S_x$ 时改取比较参数
$$
K=2^{40},\quad y=\lceil K/S_x\rceil,
$$
$$
m=4\max\!\left\{
5,\left\lceil\frac1{12}\log_2\big(2\log(y+1)\big)\right\rceil
\right\},
\quad d=2^m,\quad n=d/2.
\tag{6.1}
$$
它们只用于原 $T/L_m$ 比较，不更换 $a(S_x)$ 或 $k(S_x)$。
有
$$
d^3\ge2\log(y+1),\qquad
d^3\le\max\{2^{60},8192\log(y+1)\},
$$
$$
y<e^{12n^3},\qquad K/y\le S_x\le2K/y.
\tag{6.2}
$$
因此 $m=O(\log\log x)$、$d=O((\log x)^{1/3})$（超过固定初始头后），
特别对充分大的 $x$ 有
$$
m+d\le x\le y.
$$
例如 $x\ge e^{100}$ 已足够：
此时 $\log(y+1)\le4\log x$，
$d^3\le\max\{2^{60},32768\log x\}\le x^3/8$，
且 $m\le d$。

只在偶整数 $x$ 中选择，则 $R=x-m$ 为偶数、$R\ge d$。
$r=3$ 对充分大 $x$ 满足原
$$
r\le1+\left\lfloor\frac{\sqrt{x+1}}{8(m+1)}\right\rfloor .
$$
若同时保留全列比较的已付
$$
J_*=\left\lceil\max\{d+y-m-1,\ 81e^2/S_x,\ 4d^4+2\}\right\rceil,
$$
可取
$$
Q=\max\{R+3,\ y-m+J_*+1\}.
\tag{6.3}
$$
对上述充分大的 $x$，有 $J_*\le3y$、$Q\le5y$。
而 $26n^3\ge(13/2)\log(y+1)$，故
$$
Q<e^{26n^3}/4,\qquad x+1<e^{26n^3}/4.
$$
最高零头改基为 $m-1$ 后，物理强长度变为 $R+1$，
已付 $Q\ge R+3=(R+1)+(3-1)$；
在比较起点 $y$ 也保留
$Q\ge(y-(m-1))+J_*$。
全部原支持方向一致。

这些母窗检查不把完整 $J=\infty$ 源本身称为某个有限 $Q$ 的物理代表。
有限列的原同 $u$ 身份仍按各自已经证明的运输式使用。

## 7. 同一实际 $S_x$ 上的完整二阶物理矩

写
$$
L_s=1+\log((K+1)/s),\qquad
\mathcal A(s)=\sqrt s\,\|\widehat{\mathcal N}^{\,2}k(s)\|.
$$
前稿的证明只使用
$m\ge20,y\ge m+d,s\asymp K/y,y\le e^{12n^3}$
及已付的全列误差。
故 (6.1) 的小比较头仍给
$$
\mathcal A(S_x)
\le4(m+2)^2\sqrt{S_x}
+6\sqrt{L_{S_x}}\sqrt{\mu_1(S_x)}.
$$
对充分大的 $x$，$m+2\le L_{S_x}$，于是
$$
\boxed{
\mathcal A(S_x)^2
\le32L_{S_x}^4S_x+72L_{S_x}\mu_1(S_x).
}
\tag{7.1}
$$
低头 $m^2\sqrt{S_x}$ 仍在证明中保留。

对充分大 $L$，在偶整数
$e^L\le x\le e^{2L}$ 上令
$$
I_L^{\rm disc}
=\sum_{\substack{e^L\le x\le e^{2L}\\x\ {\rm even}}}
\frac{\mu_1(S_x)}x.
$$
(5.3) 给 $I_L^{\rm disc}\to0$。
这些偶整数的 $\sum 1/x\ge L/3$。
在同一窗上，$L_{S_x}\le8L$、$S_x\le e^{-3L}/3$。
对 (7.1) 的右端按权 $1/x$ 平均，因此可选一个同窗偶整数 $x_L$，
使
$$
\boxed{
\mathcal A(S_{x_L})^2
\le\frac{131072}{3}L^4e^{-3L}
+1728I_L^{\rm disc}
\longrightarrow0.
}
\tag{7.2}
$$
此处 $131072=32\cdot8^4$。
选择的是预算右端，所以同一选择还使
$L_{S_{x_L}}\mu_1(S_{x_L})\to0$。

完整列的全部真实行因此同时满足
$$
\boxed{
\|\mathcal N^2T^ja(S_{x_L})\|
\le\sqrt{j!}\,S_{x_L}^{(j-1)/2}\mathcal A(S_{x_L})
\quad(j\ge1).
}
\tag{7.3}
$$
特别原完整残量有
$\|\mathcal N^2Ta(S_{x_L})\|\to0$。
这里每一个 $S_{x_L}$ 都是实际平方自由尾的准确方差。

## 8. 实际方差尺度上的整列远孔占据量

还有一个直接对应物理起点 $x$ 的源专属估计。
对完整参考 $L_m$、任意 $z>x\ge m$，
在前稿位置正规式中取
$$
\mathcal W=\mathcal N_{[x,z)},\qquad
D_\omega=D_{[x,z)}.
$$
准确交换关系仍成立，且相对形式常数平方为
$\sum_{x\le i<z}a_i^2\le S_x$。
因此
$$
\sqrt s\,\|\widehat{\mathcal N}_{[x,z)}^{1/2}k_{L_m}(s)\|
\le\sqrt{S_x}\sqrt{\mu_{L_m}(s)}.
$$
按非负对角形式令 $z\to\infty$，得到
$$
\|\widehat{\mathcal N}_{\ge x}^{1/2}k_{L_m}(s)\|
\le\sqrt{S_x/s}\sqrt{\mu_{L_m}(s)}.
\tag{8.1}
$$

(6.1) 中 $x\le y$。对完整 $T/L_m$ 列差，
$[x,y)$ 的孔数至多 $y$，而
$\mathcal N_{\ge y}^{1/2}\le\Gamma_y/32$、
$\Gamma_y=32^{\mathcal N_{\ge y}}$。
故原加权列差给
$$
\|\widehat{\mathcal N}_{\ge x}^{1/2}(k_T-k_{L_m})\|
\le\sqrt{y+1}\,e^{-3d^4/2}\le e^{-d^4}.
$$
辅助 $\sqrt j$ 比较也已给
$\sqrt{\mu_{L_m}}\le\sqrt{\mu_T}+e^{-d^4}$。
在原准确 $s=S_x$ 处遂得
$$
\boxed{
\|\widehat{\mathcal N}_{\ge x}^{1/2}k_T(S_x)\|
\le\sqrt{\mu_1(S_x)}+2e^{-d^4}.
}
\tag{8.2}
$$
沿 (7.2) 的同一选择，该实际整列远孔占据量趋零。
它同时控制离开远尾真空的整列范数，
但没有把尾真空投影后的列当成某个有限头的精确 Gram 列。

## 9. 保留的缺口

本稿完成的是原全空间完整源在真正离散 $S_x$ 上的公共物理矩选择；
所有 $w\in\ker T$ 仍有
$\langle w,a(S_x)\rangle=\langle w,f_1\rangle$。

尚未证明真 $F_0$ 的原压缩 inverse 继承这些矩，
没有以 (8.2) 代替向原物理核的准确投影，
也没有支付完整 MP、真帽或指数孔权右逆的费用。
实际方差、原强头母窗及同 forcing 都已对齐，
但 $N=M$ 与普通 Hilbert ISP 仍开放。
