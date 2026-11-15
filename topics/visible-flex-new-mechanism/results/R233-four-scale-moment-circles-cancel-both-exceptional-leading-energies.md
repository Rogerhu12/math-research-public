# R233：四尺度三矩圆消去例外端芽的两个领先能量

日期：2026-11-15。**完整纸面构造；没有执行新的研究计算、profile 求积或原式编译。**

本稿接 [R229](R229-p2-energy-boundary-identity-for-exceptional-germs.md) 的同右锚能量身份、[R231](R231-complete-mixed-leading-gate-for-the-exceptional-even-port.md) 的完整 mixed 领先门，以及 [R183](R183-overlapping-derivative-packet-circle-invisible-to-third-hook.md) 的导数分包和八包第三阶构造。新增结论是：R231 的两个领先能量并非在所有合法三矩圆上都非零；可用四个同形尺度包和一个明确旋转同时使它们为零。

**范围先固定。** 下面的平面可由常数 GL(2) 换基分离成不交 profiles。它不是 R183 的“不能换基变成不交”的新实例，也不自动继承旧圆的首个 $f$ 上升而 $g=0$、八条非退化 flux 或 R225 的特定解析包条件。本稿没有证明完整第四 period 或 ruling 可解。八复制的小节只准确兼容已经发表的完整第三阶构造；旧分离圆若另有更强障碍，仍须保留。

## 1. 原算子、三矩和两个目标

固定正区间 $I=[\ell,r]\Subset(0,\infty)$，左右均保开放 collar。所有输入是实 $C^\infty_c((\ell,r))$，右积分始终为

$$
J(F)(x)=\int_x^rF(\eta)\,d\eta.
\tag{1}
$$

采用 R229/R231 在 $b=0$ 的同一原二次算子

$$
8G(u,v)=
4xuv-2x^2(uv'+u'v)+2x^3u'v'
+x^2J(x^2u''v''+2u'v')
\tag{2}
$$

和同一双线性能量

$$
E(U,V)=\frac14\int_\ell^r
\bigl(x^2U''V''+2U'V'\bigr)\,dx.
\tag{3}
$$

即使 $U,V$ 有左侧二次尾，(3) 也使用其真实原值。

三矩为

$$
\begin{aligned}
m_0(u,v)&=\int_\ell^r u''v'',\\
m_1(u,v)&=\int_\ell^r x u''v'',\\
m_2(u,v)&=\int_\ell^r x^2u''v''+2\int_\ell^r u'v'.
\end{aligned}
\tag{4}
$$

合法非退化三矩圆要求

$$
m_\nu(f,f)=m_\nu(g,g),\qquad
m_\nu(f,g)=0\quad(\nu=0,1,2),\qquad m_0(f,f)>0.
\tag{5}
$$

同乘一个正数即可取 $m_0(f,f)=m_0(g,g)=1$。这里普通复平方 $q=f+ig$ 满足三复零矩；没有用复绝对值替代 (5)。

置

$$
A_f=G(f,f),\quad A_g=G(g,g),\quad X=G(f,g).
$$

R231 (25)–(27) 的完整领先相位为

$$
C_\theta=\sin^2\theta\,L_c+\sin(2\theta)\,L_s,
\qquad
L_c=E(A_f,A_g-A_f),\quad L_s=E(A_f,X).
\tag{6}
$$

本稿准确构造 (5) 且 $L_c=L_s=0$ 的圆。式 (6) 已经包含 R231 所付的完整最高 $h\beta^2$ 层；较低层的局部恢复和 histories 不因 (6) 为零而消失。

## 2. 左二次尾和正 bulk 必须分开

对紧输入 $u=x y,v=x z$，直接微分给

$$
x^2u''v''+2u'v'
=x^4y''z''+D_x(2x^3y'z'+2xyz).
\tag{7}
$$

右 collar 端项为零。把 (7) 代入 (2)，局部项准确相消：

$$
\boxed{G(u,v)=\frac{x^2}{8}J\!\left[x^4(u/x)''(v/x)''\right].}
\tag{8}
$$

