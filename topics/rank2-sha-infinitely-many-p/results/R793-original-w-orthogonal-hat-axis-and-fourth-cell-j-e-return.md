# R793 — 原 W 正交帽轴、固定条件来源与第四块的 J/E 同观察返回

日期：2026-11-15。**状态：以下 whole 核、完整三态返回、固定帽来源和实际第四块条件表已证明。**

本文保持 R734 的同一个 $q=q_N^*$。R789 的 W 返回帽使用
$z^\circ=Z_0-4W/17$，它虽不与 Y 正交，却与 W 及原 q 的全部伙伴正交。
本篇将这条轴真正整化到 degree2808，用已有射线和绝对 Theta 锚支付其两层核。
再付第三正交轴，得到保 W 的两个独立偶深返回。

这允许把 R789 的固定帽直接送到 R786 的同一有限 J 来源，保原 U 失败门及额外 Y-unit。
更直接的算术接点是一张完整的 J/E 两门表：两列是原 E 深、浅的同一 W Mellin 行，
两行是原 J 深、浅来源。物理 E 浅的两个格子准确落入 R789 尚未处理的第四块。
所有局部质量、另一个 E 门和第三中央所需的 W 深补域均显示保留。

本文没有把 R791 的 $t/Y$ 两点值独立换成 W 中央独立，也不把
R789 的 $\lambda^{-m}$ 稳定族再计成独立零。

## 1. 原空间、实际 W 正交行与新整轴

保持原普通射线、所有固定坏集、$p>163$，置
$$
\omega^2+\omega+1=0,\quad \delta=1+2\omega,\quad
a=1+3\omega,\quad \alpha=17-3\omega,\quad
b_Y=\frac{20+3\omega}{17},
$$
$$
\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2,\quad u=\kappa^N,\quad N\in4\mathbf Z_{>0}.
\tag{1}
$$
物理原输入按 $(\xi_1,\xi_2,\xi_3,x,c,d)$ 排列。原行是
$$
\begin{aligned}
Y&=\delta\xi_1+2\delta\xi_2+(3+\omega)\xi_3+(2-\omega)x+c+2d,\\
W&=\delta\xi_1+2\delta\xi_2+(3+\omega)\xi_3+(2-\omega)x+3\delta c+4d,\\
t&=(\xi_1-\omega^2\xi_3+\omega x)/\delta-c,\qquad
P=W+at,\qquad Z_0=P-b_YY.
\end{aligned}
\tag{2}
$$
原观察三维 $\mathcal V=\operatorname{span}(Y,P,t)$ 的正交补为 C、$H_1$、J，
q 只依这三条隐藏行。沿 R786 更正后的规范，
$$
N(C)=1,\quad N(H_1)=7,\quad N(J)=72/7.
$$
三条彼此正交；全部纯 C 平均继续保留。

用 R789 的真实行
$$
y^\circ=Y-\frac{\alpha}{36}W,\qquad
z^\circ=Z_0-\frac4{17}W,\qquad
t^\circ=t+\frac{\bar a}{36}W=\frac{V_t}{36}.
\tag{3}
$$
它们都垂直于 W，且
$$
b_Yy^\circ+z^\circ=a t^\circ,\qquad
N(z^\circ)=\frac{3744}{289}.
\tag{4}
$$
但 $17z^\circ$ 并非这里最小的标准整呈示。由 (2) 直接得到
$$
\boxed{
L_z=\frac{17\delta}{2}z^\circ
=(19+30\omega,\ 21+9\omega,\ -13-3\omega,\
 -32-33\omega,\ -23-10\omega,\ 12+15\omega),
}
\tag{5}
$$
$$
\boxed{N(L_z)=2808=8\cdot27\cdot13.}
\tag{6}
$$
例如六项范数依次为
$691,333,139,1057,399,189$，和为2808。
这是原六个实际系数的整行，不是仅用一个抽象范数替代真实轴。
因 $17\delta/2$ 是当前 p-unit，(5) 与 $z^\circ$ 定义同一深度及同一个物理缩放。

