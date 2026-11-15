# R812 — 原 first-p apolar 源、五个端项与 Gaussian Frobenius 低矩

日期：2026-11-15。状态：**本文的原源方程、特解及 p=5 mod12 时的 Frobenius 低五阶运输公式已证明。固定六个代数 FG 输出须由指定公开 Actions 核实；不预称其非零。原 primitive/Legendre 同标签共同单位仍开放。**

本篇接 [FT：全六 heat 平凡化与偶源](../notes/2026-11-15-sigma-full-heat-tame-trivialization-and-even-source.md)、OP、QS、R808、R810。
只使用原 c=0 sigma、原四个偶截面和两个奇截面；
不以完整非整普通 sigma 级数的模 p 约化代替 first-p 截断。

## 1. 原 first-p 配对及其所测的系数

保留
$$
p=6N+5\ge41,\quad Y^2=X^3+16,\quad DX=2Y,\quad DY=3X^2,
$$
$$
A(P_0)=0,\quad DA(P_0)=B\ne0,\quad D^2A=-XA/4,\qquad P_0=(0,4).
\tag{812.1}
$$
这里 X、Y 是辅助模曲线坐标。原椭圆曲线在 P_0 为
y^2=x^3-1，dz=dx/(2y)。沿用
$$
\Phi_e=(S,F,H,R)^t
=(\sigma^6,x\sigma^6,x^2\sigma^6,(x^3+Y/2)\sigma^6)^t,
$$
$$
\Phi_o=(J,G)^t=(y\sigma^6,-xy\sigma^6)^t.
\tag{812.2}
$$
所有下文使用的 Phi 都是已证整的次数小于 p 的普通 Taylor 截断。
令
$$
O=\partial_z^2/12+3Xz^2/4,\qquad
L=A\partial_z+6(DA)z.
$$
FT、MH、QS 的原方程为
$$
(D-O-M_e)\Phi_e
=-z^{p-1}\left(Ae_H/6+(DA)e_R/2\right)=:\mathcal S_e,
$$
$$
(D-O-M_o)\Phi_o=(A/12)z^{p-2}e_G=:\mathcal S_o,
\qquad [D-O,L]=0.
\tag{812.3}
$$

取常数 iota^2=-1，在 P=k(E)[z]/(z^p) 上定义
$$
\mathcal B(f,g)=[z^{p-1}]\,f(z)g(\iota z).
\tag{812.4}
$$
partial_z 是这个商环的真正导子。
对通常的顶系数型 <f,g>=[z^(p-1)]fg，分部积分给
partial_z^*=-partial_z，而乘 z 自伴。
因此 O 对 (812.4) 反对称，并且
$$
\mathcal B(Lf,g)=-\iota\,\mathcal B(f,Lg).
\tag{812.5}
$$
这些式子已在商环中处理边界，不能把商环改成允许跨 p 的普通 Taylor 级数。

定义实际 4 by 2 矩阵
$$
Q_{ab}=\mathcal B(L^2\Phi_{e,a},L^3\Phi_{o,b}).
\tag{812.6}
$$
在 P_0，L=6Bz，故对原
F=z^4 f(z^6)、G=z g(z^6)，准确有
$$
\boxed{
Q_{FG}(P_0)
=(6B)^5\sum_{j=0}^{N-1}(-1)^j f_{N-1-j}g_j.
}
\tag{812.7}
$$
这里包括第二变量 z^3 在 z mapsto iota z 下的 iota^3 因子；
它与 G 的首 iota 因子相乘为一。

这个交替卷积若非零，足以证明未筛的某一项
f_i g_(N-1-i) 非零。但它没有原 primitive 指示或
P_(6i+6)(1/s) 权，也不是 R770 的同标签乘积。
在 R808 的位置 Cartan 中，它属于一个端点观测值；
不能把端点观测与各个真正原 h 的中心观测混淆。

## 2. 完整有限源和一个实际特解

记 C=6DA、epsilon=iota^(p-1)=(-1)^((p-1)/2)，并令
$$
v_e=Ae_H/6+(DA)e_R/2.
$$
由 (812.3)--(812.5)，不删任何跨 p 边界，有
$$
\boxed{
DQ-M_eQ-QM_o^t
=v_e c_o^t-\frac{\epsilon A}{12}d_e e_G^t.
}
\tag{812.8}
$$
右端只涉及原不超过六阶的 jets：
$$
c_o=
\begin{pmatrix}
-360A^4DA\\
-9XA^5+540A^3(DA)^2
\end{pmatrix},
\tag{812.9}
$$
$$
d_e=
\begin{pmatrix}
720A^5\\
2160A^4DA\\
3240A^3(DA)^2+162XA^5\\
3240A^2(DA)^3+810XA^4DA+432YA^5
\end{pmatrix}.
\tag{812.10}
$$

