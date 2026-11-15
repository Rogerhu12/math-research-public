# R373：完整 W 平方角商与五形状十一行有限频率支付

日期：2026-11-15。**完整有限纸面证明；未运行求积、符号程序、参数扫描、人工测试或研究计算。**

当前同一个全偶真实弱圆已经支付全部18面积、R364 的局部条件 $\mathcal T=0$、完整 $P^2,PW,PZ,PY,ZW$，并由 R372 新增完整 $ZZ_0$。本稿比较原 cubic 后，先完成能够准确闭合的整个 $W^2$ 乘积。$ZZ_2$ 不作自动推断，仍保留未付。

$WW_0$ 和 $WW_2$ 的完整角商都能由既有面积及 R372 的真实 self 关系消去；这一步包含原 primitive，并非只处理主项。剩余两个实际 $\pi/2$ 值，与旧九行组成十一维真实正锥。新增第五种振荡形状由五个明确的有限二阶 jet 数据构造，与同一个 $\mathcal F_{\rm new}$ 最大 minor 从起点相容。最终用60个实际正幅列和一个有限频率精确根，同点保持所有旧门并支付完整 $W^2$。

来源：
[R259](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md)、
[R267](R267-amplitude-width-shapes-pay-the-complete-minus-one-minus-three-area.md)、
[R285](R285-principal-splitting-of-symmetric-Gaussian-products.md)、
[R293](R293-finite-frequency-zero-of-all-necessary-symmetric-Gaussian-observations.md)、
[R294](R294-corrected-self-fibers-pay-all-angular-symmetric-Gaussian-histories.md)、
[R354](R354-complete-reflection-and-positive-omega-bridges-pay-three-remaining-Gaussian-moments.md)、
[R361](R361-even-weak-circles-and-three-oscillation-shapes-pay-the-negative-three-square.md)、
[R364](R364-local-angular-quotient-and-five-target-control-pay-the-negative-three-minus-one-product.md)、
[R368](R368-two-exact-cubic-identities-and-seven-target-control-pay-the-PY-product.md)、
[R369](R369-vanishing-first-cubic-and-eight-target-control-pay-the-ZW-product.md)、
[R372](R372-complete-ZZ-zero-angular-quotient-and-nine-target-finite-frequency-control.md)。

## 1. 当前同一个对象与原记号

保持
$$
P=\Phi_{r_0},\quad R=\Phi_{r_1},\quad S=\Phi_{s_0},
\quad L=\Phi_{p_0},\quad U=\Phi_{s_1},\quad Y=\Phi_{p_2},
$$
$$
W=aR+bS,\qquad Z=dL+eU.
$$
仍固定 $\zeta=\kappa^2\in(0,1/100)$、$\kappa>0$，以及
$$
a=-\frac{51\zeta^2+2\zeta+8}{64h_e^2},\quad
b=-\frac{34\zeta^2+8\zeta}{64h_e^2},\quad
d=\frac{6\kappa\zeta}{h_e},\quad
e=-\frac{\kappa(15\zeta+1)}{4h_e}.
\tag{1}
$$
本稿用 $h_W=a+b$，它不是几何高度函数。

对当前全偶实紧 $f,g$，
$$
\phi=f\cos\theta+g\sin\theta,\qquad
D=f\odot f-\phi\odot\phi.
$$
原三矩圆使 $PD,WD,ZD,YD$ 真紧。
弱单 hook、非零 derivative rank-two 核及完整第二／第三 range 均按原构造保留。
没有补加第二 hook，也不把弱核套成 rank-one 微包。

normalized 平方外矩为
$$
\mathcal Q_{WW,j}
=-I_j(WD,WD)+2I_j\{\phi,W(\phi,WD)\}.
\tag{2}
$$
原 $I_2$ 始终是 $\int(x^2u''v''+2u'v')$。
由现有十二完整副本，angular odd 项已经清除；由全偶反射，$\mathcal Q_{WW,1}=0$。
本稿必须处理的是第0、2矩的两个完整角函数。

## 2. 原 W 的两个完整 cubic 密度

对任意紧 $u$，记
$$
v=u',\qquad r=u'',\qquad t=r',\qquad
P_u=J(r^2),\quad S_u=J(xr^2).
$$
原输出及导数为
$$
R(u,u)=v^2+xP_u,\quad
R'=2vr+P_u-xr^2,\quad R''=2(v-xr)t,
$$
$$
S(u,u)=S_u,\quad S'=-xr^2,\quad S''=-r^2-2xrt.
\tag{3}
$$
单个输出一般有真实左尾，不假设它紧。

