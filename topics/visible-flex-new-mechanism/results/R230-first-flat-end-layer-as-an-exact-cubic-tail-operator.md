# R230：平端一次层的真实三次尾算子及有限有理消元门

日期：2026-11-15。**完整纸面证明；未执行新的原式研究、profile 求积或函数核计算。**

来源为 [R56](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md) 的同右锚原式、[R105](R105-finite-canonical-fourth-cost-space-and-response-quotient.md) 的完整 canonical 空间、[R178](R178-fixed-color-priority-IBP-and-terminating-shared-word-map.md) 与 [R179](R179-universal-independence-of-fixed-color-remainder-words.md) 的固定颜色余字母表示、[R201](R201-weight-zero-pure-image-and-failure-of-positive-character-readout.md) 的已付 pure 零代表、[R225](R225-complete-period-range-flat-end-germs-and-finite-observation-quotient.md) 的完整 period 像，以及 [R226](R226-exact-flat-end-layers-and-remainder-germs-of-the-response-chain.md) 的准确平端渐近。

本稿把 R226 尚未评价的一次层收成可以从既有原 DAG 单独提取的有限对象。没有把真实 Volterra 尾值当成独立参数。随后给出有限有理运算判据：指定真正的解析平端 profile 后，该一次层若非零，就必有 R226 所需的非零有限首渐近项；不会遗漏“非零但所有渐近系数均为零”的这一层。

当前尚未指定 R225 存在性构造中的正多项式，也没有计算相应圆的三次尾值。因此后继先比较 **universal 三次尾函数值算子**，不冒称某个冻结圆的 period 已被判定。

## 1. 固定端口、真实尾值与记号

取首个 $f$ 上升活动区间左端 $a$，在其左边保 $f=g=0$ 的开放间隙。令 $t=x-a$，在 $0<t<\delta$ 有

$$
g=0,\quad f(a)=0,\quad
p(t)=f'(a+t)=\epsilon_0 e^{-c/t}A(t),\qquad
c>0,\quad A\in C^\infty([0,\delta)),\quad A(0)>0,
\tag{1}
$$

其中 $\epsilon_0\ne0$ 是固定实幅度。$f$ 的全部 jets 在 $a$ 全平。所有右积分保持原右端 $r$：

$$Jv(x)=\int_x^r v(s)\,ds.\tag{2}$$

对余字母 word $w=(\ell_1,\ldots,\ell_m)$，记

$$
I_w(x)=\int_{x<s_1<\cdots<s_m<r}
\ell_1(s_1)\cdots\ell_m(s_m)\,ds_1\cdots ds_m,\qquad I_\varnothing=1.
\tag{3}
$$

本文 (3) 使用正尾。旧计算环的 atom 与 R178 存储代表使用 $\mathcal I=\int_r^x=-J$；将其长度 $m$ 的 word 改写成 (3) 时，系数准确乘 $(-1)^m$。原 SHA 和原节点方向不改变。

故 $I_w'=-\ell_1I_{w'}$，$w'=(\ell_2,\ldots,\ell_m)$。定义

$$\tau_w=I_w(a).\tag{4}$$

式 (4) 是同一真实输入在同一右锚的原函数值。各 $\tau_w$ 服从全部 shuffle、分部积分和实共轭关系；不赋予它们互相独立的数值。

canonical 复颜色为 $q=f+ig,\bar q=f-ig$。局部区间中 $q=\bar q=f$，但右侧仍保完整 $f,g$，所以 $\tau_w$ 中两种颜色不能合并。只有 word 的**局部因子**可以代入 $q=\bar q=f$。记

$$\mathscr A=\bigcup_{N\ge0}t^{-N}C^\infty([0,\delta)).\tag{5}$$

它允许有限极点；不把其中每个函数称为可平滑延至端点。

## 2. 有限局部次数展开是准确身份

由 R226 的准确指数积分引理，对每个固定 $j\ge0$，

$$p^{(j)}\in p\mathscr A,\qquad f\in p\mathscr A.\tag{6}$$

对正整数 $d,d_1,d_2$，

$$
D(p^d\mathscr A)\subset p^d\mathscr A,\qquad
(p^{d_1}\mathscr A)(p^{d_2}\mathscr A)\subset p^{d_1+d_2}\mathscr A,
\tag{7}
$$

