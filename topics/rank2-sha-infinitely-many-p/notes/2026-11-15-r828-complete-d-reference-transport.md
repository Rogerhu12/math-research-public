# R828 补充 — 同一原 M 的完整 d 参考运输与 native Schur 消元

日期：2026-11-15。**状态：下列原参考运输、整列恒等与同一首核／首余核上的 Bockstein 公式已证明。**

本补充把 R828 中由 $\log d$ 产生的二次角色项准确吸入参考来源。
这是对同一个实际矩阵的完整参考变换；并未证明该响应属于 $\operatorname{im}\bar M$，
也没有把四个真实中央的低卷积或原 Schur 项赋零。

## 1. 两种参考及同一个实际来源

沿用 [R821](../results/R821-original-four-central-axes-and-complete-four-block-carries.md)
和 [R828](../results/R828-original-four-high-axis-reflection-and-native-central-compatibility.md) 的所有对象、
好素数和固定坏集：
$$
p=6s-1>211,\qquad
w=z^6,\quad t=-x^{-3},\quad d=1+8t,\quad
g=d\Theta^{17}e^{-\kappa w^s},\quad a_p=p\kappa\in\mathcal O^\times.
\tag{1}
$$
原完整角式为
$$
\log\Theta^{17}=\sum_{n\ge1}\ell_nt^n,\qquad
\ell_n=\frac{17}{3n}\frac{(1/3)_n}{(5/6)_n}.
$$
分别定义两个真正的四项多项式
$$
h_\Theta(t)=\sum_{r=1}^4\ell_{s-r}t^{s-r},
\qquad
h_d(t)=\sum_{r=1}^4
 (-1)^{s-r+1}\frac{8^{s-r}}{s-r}\,t^{s-r}.
\tag{2}
$$
每个分母 $s-r$ 都是原 $p$ 单位。
R821 的参考删去了二者：
$$
g_\circ=g\,e^{-h_\Theta-h_d}.
$$
本补充另定义
$$
\boxed{
g_{\Theta,\circ}=g_\circ e^{h_d}=g\,e^{-h_\Theta}.
}
\tag{3}
$$
因此同一实际 $g$ 有准确的两种写法
$$
\boxed{
g=g_\circ e^{h_\Theta+h_d}
  =g_{\Theta,\circ}e^{h_\Theta}.
}
\tag{4}
$$
没有更换 $\Theta,t,\kappa$，没有改变原四个全多项式 $f_\nu$，
也没有改动实际来源格。

这里“只删 $\Theta$ 的高项”是指 (2) 的四个 $\ell_{s-r}$；
不是把 $g$ 中的 $d$ 因子、原 $f_\nu$ 中的 $d$ 零点，
或物理公共因子中的 $d$ 分母删去。

## 2. 原 w 三角坐标中的全精度 d 列

保持 R828 的唯一线性运输
$$
h_A=w^{s-4}P_3(w)+w^sH_A(w),\qquad
P_3=u_0+u_1w+u_2w^2+u_3w^3.
\tag{5}
$$
令 $\mathsf T_s$ 为 R828(31) 的原单位下三角矩阵，
其输入按 $(L_4,L_3,L_2,L_1)^t$ 排列，
其中 $L_r=(-1)^{s-r}A_r$。

记 $u_\Theta,u_d$ 分别是 $h_\Theta,h_d$ 的四个物理坐标。
由 (2) 准确有
$$
L_{d,r}=-\frac{8^{s-r}}{s-r}.
$$
置 $E_p=8^s$，得到全精度公式
$$
\boxed{
u_d=E_p\,\mathsf T_s
 \begin{pmatrix}
 -1/(8^4(s-4))\\
 -1/(8^3(s-3))\\
 -1/(8^2(s-2))\\
 -1/(8(s-1))
 \end{pmatrix}.
}
\tag{6}
$$
原实际四轴就是
$$
u^*=u_\Theta+u_d.
\tag{7}
$$
在模 $p$ 层，R828 的两个固定有理列 $v,z$ 给
$$
\boxed{
u_\Theta\equiv a_pv,\qquad
u_d\equiv\chi_2z,\qquad
\chi_2=(2/p).
}
\tag{8}
$$
第二式使用的只是 $8^s\equiv2\chi_2$；在更高精度仍使用 (6)，
不省略 Fermat 商 $q_p(2)$。

还可把第一列写成全精度的一维式。沿 R828 记
$$
H_p=\frac{17}{3}(-1)^s
       \frac{(1/3)_{s-1}}{(5/6)_{s-1}},\qquad
P_r(p)=\prod_{j=1}^{r-1}\frac{p-6j}{p-6j-3}.
$$
则
$$
\boxed{
u_\Theta=H_p\,\mathsf T_s
 \begin{pmatrix}
 P_4(p)/(s-4)\\
 -P_3(p)/(s-3)\\
 P_2(p)/(s-2)\\
 -P_1(p)/(s-1)
 \end{pmatrix}.
}
\tag{9}
$$
$H_p\equiv-a_p/18\bmod p$，而其高精度仍按 R828(20)–(22)
保留全部原低阶卷积。这不是在模 $p^4$ 中把 $H_p$ 直接换成 $-a_p/18$。