为核对 (812.8)，先把两次左侧 L 移到右侧：
Q=-mathcal B(Phi_e,L^5Phi_o)。于是原源恰为
-mathcal B(S_e,L^5Phi_o)-mathcal B(Phi_e,L^5S_o)。
第一项取 L^5Phi_o 的常数项；第二项是
-epsilon A[z^1]L^5Phi_e/12。
正常排序
L^5=:L^5:+10AC:L^3:+15A^2C^2:L:
给出 (812.9)--(812.10)。

所用原低 jets 可独立写成
$$
\begin{array}{c|rrrr}
 &z^0&z^2&z^4&z^6\\ \hline
 S&0&0&0&1\\
 F&0&0&1&0\\
 H&0&1&0&9X/40\\
 R&1&0&3X/8&3Y/5
\end{array},
\qquad
J=-z^3+O(z^7),\quad
G=z-\frac{3X}{40}z^5+O(z^7).
\tag{812.11}
$$
这些式子来自原 sigma、x、y 的低阶展开；
显示分母对 p>=41 均为单位。

现在仅在 epsilon=1，即本允许族的 p=5 mod12 情形，定义
$$
\boxed{
Q_{\rm part}=
\begin{pmatrix}
0&0\\
0&-24A^6\\
-12A^6&-36A^5DA\\
-36A^5DA&-9XA^6
\end{pmatrix}.
}
\tag{812.12}
$$
逐行代入 M_e、M_o，使用 D^2A=-XA/4、DX=2Y、DY=3X^2，
得到它准确满足 (812.8)。
例如 SG、FG、HJ、RJ 四项分别给
-60A^6、-180A^5DA、-60A^5DA、-180A^4(DA)^2；
HG、RG 两项分别给
-180A^4(DA)^2-15XA^6、
-72XA^5DA-36YA^6，与 (812.9)--(812.10) 完全一致。
其余 SJ、FJ 项为零。

所以
$$
D(Q-Q_{\rm part})=M_e(Q-Q_{\rm part})+(Q-Q_{\rm part})M_o^t.
\tag{812.13}
$$
且 Q_part(P_0)=0。
这是一个真正的水平余项，不能用特征零单值群没有不变量把它删掉：
特征 p 的常数域包含 p 次幂，零 p 曲率允许非零有理水平截面。

## 3. 固定 canonical Gaussian 的 q 模型

本节先在特征零写定义，再仅将合法的 first-p 部分约化。
令 delta=-432，选一个固定 d_0 满足 d_0^12=delta，令
$$
\lambda=d_0\eta^{-2},\quad
a=\lambda^4E_4/12,\quad b=-\lambda^6E_6/216,\quad
X=a/3,\quad Y=b,\quad t=\lambda z.
\tag{812.14}
$$
E_2,E_4,E_6、eta 使用通常 q 级数规范；
theta=q d/dq，则
$$
D=\lambda^2\theta,\qquad
D\lambda=-\lambda^3E_2/12.
\tag{812.15}
$$
Ramanujan 的三个微分式逐项给 Da=6b、Db=a^2/3，
且 a^3-27b^2=lambda^12 eta^24=delta，
所以这正是 (812.1) 的同一辅助曲线和导子。

取奇 theta
$$
\vartheta(t,q)=
\sum_{n\in\mathbf Z}(-1)^n q^{(n+1/2)^2/2}e^{(n+1/2)t},
\qquad \partial_t\vartheta(0,q)=\eta^3.
$$
原 c=0 sigma 的准确式是
$$
\sigma(z)=\lambda^{-1}\eta^{-3}
 e^{-E_2t^2/24}\vartheta(t,q).
\tag{812.16}
$$
它的首项为 z，三阶项为零。
在第 p 个 Hurwitz 导数中，所有混合 binomial(p,j) 都为零；
半整数频率在 F_p 中满足 u^p=u。
由 (812.16) 以及 MH 的原 sigma_p=A，得到
$$
\boxed{A=\lambda^{p-1},\qquad
6DA=A\lambda^2E_2/2}
\tag{812.17}
$$
作为 q 展开上的模 p 等式。
这不声称 lambda 在 supersingular 点 P_0 是一个单位；
确实不能在 P_0 将 (812.17) 当作任意可逆解析 gauge 使用。