原第零 cubic 为
$$
\boxed{
F_{W,0}(u)=I_0(u,Wu^2)
=-\frac{h_W}{3}\int r^3.
}
\tag{4}
$$
完整第2 cubic 由(3)代入 $I_2$ 的两项，准确得到
$$
F_{R,2}=2\int ur^2-4\int xvr^2+\int x^2r^3,
$$
$$
F_{S,2}=-2\int xvr^2+\int x^2r^3.
$$
例如 $R$ 项中的真实 primitive 是 $2\int vP_u=2\int ur^2$；
它只用紧 outer $u$ 的端值，不删 $P_u$ 的左常数。
含 $r'$ 的项分别用 $(r^2)'$ 和 $(r^3)'$ 积分；
$\int v^2r=0$ 是紧 $v$ 的总导数。
所以
$$
\boxed{
F_{W,2}
=2a\int ur^2-(4a+2b)\int xvr^2
+h_W\int x^2r^3.
}
\tag{5}
$$
(4)—(5)对任意紧实输入成立，其复多项式延拓使用同一个右锚。

## 3. 第零 self：已付面积准确杀完整角商

取当前合法复输入
$$
q=f+ig,\qquad I_j(q,q)=0\quad(j=0,1,2),
$$
写 $v=q',r=q'',t=r'$。
此时 $w=W(q,q)$ 真紧，故合法 cubic 变分给
$$
K_{WW,j}(q)
=I_j(Wq^2,Wq^2)+2I_j\{q,W(q,Wq^2)\}
=DF_{W,j}(q)[Wq^2].
\tag{6}
$$
不对一般 nonlegal 单包使用这个紧方向等式。

原
$$
w''=2avt-2h_Wxrt-br^2
$$
与(4)给
$$
K_{WW,0}=-h_W\int r^2w''.
$$
紧 IBP
$$
\int vr^2t=-\frac13\int r^4,\qquad
\int xr^3t=-\frac14\int r^4
$$
遂给
$$
\boxed{
K_{WW,0}
=\frac{h_W(a+3b)}6\,C_0,\qquad C_0=\int r^4.
}
\tag{7}
$$

原 R267 的真实 self 身份是
$$
S_{P,L,0}(q)=\frac{C_0}{6},\qquad
S_{P,U,0}(q)=\frac{7C_0}{6},
$$
其中 $S_{X,Y,j}=2I_j\{q,[X,Y](q;q^2)\}$。
当前全相位 $PZ_0$ 面积已零，四次相位系数迫
$$
\frac{d+7e}{6}C_0=0.
$$
$d+7e\ne0$，故 $C_0=0$，从而
$$
\boxed{\operatorname{Re}K_{WW,0}(q)=0.}
\tag{8}
$$
这是原完整角商为零，不是仅令它的 $C^3$ 主部为零。

## 4. 第2 self：全部 primitive 和端项保留

仍对整个合法 $q$ 计算，记
$$
C_2=\int x^2r^4,\quad N=\int xvr^3,\quad
V_2=\int v^2r^2,\quad U_3=\int qr^3,\quad
A_2=\int[J(r^2)]^2,
$$
并令 $k_W=4a+2b$。
由(5)，
$$
DF_{W,2}[w]
=\int\{2ar^2w-k_Wxr^2w'
+(4aqr-2k_Wxvr+3h_Wx^2r^2)w''\}.
\tag{9}
$$
原真实输出为
$$
w=a(v^2+xP_q)+bS_q,\quad
w'=2avr+aP_q-h_Wxr^2,\quad
w''=2avt-2h_Wxrt-br^2.
\tag{10}
$$

(9)—(10)中的全部 primitive 正好是
$$
-2ah_W\int xP_qr^2+2ab\int S_qr^2.
$$
整个复矩零给 $P_q,S_q$ 左右两侧真零，故先保边项再用
$$
\int xP_qr^2=\frac{A_2}{2},\qquad
\int S_qr^2=-\frac{A_2}{2},
$$
得到
$$
-a(a+2b)A_2.
\tag{11}
$$
这一步没有对单个 nonlegal 微包分别删尾。

