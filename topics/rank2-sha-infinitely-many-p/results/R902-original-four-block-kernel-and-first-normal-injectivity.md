# R902 — 原完整四块核的第一法向值单射与真实短窗阈值

日期：2026-11-16。**状态：下述实际核的单射和同一指定目标的唯一性已证明。第一法向值的实际像、指定 trace/forcing 与主目标仍未完成。**

[R836](R836-original-restricted-euler-values-and-three-long-kernel-presentation.md)
将原三个长块写成同一曲线上的两个受限值与真实 $3\eta$ 镜轴；
[R840](R840-original-double-ramification-euler-image-and-unique-normal-tail.md)
进一步证明第四短块的前段给第二法向值一个额外高前缀。
本篇用这个已经读取的前缀，排掉完整四块核中第一法向限制截面为零的整个分支。
这不是只排一个显示的原函数子格，也不是把未加前缀的 Euler 满像继承到受限像。

准确地说，零第一值的核单射到一个真正的 $N^2$ 高前缀截面空间；
当其次数为负时，第一法向值在整个所述四块核上单射。
原 $\mathcal W_D$ 中不属于本篇已付子格的其它列仍保留。

## 1. 同一原来源、角帽与物理长度

保持 R836/R840 的原十九角曲面 $X$、几何整 Cartier 曲线
$$
C=(F=0),\qquad P=(0,1),\qquad
N=\mathcal O_C(C),\qquad \kappa=C^2,
$$
以及实际截面格
$$
\mathcal H_j=H^0(X,\mathcal O_X(jC)),\qquad
\mathcal E=Y\partial_Y,\qquad e=\mathcal EF.
\tag{1}
$$
$P$ 光滑且 $e(P)\ne0$。所有 Euler 算子均为完整物理单位运输后的相对 Euler；
十九角逐框证明给 $\mathcal E\mathcal H_j\subset\mathcal H_j$。
设
$$
b=\deg_YF,\qquad 3b<p,\qquad F_0(t)=F(t,0)\ne0.
\tag{2}
$$
只使用已整返回同一个原格的子格
$$
q_{\rm src}t^r\mathcal H_3\subset\overline{\mathcal W_D},
\qquad q_{\rm src}(P)\ne0.
\tag{3}
$$
$q_{\rm src}$、原 $P_{134}/U_0$、总 charge 四十及全部原 Gauss 帽
都包含在 (3) 及 R836 的同源单位下三角运输中。

沿 $C$ 的指定支写
$$
g(t)=\psi(t)\exp\eta(t),\qquad \operatorname{ord}_t\eta=h.
$$
本篇假设
$$
\boxed{
h<T\le2h,\qquad T-h>\kappa,\qquad T>3z_-,
}
\qquad z_-=C.H_-.
\tag{4}
$$
这里 $H_-$ 为原严格负水平。由前两个不等式已得 $h>\kappa$、$T>2\kappa$。
不把 $T-h>\kappa$ 的严格号弱化。

原四块物理矩阵的长度准确是
$$
\boxed{
T=s-r-13,\qquad
\ell_{\rm eff}=\max(\ell-r,0)<T,\qquad p=6s-1.
}
\tag{5}
$$
相对 $J_4$ 若另行使用，则取其自己的 $T=s-r$；
不以这个长度代替 (5)。定义
$$
q_T=T-h,\qquad
H_*=\min(T,h+\ell_{\rm eff})
     =h+\min(\ell_{\rm eff},q_T).
\tag{6}
$$

在上述真实单位运输后，所述子格的完整约化四块核为
$$
\boxed{
K_{4,T,\ell_{\rm eff}}
=\left\{G\in\mathcal H_3:
\begin{array}{l}
G(t,g),\ \mathcal EG(t,g),\ \mathcal E^2G(t,g)\in t^T k[[t]],\\
\mathcal E^3G(t,g)\in t^{\ell_{\rm eff}}k[[t]]
\end{array}\right\}.
}
\tag{7}
$$
第四行只读实际 $\ell_{\rm eff}$，没有扩成第四长行。
当 $\ell_{\rm eff}=0$ 时，这一条件为空。

原零 charge 格和同源限制序列为
$$
\mathcal H_j^0=d^{j\mu_{d,1}}k[t]_{\le jz_-},
\qquad d=1+8t,
\tag{8}
$$
$$
\ker\!\left[\mathcal H_j\longrightarrow H^0(C,N^j)\right]
=F\mathcal H_{j-1}\quad(j\ge1),\qquad \mathcal H_0=k.
\tag{9}
$$
这些是原截面格上的式子。
特别，后文出现的 $A\in\mathcal H_2$、$L\in\mathcal H_1$
由 (9) 得到，不能改成仅在 $k(t)[Y]$ 中的形式商。

## 2. 第四短行给同一个第二值的准确前缀