## 2. Whole degree2808 的完整平方与全部 quarter 来源

(5) 的系数模2依次为
$$
1,\quad 1+\omega,\quad 1+\omega,\quad\omega,\quad1,\quad\omega.
\tag{7}
$$
六项都非零。原 odd sigma 在任一非零模二周期上的符号都是 $-1$，
所以六项乘积为 $+1$；偶周期上的乘积也为 $+1$。
原正交框架的 Gaussian 交叉项为零，故该轴给整个联合中的标准 even
$\mathcal S_{2808}$，没有遗漏的伙伴 flat 特征。

原 R520/R785 的射线与 R487 保留的13条件给
$$
g_\pi=\pi_0/\bar\pi_0\equiv11+8\omega\pmod{16},
\qquad g_\pi\equiv1\pmod{27\cdot13}.
\tag{8}
$$
于是
$$
\boxed{g_\pi^2\equiv1+2808\pmod{5616}.}
\tag{9}
$$
模16平方为9，模351为1，完整 CRT 给 (9)，并非仅模2808的1。

如 R785 对1512的证明，标准 even theta 中乘 $1+d$ 的 canonical
Heisenberg 额外中心为 $\exp(\pi i(2+d)vw)=1$。
取 $d=2808$，完整不可约性使 normalized $K_d^2$ 为 whole scalar。

令 $\gamma_{13}=4+\omega$，$N(\gamma_{13})=13$。真实非零锚
$$
\Theta(6\delta\gamma_{13}z),\qquad
N(6\delta\gamma_{13})=1404,
\tag{10}
$$
正属于 $\mathcal S_{2808}$。R471 的同一原 $\Theta=x\sigma^2$ 核为
$\beta=-\lambda$，其固定 p-unit CM 拉回保留这个绝对归一。
故锚上的 normalized 平方为1，准确支付
$$
\boxed{K_{2808,p}^2=I.}
\tag{11}
$$

此处还须保原 W-quarter。因为
$$
\langle L_z,W\rangle=0,
\tag{12}
$$
所有原 $\mathsf T_{\tau,W}^{72}e_0$、$\tau\in E[4]$，
沿 $L_z$ 的 flat 字符均平凡；canonical 中心的交叉项也恰为零。
所以这些实际来源全在同一个标准空间中。
(11) 逐项适用于原 $e_0,e_1,e_2$、$h_W$，及
$$
B_0=\frac{e_0-\omega h_W}{c_B},\quad B_1=K_WB_0,\quad
c_B=1-\omega^2 .
$$
原 C 平均不改变 (12)。

由于 q 与此轴正交，对原三态空间中任意固定 $\mu$，令 $\rho_\mu=q\mu$。
得到新的完整来源身份
$$
\boxed{
\rho_\mu|_{z^\circ\in p^{2h}}
=\lambda^{2h}(P_{z^\circ,\kappa^{2h}})_*\rho_\mu
\qquad(h\ge0).
}
\tag{13}
$$
所有伙伴保持。没有添加射线，亦没有把一层核猜成 scalar。

## 3. 保 W 的真正第三轴及独立偶深框架

置
$$
c=\frac{\alpha}{36},\qquad
c_z=-\frac{17\alpha}{468},\qquad
c_t=\frac{17\bar a}{468},
$$
$$
\boxed{
R_z=y^\circ-c_z z^\circ
=\frac{17}{468}(7Y+\alpha a t).
}
\tag{14}
$$
由 (3)、原 Gram 得
$$
R_z\perp W,z^\circ,\qquad
N(R_z)=\frac{2023}{234}=\frac{7\cdot17^2}{18\cdot13}.
\tag{15}
$$
整个反变换为
$$
\boxed{
\begin{aligned}
Y&=R_z+c_z z^\circ+cW,\\
t^\circ&=(b_Y/a)R_z+c_tz^\circ,\\
t&=(b_Y/a)R_z+c_tz^\circ-\bar aW/36,\\
P&=b_YR_z+a c_tz^\circ+29W/36 .
\end{aligned}}
\tag{16}
$$
因此 $(W,z^\circ,R_z)$ 是同一原 $\mathcal V$ 的正交框架，Gram 行列式为8064。
所有所用变基在当前 p 可逆，不另扩大或缩小原深格。

