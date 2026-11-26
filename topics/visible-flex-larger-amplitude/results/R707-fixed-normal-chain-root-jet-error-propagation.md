# R707 — 共同有限分段法向闭合链的完整工作误差传播

日期：2026-11-26。

**状态：以下代数恒等式、条件误差命题及其证明已完成；没有验证任何实际候选的余量，没有生成连续闭合、剩余 Gram 或几何证书。** 本文处理 [R703](R703-normal-endpoint-lifting-and-fixed-partition-jets.md) 中“共同有限分段本身就是数学定义”的法向选择。它不把有限分段当作准确辅助 ODE 的终值，也不重证 [R695](R695-so3-zero-closure-bubble-uniform-IFT.md) 的一般端点 IFT。

新增内容是完整误差账：上一段控制及其两阶角 jet 的误差如何进入本段法向平面，实际三维交叉 Jacobian 如何验证，实际工作残差如何转成准确残差，根和角 jet 误差如何逐段传播，以及完整外参数 J/J* 和最终六个物理 jet 怎样继续支付。真实积分、符号域载体、浮点运算和分支关联均保留。本文不是求解器新增的前置检查；数值方向可以按原完整合同继续运行，证书只在实际输入满足所列条件时成立。

## 1. 固定对象、范数和覆盖范围

令 $x$ 是一个完整外部自由点，包括原全部自由 core、全部旋转系数和自由高度 $H$。当前自由点的保存字可以准确解释为实数定义；本文不擅改其非高度槽、参考模型或目标度量。固定对象包括准确标量 $g$、准确 $S>0$ 和符号径向节点、固定材料图 $\theta_0(\phi)$、十八个字面 $Q$ 常量、两个 bubble 与新增 $\gamma$ 的准确支持，以及所有角、所有 $x$ 共用的准确分段
$$
0=\tau_0<\tau_1<\cdots<\tau_m=1.
\tag{1}
$$
改变其中任一数学选择须另记模型身份。以显式新 $H$ 构造的新自由点仍须真实重读；原输入验证成功不等于原初根或新初根成功。

记 R703 的完整无量纲端点函数为
$$
f(x,\phi,u)=
\frac{\Gamma_x(\phi)-P_x(\phi)+
\int_0^S \exp([\mathcal W(s,\phi)u]_\times)
             T_y(x,s,\phi)\,ds}{S},
\qquad u\in\mathbb R^6,
\tag{2}
$$
其中 $\mathcal W=[S W,\gamma I_3]$，$u=(z/S,v)$，$A=f_u$。$\mathcal W$ 只表示物理旋转控制矩阵；下文的 $B$ 专指某一段的法向平面，二者不混用。$f(x,\phi,0)$ 依赖全部当前 $x$ 和角 $\phi$，不是一个可从导数图中删除的常量。

向量均用欧氏范数；矩阵用对应谱范数；多线性导数用每个输入均取欧氏单位球的诱导范数。三套 jet 堆叠后仍用乘积欧氏范数。外参数可另用明确声明的 Hilbert 范数，相关算子及其对偶都须使用该同一范数。以下任何张量上界都不是单个 entry 的最大绝对值；若由 entry 区间获得，须另支付相应行和、维数或 Frobenius 界。

所有上界在所声明的**整个角胞、完整根盒和连接所需的线段**上成立。若只在一个数值角节点得到了值，不能把它直接作为整个角胞的上界。可以用胞内常数作为比较载体：零、一、二阶比较载体不必彼此是导数，但每一个都必须与相应准确 jet 作独立的完整比较。

本节所用混合导数在覆盖域中连续。对角二 jet 的一次外参数微分，$f$ 的相应混合四阶导数足够形成公式；没有由任意 $C^2$ 曲面自动推出这一正则性。分片径向函数可以按真实接点分胞，只需下面实际使用的径向绝对连续性和一阶 Lipschitz 界。当前 core 逆图还须有同一提升分支上的真实正 $\rho_c$ 下界。

## 2. 一段的准确方程与真实交叉矩阵

固定段 $i$，暂省略 $x,i$。上段已经选定的准确控制曲线及其总角 jet 记为
$$
p_j=\partial_\phi^j u_{i-1},\qquad j=0,1,2.
$$
定义
$$
B_0(\phi)=A(x,\phi,p_0(\phi)),\qquad
B_j=\partial_\phi^j B_0\quad(j=1,2),
\tag{3}
$$
以及固定本段未知量 $\eta\in\mathbb R^3$ 时的函数
$$
v(\phi,\eta)=p_0+B_0^T\eta,\qquad
G(\phi,\eta)=f(x,\phi,v)-(1-\tau_i)f(x,\phi,0).
\tag{4}
$$
本段根满足 $G(\phi,\eta_0)=0$。其准确三套角 jet 记为 $\eta_j=\partial_\phi^j\eta_0$，输出为
$$
u_{i,j}=p_j+
\sum_{k=0}^j {j\choose k}B_{j-k}^T\eta_k,\qquad j=0,1,2.
\tag{5}
$$

在偏 $\phi$ 导数中先固定 $\eta$。本段真实 Jacobian 是
$$
J=G_\eta=A(x,\phi,p_0+B_0^T\eta)B_0^T.
\tag{6}
$$
它通常不对称。$A(x,\phi,u_i)$ 和 $B_0$ 各自满行秩并不推出 (6) 可逆；本证明始终包围整个交叉矩阵。$\eta$ 是三维法向增量，不是原九 KKT 的乘子，也不把六控制当作三个外部自由变量。

## 3. 一个完整二阶 jet 比较恒等式

先给出后续反复使用的有限维代数。设 $M(\phi,v)$ 取值于一个有限维赋范空间，所需混合导数在覆盖域中有诱导范数上界
$$
M_{ab}\ge\|\partial_\phi^aD_v^bM\|.
$$
对 $v_0,v_1,v_2$ 定义
$$
\begin{aligned}
\mathcal J_0(M;v)&=M(\phi,v_0),\\
\mathcal J_1(M;v)&=M_\phi+M_v[v_1],\\
\mathcal J_2(M;v)&=M_{\phi\phi}+2M_{\phi v}[v_1]
                 +M_{vv}[v_1,v_1]+M_v[v_2],
