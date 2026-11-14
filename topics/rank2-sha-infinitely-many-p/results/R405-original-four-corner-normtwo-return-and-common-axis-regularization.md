# R405：原两目标的 norm2 四角联合、双输出单位差与完整中央返回

日期：2026-11-14。**状态：已证明。** 在 R398、R399 的同一四条实际来源上，
本篇构造一个原五输入 norm2 联合。它的两个输出分别是 degree34 和
degree72，完整保留原 sigma 规范与所有单位域。两个真实 rank-two 来源
$S,T$ 占四角中的一对；另一对是质量一的 $G$ 与零质量的 $Q$。

由于四条真实 core 的符号不同，同一联合及其原 primitive-input
双输出深域给一个行列式恰为 $2\lambda^2$ 的整可逆返回。
它准确分离出 $\nu_S\otimes\nu_T$，并给两条中央同时失败的完整
$p^4u^2v^2$ 条件。本文不将原五输入的任意叶域赋成零，
也不从该单位矩阵单独推出无穷素数结论。

## 1. 同一模型、四角和原相位

全篇使用 R399 的 $E_b:y^2=x^3+b$、$b=17$、原周期 $\Omega$ 及固定 ray：
$$
\pi_0\equiv261631+198018\omega
 \pmod{279072\mathcal O_K},\qquad
\lambda=1/\bar\pi_0,\quad
\pi_{17}=\pi_{24}=-\pi_0,\quad
\kappa=p/\bar\pi_{17}^{\,2}.
\tag{1}
$$
$X=x^3$，$\delta=1+2\omega$。保留实际来源
$$
\begin{aligned}
A&=\sigma(z)\sigma(2z)\sigma(\delta z)
   =-2\delta\sigma^8xy,\\
C&=\sigma^{18}(X-8b)
      \left(X^2-\frac{4bX}{7}+\frac{16b^2}{7}\right),\\
D&=\sigma^{16}x^2(X+b),\\
H&=\sigma^{16}x^2(X^2+20bX-8b^2),\\
K&=\sigma^{38}x(X+b)Q_4(X),\\
L&=\sigma^{38}x(X^2+20bX-8b^2)Q_4(X),
\end{aligned}
\tag{2}
$$
其中 $Q_4=(X+4b)(X^3-96bX^2+48b^2X+64b^3)$。$A$ 的型为三，其余各条型为零。

定义四角
$$
\boxed{
S=DC,\qquad G=HC,\qquad
T=DLC=HKC,\qquad Q=DKC.
}
\tag{3}
$$
$S,T$ 是 R398 已付的两条原 rank-two 曲线来源在同一 frame 中的版本；
实际 $E_{24}$ 测度只需再乘固定单位 $-102816\sqrt[3]9$。
不能把 $G,Q$ 加入 rank-two 候选池。

原点阶为
$$
S=z^6+\cdots,\quad T=z^6+\cdots,\quad
G(0)=1,\quad Q=z^{12}+\cdots .
$$
全纯乘法身份准确为
$$
\boxed{S(z)T(z)=G(z)Q(z).}
\tag{4}
$$
(4) 是加法卷积身份，未被当作 Mellin 行列式恒等式。

R399 的全来源与整个 CM7 矩阵已支付本 ray 上
$$
\boxed{
\nu_S|_p=-\lambda[\kappa]_*\nu_S,\quad
\nu_T|_p=-\lambda[\kappa]_*\nu_T,\quad
\nu_G|_p=-\lambda[\kappa]_*\nu_G,\quad
\nu_Q|_p=+\lambda[\kappa]_*\nu_Q.
}
\tag{5}
$$
同时 $\nu_A,\nu_C,\nu_K$ 的原 core 都为
$+\lambda[\kappa]_*$。
因此
$$
J_S(0)=J_T(0)=J_Q(0)=0,\qquad
m_G:=J_G(0)=1+\lambda\in\mathcal O^\times.
\tag{6}
$$
这里单位证明来自实际 $E_1$ 偶 trace 和 Hasse 界，保原普通嵌入。

