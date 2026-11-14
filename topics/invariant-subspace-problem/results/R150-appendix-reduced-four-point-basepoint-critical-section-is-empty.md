# R150 附录：四不同点、满秩外均值的有基点临界截面为空

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d。

状态：**已证明的整类排除。** 在原六模式完整立方临界条件下，保持均值 Hankel 秩三、第三普通矩本质支撑三维而均值在其外、原二阶矩秩四。若准确四维支撑由四个不同物理点组成，其物理四投影不能有基点。

因此这一整个不同四点子类只剩无基点五次曲线，经准确长度二、与原支撑互素的中心除子双有理投向不可约平面三次曲线。本文排除的是上一稿的全部六个有基点候选，未把重 jet 或二阶矩降秩混入。

## 1. 六候选上的同一原张量及两个实际锚

沿用[六支撑与半权节点归约](R150-appendix-reduced-four-point-basepoint-critical-section-six-supports.md)。若这样的有基点完整临界点存在，则可以编号使
$$
A=\{0,2,3\},\qquad \operatorname{span}\{u_i:i\in A\}=W_\pm,
$$
而额外点为 $u_1=v(\tau)$，基点为 $s=s_0$。原二次目标为
$$
F_0=X_1L,\qquad L=k_{12}X_2+k_{13}X_3,
\qquad k_{12}k_{13}\ne0.
$$
节点中央权满足 $w_1=a_1l_1=1/2$，所以 $b_1=c_1=0$。所有节点均值 $a_i$ 和 $l_i=\lambda(u_i)$ 均非零。

把仅在 $A$ 上的二、三次普通矩记为
$$
\mathcal B=T_{2,A},\qquad \mathcal C=T_{3,A}.
$$
在三节点坐标中 $\mathcal B=yy^{\mathsf T}-2H$ 的交叉项为非零的 $a_i a_j$，因此 $\mathcal B\ne0$。

令 $\lambda_A=(l_i)_{i\in A}$，并将 $L$ 的系数向量记为 $l$。两个剩余完整梯度等价式是
$$
\mathcal C_l(p_A(z),p_A(z))\equiv0,
\tag{1.1}
$$
$$
\mathcal C(p_A(z))+3a_1p_1(z)\mathcal B(p_A(z))\equiv0.
\tag{1.2}
$$
原全部第三矩为
$$
T_3(r)=\mathcal C(r_A)+3a_1r_1\mathcal B(r_A).
$$
由于 $\lambda$ 湮灭它的本质支撑，对该张量收缩 $\lambda$ 并比较 $r_1$ 次数，准确得到
$$
\boxed{\mathcal B_{\lambda_A}=0,\qquad
\mathcal C_{\lambda_A}=-\tfrac12\mathcal B,\qquad
\mathcal C_{\lambda_A\lambda_A}=0.}
\tag{1.3}
$$
这里 $\mathcal C_\eta$ 表示对称张量收缩一次；相应方向导数为 $D_\eta\mathcal C=3\mathcal C_\eta$。

写 $p_A=P_\pm\psi$，其中 $\psi$ 是已付的非退化二次曲线参数化，方程为 $Q$。由 (1.1)，
$$
\boxed{\mathcal C_l=\kappa Q}
\tag{1.4}
$$
对某个标量 $\kappa$ 成立。

$[l]$ 是这条二次曲线上的点，因为 $l=p_A(\tau)$。$[\lambda_A]$ 也是同一二次曲线上的点：单基点与光滑中心定理已证明完整中心 $[\lambda]$ 在四维物理曲线上，且其全部物理原像与原四次支撑互素。取其中一个原像 $\zeta$，则 $\zeta\notin\{s_0,s_1,s_2,s_3\}$，且
$$
[\lambda_A]=[\psi(\zeta)],\qquad [l]=[\psi(\tau)].
$$
二次曲线参数化是同构，$\zeta\ne\tau$，所以这两个点不同。

除去 (1.2) 中的 $P_\pm^3$，剩下的是同一原有理式
$$
\boxed{\mathcal C(\psi(z))+3a_1R(z)\mathcal B(\psi(z))=0,
\qquad R(z)=p_1(z)/P_\pm(z).}
\tag{1.5}
$$
它有二次齐次次数；在改变物理射影参数时必须按该次数变换，不能把它当成次数零的不变函数。

