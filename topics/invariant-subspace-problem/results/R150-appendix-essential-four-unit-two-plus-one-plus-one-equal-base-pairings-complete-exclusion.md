# R150 附录：单位 2+1+1 的相等非零基点配对整个分支为空

日期：2026-11-26（UTC）。作者：Astra-ISP-347c-20261126；AI-assisted GPT-6 Astra Pro。

**状态：本条精确范围已证明。** 在原本质四维外均值、rankH4、活跃单位 $2+1+1$ 与一个孤立零点的长度五分支中，全部 $p=q\ne0$ 情形为空。本稿关闭先前余下的 $bc\,t\,\ell(\ell-1)(2\ell-1)\ne0$ 一般图；原 $\ell=0,1/2,1$ 和 $t=0$ 的完整结论只作引用，不重新执行。没有据此关闭 $p\ne q$、其他除子型或普通 Hilbert ISP。

## 1. 原物理模型和所有已闭边界

保留原六维非退化配对、同一长度五物理除子 $2A+B+C+Z$ 及所有值和一阶 jet。使用[原单位 2+1+1 参数化](R150-appendix-essential-four-unit-two-plus-one-plus-one-one-zero-base-pairing-exclusion.md)。同尺度规范 $p=q\ne0$ 为 $p=q=1$ 后，
$$
\mathcal B=\mathbb C[\epsilon]/(\epsilon^2)\oplus\mathbb C\oplus\mathbb C,
\quad\tau(x)=a x_0+x_1+b x_B+c x_C,\quad a=1-b-c,
$$
$$
K_B=\begin{pmatrix}
0&0&1&1\\0&A_1&r&s\\1&r&0&t\\1&s&t&0
\end{pmatrix},\qquad bc\ne0.                                  \tag{1.1}
$$
相同尺度作用于零点配对列；原 mean、最高式和第二梯度的齐次次数保持，故此规范没有删除非零 $p$。

令 $\ell=b+c$。已有[整个最高基点值零支](R150-appendix-essential-four-unit-two-plus-one-plus-one-equal-base-pairings-zero-highest-value-exclusion.md)覆盖 $\ell=0,1/2,1$，其中 $\ell=0$ 的完整原物理二阶 germ 由其所引前稿支付。[整个零单点配对支](R150-appendix-essential-four-unit-two-plus-one-plus-one-equal-base-pairings-zero-singleton-pairing-exclusion.md)又覆盖 $t=0$。因此余下必须满足
$$
\boxed{bc\,t\,\ell(\ell-1)(2\ell-1)\ne0.}                    \tag{1.2}
$$
这些是已经独立完整排除的边界，不是为了使用一般图而追加的假设。

## 2. 必须同时保留的原零点条件

令 $1=(1,0,1,1)$，使用原乘法定义
$$
(D_Kx)_i=\tau((K_B)_{i,\bullet}x),\quad d=D_K1,\quad f=\tau(d)/2,
$$
$$
P(x)=\tfrac12\tau(x-\tau(x)1)^3,
$$
$$
N(x)=\tfrac12\tau((d-f1)x^2)-\tau(x)\tau(dx)
+f\tau(x)^2+\tfrac14\tau(xD_Kx).
$$
四条 active mean 是
$$
E=e-2D_Kd-2d^2+4fd=0,
\quad e=(\tau k_0^2,2\tau k_0k_1,\tau k_B^2,\tau k_C^2).          \tag{2.1}
$$
$P_0,P_1,P_B,P_C$、$N_0,N_1,N_B,N_C$ 表示同一原行上的值及双点的一阶 jet；$P_1$ 是 $P(k_0+h k_1)$ 在 $h=0$ 的导数，$N_1$ 同理。

