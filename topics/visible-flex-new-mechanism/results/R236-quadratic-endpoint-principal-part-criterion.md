# R236：二次平端层的目标主部判据与无需逆解的有限观测

日期：2026-11-15。**完整纸面推导；没有新的 profile 求积、原目标提取、符号研究运行或候选评价。**

本文接 [R226](R226-exact-flat-end-layers-and-remainder-germs-of-the-response-chain.md) 的精确指数积分和 [R234](R234-weight-zero-first-endpoint-layer-cancelled-by-a-zero-pure-response.md) 的一次层消去。新增内容是：在 R226 的有限极点光滑类内，二次层的光滑可解性可直接从目标的有限 Laurent 主部判断，不必先递推退化方程逆解的 jets。

这里仍取 R225/R230 的首个 f 上升、局部 g=0 的左平端。它不是 R233 新圆的端点结论，也不把一个局部条件替代完整 period。

## 1. 固定真实端芽、平台和分层

令 t=x-a_*，在 t>0 的真实材料坐标中取

$$
p=f'=\epsilon_p e^{-c/t}a(t),\qquad
c>0,\quad \epsilon_p\in\{1,-1\},\quad
a\in C^\infty([0,t_0]),\quad a>0,
\tag{1}
$$

并令 f(t)=\int_0^t p、g=0。c 是实际宽度后的参数，不能在导数不变时暗设为 1。记

