# R544 — 原双 sigma 的完整 S3 两态与三个真实单位环带补偿

日期：2026-11-14。**状态：已证明。**

本篇在 R541 的同一个原六输入上付清一个真正混合原 $Y/W$ 的
两态结构。第三来源 $\eta$ 与 $\rho_0$ 在带绝对 $\mu_6$ 常数的
三阶变换、原输入反射和原输入 $p$ 核下全部闭合。
这给三个实际旋转框架的完整核心，及原 $L=(W-Y)/2$ 单位补域
中三个互不相交环带的准确消元。剩余域和唯一的 $\eta$ 测试差
均明确保留，没有由边际核心推断 whole 联合。

## 1. 同一个原两态和绝对三阶常数

沿用 R539、R541 的原规范
$$
\rho_0=-\nu_\sigma^{\otimes6}/84,\quad
\omega^2+\omega+1=0,\quad\delta=1+2\omega,\quad
\gamma=3+\omega,\quad\alpha=1+3\omega,
$$
$$
\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2,\quad d=p-1,\quad b=17.
\tag{1}
$$
原输入为 $(\xi_1,\xi_2,\xi_3,x,c,d_0)$。
以下全部变换只作用于 $(c,d_0)$，逐个固定前四个原 sigma。

使用 R541 的真实矩阵
$$
H=\frac12\begin{pmatrix}
-1-\omega&-1-2\omega\\
2+\omega&-1-\omega
\end{pmatrix},\qquad
R_c=\begin{pmatrix}-1&0\\0&1\end{pmatrix},
$$
$$
\eta=\omega^2H_*\rho_0,\qquad
\mathsf T=\omega^2H_*.
\tag{2}
$$
物理矩阵满足 $H^3=-I$，不是 $H^3=I$。
由于两个原 sigma 同时变号后来源不变，$H_*^3=I$ 于这些来源；
加上 $\omega^6=1$，实际归一来源算子 $\mathsf T$ 为三阶。

完整身份为
$$
\boxed{
\rho_0+\omega^2H_*\rho_0+\omega H_*^2\rho_0=0,\qquad
(R_c)_*\eta=\rho_0+\eta.
}
\tag{3}
$$
因此在有序基 $(\rho_0,\eta)$ 上，
$$
\boxed{
\mathsf T=
\begin{pmatrix}0&-1\\1&-1\end{pmatrix},
\qquad
\mathsf R=(R_c)_*=
\begin{pmatrix}-1&1\\0&1\end{pmatrix}.
}
\tag{4}
$$
具体 $\mathsf T\eta=-\rho_0-\eta$；
若使用没有前置 $\omega^2$ 的 raw $H_*$，
则 $H_*\eta=-\omega(\rho_0+\eta)$。两者不可混写。

(3) 的全函数证明很短。在两个 raw 变量共同作 $[2]$ 覆盖后，
$\rho_0,\eta,H_*^2\rho_0,(R_c)_*\eta$ 的两个 theta degree 都为 $4$，
交叉为零，半特征相同。同时 $\mu_6$ 型为 $2$。
矩形 jet $0\le i,j\le4$ 只需总阶 $2$ 和 $8$；
两整层分别具有 $b^0,b^1$ 的齐次因子；附证书将全部 CM 有理系数
展开，(3) 的差逐项为零。
degree4 截面不可能有五阶零，故该有限矩形判定完整联合，
不只是边际或数值采样。
$\rho_0$ 的首项是 $cd_0$，而 $\eta$ 有非零 $c^2$ 项，
所以两态确实独立。

直接有
$$
\mathsf T^3=I,\qquad \mathsf R^2=I,\qquad
\mathsf R\mathsf T\mathsf R=\mathsf T^{-1}.
\tag{5}
$$
这是来源上的完整 $S_3$，绝对相位已包含在 (2)。

## 2. 原独立输入 c、d0 的完整核心也在同一两态中

当前 ray 的 $g_\pi\equiv3\pmod8$。
[R506](R506-original-reflection-axis-four-core-and-complete-w-c-rectangles.md)
已付 entire $\mathcal S_4$ 的完整 Heisenberg 中心和
$\sigma(2z)$ 绝对锚：
$$
K_4=R,\qquad\text{实际核心为 }\lambda R.
\tag{6}
$$
上述两态的共同 $[2]$ 覆盖准确在
$\mathcal S_4\otimes\mathcal S_4$ 中；
固定单位倍点 $[2]$ 与普通核心严格交换。
所以 (6) 直接作用于原物理输入 $c,d_0$，而不是把较低 degree
的 scalar 核免费扩到更大空间。