对任意右 collar 为零、左侧允许有尾的 $U,V$，(7) 另给

$$
\boxed{
E(U,V)=\frac14\int_\ell^r
x^4(U/x)''(V/x)''
+\frac12\left[x^3(U/x)'(V/x)'+x(U/x)(V/x)\right]_\ell^r.
}
\tag{9}
$$

例如，若左 collar 上 $U=x^2 C_U/8$、$V=x^2 C_V/8$，则 (9) 的边界为

$$
-\frac{\ell^3 C_UC_V}{64}.
\tag{10}
$$

因此本文不把 $E(G(u,u),G(u,u))$ 当成正 bulk；它一般有 (10) 的负边界。

对单个非零实紧输入 $u$，写

$$
A=G(u,u),\qquad
C_u=\int_\ell^r x^4((u/x)'')^2>0.
\tag{11}
$$

由 (8)，$A=x^2C_u/8$ 于左 collar，右 collar 为零。于是 $(A/x)''$ 紧支撑在 $u$ 的活动包内。定义

$$
S(u)=\frac14\int_\ell^r x^4((A/x)'')^2.
\tag{12}
$$

有 $S(u)>0$。若 (12) 为零，则 $(A/x)''=0$，故 $A/x$ 在整个 I 仿射；右 collar 为零迫 $A=0$。式 (8) 再迫 $((u/x)'')^2=0$，紧支撑使 $u=0$，矛盾。这个证明没有删掉 (11) 的非零左尾。

## 3. 四个尺度准确支付全部三矩

取四个不同正数

$$
a_1<a_2<a_3<a_4,\qquad a_j\in(\ell,r).
$$

取 $\delta>0$ 足够小，使四个闭区间
$[a_j(1-\delta),a_j(1+\delta)]$ 两两不交并严格位于 I 内。
任取非零实

$$u\in C^\infty_c((1-\delta,1+\delta)),$$

定义 $u_j(x)=u(x/a_j)$。所有原积分可用共同右锚 r，因为其右侧 integrand 已为零。

令

$$
v_j=\frac1{\prod_{i\ne j}(a_j-a_i)},\qquad
s_j=\operatorname{sign}v_j,\qquad
w_j=|v_j|a_j^3>0.
\tag{13}
$$

四阶 Lagrange 插值的最高次系数给

$$
\sum_{j=1}^4v_j a_j^\nu=0\qquad(\nu=0,1,2).
\tag{14}
$$

具体地，次数至多二的多项式 $z^\nu$ 在四节点的插值式中，$z^3$ 系数为 (14)，左侧原多项式该系数为零。四个 $v_j$ 全非零且符号交替，故两种 $s_j$ 都出现。

置

$$
\boxed{
f=\sum_{j=1}^4\sqrt{w_j}\,u_j,\qquad
g=\sum_{j=1}^4s_j\sqrt{w_j}\,u_j.
}
\tag{15}
$$

每个包内 $g=s_j f$，不同包不交。因此三条自矩逐点相等。准确尺度律为

$$
m_\nu(u_j,u_j)=a_j^{\nu-3}m_\nu(u,u),
\qquad \nu=0,1,2,
\tag{16}
$$

其中 $\nu=2$ 的两项都同为 $a_j^{-1}$。从而

$$
m_\nu(f,g)=m_\nu(u,u)
\sum_j s_jw_j a_j^{\nu-3}
=m_\nu(u,u)\sum_jv_j a_j^\nu=0.
\tag{17}
$$

此外

$$
m_0(f,f)=m_0(u,u)\sum_j|v_j|>0.
\tag{18}
$$

若 $A f+B g=0$，分别在正、负号包上限制得 $A+B=A-B=0$，所以 f、g 线性独立。(15) 已是非退化三矩圆，不需要新增左补矩包或近似后修复。

## 4. 共同尾、正交 bulk 和准确旋转

记 $A_j=G(u_j,u_j)$。由支撑不交与 (2) 的双线性，