含 $t$ 的全部项为
$$
8a^2qvrt-8ah_Wxqr^2t-4ak_Wxv^2rt
+h_W(4k_W+6a)x^2vr^2t-6h_W^2x^3r^3t.
$$
分别用 R372(14)的五个紧 IBP：
$$
\int qvrt=-\frac{V_2+U_3}{2},\quad
\int xqr^2t=-\frac{U_3+N}{3},\quad
\int xv^2rt=-\frac{V_2}{2}-N,
$$
$$
\int x^2vr^2t=-\frac{2N+C_2}{3},\qquad
\int x^3r^3t=-\frac34C_2.
$$
连同(9)的全部低项及(11)，完整合并为
$$
\boxed{
\begin{aligned}
K_{WW,2}
={}&\frac{h_W(7a+5b)}6C_2
-\frac{4h_W(3a+b)}3N
+2a(3a+2b)V_2\\
&-\frac{4ah_W}{3}U_3-a(a+2b)A_2.
\end{aligned}}
\tag{12}
$$
这保留了真实 $A_2$，不是一个 mod-$C^2$ 的式子。

R372 已由三个完整面积和 R364 的 $\mathcal T=0$ 证明
$$
(\operatorname{Re}C_2,\operatorname{Re}N,
\operatorname{Re}V_2,\operatorname{Re}U_3,\operatorname{Re}A_2)
=\frac{\operatorname{Re}N}{5}(8,5,2,4,-4).
\tag{13}
$$
代(12)，前两项与 $U_3$ 项合为 $-16ah_W\operatorname{Re}N/5$，
$V_2,A_2$ 两项合为其相反数。
所以
$$
\boxed{\operatorname{Re}K_{WW,2}(q)=0.}
\tag{14}
$$
本稿没有新增未经证明的 $C^2$ 纤维条件；
(8)、(14)由原式和当前确实保持的面积／$\mathcal T$ 得到。

## 5. 整个 W 平方只余两个实际值

R294 的准确角分解、原 odd 副本及(8)、(14)给
$$
\boxed{
\mathcal Q_{WW,j}(\theta)
=\sin^2\theta\,\mathcal Q_{WW,j}(\pi/2),
\qquad j=0,2.
}
\tag{15}
$$
第1矩已由全偶反射为零。
因此需将(15)的两个实际值与原九行同时支付；
不能沿一个已经冻结的九行根任意改变 profile。

## 6. 完整主项与新常数方向

只在末端强 rank-one 微包中扰动，写
$$
f_i=a_i u_i,\quad g_i=b_i u_i,\quad
\lambda_i=-a_i^2(a_i^2-b_i^2),\quad
v=u_i',\ r=u_i'',\ t=u_i'''.
$$
原
$$
\alpha_W=2av-2h_Wxr
$$
给
$$
\mathcal Q_{WW,j}(\pi/2)
\equiv_2
\sum_i\lambda_i\int x^j\alpha_W^2t^2,\qquad j=0,2.
\tag{16}
$$
所有实际 Green、右历史、内部尾和连续 $C^2$ 余项都留在 $\equiv_2$ 中，最后共同评价。

原四行可逆换成
$$
H_0=\int r^2t^2,\quad H_a=\int x^2r^2t^2,\quad
H_b=\int xvrt^2,\quad H_d=\int urt^2.
$$
由(16)，新增 $WW_0$ 与旧行的固定组合，principal 正好给
$$
\frac{\mathcal Q_{WW,0}+8ah_WH_b-4h_W^2H_a}{4a^2}
\equiv_2\int v^2t^2.
\tag{17}
$$
这里(17)只记 principal 行变换；原目标仍是完整真实函数。

为处理 $WW_2$，沿用 R369/R372 的三个变换：
$$
\mathcal R_P=\mathcal Q_{PZ,2}+6e\mathcal Q_{PY,0},
$$
$$
\mathcal R_Z=\mathcal Q_{ZW,1}-h_W\mathcal Q_{PZ,2},
$$
$$
\widehat{\mathcal R}_Q
=\mathcal Q_{ZZ,0}+9e^2\mathcal Q_{PY,0}
-\frac{3e(d+3e)}{d+6e}\mathcal R_P
-\frac{2e-d}{2a}\mathcal R_Z.
\tag{18}
$$
对偶母与偶 $\chi$，其二次位置系数分别为
$$
T_\chi=-2(d+6e)U_\chi+6(d+4e)V_\chi,\quad
S_\chi=2a\{(2e-d)V_\chi^{(2)}-9eV_\chi\},
$$
$$
\gamma_\kappa V_\chi,\qquad
\gamma_\kappa=-\frac{9ed(d+4e)}{d+6e}\ne0,
\tag{19}
$$
其中
$$
R_\chi=\int r^2\chi^2,\quad
V_\chi=\int yvr\chi^2,\quad
U_\chi=\int ur\chi^2,\quad V_\chi^{(2)}=\int v^2\chi^2.
$$
全部实际 copy 正权与偏移仍按 R372 保留。