$$
\int_0^t p(s)^d\mathscr A(s)\,ds\subset p(t)^d\mathscr A(t).
\tag{8}
$$

式 (8) 逐个有限和理解：若被积项为 $p^dt^\nu v(t)$，R226 给 $p^dt^{\nu+2}$ 乘一个真正的 $C^\infty$ 因子。这不是只比较首阶数量级。有限次微分、乘法、左 Volterra 积分保持 $p^2\mathscr A$，所以后文余项求两次导数后仍是 $p^2\mathscr A$。

由真实初值 (4)，

$$
I_{\ell_1,\ldots,\ell_m}(a+t)
=\tau_{\ell_1,\ldots,\ell_m}
-\int_0^t\ell_1(a+s)I_{\ell_2,\ldots,\ell_m}(a+s)\,ds.
\tag{9}
$$

重复最多 $m$ 次即结束，不是无穷级数。一个局部 $d$ 次字母属于 $p^d\mathscr A$，故局部次数至少二的项准确进入 $p^2\mathscr A$。嵌套右原函数的第一项始终是其真实 $\tau_w$，不是零；其首个局部变化可能仅一次，而余 word 携带真实三次尾。

## 3. 一次层的明确公式

取四次输出原式 $G$，用 R178 的 sound 表示写为

$$
G(x)=\sum_\alpha c_\alpha x^{m_\alpha}
\prod_{\nu\in J_\alpha}q_{\kappa_\nu}^{(j_\nu)}(x)I_{w_\alpha}(x),
\qquad c_\alpha\in\mathbb Q,\quad d_\alpha=|J_\alpha|.
\tag{10}
$$

颜色 $\kappa_\nu$ 是 $q$ 或 $\bar q$；复线性组合逐实部、虚部处理。所有存活字母均满足 R178/R179 余语法，总 profile 次数四。

一个 profile 次数恰为一的余字母只能是

$$x^nq\quad\hbox{或}\quad x^n\bar q,\qquad n\ge0.\tag{11}$$

只有一个颜色 jet 时，若其阶正，就不满足最高优先颜色的最高 jet 为零或重复出现的余字母条件。

定义线性局部算子

