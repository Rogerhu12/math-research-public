# R357：原双辅助的和差四项联合式及单相位完整边界消元

日期：2026-11-13。**状态：已证明。** 将 R350 的实际两个辅助改为
$P=\delta(L_r+L_s)$、$Q=\delta(L_r-L_s)$，完整二维来源有四项真实乘积测度分解。
其全部系数为 $1,12b,4b,-8b^2$；证明由原 $\mathcal O(8O)\boxtimes\mathcal O(4O)$
六维空间与 R350 的 CM 截线给出，涵盖全部辅助权。
两个新坐标分别作 $\mu_6$ 平均后，联合恰为两条固定低次来源的独立乘积。
因此 R339 原叶域所在的 $\zeta=1$ 碰撞管及其双非单位边界得到完整消元。
原叶变量的额外独立深度限制仍完整保留，不由此宣称原中央非零。

## 1. 原对象、坐标和已付身份

沿用 R350 的全部原规范：
$$
E:y^2=x^3+b,\quad b=17,\quad
\omega^2+\omega+1=0,\quad\delta=1+2\omega,\quad
\gamma=3+\omega ,
$$
$$
\boldsymbol c=(1,2,\delta,2\delta,\gamma,\bar\gamma)^t,\qquad
S=-\frac1{84}\prod_i\sigma(c_i z)=z^6+\cdots.
\tag{1}
$$
$\Theta=x\sigma^2$、$C=y\sigma^3$、$X=x^3$，且
$x=z^{-2}+\cdots$、$y=-z^{-3}+\cdots$。
原相交三元组和辅助为
$$
\boldsymbol r=(1,\omega^2,1,0,0,0)^t,\quad
\boldsymbol s=(1,0,0,-\omega^2,-\omega,0)^t,
$$
$$
Y=\boldsymbol c^t\boldsymbol X,\qquad
L_r=\delta^{-1}\boldsymbol r^*\boldsymbol X,\qquad
L_s=\delta^{-1}\boldsymbol s^*\boldsymbol X.
\tag{2}
$$
R350 已证明仅对两个辅助**同时**平均的完整联合身份
$$
\mathsf P_\Delta(Y,L_r,L_s)_*\eta_6
           =\nu_S\otimes\Xi_\Delta,\qquad
\eta_6=-\nu_\sigma^{\otimes6}/84.
\tag{3}
$$
$\Xi_\Delta$ 的变换是
$$
\psi_\Delta(v,w)
=[z^6]\left\{-\frac1{84}
 \prod_i\sigma\left(c_i z+
              \frac{\bar r_i v+\bar s_i w}{\delta}\right)\right\}.
\tag{4}
$$
原点质量为一，$\psi_\Delta(\xi v,\xi w)=\psi_\Delta(v,w)$。
其六条完整相位截线为
$$
\begin{array}{c|c}
\zeta&D_\zeta(t)=\psi_\Delta(\delta t,-\zeta\delta t)\\ \hline
1&\Theta(t)^2\\
-1&\Theta(t)\Theta(\delta t)\\
\omega,\omega^2&-\Theta(t)^2C(t)\\
-\omega,-\omega^2&-\Theta(t)C(t).
\end{array}
\tag{5}
$$
这些是完整整个函数身份，不是低阶拟合。

定义本篇的**真实**和差输出
$$
\boxed{
P=\delta(L_r+L_s),\qquad Q=\delta(L_r-L_s).
}
\tag{6}
$$
对应矩阵的行列式为 $-2\delta^2=6$。
对每个本篇普通素数 $p>7$，它在 $\mathbf Z_p$ 上可逆，准确逆式是
$$
L_r=\frac{P+Q}{2\delta},\qquad
L_s=\frac{P-Q}{2\delta}.
\tag{7}
$$
变换变量相应为
$$
H(t,u)=\psi_\Delta\bigl(\delta(t+u),\delta(t-u)\bigr).
\tag{8}
$$

## 2. 真正的有限 theta 空间