## 2. 完整 norm2 联合恰为四角差

令 $\mathsf P_wF(z,w)=\frac16\sum_{\zeta\in\mu_6}F(z,\zeta w)$。
R381、R387 已付原完整 norm2 式
$$
\mathsf P_w\bigl(A(z+w)A(z-w)\bigr)
=-12\bigl(D(z)H(w)-H(z)D(w)\bigr).
\tag{7}
$$
$C,K$ 型零，所以乘它们后可与这个**同一输出**投影交换。
由 (3)，得到全双变量身份
$$
\boxed{
\begin{aligned}
&S(z)T(w)-G(z)Q(w)\\
&\qquad=-\frac1{12}C(z)K(w)C(w)\,
       \mathsf P_w\bigl(A(z+w)A(z-w)\bigr).
\end{aligned}}
\tag{8}
$$
没有遗漏 R387 的 $20bD$：它在反对称式中准确抵消。

现在用五个真实原输入
$$
d\eta=-\frac1{12}\,
 d\nu_A(a)d\nu_A(b_1)d\nu_C(c)d\nu_K(k)d\nu_C(e),
$$
$$
Y=a+b_1+c,\qquad R=a-b_1+k+e .
\tag{9}
$$
设 $\mathsf P_R$ 为 $R$ 的实际 $\mu_6$ 推前平均，则 (8) 给
$$
\boxed{
\Delta:=\mathsf P_R(Y,R)_*\eta
=\nu_S\otimes\nu_T-\nu_G\otimes\nu_Q.
}
\tag{10}
$$
这是完整联合测度；输出单位域、每个深层和所有矩都可以直接代入。

原 Hermitian Gram 准确为
$$
\begin{pmatrix}1&1&1&0&0\\1&-1&0&1&1\end{pmatrix}
\operatorname{diag}(8,8,18,38,18)
\begin{pmatrix}1&1\\1&-1\\1&0\\0&1\\0&1\end{pmatrix}
=\operatorname{diag}(34,72).
\tag{11}
$$
它也直接由 $A(z+w)A(z-w)C(z)K(w)C(w)$ 给出。
每个线性系数都是原整系数 $0,\pm1$；在两轴上分别作原格平移，
各 sigma 的中心因子逐项相乘，正给 degree34、72 的原中心因子。
因此没有 R404 单项中额外的二分之一平移；两轴的原周期、半特征与
全部交叉 Gaussian 均由这个实际乘积支付。

投影只作用于原 $R$，不假设五输入各自可任意转相位。
对 $R$ 的单位/原点深域，它确实交换；对任意原叶条件则未必交换。

## 3. 两个输出的真实核心和单位返回

简记
$$
\mathcal A=\nu_S\otimes\nu_T,\qquad
\mathcal B=\nu_G\otimes\nu_Q,\qquad
\Sigma=\mathcal A+\mathcal B,\qquad\Delta=\mathcal A-\mathcal B.
$$
由 (5)，整个输出 core 是
$$
\boxed{
\Delta|_{Y\in p}=-\lambda[\kappa_Y]_*\Delta,\qquad
\Delta|_{R\in p}=-\lambda[\kappa_R]_*\Sigma.
}
\tag{12}
$$
第二式中的加号 $\Sigma$ 不能换回 $\Delta$：
$T$ 与 $Q$ 的原符号不同。
特别
$$
\boxed{
\frac12\left(\Delta-
 \lambda^{-1}[\kappa_R^{-1}]_*(\Delta|_{R\in p})\right)
=\mathcal A=\nu_S\otimes\nu_T .
}
\tag{13}
$$
逆缩放只作用于已限制的 $R\in p$ 域，所以是合法整映射。
(13) 是两个真实输出环带的转置，未把一个 source projector
误写成乘某个输出多项式。

两输出同时深时，
$$
\boxed{\Delta|_{Y,R\in p}
 =\lambda^2[\kappa_Y,\kappa_R]_*\Sigma.}
\tag{14}
$$

## 4. 原五输入 primitive 域给第二个完整返回

