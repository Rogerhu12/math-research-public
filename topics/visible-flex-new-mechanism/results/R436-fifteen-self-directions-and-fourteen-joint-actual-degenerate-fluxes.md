# R436：P 支路的十五个 self 方向与同一实际圆十四个内部点的联合支付

日期：2026-11-16。**完整原式纸面证明；没有执行新的 profile、求根、积分、符号程序、秩、人工测试或科学运行。**

[R435](R435-complete-local-self-currents-and-joint-actual-internal-flux-control.md) 给原局部轨道 $K_0,\ldots,K_{10}$ 的完整 self current。其至多十一个同形对应点的结论不能直接覆盖同包的不同退化点。本稿使用 [R432](R432-complete-zero-order-kernel-and-all-degenerate-point-response-matrices.md) 已分类的零阶零第三核，专取原 $P$ 支路，得到四个新的 self 方向；它们在当前全部消-self 行上仍准确为零。

新增结论不只是一张形式列清单：在同一个实际镜点对和已有完整复制库内，可以联合支付 **11 个左对应点加 3 个不同右对应点**。全部原 $J^+=(E,\mathcal A,\mathcal O)$ 同时保持，若其它 C 已按同一联合接口支付也能保持。无需新母条件、额外 profile 运行或重新安置原点。

一个另外的 jet 比值条件可以支付第十五点，但本文不假定已冻结母必然满足它。对更多点，文末给出本明确模块的准确像，仍不把其限制冒称全响应障碍。

## 1. 原 P 支路的真实 self 和真实尾

采用共同右锚
$$
P(u,u)=J(r^2),\qquad p=u',\quad r=u'',\quad t=u'''.
$$
令
$$
A_u=6pt-2r^2.
$$
R432 的五个原方向为
$$
Z_{c0}=\operatorname{span}\{\sigma,\tau_0,\tau_1,\tau_2,\tau_3\},
$$
其真实自伴系数满足 $c=0$、$(a r)'+bp=0$，并有
$$
\begin{array}{c|c}
\text{方向}&a\\ \hline
\sigma&p^2\\
\tau_0&A_u\\
\tau_1&xA_u+2pr\\
\tau_2&x^2A_u+4xpr-4p^2\\
\tau_3&x^3A_u+6x^2pr-4xp^2 .
\end{array}
\tag{1}
$$
这些都是 R432(5)的完整原算子，不是另猜的局部微分系数。