把 $WW_2$ 加 $4h_W^2\mathcal Q_{PY,0}$，四次位置主项相消，余密度为
$$
-8h_W^2x^2ur+4a^2x^2v^2+8h_Wb\,x^3vr.
\tag{20}
$$
其二次位置系数是
$-8h_W^2U_\chi+4a^2V_\chi^{(2)}+24h_WbV_\chi$。
再减
$$
\frac{4h_W^2}{d+6e}\mathcal R_P
+\frac{2a}{2e-d}\mathcal R_Z
$$
的二次系数，余下 $\eta_\kappa V_\chi$，其中
$$
\eta_\kappa=
\frac{24h_W\{2be-a(d+4e)\}}{d+6e}
+\frac{36a^2e}{2e-d}.
\tag{21}
$$
定义完整行变换
$$
\begin{aligned}
\mathcal N_W={}&
\mathcal Q_{WW,2}+4h_W^2\mathcal Q_{PY,0}
-\frac{4h_W^2}{d+6e}\mathcal R_P
-\frac{2a}{2e-d}\mathcal R_Z\\
&-\frac{\eta_\kappa}{\gamma_\kappa}\widehat{\mathcal R}_Q.
\end{aligned}
\tag{22}
$$
对任意偶母与偶 $\chi$，其 principal 位置多项式只剩常数。
其中 $u^2t^2$ 的系数准确为
$$
\boxed{-\frac{\eta_\kappa d^2}{\gamma_\kappa}.}
\tag{23}
$$
因为(22)中只有 $\widehat{\mathcal R}_Q$ 含 $d^2u^2t^2$；
其他项均没有 $u^2$。所有其余常数项仍保留，不能从(23)只取一个候选项宣秩。

## 7. 新系数在全部原小参数范围非零

令
$$
r_\kappa=\frac de,\qquad \beta_\kappa=\frac ba.
$$
由(1)，
$$
-\frac6{25}<r_\kappa<0,\qquad 0<\beta_\kappa<\frac{11}{1000}.
$$
直接通分(21)给
$$
\frac{\eta_\kappa}{12a^2}
=
\frac{
2(1+\beta_\kappa)(2\beta_\kappa-r_\kappa-4)(2-r_\kappa)
+3(r_\kappa+6)
}{(r_\kappa+6)(2-r_\kappa)}.
\tag{24}
$$
分母为正。分子在 $\beta_\kappa=0$ 时是
$2r_\kappa^2+7r_\kappa+2\ge272/625$。
其余部分为
$$
2\beta_\kappa(2-r_\kappa)
(2\beta_\kappa-r_\kappa-2)
\ge-\frac{308}{3125}.
$$
故完整分子至少为 $1052/3125>0$，从而
$$
\boxed{\eta_\kappa>0.}
\tag{25}
$$
(23)因此在原全部小共振范围非零，不需要选一个未经验证的数值参数或扫描例外根。

## 8. 五个有限 jet 点值给真实第五形状

下面构造同一个正偶母，不能把五个母积分当独立坐标。

先把(22)的 principal 密度在 $X=0$ 写为
$\mathfrak n(y,u,v,r)t^2$。
它是完整已列行的固定线性组合。对 $r\ne0$，置
$$
A(y)=\frac{yv}{r},\quad B(y)=\frac ur,\quad
C(y)=\frac{v^2}{r^2},\quad
E(y)=\frac{\mathfrak n(y,u,v,r)}{r^2}.
$$
(23)保证 $E$ 的 $B^2$ 系数为一个固定非零常数
$$
c_*=-\eta_\kappa d^2/\gamma_\kappa.
\tag{26}
$$
其余项至多对 $B$ 一次。系数为 $y$、$v/r$ 的真实多项式，未删除。

取五个正点
$$
y_1=\frac1{20},\quad y_2=\frac1{10},\quad
y_3=\frac3{20},\quad y_4=\frac14,\quad y_5=\frac13.
$$
在前三点指定
$$
r=1,\quad v=0,\quad u=L,\ 2L,\ 3L,
$$
在后两点指定
$$
r=1,\quad v=1,\ 2,\quad u=L.
\tag{27}
$$
$L>0$ 是随后取足够大但有限的常数。

