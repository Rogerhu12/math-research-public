# R299：完整中心 ruling 的纯四次 self 降到 C²，以及全部角向余项的一次支付

日期：2026-11-15。**完整纸面证明；没有执行新的符号程序、profile 求积、秩计算、人工测试或研究运行。**

本稿将 R296 的完整主平方与 R292 的原跨包恢复合并。结果是整个例外中心 germ 的角向归约，不只一个 Gaussian 层：从构造起点加入一组明确的有限 $C^2$ 观测后，同一个真实解析微包圆满足
$$
\widehat{\mathscr K}_\theta
=\sin^2\theta\,\widehat{\mathscr K}_{\pi/2}.
\tag{1}
$$
这里保留原零层、一层、二层、全部 chain 和真实有序尾。式(1)没有把右侧函数置零。因此完整偶 germ 的剩余门缩为一个函数属于原 $\mathcal W_e$，仍须真正支付该门。

新增的低阶观测由完整纯四次 self 的真实边界补偿定义；它们不是把一般三阶能量冒充低阶数据。原 R295/R298 的单包 period self $q_B(u)$ 依然可能具有不可删的三阶平方项，与本稿的 instantaneous pure-ruling self 是不同对象。

来源：[R56 原 range](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)、[R243 中心偶部比较与有限函数空间](R243-finite-jet-criterion-for-the-complete-even-exceptional-ruling.md)、[R245 完整 block/平移次数](R245-complete-block-additivity-and-four-Gaussian-history-reduction.md)、[R248 完整四次槽](R248-complete-fourth-harmonics-and-complementary-block-reduction.md)、[R280 三个真实有序面积](R280-ordered-three-moment-areas-and-five-block-Gaussian-cancellation.md)、[R288 跨包第三局域](R288-cross-packet-third-locality-and-automatic-canonical-first-end-layers.md)、[R292 真实三矩跨包恢复](R292-zero-platform-periods-and-ordered-second-history-matrix.md)、[R293 初选有限低阶纤维](R293-finite-frequency-zero-of-all-necessary-symmetric-Gaussian-observations.md)、[R294 校正 self 的角向代数](R294-corrected-self-fibers-pay-all-angular-symmetric-Gaussian-histories.md)及 [R296 完整主平方](R296-complete-zero-one-Gaussian-layers-and-the-full-principal-square.md)。

## 1. 同一中心模型、右锚和实际偶部商

先固定已经按 R241 从起点安装的实际例外几何，在一个共同中心 germ 内写
$$
h=h_e e^{\varepsilon\sigma^2},\quad
k=\kappa(1-2\varepsilon\sigma^2),\quad
\omega=\kappa/h,\quad
\varepsilon=\kappa^2/4,\quad 0<\kappa^2<1/100.
$$
共同合法 profile 区间为 $I=[\ell,r_*]$，保 $z=x+\omega\ne0$。记
$e=hx+d$、$d=h\omega-k$、$Q=1+e^2$。
本稿的 $Z$、$C$ 使用 R243/R296 的同中心、同右锚 canonical 表示：
$$
Z(u,v)=\operatorname{Range}H(Y_u,Y_v),\qquad
C(a;u,v)=\operatorname{Range}H(Y_a,Z(u,v)).
\tag{2}
$$
第二、第三 characteristic 中心值为零，其他局部恢复量保原值。它们是允许有左尾的原分解项，不能单独冒作双 collar 的实际全局场。

原全路径传入 history 没有被丢弃。R243(2) 已证明完整比较
$$
[\operatorname{Ev}\mathscr K^0_\theta]
=[\widehat{\mathscr K}_\theta]\pmod{\mathcal W_e},
\quad
\mathcal W_e=\operatorname{span}
\left\{h,\sigma^2,\frac{1+4\varepsilon^2\kappa^2\sigma^4}{h}\right\}.
\tag{3}
$$
本稿先证明中心函数的身份，再经(3)取得实际偶部的商身份。不将(1)外推为整条实际闭路径的点态等式。

对原恢复分子定义
$$
\mathfrak b_\sigma(A,B)
=\frac1h\int_\ell^{r_*}(V_A)_x\cdot(V_B)_x\,dx.
\tag{4}
$$
带尾单项仍按(4)处理。下文先保全部边界，再作准确补偿。

