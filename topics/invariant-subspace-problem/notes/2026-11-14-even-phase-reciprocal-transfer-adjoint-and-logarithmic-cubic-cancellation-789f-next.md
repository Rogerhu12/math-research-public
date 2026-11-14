# 任意正权偶相位的倒数伴随传输、完全同谱与对数流三阶抵消

本稿建立一个非微扰的同源恒等式：倒数权变换把实际相位的归一传输算子变为其伴随。因此两个实际相位的完整特征值多重集相同。其局部推论是，沿任意居中对数权直线，物理归一相位的三阶项严格消失。

它没有证明传输算子已经是收缩，也不把倒数同谱当作任意正权的相位上界。所有完整层逆、源压缩、物理度量及乘积次序均保留。

## 1. 共同固定源与四个真实二次型

在 \(2s\) 位上，取 \(b_i>0\)、\(z_i=b_i^2\)、\(\pi=\prod_i z_i\)。记
\[
d_b=\sum_i b_iE_i,\quad e_b=\sum_i b_i^{-1}E_i^*,\quad
d_0=\sum_iE_i,\quad e_0=d_0^*.
\]
固定无权源是 \(V_0=\ker d_0\cap\mathcal H_{s-1}\)，其物理正交投影记为 \(P\)。令
\[
Z_j=\operatorname{diag}(z_I:|I|=j),\quad z_I=\prod_{i\in I}z_i,\qquad
K(z)=d_0Z_se_0\quad\text{于完整 }\mathcal H_{s-1}.
\]
完整 \(K(z)\) 正定。实际去权源为
\[
\mathcal E_z=Z_{s-1}^{-1/2}|_{V_0}:
V_0\longrightarrow V_b:=\ker d_b\cap\mathcal H_{s-1}.
\]
在同一个 \(V_0\) 上定义
\[
\begin{aligned}
h(z)&=PZ_{s-1}^{-1}P,&
\ell(z)&=\pi^{-1}PZ_{s-1}P,\\
g(z)&=P K(z)^{-1}P,&
q(z)&=\pi^{-1}P K(z)P.
\end{aligned} \tag{1.1}
\]
它们的实际含义为
\[
h=\mathcal E_z^*\mathcal E_z,\qquad
g=\mathcal E_z^*G_b\mathcal E_z,\qquad
\ell=\mathcal E_z^*L_b\mathcal E_z,\qquad
q=\mathcal E_z^*Q_b\mathcal E_z. \tag{1.2}
\]
这里 \(G_b,L_b\) 是完整 \(d_b,d_b^2/2\) 的 primitive MP Gram，
\[
Q_b=P_{V_b}e_b^*e_b|_{V_b}=4G_b+A_{0,b}A_{0,b}^*.
\]
式 (1.1) 的 \(g\) 使用**完整** \(K^{-1}\) 后压到 \(V_0\)；没有把它换成 \((PKP)^{-1}\)。

为直接核清 (1.2)，设 \(D_j=Z_j^{1/2}\)。完整
\[
d_bd_b^*=D_{s-1}^{-1}K(z)D_{s-1}^{-1}
\]
使第一逆给 \(g\)。顶 MP 公式在实际 \(V_b\) 上为
\[
\mathcal J_2=(-1)^{s-1}\pi^{-1/2}\,\mathrm{comp}\,D_{s-1}^{\,2},
\]
因此其在 \(\mathcal E_z\) 上的 Gram 为 \(\ell\)。最后
\[
e_b\mathcal E_z=D_s^{-1}e_0|_{V_0},
\]
故 reciprocal Gram 为 \(P d_0 Z_s^{-1}e_0P\)，由下节补集身份恰等于 \(q\)。

实际相位仍为
\[
H_{0,b}=G_b^{-1}L_b+2G_b-Q_b,\qquad
\Phi_b=H_{0,b}^*L_b^{-1}H_{0,b}. \tag{1.3}
\]

## 2. 完整中央补集与倒数共轭

