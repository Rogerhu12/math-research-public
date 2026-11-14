# R286：原严格 MW 字符的中心 socle 与第二个全局单位除点

日期：2026-11-13。**状态：以下条件定理、整构造及全部相容性已证明。**

本篇使用 O6 的同一 $\pi$ 塔、同一直接字符、原完整类群模和原椭圆单位。主要结论是：如果原严格 Mordell–Weil 字符杀掉类群模的 $\theta$-socle，则原椭圆单位确有第二个全局中心除点，且只需乘一个与层数无关的 $p$ 次幂。该条件不由已知反圆 MW 高度非退化自动给出；在允许的 $q_p\ge3$ 结构中也可能失败。

证明不把单个 Rubin–Stark 值为零升级为整个 Fitting 理想的整除。它先构造原类群模上的真实一阶中心变形，再用该变形证明整赋值行可除，最后收缩原 Rubin–Stark 元素。

## 1. 原对象及准确有限层控制

固定
$$
E:y^2=x^3-17x,\quad K=\mathbf Q(i),\quad
p\ge13,\ p\equiv1\pmod4,\ p\ne17.
$$
记号取自 R32–R36：
$$
K_n=K(E[\pi^n]),\qquad
\Lambda=\mathbf Z_p[[T]],\quad
\rho_E(\gamma)=1+p,\quad T=\gamma-1,\quad\theta=T-p,
$$
$$
A=\mathcal A_p
=\left(\varprojlim_n\operatorname{Cl}(K_n)\otimes\mathbf Z_p\right)^{\widetilde\chi},
\quad A_n=(\operatorname{Cl}(K_n)\otimes\mathbf Z_p)^{\widetilde\chi}.
$$
$\widetilde\chi$ 为直接 Tate 字符。$A$ 为有限生成 $\mathbf Z_p$-模；允许它有有限挠子 $A_{\rm tor}$。本文从不删去该挠子来作有限层识别。

令
$$
\omega_n(T)=(1+T)^{p^{n-1}}-1,\qquad
R_n=\Lambda/(\omega_n),\qquad
S_n=R_n/\theta R_n\simeq\mathbf Z_p/p^n.
$$
R32 §5 使用 Rubin Lemma 11.1 给出本塔的**准确范数控制**
$$
\boxed{\quad A_n\simeq A/\omega_nA.\quad}\tag{1}
$$
其已核条件是：$\mathfrak p$ 在塔中只有一个素位且全分歧，$K_n/K_1$ 在其余素位未分歧。这是完整类群，不是先删去分歧位类的类群商。固定 $\mathcal T=\{(67)\}$ 的射线修正和原有限 $S$-位置项，在直接字符上的消除见 R32 §3。因此以下单位列与 (1) 使用同一个 $A_n$，没有另换 fine Selmer 模。

R35 的两个固定点给原饱和满射
$$
\lambda=\lambda_p:A\twoheadrightarrow\mathbf Z_p,
\qquad \lambda\theta=0.
\tag{2}
$$
其有限层约化 $\lambda_n:A_n\to S_n$ 满射。本文对 $\lambda$ 的条件始终作用于完整 $A$；未知的 Sha 方向仍在其中。

设原单位为 $z_\infty=(z_n)_n$。整单位工作记录已经证明
$$
z_n/\theta\in U_{0,n},\qquad
z_\infty/\theta\in E_\infty^{\widetilde\chi}.
\tag{3}
$$
$U_{0,n}$ 是固定原 $S,\mathcal T$ 全局单位的 $p$-完备化字符格。商在 $\mathbf Q_p\otimes U_{0,n}$ 中唯一，因为 $\theta$ 在 $\mathbf Q_p\otimes R_n$ 中可逆。

## 2. 原 Tor 正是辅助循环类的底层部分

