# R154：五族加速度商由二十个状态系数值的正仿射轨道生成

日期：2026-11-15。**已证明。** 纸面推导，只读取 R136 已发表原导出的状态键确认 k 次数；没有新 profile、原式、几何或数值运行。

[R146](R146-acceleration-family-quotient-covariance-and-eighty-seeds.md) 将五族的 314 个完整记录缩为 80 个 $\omega=0$ 系数。本文进一步给一个不同用途的有限生成结论：只取 $h=1,\omega=0,k=0,1,2,3$ 处五个状态系数函数的值，共 20 个向量，它们的**正仿射轨道的实线性 span**模 R 就生成全部五族。这里不称维数至多 20，不声称这些向量分别是单条实际路径成本，也不把正性条件改成四点检查。

依据 [R105](R105-finite-canonical-fourth-cost-space-and-response-quotient.md)、[R130](R130-true-fourth-span-from-horizontal-normal-coefficients.md)、[R136](R136-acceleration-coefficient-beyond-response-and-G-orbit.md)、[R145](R145-true-curvature-reflection-and-even-positive-characters.md) 及 R146。

## 1. 五族与正仿射协变

记

$$
U=\mathcal U_4,\qquad R=\mathcal R_8,\qquad Q=U/R,
$$

$$
\mathcal F=\{\bar A_{hh},\bar A_{hk},\bar A_{kk},H_1,H_2\},
\qquad(e_F)=(2,1,0,2,1).
$$

R130 保证各 $F(S)$ 都属于真实函数空间 U。它们是状态系数值，不因此自动是某一条实际路径的第四成本。

R146 对任意商泛函的完整证明给

$$
H^{e_F}[F(Hh,k,(\omega+d)/H)]
=\mathsf P_{H,d}[F(h,k,\omega)],\qquad H>0.
\tag{1}
$$

令

$$
g_F(k)=[F(1,k,0)]\in Q.
$$

将 (1) 应用于状态 $(1,k,0)$，取 $H=h,d=h\omega$，准确得到

$$
\boxed{[F(h,k,\omega)]
=h^{-e_F}\mathsf P_{h,h\omega}g_F(k).}
\tag{2}
$$

所以对任一仿射不变子空间 $R\subseteq Z\subseteq U$，五族全部状态值属于 Z，当且仅当全部 $F(1,k,0)$ 属于 Z。

R136 的完整原导出实际给五族的 k 次数均不超过六。因此 $g_F$ 是次数不超过六的 Q 值多项式。单用这件事，七个不同 k 值的准确插值已将问题缩为 35 个状态值的轨道。下面使用同右锚的真实反号，把所需正向取值进一步减为 20 个。

## 2. 五族在真实曲率反号下的准确商身份

R145 定义

$$
\mathsf S=\mathsf P_{-1,0}^{\mathrm{alg}},
$$

这是有限 Laurent 表示的代数取值，是真实函数空间上的 involution。它不是实际将 profile 镜像后改换右锚，也不要求物理 h 变负。

R145 的真实路径变换为

$$
S^\sharp=(h,-k,-\omega),\qquad
F_{\mathrm{frame}}^\sharp=E F_{\mathrm{frame}}E,
\qquad\alpha^\sharp=-E\alpha,
\qquad E=\operatorname{diag}(-1,1,1).
\tag{3}
$$

它保持真实水平约束，首末 frame I、零矩阵条件及常值 germs 按原规则变换，并有完整成本身份

$$
V_{B^\sharp}=\mathsf S V_B.
\tag{4}
$$

时间方向不变。若 $u=h_s,w=k_s,a=h_{ss},b=k_{ss}$，则

$$
(u,w,a,b)^\sharp=(u,-w,a,-b).
\tag{5}
$$

**引理。** 五族在 Q 中满足

$$
\boxed{[F(h,-k,-\omega)]=\eta_F\mathsf S[F(h,k,\omega)],}
\tag{6}
$$

其中

| F | $\bar A_{hh}$ | $\bar A_{hk}$ | $\bar A_{kk}$ | $H_1$ | $H_2$ |
|---|---:|---:|---:|---:|---:|
| $\eta_F$ | $+1$ | $-1$ | $+1$ | $-1$ | $+1$ |

**证明。** 任取 $\lambda\in Q^*$，延拓到包含完整局部密度 L 的系数及其 S 像的有限真实环境。考虑局部积分差

