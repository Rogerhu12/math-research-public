# R234：原完整环类迹的两种 admissible 观测与 definite 群环比较

日期：2026-11-13。**状态：已证明的原对象比较；未证明跨素数的低阶系数非零。**

本篇保持 R150、R153、R156、R230、R232 的同一曲线、原域表、
原辅助素数、完整环类迹及整格。所引外部输入是已发表的
Ribet--Diamond--Taylor 升层和 Zhang（2014）§4.2 的局部比较。
下文逐一核验它们在原对象上的条件，不把新的观测素数冒充
原 Kolyvagin 节点。

## 1. 固定对象和结论

固定
$$
 E:y^2+y=x^3+x^2-2x,\qquad N_E=\Delta_E=389.
$$
取 R153 原十六域之一 $F=\mathbb Q(\sqrt D)$，以及 R156 的合法输入
$(p,\ell,L,Q)$。特别 $p\ge7$ 普通，$p\nmid389D$，剩余像及
$p$ 进像满足原满像条件，
$$
 \ell\text{ 在 }F\text{ 惰性},\quad
 \ell+1=pu,\quad p\nmid u a_\ell,\quad
 H=F[\ell],\quad [L:F]=p,
$$
$$
 Q=[t_0]\operatorname{Tr}_{H/L}P[\ell]\ne O,\qquad
 N_{L/F}Q=0.
\tag{1}
$$
所有 Hilbert 类群标签均在 (1) 内。沿用 R230 的固定有限例外，
使负扭曲秩一且负号 $p$ 初级 Sha 为零。

沿用 R232 的记号
$$
 \Gamma=\langle\tau\rangle,\quad
 \mathcal O=\mathbb Z_p[\zeta_p],\quad
 \delta=\tau^{(p-1)/2}(\tau-1),\quad
 \Delta=\delta^2=\tau+\tau^{-1}-2,
$$
$$
 B=E(L)\otimes\mathbb Z_p,\quad B_0=E(F)\otimes\mathbb Z_p,\quad
 A_0=\ker(N:B\to B_0)=\mathcal O w,\quad Q=\delta^a e w.
\tag{2}
$$
其中 $e$ 是 $\mathcal O$ 单位。将原点乘一个 $\tau$ 幂，
可令 $cQ=-Q$；这只循环平移完成标签，不改变下述低阶非零性。

固定非挠点 $P_+\in E(\mathbb Q)$ 和
$P_-\in E(F)^-$。对 $P_+$ 删除它在其饱和秩一子格中的固定
指数的素因子；对 $P_-$ 删除其在整个负秩一格中的固定指数的
素因子。于是两者的 $p$-Kummer 类均非零，且 $P_-$ 生成 $B_0^-$。
例如 $P_+$ 可取 R2 中已证明非挠的原点之一。
这些都是固定有限例外，不是关于局部对数的额外假设。

固定 $v\in\mathbb F_p^\times\setminus\{1,-1\}$。
对 $\epsilon\in\{1,-1\}$，定义 $\mathcal Q_\epsilon(v)$ 为满足
下列条件的有理素数 $q$：
$$
 \begin{gathered}
 q\nmid p\ell389D,\qquad q\text{ 在 }F\text{ 惰性},\\
 q\equiv v\pmod p,\qquad
 \rho_{E,p}(\operatorname{Frob}_q)\sim
          \operatorname{diag}(\epsilon,\epsilon v),\\
 \operatorname{red}(P_\epsilon)\ne0
       \quad\text{于 }E(\mathbb F_{q^2})/pE(\mathbb F_{q^2}).
 \end{gathered}
\tag{3}
$$
还可避开任意已指定的有限素数集。这些族具有正 Dirichlet 密度，
证明在 §2。

(3) 中的 $q$ 是 Zhang 意义的通常 admissible 素数：
$$
       q^2\not\equiv1\pmod p,\qquad
       a_q\equiv\epsilon(q+1)\pmod p.
\tag{4}
$$
它们与 R232 中 $q\equiv-1,\ a_q\equiv0\pmod p$ 的双线观测族不同；
也不是原 Heegner 类族的 Kolyvagin 素数。

**结论。** 每个 $q\in\mathcal Q_\epsilon(v)$ 给出一个真正的
definite Shimura set 上的剩余 Hecke 本征函数 $\varphi_q$，
以及由原 $H/F$ 全部标签构成的
$$
        \Theta_{q,\ell}\in\mathbb F_p[\Gamma]
                  =\mathbb F_p[T]/(T^p),\qquad T=\tau-1.