## 2. 二次曲线上的纯代数引理

**引理。** 设 $Q$ 为非退化三元二次式，$\lambda,l$ 是其上两个不同点的非零代表，$\psi$ 是其无基点二次参数化。设非零二次式 $B$ 和三次式 $C$ 满足
$$
C_\lambda=-B/2,\qquad C_{\lambda\lambda}=0,\qquad
C_l=\kappa Q,
$$
以及
$$
C(\psi)+cR B(\psi)=0,\qquad c\ne0.
\tag{2.1}
$$
在将 $[l]$ 放到参数无穷远的仿射图中，若 $R$ 有准确两个不同简单极点，并在 $[\lambda]$ 及参数无穷远作为普通有理函数均有限，则：

1. $[\lambda]$ 的仿射参数是两个极点参数的算术平均；
2. $R(\lambda)+R(\infty)=0$。

**证明。** 选择三维坐标，使 $\lambda=e_0,l=e_2$，并归一化
$$
Q=x_0x_2-x_1^2.
$$
在参数上将 $\lambda$ 放到零、$l$ 放到无穷远，再作非零仿射缩放，可写
$\psi(t)=d(1,t,t^2)$，$d\ne0$。这只用了无基点二次参数化是完整二元二次线性系。

$C_{\lambda\lambda}=0$ 说明 $C$ 对 $x_0$ 至多一次；$D_lC=3\kappa Q$ 再精确给出
$$
C=-\frac32A x_0x_1^2+B_0x_1^3
-3\kappa x_1^2x_2+\frac32\kappa x_0x_2^2,
$$
$$
B=A x_1^2-\kappa x_2^2.
\tag{2.2}
$$
所有自由系数已经显示，没有略去其他三次项。

代入二次曲线，(2.1) 因而给
$$
R(t)=-\frac dc\,
\frac{-\frac32A+B_0t-\frac32\kappa t^2}{A-\kappa t^2}.
\tag{2.3}
$$
若 $\kappa=0$，该式至多是一次多项式；若 $A=0$，它至多在 $t=0$ 有一个极点，或为常数。二者都与假设不符。因此 $A\kappa\ne0$，并且两个分母零点均未被分子约掉。

两个极点准确是 $t=\pm\sqrt{A/\kappa}$，关于 $\lambda$ 的参数零点对称。而
$$
R(0)=\frac{3d}{2c},\qquad R(\infty)=-\frac{3d}{2c}.
$$
结论成立。将参数作仿射平移、非零缩放，或将 $R$ 乘非零常数，都保持所述两个条件。$\square$

## 3. 对原两个剩余极点的必要标量条件

记同一 $W_\pm$ 的另外两个根为 $a,b$，所以其三个根为 $s,a,b$。额外点为 $\tau$，四点互异。原配对模式给 $p_1(a),p_1(b)\ne0$，而 $p_1(s)=0$。故 $R=p_1/P_\pm$ 约分后准确只有 $a,b$ 两个简单极点；在投影中心的原像处有限。

原极化核的 $q(\tau,z)$ 被 $z-s$ 整除。写
$$
q(\tau,z)=(z-s)(\alpha z^2+\beta z+\gamma),
\qquad S=a+b,\quad P=ab.
\tag{3.1}
$$
忽略一个非零常数，原二次齐次有理式为
$$
R(z)=-(z-\tau)^2
\frac{\alpha z^2+\beta z+\gamma}{(z-a)(z-b)}.
$$
将额外点 $\tau$ 放到新参数无穷远，取齐次变换
$[z_0:z_1]=[x:\tau x+1]$。必须同时付上二次次数；因此新仿射表达准确为
$$
\widetilde R(x)=x^2R(\tau+1/x)
=-\eta\frac{A x^2+B x+C}{D x^2+E x+1},\qquad\eta\ne0,
\tag{3.2}
$$
其中
$$
\begin{aligned}
A&=\alpha\tau^2+\beta\tau+\gamma,&B&=2\alpha\tau+\beta,&C&=\alpha,\\
D&=(\tau-a)(\tau-b),&E&=2\tau-S.
\end{aligned}
$$
$D\ne0$，两个分母根不同。自极线在 $\tau$ 至少二重，恰保证 (3.2) 在新参数无穷远有限。

