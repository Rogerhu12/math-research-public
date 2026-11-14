# R476 — 原 Xi 与 norm-two 来源的完整桥及整八维联合基

日期：2026-11-14。**状态：已证明。** 本篇把 R465 原六 sigma 的
第二态接到 R471 的同一个 norm-two 来源 $W_*$。完整的 $D_{33}=-1$
块为七维 $W_*$ 轨道加一条已识别的秩零参考线。等式在全部二十三个
theta 坐标中成立；相应八维基的系数提取在当前普通射线上整。
因此原五个伴随可以逐个保留，不能把它们各自的函数换成边际常数。
本篇还给这整个块的实际新增伴随提升。混合第一输出的原 $T$ 管仍须
逐支运输；本篇不赋六个外谱或秩零参考的中央导数为零。

## 1. 原规范、完整空间与实际 CM19

沿用 R465、R466、R470 的同一 $E_b$、reduced sigma 和普通周期，
最终取 $b=17$。记
$$
\delta^2=-3,\qquad \omega=\frac{-1+\delta}{2},\qquad
\gamma_7=\frac{5+\delta}{2},\qquad \gamma_{19}=4+\delta,
$$
$$
N_7=\mathscr M_{\gamma_7}/\gamma_7,\qquad
N_{19}=\mathscr M_{\gamma_{19}}/\gamma_{19}.
\tag{1}
$$
所有 $\mathscr M$ 都是原 canonical theta lift 的完整 CM 纤维迹。
本篇计算的整个 principal 空间为
$$
\mathcal V_{136}
=\sigma_b^{136}x_b^2
 \operatorname{span}_{K}\{1,X,\ldots,X^{22}\},\qquad
X=x_b^3,\quad K=\mathbf Q(\delta).
\tag{2}
$$
质量是 (2) 的 $X^{22}$ 坐标。对于质量不为零的函数，$X^{21}$
坐标本身不是 Taylor 的 $z^6$ 系数；本篇不混用这两个读数。

R466 已给完整 $N_7$ 及 positive 三次角色块的 $N_{19}$。
本篇对 (2) 的**全部二十三列**计算实际 $N_{19}$，得到
$$
N_7^{18}=I,\qquad [N_7,N_{19}]=0,\qquad
D:=\omega^{-1}N_{19}N_7^{-2},\qquad D^2=I.
\tag{3}
$$
这里 $N_7^{-2}=N_7^{16}$，$D$ 是同一个 $D_{33}$，而不是只在
五条算术线上重新规定的符号。准确维数为
$$
\dim\ker(D-I)=15,\qquad \dim\ker(D+I)=8.
\tag{4}
$$
尤其
$$
\boxed{D_-:=\frac{I-D}{2}
\quad\Longrightarrow\quad N_7^9D_-=D_-.}
\tag{5}
$$

### 1.1 为什么完整矩阵是全函数证明

完整证书采用 R466 的同一个 degree19 除法多项式
$$
q_\gamma(x)=\frac{\sigma(\gamma z)}
                  {\gamma\sigma(z)^{19}},\qquad \gamma=4+\delta.
$$
其单项式只可能为 $x^9,x^6,x^3,1$。原
$(\log\sigma)''=-x$ 和 $x''=6x^2$ 决定这四个系数；
随后使用由该除法多项式给出的真实 $x(\gamma z)$ 有理映射。
在每个 $x(\gamma z)=a$ 的 degree19 纤维商环内，canonical
frame 与全部输入多项式相乘，按 Newton trace 取完整纤维迹，
没有选取一个逆像。

取 $a=1,\ldots,23$。脚本在 $K[x]/(f_a)$ 中实际验证所需分母的逆，
然后精确反演 $(a^{3j})_{a=1,\ldots,23;\,j=0,\ldots,22}$。
该矩阵是不同 $a^3$ 上的 Vandermonde 矩阵。CM 迹先已知保持 (2)，
所以这二十三个精确取值唯一决定整个函数的二十三个系数。
(3)–(5) 都是由这些完整矩阵的有理恒等式得到，不是对变化的
普通素数作抽样。

文件为：

- [完整 degree136 CM19 纤维脚本](../scripts/check-original-degree136-cm19-exact.py)；
- [完整 CM19 与 D33 矩阵](../notes/2026-11-14-theta-degree136-cm19-exact.json)；
- [本篇完整桥与整提取证书](../scripts/check-r476-full-xi-wstar-bridge.py)；
- [本篇全部有理系数](../scripts/check-r476-full-xi-wstar-bridge.json)。