\end{aligned}
\tag{7}
$$
右边均在 $(\phi,v_0)$ 取值。对比较载体 $\widehat v_j$，设
$a_j\ge\|v_j-\widehat v_j\|$，$V_j=\|\widehat v_j\|$。那么
$$
\begin{aligned}
\|\mathcal J_0(M;v)-\mathcal J_0(M;\widehat v)\|
&\le M_{01}a_0,\\
\|\mathcal J_1(M;v)-\mathcal J_1(M;\widehat v)\|
&\le(M_{11}+M_{02}V_1)a_0+M_{01}a_1,\\
\|\mathcal J_2(M;v)-\mathcal J_2(M;\widehat v)\|
&\le(M_{21}+2M_{12}V_1+M_{03}V_1^2+M_{02}V_2)a_0\\
&\quad+2(M_{11}+M_{02}V_1)a_1+M_{02}a_1^2+M_{01}a_2.
\end{aligned}
\tag{8}
$$

**证明。** 先把两式的 $v_1,v_2$ 都固定为 $\widehat v_1,\widehat v_2$，仅沿 $v_0$ 到 $\widehat v_0$ 的线段积分。逐项求 $v_0$ 导数分别给出 (8) 中乘 $a_0$ 的全部项。随后在真实 $v_0$ 处写 $v_1=\widehat v_1+\delta_1$、$v_2=\widehat v_2+\delta_2$。二次项展开为
$2M_{vv}[\widehat v_1,\delta_1]+M_{vv}[\delta_1,\delta_1]$；
其余为相应线性项，得到剩余界。所有系数在完整线段和 jet 域上取统一上界，因而不遗漏依赖上游误差的乘积。证毕。

(8) 不要求比较 jet 来自某个插值函数，也不把工作数组的自动微分当作准确 jet；工作误差须另加。

## 4. 上段误差进入法向平面的完整三 jet

由 (3) 直接得到
$$
\begin{aligned}
B_0&=A(\phi,p_0),\\
B_1&=A_\phi+A_u[p_1],\\
B_2&=A_{\phi\phi}+2A_{\phi u}[p_1]
                   +A_{uu}[p_1,p_1]+A_u[p_2].
\end{aligned}
\tag{9}
$$
设上一段已给
$e_j^-\ge\|p_j-\widehat p_j\|$。
实际保存或重新读取的工作法向载体是 $\widehat B_j$。
用 $\varepsilon_{B,j}$ 支付
$\widehat B_j$ 与式 (9) 在准确函数 $A$、比较点
$(\widehat p_0,\widehat p_1,\widehat p_2)$ 上所得值的差。这些费用须包含该工作法向装配的全部积分、指数、AD、算术和载体差，不能默认为零。

记 $P_j=\|\widehat p_j\|$，取
$M_{ab}\ge\|\partial_\phi^aD_u^b A\|$。由 (8) 可取
$$
\begin{aligned}
b_0&=\varepsilon_{B,0}+M_{01}e_0^-,\\
b_1&=\varepsilon_{B,1}+
 (M_{11}+M_{02}P_1)e_0^-+M_{01}e_1^-,\\
b_2&=\varepsilon_{B,2}+
 (M_{21}+2M_{12}P_1+M_{03}P_1^2+M_{02}P_2)e_0^-\\
&\quad+2(M_{11}+M_{02}P_1)e_1^-+M_{02}(e_1^-)^2+M_{01}e_2^-,
\end{aligned}
\tag{10}
$$
从而 $\|B_j-\widehat B_j\|\le b_j$。

注意 $A=f_u$，所以 (10) 的 $M_{03}$ 等项已经涉及 $f$ 的混合四阶导数。这是真实依赖，不因每段只解三个根而消失。第 $i$ 段使用上段完整 $e_0^-,e_1^-,e_2^-$；不能只把上段零阶误差传进新的法向平面。

## 5. 把实际工作残差转成准确残差

### 5.1 保留所有实际加乘缺陷

令工作增量三 jet 为 $\widehat\eta_j$。在比较这些固定增量时，准确测试控制 jet 为
$$
v_j=p_j+\sum_{k=0}^j{j\choose k}B_{j-k}^T\widehat\eta_k.
\tag{11}
$$
设实际用于读取本段端点 jet 的工作控制为 $\widehat v_j$。定义其完整加乘缺陷上界
$$
\chi_j\ge\left\|\widehat v_j-
\left(\widehat p_j+
\sum_{k=0}^j{j\choose k}
\widehat B_{j-k}^T\widehat\eta_k\right)\right\|.
\tag{12}
$$
括号内按准确实数加乘解释工作字。$\chi_j$ 包含所有乘法、加法、归约及实际 value-anchor 之间的差；若不同 grad mode、批形或缓存路径返回不同字，不能据公式相同将它们宣称逐字一致。

于是可以取
$$
a_j=e_j^-+\chi_j+
\sum_{k=0}^j{j\choose k}b_{j-k}\|\widehat\eta_k\|,
\qquad
\|v_j-\widehat v_j\|\le a_j.
\tag{13}
$$

### 5.2 闭合三 jet 和零控制右端

令 $\Phi_j=\mathcal J_j(f;v)$，$\widehat V_j=\|\widehat v_j\|$，
$F_{ab}\ge\|\partial_\phi^aD_u^bf\|$。
由 (8)，准确 $\Phi_j$ 相对准确函数在工作测试控制上的差可用
$$
\begin{aligned}
P^{f}_0&=F_{01}a_0,\\
P^{f}_1&=(F_{11}+F_{02}\widehat V_1)a_0+F_{01}a_1,\\
P^{f}_2&=(F_{21}+2F_{12}\widehat V_1+F_{03}\widehat V_1^2
                         +F_{02}\widehat V_2)a_0\\
&\quad+2(F_{11}+F_{02}\widehat V_1)a_1+F_{02}a_1^2+F_{01}a_2.
\end{aligned}
\tag{14}
$$
以 $\varepsilon_{\Phi,j}$ 支付实际工作端点 jet
$\widehat\Phi_j$ 与该准确函数值的差。
零控制准确右端
$f_{0,j}=\partial_\phi^j f(x,\phi,0)$
的工作载体 $\widehat f_{0,j}$ 另有误差
$\varepsilon_{0,j}$。零控制并不等于零端点残差。