R785 已付整个 $\mathcal V$ 的偶深 $\lambda^{6h}$ 核及 W 的偶深
$\lambda^{2h}$ 核。将这些完整整像与 (13) 比较，逐个约消
W、$z^\circ$ 的可逆正交推前，得到
$$
\boxed{
\rho_\mu|_{R_z\in p^{2h}}
=\lambda^{2h}(P_{R_z,\kappa^{2h}})_*\rho_\mu.
}
\tag{17}
$$
这里 q 不变；这是原三态来源上的身份，不声称某个新的巨大 whole theta
空间在一层为 scalar。

对任意偶数 $L,r\ge0$，两轴实际交换，所以
$$
M_{L,r}=P_{z^\circ,\kappa^L}P_{R_z,\kappa^r},
$$
$$
\boxed{
\rho_\mu|_{\{z^\circ\in p^L,\ R_z\in p^r\}}
=\lambda^{L+r}(M_{L,r})_*\rho_\mu .
}
\tag{18}
$$
W、J、C、$H_1$ 及 q 在 (18) 中逐点不变。
任意附加门与观察都按这个明确的 M 转置；不预设它固定 Y 或 E。

## 4. D° 的完整双返回与额外 Y-unit

R789 的固定 W 返回帽是
$$
\mathcal D^\circ=
\{y^\circ\ {\rm unit},\,J,z^\circ\in p^N,\
                  u_JJ+u_Zz^\circ\notin p^n\},
$$
$$
u_J=\frac{7(4+9\omega)}{72},\qquad
u_Z=-\frac{68+33\omega}{144}.
\tag{19}
$$
因为 $z^\circ\in p^N$，其第一条件准确等价于 $R_z$-unit。

记 $\widetilde\Phi_N(u)$ 为 R786(17) 的同一个完整多项式。
它包含原五个次数块 $6,12,18,24,30$、六个 $\zeta$、
全部 $E_c$ 次数逆及 M-unit 第二项。
R786(18) 的四输出身份是
$$
\int_{J\in p^N}f(Y,P,t,J)q\,d\mu
=\lambda^N\beta^N
 \int f(Y,P,t,uJ)\widetilde\Phi_N(u)\,d\mu .
\tag{20}
$$
此处不重新适配 $\widehat P_{d,N}$，也不将它的参数改成辅助有限域值。

先用 (20)，再用 (13)。$\widetilde\Phi_N$ 只依原三个隐藏行，
所以第二步真正固定它。令
$$
\mathcal B_{n-N}=
\{R_z\ {\rm unit},\quad u_JJ+u_Zz^\circ\notin p^{\,n-N}\},
\qquad
Q_{z,u}=P_{z^\circ,u}.
\tag{21}
$$
对任意完整连续 $f(Y,P,t,J)$，准确得到
$$
\boxed{
\int_{\mathcal D^\circ} f(Y,P,t,J)q\,d\mu
=\lambda^{2N}\beta^N
 \int_{\mathcal B_{n-N}}
 f\bigl((Y,P,t)\circ Q_{z,u},uJ\bigr)
                       \widetilde\Phi_N(u)\,d\mu .
}
\tag{22}
$$
原失败门经过两步依次为
$u_JuJ+u_Zz^\circ\notin p^n$、
$u(u_JJ+u_Zz^\circ)\notin p^n$；
因此 (21) 保原整个 $n-N$ 层，而不是裸 unit 门。
原 $n=N+300$ 时，这就是一个固定的模 $p^{300}$ 伙伴条件。

