# R310：一个完整 self 新方向——even 母包的全部平移仍不忠实于全 Q

日期：2026-11-15。**完整纸面证明；没有执行新的符号程序、profile 求积、采样、秩计算或人工检查。**

R303 已证明：对每个固定非零实紧母包，十条响应准确控制其全部平移的完整 self。R307/R309 又给全母包九次、八次层的共同系数。本稿指出不能把这些结论直接提升为整个 profile 函数空间上的 self 控制：有一个完全明确的真实响应，在所有 even 母包的任意平移、幅度及正宽度下都不可见，但其完整 universal self 非零。

该响应来自既有原 $\chi_{34}-3\chi_{32}$ 与 $P=\Phi_{r_0}$。准确结论是
$$
\pi K_J=0,\qquad \mathsf T(K_J)=0,\qquad
\boxed{\mathfrak q_u(K_J)=\int u'u''(u''')^2.}
$$
右端是完整值，无 $C^2$ 余项。下面支付同右锚积分、真实三矩核、非零紧母包的存在，以及与 R303 十维模块的严格独立性。

来源：[R261](R261-eight-local-self-adjoint-hook-operators-and-full-third-kernel.md)、[R297](R297-ordered-platform-matrix-surjective-pure-zero-responses-and-real-control.md)、[R298](R298-zero-platform-matrix-with-nonzero-self-response-and-ten-observation-control.md)、[R303](R303-complete-self-degree-nine-and-all-translation-control.md)、[R307](R307-universal-degree-nine-self-layer-and-real-elimination.md)、[R309](R309-universal-degree-eight-self-layer-and-second-real-compensation.md)。

## 1. 完整第三方向和原响应

保原右积分
$$
(Jf)(x)=\int_x^{r_*}f(\xi)d\xi,\qquad DJ=-1.
$$
取 R254/R261 的真实完整第三对角核元素
$$
\tau_*=\chi_{34}-3\chi_{32}\in Z=\ker\Delta .
\tag{1}
$$
定义真实完整第四响应
$$
\boxed{K_J=64\,\mathcal B_{r_0}(\tau_*),\qquad
P(u,u)=\Phi_{r_0}(u,u)=J((u'')^2).}
\tag{2}
$$
$\mathcal B$ 始终是 R83/R255 的完整外槽、内槽及第三 history 规范；(2)不是只定义一个新的 quartic 密度。

R261 的完整局部表示为
$$
K_f^\tau(w)=-J^3(\mathscr A_{\tau,f}w),\qquad
\mathscr A_{\tau,f}=D^2(aD^2)+D(bD)+c.
\tag{3}
$$
三个原右常数是零，全部左尾保留。因为 $\tau_*\in Z$，完整极化身份给
$$
\pi K_J=0.
\tag{4}
$$

## 2. 原 c 系数的一条准确差

