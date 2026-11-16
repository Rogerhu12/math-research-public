# R450：真实周期逆后的最高第二规范七余系数与完整宏复制消去

日期：2026-11-16。**完整原式纸面证明；没有执行新的符号、积分、profile、秩、零点、开发检查或科学计算。**

[R444](R444-original-hook-response-action-and-the-highest-second-period-blind-row.md) 已证明当前十二个 $g$ 翻号完整副本使八个 hook 响应的最高第二规范作用为零，也消掉该行的真实 incoming 修正。它没有证明实际 canonical 或 prototype 基准本身为零。本稿直接保留完整周期源及其真正的 $L_f$ 逆，处理这个差别。

准确的新结论是：

- 完整 scalar self 及其有序 $2+2$ 输出的共同平移次数至多十一。这个界来自全 $U$ 真权和 R356 的完整最低权身份，绝非左二次 self 尾的次数界。
- 在十二个真实不同中心的完整周期源确实属于同一个紧 $L_F$ 像的前提下，可构造一次统一的、次数至多十一的紧逆解多项式。最高规范读出次数至多十七。因此当前十二副本留下一个明确的至多六次宏中心多项式；本稿不将它擅自置零。
- 从起点在原十二包装外再放八个完整、四次幅权的 $g$ 翻号宏副本，第十一与第七有限差分一起准确消掉这个完整十七次读出。这项结论对实际最终成本的全部基准适用，但仍以其真正周期像条件为前提。
- 新增宏复制可从起点纳入 R447 的同一二十目标构造。原十九门和非零 $d_f(P)$ 可在这个新库上同时保持；没有修改旧冻结圆后冒称其目标未变。

整个证明保留同一几何、原右锚、所有 affine/quadratic 左尾、实际宽度与幅度及同一个二阶规范。它不支付完整周期像、其余九个端口行或 signed 响应的 actual 零基准实现。

## 1. 原对象与本稿实际使用的三层条件

令 $U$ 是原真实完整 canonical 第四成本空间。固定一条实际最终路径，其总矩阵和第三成本为
$$
M_{\rm total}=0,\qquad T_{\rm total}=\tau\mathfrak H,\qquad \tau\ne0,
$$
并采用已经支付的 whole pure 与 whole self 条件
$$
\pi V=0,\qquad \mathcal Q_{\rm all}(V)=0.
\tag{1}
$$
完整的 $J^+$ 还包含当前共同自然查询和 universal ordered 查询；本稿的拆分只使用其中(1)，不把较强条件删出实际联合问题。

总第三系数 $\tau$ 不是有理端芽的曲率 $\kappa$。所有输出来自同一个原右 collar 和同一全路径起点。

一个固定完整 base 写为
$$
F=\sum_i a_i u_i,\qquad G=\sum_i b_i u_i,\qquad
R_i=a_i^2-b_i^2,\quad T_i=a_ib_i,
\tag{2}
$$
其中实际微包值支撑不交，宽度与内部位置全部固定。该 base 已包括原完整八复制，并满足
$$
\mathbf I(F,F)=\mathbf I(G,G),\qquad \mathbf I(F,G)=0.
\tag{3}
$$
它也保持原完整第三条件及 R326 的全部 cubic 三矩零式。式(3)来自 R277 的真实格点矩、后续保矩纤维和完整副本，不要求任一单微包三矩为零。

写
$$
\phi_\theta=F\cos\theta+G\sin\theta,\qquad
V_\theta=\sin^2\theta\,V_d+2\sin\theta\cos\theta\,V_e .
$$
这里 $V_e[V;F,G]$ 指原 canonical 成本的第二系数，不先施 incoming 端口清理。相应源为
$$
G_e^0[V;F,G]=-\frac{V_e[V;F,G]}{2\tau}.
\tag{4}
$$

必须区分：

1. 原成本(1)及其输出函数已经定义；
2. 某一实际源(4)确实属于 $L_F(C_c^\infty)$；
3. 一个二阶逆解还同时满足原十三个端口行。

第2项未由第1项自动推出；第3项也未由第2项自动推出。下文所有最高规范读出只在第2项的真实像域上使用。