定义六个 degree-six theta 截面
$$
\Theta_r(t,q)=
\sum_{\substack{a\in\mathbf Z\\a\equiv r\ (6)}}
 q^{a^2/12}e^{at},\qquad
\Psi_r(z)=\eta^{-1}e^{-E_2t^2/4}\Theta_r(t,q),
\quad r\in\mathbf Z/6.
\tag{812.18}
$$
theta Theta_r=partial_t^2Theta_r/12；
结合 (812.15) 直接求导，得到 (D-O)Psi_r=0。
它们与 (812.2) 的六个截面有相同 degree-six automorphy，
所以存在同一规范的可逆矩阵 U，使
$$
\Phi=(S,F,H,R,J,G)^t=U\Psi,\qquad DU=(M_e\oplus M_o)U.
\tag{812.19}
$$
偶行 U_(a,r) 在 r mapsto-r 下对称，奇行反对称。

为固定共同尺度，取 z 导数阶 0,1,2,3,4,6。
Phi 的 jet 行列式是 -207360。
Theta_r 最低 q 项使用频率
0,1,2,{3,-3},-2,-1；
相应 jet 行列式的首系数为 207360。
乘上 lambda^16 eta^-6 后 q 阶恰抵消。
因原有限矩阵总迹为零，
$$
\boxed{\det U=-d_0^{-16}.}
\tag{812.20}
$$
等价地，反向的 theta 变换行列式为 -d_0^16。
任何后文选取的 Heisenberg 标准基只可差一个共同尺度；
不能将这个尺度或其 Frobenius 因子任意设为一。

## 4. first-p 指数截断必须扣掉的五项

在 P 中，Gaussian
exp(-E_2 lambda^2 z^2/4) 的微分公式准确成立：
其潜在末端乘法项的次数为 p，已在商环中为零。
由 (812.17)，L 在去掉这个 Gaussian 后恰为
A partial_z=A lambda partial_t。

但是线性指数 exp(az) 的 first-p 截断不是 partial_z 的完整特征向量。
L^2 使用的指数次数至多 p-3，L^3 使用的次数至多 p-4。
所以顶系数的二项式和只允许
$$
3\le m\le p-3.
\tag{812.21}
$$
不能直接用完整的 (a+iota b)^(p-1)。

设
$$
\mathcal P_0=A^5\lambda^{p+4}\eta^{-2}.
$$
在六个 theta 坐标中，原 Q 的被积矩为
$$
-\mathcal P_0\,a^2b^3
\left((a+\iota b)^{p-1}-R_0(a,b)\right),
$$
其中将五个漏出的 m=0,1,2,p-2,p-1 项准确约化以后，
$$
a^2b^3R_0(a,b)=
(\epsilon+1)a^2b^3+\epsilon\iota a^3b^2
-\epsilon a^4b-\iota ab^4.
\tag{812.22}
$$
负号来自 Wilson：(p-1)!=-1。
(812.22) 不用除以 a 或 b，故二者在模 p 为零时仍成立。
每项还带原 q^((a^2+b^2)/12) 和原 residue classes (r,s)。

投到原 even by odd 两行列后，奇 a 次数或偶 b 次数自动消失。
在 epsilon=1 时，若再将完整幂写成一减去零指标，
非格点部分准确为
$$
\mathcal P_0(a^2b^3-a^4b).
\tag{812.23}
$$
设 h_0=E_2 lambda^2/4=3DA/A（只在 q 字段中使用）。
将 (812.23) 的 theta 导数改回原 Gaussian 后的低 jets，所得是
$$
A^6\left(
\Phi_e''(\Phi_o''')^t-\Phi_e''''(\Phi_o')^t
-6h_0\Phi_e''(\Phi_o')^t+2h_0\Phi_e(0)(\Phi_o''')^t
\right)_{z=0}.
\tag{812.24}
$$
用 (812.11) 代入，(812.24) 逐项恰是 (812.12)。
因此独立的 q 展开推导与完整源方程给同一个特解，
包括两个 -36A^5DA 项；五个端项不可省略。

## 5. 真正 Gaussian 理想重指标和 Frobenius 低矩

