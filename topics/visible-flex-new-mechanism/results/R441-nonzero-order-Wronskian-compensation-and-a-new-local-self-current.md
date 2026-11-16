# R441：一个非零零阶核的完整 Wronskian 补偿与新的 self current

日期：2026-11-16。**原式纸面证明；未执行新的 profile、积分、符号、矩阵或科学运行。**

[R440](R440-complete-zero-order-compatible-self-module-and-sixteen-actual-fluxes.md) 已闭合原 $c=0$ 第三核中 universal 消-self 核的全部 current，并给出同一原库的实际十六行与全部其它根的五列余商。本稿使用 $c\ne0$ 的两个原第三方向，构造一个 whole-E 零且全部退化点消-self 行均零的响应。其完整 self current 可以准确单取
$$
u(u'')^4.
$$
这不是原第四输出本身等于该五次 monomial，而是保原右锚之后的真实内部 partial。

新方向严格超出 R440 的二十一维 current 空间。对原固定镜对族它没有增加新的自由行，而是在原五列余商之外添加一个明确的第六列。全部实际基准和其它真实目标继续保留；不由一条 signed 补偿宣称全部根已经实际支付。

## 1. 原系数和比例规范

仍用
$$
p=u',\quad r=u'',\quad t=u''',\quad A=6pt-2r^2.
$$
$\mathfrak H$ 是原 hook，$\mathfrak H_1=\delta\mathfrak H$；
$\mathfrak J_0$ 是 [R255](R255-explicit-third-diagonal-kernel-and-complete-hook-response-formula.md)(5)—(6)的原三维补串首元。
本稿固定
$$
\jmath=\mathfrak J_0/2,\qquad \eta=\mathfrak H_1/6.
\tag{1}
$$
这些 $1/2,1/6$ 属于原成本定义，不并入 current 的外因子2。

由 [R261](R261-eight-local-self-adjoint-hook-operators-and-full-third-kernel.md) 的 $\chi_{30},\chi_{32},\chi_{34}$ 完整系数，结合 R432 的
$$
\tau_1=-(\mathfrak H_1+1024\chi_{30})/8,\qquad
2\sigma=64(\chi_{34}-3\chi_{32})-\mathfrak J_0/2,
$$
直接得到
$$
\boxed{
\begin{aligned}
a_{\jmath}&=-2(ur+p^2),&
c_{\jmath}&=2p\,u^{(5)}+6r\,u^{(4)}+4t^2,\\
a_\eta&=-xA+2ut-\tfrac43pr,&
c_\eta&=-2r\,u^{(5)}-6t\,u^{(4)} .
\end{aligned}}
\tag{2}
$$
例如原全系数为
$a_{\mathfrak H_1}=-6xA+12ut-8pr$、
$c_{\mathfrak H_1}=-12(ru^{(5)}+3tu^{(4)})$，
以及 $a_{\mathfrak J_0}=-4(ur+p^2)$。
这些从已发表原算子相减取得，不把对角信息当成完整第三系数。

