# R267 — 真半特征降阶、四维完整极空间与原八次伴随的一阶表达

日期：2026-11-13。**状态：半特征及实际 deck lift、包含原 $4692$ 项的完整输入、十九阶表面极项的准确抵消、四条代数降阶、真实共轭十七迹、全部极补偿、原四八次伴随的可逆矩阵及原 A/B 的完整中央回代均已证明。这里的固定对数常数经过原二处投影准确为零；没有由这项降阶推出原中央非零。**

本篇接续 [R259](R259-normtwo-compensation-conductor17-rankone-and-full-log-transport.md)、
[R261](R261-nonpullback-normtwo-pole-correction-and-original-e34-row.md)。
下面选择的乘子有真实的非平凡二挠半特征。它消去 R259 的非恒定
$\Upsilon$ 项时，也改变目标线丛与 norm-two 的 canonical deck lift。
这两项变化以及残余的十六个真极均在本篇保留。

## 1. 原分支、半特征与实际 norm-two 输入

沿用
$$
\alpha=1+i,\qquad\beta=4-i,\qquad\bar\beta=4+i,\qquad
E_0:y^2=x^3-x,\qquad dz=\frac{dx}{2y},
$$
$$
x\sim z^{-2},\qquad y\sim-z^{-3},\qquad
\sigma\sim z,\qquad\vartheta(0)=1,\qquad
\sqrt x=\frac{\vartheta}{\sigma}.
$$
仍令 $S_8=-y\vartheta\sigma^3$、$F=S_8^{17}$。对
[R253](R253-four-octic-ray-logarithms-and-norm2-constants.md)、
[R254](R254-octic-ray-original-companions-and-full-fourth-order-transport.md)
的四个实际角色 $\chi_k(3)=\zeta_8^k$，$k=1,3,5,7$，写
$$
\Psi_k=\Phi_k+C_k,\qquad
\Phi_k(z+T_0)=-\Phi_k(z)-2C_k,\qquad T_0=(1+i)\Omega/2.
$$
令 $b_k=[z^2](-\Phi_k''/8)\ne0$，并记
$$
\phi_k=\Phi_k/b_k,\qquad c_k=C_k/b_k.
\tag{1}
$$
这里只除以一个固定非零代数数；没有假设 $C_k$ 是 $p$ 单位。

在目标变量 $w$ 中置 $X=x(\beta w)$、$Y=y(\beta w)$，并定义
$$
\boxed{
h^\flat(w)=\frac{X^{25}\,\vartheta(\beta w)}
                  {Y^{17}\sigma(\beta w)}.
}
\tag{2}
$$
这是 $T_0$ 对应的 flat section，两个基本周期的特征都是 $-1$，
而不是目标椭圆曲线上的单值椭圆函数。原分支准确给
$$
h^\flat(0)=-1,\qquad
\boxed{h^\flat(w)F(\beta w)=-\vartheta(\beta w)^{68}.}
\tag{3}
$$
特别不能把中心值为 $+1$ 的 $(1-X^{-2})^{-17/2}$ 直接代替 (2)
而保留后面的符号。

设 $t=\beta z$、$U=x(t)^2$。原 CM2 公式
$$
\sigma(\alpha t)=\alpha\sigma(t)\vartheta(t),\quad
\vartheta(\alpha t)=-\frac{y(t)\sigma(t)^3}{\vartheta(t)},\quad
x(\alpha t)=-\frac{i(U-1)}{2x(t)}
$$
逐项给出
$$
\boxed{
h^\flat(\alpha z)=-\left(\frac{U-1}{U+1}\right)^{17}.
}
\tag{4}
$$
所以真实输入乘子 (4) 是椭圆函数，但在 norm-two 的非平凡 deck
平移 $z\mapsto z+T_0$ 下反号。
R259 的 $F(\alpha\beta z)$ 在标准 Mumford lift 下也是反号；
它原来的 canonical deck lift 是 $-T_{T_0}$。
乘 (4) 后，目标变成未扭曲的 $\vartheta(\beta w)^{68}$，
其拉回 $\vartheta(\alpha\beta z)^{68}$ 在该 lift 下为正号。
**新的 canonical deck lift 因此是 $+T_{T_0}$。**
对应的有限平坦迹是两个真实分支相加，没有额外 $1/2$。