两个来源在 $(c,d_0)$ 同时变号下都固定，故原 $d_0$ 反射与
$c$ 反射在这个整个两态上相同。准确得
$$
\boxed{
\boldsymbol\rho|_{c\in p^r,\ d_0\in p^s}
=\lambda^{r+s}
(P_{c,\kappa^r}P_{d_0,\kappa^s})_*
\,\mathsf R^{\,r+s}\boldsymbol\rho.
}
\tag{7}
$$
这里 $\boldsymbol\rho$ 表示两态空间中的任意来源，
矩阵按 (4) 作用于其系数。
特别两个原输入共同深一层时，整个两态的核心都是
$\lambda^2I$。这也可由 $H$ 保原完整共同深域直接核定。

## 3. 三个真实旋转框架

令
$$
\boxed{
u_j=cH^{-j},\qquad v_j=d_0H^{-j},\qquad j=0,1,2.
}
\tag{8}
$$
它们不是 R536 的隐藏 $C,D_j$；
本篇小写 $u_j,v_j$ 是原两个 sigma 平面的实际线性坐标。
每个框架都是酉整可逆框架，两个 Gram 对角都是 $1$。
准确矩阵为
$$
\binom{u_0}{v_0}=\binom c{d_0},
\quad
\binom{u_1}{v_1}
=\frac12
\begin{pmatrix}\omega&1-\omega\\1+2\omega&\omega\end{pmatrix}
\binom c{d_0},
$$
$$
\binom{u_2}{v_2}
=\frac12
\begin{pmatrix}1+\omega&1+2\omega\\-2-\omega&1+\omega\end{pmatrix}
\binom c{d_0}.
\tag{9}
$$
对 (7) 作真正物理共轭，得到整个两态上的
$$
\mathsf R_j=\mathsf T^j\mathsf R\mathsf T^{-j},
$$
$$
\boxed{
\mathsf R_0=\begin{pmatrix}-1&1\\0&1\end{pmatrix},\quad
\mathsf R_1=\begin{pmatrix}1&0\\1&-1\end{pmatrix},\quad
\mathsf R_2=\begin{pmatrix}0&-1\\-1&0\end{pmatrix}.
}
\tag{10}
$$
它们每个平方为 $I$，且
$$
\boxed{\mathsf R_0+\mathsf R_1+\mathsf R_2=0.}
\tag{11}
$$
令 $P_{u,t}=I+(t-1)\bar u^{\,t}u$ 为原六输入物理缩放；
$Nu=1$，没有额外分母。对每个 $j$ 及所有 $r,s\ge0$，
$$
\boxed{
\boldsymbol\rho|_{u_j\in p^r,\ v_j\in p^s}
=\lambda^{r+s}
(P_{u_j,\kappa^r}P_{v_j,\kappa^s})_*
\mathsf R_j^{\,r+s}\boldsymbol\rho.
}
\tag{12}
$$
四个共有 sigma、任意隐藏条件和测试都完整保留。
(12) 来自已证明两态的共轭，不以拉大覆盖后未经支付的 scalar
核心为前提。

## 4. 实际词域和返回原 S/T 的混合词

(12) 可以逐词使用，但物理条件必须逐步归一。
对一步 $u_j$ 深 $r$，先要求 $u_j(\xi)\in p^r$，
再将实际坐标变为 $P_{u_j,\kappa^{-r}}\xi$。
下一步的条件施加在这个已归一坐标上，不能改成所有原
$u_j$ 同时独立深。

所有来源矩阵仍在 (5) 的六元群内。
例如归一顺序 $(0,1,0,1,0,1)$ 的来源矩阵为
$(\mathsf R_1\mathsf R_0)^3=I$。
设
$$
B=P_{u_0,\kappa}P_{u_1,\kappa},\qquad
\mathcal A=B^3.
$$
相应六步实际域准确为 $\mathcal A\mathcal O^6$，
四个共有输入在 $\mathcal A$ 下不变，且
$$
\boxed{
\rho_0|_{\mathcal A\mathcal O^6}
=\lambda^6\mathcal A_*\rho_0.
}
\tag{13}
$$
它不是各个 raw 轴独立深的矩形。
在实际两维块上
$$
\det B=\kappa^2,\qquad
\operatorname{tr}B=\frac{1+6\kappa+\kappa^2}{4},
$$
$$
\det\mathcal A=\kappa^6,\qquad
\operatorname{tr}\mathcal A
=(\operatorname{tr}B)^3-3\kappa^2\operatorname{tr}B
\equiv\frac1{64}\pmod p.
\tag{14}
$$
所以它也不能认成两个原输入的共同标量缩放。