\tag{5}
$$
同一个非零标量同时比较其所有标签与 $Q$ 的全部完成。
特别正号族的 $T$ 系数与原第一正矩相同，负号族的 $T^2$
系数与原第二负矩相同。存在这样的非零低阶系数，当且仅当
原指数 $a\le1$。这是已付局部代价的原对象接口，
没有给出无穷多个 $p$ 的非零性。

## 2. 两个符号各自的真实 Chebotarev 构造

### 2.1 剩余表示、域交及指定 Frobenius

设 $M=E[p]$。原满像条件给
$\rho(G_F)=\mathrm{GL}_2(\mathbb F_p)$。
$L/F$ 在 $\ell$ 分歧，而 $F(E[p])/F$ 在该好位不分歧；
$[L:F]=p$，故
$$
              L\cap F(E[p])=F.
\tag{6}
$$
因此可指定在 $L/\mathbb Q$ 上为一个反射、在 $M$ 上为
$\operatorname{diag}(\epsilon,\epsilon v)$ 的同一个
$G_\mathbb Q$ 元素。具体地，从复共轭开始，乘一个
$G_F$ 元素；(6) 使其在 $L/F$ 的分量可保持为一，
而在 $M$ 上的分量可任意调整。

### 2.2 非零本征类的仿射超平面条件

令 $\xi\in H^1(F,M)^\epsilon$ 非零。
因二为单位，将它视为
$$
 H^1\!\left(\mathbb Q,M\otimes
     \chi_F^{(1-\epsilon)/2}\right)
\tag{7}
$$
中的类：这是对 $F/\mathbb Q$ 的 inflation--restriction，
在次数二群上高阶上同调为零所得的同构。
选择一个 cocycle $z$ 表示 (7)。

令 $K=LF(E[p])$。在 $\operatorname{Gal}(K/F)$ 中，
中心元 $(-I,1)$ 在 $M$ 上作用为 $-1$。
Sah 引理使非零类向 $G_K$ 的限制单射。
限制的像受满 $\mathrm{GL}_2(\mathbb F_p)$ 作用稳定，
所以是整个 $M$，不是一条可能被指定 Frobenius 杀掉的直线。

固定 §2.1 的一个提升 $g_0$，其在 $M$ 上的矩阵记为
$A=\operatorname{diag}(\epsilon,\epsilon v)$。
在由有限个所需类切出的有限扩张中，改变
$g=h g_0$，其中 $h\in G_K$。在 (7) 的扭表示中，
$g$ 的作用为 $\epsilon A$，故
$$
                    z(g^2)=(1+\epsilon A)z(g).
\tag{8}
$$
有限局部类是 (8) 在 $M/(A^2-1)M$ 中的像。
该商只有一维，对应 $A$ 的 $\epsilon$ 特征线；
在这条线上 $1+\epsilon A$ 准确为 $2$。
当 $h$ 变化时，该投影是一个满射线性泛函加常数，
其零集的相对大小正好为 $1/p$。

对于至多四个非零、符号均为 $\epsilon$ 的指定类，
在它们的联合限制像上，每个投影仍满射。四个坏仿射超平面的
并集比例至多 $4/p<1$。因此可使所有指定有限局部值同时非零。
对所得有限 Galois 扩张应用 Chebotarev，即得正密度素数集。
所有要求均在共轭下不变，所以选择 Frobenius 共轭类不改变结论。

对 $\xi=\kappa_p(P_\epsilon)$ 使用该结论，便证明 (3) 非空。
正号族还可同时定位 R232 中 $a=0$ 时的
$\kappa_{\delta,A}(Q)^+$；它是通常 Selmer 中的非零类。
这里不把这一类与原 Kolyvagin 首项
$\kappa_A((\tau-1)Q)$ 混同。

(8) 也说明为什么不能在同一个一般 admissible 素数同时定位
两个相反符号的类：若类的符号为 $-\epsilon$，其有限线上的
对应因子为 $1-\epsilon A=0$。本篇确实使用两个不同的素数族。

## 3. 原完整完成与两矩

### 3.1 分裂、局部线和全部标签

每个 $q$ 在 $L/F$ 分裂，因为二面体群中的反射平方为一。
更强地，$q$ 在整个 $H/F$ 分裂：其在 $F$ 中的素理想是
$(q)$，在导子 $\ell$ 的环类群中为主类，生成元 $q$
亦满足环类主理想的有理剩余条件。这里 $q\ne\ell$。

