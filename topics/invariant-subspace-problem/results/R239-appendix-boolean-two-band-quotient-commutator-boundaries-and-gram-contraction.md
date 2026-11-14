# R239 附录：原Boolean两带结构、首头商的三阶交换子边界与Gamma正规方程

日期：2026-11-14 UTC。作者：Astra-ISP-0c017065 / boundary_nonprimitive_1856；AI-assisted，GPT-6 Astra Pro。

状态：以下恒等式、支持和范数界已逐项核验。原 Boolean 删除的三阶交换子在压缩后有两类明确边界；本稿没有把压缩误当成保持无边界恒等式，也没有宣称已付所需窗口阶局部化。

依赖：[完整首物理头商及三种原Gram](R239-appendix-first-physical-head-quotient-gram-for-left-plus-bare.md)、[实际联合旗](R271-appendix-two-sided-actual-head-flux-gram-and-exact-energy-gap.md)及原 Boolean 关系
$$[D,D^*]=S_mI-2W_m,\qquad\operatorname{ad}_D^3(D^*)=0.$$
沿这些原对象，固定 $d=2^m$、合法 q，$D=D_m$、$\nu=\|D\|\le1/m$。全部正交投影仍为原物理内积中的投影。

## 1. 原尾准确只有两种下降

令
$$E_{h,p}=\ker D^h\cap\mathcal H_p,\quad
W_{h,p}=E_{h,p}\ominus E_{h-1,p},\quad E_{0,p}=0.$$
对 $x\in E_{h,p}$，原三阶交换子给
$$D^{h+2}D^*x=
D^*D^{h+2}x+(h+2)[D,D^*]D^{h+1}x
+\binom{h+2}{2}[D,[D,D^*]]D^hx=0.$$
因此 $D^*E_h\subset E_{h+2}$。若 $x\in W_h,\ y\in E_{h-3}$，则
$\langle Dx,y\rangle=\langle x,D^*y\rangle=0$；再用 $Dx\in E_{h-1}$，得到
$$\boxed{DW_{h,p}\subset W_{h-1,p-1}\oplus W_{h-2,p-1}.}\tag{1.1}$$
无效下标项取零。

定义出生指标 $a=p-h+1\ge0$。两项分别为
$$(a,h)\longmapsto(a,h-1),\qquad
(a,h)\longmapsto(a+1,h-2). \tag{1.2}$$
即每次降一孔，出生保持或增加一；后者额外降低一层短核阶。

## 2. 先在全部孔层取高出生商

先不硬截 $q+d$。令
$$Q=\bigoplus_{j\ge1}E_{j-1,q+j},\qquad P=I-Q.$$
Q 恰为 $a\ge q+2$，P 恰为 $a\le q+1$。Q 对 D 不变。按 $Q\oplus P$ 写
$$D=\begin{pmatrix}H&C\\0&\delta_\infty\end{pmatrix},
\qquad C=QDP,\quad\delta_\infty=PDP|_P.$$
各块范数不超过 $\nu$。由 (1.1)，C 仅有
$$C|_{\mathcal H_{q+j}}
=P_{W_{j-2,q+j-1}}DP_{W_{j,q+j}},\qquad j\ge3. \tag{2.1}$$
故 C 只跨出生右边 $q+1\to q+2$。

第一交换子的低低块为
$$\boxed{[\delta_\infty,\delta_\infty^*]
=P[D,D^*]P+C^*C.}\tag{2.2}$$
附加项不可删除。记
$$C_\ell=\sum_{a=0}^{\ell-1}H^aC\delta_\infty^{\ell-1-a};$$
这是 $D^\ell$ 的高低块。把原 $\operatorname{ad}_D^3D^*=0$ 的低低块完整展开，
$$\boxed{B_{\rm birth}:=\operatorname{ad}_{\delta_\infty}^3(\delta_\infty^*)
=C^*C_3-3\delta_\infty C^*C_2+3\delta_\infty^2C^*C.}\tag{2.3}$$
因而
$$\|B_{\rm birth}\|\le12\nu^2\|C\|^2. \tag{2.4}$$
每项的像都在出生 $q+1$：$C^*$ 的像在该层，$\delta_\infty$ 在最大允许出生上不能再向右越界。输入只可能在出生 $q-1,q,q+1$；算子准确降两孔。此为三层出生边界，不能改写成没有支持信息的任意扰动。

## 3. 再限制真实最高短核阶

首头商中的真实 $\mathcal F_d$ 正是
$$\{0\le a\le q+1,\quad1\le h\le d\}.$$
它已自动限制 $p=a+h-1\le q+d$，不另加硬孔边界。令 $\mathsf R$ 为其投影，并按
$\mathcal F_d\oplus(P\ominus\mathcal F_d)$ 写
$$\delta_\infty=\begin{pmatrix}\delta&E\\0&K\end{pmatrix}.$$
这里 $\delta$ 就是首头商稿的删除。E 只从高度 $d+1,d+2$ 输入，输出在 $d-1,d$。

第一交换子准确为
$$\boxed{[\delta,\delta^*]
=\mathsf RP[D,D^*]P\mathsf R+C_d^*C_d-EE^*,\quad C_d=C|_{\mathcal F_d}.}\tag{3.1}$$
两类边界符号相反，均保留。原第一项也可写作
$S_mI_{\mathcal F_d}-2\mathsf RW_m\mathsf R$，没有假定 $W_m$ 与投影交换。

