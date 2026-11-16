# R859 — 原最高 CM 分量的惯性约化 shadow 与整 Abel–Jacobi 检测

日期：2026-11-16。**状态：下述真实 Frobenius 除子、最高块的整收缩同构、原系数与角色保留的点公式、全局 torsion-free 判据已证明。尚未计算出原点公式的非零值；不据此宣布原端点、原同步迹或指定普通局部化非零。**

本篇直接处理 R831 修复后的同一个端点类，经 R832、R839 的实际
Chow 对应写入 $E_0^3$。检测的是该原类；R817 的7993证书仍只属于
R814/R854 的 canonical 来源，不用于本篇。

有限约化素数记为 $r$，系数素数记为 $\ell$。二者均不与主问题
沿原 ordinary ray 变化的 $p$ 混用。本文没有运行素数扫描，也未用
只有名字而没有实际输入的 producer。

## 1. 同一个固定源、系数及 Artin 域

沿 R832、R858 置
$$
K=\mathbf Q(\omega),\qquad
E_0:\ y^2=x^3+1,\qquad A=E_0^3,\qquad H=H_{34}.
\tag{1}
$$
$H/K$ 是原三个十八阶角色 $\eta_j$ 的共同核域；
系数域 $\mathbb E$ 含 $K,\zeta_{18}$ 及原 Hecke 提取系数。
几何基域与系数域分别保留：$\mathbb E$ 中的系数不受 point-factor
Galois 投影作用。

令 $\pi_1$ 为以 $O$ 为基点的椭圆 $h^1$ Chow 幂等元。
写
$$
R=([\omega],[\omega],[\omega]),\qquad
\boxed{\Pi=\pi_1^{\otimes3}\frac{1+R_*+R_*^2}{3}.}
\tag{2}
$$
原 CM 分解给
$$
\operatorname{im}\Pi=M_+\oplus M_-,
\qquad M_\pm=H_\pm^{\otimes3}.
\tag{3}
$$
式(2)是实际 Chow 投影：在 $\pi_1^{\otimes3}$ 内，
两个全同号特征为1，其余六条特征为 $\omega,\omega^2$。
因此它与 R839/R852 的原最高投影相同，不另引入一个只在实现上
定义的投影。它在所有 $\ell>3$ 上为整投影。

对原一个固定有序对，R832、R839 的真正 $h^1$ 同构给
$$
\boxed{
\mathcal Z_{\rm orig}
 =\sum_{\rho}c_\rho\,
    \Pi\,(\Phi_\rho)_*[X],\qquad
\Phi_\rho=(F_\rho,G_\rho,H_\rho):X\longrightarrow E_0^3,
\quad X=X_0(10404).
}
\tag{4}
$$
这里
$$
G_\rho=a_\rho\circ q_0,\qquad
H_\rho=b_\rho\circ q_2
$$
保持原 $q_0(z)=z,\ q_2(z)=4z$，第一份 $F_\rho$ 经原 $f$ 因子。
有限 $h^1$ 表达中的有理倍 Hom 可先清分母成为实际同态，所需
逆倍数保入 $c_\rho$，从而(4)中的各 $\Phi_\rho$ 都是实际态射。

所有这些映射可取在 $H$ 上：R832 的 Artin 因子在 $H$ 上平凡，
其 $h^1$ 同构由该域上的实际 Hom 给出。扩张 $\mathbb E$ 只改变
线性提取系数，不要求把几何 Hom 的域免费扩大。
原 $X_1/X_0$、old pullback、source3 等尺度均在同一个
$c_\rho$ 中保留；本文不把它们重新归一为1。

若处理有限 point-factor $\chi=\eta_j^{\pm1}$，则按 R858
附录B与实际 CM 符号一起投影：
$$
e_\chi=\frac1{18}\sum_{\sigma\in\operatorname{Gal}(H/K)}
                 \chi(\sigma)^{-1}\sigma.
\tag{5}
$$
可把(5)展开为(4)的一个更长的有限和。原 all-plus 使用
$\chi=\eta_j$，all-minus 使用 $\chi=\eta_j^{-1}$；
不得在不选 CM 符号时把满 $\Pi e_\chi$ 全称作单条 $\lambda_j$。

固定整数 $D>0$，使(4)及已采用的(5)中除2、3外的所有系数分母
均由 $D$ 清除。对每个 $\mathfrak l\mid\ell>3$，令
$\mathcal O=\mathcal O_{\mathbb E,\mathfrak l}$，
可把 $D\mathcal Z_{\rm orig}$ 视作
$$
\widetilde{\mathcal Z}\in
\Pi\,CH^2(A_H)_{\rm hom}\otimes\mathcal O.
\tag{6}
$$
即使 $\ell\mid D$，后面的非零检测仍有效；只是该整倍数可能使
某一次有限检测变为零，不能据零检测反推原类为零。

## 2. 惯性素数的实际剩余域与 Frobenius

取
$$
r>3,\qquad r\ne17,\qquad r\equiv2\bmod3.
\tag{7}
$$
$r$ 在 $K$ 惯性。其 $K$ 上素理想是主理想 $(r)$，
生成元 $r$ 属于原 order $\mathcal O_{34}$，且素于其 conductor。
环类 reciprocity 因而给 $(r)$ 在 $H_{34}/K$ 完全分裂。
对任何 $\mathfrak r\mid r$，准确有
$$
k_{\mathfrak r}=\mathbf F_{r^2}.
\tag{8}
$$
这不是把整个 $\operatorname{Gal}(H/K)$ 当成剩余域的 Galois 群。

$E_0/\mathbf F_r$ 的 $r$-次 Frobenius 态射记为 $\varphi_r$。
因为 $r\equiv2\bmod3$，$x\mapsto x^3$ 在 $\mathbf F_r$ 上双射，
故 $\#E_0(\mathbf F_r)=r+1$，迹为0。
于是实际椭圆同态满足
$$
\boxed{
\varphi_r^2=[-r],\qquad
\varphi_r[\omega]=[\omega^2]\varphi_r.
}
\tag{9}
$$
第二式也可直接在坐标
$[\omega](x,y)=(\omega x,y)$ 上核对。
特别
$$
E_0(\mathbf F_{r^2})=E_0[r+1],\qquad
E_0(\mathbf F_{r^2})\simeq
(\mathbf Z/(r+1)\mathbf Z)^2.
\tag{10}
$$
所有原 Jacobian Hom 在好约化处延拓，故(4)可在所选
$\mathfrak r$ 上逐项约化；原 $q_0,q_2$ 也保持。

## 3. 真实 cross divisor 与轴的准确次序

