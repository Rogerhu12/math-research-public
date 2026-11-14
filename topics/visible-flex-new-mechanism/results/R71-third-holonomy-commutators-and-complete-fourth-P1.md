# R71：零矩桥的第三 holonomy：准确 P1 公式、可达交换子与真实有限控制

日期：2026-11-14。本文承接 [R70](R70-zero-matrix-bridges-and-affine-complete-fourth-period.md)，倒行端口依 [R45](R45-reversal-four-block-third-period-cancellation.md)，纯局部 drift 依 [R65](R65-reciprocal-pure-fourth-drift-complex-uniqueness.md)。来源审查代理已独立核对全部 P1 符号、倒行、第三 composition、准确交换子词及最后的积分例。没有新的真实几何/profile 评价。结论是实际平滑控制路径及其第三、第四形式 range 身份，尚非有限等距族。

## 1. 保留的第三历史不是零

采用同一个紧区间 I、同一右 collar 锚，并假定所有真实路径全程 $h>0,\xi+\omega\geq\delta>0$。桥端具有常值 germ。对任意同右 collar 为零的 profiles 定义

$$Z_{\mathcal B}(g,h)=\mathcal I_{\mathcal B}H(Y_g,Y_h),$$

其中第二 scalar 原函数在该桥的 s 起点为零；正常分量仍由真实右 xi 锚恢复，不在左 collar 清零。定义第三算子

$$\boxed{\mathcal T_{\mathcal B}(f;g,h)
=\int_{\mathcal B}R\!\left(H(Y_f,Z_{\mathcal B}(g,h))\right)\,ds.} \tag{1}$$

它对三个输入线性，后两个输入对称，但不预先假设对第一个输入也对称。积分和原函数均来自同一真实桥，不可逐局部常段另选常数。

即使桥的二阶矩阵 M=0，(1) 一般仍不为零。这是仿射第四周期里必须保留的 $U_0$ 记忆。本文准确给出它怎样进入 P1，再给一个实际可调的第三算子族。

## 2. 全相位 P1 对内部桥的准确依赖

固定目标 $g_X+\varepsilon^2dY_f^2$，令 $\phi=\cos\theta f+\sin\theta g$。把一对互反常态的正段积分算子记为 $\mathcal A=\ell r$，负段为 $-\mathcal A$；两段之间是一座真实 M=0 桥。记

$$a=\mathcal A(f,f)-\mathcal A(\phi,\phi),\qquad
Z_D=Z_{\mathcal B}(f,f)-Z_{\mathcal B}(\phi,\phi).$$

上一命题已给桥前后 $W_0=U_1=0$，而最高第二历史在内部桥上为 $w=a$。桥上的场按 N 展开为

$$Z_2=Z_D-NY_w,$$

$$Z_3=Z_{3,0}+2N Z_{\mathcal B}(\phi,w)-N^2Y_v.$$

这里 $Z_{3,0}$ 含真实第三入历史，不能置零。不过它只进入 N 零次 forcing，不进入桥的 P1 密度。因此桥直接贡献

$$2\mathcal T_{\mathcal B}(w;f,f)
-2\mathcal T_{\mathcal B}(w;\phi,\phi)
-4\mathcal T_{\mathcal B}(\phi;\phi,w). \tag{2}$$

桥的第三 scalar 跳变量是

$$C_{\mathcal B}=-2\mathcal T_{\mathcal B}(\phi;f,f)
+2\mathcal T_{\mathcal B}(\phi;\phi,\phi). \tag{3}$$

在两个 bulk 中，常态完整 drift 分解为

$$R_4=-r(W,W)+2r(\phi,U)+J(f,\phi).$$

任意进入 pair 的 $U_0$ 在 $+\mathcal A,-\mathcal A$ 的两个积分中相消；内部桥新增的 (3) 只进入负半段，贡献 $-2\mathcal A(\phi,C_{\mathcal B})$。故该 pair 的完整 P1 是

$$\boxed{\begin{aligned}
P_{1,\rm pair}={}&\ell\{J_+(f,\phi)+J_-(f,\phi)\}\\
&+2\mathcal T_{\mathcal B}(a;f,f)
-2\mathcal T_{\mathcal B}(a;\phi,\phi)
-4\mathcal T_{\mathcal B}(\phi;\phi,a)\\
&+4\mathcal A\!\left(\phi,\mathcal T_{\mathcal B}(\phi;f,f)
-\mathcal T_{\mathcal B}(\phi;\phi,\phi)\right).
\end{aligned}} \tag{4}$$

每项均使用同一个全局 profile、同一物理 xi 和真实内部桥。位于相邻 pair 之间的 M=0 桥虽会改变入 $U_0$，但该入值在下一个完整 pair 中相消；在这些外部桥上 w=v=0，直接 P1 也为零。因此 P1 的桥调节集中在每个正/负段之间的第三算子，不能以“所有桥 M=0”代替它们。

