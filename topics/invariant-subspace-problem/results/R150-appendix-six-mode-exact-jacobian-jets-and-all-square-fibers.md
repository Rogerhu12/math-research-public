# R150 附录：六模式第五自然 Bell 幂的精确 Jacobian 证书与原平方全部纤维

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d。
状态：有限特征零证书已经独立全量验证；实际算子结论经已付 Schur 字典与真实 Bell 逆分母定理。

## 1. 结论与原目标

沿用原六个连续正实对数模式，写 $U_\nu=u_\nu/\nu$，并定义
$
\begin{aligned}
g_6(x)&=5x_0x_4-32x_1x_3+27x_2^2,\\
g_7(x)&=x_0x_5-5x_1x_4+4x_2x_3,\\
g_8(x)&=x_1x_5-5x_2x_4+4x_3^2,\\
F(U)&=g_6(U)+i g_7(U)+g_8(U).
\end{aligned}
$
这里 $x_j=U_{j+1}$，$0\le j\le5$。

**定理。** 对每个 $\lambda\in\mathbb C$ 和原模型的每个合法指数权 $w$，
$
\boxed{[F(U)^2-\lambda]e^w\ \text{非零且循环}.}
\tag{1.1}
$
新增的实际纤维是 $\lambda=0$；非零纤维已有齐次 Euler 证明。
本稿另给同一份与 $\lambda$ 无关的完整梯度证书，直接覆盖全部纤维。

核心有限结论是下述原四次 $R$ 与指定自然 Bell 二次 $B_r$ 满足
$
\boxed{B_r^5\in(\partial_{y_0}R,\ldots,\partial_{y_5}R)}
\quad\text{在特征零中}.
\tag{1.2}
$
证明使用明确的有理左核与两个非零整数子式。
它不从有限域中的归属推断有理归属，也不需要列出某个数千位分母表示。

## 2. 完整普通矩消元及同一整数输入

作固定可逆对角标量换元 $x_j=i^j y_j$。偏导按链式法则仅乘非零常数，随后仍读取原合并键梯度；这不改变物理矩池。于是
$
F'=g_6(y)-g_7(y)-g_8(y)=\tfrac12 y^\mathsf T K y,
\quad
K=
\begin{pmatrix}
0&0&0&0&5&-1\\
0&0&0&-32&5&-1\\
0&0&54&-4&5&0\\
0&-32&-4&-8&0&0\\
5&5&5&0&0&0\\
-1&-1&0&0&0&0
\end{pmatrix}.
$
令 $H_m$ 为六阶矩阵，其 $(i,j)$ 项在 $i+j=m$ 时为一，否则为零，
$0\le m\le10$。定义
$
J_{mn}=\operatorname{tr}(K H_m K H_n),
\qquad b_m=(Ky)^\mathsf T H_m(Ky).
$
完整普通矩的原精确消元已给
$
\det J=-64701092257700249600\ne0,
$
$
Q(y,W)=F'(y)^2-2b(y)^\mathsf T W+2W^\mathsf T J W,
\qquad
R(y)=F'(y)^2-\tfrac12 b(y)^\mathsf T J^{-1}b(y).
\tag{2.1}
$
这里 $W=(W_0,\ldots,W_{10})$ 是实化后的全部二阶合并矩；
更高普通矩项的消失已经在完整矩计算中支付，不是只截取了二阶近似。
原始完整计算见[临界曲线与第二矩消元](../notes/2026-11-13-complete-ordinary-bell-curve-critical-locus-and-symbol-denominator-boundary-1cf.md)。

令
$
f(d)=3725d^3-43931504d^2+6080833024d+52565262336.
$
它在 $(-9,-8),(144,149),(11600,11700)$ 各有一个实根。
固定其中任意一个，设
$
A=-\frac{521d^2-46784d+271360}{160(5d-704)},\qquad B=A+d,
\qquad r=(A,B,0,0,0,1).
\tag{2.2}
$
所有这些数均有限且为实数。定义
$
c_m=\sum_{i+j=m}r_i r_j,\qquad
B_r(y)=(r\cdot y)^2-c^\mathsf T J^{-1}b(y).
\tag{2.3}
$

为逐项整数核验，沿用已经发布的[整数生成数据](../notes/2026-11-13-six-mode-fifth-power-dixon-integer-generators.json)，不改变其归一化：
$
R_{\rm int}=\sigma R,\quad \sigma=77129712412,\qquad
q_{\rm int}=\kappa B_r,\quad
\kappa=\frac{31646381397859212552175616000000000}{30760960000}.
\tag{2.4}
$
取 $t=3725d$，系数在有限自由有理代数
$
\mathcal E=
\mathbb Q[t]\big/
(t^3-43931504t^2+22651103014400t+729375868200960000)
\tag{2.5}
$
中按 $1,t,t^2$ 表示。数据给出 $R_{\rm int}$ 的全部102项、
$q_{\rm int}$ 的21个二次单项式及各自三个整数系数。
不需要先假定 (2.5) 是一个域；最后可在任意指定实根处取值。