## 2. 原最高行及同锚周期算子的协变

记
$$
L_F(k)=\mathfrak H(k;F,F),\qquad
Y=\Phi_{p_2},\qquad
\ell_F(k)=I_2\{Y(F,F),k\}.
\tag{5}
$$
$Y$ 的原输出通常带纯二次左尾。R437 已证明
$$
\ell_F|_{\ker L_F}=0,\qquad
P_{2,\theta}(k)=\frac{\kappa}{24}\ell_F(k).
\tag{6}
$$
所以真实像泛函
$$
\mathfrak p_F(L_Fk)=\ell_F(k)
\tag{7}
$$
与紧特解的选择无关。它不在尚未入像的目标上预先定义。

令 $T_tu(x)=u(x-t)$。原 $P,R,S$ 公式及共同右零 collar 给
$$
L_{\gamma T_tF}(T_tk)=\gamma^2T_t(L_Fk),\qquad \gamma\ne0.
\tag{8}
$$
这里 $L_F$ 本身平移不变，$R$ 和 $S$ 各自的平移项在原 hook 组合中准确相消。原右积分换元后的上端仍在零 collar；没有新加左常数。

写
$$
p=F',\quad r=F'',\quad A_F=6F'F'''-2(F'')^2 .
$$
原局部身份为
$$
L_F(k)''=(A_Fk'')'-6(rF''')'k'.
\tag{9}
$$
因此 $L_F$ 只读取各活动包附近的 $k'$ 及其导数；间隙内的修改和活动包上的常数平台不改变(9)。整个输出仍由原右零值及零一导唯一恢复，不能任取左仿射常数。