在 (4)、(8) 中，六个 sigma 的自变量为
$$
c_i z+d_{+,i}t+d_{-,i}u,\qquad
\boldsymbol d_+=\overline{\boldsymbol r}+\overline{\boldsymbol s},
\quad
\boldsymbol d_-=\overline{\boldsymbol r}-\overline{\boldsymbol s}.
\tag{9}
$$
准确的 Hermitian 关系是
$$
\|\boldsymbol d_+\|^2=8,\quad
\|\boldsymbol d_-\|^2=4,\quad
\boldsymbol d_+^*\boldsymbol d_-=0,\quad
\boldsymbol d_\pm^*\boldsymbol c=0.
\tag{10}
$$
因此全部交叉 Gaussian 消失。
用 R350 已付的原 CM sigma 线丛规范，$H$ 真正属于
$$
H^0(E,\mathcal O(8O))\otimes H^0(E,\mathcal O(4O)),
\tag{11}
$$
其中第一因子为 $t$、第二因子为 $u$。
提取 $[z^6]$ 没有留下随 $t,u$ 变化的准周期连接项。
由 (4)，$H(\xi t,\xi u)=H(t,u)$。

实际 sigma 基的 $\mu_6$ 型为
$\sigma^N x^a y^e$ 的 $N-2a-3e$，$2a+3e\le N$。
所以 (11) 中同时 $\mu_6$ 不变的完整空间为以下六维：
$$
\begin{aligned}
&\Theta(t)^4\Theta(u)^2,\qquad
  [\sigma^6\Theta](t)\Theta(u)^2,\\
&[\sigma^8y](t)[\sigma^4y](u),\qquad
  [\sigma^4\Theta^2](t)[\sigma^2\Theta](u),\\
&[\sigma^2\Theta^3](t)\sigma(u)^4,\qquad
  \sigma(t)^8\sigma(u)^4.
\end{aligned}
\tag{12}
$$
这些是六个真实独立基列；没有把原空间换成任意角函数环境。

由 (5)，
$$
H(t,0)=\Theta(t)\Theta(\delta t)
      =\Theta(t)^4+4b\sigma(t)^6\Theta(t),\qquad
H(0,u)=\Theta(u)^2.
\tag{13}
$$
故 (12) 的前两列系数准确为 $1,4b$。

## 3. 原 CM 截线杀掉唯一奇列

(5) 与 $-2\omega,-2\omega^2\in2\mu_6$ 给
$$
\boxed{
H(t,\delta t)=H(t,-\delta t)
                       =-\Theta(2t)C(2t).
}
\tag{14}
$$
例如 $\zeta=-\omega^2$ 时，令 (5) 的变量为 $-2\omega^2t$，
便有 $(1-\zeta)v/2=t$、$(1+\zeta)v/2=\delta t$；
所有单位相位由所列原 $\mu_6$ 不变性准确支付。
另一相位给负号截线。

(12) 中只有
$[\sigma^8y](t)[\sigma^4y](u)$ 对 $u\mapsto-u$ 为奇；
它在 $u=\delta t$ 上不是零函数。
因此 (14) 迫其系数准确为零。

同理，由 $\zeta=\omega,\omega^2$ 两条原截线，
$$
\boxed{
H(\delta t,t)=H(\delta t,-t)
                       =-\Theta(2t)^2C(2t).
}
\tag{15}
$$
这两条完整 CM 关系足以确定其余三列。

## 4. 四项整个函数恒等式

现在写
$$
\begin{aligned}
H(t,u)={}&
 [\Theta\Theta_\delta](t)\Theta(u)^2\\
&+a b[\sigma^4\Theta^2](t)[\sigma^2\Theta](u)\\
&+d b[\sigma^2\Theta^3](t)\sigma(u)^4
 +e b^2\sigma(t)^8\sigma(u)^4 .
\end{aligned}
\tag{16}
$$
其中 $\Theta_\delta(t)=\Theta(\delta t)$。

全部计算只使用原 CM 和倍点身份：
$$
\sigma(\delta t)=\delta x\sigma^3,\qquad
x(\delta t)=-\frac{X+4b}{3x^2},\qquad
\Theta_\delta=\sigma^6(X+4b),
\tag{17}
$$
$$
\sigma(2t)=-2y\sigma^4,\qquad
x(2t)=\frac{x(X-8b)}{4(X+b)},\qquad
y(2t)=\frac{X^2+20bX-8b^2}{8y^3}.
\tag{18}
$$
尤其
$$
\Theta(2t)=\sigma^8x(X-8b),\qquad
C(2t)=-\sigma^{12}(X^2+20bX-8b^2).
\tag{19}
$$

