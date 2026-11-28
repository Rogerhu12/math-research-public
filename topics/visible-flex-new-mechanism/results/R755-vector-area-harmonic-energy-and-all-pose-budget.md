# R755　两真刚圈的向量面积、调和能量与全姿态四阶矩阵门

设同一材料环带 \(a\le r\le b,\phi\in\mathbb R/(2\pi\mathbb Z)\) 有度量 \(g=E(r)dr^2+r^2d\phi^2,\ E>0\)。外刚圈实际材料参数为 \(bD_o e(\phi)\)，内圈为 \(C+aD_i e(\phi)\)，\(e=(\cos\phi,\sin\phi)^T\)。每个 \(D_e\) 的两个列向量是对应刚件的有序正交单位向量，其向量积为 \(n_e\)，\(P_e=D_eD_e^T\)。两个 \(D_e\) 保有真实材料标记与相对周向转角。空间共同平移已消去。定义
\[
 A=2\pi\int_a^b r\sqrt E\,dr,\quad L=\int_a^b {\sqrt E\over r}\,dr,\quad
 B=\pi(b^2n_o-a^2n_i).
\]
\(A\) 是给定材料度量的面积。Stokes 给任何带此边界的有向浸入 \(F\) 的向量面积 \(\int n\,dA_F=B\)，其中 \(n=F_r\times F_\phi/|F_r\times F_\phi|\)。这不要求图或凸性。

## 1　完整边值的三分量调和延拓

令 \(x(r)=\int_a^r \sqrt E\,dr/r\)，则 \(g=r^2(dx^2+d\phi^2)\)。等温圆柱长度为 \(L\)。唯一的调和边值解为
\[
 H=(1-x/L)C+
 \left[a{\sinh(L-x)\over\sinh L}D_i+
       b{\sinh x\over\sinh L}D_o\right]e .
\]
对向量场定义 \(M(Y)=\int dY\,g^{-1}dY^T\,dA_g\)，不含二分之一。由零边差 \(Z=F-H\) 和调和分部积分，\(M(F)=M(H)+M(Z)\)。这是整个对称矩阵的等式，交叉两个坐标也消失。径向零模给第一项；一次角模利用 \(\int ee^T\,d\phi=\pi I\) 和边通量给
\[
 M:=M(H)=\frac{2\pi}{L} CC^T+
  \pi\coth L(a^2P_i+b^2P_o)-
  \pi ab\,\operatorname{csch} L(D_iD_o^T+D_oD_i^T).             \tag{1}
\]
材料相位改动会改最后两矩阵的乘积。独立旋转内帽后继续使用原相位必须有实际重标识依据。

## 2　真等距的分解与全部中心

真等距时 \(dF\,g^{-1}dF^T=I-nn^T\)，向量面积的积分权是同一 \(dA_g\)。因此
\[
 AI-BB^T/A-M=
 \int(n-B/A)(n-B/A)^T dA_g+M(F-H)\succeq0.                  \tag{2}
\]
设 \(M_1\) 为 (1) 去掉 \(CC^T\) 后的矩阵，\(D=AI-BB^T/A-M_1\)。全部可能的相对中心必须落在
\[
 D\succeq0,\qquad C\in\mathop{\rm range}D,\qquad
 C^T D^\dagger C\le L/(2\pi).                               \tag{3}
\]
\(D^\dagger\) 为 Moore–Penrose 逆。将 \(D-(2\pi/L)CC^T\) 限制到 \(\ker D\) 得到值域条件，再在 \(\operatorname{range}D\) 上取平方根得到 (3)。若 \(D\) 有负方向，任何中心都不可能。仅在某一姿态 \(C\) 的 (2) 失败，只排这一姿态和共享该材料边数据的解。固定材料全时间的族须在每一时刻使用同一个 \(A,L\)，配合各自真正的 \(D_i,D_o,C\)；通过全部端点单独的必要门不构成族。

## 3　对任意近等距候选的可验证误差下界

设 \(\|g^{-1/2}(g_F-g)g^{-1/2}\|_{\rm op}\le\eta\)，\(s=1+\eta\)，\(J=dA_F/dA_g>0\)。切面两奇异值给 \(dF g^{-1}dF^T\preceq s(I-nn^T)\)，及 \(J\le s\)。对任一 \(v\)，
\[
 (v\cdot B)^2=\left(\int J(v\cdot n)dA_g\right)^2
 \le s^2 A\int(v\cdot n)^2 dA_g .
\]
所以 \(M\preceq M(F)\preceq sAI-BB^T/(sA)\)。Schur 补给全方向等价的必要门
\[
 1+\eta \ \ge\ \lambda_{\max}\!
 \begin{pmatrix}M/A&B/A\\B^T/A&0\end{pmatrix}.                \tag{4}
\]
任意完整四维非零试向量的 Rayleigh 商都给严格可下包的必要量。可先由普通浮点特征分解选择方向，再对该字面向量及真实有向积分区间重新求商。未违反某次单向测试既非全方向通过，也非充分。\(C=0\) 给全部中心的共同下限，因为 \(CC^T\) 是唯一剩余的中心项，且为半正定。

