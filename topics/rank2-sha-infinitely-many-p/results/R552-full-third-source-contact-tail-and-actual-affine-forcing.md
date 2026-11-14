# R552 — 全 H3 的纯接触尾像与原完整 forcing 的逐层相容

日期：2026-11-14。**状态：已证明。** 本篇计算 R547 的纯 \(\xi\) 尾在加入
整个原 \(\mathcal H_3\) 后的准确像。原接触余核
\(\operatorname{coker}E_q\) 还须商掉第一连接的像，以及第二连接中
通过上层测试的那部分像；不能只商掉两个连接的核。

随后将 R502 的完整首 Bockstein 分成一个完全不含 \(\xi\) 的已知向量，
和准确系数为 \(3e\xi\) 的纯接触尾。
原低行右逆的高尾、活着的 \(V_1/f_2\)、全部其余原列都进入同一消元。
得到整个原来源首次可解性的一个准确仿射判据，而非较小显示子格的判据。
本篇没有证明最终指定类非零，也没有由此新增中央零或全局斜率估计。

## 1. 同一个原目标及两种合法长度

保 R495、R498、R502、R524、R547、R550 的实际因子与整提升：
$$
P^{\rm fact}=d^{-C_D}t^rQF^3\in\mathcal W_D,\qquad
d=1+8t,\qquad
p=6s-1>83,
$$
$$
1\le\ell\le r<h,\qquad
0\le k=2h+r-s<\ell.
\tag{1}
$$
\(C\subset X\) 是同一个十九角严格变换，
\(N=\mathcal O_C(C)\)、\(\kappa=C^2\)、\(\chi=-K_XC\)，
\(P=(0,1)\) 为同一个有理光滑点。仍记
$$
\mathcal H_j=H^0(X,\mathcal O_X(jC)),\qquad
e=(\mathcal EF)|_C,\quad f_2=(\mathcal E^2F)|_C .
$$
\(e(P)\ne0\)，所有正规系数在原 \(P\) 框中读取。

以 \(\Delta=0\) 表示相对 \(J\)，以 \(\Delta=13\) 表示本候选的整个原
\(M=c_*U_0m_{13}J\) 首次提升。设置
$$
s_\Delta=s-\Delta,\qquad T=s_\Delta-r,\qquad q=T-h.
\tag{2}
$$
沿用 R550 的强窗
$$
\boxed{h>\kappa,\qquad q>\kappa,\qquad T\le2h.}
\tag{3}
$$
特别 \(0<q\le h<T<p\)。

原高双块为
$$
\mathcal A_T=k[[t]][\epsilon]/(t^T,\epsilon^2),\qquad
\zeta\longmapsto\eta+a\epsilon,\qquad
\eta=t^hu,\quad u(0)\ne0,\quad\eta^2=0\bmod t^T .
\tag{4}
$$
\(a=p\kappa_{\rm Gau}\) 是原 Gaussian 单位，不与曲线交数混同。

对 \(\Delta=13\)，(2) 不是把原目标的十三行删除。
先使用整个 \(c_*U_0\) 的整单位逆，再按 R479 的真实 \(m_{13}\) 分解：
在首 Bockstein 上，两条相对块只读 \(<s-13\)，第三块仍读原 \(\ell\) 行。
本候选在 \(\ker\bar J\)，所以其原首 Bockstein 在另两条十三行的
初始空带中为零；任一 \(\bar M R\) 在这些带也为零。
因此针对本候选的首次可解性，恰等价于这个投影问题。
原 \(B_0,B_1\) 是解出同一个 \(R\) 后的完整相对高尾，未被设成自由参数。
完整第三精度仍使用 R481，见第9节。

## 2. 两个准确局部映射

