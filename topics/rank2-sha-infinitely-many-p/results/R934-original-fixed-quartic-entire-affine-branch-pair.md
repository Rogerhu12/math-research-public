# R934 固定原 quartic 的整段仿射双 jet：实际 −11 尾与既定基点

日期：2026-11-20。**状态：完整符号证明；root 全文核 R928 原式及全部窗口，theta 独立全文审查，无数学执行。**

R824 及 R872 的同修正后继已给原 quartic 的 −11 首法向项。本注不重新登记该首常数，而在 R928 的负 fringe 全 J 窗口求出整个固定双 jet，并把任意既定 R_b 的偏移写成原 P 的两条真实除 p 分支读数。xi 在这两个整段中退出是完整逆 Taylor 和准确精度的结果，其它 normal 及受限 S 中的 xi 仍保留。

## 1. 原输入与严格范围

保 R928 的同一个原整 M、完整 WD、P134、十九角、总 charge 四十、三十九 carry 及短块。用相对源坐标写固定整 P 的约化：
\[
\bar P=t^{r_{\rm src}}F^4q\in\overline{\mathcal W}_D,\qquad
F(t(w),\bar g(w))=w^hu(w),\qquad u_0e_0q_0\ne0.
\tag{1}
\]
g 是原实际 regularized 轴，E=Y∂Y，e=EF 的同轴值。F、q 只带原固定 d(t)=1+8t 分母，在原点正则。返回必须使用同一个 q：
\[
\jmath(G)=qt^2G,\qquad G\in\mathcal H_3=H^0(X,\mathcal O_X(3C)),\qquad C=(F=0).
\tag{2}
\]
加入 R928/R920 的全部原几何及强窗，特别
\[
p=6s-1>211,\quad J=s-2,\quad T=J-13,\quad L=\ell-2>0,
\quad T-h\le L\le h,\quad2h+L>J.
\tag{3}
\]
本注取 R930 同 q 负 fringe 的明确范围
\[
\boxed{s=2h+d_0+2,\quad1\le d_0\le13,\quad h>21,\quad
\tau=r_{\rm src}+2h-s\ge0.}
\tag{4}
\]
d0=−delta 是 fringe 宽度，不是角多项式 d(t)。因此
\[
r_{\rm src}=\tau+d_0+2\ge3,\qquad J=2h+d_0,\qquad3h-2>J.
\tag{5}
\]
源指数 r_src 不换成返回指数 2。尤其 R872 的最小 r_src=3、tau=1 给 delta=0，不在 (4) 内。

固定允许的一阶修正陪集
\[
\bar R_b+\jmath(\mathcal H_3).
\tag{6}
\]
R_b 是这个已指定陪集的原整代表，不为消去偏移另选不同陪集。

## 2. 同一 P 的字面重记账与固定 B

按 R491 选择真正同预算的因子基准
\[
P^{\rm fact}=t^{r_{\rm src}}\widetilde F^{\,4}\widetilde q
\in\mathcal W_D,\qquad P^{\rm fact}\bmod p=\bar P.
\tag{7}
\]
F 带 d 分母时，先作 R932 §1 的中间 d-primitive 清分母，再在整提升后撤回，保持原 F、q、u、e 规范。定义
\[
D=\frac{P-P^{\rm fact}}p\in\mathcal W_D,\qquad R_b^\flat=R_b+D.
\tag{8}
\]
P+pR=P^fact+p(R+D) 是同一整向量的恒等式，未丢掉 D 的原下一位。

只在原点邻域定义固定 Laurent germ
\[
\boxed{B(t,Y)=\frac{\bar R_b^\flat(t,Y)}{q(t,Y)t^2}.}
\tag{9}
\]
q(0,1) 为单位，所以 B 及其有限个 E 导数最多有 t^(−2) 极。B 未必属于 H3，不能因 (9) 局部有定义就令其全局类为零。

R928 的四个低 t² 整除门仍须先核。通过后，实际四目标是下节自然目标减去同一个 E^iB(t,g)，不是四个独立局部参数。

