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



## 8. 原 Miller 乘法、完整 Cartier 极化与显式核

本节仍在同一个特征 $p$ 的原模型上工作。记
$J_P(T)=J(T,P)$。点 $P,R$ 起初取 generic，避开弦线、竖线
及标记点碰撞；最后所有等式按有理函数恒等式延拓。
不在推导中把一个趋零因子与另一极因子分别取值。

### 8.1 刚化弦线与原 Miller 的确切乘法

对一般点 $A,B$，令
$$
m_{A,B}=\frac{V(B)-V(A)}{U(B)-U(A)},\qquad
b_{A,B}=V(A)-m_{A,B}U(A),
$$
$$
L_{A,B}(T)=
-\frac{V(T)-m_{A,B}U(T)-b_{A,B}}{U(T)-U(A+B)}.
\tag{1095.24}
$$
这是原 normalized chord：
$$
\operatorname{div}L_{A,B}=(A)+(B)-(A+B)-(O),\qquad
L_{A,B}=u_T^{-1}(1+O(u_T)).
$$
负号由原 $V(T)=-u_T^{-3}+O(u_T^3)$ 固定，不能省去。

原 Miller 函数 $g_A$ 的除子为
$([p]A)-p(A)+(p-1)(O)$，$O$ 首项为 $u_T^{p-1}$、系数一。
逐项比较除子与这个首项，直接得到
$$
\frac{g_A(T)g_B(T)}{g_{A+B}(T)}
=
\frac{L_{[p]A,[p]B}(T)}{L_{A,B}(T)^p}.
\tag{1095.25}
$$
这是有理函数的确切等式。其 divisor/刚化证明本身也适用于
特征零的 Miller 函数；本节只把它直接用于已经定义的原特征
$p$ 函数，并没有从特征零 sigma 展开删掉 first-$p$ 项。

取 $A=F^{-1}P,B=F^{-1}R$，只在证明弦线身份时可作相应的
纯不可分基域扩张。$[p]=-F^2$ 给
$$
\frac{K(T,P)K(T,R)}{K(T,P+R)}
=
\frac{L_{-FP,-FR}(T)}
     {L_{F^{-1}P,F^{-1}R}(T)^p}.
\tag{1095.26}
$$
右边分母的 $p$ 次幂已在原 base 上定义。相对 Cartier 运输它时，
准确得到 $L_{P,R}(Z)$，其中 $Z=FT$；不是对 base 常数再取
$p$ 次根。

### 8.2 全部乘积的相对 Cartier

在本小节写
$$
m=m_{P,R},\qquad b=b_{P,R},\qquad S=P+R.
$$
弦线第三交点为 $-S$，所以
$V(S)+mU(S)+b=0$。由 (1095.24) 严格有
$$
L_{-FP,-FR}(T)=-h_{-FS}(T)-m^p.
\tag{1095.27}
$$
原 R1061 (1061.65) 给
$D_T\log K(T,S)=h_{-FS}(T)+\Psi(S)$。
因此 $C_{\rm rel}(dK)=0$ 与原
$C_{{\rm rel},T}(K(T,S)\omega_T)=\omega_Z$ 给
$$
C_{{\rm rel},T}\!\left(
 K(T,S)\{-h_{-FS}(T)-m^p\}\omega_T\right)
=\{\Psi(S)-m^p\}\omega_Z.
$$
这里 $m^p$ 是 base 函数，Cartier 对它线性。
再用原完全归一的加法律
$\Psi(P+R)=\Psi(P)+\Psi(R)+m^p$，(1095.26) 成为
$$
\boxed{
C_{{\rm rel},T}\bigl(K(T,P)K(T,R)\omega_T\bigr)
=\frac{\Psi(P)+\Psi(R)}{L_{P,R}(Z)}\,\omega_Z.
}
\tag{1095.28}
$$