令原孤立零点配对列为 $\mathbf u=(u_0,u_1,u_B,u_C)$、$m=\tau(\mathbf u)$。原最高式和第二梯度要求
$$
(P_0,P_1,P_B,P_C)=(-u_0^3,-3u_0^2u_1,-u_B^3,-u_C^3),
$$
$$
(N_0,N_1,N_B,N_C)=(-mu_0^2,-2mu_0u_1,-mu_B^2,-mu_C^2).         \tag{2.2}
$$
独立的原零点 mean 和最高式还给
$$
\tau(\mathbf u^2)=2m^2,\qquad P(\mathbf u)=0.                 \tag{2.3}
$$
这是[原零点 mean 的无除法推导](R150-appendix-essential-four-unit-two-plus-one-plus-one-equal-base-pairings-zero-singleton-pairing-exclusion.md)中的同一系数，不可由两两范数相容式替代。

写
$$
\overline P=(1-\ell)P_0+P_1+bP_B+cP_C,\quad
\overline N=(1-\ell)N_0+N_1+bN_B+cN_C.
$$
(2.2)—(2.3) 使 $\overline N=-2m^3$、$\overline P=-4m^3$。所以所有原解必须同时满足
$$
S:=\overline P-2\overline N=0,\qquad
c_0:=3P_0N_1-2N_0P_1=0,
$$
$$
\boxed{\Lambda_0:=2N_0^3-\overline N P_0^2=0.}                \tag{2.4}
$$
这些条件的推导没有除以 $m$ 或任何 $u_i$。下文只用原必要条件作排除，并不反称其充分。

## 3. 对称变量与第一个完整线性消去

置
$$
\beta=bc\ne0,\quad\delta=b-c,\quad\delta^2=\ell^2-4\beta,
$$
$$
x=d_B,\quad y=d_C,\quad X=(bx+cy)/\ell=\ell+V,\quad Z=x-y.
$$
这里 $V$ 只是本节标量参数，不是原第三累积量张量。由 $E_0=0$ 可且仅可恢复
$$
f=\frac X2+\frac\ell2-\frac14,
\quad A_1=(1-2\ell)(X-\tfrac12)+2\beta t,
$$
$$
x=X+\frac{cZ}{\ell},\quad y=X-\frac{bZ}{\ell},\quad
r=x-(1-\ell)-ct,\quad s=y-(1-\ell)-bt.                       \tag{3.1}
$$
只使用已知非零的 $\ell$。

再置 $U=Z^2,W=\delta Z$。原式中的对称偶多项式可由
$\delta^{2i}Z^{2j}\mapsto(\ell^2-4\beta)^iU^j$ 和
$\delta^{2i+1}Z^{2j+1}\mapsto(\ell^2-4\beta)^iU^jW$ 准确转换；源码逐单项核验两指数同奇偶。必须保留
$$
W^2=(\ell^2-4\beta)U.                                       \tag{3.2}
$$

原 $E_1$ 和 $E_w=(bE_B+cE_C)/\ell$ 对 $(U,W)$ 为线性，其系数行列式准确为
$$
-\frac{8\beta^2t}{\ell^3}\ne0.                              \tag{3.3}
$$
因此它们唯一解出
$$
U=\frac{\ell[-8V^2\ell+4V^2+8V\ell-4V+4\beta t^2-16\beta t
+4\ell^2-4\ell+1]}{8\beta},
$$
$$
W=-\frac{\ell[8V^2\ell-4V^2-16V\beta t+8V\ell^2-12V\ell+4V
+4\beta t^2-4\ell^2+4\ell-1]}{8\beta t}.                     \tag{3.4}
$$
还保留 $\delta(E_B-E_C)=0$。这里乘以 $\delta$ 只给必要条件，**没有除以 $\delta$**，故 $b=c$ 的等权纤维也保留；对这个必要方程集的空性足以排除原解。

## 4. 第二个处处合法的线性消去

将 (3.4) 代入下列四个原必要式：
$$
\delta(E_B-E_C),\quad W^2-(\ell^2-4\beta)U,\quad c_0,\quad S.
\tag{4.1}
$$
取约分后的分子，只除去 (1.2) 已非零的有理常数和 $\ell,\beta,t,\ell-1,2\ell-1$ 的因子。完整因子及分母清单由源码实际打印在执行记录中；其余任何因子均不删除。

