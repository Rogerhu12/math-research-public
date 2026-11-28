# R1200：原 Igusa–Weil 相位的锁定及最高 packet 的有理配对算子

**现行范围更正（R1208，2026-11-28）：** 本文 canonical Igusa–Weil 相位、原有限算子及完整 SS 收缩均保持成立。§7 及依赖 R1199 (1199.30) 将该 SS 和写作完整 V_m(T*) 的接口遗漏 CM node 静态单位；旧正文相应左侧 V_m(T*) 现应读为 SS 部分。完整原对数在 [R1208](R1208-original-CM-node-boundary-and-corrected-highest-kernel-log.md) 中补足，准确为 −8·2^mν/binom(m,n)²。以下原 SS 算式和证明不重算，不能再把它单独称为全图值。

## 更正前正文（按上方现行范围读取）


日期：2026-11-28。会话：Astra-serre-24b8836b-20261126；global_route / root。

**已证明。** 本文使用原普通商的同一个 Cartier–Weil character、同一个刚化 Poincaré 线和原 full-level 参数，确定 R1199 中全部普通节点的相位。原相位 $\nu_s$ 是一个与 supersingular 点 $s$ 无关的明确单位 $\nu$。随后把 R1199 的完整有限收缩写成原 $b$ 坐标中的一个有理微分算子；它保留全部较低 log 次数与较高 normal 的交叉项。

对原 CM profile 的核 $T_*=(b^3-1)^{2g-1}$，同一 $P=(p-1)D_0$ 的完整首对数值成为一个没有独立节点相位的 supersingular 有限和。本文不证明该有限和非零或为单位，不把整 packet 换成指定非 CM 商的单 cuspidal 投影，也不把首层读数当作整个 $p$-adic 盘的排除。Serre 主目标仍 OPEN。

## 1. 原对象和规范

保持 R1021、R1023、R1028、R1196–1199 的原对象：
$$
p=12g-1>37,\qquad m=(p-1)/2=6g-1,\qquad
e_0=m(p+1),\qquad \pi_0^{e_0}=p.
$$
在 full-level 源取 $\varpi^2=\pi_0$，并保持原 Weil 根 $\zeta_p$。记
$$
r(b)=1-b^3,\qquad
E_b:\ y^2=x^3+3br(b)x+r(b)(1-2b^3),
$$
$$
t=-x/y,\qquad \omega=dx/(2y),\qquad \eta=x\omega,
$$
$$
h(b)=h_p(b)=r(b)^{2g}A(b),\qquad
S=\{s:A(s)=0\}.
\tag{1200.1}
$$
$A=A_p$ 是原 monic polynomial，$\deg A=m-1$，其根简单且 $r(s)\ne0$。

原 Igusa 坐标不是任意 Hasse 根。若 $Q$ 是原普通商给出的 $\ker V$ 生成元，令
$$
F:E_b\longrightarrow E_b^{(p)},\qquad
V:E_b^{(p)}\longrightarrow E_b
$$
为相对 Frobenius 及其对偶。由同一 $Q$ 给出的 Cartier 对偶 character
$$
\chi_Q:\ker F\longrightarrow\mu_p
$$
定义实际 Igusa 微分
$$
\chi_Q^*(dZ/Z)=\omega_{\rm Ig}
 =\mathfrak a_{\rm Ig}\omega,\qquad
\mathfrak a_{\rm Ig}^{p-1}=h,\qquad
u=\mathfrak a_{\rm Ig}^{\,2},\quad u^m=h.
\tag{1200.2}
$$
其 source/target 正是 Ulmer 的 Igusa 定义：$Q$ 位于 $E_b^{(p)}$，微分 $\omega_{\rm Ig}$ 位于 $E_b$。改变 Weil 配对的两个槽的顺序只将 character 取逆；本文会平方消去这个真实的符号，不引入任意 $\mathbf F_p^\times$ 归一。

在 $s\in S$，令
$$
B_s=2r(s)h'(s)=-b_F(s)\ne0.
\tag{1200.3}
$$
这里 $b_F$ 是 R1023 §5 的原 crystalline off-diagonal，规范为
$F_{\rm cris}(\eta)=b_F\omega+h\eta$。原 Gauss–Manin 连接为
$$
\nabla\omega=\frac{b^2}{2r}\omega+\frac1{2r}\eta,\qquad
\nabla\eta=\frac b2\omega-\frac{b^2}{2r}\eta.
\tag{1200.4}
$$