前三行的 $A=C=0$，其 $(1,B,E)$ 子式为
$$
2c_*L^3+O(L^2),
$$
所以有限 $L$ 足够大时非零。
后两行在 $(A,C)$ 上的 determinant 是
$$
\det\begin{pmatrix}y_4&1\\2y_5&4\end{pmatrix}
=4y_4-2y_5=\frac13\ne0.
$$
因此五个完整点值向量 $(1,A,B,C,E)$ 满秩5。

这些有限 jets 可由一个真实正偶紧母实现。
令 $\psi=\exp[-1/(1-y^2)]$ 于 $|y|<1$，外延拓零。
在 $\pm y_i$ 以对应奇偶指定
$$
H=\log(u/\psi),\quad
H'=v/u-(\log\psi)',\quad
H''=r/u-(v/u)^2-(\log\psi)''.
$$
有限 Hermite 插值并取偶部，给一个真实偶多项式 $H$，
使 $\psi\exp H$ 实现(27)且正 prefactor 严格为正。
可额外指定 $u(0)=u''(0)=1$，不影响上述有限点值。

再以偶多项式在闭支撑上连同有限导数逼近 $\exp H$。
选一个实际有限次数，保正 prefactor 与严格点值 minor。
于是得到同一类 $u^\dagger=\psi P^\dagger$ 的正见证。
最后取五个分别集中于 $\pm y_i$ 的真实偶 cutoff，
再用 $\psi$ 偶多项式逼近。足够窄但有限的支撑保五积分列
$$
\left(
\int r^2\chi_\alpha^2,\ 
\int yvr\chi_\alpha^2,\ 
\int ur\chi_\alpha^2,\ 
\int v^2\chi_\alpha^2,\ 
\int\mathfrak n\chi_\alpha^2
\right)
\tag{28}
$$
满秩5。

整个过程是有限 jet 插值与严格开性，没有用点质量作为最终形状。
第五列包含(22)的全部常数密度，不是只用 $u^2$ 的孤立候选项。

## 9. 同母最大 minor、真实 copy 与十一维秩

从起点继续使用 R364 的同一有限映射
$$
\mathcal F_{\rm new}
=(\mathcal F_\star,\
\text{全部 }\mathfrak j,\mathfrak k
\text{ 的真实平移系数}).
\tag{29}
$$
不增加一个尚未证明可保持的角条件。

$\psi$ 偶多项式在共同偶 $C^2$ 域稠密，
可选一个真实最大秩母及固定同类纠正方向。
将它与§8的正见证用同类多项式直线连接。
固定最大 minor 沿直线是非恒零多项式；
在正见证附近避开其有限零点，即可同时保持最大 minor、
正 prefactor 和(28)的严格 rank5。
然后固定五个实际 $\chi_\alpha$。
这是同一母上的真正选择，不假任意母 regular。

对全部原实际 copy 偏移 $d_\nu$、正权 $\omega_\nu$，
取物理 $x=X+d_\nu+y$。
本稿所有 principal 行均为 $X$ 的次数至多6多项式。
(22)的二次系数对所有偶母、所有偶 $\chi$ 准确为零，
其未平移多项式又是偶多项式，故只余常数；
每次真实 copy 只乘同一个正权和，不引入被遗漏的偏移项。

原九行的位置秩为两个高次方向、四个二次方向和三个常数方向。
(17)新增常数 $\int v^2\chi^2$；
(22)、(28)再新增完整常数 $\int\mathfrak n\chi^2$。
五列(28)满秩，同时也保证其前四列满秩。
所以新十一行的联合实际主空间准确为
$$
\boxed{1+1+4+5=11.}
\tag{30}
$$

每个 $\chi_\alpha$ 使用一个原实际层的十二个交替索引
$$
0,1,33,34,49,50,65,66,81,82,97,98.
$$
五组层互异，所有同名八／十二副本和空间镜像共享参数。
每组真实 $\beta_i/\lambda_i>0$ 的十二点 kernel 消去次数至多十的多项式；
本稿仍只用到次数至多6。
由(30)，60列联合 span 为 $\mathbb R^{11}$，
每组又有严格正 kernel，故
$$
\boxed{
\operatorname{cone}_+(\text{60个真实十一行列})=\mathbb R^{11},
\qquad\ker\cap\mathbb R^{60}_{>0}\ne\varnothing.
}
\tag{31}
$$