## 3. 原度十梯度矩阵

记 $V_{10}=\mathbb Q[y_0,\ldots,y_5]_{10}$，维数为3003。
六个三次 $\partial_iR_{\rm int}$ 分别乘全部792个七次单项式，形成
$
\mathcal A:\mathbb Q^{4752}\longrightarrow V_{10}.
\tag{3.1}
$
单项式次序与原 Dixon 输入完全相同：递归让第一指数从零递增。

[已发布模103种子](../notes/2026-11-13-six-mode-fifth-power-mod103-certificate.json)
给出各有2918项的有序行列集 $I,J_0$。
本次独立验证器重新从102个整数四次项构造
$
S=\mathcal A_{I,J_0},
$
并从头完成模103消元；没有使用原提升缓存或原有理候选。
所有主元非零，准确得到
$
\boxed{\det S\equiv35\pmod{103}.}
\tag{3.2}
$
故 $\operatorname{rank}_{\mathbb Q}\mathcal A\ge2918$。

下面用有理恒等式给反向秩界，并确定整个像。

## 4. 八十五个明确有理左泛函

### 4.1 曲线和两个原临界节点

令
$
v(z)=(1,z,z^2,z^3,z^4,z^5).
$
全部六个原梯度在 $v(z)$ 上恒为零。
对 $P\in V_{10}$，取 $P(v(z))$ 的次数0至50的系数，得到51个有理泛函。

另取两个已经精确核验的射影点，以以下整数向量为代表：
$
\begin{aligned}
n_+&=(990895,1153105,2063840,4524760,11260192,30644640),\\
n_-&=(143682655,-222517655,664053920,-4306767840,
39985265088,-450141192000).
\end{aligned}
\tag{4.1}
$
本次验证器重新核验两点上的全部六个整数梯度为零。
因此 $P\mapsto P(n_\pm)$ 也是 $\mathcal A$ 的左核泛函。

### 4.2 五个局部变量中的准确三阶截断

在有限曲线图上使用五个形式变量 $s,u_2,u_3,u_4,u_5$，代入
$
y_0=1,\quad y_1=z+s,\quad y_i=(z+s)^i+u_i\quad(2\le i\le5).
\tag{4.2}
$
只取总次数至多三的 Taylor 系数。
这有56个单项式；删去四个纯 $s$ 单项式，剩52个含至少一个 $u_i$ 的系数。
在无穷远使用反向图
$
y_5=1,\quad y_4=z+s,\quad y_{5-i}=(z+s)^i+u_i\quad(2\le i\le5).
\tag{4.3}
$

六个原梯度沿整条曲线恒零，因此其所有纯 $s$ 系数为零，
且局部最低总次数至少一。
于是检验一个至多三阶的局部泛函是否杀掉
$(\partial_iR_{\rm int})H$，只需要 $H$ 的至多二阶 Taylor 展开。
五变量至多二次共有21个单项式。
因此准确只需检验
$
6\cdot21=126
$
个原梯度乘局部单项式的52维系数行。
这一步覆盖任意七次乘子，故覆盖 (3.1) 的全部4752列；
没有把原乘子限制为全局二次。

### 4.3 四个有限有理代数中的明确数据

以下代数只用于记录局部参数；令 $t=5z$。
$
\begin{aligned}
g(t)&=t^6+110t^5+1105t^4-65000t^3+124200t^2
      +2592000t-4320000,\\
h(t)&=t^8+50t^7+765t^6-23400t^5-361000t^4
      +9960000t^3-10600000t^2-398000000t+750000000.
\end{aligned}
$
全部有理系数存于[精确 jet 数据](../notes/2026-11-13-six-mode-jacobian-degree-ten-jet-certificate.json)。
它们按以下四组组织：

| 曲线图 | 参数代数 | 52维代数线性泛函数 | 展开后的有理泛函数 |
|---|---|---:|---:|
| 有限，$z=0$ | $\mathbb Q[t]/(t)$ | 3 | 3 |
| 无穷远，反向图且 $z=0$ | $\mathbb Q[t]/(t)$ | 3 | 3 |
| 有限，$z=t/5$ | $\mathbb Q[t]/(g)$ | 3 | 18 |
| 有限，$z=t/5$ | $\mathbb Q[t]/(h)$ | 1 | 8 |