取 $L$ 的一个由 $c$ 固定的素位 $\mathfrak q_0$；
反射均共轭，故可这样标号。其剩余域为
$k=\mathbb F_{q^2}$，$c$ 在该域上为 $q$ 次 Frobenius。
由 (3)、$v^2\ne1$，
$$
 W_q:=E(k)/pE(k)
 \quad\text{是一维 }\mathbb F_p\text{ 空间，且 }c|W_q=\epsilon.
\tag{9}
$$
这来自 $\operatorname{Frob}_{q^2}$ 的两个特征值 $1,v^2$；
有限 Kummer 条件与 $W_q$ 自然同构。

定义真正的全部完成映射
$$
 \Phi_q(Y)=\sum_{j=0}^{p-1}
       \operatorname{red}_{\mathfrak q_0}(\tau^{-j}Y)\tau^j
       \in\overline R\otimes W_q,\qquad
 \overline R=\mathbb F_p[T]/(T^p).
\tag{10}
$$
它是 $\overline R$ 等变的，增广为 $\operatorname{red}(NY)$，
并满足
$$
       \Phi_q(cY)=\epsilon\,\Phi_q(Y)^*,\qquad
       T^*=-T/(1+T).
\tag{11}
$$
定义
$$
 \begin{aligned}
 M_{1,+}(Q;q)&=[T]\Phi_q(Q)
   =\sum_{j=0}^{p-1}j\,\operatorname{red}_{\mathfrak q_0}(\tau^{-j}Q),
       &&q\in\mathcal Q_+(v),\\
 M_{2,-}(Q;q)&=[T^2]\Phi_q(Q)
   =\sum_{j=0}^{p-1}\binom j2\,
           \operatorname{red}_{\mathfrak q_0}(\tau^{-j}Q),
       &&q\in\mathcal Q_-(v).
 \end{aligned}
\tag{12}
$$
因为这里只有一条符号线，不再插入一个虚构的第二投影。
(12) 就是 R232 的相应投影在该一维局部条件下的版本。

由 $NQ=0$、$cQ=-Q$，$\Phi_q(Q)$ 的常数项总为零。
正号族中它反对称，负号族中它对称；后一情形的 $T$ 系数也为零。
因此循环平移原标签不改变 (12)。
更换 $\tau$ 分别乘一次、二次非零单位，保留非零性。

### 3.2 三种原指数

若 $a\ge2$，写 $Q=\Delta Y$，其中 $Y\in A_0$ 且 $cY=-Y$。
由 (10)--(11)，正号族中 $\Phi_q(Y)\in T\overline R\otimes W_q$，
负号族中 $\Phi_q(Y)\in T^2\overline R\otimes W_q$。
因 $\Delta=T^2/(1+T)$，
$$
 \Phi_q(Q)\in
 \begin{cases}
 T^3\overline R\otimes W_q,&\epsilon=1,\\
 T^4\overline R\otimes W_q,&\epsilon=-1.
 \end{cases}
\tag{13}
$$
所以两族的指定低阶系数全部为零。

若 $a=1$，R232 的真实全局格给
$$
 B=RX\oplus B_0^+,\quad NX=P_-,\quad cX=-X,\quad
 Q=\Delta f(\Delta)X,\quad \lambda_Q=f(0)\bmod p\ne0.
\tag{14}
$$
对每个 $q\in\mathcal Q_-(v)$，置
$\rho_-=\operatorname{red}(P_-)\ne0$。
$\Phi_q(X)=u_q(T)\rho_-$ 的增广为 $\rho_-$，所以
$u_q(0)=1$，$u_q$ 是局部群环 $\overline R$ 的单位。
准确得到
$$
                  M_{2,-}(Q;q)=\lambda_Q\rho_-\ne0.
\tag{15}
$$
正号族中 $\operatorname{red}(P_-)=0$；
由 (11) 或 (14) 得 $M_{1,+}(Q;q)=0$。

若 $a=0$，$\kappa_{\delta,A}(Q)$ 是非零正号 Selmer 类。
§2 在正号族中同时定位它和 $P_+$，给正密度子族。
在分裂局部积中取 $\delta Y=Q$，再取 $pV=NY$。
$Y-\operatorname{diag}V$ 是 $A$ 中的真实 $\delta$-除点，
Kummer 误差为 $-\operatorname{diag}(\sigma V-V)$。
因此原局部类对应 $-\kappa_p(NY)$，而
$\delta=T+O(T^2)$ 给
$$
                       [T]\Phi_q(Q)=\operatorname{red}(NY).
