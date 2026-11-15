# R199：在全部 universal pure 成本空间上忠实的单调末 step 与新的合法 R183 圆

日期：2026-11-15。**完整纸面构造；无新 profile 评价、积分或研究编译。** 推导与整理：tail_cost。本文使用 [R96](R96-single-profile-faithfulness-for-affine-Volterra-spaces.md)、[R105](R105-finite-canonical-fourth-cost-space-and-response-quotient.md)、[R183](R183-overlapping-derivative-packet-circle-invisible-to-third-hook.md) 和 [R198](R198-rightmost-single-profile-period-obstruction-under-all-second-gauges.md) 的已付定义与 range 证明，对本文结论负责。

本稿构造的是**一个新的**合法 R183 profile 圆。它没有声称先前冻结的具体 step 已忠实，也没有把只在权零成立的评价当作整个成本空间的读出。新 step 同时检测所有真权的 universal pure 像。

## 1. 精确结论

令

$$
\pi:U=\mathcal U_4\longrightarrow\mathcal P,\qquad
\pi V=V_{-4},\qquad
\mathcal P=\pi(U),
\tag{1}
$$

其中 pure 输入 q 可以取任意实光滑紧支撑函数；对应的复输入由其准确四次复化恢复。继续使用完整 canonical 右锚、零 scalar 传入值及全部实际历史。

**定理。** 对已经固定的 R183 真实有限几何及共同合法物理区间，可以重新选择其四个矩形导数包中的最后一个下降 step，并重新执行左矩补偿、八个完整 packet 与归一，得到一个非退化、真正重叠的光滑三矩圆 $(f,g)$，具备以下全部性质。

1. R183 的完整二阶、三阶 range 与对 $T=\kappa\mathfrak H$ 的不可见性保持。
2. 存在最右区间 J，其中 f 在 J 及其全部右尾恒为零，而 g 是一个非零幅值的单调平端下降 step。
3. 若 $m=\dim\mathcal P$，可在这个**同一个**末 step 内选择 m 个真实输出点，使
   $$
   \mathcal E_g:\mathcal P\longrightarrow\mathbb R^m,\qquad
   F\longmapsto(F(g)(\xi_1),\ldots,F(g)(\xi_m))
   $$
   是单射。
4. 对任何满足 R184 定义域的全区间二阶 gauge，R198 的右 step period 不变量仍完整保持。因此，该新圆能通过第四 period 的一个必要条件是
   $$
   \boxed{\pi V_B=0\quad\text{作为整个 universal pure 算子}.}
   \tag{2}
   $$

第 3 项同时包含 $\mathcal P$ 的全部权，因而没有遗漏不同真权在固定 profile 上相消的可能。它是对同一个固定 g 的真实函数评价，不是对不同 profiles 的多次结果改名。

式 (2) 只是一道必要门；它没有支付其他区间的 period、mixed 通道、同一个 gauge 的 ruling、第五阶或精确有限等距族。若 $\mathcal P=\{0\}$，第 3 项和 (2) 为空条件；其余构造仍成立。

## 2. 全 pure 空间具有 R96 所需的结构

R105 证明 U 是完整 canonical 第四成本的有限真实函数空间，并在正仿射 pullback 下不变。pure 投影与该作用交换，所以 $\mathcal P$ 同样有限维、正仿射不变。作用矩阵为缩放参数的有限 Laurent 多项式、平移参数的有限多项式。

每个 pure 算子由 q 的有限 jets、坐标多项式、乘积及同一真实右 Volterra 原函数有限次组成。全部项对 q 四次齐次，每个原函数节点有严格正的 profile 次数。故：

- 查询点的值只依赖该点及其右侧的输入；
- 把共同右锚移到更右的空 collar 不改变算子；
- 在固定紧区间上，算子对某个有限 $C^K$ 拓扑连续。

这里 pure 并不是把所有输入 primitive 任意赋值，也不是对幂尾作 formal 替换。它是 R56 已定义的真实右锚函数算子。

### 2.1 单实输入足以分离这个空间

pure 公式的几何系数和基本微分、原函数操作都为实。因此每个 pure 算子在实 q 上取实值，且它作为四次齐次多项式有一个准确的对称实四线性极化。

