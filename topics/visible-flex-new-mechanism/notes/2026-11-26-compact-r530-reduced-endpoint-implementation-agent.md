# 紧凑 R530 输入的准确 27 状态端图与全程空间读出

日期：2026-11-26。实现前的原式接口。本文不宣称四个偶矩已有有限根，不把任意给定的 $h(k)$ 曲线当作同规范 ruling 的解。目标是直接评价 R530 的真实有限尺度端图，同时记录整段空间范围。

## 1. 只压缩 ruling 所读的第三投影，不删除第三历史

固定一份 R521 实际库、共同右锚及固定 $y=x+\omega_c$ 坐标。
在 $\theta=\pi/2$ 置
$$
\phi=g,\qquad \Delta=f^2-g^2 .
$$
R521 已准确证明全相位 ruling 为 $\sin^2\theta$ 乘同一 scalar，
因此此处的一个 phase 评价读出整个 scalar 方程，不是用一个相位替代未知的其它相位。

保原八维矩阵 $A=\Phi_{\mathsf a}$。
对完整第三算子 $T$，只为计算 ruling 定义三个真实状态
$$
t_j=I_{j,y}\{g,T(g;\Delta)\},\qquad j=0,1,2.
\tag{1}
$$
给定的三元组必须来自正在运行的同一个真实 $T$；
没有将三槽算子换成三个独立可控 profile。

R482 **未消历史**的(24)及 R544 的真实配对给
$$
\begin{aligned}
\mathscr K={}&
\mathscr R(S,\gamma,\upsilon,h_{ss},k_{ss})
+\mathscr L_S(\Phi_{\mathsf a}\Delta)\\
&-\mathbf w_y(S)\cdot
 \mathbf I_y(\Phi_{\mathsf a}\Delta,\Phi_{\mathsf a}\Delta)
-4\mathbf w_y(S)\cdot t
-2\mathbf w_y(S)\cdot\nu,
\end{aligned}
\tag{2}
$$
其中
$$
d=h\eta-k,\quad
\mathbf w_y=\left(\frac{1+d^2}{4h},\frac d2,\frac h4\right),
\quad \eta=\omega-\omega_c .
$$
$\mathscr R$ 是原完整局部值，含原 $M_{\rm raw}$ 引起的 chain 项；
$\mathscr L$ 保原速度与八矩交叉项。
(2)对两个加速度仿射，其准确系数就是 R521 的 $C_h,C_k$。
规范仍是同一个 $\chi^\nu$，并非沿 $s$ 重选。

令 $E_\alpha$ 为原八基。预先定义固定完整四次张量
$$
B_{j,\alpha\beta}
 =I_{j,y}\{g,\Phi_{E_\alpha}
           (g,\Phi_{E_\beta}\Delta)\},
\tag{3}
$$
以及原完整局部收缩
$$
c_j(S,\gamma,\upsilon,a,b)
 =I_{j,y}\{g,\mathcal C_s(g;\Delta)\}.
\tag{4}
$$
$\mathcal C_s$ 必须使用 R73(16)的
$$
\mathcal C_s(g;\Delta)
 =R[H(Y_g,K_s(\Delta))]
  -\Psi_s(g,\Phi_{M_{\rm raw}}\Delta),
\tag{5}
$$
其中对整个 second local 场真正作 $s$ 导数。
(5)保 R73(15)的变化-profile 项，不用静态 third 公式替代。

由原 $T_s=-\Phi_M\circ A+\mathcal C_s$，
$$
\boxed{
(t_j)_s
 =-\sum_{\alpha,\beta}
 M_\alpha(S,\gamma,\upsilon)\,\mathsf a_\beta
 B_{j,\alpha\beta}
 +c_j(S,\gamma,\upsilon,a,b).}
\tag{6}
$$
右侧不含其它第三坐标。
$c_j$ 对 $a,b$ 至多仿射；其所有系数由同一已固定的 profiles 与原右积分决定。

