# R114：整个平帽的 C1 缺陷到 C2 修复，常数 1024

2026-11-13，visible-exact-astra-f6a2。

**状态：完整证明，25个有理常数门已实际以 BigInt 执行。**
本篇把 R112 的整帽修复加强为
$$
 \boxed{\qquad
 \|b\|_{C^2(\mathbb S^2)}
 \le1024\,\|T\|_{C^1(C_r)} .
 \qquad}
\tag{114.1}
$$
保持整个小帽；没有帽半径的负幂；无需 $T$ 的二阶导数。
这里是单位球面上的局部兼容修复，不是物理重构乘子为1的声明。
完整强尾、全 PDE 逆、背景邻域及 Newton 收敛仍须支付。

## 1. 精确假设、范数和结论

取北极 $p$ 的图
$$
 \Phi(x)=(x_1,x_2,\sqrt{1-|x|^2}),\quad
 C_r=\Phi(\overline{B_r}),\quad 0<r\le1/8.
$$
固定支持尺度 $R=1/4$。$T$ 是 $C_r$ 上 C1 对称球面张量，并满足
R32/R37 的兼容条件
$$
 \mathcal CT=
 \operatorname{div}\operatorname{div}T
 -\Delta\operatorname{tr}T-\operatorname{tr}T=0
\tag{114.2}
$$
（C1 情形按分布理解）。使用球面连接及 Hilbert–Schmidt 点范数：
$$
 B=\|T\|_{C^1(C_r)}
 =\max(\|T\|_\infty,\|\nabla T\|_\infty),\qquad
 \|b\|_{C^2}=\max(\|b\|_\infty,\|\nabla b\|_\infty,\|\nabla^2b\|_\infty).
$$

**定理114.1。** 存在关于 $T$ 线性的 C2 球面切向场 $b$，
支持于 $C_R$，在整个闭帽 $C_r$ 满足
$$
 \mathcal L_b\sigma=T,
\tag{114.3}
$$
且满足 (114.1)。该构造与固定 $p$ 的全部平面正交作用等变，
特别保当前 D4 对称。南极有相同结论。
两个支持不相交的帽同时修复时，sup 范数常数仍为1024。

设 $T$ 还定义于全球面，令 $T_{\rm cap}=T-\mathcal L_b\sigma$，则
$$
 T_{\rm cap}=0\quad\hbox{在整个 }C_r,\qquad
 \mathcal CT_{\rm cap}=\mathcal CT
\tag{114.4}
$$
按分布成立，而且
$$
 \|T_{\rm cap}\|_{C^1}
 \le \|T\|_{C^1}+2048\,\|T\|_{C^1(C_r)}.
\tag{114.5}
$$

## 2. 局部兼容场只需要 T 的一阶导数

置 $E=T/2$。R71/R112 的局部兼容重构给环境向量场 $\Omega$，
取 $\Omega(p)=0$，并满足
$$
 D_i\Omega=J(E_i{}^\sharp)+\beta_i u,\qquad
 \beta_i=\varepsilon^{jk}\nabla_jE_{ik},\quad Jv=u\times v .
\tag{114.6}
$$
(114.2) 恰使这个环境向量值一形式闭。对于 C1 的 $T$，
一形式连续且分布闭；在球面小帽的单连通图中，分量逐一取原函数，
得到 C1 的 $\Omega$。连续闭形式的这个结论也可在图中先卷积，
利用 $d$ 与卷积交换，再对原函数取 C1 极限。没有假设 $T$ 存在二阶连续导数。

令
$$
 q=\Omega\times u,\qquad \alpha=\Omega\cdot u .
$$
与 R112 完全相同的逐点恒等式为
$$
 \nabla q=E+\alpha J,\qquad
 d\alpha=\beta+(Jq)^\flat .
\tag{114.7}
$$
由 $E\in C^1$、$\alpha\in C^1$ 可知 $q\in C^2$，
且 $\mathcal L_q\sigma=2E=T$。这正是一阶应变重建；
无需为了延伸而先把 $q$ 提升到 C3。

有
$$
 |\beta|\le\sqrt2\,|\nabla E|,\qquad
 |D\Omega|^2=|E|^2+|\beta|^2\le3B^2/4.
$$
帽内点到 $p$ 的球面距离最多
$$
 \arcsin r\le r/\sqrt{1-r^2}\le1/\sqrt{63}<1/7.
