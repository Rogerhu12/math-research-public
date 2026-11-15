# R146：五族加速度系数模真实响应的完整协变与八十个起始条目

日期：2026-11-15。**已证明。** 纸面证明；只解析 R136 已发表完整导出的状态键以统计条目，没有重新计算 profile、幂尾、响应或几何。

本稿把 [R141](R141-affine-character-acceleration-covariance-and-J-positivity.md) 的字符后协变提升为完整有限函数商上的恒等式。对三族加速度二次系数和两族面积系数，任意 $\omega$ 系数都由 $\omega=0$ 系数的真实仿射平移生成，等式成立于 $U/R$。R136 的 314 个完整状态条目因此缩减为 80 个起始条目的成员问题。80 是原记录数，不是独立维数，也不是已可自由取正负的控制数。

依据 [R89](R89-affine-covariance-and-positive-multiple-pair-P1.md)、[R105](R105-finite-canonical-fourth-cost-space-and-response-quotient.md)、[R109](R109-local-density-of-the-complete-fourth-quotient.md)、[R112](R112-local-fourth-geometric-derivative-weights.md)、[R129](R129-horizontal-geometry-IBP-for-complete-fourth-costs.md)、[R130](R130-true-fourth-span-from-horizontal-normal-coefficients.md)、[R134](R134-acceleration-layer-from-complete-local-v4.md) 和 [R136](R136-acceleration-coefficient-beyond-response-and-G-orbit.md)。

## 1. 空间、真实状态与结论

记真实完整第四成本空间及响应子空间为

$$
U=\mathcal U_4,\qquad R=\mathcal R_8,\qquad Q=U/R.
$$

R105 已证明它们有限维，$R\subseteq U$，且完整正仿射作用 $\mathsf P_{H,d}$ 保持 U 和 R。因此该作用准确下降到 Q。这里 U、R 都是真实函数空间，不是不完备 normal form 的标签空间。

真实状态与水平约束为

$$
S=(h,k,\omega),\quad h>0,\qquad
u=h_s,\quad w=k_s,\quad a=h_{ss},\quad b=k_{ss},\qquad
\omega_s=\frac{w}{2h}.
\tag{1}
$$

R129 的完整第四导数层有准确正规式

$$
\begin{aligned}
L_4={}&D_sP_3+
\bar A_{hh}(S)a^2+\bar A_{hk}(S)ab+\bar A_{kk}(S)b^2\\
&+\bigl(H_1(S)u+H_2(S)w\bigr)(ub-wa)
+\widehat Q_4(S;u,w).
\end{aligned}
\tag{2}
$$

其中 $\widehat Q_4$ 对速度齐次四次，$P_3$ 是明确的正导数权三边界势。R130 证明以下五个状态函数的每个值都属于 U：

$$
F\in\{\bar A_{hh},\bar A_{hk},\bar A_{kk},H_1,H_2\}.
$$

设相应的几何缩放指数为

| 族 F | $\bar A_{hh}$ | $\bar A_{hk}$ | $\bar A_{kk}$ | $H_1$ | $H_2$ |
|---|---:|---:|---:|---:|---:|
| $e_F$ | 2 | 1 | 0 | 2 | 1 |

**定理 1。** 对任意 $H>0,d\in\mathbb R$、任意真实状态 S，令

$$
S_{H,d}=(Hh,k,(\omega+d)/H).
$$

则有完整商恒等式

$$
\boxed{
H^{e_F}[F(S_{H,d})]
=\mathsf P_{H,d}[F(S)]\quad\text{于 }Q.
}
\tag{3}
$$

特别，(3) 不是仅对正泛函、单权泛函或平移不变泛函才成立。其差确实属于 R。但本稿不把这个差直接置为零，不声称原始 DAG 在未加响应校正时逐点相同。

## 2. 任意商泛函的准确局部积分差

