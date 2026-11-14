# R402 — E24 原 degree72 来源的惰性半因子、完整 Selmer 桥与联合进位

日期：2026-11-14。**状态：以下固定 E24 原来源的全部高度二估计、过收敛半因子、同一整 signed 类与完整通常 Selmer 比较、首项常数及全深度有限证书均已证明。原 S34/S72 的实际乘积给完整角向进位关系。尚未证明这些证书对无穷多个素数命中。**

## 1. 固定原来源、真实缩放和结论

固定
$$
E_{24}:y^2=x^3+24,\quad K=\mathbf Q(\delta),\quad
\delta^2=-3,\quad s_0=(1-\omega)^{-1}.
$$
R398 已证明本曲线秩恰二；本篇不重新计算秩。
在 $E_1:y^2=x^3+1$、原微分 $dz=dx/(2y)$ 下，令
$$
\begin{aligned}
Q_4(X)&=(X+4)(X^3-96X^2+48X+64),\\
P_6(X)&=(7X^2-4X+16)(X+1)(X-8)(X^2+20X-8),\\
A_{72}(z)&=\frac17\sigma^{72}x^3Q_4(x^3)P_6(x^3)
          =\sum_{m\ge0}\alpha_m^{72}z^m,\\
B(z)&=x\sigma^2=\sum_{m\ge0}\beta_mz^m .
\end{aligned}
\tag{1}
$$
$A_{72}=z^6+\cdots$、$B=1+\cdots$，两者只含六的倍数次幂。
它们的物理意义已经由 R398/R302 识别，不重新选择 theta 来源。

取固定正实根
$$
\theta=24^{1/6},\qquad C_{24}=-6048\sqrt[3]9,\qquad
\kappa_{24}=\frac{L(E_{-8},1)}{6\Omega_{24}}\ne0 .
$$
R395/R397/R398 的同一个实际六项来源满足
$$
\boxed{
\Phi_{24}(z)=C_{24}A_{72}(\theta z)=\sum s_mz^m,\qquad
s_m=C_{24}\theta^m\alpha_m^{72}.
}
\tag{2}
$$
$C_{24}$ 是原有限 lift 的准确标量，不是待选择的平方根单位。
$\kappa_{24}$ 的代数性、非零性及周期已由 R397 支付。
[R401 的四个原模符号计算](R401-e24-exact-central-constant-from-four-original-modular-symbols.md)
进一步准确给
$
\boxed{\kappa_{24}=\frac1{6\sqrt[3]3}.}
\tag{2a}
$
因此本篇全部素数都有 $v_p(\kappa_{24})=0$。
下文仍显示它在比较式中的位置，以保留真实规范。

本篇范围是
$$
\boxed{p\ge11,\qquad p\equiv5\pmod6,\qquad d=p+1=6s.}
\tag{3}
$$
新曲线在这些素数均好惰性；本篇不排除 $p=17$。
与旧 $E_{17}$ 联合使用时，再按旧曲线的好约化范围排除十七。
记 $\mathcal O=\mathbf Z_{p^2}$，$v_p(p)=1$。

置
$$
F(z)=\log(\sigma(z)/z),\qquad c=[z^d]F,\qquad
G_{72}=A_{72}e^{-72cz^d},\quad G_0=Be^{-2cz^d}.
$$
定义准确 Newton 半因子
$$
\boxed{
J_{72,p}(u)=\sum_{h\ge0}a_h(u)_h,\quad
a_h=[z^{dh}]G_{72}(72c)^{-h},\qquad
J_{0,p}(u)=\sum_{h\ge0}[z^{dh}]G_0(2c)^{-h}(u)_h.
}
\tag{4}
$$
这里 $(u)_h=u(u-1)\cdots(u-h+1)$。
本篇证明
$$
J_{72,p}\in pu\mathbf Z_p\langle u\rangle,\quad
J_{0,p}\in1+p\mathbf Z_p\langle u\rangle,\quad J_{72,p}\ne0.
\tag{5}
$$
令 $e=\operatorname{ord}_0J_{72,p}$、$j_e=[u^e]J_{72,p}$。
存在同一标准椭圆单位类的非零整 Rubin 系数
$\mathcal A_{24,p}(T)\in\mathcal O[[T]]$，满足
$$
\boxed{
\operatorname{ord}_0\mathcal A_{24,p}=2e,\qquad
v_p([T^{2e}]\mathcal A_{24,p})
 =v_p(\kappa_{24})+2v_p(j_e)-2e.
}
\tag{6}
$$
这里保留固定 $v_p(\kappa_{24})$，没有无证将它设为零。
完整通常 Selmer 给
$$
\boxed{
2+\operatorname{corank}_{\mathbf Z_p}
 \Sha(E_{24}/\mathbf Q)[p^\infty]\le2\operatorname{ord}_0J_{72,p}.
}
\tag{7}
$$
所以 $J_{72,p}'(0)\ne0$ 足以证明同一固定曲线的完整初级有限。