## 2. 全部层共用的二次槽与角项

对对称二次槽 $A,B$ 置
$$
\mathcal B_\sigma(A,B)=\mathfrak b_\sigma(Z(A),Z(B)).
$$
将外槽作真正二次极化，定义
$$
\mathcal C_\sigma(u\odot v,B)
=2\{\mathfrak b_\sigma(Y_u,C(v;B))
+\mathfrak b_\sigma(Y_v,C(u;B))\},
\qquad
\mathcal K_\sigma=\mathcal B_\sigma+\mathcal C_\sigma.
\tag{5}
$$
因此 $\mathcal C_\sigma(u^2,B)=4\mathfrak b_\sigma(Y_u,C(u;B))$。第二个槽不能未经证明交换；后面只使用其准确对角二次值。

写
$$
F=f^2,\quad G=g^2,\quad H_1=f\odot g,\quad
\Delta=F-G,\quad
D_\theta=\sin^2\theta\,\Delta-2\sin\theta\cos\theta\,H_1.
$$
完整原第四 ruling 恰为
$$
\widehat{\mathscr K}_\theta
=-\mathcal B_\sigma(D_\theta,D_\theta)
+\mathcal C_\sigma(\phi_\theta^2,D_\theta)
=\mathcal C_\sigma(F,D_\theta)
-\mathcal K_\sigma(D_\theta,D_\theta).
\tag{6}
$$
这是 R56/R248 的完整式，未取高频极限，也未投掉某个 Gaussian word。

按 R259/R294 的原十二完整副本消掉 odd 角项后，四次代数准确给
$$
\widehat{\mathscr K}_\theta
=\sin^2\theta\,\widehat{\mathscr K}_{\pi/2}
+\sin^2\theta\cos^2\theta\,\Xi_\sigma,
\tag{7}
$$
$$
\Xi_\sigma
=\mathcal K_\sigma(\Delta,\Delta)
-4\mathcal K_\sigma(H_1,H_1).
\tag{8}
$$
本稿支付的是整个 $\Xi_\sigma$。原十二副本可用于整个式(6)，因为 R245 的完整 ruling 平移次数至多十，而非只对某一已付层成立。

## 3. 完整 pure-ruling self 是真实 C² 泛函

定义单包 self
$$
K_\sigma(u)=
\mathfrak b_\sigma(Z(u,u),Z(u,u))
+4\mathfrak b_\sigma(Y_u,C(u;u,u)).
\tag{9}
$$
它是 R248 pure 四次分子的负值。这里的“pure”指原第四表达中的齐次四次 profile 槽；并不把它和 whole-period pure 身份混同。