将 (16) 的 $u$ 置为 $\delta t$，除去共同非零亚纯因子
$\sigma^{20}x$。整个函数身份 (14) 等价为多项式恒等式
$$
(X+4b)^3-3abX(X+4b)+9dbX^2+9eb^2X
       =(X-8b)(X^2+20bX-8b^2).
\tag{20}
$$
比较 $bX^2,b^2X$ 的系数，得到
$$
a=3d,\qquad e=4d-24.
\tag{21}
$$

将 (16) 的第一变量置为 $\delta t$，除去 $\sigma^{28}x^2$。
由 (15)、(17)–(19)，得到
$$
\begin{aligned}
&(X+4b)^4-108bX^2(X+4b)
  +9abX(X+4b)^2\\
&\hspace{20mm}-3db(X+4b)^3+81eb^2X^2\\
&\hspace{10mm}=(X-8b)^2(X^2+20bX-8b^2).
\end{aligned}
\tag{22}
$$
代入 (21) 后，比较 $bX^3$ 给 $-92+24d=4$。
所以
$$
\boxed{a=12,\qquad d=4,\qquad e=-8.}
\tag{23}
$$
其余系数也逐项相同：
两边的 $X^4,bX^3,b^2X^2,b^3X,b^4$ 系数为
$1,4,-264,1408,-512$。

因此得到全部权的实际整个身份
$$
\boxed{
\begin{aligned}
H(t,u)={}&
 [\Theta\Theta_\delta](t)\Theta(u)^2\\
&+12b[\sigma^4\Theta^2](t)[\sigma^2\Theta](u)\\
&+4b[\sigma^2\Theta^3](t)\sigma(u)^4
 -8b^2\sigma(t)^8\sigma(u)^4 .
\end{aligned}}
\tag{24}
$$
证明在真正的六维空间中使用完整 CM 截线，没有由有限 Taylor 系数外推。

## 5. 完整原联合测度与全部分型

以下短名仅表示已经明确的原整个函数：
$$
K=\Theta\Theta_\delta,\quad D=\Theta^2,\quad
F=\sigma^4\Theta^2,\quad G=\sigma^2\Theta,\quad
B=\sigma^2\Theta^3,\quad A=\sigma^4,\quad E=\sigma^8 .
\tag{25}
$$
每个 $\nu_T$ 都在同一个原 $\Omega$ frame 中，由所列正乘积的
**加法卷积**定义。它们整有界。
令 $\mathcal T(u,v)=(\delta(u+v),\delta(u-v))$。
整个 (24) 给真正的测度等式
$$
\boxed{
\mathcal T_*\Xi_\Delta
=\nu_K\otimes\nu_D
 +12b\,\nu_F\otimes\nu_G
 +4b\,\nu_B\otimes\nu_A
 -8b^2\,\nu_E\otimes\nu_A .
}
\tag{26}
$$
与原输出合并为
$$
\boxed{
\mathsf P_\Delta(Y,P,Q)_*\eta_6
=\nu_S\otimes
 \left(\nu_K\otimes\nu_D+12b\nu_F\otimes\nu_G
       +4b\nu_B\otimes\nu_A-8b^2\nu_E\otimes\nu_A\right).
}
\tag{27}
$$
坐标改变 (6) 与同时平均相容，故没有新的投影交换假设。

全部辅助分型、原点质量和最小阶如下：
$$
\begin{array}{c|c|c|c}
\text{来源}&\text{degree}&\mu_6\text{ 型}&\text{原点首项}\\ \hline
K&8&0&1\\
D&4&0&1\\
F&8&4&z^4\\
G&4&2&z^2\\
B&8&2&z^2\\
A&4&4&z^4\\
E&8&2&z^8
\end{array}
\tag{28}
$$
因此在 $P,Q$ 上**分别**投影到 $\mu_6$ 不变型时，
后三项准确消失，得到
$$
\boxed{
\mathsf P_{\mathrm{ind}}\mathcal T_*\Xi_\Delta
                         =\nu_K\otimes\nu_D.
}
\tag{29}
$$
这是原两个新辅助的完整独立乘积身份。
它与旧 $(L_r,L_s)$ 的相关性不冲突，因为 (6) 确实混合了两个坐标。