如果实际工作残差 $\widehat r_j$ 是用载体 $\widehat\tau_i$ 计算
$\widehat\Phi_j-(1-\widehat\tau_i)\widehat f_{0,j}$
所得，令 $\varepsilon_{r,j}$ 支付其完整减乘算术误差，则
$$
r_j=
\|\widehat r_j\|+\varepsilon_{\Phi,j}+P^f_j
 +(1-\tau_i)\varepsilon_{0,j}
 +|\tau_i-\widehat\tau_i|\,\|\widehat f_{0,j}\|
 +\varepsilon_{r,j}
\tag{15}
$$
是准确三个残差在工作增量 jet 处的范数上界。

**证明。** 先在式 (11) 与工作测试控制之间用 (14)，再插入准确函数在工作控制上的值与 $\widehat\Phi_j$。右端差准确拆成
$(1-\tau_i)(f_{0,j}-\widehat f_{0,j})
+(\widehat\tau_i-\tau_i)\widehat f_{0,j}$。
最后加实际减乘费用，即得 (15)。证毕。

对于当前某个 dyadic 等分，$\tau_i$ 可能恰好有准确 binary64 载体，但一般接口不能默删该项。也可以直接用完整区间求值包围三个准确残差；那是 (15) 的合法替代，必须保留完整来源和全部实际差异，不把两种路径的未付部分互相抵消。

## 6. 本段准确零阶根及交叉逆界

在整个角胞及上一段已经认证的所有 $p/B$ 包围上，取一个准确解释的有限矩阵 $Y$ 和比较中心 $\widehat\eta_0$，考虑
$$
\mathbb B=\{\eta:\|\eta-\widehat\eta_0\|\le r\}.
$$
所有 $p_0+B_0^T\eta$ 必须留在本段所声明的数学控制域；若模型另声明一个控制半径，也要如实验证包含关系，不能把数值半径标签当作已经证明的条件。

设已有真正向外上界
$$
q\ge\sup_{\phi,\eta\in\mathbb B}
\|I-YG_\eta(\phi,\eta)\|<1,\qquad
z\ge\sup_\phi\|Y G(\phi,\widehat\eta_0)\|,
\qquad
z<(1-q)r.
\tag{16}
$$
这里残差须是整个角胞的准确残差；$Y$ 可以是一个保存的近似逆，但无需、也不能未经证明称为准确 $J^{-1}$。例如 $z=\|Y\|r_0$ 可用，直接区间乘积通常更紧。

把 R695 的收缩论证应用于本段准确方程 (4)，得到球内唯一根和
$$
d_0:=\frac z{1-q}\ge\|\eta_0-\widehat\eta_0\|,
\qquad
K:=\frac{\|Y\|}{1-q}\ge\|G_\eta(\phi,\eta_0)^{-1}\|.
\tag{17}
$$
简要核对：映射 $\eta\mapsto\eta-YG$ 的导数范数至多 $q$，中心偏移至多 $z$，故严格映入球内；$YG_\eta$ 的 Neumann 级数给可逆性。方阵情形同时推出 $Y$ 与 $G_\eta$ 可逆，并有
$G_\eta^{-1}=(YG_\eta)^{-1}Y$。这只是 R695 的预条件局部形式，不增添另一种存在前提。

严格余量和完整邻域使普通 IFT 能给根的角与参数光滑性。该结论只给本球唯一性，不给整个数值控制半径内唯一性，也不由一个角胞单独推出全圈同支。后者在第 13 节处理。

## 7. 两阶角根误差及其全部系数

固定上段真实曲线以后，(4) 的偏 $\phi$ 导数都包括 $p_j,B_j$ 和零控制右端的相应导数。在三个增量变量暂独立时，准确 jet 方程为
$$
\begin{aligned}
R_0&=G(\phi,\eta_0),\\
R_1&=G_\phi+J\eta_1,\\
R_2&=G_{\phi\phi}
 +2G_{\phi\eta}[\eta_1]
 +G_{\eta\eta}[\eta_1,\eta_1]+J\eta_2.
\end{aligned}
\tag{18}
$$
第 5 节的 $r_j$ 正是这些式子在
$(\widehat\eta_0,\widehat\eta_1,\widehat\eta_2)$ 上的完整误差上界。

取
$g_{ab}\ge\|\partial_\phi^aD_\eta^bG\|$
于整个根球和准确上游域，令
$h_j=\|\widehat\eta_j\|$。则
$$
d_1=K\{r_1+(g_{11}+g_{02}h_1)d_0\}
\tag{19}
$$
和
$$
\begin{aligned}
d_2=K\{r_2
 &+(g_{21}+2g_{12}h_1+g_{03}h_1^2+g_{02}h_2)d_0\\
 &+2(g_{11}+g_{02}h_1)d_1+g_{02}d_1^2\}
\end{aligned}
\tag{20}
$$
分别包围 $\|\eta_1-\widehat\eta_1\|$ 和
$\|\eta_2-\widehat\eta_2\|$。

**证明。** 对 $R_1$ 先固定 $\widehat\eta_1$，沿
$\widehat\eta_0$ 到真实 $\eta_0$ 积分。其导数为
$G_{\phi\eta}+G_{\eta\eta}[\cdot,\widehat\eta_1]$，
故误差至多 $(g_{11}+g_{02}h_1)d_0$。在真实 $\eta_0$ 处，
$R_1$ 对 $\eta_1$ 为同一 $J$，用 (17) 即得 (19)。

对 $R_2$ 同样先固定两个工作角 jet，沿零阶根积分，所需导数正好给 (20) 中乘 $d_0$ 的四项。随后在真实零阶根处改变一阶 jet；二次项差为
$2G_{\eta\eta}[\widehat\eta_1,\eta_1-\widehat\eta_1]
+G_{\eta\eta}[\eta_1-\widehat\eta_1,\eta_1-\widehat\eta_1]$。
连同线性 $2G_{\phi\eta}$，得到乘 $d_1$ 及 $d_1^2$ 的项。最后二阶 jet 仅乘同一 $J$，再用 (17)。右边没有未知 $d_2$，证毕。

### 7.1 从完整端点函数得到 $g$ 上界

这些系数不必视为未展开的黑盒。取真正上界
$B_j^*\ge\|B_j\|$、$P_j^*\ge\|p_j\|$，
$E=\|\widehat\eta_0\|+r$，并置
$$
V_1=P_1^*+B_1^*E,\qquad
V_2=P_2^*+B_2^*E.
$$
由链式法则可取
$$
\begin{aligned}
g_{02}&=F_{02}(B_0^*)^2,&
g_{03}&=F_{03}(B_0^*)^3,\\
g_{11}&=(F_{11}+F_{02}V_1)B_0^*+F_{01}B_1^*,\\
g_{12}&=(F_{12}+F_{03}V_1)(B_0^*)^2
                         +2F_{02}B_0^*B_1^*,\\
