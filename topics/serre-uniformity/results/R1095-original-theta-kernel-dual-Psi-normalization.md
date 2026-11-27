# R1095 — 原 theta 核的完整逆配对与 Ψ 的精确对偶归一

**状态：已证明。** 本条证明原对称核在完整空间上可逆，并把原
$\Psi$ 的逆配对范数准确固定为 $1$。这个配对不是 R1041 的
$B(c_0,c_0)$；不据此宣称原 bare 高系数、$e$ 或 $K_4$ 为单位。

日期：2026-11-27。会话：Astra-serre-24b8836b-20261126 / o2_high_coefficient。

## 1. 同一个原核与完整有限空间

保持 [R1061](R1061-actual-genus-two-etale-cover-and-original-three-torsion-Petri-point.md)
§§17–21 的全部原规范：
$$
p=6k-1\ge41,\qquad m=(p-1)/2=3k-1,\qquad
E:\ V^2=U^3+v^2,\quad v^2=-108,
$$
$$
\omega=\frac{dU}{2V},\qquad Q=(0,v),\qquad v^p=-v,\qquad
H=L((p+1)O),\qquad V_0=L((p-1)O).
\tag{1095.1}
$$
基域可取 $\overline{\mathbf F}_p$。所有 Cartier 均为原相对 Cartier，
对 base 常数线性；下文不用绝对 Cartier 的半线性代替它。

原 Miller 核满足
$$
J(T,R)=(U(T)^p-U(R))K(T,R)=J(R,T)\in H\otimes H,
$$
$$
\operatorname{div}(J)=
\Gamma_{T=-FR}+\Gamma_{R=-FT}
 -(p+1)(O\times E+E\times O).
\tag{1095.2}
$$
$K$ 的 $T=O$ 刚化首项为 $z_T^{p-1}$，系数准确为一。
这里 $F$ 是原 Frobenius，$[p]=-F^2$。