每层按 R35 选择 $w\mid\mathfrak q$，使
$$
\lambda_n(c_w)\in S_n^\times.
$$
记 $W_n=U_{\mathfrak q,n}$，并暂略下标 $n$。原准确列为
$$
0\longrightarrow U_0\longrightarrow W
\xrightarrow{v_w}R\xrightarrow{r\mapsto rc_w}A_n.
\tag{4}
$$
令
$$
I=\operatorname{Ann}_R(c_w),\qquad
C_w=Rc_w,\qquad J=I/\theta=\operatorname{Ann}_R(\theta c_w).
$$
由 $\lambda_n(c_w)$ 为单位，$I\subset\theta R$，故 $I=\theta J$；而
$$
g=v_w/\theta:W\twoheadrightarrow J
$$
为原整泛函。

有准确同构
$$
\boxed{\quad
J/\theta J\xrightarrow{\sim}C_w[\theta],\qquad
r\longmapsto rc_w.
\quad}\tag{5}
$$
其核是 $I=\theta J$，像由 $\theta rc_w=0$ 的定义给出。在这个同构下，$J/\theta J\to S_n$ 的评价是
$$
rc_w\longmapsto
\lambda_n(rc_w)/\lambda_n(c_w).
\tag{6}
$$
特别地，原来不能删除的 Tor 具有实际类群解释
$$
\boxed{\quad
\frac{I\cap\theta^2R}{\theta I}
\xrightarrow{\sim}\theta C_w\cap C_w[\theta],\qquad
\theta^2r\longmapsto\theta r c_w.
\quad}\tag{7}
$$
该映射的核恰为 $\theta I$，满射性由右边的定义直接得到。结合 (4)–(6)，
$$
0\longrightarrow U_0/\theta U_0
\longrightarrow\ker\bar g
\longrightarrow\theta C_w\cap C_w[\theta]
\longrightarrow0,
\tag{8}
$$
$$
\bar g(W/\theta W)
=\lambda_n(C_w[\theta])/\lambda_n(c_w)
\subset S_n.
\tag{9}
$$
式 (7) 保留全部 $p$-primary 类标签，不用半单化代替它。

## 3. 主定理与其具体 Jordan 条件

**定理。** 假设
$$
\boxed{\quad\lambda(A[\theta])=0.\quad}\tag{10}
$$
则存在一个有限整数 $C_p\ge0$，使对全部 $n\ge1$ 都有
$$
\boxed{\quad
p^{C_p}I_{n,w}\subset\theta^2R_n,\qquad
g^{(2)}_{n,w}:=p^{C_p}g_{n,w}/\theta\in W_n^*,
\quad}\tag{11}
$$
并且
$$
\boxed{\quad
v_n:=p^{C_p}z_n/\theta^2\in U_{0,n},\qquad
(v_n)_n\in E_\infty^{\widetilde\chi}.
\quad}\tag{12}
$$
$C_p$ 与 $n,w$ 均无关。各 $v_n$ 不依赖辅助素位、主化单位或变形的选择；它们由 $\theta^2v_n=p^{C_p}z_n$ 唯一指定，且按原范数准确相容。

条件 (10) 有以下完全等价的具体表述。

1. 存在连续 $\mathbf Z_p$-线性映射 $\mu:A\to\mathbf Q_p$，满足
   $$\mu\theta=\lambda.$$
2. $\lambda$ 可提升为 $\Lambda$-线性映射
   $$
   A\longrightarrow\mathbf Q_p[\epsilon]/(\epsilon^2),
   \qquad x\longmapsto\lambda(x)+\epsilon\mu(x),
   \qquad T\mapsto p+\epsilon.
   \tag{13}
   $$
3. 在 $V=A\otimes\mathbf Q_p$ 的 $\theta$-primary Jordan 分解中，$\lambda$ 在所有长度一块上的投影为零。长度至少二的块，其 socle 已包含于 $\theta V$，本来就被 $\lambda$ 杀掉。
4. 存在固定 $C$，使对全部 $n$ 有
   $$p^C\lambda_n(A_n[\theta])=0\quad\text{于 }S_n.$$

这里不是说整个 $\theta$-primary 模没有长度一块；只要求原特定 $\lambda$ 不检测这些块。

### 3.1 有限挠子没有被漏掉