置
$$
J_\sigma=\mathcal B_P\sigma,\qquad
J_j=\mathcal B_P\tau_j\quad(0\le j\le3).
\tag{2}
$$
$\tau$ 在原第三对角核中，R432(25)—(27)给真实 self
$$
J_\tau(u^2,0)=2K_u^\tau(P(u,u)),\qquad
\int_\ell^x p\,[J_\tau(u^2,0)]''
=2a_\tau\{pP''-rP'\}.
\tag{3}
$$
$P'=-r^2,\ P''=-2rt$，故
$$
\int_\ell^x p\,[J_\tau(u^2,0)]''
=2a_\tau r(r^2-2pt).
\tag{4}
$$
左端常数由原平零 jets 支付；没有假设 P 左紧。
在 $A_u=0$ 点，(4)变为
$$
\boxed{\mathcal F_x(J_\tau;u)=\frac23a_\tau r^3.}
\tag{5}
$$

原 P 的右包左尾为常数 $p_P(n)=n_0$。
因此 R432 的所有真正 suffix 导数在 P 支路都为零；
更直接地，$c=0$ 时 $\mathscr A_{\tau,u}(\text{constant})=0$，原右三常数给
$K_u^\tau(\text{constant})=0$。
这并不把同包 self 的左仿射尾设为零。

对原圆
$$
f=\sum_i a_i u_i,\quad g=\sum_i b_i u_i,\quad
R_i=a_i^2-b_i^2,\quad T_i=a_ib_i,
$$
完整两通道因而为
$$
\boxed{
H_{d,i}(J_\tau)=a_i^3R_i\mathcal F_x(J_\tau;u_i),
\qquad
H_{e,i}(J_\tau)=-a_i^3T_i\mathcal F_x(J_\tau;u_i).
}
\tag{6}
$$
其原未扣平台规范与 R435 相同；本列在外 collar 的第二导数为零。
所以
$$
\boxed{C_i(J_\tau):=R_iH_{e,i}+T_iH_{d,i}=0}
\tag{7}
$$
对同一圆全部包、全部点成立，非只对本稿选中的行。

由 R432 的完整 whole-E 核及 R344/R352 的全响应自然零，
$$
\boxed{\mathcal B_PZ_{c0}\subset\mathcal R\cap\ker E\cap\ker J^+.}
\tag{8}
$$
(8)不宣 universal self 自然零可实际同时构造；它只是这些 signed 响应的准确身份。

## 2. 四条新的完整 self 列与十五个形式方向

将(1)代入(5)：
$$
\boxed{
\begin{aligned}
\mathcal F_x(J_\sigma)&=\frac23p^2r^3,\\
\mathcal F_x(J_0)&=0,\\
\mathcal F_x(J_1)&=\frac43pr^4,\\
\mathcal F_x(J_2)&=\frac83(xpr^4-p^2r^3),\\
\mathcal F_x(J_3)&=4x^2pr^4-\frac83xp^2r^3 .
\end{aligned}}
\tag{9}
$$
这些是全部原 self partial；不是只列其三阶平方部分。

定义
$$
\mathscr M=\operatorname{span}\{
K_0,\ldots,K_{10},J_\sigma,J_1,J_2,J_3\}.
\tag{10}
$$
它在 universal $A_u=0,\ p\ne0$ 的自由 jets 上给十五个独立 current 方向。
证明可以直接使用 R435 的完整生成式，而不逐项展开高阶列。

令 $w=1-zx$、$A_z=w^2r+2zwp+2z^2u$。原根值为
$$
\sum_{n=0}^{10}\frac{z^n}{n!}\mathcal F_x(K_n)
=\frac{A_z^3}{15}
\left(4A_z^2-10z^2uA_z-\frac{20}{3}w^4r^2\right).
\tag{11}
$$
其纯 $r^5$ 部分准确是
$$
-\frac8{45}(1-zx)^{10}r^5 .
$$
所以第 n 列具有非零的 $x^nr^5$ 系数，而其它 K 列不含同一纯 monomial；(9)的四列没有任何 $r^5$ 项。若十五列有 universal 关系，逐个比较这些系数先使全部十一条 K 系数为零。
余四列再按 $x^2pr^4,xpr^4,pr^4,p^2r^3$ 比较，全部为零。

这里的多项式比较有真实有限 jet 见证：在任意内部点给定 $p\ne0,u,r$，取
$t=r^2/(3p)$，再选择四阶 jet 使 $A_u'$ 非零；有限紧 profile 可实现这些 jets。
因此不在一个不可能的实际 $p=0,r\ne0$ 点作取值。上述纯 monomial 比较只是在已成立于 $p\ne0$ 开集的多项式恒等中比较系数。

于是
$$
\boxed{\dim\mathscr M=15,\quad
\mathscr M\subset\mathcal R\cap\ker E\cap\ker J^+,\quad
C(\mathscr M)=0.}
\tag{12}
$$
这是原成本列的线性独立及 universal current 身份。
它没有宣称某个固定有限根配置的矩阵必有秩15。

若需要真仿射闭包，取
$\mathscr K+\mathcal B_PZ_{c0}$，另含 J0 的盲列。
R432 的
$$
N\sigma=N\tau_0=0,\quad N\tau_1=\tau_0,\quad
N\tau_2=2\tau_1,\quad N\tau_3=3\tau_2+8\sigma
$$
及 $NP=0$ 给其平移闭合；正伸缩按原真权作用。
不要求该空间对 $\delta$ 闭合，也不把原型安置当作任意点上列值不变。

## 3. 同一个实际镜点对及真实宽度

使用 R431 最后母库中一个真实对应点类。将共同真实宽度收入参考 u，令其偶镜点为
$$
-b,\quad b,\qquad b>0,
$$
$$
u(-b)=u(b)=u_*,\quad
u'(-b)=p_*>0,\quad u'(b)=-p_*,
\quad u''(-b)=u''(b)=r_*>0 .
\tag{13}
$$
原 R340/R401 的 $(u'^{\,2/3})'$ 正最大点论证给这种镜对；
R431 保原 p 与 A 的简单性以及全部外区，故这两个点是最后实际根。
不是另换 R410 的单对模式，也不要求它们是仅有的根。

在已有完整副本中写
$$
f=\rho_j a\,u(x-\xi_j),\quad
g=\rho_j\epsilon_jb_0\,u(x-\xi_j),\quad
x_j^-=\xi_j-b,\quad x_j^+=\xi_j+b.
\tag{14}
$$
这里 $\rho_j\ne0,\epsilon_j=\pm1,\ a\ne0,\ R=a^2-b_0^2\ne0$；
$\xi_j$ 是已存在的不同真实中心，不为增加 rank 自由移动。
参考包宽已经固定在 u 中，不能把不同实际宽度混入这组。

若原最细形式为 $U((x-\xi)/w_0)$，则
$p_*=U'(-b_{\rm ref})/w_0$、
$r_*=U''(-b_{\rm ref})/w_0^2$、
$b=w_0b_{\rm ref}$。
以下系数使用这些**物理 jets**，不是归一母值。
共同复制幅 $\rho_j$ 始终按第五次进入 partial。

记
$$
s_*=\frac{p_*}{r_*},\qquad h_*=\frac{u_*}{r_*},\qquad
\kappa_*=-\frac83p_*r_*^4\ne0 .
\tag{15}
$$
$r_*>0$ 足以使这些真实比值有定义。

## 4. 三条只作用右镜点的准确列

R435 生成式的前两阶给
$$
\mathcal F_x(K_0)=-\frac8{45}r_*^5,\quad
\mathcal F_x(K_1)=-10x\,\mathcal F_x(K_0),
$$
$$
\mathcal F_x(K_2)
=-16x^2r_*^5+\frac{32}{3}p_*^2r_*^3-\frac43u_*r_*^4
\tag{16}
$$
在两侧镜点都成立。特别其实际 x、常项、u 项均相同，不能只用最高平移项作下面消去。

定义原成本的准确实线性组合
$$
\boxed{
\begin{aligned}
L_0={}&J_1+\frac{15}{2}s_*K_0,\\
L_1={}&J_2-\frac32s_*K_1-15s_*^2K_0,\\
L_2={}&J_3+\frac14s_*K_2+\frac32s_*^2K_1
+\left(15s_*^3-\frac{15}{8}h_*s_*\right)K_0 .
\end{aligned}}
\tag{17}
$$
这些是同一个实际基点数据确定的有限成本，不是对每个查询点分别选系数。

由(9)、(16)直接消去整个左族，得到
$$
\boxed{
\mathcal F_{x_j^-}(L_0;u_j)
=\mathcal F_{x_j^-}(L_1;u_j)
=\mathcal F_{x_j^-}(L_2;u_j)=0
\quad\text{对全部已有对应副本}.}
\tag{18}
$$
在右镜点，p 变号，$u,r,p^2$ 不变，因此
$$
\boxed{
\bigl(\mathcal F_{x_j^+}(L_0),
\mathcal F_{x_j^+}(L_1),
\mathcal F_{x_j^+}(L_2)\bigr)
=\kappa_*\bigl(1,\,2x_j^+,\,3(x_j^+)^2\bigr).
}
\tag{19}
$$
未把 $\xi_j$ 与 $x_j^\pm$ 混同。式(18)—(19)是完整 self partial，不删原常项或真实左锚。

由(7)、(12)，三列仍满足
$$
J^+(L_j)=0,\qquad C(L_j)=0
$$
在整个原圆所有包、所有根上成立。

## 5. 真实十四行矩阵

在已有十二个完整 cell 的同一首包或末包对应点中，选十一个不同左点；
在其中三个不同副本中，再选其右镜点。
更一般，只需原库中确有(14)的这些对应副本和三个不同 $x_j^+$。
不能将八个孤立同轴包误称为含完整 R/T 编码的 cell。

按十一左行在前、三右行在后排列，取十四列
$$
K_0,\ldots,K_{10},L_0,L_1,L_2 .
$$
原 raw 平台规范取 R435(16)，对这些列平台第二导数准确零。
矩阵为
$$
\boxed{
\begin{pmatrix}
M_-&0\\
*&M_+
\end{pmatrix}.}
\tag{20}
$$
$M_-$ 是 R435 已付的同基点、同宽、实际第五幅矩阵，可逆；
这里不重做该旧对应点 rank。
若三右行的真实幅系数为
$$
d_j=\rho_j^5a^3R\ne0,
$$
则
$$
M_+=\operatorname{diag}(d_j)\,
\kappa_*
\begin{pmatrix}
1&2x_1^+&3(x_1^+)^2\\
1&2x_2^+&3(x_2^+)^2\\
1&2x_3^+&3(x_3^+)^2
\end{pmatrix},
$$
$$
\boxed{
\det M_+
=6\kappa_*^3(d_1d_2d_3)
\prod_{i<j}(x_j^+-x_i^+)\ne0 .}
\tag{21}
$$
星号是原 K 列的全部右镜点值，保留在同一个矩阵中。

所以同一个真实圆的十四条 H 观察在 $\mathscr M$ 上满射。
这些列全部保持原 $J^+$ 和整个 C 向量，不是只保持一小部分已选 C。

### 5.1 第十五点的准确条件

另定义
$$
L_*:=J_\sigma+\frac{15}{4}s_*^2K_0.
\tag{22}
$$
它在上述**全部左、右镜点对应族**上均为零。
在另一个真实 $A_u=0$ 点的物理 jets $(p_\dagger,r_\dagger)$ 上，
$$
\boxed{
\mathcal F_{x_\dagger}(L_*)
=\frac23r_\dagger^3
\{p_\dagger^2-s_*^2r_\dagger^2\}.}
\tag{23}
$$
若该点的真实 $a_\dagger R_\dagger\ne0$，且
$$
r_\dagger\ne0,\qquad
\left|\frac{p_\dagger}{r_\dagger}\right|\ne s_*,
\tag{24}
$$
则(23)非零，追加 L* 给一个真正十五行块三角矩阵。

(24)是实假设，不从 R431 的简单性自动推出。
比如另一个相同 cap 点若物理宽度不同，必须按实际宽度检查这个比值；
本文既不假定这样的副本已经存在，也不为满足它重新改变最后母库。
若(24)未证，结论止于(20)的十四行。

## 6. 同一个实际截面，而非十四次独立路径

由(8)、(12)、(20)，令 $\mathbf H_{14}$ 为这十四条完整 raw/平台规范读出，有
$$
(J^+,\mathbf H_{14})(U)=J^+(U)\times\mathbb R^{14},
$$
$$
(J^+,\mathbf H_{14})(\mathcal R)
=J^+(\mathcal R)\times\mathbb R^{14}.
\tag{25}
$$
若(24)成立，相应将14换15。
这是同一固定 profile 库的联合像。

R435 第5节的真实有限构造现在直接适用：原 J⁺ 响应基与(20)的十四列形成一个固定可逆块三角基。所有新列均由原有限 $E_8,Z$ 与 $K$ 原型给出，从起点连同保护芽、桥、共享真倒行、右锚及目标紧盒放入同一合法窗口。

原型成本的完整 J⁺ 商基准先支付；第二次真实商修正的全部 H 代价也保留。
最后剩同一个方程
$$
n(a+Mt)+F(t,y)=y_{\rm resp},
$$
所有内部整数先固定，最后选一次有限 n 作统一 $C^1$ 收缩。
Klein 的完整 $V_{\rm base}+4V_B$ 仍先减基准再除4。
因此有同一个固定有限真实词的紧目标 $C^1$ 截面
$$
\boxed{J^+=y,\qquad \mathbf H_{14}=h.}
\tag{26}
$$
不将十四条分别存在的实际几何拼成一条，也不在旧冻结几何上免费叠加 signed 响应。

若同一库的 C 已通过完整实际联合截面支付，或者已证明 R435§5.1 的精确共同等像入口，(7)使整个补偿仍保持 C，全部 prototype 的 C 基准照样入账。
没有此前提时，(26)只授显示的联合目标。

在 R397/R435 已核的完整 cell 首、末包上，消-self 行本来经 E 因子化。每个完整编码在八包装**以前**已有
$\sum R_i\mu_i=\sum T_i\mu_i=0$；
$\alpha^2$ 只乘已零三向量，$\alpha^3$ 差分另负责第三条件。
所以在这类实际对应组中，取 $J^+=0,\mathbf H_{14}=0$ 就使选中的十四个点上**两条** period 内部通量都零。
其余根、平台仿射连接及同相位十三行不由此支付。

## 7. λ⁺ 仍不能由这一组 self 门读出

原 $H_*$ 满足 $J^+(H_*)=0,\lambda_+(H_*)=1$。
用(20)的完整原矩阵，减去唯一的十四列线性组合，使
$\mathbf H_{14}$ 也为零。所有列在原响应空间，故 $\lambda_+$ 不变。
于是有明确 signed 见证
$$
\boxed{
J^+(\widetilde H_*)=0,\quad
\mathbf H_{14}(\widetilde H_*)=0,\quad
\lambda_+(\widetilde H_*)=1.}
\tag{27}
$$
若(24)成立，同样给十五行版本。
这些修正使用 $H_*$ 的完整真实查询值，包括其原 self/history，而不把它们预设为零。

若另要求其它 C 零，须先如 R435 说明用一个原 whole-E 响应清 $C(H_*)$，再施本稿修正；本稿全部列都不改变 C。
因此(27)不跨越尚未证明的 ordered 响应像。

(27)是排除这一组新 λ 障碍的线性见证；实际存在来自(26)，两种论证不混淆。

## 8. 更大镜对库上的本模块完整像

本稿还可准确描述本已知模块对一个固定镜点对的全部对应副本，避免把十四行外误作自由。

记 K 列在左、右的 normalized 原多项式为 $p_n^-(\xi),p_n^+(\xi)$。
每个都直接由(11)在真实 $x=\xi\mp b$ 上评价，保全部 $u_*,p_*,r_*$。
左侧 $p_0^-,\ldots,p_{10}^-$ 是次数至多10的基，故唯一地定义一个真实线性输运
$$
\mathsf T:\operatorname{Pol}_{\le10}\longrightarrow
\operatorname{Pol}_{\le10},
\qquad \mathsf T(p_n^-)=p_n^+ .
$$
$\mathsf T$ 是固定 cap 数据确定的多项式基变换，不是假设两侧 current 相同。

由(18)—(19)、(22)，整个十五维 $\mathscr M$ 在这类全部副本上的 normalized 像准确为
$$
\boxed{
h^-(\xi)=P(\xi),\qquad
h^+(\xi)=\mathsf TP(\xi)+Q(\xi+b),
\quad
\deg P\le10,\quad\deg Q\le2 .
}
\tag{28}
$$
实际原值再乘各自 $\rho_j^5a^3R$。
L* 对这一整镜对族准确盲，故一旦已有(20)的点，本模块在该族上的 rank 恰14，不是15。

对有限更大库，(28)的精确检验是：左目标来自同一个十次以下 P；扣去其真实右值 $\mathsf TP$ 后，全部右目标来自同一个二次以下 Q。
这只是当前明确模块的限制，不能据此排除其它 $\mathcal R\cap\ker E$ 响应或整个实际成本锥。

新内容是四条 P 支路 self、十五个原形式方向、同一最终圆的十四行准确实际支付及有条件十五行。全部不同根的 self/ordered 联合像、完整 period 与十三行同规范，仍须沿同一个真实对象继续。