R296 §§4–6 已从原局部恢复、真实 chain 与完整 $W_C$ 证明：对一个 rank-one 输入 $\phi=c u$、$D=d u^2$、$d=a^2-c^2$，整个第四式的三阶平方部分为
$$
-a^2d\int\frac Qh L_\sigma[u]^2(u''')^2,
\quad
L_\sigma=\alpha_{m(\sigma)}/2+
\frac{Q(\gamma u'-e_\sigma u'')}{8h^3},
\tag{10}
$$
其差是保全部右 primitives、左值及 Green 项的准确 polynomial/$C^2$ 泛函。特别这不是只说某个振荡极限的主符号为零。

在这个原多项式身份中取形式 $a=0$、$d=-c^2$。由(6)左边是 $-c^4K_\sigma(u)$，而(10)右边的三阶平方为零。因此
$$
\boxed{K_\sigma:C_c^\infty(J)\longrightarrow\mathbb R
\text{ 有连续、光滑的四次 polynomial/}C^2\text{ 延拓}.}
\tag{11}
$$
这里只在同一原公式内抽取幅度系数，没有构造种子 $f=0$ 的非法实际等距圆。R296 的三项抵消是任意实幅参数的代数身份；不需要单包具有不可能的零三矩。

为明确(11)的正则性内容，剩余三阶项至多线性为
$A(x,u,u',u'',\mathbf J)u'''$。按 R296(16) 对 local $u''$ 取 primitive，再一次真实分部积分，将它准确改为只含 $u,u',u''$ 与有限右积分的表达。每个原 primitive 的导数也是相应的低阶密度；真实 collar 边项已经保留或因紧端 jets 为零消失。有限 $\sigma$ 积分作用于这些系数，不增加 profile 导数阶。

本稿不对 R295 的 $q_B(u)$ 作同一替换。那个量是一个不同的 period 投影；R298 的 $3\int(u'')^2(u''')^2/512$ 仍完整存在。

## 4. 原跨包核：两个真实二阶尾和一个第三局部场

取 $u$ 在 $v$ 左方，两支撑有正间隙，记真实三矩
$$
\mu(u)=\left(\int(u'')^2,\ \int x(u'')^2,\
\int\{x^2(u'')^2+2(u')^2\}\right).
\tag{12}
$$
沿 R292(11)–(15)，由同一个 $m(\sigma)$ 得到二阶左尾
$$
V_{Z_\mu}(x)=xU_\mu+V_\mu=:\Pi_\mu(x).
\tag{13}
$$
所有分量对 $\mu$ 线性。$U_\mu,V_\mu$ 是原几何/history 的确定函数，不能独立指定；(13)也没有将该尾置零。

因为 $(V_{Z_v})_x=U_\nu$ 在 $Z_u$ 的整个非零区间上为常向量，且 $Z_u$ 在自身右侧为零，
$$
\boxed{\mathfrak b_\sigma(Z_u,Z_v)
=-\frac1h\,\Pi_\mu(\ell)\cdot U_\nu.}
\tag{14}
$$
这是完整积分的端差。两非紧分子之间的 Green 项由此显式保留。

R288 给 $C(u;v,v)$ 整体支撑于左包，而 $C(v;u,u)=0$。R292(18) 保其真实 characteristic
$$
W_C=\beta_\nu(\sigma,x)u'-\partial_x\beta_\nu(\sigma,x)u,
\qquad\beta_\nu(0,x)=0,
\tag{15}
$$
其中 $\beta_\nu$ 为二次 $x$ 多项式，由原公式
$$
\partial_\sigma\beta_\nu=
\frac14\left[
\left(t_\nu-kq_\nu-\frac{\gamma\tau_\nu}{h}\right)\frac Q{h^2}
-\tau_\nu\partial_\sigma\left(\frac Q{h^2}\right)
\right]
\tag{16}
$$
沿共同中心积分。$(t_\nu,q_\nu,\tau_\nu)$ 全按 R292 的原二阶尾确定。

令
$$
\mathcal A_{\beta_\nu}=he\beta_\nu-\frac Q2\partial_x\beta_\nu,
\quad
\mathbf a_{\beta_\nu}=
([x^0]\mathcal A_{\beta_\nu},
[x^1]\mathcal A_{\beta_\nu},
[x^2]\mathcal A_{\beta_\nu}).
$$
其三次项准确抵消。R292(20)–(21) 已逐项保全部局部 $\tau$ 项并得到
$$
\boxed{\mathfrak b_\sigma(Y_u,C(u;v,v))
=\frac1{4h}\,\mu\cdot\mathbf a_{\beta_\nu}.}
\tag{17}
$$
这里 $2(u')^2$ 正好给 $\mathcal A_{\beta_\nu}''$ 项，不能从(12)删掉。

因此完整有序 cross 核是
$$
\boxed{
\Gamma_\sigma(\mu,\nu)
=-\frac2h\,\Pi_\mu(\ell)\cdot U_\nu
+\frac1h\,\mu\cdot\mathbf a_{\beta_\nu}.
}
\tag{18}
$$
第一项是两次(14)，第二项是四次(17)，所有因子来自(5)。这是整个中心函数的真实三矩双线性核，包含全部局部与累计 history；不只一个 principal 或 period 值。

## 5. 校正 self、原锚及完整有序展开

定义
$$
\boxed{\widehat K_\sigma(u)
=K_\sigma(u)-\frac12\Gamma_\sigma(\mu(u),\mu(u)).}
\tag{19}
$$
由(11)、(12)、(18)，它仍是连续光滑的四次 polynomial/$C^2$ 观测。

这个补偿也准确消掉任选左零 collar 的位置。改变 $\ell$ 时，(9)中唯一非局域积分段来自 $Z_u$ 的常导数尾，故
$$
\partial_\ell K_\sigma(u)=-|U_\mu|^2/h.
$$
而(18)给
$$
\partial_\ell\{\Gamma_\sigma(\mu,\mu)/2\}=-|U_\mu|^2/h.
$$
所以 $\widehat K_\sigma$ 与这个端点选择无关。右锚始终是真实共同右零 collar；没有对实际场重置任何积分常数。

现设 $u_i$ 从左到右不交，$A=\sum_i\lambda_i u_i^2$。R248 的紧分子端差使不同外包的 $Y$–$C$ 配对为零；R288 与(14)–(18)保全部余下交叉。因而
$$
\mathcal K_\sigma(A,A)
=\sum_i\lambda_i^2K_\sigma(u_i)
+\sum_{i<j}\lambda_i\lambda_j
\Gamma_\sigma(\mu_i,\mu_j).
\tag{20}
$$
式(20)允许实有符号 $\lambda_i$，只是准确槽极化；不把它解释成负路径。

对实际圆 $f=\sum a_i u_i$、$g=\sum b_i u_i$，记
$R_i=a_i^2-b_i^2$、$T_i=a_ib_i$。原三矩保证
$$
\sum_iR_i\mu_i=\sum_iT_i\mu_i=0.
\tag{21}
$$
和 R294 一样，(8)、(19)–(21)给
$$
\boxed{
\Xi_\sigma=
\sum_i(R_i^2-4T_i^2)\widehat K_\sigma(u_i)
+\sum_{0\le r<s\le2}\gamma_{rs}(\sigma)\mathcal A_{rs},
}
\tag{22}
$$
其中 $\gamma_{rs}$ 为(18)双线性矩阵的反对称坐标，
$$
\mathcal A_{rs}=
\sum_{i<j}(R_iR_j-4T_iT_j)
(\mu_{r,i}\mu_{s,j}-\mu_{s,i}\mu_{r,j}).
\tag{23}
$$
这是 R280 的三条真实有序面积规范，无新增方向数或 rank 主张。对称 cross 由(21)准确变成(19)的 self 补偿；反对称部分没有被平均或删除。

## 6. 这是有限低阶观测，不能只写一个未实施的函数约束

先证明共同平移
$u_t(x)=u(x-t)$ 的准确次数界：
$$
\boxed{\widehat K_\sigma(u_t)
=\sum_{k=0}^{10}t^k\,\widehat K_{\sigma,k}(u).}
\tag{24}
$$
(19)已与左 collar 位置无关，因此在证明次数时可以同时平移这个积分端点，以固定母坐标积分区间；这仅是已经证明的同一值身份，不改实际场或全局锚。

R245 §3 的原逐槽界随后直接适用：第一分子对 t 次数至多1，第二至多5，第三至多9，故两种完整 ruling 配对至多10。局部恢复、$\sigma$ 积分和换回共同右零 collar 的 Volterra 积分均不增加此界。扣去(18)的三矩尾项也不增加次数。单包带尾本来可能造成的移动下端贡献，已经由(19)准确补偿，不能未经这一步就套完整 block 界。

R56/R243 另给一个与 profile 数值无关的有限维真实函数空间 $\mathscr E$，使
$\sigma\mapsto\widehat K_\sigma(u_t)$ 对所有允许 u,t 都在 $\mathscr E$ 内。它来自固定第二、第三恢复的有限运算清单，包含全部真实长度至多二的中心 history，不假定冗余字生成元独立。

选 $\mathscr E$ 的真实函数基，记其维数为 n。存在 germ 内有限点
$\sigma_1,\ldots,\sigma_n$，使评价映射
$$
\mathscr E\longrightarrow\mathbb R^n,\quad
v\longmapsto(v(\sigma_1),\ldots,v(\sigma_n))
\tag{25}
$$
单射。证明是有限维函数空间的一般事实：如果全部点评价的张成不是整个对偶，就有非零函数被所有点评价杀掉，矛盾；从张成中取有限基即可。此处没有声称运行过选点或数值 rank，也不需要给尚未编译的 n 一个虚构值。

从构造起点明确取
$$
\boxed{
\mathcal F^{\rm ang}
=\left(\mathcal F^+,\ 
[t^k]\widehat K_{\sigma_j}(u_t):
1\le j\le n,\ 0\le k\le10\right).
}
\tag{26}
$$
$\mathcal F^+$ 是 R294 的全部旧观测。式(24)使系数可由十一种固定允许小平移的值作准确插值取得；因此每一项确实是 $C^2$ polynomial 泛函，不要求 profile 有额外十阶导数。式(25)保证保持(26)就保持整个 $\widehat K_\sigma(u_t)$，不是仅保持有限采样后猜整个函数。

这也避免强迫冗余 geometry-word 的每个系数分别为零。n 或 $11n$ 只是有限接口大小，不是控制响应的秩，(26)的实际最大秩由 R293 的初选纤维构造处理。

## 7. 等背景真格点与三个已付有序面积使整个 Xi 零

在每个原基本布局内，
$$
b_i^2=B_0,\quad R_i\in\{-B_0/2,8B_0\},
\quad R_i^2-4T_i^2=\frac{7B_0}{2}R_i,
\quad\sum_iR_it_i^k=0\quad(0\le k\le10).
\tag{27}
$$
先从同一个母包放置，再允许各包在同一个初选 $\mathcal F^{\rm ang}$ 纤维内作实际扰动。由(24)–(27)，对整个 germ 同时有
$$
\sum_i(R_i^2-4T_i^2)\widehat K_\sigma(u_i)
=\frac{7B_0}{2}\sum_iR_i\widehat K_\sigma((u_0)_{t_i})=0.
\tag{28}
$$
(28)不把任何未指定 self 值任意设成零；它用的是原十次矩消去与准确同纤维保持。

原完整复制与最后五个正四次 block 的所有位置、权和有序规则保留。各完整 base 的(21)使跨 base 的 wedge 为零；R280 最后准确支付三条(23)。因此(22)给
$$
\boxed{\Xi_\sigma\equiv0}
\tag{29}
$$
作为完整中心函数成立。将其放回(7)即得(1)。

按照 R293 §6，有限 $C^2$ polynomial 映射(26)必须从最初选定；最大秩母包、有限纠正方向、正解析 prefactor 与有限高频根联合构造。它可以同时保 R293/R294 已付的全部二层 Gaussian、72面积、三矩、完整第三和六识别能量。若另选择 R296 的单个一层 jet 目标，主秩31和相同初选纤维入口仍适用；本稿不新增任何未知主关系。

此处没有在某个已冻结旧圆上无偿添加新约束，也没有改变已选几何的参数后仍称同一旧纤维。

## 8. 完整偶 germ 的剩余门准确缩成一个函数

由(1)、(3)，在上述新圆上
$$
\boxed{
[\operatorname{Ev}\mathscr K^0_\theta]
=\sin^2\theta\,[\operatorname{Ev}\mathscr K^0_{\pi/2}]
\quad\text{于 }C^\omega_{\rm even}/\mathcal W_e.
}
\tag{30}
$$
因此
$$
\boxed{
\operatorname{Ev}\mathscr K^0_\theta\in\mathcal W_e
\text{ 对全部 }\theta
\quad\Longleftrightarrow\quad
\operatorname{Ev}\mathscr K^0_{\pi/2}\in\mathcal W_e.
}
\tag{31}
$$
反向用(30)，正向只取 $\theta=\pi/2$。这一次覆盖整个零/一/二层函数，不是只用某个 leading term 看到两个谐波。

在已有 R294 全二层零的构造上，(31)的右侧仍包含 R296 的四个完整一层系数和零层 $\mathcal W_e$ 商。R296 可再支付的单个中心 jet 不能代替它们。还必须核实际主空间的全部关系与真实 $C^2$ 基线，不能把54/52的通用 symbol 上界当成全函数可达。

更不能从(31)跳到整条实际路径的 ruling：其他 s 段、奇部、canonical period、平台/flux/内部 Laurent、同一二阶 gauge 的 joint 匹配、高阶收敛及主课题的固定度量有限嵌入族仍另欠。R297/R298 的几何控制与本稿母包选择之间也有自己的兼容次序，尚未因此共同解决。

本稿新增完成项是完整 pure-ruling self 的准确 $C^2$ 性、完整三矩有序核(18)、明确有限初选观测(26)，以及其给出的全中心角向支付(29)–(31)。所有结论均来自原恢复的纸面恒等，未产生新的机器结果或阶段完成声明。