## 3. 四个完整中央的准确参考平移

原来源与相对 charge 为
$$
\widehat\nu_A=(g_A/d)^{q_\nu}f_\nu(t),\qquad
(q_S,q_T,q_U,q_V)=(1,36/17,4,33/17).
\tag{10}
$$
记 $F_\nu^\circ(u)$ 为 R821 的完整八权归一中央多项式模 $p^4$，
并把新的参考 $g_{\Theta,\circ}$ 所给同一式记为 $F_\nu^\Theta(u)$。
由于 (5) 的运输线性、且全部高尾也线性，(3)–(4) 逐来源给
$$
\boxed{
F_\nu^\Theta(u)=F_\nu^\circ(u+u_d)\pmod{p^4}.
}
\tag{11}
$$
在原收敛圆盘上，这首先是整个来源与其完整中央函数的恒等；
R821 的 Hurwitz 四权化和八权尾界再允许按同一模 $p^4$ 读取。
因此没有把第五至第八权或无穷尾在参考变换中另行丢掉。

定义两个真正的参考截距
$$
b=(F_\nu^\circ(0))_\nu\bmod p,\qquad
b_\Theta=(F_\nu^\Theta(0))_\nu\bmod p.
$$
两个参考保留同一原低四阶矩阵 $B_4$，因为 $s-4>4$。
R821 的整 Jacobian 公式与 (8)、(11) 遂给
$$
\boxed{
b_\Theta=b+\chi_2B_4z,\qquad
F^\Theta(u)\equiv b_\Theta+B_4u\pmod p.
}
\tag{12}
$$
四个实际中央同时零的原首必要条件因而准确改写为
$$
\boxed{b_\Theta+a_pB_4v=0\pmod p.}
\tag{13}
$$
这里 $b_\Theta$ 仍是四个不同真实 charge 的全部原低阶卷积。
(13) 不宣称它自动成立或不可能成立。

若 $u^\dagger$ 是旧参考的唯一模 $p^4$ Hensel 解，
则新参考的唯一解准确为
$$
\boxed{u_\Theta^\dagger=u^\dagger-u_d\pmod{p^4}.}
\tag{14}
$$
故原相容条件
$u^\dagger=u^*\bmod p^4$ 等价于
$u_\Theta^\dagger=u_\Theta\bmod p^4$。
后者可用 (9) 的实际一维列检验，仍须保 $H_p$ 的原值。
这只是完整坐标变换，不新增中央条件或提升深度。

## 4. 每个真实 charge 列在同一 M 中怎样运输

设 $\mathcal W_{\rm act}$ 是已经支付的同一个原来源格。
保持其整个物理公共因子、所有实际角帽及固定导子成本。
令 $\Phi$ 为其中一个真正的 charge 列，$Q_\Phi$ 为它对 $g$ 的总 charge；
在原 canonical 单部分中，$Q_\Phi$ 包括公共的四十。
已经运输的混合列亦使用其真实总 charge，不能免费添入新列。

对该列，(3) 给准确的原函数恒等
$$
\boxed{
\Phi[g_{\Theta,\circ}]
 =e^{Q_\Phi h_d}\Phi[g_\circ].
}
\tag{15}
$$
若一条实际来源以若干 charge 项给出，就对其原有限和逐项使用 (15)；
这不是将每项另计为新增来源。
$t$、固定角多项式和既有半特征在 (15) 中均保持原值。

(15) 是同一来源的评价变换，**并未声称**
$e^{Q_\Phi h_d}\Phi$ 本身是原有限角帽内的一个基向量，
也没有假设它给 $\mathcal W_{\rm act}$ 的一个无成本列基变换。
本节始终在相同的已付源格上比较两个评价矩阵。

具体令
$$
h_d=w^{s-4}D_3+w^sH_d,\qquad
D_3=(u_d)_0+(u_d)_1w+(u_d)_2w^2+(u_d)_3w^3.
$$
使用 R821 的同一个目标
$$
\Gamma^{(4)}_{L_4+13}
=\mathcal O[w,\epsilon]/(w^s-p\epsilon,\epsilon^4,
                         w^{\ell+13}\epsilon^3),
\qquad L_4=3s+\ell,\quad1\le\ell<s-13.
$$
保原 $c_*U_{0,\circ}$、$J_{4,\circ}$ 与完整
$\mathcal E_{\rm tot}$，则新参考矩阵为
$$
\boxed{
\begin{aligned}
M_{\Theta,\circ}^{\rm orig}
=c_*U_{0,\circ}\bigg\{&
 \sum_{j=0}^{3}\frac{p^j\epsilon^j}{j!}
 w^{13-4j}(D_3+w^4H_d)^j
 J_{4,\circ}\mathcal E_{\rm tot}^{\,j}\\
&+\frac{p^3\epsilon^3}{24}w^{s-3}D_3^4
 J_{4,\circ}\mathcal E_{\rm tot}^{\,4}
\bigg\}\pmod{p^4}.
\end{aligned}
}
\tag{16}
$$
这是 R821(36) 在真实 $u_d$ 的直接代入。
因此下列内容全部运输，而没有被参考改名抹去：

