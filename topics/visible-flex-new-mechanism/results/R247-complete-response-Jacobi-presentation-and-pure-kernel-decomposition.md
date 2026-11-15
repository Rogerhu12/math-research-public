# R247：完整响应的 Jacobi 呈示与全 pure 零响应分解

日期：2026-11-15。**已证明；新部分为完整纸面推导，继承已发表的原函数下界和原式覆盖。** 没有新的 profile 评价、原式编译、正规化、矩阵消元或研究计算。

本稿从 R244/R246 的单个十一维模转向全部真实响应。新结论是：完整 Jacobi 把 288 个形式响应压到 **232 维呈示**；与 R147 的真下界结合，$228\le\dim\mathcal R\le232$，结构关系之外的真实核至多四维。又给出整个 $\mathcal R\cap\ker\pi$ 的穷尽分解和一个明确的五十六维形式 pure 零子模块。

R87 已用原有理子式证明完整第三空间真维数 36，含 28 个独立交换子和 8 个独立额外类。本稿第 4 节给该事实的另一条纸面夹逼证明，**不是新求得的 rank**，也不重跑原独立性。新上界 232 仍不是实际维数；“余核至多四维”不表示完整 period 只有四个障碍，更不表示 $\dim(U/\mathcal R)\le4$。

来源：[R71](R71-third-holonomy-commutators-and-complete-fourth-P1.md)、[R80](R80-complete-third-affine-class-and-P1-endpoint-obstruction.md)、[R83](R83-true-fourth-transfer-and-zero-lower-history-variations.md)、[R87](R87-exact-complete-P1-separation-and-smooth-moment-circles.md)、[R105](R105-finite-canonical-fourth-cost-space-and-response-quotient.md)、[R147](R147-eighth-G-translation-and-237-query-control.md)、[R149](R149-ninth-G-membership-and-exact-nine-dimensional-orbit-quotient.md)、[R208](R208-every-universal-pure-response-has-a-second-jet-representative.md)、[R213](R213-two-mixed-sources-and-gauge-invariant-platform-obstructions-after-pure-closure.md)、[R217](R217-two-left-tail-invariants-independent-on-pure-zero-responses.md)、[R219](R219-eight-packet-fluxes-independent-on-pure-zero-responses.md)、[R244](R244-eleven-dimensional-response-module-pays-first-platform-and-eight-fluxes.md)、[R246](R246-complete-multiplatform-interface-and-unique-eleven-module-correction.md)。

## 1. 完整空间、槽与投影

全部 profiles 使用同一右 collar 锚，左尾保留。先在任意紧支撑光滑输入上作 universal 原函数身份；几何实现仍须按 R80/R105 先选有限真实控制族，再选共同物理区间。

令 $E=E_8$ 是八维真实二次算子空间，坐标顺序
$(p_0,p_1,p_2,r_0,r_1,s_0,s_1,t_1)$。完整第三算子保留外槽及对称内两槽。定义

$$
C(A,B)(a;b,c)=\Phi_A(a,\Phi_B(b,c))-\Phi_B(a,\Phi_A(b,c)),
$$

$$
W_{71}=\operatorname{span}\{C(A,B):A,B\in E\},\qquad
W=W_{71}+V_3+W_1.
\tag{1}
$$

$V_3,W_1$ 是 R77、R79 的完整实际可达空间，R80 已付全端点仿射类。记

$$
\Delta\tau(q)=\tau(q;q,q),\quad
Z=\ker(\Delta|_W),\quad Z_{71}=Z\cap W_{71}.
\tag{2}
$$

对 $F=f\odot f$、$D=F-\phi\odot\phi$，R83 的完整响应为

$$
\begin{aligned}
\mathcal B_A(\tau)(F,\phi)
={}&2\tau(\Phi_A D;D)-4\tau(\phi;\phi,\Phi_A D)\\
&+4\Phi_A(\phi,\tau(\phi;D)).
\end{aligned}
\tag{3}
$$

对称平方槽按线性延拓解释。令 $\mathcal R$ 为全部 (3) 的真实实线性跨度，并记

$$
\mathcal R_{71}=\mathcal B(E,W_{71}),\qquad
\mathcal R_{\mathrm p0}=\mathcal R\cap\ker\pi.
\tag{4}
$$

