# R254 — 四个原八次 ray 完整覆盖原伴随、准确二处常数与全四阶中央转置

日期：2026-11-13。**状态：四个原八次 ray 的准确有理式、真实共轭 CM17 迹、到 R235 四条原八次伴随线的可逆矩阵、两条原伴随的反解、保全部连接和移权的四阶 Mellin 转置，以及 norm-two 常数的完整水平核已证明。原秩二曲线的无穷素数中央非零仍未证明。**

本篇把 [R253](R253-four-octic-ray-logarithms-and-norm2-constants.md)
的四个实际八次对数送到 [R235](R235-original-octic-sources-and-regularized-seven-dimensional-companion.md)
的原伴随，使用同一 CM17 迹和 R246 的实际双向二处运输。
四个 ray 对数常数并不自动成为四条新的中央非零行：下面精确写出
它们被原二阶协变微分杀掉的位置，以及转置以后仍须保留的全部项。

## 1. 四个实际二阶 ray 函数及其非零首项

沿用
$$
E_0:y^2=x^3-x,\qquad dz=dx/(2y),\qquad
\beta=4-i,\quad\bar\beta=4+i,\quad U=x(z)^2.
$$
取 $P\in E_0[\beta]\setminus\{O\}$，$\zeta=\zeta_8$，并取
R253 的原角色 $\chi_k(3)=\zeta^k$，$k=1,3,5,7$。记
$$
\Phi_k(z)=\sum_{a\in\mathbf F_{17}^{\times}}
\chi_k(a)^{-1}\log_p r(z+aP)-C_k,\qquad
r=\frac{x-1}{x+1}.
$$
因为 $\sum_a\chi_k(a)^{-1}=0$ 及
$(\log r)''=-4-8/(x^2-1)$，准确有
$$
B_k(z):=-\frac18\Phi_k''(z)
=\sum_a\frac{\chi_k(a)^{-1}}{x(z+aP)^2-1}.
\tag{1}
$$
这是固定代数椭圆函数，且 $B_k(iz)=-B_k(z)$。

写 $X=x(z),A=x(P),V=A^2$。原加法公式直接给
$$
\begin{aligned}
&B(z+P)+B(z-P)-B(z+iP)-B(z-iP)\\
&\quad=XA\,
\frac{8(U+1)(V+1)\{3(U^2+1)(V-1)^2+U(-6V^2+28V-6)\}}
{\{(V-1)^2(U^2+1)-2(V^2+6V+1)U\}^2},
\qquad B=\frac1{x^2-1}.
\end{aligned}
\tag{2}
$$
其原 $z^2$ 系数为 $24A(V+1)/(V-1)^2$，不是另取一个归一质量。

令 $g(V)=x(3P)^2$、$k(V)=x(3P)/x(P)$，在真实四次商环
$$
\mathcal K=\mathbf Q(\zeta)[V]/K_\beta(V),\qquad
K_\beta=(4-i)V^4+(-12+20i)V^3+(28+10i)V^2+(-20-12i)V-i
$$
中计算。准确有
$$
k(V)=\frac{V^4+12V^3+30V^2-36V+9}{(3V^2-6V-1)^2},
\qquad g=Vk^2,\qquad g^{\circ4}=V,
\qquad\prod_{j=0}^3k(g^{\circ j}V)=-1.
$$
于是 $b_k=[z^2]B_k$ 的准确表达是
$$
\frac{b_k}{A}=\sum_{j=0}^3\zeta^{-kj}
\frac{x(3^jP)}{x(P)}\,
\frac{24(g^{\circ j}(V)+1)}{(g^{\circ j}(V)-1)^2}.
\tag{3}
$$
证书分别给出 (3) 在 $\mathcal K$ 中的乘法逆，故四个 $b_k$
都非零。特别 $\Phi_k=-2b_kz^4/3+O(z^8)$。

令
$$
\begin{aligned}
D_\beta(U)={}&U^8+(-56+80i)U^7+(156-32i)U^6+(1144+176i)U^5\\
&+(-2234+576i)U^4+(1144+176i)U^3+(156-32i)U^2\\
&+(-56+80i)U+1.
\end{aligned}
$$
四个完整归一函数准确为
$$
\boxed{\frac{B_k}{b_k}=x(z)\frac{N_k(U)}{D_\beta(U)^2},
\qquad N_k\in\mathbf Q(\zeta)[U],\quad\deg N_k=15,
\quad [U^{15}]N_k=1.}
\tag{4}
$$
全部六十四个系数见证书。次数界来自实际极点：分母的零点恰是
两组二挠点减去非零 $\beta$ 挠点，极阶至多二；$i=-1$ 给出
$x$ 乘 $U$ 的有理函数，原点至少二阶零将分子次数压到十五。
所以用十六个准确值恢复 (4) 是在已有全局次数界内的精确运算。
脚本另核一个未参与插值的值。

