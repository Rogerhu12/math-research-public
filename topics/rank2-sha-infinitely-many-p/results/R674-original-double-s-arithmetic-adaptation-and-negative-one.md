# R674 — 同一测试的双 S 算术适配、保非零负一系数与六步真返回

日期：2026-11-15。**状态：已证明。**

本篇在原 R594 的十一维整核内选择一个明确区别于旧测试的
$q_N^\dagger$。固定 N 后它独立于观察深度 n。
这个同一个测试同时满足：

- 两个原 S 共同来源的深度常数项分别是原 S 的单位倍；
- 原 R665 二阶系数的整规范准确为一，故其已知负一深支保留；
- 原九条补偿约束与整个 $\pi_4$ 算术返回保持不变。

两条共同来源的其余六个深度系数全部保留。
由此得到六步完整来源返回，准确提取原 S；
同一个六步算子作用于原 T 混合深差，仍给准确非零值层。
全文保原浅门、原 Y 外部和 T 的两个移动单位 cut，
不将两个不同实际补偿域相认。

## 1. 一个固定 N 的实际共同来源问题

沿用 R594、R664–R670 的全部原 ray、周期及坏集。
$$
b=17,\quad\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2,\quad\Omega\in\mathcal O^\times,
\qquad N\in4\mathbf Z_{\ge1}.
$$
保原
$$
\mu_0=\nu_4\otimes\nu_\sigma(c)\otimes\nu_\sigma(d),\qquad
Q=c+2d,\quad L=2c-d,
$$
$$
Y_0=A+Q,\quad Y_1=A+L,\quad
\mathcal E=5A-29(Q+L),\qquad\epsilon_i=(-1)^i .
$$
测试的 i=1 支始终是同一个原整数旋转
$q_1=q_0\circ\mathsf J^{-1}$，不是独立选择第二个多项式。

R669 的完整来源式使用
$$
u=\kappa^N,\qquad t=\kappa^{n-N},
$$
并将第 i 个原 S 共同来源写成
$$
\boxed{
\mathcal A_{\mathfrak C_{i;N,n}}(z)
=\epsilon_i\lambda^{2n+2N}\,
                 \mathscr S_{i,N,p}(t;z),
\qquad \deg_t\mathscr S_{i,N,p}\le6.
}
\tag{1}
$$
对每个 t，右边属于整个 standard even $\mathcal S_{34}$ 的型零空间。
固定旧多项式时，它也按 R669 对 u 至多六次；本篇随后选择的
多项式依 N，因此不免费继承 N 方向递推。

记实际冻结来源
$$
\mathscr U_{i,N,p}(P)=\mathscr S_{i,N,p}(0;\cdot).
$$
这是同一有限多项式的 t 常数项，不是把一个真实浅域赋零。
下面在这两条**完整**来源上解一个实际整线性问题。

原 S 的准确规范为
$$
\boxed{
S=\frac{\sigma^{34}x^2}{7}
 (x^3+b)(x^3-8b)(7x^6-4bx^3+16b^2).
}
\tag{2}
$$
在 R669 的完整六基
$\Xi_j=\sigma^{34}x^{17-3j}$ 上，其系数是
$$
s=(0,\ 1,\ -53b/7,\ -12b^2/7,\ -80b^3/7,\ -128b^4/7).
\tag{3}
$$
没有改变原首项 $S(z)=z^6+\cdots$、Fourier 变量或周期。

## 2. 全部 C 第六矩保留的原六次计算

本篇的权次数为六，不能沿用 R670 四次权时只取 C 质量的简化。
R590/R594 的完整分离为
$$
\mu_0=\nu_{B_C}\otimes\nu_{\rm flat,5},
$$
$$
\nu_{\rm flat,5}=\frac1{42}
(\nu_{f_1}(Z_f)\otimes\nu_\Sigma(Q_f)
-\nu_{f_3}(Z_f)\otimes\nu_\Theta(Q_f))
\otimes\nu_\sigma(r_f)\otimes\nu_\sigma(c)\otimes\nu_\sigma(d),
\tag{4}
$$
且
$$
m_{B_C}(0)=1,\quad m_{B_C}(1)=\cdots=m_{B_C}(5)=0,\quad
\boxed{m_{B_C}(6)=-8b\Omega^6.}
\tag{5}
$$
这里 $(Z_f,Q_f,r_f)$ 是原四输入忘 C 后的三个真实坐标，
不同于后两个 sigma 的 Q/L。

