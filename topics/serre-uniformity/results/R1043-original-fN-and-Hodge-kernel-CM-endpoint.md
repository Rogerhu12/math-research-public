# R1043：原最高 sigma 系数与实际 Hodge 核的 CM 端值

日期：2026-11-27（UTC+8；2026-11-26 UTC）。
会话：Astra-serre-24b8836b-20261126；o1_theta / root；
全部尺度和两种 p mod12 行另经 o2_high_coefficient 独立纸审。

**已证明：对全部 p≡5 mod6、p≥41，原最高 sigma 系数准确等于
同一个实际 Hodge graph 核多项式在原 CM 标记的端值乘 −1/6。**
若 p=6N+5，结论为
\[
\boxed{\qquad f_N=-\frac16 T_0(1)\pmod p.\qquad}
\tag{1043.1}
\]
这里保持 R949 的原 sigma、正 CM 嵌入、完整 oldform 相位及原
六标记。T_0 是 R1037 / R1040 的准确归一化核多项式，定义重述于下。
这接通的是指定原 CM 读数；不以它替代 R1041 的核范数。

在同一个原 Lie 配对中，还得到
\[
\boxed{\quad
 B(c_0,\lambda)=B(c_0,\bar v)
 =\frac{3T_0(1)}{A(1)}
 =-\frac{18f_N}{A(1)}.
\quad}
\tag{1043.2}
\]
本篇不证明 T_0(1) 非零，不删除原 primitive 或 Legendre 筛选，
也不把这一个指定线性读数等同于 B(c_0,c_0)。

## 1. 两行共同的原族及归一化

设
\[
p=6N+5\ge41,\qquad m=(p-1)/2=3N+2,\qquad d=3N+1.
\]
用 R1023 / R1038 的同一个族和 Hodge frame：
\[
E_b:\quad y^2=x^3+3brx+r(1-2b^3),\qquad
r=1-b^3,\qquad \omega=\frac{dx}{2y}.
\tag{1043.3}
\]
其实际 Hasse 和 Kodaira–Spencer 为
\[
h_p=r^{N+1}A,\qquad
A=bQ_p(b^3)\text{ 单首},\quad \deg A=d,\qquad
\operatorname{KS}(\omega^2)=\frac{db}{2r}.
\tag{1043.4}
\]
A 的根简单，属于 F_{p²}，均避开 r=0；特别地 A(1)≠0。
这些是同一族的实际 Hasse 值，不是只差一个未知常数的超奇异多项式。

定义
\[
\mathcal L
 =r\partial_b^2-4b^2\partial_b-\frac94b.
\tag{1043.5}
\]
R1023 / R1038 从该族的原 Gauss–Manin 方程给出 \(\mathcal LA=0\)。
直接有
\[
\mathcal L(b^e)
 =e(e-1)b^{e-2}-(e+3/2)^2b^{e+1}.
\tag{1043.6}
\]
在 0≤e<d 中，最后一个系数皆非零；其第一个共振恰在 e=d。
因此 \(\mathcal L\) 在次数 <d 的多项式上单射。它将
\(\langle1,b^3,\ldots,b^{3N}\rangle\) 三角同构地送到
\(\langle b,b^4,\ldots,b^{3N+1}\rangle\)。于是存在唯一
\[
\boxed{\quad
T_0\in\mathbf F_p[b^3],\qquad \deg T_0<d,\qquad
\mathcal LT_0=A.
\quad}
\tag{1043.7}
\]
其次数为 d−1=3N，首系数为 −1；因为
\(-(3N+3/2)^2=-1\) 于 F_p。

对 p≡11 mod12，这是 R1037 / R1041 的 T_0；对 p≡5 mod12，
这是 R1040 的 T_0。整个证明以下不依赖 N 的奇偶性，只有原
oldform 尺度中的 \((-1)^N\) 必须继续保留。

## 2. 同一个原 fine source 的完整空间

先证明所需 weight p−1 的全空间公式，而不从 p≡11 mod12 的
r=2 应用直接扩大范围。原 H_6 曲线为 \(\mathbf P^1_b\)，
唯一 cusp 是 ∞，三个 order-three elliptic 点为 r=0。
在 (1043.3) 的 frame 中，
\[
\boxed{\quad
S_{p-1}(H_6,k)
 =\{r^{N+1}T(b)\omega^{p-1}:\ T\in k[b],\ \deg T<d\}.
\quad}
\tag{1043.8}
\]