定义可逆的新非零参数
$$
k=\frac{4\beta t}{\ell}\ne0,\qquad\beta=\frac{\ell k}{4t}.
\tag{4.2}
$$
把它代入这四个原分子后，所有 $t$ 分母准确消去。第三个分子对 $t$ 为一次式，系数恰为
$$
\boxed{k\ell^2(\ell-1)(2\ell-1)\ne0.}                       \tag{4.3}
$$
所以全部原解必须
$$
t=-\frac{T(V,k,\ell)}{k\ell(\ell-1)(2\ell-1)},              \tag{4.4}
$$
其中
$$
\begin{aligned}
T={}&40V^2\ell^2-44V^2\ell+12V^2-16Vk\ell^2+8Vk\ell\\
&+16V\ell^4+32V\ell^3-84V\ell^2+56V\ell-12V+2k^2\ell\\
&-20k\ell^3+26k\ell^2-10k\ell
+32\ell^4-68\ell^3+56\ell^2-21\ell+3.
\end{aligned}
$$
没有使用 $T$ 作除数，因此不会漏掉它的零点。

把 (4.4) 代入 (4.1) 的第一、第二、第四个分子，取约分后分子再除已知非零的单因子 $\ell$，依次称为 $G_0,G_1,G_2\in\mathbb Q[k,V,\ell]$。它们的 $(k,V,\ell)$ 次数为
$$
(4,4,6),\qquad(4,4,8),\qquad(4,4,6).                         \tag{4.5}
$$
同样从原 $\Lambda_0$ 作 (3.4)、(4.2)、(4.4) 代入后，准确得到
$$
\Lambda_0=\frac{\ell G_3}{256k},\qquad
\deg_{(k,V,\ell)}G_3=(4,4,8).                                \tag{4.6}
$$
其分母在当前图处处非零。所有原解因此满足
$$
G_0=G_1=G_2=G_3=0.                                          \tag{4.7}
$$
这些多项式的定义由原式和显示的代换完全确定；配套自含源码重建它们，不以保存的计算数组作输入。

## 5. 两轮完整 QQ 结式保留所有例外纤维

先计算四个关于 $k$ 的完整结式
$$
R_{01},R_{02},R_{12},R_{03}:=
\operatorname{Res}_k(G_0,G_1),\operatorname{Res}_k(G_0,G_2),
\operatorname{Res}_k(G_1,G_2),\operatorname{Res}_k(G_0,G_3).
$$
其关于 $(V,\ell)$ 的次数依次为
$$
(16,38),\ (16,34),\ (16,40),\ (16,42).                        \tag{5.1}
$$
只删除已知非零的 $\ell,\ell-1,2\ell-1$ 因子和有理常数，得 $\widetilde R$。源码核验因子乘积与每个原结式完全相等，并确认没有其他仅依赖 $\ell$ 的因子被删除。

$\widetilde R_{01}$ 准确分为三个不同因子 $A,B,C$，重数分别为 $1,1,2$；双次数分别为 $(2,3),(10,12),(2,2)$。其中
$$
\begin{aligned}
A={}&4V^2\ell^3-12V^2\ell^2+12V^2\ell-4V^2
-12V\ell^3+26V\ell^2-18V\ell+4V\\
&+10\ell^3-14\ell^2+7\ell-1,\\
C={}&4V^2+4V\ell^2+2V\ell-4V-2\ell+1.
\end{aligned}                                                 \tag{5.2}
$$
$B$ 是由同一精确因子分解唯一确定的 $(10,12)$ 因子，规范差非零有理常数无关零点。其余三个净结式的双次数为 $(16,20),(16,20),(16,29)$。

对 $D=A,B,C$，分别对 $V$ 计算
$$
\operatorname{Res}_V(D,\widetilde R_{02}),\quad
\operatorname{Res}_V(D,\widetilde R_{12}),\quad
\operatorname{Res}_V(D,\widetilde R_{03}).                    \tag{5.3}
$$
特征零有理数计算给以下完整清单，gcd 只省略非零常数：

| $D$ | 三个 $\ell$ 结式次数 | 精确 gcd |
|---|---:|---|
| $A$ | $88,88,106$ | $\ell^{16}(\ell-1)^{10}(5\ell^2-4\ell+1)$ |
| $B$ | $309,315,405$ | $\ell^{80}(\ell-1)^{30}(2\ell-1)^{10}(5\ell^2-4\ell+1)$ |
| $C$ | $59,59,79$ | $\ell^{16}(2\ell-1)^4$ |

