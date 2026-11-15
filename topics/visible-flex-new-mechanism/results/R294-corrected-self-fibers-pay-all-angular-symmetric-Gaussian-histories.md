# R294：校正 self 的有限 C² 纤维支付全部角向对称 Gaussian 二层 history

日期：2026-11-15。**完整纸面构造；未执行符号程序、求积、有限秩扫描、人工检查或研究计算。**

[R293](R293-finite-frequency-zero-of-all-necessary-symmetric-Gaussian-observations.md)在从起点给定的任意有限 polynomial/$C^2$ 观测纤维上，用真实正微包锥与有限频率 IFT 同时支付三十二个 $\theta=\pi/2$ 观测。本稿处理那个特殊角看不到的全部低阶角项。

关键是一个准确的有序公式：每个额外 even 系数由经真实边界补偿的单包 self 和三个真实三矩面积构成。校正 self 是平移次数至多十的 $C^2$ 四次观测。**从最初**显式采用包含这些观测的新有限映射 $\mathcal F^+$，原等背景格点十矩便支付全部 self 和；R280 的三个真实矩面积支付全部 cross。接 R293 后，同一个实际有限频率圆上，十个对称 Gaussian 乘积的三个外矩对所有角度同时为零。

这里不把 $\mathcal F^+$ 冒称为原 $\mathcal F$，也不声称任意已冻结旧圆能无偿保持新观测。构造一次从起点选择新的母包、有限纠正方向与实际 profile；全部原三矩、第三层、72面积和六能量仍同时保留。

来源：[R259 原 local adjoint、真实二次尾及 sl2 表](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md)、[R277 有限低阶纤维](R277-low-jet-observation-fibers-and-high-jet-energy-control-for-equal-background-circles.md)、[R280 三矩面积](R280-ordered-three-moment-areas-and-five-block-Gaussian-cancellation.md)、[R281 解析母包](R281-analytic-packet-fibers-and-finite-canonical-end-germ-conditions.md)、[R282 完整二层系数](R282-symmetric-Gaussian-products-and-an-independent-square-history-gate.md)、[R285 主项分解](R285-principal-splitting-of-symmetric-Gaussian-products.md)、[R289 正锥](R289-universal-even-principal-space-and-positive-real-packet-cones.md)、[R291 完整能量关系](R291-exact-positive-Gaussian-square-moment-is-the-leading-energy.md)及 R293。

## 1. 原平方/cross 规范与两个二次槽

固定原正区间 $I=[\ell,r_*]$、同一个右积分 $Jv(x)=\int_x^{r_*}v$。令 $X,Y$ 为原四 Gaussian 方向中的任意一对，允许 $X=Y$：

$$
B_1=\zeta\Phi_{p_2},\quad
B_{-1}=d_-\Phi_{p_0}+e_-\Phi_{s_1},\quad
B_{-2}=a\Phi_{r_1}+b\Phi_{s_0},\quad
B_{-3}=c\Phi_{r_0}.
\tag{1}
$$

系数、共振 $\varepsilon=\kappa^2/4$、同锚与真实安装完全沿原来源。采用 R289/R293 的通常参数，避开其唯一额外退化；例如可在实际几何初始选择时统一取足够小的 $0<\kappa^2<1/100$，而非修改一个任意已冻结 $\kappa$。

外矩 $I_j$ 为原 $j=0,1,2$ 三矩，$I_2$ 始终含 $2u'v'$。对对称二次槽 $A,B$ 定义

$$
\mathcal B_j(A,B)
=\frac12\{I_j(XA,YB)+I_j(YA,XB)\}.
\tag{2}
$$

它对 $A,B$ 对称。再以外槽极化定义

$$
\begin{aligned}
\mathcal C_j(u\odot v,B)=\frac12\big[
&I_j\{u,X(v,YB)+Y(v,XB)\}\\
+&I_j\{v,X(u,YB)+Y(u,XB)\}\big].
\end{aligned}
\tag{3}
$$

令 $\mathcal K_j=\mathcal B_j+\mathcal C_j$。不要求 $\mathcal C_j$ 的两个二次槽互换对称；下文使用的是准确的对角二次值。

