# R372：真实 ZZ 第零角商闭合与九行有限频率联合支付

日期：2026-11-15。**完整有限纸面证明；未运行求积、符号程序、参数扫描、人工测试或研究计算。**

R369 已在当前同一个全偶真实弱圆构造中，联合支付完整 $P^2,PW,PZ,PY,ZW$ 对称乘积。这个结论不自动支付 $Z^2$。本稿处理 $Z^2$ 的第零外矩，并完整保留其额外角商与真实 primitive。

新角商并非仅凭 $F_{Z,1}=0$ 消失。它来自另一个 cubic 变分，含 $\int(Jq''{}^2)^2$；本稿先以三个已付面积和 R364 的局部 $\mathcal T=0$ 准确消去它。然后把实际 $\pi/2$ 值接入原八行，仍用同一个母、四种偶振荡形状和48个真实正幅列，得到同一有限频率的九行精确根。

新增的是完整 $ZZ_0(\theta)=0$；$ZZ_1$ 仍由反射为零，$ZZ_2$ 明确保留未付。没有把一个已消的角商当作全部对称乘积的通用处理。

来源：
[R259](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md)、
[R275](R275-first-moment-obstruction-for-the-small-width-two-slope-family.md)、
[R285](R285-principal-splitting-of-symmetric-Gaussian-products.md)、
[R293](R293-finite-frequency-zero-of-all-necessary-symmetric-Gaussian-observations.md)、
[R294](R294-corrected-self-fibers-pay-all-angular-symmetric-Gaussian-histories.md)、
[R354](R354-complete-reflection-and-positive-omega-bridges-pay-three-remaining-Gaussian-moments.md)、
[R359](R359-exact-same-weight-quotient-and-four-dimensional-cone-pay-the-Gaussian-PY-zero-moment.md)、
[R361](R361-even-weak-circles-and-three-oscillation-shapes-pay-the-negative-three-square.md)、
[R364](R364-local-angular-quotient-and-five-target-control-pay-the-negative-three-minus-one-product.md)、
[R368](R368-two-exact-cubic-identities-and-seven-target-control-pay-the-PY-product.md)、
[R369](R369-vanishing-first-cubic-and-eight-target-control-pay-the-ZW-product.md)。

## 1. 同一个对象、原系数及完整角商

保持
$$
P=\Phi_{r_0},\quad R=\Phi_{r_1},\quad S=\Phi_{s_0},
\quad L=\Phi_{p_0},\quad U=\Phi_{s_1},\quad Y=\Phi_{p_2},
$$
$$
W=aR+bS,\qquad Z=dL+eU.
$$
仍固定 $0<\zeta=\kappa^2<1/100$、$\kappa>0$，实际系数是
$$
a=-\frac{51\zeta^2+2\zeta+8}{64h_e^2},\quad
b=-\frac{34\zeta^2+8\zeta}{64h_e^2},\quad
d=\frac{6\kappa\zeta}{h_e},\quad
e=-\frac{\kappa(15\zeta+1)}{4h_e}.
\tag{1}
$$
本稿用到
$$
a,d,e,d+4e,d+6e,d+7e,2e-d\ne0,\qquad a-b\ne0.
\tag{2}
$$
例如 $d+4e=-\kappa(9\zeta+1)/h_e$；其余非零范围与 R364/R369 相同。

令
$$
\phi=f\cos\theta+g\sin\theta,\qquad D=f\odot f-\phi\odot\phi.
$$
$f,g$ 是同一构造中的全偶实紧函数，保三矩圆、弱单 hook、
非零 derivative rank-two 核与完整第二／第三 range。
原18个反对称 Gaussian 外矩、$\Psi$、三条 directed 行及 R364 的
$$
\mathcal T(f,g)=
\operatorname{Re}\{\mathfrak k(f+ig)-\rho_\kappa\mathfrak j(f+ig)\}=0,
\qquad
\rho_\kappa=\frac{28e}{15(d+7e)}
\tag{3}
$$
全部是本稿必须保持的条件。

normalized 平方外矩为
$$
\mathcal Q_{ZZ,j}
=-I_j(ZD,ZD)+2I_j\{\phi,Z(\phi,ZD)\}.
\tag{4}
$$
$ZD$ 的紧性来自整个 $D$ 的三矩零；单包 $Z(u,u)$ 仍可带真实左尾。

