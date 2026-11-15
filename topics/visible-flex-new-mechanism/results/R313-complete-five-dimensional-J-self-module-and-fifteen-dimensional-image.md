# R313：完整 𝔍 核的五维零矩 self 模块与全 self 像的十五维下界

日期：2026-11-15。**完整纸面证明；没有执行新的符号程序、profile 求积、秩计算、采样或人工测试。**

[R310](R310-full-self-direction-invisible-to-all-translates-of-even-profiles.md) 给出一个完整 self 新方向：所有 even 母包的任意平移都看不见它，但某个真实紧支撑的非对称母包能检测到它。本稿不继续逐个列孤立方向，而是完整计算同一真实第三核 $\mathfrak J$ 与五个 E8 方向的整个 self 子块。

得到五条完整 quartic 函数公式，全部属于 $\mathcal R_{\mathrm p0}\cap\ker\mathbf T$。其平移作用为一条长度四的幂零链与一条常链；常链中存在对每个非零实紧 profile 都严格正的完整 self。与 R303 长度十的旧链比较，两个 self 像准确交零，因而
$$
\boxed{\dim\mathcal Q_{\rm all}
(\mathcal R_{\mathrm p0}\cap\ker\mathbf T)\ge15.}
$$
这里的十五是完整 profile 函数像的严格下界，不是整个像的已定维数，也不把 principal 满秩替代完整成本。

来源：[R255](R255-explicit-third-diagonal-kernel-and-complete-hook-response-formula.md)、[R258](R258-self-adjoint-hook-green-operator-and-complete-period-interface.md)、[R261](R261-eight-local-self-adjoint-hook-operators-and-full-third-kernel.md)、[R297](R297-ordered-platform-matrix-surjective-pure-zero-responses-and-real-control.md)、[R298](R298-zero-platform-matrix-with-nonzero-self-response-and-ten-observation-control.md)、[R303](R303-complete-self-degree-nine-and-all-translation-control.md)、[R310](R310-full-self-direction-invisible-to-all-translates-of-even-profiles.md)。

## 1. 完整核、右积分与 self 查询

保原正右积分
$$
(Ja)(x)=\int_x^{r_*}a(\xi)\,d\xi,\qquad DJ=-1.
$$
所有输入在同一个合法开区间内紧支撑，右 collar 为零；不把算子的左尾设为零。

$\mathfrak J$ 是 R255 的真实三维链根，满足
$$
\Delta\mathfrak J=0,\qquad N\mathfrak J=0,\qquad
\delta^3\mathfrak J=0.
\tag{1}
$$
本稿只用第一、二式及 R258 已付的完整局部算子，不重新评价这条原核。

对 E8 的任一真实单位组合 E，令
$$
K_E=\mathcal B_E(\mathfrak J).
\tag{2}
$$
$\mathcal B$ 是原完整第四响应，全部外槽、内槽与第三 history 均保留。由 $\Delta\mathfrak J=0$，
$$
K_E\in\mathcal R_{\mathrm p0}.
\tag{3}
$$

完整 self 定义为
$$
\mathfrak q_u(V)=\frac14[x^2]_{\rm left}V(u^2,0),\qquad
\mathcal Q_{\rm all}(V):u\longmapsto\mathfrak q_u(V).
\tag{4}
$$
它是成本 V 的线性查询，但对 profile u 为四次函数。以下全部等号是 (4) 的完整值。

记
$$
v=u',\qquad r=u'',\qquad s=u'''.
$$
R258 的准确零阶系数为
$$
c_{\mathfrak J,u}
=8s^2+12r\,u^{(4)}+4v\,u^{(5)}
=4D^3(vr)-2D^2(r^2).
\tag{5}
$$
R297/R298 的完整 self 身份给
$$
\mathfrak q_u(K_E)=-\frac14\int c_{\mathfrak J,u}\Phi_E(u,u).
\tag{6}
$$

## 2. 对全部 E8 成立的一个完整积分入口

