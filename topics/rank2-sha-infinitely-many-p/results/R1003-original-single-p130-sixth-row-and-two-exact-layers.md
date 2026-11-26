# R1003 — 原 B130 的单 P130 第六行、真实三次零与两层 exact

日期：2026-11-26 UTC。**已证明：对 R999 的原 $\mathcal B_{130}$，可以把第六 Cartier 中的 $P_2^{65}$ 准确换成同一初始化的单个 $P_{130}$。替换后的整个三次 Cartier 确实为零，因此第六读数的32级第三层可用两个完整 exact 层取代。** 下面同时把这个改写准确接入 R989 六位中央的最后一项，保持原前五项和低卷积。

这里没有给 $\mathcal C\eta$ 或 $\mathcal B$ 的中央导数赋零。这个替换只先支付指定第六读取的模 $p$ 身份；它不把整个 ordinary 测度、任意高轴 family 或完整模 $p^6$ 中央换成一个新有理模型。

## 1. 原固定来源及可用的二十维子空间

沿 R999–R1001 的同一个 $E_1:y^2=x^3+1$、$X=x^3$、原微分、sigma 及 $Z,G,P_2$。固定好惰性 $p=6s-1>211$，记

$$
\mathcal B=120\Phi_{260}-11\Phi_*-108\mathcal X_{130}-F_{10}
=\sigma^{130}R_{\mathcal B},\qquad
R_{\mathcal B}=x^2P_{\mathcal B}(X).
\tag{1}
$$

已经支付的完整数据是

$$
\deg P_{\mathcal B}=19,\quad
P_{\mathcal B}\in35^{-1}\mathbf Z[X],\quad
(X+1)^2Q_2\mid P_{\mathcal B},\quad
\mathcal B=24768z^{12}+O(z^{18}).
\tag{2}
$$

特别 $R_{\mathcal B}$ 在 $O$ 仅有118阶极，且在三个非零二挠点均至少四阶零。

同一比较也适用于原准确子空间

$$
V_{130}^{\ge12}
=\sigma^{130}x^2k[X]_{\le19}\subset V_{130},\qquad \dim=20.
\tag{3}
$$

在原全部22列中，(3)要求质量列 $u_{21}=0$、六阶列 $u_{20}=0$。因此下面的第六读取替换**不覆盖整个22维空间**。除 $\mathcal B$ 外，R993/R992 的 $G_{65},G_{\mathcal X},G_{\rm old}$ 都在(3)，但不借此给其中央导数新增零。

## 2. 同一原初始化的 P130

定义

$$
\nabla_{130}=D-130G,\qquad
P_{130}=-\nabla_{130}^{p-1}Z^{p+129}.
\tag{4}
$$

这正是 R887 §15 对 $m=130<p$ 的原有限表达式。原 $p$ 曲率及方程是

$$
\nabla_{130}^p=-130H^p,\qquad
\nabla_{130}P_{130}=130H^pZ^{p+129},\qquad H=G+x^2/y.
\tag{5}
$$

既没有重新选 $G$，也没有添加局部水平解。R887(70)在同一原点及整窗给

$$
P_{130}-P_2^{65}=O(Z^{6p+130}).
\tag{6}
$$

对每个 $f\in V_{130}^{\ge12}$，其 $R_f$ 在 $O$ 极阶至多118，所以

$$
\boxed{(P_{130}-P_2^{65})R_f=O(Z^{6p+12}).}
\tag{7}
$$

原第六读取只用 $Z^{6p+6}$ 系数。因此

$$
\boxed{
\mathcal T_6(f)
=[Z^{6p+6}]P_2^{65}R_f
=[Z^{6p+6}]P_{130}R_f
\quad(f\in V_{130}^{\ge12}).}
\tag{8}
$$

这一次是真正支付了目标系数：余阶(7)严格高于第六位，而不是只知道它不影响前五位。若 $u_{20}\ne0$，相应余阶只能保证 $6p+6$，不能使用(8)；若还保留质量列，余阶更低。

### 2.1 准确的原 p 基实现

保持 R1001 的 $K/K^p$ 有序基 $1,Z,\ldots,Z^{p-1}$，$q=Z^p$。令 $\mathsf A_{130}$ 为原 $D-130G$ 的完整矩阵，则

$$
\boxed{[P_{130}]_{\rm vec}
=-q\,\mathsf A_{130}^{p-1}e_{129},\qquad
\mathsf A_{130}^p=-130H^pI.}
\tag{9}
$$

