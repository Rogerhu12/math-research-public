# R1022 — 原 degree390 的完整三乘十三平坦 trace 与同一 S10 长读者

日期：2026-11-27 UTC。**已证明。** 本篇将 R981 的两条实际
$\delta$-new 秩二来源，经完整十三支和三支返回同一个 degree10
target。全部39个分支、原 sigma／Miller 相位、质量 Gaussian、
特征零长前缀和完整 Newton 尾均保留。不是把 degree30 的
$F_A,Q_B$ 直接当成旧 $S_{10}$ 来源。

新的三处权使用原核零阶三，因此最终每个二挠极的 leading
成本为 $17p^2/18$，仍严格保持第三 Cartier 的原小边界范围。
在 R1018 的同一线性深度，整个39支原权模 $p$ 是一个真实
$p$ 次权。R1020 的同一个单 primitive 读者遂同时适用于原
degree130 行和两条新的 degree390 canonical 行。
原 $\delta$-old 分量的全部有限读数和全精度导数也准确返回旧行。

## 1. 原相位、两级 division 与固定输入

固定
$$
E:y^2=x^3+1,\quad X=x^3,\quad
\delta^2=-3,\quad \omega=(-1+\delta)/2,\quad
\pi=(7+\delta)/2,\quad \alpha=\delta\pi,\quad N(\alpha)=39.
\tag{1}
$$
仍用 $D=d/dz$、$\omega_E=dx/(2y)$。
取与 R1018、R1020 完全相同的
$$
p=6s-1>13^4,\qquad
H=6\left\lfloor\frac{s-5}{6}\right\rfloor+5=6q+5,
\qquad N=H(p+1).
\tag{2}
$$
原完整输入允许整个
$$
f=\sigma^{390}R_f,\qquad
R_f\in\mathcal O[X]_{\le65}.
\tag{3}
$$
所以 R981 的两条质量零 canonical 来源及原完整66维来源都在范围内。
以下加权 target 不另获 Hecke／Selmer 解释；其必要中央行只从
原真实 $f$ 的完整比较取得。

保持原
$$
\sigma(\pi z)=\pi\sigma(z)^{13}R_\pi(X),\qquad
x(\pi z)=\frac{x\mathsf A_\pi(X)}{\pi^2R_\pi(X)^2},
$$
$$
R_\pi=X^2+(2+6\delta)X+(40+24\delta)/13.
\tag{4}
$$
其中 $\mathsf A_\pi$ 是 R961/R1012 的原 monic degree4 多项式，
没有换成一个低 jet 拟合的 x-map。
原三处 division 是
$$
\boxed{\sigma(\delta z)=\delta\sigma(z)^3x(z).}
\tag{5}
$$
合并 (4)、(5)，完整地得到
$$
\boxed{
\sigma(\alpha z)=\alpha\sigma(z)^{39}R_\alpha,\qquad
R_\alpha=x\mathsf A_\pi R_\pi.
}
\tag{6}
$$
例如直接合成先给
$R_\alpha=\pi^2R_\pi^3x(\pi z)$，再用 (4) 即是 (6)。
所以没有一个未指定的三处 theta 常数。

## 2. 真实 normδ 平坦权与准确成本

沿 R1016，记
$$
B_{a,k}(T)=\sum_{j=0}^k(-1)^j\binom{a+j-1}{j}(T-1)^j,
$$
$$
v_\pi=\frac{R_\pi}{(X+1)^2},\qquad
V_\pi=v_\pi^{N+1}B_{N+1,N/6}(v_\pi).
\tag{7}
$$
新的三处权是
$$
\boxed{
v_\delta=\frac{X}{X+1},\qquad
a_\delta=N/3+1,\quad k=N/6,\qquad
V_\delta=v_\delta^{a_\delta}B_{a_\delta,k}(v_\delta).
}
\tag{8}
$$
这些都是特征零的明确有理函数。

在 $O$，$v_\delta=1+O(z^6)$。
在两个非零 $\delta$ 核点 $(0,\pm1)$，$x$ 有一阶零，
所以 $v_\delta$ 有三阶零；在三个非零二挠点有二阶极。
因此完整有限和给
$$
\boxed{
\begin{aligned}
V_\delta&=1+O(z^{N+6})&&\text{at }O,\\
\operatorname{ord}_T V_\delta&=N+3&&
  (0\ne T\in E[\delta]),\\
\operatorname{pole}_T V_\delta&=N+2&&
  (T\in\mathcal D_2).
\end{aligned}}
\tag{9}
$$
第一行使用 $k+1=N/6+1$，第二行使用 $3a_\delta=N+3$，
第三行使用 $2(a_\delta+k)=N+2$。
特征零首系数 $B_{a_\delta,k}(0)$ 非零。
其约化可能提高核零阶，本篇不将该二项式反演。

