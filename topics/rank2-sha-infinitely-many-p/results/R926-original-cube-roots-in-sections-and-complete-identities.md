# R926 — 原 RF/Ri 的完整截面分式与全局立方恒等式

日期：2026-11-20。

**状态：本篇的精度、分式识别与全部全局身份接受门已证明；实际原立方根前端尚待公开 Actions 回执。原 F/P 与 vF/Yi 的既有 PASS 不自动填成本篇的新计算 PASS。**

本篇接 [R924§6.2、§15](R924-original-section-divisor-algebras-and-shadow-interface.md) 的同一原函数。固定已实际认证的成功权 $k_F=4$、$k_P=6$，不换目标曲线、原微分、常数嵌入、首项、Artin 顺序或完整返回。以下在 $r=29,41$ 的原常数域中成立；首次请求仍取 $r=29$。

## 1. 已存在的原函数和完整恢复空间

令 $B=X_0(867)$、$g_B=85$，$L=\Omega_B(\mathcal C_B)$、$\deg L=204$，
$R_m=H^0(B,L^m)$，$V_m=R_m/S^m$。原 $S(\infty)=1$，而
$$
\dim R_m=204m-84\qquad(m\ge1).
$$
R924§15 已准确恢复
$$
v_F=\frac{A_F}{D_F},\qquad A_F\in R_5,\quad
D_F=B_FS^3\in R_5,\quad B_F\in R_2,
\tag{1}
$$
$$
Y_i=\frac{A_i}{B_i},\qquad A_i,B_i\in R_3\quad(i=0,1,2).
\tag{2}
$$
两份原特征零完整证书须先由实际 job/run/head/source/hash 鉴定；这些分式随后按 R881 识别同一原约化。

R882 和 R924 已证明原函数 $R_F,R_i\in k(B)$ 的存在，并给
$$
R_F^3=v_F^2\frac{(T+27)^3}{T^3}-\frac{17}{T+27},\qquad
R_i^3=\frac{Y_i(Y_i+v_{\mathrm{new},i})}{(T+27)^2},
\tag{3}
$$
以及所有原首项 $R_F(\infty)=R_i(\infty)=1$。这里 $T=T_3(Q)$，极除子 $P_T$ 的次数为306，原 $Q=0$ 在 $P_T$ 中的系数为1。本篇以(3)恢复这些已存在的原函数，不从任意形式立方根发明一个新覆盖。

R924 的完整极次数帽为
$$
\deg\operatorname{pole}(R_F)\le1088,\qquad
\deg\operatorname{pole}(R_i)\le612.
\tag{4}
$$
所以取
$$
R_F=N_F/E_F\quad(N_F,E_F\in R_6),\qquad
R_i=N_i/E_i\quad(N_i,E_i\in R_4).
\tag{5}
$$
这些分式确实存在：乘掉原极除子的分母空间，Riemann–Roch 分别给维数下界
$1224-1088+1-85=52$ 和 $816-612+1-85=120$。分子由乘原函数得到，并仍在同一个完整截面空间中。

对同一原 $R_F$，任一候选差 $N_F-R_FE_F$ 的全部零次数上界为 $1224+1088=2312$。因此核完 $Q^0,\ldots,Q^{2312}$，就准确得到全部分式空间。对 $R_i$ 的相应界为 $816+612=1428$。完整线性系统为
$$
[\,R_6\mid -R_F R_6\,]\quad\text{在全部2313项上},\qquad
[\,R_4\mid -R_i R_4\,]\quad\text{在全部1429项上}.
\tag{6}
$$
两边维数分别1140和732；完整核维至少52和120。两投影均单射：如果其中一个截面为零，另一个也因原函数非零而为零。保全部原窗口、全核回代及两个投影的秩；一条选出的分式须保非零分子分母和原首项1。共同零可以存在，之后由 R925 的完整理想处理，不在这里把分母零点都判成原极点。

## 2. 从已认证截面取得足够长的原级数

原良素数形式输入已经按 R881 付了其精度损失。无须把那条 $p$ 进递推重新延到本篇较长窗口：保持同一 PARI 原 $M_2$ 基和同一个有理整格变换，继续它们的真实全局 $Q$ 展开即可。

统一把原120条 $M_2$ 基延到 $N=2725$ 项；逐项核全部旧1429项相同、原有理变换未变，以及所有新系数在 $r$ 处整。原乘积 recipes 不变，只在需要的窗口评价真实截面乘积。

因为 $B_F\in R_2\setminus\{0\}$，$\operatorname{ord}_\infty B_F\le408$；$S$ 在该点为单位，所以 $D_F$ 阶相同。由(1)的原 $v_F(\infty)=-1$，分子阶也相同，故它的商至少保留 $N-408=2317$ 个真实正则系数。对(2)，$\operatorname{ord}_\infty B_i\le612$，$Y_i$ 有简单极，因此正则的 $QY_i$ 至少保留 $N-612=2113$ 项，足够本篇的1429项。