写 \(z=z_0+\epsilon z_1\in\mathcal A_T\)，定义
$$
\boxed{v(z)=z_0-\frac{\eta}{a}z_1\in k[t]/t^T.}
\tag{5}
$$
若 \(G=g_0+\zeta g_1+\zeta^2g_2\) 来自同一个 \(\mathcal H_3\)，
则
$$
\operatorname{ev}(G)
=g_0+\eta g_1+\epsilon a(g_1+2\eta g_2),\qquad
v(\operatorname{ev}G)=g_0=G|_C\bmod t^T.
\tag{6}
$$
这里是已支付前缀后的高目标；没有在原 raw \(\bar\Gamma\) 中令
\(\zeta^3=0\)。

令 \(u_F=e+f_2\eta\)，这是原点单位。准确有同构
$$
\boxed{
j_F:k[t]/t^T\xrightarrow{\sim}\ker v,\qquad
f\longmapsto \eta u_F f+\epsilon a u_F f .
}
\tag{7}
$$
其逆为 \(z\mapsto z_1/(a u_F)\)。原二倍来源满足
$$
\boxed{j_F(E_{\rm mir}(H))=\operatorname{ev}(FH),}
\qquad
E_{\rm mir}(H)=H(t,\psi e^{2\eta})\bmod t^T .
\tag{8}
$$
确切单位 \(u_F\) 在 (7)–(8) 中完整保留。

本篇的纯接触尾用下列固定归一：
$$
\boxed{
\iota_\xi:k[t]/t^q\longrightarrow\mathcal A_T,\qquad
x\longmapsto 2a e^2\eta\,\epsilon x
=j_F(2e\eta x).
}
\tag{9}
$$
它是单射，像就是 R547 的 \(\epsilon\eta\,k[t]/t^T\)。
对真实 \(H_1\in\mathcal H_1\)，
$$
\operatorname{ev}(F^2H_1)=\iota_\xi(E_q(H_1)),
\quad E_q(H_1)=H_1|_C\bmod t^q.
\tag{10}
$$
(9) 的系数二和 \(e^2\) 不能在之后的 forcing 中另换归一。

## 3. 第一连接的像准确支付多少接触尾

记真实有限余核
$$
C_q=\operatorname{coker}E_q,\qquad
C_{\rm mir}=\operatorname{coker}E_{\rm mir},
$$
$$
C_h=\operatorname{coker}E_h,\qquad
E_h:\mathcal H_2\to k[t]/t^h,\quad H\mapsto H|_C\bmod t^h .
\tag{11}
$$
所有来源均为已付十九角有限格的约化；没有添加独立 normal 系数。

令
$$
V_2=H^0(C,N^2(-hP)),\qquad
\alpha=\alpha_\eta:V_2\to C_q
$$
为 R524 的同一第一连接。具体地，对任意真正的
\(H_2\in\mathcal H_2\) 提升 \(v_2\)，
$$
\alpha(v_2)=\left[\frac{E_{\rm mir}(H_2)}{2e\eta}\right]\in C_q .
\tag{12}
$$
除法只在已知 \(t^h\) 像中进行，读长 \(q\)。

**定理1。** 准确有
$$
\boxed{
0\longrightarrow C_\alpha:=C_q/\alpha(V_2)
\xrightarrow{\,2e\eta\,}C_{\rm mir}
\xrightarrow{\pi_h}C_h\longrightarrow0.
}
\tag{13}
$$

**证明。** 镜轴评价模 \(t^h\) 正是 \(E_h\)，故末映射满射。
其核由 \(t^h k[t]/t^T=2e\eta\,k[t]/t^q\) 表示。
一个真实 \(H_2\) 的镜轴值在这个尾中，当且仅当
\(H_2|_C\in V_2\)。
同一个值层的不同提升恰相差 \(FH_1\)，其镜轴值为
\(2e\eta E_q(H_1)\)。
因此尾中被真实二倍来源支付的向量，准确是
\(E_q(\mathcal H_1)+\alpha(V_2)\)，得到 (13)。证毕。

这里是 \(\alpha\) 的**像**，不是 \(\ker\alpha\)。
R524/R550 对同一首核的描述不会允许把这份像省去。

## 4. 第二连接再支付的准确子空间

