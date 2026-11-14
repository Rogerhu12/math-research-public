# R499 — 新四态来源的完整 Y 多项式、D33 身份与十七维正块

日期：2026-11-14。**状态：已证明。** 本篇计算 R496 新增真实状态
\(z=q-h/2\) 的整个第一 \(Y\) 来源。使用原四挠纤维和绝对周期锚，
得到一个显式的 degree21 多项式，并在完整二十三维 theta 空间中证明
\[
\boxed{Z_Y=D_{33}v_Y,\qquad
D_{33}=\omega^{-1}N_{19}N_7^{-2}.}
\]
因此新线和参考线的系数分别是 \(-52/3\) 与
\((1+\delta)/(2016b)\)。两个来源的 CM7 轨道合起来准确张满
\(N_7^9=1\) 的全部十七维空间，原外谱也在其中。

这里证明完整第一边缘；它本身没有把两个六变量来源的不同伴随认同。
保原五伴随的身份须在联合来源上另证。完整中央跨 \(p\) 非零尚未得到。

## 1. 原状态、原中心与所计算的函数

保持 R465、R488、R496 的原周期和全部 canonical lifts。令
\[
\delta^2=-3,\quad \omega=(-1+\delta)/2,\quad X=x^3,\quad
\mathcal C(t)=
 \sigma(\delta t)\sigma(2\delta t)
 \sigma(\gamma_7t)\sigma(\bar\gamma_7t).
\]
原 \(\rho_0\) 的常数为 \(-1/84\)。以 R465 的实际 \(W\) 轴定义
\(f_t=\mathsf T_{W,t}\rho_0\)，其中 \(t=\ell/4\in E[4]\)。
原三个状态满足
\[
e_1=\frac14\sum_{E[4]\setminus E[2]}f_t
       -\frac14\sum_{E[2]}f_t,\qquad
h=e_1+e_2=-\frac12\sum_{E[2]}f_t.
\tag{1}
\]
R496 的完整偶核心 \(F=K_{V'}^2\) 已绝对定标为
\[
Ff_t=\epsilon(t)f_t,\qquad
\epsilon(t)=(-i)^{N(\ell)}.
\tag{2}
\]
它在 \(E[2]\) 上为一。因此新增状态准确是
\[
z=Fe_1-h/2
   =\frac14\sum_{E[4]\setminus E[2]}\epsilon(t)f_t.
\tag{3}
\]

对第一未加倍输出 \(Y_s\)，仍使用 R465 的整个函数
\[
\Phi_t(u)=
(\mathsf T_t^{(29)}\mathcal C)(u)
(\mathsf T_{3\delta t}^{(1)}\sigma)(u)
(\mathsf T_{4t}^{(1)}\sigma)(2u).
\]
其完整指数是
\[
\Phi_t(u)=
e^{-\eta_t((37-3\delta)u+36t)}
\mathcal C(u+t)\sigma(u+3\delta t)\sigma(2u+4t).
\tag{4}
\]
由 (3) 得
\[
\mathcal Z(u):=(Y_s)_*z
=-\frac1{336}\sum_{E[4]\setminus E[2]}
   \epsilon(t)\Phi_t(u),\qquad
Z_Y(u)=\mathcal Z(2u)\in\mathcal S_{136}.
\tag{5}
\]
符号 \((Y_s)_*z\) 在此表示其 Amice 生成函数。
双覆盖、全部 Gaussian 和独立输入均来自原来源。

## 2. 两类四挠点的绝对符号

不能随意把 \(x(t)=-1\pm\sqrt3\) 对应到 (2) 的两个范数类。
下面给一个固定周期锚。

先取 \(b=-1\)，令 \(\Omega_0>0\) 是其原实周期。
实半周期满足 \(x_{-1}(\Omega_0/2)=1\)。
在 \(0<u<\Omega_0/2\) 的实支上 \(x_{-1}(u)>1\)，
原倍点公式遂给
\[
x_{-1}(\Omega_0/4)=1+\sqrt3.
\]
转到 \(b=1\) 时，保持微分和 \(\sigma'(0)=1\) 的规范：
\[
\sigma_1(u)=i\sigma_{-1}(u/i),\qquad
x_1(u)=-x_{-1}(u/i),\qquad \Omega=i\Omega_0.
\tag{6}
\]
故 \(t=\Omega/4\) 的实际坐标为
\[
h=x(2t)=-1,\qquad e=x(t)=-1-\sqrt3,
\qquad N(\ell)=1\pmod4,\qquad\epsilon(t)=-i.
\tag{7}
\]
原 CM 除法公式
\[
x(\delta t)=-\frac{x(t)^3+4}{3x(t)^2}
\]
把 (7) 送到 \(e=-1+\sqrt3\)。
\(\delta=1+2\omega\) 的范数为三，因此另一类准确有
\[
e=-1+\sqrt3,\qquad \epsilon(t)=+i.
\tag{8}
\]
两种 \(y(t)\) 符号具有同一 \(\epsilon\)，三个非零二挠纤维由
原 \(\mu_3\) 旋转给出。(6) 同时固定 reduced 指数的规范，
不留下额外半周期平方根选择。

在 \(\mathbf Q(\sqrt3,\delta)\) 中令 \(\tau\) 固定 \(\delta\)、
把 \(\sqrt3\) 送到 \(-\sqrt3\)；于是它把 \(i\) 送到 \(-i\)。
若 \(c\) 是先对 (7) 的两种 \(y(t)\) 求和后的系数，
整个四点纤维的带权迹准确为
\[
\boxed{-i(c-\tau c).}
\tag{9}
\]
这一式在 \(\mathbf Q(\delta)\) 中，且符号由 (6)–(8) 支付。

## 3. 全部纤维的整除与显式多项式

使用 R465(19)–(26) 的同一有理加法式。特别保留
\[
c_t^8=\frac{e-h}{12h^2y(t)^2},\qquad
\sqrt{x(2u)-h_m}
=-\frac{x(u)^2-2h_mx(u)-2h_m^2}{2y(u)}.
\tag{10}
\]
第一个式子在原 \(c_t^{56}\) 中取七次幂；反号不会被平方消掉。

附脚本逐字保留 R465 的完整有理分子、分母和所有原点首项，
在
\[
\mathbf Q(\sqrt3,\delta)[x,\xi]/
  \bigl(\xi^2-(e^3+1)(x^3+1)\bigr)
\]
中先对 \(\pm y(t)\) 求和，再做完整多项式整除。
余数严格为零。所得多项式次数为 \(67\)，应用 (9)，
最后加上三个真实 \(\mu_3\) 纤维：
在 \(\sigma^{136}x^j\) 中保 \(j\equiv2\bmod3\)，并乘以三。
这给 (5) 的全部二十三个坐标，没有使用截断插值或变化素数的扫描。

为把结果完整写出，先用 \(b=1\)。置
\[
\begin{aligned}
F_6(X)={}&X^6-84X^5+11040X^4+47936X^3\\
 &+204288X^2+33792X+4096,\\
C_{13}(X)={}&(X-8)(X+1)^2(X^2+20X-8)
 (7X^2-4X+16)F_6(X),
\end{aligned}
\tag{11}
\]
以及
\[
\begin{aligned}
A_8(X)={}&25X^8+5960X^7-12224X^6+467744X^5\\
 &+2039296X^4+2398208X^3+3014656X^2
   +1703936X+65536,\\
B_8(X)={}&X^8+176X^7+64384X^6+353504X^5\\
 &+1418752X^4+499712X^3-1212416X^2
   -1048576X+65536.
\end{aligned}
\tag{12}
\]
整个结果是
\[
\boxed{
Z_Y(u)=\frac47\sigma(u)^{136}x(u)^2
 C_{13}(X)\{-A_8(X)+\delta B_8(X)\}.
}
\tag{13}
\]
其质量为零，首个非零 Taylor 项是
\[
Z_Y(u)=(-100+4\delta)u^6+O(u^{12}).
\tag{14}
\]
这里 (14) 只是 (13) 的直接结果，证明用的是整个 (13)。

一般 \(b\) 不另改 CM 规范：在每个 \(d\) 次多项式中，
将 \(a_jX^j\) 替为 \(a_jb^{d-j}X^j\)。
因 (11)–(12) 总次数为 \(21\)，这准确给
\(b^{-1}Z_{Y,1}(b^{1/6}u)\)，即与 R465/R470 相同的原来源。
特别可直接取本题固定 \(b=17\)。

## 4. 整个 D33 身份

在同一个完整主角型基
\[
\mathcal B=\bigl(\sigma^{136}x^2X^j\bigr)_{j=0}^{22}
\]
中，令 \(M=N_7\)、\(N=N_{19}\)，规范仍为 R466/R476 的
完整 canonical traces。已付的全矩阵满足
\[
M^{18}=I,\qquad MN=NM,\qquad
D:=\omega^{-1}NM^{16},\qquad D^2=I.
\tag{15}
\]
这里 \(M^{16}=M^{-2}\)。

R488 原三态中的正来源是
\[
v_Y=\Xi(2u)+\frac{1+\delta}{4}S(2u).
\tag{16}
\]
把 R465 的整个 \(\Xi(2u)\)、\(S(2u)\) 及 (13) 代入同一基，
逐个精确比较所有二十三个有理二元坐标，给
\[
\boxed{Z_Y=Dv_Y,\qquad v_Y=DZ_Y.}
\tag{17}
\]
脚本同时由 \(N,M\) 重构 (15)，并与 R476 的原 \(D_{33}\)
矩阵一致，不另外选择一个只在所需向量上正确的算子。
因为 \(\mathcal B\) 是整个空间的基，(17) 是全函数身份。

另外
\[
M^9v_Y=v_Y,\qquad M^9Z_Y=Z_Y,
\tag{18}
\]
与 R496 的整个新 \(Y\) 二挠平均为零一致。

## 5. 参考线、新线及全部八维负块

令
\[
D_\pm=(I\pm D)/2,\qquad
H=H_{\mathrm{ref}},\quad H(0)=1.
\]
\(H\) 仍是 R476 已识别的 \(E_{668168}\) 来源；
不是另一条 CM7 特征同为一的曲线。

由 (17) 得
\[
D_+Z_Y=D_+v_Y,\qquad D_-Z_Y=-D_-v_Y.
\tag{19}
\]
原 \(S(2u)\) 在 \(D_+\)，所以后一式也是
\(D_-Z_Y=-D_-\Xi(2u)\)。
以 R476 的同一八元基
\[
H,\ W_*,\ N_7W_*,\ldots,N_7^6W_*,
\qquad
W_*=-\frac{111}{280}\sigma^4\sigma(2u)\sigma(8u)\Theta_4^2
\]
表示，完整负块为
\[
\boxed{
D_-Z_Y=\frac{1+\delta}{2016b}H+
 \sum_{j=0}^{6}r_jN_7^jW_*.
}
\tag{20}
\]
全部系数如下；\(W_*\) 使用 R476 原 \(b\) 规范。

| \(j\) | \(r_j\) |
|---:|---:|
| 0 | \(5/333\) |
| 1 | \(-5/444+5\delta/1332\) |
| 2 | \(5\delta/333\) |
| 3 | \(5/333-5\delta/666\) |
| 4 | \(-5/444-5\delta/1332\) |
| 5 | \(5/222+5\delta/666\) |
| 6 | \(35/1332-5\delta/1332\) |

附脚本用原八元基的完整整系数提取器核对 (20) 的每一个坐标，
其固定坏素数仍可沿用 R476 的分母集合。
因此原新线投影 \(\mathcal Q\) 和原参考投影 \(\mathcal Q_H\) 给
\[
\boxed{
\mathcal QZ_Y=-\frac{52}{3}S_{\mathrm{new}},\qquad
\mathcal Q_HZ_Y=\frac{1+\delta}{2016b}H.
}
\tag{21}
\]
(20) 同时保留其余七维轨道，(21) 没有将它们删去。

## 6. 两个轨道准确张满整个正块

置 \(P_9=(I+M^9)/2\)。在完整 \(\mathcal B\) 中的精确维数是

| 实际空间或循环子空间 | 维数 |
|---|---:|
| \(\operatorname{im}P_9\) | 17 |
| \(\operatorname{im}(P_9D_+)\) | 9 |
| \(\operatorname{im}(P_9D_-)\) | 8 |
| \(\langle M^jv_Y:0\le j<9\rangle\) | 9 |
| \(\langle M^jZ_Y:0\le j<9\rangle\) | 9 |
| \(\langle M^j(v_Y+Z_Y):0\le j<9\rangle\) | 9 |
| \(\langle M^j(v_Y-Z_Y):0\le j<9\rangle\) | 8 |
| \(\langle M^jv_Y,M^jZ_Y:0\le j<9\rangle\) | 17 |

所有秩均在 \(\mathbf Q(\delta)\) 上用整个矩阵精确消元。
结合 (18)、(19) 及两块维数，得到等号
\[
\begin{aligned}
\langle M^j(v_Y+Z_Y)\rangle&=\operatorname{im}(P_9D_+),\\
\langle M^j(v_Y-Z_Y)\rangle&=\operatorname{im}(P_9D_-),\\
\langle M^jv_Y,M^jZ_Y\rangle&=\operatorname{im}P_9.
\end{aligned}
\tag{22}
\]
第一块的最小多项式是 \(T^9-1\)，第二块为
\[
\frac{T^9-1}{T-\omega}
 =(T-1)(T-\omega^2)(T^6+T^3+1).
\tag{23}
\]

三个落在原系数域中的 CM7 特征还可逐块列出：

| CM7 特征 | 正块全维数 | \(D_+\) | \(D_-\) |
|---|---:|---:|---:|
| \(1\) | 2 | 1 | 1 |
| \(\omega\) | 1 | 1 | 0 |
| \(\omega^2\) | 2 | 1 | 1 |

这五维只是三个有理特征的总和；整个正块是十七维。
其余十二维仍完整存在，不能由 (21) 的两条算术线替代。

## 7. 对实际后续的准确接口

R496 已证明新增状态保原 \(M\) 深度矩形、
simultaneous CM13/19 标签及完整第一轴投影的合法性。
本篇确定它的全部第一边缘及所有上述投影的质量。

尤其新来源虽有整个 \(W\) 边缘零、第一 \(Y\) 非零，
该非零本身不等于原 rank-two 中央非零。
由 (17) 或 (21) 单独也不能推出两个六变量来源的五伴随相同。
后续若在整个联合上得到 \(D\) 身份，才可把 (19) 升级到相同
伴随的条件行；其实际 norm7/norm19 纤维仍须运输所有混合域。

## 证书与依赖

- [完整带权四纤维、多项式及二十三坐标计算](../scripts/check-r499-four-state-z-complete-y-source.py)；
  [精确结果](../scripts/check-r499-four-state-z-complete-y-source.json)。
- [R496：原新轴偶核心及四态](R496-original-new-axis-even-core-and-four-source-group.md)。
- [R465：同一原四挠有理分子与全 Xi](R465-original-common-six-sigma-core-and-new-conditional-central-row.md)。
- [R476：全 D33 负块及八元基](R476-original-complete-xi-normtwo-bridge-and-integral-eight-source-basis.md)。
- [R488：原 v 状态和真实全来源规范](R488-original-shared-a-odd-core-and-actual-even-depth-dihedral-return.md)。