R442 的完整配对还给
$$
\boxed{
\ell_F(k)=-\int x^2\left(F-xF'+\frac{x^2F''}{2}\right)^2k''' .
}
\tag{10}
$$
真正紧的是 $k$ 和 outer profile 的端 jets；未截断 $Y(F,F)$ 的左二次尾。

## 3. 完整 scalar 输出的十一阶位置上界

定义整个 self 输出
$$
\Sigma_V(u)(x)=V(u\odot u,0)(x).
\tag{11}
$$
它不同于 $\mathcal Q_{\rm all}$ 的左二次系数，也不同于自然积分 $\Lambda_u$。

[R190](R190-complete-weight-plus2-quotient-vanishes-and-remaining-even-weights.md) 与 [R203](R203-general-pure-lowest-two-weights-vanish.md) 的原有限仿射表示给
$$
U=\bigoplus_{\sigma=-9}^{3}U_\sigma,\qquad
N(U_\sigma)\subseteq U_{\sigma-1},
\tag{12}
$$
其中 $N$ 是同时输运全部输入和输出的真实平移导子。[R356(33)](R356-lowest-two-full-self-weights-and-universal-total-flux-cancellation.md) 的完整输出身份是
$$
\boxed{\Sigma(U_{-9})=0.}
\tag{13}
$$
**R356 没有给 $\Sigma(U_{-8})=0$**；其真实两个模板和仿射左尾均保留。本稿只使用(13)。

对任意 $V\in U$，$N^{12}V_\sigma$ 在 $\sigma\le2$ 时落到原支撑以下；在 $\sigma=3$ 时落到 $U_{-9}$。故
$$
\boxed{\Sigma_{N^{12}V}(u)\equiv0\quad\text{对全部紧 }u.}
\tag{14}
$$
真实仿射协变于是给
$$
T_{-t}\Sigma_V(T_tu)=\Sigma_{e^{tN}V}(u)
=\sum_{m=0}^{11}\frac{t^m}{m!}\Sigma_{N^mV}(u).
\tag{15}
$$
这是整个 profile 输出函数的有限多项式，包括全部左尾。

对两个不交包 $u<v$，原 self 极化没有奇次数项；定义
$$
U_V(u,v)=\Sigma_V(u+v)-\Sigma_V(u)-\Sigma_V(v).
\tag{16}
$$
它就是原有序 $2+2$ 输出。因此(15)也直接给(16)的完整共同平移次数至多十一。没有由 $\Omega$ 或左尾的次数外推全函数。

式(14)—(16)最初在一个共同物理合法的开放位置区间上使用。比较有限多项式系数不要求把任何实际支撑移出允许窗口；式中的原函数锚始终可以在同一右零 collar 内取共同值。

## 4. 先消真实跨完整 base 的第二周期尾

R389 在 whole pure 为零时给完整输出
$$
V_e[V;F,G]
=-\sum_i a_i^2
\left[T_iS_i+\sum_{j>i}T_jU_{ij}\right],
\tag{17}
$$
其中
$$
S_i=\Sigma_V(u_i),\qquad U_{ij}=U_V(u_i,u_j).
$$
$S_i,U_{ij}$ 在 outer 包右侧为零，左侧为真实二次多项式。由 whole $\mathcal Q_{\rm all}=0$，这个左尾至多仿射。

若两个完整 base 的包络严格不交，左 base 内一个固定 outer 包与右 base 的全部交叉项准确为
$$
\sum_{j\ {\rm in\ right\ base}} T_jU_{V,u_i}(\mu(u_j))
=U_{V,u_i}\left(\sum_jT_j\mu(u_j)\right)=0,
\tag{18}
$$
因为原完整第二尾对右三矩线性，而(3)给 $\sum T_j\mu(u_j)=0$。这消掉的是整个输出函数，不仅总通量或左二次系数。

将 base 同时变为
$$
(\gamma T_tF,\ \epsilon\gamma T_tG),\qquad
\epsilon\in\{1,-1\},\quad\gamma>0,
$$
则(17)准确乘 $\epsilon\gamma^4$。对任意有限组这样的完整 base，
$$
\boxed{
G_e^0[V;f,g]=
\sum_\nu\epsilon_\nu\gamma_\nu^4\,T_{t_\nu}\mathcal G(t_\nu),
}
\tag{19}
$$
其中把同一个 base 的源拉回固定坐标：
$$
\mathcal G(t)=T_{-t}G_e^0[V;T_tF,T_tG].
\tag{20}
$$
对不同完整 base 类型分别取自己的 $\mathcal G$ 后相加，完全相同。

由(15)—(17)，
$$
\boxed{\mathcal G(t)=\sum_{m=0}^{11}t^mG_m.}
\tag{21}
$$
所有 $G_m$ 是实际输出的函数系数。它们可能有非零左仿射尾；此处不先宣称它们在 $L_F$ 像中。

## 5. 总 range 与逐副本真 range：原间隙延拓证明

下面给出插值前必须支付的条件。

**拆分引理。** 在(1)、(3)及严格不交完整 base 包络下，(19)属于整个 $L_f(C_c^\infty)$，当且仅当每个相应的 $\mathcal G(t_\nu)$ 属于同一个 $L_F(C_c^\infty)$。不同 base 类型使用各自的固定 $F$。所有紧输入可取在各 base 预留的共同包络及两侧空 collar 内。

充分性由(8)、(9)及共同右零值相加得到：严格不交使 $A_f$ 及(9)其余 profile 系数逐包相加，右锚唯一恢复整个输出。必要性不能只凭形式分块，证明如下。

设 $L_fk=G_e^0$，$k$ 是一个真实全局光滑紧解。对第 $\nu$ 个 base，其他输出在其包络上要么为零、要么为真实仿射函数，所以其二导为零。由(9)，在这个 base 的全部活动包上，
$$
L_{\gamma_\nu T_{t_\nu}F}(k)''
=\epsilon_\nu\gamma_\nu^4
\{T_{t_\nu}\mathcal G(t_\nu)\}''.
\tag{22}
$$

在该 base 的两侧预留空隙内，选择一个光滑紧函数 $v_\nu$，使其在全部活动包的邻域准确等于 $k'$。先截取 $k'$，再在额外空隙中加一个固定紧 bump，准确调成 $\int v_\nu=0$；这些操作不改变任何活动包上的 jets。令 $k_\nu$ 是 $v_\nu$ 的原右原函数，则 $k_\nu$ 两端均为零且 $k_\nu'=v_\nu$。

式(9)、(22)使
$$
L_{\gamma_\nu T_{t_\nu}F}(k_\nu)
-\epsilon_\nu\gamma_\nu^4T_{t_\nu}\mathcal G(t_\nu)
$$
的二导在活动包和所有间隙上均为零。两个输出在同一右 collar 的值和一导均为零，因此该仿射差整体为零。特别没有在左端另调常数。

再用(8)及非零 $\gamma_\nu$，得到所需紧逆。反过来把这些 $k_\nu$ 相加就恢复全源。不同紧延拓的差属于完整原核，不改变(7)。

此外，
$$
I_2(q_2,k_\nu)=0
\tag{23}
$$
对任意真实二次多项式 $q_2$ 成立；原 $x^2q_2''k_\nu''$ 与 $2q_2'k_\nu'$ 两项准确相消。故 $\ell_f$ 的不同 base 交叉尾也全部消失。这一步允许 $Y(F,F)$ 的非零二次左尾，不能用 whole self 的仿射尾替代它。

## 6. 十二个真实中心给同一个紧逆多项式

固定同一 $V,F,G$，并取十二个真实不同中心 $t_0,\ldots,t_{11}$。现明确假设
$$
\mathcal G(t_j)\in L_F(C_c^\infty)\qquad(0\le j\le11).
\tag{24}
$$
若它们是同一个已入像的十二包装的全部副本，(24)由第5节得到；没有先把它作为免费条件。

因为(21)次数至多十一，十二个准确函数值通过原 Vandermonde 反解其十二个函数系数。$L_F$ 的像是实线性空间，所以
$$
G_m\in L_F(C_c^\infty),\qquad0\le m\le11.
\tag{25}
$$
选定一次真正的紧逆 $k_m$，使
$$
L_Fk_m=G_m,
\qquad
\boxed{k(t)=\sum_{m=0}^{11}t^mk_m.}
\tag{26}
$$
例如，可将(24)的十二个实际紧逆按同一个逆 Vandermonde 线性组合；这不涉及无限维闭像、连续右逆或新的求解假设。它们的支撑包含在一个预先固定的共同 base 包络内。于是
$$
L_Fk(t)=\mathcal G(t)
\tag{27}
$$
是整个有限多项式身份。

对原几何窗口内的新合法 $t$，(27)确实提供一个紧逆；这是**在固定 $V,F,G$ 和(24)成立之后**得到的条件性位置延拓。若重新选择母形、最终成本、目标或几何，这十二份旧 range 收据不能移植过去。尤其新的二十目标有限根一般改变 $F,G$，新的 actual 截面也可能改变 $V$；必须对其最终数据重新支付原 range 条件。

## 7. 逆解后的准确十七次多项式

写
$$
a=F-xp+\frac{x^2r}{2},\qquad W=p-xr.
$$
由(10)，
$$
\begin{aligned}
\ell_{T_tF}(T_tk(t))
&=-\int (x+t)^2
\left(F-(x+t)p+\frac{(x+t)^2r}{2}\right)^2k(t)'''\\
&=-\int (x+t)^2\left(a-tW+\frac{t^2r}{2}\right)^2k(t)''' .
\end{aligned}
\tag{28}
$$
令
$$
(x+t)^2\left(a-tW+\frac{t^2r}{2}\right)^2
=\sum_{q=0}^{6}t^qW_q.
$$
七个完整 local 权是
$$
\begin{aligned}
W_0={}&x^2a^2,\\
W_1={}&2xa^2-2x^2aW,\\
W_2={}&a^2-4xaW+x^2(W^2+ar),\\
W_3={}&-2aW+2x(W^2+ar)-x^2Wr,\\
W_4={}&W^2+ar-2xWr+\frac{x^2r^2}{4},\\
W_5={}&-Wr+\frac{xr^2}{2},\\
W_6={}&\frac{r^2}{4}.
\end{aligned}
\tag{29}
$$
定义
$$
\ell_q(k)=-\int W_qk''',\qquad
e_n=\sum_{\substack{m+q=n\\0\le m\le11,\ 0\le q\le6}}
\ell_q(k_m).
\tag{30}
$$
则真实读出为
$$
\boxed{\mathcal E(t)=
\mathfrak p_{T_tF}\{G_e^0[V;T_tF,T_tG]\}
=\sum_{n=0}^{17}e_nt^n.}
\tag{31}
$$

这些系数与紧逆的选择无关。若 $h\in\ker L_F$，则(8)使 $T_th\in\ker L_{T_tF}$；由(6)，(28)对 $h$ 在所有允许 $t$ 为零，所以(29)的各个 $\ell_q(h)=0$。因此每个(30)都是实际像上的固定线性读出，不含未定平台或间隙选择。

对幅度 $\gamma$ 和 $G$ 翻号 $\epsilon$，真正的源乘 $\epsilon\gamma^4$，真正的逆乘 $\epsilon\gamma^2$，outer $Y(F,F)$ 再乘 $\gamma^2$。故完整读出的准确权仍为
$$
\boxed{\epsilon\gamma^4,}
\tag{32}
$$
不是五次自然权，也不是直接把逆算子从公式中删掉后猜出的齐次性。

## 8. 当前十二包装的七个准确余系数

现在使用原十二个等距中心和真实幅权：
$$
t_j=t+jh_c,\qquad
\epsilon_j=(-1)^j,\qquad
\gamma_j=\binom{11}{j}^{1/4},
\qquad h_c>0 .
\tag{33}
$$
假设其实际第二源已满足第5—6节的真 range 条件。由(19)、(23)、(31)、(32)，该完整 block 的最高第二基准准确为
$$
\boxed{
B_e(t)=\sum_{j=0}^{11}(-1)^j\binom{11}{j}
\mathcal E(t+jh_c)
=-\Delta_{h_c}^{11}\mathcal E(t).
}
\tag{34}
$$
因而
$$
\boxed{B_e(t)\in\operatorname{Pol}_{\le6}.}
\tag{35}
$$
这里没有把(35)升为零，也没有把(31)的上界改成十。

若 $\left\{\begin{smallmatrix}r\\11\end{smallmatrix}\right\}$ 表示第二类 Stirling 数，则(30)给完全明确的七个系数：
$$
\boxed{
[t^\ell]B_e(t)=
-11!\sum_{n=\ell+11}^{17}
\binom n\ell h_c^{\,n-\ell}
\left\{\begin{matrix}n-\ell\\11\end{matrix}\right\}e_n,
\qquad0\le\ell\le6 .
}
\tag{36}
$$
这是有限差分的整式展开；不是新增数值观察。特别，
$$
[t^6]B_e(t)=-\frac{17!}{6!}h_c^{11}e_{17}.
\tag{37}
$$
当前基准的零判据是(34)在实际宏中心的值为零；若要求其整个允许宏中心轮廓为零，则恰是(36)七个值全零。它们是至多七个显示系数，不宣称独立或都能出现。

不同的完整 base 类型、真实内部宽度、最后五块位置和正幅只把各自(34)相加。每一类型都先保其同一真实母形及整个内部布局。总宏中心轮廓仍至多六次，但不能把不同类型的逆解或系数互相替换。

## 9. 从起点增加八个真实宏副本

下面给一个准确的有限消去，而不假定当前七余已经为零。

在构造开始时，把每个原十二包装保为一个完整宏块，再作八个宏副本：
$$
d_k=c+kH_c,\quad
\delta_k=(-1)^k,\quad
\Gamma_k=\binom7k^{1/4},
\qquad0\le k\le7.
\tag{38}
$$
第 $k$ 个宏副本为
$$
(\Gamma_kT_{d_k}f_{\rm old},\
 \delta_k\Gamma_kT_{d_k}g_{\rm old}).
$$
$H_c$ 从起点选为足够大的有限正数，保证八个完整包络及其 collars 严格不交；原微包宽度不变。原十二内部步长也仍为实际 $h_c$，不要求与 $H_c$ 相等。全部位置、幅度、窗口和右锚先固定，再选择最终有限频率。

每个完整宏块都有原(3)，所以不同宏块间的第二周期交叉输出由(18)准确为零。假设新最终圆与同一最终成本的第二源确在原紧像内。对每种最初 base，从新实际副本中任选一组十二个不同内部中心，第5—6节给它自己的(26)。原第十一差分和新的第七差分于是同时作用于同一个完整多项式(31)：
$$
\begin{aligned}
b_e^{\rm new}
&=\sum_{k=0}^{7}\sum_{j=0}^{11}
(-1)^{k+j}\binom7k\binom{11}{j}
\mathcal E(c+kH_c+t_0+jh_c)\\
&=\Delta_{H_c}^{7}\Delta_{h_c}^{11}\mathcal E(c+t_0)
=0 .
\end{aligned}
\tag{39}
$$
两个有限差分保留各自实际步长。最后一步是 $11+7=18$，严格大于(31)的十七次上界。

式(39)使用了全部 $8\times12$ 个真实副本和四次幅权
$$
\delta_k\epsilon_j(\Gamma_k\gamma_j)^4
=(-1)^{k+j}\binom7k\binom{11}{j}.
$$
它不是对一条已算 e 数值另作 signed 线性组合。f、g、$L_f$、完整源及紧逆都按这些副本同时改变，(8)、(19)、第5节及(32)逐项支付了这个区别。

因此，在新包装的真实像域上，
$$
\boxed{\mathfrak p_f(G_e^0)=0.}
\tag{40}
$$
它覆盖任意最终 $V\in U$ 满足(1)的实际 canonical、prototype、回桥和完整组合成本，不只覆盖八个 hook 响应。

## 10. 原 incoming 与真正 P2 行

同一个实际 incoming 矩阵 $X_*=\Phi_{m_*}$ 给
$$
G_e^c=G_e^0-L_f(X_*(f,g)).
\tag{41}
$$
原十二包装已经对每个允许宏中心、任意 $X\in E_8$ 准确满足
$$
I_2\{Y(f,f),X(f,g)\}=0.
$$
第5节的跨二次尾计算在新增宏副本间继续成立，所以(38)保持该身份。由(7)、(41)，
$$
\mathfrak p_f(G_e^c)=\mathfrak p_f(G_e^0)=0.
\tag{42}
$$

真正最高有理行还乘原非零曲率：
$$
P_{2,\theta}(k_\theta^0)
=\frac{\kappa}{24}
\left\{\sin^2\theta\,\mathfrak p_f(G_d^c)
+2\sin\theta\cos\theta\,\mathfrak p_f(G_e^c)\right\}.
\tag{43}
$$
因此(42)准确支付第二幅系数。总第三常数 $\tau$ 已在(4)中；不能将(42)另乘一个错误的 $1/\tau$ 或把它与 $P_2$ 本身混名。

## 11. 原十九门与非零最高 d 的同一个新初选库

不能先冻结 R447 的旧二十目标解，再照(38)复制并宣称其十九门和 $d_f(P)$ 数值不变。正确选择顺序是把(38)从起点放入 R447 的实际复制结构。

这里需要的原证明输入没有改变：

1. 每个真实微包母仍满足同一四个 natural 约束，并沿同一个受限最大秩图册保持全部 $F^\star=(F_{\rm rat},D,E_5)$。新宏复制只输运同一母，不增加独立形状。
2. 原 q 正常方向、全部 $F^\star$ 纠正、二十组集中脉冲都仍放在共同 $A_f<0$ 的中心区间。原外部全部简单 $p/A_f$ 根、邻域和 jets 原样共同。
3. 原三矩闭合及完整第三/cubic 三矩零在每个完整 base 上成立；任意真实平移、实幅和整块 $g$ 翻号均保持这些零。
4. 二十个 principal 都是原四次齐次量。新增宏副本对它们只增加正四次幅的完整位置输运；所有非-self 余项仍按原同锚有限式放入完整 $C^2$ 基准。

更明确地，令 $P(X)\in\operatorname{Pol}_{\le10}$ 为 R447 任一 principal 位置多项式。原完整副本算子为
$$
\mathscr T_{\rm old}P(X)=\sum_\nu w_\nu P(X+d_\nu),
\qquad w_\nu>0 .
$$
新增宏复制给
$$
\boxed{
\mathscr T_{\rm new}P(X)
=\sum_{k=0}^{7}\Gamma_k^4
\,\mathscr T_{\rm old}P(X+d_k).
}
\tag{44}
$$
其在 $\operatorname{Pol}_{\le10}$ 上按次数三角，全部对角均为严格正数
$(\sum_k\Gamma_k^4)(\sum_\nu w_\nu)$，所以准确可逆。g 的符号没有改变这二十条已使用的 even principal 的四次权。

因此 R447 的 paired-jet 二十行独立性、每一真实十二交替列的正核、二十层合成的严格正幅盒都原样成立。四个 q 方程与全部 $F^\star$ 仍使用同一受限图册；没有暗中增强旧冻结纤维。所有新增有限复制的 cross 和低阶项先放入完整新基准 $b$，不逐块假定为零。

最后先在固定正幅盒中解新的二十维极限方程，再选一次足够大而有限的集中参数，由同一 $C^1$ IFT 得到
$$
\boxed{V_{19}=0,\qquad d_f(P)=\eta}
\tag{45}
$$
对任意预先指定的有限 $\eta$。取 $\eta\ne0$ 即保最高第一规范的真实非零 signed 方向。集中脉冲与全部纠正同步复制至新增宏副本；因此(39)所需“同一个完整 base”在最终有限频率解上仍准确成立。

式(44)只是完整旧 proof 的有限复制输入替换；不借它宣称新的 range 满射、九行规范满射或实际成本秩。


### 11.1 为什么旧 F★ 足够，而新基准不必逐项冻结

这里有两类不同的义务，来源分别是 R324(20)—(24)和 R447(8)、(9)、(29)—(30)，不能只凭(44)的主项可逆合并论证。

第一类是从 $\pi/2$ 十九值恢复完整角函数时必须**准确保持**的低阶身份。R324(20)的整个有序 Green 核 $\Gamma_\sigma(\mu,\nu)$ 对两个真实三矩线性；R324(21)—(23)的 $\widehat K_\sigma(u_t)$ 全部 $0,\ldots,10$ 次平移系数已经收入 $\mathcal F_{\rm rat}$。把 $t$ 换成 $t+d_k$ 只是这些同一系数的有限二项式重组，不产生新的形状观察。原三矩在宏平移下准确作三角输运，在实幅 $\Gamma_k$ 下乘 $\Gamma_k^2$。每个完整宏块仍分别满足
$$
\sum_{i\ {\rm in\ macro}}R_i\mu_i=0,\qquad
\sum_{i\ {\rm in\ macro}}T_i\mu_i=0.
$$
因此 R324(24)中不同宏块之间的三个真实 ordered wedge 逐项为零；各宏块内部的 corrected-self 角项和旧有序零式，则由原全部平移系数及原矩编码继续准确支付。允许不同宏块有不同的 $\Gamma_k^2 B_0$；只在各完整宏块内部使用原等背景恒等，未假定扩大后的全圆仍有一个共同背景常数。

第二类是新二十维方程自身的全部 local、chain、非紧 self、Green 及跨宏低阶余式。它们不需要分别恒定，也不需要逐项属于旧 $F^\star$ 的线性跨度。R447(8)、(9)、(29)给整个目标的准确分裂；在固定有限宏布局上，它仍是
$$
\mathbf T_{20}^{\rm new}(\mathbf U)
=\mathbf B_{20}^{\rm new}(\mathbf U)
+\sum_i\lambda_i\int
\mathbf P_{20}(x,U_i,U_i',U_i'')(U_i''')^2,
$$
其中所有新余式均保留在同一个连续 $C^2$ 多项式映射
$\mathbf B_{20}^{\rm new}$ 内。原同锚积分、有限乘积和固定平移是这个映射的连续运算；这里的 $C^2$ 是整个余式的既有降阶性质，不把任何未降阶三导项另藏入基准。