$$
A_f=A_g=:A=\sum_jw_jA_j,\qquad
X=\sum_js_jw_jA_j.
\tag{19}
$$

每个 $A_j$ 自己保留左二次尾。其尾系数由 (7) 的双端边界为零得到

$$
C_j=\int x^4((u_j/x)'')^2=m_2(u_j,u_j).
$$

因而 $X$ 的总左尾系数为 $m_2(f,g)=0$；X 是真正双 collar 为零的函数。A 的左尾一般非零，但 $A_f$ 和 $A_g$ 完全相同。

各 $W_j=(A_j/x)''$ 支撑在互不交的小包内。令

$$
S_j=\frac14\int_\ell^r x^4 W_j^2>0.
$$

由于 X 紧支撑，(9) 在 $(A,X)$ 和 $(X,X)$ 上的边界均严格为零。因此

$$
\boxed{
P:=E(A,X)=\sum_js_jw_j^2S_j,\qquad
Q:=E(X,X)=\sum_jw_j^2S_j>0.
}
\tag{20}
$$

这一步只是 $(A_j/x)''$ 的真实支撑正交，绝非把 $A_j$ 原左尾删除。两种符号都有严格正权，故

$$|P|<Q.\tag{21}$$

取

$$t=-P/Q\in(-1,1),\qquad
\sin(2\alpha)=t,\quad \cos(2\alpha)>0,
\tag{22}
$$

并作同一常数旋转

$$
f_\alpha=\cos\alpha\,f+\sin\alpha\,g,\qquad
g_\alpha=-\sin\alpha\,f+\cos\alpha\,g.
\tag{23}
$$

(5) 的三个 $2\times2$ 矩阵都是标量矩阵，故 (23) 保持所有三矩和非退化性。双线性直接给

$$
\begin{aligned}
G(f_\alpha,f_\alpha)&=A+tX,\\
G(g_\alpha,g_\alpha)&=A-tX,\\
G(f_\alpha,g_\alpha)&=\cos(2\alpha)X.
\end{aligned}
\tag{24}
$$

代回 (6)，得到

$$
\boxed{
L_c(f_\alpha,g_\alpha)=-2t(P+tQ)=0,\qquad
L_s(f_\alpha,g_\alpha)=\cos(2\alpha)(P+tQ)=0.
}
\tag{25}
$$

最后同乘 (18) 的负二分之一次幂，即得归一圆。两个能量同乘该正归一化因子的四次方，所以 (25) 准确保持。

## 5. 旋转参数是尺度的显式有理式

主构造不需要先求一个未知能量比。由 (2) 逐项或 (8) 的变量代换，

$$
G(u(\,\cdot/a),u(\,\cdot/a))(x)=a\,G(u,u)(x/a).
\tag{26}
$$

这里只将紧 integrand 延零后变换共同尾积分；新、旧锚都在实际支撑右方，未把左尾归零。

于是

$$
\frac{A_j(x)}x=\frac{A_*(x/a_j)}{x/a_j},\qquad
S_j=a_j S_*,
\qquad S_*:=S(u)>0.
\tag{27}
$$

式 (20) 的公共 $S_*$ 消去，(22) 准确成为

$$
\boxed{
t=-\frac{\sum_{j=1}^4\operatorname{sign}(v_j)\,v_j^2 a_j^7}
{\sum_{j=1}^4v_j^2 a_j^7}.
}
\tag{28}
$$

因此取有理 $a_j$ 时，t 为显式有理数，与 bump 的形状无关。可用

$$
c=\sqrt{\frac{1+\sqrt{1-t^2}}2}>0,\qquad
s=\frac{t}{2c}
\tag{29}
$$

直接写旋转 $f_\alpha=cf+sg,g_\alpha=-sf+cg$，无需实际求角或数值拟合。

例如 $a_j=1,2,3,4$、$I=[1/2,9/2]$、
$u\in C^\infty_c((19/20,21/20))$，有

$$
(v_1,v_2,v_3,v_4)=(-1/6,1/2,-1/2,1/6),
$$