尤其对**同一个原 W 观察**，因 $Q_{z,u}$ 固定 W，
$$
\boxed{
\int_{\mathcal D^\circ} f_w(W)q\,d\mu
=\lambda^{2N}\beta^N
 \int_{\mathcal B_{300}}f_w(W)\widetilde\Phi_N(u)\,d\mu
\quad(n=N+300).
}
\tag{23}
$$
这是真正同观察的有限来源返回。

若原测试另有 Y-unit，不能从 (23) 补猜其作用。
实际返回的 Y 是
$$
Y_{\rm ret}=R_z+cW+u c_z z^\circ.
\tag{24}
$$
其 unit 条件准确为 $R_z+cW$-unit，但完整 Mellin 权仍为
$$
\boxed{
f_w(Y_{\rm ret})
=1_{R_z+cW\ {\rm unit}}\,
 \langle R_z+cW\rangle^{d_pw}
 \left\langle1+\frac{u c_z z^\circ}{R_z+cW}\right\rangle^{d_pw}.
}
\tag{25}
$$
最后的对数项不能因 unit cut 稳定而删掉。
同样，原 $t^\circ$ 分母完整返回为
$(b_Y/a)R_z+u c_tz^\circ$，它在 (21) 上为单位。
所以 R789 的全质量与附 Y-unit 质量仍是两个不同的固定域积分。

(23) 右边的两个门、$\widetilde\Phi_N$ 全部与 W 正交。
原有限 p-Fourier 平移和正阶隐藏 jets 不移动第一 W 因子；
因此它的完整 W 来源仍在原 principal $\mathcal S_{72}$ 十三维空间
$$
\mathcal S_{72}^{(0)}
=\operatorname{span}\{\sigma^{72}x^{36-3j}:0\le j\le12\}.
\tag{26}
$$
这里的 x 是原 Weierstrass 坐标，固定角型由原全六角作用给出。
该来源由同一有限门上的 W 正矩阶 $0,6,\ldots,72$ 完全决定。
系数可以保原有限伙伴 torsion；没有把它猜成 T 线或由质量给中央非零。
若附 (25)，第一 W 方向另有显示的 mod-p gate，不能再直接称为裸十三维来源。

## 5. 物理 E 在这个框架中的完整 J 截距

原 E 身份为
$$
E=e_ZZ_0+h_0t+e_JJ,\quad
e_Z=-17(25+48\omega)/144,\quad
h_0=17+3\omega,\quad e_J=-1841/72 .
$$
由 (16)，准确为
$$
\boxed{
E=e_RR_z+e_zz^\circ+e_JJ,\qquad
e_R=\frac{h_0b_Y}{a},\quad
e_z=-\frac{289(25+48\omega)}{1872}.
}
\tag{27}
$$
显示的系数均是原 p-unit。特别 (18) 给
$$
E\circ M_{L,r}=e_R\kappa^rR_z+e_z\kappa^Lz^\circ+e_JJ.
\tag{28}
$$
若 $L,r\ge N$，物理 E 深/浅在返回后准确等于 J 深/浅。
另一方面，在整像上定义的**另一个 E 门**是
$$
E_{L,r}^{[-]}=E\circ M_{L,r}^{-1}
=e_R\kappa^{-r}R_z+e_z\kappa^{-L}z^\circ+e_JJ .
\tag{29}
$$
它一般不等于 E；J 的截距始终未缩放。
单用 $z^\circ$ 返回时同理有
$E\circ P_{z^\circ,\kappa^{-L}}
=E+e_z(\kappa^{-L}-1)z^\circ$。

令 $J^+=\{J\in p^N\}$、$J^-=\{J\notin p^N\}$，
$E^\pm$ 及 $(E_{L,r}^{[-]})^\pm$ 取同样的深 N/浅补约定。
这里的浅是全部不深 N，并不只指单位。

## 6. 第四块中的两条完整 J/E 行：同一个 W 观察