记
$$
G_\beta=F(\beta z)^2,\qquad H_\beta=F(\alpha\beta z),
\qquad\nabla_{G_\beta}=\partial_z-G_\beta'/G_\beta.
$$
保留 R259 的原极补偿后，实际修改输入是
$$
\mathcal I_k=
\nabla_{G_\beta}^2\!\left(h^\flat(\alpha z)H_\beta\phi_k\right)
+\frac{4692\beta^2}{x(\beta z)}
       h^\flat(\alpha z)H_\beta\phi_k .
\tag{5}
$$
这包括 R261 的全部 Leibniz 项，而非只在输出乘 $h^\flat$。
由
$$
\frac{h^\flat(\alpha z)H_\beta}{G_\beta}
=-(1-U^{-1})^{17},\qquad
\partial_z\log\frac{h^\flat(\alpha z)H_\beta}{G_\beta}
=\frac{68\beta}{y(t)},
$$
完整输入可写成
$$
\boxed{
\mathcal I_k(z)=
-\vartheta(\alpha\beta z)^{68}
\left[
\phi_k''(z)+\frac{136\beta}{y(t)}\phi_k'(z)
+\frac{4488\beta^2x(t)}{U-1}\phi_k(z)
\right].
}
\tag{6}
$$
这里 $\phi_k$ 的系数并非零。
如果相对于新的 theta frame 写协变导数，(6) 的三项分别是
$$
\nabla_{\vartheta(\alpha\beta z)^{68}}^2
       \bigl(-\vartheta(\alpha\beta z)^{68}\phi_k\bigr),
$$
$$
\frac{136\beta}{y(t)}
\nabla_{\vartheta(\alpha\beta z)^{68}}
       \bigl(-\vartheta(\alpha\beta z)^{68}\phi_k\bigr),
\qquad
\frac{4488\beta^2x(t)}{U-1}
       \bigl(-\vartheta(\alpha\beta z)^{68}\phi_k\bigr).
\tag{7}
$$
因此换连接没有删除原对数项或原 $4692$ 项。

## 2. 表面十九阶极的完整抵消及真正一阶降阶