## 2. 八维块中的七维真来源与正确参考线

令
$$
E_1=\frac1{18}\sum_{j=0}^{17}N_7^j,\qquad
\mathcal Z=(I-E_1)D_-.
\tag{6}
$$
由完整矩阵，
$$
\operatorname{rank}(E_1D_-)=1,\qquad
\operatorname{rank}\mathcal Z=7.
\tag{7}
$$

保 R466、R471 的原组合
$$
W_*=101W_{13}-64W_{15}
=-\frac{111}{280}\,
 \sigma(z)^4\sigma(2z)\sigma(8z)\Theta(4z)^2.
\tag{8}
$$
这是真实六 sigma 与两个 Theta 的加法卷积来源。它的完整
CM7 轨道满足
$$
D_-W_*=W_*,\qquad E_1W_*=0,\qquad
\operatorname{rank}\{W_*,N_7W_*,\ldots,N_7^6W_*\}=7.
\tag{9}
$$
其准确最小多项式是
$$
(t-\omega^2)(t^6+t^3+1).
\tag{10}
$$
因此一条新算术线以外还有六个真实外谱方向；不能删掉后一个因子。

令 $A_{136,b}$ 是 R470 的原 R414 负来源。定义
$$
\boxed{H_{{\rm ref},b}
=-120960\,b\,E_1D_-A_{136,b}.}
\tag{11}
$$
完整坐标给
$$
H_{\rm ref}(0)=1,\quad
N_7H_{\rm ref}=H_{\rm ref},\quad
N_{19}H_{\rm ref}=-\omega H_{\rm ref},\quad
DH_{\rm ref}=-H_{\rm ref}.
\tag{12}
$$
该向量与 R466 的 $k=4$ 线归一化后完全相等。其固定真实曲线为
$$
\boxed{E_{668168}:y^2=x^3+668168,\qquad668168=8\cdot17^4.}
\tag{13}
$$
R466 的完整角色表给 $D_k=8(-17)^k$、
$N_7=\omega^{2k-2}$、$D_{33}=(-1)^{k+1}$。
$k=1$ 的 $E_{-136}$ 具有 $D_{33}=+1$、$N_{19}=+\omega$，
所以它不是本篇的参考线。这里使用的是 R466 已付的完整
一维算术身份及非零质量给出的秩零结论，不是用两个好素数的相位猜曲线。

当前普通 core 规范为
$$
\lambda=-\bar\pi_0^{-1},\qquad \kappa=p/\bar\pi_0^2,\qquad
d=p-1,\qquad K_{136}=-N_7^9.
$$
故 (5) 中每个实际来源都具有完整 core $-\lambda$。特别
$$
J_{H_{\rm ref}}(0)=1+\lambda,
\tag{14}
$$
它由 R410 在当前射线上为单位；$J'_{H_{\rm ref}}(0)$ 仍是
未知中央导数，没有在本篇中被赋零。

## 3. Xi 的整个 D33 负块

令 $\Xi_b(2z)$ 是 R465 第二真实态的完整 $2Y_s$ 边际。
它保 R465 原四挠常数 $c_t^8=(e-h)/(12h^2f^2)$ 以及所有
Gaussian 中心。定义固定七次以下多项式
$$
\boxed{
\begin{aligned}
P(t)=\frac5{1332}\bigl[
 &-4+(3-\delta)t-4\delta t^2+(-4+2\delta)t^3\\
 &+(3+\delta)t^4+(-6-2\delta)t^5+(-7+\delta)t^6
\bigr].
\end{aligned}}
\tag{15}
$$
准确全函数身份为
$$
\boxed{\mathcal Z\Xi_b(2z)=P(N_7)W_{*,b},}
\tag{16}
$$
$$
\boxed{
D_-\Xi_b(2z)
=P(N_7)W_{*,b}
-\frac{1+\delta}{2016b}\,H_{{\rm ref},b}.
}
\tag{17}
$$
证明在 $b=1$ 的 (2) 全部二十三坐标中进行：先由 R465 的全四挠
多项式计算左侧，再用 (9) 的七列求唯一坐标，所得恰为 (15)；
余下的一维向量恰为 (11) 的显示倍数。脚本逐个坐标验证等式，
以及八列秩、(9)、(10) 和参考的 (12)。由同一 homogeneity，
$$
\Xi_b(2z)=b^{-1}\Xi_1(2b^{1/6}z),\quad
W_{*,b}(z)=b^{-1}W_{*,1}(b^{1/6}z),\quad
H_{{\rm ref},b}(z)=H_{{\rm ref},1}(b^{1/6}z),
\tag{18}
$$
得到一般 $b$ 的 (16)、(17)。这也解释了参考项中的 $b^{-1}$。