因为 $vr,r^2$ 及所需端 jets 都真正紧支撑，(5)–(6) 可在保留 $\Phi_E$ 的全部左尾时分部积分：
$$
\mathfrak q_u(K_E)
=\int vr\,D^3\Phi_E(u,u)
+\frac12\int r^2D^2\Phi_E(u,u).
$$
再对第一项分部积分一次，得到
$$
\boxed{
\mathfrak q_u(K_E)
=-\int\left(vs+\frac12r^2\right)
D^2\Phi_E(u,u).
}
\tag{7}
$$

(7) 对全部八维 E8 都成立。它没有把一般 $\Phi_E''$ 中仍可能存在的 primitive 删除；本稿选择的五个方向恰可完整化为局部表达。其余三个方向是否含真正的矩尾、是否可用其他响应校正，应另按原式处理。

式 (7) 是完整 self 的入口，不是将最高 $s^2$ 项作为定义。以下每条 $C^2$ 项也显式保留。

## 3. 五个原 E8 方向与真实左尾

采用原八矩算子中的
$$
\begin{aligned}
P(u,u)&=J(r^2),\\
R(u,u)&=v^2+xJ(r^2),\\
S(u,u)&=J(xr^2),\\
U(u,u)&=xv^2+xJ(xr^2)+\frac12J_2^*,\\
T(u,u)&=x^2v^2+xJ_2^*,
\end{aligned}
\qquad
J_2^*=J(x^2r^2+2v^2).
\tag{8}
$$
它们分别是 $r_0,r_1,s_0,s_1,t_1$ 方向，恰为 E8 中 $p_0=p_1=p_2=0$ 的五维子空间。此处 T 是一个二次 profile 算子，九矩记作粗体 $\mathbf T$，不混淆。

若 w 是在 u 整个右方的真实紧包，记其三个原矩为 $\mu_0,\mu_1,\mu_2$。在 u 的支撑上，(8) 的真实左尾依次为
$$
\mu_0,\qquad x\mu_0,\qquad\mu_1,\qquad
x\mu_1+\frac12\mu_2,\qquad x\mu_2.
\tag{9}
$$
它们均为仿射函数，但一般非零。

由 (5)，
$$
\int c_{\mathfrak J,u}=0,\qquad
\int x\,c_{\mathfrak J,u}=0.
\tag{10}
$$
R297 的完整有序查询为
$$
\mathfrak t_{u,w}(K_E)
=-\frac14\int c_{\mathfrak J,u}\Phi_E(w,w).
$$
结合 (9)–(10) 对全部真实分离包成立，故
$$
\boxed{\mathbf T(K_P)=\mathbf T(K_R)=\mathbf T(K_S)
=\mathbf T(K_U)=\mathbf T(K_T)=0.}
\tag{11}
$$

这不是仅对某个总三矩零的圆成立。相反，一般 E8 的二次左尾会看到
$$
\int x^2c_{\mathfrak J,u}=-4\mu_0(u),
$$
故不能将 (11) 扩大成该根对全部八个 E 都九矩零。

## 4. 五条完整 self 公式

定义下面的真实 profile 积分：
$$
\begin{aligned}
A_j(u)&=\int x^jv^2s^2,&
J_j(u)&=\int x^jvrs^2,\\
C_j(u)&=\int x^jr^4,&
D_j(u)&=\int x^jvr^3,\qquad
E_0(u)=\int v^2r^2.
\end{aligned}
\tag{12}
$$
下标 j 只是显式位置幂，不是平移后的拟合系数。

完整结果为
$$
\boxed{
\begin{aligned}
\mathfrak q_u(K_P)&=2J_0,\\
\mathfrak q_u(K_R)&=-2A_0+2J_1+\frac1{12}C_0,\\
\mathfrak q_u(K_S)&=2J_1-\frac1{12}C_0,\\
\mathfrak q_u(K_U)&=-2A_1+3J_2+\frac23D_0-\frac1{12}C_1,\\
\mathfrak q_u(K_T)&=-2A_2+2J_3-3E_0+\frac43D_1-\frac1{12}C_2.
\end{aligned}}
\tag{13}
$$
式 (13) 中 $J_j$ 始终是 (12) 的完整积分；(8) 的原函数以 $J_2^*$ 区分。