固定 H,d，任取 $\lambda\in Q^*$，也把它视为 U 上杀 R 的实泛函。取一个有限真实函数环境 E，包含 U、局部密度 L 的全部 profile 系数以及它们经过这一个固定 $\mathsf P_{H,d}$ 后的像。原环境有限且该作用线性，所以这样的 E 有限。将 $\lambda$ 任意线性延拓为 $\ell\in E^*$。

不要求延拓本身为字符，也不要求它杀掉 U 以外的所有局部系数。延拓只用于定义下列真实局部积分：

$$
\begin{aligned}
J_{H,d}(B)=\int_B\{&\ell(L(S_{H,d};Hu,w,Ha,b,\ldots))\\
&-\ell(\mathsf P_{H,d}L(S;u,w,a,b,\ldots))\}\,ds.
\end{aligned}
\tag{4}
$$

这里 $L=L_0+L_2+L_4=v-\mathcal B_mN$ 是 R109 的完整局部密度，$m=m_0+m_2$。所有真实 $s$ 导数、累计历史消去产生的局部势及其端项按原式保留；不是把完整非零矩阵路径成本误当可加量。

式 (4) 对平端路径拼接可加，对固定环境旋转不变。同 k 真倒行使每个 j 阶几何导数乘 $(-1)^j$；L 只有偶的导数权 0、2、4，因此 (4) 的局部积分倒行同号。仿射作用只改 profile 变量，不破坏这些性质。

若 B 是同 scalar germ、frame $I\to I$、$M_B=0$ 的真实路径，其第三算子可以非零。R105 仍给 $V_B\in U$。R89 的整路径变换使 $B_{H,d}$ 也具有这些零矩阵及 frame 条件，并有

$$
V_{B_{H,d}}=\mathsf P_{H,d}V_B.
$$

R109 在整条 $M=0$ 路径上给 $\int L-V_B\in R$；再用 $\mathsf P_{H,d}R=R$，得到

$$
J_{H,d}(B)
=\lambda(V_{B_{H,d}})-\lambda(\mathsf P_{H,d}V_B)=0.
\tag{5}
$$

该等式只用了 $\lambda(R)=0$。第二项没有被未经证明地改成某个 $H^\sigma\lambda(V_B)$。

## 3. 先支付全部端口，再分离最高时长权

R130 §§4–6 的端点纤维论证适用于 (4)。其所需输入正是局部可加性、环境旋转不变、同 k 倒行同号及 (5)。为说明这里没有偷删矩阵项，逐项给出作用。

固定 scalar germ g。若两条 scalar 闭路径有相同末 frame A、相同矩阵 M，R70 给一条真实同 germ 补偿路径，目标为 $A^{-1},-M$。将同一补偿分别接上，所得两字均满足 (5)。局部可加性迫它们原来的 J 值相等。这只是比较两个真实正时长路径的积分，不把任何第四成本取成实际逆元。

故 J 下降为 $SO(3)\times E_8$ 上的函数。拼接和 R70 的局部光滑端点截面使它成为连续加法同态。$SO(3)$ 紧，其到实数加法群的连续同态为零；E8 上只剩一个线性函数。

对任意开 scalar 平端路径 B，接其同 k 真倒行 $B^R$。实际末 frame 为 $ADA^TD$，通常不为 I；但前一步已经处理全部 frame，且矩阵与局部 J 均倒行同号，故可除以二得到开路径公式。再用 R70 的真实零矩阵开桥比较 germs，乘子对全部起止 germs 相同。因此存在固定 $\beta_{H,d,\ell}\in E_8^*$，使

$$
\boxed{J_{H,d}(B)=\beta_{H,d,\ell}(M_B)}
\tag{6}
$$

对所有真实开平端路径成立。

现在才把任意固定 scalar 轨迹的真实时长缩放为 $\delta>0$。水平约束 (1) 仍准确成立；frame 和矩阵一般会改变，但这些新端口已在 (6) 的范围内。R112 给