$\pi$ 是完整 canonical 的 pure $-4$ 模式投影；$\mathrm p0$ 表示**全权** pure 核，不是真权零响应块。R80(15) 给

$$
\pi\mathcal B_A(\tau)(q)=\frac18
\left\{D(\Delta\tau)(q)[\Phi_A(q,q)]
-2\Phi_A(q,\Delta\tau(q))\right\}.
\tag{5}
$$

所以 $\Delta\tau=0$ 使全部 $\pi\mathcal B_A(\tau)=0$。逆命题不成立：R215 的 $\mathcal B_P([P,R])$ 第三对角非零而 pure 响应零。只计算 Z 不能找全 $\mathcal R_{\mathrm p0}$。

## 2. 使用的已发表证据与三十六列来源

### 2.1 完整 W 覆盖和既有真独立性

run **43633746055**、source **26c3f2c0308d179a094d3967cfb7189db426081e** 的原 [full-phase-bridge-exact.json](../notes/actions-43633746055-1-full_phase_bridge_exact/full-phase-bridge-exact.json)，SHA-256 为
**7c2cb9fece518fb6fbb15b6b4e034565dfcc5a10cf0e103a7011cd56dc4ac960**。

其 pre_response_reduction 对全部 152 个完整第三模板保留原差核零，保留原索引

$$0,1,\ldots,27,\quad30,32,34,37,40,100,104,109.\tag{6}$$

前 28 列按上述 E 坐标顺序，对所有 $i<j$ 作字典序枚举，正是全部完整交换子。其余八列依 R87§3 的完整表为：

| 保留位置 | 原索引 | 原来源 | 对应状态 monomial |
|---:|---:|---|---|
| 28 | 30 | R77 area | $h^{-5}k$ |
| 29 | 32 | R77 area | $h^{-4}$ |
| 30 | 34 | R77 area | $h^{-4}k^2$ |
| 31 | 37 | R77 area | $h^{-3}k$ |
| 32 | 40 | R77 area | $h^{-2}$ |
| 33 | 100 | R79 h-shape | $h^{-2}k$ |
| 34 | 104 | R79 h-shape | $h^{-1}k^2$ |
| 35 | 109 | R79 h-shape | $k$ |

area 是完整局部式中乘在 $k_s h_{ss}-h_s k_{ss}$ 前的系数，h-shape 是 $\partial_h(h^2\partial_h R)$；所有槽保留为 $a;b,c$。记八个额外完整模板为 $\tau_j$，则原差给

$$W=W_{71}+\operatorname{span}\{\tau_1,\ldots,\tau_8\}.\tag{7}$$

v2 回执本身只授覆盖。随后 **R87** 的 run 43635287277、source f3102464c049e13cbf306b29cb31cd3d38eb5607，用同一完整两模式响应的原有理 $36\times36$ 子式，模 $2147483647$ 的非零值 $1164198643$，已证明这 36 个原模板真独立，故 $\dim W=36$。这里明确继承，不冒作本稿新实际。

### 2.2 同一个完整响应空间的 228 下界

R147 的原有理子式及前驱各真权块证明

$$\boxed{\dim\mathcal R\ge228.}\tag{8}$$

这是 (3) 对完整 E、W 的响应空间，不是仅对角第三空间，不是仅 $m_8$ 尾像，也不含额外 G 轨道、J 或 $D_0$ 商类。R147 把同一 pure 尾像 31 维与已在其核内的至少 197 维相加；各新增方向由原函数有理评价的非零子式支付。R149 明确保留这个下界，不把最后两列的非零正规形加到它上面。

R147 的 **237** 属于另含 G 商轨道的空间，不能替换 (8)。本稿不重跑旧评价、旧子式或旧消元。

## 3. 完整 Lie 身份与 232 维呈示

固定对称平方输入 F，把 $\phi$ 当作变量，令

$$
X_A(\phi)=\Phi_A(F-\phi^2),\qquad
Y_\tau(\phi)=\tau(\phi;F-\phi^2).
\tag{9}
$$

F 与右锚固定。括号约定为 $[X,Y]=DY[X]-DX[Y]$。完整槽导数是

$$
DX_A[v]=-2\Phi_A(\phi,v),\qquad
DY_\tau[v]=\tau(v;D)-2\tau(\phi;\phi,v).
\tag{10}
$$