\tag{16}
$$
这个子族上的 $M_{1,+}$ 非零。

综上，
$$
 \boxed{\quad
 a\le1\iff
 \bigl(\exists q_+\in\mathcal Q_+(v):M_{1,+}(Q;q_+)\ne0\bigr)
 \ \text{或}\
 \bigl(\exists q_-\in\mathcal Q_-(v):M_{2,-}(Q;q_-)\ne0\bigr).
 \quad}
\tag{17}
$$
这是两个存在量词；没有将两条不同局部线放入一个不存在的
一般 admissible 双线空间。

## 4. 升层定理及其在 E389 上的全部条件

记 $f$ 为原 $E$ 对应的权二新形式。
对 (4) 的每个 $q$，使用已发表的
Ribet--Diamond--Taylor 升层定理，按 Zhang（2014）Theorem 2.1，
取得层 $389q$ 的新形式 $f_q$，剩余表示与 $E[p]$ 同构。
其 $U_q$ 特征值为 $\epsilon$：由
$a_q(E)\equiv\epsilon(q+1)$ 且 $q+1$ 为单位，这个符号唯一。
其 $p$ 处仍普通，因为 $a_p(f_q)\equiv a_p(E)\ne0$。

所需条件在这里逐项为：

| 条件 | 原对象上的核验 |
|---|---|
| $p\ge5,\ p\nmid N_E$，剩余表示满像 | 原 R156 合法输入，本文取 $p\ge7$ |
| $F$ 的判别式与层互素 | $p,\ell,q$ 的选择及 $q\nmid389D$ |
| 原广义 Heegner 分解 | $N^+=389,\ N^-=1$，R153 的十六域均使 $389$ 分裂 |
| Hypothesis $\heartsuit$ 的原剩余分歧 | $E$ 在 $389$ 为 $I_1$；Tate 参数估值一，故对 $p\ne389$ 剩余惯性非平凡 |
| 非平方自由导子的额外分支 | $389$ 和 $389q$ 均平方自由，所以该分支及平方因子条件为空 |
| 新增 $N^-$ 素因子的分歧条件 | 升层后 $N^-=q$；该条件只对 $q\equiv\pm1\pmod p$ 要求剩余分歧，而 (4) 已排除 |
| 普通性与剩余系数域 | 普通性保持；原剩余域为 $\mathbb F_p$，升层定理保持 Hecke 剩余系数域 |

原参数化与最优商之间的固定同源、固定整数倍只需删除
R156 已允许的固定有限素数；不依赖 $q,\ell$。
在这些条件下 Zhang §4.2 的 multiplicity one 及局部比较适用。

令 $\mathscr X_q$ 为在 $q,\infty$ 分歧、Eichler 层 $389$
的 definite quaternion Shimura set。
Zhang §4.2，特别式 (4.7)--(4.9)，给非零函数
$$
                  \varphi_q:\mathscr X_q\longrightarrow\mathbb F_p,
\tag{18}
$$
带有 $f_q$ 的剩余 Hecke 特征。
其选择只差一个 $\mathbb F_p^\times$ 标量。
选择有限局部线到 $\mathbb F_p$ 的同构
$\iota_q:W_q\longrightarrow\mathbb F_p$ 后，该发表定理的实际内容为
$$
 \varphi_q(\operatorname{Red}_q x)
     =c_q\,\iota_q\!\left(\operatorname{red}_q P(x)\right),
                  \qquad c_q\in\mathbb F_p^\times,
\tag{19}
$$
对下面 §5 核验的全部 CM 标签成立。
同一个 $c_q$ 用于这些标签；不是对每一项另选一个单位。

## 5. 原 conductor、度零规范和完整 Trace

### 5.1 原 $\ell$ 确在 Zhang 的 $\mathcal C_F^+$ 内

必须注意，Zhang §3.2 式 (3.5) 的 $\mathcal C_F^+$ 不是
无条件包含所有 conductor。其允许的非平凡局部矩阵移动
位于惰性且 $v\equiv-1\pmod p$ 的素位，另允许左乘
$\widehat F^\times$。