g_{21}&=(F_{21}+2F_{12}V_1+F_{03}V_1^2+F_{02}V_2)B_0^*\\
&\quad+2(F_{11}+F_{02}V_1)B_1^*+F_{01}B_2^* .
\end{aligned}
\tag{21}
$$
这里 $\eta$ 固定时 $v_\phi=p_1+B_1^T\eta$、
$v_{\phi\phi}=p_2+B_2^T\eta$。对
$G_\eta=f_uB_0^T$ 求两次角导数即得到最后一式；
另两种纯 $\eta$ 导数和一角两 $\eta$ 导数给其余式。
零控制右端在这些至少含一次 $\eta$ 的导数中消失，
但在 (15)、(18) 和全部外参数偏导中都不能消失。

## 8. 输出控制误差的逐段非循环递推

设本段实际工作输出为 $\widehat u_{i,j}$，
以 (12) 同样方式保留其实际输出加乘缺陷 $\chi_j^{\rm out}$。
若工作测试控制正是输出控制，可以用同一个已付缺陷；
若数值路径不同必须分别读取。由 (5) 的准确恒等式可取
$$
e_j^+=e_j^-+\chi_j^{\rm out}
+\sum_{k=0}^j{j\choose k}
\left(B_{j-k}^*d_k+b_{j-k}\|\widehat\eta_k\|\right).
\tag{22}
$$
它包围 $\|u_{i,j}-\widehat u_{i,j}\|$。

证明只需逐项写
$B^T\eta-\widehat B^T\widehat\eta
=B^T(\eta-\widehat\eta)+(B-\widehat B)^T\widehat\eta$，
然后加入真实 $p$ 误差和实际算术缺陷。此拆分已经包含所有误差乘积；不用另假定工作 $B$ 准确。

从 $u_0=0$ 的三套准确零 jet 开始，$e^-_0=e^-_1=e^-_2=0$。
每段按 (10)、(13)–(17)、(19)–(22) 顺序更新。
本段第二阶根误差只使用**上一段**已经支付的第二阶控制误差，
不存在把尚未证明的本段上界代回自身的循环。
不过误差可以随段数累积甚至变大；本文不保证任何当前 $m$ 已经足够。


## 9. 本段九维角 jet Jacobian 的准确逆界

把本段三个增量 jet 堆成 $E=(\eta_0,\eta_1,\eta_2)$。对式 (18) 逐项微分，定义
$$
\begin{aligned}
H_1 a&=G_{\phi\eta}[a]+G_{\eta\eta}[a,\eta_1],\\
H_2 a&=G_{\phi\phi\eta}[a]
 +2G_{\phi\eta\eta}[a,\eta_1]
 +G_{\eta\eta\eta}[a,\eta_1,\eta_1]
 +G_{\eta\eta}[a,\eta_2].
\end{aligned}
\tag{23}
$$
得到
$$
D:=R_E=
\begin{pmatrix}
J&0&0\\
H_1&J&0\\
H_2&2H_1&J
\end{pmatrix}.
\tag{24}
$$
令 $s_j=h_j+d_j$，并取
$$
\alpha_1=g_{11}+g_{02}s_1,\qquad
\alpha_2=g_{21}+2g_{12}s_1+g_{03}s_1^2+g_{02}s_2.
$$
逐块前代给出 $D^{-1}$ 的非负标量主控矩阵
$$
\mathsf M=
\begin{pmatrix}
K&0&0\\
K^2\alpha_1&K&0\\
K^2\alpha_2+2K^3\alpha_1^2&2K^2\alpha_1&K
\end{pmatrix}.
\tag{25}
$$
具体说，若 $D w=b$，则三个欧氏块范数组成的向量逐项不超过
$\mathsf M(\|b_0\|,\|b_1\|,\|b_2\|)^T$。因此
$$
\|D^{-1}\|_2\le
\Lambda:=\sqrt{\|\mathsf M\|_1\|\mathsf M\|_\infty}.
\tag{26}
$$
平方根也须向外包围。证明只使用 (17)、三次三维前代和
$\|\mathsf M\|_2^2\le\|\mathsf M\|_1\|\mathsf M\|_\infty$；
没有另假定一个未经验证的九维 inverse。

只有一阶角 jet 的路径取 (24) 的左上 $6\times6$ 块。
完整曲率、物理六 jet 及其参数导数使用整个九维块。
全 $m$ 段的下三角结构不允许只保最后一段的 $D$ 而忽略前段。

## 10. 完整外参数 J/J* 与工作线性化误差

### 10.1 每段准确的参数链

为避免漏掉上游依赖，暂把上一段三套六控制 jet 堆成独立变量
$P\in\mathbb R^{18}$，本段三套增量为 $E\in\mathbb R^9$。
令 $U_i(x,P,E)\in\mathbb R^{18}$ 是式 (5) 的完整输出，
其中 $B_0,B_1,B_2$ 全部由式 (9) 的完整函数计算。
令
$$
\mathcal R_i(x,P,E)=
\operatorname{Jet}_\phi^2 f(x,\phi,U_i)
 -(1-\tau_i)\operatorname{Jet}_\phi^2 f(x,\phi,0).
\tag{27}
$$
此处 jet 记号按式 (7) 的代数定义理解，不能把三套独立 $P$ 直接当作常数后删去其角链。

在准确同一分支上记
$$
D=\mathcal R_E,\quad
Q=\mathcal R_P,\quad
C=\mathcal R_x,\qquad
U_P,\ U_E,\ U_x
\tag{28}
$$
为完整偏导；这里 $Q$ 是一个 $9\times18$ 导数块，**不是**被冻结的十八字面旋转矩阵输入。
若不希望在实现中复用字母，可把它命名为 upstream_derivative_block。

设 $V^-=\partial_xP$、$W_E=\partial_xE$、$V^+=\partial_xU_i$。
隐式微分和乘积链准确给出
$$
D W_E+Q V^-+C=0,\qquad
V^+=U_x+U_PV^-+U_EW_E.
\tag{29}
$$
所有 $B_j$ 对 $x$、对上游三个控制 jet 的依赖都在这些块中。
右端零控制函数的全部 core、$\omega$、$H$、逆图和角链都在 $C$ 中。
初始 $V_0=0$ 只表示初始内部控制恒为零，不表示 $f(x,\phi,0)$ 对外参数的导数为零。