R447(25)—(26)使最终脉冲及正常纠正满足
$U_{i,N,z}\to u_0$、$\partial_zU_{i,N,z}\to0$ 于 $C^2$，
在已固定有限幅盒上一致。故完整多项式链式法则直接给
$$
\mathbf B_{20}^{\rm new}(\mathbf U_{N,z})
=\mathbf b_{\rm new}+o_{C^1}(1).
$$
$\mathbf b_{\rm new}$ 包含全部新增宏间基准，通常不同于旧基准；既不置零，也不以保持旧 $F^\star$ 为由宣称它不变。式(44)只支付新主列的满像和正核，随后同一个二十维方程用它支付任意这个有限 $\mathbf b_{\rm new}$。因此本稿没有为冻结所有新增基准暗增低阶观测，也没有从 principal 可逆跳到全式零。

## 12. Whole J+ 与新增真实 range 门的选择顺序

新增宏副本仅对已有母作固定平移和非零实幅变换。R414/R429 采用的共同自然查询空间已经包含这些母的完整正仿射 orbit；幅度只乘相应真实齐次常数。universal ordered 查询和 whole $E$ 本身也不因增加查询副本改变定义。因此，从起点使用(38)、(45)的新有限母库后，可以按 R433 的同一个实际有限截面付
$$
J^+(V)=0
\tag{46}
$$
并保持其原几何安装范围。这里消费的是该新库的真实共同截面，不把多个单母截面拼起来，也不移植另一旧几何的 incoming 数据。