以下仍只考虑 p=5 mod12，所以 iota 属于 F_p。
在每个整数频率对上
$$
(a+\iota b)^{p-1}=1-1_{\{a+\iota b=0\ {\rm mod}\ p\}}.
\tag{812.25}
$$
固定所选 p-adic 嵌入，选 Gaussian 素数
$$
\pi=m+n i,\quad m^2+n^2=p,\quad m+\iota n=0\pmod p.
\tag{812.26}
$$
i 是特征零的指定平方根，i mod p=iota。
(812.26) 从 pi 与共轭 pi 中准确选出一个；不可混用两种选择。
该零指标的整数格正是 pi Z[i]。
因 p 与 6 互素，乘 pi 对模 6 特征是可逆的。

写
$$
a=mc-nd,\qquad b=nc+md.
\tag{812.27}
$$
则 a^2+b^2=p(c^2+d^2)，且原 residue classes
(r,s) 变为
$$
(r',s')=
\begin{pmatrix}m&-n\\n&m\end{pmatrix}^{-1}(r,s)
\quad\bmod6.
\tag{812.28}
$$
由 n=iota m mod p，有
$$
a^2b^3=-\iota m^5(c-\iota d)^5\pmod p.
\tag{812.29}
$$

定义完整六 by 六低矩
$$
K^\Psi_{rs}
=\left.\partial_z^5\bigl(\Psi_r(z)\Psi_s(-\iota z)\bigr)\right|_{z=0}.
\tag{812.30}
$$
两个 canonical Gaussian 正好抵消，所以
$$
K^\Psi_{rs}
=\eta^{-2}\lambda^5
\sum_{\substack{c\equiv r(6)\\d\equiv s(6)}}
(c-\iota d)^5q^{(c^2+d^2)/12}.
\tag{812.31}
$$
这是低五阶导数，不是普通第五系数，因而保留 5!。

令 mathscr P_pi 对六 by 六矩阵作 (812.28) 的条目重排。
用 (812.17) 比较全部 eta、lambda 因子：
$$
\frac{A^5\lambda^{p+4}\eta^{-2}}
     {(\eta^{-2}\lambda^5)^p}
=(\lambda\eta^2)^{p-1}=d_0^{p-1}.
\tag{812.32}
$$
因此真实水平余项在 theta 坐标中，准确是
$$
-\iota m^5d_0^{p-1}\,
\mathscr P_\pi\bigl((K^\Psi)^{(p)}\bigr),
\tag{812.33}
$$
再取原 even by odd 行列。
这里 (p) 是逐条目和全部 q 幂的 Frobenius；
它不是保系数不动的变量重命名。

写 U_e 为 U 的前四行、U_o 为末两行，
K^\Phi 为原六截面的同一低矩。
由于 K^\Psi=U^{-1}K^\Phi U^{-t}，完整原基公式为
$$
\boxed{
Q-Q_{\rm part}
=-\iota m^5d_0^{p-1}\,
U_e\,
\mathscr P_\pi\left((U^{-1}K^\Phi U^{-t})^{(p)}\right)
U_o^t.
}
\tag{812.34}
$$
m 非零模 p，d_0 在 p>3 为单位。
pi 改乘 Gaussian 单位时，(m,n)、特征重排以及低矩方向都必须同时按
(812.26)--(812.31) 变动，不能单独改一个因子。
(812.34) 保留这种选择，而不是把公共相位删掉。

在 P_0，(812.11) 给实际低矩
$$
\boxed{
K^\Phi(P_0)=120\bigl(
e_Ge_F^t+e_Je_H^t
-\iota e_Fe_G^t-\iota e_He_J^t
\bigr).
}
\tag{812.35}
$$
在一般辅助点还多
36X(e_Ge_R^t-iota e_Re_G^t)；
故 (812.35) 只在明确的 P_0 使用。
这把所需交替卷积的水平余项定位为四个已知低项的实际有限运输，
并未仅以整个运输算子可逆证明其 FG 条目非零。

## 6. 在原 CM 点固定 Heisenberg 基，不任意选 theta 相位

以下固定特征零 E_0:y^2=x^3-1 的正实周期 Omega。
设 alpha^3=4 为正实根，t_3=sqrt(3)>0，
zeta=(-1+i t_3)/2，rho=(1+i t_3)/2。
取 Q_0=Omega/6、P_0^{tor}=zeta Omega/6；
此处 P_0^{tor} 是六阶挠点，不是辅助模曲线的 P_0。