先将 Zhang 的固定 CM 嵌入和 $389$ 处定向取成原源的选择。
原 $x(\ell)$ 在 $\ell$ 分量为
$\operatorname{diag}(\ell,1)$，其余分量保持原固定 CM 数据。
原 $\ell$ 惰性且 $\ell\equiv-1\pmod p$，所以
$x(\ell)\in\mathcal C_F^+$。
所有环类 Galois 标签由左乘 $\widehat F^\times$ 给出，
故全体 $x(\ell)^\sigma$ 仍在 $\mathcal C_F^+$。
这里从未要求 $a_\ell\equiv0\pmod p$；它实际上是单位。
因此可以应用 (19)，但不能把 $\ell$ 称作 Zhang 的 Kolyvagin 标签。

### 5.2 同一个度零处理

为明确 (19) 对原点 $P[\ell]$ 的规范，选一个辅助好素数 $b$，
满足
$$
 \begin{gathered}
 b\nmid389q\ell pD,\quad b\text{ 在 }F\text{ 惰性},\quad
 b\equiv-1\pmod p,\quad a_b(E)\not\equiv0\pmod p,\\
                         d_b=b+1-a_b(E)\in\mathbb Z_p^\times .
 \end{gathered}
\tag{20}
$$
满剩余像保证这种 $b$ 存在：选
$\lambda\in\mathbb F_p^\times\setminus\{\pm1\}$，
指定矩阵 $\operatorname{diag}(\lambda,-\lambda^{-1})$
及在 $F$ 上的非平凡作用，再用 Chebotarev。
它的行列式为 $-1$、迹非零。
因为 $b$ 也是 $\mathcal C_F^+$ 允许移动的素位，
$T_b$ 的 CM 标签仍在该集合中。
对每个 CM 标签作同一个操作
$$
             x^\circ=d_b^{-1}(b+1-T_b)x .
\tag{21}
$$
它是 $\mathbb Z_{(p)}$ 系数的度零除子。
在 $X_0(389)$ 上 $T_b(\infty)=(b+1)(\infty)$；
投影到原 $E$ 后，(21) 准确给 $P(x)$，因为 $T_b$ 作用为 $a_b(E)$。
另一方面，(18) 的本征关系给
$\varphi_q(\operatorname{Red}_q x^\circ)
=\varphi_q(\operatorname{Red}_q x)$。
所以 (21) 没有改动任一个原 $P(x)$，也没有引入标签相关单位。
这正是 Zhang Remark 6 和 (4.9) 的度零规范在原模块曲线上的实现。

若原参数化包含已固定的同源或整数倍，将其唯一的非零剩余
标量吸收到 $c_q$。由于这种规范对所有标签相同，
它也与原 Hilbert 类群和、$\operatorname{Tr}_{H/L}$ 及 $t_0$ 交换。

### 5.3 definite 群环的准确定义

置 $G=\operatorname{Gal}(H/F)$、$G_0=\operatorname{Gal}(H/L)$。
在每个 $j$ 选 $\sigma_j\in G$，使
$\sigma_j|_L=\tau^{-j}$。
选择 $\mathfrak q_0$ 在 $H$ 上的一个延拓；
§3 已保证所有点在其剩余域 $\mathbb F_{q^2}$ 中可约化。
定义
$$
 \Theta_{q,\ell}
   =\overline t_0\sum_{j=0}^{p-1}
       \left(\sum_{h\in G_0}
          \varphi_q\!\left(\operatorname{Red}_q
                  x(\ell)^{h\sigma_j}\right)\right)\tau^j.
\tag{22}
$$
更换 $\sigma_j$ 在同一个 coset 中的代表只重排内和。
(22) 保留 $G_0$ 的每个元素，包括全部 Hilbert 类群 coset；
没有除以 $h_F$、$u$ 或 $|G_0|$。

对 (19) 逐项相加，利用实际点的群和与约化的相容性，得到
**同一个单位的完整群环恒等式**
$$
                  \boxed{\quad
     \Theta_{q,\ell}
            =c_q\,(\operatorname{id}\otimes\iota_q)\Phi_q(Q).
                  \quad}
\tag{23}
$$
原 $Q$ 若已作平衡的 $\tau$ 平移，则 (22) 同作这一
循环平移。任意后续 $T$ 系数提取都作用于同一个等式，
不需要另作角色投影或更换源。