对任何在 $P,Q$ 上分别 $\mu_6$ 不变的有界连续函数 $h$，
(27)、(29) 在未平均的原核上给
$$
\boxed{
Y_*\{h(P,Q)\eta_6\}
                  =(\nu_K\otimes\nu_D)(h)\,\nu_S.
}
\tag{30}
$$
函数 $h$ 可以相关；不必是两个函数的乘积。
所有相加产生的单位/非单位输出域均由 (26) 完整保留。

## 6. 单相位碰撞管的边界完全算回两个深度质量

记
$$
k_a=\nu_K(p^a\mathbf Z_p),\qquad
d_a=\nu_D(p^a\mathbf Z_p),\qquad k_0=d_0=1 .
\tag{31}
$$
这些是两条**真实**固定来源的整个深度质量；
本篇不先猜测其新 core 标量。

对 $N\ge a\ge1$，由 (7) 和 $2\delta$ 为单位，
$$
\{L_r,L_s\in p^a,\ L_r-L_s\in p^N\}
                  =\{P\in p^a,\ Q\in p^N\}.
\tag{32}
$$
此域对新两坐标分别 $\mu_6$ 不变，所以 R350 的边界恰为
$$
\boxed{e_{1;a,N}=k_a d_N.}
\tag{33}
$$
特别实际双方单位相位管满足
$$
\{L_r,L_s\in\mathbf Z_p^\times,\ L_r-L_s\in p^N\}
                   =\{P\in\mathbf Z_p^\times,\ Q\in p^N\},
$$
故
$$
\boxed{q_{1,N}=(1-k_1)d_N.}
\tag{34}
$$
这完整消去了该相位的二维边界未知量。
没有删掉原 primitive-input carry；它现在由一个确定的低次测度式支付。

反相位同样准确为
$$
\boxed{
e_{-1;a,N}=k_Nd_a,\qquad
q_{-1,N}=(1-d_1)k_N.
}
\tag{35}
$$
这两条是本篇真正的新边界信息，不只是 R350 的递推换名。

结合原五输入收缩 $\Xi_\Delta=\Xi_\Delta^{\mathrm{prim}}
+t_p^5[\kappa,\kappa]_*\Xi_\Delta$，还准确得到
$$
\boxed{
e^{\mathrm{prim}}_{1;a,N}
 =k_ad_N-t_p^5k_{a-1}d_{N-1}.
}
\tag{36}
$$
特别
$$
e^{\mathrm{prim}}_{1;1,N}
 =k_1d_N-t_p^5d_{N-1}.
\tag{37}
$$
将它代入 R350(37)，恰恢复 (34)。
原双非单位 carry 没有被假定为小，而是被完整计算。

其余四个相位仍有明确的四项原积分，不能把 (33) 直接套用。
确切地，条件 $L_r-\zeta L_s\in p^N$ 在新坐标下为
$$
(1-\zeta)P+(1+\zeta)Q\in2\delta p^N\mathbf Z_p.
\tag{38}
$$
双方在 $p^a$ 等价于 $P,Q\in p^a$。
因此把 (38) 与 $P,Q\in p^a$ 的指标直接代入 (26)，就给全部
$e_{\zeta;a,N}$ 的四项原来源公式。
当 $\zeta\ne\pm1$ 时，该域通常不分别 $\mu_6$ 不变，后三项须保留。
本篇没有把旧六条相位的质量或非单位边界误当相等。

## 7. 完整 tame、尺度及中央公式

令 $d=p-1$，对任何原测度 $\nu_T$ 定义
$$
M_{T,\ell}(u)=
 \int_{\mathbf Z_p^\times}
       \omega_p(x)^\ell\langle x\rangle^{du}\,d\nu_T(x).
\tag{39}
$$
在 (27) 的已平均真实联合测度上，可测试任意三个 tame。
完整三变量 Mellin 为
$$
\begin{aligned}
J_{S,\ell_0}(u_0)\bigl\{&
 M_{K,\ell_1}(u_1)M_{D,\ell_2}(u_2)\\
&+12bM_{F,\ell_1}(u_1)M_{G,\ell_2}(u_2)\\
&+4bM_{B,\ell_1}(u_1)M_{A,\ell_2}(u_2)
 -8b^2M_{E,\ell_1}(u_1)M_{A,\ell_2}(u_2)\bigr\}.