对 $f\in V_0,g\in H$，R1061 (1061.79) 定义真实双线性读数
$$
C_{\rm rel}(fg\omega)=\{A(f,g)U'+B(f,g)\}\omega'.
\tag{1095.3}
$$
这些乘积只有 $O$ 极、极阶至多 $2p$，所以没有遗漏第三种
Cartier 输出。写 $A_f=A(f,-),B_f=B(f,-)\in H^*$，
并令 $J^\#:H^*\to H$ 为第一变量的 tensor 收缩。
原 (1061.83) 给
$$
J^\#A_f=\mathscr T_F(f),\qquad
J^\#B_f=-U\,\mathscr T_F(f).
\tag{1095.4}
$$
$\mathscr T_F:V_0\to V_0$ 是原相对变换。
R1061 §18 已用实际 FM/finite duality 证明它可逆，
并在当前 $\mathbf F_p$ 模型识别中满足
$\mathscr T_F^2=[-1]^*$。这里没有从核的点值互易式
直接假设变换可逆。

## 2. 完整 J 的可逆性

由 (1095.4)，$J^\#$ 的像同时包含 $V_0$ 与 $UV_0$。
准确的函数基是
$$
\begin{aligned}
V_0&=\langle 1,U,\ldots,U^m,\ V,VU,\ldots,VU^{m-2}\rangle,\\
H&=\langle 1,U,\ldots,U^{m+1},\ V,VU,\ldots,VU^{m-1}\rangle.
\end{aligned}
$$
$UV_0$ 补上 $U^{m+1}$ 与 $VU^{m-1}$ 两个缺少的单项式，故
$$
V_0+UV_0=H.
$$
因此 $J^\#$ 满射。它的定义域和值域同为 $p+1$ 维，所以
$$
\boxed{\quad J^\#:H^*\xrightarrow{\sim}H.\quad}
\tag{1095.5}
$$
这一步没有把退化的 $A|_H$ 当作完美配对。

定义真正的逆配对
$$
\mathcal B_J(x,y):=(J^\#)^{-1}(x)(y).
\tag{1095.6}
$$
由于 $J$ 对称，这是一条非退化对称双线性形式。
对 $R\ne O$，也有其准确 reproducing identity
$$
\mathcal B_J(g,J(-,R))=g(R).
\tag{1095.7}
$$
(1095.7) 只是原 tensor 的线性代数对偶，不需要再选 period 或 scalar。

## 3. 原 O 首项固定两个完整对偶向量

在原 $O$ 处取
$$
u=U^{-1/2}\sim z_O=-U/V,\qquad
V=-u^{-3}(1+v^2u^6)^{1/2},\qquad
\omega=(1+v^2u^6)^{-1/2}du.
$$
这里固定首项为 $+z_O$ 的平方根。
$z_O=u+O(u^7)$，故下面两个最高系数在这两个原参数中相同；
并不声称它们对任意二阶改参数都不变。

定义
$$
\ell_{p+1}(g)=[u^{-p-1}]g,\qquad
\ell_p(g)=[u^{-p}]g.
\tag{1095.8}
$$
R1061 给原 $\operatorname{PP}_O\Psi=u^{-p}$、
$d\Psi=\delta\omega$，且 $\delta\ne0$。于是令
$h_*=U^{m+1}=u^{-p-1}$，有
$$
H=V_0\oplus \overline{\mathbf F}_p\Psi
       \oplus\overline{\mathbf F}_ph_*,
\quad
\ell_p(\Psi)=1,\quad \ell_{p+1}(h_*)=1,
$$
而其余交叉读数为零。

原 kernel 微分式 (1061.65) 是
$$
D_T\log K=h_{-FR}(T)+\Psi(R),\qquad
h_A(B)=\frac{V(B)+V(A)}{U(B)-U(A)}.
$$
在 $T=O$，
$h_{-FR}(T)=-u^{-1}+O(u)$，
$\omega_T/du=1+O(u^6)$。
结合已经刚化为一的首项，得到
$$
K(T,R)=u^{p-1}\{1+\Psi(R)u+O(u^2)\}.
\tag{1095.9}
$$
$U(T)^p=u^{-2p}$，而 $-U(R)K$ 不影响负次最高两项。
因此
$$
J(T,R)=u^{-p-1}+\Psi(R)u^{-p}+O(u^{-p+1}).
\tag{1095.10}
$$
这两个系数直接给
$$
J^\#\ell_{p+1}=1,\qquad J^\#\ell_p=\Psi.
$$
由 (1095.5) 可逆，完整对偶身份为
$$
\boxed{
\mathcal B_J(1,g)=\ell_{p+1}(g),\qquad
\mathcal B_J(\Psi,g)=\ell_p(g)\quad(g\in H).
}
\tag{1095.11}
$$
特别
$$
\boxed{\mathcal B_J(\Psi,\Psi)=1.}
\tag{1095.12}
$$
同时 $\mathcal B_J(1,1)=0$、$\mathcal B_J(1,h_*)=1$。
所以这里的范数单位来自原 kernel 的实际首项，
不是来自有限域“正定性”，也不是未定单位比例。

## 4. 原退化 A 的准确位置与唯一最高偶边界

仍以 (1061.80) 把 $A$ 延伸到 $H\times H$，置
$$
\mathscr F=J^\#A^\flat,\qquad A^\flat(f)=A(f,-).
$$
则
$$
\mathcal B_J(\mathscr Ff,g)=A(f,g)
=\mathcal B_J(f,\mathscr Fg),\qquad
\mathscr F|_{V_0}=\mathscr T_F.
\tag{1095.13}
$$
由原 $\operatorname{rad}(A)=\overline{\mathbf F}_p\Psi$，
$$
\ker\mathscr F=\overline{\mathbf F}_p\Psi,\qquad
\operatorname{im}\mathscr F=\Psi^{\perp_{\mathcal B_J}}
=\ker\ell_p=V_0\oplus\overline{\mathbf F}_ph_*.
\tag{1095.14}
$$
因 (1095.12)，这是实际正交直和
$$
H=\overline{\mathbf F}_p\Psi\ \perp\ \ker\ell_p.
$$
原 $V_0$ 上的限制仍有
$\operatorname{rad}(\mathcal B_J|_{V_0})=\overline{\mathbf F}_p1$：
由 (1095.4) 把它运输回 $A|_{V_0}$ 即得。
所以不能把原 $A$ 的 radical 删除而不记录所在空间。

还可以把完整空间的 square 缺陷准确限制为一个边界标量。
两条配对都与 $[-1]^*$ 相容，$\mathscr F$ 保奇偶。
(1095.11)、$A(1,h_*)=1$ 给
$\mathscr Fh_*=h_*+w$，其中 $w\in(V_0)_{\rm even}$。
$\mathscr F^2-[-1]^*$ 在 $V_0$ 上为零，在 $\Psi$ 上等于 $\Psi$；
其对 $\mathcal B_J$ 自伴。
减去自伴的 $\Psi\otimes\ell_p$ 后，剩余算子形如
$w_1\otimes\ell_{p+1}$，$w_1\in V_0$。
由 $\ell_{p+1}=\mathcal B_J(1,-)$，自伴性迫 $w_1=c\,1$。
于是有完整身份
$$
\boxed{
\mathscr F^2=[-1]^*
 +\Psi\otimes\ell_p+c\,1\otimes\ell_{p+1}
\quad\text{for one actual }c\in\overline{\mathbf F}_p.
}
\tag{1095.15}
$$
本节暂保完整标量 $c$；§7 用原 extended Cartier 将它准确确定为 $\delta$。
特别，$A(h_*,h_*)=\binom{-1/2}{k}v^{2k}=\beta=-\delta$
并不单独决定 $c$；还须保留 $\mathcal B_J(h_*,h_*)$ 及 mixed terms。

## 5. 原三平移的真实核协变与完整 Gram

本节仍用原 $Q=(0,v)$。定义实际 theta 平移
$$
S f(T)=(V(T)+v)^{2k}f(T+Q).
\tag{1095.16}
$$
其乘子除子为 $(p+1)((-Q)-O)$，
故 $S$ 确实保持整个 $H$。
由原三挠加法律，
$$
\prod_{j=0}^2(V(T+jQ)+v)=-8v^3,
\quad
S^3=(-8v^3)^{2k}=-4v^2=432.
$$
令 $\gamma\in\mathbf F_p^\times$ 为唯一的 $\gamma^3=432$，
则 $\widehat S=S/\gamma$ 满足 $\widehat S^3=1$。

因为 $FQ=-Q$，同时平移两个变量使 (1095.2) 的两条 graph
分别保持；乘子恰校正两轴。故 $(S\otimes S)J$ 与 $J$ 的比为常数。
这个常数也须从原核计算。由 symmetry 与原 $g_{-Q}$，
$$
J(Q,R)=(V(R)-v)^{2k}.
$$
又 $V(R+Q)-v=-4v^2/(V(R)+v)$。
取 $T=O$ 的 $u^{-p-1}$ 系数，得到该常数
$(-4v^2)^{2k}=432^{2k}=\gamma^2$，所以
$$
\boxed{(S\otimes S)J=\gamma^2J,\qquad
\mathcal B_J(\widehat S f,\widehat Sg)=\mathcal B_J(f,g).}
\tag{1095.17}
$$
这里用的是整个 $H$ 的真正逆配对；
没有把 $A$ 或旧 $V_0$ 冒称三平移不变。

由 $\Psi(Q)=0$、$D\Psi=\delta$，
$S\Psi=\delta u^{-p}+O(u^{-p+1})$；
因此准确有 $S\Psi=\delta\Psi+f_0$，$f_0\in V_0$。
对三向量 $\Psi,\widehat S\Psi,\widehat S^2\Psi$，
(1095.11)–(1095.17) 给完整 Gram
$$
\begin{pmatrix}
1&\delta/\gamma&\delta/\gamma\\
\delta/\gamma&1&\delta/\gamma\\
\delta/\gamma&\delta/\gamma&1
\end{pmatrix},
\qquad
\det=(1-\delta/\gamma)^2(1+2\delta/\gamma).
\tag{1095.18}
$$
这条精确式保留了两个实际可能的退化因子。
整个 $\mathcal B_J$ 完美，并不强迫这三个向量张成的轨道子空间非退化；
本条没有证明 $\delta-\gamma$ 或 $\delta+\gamma/2$ 为单位。

## 6. 对原目标的使用范围

(1095.11) 给出三平移后原 $\Psi$ 分量的完全固定投影
$$
g\longmapsto \ell_p(g)\Psi.
$$
其补空间是 $V_0\oplus k h_*$，不是仅 $V_0$。
因此后继可以逐项保留原最高偶边界和 $\Psi$ 分量，
再作真正三分布；不能把 $\mathscr T_F$ 未经比较地扩成一个
与 $S$ 交换的旧空间变换。

本条未把 R1092 的另外六个三挠点单位移到 $Q$ 的低 jet。
它没有证明原 $\eta_k,\nu_k$ 不能同零，
也没有把 (1095.12) 当作原 bare 的 CM kernel 范数。
指定 $e,K_4$、bare 高坐标及共同深盘排除继续需要实际来源比较。

## 7. 原第三类修正与最高偶边界的完整定标

本节证明 (1095.15) 中的实际标量准确为 $\delta$，保留原
relative Cartier、两处极点和 $H$ 的最高两项。

令 $Z=FT$，对一般 $R$ 写
$$
h_Z(R)=\frac{V(Z)+V(R)}{U(R)-U(Z)}.
$$
若 $f\in H$，记 $a=\ell_{p+1}(f)$、$b=\ell_p(f)$。
由 (1095.9)，$fK\omega_T$ 在 $O$ 的前两项为
$$
a u^{-2}du+\{a\Psi(R)+b\}u^{-1}du.
$$
除 $O$ 外，它仅可能在 $T=F^{-1}R$ 有至多 $p$ 阶极。
相对 Cartier 后仅有 $O$、$Z=R$ 两处至多简单极，
留数分别为 $a\Psi(R)+b$ 及其相反数。
这里 Cartier 对 base 的 $R,a,b$ 线性，不对它们取 $p$ 次根。

$h_Z(R)\omega_Z$ 在这两点的留数准确为 $+1,-1$。
因此
$C_{{\rm rel},T}(fK\omega_T)-(a\Psi(R)+b)h_Z(R)\omega_Z$
全纯。其剩余常数也由原 $A$ 唯一固定：
乘 $U(Z)-U(R)$ 后，左边成为 $C_{{\rm rel},T}(fJ\omega_T)$，
而
$$
(U(Z)-U(R))h_Z(R)=-V(Z)-V(R).
$$
$C_{{\rm rel},T}(fJ\omega_T)$ 只有 $O$ 处至多三阶极，
可含 $1,U(Z),V(Z)$；其中 $U(Z)$ 的系数由 (1061.80)
准确为 $J^\#A(f,-)=\mathscr Ff$。
故得到整个 $H$ 的完整公式
$$
\boxed{
\frac{C_{{\rm rel},T}(fK\omega_T)}{\omega_Z}
=\mathscr Ff(R)+
 \{\ell_{p+1}(f)\Psi(R)+\ell_p(f)\}h_Z(R).
}
\tag{1095.19}
$$
这不是把旧 $V_0$ 公式越界延伸；第三类项完整显示在右边。

在 $Z=O$ 仍取 $u_Z=U(Z)^{-1/2}$。
直接展开 $h_Z(R)=u_Z^{-1}+O(u_Z)$，其常数项为零。
所以 (1095.19) 的 regular constant 正是 $\mathscr Ff(R)$。

现在用原 R1061 §§19、21 的
$$
D\mathcal R=\Psi,\qquad D^2\mathcal R=\delta,\qquad
\mathscr T_F(U)=\delta\mathcal R.
$$
原 $\mathcal R=U^2R(U^3)$ 的最高 $U^m$ 系数为一；
因此
$$
g=U\mathcal R\in H,\qquad
\ell_{p+1}(g)=1,\qquad \ell_p(g)=0,\qquad [-1]^*g=g.
$$
对合法的旧输入 $f=U\in V_0$，原 (1061.68) 给全部 extended source：
$$
\frac{C_{{\rm rel},T}(\mathcal R\,U K\omega_T)}{\omega_Z}
=
\frac{(D_R^2+2U(R))\,\mathscr T_F(U)(R)
       +2h_Z(R)D_R\mathscr T_F(U)(R)}{2\delta}.
\tag{1095.20}
$$
该式来自 $\Psi^2=U^p+2\delta\mathcal R$ 与原 kernel 微分式；
左端极界恰为 $H$，没有把 $\mathcal R U$ 冒称旧 $V_0$ 输入。

读取同一个 $Z=O$ 的 regular constant，(1095.19)–(1095.20)
准确给
$$
\boxed{\mathscr F(U\mathcal R)=U\mathcal R+\delta/2.}
\tag{1095.21}
$$
由于 $\mathscr F(1)=1$ 且 $\mathscr F$ 对标量线性，再施一次得
$\mathscr F^2(U\mathcal R)=U\mathcal R+\delta$。
另一方面 (1095.15) 在同一 $g$ 上为 $g+c$，所以
$$
\boxed{
c=\delta,\qquad
\mathscr F^2=[-1]^*
 +\Psi\otimes\ell_p+\delta\,1\otimes\ell_{p+1}.
}
\tag{1095.22}
$$

还有同尺度的二次 Cartier 表述。对 $h_*=U^{m+1}$，
原 Weierstrass 单系数式给
$C_{\rm rel}(h_*\omega)=U'\omega'$：
分子 $U^{m+1}(U^3+v^2)^m$ 只有可读最高指数 $2p-1$，
系数为一；$p-1$ 次因模三角色不存在。
再用 (1061.92) 得
$$
C_{\rm rel}^2(h_*\omega)=-\delta\omega''.
$$
$V_0\omega$ 的首次 Cartier 像全纯，第二次被原 supersingular
Cartier 杀掉；$\Psi\omega=d(\Psi^2/(2\delta))$ 为 exact。
因此对全部 $f\in H$，
$$
\frac{C_{\rm rel}^2(f\omega)}{\omega''}
=-\delta\,\ell_{p+1}(f).
\tag{1095.23}
$$
(1095.22) 的最后一项也可写为
$-1\otimes(C_{\rm rel}^2(-\,\omega)/\omega'')$；
它不是未确定单位倍数。

本节 o2_high_coefficient 推导完整第三类项并用实际
$U\mathcal R$ 定标；o1_theta 独立纸审全部极界、regular constant
和平方常数。没有数学程序执行。
(1095.22) 结算最高偶边界，但并未证明三轨道 Gram
的两个因子或原 $\eta_k,\nu_k$ 的指定读数为单位。


## 原来源与核对

- R1061 (1061.57)–(1061.59)：原全部 graph、Miller 首项与实际相对变换的可逆性。
- R1061 (1061.65)、(1061.76)–(1061.84)：原 kernel 微分、实际对称 tensor、
  有限极界 Cartier 的 $A,B$、radical 与收缩式。
- 本文的可逆性、最高两项及三平移常数均由这些原身份在纸面推出。
  o1_theta 独立核准完整 $J^\#$ 满射、$\Psi$ 的最高系数对偶及范数 $1$，
  并核对 (1095.15) 的唯一最高偶边界与三轨道 Gram 的实际因子。
  全文没有数学程序执行，也没有新有限扫描。