$$
J^\sharp(B)=\int_B\ell\bigl(L(S^\sharp;u,-w,a,-b,\ldots)
-\mathsf S L(S;u,w,a,b,\ldots)\bigr)\,ds.
\tag{7}
$$

因为 $\mathsf S R=R$，对同 germ、frame I、M=0 路径，R109 与 (4) 准确给 $J^\sharp(B)=0$。这里不把局部 L 的原式先假定为点态严格协变。

式 (7) 具有 R146 §§2–3 端点论证的全部性质：局部拼接可加，环境旋转不变，几何导数权仅 0、2、4，故同 k 真倒行同号。于是先用共同的真实 $(-M,A^{-1})$ 补偿证明端点纤维常值，再下降到 $SO(3)\times E_8$ 的连续同态，最后用真倒行及不同 germs 的零矩阵桥，得到固定矩乘子

$$
J^\sharp(B)=\beta(M_B)
\tag{8}
$$

对全部开平端路径成立。这个顺序支付了变化后的 frame 和矩阵，未把实际成本取负。

此后才改变真实时长。左侧含 $\delta J_0+\delta^{-1}J_2+\delta^{-3}J_4$，右侧仅含 $\beta(\delta M_0+\delta^{-1}M_2)$，所以最高导数层的差对所有开平端路径积分为零。

使用 R129 的准确正规式及零端边界势，再按 R130 的真实微幅路径依次分离加速度二次项和面积项。由 (5)，三种加速度单项式 $a^2,ab,b^2$ 的符号为 $+,-,+$。面积项则准确变成

$$
\bigl(H_1(S^\sharp)u-H_2(S^\sharp)w\bigr)
(-ub+wa),
$$

所以其 $u(ub-wa)$、$w(ub-wa)$ 两系数的符号分别为 $-,+$。任意 $\lambda\in Q^*$ 都杀相应差；各向量属于 U，有限维对偶分离即给 (6)。证明没有将 raw DAG 的非零响应差删除。证毕。

取 $h=1,\omega=0$，(6) 给

$$
\boxed{g_F(-k)=\eta_F\mathsf Sg_F(k).}
\tag{9}
$$

## 3. 正仿射不变的子空间自动保持 S

这里还须确认：使用 (9) 不会偷偷扩大到一种尚未允许的负物理缩放。

设 Z 是 U 中的正仿射不变实子空间。对任意 $z\in Z$，$\mathsf P_{H,0}z\in Z$ 对所有 $H>0$ 成立。R105 给这一 U 值函数是 H 的有限 Laurent 多项式。

若 $\lambda$ 杀 Z，则 $\lambda(\mathsf P_{H,0}z)=0$ 对全部正 H 成立。乘足够的 H 正幂后是普通多项式恒零，所以可在 $H=-1$ 取值，得到 $\lambda(\mathsf S z)=0$。任意湮灭子都如此，故 $\mathsf S z\in Z$；再用 $\mathsf S^2=I$ 得

$$
\boxed{\mathsf S Z=Z.}
\tag{10}
$$

更具体地，$\mathsf S z$ 本来就在 z 的**正缩放轨道的有限实线性 span**中：清 Laurent 负幂后，选有限个不同正 H，用多项式插值恢复全部系数，再在 $-1$ 代数取值即可。插值系数可为负，因此这不证明锥或实际半群中有负成本；它只说明本稿的线性生成不需要新增负 h 路径。

上述论证同样适用于 Q 中的轨道 span 和一般 pure 投影商。

## 4. 七点准确插值只需四个非负取值

置

$$
\mathcal I=\{-3,-2,-1,0,1,2,3\},\qquad
\ell_i(k)=\prod_{j\in\mathcal I\setminus\{i\}}\frac{k-j}{i-j}.
$$

每个 $g_F$ 为次数至多六的 Q 值多项式，故逐分量的准确 Lagrange 身份为

$$
g_F(k)=\sum_{i\in\mathcal I}\ell_i(k)g_F(i).
\tag{11}
$$

代入 (9)，得到

$$
\boxed{
g_F(k)=\ell_0(k)g_F(0)
+\sum_{i=1}^3
\bigl(\ell_i(k)\operatorname{id}
+\eta_F\ell_{-i}(k)\mathsf S\bigr)g_F(i).
}
\tag{12}
$$

