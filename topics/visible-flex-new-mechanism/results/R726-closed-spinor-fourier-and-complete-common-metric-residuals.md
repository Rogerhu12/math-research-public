# R726　严格闭合傅里叶纬圈与完整同一度量残差

对 [R725 的真实闭曲线坐标](R725-closed-latitude-coordinates-and-one-common-radial-metric.md) 给出一个有限实系数输入。完整材料圈的周长、周期、角原函数和误差各角模均能准确表示。全部公式使用同一个外圈固定的材料角。

## 单位复系数与真端口

取 $K\ge0$，每半径有两列复系数 $A_k,B_k$（$0\le k\le K$），分别满足 $\sum|A_k|^2=\sum|B_k|^2=1$。置
$$
 a=\sum A_k\cos[(k+\tfrac12)\psi],\quad b=\sum B_k\sin[(k+\tfrac12)\psi],\quad
 V_y=|a|^2-|b|^2,\quad V_x+iV_z=2a\overline b,\quad J=|a|^2+|b|^2 .
$$
逐点 $|V|^2=J^2$。须验证 $J>0$，即两函数无共同零。$a,b$ 反周期，$V,J$ 为最高 $d=2K+1$ 的整数三角多项式；$V_{x,z}$ 奇，$V_y,J$ 偶。半整频正交给 $\langle|a|^2\rangle=\langle|b|^2\rangle=1/2$，因此 $\langle V\rangle=0,\langle J\rangle=1$。令 $I$ 将每个非零整数频率除以 $in$、常模置零，置
$$
 \Gamma=I(V),\quad\Phi=\psi+I(J-1)(\psi)-I(J-1)(0),\quad
 M=\langle\Gamma J\rangle,\quad U=\Gamma-M .
$$
$\Phi_\psi=J$，升向满圈逆为 $\Psi$。真实 $F(r,\varphi)=C(r)+rU(r,\Psi(r,\varphi))$ 严格闭合，$F_\varphi/r=V/J$，周长 $2\pi r$，$C$ 为弧长重心。$M$ 是有限卷积的零频。

对实 $(2K+1)$ 向量 $z$ 令 $\sigma=|z|^2$，立体参数 $((1-\sigma)/(1+\sigma),2z/(1+\sigma))$ 具有单位范数，两组各自经固定实正交变换后配为复系数，正分母均至少 1。外平圈可取 $A_0=1,B_0=-1$，内倾平圈取 $B_0=-e^{i\vartheta}$，对应第二实坐标的参数 $-\tan(\vartheta/2)$。有限实参数中的潜在共同相位和其他小奇异方向须完整分解或严格消元。使用复步求实坐标导数时，必须以 $a_R^2+a_I^2$、$2(a_Rb_R+a_Ib_I)$、$2(a_Ib_R-a_Rb_I)$ 等实多项式作全纯延拓；复步后直接共轭微扰会丢导数。

[R680](R680-smaller-tilt-offset-cap-and-positive-hoop-curvature-phase-input.md) 真圆基由 $A_0=1,B_0=-e^{iq(r)}$ 给出 $J=1$, $V=(-\cos q\sin\psi,\cos\psi,\sin q\sin\psi)$。内外设对应准确系数、其一二径阶为零，$C'=C''=0$，外 $C=0$。端部 $O(h^3)$ 的曲线增量保这些条件。于是 $\Phi_r=\Phi_{rr}=0$，以 $F,F_r,F_\varphi/r,F_{rr},F_{r\varphi}/r,F_{\varphi\varphi}/r^2$ 顺序，真六 jet 为 $C+rQe_r,Qe_r,Qe_\varphi,0,Qe_\varphi/r,-Qe_r/r$。分段立体参数和重心须在每个内部径结保持同一两阶实物迹；采用 $C^2$ 参数和重心即足够。

## 全角同一度量与全点几何

以下 $r$ 导先固定辅助 $\psi$。写 $P=\Phi_r,\ W=C'+U+rU_r,\ T=V/J$。固定材料 $\varphi$ 时 $F_r=W-rPT$。给一条具体的 $E(r)>0$，置
$$
 R_B=W\cdot V-rPJ,\qquad R_A=W\cdot W-r^2P^2-E .
$$
真实 $F_r\cdot T=R_B/J$、$|F_r|^2-E=R_A-2rP R_B/J$。两残差全域为零当且仅当诱导 $E\,dr^2+r^2d\varphi^2$。二者次数均不超过 $2d=4K+2$，直接卷积或至少 $8K+5$ 等距点的完整变换可取全系数。真实反射还需 $C_y\equiv0$，包括两阶径向 jet；此时 $R_B$ 纯奇、$R_A$ 纯偶。一般重心须保全部正余弦和常数。设计可取 $E=\langle W\cdot W-r^2P^2\rangle$ 消去径向误差常模，真实 $E>0$ 和其余全部系数仍须检查。冻结后须以同一 $E$ 重算该常模，不能再拟合。