这里必须利用实际三阶核零。
若无证把 $a_\delta$ 改为 $N+1$，就会丢掉本篇之后
$17/18$ 的真实极帽余量。

## 3. 两次未平均 trace 与整个39支的唯一归一

先作原十三支到 degree30：
$$
A_{30,\pi}(f)
=\pi^{-30}\operatorname{Tr}_{[\pi]}
\left(V_\pi\frac{R_f}{R_\pi^{30}}\right),\qquad
h_{30,\pi}=\sigma^{30}A_{30,\pi}.
\tag{10}
$$
再作完整三支：
$$
\boxed{
A_{10,\alpha}(f)
=\delta^{-10}\operatorname{Tr}_{[\delta]}
\left(V_\delta\frac{A_{30,\pi}(f)}{x^{10}}\right),\qquad
h_{10,\alpha}(f)=\sigma^{10}A_{10,\alpha}(f).
}
\tag{11}
$$
所有 trace 均未平均。

由有限 trace 的传递性和 (4)，
$$
R_\pi^{30}x(\pi P)^{10}
=\pi^{-20}R_\alpha^{10}.
$$
所以 (10)–(11) 完整地等于
$$
\boxed{
A_{10,\alpha}(f)
=\alpha^{-10}\operatorname{Tr}_{[\alpha]}
\left(V_\alpha\frac{R_f}{R_\alpha^{10}}\right),\qquad
V_\alpha(P)=V_\pi(P)V_\delta(\pi P).
}
\tag{12}
$$
前面的 $\pi^{-30}\delta^{-10}$ 与 $\pi^{20}$ 正好形成
$\alpha^{-10}$；没有额外3、13或39。

使用原 degree390 canonical Heisenberg lift $T_T$，
(6) 直接给完整 theta 身份
$$
\boxed{
h_{10,\alpha}(f)(\alpha z)
=\sum_{T\in E[\alpha]}V_\alpha(P(z)+T)\,T_Tf(z).
}
\tag{13}
$$
其相位可直接检查：
$\alpha T$ 属原晶格，sigma 的准周期在第十次幂后
semichar 为一，余下指数准确是原 degree390 lift。
所以 (13) 没有用未规范的普通平移替代 $T_T$。
也没有先对十三字或三字作几何投影后再乘权。

39个点分成原点、12个非零 $\pi$ 核点和另外26个
$\pi T\in E[\delta]\setminus O$ 的点。
由 (7)、(9)，前一类的核零至少 $N+1$，
后一类至少 $N+3$；在 $O$，$V_\alpha=1+O(z^{N+6})$。
因此整个特征零前缀满足
$$
\boxed{
h_{10,\alpha}(f)(\alpha z)-f(z)=O(z^{N+1}).
}
\tag{14}
$$
两边 principal 时实际可提高至 $N+6$；
后文只使用 (14)。

## 4. 整个增长极、整基和统一 Hurwitz 尾

第一步只在原二挠有极：
$$
\operatorname{pole}_{\mathcal D_2}A_{30,\pi}
\le4(7N/6+1)=14N/3+4.
$$
其在 $O$ 的极至多30。
第二步 (9) 只增加 $N+2$；
$x^{-10}$ 的两个三核极由 (9) 完整消去。
$[\delta]$ 置换原三个二挠点，故
$$
\boxed{
\operatorname{pole}_{\mathcal D_2}A_{10,\alpha}
\le17N/3+6,\qquad
\operatorname{pole}_OA_{10,\alpha}\le10.
}
\tag{15}
$$
没有其它极。等价地，直接看 (12)：
$V_\delta(\pi P)$ 的极在 $[\pi]^{-1}\mathcal D_2$，
这些点全部由 $[\alpha]$ 送到 $\mathcal D_2$；
真正最大的帽出现在原三个二挠点。

由原 principal 角色及整模型上的 trace，
$$
\boxed{
A_{10,\alpha}(f)=
\frac{x^2P_{\alpha,f}(X)}{(X+1)^{M_\alpha}},
\qquad M_\alpha=17N/6+3,\qquad
\deg P_{\alpha,f}\le M_\alpha+1,\qquad
P_{\alpha,f}\in\mathcal O[X].
}
\tag{16}
$$
整性逐步成立：
两次 cover 在 $p>13^4$ 都是有限 étale；
所有 binomial 整数和原 division 系数整，
核处分母已由实际零阶消去。
整局部环中有限自由乘法的矩阵 trace 仍整。
乘去 (15) 的显示二挠分母、再除去角色强迫的 $x^2$，
得到原仿射不变量环 $\mathcal O[X]$ 中的元素。
这不使用一个可能有 $p$ 分母的坐标求解器。

