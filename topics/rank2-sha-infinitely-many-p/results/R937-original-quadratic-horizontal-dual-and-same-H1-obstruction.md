# R937：原二次正水平真行与双 jet 之后的同 H1 非零残差

日期：2026-11-20。状态：完整符号证明；未执行数学计算。

本注接 R928、R934 与 R936 的真实左行方法，但处理不同的阶段。
在自然固定陪集中，τ≥d₀+2 时 R934 的整个双 jet 类已经为零。
这里用同一原二次 Euler 端点算子，构造杀掉完整原 H3 选定像、
并在每个真实兼容对之后杀掉同一 H1 normal 像的实际行。
在显示的严格次数门内，它对原固定右端取单位 28。
不把结论扩到任意 WD 陪集。

## 1. 原输入、陪集与精度

保 R928/R934 的同一原整 P、WD、P134、charge 四十、原 q、
十九角与完整返回 qt²H3。仍记

\[
C=(F),\quad P_0=(0,1),\quad N=\mathcal O_C(C),\quad
\kappa=C^2,\quad b=\deg_YF,\quad
\mathcal H_i=H^0(X,\mathcal O_X(iC)).
\tag{1}
\]

C 几何整，P₀ 光滑，\(\mathcal E=Y\partial_Y\)，
\(e=\mathcal EF\)、\(e(P_0)\ne0\)、\(3b<p\)。
保原 p>211、C·f₀=3、b≥5、全部原整格与好素数门。
在同一实际轴上写

\[
F(t(w),\bar g(w))=w^hu(w),\qquad
t=t_1w+O(w^2),\quad t_1u_0\ne0.
\tag{2}
\]

准确负 fringe 参数和读窗为

\[
s=2h+d_0+2,\quad 1\le d_0\le13,\quad
r_{\rm src}=\tau+d_0+2,
\]
\[
J=s-2=2h+d_0,\quad T=J-13,\quad L=\ell-2,
\tag{3}
\]
\[
h<T\le2h,\quad T-h>\kappa,\quad
T-h\le L\le h,\quad2h+L>J,\quad h>21.
\tag{4}
\]

本注的 τ 范围是

\[
\boxed{d_0+2\le\tau<\min(h+2,\ell).}
\tag{5}
\]

它较 raw 全 R 第二法向的 τ<h 多出至多两项：
这里最终作用的是 H3 中正则的同一 G，不能在任意带 t^(−2)
极的 B 上借用这两项精度。

固定原 R_b 陪集，通过 R928 四个低 t² 门，并置

\[
\Delta=(P-P^{\rm fact})/p,\qquad
B=\frac{\overline{R_b+\Delta}}{qt^2}.
\tag{6}
\]

非零结论明确要求这个既定陪集已核

\[
\boxed{B\in\mathcal H_3.}
\tag{7}
\]

它不是事后改选 R_b 的许可。一般 B 的实际行值见 §6。

令

\[
n=h+\tau-2,\qquad m=n+1=h+\tau-1.
\tag{8}
\]

由 (3)–(5)，

\[
\boxed{m\le2h<J,\qquad m\le h+L.}
\tag{9}
\]

这两个弱不等号准确来自严格的 τ<h+2、τ<ell。
因此模 t^m 时，二次 Taylor 的未知项和第四短行的未知尾均退出。

## 2. 真实二次端点算子与完整双正水平

记原严格正水平及其全交为

\[
H_+,\qquad Z_+=C\cap H_+,\qquad e_+=C\cdot H_+.
\tag{10}
\]

定义同一个原全局算子

\[
\boxed{
\mathcal Q_+=(\mathcal E-3b)(\mathcal E-3b+1)
=\mathcal E^2-(6b-1)\mathcal E+3b(3b-1).
}
\tag{11}
\]

原十九角已付 E 保 H3，所以 Q₊ 也保完整 H3。
在正水平图 x=Y^(−1)、原 frame \(\widehat G=x^{3b}G\) 中，