原 full-level eigenparameters $x,y$ 仍来自 $P,Q$ 的原形式参数；R1021 的平均保持在 supersingular 点的线性首项为 $1$。写 $x=\varpi\alpha,\ y=\varpi\beta$。在同一固定 Weil 分支，
$$
C_s=\alpha^p\beta-\alpha\beta^p,\qquad
A_s=-3C_s^2.
\tag{1200.5}
$$
为避免记号混淆，$A_s$ 是原 generic tail 的常数，$A(b)$ 是 supersingular polynomial。

R1199 保留的实际 node 参数是
$$
V=\frac{y^2-s_{\rm Car}^2x^2}{\varpi^2},\qquad
z=V^{-1},\qquad
W=\pi_0/z=y^2-s_{\rm Car}^2x^2,\qquad
s_{\rm Car}^2=-3.
$$
在普通 centre 上 $x=0$，故 $W=y^2$。原节点单位满足
$$
u=\tau_sW+\cdots,\qquad b-s=\theta_sW^m+\cdots,\qquad
\tau_s^m=h'(s)\theta_s.
\tag{1200.6}
$$
本文计算的是这同一个 $\tau_s,\theta_s$，不重新选择 plumbing 参数。

## 2. 同一 Poincaré 线的一阶计算

### 2.1 相对 Frobenius 固定测试基上的一阶参数

固定 $E_s$，在 $k[\epsilon]/(\epsilon^2)$ 上取
$Q\in E_s^{(p)}$，其实际参数 $q=t'(Q)=\epsilon$。在 supersingular 点，$dV=0$，因此这个一阶点属于 $\ker V$。刚化 Poincaré 线
$\mathcal O(Q-O)$ 的一阶 transition 是
$$
1\pm\epsilon/t'
\tag{1200.7}
$$
乘以一个由两开集上的正则函数给出的 coboundary；符号只取决于把该线还是其逆用于 character。

这里必须使用相对 $F$。椭圆曲线和它的 Frobenius twist 是测试基的常 family，相对 $F$ 固定 $k[\epsilon]/(\epsilon^2)$ 中的 $\epsilon$，而将曲线参数 $t'$ 拉回为 $t^p$。所以 (1200.7) 拉回为
$1\pm\epsilon/t^p$，绝不能把 $\epsilon$ 也升为 $p$ 次而使一阶类消失。

### 2.2 原 $\eta'$ 的 Čech primitive 固定绝对尺度