R1016 的同一个整 Hurwitz 证明逐基适用：
$$
(\sigma^\circ)^{10}\frac{x^2X^j}{(X+1)^{M_\alpha}}
=
w^{M_\alpha+1-j}U_\sigma^{10}
W_0^{2+3j-3M_\alpha}(1+wW_0^{-3})^{-M_\alpha}.
\tag{17}
$$
所有 $w$ 指数非负，单位的整数负幂保持整性；
严格内盘范数仍至多一，常数不随 $M_\alpha$ 增长。
第一步的 degree30 版本同样由
$w^{M+5-j}U_\sigma^{30}W_0^{3j-3M}
(1+wW_0^{-3})^{-M}$ 直接支付。
本篇不把增长空间称为固定十维来源，也不假定其复高度固定。

## 5. 两个 Gaussian、质量和全 p^(H+1) 比较

令
$$
q_\pi=\pi^{p+1}/13,\qquad
q_\delta=\delta^{p+1}/3,\qquad
q_\alpha=\alpha^{p+1}/39=q_\pi q_\delta.
\tag{18}
$$
它们都属于 $1+p\mathcal O$。
保持原共同 $c$、$v_p(c)=-1$，置
$$
\gamma_\alpha=10c(\alpha^{p+1}-39)\in\mathcal O.
$$
整个 charge390 Gaussian 准确为
$$
e^{-390cz^{p+1}}h_{10,\alpha}(f)(\alpha z)
=e^{\gamma_\alpha z^{p+1}}
G_{10,h}(\alpha z).
\tag{19}
$$
在全部非负整数插值后，原同一 Tate 域中的唯一性给
$$
J_{390,h(\alpha z)}(v)=q_\alpha^vJ_{10,h}(v).
\tag{20}
$$
原单位 $\alpha$ 保盘范数，(17) 保全部无限尾。

由 (14)，原 Gaussian 的前 $H$ 个 Newton 项在特征零中
准确相同；剩余尾沿 R1016 的同一个证明至少含 $p^{H+1}$。
该证明只需 $H\le s$，所有 charge 常数10、30、390在本篇好位是单位。
于是
$$
\boxed{
j_f-j_{10,h_{10,\alpha}(f)}
-m_0(f)\log_pq_\alpha
\in p^{H+1}\mathcal O.
}
\tag{21}
$$
这同时保全部旧低项的真实高精度，
不是只替换最后一项的模 $p$ 值。
对 R981 两个质量零 canonical 来源，
其坏素数假设因此确实给同一 $S_{10}$ target 的深零行。

若拆成两步，第一步的质量修正是 $m_0(f)\log q_\pi$，
第二步是 $m_0(f)\log q_\delta$；两次质量均由真实长前缀保留。
只有它们的和才是 (21)。
特别不得因标准 $F_A$ 的质量一或 $Q_B$ 的四阶首项，
擅自改变整个 degree390 canonical 来源的质量。

## 6. 三处也是真实单 Frobenius 权

R1018 已付
$$
\bar V_\pi=W_\pi^p,\qquad
W_\pi=v_\pi^{H+1}B_{H+1,q}(v_\pi).
$$
这里 $H=6q+5$。同一 $k=N/6=Hs$ 可写为
$$
k=qp+t,\qquad t=q+5s.
$$
三处的参数准确分解为
$$
a_\delta=2Hs+1=(2q+1)p+a_0,\qquad
a_0=2q+4s+2.
$$
在本篇范围 $0<a_0<p$、$p\le a_0+t<2p$。
所以二项式 $\binom{a_\delta+k}{k}$ 有一次实际 carry。

用 R1018 的完整导数式，$\bar V_\delta$ 的导数为零，
故它是某个多项式的 $p$ 次幂。
其根在 $v_\delta=0$ 至少有 $2q+2$ 阶零，
在 $v_\delta=1$ 与1的差至少有 $q+1$ 阶零，
次数至多 $3q+2$。
这唯一确定
$$
\boxed{
\bar V_\delta=W_\delta^p,\qquad
W_\delta=v_\delta^{2q+2}B_{2q+2,q}(v_\delta).
}
\tag{22}
$$
因此
$$
\boxed{
\bar V_\alpha=W_\alpha^p,\qquad
W_\alpha(P)=W_\pi(P)W_\delta(\pi P).
}
\tag{23}
$$
在39个原核点的每一个非零点，$W_\alpha$ 的零阶至少 $H+1$，
在 $O$ 则 $W_\alpha=1+O(z^{H+1})$。
三处准确使用 $3(2q+2)=H+1$。
(22)–(23) 是同一个原特征零权的实际约化；
本篇从不把特征零 $V_\alpha$ 替换为 $W_\alpha^p$ 后声称保持
整个 $p^{H+1}$ 精度。