## 10. 一个有限频率根共同支付全部旧门和完整 W 平方

从原负 $\Psi$、全部18面积及 $\mathcal T=0$ 已付的实际入口开始，
固定弱 rank-two 核和此前全部宏块，不在其上套微包公式。
先按§9选择最后强控制器的真实母、五个 $\chi$、全部 copy 与最后位置，
再以静态正幅支付 $\Psi$。

各实际微包采用
$$
u_{N,z}=u_0+N^{-3}z\chi_\alpha\cos Ny
+\sum_\ell a_\ell(N,z)e_\ell,\qquad
\mathcal F_{\rm new}(u_{N,z})=\mathcal F_{\rm new}(u_0).
\tag{32}
$$
最大 minor／局部常秩保持整个(29)。
纠正与参数一导在 $C^2$ 为 $O(N^{-1})$，
固定光滑纠正方向的三导贡献同阶。
有限正幅盒先固定，随后选同一个有限整数 $N$。

完整十一量为原 R372 九行，再添
$\mathcal Q_{WW,0}(\pi/2),\mathcal Q_{WW,2}(\pi/2)$。
R285 原主分裂给一致的
$$
\mathbf G_N(\mathbf z)
=\mathbf G_{\rm base}+\sum_i z_i^2v_i+o_{C^1}(1).
\tag{33}
$$
基线保完整弱核、宽 cutoff、补矩、全部旧面积模块、
真实 Green／右历史／内部非紧尾、实际 copy 权和最终中心。
不同完整 block 按各自真三矩零与原支持论证相加；
不对单微包假定三矩合法。

由(31)，极限目标存在全部严格正的平方幅解。
选十一独立列，固定其他正幅，Jacobian $2z_iv_i$ 可逆。
非退化零在小 $C^1$ 扰动下稳定，因此某个实际有限 $N$ 给
$$
\boxed{\mathbf G_N=0.}
\tag{34}
$$
这同时恢复原九行，未在旧根后单独扰动新两值。

(32)保持全部18面积、R364 的 $\mathcal T$、末强块原72面积数据与 quartic $C$，
故 $\Psi$、三条 directed 行、指定一层和完整第三保持。
原五个完整乘积及 R372 的 $ZZ_0$ 由旧九行与其原角身份保持。
(8)、(14)、(15)把新两行准确提升为
$$
\boxed{
\mathcal Q_{WW,j}(\theta)=0,\qquad j=0,1,2,\quad\text{全部相位}.
}
\tag{35}
$$
空间镜像仍共享参数，故第1矩的反射零在同一个最终圆上成立。

同一证明可任意指定两个新有限实数 $(\tau_0,\tau_2)$，旧九行为零；
对应完整角函数为 $\tau_j\sin^2\theta$。
这给真实联合控制，不把新零说成旧九行的自动推论。

## 11. 有限选择顺序与未付范围

本稿保持原有限构造顺序：
先定弱核、面积／角商模块和负 $\Psi$ 储备；
从起点定(29)及同母最大 minor、§8五个实际形状；
再定全部真实 copy、最后中心与静态正幅；
最后定有限正幅盒、有限 $N$ 和完整十一行根。
根后不再平移、更换锚或拆开共享副本。

全部 profiles 与正负支撑确定后，按 R354 选择新共同物理区间、
足够大的 $\omega$ 下界和初始小 $h_e$，真实安装闭 hook 与共振保护芽。
新增行的共同非零 $h_e$ 归一化与(25)不改变零目标。
不继承另一条几何的 wholeE、Morse 或全 period。

当前完整支付的对称乘积为
$$
P^2,\quad PW,\quad PZ,\quad PY,\quad ZW,\quad W^2,
$$
另有 $ZZ_0=0$ 和反射自动的 $ZZ_1=0$。
剩余反射允许的位置是
$$
ZZ:2;\qquad ZY:0,2;\qquad WY:1;\qquad YY:0,2.
$$
共6个完整角函数位置，不是独立 rank。
尤其 $ZZ_2$ 的完整同权 $C^2$ self 未由本稿新增主锥宣称为零。

原 canonical 第四 period、其余零／一 Gaussian history、
平台／退化通量／端芽、整条闭路径 ruling 和同一个 gauge 的 joint 条件仍未付。
本稿完成的是当前同一最终弱圆上，完整 $W^2$ 与全部既有面积、局部角商、
五个旧对称乘积、$ZZ_0$、$\Psi$ 和三行的联合有限支付。