$$
\delta J_0+\delta^{-1}J_2+\delta^{-3}J_4
=\beta_{H,d,\ell}(\delta M_0+\delta^{-1}M_2).
\tag{7}
$$

对全部 $\delta>0$ 比较不同幂，得到

$$
\boxed{J_4(B)=0\quad\text{对全部真实开平端 B}.}
\tag{8}
$$

原八矩项最高只有导数权二，所以它不进入这个最高层恒等式。这里既没有假定时长缩放保 M、frame，也没有提前丢掉完整矩阵乘子。

## 4. 正规系数的分离与完整商等式

R129 的 $P_3$ 在任一常值 germ 上分别为零。仿射变换使 $(u,w,a,b)\mapsto(Hu,w,Ha,b)$，仍保该零端势；$\mathsf P_{H,d}$ 作用于 profile 系数并与真实 $D_s$ 交换。因此在 (8) 中使用 (2) 后，所得积分仍为零，其三种加速度二次系数依次为

$$
\ell\bigl(H^2\bar A_{hh}(S_{H,d})-\mathsf P_{H,d}\bar A_{hh}(S)\bigr),
$$

$$
\ell\bigl(H\bar A_{hk}(S_{H,d})-\mathsf P_{H,d}\bar A_{hk}(S)\bigr),
$$

$$
\ell\bigl(\bar A_{kk}(S_{H,d})-\mathsf P_{H,d}\bar A_{kk}(S)\bigr).
\tag{9}
$$

面积部分的缩放必须逐项计算：

$$
\bigl(H_1(S_{H,d})Hu+H_2(S_{H,d})w\bigr)
\,H(ub-wa).
$$

故其两个系数恰为

$$
\ell\bigl(H^2H_1(S_{H,d})-\mathsf P_{H,d}H_1(S)\bigr),\qquad
\ell\bigl(HH_2(S_{H,d})-\mathsf P_{H,d}H_2(S)\bigr).
\tag{10}
$$

剩余项仍是速度四次式。没有把全部速度—加速度项冒充总导数。

在任意状态 $S_*$ 取真实微幅路径

$$
u_\varepsilon=\varepsilon U_0,\quad
w_\varepsilon=\varepsilon W_0,\quad
\omega_\varepsilon=\omega_*+
\int\frac{\varepsilon W_0}{2h_\varepsilon}.
$$

两端为开常值 germs，$h_\varepsilon>0$，状态为 $S_*+O(\varepsilon)$。按 R130 §8，先除 $\varepsilon^2$ 取同向速度，迫 (9) 在任意状态全部为零。于是这些标量系数处处恒零，其状态变化不污染下一阶。