这是函数商中的整 k 恒等式，不是采样误差估计。由 (10)，每一个负 k 值都属于对应正 k 值的正仿射轨道实 span。再用 (2)，全部 h、omega 状态也都被同一个有限生成问题覆盖。

令

$$
\mathcal A=R+\operatorname{span}_{\mathbb R}
\{F(h,k,\omega):F\in\mathcal F,\ h>0,\ k,\omega\in\mathbb R\}.
$$

**定理。**

$$
\boxed{
\mathcal A
=R+\operatorname{span}_{\mathbb R}
\{\mathsf P_{H,d}F(1,i,0):
F\in\mathcal F,\ i=0,1,2,3,\ H>0,\ d\in\mathbb R\}.
}
\tag{13}
$$

右侧只有 20 个初始状态系数值，但允许各自的正仿射轨道。

证明右侧包含左侧，直接由 (2)、(12) 及第 3 节。反向由 (1)：每个种子本来在左侧，且其每个正仿射像模 R 是另一个真实状态值乘一个实数，所以仍在左侧。R 的不变性支付所有商代表差。这也证明 $\mathcal A$ 本身正仿射不变。

## 5. 准确来源及成员问题缩减

唯一使用的原记录来源为

~~~text
notes/actions-43654534244-1-acceleration_layer_mixed/
acceleration-layer-mixed-original-expressions.json.gz
~~~

Run `43654534244`，source `1177f251dc3d9455adf88b585e4c0e4bd6f7e69b`；压缩 318634 B，SHA256 `b3227509c891a2e86e9bcc7823e3d6b3abb0a9ff80975b2e1162a0911739146e`；原始 1909429 B，SHA256 `7c1e0bda999d2c8958d7e5fdf6d9460f30eb6003eb1c69172ba1ca948dfeac38`。

只解析其 314 个 `family_records` 的 `state_key`。五族 k 的最大指数都为 6，且 $\omega=0$ 时各自出现的 k 指数集合为 $\{0,1,2,3,4,5,6\}$。这给 (11) 所需的原式次数上界。没有将 314 个 profile 原根重新展开、归约或评价。

因此，对任一正仿射不变的 $R\subseteq Z\subseteq U$，准确有

$$
\boxed{\mathcal A\subseteq Z
\iff F(1,i,0)\in Z\quad
\forall F\in\mathcal F,\ i=0,1,2,3.}
\tag{14}
$$

例如可取 $Z=R$ 或 $R+\operatorname{span}\operatorname{Orb}(G)$；这些等价式不是在宣称右侧已经成立。

一般 pure 投影 $\pi$ 与正仿射作用及 S 都交换。对 $\pi(U)/\pi(R)$ 应用相同论证，得到

$$
\boxed{
\pi(\mathcal A)=\pi(R)
\iff \pi F(1,i,0)\in\pi(R)
\quad\forall F\in\mathcal F,\ i=0,1,2,3.
}
\tag{15}
$$

式 (15) 不由 R151 的单 J 身份自动满足；一个状态值会同时包含多个独立 Laurent 系数及权。实际逐权处理仍可沿 R146 的 80 个起始系数进行，不必为了缩小“条目数”而将已分权的原问题重新混合。

## 6. 不应从生成数推出的结论

20 是所用初始向量数，轨道可以扩展到更多独立权和更多平移方向；本文没有给 $\dim\mathcal A\le20$，也没有证明 20 最小或这 20 个向量相互独立。

(11)–(12) 是有符号线性插值。对一个正泛函，有限几个 k 值的非负性不能因此推广为全部 k 非负；同样不能将加速度 PSD、R148/R152 的一维 action 门或完整正性问题改成四点或七点检查。R145 的真实反号和正缩放都合法，但本稿的实线性组合不是实际成本拼接规则。

本稿只处理三族加速度二次与两族面积系数。R130 的归一静态族、三个速度二次族和五个速度四次族仍有自己的完整项；特别 D0 的 $N^{[2]}$ 响应和完整 $\widehat Q_4$ 没有被这五族生成定理省去。

新 actual 仍应围绕已发现的具体未付原式推进。本稿不派发 20 个状态值或 80 个起始系数的盲扫描，不重复已证 J/G 的一般 pure 身份。完整周期、ruling、高阶与收敛、闭嵌入、全时 reach 以及宏观弯曲幅度仍须继续支付。