完整质量逐项为

| $j$ | $(N_7^jW_{*,b})(0)$ |
|---:|---:|
| $0$ | $0$ |
| $1$ | $(-37/1120+37\delta/3360)/b$ |
| $2$ | $(37/1120+37\delta/1120)/b$ |
| $3$ | $0$ |
| $4$ | $37\delta/(1680b)$ |
| $5$ | $-37\delta/(1680b)$ |
| $6$ | $0$ |

所以
$$
(P(N_7)W_{*,b})(0)=\frac{1+\delta}{2016b},
\qquad (D_-\Xi_b(2\cdot))(0)=0.
\tag{19}
$$
参考项确实消掉该质量；这不是说它的导数也消掉任意来源的导数。

在新线上的检查为
$$
P(\omega^2)=-\frac5{222},\qquad
P_{\rm new}W_*=-\frac{3848}{5}S_{\rm new},
$$
$$
\boxed{P_{\rm new}\Xi_b(2z)=\frac{52}{3}S_{\rm new}(z).}
\tag{20}
$$
这里必须保 R470 的整个十八项投影：
$$
P_{\rm new}
=D_-\frac1{18}\sum_{j=0}^{17}\omega^jN_7^j
=\frac{I-\omega N_{19}}{36}
  \sum_{j=0}^{17}\omega^jN_7^j
\quad\text{在 principal 空间上。}
\tag{21}
$$
第二式的 $N_{19}$ 因子是在已选 $N_7=\omega^2$ 空间上读取。
只有先限制到 $N_7^9=1$ 才能将十八项缩成九项。

## 4. 原五伴随下的整八维分解

保 R465 的同一完整坐标
$$
L=(2Y_s,2Q_s,2U_s,R_1,R_2,R_3),\qquad
Y=2Y_s,\qquad \mathbf Z=(2Q_s,2U_s,R_1,R_2,R_3).
\tag{22}
$$
两态 $L_*\rho_i$ 都属于已经付清半特征与中心的同一个整张量格，
其 degree 为
$$
(136,3480,1020,60,2310,4466).
\tag{23}
$$
令 $\Pi_0$ 只在第一轴取几何 principal 投影。由 (7)、(9)、(12)，
存在唯一五变量全来源 $\Lambda_{\rm ref},\Lambda_0,\ldots,\Lambda_6$
使完整联合等式为
$$
\boxed{
(D_-\Pi_0\otimes I_5)L_*\rho_1
=\nu_{H_{\rm ref}}\otimes\nu_{\Lambda_{\rm ref}}
+\sum_{j=0}^6\nu_{N_7^jW_*}\otimes\nu_{\Lambda_j}.
}
\tag{24}
$$
各 $\Lambda$ 处于 (23) 的后五因子。这是整个 theta 张量的系数
分离，没有先令五个伴随等于零。

### 4.1 系数提取在当前射线上整

在 $b=1$，令 $B$ 的八列依次为
$$
(H_{\rm ref},W_*,N_7W_*,\ldots,N_7^6W_*)
$$
在 (2) 中的完整坐标。取行 $j=22,21,\ldots,15$，所得
$8\times8$ 子矩阵可逆。其逆矩阵的准确共同分母是
$$
2^{22}3^{11}5^2\cdot7\cdot13\cdot19\cdot23
 \cdot29^2\cdot37^3\cdot41\cdot53\cdot61.
\tag{25}
$$
脚本给出整个逆矩阵及八个系数泛函，并验证
$$
\ell B=I_8,\qquad B\ell D_-=D_-.
\tag{26}
$$
当前 $p>19$、$p\equiv7\bmod64$ 强制 $p\ge71$，所以 (25) 的
全部因子都是单位，不需新增素数例外。