在有限 r≠0 的点，(1043.3) 是好模型，所以标量正则。
在 r=0，取辅助参数 r=t⁶，作 x=t²x₀、y=t³y₀；
此时 \(\omega=t^{-1}\omega_0\)。weight p−1 的标量 F 必须满足
\[
6\operatorname{ord}_rF-(p-1)\ge0,
\]
故 \(\operatorname{ord}_rF\ge N+1\)。
原 fine 参数实际上是 r=v³，需同步运输二次 twist。
因为权重是偶数，截面下降；在 fine 参数中的最小零阶是
\[
3(N+1)-(p-1)/2=1,
\tag{1043.9}
\]
而辅助六次参数中是 2。这里没有把这两个阶数混为一谈。

在 ∞ 作 x=b²x₀、y=b³y₀，有
\(\omega=b^{-1}\omega_0\)，其中 \(\omega_0\) 是原 cusp 的单位 frame，
b^{-1} 是宽度六 cusp 的参数到一个单位。
cuspidality 因而要求 \(\deg F\le p-2=6N+3\)。
除去 r^{N+1} 后即 \(\deg T\le3N=d-1\)。
反向这些条件保证在全部点正则并在 cusp 消失，证明 (1043.8)。

该全空间不是只取一个 deck 角色。下一节使用的仍是原 fine Igusa
的规范截面 \(\mathfrak a^{p-1}=h_p\)，并置 \(u=\mathfrak a^2\)。
尤其在 p≡5 mod12 行，不把这个 fine u 偷换为实际 Raynaud 中心
所用的 \(\mathfrak a^4\)；两者的商、惯性角色和几何范围不同。

## 3. 实际 Cartier 与同一个核多项式

R932 / R952 的规范给
\[
\Phi_{p-1}(H)
 =\frac16\operatorname{KS}(H/\mathfrak a^{p-3}).
\]
对 \(H=r^{N+1}T\omega^{p-1}\)，准确为
\[
\Phi_{p-1}(H)=\frac{Tu}{12rA}\,db
 =u^p\frac{T\,db}{12r^{2N+3}A^3},
\qquad u^p=u\,h_p^2.
\tag{1043.10}
\]
原 Fourier 因子 1/6 和 KS 因子 1/2 均在这里。