记 $E_\ell=\sum_{a=0}^{\ell-1}\delta^aEK^{\ell-1-a}$。三阶上左块展开给
$$\operatorname{ad}_\delta^3(\delta^*)
=\mathsf RB_{\rm birth}\mathsf R-E_3E^*
+3E_2E^*\delta-3EE^*\delta^2. \tag{3.2}$$
两带结构分别给出三个消项：

- $E^*\delta^2=0$：输入高度至多 d，下降两次后至多 $d-2$。
- $K^2E^*=0$：$E^*$ 的输出高度至多 $d+2$，在 $>d$ 部分再降两次便离开该部分。
- $KE^*\delta=0$：$\delta$ 后至多 $d-1$，$E^*$ 仅能将非零部分升至 $d+1$，K 再降就归零。

所以
$$\boxed{\operatorname{ad}_\delta^3(\delta^*)
=\mathsf RB_{\rm birth}\mathsf R+H_{\rm top},}\tag{3.3}$$
$$\boxed{H_{\rm top}=-\delta^2EE^*-\delta EKE^*+3\delta EE^*\delta,\qquad
\|H_{\rm top}\|\le5\nu^2\|E\|^2.}\tag{3.4}$$
它只读取最高两高度 $d-1,d$，特别在 $\mathcal F_{d-2}$ 上为零；像的高度至少为 $\max(1,d-5)$，且准确降两孔。最高高度边界依然存在。

## 4. 同一个原源和可精确消去的零源边界

沿首头商稿使用
$$\mathcal Bf=\sum_{j=1}^{d-1}(-1)^jV_me_{j-1}D^jf_{q+j}.$$
未来压缩所删的 $E_{j-1}$ 被 $D^j$ 杀掉。重编号后，末项由 $D^d f=0$ 消去，得到
$$\boxed{\mathcal B\delta=-A_m\mathcal B.}\tag{4.1}$$
原全尾前缀 $X_{K,q}$ 对 $A_m$ 不变，所以
$\mathcal C_K=\mathcal B^{-1}X_{K,q}$ 对 $\delta$ 不变。

出生 $q+1$ 的矩形右边恰为首头商零源空间 $\mathcal C_0=\ker\mathcal B$ 中的未来 $W_j$ 部分。因此
$$\operatorname{Ran}(\mathsf RB_{\rm birth}\mathsf R)\subset\mathcal C_0,\qquad
\mathcal B\mathsf RB_{\rm birth}\mathsf R=0,$$
从而
$$\boxed{\mathcal B\operatorname{ad}_\delta^3(\delta^*)=\mathcal BH_{\rm top}.}\tag{4.2}$$
没有把三阶交换子本身认成零。

原最小坐标满足
$$\Gamma f_r=\mathcal B^*(L+B)r\perp\mathcal C_0.$$
故对任意 $x\in\mathcal F_d$，
$$\boxed{\langle\Gamma f_r,\operatorname{ad}_\delta^3(\delta^*)x\rangle
=\langle\Gamma f_r,H_{\rm top}x\rangle.}\tag{4.3}$$
特别当 $x\in\mathcal F_{d-2}$ 时该配对为零。这里保同一个原 $L+B$ 正规方程。

## 5. Gamma的真实出生带宽与不含头条件数的收缩

原首头映射为
$$\mathcal Tf=\sum_{j=0}^{d-1}(V_me_j)(-\delta)^jf,\qquad
\Gamma=\mathcal T^*\mathcal T.$$
若 $\delta^j$ 的一个非零块增加出生 b，由 (1.2) 有
$0\le b\le j$，总高度下降为 $j+b\le d-1$。因此
$b\le\lfloor(d-1)/2\rfloor$。在 $\Gamma$ 的全部
$\delta^{*k}\delta^j$ 交叉项中，出生净变化为两个此类非负增量之差。故
$$\boxed{\Gamma\text{ 在出生方向带宽至多 }\lfloor(d-1)/2\rfloor.}\tag{5.1}$$
原孔方向带宽仍为 $d-1$，全部列间交叉项保留。

另外
$$\mathcal T\delta=(I_{\rm head}\otimes\delta)\mathcal T=-A_m\mathcal T.$$
尾 $\delta$ 在整个联合旗上范数不超过 $\nu$，所以
$$\boxed{\delta^*\Gamma\delta\preceq\nu^2\Gamma.}\tag{5.2}$$
由于 $\mathcal C_K$ 对 $\delta$ 不变，此收缩降到真实 $\Gamma$ Schur 商：对任意商类，先取全部 $\mathcal C_K$ 修正的范数下确界，再用 (5.2)，所得商算子范数仍不超过 $\nu$。

同一原源上还有直接推论
$$\boxed{A_m^*(L+B)A_m\preceq\nu^2(L+B).}\tag{5.3}$$
证明是 $\delta f_r$ 为源 $-A_mr$ 的合法候选，于是
$$\langle(L+B)A_mr,A_mr\rangle
\le\langle\Gamma\delta f_r,\delta f_r\rangle
\le\nu^2\langle(L+B)r,r\rangle.$$
这不控制 $\delta$ 的逆，也不把 $\Gamma$ 的总体条件数变成单位。

## 6. 仍需支付的实际接口

原 Boolean 结构把压缩三阶缺陷分成可由源正规方程准确消去的出生边界，以及必须继续控制的最高高度边界。双向带宽和真实能量收缩同时保持。

下一步仍须对 $\Gamma_{CC}^{-1}$ 与原物理低侧测试得到窗口阶上界。固定物理低头的测试在首头坐标中可以触及最高高度，因此不能据低头固定就删除 $H_{\rm top}$；也不能把单列 $V_me_j\delta^jf$ 免费按 $\Gamma$ 范数控制。普通 ISP 与无权 $N=M$ 仍开放。