对偶数 $L,r\ge N$，定义四个真实域
$$
\boxed{
\mathcal A_{\epsilon,\delta}(L,r)=
\{z^\circ\in p^L,\ R_z\in p^r,\
                       E^\epsilon,\ (E_{L,r}^{[-]})^\delta\},
\qquad \epsilon,\delta\in\{+,-\}.
}
\tag{30}
$$
由 (28)，在这个整像上 $E^\epsilon$ 准确等于 $J^\epsilon$。
对任意完整连续测试 f，(18) 给全来源身份
$$
\boxed{
\int_{\mathcal A_{\epsilon,\delta}}
          f\circ M_{L,r}^{-1}\,q\,d\mu
=\lambda^{L+r}\int_{J^\epsilon,E^\delta}f\,q\,d\mu.
}
\tag{31}
$$
两种 E 条件的来源不同，(31) 一项也未省略。

现在始终用**原物理 W**：
$$
A_{\epsilon,\delta}^{\,i}(w)
=\int_{\mathcal A_{\epsilon,\delta}}f_w(W)q\,dB_i,
\qquad i=0,1 .
\tag{32}
$$
因为 W 被 M 固定，(31) 没有移动 (32) 的观察。记
$$
F_i^\epsilon(w)=
\int f_w(W)\,d\mathfrak F_{B_i,N}^\epsilon
=\int_{J^\epsilon}f_w(W)q\,dB_i,
\qquad T_B(w)=\frac{6\delta}{c_B}J_T(w).
$$
则这张完整表的行和、列和分别为
$$
\boxed{
\begin{array}{c|cc|c}
&\delta=+&\delta=-&\text{行和}\\ \hline
\epsilon=+&A_{++}^{\,i}&A_{+-}^{\,i}
 &\lambda^{L+r}F_i^+\\
\epsilon=-&A_{-+}^{\,i}&A_{--}^{\,i}
 &\lambda^{L+r}F_i^-\\ \hline
\text{列和}&\lambda^{L+r+2N}T_B
 &\lambda^{L+r}(\beta^N-\lambda^{2N})T_B
 &\lambda^{L+r}\beta^NT_B
\end{array}}
\tag{33}
$$
列式正是 R786(29) 的原 E 深/浅全 W 来源；
行式正是 R786(19) 的 J 深/浅有限来源。
它们是整个 Mellin 函数等式，包含全部质量，不只中央导数。

这张表的下行确实进入 R789 的第四块。
在 (32) 的支撑上 W 为单位，而 $z^\circ\in p^L$、$L\ge1$，故
$$
Z_0=z^\circ+4W/17\ {\rm unit}.
\tag{34}
$$
原帽 $\mathcal H$ 需要 $Z_0\in p^N$，因此完全失败。
对 $\epsilon=-$，物理 E 同时不深 N。
所以对任意 $m\ge1$，
$$
\boxed{
\mathcal A_{-,\delta}(L,r)\cap\{W\ {\rm unit}\}
\subset
(\mathcal E^c\setminus\mathcal K)\cap\{W\notin p^m\}.
}
\tag{35}
$$
右侧正是 R789 恒等来源 $s=1$ 的第四格，且 (35) 保原 q、两个 E 门和完整 W-unit。
并未把它认成整个第四块；未命中的域仍完整存在。

若 $J_T'(0)=0$，(33) 合法给
$$
(A_{-+}^{\,i})'(0)=-(A_{++}^{\,i})'(0),\qquad
(A_{--}^{\,i})'(0)=-(A_{+-}^{\,i})'(0).
\tag{36}
$$
它不令这四个值分别为零。两个下格之和是
$\lambda^{L+r}(F_i^-)'(0)$，不是原无门 $J_T'$。
R791 的两个独立点值使用 $t/Y$，不能代替此处的 $(F_i^\pm)'(0)$。

## 7. 这些四格的 J 来源可由同一有限条件模型读取