\[
x^{3b}\mathcal Q_+G
=(x\partial_x)(x\partial_x-1)\widehat G
=x^2\partial_x^2\widehat G.
\tag{12}
\]

于是 Q₊G 在 H₊ 的一般点至少消失二次。
它已经是同一光滑 X 上的全局 H3 截面，
故这一除子重数给完整的全局包含

\[
\mathcal Q_+\mathcal H_3
\subset H^0(X,\mathcal O_X(3C-2H_+)).
\]

不另去掉 H₊ 与例外曲线的交点。
限制到原 C，

\[
\boxed{
(\mathcal Q_+G)|_C
\in \mathcal V_{2,+}:=H^0(C,N^3(-2Z_+))
\quad(G\in\mathcal H_3).
}
\tag{13}
\]

这里保 2Z₊ 的全部非约化长度，
\(\deg N^3(-2Z_+)=3\kappa-2e_+\)。
P₀ 不在 Z₊ 上，jet 使用原 N³ frame。

## 3. 从原四行到同一个全局截面的有限读取

对任意原四目标

\[
f=(f_0,f_1,f_2,f_3)
\in(k[t]/t^J)^3\oplus k[t]/t^L,
\]

用 R928 的实际有限逆 Taylor 定义

\[
j_0(f)=f_0-\eta f_1+\eta^2f_2/2\pmod{t^J},
\]
\[
j_1(f)=f_1-\eta f_2+\eta^2f_3/2\pmod{t^J},
\tag{14}
\]

其中同一 \(g=\psi e^\eta\)，\(\operatorname{ord}\eta=h\)。
2h+L>J 支付 j₁ 的真实短窗；不读取未知尾。

定义到长度 m 的同一个线性读取

\[
\boxed{
\Psi_{2,+}(f)=
f_2-\eta f_3-(6b-1)j_1(f)
                +3b(3b-1)j_0(f)\pmod{t^m}.
}
\tag{15}
\]

(9) 保 f₂−ηf₃ 在此长度有定义。
对于真实 \(G\in\mathcal H_3\)，设
\(f_i=(E^iG)(t,g)\) 为其原选定前缀。
G 正则，因而

\[
(E^2G)|_C
=(E^2G)(t,g)-\eta(E^3G)(t,g)+O(t^{2h}).
\]

再用 (14) 的全 J 身份及 m≤2h<J，得到

\[
\boxed{
\Psi_{2,+}\bigl(\operatorname{jets}_{J,L}G\bigr)
=\operatorname{ev}_m((\mathcal Q_+G)|_C).
}
\tag{16}
\]

这是对全部原 H3 的完整列恒等式。
未用未知的 E⁴G 行，亦不将旧模 T 的 3η 镜轴免费延至 J。

## 4. 真完整截面列产生实际左行

本注的次数门是

\[
\boxed{n+2e_+>3\kappa.}
\tag{17}
\]

它使实际
\(\operatorname{ev}_n:\mathcal V_{2,+}\to k[t]/t^n\)
单射：非零截面不可能有大于其全线束次数的原点零阶。
原 C 可能奇异，但它整、线束可逆且 P₀ 光滑，所以同一次数
论证仍成立，未删除 conductor 或边界。

按 R936 的实际完整列方法，取 \(\mathcal V_{2,+}\) 真基，
组成前 n 项矩阵 A 和第 n 项列 c。
取 A 中按列序的首组独立列 I，定义

\[
\boxed{\lambda_{2,+}(v)=[t^n]v-v_I A_I^{-1}c.}
\tag{18}
\]

零维来源时第二项为零。
它使用全部真实截面列，且由 (17) 所付的满行秩合法定义。
逐列直接核得

