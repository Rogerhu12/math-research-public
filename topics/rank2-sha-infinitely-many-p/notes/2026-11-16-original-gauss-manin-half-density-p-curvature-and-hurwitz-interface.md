# 原 Gauss–Manin 半密度的准确 p-曲率与除幂接口

日期：2026-11-16。**状态：以下原参数曲线上的规范 p-曲率矩阵、Riccati 半密度算子及其完整 Hurwitz 块递推已证明。四个指定除 p 首行非零仍开放。**

本注使用 [R855](../results/R855-original-full-heat-connection-and-canonical-divided-jet.md)、
[R856](../results/R856-original-full-hurwitz-frobenius-recurrence-and-universal-divisibility.md) 的同一参数和 Hasse 多项式。新增变量 \(v\) 只是下述标量生成参数，不是原 \(t=-x^{-3}\)，也不是新增算术来源。

## 1. 同一参数导子及其受限 p 次幂

固定原 \(p=6s-1>211\)，在
\[
k=\mathbf F_p,\qquad A=k[g_2,g_3],\qquad
D=6g_3\partial_{g_2}+\frac{g_2^2}{3}\partial_{g_3}
\]
中记
\[
\Delta=g_2^3-27g_3^2,\quad a=g_2/12,\quad
H=[x^{p-1}](x^3-g_2x/4-g_3/4)^{(p-1)/2},\quad C=DH.
\tag{1}
\]
R856 已付
\[
D^2H+aH=0.
\tag{2}
\]

准确有
\[
\boxed{D^p=0\quad\text{在 }A\text{ 及 }\operatorname{Frac}(A)\text{ 上}.}
\tag{3}
\]
证明：\(D\Delta=0\)。令 \(X=g_2/3,Y=g_3\)，则
\[
Y^2=X^3-\Delta/27,\qquad DX=2Y,\quad DY=3X^2.
\]
在泛型 \(\Delta\ne0\) 纤维，这是同一个 j=0 椭圆曲线的不变导子。
R855 的不变导子 Hasse 公式在这里给
\(D^p=H_{\rm par}D\)，其中
\[
H_{\rm par}=[X^{p-1}](X^3-\Delta/27)^{(p-1)/2}=0:
\]
\(p-1=6s-2\) 不是3的倍数。故在泛型函数域有(3)，再由多项式身份延拓到 \(A\)。因 \(D^p\) 是导子，结论也延至其分式域。在任一有限可分代数扩域上，延拓的 \(D^p\) 仍为零：它杀底域，而可分代数扩域没有相对导子。

这里的 \(D\) 是参数导子，不是 R856 的物理 \(z\) 导数。

## 2. 规范周期方程的完整矩阵

保同一参数周期方程
\[
D\ell=r,\qquad Dr=-a\ell,\qquad
M=\begin{pmatrix}0&1\\-a&0\end{pmatrix}.
\tag{4}
\]
它的规范可直接由原不变微分
\(\omega=dx/(2y),\eta=x\omega\) 读取：
R855 的代数横向提升满足
\[
\nabla_D\omega=\eta,\qquad
\nabla_D\eta=-a\omega
\]
（第二式用 \(dy=(3x^2-g_2/4)\omega\) 消去准确项）。
因此没有重选周期或乘一个未定常数。

定义多项式矩阵
\[
P_0=I,\qquad P_{j+1}=DP_j+P_jM.
\tag{5}
\]
对任何形式解向量 \((\ell,r)^t\)，有
\(D^j(\ell,r)^t=P_j(\ell,r)^t\)。

**定理1。**
\[
\boxed{
P_p=
\begin{pmatrix}
HC&-H^2\\ C^2&-HC
\end{pmatrix}.
}
\tag{6}
\]
这给周期迭代 \(D^pY=P_pY\)。若采用列连接 \(D-M\)，其 p-曲率矩阵为 \(-P_p\)；以下 Riccati 算子按明确的(15)定义，不混用这两个符号。

### 2.1 先将未定系数严格压成常数

将(4)作用在两列代数独立的形式变量 \(Y\) 上，并倒置 \(\det Y\)。
由 \(\operatorname{tr}M=0\)，\(D(\det Y)=0\)。
由于 \(D^p\) 在特征 p 为导子，(5)给
\[
0=D^p(\det Y)=\operatorname{tr}(P_p)\det Y,
\quad\text{故 }\operatorname{tr}P_p=0.
\tag{7}
\]
(2)说明 \((H,C)^t\) 也是(4)的解；(3)于是给
\[
P_p(H,C)^t=0.
\]
在分式域中，迹零与这个核向量准确迫
\[
P_p=\kappa
\begin{pmatrix}HC&-H^2\\C^2&-HC\end{pmatrix}
\tag{8}
\]
，先不认 \(\kappa\) 是常数或单位。