设
$$
\mathcal P=\{(a,b_1,c,k,e):\text{至少一个输入为单位}\},
\qquad
\Delta^{\rm prim}=\mathsf P_R(Y,R)_*(1_{\mathcal P}\eta).
$$
原五个输入的完整 core 都为 $+\lambda$，故
$$
\boxed{\Delta-\Delta^{\rm prim}
 =\lambda^5[\kappa_Y,\kappa_R]_*\Delta.}
\tag{15}
$$
这里 $\lambda^5$ 是单位，没有按 $A,K$ 的原点零阶擅添收缩。
五输入全深与两输出全深是不同的原域，(15) 恰好保留两者之间的差。

由 (14)、(15)，
$$
\boxed{
[\kappa_Y^{-1},\kappa_R^{-1}]_*
  (\Delta^{\rm prim}|_{Y,R\in p})
=\lambda^2\{(1-\lambda^3)\mathcal A
                  +(1+\lambda^3)\mathcal B\}.
}
\tag{16}
$$
它来自真正的 primitive 输入、两输出深碰撞，
包括每一种单位输入数目与全部相加 carry。

把 (10) 与 (16) 合成，其两列的行列式为
$$
\det\begin{pmatrix}
1&-1\\
\lambda^2(1-\lambda^3)&\lambda^2(1+\lambda^3)
\end{pmatrix}
=\boxed{2\lambda^2\in\mathcal O^\times}.
\tag{17}
$$
不需要分别假设 $1-\lambda^3$ 或 $1+\lambda^3$ 为单位。
准确逆式为
$$
\boxed{
\begin{aligned}
\mathcal A
&=\frac{1+\lambda^3}{2}\Delta
 +\frac1{2\lambda^2}
 [\kappa_Y^{-1},\kappa_R^{-1}]_*
 (\Delta^{\rm prim}|_{Y,R\in p}),\\
\mathcal B
&=\frac{\lambda^3-1}{2}\Delta
 +\frac1{2\lambda^2}
 [\kappa_Y^{-1},\kappa_R^{-1}]_*
 (\Delta^{\rm prim}|_{Y,R\in p}).
\end{aligned}}
\tag{18}
$$
原 $1/12$、两轴的两个深缩放、全部五输入条件都保留。

同一个符号差也可在 (4) 的两个加法卷积表示中读出：
$\nu_S*\nu_T$ 的全两输入深部为
$+\lambda^2[\kappa]_*(\nu_{ST})$，
$\nu_G*\nu_Q$ 的全两输入深部则为
$-\lambda^2[\kappa]_*(\nu_{ST})$。
所以它们的 primitive-input 输出差准确为
$-2\lambda^2[\kappa]_*\nu_{ST}$。
这条单输出式的来源是 $ST$；本文没有把它当作原 $S$ 或 $T$ 的中央零。

## 5. 全部 tame、原环带尺度与导数

置 $d=p-1$，并在单位输入上用
$$
\chi_{\ell,u}(t)=\omega_p(t)^\ell\langle t\rangle^{du},\qquad
U_\ell(u)=\omega_p(\bar\pi_{17})^{-2\ell}
          \langle\bar\pi_{17}\rangle^{-2du}.
$$
两变量 Mellin 记为 $\mathscr D_{\ell_1,\ell_2}(u,v)$。
由 (10)，
$$
\boxed{
\mathscr D(u,v)
=J_{S,\ell_1}(u)J_{T,\ell_2}(v)
 -J_{G,\ell_1}(u)J_{Q,\ell_2}(v).
}
\tag{19}
$$
四条来源型零，所以不相容的 tame 自动为零；
若直接在 (9) 上计算，仍使用原 $\mathsf P_R$，
不能先删掉其六相位。

令 $\mathscr D_{01}$ 在 $Y$ unit、$R\in p\mathbf Z_p^\times$ 上
用 $(Y,R/p)$ 测试。则
$$
\boxed{
\mathscr D_{01}(u,v)
=-\lambda U_{\ell_2}(v)
 [J_S(u)J_T(v)+J_G(u)J_Q(v)].
}
\tag{20}
$$
所以原两目标的完整乘积准确为
$$
\boxed{
J_S(u)J_T(v)
=\frac12\{\mathscr D(u,v)
 -\lambda^{-1}U_{\ell_2}(v)^{-1}\mathscr D_{01}(u,v)\}.
}
\tag{21}
$$