同一规范中
$$
2Q_0=(\alpha,-t_3),\qquad 3Q_0=(1,0).
\tag{812.36}
$$
在函数基
$$
\mathcal R=(1,x,x^2,x^3+2,y,-xy)
$$
上，canonical theta 平移可用如下 Miller 乘数准确表示：
$$
T_{\Omega/2}f
=\frac{(x-1)^3}{3t_3}\,f(\,\cdot+(\,1,0\,)),
\tag{812.37}
$$
$$
T_{\Omega/3}f
=\frac{(y+t_3-t_3\alpha^2x/2)^2}{12}\,
 f(\,\cdot+(\,\alpha,-t_3\,)).
\tag{812.38}
$$
这两个式子表示平移后再除公共 sigma^6 的原有理函数作用。

常数可以直接核：
x(z+Omega/2)-1=3/(x-1)，所以未归一乘数两次相乘为 27；
正实 sigma 规范选 1/(3sqrt(3))。
对 (812.38) 的线 l=y+t_3-t_3alpha^2x/2，
l 在 -(alpha,-t_3) 有三重零，D^3l/3!=12，
且 l(alpha,-t_3)^2=12。
三次平移的未归一平方乘数积为 12^3，
正实规范选 1/12。没有遗留任意二次或三次单位根。

将 x 坐标分别乘 zeta、y 保持不变，便得到 zeta Omega 方向；
CM sigma(zetaz)=zeta sigma(z) 保证同一归一化常数。
令 H_Q、H_P 为在 Phi 列基上对应的行作用矩阵：
T_Q Phi=H_Q Phi，T_P Phi=H_P Phi。
由 Q_0=Omega/2-Omega/3，有
H_Q=H_(Omega/3)^(-1)H_(Omega/2)，zeta 方向同理。

原 Legendre 关系给 T_Q T_P=rho T_P T_Q。
由于这里的行作用矩阵反转算子复合次序，矩阵检查是
$$
H_PH_Q=\rho H_QH_P.
\tag{812.39}
$$
选择 H_Q 的特征值 1 的一个非零列 u_0，并令
$$
\widehat U_r=H_P^{-r}u_0,\qquad0\le r<6.
\tag{812.40}
$$
则 H_Q Uhat=Uhat diag(rho^r)，
H_P Uhat=Uhat Shift，其中 Shift 的 (r,r+1) 项为 1。
(812.18) 的 theta 基也有这两个准确作用：
实 Omega/6 平移的特征值为 rho^r，
zeta Omega/6 平移送 Psi_r 到 Psi_(r+1)。
故实际 U(P_0) 与 Uhat 只差一个共同非零尺度 c，而不是六个独立相位。

由 (812.20)，
$$
c^6=-d_0^{-16}/\det\widehat U.
\tag{812.41}
$$
用 Uhat 代替 U 时，(812.34) 另保留共同因子 c^(2-2p)。
对于零与非零的判断，这个因子不能创造或消灭条目；
对于 p 单位的判断，须先排除 det Uhat 与其整分母的有限坏素数，
不能没有检查就将 c 设为单位。

### 6.1 从 q 恒等到 supersingular CM 评价

(812.34) 的右边使用的是 level-six 代数变换矩阵 U。
它可由同一 Miller/Heisenberg 本征线、六阶挠点的 Weil 配对，
以及 (812.20) 的行列式归一代数化：
先取标准 Heisenberg 本征基，唯一的共同尺度再由其六次幂固定。
所用代数盖由六阶挠点和这些有限次单位根/尺度构成；
在 p 不整除 6 的好约化处，q 展开给该代数函数域的同一分支。

因此先将 (812.34) 视为这个代数函数域上的恒等式，
再在所选 CM 点评价。CM 处的实际整性由 Uhat 的清分母、
det Uhat 的整 Norm、d_0^12=-432 及 (812.41) 检查；
只有排除这些实际有限坏素数后，U、U^{-1}、c 才按所用规范作为单位数据约化。
未执行指定有限计算之前，不预称该坏素数清单已得到。

这个过程没有把 q 参数、lambda 本身或原非整的完整 sigma
当成 supersingular 单位，也没有从普通 q 盘直接搬运一个任意解析 gauge。
所约化的 sigma 输入始终只有已证整的 first-p 截断；
Frobenius 右边则先经 level-six 代数矩阵和共同尺度成为可评价的原对象。

## 7. 固定六个有限代数案例及公开执行 contract

整个 CM Heisenberg 计算在固定十二次域
$$
K=\mathbf Q(\alpha,\sqrt3,i)
$$
内进行。对于 p=5 mod12 且 p>3，
$$
i^p=i,\qquad(\sqrt3)^p=-\sqrt3,\qquad
\alpha^p=\zeta^j\alpha
$$
中恰有一个 j in {0,1,2}。
这是实际的三个 tame Frobenius 可能；不能把 Frobenius 当成 K 上的恒等。