把 $J(T,P)=(U(T)^p-U(P))K(T,P)$ 的两个 $p$ 次因子
完整提出 Cartier。弦线的确切范数是
$$
\{V(Z)-mU(Z)-b\}\{V(Z)+mU(Z)+b\}
=(U(Z)-U(P))(U(Z)-U(R))(U(Z)-U(S)).
$$
所以得到整个乘积，而不只是其中一个系数：
$$
\boxed{
C_{{\rm rel},T}(J_P(T)J_R(T)\omega_T)
=-(\Psi(P)+\Psi(R))
 \{V(Z)+mU(Z)+b\}\omega_Z.
}
\tag{1095.29}
$$
$J_PJ_R\omega$ 的极界为 $2p+2$；输出允许 $1,U(Z),V(Z)$
三个方向。本式保留了全部三个方向，没有套用只适用于
$V_0\times H$ 的二项输出。

### 8.3 原完整变换的显式极化核

读取 (1095.29) 的 $U(Z)$ 系数，得到
$$
\boxed{
(\mathscr FJ_P)(R)
=A(J_P,J_R)
=-\frac{V(R)-V(P)}{U(R)-U(P)}
       \{\Psi(P)+\Psi(R)\}.
}
\tag{1095.30}
$$
这就是原完整变换的实际极化核；不是另选同角色的 theta 核。

它还可完全写成两个 divided polynomials。用原
$$
\Psi=V\,r(U),\qquad r(U)=U S(U^3),\qquad
q(U)=(U^3+v^2)r(U),
$$
则 (1095.30) 等于
$$
\boxed{
-\frac{q(U(P))-q(U(R))}{U(P)-U(R)}
+V(P)V(R)
 \frac{r(U(P))-r(U(R))}{U(P)-U(R)}.
}
\tag{1095.31}
$$
两分子都被分母整除。因而 (1095.31) 也明确支付了竖线与
对角处的延拓；没有保留人为的 $0/0$ 例外。
这里 $\deg r=m-1,\deg q=m+2$，第一项在每个变量中的
最高 $U$ 次数为 $m+1$，第二项的最高 $V U$ 次数不超过
$V U^{m-2}$，与整个 $H$ 的极界一致。

### 8.4 两处第三类项给独立的完整平方核

以下计算作为 (1095.22) 的独立来源核对，同时保留后继三分布
所需的极点。固定一般 $P$，令
$$
\mathcal T_P(Z,R)=
\frac{C_{{\rm rel},T}(h_{-P}(T)K(T,R)\omega_T)}{\omega_Z}.
$$
源在 $T=-P$ 有简单极，在 $T=F^{-1}R$ 至多有 $p$ 阶极；
在 $O$ 的阶为 $p-2$，所以输出在 $O$ 正则。
相对 Cartier 后两处留数分别为 $K(-P,R)$ 及其相反数。
因此减去
$K(-P,R)\{h_{-FP}(Z)-h_R(Z)\}$
后全纯。

其常数由原 $O$ frame 固定：
$h_{-P}(T)=-u_T^{-1}+O(u_T)$，
而 (1095.9) 的下一项为 $\Psi(R)u_T$。
源 $u_T^{p-1}du_T$ 的系数准确为 $-\Psi(R)$；
两条 $h$ 的差在 $Z=O$ 常数为零。故
$$
\boxed{
\mathcal T_P(Z,R)
=-\Psi(R)+K(-P,R)\{h_{-FP}(Z)-h_R(Z)\}.
}
\tag{1095.32}
$$
这些留数的 base 常数仍保持不变，未换成绝对 Cartier。

置
$G_P(T)=(\mathscr FJ_P)(T)
       =-h_{-P}(T)(\Psi(T)+\Psi(P))$。
它确在 $H$ 中，最高两项为
$\ell_{p+1}(G_P)=1,\ell_p(G_P)=0$。
原 R1061 (1061.66) 对这个完整有理源给
$$
\frac{C_{{\rm rel},T}(G_P(T)K(T,R)\omega_T)}{\omega_Z}
=-(D_R+h_Z(R)+\Psi(P))\mathcal T_P(Z,R).
\tag{1095.33}
$$
这里使用的是未丢第三类项的 kernel 微分式。