原十二完整副本清除 angular odd 项后，R294 的准确槽代数给
$$
\mathcal Q_{ZZ,0}(\theta)
=\sin^2\theta\,\mathcal Q_{ZZ,0}(\pi/2)
+\sin^2\theta\cos^2\theta\,\Xi_{ZZ,0},
\tag{5}
$$
$$
\Xi_{ZZ,0}=\operatorname{Re}K_{ZZ,0}(q),\qquad q=f+ig,
$$
$$
K_{ZZ,0}(q)=I_0(Zq^2,Zq^2)+2I_0\{q,Z(q,Zq^2)\}.
\tag{6}
$$
以下先计算(6)，不把 $\Xi$ 设成零。

## 2. 合法复输入与真紧 cubic 变分

三个原实矩圆给
$$
I_j(q,q)=0,\qquad j=0,1,2.
\tag{7}
$$
所有复积分都为原双线性极化，不取复共轭。
写
$$
v=q',\quad r=q'',\quad t=r',\quad
P_q=J(r^2),\quad S_q=J(xr^2),
$$
$$
C_2=\int x^2r^4,\quad N=\int xvr^3,\quad
V_2=\int v^2r^2,\quad U_3=\int qr^3,\quad
A_2=\int P_q^2.
\tag{8}
$$
$A_2$ 是原 primitive 的完整平方积分，不是面积记号。

R259 的原 cubic 密度为
$$
F_{L,0}(q)=-\frac12\int vr^2,\qquad
F_{U,0}(q)=\int(vr^2-xr^3).
$$
这两式先对任意紧输入成立；例如 $F_{L,0}$ 中使用
$\int rP_q=\int vr^2$，只由紧 outer 的零端值支付。
因此，令
$$
m=e-\frac d2,
$$
则
$$
F_{Z,0}(q)=m\int vr^2-e\int xr^3.
\tag{9}
$$

由(7)，$w=Z(q,q)$ 的完整二次／一次／常数左尾全部为零，右侧亦为零。
所以 $q+tw$ 是真正的紧输入族，合法变分给
$$
\boxed{K_{ZZ,0}(q)=DF_{Z,0}(q)[Z(q,q)].}
\tag{10}
$$
这一步不能直接对一般 nonlegal 单包使用。
本稿没有把其非零左尾假装成合法紧变分，也没有漏掉由此会产生的 Green 项。

## 3. 从原导数求完整 self，保原 primitive 的端项