应用 §2，引理的第一个条件迫中心参数
$$
x_\lambda=-E/(2D).
$$
该点不是极点，因为
$$
D\bigl(Dx_\lambda^2+Ex_\lambda+1\bigr)
=D-E^2/4=-(a-b)^2/4\ne0.
$$
再代入第二个条件，清除此非零分母，得到
$$
2A+2DC-BE=0.
$$
左边精确约去所有 $\tau$ 的显式项：
$$
\boxed{\chi:=2\gamma+\beta(a+b)+2\alpha ab=0.}
\tag{3.3}
$$
这是同一原两梯度恒等式的必要条件，未重新选择中心或矩。

## 4. 原六个支撑全部违反该条件

按前稿的整数三次记号，
$$
P_+(s)=5s^3-25s^2+32s-8,\quad
\tau_+(s)=\frac{4s^2-s}{s+1},
$$
$$
P_-(s)=5s^3+135s^2+864s+864,\quad
\tau_-(s)=\frac{4s^2+31s+32}{s+1}.
$$
其余两根的和积为
$$
\begin{array}{c|cc}
& a+b&ab\\\hline
+&5-s&32/5-s(5-s)\\
-&-27-s&864/5-s(-27-s).
\end{array}
$$
对 (3.1) 作精确多项式除法，再模 $P_\pm(s)$ 化简，原 (3.3) 分别为
$$
\boxed{\chi_+(s)=-\frac{606665s^2-652964s+232916}{6860},}
\tag{4.1}
$$
$$
\boxed{\chi_-(s)=\frac{8954105s^2+80605252s+99846172}{43940}.}
\tag{4.2}
$$
完整原核运算由[精确验证器](../notes/2026-11-13-reduced-basepoint-critical-exclusion-verify.py)重建，[有限证书](../notes/2026-11-13-reduced-basepoint-critical-exclusion-certificate.json)保存全部输出；不是根据根的数值近似猜测非零。

令 (4.1)、(4.2) 的二次分子分别为 $C_+,C_-$。原整数结果式准确为
$$
\operatorname{Res}(P_+,C_+)=5930013732223926800
\equiv66\pmod{103},
$$
$$
\operatorname{Res}(P_-,C_-)=12326789196383727288230800
\equiv91\pmod{103}.
\tag{4.3}
$$
两者均非零。因此每个三次的全部复根都使相应 $\chi$ 非零，直接违反 (3.3)。这排除了全部六个候选。

## 5. 整类结论及准确剩余类型

所以不存在满足开头全部假设、四个物理支撑点互异且四维投影有基点的原完整临界点。

结合单基点定理和光滑中心定理，若原外均值满秩四点临界截面仍有点存在，则必须同时满足：

- 四维物理投影无基点，是双有理的非退化五次曲线；
- 原二次梯度给非零二次曲面，投影中心在其光滑部分；
- 从该中心投向本质三空间，像是不可约平面三次曲线；
- 中心的物理原像除子准确长二，且与原四点支撑互素。

还有一个直接的权参数限制。四个 $w_i$ 全非零，$\sum w_i=1$，中央第三矩的奇点恰对应半权分割；这一点已在长度四归约中完整证明。当前三次不可约，所以半权分割只能有一个（将一个子集与其补集认作同一分割）：若有两个不同奇点，连接它们的直线与三次至少有四重交，迫该直线为分量，矛盾。

每个这样的奇点还是普通节点。将其归一化为符号向量 $\varepsilon_i\in\{1,-1\}$，$\sum w_i\varepsilon_i=0$，中央三次的二次微分在超平面 $\sum w_i z_i=0$ 上来自非退化对角型 $\operatorname{diag}(w_i\varepsilon_i)$。其核准确是一维的奇点方向 $\varepsilon$；在射影切片上的二次型因此非退化。故当前尚可能的平面三次是节点三次，不是尖点三次。

上述排除严格保留外均值、非割线均值、$\operatorname{rank}H=4$ 和四点互异的范围。重 jets、有降秩 $H$ 的四维截面、均值割线情形及第三矩本质维数四至六仍须继续；没有由本稿得到全局 Jacobian 幂或原 $F^3$ 的完整循环性。
