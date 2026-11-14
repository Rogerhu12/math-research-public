# R81：纯模式不可见、混合模式非零的真实第三控制

日期：2026-11-14。**已证明。** 本文由纸面分部积分与端尾展开得到，没有运行新的研究数值或完整符号目标。承接 [R71](R71-third-holonomy-commutators-and-complete-fourth-P1.md) 的真实有限交换子环、[R78](R78-complete-phase-P1-symmetric-square-conditions.md) 的完整相位条件和 [R39](R39-explicit-moment-circle-and-third-order-range.md) 的三矩圆。

结论是一个明确的真实控制方向：它对所有 profile 的纯 $-4$ 模式准确无作用，却对某些严格三矩配平的 $C^\infty$ profile 圆产生非零的 $-2$ 响应。它可以在保住已经支付的纯模式时用于调节另一模式，但尚未证明这一条方向或所有此类方向足以支付完整第四条件。

## 1. 三个二次算子与真实可达组合

全部 profile 使用同一个紧区间 $I=[l,r]\Subset(1,\infty)$，在右 collar 恒为零。记正右积分为

$$J(F)(x)=\int_x^r F(\eta)\,d\eta,\qquad J(F)'=-F.$$

采用 R71 的三个真实无迹矩阵算子

$$P(a,b)=J(a''b''),\qquad
R(a,b)=a'b'+xJ(a''b''),\qquad
S(a,b)=J(\eta a''b''). \tag{1}$$

它们分别是 $r_0,r_1,s_0$ 坐标。对任意两个这样的对称双线性算子定义完整第三交换子

$$[P,Q](a;b,c)=P(a,Q(b,c))-Q(a,P(b,c)).$$

外槽 $a$ 保持独立。定义

$$\boxed{\mathfrak H=[P,S]-3[P,R].} \tag{2}$$

R71 的准确有限真环分别实现两个交换子。因此任意固定有限实数 $\lambda$ 都能由有限个小参数环的连接实现

$$\Delta\mathcal T=\lambda\mathfrak H,$$

并保持原桥 scalar/frame 端口与 $M=0$。这里 $\lambda$ 是构造桥的设计参数，不是最终弯曲相位。大幅值用有限复制局部小环，不假定单个局部 IFT 族允许任意参数。位置终值仍自由；它与主课题嵌入/reach 无关。

## 2. 对角恒零，但完整算子不为零

对任意实或复光滑 $q$，令 $p=q''$。直接分部积分，所有右边界因共同 collar 消失，得

$$P(q,S(q,q))=\frac{2x}{3}p^3-\frac13J(p^3),$$

$$S(q,P(q,q))=\frac{2x}{3}p^3+\frac23J(p^3).$$

故 $[P,S](q;q,q)=-J(p^3)$。R71 同一锚的恒等式为 $[P,R](q;q,q)=-J(p^3)/3$，于是

$$\boxed{\mathfrak H(q;q,q)=0\quad\text{对全部 }q.} \tag{3}$$

由于内槽对称，普通三次极化给

$$\mathfrak H(a;b,c)+\mathfrak H(b;c,a)+\mathfrak H(c;a,b)=0. \tag{4}$$

这只说明其全对称部分为零，并不说明完整第三算子为零。事实上，取非零的内部 profiles $b,c$，再取右 collar 为零的 $a$，使其在 $b,c$ 支撑的共同邻域内是斜率 $C\ne0$ 的仿射函数。令 $Q=S-3R$，则

$$Q(b,c)''=-b''c''+2x(b'''c''+b''c''')-3(b'''c'+b'c'''),$$

$$P(b,c)''=-(b'''c''+b''c''').$$

两者的二阶导数都支撑在该共同邻域。这里 $a''=0$，所以 $P(a,Q(b,c))=P(a,P(b,c))=S(a,P(b,c))=0$，剩下 $Q$ 的局部项给

$$\boxed{\mathfrak H(a;b,c)=-3C\,b''c''.} \tag{5}$$

取 $b=c\ne0$ 即见非零。这一外槽自由度确由真实有限控制实现，不是仅在形式任意三次张量中存在。

## 3. 对全部纯模式准确无作用