原 $w=Z(q,q)$ 的导数为
$$
w'=dqr+2mxvr-\frac{3e}{2}x^2r^2-\frac d2xP_q+eS_q,
$$
$$
w''=(dq+2mxv-3ex^2r)t
+2evr-\left(\frac d2+2e\right)xr^2-\frac d2P_q.
\tag{11}
$$
由(9)，
$$
DF_{Z,0}[w]
=\int\{mr^2w'+(2mvr-3exr^2)w''\}.
\tag{12}
$$
含 $t$ 的完整多项式为
$$
2md\,qvrt+4m^2xv^2rt
-12mex^2vr^2t-3dexqr^2t+9e^2x^3r^3t.
\tag{13}
$$
逐项 IBP 所需五式为
$$
\begin{aligned}
\int qvrt&=-\frac{V_2+U_3}{2},\\
\int xv^2rt&=-\frac{V_2}{2}-N,\\
\int x^2vr^2t&=-\frac{2N+C_2}{3},\\
\int xqr^2t&=-\frac{U_3+N}{3},\\
\int x^3r^3t&=-\frac34C_2.
\end{aligned}
\tag{14}
$$
端项由紧 $q,v,r$ 消去。

与此同时，(11)—(12)中的 primitive 部分准确为
$$
\left(de+\frac{d^2}{4}\right)\int xP_qr^2
-dm\int P_qvr+em\int S_qr^2.
\tag{15}
$$
此处先保真实同锚 primitive，再用(7)：
$$
\int xP_qr^2=\frac12A_2,\qquad
\int P_qvr=\frac12V_2,\qquad
\int S_qr^2=-\frac12A_2.
\tag{16}
$$
第一、三式分别先保 $[xP_q^2]$、$[S_qP_q]$；
(7)使 $P_q,S_q$ 两侧真零后，才消这些边项。
第二式只需紧 $v$。
因此(15)为
$$
\frac{d^2+6de-4e^2}{8}A_2
+\left(\frac{d^2}{4}-\frac{de}{2}\right)V_2.
$$

把(13)—(16)和全部其余局部项合并，得到
$$
\boxed{
\begin{aligned}
K_{ZZ,0}(q)
={}&\frac{e(d+7e)}4C_2-4e^2N+deU_3\\
&+\left(\frac{d^2}{4}-\frac{3de}{2}+2e^2\right)V_2
+\frac{d^2+6de-4e^2}{8}A_2.
\end{aligned}}
\tag{17}
$$
这是完整 self，不是模 $C^2$ 的主式。
尤其 $A_2$ 仍在；它不能以“最终有三矩零”为由直接删掉。

## 4. 三个旧面积与 R364 的新局部条件共同闭合角商

记原 diagonal 面积
$$
S_{XY,j}(q)=2I_j\{q,[X,Y](q;q^2)\}.
$$
当前相应 full-circle 面积全相位为零，故其四次 Fourier 系数迫
$$
S_{PY,0}(q)=S_{PZ,2}(q)=S_{ZW,1}(q)=0.
\tag{18}
$$
这里 full-circle 面积采用 R259(9) 的 $I_j$ 规范，diagonal self 采用上述 $2I_j$ 规范。
具体说，面积中的 outer $f^2$ 项只有零／二次相位，
而 $-\phi^2$ 项的 $e^{-4i\theta}$ 系数是
$-S_{XY,j}(q)/32$。因此(18)不需额外假设 whole-pure。

R364 原准确 self 为
$$
S_{PY,0}
=-C_2+\frac83N-V_2-\frac43U_3-\frac12A_2,
$$
$$
S_{PZ,2}
=-\frac56(d+7e)C_2+\frac43(d+11e)N
-8eV_2-\frac83eU_3.
\tag{19}
$$
定义
$$
\mathfrak j=3V_2+U_3-2N,\qquad
\mathfrak k=V_2-\frac25N.
$$
由(19)的第二式为零，
$$
C_2=\frac85N-\frac{16e}{5(d+7e)}\mathfrak j.
\tag{20}
$$

还需要原 $ZW$ 第1面积，而非仅原 $PZ$ 两式。
R275 的完整表在合法复输入(7)上给
$$
\begin{aligned}
S_{LR,1}&=\frac{C_2}{6}-\frac N3+\frac{U_3}{3}-\frac{V_2}{2},\\
S_{LS,1}&=\frac{C_2}{6}-\frac N3+\frac{U_3}{3}+\frac{A_2}{4},\\
S_{UR,1}&=\frac{11C_2}{12}-\frac{8N}{3}+2V_2-\frac{A_2}{2},\\
S_{US,1}&=\frac{5C_2}{12}-\frac{2N}{3}.
\end{aligned}
\tag{21}
$$
R275 的 $U$、$T$ 名称分别对应本稿 $S$、$U$。
其 nonlegal 单包表中的 $\ell\mu_0^2$、$\mu_0\mu_1$ 及 Green 项，
在这里是由整个 $q$ 的真实 $\mu_0=\mu_1=0$ 消去；
没有将这个消去搬到各个微包。

令
$$
k_G=\frac{db}{2}-ea,\quad
p=\frac{d(a+b)+e(8a+2b)}3,\quad
\mathfrak d=2d(a+b)+e(11a+5b).
$$
按 $da,db,ea,eb$ 合并(21)，准确为
$$
S_{ZW,1}
=\frac{\mathfrak d}{12}C_2-pN
+\frac{d(a+b)}3U_3+\frac{a(4e-d)}2V_2
+\frac{k_G}{2}A_2.
\tag{22}
$$
先用 $S_{PY,0}=0$ 消 $A_2$，再代(20)，全部 $N$ 系数抵消，得到
$$
\boxed{
S_{ZW,1}=R_J\mathfrak j-\frac G2\mathfrak k,
}
\tag{23}
$$
$$
G=d(3a-b)+2ae,
$$
$$
R_J=
\frac{5d^2(a-b)+de(47a-19b)+4e^2(12a-5b)}
{15(d+7e)}.
$$
(23)是整个合法复输入的准确恒等，不限 R357 的特殊母包。
它也解释 R359 原同权商出现的同一两个系数。

由(18)、(23)和已经真实支付的(3)，
$$
R_J\operatorname{Re}\mathfrak j
-\frac G2\operatorname{Re}\mathfrak k=0,\qquad
\operatorname{Re}\mathfrak k-\rho_\kappa\operatorname{Re}\mathfrak j=0.
$$
原非退化 determinant 是
$$
R_J-\frac{G\rho_\kappa}{2}
=\frac{(a-b)(d^2+de+4e^2)}{3(d+7e)}\ne0.
\tag{24}
$$
故
$$
\boxed{\operatorname{Re}\mathfrak j
=\operatorname{Re}\mathfrak k=0.}
\tag{25}
$$
这不宣称两者的虚部也由该实条件自动为零。

(19)—(20)、(25)进一步给
$$
(\operatorname{Re}C_2,\operatorname{Re}N,
\operatorname{Re}V_2,\operatorname{Re}U_3,\operatorname{Re}A_2)
=\frac{\operatorname{Re}N}{5}(8,5,2,4,-4).
\tag{26}
$$
将(26)代入(17)，$d^2,de,e^2$ 三类系数分别准确为零。
所以
$$
\boxed{\Xi_{ZZ,0}=\operatorname{Re}K_{ZZ,0}(q)=0.}
\tag{27}
$$
这是完整原角商的闭合：使用真实 primitive、三个已付面积和已经单独支付的 R364 局部条件。
没有假设新增四次量自然属于旧纤维。

## 5. 完整角函数只余一个实际值

由(5)、(27)，原 angular odd 副本仍保持时，
$$
\boxed{
\mathcal Q_{ZZ,0}(\theta)
=\sin^2\theta\,\mathcal Q_{ZZ,0}(\pi/2).
}
\tag{28}
$$
同一全偶 profiles 的真实反射律还给 $\mathcal Q_{ZZ,1}=0$。
本稿不对 $\mathcal Q_{ZZ,2}$ 作任何自动结论。

因此下一步需要支付的是(28)的一个实际 scalar。
它的完整 $C^3$ 主项以及所有 $C^2$ 真余项都必须与此前八行同时处理。

## 6. 新 principal：原四种 χ 已足够，出现第四个二次位置方向

在末端强控制器的实际 rank-one 微包中仍写
$$
f_i=a_i u_i,\quad g_i=b_i u_i,\quad
\lambda_i=-a_i^2(a_i^2-b_i^2),\quad
v=u_i',\ r=u_i'',\ t=u_i'''.
$$
原二导主系数
$$
\alpha_Z=du+(2e-d)xv-3ex^2r
$$
给
$$
\mathcal Q_{ZZ,0}(\pi/2)
\equiv_2\sum_i\lambda_i\int\alpha_Z^2t^2.
\tag{29}
$$
$\equiv_2$ 仍保 R285 的完整连续 $C^2$ 余项，包括 Green、真实右历史和内部尾。

沿用 R369 的准确行变换
$$
\mathcal R_P=\mathcal Q_{PZ,2}+6e\mathcal Q_{PY,0},
\qquad
\mathcal R_Z=\mathcal Q_{ZW,1}-(a+b)\mathcal Q_{PZ,2}.
$$
其 principal 分别为
$$
-2(d+6e)x^2ur+2(d+4e)x^3vr,
$$
$$
2a\{dxuv+(2e-d)x^2v^2-3ex^3vr\}.
\tag{30}
$$

再取
$$
\mathcal R_Q=\mathcal Q_{ZZ,0}+9e^2\mathcal Q_{PY,0}.
$$
$x^4r^2$ 准确相消；完整 principal 密度为
$$
\begin{aligned}
d^2u^2+2d(2e-d)xuv
-6e(d+3e)x^2ur
+(2e-d)^2x^2v^2
+6e(d+e)x^3vr.
\end{aligned}
\tag{31}
$$
对同一偶母与偶 $\chi_\alpha$，写
$$
R_\alpha=\int r_0^2\chi_\alpha^2,\quad
V_\alpha=\int yv_0r_0\chi_\alpha^2,\quad
U_\alpha=\int u_0r_0\chi_\alpha^2,\quad
V_\alpha^{(2)}=\int v_0^2\chi_\alpha^2.
$$
保实际 $x=X+d_\nu+y$ 及全部复制正权 $\omega_\nu$。
(31)的位置次数至多2；其二次系数除共同
$W_c=\sum_\nu\omega_\nu>0$ 后为
$$
-6e(d+3e)U_\alpha+(2e-d)^2V_\alpha^{(2)}
+18e(d+e)V_\alpha.
$$
减掉
$$
\frac{3e(d+3e)}{d+6e}\,\mathcal R_P
+\frac{2e-d}{2a}\,\mathcal R_Z
$$
的二次系数，准确余下
$$
\boxed{
\gamma_\kappa V_\alpha,\qquad
\gamma_\kappa=-\frac{9ed(d+4e)}{d+6e}\ne0.
}
\tag{32}
$$
只用(2)即可判非零。

(31)—(32)没有删去 $u^2,xuv$ 等低次积分。
这些项在完整有限频率能量映射中仍全部保留；
它们只是不会影响这里的二次位置秩。

## 7. 同母九维实际主空间与48列正核

采用 R369 从起点已经证明可同时选择的同一个正解析母：
$\mathcal F_{\rm new}$ 的真实最大 minor 非零，
且四个实际偶 $\chi_\alpha$ 使
$$
(R_\alpha,V_\alpha,U_\alpha,V_\alpha^{(2)})
\quad(\alpha=1,2,3,4)
$$
满秩4。
这一选择来自明确正见证
$u=1+y^2/2+y^6+O(y^8)$ 的 finite-jet 子式 $720\ne0$
及最大 minor 的同一多项式直线，不是任意母 regular 的假设。

R361 原四目标可逆换为 $(H_0,H_a,H_b,H_d)$。
再将九行作(30)—(32)的固定可逆行变换：

- $\mathcal Q_{PY,2}$ 的最高位置次数6；
- $\mathcal Q_{PY,0}$ 的最高位置次数4；
- 四个二次位置系数对应
$$
R_\alpha,\quad
T_\alpha=-2(d+6e)U_\alpha+6(d+4e)V_\alpha,\quad
S_\alpha=2a\{(2e-d)V_\alpha^{(2)}-9eV_\alpha\},\quad
\gamma_\kappa V_\alpha;
$$
- 剩余三个常数方向仍在
$(R_\alpha,V_\alpha,U_\alpha)$ 上满秩3。

四个二次行在满秩4的母积分列上独立：
最后一行先给 $V_\alpha$，第二、三行分别再给 $U_\alpha,V_\alpha^{(2)}$，第一行为 $R_\alpha$。
故同一实际 copy 权／位置下，九行联合秩为
$$
\boxed{1+1+4+3=9.}
\tag{33}
$$
也可逐 covector 检验：六次、四次系数先清两个坐标，
四种 $\chi$ 的二次系数清四个坐标，
最后常数三列清余下三个坐标。
真实偏移产生的低次项始终保留，不影响这个逐级消元。

仍使用 R369 的四组十二个实际交替位置，索引
$$
0,1,33,34,49,50,65,66,81,82,97,98.
$$
每组十二点的
$\beta_i=\prod_{k\ne i}(X_i-X_k)^{-1}$
满足 $\beta_i/\lambda_i>0$，准确消去次数至多十的位置多项式。
本稿九行次数仍至多6，因此每组都有严格正 kernel。
(33)给48列联合 span 为 $\mathbb R^9$，遂有
$$
\boxed{
\operatorname{cone}_+(\text{48个真实九行列})=\mathbb R^9,
\qquad\ker\cap\mathbb R^{48}_{>0}\ne\varnothing.
}
\tag{34}
$$
没有增加第五种母形状，也没有以 signed span 代替正幅可实现性。

## 8. 同一个有限 N 同点恢复全部五个旧乘积

继续使用 R364 的显式有限映射
$$
\mathcal F_{\rm new}
=(\mathcal F_\star,\
\text{全部 }\mathfrak j,\mathfrak k
\text{ 的实际平移系数}).
$$
本稿不在该映射之外假定任何新的 $C^2$ 角量已被固定。
新增角商(27)是由原式及被保持的面积／$\mathcal T$ 推出。

从原最后控制器以前的实际负 $\Psi$ 入口开始，
固定弱 rank-two 核、全部面积和角商模块、宽过渡、补矩及其最终位置。
先选同母最大 minor、四个 $\chi$ 和真实 copy，
再固定末强宏块的正静态幅支付 $\Psi$。
仍仅在强 rank-one 微包上作
$$
u_{N,z}=u_0+N^{-3}z\chi_\alpha\cos Ny
+\sum_\ell a_\ell(N,z)e_\ell,
\qquad
\mathcal F_{\rm new}(u_{N,z})=\mathcal F_{\rm new}(u_0).
\tag{35}
$$
同一最大 minor／局部常秩保持整个有限映射。
纠正及参数一导在 $C^2$ 为 $O(N^{-1})$，固定纠正方向的三导贡献同阶；
有限正幅盒先固定，频率后选。

本次完整九量是
$$
\mathbf G_N=
(\mathcal Q_{PP,0},F_0,F_1,F_2,
\mathcal Q_{PZ,2},\mathcal Q_{PY,0},\mathcal Q_{PY,2},
\mathcal Q_{ZW,1},\mathcal Q_{ZZ,0})(\pi/2).
$$
R285 的完整主分裂和真实同频平均给
$$
\mathbf G_N(\mathbf z)=
\mathbf G_{\rm base}+\sum_i z_i^2v_i+o_{C^1}(1).
\tag{36}
$$
这里基线包括原弱核、所有强宏块、最终 copy 权／中心、原 Green、
内部非紧微包尾与全部 $C^2$ 四次项。
不同完整 block 仍按原真三矩零和完整支持论证加法；
没有将弱核套成 rank-one，也没有把微包分别假定为三矩合法。

由(34)，极限目标有全部严格正的平方幅解。
选九个独立列并固定其余正幅，Jacobian 为 $2z_iv_i$，可逆。
完整 $C^1$ 收敛使非退化零稳定，得到一个足够大但真正有限的整数 $N$ 和精确根
$$
\boxed{\mathbf G_N=0.}
\tag{37}
$$
不以 $N=\infty$ 作为实际 profile。

(35)保全部18面积、末强块原72面积数据、R364 的 $\mathcal T$ 与 quartic $C$，
故 $\Psi$、原三条 directed 行、指定一层／完整第三保持。
前八行和原全角身份同时恢复整个
$P^2,PW,PZ,PY,ZW$。
第九行经(27)—(28)准确给
$$
\boxed{\mathcal Q_{ZZ,0}(\theta)=0\quad\text{所有相位}.}
\tag{38}
$$
空间镜像共享参数，$f,g$ 仍全偶，$ZZ_1=0$ 也保持。

同一构造可将第九行指定为任意有限实数 $\tau$，前八行为零；
此时准确得到 $\mathcal Q_{ZZ,0}(\theta)=\tau\sin^2\theta$。
因此这里确实支付一个新的可联合调节方向，而不是声称旧八行已自动推出(38)。

## 9. 选择顺序及准确未付范围

从一开始选定有限 $\mathcal F_{\rm new}$ 和同母最大 minor，
再定实际 $\chi$、所有强／弱完整 copy、正静态幅与最终中心。
有限幅盒确定之后才选有限 $N$，解(37)。
根后不再平移、换锚或改共享 copy。

全部正负支撑和有限 profiles 确定之后，按 R354 选择新共同物理区间、
足够大的 $\omega$ 下界及初始小 $h_e$，安装真实闭 hook 与共振保护芽。
新行只有原固定非零 Gaussian 系数的共同尺度；
(2)、(24)、(32)保证这个最后几何选择不改变零方程。
不将它变成某条旧冻结几何或旧窄区间上的免费扩域。

当前剩余的反射允许对称位置为
$$
ZZ:2;\qquad ZY:0,2;\qquad
WW:0,2;\qquad WY:1;\qquad YY:0,2.
$$
共8个完整角函数位置，不是独立 rank。
特别 $ZZ_2$ 的完整 cubic／角商还需原式另付，
不能从本稿的第零矩闭合推断。

其余零／一 Gaussian history、原 canonical 第四 period、
平台／退化通量／端芽、整条闭路径 ruling 及同一 gauge 的 joint 条件仍未完成。
当前新几何也不继承另一条几何的 wholeE、Morse 或 full period。
本稿严格完成的是当前同一最终真实弱圆上，
在全部五个旧对称乘积与原18面积／$\mathcal T$／$\Psi$／三行共同保持下，
新增 $ZZ_0$ 的完整全角有限支付。