## 2. 真正共轭 CM17 迹及相邻权 frame

令
$$
S_8=-y\vartheta\sigma^3,\qquad F=S_8^{17},\qquad
\mathcal W=-y\vartheta\sigma^{67},\qquad
D(U)=U^8(U-1)^8.
$$
于是 $F=\mathcal W D$。这里仍保留自然 degree-$68$ 的 $T_0$
二挠线丛；并未把它与旧 $\vartheta(2z)^{17}$ 的线丛混同。

置
$$
\mathcal B_k(z)=F(\beta z)B_k(z)/b_k.
\tag{5}
$$
$F(\beta z)$ 在 (1) 的所有二阶极点处都有至少十七阶零，
故 (5) 是真实全纯 degree-$1156$ 截面，$i$ 特征为 $-1$。
取 R248 同一线丛同构、正有限平坦迹与相位，得到
$$
\mathscr T_{\bar\beta}\mathcal B_k
=\frac{\mathcal W}{x}T_k(U),\qquad\deg T_k\le16.
\tag{6}
$$
这是整个十七点纤维的迹，不是原点分支。

为完全固定计算，沿用 R248 的 $P_\beta,P_{\bar\beta},Q_{\bar\beta},K_{\bar\beta}$，
其中 $S_8(\alpha z)/S_8(z)^{17}=P_\alpha(U)/D(U)$、
$x(\bar\beta z)=x(z)Q_{\bar\beta}(U)^2/K_{\bar\beta}(U)^2$。
准确公式为
$$
\boxed{
T_k(t)=D(t)\operatorname{Tr}_{UQ_{\bar\beta}^4-tK_{\bar\beta}^4=0}
\left[
\left(\frac{P_\beta}{P_{\bar\beta}}\right)^{17}
\frac{UQ_{\bar\beta}^2}{K_{\bar\beta}^2}
\frac{N_k(U)}{D_\beta(U)^2}
\right].}
\tag{7}
$$
中间的 $UQ_{\bar\beta}^2/K_{\bar\beta}^2=x(z)x(\bar\beta z)$
是实际 $\mathcal W/x$ frame 的必要因子。删掉它将得到别的权。
脚本先在 $\mathbf Q(i)$ 上计算十六个单项式的迹矩阵，再作用于
(4)，并在已有十六次界外另核一个值。

## 3. 到原四条八次伴随的准确可逆矩阵

令 $N=\mathscr T_\pi/(2+i)$ 是 R251 在
$(\mathcal W/x)\mathbf Q(i)[U]_{\le16}$ 上的真实 CM5 矩阵。
它满足 $N^{16}=1$。原二处向量 $v$ 在这个全局 $i=-1$ 空间中的
投影准确是
$$
\Pi_v=\frac{1-N^4+N^8-N^{12}}4.
\tag{8}
$$
说明其为同一个实际投影，而非只比较维数。R246 已固定 $v$ 的
二处 $I=1$ 与 CM5 特征；全局 $i=-1$ 因而要求十七处 $\chi(i)=-1$。
在实际 torus 中正是 $N^4=-1$ 的四个八次类型。
其余二处类型对应 $N^4=1,i,-i$，所以 (8) 的像就是原 $v$ 块。
R248/R251 的共同 CM5 标量及 R246 的归一同时固定了角色标签。

对 $j=1,3,5,7$，令
$$
E_j=\frac14\sum_{h=0}^3\zeta^{-jh}N^h\Pi_v,
\qquad H_j^{\rm new}=\frac{\mathcal W}{x}P_j^{\rm new}(U),
\qquad [U^{16}]P_j^{\rm new}=1,
\tag{9}
$$
其中 $H_j^{\rm new}$ 是 $N=\zeta^j$ 的实际特征线。
全部四个十六次多项式在证书中明确给出。