对同一个 $G\in K_{4,T,\ell_{\rm eff}}$，记
$$
V_i=(\mathcal E^iG)|_C\in H^0(C,N^3).
$$
有限逆 Taylor 展开及 $\eta^2\in(t^T)$ 给
$$
V_0\equiv G(t,g)-\eta\,\mathcal EG(t,g),\qquad
V_1\equiv \mathcal EG(t,g)-\eta\,\mathcal E^2G(t,g)
\pmod{t^T}.
$$
所以
$$
\boxed{V_0,V_1\in V_T:=H^0(C,N^3(-TP)).}
\tag{10}
$$
同样，
$$
V_2\equiv\mathcal E^2G(t,g)-\eta\,\mathcal E^3G(t,g)
\pmod{t^T},
$$
因而
$$
\boxed{V_2\in H^0(C,N^3(-H_*P)).}
\tag{11}
$$
这是 R840 的零目标特例，亦由上述三项直接证明。
被略去项含 $\eta^2$，全部局部系数在光滑 $P$ 正则。
没有使用 $\mathcal E^3G$ 在未读的短窗之后的值。

## 3. 零第一法向值的整个核落入真正的二次高前缀格

置
$$
K^{(1=0)}
=\{G\in K_{4,T,\ell_{\rm eff}}:V_1=0
       \text{ 作为整个 }C\text{ 上的限制截面}\}.
\tag{12}
$$
(12) 中的零不是仅指原点 jet 为零；后者对所有 (7) 中的 $G$ 已由 (10) 成立。

**定理 1。** 有一个自然的同来源单射
$$
\boxed{
K^{(1=0)}
\hookrightarrow H^0(C,N^2(-H_*P)),\qquad
G\longmapsto A|_C,\qquad \mathcal EG=FA.
}
\tag{13}
$$
其中 $A$ 唯一，而且准确属于原 $\mathcal H_2^{>0}$。

**证明。** $V_1=0$ 和 (9) 给唯一
$$
\mathcal EG=FA,\qquad A\in\mathcal H_2.
\tag{14}
$$
$\mathcal EG$ 的 charge 零为零，取 (14) 的 charge 零系数得
$F_0A_0=0$。因 $F_0\ne0$，有 $A_0=0$，即 $A\in\mathcal H_2^{>0}$。
因此其 $Y$ 次数至多 $2b$，并保全部实际十九角帽，而非只付这个粗次数。

原乘积法则在同一 $C$ 上给
$$
V_2=(\mathcal E(FA))|_C=e|_C\cdot A|_C.
\tag{15}
$$
$e(P)$ 是单位，故 (11) 迫 $\operatorname{ord}_P(A|_C)\ge H_*$，
这证明 (13) 的目标范围。

须再证 (13) 的核为零。若 $A|_C=0$，由 (9) 得
$A=FL$、$L\in\mathcal H_1$。
再次取 charge 零，$A_0=F_0L_0=0$，所以 $L_0=0$。
于是
$$
\mathcal EG=F^2L,\qquad
\mathcal E^2G=2FeL+F^2\mathcal EL.
\tag{16}
$$
沿 $g=\psi e^\eta$ 使用同一有限展开，
$$
\mathcal E^2G(t,g)
=2e(P(t))^2\,\eta(t)\,L|_C(t)\pmod{t^T},
\tag{17}
$$
这里 $e(P(t))$ 表示 $e(t,\psi(t))$ 的完整轴函数，不只取首常数。
其它项均含 $\eta^2$。
第三长行和 $e(P)\ne0$ 遂给
$$
\operatorname{ord}_P(L|_C)\ge T-h>\kappa=\deg N.
$$
在原整射影曲线上，非零线束截面的零除子次数等于线束次数；
故 $L|_C=0$。由 (9)，$L=cF$，$c\in k$。
但 $L_0=0$、$F_0\ne0$，故 $c=0$。

现在 $\mathcal EG=0$。因全部原正 charge $1,\ldots,3b$ 都小于 $p$，
$\mathcal E$ 在每个正 charge 上是单位，故 $G\in\mathcal H_3^0$。
按 (8)，$G=d^{3\mu_{d,1}}P_0(t)$，$\deg P_0\le3z_-$。
$d(0)=1$，第一长行及 $T>3z_-$ 迫 $P_0=0$，所以 $G=0$。
证毕。

因此，不付任何额外满射便有准确的核维数上界
$$
\dim K^{(1=0)}
\le h^0(C,N^2(-H_*P)).
\tag{18}
$$
这里只是实际核的单射；不认 (13) 的像为整个右侧，
也不以环境 Riemann–Roch 截面替换 (14) 的真实来源。

## 4. 第一法向值在完整四块核上单射