## 3. 完整消去原公共框与 q 的真实四行

在原有限整窗口写
\[
\widetilde F(t(w),g(w))=w^hu(w)+p\xi(w),\qquad
\xi=[\widetilde F(t(w),g(w))]_{<h}/p.
\tag{10}
\]
记 A(w)=t(w)^(r_src−2)，e_k=(E^kF)(t(w),bar g(w))、e=e1。以下先作真正的 (10)，再约化；xi 不另选。

对 (7)，执行 R928(9) 的全部除 p 与 s 阶移位，再按其 (16)–(17) 消去 U^act、共同 t² 和 q 的完整 Euler 三角矩阵。所得自然目标为
\[
\boxed{\begin{aligned}
f_0^*&=0\pmod{w^J},\\
f_1^*&=-\frac1a A w^{4h-s}u^4\pmod{w^J},\\
f_2^*&=-24A w^hu\xi e^2-\frac8a A w^{3h-s}u^3e\pmod{w^J},\\
f_3^*&=-24A\xi e^3-\frac{36}a A w^{2h-s}u^2e^2
       -\frac{12}a A w^{3h-s}u^3e_2\pmod{w^L}.
\end{aligned}}
\tag{11}
\]
tau=0 或 1 时，末式允许最低幂 tau−2；这只是未通过 t² 低行门前的自然 Laurent 目标。必须先减去固定基点、检验负幂全部消失，不能先把负幂删除。

### 3.1 q 的全部导数与四十为何真正相消

引入只到三次的形式 Euler 变量 z。完整源 jet 为
\[
\exp(z(E+40))(qH)=e^{40z}q(t,Ye^z)H(t,Ye^z).
\tag{12}
\]
R928(9) 中 i/a 倍前一 Euler 行，在指数生成函数中就是乘 z/a。当前 W0、W1、W2 的约化首阶均至少 s，所以其真实 s 阶移位等于 w^(−s) 倍全式，没有漏掉前 s 项。乘 (12) 的原单位逆后，公共框、q 的全部 Euler 项和四十一起准确消去，留下
\[
-\frac{A\,E^i(\widetilde F^4)(t,g)}p
-\frac{i}{a}A w^{-s}E^{i-1}(F^4)(t,\bar g)
\quad(0\le i\le3)
\tag{13}
\]
的已付前缀；i=0 的第二项定义为零。第一商只在被 p 整除的有限前缀取商；其整性由
r_src−2+(4−i)h≥J（i≤2）及 r_src−2+h≥L（i=3）支付。

完整乘积式
\[
\begin{aligned}
E(F^4)&=4F^3e,\\
E^2(F^4)&=12F^2e^2+4F^3e_2,\\
E^3(F^4)&=24Fe^3+36F^2ee_2+4F^3e_3
\end{aligned}
\]
给 (11)。第三长行的其它一次 xi 项从 r_src−2+2h=J+tau 起；第四短行的其它一次 xi 项从 r_src−2+h=h+tau+d0≥L 起。较高整数字乘的未除 p 项本在窗口外。末式的 e2 carry 项仍保留，它可能在原短窗内存在。

对固定 (6) 作 R928 的同一线性减法，得到
\[
\boxed{f_i=f_i^*-(E^iB)(t,g).}
\tag{14}
\]
前三式按 J、末式按 L；只有在低行门通过后才将它们作为整幂级数目标。

## 4. 全 J 双 jet 的实际值

令 Y=psi(t) 是 F=0 通过原点的同一光滑支，g=psi exp(eta)。在原有限 Taylor 窗口，
\[
\eta=\frac{w^hu}{e}+O(w^{2h}),\qquad\operatorname{ord}\eta=h.
\tag{15}
\]