令 $\mathscr E_{11}$ 用同一五输入 $\mathcal P$，
限制 $Y,R\in p\mathbf Z_p^\times$，
并用 $(Y/p,R/p)$ 测试。则
$$
\boxed{
\mathscr E_{11}
=\lambda^2 U_{\ell_1}(u)U_{\ell_2}(v)
\{(1-\lambda^3)J_S(u)J_T(v)
 +(1+\lambda^3)J_G(u)J_Q(v)\}.
}
\tag{22}
$$
因而另一完整式为
$$
\boxed{
J_S(u)J_T(v)=\frac12\left\{
 (1+\lambda^3)\mathscr D(u,v)
 +\lambda^{-2}U_{\ell_1}(u)^{-1}U_{\ell_2}(v)^{-1}
       \mathscr E_{11}(u,v)\right\}.
}
\tag{23}
$$
(21)、(23) 包含所有 tame 和中央质量。
例如对第二变量求导时
$(U_{\ell_2}^{-1})'(0)=2d\log_p\bar\pi_{17}\,
 U_{\ell_2}(0)^{-1}$；
二阶混合导数保其两个一次项及乘积项。
只在已证明相应整条质量行为零时，才可删对应项。

## 6. 两条原失败的准确同核条件

以下取 principal 分支。因 (6)，
$$
\mathscr D(u,0)=0,\qquad
\mathscr D(0,v)=-m_GJ_Q(v),\qquad m_G=1+\lambda.
\tag{24}
$$
因此还有完整参考消去式
$$
\boxed{
\mathscr D(u,v)-\frac{J_G(u)}{m_G}\mathscr D(0,v)
=J_S(u)J_T(v).
}
\tag{25}
$$
$J_G(u)/m_G$ 是原整解析单位；它的未知斜率保持在式中。

若两个真正的原中央导数同时为零，则由于各自质量零，
$$
J_S(u)\in p^2u^2\mathcal O\langle u\rangle,\qquad
J_T(v)\in p^2v^2\mathcal O\langle v\rangle .
$$
系数界直接来自
$v_p((d\log\langle x\rangle)^n/n!)\ge n-v_p(n!)$；
在 $p>19,n\ge2$ 时至少二。
故以下三个实际表达式都属于
$$\boxed{p^4u^2v^2\mathcal O\langle u,v\rangle:}\tag{26}$$
(21) 的原相邻 $R$ 两环带差、(23) 的原五输入
primitive 双深域组合、以及 (25) 的完整参考消去。
此外它们在 $u=0$、$v=0$ 的完整行列及一阶行列均为零。

这是原两失败在同一实际 norm2 核中的明确结果。
特别 (23) 的测试域是
$$
\{\text{至少一个原输入 unit},\
  v_p(a+b_1+c)=v_p(a-b_1+k+e)=1\},
$$
并非“两输入 unit”或“两个输出 unit”代替后的另一个域。
其余输入的所有深度、相消与相加均留在积分中。

## 7. 可与 R399 联立的范围

本篇两个输出与 R404 的双变量 Hadamard 来源具有同一
$\operatorname{diag}(34,72)$ 原 Gram，但来源恒等式不同。
(8) 来自已付的 $A_8$ norm2；R404 的四个 active sigma
变换必须保持自己的全部输入和域。

在本篇，$Y$-only 或 $R$-only 的有界测试可以直接用于
(13)、(18) 的全联合。这确实给两目标的合法中央返回。
如果再施加原五输入某个叶条件，需要先将其送过
$\mathsf P_R$ 和两条 core：
该条件可能依赖三个未观测输入，不能由 (17) 的可逆性删除。