目标导数准确满足
$$
\frac{(h^\flat)'}{h^\flat}=-\frac{34\beta}{Y},\qquad
\frac{(h^\flat)''}{h^\flat}
=\frac{102\beta^2(X^2+11)}{Y^2}.
$$
在 $X=\pm1$，$h^\flat$ 有十七阶极，其二阶导数有十九阶极。
必须保留 R261 式 (3) 的全部三项，才能得到
$$
\begin{aligned}
& (h^\flat)''
+68\beta(h^\flat)'\frac{YX}{X^2-1}
+1088\beta^2h^\flat\frac{X}{X^2-1}\\
&\hspace{30mm}=-1122\beta^2\frac{h^\flat}{X}.
\end{aligned}
\tag{8}
$$
故完整常数载体为
$$
\boxed{K_{h^\flat}=4488i\beta^2
                  \frac{\vartheta(\beta w)^{68}}{X}.}
\tag{9}
$$
它在 $X=\pm1$ 全纯；在 $X=0$ 至少六十六阶零。
在非零 kernel-$\beta$ 点，$(h^\flat)'$ 有三阶零，因而
R261 的另一类 kernel-$\beta$ 简单极在 (9) 中也不存在。
不能对 (8) 的某一项单独使用全纯截面空间。

R259 的下降对象是
$$
\Upsilon_{\beta,k}(\alpha z)
=\frac{y(\beta z)}{x(\beta z)}\Psi_k(z).
$$
由两个反号保证其下降。现在准确有
$$
\Upsilon_{\beta,k}'-\frac{\beta Y}{X}\Upsilon_{\beta,k}
=R_k,\qquad
R_k(\alpha z)=
\frac{y(\beta z)}{\alpha x(\beta z)}\Phi_k'(z).
\tag{10}
$$
右端已经是固定代数椭圆函数，且不含 $C_k$。
将 R259 的 $\mathcal A_\beta=-\vartheta(\beta w)^{69}/\sigma(\beta w)$
与 (2) 同时保留，得到
$$
\nabla_{\mathcal A_\beta}
     (h^\flat F_\beta\Upsilon_{\beta,k})
=-\vartheta(\beta w)^{68}R_k.
$$
等价地，用 (6) 的两个真实 deck 分支直接相加：
$\phi_k''$ 两项抵消，
$$
\left(\frac1{y(t)}-\frac{x(t)^2}{y(t)}\right)\phi_k'
=-\frac{y(t)}{x(t)}\phi_k',
$$
而 $x(t)/(U-1)$ 在 deck 下不变，
$\phi_k+\phi_k\circ T_0=-2c_k$。
所以完整 norm-two 输出为
$$
\boxed{
[\alpha]_*\mathcal I_k
=136\alpha\beta\,\vartheta(\beta w)^{68}\mathcal R_k(w)
-4488i\beta^2c_k\frac{\vartheta(\beta w)^{68}}{x(\beta w)},
\qquad \mathcal R_k=R_k/b_k.
}
\tag{11}
$$
这明确区分了输入侧的 $\phi_k$ 与输出侧的固定常数。

## 3. 四条实际代数源恰为四维真极空间

沿用 R248/R254 的
$$
K_\beta(U)=(4-i)U^4+(-12+20i)U^3
 +(28+10i)U^2+(-20-12i)U-i
$$
和八次 $D_\beta$。R254 给出
$$
-\phi_k''/8=x\,N_k(U)/D_\beta(U)^2,\qquad \deg N_k=15.
$$
存在准确的回文六次多项式
$$
A_k(U)=a_0+a_1U+a_2U^2+a_3U^3+a_2U^4+a_1U^5+a_0U^6,
\qquad a_0=8/3,
$$
使
$$
\boxed{\phi_k'(z)=x(z)y(z)\frac{A_k(U)}{D_\beta(U)}.}
\tag{12}
$$
全部系数在证书中。它们满足完整多项式恒等式
$$
(5U-3)A_kD_\beta
+4U(U-1)(A_k'D_\beta-A_kD_\beta')
=-8N_k.
\tag{13}
$$
由 $x'=2y$、$y'=3x^2-1$，(13) 说明 (12) 两边的导数完全相同。
两边在原点都为零，故差常数也为零；
这不使用不定积分的未知常数。

R248 的实际 division 恒等式又给
$$
K_\beta\!\left(-\frac{(U-1)^2}{4U}\right)
=\frac{K_\beta(U)Q_\beta(U)}{256U^4}.
$$
因此 (10) 准确下降为
$$
\boxed{
\mathcal R_k(w)=x(w)\frac{P_k(x(w)^2)}{K_\beta(x(w)^2)},
\qquad \deg P_k=3,
}
\tag{14}
$$
其中令 $S=2-4V$ 后，
$$
P_k(V)=\frac{\alpha}{256}
\left[a_3+a_2S+a_1(S^2-2)+a_0(S^3-3S)\right].
\tag{15}
$$
四个最高系数均为 $-2\alpha/3$，且
$$
\boxed{
\det\bigl([U^j]P_k\bigr)_{\substack{0\le j\le3\\k=1,3,5,7}}
=\frac{-381681664+1332740096i}{141582897}\ne0.
}
\tag{16}
$$
故这四条实际来源张成整个
$x\,\mathbf Q(i,\sqrt2)[U]_{\le3}/K_\beta(U)$。
证书还逐条核定 $\gcd(P_k,K_\beta)=1$。
十六个非零 kernel-$\beta$ 点因此都是真简单极，
并未被 $\vartheta(\beta w)^{68}$ 的零点支付：
在这些点，$\vartheta(\beta w)$ 非零。

## 4. 原未扭曲 frame 中的完整共轭十七迹

令
$$
\mathcal B_{\rm old}=x\sigma^{68}.
$$
未扭曲 degree-$68$、全局 $i=-1$ 的全纯空间恰为
$$
\mathcal B_{\rm old}\,\mathbf Q(i)[U]_{\le16}.
\tag{17}
$$
这些十七个截面分别有除子
$(4n+2)T_0+(66-4n)O$。
R229 的椭圆正规四次基中，$i=-1$ 部分也恰有十七维，
故它们构成全基。允许非零 kernel-$\beta$ 的简单极以后，
除以 $\mathcal B_{\rm old}$ 的函数在 $i$ 下不变，必为 $U=x^2$ 的有理函数；
原点次数界给出相应空间
$$
\mathcal B_{\rm old}\,
\frac{\mathbf Q(i)[U]_{\le20}}{K_\beta(U)}.
\tag{18}
$$
这里共轭迹不自动消极：$\bar\beta$ 在 $E_0[\beta]$ 上可逆，
每个像点只有一个有极的实际 trace 分支。

先对四个单项式来源
$$
Z_j(w)=\vartheta(\beta w)^{68}
              \frac{x(w)U^j}{K_\beta(U)},\quad 0\le j\le3
$$
计算。记
$$
[\bar\beta]_*Z_j=
\mathcal B_{\rm old}\frac{N_j(U)}{K_\beta(U)},\qquad\deg N_j\le20.
\tag{19}
$$
所有线丛同构采用原 sigma/theta division 公式，因此完整有限平坦迹是
$$
\boxed{
\frac{N_j(t)}{K_\beta(t)}
=t^{16}\operatorname{Tr}_{\,UQ_{\bar\beta}^4-tK_{\bar\beta}^4=0}
\left[
\left(\frac{Q_\beta}{Q_{\bar\beta}}\right)^{68}
\frac{UQ_{\bar\beta}^2}{K_{\bar\beta}^2}
\frac{U^j}{K_\beta}
\right].
}
\tag{20}
$$
例如分母 frame 的准确比值来自
$$
\mathcal B_{\rm old}(\bar\beta w)
=x(w)\sigma(w)^{1156}
          Q_{\bar\beta}(U)^2K_{\bar\beta}(U)^{66}.
$$
这支付了整个 Gaussian/line-bundle 因子，未使用 norm-five 可逆 Weil
算子替代导子十七处的迹。

(18) 已给二十次界。证书用 $t=2,\ldots,22$ 的全部真实纤维确定
四个 $N_j$，另核 $t=23$；每个纤维含全十七个分支。
全部八十四个系数和固定纤维值均在证书内。

在规定的 frame 中作以下唯一拆分：
$$
r_j\equiv U^{-17}N_j\pmod{K_\beta},\quad\deg r_j\le3,\qquad
h_j=\frac{N_j-U^{17}r_j}{K_\beta},\quad\deg h_j\le16.
$$
于是
$$
\boxed{
[\bar\beta]_*Z_j=
\underbrace{\vartheta^{68}x\,\frac{r_j(U)}{K_\beta(U)}}_{\mathcal P_j}
+\underbrace{\mathcal B_{\rm old}h_j(U)}_{\mathcal H_j}.
}
\tag{21}
$$
这是固定的完整极补偿，不是把 (19) 擅自当作全纯向量。
四个极部列的行列式为
$$
\boxed{
-14025078035013399710106447819907758603370496
-20906948623622459195189735880607838911856640i\ne0.
}
\tag{22}
$$
所以四条真极来源经该迹仍无非零固定线性组合能整体消去极部。

对实际四条 $P_k$ 线性组合，记所得极部与全纯部分分别为
$\mathcal P_k,\mathcal H_k$。此处下标 $k$ 总是角色标签，
它们的全部四次、十六次坐标均在证书中。

## 5. 原二处投影、四八次伴随及实际质量

使用 [R229](R229-original-heisenberg-companion-projectors-and-complete-mellin.md)
的原 degree-$4$ 坐标
$$
T=\sigma^4(U+1),\quad F_0=\sigma^4(U-1),\quad G_0=2x\sigma^4
$$
以及原 Mumford lifts $M,N$。准确有
$$
M^2:(T,F_0,G_0)\mapsto(T,G_0,F_0),\qquad
N^2:(T,F_0,G_0)\mapsto(T,-G_0,-F_0).
$$
因而
$$
\Pi_0=\tfrac14(1+M^2)(1+N^2)
\tag{23}
$$
是原实际二处投影。对 (17) 的单项式，
$$
\mathcal B_{\rm old}U^n
=\frac{G_0}{2^{17}}(T+F_0)^n(T-F_0)^{16-n}.
\tag{24}
$$
(23)、(24) 给出证书中完整的 $4\times17$ 有理矩阵。
其目标基准确是
$$
\frac{\vartheta(2z)^{17}}{x(2z)}x(2z)^{-2j},\qquad0\le j\le3.
$$
证书对这四个原基逐列回乘得到单位矩阵，因此没有未知二处标量。

令 $H_j$ 为
[R235](R235-original-octic-sources-and-regularized-seven-dimensional-companion.md)
按首项归一的四条实际八次线，$j=1,3,5,7$。
全体来源作共同 $[2]$ 后，记
$$
\boxed{
Y_k(z)=(\Pi_0\mathcal H_k)(2z)
=\sum_{j=1,3,5,7}\mathsf M_{jk}H_j(2z).
}
\tag{25}
$$
这里的 $\mathsf M$ 是实际完整矩阵，全部十六项在证书中。
它的每一项均非零，且
$$
\boxed{
\Re\det\mathsf M=
\frac{
314987986061305563255536449613594243934377348980941524338647101434702493201
}{
1541701225813870003707943370125679142734370177024
}>0.
}
\tag{26}
$$
所以四条新的全纯部分完整覆盖原四八次伴随。
每个投影的共同尺度质量是 $16\mathsf M_{jk}$，
全部质量在证书中准确保存。

极部也经过同一个实际算子，定义
$$
\mathcal P_k^0(z)=(\Pi_0\mathcal P_k)(2z).
\tag{27}
$$
它不是零。四个 half-period 平移后的极支持互不相交：
非零 $\beta$ 挠点与其三个非零二挠平移不可能重合。
在原非零 $\beta$ 挠点上，(23) 只有恒等分支有极，其系数为 $1/4$。
所以 (22) 也证明四条 $\mathcal P_k^0$ 没有非零固定线性组合整体为零。
证书给出 (27) 的准确原点二阶质量；没有只保存全纯部分的质量。

## 6. 固定常数的真实 CM 像及其原投影

与 (20) 同样计算完整常数载体，准确得到
$$
\boxed{
[\bar\beta]_*
\left(\frac{\vartheta(\beta w)^{68}}{x(\beta w)}\right)
=c_{\rm CM}\frac{\vartheta(\beta z)^4}{x(\beta z)},\qquad
c_{\rm CM}=\frac{79913895-49408994i}{2^{30}}.
}
\tag{28}
$$
目标多项式是
$$
\frac{\vartheta(\beta z)^4}{x(\beta z)}
=\mathcal B_{\rm old}\,(Q_\beta K_\beta)^2.
$$
证书在同样二十二个完整纤维上核定 (28)，并直接使用 (23) 得到
$$
\boxed{
\Pi_0\!\left(\mathcal B_{\rm old}(Q_\beta K_\beta)^2\right)=0.
}
\tag{29}
$$
这是真实常数行的准确零，不是从一般不适用条件逆推零。

如果在原二处投影以前保留该 CM 行，其中央函数也不能漏掉缩放。
令
$$
\gamma_0(z)=\frac{\vartheta(z)^4}{x(z)z^2},\qquad\gamma_0(0)=1,\quad
q_2=2^{p-1},\quad U_{\beta,p}=\beta^{p+1}/17.
$$
在共同 $[2]$ 尺度上，
$$
J_{272c_0}\!\left(
z^{-2}\frac{\vartheta(2\beta z)^4}{x(2\beta z)};u\right)
=4\beta^2 q_2^uU_{\beta,p}^{\,u}J_{4c_0}(\gamma_0;u).
\tag{30}
$$
因此 (11) 常数项的未投影中央贡献是
$$
-17952i\beta^4c_kc_{\rm CM}\,
 q_2^uU_{\beta,p}^{\,u}J_{4c_0}(\gamma_0;u).
\tag{31}
$$
其导数包括 $J_{4c_0}'(\gamma_0;0)$ 和
$\log_pq_2+\log_pU_{\beta,p}$。
(29) 消去的是整个真实来源，故原八次行中 (31) 全部为零；
不能只保留其中一个固定对数再用线性独立性。
本篇没有给 $\gamma_0$ 添加未经证明的椭圆曲线算术身份。

## 7. 保完整输入与全部极补偿的原来源等式

综合 (11)、(21)、(25)、(29)，定义实际输入行
$$
\mathcal J_k(z)=
\left(\Pi_0[\bar\beta]_*[\alpha]_*\mathcal I_k\right)(2z).
$$
则完整原来源等式为
$$
\boxed{
\mathcal J_k
=136\alpha\beta\,(Y_k+\mathcal P_k^0),\qquad
Y_k=\frac{\mathcal J_k}{136\alpha\beta}-\mathcal P_k^0.
}
\tag{32}
$$
在 (32) 中，$\mathcal I_k$ 始终是 (5) 或完全展开的 (6)，
并非只取其 $\phi_k''$ 一项。
特别，先把原 $\nabla_{G_\beta}^2$ 单独作转置，会在 $T_0$ 引入
Laurent 二阶项；原 $4692$ 补偿正是其抵消的一部分。
(6) 给出保留抵消后的真实表达，(32) 再保留余下全部 $\beta$ 极。

取 R235 的原八次系数列 $\mathbf a,\mathbf b$，置
$$
\lambda_A=\mathsf M^{-1}\mathbf a,\qquad
\lambda_B=\mathsf M^{-1}\mathbf b.
$$
全部八个系数在证书中，并已逐项回乘。
令 $\kappa_4=2^{-1/4}$，$Q_{+,0}$、$\operatorname{Reg}$ 为
R231/R235 已付出的实际运输与唯一原次数恢复，
$$
\widetilde Y_k=\operatorname{Reg}
                      (\kappa_4^{-1}Q_{+,0}Y_k).
$$
于是
$$
\boxed{C_A(2z)=\sum_k\lambda_{A,k}Y_k,}
$$
$$
\boxed{
C_B(2z)=\sum_k\lambda_{B,k}\widetilde Y_k
+a_{17}L_1(2z)+a_{289}L_2(2z)+a_{4913}L_3(2z).
}
\tag{33}
$$
$L_\ell$ 和三个 $a$ 完全沿用 R235 式 (23)、(27)。
所以 (33) 包含其原两个 CM 次数补偿和三个 primitive 四次来源，
没有新增可任意保留的 CM 常数。

## 8. 完整中央关系、共同尺度与解析盘

自然输入 (6) 的次数为 $2312$，norm-two 输出次数为 $1156$；
共轭十七迹后次数为 $68$。全体共同 $[2]$ 后相应次数是
$9248,4624,272$。这里的实际半特征已在第 1 节改变并支付，
没有在 degree-$1156$ 处直接把新旧线丛等同。

在目标 gauge
$$
c=272c_0,\qquad d=p+1,\qquad
\Theta_2=\vartheta(4z)^{17},\qquad
W_0=z\Theta_2'/\Theta_2-dcz^d
$$
上，对本篇任何一个原点至少二阶零的完整来源 $V$，置
$$
f_V=J_c(z^{-2}V),\quad
g_V=J_c(W_0z^{-2}V),\quad
h_V=J_c((W_0^2+zW_0'-W_0)z^{-2}V).
$$
保留全部负移权的准确二阶行是
$$
\begin{aligned}
\mathfrak M_2(V;u)={}&(du+1)(du+2)f_V(u)
+du(d-3-2du)f_V(u-1)\\
&+d^2u(u-1)f_V(u-2)-2(du+1)g_V(u)
+2dug_V(u-1)+h_V(u)\\
={}&J_c(\nabla_{\Theta_2}^2V;u).
\end{aligned}
\tag{34}
$$
特别 (32) 给出完整输入侧表达
$$
\boxed{
\mathfrak M_2(Y_k;u)=
\frac{\mathfrak M_2(\mathcal J_k;u)}{136\alpha\beta}
-\mathfrak M_2(\mathcal P_k^0;u).
}
\tag{35}
$$
所有乘子在 $\mathcal J_k$ 中作为真实源保留；(35) 不把 $J$ 与
有限 trace、投影、乘法或换连接擅自交换。

对 R229/R254 原 $A=A_{17}(2z)/16$、$B=A_{34}(z)$，得到
$$
\boxed{
q_2^uJ_{68c_0}(A;u)=
\beta_AJ_c(\Theta_2;u)
+\frac1{16}\sum_k\lambda_{A,k}\mathfrak M_2(Y_k;u),
}
$$
$$
\boxed{
\begin{aligned}
q_2^uJ_{68c_0}(B;u)={}&
\beta_BJ_c((\Theta\rho)(2z);u)\\
&+\frac1{16}\left[
\sum_k\lambda_{B,k}\mathfrak M_2(\widetilde Y_k;u)
+\sum_{\ell=1}^3a_\ell\mathfrak M_2(L_\ell(2z);u)\right].
\end{aligned}
}
\tag{36}
$$
这里 $\beta_A=34/1155$、$\beta_B=2261/81920$；
$1/16$ 同时支付原 $1/4$ 和共同双倍的二阶链式因子。
证书核定两条完整伴随质量分别为
$-272/1155$、$-2261/10240$，准确抵消 (36) 的参考质量。

例如 (34) 的完整中央导数为
$$
\begin{aligned}
\mathfrak M_2'(V;0)={}&
2f_V'(0)+3df_V(0)+d(d-3)f_V(-1)-d^2f_V(-2)\\
&-2g_V'(0)+2dg_V(-1)+h_V'(0),
\end{aligned}
\tag{37}
$$
其中 $g_V(0)=0$。原极补偿的 $f(-1),f(-2)$ 和两个连接行
仍在 (35)、(37) 内，没有把它们当作固定常数。

除固定有限坏素位后，所有 $\beta$、$\bar\beta$、二挠点均为
prime-to-$p$ 挠点。$\mathcal P_k^0$ 的极支持避开原点，
而 (32) 的代数输出也在原点正则。
对输入 (6) 的各真实 trace 分支，原对数的奇点带非零
$\beta$ 挠分量；原点分支的十七分量却在
$E_0[\bar\beta]$，二者交集仅为零，故没有对数奇点落到原点。
在二挠点处可能出现的连接极已由 (6)、(8) 的完整抵消支付。
因此可在 R54/R254 的同一形式盘上使用 (34)；
固定有理极离开该盘，对数原函数使用 R254 的积分估计即可。

本篇从原对数的实际一阶导数恢复了原四八次伴随。
等式 (22)、(27)、(35) 同时指出仍须使用的完整极补偿，
而 (28)、(29) 说明为何这次降阶没有留下一个独立的 $c_k$ 中央项。
原无穷素数非零问题仍要求证明 (36) 中完整行的非零，
不能由 (16)、(26) 或固定对数线性独立单独推出。

## 9. 可重现证书

- 脚本：[check-flat-lowering-original-octic-and-full-poles.py](../scripts/check-flat-lowering-original-octic-and-full-poles.py)
- 全部准确数据：[check-flat-lowering-original-octic-and-full-poles.json](../scripts/check-flat-lowering-original-octic-and-full-poles.json)

脚本运行结果为 **41 项 PASS**，完整保存全部 raw、polar、holomorphic、
原八次、CM 和中央质量；JSON 为 67494 字节。
计算只使用固定四维、十七维多项式及实际十七点纤维，
不构造 level-$4624$ 的稠密矩阵，也不以有限素数实验代替无穷结论。