因为 $\lambda$ 的目标无挠，它杀掉 $A_{\rm tor}$。若 $v\in V$ 满足 $\theta v=0$，先乘一个 $p$ 次幂使其来自 $x\in A$；此时 $\theta x$ 可能只是有限挠子。再乘一个杀掉 $A_{\rm tor}$ 的 $p$ 次幂，才得到 $A[\theta]$ 中的元素。由此
$$
\lambda(A[\theta])=0
\quad\Longleftrightarrow\quad
\lambda(\ker(\theta:V\to V))=0.
\tag{14}
$$
不能略去第二次乘法后直接把有理特征向量称为原整类群中的 $\theta$-挠点。

在 (14) 下，先在 $\theta V$ 上定义
$$
\mu(\theta x)=\lambda(x).
$$
它因 (14) 而良定义；把这个有理线性泛函延拓到 $V$，再拉回 $A$，便得到 (13)。它自动杀掉全部有限挠子。反向由 $\mu\theta=\lambda$ 立即给 (10)。式 (13) 的 $\Lambda$-线性只需核 $\theta$：
$$
(\lambda+\epsilon\mu)(\theta x)
=\epsilon\lambda(x)
=\epsilon(\lambda+\epsilon\mu)(x).
$$
幂级数作用由连续性得到。

在 Jordan 块 $\mathbf Q_p[X]/X^r$ 上，$\lambda X=0$，所以 $\lambda$ 只读顶层系数。若 $r\ge2$，核 $\ker X$ 在 $X V$ 中；若 $r=1$，整个块均在核中。这证明表述 3，并说明该条件作用于完整类群结构，不是只看 MW 子空间的秩。

### 3.2 一个可计算的统一分母

在自由格 $A/A_{\rm tor}$ 上把 $\theta$ 写成整数矩阵 $B$，把 $\lambda$ 写成行向量 $l$。取 Smith 形
$$
U B V=\operatorname{diag}(p^{s_1},\ldots,p^{s_r},0,\ldots,0),
\qquad U,V\in\operatorname{GL}_d(\mathbf Z_p).
$$
(10) 恰使 $(lV)_j=0$ 对 $j>r$ 成立。可取
$$
\boxed{\quad
C_p=\max_{1\le j\le r}\{0,s_j-v_p((lV)_j)\},
\quad}\tag{15}
$$
其中 $v_p(0)=+\infty$。确实，令 $\mu U^{-1}$ 的前 $r$ 个坐标为 $(lV)_j/p^{s_j}$，其余为零，便有 $\mu B=l$ 及 $p^{C_p}\mu(A)\subset\mathbf Z_p$。这也给这个 Smith 解的最小统一分母。若 $r=0$，非零满射 $\lambda$ 不可能满足 (10)。

## 4. 一阶中心变形直接给全部有限层的整除

固定一个满足 $\mu\theta=\lambda$、$p^{C_p}\mu(A)\subset\mathbf Z_p$ 的 $\mu$。令
$$
L_{C_p}=\mathbf Z_p\oplus p^{-C_p}\mathbf Z_p\epsilon,
\qquad\epsilon^2=0,
\qquad L_0=\mathbf Z_p[\epsilon]/(\epsilon^2).
$$
$L_{C_p}$ 是环，$p^{C_p}L_{C_p}\subset L_0$，且
$$
\eta:=\lambda+\epsilon\mu:A\longrightarrow L_{C_p}
\tag{16}
$$
是上节已经构造的真实 $\Lambda$-线性映射。

写
$$
a_n=\omega_n(p),\qquad b_n=\omega_n'(p),\qquad
v_p(a_n)=n,
$$
于是 $\omega_n$ 在两个环中的作用均为乘 $a_n+b_n\epsilon$。由准确控制 (1)，(16) 下降为
$$
A_n\longrightarrow L_{C_p}/(a_n+b_n\epsilon)L_{C_p}.
\tag{17}
$$
任取 $c\in A$ 提升 $c_w$。因为 $\lambda_n(c_w)$ 为单位，$\lambda(c)\in\mathbf Z_p^\times$，从而
$$
\eta(c)=\lambda(c)+\epsilon\mu(c)\in L_{C_p}^{\times};
$$
其逆仍在 $L_{C_p}$ 中。这是不能省掉的整环步骤：无需把两个分母各付一次。