若 F 在全部实紧支撑 q 上为零，实极化恒等式使该四线性算子在全部实四元组上为零。再作复线性延拓，它在所有复 q 上也为零。因此，按真实函数定义，单实输入评价已经分离 $\mathcal P$。

这一步允许直接使用 R96 第 2–3 节的**单输入版本**。它不是假设复 q 的某个非零取值必出现在一个指定实 profile 上。

## 3. 先得到一个紧支撑实 profile 的完整忠实评价

取真实基 $F_1,\ldots,F_m$。由第 2 节，存在 m 个可能使用不同实输入的评价

$$
e_j(F)=F(q_j)(x_j)
$$

使 $(e_j(F_k))$ 可逆。R96 的两个精确步骤将它们合到同一个实 profile。

先独立作正仿射变换，将每个输入支撑与其查询点放进一个指定开区间内部、从左到右互不交的小 packet。变换后评价行列式是仿射参数的有限 Laurent 多项式，在未变换点非零，故可以同时满足这些开放位置条件并保持非零行列式。

再以实幅 $z_j$ 相加。第 j 个查询只看到第 j 个及其右侧 packets，且整行是总次数四的多项式。行列式中词典序最高的

$$
z_1^4z_2^4\cdots z_m^4
$$

系数就是前面的非零独立评价行列式。由非零多项式性质，可选固定有限实幅使总行列式非零。

所以，在任意预留的非空开区间内部，存在一个**实、光滑、紧支撑**的 $q_*$ 及查询点 $\xi_1,\ldots,\xi_m$，满足

$$
\boxed{
\Delta_*=\det(F_k(q_*)(\xi_j))_{j,k=1}^m\ne0.
}
\tag{3}
$$

这个步骤保留同一右锚的全部尾项。packet 的右尾常数没有被设为零；右因果性只用于排除查询点左侧的输入。

## 4. 把忠实输入放进一个单调 step

选 $a<b$，使 $q_*$ 的支撑及所有查询点都紧含于 $(a,b)$。取光滑函数 b0，使

$$
b_0(x)=1\quad(x\le a),\qquad
b_0(x)=0\quad(x\ge b),
$$

并且

$$
b_0'(x)<0\quad(a<x<b),
\tag{4}
$$

两端所有正阶导数平坦。可先取在 $(a,b)$ 内严格正、两端平坦、积分为一的密度 $\rho$，再令
$b_0(x)=\int_x^\infty\rho$。

在所有查询点左方把 b0 另作一个固定光滑 compact 延伸，供 universal 原式求值；这个延伸对查询没有影响。以后只使用 $[a,\infty)$ 上的真正 step。

令

$$
q_t=b_0+tq_*.
\tag{5}
$$

因为 q* 支撑紧含于 $(a,b)$，存在紧集 K 覆盖其支撑且