记
$$
F=r^2,\qquad G=pt+\tfrac12r^2.
$$
则(2)等价于
$$
c_{\jmath}=2G'',\qquad c_\eta=-F'''.
\tag{3}
$$

## 2. P 与 R−S 的同锚 Wronskian

令原二次算子
$$
P(u,u)=J(r^2),\qquad Q(u,u)=(R-S)(u,u)=p^2+xP-J(xr^2).
\tag{4}
$$
Q 在本稿是原 $R-S$，不是 whole-self 观察的符号。
直接保右原函数求导：
$$
P'=-F,\quad Q'=2pr+P,\quad Q''=2G,
$$
$$
c_{\jmath}=Q'''',\qquad c_\eta=P''''.
\tag{5}
$$

定义真实响应
$$
\boxed{\mathcal V=\mathcal B_P\jmath-\mathcal B_Q\eta.}
\tag{6}
$$
原 $\mathcal B$ 使用 R255(30)—(31)的完整归一：
self 为 $2K_u^\tau(\Phi_E(u,u))$，全圆响应还须先按原公式处理其它 history。

其 whole-Q 左二次尾为
$$
-\frac14\int(c_{\jmath}P-c_\eta Q)
=-\frac14\int(PQ''''-QP'''').
$$
原恒等
$$
PQ''''-QP''''=
D_x\{PQ'''-P'Q''+P''Q'-P'''Q\}
\tag{7}
$$
给零，但必须保两端：
右 collar 的 P、Q 和所有相关 jets 为零；左 collar 上
$$
P=\mu_0,\qquad Q=x\mu_0-\mu_1,\qquad
P'=P''=P'''=Q''=Q'''=0.
$$
所以(7)的原边界在两端均零。并未假 Q 左紧或令 $Q'(\ell)=\mu_0$ 为零。

两原第三方向都在 Z 中，故对应的 universal pure 零。
于是
$$
\boxed{E(\mathcal V)=0.}
\tag{8}
$$
同时对一个真实右包，$P$、Q 的左尾为
$n_0,\ xn_0-n_1$；(3)的导数形式也使其原二次跨尾全零。后面给出其内部 current，而不将这条全尾结论扩大成内部零。

## 3. 完整 Green current：保三个右常数

对任意原 $\tau\in Z$，设
$$
h_\tau=(a_\tau r)'+b_\tau p,\qquad h_\tau'=-c_\tau u .
$$
取 $I=-J$，故 $(IF)'=F$，且 $IF$ 在原右 collar 为零。
由 R261 的完整自伴恢复，
$$
(K_u^\tau w)''=(a_\tau w'')'+b_\tau w'+I(c_\tau w).
$$
原 Green 恒等逐项给
$$
\boxed{
\int_{\ell_u}^x p[2K_u^\tau(w)]''
=2\{a_\tau(pw''-rw')+w h_\tau+uI(c_\tau w)\}.
}
\tag{9}
$$
这是对真实右零、可有左二次尾的 w 的式子。左平端使右侧原积分常数为零；$K,K',K''$ 的右三常数仍是原恢复给的零，没有另选。

对(1)，从 $h'=-cu$ 和同一个右端得到
$$
\boxed{
h_{\jmath}=-2uG'+2p^2t,\qquad
h_\eta=uF''-pF'+\tfrac23r^3.
}
\tag{10}
$$
例如 $J(rG)=-pr^2/2$、$J(tr^2)=-r^3/3$ 是保紧 outer 的同锚分部式；它们固定(10)中的常数。

由(5)、(7)，
$$
I(c_{\jmath}P-c_\eta Q)
=PQ'''-P'Q''+P''Q'-P'''Q
$$
$$
=2PG'+2FG-F'Q'+F''Q.
\tag{11}
$$
(11)的右端在右 collar 准确为零，因此没有额外常数。

将(10)—(11)代入(9)，不先使用 A=0，完整 self current 为
$$
\boxed{
\begin{aligned}
\tfrac12\mathcal F_x(\mathcal V)
={}&a_{\jmath}(pP''-rP')-a_\eta(pQ''-rQ')\\
&+2p^2t\,P+(pF'-\tfrac23r^3)Q
+u(2FG-F'Q').
\end{aligned}}
\tag{12}
$$
式(12)仍保原 P、Q，故它不是预先截成局部的计算。

## 4. 全部 A 根上的 self 与真实 ordered 槽

在 A=0 点，$pt=r^2/3$，
$$
pP''-rP'=\tfrac13r^3,\qquad
pQ''-rQ'=-\tfrac13pr^2-rP.
$$
式(12)中 Q 的系数
$pF'-2r^3/3=rA/3$ 准确为零。其余完整收集给
$$
\boxed{
\mathcal F_x(\mathcal V)
=-\tfrac29ur^4-\tfrac{20}{9}p^2r^3-\tfrac43pr^2P.
}
\tag{13}
$$
最后 P 项仍是同一个实际 profile 的原 primitive；本步没有删掉它。

对真实右包尾 $w_P=n_0,\ w_Q=xn_0-n_1$，
原 right primitives 是
$$
I(c_{\jmath})=2G',\qquad I(c_\eta)=-F'',\qquad
I(xc_\eta)=-xF''+F'.
$$
将它们直接代(9)，得整个尾 current
$$
\boxed{
\mathcal F^{\to}_{x,n}(\mathcal V)
=-\tfrac43pr^2n_0+
\tfrac23A\{(p-2xr)n_0-rn_1\}.}
\tag{14}
$$
所以它在 A 根确为 $-4pr^2n_0/3$，不为零。
这也从原槽直接保住了内部 constant/affine 尾的影响；whole-E 零不等于内部 current 零。

## 5. 同一原响应同时清 primitive 和全部 ordered 行

R432 的 $\tau_1$ 满足
$a_{\tau_1}=xA+2pr,\ c_{\tau_1}=0$。原 R self 导数给
$$
pR''-rR'=-\tfrac43pr^2+\tfrac13xr^3-rP
\quad(A=0).
$$
因此
$$
\mathcal F_x(\mathcal B_R\tau_1)
=-\tfrac{16}{3}p^2r^3+\tfrac43xpr^4-4pr^2P.
\tag{15}
$$
其右包尾为 $xn_0$，原 current 为
$$
-2(xA+2pr)r n_0.
\tag{16}
$$

置
$$
\boxed{\mathcal V_0=\mathcal V-\tfrac13\mathcal B_R\tau_1.}
\tag{17}
$$
式(13)、(15)同时使所有同包 P 项消去，得到
$$
\boxed{\mathcal F_x(\mathcal V_0)
=-\tfrac29\{ur^4+2p^2r^3+2xpr^4\}\quad(A=0).}
\tag{18}
$$
而(14)、(16)给不先令 A 零的完整尾
$$
\boxed{
\mathcal F_{x,n}^{\to}(\mathcal V_0)
=\tfrac23A\{(p-xr)n_0-rn_1\}.}
\tag{19}
$$
因此(19)在全部实际 A 根准确为零，对所有真正三矩 n 都成立。

所有其它 outer 包的左二次平台也已保账：(7)杀同包二次尾，(3)的导数形式对 $n_0,xn_0-n_1$ 杀跨包二次尾。它们可以留下原仿射平台，但其第二导数零；不能将它们写作整个场为零。

在逐包比例的当前圆上，原局部自伴算子满足
$\mathscr A_{\tau,f}(\phi_\theta)=0$；原三个右常数使完整
$K_f^\tau(\phi_\theta)=0$。这是对本稿原 Z 方向逐包得到的全场身份，才允许在 R255 完整响应中删去另一 $4\Phi_E(\phi,K_f^\tau\phi)$ 项。
由此(18)—(19)确给该圆的两条完整 current，不只是单包示范。

## 6. 一个具体原成本准确给出 ur⁴

沿 R436/R438 记 $J_\sigma=\mathcal B_P\sigma$、$J_2=\mathcal B_P\tau_2$。
它们的 current 为 $2p^2r^3/3$ 和 $8(xpr^4-p^2r^3)/3$，且 P 的常尾使 ordered 部分零。

定义
$$
\boxed{
\mathcal U_*=-\tfrac92\mathcal V_0-6J_\sigma-\tfrac34J_2.
}
\tag{20}
$$
这是有限原成本的完整实线性组合，仍使用(1)、(6)、(17)的原比例。
由(18)逐项收集，
$$
\boxed{\mathcal F_x(\mathcal U_*;u)=ur^4\quad\text{在全部 }A_u=0\text{ 点}.}
\tag{21}
$$
它的完整 ordered current 为
$-3A\{(p-xr)n_0-rn_1\}$，故所有实际退化点均零。

本稿各成本是原 response，且(8)、R432 的 whole-E 恒等给
$$
\boxed{
E(\mathcal U_*)=0,\qquad J^+(\mathcal U_*)=0,\qquad
C_{i,\alpha}(\mathcal U_*)=0
}
\tag{22}
$$
对当前整个圆所有包和所有实际 A 根成立。
最后一步使用 R344/R352 的全响应自然零，因此包括 R433 的全部 ordered 自然观察；不是只对一个固定 profile 的数值零。

原两通道准确为
$$
H_{d,i,\alpha}(\mathcal U_*)=a_i^3R_i\,u_i r_i^4,\qquad
H_{e,i,\alpha}(\mathcal U_*)=-a_i^3T_i\,u_i r_i^4.
\tag{23}
$$
$a_i,b_i$、全部原宽度、中心与真实第五幅仍按 R432 规范。
一般实际目标的原平台项不能由(23)预先删去；本文列的二次平台已逐式证明为零。

## 7. 它严格超出二十一维空间，但不虚增镜对秩

R440 的非 K 十条 current 都含 p 因子。若 $ur^4$ 由其二十一列表示，先比较独立的纯 $x^nr^5$ 迫十一条 K 系数为零，再比较不含 p 的 monomial $ur^4$ 即矛盾。

这个比较仍在 $p\ne0$ 的真实有限 jet 开集上进行多项式恒等；不是声称可以选一个不可能的 $p=0,r\ne0$ 退化点。
因此
$$
\mathscr M_{22}=\mathscr M_{21}+\mathbb R\mathcal U_*
$$
给二十二个独立 formal self 方向。

在 R438/R440 固定的物理镜对上，$u_*/r_*=h_*$，所以(21)仅为 $h_*r_*^5$，已由 K0 给出。令 $\mathsf R=-45K_0/8$，则
$$
\boxed{\mathfrak b_5=\mathcal U_*-h_*\mathsf R,\qquad
F_{\mathfrak b_5}=r^4(u-h_*r).}
\tag{24}
$$
它在该整镜对全部对应副本上盲，不只杀选中的十六点。
故镜对像仍是 R440 的
$(P,\mathsf TP+Q)$、$\deg P\le10,\deg Q\le4$；
不能把 formal22 说成实际22或17。

另一方面，(24)在其它根保留了一个此前没有的共同 cap 读出。
相较原第五列，原 $pr^3(u-h_*r)$ 只在一个固定点与它成比例；若不同实际根的 $p/r$ 不同，不能以每点一个不同系数把两列合并成同一个成本。

## 8. 全部真实目标：五列余商准确扩大为六列

保持 R440 的同一十六行核心、同一原实际 V 和同一扣平台规范。
当 $J^+(V)=0$ 且全部 C 已按同一联合入口清零，令 $V^\flat$ 为使用原十六列消去核心目标后的完整剩余成本。

沿用 R440(25)的 normalized 通道
$$
\eta_{i,\alpha}
=\frac{R_iH_{d,i,\alpha}-T_iH_{e,i,\alpha}}
{a_i^3(R_i^2+T_i^2)} .
$$
它保所有 self/history 真值，也允许 $R_i=0$。
在 R440 的五条原 blind 列后，追加(24)的第六列：
$$
\mathsf B^+_{(i,\alpha),j}
=F_{\mathfrak b_j}(x_{i,\alpha};u_i,p_i,r_i),
\quad 0\le j\le5.
\tag{25}
$$
$\mathfrak b_5$ 的 $ur^4$ monomial 在原五列中不存在，故它们是整镜对核的六个独立 formal current。
同一有限实际库的评价仍可能降秩，本文不作新 rank 断言。

现在原明确模块的完整判据变为
$$
\boxed{
\mathscr M_{22}\text{ 在线性成本层清全部根}
\iff
\eta_{\rm rest}(V^\flat)\in\operatorname{im}\mathsf B^+ .
}
\tag{26}
$$
(26)中的目标不是另选的 local polynomial，而是原 V 的真实积分。
r=0 的其它根仍使六列全零，所以 R440 的该类明确余条件尚未消失。
若一个实际根有 $r\ne0$ 且 $u/r\ne h_*$，则(24)非零；这给一个准确的新响应读出，不预先假定当前库存在一个新独立行。

同一实际 J⁺/已付 C 截面中的原 prototype、共享倒行、两次商校正、Klein 基准都仍按 R435/R440 入账。新增列保持这些已列观察，但不能据 signed 值把它直接拼上冻结实际几何。
若要把(26)所有其它根升级成实际联合截面，仍须核同一个增强响应商/目标像与完整原型基准。本文没有将 R434 的 85 维 whole-Q 核或 53 个 current 零关系当成这些 self 观察已经评价。

本稿完成的是一个真正 $c\ne0$ 来源、Wronskian 两端及三个右常数完整保留的 self 补偿。它使已知 universal 消-self self 模块从21增加到22，且把同一全部根目标的明确余商从五列变为六列；其它 whole-E 核的完整 self 像仍待消费原证书或继续原式推导。