在 $E_0^2/\mathbf F_{r^2}$ 上定义
$$
\boxed{
D_r=\Gamma_{\varphi_r}
      -(E_0\times\{O\})
      -r(\{O\}\times E_0),
\qquad
\Gamma_{\varphi_r}=\{(P,\varphi_rP)\}.
}
\tag{11}
$$
系数 $r$ 必须在第二条轴上。
确实图形投向第一因子次数1，投向第二因子次数 $r$；
(11)的两次推出均为零。

更精确地，(11)的线丛限制到两条轴均平凡：
在 $\{O\}\times E_0$ 上图形给 $[O]$；
在 $E_0\times\{O\}$ 上给
$\ker\varphi_r=r[O]$，这里是实际非分离核的 scheme 长度。
因此(11)是以两条轴刚化的 cross 线丛，其真正 Chow 分量位于
$h^1(E_0)\otimes h^1(E_0)$。
这说明对 $\pi_1^{\otimes3}$ 的使用不会在下述点公式中遗漏
Picard 或轴项。

对 $\widetilde{\mathcal Z}_{\mathfrak r}$ 定义原 shadow
$$
\boxed{
\mathscr S_{\mathfrak r}(\widetilde{\mathcal Z})
=(\operatorname{pr}_3)_*
 \left(
 \widetilde{\mathcal Z}_{\mathfrak r}
 \cdot\operatorname{pr}_{12}^*D_r
 \right)
\in E_0(\mathbf F_{r^2})\otimes\mathcal O.
}
\tag{12}
$$
右侧用 $O$ 把 degree0 零维循环认作椭圆点。
原类同调平凡，故交积推出确有 degree0。
若某几何代表与图形相交不适当，(12)仍取线丛第一 Chern 类的
交积；下一节给相容的可执行 divisor 读法。

这里的有限点并不是有理系数的有限域 Chow 群值。
后者张量 $\mathbf Q$ 后会消失。检测必须先保(6)的整代表，
再在(12)的 $\ell$-primary 模中读取。

## 4. 最高两条 CM 线的整收缩同构

固定 $\ell>3,\ell\ne r$。令
$$
V=H^1_{\rm et}(E_{0,\overline{\mathbf F}_r},\mathcal O).
$$
$\omega-\omega^2$ 在 $\mathcal O$ 中为单位，所以
$$
V=V_+\oplus V_-
$$
是两条整直和线。主极化的 cup pairing 在 $V_+\times V_-$ 上
完美。选择基 $e_\pm$ 并固定 Tate 基，使
$\langle e_+,e_-\rangle=1$。

由(9)，存在 $a,b\in\mathcal O^\times$ 使
$$
\varphi_r^*e_+=a e_-,
\qquad \varphi_r^*e_-=b e_+,
\qquad ab=-r.
\tag{13}
$$
最后一式同时证明两系数为单位，未把复 period 或有限 Gauss
系数当成额外单位输入。

与(11)交积的 cohomological contraction 是
$$
c_r(x\otimes y\otimes z)
=\langle x,\varphi_r^*y\rangle z.
\tag{14}
$$
轴项在这个 $h^1\otimes h^1$ 分量上为零。
由图形的第一、第二坐标约定，(14)的顺序就是所显示的顺序。

在最高块
$$
T_{\rm top}=(V_+^{\otimes3}\oplus V_-^{\otimes3})(2)
$$
上，(14)准确成为
$$
e_+^{\otimes3}\longmapsto a e_+,\qquad
e_-^{\otimes3}\longmapsto -b e_-.
\tag{15}
$$
目标是 $V(1)$；两个输入 cup 因子提供所需 Tate 移位。
因此
$$
\boxed{
c_r:T_{\rm top}\xrightarrow{\;\sim\;}V(1)
\quad\text{为 }\mathcal O\text{-整的 }G_{\mathbf F_{r^2}}\text{ 同构},
\qquad \det(c_r)=r.
}
\tag{16}
$$
这里用的是(13)的真实反交换，不是只比较两边的维数或 Frobenius
特征多项式。对 ordinary split 约化，Frobenius 保持两个 CM
符号，(14)反而杀最高两条线；所以(7)是此检测的实质条件。

几何 Frobenius $\operatorname{Frob}_{r^2}$ 在
$T_{\rm top}$ 和 $V(1)$ 上均为标量 $-1/r$。
这与(16)相容，但不是(16)的替代证明。

## 5. 同一源 specialization 与有限域 AJ 的完整读取

令
$$
T_A=H^3_{\rm et}(A_{\overline H},\mathcal O)(2),
\qquad T=\Pi T_A.
$$
采用几何 Frobenius 规范，$\mathcal O(1)$ 在剩余域
$\mathbf F_q$ 上的 Frobenius 值为 $q^{-1}$。
Bloch 的整 étale AJ 给
$$
AJ_\ell(\widetilde{\mathcal Z})\in H^1(H,T).
$$
好约化 specialization、代数对应与 cup/Gysin 的相容性给交换图：
$$
\begin{array}{ccc}
AJ_\ell(\widetilde{\mathcal Z})
 &\longmapsto&
AJ_\ell(\widetilde{\mathcal Z}_{\mathfrak r})
 \in H^1(\mathbf F_{r^2},T_{\rm top})\\
&&\downarrow\,H^1(c_r)\\
&&\kappa_\ell\bigl(
 \mathscr S_{\mathfrak r}(\widetilde{\mathcal Z})\bigr)
 \in H^1(\mathbf F_{r^2},V(1)).
\end{array}
\tag{17}
$$
上行是同一个原全局类的局部 restriction 与 unramified
specialization，未换成另一个 CM cycle。

椭圆主极化识别 $V(1)$ 与 Tate module。
有限域 Kummer 映射准确给
$$
E_0(\mathbf F_{r^2})\otimes\mathcal O
 \xrightarrow{\;\sim\;}
H^1(\mathbf F_{r^2},V(1)).
\tag{18}
$$
例如两边均是相应整格模
$\operatorname{Frob}_{r^2}-1$；因 $r$ 在 $\mathcal O$ 中为单位，
它也就是模 $r+1$ 的两维整格。

由(16)–(18)，不是只有一个单向蕴含，而有
$$
\boxed{
AJ_\ell(\widetilde{\mathcal Z}_{\mathfrak r})=0
\ \Longleftrightarrow\
\mathscr S_{\mathfrak r}(\widetilde{\mathcal Z})=0.
}
\tag{19}
$$
(19)准确读取此 prime 上的原最高块有限域 AJ；
它不反推全局类在所有地方为零。

可直接用的 primary 依据是 Ellenberg–Logan–Srinivasan,
*Certifying nontriviality of Ceresa classes of curves*，
Propositions2.10、2.11：它们把实际交积 shadow、Kummer 和好约化
specialization 放入同一个交换图，引用的是
Buhler–Schoen–Top 的一般光滑射影 cycle-class 相容性。
本篇额外支付了其一般算法所没有的指定最高块整同构(16)。