### 4.1 完整二阶导数

从 (8) 的原同锚表达逐项求导，得到
$$
\begin{aligned}
P''&=-2rs,\\
R''&=2(v-xr)s,\\
S''&=-r^2-2xrs,\\
U''&=2vr-2xr^2+(2xv-3x^2r)s,\\
T''&=-2(v-xr)^2+(2x^2v-2x^3r)s.
\end{aligned}
\tag{14}
$$
这里使用 $(J_2^*)'=-(x^2r^2+2v^2)$，没有将该导数误作仅 $-x^2r^2$。所有 primitive 在 (14) 中因真实求导准确消去，不是预先置零。

### 4.2 全部低阶余项的准确化简

把 (14) 代入 (7)。所需的有限分部积分身份是
$$
\begin{aligned}
\int r^3s&=0,&
\int vr^2s&=-C_0/3,&
\int xr^3s&=-C_0/4,\\
\int v^2rs&=-D_0,&
\int xvr^2s&=-D_0/3-C_1/3,&
\int x^2r^3s&=-C_1/2,\\
\int v^3s&=-3E_0,&
\int xv^2rs&=-E_0/2-D_1,&
\int x^2vr^2s&=-2D_1/3-C_2/3,\\
\int x^3r^3s&=-3C_2/4.
\end{aligned}
\tag{15}
$$
每式只用真实紧端的全导数。例如
$3vr^2s=v(r^3)'$ 和 $4x^jr^3s=x^j(r^4)'$。
代回即得 (13)。特别，U、T 两式中的 $D_j,E_0,C_j$ 都是完整值的一部分，没有因它们是 $C^2$ 观测而省略。

## 5. 一个对所有非零实紧母包严格正的方向

取
$$
K_+=K_S-K_R.
\tag{16}
$$
由 (11)、(13)，
$$
\pi K_+=0,\qquad\mathbf T(K_+)=0,\qquad
\boxed{\mathfrak q_u(K_+)=F(u):=2A_0(u)-C_0(u)/6.}
\tag{17}
$$
对任意非零实紧 u，$C_0>0$。由 (15) 与 Cauchy–Schwarz，
$$
C_0=-3\int vr^2s
\le3\sqrt{A_0C_0},
\qquad C_0\le9A_0.
$$
因此
$$
\boxed{F(u)\ge C_0(u)/18>0.}
\tag{18}
$$
这是完整 self 的严格号，不是只对其 principal 部分判号，也没有要求 u 满足三矩零。

(18) 仅是这个真实响应方向的 self 查询性质。它不授该响应自身为任意符号实际成本，也不声称对 U 或整个第四 ruling 有一个新的正字符；R297/R298 的实际实现仍须保全部基准。

另一方面，$J_0=\int vrs^2$ 不恒零。R310 用真实紧 cutoff 与 Euler 变分已给严格存在证明：其 Euler 表达式的最高项为 $-2u'u''u^{(6)}$，可在一个紧函数中心取值 $-2$，再用一个紧变分得到 $J_0\ne0$。本稿复用该证明，不寻找新数值 profile。

## 6. 平移作用的完整五维结构

N 是原仿射平移导子，保同一右锚与全部槽。在 self 函数像上，它诱导
$$
(\mathcal N q)(u)
=\left.\frac{d}{dc}\right|_{c=0}q(u(\,\cdot-c)).
\tag{19}
$$
原因是输出导数不贡献左二次尾的 $x^2$ 系数，而全部输入槽的导数给真实平移变分。这里的局部平移只需在一个允许开窗口内；不移动 profile 到物理区间外。