$$
(w_1,w_2,w_3,w_4)=(1/6,4,27/2,32/3),
\qquad
t=\frac{537}{9305}.
\tag{30}
$$

(30) 是 (13)、(28) 的有限分数代入，不是一次 profile 求积或新的科学运行。任意给定的正 I 内也可选四个有理节点，再选足够小的 $\delta$，故不需要先改变既有几何的物理区间。

## 6. 该平面确实可分离，且没有旧首包条件

(15) 满足

$$
f+g=2\sum_{s_j=1}\sqrt{w_j}u_j,\qquad
f-g=2\sum_{s_j=-1}\sqrt{w_j}u_j.
\tag{31}
$$

两者支撑不交。常数旋转 (23) 不改变这个平面，所以**整条新圆属于 GL(2) 可分离的 profile 平面**。本稿不能作为不可分离圆存在性的证据，也不撤销对分离圆已经发表的任何完整障碍。

另一方面，$|t|<1$ 使 $c\pm s\ne0$。在每个活动包内，旋转后的两个 profiles 一般都同时非零。特别，最左活动包一般没有“f 已开始上升而 g 恒零”的旧结构。故：

- R230/R234 的特定 first-f-up/g0 端层不能直接当成本新圆的端层；
- R217/R219 的非对称导数平台和八个非退化 flux 不由本构造继承；
- R225 的指定内部解析有限退化类，也没有由任意 $C^\infty$ bump 自动实现。

这些界限不影响 (5)、(25) 的准确证明。

## 7. 对真实第三 hook 的直接兼容

每个小包内 $(f',g')$ 是同一个 $u_j'$ 的固定实向量倍数。由 R183 (1) 的完整单层三次 hook 原式及第 2 节导数分包引理，

$$
\mathfrak H\big|_{\mathcal P\times\operatorname{Sym}^2\mathcal P}=0,
\qquad \mathcal P=\operatorname{span}_{\mathbb R}\{f,g\}.
\tag{32}
$$

该引理只使用三个同点正阶导数及同一右积分，不产生跨包的未付内尾。固定旋转 (23) 保持 $\mathcal P$，因此 (32) 仍成立。

这支付真实 $T=\kappa\mathfrak H$ 对此平面的全部三次周期槽；它尚不单独支付完整第三逐 ruling。后者如需与本稿 leading 零同时成立，可使用下一节的重新选角构造。

## 8. 八复制后重新选角，保持完整第三阶

本节取第 3 节的未旋转基本 pair $(f_*,g_*)$。先选择其支撑足够小，使八个完整平移包可放入同一正 I，留两端 collar 和包间正间隔。平移量为

$$
t_j=t_*+jL,\qquad
d_j=(-1)^j\binom7j^{1/3}\quad(j=0,\ldots,7).
$$

令

$$
F_8=\sum_{j=0}^7d_j f_*(x-t_j),\qquad
G_8=\sum_{j=0}^7d_j g_*(x-t_j).
\tag{33}
$$

每个基本 pair 单独满足 (5)，且三复零矩在平移下按三角矩阵变换。因此 (33) 全局仍满足 (5)；导数分包和 (32) 逐小包保持。

### 8.1 有限差分所用的是完整四槽

这里使用的是 R183 第 5 节所引 R46／[R52](R52-overlapping-profile-plane-complete-third-order-circle.md) 的**任意基本三矩包**结论：完整两个二阶 forcing 为差槽 $f_*^2-g_*^2$ 和交叉槽 $2f_*g_*$；两者逐包三矩零，所以其真实二阶解、包括 second 历史，在包外的右尾为零。不存在尚未支付的跨包二阶尾乘另一个包的第一输入。

对任意固定真实变量几何，把
$(f,d),(g,d),(f,c),(g,c)$ 四条完整第三 ruling 平移回基本坐标后，其对 t 的依赖各是次数至多六的多项式。这是 R46/R52 已付的有限分离次数界，不是只对 R193 冻结数值 profile 的拟合。逐包三次幅度为
$d_j^3=(-1)^j\binom7j$，故