所以为求真实几何及八矩，状态可以准确压到
$(h,k,\eta,\gamma,\upsilon,\mathsf a,t)$ 的 16 维。
原完整 $T$ 可以在所得几何上随后由其线性累计公式恢复；
特别，(1)末值为零并不等于完整第三 period 为零。

## 2. R530 双边的 27 维真正 ODE

正侧共用五个几何状态
$$
S_+=(h,k,\omega_c+\eta),\qquad
h_s=\gamma,\quad k_s=\upsilon,\quad
\eta_s=\upsilon/(2h).
$$
负侧按原实际物理时间 $-s$ 读取
$$
S_-=(h,-k,\omega_c-\eta),\qquad
(\gamma_-,\upsilon_-)=(-\gamma,\upsilon).
$$
两侧各有一份真实 $(\mathsf a_\pm,t_\pm)$，
共 $5+2(8+3)=27$ 个状态。

将(2)两侧的无加速度部分记作 $F_\pm$。
原真实加速度仍由
$$
\begin{pmatrix}
C_h(S_+)&C_k(S_+)\\
C_h(S_-)&-C_k(S_-)
\end{pmatrix}
\binom a b
=-\binom{F_+}{F_-}
\tag{7}
$$
唯一给出。
在 R530 的共同合法盒
$$
h>0,\quad y\pm\eta>0,\quad
h(y\pm\eta)\mp k>0,\quad
h^2(y\pm\eta)^2>1+k^2
$$
中，原行列式有严格正下界。
这里没有增加一个新的独立输入去覆盖未解的 ruling 行。

记(6)右侧的函数为 $G_j(S,\gamma,\upsilon,a,b,\mathsf a)$。
完整两侧演化是
$$
(\mathsf a_+)_s=M_+,\qquad
(t_+)_s=G_+(S_+,\gamma,\upsilon,a,b,\mathsf a_+),
$$
$$
\boxed{
(\mathsf a_-)_s=-M_-,\qquad
(t_-)_s=-G_-(S_-,-\gamma,\upsilon,a,-b,\mathsf a_-).}
\tag{8}
$$
负侧的整个右侧反号，不能只翻 $M$ 而保局部 $\mathcal C$ 的原号。

中心资料采用 R530 原式：
$$
h(0)=H,\quad k(0)=\eta(0)=\gamma(0)=0,\quad
\upsilon(0)=v_0,
$$
$$
\mathsf a_+(0)=\mathsf a_-(0)=\mathsf a_{\rm o}\in E_{\rm o},
\qquad t_+(0)=t_-(0)=0 .
\tag{9}
$$
$t=0$ 来自原完整中心 $T=0$。
中心非零 $\mathsf a_{\rm o}$ 仍按 R530(10)(11)(34)(35)
由同一合法固定第二规范和最终左端重锚解释，
不是免费指定一条已运行路径的中途 history。

对每一实际存在到 $L$ 且保合法盒的解，读
$$
O_L=\operatorname{pr}_{E_{\rm o}}\mathsf a_+(L),\qquad
E_L=\operatorname{pr}_{E_{\rm e}}\mathsf a_+(L),
\tag{10}
$$
其中
$$
E_{\rm e}=(p_1,t_1,r_1,s_0),\qquad
E_{\rm o}=(p_0,p_2,r_0,s_1).
$$
准确目标是同一条解上的 $(O_L,E_L)=0$。
原四奇总矩自动零，但共同端奇入值 $O_L$ 仍须保持；
小 $L$ 的原 IFT 不被推广成任意有限 $L$ 的无条件逆。

## 3. 用同一正半轨道读出整个实际空间范围