逐项代入得

$$
\boxed{[X_A,X_B]=2Y_{C(A,B)},\qquad
\mathcal B_A(\tau)=2[X_A,Y_\tau].}
\tag{11}
$$

后一式包含 (3) 三项，特别保留最后的真实第三 history 响应。因此

$$
\mathcal B_A(C(B,C))=[X_A,[X_B,X_C]],
$$

$$
\boxed{\mathcal B_A(C(B,C))+
\mathcal B_B(C(C,A))+
\mathcal B_C(C(A,B))=0.}
\tag{12}
$$

这是完整 Jacobi 身份，取 $F=f^2$ 后仍是全部 canonical 相位原函数身份，不限 pure。

定义

$$
\iota:\Lambda^3E\longrightarrow E\otimes\Lambda^2E,
$$

$$
\iota(a\wedge b\wedge c)=
a\otimes(b\wedge c)+b\otimes(c\wedge a)+c\otimes(a\wedge b).
\tag{13}
$$

外楔映射与 $\iota$ 的复合是 $3\,\mathrm{id}$，故 $\iota$ 单射。这是形式空间事实，不需先用 W 的独立性。由 (12) 得满射

$$
\Theta_{71}:\mathfrak J:=
(E\otimes\Lambda^2E)/\iota(\Lambda^3E)
\longrightarrow\mathcal R_{71},
$$

$$\boxed{\dim\mathfrak J=8\binom82-\binom83=168.}\tag{14}$$

具体形式基可由全部 $e_i\otimes(e_j\wedge e_k)$、$j<k$，对每个 $i<j<k$ 删除 $e_k\otimes(e_i\wedge e_j)$ 得到。原替换是

$$
\mathcal B_{e_k}(C(e_i,e_j))
=\mathcal B_{e_j}(C(e_i,e_k))-\mathcal B_{e_i}(C(e_j,e_k)).
\tag{15}
$$

五十六个删列标签各自唯一，(13) 付其独立性。加 (7) 八个额外模板的八矩响应，得到

$$
\Theta:\mathfrak J\oplus(E\otimes\mathbb R^8)\longrightarrow\mathcal R,
\qquad\dim\operatorname{dom}\Theta=168+64=232.
$$

结合 (8)，

$$
\boxed{228\le\dim\mathcal R\le232,\qquad0\le\dim\ker\Theta\le4.}
\tag{16}
$$

这是新结构上界；没有跑新的 224/288 列矩阵。

## 4. 对既有 W36 的独立纸面再证明

此节不用 R87 子式，另由 (7)、(8)、(16) 重新推出已付结论，说明新结构没有循环依赖。

设 $q=\dim(W/W_{71})\le8$。双线性给满射
$E\otimes(W/W_{71})\to\mathcal R/\mathcal R_{71}$，故

$$228\le\dim\mathcal R\le168+8q.$$

若 $q\le7$，右端至多 224。因此 $q=8$，八个额外商类独立。

再假设 $C:\Lambda^2E\to W_{71}$ 有非零核元 k。则 (16) 的核包含

$$\{[a\otimes k]\oplus0:a\in E\}.\tag{17}$$

这些类确有八维。若 $a\ne0$ 且 $a\otimes k=\iota(\gamma)$，对任意 $\ell(a)=0$ 作外槽收缩，得
$\iota_\ell\gamma=0$。取 $a=e_1$，则所有 $e_i^*$、$i>1$ 的收缩为零；每个三重交替系数至少含一个这样的指标，故 $\gamma=0$。随之 $a\otimes k=0$，矛盾。于是

$$
(E\otimes\operatorname{span}\{k\})\cap\iota(\Lambda^3E)=\{0\}.
\tag{18}
$$

(17) 是八维真核，与 (16) 至多四维矛盾。故 C 单射，重新得到

$$\boxed{\dim W_{71}=28,\qquad\dim(W/W_{71})=8,\qquad\dim W=36.}\tag{19}$$

并得

$$
\boxed{164\le\dim\mathcal R_{71}\le168,\qquad
60\le\dim(\mathcal R/\mathcal R_{71})\le64.}
\tag{20}
$$