记 $H_j$ 为 R235 的旧伴随
$\vartheta(2z)^{17}x(2z)^{-1}V_j(x(2z)^{-2})$。
R246 的实际 $\mathcal U,\mathcal V$ 满足
$$
\boxed{\mathcal U H_j(2z)=\delta_j H_j^{\rm new}(2z),}
\tag{10}
$$
其中
$$
\begin{array}{c|cccc}
j&1&3&5&7\\\hline
\delta_j&\dfrac{i(70-47\sqrt2)}4&\dfrac{i(16-7\sqrt2)}4&
\dfrac{i(70+47\sqrt2)}4&\dfrac{i(16+7\sqrt2)}4
\end{array}.
$$
四个标量全部非零，乘积为 $19039/64$。

给出原相位的支付。R246 的四个四挠平移仍都带相同的 $i$，
但这里 $i=-1$ 的来源使旋转和保留 $2\bmod4$ 权。
在 $T=(1-i)\Omega_0/4$ 写
$$
x(w-T)=i-2(1-i)w-4w^2+O(w^3),\qquad
g_{17}(w)=\exp\left(17\left(\frac{1+i}2w-\frac i2w^2+O(w^3)\right)\right).
$$
把 $w=4z$、目标 $H_j^{\rm new}(2z)=4z^2+O(z^6)$、
R246 的准确 $\rho$ 都代入，得到
$$
\delta_j=\frac i{16}[w^2]\left(
g_{17}(w)x(w-T)^{-1}V_j(x(w-T)^{-2})\right).
$$
这逐项给出 (10)，没有留下未知的八次根。
证书还独立核对四个像的全部十七个坐标 $z^2,z^6,\ldots,z^{66}$：
四挠端用 $x''=6x^2-2$、$(\log\vartheta)''=1/x$，原点端用
$u=x^{-1/2}$ 的 $u''=-2u^3$。实际基为
$\vartheta^{68}u'u^{66-4j}$，$0\le j\le16$，其首阶两两不同。
全局十七维界因而使这些准确坐标核对证明整个 (10)，不只核其首项。

现在定义四个真实原伴随来源
$$
Z_k=\mathcal V\bigl((\mathscr T_{\bar\beta}\mathcal B_k)(2z)\bigr).
$$
由 (6)–(10)，准确有
$$
\boxed{Z_k=\sum_{j=1,3,5,7}M_{jk}H_j(2z).}
\tag{11}
$$
证书给出 $M$ 的全部十六项。它们全在 $\mathbf Q(i,\sqrt2)$，且
$$
\boxed{
\Re\det M=
-\frac{1688717610759870974566780528313317}
{2871642309825625277511670012261120868352}\ne0.
}
\tag{12}
$$
因此这四个实际 ray 覆盖整个原四维八次伴随。
四个 $T_k$ 在其余十三维部分的余项也全部非零；它们被真正的
$\mathcal V=\mathcal V\Pi_v$ 杀掉，并非计算时把未知余项省去。

## 4. 原 C_A 与带原 CM 补偿的 C_B 全部反解

把 R235 式 (14) 的四个 $a_j,b_j$ 排成列 $\mathbf a,\mathbf b$，定义
$$
\lambda_A=M^{-1}\mathbf a,\qquad\lambda_B=M^{-1}\mathbf b.
\tag{13}
$$
这两个固定代数列的全部八项均由证书给出并直接回乘验证。
记 $\kappa=2^{-1/4}$；对 R235 已付出的准确次数恢复算子
$\operatorname{Reg}:K_j\mapsto\widetilde K_j$，令
$$
\widetilde Y_k=\operatorname{Reg}\bigl(\kappa^{-1}Q_{+,0}Z_k\bigr)
=\sum_jM_{jk}\widetilde K_j(2z).
$$
这里 $\operatorname{Reg}$ 使用 R235 的实际两个 CM 截面及矩阵
$C_{\rm top}^{-1}D_{\rm top}$；不增加任何可自由选择的 CM 系数。
于是
$$
\boxed{C_A(2z)=\sum_k\lambda_{A,k}Z_k,}
$$
$$
\boxed{C_B(2z)=\sum_k\lambda_{B,k}\widetilde Y_k
       +a_{17}L_1(2z)+a_{289}L_2(2z)+a_{4913}L_3(2z).}
\tag{14}
$$
三个 $a$ 和三个 $L$ 是 R235 式 (23)、(27) 的原对象。
(14) 包括恢复原七维空间的全部 CM 补偿。

质量也准确保持：
$$
[z^2]C_A(2z)=-\frac{272}{1155}=-8\beta_A,
\qquad [z^2]C_B(2z)=-\frac{2261}{10240}=-8\beta_B,
\tag{15}
$$
其中 $\beta_A=34/1155,\ \beta_B=2261/81920$。
三个 $L_\ell(2z)/z^2$ 的质量仍为零。