对 $0<\eta<1$，真实相对 Gram 的算子范数不超过 $\eta$ 恰等价于
$$
 S_\pm=(\eta^2E\pm\eta R_A)J^2\mp2\eta rP R_BJ-R_B^2\ge0 .
$$
这是两个二阶 PSD 的 Schur 补，已清 $J^2$；次数至多 $4d$。也可直接用 $\|R_A\|_\infty/E+(2r\|P\|_\infty/E+1/\sqrt E)\|R_B\|_\infty/\inf J$ 估计真实误差。若原始立体参数、$C$ 逐径段为多项式，则 $V,J,\Gamma,\Phi-\psi,M,U,W$ 的角系数均为 $r$ 有理函数。清两个严格正立体分母的幂即可验证全径段多项式恒等式或不等式；另给有理 $E$ 时也须核其正分母。内倾 $\sin\vartheta=27/100$ 的锚只需代数数 $\cos\vartheta=\sqrt{9271}/100$。若具体参考 $q$ 使用原 R680 的径向积分，则其非多项式部分仍需真实包围，不能借多项式结论。

真实两阶可取 $\gamma=P/J,\ \mathcal D=\partial_r-\gamma\partial_\psi$，有 $F_{rr}=C''+2\mathcal DU+r\mathcal D^2U,\ F_{r\varphi}/r=T/r+\mathcal DT,\ F_{\varphi\varphi}/r^2=T_\psi/(rJ)$。还可直接以辅助 $X=C+rU$ 计算几何。写 $G_{ij}=X_i\cdot X_j,\ n_0=X_r\times X_\psi,\ \Delta=\det G=|n_0|^2,\ H_{ij}=n_0\cdot X_{ij}$。若 $\Delta>0$，两主曲率绝对值都小于 $1/\tau$ 恰等价于
$$
 \mathcal P=\Delta^2G-\tau^2H\,\operatorname{adj}(G)H\succ0 .
$$
理由是 $G^{-1}H/\sqrt\Delta$ 关于 $G$ 自伴，其平方的二次型严格小于 $G/\tau^2$。故核 $\mathcal P_{11}>0,\det\mathcal P>0$ 足够，亦适用重主曲率。次数依次为 $G\le2d,\Delta\le4d,H\le3d,\mathcal P\le10d,\det\mathcal P\le20d$。双正图门 $n_0\cdot e_z>0,n_0\cdot Qe_z>0$ 至多 $2d$。反射下这些标量和 $S_\pm$ 都偶，代 $x=\cos\psi$，用 $\cos(n\psi)=T_n(x)$、$\sin(n\psi)=\sin\psi\,U_{n-1}(x)$ 与 $\sin^2\psi=1-x^2$ 可化成每个径段乘 $[-1,1]$ 的双变量符号题。带向外舍入的 Bernstein 包围和细分可证严格正，若恰触零需另证非负。实际内外刚帽、净空、全像支撑与固定握持仍要核 [R662](R662-tilted-two-plane-global-tube-and-offset-cap-clearance.md) 和 R680 的全部条件。

在 R680 特例，$F_\alpha(r,\varphi)=R_z(\alpha)F(r,\varphi-\alpha)$，外帽固定；内刚件施 $R_z(\alpha)Q R_z(-\alpha)Q^{-1}$ 及真实中心平移。取 $\Psi(r,\varphi-\alpha)$ 后才施刚转，故基相位全角的同一 $E$ 界覆盖全部 $\alpha$。一般真实路径须同时遍历 $(t,\psi)$，冻结一条 $E$ 并在所有参数精化中保持它。

## 从真正闭圈取半整频系数

设已经准确归一的正则反射圈速度 $V_0$ 满足 $\langle V_0\rangle=0,\langle|V_0|\rangle=1$，在 $0,\pi$ 的单位切向为 $+e_y,-e_y$。令 $n=V_0/|V_0|$，取
$$
 \Pi=\tfrac12\begin{pmatrix}1+n_y&n_x+in_z\\ n_x-in_z&1-n_y\end{pmatrix},\qquad
 q'=[\Pi',\Pi]q,\quad q(0)=(1,0)^t .