**定理 1。** 通过原低行门后，固定 (6) 的整个双 jet 恰为
\[
\boxed{j_0^P=-B|_C\pmod{t^J},\qquad
j_1^P=\mathcal T_P-(EB)|_C\pmod{t^J},}
\tag{16}
\]
其中完全指定的原 forcing 是
\[
\boxed{\mathcal T_P(t)=-\frac{11}{a}\,
t^{r_{\rm src}-2}w(t)^{-s}F(t,\bar g(t))^4\pmod{t^J}.}
\tag{17}
\]
除了固定 P 的基点 (9)，该式不再含 xi 或合法 factor lift 的其它数字。

**证明。** 先看自然目标。R928 的
j0*=f0*−eta f1*+eta²f2*/2 中，carry 项从 3h+tau−2>J 起，xi 项更高，所以 j0*=0。

对 j1*=f1*−eta f2*+eta²f3*/2，两个 xi 主项合为 12A w^(2h)u²xi e，其首阶至少
\[
r_{\rm src}-2+2h=J+\tau\ge J.
\tag{18}
\]
eta−w^hu/e 引入的 carry 误差、以及 (11) 的 e2 项乘 eta²，均从
\[
r_{\rm src}-2+5h-s=3h+\tau-2>J
\tag{19}
\]
起。余下同一 A w^(4h−s)u⁴ 的系数是
\[
-\frac1a+\frac8a-\frac{18}a=-\frac{11}a.
\tag{20}
\]
这付清 (17) 的整个前缀，非只首项。短 f3 的未知尾乘 eta² 从 2h+L>J 起，未给短块免费加长。

B 及 E^iB 至多有二阶 t 极，所以其有限逆 Taylor 的三次余项从 3h−2>J 起。于是
\[
\begin{aligned}
B|_C&=B(t,g)-\eta EB(t,g)+\eta^2E^2B(t,g)/2\pmod{t^J},\\
(EB)|_C&=EB(t,g)-\eta E^2B(t,g)+\eta^2E^3B(t,g)/2\pmod{t^J}.
\end{aligned}
\tag{21}
\]
与自然式相减即得 (16)。低行门通过时左边是整 jet，因此 B|C、EB|C 的负幂也确已消失；未在门通过之前默认这项整性。证毕。

## 5. 固定 B 的两条实际除 p 读取

取 (7) 中 F̃ 的同一原 Hensel 支 psĩ(t)，满足 F̃(t,psĩ)=0、psĩ(0)≡1 mod p。e0 为单位，故该支在原 p 进系数环中存在唯一。P 的约化含 F⁴、EP 的约化含 F³，因而
\[
b_0^P=\overline{P(t,\widetilde\psi(t))/p},\qquad
b_1^P=\overline{(EP)(t,\widetilde\psi(t))/p}
\tag{22}
\]
是实际整商，并分别等于 D|C、(ED)|C。令 q_C=q|C，则固定地有
\[
\boxed{B|_C=\frac{\bar R_b|_C+b_0^P}{q_Ct^2},}
\tag{23}
\]
\[
\boxed{(EB)|_C=
\frac{(E\bar R_b)|_C+b_1^P}{q_Ct^2}
-\frac{(Eq)|_C}{q_C}B|_C.}
\tag{24}
\]
只在同一真分支上读原 P 的两条整商，不假设整个 P/p 属于原格。

