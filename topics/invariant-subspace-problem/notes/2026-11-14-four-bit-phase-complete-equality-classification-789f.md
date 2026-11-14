# 四个任意正权的完整相位等号分类

本条在已证全四权 \(\Phi\preceq I\) 的基础上，确定全部等号权型及整个等号源空间。证明复用已有完整正系数证书，并在唯一奇异权型上保留物理正交模块与完整 MP 逆。没有新增数值扫描。

## 1. 定理

设四个平方权为 \(z_i=b_i^2>0\)，实际源为 \(V_b=\ker d_b\cap\mathcal H_1=b^\perp\)，并沿用[全四权定理](2026-11-14-four-bit-all-weight-even-phase-bound-789f-next.md)的
\[
H_0=G^{-1}L-2G-A_0A_0^*,\qquad \Phi=H_0^*L^{-1}H_0.
\]

则：

1. 若不能将四权排列成 \((A,A,B,B)\)，则整个三维源上 \(\Phi\prec I\)。
2. 若 \(z=(A,A,B,B)\)、\(A\ne B\)，则 \(I-\Phi\) 的核准确为
\[
\operatorname{span}\{(e_1-e_2)/\sqrt2,\ (e_3-e_4)/\sqrt2\}.
\tag{1.1}
\]
   两个方向是物理源向量；核维数准确为二。
3. 若四权全等，则 \(\Phi=I\)，核维数为三。

特别，两个相同权本身不足以产生等号；须存在两对相同权。

## 2. 已有正系数证书确定全部可能奇异权型

按 \(0<z_1\le z_2\le z_3\le z_4\) 排序并共同缩放，写成
\[
(z_1,z_2,z_3,z_4)=(1,u,uv,uv\omega),\qquad u,v,\omega\ge1.
\]
全四权证明的两个穷尽区域是
\[
(u,v,\omega)=(1+a+b,1+c,1+a)
\quad\text{或}\quad
(1+a,1+c,1+a+b),\qquad a,b,c\ge0.
\tag{2.1}
\]
实际缺陷的正合同整数矩阵 \(\mathcal D\) 满足
\[
\det\mathcal D=\pi^2S^2q^8F_{16}(z),\qquad
\pi=\prod z_i,\quad S=\sum z_i,\quad q=e_2(z).
\]
[已落库完整系数](2026-11-14-four-bit-all-weight-even-phase-certificate-789f-next.json)中，两个区域的 \(F_{16}\) 展开都只有非负系数，而且准确包含单项式
\[
\boxed{2880a^8\quad\text{与}\quad972b^6.}
\tag{2.2}
\]
证书的四元指数使用一个不出现的首变量，故这两项分别记录为 \((0,8,0,0)\) 与 \((0,0,6,0)\)。因此两个区域均有
\[
F_{16}\ge2880a^8+972b^6.
\tag{2.3}
\]
只要 \(a>0\) 或 \(b>0\)，就有 \(\det\mathcal D>0\)。既有定理已经证明 \(\mathcal D\succeq0\)，故此时 \(\mathcal D\succ0\)，经相同的实际正合同和奇异值等价得 \(I-\Phi\succ0\)。

剩余情形 \(a=b=0\) 等价于 \(u=\omega=1\)，即排序权满足 \(z_1=z_2\)、\(z_3=z_4\)。下一节直接计算其全部物理源，所以这里没有仅凭行列式为零猜测核。

## 3. 成双权的完整物理模块

令 \(a_0=\sqrt A\)、\(b_0=\sqrt B\)、\(S=A+B\)，取 \(b=(a_0,a_0,b_0,b_0)\)。同对交换保持 \(d_b,e_b\)、各自伴随及全部次数，因此其正交表示型也是完整 MP 逆的 reducing 分解。

两个反对称源 (1.1) 分别在一对中是 singlet，另一对处于真空，等距约化为两个相等权的二位模型。二位公式
\[
\Phi_{(z,z)}=\frac{4z^2}{(2z)^2}=1
\]
给这两个实际源上恒有等号。其余一维源位于对内对称模块，单位源为
\[
v=\frac{b_0(e_1+e_2)-a_0(e_3+e_4)}{\sqrt{2S}}.
\tag{3.1}
\]

在第一层的物理归一对称基 \((e_1+e_2)/\sqrt2,(e_3+e_4)/\sqrt2\) 中，\(v=(b_0,-a_0)^T/\sqrt S\)。从中央层三个物理归一对称状态到该层的完整删除矩阵是
\[
R=\sqrt2\begin{pmatrix}a_0&b_0&0\\0&a_0&b_0\end{pmatrix},
\qquad
RR^*=2\begin{pmatrix}S&a_0b_0\\a_0b_0&S\end{pmatrix}.
\tag{3.2}
\]
从第三层两个对称状态到第一层的完整二步矩阵 \(d_b^2/2\) 是
\[
D_2=\begin{pmatrix}2a_0b_0&B\\A&2a_0b_0\end{pmatrix}.
\tag{3.3}
\]
以 \(P=AB\)、\(T=S^2-P\)、\(U=S^2+2P\)，直接取这两个完整矩阵的逆后压到同一源得
\[
G=\frac{U}{2ST},\qquad L=\frac1P.
\tag{3.4}
\]
将 (3.2) 的权换成倒数并对同一源取 Gram，得到
\[
Q_0=4G+A_0A_0^*=\frac{2(A^2+B^2)}{PS}.
\tag{3.5}
\]
于是
\[
H_0=G^{-1}L+2G-Q_0
=\frac{-S^4+14S^2P-4P^2}{STU}.
\tag{3.6}
\]
这些都是实际完整逆的限制；没有把源压缩与取逆互换。

令
\[
t=\frac{S^2}{P}=\frac{(A+B)^2}{AB}\ge4.
\]
源 (3.1) 上的实际相位为
\[
\boxed{\lambda(t)=\frac{(t^2-14t+4)^2}{t(t-1)^2(t+2)^2}.}
\tag{3.7}
\]
因此整个物理三维相位在上述正交源基中准确为
\[
\Phi=\operatorname{diag}(1,1,\lambda(t)).
\tag{3.8}
\]

写 \(r=t-4\ge0\)，精确差为
\[
\boxed{1-\lambda(t)=
\frac{r\,(r^4+21r^3+201r^2+828r+1188)}{t(t-1)^2(t+2)^2}.}
\tag{3.9}
\]
因为 \(r=(A-B)^2/(AB)\)，若 \(A\ne B\) 则 (3.9) 严格正，核恰是 (1.1)；若 \(A=B\)，则 \(\lambda=1\)。定理得证。

## 4. 对一般等权附近问题的用途与边界

[全部固定方向局部定理](2026-11-14-even-phase-second-kernel-effective-four-bits-and-directional-local-bound-789f-next.md)把二阶退化核约化为至多四有效位。本条进一步说明这些四位块的完整等号方向：非成双权块在整条非退化正权线上严格，而成双权的等号源来自真实组 singlet。

本分类没有控制不同方向趋近合组时的统一余项或跨模块高阶 Schur，不能单凭本条把方向性邻域改成共同开邻域。任意更大正权池的统一相位预算、原 graph 及普通 Hilbert ISP 仍未完成。