$$
又 $\sqrt3/2<7/8$，故
$$
 |q|,\ |\alpha|\le B/8.
$$
对 (114.7) 再求一次协变导数，利用 $\nabla J=0$，得到完整界
$$
 \boxed{\quad
 |q|\le B/8,\qquad
 |\nabla q|\le11B/16,\qquad
 |\nabla^2q|\le27B/16 .
 \quad}
\tag{114.8}
$$
具体地，第一导不超过 $B/2+\sqrt2B/8$；
$d\alpha$ 不超过 $\sqrt2B/2+B/8$，
故第二导不超过 $3B/2+\sqrt2B/8$。
所用的 $\sqrt2<3/2$ 只把常数向上放宽。

## 3. 图中分量的二阶界及中心线性 jet

写 $q=d\Phi\,Q$。因为图的前两个坐标就是 $x$，$Q$ 等于
环境向量 $q$ 的前两分量。特别
$$
 Q(0)=0,\qquad A:=DQ(0)=E(p),\qquad \|A\|\le B/2.
\tag{114.9}
$$
$\alpha(p)=0$ 是这里保留小常数的原因。

在 $|x|\le1/8$ 上可取
$$
 \|D\Phi\|\le L=65/64,\qquad
 \|D^2\Phi\|\le M=33/32 .
$$
这些分别来自 $(1-r^2)^{-1/2}$ 和 $(1-r^2)^{-3/2}$。
对单位坐标方向 $\xi,\eta$，令 $v=D\Phi\,\xi$、
$w=D\Phi\,\eta$，$W=\nabla_vw$。因 $D^2\Phi$ 是竖直向量，
其球面切向投影另有因子 $|x|$，所以
$$ |W|\le rM. $$
把环境微分分成切向和法向，再取水平分量，给
$$
 \begin{aligned}
 D^2Q[\xi,\eta]={}&
 \operatorname{hor}\{\nabla^2q(v,w)+\nabla_Wq\}\\
 &-x\{\langle\nabla_vq,w\rangle+
        \langle\nabla_wq,v\rangle+\langle q,W\rangle\}
 -\xi\langle q,w\rangle .
 \end{aligned}
\tag{114.10}
$$
因此由 (114.8)，
$$
 \begin{aligned}
 \|D^2Q\|/B\le{}&
 L^2\frac{27}{16}
 +rM\frac{11}{16}
 +2rL^2\frac{11}{16}
 +r^2M\frac18+L\frac18\\
 \le{}&\frac{559815}{262144}<\frac94 .
 \end{aligned}
\tag{114.11}
$$
这一步显式利用了球面图的水平投影；没有把各个图/连接常数统一替换成1024。
以后只使用较宽的
$$ M_2:=\|D^2Q\|_\infty\le9B/4. $$

## 4. 保整个边界 jet 的 3、−3、1 反射

令
$$
 P(x)=Ax,\qquad Z(x)=Q(x)-P(x).
$$
由 (114.9) 及积分 Taylor 公式，在 $|x|\le r$，
$$
 |Z|\le\tfrac12r^2M_2,\quad
 |DZ|\le rM_2,\quad |D^2Z|\le M_2.
\tag{114.12}
$$
不需要三阶 Taylor 余项。

对 $s=|x|\in[r,3r/2]$、$e=x/s$，定义
$$
 \psi_0(x)=re,\quad
 \psi_1(x)=(2r-s)e,\quad
 \psi_2(x)=(3r-2s)e
$$
以及
$$
 \mathcal EZ=3Z(\psi_0)-3Z(\psi_1)+Z(\psi_2).
\tag{114.13}
$$
所有取值仍在原闭球 $|x|\le r$。外端 $\psi_2=0$ 没有奇点，
因为自变量 $s\ge r>0$，$\psi_2$ 本身是光滑映射。

沿每条射线，在 $s=r$ 的0、1、2阶外侧导数系数分别满足
$$
 \sum_{j=0}^2a_j(-j)^m=1,\quad m=0,1,2,\qquad
 (a_0,a_1,a_2)=(3,-3,1).
\tag{114.14}
$$
所以值、法向一阶及二阶 jet 与 $Z$ 完全相同。
它们关于角的相应导数也相同，故所有二阶坐标 jet 都匹配，
不是仅法向 C2。这里有意允许 $\psi_0$ 落在原边界；
它只使用原场的边界迹及切向导数。

