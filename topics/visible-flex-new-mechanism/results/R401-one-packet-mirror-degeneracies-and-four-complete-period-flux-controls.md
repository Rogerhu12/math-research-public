# R401：同一真实微包的镜像退化点与四条完整 period 内部通量的联合支付

日期：2026-11-15。**只读原式与纸面证明；没有执行新的 profile 计算、积分、求根、秩程序或人工测试。**

[R399](R399-new-whole-E-natural-kernel-and-four-ordered-internal-period-controls.md)
给出看见真实有序 suffix 的 whole-$E$、whole-$\Lambda$ 核响应。本稿处理同一个微包内部的两个点，而非再次移动到不同副本：在 R391 最终偶母包的一对真实镜像 $A_f$ 零点上，四个原响应已经使两个 period 的四条部分通量独立。

该有限组可以接入原实际截面，并保留所有 prototype、真实倒行、桥及 Klein 成本。结论只付这两个点；不把“一对已经付清”写成该包全部 $A_f$ 零点已经付清。

## 1. 同一最终包与非零原 suffix

固定 R391 的最后实际 profiles、右锚与原有理核心。不再更换母形、频率、幅度、中心或退化点。

取 R399§6 指定的负布局微包：它是完整八副本 cell 最后副本内，负布局末端的倒数第二包。用该包中心 $\xi$ 写
$$
f=a\,u(x-\xi),\qquad g=b\,u(x-\xi),\qquad
R=a^2-b^2\ne0,\quad T=ab .
\tag{1}
$$
所有实际八/十二/五块幅因子已收入 $a,b$；没有把它们改成单位权。

R391 的最终 $u$ 为非零实偶函数，正解析 prefactor、严格单峰和所有内部 $A_u$ 简单零均保留。偶性由起点偶多项式、偶纠正方向及
$\chi(y)\cos Ny,\ \chi(y)y\sin Ny$
保留，不能将任意非偶纤维替换搬到这里。