(31) 右边的 $J^+,E^\delta$ 交域不需要引入任意条件测度。
R786(20) 保留 J 作为第四输出，故准确为
$$
\boxed{
\int_{J^+,E^\delta} f(Y,P,t,J)q\,d\mu
=\lambda^N\beta^N
 \int_{\{E_{\mathcal V}+e_JuJ\}^{\delta}}
 f(Y,P,t,uJ)\widetilde\Phi_N(u)\,d\mu,
}
\tag{37}
$$
其中 $E_{\mathcal V}=e_RR_z+e_zz^\circ$，深/浅阈值仍是 N。
$J^-,E^\delta$ 来源则是整个 $E^\delta$ 来源减去 (37)，不是另选的同质量来源。
对 f=$f_w(W)$，整个 $E^\delta$ 项由 (33) 已知。

因此 (33) 中的四格以同一个实际 $\widetilde\Phi_N$ 和 (37) 的显示 finite gate
完全指定。保 C、$H_1$ 的其它测试时，仍须按 R786 的六支
$P_{L_\zeta,u}$、$P_{M_\zeta,\kappa}$ 分别转置；
本文没有从三输出推前倒造这些额外伙伴。

若写 $X_i(w)=\lambda^{-L-r}A_{++}^{\,i}(w)$，则表中四个归一元素准确为
$$
\boxed{
\begin{pmatrix}
X_i&F_i^+-X_i\\
\lambda^{2N}T_B-X_i&
(\beta^N-\lambda^{2N})T_B-F_i^++X_i
\end{pmatrix}.}
\tag{38}
$$
这是同一来源、同一观察的完整有限关系；唯一的交域项 $X_i$ 由 (37) 给出。
它不是由总质量或有限维数计数选出的自由数。

## 8. 原第三中央在同一个词上的准确范围

同一个 M 也可运输 Y 观察，但该观察必须写成
$$
\boxed{
Y_{L,r}^{[-]}=Y\circ M_{L,r}^{-1}
=\kappa^{-r}R_z+c_z\kappa^{-L}z^\circ+cW.
}
\tag{39}
$$
它只在 (30) 的整像上使用。对 $i=1$，(31) 按 $\epsilon$ 求和、取
$f=f_w(Y)$，给整个 E 深列
$$
\boxed{
\sum_{\epsilon=\pm}
 \int_{\mathcal A_{\epsilon,+}}
            f_w(Y_{L,r}^{[-]})q\,dB_1
=
\frac{\lambda^{L+r+2N}}{c_B}
\left(\langle2\rangle^{-d_pw}J_U(w)
             +\frac{\delta\omega^2}{2}J_S(w)\right).
}
\tag{40}
$$
这是原第三来源 U 与原 S 的已付完整行，不添加一个辅助中央零。
对 B0 的相应列及 E 浅 Y 列，严格使用 R780/R786 的原表：
B0 两列整条为零；B1 的 E 浅列保原 $\Xi$、reference 和全部外谱。
(40) 导数的尺度项只因整个 $J_U(0)=0$ 才消去，不能逐格删除质量。

要将 (40) 用到 (35) 的第四格，必须分开
$$
\mathcal A_{-,+}\cap\{W\ {\rm unit}\},
\qquad
\mathcal A_{-,+}\cap\{W\in p\}.
\tag{41}
$$
第一部分在第四格，第二部分不在 (35) 中，仍为完整补域。
在整个两轴深域上，物理 $Y$-unit 等价于 W-unit，
因为 $Y=R_z+c_zz^\circ+cW$ 且 $c$ 为单位；
但 $Y_{L,r}^{[-]}$-unit并不等价于它们。
其完整条件是 (39) 的显示行。
所以不能把 (40) 的第二部分按物理 Y 深误判为零。

(33) 与 (40) 因而共享真正的原域和两态，却保持两个准确的观察。
这是可继续联立的接口；并未将逆 Y 的原第三中央直接赋给 (33) 的单格 W 值。