R399 的两移动单位管也是实际依赖输入的域。
它们与 (9) 的五输入接口可继续逐条件相交；
本文没有把它们当成只依赖 $(Y,R)$ 的矩形，
也没有从 (26) 推出每个单独相加 carry 为零。
未知 $J'_G,J'_Q$ 在 (19)、(24)、(25) 中的位置全部明确。

## 8. 同一原双输出的共同正则化

本节支付的是**相同原 $(Y,R)$ 坐标**的全部环带，包含每个混合
来源的 core；不要求把任何单个 unit 补域赋零。

先考虑任意实际有界联合 $\mathcal F$，其全函数确实属于原
$\mathcal S_{34}\boxtimes\mathcal S_{72}$。
取两个输出的 $\mu_6$ 型零部分；这对 principal 测试合法。
R399 的原整有限算子给
$$
\mathcal F|_{Y\in p}=-\lambda[\kappa_Y]_*\mathcal F,\qquad
\mathcal F|_{R\in p}=\lambda[\kappa_R]_*\mathcal K_R\mathcal F,
\quad\mathcal K_R^2=1.
\tag{27}
$$
$\mathcal K=N_7^9$ 的完整十三维矩阵已经付清；
其分母最小公倍数准确为 $2^{17}3^{17}$，故这里是原整算子。
置 $\mathcal F_\pm=(1\pm\mathcal K_R)\mathcal F/2$，
记其单位矩形 Mellin 为 $\mathscr J_\pm(u,v)$。

在 $|t_1|_p,|t_2|_p<1$ 中，对两个输出的精确环带作真正收敛和：
$$
\mathscr Z_{\mathcal F}(t_1,t_2;u,v)
=\sum_{n,m\ge0}t_1^nt_2^m
 \int_{\substack{v_p(Y)=n\\v_p(R)=m}}
 \chi_{\ell_1,u}(Y/p^n)\chi_{\ell_2,v}(R/p^m)\,d\mathcal F.
$$
由两个可交换的原 core，
$$
\boxed{
\mathscr Z_{\mathcal F}=
\frac{\mathscr J_+}
 {(1+\lambda t_1U_{\ell_1}(u))(1-\lambda t_2U_{\ell_2}(v))}
+
\frac{\mathscr J_-}
 {(1+\lambda t_1U_{\ell_1}(u))(1+\lambda t_2U_{\ell_2}(v))}.
}
\tag{28}
$$
这先是收敛域中的实际等式，后是唯一解析延拓；没有直接给单位几何和
任意指定一个求和值。

在 principal 中央，$1-\lambda$、$1+\lambda$ 都已证为单位，
所以 (28) 在 $(t_1,t_2,u,v)=(1,1,0,0)$ 的一个原整邻域无极。
两个延拓/取值顺序准确相同。固定非 principal tame 时，
相应中心分母仍非零：若等于零，$\bar\pi_0$ 会等于一个根单位，
与其范数 $p$ 矛盾；但此时不额外声称分母是 $p$ 单位。

因此定义
$\mathscr R_{\mathcal F}(u,v)=\mathscr Z_{\mathcal F}(1,1;u,v)$
得到此同一双轴上的 canonical 正则化。
对这些真实来源间的任何线性、Hadamard 或 Fay **源身份**，
先在收敛域相加，再唯一延拓，身份仍然成立。
这没有把原输入的加法卷积改成 Mellin 乘积。

对于四角，$\Delta_-=\mathcal A,\ \Delta_+=-\mathcal B$，故
$$
\boxed{
\mathscr R_\Delta
=\frac{J_S(u)J_T(v)}
 {(1+\lambda U_1(u))(1+\lambda U_2(v))}
-\frac{J_G(u)J_Q(v)}
 {(1+\lambda U_1(u))(1-\lambda U_2(v))}.
}
\tag{29}
$$
两目标的正则化中央导数分别为 $J'_S/(1+\lambda)$、
$J'_T/(1+\lambda)$，与原失败无损等价。
但质量一角保留准确尺度项：
$$
\widetilde J_G(0)=1,\qquad
\widetilde J_G'(0)=
 \frac{J_G'(0)+2d\lambda\log_p\bar\pi_{17}}{1+\lambda},
\qquad
\widetilde J_Q'(0)=\frac{J_Q'(0)}{1-\lambda}.
\tag{30}
$$