令 \(C_0\) 为中央 \(\mathcal H_s\) 上的物理酉补集算子。它是自伴 involution，满足
\[
C_0Z_sC_0=\pi Z_s^{-1}. \tag{2.1}
\]
完整 unweighted raising \(e_0:\mathcal H_{s-1}\to\mathcal H_s\) 单射。记
\[
F_0=d_0e_0,\qquad R_0=e_0F_0^{-1/2}.
\]
则 \(R_0\) 是到 \(\operatorname{Ran}e_0=(\ker d_0\cap\mathcal H_s)^\perp\) 的等距映射。中央层的 \(d_0,e_0\) 交换，所以 \(C_0\) 与中央 \(e_0d_0\) 交换，并保持上述像空间。于是
\[
T_0=R_0^*C_0R_0
\]
是完整 \(\mathcal H_{s-1}\) 上的自伴酉算子；它与 \(F_0\) 交换，且
\[
C_0e_0=e_0T_0. \tag{2.2}
\]
在 \(V_0\) 上，标准 unweighted primitive 顶补集恒等式给
\[
T_0|_{V_0}=(-1)^{s-1}I. \tag{2.3}
\]
这里的 \(T_0\) 正是既有完整共同谱稿使用的 unweighted 相位 involution；不是把完整 \(d_0^2/2\) 的逆误作 \(T_0\)。也可从各 primitive ladder 验证：中央补集在源次数 \(r\) 的 ladder 上作用为 \((-1)^r\)，而 \(V_0\) 的源次数是 \(s-1\)。

由 (2.1)–(2.2)，在完整层严格有
\[
\boxed{K(z^{-1})=\pi^{-1}T_0K(z)T_0.} \tag{2.4}
\]
这先是一条完整层共轭，故对完整逆同样成立：
\[
K(z^{-1})^{-1}=\pi T_0K(z)^{-1}T_0.
\]
最后再用 (2.3) 压到实际固定源，得到
\[
\boxed{
\begin{aligned}
h(z^{-1})&=\pi\ell(z),&
\ell(z^{-1})&=\pi h(z),\\
g(z^{-1})&=\pi g(z),&
q(z^{-1})&=\pi q(z).
\end{aligned}} \tag{2.5}
\]
所有四式使用同一个 \(V_0\)，不是四个独立坐标选择。共同因子 \(\pi\) 不能只在其中某些式里删掉。

## 3. 物理归一传输及其倒数伴随

源坐标中的实际算子为
\[
\mathsf G=h^{-1}g,\qquad \mathsf L=h^{-1}\ell,\qquad \mathsf Q=h^{-1}q.
\]
因此
\[
\mathsf H_0=g^{-1}\ell+2h^{-1}g-h^{-1}q.
\]
定义同源双线性块
\[
\boxed{J(z)=h(z)g(z)^{-1}\ell(z)+2g(z)-q(z).} \tag{3.1}
\]
注意 \(h g^{-1}\ell\) 的次序；一般 \(J\) 并不自伴。恰有 \(J=h\mathsf H_0\)。

实际源等距同构是
\[
\mathcal U_z=\mathcal E_z h(z)^{-1/2}.
\]
将 (1.3) 保完整物理伴随写回固定源，得到
\[
\mathcal U_z^*\Phi_b\mathcal U_z
=h^{-1/2}J^*\ell^{-1}J h^{-1/2}
=\mathcal T(z)^*\mathcal T(z), \tag{3.2}
\]
其中
\[
\boxed{\mathcal T(z)=\ell(z)^{-1/2}J(z)h(z)^{-1/2}.} \tag{3.3}
\]
这是实际相位的平方根传输，不是任意选取的因子。

由 (2.5) 与 \(g,q\) 自伴，
\[
J(z^{-1})=\pi[\ell g^{-1}h+2g-q]=\pi J(z)^*.
\]
代入 (3.3)，共同因子全部准确抵消，给
\[
\boxed{\mathcal T(z^{-1})=\mathcal T(z)^*.} \tag{3.4}
\]
从而实际物理归一相位分别是
\[
\widehat\Phi(z)=\mathcal T^*\mathcal T,\qquad
\widehat\Phi(z^{-1})=\mathcal T\mathcal T^*.
\]
两者是同维有限方阵的两侧奇异值平方，故：

**定理 3.1。** 对任意偶位数、任意独立正权，
\[
\boxed{\operatorname{spec}_{\rm mult}\Phi_b
=\operatorname{spec}_{\rm mult}\Phi_{b^{-1}}.} \tag{3.5}
\]
包括零特征值的重数也相同。特别地，对每个固定 \(\kappa\ge0\)，
\[
\Phi_b\preceq\kappa I
\quad\Longleftrightarrow\quad
\Phi_{b^{-1}}\preceq\kappa I.
\]
这个等价不要求 \(H_0\) 可逆，也没有把一般不交换的 \(H_0^*L^{-1}H_0\) 与 \(H_0L^{-1}H_0^*\) 在同一权点直接交换。