R255 给 $N\mathfrak J=0$，E8 原表给
$$
NP=0,\quad NR=NS=P,\quad
NU=R+2S,\quad NT=2U.
$$
因此完整响应本身满足
$$
NK_P=0,\quad NK_R=NK_S=K_P,\quad
NK_U=K_R+2K_S,\quad NK_T=2K_U.
\tag{20}
$$

定义
$$
X_0=K_P,\quad
X_1=(K_R+2K_S)/3,\quad
X_2=K_U/3,\quad X_3=K_T/6.
\tag{21}
$$
则
$$
NX_0=0,\qquad NX_j=X_{j-1}\ (1\le j\le3),\qquad NK_+=0.
\tag{22}
$$
这是一条长度四的有限幂零链和一条常链。

令
$$
\mathcal V_{\mathfrak J}
=\operatorname{span}\{\mathcal Q_{\rm all}(X_0),\ldots,
\mathcal Q_{\rm all}(X_3),\mathcal Q_{\rm all}(K_+)\}.
$$
因为 $\mathcal Q_{\rm all}(X_0)=2J_0\ne0$，对链上线性关系反复施 $\mathcal N$，从最高项向下即得四项独立。若 $\mathcal Q_{\rm all}(K_+)$ 在该四链中，同样施幂零导子会迫它为 $2J_0$ 的倍数。

但 $J_0$ 对反射为奇，而 F 对反射为偶且对每个非零 even 紧 u 严格正；所以不可能。于是
$$
\boxed{\dim\mathcal V_{\mathfrak J}=5,\qquad
\ker(\mathcal N|_{\mathcal V_{\mathfrak J}})
=\operatorname{span}\{J_0,F\}.}
\tag{23}
$$
五条完整成本也因此独立：成本零关系必给 self 零关系。这里只付这个五维子块，不把它冒作 $E8\otimes\mathfrak J_3$ 的全部 self 像。

## 7. 与旧十链交零：完整有限幂零论证

令
$$
\mathcal V_{\mathfrak H}
=\operatorname{span}\{\mathcal Q_{\rm all}(G_0),\ldots,
\mathcal Q_{\rm all}(G_9)\}
$$
为 R303 的旧十链 self 像。R303 的完整原式给
$$
\mathcal N\mathcal Q_{\rm all}(G_0)=0,\qquad
\mathcal N\mathcal Q_{\rm all}(G_j)=
\mathcal Q_{\rm all}(G_{j-1})\quad(j\ge1),
$$
$$
\mathcal Q_{\rm all}(G_0)=I_0,\qquad
I_0(u)=\int r^2s^2.
\tag{24}
$$
$I_0$ 对每个非零实紧 u 严格正。故这确是长度十的 cyclic 幂零模块，
$$
\dim\mathcal V_{\mathfrak H}=10,\qquad
\ker(\mathcal N|_{\mathcal V_{\mathfrak H}})=\mathbb RI_0.
\tag{25}
$$
(24) 对 self 像成立；不将那个可能 self 为零的下一条原成本擅自宣布为零。

现在两空间均有限维、$\mathcal N$ 不变，且 $\mathcal N$ 在其和上幂零。若交空间非零，选其中非零元素并施加最后一个非零幂次，便得到交空间中一个非零 $\mathcal N$ 核元素。因此由 (23)、(25)，非零交将迫
$$
I_0\in\operatorname{span}\{J_0,F\}.
\tag{26}
$$

下面在真实允许的 profiles 上排除 (26)。反射保持 $I_0,F$，使 $J_0$ 变号；R310 已证 $J_0$ 不恒零，因此任何 (26) 的 $J_0$ 系数必须零。若还剩 $I_0=\beta F$，固定一个非零 even 紧母函数并作真实正宽度变化
$$
u_a(x)=u((x-x_0)/a).
$$
只需选两个足够靠近的不同正 a，使全部支撑仍落在一个预留内部包络，不使用无限缩放或外移。直接变量代换给
$$
I_0(u_a)=a^{-9}I_0(u),\qquad F(u_a)=a^{-7}F(u).
\tag{27}
$$
两者均正，不可能对两个不同 a 由同一个 $\beta$ 相等。故 (26) 不成立，得到
$$
\boxed{\mathcal V_{\mathfrak H}\cap\mathcal V_{\mathfrak J}=0.}
\tag{28}
$$

