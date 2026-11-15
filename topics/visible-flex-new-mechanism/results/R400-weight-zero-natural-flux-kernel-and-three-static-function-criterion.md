# R400：完整自然通量的权零联合核恰归于三个原静态函数

日期：2026-11-15。**纸面原空间推论；没有执行新的原根恢复、profile 评价、积分、秩、成员或人工检查。**

本稿准确核清一个实际联合控制接口：R333 的 $H_*,J_4,J_6$ 已同时消去 whole pure 与完整 universal self，但其自然总通量不在该成员结果的结论内。特别，$H_*$ 不是已在 R382 全部消去自然通量的正常 $H_1,H_2$ 层。

更具体地，本稿把增强投影的全部权零商，以及原正字符能否经过该投影下降，准确归于三个**完整函数**
$$
n_i:u\longmapsto\Lambda_u(C_i),\qquad i=2,4,6.
$$
这些函数目前尚未求值。本稿给充要条件，不将未知条件当作已经成立。

来源：[R196 原完整权零空间与正字符](R196-complete-weight-zero-character-head-positive-ray-and-strict-canonical-cost.md)、[R316 原 $H_*$](R316-complete-weight-zero-self-membership-and-positive-character-representative.md)、[R333 两剩余联合成员及实际 E 控制](R333-complete-joint-pure-self-membership-and-real-finite-control.md)、[R352 完整自然总通量](R352-ordered-three-moment-tail-map-and-natural-total-flux-quotient.md)、[R365 独立第 5 节的完整仿射协变](R365-complete-H-layer-affine-orbits-and-exact-total-flux-functionals.md)、[R382 修正后完整 H 层消去](R382-universal-cancellation-of-the-corrected-H-total-flux-and-independent-Q4.md)。

## 1. 原映射和完整函数目标

沿用真实完整成本空间 $U$、真实响应空间 $\mathcal R$ 和原真权分解 $U=\bigoplus_\sigma U_\sigma$。所有 profiles 为共同合法区间内的实紧光滑函数；所有原积分保持同一右锚、原 characteristic 初值及实际左尾。

R333 的联合映射是
$$
E=(\pi,\mathcal Q),\qquad
\mathcal Q(V)(u)=\frac14[x^2]_{\rm left}V(u^2,0).
\tag{1}
$$
这里 $\pi$ 是整个 universal pure 函数，$\mathcal Q$ 是整个左二次 self 泛函。后者不是下面的总通量，也不是整个输出 $V(u^2,0)$。

为固定规范，R352 的自然总通量是
$$
\begin{aligned}
\Lambda_u(V)
={}&\int u'''V(u^2,0)
-\frac{16}{5}\int u'''\pi V(u)\\
&-\frac{32}{15}\int u'''\mathscr G_{V,u}(\mu(u)),\\
\mu(u)={}&
\left(\int(u'')^2,\ \int x(u'')^2,\
\int\{x^2(u'')^2+2(u')^2\}\right).
\end{aligned}
\tag{2}
$$
$\mathscr G$ 是原有序 $2+2$ pure 输出对右包真实三矩的完整线性尾映射。它不是任意补偿项；尤其最后一项不能由单包非紧左尾中删去。

定义
$$
\mathcal N:U\longrightarrow\mathscr F,\qquad
\mathcal N(V)(u)=\Lambda_u(V),\qquad
J_\infty=(E,\mathcal N).
\tag{3}
$$
$\mathscr F$ 只需取这些实际函数的线性空间。因为 $U$ 有限维，$\mathcal N(U)$ 有限维；本稿不为它指定未经证明的维数。

R344/R352 已付
$$
\boxed{\mathcal N(\mathcal R)=0.}
\tag{4}
$$
若 $\pi V=0$，则 (2) 的两个修正项均准确为零，故
$$
\Lambda_u(V)=\int u'''V(u^2,0).
\tag{5}
$$
但 $\mathcal Q(V)=0$ 本身不推出 (5) 的右边为零。

## 2. $H_*$ 的实际组成来自 $F_0$，不是正常 H 层

下列 $R_j$ 始终是 R126 的原 old-column 标签，不是压缩列位置。R316 的准确代表为
$$
\boxed{\begin{aligned}
H_*={}&C_2+\frac{649}{768}R_2-\frac{73}{3072}R_3
+\frac{649}{1536}R_4-\frac{821}{768}R_5\\
&+\frac1{64}R_7+\frac{187}{1024}R_9.
\end{aligned}}
\tag{6}
$$
已经证明
$$
E(H_*)=0,\qquad\lambda_+(H_*)=1.
\tag{7}
$$