沿用 R665/R670 的实际 $D_*,E_\perp,G_\perp,G_{00}$，
以及
$$
\epsilon_D=-263/143,\qquad\gamma_D=(-789+526\omega)/143,
$$
$$
e_0=-(170+117\omega)/9135,\qquad
e_1=-(170+291\omega)/9135 .
$$
从 R666 的全部条件来源或 R669 的整个合成式直接相加，
冻结来源有以下完全等价的六次权表达。
置 $H_i=D_*+e_i\mathcal E$，则
$$
\boxed{
\begin{aligned}
\mathscr U_{i,N,p}(P)(z)
=\frac{\epsilon_i}{b\Omega^6}\int e^{Y_i z/\Omega}\Big[
&\widehat P(H_i,E_\perp+\epsilon_DuD_*+ue_i\mathcal E,
             G_\perp+\gamma_DuD_*+ug e_i\mathcal E)\\
-\eta\lambda\,&\widehat P(H_i,\kappa E_\perp+\epsilon_DuD_*+ue_i\mathcal E,
 G_{00}+\kappa(G_\perp-G_{00})+\gamma_DuD_*+ug e_i\mathcal E)
\Big]\,d\mu_0 ,
\end{aligned}}
\tag{6}
$$
其中 $g=3-2\omega$，$\eta=\pm1$ 是原实际 C 伴随 whole 标量。
第二行是完整 C 单位补项，不删除，也不猜号。
原 $\widehat P$ 保全部 $u_j=(1+\lambda\kappa^j)^{-1}$。

证明 (6) 可对 $\widehat P$ 沿
$\partial_D+u\partial_E+ug\partial_G$ 作完整有限 Taylor 展开。
第 k 项正是 R666 的 $F_k/k!$ 及 R669 的第 k 次物理矩；
$\mathcal E$ 与 $D_*,C^\perp$ 正交，所有表示使用同一输入。
因而只在原第一自变量增加 $e_i\mathcal E$，
第二、三自变量分别增加 $ue_i\mathcal E,ug e_i\mathcal E$。
$\epsilon_i$ 是 i=1 来源的真实整数旋转号。
没有交换不相容的限制，也没有忽略其余伴随。

为了准确计算 (6) 模 p，令形式 $\kappa=u=0$。
此时只需原全次数至多 $6+30=36$ 的矩。
对于形式伴随变量 $(d,e,g_1)$，C 分量准确为
$$
\ell_C=-d+\frac{1596}{143}e+
             \frac{-789+526\omega}{143}g_1 .
$$
因 $Y_i\perp C$，C 因子对整条 Y 生成变量没有依赖。
故在伴随次数至多六时，它准确为
$$
\boxed{1-\frac b{90}\ell_C^6\pmod{(d,e,g_1)^7}.}
\tag{7}
$$
附脚本将 (7) 完整乘到 (4) 的五输入生成函数上。
其余各生成变量取真实行
$(Y_i,H_i,E_\perp,G_\perp)$，并保 i=1 的 $\epsilon_i=-1$。
读取伴随六次和 Y 次数 $0,6,\ldots,30$ 给整个 S34 来源，
并非仅某个局部阶数的近似。

脚本还从 (4) 无权的整个 Y 边际独立恢复 (2) 的六个原系数；
因此 (3) 的来源常数和周期没有靠猜测确定。

## 3. 原十一维核的成对矩阵与真正的第十三行

仍用 R667 的实际整投影
$$
\Pi_p=I_{20}-B(\tau)(A_pB(\tau))^{-1}A_p,\qquad
\tau=(1+\lambda)^{-1}.
$$
选择原二十列的零起编号
$$
\boxed{\mathcal I=(0,1,2,3,4,13,15,16,17,18,19),\qquad
v_{p,j}=\Pi_pe_j,\quad j\in\mathcal I.}
\tag{8}
$$
它们是同一个原九行核中的向量。

对 S34 来源 F，使用整的六行
$$
\mathcal T_r(F)=b^{1-r}[z^{6r}]F,\qquad0\le r\le5 .
\tag{9}
$$
R669 已付这六阶准确决定完整来源；到 $\Xi_j$ 是单位三角恢复。
b 在当前处为单位，故 (9) 没有改变整秩。