五输入 primitive 条件也与同一个正则化相容。
由 (15)，在收敛域已经有
$$
\boxed{
\mathscr Z_{\Delta^{\rm prim}}
=(1-\lambda^5t_1t_2U_1(u)U_2(v))\mathscr Z_\Delta .
}
\tag{31}
$$
所以可按同一顺序取值。这个因子不是 $(1-\lambda)^5$；
它保留两个输出共同深一层的实际条件。
(31) 不要求 $1-\lambda^5$ 为单位，也不把该因子删掉。

这里有一个必须区分的全局覆盖。R404 的两个单独 mixed 来源
仅已证明在共同双 $[2]$ 后属于
$\mathcal S_{136}\boxtimes\mathcal S_{288}$，
不能仅由 Gram 相似就逐项套用 (27) 的十三维算子。
它们的和已是原 $\nu_S\otimes\nu_T$。
单项的相应覆盖上有限 Heisenberg 算子、真实锚及其延拓须另付；
本节不以 $\mu_6$ 平均冒称这些半周期块自动下降。

同样，若要把 (28) 换到 $Y,Z$ 或其他重叠线性超平面，
必须先比较那些真实深域。R399 的 (25)–(30) 给的恰是
两个移动管及其完整中央尾，未证明其交叠误差为零。
本节的共同双轴正则化因此解决了四角同核的次序问题，
尚未把不同输入叶的所有 unit 补集消掉。

## 9. Q 的实际身份范围与证书

$Q$ 的 $+\lambda$ core 来自 R399 全 $13\times13$ 矩阵的
$N_7^9Q=Q$，不是凭其质量猜测。
它本身不是该原 CM7 算子的单线：
在 $b=1$，$Q=\sigma^{72}q(X)$ 的 $q$ 次数为十，
而真实 $N_7Q$ 的 $X^{11}$ 系数准确是
$$-\frac1{288}-\frac{\omega}{144}=-\frac{\delta}{288}\ne0.$$
故它从 $z^6$ 起，不与从 $z^{12}$ 起的 $Q$ 成比例。
这排除当前同一 CM7 单线认定；不泛称所有可能的新坏点
Schwartz 选择都已被排除。

[check-original-four-corner-normtwo-return.js](../scripts/check-original-four-corner-normtwo-return.js)
对固定多项式、已付反对称式的原系数、真实 Gram、两套 core、返回矩阵
及共同正则化作二十六项精确符号核验。原全函数 norm2 身份引用 R381。没有目标素数扫描，也没有用有限样本推无穷结论。

### 依赖

- [R381](R381-original-antisymmetric-joint-twelve-balls-and-complete-reference-elimination.md)、
  [R387](R387-original-degree-sixteen-quartic-core-and-all-ordinary-moving-balls.md)：
原 $A_8$ norm2、$D,H$ 反对称整条式。
- [R398](R398-e24-actual-polynomial-six-sigma-source-and-original-central-comparison.md)：
新真实 rank-two 来源、周期和原常数。
- [R399](R399-original-two-ranktwo-cross-source-and-overlapping-core-domains.md)：
共同固定 ray、四源、全部 core 及实际 $N_7^9$ 矩阵。
- [R404](R404-two-original-ranktwo-riemann-joint-and-complete-two-axis-central-transport.md)：
  独立的双变量 Hadamard 来源、真实双 $[2]$ 覆盖；本篇不以其
  尚未代入的单叶条件替代 (9)、(22)。

终端不可用，本篇使用仓库授权的小文本 GitHub 集成；API 同步不冒称
`git pull`。2026-11-14 03:13:43 UTC 核对 `main`
`4917a217bdd14f1aa432735aa31ef60166593fdb`，与此前已读
`e4177299da5800620b81f1820d084e643620a839` 比较，两份 README 均无变；
03:11 的两个 README blob 也已独立核对一致。读号交根代理更新 HANDOFF。