这里 $C_2$ 是 R196 **静态正常族 $F_0$** 的原 normal index 2。按 R196 第 4 节明确规定的状态键顺序
$$
(h\text{ 幂},\,k\text{ 幂},\,\omega\text{ 幂},\,\log h\text{ 幂}),
$$
三个静态原系数为
$$
C_2:(0,2,0,0),\qquad
C_4:(0,4,0,0),\qquad
C_6:(1,1,1,0).
\tag{8}
$$
所以 $C_6$ 对应这里的 $hk\omega$ 键；不把状态键第三项改写成 $\log h$。

由 (4)、(6)，当前准确结论只是
$$
\boxed{\mathcal N(H_*)=\mathcal N(C_2)=n_2.}
\tag{9}
$$
R382 的完整定理是所有状态的正常 $H_1,H_2$ 自然通量为零；它不包含 $C_2$。两处字母 H 不能互换。

还可从已付来源直接严格区分这两个空间。R196 的完整 normal 赋值表表明 $\lambda_+$ 杀掉全部 $\mathcal R$ 和所有正常 $H_1,H_2$ 系数；后一族的真权零呈示为零，其余权也由 $\lambda_+$ 的权零性消去。因此
$$
H_*\notin
\mathcal R+\operatorname{span}
\{H_1(S),H_2(S):S\text{ 为允许状态}\}.
\tag{10}
$$
否则对其施 $\lambda_+$ 将把 (7) 的 1 变成 0。

(10) 不给出 $n_2$ 非零；它只严格排除用正常 H 消去定理代替 $C_2$ 原式的推断。

## 3. 原三个联合零代表及权零核

R333 的另外两个真实代表是
$$
\begin{aligned}
J_4={}&C_4+\frac{95}{768}R_2+\frac1{3072}R_3
+\frac{95}{1536}R_4-\frac{115}{768}R_5\\
&-\frac1{64}R_7+\frac{29}{1024}R_9,\\
J_6={}&C_6-\frac5{384}R_2+\frac5{1536}R_3
-\frac5{768}R_4+\frac1{384}R_5+\frac1{512}R_9 .
\end{aligned}
\tag{11}
$$
它们满足
$$
E(J_4)=E(J_6)=0,\qquad
\mathcal N(J_4)=n_4,\quad \mathcal N(J_6)=n_6.
\tag{12}
$$
R196 还给
$$
\lambda_+(C_2)=1,\qquad
\lambda_+(C_4)=\lambda_+(C_6)=0,\qquad
\lambda_+(\mathcal R)=0.
\tag{13}
$$
因此 $\lambda_+(J_4)=\lambda_+(J_6)=0$。

这里只消费已发表的真实函数空间身份
$$
U_0=\mathcal R_0\oplus
\operatorname{span}\{C_2,C_4,C_6\},
\qquad E(U_0)=E(\mathcal R_0).
\tag{14}
$$
由 (6)、(11)、(14)，每个 $V\in U_0\cap\ker E$ 有唯一表示
$$
\boxed{
V=aH_*+bJ_4+cJ_6+R,\qquad
R\in\mathcal R_0\cap\ker E.
}
\tag{15}
$$
唯一性中的 $R$ 指完整元素，不要求为它另选坐标基。证明只需先在 $U_0/\mathcal R_0$ 读取三个系数，再用 $E(V)=0$；无需重做成员或秩。

施自然映射和正字符，得到
$$
\boxed{
\mathcal N(V)=a n_2+b n_4+c n_6,\qquad
\lambda_+(V)=a.
}
\tag{16}
$$
所以完整自然通量在旧 E 核内的权零新增像准确为
$$
\mathcal N(U_0\cap\ker E)
=\operatorname{span}\{n_2,n_4,n_6\}.
\tag{17}
$$
这里的 span 是所有实紧 profiles 上的函数身份，不是一组固定测试值。

更完整地，由 (4)、(14) 可先减去匹配 E 的响应，故
$$
\boxed{
\begin{aligned}
J_\infty(U_0)
&=E(U_0)\oplus\operatorname{span}\{n_2,n_4,n_6\},\\
J_\infty(\mathcal R_0)&=E(U_0)\oplus\{0\},\\
J_\infty(U_0)/J_\infty(\mathcal R_0)
&\simeq\operatorname{span}\{n_2,n_4,n_6\}.
\end{aligned}}
\tag{18}
$$
式 (18) 是准确的线性商，不宣称其真维为三；这三个函数可能有关系，也可能有零函数。

## 4. 从全权核到权零核：必须使用完整自然函数

R365 **独立第 5 节**从原 R89 的同锚输运证明
$$
\Lambda_u(P_{H,c}V)
=H^2\Lambda_{C_{H,c}u}(V),
\qquad
(C_{H,c}u)(x)=u((x-c)/H).
\tag{19}
$$
其中真实三矩按可逆三角矩阵一起输运，所有有序尾都保留。该协变不依赖 R365 已撤回的 H 非零数值公式。