## 2. 同一高度二对数与真实首分母

R301 的底曲线正是本篇 $E_1$。
其证明仅使用该曲线的形式对数，与目标来源的 degree 无关。
为明确全部归一，取 $t=x^{-1/2}=z+\cdots$，则
$$
z(t)=t+\sum_{n\ge1}
 \frac{(-1)^n\binom{2n}{n}}{4^n(6n+1)}t^{6n+1},
\qquad
W(z):=z^2x(z)=1+\sum_{n\ge1}X_nz^{6n}.
\tag{8}
$$
若 $a=v_p(6n+1)$，$n$ 的前 $a$ 位交替为 $5s-1,s-1$。
二项式进位数至少 $\lceil a/2\rceil$，所以形式对数的相应系数
赋值至少 $-\lfloor a/2\rfloor$。
由
$(6n)/(p^2-1)\ge\lfloor v_p(6n+1)/2\rfloor$
和严格圆盘内的解析反演，
$$
v_p(X_n)\ge-\frac{6n}{p^2-1},\qquad
\|W\|_{R'}=1\quad(R'<R_E:=p^{-1/(p^2-1)}).
\tag{9}
$$
这是严格半径内的结论，不在临界边界假设逆函数等距。

原 sigma 微分方程给
$$
F=-\sum_{n\ge1}\frac{X_n}{6n(6n-1)}z^{6n}.
$$
对 $X_s$ 作同一有限 Lagrange 反演，准确有
$$
\boxed{
v_p(c)=-1,\qquad
pc\equiv-(-1)^s4^{-s}\binom{2s}{s}\pmod p .
}
\tag{10}
$$
$2s<p$ 使右边为单位；这不是可另选的 Gaussian 参数。

R301 的三段分母估计进一步给
$$
R=p^{-1/(2p)}<R_E,\qquad
\|F-cz^d\|_R<p^{-1/(p-1)} .
\tag{11}
$$
具体地，低于 $p^2-1$ 的剩余含分母项首个次数至少 $6p$；
边界项的加权赋值至少 $(p^2-1)/(2p)-1$；
高项 $q\ge p^2$ 的下界为
$q(1/(2p)-1/(p^2-1))-\lfloor\log_pq\rfloor$，并趋于无穷。
这些同一估计在 (3) 下均严格超过 $1/(p-1)$。

## 3. 新 degree72 的完整解析余项与所有整数权

令 $P(X)=XQ_4(X)P_6(X)=\sum_{i=1}^{11}P_iX^i$。
所有 $P_i$ 为整数，$P_{11}=7$。
因此原余项不是一个任意新的角多项式，而是
$$
\boxed{
G_{72}(z)=
 \frac17\sum_{i=1}^{11}P_i z^{72-6i}W(z)^{3i}
             e^{72(F-cz^d)}.
}
\tag{12}
$$
每个 $72-6i\ge6$。当前 $p$ 不整除七或七十二，
故 (9)–(11) 给
$$
\boxed{\|G_{72}\|_R\le R^6,\qquad
       \|G_0\|_R\le1,\qquad G_0(0)=1.}
\tag{13}
$$
单独取出的 $e^{72cz^d}$ 不需要在整个 $R$ 圆盘解析；
(12) 是实际解析定义，形式乘积仍完全正确。