每个原解使 $R_{01}=0$，所以至少属于 $A,B,C$ 的一个零集；又必须使 (5.3) 三式同时为零。由 (1.2)，$C$ 整支不可能，前两支只余
$$
\boxed{Q(\ell):=5\ell^2-4\ell+1=0.}                          \tag{5.4}
$$
这里只使用有限共同根使结式为零的必要性。所有首项系数下降可能增加的候选均仍留在 (5.4)，没有把“结式零”当成原方程有解。

## 6. 最后两个共轭权重的原理想身份

令 $Q_0=\ell^2-4\ell/5+1/5$，并记 $g_i$ 为 $G_i$ 对 $Q_0$ 关于 $\ell$ 的精确余式。每个 $g_i$ 的 $\ell$ 次数至多一，$(k,V)$ 总次数至多四。

采用乘子单项式
$$
\{k^aV^b\ell^c:a+b\le3,\ c=0,1\}.
$$
对四个 $g_i$ 建立精确有理数系数身份矩阵：系数矩阵为 $72\times80$，附目标 $k$ 后为 $72\times81$。完整有理数行化简的秩是 $70$，所有主元都在前 $80$ 列。由此取得四个真实有理系数乘子 $A_i$，满足
$$
\deg_{k,V}A_i\le3,\quad\deg_\ell A_i\le1,
\qquad
\boxed{\operatorname{rem}_\ell\left(\sum_{i=0}^3A_i g_i-k,Q_0\right)=0.}
\tag{6.1}
$$
源码实际构造这些乘子，并重新作精确多项式乘法核验 (6.1) 的余式为零；不只报告一个 Gröbner 基标签。按源码固定顺序排列的乘子字符串 SHA256 为
`81f5bdb609e64b3a733a08f611e9d03632eed779e8767baee001c2ea7dc834ad`。
乘子及矩阵均从原方程重建，不保存可重算数组。

因此在 $Q=0$ 和全部 $G_i=0$ 上必有 $k=0$，与 (4.2) 的 $k\ne0$ 矛盾。两个复共轭权重均一起支付，没有挑选根号分支。一般图 (1.2) 完全为空；接第一节已闭边界，整个相等非零配对分支也为空。

## 7. 执行身份和准确范围

自含[原式 QQ 源](../notes/2026-11-26-unit211-equal-general-347c.py)直接重建原 $E,P,N$ 和 jets，检查全部线性消元系数、所有删除因子、完整特征零结式及最后的有理数理想身份。运行依赖 Python 3.12.14、SymPy 1.14.0 和 python-flint 0.9.0，命令为 `PYTHONPATH=/tmp/isp-347c05929dd3/deps python 2026-11-26-unit211-equal-general-347c.py`。实际执行身份见[小回执](../notes/2026-11-26-unit211-equal-general-execution-347c.json)。

最终自含源实际 exit 0，程序计时 19.744046 秒，峰值 RSS 78596 KiB；源码 SHA256 为 `cc7b22bbbb720e2fd19378ceb18618784175c783ac77a4c7a053e195050e4422`。原始紧凑输出 SHA256 为 `fccbef76786524454d23b94b88d247b4dd69373a2a43e2309bd30045f470e872`。全部新增 QQ 门和最后理想身份在这次成功执行中完整完成。

最初对未降维四变量方程作 QQ(ℓ) F5b 的探索实际在 240 秒停止，没有数学结论；本稿换用原非零变量和原生结式，并未把该超时当作空性。首次整合源码的末尾 JSON 格式化曾因 FLINT 整数序列化失败；修正只涉及回执格式，前后源码 SHA 和该失败输出身份均保留在小回执中。

排除始终保同一原物理配对、最高式、低梯度和全部 jets，只从其必要条件推出矛盾。证明未选物理点的有限仿射坐标，因而原 divisor 模型所允许的无穷远情形也涵盖。其余非相等配对、unit $1^4$、更高秩层、原 Bell 全局自然幂与算子桥仍须继续。