## 7. 原 P10 的全部边界仍严格落在同一小帽

对每个 $0\le b<p$，令
$$
\eta_{\alpha,b}
=Z^{-b-1}P_{10}A_{10,\alpha}(f)\omega_E.
$$
由 (15) 和原 $P_{10}$ 的完整 $Z^p$ 因子，
$$
\boxed{
\operatorname{pole}_O\eta_{\alpha,b}\le b+1\le p,\qquad
\operatorname{pole}_{\mathcal D_2}\eta_{\alpha,b}
\le d_{\alpha,b}
=p^3-p^2+(8-b)p+17N/3+7<p^3.
}
\tag{24}
$$
不存在其它 $Z=0$ 点补极。
最后一个严格不等式使用
$$
d_{\alpha,b}-p^3
\le\frac{-p^2+178p+143}{18}<0.
$$
这正是 $17p^2/18$ 的实际余量，不是忽略增长极。

两次 Cartier 的形式帽为
$$
d_{1,\alpha}
=p^2-p+9-b+
\left\lfloor\frac{17N/3+6}{p}\right\rfloor<p^2,\qquad
d_{2,\alpha}=
\left\lfloor\frac{d_{1,\alpha}-1}{p}\right\rfloor+1\le p.
\tag{25}
$$
原点留数准确是
$$
\boxed{\rho_{\alpha,b}=\alpha^{-b}c_b(f).}
\tag{26}
$$
因此 R1013 的六类对数／全纯边界及其全部符号仍适用，
R1020 的同一个 $Z,\varphi,\varphi_H,\mathfrak M_H$ 也逐式适用。
特别两种第一 primitive 的统一帽仍分别不超过
$p^2+1$ 和 $p(p+H-1)-1$。
全部 $b$，包括末四个非 diagonal 余数，都按原完整公式保留。

有限模型到 sigma 的回代也保持所有项。若
$t_n=[Z^n](P_{10}A_{10,\alpha})$，置
$$
E_{\alpha,p}(z)=
\frac{\sigma^\circ(\alpha z)^{10}}{P_{10}(\alpha z)},\qquad
V_{\alpha,p}(z)=\frac{Z(\alpha z)}{\alpha z},
$$
$$
M_\alpha(m,n)=[z^{m-n}]E_{\alpha,p}(z)V_{\alpha,p}(z)^n.
$$
则原 $g_h$ 的模 $p$ 返回是
$$
\boxed{
g_{h,390}\equiv
\sum_{j=0}^h\frac{\gamma_\alpha^j}{j!}
\sum_{\substack{0\le n\le(h-j)(p+1)\\6\mid n}}
\alpha^n M_\alpha((h-j)(p+1),n)t_n\pmod p.
}
\tag{27}
$$
这是真实完整下三角式；非 diagonal 的 $\alpha^n$ 没有被
改为 $39^h$。所有高精度低项仍由 (21) 的单一特征零输入支付。

## 8. 明确的三字 Kummer 规范与全39字

三处的实际点沿 R1021 取
$B_3=\delta v_3=(0,-1)$。
于是标准点 $S_3=-10B_3=(0,1)$、$R_i=-iB_3$。
可直接采用
$$
\boxed{
h_3=1-y,\qquad
\kappa_3=-\frac{y+\delta}{\delta x},\qquad
\kappa_3^3=[\delta]^*h_3,\qquad
\kappa_3\sim\delta^{-1}z^{-1}.
}
\tag{28}
$$
证明使用原
$$
x(\delta P)=-\frac{X+4}{3x^2},\qquad
y(\delta P)=-\frac{y(X-8)}{3\delta X}.
$$
因 $(y+\delta)^3=y(X-8)+3\delta X$，(28) 的常数准确为一。
直接加 $(0,1)$ 使 $\kappa_3$ 乘 $\omega^2$，
故原 $u_\delta=(0,-1)$ 给字符 $\omega$。
这与原 odd3 lift 的中心相位配准。

