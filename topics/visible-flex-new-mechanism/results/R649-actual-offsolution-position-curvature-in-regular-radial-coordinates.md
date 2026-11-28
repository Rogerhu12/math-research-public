# R649：完整离解位置的真实曲率及正则径向区间入口

2026-11-28，Astra-new-mechanism-8cdb3418-20261128。

R645 将当前几何类的全闭面 reach 缩到真实图结构、连续主曲率及高度门。
本稿支付其中的实际曲率公式：它作用于 R643 完整归一位置本身，在
F、G、S 都未解为零时仍准确成立。它保留 S 的真实径向导数，也保留归一
相位的全部 F/G 项，不能把目标度量的 Hessian 直接当作离解曲面的第二基本形式。

已有同态双位置差分已经计算过样本曲率，本稿不重算那些样本。
新增的是可用于连续区间的准确表达和其必要数据。下面所有 primitive 均是
完整连续周期 primitive，有限 FFT 和径向差分的误差仍按它们自己的来源支付。

## 1. 同一归一位置与真实缺陷

沿 R643 的实际连续场，令

\[
g=E(r)\,dr^2+r^2d\theta^2,\quad
p=Z_r,\quad q=Z_\theta,\quad t=Z_{\theta\theta},\quad
b=(r^2-q^2)^{1/2},
\]
\[
u=(E-r^2p^2/b^2)^{1/2},\quad v=-pq/b,\quad
N=r/b+r^2pt/b^3,\quad a=N/u,
\]
\[
A=\langle a\rangle>0,\quad F=A-1,\quad G=\langle R\rangle,\quad
\phi=\theta+\Pi a/A.
\tag{1}
\]

固定 T=(-sin φ,cos φ)、n=(cos φ,sin φ)=-JT。准确位置为 Y=Π(bT)，故

\[
Y_\theta=bT,\qquad
Y_r=vT+un+\sqrt E\,S.
\tag{2}
\]

这是同一个真正位置的导数身份，S 不被设成零。R643 给

\[
k:=\phi_\theta=a/A,\qquad
h_r:=\phi_r=\frac{K+\Pi R}{A}-\frac{(\Pi a)G}{A^2},
\quad K=\frac{r^2p(p_\theta-q/r)}{ub^3}.
\tag{3}
\]

这里 h_r 是角速度的名称，不是某个高度函数 h 的导数。
第二项在离解时必须保留。T_r=-h_r n，n_r=h_r T；
T_θ=-kn，n_θ=kT。

## 2. 用目标径向弧长消去纯坐标发散

取准确变量 s，使 ds=√E dr，记 χ=dr/ds=E^(−1/2)。固定同一场后该变量
与 θ 无关。它的用途是把目标度量写成 ds²+r(s)²dθ²；没有改变目标 g 或
将试值 E 重新求成另一个度量。

记

\[
P=Z_s=\chi p,\quad
U_0=\chi u,\quad V_0=\chi v=-Pq/b,\quad
h=\phi_s=\chi h_r.
\tag{4}
\]

真实 S 与 (2) 中相同：

\[
Y_s=V_0T+U_0n+S.
\tag{5}
\]

在同一 moving frame 中写

\[
s_T=S\cdot T,\quad s_n=S\cdot n,\quad
\dot s_T=S_s\cdot T,\quad \dot s_n=S_s\cdot n,
\]
\[
V=V_0+s_T,\qquad U=U_0+s_n.
\tag{6}
\]

点号在 (6) 中明确表示先对原平面向量求 s 导数、再投影。
它不是 moving-frame 标量的普通导数；准确换算为

\[
S_s\cdot T=(s_T)_s+h s_n,\qquad
S_s\cdot n=(s_n)_s-h s_T.
\tag{7}
\]

若漏掉 (7) 的两项，会把真实 Y_ss 错算成另一个向量。

定义两个实际径向加速度的平面分量

\[
L_T=(V_0)_s+U_0h+\dot s_T,\qquad
L_n=(U_0)_s-V_0h+\dot s_n.
\tag{8}
\]

由 (5) 直接微分，真实完整六个空间 jets 是