\end{aligned}
\tag{40}
$$
这里出现乘积是因为 (26) 已经证明是**独立坐标的张量测度**，
不是把同一输出中一个 theta 乘积的 Mellin 擅自拆开。

在未平均原六输入核上，辅助测试需同时 $\mu_6$ 不变，
例如 $\ell_1+\ell_2\equiv0\pmod6$。
由 (28)，三个可能的非零辅助型分别为
$(0,0),(4,2),(2,4)$；原 principal 辅助分支恰只保第一项。
各自的全部正则权 $u_1,u_2$ 和其导数仍按 (40) 保留。

若改用未乘 $\delta$ 的和差
$U=L_r+L_s,V=L_r-L_s$，则完整辅助 Mellin 必乘
$$
\omega_p(\delta)^{-\ell_1-\ell_2}
             \langle\delta\rangle^{-d(u_1+u_2)} .
\tag{41}
$$
对其中任一个权求导，都保留相应的
$-d\log_p(\delta)$ 乘质量项。
若回到 $L_r,L_s$，必须使用 (7) 的
$(P+Q)/(2\delta),(P-Q)/(2\delta)$：
这时相加的非单位 carry 以及 $\log_p(2\delta)$ 都仍存在，
不能沿用 (40) 的独立坐标乘法式。

对原 $Y$ 的完整 principal 中央，$Y$ 没有缩放。
故 (34)、(35) 直接给
$$
\boxed{
J'_{\mathcal H_{1,N}}(0)=(1-k_1)d_NJ'_S(0),\qquad
J'_{\mathcal H_{-1,N}}(0)=(1-d_1)k_NJ'_S(0).
}
\tag{42}
$$
没有新的原点参考斜率被删除；右边只出现与原 Mellin 权无关的深度质量。

## 8. 与原叶深度域的实际关系

R350(40)–(49) 已在原范数三叶核 $\mathscr M_m$ 上写出
R339 的独立深度域 $\mathcal D_{\boldsymbol n}$、
相位管 $\mathcal H_{1,N}$ 和全部不交补域 $\mathcal E_j$。
对所有叶深度至少 $N$，仍有
$\mathcal D_{\boldsymbol n}\subset\mathcal H_{1,N}$。
将新 (34) 代入那个**同一原核**的完整中央等式，得到
$$
\boxed{
\mathcal L_p(\mathcal D_{\boldsymbol n})
+\mathcal L_p(\mathcal E_0)+\sum_j\mathcal L_p(\mathcal E_j)
                       =(1-k_1)d_NJ'_S(0).
}
\tag{43}
$$
相比 R350，本篇已经计算了右边碰撞管的全部双非单位边界：
它不再依赖一个未计算的二维 primitive-output 质量。

另一方面，$\mathcal E_j$ 中对原 $X_6$、各叶 $A_h,B_h$ 等变量的限制，
并非只由新 $P,Q$ 决定。
例如 R350 已给 $X_6$ 为单位而 $P$ 单位、$Q$ 任意深的真实补域。
所以 (29) 不会自动把每一 $\mathcal E_j$ 变成独立辅助域。
若原 $J'_S(0)=0$，(43) 仍保留这些补项对 R339 非零叶积分的完整补偿。

下一步可以在 (26) 的真实低次来源上支付 $k_a,d_a$ 的全部 core/相位，
并继续检验更多原域运输是否控制 (43) 的补项。
本篇已经完成的是同一原联合函数的有限分解和两个单相位边界的真实消元，
不是原固定曲线无穷中央非零的最终证明。

### 引用

- [R297：原 CM sigma 来源及倍点/norm3 规范](R297-jzero-actual-cm13-mass-kernel-cm7-product-and-angular-source.md)。
- [R316：原整测度与低次 core](R316-jzero-low-degree-original-cores-and-complete-four-factor-carry.md)。
- [R339：实际独立叶深度非零族](R339-original-normthree-depth-family-and-a-unit-negative-moment-coefficient.md)。
- [R344：重叠双辅助的真实挠点因子化](R344-overlapping-original-pair-full-torsion-factorization-and-contracting-kernel.md)。
- [R350：对角联合、六相位与完整叶补域](R350-original-diagonal-pair-six-phase-collision-and-leaf-complement.md)。