由 $v_p(72c)=v_p(2c)=-1$，
$$
\boxed{
v_p(a_h)\ge\left\lceil\frac{h(p-1)+6}{2p}\right\rceil,\qquad
v_p(a_h^0)\ge\left\lceil\frac{h(p-1)}{2p}\right\rceil
\quad(h\ge1).
}
\tag{14}
$$
所以 (4) 在 $|u|_p<p^{(p-1)/(2p)}$ 上解析，并得 (5) 的两条
Tate 代数包含关系。
对每个非负整数 $k$，$(k)_h=0$ 当 $h>k$，
准确有限卷积给
$$
\boxed{
J_{72,p}(k)=k!(72c)^{-k}\alpha_{dk}^{72},\qquad
J_{0,p}(k)=k!(2c)^{-k}\beta_{dk}.
}
\tag{15}
$$
特别参考系数全部非零，且
$$v_p(\beta_{dk})=-k-v_p(k!).\tag{16}$$

若直接使用物理 $\Phi_{24}$，其 sigma 首分母为
$c_{24}=\theta^d c$，正确 Gaussian 是 $72c_{24}$。
由 (2) 在每一个 Newton 系数上精确相消，
$$
\boxed{J_{\Phi_{24},p}(u)=C_{24}J_{72,p}(u).}
\tag{17}
$$
$C_{24}$ 在 (3) 全部为单位。
这同时支付曲线变量和 Gaussian，不能只把原系数换成 $s_m$
而仍使用底曲线的 $c$。

## 4. 共同整 signed 模与标准椭圆单位

本节把 R303 已证明的整比较用于新曲线，逐一列明改变的输入。
新旧来源的 degree 不进入这一步；实际 CM 曲线、导子和整微分进入。

### 4.1 完整局部格与同一反圆分权

因 $6\mid p+1$，$\mathbf F_{p^2}^\times$ 的六次幂子群包含
$\mathbf F_p^\times$。Hensel 提升给 $\theta=24^{1/6}\in\mathcal O^\times$。
实际整同构
$$
F_\theta:E_1\longrightarrow E_{24},\quad
(X,Y)\longmapsto(\theta^2X,\theta^3Y),\quad
F_\theta^*\omega_{24}=\theta^{-1}\omega_1
\tag{18}
$$
保持光滑整模型、形式群和完整 CM Tate 格，逆映射也整。

以 $\varpi_j=s_0\Omega_j$ 作真实 CM 格生成周期，
$\varpi_{24}=\varpi_1/\theta$。
选与 (18) 相容的原始 CM Betti/Tate 基。
两条 Hecke 角色的商为六次有限角色，
故当 $d\mid m$，同一个全局角色是
$$
\chi_m=(\psi_{24}/\bar\psi_{24})^m
       =(\psi_1/\bar\psi_1)^m .
\tag{19}
$$
其 $p$ 处 tame 指数 $(1-p)m$ 被 $p+1$ 整除条件消掉；
其余有限六次角色由 $6\mid m$ 消掉。
因此它处于同一反圆分 $\mathbf Z_p$ 塔，未改换分支。

取生成元 $\gamma_{\rm ac}$，
$q=\kappa_{\rm ac}(\gamma_{\rm ac})\in1+p\mathcal O$，
$v_p(q-1)=1$。评价点 $x_m=q^m-1$ 满足
$$v_p(x_{dk})=1+v_p(k).\tag{20}$$
反向 Artin 约定同时反演 $q$，只是整参数自同构。

### 4.2 参考类给真正整基

记 $T_j=T_pE_j$ 为秩一 $\mathcal O$-模，
$$M_j=\varprojlim_nH^1(\Psi_n,T_j^{-1}(1)),\qquad
\Lambda=\mathcal O[[T]].$$
BKO21 的 Rubin 局部分解及 BKO24 §2.2.1 给完整整直和
$$M_j=M_j^+\oplus M_j^-,\qquad M_j^\pm\simeq\Lambda.$$
(18) 与局部限制、corestriction、dual exponential 相容，
所以给两符号模的整同构。
这些是完整格，不是删有限模后的伪同构。

R389 已给新曲线根数正；参考 E1 的非零中央值也给正号。
两条标准椭圆单位局部类 $\xi_j$ 因而都在 $M_j^+$。
R302 的实际常数为
$$
L(E_1,1)/\varpi_1=(1-\omega)/6\in\mathcal O^\times.
$$
BKO24 Corollary 4.11(i) 的证明给该参考的 Rubin 函数为
$\Lambda^\times$，所以 $\xi_1$ 是原正号模的整基。
于是唯一存在
$$
\boxed{F_\theta^*\xi_{24}=\mathcal A_{24,p}(T)\xi_1,\qquad
       \mathcal A_{24,p}\in\Lambda,\quad\mathcal A_{24,p}\ne0.}