\[
\begin{split}
X_s&=(VT+Un,\ P),\\
X_\theta&=(bT,\ q),\\
X_{ss}&=(L_TT+L_nn,\ P_s),\\
X_{s\theta}&=(b_sT-bhn,\ q_s),\\
X_{\theta\theta}&=(b_\theta T-bkn,\ t),
\end{split}
\tag{9}
\]

其中

\[
b_s=(r r_s-qq_s)/b,\qquad b_\theta=-qt/b,
\]
\[
(V_0)_s=-\frac{P_sq+Pq_s}{b}+\frac{Pq\,b_s}{b^2}.
\tag{10}
\]

混合导数直接从准确 Y_θ=bT 求得，因此不需要另提供 S_θ 或把离散
mixed derivatives 当成相等。(9) 中唯一新增的缺陷导数是实际 S_s。

## 3. 实际法向与实际诱导度量

置

\[
C_N=Vq-Pb,\qquad
\mathcal Q=\sqrt{U^2r^2+C_N^2}.
\tag{11}
\]

若 Q>0，则当前真实曲面正则，并有

\[
\boxed{\nu=\frac{-Uq\,T+C_N n+Ub\,e_z}{\mathcal Q}.}
\tag{12}
\]

式 (12) 不除 νz，允许竖直接边上 νz=0。实际平面 Jacobian 为

\[
\det(Y_s,Y_\theta)=bU.
\tag{13}
\]

因此 r 内部的 b>0、U>0 支付 R645 所需的局部正图结构。核心接边允许
U→0；那里须由原 C² 端部坐标及竖直接边处理，不能把一个包含边缘的闭区间
要求成统一严格 U>0。

用目标单位基 ∂s、r^(−1)∂θ 表示真实诱导度量，得到

\[
g_X=
\begin{pmatrix} e&f\\f&1\end{pmatrix},\qquad
e=U^2+V^2+P^2,\quad f=(bV+qP)/r.
\tag{14}
\]

下角元素准确为一是因为 b²+q²=r²，尚未使用等距方程。其 determinant 为

\[
d=e-f^2=\mathcal Q^2/r^2
       =U^2+(C_N/r)^2>0.
\tag{15}
\]

区间实现宜使用 (15) 的正平方和，避免从两个接近的量相减。
因原 U0²+V0²+P²=1、bV0+qP=0，还可以得到 R643 的误差表达，但曲率
计算直接使用当前 e、f、d，不把它们强制设成 1、0、1。

## 4. 完整真实第二基本形式与主曲率

把真实第二基本形式在同一个目标单位基中记为 B。由 (9)、(12) 准确有

\[
\boxed{
B_{11}=\frac{-UqL_T+C_NL_n+UbP_s}{\mathcal Q},}
\]
\[
\boxed{
B_{12}=\frac{-Uq\,b_s-C_Nbh+Ubq_s}{\mathcal Q\,r},}
\]
\[
\boxed{
B_{22}=\frac{-Uq\,b_\theta-C_Nbk+Ubt}{\mathcal Q\,r^2}.}
\tag{16}
\]

即使目标连接与实际 Levi-Civita 连接不同，(16) 仍正确：第二基本形式
是 ν·X_ij，任何添加的切向 Christoffel 项都与 ν 正交。
但是把竖直分量 Hess_g Z 单独除以 νz，只在目标连接与实际连接相同
或补齐其差时才成立，不能用来取代 (16)。

对当前实际切向量作准确 Gram–Schmidt：

\[
E_2=X_\theta/r,\qquad
E_1=\{X_s-fE_2\}/\sqrt d.
\tag{17}
\]

这给当前 Euclidean 度量下的一组真正正交单位切基。形算子在其中为对称矩阵

\[
\boxed{
\mathcal B=
\begin{pmatrix}
(B_{11}-2fB_{12}+f^2B_{22})/d
 &(B_{12}-fB_{22})/\sqrt d\\
(B_{12}-fB_{22})/\sqrt d&B_{22}
\end{pmatrix}.}
\tag{18}
\]

两个真实主曲率是 (18) 的特征值。因此准确的最大绝对主曲率为

\[
\boxed{
K_{\rm abs}=\frac12\left(
|\mathcal B_{11}+\mathcal B_{22}|+
\sqrt{(\mathcal B_{11}-\mathcal B_{22})^2+4\mathcal B_{12}^2}
\right).}
\tag{19}
\]