置 $v=u'$、$r=u''$、$s=u'''$。直接相减 R261§3.2、§3.3 已发表的 c 多项式，所有显式 x 项准确消去：
$$
256c_{\tau_*,u}
=8u'u^{(5)}+24u''u^{(4)}+16(u''')^2 .
\tag{5}
$$
用乘法求导把它写成
$$
\boxed{
c_{\tau_*,u}
=\frac1{32}D^3(vr)-\frac1{64}D^2(r^2).
}
\tag{6}
$$
这里使用
$$
D^3(vr)=u'u^{(5)}+4u''u^{(4)}+3(u''')^2,\quad
D^2(r^2)=2u''u^{(4)}+2(u''')^2.
$$
这是已发表局部式的手写准确重组，没有新原根恢复或算子评价。

对真实紧 u，(6)特别给
$$
\int c_{\tau_*,u}=0,\qquad
\int x c_{\tau_*,u}=0,\qquad
\int x^2c_{\tau_*,u}=-\frac{\mu_0(u)}{32}.
\tag{7}
$$
第三个矩一般非零。因此不能把 $\tau_*$ 误称为对所有 E8 方向都产生矩阵零响应；下面的结论使用(2)中特定的 $P$。

## 3. 整九矩为零，保真实右包尾

对全在 u 右侧的紧包 w，$P(w,w)$ 在 u 的整个支撑上是原常尾
$$
P(w,w)=\mu_0(w).
$$
没有将它置零。

R297 的完整有序查询恒等给
$$
\mathfrak t_{u,w}(\mathcal B_E\tau)
=-\frac14\int c_{\tau,u}\Phi_E(w,w).
$$
采用(7)和 $E=r_0$，得到
$$
\mathfrak t_{u,w}(K_J)
=-16\,\mu_0(w)\int c_{\tau_*,u}=0.
$$
对全部真实分离输入成立；R297 的固定三左三右三矩基因而给
$$
\boxed{\mathsf T(K_J)=0.}
\tag{8}
$$
这里是完整九矩零，不是只对总三矩为零的某个圆成立。其原因是 P 的真实左尾为常数与(7)第一式，而非忽略(7)的非零二次矩。

## 4. 完整 self 恰等于一个奇反射积分

全 U 的 self 查询仍是
$$
\mathfrak q_u(V)=\frac14[x^2]_{\rm left}V(u^2,0).
$$
R298 的完整原式给
$$
\mathfrak q_u(\mathcal B_E\tau)
=-\frac14\int c_{\tau,u}\Phi_E(u,u).
\tag{9}
$$
将(6)代入，暂不乘(2)的64，得到
$$
\mathfrak q_u(\mathcal B_{r_0}\tau_*)
=-\frac1{128}\int D^3(vr)P(u,u)
+\frac1{256}\int D^2(r^2)P(u,u).
\tag{10}
$$

虽然 P 一般有非零左常尾，但 $vr,r^2$ 及其所需端 jets 都真正紧支撑。所有分部积分边项因此为零。又
$$
P'=-r^2,\quad P''=-D(r^2),\quad P'''=-D^2(r^2).
$$
所以第二项为
$$
\int D^2(r^2)P=\int r^2P''
=-\int r^2D(r^2)=0.
\tag{11}
$$
第一项中
$$
\int vrD^2(r^2)
=2\int vrs^2+2\int vr^2u^{(4)}.
$$
而
$$
\int vr^2u^{(4)}
=-\int(r^3+2vrs)s=-2\int vrs^2,
$$
其中 $\int r^3s=0$ 是真实紧端全导数。因此
$$
\int vrD^2(r^2)=-2\int vrs^2.
$$
回到(10)并乘64，最终得到
$$
\boxed{
\mathfrak q_u(K_J)=\mathcal J(u):=
\int_Iu'u''(u''')^2dx .
}
\tag{12}
$$

式(12)来自(9)的完整 self，不是仅其 $u'''$ 主符号。没有剩下未写的 $C^2$ 观测、右尾常数或局部端势。

## 5. 真实非零紧母包存在，不用数值找例子

对泛函
$$
\mathcal J(u)=\int L(u',u'',u'''),\qquad
L=u'u''(u''')^2,
$$
其 Euler 表达式为
$$
\mathcal E(L)
=-D\{u''(u''')^2\}
+D^2\{u'(u''')^2\}
-D^3\{2u'u''u'''\}.
\tag{13}
$$
最高六阶 jet 的系数准确为
$$
-2u'u''\,u^{(6)};
$$
前两项最高只到五阶，不能抵消它。因此该 Euler 多项式不恒零。