于是这两个完整 self 子块共同给
$$
\boxed{
\dim\mathcal Q_{\rm all}
(\mathcal R_{\mathrm p0}\cap\ker\mathbf T)\ge10+5=15.
}
\tag{29}
$$
所用每个方向都是真实完整响应；(29) 不只是 formal domain 的维数，也没有以一条母函数上的次数拟合充当全函数独立性。

## 8. 一个实际有限控制后果与其准确范围

十五个完整 self 函数独立，故可选十五个真实紧 profile $u_1,\ldots,u_{15}$，使相应评价矩阵可逆。理由是：若全部允许 profile 的评价泛函没有张成十五维对偶，就有一个非零 self 函数在每个允许 profile 上都为零，和上述独立性矛盾。可逐个选取，全部在同一个预留内部包络；这是存在证明，不是未执行的采样秩报告。

这些十五方向都在九矩核内。再加入 R297 已付的九个矩阵响应，整体矩阵为分块三角：先用九列支付 $\mathbf T$，再用十五列支付 self 查询。九列对 self 的基准值不需要另为零，必须由后十五列准确校正。因此
$$
V\longmapsto
\bigl(\mathbf T(V),\mathfrak q_{u_1}(V),\ldots,\mathfrak q_{u_{15}}(V)\bigr)
$$
在 $\mathcal R_{\mathrm p0}$ 上满射到 $\mathbb R^{24}$。

R222/R297 的保基准有限响应控制可据此真实同时指定 whole pure、这九矩和十五个指定完整 self 值。其有限复制、共同端口、真实倒行、pure 校正的全部 mixed 成本及闭 hook 包装仍按原完整证明保留。

本节不是说十五个 profiles 已经忠实读取整个 $\mathcal Q_{\rm all}(U)$，也不是说所有不同母包的 self 都能同时任意指定。它只对已经证明独立的完整十五维子块给一个明确可实现的有限观测后果。若后续 profile 依赖新的 shape 参数，必须重新证明同一控制矩阵在该族上保持所需秩；不能把固定母/固定有限查询的结论自动授给整个自适应构造。

## 9. 与 R310 和后续全 Q 的关系

R261 的原系数直接给
$$
c_{\chi_{34}-3\chi_{32},u}=c_{\mathfrak J,u}/128.
$$
所以对全部 E8，其完整 self 满足
$$
\mathfrak q_u\bigl(\mathcal B_E(\chi_{34}-3\chi_{32})\bigr)
=\mathfrak q_u(K_E)/128.
\tag{30}
$$
特别，R310 的 $K_J=64\mathcal B_P(\chi_{34}-3\chi_{32})$ 与本稿 $K_P/2$ 有相同完整 self，也有相同的零九矩。

(30) **不声称两个完整成本相等**。它只来自控制 self 的相同 c 系数；原局部 a、d 系数确可不同，其他 period/ruling 查询仍会区分它们。这正是保完整观测范围的必要区分。

本稿已将这条新的母形信息放入一个完整、闭合于 N 的五维原函数子块。接下来要决定整个 Q，仍须比较 canonical self 的完整原函数像与全部可用响应，包括真正的 $C^2$ 与累计矩尾；不能只靠 (29) 的维数下界或最高 jet 满秩。

同时，本稿不会撤销任何另已证明的特定圆类的 joint 障碍。若不交 rank-one 微包圆被完整 ruling 关系排除，这些实际成本控制结论仍成立，但不因此使该圆类恢复可解。新的 profile 构造须支付同一几何、同一二阶 gauge 的全部原条件。

作者责任：全部新式来自已发表原局部系数、五条原 E8 表达和本文显示的有限手写分部积分。没有重新生成原 forcing、W 模板、χ 差、full responses 或任何已付科学目标。