对原三矩圆

$$
\phi_\theta=f\cos\theta+g\sin\theta,\qquad
D_\theta=f\odot f-\phi_\theta\odot\phi_\theta,
$$

用统一 normalized 外矩

$$
q_j^{XY}(\theta)
=-\mathcal B_j(D_\theta,D_\theta)
+\mathcal C_j(\phi_\theta^2,D_\theta).
\tag{4}
$$

$X=Y$ 时(4)就是 R282 的原平方；$X\ne Y$ 时原 history cross 系数为(4)的两倍。检验零不受这个准确非零因子影响，但不能混淆二者。

## 2. 完整角余项的准确形式

写

$$
F=f\odot f,\quad G=g\odot g,\quad H=f\odot g,\quad
\Delta=F-G,\quad s=\sin\theta,\ c_\theta=\cos\theta.
$$

则 $D_\theta=s^2\Delta-2sc_\theta H$、
$\phi_\theta^2=F-D_\theta$，故

$$
q_j^{XY}=\mathcal C_j(F,D_\theta)
-\mathcal K_j(D_\theta,D_\theta).
$$

在原十二完整副本消去 odd 角项以后，准确得到

$$
\boxed{
q_j^{XY}(\theta)
=s^2q_j^{XY}(\pi/2)+s^2c_\theta^2\,\Xi_j^{XY},
}
\tag{5}
$$

$$
\boxed{
\Xi_j^{XY}
=\mathcal K_j(\Delta,\Delta)-4\mathcal K_j(H,H).
}
\tag{6}
$$

(5)是完整槽的四次代数，不是 Taylor 近似。它也说明为什么只把 $\theta=\pi/2$ 的三十个量置零仍不够。

等价地，若 $q=f+ig$，则 $\Xi_j^{XY}$ 是
$\mathcal K_j(q\odot q,q\odot q)$ 的实部；这只是核对式(6)，不是把完整圆改成 pure 问题。下面始终保留两个真实槽。

## 3. 两个二次场的交叉：完整原尾边界

设一个实紧微包 $u$ 的真实矩为