标准两条 Miller 函数也可显示为
$$
\boxed{h_{3,1}=(1-y)^{-3},\qquad
h_{3,2}=x^2/(1+y)^4.}
\tag{29}
$$
它们分别满足
$\operatorname{div}h_{3,i}=(10-i)O+iS_3-10R_i$
及原点首项 $z^{10-i}$，没有额外三次根。
这些公式可用于逐三支消费，或与原十三字合并。

在完整 $\alpha$ cover 上，按实际 canonical lifts 选择原
CRT 字符，取规范 Kummer 函数
$$
\kappa_{39}^{39}=[\alpha]^*h_{39},\quad
\kappa_{39}\sim\alpha^{-1}z^{-1},\quad
\operatorname{div}h_{39}=39(S_{39}-O).
$$
这里 $S_{39}=-10B_{39}$，$B_{39}$ 由实际 dual lift 确定，
并令
$$
R_i=4iS_{39}=-iB_{39},\qquad
\operatorname{div}h_{39,i}=(10-i)O+iS_{39}-10R_i,
\quad h_{39,i}\sim z^{10-i}.
\tag{30}
$$
$10\cdot4\equiv1\pmod{39}$，所以这些 divisor 都是 principal；
原 Laurent 首项唯一固定常数。
Kummer 等式的常数也由首项确定为一。

写
$$
R_f/R_\alpha^{10}=\sum_i f_i\kappa_{39}^i,\qquad
W_\alpha=\sum_j g_j\kappa_{39}^j.
$$
则 (12)、(23) 的完整未平均返回准确为
$$
\boxed{
A_{10,\alpha}(f)\bmod p
=39\alpha^{-10}
\sum_{i+pj\equiv0\ (39)}
g_j^p h_{39}^{(i+pj)/39}f_i.
}
\tag{31}
$$
标准化后每项保
$Z^{-b-1}P_{10}$、$g_j^p$、显示的 $h_{39}$ 幂、
原 $h_{39,i}^{-1}$ 及 $R_i$ 平移。
只有整个乘积形成后才可作几何投影。
各原3字和13字没有被删成一个无权 trace。

### 8.1 全部规范常数有有限代数读法

令 $m_i=m_0(\mathcal P_i f)$。
对 $T\ne O$ 的原 $\alpha$ 核点，由 (6) 和原 lift，
$$
m_0(T_Tf)=\frac{R_f(T)}{(DR_\alpha(T))^{10}}.
$$
所以
$$
\boxed{
m_i=\frac1{39}\sum_{T\in E[\alpha]}
\chi_i(T)^{-1}m_0(T_Tf),
}
\tag{32}
$$
$T=O$ 项取原质量。这里每项都是指定的有限代数表达式；
没有另挑一个 theta 常数。

在 (30) 的标准规范中，完整 $Q_i$ 满足
$$
Q_i(P)=h_{39,i}(P+R_i)f_i(P+R_i),\qquad
Q_i(iB_{39})=\alpha^{10}m_i.
\tag{33}
$$
因此若该原纯张量的标准方向是已付的 $u=\sigma^{10}U$，
则准确为
$$
\boxed{
Q_i(P)=\frac{\alpha^{10}m_i}{U(iB_{39})}U(P).
}
\tag{34}
$$
这不是仅给一个未定比例。
在本题两条 odd3/nontrivial13 来源上，
只有24个 $i\in(\mathbf Z/39)^\times$ 的字非零，
标准方向分别是 R1021 的
$$
U_A=y(X+4),\qquad U_B=xy.
$$
它们在 primitive39挠点上都不为零：
其零点只属于二挠或三挠。
在本篇好约化上 prime-to-p torsion 保持准确阶，
故这些显示分母都是单位。
公式 (32) 本身不反演 $m_i$。

### 8.2 同一完整字中的实际乘子

使用 R1021 的原 raw 来源
$f_A=\mathcal L_{30,\chi_6}F_A$、
$f_B=\mathcal L_{30,\chi_{10}}Q_B$，
同一 $(s,i)$ 字（$s=\pm1,i\ne0\bmod13$）的完整原系数分别是
$$
-\frac{s\chi_6(i)}{8C_v^{10}},\qquad
-\frac{s\chi_{10}(i)}{60C_v^{10}},
$$
并使用同一 $T_{iv_{13}+su_3}D_\alpha$。
所以在整个字上准确有
$$
\boxed{
\mathcal P_{s,i}f_B(P)=
\frac2{15}\chi_4(i)
\frac{x(\alpha P+B_{s,i})}{X(\alpha P+B_{s,i})+4}
\,\mathcal P_{s,i}f_A(P).
}
\tag{35}
$$
标准化后，同一个全部带权输入的乘子就是
$(2/15)\chi_4(i)x(Q)/(X(Q)+4)$。
原三处 $C_v^{10}$ 与全部 lift 相位真实相消。
若使用 R981 首项一的 canonical 规范，只再乘其固定整体
$\gamma_A/\gamma_B$；不把这个比例当成每个字的新自由参数。