R1165 §1 的两开集 de Rham 代表为
$$
\eta'=
 \bigl(\eta',\ \eta'-t'^{-2}dt',\ t'^{-1}\bigr),
\tag{1200.8}
$$
总微分取 $\alpha_V-\alpha_U-dh$。因此相对 Frobenius 的模 $p$ 拉回恰由
$$
(0,0,t^{-p})
\tag{1200.9}
$$
表示。若用同一局部 primitive 的更长正则展开，其高次正则部分只改变 Čech coboundary；$t'^{-1}$ 的首系数是 $1$，没有额外的模型常数。

在 $s$ supersingular 时，$F$ 在 $H^1(\mathcal O)$ 上为零，故可取实际正则函数 $f_U,f_V$，使
$$
f_V-f_U=t^{-p}.
$$
另一方面，R1023 的原 crystalline 归一给
$$
[(0,0,t^{-p})]=-B_s\omega.
$$
减去总边界 $d(f_U,f_V)$ 后，
$$
(0,0,t^{-p})-d(f_U,f_V)
 =(-df_U,-df_V,0)=-B_s\omega,
$$
因而
$$
df_U=df_V=B_s\omega.
\tag{1200.10}
$$
这一步把原 $\eta'$ 的 primitive、相对 $F$、原 $b_F$ 和同一 Poincaré transition 联系起来。它不是仅从两个一维空间之间存在同构来推断某个非零常数。

由 $f_U,f_V$ 得到的 $F^*\mathcal O(Q-O)$ 的刚化平凡化，沿 $\ker F$ 平移后给 Cartier 对偶 character。其一阶对数微分由 (1200.10) 为
$\pm B_s\epsilon\,\omega$。因此
$$
\left.\frac{\mathfrak a_{\rm Ig}}q\right|_s=\pm B_s.
\tag{1200.11}
$$
同一 source eigenparameter $y=T(Q)$ 与 $q=t'(Q)$ 在 $s$ 的线性比为 $1$，这是 R1021 的实际线性首项归一。结合原定义 (1200.2)，得到
$$
\boxed{\quad \tau_s=B_s^2,\qquad
\theta_s=\frac{B_s^{p-1}}{h'(s)}.\quad}
\tag{1200.12}
$$
只在此平方后消去了真实的 $\pm$。若把 $\mathfrak a_{\rm Ig}$ 换成任意 $(p-1)$ 次根，(1200.11) 就不再是已证的规范身份，故不能用那种替换证明 (1200.12)。

## 3. 同一 Weil 根固定 $C_s$ 的平方

记
$$
\gamma=\overline{\frac{\zeta_p-1}{\varpi^{p+1}}}.
\tag{1200.13}
$$
沿原分支，$\gamma^{p-1}=-1$。由
$p=\text{unit}\cdot(\zeta_p-1)^{p-1}$，原 full-level 正则局部环中 $\zeta_p-1$ 的首齐次次数为 $p+1$。

其首齐次项在 $\mathrm{SL}_2(\mathbf F_p)$ 下不变。这个次数的不变量线由
$x^py-xy^p$ 生成：对角作用只留下
$xy^p,\ x^{m+1}y^{m+1},\ x^py$，两个基本 unipotent 作用迫中间项为零并使两个外项系数互为相反数。因此有实际单位 $\kappa_s$ 满足
$$
\zeta_p-1=\kappa_s(x^py-xy^p)
 +\text{更高次数项},\qquad
\kappa_sC_s=\gamma.
\tag{1200.14}
$$

现在以同一个 character 比较这个系数。原 Weil 配对的对偶相容为
$$
e_p(P,Q)=e_F(VP,Q)
\tag{1200.15}
$$
或其倒数，取决于同一固定槽序。$Q$ 在 $E_s^{(p)}$；$e_F(-,Q)$ 是 (1200.2) 的 character。沿 connected $P$ 方向求对数微分时，$V^*\omega=h\,\omega'$，所以系数为
$\pm h\mathfrak a_{\rm Ig}=\pm\mathfrak a_{\rm Ig}^p$。

由 (1200.11)，这个 source 参数中的最低 $y^p$ 系数是
$\pm B_s^p$。另一方面，对 (1200.14) 沿 $x$ 求微分，最低 $y^p$ 系数为 $\pm\kappa_s$。平方后得到
$$
\boxed{\quad
\kappa_s^2=B_s^{2p},\qquad
C_s^2=\frac{\gamma^2}{B_s^{2p}}.\quad}
\tag{1200.16}
$$
这一步保留了 source Frobenius twist：不能用 $B_s^2$ 代 $B_s^{2p}$。$\gamma$ 由全部节点共同的原 $\zeta_p,\varpi$ 固定；若运输到别的 Weil 分支，必须同时运输 $\gamma$。

## 4. 原节点相位成为同一个明确单位

令 $L=(m-1)/2$。R1199 中出现的是
$$
U_s=\frac{\theta_s^mA_s^L}{\tau_s}.
\tag{1200.17}
$$
代入 (1200.5)、(1200.12)、(1200.16)，逐项得到
$$
U_s=
 (-3)^L\gamma^{m-1}
 \frac{B_s^{m-1}}{h'(s)^m}
 =
 (-3)^L(2\gamma)^{m-1}
 \frac{r(s)^{m-1}}{h'(s)}.
$$
由于 $h'(s)=r(s)^{2g}A'(s)$ 和 $m-1-2g=4g-2$，
$$
\boxed{\quad
U_s=\nu\,\frac{r(s)^{4g-2}}{A'(s)},\qquad
\nu=(-3)^L(2\gamma)^{m-1}\in\mathbf F_p^\times.
\quad}
\tag{1200.18}
$$
所有 $s$ 的 $\nu_s$ 因而都是这个同一 $\nu$。这里没有遗漏 $r(s)/h'(s)$ 的有理因子，也没有使用不成立的 $h'(s)=r(s)^{m-1}$。

因为 $\gamma^p=-\gamma$ 且 $m-1$ 为偶数，$\nu$ 确在 $\mathbf F_p$ 中。又 $(-3)^m=-1$、$\gamma^{2m}=-1$，故
$$
\nu^m=1.
\tag{1200.19}
$$
这锁定的是原固定 Weil 分支上的单位；并非声称改变原 Weil 根后数值 $\nu$ 不变。

## 5. 完整收缩的 framing 不变性

保留 R1199 的参考权
$$
w_a=
 \frac{2(-1)^{m-a}(m-1)!}{(a-1)!(m-a+2)!}
 =\frac2{m(m+1)}(-1)^{m-a}\binom{m+1}{a-1},
\quad 1\le a\le m.
\tag{1200.20}
$$
令 $f_0,f_1$ 是同一 target Picard–Fuchs 方程
$$
f''-\frac{3b^2}{r}f'
 -\frac{b(5-4b^3)}{4r^2}f=0
\tag{1200.21}
$$
在 $b=s+t$ 的规范局部解，$f_0(0)=1,\ f_1(0)=0,\ f_1'(0)=1$。写
$\xi=f_1/f_0$，$J=\xi^{-1}$。

R1199 的全部收缩是
$$
\mathscr S_s(T)=\sum_{a=1}^m w_aD_{a,s}e_{m-a,s}(T).
\tag{1200.22}
$$
单个 $D_{a,s}$ 依赖原 opposite line；整个 (1200.22) 与其无关。此处直接消费 R1199 (1199.25) 的完整 opposite 不变性，包括端点和次数小于 $p$ 的多项式论证，不重做该结论。

因此以下有理算子可以在计算整个收缩时取 $f_0'(0)=0$；这不授权把 R1198 的任何单个原 $D_a$ 的初值独立改成零。

## 6. 原 $b$ 坐标中的有限微分算子

现在把 $b$ 当变量，令 $f_0(t),f_1(t)$ 为 (1200.21) 在 $b+t$ 的有限形式解，取
$$
f_0(0)=1,\ f_0'(0)=0,\qquad
f_1(0)=0,\ f_1'(0)=1,\qquad
\xi=f_1/f_0,\quad J=\xi^{-1}.
$$
所用次数都小于 $p$。令 $\lambda(b)=-6(b+1)/r(b)$，并定义
$$
D_a(b)=\frac1a[t^{a-1}]
 \lambda(b+t)\left(\frac t{\xi(t)}\right)^a,
$$
$$
\widetilde e_N(T;b)
 =[v^N]\,
 r(b+J(v))^{2g+1}T(b+J(v))f_0(J(v))^3.
\tag{1200.23}
$$
定义参考权规范下的算子
$$
\boxed{\quad
\mathcal P_m(T)(b)
 =r(b)^{m-2g-1}
  \sum_{a=1}^m w_aD_a(b)\widetilde e_{m-a}(T;b).
\quad}
\tag{1200.24}
$$

在 supersingular 点 $s$，$f_1(t)=h(s+t)/h'(s)$。Wronskian 恒等式给
$\xi'=r(s)/(r(s+t)f_0(t)^2)$。R1199 的
$K=(h(s+t)/(h'(s)\xi))^{1/m}$ 是 $f_0^{1/m}$；因为
$1-1/m=3$ 于 $k$，在当前全部次数小于 $p$ 的有限 jet 中，
$$
\mathcal E_{s,T}(t)
 =\frac{r(s+t)^{2g+1}T(s+t)f_0(t)^3}
        {h'(s)r(s)}.
$$
因此
$$
\boxed{\quad
\mathscr S_s(T)
 =\frac{r(s)^{2g-m}}{h'(s)}\,
   \mathcal P_m(T)(s).
\quad}
\tag{1200.25}
$$
这保持 (1200.20) 中的因子 $2/[m(m+1)]$。若另用无该因子的 binomial 收缩，必须同步改变外面的系数，不能混用两种 $\mathcal P$。

### 6.1 分母和次数的有限证书

方程 (1200.21) 的有限递推逐项给
$$
[t^n]f_0\in r^{-n}k[b]_{\le2n},
$$
$$
[t^n]f_1,\ [t^n]\xi,\ [v^n]J
 \in r^{-(n-1)}k[b]_{\le2n-2}.
$$
这是直接按方程中的 $r^{-1},r^{-2}$ 及 Taylor 次数归纳；每次反除的整数都不超过当前所需次数加一，因而是 $p$ 单位。由有限 Lagrange 反演，
$$
D_a\in r^{-a}k[b]_{\le2a-1}.
$$
进一步按 $T$ 的 Taylor 展开分离其导数，得到
$$
\widetilde e_N(T;b)=
 r^{2g+1-N}
 \sum_{j=0}^N r^j E_{N,j}(b)\frac{T^{(j)}(b)}{j!},
\qquad
\deg E_{N,j}\le2(N-j).
$$
代入 (1200.24) 后全部剩余 $r$ 分母相消：
$$
\boxed{\quad
\mathcal P_m(T)=
 \sum_{j=0}^{m-1}r^jP_{m,j}(b)\frac{T^{(j)}(b)}{j!},
\qquad
P_{m,j}\in k[b],\quad
\deg P_{m,j}\le2m-2j-1.
\quad}
\tag{1200.26}
$$
所有整数分母只来自 $2$ 及 $1,\ldots,m+1$，故 $p>37$ 下均可逆。特别当 $\deg T\le m-2$ 时，
$$
\deg\mathcal P_m(T)\le3m-3.
\tag{1200.27}
$$
这里是原同一个有限源的系数界，不是任意有理非零泛函的存在论。

## 7. 同一 CM 核向量的完整 MW 首列

置
$$
T_*(b)=(b^3-1)^{2g-1}=-r(b)^{2g-1},\qquad
c_m^0=(-1)^{(m-1)/2}\binom{m-1}{(m-1)/2}.
$$
R1199 已从实际相对 Picard transition、三个 CM 支及全部 generic normal 证明
$$
V_m(T_*)=-m c_m^0\sum_{s\in S}U_s\mathscr S_s(T_*).
$$
使用 (1200.18)、(1200.25) 和
$h'(s)=r(s)^{2g}A'(s)$，得到
$$
\boxed{\quad
V_m(T_*)=
 -m c_m^0\nu
 \sum_{A(s)=0}
 \frac{\mathcal P_m(T_*)(s)}
 {r(s)^{2g+1}A'(s)^2}.
\quad}
\tag{1200.28}
$$
$m,c_m^0,\nu$ 全部为单位。此处没有删去任何低次 log 与较高 normal 的交叉项，没有把三个 CM 支的消去推广到任意 $T$，也没有从 packet 投影自动得到指定单因子上的横截单位。

(1200.28) 是同一 $P=(p-1)D_0$ 与同一整 $\Omega_{T_*}$ 的完整首列。其右侧现在只含原 $A_p,r$ 和显示的有限算子，不再含彼此独立的节点根相位。

## 8. 全和的有理极部入口及精确未付处

记
$$
P_T=\mathcal P_m(T),\qquad
\mathscr R_T(b)=
 \frac{P_T(b)}{r(b)^{2g+1}A(b)^2}.
\tag{1200.29}
$$
在 $s\in S$，$\mathscr R_T$ 的双极系数正是
$P_T(s)/(r(s)^{2g+1}A'(s)^2)$。由 (1200.27)，在三个 $r=0$ 点极阶至多 $2g+1<p$，而在无穷处
$\mathscr R_T=O(b^{-5})$。这些是直接可检查的全局次数界。

原 supersingular polynomial 的方程为
$$
A''-\frac{4b^2}{r}A'-\frac{9b}{4r}A=0.
\tag{1200.30}
$$
将 (1200.29) 在每个 $s$ 展开，其简单极部为零当且仅当
$$
\boxed{\quad
r\,P_T'+m b^2P_T\equiv0\pmod A.
\quad}
\tag{1200.31}
$$
证明只需写简单极系数
$P_T'-(2g+1)(r'/r)P_T-(A''/A')P_T$，再用
$r'=-3b^2$、$A''(s)/A'(s)=4s^2/r(s)$ 和
$3(2g+1)-4=m$。

本文没有预先断言 (1200.31) 对 $T_*$ 成立，也没有仅从总 residue 为零推出双极系数之和为零。真正下一步是计算原有限算子对 $T_*$ 的这个余式及全和，或给出同源的微分恒等式；在此之前，(1200.28) 的单位性和指定 $C$ 上的结论均保持未付。


### 8.1 完整 supersingular 和的三次对称消去

只对本节的核向量 $T_*=-r^{2g-1}$，将原
$\lambda=-6(b+1)/r$ 分成
$$
\lambda_0=-6/r,\qquad \lambda_1=-6b/r,
$$
并分别以 (1200.23)–(1200.24) 定义线性算子值
$P_0=\mathcal P_m^{\lambda_0}(T_*)$、
$P_1=\mathcal P_m^{\lambda_1}(T_*)$。在含一个本原三次根 $\zeta$ 的剩余域中，
$r(\zeta b)=r(b)$、$T_*(\zeta b)=T_*(b)$，
而 (1200.21) 及其初值给出实际有限级数恒等式
$$
f_{0,\zeta b}(\zeta t)=f_{0,b}(t),\qquad
f_{1,\zeta b}(\zeta t)=\zeta f_{1,b}(t),\qquad
\xi_{\zeta b}(\zeta t)=\zeta\xi_b(t).
\tag{1200.32}
$$
因此对 $\epsilon=0,1$，
$D_a^{\lambda_\epsilon}$ 的权为 $\epsilon+1-a$，
$\widetilde e_{m-a}(T_*)$ 的权为 $-(m-a)$。因
$m\equiv2\pmod3$，整个已完成收缩满足
$$
P_\epsilon(\zeta b)=\zeta^{\epsilon+1-m}P_\epsilon(b)
                  =\zeta^{\epsilon-1}P_\epsilon(b).
$$
特别
$$
P_0\in b^2k[b^3],\qquad P_1\in k[b^3].
\tag{1200.33}
$$
原 $A(b)=bQ_p(b^3)$ 满足
$A(\zeta b)=\zeta A(b)$ 和 $A'(\zeta b)=A'(b)$，所以 (1200.28) 的分母沿每个非零三次轨道不变。$P_0$ 的轨道和为零；在固定根 $s=0$，(1200.33) 也给 $P_0(0)=0$。于是
$$
\boxed{\quad
V_m(T_*)=
 -m c_m^0\nu
 \sum_{A(s)=0}\frac{P_1(s)}
 {r(s)^{2g+1}A'(s)^2}.
\quad}
\tag{1200.34}
$$
这是真正完整配对之后的对称消去。它不把原某个节点的
$G(b_{\rm lift})^2$ 或单个 log 系数改成 $\lambda_1$，也不宣称被消去的 $P_0$ 在每个 supersingular 点的简单极部为零。剩余 $P_1$ 的简单极部判据及全和单位性仍由 (1200.31) 和 (1200.34) 准确保留。

## 来源与范围

1. Douglas L. Ulmer, *On Universal Elliptic Curves Over Igusa Curves* (1990), Invent. Math. 99, 377–391；[作者 PDF](https://dlulmer.github.io/research/papers/1990a.pdf)。Lemma 1.1 位于 PDF 第 2–3 页，给出 $\ker F$ 的 $p$-Lie algebra、Cartier duality 与 Hasse 规范；Igusa 生成元的 source 定义在第 3 页；Proposition 1.2 在第 4 页给原 $A=1$ 模型。本文的绝对一阶尺度另外由 §2 的原 Poincaré–Čech 计算支付，不从 Ulmer 的存在论自动补上。
2. [R1021：actual full-$p$ affine rigidity](R1021-actual-full-p-affine-tail-rigidity-and-quotient-parameter.md)：原 eigenparameter 的线性首项、full 非约化仿射图和普通商方向。
3. [R1023：原完整 first-log vector](R1023-original-CM-divisor-complete-first-log-vector.md)，§5：同一 $(\omega,\eta)$ 中的 $b_F=-2rh'$ 和原固定 Weil 分支。
4. [R1028：原 Igusa Kummer model](R1028-original-Igusa-Kummer-model-and-same-order-CM-jet-correction.md)：实际 $\omega_{\rm Ig}$、$u=\mathfrak a_{\rm Ig}^2$ 与 $u^m=h_p$。
5. [R1164：pointed Miller coefficients](R1164-original-pointed-Miller-coefficients-and-Cech-symbols.md)；[R1165：原整 residue contraction](R1165-original-integral-residue-contraction-and-log-PD-cone.md)，§1：同一 Poincaré 刚化和 $\eta$ 的 $(\eta,\eta-t^{-2}dt,t^{-1})$ 代表。
6. [R1198：原 ordinary quotient period jets](R1198-original-ordinary-quotient-period-jets-and-finite-log-source.md)：target 周期比、Frobenius twist 方向及实际 $G(b_{\rm lift})^2$ 的全部有限 log。
7. [R1199：完整 generic pairing 与 kernel log](R1199-original-highest-packet-complete-generic-pairing-and-kernel-log.md)：全部 normal、原参考权、完整 framing 不变性、三个 CM 支的实际消去及未简化全和。

全文是纸面证明；未运行本地数学程序。原主目标及 whole-disc 比较没有在本文中被宣布完成。