$$
交换子反 Hermitian，保单位范数；由 $\Pi^2=\Pi$ 得 $[[\Pi',\Pi],\Pi]=\Pi'$，故 $\Pi q=q$。$D=\operatorname{diag}(1,-1)$ 满足 $\Pi(-\psi)=D\Pi(\psi)D$。$0$ 点 $Dq=q$，$\pi$ 点 $-Dq=q$。由 ODE 唯一性，$q(-\psi)=Dq(\psi),q(2\pi-\psi)=-Dq(\psi)$。因而 $q$ 反周期，第一分量偶、第二奇。乘 $\sqrt{|V_0|}$ 后外积为 $|V_0|\Pi$，前节二次式重得 $V_0$。两系数列的范数由闭合和总周长恰给 1。若所需角、径混合导足够光滑，半整频截断及再归一一致逼近；各径导的 $\sum_{k>K}(k+1/2)^j(|A_k|+|B_k|)$ 控制其 $j$ 阶角尾。归一分母须离零，所选立体极点须避开整个系数路径。仅 $L^2$ 收敛不足以控制曲率。

自然 R703 run 46151140087 / job 140997832329，源 1b2ba533d51b4f4b416d30dcee1aaa516b2c64be，FINAL 原字面 39163 字节 / bd5a52dcc40e31e898d3e02b99e4e5c0d449bfd697ac95faa8a168082c6012b2。原 157 系数、K5/12、材料级 1、无冻结 $E$，原 448.583230591 秒、63 完整 J/QR、91 次试步均保。FINAL 未保存每径每角的旧原函数。后继须一次验自然对象，明确旧参考角数和径网（原双细为 289 角、9 阶），只为新坐标重建必要的真实有限曲线/两径 jet。离散投影传播 $\Pi_jq_{j-1}/|\Pi_jq_{j-1}|$ 是一个逐节点的相位选择，不是上述连续 ODE 的精确积分。须记录相邻重叠、反射改量、正速、两组单位化、傅里叶截断、径样条拟合、旧中心两侧迹/新 $C^2$ 拟合及同一材料 $\varphi$ 反求后的两套真六 jet、两径角读数、全壳与费用。取已完成参数不等于已经持有旧全场数组。

## 圆纬圈的必要角度与重心消元

$K=0$ 给 $J=1$，只有圆纬圈。更一般设真实圆纬圈 $F=C+rP_0$，$P_0=e_1\cos\varphi+e_2\sin\varphi$，标架角速度 $\omega$、平面法向 $n=e_1\times e_2$。此时 $F_r=C'+P_0+r(\omega\times P_0)$。$\omega\times P_0=(\omega\cdot n)T+[(\omega\times P_0)\cdot n]n$，所以 $|F_r|^2$ 的第二角谐波振幅正好 $r^2|n'|^2/2$；任意 $C'$ 和标架绕 $n$ 的自转只影响常量和一次项。取相反两角平均消一次项，再与 $\pi/2$ 移位比较得 $r^2|n'|^2\le2\eta E$。若内外平面夹角 $\vartheta$、$S=\int\sqrt E\,dr$，则 $\vartheta\le\sqrt{2\eta}\int\sqrt E\,dr/r\le\sqrt{2\eta}\,S/r_{\min}$。准确等距圆纬圈不能改变平面法向；以 $r_{\min}=.075$, $\vartheta=\arcsin(.27)$, $S\le.1515$，必要 $\eta>.0089$。此门约束圆族，不足以排除更高模式。

另记 $W_0=U+rU_r,\ c=C'$。全部 $R_B$ 和全部非恒 $R_A$ 关于 $c$ 仿射，分别为 $W_0\cdot V-rPJ+c\cdot V$ 和 $\Pi_{\ne0}(|W_0|^2-r^2P^2)+2c\cdot\Pi_{\ne0}W_0$。堆叠全部 Fourier 行成 $Mc+d_0$，则确切形状兼容须有 $-d_0\in\operatorname{range}M$。反射时每径至多两列，任何小方向都保；一般为三列。若 $E$ 已冻结，还须
$$
 |c+\langle W_0\rangle|^2
 = E-\langle|W_0-\langle W_0\rangle|^2-r^2P^2\rangle .
$$
即上述仿射解集与一圆（一般三维为球）相交。平端反射的非恒行只锁一个水平方向，$E=1$ 再迫 $c=0$。点态相交仍须径向光滑选支、积分实际 $C$ 并支付帽位及全壳。若声明有限中心样条，所有非恒行对其整段系数仍线性，可作全列投影；点态自由 $c$ 不能用作有限空间或两端积分资格。

配套两个模块给出精确三角构造的普通浮点评估与一次性源转换接口。其浮点原函数会弃常模，实际插值的 $\Phi_\psi=1+J-\langle J\rangle$、$U_\psi=V-\langle V\rangle$ 还受变换舍入。零、一、二径阶质量/速度均值和原生角导差均单列，完整真有限插值两阶须用自己的 $\Phi_\psi,U_\psi$ 计算。标量/系数的普通误差不等于有向区间证明。本篇和模块发布时**未执行新科学**，并未冻结实际共同度量或完成 README 所求全族。