## 5. 两条原中央行及全部 u−1、u−2 项

固定惰性 $p>19$，排除本篇有限个固定代数分母及行列式的坏素位。
置 $d=p+1,c=272c_0,q_2=2^{p-1}$，并写
$$
\Theta_2=\vartheta(4z)^{17},\quad
\nabla_0=\partial_z-\Theta_2'/\Theta_2,\quad
W=z\Theta_2'/\Theta_2,\quad W_0=W-dcz^d.
$$
对 (14) 的任一伴随 $U\in z^2[[z^4]]$，令
$$
f_U(u)=J_c(U/z^2;u),\quad
g_U(u)=J_c(W_0U/z^2;u),\quad
h_U(u)=J_c((W_0^2+EW_0-W_0)U/z^2;u),\quad E=z\partial_z.
$$
完整二阶行是
$$
\begin{aligned}
\mathfrak M_2(U;u)={}&(du+1)(du+2)f_U(u)
 +du(d-3-2du)f_U(u-1)\\
&+d^2u(u-1)f_U(u-2)-2(du+1)g_U(u)
 +2dug_U(u-1)+h_U(u)\\
={}&J_c(\nabla_0^2U;u).
\end{aligned}
\tag{16}
$$
沿用 R229 的 $A=A_{17}(2z)/16,B=A_{34}(z)$ 及 $\rho=F_0/T$，
两条原行于是准确为
$$
\boxed{
q_2^uJ_{68c_0}(A;u)=\beta_AJ_c(\Theta_2;u)
 +\frac1{16}\sum_k\lambda_{A,k}\mathfrak M_2(Z_k;u),}
$$
$$
\boxed{\begin{aligned}
q_2^uJ_{68c_0}(B;u)={}&\beta_BJ_c((\Theta\rho)(2z);u)\\
&+\frac1{16}\left(
\sum_k\lambda_{B,k}\mathfrak M_2(\widetilde Y_k;u)
 +\sum_{\ell=1}^3a_\ell\mathfrak M_2(L_\ell(2z);u)\right).
\end{aligned}}
\tag{17}
$$
系数 $1/16$ 来自原 $1/4$ 及 $z\mapsto2z$ 的二阶链式因子。
式 (15) 使 (16) 的 $2f_U(0)$ 准确抵消 (17) 的参考质量。
固定单位 $q_2^u$ 保留在全 $u$ 恒等式中。

## 6. 真正 primitive 的全四阶转置