接着证明 \(H,C\) 在 \(k[g_2,g_3]\) 互素。可先扩到 \(\bar k\)。
按权 \((4,6)\)，\(H\) 齐次，权为 \(p-1\)。
其可能的齐次不可约因子只有 \(g_2,g_3\) 和
\(g_2^3-cg_3^2\)。其中唯一被 \(D\) 保持的因子是 \(\Delta\)，因为
\[
D(g_2^3-cg_3^2)=\frac23(27-c)g_2^2g_3.
\]
在结点参数
\[
g_2=12u^2,\qquad g_3=-8u^3
\tag{9}
\]
上，原三次式为 \((x-u)^2(x+2u)\)。令 \(n=(p-1)/2\)。
模 p 展开
\((x-u)^{p-1}=\sum_{i=0}^{p-1}u^{p-1-i}x^i\)
逐项给
\[
\boxed{H|_{\Delta=0}=(3u)^n,}
\tag{10}
\]
故 \(\Delta\nmid H\)。

若非不变因子 \(Q\) 在 \(H\) 中重数为 \(d\ge2\)，则
\(d<p\)，而(2)左端的最低 Q 阶项为
\[
d(d-1)Q^{d-2}(DQ)^2(H/Q^d),
\]
在 \(Q\) 上不为零，矛盾。若重数为1，则 \(Q\nmid DH\)。
这证明互素性，且没有仅假设 Hasse 零点简单。

(8)的两个非对角项为多项式且 \(H^2,C^2\) 互素，故 \(\kappa\) 为多项式。
(5)的四个权分别为 \(2p,2p-2,2p+2,2p\)，与(8)中的对应项相同；
所以 \(\kappa\) 权为0，必为 \(k\) 中常数。

### 2.2 用同一结点规范确定常数恰为一

在(9)上
\[
Du=-2u^2,\qquad a=u^2,\quad H=(3u)^n,\quad C=uH.
\tag{11}
\]
在微分域中添一个变量 \(\rho\)，仅规定 \(D\rho=-2u\)。
取
\[
\ell_1=u^n,\qquad \ell_2=u^n\rho.
\]
两者都满足 \(D^2\ell+a\ell=0\)，Wronskian 为
\(-2u^p\ne0\)。直接迭代给
\[
D^p\rho=(-2)^p(p-1)!u^p=2u^p,\qquad
D^p\ell_2=2u^{p+n}.
\tag{12}
\]
这里用 Wilson 恒等式及 \(2^p=2\)；没有将 \(\rho\) 解释成一个有理对数。

另一方面，(8)第一行在 \(\ell_2\) 上为
\[
\kappa(HC\ell_2-H^2D\ell_2)
=2\kappa H^2u^{n+1}
=2\kappa u^{p+n},
\]
因为 \(3^{p-1}=1\)。故 \(\kappa=1\)，证明(6)。

在原 CM 点 \(P=(0,-4b)\)，R856 给 \(H(P)=0,C(P)=c_p\ne0\)，因此
\[
\boxed{P_p(P)=\begin{pmatrix}0&0\\c_p^2&0\end{pmatrix}.}
\tag{13}
\]
这个单位矩阵元属于 Gauss–Manin 周期连接，尚不是原四个 B 值。

## 3. Riccati 与半密度的精确 p 次幂

令 \(\partial=\partial_v\)。R855 的通用标量算子为
\[
\mathcal T_0=1,\quad\mathcal T_1=D,\qquad
\mathcal T_{j+1}=D\mathcal T_j-\frac{j(2j-1)g_2}{24}\mathcal T_{j-1}.
\tag{14}
\]
定义同一个一阶算子
\[
\boxed{\mathcal Q=D-(1+av^2)\partial-\frac a2v.}
\tag{15}
\]
在普通有理函数环 \(\operatorname{Frac}(A)(v)\) 上，准确有
\[
\boxed{
\mathcal Q^p=(H+Cv)^2\partial+\frac C2(H+Cv).
}
\tag{16}
\]

为支付半密度及符号，在(4)的微分扩域中置 \(v=-\ell/r\)。
则
\[
Dv=-1-av^2,\qquad Dr=avr.
\]
再有限扩域取 \(r^{1/2}\)。对函数 \(F(v)\)，
\[
D(r^{-1/2}F)
=r^{-1/2}\mathcal QF.
\tag{17}
\]
这就是(15)中的真实半密度，不是删去的 gauge。

用(6)及 \(D^p\) 的导子性，
\[
D^pv=(H+Cv)^2,\qquad
D^pr/r=-C(H+Cv).
\tag{18}
\]
对 \(r^{-1/2}\) 再用同一个导子，得到
\[
D^p(r^{-1/2})/r^{-1/2}=\frac C2(H+Cv).
\]
结合(17)、底域上的(3)即得(16)。

若只在普通有理函数环讨论(16)的核，则
\[
\ker(\mathcal Q^p)
=(H+Cv)^{(p-1)/2}\operatorname{Frac}(A)(v^p).
\tag{19}
\]
这是 \(\partial_v\) 的核计算。在 \(H=0,C=c_p\) 的系数特化中，
右侧一阶算子为
\[
c_p^2v(v\partial+1/2).
\tag{20}
\]
(19)–(20)不允许直接套到下一节的除幂级数；两种环中的 \(\partial^p\) 不同。