(35) 保留 (31) 的所有权和 Miller 函数。
它既不将该有理乘子越过 Cartier，也不由一个来源中央为零
推另一个字的测试为零。

## 9. 真 δ-old 分量与旧读者的全精度相容

对任意原 $g\in\mathcal V_{130,\mathcal O}$，取真实
$D_\delta g(z)=g(\delta z)\in\mathcal V_{390,\mathcal O}$。
应用 (14) 后把变量换成 $w=\delta z$，有
$$
h_{10,\alpha}(D_\delta g)(\pi w)-g(w)=O(w^{N+1}).
$$
R1016 原十三 trace 同时满足
$h_{N,\pi}(g)(\pi w)-g(w)=O(w^{N+1})$。
因此在同一个目标变量中，完整特征零前缀准确相同：
$$
\boxed{
h_{10,\alpha}(D_\delta g)-h_{N,\pi}(g)=O(z^{N+1}).
}
\tag{36}
$$
由共同整 Hurwitz 尾，
$$
\boxed{
j_{10,h_{10,\alpha}(D_\delta g)}
-j_{10,h_{N,\pi}(g)}
\in p^{H+1}\mathcal O.
}
\tag{37}
$$

质量的整个账本也可单独核对：
$$
J_{390,D_\delta g}(v)=q_\delta^vJ_{130,g}(v),\qquad
q_\alpha=q_\pi q_\delta.
$$
所以 (21) 中增加的 $m_0(g)\log q_\delta$
与真实 $D_\delta$ 的质量修正准确相消。
这不是把质量一的两 target 导数直接认作相同。

(36) 还通过同一个 sigma／$P_{10}$ 下三角返回，给
全部 $n\le N$ 的实际模 $p$ 有限读数相同。
原点留数亦准确为
$$
\alpha^{-b}c_b(D_\delta g)=\pi^{-b}c_b(g).
$$
故对 R1020 的同一个平坦 primitive，在
$n=rp+b\le N$、$0<r\le H$ 时，
$$
\boxed{
[Z^r]\!\left(
K_{H,\alpha,b}(D_\delta g)-K_{H,\pi,b}(g)
\right)=0.
}
\tag{38}
$$
这是整个实际低窗的同类读取，未宣称两个全局 primitive 类
或两个全局亚纯 target 相等。

因此 R1021 六项分解中的真实
$D_\delta\Psi_{125}$、$D_\delta\Psi_{12500}$ 及其完整十三字，
可以用 (36)–(38) 返回 R978 的原 old 差。
所有有限 profile、原连接缺陷和另外四个完整来源仍须保留；
不能以 (38) 为由把 $\delta$-new 项也改成 old 项。

## 10. 实际取得的共同约束与继续的非零目标

若四条既有 rank至少二曲线在同一目标素数都坏，
R970/R973/R981 的真实桥给其四条 canonical $j$ 为零。
R1016 与 (21) 因而把这四条真实必要行送到同一个
$S_{10}$ 的原 $P_{10},Z,\varphi_H,\mathfrak M_H$ 读者中；
来源与权仍按各自的实际完整 trace 保留，不把它们认作相同函数。

与此同时，(36)–(38) 把已付的 old 对数非零保留在同一读者。
例如原两个 old 质量一标准来源的三处拉回，必须支付完整
$\log q_\delta$ 后才返回旧差，不能因中间 $F_A$ 的质量一
或 $Q_B$ 的低阶形状而修改原 canonical 零条件。

后续须在 R1021 的实际3处连接／六分量身份、
(31)–(35) 的完整字权和 R1020 的同一 primitive 中，
迫使这个 old 读数消失，才能得到目标矛盾。
本篇没有从一次 trace、一个 $O_3$ 方向、一个乘子或
四条标准向量的线性独立性自动传播中央零。

全部结论使用显示 division、有限整 trace、原 Tate 插值、
统一 Hurwitz 尾和完整 Kummer／Miller 规范，无新数学执行或素数扫描。
固定坏处已被 $p\le13^4$ 包含；增长二项式不被反演。
依赖：R961/R973/R978/R981 的真实来源和 division；
R1012/R1015 的标准字方法；
R1016/R1018 的原全精度与单 Frobenius 权；
R1020 的单 primitive；R1021 的实际 odd3 来源及全部连接分量。