这两个都是安全下界；实现还须读取实际 series 的绝对精度。不得把未知高项当零。已知有限多项式系数不是对原函数无限尾的零声明。

记
$$
\tau=QT_3(Q),\qquad\zeta=\tau+27Q=Q(T+27),
\qquad \tau(0)=\zeta(0)=1.
$$
由原 Euler 乘积精确给
$$
\tau=\left(\frac{\prod_{n\ge1}(1-Q^n)}{\prod_{n\ge1}(1-Q^{3n})}\right)^{12}.
\tag{7}
$$
可用同一原 `euler_series` 的 Euler 五边形展开和单位除法读取任意完整有限窗；这不在特征 $r$ 中除以可能为零的整数 $n$。它与 R924 的整数对数递推计算同一个原 eta 商，而不是换一个任意形式参数。

(3)的正则右端准确成为
$$
H_F=v_F^2(\zeta/\tau)^3-17Q/\zeta,\qquad
H_i=(QY_i)(QY_i+v_{\mathrm{new},i}Q)/\zeta^2.
\tag{8}
$$
这些单位的常数项均为1。因 $3\in k^\times$，Newton 更新
$$
R_{\mathrm{new}}=\frac{2R+H/R^2}{3}
\tag{9}
$$
从首项1开始唯一逐次倍增。每一步检查完整当前窗口的 $R^3-H=0$，保留全部前缀。新的迭代近似可选高项为零作为计算起点；这不允许把输入原 $H$ 的未知项补零。到达2313或1429项后，将同一个原根送入(6)。

## 3. 原 RF 的全局恒等式必须核到哪一项

将(1)、(5)代入原第一式(3)，清除全部真实分母后，得到
$$
\begin{aligned}
\mathcal E_F={}&N_F^3D_F^2T^3(T+27)
-E_F^3A_F^2(T+27)^4\\
&+17E_F^3D_F^2T^3.
\end{aligned}
\tag{10}
$$
每个原截面乘积的总幂数为 $3\cdot6+2\cdot5=28$；关于 $T$ 的有理函数额外极最多为 $4P_T$。所以非零 $\mathcal E_F$ 的全部零次数最多为
$$
28\cdot204+4\cdot306=6936.
\tag{11}
$$
在原无穷点乘 $Q^4$ 后得到正则局部截面，其实际多项式式为
$$
\boxed{Q^4\mathcal E_F
=N_F^3D_F^2\tau^3\zeta-E_F^3A_F^2\zeta^4
+17Q E_F^3D_F^2\tau^3.}
\tag{12}
$$
**完整接受门是(12)的全部 $Q^0,\ldots,Q^{6940}$ 为零。** 这使原 $\mathcal E_F$ 在无穷点的阶至少 $6941-4=6937>6936$，所以原全局恒等式严格成立。此处故意保这个统一保守窗，不用短展开、抽样系数或形式微分方程代替它。

## 4. 原三 Ri 的全局恒等式

同理原第 $i$ 个 P 恒等式的全部清分母残差为
$$
\mathcal E_i=N_i^3B_i^2(T+27)^2
-E_i^3A_i(A_i+v_{\mathrm{new},i}B_i).
\tag{13}
$$
截面幂数为 $3\cdot4+2\cdot3=18$，额外极为 $2P_T$，故全部零次数帽为
$$
18\cdot204+2\cdot306=4284.
\tag{14}
$$
其正则完整表达式准确为
$$
\boxed{Q^2\mathcal E_i
=N_i^3B_i^2\zeta^2
-Q^2E_i^3A_i(A_i+v_{\mathrm{new},i}B_i).}
\tag{15}
$$
**完整接受门是每个原嵌入的(15)全部 $Q^0,\ldots,Q^{4286}$ 为零。** 此时原残差在无穷点的阶至少4285，严格超过4284，故每条都是同原曲线上的全局身份。

原嵌入0可以用 $\mathbf F_r$ 计算；嵌入1使用原固定 $k=\mathbf F_{r^2}$。嵌入2可由嵌入1对常数作 $c\mapsto c^r$ 得到，但仍须回代它自己的原 $v_{\mathrm{new},2}$、原 $QY_2$ 和完整(15)，并保首项1。它不是原 Artin 置换(2,0,1)本身，二者不得互换。

## 5. 完整高窗的同基分组评价

最高原 $M_2$ 精度取6941；同一120维原格再次延长，保旧2725项、同有理变换和逐项整性。为了计算(12)、(15)，只须评价已经选定的 $N,E,A,B$，无须把所有 $R_6$ 乘积基都扩成高维系数矩阵。