为估计二阶映射费用，二维单位径向映射 $u(x)=x/|x|$ 满足
$$
 \|D^2u\|_{\rm bilinear}\le\frac2{\sqrt3\,s^2}
 \le\frac7{6s^2}.
\tag{114.15}
$$
证明可旋转到 $u=e_1$，此时
$s^2D^2u[v,w]=(-v_2w_2,-v_1w_2-v_2w_1)$。
与单位输出向量 $(a,b)$ 配对的对称矩阵算子范数为
$(|a|+\sqrt{a^2+4b^2})/2$；在 $a^2+b^2=1$ 上最大值
是 $2/\sqrt3$，由一元求导或平方配方直接得到。

$\|D\psi_j\|\le(1,1,2)_j$，
$\|D^2\psi_j\|\le(j+1)7/(6r)$。
故 (114.12)–(114.13) 给
$$
 |\mathcal EZ|\le\tfrac72r^2M_2,\qquad
 |D\mathcal EZ|\le8rM_2,\qquad
 |D^2\mathcal EZ|\le24M_2 .
\tag{114.16}
$$
最后一个系数是
$\sum|a_j|\|D\psi_j\|^2=10$ 加上
$\sum|a_j|(j+1)7/6=14$。全部反射项均保留。

## 5. cutoff 的完整费用及无半径逆幂

取五次 smoothstep
$$
 S_5(t)=10t^3-15t^4+6t^5 .
$$
在 $[0,1]$ 上
$0\le S_5\le1$，
$\|S_5'\|_\infty=15/8$，
$\|S_5''\|_\infty=10/\sqrt3$，
且两端一、二阶导数均为零。

令 $\chi_r=1-S_5(2(s-r)/r)$ 于 $[r,3r/2]$。
对径向函数，Hessian 的两个特征值是径向二导与一导除以 $s$，
所以
$$
 |D\chi_r|\le15/(4r),\qquad
 \|D^2\chi_r\|\le70/(3r^2).
\tag{114.17}
$$
用 $\chi_r\mathcal EZ$ 连接内侧的 $Z$，并在 $s\ge3r/2$ 置零，
得到 C2 延拓 $\widetilde Z$。两边界的完整匹配和 cutoff 的零二 jet
证明其 C2 性。由 (114.16)–(114.17)，
$$
 \begin{aligned}
 \|\widetilde Z\|_\infty&\le\tfrac72r^2M_2,\\
 \|D\widetilde Z\|_\infty&\le\tfrac{169}{8}rM_2,\\
 \|D^2\widetilde Z\|_\infty
 &\le\left(24+2\frac{15}{4}8+\frac{70}{3}\frac72\right)M_2
 =\frac{497}{3}M_2<166M_2 .
 \end{aligned}
\tag{114.18}
$$
所以 cutoff 的 $r^{-1},r^{-2}$ 分别被真 Taylor 余项的 $r,r^2$ 抵消；
没有省略一阶或二阶 cutoff 项。

对固定的 $R=1/4$，取 $\chi_R=1$ 于 $s\le R/2$，
在 $[R/2,R]$ 用同一 $S_5$ 降到0。置
$$ \widetilde Q=\chi_RP+\widetilde Z. $$
因 $r\le R/2$，在整个原帽上 $\widetilde Q=Q$。
其支持位于 $|x|\le R$，而 $\widetilde Z$ 实际支持至
$3r/2\le3/16<R$。

固定尺度 Taylor 部分的三个界为
$$
 R\|A\|,\quad \frac{19}{4}\|A\|,\quad
 \frac{185}{6R}\|A\|.
$$
和 (114.18) 相加，再用 $r\le1/8$、$\|A\|\le B/2$、
$M_2\le9B/4$，得到
$$
 \begin{array}{c|c|c}
 &\hbox{准确有理上界}/B&\hbox{稍放宽的上界}/B\\ \hline
 |\widetilde Q|&127/512&1/4\\
 |D\widetilde Q|&2129/256&17/2\\
 |D^2\widetilde Q|&2611/6&436
 \end{array}
\tag{114.19}
$$

## 6. 转回球面并支付全部连接项

定义环境切向场
$$
 b(\Phi(x))=D\Phi(x)\,\widetilde Q(x)
$$
于 $C_R$，其外为零。$D\Phi$ 自动将其送入球面切空间。
在固定图 $|x|\le1/4$ 上，
$$
 \|D\Phi\|\le17/16,\quad
 \|D^2\Phi\|\le9/8,\quad
 \|D^3\Phi\|\le1 .