一般 $b$ 的第 $j$ 行乘 $b^{22-j}$，后七列再乘 $b^{-1}$；
其逆只增添 $b$ 的幂。$b=17$ 在当前普通处也为单位。
原 R413/R465 整 theta 基按互异首阶提取系数，保整 Amice 格；
把 (26) 应用于这个完整整张量便得
$$
\boxed{\nu_{\Lambda_{\rm ref}},\nu_{\Lambda_0},\ldots,
       \nu_{\Lambda_6}\text{ 全部为有界整测度。}}
\tag{27}
$$
这里用有限 theta 基的整提取，不用除高阶阶乘推断整性。

令 $p_j=[t^j]P(t)$。忘掉五伴随后，(17) 与唯一性准确给
$$
\Lambda_{\rm ref}(0)=-\frac{1+\delta}{2016b},\qquad
\Lambda_j(0)=p_j.
\tag{28}
$$
不同 $\Lambda_j$ 没有因此变成同一个函数，也没有得到
$\Lambda_j=p_j\Lambda$。这样的替换会丢掉原五输入信息。

R465 第一态的整个 principal 第一轴位于 $N_7^9=-1$；
由 (5) 得更完整的消失：
$$
\boxed{(D_-\Pi_0\otimes I_5)L_*\rho_0=0.}
\tag{29}
$$
这消掉第一态的整个八维块，不仅消掉某个边际。

最后令 $\Lambda_{\rm old}$ 表示 R465 已定义的实际五伴随来源，
$P_{\rm new}L_*\rho_1=S_{\rm new}\otimes\Lambda_{\rm old}$、
$\Lambda_{\rm old}(0)=52/3$。对 (24) 施加 (21)，得完整五变量等式
$$
\boxed{
\Omega:=\sum_{j=0}^6\omega^{2j}\Lambda_j
=-\frac5{3848}\Lambda_{\rm old},\qquad \Omega(0)=-\frac5{222}.
}
\tag{30}
$$
这是已付的共同伴随组合；本篇不把其余六个独立组合删除。

## 5. 同一 norm-two 联合给出的新增伴随提升

R477 的实际两输入来源为
$$
\widetilde\Phi(y,v)=F_{72}(y+2v)\Theta(4y-9v)^2,
\qquad
F_{72}=\sigma^4\sigma(2\cdot)\sigma(8\cdot),
\tag{31}
$$
属于 $\mathcal S_{136}\boxtimes\mathcal S_{612}$。记
$c_0=-111/280$、$c=5824/3$。其完整身份为
$$
c_0\widetilde\Phi(y,0)=W_*(y),\qquad
P_{{\rm new},Y}\widetilde\Phi
=S_{\rm new}(y)\Lambda_{612}(v),\qquad \Lambda_{612}(0)=c.
\tag{32}
$$
$\nu_{\Lambda_{612}/c}$ 是 R477 的整、质量一伴随；并未在第一轴
做任何反卷积。

用 (24) 的八个不同伴随定义整个七变量来源
$$
\begin{aligned}
\widehat{\mathcal F}_-(y,v,\mathbf z)
={}&H_{\rm ref}(y)\frac{\Lambda_{612}(v)}c
                   \Lambda_{\rm ref}(\mathbf z)\\
&+c_0\sum_{j=0}^6
 (N_{7,Y}^{\,j}\widetilde\Phi)(y,v)\Lambda_j(\mathbf z).
\end{aligned}
\tag{33}
$$
所有算子均为实际完整纤维迹，并作用于第一轴，保 $v,\mathbf z$。
(27)、(31)–(32) 保证 (33) 是有界整的固定 theta 来源。
它忘掉 $v$ 后**准确**返回 (24)，所以任意原 $(Y,\mathbf Z)$
测试都能通过这个明确的新增坐标推前，而不只是通过边际质量。

对 (33) 的第一轴施加 (21)，参考项为零，另七项由
$P_{\rm new}N_7^j=\omega^{2j}P_{\rm new}$ 和 (30) 给
$$
\boxed{
P_{{\rm new},Y}\widehat{\mathcal F}_-
=S_{\rm new}(y)\,
\frac{\Lambda_{612}(v)}c\,\Lambda_{\rm old}(\mathbf z).
}
\tag{34}
$$
常数准确使用
$$
c_0c=-\frac{3848}{5},\qquad
c_0\Omega=\frac1c\Lambda_{\rm old}.
\tag{35}
$$
故对任意完整连续六伴随测试 $h(V,\mathbf Z)$，
$$
\begin{aligned}
&\int_{Y\ {\rm unit}}\langle Y\rangle^{du}
 h(V,\mathbf Z)\,d\nu_{P_{\rm new}\widehat{\mathcal F}_-}\\