(18) 不声称一般秩一张量不在未知真实响应核；只排除一个完整第三函数关系所产生的**整八维**核。168、64、232 仍是上界，不提前授实际等号。

## 5. 全 pure 零响应的穷尽分解

R208 从已发表的全部 151 个对角第三列覆盖证明

$$\boxed{\Delta W=\Delta W_{71}.}\tag{21}$$

不把它升级为 $W=W_{71}$。对每个额外 $\tau_j$ 选
$\gamma_j\in W_{71}$，使 $\Delta\gamma_j=\Delta\tau_j$，令

$$\chi_j=\tau_j-\gamma_j.\tag{22}$$

这些完整原算子在 Z 内，其商类由 (19) 独立，因此

$$
\boxed{W=W_{71}\oplus\operatorname{span}\chi_j,\qquad
Z=Z_{71}\oplus\operatorname{span}\chi_j.}
\tag{23}
$$

更换 $\gamma_j$ 只给 $\chi_j$ 加一个 $Z_{71}$ 元素。由 (5) 所有 $\mathcal B_A(\chi_j)$ pure 零，故

$$
\boxed{\mathcal R_{\mathrm p0}
=(\mathcal R_{71}\cap\ker\pi)
+\operatorname{span}\{\mathcal B_{e_i}(\chi_j):1\le i,j\le8\}.}
\tag{24}
$$

反向包含证明：写 $V=V_{71}+V_\chi$，由 $\pi V_\chi=0$ 和 $\pi V=0$ 得 $\pi V_{71}=0$。两个响应像不预设直和。特别

$$\boxed{\pi\mathcal R=\pi\mathcal R_{71}.}\tag{25}$$

令 $\Pi_{71}=\pi\Theta_{71}$，完整有限核接口为

$$
\boxed{\mathcal R_{\mathrm p0}
=\Theta_{71}(\ker\Pi_{71})+
\mathcal B(E,\operatorname{span}\chi_j).}
\tag{26}
$$

因此可以先在 168 维形式商上求完整 pure 核，再加八个第三对角核代表的六十四个响应。不能漏掉第一项：第四 pure 核不等于第三对角核产生的响应。

R208 的旧代表覆盖只授 $\dim\Delta W_{71}\le18$，与 (19) 给

$$\boxed{\dim Z_{71}\ge10,\qquad\dim Z\ge18.}\tag{27}$$

不宣称对角真维数恰18。已知七维 hook 串外至少还有三个独立第三对角核方向；其第四像和固定圆商像另判。

## 6. 交换子部分的完整 sl2 结构

对 n 线性 A，记
$\mathscr L_XA=X_{\rm out}A-\sum_\nu A(\ldots,X_{\rm in,\nu},\ldots)$，并令

$$
N=\mathscr L_{\partial_x},\quad H=\mathscr L_{x\partial_x-1},\quad
\delta=\mathscr L_{x^2\partial_x-2x}.
$$

R217/R219 同锚导子满足

$$[N,\delta]=2H,\qquad[H,\delta]=\delta,\qquad[H,N]=-N.\tag{28}$$

$\delta$ 不是已允许的真实几何非仿射变换。记 $V_m$ 为最低 H 权 $-m/2$、维数 $m+1$ 的有限不可约串。取正右积分 J，并记

$$
P(a,b)=J(a''b''),\quad R(a,b)=a'b'+xJ(a''b''),\quad
S(a,b)=J(\eta a''b''),\quad Q=R-S.
$$

原表给

$$
NP=0,\ HP=-2P,\ \delta^5P=0;\qquad
NQ=0,\ HQ=-Q,\ \delta^3Q=0.
\tag{29}
$$

后一链可逐项写成
$\delta Q=4\Phi_{p_0}$、
$\delta^2Q=-8\Phi_{p_1}-2\Phi_{t_1}$、
$\delta^3Q=0$。
P 非零；Q 非零可由
$Q(a,b)''=a'''b'+a'b'''+a''b''$
及合法内部 jets $a'=b'=0,a''=b''=1$ 看出。

若 $Nv=0,Hv=-mv/2$，则

$$N\delta^nv=n(n-m-1)\delta^{n-1}v.\tag{30}$$

(29) 两串各自独立，交零且合计八维，故

$$\boxed{E\simeq V_4\oplus V_2.}\tag{31}$$

