# R138：原 high97 principal 压缩的完整小余项

2026-11-20，visible-exact-astra-ac637-20261120 / joint_kernel。

**状态：已证明；未执行新科学计算。** 这是 [R138 relative-root 合同](R138-supplement-original-high-compression-and-relative-root-receivers.md)中原全部 high 压缩的一个直接可消费引理。它不提高真实 high 分界，不删除 mean rank 或非局部 primitive，也不假定完整根型非负。

用 moving $\phi$ 的归一 $L^2$。令 $P_H$ 是原 odd-fourfold scalar 的 $j\ge97$ 投影，$n_H=4\cdot97=388$，$N=|D_\phi|$。$a$ 为真实 principal 系数；若使用人工轴矩形顶点，先作 [F.9a](R138-supplement-root-source-elimination-and-concave-finite-gate.md) 的 even-fourfold 投影。于是 $a$ 为实值，$a_n=0$ 除非 $n\in4\mathbb Z$。

## 1. 对称 principal 与乘子的直接差

定义

$$
E_{\rm pr}=\frac12P_H
\{N^{1/3}M_aN^{-1/3}+N^{-1/3}M_aN^{1/3}-2M_a\}P_H.
\tag{HP.1}
$$

若同一实际根全圈 $a\in H^2$，则

$$
\boxed{\quad
\|E_{\rm pr}\|
\le\frac{2^{1/6}}{32}\,n_H^{-4/3}\|a''\|_{L^2}
\le\frac{2^{1/6}}{32}\,n_H^{-4/3}\|a''\|_\infty .\quad}
\tag{HP.2}
$$

这里的 $H^2$、导数与 Fourier 系数都属于同一实际周期系数；理想角 ODE 的高导数不能免费替换 actual 导数。只需 actual $a''$，不需第三导。

**证明。** 在完整复 Fourier 表示中，(HP.1) 的 $(k,l)$ 元素是

$$
a_{k-l}\,d(|k|/|l|),\qquad
d(r)=\frac12(r^{1/3}+r^{-1/3}-2),
\quad |k|,|l|\ge n_H.
\tag{HP.3}
$$

因为 $d(r)=d(1/r)$，可设 $r\ge1$。声称

$$
d(r)\le\frac1{32}(r-1)^{4/3}.
\tag{HP.4}
$$

置 $y=r^{1/3}\ge1$。$r=1$ 时两侧为零。其余情形对 (HP.4) 取三次方并约去正因子，等价于

$$
4096(y-1)^2\le y^3(y^2+y+1)^4.
$$

AM--GM 给右侧至少 $81y^7$；直接求导给

$$
\sup_{y\ge1}\frac{(y-1)^2}{y^7}
=\frac{4\cdot5^5}{7^7}.
$$

所需比较是 $4096\cdot4\cdot5^5<81\cdot7^7$，即
$51200000<66706983$，故 (HP.4) 成立。再用
$\min(|k|,|l|)\ge n_H$ 与 $||k|-|l||\le|k-l|$，有

$$
|d(|k|/|l|)|\le
\frac{|k-l|^{4/3}}{32n_H^{4/3}}.
\tag{HP.5}
$$

因此完整矩阵的 Schur 行、列和均不超过
$(32n_H^{4/3})^{-1}\sum_{n\ne0}|n|^{4/3}|a_n|$。
最后，Parseval 和 Cauchy--Schwarz 给

$$
\begin{split}
\sum_{n\ne0}|n|^{4/3}|a_n|
&\le\left(\sum_{n\in4\mathbb Z\setminus\{0\}}
                         |n|^{-4/3}\right)^{1/2}\|a''\|_{L^2}\\
&=\left(2\,4^{-4/3}\zeta(4/3)\right)^{1/2}\|a''\|_{L^2}
\le2^{1/6}\|a''\|_{L^2}.
\end{split}
$$

末步只用 $\zeta(4/3)\le1+\int_1^\infty x^{-4/3}dx=4$。先对 Fourier 多项式成立，再以显示的绝对行列和收敛延拓到 $H^2$。奇函数实对称子空间上的压缩不增范数，证明 (HP.2)。

## 2. 同一个完整根型的无输入导数展开

这里补齐后续费用所消费的准确对象。沿 [U.2--12](R138-supplement-complete-root-angular-form-and-two-scalar-geometry.md)，所有 frame、位置和角导数均已拉回同一 moving $\phi$。写