$$
\sum_{j=0}^7(-1)^j\binom7j p(t_*+jL)=0
\quad\text{对每个 }\deg p\le6,
\tag{34}
$$

准确消去四条第三 ruling。

对于 R180/R183 已构造的真实闭几何 $M=0,T=\kappa\mathfrak H$，
$\kappa\ne0$，(32) 又消去四条完整周期槽。因此 (33) 在该几何上通过完整二、三阶 range。选几何后再把有限八包放进其共同合法 I；本节没有用 profile 换基去修改几何、frame 或端口。

### 8.2 必须对完成的八包重新选角

不能把第 5 节四尺度的 t 原样沿用到 (33)：$G_0$ 以真实 x 为系数，平移后的各包 bulk 不再由同一四尺度比例 (27) 决定。

但 (33) 的全部微包仍满足 $G_8=\pm F_8$。设其微包为 $b_\nu u_\nu$，相应符号为 $\epsilon_\nu\in\{1,-1\}$，两种符号都出现。于是

$$
A:=G(F_8,F_8)=G(G_8,G_8),\qquad X:=G(F_8,G_8).
$$

三矩使 X 真正紧支撑，各
$\bigl(G(u_\nu,u_\nu)/x\bigr)''$ 的支撑互不交。重复第 4 节的完整边界计算得

$$
P=\sum_\nu\epsilon_\nu b_\nu^4S(u_\nu),\qquad
Q=\sum_\nu b_\nu^4S(u_\nu)>0,\qquad |P|<Q.
\tag{35}
$$

因此为**完整八包**另取 $\sin(2\alpha_8)=-P/Q$，再作共同 O(2) 旋转和共同正归一化，即再次得到 $L_c=L_s=0$。这里 P、Q 是明确的有限准确积分定义，不预填其值，也不声称它们仍等于 (28)。

这个后置 O(2) 不破坏完整第三阶消去。第一输入槽 $(F_8,G_8)$ 按一个二维旋转变换；差／交叉二次槽
$(F_8^2-G_8^2,2F_8G_8)$ 按角度两倍的二维旋转变换。四条第三 forcing／ruling 是这两个二维槽的双线性组合，所以全部四条零在共同换基后仍为零。canonical 二阶解的线性、完整 third forcing 的线性及同右锚范围都是 R52/R183 在四槽中已经付清的对象；不需要重新假设一个未证的单槽局部化。

由此存在：三矩非退化归一、对第三 hook 不可见、完整二三阶 range 已付，并且 R231 两领先能量均零的新圆。它仍然 GL(2) 可分离；没有继承旧首包或 F8 非退化条件，也没有得到完整第四阶解。

## 9. 对例外偶端芽的准确含义

R231 的例外端芽为

$$
h=h_e e^{\varepsilon\sigma^2},\qquad
k=k_e(1-2\varepsilon\sigma^2),\qquad
\omega=\frac{k_e}{h}
\tag{36}
$$

的 $b=0$ 情形，$\varepsilon,h_e>0,k_e\ne0$，并需真实物理支
$x>0,\ x+k_e/h_e>0$。可在满足这两个条件的正 I 上作上述构造；本稿不改变这些几何假设。

R231 已证明 centered ruling 的最高 $h\beta^2$ 系数正是 (6)。所以 (25)，以及八包重新选角版，确实清掉这一整层的所有相位。这与原冻结八包两能量的实际非零结论并不矛盾：profiles、基准第一向量和目标在此已经重新选择。

仍然必须处理 R231 (12)、(18)–(21) 中较低的 second history、third history、local recovery、变化 profile 的链式项及实际三矩商。最高层零不能把它们略去。完整 period 的端点、平台和退化条件也独立保留。

本稿的用途是给下一完整层分析一个准确候选，并说明“对原圆的两个领先能量非零”不能升级为“对一切合法三矩圆都非零”。没有运行新的 payload，没有改原圆实际输出，也没有宣告本课题完成。