式 (4) 不处理 P0：桥的第四本地历史和前面第三入值在 P0 中仍可出现。

## 3. 纯模式可用 cubic diagonal 表示

在纯 $-4$ 规范

$$B=\mathcal I H(Y_q,Y_q),\quad U=\mathcal I H(Y_q,B),\quad
H_{4,-4}=-H(B,B)/16-H(Y_q,U)/4$$

下，设 $a=\mathcal A(q,q)$，并记

$$\tau_{\mathcal B}(q)=\mathcal T_{\mathcal B}(q;q,q).$$

桥的 N 一次项为 $\mathcal T(a;q,q)/8+\mathcal T(q;q,a)/4$，负 bulk 的第三历史项为 $-\mathcal A(q,\tau(q))/4$。于是

$$\boxed{P_{1,-4,\rm pair}
=\frac{\ell}{16}\mathcal P_{\rm reciprocal}[q]
+\frac18\{D\tau(q)[\mathcal A(q,q)]-2\mathcal A(q,\tau(q))\}.} \tag{5}$$

其中 $\mathcal P_{\rm reciprocal}$ 是 R65 的真实两态局部 drift；一般 $(h,d)$ 先按 R62 的共同 profile 变换到标准坐标，不能直接换一份独立 profile。第二项的准确含义是

$$D\tau(q)[a]=\mathcal T(a;q,q)+2\mathcal T(q;q,a).$$

它是 quadratic 向量场 $\mathcal A(q,q)$ 与 cubic 向量场 $\tau(q)$ 的 Lie bracket（按 (5) 的符号）除以 8。这个名称只表示已写出的导数恒等式，不预设其像足以抵消局部 drift。

若倒行整座 M=0 桥，同右/起点规范下第二恢复场为偶，Y 为奇，因此

$$\mathcal T_{\mathcal B^{\rm rev}}=-\mathcal T_{\mathcal B}. \tag{6}$$

这里必须使用 R45 的**同 k 倒行**。对第 5 节首末 frame 均为 I、首末同一常值标量状态的环，令 $D=\operatorname{diag}(-1,1,-1)$、长度为 L、末位移为 V，则实际归一化倒行是

$F^{\rm rev}(s)=D F(L-s)D,\qquad
\alpha^{\rm rev}(s)=D\{\alpha(L-s)-V\},$

$k^{\rm rev}(s)=k(L-s),\quad h^{\rm rev}(s)=h(L-s),\quad
\omega^{\rm rev}(s)=\omega(L-s). \tag{6a}$

因为 $D\Omega(k)D=-\Omega(k)$，(6a) 满足真实 frame 方程，首末都为 I；标量端态也保持，任意常值 k 均可直接平滑拼接，无须另要求 k=0。它同时满足 $\omega_s^{\rm rev}=k_s^{\rm rev}/(2h^{\rm rev})$。此时 $Y^{\rm rev}=-D\,Y\circ{\rm rev}$，在 M=0 与同锚条件下 $Z^{\rm rev}=D\,Z\circ{\rm rev}$，准确给 (6)。这不是会把 k 翻号的另一种参数倒行。

同时反向 pair 的 $\mathcal A,a$ 取负，故 (4)、(5) 均保持不变。每个 pair 的任意入 $U_0$ 已直接相消，因而完整 R45 四块的 P1 是四份对应单 P 函数的和；相同反转构造时为四倍。这没有借用尚未支付的有限 N collar/ruling 条件。

## 4. 任意二阶矩路径的真实第三 composition

上一桥存在命题允许指定 frame I、同一标量常态的两端，以及任意有限无迹目标 M。由同端参数 IFT 可在目标的小邻域光滑选择这样一族真实桥，h 保持正；起点位置可以整体平移，终点位移不被指定。

对这些非零 M 的中间路径，也定义 (1)。令 $\Phi_i$ 是第 i 条路径的完整 second 算子。两路径连接时，第二路径继承第一路径留下的 scalar $\Phi_1(g,h)$，因此其第二场准确多出 $-Y_{\Phi_1(g,h)}$。于是

$$\boxed{\mathcal T_{21}(f;g,h)
=\mathcal T_1(f;g,h)+\mathcal T_2(f;g,h)
-\Phi_2(f,\Phi_1(g,h)).} \tag{7}$$

对有序词得到

$$\mathcal T_{\rm word}
=\sum_i\mathcal T_i
-\sum_{i>j}\Phi_i(f,\Phi_j(g,h)). \tag{8}$$

这已经包含前段所有真实第二记忆，不是把每段重锚后直接相加。特别地，若每段自身 M=0，则 (7) 退化为第三算子的准确加法。

## 5. 一个准确可调交换子环