对每个数据向量 $\beta=(\beta_1,\ldots,\beta_{52})$，
定义先在相应参数代数内求和的泛函
$
P\longmapsto \sum_{\alpha=1}^{52}
\beta_\alpha\, [s^{\alpha_0}u_2^{\alpha_1}\cdots u_5^{\alpha_4}]
P(y(s,u)).
\tag{4.4}
$
再按 $1,t,\ldots$ 抽取其有理坐标。
这是定义明确的有理线性运算；不要求参数代数为域，也不要求先分类临界簇。

[独立验证器](../notes/2026-11-13-six-mode-jacobian-degree-ten-jet-verify.js)
逐项验证 (4.4) 杀掉 §4.2 的全部126行。
共1260条参数代数恒等式，即4032个有理系数恒等式，全部准确为零。
这些数据因而给出32个真正的有理左泛函。

连同 §4.1，得到
$
\mathcal L:V_{10}\longrightarrow\mathbb Q^{85},
\qquad
\boxed{\mathcal L\mathcal A=0}.
\tag{4.5}
$

### 4.4 八十五个泛函确实独立

数据中的所有有理分母模103均可逆。
验证器按 (4.2)–(4.4) 直接把上述泛函作用于全部3003个原十次单项式，
并用精确模运算核验数据给定的85列子式：
$
\boxed{\det\mathcal L_{\rm selected}\equiv47\pmod{103}.}
\tag{4.6}
$
所以 $\operatorname{rank}_{\mathbb Q}\mathcal L=85$。
由 (3.2)、(4.5) 及 $3003-85=2918$，准确得到
$
\boxed{
\operatorname{rank}_{\mathbb Q}\mathcal A=2918,\qquad
\operatorname{Ran}_{\mathbb Q}\mathcal A=\ker\mathcal L.
}
\tag{4.7}
$
这里只用有限维秩与已核有理恒等式。
没有使用未证的理想饱和、局部环长度、根单性或完整临界簇分类。

## 5. 第五自然 Bell 幂的特征零归属

本次验证器还独立核验
$
q_{\rm int}(v(z))=0,\qquad
q_{\rm int}(n_+)=q_{\rm int}(n_-)=0
\quad\text{于 }\mathcal E.
\tag{5.1}
$
事实上三个 $1,t,t^2$ 系数分别消失：曲线上全部33个二次曲线系数为零，
两个节点上每个分量也为零。

在 (4.2) 或 (4.3) 的任一参数代数中，
$q_{\rm int}$ 因而属于由五个局部增量生成的理想；
更强地，它在 $u=0$ 上对整个 $s$ 恒零。
所以 $q_{\rm int}^5$ 的至多三阶 Taylor 系数全部为零。
也可以直接用 Leibniz：至多三次微分分配给五个因子时，至少一个因子未被微分，
在相应曲线点上仍为零。
这给全部32个局部泛函的消失。
曲线的51个值系数及两点值也消失，因此
$
(\mathcal L\otimes I_{\mathcal E})q_{\rm int}^5=0.
$
将 (4.7) 扩展到有限自由系数代数 $\mathcal E$，即得
$
q_{\rm int}^5\in(\partial_0R_{\rm int},\ldots,\partial_5R_{\rm int})
\quad\text{于 }\mathcal E[y].
\tag{5.2}
$
由 $\sigma,\kappa\ne0$，在 (2.2) 的任意实根处取值即得 (1.2)。

### 5.1 明确的有理见证定义

本稿也给完整系数的有限精确表达，不只给存在性。
令 $\mathsf B$ 为 $q_{\rm int}^5/2^{29}$ 的三个原十次系数列；
这里 $2^{29}$ 是非零有理缩放；原整数生成计算另外已经准确验证其整除。
在所选列 $J_0$ 上取
$
X=S^{-1}\mathsf B_I=\frac{\operatorname{adj}S}{\det S}\mathsf B_I,
$
其余1834列置零。
由 (4.7)，每个目标列均属于 $\operatorname{Ran}\mathcal A$；
而所选2918列线性独立，故它们构成该像的一组基。
因此
$
\boxed{\mathcal A_{J_0}X=\mathsf B}
$
在原完整3003行及三个分量上成立。
这与仅解所选方阵的旧候选有本质不同：其余行现由完整左核证书严格支付。

将 $X$ 按六个导数及七次单项式还原为 $D_i(y)$，便有
$
B_r^5=\sum_{i=0}^5 C_i(y)\partial_iR,\qquad
C_i=\frac{\sigma\,2^{29}}{\kappa^5}D_i.
\tag{5.3}
$
旧固定主元的巨大有理高度与 (5.3) 完全相容，不再阻止确定这些系数。

## 6. 接回完整普通矩的准确梯度证书