第十三行不是一个新裸矩。
它是 R665/R667 的同一个实际二阶量
$$
\boxed{
\mathfrak j_{N,p}(P)=
\frac{2b\Omega^2}{\ell_0^2}
 \lambda^{-N}\kappa^{2N}J_N(P),\qquad
\ell_0=-3\omega/5.
}
\tag{10}
$$
R670 的完整公式使这是一条整的实际来源行，
包含全部 $\lambda,\kappa,u$ 和 C 单位补项。

现在定义实际 $13\times13$ 矩阵 $\mathbb A_{N,p}$。
前十一列是同一个 $v_{p,j}$ 的：
$$
(\mathcal T_r\mathscr U_{0,N,p}(v_{p,j}))_{r=0}^5,\quad
(\mathcal T_r\mathscr U_{1,N,p}(v_{p,j}))_{r=0}^5,\quad
\mathfrak j_{N,p}(v_{p,j}).
$$
最后两列分别是
$$
-(\mathcal T(S),0,0)^t,\qquad
-(0,\mathcal T(S),0)^t .
\tag{11}
$$
这里两条 S 目标共用原周期；最后一行的两个 S 系数均为零。

这一个矩阵同时控制两个完整 S 来源与同一个 J_N，
没有独立更换第二个 gate、第二个测试或第三条来源。

## 4. 固定非零证书与完整实际整逆

附两个矩阵文件保存特征零的完整 $12\times20$ 行
$$
J_\eta(\tau)=J_{\eta,+}+\tau J_{\eta,0},\qquad \eta=\pm1 .
\tag{12}
$$
每行由 (6)–(7) 的原矩直接给出。
具体对每个原六次列 P，令 a 为完整矩、a0 为置 E=0 的矩，
b0 为再置 $G=G_{00}$ 的矩，则整单位补项准确给
$$
j_\eta(\tau)=(a-a_0-\eta b_0)+\tau(a_0+\eta b_0).
\tag{13}
$$
第十三行使用 R667 的同一四次表达，绝不以一个无权质量替代。

模 p，原核列为
$$
v_j(\tau)=
e_j-\frac{B_0+\tau B_1}{\tau-1}(A_++\tau A_0)e_j .
\tag{14}
$$
因此 $\mathbb A_{N,p}$ 的余式是一个完全显示的固定
$\overline{\mathbb A}_\eta(\tau)$。
其前十一列分母为 $\tau-1$，分子次数至多三；
两个 S 列固定。
乘去前十一列的分母后，其行列式是次数至多33的固定
$K[\tau]$ 多项式。

下面给一个精确有限的**特征零非零证书**，而非普通素数采样。
在辅助域
$$
\mathbf F_{1009},\qquad\omega=374,\qquad\tau=2
$$
中，所有原固定分母均为单位，且
$374^2+374+1\equiv0\bmod1009$。
脚本核过 1009 为素数，保存两个完整十三乘十三矩阵。
其行列式准确为
$$
\boxed{\det\overline{\mathbb A}_+(2)=856,\qquad
       \det\overline{\mathbb A}_-(2)=729\quad\bmod1009.}
\tag{15}
$$
所以两个固定特征零行列式多项式都不恒等为零。
此辅助地点不被当作当前 ray 的研究素数，也不据此赋任何中央非零。

前十二行在原核上的秩因而恰为十一。
其唯一左行可按十二个带号子式定义；
附证书还保存相同辅助规范下该左行与原目标、仿射项的准确配对：
$$
\begin{array}{c|ccc}
\eta&\ell(S,0)&\ell(0,S)&\ell(\text{原固定共同源})\\ \hline
+1&918&760&115\\
-1&1005&225&685
\end{array}\pmod{1009}.
\tag{16}
$$
因此两个原 S 目标和原仿射项都被实际唯一兼容行看见；
没有由“十三个未知量”猜测可解。

给定原固定多项式 $P_p^{\rm old}$，
以实际矩阵解
$$
\boxed{
\mathbb A_{N,p}
\begin{pmatrix}a\\c_0\\c_1\end{pmatrix}
=
\begin{pmatrix}
-\mathcal T\mathscr U_{0,N,p}(P_p^{\rm old})\\
-\mathcal T\mathscr U_{1,N,p}(P_p^{\rm old})\\
1-\mathfrak j_{N,p}(P_p^{\rm old})
\end{pmatrix}.
}
\tag{17}
$$
辅助证书的两个解中，最后两项分别为
$$
\boxed{(c_0,c_1)=(398,158)\quad(\eta=+1),\qquad
       (c_0,c_1)=(796,506)\quad(\eta=-1)
       \pmod{1009}.}