写
$a_Z=h_{-FP}(Z),\ h=h_R(Z),\ b_R=h_{-FP}(R)$。
原对称变量微分给
$$
D_R\log K(-P,R)=-\Psi(P)-b_R,\qquad h_Z(R)=-h.
$$
把 (1095.32) 代入 (1095.33)，右边准确化为
$$
\delta-h\Psi(R)+\Psi(P)\Psi(R)
+K(-P,R)\{(b_R+h)(a_Z-h)+D_Rh\}.
$$
在 $Z=O$，
$$
\begin{aligned}
h&=-u_Z^{-1}-U(R)u_Z+O(u_Z^2),\\
a_Z-h&=(U(R)-U(P)^p)u_Z+O(u_Z^2),\\
D_Rh&=O(u_Z).
\end{aligned}
$$
故正规常数为
$$
\delta+\Psi(P)\Psi(R)
 +K(-P,R)(U(P)^p-U(R)).
$$
依 (1095.19)，这正是 $\mathscr F G_P(R)$。于是
$$
\boxed{
(\mathscr F^2J_P)(R)=J(-P,R)+\Psi(P)\Psi(R)+\delta.
}
\tag{1095.34}
$$
由于 $J^\#$ 完美，这些 $J_P$ 张成 $H$；
(1095.34) 因而再次给出 (1095.22)，包括精确的最高偶常数
$\delta$，并展示了该常数来自哪里。

### 8.5 原两条短障碍的三平移读数

令 $f=U^m$，仍用原 $Q=(0,v)$ 和 (1095.16) 的 $S$。
在 $-Q$，原 Picard 一阶参数满足
$D_R\mathscr T_F(f)(-Q)=e$。
最高两项对偶、或直接对原 $J$ 微分，给
$$
D_RJ(T,-Q)=S\Psi(T).
$$
四阶不能省去 theta multiplier 的修正。用与原不变微分相容、
且 $u=t+O(t^7)$ 的局部参数，有
$$
t^{p+1}(V(t)+v)^{2k}=1-\frac v3t^3+O(t^6).
$$
在这里另记 $\ell_{p-3}(g)=[u^{-p+3}]g$。
又 $J^\#\ell_{p-3}=\mathscr T_F(U^2)$，因为
$A(U^2,g)=\ell_{p-3}(g)$。从同一四阶读数准确得到
$$
D_R^4J(T,-Q)
=24S\mathscr T_F(U^2)(T)-8vS\Psi(T).
$$
因此 (1061.74) 的完整四阶式给
$$
\boxed{
e=A(f,S\Psi),\qquad
A\!\left(f,S\mathscr T_F(U^2)\right)
=ve+\frac{\delta^2}{6}K_4.
}
\tag{1095.35}
$$
这两条等式定位了真正的三平移配对，未把曲线族的 normal
导数、另外六个三挠点值或一般 evaluation 代入。
(1095.28)–(1095.35) 尚未证明这两个指定配对不能同时为零；
原 $\eta_k,\nu_k$、$e,K_4$ 及同标签筛选仍须继续。

本节 o1_theta 直接从原 Miller divisor/首项推导完整乘法、
相对 Cartier 极化及两处第三类复合；o2_high_coefficient
独立逐式核准弦线符号、相对 base 规则、$V(Z)$ 项以及原四阶
平移修正。全文没有数学执行或新扫描。


## 9. 保留移位 Miller 项的完整三平移公式

本节沿用 $S f(T)=(V(T)+v)^{2k}f(T+Q)$、$Q=(0,v)$，
以及 §8 的 $G_P=\mathscr FJ_P$。本节给出实际
$\mathscr F S\mathscr F$，包括不能删去的移位 Miller 项；
不假定 $S$ 与 $\mathscr T_F$ 交换。

### 9.1 原 $S\Psi$ 的变换现在有确切来源

在 $O$ 的原 frame 中，$S\Psi$ 的最高项是
$\delta u^{-p}$，没有 $u^{-p-1}$ 项。因此
$g=S\Psi-\delta\Psi\in V_0$。由 (1095.35) 的第一阶核和
(1095.30)，可以对参数 $P$ 在 $-Q$ 微分：
$$
\begin{aligned}
\mathscr F(S\Psi)(T)
 &=D_P G_P(T)\big|_{P=-Q},\\
D_Pm(T,P)\big|_{P=-Q}
 &=-\frac{2v(V(T)+v)}{U(T)^2}.
