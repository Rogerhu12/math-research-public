# R215：同一正字符值的两条真实 pure-zero 闭 hook 有不同固定圆退化通量

日期：2026-11-15。**完整纸面证明；未运行新的研究计算。**

本稿给出一个已经可判定的 fixed-circle period 障碍，而不再把通量仅当作待评估的模板。一个既有真实响应的 universal pure 恒为零；在 R183 导数分包圆上，它模全部二阶 hook gauge 后留下一个明确的局部四次项。该项在 f 的一个上升导数包内必有严格非零的 R181 退化通量。

进一步使用真实的正、负参数控制词和**同一个** pure 校正，得到两条有限闭 hook 几何：二者 universal pure 都已经为零，$M=0$、$T=\kappa\mathfrak H$ 相同，R196 的严格正字符值也相同，但在同一个 profile 圆上的该通量不同。因此至少一条几何的完整第四 period 不能由任何允许的二、三阶 gauge 支付。

这不排除全部几何或全部 R183 圆，也不证明 $\lambda_+$ 不能经更大的 joint 不变量组读出。它准确否定的是把本稿这一个退化通量与 $\lambda_+$ 等同或视为非零常数倍。两条几何的原度量一般不同；每条几何的不可修复结论分别保持其自己的同一固定目标，未声称沿几何替换保持原度量。

## 1. 同锚算子和真实响应

采用 [R71](R71-third-holonomy-commutators-and-complete-fourth-P1.md)、[R180](R180-fixed-circle-invisible-third-hook-and-signed-fourth-period-gauge.md) 的正右积分

$$J(a)(x)=\int_x^r a(\eta)\,d\eta$$

及三个八矩算子

$$
P(a,b)=J(a''b''),\quad
R(a,b)=a'b'+xJ(a''b''),\quad
S(a,b)=J(\eta a''b'').
\tag{1}
$$

记

$$\tau_R=[P,R],\quad \tau_S=[P,S],\quad
\mathfrak H=\tau_S-3\tau_R,$$

其中 $[P,Q](a;b,c)=P(a,Q(b,c))-Q(a,P(b,c))$。
对任意第三算子 $\tau$，R83 的完整第四响应为

$$
\begin{aligned}
K_{P,\tau}(F,\phi)={}&2\tau(PD;D)
-4\tau(\phi;\phi,PD)\\
&+4P(\phi,\tau(\phi;D)),
\qquad D=F-\phi^2.
\end{aligned}
\tag{2}
$$

这保留真实传入 third 历史的最后一项。记

$$K_R=K_{P,\tau_R},\qquad K_S=K_{P,\tau_S},
\qquad K_H=K_{P,\mathfrak H}.$$

它们都是既有 $\mathcal R$ 中的真实完整函数方向；不把函数差先验当作一个可单独取得负成本的路径。

## 2. 一条无需正规化计算的完整原式

直接对 (1) 的内层求导，右 collar 端值为零，得到

$$
S(b,c)''=-b''c''-x(b''c'')',\qquad
P(b,c)''=-(b''c'')'.
$$

故完整三线性式准确为

$$\boxed{\tau_S(a;b,c)=-J(a''b''c'').} \tag{3}$$

现在取 $F=f^2$，记

$$q=f'',\qquad z=\phi'',\qquad d_2=q^2-z^2.$$

这里 $d_2$ 是对称平方 forcing 的二阶导数乘积密度，不能把它误写成普通函数 $D''$。有

$$PD=J(d_2),\quad (PD)''=-d_2',\quad
\tau_S(\phi;D)=-J(zd_2).$$

逐项代入 (2)，只对同一右锚作一次分部积分，给