但(46)仍不等于 period range。所有新活动包的实际内部 partial、禁止 Laurent 项、原平台连接和端点条件仍须检验。两种合法使用方式是：

- 对固定不变的 $V,F,G$，若已经有一组真实十二位置的(24)，第6节确实给出同一窗口内的多项式紧逆，从而可延拓到新的合法宏位置；
- 若按第11节重新完成二十根或按(46)重新选择 actual 成本，则对这一最终数据重新证明所需(24)或整个新包装的真 range。旧解的十二个点不再是它的收据。

本稿不把第一种条件结论用于第二种未验证的数据。全部物理窗口、支撑间隙、原几何合法余量和共同右锚必须在各自构造开始时确定。

## 13. 与 R447 d 方向、同一个规范及实际基准合并

在新库(45)上，R444 的原响应 $\mathcal B_P\mathfrak H$ 仍属于
$$
\mathcal R\cap\ker J^+,
$$
并且是原紧 $L_f$ 像方向，保持全部已存在的 period range、内部通量、ordered $C$ 及三个合法性矩。它对两个真实像泛函的变化是
$$
(\delta b_d,\delta b_e)=
\left(-\frac{s\eta}{\tau},\,0\right).
\tag{47}
$$
所以一旦最终成本的两个真实 period 特解存在，(42)给 $b_e=0$，而 $\eta\ne0$ 使最高 $d$ 行在这一 signed 支路内可准确修正。真正 $P_2$ 的变化仍为(47)乘 $\kappa/24$。