**定理 2。** 除 (1)–(5) 外，若
$$
\boxed{H_*>2\kappa,}
\tag{19}
$$
则
$$
\boxed{
G\longmapsto(\mathcal EG)|_C
\quad\text{在 }K_{4,T,\ell_{\rm eff}}\text{ 上单射}.
}
\tag{20}
$$
特别，原准确条件
$$
\boxed{\ell_{\rm eff}\ge T-h}
\tag{21}
$$
使 $H_*=T>2\kappa$，故足以给 (20)。

**证明。** (19) 使 $\deg N^2(-H_*P)=2\kappa-H_*<0$，
所以 (13) 的目标为零，$K^{(1=0)}=0$。证毕。

(19) 是略弱于 (21) 的真实短窗门；它没有把短块延长。
例如在已成立的原 $r=2$ 强窗
$$
s=2h+r,\qquad h\ge\kappa+14,\qquad z_-\le2,
$$
有 $T=2h-13$、$T-h=h-13>\kappa$ 且 $T>3z_-$。
此时足够条件 (21) 准确为
$$
\max(\ell-r,0)\ge h-13,
\tag{22}
$$
较弱条件 (19) 则保原式
$$
\min(2h-13,h+\max(\ell-r,0))>2\kappa.
\tag{23}
$$
这些仅是对已经存在、且满足原返回和强窗的候选的结论；
没有由不等式自行构造因子或原首核。

## 5. 真正的非零二步链，不是 Euler 稳定性

保持 (21)。R840 给 $V_2\in V_T$；
同一 $G$ 的原有限 Euler 值满足
$$
D_3(V_0)=V_1|_Z,\qquad
D_3(V_1)=V_2|_Z,
\qquad Z=(e|_C).
\tag{24}
$$
由 R836 中 $V_T\to H^0(Z,N^3|_Z)$ 的单射，
两次兼容中的后继值各自唯一。

在严格负水平 $H_-$ 的实际线性化中，Euler 权为零。
所以正 charge 来源 $\mathcal EG,\mathcal E^2G$ 在
$Z_-=C\cap H_-$ 上均为零；这里保全部厚化、固定角和剩余域。
结合 R836 的
$$
W_T=\{V\in V_T:D_3(V)\in\operatorname{res}_Z(V_T)\},
$$
得到实际单射
$$
\boxed{
K_{4,T,\ell_{\rm eff}}
\hookrightarrow
W_T\cap H^0(C,N^3(-TP-Z_-)),
\qquad G\longmapsto V_1.
}
\tag{25}
$$
同一个原核原本已经由 $G\mapsto V_0$ 单射；
本篇新增的是 (25)，所以非零来源不能再落在整条 $V_1=0$ 分支。

式 (25) 不认 $V_1$ 的像为整个右端，也不认其右端为零。
尤其它没有证明 $V_T$ 或 $W_T$ 对 Euler 稳定，
没有给任意长的 $V_0,V_1,V_2,\ldots$ 链，
也没有把各次兼容分别换成不同的 $G$。
未读的第四尾、第三长行中的同一 $3\eta$ 镜轴与最后 $cF^3$
继续按 R836/R840 联立。

## 6. 同一个指定 forcing 的结果与范围

对 R836 的一个指定完整物理目标，先保低行成员性，
再使用原 $q_{\rm src}$、charge 四十和 $P_{134}/U_0$
的全部单位下三角逆。
若两个实际 $G,G'\in\mathcal H_3$ 在该同一目标的四块上均为解，
则其差属于 (7)。

因此在 (19) 下，若它们的第一法向限制截面相同，
$$
(\mathcal EG)|_C=(\mathcal EG')|_C,
$$
就有 $G=G'$。即：

> 在已经付清的同一子格内，一个指定完整四块目标，加上它的第一法向限制截面，至多有一个实际全局来源。

这不保证该第一值可实现，也不提供一种可自由选取的修正。
对物理来源 $R=q_{\rm src}t^rG$，还有
$$
(\mathcal ER)|_C
=t^r\bigl(q_{\rm src}V_1+(\mathcal Eq_{\rm src})V_0\bigr).
\tag{26}
$$
故本篇的“第一法向值”始终指运输后的 $V_1$；
不能把它混成 (26) 中的一项或直接假设物理 $\mathcal ER|_C=0$。

指定 $\mathfrak G_F(q_{\rm src}t^rG)$、$[b_0]$、
十九边界及原点短尾仍由这个唯一可能的同一 $G$ 读取。
本篇没有判定其在 (25) 的真实像上为零或非零。
同 $K_{\rm corr}/H_{\rm corr}$ 的两条高前缀与镜轴第三行，
以及原三个十三行带、完整 $p^4$ 的末端项和同 $R/S$ 更高位，
全部保留。
原 $\mathcal W_D$ 的其它来源列不由 (20) 或 (25) 删除。

本篇为同源截面序列、原 Euler charge 分解和有限 Taylor 的精确证明；
没有新增数学运行或数值证书。