\tag{18}
$$
所以两个 c 的固定余式分子也都不恒等为零。

包含全部已保存固定系数分母的一个整数为
$$
D_{674}=
72845862751585351656416832390010661870857547661088706607157048996336519369984849638224227842000154817406102247778250000000 .
\tag{19}
$$
保原全部 ray 和坏集，再删其有限素因子。
将 (15)、(18) 所定的有限组固定有理式代
$\tau=T/(T-1)$ 并清分母，对其非零分子乘积使用
[固定 CM 多项式单位密度引理](../notes/2026-11-14-fixed-cm-polynomial-unit-density.md)。

在同一原 ray 的相对密度一子族，实际
$\mathbb A_{N,p}$ 有整逆，两个实际 c 都为单位，
并且
$$
\boxed{
\mathbb A_{N,p}\in{\rm GL}_{13}(\mathcal O),\qquad
c_0,c_1\in\mathcal O^\times
\quad\text{对全部 }N\in4\mathbf Z_{\ge1}\text{ 同时成立}.}
\tag{20}
$$
因为实际 $\kappa,u=\kappa^N$ 模 p 都为零，余式与 N 无关。
(17) 使用的是完整实际矩阵，不把余式的系数当作实际解。
这支付所有 $\lambda,\kappa,\kappa^N$ 修正；
没有把 p 依赖的负矩用于固定多项式密度论证。

## 5. 同一原算术测试族中的新固定 N 测试

由 (17) 定义
$$
v_{N,p}^\dagger=\sum_{j\in\mathcal I}a_jv_{p,j},\qquad
\boxed{q_N^\dagger=q_N+\delta q_{v_{N,p}^\dagger,N}.}
\tag{21}
$$
这里旧 $q_N$ 及所有旧结论原样保留；
$q_N^\dagger$ 是另一个明确命名的同家族测试。

因为 $v_{N,p}^\dagger\in\ker A_p$，原九条约束、
原真实网格首项和整个 $\pi_4$ 推前保持。
两个旋转支仍由同一个 $q_N^\dagger$ 运输，故两个 S/T 总行
仍严格是 R664 的原行，没有新增算术零假设。

由 (17) 及整个 S34 的六阶恢复，
$$
\boxed{
\mathscr U_{0,N,p}(q_N^\dagger)=c_0S,\qquad
\mathscr U_{1,N,p}(q_N^\dagger)=c_1S,\qquad
\mathfrak j_{N,p}(q_N^\dagger)=1 .
}
\tag{22}
$$
这些是两个完整来源和同一个实际系数的准确身份。
c_i 只是来源的乘法系数，不是物理 Y 变量缩放；
因此没有漏掉一个 $\log c_i$ 的尺度项。

由 (10)，
$$
\boxed{
J_N^\dagger=
\frac{\ell_0^2}{2b\Omega^2}\lambda^N\kappa^{-2N}\ne0 .
}
\tag{23}
$$
与 R670 取消 $\Lambda_2$ 的另一测试不同，
本篇明确保留并定标了这条负一接口。

固定 N 后，(17) 不含 n；
所以 $q_N^\dagger$ 可用于整个 n 序列及其真深度过滤。
它依 N，不能直接使用 R666/R669 针对同一个固定多项式
所给的 N 方向递推。

## 6. 两个共同 S 行的六步完整算术返回

R669 对任何同家族六次多项式都给 t 次数至多六。
所以对这个固定 N 的同一测试，准确有
$$
\boxed{
\mathscr S_{i,N,p}^\dagger(t)
=c_iS+\sum_{a=1}^6 t^a T_{i,a,N,p},
\qquad T_{i,a,N,p}\in\mathcal S_{34}^{\rm type\,0}.
}
\tag{24}
$$
这六条高系数完整保留，未给它们的中央导数赋零。