令
$$
V_3=H^0(C,N^3(-TP)),\qquad
\beta=\beta_\eta:V_3\to C_{\rm mir}
\tag{14}
$$
为 R524 的第二连接。对同一个真实提升
\(G\in\mathcal H_3\)、\(G|_C=v_3\)，它准确为
$$
\beta(v_3)=
\left[\frac{g_1+2\eta g_2}{e+f_2\eta}\right]\in C_{\rm mir}.
\tag{15}
$$
特别 (15) 不能只保 \(g_1\)。

定义
$$
\boxed{
\bar\beta=\pi_h\beta:V_3\to C_h,\qquad
V_3^0=\ker\bar\beta.
}
\tag{16}
$$
由 (13)，\(\beta(V_3^0)\) 在其首子空间内，故有唯一实际映射
$$
\boxed{\beta_0:V_3^0\to C_\alpha,\qquad
(2e\eta)\beta_0(v_3)=\beta(v_3).}
\tag{17}
$$
它仍由同一个 \(G\)、同一个二倍修正和原单位计算。
不是给每个 \(v_3\) 独立选一个自由尾。具体地，置
\(f_G=(g_1+2\eta g_2)/(e+f_2\eta)\)；
因为 \(\bar\beta(v_3)=0\)，可且只可用真正的
\(H_2\in\mathcal H_2\) 解
\(E_h(H_2)=f_G\bmod t^h\)。随后
$
\boxed{
\beta_0(v_3)=
\left[\frac{f_G-E_{\rm mir}(H_2)}{2e\eta}\right]\in C_\alpha .
}
\tag{17a}
$
不同的这样的 \(H_2\) 差一个值层落在 \(V_2\) 的真实截面，
其差准确由 (12) 支付；所以 (17a) 无选择歧义。

令
$$
U=\operatorname{coker}(\operatorname{ev}:\mathcal H_3\to\mathcal A_T),
\qquad
C_3=\operatorname{coker}
(\mathcal H_3\xrightarrow{G\mapsto G|_C\bmod t^T}k[t]/t^T).
\tag{18}
$$

**定理2。** 纯接触尾在整个原 \(\mathcal H_3\) 余核中的像准确是
$$
\boxed{
D_\xi=C_\alpha/\beta_0(V_3^0)
=
\frac{\operatorname{coker}E_q}
{\alpha(V_2)+\beta_0(V_3^0)},
}
\tag{19}
$$
其中第二个式子的 \(\beta_0\) 项按其在 \(C_\alpha\) 中的逆像理解。
更精确地，(9) 诱导一个单射 \(D_\xi\hookrightarrow U\)，且有准确序列
$$
\boxed{
0\to C_{\rm mir}/\beta(V_3)\to U\to C_3\to0,
}
\tag{20}
$$
$$
\boxed{
0\to D_\xi\to C_{\rm mir}/\beta(V_3)
\to C_h/\bar\beta(V_3)\to0.
}
\tag{21}
$$

**证明。** (5) 对原 \(\mathcal H_3\) 的限制是普通值 jet。
若目标向量的值层已由同一个 \(G\) 支付，余向量落在 \(\ker v\)，
由 (7) 唯一写成长度 \(T\) 的镜轴目标。
改变 \(G\) 的值层提升，先有 \(F\mathcal H_2\)，给
\(E_{\rm mir}\)；再有 \(V_3\) 的真实提升，给 (15) 的 \(\beta(V_3)\)。
这证明 (20)。

现在把 (13) 商掉 \(\beta(V_3)\)。
它与首子空间 \(C_\alpha\) 的交准确是
\(\beta(V_3^0)\)：若 \(\beta(v_3)\) 在首子空间，
则 \(\bar\beta(v_3)=0\)，反向显然。
所以首子空间之商恰为 (19)，得到 (21) 及所述单射。证毕。