因此 $\ker\mathcal N$ 对真实正仿射作用不变。R322/R323 已付 $\ker E$ 的相同稳定性，所以
$$
\ker J_\infty=\ker E\cap\ker\mathcal N
\tag{20}
$$
也稳定。使用原 U 的有限 Laurent 真权分解，有限个 $H=1$ 附近的正缩放线性组合给各权投影。于是
$$
K\in\ker J_\infty
\ \Longrightarrow\ 
\Pi_0K\in\ker J_\infty,\qquad
\lambda_+(\Pi_0K)=\lambda_+(K).
\tag{21}
$$
所有输入可先限制在共同更小窗口以保 collars，随后用原有限函数恒等延拓。没有新数值插值或投影执行。

注意 (19) 用的是**全部紧输入 u 的自然函数**。它不能由两个固定 profiles 的零值替代。R392 对固定两条自然读出已构造的 $\lambda_+$ 核代表，不能因此直接升级成 (20) 中的代表。

## 5. 消除原正字符的精确充要条件

由 (15)–(21)，得到本稿的主要新接口：
$$
\boxed{
\begin{aligned}
&\exists K\in U:\quad
E(K)=0,\quad\mathcal N(K)=0,\quad\lambda_+(K)=1\\
&\hspace{20mm}\Longleftrightarrow\quad
n_2\in\operatorname{span}\{n_4,n_6\}.
\end{aligned}}
\tag{22}
$$

**充分性。** 若存在实常数 $a,b$ 使
$$
n_2=a n_4+b n_6
\quad\text{对全部真实紧 }u,
\tag{23}
$$
则取
$$
K=H_*-aJ_4-bJ_6.
\tag{24}
$$
(7)、(12)、(13) 直接给 (22) 左边。此处 $a,b$ 是同一个完整函数关系的常数，不能随 u 改变。

**必要性。** 若有 (22) 左边的 K，先用 (21) 取其权零投影，再作 (15)。由 $\lambda_+(K)=1$，H* 的系数恰为 1；由 $\mathcal N(K)=0$，得到
$$
n_2=-b n_4-c n_6,
$$
即所需关系。没有假定 $n_4,n_6$ 独立，也没有除以某个可能为零的 profile 值。

更一般地，线性泛函 $\lambda_+$ 能经过 $J_\infty$ 下降，当且仅当它杀掉 $\ker J_\infty$。因此 (22) 等价于
$$
\boxed{
\lambda_+\text{ 经 }J_\infty\text{ 下降}
\quad\Longleftrightarrow\quad
n_2\notin\operatorname{span}\{n_4,n_6\}.
}
\tag{25}
$$
若存在核中非零的 $\lambda_+$ 值，缩放该线性元素即能把它归一为 1，所以 (25) 没有遗漏另一种核值情形。

若 (25) 右边成立，下降的泛函在每条真实正时长、同端口 $M=\mathbf T=0$ 路径上仍满足原精确公式
$$
\overline\lambda_+(J_\infty(V_B))
=\lambda_+(V_B)
=L_B+\int_B(h_s/h)^2\,ds>0.
\tag{26}
$$
这将成为 whole E 与完整自然通量同时为零的一个严格实际障碍。

若 (23) 成立，则 (24) 正确阻止原 $\lambda_+$ 下降，但仍不自动证明增强实际锥满或有限截面存在。其他真权的增强正字符、真实 prototype 成本及联合商基准仍须独立支付。

本稿没有判定 (23) 或其否定；两个分支目前都作为准确待定条件保留。

## 6. 立即需要计算的原层，以及已完成结论的边界

三个 $n_i$ 都来自同一个原静态正常族 $F_0$，包括原 $N_0$、$\Gamma$ 和参考态归一。R333 的成员程序只读其 whole pure/self，不包含 (2) 的新收缩。R382 消去正常 H、R350 消去加速度平方、R393 求清 Q4 的九维自然像，都不能代替这三个静态函数。

另一方面，(18) 是只在零权得到的完整新归约。即使它最终为零，也不能据此令三个速度二次族 $\widehat Q_2$ 的全自然像为零。R398 已证明完整 $F_0$ 和完整 $\widehat Q_2$ 不能同时在全部状态、全部 u 上自然消去；那个存在性结论尚未给出这里的三个具体静态值。

因此本稿把一项真实联合条件从“需要知道整个新映射”准确缩到三个已固定原系数的完整自然函数依赖，同时保留其余低层。下一原式工作继续从 $v-\mathcal B_m(N_0+N_2)$ 提取 $F_0/\widehat Q_2$，保所有相同右锚和参考态项；不重新运行旧 pure/self 或原权零成员。

(24) 若存在也只是 U 中的真实线性元素，不是一条可自由取正负的实际路径。R392 已完成的响应 E 分量与两个固定自然读出联合截面、以及本稿的全函数权零判据，是不同且相容的结论。任何整体几何、Morse、固定 g、完整 period 或同一二阶修正的联合目标仍按其原实际接口处理。