令 $q=\mathfrak q_{n,p}$ 为 R536 的完整测试。
用准确转置
$$
q_{\mathcal A}=q\circ\mathcal A^{-1},\quad
Y_{\mathcal A}=Y\circ\mathcal A^{-1},\quad
W_{\mathcal A}=W\circ\mathcal A^{-1},
$$
得到
$$
\boxed{
\begin{aligned}
\int_{\substack{\mathcal A\mathcal O^6\\Y_{\mathcal A}\ {\rm unit}}}
 \langle Y_{\mathcal A}\rangle^{du}q_{\mathcal A}\,d\rho_0
 &=\lambda^6\beta^nJ_S(u),\\
\int_{\substack{\mathcal A\mathcal O^6\\W_{\mathcal A}\ {\rm unit}}}
 \langle W_{\mathcal A}\rangle^{du}q_{\mathcal A}\,d\rho_0
 &=6\delta\lambda^6\beta^nJ_T(u).
\end{aligned}}
\tag{15}
$$
同样可迭代 $\mathcal A^k$。
R536 的原零质量非零管和 R539 的放大管均可按这个同一矩阵
完整运输；其原补域也一起运输。
本篇不把 $q_{\mathcal A}$ 换回未移动的 $q$：
$C$ 虽被固定，$F,G_{\rm hid}$ 的 $M$ 分量一般改变。

## 5. 三个互不相交环带都在原 L 单位补域内

设
$$
\mathcal B_j=\{u_j\in p,\ v_j\ {\rm unit}\}.
\tag{16}
$$
任意两行 $u_i,u_j$ 的行列式范数都为 $3/4$；
因此当前 $p>7$ 时，若两者都深，则 $(c,d_0)$ 都深。
所以三个 $\mathcal B_j$ 互不相交。

原
$$
L=\alpha c+d_0=(W-Y)/2
$$
在三个框架中的准确表达是
$$
\boxed{
L=\alpha u_0+v_0
=2u_1+2v_1
=u_2+\bar\alpha v_2.
}
\tag{17}
$$
三个 $v_j$ 系数 $1,2,\bar\alpha$ 都是单位。
所以
$$
\mathcal B_j\subset\{L\ {\rm unit}\}.
$$
并且准确不交分解为
$$
\boxed{
\{L\ {\rm unit}\}
=\mathcal B_0\ \sqcup\ \mathcal B_1\ \sqcup\ \mathcal B_2
\ \sqcup\ \mathcal V,
\quad
\mathcal V=\{L,u_0,u_1,u_2\ {\rm unit}\}.
}
\tag{18}
$$
$\mathcal V$ 是实际剩余域，并未由有限来源群自动覆盖。

先给任意完整测试的来源身份。
记 $S_\kappa$ 为原 $c,d_0$ 同时缩放 $\kappa$，并令
$P_j=P_{u_j,\kappa}$。由 (12)，
$$
\boxed{
\boldsymbol\rho|_{\mathcal B_j}
=\lambda(P_j)_*(\mathsf R_j\boldsymbol\rho)
-\lambda^2(S_\kappa)_*\boldsymbol\rho.
}
\tag{19}
$$
这是原共同深域的准确减法。若仅将 $u_j$ 归一，则
$$
(P_j^{-1})_*(\boldsymbol\rho|_{\mathcal B_j})
=\lambda\mathsf R_j\boldsymbol\rho
-\lambda^2(P_{v_j,\kappa})_*\boldsymbol\rho.
\tag{20}
$$
利用 (11)，三个实际归一环带的和消掉两态矩阵：
$$
\boxed{
\sum_{j=0}^2(P_j^{-1})_*
 (\boldsymbol\rho|_{\mathcal B_j})
=-\lambda^2\sum_{j=0}^2(P_{v_j,\kappa})_*\boldsymbol\rho.
}
\tag{21}
$$
右端仍保三个不同物理缩放，不能认成三倍同一个来源测试。

## 6. 与 R541 原两中央的同一个单位差准确联立

令
$$
\begin{aligned}
f(\xi)=1_{\{L\ {\rm unit}\}}q(\xi)\bigl(
&1_{\{Y\ {\rm unit}\}}\,d\log\langle Y\rangle\\
-&1_{\{W\ {\rm unit}\}}\,d\log\langle W\rangle\bigr),
\end{aligned}
\tag{22}
$$
并记 $\Phi_j=f\circ P_j$。
所有原 cubic carry、$\kappa^{-n}$ 和完整 $\lambda,\kappa$
系数都包含在 $q$ 中。