\tag{21}
$$
非零性来自 BKO21 的非零/特征理想结论。
原始 signed 基的改变只乘 $\Lambda^\times$。

这些定理的具体条件均满足：$K$ 类数一，两曲线为最大整环 CM
的有理曲线，$p\ge11$ 好惰性，且 $p\nmid h_K$。
新导子是 $(8\delta^4)$，有限射线类次数为 $432$；
六次扭转次数及此射线类次数均与当前 $p$ 互素。
wild 三端在这里是固定的 prime-to-$p$ 导子，
不需要把它替成旧 ground 三端。

## 5. 混合权的实际类、全部周期和非单位抵消

置
$$
\mathscr E_{j,m}=
\frac{(2\pi/\sqrt3)^mL(\psi_j^{2m+1},m+1)}
     {m!\varpi_j^{2m+1}} .
\tag{22}
$$
沿同一原标准类作混合权特化，R303 §4 的比较给
$$
\boxed{
v_p\mathcal A_{24,p}(x_m)
 =v_p\mathscr E_{24,m}-v_p\mathscr E_{1,m}
\qquad(m>0,\ d\mid m).
}
\tag{23}
$$
以下说明新曲线满足该比较的每一个具体输入，而不是从有限阶插值
直接跳到混合权。

两条曲线的 primitive 导子分别为 $(8\delta^4)$ 和 $(2\delta)$，
支撑都在二、三处。对各自完整 ray tower 的同一个椭圆单位系统，
先取 $T_j^{-1}(1)$ 再作反圆分特化，和先按高权 CM 基张量再作
cyclotomic 临界特化，最终均得到
$$
T_j^{-(2m+1)}(1+m),\qquad
\psi_j^{-(2m+1)}\chi_{\rm cyc}^{1+m}.
\tag{24}
$$
在原 CM 基 $b_j$、共同 Tate 基 $\zeta$ 下，两条路径的向量都是
$\mathbf u_j\otimes b_j^{\otimes(2m+1)}\otimes\zeta^{\otimes m}$。
norm、twist、特化和局部化交换。
Kato (15.16.1)、Theorem 12.5(1) 以
$k=2m+2,r_{\rm crit}=m+1$ 识别同一高权 CM 类。
使用其 §15.8/15.11 的两张定义性 period 图时，
中间 CM 新形式空间的缩放在两条路径间相消。
这里不使用 Kato §15.11 末尾未证明的高权 motivic 相容性；
使用的是 R303 已逐步证明的同一 ray 类及 CM 秩一张量比较。

为固定实际整除法，可取惰性辅助素数
$\ell\equiv1\pmod p$、$\ell\nmid6p$。
两条曲线都有 $\psi_j((\ell))=-\ell$，
辅助值在两路径同为 $\ell^2+\ell^{-1}\equiv2\pmod p$。
因此最后除辅助算子是整单位除法。
微分张量的比较为 $\theta^{-(2m+1)}$，也是单位；
canonical CM-pair 的导子幂及有限下降只含二、三与度数 $432$。
全部张量在秩一格上作，未引入对称幂投影的阶乘分母。

可能非单位的共同因子必须原样保留到取比：
Kato 临界 Tate 因子与 (22) 的比含 $(i\sqrt3)^m m!$；
两个 $m!$ 在高权可有正赋值，但彼此准确抵消。
在惰性好约化处两曲线均有 $\psi_j((p))=-p$，
故实际去 $p$ 因子都是
$$
\boxed{
1-\frac{(-p)^{2m+1}}{(p^2)^{m+1}}
 =1+\frac1p,\qquad v_p(1+1/p)=-1.
}
\tag{25}
$$
它也只在两边取比后消掉，不是单位。
$6\mid m$ 保持各自完整有限角色、uniformizer 值及 primitive 导子；
两个坏位集合相同，无额外删掉一个好位 Euler 因子。
参考值由 (15)–(16) 非零，故取比合法。这证明 (23)。