若 $i\in I_{n,w}$，取 $\widetilde i\in\Lambda$ 提升，则 $\widetilde i c\in\omega_n A$。作用 (16) 并用 $\eta(c)$ 为上述整环中的单位，得到
$$
\widetilde i(p+\epsilon)
\in(a_n+b_n\epsilon)L_{C_p}.
$$
乘 $p^{C_p}$ 后，右边包含于 $(a_n+b_n\epsilon)L_0$。而
$$
R_n/\theta^2R_n
\simeq L_0/(a_n+b_n\epsilon)L_0.
\tag{18}
$$
所以 $p^{C_p}i\in\theta^2R_n$，证明 (11) 的理想包含。因为 $v_w(W_n)=I_{n,w}$、$g=v_w/\theta$，$p^{C_p}g/\theta$ 在完整的原 $W_n$ 上取整值；不是只对两枚测试单位核整。

### 4.1 原 socle 观察的统一有限精度

同一构造还直接给表述 4。若 $\bar x\in A_n[\theta]$，取 $x,y\in A$ 使
$$
\theta x=\omega_n y.
$$
作用 $\lambda$ 得 $0=a_n\lambda(y)$，故 $\lambda(y)=0$。再作用 $\mu$，得到
$$
\lambda(x)=a_n\mu(y)+b_n\lambda(y)=a_n\mu(y).
$$
于是 $p^{C_p}\lambda(x)\in a_n\mathbf Z_p=p^n\mathbf Z_p$，即
$$
p^{C_p}\lambda_n(A_n[\theta])=0.
\tag{19}
$$
反过来，若一个固定 $C$ 对全部层满足 (19)，把任意 $x\in A[\theta]$ 约化到各层，便得 $p^C\lambda(x)\in p^n\mathbf Z_p$ 对所有 $n$ 成立，故 $\lambda(x)=0$。这证明全部等价。

结合 (9)，(19) 也直接说明为何 $p^{C_p}\bar g=0$，但 (16)–(18) 同时保留了产生整除的实际变形。

## 5. 收缩原 Rubin–Stark 元素给全局单位，并自动兼容范数

保持 R35 的位置顺序 $[\infty,\mathfrak q]$。选原主化单位 $z_w$，使 $v_w(z_w)=h$。原元素为
$$
\epsilon_{2,n,w}=\frac{u_n}{h}\,z_n\wedge z_w
\in\bigcap_{R_n}^2W_n,
\qquad u_n\in R_n^\times.
\tag{20}
$$
已出版 Bley–BKS 输入在 R32–R35 给出这里的完整整性；$R_n$ 对称群环的双对偶识别给 $\bigcap_{R_n}^1W_n=W_n$，详见整单位工作记录 §2。

使用已在整个 $W_n$ 上证明整的 $g^{(2)}_{n,w}$ 收缩。由于 $v_w(z_n)=0$，BKS 的原符号约定给
$$
\begin{aligned}
i_{g^{(2)}_{n,w}}\epsilon_{2,n,w}
&=\frac{u_n}{h}
\left(g^{(2)}(z_n)z_w-g^{(2)}(z_w)z_n\right)\\
&=-u_n\,\frac{p^{C_p}z_n}{\theta^2}\in W_n.
\end{aligned}
\tag{21}
$$
其 $v_w$ 为零，故由原准确列 (4)，(21) 的单位商属于 $U_{0,n}$。这证明 (12) 的整性。