&\qquad =
J_{\rm new}(u)\,
(\nu_{\Lambda_{612}/c}\otimes\nu_{\Lambda_{\rm old}})(h).
\end{aligned}
\tag{36}
$$
R466/R469 识别的是同一 $E_{2312}$ 来源，所以当反证输入为
$J'_{\rm new}(0)=0$ 时，(36) 的全部这些完整伴随中央导数确为零。
等式没有把投影前的原独立六 sigma 事件与投影后的来源相认。

R480 将 (33) 中的第一轴 CM7/19 通过同一两输入的同时 CM
身份移到新增的 $V$ 轴；该操作需要两个原输入各自的完整 CM
特征及绝对逆迹规范，不能仅由本篇的七维边际身份推出。

## 6. 中央测试及原 T 管仍保留的准确运输

从 (24) 直接得到任意五伴随测试 $h$ 的完整中央函数
$$
\begin{aligned}
&\int_{Y\ {\rm unit}}\langle Y\rangle^{du}h(\mathbf Z)\,
 d[(D_-\Pi_0\otimes I_5)L_*\rho_1]\\
&=J_{H_{\rm ref}}(u)\nu_{\Lambda_{\rm ref}}(h)
 +\sum_{j=0}^6J_{N_7^jW_*}(u)\nu_{\Lambda_j}(h).
\end{aligned}
\tag{37}
$$
原 $(Y,\mathbf Z)$ 的完整等式允许所有这样的 $h$；
它没有把右边八个中央函数分别赋零。

每个 $N_a$ 的第一单位测试仍按 R470 的实际 CM 纤维运输。
对 canonical 分支
$$
G_{a,t}(y,\mathbf z)
=(\mathsf T_{\bar at}^{(136)}F)(\bar ay,\mathbf z),
\qquad t\in E[a],
$$
有
$$
\nu_{N_aF}
=a^{-1}[a^{-1},I]_* \sum_{t\in E[a]}\nu_{G_{a,t}},
$$
$$
J_{N_aF}(u)
=a^{-1}\langle a\rangle^{-du}
 \sum_{t\in E[a]}J_{G_{a,t}}(u).
\tag{38}
$$
所有中心相位包含在 $\mathsf T$ 中。取导数时每一项都保留
$-d\log\langle a\rangle J_{G_{a,t}}(0)$；(19) 的非零质量
说明不能预先丢掉这些尺度项。

R465 的原 $T$ 输出在 (22) 中是
$$
W_{\rm old}
=\frac{37+3\delta}{68}Y
+ \frac{1-3\delta}{60}Z
+ \frac{-31+3\delta}{510}V_{\rm old},
\tag{39}
$$
其中 $Z=2Q_s$、$V_{\rm old}=2U_s$，与 (31) 新增的 $V$ 不同。
一个实际 CM 及角分支 $(a,\zeta)$ 把旧深管测试变成
$$
\frac{37+3\delta}{68}\frac{\zeta}{a}Y
+ \frac{1-3\delta}{60}Z
+ \frac{-31+3\delta}{510}V_{\rm old}
\in p^n\mathbf Z_p.
\tag{40}
$$
所以 (39) 不是 (36) 中独立于 $Y$ 的伴随条件。R465 的真实
$\mathcal A_W$ 缩放还同时改变 $Y$；将它移到新提升 (33)
之前，须按整个联合运输并保新 $V$ 的 theta 交叉与中心相位。
(16)、(24)、(34) 没有允许先施投影再把未投影的 $W$ 限制
原样放回。当前真实新增结果是原混合 core 后的完整来源桥，
以及有实际两输入表示的整六伴随中央行；所述混管补偿仍未删除。

## 依赖

- [R465：原共同六 sigma 与完整五伴随](R465-original-common-six-sigma-core-and-new-conditional-central-row.md)。
- [R466：完整有限角色和新秩二曲线](R466-fixed-two-division-sources-and-new-rank-two-sextic-curve.md)。
- [R470：原负来源、整个十八项投影和真实 CM 测试](R470-original-riemann-negative-source-and-explicit-new-line.md)。
- [R471：实际 norm-two 六 sigma 因式](R471-original-six-sigma-normtwo-factor-and-complete-input-carry.md)。
- [R477：同一新线的 degree612 完整伴随](R477-original-new-line-and-complete-degree612-companion.md)。