这给一个直接的精确吸收判据：
$$
\boxed{
\iota_\xi(x)\in\operatorname{ev}(\mathcal H_3)
\quad\Longleftrightarrow\quad [x]=0\text{ 于 }D_\xi .
}
\tag{22}
$$
因此 \([x]\ne0\) 于 \(\operatorname{coker}E_q\) 本身不足以判非零。
即使第一连接像已商掉，也仍须保 (17)。

### 有限容量核对

在 (3) 下，\(E_q\) 的准确秩为 \((\kappa+\chi)/2\)。
故
$$
\boxed{
\dim D_\xi
=q-\frac{\kappa+\chi}{2}
-\operatorname{rank}\alpha-\operatorname{rank}\beta_0,
}
\tag{23}
$$
$$
\operatorname{rank}\beta_0=\dim\ker\bar\beta-\dim\ker\beta .
\tag{24}
$$
这不同于把 \(\ker\alpha,\ker\beta\) 的维数直接相减。
(20)–(21) 的总长度与 R550 完全相符：
若 \(a_\eta=\dim\ker\alpha,b_\eta=\dim\ker\beta\)，
$$
\dim U=2T-\frac{9\kappa+3\chi}{2}+a_\eta+b_\eta .
\tag{25}
$$
这些是同一约化矩阵的准确像、核和余核计算；
不由来源整性推断其物理像 \(p\)-饱和。

## 5. 完整首 Bockstein 的 ξ 恰只进入最后这个尾

使用 R502 的同一整分支和唯一低次分解
$$
\log(g/\widetilde\psi)=t^hu+p\xi,\qquad
\xi\in\mathcal O[t]_{<h},\qquad
b_s=(t/w(t))^s .
\tag{26}
$$
\(b_s\) 是完整原单位，仍用真实 \(s\)，不以较短的 \(s_\Delta\) 替代。
R502 的第三块 forcing 是
$$
T_2=3a\,b_s t^k u^2V_0\bmod t^\ell,\qquad
V_0=(d^{-C_D}Q)|_C\,e^3 .
\tag{27}
$$
它不含 \(\xi\)。

取 R498 用原相邻 charge 选定的整个低行右逆，置
$$
L_\beta=\mathscr L_{\rm low}(0,0,T_2)\in\overline{\mathcal W}_D .
\tag{28}
$$
它填满原 \(2r+\ell\) 条低行，全部高尾保持。
经同一 \(t^{-r}\mathfrak q_{\rm phys}^{-1}\) 的已知高像归一，
记其前两块为 \(\ell_0+\epsilon\ell_1\)，
其中 \(\mathfrak q_{\rm phys}=d^{-C_D}Q(t,Y_{\rm phys})\)。
对 \(\Delta=13\) 只作 (2) 的合法较短截断；(28) 是同一实际低行操作。

R502 已付的整个剩余高向量现在准确为
$$
\boxed{
b=b_{\rm car}+\iota_\xi(3e\xi),
}
\tag{29}
$$
其中
$$
\boxed{
b_{\rm car}=-\ell_0+
\epsilon\left[
b_se^3u^3t^{h+k-r}
+\frac32b_se^2f_2u^4t^{2h+k-r}
-\ell_1
\right]\in\mathcal A_T .
}
\tag{30}
$$
所有系数在本节取模 \(p\)，长为同一 \(T\)。

**证明。** R502 的完整 \(V_1\) 与物理 \(Q\) 单位运输给第二块
$$
b_se^3u^3t^{h+k-r}
+6ae^3u\xi t^h
+\frac32b_se^2f_2u^4t^{2h+k-r}.
$$
中间项恰为 (9) 中 \(x=3e\xi\) 的系数。
减掉整个 (28) 的高尾，得到 (29)–(30)。
第一块没有别的 \(\xi\) 项；(27) 也不含它。证毕。

因此 (20) 的值层条件以及 (21) 的下一层条件全部不含 \(\xi\)。
只有在这两层通过之后，真实算术提升量 \(\xi\) 才以准确的
\(3e\xi\) 进入最终仿射类。
这没有把 \(\xi\) 当作可调参数，也没有删除活着的 \(f_2\) 项或
低行高尾。