取无迹矩阵 P,Q，仍用同名表示其 second 算子 $\Phi_P,\Phi_Q$。选择以下真实路径，均从同一标量常态与 frame I 回到该常态和 frame I：

- 一条光滑族 $A(t)$，其矩阵准确为 tP；
- 一条固定路径 B，矩阵为 Q；
- 一条固定路径 C，矩阵为 $-Q$。

这些路径及全部辅助圈数先由任意目标桥命题构造并冻结；t 在固定小区间内，使用同一个端点 family，而不是在 $t$ 和 $-t$ 处独立选择两条无关解。对这个紧参数区间选择共同物理 I。

定义真实词

$$W(t)=A(t)\,B\,A(-t)\,C.$$

它的总矩阵准确为零、frame 为 I、标量端态保持。式 (8) 中路径自身项

$$\mathcal T_{A(t)}+\mathcal T_{A(-t)}
+\mathcal T_B+\mathcal T_C$$

是 t 的偶函数。交叉项的奇部准确为

$$t\{P(f,Q(g,h))-Q(f,P(g,h))\}.$$

故

$$\mathcal T_{W(t)}-\mathcal T_{W(-t)}
=2t\{P(f,Q(g,h))-Q(f,P(g,h))\}. \tag{9}$$

现在把 W(t) 接上 W(-t) 的**真实倒行**。后者整体 M=0，所以可合法应用 (6)。这给一条实际平滑环 $\mathcal L(t)$，满足 frame I、同一 scalar 端状态、M=0，且

$$\boxed{\mathcal T_{\mathcal L(t)}(f;g,h)
=2t\{P(f,Q(g,h))-Q(f,P(g,h))\}.} \tag{10}$$

这是有限路径的准确身份，无大圈数极限，也没有 O(t²) 或 O(L) 未付项。未知的各路径第三成本因采用同一 $A(t)$ 的对称词和真实倒行而准确消去。其空间位移一般非零，但可插入 R45 的单 P 并由同一个修改后 P 的四块结构支付全局位移闭合。

可以把这种 M=0 环插入任意内部桥的同态常值 germ；原桥 M、frame 和 scalar 两端不变，而第三算子准确增加 (10)。对八个矩阵基两两选择，可串联得到它们交换子所张成的真实可达线性空间，维数**至多 28**。没有宣称这些算子一定独立，也没有把这个可达空间冒称为全部待付 P1 函数空间。

## 6. 一个严格非零、完全显式的方向

取两个实际无迹矩阵坐标：第一个仅 $r_0=1$，第二个仅 $r_1=1$。相应 second 算子为

$$P(f,g)=\int_\xi^r f''g'',\qquad
Q(f,g)=f'g'+\xi\int_\xi^r f''g''. \tag{11}$$

对右 collar 为零的光滑 q，设 $J=\int_\xi^r(q'')^2$。则

$$P(q,q)=J,\qquad Q(q,q)=q'^2+\xi J,$$

$$J''=-2q''q''',\qquad
(q'^2+\xi J)''=2(q'-\xi q'')q''' .$$

直接分部积分，所有右端项因 collar 为零而消失，得到

$$\boxed{P(q,Q(q,q))-Q(q,P(q,q))
=-\frac13\int_\xi^r(q'')^3.} \tag{12}$$

例如第一项等于
$-q'(q'')^2+2\xi(q'')^3/3-\int_\xi^r(q'')^3/3$，
第二项等于前面的两个局部项，差即 (12)。

所以准确交换子环实现

$$\tau_{\mathcal L(t)}(q)=-\frac{2t}{3}\int_\xi^r(q'')^3. \tag{13}$$

对任意非零的同右 collar q，右侧作为 xi 函数不恒零：若其恒零，求一次导数给 $(q'')^3=0$，故 $q''=0$；结合右端零值和零一阶导数得 q=0。这个论证对复 q 同样成立，不使用普通复平方的正性。

因此第三控制空间并非只是形式上可能非零。式 (13) 是一个由真实有限平滑路径实现的明确连续方向。

## 7. 接下来能准确求解的有限问题及范围

用固定有限 basis 写 (10) 的至多 28 个第三控制方向后，式 (4)、(5) 给每个内部桥对完整 P1 的真实线性响应。对于已经选定的共同 profile，可以构造这些**整个函数**的 Gram 核及线性匹配问题；必须保留可能的函数依赖，不能把分离表达式各系数必须为零当成必要条件。

仍需判断固定局部 drift 和基准桥的第三算子在这个响应空间中能否共同匹配。目前没有证明全函数满射，没有给使 P1 或 P0 为零的参数，也没有支付第四 ruling、完整高阶或收敛。加入交换子环会改变 P0，不能在解决 P1 时把这项当作不变。

任意目标桥的辅助整圈可能很长；这些环没有宏观厚度或嵌入保证。本文支付的是先前未知的真实第三可调性和它进入 P1 的完整公式，而不是主课题完成条件。