\[
\lambda_{2,+}(\operatorname{ev}_mV)=0
\quad\text{对全部 }V\in\mathcal V_{2,+},
\qquad
\lambda_{2,+}(t^n u)=u(0).
\tag{19}
\]

于是原选定四行的实际左行

\[
\boxed{\Lambda_{2,+}:=\lambda_{2,+}\circ\Psi_{2,+}}
\tag{20}
\]

杀掉全部 \(\operatorname{jets}_{J,L}(\mathcal H_3)\)，由 (13)、(16)
逐式保证。它不只杀同一 H1 的某个试验子格。

## 5. 对同一个固定 P 的实际值

在原自然基准中，R934 的真实四目标仍是

\[
\begin{aligned}
 f_0^*&=0\pmod{t^J},\\
 f_1^*&=-\frac1a A w^{4h-s}u^4\pmod{t^J},\\
 f_2^*&=-24A w^hu\xi e^2-\frac8a A w^{3h-s}u^3e
                                                  \pmod{t^J},\\
 f_3^*&=-24A\xi e^3-\frac{36}a A w^{2h-s}u^2e^2
              -\frac{12}a A w^{3h-s}u^3e_2
                                                  \pmod{t^L},
\end{aligned}
\tag{21}
\]

其中 \(A=t(w)^{r_{\rm src}-2}\)，xi 是同一整 factor lift
的真除 p 低项，e、e₂ 取原实际轴。
全部 Euler 三角运输、原 q 导数及公共四十已经完整支付，
不是现在另行丢掉。

由 R934，(5) 中的 \(K=2h+\tau-2\ge J\)，故

\[
j_0(f^*)=j_1(f^*)=0\pmod{t^J}.
\tag{22}
\]

另一方面 \(f_2^*-\eta f_3^*\) 在 w^(h+τ−2) 的系数是 −8+36=28。
两条 xi 项从 h+τ+d₀ 起才出现，严格高于 n；
e₂ carry、eta 的次项均至少再晚 h 阶。
未知长行从 J 起，短行尾乘 eta 从 h+L 起，
(9) 精确支付所有所用项。

令

\[
\widehat u(t)=t^{-h}F(t,\bar g(t)),\qquad
\zeta(t)=w(t)/t.
\]

在原 t 参数中，实际读取为

\[
\boxed{
\Psi_{2,+}(f^*)
=\frac{28}{a}\,\zeta(0)^{-s}\widehat u(0)^3e(P_0)\,
                  t^n\pmod{t^{n+1}}.
}
\tag{23}
\]

所有 t^n 以下系数全零。
若先用 w 写，首系数为
\(28t_1^{r_{\rm src}-2}u_0^3e_0/a\)；
换到 t 后须乘 \(t_1^{-n}\)，恰与 (23) 相同。
这里保了真实变量变换的倍率。

因 p>211，(23) 的系数是单位。
由 (19) 得完整原行的确定值

\[
\boxed{
\Lambda_{2,+}(f^*)
=\frac{28}{a}\,\zeta(0)^{-s}\widehat u(0)^3e(P_0)\ne0.
}
\tag{24}
\]

给定陪集的实际目标是 \(f_i=f_i^*-(E^iB)(t,g)\)。
当已核 (7) 时，B 的四个前缀本身属于原 H3 完整像，
故由 (20) 被同一左行杀掉。因此

\[
\boxed{\Lambda_{2,+}(f)=\Lambda_{2,+}(f^*)\ne0.}
\tag{25}
\]

这准确排除该既定陪集的原选定四行，
于是原完整 p³ 条件也不可解；受限 S 不可能改变此结论。

## 6. 每个真正兼容对后的同 H1 余核

本段进一步明确 (25) 作用的剩余层。
在 (5)、(7) 下，R934 的双 jet 类本来为零；
这不表示所有选定行已有解。

取任意一个真正兼容对 \(V_0,V_1\) 实现目标 j₀、j₁ 的前缀，
并取 R836 支付的同一 \(G_0\in\mathcal H_3\) 实现整对。
置