\end{aligned}
$$
因为 $D_P\Psi=\delta$，得到完整式
$$
\boxed{
\mathscr T_F(g)=\mathscr F(S\Psi)
 =\frac{(V+v)(2v\Psi-\delta U)}{U^2}.
}
\tag{1095.36}
$$
这不是由角色或未登记的旧 $g$ 候选猜出的变换。

两处 $U=0$ 的表面极都可直接消去。写
$\Psi=VU\,s(U)$，其中 $s(U)$ 只含 $U^3$ 的幂，
且 $s(0)=\delta/(2v^2)$。右边准确等于
$$
2vU^2s(U)+2v^2(V+v)\frac{s(U)-s(0)}U.
$$
后一分子被 $U^3$ 整除。由于 $\deg_U s=m-2$，
整式在 $O$ 的极阶至多 $p-1$，确属原 $V_0$。

### 9.2 完整三平移所需的三个实际极点

以下先取一般位置的 $P,R$，最后按有理函数恒等式延拓。
为避免将点名与算子混淆，设
$$
\begin{gathered}
A=-P-Q,\qquad R_-=R-Q,\qquad
a=\frac{V(R)+v}{U(R)},\qquad
b=\frac{V(P)-v}{U(P)},\qquad d=\Psi(P),\\
m_0(T)=(V(T)+v)^{2k},\\
r_0=-U(A)+b\Psi(R),\qquad
r_A=m_0(A)K(A,R).
\end{gathered}
\tag{1095.37}
$$
记原完整相对 Cartier 输出
$$
W(Z,R)=
\frac{
 C_{{\rm rel},T}
 \bigl(m_0(T)h_{-P}(T+Q)K(T,R)\omega_T\bigr)}
 {\omega_Z}.
$$
源只须保留以下三个极点：

- $T=A$ 是简单极，留数准确为 $r_A$；
- $T=F^{-1}R$ 至多为 $p$ 阶极；
- $T=O$ 至多为二阶极，留数准确为 $r_0$。

最后一条由原 frame 直接给出：
$$
\begin{aligned}
h_{-P}(T+Q)&=b-U(A)u_T+O(u_T^2),\\
m_0(T)K(T,R)\omega_T
 &=u_T^{-2}\{1+\Psi(R)u_T+O(u_T^2)\}\,du_T.
\end{aligned}
$$
相对 Cartier 后仅有 $Z=FA,R,O$ 三个简单极。
留数和为零，因此必有
$$
W=w_0-r_0h_R(Z)+r_A\{h_{FA}(Z)-h_R(Z)\},
\tag{1095.38}
$$
其中 $w_0=\operatorname{Reg}_{Z=O}W$。

这里的全纯常数不能省去，也不以同除子为由另选。
在 $T=-Q$，$m_0$ 的零阶是 $p+1$，
$h_{-P}(T+Q)$ 至多有一个简单极，$K$ 在一般位置正则。
故整个源的零阶至少 $p$；相对 Cartier 输出在
$Z=F(-Q)=Q$ 确实消失。又
$$
h_R(Q)=-a,\qquad h_{FA}(Q)=-b^p.
$$
后一式来自原弦线 $V(A)=bU(A)+v$ 及 $v^p=-v$。
把 $Z=Q$ 代入 (1095.38)，严格固定
$$
\boxed{w_0=-ar_0+(b^p-a)r_A.}
\tag{1095.39}
$$
因此这里已支付整个源的常数，而不只是极部。

### 9.3 真实 $\mathscr F S\mathscr F$ 核

原弦线加法和原 Deuring 加法分别给
$$
\begin{aligned}
h_{-P}(T+Q)
 &=h_{-(P+Q)}(T)-h_{-Q}(T)+b,\\
\Psi(T+Q)&=\Psi(T)+h_{-Q}(T)^p.
\end{aligned}
$$
于是由 $G_P(T)=-h_{-P}(T)(\Psi(T)+d)$，
保留相对 Cartier 的整个目标变量 $Z$，得到
$$
\frac{C_{{\rm rel},T}((SG_P)(T)K(T,R)\omega_T)}
 {\omega_Z}