置
$
z=W-\tfrac12J^{-1}b(y),\qquad
S_r(y,W)=(r\cdot y)^2-2c^\mathsf T W.
$
则
$
Q=R+2z^\mathsf T Jz,\qquad S_r=B_r-2c^\mathsf T z,
$
$
\partial_WQ=4Jz,\qquad
\partial_iR=\partial_{y_i}Q+2(\partial_i b)^\mathsf Tz.
\tag{6.1}
$
这里 $\partial_{y_i}Q$ 保持原 $W$ 不动；没有误用保持 $z$ 不动的偏导。

令
$
U_5=\sum_{j=0}^4 S_r^{\,4-j}B_r^j.
$
把 (5.3) 代入 $S_r^5-B_r^5=-2c^\mathsf Tz\,U_5$，准确得到
$
\boxed{
S_r^5=
\sum_i C_i\partial_{y_i}Q+
\frac12\left(\sum_i C_i\,\partial_i b-c\,U_5\right)^\mathsf T
J^{-1}\partial_WQ.
}
\tag{6.2}
$
这是原完整 $Q$ 的梯度理想证书，没有 $Q$ 本身的倍数。
所以对每个 $\lambda$，同一身份也属于 $Q-\lambda$ 的 Jacobian 理想。
其它完整矩键若不出现在普通 $Q$ 中，其偏导为零；没有删去实际 Bell 修正。

## 7. 真实空谱 first 与原自然域

回到原 $U$ 变量，取
$
a=iA\,U_1+B\,U_2+U_6.
\tag{7.1}
$
因 $x_j=i^jy_j$，准确有 $a=i(r\cdot y)$。
因此 $a^2$ 的完整普通 Bell 多项式在当前坐标中是
$
\boxed{S_a=-S_r}.
\tag{7.2}
$
这一个整体负号必须保留；其第五幂只将 (6.2) 的系数整体变号。

原物理 first 行的主部为
$
\frac{\log^5(p+2)+B\log(p+2)+iA}{p+2}.
$
实部最终为正，且沿正实射线的相位缺陷为
$
O\!\left(\frac1{(p+2)\log^5(p+2)}\right),
$
可和。由原实际 first 相位判据，这个 first 在原规范自然图上空谱，
其全域有界逆属于原交换子代数；原指数权的变化仍在已付有界交换扰动范围内。
这个断言及三实根的同一相位预算已经在原六模式候选记录中支付。

再使用
[真实 Bell 逆分母定理](R150-appendix-jacobian-certificates-with-actual-bell-inverse-denominators.md)：
空谱 first 的完整 ordinary Bell 平方，在原自然域上也具有全域有界交换子逆。
(7.2) 因而给实际 $S_r$ 的同样真逆，只差非零常数符号。

(6.2) 的全部矩键都来自原六模式、次数至多二的同一合并矩表；
它们已经包含在原 $F^2$ 的完整次数四矩池中。
没有新增未支付的物理行或另一个矩池。
上述定理于是直接适用，$\nu=5$、多项式倍数项取零。

具体说，实际 Bell 多项式仍为 $P=Q-\lambda+K_Q$。
将原真实逆仅放在右输入端，快修正的联合四次幂型和 $O(r^2)$ 自然词域预算
由所引定理支付；不假称含该逆的系数仍属于快类，也不将逆越过物理反射。
因此得到 (1.1)，包括原来尚开的零纤维和任意原合法指数权。

## 8. 可重复核验与完成范围

三个必需输入均为已保存的小文本文件：

- [原整数生成数据](../notes/2026-11-13-six-mode-fifth-power-dixon-integer-generators.json)；
- [原主元次序](../notes/2026-11-13-six-mode-fifth-power-mod103-certificate.json)；
- [本次全部有理 jet 系数](../notes/2026-11-13-six-mode-jacobian-degree-ten-jet-certificate.json)。

运行[独立验证入口](../notes/2026-11-13-six-mode-jacobian-degree-ten-jet-reproduce.cjs)，
默认从原102个整数项重新构造并核验2918阶子式，不使用 Dixon 状态、网络或外部代数包。
root 已用[验证器](../notes/2026-11-13-six-mode-jacobian-degree-ten-jet-verify.js)执行全流程，输出完整通过：
4032个有理系数身份、85阶子式47、2918阶子式35及全部目标消失均成立。
normal 独立重新执行局部有理身份、全局85阶秩和目标消失；
kernel 另审有限截断、有限自由系数代数与两个秩界的逻辑连接。
原终端仍离线，命令行包装器未被冒称在终端运行；其调用的全部数学验证已经执行。

本稿闭合的是这一个原六模式 $F$ 的普通平方、全部 $\lambda$ 和指数权。
没有将 $B_r^5$ 误认成 first 的第十普通 Bell 幂，
没有由此宣称 $F^h$ 的所有更高点态幂、任意外多项式、一般六模式复二次或普通 ISP 已解决。