令 $D_B=\operatorname{diag}(-1,-1,1)$，
从中心 $F(0)=I,\alpha(0)=0$ 在正侧积分
$$
F_s=F\Omega(k),\qquad
\alpha_s=h^2Fe_1 .
\tag{11}
$$
R530 的准确几何奇偶给
$$
\boxed{
F(-s)=D_BF(s)D_B,\qquad
\alpha(-s)=D_B\alpha(s).}
\tag{12}
$$
证明只需核
$D_B\Omega(k)D_B=-\Omega(-k)$；
再用 $D_Be_1=-e_1$、$h(-s)=h(s)$ 与 ODE 唯一性。
不使用 profile 空间反射。

记 $N(s)=F(s)e_2$。
同一个固定材料坐标 $y$ 上，两侧真实基底为
$$
X_+(s,y)=\alpha(s)+\frac{h(s)}{y+\eta(s)}N(s),
$$
$$
\boxed{
X_-(-s,y)
 =D_B\left\{\alpha(s)
     -\frac{h(s)}{y-\eta(s)}N(s)\right\}.}
\tag{13}
$$
所以只须积分正半 frame 和位置，但空间范围必须读出(13)两侧，
不能只记录一个最终位移或 $\alpha(L)$。

若先选球心 $c=c_3e_3$，则 $D_Bc=c$。
对每个固定 $s$，$\|\alpha\pm uN-c\|^2$ 是 $u$ 的凸二次式；
$y$ 在材料窗口两端间单调改变 $u=h/(y\pm\eta)$。
因此整个窗口上的半径最大值准确落在下列四条边界曲线上：
$$
\alpha(s)+\frac{h(s)}{\ell_y+\eta(s)}N(s),\quad
\alpha(s)+\frac{h(s)}{r_y+\eta(s)}N(s),
$$
$$
\alpha(s)-\frac{h(s)}{\ell_y-\eta(s)}N(s),\quad
\alpha(s)-\frac{h(s)}{r_y-\eta(s)}N(s).
\tag{14}
$$
对(14)取整个 $0\le s\le L$ 的连续上界，再乘2，才给完整基底直径上界。
这不是 finite sample 已经给连续认证的声明；
数值阶段须保时间细化，严格阶段可用原 ODE 导数盒认证这些一维 supremum。

局部曲率继续用 R573 的准确形算子。
全局 reach 下界还需真实嵌入与所有非局部法弦；
(14)或一个局部曲率上界不能代替它们。

## 4. 直接分子评价，避免静态或冻结替身

实现(4)(5)(2)时可以直接使用 R56 的分子演算：

- 第一分子
  $V_q=(-q'/2,0,hq-(hz-k)q'/2)$；
- 原 second local 分子
  $V_K=(\eta_0/h,zP+B,(hz-k)\eta_0/h)$，
  $P,B,\eta_0$ 均按完整 R56(2)(6)读取；
- 对 $V_K$ 真正作 $s$ 导数，使用输入
  $(h_s,k_s,\omega_s,h_{ss},k_{ss},\omega_{ss})$，
  其中 $\omega_{ss}=b/(2h)-\upsilon\gamma/(2h^2)$；
- 原第三局部 $\ell_s=R[H(Y_g,K_s(\Delta))]$
  后再减完整(5)的 chain；
- 原 fourth ruling 保 $Z=K-Y_{\Phi_A\Delta}$ 的全部导数，
  包括 $(\Phi_A\Delta)_s=\Phi_M\Delta$，
  最后加入真实 $-4\mathbf w\cdot t-2\mathbf w\cdot\nu$。

这些步骤只用固定 profile、导数、共同右积分和有限几何 jets。
为加速可以预收固定积分张量，或用已证明的十次平移恒等式评价 R521
参考正交平均；若这样做，必须保持真实复制图与参考矩匹配的数学身份，
不能把物理重叠副本当成原不交库。

当前尚无有限尺度 $(10)=0$ 数值或精确根，
也没有末 scalar germs、pose、完整第三／第四或最终几何主门的新结论。
本接口的用途是让下一次搜索真正沿同一 $K=0$、同一 $\chi$、
全部 incoming 的 ODE 运行，并把全程空间范围作为同时输出。