本节不把有限投影与中央泛函交换。它逐个转置实际有限分支。
在共同 degree-$4624$ 源上置
$$
f(z)=F(2\beta z),\qquad
\mathcal H_k(z)=f(z)\Phi_k(2z)/b_k,\qquad
\nabla_f=\partial_z-f'/f.
$$
准确有
$$
\mathcal B_k(2z)=-\frac1{32}\nabla_f^2\mathcal H_k.
\tag{18}
$$
令 $\mathcal L=\mathcal V[\bar\beta]_*$，所有线丛同构和全体
纤维均取前节原规范，因此 $Z_k=\mathcal L\mathcal B_k(2z)$。
把它写成实际分支和
$$
\mathcal L=\sum_\nu c_\nu T_\nu,
\qquad T_\nu:\ z\longmapsto z/\bar\beta+s_\nu.
$$
$T_\nu$ 包括其原 Mumford 乘子，$c_\nu$ 是固定代数数。
所有分支的斜率相同，均为 $1/\bar\beta$。定义
$$
a_\nu=\partial_z\log\frac{T_\nu f}{\Theta_2}.
$$
链式法则给出完整恒等式
$$
T_\nu\nabla_f^2\mathcal H_k
=\bar\beta^2\left[
\nabla_0^2-2a_\nu\nabla_0+(a_\nu^2-a_\nu')
\right]T_\nu\mathcal H_k.
\tag{19}
$$
设置
$$
S_{0,k}=\sum c_\nu T_\nu\mathcal H_k,\quad
S_{1,k}=\sum c_\nu a_\nu T_\nu\mathcal H_k,\quad
S_{2,k}=\sum c_\nu(a_\nu^2+a_\nu')T_\nu\mathcal H_k.
$$
将 (19) 中的乘法项移到导数内，得到
$$
\boxed{
\nabla_0^2Z_k=-\frac{\bar\beta^2}{32}
\left(\nabla_0^4S_{0,k}-2\nabla_0^3S_{1,k}
                         +\nabla_0^2S_{2,k}\right).}
\tag{20}
$$
三类和分别有全局 $i$ 特征 $1,-i,-1$。
因此，令 $m_k=S_{0,k}(0)$ 后，
$$
G_{4,k}=\frac{S_{0,k}-m_k\Theta_2}{z^4},\qquad
G_{3,k}=\frac{S_{1,k}}{z^3},\qquad
G_{2,k}=\frac{S_{2,k}}{z^2}
\tag{21}
$$
均在原形式盘正则。减去 $m_k\Theta_2$ 是准确的水平项扣除，
因为 $\nabla_0\Theta_2=0$；$m_k$ 不被预设为零。

下面的有限递推明确保留最高到 $u-4$ 的全部项。
定义
$$
\mathfrak D_p H(u)=du\bigl(H(u)-H(u-1)\bigr),
$$
以及 $P_{0,0}=1$、越界下标为零，
$$
P_{n+1,h}=P_{n,h-1}+(n+1-W_0)P_{n,h}-E P_{n,h}.
\tag{22}
$$
这些是 $W_0,EW_0,\ldots$ 的固定微分多项式。对 $0\le n\le4$ 令
$$
\mathcal M_n(g;u)=\sum_{h=0}^n\mathfrak D_p^h
J_c(P_{n,h}g;u).
\tag{23}
$$
则准确有
$$
\mathcal M_n(g;u)=J_c(\nabla_0^n(z^ng);u).
$$
证明是先将
$e^{-cz^d}\nabla_0^n(z^ng)=\prod_{j=1}^n(E+j-W_0)(e^{-cz^d}g)$
左正规排序；其准确形式为 $\sum_hE^h\circ M_{P_{n,h}}$，
即先乘 $P_{n,h}$，再作用左侧的 $E^h$。
完整 Newton 求和将 $E$ 变成 $\mathfrak D_p$，而不是单独的 $du$。
例如 $P_{2,0}=W_0^2-3W_0+EW_0+2$、
$P_{2,1}=3-2W_0$，展开 (23) 即 (16)。
证书同时列出 $n=0,1,2,3,4$ 的全部多项式。

由 (20) 得到所需全四阶中央行
$$
\boxed{
\mathfrak M_2(Z_k;u)=-\frac{\bar\beta^2}{32}
\left(\mathcal M_4(G_{4,k};u)-2\mathcal M_3(G_{3,k};u)
                              +\mathcal M_2(G_{2,k};u)\right).}
\tag{24}
$$
把 (24) 代入 (17) 首行，外系数为 $-\bar\beta^2/512$。
对原 $B$ 的未补偿八次部分，同一计算应用于
$\kappa^{-1}Q_{+,0}\mathcal L$；其分支斜率仍为 $1/\bar\beta$。
随后必须加回 (14)、(17) 中准确的原 CM 与三个四次补偿行。
这给出两条原行的完整 primitive 表达，不从四次微分中删掉任何
$a_\nu'$、$W_0$、质量或负移权。

若把单个分支的缩放移出 $J$，还须保留
$$
U_{\bar\beta,p}^{-u},\qquad U_{\bar\beta,p}=\bar\beta^{p+1}/17.
\tag{25}
$$
具体地，把 $T_\nu$ 写为固定平移及原乘子后再作 $z\mapsto z/\bar\beta$，
R54 的缩放把 $J_{272c_0}$ 变成
$U_{\bar\beta,p}^{-u}J_{4624c_0}$。
(19)–(24) 在目标 gauge 中保留整个分支，所以该因子已在原 germ 内；
它不能在改换 gauge 时置为一。

## 7. norm-two 非零常数的准确水平核

在 $f$ 乘原 log germs 的模块上定义保 frame 的实际平移
$$
\tau_f(fh)(z)=f(z)h(z+T_0/2),\qquad T_0=(1+i)\Omega_0/2.
$$
它等于真实 $T_0/2$ Mumford 平移再乘固定 meromorphic frame 比值；
这里只在上述模块上使用，未声称它保持任意全纯截面格。
R253 的原 norm-two 式准确变成
$$
\boxed{
\tau_f\mathcal H_k=-\mathcal H_k-2(C_k/b_k)f,
\qquad \frac{1+\tau_f}{2}\mathcal H_k=-(C_k/b_k)f\ne0.}
\tag{26}
$$
未中心化 primitive $f\Psi_k(2z)/b_k$ 则是 $\tau_f=-1$ 类型。
其质量为 $C_k/b_k$；中心化和取该负类型不是同一个归一。

但是 $\nabla_f^2 f=0$。因此 (18) 的真实代数来源满足负类型，
而 (26) 的全部非零常数都在这个二阶算子的水平核中。
转置后也不能把它们重新当作剩余常数。事实上，对输入 $cf$，
$$
\nabla_0(T_\nu f)=a_\nu T_\nu f,
\qquad S_1=\nabla_0S_0,\qquad S_2=\nabla_0^2S_0.
$$
于是 (20) 的三个项准确合成
$$
\nabla_0^4S_0-2\nabla_0^3S_1+\nabla_0^2S_2=0.
\tag{27}
$$
(27) 是包含全部连接、全部移权和全部质量后的抵消。
R253 的六维对数独立性不改变这个核。

另一方面，非恒定 primitive 并未因此消失。在共轭迹以前，
$\log r(z+aP)$ 的除子是
$2(T_+-aP)-2(T_--aP)$。共轭迹后的奇点为
$$
\bar\beta(T_\pm-aP)=T_\mp-8aP,
\tag{28}
$$
因为 $\bar\beta\equiv i\bmod2$ 且 $\bar\beta\equiv8=3^{10}\bmod\beta$。
三十二个点互异。每处只有一个 trace 分支带相应对数；其 monodromy
为 $\pm4\pi i\chi_k(a)^{-1}/b_k$ 乘一个非零 theta 分支 germ。
该 germ 虽有十七阶零，仍不为零。角色独立性因此证明：在加二处投影
以前，四个未微分 trace primitives 的非恒定 log 无固定代数线性组合
可以消去。这里不从这一点擅自推出投影后的中央非零。

## 8. 原解析盘、混合挠点常数及下一条实质约束

所有算子都固定于目标素数 $p$ 之前。除有限坏素位后，涉及的
代数数、矩阵逆及 torsion 参数均在固定整格中。
尤其 $\mathcal V$ 的每个二处平移坐标都是 odd/odd；在原自然变量中
其二主部分是 exact-order-eight。经 $\bar\beta$ 逆像仍保持此性质，
所以不会碰到 $\Phi_k$ 的二挠零极点。
因此 (19)–(21) 的每个实际 primitive germ 在原点存在。

单个分支不再有 R253 原未平移角色和的 $R^4$ 界。
在 $R=p^{-1/(2p)}$ 上，使用原形式参数积分的准确通用估计
$\sup_{n\ge1}p^{v_p(n)}R^n=p^{1/2}$，再乘固定次连接和除去固定
原点零阶，即得到 $p^{1/2}R^{-C}$ 型界，$C$ 与 $p$ 无关。
R54 的共同 theta gauge 于是使 Newton 尾项估值至少为
$$
\frac{h(p-1)}{2p}-\frac12-\frac{C}{2p}\longrightarrow+\infty.
$$
故本篇全部 $J$、移位和中央导数均在同一原盘上收敛。

各 $m_k$ 及平移分支常数必须原样保留：它们一般涉及
八挠点加 $\ker\beta$、$\ker\bar\beta$ 点上的 $r$ 值。
没有已付分布就不能把这些混合挠点对数归到纯二次幂挠点的两个单位中。

现在已得到一个具体完整接口：两条原中央行来自四个真实 log primitives
的 (24)，而 norm-two 的四个已知非零常数由 (26) 进入其水平扩张。
要用这些常数迫原中央非零，仍须证明额外的真实 primitive 兼容关系，
使原中央零约束到 (26) 的正投影；仅对已微分的 (11) 作可逆换基无法做到。
本篇不把该未付关系登记为完成。

## 精确证书

- [脚本](../scripts/check-octic-ray-original-companion-transport.py)
  与 [完整输出](../scripts/check-octic-ray-original-companion-transport.json)
  含原加法式、四个首项的逆证书、四个 $N_k$、整个共轭迹矩阵、四个
  相邻特征多项式、实际 $4\times4$ 矩阵及行列式、两条原伴随的反解，
  以及全四阶左正规连接多项式。
- 原四八次来源与唯一 CM 补偿：R235；原双向 dyadic 相位：R246；
  原共轭 CM17 及 trace 模型：R248；相邻 CM5 规范：R251；
  原四个八次对数常数、norm-two 分布及原盘：R253。
- 所有有限运算在固定数域中准确进行，没有扫描目标素数，也没有用
  数值拟合或有限中央非零样本替代恒等式。