给 (16)–(18) 中每个输入一个真实连续区间后，普通向外区间算式就包围 (19)。
同时可以使用对称矩阵的最大绝对行和上界，取两个已证上界的较小者；
这只收紧相同数据的代数包围，不改变要检查的实际曲面。

同一块的度量相对误差也可准确写为

\[
\eta=\frac12\left(|e-1|+\sqrt{(e-1)^2+4f^2}\right),
\tag{20}
\]

其为当前相对固定目标 g 的 operator norm，仍非任何新求度量。
实际 νz=Ub/Q 可同时用于 R640 的同对象高度门
Z−hc−τ|νz|；(19) 的 K≤1/τ 只是 R645 的一个假设，不能单独宣称全闭 reach。

## 5. 完整离解 S_s 的准确输入，不从小 S 猜小导数

R643 的完整连续场写为

\[
B_a=\Pi a,\quad
Q=\Pi R-B_aG/A,\quad
c=F/A,\quad d_b=b/A,
\]
\[
\mathcal H=c(NT+u_\theta JT)+d_bQJT,\qquad
S=\Pi\mathcal H/\sqrt E.
\tag{21}
\]

本节的 Q 是 R643 的相位缺陷，与第 3 节的 Qcalligraphic 不同。
R643 的高度关于角反射为偶函数，所以 p、b、u 为偶函数，B 为奇函数；
故 K 为奇函数，连续均值准确为零。由 A_r=G 及这一零均值，

\[
(B_a)_r=K+\Pi R,\qquad F_r=G,\qquad
G_r=\langle R_r\rangle.
\tag{22}
\]

于是

\[
Q_r=\Pi R_r-\frac{(K+\Pi R)G}{A}
             -\frac{B_aG_r}{A}+\frac{B_aG^2}{A^2},
\]
\[
c_r=G/A^2,\qquad (d_b)_r=b_r/A-bG/A^2.
\tag{23}
\]

令 HT=cN、HJ=c uθ+d_bQ，即 H=HT T+HJ JT。完整径向导数为

\[
\boxed{
\begin{split}
(\mathcal H_r)_T&=c_rN+cN_r-h_rH_J,\\
(\mathcal H_r)_{JT}
 &=c_ru_\theta+c\,u_{\theta r}+(d_b)_rQ+d_bQ_r+h_rH_T.
\end{split}}
\tag{24}
\]

包括最后两项 frame 导数和 (23) 的全部 G、Gr 项。这里不能先对 HT、HJ
分别取 scalar primitive 再拼回 T、JT；实际 ΠHr 必须作用于完整原平面向量
Hr(r,θ)，因为这个 frame 本身随 θ 变化。

对 (21) 真的求导，再变到同一个 s，得