### 10.2 工作 J 的完整误差递推

令带帽量是当前实际工作线性化使用的块和方向算子。
每个块误差须由完整准确状态包围及真实计算误差支付，例如
$\delta_D\ge\|D-\widehat D\|$、
$\delta_Q\ge\|Q-\widehat Q\|$、
$\delta_C\ge\|C-\widehat C\|$，
以及 $\delta_{U_x},\delta_{U_P},\delta_{U_E}$。
它们包括第 4–8 节的根、上游、法向和 jet 不确定性；
不能只比较两个普通浮点自动微分结果。

令实际工作线性求解与输出的残差算子为
$$
\begin{aligned}
r_E^{\rm lin}
 &=\widehat D\,\widehat W_E
   +\widehat Q\,\widehat V^-+\widehat C,\\
r_U^{\rm lin}
 &=\widehat V^+
 -(\widehat U_x+\widehat U_P\widehat V^-
                         +\widehat U_E\widehat W_E).
\end{aligned}
\tag{30}
$$
表达式按保存字的准确实数解释；实际读取该表达式本身的运算误差仍须加到所用残差上界。若
$\epsilon_{V^-}\ge\|V^--\widehat V^-\|$，则
$$
\epsilon_{W_E}\le\Lambda\left(
 \|Q\|\epsilon_{V^-}
 +\delta_D\|\widehat W_E\|
 +\delta_Q\|\widehat V^-\|
 +\delta_C+\|r_E^{\rm lin}\|\right),
\tag{31}
$$
$$
\begin{aligned}
\epsilon_{V^+}\le{}&
 \|U_P\|\epsilon_{V^-}+\|U_E\|\epsilon_{W_E}
 +\delta_{U_x}
 +\delta_{U_P}\|\widehat V^-\|\\
 &+\delta_{U_E}\|\widehat W_E\|+\|r_U^{\rm lin}\|.
\end{aligned}
\tag{32}
$$

**证明。** 从 (29) 减去 (30)，把
$D(W_E-\widehat W_E)$ 单独移到左边。
剩余项分别是上游导数误差、三个块误差和实际线性残差。
用 (26) 得 (31)。输出式以同样的准确加减得到 (32)。
证毕。

这些式子可用于一个明确参数方向，也可用于声明 Hilbert 范数下的完整算子；后一种情形必须真正支付算子范数，不能由几条随机方向估计替代。可以利用完整块结构避免形成巨大的稠密参数矩阵，原全部变量和线性依赖仍须保留。

数值 Newton 迭代轨迹可以不被微分；本文比较的是实际工作零值隐式 surrogate 的**一次**参数线性化与准确选枝导数。value-anchor 的前向字和 active graph 的偏导须分别按 (12)、(30) 支付。此分析不宣称再对该 surrogate 自动求导就得到准确二次参数导数。

### 10.3 完整转置与其直接误差账

若准确输出控制 covector 为 $\lambda$，每段逆序执行
$$
D^T w=U_E^T\lambda,\qquad
g_x=U_x^T\lambda-C^Tw,\qquad
\lambda^- =U_P^T\lambda-Q^Tw.
\tag{33}
$$
对所有段从后往前迭代，累加每个 $g_x$，再加入实际物理输出的直接参数项。这是 (29) 的准确转置，不用反传 Newton 的有限迭代历史。

若工作值为 $\widehat\lambda,\widehat w$，并令
$$
r_w=\widehat D^T\widehat w-\widehat U_E^T\widehat\lambda,
$$
则 $\epsilon_\lambda\ge\|\lambda-\widehat\lambda\|$ 时可取
$$
\epsilon_w\le\Lambda\left(
 \|U_E\|\epsilon_\lambda+
 \delta_{U_E}\|\widehat\lambda\|+
 \delta_D\|\widehat w\|+\|r_w\|\right).
\tag{34}
$$
实际两个输出的乘加误差分别记为
$\varepsilon_{x,\rm arith}$、$\varepsilon_{P,\rm arith}$，于是
$$
\begin{aligned}
\|g_x-\widehat g_x\|
&\le\|U_x\|\epsilon_\lambda
 +\delta_{U_x}\|\widehat\lambda\|
 +\|C\|\epsilon_w+\delta_C\|\widehat w\|
 +\varepsilon_{x,\rm arith},\\
\|\lambda^--\widehat\lambda^-\|
&\le\|U_P\|\epsilon_\lambda
 +\delta_{U_P}\|\widehat\lambda\|
 +\|Q\|\epsilon_w+\delta_Q\|\widehat w\|
 +\varepsilon_{P,\rm arith}.
\end{aligned}
\tag{35}
$$
式 (34) 由真实转置方程相减得到，式 (35) 逐项用三角不等式。
这保留了每段反向算术误差；不能只说“转置范数相同”便忽略实际浮点反传的额外差。

### 10.4 接最终物理观察、归一化和 H² 坐标

若最终输出为 $\mathcal L(x,U_m)$，则
$$
J_{\rm out}=\mathcal L_x+\mathcal L_U V_m.
$$
例如已有 $\delta_{\mathcal L_x},\delta_{\mathcal L_U}$ 时，
工作差满足
$$
\|J_{\rm out}-\widehat J_{\rm out}\|
\le\delta_{\mathcal L_x}
 +\|\mathcal L_U\|\epsilon_{V_m}
 +\delta_{\mathcal L_U}\|\widehat V_m\|
 +\varepsilon_{\rm out,lin}.
\tag{36}
$$
固定准确 $a\rho_0$ 的归一化、正权观测和全部物理点的 cotangent 都必须在 $\mathcal L$ 中完整支付。隐式闭合仅消去内部控制，没有删掉原自由量或几何工作行。

若工作求解器最后使用白化坐标 $\widehat T$，准确声明的坐标为 $T$，还须使用例如
$$
\|J_{\rm out}T-\widehat J_{\rm out}\widehat T\|
\le \|J_{\rm out}\|\|T-\widehat T\|
 +\|J_{\rm out}-\widehat J_{\rm out}\|\,\|\widehat T\|.
\tag{37}
$$
原 integral/QR 的工作因子、宽度载体及三角解误差不能因闭合链的准确代数而被免除。相同责任适用于最终坐标转置。