$$
\mathscr A=\bigcup_{N\ge0}t^{-N}C^\infty([0,t_0]),
\qquad b=\frac{a'}a,\qquad
\lambda=\frac{p'}p=\frac c{t^2}+b.
\tag{2}
$$

假定目标已经付清本文指定的一次端层消去。由 R230 可写成

$$
G=P_2+p^2B+p^3C,\qquad B,C\in\mathscr A.
\tag{3}
$$

可直接取 C=0；显写高层是为说明判据不受其影响。P_2 是由真实左零平台延入 germ 的原二次以下多项式，不是任意改选的减项。原 period 的平台必要门仍是

$$
P_2''=0.
\tag{4}
$$

若尚未支付 (4)，可如 R226 只讨论平台修正后的 germ，但不能因此声称原目标可解。以下定理在 (4) 已付时作用于 G；否则只作用于扣除真实平台二次项后的目标。

零端通量分支沿用 R225/R226：

$$
\mathcal M_fu=(A_fu')'-V_fu=G'',\qquad
u=w',\quad A_f=6pp''-2(p')^2,\quad
V_f=6(p'p'')',
\tag{5}
$$

$$
F_G(t)=\int_0^t p(s)G''(s)\,ds,\qquad
u(t)=p(t)\left(C_0+
\int_{t_*}^{t}\frac{F_G(s)}{A_f(s)p(s)^2}\,ds\right).
\tag{6}
$$

光滑 w 必有该零端通量。这里不把含另一非零通量常数的齐次支路纳入光滑结论。

## 2. 直接目标判据

**定理 1。** 设真实目标满足

$$
G''=p^2R+p^3R_3,\qquad R,R_3\in\mathscr A.
\tag{7}
$$

则 (6) 的零端通量解可在 t=0 光滑延拓，当且仅当

$$
\boxed{t^8R\in C^\infty([0,t_0]).}
\tag{8}
$$

若成立，(6) 中每个 C_0 都给光滑延拓；不同 C_0 只差全平项 C_0p。若不成立，没有一个 C_0 能修复该 germ。

**证明。** 直接使用 p'=\lambda p，得到

$$
\frac{A_f}{p^2}=\mathsf A=6\lambda'+4\lambda^2,
\tag{9}
$$

$$
\frac{V_f}{p^2}=\mathsf V
=6\bigl((\lambda')^2+\lambda\lambda''
+5\lambda^2\lambda'+2\lambda^4\bigr).
\tag{10}
$$

于是原方程准确变成

$$
\mathsf A u''+(\mathsf A'+2\lambda\mathsf A)u'
-\mathsf V u=R+pR_3.
\tag{11}
$$

乘 t^8 后，左端具有形式

$$
\mathsf P u=t^4A_2(t)u''+t^2A_1(t)u'+A_0(t)u,
\tag{12}
$$

其中 A_i 都真属于 C^\infty，且

$$
A_2(0)=4c^2,\qquad A_1(0)=8c^3,\qquad
A_0(0)=-12c^4\ne0.
\tag{13}
$$

若 u 光滑，(12) 光滑。t^8pR_3 及其全部导数全平，所以 t^8R 必光滑。这证明必要性，不需要对 u 预设有限 Laurent 展开。

反过来若 (8) 成立，写 v=t^8R\in C^\infty，则二次项准确为 p^2t^{-8}v。R226 第 4.2 节取 \nu=-8，已经证明其零通量逆解为一个真正光滑函数加 C_0p；第 4.3 节证明 p^3R_3 所给逆解全平。两者相加给充分性。这里引用的是 R226 的精确光滑余项定理，不是形式渐近级数。证毕。

因此 R226 的二次层有限 jet 条件，在目标一侧等价于“R 没有严格低于 t^{-8} 的有效极点”。同一个 R 用不同 N 表示不会改变条件。

## 3. 对原目标 G 的四次权重判据

**定理 2。** 在 (1)–(4) 下，(6) 的光滑可延拓性当且仅当

$$
\boxed{t^4B\in C^\infty([0,t_0]).}
\tag{14}
$$

令 V=t^4B。若 (14) 成立，则所有零端通量解有相同的端点值

$$
\boxed{u(0)=-\frac{V(0)}{3c^2}.}
\tag{15}
$$

它不必为零；本定理要求光滑，不把光滑与全平混淆。

**证明。** 先准确微分：

$$
\frac{(p^2B)''}{p^2}
=B''+4\lambda B'+(2\lambda'+4\lambda^2)B.
\tag{16}
$$

把 B=t^{-4}V 和 (2) 代入，得到完整公式

$$
\begin{aligned}
t^8\frac{(p^2B)''}{p^2}
={}&t^4V''
+t^2(4c-8t+4bt^2)V'\\
&+\bigl[
4c^2-20ct+(20+8cb)t^2-16bt^3
+(2b'+4b^2)t^4
\bigr]V.
\end{aligned}
\tag{17}
$$

记右端为 \mathsf QV。若 V 光滑，显然 \mathsf QV 光滑。反之，V\in\mathscr A 若不光滑，其有限 Laurent 主部有一个最低负幂 t^m，m<0，非零系数记为 v_m。第一项 t^4V'' 的最低可能幂为 m+2，第二项为 m+1，而零阶系数首值为 4c^2。因此

$$
[t^m](\mathsf QV)=4c^2v_m\ne0.
\tag{18}
$$

高次项及全平余项不能消去这一最低负幂，故 \mathsf QV 也不光滑。于是 \mathsf QV 光滑 iff V 光滑。

对 p^3C 连续两次求导仍在 p^3\mathscr A，除以 p^2 再乘 t^8 后全平。由定理 1 与 (17)，得到 (14)。在光滑情形，令 t=0，(12)–(13) 的左端只余 -12c^4u(0)，(17) 的右端只余 4c^2V(0)，立即得到 (15)。证毕。

这也给端点 Taylor 递推的简洁结构：每一阶中，最高待定 u-jet 的系数来自 A_0(0)，非零；其余只读有限个较低 jets。本文的光滑存在性来自 R226，不依赖把这组形式递推当作存在证明。

## 4. 有限主部观测的准确意义

对 T 一次层已消去的目标类，定义

$$
\boxed{
\mathfrak B_{a_*}(G)
=\operatorname{pp}_{<0}\!\left(t^4B\right),
}
\tag{19}
$$

其中 \operatorname{pp}_{<0} 表示有限 Laurent 主部，只保严格负幂。由于 B\in\mathscr A，这一主部总是有限且与选取的极点上界无关。

若 (3) 的拆分改变为 B+pD、C-D，D\in\mathscr A，(19) 不变，因为 t^4pD 全平。P_2 必须仍是同一个真实平台多项式；不能通过任意改变 P_2 来改变端层。

对固定真实 profile 和 p，(19) 是该目标类上的线性观测。定理 2 说明：

$$
\boxed{
P_2''=0\ \text{且本文一次层已消去时，}\quad
\mathfrak B_{a_*}(G)=0
\iff \text{零端通量 germ 可光滑延拓。}
}
\tag{20}
$$

凡真实光滑 gauge 给出的目标属于此类，其 (19) 必为零。这里付的是 R225 完整 range 中这个左平端 germ 的准确门，不是整区间 L_f 成员关系。

若已知 B=t^{-N}b_N，b_N\in C^\infty，则：

- N\le4 时，(19) 自动为零；
- N>4 时，(19) 准确由 b_N 在 0 的第 0 至 N-5 阶导数给出，共 N-4 个线性系数条件。

条件数取决于已证明的原 DAG 极点上界，不是先任选有限 jet 阶数再把后续遗漏。若其中一些系数恒等消失，实际条件可减少。

两个简单 germ 显示门的位置：

$$
G=p^2t^{-5}\quad\Longrightarrow\quad
u(t)\sim-\frac1{3c^2t},
\tag{21}
$$

所以目标自身全平光滑仍不保证光滑 gauge。另一方面，

$$
G=p^2t^{-4}
\quad\Longrightarrow\quad
u\in C^\infty,\qquad u(0)=-\frac1{3c^2}.
\tag{22}
$$

(21)–(22) 只是精确类内的说明例，不声称它们属于某个未验证的 canonical U 或真实响应库。

## 5. 怎样给新原式提取一个可审查的有限上界

R226 已准确证明，首上升端的每个固定 profile jet 满足

$$
\frac{f^{(j)}}p\in t^{\,2-2j}C^\infty,\qquad j\ge0.
\tag{23}
$$

j=0 用精确衰减积分，j\ge1 用 p=e^{-c/t}a 的有限次微分。对于任何 d\ge1 和 \nu\in\mathbb Z，

$$
p^{-d}\int_0^t p(s)^d s^\nu v(s)\,ds
=t^{\nu+2}\widetilde v(t),
\qquad \widetilde v\in C^\infty.
\tag{24}
$$

所以，给定一份有限原 DAG，可以按有限次乘法、微分及真实左增量积分，在每个节点传播一个保守但证明过的 pole 上界。由 (19) 只需保留会进入严格负幂的有限 jets。该截断界先由原 DAG 结构支付，不需要重算完整第四正规形或对整个目标作数值 ODE。

所有右尾常数仍必须是原同右锚表达式的真实值。本文下一次消费若用 quadratic tail 系数，应保它们之间的 shuffle、IBP、颜色和共锚关系；不能把这些数独立任赋。旧原积分 \mathcal I=\int_r^x 的局部增量是正号；若转写正右 J，须完整转换符号。没有把多项式外系数或 word 内的 profile jets 先行删掉。

## 6. 对 H_E 的后继任务与尚未支付之处

R234 已给明确 H_E：whole pure 零、\lambda_+=1，并且本文特定一次层 T 为零。因此它是 (19) 的一个新合法候选输入，但**本文没有计算其 \mathfrak B 值**，也没有预报零或非零。

最小新消费可只恢复 C_2 与 R_0,R_1,R_2,R_3,R_4,R_{10} 的必要原根，继承 R234 已付关系，不重新跑那 17 个一次层、旧 pure 查询或完整 H0。新目标仅是局部二次层与 (19) 的有限主部。固定解析 germ 若尚未指定，就必须明确使用的 universal 有限 jet/真实尾函数意义；其形式非零不自动证明某个未指定固定圆的实际值非零。

即使 (19) 对 H_E 为零，仍不能跳过：

- 原 P_2'' 平台门；
- R225 的每包总通量、内部 p/A_f 退化、其他端点与右锚条件；
- 全相位完整 period 和同一个 w 的 ruling 联立；
- 更高阶收敛、同一固定 g 的有限族、嵌入、reach 与幅度要求。

反之，某个代表的 (19) 非零也不证明整个响应仿射类都失败；仍可能用保持 whole pure 和一次层为零的真实响应修复。本文不以一个局部读出代替该完整比较问题。

本结论将二次层的准确 germ 门改写成可直接读取的目标主部。它没有结束课题，后继仍按 open 中的未付条件推进。