由于 $L(S_\kappa\xi)\in p$，在 (19) 中
$f\circ S_\kappa=0$ 严格成立，故共同深项在这里确实消去。
(10)、(18) 因此给
$$
\boxed{
\int f\,d\rho_0
=\lambda\int(\Phi_1-\Phi_0)\,d\rho_0
+\lambda\int(\Phi_1-\Phi_2)\,d\eta
+\int_{\mathcal V}f\,d\rho_0.
}
\tag{23}
$$
辅助来源只剩一个明确的实际测试差，三个环带没有被遗漏。

每个 $\Phi_j$ 的原 $L$ 单位条件准确变为 $v_j$ 单位，因为
$$
L(P_j\xi)=a_j\kappa u_j+b_jv_j,\qquad
b_j\in\{1,2,\bar\alpha\}.
$$
但它的两个 Mellin 单位条件仍为
$Y(P_j\xi)$ 和 $W(P_j\xi)$ 各自单位。
例如写共同四输入为
$$
A=\delta\xi_1+2\delta\xi_2+\gamma\xi_3+\bar\gamma x,
$$
则 $Y(P_j\xi)=A+\kappa y_ju_j+\tilde y_jv_j$，
$W(P_j\xi)=A+\kappa w_ju_j+\tilde w_jv_j$。
全部系数在附 JSON 中；三个 $Y$ 对分别为
$$
(1,2),\qquad
\left(\frac{3+\omega}{2},-\frac{3+4\omega}{2}\right),\qquad
\left(-\frac{2+5\omega}{2},-\frac{1+\omega}{2}\right).
\tag{24}
$$
这些实际单位条件不可相互代换。

现在用 R541 的真实一层 $L$ 核。
记
$$
Y_\kappa^{\mathcal G}
=A+\kappa a(\gamma c+d_0)+b_M(c-\bar\gamma d_0),
$$
$$
W_\kappa^{\mathcal G}
=A+\kappa a_W(\gamma c+d_0)+b_M(c-\bar\gamma d_0),
$$
其中 $a=-3\omega/8,\ a_W=a+2,\ b_M=-(1+6\omega)/8$。
它们之差为 $2\kappa(\gamma c+d_0)$，单位域准确相同，
记为 $\mathcal U_\kappa$。令
$$
\mathcal J=
\int_{\mathcal U_\kappa}
d\log\!\left(\frac{Y_\kappa^{\mathcal G}}
                  {W_\kappa^{\mathcal G}}\right)
(q\circ\mathcal G)\,d\rho_0.
\tag{25}
$$
这里 $\mathcal G$ 是 R541 的固定物理矩阵，原两条来源和全部
测试已在该文付清。

在原算术条件 $J'_S=J'_T=0$ 下，R541 准确给
$\int f\,d\rho_0=-\beta\mathcal J=\lambda\mathcal J$。
与 (23) 合并，即得真正同域联立式
$$
\boxed{
\int_{\mathcal V}f\,d\rho_0
=\lambda\left\{
\mathcal J-\int(\Phi_1-\Phi_0)\,d\rho_0
-\int(\Phi_1-\Phi_2)\,d\eta
\right\}.
}
\tag{26}
$$
(25) 的 log 比属于 $p\mathcal O$。
(26) 的其他行保所有实际质量和 log 常数；
不因它们来自正矩提取而假设每个新限制域的质量为零。

R546 可对最后的 $\eta$ 行使用同一五伴随的完整
$S,S_{\rm new},H_{\rm ref}$ 投影，但 $\Phi_1,\Phi_2$ 混合
第一 $Y$ 与伴随，仍须逐 CM 分支完整转置。
本篇没有将整个 $\eta$ 行或参考导数赋成零，也不删除外谱。
等价地，若只想保原六 sigma 来源，最后一项准确为
$$
\int(\Phi_1-\Phi_2)\,d\eta
=\omega^2\int(\Phi_1-\Phi_2)\circ H\,d\rho_0,
\tag{27}
$$
其第一权和所有 cut 一并改变。

## 7. 同一 L-odd 来源的完整负矩单位接口