令 $\mathsf T$ 作用于真实序列 n→n+1，置
$$
\mathcal P_6(\mathsf T)
=\prod_{a=1}^6(\mathsf T-\lambda^2\kappa^a),\qquad
U_6=\prod_{a=1}^6(1-\kappa^a),\quad
V_6=\prod_{a=1}^6(1-\lambda\kappa^a).
$$
$U_6,V_6$ 都是单位。
对同一个原 unit Mellin 变量 w，(1)、(24) 严格给
$$
\boxed{
\mathcal P_6(\mathsf T)\,
 \mathcal C_{i,n}^{S,\dagger}(w)
=\epsilon_i c_i\lambda^{2n+2N+12}U_6\,J_S(w),
\qquad n\ge N .
}
\tag{25}
$$
这是六步完整来源返回，不是先给六个新观察分别赋零。
由于 c_i 和所有显示系数均单位，它确实提取同一个原 S 行。

仍令 $\mathcal L_{i,n}^{S,\dagger}$ 为完整 E 浅域之和
（包括第零层），$\mathcal O_{i,n}^{S,\dagger}$ 为原 Y 外部。
完整总行是 $\epsilon_i\lambda^{n+N}J_S$。
因此
$$
\boxed{
\begin{aligned}
\mathcal P_6(\mathsf T)
  (\mathcal O_{i,n}^{S,\dagger}+
   \mathcal L_{i,n}^{S,\dagger})(w)
=\epsilon_i\bigl[
 \lambda^{n+N+6}V_6
-c_i\lambda^{2n+2N+12}U_6\bigr]J_S(w).
\end{aligned}}
\tag{26}
$$
每一个移位项都使用它自己的原真实域和同一个固定
$q_N^\dagger$；没有把这些不同域当作一个不动的 cut。

若原 $J'_S(0)=0$，(25)、(26) 的中央导数都准确为零。
质量由原 $J_S(0)=0$ 同理处理；
其余 Mellin 权没有被错误地整体设为零。

## 7. 同一个过滤器下，原负一深差仍准确非零

对同一 $q_N^\dagger$，R665 的全角型因子式仍准确成立：
$$
\Delta_{N,n}^\dagger
=2\beta^n\kappa^{2n}J_N^\dagger\,\mathscr H_p(\kappa^n).
\tag{27}
$$
这是原混合观察 $b_LL\pm b_YQ$、原冻结门和真实 L 深域，
不是 (25) 的双 Y 共同域。
$\mathscr H_p$ 的所有其余负矩、原 log 分母与单位限制仍按原式保留。

R655 已付同一个
$I_{\Sigma_5,-1}\ne0$，R665 的完整尾界和 (23) 给
$$
\boxed{
\Delta_{N,n}^\dagger
=36\ell_0^2\Omega(b_L/b_Y)
 \lambda^N\beta^n\kappa^{3n-2N}I_{\Sigma_5,-1}
+p^{5n-2N}\mathcal O.
}
\tag{28}
$$
因此当 $n\ge N$ 且 $2n>v_p(I_{\Sigma_5,-1})$，其赋值为
$3n-2N+v_p(I_{\Sigma_5,-1})$。

现在用 (25) 的**同一个**六步算子。
首项的真实移位特征为 $\beta\kappa^3$，所以其乘数为
$$
\prod_{a=1}^6(\beta\kappa^3-\lambda^2\kappa^a)
=\kappa^{15}U_p,
$$
$$
\boxed{
U_p=(\beta\kappa^2-\lambda^2)
(\beta\kappa-\lambda^2)(\beta-\lambda^2)
(\beta-\lambda^2\kappa)
(\beta-\lambda^2\kappa^2)
(\beta-\lambda^2\kappa^3).
}
\tag{29}
$$
原 R410 已给 $1+\lambda$ 单位，而
$\beta-\lambda^2=-\lambda(1+\lambda)$。
其余因子也都为单位；准确有
$U_p\equiv\lambda^8(1+\lambda)\bmod p$。

(27) 的下一可能模式为 $\beta\kappa^5$，乘数赋值为20；
其后模式的乘数赋值至少21。
保全部原 $1/k$ 分母，R665 的统一界因此给
$$
\boxed{
\begin{aligned}
\mathcal P_6(\mathsf T)\Delta_{N,n}^\dagger
={}&36\ell_0^2\Omega(b_L/b_Y)
 \lambda^N\beta^n\kappa^{3n-2N+15}U_p I_{\Sigma_5,-1}\\
&\quad+p^{5n-2N+20}\mathcal O .
\end{aligned}}
\tag{30}
$$
也可直接逐移位检查尾界：
第 j 次移位的系数赋值至少
$(6-j)(7-j)/2$，故其尾项至少
$5n-2N+5j+(6-j)(7-j)/2$，最小值为 $5n-2N+20$。