因为 $129<p$，$e_{129}$ 是原基的合法固定列。全部乘法仍按 $Z^p=q$ 折回；(9)不除以 $H$。

若 $P_{130}R_f=\sum\widetilde\beta_j(f)Z^j$，则与 R1001 同样逐坐标得到

$$
\boxed{
\mathcal C\bigl(Z^{-7}P_{130}R_f\omega_E\bigr)
=\widetilde\beta_6(f)^{1/p}\frac{\omega_E}{Z},\qquad
\widetilde\beta_6(f)
=-q e_6^t\mathsf M_{R_f}\mathsf A_{130}^{p-1}e_{129}.}
\tag{10}
$$

这是一个原矩阵幂和一个完整来源乘法，不再使用 $\mathsf M_{P_2}^{65}$。式(8)等价于两份实际第六坐标的指定 $Z^{6p}$ 系数相同；没有宣称两个完整坐标函数或两个整体 Cartier 输入相同。

## 3. 所有移动零点准确消去，整个三次 Cartier 为零

置

$$
\widetilde\eta_6(f)=Z^{-7}P_{130}R_f\omega_E.
\tag{11}
$$

对 $f\in V_{130}^{\ge12}$，在 $O$，$P_{130}$ 的阶为130，故(11)阶至少五。若 $Q\ne O$ 是任何其它 $Z$ 零点，(4)含有 $Z^p$ 因子，剩下有限表达式在该点正则，所以

$$
\operatorname{ord}_Q\widetilde\eta_6(f)\ge p-7>0.
\tag{12}
$$

这里正是 $Z^{-7}$ 与 R887 §15 的 $Z^{-p-2}$ 不同之处：后者会留下额外极，本篇(12)已逐点将其排除，不能沿用后者的补项，也不能把本篇结论迁回那个不同的 weight。

原单因子帽是

$$
(P_{130})_\infty
\le(p^3-p^2+129p+1)\mathcal D_2,
\tag{13}
$$

其中 $\mathcal D_2=E[2]\setminus\{O\}$。对新 $\mathcal B$，再用(2)得到全部极阶至多

$$
\boxed{d_{\mathcal B,p}=p^3-p^2+122p-3<p^3.}
\tag{14}
$$

所以(11)只有原三个二挠极，三次 Cartier 后每处至多简单。对整个(3)，把(14)中的 $-3$ 改为 $+1$ 仍严格小于 $p^3$，结论同样成立。

输入对原 $\mu_6$ 不变，Cartier 与该实际自同构相容。输出无 $O$ 极，三个二挠点的留数因对称而相同，总和为零；$p>3$ 故每一个留数均为零。输出因而为全局正则微分，但原 $\mu_6$ 不变部分的正则微分空间为零，因为 $\omega_E$ 是型一。由此得到整个有理微分身份

$$
\boxed{\mathcal C^3\widetilde\eta_6(f)=0
\qquad\text{对每个 }f\in V_{130}^{\ge12}.}
\tag{15}
$$

没有只在一个点或一个 jet 赋零。

## 4. 新 B 的两个完整 exact 层

在同一个 $t=-x^{-3}$、$Y=(t-1)^{-1}$ quotient 上，(11)只在 $t=1$ 有极，$t=0,\infty$ 正则。其准确下游极帽是

$$
\widetilde L_p=\frac{p^3-p^2+122p-2}{2}.
\tag{16}
$$

用原固定函数定义唯一的完整主部

$$
\widetilde\eta_6(\mathcal B)
=\sum_{k=1}^{\widetilde L_p}
      \frac{\widetilde b_{k,p}}{(t-1)^k}dt,
\qquad \widetilde b_{1,p}=0.
\tag{17}
$$

系数由(4)、(11)、(1)完整规定，不能用 R1001 的旧 $b_{k,p}$ 替换它们。

令

$$
\widetilde A_0(Y)=\sum_{j=1}^{\widetilde M_0}
 \widetilde b_{1+jp,p}^{1/p}Y^{j-1},\qquad
\widetilde A_1(Y)=\sum_{j=1}^{\widetilde M_1}
 \widetilde b_{1+jp^2,p}^{1/p^2}Y^{j-1},
\tag{18}
$$

其中