$$
第三个界可由
$3R/(1-R^2)^{5/2}<1$ 得到；不是 $\widetilde Q$ 的三阶正则要求。
对环境分量作通常坐标微分，(114.19) 给
$$
 |b|\le17B/64,\quad
 |D_xb|\le149B/16,\quad
 |D_x^2b|\le3861B/8.
\tag{114.20}
$$

还须把这些坐标界转换成球面协变界。对单位球面切向量 $v,w$，
其水平分量的长度不超过1；坐标函数满足
$\nabla_\sigma^2x=-x\sigma$。对于切向场 $b$，
$$
 \nabla^2b(v,w)
 =P_u\{D_x^2b[v_{\rm hor},w_{\rm hor}]
              -D_xb[x]\langle v,w\rangle\}
   +\langle b,w\rangle v .
\tag{114.21}
$$
这是微分切向投影 $P_u=I-u\otimes u$ 的准确公式。
因此二阶双线性算子范数不超过
$|D_x^2b|+R|D_xb|+|b|$。
二维两个输入指标的 Hilbert–Schmidt 范数最多再乘2，故
$$
 |\nabla^2b|
 \le2\left(\frac{3861}{8}+\frac14\frac{149}{16}
                         +\frac{17}{64}\right)B
 =\frac{15527}{16}B<1024B.
\tag{114.22}
$$
同理 $|\nabla b|\le\sqrt2\,|D_xb|<1024B$，
零阶也小于此界。于是 (114.1) 证明完毕。

支持边界的零二 jet 使 $b$ 的零延拓确为 C2。
(114.3) 来自整个原帽上 $\widetilde Q=Q$。
恒等式 $\mathcal C\mathcal L_b\sigma=0$ 按分布成立，
给 (114.4)；$|\mathcal L_b\sigma|$ 及其一导分别不超过
$2|\nabla b|$ 和 $2|\nabla^2b|$，即得 (114.5)。

## 7. 对称、两个帽及迭代接口

局部原函数的基点条件 $\Omega(p)=0$ 固定了唯一的三维 Killing 自由度；
正交作用下的轴向向量变换与叉乘相容，所以局部 $q$ 等变。
取水平分量、中心 Taylor1、径向反射、两个径向 cutoff 及图的微分
也均与平面正交作用交换。故整个修复保 D4，包括反射。
南极图只有竖直坐标符号改变，全部常数相同。

若同时修复南北两个小帽，两个 $C_R$ 不相交。
将各自场相加，在每一点至多一个非零，因此 (114.1) 不增加因子2。
这不是把两个不同局部刚体场当作一个全局规范；
实际添加的是两个有明确支持和应变费用的全局场。

在 R112 的同一 Newton 构造中，
可以把其原整帽修复替换为本算子。
在兼容缺陷 $T$ 上，这给一个 C1 到 C2 的实际有界线性修复，
同时保持全部材料小帽，而无需逐步缩小 H。
帽半径随允许的轴向刚体平移变化，只要仍有 $0<r\le1/8$，
每步都适用同一1024界。本文没有声称算子关于 $r$ 的任意高阶参数导数
也有同一界。

物理重构还要乘 $\rho^{-1}$、作真实坐标变换，并支付这些有限阶乘子；
强尾 $w=\lambda_\pm u_z$ 与高模 C2 零延拓、完整源和邻域仍按 R112 保留。
本篇不把一项局部修复常数当成全 Newton 或最终 reach/幅度证书。

## 8. 实际精确常数核

源码 scripts/fourfold_whole_cap_C1_repair_exact.mjs；
完整紧凑结果 notes/2026-11-13-R114-C1-to-C2-whole-cap-exact.json。
纯核在 V8 已实际执行25门，全部通过。
所有量用约分 BigInt 分数；平方比较只用于已知正数，
没有浮点近似参与门判定。三个边界 jet 恒等式也逐整数检查。

源码 SHA256：
f89eeb013e5b7c591d547e7fbf890ef76e8c11643659b45a07a64099485dc91e。
完整结果 SHA256：
6c722866ce9c381747060c79154d32556ed00ea9f5b4a41f6e72ac7c9c64ef98。

这些门核算的是本篇已证明的估计链；其输入是明确的兼容张量假设，
不是当前未知非线性解的数据。Node文件CLI尚未运行，和纯BigInt核执行分开记账。