## 11. 积分、四阶混合导数及实际数值费用

### 11.1 可直接复用 R694 的带符号低阶核

对 (2) 及所需混合导数的每一个向量或张量被积函数 $X$，
在准确物理胞宽度 $\ell\in[\ell_-,\ell_+]$ 上给出
$\|X\|\le B_X$、$\|\partial_sX\|\le L_X$。
采用真实工作节点、真实有符号权 $v_j$ 和正确的准确积分密度。
令质量缺陷 $m$ 和一阶 Peano 质量 $\kappa$ 按
[R694 第 3 节](R694-so3-low-order-signed-quadrature-error-algebra.md) 定义。
若工作宽度为 $\widehat\ell$、每个节点值完整误差为 $e_j$，
则同一证明给
$$
\begin{aligned}
\varepsilon_{\rm quad}\le{}&
 \ell_+|m|B_X+\ell_+^2\kappa L_X
 +\delta_\ell B_X\sum_j|v_j|\\
 &+\widehat\ell\sum_j|v_j|e_j+\varepsilon_{\rm sum},
\qquad
\delta_\ell=\max(|\ell_--\widehat\ell|,
                         |\ell_+-\widehat\ell|).
\end{aligned}
\tag{38}
$$
R694 的分部积分是有限维逐分量恒等式，因此对上述真正诱导范数也成立。
若实现从 entry 盒转成诱导范数，则该转换仍须明确支付。

不得假设 full Gauss 的浮点权和恰为一，不得把负 partial weights 删掉，
不得把不同 binary 节点合并。整个域的费用是全部真实胞的完整和；
替换尾、cutoff 接点和无穷振荡平尾仍按原准确标量定义包围。
节点位移、准确查询点与 carrier 查询点的差、角 $\pi$ 的载体误差、
以及实际构造权的误差，均进入同一实际求值责任。

### 11.2 四阶公式不免除更高一阶径向 Lipschitz 费用

式 (10) 以及 (28) 可以涉及 $f$ 的混合四阶导数。
若给其积分 integrand 使用 (38)，再取一次径向导数可能出现
$D^5\exp$。不能把 R694 中“该场六 jet 应用只需 $k\le3$”
无声当成已经实现了这里所有四、五阶误差消费者。

所需的解析范数界本身已有统一理由：对任意实斜对称 $X,H_1,\ldots,H_k$，
有序 Duhamel 单纯形公式由 $k!$ 个次序组成，
每个单纯形体积 $1/k!$，每个 $\exp(tX)$ 正交。因此任意有限 $k$ 均有
$$
\|D^k\exp(X)[H_1,\ldots,H_k]\|
\le\prod_{\nu=1}^k\|H_\nu\|.
\tag{39}
$$
这里没有 $e^{\|X\|}$ 损失，也没有把非交换矩阵当成可交换。
对四阶 integrand 求一次径向导数只再使用
$\mathcal W_s,\omega_s,T_{0,s}$ 及相应两阶角混合导；
它不要求第三阶径向导数 $F_{sss}$。
各具体乘积的完整组合数仍需由真实导数图或已证明的完整多线性展开给出。

式 (28) 的块误差可以用准确混合四阶导数的整个区间范围与工作块直接比较。
如果改用“该四阶导数的 Lipschitz 常数乘状态误差”，
那是额外的五阶参数正则性责任，不能凭空假定。
直接区间比较不需要这项额外假设，可能较松，但完整。

### 11.3 工作费用必须指向真实计算路径

R694 第 6 节给的是当前 core 位置及两阶物理角 jet 的逆图误差；它本身不认证这里外参数块中实际出现的 core 逆图混合导数。这些导数必须对同一个准确方程 $\Theta_c(\phi_c)=\theta_0$ 完整隐式微分或直接作区间比较，并支付数值有限迭代/AD 路径的差。只需所列块真实使用的导数，不额外要求未出现的径向高阶量。

第 4–10 节的每个 $\varepsilon$ 或 $\delta$ 均须明确由什么实际对象产生。
至少包含实际涉及的以下部分：

- 当前准确标量所有分段、完整尾及 $S$、帽半径、符号径向节点与工作载体之间的差；
- 当前 core 逆图的真实残差、正 $\rho_c$、support 和三角函数误差，以及固定材料图本身的载体；
- 工作 SO(3) 小分支多项式或其它指数实现的截断与舍入，大分支函数及其实际分支边界；
- 每个实际积分节点与权、非零质量缺陷、负权、准确/工作宽度和所有加权归约；
- 求 $B_j$ 和全部混合导数时真实 AD 图与数学导数的差、缓存前向 anchor 的差；
- 按准确 $S$ 归一化与实际工作 $\widehat S$ 归一化的差；
- 三维/六维/九维线性解、转置、矩阵乘法和残差读取的完整浮点误差。

例如向量 $c$ 和工作 $\widehat c$、$S\ge S_->0$、
$\widehat S>0$ 时，
$$
\left\|\frac cS-\frac{\widehat c}{\widehat S}\right\|
\le\frac{\|c-\widehat c\|}{S_-}
 +\frac{\|\widehat c\|\,|S-\widehat S|}{S_-\widehat S}
 +\varepsilon_{\rm div}.
\tag{40}
$$
这说明一个很小的工作无量纲残差并不自动是准确物理闭合残差盒。
完整闭合物理残差为 $S f$，其 carrier 乘法同样须按真实路径支付。

以上都是证书的输入责任，本文没有把任何尚未实现的高阶节点核写成已返回结果。
同一真实场上可以增加积分子胞、提高向外精度而不改 (1)；
改变 (1) 本身则定义另一有限选枝，须另记身份和实际 baseline。

## 12. 从末段控制误差到完整六个物理 jet

### 12.1 旋转角的全部混合 jet

末段控制 $u_j$ 只依赖 $\phi$ 和 $x$，不依赖径向 $s$。
设 $w=\mathcal W u_0$。完整所需 jets 是
$$
\begin{aligned}
w&=\mathcal W u_0,&
w_s&=\mathcal W_su_0,\\
w_\phi&=\mathcal W_\phi u_0+\mathcal W u_1,&
w_{s\phi}&=\mathcal W_{s\phi}u_0+\mathcal W_su_1,\\
w_{\phi\phi}&=\mathcal W_{\phi\phi}u_0
       +2\mathcal W_\phi u_1+\mathcal W u_2,&