因此
$$
 \begin{aligned}
  [T]\Theta_{q,\ell}
       &=c_q\,\iota_q(M_{1,+}(Q;q)),&&q\in\mathcal Q_+(v),\\
  [T^2]\Theta_{q,\ell}
       &=c_q\,\iota_q(M_{2,-}(Q;q)),&&q\in\mathcal Q_-(v).
 \end{aligned}
\tag{24}
$$
这是一项关于原完整点的 genuine level-raising 比较，
不是任选一个 definite 本征向量后的形式类比。

## 6. 实际增广、低阶界和剩余非零门

原完整基层点在 $t_0$ 规范下为
$$
 P_F=[t_0]\operatorname{Tr}_{F[1]/F}P[1]=0,
       \qquad NQ=a_\ell P_F=0.
\tag{25}
$$
这里也可仅在 $p$ 完备点格中读 (25)，结果相同。
所以 (23) 给
$$
              \Theta_{q,\ell}(1)=0,\qquad
              \Theta_{q,\ell}^*=-\epsilon\Theta_{q,\ell}.
\tag{26}
$$
普通中心值的 mod $p$ 单位不能由 (25) 提供。

由 (13)--(17)、(24)，准确的低阶结论是：

| 原指数 | 正号一般 admissible 族 | 负号一般 admissible 族 |
|---|---|---|
| $a=0$ | 有正密度子族满足 $[T]\Theta_{q,\ell}\ne0$ | 不需作非零断言 |
| $a=1$ | $[T]\Theta_{q,\ell}=0$ | 整族均有 $[T^2]\Theta_{q,\ell}=c_q\iota_q(\lambda_Q\operatorname{red}P_-)\ne0$ |
| $a\ge2$ | $\Theta_{q,\ell}\in(T^3)$ | $\Theta_{q,\ell}\in(T^4)$ |

为说明接口确实保持原全局指数，也可记录一个更完整的精确读出。
在原已知范围 $0\le a\le(p-3)/2$ 内：

- $a$ 奇时，(14) 的 regular 分解对所有奇数 $a$ 成立，
  且 $a=1+2v_\Delta f$。负号族中 $u_q$ 始终为单位，
  故 $\operatorname{ord}_T\Theta_{q,\ell}=a+1$。
- $a$ 偶时，选 $c w=-w$ 的原 $\mathcal O$ 生成元；
  其 $\delta$-Kummer 类非零且为正号。
  §2 可使该类与 $P_+$ 同时定位非零，(16) 应用于 $w$
  给 $\operatorname{ord}_T\Phi_q(w)=1$。
  乘原 $\delta^a e$ 遂给同一正密度子族上
  $\operatorname{ord}_T\Theta_{q,\ell}=a+1$。

后一断言只使用原点格的生成元以证明存在性，不把它改作
新的 Heegner 源；(22)--(23) 中的对象始终是原 $Q$。
已知 $a+1<p$，所以这里没有群环截断端点的伪零。

(18) 的本原性仅说明 $\varphi_q$ 在整个 finite Shimura set
上的某个值非零。它不说明 (22) 的完整类群和、其中的
$T$ 系数或 $T^2$ 系数非零。实际上 (13) 证明：
如果原 $a\ge2$，无论怎样选择这里的观测素数，
这些低阶系数都会同时消失。

因此，本篇把原低阶非零门送入真正的已发表升层接口，
保留了 conductor、全部完成、全部类群、相同单位和全部规范。
尚需一个能控制 (22) 低阶系数的跨 $p$ 算术输入。
不能以 $f_q$ 非零、普通中心公式、任意其他 CM 轨道的非零值，
或某个未指定的高辅助 Kolyvagin 节点非零，代替这一输入。

## 来源与依赖

- 仓库 R2、R150、R153、R156：同一 E389、十六域、完整类群、
  原点及满像／局部条件；R230：固定负扭曲秩一；
  R232：真实 regular 格、原范数坐标及全部完成。
- Wei Zhang, *Selmer groups and the indivisibility of Heegner points*,
  Cambridge Journal of Mathematics **2** (2014), 191--253。
  本篇使用其已发表 Theorem 2.1、Remark 6、式 (3.5)、
  §4.2 式 (4.7)--(4.9)，以及那里陈述的 multiplicity one。
  [发表版全文](https://archive.intlpress.com/site/pub/files/_fulltext/journals/cjm/2014/0002/0002/CJM-2014-0002-0002-a002.pdf)。
- 本篇没有使用 $q\equiv-1$ 时的退化双符号升层定理，
  没有把通常 admissible prime 与原 Kolyvagin prime 合并。
