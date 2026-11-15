# R396：两条固定自然通量与十一类内部通量的真实联调

日期：2026-11-15。**只读原 source 与纸面构造；没有执行科学、符号、积分、数值或人工测试。**

本稿只补一个实际接口：
[R395](R395-independent-internal-fluxes-in-the-joint-pure-self-and-natural-kernel.md)
的新内部通量列可以直接加入
[R392](R392-real-joint-control-of-response-E-components-and-two-natural-fluxes.md)
的真实截面。它们不增加原未付商；也不因此支付 whole $E$ 或全部自然 $\Lambda$。

## 1. 固定查询与准确实际结论

沿用
$$
E=(\pi,\mathcal Q),\quad
\mathscr P=E(U),\quad
\mathscr L=E(\mathcal R),\quad
F=P_{\mathscr L}E,\quad
A=(\Lambda_{u_+},\Lambda_{u_-}).
$$
$P_{\mathscr L}$ 与 R390 的两个 profiles 从起点固定。

另固定 R391 的最终真实 profiles，以及 R345/R395 的 $m\le11$ 个同形对应点 $x_j$。使用同一右锚和完整查询
$$
\mathfrak F_j(V)=
\int_{\ell_j}^{x_j}f'V(f^2,g)''
-\{f(x_j)-f(\ell_j)\}V(f^2,g)''(\ell_j),
\qquad
\mathfrak F=(\mathfrak F_j)_{j=1}^m.
\tag{1}
$$
原平台校正项对一般 $V$ 始终保留。共同合法窗口与有限原型库按 R392 从起点选择；这里不扩大旧冻结 metric，也不在求目标时移动这些 profiles 或点。

**推论。** 对每个
$$
(z,\lambda,b)\in\mathscr L\times\mathbb R^2\times\mathbb R^m
$$
存在同一个有限真实 $M=\mathbf T=0$ 块 $B$，满足
$$
\boxed{F(V_B)=z,\qquad A(V_B)=\lambda,\qquad
\mathfrak F(V_B)=b.}
\tag{2}
$$
紧目标集有固定有限字、固定整数中的 $C^1$ 截面；原 Klein 闭合可以保全部目标与其完整基准。

这是实际路径结论。$F$ 仍只是 E 的响应分量；$A$ 仍只是原两条固定自然读出。

## 2. 增广响应基与真实仿射安置

令
$$
K_n=\delta^n\!\left(\frac13\mathcal B_P[P,S]\right),
\quad 0\le n\le10.
$$
R395 已付
$$
K_n\in\mathcal R_{71}\cap\ker E\cap\ker\Lambda_{\rm all},
$$
且 $m\times m$ 的真实矩阵
$$
\mathsf M_{\rm pt}=(\mathfrak F_j(K_n))_{j=1,\ldots,m;\ n=0,\ldots,m-1}
$$
可逆。这里只引用原对应点结论，不重做 Vandermonde，不将它推广到任意不同的退化点。

选旧响应 $R_1,\ldots,R_d$，使 $\mathsf M_E=(F(R_j))$ 是 $\mathscr L$ 的基。置
$$
F^+=(F,\mathfrak F).
$$
对列 $(R_1,\ldots,R_d,K_0,\ldots,K_{m-1})$，完整矩阵准确为
$$
\boxed{
\mathsf M=
\begin{pmatrix}
\mathsf M_E&0\\
\mathsf C&\mathsf M_{\rm pt}
\end{pmatrix},\qquad\det\mathsf M\ne0.}
\tag{3}
$$
左下块 $\mathsf C$ 是旧响应的实际内部通量，不置零。全部这些响应仍满足 $A(\mathcal R)=0$。

R392 的共同 $\omega$ 安置会输运成本列，不能把列值标签当作不变。本处有准确的稳定性：R345 原
$$
NK_n=n(n-11)K_{n-1},\qquad HK_n=(-5+n)K_n
$$
使 $\operatorname{span}(K_0,\ldots,K_{m-1})$ 在平移和正伸缩的真实作用下稳定。由 R89 的完整协变，输运在该空间是可逆三角矩阵，真成本伸缩权为 $-8+n$。保持查询(1)不动时，新 $\mathsf M_{\rm pt}$ 只是右乘该可逆矩阵。

因此无需假设固定查询的核仿射稳定。旧 E 列也按 R392 在变换后的响应像中重选基，保(3)。M0/frame 夹心桥保完整第三算子，其新增第四基准仍必须入账。此处没有把形式非仿射 $\delta$ 流当作实际几何变换。