$$
c_K=\min_K(-b_0')>0.
$$

充分小的有限 $|t|$ 满足
$|t|\|q_*'\|_\infty<c_K$，从而 $q_t'<0$ 于 $(a,b)$，两端仍准确为 1 和 0，所有端 jets 仍平坦。特别地，q_t 是真正的单调下降 step，不是通过符号系数允许局部反向的阶跃。

对固定查询点，定义

$$
\Delta(t)=\det(F_k(b_0+tq_*)(\xi_j)).
$$

每个矩阵项是 t 的次数至多四的实多项式。由四次齐次性，其四次系数为 $F_k(q_*)(\xi_j)$，因此

$$
[t^{4m}]\Delta(t)=\Delta_*\ne0.
\tag{6}
$$

所以 $\Delta(t)$ 只有有限个实零点。可以取任意小的非零 t，同时满足单调性条件和 $\Delta(t)\ne0$。

由此得到了一个真实单调平端 step q，满足

$$
\boxed{
\mathcal E_q:\mathcal P\to\mathbb R^m
\text{ 单射。}
}
\tag{7}
$$

整个证明使用同一个固定尾 b0 及其真实 right collar；没有采用“q 局部常数而所有 Volterra 尾同时为零”的非法评价。

第 4 节也说明：在这个小扰动族中，除有限个 t 外都 faithful。本文不据此声称有统一导数盒、定量最小宽度，或原先某个固定 t 已经 faithful。

## 5. 修改 R183 的最后导数包

取 R183 的前三个非负、单位积分、互不交导数包 $\rho_1,\rho_2,\rho_3$。将第四个包替换为

$$
\rho_4=-q'\ge0.
$$

它光滑、紧支撑于 $[a,b]$，满足 $\int\rho_4=1$，并与前三个包支撑分离。仍令

$$
s_j(x)=\int_{-\infty}^x\rho_j(t)\,dt,\qquad
f_0=s_1-s_3,\qquad g_0=s_2-s_4.
\tag{8}
$$

在第四下降包及其全部右尾，

$$
f_0=0,\qquad g_0=1-s_4=q.
\tag{9}
$$

前三个开放平台的值仍依次为

$$
(1,0),\quad(1,1),\quad(0,1).
$$

因此 R183 的三个不同实射影方向仍存在，任何常数可逆换基都不能将这个 profile 平面化为支撑不交的两函数。新 step 没有破坏真正重叠性质。

导数在四个包上的方向仍为

$$
(1,0),\quad(0,1),\quad(-1,0),\quad(0,-1).
$$

R183 的同右锚导数分包引理因此逐字成立：

$$
\mathfrak H\big|_{\operatorname{span}(f_0,g_0)
\times\operatorname{Sym}^2\operatorname{span}(f_0,g_0)}=0.
\tag{10}
$$

其中 hook 的全部真实原函数只含同点三输入的正阶导数乘积。不能把这一局部性外推给一般第四算子；本文只在已付 hook 身份中使用它。

## 6. 重新配平全部三矩，并准确控制 Gram

修改第四包后必须重新配平，不能继承旧 step 的矩数值。令 $q_0=f_0+ig_0$，定义普通复平方矩

$$
M_0(q)=\int(q'')^2,\quad
M_1(q)=\int x(q'')^2,\quad
M_2(q)=\int x^2(q'')^2+2\int(q')^2.
\tag{11}
$$

在整个矩形 profile 与全部查询的左方取三个互不交的同形偶实 bump $\eta(x-c_j)$。若

$$
a_0=\int(\eta'')^2>0,\qquad
a_2=\int x^2(\eta'')^2+2\int(\eta')^2,
$$

其矩列为

$$
v_j=(a_0,\ a_0c_j,\ a_2+a_0c_j^2)^T.
$$

三中心不同，行列式为非零的
$a_0^3\prod_{i<j}(c_j-c_i)$。准确解

$$
\sum_{j=1}^3 z_jv_j=-(M_0(q_0),M_1(q_0),M_2(q_0))^T,
$$

任取每个 $\beta_j^2=z_j$，置

$$
\widehat q=q_0+\sum_{j=1}^3\beta_j\eta(x-c_j)
=\widehat f+i\widehat g.
\tag{12}
$$

支撑分离使全部三矩准确为零。每个新增包的导数仍是一条固定实二维方向乘同一个实 bump 导数，故 (10) 保持。因为新增支撑严格在查询左方，(9)、整个右尾和 (7) 的全部查询也完全不变。

### 6.1 不是任意 GL2 归一

从 $M_0(\widehat q)=0$ 准确得到

$$
\int(\widehat f'')^2
=\int(\widehat g'')^2=:E,\qquad
\int\widehat f''\widehat g''=0.
\tag{13}
$$

E 严格为正：原 f0 的上升、下降包未变且非零，左侧补丁又不能消去这些不交支撑上的导数能量。所以 I0-Gram 已经是 $E\,\mathrm{Id}$，并非一个尚待任意旋转的矩阵。

同理，$M_1=M_2=0$ 分别给另外两个双线性矩的对角相等、交叉为零。因此使用**同一个正实标量** $E^{-1/2}$ 即可归一三矩圆，保持 $\widehat f=0$ 于整个右尾，且只把右 step 乘非零幅值。这里没有将 g 混入 f。

为明确一般 Gram 处理也不能破坏右 f=0：若某一步先有正定 Gram
$\left(\begin{smallmatrix}a&c\\c&b\end{smallmatrix}\right)$，应选保持 f 直线的三角变换

$$
f\longmapsto \frac f{\sqrt a},\qquad
g\longmapsto
\frac{g-(c/a)f}{\sqrt{b-c^2/a}},
\tag{14}
$$

而非任意 GL2。式 (14) 在 f=0 的右区间只将 g 乘非零标量。本构造 (13) 已有 $a=b=E,c=0$，所以 (14) 实际退化为共同标量。没有额外调用一个可能改变三矩或右 f=0 的换基。

复平方根只需对最终选择的一个 t 取值；本文没有声称在参数空间连续选择全部平方根或产生一个已控制导数的 family。

## 7. 八个完整 packet 支付三阶 ruling

把 $(\widehat f,\widehat g)$ 作为一个完整基本 packet，取八个相互分离的等距平移

$$
t_j=t_*+jL,\qquad
a_j=(-1)^j\binom7j^{1/3},\qquad j=0,\ldots,7,
$$

$$
f_{\mathrm{pack}}=\sum_{j=0}^7a_j\widehat f(x-t_j),\qquad
g_{\mathrm{pack}}=\sum_{j=0}^7a_j\widehat g(x-t_j).
\tag{15}
$$

每个基本 packet 都有自己的三个复零矩。平移变换律保持零矩，支撑分离给总复零矩；不需要不同 packet 的矩再相消。

本构造仍必须保留 R52/R183 的完整两类二阶 forcing

$$
H_d=(dY_f)^2-(dY_g)^2,\qquad
H_c=\mathcal S(Y_f,Y_g).
$$

$H_c$ 一般非零，不能因为导数分包就当作不交 profile 情形删掉。每个基本 packet 的三矩使这两条二阶右尾在包外准确为零，所以 canonical 二阶解按 $a_j^2$ 局部化。

R46/R52 已证明，对固定真实变量几何，四条第三 forcing $(f,d),(g,d),(f,c),(g,c)$ 的 ruling 在平移回基本坐标后，对平移参数 t 都是次数至多六的多项式。它们按

$$
a_j^3=(-1)^j\binom7j
$$

相加，第七有限差分使四条 ruling 对每个真实 s 准确为零。改变 $\rho_4$ 只改变这个多项式的系数，不改变已付的次数上界；也没有把二阶局部化外推到第四阶。

导数分包对所有基本 packet 以及左补丁仍成立，故总 hook 在 f、g 平面上的全部三次槽为零。真实几何仍为原 R183 的

$$
M=0,\qquad T=\kappa\mathfrak H.
$$

于是二阶 period 由 M0 消失，第三 period 由 hook 不可见性消失；四条第三 ruling 如上为零。已有完整 range 恢复给实际光滑、周期、双 collar 的二阶和三阶场，而非只给某些矩查询为零。

## 8. 放入共同物理区间、最终归一与忠实性保持

先固定真实有限几何，再选择共同合法 I，使 h>0 与 $\xi+\omega>0$ 有正间隙。所有 profile 构造是有限的，可以对 (15) 作同一个正仿射坐标变换

$$
x\longmapsto Hx+d,\qquad H>0,
$$

将全部八 packet、左补丁和查询放入 I 并留双 collar。

若基本 packet 的 I0 能量为 E，则 (15) 的 Gram 为

$$
E\left(\sum_{j=0}^7a_j^2\right)\mathrm{Id}.
$$

正仿射变换后 I0 能量准确乘 $H^{-3}$。因此最终共同归一幅值可显式取为

$$
\boxed{
\rho=\frac{H^{3/2}}
{\sqrt{E\sum_{j=0}^7a_j^2}}>0.
}
\tag{16}
$$

另外两个复矩的变换为原三矩的三角线性组合，故三个复零矩仍全部为零。式 (16) 只共同缩放 f、g；最右完整 packet 之后没有其他输入，那里仍有 f=0，g 恰为非零系数 $\rho a_7$ 乘变换后的 q。

把原查询点移至最右第七 packet：

$$
\xi_j^{\mathrm{new}}=H(\xi_j+t_7)+d.
$$

查询点及其右侧的实际 g 与 $\rho a_7 C_{H,d+Ht_7}q$ 完全一致；其他七个 packets、左补丁及 f 的所有支撑都在其左方。

右因果性与四次齐次性因此给

$$
F(g)(\xi_j^{\mathrm{new}})
=(\rho a_7)^4
(\mathsf P_{H,d+Ht_7}F)(q)(\xi_j).
\tag{17}
$$

$\rho a_7\ne0$，而 $\mathsf P_{H,d+Ht_7}$ 在**整个** $\mathcal P$ 上可逆。因此 (7) 与 (17) 证明最终同一真实末 step 的评价仍单射。这里使用的是全部真权组成的仿射不变空间，不是一个可能被平移混到别权的单权子空间。

不可换基为不交支撑的三个平台射影方向、完整三矩圆及二、三阶 range，均由前述步骤保留。这完成定理前三项。

## 9. 全部二阶 gauge 下的右 step 必要门

对 R183 的真实 $M=0,T=\kappa\mathfrak H$ 几何，R184 给允许二阶 gauge 的完整 period 改变量

$$
\Delta V_\theta=2\kappa L_f(w_\theta).
$$

R198 已在 f=0 的整个右尾证明 $L_f(w)$ 本身准确为零，而不只是它的二阶导数为零。因此在本稿最右 step 上，任意全 I、满足真实定义域的二阶 gauge 都不能改变 period，第三齐次 gauge 也由 M0 不改变 period。

同一右尾上的 canonical period 准确为

$$
V^0_{B,\theta}(\xi)
=\sin^4\theta\,P_B(g)(\xi),\qquad
P_B(q)=16(\pi V_B)(q).
\tag{18}
$$

所有右转接尾完整保留；没有把它们替换为零常数。若第四 period 全函数可解，取 $\theta=\pi/2$ 并在 (17) 的所有点评价，得到

$$
\mathcal E_g(\pi V_B)=0.
$$

这里必须另付 $V_B\in U$，不能把 $T_B\ne0$ 的 B 直接塞进 R105 的 $M=T=0$ 定义。R183 的 B 具有相同首末 scalar 常值 germ、frame $I\to I$ 且 $M_B=0$。取 [R83](R83-true-fourth-transfer-and-zero-lower-history-variations.md) 第 3 节、[R84](R84-fourth-cost-semigroup-and-frame-length-bound.md) 使用的同 k 真倒行 $B^{\rm rev}$。它仍在相同端口、frame $I\to I$，并准确满足

$$
M_{B^{\rm rev}}=0,\qquad T_{B^{\rm rev}}=-T_B,\qquad
V_{B^{\rm rev}}=V_B.
$$

两块矩阵均为零，R83 的完整历史传递中全部交叉项因而为零，所以真实拼接 $BB^{\rm rev}$ 满足

$$
M_{BB^{\rm rev}}=T_{BB^{\rm rev}}=0,\qquad
V_{BB^{\rm rev}}=2V_B.
$$

因此 $V_B=\tfrac12V_{BB^{\rm rev}}\in U$；事实上它已在实际零矩零第三成本所生成的凸锥中。这里只用正半倍证明空间或锥归属，没有把半倍当作另一条实际路径，也没有用倒行取负第四成本。由此 $\pi V_B\in\mathcal P$，第 8 节的单射准确给

$$
\pi V_B=0
$$

作为 universal pure 算子。反过来，若这个 universal pure 算子为零，(18) 的整个右 step period 当然为零；但全区间其他部分及 ruling 仍然未付。

因此，对本稿新选的圆，

$$
\boxed{
\text{最右 step 的完整 period 恒零}
\quad\Longleftrightarrow\quad
\pi V_B=0\text{ universal。}
}
\tag{19}
$$

这是对固定 circle 必要门的准确有限化，不是多 profile 结果的拼接替代。

## 10. R201 之后的解释

[R201](R201-weight-zero-pure-image-and-failure-of-positive-character-readout.md) 已证明存在 $H\in U_0$，使 $\pi H=0$ 而 $\lambda_+(H)=1$。因此即使本稿的新 step 对**全部** pure(U) faithful，也不能从它恢复 R196 的完整正字符：投影已经丢掉的核，不会因对像选取忠实输入而恢复。

本稿不会据 R196 宣称新圆必然第四阶失败。它准确把右 step 条件变成 (19)，下一问题是实际 pure 成本的可达性或独立 pure 不变量。R202 若分析其闭锥，也仍须区分闭锥与实际有限成本半群。

原冻结 step 是否满足 (19) 的单射前提，本稿没有判断。新 step 的构造只给有限存在性与任意小扰动族的多项式排零，没有提供一份已执行的数值 profile 或导数上界。

本文完成的是保持 R183 全部已付低阶条件的新 faithful step 圆和相应全权 pure 必要门；未完成完整第四联合 period/ruling、更高阶、收敛及主课题要求的精确嵌入有限等距族。