=-(D_R+d+h_Z(R)+h_Q(Z))W(Z,R).
\tag{1095.40}
$$
此处 $h_{-Q}(T)^p$ 的目标函数准确是 $h_Q(Z)$；
这是 $F(-Q)=Q$ 的实际 Frobenius 扭曲，base 常数未取 $p$ 次根。

在 $Z=O$，原两项的极恰相消：
$$
h_Z(R)+h_Q(Z)=U(R)u_Z+O(u_Z^2),\qquad
W=r_0u_Z^{-1}+w_0+O(u_Z).
$$
所以 (1095.19) 给出的正规常数是
$$
(\mathscr F S\mathscr FJ_P)(R)
=-(D_R+d)w_0-U(R)r_0.
\tag{1095.41}
$$
特别是 $U(R)r_0$ 这一项不能因两条 $h$ 的常数都为零而删除。

最后只需原加法公式作确切代数化简：
$$
\begin{aligned}
D_Ra&=U(R)-U(R_-),\\
D_Rr_0&=b\delta,\\
D_R\log r_A&=-d-b^p-h_{FA}(R),\\
(a-b^p)h_{FA}(R)
 &=U(R)+U(A)^p-ab^p,\\
U(A)&=b^2-U(P).
\end{aligned}
$$
将 (1095.39) 代入 (1095.41)，得到完整三平移核
$$
\boxed{
\begin{aligned}
(\mathscr F S\mathscr FJ_P)(R)
={}&\bigl(d\,a-U(R_-)\bigr)
       \bigl(-U(A)+b\Psi(R)\bigr)+ab\delta\\
 &+\bigl(U(P)^p-U(R_-)\bigr)
       m_0(A)K(A,R).
\end{aligned}
}
\tag{1095.42}
$$
末行是实际移位 Miller 项，仍保留它的全部零点和极点。
它不是可不经证明删掉的有限秩误差。
右边各项在某些点有表面极；其总和由左边的
$\mathscr F S\mathscr FJ_P\in H$ 延拓为正则截面。
碰撞、切线和竖线情形一律在完成恒等式后取极限，
没有将单独的 $0\cdot\infty$ 项先置零。

### 9.4 一个保留原标架的切线特化

在 $P=Q$ 的切线极限，$b=d=U(P)=U(A)=0$，
$A=Q$，而 $m_0(Q)=(2v)^{2k}=\gamma$。
另由原加法和原 $J(Q,R)$，
$$
U(R-Q)=\frac{2vU(R)}{V(R)-v},\qquad
K(Q,R)=-\frac{(V(R)-v)^{2k}}{U(R)}.
$$
故 (1095.42) 给出
$$
\boxed{
\mathscr F S\mathscr F J_Q
=2v\gamma(V-v)^{2k-1}.
}
\tag{1095.43}
$$
这支付了该特化的全部 theta multiplier 和常数，
没有用一般三平移范数来代替单个变换。

(1095.36)–(1095.43) 给出了真正可用于原三分布的源；
(1095.35) 的两条指定配对仍是
$e$ 与 $ve+\delta^2K_4/6$。本节没有由
$g$、$J_Q$ 或另一输入的非零，推出原 $e,K_4$ 非同时零。

本节 o1_theta 从 §8 完整核微分及三极相对 Cartier 推导；
o2_high_coefficient 独立核准原 $g$ 的多项式消极、
三个实际留数、$T=-Q$ 的零阶、$W(Q)=0$ 所固定的常数、
正规项 $-U(R)r_0$ 以及最后弦线化简。
全文没有数学程序执行或新扫描。


## 原来源与核对

- R1061 (1061.57)–(1061.59)：原全部 graph、Miller 首项与实际相对变换的可逆性。
- R1061 (1061.65)、(1061.76)–(1061.84)：原 kernel 微分、实际对称 tensor、
  有限极界 Cartier 的 $A,B$、radical 与收缩式。
- 本文的可逆性、最高两项及三平移常数均由这些原身份在纸面推出。
  o1_theta 独立核准完整 $J^\#$ 满射、$\Psi$ 的最高系数对偶及范数 $1$，
  并核对 (1095.15) 的唯一最高偶边界与三轨道 Gram 的实际因子。
  全文没有数学程序执行，也没有新有限扫描。
