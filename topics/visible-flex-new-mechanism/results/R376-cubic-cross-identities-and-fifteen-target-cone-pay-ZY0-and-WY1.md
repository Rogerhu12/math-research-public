# R376：完整 cubic 交叉恒等与十五行正锥支付 ZY0 和 WY1

日期：2026-11-15。**完整有限纸面证明；未运行求积、符号程序、参数扫描、人工测试或研究计算。**

本稿沿 R373、R375 的同一个全偶真实弱圆构造，新增 $ZY$ 的第0外矩和 $WY$ 的第1外矩。先保真实右 primitive 与 Green 尾，证明这两个完整角商均由已付的面积恒等消去；没有新增一个被默认落入旧纤维的 $C^2$ 条件。随后给十五个完整主行的有限 jet 见证、同母最大 minor 和180个实际正幅列。一个有限频率十五行根同时保持全部旧目标并支付两个新值。

最高位置次数仍为10。十二点正 kernel 只用于每个实际形状组的十次多项式；十五维来自十五个真实形状组的联合 span，不把十二点当作十五阶差分。最后尚欠的是 $ZZ_2$ 与 $YY_0$ 两个完整角函数位置。

来源：
[R259](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md)、
[R280](R280-ordered-three-moment-areas-and-five-block-Gaussian-cancellation.md)、
[R285](R285-principal-splitting-of-symmetric-Gaussian-products.md)、
[R293](R293-finite-frequency-zero-of-all-necessary-symmetric-Gaussian-observations.md)、
[R294](R294-corrected-self-fibers-pay-all-angular-symmetric-Gaussian-histories.md)、
[R325](R325-inward-weak-hook-circles-pay-three-directed-rows-and-the-one-history-compatibility.md)、
[R353](R353-ordered-tails-and-three-positive-centers-pay-the-positive-minus-two-first-moment.md)、
[R354](R354-complete-reflection-and-positive-omega-bridges-pay-three-remaining-Gaussian-moments.md)、
[R360](R360-complete-positive-negative-second-self-and-six-dimensional-middle-cone.md)、
[R361](R361-even-weak-circles-and-three-oscillation-shapes-pay-the-negative-three-square.md)、
[R364](R364-local-angular-quotient-and-five-target-control-pay-the-negative-three-minus-one-product.md)、
[R368](R368-two-exact-cubic-identities-and-seven-target-control-pay-the-PY-product.md)、
[R369](R369-vanishing-first-cubic-and-eight-target-control-pay-the-ZW-product.md)、
[R372](R372-complete-ZZ-zero-angular-quotient-and-nine-target-finite-frequency-control.md)、
[R373](R373-complete-W-square-angular-quotients-and-eleven-target-control.md)、
[R375](R375-exact-Y-second-cubic-and-thirteen-target-control-pay-ZY2-and-YY2.md)。

## 1. 当前同一圆与准确规范

仍用原算子
$$
P=\Phi_{r_0},\quad R=\Phi_{r_1},\quad S=\Phi_{s_0},\quad
L=\Phi_{p_0},\quad U=\Phi_{s_1},\quad Y=\Phi_{p_2},
$$
$$
W=aR+bS,\qquad Z=dL+eU.
$$
固定 $0<\zeta=\kappa^2<1/100$、$\kappa>0$，
$$
a=-\frac{51\zeta^2+2\zeta+8}{64h_e^2},\qquad
b=-\frac{34\zeta^2+8\zeta}{64h_e^2},
$$
$$
d=\frac{6\kappa\zeta}{h_e},\qquad
e=-\frac{\kappa(15\zeta+1)}{4h_e}.
\tag{1}
$$
特别 $a,d,e,a-b,d+6e$ 都非零。

令
$$
\phi=f\cos\theta+g\sin\theta,\qquad
D=f\odot f-\phi\odot\phi.
$$
当前 $f,g$ 全偶、实、紧，保原三矩圆、弱单 hook、非零 derivative rank-two 核与完整第三 range。对称外矩仍是
$$
\mathcal Q_{XY,j}
=-I_j(XD,YD)
+I_j\{\phi,X(\phi,YD)+Y(\phi,XD)\}.
\tag{2}
$$
$I_2(u,w)=\int(x^2u''w''+2u'w')$，两项始终共同保留。