$$
\boxed{\widetilde M_0=\frac{p(p-1)}2+60,
\qquad \widetilde M_1=\frac{p-1}{2}.}
\tag{19}
$$

它们分别是 $\lfloor(\widetilde L_p-1)/p\rfloor$ 和
$\lfloor(\widetilde L_p-1)/p^2\rfloor$；由于
$\lfloor(\widetilde L_p-1)/p^3\rfloor=0$，没有第三多项式 $\widetilde A_2$。

定义

$$
\widetilde H_0(Y)=
\sum_{\substack{1\le j\le\widetilde M_0\\p\nmid j}}
 \frac{\widetilde b_{1+jp,p}^{1/p}}j
       \{Y^j-(-1)^j\},
$$

$$
\widetilde H_1(Y)=
\sum_{j=1}^{(p-1)/2}
 \frac{\widetilde b_{1+jp^2,p}^{1/p^2}}j
       \{Y^j-(-1)^j\}.
\tag{20}
$$

所有显示除数均为单位。两多项式在 $Y=-1$ 的值为零，只是固定原点常数；其导数不能据此赋零。逐项得

$$
\boxed{\widetilde A_0=\widetilde H_0'
       +Y^{p-1}(\widetilde H_1')^p,\qquad
\mathcal C\widetilde\eta_6
=-\widetilde A_0dY,\qquad
\mathcal C^2\widetilde\eta_6=-d\widetilde H_1.}
\tag{21}
$$

所以三次零(15)在这里是 $\mathcal C(d\widetilde H_1)=0$ 的完整原函数身份，而不是把第一 Cartier 已经设零。

由 $dY/\omega_E=6z^5+\cdots$ 和(8)，真正的原第六读数准确为

$$
\boxed{\mathcal T_6(\mathcal B)
=-6\left\{\widetilde H_0'(-1)^p
                 +\widetilde H_1'(-1)^{p^2}\right\}.}
\tag{22}
$$

### 4.1 原第三层是被完整搬运，不是单独赋零

若仍用 R1001 的原 $P_2^{65}$ 输入及其 $H_0,H_1,A_2$，(8)给

$$
\boxed{
A_2(-1)^{p^3}
=\bigl(\widetilde H_0'(-1)-H_0'(-1)\bigr)^p
 +\bigl(\widetilde H_1'(-1)-H_1'(-1)\bigr)^{p^2}.}
\tag{23}
$$

因此本篇并未声称 $\mathcal C^3\eta_6(\mathcal B)=0$ 对旧输入成立，也未将旧 $A_2$ 本身置零。它们的影响已由真实不同的两个 exact 多项式承担。完整差
$Z^{-7}(P_{130}-P_2^{65})R_{\mathcal B}\omega_E$
在 $O$ 至少 $6p+5$ 阶，故恰不影响原第六 jet；其全局其它系数继续存在。

## 5. 与原 Gaussian 第六项的准确拼接

保持 R989 的所有原记号

$$
w=z^6,\quad c=[w^s]\log(\sigma/z),\quad
\kappa=34c,\quad a=p\kappa\in\mathcal O^\times,
\quad q=65/17.
\tag{24}
$$

于是 $q\kappa=130c$，没有改首 Gaussian。写

$$
B_{\mathcal B}=w^{-1}\mathcal B e^{-q\kappa w^s}.
$$

由完整 degree19 分子，若 $P_{\mathcal B}=\sum_{i=0}^{19}p_iX^i$，则

$$
\boxed{B_{\mathcal B}
=f^{-65}\sum_{i=0}^{19}p_i w^{20-i}W^{2+3i},
\quad W=z^2x,\quad f=e^{-2(\log(\sigma/z)-cw^s)}.}
\tag{25}
$$

所有 $w$ 幂至少一，所有 $W$ 幂至少二，固定分母仅35。因此 R989 的同一 Hurwitz、整窗口、两个端点及完整无限尾逐项适用，尽管 $B_{\mathcal B}$ 的常数项为零。令

$$
C_{\mathcal B,h}(0)=[w^{hs-1}]B_{\mathcal B},\qquad
F_{\mathcal B}^{[6]}(0)
=\sum_{h=1}^6\frac{(-1)^{h-1}(h-1)!p^{h-1}}
                       {q^h a^{h-1}}C_{\mathcal B,h}(0).
\tag{26}
$$

R989 的整个原尾给

$$
F_{\mathcal B}^{[6]}(0)
\equiv\frac apJ'_{\mathcal B,p}(0)\pmod {p^6}.
\tag{27}
$$

同时

$$
g_{\mathcal B,6}=C_{\mathcal B,6}(0),\qquad
a^+_{\mathcal B}=[w^{s+1}]\mathcal B e^{-130cw^s}
=[w^s]B_{\mathcal B}.
\tag{28}
$$

式(25)从 $w$ 起，因此最后一个量只用严格低于 $s$ 的原 $U_\sigma,W$ 输入；没有隐含一个未消的第 $s$ 个 sigma 系数。R711/R999 的准确剩余是

$$
\boxed{\overline{C_{\mathcal B,6}(0)}
=-6\left\{\widetilde H_0'(-1)^p
            +\widetilde H_1'(-1)^{p^2}\right\}
 -7\kappa_5\overline{a^+_{\mathcal B}},
\qquad \kappa_5=(3/5)^p/c_p.}
\tag{29}
$$

共同 $\eta_p$ 与第五行常数因真实 $c_6=0$ 消失；低卷积(28)没有消失。

## 6. 只替换真实第六位，保留前五项全部精度

第六项在(26)的系数为 $-120p^5/(q^6a^5)$，所以它只需(29)的模 $p$ 值。对(29)中剩余域元素取任意整提升；不同提升乘 $p^5$ 后相差 $p^6$，不会引入新的选择。得到真正的六位身份

$$
\boxed{\begin{aligned}
F_{\mathcal B}^{[6]}(0)\equiv F_{\mathcal B}^{[5]}(0)
 +\frac{p^5}{q^6a^5}\bigg[&720\left\{
   \widetilde H_0'(-1)^p+\widetilde H_1'(-1)^{p^2}\right\}\\
 &+840\kappa_5\overline{a^+_{\mathcal B}}\bigg]
\pmod {p^6}.
\end{aligned}}
\tag{30}
$$

这里 $F^{[5]}$ 指(26)的真实前五项，仍读到模 $p^6$ 所需的全部精度；不是只知道其模 $p^5$ 类后任意提升。没有将任意高轴 $x$ 的扰动来源替换为 $P_{130}$，(30)只用实际点 $x=0$；若某个已付必要系统把其指定点强制为 $0\bmod p^6$，再按该系统的原整多项式同余消费它。

在两 canonical 坏中央假设下，R999 的精确值给

$$
\boxed{F_{\mathcal B}^{[6]}(0)
\equiv-\frac{\delta a(p+1)}{10080p}
                       \log_p(\pi/\bar\pi)\pmod {p^6}.}
\tag{31}
$$

右侧是实际整量，因为该单位的对数属于 $p\mathcal O$。这不保证其六位截断非零；不能把非零对数自动当成赋值小于六。真实随 $p$ 的 Lucas 深度预算由 R1000 支付，后续必须用相应的全位精度。

## 7. 已支付的节省与后继必须保留的项

相比 R1001 的 $P_2^{65}$ 全22算子，本篇在真实子空间(3)保第六读取后，把二挠极帽的首系数从65降为1，第三 Cartier 的32个 sparse 行真正改成零，第一、第二 exact 多项式的长度分别降至
$p(p-1)/2+60$ 与 $(p-1)/2$。这些都是原完整来源的准确界。

式(22)、(29)、(30)仍有两个明确的 exact 导数、严格低卷积和原五项。它们不能由三次零(15)再赋零。已知非零的(31)也没有被写成一个新的 canonical 非零结论。

本篇没有数学执行、素数扫描或生成系数文件。全部身份来自原指定有限算子、R999 的实际 degree19/双二挠因子以及显示的完整 Cartier 读取。接续需要把(30)的这些真实项与 R1000/后继同一高轴校准和全位强迫联立；仅有模 $p$ 的模型节省不删改原六位的其它除 $p$ 成本。

## 依赖

- R887 §§14–15、19：原全部 $p$ 曲率、$P_m$ 初始化、极帽和准确第一乘法缺陷。
- R711、R989：同一个第六 Gaussian、实际低卷积、整六位前五行及整个尾。
- R999：固定 $\mathcal B_{130}$ 的完整分子、首阶、二挠双因子和非零中央。
- R1001：准确第六 $p$ 基坐标、整个主部返回与保两层 exact 的原有限部。
- R1000：原对数的 Lucas 深度及与同一全位预算的比较范围。