新曲线的全权平方是 R397 的
$$
\mathscr E_{24,m}=\frac{\kappa_{24}}{s_0}72^{-m}s_m^2,
\qquad
\mathscr E_{1,m}=\frac1{6s_0}2^{-m}\beta_m^2.
\tag{26}
$$
代入 (2)，其完整代数比为
$$
\frac{\mathscr E_{24,m}}{\mathscr E_{1,m}}
 =6\kappa_{24}C_{24}^2\,\theta^{2m}36^{-m}
      \left(\frac{\alpha_m^{72}}{\beta_m}\right)^2 .
\tag{27}
$$
再令 $m=dk$，由 (15)
$$
\frac{\alpha_{dk}^{72}}{\beta_{dk}}
 =36^k\frac{J_{72,p}(k)}{J_{0,p}(k)} .
\tag{28}
$$
此式同时保两个 $k!$ 和两个赋值负一的 Gaussian 常数。
所有 $\theta$、$36$、$C_{24}$ 在 (3) 下为单位，
$J_{0,p}(k)$ 也是单位，故 (23)–(28) 准确给
$$
\boxed{
v_p\mathcal A_{24,p}(x_{dk})
 =\Delta_p+2v_pJ_{72,p}(k),\qquad
\Delta_p:=v_p(6\kappa_{24}C_{24}^2)=v_p(\kappa_{24}).
}
\tag{29}
$$
没有假定剩余逐权单位随权解析，也没有删除固定 $\Delta_p$。

## 6. 消失阶与整个通常 Selmer 群

若 $J_{72,p}$ 恒零，(29) 将使非零
$\mathcal A_{24,p}$ 在 $x_{dp^n}\to0$ 的无穷点上为零，矛盾。
所以 $J_{72,p}\ne0$。
设 $r=\operatorname{ord}_0\mathcal A_{24,p}$，
$A_r=[T^r]\mathcal A_{24,p}$。
对充分大的 $n$，两边各自由首非零项支配，(20)、(29) 给
$$
v_p(A_r)+r(n+1)=\Delta_p+2v_p(j_e)+2en .
$$
比较 $n$ 的系数和常数项即得 (6)。
整性仅给
$$\Delta_p+2v_p(j_e)-2e\ge0;$$
式 (2a) 已在本篇全部素数支付 $\Delta_p=0$，所以这里进一步得到
$v_p(j_e)\ge e$。这个结论使用已证明的真实常数，而非先将其视为单位。

BKO21 Theorems 6.1–6.2 的通常 Selmer 控制在根数正、平凡角色
属于 $\Xi^+$ 时给
$$
\operatorname{corank}_{\mathcal O}
 \operatorname{Sel}_{p^\infty}(E_{24}/K)
 \le\operatorname{ord}_0\mathcal A_{24,p}.
\tag{30}
$$
此处是完整通常 Selmer，未只取 Mordell–Weil 子空间，
也不预设原高度非退化。

有理三同源
$E_{24}\to E_{24}^{(-3)}:y^2=x^3-648$
及其对偶复合为 $[3]$。
当前 $p\ne2,3$，三同源、限制/corestriction 和二次特征投影
都在完整 $p^\infty$-Selmer 群上保余秩。
因此
$$
\operatorname{corank}_{\mathbf Z_p}\operatorname{Sel}_{p^\infty}(E_{24}/K)
 =2\operatorname{corank}_{\mathbf Z_p}
       \operatorname{Sel}_{p^\infty}(E_{24}/\mathbf Q).
$$
而 $\mathcal O/\mathbf Z_p$ 度二，R398 的秩恰二及完整 Kummer 序列给
$$
\boxed{
\operatorname{corank}_{\mathcal O}\operatorname{Sel}_{p^\infty}(E_{24}/K)
 =2+\operatorname{corank}_{\mathbf Z_p}\Sha(E_{24}/\mathbf Q)[p^\infty].
}
\tag{31}
$$
由 (6)、(30)、(31) 得 (7)。
当 $J_{72,p}'(0)\ne0$，右边阶恰二，故 Sha 初级余秩为零；
通常 Selmer 及其 Sha 商余有限生成，余秩零因而给有限性。
这里没有主张初级群为零或这个充分条件的逆命题。

## 7. 指定首权与全深度的有限证书