## 4. 真正 Hurwitz 环必须保留的 \(-\partial^p\)

令 \(L/\operatorname{Frac}(A)\) 为任意有限可分扩域，延拓 D。
在
\[
\mathscr H_L(v)=\{\sum_{j\ge0}q_jv^{[j]}:q_j\in L\},
\quad
\partial v^{[j]}=v^{[j-1]}
\]
上，\(D^p=0\) 仍成立，但 \(\partial^p\ne0\)，而普通乘积 \(v^p=0\)。
所以真正的恒等式是
\[
\boxed{
\mathcal Q^p=-\partial^p+
 (H+Cv)^2\partial+\frac C2(H+Cv).
}
\tag{21}
\]

可在 commuting \(D,\partial\) 的微分算子环中核对这一步。
Jacobson 的 p 次幂展开把
\((D-(1+av^2)\partial)^p\) 写成
\(D^p-(1+av^2)^p\partial^p\) 与一个一阶向量场之和：
交叉项是迭代交换子，而这些交换子仍为一阶 \(\partial\) 项。
添入乘法项 \(-av/2\) 后只再添乘法项。
普通有理函数环中 \(D^p=\partial^p=0\)，所以两个低阶系数已由(16)唯一确定。
在除幂环中 \(v^p=0\)，从而 \((1+av^2)^p=1\)，给出(21)。
这同时解释为什么在普通环中算出的 p-曲率不能删掉除幂环的最高导数。

对任何 \(f\in L\)，完整生成函数
\[
\mathscr K_f(v)=\sum_{j\ge0}(\mathcal T_jf)v^{[j]}
\tag{22}
\]
由(14)准确满足 \(\mathcal Q\mathscr K_f=0\)。
将(21)用于(22)，得到
\[
\partial^p\mathscr K_f
=(H+Cv)^2\partial\mathscr K_f+\frac C2(H+Cv)\mathscr K_f.
\tag{23}
\]
逐除幂系数读取，约定 \(\mathcal T_{-1}=0\)，遂有对全部 \(j\ge0\)
\[
\boxed{
\mathcal T_{p+j}f
=H^2\mathcal T_{j+1}f
+HC(2j+1/2)\mathcal T_jf
+C^2j(j-1/2)\mathcal T_{j-1}f.
}
\tag{24}
\]
它是完整实际输入的统一递推，不把 \(\mathscr K_f\) 当普通 p-整 Taylor 级数。

## 5. 与原物理二次 Frobenius 的逐项相认

对 R855 的一个真实水平截面 \(R\)，令 \(f=\varepsilon(R)\)。
同一热递推给
\[
j_{m,2r}(R)=(2m)^r\mathcal T_rf.
\tag{25}
\]
这里在一个实际代数水平扩域及其可分好约化处解释；该水平基须另行构造，(24)本身对任意有限可分系数扩域已经成立，不需要选择新的 theta 来源。

R856 的物理导子 \(D_z\) 满足
\(D_z^pA=HD_zA+mCzA\)。
重复同一导子而完整保 \(D_z(zA)=A+zD_zA\)，准确得到
\[
D_z^{2p}A
=H^2D_z^2A+2mHCzD_zA+mHCA+m^2C^2z^2A.
\tag{26}
\]
用(25)与 \((2m)^{p-1}=1\) 逐系数归一，(26)正是(24)，
包括 \(HC/2\) 与 \(j(j-1/2)\)，没有缺掉常数项。

特别在原 CM 点，
\[
\mathcal T_{p+j}f(P)=c_p^2j(j-1/2)\mathcal T_{j-1}f(P),
\quad
\mathcal T_{p+1}f(P)=c_p^2f(P)/2.
\tag{27}
\]
这与原 \(j_{m,2p+2}=2m^2c_p^2j_{m,0}\) 同一，不是原
\(N=(p+1)/2\) 处 \(\mathcal T_N/p\) 的非零判据。

## 6. 继续保留的真正问题

R856 的 \(\mathcal R_p=(D^2H+g_2H/12)/p\) 是固定特征零 Hasse 提升的除 p 缺陷；
本注(2)、(6)、(21)是它相应的模 p 几何结构。
其 CM 横向二阶 \(110bc_p\) 与本注 \(c_p^2\) 都是已知单位，
但它们处于明确不同的行。

四个原输入的目标仍为
\[
\mathfrak B_{\nu,p}
=(2m_\nu)^N\,\mathcal T_N f_\nu^{\rm flat}(P)/p\bmod p,
\qquad N=(p+1)/2,
\]
其中 \(f_\nu^{\rm flat}\) 必须来自同一原纤维向量的水平提升。
这不是任意核向量，除法也必须保原模 \(p^2\) 初始资料。
有限 theta 水平格上的零 p-曲率不消去(21)中的真实 Gauss–Manin 半密度；
反过来，(13)或(20)的非零也不直接迫四个指定首值之一非零。

本注无新增数学程序执行、素数扫描或可重算输出。
核心 p-曲率常数、互素性、结点规范及除幂区别均已在上文证明；
既有 R79 的 Legendre 规范未被无常数地移用。