\[
d_i=f_i-(E^iG_0)(t,g).
\]

则原完整逆 Taylor 给

\[
j_0(d)=j_1(d)=0\pmod{t^J}.
\tag{26}
\]

由 (15)、(20)、(25)，同一个 normal 行

\[
\boxed{
\rho_{2,+}(x,y)=\lambda_{2,+}(x-\eta y)\pmod{t^m}
}
\tag{27}
\]

满足

\[
\boxed{
\rho_{2,+}(d_2,d_3)
=\frac{28}{a}\,\zeta(0)^{-s}\widehat u(0)^3e(P_0)\ne0.
}
\tag{28}
\]

对于每一个原 \(L_1\in\mathcal H_1\)，
\(G=F^2L_1\) 的值与首 Euler 值在整个 C 上为零。
由 (16)、(20)，

\[
\boxed{
\rho_{2,+}\bigl(
(E^2(F^2L_1))(t,g),\
(E^3(F^2L_1))(t,g)\bigr)=0.
}
\tag{29}
\]

所有截断仍是 J、L；(27) 只读它们已知的组合。
所以 (27) 是原 \(\mathcal N_{J,L}\) 真像的一个左行，
而 (28) 对每一个真实兼容 G₀ 都是同一单位。
这排除的是全部兼容对之后的同 H1 原像，
不是只试了零兼容对或某一个便利的 G₀。

若 (7) 未核，则正确的一般值始终是

\[
\Lambda_{2,+}(f)
=\Lambda_{2,+}(f^*)-
 \Lambda_{2,+}\bigl((B,EB,E^2B,E^3B)(t,g)\bigr).
\tag{30}
\]

四个 B 前缀用原实际输入读取。
任意 B 可能有 t^(−2) 极，特别当 τ=h 或 h+1 时，
不能把 (30) 无证替换成 Q₊B|C：其二次 Taylor 尾可能进入。
这里没有删除这个偏移，也不把 (25) 扩成全 WD 结论。

## 7. 新门的准确范围与未付部分

在当前额外的 T≤3κ 范围，(17) 并非 R935 的 nef 预算门。
若同时处于 R903 未由正水平齐次门排除的范围
T+e₊≤3κ，记

\[
\delta_+=3\kappa-T-e_+\ge0.
\]

则 (17) 准确等价于

\[
\boxed{\tau-h-d_0+11+e_+>\delta_+.}
\tag{31}
\]

所以它可在双 jet 类已为零的高 τ 范围中提供实际同 H1 非零行；
但本注不宣称某个未识别的 F、D、τ 必然满足 (31)。
来源帽、原 r_src 与真正允许的陪集仍须逐项核定。

m=2h 时 E⁴G 的未知项从 t^(2h) 起，恰在模数之外，合法；
m=h+L 时原短尾也恰在模数之外。
相反，τ=h+2 或 τ=ell 时所需首项与未知尾相撞，
本注严格排除这两个端点。

n+2e₊=3κ 的等号可能有零次数截面，不能认前 n 列单射。
(17) 未付时，本注也不声称同 H1 目标有解或无解。
其它给定 B、其它 WD 陪集、受限 S 的后续原行、
完整 p⁴ 及 ordinary / 无穷 p 主门继续保留。

依赖：R495/R836 原 H3 及 Euler 稳定、真实两值提升；
R903 严格正水平框；R928 全 J/短 L 的四行与同 H1 像；
R934 固定原四目标、双 jet 与既定基点；
R936 完整截面列所构造的真实前缀左行方法。


审阅：deep完整推导；root/theta全文核完整2H+算子、实际四行和全部精度端点、同一兼容G0后的rho2与全部F²H1源。没有数学执行；原定稿SHA256 `2572ee053890f44405144c915e99b991ba7df1daf3e6531f31dbb2e079003852`。