合法 factor lift 改变时，R888 的同一展开给
(P'^fact−P^fact)/p mod p∈t^(r_src)F³k[t,Y,d^(−1)]。其值与首 Euler 导数在 C 上全零，所以 (22)–(24) 以及 (16) 逐字不变。也可直接核：Hensel 支改动 p 倍量时，P、EP 的约化分别至少四重、三重消失，故这两个模 p 商不变。没有任意改 xi 或其它整 R/S 数字。

## 6. 指定真左行只需一个至多十五项的 forcing 尾

置
\[
K=2h+\tau-2,\qquad N=J-K=d_0+2-\tau,
\tag{25}
\]
\[
\widehat u(t)=t^{-h}F(t,\bar g(t)),\qquad
\zeta(t)=w(t)/t,\qquad
\mathcal U_*(t)=\zeta(t)^{-s}\widehat u(t)^4.
\tag{26}
\]
U_*(0)≠0，且
\[
\boxed{\mathcal T_P=-\frac{11}{a}t^K\mathcal U_*(t)\pmod{t^J}.}
\tag{27}
\]
N≤0 时整个自然双 jet forcing 为零；N>0 时只用 U_* 的前 N 项，1≤N≤15。因 h+N<s，这些数据仍在原实际轴的严格 <s 区间，不读取 t^p 之后的新 Frobenius 块。

只取一个已真正满足 R928(26) 的全局左行 (lambda0,lambda1,nu)。在原局部 N³ 框中，将它的 lambda1 唯一写成
\[
\lambda_1(v)=[t^{J-1}]H_\lambda(t)v(t),\qquad H_\lambda\in k[t]_{<J}.
\tag{28}
\]
这只是该既有真左行的局部写法，不能自由指定 H_lambda 再声称有全局延拓。由 (16)、(27)，它对固定 R928 类的准确值是
\[
\boxed{
-\frac{11}{a}[t^{N-1}](H_\lambda\mathcal U_*)
-\lambda_0(B|_C)-\lambda_1((EB)|_C).
}
\tag{29}
\]
N≤0 时第一项为零。其它两项由原 P/R_b 的 (22)–(24) 唯一确定，不能因为第一项是单位倍短系数就删除它们。

若使用 R842 已实际延拓成功的同一 GRes 对，R928(32) 的既定负留数规范给
\[
\mathfrak G_F(\jmath G)
=\operatorname{Res}_{P_C}
 \frac{B|_C\,\omega_0+(EB)|_C\,\omega_1}{e_C^2}
+\frac{11}{a}\operatorname{Res}_{P_C}
 \frac{t^K\mathcal U_*(t)\omega_1}{e_C^2}.
\tag{30}
\]
e_C=(EF)|C 在原点是单位。符号直接来自 R928 的原负留数和 (17) 的负十一；只有原联合延拓与其它边界均已支付才能使用。没有构造一个未经全局原列测试的任意 omega1。

## 7. 哪些指定陪集确可删除基点

若额外核实固定 B 属于原 H3，其值和首 Euler 值是真正兼容全局对；在低行门通过后，R928 的类才等于
\[
[(0,\mathcal T_P,0)]\in\operatorname{coker}\mathcal T_J.
\tag{31}
\]
这包括已指定的自然因子陪集 R_b≡−D mod j(H3)，不覆盖任意 R_b。

在这个准确分支中有两个直接结论。tau=0 或 1 时，(11) 末行唯一最低项从 w^(tau−2) 起，系数 −36t1^(r_src−2)u0²e0²/a 为单位。B∈H3 的 E³B 正则，不能抵消它，所以原 t² 低行门已失败。这是该指定陪集的真实非零低行，不是全原 R 的排除。

tau≥d0+2 时，N≤0，(31) 的双 jet 类恰为零。这里只支付 R928 的双值必要门；同一 H1 的完整 (29) 和受限 S 的 (31) 仍需另行通过。

剩余 2≤tau≤d0+1 时，(31) 的 forcing 是明确非零、至多十三项的原尾。然而局部目标非零不等于全局余核类非零，仍须真正的 (29) 左行或完整同源像判定。任意其它固定 R_b 始终保 (23)–(24) 的偏移；将它们默设零会改变原 affine 问题。

本注付清固定 quartic 的全 J 输入及任意真左行的实际短系数值，不重复单首 −11，不再引入一个抽象未赋值右端。原同 H1、同整 R/S、完整 p4 和 ordinary / 无穷 p 主门均未据此宣称完成。

依赖：R491 真实因子提升；R824 全 Euler 乘积与 −11 首项；R872 同修正后继及 R888 合法 lift 运输；R928 完整长行、二次逆 Taylor、真实全局左行及受限 S；R930 同 q 负 fringe；R932 同时 factor lift 的分母核算。全部为符号证明。