## 6. 原 Artin 域上全局 H1 的无挠性

**引理。** 对任意 $\ell>3$ 及上述 $\mathcal O$，
$$
\boxed{H^1(H,T_A)\text{ 没有非零 }\mathcal O\text{-torsion}.}
\tag{20}
$$
同一结论适用于直和因子 $T$。

证明。5、11均在 $K$ 惯性，素于34。
与(8)相同的 principal ideal 论证给 $H$ 上剩余域
$\mathbf F_{25}$、$\mathbf F_{121}$。
在 $E_0$ 的 $H^1$ 上，它们的几何 Frobenius 分别为
$-5,-11$。所以在**整个** $T_A$ 上分别是
$$
\boxed{
\operatorname{Frob}_{25}=-1/5,\qquad
\operatorname{Frob}_{121}=-1/11.
}
\tag{21}
$$
这里 $H^3(A)$ 由三份 $H^1(A)$ 的外幂给出；
Tate twist2分别除以 $25^2,121^2$。
也可以逐个原 product Künneth 分量得到同一标量。

置 $V_A=T_A\otimes_{\mathcal O}\operatorname{Frac}\mathcal O$。
由(21)，$H^0(H,V_A)=0$。
短正合列
$$
0\longrightarrow T_A\longrightarrow V_A
 \longrightarrow V_A/T_A\longrightarrow0
$$
把 $H^1(H,T_A)$ 的 torsion 部分识别为
$H^0(H,V_A/T_A)$。
当 $\ell>3,\ell\ne5$ 时，
$$
\operatorname{Frob}_{25}-1=-6/5
$$
为 $\mathcal O$ 单位，故该不变量为0。
$\ell=5$ 时改用
$$
\operatorname{Frob}_{121}-1=-12/11,
$$
仍为单位。证毕。

这个证明不假设原全局 AJ 非零，也不使用一般 Selmer rank-one
的局部注入猜想。它只排除一个全局整 AJ 类可能是非零 torsion。
原有限 $\eta_j$ 的实现也相容：在上述惯性主理想上
$\eta_j((5))=\eta_j((11))=1$。
但证明本身已经对平凡化域上整个 $H^3(E_0^3)(2)$ 成立。

由(17)、(20)立即得到实际检测定理：

**定理。** 若某个满足(7)的 $r$、某个 $\mathfrak r\mid r$、
某个 $\ell>3,\ell\ne r$ 使
$$
\boxed{\mathscr S_{\mathfrak r}(\widetilde{\mathcal Z})\ne0}
\tag{22}
$$
在 $E_0(\mathbf F_{r^2})\otimes\mathcal O$ 中成立，则
$$
AJ_\ell(\mathcal Z_{\rm orig})\ne0
\quad\text{于有理 }\ell\text{-adic cohomology},
\qquad
\mathcal Z_{\rm orig}\ne0
\quad\text{于原 }\mathbb E\text{-系数 Chow 群}.
\tag{23}
$$
事实上有限域 AJ 非零迫整全局 AJ 非零，(20)再使其有理化仍非零。
若原有理 Chow 类为零，任一整代表的 AJ 必为 torsion，和(20)
矛盾。清分母整数 $D$ 不影响这个蕴含。

对原 $\chi$ 部分，R858 的真实 restriction 单射还给
$$
(22)\ \Longrightarrow\ \mathfrak T_{\tau,\chi}\ne0
\tag{24}
$$
的同一个同步 generic trace 结论。
此处没有使用 canonical7993来满足(22)。

## 7. 从原 Φ 写出的完整有限点公式

以下公式不要求曲线源 genus3，不要求源的 Jacobian 全为
$E_0$ 幂，也不要求任一映射是 degree2。

先取(4)的一项，记其约化为
$$
\Phi=(F,G,H_0):X_{k_{\mathfrak r}}\longrightarrow E_0^3.
$$
为避免与基域 $H$ 混淆，本节第三映射写为 $H_0$。
对 $k=0,1,2$ 定义实际差映射
$$
d_k=G-[\omega^k]\varphi_r F,
\qquad
\mathfrak d_k=d_k^*(O)\in\operatorname{Pic}(X_{k_{\mathfrak r}}).
\tag{25}
$$
若 $d_k$ 非常数，$\mathfrak d_k$ 由其真实零纤维表示，所有
inseparable multiplicity 均保留。
若 $d_k$ 为常数，其 pullback 线丛平凡，应取
$\mathfrak d_k=0$ 的 divisor class；尤其不能把恒为 $O$ 的差映射
误当作一个可数的有限零集。

设 $\mathfrak d_k=\sum_x m_{k,x}[x]$ 为任一代表，定义
$$
B_k(\Phi)
 =\sum_xm_{k,x}
      \operatorname{Tr}_{k(x)/k_{\mathfrak r}} H_0(x)
 \in E_0(k_{\mathfrak r}).
\tag{26}
$$
这是把推出 divisor 的 degree0 部分用 $O$ 取 Albanese。
更换 divisor 代表不改变这个点。
所有闭点和其剩余域的 trace 必须保留，不能只求
$X(\mathbf F_{r^2})$ 中的解。

**准确点公式是**
$$
\boxed{
3\,\mathscr S_{\mathfrak r}
       \bigl(\Pi\Phi_*[X]\bigr)
   =\sum_{k=0}^2[\omega^k]\,B_k(\Phi).
}
\tag{27}
$$

证明。由(9)，$R_*^k\Phi$ 的两前坐标落在 $\Gamma_{\varphi_r}$
上的条件是
$$
[\omega^k]G
 =\varphi_r[\omega^k]F
 =[\omega^{-k}]\varphi_r F,
$$
等价于 $G=[\omega^k]\varphi_r F$，正是(25)。
其第三坐标为 $[\omega^k]H_0$。
由(11)，对应 pullback divisor class 为
$$
\mathfrak d_k-G^*(O)-rF^*(O).
\tag{28}
$$
两个轴项与 $k$ 无关，推第三因子后乘 $[\omega^k]$。
它们在完整三项求和中由
$$
[1]+[\omega]+[\omega^2]=0
\quad\text{于 }\operatorname{End}(E_0)
$$
准确消去。
$D_r$ 的真实 cross 性使前两个 $\pi_1$ 不添项；
第三个 $\pi_1$ 正是取 degree0/Albanese 的规范。
代入(2)即得(27)。证毕。