为具体说明 (28) 使用真列，在 \(\ell=r=1,k=0\) 时，
原 charge \(0,1,2\) 给
$$
H_{\rm low}=1-2Y-\frac{t-1}{d}Y^2\in\mathcal W_2,\qquad
L_\beta=\frac{T_2(0)}{a^2}H_{\rm low}.
\tag{31}
$$
因为 \(q_0=q_1=1,q_2=(t-1)/d\)，其两个普通低值均为零，
且第三常数行恰为 \(a^2\)。
这是一条完整有理来源，不能只保它的第三常数而省掉前两块高尾。
本篇后面的判据不限于这个最小例。

## 6. 其余全部原列必须以同一个核加入

(19) 已使用整个 \(\mathcal H_3\)，仍不是整个 \(\mathcal W_D\)。
下面支付全部其余列，不假定它们分别只改变某一层。

对每个真正的原列 \(R\in\overline{\mathcal W}_D\)，先在同一原目标上定义
$$
\widehat R=
R-\mathscr L_{\rm low}(\operatorname{low}\bar J_\Delta R).
\tag{32}
$$
它仍属于同一原来源，全部低行恰为零。
将其完整高像按第5节归一后，取在 (18) 中的类，得到真实有限矩阵
$$
\boxed{\sigma:\overline{\mathcal W}_D\longrightarrow U.}
\tag{33}
$$
允许 (33) 用全部原基列作为冗余自由呈示；
无需先挑一个未经证明的来源补空间。
显示的 \(d^{-C_D}t^rQ\mathcal H_3\) 列在 (33) 中为零，
其他原列的高尾均未删去。

令
$$
Q_{\rm up}=U/D_\xi,\qquad
\bar\sigma:\overline{\mathcal W}_D\to Q_{\rm up},\qquad
W^0=\ker\bar\sigma .
\tag{34}
$$
由 (20)–(21)，\(Q_{\rm up}\) 具有准确序列
$$
0\to C_h/\bar\beta(V_3)\to Q_{\rm up}\to C_3\to0.
\tag{35}
$$
它一般不是两个余核的直和。

对 \(R\in W^0\)，\(\sigma(R)\) 在 \(D_\xi\) 的真实单射像内，
故唯一给出
$$
\boxed{\nu:W^0\to D_\xi,\qquad
D_\xi^{\rm actual}=D_\xi/\nu(W^0).}
\tag{36}
$$
这里必须取 (34) 的**共同核**。
把所有原列各自的接触尾投影任意加入，会丢掉它们在上两层的真实输出。

同样的蛇形论证给
$$
\boxed{
D_\xi^{\rm actual}\hookrightarrow
\mathcal A_T/
\bigl(\operatorname{ev}\mathcal H_3+
\operatorname{high}\bar J_\Delta(\ker\operatorname{low})\bigr),
}
\tag{37}
$$
其像准确是原纯接触尾的像。
这次已经加入整个原来源；没有把显示子格的余核冒充原余核。

## 7. 原完整首次提升的准确仿射判据

将 (30) 的类记为 \([b_{\rm car}]\in U\)。

**定理3。** 同一个 \(P^{\rm fact}\) 可在原来源中作所选
\(\Delta\) 的首次提升，当且仅当下面两步同时成立。

首先，完全不含 \(\xi\) 的上层类必须满足
$$
\boxed{
[b_{\rm car}]\bmod D_\xi\ \in\operatorname{im}\bar\sigma .
}
\tag{38}
$$
若 (38) 成立，取一个同格 \(R_0\) 达到该值。
则 \([b_{\rm car}]-\sigma(R_0)\) 唯一属于 \(D_\xi\)，定义其在 (36) 中的类
$$
\gamma_{\rm car}
=\bigl[[b_{\rm car}]-\sigma(R_0)\bigr]\in D_\xi^{\rm actual}.
\tag{39}
$$
第二步准确为
$$
\boxed{\gamma_{\rm car}+[3e\xi]=0
\quad\text{于同一个 }D_\xi^{\rm actual}.}
\tag{40}
$$
(39) 不依赖所选 \(R_0\)。