w_{s\phi\phi}&=\mathcal W_{s\phi\phi}u_0
       +2\mathcal W_{s\phi}u_1+\mathcal W_su_2.
\end{aligned}
\tag{41}
$$
不能在每个径向位置重解根，再把该新结果称为同一 meridian 控制。

若末段 $e_j$ 已付，而实际 $\widehat{\mathcal W}$ 的各 mixed jets
也有误差 $b_{\mathcal W,a}$ 和真实范数上界 $\mathcal W_a^*$，
每一个乘积项用
$$
\|\mathcal W_a u_j-\widehat{\mathcal W}_a\widehat u_j\|
\le\mathcal W_a^* e_j+
 b_{\mathcal W,a}\|\widehat u_j\|
\tag{42}
$$
再加该输出的真实算术费用即可。
式 (41) 的系数 $1,2,1$ 完整保留。
所有范数现在同为欧氏/谱范数，不存在把坐标无穷范数误当二范数的隐含转换。

### 12.2 指数及被积函数的节点误差

记相应旋转角 jet 误差为
$e_w,e_{w_s},e_{w_\phi},e_{w_{\phi\phi}}$。
比较准确指数 $R=\exp([w]_\times)$
与在工作角上使用**准确指数和准确导数**得到的中间量。
由 (39) 及线段积分，可取
$$
\begin{aligned}
e_R^{\rm in}&=e_w,\\
e_{R_s}^{\rm in}&=e_{w_s}+\|\widehat w_s\|e_w,\\
e_{R_\phi}^{\rm in}&=e_{w_\phi}+\|\widehat w_\phi\|e_w,\\
e_{R_{\phi\phi}}^{\rm in}
 &=e_{w_{\phi\phi}}+\|\widehat w_{\phi\phi}\|e_w
 +2\|\widehat w_\phi\|e_{w_\phi}+e_{w_\phi}^2
 +\|\widehat w_\phi\|^2e_w.
\end{aligned}
\tag{43}
$$
例如二阶式来自
$R_{\phi\phi}=D\exp[w_{\phi\phi}]
 +D^2\exp[w_\phi,w_\phi]$；
先固定两个工作方向改变基点，再改变方向，正好产生所列项。
实际 Rodrigues/指数与导数计算相对这些中间量的误差再分别加入，
得到真正 $e_R,e_{R_s},e_{R_\phi},e_{R_{\phi\phi}}$。

记准确未修正单位 meridian 为 $U=T_y$，
其工作节点 jet 的完整误差为
$e_{U,0},e_{U,s},e_{U,1},e_{U,2}$。
当前完整 integrand 为 $T=RU$。
用真实旋转导数范数上界 $R_a^*$，可取
$$
\begin{aligned}
e_T\le{}&e_{U,0}+e_R\|\widehat U\|+\varepsilon_{T,\rm arith},\\
e_{T_s}\le{}&R_s^*e_{U,0}
 +e_{R_s}\|\widehat U\|+e_{U,s}
 +e_R\|\widehat U_s\|+\varepsilon_{T_s,\rm arith},\\
e_{T_\phi}\le{}&R_\phi^*e_{U,0}
 +e_{R_\phi}\|\widehat U\|+e_{U,1}
 +e_R\|\widehat U_\phi\|+\varepsilon_{T_\phi,\rm arith},\\
e_{T_{\phi\phi}}\le{}&
 R_{\phi\phi}^*e_{U,0}
 +e_{R_{\phi\phi}}\|\widehat U\|
 +2R_\phi^*e_{U,1}
 +2e_{R_\phi}\|\widehat U_\phi\|\\
&+e_{U,2}+e_R\|\widehat U_{\phi\phi}\|
 +\varepsilon_{T_{\phi\phi},\rm arith}.
\end{aligned}
\tag{44}
$$
这些式子由每个乘积准确加减得到，$R$ 的范数准确为一。
对 $T,T_\phi,T_{\phi\phi}$ 的连续范数和径向 Lipschitz 界，
把式 (41) 的完整真实界代入 R694 的 (5.2)–(5.3) 即可；
所有 $w_{s\phi},w_{s\phi\phi}$ 项保留。
对于 direct R690 的单位参考，不必人为重新引入旧父 $F_s$ 的归一化费用；
但它自己的准确标量/节点误差仍要支付。

### 12.3 准确零闭合场和真实六 jet

准确末段 $f=0$ 后，物理场定义为
$$
F(s,\phi)=P(\phi)+\int_S^s T(r,\phi)\,dr.
\tag{45}
$$
令 $I_j$ 支付该同一有符号积分的第 $j$ 阶角 jet，
$P_j$ 支付实际 cap jet，$j=0,1,2$。
R694 的核可直接用：
查询胞前的积分密度为零，后的完整胞为 $-1$，
查询胞取 $0$ 与 $-1$ 的分段密度，并使用实际 partial-minus-full 权。
若工作代码分别求两个积分再相减，实际相减费用也须保留。

由 (45) 得
$$
\begin{aligned}
e_F&\le P_0+I_0+\varepsilon_{F,\rm arith},&
e_{F_s}&\le e_T+\varepsilon_{s,\rm arith},\\
e_{F_\phi}&\le P_1+I_1+\varepsilon_{\phi,\rm arith},&
e_{F_{ss}}&\le e_{T_s}+\varepsilon_{ss,\rm arith},\\
e_{F_{s\phi}}&\le e_{T_\phi}+\varepsilon_{s\phi,\rm arith},&
e_{F_{\phi\phi}}&\le P_2+I_2+\varepsilon_{\phi\phi,\rm arith}.
\end{aligned}
\tag{46}
$$
这里没有 $h\Delta$ 项，因为准确闭合已经由整条选枝链证明。
不能在只有工作根残差时先删掉其误差，
也不能把工作 $F(0)$ 直接覆写成 $\Gamma$ 后漏付原积分差。
准确 core 端口来自 (2) 的准确零与其准确角导数。

准确 $|F_s|=1$ 仅是径向 Gram 恒等式。
剩余混合和角向 Gram、固定目标归一化、embedding、全像幅度、
reach 仍须同场真实支付。
以 (46) 接 R694 第 8 节的固定分母谱误差，可比较工作 Gram 与准确 Gram；
不得换成当前 core 的 $\rho_c$ 作为目标分母来缩小误差。

## 13. 全角同支、反射、端口和物理全相位