因此对(6)的完整原来源，
$$
\boxed{
3\,\mathscr S_{\mathfrak r}(\widetilde{\mathcal Z})
 =D\sum_\rho c_\rho
       \sum_{k=0}^2[\omega^k] B_k(\Phi_\rho).
}
\tag{29}
$$
若尚未把(5)并入 $\rho$，则右侧还必须显示
$$
\frac1{18}\sum_{\sigma\in\operatorname{Gal}(H/K)}
       \chi(\sigma)^{-1}
       \sum_\rho c_\rho\sum_{k=0}^2
           [\omega^k]B_k(\Phi_\rho^\sigma).
\tag{30}
$$
所有 $\Phi_\rho^\sigma$ 都在同一个所选 $\mathfrak r$ 上约化。
因为 $r$ 在 $H/K$ 完全分裂，$\sigma$ 通常移动该素理想；
不能把(30)替换成对 $\mathbf F_{r^2}$ 的一个域自同构平均。
这是本篇完整角色与实际有限点计算的必要区别。

在 affine 非无穷输入上，(25)可用精确方程
$$
x_G=\omega^k x_F^{\,r},\qquad y_G=y_F^{\,r}
\tag{31}
$$
计算；原点、极点、scheme multiplicity 和闭点 trace 仍按(25)处理。
(31)只是实际态射方程的一个坐标区，不替代全 divisor 公式。

## 8. 可执行输入与目前未完成的计算

(25)–(30)把一次真正的非零检测化为有限数据：

1. R839 同一有限展开中实际 $F_\rho,a_\rho,b_\rho$ 的函数域表达，
   原 $q_0,q_2$ 和全部 $c_\rho$；
2. 原 $H_{34}$ 的所选素理想 $\mathfrak r$ 及全部 $\sigma$ 对该展开的作用；
3. $d_k^*(O)$ 的完整 divisor、推出点及有限域 trace；
4. 目标 $\ell$-primary 点模中的(29)或(30)。

这些输入一旦明确，(29)是精确代数算法，不需近似积分或猜
$p$-adic period。完整计算输出应含原展开/模型哈希、$r,\mathfrak r,\ell$、
清分母整数、每份 divisor 的 degree 与实际 trace、角色加权点及其
$\ell$-primary 阶。

现有 R839 给出实际 Hom 的有限存在与规范，但未列出这些
Jacobian 映射的函数域坐标；本篇没有把存在性伪装成一份已经能运行的
producer。也没有因为 $r+1$ 含某个 $\ell>3$ 就预认(29)非零。
这里不新增无来源的素数扫描。

即便以后(22)成立，结论是同一原端点的非零及某一整 étale AJ
的非零。它不自动给原普通 $p$ 处的指定 localization 非零，
不把它等同 R814 canonical 类，也不完成无穷 $p$ 的
$\Sha[p^\infty]$ 主目标。

## 9. 引用与证据

- [R831](R831-original-dyadic-old-space-and-unique-endpoint-class.md)：
  唯一真实端点、$q_0/q_2$、原所有 old/X0/X1 次数。
- [R832](R832-original-triple-chow-purity-and-rank-zero-contractions.md)、
  [R839](R839-top-cm-translation-invariance-and-original-ceresa-expression.md)：
  真正 $h^1$ Artin–CM 对应及(4)的同源有限态射表达。
- [R852](R852-original-schoen-correspondence-and-exact-chow-inverse.md)：
  两条 CM Chow 线和原最高投影的实际分解。
- [R858](R858-original-artin-cm-vertical-vanishing-and-generic-injectivity.md)：
  $H_{34}$、原 $\chi$ 与 CM 符号、同一同步 trace 和 restriction 单射；
  本篇(24)只沿它已经证明的真实对象使用。