再除 $\varepsilon^3$，取非负、非零、偶的紧支撑函数 $\psi$ 及 $(U_0,W_0)=(\psi,\psi')$。准确分部积分给

$$
\int U_0(U_0W_0'-W_0U_0')=-3\int\psi(\psi')^2\ne0,
\qquad
\int W_0(U_0W_0'-W_0U_0')=0.
$$

交换两个速度后分离另一项，故 (10) 也在每个状态为零。全程均是真实水平路径；没有独立指定不相容的 $\omega$ 历史或末端数据。

由 R130，各 $F(S)$ 属于 U；由 R105，$\mathsf P_{H,d}F(S)$ 也属于 U。因此 (9)–(10) 只依赖延拓 $\ell$ 在 U 上的原泛函 $\lambda$。任意 $\lambda\in(U/R)^*$ 都杀相应差，有限维对偶分离遂给该差属于 R。这证明 (3)。

本证明继承 R105 的 universal 函数约定。每次实际端口补偿只涉及有限条路径和紧小族，可先选它们，再取共同正物理区间。没有要求所有状态同时适合某个任意预给的窄区间。

## 5. 全部 omega 系数由 omega 零值生成

令 N 为真实平移表示的生成元：

$$
\mathsf P_{1,d}=\exp(dN).
$$

R105 保证这个表示对 d 为有限多项式，所以 N 在 U 及 Q 上均幂零。取 (3) 中 $H=1$，得到

$$
\boxed{[F(h,k,\omega+d)]=e^{dN}[F(h,k,\omega)].}
\tag{11}
$$

每个完整状态函数可按有限 Laurent/log 单项式写为

$$
F(h,k,\omega)=
\sum_{a,b,j,\ell}h^ak^b\omega^j(\log h)^\ell F_{a,b,j,\ell}.
\tag{12}
$$

R130 已证明这些真实系数属于 U，且其 span 等于状态值的 span。有限函数 $h^a(\log h)^\ell k^b$ 在 $h>0$ 的状态域上独立；这是比较真实函数系数，不是假设原 profile 模板独立。

将 (11) 的 $\omega=0$ 代入，比较 d 和上述状态单项式，得

$$
\boxed{
[F_{a,b,j,\ell}]=\frac{1}{j!}N^j[F_{a,b,0,\ell}].
}
\tag{13}
$$

等价地，$N[F_{a,b,j,\ell}]=(j+1)[F_{a,b,j+1,\ell}]$，超过原有限支撑后右边为零。若某个起始条目本来缺失，其向量就是零，所有后继条目均在 R 中。

这里的“生成”在 Q 中成立；一般原表达式仍可相差一个非零响应。若需要给指定原 DAG 的显式响应表示，仍须恢复相应响应系数并证明原差，不能用 (13) 静默删掉它。

## 6. 已发表五族的准确条目缩减与逐权位置

只读取 R136 已发表完整导出中的 `family_records` 和 `state_key` 元数据：

~~~text
notes/actions-43654534244-1-acceleration_layer_mixed/
acceleration-layer-mixed-original-expressions.json.gz
~~~

Run `43654534244`，source `1177f251dc3d9455adf88b585e4c0e4bd6f7e69b`。压缩 318634 B，SHA256 `b3227509c891a2e86e9bcc7823e3d6b3abb0a9ff80975b2e1162a0911739146e`；原始 1909429 B，SHA256 `7c1e0bda999d2c8958d7e5fdf6d9460f30eb6003eb1c69172ba1ca948dfeac38`。主报告 SHA256 为 `baccbf48f39a7fb3296ca4e8a933d18f246a8db317423846e66d9c46374b2745`。

这份导出保存五族的全部 314 个状态记录及两个完整相位模式。所有记录的 $\log h$ 指数实际为零；这里没有通过假设删去 log 项。每族的 $\omega=0$ 条目数如下。

| 族 | 全部记录 | $\omega=0$ 起始记录 | 起始类的可能协变权及记录数 |
|---|---:|---:|---|
| $\bar A_{hh}$ | 82 | 16 | $0:1,-1:1,-2:2,-3:2,-4:3,-5:3,-6:4$ |
| $\bar A_{hk}$ | 66 | 16 | $-1:1,-2:1,-3:2,-4:2,-5:3,-6:3,-7:4$ |
| $\bar A_{kk}$ | 50 | 16 | $-2:1,-3:1,-4:2,-5:2,-6:3,-7:3,-8:4$ |
| $H_1$ | 66 | 16 | $-1:1,-2:1,-3:2,-4:2,-5:3,-6:3,-7:4$ |
| $H_2$ | 50 | 16 | $-2:1,-3:1,-4:2,-5:2,-6:3,-7:3,-8:4$ |
| 合计 | 314 | 80 | 不表示这些类独立或非零 |

三族 A 的共同起始 $(a,b)$ 键集为

$$
\begin{aligned}
\mathcal K={}&\{(-8,0),(-8,2),(-8,4),(-8,6),\\
&(-7,1),(-7,3),(-7,5),\\
&(-6,0),(-6,2),(-6,4),\\
&(-5,1),(-5,3),(-4,0),(-4,2),(-3,1),(-2,0)\}.
\end{aligned}
\tag{14}
$$

两个 H 族的键集均为 $\{(a-1,b):(a,b)\in\mathcal K\}$。列数差别来自各起始条目的有限 $\omega$ 后继长度，不代表每族有同一真实商维数。

因为当前实际展开没有 log 项，将 (3) 取 $d=0$ 并比较状态单项式，得到每个系数类的准确缩放：

$$
\boxed{
\mathsf P_{H,0}[F_{a,b,j,0}]
=H^{a+e_F-j}[F_{a,b,j,0}].
}
\tag{15}
$$

所以起始类若非零，其权为 $a+e_F$；每次 N 输运降低一权。这给出表中逐权位置，但不声称原 DAG 中不含模 R 消失的其他权分量。

将五族起始记录合计，名义权 $0,-1,\ldots,-8$ 的记录数分别为

$$
1,\ 3,\ 6,\ 8,\ 11,\ 13,\ 16,\ 14,\ 8.
\tag{16}
$$

这些数只从已发表元数据和 (15) 得到，没有新的研究符号计算。

## 7. 对完整商和一般 pure 成员门的准确推论

设 Z 是任一仿射不变子空间，满足 $R\subseteq Z\subseteq U$。例如

$$
Z=R+\operatorname{span}\operatorname{Orb}(G).
$$

由 (13) 和 $NZ\subseteq Z$，以下条件等价：

1. 五个完整状态函数的全部值属于 Z；
2. 它们的全部状态系数属于 Z；
3. 它们的 80 个 $\omega=0$ 起始系数属于 Z。

第一、二项的等价使用 R130 的真实有限状态函数独立性；第三项到第二项则使用 (13)，不是逐条盲测 314 个系数。

对一般 pure 投影 $\pi V=V_{-4}$，仿射作用不混合相位模式，故 $\pi\mathsf P=\mathsf P\pi$。于是诱导映射

$$
\bar\pi:U/R\longrightarrow\pi(U)/\pi(R)
$$

也是仿射等变的。相同论证给

$$
\boxed{
\text{五族全部一般 pure 系数在 }\pi(R)
\iff
\text{这 80 个起始系数的 pure 像在 }\pi(R).
}
\tag{17}
$$

式 (17) 是问题缩减，不是成员结论。R133 的单 $m=8$ 投影和 R138 的整个 G 轨道 pure 恒等式，都不能替代这里剩余的起始条目。R136 的新 J 正是 $\bar A_{hh}$ 的 $(a,b,j)=(-4,0,0)$ 起始系数；它的完整商非零并未被本定理消除。对该 J 的固定六列一般 pure 候选，R143 实际只得到非零 sound 代表，成员状态仍未决。

本稿也不把五族等同于 R130 的全部十四族：归一静态族、三个速度二次系数与五个速度四次系数仍有各自原式和矩阵项。特别是完整 $N^{[2]}$ 对 $\widehat Q_2,\widehat Q_4$ 的贡献没有被省略。

## 8. 字符推论及实现范围

若额外给定 $\lambda(R)=0$、$N^*\lambda=0$，则 (13) 使全部正 $\omega$ 次系数在 $\lambda$ 后消失。若再有 $\lambda\circ\mathsf P_{H,0}=H^\sigma\lambda$，则 (15) 使只有 $a+e_F=\sigma$ 的起始条目可能保留。这重得 R141 的字符结构，但没有对一般商类附加这些额外假设。

所有 (3)、(13)、(15)、(17) 都是完整真实函数商上的恒等式，可以用于避免重复计算后继条目。它们没有自动提供某条原式的显式响应系数、真实成本负值、实际有符号控制或新闭锥 lineality。若需要这些结论，仍要付清各自的原式表示或真实有限路径成本。

完整 mixed 周期、逐 s ruling、高阶与收敛、闭嵌入和全时 reach 以及宏观弯曲幅度仍未由本稿支付。下一实际只继续 J 的单目标一般 pure 成员门，复用已发表的完整真权 $-2$ 响应原根；不因条目缩减而盲扫全部 80 个起始条目。