R71 的纯模式响应只依赖对角三次函数 $\tau(q)=\mathcal T(q;q,q)$：

$$\Delta P_{1,-4}=\frac18\{D\tau(q)[\mathcal A(q,q)]-2\mathcal A(q,\tau(q))\}.$$

由 (3)，加入任意 $\lambda\mathfrak H$ 都使该响应严格为零。此结论对**所有**同右 collar 的复 $q$ 成立，不只是某个采样 profile，也没有改变原来纯模式的系数。

以下在标准常态 $h=1,d=0,k=\pm1$ 下使用正段单位时间算子

$$\mathcal A(f,f)=\frac x2f^2-\frac{1+x^2}{2}ff'
+\frac{x(1+x^2)}4f'^2
+\frac{x^2-1}{8}J\bigl((1+\eta^2)f''^2+2f'^2\bigr). \tag{6}$$

整体 $P_1$ 已除去公共正 bulk 时间；恢复该时间只乘一个非零常数。

## 4. 右尾上的混合模式准确公式

取 R78 的固定目标 $F=f^2$ 与圆 $\phi_\theta=\cos\theta f+\sin\theta g$。假设在某个查询点 $x$ 及其整个右区间 $[x,r]$ 上 $g=0$。全部算子 (1)、(6) 和其复合都只使用右尾与局部导数，因此在这个查询点可准确以 $g=0$ 计算，而不影响 $x$ 左侧其他 profiles。

此时 $D_\theta=\sin^2\theta f^2$。对控制 $\mathfrak H$，R78 给

$$\Delta\mathcal K(f^2,f^2)=2\mathfrak H(\mathcal A(f,f);f,f).$$

由 (3)、(4)，

$$\begin{aligned}
\Delta\mathcal L(f^2,f^2)
&=-4\mathfrak H(f;f,\mathcal A(f,f))
+4\mathcal A(f,\mathfrak H(f;f,f))\\
&=2\mathfrak H(\mathcal A(f,f);f,f).
\end{aligned}$$

于是整个相位响应恰为

$$\boxed{\Delta P_1(\theta,x)
=2\sin^2\theta\,\mathfrak H(\mathcal A(f,f);f,f)(x).} \tag{7}$$

在 $\zeta=e^{-i\theta}$ 规范下，$\sin^2\theta=(2-\zeta^2-\zeta^{-2})/4$，所以

$$\boxed{\Delta P_{1,-2}(x)
=-\frac12\mathfrak H(\mathcal A(f,f);f,f)(x).} \tag{8}$$

式 (7) 的常数模式同步改变，从而 $\theta=0$ 的准确种子仍保持；没有把常数模式当独立参数丢掉。

## 5. 一个严格非零的右尾计算

为产生可复核非零例，先取一个足够光滑的有限幂尾

$$f(x)=B(c-x)^m+O((c-x)^{m+1}),\qquad m\ge8,\quad B\ne0,\quad c>1,$$

在 $x\ge c$ 外延零，并使前若干导数具有相应展开。暂用这种 $C^{m-1}$ 紧支撑函数；下一节以 $C^3$ 连续性升级为共同 $C^\infty$ 三矩圆。

置 $t=c-x$、$Q_c=1+c^2$、$L_c=c^2-1$。由 (6)，最低阶项来自右尾积分，准确为

$$\mathcal A(f,f)
=\frac{L_cQ_c B^2m^2(m-1)^2}{8(2m-3)}t^{2m-3}
+O(t^{2m-2}). \tag{9}$$

下面给出所用三次算子的精确幂次系数，不靠符号软件判断其符号。对 $q=t^m$、$a=A_*t^n$，$m,n\ge3$，(1)–(2) 直接给

$$\boxed{\mathfrak H(a;q,q)
=-\frac{2A_* n m^2(m-1)(n-m)(2m-5)(n+3m-7)}
{(n+2m-5)(n+2m-6)}\,t^{n+2m-5}.} \tag{10}$$

**核对 (10)。** 在右尾取 $x=c-t$。写 $Q=S-3R$，其中 $-2cP$ 与 $P$ 的交换子为零，因此可改用

$$\widetilde Q(a,b)=3tP(a,b)-3a'b'-J((c-\eta)a''b'').$$

对任意幂 $t^u,t^v$，

$$P(t^u,t^v)=\frac{u(u-1)v(v-1)}{u+v-3}t^{u+v-3},$$

$$\widetilde Q(t^u,t^v)
=uv\left\{\frac{3(u-1)(v-1)}{u+v-3}-3
-\frac{(u-1)(v-1)}{u+v-2}\right\}t^{u+v-2}.$$

代入 $P(a,\widetilde Q(q,q))-\widetilde Q(a,P(q,q))$，通分后得到 (10)。这些只是右端为零的幂积分，$c$ 项的交换抵消已显式保留。

取 $n=2m-3$，把 (9) 的系数和 $f$ 的幅值代入 (10)，再用 (8)，得到

$$\boxed{\begin{aligned}
\Delta P_{1,-2}(x)
={}&\frac{5L_cQ_c B^4m^4(m-1)^3(m-3)(2m-5)}{32(4m-9)}\,
t^{4m-8}\\
&+O(t^{4m-7}).
\end{aligned}} \tag{11}$$

所有主系数因子严格为正。故该响应在足够靠近右端但仍位于支撑内部的点严格非零。这里不是将普通复平方当正模平方：本节选的是实有限幂尾，非零来自明确的有理系数。

## 6. 非零响应可同时满足全部三矩圆条件

非零例不必停在 $g=0$ 的退化平面。取偶函数

$$\eta_0(x)=(\delta^2-x^2)^m\quad(|x|<\delta),\qquad0\quad(|x|\ge\delta),$$

其中 $m\ge8$，$\delta<1/10$。按 R39 取

$$b_j(x)=\eta_0(x-j)+\eta_0(x+j),$$

$$f=\sqrt{19/30}\,b_1+\sqrt{11/30}\,b_4,
\qquad g=(b_2+b_3)/\sqrt2. \tag{12}$$

共同平移、正缩放，使全部支撑落入 $I\Subset(1,\infty)$ 并保留双侧开放 collar。由于所有 bump 同形且成偶对，R39 的平移恒等式逐字适用：$I_0,I_1,I_2^*$ 的两条对角值相等，三个交叉值为零。$f,g$ 线性独立。

最右侧的 packet 只属于 $f$；其右端附近 $g$ 在全部右尾恒零，$f$ 是满足第 5 节假设的非零 $m$ 次尾。所以 (11) 在那里给严格非零。

再以共同的偶 $C^\infty$ 紧支撑函数 $\eta_j$ 在 $C^3$ 中逼近 $\eta_0$，支撑只略放大并保持八个 packet 分离。对每个 $j$，仍用**同一** $\eta_j$ 形成 (12)，所以三矩与交叉零矩仍准确成立，并非数值重新配平。

取 (11) 给出的一个固定内部非零点。映射

$$f\longmapsto\mathfrak H(\mathcal A(f,f);f,f)(x)$$

在固定区间的 $C^3$ 拓扑中连续：原式 (1)、(2) 只需 $\mathcal A(f,f)$ 的两阶导数和 $f$ 的三阶导数，右积分是有界线性算子；(6) 的两阶导数也只需 $f$ 到三阶。故充分大 $j$ 的响应在该点仍非零。最右 packet 与 $g$ 的右尾分离也保持。

这样得到真正 $C^\infty$、严格三矩配平的非退化 profile 圆，并有一个真实有限控制方向，使纯模式对全部 profiles 恒不变而混合模式确实改变。

## 7. 使用范围

本结果把 R78 留下的额外槽自由度具体化为 R71 已实现的控制，而不是额外假定任意第三张量可达。它可以与已经支付纯模式的桥叠加；$-4$ 身份严格保留，$-2$ 响应按实际同一个参数线性变化。

没有证明单个参数可抵消任意未付的 $-2$ 函数，也没有证明全部 hook 响应覆盖所需函数空间。添加这条环还会改变 $P_0$，不能据此宣布完整第四 range、连续有限等距族、嵌入或 reach 已完成。完整外槽 producer 的实际联合消元仍需保留这些范围。