- J. Ellenberg, A. Logan, P. Srinivasan,
  *Certifying nontriviality of Ceresa classes of curves*，
  [作者全文](https://padmask.github.io/CertifyingCeresa.pdf)，
  [arXiv:2412.02015](https://arxiv.org/abs/2412.02015)：
  Definition2.2、Propositions2.10、2.11、3.1、3.4及§4.5–4.6。
  本篇使用实际交积/Kummer/specialization 的原定理，
  不套其 full-GSp 的算法终止假设，也不套只陈述 semidiagonal
  genus3 的特殊点公式；(27)另由本篇对原 $\Phi$ 完整推导。
- J. Buhler, C. Schoen, J. Top,
  *Cycles, L-functions and triple products of elliptic curves*，
  J. reine angew. Math. **492** (1997), 93–133，
  Proposition1.9(5)–(6)。
  此处相容性通过前一作者全文中 Proposition2.10–2.11 的明确转述使用；
  本篇没有声称已经亲读不可提取的原 PDF 全文。
- 原(20)的全局无挠性和(16)的最高块整同构均在本文自含证明，
  不以任何新数值或待证 regulator 假设为输入。


## 附录 A. 同一个 shadow 的实际有限域 Chow 逆

本附录加强§4的整实现同构。仍取同一个惯性素数
$r>3$、$k=\mathbf F_{r^2}$、$E=E_0/k$、$\varphi=\varphi_r$
和正文(2)的实际投影 $\Pi$。系数环置
$$
\mathscr R=\mathbf Z[1/(6r),\omega].
\tag{A1}
$$
以下等式在 Chow 对应中成立，因而也可用于正文原系数环的任一
$\ell>3,\ \ell\ne r$ 完备化。它们不只是在 étale 实现上成立。

记正文的交积对应为
$$
S_r(Z)=\operatorname{pr}_{3,*}
       \bigl(Z\cdot\operatorname{pr}_{12}^*D_r\bigr),
\qquad
D_r=\Gamma_\varphi-E\times O-r\,O\times E.
$$
反向对应定义为
$$
\boxed{
I_r(P)=\Pi\bigl(D_r\times([P]-[O])\bigr).
}
\tag{A2}
$$
这里 $P$ 可先是一个点，再线性延拓为 $\operatorname{Pic}^0(E)$
中的类。作为动机对应，$I_r$ 的来源是
$\mathbb L\otimes h^1(E)$；不是在特征零中另选一个 Frobenius lift。

### A.1 两个复合的实际系数

对任意椭圆自同态 $\alpha$ 置
$$
D_\alpha=\Gamma_\alpha-E\times O-(\deg\alpha)\,O\times E.
$$
图形和两条轴的直接交积给出
$$
D_\alpha D_\beta
 =\deg(\alpha-\beta)-\deg\alpha-\deg\beta.
\tag{A3}
$$
$\alpha=\beta$ 时图形自交为0，因为其正规丛是椭圆曲线的
平凡切丛；$\alpha\ne\beta$ 时图形交集按
$\ker(\alpha-\beta)$ 的完整长度计算。因此(A3)保留不可分重数。

正文已付 $\varphi[\omega]=[\omega^2]\varphi$，所以
$$
D_k:=([\omega^k],[\omega^k])_*D_r
       =D_{[\omega^{2k}]\varphi},
\qquad k=0,1,2.
\tag{A4}
$$
$\deg(1-\omega)=\deg(1-\omega^2)=3$，从而
$$
(D_rD_0,D_rD_1,D_rD_2)=(-2r,r,r).
\tag{A5}
$$
各 $D_k$ 均已在 $h^1(E)\otimes h^1(E)$ 中，而
$[P]-[O]$ 已在第三个 $h^1$ 中。因此按 $\Pi$ 的实际三项平均，
$$
\begin{aligned}
S_rI_r(P)
 &=\frac13\bigl(-2r\,P+r[\omega]P+r[\omega^2]P\bigr)\\
 &=-r\,P.
\end{aligned}
\tag{A6}
$$
最后一步使用椭圆自同态环中的
$[1]+[\omega]+[\omega^2]=0$。同一交积计算给出
$\mathbb L\otimes h^1(E)$ 上的对应等式
$S_rI_r=-r\,\mathrm{id}$，而不只给出有理点上的等式。

为证明另一侧 $I_rS_r=-r\Pi$，还需证明 $S_r$ 在 Chow 动机上
确为同构。不能仅从正文的 étale 行列式为单位推出这一点。
下面给出所需的整数系数椭圆引理。

### A.2 椭圆 $h^1$ 的几何对称平方是实际 Tate 线

令 $E$ 为任意特征不为2的椭圆曲线，基点为 $O$，$H=h^1(E)$。
设 $\tau$ 为 $E^2$ 的几何交换。则在
$\mathbf Z[1/2]$ 系数的 Chow 动机中，
$$
\boxed{
\operatorname{im}\left(
   \frac{1+\tau_*}{2}\,\pi_1^{\otimes2}\right)
 \simeq\mathbb L.
}
\tag{A7}
$$
这里是几何交换的 $+1$ 块；在 cohomology 上包含两个奇次数
因子的 Koszul 符号，所以其实现为通常的
$\bigwedge^2 H^1$。以下证明直接在 Chow 对应上进行。

取有限平坦次数2的商
$$
q:E^2\longrightarrow Y=\operatorname{Sym}^2E.
$$
它满足实际对应式
$q^*q_*=\mathrm{id}+\tau_*$、$q_*q^*=2\,\mathrm{id}$。
加法给出
$$
a:Y\longrightarrow E,\qquad P+Q\longmapsto P+Q,
$$
这是一个 $\mathbf P^1$ 丛；截面为 $i(P)=O+P$。
截面除子在每条纤维上的次数为1，故 projective-bundle 公式
可用 $a^*$ 和 $i_*$ 给出 $h(Y)$ 的两份实际生成元。
其中一份为 $a^*h(E)$，另一份是 $i_*h(E)$ 的相应 Tate 移位。

将 $(1+\tau_*)\pi_1^{\otimes2}/2$ 通过 $q$ 搬到 $Y$，
记所得幂等元为 $p_Y$。
由于
$$
q^*i_*=j_{1,*}+j_{2,*},
\qquad
j_1(P)=(P,O),\quad j_2(P)=(O,P),
$$
$\pi_1^{\otimes2}$ 杀掉整个 $q^*i_*$；所以 $p_Y$ 杀掉第二份
生成元。对第一份有
$$
q^*a^*=m^*,
\qquad m:E^2\longrightarrow E,\quad m(P,Q)=P+Q.
$$

还要在 Chow 而非仅在实现上说明
$\pi_1^{\otimes2}m^*$ 杀 $h^0(E)$ 与 $h^1(E)$。
$h^0$ 的陈述直接成立。对 $h^1$，令
$\mathcal L=\mathcal O_E(O)$，
$\mathcal B=m^*\mathcal L\otimes
 \operatorname{pr}_1^*\mathcal L^{-1}\otimes
 \operatorname{pr}_2^*\mathcal L^{-1}$ 为规范 Poincaré 双扩张。
在 $E^3$ 上，$m$ 的图形是
$P+Q-R=O$ 这一个除子；双扩张的双线性给出
$$
\mathcal O(\Gamma_m)
 \simeq
 \mathcal L_1\otimes\mathcal L_2\otimes\mathcal L_3
 \otimes\mathcal B_{12}
 \otimes\mathcal B_{13}^{-1}
 \otimes\mathcal B_{23}^{-1}.
\tag{A8}
$$
各项只依赖至多两个坐标，故施加三份 $\pi_1$ 后全为0。
这正是 $\pi_1^{\otimes2}m^*\pi_1=0$ 的实际除子对应式；
没有使用一般 realization faithfulness。

剩下的 $h^2(E)=\mathbb L$ 生成元 $[O]$ 满足
$$
m^*[O]=[\Gamma_{[-1]}],
\qquad
\pi_1^{\otimes2}m^*[O]=-D_{\mathrm{id}},
$$
其中
$$
D_{\mathrm{id}}=\Delta_E-E\times O-O\times E.
\tag{A9}
$$
后一等式同样是规范双扩张的双线性：
$D_{[-1]}=-D_{\mathrm{id}}$。
于是 $p_Yh(Y)$ 整个通过由 $D_{\mathrm{id}}$ 生成的一份
$\mathbb L$ 因子化。另一方面
$$
\tau_*D_{\mathrm{id}}=D_{\mathrm{id}},
\qquad
\pi_1^{\otimes2}D_{\mathrm{id}}=D_{\mathrm{id}},
\qquad
D_{\mathrm{id}}^2=-2.
\tag{A10}
$$
$-D_{\mathrm{id}}^{\,t}/2$ 因而给该线的实际左逆。
由于整个像已经由这条线生成，它也是所需的右逆。
这证明(A7)，只需倒置2；没有把 Kimura 有限维性误用成
任意整数系数的 realization 忠实性。

回到 $E_0$ 并再倒置3。$[\omega]$ 的实际幂等元将
$$
H=C_+\oplus C_-
$$
分裂成两个 CM 因子。在(A7)的 Tate 线上
$[\omega]\otimes[\omega]$ 的作用为1；在
$\operatorname{Sym}^2C_+$、$\operatorname{Sym}^2C_-$ 上分别为
$\omega^2,\omega$。这些特征与1的差在 $\mathscr R$ 中为单位，
故两个同号几何对称平方为0，而异号的对称块给出
$$
\boxed{C_+\otimes C_-\simeq\mathbb L.}
\tag{A11}
$$
可把该同构选为限制后的 cup/polarization 对应；
(A9)–(A10)给其真实逆。因子2和
$\omega-\omega^2$ 均已在 $\mathscr R$ 中可逆。
因此(A11)是实际 Chow 线的可逆性，不是只从 Betti 维数1作判断。

### A.3 两侧互逆及全部有限域最高 Chow 群

正文的实际 Frobenius 关系给出
$$
\varphi^*:C_+\longleftrightarrow C_-,
\qquad
(\varphi^*)^2=-r\,\mathrm{id},
\qquad
(\varphi^*)^{-1}=-(1/r)\varphi^*.
\tag{A12}
$$
因此，在每一个最高块上，$S_r$ 都是下面两条实际同构的复合：
$$
C_\pm^{\otimes3}
 \xrightarrow{\ \mathrm{id}\otimes\varphi^*\otimes\mathrm{id}\ }
 C_\pm\otimes C_\mp\otimes C_\pm
 \xrightarrow{\ \mathrm{cup}\otimes\mathrm{id}\ }
 \mathbb L\otimes C_\pm.
\tag{A13}
$$
这就是正文(14)的收缩规范在 Chow 对应上的提升。
(A11)–(A12)证明 $S_r$ 为同构；将(A6)作为其另一侧逆，
得到完整等式
$$
\boxed{
S_rI_r=-r\,\mathrm{id},
\qquad
I_rS_r=-r\,\Pi.
}
\tag{A14}
$$

特别地，不仅是某一有限域 AJ 像，而是整个实际最高 Chow 群满足
$$
\boxed{
S_r:
 \Pi\operatorname{CH}^2(E_0^3/k)_{\mathscr R}
 \ \xrightarrow{\ \sim\ }\
 \operatorname{Pic}^0(E_0/k)\otimes\mathscr R
 =E_0(k)\otimes\mathscr R,
\qquad
S_r^{-1}=-(1/r)I_r.
}
\tag{A15}
$$
正文已付 $E_0(k)=E_0[r+1]$，故
$$
\boxed{
(r+1)\,\Pi\operatorname{CH}^2(E_0^3/\mathbf F_{r^2})_{\mathscr R}=0.
}
\tag{A16}
$$
对任意原系数素数 $\ell>3,\ \ell\ne r$ 完备化，
(A15)给同一 $\ell$-primary 最高 Chow 群和有限点群的真实同构。
因此正文(29)–(30)的原点读数若非零，检测到的也是同一原类
约化后的实际 Chow 类，而不只是一个可能丢失 torsion 的
有理 realization。

(A14)并未构造原类的非零约化。任意选择 $P$ 后的 $I_r(P)$
是在这一有限特征纤维中的类；反向对应使用反 CM 的
$\varphi_r$，不能把它提升成特征零中的一个自由可选原来源。
原 $\mathcal Z_{\rm orig}$ 的 shadow 仍必须使用正文(4)和
(29)–(30)中全部真实 Hom、原 $q_0/q_2$、系数与 point-factor
角色来计算。canonical7993 与原端点的区别、普通指定局部化
的缺口、主 $\Sha$ 目标的未闭状态均保持。


## 附录 B. 原九阶商上的完整 Frobenius 交积及 source 三次的消去

本附录仍在正文同一个好惯性素数 $r$、同一个选定
$\mathfrak r\mid r$ 上工作。置 $k=\mathbf F_{r^2}$，
$\mathscr R=\mathbf Z[1/(6r),\omega]$；亦可再张量原系数整环。
这里保留 $r+1$ 的所有素于 $6r$ 的 torsion，绝不先把
Chow 群张量 $\mathbf Q$。原固定分母 $D$ 与全部
$c_\rho,e_\chi$ 沿用正文。

### B.1. 同 R851 的真实商及准确坐标

令
$$
N=\{(\zeta_1,\zeta_2,\zeta_3)\in\mu_3^3:
             \zeta_1\zeta_2\zeta_3=1\},\qquad
q:A=E_0^3\longrightarrow B=A/N .
\tag{B1}
$$
$B$ 是完整射影有限商，未用一个仿射方程替代其无穷边界。
在原 $E_0:Y_i^2=X_i^3+1$ 的仿射区，严格采用 R851(15)：
$$
a_i=(Y_i+1)/2,\qquad b_i=a_i-1,\qquad
T=X_1X_2X_3/4,\qquad T^3=\prod_i a_i(a_i-1).
\tag{B2}
$$
这些是真正的 $N$-不变函数。特别 $T$ 含 $1/4$；
它不是未归一的 $X_1X_2X_3$。
R851 已给这个不变函数域到同一个 Schoen 模型的完整有理逆。
本附录先直接在有限商 $B$ 上作交积，不借有理解消对应
把 torsion 类变成只有有理系数才成立的等式。

取原实际 Frobenius 图面
$$
\mathcal D_r=\Gamma_{\varphi_r}\times E_0
 =\{(P,\varphi_rP,Q):P,Q\in E_0\}\subset A,
\qquad \overline{\mathcal D}_r=q(\mathcal D_r).
\tag{B3}
$$
因为 $\varphi_r[\zeta]=[\zeta^{-1}]\varphi_r$，其在 $N$ 中的
集合稳定子准确为
$$
N_r=\{(\zeta,\zeta^{-1},1):\zeta\in\mu_3\},\qquad |N_r|=3.
\tag{B4}
$$
这是泛型稳定子计算；没有把 $N$ 的全部九个元素认作同一图面
的稳定子。$N_r$ 在 $\mathcal D_r\simeq E_0\times E_0$ 上
只作用于第一份。因此
$$
\boxed{
\mathcal D_r/N_r\simeq\mathbf P^1_{a_1}\times E_0
 \xrightarrow{\;\nu_r\;}\overline{\mathcal D}_r
\text{ 是完整正规化。}}
\tag{B5}
$$
证明：$q|_{\mathcal D_r}$ 有限，其泛型纤维正是 $N_r$ 轨道；
由此得到的商到像有限双有理。源为正规射影曲面，故它就是
像的正规化。此论证包括 $a_1=0,1,\infty$，而不是仅在去掉
分歧点后给出一个双有理图。正规化上第二投影
$$
h_r:\mathbf P^1\times E_0\longrightarrow E_0
\tag{B6}
$$
是处处定义的态射。

### B.2. 正规化的显式点读数及所有分支

置 $m_r=(r+1)/3$。在 $a_1(a_1-1)\ne0$ 的区间，
$\overline{\mathcal D}_r$ 的方程与 (B6) 准确为
$$
\boxed{
a_2=a_1^r,\qquad
X_{\rm sh}=\frac{4T}{[\,4a_1(a_1-1)\,]^{m_r}},
\qquad Y_{\rm sh}=2a_3-1 .}
\tag{B7}
$$
由 $T^3=[a_1(a_1-1)]^{r+1}a_3(a_3-1)$ 以及
$4^r=4$，直接有
$$
X_{\rm sh}^3=4a_3(a_3-1)=Y_{\rm sh}^2-1.
$$
式(B7)不需要另选一个三次根或扩大原 Artin 域。
在 $q^{-1}(\overline{\mathcal D}_r)$ 的第 $k$ 条图面
$$
G=[\omega^k]\varphi_rF
$$
上，(B7)恰读出 $[\omega^k]H_0$。
这同时确定第三轴的方向和全部三个 CM 相位。

作为 $E_0^2$ 上的完整有理函数除子，
$$
\boxed{
\operatorname{div}(Y_2-Y_1^r)
 =\sum_{k=0}^2\Gamma_{[\omega^k]\varphi_r}
   -3(E_0\times O)-3r(O\times E_0).}
\tag{B8}
$$
在每条图面的泛点其零重数为1；在第一、第二个无穷除子上
极阶分别为 $3r,3$。等式由这些泛型赋值决定，所以图面相交
于 $X_1=0$ 或原点处并不产生一个可删去的新除子，也不允许
在那里只按不同点的个数计数。

(B7)在 $a_1=0,1,\infty$ 可能呈 $0/0$。其含义始终是
(B5)上的正规化态射，不是任意指定该分式的值。
在这些边界上正规化到像还可能把第三轴的几个点合并；
完整交积必须保留下面的 transfer 重数，不能把边界统统置零。

### B.3. 含稳定子重数的有限商 transfer

为避免对奇异 $B$ 误用平坦拉回，明确所用算子。
对一个整闭子簇 $W\subset B$，取 $q^{-1}(W)_{\rm red}$ 的
各不可约分量 $V$，记 $I_V$ 为 $N$ 在其几何泛点的稳定子。
定义
$$
q^\#[W]=\sum_{V\mid W}|I_V|[V].
\tag{B9}
$$
这是有限商的加权 transfer，通常不同于把 scheme inverse
image 随意取约化。令 $D_V$ 为保持分量 $V$ 的分解群。
因为 $r\nmid9$，
$$
[k(V):k(W)]=|D_V|/|I_V|,\qquad
\#\{V\mid W\}=9/|D_V|.
$$
所以在 cycle 层面已准确有
$$
\boxed{q_*q^\#=9,\qquad q^\#q_*=\sum_{g\in N}g_*.}
\tag{B10}
$$

(B9)尊重有理等价。可在相关子簇的正规化上逐个离散赋值核对：
对下层函数 $f$，上层 $\operatorname{ord}(f)$ 等于分歧指数
乘下层阶数；再乘泛型 $|I_V|$，恰成为上层素除子的稳定子阶
乘其剩余域推前次数。将所有上层素除子相加，正是
$q^\#\operatorname{div}(f)$。正规化到原子簇的推前与这个
等式相容。反向用函数域 norm 得到同一个公式。
因此(B9)在 Chow 群上定义，(B10)仍成立；
这里只须倒转9，未倒转 $r+1$。

这也可视为有限群版的 equivariant quotient 交积。
所用稳定子权及其与 divisor boundary 的相容性，在
Edidin–Graham, *Equivariant Intersection Theory*，
arXiv:alg-geom/9603008v3，§3.1，printed pp.15–17，
Propositions5–6 中有同一构造：
<https://arxiv.org/pdf/alg-geom/9603008>。
这里已对本篇阶9、tame、所有不分离度为1的有限商给出
(B9)–(B10)的整系数核对；不以该文一般有理系数定理
替代本篇需要保留的有限域 torsion。

也可直接检查本处系数范围：取自由 $N$-空间 $N\times A$，
以 $(g,x)\mapsto gx$ 映到 $A$，其商底映射为 $q:A\to B$。
上、下两个有限映射的次数都是9；任何下层闭子簇的提升
剩余域次数都整除9，故相应 cycle 推前在 $\mathbf Z[1/9]$
上满射。由上述 proper pushforward 相容性，从自由有限平坦
拉回的 boundary 相容性下降，即得(B9)的 boundary 相容性。
因此这一下降只倒转3，不隐含对其它 torsion 素数的除法。

对 $Y\in\operatorname{CH}_1(B)_{\mathscr R}$，定义完整交积读数
$$
\boxed{
\mathcal K_r(Y)=\frac13\,
 \operatorname{Alb}_{E_0}\operatorname{pr}_{3,*}
 \bigl([\mathcal D_r]\cdot q^\#Y\bigr)
 \in E_0(k)\otimes\mathscr R .}
\tag{B11}
$$
交积在光滑三维簇 $A$ 上进行；$\mathcal D_r$ 是实际 Cartier
除子。$\operatorname{Alb}$ 指从推出的零循环减去其 degree
倍 $O$ 后取 $\operatorname{Pic}^0$。
如果某条曲线落在图面内，使用其 pullback 线丛的第一 Chern
类，不能把它当无限个零点。因而(B11)对所有 Chow 类定义。

在自由且交积正常的开集，(B11)就是用(B7)将曲线与
$a_2=a_1^r$ 的交点送入 $E_0$。全局的定义则是(B11)：
它保留闭点 trace、分歧、非分离交重和全部边界。
本篇不声称奇异粗商上的朴素交点计数与它相同。

### B.4. 最高类的准确三倍及任意原三元映射

$N$ 在两个最高 CM Chow 线上都恒等：
三个特征的乘积为1。此处是正文(2)及附录A的真实 CM
投影等式，故
$$
q^\#q_*\Pi Z=9\Pi Z .
$$
前两个 $\pi_1$ 杀掉 $\Gamma_{\varphi_r}$ 与 $D_r$ 之间的
两个轴除子，第三个 $\pi_1$ 正是取 Albanese。因此
$$
\boxed{\mathcal K_r(q_*\Pi Z)=3\,S_r(\Pi Z).}
\tag{B12}
$$
倍数为3，不是9；除以3来自正规化图面到其像的准确次数。

更具体地，对正文任意实际
$\Phi=(F,G,H_0):X\to A$，即使尚未先施 $\Pi$，也有
$$
\boxed{\mathcal K_r(q_*\Phi_*[X])
       =\sum_{k=0}^2[\omega^k]B_k(\Phi)
       =3\,S_r(\Pi\Phi_*[X]).}
\tag{B13}
$$
证明：令 $g=(\zeta_1,\zeta_2,\zeta_3)\in N$。
$g\Phi$ 落在 $\mathcal D_r$ 的条件是
$$
\zeta_2G=\zeta_1^{-1}\varphi_rF
\quad\Longleftrightarrow\quad G=\zeta_3\varphi_rF,
$$
第三输出为 $\zeta_3H_0$。每个 $\zeta_3$ 对应恰三个 $g$。
把它代入(B10)–(B11)，即得第一等式；
第二等式是正文(27)。所有等式都是 divisor class 的等式，
故也覆盖恒定差映射及边界。证毕。

(B13)是针对这个读数的完整等式，不是说
$q_*\Phi_*[X]=q_*\Pi\Phi_*[X]$。

### B.5. 原 source 的三次下降与真实原点公式

R841附录A已在**整个原权一对应**上作整数和平均：
$$
\varphi^\circ=\sum_{a=0}^2[\omega]^{-a}\varphi R_C^a,
\qquad
\Gamma_i=\frac13\sum_\alpha c_{i,\alpha}\varphi^\circ_{i,\alpha}.
\tag{B14}
$$
所有平均仍是实际 Jacobian 同态，定义于同一个固定域；
三个 $1/3$ 全留在原 $c_\rho$ 中。
故正文(4)可采用同一原类的等变有限表达
$$
\Phi_\rho R_X=R\Phi_\rho,\qquad
\overline X=X/\langle R_X\rangle=X_0(3468).
\tag{B15}
$$
这没有更换原 $q_0,q_2$，也没有把不同的 Hom 向量混同。
因为 $R\subset N$，有真正下降态射
$\overline\Phi_\rho:\overline X\to B$，并且
$$
q_*\Phi_{\rho,*}[X]=3\,\overline\Phi_{\rho,*}[\overline X].
\tag{B16}
$$
这里保留曲线到其像的所有额外有限次数；3仅是原 source
商的次数。由(B13)–(B16)，得到所需准确式
$$
\boxed{
S_r(\Pi\Phi_{\rho,*}[X])
 =\mathcal K_r(\overline\Phi_{\rho,*}[\overline X]).
}
\tag{B17}
$$
因此原 source 的3与(B12)的交积3恰好相消。
对清分母的全部原类，
$$
\boxed{
S_r(\widetilde{\mathcal Z}_{\mathfrak r})
 =D\sum_\rho c_\rho\,
   \mathcal K_r(\overline\Phi_{\rho,*}[\overline X]).
}
\tag{B18}
$$
若 $e_\chi$ 尚未并入 $\rho$，右边仍须加上正文(30)中完整
$18^{-1}\sum_\sigma\chi(\sigma)^{-1}$，并把每份
$\overline\Phi_\rho^\sigma$ 在同一个 $\mathfrak r$ 上约化。
(B1)、(B7)、(B9)均不新增17定义域；它们不使 point-factor
投影变成系数的半线性共轭。

同一等变性也把正文三个差映射简化为一个。
由 $\varphi_r[\omega]=[\omega^2]\varphi_r$，
$$
d_k(R_Xx)=[\omega]\,d_{k+1}(x),\qquad
\mathfrak d_{k+1}=R_X^*\mathfrak d_k,\qquad
B_{k+1}=[\omega]^{-1}B_k.
$$
故准确有
$$
\boxed{
S_r(\Pi\Phi_*[X])
 =B_0(\Phi)
 =\operatorname{Alb}\,H_{0,*}(G-\varphi_rF)^*(O).
}
\tag{B19}
$$
(B19)和(B17)是同一读数的两种实际算法；
它们都保留图面的全部交重，而非只取仿射零集。
也没有从这个简化推出 $B_0$ 为零或非零。

### B.6. 接回原实际模函数，仍保未给出的输入

(B15)使
$$
a_i\circ\Phi_\rho,\qquad T\circ\Phi_\rho
  \in H(\overline X),\qquad \overline X=X_0(3468)
\tag{B20}
$$
成为原模曲线上四个真实代数函数。
它们沿(B2)定义，未任取一个满足相同三次方程的覆盖。
给出这四个函数后，可用(B9)重建有限 Kummer lift，
在光滑原 $A$ 上作(B11)的交积；也可直接正规化(B7)
的对应并保其全部边界权。因此不需要先为任意 Schoen 解消
猜测一个 torsion-level Chow 逆。

在 R851 的目标仿射坐标记为 $(x,y,\xi,\upsilon)$
（即该篇的 $(x,y,r,s)$），同一有理逆为
$$
\begin{aligned}
a_1&=\frac{(\xi-x)y}{x(\upsilon-y)},&
a_2&=\frac{(\xi-x)\upsilon}{\xi(\upsilon-y)},\\
a_3&=\frac{x\xi(\upsilon-y)}{\xi-x},&
T&=\frac{x\upsilon-\xi y}{\upsilon-y}.
\end{aligned}
\tag{B21}
$$
将(B21)代入(B7)，便得到同一模纤维积上明确的 Frobenius
相交方程及点读数；不是只识别其最高 $H^3$。
若经过 R851 的 proper graph 使用(B21)，不定点仍由(B9)–
(B11)处理，不能把主像上的计算代替全部异常项。

还可在原 cusp 处精确固定(B20)的形式展开。
写实际代数映射的微分为
$$
F^*\omega_0=f_F(Q)\frac{dQ}{Q},\quad
G^*\omega_0=g_a(Q)\frac{dQ}{Q},\quad
H_0^*\omega_0=4h_b(Q^4)\frac{dQ}{Q},
\qquad\omega_0=\frac{dX}{2Y}.
\tag{B22}
$$
$f_F,g_a,h_b$ 是这些**实际 Hom** 的拉回形式，含全部
代数归一；不能用名字相同的 normalized newform 擅自代替。
取零常数积分 $z_F,z_G,z_H$，则
$$
z_F=\sum_{n\ge1}\frac{f_{F,n}}nQ^n,\quad
z_G=\sum_{n\ge1}\frac{g_{a,n}}nQ^n,\quad
z_H=\sum_{n\ge1}\frac{h_{b,n}}nQ^{4n}.
\tag{B23}
$$
设 $X(z),Y(z)$ 是 $Y^2=X^3+1$ 的原形式参数展开，
$dX/(2Y)=dz$、$X=z^{-2}+\cdots$、$Y=-z^{-3}+\cdots$。
则(B20)的四个实际 Laurent 展开严格为
$$
a_i(Q)=\frac{Y(z_i(Q))+1}{2},\qquad
T(Q)=\frac{X(z_F(Q))X(z_G(Q))X(z_H(Q))}{4}.
\tag{B24}
$$
这些形式等式在特征零中确定原代数函数；它们不准许直接把
含 $1/n$ 的全积分逐系数约化模 $r$，也不取消原 Hom 的
period/整格归一。

目前尚未列出(B20)的完整函数域表达或(B22)的实际 Hom 基与
代数倍率。因此本附录没有声称已运行(B18)，没有拿有限
$q$-展开或另选 CM 模函数代替这些原输入。
新增的是同一原类的完整九阶商交积、其真实 source 三次消去，
以及可以直接实现的原模函数接口。
canonical7993 与本篇端点仍是不同来源；主目标与原
$AJ_\ell$ 非零仍未由本附录完成。