$$
\rho=a_{\rm geom}/m,\quad \mathbf T=X-uY,\quad
\mathbf A=\mathbf T'+u'Y,\quad
\mathbf k=\rho\mathbf T/v,\quad
\mathbf b=\rho Y,\quad \mathbf c=-\rho\mathbf A/v.
\tag{HP.6}
$$

对原高输入 $z$，设

$$
f=N^{1/3}z,\quad q=N^{-1/3}z,\quad
R=JN^{-2/3}z,\quad T_s=JN^{-4/3}z;
\qquad R'=-f,\quad T_s'=-q.
$$

以及

$$
\mathbf y=\mathbf kq-\mathbf bR-\mathbf cT_s,\quad
\mathbf e=\mathbf b'R+\mathbf c'T_s,\quad
\ell_z=\mathcal D^{-1}\langle\mathbf e\rangle\cdot\ell,
\quad \mathbf v=\mathbf e-g_m\ell_z.
\tag{HP.7}
$$

这里 $g_m,\mathcal D,\ell$ 是 U.8--12 的完整真实 mean 列、分母和轴，保留已付 $\mathcal D^{-1}<20/17$。U.4 的准确消元给
$\mathcal Rf=\mathbf y'+\mathbf v$。
本题同一 C4/reflection 下，$\mathbf y$ 的水平平均由四重等变为零，竖直分量由 odd 反射为零，故 $\langle\mathbf y\rangle=0$；周期相容式给 $\langle\mathbf v\rangle=0$。因此原环境 primitive 是
$I\mathcal Rf=\mathbf y+I\mathbf v$，没有重设旋转规范。

把此式代入 U.15，并对 $I\mathbf v\times\mathbf y'$ 分部积分，得到

$$
\begin{split}
\mathfrak b_*(f)/(2\pi)={}&
\langle a f q+A_{qq}q^2+A_{RR}R^2+A_{TT}T_s^2
                  +A_{Rq}Rq+A_{qT}qT_s+A_{RT}RT_s\rangle\\
&-2\ell_z\langle G\cdot(\mathbf y\times g_m)\rangle
+\langle G\cdot[(I\mathbf v)\times\mathbf v]\rangle
-\langle G'\cdot[(I\mathbf v)\times\mathbf y]\rangle,
\end{split}
\tag{HP.8}
$$

其中在实际位置 $a=2G\cdot(\mathbf k\times\mathbf b)$，人工顶点则先按 F.9a 投影；其余六个完整系数为