## 11. 原三字代数的显式系数与合法的反次序权

### 11.1 三字不是三个自由输入

以下 $(x,y)$ 是 $[\delta]$ 的 target 坐标，$\kappa=\kappa_3$。
由 (28) 和原 $x$-map，完整逆式是
$$
x_{\rm up}=-\frac{2\kappa}{\kappa^2-x},\qquad
y_{\rm up}=\delta\frac{\kappa^2+x}{\kappa^2-x},\qquad
\kappa^3=1-y.
\tag{45}
$$
因此原三处权的生成元准确为
$$
\boxed{
v_\delta=
\left(\frac13+\frac1{y^2}\right)
-\frac{x(y+3)}{3y^2}\kappa
+\frac{(y+1)(y-3)}{3xy^2}\kappa^2.
}
\tag{46}
$$
证明不依赖数值选择：将右端乘以
$3y^2(\kappa^2+x)^2$，用
$\kappa^3=1-y$、$x^3=y^2-1$，三个字的系数分别成为
$4y^2x^2$、$4y^2(1-y)$、$4y^2x$。
这正是
$3y^2\{(\kappa^2+x)^2+(\kappa^2-x)^2/3\}$。
特别 $\operatorname{Tr}_{[\delta]}v_\delta=1+3/y^2$，
其原点值是一，和真实三个纤维的质量吻合。

记
$$
W_\delta=g_0+g_1\kappa+g_2\kappa^2.
\tag{47}
$$
全部 $g_j$ 是在明确的三维代数
$K(E)[\kappa]/(\kappa^3-(1-y))$ 中，将 (46)
代入 $v^{2q+2}B_{2q+2,q}(v)$ 得到的固定有理函数。
没有逐字另选的标量、额外根或自由参数。

### 11.2 反次序必须重新支付完整比较

定义另一条特征零原权
$$
V_\alpha^{\rm alt}(P)=V_\delta(P)V_\pi(\delta P).
\tag{48}
$$
它在 $O$ 仍是 $1+O(z^{N+6})$；
在两个非零 $\delta$ 核点零至少 $N+3$，
在其余36个非零 $\alpha$ 核点零至少 $N+1$。
其所有极在 $\mathcal D_2$ 及 $[\delta]^{-1}\mathcal D_2$。
原三个二挠点处的最大极准确不超过
$$
(N+2)+(14N/3+4)=17N/3+6.
$$
所以
$$
A_{10,\alpha}^{\rm alt}(f)
=\alpha^{-10}\operatorname{Tr}_{[\alpha]}
\left(V_\alpha^{\rm alt}\frac{R_f}{R_\alpha^{10}}\right)
\tag{49}
$$
满足 (14)–(27) 的全部整性、Hurwitz、质量 Gaussian、
原窗口和极帽。

其常数也可逐级检查。先作
$$
A_{130,\delta}
=\delta^{-130}\operatorname{Tr}_{[\delta]}
\left(V_\delta\frac{R_f}{x^{130}}\right),
$$
再作
$\pi^{-10}\operatorname{Tr}_{[\pi]}
(V_\pi A_{130,\delta}/R_\pi^{10})$。
另一顺序的 sigma identity 是
$R_\alpha=\delta^{12}x^{13}R_\pi(\delta P)$；
其第十次幂正好把前面的
$\delta^{-130}\pi^{-10}$ 变为 $\alpha^{-10}$。

因此这是一个已付精度的新选择，而不是把旧权交换后
直接宣布读者不变：
$$
j_{10,h_\alpha^{\rm alt}(f)}
-j_{10,h_\alpha(f)}\in p^{H+1}\mathcal O,
\qquad
h_\alpha^{\rm alt}(f)-h_\alpha(f)=O(z^{N+1}).
\tag{50}
$$
原 $H$ 窗内的全部实际有限读数亦相等。
模 $p$ 的真实根是
$W_\alpha^{\rm alt}=W_\delta(P)W_\pi(\delta P)$，
两因子的完整来源各自仍保留。

### 11.3 两条新行确实共享同一个三字权

取 R1021 的几何正分支
$u_3=\pi^{-1}v_3$，而 deck 方向仍固定为
$u_\delta=(0,-1)$。
原 $T_{v_3}D_\delta$ 的字方向是 $\kappa^{10}$，即 mode1；
但 $\pi u_\delta=-u_\delta$。
所以经过真实 $D_\pi$ 后，正分支在当前 $\kappa_\delta$
规范中是 **mode2**。这一步不能沿用 degree30 的 mode1 标签。
因 $p\equiv-1\pmod3$，相应的权准确是 $g_2$。