若一个截面由同原乘积 recipes $I=(i_1,\ldots,i_m)$ 及系数 $c_I$ 表示，则按长度 $m-1$ 前缀分组：
$$
\sum_I c_I F_{i_1}\cdots F_{i_m}
=\sum_J\left(\prod_{j\in J}F_j\right)
\left(\sum_i c_{(J,i)}F_i\right).
\tag{16}
$$
在 $k[Q]/(Q^N)$ 中，截断同乘法兼容。所有 $F_i$ 都是同原全局截面且各项精度足够，因此(16)逐次截断给完整目标窗，不是数值近似。全部旧产品前缀和所选截面的低窗须与原读取一致。

为了避免新选有限域根，直接用消费者的原 $\omega$，$\omega^2+\omega+1=0$。一个 $k[Q]$ 元素保存为两条 $\mathbf F_r[Q]$ 多项式 $a+b\omega$；其乘法严格是
$$
(a+b\omega)(c+d\omega)
=(ac-bd)+(ad+bc-bd)\omega.
\tag{17}
$$
若 Sage 的默认生成元与原 $\omega$ 不同，先通过原 $1,\omega$ 的实际两维坐标变换读取系数，并完整回代原系数。不独立选另一立方单位根，不把两个分量的身份窗口分开缩短。

## 6. 公开执行和下游接口

本篇先鉴定原 F/P 两份完整成功证书，再在同一个断网 Sage 进程内取得原截面和原根。输出在内存中保：原120维格与变换、完整产品 recipes、F 的真实 $B_FS^3$、每个原 $N/E$、完整核、各原嵌入、全低窗和(12)、(15)的实际回执。只将源码、参数、source/run/job/hash 与证明结论入库，不输出或储存重算系数数据库。

这些同次分式可直接进入 [R925§5](R925-original-ys-affine-rings-and-complete-divisor-ideals.md) 的三个真实退化及306维整环；所有 $j^m$、$S$ 因子和原常数域仍保留。原 F/P 低核、原 cube 身份、完整整环、四个大交除子和最终原 shadow 是逐项的接受门，任何前一项通过都不代后一项。

本篇没有新增通常全 Selmer、ordinary、中央非零或跨无穷不同 $p$ 的结论；主目标仍按 HANDOFF 四个原前沿继续。

### 来源

- [R882](R882-original-degree18-source-model-and-two-endpoint-coordinates.md)、[R883](R883-original-relative-six-shadow-and-complete-boundary.md)：同一原曲线、原根的全局存在、无穷支及完整消费者。
- [R924§6.2、§15](R924-original-section-divisor-algebras-and-shadow-interface.md)：原完整极帽与截面恢复，以及原 vF/三 Yi 的实际全局分式回执。
- `produce-original-shadow-local-input.py` 的原 `euler_series`：与原形式输入共用的 Euler 五边形系数实现；本篇(7)–(17)证明其新窗口中的使用及全局接受界。


## 7. 完整producer接入与公开请求

`produce-original-cube-section-fractions.py` 已经实现§1–6的全部门；root读完全文，两名独立审阅者检查完整二次常数域的Fp核限制、原根首项、所有分母和全局高窗。原嵌入1的完整Fp块为 `[[M0,M1],[-M1,M0−M1]]`，转回原k后另核完整k秩与两分量残差。嵌入2不仅取常数Frobenius，还回代其自己的原QY/常数及完整4287项身份；整个6941项所选分子/分母同时核常数共轭。原map_context的旧1429项前缀不变，高窗单独保留供同原环嵌入鉴定。

host先鉴定§6所述真实F/P完整证书，再以固定镜像断网运行；令牌只在host认证日志，未传入数学容器。新workflow只由本请求/源码变化触发。这里只做过本地AST/YAML及静态证明检查，尚无新cube计算PASS。

| 源文件 | SHA256 |
|---|---|
| `produce-original-cube-section-fractions.py` | `71bbd011acdcc75d27647578c83751bac4bf64a3ac81c87a63b607417754fd42` |
| `launch-original-cube-sections.py` | `51ab6d3a8ab40d57f12fa6dba0a06c8cac9ef06162063e3cf90f9a959528218a` |
| `rank2-sha-original-cube-sections.yml` | `6a5c98af159b8a181ecd6644ea91061eabc26302c853e31df8ae082fe9b51479` |

原始F/P凭据分别钉在run43906594646/job133436977753/source135b50ff04a12c51dd1b9de583a20b2bed19cbed和run44714703201/job136215000168/sourceb688d6ac703fec422a7c864bcdc997cc553185fd；完整result hash见请求JSON及R909§7、R906§8。