这里仍使用
$$
k_\theta^0=\sin^2\theta\,k_d+2\sin\theta\cos\theta\,k_e
$$
及同一个二阶规范，没有为两个相位槽分别换几何或重锚。后续齐次核只用于原其余行；其 $P_2$ 行仍由 R437 全零。

实际实现也必须保完整账目。响应列(47)不是一个实际 word 的全部成本。prototype 的自成本、原 M0 桥、整数复制及回桥的完整基准均仍进入同一个最终 $V$。本稿(40)—(42)的优点是：**只要这个完整最终 V 满足(1)和真实 range，它的全部最高 e 基准也被同一包装消掉**，不需要逐 prototype 假定 e 自成本为零。它没有因此给出最高 d 与其它门的 actual 增强截面。

## 14. 完成范围与剩余问题

对当前十二包装，本稿准确证明了(21)、第5节的真逆拆分、(31)及七余式(36)。这些结论并未证明当前冻结圆的 $b_e$ 已零。

对从起点扩充的同母八/十二包装，本稿给出了真实(39)—(42)，并将其与同一个新二十目标根(45)、原 whole $J^+$ 截面及合法性矩接在一起。它使最高第二规范成为完整 period 存在之后的自动条件，覆盖完整 actual 基准；最高第一规范保留 R447 的非零原响应方向。

仍未支付：新最终圆的全部 period range、其余九个端口行、最高 d 与这些门的同一个实际原型截面，以及其它几何段的完整 ruling。更未支付后续阶、收敛、闭嵌入或主课题完成。完整逆算子与原尾保真后的有限差分，不能替代这些剩余条件。