每个选定 pi 可乘 Gaussian 单位，唯一到如下两个 residue types 之一：
$$
\pi\equiv1+2\epsilon_\pi i\pmod6,\qquad\epsilon_\pi=\pm1.
\tag{812.42}
$$
因为 p=5 mod12，Gaussian 两坐标奇偶相反，且模 3 都非零；
(812.42) 覆盖所有情形。其逆特征变换为
$$
(r,s)\longmapsto(-r-2\epsilon_\pi s,\ 2\epsilon_\pi r-s)\pmod6.
\tag{812.43}
$$

因此对 j=0,1,2 与 epsilon_pi=+1,-1，
需要核的实际原 FG 条目只有以下六个固定 K 中的代数数：
$$
\boxed{
\left[
\widehat U\,
\mathscr P_{\epsilon_\pi}
\left(\tau_j(\widehat U^{-1}K^\Phi(P_0)\widehat U^{-t})\right)
\widehat U^t
\right]_{FG}.
}
\tag{812.44}
$$
这里 tau_j 对 i 固定、sqrt3 变号、alpha 送 zeta^jalpha。
(812.35) 的四个低项都在 (812.44) 中保留。
不能用整个矩阵的可逆性代替这一个条目的真实值。

指定源码：
scripts/R812_tame_theta_transport.py。
执行只允许公开 Rogerhu12/math-research-public 的 Actions，命令
sage -python topics/serre-uniformity/scripts/R812_tame_theta_transport.py。
程序在导入 Sage 或进行任何数学运算之前，强制核对 GITHUB_ACTIONS=true 与
GITHUB_REPOSITORY=Rogerhu12/math-research-public；没有本地绕过参数。
它输出实际源码 SHA256、run/attempt/commit/ref 及 Python/Sage 版本。
程序不循环素数，不重算任何高阶 sigma 系数；
它检查原 Miller 平移、六阶数、Heisenberg 相位、标准 theta 基，
再计算上述六个条目。

程序为每个条目先在积分幂基中清有理分母，再给整 Norm，
同时保存 Uhat 的公共分母和 det Uhat 的整 Norm。
这一区分是必要的：非零代数数的裸 Norm 非零，
并不能在某个素数处同时保证整性和单位性。
公开运行结果尚未在本文预称返回。
若六个条目均非零，才可按这些有限常数的坏素数清单得到
相应的充分大 p 未筛非零结论；若有零条目，必须保留其实际 residue type。

## 8. 严格保留的两项缺口

第一，p=3 mod4 时 iota 不在 F_p。
对非零 (a,b)，
(a+iota b)^(p-1)=(a-iota b)/(a+iota b)，
而不是 (812.25)。
它不能被替换为一个 index-p Gaussian 素理想指标。
本篇的 (812.8) 仍成立，但 (812.12)、(812.25)--(812.44) 只用于
明确说明的 p=5 mod12 分支。

第二，即使 (812.44) 的 FG 条目在某些或全部 residue types 为单位，
(812.7) 只给未筛交替总和非零。
它尚未给同一个 primitive h 上
P_(h-1)(1/s)f_i g_(N-1-i) 非零；
更未给原 canonical height 的 common-root 排除。
本文不把任何中间有限运输结论当作 Serre uniformity 完成。

## 依赖和外部规范

- [FT：全六 heat 平凡化与偶源](../notes/2026-11-15-sigma-full-heat-tame-trivialization-and-even-source.md)、MH、OP、QS：原有限 heat 矩阵、first-p 两种源、Hasse 及水平 L。
- R808：原 split/period 规范及区分位置 Cartan 与 phase Cartan。
- R810：原 toric 线的全部单位矩；本篇不删除其中保留的交换子。
- 原 R770：same-h 目标及原 f_i、g_j。
- Bunkova, arXiv:1701.00848v2, equation (1), Corollary 3.4：
  canonical sigma heat 规范。
- Rodriguez Villegas, frvillegas.github.io/pdf/frv-cm-theta.pdf，
  equations (2.8), (2.16)：sigma/theta 的同一 Gaussian 规范。
- DLMF 20.7、23.18：theta、eta 的标准变换规范。
  本文的 lambda、A、低矩及 five-boundary 常数在正文逐项推导，
  没有以未核的文献归一替代原对象。