$$
\boxed{K_S(f^2,\phi)=-d_2^2+4J(zz'd_2)
=-q^4+2q^2z^2+4J(zz'q^2).}
\tag{4}
$$

例如第一项 $2J(d_2d_2')=-d_2^2$；最后一次使用
$J(z^3z')=-z^4/4$。所有积分常数均由真实右 collar 固定。

式 (4) 对所有 profiles 成立，并且每项都至少含两个 f 槽。因此它的 universal pure $-4$ 模式恒为零：在 $F=0$ 的四次 $\phi$ 项中，$-z^4-4J(z^3z')=0$。另外 $\mathfrak H(q;q,q)=0$，R71/R83 的 pure 响应公式给 $\pi K_H=0$。由响应对 $\tau$ 线性，

$$K_H=K_S-3K_R,$$

于是

$$\boxed{\pi K_R=0.} \tag{5}$$

这是一条 universal 原式身份，不是单幂尾或一个具体圆的投影结论。

## 3. R183 圆上模全部 hook gauge 的局部四次项

取 R183 的同一导数分包圆。每个小导数包内，f、g 的全部正阶导数沿一个固定实方向；故对 $\phi=cf+sg$，逐点有

$$qz'-zq'=0.$$

该身份也在包间零导数区成立。因此

$$(q^2z^2)'=4q^2zz',$$

并由共同右端零值得 $4J(q^2zz')=-q^2z^2$。式 (4) 化为准确局部式

$$\boxed{K_S(f^2,\phi)=-q^2(q^2-z^2).} \tag{6}$$

R183 已证明 $\mathfrak H$ 在这个平面的三个槽上全零。R213 或直接用 R180 的循环身份给

$$K_H(f^2,\phi)=2L_f(PD),\qquad
L_f(w)=\mathfrak H(w;f,f).$$

所以整个固定圆函数有

$$
\boxed{K_R(f^2,\phi)
=-\frac13(f'')^2\bigl((f'')^2-(\phi'')^2\bigr)
-\frac23L_f(PD).}
\tag{7}
$$

这里 $PD$ 在 R183 八完整 packet 上本身是合法的六矩零 profile，见 R213；即使只用于下面通量计算，(7) 也是保持原锚的完整原式，不需要丢弃任何其他 packet 的尾。

特别地，在一个 f-only 导数包 J 上，g 的值可以非零，但 $g'=0$。对 $\theta=\pi/2$，$\phi=g$，有

$$K_R(f^2,g)|_J=-\frac13(f'')^4-\frac23L_f(P(f^2-g^2))|_J.
\tag{8}$$

式 (8) 不是说未知的原 canonical 第四成本在 J 局部化；它只对这个已经准确推出的响应成立。

## 4. 一个必然存在的内部退化点和严格非零通量

在 R183 的一个正向 f 上升导数包内选正分支，使

$$p=f'>0\quad\text{于 }(a,b),\qquad p(a)=p(b)=0.$$

可以取最左完整 packet 的第一个 f 上升段；幅度与最终归一化均为正。R183 允许预先选该 $\rho_1$ 在 $(a,b)$ 严格正、零延拓为 $C^\infty$，本文就作此选择；下文的非负 p 零延拓指这个单独的导数包，不把后面的 f 下降段包括进去。令

$$q=p',\qquad A_f=6pq'-2q^2.$$

由于 p 是非负光滑紧支撑函数，端点还满足 $q=0$。置 $v=p^{2/3}$；在内部

$$A_f=9p^{4/3}v''.$$

需要的端点论证不假定分数幂自动无限光滑。令 $M=\|p''\|_\infty>0$，对零延拓后的非负 p 用 Taylor 上界可得
$|p'|^2\le2Mp$。因此

$$|v'|=\frac23p^{-1/3}|p'|
\le\frac23\sqrt{2M}\,p^{1/6}\longrightarrow0$$

于两个端点。v 在内部为正、端点为零，所以 $v'$ 有一个正的内部最大值。取最大点 $x_0$，则

$$
\boxed{A_f(x_0)=0,\qquad p(x_0)>0,\qquad q(x_0)>0.}
\tag{9}
$$

不要求该 A 零点简单。这里利用的是光滑 w 必须满足的必要通量条件，不是穿越高重零点的充分性。

定义固定圆、固定点的线性读出

$$
\mathfrak F(U)=\int_a^{x_0}p(x)\,\partial_x^2U(f^2,g)(x)\,dx.
\tag{10}
$$

同一个积分也以 $\mathfrak F$ 记号作用于已经代入该圆的单个 $x$ 函数；因此下面 $\mathfrak F(L_f(w))$ 的含义是直接对该函数积分。

R181 的真实自伴/通量身份是

$$
pL_f(w)''=\partial_x\{A_f(pw''-qw')\}.
$$

在 a 处 $p=q=0$，在 $x_0$ 处 $A_f=0$。因此对任意全 I 光滑 w，

$$\boxed{\mathfrak F(L_f(w))=0.} \tag{11}$$

这比仅对局部支撑 gauge 为零更强；所有左、右尾以及允许的外部 w 都已包含。

对局部四次项的原积分可直接求出：

$$
\int_a^x p(q^4)''
=4pq^3q'-\frac45q^5.
\tag{12}
$$

端点常数由 $p(a)=q(a)=0$ 固定。在 (9) 处，$pq'=q^2/3$，故

$$\int_a^{x_0}p(q^4)''=\frac8{15}q(x_0)^5.$$

结合 (8)、(11)，得到严格结果

$$
\boxed{\mathfrak F(K_R)=-\frac8{45}q(x_0)^5\ne0.}
\tag{13}
$$

所以虽然 $K_R$ 的 universal pure 恒零，它在此固定圆的整个 period 函数仍不属于 $L_f$ 的像。这是一个真实响应方向的具体函数非成员证据，无需词正规形完备性或任何采样。

## 5. 完整基准保留的两条真实 pure-zero 闭 hook

下面把 (13) 接到真实几何，而不把响应差当成一个实际负成本。

R71 的有限小环重复可以提供所需的实际第三控制 $T=\tau_R$。R70 给同一常值 scalar/frame 端口的局部族 $A(t)$，其矩阵是 $tP$。使用 R83 的完整词 $Z(t,1)$，记作 $Z_t$；对某个固定允许的非零小 t，

$$
M_{Z_t}=T_{Z_t}=M_{Z_{-t}}=T_{Z_{-t}}=0,
$$

$$
\boxed{V_{Z_t}-V_{Z_{-t}}=2tK_R.}
\tag{14}
$$

两个词的全部真实基准和偶项仍在各自成本内。这里的第三控制系数 1 由有限小环复制实现，不要求一个任意给定的局部单环参数区间已经包含 1。

取 R180 的闭 hook 背景。在它同一类 Klein prototype 中，分别插入 $Z_t$ 或 $Z_{-t}$，各有四个 ambient 副本。由于每段 M=0，完整成本准确相加；第三总算子仍为同一个 $\kappa\mathfrak H$。两个未校正闭 hook 成本的差为 $8tK_R$。

由 (5)，它们具有相同的 universal pure 成本。现在只选择**同一条** R206/R210 的实际 $M=T=0$ pure 校正块 D，使四个副本清掉这个共同 pure 值。得到两条实际有限闭几何 $X_+$、$X_-$，其成本满足

$$
\boxed{
M_\pm=0,\quad T_\pm=\kappa\mathfrak H,
\quad\pi V_\pm=0,\quad V_+-V_-=8tK_R.}
\tag{15}
$$

Klein 闭合按每条修改后的真实 prototype 的位移分别成立，不假定插入块位移为零。全部背景、控制词及 D 都先有限选定，再选共同物理 I 和同一 R183 圆。因此不为比较 (15) 临时改变右锚、丢弃 s 历史或给两个几何使用不同的 profile pair。

每个 $V_\pm$ 都确实属于 U：R105 使用真实 $X_\pm X_\pm^R$ 的 $M=T=0$ 及成本 $2V_\pm$ 给出该线性空间归属。这里取半只用于空间归属，不把半倍成本冒作一个实际路径。

R196 的真实字符杀掉全部 $\mathcal R$，所以

$$
\boxed{\lambda_+(V_+)=\lambda_+(V_-)>0.}
\tag{16}
$$

严格正性分别由两个实际零矩闭路径的
$\int k^2=L+\int(h_s/h)^2>0$ 给出。另一方面，(13)、(15) 给

$$
\boxed{\mathfrak F(V_+)-\mathfrak F(V_-)
=-\frac{64t}{45}q(x_0)^5\ne0.}
\tag{17}
$$

所以至少一个 $\mathfrak F(V_\pm)$ 非零。对该几何，R184 的全部允许二阶 gauge 只加 $2\kappa L_f(w_\theta)$，第三 gauge 不改 period；(11) 说明这个违例不可能修复。该固定几何、同一第一圆和其固定目标不能通过完整第四 range。

本文没有指认未知基准下究竟是哪一个符号的几何失败，也没有把两个候选的 metric 相同当作前提。存在性反例来自严格不同的两个实际通量值，已经足够。

## 6. 对 $\lambda_+$ 读出的准确结论

在 universal pure-zero 子空间中，$K_R\in\mathcal R$，故
$\lambda_+(K_R)=0$，而 (13) 非零。该子空间上 $\lambda_+$ 本身又不为零，例如 (16)。因此不存在一个常数 c，使

$$\lambda_+=c\,\mathfrak F$$

作为该真实函数子空间上的普适身份。反方向的非零倍数关系也不成立。式 (16)–(17) 进一步给这种区别的实际几何见证。

这不回答 $\lambda_+$ 是否可能经多个左 ruling 标量、平台源和退化通量的联合映射 factor；也不回答某个特殊 fixed circle 的完整代入核是否被 $\lambda_+$ 消灭。R213 的两个左二次尾矩仍未在本文评价。

R216 的标准四阶 flat 点 ruling 障碍另有其真实状态与指定 profile 假设；本文不将它扩大。本稿的 period 反例只需要 R183 类中一个非负 f 上升导数包和 (1)–(15) 的真实构造，不依赖 R193 某个冻结有理 step 的数值或符号表。

所得新结论是：整 pure 已付以后，固定圆的退化 period 像仍有一个明确可证明的余方向；这个方向已经在 canonical 响应空间内，却不在该圆的二阶 hook gauge 像内。universal 正字符与这些固定圆可解性障碍必须分别处理。