\[
\boxed{
S_s=\frac1E\Pi\mathcal H_r-\frac{E'}{2E^2}\Pi\mathcal H.}
\tag{25}
\]

因此连续的 S、S_s 由同一个向量 primitive 体系给出；不依赖有限差分标签。
如果只有 S 的数值小量而没有 ΠHr 的界，本稿不会赋予任何曲率界。

## 6. R_r 与 H_r 所需的完整三 jets

为了明确 (24)–(25) 的费用和输入，记 pθ=q_r，p_rθ=q_rr，
t_r=p_θθ；它们由同一个高度函数产生，不是彼此独立的新自由标量。
在第 1 节的普通 r 坐标内，置

\[
B=p_\theta-q/r,\quad C=Et+rp,\quad
M=r+pt-q^2/r,\quad\omega=r^2/(u^3b^3),
\]
\[
D=Cp_r-EB^2-E'M/2,\quad R=\omega D.
\tag{26}
\]

直接求导：

\[
\begin{split}
b_r&=(r-qp_\theta)/b,\quad b_\theta=-qt/b,\\
v_r&=-(p_rq+pp_\theta)/b+pq\,b_r/b^2,\\
u_r&=\{E'/2-rp^2/b^2-r^2pp_r/b^2+r^2p^2b_r/b^3\}/u,\\
C_r&=E't+Et_r+p+rp_r,\\
B_r&=p_{r\theta}-p_\theta/r+q/r^2,\\
M_r&=1+p_rt+pt_r-2qp_\theta/r+q^2/r^2,\\
D_r&=C_rp_r+Cp_{rr}-E'B^2-2EBB_r-E''M/2-E'M_r/2.
\end{split}
\tag{27}
\]

从而

\[
\boxed{R_r=\omega D_r+(2/r-3u_r/u-3b_r/b)R.}
\tag{28}
\]

最后一项含当前真实 R；它不能在离解场中删除。
K、Kθ、Kr 的无人工零分母式为

\[
K=\frac{r^2pB}{ub^3},
\]
\[
K_r=\frac{2rpB+r^2(p_rB+pB_r)}{ub^3}
                       -K(u_r/u+3b_r/b),
\]
\[
K_\theta=\frac{r^2\{p_\theta B+p(t_r-t/r)\}}{ub^3}
                       -K(u_\theta/u+3b_\theta/b).
\tag{29}
\]

这些式子不除 p 或 B。再使用

\[
a_r=K_\theta+R,\qquad
u_{\theta r}=a_rv+a v_r-b_rK-bK_r,
\]
\[
N_r=b^{-1}-rb_r/b^2+
      \{2rpt+r^2(p_rt+pt_r)\}/b^3-3r^2ptb_r/b^4
\tag{30}
\]

便完整支付 (24)。所需新径向信息恰为 E''、p_rr、p_rθ、t_r 以及同一连续
角 primitive/均值。p_rr 包含真实 mean 的三阶导数，不能只增加旧非mean
三 jets；固定 seed mean 的这些导数同样要来自其真正定义。

这说明为什么原六 jet 离解残差可以很小，但实际连续曲率还需要另外的
导数消费。它不要求为一个已付 finite stencil 重新计算所有三 jets；
现成真实 Y_ss 区间若已存在，可以直接代入 (16)。

## 7. 核心接边的有限形式

原核心 W~k0(R−r)^(−α)、1/2<α<1 使目标弧长 s 达到有限端点；
χ→0。普通 r 表中的某些高度导数发散，不能据此把实际曲率判断成无穷。
在 s 表中，真实竖直接边的基准极限为

\[
q=0,\quad b=R,\quad P=-1,\quad U=V=0,\quad
\nu=n.
\tag{31}
\]

若原 C² 迹已经支付对应的 L_T=L_n=P_s=h=0，则 (16)–(19) 给

\[
B_{11}=B_{12}=0,\qquad B_{22}=-k/R=-1/\rho_\Gamma.
\tag{32}
\]

这正是同一个中央柱的两主曲率 0、−1/ρΓ。它不除 νz，也没有 0/0。
原 C² 迹若尚未付，本节只是指出准确需要的有限量，不能将 (31) 的
有限位置迹单独升格成 (32) 的二阶迹。

对实际核心 proof/interval producer，可直接提供正则 s jets 和 (8) 的
真实加速度来调用第 4 节。普通 r 的 (27)–(30) 只用于其实际有限的内部；
在边缘不通过浮点 infinity 相乘来伪造 χp 等有限极限。

## 8. 后继区间消费者

纯源码 scripts/r649_complete_offsolution_curvature_20261128.py 提供三个相连入口：

1. 从同一 r 块的三 jets、真实 A/G/Gr 以及完整 scalar primitives，形成
   (24) 的完整向量 kernel 和 (28)，保留所有离解项。
2. 在普通内部，从同一完整向量 ΠH、ΠHr 和准确归一相位，形成 (4)–(10)
   的正则 s 输入；此步不自行进行 FFT、mean 求根或新的角求积。
3. 从这些实际正则 jets，或已有真实 Y_ss 区间，直接计算 (11)–(20)
   的真实面积、法向、主曲率、metric、平面 Jacobian 及可选高度门。

输入区间必须来自同一个真正连续位置和高度，保留相同目标/参数身份及原源、
角和径向误差。消费者只证明所给连续区间的代数后果，并将未闭条件原样输出。
它不把样本值包成退化区间来冒充连续包围，也不为这份公式启动重复的科学 scope。
当前 R631/R643 的自然终态及原已付差分继续按原计划消费。