此节给后续混合负矩可直接使用的原来源，不引入新算术曲线。
在 R539 的两个真正输出中，令
$$
F_{\rm odd}(l,m)=F_0(l,m)-F_0(-l,m).
$$
它分别在 $l,m$ 下为奇函数，两个完整边际都为零。
记
$$
f_j(z)=\sigma(z)^8y(z)\wp(z)^j,\qquad j=0,1,2,
\quad y=\wp'/2.
$$
相应 odd degree8 空间的基就是这三个函数。
同时型 $2$ 只允许 $f_0\otimes f_1,f_1\otimes f_0,
f_2\otimes f_2$，由三个三角首系数准确得到
$$
\boxed{
F_{\rm odd}
=-12 f_2\otimes f_2
+48b\omega^2 f_0\otimes f_1
+48b\omega f_1\otimes f_0.
}
\tag{28}
$$
附证书核定全部系数。
由于 $f_2(z)=-z+O(z^7)$，准确有
$$
\boxed{
\partial_lF_{\rm odd}(0,m)=12f_2(m),\qquad
\partial_l\partial_mF_{\rm odd}(0,0)=-12.
}
\tag{29}
$$
R539 的 $K_8=-R(2P_2-I)$ 在 odd 子空间上为 $-I$，
所以该整个联合的两个实际核心都是 $\beta$。

任意 $L$ 深域或环带均在 $L\mapsto-L$ 下稳定。
其 $L$ 条件质量作为剩余全部五输入的测度严格为零。
故任何不依赖 $L$ 的完整测试都可保留这个零质量；
R536 的 $q(C,F,G_{\rm hid})$ 正属于此范围。

令 $\nu_{\rm odd}$ 为这两个输出的原整测度。
完整双单位首矩为
$$
\int_{L,M\ {\rm unit}}LM\,d\nu_{\rm odd}
=-12\Omega^2(1-\beta\kappa)^2.
$$
由于 $L,M$ 的单位值属于 $\mathbb Z_p^\times$，
在当前普通处逐点用 Fermat 同余即得
$$
\boxed{
\int_{L,M\ {\rm unit}}
L^{-(p-2)}M^{-(p-2)}\,d\nu_{\rm odd}
\equiv-12\Omega^2(1-\beta\kappa)^2\pmod p.
}
\tag{30}
$$
右边是单位。

若保持原四个共有 sigma，并在它们各自单位域上乘
$\xi_1\xi_2\xi_3x$，同一个完整六输入来源
$\rho_0-(\mathcal R_L)_*\rho_0$（此处 $\mathcal R_L$ 是 R541 的
$L$ 反射）准确给
$$
\boxed{
\int_{\substack{\xi_1,\xi_2,\xi_3,x,L,M\ {\rm unit}}}
 \xi_1\xi_2\xi_3x\,
 L^{-(p-2)}M^{-(p-2)}
\,d\{\rho_0-(\mathcal R_L)_*\rho_0\}
\equiv
\frac{\Omega^6}{7}(1-\beta\kappa)^6\pmod p.
}
\tag{31}
$$
原 $-1/84$ 和两个输出的 $-12$ 已包含。
这是完整原联合上的负矩单位，尚不是原中央非零；
把它接到中央仍须支付相应的实际第一权和补域。

## 8. 已完成的连接与保留项

(3)–(12) 付清同一原两态的 $S_3$、原输入核心及三个实际框架；
(19)–(26) 将原 $L$ 单位补域准确压成三个真环带、
一个明确的 $\eta$ 测试差和唯一剩余共同单位域 $\mathcal V$。
(13)–(15) 给真正混合原第一权且返回原 S/T 的词域；
(30)–(31) 给同一原来源的完整负矩单位接口。

$\mathcal V$、$\eta$ 的混合测试差和 (25) 的公共单位域均完整
保留。已知的三个算术中央条件只能用在已支付的对应投影及其
真实域上。主目标尚未由这些局部单位或有限来源矩阵完成。

## 精确证书与依赖

- [check-r544-original-s3-and-unit-annulus-carry.js](../scripts/check-r544-original-s3-and-unit-annulus-carry.js)
- [全 theta jet、三个物理框架和六步词 JSON](../scripts/check-r544-original-s3-and-unit-annulus-carry.json)
- [R541：完整三支双 sigma 与实际 cut](R541-original-degree8-second-state-and-exact-sigma-transport.md)
- [R539：entire degree8 核](R539-original-degree8-mixed-st-core-and-amplified-central-domain.md)
- [R506：entire degree4 的中心和绝对锚](R506-original-reflection-axis-four-core-and-complete-w-c-rectangles.md)
- [R546：同一第三 sigma 来源的完整五伴随 CM 转移](R546-original-third-sigma-full-five-companion-cm-transfer.md)

证书已经在当前 JavaScript 环境以 BigInt 有理 CM 算术精确执行。
它核定有限 jet 判定的每一项、所有来源矩阵与物理框架、三个
行列式范数以及六步实际词的完整迹和行列式。