对 n 线性算子，H 权等于真仿射权加 $n-1$；例如 P 真权 $-3$ 对应 H 权 $-2$。不混淆表示标签与真权字符。

由 (19)，$\Lambda^2E\to W_{71}$ 是真实等变同构，因此

$$
\boxed{W_{71}\simeq2V_6\oplus V_4\oplus3V_2.}
\tag{32}
$$

这是
$\Lambda^2V_4=V_6\oplus V_2$、
$V_4\otimes V_2=V_6\oplus V_4\oplus V_2$、
$\Lambda^2V_2=V_2$
的有限串分解，维数 $14+5+9=28$；可用 (28) 的最低权串和权重计数核对，无新 profile 值。

(3) 满足组合 Leibniz，所以 $\mathcal R_{71}$ 及其 pure 核在三导子下不变，$\Theta_{71}$ 等变。**没有证明整个 W 或八个 $\chi_j$ 在 $\delta$ 下闭合**；不把全 $\mathcal R$ 擅自授为这个非仿射作用的模。

## 7. 七维 hook 与五十六维形式 pure 零子模块

R81/R180 的完整非零 hook 为

$$\mathfrak H=C(P,S)-3C(P,R),\qquad\Delta\mathfrak H=0.\tag{33}$$

非零有原式证据：w 在 f 支撑附近仿射、$w'=C$ 时，
$\mathfrak H(w;f,f)=-3C(f'')^2$。又 $NR=NS=P$，故
$N\mathfrak H=0,H\mathfrak H=-3\mathfrak H$。两个 E 槽均有 $\delta^5=0$，给 $\delta^9\mathfrak H=0$；用 (30) 依次降到 $\delta^7\mathfrak H=0$，并证明前七项独立。所以

$$
\mathfrak H_7=\operatorname{span}\{\mathfrak H,\delta\mathfrak H,\ldots,
\delta^6\mathfrak H\}\simeq V_6\subset Z_{71}.
\tag{34}
$$

所有 $\mathcal B_A(\delta^j\mathfrak H)$ pure 零，是等变映射
$(V_4\oplus V_2)\otimes V_6\to\mathcal R_{\mathrm p0}$ 的像。形式定义域为

$$
\boxed{V_{10}\oplus2V_8\oplus2V_6\oplus2V_4\oplus V_2,}
\tag{35}
$$

维数 $11+18+14+10+3=56$。实际像可能有核、同型串之间也可能相依，不能报实际秩56。

具体原式生成接口：对最低权串归一为
$Nv_i=i v_{i-1}$、$Nw_j=jw_{j-1}$。在 $V_m\otimes V_n$ 中，

$$
z_k=\sum_{i=0}^k(-1)^i\binom ki\,v_i\otimes w_{k-i},
\qquad0\le k\le\min(m,n)
\tag{36}
$$

被 N 杀掉，最低权 $-(m+n-2k)/2$；各 $\delta$ 串生成
$V_{m+n-2k}$。$Nz_k=0$ 由
$(i+1)\binom{k}{i+1}=(k-i)\binom{k}{i}$
逐项相消。取 $(m,n)=(4,6),(2,6)$ 即 (35)。不靠函数采样辨认这些形式串。

## 8. 固定圆商不能忽略原 gauge 像

对 R183/R225 的合法八包圆与闭 hook，R213 已证明

$$
\boxed{\mathcal B_A(\mathfrak H)(F,\phi_\theta)
=2L_f(\Phi_A D_\theta).}
\tag{37}
$$

$\Phi_A D_\theta$ 是真实合法二阶 gauge：三矩支付每个基本包左尾，八包七阶有限差分支付六个交叉矩。因此上述五十六列表中 $j=0$ 的八个方向在固定圆完整 period 商内全零，尽管 universal 响应可非零。

对 $j>0$，不能对 (37) 施 $\delta$ 后仍当作同一个固定 $L_f$ 的像；$\delta$ 也作用 f、g、目标槽及所有输入。固定圆并没有保持不动。

令 R225 的完整观测为

$$
O:U_{\mathrm p0}\to
\frac{\text{两个真实输出函数}}{\text{全部合法 }L_f\text{ 的像}}.
$$

剩余问题仍是