对 whole legal complex input $q=f+ig$，三种双线性矩均为零，故 $X(q,q)$ 对所有 $X\in E_8$ 都真紧。定义
$$
F_{X,j}(q)=I_j(q,X(q,q)),
$$
$$
S_{XY,j}(q)=2I_j\{q,[X,Y](q;q^2)\},
$$
$$
K_{XY,j}(q)
=I_j(Xq^2,Yq^2)
+I_j\{q,X(q,Yq^2)+Y(q,Xq^2)\}.
\tag{3}
$$
这里 $S$ 是两倍 pure area；本稿的 whole area 使用 $I$ 规范。

所有18个 whole area 已经为零。它们的第4谐波给
$$
S_{XY,j}(q)=0.
\tag{4}
$$
准确系数为 $-S/32$；若采用 $2I$ 的 raw whole area 规范，则为 $-S/16$。本稿只使用该非零系数与完整零结论。

由于此处变分方向 $Xq^2,Yq^2$ 真紧，原紧域变分准确给
$$
S_{XY,j}
=DF_{X,j}[Yq^2]-DF_{Y,j}[Xq^2],
$$
$$
\boxed{
K_{XY,j}=DF_{X,j}[Yq^2]-\frac12S_{XY,j}.
}
\tag{5}
$$
(5)不用于单个 nonlegal 微包。后文引用的单包 self 仍先保原 Green 与 primitive，再在 whole legal q 上施三矩零。

## 2. 一个保真实 primitive 的完整交叉积分

暂写 $u=q,v=q',r=q''$，并令
$$
C=J(x^2r^2+2v^2),\qquad
Jz(x)=\int_x^{r_I}z(t)\,dt.
$$
原完整 $Y$ 的两个导数是
$$
Y'=-u^2+x^2ur-x^3vr+\frac{x^4r^2}{4}-\frac{xC}{2},
$$
$$
\begin{aligned}
Y''={}&(x^2u-x^3v+x^4r/2)r'
-2uv+2xur-2x^2vr\\
&-\frac C2+\frac{x^3r^2}{2}+xv^2.
\end{aligned}
\tag{6}
$$
其真实左二次尾并未在推导中删除。