所以同一条件下
$$
\boxed{
v_p\!\left(\mathcal P_6(\mathsf T)\Delta_{N,n}^\dagger\right)
=3n-2N+15+v_p(I_{\Sigma_5,-1}).
}
\tag{31}
$$
没有将这个 p 依赖负矩套入固定 CM 多项式引理；
该引理只用于 (15)、(18) 的有限代数系数。

## 8. 仍须完整保留的 T 浅域和原外部

令 $\mathcal E_\pm^\dagger$、$\mathcal R_{N,n}^\dagger$
严格使用 R662/R665 的两个原 T 外部词和原 L 浅补域，
仅将权换为同一个 $q_N^\dagger$。
尤其保 $Q/p^m$ 尺度、两个不同的 $b_LL\pm b_YQ$ 单位 cut
和各自全部 log 质量。

若原 $J'_T(0)=0$，完整关系仍为
$$
\mathcal E_+^\dagger-\mathcal E_-^\dagger+
\mathcal R_{N,n}^\dagger=-\Delta_{N,n}^\dagger .
$$
故
$$
\boxed{
\mathcal P_6(\mathsf T)
(\mathcal E_+^\dagger-\mathcal E_-^\dagger+
 \mathcal R_{N,n}^\dagger)
=-\mathcal P_6(\mathsf T)\Delta_{N,n}^\dagger\ne0,
}
\tag{32}
$$
其准确赋值由 (31) 给出。
外部极限在 n 中是常量，故其准确乘数是
$\prod_{a=1}^6(1-\lambda^2\kappa^a)\in\mathcal O^\times$；
(32) 对该项完整保留这个因子，不能把它省掉。

在原两个中央同时为零的假设下，现有的真实联立是：
(26) 的两条 S 完整补偿经同一算子为零，
而 (32) 的 T 完整补偿经该算子非零。
两者的实际域和观察不同，本文没有证明它们相等。
尚须支付一个把 (32) 的真实 T 补偿接回 (26) 两条 S 补偿
及已控整总行的来源恒等，才能推出中央矛盾。

新增实质是：上述两侧现在使用同一个固定 N、独立于 n 的
合法原算术测试，两个 S 常数来源确已返回原 S，
负一深支又没有被测试适配删掉。
这给一个明确的同过滤器剩余比较，而不是新的无来源负矩池。
原固定曲线、无穷不同 p 的目标仍未完成。

## 精确文件

- [check-r674-double-s-arithmetic-adaptation.js](../scripts/check-r674-double-s-arithmetic-adaptation.js)
- [check-r674-double-s-arithmetic-adaptation.json](../scripts/check-r674-double-s-arithmetic-adaptation.json)
- [check-r674-double-s-arithmetic-adaptation-eta-plus.json](../scripts/check-r674-double-s-arithmetic-adaptation-eta-plus.json)
- [check-r674-double-s-arithmetic-adaptation-eta-minus.json](../scripts/check-r674-double-s-arithmetic-adaptation-eta-minus.json)

两个分文件保存完整特征零十二乘二十行，避免只保辅助模数数据。
主证书保存原 S 六阶规范、原仿射项、第十三行、完整辅助矩阵、
左行配对和两个解；辅助计算的用途仅是证明固定特征零函数非零。
脚本从原 sigma 递推及 R594 原二十列/右逆生成所有数据，
包含 B_C 的第六矩，未增加独立抽样或复核门槛。

主要依赖：
[R594](R594-two-source-six-carry-compensation-and-unit-z-rectangle.md)；
[R664](R664-original-double-s-rotation-and-common-companion-gate.md)；
[R665](R665-original-mixed-unit-deep-branch-and-negative-one-return.md)；
[R667](R667-original-kernel-visible-mass-and-seven-source-contraction.md)；
[R669](R669-original-double-s-six-dimensional-source-return.md)；
[R670](R670-original-full-lambda-two-image-and-exact-cancellation.md)。