这个形式判断可以直接变成一个真实紧函数的存在证明。任取预留开包络中的一点 $x_0$，用一个在其邻域为1的光滑紧 cutoff 乘以多项式
$$
(x-x_0)+\frac12(x-x_0)^2+\frac1{720}(x-x_0)^6.
$$
所得真实紧 $u_0$ 在 $x_0$ 有
$$
u_0'=u_0''=u_0^{(6)}=1,\qquad
u_0'''=u_0^{(4)}=u_0^{(5)}=0.
$$
代(13)得 $\mathcal E(L)(x_0)=-2$。选一个非零、非负、支撑足够靠近 $x_0$ 的真实紧变分 $\psi$，则
$$
D\mathcal J(u_0)[\psi]
=\int\mathcal E(L)(u_0)\psi<0.
$$
如果 $\mathcal J(u_0)\ne0$ 已得所需母包；若它为零，则对充分小的非零有限 $\epsilon$，
$\mathcal J(u_0+\epsilon\psi)\ne0$。所有 profiles 都在原预留包络内，没有求积、扫描或执行测试。

由(12)，$K_J$ 是一个真实非零完整成本函数；若它在 U 中为零，则所有真实原 self 查询都应为零，与上述母包矛盾。

## 6. 所有 even 母包的平移、幅度、宽度都看不见它

对任意真实平移，
$$
\mathcal J(u(\,\cdot-c))=\mathcal J(u).
\tag{14}
$$
在一个对称内部包络中作真实反射 $u^\#(x)=u(2x_0-x)$，则 $u'$ 变号、$u''$不变、$(u''')^2$不变，所以
$$
\mathcal J(u^\#)=-\mathcal J(u).
\tag{15}
$$
故一个关于其母中心 even 的 u 满足 $\mathcal J(u)=0$。

更一般，对非零实幅 $\rho$、正宽 $a$，
$$
\mathcal J\!\left(\rho\,u\!\left(\frac{x-c}{a}\right)\right)
=\rho^4a^{-8}\mathcal J(u).
\tag{16}
$$
因此
$$
\boxed{
u\text{ 为 even 母包}
\Longrightarrow
\mathfrak q_{\rho u((\cdot-c)/a)}(K_J)=0
\quad\text{对全部允许 }c,\rho,a.
}
\tag{17}
$$
这不是说 K 对由多个不同中心包叠加而成的整个 profile 也为零；(17)只陈述这些单包 self 查询。叠加时 quartic 交叉仍须完整保留。

结合第5节，(17)明确证明：某 even 母包的全部平移 self 即使忠实读取了 R303 的十维模块，也不忠实于整个 universal self 像。不是把一个非零 NF 当作反例，而是给出了一个完整非零原查询。

## 7. 与十维模块的严格独立及一个有限控制接口

令
$$
\mathcal G_{10}=\operatorname{span}(G_0,\ldots,G_9)
$$
为 R303 的明确十响应。固定任意非零 even 紧母包 $u_{\rm e}$。R303 已证明
$$
\mathcal G_{10}\longrightarrow\operatorname{Pol}_{\le9},
\quad V\mapsto[c\mapsto\mathfrak q_{(u_{\rm e})_c}(V)]
$$
是同构。

若 $K_J$ 属于 $\mathcal G_{10}$，则由(17)，该同构会迫其全部十个系数为零，从而成本 $K_J=0$，与第5节矛盾。因此它不在这十维模块中。

结论可准确提升到全 self 函数像。定义
$$
\mathcal Q_{\rm all}(V):u\longmapsto\mathfrak q_u(V).
$$
任何
$$
\sum_{l=0}^9a_l\mathcal Q_{\rm all}(G_l)
+b\mathcal Q_{\rm all}(K_J)=0
$$
先在 $u_{\rm e}$ 全平移上评价，由(17)及十维同构得全部 $a_l=0$；再用第5节的真实非零母包得 b=0。所以
$$
\boxed{
\dim\mathcal Q_{\rm all}
(\mathcal R_{\mathrm p0}\cap\ker\mathsf T)\ge11.
}
\tag{18}
$$
这里是完整 self 像的严格下界，不预报其总维数或全 U 的像是否已被覆盖。

一个直接的实际有限后果是：选第5节的 $u_{\rm a}$，使 $\mathcal J(u_{\rm a})\ne0$。R303 的十个 even 母包查询加 $\mathfrak q_{u_{\rm a}}$，在 $\mathcal G_{10}+\mathbb RK_J$ 上为三角满秩；KJ在前十行零、最后一行非零。再与 R297 九矩作同一准确三角消元，R222 可真实同时支付 whole pure、九矩、该 even 母包全部平移 self，以及这一指定非 even 母包的一个完整 self 值。

这仍是有限观测的实际控制，不是所有不同母包或所有平移族的共同解，也不靠符号负路径。全部基准、pure 校正的 mixed 成本与最后有限复制保留。

## 8. 与全 Q 主线及构造范围

本稿给了一个自然的新分支，说明继续全 Q 时必须保不同母形的真实信息。R307/R309 的普适高层系数仍然有效；本稿的 $\mathcal J$ 是平移不变的零次轮廓，不反驳它们，而是显示低层已经出现不同于正积分 $\mathcal I$ 的完整母包泛函。

它不宣称 $\mathcal J$ 是某个尚未计算七次层的全部系数，也不从(18)推出全部 self 可控。下一需要比较的是完整 self 函数像及其真实关系，不能继续只拿一条 even 母形的所有中心当作 universal 忠实查询。

这些成本/控制结论本身不保证任何指定圆的完整 period/ruling 相容性。若另有原完整证明排除某个不交 rank-one 微包圆类，(12)、(18)不会使那个类恢复 joint 可解；新构造仍须逐项支付其真实全角原条件。

作者责任：以上只使用已发表 c 系数、完整 self/矩阵公式和有限手写积分身份；非零性用真实 compact 变分证明，没有新增科学执行。