设 s 为 A 的任一根，并记 \(\vartheta=4b^2/r\)。因
\(3(2N+3)=p+4\)，有
\[
\frac{(r^{-(2N+3)})'}{r^{-(2N+3)}}=\vartheta.
\]
由 \(\mathcal LA=0\)，在 A=0 处
\[
A''/A'=\vartheta,\qquad
A'''/A'=\vartheta'+\vartheta^2+\frac{9b}{4r}.
\]
展开全部三阶极部，得到
\[
\begin{aligned}
\operatorname{Res}_s
 \frac{T\,db}{12r^{2N+3}A^3}
&=\frac1{12r_s^{2N+3}A'(s)^3}
 \left(\frac{T''}2-\frac{\vartheta T'}2-\frac{9bT}{8r}\right)(s)\\
&=\frac{\mathcal LT(s)}
 {24r_s^{2N+4}A'(s)^3}.
\end{aligned}
\tag{1043.11}
\]

Cartier 杀二阶和三阶极部，对一阶极部系数取 p 次根。
R952 的 whole-space 公式保证输出仍在 (1043.8)，其系数的
逆 Frobenius及实际 character transport 不丢弃。
若输出多项式为 \(\mathscr U_b(T)\)，比较 (1043.10) 的简单极部，
并取 p 次方，准确得
\[
\boxed{\quad
 \mathscr U_b(T)(s)^p
  =\frac12r_s^{4N+1}A'(s)^{p-3}\mathcal LT(s),
 \qquad A(s)=0.
\quad}
\tag{1043.12}
\]
例如 r 的指数来自
\(p-(2N+4)=4N+1\)，不是改变 Hodge frame 后猜测的幂。

所有 d 个简单根均保留，次数 <d 的多项式由这些值唯一决定。
因此，即使 (1043.10) 的 rational expression 在 r=0 还有极部，
也不需要删除那些点来判零：
\[
\mathscr U_b(T)=0
\iff \mathcal LT\equiv0\bmod A
\iff \mathcal LT=cA
\iff T\in kT_0.
\tag{1043.13}
\]
中间使用 \(\deg\mathcal LT\le d\)，最后使用 (1043.6) 的单射性。

现在保持指定原 CM form：
\[
F=V_{p-1}^{\dagger}(Q)
 =F_{p-1}(Q)-2^{p-1}\zeta^2F_{p-1}(Q^4).
\tag{1043.14}
\]
F_{p-1} 是 R913 / R949 正 CM 嵌入的归一化理想 theta 级数，
首 Q 系数为 1。对任何惰性 p，每个 p-倍 Fourier 指数的系数
都为零模 p：p 的奇数次赋值不可能是理想范数；若范数含 p²，
相应理想含 (p)，其 Hecke 特征贡献含 \(p^{p-2}\)。
原 Q⁴ oldform 保留这个性质，因为 p 为奇数。
故 R952 的真正 Fourier–Cartier 公式给 \(\mathscr U F=0\)。

由 (1043.13) 和首系数 1，
\[
\boxed{\quad
F(E_b,\omega)=\xi_p r^{N+1}T_0(b),\qquad \xi_p\ne0.
\quad}
\tag{1043.15}
\]
这一步在全部 p≡5 mod6 成立，不需 p≡2,5 mod9，
也没有把 r=8 的原 companion 换为本 weight p−1 form。

## 4. 原 oldform、Tate 符号及完整尺度

本节写 \(s_0=\sqrt{-3}\)、\(\zeta=(-1+s_0)/2\)，保持原正 CM
嵌入。另置
\[
\rho^3=2,\qquad c=\rho^2,\qquad \lambda^2=\rho;
\quad \rho,c\in\mathbf F_p,\quad \lambda^6=2.
\tag{1043.16}
\]
这里 \(\rho\) 是 F_p 中唯一的立方根，与 R949 中表示
\(1+\zeta\) 的解析字母 \(\rho\) 无关。

由 R936 的原粗参数 \(u_{\rm old}\)，取
\[
b=c\,u_{\rm old},\qquad
x_b=\lambda^2x_{\rm old},\qquad
y_b=\lambda^3y_{\rm old}.
\]
其 ET15 方程正好变为 (1043.3)，而
\(\omega_b=\lambda^{-1}\omega_{\rm old}\)。
偶权值不依赖 \(\lambda\) 的正负。

R936 ET17 的完整正确 Tate 相位于是给
\[
V_4^\dagger(E_b,\omega)=\lambda^4\,12s_0r,\qquad
\eta^{12}(E_b,\omega)=-6s_0\lambda^6r=-12s_0r,
\]
\[
E_6(E_b,\omega)=864r(1-2b^3)=-c_6(E_b).
\tag{1043.17}
\]
特别地
\[
\frac{E_6}{\eta^{12}}=24s_0(1-2b^3),\qquad
\left.\frac{E_6}{\eta^{12}}\right|_{b=1}=-24s_0.
\tag{1043.18}
\]
这恰是 R949 (949.5) 的原 full-six 标记。
没有把 E₆ 误认成 c₆，也没有换到其共轭标记。

R936 §5 的同一个完整 integral triangular basis，适用于任意
weight \(6N+4=p-1\)，给原单首 companion：
\[
F=V_4^\dagger\eta^{12N}P_N(E_6/\eta^{12}),\qquad
P_N\text{ 单首、次数 }N.
\tag{1043.19}
\]
理由是 \(F/V_4^\dagger\) 在三个 elliptic 点正则；
再除 \(\eta^{12N}\) 后为原粗曲线上的 polynomial，
其原 deck 角色迫它是 \(u_{\rm old}^3\) 的次数 ≤N 多项式。
原 basis
\(V_4^\dagger E_6^{N-j}\eta^{12j}\)、0≤j≤N，
首项依次是 \(Q^{1+3j}\)，系数均为 1，且已证明为整个整角色空间。
F 的首 Q 系数 1 因而固定 P_N 单首。
这不依赖 N 的奇偶性或原 r=2/r=8 选行。

代入 (1043.17) 得
\[
F(E_b,\omega)
 =(-1)^N\lambda^{p-1}12s_0(6s_0)^N r^{N+1}
 P_N\!\left(24s_0(1-2b^3)\right).
\tag{1043.20}
\]
除去 r^{N+1}，其 b^{3N} 系数为
\[
(-1)^N\lambda^{p-1}12s_0\,864^N,
\]
因为 \((6s_0)(-48s_0)=864\)。
与 T₀ 的首系数 −1 比较得到
\[
\boxed{\quad
\xi_p=(-1)^{N+1}\lambda^{p-1}12s_0\,864^N.
\quad}
\tag{1043.21}
\]
p≡11 mod12 时 N 奇，恢复 R1041 的正号；
p≡5 mod12 时 N 偶，多出的负号不能略去。

## 5. 同一个 marked quotient 与原 f_N

保持 R949 的原 sigma 规范
\[
E_0:y^2=x^3-1,\qquad dz=dx/(2y),\qquad \sigma'(0)=1,
\]
\[
x(z)\sigma(z)^6=z^4\sum_{i\ge0}f_i z^{6i}.
\tag{1043.22}
\]
定义同一个原 marked quotient
\[
\mathcal C_{p-1}^{\rm mark}
 =\left[\frac{F}{V_4^\dagger E_6^N}\right]_{\rm mark}.
\tag{1043.23}
\]
(1043.18) 证明原 mark 正是当前 b=1 分支。

在 fine r=v³ 的好模型上，分子分母都除去同一个必需的一阶零，
因此 (1043.23) 是整 regular quotient，不是两个零值的形式相除。
由 (1043.15)、(1043.17)、(1043.21)，在整个 r≠0 范围先有
\[
\frac{F}{V_4^\dagger E_6^N}
 =(-1)^{N+1}2^N
       \frac{T_0(b)}{(1-2b^3)^N}.
\]
两边都在 b=1 正则，故
\[
\boxed{\qquad \mathcal C_{p-1}^{\rm mark}=-2^NT_0(1).\qquad}
\tag{1043.24}
\]
这里 \(\lambda^{p-5}=(\lambda^6)^N=2^N\)，
而 \((1-2b^3)^N|_{b=1}=(-1)^N\)；
两行最终确实有同一个负号。

R949 (949.7)、(949.39) 已在这个原 sigma、原 mark 和原 period
规范下证明
\[
\mathcal C_{p-1}^{\rm mark}
 =\frac{(p-1)!}{24}(-864)^{-N}f_N.
\tag{1043.25}
\]
因为 \(6N+4=p-1<p\)，所有系数都在其已证整性范围，
阶乘也是 p 单位。
Wilson 与 (1043.24) 给
\[
f_N=24(-1728)^NT_0(1).
\tag{1043.26}
\]
再用 \(3N=(p-5)/2\)、\(1728=12^3\)，
\[
1728^N=12^{(p-5)/2}=\frac{(3/p)}{144}.
\]
在 p≡11 mod12 行，N 奇、\((3/p)=1\)；
在 p≡5 mod12 行，N 偶、\((3/p)=-1\)。
故两行均有
\[
(-1)^N(3/p)=-1,
\]
代回 (1043.26)，严格得到 (1043.1)。

这也证明
\[
f_N\ne0\iff T_0(1)\ne0
       \iff\mathcal C_{p-1}^{\rm mark}\ne0,
\tag{1043.27}
\]
但没有单凭这些等价式断言任何一项为单位。

## 6. 同一个原首 log 与核的线性读数

此节在 R1037 的 p≡11 mod12 actual good type 和
R1040 的 p≡5 mod12 actual Raynaud good type 中分别使用其已证
整来源；不把 whole Jacobian 的约化类型混同。

令
\[
f(b)=r^{4N+2},\qquad
\bar{\mathcal Q}(a)=\operatorname{quo}(f\,a(b^p),A^2)\bmod A,
\]
其中 a(b^p) 保持 a 的系数不变。
归一化核向量 c₀ 定义为
\[
\frac{f\,c_0(b^p)}{A'}\equiv T_0\pmod A.
\tag{1043.28}
\]
这是 R1037 / R1040 的同一个 \(\ker\bar{\mathcal Q}\) 生成元；
该定义由根集的 Frobenius 置换和非零乘子组成，故唯一。
其系数在 F_p。对每个 s∈S={A=0}，
\[
c_0(s^p)=\frac{T_0(s)A'(s)}{r_s^{4N+2}}.
\tag{1043.29}
\]

在实际 Lie 基 e_s=θ_sf_s 上，两行的原对称型均为
\[
q_s=-\frac{r_s^{4N+2}}{A'(s)^2}\in\mathbf F_p^\times,\qquad
B(e_s,e_t)=\frac{q_s}{2}\mathbf1_{t=s^p}.
\tag{1043.30}
\]
仍取原首 formal vector 和完整 log vector
\[
\lambda(b)=-\frac{6(b+1)}r,\qquad
\bar v=(1-\bar{\mathcal Q})\lambda.
\tag{1043.31}
\]
(1043.29)–(1043.30) 直接给
\[
B(c_0,\lambda)
 =-\frac12\sum_{A(s)=0}\frac{T_0(s)\lambda(s)}{A'(s)}.
\tag{1043.32}
\]

现在对原有理微分 \(T_0\lambda\,db/A\) 用全部留数定理。
在∞，它是 O(b^{-3})db，所以留数为零；
除 S 外，只在 b=1、ζ、ζ² 有简单极。
λ 在三个点的留数依次为 4、−2、−2。
由 \(T_0\in k[b^3]\)、\(A=bQ_p(b^3)\)，有
\[
T_0(\zeta^j)=T_0(1),\qquad
A(\zeta^j)=\zeta^j A(1).
\]
三处留数的总和准确为
\[
\frac{T_0(1)}{A(1)}
  (4-2\zeta^{-1}-2\zeta^{-2})
=\frac{6T_0(1)}{A(1)}.
\]
因此 S 上的和为其负数；代回 (1043.32) 得
\[
B(c_0,\lambda)=\frac{3T_0(1)}{A(1)}.
\]
实际 \(\bar{\mathcal Q}\) 对 B 自伴，且 \(\bar{\mathcal Q}c_0=0\)，
故 \(B(c_0,\bar v)=B(c_0,\lambda)\)。
结合 (1043.1) 即为 (1043.2)。

这里没有对首 log 的完整 \(\bar{\mathcal Q}\lambda\) 或
后续 \(K_{\mathcal Q,p}\) 的 \(\bar{\mathcal Q}^2\lambda\) 误作删项。
只因当前第一输入恰为真正的核向量，才由自伴性得到这个等式。

## 7. 已接通的来源与仍须证明的非零

本篇把同一个原 f_N、原 all-weight CM quotient、原 Cartier 核
和实际首 log 的指定核读数完全接通，且常数在两种 p mod12 行相同。
所有 p≥41 的惰性素数均包括；没有附加 mod9 限制。

它与 R1041 的读数仍不同：

- 本篇为 \(B(c_0,\lambda)=B(c_0,\bar v)\)，等价于原 f_N。
- R1041 原 r=2 bare 高系数等价于 \(B(c_0,c_0)\) 非零，
  并保留该原 r=2 行的 mod9 范围。
- 原 CM 深盘系数还含指定 J 和 D、完整 \(\bar{\mathcal Q}\)，
  并不由上述任何一个单独读数自动决定。

即使将来证明 f_N 非零，也仍须按课题原要求支付同 h 的 primitive
与 Legendre 筛选，或者在另一实际几何来源中完成全部排点标准。
本篇没有将核一维或 B 完美冒作一个指定配对非零。
R1031 的实际 Faber 截断中心导数判据可与 (1043.27) 联用，
但其待证非零并未因此消失。

## 来源与审核范围

- [R936](R936-explicit-polynomial-trace-of-the-whole-supersingular-pairing.md)，
  ET15–ET18、§§4–5：原族缩放、正确 Tate 符号、
  原整 triangular basis 及 full-six marked phase。
- [R949](R949-original-all-weight-sigma-CM-marked-identity.md)，
  (949.2)、(949.5)–(949.7)、§8：同一个原 sigma、all-weight mark
  及首 p 系数整性；本篇在 i=N 的合法范围使用。
- [R952](R952-exact-Cartier-formula-for-the-last-Hasse-obstruction.md)，
  (952.12)–(952.13)：真正 fine Igusa Cartier、逆 Frobenius及全角色运输。
- [R1037](R1037-original-Hodge-graph-operator-and-primitive-MW-annihilator.md)：
  p≡11 mod12 的实际 \(\bar{\mathcal Q},B,c_0,\bar v\)。
- [R1038](R1038-original-p5-Raynaud-lowest-type-and-complete-first-log.md)、
  [R1040](R1040-original-p5-Hodge-graph-and-primitive-MW-annihilator.md)：
  p≡5 mod12 的实际 Raynaud type、原 Hasse、完整首 log 和同一核。
- [R1041](R1041-original-r2-bare-coefficient-and-Hodge-kernel-norm.md)，
  §§2–4：p≡11 mod12 的完整源公式；本篇 §2–4 重新保两行的
  fine 零阶、Cartier 指数与 \((-1)^{N+1}\)，不直接外推其 bare 范数结论。
- [R1031](R1031-original-fN-and-actual-Faber-truncation-central-derivative.md)：
  同一个 f_N 的原 Faber 截断中心读数，供后继非零问题接续。

全部新计算为原对象上的纸面恒等式、局部留数和明确源比较。
没有执行数学程序，没有重扫任何已登记有限窗口。