$$
\begin{aligned}
T_\tau f(x)
={}&\sum_{\alpha:d_\alpha=1}
c_\alpha x^{m_\alpha}f^{(j_\alpha)}(x)\tau_{w_\alpha}\\
&-\sum_{\substack{\alpha:d_\alpha=0\\
\ell_{\alpha,1}=x^{n_\alpha}q\ {\rm or}\ x^{n_\alpha}\bar q}}
c_\alpha x^{m_\alpha}\tau_{w_\alpha'}
\int_a^x s^{n_\alpha}f(s)\,ds .
\end{aligned}
\tag{12}
$$

两行中每个 $\tau$ 都是三次真实尾函数。空 word 不产生虚构三次常数。

**定理 1。** 有准确 germ 分解

$$
\boxed{G(x)=P_{\tau,0}(x)+T_\tau f(x)+p(t)^2R(t),\qquad R\in\mathscr A,}
\tag{13}
$$

其中

$$P_{\tau,0}(x)=\sum_{\alpha:d_\alpha=0}c_\alpha x^{m_\alpha}\tau_{w_\alpha}.\tag{14}$$

若 $G$ 是 canonical period 根，(14) 是截去左方输入后的真实左 collar 尾，次数至多二。截断只在此前共同零间隙中进行，不改当前查询及右侧输入；R56 的右因果性支付这一步。式 (14) 的系数是同一组真实四次尾函数。完整 canonical 左尾身份给其二次界，不凭单个尚未组合 DAG 项臆断。

**证明。** $d_\alpha\ge2$ 的项由 (6)–(8) 进入余项。$d_\alpha=1$ 时，(9) 的初值给第一行 (12)，每次再积分至少增加一个局部 profile 因子。$d_\alpha=0$ 时，初值给 (14)，只有首字母次数一才能贡献一次变化，由 (11) 得第二行 (12)。其余项至少二次。全部展开有限且准确。$\square$

二次尾不能直接删除；比较 R225 的端点 germ 时采用同一修正

$$\widetilde G(x)=G(x)-\tfrac12G''(a)(x-a)^2.\tag{15}$$

其余两项端全平，常数及一次尾对第二导数无贡献，所以

$$\boxed{\widetilde G''=(T_\tau f)''+p^2\mathscr A.}\tag{16}$$

## 4. 尾函数值与原式代表的准确边界

式 (12) 系数是三次尾函数的有限有理线性组合。raw DAG 若先产生若干初值的乘积，总次数仍为三；按真实 shuffle 身份化成三次 word，再作 R178 同锚分部积分。在 $a$ 处仅将**外部** profile jets 置零，不能把积分内部 jets 置零。

这只处理三次系数，不要求重求四次根的完整 pure/balanced 规范式或头部函数核。

R179 独立性在这里的含义是：允许变化端点 $a$，并在其右侧紧子区间取任意光滑输入时，规范三次尾 words 的函数值关系由同一余表示忠实决定。query 坐标 $x$、端点 $a$、右侧 profile 是 universal 表的实际变量。局部微分算子由查询点 jets 分离；剩余多项式 Volterra 核由严格位于左端与查询点之间的局部 test 分离。

这不意味着固定圆的 $\tau_w$ 数值独立。固定圆后必须同时代入它的真实尾值。一个有限 word 对偶行也先只是 universal 系数读出，不是固定圆已有的合法 period 观测。

若两份同锚原式定义同一函数，则 (12) 作为真实尾函数值的线性局部算子相同。可固定右侧任意尾输入，在更左小活动区间置 $\eta f_{\rm loc}$，对真实原式身份按实幅度 $\eta$ 极化，并同时保留真实左二次尾的变化。差的一次局部部分端全平，不能与非零二次多项式抵消；任意局部 test 和任意右侧紧支撑输入分离该表。因此保初值没有增加虚构自由度。

## 5. 指定解析平端后的一次层有限有理终止门

现在额外**指定** R225 类中的一个真实解析 profile：

$$
p(t)=\epsilon_0e^{-c/t-c_1/(\delta_1-t)}P(t),\qquad c,\delta_1>0,
\tag{17}
$$

其中 $P$ 是已给定的正多项式，当前区间远离 $\delta_1$。关键性质是

$$\lambda=p'/p\in\mathbb R(t),\qquad\lambda=ct^{-2}+O(1).\tag{18}$$

这一节没有替尚未指定的 $P$ 生成数值。设

$$I_j(t)=\int_0^ts^jp(s)\,ds,\qquad R_j=I_j/p.\tag{19}$$

$f=I_0$，且

$$
\int_0^ts^nf(s)\,ds
=\frac{t^{n+1}I_0(t)-I_{n+1}(t)}{n+1}.
\tag{20}
$$

对 $j\ge1$，$f^{(j)}=p^{(j-1)}$ 是 $p$ 乘有理函数。平移 $x=a+t$ 后，

$$
S(t):=\frac{T_\tau f(a+t)}{p(t)}
=A_0(t)+\sum_{j=0}^Jb_j(t)R_j(t),
\quad A_0\in\mathbb R(t),\quad b_j\in\mathbb R[t].
\tag{21}
$$

系数包含已经固定的真实三次尾值；也可保其尾函数值线性系数。R226 给 $R_j\in t^{j+2}C^\infty$ 的真正延拓。置

$$\mathcal L=D_t+\lambda=p^{-1}D_tp.\tag{22}$$

则

$$\mathcal LR_j=t^j,\qquad\mathcal L(bR_j)=b'R_j+b\,t^j.\tag{23}$$

取整数 $n>\max_j\deg b_j$，空和时取 $n=1$，有限次 (23) 给

$$Q_n=\mathcal L^nS\in\mathbb R(t).\tag{24}$$

**定理 2。**

$$\boxed{T_\tau f\equiv0\quad\Longleftrightarrow\quad Q_n\equiv0.}\tag{25}$$

若 $T_\tau f\ne0$，则 $S\in\mathscr A$ 有非零有限首渐近系数。准确地，取 $N$ 使 $t^NS$ 光滑；若这个光滑因子的全部 Taylor 系数为零，则 $S\equiv0$。不对尚有极点的 $S$ 直接谈端点全部 jets。

**证明。** $\mathcal L^nS=p^{-1}D_t^n(pS)$。$Q_n=0$ 时，$pS=T_\tau f$ 是次数小于 $n$ 的多项式；而 (12) 全部局部导数及左积分端全平，故该多项式为零。反向显然。

若 $t^NS$ 全平，则 $S$ 也全平；有限次微分及乘有理函数仍全平。因此有理函数 $Q_n$ 全平，只能恒零，再用 (25)。$\square$

不需要假设 $R_j$ 的 Taylor 级数收敛，也不以未指定阶数的有限 jet 取样判断原式零；终止对象是准确有理函数 (24)。

## 6. 一次层非零给完整 period 的端点失败

若 $T_\tau f\ne0$，则 $(T_\tau f)''\ne0$，否则端全平仿射函数只能为零。又

$$\frac{(T_\tau f)''}{p}=\mathcal L^2S\tag{26}$$

仍为 (21) 同类表示。定理 2 给某个整数 $\nu$ 使

$$
(T_\tau f)''=pt^\nu v(t),\qquad v\in C^\infty,\quad v(0)\ne0.
\tag{27}
$$

由 (16) 和 R226，在左端零通量支路中，准确 gauge 导数为

$$
u=-p^{-1}t^{\nu+8}U(t)+Cp+\text{有限极点项},\qquad
U(0)=\frac{v(0)}{16c^4}\ne0.
\tag{28}
$$

它不能平滑延至端点，故 $\widehat\Gamma_a(G)\ne0$，完整 $G\in\operatorname{im}L_f$ 失败。

此推论要求指定合法解析圆、它的真实 $\tau$、原 $G$ 和同一右锚都已给定。仅证明 universal $T\ne0$ 不等于已核这些输入。

$T_\tau f=0$ 只推进到 $p^2\mathscr A$ 层；该层的有限极点门，以及其他平台、通量、内部退化点、另一端 germ 和右锚两常数仍须支付。

## 7. 不重做四次规范式的 raw DAG 提取

用 $X$ 表示当前 query 坐标，原环的 $a$ 表示端点。每个 DAG 子表达式只保

$$(P_0(X),\ \mathcal L_1(X;f)).\tag{29}$$

$P_0$ 是 $X$ 的有限多项式，系数是原函数在 $a$ 的值；$\mathcal L_1$ 是多项式系数微分算子与矩 $\int_a^X s^mf(s)\,ds$ 的和。

1. 原 $x^j$ 变为 $(X^j,0)$；$q^{(j)},\bar q^{(j)}$ 局部变为 $(0,D^jf)$。
2. 乘法保 $(P_0Q_0,P_0\mathcal M_1+Q_0\mathcal L_1)$，两个一次量的乘积进入已证明闭合的 $p^2\mathscr A$。
3. 原右积分节点保真实初值：

   $$
   J(E)(X)=J(E)(a)-\int_a^XE(s)\,ds.
   \tag{30}
   $$

   $J(E)(a)$ 仍是原函数，不替成独立自由 atom。对存量 raw atom $\mathcal I(E)=\int_r^xE$，同一规则准确写成 $\mathcal I(E)(X)=\mathcal I(E)(a)+\int_a^XE(s)ds$；实现使用这个加号，不默改旧环方向。
4. 左积分采用有限准确恒等。$j\ge1$ 时

   $$
   \begin{aligned}
   \int_a^X s^nf^{(j)}(s)\,ds
   ={}&\sum_{i=0}^{\min(n,j-1)}(-1)^i(n)_i
   X^{n-i}f^{(j-1-i)}(X)\\
   &+{\bf1}_{j\le n}(-1)^j(n)_j
   \int_a^X s^{n-j}f(s)\,ds,
   \end{aligned}
   \tag{31}
   $$

   并有

   $$
   \int_a^X s^n\!\left(\int_a^sy^mf(y)\,dy\right)ds
   =\frac{X^{n+1}\int_a^Xy^mf(y)\,dy-\int_a^Xy^{n+m+1}f(y)\,dy}{n+1}.
   \tag{32}
   $$

   下端边界由真实全平和左积分零初值支付。

四次输出的 $\mathcal L_1$ 系数恰为三次原尾函数。只对这些系数使用 R178/R179，规范后才将外 jets 在 $a$ 置零。端点 $a$ 幂、query $X$ 幂、局部 jet 阶或矩次数、完整三次 tail word 分别保为准确行标签。

这保任意嵌套右尾，只新增所需一次层；不重原四次完整 NF、旧 pure 关系或旧 38 列头部核。

## 8. 下一唯一消费的目标与严格权范围

为避免与 R225 的全权 $R\cap\ker\pi$ 混名，写

$$R^{(0)}=\Pi_0R,\qquad R^{(0)}_{\rm p0}=R^{(0)}\cap\ker\pi.\tag{33}$$

R201 已付完整算子

$$
H=C_2+\frac1{48}R^{(0_{\rm old})}
+\frac{11}{64}R^{(2_{\rm old})}
-\frac{13}{96}R^{(3_{\rm old})},
\qquad \pi H=0,\quad\lambda_+(H)=1.
\tag{34}
$$

旧下标保 R126 的原 20 列序号。新消费仅提取 H 与 $R^{(0)}$ 十六真基的模式 $-2$ 一次层。在 $\pi V=0$ 时，完整两混合目标由 $V_d=-4\operatorname{Re}V_{-2}$、$V_e=4\operatorname{Im}V_{-2}$ 恢复；尚未施加 pure 零的比较列，其模式 $-2$ 只作为线性投影，不称完整函数忠实表示。

先判宽上界

$$T(H_{-2})\stackrel{?}{\in}T(R^{(0)}_{-2}),\tag{35}$$

再合并三条**已保存** pure 查询判窄门

$$T(H_{-2})\stackrel{?}{\in}T((R^{(0)}_{\rm p0})_{-2}).\tag{36}$$

三行是 R116 权零块的完整幂尾坐标 $(c^0r^{32},c^1r^{31},c^2r^{30})$。R116 已证这些查询在该块 pure 像上秩三，R201 已证整个 $\pi(R^{(0)})$ 维数恰三。因此三行零在 $R^{(0)}$ 上等价 universal pure 零。只读旧原列的已存值，不重幂尾评价或 pure NF。

若 (36) 成员，得到 $\lambda_+=1$、pure 零、一次层零的准确原组合；这个层不能单独在 $U_0$ 读出 $\lambda_+$。若非成员，只得**权零**比较下新一次层商非零，不能宣称某个实际成本 period 非零，或其他权在固定圆不能抵消它。H 对 R 的一次层非成员也不自动给全部 $U_0$ 的 $\lambda_+$ 因子化，尚需对另外两个零权商方向核读出。

保 $(a,X)$ 和全部右尾输入时可作 universal 仿射输运，但单圆代入可能混不同权。本文不把 universal 分级当成固定圆已付分级。

## 9. 输入恢复和未提供的数据

本新消费只需：

- R109 已保存完整静态 L0/W 原导出；
- R126 十六真 $R^{(0)}$ 标签、原模式 $-2$ SHA 和旧秩证据；
- R196 同一八参考 $\Gamma$、C2 状态键 $(0,2,0,0)$ 及来源；
- R201 已发身份 (34) 与 metadata-only receipt；
- R116 完整已存幂尾证书中的三条旧行。

R126 未保存 portable 响应 DAG，R196 依新规仅保 metadata。故十六旧模式 $-2$ 根须按原标签必要恢复并逐根核旧 SHA，不重旧原 profile 评价、核、依赖或 pure 关系。C2 从旧静态根先作同 $\Gamma$ 原组合，再仅投影真权零。不恢复 N0/N2、v2/v4 或完整3974 forcing。

新工作是17根的一次层、共享三次尾表示及 (35)–(36)。阳性成员另组同系数原根差，独立重新提取这个新层核原差零；非成员给对全部新原列有准确值的有理对偶，不能靠非零不完备 NF。

本稿没有一个具体合法解析圆的 P 和全部尾值，第一轮只能交 universal 表结论。人工开发只查新截断、cubic 边界身份、旧 pure 行消费接口和小型有理终止例；真正17列仍仅公开 Actions。依根 README 只交脚本、参数、run、SHA，不新保存可重算 payload 或机器证书到仓库、Release、artifact。

完整多权 fixed-circle period quotient、全部 $p^2$ 层和 ruling joint 条件继续未决。