$$
\mathbf m(u)=(m_0,m_1,m_2)
=\left(\int(u'')^2,\ \int x(u'')^2,\
\int\{x^2(u'')^2+2(u')^2\}\right).
\tag{7}
$$

R259 的原左尾 $p_X(\mathbf m)=A_Xx^2+B_Xx+C_X$ 是：

| 算子 $X$ | $A_X$ | $B_X$ | $C_X$ |
|---|---:|---:|---:|
| $P=\Phi_{r_0}$ | $0$ | $0$ | $m_0$ |
| $R=\Phi_{r_1}$ | $0$ | $m_0$ | $0$ |
| $S=\Phi_{s_0}$ | $0$ | $0$ | $m_1$ |
| $L=\Phi_{p_0}$ | $-m_0/4$ | $0$ | $m_2/4$ |
| $U=\Phi_{s_1}$ | $0$ | $m_1$ | $m_2/2$ |
| $Y_+=\Phi_{p_2}$ | $-m_2/4$ | $0$ | $0$ |

原 Gaussian 组合按(1)线性作用于这个表。这里 $Y_+$ 是基本算子，不能和本稿任意第二方向 $Y$ 混同。

令 $p=A_px^2+B_px+C_p$、$q=A_qx^2+B_qx+C_q$。定义准确尾配对

$$
\boxed{
\begin{aligned}
\beta_0(p,q)&=-2A_q(2A_p\ell+B_p),\\
\beta_1(p,q)&=-2A_q(A_p\ell^2-C_p),\\
\beta_2(p,q)&=-2A_q\ell^2(2A_p\ell+B_p)
-2B_q(A_p\ell^2+B_p\ell+C_p).
\end{aligned}}
\tag{8}
$$

若 $u_i$ 在 $u_k$ 左侧，则 $Yu_k^2$ 在整个 $Xu_i^2$ 的非零区间等于 $p_Y(\mathbf m_k)$，于是

$$
I_j(Xu_i^2,Yu_k^2)
=\beta_j\{p_X(\mathbf m_i),p_Y(\mathbf m_k)\}.
\tag{9}
$$

例如 $I_0(V,q)=2A_q\int V''=-2A_qV'(\ell)$；
$I_1(V,q)=2A_q[xV'-V]_\ell^{r_*}$；
$I_2(V,q)=[2A_qx^2V'+2B_qV]_\ell^{r_*}$。
代入真实左尾即为(8)，没有删去 $\ell$ 项。

同一式还给任意两条真实二次输出的 Green 恒等式

$$
I_j(V,W)=\int V\,L_jW+\beta_j(p_V,p_W),
\quad
L_0=D^4,\ L_1=xD^4+2D^3,\ L_2=x^2D^4+4xD^3.
\tag{10}
$$

(9)不是把整个二次场改成左尾；只在真正不交的交叉区域使用它。

## 4. Outer 第三槽的尾作用与完整有序核

使用 R259 的真实一阶作用

$$
D_-u=u',\qquad D_0u=xu'-u,\qquad D_+u=x^2u'-2xu.
$$

对 $p=Ax^2+Bx+C$，原共同锚给：

| $X$ | $X(u,p)$ |
|---|---|
| $P$ | $-2A D_-u$ |
| $R$ | $B D_-u$ |
| $S$ | $-2A D_0u$ |
| $L$ | $(C/2)D_-u-(A/2)D_+u$ |
| $U$ | $B D_0u-A D_+u$ |
| $Y_+$ | $(C/2)D_+u$ |

记这三项系数向量为 $\mathbf a_X(p)$。原三个外矩对这些作用准确为

$$
\begin{aligned}
\mathbf t_-(\mathbf m)&=2\mathbf I(u,D_-u)=(0,-m_0,-2m_1),\\
\mathbf t_0(\mathbf m)&=2\mathbf I(u,D_0u)=(m_0,0,-m_2),\\
\mathbf t_+(\mathbf m)&=2\mathbf I(u,D_+u)=(2m_1,m_2,0).
\end{aligned}
\tag{11}
$$

对固定 $j$，用 $t_{\bullet,j}$ 表示相应分量。完整第三槽的“和”核是

$$
\boxed{
T_j^{XY}(\mathbf m,\mathbf n)
=\frac12\sum_{\bullet=-,0,+}
\left[
a_{X,\bullet}(p_Y(\mathbf n))
+a_{Y,\bullet}(p_X(\mathbf n))
\right]t_{\bullet,j}(\mathbf m).
}
\tag{12}
$$

它就是
$I_j\{u,X(u,p_Y(\mathbf n))+Y(u,p_X(\mathbf n))\}$。
原面积核使用差，本稿必须使用和。

现在定义原二次平方交叉与第三尾共同给出的有序核

$$
\boxed{
\begin{aligned}
\Gamma_j^{+,XY}(\mathbf m,\mathbf n)
={}&\beta_j(p_X(\mathbf m),p_Y(\mathbf n))\\
&+\beta_j(p_Y(\mathbf m),p_X(\mathbf n))
+T_j^{XY}(\mathbf m,\mathbf n).
\end{aligned}}
\tag{13}
$$

这是完整、可直接逐行消费的双线性三矩核。若 $X=Y$，前两项仍各出现一次，第三项也保原两个 outer 项；没有误删对角因子。

## 5. 校正 self：准确消去 C³ 平方和原锚

定义任意 nonlegal 实紧微包的原 self

$$
K_j^{XY}(u)
=I_j(Xu^2,Yu^2)
+I_j\{u,X(u,Yu^2)+Y(u,Xu^2)\}.
\tag{14}
$$

两条 inner 输出各自可以带左尾。校正值为

$$
\boxed{
\widehat K_j^{XY}(u)
=K_j^{XY}(u)
-\frac12\Gamma_j^{+,XY}(\mathbf m(u),\mathbf m(u)).
}
\tag{15}
$$

### 5.1 真实 local 变分公式

R259 给原 cubic local 密度
$F_{X,j}(u)=I_j(u,Xu^2)=\int f_{X,j}(x,u,u',u'')$。
对任意 $v$ 定义仅作为多项式表达的

$$
D_{\rm loc}F_{X,j}(u)[v]
=\int\left(f_u v+f_{u'}v'+f_{u''}v''\right).
\tag{16}
$$

这里不把带尾的 $u+tv$ 假当紧输入族。所用的是 R259 通过 cutoff 证明的真实 adjoint：

$$
2I_j\{u,X(u,v)\}
=\int\{\operatorname{EL} f_{X,j}-L_j(Xu^2)\}v.
\tag{17}
$$

$u$ 紧使 $f_u,f_{u'},f_{u''}$ 的相关边项全零；结合(10)，对(14)得到

$$
K_j^{XY}
=\frac12\{D_{\rm loc}F_{X,j}[Yu^2]
+D_{\rm loc}F_{Y,j}[Xu^2]\}
+\frac12\{\beta_j(p_X,p_Y)+\beta_j(p_Y,p_X)\}.
$$

代入(13)—(15)遂有准确身份

$$
\boxed{
\widehat K_j^{XY}(u)
=\frac12\left[
D_{\rm loc}F_{X,j}(u)[Yu^2]
+D_{\rm loc}F_{Y,j}(u)[Xu^2]
-T_j^{XY}(\mathbf m,\mathbf m)
\right].
}
\tag{18}
$$

所有真实 Green 边项在这里先写全再准确抵消。特别，(18)不含任选左端 $\ell$。改变共同零 collar 内的积分端点，也不会改变校正 self。

### 5.2 它确是 polynomial/C² 观测

原二次表给

$$
(Xu^2)''=\alpha_X(x,u,u',u'')u'''+
\beta_X(x,u,u',u'',J(u''{}^2),J(xu''{}^2),J(x^2u''{}^2+2u'{}^2)).
$$

$\alpha_X$ 是 local 一次多项式；$Xu^2$、$(Xu^2)'$ 和 $\beta_X$ 只需 $C^2$ 数据及三个原 primitive。

因此(18)中唯一可能的三阶导项是
$A(x,u,u',u'')u'''$，**仅线性出现**，没有遗留 $(u''')^2$。其系数 A 是 local 多项式。以最后变量取原函数
$\mathscr A(x,u,v,r)=\int_0^rA(x,u,v,s)\,ds$，便有

$$
Au'''=D_x\mathscr A-\mathscr A_x-u'\mathscr A_u-u''\mathscr A_{u'}.
\tag{19}
$$

$u,u',u''$ 的端值零使总导数边项为零。右边其余各项只需 $C^2$。原 primitive 是固定区间上的连续线性积分作用于二次 $C^2$ 密度；(12)也只是原矩的乘积。

所以 $\widehat K_j^{XY}$ 是固定支持空间上的连续、光滑、四次 polynomial/$C^2$ 泛函。这里的 C³ 平方消失是(18)的准确原式，不是高频极限中的小量断言。

## 6. 真实微包展开及三个 wedge

设从左到右的不交实微包为 $u_i$。对任意实系数 $\lambda_i$，将二次槽写成 $A=\sum_i\lambda_i u_i^2$。原 local adjoint 对外槽二次极化是 local 的，所以不同支持的 outer 交叉为零；inner 的右方尾则严格用(13)。因而

$$
\boxed{
\mathcal K_j(A,A)
=\sum_i\lambda_i^2K_j^{XY}(u_i)
+\sum_{i<k}\lambda_i\lambda_k
\Gamma_j^{+,XY}(\mathbf m_i,\mathbf m_k).
}
\tag{20}
$$

现在回到实际圆
$f=\sum_i a_i u_i,\ g=\sum_i b_i u_i$，
$R_i=a_i^2-b_i^2,\ T_i=a_ib_i$。由(6)、(20)，

$$
\Xi_j^{XY}
=\sum_i(R_i^2-4T_i^2)K_j^{XY}(u_i)
+\sum_{i<k}(R_iR_k-4T_iT_k)
\Gamma_j^{+,XY}(\mathbf m_i,\mathbf m_k).
\tag{21}
$$

三矩是真实的(7)，并满足

$$
\sum_iR_i\mathbf m_i=0,\qquad
\sum_iT_i\mathbf m_i=0.
\tag{22}
$$

将 $\Gamma^+=\Gamma_{\rm sym}+\Gamma_{\rm alt}$，其中两部分按两个矩槽交换分解。由(22)，

$$
\sum_{i<k}(R_iR_k-4T_iT_k)\Gamma_{\rm sym}(\mathbf m_i,\mathbf m_k)
=-\frac12\sum_i(R_i^2-4T_i^2)\Gamma^+(\mathbf m_i,\mathbf m_i).
$$

结合(15)，得到本稿的完整接口

$$
\boxed{
\Xi_j^{XY}
=\sum_i(R_i^2-4T_i^2)\widehat K_j^{XY}(u_i)
+\sum_{0\le r<s\le2}\gamma_{rs}^{XY,j}\,\mathcal A_{rs},
}
\tag{23}
$$

其中，若 $M^{XY,j}$ 是(13)的原 $3\times3$ 双线性矩阵，则

$$
\gamma_{rs}^{XY,j}=(M_{rs}^{XY,j}-M_{sr}^{XY,j})/2,
$$

$$
\boxed{
\mathcal A_{rs}
=\sum_{i<k}(R_iR_k-4T_iT_k)
(m_{r,i}m_{s,k}-m_{s,i}m_{r,k}).
}
\tag{24}
$$

(24)恰为 R280 的三条真实有序面积规范，不另除以2。$m_2$ 包含 $2\int(u')^2$，不是只用中心点或形式尾变量。

这些 $\gamma$ 可由(8)、(11)—(13)有限直接读出；所有左锚项在反对称差中抵消。没有要求每个单包 $\mathbf m_i=0$，也没有把有序核换成未经支付的对称平均。

## 7. 显式新观测 F⁺：从构造起点支付全部 self

### 7.1 有限平移次数

对共同平移 $u_t(x)=u(x-t)$，原 $\widehat K_j^{XY}(u_t)$ 是 t 的次数至多十的准确多项式。

逐原表的界如下：二次方向的显式坐标次数至多4；R259 的 local adjoint $Q_{X,j}$ 至多6。因此 $Q_{X,j}Yu^2$ 的次数至多10，原 $I_j(Xu^2,Yu^2)$ 同样至多 $4+4+2=10$。换回母坐标时，三个右 primitive 的密度只含有限坐标幂；共同右锚位于零 collar，没有另生一个锚常数。(13)的矩核项只需平移后的三矩，次数更低。

这也是(5)中原 odd 角系数可以继续由十二副本准确清掉的次数界。

将(18)的准确 $C^2$ 代表用于这些多项式系数。也可在任意十一种允许小平移上用固定插值线性组合定义系数；因为多项式次数已证明至多十，这仍是同一个有限 $C^2$ 观测，不要求 profile 多出十阶导数。

### 7.2 新映射的明确定义

从一开始定义

$$
\boxed{
\mathcal F^+
=\left(\mathcal F_{\rm old},\
[t^k]\widehat K_j^{XY}(u_t):
X\le Y,\ j=0,1,2,\ 0\le k\le10\right).
}
\tag{25}
$$

最多列出 $30\cdot11$ 个新标量；可以冗余，本稿不声称其真实秩等于这个数。$\mathcal F_{\rm old}$ 是原三矩与全部 Gaussian self 平移观测，故先前所有72面积及 ordered 数据仍受保持。

(25)是**新构造的明确输入**。它不声称这些行都已属于原 $\mathcal F$；R290 对其中一例证明旧 $\mathcal F$ 已足，是另一个更窄的结论。也不在一个已产生的旧圆上强迫添加未知可解的数值约束。本稿采用 R293 的任意有限 $\mathcal F^\star$ 版本，从最初为(25)选择真实最大秩点与有限纠正方向。

### 7.3 等背景格点与完整副本

在每个原等平方背景基本布局内，

$$
b_i^2=B_0,\quad
R_i\in\{-B_0/2,8B_0\},\quad
R_i^2-4T_i^2=\frac{7B_0}{2}R_i.
\tag{26}
$$

原真实格点满足 $\sum_iR_it_i^k=0$，$0\le k\le10$。先从同一个母包 $u_0$ 放置，再只作保持(25)的独立实际母包扰动。每个实际 $u_i$ 的校正 self 和原 $u_0$ 在相同位置的值准确相等。因此

$$
\sum_i(R_i^2-4T_i^2)\widehat K_j^{XY}(u_i)
=\frac{7B_0}{2}\sum_iR_i\widehat K_j^{XY}((u_0)_{t_i})=0.
\tag{27}
$$

两层完整副本的共同正幅使这些四次量同乘真实正四次权。各副本可以有自己的缩放后 $B_0$；每个副本的(27)仍准确成立，不要求所有最终包共享一个全局背景值。

对(24)，每个完整 base 已有(22)，所以不同完整副本之间的 wedge cross 准确为零。原 R280 五个最终完整 block 的真实正权已经同时支付 $\mathcal A_{01},\mathcal A_{02},\mathcal A_{12}$；(25)保持每个真实 $\mathbf m_i$、实际次序及原权，故这三个零继续成立。不是只保 formal tail 的某个替代矩。

代入(23)，得到

$$
\boxed{\Xi_j^{XY}=0\quad
\text{对全部十个 pair 与全部 }j=0,1,2.}
\tag{28}
$$

## 8. 同一个有限频率圆上的完整支付

现在按 R293 从起点使用(25)。它的适用条件已经由§5—7逐项支付：

- 有限、连续、光滑的 polynomial/$C^2$ 观测；
- 包含旧观测，原三矩、原 Gaussian self/ordered 与完整复制不丢；
- 原 even、正解析 prefactor 的最大秩点与 principal 非零子式可按 R281/R289 的同一 polynomial-path 论证同时选择；
- 纠正方向保持为有限个 $\psi$ 乘偶多项式，$C^2$ 纠正与参数导数为 $O(N^{-1})$，不改变原三阶 principal；
- R289 的真实十二交替包正锥与有限多偶形状保留，R291、R286 的两条完整关系保证整个32量始终在准确30维空间内。

R293 因此给某个足够大但**有限** N、严格正有限幅度及同一 $\mathcal F^+$ 纤维，使全部
$q_j^{XY}(\pi/2)$ 和 $L_c,M_c$ 准确为零。没有把 $N=\infty$、点质量、抽象 shape 常数或只投影后的根充当真实 profile。

原十二完整复制同时清 odd 角系数，(28)清掉全部额外 even 系数。由(5)，

$$
\boxed{
q_j^{XY}(\theta)=0
\quad\text{对全部 }\theta,\quad
X,Y\in\{B_1,B_{-1},B_{-2},B_{-3}\},\quad j=0,1,2.
}
\tag{29}
$$

原完整第三与三矩由原包装保持；全部72 Gaussian 面积由旧 $\mathcal F$ 部分保持；$L_s,M_s$ 的 odd 包装及共振的 $N_c=6M_c,N_s=6M_s$ 保六能量。最终共同正归一化只乘各齐次式的公共非零因子，全部零条件保持。

在 R282 的真实独立 Gaussian 词基中，(29)支付十个对称乘积；此前72式支付六个反对称面积。故同一个新构造实际圆的**整个二层 Gaussian history 部分**准确为零。这个结论确实包含整圆角函数，不只是必要的 $\theta=\pi/2$ 子系统。

## 9. 仍须保持的边界

本稿没有消去原独立基中的零层与四个一层 history 系数，也没有由二层零推断 canonical period、全部平台/flux、homogeneous joint、完整第四 ruling或最终有限等距几何存在。原端点与全路径条件继续按已发表的准确接口处理。

(25)是显式新有限观测，而不是对旧冻结 F 的暗中增强。相应的 actual circle、母包及 seed 从起点重新选择；不把它描述成一个旧 fixed-seed 曲面的任意允许变形。所有同锚、真实三矩、支持间隙、正有限宽度与频率均在最终对象中保持。

本文没有发起或重复科学运行。它完成的是：真实尾的完整有序分解、校正 self 的准确 $C^2$ 表示、有限观测的可实施定义，以及与 R293 联用后全部角向 Gaussian 二层系数的共同支付。