记
$$
\mathscr B(u)
=\int\left(vrY''+\frac12r^2Y'\right).
\tag{7}
$$
为列出完整归并，设
$$
\begin{array}{llll}
E_1=\int u^2r^2,&E_2=\int xuvr^2,&
E_3=\int x^2v^2r^2,&E_4=\int x^2ur^3,\\
E_5=\int x^3vr^3,&E_6=\int x^4r^4,&
E_7=\int v^4,&E_8=\int xCr^2.
\end{array}
$$
由(6)中的三项含 $r'$ 的积分，
$$
\int x^2uvrr'=-E_2-\frac12E_3-\frac12E_4,
$$
$$
-\int x^3v^2rr'=\frac32E_3+E_5,\qquad
\frac12\int x^4vr^2r'=-\frac23E_5-\frac16E_6.
$$
原 primitive 项保为
$$
-\frac12\int vrC=-\frac14E_3-\frac12E_7,
\tag{8}
$$
其中只用了紧 $v$ 与 $C'=-(x^2r^2+2v^2)$；没有置 $C$ 的左值为零。其余两项
$\int uv^2r=-E_7/3$、$\int xv^3r=-E_7/4$ 也只有紧 outer 边项。

全部相加得到
$$
\boxed{
\mathscr B
=-\frac12E_1+E_2-\frac54E_3
+\frac13E_5-\frac1{24}E_6-\frac1{12}E_7-\frac14E_8.
}
\tag{9}
$$

R353 的两条完整 nonlegal self 是
$$
S_{RY,1}
=-E_1+4E_2-\frac72E_3-E_4
+\frac53E_5-\frac7{24}E_6-\frac16E_7,
$$
$$
S_{SY,1}
=2E_2-E_3-E_4+E_5-\frac5{24}E_6+\frac12E_8
-\frac{\mu_1\mu_2}{2}.
\tag{10}
$$
因此对任意紧输入，真实身份为
$$
\mathscr B
=\frac{S_{RY,1}-S_{SY,1}}2-\frac{\mu_1\mu_2}{4}.
\tag{11}
$$
现在才在 whole legal $q$ 上用 $\mu_1=\mu_2=0$，得到
$$
\boxed{\mathscr B(q)=\frac{S_{RY,1}(q)-S_{SY,1}(q)}2.}
\tag{12}
$$
这一步保住了 nonlegal self 的准确尾代价；没有逐包删掉 $\mu_1\mu_2$。

## 3. WY 第1角商是原面积的准确倍数

原 cubic 为
$$
F_{W,1}
=\frac{a+b}{3}\int xr^3-a\int vr^2,
\qquad
F_{P,2}=\int\left(\frac43xr^3-2vr^2\right).
\tag{13}
$$
原 $F_{Y,2}\equiv0$ 对任意紧输入成立，且无除 $x$ 的证明已经由 R291/R368/R375 支付。

记
$$
X_Y=\int xr^2Y''.
$$
紧方向 $Yq^2$ 的变分给
$$
S_{PY,2}=DF_{P,2}[Yq^2]=4(X_Y-\mathscr B),
$$
$$
DF_{W,1}[Yq^2]
=(a+b)X_Y-2a\mathscr B
=\frac{a+b}{4}S_{PY,2}+(b-a)\mathscr B.
\tag{14}
$$
R360 的准确 whole legal 身份为
$$
S_{PY,2}=-2S_{RY,1}-2S_{SY,1}.
\tag{15}
$$
原 nonlegal 版本另带 $-\mu_1\mu_2$；这里只在三复矩全零后使用(15)。

代(12)、(15)，得到
$$
DF_{W,1}[Yq^2]=-aS_{RY,1}-bS_{SY,1}
=-S_{WY,1}.
$$
由(5)，
$$
\boxed{
K_{WY,1}(q)=-\frac32S_{WY,1}(q).
}
\tag{16}
$$
这是 whole legal self 的完整身份，不是模 $C^2$ 或 principal 的关系。
当前面积给 $S_{WY,1}(q)=0$，因此整个额外角商准确为零。

## 4. ZY 第0角商由三个已付面积消去

原另一个 cubic 为
$$
F_{Z,0}
=(e-d/2)\int vr^2-e\int xr^3.
\tag{17}
$$
同样沿真紧 $Yq^2$ 变分：
$$
\begin{aligned}
DF_{Z,0}[Yq^2]
&=2(e-d/2)\mathscr B-3eX_Y\\
&=-(d+e)\mathscr B-\frac{3e}{4}S_{PY,2}.
\end{aligned}
$$
所以
$$
\boxed{
K_{ZY,0}(q)
=-(d+e)\mathscr B(q)
-\frac{3e}{4}S_{PY,2}(q)
-\frac12S_{ZY,0}(q).
}
\tag{18}
$$
原面积先给 $S_{PY,2}=S_{WY,1}=0$。
由(15)及
$aS_{RY,1}+bS_{SY,1}=0$，再用 $a-b\ne0$，
得到 $S_{RY,1}=S_{SY,1}=0$。故(12)、(18)和 $S_{ZY,0}=0$ 给
$$
\boxed{K_{ZY,0}(q)=K_{WY,1}(q)=0.}
\tag{19}
$$

R294 的完整角分解及原十二副本因而给
$$
\boxed{
\mathcal Q_{ZY,0}(\theta)
=\sin^2\theta\,\mathcal Q_{ZY,0}(\pi/2),\qquad
\mathcal Q_{WY,1}(\theta)
=\sin^2\theta\,\mathcal Q_{WY,1}(\pi/2).
}
\tag{20}
$$
其中 $s^2c^2$ 系数正是 $\operatorname{Re}K(q)$；不是只比较一个 pure 值。
原全偶反射已给 $ZY_1=0$ 及 $WY_0=WY_2=0$。
因此只需把(20)的两个真实值与旧十三行共同支付。

## 5. 十五个完整目标与原主分裂

末控制器的真实微包仍为
$$
f_i=a_i u_i,\quad g_i=b_i u_i,\quad
\lambda_i=-a_i^2(a_i^2-b_i^2)\ne0.
$$
只在这些强 rank-one 包内振荡；原弱 rank-two 核、宽 cutoff 和所有旧宏块固定。

设 $v=u',r=u'',t=u'''$。原主系数为
$$
\alpha_P=-2r,\qquad
\alpha_W=2av-2(a+b)xr,
$$
$$
\alpha_Z=du+(2e-d)xv-3ex^2r,\qquad
\alpha_Y=x^2u-x^3v+\frac12x^4r.
\tag{21}
$$
R285 对整个原式保尾的分裂给
$$
\mathcal Q_{XY,j}(\pi/2)
\equiv_2\sum_i\lambda_i\int x^j\alpha_X\alpha_Y\,t^2.
\tag{22}
$$
$\equiv_2$ 的余项是实际连续 $C^2$ 多项式泛函，含全部 Green、右历史、内部尾及 $I_2$ 第二项。有限根中保全部余项，不将它们置零。

原四完整目标 $(\mathcal Q_{PP,0},F_0,F_1,F_2)$ 可用 R361 的 determinant $128ad\ne0$ 换成四个主密度
$$
r^2,\quad x^2r^2,\quad xvr,\quad ur.
$$
其余十一行取
$$
\begin{gathered}
x^2\alpha_P\alpha_Z,\quad
\alpha_P\alpha_Y,\quad x^2\alpha_P\alpha_Y,\quad
x\alpha_Z\alpha_W,\quad \alpha_Z^2,\\
\alpha_W^2,\quad x^2\alpha_W^2,\quad
x^2\alpha_Z\alpha_Y,\quad x^2\alpha_Y^2,\quad
\alpha_Z\alpha_Y,\quad x\alpha_W\alpha_Y .
\end{gathered}
\tag{23}
$$
最后两行是本稿新增 $ZY_0,WY_1$。它们的位置次数均不超过6；全表最大次数仍为10。

## 6. 十五个主多项式的完整独立性

本节只证明一个明确有限多项式事实，不把形式独立自动当成真实母形自由。

给 $x,u,v,r$ 分别赋权 $1,2,1,0$，把 $a,b,d,e$ 视为已固定实常数。十五行分为权
$$
0,\quad 2,\quad 4,\quad 6,\quad 8,\quad10
$$
的六组，行数分别是
$$
1,\quad4,\quad5,\quad3,\quad1,\quad1.
\tag{24}
$$

权0只有 $r^2$。
权2的四行为
$x^2r^2,xvr,ur,\alpha_W^2$；
最后一行的 $v^2$ 系数 $4a^2\ne0$，所以独立。

权4的五行为
$$
x^2\alpha_P\alpha_Z,\quad
\alpha_P\alpha_Y,\quad
x\alpha_Z\alpha_W,\quad
\alpha_Z^2,\quad
x^2\alpha_W^2.
$$
在任一零线性组合中，$u^2$ 系数先迫 $\alpha_Z^2$ 行的系数为零，因为它是 $d^2$；
接着 $xuv$ 迫 $x\alpha_Z\alpha_W$ 行为零，因为系数为 $2ad$；
再以 $x^2v^2$ 迫 $x^2\alpha_W^2$ 行为零。
剩下两行在 $(x^2ur,x^4r^2)$ 上的 determinant 为
$$
\det\begin{pmatrix}-2d&6e\\-2&-1\end{pmatrix}
=2(d+6e)\ne0.
\tag{25}
$$

权6的三行为
$$
x^2\alpha_P\alpha_Y,\qquad
\alpha_Z\alpha_Y,\qquad x\alpha_W\alpha_Y.
$$
$x^2u^2$ 先迫第二行的系数为零，其系数为 $d$；
$x^3uv$ 再迫第三行为零，其系数为 $2a$；
第一行非零。
权8只有非零的 $x^2\alpha_Z\alpha_Y$；
权10只有非零的 $x^2\alpha_Y^2$。

故十五行作为 $(x,u,v,r)$ 的真实多项式线性独立。以下把这个事实转成同一个正偶母及有限个实际 $\chi$，不把 $u,v,r$ 当作沿一条函数任意独立的变量。

## 7. 原真实 copy 的权和偏移不丢失

先按原末控制器的有限编码固定所有相对格点、八／十二完整副本及五个面积平衡 blocks。
R280(27)—(29)已证明 $A_\pm/m^2$、中心化平移和 $\chi_--\chi_+$ 只由布局决定，因此所有相对位置与正四次权可以先定，不依赖本节将选出的母函数。静态支付 $\Psi$ 时另乘的共同正因子不改变以下 rank 或 kernel。

选其中一个有原交替层的完整 block。
其 actual copy 坐标记为
$$
x=X+d_\nu+y,\qquad \omega_\nu>0,\qquad
W_c=\sum_\nu\omega_\nu>0.
$$
全部 $d_\nu,\omega_\nu$ 是实际数据，不换成同心模型。
空间镜像对本稿十五目标均为 reflection-even，可将其共同正贡献计入 $\omega_\nu$。

设 $\mathbf p(x,u,v,r)$ 为(23)连同原四行组成的十五维主多项式向量。每行满足
$$
p(-x,u,-v,r)=p(x,u,v,r).
\tag{26}
$$
对偶母、偶 $\chi$，在位置多项式的形式值 $X=0$，对 $y$ 和 $-y$ 配对，准确得到平移平均算子
$$
\mathscr A p(y,u,v,r)
=\frac12\sum_\nu\omega_\nu
\{p(y+d_\nu,u,v,r)+p(y-d_\nu,u,v,r)\}.
\tag{27}
$$
这是保全部真实 copy 的结果；不要求实际 $d_\nu$ 的奇矩先为零。

在 $x$ 次数至多10的多项式空间上，$\mathscr A$ 的最高次系数逐阶乘 $W_c$，其余只降低 $x$ 次数。故 $\mathscr A$ 是可逆的有限三角算子，也保(26)。
所以十五行 $\mathscr A\mathbf p$ 仍线性独立。
(27)只用来证明主列的系数空间；不在 $X=0$ 放置实际微包，也不移动已经固定的物理支撑。

## 8. 同一个正偶母的有限二阶 jet 见证

考虑开放集合
$$
0<y<1/2,\qquad U>0,\qquad R>0,\qquad V\in\mathbb R.
$$
若一个行 covector 消灭这个集合上所有
$\mathscr A\mathbf p(y,U,V,R)$，
相应多项式就在一个实开集上恒零，因而是零多项式，与前节独立性矛盾。
于是这些实际点值向量的 span 是 $\mathbb R^{15}$。

可逐次选出十五组有限数据
$$
(y_i,U_i,V_i,R_i),\qquad i=1,\ldots,15,
\tag{28}
$$
使其十五列 determinant 非零，且 $y_i$ 两两不同。
每一步排除有限个已经使用的 $y$ 不影响开放集合上的多项式结论。
这是有限评价见证的存在证明，不执行点值搜索，也不是假设任意母都 regular。

令
$$
\psi(y)=\exp[-1/(1-y^2)]\quad(|y|<1),
$$
外延拓零。在 $\pm y_i$ 按对应奇偶指定
$$
H=\log(U_i/\psi(y_i)),
$$
$$
H'=V_i/U_i-(\log\psi)'(y_i),
$$
$$
H''=R_i/U_i-(V_i/U_i)^2-(\log\psi)''(y_i).
\tag{29}
$$
有限 Hermite 插值并取偶部，给一个真实偶多项式 $H$。
$u^\dagger=\psi e^H$ 因而在这些点实现(28)，正 prefactor 在闭支撑上严格为正。
还可独立指定 $u^\dagger(0)=(u^\dagger)''(0)=1$。

用一个足够高但有限次数的偶多项式逼近 $e^H$，同时保持有限二阶 jets 的严格 determinant 与全区正性，得到同类真实见证 $\psi P^\dagger$。
这一步只用严格开性，不取点质量或无限次数作为最终函数。

从起点仍用同一个有限观察映射
$$
\mathcal F_{\rm new}
=(\mathcal F_\star,\
\text{全部 }\mathfrak j,\mathfrak k\text{ 的真实平移系数}).
\tag{30}
$$
它是共同支撑偶 $C^2$ 域上的有限多项式映射。
由原 $\psi$ 偶多项式类的稠密性及导数连续性，可选最大秩母及固定同类纠正方向，使一个真最大 minor 非零。

将它与 $\psi P^\dagger$ 用同类多项式直线连接。
固定的微分 minor 沿这条直线是一个非恒零多项式，故可以任意接近正见证而避开其有限零点。
有限多项式直线同时保正 prefactor、有限二阶点值 determinant 与 $u_0''(0)\ne0$。
因此同一个最终母 $u_0=\psi P_0$ 兼有：

- 原 $\mathcal F_{\rm new}$ 最大 minor；
- 十五个完整点值列的非零 determinant；
- 全区正解析 prefactor。

最后在每个 $\pm y_i$ 附近选一个足够窄但有限的实际偶 cutoff，
再用 $\psi$ 乘偶多项式逼近它。
于是得到十五个固定真实偶形状 $\chi_\alpha$，使
$$
\left[
\sum_\nu\omega_\nu
\int\mathbf p(d_\nu+y,u_0,u_0',u_0'')\chi_\alpha(y)^2\,dy
\right]_{\alpha=1}^{15}
\tag{31}
$$
满秩15。归一 cutoff 的正积分因子不影响此 determinant。
从头至尾是同一个母；没有将十五个独立母函数的数据拼接。

## 9. 180个实际正幅列，次数不超过原十二点界

每种 $\chi_\alpha$ 使用原编码一个互异层的十二个实际交替索引
$$
0,1,33,34,49,50,65,66,81,82,97,98.
\tag{32}
$$
原有限编码有至少2048层，十五组都是真实可用的不同微包。
同名八／十二副本和空间镜像共享同一个扰动参数，保原完整结构。

对每组的递增实际坐标 $X_i$，记
$$
\beta_i=\frac1{\prod_{k\ne i}(X_i-X_k)}.
$$
原实际 $\lambda_i$ 的交替号给
$$
\beta_i/\lambda_i>0.
\tag{33}
$$
每个完整主列都是
$$
\frac{\lambda_i}{2}
\sum_\nu\omega_\nu\int
\mathbf p(X_i+d_\nu+y,u_0,u_0',u_0'')\chi_\alpha^2\,dy.
\tag{34}
$$
因子 $1/2$ 是有限频率平方的准确平均；所有复制／镜像正因子已保留在 $\omega_\nu$。

(34)除 $\lambda_i/2$ 后，是 $X_i$ 的次数至多10多项式。
十二个真实点的 barycentric 身份故使每组都有全分量严格正的 kernel。
它没有消去任何超过10次的项。

若一个行 covector 消灭全部180列，则对每个 $\alpha$，该位置多项式有十二个不同零点，因而恒零。
其形式值 $X=0$ 再由(31)迫该 covector 为零。
因此
$$
\boxed{
\operatorname{rank}(\text{180个实际十五行列})=15,\qquad
\ker\cap\mathbb R_{>0}^{180}\ne\varnothing.
}
\tag{35}
$$
联合 span 与严格正 kernel 给
$$
\boxed{\operatorname{cone}_+(\text{180列})=\mathbb R^{15}.}
\tag{36}
$$
这里没有将 signed span 直接当作实际正幅可达性；(33)给了明确的正 kernel。

## 10. 同一个有限 N 的完整十五行根

仍从末控制器以前的实际入口开始：弱核、宽 cutoff、补矩、旧宏块、
全部18面积和 R364 的 $\mathcal T=0$ 已固定，留负 $\Psi$ 储备。
按前节选好母、全部真实 copy、最终中心和固定纠正方向后，
以末强块的静态正幅准确支付 $\Psi$。

每个选中微包采用
$$
u_{N,z}
=u_0+N^{-3}z\chi_\alpha\cos Ny+\sum_\ell a_\ell(N,z)e_\ell,
\qquad
\mathcal F_{\rm new}(u_{N,z})=\mathcal F_{\rm new}(u_0).
\tag{37}
$$
原最大 minor 与局部常秩保持整个(30)。
固定正幅盒上，纠正及参数一导在 $C^2$ 为 $O(N^{-1})$；
固定光滑 $e_\ell$ 的三导贡献同阶。
所以三导振荡平方及其参数一导给(34)，交叉振荡趋零，
完整 $C^2$ 余项及其参数一导趋向真实基线。

完整目标按顺序取
$$
\begin{aligned}
\mathbf G_N=(&
\mathcal Q_{PP,0},F_0,F_1,F_2,
\mathcal Q_{PZ,2},\mathcal Q_{PY,0},\mathcal Q_{PY,2},
\mathcal Q_{ZW,1},\mathcal Q_{ZZ,0},\\
&\mathcal Q_{WW,0},\mathcal Q_{WW,2},
\mathcal Q_{ZY,2},\mathcal Q_{YY,2},
\mathcal Q_{ZY,0},\mathcal Q_{WY,1})(\pi/2).
\end{aligned}
\tag{38}
$$
前十三行是 R375 的原完整目标；本稿只添最后两行。
固定的原四行可逆变换不影响精确零。

原完整加法与 R285 保尾分裂给
$$
\mathbf G_N(\mathbf z)
=\mathbf G_{\rm base}+\sum_i z_i^2v_i+o_{C^1}(1).
\tag{39}
$$
基线保弱 rank-two 核与其全部 mixed cross、宽 cutoff、
原补矩、真正 Green／右历史／平台尾、实际 copy 权和最后物理位置。
不把 rank-one 局部公式套到固定弱核，也不把单微包输出假设成紧。

由(36)，$-\mathbf G_{\rm base}$ 有全部严格正的平方幅表示；
若先得到某些零分量，加一个严格正 kernel 即可。
选十五个独立列，固定其余正幅，极限 Jacobian $2z_iv_i$ 可逆。
非退化零在小 $C^1$ 扰动下稳定，故存在一个足够大但**实际有限**的整数 $N$，使
$$
\boxed{\mathbf G_N=0.}
\tag{40}
$$
无需把离散 $1/N$ 当作一个已光滑延拓的 IFT 参数。
这是同一有限 $N$、同一个最终圆上的十五行共同根。

(37)保持原全部面积数据、$\mathcal T$ 与 quartic $C$ 及原弱核结构。弱核心固定，强块仍为 $W=0$ 的 rank-one 微包；由原 R325(30)、§8，强块 $\Psi$ 只通过固定的 $C_{22}$ 变化，故整个 $\Psi=0$ 在每个允许纤维扰动上准确保持。三条 directed 行及其它 $C^3$ 目标则由(40)的同点完整根恢复；完整根同时保弱单 hook、指定一层和完整第三。
前十三行恢复原所有已付完整对称函数；
(19)—(20)把最后两行准确提升为
$$
\boxed{
\mathcal Q_{ZY,0}(\theta)=
\mathcal Q_{WY,1}(\theta)=0
\quad\text{对全部相位}.
}
\tag{41}
$$
同一正锥证明也可将这两行指定为任意固定有限实数，
前十三行仍为零；对应完整函数是各自常数乘 $\sin^2\theta$。

## 11. 实际选择顺序与剩余两门

本稿只扩大末端有限频率控制器，不增加末控制器以前的新角商费用。

先固定原弱基线、有限映射(30)、编码及相对 copy 数据；
再按§8选同母最大 minor、十五个实际形状和固定纠正方向；
随后固定全部最后中心、静态正幅、有限正幅盒；
最后取同一个有限 $N$ 解(40)。
实际根后不再平移、换锚或拆开共享副本。

$h_e$ 的非零共同行因子可先归一：
$a,b$ 同乘 $h_e^{-2}$，$d,e$ 同乘 $h_e^{-1}$。
因此本稿的严格独立性和零目标只依赖已固定的小 $\kappa$，
不阻止 R354 在全部有限 profile 包络确定后选择新共同物理区间、
足够大的 $\omega$ 下界和初始小 $h_e$，安装真实闭 hook 与共振端芽。
所有末母及振荡仍为 $\psi$ 乘固定有限解析 prefactor；
有限 $N$ 足够大时其全区正性也保持。
不继承另一条几何的 wholeE、Morse 或全 period。

现在完整支付的对称乘积是
$$
\boxed{P^2,\ PW,\ PZ,\ PY,\ ZW,\ W^2,\ ZY,\ WY.}
$$
另保 $ZZ_0,ZZ_1$ 与 $YY_1,YY_2$。
剩余准确为
$$
\boxed{ZZ_2,\qquad YY_0.}
$$
这是两个完整角函数位置，不是独立 rank。
它们的角商不能由十五维 principal span 免费推出。补充：R377 已消费 R349 的完整 $S_{UY,2}=-5S_{LY,2}$，证明 $YY_0$ 额外角商由原18面积准确为零；本稿尚未把它的 $\pi/2$ 实际值加入同点根。$ZZ_2$ 的完整角商仍须另付。

原 canonical 第四 period、其余零／一 Gaussian history、整条闭路径 ruling、
平台／退化通量／端芽及同一个 gauge 的 joint 条件仍未付。
本稿的新增结论严格是：同一最终全偶真实弱圆上，
完整 $ZY_0,WY_1$ 与全部18面积、原 $\mathcal T$、
此前十三个完整目标、$\Psi$ 和三行共同有限支付。