## 3. 原真实基准不能删除，但不产生新障碍

把(3)的列统一记为 $R_\alpha^+$。每条都在原响应空间，故有 R392 §3 的有限完整第三 prototypes。按其 §4，先用 R390 实际块清每组 prototype 的两条 A 基准，记修正后的真实成本和为 $\widehat v_\alpha$。准确有
$$
A(\widehat v_\alpha)=0.
$$
清零块的全部 $F^+$ 与 $qE$ 成本仍保留；它们随后随原型重复 $n$ 次。响应展开的系数只进入第二阶参数，不作为负次路径复制。

R392 §5 的真实共享倒行字于是原样给
$$
V_{Z(t,n)}=E_0(t)+n\left(2\sum_\alpha\widehat v_\alpha+
\sum_\alpha t_\alpha R_\alpha^+\right).
\tag{4}
$$
置
$$
a^+=2\sum_\alpha F^+(\widehat v_\alpha),\qquad
t^0=-\mathsf M^{-1}a^+.
$$
依次固定 $t^0$ 的紧参数盒、第二阶小族的有限重复整数，末尾 $n$ 此时尚未选取。

因为全部响应及修正原型都被 A 杀掉，后置 R390 截面仍只需目标
$\lambda-A(E_0(t))$。它也有完整的新内部通量成本。故最终准确方程为
$$
A(V_{\widetilde Z})=\lambda,\qquad
F^+(V_{\widetilde Z})=
\mathcal E^+(t,\lambda)+n(a^++\mathsf M t),
\tag{5}
$$
$$
\mathcal E^+(t,\lambda)=F^+(E_0(t))+
F^+\!\left(V_{\mathscr D_A(\lambda-A(E_0(t)))}\right).
\tag{6}
$$
(6)第二项通常非零，不能只保它的 A 值。

固定紧目标集后，(6)及一次 $t$ 导数有界；固定点导数和紧积分查询的 $C^1$ 性由 R56/R302 真实恢复给出。R392 §7 的同一次有限整数选择现在解
$$
t=t^0+\frac1n\mathsf M^{-1}
\{(z,b)-\mathcal E^+(t,\lambda)\},
\tag{7}
$$
得到准确根与 $C^1$ 截面。这就证明(2)，不需要新的正字符排除或新增科学计算。

Klein 成本为 $4V_B+V_{\rm K}$ 时，三个目标分别减去
$F(V_{\rm K}),A(V_{\rm K}),\mathfrak F(V_{\rm K})$，再共同除以4。
桥的内部通量也不能省略。

## 4. 原未付商与 complete-period 范围

R392 已付 $(E,A)(U)=\mathscr P\times\mathbb R^2$；利用上述 $K_n$ 可独立改内部通量。因此对
$J_m=(E,A,\mathfrak F)$，
$$
J_m(U)=\mathscr P\times\mathbb R^2\times\mathbb R^m,\qquad
J_m(\mathcal R)=\mathscr L\times\{0\}\times\mathbb R^m,
$$
$$
\boxed{
J_m(U)/J_m(\mathcal R)
\simeq(\mathscr P/\mathscr L)\times\mathbb R^2.}
\tag{8}
$$
新增对应点没有增加响应商，但也没有把它付掉。(5)的原商仍准确为
$$
qE(V_{\widetilde Z})=
qE(E_0(t))+2n\sum_\alpha qE(\widehat v_\alpha)
+qE\!\left(V_{\mathscr D_A(\lambda-A(E_0(t)))}\right).
\tag{9}
$$
三项均保留，尤其原型清 A 的成本可能使第二项随 $n$ 放大。其它 $\Lambda_u$ 同样未由两条固定 A 得到控制。

若以后取得(8)上的同一个实际 $C^1$ 截面，原 R392 复制法即可连同 whole $E$ 支付本稿全部内部查询，不需重证其满射。当前(2)不授该商截面。

R391 使所选简单点的 partial 值成为完整局部逆 germ 的准确条件；本稿完成的是这些有限读出与已付实际目标的联调。它没有支付全部其它点、$V_e$、R394 的同一相位十三行、其它路径段 ruling，亦不继承旧几何的 whole E、Morse 或全部自然通量。原两完整 period 与同一补偿的全局解仍需那些准确剩余条件。