## 9. 与 R789 的固定观察外部及全部 CM 分支的关系

本篇 (35) 控制的是第四格的实际原 W 行。
R789 的非零有限差使用原观察 $zP-at$，并在 P 返回后才变成原 W。
在 M 返回下，该固定观察准确为
$$
(zP-at)\circ M_{L,r}
=(z-1)\bigl(b_Y\kappa^rR_z+a c_t\kappa^Lz^\circ\bigr)
                         +\frac{29z+7}{36}W.
\tag{42}
$$
因此不能把 (33) 的原 W 列直接替换成 (42) 后仍称纯 $J_T$。
若使用这个观察，(31)、(37) 仍逐字成立，但列须保完整
$zP-at$ 的 E 条件 Mellin 来源。这正是当前还需控制的同来源余项。

本篇新核 (13)、(17) 对原完整三态和同 q 已证明。
$z^\circ$ 不垂直于第一 Y 轴，所以未声称它与 R784 的
$\mathcal Q_\alpha$ 全部 CM 平移免费交换。
R789 的原216分支、所有 $1/\alpha$、尺度-log 与其余215外部继续原样保留。
若把新返回施于这些来源，须另逐个支付它们的 flat 标签并同时运输
$z^\circ\circ D_s^{-1}$；不能只因 (35) 位于某一物理四单位集而换来源。

## 10. 已得结论与尚未关闭的门

本篇新支付的是：

1. 原 $z^\circ$ 的真实 degree2808 整轴、whole 平方及所有 quarter 三态偶深核；
   同时得到保 W 的独立 $(z^\circ,R_z)$ 偶深框架。
2. R789 固定帽的完整 J/$z^\circ$ 双返回 (22)，包括原 U 失败、两种不同局部质量及 (25) 的真实 Y Mellin 修正。
3. 原第四格中的实际两门表 (33)：同 W 观察的两列准确是原 T，两个下格确属第四块；
   其 J 条件来源全由 (37) 指定。
4. 同一个真实词给 (40) 的原 U/S 行，但 (39)、(41) 的逆观察和 W 深补域不能省略。

这些关系未与三个原中央同时为零发生矛盾。
新的表不是稳定族的重复计数，也不从某个点对数非零给完整 W-log 添非零。
实际剩余是 (37) 的完整交域 Mellin、(41) 的补域，
以及当采用 R789 非零固定观察时 (42) 引入的同来源列。
它们均已明确到原有限源和真实门。

## 依赖及执行范围

- [R471](R471-original-six-sigma-normtwo-factor-and-complete-input-carry.md)：原 Theta 绝对核。
- [R487](R487-original-cm-mixed-tubes-and-common-core-reference-carry.md)、[R520](R520-third-common-companion-even-core-and-true-three-input-source.md)：原13条件和完整dyadic/27射线。
- [R734](R734-joint-paid-tests-and-complete-type-five-arithmetic-plane.md)：同一个最终 q。
- [R777](R777-original-b-sector-p-t-core-and-complete-central-renewal.md)、[R780](R780-original-third-central-b-state-and-true-w-deep-return.md)：两态及原三算术来源表。
- [R785](R785-original-three-state-even-frames-and-exact-e-gate.md)：原共享三维偶深、全部quarter中心及 E 截距。
- [R786](R786-original-j-depth-three-output-and-native-e-exteriors.md)：同一 $\widetilde\Phi_N$、完整 J 四输出、E 深浅原 Mellin 行。
- [R789](R789-fixed-cm-hat-germs-and-nonzero-native-exterior-differences.md)：固定返回帽、四格与原非零外部差。
- [R791](R791-original-j-depth-negative-moments-and-two-e-sectors.md)：原 $t/Y$ 两 J 值的准确范围；本文不将其换成 W 中央值。

本文没有执行新数值计算、扫描或生成可重算数据。整行、Norm、中心、全部域和常数由显示公式直接证明。