最后必须核相容性，而不只逐层选解。$\theta$ 在 $\mathbf Q_p\otimes R_n$ 上的每个有限字符处取值为 $\zeta-(1+p)\ne0$，所以 $\theta^2$ 在 $\mathbf Q_p\otimes U_{0,n}$ 上可逆。式 (21) 得到的元素因此是唯一的 $p^{C_p}z_n/\theta^2$。原范数 $N_{m/n}$ 与 $\theta$ 作用交换，且 $N_{m/n}z_m=z_n$，故
$$
\theta^2 N_{m/n}v_m=p^{C_p}z_n=\theta^2v_n
\quad\Longrightarrow\quad N_{m/n}v_m=v_n.
\tag{22}
$$
不同辅助素数、不同主化单位以及不同的 $\mu$（取同一个有效 $C_p$）均得到同一唯一元素。不存在额外的逐层选解相容性假设。

## 6. Tor 上剩余的局部观察可以用原主化单位准确计算

本节不假设 (10)。记原整泛函 $f=p^{b_p}\mathcal L_n/\theta$，并令
$$
\mathfrak a_{f,n}=\bar f(U_{0,n})\subset S_n.
$$
对 $t\in\theta C_w\cap C_w[\theta]$，写 $t=\theta r c_w$，故 $\theta^2r\in I$。由原单位列取一个 $u_r\in W_n$，满足
$$
v_w(u_r)=\theta^2r.
$$
则
$$
\boxed{\quad
\mathfrak t_f(t)=\bar f(u_r)\bmod\mathfrak a_{f,n}
\in S_n/\mathfrak a_{f,n}
\quad}\tag{23}
$$
是良定义的 $S_n$-线性映射。改变 $u_r$ 加上 $U_0$ 不改变该商值；若改变代表使 $\theta^2(r'-r)\in\theta I$，可取 $v\in W$ 满足 $v_w(v)=\theta(r'-r)$，于是 $u_{r'}-u_r-\theta v\in U_0$，仍不改变 (23)。其像准确为
$$
\operatorname{im}\mathfrak t_f
=\bar f(\ker\bar g)/\bar f(U_0).
\tag{24}
$$

这里还可给不在有限群环中作形式微分的明确取值式。令 $L_r(T)$ 是 $\mathcal L_n(u_r)$ 的次数小于 $p^{n-1}$ 的唯一多项式代表。原 $f$ 整性使
$$
q_r:=\frac{p^{b_p}L_r(p)}{\omega_n(p)}\in\mathbf Z_p.
$$
在 $\mathbf Z_p[T]$ 中先除以 $T-p$，随后才评价，得到
$$
\boxed{\quad
\bar f(u_r)
=p^{b_p}L_r'(p)-q_r\omega_n'(p)\pmod{p^n}.
\quad}\tag{25}
$$
证明是 $p^{b_p}L_r-q_r\omega_n$ 在 $T=p$ 为零，且其商在 $R_n$ 中就是 $f(u_r)$。式 (25) 的第二项不可删除。它给出 (7) 的原 Tor 的实际 principalization 观察，而不是假设这个 Tor 已经消失。

## 7. 更高除法的准确条件

同一论证可迭代，但条件必须相应加强。对 $k\ge1$，存在
$$
\eta_k=\lambda+\mu_1\epsilon+\cdots+\mu_k\epsilon^k:
A\longrightarrow\mathbf Q_p[\epsilon]/(\epsilon^{k+1}),
\qquad T=p+\epsilon,
\tag{26}
$$
当且仅当
$$
\lambda(\ker(\theta^k:V\to V))=0;
\tag{27}
$$
亦即 $\lambda$ 避开全部长度不超过 $k$ 的 $\theta$-Jordan 块。其系数关系是 $\mu_1\theta=\lambda$、$\mu_j\theta=\mu_{j-1}$。逐块直接求解证明此等价，全部有限挠子仍映到零。

选 $C\ge0$ 使 $p^{jC}\mu_j(A)\subset\mathbf Z_p$。环
$$
L_{C,k}=\bigoplus_{j=0}^k p^{-jC}\mathbf Z_p\epsilon^j
$$
对乘法封闭，$\eta_k(c)$ 的常数项为单位，所以它在该环中可逆。重复 §4，并使用 $p^{kC}L_{C,k}\subset\mathbf Z_p[\epsilon]/\epsilon^{k+1}$，得到
$$
p^{kC}I_{n,w}\subset\theta^{k+1}R_n.
$$
收缩 $p^{kC}g/\theta^k$ 随即给
$$
\boxed{\quad
p^{kC}z_n/\theta^{k+1}\in U_{0,n},
\quad\text{且按原范数相容}.
\quad}\tag{28}
$$
因此第三个全局除点要求 $\lambda$ 也避开长度二块；不能从 (10) 自动再除一次。

## 8. 已知反圆高度及坏 Sha 情形都没有自动支付 (10)

先有一个本课题中的实际检查。若 (10) 成立，由 (12) 及原 $\mathcal L_n(z_n)=\theta^2G_{p,n}$，得到 $\mathcal L_n(v_n)=p^{C_p}G_{p,n}$。R36 的 $p^{b_p}\mathcal L_n/\theta$ 在全部原全局单位上整，所以对所有 $n$，
$$
p^{b_p+C_p}G_p(p)\equiv0\pmod{p^n}.
$$
故
$$
\boxed{\quad (10)\ \Longrightarrow\ G_p(p)=0.\quad}\tag{29}
$$
R36 的真实 $p=13$ 非零证书给 $G_{13}(13)\ne0$，所以该处原 $\lambda(A[\theta])\ne0$。秩二及 R37–R40 的反圆 MW 非退化在该处均已成立。因此那些已知输入不能直接推出本篇的 (10)。R40 §3.1 也明确区分反圆方向与本篇单 $\pi$ 塔的 $T=p$。

在需要排除的 $q_p\ge3$ 情形，(10) 同样不是已付结构的形式推论。一个具体允许的 $\theta$-primary 模结构是
$$
A=\bigl(\Lambda/(\theta)\bigr)^3,\qquad
M=\bigl(\Lambda/(\theta)\bigr)^4,
\qquad B=\Lambda/(\theta)\subset M,
\tag{30}
$$
其中 $M/B=A$，$\lambda$ 为 $A$ 的第一坐标。则 $q_p=3$、$s_{\infty,p}=4$，$N_p\simeq\mathbf Z_p^2$，恰保留余秩二的潜在 Sha；parity 和 R34 的局部秩一中心注入都成立。可是 $A[\theta]=A$、$\lambda(A[\theta])=\mathbf Z_p$，故 (10) 失败。

这个结构也允许完整四维反圆交替高度有一个非退化二维 MW 块和一个二维剩余块；已知 MW 块非退化并不排除它。本文仅把 (30) 作为已付模结构仍允许的模型，不声称它在某个实际素数实现。它说明从“坏 Sha 的余秩至少二”直接推出 $\lambda$ 避开长度一块，确实还缺新的算术证明。

例如取局部单位模 $U=\Lambda u$、全局单位像 $E=\theta\Lambda u$ 和 $z=\theta^4u$，则 $U/E=B$、$\operatorname{char}(E/\Lambda z)=\theta^3=\operatorname{char}A$。这同时保留原指数与完整主猜想的特征理想结构。坏情形下由完整 Fitting 已得的第三次全局整除可以存在，即使特定 $\lambda$ 的一阶变形不存在；不能把两条机制混为一条。

因此本篇确实支付了新的条件全局除点及其全部整数相容性，但还没有证明对无穷多个 $p$ 的原始性，也没有排除 (30)。下一步若用这条路线处理坏情形，必须实质控制原 $\lambda$ 在实际长度一、二块上的分量，或给原单位另外的非零输入。

## 来源与依赖

- R32 §3、§5：固定射线修正、完整类群、准确范数控制及已出版 Bley–BKS 整性输入。
- R34–R36：原严格 MW 字符、辅助素数选择、全局 Kummer–Artin 互反、原整泛函及 $p=13$ 非零证书。
- [O6 整单位记录](../notes/2026-11-13-o6-integral-unit-division-and-one-prime-mrs-descent.md)：对称群环双对偶、原 Rubin–Stark 收缩、一次全局中心除法及原 Tor。
- R40：完整 Selmer 与潜在 Sha 的反圆高度块，以及与单 $\pi$ 方向的准确区别。