由 (14)，$h\ge2$ 的 $a_h$ 至少被 $p^2$ 整除。
又 $A_{72}(0)=0$，所以 $[z^d]G_{72}=\alpha_d^{72}$。
因此在整 Tate 代数中准确有
$$
\boxed{
J_{72,p}(u)\equiv\frac{\alpha_d^{72}}{72c}u\pmod{p^2},
\qquad
\frac{J_{72,p}'(0)}p\equiv\frac{\alpha_{p+1}^{72}}{72pc}\pmod p.
}
\tag{32}
$$
结合 (2)、(10)，
$$
\boxed{
s_{p+1}\in\mathcal O^\times
\Longleftrightarrow \alpha_{p+1}^{72}\in\mathbf Z_p^\times
\Longleftrightarrow J_{72,p}'(0)/p\in\mathbf Z_p^\times
\Longrightarrow \Sha(E_{24}/\mathbf Q)[p^\infty]\text{有限}.
}
\tag{33}
$$
这里 $s_m$ 始终是原实际 $\Phi_{24}$ 的系数。
若 (33) 命中，Rubin 首项赋值为 $\Delta_p$；
由 (2a) 的 $\Delta_p=0$，这里可以进一步准确断言
$\mathcal A_{24,p}=T^2\Lambda^\times$。
对物理首项一来源 $T_{24}=\Phi_{24}/a_{24}$，同一常数也可写为
$\kappa_{24}a_{24}^2=10534551552=2^{15}3^8 7^2$，
没有新的惰性坏素数。

完整导数及严格尾界为
$$
\begin{aligned}
J_{72,p}'(0)&=\sum_{h\ge1}(-1)^{h-1}(h-1)!a_h,\\
L_{p,H}^{72}&=\sum_{h=1}^{H}(-1)^{h-1}(h-1)!a_h,\\
M_{p,H}&=
 \left\lceil\frac{(H+1)(p-1)+6}{2p}\right\rceil+v_p(H!),\\
v_p(J_{72,p}'(0)-L_{p,H}^{72})&\ge M_{p,H}.
\end{aligned}
\tag{34}
$$
最后一行由 (14) 加上 $(h-1)!$ 的赋值，且界随 $h$ 不减。
因 $M_{p,H}\to\infty$，
$$
\boxed{
J_{72,p}'(0)\ne0
\Longleftrightarrow
\exists H\ge1:\ v_p(L_{p,H}^{72})<M_{p,H}.
}
\tag{35}
$$
这对每个 (3) 的素数都是同一原 rank-two 曲线的完整有限证书；
首层失败不等同于完整导数为零。

完整失败还有一个便于联合使用的准确必要条件：
若 $J_{72,p}'(0)=0$，则
$$
\boxed{J_{72,p}\in p^2u^2\mathbf Z_p\langle u\rangle.}
\tag{36}
$$
因为常数项为零、一次项假设为零，而所有更高次系数均来自
$h\ge2$ 的 $p^2$ 项。因此对全部 $n\ge0$，
$$
v_p(\alpha_{dp^n}^{72})
 \ge 2n+2-p^n-v_p((p^n)!).
\tag{37}
$$
这只是同一完整失败的推论，不另给任意 theta 角列中央零。

## 8. 与原 S34 的全部角向进位

本节供同一个有限精度目标使用。
在同一 $E_1$ frame，R398 已证明
$$A_{72}=A_{34}H_{38},\qquad H_{38}(0)=1.$$
令
$$
G_{34}=A_{34}e^{-34cz^d},\qquad
G_{38}=H_{38}e^{-38cz^d}.
$$
整个 Gaussian 准确相加，故
$$
\boxed{G_{72}=G_{34}G_{38}.}
\tag{38}
$$
$H_{38}=\sigma^{38}xQ_4(X)(X^2+20X-8)$，
所以同样的实际解析表达给 $\|G_{38}\|_R\le1$。
在当前惰性范围 $p\nmid38$，相应 Newton 参考属于
$1+p\mathbf Z_p\langle u\rangle$；此处不赋予它新的 Hecke 身份。

置 $w=z^6$、$Z=w^s=z^d$，保所有 $s$ 个角：
$$
G_N(z)=\sum_{t=0}^{s-1}w^tG_{N,t}(Z).
$$
(38) 的中央角准确是
$$
\boxed{
G_{72,0}(Z)=G_{34,0}(Z)G_{38,0}(Z)
 +Z\sum_{t=1}^{s-1}G_{34,t}(Z)G_{38,s-t}(Z).
}
\tag{39}
$$
若 $b_{N,h,t}=[z^{dh+6t}]G_N$，
则新第 $h$ 个 Newton 系数的完整式为
$$
\boxed{
a_h^{72}=(72c)^{-h}
\left(
 \sum_{i+j=h}b_{34,i,0}b_{38,j,0}
 +\sum_{t=1}^{s-1}\sum_{i+j=h-1}
                 b_{34,i,t}b_{38,j,s-t}
\right).
}
\tag{40}
$$
所有 wrap 中项都在式内。
第一项即使只保中央角，也须使用 $(u)_{i+j}$ 的 Newton 权，
不等于两个 Newton 函数的普通乘积。
第二项不能仅因 $J_{34,p}'(0)=J_{72,p}'(0)=0$ 被逐列删除。

因此，在旧曲线也好约化的共同范围 $p\ne17$，
若两个原完整导数同时失败，可同时使用 R303 和本篇的完整失败条件，
并用 (38)–(40) 放入同一个带 Gaussian 的有限目标。
新增的合法零输入是 $A_{72}$ 本身；
$H_{38}$ 或任意 $A_{34}$ 乘子并未自动成为第三条零输入。

## 9. 与旧桥相比的实质改变及出处

本篇使用同一已证明方法，但新输入逐一不同：
原来源是 R398 的 $A_{72}$；完整物理标量为 $C_{24}$；
指数常数为 $72c$；真实 CM 平方权因子为 $72^{-m}$；
导子为 $(8\delta^4)$、有限 ray 次数 $432$；
固定平方常数在首项赋值中留下 $v_p(\kappa_{24})$。
参考类、两个共同阶乘及非单位 Euler 因子则准确按 §5 抵消。
没有将 ordinary prime-core 移到高度二情形。

已出版输入：

- A. Burungale、S. Kobayashi、K. Ota，
  *Rubin's conjecture on local units in the anticyclotomic tower at inert primes*，
  Annals of Mathematics **194** (2021), 943–966，
  Theorems 2.1、6.1、6.2。
  [出版页](https://annals.math.princeton.edu/2021/194-3/p08)；
  [作者机构存档](https://authors.library.caltech.edu/records/8svwt-jn031)。
- 同三位作者，*p-adic L-functions and rational points on CM elliptic
  curves at inert primes*，JIMJ **23** (2024), 1417–1460，
  §2.2.1、Proposition 3.1、Definition 3.13、Corollary 4.11(i) 的证明。
  [出版全文](https://catalog.lib.kyushu-u.ac.jp/opac_download_md/7330258/7330258.pdf)。
  其一般条件是 CM Q-curve、好惰性 $p$、$p\nmid h_K$；
  本篇的三端导子幂满足这些条件。
- K. Kato，*p-adic Hodge theory and values of zeta functions of modular
  forms*，Astérisque **295** (2004)，Theorem 12.5(1)、§15.8、
  Proposition 15.9、Lemma 15.11、(15.16.1)。
  [出版全文](https://www.numdam.org/article/AST_2004__295__117_0.pdf)。
  混合权的完整同类比较按 R303 §4 证明并在本篇逐项核新数据。

仓库的完整输入：
[R301](R301-jzero-inert-analytic-half-factor-and-exact-first-denominator.md)、
[R302](R302-jzero-original-degree-two-reference-and-exact-full-weight-square.md)、
[R303](R303-jzero-inert-full-selmer-period-comparison-and-central-criterion.md)、
[R389](R389-e24-primitive-wild-local-data-and-actual-hermitian-class.md)、
[R397](R397-e24-original-ordinary-square-and-full-selmer-bridge.md)、
[R398](R398-e24-actual-polynomial-six-sigma-source-and-original-central-comparison.md)。

全部局部估计、尺度、同一来源的全深度尾界及 (38)–(40) 都是统一证明。
本文不依靠新增素数扫描。现在仍须让 (35) 对无穷多个不同素数命中，
或用两条实际 rank-two 来源的完整联合关系证明同一无限集合上至少一条非零。


提交前 API main 为 $a7c64d69bcb0c02667767533f041389a98b19726$，两份 README blob 与已读版本相同。
当前无可用 shell；按根规矩八使用小文本 Contents API 提交，
这不是一次本地 git pull。