上述推导逐段以“上一段是同一准确曲线”作为归纳前提。
在相邻角胞交界处，同一 $x$、标量、固定材料图、字面 $Q$、支持及
共同分段使两边的准确 $G$ 是同一个函数。
为了把两个局部根认作同支，足够条件是：
在共同交界角，**一边已经得到的准确根包围包含于另一边的唯一性球内**。
仅有两个盒相交不够。应按有向包含及已付根盒逐段完成拼接，
并对最后周期接点也如此处理。

对 R703 的正交空间变换 $P_{\rm sp}$，
六控制按 $D_{\rm ctl}=\operatorname{diag}(P_{\rm sp},
\det(P_{\rm sp})P_{\rm sp})$ 变换。
由完整协变式
$A(\phi',D_{\rm ctl}u)=P_{\rm sp}A(\phi,u)D_{\rm ctl}^T$，
本段增量按 $\eta'=P_{\rm sp}\eta$ 变换。
欧氏球的正交像可准确处理；若改用坐标盒，
一般正交映射须真做盒像，不能当作符号置换。
变换后的根包围须进入对应唯一性域，
或另以同一可逆连续分支关联，才能推出 quarter 轴和周期的全部角迹。
各角独立一个局部根不替代此责任。

严格根盒余量、真实可逆性和混合正则性给 IFT 的局部开邻域；
相邻唯一性与协变把这些局部分支拼成同一 $C^2$ 角曲线。
每段沿同一上游分支归纳，因此最终控制是同一个全角选择，
并保原全部外参数的一次隐式导数。
同一个 checkpoint 身份本身不足以证明工作载体关联了哪条准确根分支：
还须保存对应段/角地址、工作增量与 jet 的来源、准确根包围、
同一方程身份和上述关联证据。
不同 producer report 可以作为同一数学场的不同包围证据合并，
不能因此强求它们的文件 SHA 相同；每份证据仍须可追溯。

两 bubble 和 $\gamma$ 的支持紧含于 $(0,S)$，
所以校正于 core/cap 邻域恒等于零，保原未修正 meridian 的端 jet。
准确闭合给 $F(0)=\Gamma$ 及两阶角迹；
准确单位 core 端向量 $e_z$ 给 $T_{s,z}=0$，
所以原中圈反射的 $C^2$ 条件保留。
帽端由锚定积分及原准确径向/Cartesian 端口保留。
这些是 R703 的条件端口结论，不宣称已经为任一当前失败输入生成曲面。

辅助 $\tau_i$ 不是课题物理相位 $t$。
[R248](R248-finite-C2-phase-family-and-global-reductions.md)
的准确相位表达及
[R650](R650-positive-definite-flow-support-reach.md)
的支持/reach 机制若被采用，仍须消费**新场本身**的完整连续输入、
固定帽和所需正下界。新闭合层不继承旧候选的幅度、曲率或 reach 证书，
也不由有限 $t$ 样本宣称全相位成立。
[R661](R661-complete-nonplanar-activity-and-four-fixed-markers.md)
的旧数值非平面性或含反射欧氏商读数也不跨字段转移。

## 14. 完整条件传播定理及可执行数据合同

**定理。** 固定式 (1)–(2) 的完整数学输入和一个实际完整外部点。
假设有覆盖整个角圈的有限角胞；从 $u_0=0$ 起，对每段、每胞：

1. 全部准确域、混合导数及实际工作值误差覆盖第 1、4、5、11 节的责任；
2. 真实交叉矩阵和中心残差满足 (16)，控制域包含成立；
3. 按第 13 节关联相邻、周期及反射分支；
4. 实际工作参数线性化若被认证，另付第 10 节的全部块和算术费用。

则式 (10)、(15)、(17)、(19)–(22) 给最终准确控制及两阶角 jet
相对工作载体的完整误差；式 (26)、(31)–(35) 给完整一次外参数
J/J* 的误差；式 (38)、(41)–(46) 给同一准确零闭合物理场的
完整六 jet 工作误差。

**证明。** 初始三套控制 jet 和参数导数为准确零。
第 $i$ 段先由已证上游误差和 (8) 得真实法向平面三 jet 包围，
再由完整工作误差拆分得到 (15)。
(16) 的收缩和 IFT 给本段准确根、同一交叉 inverse 及局部光滑性。
(18) 的逐项比较给两阶角误差，乘积恒等式 (5) 给新控制误差。
全角关联使这些局部根归入同一准确分支，可作为下一段的归纳前提。
有限重复至 $m$，且 $\tau_m=1$，所以末段准确 $f=0$。
全参数链是 (27) 的下三角串联，前代和逆序转置给第 10 节；
最后准确旋转、积分和物理恒等式给第 12 节。证毕。

一个真正执行此证明的消费者应至少保存以下紧凑、可恢复记录：

- 完整 source/model/reference/scalar/chart/Q/支持/分段身份和当前全部自由点摘要；
- 每段角胞地址、对应工作根和 jet 的可恢复出处、准确根域、控制域包含及分支关联；
- 交叉矩阵包围或可复核的有限表示、$Y,q,z,r,K$ 和本段三套残差/误差上界；
- 上游三 jet、法向三 jet、当前输出三 jet 及所有费用项的区分，完整覆盖集合；
- 如认证 J/J*，所用外参数范数、块误差、实际线性解残差及转置/坐标费用；
- 全径向积分覆盖、全部真实尾、节点/权/宽度出处及完整六 jet 的同场消费结果。

不需要公开巨大根矩阵或可重算工作 raw；源码、准确参数、运行身份、紧凑合法上界和必要覆盖证据必须完整。
没有实际矩阵或根返回时应报告未读取，不能补零或继承别的候选。
某段条件未闭合只说明这一份认证尚未建立；
可以细化同一场的包围、改实际科学输入或改表示继续研究，
不能据此宣布课题无解或停在条件总结。

本文的正常源码参照是完整
so3_zero_normal_lift_operator.py，
SHA256 42ea8ec5920e3815b99c83c41448efb38ee37860f4d9362ddea6bce2418d39fe。
它明确保存共同准确分段，逐段保原零阶/一阶载体再升级二阶，
并用完整前段图构造一次隐式线性化。
本文没有把该普通浮点实现或其尚未返回的任何科学运行当成已经支付上述费用。
显式初高度的独立入口只改变当前完整自由点；在同一严格模型绑定下，
本证明同样适用，但必须使用它自己的实际工作返回。