$$\boxed{O(U_{\mathrm p0})/O(\mathcal R_{\mathrm p0}).}\tag{38}$$

不宣称它是 sl2 商模、像满或已有非零字符读出。R246 的十三条兼容只描述原十一维 $\mathcal M$ 的像，不能扩成全响应的障碍。

属于 $\mathcal R$ 是真实控制词成本差中的线性方向；R102/R121 的有限实现保全部基准，不等于可任意取负的零基准实际成本。固定圆 profile gauge (37) 的准确有符号作用另有已付原因，两者不混同。

## 9. 下一最小原式消费规格

这是尚未执行的新接口，不把抽象 $\gamma_j$ 当作已存数值。

### 9.1 直接消费现存完整 W

已有 [W-only 原根导出](../notes/actions-43645177423-1-local_fourth_quotient/local-fourth-quotient-W-original-expressions.json.gz)，来自 run **43645177423**、source **2f1b809c0b0abb7a26303d36940edc203815f872**：

| 对象 | 大小 | SHA-256 |
|---|---:|---|
| gzip | 7377 B | 45cbdc8f38a4b5561924badaf9cd68a93a7fa71c6264d95489034703af4ee44a |
| 原文 | 31750 B | 615d848611aaf787bc3ae790b4b1f81fe91338301bcb57afdfd111758cf533bf |
| main | 3982 B | 19228a0aecf40416cf7ba7b8a7fa4e0180ed924a4bd04435b0e6e6e4a0b1b28a |

schema 为 visible-flex-R109-local-fourth-quotient-static-v1-original-expressions，content_scope 为 W-only。W0 至 W35 共36根、170原atom、逐根SHA及152原身份绑定均完整。main 的 output_limit 指大摘要，不是 W 失败。

复用 literature_local_fourth_quotient.decode_expressions。不得重编全 local forcing、152 原第三模板或3974第四因子。

### 9.2 首个必要新目标：八个同对角提取

R208 的151列付 (21)，但现存 closed-C1-endpoint-relations.json 主要是151标签、端点关系及旧pure P1坐标，companion expressions只有五个目标根；不能声称已有八个 (22) 坐标。

最小 consumer 只求八个 $\Delta\tau_j$ 对以下旧18交换子对角生成元的准确关系：

$$0,1,2,3,4,5,6,7,8,9,10,11,12,14,18,20,21,24.\tag{39}$$

能直接读的真代表直接消费；确缺可调用代表时，仅将 (39) 必要18个三次原根转入新共享词表作输入恢复。八目标是新工作。不恢复/重跑旧151列、旧P1目标、旧完整pure第四基或有理评价。

输出每个 $\gamma_j$ 的原28坐标及独立原差
$\Delta(\tau_j-\gamma_j)\equiv0$ 证明。完整 $\chi_j$ 保外/内颜色，不把对角零写成完整零。R87已付其商独立，无需再测。建议单入口120秒/512MiB，仅新增小人工查槽、锚、坐标和来源；实际只公开Actions。

### 9.3 真 pure 核与固定圆商分开

(26) 需要 $\Pi_{71}$ 的完整核。先将 R201/R204/R207/R210 等已付真权pure原根、坐标和转换身份接到 (15) 的标签，列清尚缺输入后只补必要原根/关系。不把R116的 $m_8$ 尾像冒充完整 $\pi$，不由偶权已付而删其余实际列。此步可只处理pure，不重全部mixed；部分完成不得报告全核。

应用 (38) 必须实际固定 R225 解析圆，或保真实tail耦合给universal参数身份。$\psi P$ 的存在性不替未选择的P系数赋值；右尾不能独立赋值。最终目标须同时含R225平台、总通量、内部退化和两平端延拓，并由同一响应组合检验。R244/R246有限读出只是子映射，真正满像或严格annihilator才决定完整period。

根README第15条继续适用：机器数据只Actions内存/临时输出；仓库保脚本、参数、run、SHA和人类结论，不存新可重算证书。

## 10. 范围

新完整Jacobi/232上界和 (26) 全pure零接口，给出超出原十一维模的真实来源；W36独立是对R87既有结论的另一纸证。仍未付 (38)、同一w的第四ruling、实际成本联合组装、更高阶收敛及主课题同一度量有限嵌入族。