同样地，\(\kappa=1\) 的目标恰为真实块
\[
\begin{pmatrix}h&J^*\\J&\ell\end{pmatrix}\succeq0. \tag{3.6}
\]
倒数权把 (3.6) 变为共同正标量 \(\pi\) 乘上其两行列互换；这提供一个保持物理源的非微扰对称形式，但其正性本身仍待证明。

## 4. 对数直线的严格三阶抵消

取 \(\sum_i x_i=0\)、\(z_i(t)=e^{t x_i}\)。此时 \(\pi=1\)，倒数权恰为 \(t\mapsto-t\)，所以
\[
h(-t)=\ell(t),\quad g(-t)=g(t),\quad q(-t)=q(t),
\quad J(-t)=J(t)^*,\quad \mathcal T(-t)=\mathcal T(t)^*. \tag{4.1}
\]
这些是对每个实 \(t\) 的准确等式，不是截断展开。

记 \(X=P(\sum_i x_i n_i)P\) 于 \(V_0\)。在 \(t=0\) 有
\[
h=\ell=I,\quad g=\tfrac12I,\quad q=2I,\quad J=\mathcal T=I,
\]
\[
h'(0)=-X,\quad \ell'(0)=X,\quad g'(0)=q'(0)=0.
\]
因而由 (3.1) \(J'(0)=0\)，再由 (3.3)
\[
\mathcal T'(0)=-\tfrac12X+\tfrac12X=0. \tag{4.2}
\]
写其实际解析展开
\[
\mathcal T(t)=I+t^2T_2+t^3T_3+O(t^4).
\]
式 (4.1) 给 \(T_2^*=T_2\)、\(T_3^*=-T_3\)。二阶全出生定理在任意光滑权路径上只取决于一阶方向（实际归一相位在等权点的第一微分为零），故这里仍给
\[
\widehat\Phi(t)=I-t^2K_x+O(t^3),\qquad
K_x=\tfrac14B_x^*B_x+\tfrac12S_x^*S_x.
\]
比较 (3.2) 可知 \(2T_2=-K_x\)，且三阶完全抵消：
\[
\boxed{
I-\mathcal U_{z(t)}^*\Phi_{b(t)}\mathcal U_{z(t)}
=t^2K_x+O_{s,x}(t^4).
} \tag{4.3}
\]
这是完整源上的算子范数展开。它不只是在某个二阶核向量上的标量抵消。

非微扰同谱还给每个整数 \(k\ge1\)
\[
\operatorname{tr}\widehat\Phi(t)^k
=\operatorname{tr}\widehat\Phi(-t)^k.
\]
不过一般不能从 \(\mathcal T(-t)=\mathcal T(t)^*\) 推出 \(\widehat\Phi(-t)=\widehat\Phi(t)\) 的逐矩阵等式：两者分别为 \(\mathcal T\mathcal T^*\) 与 \(\mathcal T^*\mathcal T\)，相同的是完整谱。式 (4.3) 也不能在 \(K_x\) 的核上直接代替四阶或完整 reducing 模块的正性论证。

## 5. 下一处实际缺口

共同矩形式 (3.6) 保留了两侧源度量与完整 Green 逆。要得到普适相位常数，仍须从真实 Boolean 结构证明这个块（或 \(\kappa\) 版本）正，先共同平方权缩放归一 \(\pi=1\)，仍不能仅使用
\[
\begin{pmatrix}h&I\\I&\ell\end{pmatrix}\succeq0,\qquad
\begin{pmatrix}g&I\\I&q\end{pmatrix}\succeq0,\qquad q\succeq4g
\]
这些各自的 Gram 正性后就取消混合项。倒数同谱给域的精确对称，对数流给完整三阶项的消失；它们都没有单独支付任意正权下 \(\|\mathcal T(z)\|\) 的统一上界。

依赖：全出生二阶稿、完整共同谱稿、R239 的 unweighted primitive 顶补集公式。本文未调用新的外部定理，未增加有限样本扫描。