**证明。** 由 (29)，纯 \(\xi\) 项在 \(Q_{\rm up}\) 中为零，
所以任何真正吸收首先必须满足 (38)。
取一个实际 \(R_0\) 后，剩余类属于 \(D_\xi\)。
所有保持上层已解值的进一步原修正，恰来自 (34) 的 \(W^0\)，
其接触输出就是 (36) 的 \(\nu(W^0)\)。
因此存在最后修正，当且仅当 (40)。
改变 \(R_0\) 恰加一个 \(W^0\)，所以 (39) 良定义。证毕。

这个判据是充分且必要的有限原矩阵条件。
每一次使用 \(V_2,V_3\) 的连接，都可由 R524 的真实全局截面提升；
每一次使用 (33) 都是原基列的组合。
最终把 (28)、(32) 和所用 \(\mathcal H_3\) 列取相反号补回，
得到**同一个**实际首次修正 \(R\)。
没有只解几个独立 jet 后宣布它们属于一个来源。

(38) 可按 (35) 先解普通值层，再解较低镜轴层；
但必须使用同一个实际来源及其上一步解空间。
(40) 也不能在 (38) 尚未通过时独立使用。

## 8. 提升选择与精确范围

改变合法的原因子整提升时，
\(\xi\) 的接触部分按 R507 改变 \(H/e\)，其中 \(H\) 是同一真实
\(\mathcal H_1\) 的限制。
其 \(3e\xi\) 改变 \(3E_q(H)\)，已在 (10) 中支付。
更一般的同来源基准改变，连同 (28)–(33) 的对应改变，
只是给原首 Bockstein 加一条原像；
(38)–(40) 的整体真假因而不变。
这不允许把任意 \(k[t]_{<q}\) 的 \(\xi\) 改成零。

(19)、(36) 给出一个实际的排除边界：
即使 \([3e\xi]\ne0\) 于最初的 \(\operatorname{coker}E_q\)，
它也可能先被 \(\alpha(V_2)\) 支付，
再被 \(\beta_0(\ker\bar\beta)\) 支付，
最后被保持上两层的真正原列核 \(\nu(W^0)\) 支付。
反过来，任何这些支付都必须经过同一实际映射，不能凭维数假定可达。

R547 增补的显示子格最后因子恰为 \(p\) 仍完全成立：
该子格没有 (28) 的低行列。
本篇正把低行单位被抵消之后的全部真实余项接到原像，
所以没有将该 \(p\) 因子直接认作全 \(M\) 的 Smith 因子。

## 9. 原两条 carry、第三精度与主目标

\(\Delta=0\) 的 (38)–(40) 判定相对
\(J(P^{\rm fact}+pR)\in p^2\Gamma\)。
\(\Delta=13\) 判定同一个原
\(M(P^{\rm fact}+pR)\in p^2\Gamma_+\)；
它不要求相对 \(J\) 也被 \(p^2\) 整除。

在后一个情形，R479 的 \(B_0,B_1\) 由解出的完整 \(R\) 唯一恢复。
继续到下一位时，必须保这个 \(R\)、两条十三行 carry、
\(P_{134}/U_0\)、\(U_1/p\) 及 R481 的完整
\(d_2^J\to G_2\) 投影；(36) 不是第二余核 \(G_2\) 的替代定义。

三条原完整中央仍只约束原实际参数。
本篇没有给 \(\mathcal H_j\)、\(\widehat R\)、连接来源或其乘积新增中央零。
现已得到的完整新接口是：
原全部列加入后，上两层为不含 \(\xi\) 的真实可解性问题，
最后只有 (40) 这一指定仿射类。
要取得非零，仍须证明 (38) 失败，或在其通过后证明
(40) 的实际左侧非零；不能只证明某个环境尾或较小比较余核中的非零。