- 三条十三行跨界带及总成本 $39$；
- 原 $H_d$ 的全高尾和 $U_{0,\circ}$；
- $\ell=s-15,s-14$ 时真正存活的末端四次项；
- 相同来源格、全部原角帽及真实总 charge。

更准确地，先按 (16) 换到新参考、再按 (15) 乘
$e^{Q_\Phi h_\Theta}$，与旧参考一次乘
$e^{Q_\Phi(h_d+h_\Theta)}$ 完全相同。
这一结论在截断以前即由指数乘法成立，
故不需要把两个截断矩阵当作可交换的自由代换来证明。

## 5. 相同 K1、C1 上的 native Bockstein

由 (16) 的所有非恒等项均带 $p$，有
$$
\boxed{\bar M_{\Theta,\circ}^{\rm orig}
       =\bar M_\circ^{\rm orig}.}
\tag{17}
$$
所以两种参考的实际首核、首余核是同一对对象：
$$
K_1=\ker\bar M_\circ^{\rm orig},\qquad
C_1=\operatorname{coker}\bar M_\circ^{\rm orig}.
$$
不是只给一个未指定的维数相等。

设 $\mathcal L_j:K_1\to C_1$ 是 R821(41) 的四个实际高轴响应，
包含其中十二条真实末行。
对同一个 $x\in K_1$，用同一整提升计算两种 native Bockstein。
两矩阵之差除以 $p$ 再模 $p$，由 (16) 只剩一次项，故
$$
\boxed{
\beta_{\Theta,\circ}(x)-\beta_\circ(x)
 =\sum_{j=0}^3 (u_d)_j\mathcal L_j(x)
 =\chi_2\sum_{j=0}^3z_j\mathcal L_j(x)
 \quad\text{于 }C_1.
}
\tag{18}
$$
此处没有预先删 $H_d$。
其消失是在使用原首核的完整阶界
$W_1,W_2\in w^{s-13}k[[w]]$、
$W_3\in w^\ell k[[w]]$ 之后发生：

- 前两项中的 $w^{13}H_dW_i$ 到达下一块端点，
  经 $w^s=p\epsilon$ 在模 $p$ 中消失；
- 末项达到 $w^{\ell+13}\epsilon^3=0$。

因此 (18) 正是原十二末行的响应，
没有忽略另一个低阶角边界。
更高的 Schur 页仍须使用整个 (16)，不能沿用首 Bockstein 的这一消去。

由 (4)、(7) 和 R821 的同一线性首响应，
实际矩阵的 Bockstein 为
$$
\begin{aligned}
\beta_{\rm act}
 &=\beta_\circ+\sum_j((u_d)_j+(u_\Theta)_j)\mathcal L_j\\
 &=\beta_{\Theta,\circ}+\sum_j(u_\Theta)_j\mathcal L_j.
\end{aligned}
$$
于是得到所需的完整参考消元：
$$
\boxed{
\beta_{\rm act}
 =\beta_{\Theta,\circ}
    +a_p\sum_{j=0}^3v_j\mathcal L_j
 \quad\text{于 }\operatorname{Hom}(K_1,C_1).
}
\tag{19}
$$
对任一真正的左行 $\Lambda\in C_1^*$，(19) 给
$$
\boxed{
\Lambda\beta_{\rm act}(x)
 =\Lambda\beta_{\Theta,\circ}(x)
    +a_p\sum_jv_j\Lambda\mathcal L_j(x).
}
\tag{20}
$$
若再假定四个原中央同时零，则由 (13) 亦等于
$$
\boxed{
\Lambda\beta_{\Theta,\circ}(x)
 -(\Lambda\mathcal L_0(x),\ldots,\Lambda\mathcal L_3(x))
          B_4^{-1}b_\Theta.
}
\tag{21}
$$
(20)–(21) 保全部原 native 来源项。
它们没有产生一个新的左核，也未证明显示的数非零。

## 6. 准确范围

二次角色项的完整去除需要同时变换
$$
(b,\beta_\circ)\longmapsto
\left(b+\chi_2B_4z,\,
      \beta_\circ+\chi_2\sum_jz_j\mathcal L_j\right).
$$
因此不能保持旧 $\beta_\circ$ 不动而删去其 $\chi_2$ 响应；
也不能从 (18) 推出 $\sum z_j\mathcal L_j$ 属于 $\operatorname{im}\bar M$。
$C_1$ 中这条响应完全可能非零。

同样，$b_\Theta$ 不是一个自由参数，不是共同的标量余项，
也没有因只剩一条实际高轴列而成为已知零。
下一项真实问题仍是四个原 $K$/sigma 卷积在 (13) 中的指定值，
或同一个实际左行在 (20) 中的指定值。
参考消元、单位 Jacobian 和全精度高轴反射本身均不证明它们不相容。

本补充是逐原来源的符号证明；没有新增数值扫描、运行证书或可重算输出。