$$
\begin{split}
A_{qq}&=G\cdot(\mathbf k\times\mathbf k'+2\mathbf k\times\mathbf c),\\
A_{RR}&=-G\cdot(\mathbf b\times\mathbf b'),\qquad
A_{TT}=-G\cdot(\mathbf c\times\mathbf c'),\\
A_{Rq}&=-G'\cdot(\mathbf k\times\mathbf b)-2G\cdot(\mathbf b\times\mathbf c),\\
A_{qT}&=-G'\cdot(\mathbf k\times\mathbf c),\qquad
A_{RT}=G'\cdot(\mathbf b\times\mathbf c)+2G\cdot(\mathbf b'\times\mathbf c).
\end{split}
\tag{HP.9}
$$

为核 (HP.8)，先得
$\langle G\cdot(\mathbf y\times\mathbf y'+2\mathbf y\times\mathbf v)\rangle$ 加显示的两个 primitive 项。代入 (HP.7)，用 $R'=-f,T_s'=-q$ 把唯一的 $q'$ 项分部积分；逐项展开即为 (HP.9)。均值产生的项准确是所示 $-2\ell_z$ 项。此推导不对未知 high 输入作范数意义的角导。

上述恒等式先对有限 Fourier 实输入成立。下面显示的全部项均有 $L^2_z$ 有界延拓，故按该同域稠密逼近得到完整 high 算子；实际弱核与此能量型的识别仍沿 V/F 的同对象弱解资格，不另授边值正则性。

## 3. 与完整 compact 部分相接

在既定无输入导数展开中，记

$$
q_H=n_H^{-1/3},\quad r_H=n_H^{-2/3},\quad t_H=n_H^{-4/3},
$$

以及同一实际全圈系数界 $k_0,b_0,c_0,b_1,c_1,g_0,G_0,G_1$、完整 mean 逆界 $d_D=20/17$。令

$$
Y_H=k_0q_H+b_0r_H+c_0t_H,\quad
E_H=b_1r_H+c_1t_H,\quad
L_H=d_DE_H,\quad V_H=(1+g_0d_D)E_H.
$$

对原七局部项中主项以外的六个系数 $A_{qq},A_{RR},A_{TT},A_{Rq},A_{qT},A_{RT}$，原 compact 展开的直接界在两个输入都取原 high 时是

$$
\begin{split}
\epsilon_{\rm comp,H}={}&
\|A_{qq}\|_\infty q_H^2+\|A_{RR}\|_\infty r_H^2
+\|A_{TT}\|_\infty t_H^2\\
&+\|A_{Rq}\|_\infty r_Hq_H
+\|A_{qT}\|_\infty q_Ht_H
+\|A_{RT}\|_\infty r_Ht_H\\
&+2G_0g_0L_HY_H+G_0V_H^2+G_1V_HY_H.
\end{split}
\tag{HP.10}
$$

倒数第三项是完整 mean rank；最后两项来自原环境 primitive，使用的是 $\|I\|\le1$，不冒用 scalar 四重 $1/4$。对每个高输入的二次型逐项估计给 (HP.10)，自伴性使其等价于完整高压缩算子范数上界。没有只取 diagonal Fourier 元素。

若 $D_H$ 为同一完整根型的原 high 压缩，则

$$
\boxed{\quad
D_H\succeq
\left[a_{\min}
-\frac{2^{1/6}}{32}n_H^{-4/3}\|a''\|_\infty
-\epsilon_{\rm comp,H}\right]I.
\quad}
\tag{HP.11}
$$

它是一个只需全角 scalar 系数界的新入口。所列 actual 系数、mean 和 primitive 费用必须完整支付；本文没有声称该右侧已正。如果直接门不分离，仍使用 relative-root 合同的完整 finite-high/无限尾压缩和 shorted 逆，不改变原 low96/high97。

## 4. 只付平方项负部的更紧单侧门

若只求 $D_H$ 的下界，不必支付正平方系数。令
$A^-:=\max(0,-A)$。在 (HP.10) 中将前三个系数范数分别换成
$\|A_{qq}^-\|_\infty,\|A_{RR}^-\|_\infty,\|A_{TT}^-\|_\infty$，其余项完整不变，所得量记为 $\epsilon^-_{\rm comp,H}$。由于 $q^2,R^2,T_s^2\ge0$，直接从 (HP.8) 得更紧的

$$
D_H\succeq
\left[a_{\min}-\frac{2^{1/6}}{32}n_H^{-4/3}\|a''\|_\infty
-\epsilon^-_{\rm comp,H}\right]I.
\tag{HP.12}
$$

这是单侧型下界；$\epsilon^-_{\rm comp,H}$ **不宣称**是 compact 算子范数或一侧输出尾范数。计算有限矩阵以外的交叉/尾时，不能把它冒用为两侧误差。

对往往最大的 $A_{qq}$，可先用真实几何恒等式减少三角损失。记几何量 $b_{\rm geom}=a'_{\rm geom}/e$、$\vartheta=v/m$、$\sigma=G\cdot n$，则 U.6 给

$$
\mathbf A=\vartheta b_{\rm geom}(Y+uX)
                      +\vartheta(Z_X-uZ_Y).
$$

由 $X\times Y=-n$、$\mathbf T\times Y=-n$ 和
$\mathbf T\times(Y+uX)=-(1+u^2)n$，准确得到

$$
\boxed{\quad
A_{qq}=\frac{\rho^2}{v^2}
\left\{[\vartheta b_{\rm geom}(1+u^2)+u']\sigma
-\vartheta G\cdot[\mathbf T\times(Z_X-uZ_Y)]\right\}.
\quad}
\tag{HP.13}
$$

具体地，$\mathbf k\times\mathbf k'+2\mathbf k\times\mathbf c
=-\rho^2v^{-2}\mathbf T\times(\mathbf A+u'Y)$，即为所示式。完整实际 $Z$ 保留，不能用理想平行 frame 令它为零。消费者可在每个真实全角 box 对 (HP.13) 先作 signed 包围，再取负部；不需先取 $k_0k_1+2k_0c_0$ 的粗绝对值。是否有负部和 (HP.12) 是否分离，均留给新的公开计算。