## 4　把真实曲率与帽的一阶材料方向纳入 (2)

现在只对真等距的 \(C^2\) 场再假设 \(\|\mathcal S\|_{\rm op}\le M_c\)。令 \(ds=\sqrt E\,dr,\ s_e(r)\) 为到端 \(e\) 的材料径长。单位速固定角母线为测地线；故真实单位径切向 \(P=F_s\) 与单位法向 \(n\) 沿其均以速率至多 \(M_c\) 转动。帽平面相切且材料一阶刚接时，端的真 \(P_e(\phi)=D_e e(\phi)\)，此处以 \(P_e(\phi)\) 指向量；(1) 中不带角的 \(P_e\) 是矩阵。对于所选空间向量 \(v\)，定义
\[
 N(r)=\max_{e=i,o}\big(|v\cdot(n_e-B/A)|-M_c s_e(r)|v|\big)_+,
\quad
 Y(r)=\max_{e=i,o}\left[
 \|v\cdot(H_s-P_e(\phi))\|_{L^2(d\phi/2\pi)}
       -M_c s_e(r)|v|\right]_+ .
\]
两端不要求影响区互不相交，分别取最大避免重复积分。对 \(N\) 用逐点三角不等式，对 \(Y\) 用 \(L^2\) 逆三角不等式并保留 \(M(F-H)\) 的径向一项。于是
\[
 v^T(AI-BB^T/A-M)v\ \ge\
 2\pi\int_a^b r\sqrt E\,\{N(r)^2+Y(r)^2\}\,dr.              \tag{5}
\]
两项来自 (2) 的不同非负项，可以相加。所有角在式中真实积分。实际 \(H_s=H_x/r\) 只有零模和一次模，零模为 \(-C/(Lr)\)，一次模为
\(\big[b\cosh x D_o-a\cosh(L-x)D_i\big]/(r\sinh L)\)。若 \(v\cdot(H_s-P_e(\phi))=h_0+h_1\cos\phi+h_2\sin\phi\)，平方均值精确为 \(h_0^2+(h_1^2+h_2^2)/2\)。对于相同两刚圈转角，任意中心只在该 RMS 中增加非负零模平方，同时 (5) 左边减少非负量。因此某一方向在 C=0 已违反 (5) 时，全部中心均违反该方向的曲率强化。

本节使用准确等距的测地线，不将曲率上限直接转给有度量误差且径线测地曲率未知的试面。

对既定绝对法管 \(T=.03\)，可取 \(M_c=100/3\)。若仅要求 \(\mathrm{reach}\ge .03D_{\rm actual}\)，必须用实际直径或其已证正下界 \(D_-\) 取必要上限 \(M_c=100/(3D_-)\)；单有直径上界不能把这两种条件认作等价。

## 5　R738/R748 来源与直接高度形式

对外平面正投影、固定高度 \(u=F\cdot n_o\)，真等距时 \(n\cdot n_o=\sqrt{1-|\nabla_g u|^2}=\sigma\)，有全域标量恒等式
\(\int \sigma\,dA_g=B\cdot n_o\)。若只知真实相对度量误差 \(\eta<1\) 且候选保持正投影，归一的二维水平 Gram 为 \(G-\nabla u\otimes\nabla u,\ I-\eta I\preceq G\preceq I+\eta I\)。当声明的 \(\sigma^2=1-|\nabla_g u|^2\ge0\) 时，特征值夹逼又给
\[
 \int\sqrt{(1-\eta)(\sigma^2-\eta)_+}\,dA_g
 \le B\cdot n_o\le
 \int\sqrt{(1+\eta)(\sigma^2+\eta)}\,dA_g.                  \tag{6}
\]
若 \(\sigma^2<\eta\)，左边立刻使用零下界。式 (6) 在选定单高度后可先验阻止仅靠水平发展消去全部误差的错误预期。

R738 的真实 \(E_\sharp\) 与原末态 \(C\) 可只新付材料积分 \(A,L\) 与沿径前缀，原 1882 参数、原尾 RHS、旧 J 及全壳格均不需重跑。R745 是另一材料，必须重新支付其自己的 \(A,L\)。在所用有向区间未呈现严格违反之前，本结果不排任一具体原输入，亦不授通过本门的输入几何资格。