取左正支上 $(u'^{\,2/3})'$ 的一个正内部极大点 $-y$。原 R340/R345 的存在论证给
$$
y>0,\qquad p:=u'(-y)>0,\qquad r:=u''(-y)>0,\qquad
A_u(-y)=0 .
$$
偶性给
$$
u'(y)=-p,\qquad u''(y)=r,\qquad A_u(y)=0 .
$$
于是实际两个点
$$
x_-=\xi-y,\qquad x_+=\xi+y
\tag{2}
$$
是同一包中不同的简单 $A_f$ 零点，且 $f'$ 都非零。

按 R397 的真实次序定义
$$
n=\sum_{k>i}(T_iR_k-R_iT_k)\mu_k .
\tag{3}
$$
原完整 cell 之后所有 weighted 三矩均闭合；最后两个 TM 符号相反，故 R399(19)给
$$
n=2r_{\rm enc}\tau_{\rm enc}\,\mu_{\rm last}
$$
再乘本 cell 的真实非零幅/翻号因子。因此
$$
\boxed{n_0\ne0.}
\tag{4}
$$
(4)用的是实际最后包的 $\int(u_{\rm last}'')^2>0$，不是可独立指定的矩。后续同 $F_{\rm rat}$ 纠正准确保这些三矩。

## 2. 四个 raw 查询与两个真正 period 通道

对任意成本 V，保原定义
$$
\mathsf V_d=V(f^2,g),\qquad
\mathsf V_e=\frac12\partial_\theta
V(f^2,f\cos\theta+g\sin\theta)\big|_{\theta=0}.
$$
令 $\ell$ 为该包左零 collar，定义
$$
H_{d,\pm}(V)=\int_\ell^{x_\pm}f'\,\mathsf V_d'',\qquad
H_{e,\pm}(V)=\int_\ell^{x_\pm}f'\,\mathsf V_e'',
$$
$$
C_\pm(V)=R\,H_{e,\pm}(V)+T\,H_{d,\pm}(V).
\tag{5}
$$
全四行使用同一个真实左端，不在右半包另起积分锚。

因为 $R\ne0$，
$$
(H_{d,-},H_{d,+},C_-,C_+)
\longleftrightarrow
(H_{d,-},H_{d,+},H_{e,-},H_{e,+})
\tag{6}
$$
是固定可逆线性变换。若 $\pi V=0$，这两个系数正是整个 circle 的两条 canonical period 分支；一般实际 V 上，(5)仍是准确 raw 线性查询，但不先删去其他 pure 相位项。

R397 已证明任意合法 incoming $L_f$ 改动均不改变这四个 raw 内部通量：
$$
f'(L_fk)''=\{A_f(f'k''-f''k')\}'.
\tag{7}
$$
左端真实平零及 $A_f(x_\pm)=0$ 支付边项；未除以 $f'$，也没有在平台 $f'=0$ 处丢失方程。

## 3. 原两条局部列独立支付两个第一通道

采用 R340/R345 的真实列
$$
K_0=\frac13\mathcal B_P[P,S],\qquad K_1=\delta K_0 .
$$
R395 已付
$$
K_0,K_1\in\mathcal R\cap\ker E\cap\ker\Lambda_{\rm all}.
$$
其当前 rank-one 包的完整输出为
$$
K_0(f^2,g)=-\frac{a^2R}{3}(u'')^4,\qquad
K_1(f^2,g)=\frac{a^2R}{3}
\{10x(u'')^4-8u'(u'')^3\}.
\tag{8}
$$
这里 $x$ 是真实全局坐标；$u'$、$u''$ 在 $x-\xi$ 评价。

R340(21)–(24)的完整上端积分只使用
$u'u'''=(u'')^2/3$，不要求所取零点在左侧。所以在两个点均有
$$
h_*=-\frac8{45}a^3Rr^5\ne0,\qquad
H_{d,\pm}(K_0)=h_*,\quad
H_{d,\pm}(K_1)=-10x_\pm h_* .
\tag{9}
$$
镜点处 $u'$ 变号不改变(9)，因为真实分部积分已把它与 $u'''$ 合成退化关系。两个左 collar 项均为零。

局部 rank-one 幅身份还给
$$
C_-(K_0)=C_+(K_0)=C_-(K_1)=C_+(K_1)=0.
\tag{10}
$$
故第一通道矩阵
$$
M_H=h_*
\begin{pmatrix}1&-10x_-\\1&-10x_+\end{pmatrix},
\qquad \det M_H=-20y\,h_*^2\ne0 .
\tag{11}
$$
这是原两列在同一包两个实际点的准确值，不调用不同副本的旧 Vandermonde 结论。

## 4. 新原核支付同包两个残差

R399 的完整第三方向为
$$
\tau_*=64(\chi_{34}-3\chi_{32})-\frac12\mathfrak J .
$$
其原算子
$$
\mathscr A_u^*=D^2(2(u')^2D^2)
-D\{(4(u'')^2+2u'u''')D\}
$$
的零阶系数为零，而且 $\mathscr A_u^*u=0$。所以对所有 $E\in E_8$，
$$
\mathcal R_E^*=\mathcal B_E(\tau_*)
\in\mathcal R\cap\ker E\cap\ker\Lambda_{\rm all}.
\tag{12}
$$
原右三常数给准确部分通量
$$
\int_\ell^x u'(K_u^*w)''
=2(u')^2\{u'w''-u''w'\}.
\tag{13}
$$
将真正右包左尾 $w=p_E(n)$ 代入，R399(16)给
$$
C_\pm(\mathcal R_E^*)
=4a^3p^2\{(\pm p)w''(x_\pm)-r\,w'(x_\pm)\},
\tag{14}
$$
其中左点取 $+p$、右点取 $-p$。

令
$$
E_1=R_{\rm op}/n_0,\qquad
E_2=-2L_{\rm op}/n_0-\xi R_{\rm op}/n_0 .
\tag{15}
$$
$R_{\rm op},L_{\rm op}$ 是原二次算子，避免与(1)的幅差 R 混淆。原完整尾
$$
p_{R_{\rm op}}(n)=n_0x,\qquad
p_{L_{\rm op}}(n)=-n_0x^2/4+n_2/4
$$
使
$$
p_{E_1}'=1,\quad p_{E_1}''=0,\qquad
p_{E_2}'=x-\xi,\quad p_{E_2}''=1 .
\tag{16}
$$
$E_2$ 的真实常数尾保留，只是在(14)中不产生导数贡献。

置 $c_*=4a^3p^2\ne0$、$D_*=p+yr>0$。则
$$
\boxed{
M_C=
\begin{pmatrix}
C_-(\mathcal R_{E_1}^*)&C_-(\mathcal R_{E_2}^*)\\
C_+(\mathcal R_{E_1}^*)&C_+(\mathcal R_{E_2}^*)
\end{pmatrix}
=c_*\begin{pmatrix}-r&D_*\\-r&-D_*\end{pmatrix},
}
$$
$$
\det M_C=2rD_*c_*^2>0 .
\tag{17}
$$
没有假定单包三矩为零，没有更换两端锚，也没有仅用 principal 部分代替完整响应。

## 5. 完整四行像及其真实成本实现

按 $(H_{d,-},H_{d,+},C_-,C_+)$ 排行，四列
$(K_0,K_1,\mathcal R_{E_1}^*,\mathcal R_{E_2}^*)$ 的原矩阵为
$$
\boxed{
M=\begin{pmatrix}M_H&*\\0&M_C\end{pmatrix},\qquad
\det M\ne0 .}
\tag{18}
$$
星号是新列的真实第一通道值；没有将其设为零。用 $K_0,K_1$ 的准确线性组合即可消去这两个列值。

因此四条查询在
$\mathcal R\cap\ker E\cap\ker\Lambda_{\rm all}$
上满射。这个核结论不使任意其他内部点的查询也自动满射。

实际实现用的仍是原 R399/R396 完整协议：

1. 将原 whole-E 商截面、原响应 E 基、新四列所需的完整第三 prototypes、frame/低阶桥、保护有理核心和 Klein 背景从起点纳入同一个有限库。
2. 真仿射安置时不假设固定点查询不变。旧 $\operatorname{span}(K_0,K_1)$ 和完整新模块 $\mathscr M_*$ 均在真平移/正伸缩下稳定；安置后在模块内重新取(18)的列，查询点保持固定。
3. 第三 prototype、共享真倒行及原校正产生的完整成本均进入同一个基准。若响应坐标为 t，有限复制的准确式仍是
   $$
   V=E_0(t)+n\left(2\sum_\alpha\widehat v_\alpha
                         +\sum_\alpha t_\alpha R_\alpha\right).
   \tag{19}
   $$
   不把 $\widehat v_\alpha$ 的内部通量或原商值删掉。
4. 原有限商/目标截面的全部四行代价记录为 $\mathcal E(t,z)$。参数盒、截面与内部小族整数先固定，最后选一个有限 n。剩余方程
   $$
   \mathcal E(t,z)+n(a+Mt)=b
   \tag{20}
   $$
   由同一个一致 $C^1$ 收缩准确求解。
5. 真 Klein 成本为 $V_{\rm base}+4V_B$，所有目标都先减完整基准再除以4。不是将 signed 响应本身当成一条零费用路径。

(19)–(20)的所有读出都是固定 profiles 与固定点的连续线性原函数查询。原 R56/R302 的恢复给所需几何参数 $C^1$ 性，没有对 profiles 运行求值或求根。

由此得到两种分别准确的实际结论：

- 使用 whole-E 商截面，可取
  $$
  \boxed{E=0,\qquad
  H_{d,-}=H_{d,+}=H_{e,-}=H_{e,+}=0.}
  \tag{21}
  $$
- 使用 R396 的原两条固定自然读出截面，可同时任意指定
  $$
  \boxed{(P_{\mathscr L}E,\ A,\
       H_{d,-},H_{d,+},H_{e,-},H_{e,+}).}
  \tag{22}
  $$
  此时原 $qE$ 和其余 $\Lambda_u$ 仍未付。

在(21)中，pure 与平台二次门已经由 whole E 支付，R391 的简单零判据使同一包这两个内部点对两条完整 period 都有光滑逆 germ。R326 的同一个 incoming gauge 不改变(21)，见(7)。

两种实际结论不能相互拼接为 whole $E+A$ 或 whole $E+\Lambda_{\rm all}$。几何通常重新选择；不能宣称在某一旧冻结 metric 上无代价叠加四列。

## 6. 仍然精确保留的条件

本稿不要求、也没有证明当前包仅有这一对 $A_f$ 零点。R391 保证的是全部零点有限且简单，有限频率扰动可能增加其数目。其他内部零点、各包全部自然总通量、完整平端条件、仿射 gluing、$k$ 值闭合及原同相位十三行，仍须按 R394 同一个真实目标逐项处理。

本稿的新内容是同一实际包内的两个镜点及(18)的完整四行原基。它与 R399 的不同副本四维残差像是不同的使用方式；没有重做旧对应点秩，也没有把不同最终 profiles 的支付拼接成同一点结论。