若写完整第一步 rational source 为
$R_f/x^{130}=\sum_i f_i\kappa^i$，则该正分支的整个
第一返回是
$$
\boxed{
\bar A_{130,\delta}
=3\delta^{-130}g_2^p h_3^{4s}f_2,
\qquad 4s=(2+2p)/3.
}
\tag{51}
$$
两条真实 $u_A,u_B$ 分支使用完全同一个 $g_2^p$。
其后的十三字、$P_{10}$、Miller 和原测试仍整体保留。

同一第一步对真正 $\delta$-old 来源 $D_\delta g$ 则是
$$
\boxed{\bar A_{130,\delta}(D_\delta g)=3g_0^pR_g.}
\tag{52}
$$
因此旧、新权的准确差是实际 $(g_0,g_2)$，不是两个可自由
调整的常数。旧行与原 degree130 读者的全精度相等仍由
§9 的特征零比较支付，不能只从 (52) 猜出。

若在第一步先作标准 Miller 返回，target 是 degree130，
必须使用
$$
h_{3,1;130}=(1-y)^{-43},\qquad
h_{3,2;130}=x^2/(1+y)^{44}.
\tag{53}
$$
它们满足
$\operatorname{div}h_{3,i;130}=(130-i)O+iS_3-130R_i$
且原点首项分别为 $z^{129}$、$z^{128}$。
(29) 的 degree10 函数不能直接代替它们。
完成后一个十三支 trace 后，才回到本篇原 $P_{10}$
和 R1020 的同一 primitive。

## 12. 单个三处正分支的真实必要行

R1021 的几何正、负来源记作
$$
A_\pm=\sum_{i\ne0}\chi_6(i)
 T_{iv_{13}\pm u_3}D_\alpha u_A,\qquad
B_\pm=\sum_{i\ne0}\chi_{10}(i)
 T_{iv_{13}\pm u_3}D_\alpha u_B.
$$
$u_A,u_B$ 都是奇函数，两个十三字符在 $-1$ 上都是一。
原 canonical lifts 因此给
$A_+(-z)=-A_-(z)$、
$B_+(-z)=-B_-(z)$。
原未归一来源 $f_A,f_B$ 的完整偶部准确是
$$
\Pi_{\rm even}A_+=-4C_v^{10}f_A,\qquad
\Pi_{\rm even}B_+=-30C_v^{10}f_B.
\tag{54}
$$
因为所有 $h(p+1)$ 都是偶数，原 Gaussian 也为偶函数，
(54) 给真实的全中央关系。
坏 canonical 假设确实迫
$j(A_+)=j(B_+)=0$；负分支亦然。
这里只分开三处的两个几何分支，没有把十三字逐一赋零。

为了在返回中保持这个正分支，允许原整个 $S_{390}$
作为中间输入。§3–§7 的 trace、核零和极帽不变；
只是 target 的整基改为
$$
\sigma^{10}\frac{P(x)+yQ(x)}{(X+1)^{M_\alpha}},
\qquad
\deg P\le3M_\alpha+5,\quad
\deg Q\le3M_\alpha+3.
\tag{55}
$$
两个基族的原点阶分别为
$10+6M_\alpha-2j\ge0$、
$7+6M_\alpha-2j\ge1$。
同一 Hurwitz 单位证明遂逐项成立。
原 $J$ 通过真实 principal 投影扩展到这些输入；
本篇只消费 (54) 的偶部，未额外声明非 principal Selmer 桥。

两种权都是偶函数，$[\alpha]$ 和全部 trace 与 $[-1]$
交织，原 $Z$ 为奇、$P_{10}$ 为偶；
R1020 的两个 section 也与 $[-1]$ 交织。
因此 (54) 不只在最终 $j$ 成立，
也在同一 primitive 的全部所需低窗成立：
对于 $n=rp+b\le N$、$n$ 偶、
$0<r\le H$，对应 primitive 系数的比例准确是
$(-4C_v^{10})^{1/p}$ 或 $(-30C_v^{10})^{1/p}$。
最后的原读者再取 $p$ 次方恢复 (54) 的标量。

所以实际消元现在可使用同一个三处正分支、同一
$g_2^p$ 和同一完整 target primitive；
旧两行仍用真实 $g_0^p$，并由 §9 精确接回原旧对数。
这个安排没有删去 $g_2/g_0$、十三处 profile、Miller
连接或 R1021 第四阶中的四个补来源。
